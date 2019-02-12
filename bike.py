import networkx as nx

if __name__ == "__main__":
  inst = 1
  str = input("")
  n, m = str.split(" ")
  n = int(n)
  m = int(m)

  while n > 0:
    print("Instancia ", inst)
    inst = inst + 1
    G = nx.Graph()
    for i in range (m):
      str = input("")
      u, v, p = str.split(" ")
      G.add_edge(int(u), int(v), height=int(p))
    
    k = int(input())
    for i in range(k):
      s, t = [int(i) for i in input().split()]
      #paths = list(nx.all_simple_paths(G, source=s, target=t))
      path = nx.shortest_path(G, s, t, 'height')
      #por algum motivo obscuro nao funciona  ¯\_(ツ)_/¯
		  
		
      menor = G[path[0]][path[1]]['height']
      for c in range(len(path) - 1):
        tam = G[path[c]][path[c + 1]]['height']
        if tam > menor:
          menor = tam
		
		
      #for path in paths:
      #  maior = G[path[0]][path[1]]['height']
      #  for c in range(len(path) - 1):
      #    tam = G[path[c]][path[c + 1]]['height']
      #    if tam > maior:
      #      maior = tam
      #  if maior < menor:
      #    menor = maior
      print(menor)
      
    n, m = input().split(" ")
    n = int(n)
    m = int(m)
