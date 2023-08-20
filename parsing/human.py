import json
import xml.etree.ElementTree as ET


class Human:
    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        return json.dumps({
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "birth_year": self.birth_year
        }, indent=4)

    def convert_to_xml(self):
        human_element = ET.Element("Human")
        name_element = ET.SubElement(human_element, "Name")
        name_element.text = self.name
        age_element = ET.SubElement(human_element, "Age")
        age_element.text = str(self.age)
        gender_element = ET.SubElement(human_element, "Gender")
        gender_element.text = self.gender
        birth_year_element = ET.SubElement(human_element, "BirthYear")
        birth_year_element.text = str(self.birth_year)
        xml_string = ET.tostring(human_element, encoding="utf-8", method="xml")
        return xml_string.decode("utf-8")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python your_script.py [json|xml]")
        sys.exit(1)

    conversion_type = sys.argv[1]

    human = Human("John", 30, "Male", 1993)

    if conversion_type == "json":
        json_data = human.convert_to_json()
        print(json_data)
    elif conversion_type == "xml":
        xml_data = human.convert_to_xml()
        print(xml_data)
    else:
        print("Invalid conversion type. Use 'json' or 'xml'.")
