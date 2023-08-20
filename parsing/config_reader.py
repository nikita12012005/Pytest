import json


class ConfigReader:
    def __init__(self, config_file_path):
        with open(config_file_path, 'r') as config_file:
            self.config = json.load(config_file)

    def get(self, section, option):
        return self.config[section][option]
