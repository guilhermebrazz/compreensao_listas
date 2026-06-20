def extrair(lista):

    return [letra for palavra in lista for letra in palavra]

lista = ["python", "java", "c++"]

print(extrair(lista))