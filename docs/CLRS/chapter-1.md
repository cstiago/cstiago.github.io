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
> Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size $n$, insertion sort runs in $8n^2$ steps, while merge sort runs in $64n \lg{n}$ steps. For which values of n does insertion sort beat merge sort?

Let $f_x(n)$ be a function for the number of steps obtained through the implementation of an arbitrary algorithm $x$. We define $s_i(n)$ for insertion sort and $f_m(n)$ for merge sort. Since the number of steps for an algorithm is a positive integer, we round up to the nearest integer.

$$
\begin{align}
s_i:\mathbb{N} &\to \mathbb{N}&
s_m:\mathbb{N} &\to \mathbb{N}\\
n &\mapsto \lceil 8n^2 \rceil&
n &\mapsto \lceil 64n\lg{n} \rceil\\
\end{align}
$$

For insertion sort to beat merge sort, must hold the following:

$$
\begin{align}
s_i(n) &< s_m(n)\\
\lceil 8n^2 \rceil &< \lceil 64n\lg{n} \rceil
\end{align}
$$

Since $n \in \mathbb{N}$, $8n^2 \in \mathbb{N}$ under the closure of naturals. For all $a \in \mathbb{N}$, it is true that $\lceil a \rceil = a$. Hence, we can simplify $\lceil 8n^2 \rceil$ as $8n^2$.

$$
\begin{align}
8n^2 &< \lceil 64n \lg{n} \rceil
\end{align}
$$

Also, for all $b \in \mathbb{N}$, exists $c \in \mathbb{R^+}$ such that if $b \le \lceil c \rceil$, then $b \le c$.

$$
\begin{align}
8n^2 &< 64n\lg{n}
\end{align}
$$

From that, we can derive that:

$$
\begin{align}
\frac{8n^2}{8n} &< \frac{64n\lg{n}}{8n}\\
n &< 8\lg{n}
\end{align}
$$

This turns out to be a transcendental inequality, since the left term is linear and the right term is logarithmic on $n$. Therefore, it's not possible to solve for $n$ algebraically. However, we can analyse its behavior by manipulating the inequality and defining a function $f(x)$ as the following:

$$
\begin{align}
0 &< 8\lg{n}-n &
f: \mathbb{R^+} &\to \mathbb{R}\\
&&
x &\mapsto 8\lg{x}-x
\end{align}
$$

The domain of $f(x)$ is $\mathbb{R^+}$, or $(0, \infty]$, since $\lg n$ is undefined for $x \le 0$. We're then looking for the natural values that satisfy $f(x) > 0$. In order to find its critical points, we first take the derivative $f'(x)$.

$$
\begin{align}
f'(x) &= \frac{d}{dx} (f(x))\\
f'(x) &= \frac{d}{dx} (8\lg{x}-x)\\
f'(x) &= \frac{d}{dx} (8\lg{x}) - \frac{d}{dx}(x)\\
f'(x) &= \frac{d}{dx} (8) \lg{x} + 8 \frac{d}{dx} (\lg{x}) - 1\\
f'(x) &= \cancel{0\lg{x}} + 8\frac{d}{dx}(\lg{x}) - 1\\
f'(x) &= \frac{8}{x\ln{2}} - 1\\
\end{align}
$$

Since $f'(x)$ is not a constant, $f(x)$ may have critical points given by the solutions of $f'(x_i) = 0$.

$$
\begin{align}
0 &= \frac{8}{x_i\ln{2}} - 1\\
1 &= \frac{8}{x_i\ln{2}}\\
x_i &= \frac{8}{\ln{2}}\\
x_i &\approx 11.54
\end{align}
$$

Additionally, we calculate the second derivative $f''(x)$ in order to interpret its concavity.

$$
\begin{align}
f''(x) &= \frac{d}{dx} (f'(x))\\
f''(x) &= \frac{d}{dx} (\frac{8}{x\ln{2}} - 1)\\
f''(x) &= \frac{d}{dx} (\frac{8}{x\ln{2}}) - \cancel{\frac{d}{dx}(1)}\\
f''(x) &= \frac{d}{dx} (\frac{8}{x\ln{2}})\\
f''(x) &= \frac{d}{dx} (\frac{1}{x} \frac{8}{\ln{2}})\\
f''(x) &= \frac{d}{dx} (\frac{1}{x}) \frac{8}{\ln{2}} + \cancel{\frac{1}{x} \frac{d}{dx} (\frac{8}{\ln{2}})}\\
f''(x) &= - \frac{1}{x^2} \frac{8}{\ln{2}}\\
f''(x) &= - \frac{8}{x^2 \ln{2}}\
\end{align}
$$

For all $x \in \mathbb{R}$, $f''(x) < 0$. Then, we know that $x_i$, the only critical point, is a global maximum. Also, we want to know the behavior of the function at both ends of the domain.

$$
\begin{align}
\lim_{x \to 0^+} f(x) &= \lim_{x \to 0^+} 8\lg{x}-x & \lim_{x \to \infty} f(x) &= \lim_{x \to \infty} 8\lg{x}-x\\
\lim_{x \to 0^+} f(x) &= 8 \cdot \lim_{x \to 0^+}\lg{x} - \lim_{x \to 0^+} x & \lim_{x \to \infty} f(x) &= \lim_{x \to \infty} 8(\frac{\ln{x}}{\ln{2}}) - x\\
\lim_{x \to 0^+} f(x) &= \cancel{8} \cdot (- \infty) - \cancel{0} & \lim_{x \to \infty} f(x) &= \lim_{x \to \infty} \frac{8}{\ln{2}}x(\frac{\ln{x}}{x} - 1)\\
\lim_{x \to 0^+} f(x) &= - \infty & \lim_{x \to \infty} f(x) &= \frac{8}{\ln{2}} \cdot \lim_{x \to \infty} x \cdot (\lim_{x \to \infty}\frac{\ln{x}}{x} - 1)\\
& & \lim_{x \to \infty} f(x) &= \cancel{\frac{8}{\ln{2}}} \cdot \infty \cdot (\lim_{x \to \infty} \frac{\frac{d}{dx} (\ln{x})}{\frac{d}{dx} (x)} - 1)\\
& & \lim_{x \to \infty} f(x) &= \infty \cdot (\lim_{x \to \infty} \frac{1}{x} - 1)\\
& & \lim_{x \to \infty} f(x) &= \infty \cdot (\cancel{0} - 1)\\
& & \lim_{x \to \infty} f(x) &= - \infty\\
\end{align}
$$

From $f(\frac{8}{\ln{2}}) \approx 16.69$, we know that $f(x_i) > 0$. Also, by the Intermediate Value Theorem, since $f(x)$ is continuous on $(0, \infty)$ with a single critic point as a global maximum on $x_i$ and limits at both ends at $- \infty$, then $f(x)$ must have two roots. That is, there must must two values $x'$ and $x''$ such that $f(x') = 0$ with $0 < x' < x_i$ and $f(x'') = 0$ with $x_i < x'' < - \infty$.

For that, we will use a numerical analysis tool known as the Newton-Raphson method. This method comprises an iterative algorithm which consists on the construction of better approximations for a given root of an equation. In this case, $f(x)$. From an initial approximation $g_0$, each consecutive approximation is calculated by the following definition, being $g_x$ the $x$-th guess.

$$
\begin{align}
g_{x+1} = g_x - \frac{f(g_x)}{f'(g_x)}
\end{align}
$$

Choosing the first integer of each interval as a guess for finding each root, we get $g_0' = 1$ and $g_0'' = 12$. Also, we choose a tolerance value $\epsilon = $1\text{e-}4$, such that $|g_{k+1}-g_k| < \epsilon$ in order to halt the algorithm. Then, we compute $f(x)$ roots, showing up to 6 decimal places.

<div class="table-row" markdown>
|Iteration|$g'$|$\epsilon'$|
|:-:|:-:|:-:|
|0|1.000000|$-$|
|1|1.094863|0.094863|
|2|1.099984|0.005121|
|3|1.099997|0.000013|
</div>

<div class="table-row" markdown>
|Iteration|$g''$|$\epsilon''$|
|:-:|:-:|:-:|
|0|12.000000|$-$|
|1|448.603575|436.60357|
|2|60.489066|388.11450|
|3|44.250420|16.238646|
|4|43.561185|0.689235|
|5|43.559260|0.001925|
|6|43.559260|0.000000|
</div>

From that, we achieve $x' \approx 1.099997$ and $x'' \approx 43.559260$. Knowing that $f(x) > 0$ for $x' < x < x''$, the solution for the inequality must be the interval (1.099997, 43.559260).

Finally, accounting for the domain of $s_x(n)$ as $\mathbb{N}$, insertion sort will beat merge sort for $2 \le n \le 43$.

### 1.2-3
> What is the smallest value of n such that an algorithm whose running time is $100n^2$ runs faster than an algorithm whose running time is $2^n$ on the same machine?



