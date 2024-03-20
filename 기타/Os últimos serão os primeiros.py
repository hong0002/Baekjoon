# Eric Ruiz Irrigado, o famoso Erí, é conhecido entre seus amigos por querer fazer previsões. Em ´ todo tipo de competição ou evento esportivo ele sempre tenta adivinhar os vencedores, os perdedores, artilheiros e coisas similares. Apesar das brincadeiras e deboches de seus amigos, Erí nunca desistiu e sempre busca padrões onde os outros vêem apenas coincidências.
#
# Acompanhando os times da Maratona de Programação, Erí percebeu que a colocação dos times de seu estado na primeira fase sempre se invertiam na segunda fase, ainda que outros times de outras regiões do país estivessem entre eles. Assim, se o time da Uni1 ficar na frente da Uni2 na primeira fase, Erí imagina que o time da Uni2 ficará na frente do time da Uni1 na segunda fase.
#
# Para validar sua hipótese, ele quer desenvolver um programa que, dada uma lista de colocação dos times na primeira fase, mostre qual será a posição relativa destes mesmos times na segunda fase.
#
#
# A entrada é composta por diferentes casos de teste. A primeira linha de cada caso de teste contém n ≤ 100, o número de times do estado de Erí. As n linhas seguintes conterão n inteiros distintos entre 1 e n, inclusive, um por linha, cada inteiro representando um time.
#
# A entrada termina com n = 0. Essa linha não deve ser processada.
#
#
# Para cada caso de teste, seu programa deve imprimir a posição relativa de cada um dos times de acordo com a previsão de Erí, com um número por linha. Após a lista de times, deve ser impressa uma linha contendo um único “0”. Veja o exemplo abaixo.

while True:
    n = int(input())
    if n == 0: break
    my_list = []
    for i in range(n):
        my_list.append(int(input()))
    for i in range(len(my_list)):
        print(my_list[len(my_list)-1 - i])
    print("0")
