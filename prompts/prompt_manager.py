def build_summary_prompt(document_text):
    if not isinstance(document_text, str):
        raise TypeError("document_text must be a string")

    if document_text.strip() == "":
        raise ValueError("document_text cannot be empty")

    return f"{document_text}"
