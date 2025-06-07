

class InfoDao:
    def __init__(self):
      self.estudiante = []
        
    def add(self ,estudiante):
        self.estudiante.append(estudiante)
        
    def show(self):
        for estudiante in self.estudiante:
            print(estudiante)