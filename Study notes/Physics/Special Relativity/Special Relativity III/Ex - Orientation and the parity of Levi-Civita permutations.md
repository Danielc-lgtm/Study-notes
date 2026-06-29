---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Spacetime Orientation"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\epsilon$ be the [[Def - Spacetime Orientation|Levi-Civita tensor]] on Minkowski space, normalised so that $\epsilon(e_0, e_1, e_2, e_3) = +1$ on a right-handed orthonormal basis.

1. Compute $\epsilon(e_1, e_2, e_3, e_0)$ — the value on the cyclically-shifted basis — and confirm Gourgoulhon's warning (Remark 1.14) that in four dimensions a cyclic permutation is **odd**, so this equals $-1$, not $+1$.
2. Show that the antisymmetric four-linear forms on a four-dimensional space form a **one-dimensional** space, and deduce that orientation is a binary choice (two forms, opposite in sign, satisfy the $\pm 1$-on-orthonormal-bases normalisation).
3. Show that a spatial reflection $P : (e_0,e_1,e_2,e_3) \mapsto (e_0,-e_1,e_2,e_3)$ reverses the orientation ($\det P = -1$), while a boost preserves it ($\det = +1$), and hence that $P$ lies outside the proper orthochronous group $SO^+(1,3)$.

**Recall:**

![[Def - Spacetime Orientation#The Definition]]

The [[Def - Spacetime Orientation|Levi-Civita tensor]] $\epsilon$ is an antisymmetric four-linear form with $\epsilon(\text{orthonormal basis}) = \pm 1$; it returns the determinant of four vectors with respect to a right-handed orthonormal basis. For a permutation $\sigma$, $\epsilon(X_{\sigma(1)},\ldots,X_{\sigma(4)}) = (-1)^{k(\sigma)}\epsilon(X_1,\ldots,X_4)$ with $k(\sigma)$ the number of transpositions.

---

# Convergent Strategy

**Problem class.** A *structural / orientation* problem — verify the parity behaviour of the volume form and the reduction of the structure group. The [[Special Relativity III — Minkowski Spacetime and the Metric#Legal Operations|topic legal operations]] flag the four-dimensional cyclic-permutation trap (operation 9) as a recurring pitfall.

**Assumption pattern.** The normalisation $\epsilon(e_0,e_1,e_2,e_3) = +1$ and the antisymmetry of $\epsilon$. The recognition step is that $\epsilon$ behaves like a determinant, so permutations of its arguments contribute the sign of the permutation, and a 4-cycle is odd.

**Theorem routing.** Part 1 decomposes the 4-cycle into transpositions and counts parity. Part 2 invokes the one-dimensionality of $A_4(E)$ ([[Def - Spacetime Orientation|the dimension count]]) and the $\pm 1$ normalisation. Part 3 computes determinants of the reflection and boost matrices and connects $\det = -1$ to exclusion from $SO^+(1,3)$.

**Key decision point.** The crux is that a *cyclic* permutation of four objects is **odd** — unlike the three-dimensional intuition where cyclic permutations of the triple product are even. The natural error is to carry over $\varepsilon_{ijk}$'s cyclic-invariance; in four dimensions a 4-cycle is three transpositions, hence odd, flipping the sign.

---

# Legal Operations Used

1. **Operation 9 (use the orientation / Levi-Civita tensor):** the entire exercise manipulates $\epsilon$ and its determinant interpretation.

2. **Operation 2 (compute the scalar product by the Minkowski matrix):** implicit in identifying orthonormal bases and computing the boost/reflection determinants.

3. **Operation 3 / the structure-group reduction:** part 3 connects $\det$ to membership in $SO^+(1,3)$.

---

# Hints

> [!note]- Hint 1
> The cyclic shift $(0123) \mapsto (1230)$ sends position-1 to $e_1$, etc. To sort $(1,2,3,0)$ back to $(0,1,2,3)$, count adjacent swaps, or note that the 4-cycle $(0\,1\,2\,3)$ equals the product of three transpositions $(0\,1)(1\,2)(2\,3)$ — wait, count carefully: a $k$-cycle is a product of $k-1$ transpositions, so a 4-cycle is $3$ transpositions, odd.

> [!note]- Hint 2
> $\epsilon(e_1,e_2,e_3,e_0) = (-1)^3\epsilon(e_0,e_1,e_2,e_3) = -1$. (Three transpositions: move $e_0$ from the last slot to the first, swapping it past $e_3$, then $e_2$, then $e_1$ — three swaps.) The three-dimensional reflex "cyclic permutations preserve the triple product" is *wrong* in four dimensions.

> [!note]- Hint 3
> An antisymmetric four-linear form on $E$ (dimension 4) is determined by its single value on a fixed basis, because antisymmetry and multilinearity fix it everywhere else. So $A_4(E)$ is one-dimensional. Two forms with $|A(\text{basis})| = 1$ exist, differing by sign — the two orientations.

> [!note]- Hint 4
> For part 3: the reflection $P = \mathrm{diag}(1,-1,1,1)$ has $\det P = -1$, so $\epsilon(Pe_0, Pe_1, Pe_2, Pe_3) = \det(P)\,\epsilon(e_0,\ldots) = -1$: orientation reversed. A boost is a continuous deformation of the identity with $\det = +1$, so it preserves $\epsilon$. Since $SO^+(1,3)$ is the $\det = +1$, orthochronous component, $P$ (with $\det = -1$) is not in it.

---

# Solution

The Levi-Civita tensor behaves like a determinant; a 4-cycle is odd; orientation is binary because $A_4(E)$ is one-dimensional; and $\det = \pm 1$ separates orientation-preserving from -reversing maps. Step 1 computes the cyclic value; Step 2 establishes one-dimensionality and the binary choice; Step 3 separates reflection from boost.

**Step 1: a cyclic permutation is odd, so $\epsilon(e_1,e_2,e_3,e_0) = -1$.**

> [!note]- Derivation
> The arguments $(e_1,e_2,e_3,e_0)$ are the cyclic shift of $(e_0,e_1,e_2,e_3)$. To express the cyclic shift as transpositions, note that the 4-cycle $\sigma = (0\,1\,2\,3)$ (sending $0\to1\to2\to3\to0$) decomposes as a product of three transpositions — a $k$-cycle is always $k-1$ transpositions. Concretely, to bring $(e_1,e_2,e_3,e_0)$ back to standard order $(e_0,e_1,e_2,e_3)$, slide $e_0$ leftward past $e_3, e_2, e_1$: three adjacent swaps. Hence $k(\sigma) = 3$ is odd, and
> $$\epsilon(e_1, e_2, e_3, e_0) = (-1)^{k(\sigma)}\epsilon(e_0,e_1,e_2,e_3) = (-1)^3 (+1) = -1.$$
> This confirms [[Def - Spacetime Orientation|Gourgoulhon's Remark 1.14]]: in dimension four a cyclic permutation is **odd**, not even. The three-dimensional reflex — that cyclic permutations of the scalar triple product $\varepsilon_{ijk}$ preserve its sign (because a 3-cycle is two transpositions, even) — does *not* carry over, because parity depends on the dimension: a 4-cycle is three transpositions.

**Step 2: $A_4(E)$ is one-dimensional, so orientation is binary.**

> [!note]- Derivation
> An antisymmetric four-linear form $A$ on the four-dimensional $E$ is determined by its value on a single ordered basis $(e_0,e_1,e_2,e_3)$. Indeed, for any four vectors $X_j = X_j^{\alpha_j}e_{\alpha_j}$, multilinearity gives $A(X_0,X_1,X_2,X_3) = X_0^{\alpha_0}\cdots X_3^{\alpha_3}A(e_{\alpha_0},\ldots,e_{\alpha_3})$, and antisymmetry forces $A(e_{\alpha_0},\ldots,e_{\alpha_3})$ to vanish unless $(\alpha_0,\ldots,\alpha_3)$ is a permutation of $(0,1,2,3)$, in which case it equals $(-1)^{k}A(e_0,\ldots,e_3)$. So $A$ is the single number $A(e_0,\ldots,e_3)$ times the determinant function — the space $A_4(E)$ is **one-dimensional**. The metric normalisation $|A(\text{orthonormal basis})| = 1$ then picks out exactly *two* forms (the value $+1$ or $-1$ on a fixed right-handed orthonormal basis), opposite in sign. Choosing one is the **orientation**: a binary choice, as claimed. (Any positive multiple would orient equally; the metric pins the scale to $\pm 1$, giving the volume form as well.)

**Step 3: reflection reverses orientation, boost preserves it.**

> [!note]- Derivation
> A **spatial reflection** $P$ acts as $P : (e_0,e_1,e_2,e_3) \mapsto (e_0,-e_1,e_2,e_3)$, with matrix $\mathrm{diag}(1,-1,1,1)$ and $\det P = -1$. Since $\epsilon$ is the determinant relative to a right-handed orthonormal basis,
> $$\epsilon(Pe_0, Pe_1, Pe_2, Pe_3) = \det(P)\,\epsilon(e_0,e_1,e_2,e_3) = (-1)(+1) = -1,$$
> so $P$ maps a right-handed basis to a left-handed one: it **reverses** the orientation. (It also preserves $\eta$, being a reflection of one spacelike axis, so $P \in O(1,3)$.) A **boost** $\Lambda[v]$, by contrast, is connected to the identity by the continuous family $\Lambda[\lambda v]$, $\lambda \in [0,1]$, along which $\det$ is continuous and integer-valued, hence constant at $\det = +1$; so $\epsilon(\Lambda e_0,\ldots,\Lambda e_3) = +1$ and a boost **preserves** the orientation. The proper orthochronous Lorentz group $SO^+(1,3)$ is exactly the identity component — the transformations with $\det = +1$ and $\Lambda^0{}_0 > 0$ — so it contains every boost and rotation but *not* the reflection $P$ (which has $\det = -1$). The orientation is the structure whose stabiliser excludes $P$: choosing $\epsilon$ reduces the structure group from $O(1,3)$ to the orientation-preserving $SO(1,3)$, and adding the time arrow reduces it further to $SO^+(1,3)$.

> [!note]- Complete formal solution
> *Part 1.* The cyclic shift is a 4-cycle, a product of three transpositions, hence odd: $\epsilon(e_1,e_2,e_3,e_0) = (-1)^3\epsilon(e_0,e_1,e_2,e_3) = -1$, confirming Remark 1.14 (a 4-cycle is odd, unlike a 3-cycle). *Part 2.* An antisymmetric four-linear form on a four-dimensional space is fixed by its value on one ordered basis (multilinearity + antisymmetry), so $A_4(E)$ is one-dimensional; the $\pm 1$ normalisation selects two opposite forms, and orientation is the binary choice between them. *Part 3.* The reflection $P = \mathrm{diag}(1,-1,1,1)$ has $\det P = -1$, so $\epsilon(Pe_\alpha) = -\epsilon(e_\alpha)$: orientation reversed, $P \in O(1,3)\setminus SO^+(1,3)$. A boost is connected to the identity with $\det = +1$, preserving $\epsilon$; thus $SO^+(1,3)$ (det $+1$, orthochronous) contains boosts and rotations but not $P$. $\blacksquare$

---

# Key Takeaways

**In four dimensions a cyclic permutation is odd, and carrying over three-dimensional triple-product intuition is the trap.** The headline computation is that $\epsilon(e_1,e_2,e_3,e_0) = -1$, not $+1$: a 4-cycle is a product of three transpositions, hence odd, so it flips the sign of the Levi-Civita tensor. This contradicts the ingrained three-dimensional reflex that "cyclic permutations preserve the scalar triple product" — true there because a 3-cycle is two transpositions (even), false in four dimensions. The trigger to be careful: any manipulation of $\epsilon_{\alpha\beta\gamma\delta}$ that reorders indices cyclically. The reusable rule is that the sign is always $(-1)^{k(\sigma)}$ with $k(\sigma)$ the transposition count, and that a $k$-cycle contributes $(-1)^{k-1}$ — so cyclic invariance holds in odd dimensions and fails in even ones. This is the kind of dimension-dependent sign that silently corrupts Hodge-star and four-volume computations if assumed away.

**Orientation is a binary choice because the top antisymmetric forms are one-dimensional, and the metric upgrades it to a volume form.** The structural fact is that $A_4(E)$ (equivalently $\Lambda^4 E^*$) is one-dimensional for a four-dimensional space, so all antisymmetric four-linear forms are proportional — there is essentially one determinant, up to scale. Orientation needs only a *ray* (a positive scaling class); the metric does more, pinning the scale to $\pm 1$ on orthonormal bases and thereby selecting two specific forms, the two orientations, and simultaneously a *volume element*. The reusable view: whenever you need volumes or a Hodge star, the relevant object is the metric-normalised $\epsilon$, which carries both a sign (orientation) and a scale (volume); a bare orientation is the weaker datum of just the sign. This one-dimensionality is what makes "right-handed versus left-handed" a coherent binary distinction in any dimension.

**$\det = \pm 1$ separates orientation-preserving from -reversing maps, and this is the reduction $O(1,3) \to SO^+(1,3)$.** The payoff is that choosing an orientation reduces the structure group: maps with $\det = +1$ preserve $\epsilon$ (these are $SO(1,3)$, including all boosts and rotations, which are connected to the identity), while a reflection with $\det = -1$ reverses it and is excluded. Adding the time arrow excludes time-reversal too, leaving the identity component $SO^+(1,3)$ — the physically relevant group. The transferable lesson: orientation-preservation is exactly the condition $\det \Lambda = +1$, and parity ($P$) and time-reversal ($T$) are precisely the discrete transformations that take you out of the identity component. This is why $SO^+(1,3)$, not the full $O(1,3)$, is the symmetry group of oriented, time-oriented Minkowski space, and why the discrete symmetries $P$ and $T$ must be discussed separately from the continuous boosts and rotations.
