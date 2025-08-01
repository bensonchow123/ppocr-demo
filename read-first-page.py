from paddleocr import PaddleOCR
import os
from pdf2image import convert_from_path
import numpy as np

ocr = PaddleOCR()

pdf_dir = "pdf-examples"
output_dir = "output"

os.makedirs(output_dir, exist_ok=True)

pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]

for pdf_file in pdf_files:
    print(f"Processing: {pdf_file}")
    
    pdf_name = os.path.splitext(pdf_file)[0]
    pdf_output_dir = os.path.join(output_dir, pdf_name)
    os.makedirs(pdf_output_dir, exist_ok=True)
    
    pdf_path = os.path.join(pdf_dir, pdf_file)
    
    # Convert only the first page to image
    images = convert_from_path(pdf_path, first_page=1, last_page=1)
    
    if images:
        # Convert PIL image to numpy array
        image_array = np.array(images[0])
        
        # Process only the first page image
        result = ocr.predict(input=image_array)
        
        if result:
            res = result[0]
            img_filename = f"{pdf_name}_visualisation.png"
            img_path = os.path.join(pdf_output_dir, img_filename)
            res.save_to_img(img_path)
            res.save_to_json(pdf_output_dir)
    
    print(f"Completed: {pdf_file}")

print("All PDFs processed!")

