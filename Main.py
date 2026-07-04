import random
password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
password_length = int(input("Ingrese la longitud de la contraseña: "))
password = ""
for i in range(password_length):
    password += random.choice(password_characters)
print("Contraseña generada:", password)
