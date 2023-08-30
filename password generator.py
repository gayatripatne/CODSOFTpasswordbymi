import random
import string

def generating_password(length=10):
    character=string.digit+string.ascii_letter+string.punctuation+string.ascii_letter
    password=''.join(random.choice(characters) for _ in range(len))
    return password

len=int(input("enter the length to password:"))
password= generate_password(length)
print("generate password",password)
