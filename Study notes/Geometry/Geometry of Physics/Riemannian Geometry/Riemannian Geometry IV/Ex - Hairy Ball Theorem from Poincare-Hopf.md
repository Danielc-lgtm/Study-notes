---
type: exercise
subject: differential-topology
difficulty: "⭐⭐"
prereqs:
  - "Thm - Poincare-Hopf Theorem for Surfaces"
  - "Def - Kronecker Index of a Vector Field"
  - "Def - Vector Field on a Manifold"
tags: [topology, differential-topology, vector-fields, hairy-ball, sphere]
---

# Problem Statement

Using the [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]], prove the **hairy ball theorem**: there is no continuous nowhere-vanishing tangent vector field on $S^2$.

Equivalently, every continuous tangent vector field on the $2$-sphere must vanish at at least one point — "you cannot comb a hairy ball flat".

Additionally, **compute the Euler characteristic $\chi(S^2) = 2$** by constructing a specific concrete tangent vector field on $S^2$ with isolated zeros, computing the Poincaré–Hopf indices at each zero, and summing.

**Recall:**

![[Thm - Poincare-Hopf Theorem for Surfaces#Statement]]

![[Def - Kronecker Index of a Vector Field#The Definition]]

For an isolated zero $p$ of a vector field $v$:
- A **source** (linear field $v(x) = x$ near origin in $\mathbb{R}^2$) has index $+1$.
- A **sink** ($v(x) = -x$) has index $+1$.
- A **saddle** ($v(x) = (x, -y)$) has index $-1$.
- A **centre** ($v(x) = (-y, x)$) has index $+1$.

---

# Convergent Strategy

**Problem class:** Topological obstruction problem — show that a certain global structure (a nowhere-vanishing vector field) cannot exist on a manifold, by computing a topological invariant that would force the existence of zeros. The standard technique: combine Poincaré–Hopf with a known Euler characteristic of $S^2$.

**Assumption pattern:** $S^2$ is a closed (compact, without boundary) oriented smooth $2$-manifold. We need to show $\chi(S^2) = 2$ — either by appeal to a known fact or by direct computation. Poincaré–Hopf gives $\sum\mathrm{Ind}(v) = \chi(M)$ for any vector field with isolated zeros; combining with $\chi(S^2) \neq 0$ forces *some* zero to exist for *every* vector field.

**Theorem routing:** (i) [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf]] $\Rightarrow$ $\sum\mathrm{Ind}(v) = \chi(M)$. (ii) Need $\chi(S^2) = 2$: either cite it as a known topological fact, or compute via any concrete vector field (Morse function on $S^2$ gives $1 + (-1)\cdot 0 + 1 = 2$ from one minimum, no saddles, and one maximum). (iii) Conclude: if $v$ had no zeros, $\sum\mathrm{Ind} = 0$, contradicting $\chi = 2$.

**Key decision point:** Whether to (a) take $\chi(S^2) = 2$ as a given topological fact and immediately conclude the hairy ball theorem, or (b) construct a concrete vector field on $S^2$, compute its index sum, and verify the sum equals $2$. The second approach is more concrete and gives the Euler characteristic $\chi(S^2) = 2$ as a *derivation* rather than an assumption. We do both, with emphasis on (b) for the calibration value.

---

# Legal Operations Used

1. **Operation 5 from the topic page (compute the Kronecker index of a vector field at a zero):** For each zero of the chosen vector field, identify the type (source/sink/saddle/centre) and read off the index from the standard list.

2. **Operation 7 from the topic page (apply Poincaré–Hopf for vector-field index sums):** The sum of indices over all zeros equals $\chi(M)$, which for $S^2$ equals $2$.

---

# Hints

> [!note]- Hint 1
> Construct a concrete vector field on $S^2$ with as few zeros as possible. The "flow toward the north pole" is a good choice: at each point $p \in S^2$, take $v(p) = (-\partial_z)|_p^{\text{tangent}}$ — the projection of the downward vertical onto the tangent plane. This field has isolated zeros only at the north and south poles.

> [!note]- Hint 2
> Identify the type of zero at the north pole. As you walk around the pole on a small circle, the field always points *back* toward the pole (radially inward) — it is a sink at the north pole. Similarly at the south pole: the field points *away* from the pole — it is a source. Both sinks and sources have index $+1$.

> [!note]- Hint 3
> Total index sum $= +1$ (south pole, source) $+ +1$ (north pole, sink) $= 2$. By Poincaré–Hopf, this equals $\chi(S^2)$, so $\chi(S^2) = 2$. Now: if any nowhere-vanishing $v$ existed, $\sum\mathrm{Ind} = 0$ (the empty sum), contradicting $\chi = 2$. Hence the hairy ball theorem.

---

# Solution

The proof has two parts. Part 1 computes $\chi(S^2) = 2$ by constructing a concrete vector field with computable indices. Part 2 deduces the hairy ball theorem from Poincaré–Hopf plus this Euler characteristic.

**Part 1: Construct a vector field on $S^2$ with index sum $= 2$.**

> [!note]- Derivation
> Define $v(p) = (-\mathbf{e}_z) - \langle -\mathbf{e}_z, N(p)\rangle N(p)$, the projection of the downward unit vector $-\mathbf{e}_z$ onto the tangent plane $T_pS^2$. Here $\mathbf{e}_z = (0, 0, 1)$ and $N(p) = p$ (since $|p| = 1$ on the unit sphere with outward normal).
>
> Explicitly: $v(p) = -\mathbf{e}_z - (-\langle \mathbf{e}_z, p\rangle)p = -\mathbf{e}_z + p_z\cdot p$, where $p_z$ is the $z$-coordinate of $p$. At a point $p = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$, the field is $v(p) = -(0, 0, 1) + \cos\theta\cdot(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta) = (\sin\theta\cos\theta\cos\varphi, \sin\theta\cos\theta\sin\varphi, \cos^2\theta - 1) = \sin\theta\cos\theta(\cos\varphi, \sin\varphi, 0) + (0, 0, -\sin^2\theta)$. (Let me double-check: $\cos^2\theta - 1 = -\sin^2\theta$. Yes.)
>
> So $v(p) = \sin\theta(\cos\theta\cos\varphi, \cos\theta\sin\varphi, -\sin\theta)$. The magnitude is $|v|^2 = \sin^2\theta(\cos^2\theta(\cos^2\varphi + \sin^2\varphi) + \sin^2\theta) = \sin^2\theta(\cos^2\theta + \sin^2\theta) = \sin^2\theta$. So $|v(p)| = |\sin\theta|$.
>
> Zeros of $v$: $v(p) = 0$ iff $\sin\theta = 0$, iff $\theta = 0$ (north pole) or $\theta = \pi$ (south pole). So exactly two zeros, both isolated.
>
> **Index at the south pole ($\theta = \pi$):** Near the south pole, $\theta$ is close to $\pi$. Set $\tilde\theta = \pi - \theta$ small; then $\sin\theta = \sin\tilde\theta \approx \tilde\theta$ and $\cos\theta = -\cos\tilde\theta \approx -1$. The field becomes $v(p) \approx \tilde\theta(-1\cdot\cos\varphi, -1\cdot\sin\varphi, -\tilde\theta) \approx (-\tilde\theta\cos\varphi, -\tilde\theta\sin\varphi, 0)$ (the $z$-component is higher order). In a tangent-plane chart around the south pole, this is approximately the radial inward field $v \approx -\tilde\theta(\cos\varphi, \sin\varphi)$. This is a **sink** (the negative radial vector field, $v \propto -\mathbf{r}$), with index $+1$ (a sink has index $+1$, same as a source).
>
> Wait — let me recompute. At the south pole, the outward normal is $N = -\mathbf{e}_z$ (pointing down, since $p = (0, 0, -1)$ and outward = away from centre = downward). The field $v(p) = -\mathbf{e}_z$ projected onto the tangent plane to $S^2$ at the south pole... The tangent plane at the south pole is the *horizontal* plane $z = -1$, but viewed as a translate of $T_{p_{\text{south}}}S^2 = \{(x, y, 0)\}$, the projection of $-\mathbf{e}_z = (0, 0, -1)$ onto this plane is $0$ (since $-\mathbf{e}_z$ is already perpendicular to the tangent plane at the south pole). So $v(p_{\text{south}}) = 0$ — confirmed.
>
> For points just above the south pole, $\theta$ close to $\pi$, the projection of $-\mathbf{e}_z$ onto the tangent plane $T_pS^2$ is nonzero and points *away* from the south pole (downward = away from this part of the surface, projected onto the local "up" direction in the tangent plane). Hmm — actually, "flow toward the north pole" means the field flows the *opposite* of toward the south pole. Let me re-examine.
>
> The field $v(p) = $ projection of $-\mathbf{e}_z$ onto $T_pS^2$. At a point $p$ in the northern hemisphere (just above the equator), $-\mathbf{e}_z = (0, 0, -1)$ is pointing down, and its projection onto $T_pS^2$ is a vector tangent to $S^2$ pointing "southward" (toward the south pole). So the flow lines of $v$ run *toward the south pole* in the northern hemisphere and *away from the north pole* in the northern hemisphere — wait, that's the same direction. So everywhere in the northern hemisphere, the field flows toward the south pole; everywhere in the southern hemisphere, the field also flows toward the south pole (toward the bottom). So this field is a **source at the north pole** (flows away from N) and a **sink at the south pole** (flows toward S).
>
> Both sources and sinks have index $+1$. So $\mathrm{Ind}_N(v) = +1$ and $\mathrm{Ind}_S(v) = +1$.
>
> **Sum of indices:** $\sum\mathrm{Ind}(v) = 1 + 1 = 2$.

**Part 2: Deduce $\chi(S^2) = 2$ and the hairy ball theorem.**

> [!note]- Derivation
> By [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf]], $\sum\mathrm{Ind}(v) = \chi(M)$ for any tangent vector field on a closed oriented surface $M$. From Part 1, our specific field on $S^2$ has $\sum\mathrm{Ind} = 2$. Hence $\chi(S^2) = 2$.
>
> **Hairy ball theorem.** Suppose for contradiction that there exists a continuous nowhere-vanishing tangent vector field $w$ on $S^2$. Then $w$ has no zeros, so its index sum is $\sum\mathrm{Ind}(w) = 0$ (the empty sum). By Poincaré–Hopf, this equals $\chi(S^2) = 2$, a contradiction. Hence no such $w$ exists. $\square$

> [!note]- Complete formal solution
> **Step 1: Construct a vector field on $S^2$ with two isolated zeros.** Define $v : S^2 \to TS^2$ by $v(p) = -\mathbf{e}_z - \langle -\mathbf{e}_z, p\rangle p = -\mathbf{e}_z + p_z\cdot p$ (the orthogonal projection of $-\mathbf{e}_z$ onto $T_pS^2$ — using $N(p) = p$ on the unit sphere). In spherical coordinates with $p = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$, $|v(p)| = |\sin\theta|$. So $v$ vanishes precisely at $\theta = 0$ (north pole) and $\theta = \pi$ (south pole), with $v$ nonzero elsewhere — isolated zeros.
>
> **Step 2: Compute indices.** At the south pole, the field's flow lines converge inward (all of $S^2$ flows southward), making it a sink, index $+1$. At the north pole, the field's flow lines diverge outward, making it a source, index $+1$. (Both source and sink have index $+1$ in $2$ [[Def - Dimension|dimensions]] because the linearisation has positive determinant in both cases.)
>
> **Step 3: Apply Poincaré–Hopf.** $\chi(S^2) = \sum_p\mathrm{Ind}_p(v) = 1 + 1 = 2$.
>
> **Step 4: Hairy ball theorem.** Suppose $w$ is a continuous nowhere-vanishing tangent vector field on $S^2$. Then the index sum is $0$ (no zeros). By Poincaré–Hopf, $0 = \chi(S^2) = 2$, contradiction. Hence no continuous nowhere-vanishing tangent vector field on $S^2$ exists. $\square$

> [!warning] Illegal but tempting: "Any vector field on $S^2$ has exactly two zeros"
> This is false. A vector field on $S^2$ can have any number of zeros, as long as the index sum is $2$. **Counterexamples:**
> - A vector field with $4$ sources and $2$ sinks: $\sum = 4 + 2 = 6 \neq 2$. **Invalid** — can't sum to $2$ that way.
> - A vector field with $3$ sources and $1$ sink: $\sum = 3 + 1 = 4 \neq 2$. **Invalid**.
> - A vector field with $2$ sources, $2$ saddles: $\sum = 2 + 2(-1) = 0 \neq 2$. **Invalid**.
> - A vector field with $3$ sources, $1$ saddle: $\sum = 3 + (-1) = 2$. **Valid** — $4$ zeros.
> - A vector field with $1$ source (index $+1$), $1$ "second-order zero" with index $+1$ (a degenerate spiral): $\sum = 2$. **Valid** — $2$ zeros.
> - A vector field with $1$ source of index $+2$ (like the holomorphic field $z^2\partial_z$ at the origin): $\sum = 2$. **Valid** — $1$ zero.
>
> So the index sum is locked at $2$, but the number of zeros and the type of each zero are not — there are infinitely many possible vector-field configurations consistent with $\chi(S^2) = 2$.

> [!tip] Sanity check via Morse theory
> Consider the height function $h(p) = p_z$ on $S^2$, a Morse function with two critical points: a maximum at the north pole (Morse index $2$, vector-field index $(-1)^2 = +1$) and a minimum at the south pole (Morse index $0$, vector-field index $(-1)^0 = +1$). The gradient field $\nabla h$ on $S^2$ has zeros exactly at the critical points, with indices $+1$ each. Index sum $= 2 = \chi(S^2)$. Confirmed.
>
> Alternatively: triangulate $S^2$ as a tetrahedron. Euler characteristic = $V - E + F = 4 - 6 + 4 = 2$. Confirmed.

---

# Key Takeaways

**The hairy ball theorem is a topological obstruction theorem: $\chi \neq 0$ forces vector-field zeros.** The argument is fundamentally about the impossibility of "smoothly combing" a topologically nontrivial surface. The same argument generalises: for any closed oriented $2n$-dimensional manifold with $\chi \neq 0$, every tangent vector field has a zero. The even-sphere case is $S^{2n}$ with $\chi = 2 \neq 0$. The odd-sphere case $S^{2n-1}$ has $\chi = 0$, and indeed odd spheres *do* admit nowhere-vanishing tangent fields (the Hopf flow on $S^3$, generalising the "around-the-equator" field on $S^1$). The vector-field problem on a manifold of arbitrary dimension is the **vector field problem**, and the cleanest answer is in terms of the Euler class of the tangent bundle: a nowhere-vanishing section exists iff the Euler class vanishes, iff $\chi(M) = 0$ in the rank-$n$ case.

**The proof structure "$\chi \neq 0$ + Poincaré–Hopf $\Rightarrow$ existence of zeros" is universally applicable.** Any time you have a closed oriented manifold and want to show a section of the tangent bundle (or more generally, any rank-$n$ vector bundle on an $n$-manifold) must have a zero, the same argument works: compute the Euler class as the index sum of any section, observe that the empty section would give index sum $0$, and use any concrete nonzero topological invariant to derive a contradiction. **Trigger:** "must a section of a bundle vanish somewhere?" → "compute the Euler class of the bundle; if nonzero, every section has a zero."

**The applications of the hairy ball theorem extend far beyond mathematics.** (a) **Meteorology:** there is always a point on the Earth's surface where the wind is calm (the horizontal wind is a tangent vector field on the sphere of Earth, which must vanish somewhere). (b) **Fluid dynamics:** the velocity field of a fluid flowing over a sphere must have stagnation points (vortex shedding from spherical bodies); this constrains the topology of vortex structures. (c) **Electromagnetism:** the tangential component of a magnetic field on a closed conducting sphere must have zeros (electric and magnetic fields, restricted to closed surfaces, give tangent vector fields). (d) **Computer graphics:** "combing" a hair texture on a spherical surface for a $3$D model must produce singular cowlicks, requiring special techniques (vector-field-based texturing on spheres).

**The local computation of indices at sources, sinks, saddles, and centres is the basic vocabulary.** For any vector field problem on a closed surface, the strategy is: identify the zeros, classify each as one of source/sink/saddle/centre (or higher-order), tally the indices ($+1$ for source/sink/centre, $-1$ for saddle, $\pm n$ for higher order), and verify the sum equals $\chi$. With practice, this becomes routine, and the index sums for various Morse-style vector fields on simple manifolds become reflex.

**Companion exercises:** Compare with [[Ex - Total Curvature of a Closed Surface via Gauss-Bonnet]] (computes $\chi(M)$ via the integral $\int K\, dA$ on various surfaces — the Gauss–Bonnet route to the Euler characteristic). The two together give complementary perspectives on $\chi(M)$: the integral-of-curvature route (Gauss–Bonnet) and the sum-of-vector-field-indices route (Poincaré–Hopf), both yielding the same topological invariant. The hairy ball theorem is the topological obstruction extracted from the Poincaré–Hopf route applied to $S^2$.
