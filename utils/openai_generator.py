import os
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_ai_content(rule):
    try:
        # Generate title
        title_prompt = f"Given the following rule description: '{rule['description']}', generate a concise title for the domain, including the Rule ID '{rule['rule_id']}'."
        title_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": title_prompt}],
            max_tokens=50
        )
        title = title_response.choices[0].message.content.strip()

        # Generate mapping table content
        mapping_prompt = f"Based on the rule: '{rule['description']}', identify the XML element it applies to and the corresponding JSON element after conversion. Provide this information in a structured format."
        mapping_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": mapping_prompt}],
            max_tokens=100
        )
        mapping_content = mapping_response.choices[0].message.content.strip()

        # Generate rule condition and pseudocode
        condition_prompt = f"Express the following rule in a formal condition and pseudocode: '{rule['description']}'"
        condition_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": condition_prompt}],
            max_tokens=200
        )
        condition_content = condition_response.choices[0].message.content.strip()

        # Parse the condition content to separate condition and pseudocode
        condition_lines = condition_content.split('\n')
        rule_condition = condition_lines[0] if len(condition_lines) > 0 else ""
        pseudocode = '\n'.join(condition_lines[1:]) if len(condition_lines) > 1 else ""

        return {
            'title': title,
            'mapping_table': mapping_content,
            'rule_condition': rule_condition,
            'pseudocode': pseudocode
        }
    except Exception as e:
        raise Exception(f"Error generating AI content: {str(e)}")
