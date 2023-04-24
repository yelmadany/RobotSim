from queue import PriorityQueue
from cell import cell


class GraphC:
    def __init__(self):
        self.v = 100
        self.vertx = []
        self.edges = [[-1 for i in range(self.v)] for j in range(self.v)]
        self.visited = []
        self.CellNumbering = {}
        for x in range(10):
            for y in range(10):
                self.CellNumbering[(x*10)+y] = [x,y]

        self.GraphQ = {0: [1, 10],
                       1: [0, 2, 11],
                       2: [1, 3, 12],
                       3: [2, 4, 13],
                       4: [3, 5, 14],
                       5: [4, 6, 15],
                       6: [5, 7, 16],
                       7: [6, 8, 17],
                       8: [7, 9, 18],
                       9: [8, 19],
                       10: [0, 11, 20],
                       11: [1, 10, 12, 21],
                       12: [2, 11, 13, 22],
                       13: [3, 12, 14, 23],
                       14: [4, 13, 15, 24],
                       15: [5, 14, 16, 25],
                       16: [6, 15, 17, 26],
                       17: [7, 16, 18, 27],
                       18: [8, 17, 19, 28],
                       19: [9, 18, 29],
                       20: [10, 21, 30],
                       21: [11, 20, 22, 31],
                       22: [12, 21, 23, 32],
                       23: [13, 22, 24, 33],
                       24: [14, 23, 25, 34],
                       25: [15, 24, 26, 35],
                       26: [16, 25, 27, 36],
                       27: [17, 26, 28, 37],
                       28: [18, 27, 29, 38],
                       29: [19, 28, 39],
                       30: [20, 31, 40],
                       31: [21, 30, 32, 41],
                       32: [22, 31, 33, 42],
                       33: [23, 32, 34, 43],
                       34: [24, 33, 35, 44],
                       35: [25, 34, 36, 45],
                       36: [26, 35, 37, 46],
                       37: [27, 36, 38, 47],
                       38: [28, 37, 39, 48],
                       39: [29, 38, 49],
                       40: [30, 41, 50],
                       41: [31, 40, 42, 51],
                       42: [32, 41, 43, 52],
                       43: [33, 42, 44, 53],
                       44: [34, 43, 45, 54],
                       45: [35, 44, 46, 55],
                       46: [36, 45, 47, 56],
                       47: [37, 46, 48, 57],
                       48: [38, 47, 49, 58],
                       49: [39, 48, 59],
                       50: [40, 51, 60],
                       51: [41, 50, 52, 61],
                       52: [42, 51, 53, 62],
                       53: [43, 52, 54, 63],
                       54: [44, 53, 55, 64],
                       55: [45, 54, 56, 65],
                       56: [46, 55, 57, 66],
                       57: [47, 56, 58, 67],
                       58: [48, 57, 59, 68],
                       59: [49, 58, 69],
                       60: [50, 61, 70],
                       61: [51, 60, 62, 71],
                       62: [52, 61, 63, 72],
                       63: [53, 62, 64, 73],
                       64: [54, 63, 65, 74],
                       65: [55, 64, 66, 75],
                       66: [56, 65, 67, 76],
                       67: [57, 66, 68, 77],
                       68: [58, 67, 69, 78],
                       69: [59, 68, 79],
                       70: [60, 71, 80],
                       71: [61, 70, 72, 81],
                       72: [62, 71, 73, 82],
                       73: [63, 72, 74, 83],
                       74: [64, 73, 75, 84],
                       75: [65, 74, 76, 85],
                       76: [66, 75, 77, 86],
                       77: [67, 76, 78, 87],
                       78: [68, 77, 79, 88],
                       79: [69, 78, 89],
                       80: [70, 81, 90],
                       81: [71, 80, 82, 91],
                       82: [72, 81, 83, 92],
                       83: [73, 82, 84, 93],
                       84: [74, 83, 85, 94],
                       85: [75, 84, 86, 85],
                       86: [76, 85, 87, 96],
                       87: [77, 86, 88, 97],
                       88: [78, 87, 89, 98],
                       89: [79, 88, 99],
                       90: [80, 91],
                       91: [81, 90, 92],
                       92: [82, 91, 93],
                       93: [83, 92, 94],
                       94: [84, 93, 95],
                       95: [85, 94, 96],
                       96: [86, 95, 97],
                       97: [87, 96, 98],
                       98: [88, 97, 99],
                       99: [89, 98], }
        self.buildGraph()

    def buildGraph(self):
        for v in range(self.v):
                celcost = int(cell().getcost())
                self.vertx.append(celcost)
        for ik,iv in self.GraphQ.items():
            for y in iv:
                self.edges[int(ik)][int(y)] = self.vertx[int(y)]

    # def add_edge(self, u, v, weight):
    #     self.edges[u][v] = weight
    #     self.edges[v][u] = weight

    def returnCellNumber(self, x, y):
        for i, kg in self.CellNumbering.items():
            if ([x, y] == kg):
                return i
        return None


def dijkstra(graph, start_vertex):
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0
    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]

                if neighbor not in graph.visited:

                    old_cost = D[neighbor]

                    new_cost = D[current_vertex] + distance

                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))

                        D[neighbor] = new_cost



    return D

def dijsktraEND(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)

        weight_to_current_node = shortest_paths[current_node][1]
        cont = 0
        destinations = graph.edges[current_node]
        for next_node in destinations:
            if next_node != -1:
                weight = next_node + weight_to_current_node
                if cont not in shortest_paths.keys():

                    shortest_paths[cont] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[cont][1]
                    if current_shortest_weight > weight:
                        shortest_paths[cont] = (current_node, weight)
            cont += 1
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

#g = GraphC()
#print(g.edges)
#print("++++++++++++++++++")
#print(dijkstra(g,1))
#print("=================")
#listofmovement = dijsktraEND(g,1,14)
#print(listofmovement)
# while len(listofmovement) != 0:
# print(listofmovement.pop(0))