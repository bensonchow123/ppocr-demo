import os
from pathlib import Path
from pdf2image import convert_from_path

pdf_dir = "pdf-examples"

def pdf_first_page_to_png():
    # Create output directory
    output_dir = Path("pdf-first-page-png")
    output_dir.mkdir(exist_ok=True)
    
    # Get all PDF files in the current directory
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s). Converting first pages to PNG...")
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        try:
            # Convert only the first page of the PDF to an image
            images = convert_from_path(pdf_path, first_page=1, last_page=1, dpi=200)

            if images:
                first_page_image = images[0]
                
                # Create output filename
                base_name = Path(pdf_file).stem
                output_filename = output_dir / f"{base_name}_first_page.png"
                
                # Save the image
                first_page_image.save(output_filename, "PNG")
                
                print(f"✓ Converted: {pdf_file} -> {output_filename}")
            else:
                print(f"✗ No pages found in {pdf_file}")
                
        except Exception as e:
            print(f"✗ Error processing {pdf_file}: {str(e)}")
    
    print(f"\nConversion complete! PNG files saved to '{output_dir}' directory.")

if __name__ == "__main__":
    pdf_first_page_to_png()