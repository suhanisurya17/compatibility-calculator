# compatibility-calculator


Follow these steps to set up and run the project.

## Prerequisites

- Python installed
- Node.js installed

## Steps to Set Up the Project

### 1. Project Structure
│── main.py
│── templates
│   └── index.html
│── static
│   └── attributes
│       └── style.css

### 2. Create a Python Virtual Environment
Open the terminal and run:
```sh
python -m venv venv
source ./venv/bin/activate
pip install Flask
pip install pytesseract
pip install Pillow
npm install --local http-server
cd compatibility_calculator
python main.py



