import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    caminos = {nodo: [] for nodo in grafo}
    caminos[inicio] = [inicio]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
                caminos[vecino] = caminos[nodo_actual] + [vecino]
    
    return distancias, caminos

grafo = {
    'A': {'B': 2, 'C': 9},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'
distancias, caminos = dijkstra(grafo, inicio)

print("Distancia recorridas desde el  nodo inicial:", distancias)
print("Diastancias más cortas desde el nodo inicial:")
for nodo in caminos:
    print(f"{inicio} -> {nodo}: {' -> '.join(caminos[nodo])} (Distancia: {distancias[nodo]})")
