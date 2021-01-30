from DAG import *
from InputParser import *
from CoordinateCompress import *

# Since DAGs don't have cycles, we don't need to keep a visited array to check for cycles
def depthFirstSearch(graph, hack, visited, currentTask, topologicalSort):
    visited[currentTask] = 1
    for nextTask in graph.adjList[currentTask]:
        if visited[nextTask] == 0:
            depthFirstSearch(graph, hack, visited, nextTask, topologicalSort)

    topologicalSort.append(currentTask)
    return

'''
    Time complexity: O(Number of Tasks)
    Memory Complexity: O(Number of relations)  [Applied Co-ordinate Compression technique for optimization]
'''


if __name__ == '__main__':
    '''
    Since there is no constraint on the ID of the tasks, I am assuming - they can be very large. To reduce the memory
    complexity of the graph (Which I will store as adjacency List), I'll use coordinate-compression technique to reduce
    the memory complexity of the graph to O(Number to relations)
    '''

    hack = CoordinateCompress()

    taskList = [[x, hack.getMappedID(x)] for x in InputParser.readTaskIds('Inputs/task_ids.txt')]
    startTask, goalTask = [[x, hack.getMappedID(x)] for x in InputParser.readQuestions('Inputs/question.txt')]
    
    print("List of all the mappings\n")

    for task in taskList:
        print("\tTask: {} --> Mapped with: {}".format(task[0], task[1]))
    print("\n")

    print("Start Task is {} --> mapped with {}\nGoal Task is {} --> mapped with {}\n".format(startTask[0], startTask[1], goalTask[0], goalTask[1]))

    # relations can be modeled as edges in the graph
    relations = InputParser.readRelations('Inputs/relations.txt')

    graph = DAG()
    for edge in relations:
        # Creating the recerse graph with reverse edges
        graph.addEdge(edge[1], edge[0], hack)
    graph.printGraph(hack)

    # Starting the DFS with the start-task
    topologicalSort = []
    visited = [0 for x in range(hack.taskCount)]
    depthFirstSearch(graph, hack, visited, goalTask[1], topologicalSort)

    topologicalSort = [hack.getRealIDfromMappedID(x) for x in topologicalSort]

    # The final topological ordering
    print("Final topological ordering: ", end = "")
    for task in topologicalSort:
        print(task, end = " ")
