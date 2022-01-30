import cadastro.cadastroProdutos as cadastro

print("--------Menu temporário--------")
print("1. Criar um produto")
print("2. Editar um produto")
print("3. Consultar um produto")
print("4. Excluir um produto")
print("5. Sair do programa")
print("------------------------")

menu = int(input("\nDigite a opção: "))
if menu == 1:
    cadastro.criarProduto()
elif menu == 2:
    cadastro.consultarItem()
    cadastro.editarItem()
    cadastro.consultarItem()
elif menu == 3:
    cadastro.consultarItem()
elif menu == 4:
    cadastro.deletarItem()
elif menu == 5:
    exit()