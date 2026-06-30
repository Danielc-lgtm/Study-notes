---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Infinitesimal Lorentz Transformations"
tags: [physics, special-relativity, lie-groups]
---

# Problem Statement

1. Write the most general element $\omega \in \mathfrak{so}(1,3)$ as an explicit $4\times4$ matrix in terms of six real parameters: three boost rapidities $(k_1, k_2, k_3)$ and three rotation angles $(j_1, j_2, j_3)$.
2. Verify that $\omega$ satisfies the generator condition $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ (equivalently, $\eta\,\omega$ is antisymmetric).
3. Identify the components $\omega_{\mu\nu}$ (both indices down) and confirm the antisymmetric array $\omega_{\mu\nu}$ has exactly six independent entries, organised as three time-space ($\omega_{0i}$, the boosts) and three space-space ($\omega_{ij}$, the rotations).
4. Check that $\mathrm{tr}\,\omega = 0$, and explain why this guarantees $\det\exp(\omega) = 1$.

**Recall:**

![[Def - Lie Algebra of the Lorentz Group#The Definition]]

A general element is $\omega = k_1 K_1 + k_2 K_2 + k_3 K_3 + j_1 J_1 + j_2 J_2 + j_3 J_3$, with $K_i$ the boost generators (symmetric, $1$ in the $(0,i)/(i,0)$ slots) and $J_i$ the rotation generators (antisymmetric, acting as $\mathbf{e}_i\times$). The index-lowered form is $\omega_{\mu\nu} = \eta_{\mu\alpha}\omega^\alpha{}_\nu$. The determinant identity is $\det\exp(\omega) = e^{\mathrm{tr}\,\omega}$.

---

# Convergent Strategy

**Problem class.** A *Lie algebra computation* of the most elementary kind: assemble the general generator from the basis and verify the defining condition. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]]'s first move for any algebra question is the generator condition, and here we both build the general element and check it satisfies the condition.

**Assumption pattern.** The six basis generators are explicit and sparse, and a general element is their linear combination. The signpost is that the boost coefficients fill the time-space entries and the rotation coefficients fill the space-space entries, so the general matrix has a clean block structure.

**Theorem routing.** Part 1: superpose the six basis matrices, placing $k_i$ in the time-space slots and $j_i$ in the space-space slots. Part 2: check $\eta\,\omega$ antisymmetric, which holds because each basis generator satisfies it ([[Def - Infinitesimal Lorentz Transformations]]). Part 3: lower an index to read off $\omega_{\mu\nu}$ antisymmetric with six entries. Part 4: $\mathrm{tr}\,\omega = 0$ by inspection (the diagonal is zero), giving $\det\exp(\omega) = e^0 = 1$.

**Key decision point.** The crux is the block layout: the boost parameters $k_i$ occupy the *first row and first column* (mixing time with space, symmetrically), while the rotation parameters $j_i$ occupy the *spatial $3\times3$ block* (antisymmetrically). Getting the symmetry types right — boosts symmetric across the time axis, rotations antisymmetric in space — is the whole content, and it is exactly the lowered-index antisymmetry condition manifesting differently in the two blocks.

---

# Legal Operations Used

1. **Check the generator condition by lowering an index (operation 2 from the topic page).** Part 2: confirm $\eta\,\omega$ is antisymmetric for the general $\omega$.

2. **Linearise / build from generators (operation 1 from the topic page).** Part 1: the general element is the linear combination of the six generators, the basis of $\mathfrak{so}(1,3)$.

---

# Hints

> [!note]- Hint 1
> Superpose: $\omega = \sum_i k_i K_i + \sum_i j_i J_i$. The $K_i$ contribute to the first row and column (time-space); the $J_i$ contribute to the spatial $3\times3$ block. Write the resulting $4\times4$ matrix.

> [!note]- Hint 2
> The first row of $\omega$ is $(0, k_1, k_2, k_3)$ and the first column is $(0, k_1, k_2, k_3)^{\mathsf T}$ — symmetric. The spatial block is the antisymmetric $\hat{\mathbf{j}}$ with $\mathbf{j} = (j_1, j_2, j_3)$.

> [!note]- Hint 3
> Multiplying by $\eta = \mathrm{diag}(1,-1,-1,-1)$ on the left flips the sign of rows $1,2,3$. Check that the result is antisymmetric: the time-space entries become equal-and-opposite, the spatial block stays antisymmetric.

> [!note]- Hint 4
> The diagonal of $\omega$ is all zeros (boosts have zero diagonal, rotations have zero diagonal), so $\mathrm{tr}\,\omega = 0$. Then $\det\exp(\omega) = e^{\mathrm{tr}\,\omega} = e^0 = 1$.

---

# Solution

The general generator is the superposition $\sum k_i K_i + \sum j_i J_i$: the boost rapidities fill the symmetric time-space slots, the rotation angles fill the antisymmetric spatial block. It satisfies $\eta\,\omega$ antisymmetric, has six independent components, and zero trace — so its exponential is a proper Lorentz transformation.

**Step 1: The general element.**

> [!note]- Derivation
> Superposing the six generators,
> $$\omega = k_1 K_1 + k_2 K_2 + k_3 K_3 + j_1 J_1 + j_2 J_2 + j_3 J_3 = \begin{pmatrix} 0 & k_1 & k_2 & k_3 \\ k_1 & 0 & -j_3 & j_2 \\ k_2 & j_3 & 0 & -j_1 \\ k_3 & -j_2 & j_1 & 0 \end{pmatrix}.$$
> The first row and column carry the three boost rapidities $k_i$ (symmetrically: the $(0,i)$ and $(i,0)$ entries are both $k_i$, since each $K_i$ is a symmetric matrix). The spatial $3\times3$ block carries the three rotation angles as the antisymmetric hat matrix $\hat{\mathbf{j}}$, $\mathbf{j} = (j_1, j_2, j_3)$ — the $J_i$ acting as $\mathbf{e}_i\times$. This is the most general matrix that is "antisymmetric once an index is lowered".

**Step 2: Verify $\eta\,\omega$ is antisymmetric.**

> [!note]- Derivation
> Multiply on the left by $\eta = \mathrm{diag}(1,-1,-1,-1)$, which scales row $0$ by $+1$ and rows $1,2,3$ by $-1$:
> $$\eta\,\omega = \begin{pmatrix} 0 & k_1 & k_2 & k_3 \\ -k_1 & 0 & j_3 & -j_2 \\ -k_2 & -j_3 & 0 & j_1 \\ -k_3 & j_2 & -j_1 & 0 \end{pmatrix}.$$
> This matrix is antisymmetric: $(\eta\,\omega)_{\mu\nu} = -(\eta\,\omega)_{\nu\mu}$ for every pair. (Check the time-space entries: $(\eta\,\omega)_{0i} = k_i$ and $(\eta\,\omega)_{i0} = -k_i$, opposite. The spatial block was already antisymmetric and stays so after the uniform sign flip on its rows, because $-\hat{\mathbf{j}}$ is still antisymmetric.) So $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ holds, confirming $\omega \in \mathfrak{so}(1,3)$.

**Step 3: The components $\omega_{\mu\nu}$ and the count of six.**

> [!note]- Derivation
> The index-lowered components are $\omega_{\mu\nu} = (\eta\,\omega)_{\mu\nu}$, read off the matrix in Step 2:
> $$\omega_{0i} = k_i \quad(\text{three time-space entries, the boosts}),\qquad \omega_{ij} = \epsilon_{ijk}j_k \quad(\text{three space-space entries, the rotations}),$$
> with $\omega_{\mu\nu} = -\omega_{\nu\mu}$. An antisymmetric $4\times4$ matrix has $\binom{4}{2} = 6$ independent entries — exactly the six parameters $(k_1, k_2, k_3, j_1, j_2, j_3)$. They split as three time-space ($\omega_{0i} = k_i$) and three space-space ($\omega_{ij}$), confirming $\dim\mathfrak{so}(1,3) = 6$ with the boost/rotation decomposition. There is a perfect correspondence: each independent entry of the antisymmetric array $\omega_{\mu\nu}$ is one generator.

**Step 4: $\mathrm{tr}\,\omega = 0$ and $\det\exp\omega = 1$.**

> [!note]- Derivation
> The diagonal entries of $\omega$ (from Step 1) are all zero: the boost generators have zero diagonal (their nonzero entries are off-diagonal time-space slots), and the rotation generators have zero diagonal (antisymmetric matrices have zero diagonal). So
> $$\mathrm{tr}\,\omega = \omega^0{}_0 + \omega^1{}_1 + \omega^2{}_2 + \omega^3{}_3 = 0.$$
> By the determinant identity $\det\exp(\omega) = e^{\mathrm{tr}\,\omega}$, we get $\det\exp(\omega) = e^0 = 1$. So every $\exp(\omega)$ for $\omega \in \mathfrak{so}(1,3)$ has determinant $+1$ — it lands in the *proper* Lorentz group. This is the infinitesimal reason the exponential map cannot reach the improper components ($\det = -1$): the generators are traceless, so their exponentials have unit determinant.

> [!note]- Complete formal solution
> Superposing the six generators, the general $\omega \in \mathfrak{so}(1,3)$ is the matrix with first row/column $(0, k_1, k_2, k_3)$ (symmetric time-space, the boosts) and spatial block the antisymmetric hat matrix $\hat{\mathbf{j}}$ (the rotations):
> $$\omega = \begin{pmatrix} 0 & k_1 & k_2 & k_3 \\ k_1 & 0 & -j_3 & j_2 \\ k_2 & j_3 & 0 & -j_1 \\ k_3 & -j_2 & j_1 & 0 \end{pmatrix}.$$
> Left-multiplying by $\eta$ gives an antisymmetric matrix $\eta\,\omega$ (time-space entries become $\pm k_i$, spatial block $-\hat{\mathbf{j}}$ still antisymmetric), so $\omega^{\mathsf T}\eta + \eta\,\omega = 0$ and $\omega \in \mathfrak{so}(1,3)$. The lowered components are $\omega_{0i} = k_i$, $\omega_{ij} = \epsilon_{ijk}j_k$, an antisymmetric array with exactly six independent entries (three boosts, three rotations), so $\dim\mathfrak{so}(1,3) = 6$. The diagonal of $\omega$ is zero, so $\mathrm{tr}\,\omega = 0$ and $\det\exp(\omega) = e^0 = 1$ — the exponential lands in the proper Lorentz group. $\blacksquare$

---

# Key Takeaways

**The general Lorentz generator is a boost vector in the time row and a rotation vector in the spatial block.** The most general element of $\mathfrak{so}(1,3)$ has a transparent layout once the symmetry types are right: the three boost rapidities $k_i$ fill the first row and column *symmetrically* (mixing time with each space axis), and the three rotation angles $j_i$ fill the spatial $3\times3$ block *antisymmetrically* (as the hat matrix). The reusable picture: a Lorentz generator is "$\mathbf{k}$ in the time slots, $\hat{\mathbf{j}}$ in the space block", six numbers total. This layout is the fastest way to write down or recognise a generator, and it makes the boost/rotation split visible at a glance — the symmetric part (across the time axis) is the boost content, the antisymmetric spatial part is the rotation content. The same template, with the time row replaced by a fourth spatial row, gives the general element of Euclidean $\mathfrak{so}(4)$, differing only in whether the time-space block is symmetric (Lorentz) or antisymmetric (Euclidean).

**The six independent entries of an antisymmetric $4\times4$ array are exactly the six generators — the dimension count made concrete.** The lowered-index form $\omega_{\mu\nu}$ is genuinely antisymmetric, and an antisymmetric $4\times4$ matrix has $\binom{4}{2} = 6$ independent entries above the diagonal. Each entry is one generator: the three time-space entries $\omega_{0i}$ are the boosts, the three space-space entries $\omega_{ij}$ are the rotations. The reusable principle is that the dimension of $\mathfrak{so}(p,q)$ in $n = p+q$ dimensions is always $\binom{n}{2}$, the number of independent antisymmetric components, regardless of signature — the signature affects the *symmetry type* of the generators as plain matrices (which entries are symmetric versus antisymmetric) but not their *count*. So $\dim\mathfrak{so}(1,3) = \dim\mathfrak{so}(4) = 6$, and the difference between Lorentz and Euclidean is in the brackets and the matrix realisations, not the dimension.

**Tracelessness of generators is why the exponential map lands in the proper group.** Every Lorentz generator has zero trace — the boosts because their nonzero entries are off-diagonal, the rotations because antisymmetric matrices have zero diagonal — and the determinant identity $\det\exp(\omega) = e^{\mathrm{tr}\,\omega}$ then forces $\det\exp(\omega) = 1$. This is the infinitesimal explanation for a global fact: the exponential map reaches only the *proper orthochronous* component $SO^+(1,3)$, never the improper ($\det = -1$) or antichronous components, because those are disconnected from the identity and the continuous image of the (connected, traceless) Lie algebra cannot jump to them. The reusable diagnostic: to check whether a one-parameter family $\exp(t\omega)$ stays in the special (determinant-one) subgroup, check whether the generator is traceless — and for any $\mathfrak{so}(p,q)$ or $\mathfrak{su}(n)$ generator, it automatically is. Tracelessness of the algebra is the shadow of determinant-one of the group.
