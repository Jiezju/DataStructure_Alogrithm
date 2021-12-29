'''
邻接矩阵
'''


class Vertex:
    def __init__(self, name=None, idx=None):
        self.name = name
        self.idx = idx


class DenseGraph:
    def __init__(self, count=0, directed=True):
        self.n_vertex = count
        self.directed = directed
        self.vertices = []
        self.n_edges = 0

        self.matrix = [[0] * self.n_vertex for _ in range(self.n_vertex)]

        for i in range(self.n_vertex):
            self.vertices.append(Vertex(str(i), i))
    
    def get_vertex(self):
        return self.vertices

    def lenV(self):
        return self.n_vertex

    def lenE(self):
        return self.n_edges

    def hasEdge(vetex_1, vetex_2):
        if vetex_1 not in self.vertices or vetex_2 not in self.vertices:
            raise ValueError

        return self.matrix[vetex_1.idx][vetex_2.idx]

    def addEdge(vetex_1, vetex_2):
        if vetex_1 not in self.vertices or vetex_2 not in self.vertices:
            raise ValueError
        if hasEdge(vetex_1, vetex_2):
            return

        self.matrix[vetex_1.idx][vetex_2.idx] = 1

        if (not self.directed):
            self.matrix[vetex_2.idx][vetex_1.idx] = 1
    
    def get_ngbs(self, vertex):
        for v in self.vertices:
            if self.matrix[vertex.idx][v.idx] == 1:
                yield v


class SparseGraph:
    def __init__(self, count=0, directed=True):
        self.n_vertex = count
        self.directed = directed
        self.vertices = []
        self.n_edges = 0
        self.table = [[]] * self.n_vertex

        for i in range(self.n_vertex):
            self.vertices.append(Vertex(str(i), i))

    def lenV(self):
        return self.n_vertex

    def lenE(self):
        return self.n_edges

    def hasEdge(vertex_1, vertex_2):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            raise ValueError

        for ele in self.table[vertex_1.idx]:
            if ele == vertex_2:
                return True

        return False

    def addEdge(vertex_1, vertex_2):
        if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
            raise ValueError

        if hasEdge(vertex_1, vertex_2):
            return

        self.table[vertex_1.idx].append(vertex_2)

        if not directed:
            self.table[vertex_2.idx].append(vertex_1)

    def get_ngbs(self, vertex):
        for v in self.table[vertex.idx]:
            yield v
