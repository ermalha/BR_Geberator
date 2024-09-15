# Business Rules Document Generator

This Flask-based web application automates the generation of Word documents based on business rules provided in an Excel file.

## Features

- Excel file upload and processing
- Word document generation based on business rules
- OpenAI API integration for content generation
- Web interface for easy use

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your OpenAI API key as an environment variable: `export OPENAI_API_KEY='your-api-key'`
4. Run the application: `python main.py`

## Usage

1. Access the web interface at `http://localhost:5000`
2. Upload an Excel file containing business rules
3. The application will generate Word documents for each rule
4. Download the generated documents

## Configuration

Adjust settings in `config.py` to customize file paths, Excel column mappings, and other options.

## Requirements

- Python 3.x
- Flask
- pandas
- python-docx
- openai

## License

This project is licensed under the MIT License.
