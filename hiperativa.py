import networkx as nx

if __name__ == "__main__":
    m, n = [int(x) for x in input().split()]
    while n != 0:
        soma = 0
        G = nx.DiGraph()
        iniciais = []
        finais = []
        ats = []
        for i in range(n):
            s, f = [int(x) for x in input().split()]
            ats.append({'s': s, 'f': f})
            if s == 0 :
                iniciais.append(i)
            if f == m :
                finais.append(i)
            G.add_node(i)
            soma = soma + 1 if s == 0 and f == m else soma
            for j in range(len(ats)):
                if((ats[j]["s"] <= f and ats[j]["s"] > s)):                
                    G.add_edge(i, j)
                elif((ats[j]["f"] >= s and ats[j]["f"] < f)):                
                    G.add_edge(j, i)            

        for node in iniciais:
            try:
                paths = list(nx.all_simple_paths(G, source=node, target=[finais]))
                for path in paths:
                    minimum = True
                    for i in range(1, len(path) - 1):
                        minimum = minimum and ats[path[i - 1]]["f"] < ats[path[i + 1]]["s"]
                        if(not minimum):                        
                            break
                        pass
                    pass
                    if(minimum):                    
                        soma+=1                                       
                    pass

                
                soma+=1
            except:
                pass
        print(soma) 
        m, n = [int(x) for x in input().split()]
    pass