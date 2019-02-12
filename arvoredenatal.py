if __name__ == "__main__":
    G = int(input())
    for galho in range(G):
        n_pacotes = int(input())
        capacidade = int(input())
        pacotes = []
        for x in range(n_pacotes):
            e, pc = [int(i) for i in input().split()]
            pacotes.append({'e': e, 'pc': pc})

        bestE = 0
        bestPc = 0
        for i in range(pow(2, n_pacotes), 0, -1):
            e = 0
            pc = 0
            for k in range(n_pacotes):
                if((i >> k) % 2 != 0):
                    e = e + pacotes[k]['e']
                    pc = pc + pacotes[k]['pc']

                    if pc > capacidade:
                        break

            if e > bestE and pc <= capacidade:
                bestE = e
                bestPc = pc
            pass

        print("Galho %d:" %(galho+1))
        print("Numero Total de enfeites:", bestE)
    pass