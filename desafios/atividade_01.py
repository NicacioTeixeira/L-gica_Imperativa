altura = []
genero = []

for i in range(3):

    genero_digitado = input(f'Insira o  {i+1}º Dado:\n Digite o genero da pessoa abaixo \n (1) para Homen -- (2) para Mulher : ')
    genero.append(genero_digitado)
    quantidade_mulher = genero.count("2")

    altura_digitada = float(input('Digite a altura: '))
    altura.append(altura_digitada)

    altura_total = sum(altura)
    operacao_media_altura = altura_total / len(altura)
    altura_maxima = max(altura)
    altura_minima = min(altura)

print(f'A altura maxima foi de  :', altura_maxima)
print(f'A altura minima foi de  :', altura_minima)
print(f'A média de altura foi de :', operacao_media_altura)
print("Quantidade de mulheres foi:", quantidade_mulher)

