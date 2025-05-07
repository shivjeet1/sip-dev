# Secure OCR Tool

A comprehensive OCR (Optical Character Recognition) tool that runs locally, providing both CLI and GUI support. This tool allows users to extract text from images and documents while ensuring privacy and control by running locally.

## Features

- **CLI Support**: Execute OCR tasks directly from the command line.
- **GUI Support**: A user-friendly graphical interface for easy interaction.
- **Camera OCR**: Capture images using a camera and perform OCR instantly.
- **Privacy-Focused**: Runs entirely on your local machine, ensuring privacy.
- **Multi-Format Compatibility**: Supports text extraction from multiple formats, including images and documents.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shivjeet1/sip-dev.git
   cd sip-dev
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have Python 3.8 or higher installed.

## Usage

### Command-Line Interface (CLI)

- To perform OCR via CLI:
  ```bash
  ocr-cli <your-image-file>
  ```

### Graphical User Interface (GUI)

- To launch the GUI:
  ```bash
  ocr-gui
  ```

### Camera-Based OCR

- To capture an image and perform OCR:
  ```bash
  ocr-camera
  ```

## Dependencies

- `opencv-python`
- `pytesseract`
- `pillow`
- `pyqt6`
- `reportlab`
- `python-docx`
- `argparse`

## Project Structure

- `setup.py`: Contains the setup configuration for the tool.
- `requirements.txt`: Lists all dependencies.
- `src/`: Contains the main source code for CLI, GUI, and camera-based OCR.
- `assets/` and `config/`: Resources and configuration files.

## Author

- **shivjeet1**
  - [GitHub Profile](https://github.com/shivjeet1)
  - Contact: shivamlavhale120@gmail.com

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for OCR functionality.
- Open-source libraries listed in the dependencies.

## Issues and Feedback

If you encounter any issues or have feedback, please [open an issue](https://github.com/shivjeet1/sip-dev/issues).
