import pdfplumber
import tempfile
import os


def extract_text_from_file(file):
    text = ""

    if file.name.lower().endswith(".pdf"):
        # Cria arquivo temporário manualmente
        fd, path = tempfile.mkstemp(suffix=".pdf")
        os.close(fd)

        try:
            # Salva o conteúdo do upload no arquivo temporário
            with open(path, "wb") as f:
                for chunk in file.chunks():
                    f.write(chunk)

            # Lê com pdfplumber
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

        finally:
            # Remove o arquivo temporário
            os.remove(path)

    else:
        # Arquivo de texto simples
        file.seek(0)
        text = file.read().decode("utf-8", errors="ignore")

    return text.strip()
