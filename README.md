# PipelineDependency
    
Since there is no constraint on the ID of the tasks, I am assuming - they can be very large. To reduce the memory complexity of the graph (Which I will store as adjacency List), I'll use coordinate-compression technique to reduce the memory complexity of the graph to O(Number to relations)

The given graph is: 

![Alt text](forwardGraph.PNG?raw=true "Title")

Since it's a DAG, there's no cycle in the graph. I have generated a topological sort using the reverse graph leveraging the fact that all the tasks must end at a fixed point. The reverse graph is:

![Alt text](reverseGraph.PNG?raw=true "Title")

Final topological ordering for the given task: 41 112 39 100 21 73 20 97 94 56 102 36 
