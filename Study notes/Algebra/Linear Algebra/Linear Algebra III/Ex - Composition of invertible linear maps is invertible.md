---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Invertibility and Isomorphism"
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $S \in \mathcal{L}(U, V)$ and $T \in \mathcal{L}(V, W)$ both be invertible linear maps. Prove that $TS \in \mathcal{L}(U, W)$ is invertible, and
$$(TS)^{-1} \;=\; S^{-1}\, T^{-1}.$$

(This is the "socks-and-shoes" reversal for linear maps, and Exercise 2 of LADR §3D.)

**Recall:**

![[Def - Invertibility and Isomorphism#The Definition]]

Composition: $(TS)(u) = T(S(u))$ for $u \in U$. The inverse of $TS$, when it exists, is the unique $R \in \mathcal{L}(W, U)$ with $R(TS) = I_U$ and $(TS) R = I_W$.

---

# Convergent Strategy

**Problem class.** This is a *prove a constructed map is the inverse* problem. The topic-page Problem-Solving Strategy categorises it under "verify invertibility by exhibiting an explicit inverse": guess the candidate inverse and verify the two defining equations.

**Assumption pattern.** $S, T$ both invertible. The natural guess for $(TS)^{-1}$ is $S^{-1} T^{-1}$ — the inverses in reverse order. Verifying this guess is the entire content.

**Theorem routing.** Direct verification: compute $(TS)(S^{-1} T^{-1})$ and $(S^{-1} T^{-1})(TS)$, and show both equal the identity. The "reverse order" is forced by the fact that the inverse must undo the composition in the *opposite order* — applying $TS$ does "$S$ then $T$", so its inverse does "$T^{-1}$ then $S^{-1}$", i.e., $S^{-1} T^{-1}$.

**Key decision point.** The crucial recognition is the "socks-and-shoes" reversal: putting on socks then shoes is undone by removing shoes then socks. The reversal of order is mandatory; one cannot avoid it. The "key decision" is to verify both compositions, since invertibility requires *both* $R(TS) = I$ and $(TS) R = I$. (Each implies the other in finite [[Def - Dimension|dimensions]] by [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]], but in general we verify both.)

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Build new linear maps by sum, composition, restriction, and extension** (operation 10). The candidate $S^{-1} T^{-1}$ is a composition of two invertible maps; verifying it is an inverse is the content.

2. **Pass between a linear map and its matrix** (operation 6). In matrix terms, $(AB)^{-1} = B^{-1} A^{-1}$ — the same statement.

---

# Hints

> [!note]- Hint 1
> What is the natural candidate for $(TS)^{-1}$? Try $S^{-1} T^{-1}$ (the inverses in reversed order).

> [!note]- Hint 2
> Verify: $(TS)(S^{-1} T^{-1}) \stackrel{?}{=} I_W$. Use associativity of composition.

> [!note]- Hint 3
> $(TS)(S^{-1} T^{-1}) = T (S S^{-1}) T^{-1} = T I_V T^{-1} = T T^{-1} = I_W$. The cancellation goes through cleanly because the parenthesisation is what allows $SS^{-1}$ to appear in the middle.

---

# Solution

The plan: guess $(TS)^{-1} = S^{-1} T^{-1}$ and verify by computing both compositions. The reversed order is forced by the composition structure.

**Step 1: Compute $(TS)(S^{-1} T^{-1})$.**

By associativity, $(TS)(S^{-1} T^{-1}) = T(S S^{-1}) T^{-1} = T I_V T^{-1} = T T^{-1} = I_W$.

> [!note]- Derivation
> By associativity of function composition:
> $$(TS)(S^{-1} T^{-1}) = T \circ S \circ S^{-1} \circ T^{-1} = T \circ (S \circ S^{-1}) \circ T^{-1} = T \circ I_V \circ T^{-1}.$$
> Using that $I_V$ is the identity, $T \circ I_V = T$, so this equals $T \circ T^{-1} = I_W$. Hence $(TS)(S^{-1} T^{-1}) = I_W$.

**Step 2: Compute $(S^{-1} T^{-1})(TS)$.**

Similarly: $(S^{-1} T^{-1})(TS) = S^{-1}(T^{-1} T) S = S^{-1} I_V S = S^{-1} S = I_U$.

> [!note]- Derivation
> By associativity:
> $$(S^{-1} T^{-1})(TS) = S^{-1} \circ (T^{-1} \circ T) \circ S = S^{-1} \circ I_V \circ S = S^{-1} \circ S = I_U.$$
> Hence $(S^{-1} T^{-1})(TS) = I_U$.

**Step 3: Conclude.**

By [[Def - Invertibility and Isomorphism|definition of invertible]], the existence of a linear map $R$ (here $R = S^{-1} T^{-1}$) satisfying $R(TS) = I_U$ and $(TS) R = I_W$ means $TS$ is invertible with inverse $R$. By Steps 1 and 2, $R = S^{-1} T^{-1}$ does this. So $(TS)^{-1} = S^{-1} T^{-1}$.

> [!note]- Derivation
> The two equations from Steps 1 and 2 satisfy the defining conditions for the inverse of $TS$. Since the inverse is unique (Proposition 3.60 of LADR), $(TS)^{-1}$ is exactly $S^{-1} T^{-1}$.

> [!note]- Complete formal solution
> Let $S \in \mathcal{L}(U, V)$ and $T \in \mathcal{L}(V, W)$ be invertible. We claim $TS \in \mathcal{L}(U, W)$ is invertible with $(TS)^{-1} = S^{-1} T^{-1}$.
>
> The composition $S^{-1} T^{-1} : W \to U$ is well-defined (and linear): $T^{-1} : W \to V$, then $S^{-1} : V \to U$.
>
> By associativity of composition:
> $$(TS)(S^{-1} T^{-1}) = T(SS^{-1}) T^{-1} = T I_V T^{-1} = T T^{-1} = I_W.$$
> $$(S^{-1} T^{-1})(TS) = S^{-1}(T^{-1} T) S = S^{-1} I_V S = S^{-1} S = I_U.$$
>
> Hence $S^{-1} T^{-1}$ satisfies the defining equations of the inverse of $TS$. By uniqueness of the inverse, $(TS)^{-1} = S^{-1} T^{-1}$. $\blacksquare$

> [!warning] Illegal but tempting alternative route: $(TS)^{-1} = T^{-1} S^{-1}$
> A common error is to write $(TS)^{-1} = T^{-1} S^{-1}$, in the same order. This fails: $(TS)(T^{-1} S^{-1}) = T (S T^{-1}) S^{-1}$, which generally does not simplify to the identity because the middle product $S T^{-1}$ is not in general $I$ — there is no reason for $S$ and $T^{-1}$ to compose to the identity. The reversal in order is genuine and mandatory.
>
> A concrete check: $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $T = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$. Then $TS = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, $S^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$, $T^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$. Compute $S^{-1} T^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$, and $T^{-1} S^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$. Verify $(TS)(S^{-1} T^{-1}) = I_2$: $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, yes. But $(TS)(T^{-1} S^{-1}) = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 3 \end{pmatrix}$, not the identity.

---

# Key Takeaways

**The "socks-and-shoes" reversal: inverting a composition reverses the order.** Whenever an operation is a composition, its inverse is the composition of inverses *in reverse order*: $(TS)^{-1} = S^{-1} T^{-1}$, $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$, $(AB)^{-1} = B^{-1} A^{-1}$ for invertible matrices. The reversal is forced by associativity and the cancellation pattern $T T^{-1} = I$. The reusable principle: **non-commutative operations** (function composition, matrix multiplication, [[Def - Group|group]] multiplication) all share this reversal. The trigger is "invert a product or composition" — the order reverses, no exceptions.

**Inverting a composition extends to longer products.** By induction, $(T_n T_{n-1} \cdots T_1)^{-1} = T_1^{-1} T_2^{-1} \cdots T_n^{-1}$. So inverting a chain of operations reverses the whole chain. This is the same principle as the algorithmic "undo": to undo a sequence of operations, undo them in reverse order. Concrete applications: inverting a sequence of linear transformations (apply the inverses in reverse), undoing a sequence of row operations in Gauss elimination, computing the inverse of a product of permutations.

**Invertibility is preserved under composition.** The set of invertible linear maps $\operatorname{GL}(V) \subseteq \mathcal{L}(V)$ is closed under composition. Combined with the fact that $\operatorname{GL}(V)$ has an identity ($I_V$) and inverses (by definition), $\operatorname{GL}(V)$ is a **[[Def - Group|group]]** — the **general linear group** of $V$. This is the structural content of the exercise: composition of invertible maps stays invertible, with the predicted inverse. The reusable principle: $\operatorname{GL}(V)$ is a group, and group-theoretic facts (Lagrange, homomorphism theorems, conjugacy classes) apply. See [[Linear Algebra III — §3A–D Linear Maps#Bridges]] for the bridge to group theory.

---
