# 🧠 SentiMobile AI V3.4 | Neural Sentiment Engine

![Project Status](https://img.shields.io/badge/Status-Stable_V3.4-00ff88?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-white?style=for-the-badge&logo=flask)
![Tailwind](https://img.shields.io/badge/Frontend-Tailwind_CSS-38bdf8?style=for-the-badge&logo=tailwindcss)

> **A Next-Gen Sentiment Analysis Dashboard designed with a Cyberpunk aesthetic.**
> SentiMobile AI processes bulk customer reviews (CSV/Excel), extracts semantic insights, and visualizes data through an interactive, high-performance interface.

---

## 📸 Screenshots
- **HomePage** ![Home Page](screenshots/image.png)
- **Loading** ![Loading Animation](screenshots/image-1.png)
- **ANALYSIS** ![Dashboard](screenshots/image-2.png) ![Charts](screenshots/image-3.png) ![System Analysis](screenshots/image-4.png)

---

## ⚡ Key Features

### 🔍 Core Analysis
- **Bulk Processing:** Upload `.csv` or `.xlsx` files containing thousands of reviews.
- **Sentiment Scoring:** Polarity detection (Positive, Neutral, Negative) using NLP (`TextBlob`).
- **Subjectivity Meter:** Distinguishes between **Factual** statements and **Opinionated** text.
- **Smart Sampling:** Automatically extracts key review samples for each category (including edge cases).

### 📊 Advanced Visualization
- **Cyber-Interface:** A fully responsive, dark-mode UI with neon accents, particle animations, and glassmorphism.
- **Timeline Analysis:** Automatically detects dates to plot sentiment trends over time.
- **Word Cloud:** Generates a dynamic cloud of the most frequent keywords in the dataset.
- **Interactive Charts:** Powered by `Chart.js` (Pie, Line, and Bar charts).

### 🌐 User Experience
- **Bilingual Support:** One-click toggle between **English** and **Arabic** (RTL support).
- **Flying Text Animation:** Visualizes data processing in real-time during upload.
- **Executive Abstract:** AI-generated textual summary and strategic recommendations for Sellers & Buyers.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Pandas, TextBlob.
* **Frontend:** HTML5, Tailwind CSS (CDN), Anime.js, Chart.js.
* **Data Handling:** Pandas, OpenPyXL.

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/SentiMobile-AI.git](https://github.com/YourUsername/SentiMobile-AI.git)
    cd SentiMobile-AI
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

4.  **Access the Dashboard:**
    Open your browser and go to: `http://127.0.0.1:5000`

---

## 📂 Project Structure
SentiMobile-AI/ │ ├── app.py # The Flask Backend & Logic Core ├── requirements.txt # Python Dependencies ├── README.md # Documentation │ ├── templates/ │ └── index.html # The Cyberpunk Frontend (Single File) │ └── static/ # (Optional) For custom assets

---

## 📝 Data Formatting Guide

To ensure the best results, your uploaded file should follow these rules:
1.  **Format:** `.csv` or `.xlsx`.
2.  **Review Column:** Must contain a column named `Review`, `Reviews`, `Text`, `Comment`, or `Body`.
3.  **Date Column (Optional):** If a date column exists (e.g., `Date`, `Time`), the system will generate a timeline chart.

---

## 🔮 Future Roadmap

- [ ] Add deep learning models (BERT/RoBERTa) for higher accuracy.
- [ ] Implement color-coded Word Cloud based on sentiment.
- [ ] Export reports as PDF.

---

*Developed by **KhalidExe** © 2026*