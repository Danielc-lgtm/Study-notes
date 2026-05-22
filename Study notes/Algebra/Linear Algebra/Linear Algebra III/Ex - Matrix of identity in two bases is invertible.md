---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Change of Basis Matrix"
  - "Def - Matrix of a Linear Map"
  - "Thm - Composition Corresponds to Matrix Multiplication"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $u_1, \ldots, u_n$ and $v_1, \ldots, v_n$ be two bases of a finite-dimensional vector space $V$. Prove that the matrices
$$\mathcal{M}(I, (u), (v)) \quad \text{and} \quad \mathcal{M}(I, (v), (u))$$
are invertible, and that each is the inverse of the other:
$$\mathcal{M}(I, (u), (v))^{-1} = \mathcal{M}(I, (v), (u)).$$

(This is Theorem 3.82 of LADR.)

**Recall:**

![[Def - Change of Basis Matrix#The Definition]]

The matrix of a composition: by [[Thm - Composition Corresponds to Matrix Multiplication]], $\mathcal{M}(ST) = \mathcal{M}(S) \mathcal{M}(T)$ when the inner basis used is the same.

The matrix of the identity operator in a single basis is the identity matrix: $\mathcal{M}(I, (u)) = I_n$.

---

# Convergent Strategy

**Problem class.** This is a *prove an inverse relationship* problem. The topic-page Problem-Solving Strategy categorises it under "use $\mathcal{M}(ST) = \mathcal{M}(S) \mathcal{M}(T)$ for explicit matrix computations": the two change-of-basis matrices multiply to give the identity matrix, in both orders.

**Assumption pattern.** Two bases $u$ and $v$ of the same space $V$. The defining feature: the operator under consideration is the identity, which is invertible (its inverse is itself).

**Theorem routing.** Apply [[Thm - Composition Corresponds to Matrix Multiplication]] to the identity composition $I \circ I = I$ in the basis pairs $(u, v) \to (v, u)$ and $(v, u) \to (u, v)$. The product of the two change-of-basis matrices in each order is the matrix of $I \circ I = I$ in a single basis, which is $I_n$.

**Key decision point.** The crucial recognition is that the *identity operator* expressed in two ways — once with domain $u$ codomain $v$, and once with domain $v$ codomain $u$ — composes to the identity in a single basis. The composition theorem then gives the matrix identity automatically. The "key decision" is to invoke the composition theorem rather than try to verify by direct entry computation, which would be much harder.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Use $\mathcal{M}(ST) = \mathcal{M}(S) \mathcal{M}(T)$** (operation 7). The whole proof is one application of the composition theorem.

2. **Pass between a linear map and its matrix** (operation 6). The identity operator has a clean matrix description that drives the calculation.

3. **Change basis to simplify** (operation 8). This exercise is the foundational fact underlying [[Thm - Change of Basis Formula|the change of basis formula]].

---

# Hints

> [!note]- Hint 1
> Apply $\mathcal{M}(ST) = \mathcal{M}(S) \mathcal{M}(T)$ to $I \circ I = I$, choosing the basis assignments carefully.

> [!note]- Hint 2
> With $S = I : V_{(v)} \to V_{(u)}$ (codomain basis $u$) and $T = I : V_{(u)} \to V_{(v)}$ (codomain basis $v$), the composition $S \circ T = I : V_{(u)} \to V_{(u)}$. Its matrix is $\mathcal{M}(I, (u)) = I_n$.

> [!note]- Hint 3
> The composition theorem gives $I_n = \mathcal{M}(S \circ T, (u), (u)) = \mathcal{M}(S, (v), (u)) \cdot \mathcal{M}(T, (u), (v)) = \mathcal{M}(I, (v), (u)) \cdot \mathcal{M}(I, (u), (v))$. So the two matrices are inverses.

---

# Solution

The plan: apply [[Thm - Composition Corresponds to Matrix Multiplication]] to the composition $I \circ I = I$, with carefully chosen bases on each side. The result is $I_n$, which forces the two change-of-basis matrices to be mutual inverses.

**Step 1: Express $I \circ I = I$ as a composition between basis pairs.**

The identity operator on $V$, viewed as the composition $I : V \xrightarrow{I} V \xrightarrow{I} V$, where we equip the first $V$ with the $u$-basis, the middle $V$ with the $v$-basis, and the last $V$ with the $u$-basis again.

> [!note]- Derivation
> The identity operator $I : V \to V$ sends every $v \in V$ to $v$. We can view this as a composition of two identity operators, each viewed as a linear map between different basis equipments:
> $$V_{(u)} \xrightarrow{I_1} V_{(v)} \xrightarrow{I_2} V_{(u)},$$
> where $I_1$ and $I_2$ are both the identity map of $V$ as functions, but viewed as linear maps between basis-equipped versions of $V$. The composition $I_2 \circ I_1 = I$ on $V$, with overall basis-equipment $u$ on both ends.

**Step 2: Compute matrices.**

- $\mathcal{M}(I_1, (u), (v)) = \mathcal{M}(I, (u), (v))$ by definition. Call this $C$.
- $\mathcal{M}(I_2, (v), (u)) = \mathcal{M}(I, (v), (u))$. Call this $D$.
- $\mathcal{M}(I_2 \circ I_1, (u), (u)) = \mathcal{M}(I, (u))$.

> [!note]- Derivation
> Each matrix is computed in the appropriate basis pair, with $I_1$ and $I_2$ being the same function $I$ but with different basis labels. The composition $I_2 \circ I_1 = I$ has matrix $\mathcal{M}(I, (u), (u)) = \mathcal{M}(I, (u)) = I_n$ (the identity matrix), because in any single basis, the identity operator has the identity matrix.

**Step 3: Apply the composition theorem.**

$\mathcal{M}(I_2 \circ I_1, (u), (u)) = \mathcal{M}(I_2, (v), (u)) \cdot \mathcal{M}(I_1, (u), (v))$, by [[Thm - Composition Corresponds to Matrix Multiplication]].

> [!note]- Derivation
> By the composition theorem:
> $$\mathcal{M}(I_2 \circ I_1, (u), (u)) = \mathcal{M}(I_2, (v), (u)) \cdot \mathcal{M}(I_1, (u), (v)) = D \cdot C.$$
>
> Combining with Step 2:
> $$I_n = D \cdot C, \quad \text{i.e.,} \quad \mathcal{M}(I, (v), (u)) \cdot \mathcal{M}(I, (u), (v)) = I_n.$$

**Step 4: Reverse the roles.**

Repeat with the roles of $u$ and $v$ swapped: $I = I_1' \circ I_2'$ where $I_1' : V_{(v)} \to V_{(u)}$ and $I_2' : V_{(u)} \to V_{(v)}$. The composition theorem gives $C \cdot D = I_n$.

> [!note]- Derivation
> Repeating the argument with $u, v$ swapped, the composition $I : V_{(v)} \to V_{(u)} \to V_{(v)}$ has overall matrix $\mathcal{M}(I, (v)) = I_n$, and by the composition theorem:
> $$\mathcal{M}(I, (u), (v)) \cdot \mathcal{M}(I, (v), (u)) = I_n, \quad \text{i.e.,} \quad C \cdot D = I_n.$$

**Step 5: Conclude.**

$CD = DC = I_n$, so $C$ and $D$ are inverses of each other.

> [!note]- Derivation
> A matrix $C$ is invertible iff there is a matrix $D$ with $CD = DC = I_n$, and $D = C^{-1}$. We have verified $CD = DC = I_n$, so $C = \mathcal{M}(I, (u), (v))$ is invertible with inverse $D = \mathcal{M}(I, (v), (u))$.

> [!note]- Complete formal solution
> Let $u, v$ be two bases of $V$, $C := \mathcal{M}(I, (u), (v))$, and $D := \mathcal{M}(I, (v), (u))$.
>
> By [[Thm - Composition Corresponds to Matrix Multiplication]] applied to the identity $I \circ I = I$ on $V$:
> - Choosing domain basis $u$, intermediate basis $v$, codomain basis $u$: $\mathcal{M}(I, (u)) = \mathcal{M}(I, (v), (u)) \cdot \mathcal{M}(I, (u), (v))$, i.e., $I_n = DC$.
> - Choosing domain basis $v$, intermediate basis $u$, codomain basis $v$: $I_n = CD$.
>
> So $CD = DC = I_n$, hence $C$ is invertible with inverse $D$. Equivalently, $\mathcal{M}(I, (u), (v))^{-1} = \mathcal{M}(I, (v), (u))$. $\blacksquare$

---

# Key Takeaways

**Change-of-basis matrices in opposite directions are mutual inverses.** This is the foundational fact about change of basis: converting from $u$ to $v$ and then back from $v$ to $u$ does nothing. Algebraically, the matrices that implement these two conversions multiply to the identity. The reusable principle: *invertibility is automatic for any matrix representing an invertible operator between basis-equipped vector spaces of equal dimension*. The trigger is "matrix of an invertible operator" — its inverse is the matrix of the inverse operator. This is the basis-aware version of "the matrix of $T^{-1}$ is the inverse of the matrix of $T$" — but here the operator is the identity, and the two matrices represent it in two different basis-pair conventions.

**The composition theorem is the engine of every basis-change calculation.** This exercise illustrates that the change-of-basis formula and related identities all run through $\mathcal{M}(ST) = \mathcal{M}(S)\mathcal{M}(T)$. The reusable principle: whenever a matrix identity needs proving and the underlying operators are well-understood, factor the matrix calculation through the operators and use composition. The trigger is "matrix identity in question" — find the operator interpretation, use composition, translate back. The full [[Thm - Change of Basis Formula|change of basis formula]] $A = C^{-1} B C$ is three applications of this same theorem, with the middle being the operator and the outer factors being change-of-basis matrices.

**The identity operator has the identity matrix in any *single* basis.** The matrix of $I$ depends on the basis pair used. In a single basis (i.e., $\mathcal{M}(I, (u), (u))$), it is the identity matrix $I_n$. In two different bases, it is the change-of-basis matrix, generally not the identity. The reusable principle: clarity about which basis is used in domain vs. codomain. The trigger is any matrix involving the identity operator — check the bases carefully. Confusing $\mathcal{M}(I, (u))$ with $\mathcal{M}(I, (u), (v))$ is one of the most common bookkeeping errors in change-of-basis calculations.

---
