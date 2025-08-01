# PaddleOCR Document Processing Project

This project uses PaddleOCR for AI powered optical character recognition (OCR) on PDF documents. The workflow includes converting PDFs to images and processing them with PaddleOCR to extract text and generate visualizations.

## Project Structure

```
paddleocr/
├── pdf-examples/           # Input PDF files
├── output/                 # OCR results and visualizations
├── input-examples/         # Additional input examples (empty)
├── pdf-to-png.py          # Converts first page of PDFs to PNG
├── read-first-page.py     # OCR processing of PDF first pages
├── fine-tune-rec-module.md # Documentation for fine-tuning
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore file
```

## Features

### 1. PDF to PNG Conversion
- **Script**: [`pdf-to-png.py`](pdf-to-png.py)
- Converts the first page of each PDF to PNG format
- Uses 200 DPI for high-quality conversion
- Outputs to `pdf-first-page-png/` directory

### 2. OCR Processing
- **Script**: [`read-first-page.py`](read-first-page.py)
- Processes PDF documents using PaddleOCR
- Extracts text from the first page of each PDF
- Generates visualization images with bounding boxes
- Saves results as JSON files

### 3. Fine-tuning Documentation
- **Guide**: [`fine-tune-rec-module.md`](fine-tune-rec-module.md)
- Comprehensive documentation for fine-tuning PaddleOCR's recognition module
- Includes dataset preparation, training, evaluation, and model export steps
- Optimized for 3x GPU setup

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. The main dependencies include:
   - `paddleocr==3.1.0`
   - `pdf2image==1.17.0`
   - `pillow==11.2.1`
   - And other supporting libraries

## Usage

### Convert PDFs to PNG
```bash
python pdf-to-png.py
```
This will process all PDF files in the `pdf-examples/` directory and save PNG images to `pdf-first-page-png/`.

### Run OCR on PDFs
```bash
python read-first-page.py
```
This will:
- Process all PDFs in `pdf-examples/`
- Extract text from the first page of each PDF
- Save visualization images and JSON results to `output/`

## Current Dataset

The project currently processes 6 PDF files:
- `CNE-A-0049_-_Combined.pdf`
- `EW-C-A-0003_-_Combined.pdf`
- `EW-C-A-0006_-_Combined.pdf`
- `PMI-A-0009_-_Combined.pdf`
- `PPMI--0057_-_Combined.pdf`
- `PPMI-A-0069 Combined.pdf`

## Output Structure

For each processed PDF, the output directory contains:
```
output/
└── [PDF_NAME]/
    ├── [PDF_NAME]_visualisation.png  # OCR visualization with bounding boxes
    └── [timestamp].json              # OCR results in JSON format
```

## Fine-tuning Capabilities

The project includes comprehensive documentation and all dependency for fine-tuning PaddleOCR's recognition module:
- Dataset preparation using PPOCRLabel
- Pre-trained model download and setup
- Multi-GPU training configuration
- Model evaluation and export procedures

## Dependencies

Key Python packages:
- **PaddleOCR**: Core OCR functionality
- **pdf2image**: PDF to image conversion
- **OpenCV**: Image processing
- **NumPy**: Array operations
- **Pillow**: Image handling

## Next Steps

- Fine-tune the recognition module for better accuracy on your specific document types
- Expand processing to handle multiple pages per PDF
- Implement batch processing optimizations
- Add text post-processing and validation features
