import json
import jsonschema
from jsonschema import validate, Draft7Validator
import sys

def load_json_schema(schema_path):
    with open(schema_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_json_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def validate_json(json_data, schema):
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(json_data), key=lambda e: e.path)

    if not errors:
        print("JSON is valid.")
    else:
        for error in errors:
            error_path = " -> ".join([str(item) for item in error.path])
            print(f"JSON validation error: {error.message}")
            print(f"Error at: {error_path}")
            print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_json.py <json_file_path> <json_schema_key>")
        sys.exit(1)

    json_file_path = sys.argv[1]
    json_schema_key = sys.argv[2]

    schema_path = f'schemas/{json_schema_key}.json'

    # Load schema and JSON data
    schema = load_json_schema(schema_path)
    json_data = load_json_data(json_file_path)

    # Validate JSON
    validate_json(json_data, schema)
