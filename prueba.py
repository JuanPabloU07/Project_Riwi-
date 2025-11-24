# user = {
#     "name" : "Pedro",
#     "lastname" : "Pablo",
#     "id" : "1515151",
#     "number" : "0000",
#     "mail" : "pedro@.com"
# }

# print(user["name"])
# print(user["lastname"])
# print(user["id"])
# print(user["number"])
# print(user["mail"])

# lang = ["casa", "perro", "cuchara", "sarten", "salsa", "gato"]

# print(lang[2])

# x = 20
# y = 1.5
# z = "pedro"
# k = True

# print(type(x), type(y), type(z), type(k))

# print(10 + 15)
# print(20 - 10)
# print(45 * 44)
# print(10 ** 3)
# print(14 / 2)
# print(16 // 4)
# print(6 % 4)

# num1 = 18
# num2 = 19
# num3 = 8
# num4 = 7
# num5 = 18
# num6 = 4

# result = num1 != num2
# print(result)

# print(True and False)
# print(False or False)

# edad = 20
# tiene_documento = True
# puede_entrar = (edad >= 18) and tiene_documento
# print(puede_entrar)


# usuario_correcto = "admin"
# contrasena_correcta = "1234"


# usuario = input("Usuario: ")
# contrasena = input("Contraseña: ")
# if usuario == usuario_correcto and contrasena == contrasena_correcta:
#     print("Inicio de sesión valido.")
# else:
#     print("Usuario o contraseña incorrectos.")



# value = 10 
# if value > 0:
#     print("El valor es positivo.")
# elif value < 0:
#     print("El valor es negativo.")
# else:
#     print("El valor es cero.")



# for i in range(10):
#     print("Hola mundo")
#     print("Siempre")    




# entrada = input("Ingrese una palabra: ")
# while True:
#     if entrada == "x":
#         break
#     print(entrada)
#     entrada = input("Ingrese una palabra: ")

# def saludar(name):
#     print("Hola", name)

# saludar("Juan")     



# fruits = ["Manzana", "pera", "piña"]
# print(fruits)

# fruits.append ("Banano")
# fruits.append ("Mango")
# fruits.append ("Fresa")
# print(fruits)

# fruits.insert(2,"Cereza")
# print(fruits)

# fruits.clear()
# print(fruits)

# coders = []
# print(coders)

# amaount = int(input("Cuantos coders va a ingresar: "))  

# while amaount != 0 : 

#     name =  input("Ingrese su nombre: ")
#     lastname =  input("Ingrese su apellido: ")
#     age =  input("Ingrese su edad: ")
#     email =  input("Ingrese su email: ")

#     coder = {
#         "Nombre": name,
#         "Apellido": lastname,
#         "Edad": age,
#         "Email": email
#     }
#     coders.append(coder)
#     amaount -= 1
# print(coders)    

while True:
    try:
        num = int(input("Ingrese la tabla de multiplicar: "))
        with open(f"tabla_{num}.txt","w") as file:
            for i in range(11):
                file.write(f"{num} x {i} es igual: {num * i}\n")
        break        
    except ValueError:
        print("Solo puede ingresar numeros")
    finally:
        print("Fin del programa")
