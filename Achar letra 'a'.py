#Programa que conta quantas letras 'a' tem em uma string
texto = str(input('Escreva uma frase: '))
texto = (texto.lower())
n1 = (texto.count('a'))
print('Existem {} letras "a" na sua frase (string) digitada '.format(n1))