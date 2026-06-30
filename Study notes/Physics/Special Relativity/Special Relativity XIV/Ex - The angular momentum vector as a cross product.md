---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Observer and Local Rest Space"
  - "Def - The Levi-Civita Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

Relative to an observer of four-velocity $U_0$, the [[Def - Angular Momentum Four-Tensor|angular momentum tensor]] $J_{\alpha\beta}$ splits into an angular momentum vector $\vec\sigma_C$ (space-space block) and a mass-energy dipole moment (time-space block). Working with $c = 1$:

1. Starting from $J_C = \overrightarrow{CM}^\flat\wedge p$ and the decompositions $\overrightarrow{CM} = hU_0 + \vec X$ and $p = EU_0 + \mathbf{p}$ (with $\vec X, \mathbf{p}\in E_{u_0}$), show that the angular momentum vector is the rest-space cross product $\vec\sigma_C = \vec X\times\mathbf{p} = \overrightarrow{CM}\times\mathbf{p}$, with components $\sigma_C^1 = X^2p^3 - X^3p^2$, $\sigma_C^2 = X^3p^1 - X^1p^3$, $\sigma_C^3 = X^1p^2 - X^2p^1$.
2. Show that the time-space block of $J_{\alpha\beta}$ is $E X^i - h p^i$ — the mass-energy dipole contribution — and write out the full $4\times 4$ matrix $(J_{\alpha\beta})$ in the observer's orthonormal frame.
3. Explain why this is the relativistic upgrade of the Newtonian $\mathbf{L} = \mathbf{r}\times\mathbf{p}$, and identify what the extra time-space components encode that has no Newtonian analogue.
4. Recover the angular momentum vector from the tensor by the contraction $\sigma_C^i = \tfrac12\epsilon^{ijk}J_{jk}$, and verify it agrees with part 1.

**Recall:**

![[Def - Angular Momentum Four-Tensor#The Definition]]

An [[Def - Observer and Local Rest Space|observer]] of four-velocity $U_0$ has a local rest space $E_{u_0} = U_0^\perp$, a three-dimensional Euclidean space. The [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] $\epsilon$ induces a cross product on $E_{u_0}$: $(\vec a\times\vec b)^i = \epsilon^{ijk}a_jb_k$. The energy is $E = p\cdot U_0$ and the spatial momentum $\mathbf{p} = p - EU_0$.

---

# Convergent Strategy

**Problem class.** A *decompose-a-two-form* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: an antisymmetric two-form splits relative to an observer into a magnetic (space-space) and an electric (time-space) part, and here the magnetic part is the familiar cross product.

**Assumption pattern.** The two-form is $\overrightarrow{CM}^\flat\wedge p$, and the observer supplies the splitting $E_{u_0}\oplus\mathbb{R}U_0$. The signpost is "split into the vectors the observer measures": operation 2 of the topic page, executed by decomposing $\overrightarrow{CM}$ and $p$ into time and space parts.

**Theorem routing.** Part 1 computes the space-space block by evaluating the wedge on rest-space vectors. Part 2 computes the time-space block by evaluating on $U_0$ and a rest-space vector. Part 4 inverts the relation using the [[Def - The Levi-Civita Tensor|Levi-Civita]] contraction.

**Key decision point.** The crux is recognising that the space-space components $X^ip^j - X^jp^i$ are *exactly* the components of the cross product $\vec X\times\mathbf{p}$ written as an antisymmetric matrix — the three-dimensional accident that lets a plane be relabelled as an axis — while the time-space components $EX^i - hp^i$ are a genuinely new object with no three-dimensional disguise.

---

# Legal Operations Used

1. **Operation 2 from the topic page (split a two-form into observer-relative vectors).** The entire exercise is this decomposition, extracting the angular momentum vector and the mass-energy dipole.

2. **Operation 1 from the topic page (build angular momentum and read its tensor components).** Parts 1–2 read off the components of $\overrightarrow{CM}^\flat\wedge p$ in the observer's frame.

---

# Hints

> [!note]- Hint 1
> Evaluate $J_C(\vec e_i, \vec e_j)$ for two rest-space basis vectors. By the wedge formula, $J_C(\vec e_i,\vec e_j) = (\overrightarrow{CM}\cdot\vec e_i)(p\cdot\vec e_j) - (p\cdot\vec e_i)(\overrightarrow{CM}\cdot\vec e_j)$. In the rest space the inner products pick out the spatial components $X^i$ and $p^j$ (with appropriate signs from the metric), giving $J_{ij} = X_ip_j - X_jp_i$.

> [!note]- Hint 2
> For the time-space block, evaluate $J_C(\vec e_0, \vec e_i) = J_C(U_0, \vec e_i)$. This picks out the energy $E = p\cdot U_0$ and $h = \overrightarrow{CM}\cdot U_0$ (the time-components), giving $J_{0i} = EX^i - hp^i$ (up to signs).

> [!note]- Hint 3
> The space-space block $J_{ij} = X_ip_j - X_jp_i$ is antisymmetric in $i,j$, so it has three independent components in three dimensions — exactly the three components of $\vec X\times\mathbf{p}$. The time-space block has no three-dimensional analogue because there is no "time direction" in Newtonian space; it appears only because relativity has a fourth dimension.

> [!note]- Hint 4
> The inverse of "antisymmetric matrix to axial vector" is $\sigma^i = \tfrac12\epsilon^{ijk}J_{jk}$. Plug in $J_{jk} = X_jp_k - X_kp_j$ and use $\epsilon^{ijk}\epsilon_{jk\ell}$ identities (or just expand) to recover $\sigma^i = (\vec X\times\mathbf{p})^i$.

---

# Solution

The exercise decomposes the angular momentum two-form into the two three-vectors an observer measures. Part 1 extracts the angular momentum vector as a cross product from the space-space block; part 2 extracts the mass-energy dipole from the time-space block and assembles the full matrix; part 3 interprets the split; part 4 inverts to recover the vector.

**Step 1: The space-space block is the cross product.**

> [!note]- Derivation
> Work in the observer's orthonormal frame $(\vec e_\alpha)$ with $\vec e_0 = U_0$, $\vec e_i\in E_{u_0}$, and $\eta_{\alpha\beta} = \mathrm{diag}(1,-1,-1,-1)$. Evaluate the two-form on two spatial basis vectors:
> $$J_{ij} = J_C(\vec e_i,\vec e_j) = (\overrightarrow{CM}\cdot\vec e_i)(p\cdot\vec e_j) - (p\cdot\vec e_i)(\overrightarrow{CM}\cdot\vec e_j).$$
> Since $\vec e_i\in E_{u_0}$ with $\vec e_i\cdot\vec e_j = -\delta_{ij}$, the inner products give $\overrightarrow{CM}\cdot\vec e_i = -X^i$ and $p\cdot\vec e_j = -p^j$ (the spatial components, with the metric sign). So
> $$J_{ij} = (-X^i)(-p^j) - (-p^i)(-X^j) = X^ip^j - X^jp^i.$$
> This is antisymmetric in $i,j$, hence has three independent components, and they are exactly the components of the cross product $\vec X\times\mathbf{p}$:
> $$\sigma_C^1 = J_{23} = X^2p^3 - X^3p^2,\quad \sigma_C^2 = J_{31} = X^3p^1 - X^1p^3,\quad \sigma_C^3 = J_{12} = X^1p^2 - X^2p^1.$$
> Since $\vec X = \overrightarrow{CM} - hU_0$ and $U_0$ contributes nothing to a rest-space cross product, $\vec\sigma_C = \vec X\times\mathbf{p} = \overrightarrow{CM}\times\mathbf{p}$. The angular momentum vector is the rest-space cross product of the displacement with the spatial momentum — the relativistic $\mathbf{r}\times\mathbf{p}$.

**Step 2: The time-space block is the mass-energy dipole.**

> [!note]- Derivation
> Evaluate the two-form on $U_0 = \vec e_0$ and a spatial $\vec e_i$:
> $$J_{0i} = J_C(U_0,\vec e_i) = (\overrightarrow{CM}\cdot U_0)(p\cdot\vec e_i) - (p\cdot U_0)(\overrightarrow{CM}\cdot\vec e_i).$$
> With $\overrightarrow{CM}\cdot U_0 = h$, $p\cdot U_0 = E$, $p\cdot\vec e_i = -p^i$, $\overrightarrow{CM}\cdot\vec e_i = -X^i$,
> $$J_{0i} = h(-p^i) - E(-X^i) = EX^i - hp^i.$$
> This is the time-space block — the **mass-energy dipole moment** contribution. The full matrix in the observer's frame is
> $$(J_{\alpha\beta}) = \begin{pmatrix} 0 & EX^1 - hp^1 & EX^2 - hp^2 & EX^3 - hp^3\\ -(EX^1 - hp^1) & 0 & \sigma_C^3 & -\sigma_C^2\\ -(EX^2 - hp^2) & -\sigma_C^3 & 0 & \sigma_C^1\\ -(EX^3 - hp^3) & \sigma_C^2 & -\sigma_C^1 & 0\end{pmatrix},$$
> with the angular momentum vector in the space-space block (magnetic) and the mass-energy dipole in the time-space block (electric) — the same layout as the electromagnetic field tensor $F_{\mu\nu}$.

**Step 3: Relativistic upgrade of $\mathbf{r}\times\mathbf{p}$.**

> [!note]- Derivation
> In Newtonian mechanics angular momentum is $\mathbf{L} = \mathbf{r}\times\mathbf{p}$, three components. Here the space-space block $\sigma_C^i = (\vec X\times\mathbf{p})^i$ reproduces this exactly — the three planes of rotation $xy, yz, zx$ relabelled as three axes, the three-dimensional accident $\binom 32 = 3$. The *new* content is the time-space block $EX^i - hp^i$, the mass-energy dipole, which has no Newtonian analogue because Newtonian space has no fourth (time) direction to pair with the spatial ones. Physically, the mass-energy dipole $\vec D \propto \sum E_a\vec X_a$ measures how the energy is distributed in space — the "first moment of energy" — and its evolution governs the motion of the centre of inertia (recall $d\vec D/dt = \mathbf{P}$). The full antisymmetric tensor has $\binom 42 = 6$ components: three are the old angular momentum vector, three are the new mass-energy dipole, and a boost rotates one set into the other.

**Step 4: Recovering the vector from the tensor.**

> [!note]- Derivation
> The axial-vector-from-antisymmetric-matrix formula is $\sigma_C^i = \tfrac12\epsilon^{ijk}J_{jk}$. Substituting $J_{jk} = X^jp^k - X^kp^j$ (raising indices in the rest space introduces no sign issue for the contraction with $\epsilon$),
> $$\sigma_C^i = \tfrac12\epsilon^{ijk}(X^jp^k - X^kp^j) = \tfrac12(\epsilon^{ijk}X^jp^k - \epsilon^{ijk}X^kp^j).$$
> Relabel $j\leftrightarrow k$ in the second term: $\epsilon^{ijk}X^kp^j = \epsilon^{ikj}X^jp^k = -\epsilon^{ijk}X^jp^k$. So
> $$\sigma_C^i = \tfrac12(\epsilon^{ijk}X^jp^k + \epsilon^{ijk}X^jp^k) = \epsilon^{ijk}X^jp^k = (\vec X\times\mathbf{p})^i,$$
> agreeing with part 1. The contraction with $\tfrac12\epsilon$ is the precise inverse of writing the cross product as an antisymmetric matrix. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** Evaluating $J_C = \overrightarrow{CM}^\flat\wedge p$ on rest-space basis vectors gives $J_{ij} = X^ip^j - X^jp^i$, the components of $\vec\sigma_C = \vec X\times\mathbf{p} = \overrightarrow{CM}\times\mathbf{p}$.
>
> **Part 2.** Evaluating on $U_0$ and $\vec e_i$ gives $J_{0i} = EX^i - hp^i$, the mass-energy dipole block; the full matrix has the dipole in the time-space block and the angular momentum vector in the space-space block, like $F_{\mu\nu}$.
>
> **Part 3.** The space-space block is the Newtonian $\mathbf{r}\times\mathbf{p}$ (three planes as three axes); the time-space block $EX^i - hp^i$ is the new mass-energy dipole, the first moment of energy, with no Newtonian analogue, governing the centre-of-inertia motion.
>
> **Part 4.** $\sigma_C^i = \tfrac12\epsilon^{ijk}J_{jk} = \epsilon^{ijk}X^jp^k = (\vec X\times\mathbf{p})^i$, agreeing with part 1. $\blacksquare$

---

# Key Takeaways

**The cross product is the space-space block of an antisymmetric tensor — that is all it ever was.** The exercise makes precise the claim that the Newtonian angular momentum vector is a three-dimensional disguise. The honest object is the antisymmetric tensor $J_{\alpha\beta}$, and its space-space part $J_{ij} = X^ip^j - X^jp^i$ is antisymmetric in $i,j$, hence has three independent components in three dimensions — which is why it *can* be repackaged as a vector $\vec X\times\mathbf{p}$. The repackaging is the formula $\sigma^i = \tfrac12\epsilon^{ijk}J_{jk}$, available only because $\binom 32 = 3$. The reusable insight is that "the cross product" and "the antisymmetric part of a tensor" are the same thing in three dimensions, and the cross-product notation is a convenience that fails in four dimensions, where the antisymmetric tensor has six components and no vector disguise. When you see a cross product, see the antisymmetric tensor behind it.

**The time-space block is the new physics — energy distribution, not rotation.** The genuinely relativistic content of the angular momentum tensor is the time-space block $EX^i - hp^i$, the mass-energy dipole moment. This has no Newtonian shadow because it pairs a spatial index with the time direction, which Newtonian space lacks. The transferable lesson is that lifting a three-dimensional object to a four-dimensional tensor *always* produces new time-space components, and those components carry physics invisible in the non-relativistic theory — here, how energy is distributed in space and how the centre of inertia moves. The same pattern appears when the three-dimensional rotation generators $J_i$ are joined by the boost generators $K_i$ to fill out the Lorentz algebra, and when the three magnetic-field components are joined by the three electric-field components to fill out $F_{\mu\nu}$. The "extra" components are not bookkeeping; they are the relativistic content.

**A boost mixes the two blocks — angular momentum and mass-energy dipole are one object.** Because the angular momentum vector and the mass-energy dipole are the magnetic and electric blocks of the same antisymmetric tensor, a boost rotates them into each other exactly as it mixes $\mathbf{B}$ and $\mathbf{E}$. The diagnostic to carry forward is that any time you decompose a relativistic two-form into observer-relative three-vectors, those three-vectors are *frame-dependent shadows* of a single frame-independent object, and a change of observer redistributes the object between them. A particle with pure angular momentum and no dipole in one frame has both in another. This is why the right way to think about angular momentum relativistically is not "a vector plus a correction" but "an antisymmetric tensor whose two halves the observer sees as a vector and a dipole" — the unifying frame of the whole chapter.
