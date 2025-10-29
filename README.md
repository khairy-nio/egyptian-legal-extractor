# 🏛️ Egyptian Legal Extractor

A Flask-based web application for extracting and converting Arabic legal PDF files into structured **CSV datasets**, ready for use in **machine learning** and **NLP training**.  
Inspired by datasets like [Egyptian Constitution and Labor Laws](https://www.kaggle.com/datasets/hemalone/egyptian-constitution-and-labor-laws).

---

## 🚀 Features

- 📤 Upload one or multiple Arabic **PDF files**
- 🔍 Automatically extract and clean Arabic text using **PyMuPDF**
- 🧹 Smart text organization into **titles**, **paragraphs**, and **content**
- 📊 Generate a **clean CSV file per document**
- ⚙️ Built with **Flask**, easy to deploy and extend

---

## 🧠 Use Cases

- Building Arabic **legal NLP datasets**
- Training **AI models** for text classification or document summarization
- Digitizing **Egyptian law and legislation**

---

## 🧩 Tech Stack

| Component | Description |
|------------|--------------|
| **Python 3.10+** | Core language |
| **Flask** | Web framework |
| **PyMuPDF (fitz)** | PDF text extraction |
| **Pandas** | CSV creation and formatting |

---

## 🗂️ Project Structure

egyptian-legal-extractor/
│
├── app.py                   # Flask main server
├── modules/
│   ├── pdf_extractor.py     # Handles PDF to text extraction
│   ├── csv_generator.py     # Converts extracted text to CSV
│
├── templates/
│   └── index.html           # Upload UI
│
├── uploads/                 # Uploaded PDFs
├── processed/               # Output CSVs
└── README.md                # Project documentation

---

## ⚙️ Setup & Run

### 1️⃣ Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Flask app
python app.py

4️⃣ Access the app

Go to: http://127.0.0.1:5000

⸻

🧾 Output Example

Each uploaded PDF is processed into a CSV file like this:
title
paragraph
content
الدستور المصري
الباب الأول
جمهورية مصر العربية دولة نظامها ديمقراطي…
