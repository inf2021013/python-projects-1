from xml.dom import minidom

class SAVER:
    def __init__(self, file):
        self.file = minidom.parse(file)

    def read(self, file):
        pass

    def save(self, file):
        pass