import random

print("Bem-vindo ao gerador de senhas")

chars = "abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ!@#$%&*()><:?0123456789"

number = input("Quantas senhas deseja gerar?\n")
number = int(number)

length = input("Quantos caracteres suas senhas precisam ter?\n")
length = int(length)

print("\nSuas senhas são:\n")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)