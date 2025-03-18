Installation Guide

Prerequisites

Python 3.8 or newer

Pip (Python package manager)

Tesseract OCR (Ensure it's installed and added to PATH)

Installing Tesseract OCR

Linux (Debian/Ubuntu)

sudo apt update
sudo apt install tesseract-ocr

Arch Linux

sudo pacman -S tesseract-ocr

Windows

Download from Tesseract GitHub

Install and add Tesseract-OCR path to system environment variables

Installation Steps

1. Clone Repository

git clone <repo_url>
cd <repo_name>

2. Install Dependencies

pip install -r requirements.txt

Running the Tool

CLI Version

python src/cli.py --image <image_path>

GUI Version

python src/gui.py

Webcam Capture

python src/camera_ocr.py

Setup for Packaging

To distribute the tool, setup.py is used to package it. Below are the included sections:

1. Metadata

Name, version, author, description, license, etc.

2. Dependencies

Uses install_requires to include dependencies from requirements.txt

3. Entry Points

Defines executable scripts for CLI and GUI usage

4. Package Data

Includes required assets, configurations, and additional files

5. Installation Command

pip install .

This will install the tool as a Python package and allow execution via command line.

Uninstallation

pip uninstall <package_name>


