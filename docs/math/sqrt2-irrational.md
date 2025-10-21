# $\sqrt{2}$ is irrational

$\boxed{\text{Theorem A. } \sqrt{2} \notin \mathbb{Q}}$

$\text{Proof. }$

01. $\vdash \neg (A)$

02. $(1) \implies \sqrt{2} \in \mathbb{Q}$

$\text{Definition B. } \mathbb{Q} := \{\frac{a}{b} \mid b \not= 0 \land \gcd(a, b) = 1\}$

03. $(B) \implies \forall x \in \mathbb{R}: x \in \mathbb{Q} \iff \exists a, b \in \mathbb{Z}(b \not= 0 \land \gcd(a, b) = 1 \land x = \frac{a}{b})$

04. $(2) \land (3) \implies \exists a, b \in \mathbb{Z}(b \not= 0 \land \gcd(a, b) = 1 \land \sqrt{2} = \frac{a}{b})$

5. Let $a, b \in \mathbb{Z}: \sqrt{2} = \frac{a}{b}$

06. $(5) \implies (\sqrt{2})^2 = (\frac{a}{b})^2$

07. $(6) \implies 2 = \frac{a^2}{b^2}$

08. $(7) \implies 2b^2 = a^2$

$\text{Lemma C. } \forall y \in \mathbb{Z}: y^2 \equiv y \pmod 2$

09. $(C) \land (4) \implies a^2 \equiv a \pmod 2$

$\text{Lemma D. } \forall z \in \mathbb{Z}: z \implies z^2 \in \mathbb{Z}$

$\text{Lemma E. } \forall m, n, o\in \mathbb{Z}: mn = o \implies m \mid o \land n \mid o$

10. $(4) \land (D) \implies b^2 \in \mathbb{Z}$

11. $(8) \land (10) \land (E) \implies 2 \mid a^2 \land b^2 \mid a^2$

$\text{Lemma F. } \forall i, j, k \in \mathbb{Z}: i \equiv j \pmod k \implies \exists l \in \mathbb{Z}(k > j \land i = lk + j)$

12. $(F) \implies i - j = lk$

13. $(E) \land (12) \implies l \mid (i-j) \land k \mid (i-j)$

14. $(9) \land (11) \implies 2 \mid a$

15. $(8) \land (14) \implies \exists p \in \mathbb{Z}(2b^2 = (2p)^2$

16. $(15) \implies 2b^2 = 4p^2$

17. $(16) \implies b^2 = 2p^2$

18. $(17) \land (D) \implies \exists r \in \mathbb{Z}(b^2 = 2r)$

19. $(18) \land (E) \implies 2 \mid b^2 \land r \mid b^2$

20. $(19) \land (C) \implies 2 \mid b$

$\text{Lemma G. } \forall s, t, u \in \mathbb{Z}: s \mid t \land s \mid u \implies \gcd(t, u) \ge s$

21. $(14) \land (20) \land (G) \implies \gcd(a, b) \ge 2$

22. $(21) \land (5) \implies \text{↯}$

23. $(22) \land (1) \implies (A)$

24. $\therefore \sqrt{2} \notin \mathbb{Q}$ $\square$

