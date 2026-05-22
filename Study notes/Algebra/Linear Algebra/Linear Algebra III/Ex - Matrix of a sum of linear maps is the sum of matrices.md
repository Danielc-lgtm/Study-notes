---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Matrix of a Linear Map"
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V, W$ be finite-dimensional vector spaces with chosen bases. For $S, T \in \mathcal{L}(V, W)$ and $\lambda \in \mathbf{F}$, prove:
$$\mathcal{M}(S + T) = \mathcal{M}(S) + \mathcal{M}(T), \qquad \mathcal{M}(\lambda T) = \lambda \mathcal{M}(T).$$
In words: the matrix-of-a-linear-map assignment is itself a *linear map* from $\mathcal{L}(V, W)$ to $\mathbf{F}^{m, n}$. (This is LADR Exercise 3 of §3C and Propositions 3.35, 3.38.)

**Recall:**

![[Def - Matrix of a Linear Map#The Definition]]

The vector space $\mathcal{L}(V, W)$ has pointwise operations: $(S + T)(v) := Sv + Tv$ and $(\lambda T)(v) := \lambda Tv$.

The vector space $\mathbf{F}^{m, n}$ has entry-wise operations on matrices: $(A + B)_{j, k} := A_{j, k} + B_{j, k}$ and $(\lambda A)_{j, k} := \lambda A_{j, k}$.

---

# Convergent Strategy

**Problem class.** This is a *prove a map preserves structure* problem — specifically, *the matrix-of-a-linear-map assignment is linear*. The topic-page Problem-Solving Strategy categorises it under "structural facts about $\mathcal{L}(V, W)$": exploit pointwise operations on both sides and verify the entries agree.

**Assumption pattern.** Bases of $V$ and $W$ are fixed (so matrices are defined). The defining feature: both the operations on $\mathcal{L}(V, W)$ and on $\mathbf{F}^{m, n}$ are pointwise/entry-wise, so the linearity of $\mathcal{M}$ reduces to checking entries.

**Theorem routing.** The route is to compute the $(j, k)$-entry of each side of the claimed identity. The $(j, k)$-entry of $\mathcal{M}(S + T)$ is the $w_j$-coefficient of $(S + T)(v_k) = S v_k + T v_k$, which by linearity of basis expansion is the sum of the $w_j$-coefficients of $S v_k$ and $T v_k$, i.e., $\mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k}$. This is the $(j, k)$-entry of $\mathcal{M}(S) + \mathcal{M}(T)$.

**Key decision point.** The crucial recognition is that "linearity of $\mathcal{M}$" reduces to "linearity of basis expansion": the operation of extracting the coefficient of $w_j$ from an expansion is itself linear. Once you see this, the proof is one line per axiom. The "key decision" is to compute entries directly rather than try to argue abstractly about isomorphisms.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Pass between a linear map and its matrix** (operation 6). The whole identity is about the matrix-of-a-linear-map map, which is the bridge between $\mathcal{L}(V, W)$ and $\mathbf{F}^{m, n}$.

2. **Build new linear maps by sum, composition, restriction, and extension** (operation 10). The pointwise sum and scalar multiple of linear maps are themselves linear (verified using [[Ex - Linear maps preserve linear combinations]] to handle linear combinations).

---

# Hints

> [!note]- Hint 1
> Compute entries directly. What is the $(j, k)$-entry of $\mathcal{M}(S + T)$? It is the $w_j$-coefficient of $(S + T)(v_k)$.

> [!note]- Hint 2
> $(S + T)(v_k) = S v_k + T v_k$ by definition. The $w_j$-coefficient of a sum of two vectors in $W$ is the sum of their $w_j$-coefficients (since basis expansion is linear). So the $(j, k)$-entry of $\mathcal{M}(S + T)$ is $\mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k}$, which is the $(j, k)$-entry of $\mathcal{M}(S) + \mathcal{M}(T)$.

> [!note]- Hint 3
> The scalar-multiplication case is symmetric: $(\lambda T)(v_k) = \lambda T v_k$, and the $w_j$-coefficient of $\lambda$ times a vector is $\lambda$ times the $w_j$-coefficient.

---

# Solution

The plan: compute the $(j, k)$-entry of each side of the claimed identity. Both sides reduce to the same expression involving basis-expansion coefficients of $Sv_k$ and $Tv_k$.

**Step 1: Additivity of $\mathcal{M}$.**

For $S, T \in \mathcal{L}(V, W)$, compute $\mathcal{M}(S + T)_{j, k}$ and verify it equals $\mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k}$.

> [!note]- Derivation
> Fix bases $v_1, \ldots, v_n$ of $V$ and $w_1, \ldots, w_m$ of $W$. By definition of $\mathcal{M}$, the $(j, k)$-entry of $\mathcal{M}(S + T)$ is the $w_j$-coefficient in the expansion of $(S + T)(v_k)$ in the $w$-basis:
> $$(S + T)(v_k) = \sum_{j=1}^m \mathcal{M}(S + T)_{j, k}\, w_j.$$
>
> By the pointwise definition of $S + T$, $(S + T)(v_k) = S v_k + T v_k$. Expand each summand in the $w$-basis:
> $$S v_k = \sum_j \mathcal{M}(S)_{j, k}\, w_j, \qquad T v_k = \sum_j \mathcal{M}(T)_{j, k}\, w_j.$$
> Adding:
> $$(S + T)(v_k) = \sum_j (\mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k})\, w_j.$$
> By the uniqueness of basis expansion, the $w_j$-coefficient on the right is the same as on the left. So
> $$\mathcal{M}(S + T)_{j, k} = \mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k} = (\mathcal{M}(S) + \mathcal{M}(T))_{j, k},$$
> where the last equality is the entry-wise definition of matrix addition. This holds for all $(j, k)$, so $\mathcal{M}(S + T) = \mathcal{M}(S) + \mathcal{M}(T)$.

**Step 2: Homogeneity of $\mathcal{M}$.**

For $\lambda \in \mathbf{F}$ and $T \in \mathcal{L}(V, W)$, $\mathcal{M}(\lambda T) = \lambda \mathcal{M}(T)$.

> [!note]- Derivation
> The $(j, k)$-entry of $\mathcal{M}(\lambda T)$ is the $w_j$-coefficient of $(\lambda T)(v_k)$.
>
> By the pointwise definition of scalar multiplication on $\mathcal{L}(V, W)$, $(\lambda T)(v_k) = \lambda T v_k$. Expand $Tv_k = \sum_j \mathcal{M}(T)_{j, k} w_j$ and multiply by $\lambda$:
> $$(\lambda T)(v_k) = \lambda \sum_j \mathcal{M}(T)_{j, k} w_j = \sum_j (\lambda \mathcal{M}(T)_{j, k}) w_j.$$
>
> By uniqueness of basis expansion,
> $$\mathcal{M}(\lambda T)_{j, k} = \lambda \mathcal{M}(T)_{j, k} = (\lambda \mathcal{M}(T))_{j, k},$$
> the last equality by the entry-wise definition of scalar multiplication on matrices. Hence $\mathcal{M}(\lambda T) = \lambda \mathcal{M}(T)$.

**Step 3: Conclude $\mathcal{M}$ is linear.**

Steps 1 and 2 together verify both axioms of [[Def - Linear Map|linearity]] for $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$.

> [!note]- Derivation
> A function $\mathcal{M}$ is linear iff $\mathcal{M}(S + T) = \mathcal{M}(S) + \mathcal{M}(T)$ (additivity) and $\mathcal{M}(\lambda T) = \lambda \mathcal{M}(T)$ (homogeneity). Both hold (Steps 1 and 2). So $\mathcal{M}$ is linear.

> [!note]- Complete formal solution
> Fix bases $v_1, \ldots, v_n$ of $V$ and $w_1, \ldots, w_m$ of $W$. Let $S, T \in \mathcal{L}(V, W)$ and $\lambda \in \mathbf{F}$.
>
> **Additivity.** For each $k$,
> $$(S + T)(v_k) = S v_k + T v_k = \sum_j \mathcal{M}(S)_{j, k} w_j + \sum_j \mathcal{M}(T)_{j, k} w_j = \sum_j (\mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k}) w_j.$$
> The $w_j$-coefficient is unique, so $\mathcal{M}(S + T)_{j, k} = \mathcal{M}(S)_{j, k} + \mathcal{M}(T)_{j, k}$ for all $(j, k)$, i.e., $\mathcal{M}(S + T) = \mathcal{M}(S) + \mathcal{M}(T)$.
>
> **Homogeneity.** For each $k$,
> $$(\lambda T)(v_k) = \lambda T v_k = \lambda \sum_j \mathcal{M}(T)_{j, k} w_j = \sum_j \lambda \mathcal{M}(T)_{j, k} w_j.$$
> The $w_j$-coefficient is unique, so $\mathcal{M}(\lambda T)_{j, k} = \lambda \mathcal{M}(T)_{j, k}$, i.e., $\mathcal{M}(\lambda T) = \lambda \mathcal{M}(T)$.
>
> Therefore $\mathcal{M}$ is a linear map from $\mathcal{L}(V, W)$ to $\mathbf{F}^{m, n}$. $\blacksquare$

---

# Key Takeaways

**Linearity of $\mathcal{M}$ is "linearity of basis expansion".** The proof reduces to the observation that extracting the coefficient of $w_j$ from a basis expansion is itself a linear operation: the coefficient of a sum is the sum of coefficients; the coefficient of a scalar times a vector is the scalar times the coefficient. This is the *true name* of the linearity of $\mathcal{M}$, and it explains why the proof is mechanical. The reusable principle: linearity is "preserved under basis expansion", because basis expansion is itself a linear operation (uniquely extracting coordinates is a linear functional on each coordinate). The trigger is "matrix or coordinate identity to verify" — verify it entry-by-entry, using that each entry-extraction is a linear functional.

**The matrix-of-a-linear-map is a linear *isomorphism*, not just a function.** This exercise verifies that $\mathcal{M}$ is linear. Combined with [[Ex - The space of linear maps has dimension mn|the exercise on dimension $mn$]], $\mathcal{M}$ is a linear isomorphism between $\mathcal{L}(V, W)$ and $\mathbf{F}^{m, n}$. So the matrix is not just one description of the linear map; it is an honest *isomorphism of vector spaces* between abstract linear maps and concrete matrices. Every operation on linear maps (sum, scalar multiplication, composition — see [[Thm - Composition Corresponds to Matrix Multiplication]]) corresponds to an operation on matrices, and the correspondence is structure-preserving. The reusable principle: when two spaces are isomorphic in a *natural* way, operations transfer. The trigger: "I want to compute with linear maps using matrices" — the iso is canonical (once bases are fixed) and respects all structure.

**Pointwise operations on functions are linear when the codomain is a vector space.** This is the structural reason $\mathcal{L}(V, W)$ is a vector space. Whenever the codomain $W$ has vector-space structure, the set of all functions $V \to W$ inherits it pointwise: $(S + T)(v) := Sv + Tv$, $(\lambda T)(v) := \lambda Tv$. This is the principle behind $C^\infty$ functions forming a vector space, $L^p$ spaces being vector spaces, sequence spaces $\mathbf{F}^\mathbb{N}$ being vector spaces, etc. The reusable principle: *function spaces inherit the codomain's structure pointwise*. The trigger is any "the space of functions with property P forms a vector space" question — verify pointwise.

---
