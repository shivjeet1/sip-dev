import cv2
import pytesseract
from file_manager import save_text

def capture_and_ocr(lang='eng'):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    print("Press 'c' to capture an image and perform OCR. Press 'q' to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
        
        cv2.imshow("Press 'c' to Capture", frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('c'):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray, lang=lang)
            print("Extracted Text:\n", text)
            save_path = "captured_text.txt"
            save_text(text, save_path, "txt")
            print(f"OCR completed. Output saved at {save_path}")
        
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_ocr()

