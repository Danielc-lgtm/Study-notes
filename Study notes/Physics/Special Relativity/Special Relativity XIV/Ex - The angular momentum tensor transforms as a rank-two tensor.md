---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Angular Momentum Four-Tensor"
  - "Def - The Lorentz Group"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

The [[Def - Angular Momentum Four-Tensor|angular momentum tensor]] of a particle about the origin is $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$, built from the position four-vector $x^\alpha$ and the four-momentum $p^\alpha$. Working with $c = 1$ and the mostly-minus signature:

1. Show that under a Lorentz transformation $\Lambda$ (with $x'^\alpha = \Lambda^\alpha{}_\mu x^\mu$ and $p'^\alpha = \Lambda^\alpha{}_\mu p^\mu$), the components transform as a rank-two contravariant tensor, $J'^{\alpha\beta} = \Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu J^{\mu\nu}$.
2. A particle has $x^\alpha = (0, L, 0, 0)$ and $p^\alpha = (E, 0, p, 0)$ in frame $S$, so $J^{12} = -J^{21} = -Lp$ is its only nonzero space-space component (the $z$-angular momentum $L_z = -Lp$... careful with signs). Compute *all* components $J^{\alpha\beta}$ in $S$.
3. Boost to a frame $S'$ moving at velocity $v$ along the $x$-axis. Compute $J'^{02}$ and $J'^{12}$, and verify that the angular momentum vector component (space-space) and the mass-energy dipole component (time-space) mix exactly as the magnetic and electric field components of the electromagnetic tensor would under the same boost.
4. Verify that the two Lorentz scalars $J_{\alpha\beta}J^{\alpha\beta}$ and $\epsilon_{\alpha\beta\gamma\delta}J^{\alpha\beta}J^{\gamma\delta}$ are unchanged by the boost.

**Recall:**

![[Def - Angular Momentum Four-Tensor#The Definition]]

A [[Def - The Lorentz Group|Lorentz transformation]] $\Lambda$ satisfies $\Lambda^{\mathsf T}\eta\Lambda = \eta$; a contravariant tensor of rank two transforms by one factor of $\Lambda$ per index. A boost along $x$ at velocity $v$ has $\Lambda^0{}_0 = \Lambda^1{}_1 = \gamma$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \gamma v$, and acts as the identity on the $y, z$ directions, where $\gamma = (1-v^2)^{-1/2}$.

---

# Convergent Strategy

**Problem class.** A *verify-tensor-character* and *compute-the-transform* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: a quantity built from four-vectors by antisymmetrisation transforms as a tensor automatically, and its observer-relative pieces (here the angular momentum vector and the mass-energy dipole) mix under a boost exactly as the electric and magnetic fields do.

**Assumption pattern.** The object is $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$, manifestly bilinear in two four-vectors. The signpost is "built from $x$ and $p$ by antisymmetrisation": this is precisely operation 1 of the topic page, and tensor character follows from the transformation of $x$ and $p$ alone.

**Theorem routing.** Part 1 uses only that $x$ and $p$ are four-vectors and the antisymmetrised product of two tensors is a tensor. Parts 2–3 apply the boost matrix to the explicit components, routing through the [[Def - The Lorentz Group|Lorentz transformation]]. Part 4 uses that any full contraction of tensors is a Lorentz scalar.

**Key decision point.** The crux of part 3 is recognising that the *same* boost mixes the space-space block (angular momentum vector) with the time-space block (mass-energy dipole), and that the mixing formula is identical to the $\mathbf{E}$–$\mathbf{B}$ mixing of the field tensor — because both $J^{\alpha\beta}$ and $F^{\alpha\beta}$ are antisymmetric rank-two tensors, so they transform identically.

---

# Legal Operations Used

1. **Operation 1 from the topic page (build angular momentum as $\overrightarrow{CM}^\flat\wedge p$, read its tensor components).** The whole exercise rests on the fact that $J^{\alpha\beta}$ is the antisymmetrised product of two four-vectors, so its transformation law is forced by theirs.

2. **Operation 2 from the topic page (split a two-form into observer-relative vectors).** Parts 2–3 identify the space-space block as the angular momentum vector and the time-space block as the mass-energy dipole, and track how the boost mixes them.

---

# Hints

> [!note]- Hint 1
> A tensor is *defined* by its transformation law. Since $x^\alpha$ and $p^\alpha$ each transform with one factor of $\Lambda$, the product $x^\alpha p^\beta$ transforms with two, and antisymmetrising does not change the transformation law. Write out $J'^{\alpha\beta} = x'^\alpha p'^\beta - x'^\beta p'^\alpha$ and substitute.

> [!note]- Hint 2
> For part 2, the only nonzero components of $x = (0,L,0,0)$ and $p = (E,0,p,0)$ are $x^1 = L$, $p^0 = E$, $p^2 = p$. So the nonzero $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$ are those with one index picking out $x^1$ and the other picking out $p^0$ or $p^2$: namely $J^{10}$, $J^{12}$ (and their antisymmetric partners).

> [!note]- Hint 3
> For part 3, the boost along $x$ acts on the indices $0,1$ and leaves $2,3$ fixed. So $J'^{02} = \Lambda^0{}_\mu\Lambda^2{}_\nu J^{\mu\nu} = \Lambda^0{}_0 J^{02} + \Lambda^0{}_1 J^{12}$ (since $\Lambda^2{}_\nu = \delta^2{}_\nu$). Compute $J^{02}$ and $J^{12}$ from part 2, then apply.

> [!note]- Hint 4
> For part 4, you do not need to recompute the scalars in $S'$ from scratch — a full contraction of a tensor with itself (or with $\epsilon$) is *automatically* a Lorentz scalar, by the same argument as part 1. But computing both sides explicitly is a good check: $J_{\alpha\beta}J^{\alpha\beta}$ should come out the same number in $S$ and $S'$.

---

# Solution

The exercise is three computations wrapped around one principle: $J^{\alpha\beta}$ is the antisymmetrised product of two four-vectors, so it transforms as a rank-two tensor, its blocks mix under a boost exactly like the field tensor's, and its full contractions are invariant. Part 1 establishes the transformation law abstractly; parts 2–3 verify it on explicit components and exhibit the $\mathbf{E}$–$\mathbf{B}$-style mixing; part 4 confirms the invariants.

**Step 1: The transformation law follows from antisymmetrising a product of four-vectors.**

> [!note]- Derivation
> Under $\Lambda$, the position and momentum transform as four-vectors: $x'^\alpha = \Lambda^\alpha{}_\mu x^\mu$ and $p'^\beta = \Lambda^\beta{}_\nu p^\nu$. Then
> $$J'^{\alpha\beta} = x'^\alpha p'^\beta - x'^\beta p'^\alpha = \Lambda^\alpha{}_\mu x^\mu\,\Lambda^\beta{}_\nu p^\nu - \Lambda^\beta{}_\nu x^\nu\,\Lambda^\alpha{}_\mu p^\mu.$$
> Relabelling the dummy index in the second term ($\mu\leftrightarrow\nu$ is not needed; just factor) ,
> $$J'^{\alpha\beta} = \Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu\big(x^\mu p^\nu - x^\nu p^\mu\big) = \Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu J^{\mu\nu}.$$
> This is exactly the transformation law of a rank-two contravariant tensor: one factor of $\Lambda$ per index. The antisymmetry is preserved, $J'^{\alpha\beta} = -J'^{\beta\alpha}$, so the tensor character and the antisymmetry both survive. No property of the Lorentz group beyond linearity was used — the result holds for any linear coordinate change.

**Step 2: The components in $S$.**

> [!note]- Derivation
> With $x = (0,L,0,0)$ and $p = (E,0,p,0)$, the nonzero entries are $x^1 = L$, $p^0 = E$, $p^2 = p$. Computing $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$:
> $$J^{10} = x^1 p^0 - x^0 p^1 = LE - 0 = LE, \qquad J^{01} = -LE,$$
> $$J^{12} = x^1 p^2 - x^2 p^1 = Lp - 0 = Lp, \qquad J^{21} = -Lp,$$
> and all other components vanish (any component not involving index $1$ has $x^\alpha = 0$ for $\alpha\ne 1$). So the matrix is
> $$(J^{\alpha\beta}) = \begin{pmatrix} 0 & -LE & 0 & 0\\ LE & 0 & Lp & 0\\ 0 & -Lp & 0 & 0\\ 0 & 0 & 0 & 0\end{pmatrix}.$$
> The space-space entry $J^{12} = Lp$ is the angular momentum vector component (here $\sigma^3 = -J^{12}$ up to the sign convention $\sigma^k = \tfrac12\epsilon^{kij}J_{ij}$; the magnitude is $Lp$, the moment of the momentum $p$ at lever arm $L$). The time-space entry $J^{10} = LE$ is the mass-energy dipole component.

**Step 3: The boost mixes the blocks like the field tensor.**

> [!note]- Derivation
> Boost along $x$ at velocity $v$: $\Lambda^0{}_0 = \Lambda^1{}_1 = \gamma$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \gamma v$, $\Lambda^2{}_2 = \Lambda^3{}_3 = 1$. Compute the two components of interest.
>
> For $J'^{02}$: only $\Lambda^0{}_0$ and $\Lambda^0{}_1$ are nonzero in the first index, and $\Lambda^2{}_2 = 1$ in the second, so
> $$J'^{02} = \Lambda^0{}_0\Lambda^2{}_2 J^{02} + \Lambda^0{}_1\Lambda^2{}_2 J^{12} = \gamma\cdot 0 + \gamma v\cdot Lp = \gamma v\,Lp.$$
> For $J'^{12}$:
> $$J'^{12} = \Lambda^1{}_0\Lambda^2{}_2 J^{02} + \Lambda^1{}_1\Lambda^2{}_2 J^{12} = \gamma v\cdot 0 + \gamma\cdot Lp = \gamma\,Lp.$$
> So the boost mixes the time-space component $J^{02}$ (mass-energy dipole, the "electric" part) and the space-space component $J^{12}$ (angular momentum vector, the "magnetic" part) by
> $$J'^{02} = \gamma(J^{02} + v J^{12}),\qquad J'^{12} = \gamma(J^{12} + v J^{02}).$$
> This is *identical* to the transformation of the electromagnetic field components $E_y = F^{02}$ and $B_z = F^{12}$ (in suitable conventions): $E'_y = \gamma(E_y + vB_z)$, $B'_z = \gamma(B_z + vE_y)$. The reason is structural — $J^{\alpha\beta}$ and $F^{\alpha\beta}$ are both antisymmetric rank-two tensors, so they transform by the identical rule, and the dictionary $\vec D\leftrightarrow\mathbf{E}$, $\vec\sigma\leftrightarrow\mathbf{B}$ is exact. A particle that has pure angular momentum (no dipole) in $S$ acquires a mass-energy dipole in $S'$, just as a pure magnetic field acquires an electric field under a boost.

**Step 4: The invariants are unchanged.**

> [!note]- Derivation
> By the same argument as Step 1, any *full* contraction of tensors is a Lorentz scalar: $J'_{\alpha\beta}J'^{\alpha\beta} = \Lambda_\alpha{}^\rho\Lambda_\beta{}^\sigma\Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu J_{\rho\sigma}J^{\mu\nu} = \delta^\rho_\mu\delta^\sigma_\nu J_{\rho\sigma}J^{\mu\nu} = J_{\mu\nu}J^{\mu\nu}$, using $\Lambda_\alpha{}^\rho\Lambda^\alpha{}_\mu = \delta^\rho_\mu$. So $J_{\alpha\beta}J^{\alpha\beta}$ is invariant; explicitly, $J_{\alpha\beta}J^{\alpha\beta} = 2(\sigma^2 - D^2) = 2((Lp)^2 - (LE)^2)$ in $S$, and the same number in $S'$ (one can check $J'_{\alpha\beta}J'^{\alpha\beta}$ directly using the boosted components). Likewise $\epsilon_{\alpha\beta\gamma\delta}J^{\alpha\beta}J^{\gamma\delta} \propto \vec\sigma\cdot\vec D$ is invariant. These are the two Lorentz scalars of the angular momentum, the mechanical analogues of $F_{\mu\nu}F^{\mu\nu}\propto B^2 - E^2$ and $\epsilon F F\propto\mathbf{E}\cdot\mathbf{B}$.

> [!note]- Complete formal solution
> **Part 1.** Since $x'^\alpha = \Lambda^\alpha{}_\mu x^\mu$ and $p'^\beta = \Lambda^\beta{}_\nu p^\nu$, $J'^{\alpha\beta} = x'^\alpha p'^\beta - x'^\beta p'^\alpha = \Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu(x^\mu p^\nu - x^\nu p^\mu) = \Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu J^{\mu\nu}$ — the rank-two contravariant tensor law.
>
> **Part 2.** With $x^1 = L$, $p^0 = E$, $p^2 = p$ the only nonzero data, $J^{10} = LE$, $J^{12} = Lp$ (and antisymmetric partners); all else zero.
>
> **Part 3.** The boost along $x$ gives $J'^{02} = \gamma v\,Lp$ and $J'^{12} = \gamma Lp$, i.e. $J'^{02} = \gamma(J^{02} + vJ^{12})$ and $J'^{12} = \gamma(J^{12} + vJ^{02})$ — identical to the mixing of $E_y$ and $B_z$ under the same boost. The mass-energy dipole and angular momentum vector mix exactly as $\mathbf{E}$ and $\mathbf{B}$, because $J^{\alpha\beta}$ and $F^{\alpha\beta}$ are both antisymmetric rank-two tensors.
>
> **Part 4.** Full contractions are scalars: $J_{\alpha\beta}J^{\alpha\beta} = J'_{\alpha\beta}J'^{\alpha\beta} = 2((Lp)^2 - (LE)^2)$, and $\epsilon_{\alpha\beta\gamma\delta}J^{\alpha\beta}J^{\gamma\delta}$ is likewise invariant. These are the two Lorentz scalars of the angular momentum. $\blacksquare$

---

# Key Takeaways

**Tensor character is free once you build from four-vectors.** The single most reusable lesson is that you never have to *check* the transformation law of an object assembled from four-vectors by tensor operations — antisymmetrisation, symmetrisation, tensor product, contraction. The law is inherited automatically: $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$ transforms as a rank-two tensor because $x$ and $p$ are four-vectors and the rest is algebra. This is the trigger to recognise: whenever a quantity is written as a combination of four-vectors with free indices balanced (one up, one down for each contraction), it is a tensor of the corresponding rank, full stop. The same reasoning certifies that the four-momentum, the angular momentum, the electromagnetic field strength, and the energy-momentum tensor are all tensors without separate proofs.

**Antisymmetric rank-two tensors all transform alike — so the angular momentum and the electromagnetic field are siblings.** The mixing $J'^{02} = \gamma(J^{02} + vJ^{12})$, $J'^{12} = \gamma(J^{12} + vJ^{02})$ is the *same formula* that mixes $E_y$ and $B_z$ under a boost, and this is not a coincidence: any two antisymmetric rank-two tensors transform by the identical rule, because the rule depends only on the rank and the index structure, not on the physical meaning. The transferable diagnostic is to recognise that "the mass-energy dipole and angular momentum vector mix under a boost" is the *same statement* as "the electric and magnetic fields mix under a boost", and every intuition about one transfers to the other. When you meet a new antisymmetric two-tensor, you already know how it boosts.

**Full contractions are the invariants — hunt for them.** The two scalars $J_{\alpha\beta}J^{\alpha\beta}$ and $\epsilon_{\alpha\beta\gamma\delta}J^{\alpha\beta}J^{\gamma\delta}$ are Lorentz-invariant because they have no free indices, and they are the frame-independent content of the angular momentum tensor — the analogues of $B^2 - E^2$ and $\mathbf{E}\cdot\mathbf{B}$ for the field. The reusable principle, drilled throughout the topic, is that to extract observer-independent information from a tensor you fully contract it, and the resulting scalars are the same in every frame. This is the labour-saving move: compute an invariant in whatever frame is easiest (here the rest frame), and the answer holds everywhere. For an antisymmetric two-tensor in four dimensions there are exactly two such scalars, and they classify the tensor up to Lorentz transformations.
