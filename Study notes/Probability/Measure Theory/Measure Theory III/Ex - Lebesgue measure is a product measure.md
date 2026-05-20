---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Product Measure"
  - "Def - Lebesgue Measure"
  - "Thm - Dynkin's π-λ Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

**(a)** Show $\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R})=\mathcal{B}(\mathbb{R}^2)$ — the Borel sets of the plane are the product $\sigma$-algebra.

**(b)** Show $\lambda_1\otimes\lambda_1=\lambda_2$ — planar Lebesgue measure is the product of two copies of one-dimensional Lebesgue measure. More generally $\lambda_m\otimes\lambda_n=\lambda_{m+n}$.

**(c)** Explain why the *Lebesgue* $\sigma$-algebras do **not** multiply: $\mathcal{B}^*(\mathbb{R})\otimes\mathcal{B}^*(\mathbb{R})\subsetneq\mathcal{B}^*(\mathbb{R}^2)$.

**Recall:**

[[Thm - Product Measure|Product measure]]: for $\sigma$-finite $\mu_i$, a unique measure on $\mathcal{A}_1\otimes\mathcal{A}_2$ with $(\mu_1\otimes\mu_2)(A_1\times A_2)=\mu_1(A_1)\mu_2(A_2)$. [[Thm - Dynkin's π-λ Theorem|Uniqueness]]: agree on a generating $\pi$-system.

---

# Convergent Strategy

**Problem class:** identifying a known measure as a product — and seeing where completion breaks the pattern.

**Assumption pattern:** both $\lambda_2$ and $\lambda_1\otimes\lambda_1$ are $\sigma$-finite measures on $\mathcal{B}(\mathbb{R}^2)$; to prove them equal, show they agree on a generating $\pi$-system — the **boxes**.

**Theorem routing:** boxes generate $\mathcal{B}(\mathbb{R}^2)$ and are a $\pi$-system; both measures give a box $\prod(a_i,b_i)$ the value $\prod(b_i-a_i)$; [[Thm - Dynkin's π-λ Theorem|uniqueness]] finishes.

**Key decision point:** for (c), the obstruction is *completeness* — the product of complete $\sigma$-algebras is not complete.

---

# Legal Operations Used

1. **Generate from boxes** — open sets are countable unions of boxes.
2. **$\pi$–$\lambda$ uniqueness** — agree on the box $\pi$-system.
3. **Completion is not preserved by products.**

---

# Hints

> [!note]- Hint 1
> Every open set of $\mathbb{R}^2$ is a countable union of open boxes $B_1\times B_2$. So $\mathcal{B}(\mathbb{R}^2)\subseteq\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R})$; the reverse is clear.

> [!note]- Hint 2
> $\lambda_2$ and $\lambda_1\otimes\lambda_1$ are both $\sigma$-finite and agree on boxes (a $\pi$-system generating $\mathcal{B}(\mathbb{R}^2)$). Apply uniqueness.

> [!note]- Hint 3
> For (c): take a $\lambda_1$-null non-measurable... rather, take a non-Borel $N\subseteq\mathbb{R}$ inside a Lebesgue-null set and consider $N\times\{0\}$. It is $\lambda_2$-null hence Lebesgue-measurable in the plane — but is it in the product $\sigma$-algebra?

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) identifies $\mathcal{B}(\mathbb{R}^2) = \mathcal{B}(\mathbb{R}) \otimes \mathcal{B}(\mathbb{R})$ by observing every open set in $\mathbb{R}^2$ is a countable union of rational open boxes; Step 2 (part b) applies Dynkin's uniqueness theorem on the $\pi$-system of boxes — both $\lambda_2$ and $\lambda_1 \otimes \lambda_1$ are $\sigma$-finite and agree on boxes, so they agree on the generated $\sigma$-algebra; Step 3 (part c) exhibits $N \times \{0\}$ for a non-Borel $N$ inside a $\lambda_1$-null set as a member of $\mathcal{B}^*(\mathbb{R}^2)$ that is *not* in $\mathcal{B}^*(\mathbb{R}) \otimes \mathcal{B}^*(\mathbb{R})$, because its slice analysis would force $N$ measurable. The non-obvious move is in Step 3 — the section-measurability constraint of the product $\sigma$-algebra is exactly what *fails* completion, since a null slab over a non-measurable base is invisible to $\lambda_2$ but visible to the slices.

**Step 1 — (a).** Every open box $B_1\times B_2$ ($B_i$ open in $\mathbb{R}$) is open in $\mathbb{R}^2$, and every open $U\subseteq\mathbb{R}^2$ is a countable union of open boxes (rational boxes). So $\mathcal{B}(\mathbb{R}^2)=\sigma(\text{open})\subseteq\sigma(\text{boxes})=\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R})$. Conversely a box $B_1\times B_2$ is Borel in $\mathbb{R}^2$, so $\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R})\subseteq\mathcal{B}(\mathbb{R}^2)$. Equality.

**Step 2 — (b).** $\lambda_2$ and $\lambda_1\otimes\lambda_1$ are both measures on $\mathcal{B}(\mathbb{R}^2)$, both $\sigma$-finite (tile by unit squares). On a box, $\lambda_2(\prod(a_i,b_i))=\prod(b_i-a_i)=(b_1-a_1)(b_2-a_2)=(\lambda_1\otimes\lambda_1)(\prod(a_i,b_i))$. The boxes form a $\pi$-system generating $\mathcal{B}(\mathbb{R}^2)$, with the plane a countable union of finite-measure boxes; by [[Thm - Dynkin's π-λ Theorem|Dynkin's uniqueness corollary]], the two measures coincide. The same argument gives $\lambda_m\otimes\lambda_n=\lambda_{m+n}$.

**Step 3 — (c).** Let $N\subseteq\mathbb{R}$ be a subset of a $\lambda_1$-null set that is not Borel (most subsets of the Cantor set, by [[Ex - Lebesgue sets are Borel modulo a null set|cardinality]]). Consider $E=N\times\{0\}\subseteq\mathbb{R}^2$.

> [!note]- Derivation
> $E$ is a subset of $\mathbb{R}\times\{0\}$, a $\lambda_2$-null set, so $E$ is $\lambda_2$-Lebesgue-measurable (by [[Ex - Null sets are Carathéodory measurable|completeness]] of $\lambda_2$): $E\in\mathcal{B}^*(\mathbb{R}^2)$. But $E\notin\mathcal{B}^*(\mathbb{R})\otimes\mathcal{B}^*(\mathbb{R})$: every slice $E_x=\{y:(x,y)\in E\}$ is $\{0\}$ if $x\in N$, $\emptyset$ otherwise, and the slice of a product-$\sigma$-algebra set is measurable *with the additional structure* — in fact $E\in\mathcal{B}^*(\mathbb{R})\otimes\mathcal{B}^*(\mathbb{R})$ would force, by the slice/section analysis, $N=\{x:E_x\ni0\}$ to be $\mathcal{B}^*(\mathbb{R})$-measurable; but $N$ was chosen non-(Lebesgue-)measurable. Contradiction. So $\mathcal{B}^*(\mathbb{R})\otimes\mathcal{B}^*(\mathbb{R})\subsetneq\mathcal{B}^*(\mathbb{R}^2)$.

The product of complete $\sigma$-algebras fails completeness because a "vertical segment" $N\times\{0\}$ over a non-measurable base, though $\lambda_2$-null, exposes the base $N$ through its sections.

> [!note]- Complete formal solution
> (a) Open boxes generate both $\mathcal{B}(\mathbb{R}^2)$ and $\mathcal{B}(\mathbb{R})\otimes\mathcal{B}(\mathbb{R})$. (b) $\lambda_2,\lambda_1\otimes\lambda_1$ agree on boxes (a generating $\pi$-system, $\sigma$-finite exhaustion); Dynkin uniqueness $\Rightarrow$ equal. (c) For non-measurable $N$ inside a null set, $N\times\{0\}$ is $\lambda_2$-null (so in $\mathcal{B}^*(\mathbb{R}^2)$) but its section structure would force $N$ measurable if it lay in $\mathcal{B}^*(\mathbb{R})\otimes\mathcal{B}^*(\mathbb{R})$; so the product $\sigma$-algebra is strictly smaller. $\blacksquare$

---

# Key Takeaways

**Lebesgue measure on $\mathbb{R}^n$ *is* an $n$-fold product — and the proof is the universal "agree on a generating $\pi$-system" move.** Any two $\sigma$-finite measures coinciding on a $\pi$-system that generates the $\sigma$-algebra are equal ([[Thm - Dynkin's π-λ Theorem|Dynkin]]); boxes are that $\pi$-system for $\mathbb{R}^n$. This makes high-dimensional integration a matter of iterated one-dimensional integration via [[Thm - Fubini-Tonelli Theorem|Fubini]], and it is why $\lambda_n$ never had to be constructed separately for each $n$.

**Completion does not commute with products — the *Borel* $\sigma$-algebras multiply cleanly, the *Lebesgue* ones do not.** A null "slab" over a non-measurable base is $\lambda_n$-measurable by completeness yet escapes the product $\sigma$-algebra, because its sections reveal the bad base. The practical rule: take products *first*, complete *afterwards*. This is the same reason [[Thm - Fubini-Tonelli Theorem|Fubini]] for Lebesgue-measurable (as opposed to Borel) functions needs the "$\mu_1$-a.e. $x_1$" hedge on the sections.
