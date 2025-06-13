# 📊 Analytics AI – AI-Powered Data Analysis Tool

**Analytics AI** is a user-friendly, Streamlit-based web application that uses **Groq AI (LLaMA 3 model)** to help you analyze your CSV and Excel datasets using natural language questions.

> 🔍 Upload your data → Ask a question → Get insights powered by AI!

---

## 🚀 Features

* 📁 Upload CSV, XLSX, or XLS files
* 🧠 Ask data-related questions in natural language
* 📈 Get AI-generated insights with statistics and summaries
* 🧮 View descriptive statistics, column types, and missing values
* 🤖 Powered by [Groq LLaMA3-70b](https://groq.com/) for high-speed AI processing

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/analytics_ai.git
cd analytics_ai
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 📂 File Structure

```
analytics_ai/
├── app.py               # Main Streamlit application
├── .env                 # API Key (not committed)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧠 How to Use

1. Launch the app: `streamlit run app.py`
2. Upload your dataset (CSV or Excel)
3. Explore:

   * View data preview
   * Check dataset shape and data types
   * See statistical summaries
   * Check missing values
4. Ask questions like:

   * "What are the key trends?"
   * "What's the average salary by department?"
   * "Which columns are most correlated?"

---

## 📌 Example Questions

* What are the top 5 most frequent values in column X?
* What is the average, min, and max of column Y?
* Show trends based on year or category.
* Which columns have missing values?

---

## 📦 Dependencies

* `streamlit`
* `pandas`
* `chardet`
* `groq`
* `python-dotenv`

Install with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Notes

* CSV files should preferably be UTF-8 encoded.
* Avoid uploading very large datasets (recommended < 10MB).
* Requires a valid Groq API key to access the LLaMA 3 model.

---

## 🙌 Acknowledgments

* [Groq](https://groq.com/) – for providing blazing-fast inference with LLaMA 3.
* [Streamlit](https://streamlit.io/) – for easy web app deployment.
* Open-source community for continuous inspiration.

---

## 👨‍💻 Author

**Prince Thummar**
Connect with me on [GitHub](https://github.com/PrinceThummar011)
