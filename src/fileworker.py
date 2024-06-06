import json
import os
from abc import ABC, abstractmethod

class BaseJSON(ABC):
    @abstractmethod
    def open_file(self):
        pass
class JSONWorker(BaseJSON):
    def __init__(self, file_name):
        self.file_name = file_name
        # упрощённо -- надо иди с корневой папки
        self.path = os.path.join('data', file_name)

    def open_file(self):
        with open(self.path) as file:
            return json.load(file)

    def write_file(self, data):
        with open(self.pathm, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)