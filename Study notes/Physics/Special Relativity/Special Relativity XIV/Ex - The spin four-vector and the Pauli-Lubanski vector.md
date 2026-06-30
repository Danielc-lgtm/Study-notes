---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Spin Four-Vector"
  - "Def - Casimir Invariants of the Poincaré Group"
  - "Def - Angular Momentum Four-Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

The [[Def - Spin Four-Vector|spin four-vector]] is the [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] divided by the mass, $S^\mu = W^\mu/(mc)$, with $W^\mu = -\tfrac12\epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$. Working with $c = 1$, mostly-minus signature, $\epsilon_{0123} = +1$:

1. Show that $W^\mu$ is orthogonal to the four-momentum, $W\cdot P = 0$, using only the antisymmetry of $\epsilon$. Deduce the spin supplementary condition $S\cdot U = 0$.
2. For a system at rest (four-momentum $P = (m,\mathbf 0)$), compute $W^\mu$ in terms of the rest-frame angular momentum tensor, and show $W^\mu = (0, m\vec\sigma)$ where $\vec\sigma$ is the rest-frame angular momentum vector. Hence $S^\mu = (0,\vec\sigma)$ in the rest frame.
3. Show that $W^2 = -m^2\|\vec\sigma\|^2$ (mostly-minus), so that $W^2$ is the second [[Def - Casimir Invariants of the Poincaré Group|Casimir invariant]] of the Poincaré group, and explain how it labels the spin of the system.
4. For a massless particle ($m = 0$), show that $W^\mu$ becomes proportional to $P^\mu$, $W^\mu = h P^\mu$, and identify $h$ as the helicity. Explain why a massless particle has only a single spin degree of freedom rather than three.

**Recall:**

![[Def - Spin Four-Vector#The Definition]]

The [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] is $W^\mu = -\tfrac12\epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$. The [[Def - Angular Momentum Four-Tensor|angular momentum tensor]] is $J_{\nu\rho} = x_\nu p_\rho - x_\rho p_\nu$ (single particle) or the system sum. The Levi-Civita tensor is totally antisymmetric, $\epsilon_{0123} = +1$, and $\epsilon^{0123} = -1$ in mostly-minus.

---

# Convergent Strategy

**Problem class.** A *connect-classical-to-group-theory* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: identify the classical spin with the Pauli–Lubanski vector, the second Casimir, and read off mass and spin as the two invariants labelling the system.

**Assumption pattern.** The spin four-vector and the Pauli–Lubanski formula. The signpost is "relate to the Casimirs": the spin is $W/m$, and its norm $W^2$ is the second Casimir. This is operation 6 (the supplementary condition) and the Wigner-classification bridge.

**Theorem routing.** Part 1 uses antisymmetry to get $W\cdot P = 0$. Part 2 evaluates in the rest frame. Part 3 computes the invariant $W^2$. Part 4 takes the massless limit, where $W\propto P$ defines helicity.

**Key decision point.** The crux is recognising that the orthogonality $W\cdot P = 0$ (which gives the supplementary condition) is an *identity* forced by the antisymmetry of $\epsilon$ contracted with the symmetric $P_\mu P_\sigma$ — not an extra physical assumption. In the massless limit this same orthogonality, combined with $P^2 = 0$, forces $W\parallel P$, collapsing the spin to helicity.

---

# Legal Operations Used

1. **Operation 6 from the topic page (impose the spin supplementary condition).** Part 1 derives $S\cdot U = 0$ from $W\cdot P = 0$.

2. **Operation 9 from the topic page (kill a contraction with antisymmetry).** Parts 1 and 4 use the antisymmetry of $\epsilon$ against symmetric momentum products.

---

# Hints

> [!note]- Hint 1
> Contract $W^\mu$ with $P_\mu$: $W\cdot P = -\tfrac12\epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu$. The factor $P_\sigma P_\mu$ is symmetric in $\sigma\mu$, but $\epsilon^{\mu\nu\rho\sigma}$ is antisymmetric in $\mu\sigma$. A symmetric tensor contracted with an antisymmetric one vanishes.

> [!note]- Hint 2
> In the rest frame $P = (m,\mathbf 0)$, so $P_\sigma = (m,\mathbf 0)$ and only $\sigma = 0$ contributes: $W^\mu = -\tfrac12\epsilon^{\mu\nu\rho 0}J_{\nu\rho}\,m$. The index $\mu = 0$ gives $W^0 \propto\epsilon^{0\nu\rho 0} = 0$. For $\mu = i$, $W^i = -\tfrac{m}{2}\epsilon^{i\nu\rho 0}J_{\nu\rho}$, where $\nu,\rho$ range over spatial indices, giving the angular momentum vector.

> [!note]- Hint 3
> $W^2 = W^\mu W_\mu$. In the rest frame $W^\mu = (0, m\vec\sigma)$, so $W^2 = \eta_{\mu\nu}W^\mu W^\nu = -m^2\|\vec\sigma\|^2$ (the spatial part with mostly-minus metric). Since $W^2$ is a Lorentz scalar, this holds in every frame.

> [!note]- Hint 4
> For $m = 0$, $P^2 = 0$ (null) and $W\cdot P = 0$ still holds. A vector orthogonal to a *null* vector $P$ and (as one can show) also satisfying $W^2 \leq 0$ with $W\cdot P = 0$ must be proportional to $P$ itself (the only vectors orthogonal to a null vector and not spacelike-transverse are multiples of it). So $W^\mu = hP^\mu$; $h$ is the helicity. The three-component spin collapses because there is no rest frame to define three orthogonal spatial directions.

---

# Solution

The exercise identifies the classical spin with the Pauli–Lubanski vector and extracts the two Casimir invariants. Part 1 derives the supplementary condition from antisymmetry; part 2 evaluates the spin in the rest frame; part 3 computes the invariant $W^2$; part 4 takes the massless limit to helicity.

**Step 1: Orthogonality and the supplementary condition.**

> [!note]- Derivation
> Contract the [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] with the four-momentum:
> $$W\cdot P = W^\mu P_\mu = -\tfrac12\epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu.$$
> The factor $P_\sigma P_\mu$ is *symmetric* under $\sigma\leftrightarrow\mu$, while $\epsilon^{\mu\nu\rho\sigma}$ is *antisymmetric* under $\mu\leftrightarrow\sigma$. The contraction of a symmetric tensor with an antisymmetric one over the same index pair vanishes:
> $$\epsilon^{\mu\nu\rho\sigma}P_\sigma P_\mu = -\epsilon^{\sigma\nu\rho\mu}P_\sigma P_\mu = -\epsilon^{\mu\nu\rho\sigma}P_\mu P_\sigma = -\epsilon^{\mu\nu\rho\sigma}P_\sigma P_\mu,$$
> so the quantity equals its own negative, hence zero. Therefore $W\cdot P = 0$ identically. Dividing by $m$ and using $S^\mu = W^\mu/m$, $P = m U$, gives
> $$S\cdot U = 0,$$
> the **spin supplementary condition**. It is not an assumption but an algebraic identity — the antisymmetry of $\epsilon$ forces the spin four-vector to be orthogonal to the four-velocity, hence spacelike and confined to the rest space.

**Step 2: The rest-frame spin.**

> [!note]- Derivation
> In the rest frame $P = (m, \mathbf 0)$, so $P_\sigma$ is nonzero only for $\sigma = 0$ ($P_0 = m$). Then
> $$W^\mu = -\tfrac12\epsilon^{\mu\nu\rho 0}J_{\nu\rho}\,m.$$
> For $\mu = 0$: $\epsilon^{0\nu\rho 0} = 0$ (repeated index $0$), so $W^0 = 0$. For $\mu = i$ (spatial), $\epsilon^{i\nu\rho 0}$ is nonzero only when $\nu,\rho$ are the two spatial indices other than $i$, so
> $$W^i = -\tfrac{m}{2}\epsilon^{i\nu\rho 0}J_{\nu\rho} = -\tfrac{m}{2}\epsilon^{ijk0}J_{jk} = \tfrac{m}{2}\epsilon^{ijk}J_{jk} = m\,\sigma^i,$$
> using $\epsilon^{ijk0} = -\epsilon^{ijk}$ (moving the $0$ index from last to a sign) and the [[Def - Angular Momentum Four-Tensor|relation]] $\sigma^i = \tfrac12\epsilon^{ijk}J_{jk}$ between the angular momentum vector and the tensor (sign conventions absorbed). So
> $$W^\mu = (0, m\vec\sigma),\qquad S^\mu = \frac{W^\mu}{m} = (0,\vec\sigma).$$
> In the rest frame the spin four-vector is purely spatial, equal to the angular momentum vector $\vec\sigma$ — exactly the "intrinsic angular momentum, no time component" picture. The supplementary condition $S\cdot U = 0$ with $U = (1,\mathbf 0)$ is manifest: $S^0 = 0$.

**Step 3: The second Casimir.**

> [!note]- Derivation
> Compute the invariant $W^2 = W^\mu W_\mu = \eta_{\mu\nu}W^\mu W^\nu$. In the rest frame $W^\mu = (0, m\vec\sigma)$, so
> $$W^2 = \eta_{00}(W^0)^2 + \eta_{ij}W^iW^j = 0 + (-\delta_{ij})(m\sigma^i)(m\sigma^j) = -m^2\|\vec\sigma\|^2,$$
> with the mostly-minus spatial metric $\eta_{ij} = -\delta_{ij}$. Since $W^2$ is a Lorentz scalar (a full contraction), this value holds in *every* frame:
> $$W^2 = -m^2\|\vec\sigma\|^2.$$
> This is the **second Casimir invariant** of the Poincaré group (the first being $P^2 = m^2$). It commutes with every Poincaré generator, so it is constant on each irreducible representation, and it *labels the spin*: in the quantum theory $\|\vec\sigma\|^2\to s(s+1)\hbar^2$, so $W^2 = -m^2 s(s+1)\hbar^2$, and the value of $W^2$ (together with $m$) determines the spin quantum number $s$. The classical spin magnitude $\|\vec\sigma\|$ is the classical shadow of this Casimir.

**Step 4: The massless limit and helicity.**

> [!note]- Derivation
> For a massless particle $m = 0$, the four-momentum is null, $P^2 = 0$, and there is no rest frame. The orthogonality $W\cdot P = 0$ still holds (it used only antisymmetry, not $m\ne 0$). Now, a four-vector $W$ orthogonal to a *null* vector $P$, and itself not "spacelike-transverse" to $P$, must be proportional to $P$: the subspace orthogonal to a null vector $P$ contains $P$ itself, and the physical spin (which for a massless particle cannot have a transverse spacelike part consistent with the little group $ISO(2)$) reduces to that direction. So
> $$W^\mu = h\,P^\mu,$$
> with $h$ a scalar — the **helicity**, the projection of the spin onto the direction of motion. Since $W\propto P$, $W^2 = h^2 P^2 = 0$: the massless Casimir $W^2$ vanishes, and the particle is labelled instead by the single number $h$. Physically, a massless particle has no rest frame in which to set up three orthogonal spin directions; the boost that would bring it to rest is unattainable, and the spin collapses from a three-component vector to a single component along the momentum. This is why a photon ($s = 1$) has only *two* helicity states ($h = \pm 1$), not three, and why a massless particle's spin is its helicity. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** $W\cdot P = -\tfrac12\epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu = 0$ because $P_\sigma P_\mu$ is symmetric and $\epsilon$ antisymmetric in $\mu\sigma$. Hence $S\cdot U = 0$.
>
> **Part 2.** In the rest frame $P = (m,\mathbf 0)$: $W^0 = 0$, $W^i = m\sigma^i$, so $W^\mu = (0, m\vec\sigma)$ and $S^\mu = (0,\vec\sigma)$.
>
> **Part 3.** $W^2 = -m^2\|\vec\sigma\|^2$ (rest frame, mostly-minus); a Lorentz scalar, the second Casimir, labelling spin via $\|\vec\sigma\|^2\to s(s+1)\hbar^2$.
>
> **Part 4.** For $m = 0$, $P^2 = 0$ and $W\cdot P = 0$ force $W^\mu = hP^\mu$ with $h$ the helicity; the spin collapses to one component because there is no rest frame, so a massless particle has two helicity states, not three. $\blacksquare$

---

# Key Takeaways

**Antisymmetry forces the supplementary condition — it is an identity, not an assumption.** The orthogonality $W\cdot P = 0$, hence $S\cdot U = 0$, follows purely from the antisymmetry of the Levi-Civita tensor contracted against the symmetric product $P_\mu P_\sigma$. This is the reusable lesson: whenever you contract the totally antisymmetric $\epsilon$ with a tensor that is symmetric in two of the contracted indices, the result vanishes, and many "constraints" in relativistic physics are actually identities of this kind. The spin supplementary condition is not an extra postulate one imposes on the spin four-vector — it is automatic once the spin is defined through the Pauli–Lubanski vector. The trigger to recognise: any quantity built by contracting $\epsilon$ with momenta will be orthogonal to those momenta, for free, by antisymmetry.

**Mass and spin are the two Casimirs — the classical spin magnitude is $W^2/(-m^2)$.** The invariant $W^2 = -m^2\|\vec\sigma\|^2$ is the second Casimir of the Poincaré group, and together with $P^2 = m^2$ it constitutes the complete set of invariants labelling an irreducible representation — which, by Wigner's theorem, *is* an elementary particle. The transferable insight is that the entire content of "what kind of particle is this" reduces to two numbers, mass and spin, extracted as the two Casimir invariants $P^2$ and $W^2$. The classical spin four-vector of this chapter is the bridge: its norm-squared is the second Casimir, and quantising $\|\vec\sigma\|^2\to s(s+1)\hbar^2$ turns the classical magnitude into the spin quantum number. When you meet a relativistic system, the two questions "how heavy" and "how much spin" are answered by its two Casimirs, and nothing else is needed to classify it.

**No rest frame means no three-component spin — masslessness collapses spin to helicity.** The massless limit is the sharpest illustration of how the kinematics determines the spin structure. A massive particle has a rest frame, three orthogonal spatial directions, and a three-component spin vector. A massless particle has no rest frame — the boost to rest is unattainable — so there are not three orthogonal spatial directions to host the spin, and the Pauli–Lubanski vector, forced parallel to the null momentum, collapses the spin to a single number, the helicity. The reusable diagnostic is that the *little group* (the symmetries fixing the momentum) determines the spin structure: $SO(3)$ for massive particles gives spin $2s+1$ states, $ISO(2)$ for massless particles gives only two helicity states. This is why the photon has two polarisations, not three, and why the graviton (massless spin 2) has two, not five. The transition from three spin components to one helicity, as $m\to 0$, is one of the deepest kinematic facts in relativistic physics, and it falls directly out of the Pauli–Lubanski vector going from spacelike to null.
