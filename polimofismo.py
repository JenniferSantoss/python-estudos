#Exemplo de Polimofismo no Python Orientado à objetos

class Argentina():
    def capital(self):
        print('Buenos Aires é a capital da Argentina')

    def lingua_ofcial(self):
        print('Espanhol é a lingua oficial da Argentina')    

class Brasil():
    def capital(self):
        print('Brasilia é a capital do Brasil')

    def lingua_ofcial(self):
        print('Portugues é a lingua oficial do Brasil')   


obj_arg = Argentina()
obj_bra = Brasil()

for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_ofcial()