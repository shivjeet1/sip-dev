import sys
import cv2
import easyocr
import numpy as np
from PIL import Image
from docx import Document
from fpdf import FPDF
from PySide6.QtWidgets import ( QApplication, QLabel, QPushButton, QFileDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QWidget, QComboBox )
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QThread, Signal
import signal

reader = easyocr.Reader(['en'], gpu=True)

class OCRThread(QThread):
    result_ready = Signal(str)

    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path

    def run(self):
        result = extract_text(self.image_path)
        self.result_ready.emit(result)

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    enhanced = cv2.equalizeHist(gray)
    return enhanced

def extract_text(image_path):
    processed_image = preprocess_image(image_path)
    if processed_image is None:
        return "Error: Could not process image."
    
    pil_image = Image.fromarray(processed_image)
    results = reader.readtext(np.array(pil_image), detail=0)
    
    return "\n".join(results) if results else "No text detected."

class OCRApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure OCR Tool")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #2b2b2b; color: #ffffff; font-size: 16px;")

        self.main_layout = QHBoxLayout()

        # Left Panel
        self.left_panel = QVBoxLayout()
        self.image_label = QLabel("Drop an image or select one")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("border: 2px dashed #ffffff; padding: 10px; font-size: 16px;")
        self.image_label.setFixedSize(400, 300)
        self.left_panel.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.select_button = QPushButton("Select Image")
        self.select_button.setStyleSheet("background-color: #444; padding: 8px; font-size: 16px;")
        self.select_button.setFixedSize(200, 40)
        self.select_button.clicked.connect(self.load_image)
        self.left_panel.setSpacing(5)
        self.left_panel.addWidget(self.select_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addLayout(self.left_panel)

        # Right Panel
        self.right_panel = QVBoxLayout()
        self.text_heading = QLabel("Extracted Text")
        self.text_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_heading.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.right_panel.addWidget(self.text_heading)

        self.ocr_result = QTextEdit()
        self.ocr_result.setReadOnly(True)
        self.ocr_result.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")
        self.right_panel.addWidget(self.ocr_result)

        self.format_selector = QComboBox()
        self.format_selector.addItems(["Save as TXT", "Save as DOCX", "Save as PDF"])
        self.format_selector.setStyleSheet("background-color: #444; padding: 5px; color: white; font-size: 16px;")
        self.right_panel.addWidget(self.format_selector)

        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet("background-color: #555; padding: 8px; font-size: 16px;")
        self.save_button.clicked.connect(self.save_text)
        self.right_panel.addWidget(self.save_button)

        self.main_layout.addLayout(self.right_panel)

        # Close Button
        self.close_button = QPushButton("X")
        self.close_button.setStyleSheet("background-color: #aa4444; border-radius: 10px; color: white; width: 20px; height: 20px;")
        self.close_button.setFixedSize(30, 30)
        self.close_button.clicked.connect(self.close_application)

        self.top_bar = QHBoxLayout()
        self.top_bar.addStretch()
        self.top_bar.addWidget(self.close_button)

        self.main_container = QVBoxLayout()
        self.main_container.addLayout(self.top_bar)
        self.main_container.addLayout(self.main_layout)
        self.setLayout(self.main_container)
        self.setAcceptDrops(True)

        # Splash Screen
        self.splash_screen = QLabel("Your image is being scanned...")
        self.splash_screen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splash_screen.setStyleSheet("font-size: 24px; font-weight: bold; color: white; background-color: rgba(0, 0, 0, 0.7);")
        self.splash_screen.setFixedSize(300, 100)
        self.splash_screen.setVisible(False)

        self.overlay = QLabel(self)
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.7);")
        self.overlay.setVisible(False)

        self.main_container.addWidget(self.splash_screen)

        signal.signal(signal.SIGINT, self.handle_sigint)

    # SIGINT handler for cross-platform termination
    def handle_sigint(self, sig, frame):
        print("\nTerminating OCR Tool...")
        QApplication.quit()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.process_image(file_path)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap.scaled(
        self.image_label.width(),
        self.image_label.height(),
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation))

        self.overlay.setGeometry(self.rect())
        self.overlay.setVisible(True)
        self.splash_screen.setVisible(True)
        self.splash_screen.raise_()

        self.thread = OCRThread(file_path)
        self.thread.result_ready.connect(self.display_result)
        self.thread.start()

    def display_result(self, text):
        self.overlay.setVisible(False)
        self.splash_screen.setVisible(False)
        self.ocr_result.setText(text if text.strip() else "No text detected or processing error.")

    def save_text(self):
        file_format = self.format_selector.currentText()
        file_extension = "txt" if "TXT" in file_format else "docx" if "DOCX" in file_format else "pdf"
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", f"*.{file_extension}")
        if file_path:
            text = self.ocr_result.toPlainText()
            if text.strip():
                if file_extension == "txt":
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(text)
                elif file_extension == "docx":
                    doc = Document()
                    doc.add_paragraph(text)
                    doc.save(file_path)
                elif file_extension == "pdf":
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_auto_page_break(auto=True, margin=15)
                    pdf.set_font("Arial", size=14)
                    pdf.multi_cell(0, 10, text)
                    pdf.output(file_path)

    def close_application(self):
        QApplication.instance().quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCRApp()
    window.show()
    sys.exit(app.exec())
