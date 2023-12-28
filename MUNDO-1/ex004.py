#tipo primitivo

palavra = input("Digite algo: ")

print("O tipo primitivo desse valor é?", type(palavra))
print('Tem espaços? ---> ', palavra.isspace())
print('É alfabetico? ---> ', palavra.isalpha())
print('É alfanúmerico? --> ', palavra.isalnum())
print('Tem maiusculo? ---> ', palavra.isupper())
print('Está capitalizada? --> ', palavra.istitle())    #quer dizer que está começa com maiuscula e contém letras minusculas a palavra