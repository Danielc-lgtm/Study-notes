---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Product σ-Algebra"
  - "Thm - Dynkin's π-λ Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $(X_1,\mathcal{A}_1)$, $(X_2,\mathcal{A}_2)$ be measurable spaces and $E\in\mathcal{A}_1\otimes\mathcal{A}_2$.

**(a)** Show every slice $E_{x_1}=\{x_2:(x_1,x_2)\in E\}$ lies in $\mathcal{A}_2$, and every $E^{x_2}=\{x_1:(x_1,x_2)\in E\}$ in $\mathcal{A}_1$.

**(b)** Deduce: if $f:X_1\times X_2\to\mathbb{R}$ is $\mathcal{A}_1\otimes\mathcal{A}_2$-measurable, every slice $f(x_1,\cdot)$ is $\mathcal{A}_2$-measurable.

**Recall:**

![[Def - Product σ-Algebra#The Definition]]

[[Thm - Dynkin's π-λ Theorem|π–λ]]: a $\lambda$-system containing a generating $\pi$-system contains the whole $\sigma$-algebra.

---

# Convergent Strategy

**Problem class:** a "for all sets in a generated $\sigma$-algebra" statement — handled by the [[Thm - Dynkin's π-λ Theorem|π–λ]] / minimality principle.

**Assumption pattern:** "$E\in\mathcal{A}_1\otimes\mathcal{A}_2$" is membership in a *generated* $\sigma$-algebra; the property "$E$ has measurable slices" must be shown to (i) hold on the generating rectangles and (ii) define a $\sigma$-algebra (or $\lambda$-system).

**Theorem routing:** the family of good $E$ is a $\sigma$-algebra (slicing commutes with all set operations) containing the rectangles, hence contains $\sigma(\text{rectangles})=\mathcal{A}_1\otimes\mathcal{A}_2$.

---

# Legal Operations Used

1. **Slicing commutes with set operations** — $(E^c)_{x_1}=(E_{x_1})^c$, $(\bigcup E_n)_{x_1}=\bigcup(E_n)_{x_1}$.
2. **Minimality of the generated $\sigma$-algebra.**
3. **Reduce $f$ to its level sets** $\{f<a\}$.

---

# Hints

> [!note]- Hint 1
> Slicing is a Boolean homomorphism: $(E^c)_{x_1}=(E_{x_1})^c$ and $(\bigcup_n E_n)_{x_1}=\bigcup_n(E_n)_{x_1}$. So the good sets form a $\sigma$-algebra.

> [!note]- Hint 2
> The slice of a rectangle: $(A_1\times A_2)_{x_1}=A_2$ if $x_1\in A_1$, else $\emptyset$ — measurable.

> [!note]- Hint 3
> For (b): $\{x_2:f(x_1,x_2)<a\}=(\{f<a\})_{x_1}$.

---

# Solution

The proof breaks into two steps, one per sub-part. Step 1 (part a) defines the family $\mathcal{C}$ of sets with measurable slices, verifies it is a $\sigma$-algebra (using that slicing commutes with complement and countable union), checks rectangles lie in $\mathcal{C}$, and invokes minimality of the generated $\sigma$-algebra; Step 2 (part b) deduces slice-measurability of $f(x_1, \cdot)$ from slice-measurability of the level sets $\{f < a\}$. The non-obvious move is the recognition in Step 1 that slicing is a *Boolean homomorphism* — once that is in place, the entire proof is "the good sets form a $\sigma$-algebra containing the generators."

**Step 1 — (a).** Fix $x_1$ and let $\mathcal{C}=\{E\subseteq X_1\times X_2:E_{x_1}\in\mathcal{A}_2\}$.

> [!note]- Derivation
> $\mathcal{C}$ is a $\sigma$-algebra: $(X_1\times X_2)_{x_1}=X_2\in\mathcal{A}_2$; $(E^c)_{x_1}=\{x_2:(x_1,x_2)\notin E\}=(E_{x_1})^c\in\mathcal{A}_2$; $(\bigcup_n E_n)_{x_1}=\bigcup_n(E_n)_{x_1}\in\mathcal{A}_2$ — slicing commutes with complement and countable union. And $\mathcal{C}$ contains every rectangle: $(A_1\times A_2)_{x_1}$ equals $A_2$ (if $x_1\in A_1$) or $\emptyset$ (otherwise), both in $\mathcal{A}_2$. Since $\mathcal{C}$ is a $\sigma$-algebra containing the rectangles, and $\mathcal{A}_1\otimes\mathcal{A}_2$ is the *smallest* such, $\mathcal{A}_1\otimes\mathcal{A}_2\subseteq\mathcal{C}$. So every $E\in\mathcal{A}_1\otimes\mathcal{A}_2$ has $E_{x_1}\in\mathcal{A}_2$. The $E^{x_2}$ statement is symmetric.

**Step 2 — (b).** For $f$ measurable and $a\in\mathbb{R}$, $\{f<a\}\in\mathcal{A}_1\otimes\mathcal{A}_2$, so by (a) its slice $(\{f<a\})_{x_1}=\{x_2:f(x_1,x_2)<a\}\in\mathcal{A}_2$. As this holds for every $a$, the slice $f(x_1,\cdot)$ is $\mathcal{A}_2$-measurable.

> [!note]- Complete formal solution
> (a) $\mathcal{C}=\{E:E_{x_1}\in\mathcal{A}_2\}$ is a $\sigma$-algebra (slicing commutes with $^c,\bigcup$) containing all rectangles, hence $\supseteq\mathcal{A}_1\otimes\mathcal{A}_2$. (b) $\{f(x_1,\cdot)<a\}$ is the slice of the measurable set $\{f<a\}$, hence in $\mathcal{A}_2$ for all $a$. $\blacksquare$

---

# Key Takeaways

**Slices of product-measurable sets are measurable — and the proof is, once again, "the good sets form a $\sigma$-algebra containing the generators."** Slicing at a fixed $x_1$ is a Boolean homomorphism, so it preserves $\sigma$-algebra structure; the only computation is the slice of a rectangle. This is the same minimality skeleton as [[Ex - Measurability via a generating set|measurability via generators]] — and it is the *first* lemma in the construction of [[Thm - Product Measure|product measures]] and [[Thm - Fubini-Tonelli Theorem|Fubini's theorem]], because both speak of integrating slice functions.

**Measurability of the *slice function* $f(x_1,\cdot)$ is immediate; measurability of the *slice-integral* $x_1\mapsto\int f(x_1,\cdot)$ is the genuinely hard fact** — that one needs the [[Thm - Dynkin's π-λ Theorem|π–λ theorem]] with a $\lambda$-system (not a $\sigma$-algebra), because the integral does not commute with all set operations. The two should not be conflated: this exercise is the easy half that Fubini's construction takes for granted.
