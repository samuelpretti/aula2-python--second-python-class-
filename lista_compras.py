def verlista():
    for x in lista:
        print(f'{x}')

def additem():
    novoitem = str(input('que item voce quer adicionar?: '))
    lista.append (novoitem)

def removeitem():
    tiraitem = str(input('que item voce quer remover?: '))
    lista.remove (tiraitem)

def modifyitem():
    moditem = str(input('qual item vai ser modificado?: '))
    newitem = str(input('qual item vai ser adicionado no lugar?: '))
    posi = lista.index(moditem)
    lista[posi] = newitem

lista = ['banana', 'leite', 'azeite']

while True:
    print('Lista de compras')
    print('1. VER LISTA')
    print('2. CADASTRAR ITEM')
    print('3. EXCLUIR ITEM')
    print('4. MODIFICAR ITEM')
    print('0. SAIR')
    opcao = input('escolha uma opção: ')

    if opcao == '1':
        verlista()
    elif opcao == '2':
        additem()
    elif opcao == '3':
        removeitem()
    elif opcao == '4':
        modifyitem()
    elif opcao == '0':
        print('Saindo do sistema...')
        break


    else:
        print('opção inválida, tente novamente!')
        break
        