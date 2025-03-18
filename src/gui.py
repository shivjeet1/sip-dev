from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QTextEdit, QVBoxLayout, QComboBox
from PyQt6.QtGui import QPixmap
from ocr_engine import extract_text
from file_manager import save_text
import sys

class OCRApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("OCR Tool")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel("Select an Image", self)
        self.button = QPushButton("Open Image", self)
        self.button.clicked.connect(self.load_image)

        # Image Preview Section
        self.image_label = QLabel(self)
        
        # Text Output Section
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        # Output Format Selection
        self.format_combo = QComboBox(self)
        self.format_combo.addItems(["txt", "pdf", "docx", "doc"])
        
        # Save Button
        self.save_button = QPushButton("Save Text", self)
        self.save_button.clicked.connect(self.save_text)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.image_label)  # Image preview section
        layout.addWidget(self.text_edit)    # Extracted text display
        layout.addWidget(self.format_combo) # Output format selection
        layout.addWidget(self.save_button)
        self.setLayout(layout)
    
    def load_image(self):
        options = QFileDialog.Option.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg)", options=options)
        if file_path:
            self.image_label.setPixmap(QPixmap(file_path).scaled(400, 300))  # Display image preview
            extracted_text = extract_text(file_path)  # Perform OCR
            self.text_edit.setText(extracted_text)  # Display extracted text
    
    def save_text(self):
        options = QFileDialog.Option.ShowDirsOnly
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*.*)")
        if save_path:
            file_format = self.format_combo.currentText()
            text = self.text_edit.toPlainText()
            save_text(text, save_path, file_format)  # Save extracted text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OCRApp()
    window.show()
    sys.exit(app.exec())

