if __name__ == "__main__":
    casos = int(input())

    for caso in range(casos):
        n_pacs = int(input()) 

        pacotes = [tuple(map(int, input().split())) for k in range(n_pacs)] # construimos tuplas com os pacotes
        
        maior_quant = [[[0,0,n_pacs] for k in range(51)] for w in range(n_pacs+1)] # inicializa o vetor para analizar as possíveis soluções
        for i in range(1, len(maior_quant)):
            for j in range(51):
                if pacotes[i-1][1] > j:
                    maior_quant[i][j] = maior_quant[i-1][j]
                else:
                    ant = maior_quant[i-1][j]
                    at = maior_quant[i-1][j-pacotes[i-1][1]]
                    if pacotes[i-1][0] + at[1] > ant[1]:
                        maior_quant[i][j][0] = at[0] + pacotes[i-1][1]
                        maior_quant[i][j][1] = at[1] + pacotes[i-1][0]
                        maior_quant[i][j][2] = at[2] - 1
                    else:
                        maior_quant[i][j] = ant
        
        maior = maior_quant[n_pacs][50] # com o algoritmo executado pega a combinação de valores ótima
        print("%i brinquedos" %(maior[1])) # quantidade de brinquedos
        print("Peso: %i kg" %(maior[0])) # peso total
        print("sobra(m) %i pacote(s)" %(maior[2])) # sobra
        print()
    pass

# Algoritmo Dinamico