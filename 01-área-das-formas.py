def circulo():
    raio = float(input("qual é o raio?: "))
    circ = (raio * raio) * 3.14
    print(f"a área do seu círculo é igual a: {circ}")

def triangulo():
    Btri = float(input("qual é a base: "))
    Htri = float(input("qual é a altura?: "))
    trian = (Btri * Htri) / 2
    print(f"a área do seu triangulo é igual a: {trian}")

def quadra():
    lado = float(input("qual é a medida de um dos lados?: "))
    quad = lado * lado
    print(f"a área do seu quadrado é igual a: {quad}")

def retangulo():
    base = float(input("qual é a base: "))
    altura = float(input("qual é a altura?: "))
    retan = base * altura
    print(f"a área do seu retangulo é igual a: {retan}")

def paralelograma():
    Bpara = float(input("qual é a base: "))
    Hpara = float(input("qual é a altura?: "))
    paral = Bpara * Hpara
    print(f"a área do seu paralelograma é igual a: {paral}")

def losango():
    Dmenor = float(input("qual é a diagonal menor: "))
    Dmaior = float(input("qual é a diagonal maior: "))
    losan = Dmaior * Dmenor
    print(f"a área do seu losango é igual a: {losan}")

def trapezio():
    bmenor = float(input("qual é a base menor: "))
    bmaior = float(input("qual é a base maior: "))
    htra = float(input("qual é a altura: "))
    trape = ((bmenor + bmaior) * htra) / 2
    print(f"a área do seu trapézio é igual a: {trape}")


while True:
    print('Calculadora')
    print('1. CIRCULO')
    print('2. TRIANGULO')
    print('3. QUADRADO')
    print('4. RETANGULO')
    print('5. PARALELOGRAMA')
    print('6. LOSANGO')
    print('7. TRAPEZIO')
    print('0. SAIR')
    opcao = input('escolha uma opção: ')
    
    if opcao == '1':
        print('Calculando...')
        circulo()
    elif opcao == '2':
        print('Calculando...')
        triangulo()
    elif opcao == '3':
        print('Calculando...')
        quadra()
    elif opcao == '4':
        print('Calculando...')
        retangulo()
    elif opcao == '5':
        print('Calculando...')
        paralelograma()
    elif opcao == '6':
        print('Calculando...')
        losango()
    elif opcao == '7':
        print('Calculando...')
        trapezio()
        
    elif opcao == '0':
        print('Saindo do sistema...')
        break

    
    else:
        print('opção inválida, tente novamente!')
    break





