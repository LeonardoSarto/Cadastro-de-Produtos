

def abrirItem(item):
    try:
        a = open(item, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def criarItem(item):
    try:
        a = open(item, 'wt+')
        a.close()
    except:
        print ('Erro')
    else:
        print ( item + 'Criado com sucesso')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def lerItem(item):
    try:
        a = open(item, 'rt')
    except:
        print ('Erro')
    else:
        print (a.read())

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def cadastrarItem(item):
    try:
        a = open(item, 'at')
    except:
        print ('Erro')
    else:
        a.write('\n'+input('\nCadastre um novo item\n'))
        a.close()
        

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

item = input('Digite o nome do arquivo: ')

if not abrirItem(item):
    criarItem(item)
else:
    print ('\n'+item + ' Encontrado\n\nLeitura do arquivo:\n')
    lerItem(item)