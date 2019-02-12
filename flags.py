if __name__ == "__main__":
    H = 1
    n, t = [int(i) for i in input().split()]
    while n !=0:
        rides = []
        cost = [0 for i in range(t+1)] # vetor de custo
        best = [0 for i in range(t+1)] # melhor combinação
        for i in range(n):
            d, p = [x for x in input().split()]
            rides.append({'d': int(d), 'p': int(p)}) # montando dicionarios com a entrada
        
        for j in range(n): # pra j montanhas russas
            for i in range(t+1): # em i minutos
                if i >= rides[j]['d']: 
                    if cost[i] < (cost[i - rides[j]['d']] + rides[j]['p']):
                        cost[i] = cost[i - rides[j]['d']] + rides[j]['p']
                        best[i] = j
        print('Instancia ', H)
        H+=1
        print(cost[t])
        print()
        n, t = [int(i) for i in input().split()]
    pass

#Programacao dinamica inspirada no problema da mochila