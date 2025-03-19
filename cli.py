import argparse
from ocr_engine import extract_text
from file_manager import save_text

def main():
    parser = argparse.ArgumentParser(description="OCR CLI Tool - Extract text from images")
    parser.add_argument("image", help="Path to the image file (JPG, JPEG, PNG)")
    parser.add_argument("-l", "--lang", default="eng", help="Language for OCR (default: eng)")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("-f", "--format", choices=["txt", "pdf", "docx", "doc"], default="txt", help="Output file format")
    args = parser.parse_args()
    
    extracted_text = extract_text(args.image, args.lang)
    
    if args.output:
        save_text(extracted_text, args.output, args.format)
        print(f"OCR completed. Output saved as {args.format} at {args.output}")
    else:
        print("Extracted Text:\n")
        print(extracted_text)

if __name__ == "__main__":
    main()

