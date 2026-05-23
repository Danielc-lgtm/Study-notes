---
type: exercise
subject: spinors
difficulty: "⭐⭐"
prereqs:
  - "Def - Spin Structure on a Manifold"
  - "Def - Smooth Manifold"
  - "Def - Vector Bundle"
tags: [geometry, spinors, differential-topology]
---

# Problem Statement

Show that the sphere $S^n$ admits a spin structure for every $n \geq 2$, and that this spin structure is unique. Specifically:

1. Show that the second Stiefel–Whitney class $w_2(S^n) \in H^2(S^n; \mathbb{Z}/2)$ vanishes, using the bundle isomorphism $TS^n \oplus \mathbb{R} \cong S^n \times \mathbb{R}^{n+1}$ (the "Whitney sum trivialisation").
2. Conclude that $S^n$ admits a spin structure.
3. Compute $H^1(S^n; \mathbb{Z}/2)$ for $n \geq 2$, and conclude that the spin structure is *unique* for $n \geq 2$.
4. For comparison: show that $S^1$ has *two* spin structures (the "periodic" and "antiperiodic" choices for fermion fields, corresponding to the two elements of $H^1(S^1; \mathbb{Z}/2) = \mathbb{Z}/2$).

**Recall:**

The spin structure existence criterion:

![[Def - Spin Structure on a Manifold#The Definition]]

The Stiefel–Whitney classes of a vector bundle $E$ are characteristic classes $w_i(E) \in H^i(M; \mathbb{Z}/2)$. Key properties:
- $w_i(E \oplus F) = \sum_{j + k = i} w_j(E) \cup w_k(F)$ (Whitney product formula).
- $w_i(E) = 0$ for $i > \mathrm{rank}(E)$.
- $w_0(E) = 1$.
- $w_i(\mathrm{trivial bundle}) = 0$ for $i \geq 1$.

So in particular, $w_i(\mathrm{trivial})_{\geq 1} = 0$, which combined with the Whitney formula gives $w_i(E \oplus \mathrm{trivial}) = w_i(E)$ — Stiefel-Whitney classes are *stable* under adding trivial summands.

The cohomology of $S^n$ (with any coefficient ring): $H^i(S^n; A) = A$ for $i = 0, n$, and $0$ otherwise (reduced cohomology).

---

# Convergent Strategy

**Problem class:** *Establishing existence of a structure on a manifold via vanishing of a characteristic class.* This is the prototypical exercise in differential topology applied to spin geometry: identify a topological obstruction (here $w_2$), compute it, conclude existence iff it vanishes.

**Assumption pattern:** Given the sphere $S^n$, the natural input is the **stable parallelisability**: $TS^n \oplus \mathbb{R} \cong S^n \times \mathbb{R}^{n+1}$ (trivial). This follows from $S^n \hookrightarrow \mathbb{R}^{n+1}$ as the unit sphere, with the normal direction providing a trivialising line bundle.

**Theorem routing:** Use the stable parallelisability + the *stability* of Stiefel–Whitney classes ($w_i(E \oplus \mathrm{trivial}) = w_i(E)$) to conclude $w_2(TS^n) = w_2(\mathrm{trivial}) = 0$. By the existence criterion from [[Def - Spin Structure on a Manifold]], a spin structure exists. Uniqueness then follows from $H^1(S^n; \mathbb{Z}/2) = 0$ for $n \geq 2$ (the spin structures form a torsor of size $|H^1| = 1$).

**Key decision point:** The trickiest part is recognizing that *all* the Stiefel-Whitney classes of $S^n$ vanish (not just $w_2$), which makes the spin structure existence quite *transparent* for spheres — there is no "barely escape" obstruction here. This contrasts with manifolds like $\mathbb{CP}^2$, where $w_2 \neq 0$ and no spin structure exists.

---

# Legal Operations Used

This exercise uses operations specific to differential topology (Stiefel-Whitney class computations), not the spinor-algebraic operations of the topic page proper.

1. **Bundle-isomorphism stability of $w_i$:** The relation $w_i(E \oplus \mathrm{trivial}) = w_i(E)$ lets one compute $w_i(TS^n)$ via the stably-trivial decomposition $TS^n \oplus \mathbb{R} \cong \mathbb{R}^{n+1}$. This is a standard tool in algebraic topology, not specific to spin geometry.

2. **Existence criterion for spin structures (from [[Def - Spin Structure on a Manifold]]):** A spin structure on an orientable manifold exists iff $w_2 = 0$. The uniqueness (when one exists) is parameterised by $H^1(M; \mathbb{Z}/2)$.

---

# Hints

> [!note]- Hint 1
> The key input is the bundle isomorphism $TS^n \oplus \mathbb{R} \cong S^n \times \mathbb{R}^{n+1}$, where the trivial $\mathbb{R}$ summand is the *outward normal bundle* of $S^n \subset \mathbb{R}^{n+1}$. Geometrically: at each point $p \in S^n$, the tangent space $T_p S^n$ is the $n$-dimensional space perpendicular to $p$ in $\mathbb{R}^{n+1}$, and adding the line $\mathbb{R}\cdot p$ recovers all of $\mathbb{R}^{n+1}$.

> [!note]- Hint 2
> Stiefel–Whitney classes are stable under adding trivial summands: $w_i(E \oplus \mathbb{R}^k) = w_i(E)$. So $w_2(TS^n) = w_2(TS^n \oplus \mathbb{R}) = w_2(S^n \times \mathbb{R}^{n+1}) = 0$. Hence $S^n$ admits a spin structure.

> [!note]- Hint 3
> For uniqueness: spin structures are parameterised by $H^1(M; \mathbb{Z}/2)$. For $n \geq 2$, $H^1(S^n; \mathbb{Z}/2) = 0$ (since $S^n$ is simply-connected, hence $\pi_1(S^n) = 0$, and $H^1(S^n; \mathbb{Z}/2) = \mathrm{Hom}(\pi_1(S^n), \mathbb{Z}/2) = 0$ by the universal coefficient theorem). So the spin structure is unique.

---

# Solution

The plan: use the stable parallelisability of $S^n$ to conclude all Stiefel-Whitney classes vanish; in particular $w_2(S^n) = 0$, so a spin structure exists. The uniqueness for $n \geq 2$ comes from $H^1(S^n; \mathbb{Z}/2) = 0$. For $S^1$ ($n = 1$), $H^1 = \mathbb{Z}/2$ gives two spin structures.

**Step 1: $TS^n \oplus \mathbb{R}$ is trivial.**

The bundle $TS^n \oplus \mathbb{R}$ is isomorphic to $S^n \times \mathbb{R}^{n+1}$, a trivial rank-$(n+1)$ bundle.

> [!note]- Derivation
> $S^n = \{x \in \mathbb{R}^{n+1} : |x| = 1\}$ is embedded in $\mathbb{R}^{n+1}$. At each point $p \in S^n$, the tangent space is $T_p S^n = \{v \in \mathbb{R}^{n+1} : v \cdot p = 0\}$ — the hyperplane perpendicular to $p$. The line $\mathbb{R}\cdot p \subset \mathbb{R}^{n+1}$ is transverse to $T_p S^n$, and together they decompose:
> $$T_p S^n \oplus \mathbb{R}\cdot p = \mathbb{R}^{n+1}.$$
> Varying over $p \in S^n$, this gives the bundle isomorphism $TS^n \oplus \mathrm{N}S^n = TS^n \oplus \mathbb{R} = S^n \times \mathbb{R}^{n+1}$ (where $\mathrm{N}S^n$ is the outward normal line bundle, which is *trivial* — globally parameterised by the position vector $p$).

**Step 2: $w_i(TS^n) = 0$ for all $i \geq 1$.**

The trivial bundle has all Stiefel–Whitney classes vanishing, and $w_i$ is stable under direct sum with trivial bundles.

> [!note]- Derivation
> The Whitney formula gives $w(TS^n \oplus \mathbb{R}) = w(TS^n) \cdot w(\mathbb{R})$. Since $\mathbb{R}$ is trivial, $w(\mathbb{R}) = 1$, so $w(TS^n \oplus \mathbb{R}) = w(TS^n)$. But $TS^n \oplus \mathbb{R}$ is trivial (Step 1), so $w(TS^n \oplus \mathbb{R}) = 1$ — only the $0$-th class is non-zero.
>
> Conclusion: $w_i(TS^n) = 0$ for all $i \geq 1$. In particular, $w_1(TS^n) = 0$ (so $S^n$ is orientable — also easily seen directly) and $w_2(TS^n) = 0$.

**Step 3: $S^n$ admits a spin structure.**

By the existence criterion ($w_2 = 0$ suffices on an oriented manifold), $S^n$ admits a spin structure.

> [!note]- Derivation
> From Step 2, $w_2(TS^n) = 0$. The existence criterion from [[Def - Spin Structure on a Manifold]] says: an oriented Riemannian manifold $M$ admits a spin structure iff $w_2(M) = 0$. So $S^n$ admits a spin structure.

**Step 4: Uniqueness for $n \geq 2$.**

For $n \geq 2$, $H^1(S^n; \mathbb{Z}/2) = 0$, so the spin structure is unique.

> [!note]- Derivation
> Use the cohomology of spheres: $H^1(S^n; \mathbb{Z}/2)$ is non-zero only when $1 = n$ (since $H^i(S^n; A) = A$ for $i = 0, n$, $0$ otherwise). So for $n \geq 2$, $H^1(S^n; \mathbb{Z}/2) = 0$.
>
> By [[Def - Spin Structure on a Manifold]], the set of spin structures is a torsor over $H^1(M; \mathbb{Z}/2)$. With $|H^1| = 1$, there is a unique spin structure.

**Step 5: Two spin structures on $S^1$.**

For $n = 1$, $H^1(S^1; \mathbb{Z}/2) = \mathbb{Z}/2$, so there are two spin structures.

> [!note]- Derivation
> $H^1(S^1; \mathbb{Z}/2) = \mathbb{Z}/2$ (the universal coefficient theorem plus $H_1(S^1; \mathbb{Z}) = \mathbb{Z}$).
>
> The two spin structures correspond physically to **periodic** and **antiperiodic** boundary conditions for fermion fields on the circle. In string theory, these are the **Ramond** and **Neveu-Schwarz** sectors of worldsheet fermions, and both are needed in the full superstring theory.
>
> Equivalently, the two spin structures on $S^1$ differ by the lift of the non-trivial loop $\pi_1(S^1) = \mathbb{Z}$ to $\mathrm{Spin}(1) = \mathbb{Z}/2$: the "trivial lift" sends every loop to $+1$ (periodic spinor), the "non-trivial lift" sends the generator to $-1$ (antiperiodic spinor).

> [!note]- Complete formal solution
> *Stable trivialisation.* The tangent bundle of $S^n \subset \mathbb{R}^{n+1}$ plus the outward normal line $\mathrm{N}S^n$ gives $TS^n \oplus \mathrm{N}S^n = S^n \times \mathbb{R}^{n+1}$. The outward normal is globally parameterised by the position vector $p \in S^n$, so $\mathrm{N}S^n \cong \mathbb{R}$ (trivial).
>
> *Vanishing of Stiefel–Whitney classes.* Stability of $w_i$ under adding trivial summands gives $w_i(TS^n) = w_i(TS^n \oplus \mathbb{R}) = w_i(\mathrm{trivial}) = 0$ for $i \geq 1$. In particular $w_2(TS^n) = 0$, so $S^n$ is spin (and $w_1 = 0$ confirms orientability).
>
> *Uniqueness for $n \geq 2$.* $H^1(S^n; \mathbb{Z}/2) = 0$ for $n \geq 2$ (from the standard sphere cohomology). The set of spin structures is a torsor over this group, so it has exactly one element: a unique spin structure.
>
> *Two spin structures on $S^1$.* $H^1(S^1; \mathbb{Z}/2) = \mathbb{Z}/2$, so there are exactly $2$ spin structures. They correspond physically to the periodic (Ramond) and antiperiodic (Neveu-Schwarz) boundary conditions for fermion fields on the circle.

> [!warning] Illegal but tempting alternative: claim $w_2(S^n) = 0$ because $S^n$ is simply connected
> Simply-connectedness alone does *not* imply spinability: $\mathbb{CP}^2$ is simply connected but not spin ($w_2(\mathbb{CP}^2) \neq 0$). What fails: $\pi_1 = 0$ implies $H_1 = 0$ (Hurewicz), which by universal coefficients gives $H^1(\cdot; \mathbb{Z}/2) = 0$, but this is the *uniqueness* of spin structures (when they exist), not the *existence*. The vanishing of $w_2$ is a *separate* topological condition. **The repair condition:** check $w_2$ via the stable-trivialisation argument (or compute it directly via the Wu formula or Chern-class relation for almost-complex manifolds).

---

# Key Takeaways

**Stable parallelisability is the key topological property that makes spheres spin.** The fact $TS^n \oplus \mathbb{R}^k \cong S^n \times \mathbb{R}^{n+k}$ (trivial) for some $k \geq 0$ is called **stable parallelisability**; for spheres, it holds with $k = 1$. Stable parallelisability immediately implies all Stiefel–Whitney classes vanish (since trivial bundles have trivial Stiefel–Whitney polynomial), and hence all bundle obstructions to lifting structures vanish: $S^n$ is spin, has $\mathrm{Spin}^c$ structures, has string structures (when $\hat A$ vanishes), etc. The spheres are "topologically simple" exactly because of this.

**The spin-structure torsor over $H^1(M; \mathbb{Z}/2)$ is the natural setting for "boundary condition" choices in physics.** The different spin structures on a manifold correspond to *physically inequivalent* fermion theories — different choices of boundary conditions, holonomies of the spin connection, etc. On the circle $S^1$, the two spin structures are the periodic and antiperiodic boundary conditions for a fermion field traveling around the circle. On the torus $T^n$, the $2^n$ spin structures correspond to choosing periodic or antiperiodic boundary conditions independently along each of the $n$ generating loops. On a Riemann surface of genus $g$, the $2^{2g}$ spin structures play a role in **theta characteristics** and the Atiyah-Singer index theorem.

**Sphere is the simplest case; $\mathbb{CP}^2$ is the simplest counterexample.** For higher-dimensional manifolds, the spinability question can be substantially more interesting. $\mathbb{CP}^n$ is spin iff $n$ is odd; $\mathbb{HP}^n$ is spin for all $n$; tori $T^n$ are spin; products $M \times N$ are spin iff both $M$ and $N$ are (modulo $w_2(M \times N) = w_2(M) + w_1(M) w_1(N) + w_2(N)$ which for orientable factors is just additivity). Understanding which manifolds are spin is a deep question in differential topology with consequences for the existence of Dirac operators, the index theorem, the Atiyah-Patodi-Singer eta-invariant, and many other invariants.
