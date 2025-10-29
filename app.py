from flask import Flask, render_template, request, send_file
import os
import fitz  # PyMuPDF
import pandas as pd
import re

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def clean_text(text):
    """تنظيف النص من الرموز الغريبة"""
    text = re.sub(r'[^\u0600-\u06FF\s\d،.؟:؛\-]+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_articles_from_pdf(pdf_path):
    """تحويل نص PDF إلى مواد منظمة"""
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text("text") + "\n"
    doc.close()

    full_text = clean_text(full_text)
    articles = re.split(r'\bمادة\s*\d*', full_text)
    data = []

    for i, art in enumerate(articles):
        art = art.strip()
        if len(art) > 30:
            title_match = re.match(r'([^\n]{0,50})', art)
            title = title_match.group(1).strip() if title_match else f"مادة {i}"
            data.append({
                "Article_No": f"مادة {i}",
                "Title": title,
                "Content": art
            })
    return data

@app.route("/", methods=["GET", "POST"])
def upload_and_process():
    if request.method == "POST":
        files = request.files.getlist("files")
        processed_files = []

        for file in files:
            if file and file.filename.endswith(".pdf"):
                upload_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(upload_path)

                print(f"📘 معالجة الملف: {file.filename}")
                data = extract_articles_from_pdf(upload_path)

                if data:
                    csv_name = os.path.splitext(file.filename)[0] + ".csv"
                    output_csv = os.path.join(PROCESSED_FOLDER, csv_name)
                    df = pd.DataFrame(data)
                    df.to_csv(output_csv, index=False, encoding="utf-8-sig")
                    processed_files.append(csv_name)

        if not processed_files:
            return render_template("index.html", message="❌ لم يتم استخراج أي بيانات من الملفات.")

        return render_template("index.html", processed_files=processed_files)

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    path = os.path.join(PROCESSED_FOLDER, filename)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "❌ الملف غير موجود."

if __name__ == "__main__":
    app.run(debug=True)