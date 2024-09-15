import os

# File paths
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
WORD_TEMPLATE_PATH = 'word_template.docx'

# Allowed file extensions
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

# Excel file structure
EXCEL_COLUMNS = {
    'Rule ID': 'rule_id',
    'Severity': 'severity',
    'Description': 'description'
}

# Logging configuration
LOG_FILE_PATH = 'app.log'
LOG_LEVEL = 'INFO'
