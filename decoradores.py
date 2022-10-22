# def decorador(func):
#     def envoltura():
#         print ("Esto se anade a mi funcion original")
#         func()
#     return envoltura
# @decorador
# def saludo():
#     print("Hola!")

# # saludo = decorador(saludo)
# saludo()



def mayuscula(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura
# @mayuscula  
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'
def mensaje2(nombre):
    return f'{nombre}, nuevo mensaje'
mensaje = mayuscula(mensaje)
mensaje2 =mayuscula(mensaje2)
print(mensaje("Oscar"))
print(mensaje2("Lucero"))

