from dados import ObjDados


print("Iniciando aplicação\nPreparando serviço...")
linha = "-"*50
print(linha)
codigo = int(input("Informe cod: "))
print("O código informado: ", codigo)
print(linha)
ObjDados.dadosObtidos(codigo)
