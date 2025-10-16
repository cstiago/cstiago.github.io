# Proof that $\sqrt{2}$ is irrational

$\boxed{\text{Proposition. } \sqrt{2} \text{ is irrational.}}$

## Definitions

$$\forall x \in \mathbb{Q} \iff \forall a, b \in \mathbb{Z}(b \not= 0 \land \gcd(a, b) = 1 \land x = \frac{a}{b}) {{label('def-q')}}$$

$$\forall x \in \mathbb{Z}(x^2\pmod 2 \equiv x\pmod 2) {{label('def-parity')}}$$

## Proof

Assume that $\sqrt{2} \in \mathbb{Q}$, which for some $a, b \in \mathbb{Z}$, can be expressed as an irreducible fraction in the form of $\sqrt{2} = \frac{a}{b}$, given $b \ne 0$ and $\gcd(a, b) = 1$.

Squaring both sides of the equation, $(\sqrt{2})^2 = (\frac{a}{b})^2$. Applying radical and exponent properties, $2 = \frac{a^2}{b^2}$. Multiplying both sides by $b^2$, $a^2 = 2b^2$.

Since $b \in \mathbb{Z}$, then by the properties of multiplication, $b^2 \in \mathbb{Z}$ as well. From that, for some $c \in \mathbb{Z}$, $a^2$ can be expressed as $a^2 = 2c$, so $a^2$ is an even number.

A fundamental property of integers is that for any $d \in \mathbb{Z}$, if $d^2$ is even, then $d$ is even as well. Then $a$ is even.

Since $a$ is even, it can be represented as $2e$ for some $e \in \mathbb{Z}$. From $a^2 = 2b^2$, substituting $a$ yields $(2e)^2 = 2b^2$. Applying exponent property on the left term, $4e^2 = 2b^2$. Dividing both sides by 2, $2e^2 = b^2$. Since $e^2 \in \mathbb{Z}$, $b^2$ is even, so $b$ is also even.

Concluding that both $a$ and $b$ are even numbers, it means that $a$ and $b$ share a common factor of 2, implying that $\gcd(a, b) \ge 2$, which contradicts the initial assumption that $\gcd(a, b) = 1$.

Therefore, $\sqrt{2}$ is irrational. $\square$ 

