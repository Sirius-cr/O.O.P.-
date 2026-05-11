class pokemon:
    def __init__(self,id ,nombre, atacke, tipo):
        self.__id = id
        self.nombre = nombre
        self.atacke = atacke
        self.tipo = tipo

    def hablar(self):
        print("hola")

    @property
    def id(self):
        return(self.__id)
    
    @id.setter 
    def id(self,new_id):
        self.__id = new_id



class pikachu(pokemon):
    def __init__(self, id, nombre, atacke,tipo,entrenador):
        super().__init__(id, nombre, atacke,tipo)
        self.entrenador = entrenador
    
    def hablar(self):
        print("pika pika chuuuuuu!!!")


a = pikachu(1,"pikachu","atactrueno", "electrico", "Ash")
a.id=2
print(a.id)

