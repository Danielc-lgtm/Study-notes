---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - Integral Closure and Normal Domain"
  - "Def - Field of Fractions"
  - "Thm - The Integral Closure is a Subring"
  - "Thm - A UFD is Integrally Closed"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A = \mathbb{Z}[\sqrt5] = \{a + b\sqrt5 : a, b \in \mathbb{Z}\}$. Prove that $A$ is **not** integrally closed in its field of fractions $\operatorname{Frac}(A) = \mathbb{Q}(\sqrt5)$, by exhibiting an element of $\mathbb{Q}(\sqrt5) \setminus A$ that is integral over $A$. Then identify the integral closure $\overline A$.

Concretely: show that $\alpha = \dfrac{1 + \sqrt5}{2}$ lies in $\mathbb{Q}(\sqrt5) \setminus \mathbb{Z}[\sqrt5]$, is integral over $\mathbb{Z}$ (hence over $A$), and that $\overline A = \mathbb{Z}\big[\tfrac{1+\sqrt5}2\big] \supsetneq \mathbb{Z}[\sqrt5]$.

**Recall:**

The objects in play are integral elements, the integral closure, the field of fractions, and normality.

![[Def - Integral Element and Integral Extension#The Definition]]

![[Def - Integral Closure and Normal Domain#The Definition]]

A domain $A$ is [[Def - Integral Closure and Normal Domain|integrally closed]] (normal) if every element of $\operatorname{Frac}(A)$ integral over $A$ already lies in $A$. To *disprove* normality, exhibit one element of $\operatorname{Frac}(A) \setminus A$ that is integral.

![[Thm - A UFD is Integrally Closed#Statement]]

The field of fractions here is $\operatorname{Frac}(\mathbb{Z}[\sqrt5]) = \mathbb{Q}(\sqrt5) = \{p + q\sqrt5 : p, q \in \mathbb{Q}\}$, since inverting nonzero elements of $\mathbb{Z}[\sqrt5]$ yields exactly the rational combinations of $1$ and $\sqrt5$.

---

# Convergent Strategy

**Problem class.** This is a *disprove-normality-by-exhibiting-a-missing-integer* problem — the counterweight to [[Ex - The integral closure of Z in Q is Z]]. It shows that "$A$ integrally closed" can *fail*, and that the failure is exactly a "missing algebraic integer" lurking in the fraction field. It also computes a normalization, exercising operation 5 (the sandwich) from the [[Commutative Algebra VI — Integral Extensions#Legal Operations|topic page]].

**Assumption pattern.** The recognisable trigger is that $A = \mathbb{Z}[\sqrt5]$ is *not* a UFD-like ring at the half-integer level: $5 \equiv 1 \pmod 4$, which is precisely the arithmetic condition that makes $\tfrac{1+\sqrt5}2$ an algebraic integer. The hypothesis to leverage is that the *quadratic* $T^2 - T - 1$ has the golden ratio as a root — a monic integer polynomial, certifying integrality.

**Theorem routing.** Three moves. (i) Show $\alpha = \tfrac{1+\sqrt5}2 \notin \mathbb{Z}[\sqrt5]$ directly (its $\sqrt5$-coefficient is $\tfrac12$). (ii) Show $\alpha$ is integral over $\mathbb{Z}$, hence over $A$, by producing the monic $T^2 - T - 1$. Together (i)+(ii) prove $A$ is not normal. (iii) To identify $\overline A = \mathbb{Z}[\alpha]$, run the sandwich: $\mathbb{Z}[\alpha]$ is integral over $A$ (so $\subseteq \overline A$) and is *itself* normal (it is a PID / Euclidean, hence a UFD, so [[Thm - A UFD is Integrally Closed|integrally closed]], capping $\overline A$ from above).

**Key decision point.** The non-obvious step is *guessing* $\alpha = \tfrac{1+\sqrt5}2$ rather than $\sqrt5$ or some other candidate. The heuristic: for $\mathbb{Q}(\sqrt d)$ with $d \equiv 1 \pmod 4$, the ring of integers is $\mathbb{Z}[\tfrac{1+\sqrt d}2]$, not $\mathbb{Z}[\sqrt d]$, because $\tfrac{1+\sqrt d}2$ satisfies the monic $T^2 - T - \tfrac{d-1}4$ with *integer* constant term exactly when $d \equiv 1 \pmod 4$. Recognising that the half-integer combination can be integral is the whole insight.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VI — Integral Extensions#Legal Operations|the topic page's Legal Operations]]:

1. **Prove integrality by exhibiting a monic equation (operation 1).** Produce $T^2 - T - 1$ for $\alpha = \tfrac{1+\sqrt5}2$ by direct computation of $\alpha^2$.

2. **Compute a closure by the sandwich $A \subseteq A' \subseteq \operatorname{Frac}(A)$ (operation 5).** Take $A' = \mathbb{Z}[\alpha]$; show it is integral over $A$ and already normal.

3. **Disprove integrality / cap a closure with a normal ring (operation 4).** Use that $\mathbb{Z}[\alpha]$ is a UFD (Euclidean), hence integrally closed, so $\overline A \subseteq \mathbb{Z}[\alpha]$.

4. **Membership test by coordinates.** Check $\alpha \notin \mathbb{Z}[\sqrt5]$ by reading off that its coefficient of $\sqrt5$ is $\tfrac12 \notin \mathbb{Z}$.

---

# Hints

> [!note]- Hint 1
> To show $A$ is not normal, you only need *one* element of $\mathbb{Q}(\sqrt5)$ that is outside $\mathbb{Z}[\sqrt5]$ but satisfies a monic equation over $\mathbb{Z}$. The "obvious" elements ($\sqrt5$, $1 + \sqrt5$) are already in $A$. Try a *half-integer* combination. Which one is famous for satisfying a nice quadratic?

> [!note]- Hint 2
> Consider $\alpha = \tfrac{1+\sqrt5}2$, the golden ratio. Compute $\alpha^2$ and look for a relation among $\alpha^2$, $\alpha$, $1$. (You should find $\alpha^2 = \alpha + 1$.) That gives a monic equation. Separately, why is $\alpha \notin \mathbb{Z}[\sqrt5]$? Write $\alpha = \tfrac12 + \tfrac12\sqrt5$ and look at the coefficients.

> [!note]- Hint 3
> For the closure: $\mathbb{Z}[\alpha]$ contains $\mathbb{Z}[\sqrt5]$ (since $\sqrt5 = 2\alpha - 1$) and is integral over it. To show $\overline A$ is *exactly* $\mathbb{Z}[\alpha]$ and no bigger, show $\mathbb{Z}[\alpha]$ is integrally closed — and the cleanest way is to show it is a Euclidean domain (with the norm $N(a + b\alpha)$), hence a PID, hence a UFD, hence normal.

---

# Solution

The plan: (1) verify $\alpha = \tfrac{1+\sqrt5}2$ is a genuine "missing" element — integral over $\mathbb{Z}$ but outside $\mathbb{Z}[\sqrt5]$ — which already proves non-normality; (2) identify the integral closure as $\mathbb{Z}[\alpha]$ by the sandwich, using that $\mathbb{Z}[\alpha]$ is a UFD hence normal. The crux is the half-integer guess: $5 \equiv 1 \pmod 4$ is what lets $\tfrac{1+\sqrt5}2$ satisfy a monic integer polynomial.

**Step 1: $\alpha = \tfrac{1+\sqrt5}2$ is integral over $\mathbb{Z}$.**

$\alpha$ satisfies the monic $T^2 - T - 1 = 0$, so it is integral over $\mathbb{Z}$, hence over $A = \mathbb{Z}[\sqrt5]$.

> [!note]- Derivation
> Compute:
> $$\alpha^2 = \Big(\frac{1+\sqrt5}{2}\Big)^2 = \frac{1 + 2\sqrt5 + 5}{4} = \frac{6 + 2\sqrt5}{4} = \frac{3 + \sqrt5}{2}.$$
> Now $\frac{3+\sqrt5}2 = \frac{1+\sqrt5}2 + \frac{2}{2} = \alpha + 1$. So $\alpha^2 = \alpha + 1$, i.e.
> $$\alpha^2 - \alpha - 1 = 0.$$
> This is a [[Def - Integral Element and Integral Extension|monic]] polynomial $T^2 - T - 1 \in \mathbb{Z}[T]$ with $\alpha$ as a root, so $\alpha$ is integral over $\mathbb{Z}$. Since $\mathbb{Z} \subseteq A$, the same monic equation has coefficients in $A$, so $\alpha$ is integral over $A$.

**Step 2: $\alpha \notin \mathbb{Z}[\sqrt5]$.**

Writing $\alpha = \tfrac12 + \tfrac12\sqrt5$, its coefficient of $\sqrt5$ is $\tfrac12 \notin \mathbb{Z}$, so $\alpha \notin \mathbb{Z}[\sqrt5]$. Hence $A$ is not integrally closed.

> [!note]- Derivation
> Every element of $\mathbb{Z}[\sqrt5]$ has the form $a + b\sqrt5$ with $a, b \in \mathbb{Z}$ — and this representation is *unique*, because $1$ and $\sqrt5$ are linearly independent over $\mathbb{Q}$ ($\sqrt5$ is irrational). Now $\alpha = \frac{1+\sqrt5}2 = \frac12 + \frac12\sqrt5$, so if $\alpha = a + b\sqrt5$ with $a, b \in \mathbb{Z}$, uniqueness forces $b = \frac12 \notin \mathbb{Z}$ — contradiction. So $\alpha \notin \mathbb{Z}[\sqrt5]$.
>
> Combining Steps 1 and 2: $\alpha \in \mathbb{Q}(\sqrt5) \setminus \mathbb{Z}[\sqrt5]$ is integral over $A$. By definition, $A = \mathbb{Z}[\sqrt5]$ is **not** [[Def - Integral Closure and Normal Domain|integrally closed]] in $\operatorname{Frac}(A) = \mathbb{Q}(\sqrt5)$.

**Step 3: The integral closure is $\overline A = \mathbb{Z}[\alpha]$.**

$\mathbb{Z}[\alpha]$ is integral over $A$ (so $\subseteq \overline A$) and is itself integrally closed (so $\supseteq \overline A$), giving $\overline A = \mathbb{Z}[\alpha] = \mathbb{Z}[\tfrac{1+\sqrt5}2]$.

> [!note]- Derivation
> *$\mathbb{Z}[\alpha] \subseteq \overline A$.* First $A \subseteq \mathbb{Z}[\alpha]$, since $\sqrt5 = 2\alpha - 1 \in \mathbb{Z}[\alpha]$. The generator $\alpha$ is integral over $A$ (Step 1), so $\mathbb{Z}[\alpha] = A[\alpha]$ is generated over $A$ by an integral element; by [[Thm - The Integral Closure is a Subring|the closure being a subring]] every element of $A[\alpha]$ is integral over $A$. Hence $\mathbb{Z}[\alpha] \subseteq \overline A$.
>
> *$\overline A \subseteq \mathbb{Z}[\alpha]$.* It suffices that $\mathbb{Z}[\alpha]$ is integrally closed in $\mathbb{Q}(\sqrt5) = \operatorname{Frac}(\mathbb{Z}[\alpha])$: then any element of $\operatorname{Frac}(A)$ integral over $A$ is integral over $\mathbb{Z}[\alpha]$ (it is a larger ring), hence lies in $\mathbb{Z}[\alpha]$. Now $\mathbb{Z}[\alpha]$ is the ring of integers $\mathcal{O}_{\mathbb{Q}(\sqrt5)}$, and it is a **Euclidean domain** for the norm $N(a + b\alpha) = |\,(a+b\alpha)(a + b\bar\alpha)\,|$ (where $\bar\alpha = \tfrac{1-\sqrt5}2$): one checks $\mathbb{Q}(\sqrt5)$ has a Euclidean algorithm with respect to this norm because every element of $\mathbb{Q}(\sqrt5)$ is within norm-distance $< 1$ of a lattice point of $\mathbb{Z}[\alpha]$. A Euclidean domain is a [[Def - Principal Ideal Domain|PID]], hence a [[Def - Unique Factorization Domain|UFD]], hence integrally closed by [[Thm - A UFD is Integrally Closed|"a UFD is integrally closed"]]. So $\overline A \subseteq \mathbb{Z}[\alpha]$.
>
> Therefore $\overline A = \mathbb{Z}[\alpha] = \mathbb{Z}\big[\tfrac{1+\sqrt5}2\big]$, strictly larger than $\mathbb{Z}[\sqrt5]$.

> [!note]- Complete formal solution
> **Claim.** $\mathbb{Z}[\sqrt5]$ is not integrally closed; its integral closure is $\mathbb{Z}[\tfrac{1+\sqrt5}2]$.
>
> Let $\alpha = \tfrac{1+\sqrt5}2$. Then $\alpha^2 = \tfrac{6 + 2\sqrt5}4 = \tfrac{3+\sqrt5}2 = \alpha + 1$, so $\alpha^2 - \alpha - 1 = 0$: $\alpha$ is integral over $\mathbb{Z}$, hence over $A = \mathbb{Z}[\sqrt5]$. But $\alpha = \tfrac12 + \tfrac12\sqrt5$ has half-integer $\sqrt5$-coefficient, so $\alpha \notin \mathbb{Z}[\sqrt5]$ (using that $1, \sqrt5$ are $\mathbb{Q}$-independent). Thus $\alpha \in \operatorname{Frac}(A) \setminus A$ is integral over $A$, and $A$ is not integrally closed.
>
> For the closure: $A \subseteq \mathbb{Z}[\alpha]$ since $\sqrt5 = 2\alpha - 1$; and $\mathbb{Z}[\alpha] = A[\alpha]$ with $\alpha$ integral over $A$, so $\mathbb{Z}[\alpha] \subseteq \overline A$ by [[Thm - The Integral Closure is a Subring|closure-is-a-subring]]. Conversely $\mathbb{Z}[\alpha]$ is a Euclidean domain (norm $N(a+b\alpha) = |(a+b\alpha)(a+b\bar\alpha)|$, $\bar\alpha = \tfrac{1-\sqrt5}2$), hence a PID, hence a UFD, hence integrally closed by [[Thm - A UFD is Integrally Closed]]; so $\overline A \subseteq \mathbb{Z}[\alpha]$. Therefore $\overline A = \mathbb{Z}[\tfrac{1+\sqrt5}2] \supsetneq \mathbb{Z}[\sqrt5]$. $\blacksquare$

---

# Key Takeaways

**Non-normality is a "missing algebraic integer", and you disprove normality by producing exactly one.** To show a domain is *not* integrally closed, you do not need to understand the whole integral closure — you need a single witness: one element of the fraction field, outside the ring, satisfying a monic equation. Here it is the golden ratio $\tfrac{1+\sqrt5}2$. The general pattern: when a ring $\mathbb{Z}[\sqrt d]$ with $d \equiv 1 \pmod 4$ appears, suspect immediately that $\tfrac{1+\sqrt d}2$ is a missing integer (it satisfies $T^2 - T - \tfrac{d-1}4$, monic over $\mathbb{Z}$ exactly when $4 \mid d - 1$). This is why $\mathbb{Z}[\sqrt5]$, $\mathbb{Z}[\sqrt{13}]$, $\mathbb{Z}[\sqrt{-3}]$ are all non-normal while $\mathbb{Z}[\sqrt2]$, $\mathbb{Z}[\sqrt3]$ ($d \equiv 2, 3 \pmod 4$) are normal. The diagnostic — "is there a half-integer combination satisfying a monic?" — generalises to detecting non-normality at any prime.

**Computing a closure is a sandwich: build it from below, cap it from above with normality.** The integral closure $\overline A$ is pinned down by two inequalities. From below: any ring $A' = A[\text{integral elements}]$ lies in $\overline A$, by [[Thm - The Integral Closure is a Subring|closure-is-a-subring]]. From above: if your candidate $A'$ is *itself normal* (most easily, a UFD), then $\overline A \subseteq A'$, because $\overline A$ is integral over $A$, hence over $A'$, hence inside the normal ring $A'$. When the two candidates coincide you have computed the closure. The capping step is where [[Thm - A UFD is Integrally Closed|"a UFD is integrally closed"]] earns its keep: it is the standard certificate that "the closure cannot be any bigger than this". This sandwich is the universal method for normalizations — used identically for the cusp $k[t^2,t^3]$ in [[Ex - The integral closure of k[t^2,t^3] resolves the cusp]].

**The naive ring $\mathbb{Z}[\sqrt d]$ is usually the wrong "ring of integers", and that is why one must take the full integral closure.** The lesson with the longest reach: in algebraic number theory, the ring of integers $\mathcal{O}_K$ of $K = \mathbb{Q}(\sqrt d)$ is the *integral closure* of $\mathbb{Z}$ in $K$, and it is strictly larger than the obvious $\mathbb{Z}[\sqrt d]$ whenever $d \equiv 1 \pmod 4$. Working with $\mathbb{Z}[\sqrt5]$ instead of $\mathbb{Z}[\tfrac{1+\sqrt5}2]$ would give wrong answers for ideal factorization, discriminants, and class numbers — the smaller ring is non-normal and not Dedekind. This is the concrete reason the chapter insists on the *full* integral closure rather than any convenient subring: only the integrally closed ring has unique factorization of ideals. Whenever you see $\mathbb{Z}[\sqrt d]$ in a number-theory problem, check $d \bmod 4$ before trusting it to be the ring of integers.
