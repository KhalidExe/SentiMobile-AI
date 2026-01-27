import pandas as pd
from flask import Flask, render_template, request, send_file, jsonify
from textblob import TextBlob
import collections
import random
import io

app = Flask(__name__)

def get_analysis(text):
    if not isinstance(text, str): text = str(text)
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    
    if polarity > 0.1: sent_type = 'Positive'
    elif polarity < -0.1: sent_type = 'Negative'
    else: sent_type = 'Neutral'
    
    return sent_type, polarity, subjectivity

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze_file', methods=['POST'])
def analyze_file():
    file = request.files.get('file')
    if not file: return jsonify({"error": "No file uploaded"}), 400
    
    try:
        if file.filename.endswith('.csv'):
            try:
                df = pd.read_csv(file, encoding='utf-8')
            except UnicodeDecodeError:
                file.seek(0)
                df = pd.read_csv(file, encoding='latin1')
        else:
            df = pd.read_excel(file)
        
        target_col = next((col for col in df.columns if any(x in col.lower() for x in ['review', 'text', 'comment', 'desc', 'body', 'content'])), None)
        
        if not target_col: 
            return jsonify({"error": f"Column not found. Available: {list(df.columns)}"}), 400

        df = df.dropna(subset=[target_col])
        df[target_col] = df[target_col].astype(str)

        results = df[target_col].apply(get_analysis)
        df['Sentiment'] = [r[0] for r in results]
        df['Score'] = [r[1] for r in results]
        df['Subjectivity'] = [r[2] for r in results]
        
        summary = df['Sentiment'].value_counts().to_dict()
        for cat in ['Positive', 'Neutral', 'Negative']: summary.setdefault(cat, 0)

        avg_score = df['Score'].mean()
        star_rating = round((avg_score + 1) * 2.5, 1)
        star_rating = max(0.0, min(5.0, star_rating))

        pos_samples = df[df['Sentiment'] == 'Positive'].sort_values(by='Score', ascending=False)[target_col].head(5).tolist()
        neg_samples = df[df['Sentiment'] == 'Negative'].sort_values(by='Score', ascending=True)[target_col].head(5).tolist()
        neu_samples = df[df['Sentiment'] == 'Neutral'][target_col].head(5).tolist()
        
        mis_df = df[(df['Score'].abs() < 0.1) & (df['Subjectivity'] > 0.5)]
        mismatch = mis_df[target_col].head(5).tolist() if not mis_df.empty else df[(df['Score'].abs() < 0.05)][target_col].head(5).tolist()

        pos_samples = pos_samples if pos_samples else ["No positive reviews found."]
        neg_samples = neg_samples if neg_samples else ["No negative reviews found."]
        neu_samples = neu_samples if neu_samples else ["No neutral reviews found."]
        mismatch = mismatch if mismatch else ["No edge cases detected."]

        all_text = " ".join(df[target_col]).lower()
        words = all_text.split()
        stop_words = {'the', 'and', 'is', 'it', 'to', 'of', 'in', 'for', 'with', 'on', 'that', 'this', 'was', 'my', 'at', 'as', 'but', 'are', 'be', 'have', 'not', 'you', 'very', 'good'}
        common_words = collections.Counter([w for w in words if w.isalpha() and len(w) > 3 and w not in stop_words]).most_common(50)
        word_cloud = [{"text": w[0], "value": w[1]} for w in common_words]

        samples_text = df[target_col].tolist()
        flying_samples = random.sample(samples_text, min(len(samples_text), 30))

        date_col = next((col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()), None)
        has_date = False
        timeline_data, timeline_labels = [], []
        if date_col:
            try:
                df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
                df = df.sort_values(by=date_col)
                daily = df.set_index(date_col).resample('D')['Score'].mean().fillna(0)
                timeline_data = daily.tolist()
                timeline_labels = daily.index.strftime('%Y-%m-%d').tolist()
                has_date = True
            except: pass
        
        if not has_date:
            timeline_data = df['Score'].rolling(window=max(1, len(df)//20)).mean().fillna(0).tolist()
            timeline_labels = list(range(len(timeline_data)))

        df.to_excel("analyzed_result.xlsx", index=False)
        
        return jsonify({
            "status": "success",
            "summary": summary,
            "total": len(df),
            "avg": round(avg_score, 2),
            "subj": round(df['Subjectivity'].mean(), 2),
            "star_rating": star_rating,  
            "word_cloud": word_cloud,
            "timeline_data": timeline_data,
            "timeline_labels": timeline_labels,
            "has_date": has_date,
            "flying_samples": flying_samples,
            "pos_samples": pos_samples,
            "neu_samples": neu_samples,
            "neg_samples": neg_samples,
            "mis_samples": mismatch
        })

    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/download_ready')
def download_ready():
    return send_file("analyzed_result.xlsx", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)