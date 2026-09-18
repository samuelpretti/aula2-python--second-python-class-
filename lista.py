notas = [7.0, 1.5, 10.0, 8.5, 3.0, 8.0, 9.5, 7.6]

# ciclo = 0
# limite = len(notas) - 1

# while ciclo <= limite:
#   print(f"Sua nota é: {notas [ciclo]}")
#    ciclo += 1

resposta = str(input("deseja ver suas notas? (sim/nao): "))

while resposta == "sim":
    for x in notas:
        print (f"Sua nota é: {x}")
    resposta = str(input("quer adicionar uma nova nota? (sim/nao): "))
    nota = float(input("digite sua nova nota: "))
    notas.append (nota)

# nota.pop(1) remove a segunda nota
# nota.remove(1.5) remove o valor exato escrito
# nota.append(7.7) adicionar um novo valor para a ultima posição da lista
# nota.index(8.5) localizar a posicao na lista
# nota[1] mostra qual é a segunda nota  