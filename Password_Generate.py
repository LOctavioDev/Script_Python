import random
import string

def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        password_length = int(input("Ingrese la longitud deseada para la contraseña: "))
        if password_length <= 0:
            print("La longitud debe ser un número positivo mayor que cero.")
        else:
            generated_password = generate_password(password_length)
            print("Contraseña generada:", generated_password)
    except ValueError:
        print("Por favor, ingrese un número válido para la longitud.")
