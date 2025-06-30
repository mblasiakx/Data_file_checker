from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text_form_file(text, chunk_size=500, overlap=100):
    split = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return split.split_text(text)
