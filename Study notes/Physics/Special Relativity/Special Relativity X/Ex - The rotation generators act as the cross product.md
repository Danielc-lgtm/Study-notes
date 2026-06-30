---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Generators and Structure Constants"
tags: [physics, special-relativity, lie-groups]
---

# Problem Statement

1. Show that the rotation generator $J_i$, acting on a four-vector, leaves the time component fixed and acts on the spatial part $\mathbf{v}$ as the cross product $\mathbf{e}_i \times \mathbf{v}$.
2. Verify that the three rotation generators close into the Lie algebra $\mathfrak{so}(3)$ with bracket the cross product, $[J_i, J_j] = \epsilon_{ijk}J_k$, identical to $(\mathbb{R}^3, \times)$ under the hat map.
3. Conclude that the rotation block of $\mathfrak{so}(1,3)$ is the angular-momentum algebra, and state the corresponding quantum and Poisson-bracket relations.

**Recall:**

![[Def - Lie Algebra of the Lorentz Group#The Definition]]

The cross product on $\mathbb{R}^3$ is $(\mathbf{a} \times \mathbf{b})_i = \epsilon_{ijk}a_j b_k$. The **hat map** sends a vector $\mathbf{v} \in \mathbb{R}^3$ to the antisymmetric matrix $\hat{\mathbf{v}}$ with $\hat{\mathbf{v}}\,\mathbf{w} = \mathbf{v} \times \mathbf{w}$; explicitly $\hat{\mathbf{v}} = \begin{pmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0\end{pmatrix}$. The Lie algebra $\mathfrak{so}(3)$ of antisymmetric $3\times3$ matrices satisfies $[\hat{\mathbf{u}}, \hat{\mathbf{v}}] = \widehat{\mathbf{u}\times\mathbf{v}}$.

---

# Convergent Strategy

**Problem class.** A *Lie algebra computation* connecting the rotation generators of $\mathfrak{so}(1,3)$ to the familiar $\mathfrak{so}(3)$ of the cross product. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] notes that the rotation block is "an object the reader already knows under three names — angular momentum, the cross product, $\mathfrak{su}(2)$".

**Assumption pattern.** The rotation generator $J_i$ is supported entirely on the spatial block (its time row and column are zero), so its action on a four-vector is its action on the spatial part — and that spatial action is exactly the hat matrix $\hat{\mathbf{e}}_i$. The signpost is that $J_i$, restricted to the spatial block, *is* the antisymmetric matrix $\hat{\mathbf{e}}_i$.

**Theorem routing.** Part 1: write $J_i$ as a $4\times4$ matrix, observe the time row/column vanish, and identify the spatial $3\times3$ block as $\hat{\mathbf{e}}_i$, so $J_i\mathbf{v} = \mathbf{e}_i\times\mathbf{v}$. Part 2: the bracket $[J_i, J_j]$ restricts to $[\hat{\mathbf{e}}_i, \hat{\mathbf{e}}_j] = \widehat{\mathbf{e}_i\times\mathbf{e}_j} = \widehat{\epsilon_{ijk}\mathbf{e}_k} = \epsilon_{ijk}\hat{\mathbf{e}}_k$, matching $[J_i, J_j] = \epsilon_{ijk}J_k$ ([[Def - Generators and Structure Constants]]). Part 3: identify with angular momentum.

**Key decision point.** The crux is recognising that the embedding of $\mathfrak{so}(3)$ into $\mathfrak{so}(1,3)$ as the block-diagonal $\mathrm{diag}(0, \hat{\mathbf{e}}_i)$ is faithful and bracket-preserving, so *no computation specific to the Lorentz algebra is needed* — the rotation block is literally $\mathfrak{so}(3)$, and everything known about the cross product transfers verbatim. The temptation is to recompute the brackets from the $4\times4$ matrices; the efficient route is to recognise the spatial block as the hat map and import the known $\mathfrak{so}(3)$ result.

---

# Legal Operations Used

1. **Compute a commutator from the structure relations (operation 3 from the topic page).** Part 2 evaluates $[J_i, J_j]$ via the cross-product structure of $\mathfrak{so}(3)$, recognising the spatial block.

2. **Check the generator condition (operation 2 from the topic page).** $J_i$ is antisymmetric on the spatial block, so $\eta J_i = -J_i$ there is antisymmetric — confirming $J_i \in \mathfrak{so}(1,3)$.

---

# Hints

> [!note]- Hint 1
> Write $J_1, J_2, J_3$ as $4\times4$ matrices. Notice that for each, the entire row $0$ and column $0$ (the time slots) are zero — they act only on the spatial indices $\{1,2,3\}$.

> [!note]- Hint 2
> The spatial $3\times3$ block of $J_i$ is exactly the hat matrix $\hat{\mathbf{e}}_i$. For instance the spatial block of $J_3$ is $\begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&0\end{pmatrix} = \hat{\mathbf{e}}_3$. So $J_i\mathbf{v} = \hat{\mathbf{e}}_i\mathbf{v} = \mathbf{e}_i\times\mathbf{v}$.

> [!note]- Hint 3
> Since the generators are block-diagonal $\mathrm{diag}(0, \hat{\mathbf{e}}_i)$, their commutators are computed entirely in the spatial block: $[J_i, J_j] = \mathrm{diag}(0, [\hat{\mathbf{e}}_i, \hat{\mathbf{e}}_j])$. Use the $\mathfrak{so}(3)$ identity $[\hat{\mathbf{u}}, \hat{\mathbf{v}}] = \widehat{\mathbf{u}\times\mathbf{v}}$.

> [!note]- Hint 4
> $\mathbf{e}_i \times \mathbf{e}_j = \epsilon_{ijk}\mathbf{e}_k$, so $[\hat{\mathbf{e}}_i, \hat{\mathbf{e}}_j] = \widehat{\epsilon_{ijk}\mathbf{e}_k} = \epsilon_{ijk}\hat{\mathbf{e}}_k$, which lifts to $[J_i, J_j] = \epsilon_{ijk}J_k$.

---

# Solution

The rotation generator $J_i$ vanishes on the time slot and acts on the spatial part as the hat matrix $\hat{\mathbf{e}}_i$, i.e. as $\mathbf{e}_i\times$. So the rotation block of $\mathfrak{so}(1,3)$ is the embedded $\mathfrak{so}(3)$, whose bracket is the cross product — the angular-momentum algebra.

**Step 1: $J_i$ acts as $\mathbf{e}_i\times$ on the spatial part.**

> [!note]- Derivation
> The rotation generators as $4\times4$ matrices:
> $$J_1 = \begin{pmatrix} 0&0&0&0\\ 0&0&0&0\\ 0&0&0&-1\\ 0&0&1&0 \end{pmatrix},\quad
> J_2 = \begin{pmatrix} 0&0&0&0\\ 0&0&0&1\\ 0&0&0&0\\ 0&-1&0&0 \end{pmatrix},\quad
> J_3 = \begin{pmatrix} 0&0&0&0\\ 0&0&-1&0\\ 0&1&0&0\\ 0&0&0&0 \end{pmatrix}.$$
> Every one has zero time row and column, so applied to a four-vector $X = (X^0, \mathbf{v})$ it gives $J_i X = (0, \hat{\mathbf{e}}_i\mathbf{v})$ — the time component is annihilated and the spatial part is acted on by the spatial $3\times3$ block. That block is precisely the hat matrix $\hat{\mathbf{e}}_i$: for $J_3$, the block is $\begin{pmatrix} 0&-1&0\\ 1&0&0\\ 0&0&0\end{pmatrix} = \hat{\mathbf{e}}_3$; similarly $J_1 \to \hat{\mathbf{e}}_1$, $J_2 \to \hat{\mathbf{e}}_2$. Since $\hat{\mathbf{e}}_i\mathbf{v} = \mathbf{e}_i\times\mathbf{v}$,
> $$J_i\,(X^0, \mathbf{v}) = (0,\ \mathbf{e}_i\times\mathbf{v}).$$
> So $J_i$ generates a rotation about the $\mathbf{e}_i$-axis, with the time component a spectator.

**Step 2: The rotations close into $\mathfrak{so}(3)$.**

> [!note]- Derivation
> The generators are block-diagonal, $J_i = \mathrm{diag}(0, \hat{\mathbf{e}}_i)$, so any commutator is computed in the spatial block alone:
> $$[J_i, J_j] = \mathrm{diag}\big(0,\ [\hat{\mathbf{e}}_i, \hat{\mathbf{e}}_j]\big).$$
> The defining identity of $\mathfrak{so}(3)$ under the hat map is $[\hat{\mathbf{u}}, \hat{\mathbf{v}}] = \widehat{\mathbf{u}\times\mathbf{v}}$. With $\mathbf{u} = \mathbf{e}_i$, $\mathbf{v} = \mathbf{e}_j$, and $\mathbf{e}_i\times\mathbf{e}_j = \epsilon_{ijk}\mathbf{e}_k$,
> $$[\hat{\mathbf{e}}_i, \hat{\mathbf{e}}_j] = \widehat{\mathbf{e}_i\times\mathbf{e}_j} = \widehat{\epsilon_{ijk}\mathbf{e}_k} = \epsilon_{ijk}\hat{\mathbf{e}}_k.$$
> Lifting back to the $4\times4$ block-diagonal form,
> $$[J_i, J_j] = \epsilon_{ijk}J_k,$$
> exactly the rotation structure relation. So $\mathrm{span}\{J_1, J_2, J_3\}$ is a faithful copy of $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ sitting inside $\mathfrak{so}(1,3)$ — see [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices]].

**Step 3: This is the angular-momentum algebra.**

> [!note]- Derivation
> The relation $[J_i, J_j] = \epsilon_{ijk}J_k$ is the **angular-momentum algebra**, the most ubiquitous Lie algebra in physics. It appears in three guises that are all the same structure:
> - *Lie algebra / cross product:* $[J_i, J_j] = \epsilon_{ijk}J_k$, or equivalently $[\hat{\mathbf{e}}_i, \hat{\mathbf{e}}_j] = \widehat{\mathbf{e}_i\times\mathbf{e}_j}$.
> - *Classical mechanics (Poisson bracket):* for the angular-momentum functions on phase space, $\{L_i, L_j\} = \epsilon_{ijk}L_k$, the [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|Hamiltonian]] generators of rotations.
> - *Quantum mechanics:* $[\hat L_i, \hat L_j] = i\hbar\,\epsilon_{ijk}\hat L_k$, the commutators of the angular-momentum operators (the $i\hbar$ being the Hermitian-generator convention).
>
> So the rotation block of $\mathfrak{so}(1,3)$ is literally angular momentum. The boost generators $K_i$ are the genuinely new, relativistic addition to this familiar core, attached as a vector ($[J, K] = K$) with mutual commutators that are rotations ($[K, K] = -J$).

> [!note]- Complete formal solution
> Each rotation generator $J_i$ has zero time row and column, so on a four-vector $(X^0, \mathbf{v})$ it gives $(0, \hat{\mathbf{e}}_i\mathbf{v}) = (0, \mathbf{e}_i\times\mathbf{v})$, the spatial block being the hat matrix $\hat{\mathbf{e}}_i$. The generators are block-diagonal $\mathrm{diag}(0, \hat{\mathbf{e}}_i)$, so $[J_i, J_j] = \mathrm{diag}(0, [\hat{\mathbf{e}}_i, \hat{\mathbf{e}}_j])$; by the $\mathfrak{so}(3)$ identity $[\hat{\mathbf{e}}_i, \hat{\mathbf{e}}_j] = \widehat{\mathbf{e}_i\times\mathbf{e}_j} = \epsilon_{ijk}\hat{\mathbf{e}}_k$, this is $[J_i, J_j] = \epsilon_{ijk}J_k$. Hence the rotation generators form a faithful $\mathfrak{so}(3) \cong (\mathbb{R}^3,\times)$ inside $\mathfrak{so}(1,3)$ — the angular-momentum algebra, which classically reads $\{L_i, L_j\} = \epsilon_{ijk}L_k$ and quantum-mechanically $[\hat L_i, \hat L_j] = i\hbar\epsilon_{ijk}\hat L_k$. $\blacksquare$

---

# Key Takeaways

**The rotation block of $\mathfrak{so}(1,3)$ is the cross product, so you already know half the Lorentz algebra.** The three rotation generators $J_i$ are nothing but the angular-momentum / cross-product algebra $\mathfrak{so}(3)$, embedded block-diagonally with the time direction as a spectator. The reusable recognition: whenever a generator acts as $\mathbf{e}_i\times$ on a vector — equivalently, whenever its matrix is the hat $\hat{\mathbf{e}}_i$ — it is a rotation generator, and its brackets are governed by the cross product. This means the entire apparatus of $\mathfrak{so}(3)$ transfers verbatim: the structure constants are $\epsilon_{ijk}$, the Jacobi identity is the cross-product Jacobi identity $\mathbf{u}\times(\mathbf{v}\times\mathbf{w}) + \text{cyclic} = 0$, and the Casimir is $\mathbf{J}^2$. The new content of the Lorentz algebra over the rotation algebra is precisely the three boosts and how they attach; the rotational core is old.

**The hat map is a Lie algebra isomorphism, and it lets you compute Lorentz rotation brackets with vector identities.** The identification $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ via the hat map is more than a notational convenience — it is an isomorphism of Lie algebras, sending the matrix commutator to the cross product, $[\hat{\mathbf{u}}, \hat{\mathbf{v}}] = \widehat{\mathbf{u}\times\mathbf{v}}$. The reusable consequence is that any computation of rotation-generator brackets can be done with three-dimensional vector algebra instead of $4\times4$ (or even $3\times3$) matrix multiplication: replace generators by their axis vectors, replace commutators by cross products, and read off the answer. The trigger: a bracket of two rotation generators (or two angular momenta) is a cross product of their axes. This is why the rotation sector of every relevant Lie algebra in physics — $\mathfrak{so}(3)$, the rotation block of $\mathfrak{so}(1,3)$, each $\mathfrak{su}(2)$ factor of the $(A,B)$ decomposition — is computationally trivial: it is just the cross product.

**Angular momentum is the same structure in three languages, and the Lorentz algebra inherits it.** The relation $[J_i, J_j] = \epsilon_{ijk}J_k$ recurs as the Poisson bracket $\{L_i, L_j\} = \epsilon_{ijk}L_k$ of classical mechanics and the commutator $[\hat L_i, \hat L_j] = i\hbar\epsilon_{ijk}\hat L_k$ of quantum mechanics — one algebra, three dialects, differing only by the placement of $i\hbar$. The Lorentz algebra contains this as its rotation block, which is why "spin" and "angular momentum" carry over unchanged into relativistic physics and why the $(A,B)$ decomposition, splitting the Lorentz algebra into two copies of this same $\mathfrak{su}(2)$, makes the representation theory tractable. The transferable insight: when you meet the bracket $[\cdot, \cdot] = \epsilon(\cdot)$ in any context — a symmetry algebra, a set of conserved charges, a spin system — you are looking at angular momentum, and the full theory of spin (multiplets, ladder operators, Clebsch–Gordan, the Wigner–Eckart theorem) applies. The rotation generators of the Lorentz group are the doorway through which all of that machinery enters relativity.
