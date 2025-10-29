import pandas as pd

def segment_text(text, chunk_size=500):
    """
    Split Arabic text into chunks for model training.
    """
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append({
            "Text_Chunk": chunk,
            "Label": ""  # Placeholder for manual labeling later
        })

    df = pd.DataFrame(chunks)
    return df