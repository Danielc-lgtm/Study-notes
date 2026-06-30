---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Generators and Structure Constants"
tags: [physics, special-relativity, lie-groups]
---

# Problem Statement

1. Compute the commutator $[J_3, K_1]$ from the explicit matrices and show it equals $K_2$, confirming the structure relation $[J_i, K_j] = \epsilon_{ijk}K_k$.
2. Interpret this relation: explain why it says "the boost generators $K_i$ transform as a $3$-vector under rotations".
3. Show that $[J_3, K_3] = 0$, and explain geometrically why a rotation about $z$ commutes with a boost along $z$.
4. Use the relations to show that the rotation generators $J_i$ *do* form a closed subalgebra (a copy of $\mathfrak{so}(3)$) while the boost generators $K_i$ do *not*, and state which physical fact each of these reflects.

**Recall:**

![[Def - Generators and Structure Constants#The Definition]]

The matrix commutator is $[A,B] = AB - BA$. Under a rotation $R$, a $3$-vector $\mathbf{V}$ transforms as $V_i \mapsto R_{ij}V_j$; infinitesimally, $[J_i, V_j] = \epsilon_{ijk}V_k$ characterises an object $\{V_j\}$ that rotates as a vector. A set of generators is a **subalgebra** if its span is closed under the bracket.

---

# Convergent Strategy

**Problem class.** A *Lie algebra computation* with structural interpretation: evaluate a mixed commutator and read its meaning (vector transformation, subalgebra structure). The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] emphasises reading the sign pattern $(+,+,-)$ on $([J,J],[J,K],[K,K])$ as the entire structure.

**Assumption pattern.** The generators are explicit sparse matrices (part 1) and the structure relations are available (parts 2–4). The signpost for part 2 is that the relation $[J_i, K_j] = \epsilon_{ijk}K_k$ has *exactly* the form $[J_i, V_j] = \epsilon_{ijk}V_k$ that defines a vector operator, so $\mathbf{K}$ is a vector under rotations.

**Theorem routing.** Part 1: multiply $J_3 K_1$ and $K_1 J_3$, subtract, identify $K_2$. Part 2: match $[J_i, K_j] = \epsilon_{ijk}K_k$ to the vector-operator condition. Part 3: compute $[J_3, K_3]$ and get $0$ (since $\epsilon_{33k} = 0$). Part 4: from $[J_i, J_j] = \epsilon_{ijk}J_k$ the $J$'s close (right-hand side is always a $J$); from $[K_i, K_j] = -\epsilon_{ijk}J_k$ the $K$'s do not (right-hand side is a $J$, outside the span of the $K$'s) — using [[Def - Generators and Structure Constants]].

**Key decision point.** The crux of part 4 is recognising that *closure under the bracket* is decided by which generators appear on the right-hand side of the structure relations: $[J,J]$ gives back $J$'s (closed), $[K,K]$ gives $J$'s (not in the span of $K$'s, so not closed). The temptation is to think the boosts "should" form a subgroup by analogy with rotations; the relation $[K,K] = -J$ is the precise obstruction, and it has the physical content that boosting in two directions induces a rotation.

---

# Legal Operations Used

1. **Compute a commutator from the structure relations (operation 3 from the topic page).** Part 1 establishes $[J_3, K_1] = K_2$ by matrix multiplication; parts 3–4 then use the relations to evaluate brackets and test closure.

2. **Check the generator condition (operation 2 from the topic page).** The result $K_2$ must be a boost generator, confirming the bracket stays in the algebra (closure of the *whole* algebra, even though the boost subspace is not closed).

---

# Hints

> [!note]- Hint 1
> $J_3$ has $-1$ at $(1,2)$ and $+1$ at $(2,1)$; $K_1$ has $1$ at $(0,1)$ and $(1,0)$. Multiply $J_3 K_1$ and $K_1 J_3$ using the sparsity, then subtract.

> [!note]- Hint 2
> The result $[J_3, K_1] = K_2$ has exactly the index structure $[J_3, K_1] = \epsilon_{31k}K_k = K_2$ (since $\epsilon_{312} = +1$). Compare with the defining property of a vector operator, $[J_i, V_j] = \epsilon_{ijk}V_k$.

> [!note]- Hint 3
> $[J_3, K_3] = \epsilon_{33k}K_k = 0$ because $\epsilon_{33k} = 0$ (repeated index). Geometrically: a rotation about the $z$-axis leaves the $z$-axis fixed, so it does not affect a boost *along* $z$.

> [!note]- Hint 4
> A set of generators forms a subalgebra iff every bracket of two of them is again in their span. For the $J$'s: $[J_i, J_j] = \epsilon_{ijk}J_k$, always a $J$ — closed. For the $K$'s: $[K_i, K_j] = -\epsilon_{ijk}J_k$, a $J$, which is *not* a linear combination of $K$'s — not closed.

---

# Solution

Matrix multiplication gives $[J_3, K_1] = K_2$, the relation $[J_i, K_j] = \epsilon_{ijk}K_k$ that says $\mathbf{K}$ is a vector under rotations. The vanishing $[J_3, K_3] = 0$ reflects that a rotation fixes the axis it rotates about. The $J$'s close into $\mathfrak{so}(3)$ because $[J,J] = J$; the $K$'s do not because $[K,K] = -J$ lands outside their span.

**Step 1: $[J_3, K_1] = K_2$.**

> [!note]- Derivation
> The matrices:
> $$J_3 = \begin{pmatrix} 0&0&0&0\\ 0&0&-1&0\\ 0&1&0&0\\ 0&0&0&0 \end{pmatrix},\qquad
> K_1 = \begin{pmatrix} 0&1&0&0\\ 1&0&0&0\\ 0&0&0&0\\ 0&0&0&0 \end{pmatrix},\qquad
> K_2 = \begin{pmatrix} 0&0&1&0\\ 0&0&0&0\\ 1&0&0&0\\ 0&0&0&0 \end{pmatrix}.$$
> Compute $J_3 K_1$: row $2$ of $J_3$ is $(0,1,0,0)$, hitting column $0$ of $K_1$ ($(0,1,0,0)^{\mathsf T}$) gives $(J_3 K_1)_{20} = 1$. Other entries vanish. So $J_3 K_1$ has a single $1$ at $(2,0)$.
> Compute $K_1 J_3$: row $0$ of $K_1$ is $(0,1,0,0)$, hitting column $2$ of $J_3$ ($(0,-1,0,0)^{\mathsf T}$) gives $(K_1 J_3)_{02} = -1$. So $K_1 J_3$ has a single $-1$ at $(0,2)$.
> Subtract:
> $$[J_3, K_1] = J_3 K_1 - K_1 J_3 = \begin{pmatrix} 0&0&1&0\\ 0&0&0&0\\ 1&0&0&0\\ 0&0&0&0 \end{pmatrix} = K_2.$$
> (The $+1$ at $(2,0)$ comes from $J_3 K_1$; the $+1$ at $(0,2)$ comes from $-(-1)$ in $-K_1 J_3$.) This matches $[J_3, K_1] = \epsilon_{31k}K_k = \epsilon_{312}K_2 = K_2$.

**Step 2: $\mathbf{K}$ is a vector under rotations.**

> [!note]- Derivation
> An object $\{V_j\}_{j=1,2,3}$ is a **vector operator** under rotations if its components satisfy $[J_i, V_j] = \epsilon_{ijk}V_k$ — this is the infinitesimal statement that under a rotation generated by $J_i$, the components $V_j$ rotate into each other exactly as the components of a spatial $3$-vector do. The boost generators satisfy precisely this:
> $$[J_i, K_j] = \epsilon_{ijk}K_k.$$
> So the triple $\mathbf{K} = (K_1, K_2, K_3)$ transforms as a $3$-vector under spatial rotations — which is geometrically obvious, since $K_i$ generates a boost *along the $i$-th spatial axis*, and rotating space rotates the boost direction. The relation is the algebraic encoding of "a boost has a direction, and that direction rotates with space".

**Step 3: $[J_3, K_3] = 0$.**

> [!note]- Derivation
> From the relation, $[J_3, K_3] = \epsilon_{33k}K_k = 0$, since $\epsilon_{33k} = 0$ (two repeated indices). Directly: $J_3$ (rotating $x$–$y$) and $K_3$ (boosting along $z$) act on disjoint blocks — $J_3$ on indices $\{1,2\}$, $K_3$ on indices $\{0,3\}$ — so their matrices commute, $J_3 K_3 = K_3 J_3 = 0$ (the product of matrices supported on disjoint index sets vanishes here), giving $[J_3, K_3] = 0$.
>
> Geometrically: a rotation about the $z$-axis leaves the $z$-direction invariant. A boost along $z$ is a transformation in the $t$–$z$ plane. Since the rotation does not touch the $z$-direction, it does not affect the boost along $z$ — they commute. More generally $[J_i, K_i] = 0$ (no sum): a rotation about an axis commutes with a boost along the *same* axis.

**Step 4: $J$'s close, $K$'s do not.**

> [!note]- Derivation
> A set of generators spans a **subalgebra** if and only if the bracket of any two lies in their span.
>
> *The rotations close.* $[J_i, J_j] = \epsilon_{ijk}J_k$: the right-hand side is always a linear combination of the $J$'s. So $\mathrm{span}\{J_1, J_2, J_3\}$ is closed under the bracket — it is a three-dimensional subalgebra, a copy of $\mathfrak{so}(3)$, the [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices|rotation algebra]]. This reflects the physical fact that **the spatial rotations form a subgroup** $SO(3) \subset SO^+(1,3)$: composing two rotations gives a rotation.
>
> *The boosts do not close.* $[K_i, K_j] = -\epsilon_{ijk}J_k$: the right-hand side is a *rotation* generator, which is *not* a linear combination of the boost generators (the $J$'s and $K$'s are linearly independent). So $\mathrm{span}\{K_1, K_2, K_3\}$ is *not* closed under the bracket — it is not a subalgebra. This reflects the physical fact that **the boosts do not form a subgroup**: composing two boosts in different directions yields a boost *times a rotation* (the [[Def - Thomas Rotation|Thomas rotation]]), not a pure boost.

> [!note]- Complete formal solution
> With $J_3$ (nonzero at $(1,2)=-1$, $(2,1)=+1$) and $K_1$ (nonzero at $(0,1),(1,0)$): $J_3 K_1$ is nonzero only at $(2,0)$ (value $+1$), and $K_1 J_3$ only at $(0,2)$ (value $-1$); subtracting gives $[J_3,K_1]$ with $+1$ at $(2,0)$ and $+1$ at $(0,2)$, which is $K_2$. Hence $[J_i,K_j] = \epsilon_{ijk}K_k$, exactly the vector-operator condition, so $\mathbf{K}$ transforms as a $3$-vector under rotations. Setting $i=j=3$ gives $[J_3,K_3] = \epsilon_{33k}K_k = 0$: a rotation about $z$ commutes with a boost along $z$, because the rotation fixes the $z$-axis. Finally, $[J_i,J_j] = \epsilon_{ijk}J_k$ has the right-hand side always in $\mathrm{span}\{J_k\}$, so the rotations form a closed subalgebra $\mathfrak{so}(3)$ (reflecting the rotation subgroup), while $[K_i,K_j] = -\epsilon_{ijk}J_k$ has the right-hand side outside $\mathrm{span}\{K_k\}$, so the boosts are not closed (reflecting that composing boosts yields a Thomas rotation). $\blacksquare$

---

# Key Takeaways

**The relation $[J_i, K_j] = \epsilon_{ijk}K_k$ is the statement "the boost is a vector", and it is the universal signature of a vector operator.** The mixed commutator delivers more than a number: its index structure $\epsilon_{ijk}$ is *exactly* the form $[J_i, V_j] = \epsilon_{ijk}V_k$ that defines a vector operator in quantum mechanics, so $\mathbf{K}$ rotates as a spatial $3$-vector. The trigger for recognising this pattern anywhere: a triple of objects $\{V_1, V_2, V_3\}$ whose commutators with the angular-momentum generators close back into the triple with an $\epsilon$ is a vector under rotations — examples include position $\mathbf{x}$, momentum $\mathbf{p}$, the boost generators $\mathbf{K}$, and the electric field $\mathbf{E}$. The reusable diagnostic: to determine how an object transforms under rotations, compute $[J_i, \text{object}]$ and match the index structure — scalar if it gives zero, vector if it gives $\epsilon_{ijk}(\text{object})_k$, tensor for more indices. The boost generators are a textbook vector operator, which is why "a boost has a direction" is encoded algebraically as exactly this commutator.

**Closure under the bracket is decided by the right-hand side of the structure relations, and it is the algebraic test for a subgroup.** The cleanest way to ask "do these generators form a subgroup?" is to ask "do their brackets stay in their span?", and the answer is read directly off which generators appear on the right of the structure relations. The rotations close ($[J,J] = J$, always a $J$), so they form the subgroup $SO(3)$. The boosts do not close ($[K,K] = -J$, a rotation), so they form *no* subgroup. The reusable principle: a subspace of a Lie algebra is a subalgebra iff it is closed under the bracket, and closure is a finite check on the structure relations — for each pair of basis elements in the subspace, verify the bracket lands back in the subspace. This is the infinitesimal version of "closed under the group operation", and it is far easier to check than the group-level statement, which is one more reason to work in the algebra.

**The non-closure of the boosts is the Thomas rotation in embryo.** The fact that $[K_i, K_j] = -\epsilon_{ijk}J_k$ lands *outside* the boost subspace is not a technical annoyance — it is the algebraic origin of one of relativity's genuine surprises. Because composing two boosts in different directions requires the bracket $[K_i, K_j]$, and that bracket is a rotation, the composition of two non-collinear boosts is a boost *times a rotation*: the [[Def - Thomas Rotation|Thomas rotation]]. A particle whose velocity direction changes (a circular orbit, say) undergoes a continuous sequence of boosts in different directions, and the accumulated rotations make its spin precess — the Thomas precession, observable in atomic fine structure. So the abstract statement "the boost generators are not closed under the bracket" has a concrete, measurable consequence, and the chain from one to the other runs through the Baker–Campbell–Hausdorff formula, where the leading correction to naive boost composition is exactly this $\tfrac12[K_i, K_j] = -\tfrac12\epsilon_{ijk}J_k$.
