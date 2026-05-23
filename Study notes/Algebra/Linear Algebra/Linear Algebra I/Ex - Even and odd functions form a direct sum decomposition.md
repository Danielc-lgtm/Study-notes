---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
  - "Def - Sum of Subspaces"
  - "Def - Direct Sum"
  - "Thm - Direct Sum of Two Subspaces"
tags: [algebra, linear-algebra]
---

# Problem Statement

A function $f : \mathbb{R} \to \mathbb{R}$ is **even** if $f(-x) = f(x)$ for all $x \in \mathbb{R}$, and **odd** if $f(-x) = -f(x)$ for all $x$.

Let $V_e \subseteq \mathbb{R}^\mathbb{R}$ be the set of even functions and $V_o \subseteq \mathbb{R}^\mathbb{R}$ the set of odd functions.

Show that $V_e$ and $V_o$ are [[Def - Subspace|subspaces]] of $\mathbb{R}^\mathbb{R}$, and that

$$\mathbb{R}^\mathbb{R} = V_e \oplus V_o.$$

In other words, every real-valued function on $\mathbb{R}$ has a unique decomposition as a sum of an even function and an odd function.

(LADR Exercise 1C.24.)

**Recall:**

The space $\mathbb{R}^\mathbb{R}$ is the [[Def - Vector Space|vector space]] of all functions $\mathbb{R} \to \mathbb{R}$ under pointwise operations: $(f + g)(x) = f(x) + g(x)$ and $(\lambda f)(x) = \lambda f(x)$.

A [[Def - Subspace|subspace]] satisfies the closure conditions:

![[Def - Subspace#The Definition]]

The [[Def - Direct Sum|direct sum]] $V_e \oplus V_o$ means $V_e + V_o = \mathbb{R}^\mathbb{R}$ and the decomposition of every function is unique. By [[Thm - Direct Sum of Two Subspaces]], the directness is equivalent to $V_e \cap V_o = \{0\}$.

---

# Convergent Strategy

**Problem class:** This is a **direct-sum decomposition** problem of the form "exhibit two subspaces and show they decompose the whole space directly". Such problems decompose into three pieces: (a) the two candidates are subspaces, (b) their intersection is trivial (so the sum is direct, by [[Thm - Direct Sum of Two Subspaces]]), (c) their sum is everything.

**Assumption pattern:** Functions $\mathbb{R} \to \mathbb{R}$, the parity conditions $f(-x) = \pm f(x)$. Pointwise operations on $\mathbb{R}^\mathbb{R}$. The proof exploits the *algebraic* structure of "evaluation at $-x$" as a substitution.

**Theorem routing:** [[Thm - Direct Sum of Two Subspaces]] reduces directness to $V_e \cap V_o = \{0\}$. The fact that every $f$ decomposes follows from the **explicit formula** $f(x) = \frac{f(x) + f(-x)}{2} + \frac{f(x) - f(-x)}{2}$, with the first summand even and the second odd. The verification that the formula works is direct evaluation; the trick is to *find* the formula, which is forced by the parity requirements.

**Key decision point:** The non-obvious step is **discovering the decomposition formula**. Suppose $f = f_e + f_o$ with $f_e$ even and $f_o$ odd. Evaluating at $-x$: $f(-x) = f_e(-x) + f_o(-x) = f_e(x) - f_o(x)$. Adding to $f(x) = f_e(x) + f_o(x)$ gives $f(x) + f(-x) = 2 f_e(x)$, so $f_e(x) = \frac{f(x) + f(-x)}{2}$. Subtracting gives $f(x) - f(-x) = 2 f_o(x)$, so $f_o(x) = \frac{f(x) - f(-x)}{2}$. The formula is *forced* by the parity conditions, which is why the decomposition is unique. (This forcing is the algebraic content of the direct sum.) Recognizing that the decomposition is determined by the symmetrization at $\pm x$ is the key insight.

---

# Legal Operations Used

1. **Verify two candidate subspaces using the subspace criterion.** From the topic page's legal operations: $V_e$ and $V_o$ are checked to contain $0$, be closed under addition, and be closed under scalar multiplication.

2. **Reduce direct sum to trivial intersection via [[Thm - Direct Sum of Two Subspaces]].** The theorem says $V_e + V_o$ is direct iff $V_e \cap V_o = \{0\}$. So we check the intersection condition rather than chasing the (harder) uniqueness condition directly.

3. **Symmetrize and antisymmetrize.** Given $f \in \mathbb{R}^\mathbb{R}$, the average $\frac{1}{2}(f(x) + f(-x))$ is even and the difference $\frac{1}{2}(f(x) - f(-x))$ is odd. This is a *general* trick for decomposing into symmetric and antisymmetric parts under any involution.

4. **Use pointwise definitions: $f \in V_e$ means $f(-x) = f(x)$ for every $x$.** The parity condition is a *universally quantified* equality, and the proof manipulates this equation by substituting specific values of $x$ or composing with $-x$.

---

# Hints

> [!note]- Hint 1
> Split into three parts: (a) verify $V_e$ and $V_o$ are subspaces; (b) compute $V_e \cap V_o$ to apply [[Thm - Direct Sum of Two Subspaces]]; (c) show every $f$ decomposes.

> [!note]- Hint 2
> For part (b): an even-and-odd function satisfies $f(-x) = f(x)$ and $f(-x) = -f(x)$, hence $f(x) = -f(x)$, hence $f(x) = 0$ for every $x$.

> [!note]- Hint 3
> For part (c), the decomposition formula is $f(x) = f_e(x) + f_o(x)$ with $f_e(x) = \frac{f(x) + f(-x)}{2}$ and $f_o(x) = \frac{f(x) - f(-x)}{2}$. Verify that $f_e$ is even and $f_o$ is odd, and that $f_e + f_o = f$.

> [!note]- Hint 4
> The formula in Hint 3 is not arbitrary: it is *forced* by the parity conditions. If $f = f_e + f_o$ with $f_e$ even and $f_o$ odd, then $f(-x) = f_e(x) - f_o(x)$, so $f_e = \frac{1}{2}(f + f^\vee)$ and $f_o = \frac{1}{2}(f - f^\vee)$ where $f^\vee(x) := f(-x)$.

---

# Solution

The proof has three parts. Step 1 verifies $V_e, V_o$ are subspaces. Step 2 shows $V_e \cap V_o = \{0\}$, reducing directness of the sum to a trivial check via [[Thm - Direct Sum of Two Subspaces]]. Step 3 exhibits an explicit decomposition $f = f_e + f_o$ for arbitrary $f$, completing $V_e + V_o = \mathbb{R}^\mathbb{R}$.

**Step 1: $V_e$ and $V_o$ are subspaces of $\mathbb{R}^\mathbb{R}$.**

> [!note]- Derivation
> *$V_e$ is a subspace.* The zero function satisfies $0(-x) = 0 = 0(x)$, so $0 \in V_e$. If $f, g \in V_e$, then $(f + g)(-x) = f(-x) + g(-x) = f(x) + g(x) = (f + g)(x)$, so $f + g \in V_e$. If $\lambda \in \mathbb{R}$ and $f \in V_e$, then $(\lambda f)(-x) = \lambda f(-x) = \lambda f(x) = (\lambda f)(x)$, so $\lambda f \in V_e$.
>
> *$V_o$ is a subspace.* The zero function satisfies $0(-x) = 0 = -0(x)$, so $0 \in V_o$. If $f, g \in V_o$, then $(f + g)(-x) = f(-x) + g(-x) = -f(x) - g(x) = -(f + g)(x)$, so $f + g \in V_o$. If $\lambda \in \mathbb{R}$ and $f \in V_o$, then $(\lambda f)(-x) = \lambda f(-x) = -\lambda f(x) = -(\lambda f)(x)$, so $\lambda f \in V_o$.

**Step 2: $V_e \cap V_o = \{0\}$.**

> [!note]- Derivation
> Suppose $f \in V_e \cap V_o$. Then $f(-x) = f(x)$ (since $f \in V_e$) and $f(-x) = -f(x)$ (since $f \in V_o$), so $f(x) = -f(x)$ for every $x$. Adding $f(x)$ to both sides: $2 f(x) = 0$, hence $f(x) = 0$ for every $x \in \mathbb{R}$. So $f = 0$, the zero function. Hence $V_e \cap V_o = \{0\}$.
>
> By [[Thm - Direct Sum of Two Subspaces]], $V_e + V_o$ is a direct sum.

**Step 3: $V_e + V_o = \mathbb{R}^\mathbb{R}$.**

We exhibit a decomposition for any $f \in \mathbb{R}^\mathbb{R}$.

> [!note]- Derivation
> Given $f \in \mathbb{R}^\mathbb{R}$, define
> $$f_e(x) = \frac{f(x) + f(-x)}{2}, \qquad f_o(x) = \frac{f(x) - f(-x)}{2}.$$
> Then $f_e + f_o = f$ pointwise: $\frac{f(x) + f(-x)}{2} + \frac{f(x) - f(-x)}{2} = \frac{2 f(x)}{2} = f(x)$.
>
> *$f_e \in V_e$.* $f_e(-x) = \frac{f(-x) + f(-(-x))}{2} = \frac{f(-x) + f(x)}{2} = f_e(x)$.
>
> *$f_o \in V_o$.* $f_o(-x) = \frac{f(-x) - f(-(-x))}{2} = \frac{f(-x) - f(x)}{2} = -\frac{f(x) - f(-x)}{2} = -f_o(x)$.
>
> So every $f \in \mathbb{R}^\mathbb{R}$ has the form $f = f_e + f_o$ with $f_e \in V_e$ and $f_o \in V_o$, proving $V_e + V_o = \mathbb{R}^\mathbb{R}$.

Combining Step 2 and Step 3: $\mathbb{R}^\mathbb{R} = V_e \oplus V_o$.

> [!note]- Complete formal solution
> **Claim.** $V_e$ and $V_o$ are subspaces of $\mathbb{R}^\mathbb{R}$, and $\mathbb{R}^\mathbb{R} = V_e \oplus V_o$.
>
> *Proof.* *Step 1 — [[Def - Subspace|Subspaces]].* For each parity, the zero function satisfies the parity condition, the sum of two parity-respecting functions has the same parity, and a scalar multiple preserves parity. So both $V_e$ and $V_o$ are subspaces.
>
> *Step 2 — Trivial intersection.* If $f \in V_e \cap V_o$, then for every $x$, $f(-x) = f(x)$ and $f(-x) = -f(x)$, so $f(x) = -f(x)$, i.e. $2 f(x) = 0$, hence $f(x) = 0$. So $f$ is identically zero. By [[Thm - Direct Sum of Two Subspaces]], $V_e + V_o$ is a direct sum.
>
> *Step 3 — Sum equals all.* For arbitrary $f \in \mathbb{R}^\mathbb{R}$, define
> $$f_e(x) := \tfrac{1}{2}(f(x) + f(-x)), \qquad f_o(x) := \tfrac{1}{2}(f(x) - f(-x)).$$
> Then $f_e + f_o = f$ identically, and direct computation verifies $f_e(-x) = f_e(x)$ (so $f_e \in V_e$) and $f_o(-x) = -f_o(x)$ (so $f_o \in V_o$). Hence every $f$ decomposes as a sum $f_e + f_o$, and $V_e + V_o = \mathbb{R}^\mathbb{R}$.
>
> Combining: $\mathbb{R}^\mathbb{R} = V_e \oplus V_o$. $\blacksquare$
>
> **Remark — uniqueness in concrete form.** The proof shows that the decomposition is unique: if $f = g + h$ with $g \in V_e, h \in V_o$, then evaluating at $\pm x$ gives the simultaneous equations $f(x) = g(x) + h(x)$ and $f(-x) = g(x) - h(x)$, with unique solution $g = f_e, h = f_o$. The directness of the sum is therefore visible in the *forcing* of the formulae.

---

# Key Takeaways

**Symmetrization and antisymmetrization decompose any space under an involution into invariants and anti-invariants.** The construction $f_e = \frac{1}{2}(f + f^\vee)$, $f_o = \frac{1}{2}(f - f^\vee)$ where $f^\vee(x) = f(-x)$ is a special case of a much more general construction. Whenever a vector space $V$ carries an **involution** — a linear map $\sigma : V \to V$ with $\sigma^2 = \operatorname{id}$ — it decomposes as $V = V^+ \oplus V^-$ where $V^+ = \ker(\sigma - I)$ (the $+1$-eigenspace) and $V^- = \ker(\sigma + I)$ (the $-1$-eigenspace), via $v = \frac{1}{2}(v + \sigma v) + \frac{1}{2}(v - \sigma v)$. The same trick decomposes matrices into symmetric and antisymmetric parts ($M = \frac{1}{2}(M + M^T) + \frac{1}{2}(M - M^T)$), tensors into symmetric and antisymmetric parts (the basis of differential forms in [[Linear Algebra IX — §9 Multilinear Algebra and Determinants]]), and operators on Hilbert space into Hermitian and skew-Hermitian parts. The pattern is one of the most reusable in linear algebra: identify an involution, use it to split.

**The proof works in characteristic not equal to 2.** The construction relies on dividing by $2$, which is invalid in fields of characteristic $2$ (such as $\mathbb{F}_2$). In characteristic $2$, even and odd functions coincide (since $-1 = 1$), and the decomposition degenerates. This is a recurring caution: many "averaging" constructions in linear algebra fail in characteristic $2$ or in fields where some integer is non-invertible. Examples include the polarization identity (recovers an inner product from a norm; divides by $2$ and $4$), the eigenspace decomposition of an involution (divides by $2$), and Maschke's theorem on [[Def - Group|group]] representations (divides by the [[Def - Group|group]] order). Being alert to characteristic-dependent steps is a transferable diagnostic.

**The trick "evaluate $f$ at $\pm x$" is a substitution that produces invariants automatically.** The substitution $x \to -x$ is an involution on the domain $\mathbb{R}$, and any function $f : \mathbb{R} \to \mathbb{R}$ can be replaced by $f^\vee(x) := f(-x)$. The pair $(f, f^\vee)$ then admits a linear decomposition into symmetric and antisymmetric combinations, which is the abstract source of the formulae here. The same trick — replace a function by its image under a domain symmetry, average to symmetrize — works for: decomposing periodic functions by Fourier components (the domain symmetry is translation), decomposing distributions by their parity under rotation (the symmetry is $O(n)$-action), and decomposing wave functions by parity in quantum mechanics. The skill is recognizing when a domain symmetry exists; once recognized, the decomposition is mechanical.

**The direct sum is the structural skeleton of "any function $=$ even part $+$ odd part".** The slogan "every function on $\mathbb{R}$ is a sum of an even and an odd part" is the *informal* version of the result here; the *formal* version is the direct sum decomposition $\mathbb{R}^\mathbb{R} = V_e \oplus V_o$. The slogan implies existence (every $f$ decomposes) but is silent on uniqueness; the direct sum carries both. The same upgrade — from "decomposes" to "decomposes uniquely" — recurs in every spectral theorem: "every Hermitian operator's eigenvectors span" implies "the eigenspace decomposition is direct", and one cares about the directness because it gives well-defined projections. Reading direct-sum statements as upgraded versions of existence statements clarifies what they buy.
