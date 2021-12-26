Authors: Arik Tatievski, 208997056
	Roi Meshulam, 315635649

What is this project?
This project is a Graph analayzing project which allows us to insert graphs, create graphs, changing graphs and study them.

The way we made our project:
We have made a few classes these next lines will explain them.
Node/Edge- are 2 low-key classes that know how to do the most basic functions.(Creating nodes/edges/getting their location values etc..)
DiGraph - this class is represting a graph = (V=group of vertexes,E=group of edges) and all the functions we can do on a graph(adding and removing edges/nodes, getting Iterators of the graph edges/nodes and more)
GraphAlgo - this class allows us to make alogrithems on graphs such as tsp(getting cities),calculating shortest path(through dijkstra algorithm), checking if a graph is connected(BFS on same vertes on a graph&the graph's opposite),Using matplotlib to show a graphic visual of the graph and more.

How did we test our project?
In every step and every function we made we did all the tests on the extreme conditions of the graph to make sure that our graph can handle all possible situations.
In addition there are 2 testing classes

Graph stability:
Regular graphs (from the examples) - all algorithms take not more than ~ 1 second
1000 Nodes - Show graph takes ~ 10 seconds, algroithms are taking more than 30 minutes

How to use our project:
Please run the jar file with the following command "java -jar Ex2.jar Filename.json and our GUI will apear.

Comparing to java(Taking A5 graph as an example):
||shortest path|center|TSP
|Java|0.000|0.063|0.016
|Python|0.015|0.5310|0.031
We can obviously see Java runing time is way faster than Python.

All the outputs of our functions were checked and verified as true answers

Hope you find good usuage of this project!

