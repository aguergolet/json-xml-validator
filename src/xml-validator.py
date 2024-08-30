import xmlschema
import os
import sys

def validate_xml(xml_file: str, key: str) -> bool:
    """
    Valida um arquivo XML contra um XSD baseado na chave fornecida.

    :param xml_file: Caminho para o arquivo XML.
    :param key: Chave usada para carregar o XSD no diretório "schemas".
    :return: True se o XML for válido, False se não for.
    """
    xsd_path = os.path.join("schemas", f"{key}.xsd")
    
    if not os.path.exists(xsd_path):
        raise FileNotFoundError(f"O arquivo XSD {xsd_path} não foi encontrado.")
    
    schema = xmlschema.XMLSchema(xsd_path)
    
    try:
        schema.validate(xml_file)
        print(f"O arquivo XML '{xml_file}' é válido.")
        return True
    except xmlschema.validators.exceptions.XMLSchemaValidationError as e:
        print(f"O arquivo XML '{xml_file}' é inválido: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python xm-validator.py <caminho_xml> <chave>")
        sys.exit(1)
    
    xml_file = sys.argv[1]
    key = sys.argv[2]

    validate_xml(xml_file, key)
