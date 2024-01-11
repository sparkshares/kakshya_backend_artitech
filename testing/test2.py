import os
from PyPDF2 import PdfReader
import json
from pdf2image import convert_from_path
import io
from PIL import Image

def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision

    # Check if the file is a PDF or an image
    if not (path.endswith('.pdf') or path.endswith('.jpg') or path.endswith('.jpeg') or path.endswith('.png')):
        return json.dumps({"error": "We accept only PDF files and image files (.jpg, .png)"})

    client = vision.ImageAnnotatorClient()

    if path.endswith('.pdf'):
        images = convert_from_path(path)
        for i, image in enumerate(images):
            byte_arr = io.BytesIO()
            image.save(byte_arr, format='JPEG')
            byte_arr = byte_arr.getvalue()
            image = vision.Image(content=byte_arr)
            response = client.document_text_detection(image=image)
            process_response(response)
    else:
        with open(path, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = client.document_text_detection(image=image)
        process_response(response)

def process_response(response):
    with open("summary.txt", "a") as summary_file:
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        word_text = "".join([symbol.text for symbol in word.symbols])
                        summary_file.write(f"{word_text} ")

        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )

detect_document("testing/dbms assignment4.pdf")