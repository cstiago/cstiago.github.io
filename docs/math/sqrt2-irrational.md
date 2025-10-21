# $\sqrt{2}$ is irrational

$\boxed{\text{Theorem A. } \sqrt{2} \notin \mathbb{Q}}$

$\text{Proof. }$

$\vdash \neg (\sqrt{2} \notin \mathbb{Q}) \implies \sqrt{2} \in \mathbb{Q}$

$\text{Definition B. } \mathbb{Q} := \{\frac{a}{b} \mid b \not= 0 \land \gcd(a, b) = 1\}$

Let $m, n \in \mathbb{Z}, n \not= 0, \gcd(m, n) = 1$:

$\sqrt{2} = \frac{m}{n}$

$(\sqrt{2})^2 = (\frac{m}{n})^2$

$2 = \frac{m^2}{n^2}$

$2n^2 = m^2$

$\text{Lemma C. } \forall a \in \mathbb{Z}: a^2 \equiv a \pmod 2$

$m^2 \equiv m \pmod 2$

$\text{Lemma D. } \forall a, b, c \in \mathbb{Z}: ab = c \implies a \mid c \land b \mid c$

$2n^2 = m^2 \implies 2 \mid m^2 \land n^2 \mid m^2$

$\text{Lemma E. } \forall a, b, c \in \mathbb{Z}: a \equiv b \pmod c \iff \exists d \in \mathbb{Z}(a = cd + b)$

$2n^2 = m^2 \implies m^2 \equiv 0 \pmod 2$

$m^2 \equiv 0 \pmod 2 \land m^2 \equiv m \pmod 2 \implies m \equiv 0 \pmod 2$

$\exists a \in \mathbb{Z}: m = 2a$

Let $k \in \mathbb{Z}: m = 2k$

$2n^2 = m^2$

$2n^2 = (2k)^2$

$2n^2 = 4k^2$

$n^2 = 2k^2$

$n^2 = 2k^2 \implies n^2 \equiv 0 \pmod 2$

$n^2 \equiv 0 \pmod 2 \land n^2 \equiv n \pmod 2 \implies n \equiv 0 \pmod 2$

$\exists a \in \mathbb{Z}: n = 2a$

Let $l \in \mathbb{Z}: n = 2l$

$\text{Lemma F. } \forall a, b, c, d, e \in \mathbb{Z}: a = cd \land b = ce \implies \gcd(a, b) \ge |c|$

$m = 2k \land n = 2l \implies \gcd(m, n) \ge 2 \text{↯}$

$\therefore \sqrt{2} \notin \mathbb{Q} \text{ } \square$
