# $\sqrt{2}$ is irrational

$\boxed{\text{Theorem A. } \sqrt{2} \notin \mathbb{Q}}$

$\text{Proof. }$

$\vdash \neg A$

$$
\begin{align}
\neg (\sqrt{2} &\notin \mathbb{Q})\\
\sqrt{2} &\in \mathbb{Q}
\end{align}
$$

$\text{Definition B. } \mathbb{Q} := \{\frac{a}{b} \mid b \not= 0 \land \gcd(a, b) = 1\}$

$(m, n) := (a, b) \in \mathbb{Z}^2: b \not= 0 \land \gcd(a, b) = 1 \land \sqrt{2} = \frac{a}{b}$

$$
\begin{align}\\
\sqrt{2} &= \frac{m}{n}\\
(\sqrt{2})^2 &= (\frac{m}{n})^2\\
2 &= \frac{m^2}{n^2}\\
2n^2 &= m^2
\end{align}
$$

$\text{Lemma C. } \forall a \in \mathbb{Z}: a^2 \equiv a \pmod 2$

$$
\begin{align}
m^2 &\equiv m \pmod 2
\end{align}
$$

$\text{Lemma D. } \forall a, b, c \in \mathbb{Z}: a \equiv b \pmod c \iff \exists d \in \mathbb{Z}(a = cd + b)$

$$
\begin{align}
2n^2 &= m^2\\
m^2 &\equiv 0 \pmod 2
\end{align}
$$


$m^2 \equiv m \pmod 2 \land m^2 \equiv 0 \pmod 2 \implies m \equiv 0 \pmod 2$

$$
\begin{align}
\exists a \in \mathbb{Z}: m &= 2a
\end{align}
$$

$k := a \in \mathbb{Z}: m = 2a$

$$
\begin{align}
2n^2 &= m^2\\
2n^2 &= (2k)^2\\
2n^2 &= 4k^2\\
n^2 &= 2k^2\\
n^2 &\equiv 0 \pmod 2
\end{align}
$$

$n^2 \equiv 0 \pmod 2 \land n^2 \equiv n \pmod 2 \implies n \equiv 0 \pmod 2$

$$
\begin{align}
\exists a \in \mathbb{Z}: n &= 2a
\end{align}
$$

$l := a \in \mathbb{Z}: n = 2a$

$\text{Lemma E. } \forall a, b, c \in \mathbb{Z}: c \mid a \land c \mid b \implies \gcd(a, b) \ge |c|$

$m = 2k \land n = 2l \implies 2 \mid m \land 2 \mid n \implies \gcd(m, n) \ge 2 \text{ ↯}$

$\therefore \sqrt{2} \notin \mathbb{Q} \text{ } \square$

