from setuptools import setup, find_packages

setup(
    name="Secure-OCR-Tool",
    version="1.0.0",
    author="shivjeet1",
    author_email="shivamlavhale120@gmail.com",
    description="A locally running OCR tool with CLI and GUI support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourrepo/local_ocr_tool",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        'console_scripts': [
            'ocr-cli=src.cli:main',
            'ocr-gui=src.gui:main',
            'ocr-camera=src.camera_ocr:capture_and_ocr'
        ],
    },
    package_data={
        '': ['assets/*', 'config/*']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
