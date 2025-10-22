# Chapter 1

## Exercises

### 1.1-1
> Give a real-world example that requires sorting or a real-world example that requires computing a convex hull.

Some real-world examples of sorting are listing reviews on a website by score, organizing a queue of students by height, or keeping track of books in alphabetical order.

Also, examples for computing convex hulls are calculating the total area of a forest, discovering minimum safe distance from an endemic strike area or minimizing costs when fencing livestock.

### 1.1-2
> Other than speed, what other measures of efficiency might one use in a real-world
setting?

In the real world, memory is also a limited resource that should be accounted for.

Outside of computing specifically, other measures of efficiency are number of steps to execute a task, energy used, or even money spent for a project.

### 1.1-3
> Select a data structure that you have seen previously, and discuss its strengths and
limitations.

Doubly-linked lists are useful for accessing and modifying elements at the start (head) or end (tail) of the list. However, it's not very performant while accessing an element in the middle of it, since it would require traversing all elements up to that specific element.

### 1.1-4
> How are the shortest-path and traveling-salesman problems given above similar?
How are they different?

Both the shortest-path and traveling-salesman problems can be modeled as graphs with weighted edges which aims to minimize the path traversal cost in a graph.

The shortest-path problem, however, comprises finding the shortest path between a source and a destination node, while the traveling-salesman consists of traversing all graph nodes, where the source and destination nodes are the same.

### 1.1-5
> Come up with a real-world problem in which only the best solution will do. Then
come up with one in which a solution that is “approximately” the best is good
enough.

Finding out whether a specific book is in a library or not, without accounting for its ordering would require, in the worst case, every single book to be checked out. Depending on the size of the library, it would take several hours to complete. Hence, only checking off shelves at a time solves this problem in a relatively short amount of time, even for libraries with millions of books.

While buying food, on the other hand, simply requires someone to go to one of the nearest supermarkets, rather than comparing prices with all of the markets in the city in order to find the absolute minimum price.
