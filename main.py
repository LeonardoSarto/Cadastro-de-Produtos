import cadastro.cadastroProdutos as cadastro

print("--------Menu temporário--------")
print("1. Criar um arquivo")
print("2. Editar um arquivo")
print("3. Consultar um arquivo")
print("4. Excluir um arquivo")
print("5. Sair do programa")
print("------------------------")

menu = int(input("\nDigite a opção: "))
if menu == 1:
    produto = input("\nDigite o nome do arquivo para criar: ")
    cadastro.criarItem(produto)
elif menu == 2:
    produto = input("\nDigite o nome do arquivo para editar: ")
    cadastro.editarItem(produto)
elif menu == 3:
    produto = input("\nDigite o nome do arquivo para consultar: ")
    cadastro.consultarItem(produto)
elif menu == 4:
    produto = input("\nDigite o nome do arquivo para excluir: ")
    cadastro.deletarItem(produto)

elif menu == 5:
    exit()