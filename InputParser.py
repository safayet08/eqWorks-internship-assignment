# Parsing the input files
class InputParser:
    def readRelations(filepath):
        file = open(filepath, 'r')
        lines = file.readlines()
        edgeList = []
        for line in lines:
            u, v = [int(x) for x in line.split("->")]
            edgeList.append([u, v])

        return edgeList

    def readQuestions(filepath):
        file = open(filepath, 'r')
        startTask = int(file.readline().split(":")[1])
        goalTask = int(file.readline().split(":")[1])

        return [startTask, goalTask]

    def readTaskIds(filepath):
        file = open(filepath, 'r')
        line = file.readline()
        taskList = [int(x) for x in line.split(",")]
        return taskList
