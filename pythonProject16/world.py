class WORLD:
    def __init__(self):
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def remove(self, object):
        self.objects.pop(object)