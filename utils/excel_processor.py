import pandas as pd
from config import EXCEL_COLUMNS

def process_excel_file(filepath):
    try:
        df = pd.read_excel(filepath)
        
        # Validate required columns
        for col, internal_name in EXCEL_COLUMNS.items():
            if col not in df.columns:
                raise ValueError(f"Required column '{col}' not found in Excel file.")
        
        # Extract and process rules
        rules = []
        for _, row in df.iterrows():
            rule = {
                'rule_id': row[EXCEL_COLUMNS['Rule ID']],
                'severity': row[EXCEL_COLUMNS['Severity']],
                'description': row[EXCEL_COLUMNS['Description']]
            }
            
            # Validate severity
            if rule['severity'] not in ['Error', 'Warning']:
                raise ValueError(f"Invalid severity '{rule['severity']}' for Rule ID {rule['rule_id']}. Must be 'Error' or 'Warning'.")
            
            rules.append(rule)
        
        return rules
    except Exception as e:
        raise Exception(f"Error processing Excel file: {str(e)}")
