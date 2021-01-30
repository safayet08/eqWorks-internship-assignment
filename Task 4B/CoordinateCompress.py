'''
Since there is no constraint on the ID of the tasks, I am assuming - they can be very large. To reduce the memory
complexity of the graph (Which I will store as adjacency List), I'll use coordinate-compression technique to reduce
the memory complexity of the graph to O(Number to relations)
'''

class CoordinateCompress:
    def __init__(self):
        self._map = dict()
        self._inverseMap = dict()
        self.taskCount = 0

    def getMappedID(self, realID):
        if self._map.get(realID) is None:
            self._map[realID] = self.taskCount
            self._inverseMap[self.taskCount] = realID
            self.taskCount = self.taskCount + 1

        return self._map.get(realID)

    def getRealIDfromMappedID(self, mappedID):
        return self._inverseMap[mappedID]