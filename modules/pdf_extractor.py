# modules/pdf_extractor.py

import fitz  # PyMuPDF

def extract_arabic_text(pdf_path):
    """
    هذه الدالة تقوم باستخراج النص العربي من ملف PDF.
    :param pdf_path: مسار ملف PDF
    :return: نص كامل من الملف
    """
    try:
        # افتح ملف الـ PDF
        pdf_document = fitz.open(pdf_path)
        text = ""

        # استخرج النص من كل صفحة
        for page in pdf_document:
            text += page.get_text("text")  # نص خام

        pdf_document.close()
        return text

    except Exception as e:
        print(f"حدث خطأ أثناء معالجة الملف: {e}")
        return ""