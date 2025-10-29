import re
from utils.stopwords_list import ARABIC_STOP_WORDS

def clean_arabic_text(text):
    """
    تنظيف النص العربي من الرموز والإنجليزية والأرقام والكلمات الشائعة.
    """
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[a-zA-Z0-9\-\(\)\[\]]', '', text)
    text = re.sub(r'[،\.\؟\!\:\؛\"\'\<\>\{\}\*]', ' ', text)
    text = re.sub(r'ـ', '', text)

    words = text.split()
    words = [w for w in words if w not in ARABIC_STOP_WORDS and len(w) > 1]

    return ' '.join(words)