# Chapter 1

## Exercises

### 1.1-1
> Give a real-world example that requires sorting or a real-world example that requires computing a convex hull.

Some real-world examples of sorting are listing reviews on a website by score, organizing a queue of students by height, or keeping track of books in alphabetical order.

Also, examples for computing convex hulls are calculating the total area of a forest, discovering minimum safe distance from an endemic strike area or minimizing costs when fencing livestock.

### 1.1-2
> Other than speed, what other measures of efficiency might one use in a real-world setting?

In the real world, memory is also a limited resource that should be accounted for.

Outside of computing specifically, other measures of efficiency are number of steps to execute a task, energy used, or even money spent for a project.

### 1.1-3
> Select a data structure that you have seen previously, and discuss its strengths and limitations.

Doubly-linked lists are useful for accessing and modifying elements at the start (head) or end (tail) of the list. However, it's not very performant while accessing an element in the middle of it, since it would require traversing all elements up to that specific element.

### 1.1-4
> How are the shortest-path and traveling-salesman problems given above similar? How are they different?

Both the shortest-path and traveling-salesman problems can be modeled as graphs with weighted edges which aims to minimize the path traversal cost in a graph.

The shortest-path problem, however, comprises finding the shortest path between a source and a destination node, while the traveling-salesman consists of traversing all graph nodes, where the source and destination nodes are the same.

### 1.1-5
> Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is “approximately” the best is good
enough.

Finding out whether a specific book is in a library or not, without accounting for its ordering would require, in the worst case, every single book to be checked out. Depending on the size of the library, it would take several hours to complete. Hence, only checking off shelves at a time solves this problem in a relatively short amount of time, even for libraries with millions of books.

While buying food, on the other hand, simply requires someone to go to one of the nearest supermarkets, rather than comparing prices with all of the markets in the city in order to find the absolute minimum price.

### 1.2-1
> Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.

Modern-day GPS devices and applications rely on shortest-path algorithms to fulfill their purpose.

The beginning of the travel is modeled as the source node and the destination place as the target node. The algorithm has to provide de most suitable path according to the route limitations and preferences specified by the user, such as the chosen mean of transport, time of the trip, intermediate places and traffic.

### 1.2-2
> Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size $n$, insertion sort runs in $8n^2$ steps, while merge sort runs in $64n \lg n$ steps. For which values of n does insertion sort beat merge sort?

Let $f_x(n)$ be a function for the number of steps obtained through the implementation of an arbitrary algorithm $x$. We define $f_i(n)$ for insertion sort and $f_m(n)$ for merge sort. Since the number of steps for an algorithm is a positive integer, we round up to the nearest integer.

$$
\begin{align}
f_i:\mathbb{N} &\to \mathbb{N}&
f_m:\mathbb{N} &\to \mathbb{N}\\
n &\mapsto \lceil 8n^2 \rceil&
x &\mapsto \lceil 64n\lg n \rceil\\
\end{align}
$$

For insertion sort to beat merge sort, must hold the following:

$$
\begin{align}
f_i(n) &< f_m(n)\\
\lceil 8n^2 \rceil &< \lceil 64n\lg n \rceil
\end{align}
$$

Since $n \in \mathbb{N}$, $8n^2 \in \mathbb{N}$ under the closure of naturals. For all $a \in \mathbb{N}$, it is true that $\lceil a \rceil = a$. Hence, we can simplify $\lceil 8n^2 \rceil$ as $8n^2$.

$$
\begin{align}
8n^2 &< \lceil 64n \lg n \rceil
\end{align}
$$

Also, for all $b \in \mathbb{N}$, exists $c \in \mathbb{R^+}$ such that if $b \le \lceil c \rceil$, then $b \le c$.

$$
\begin{align}                                   8n^2 &< 64n \lg n
\end{align}                                     $$

From that, we can derive that:

$$
\begin{align}
\frac{8n^2}{8n} &< \frac{64n \lg n}{8n}\\
n &< 8 \lg n
\end{align}
$$

This turns out to be a transcendental inequality, therefore we can't solve for n algebrically.

For that, we will use a numerical analysis method known as the Newton-Raphson method.

### 1.2-3
> What is the smallest value of n such that an algorithm whose running time is $100n^2$ runs faster than an algorithm whose running time is $2^n$ on the same machine?
