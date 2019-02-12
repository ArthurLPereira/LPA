import networkx as nx
import itertools

if __name__ == "__main__":
    R, K = [int(x) for x in input().split()]
    G = nx.Graph()
    for i in range(K):
        s, t = [int(x) for x in input().split()]
        G.add_edge(s, t)
    esquema = False
    for i in range(1, R+1):
        for sub_nodes in itertools.combinations(G.nodes(),i):
            subg = G.subgraph(sub_nodes)
            
            soma = sum([G.degree[i] for i in subg.nodes])
            if(soma == K):
                esquema = True
                break
    print("S" if esquema else "N")