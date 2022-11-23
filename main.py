from grafo import Grafo
from entradas import exemplos


while(True):
    for i in range(len(exemplos)):
        print(f"{i}. Exemplo {i+1}")
    entrada = int(input("Selecione o exemplo: "))
    
    g = Grafo(exemplos[entrada])
    g.emparelha()
    print("\n")
