class DAG:
    def __init__(self):
        self.adjList = []

    def addEdge(self, u, v, hack):
        map_u, map_v = hack.getMappedID(u), hack.getMappedID(v)
        while map_u >= len(self.adjList) or map_v >= len(self.adjList):
            self.adjList.append([])
        #print("Trying: {} --> {} / {} --> {}".format(u, v, map_u, map_v))
        self.adjList[map_u].append(map_v)
        return

    def printGraph(self, hack):
        print("Graph stored as Adjacency List: ")
        for idx in range(len(self.adjList)):
            print("Vertex {} : ".format(hack.getRealIDfromMappedID(idx)), end = "")
            for task in self.adjList[idx]:
                print("{} ".format(hack.getRealIDfromMappedID(task)), end = "")
            print("")
        return
