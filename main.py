import products.productsCreation as cadastro

print("--------Menu temporário--------")
print("1. Criar um arquivo")
print("2. Editar um arquivo")
print("3. Ler um arquivo")
print("4. Excluir um arquivo")
print("5. Sair do programa")

menu = int(input("Digite a opção"))
if menu == 1:
    cadastro.criarItem
elif menu == 2:
    produto = input("Digite o nome do arquivo para editar")
    cadastro.editarItem(produto)
elif menu == 3:
    cadastro.lerItem