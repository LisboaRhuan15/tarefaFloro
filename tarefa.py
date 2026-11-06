nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
media = (float(nota1) + float(nota2)) / 2
if media >= 7:
    print("Aprovado com média:", media)
else:
    print("Reprovado com média:", media)