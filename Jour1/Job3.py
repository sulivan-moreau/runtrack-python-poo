class Operation:
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def get_nombre1(self):
        print("Le nombre1 est ",self.nombre1)

    def get_nombre2(self):
        print("Le nombre2 est ",self.nombre2)

    def addition(self):
        print(self.nombre1+self.nombre2) 

operation = Operation()

operation.addition()