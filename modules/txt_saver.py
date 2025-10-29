import os

def save_text(text, output_path):
    """
    Saves extracted Arabic text to a .txt file
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

def convert_and_delete_pdf(pdf_path, text, output_folder="converted"):
    """
    Saves extracted text with same name as PDF and deletes original file
    """
    os.makedirs(output_folder, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    txt_path = os.path.join(output_folder, f"{base_name}.txt")

    save_text(text, txt_path)
    os.remove(pdf_path)  # delete the original PDF after converting
    print("DEBUG RESULT:", result)
    return txt_path
