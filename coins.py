if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        soma = 0
        input()
        moedas = [int(moeda) for moeda in input().split()]
        resp = 0
        for moeda in moedas:
            if (moedas.index(moeda) == (len(moedas)-1)) or soma + moeda < moedas[moedas.index(moeda)+1]:
                soma += moeda
                resp+=1
        print(resp)
# Algoritmo Guloso