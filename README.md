# Problem 4B: Pipeline Dependency

===

Problem description for data role: [`ws-data-spark`](https://github.com/EQWorks/ws-data-spark)
===

### Repository Structure

`CoordinateCompress.py`, `InputParser.py` & `DAG.py` contains helpers classes and `main.py` contains the main solution to the problem.


### My Attacking Approach


Since there is no constraint on the ID of the tasks, I am assuming - they can be very large. 

+ To reduce the memory complexity of the graph I'll be storing the graph as adjacency list instead of matrix representation
+ I'll use [coordinate-compression technique](https://www.quora.com/What-is-coordinate-compression-and-what-is-it-used-for) to reduce the memory complexity of the graph from `O(Highest Task ID + Number of Relations)` to `O(Number of Tasks + Number of Relations)`

##### Observation & Approaching Towards the Solution

Since there is only one end task, it's for certain that our task-ordering will end with the goal task. And we have to complete all the tasks that are prerequisites for this.

If we take the **reverse graph** and start traversing from the `goal task`, we can notice that all the nodes we can go to from this node **MUST BE** a pre-requisite for the `goal node` i.e. those pre-requisite tasks must be carried away *before* doing the goal task.

The problem now boils down to *finding a topological sort ordering* in the reverse graph strating from the `goal node`. 

#### Sample Analysis of the test-case

The given graph is: 

![Alt text](forwardGraph.PNG?raw=true "Title")

Since it's a DAG, there's no cycle in the graph. I have generated a topological sort using the reverse graph leveraging the fact that all the tasks must end at a fixed point. The reverse graph is:

![Alt text](reverseGraph.PNG?raw=true "Title")

Final topological ordering for the given task: `41 112 39 100 21 73 20 97 94 56 102 36 `
