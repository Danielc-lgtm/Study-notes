---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Sectional Curvature"
  - "Def - The Riemannian Exponential Map"
  - "Def - Jacobi Field"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, comparison-theorem]
---

# Notation

$(M, g)$ is a complete, connected Riemannian manifold of dimension $n$. **Complete** means every geodesic extends to all of $\mathbb{R}$ (equivalently, $(M, d_g)$ is metrically complete — [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow]]). $\exp_p : T_pM \to M$ is the [[Def - The Riemannian Exponential Map|exponential map]] at $p$. A **Jacobi field** along a geodesic $\gamma$ with tangent $T$ is a smooth vector field $J$ satisfying the Jacobi equation

$$\nabla_T\nabla_T J + R(J, T)T = 0.$$

A point $q = \gamma(s_0)$ is **conjugate** to $p = \gamma(0)$ along $\gamma$ if there exists a nontrivial Jacobi field along $\gamma$ vanishing at both endpoints.

---

# Statement

> **Theorem (Cartan–Hadamard).** Let $(M, g)$ be a complete Riemannian manifold of dimension $n$ with sectional curvature $K \le 0$ everywhere. Then for every $p \in M$, the exponential map
>
> $$\exp_p : T_pM \to M$$
>
> is a smooth covering map, and is a local diffeomorphism everywhere. If, in addition, $M$ is simply connected, then $\exp_p$ is a global diffeomorphism, so $M$ is diffeomorphic to $\mathbb{R}^n$.

> **Corollaries (under the simply-connected hypothesis):**
> 1. Any two points of $M$ are joined by a unique geodesic.
> 2. Geodesic spheres are smooth embedded $(n-1)$-spheres.
> 3. $M$ has no conjugate points along any geodesic.
> 4. $M$ is **contractible** — in particular, all higher homotopy groups vanish.
>
> **Compact-version corollary.** If $(M, g)$ is a compact Riemannian manifold with $K \le 0$, then its universal cover $\widetilde M$ is diffeomorphic to $\mathbb{R}^n$. So $M$ is a **$K(\pi_1, 1)$ space**: its homotopy type is determined by $\pi_1(M)$ alone.

---

# Motivation

Among all global topological theorems forced by curvature, Cartan–Hadamard is the cleanest: nonpositive sectional curvature, combined with completeness, forces the manifold to be (after lifting to the universal cover) diffeomorphic to $\mathbb{R}^n$. There are no exceptions, no extra hypotheses, no boundary cases. This is in stark contrast to the positive-curvature theorems (Synge, Bonnet–Myers, the sphere theorem), each of which requires *several* extra hypotheses (compactness, orientability, dimension parity, pinching).

The intuition is geodesic divergence. On a manifold with $K \le 0$, two geodesics emanating from the same point with slightly different directions *diverge* from each other — at least as fast as they would in Euclidean space, and exponentially fast if $K < 0$ (hyperbolic geodesic divergence). This divergence prevents the geodesics from ever crossing again, which is the geometric obstruction to $\exp_p$ failing to be injective. Combined with global injectivity from simple connectedness, the map $\exp_p$ becomes a diffeomorphism.

The result is foundational for the study of nonpositively-curved Riemannian manifolds. It says: *the universal cover of any compact nonpositively-curved manifold is just $\mathbb{R}^n$ with a Riemannian metric*. So the whole geometric content of such a manifold is encoded in (i) the topology of $\pi_1(M)$, and (ii) how this $\pi_1$ acts by isometries on $\mathbb{R}^n$. This is the starting point of **geometric group theory**, **Gromov-hyperbolic groups**, and **higher Teichmüller theory**.

The theorem has a long history: it is variously attributed to Hadamard (1898, in dimension $2$), Cartan (1928, full statement in arbitrary dimension), and von Mangoldt (special cases). The standard modern proof uses Jacobi fields and is due to Cartan.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: Nonpositive sectional curvature $K \le 0$.* The precondition. **The bridge:** the sign of $K$ enters the proof through the Jacobi equation $J'' + K(J)J = 0$ (in arc-length parameterisation, projected onto an orthonormal parallel frame). Under $K \le 0$, the equation becomes $J'' = -K(J)J = (\text{nonneg})J$, an ODE with the "wrong sign" for oscillation. Solutions grow rather than oscillate; in particular, a Jacobi field vanishing at $s = 0$ has no further zeros. **Example:** any manifold of constant nonpositive curvature ($\mathbb{R}^n$, $H^n$, products like $\mathbb{R}^n \times H^k$).

*Source 2: A homogeneous space $G/H$ with negative sectional curvature.* These automatically satisfy the hypothesis. **The bridge:** all symmetric spaces of noncompact type (e.g., $\mathrm{SL}(n, \mathbb{R})/\mathrm{SO}(n)$, $H^n = \mathrm{O}(1, n)/\mathrm{O}(n)$) have $K \le 0$, and Cartan–Hadamard applies to give the diffeomorphism with $\mathbb{R}^n$. **Example:** the **higher-rank symmetric spaces** are nonpositively curved noncompact manifolds; Cartan–Hadamard gives their universal cover is $\mathbb{R}^d$ where $d$ is the dimension.

*Source 3: A Cayley graph of a "non-positively curved" group.* In **geometric group theory**, a finitely-generated group with $\mathrm{CAT}(0)$ Cayley complex has the structure of a nonpositively-curved metric space, and an analogue of Cartan–Hadamard applies in this combinatorial setting (the **flag complex theorem**). **The bridge:** $\mathrm{CAT}(0)$ groups have contractible classifying space, just as in the smooth case.

**Targets (Output Amplification).**

*Target 1: $K \le 0$ + compact $\implies$ aspherical, $\pi_2 = 0$.* Compact $K \le 0$ manifolds are $K(\pi_1, 1)$ spaces by the corollary. So $\pi_k(M) = 0$ for $k \ge 2$ — all higher homotopy groups vanish. **Combined target:** the topology of a compact nonpositively-curved manifold is *entirely* the topology of $\pi_1$. **Why useful:** the homology, cohomology, and other invariants of $M$ are computable from $\pi_1$ alone via group cohomology $H^*(M) = H^*(\pi_1; \mathbb{Z})$.

*Target 2: $K \le 0$ + simply connected $\implies$ any two points joined by unique geodesic.* The exponential map being a diffeomorphism means that for any $p, q \in M$, there is a unique pre-image $v \in T_pM$ with $\exp_p(v) = q$; the geodesic $\gamma(t) = \exp_p(tv)$ is the unique geodesic from $p$ to $q$, and it is also the unique length-minimiser. **Combined target:** geodesic uniqueness + length-minimisation = no triangle inequalities collapse, no surprising shortest paths, completely "tame" geodesic geometry. **Why useful:** uniqueness of geodesics makes nonpositively-curved spaces an ideal setting for **convex optimisation on manifolds**.

*Target 3: Compact nonpositively-curved manifolds have negative Euler characteristic (under additional hypotheses).* In dimensions $2n$ where the Chern–Gauss–Bonnet formula gives $\chi$ as an integral of a polynomial in $R$ with sign determined by the curvature, $K \le 0$ forces $\chi(M)$ to have a definite sign. In dimension $2$: $\chi(M) = \tfrac{1}{2\pi}\int K\, dV \le 0$, with equality iff $K \equiv 0$. **Combined target:** topological constraints from curvature signs. **Why useful:** rules out compact nonpositively-curved structures on certain manifolds (e.g., $S^2$ cannot carry a nonpositively-curved metric).

---

# Why Is It True

The geometric picture: on a nonpositively-curved manifold, geodesics diverge. Two geodesics emanating from $p$ with slightly different initial directions $v_1, v_2$ have $d(\gamma_{v_1}(t), \gamma_{v_2}(t)) \ge |v_1 - v_2|\cdot t$ for all $t \ge 0$ (in the $K \le 0$ case), with the *exponential* bound $\sinh(\sqrt{|K|}t)|v_1 - v_2|/\sqrt{|K|}$ when $K \le -|K| < 0$. This is **Rauch's theorem** in the $K \le 0$ case. The fact that geodesics diverge — never re-converge — is what prevents the exponential map from being non-injective.

Rigorously: a Jacobi field $J$ along a geodesic with $J(0) = 0$ and $\nabla_T J(0) = v$ satisfies, in arc-length parameter $s$,

$$\tfrac{1}{2}\tfrac{d^2}{ds^2}|J|^2 = |\nabla_T J|^2 - \langle R(J, T)T, J\rangle \ge |\nabla_T J|^2 \ge 0$$

(using $K \le 0$ in the form $\langle R(J, T)T, J\rangle \le 0$). So $|J|^2$ is a *convex* function of $s$ with $|J|(0) = 0$ and $\tfrac{d}{ds}|J|(0) = 2\langle J(0), \nabla_T J(0)\rangle = 0$, so $|J|^2(s) \ge 0$ with equality only at $s = 0$. Hence $J$ has no zeros for $s > 0$ — **no conjugate points**. This means $\exp_p$ is a **local diffeomorphism** everywhere (no critical points), and standard covering-space arguments combined with completeness make it a **covering map**. If $M$ is simply connected, the cover is trivial — $\exp_p$ is a global diffeomorphism.

**The bolded mechanism summary: nonpositive curvature makes $|J|^2$ a convex function of arc length for Jacobi fields, so $|J|$ has at most one zero — no conjugate points — and hence $\exp_p$ has no critical points; combined with completeness and simple connectedness, $\exp_p$ becomes a global diffeomorphism.**

---

# What Makes This Hard

The convexity argument is fairly straightforward; the technical work is in passing from "$\exp_p$ is a local diffeomorphism everywhere" to "$\exp_p$ is a covering map." This requires using completeness of $g$ (and hence of the pulled-back metric $\exp_p^* g$ on $T_pM$) and a standard covering-space-theoretic argument. The common error is forgetting completeness — without it, the pulled-back metric might be incomplete and the global structure of $\exp_p$ unclear. The simply-connected hypothesis enters only at the last step: covering maps onto simply-connected base spaces are diffeomorphisms.

The other subtlety is the difference between "no conjugate points" (local) and "$\exp_p$ is injective" (global). Even without conjugate points, $\exp_p$ could fail to be injective if two distinct geodesics from $p$ end at the same point. The covering-map argument plus simple connectedness handles this.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use the Jacobi equation $J'' + R(J, T)T = 0$ and the assumption $K \le 0$ to show $|J|^2$ is convex, hence $J$ has no zeros after $s = 0$ — no conjugate points. This forces $\exp_p$ to be a local diffeomorphism everywhere. Combine with completeness (the Hopf–Rinow theorem) to upgrade to a covering map. Simple connectedness reduces a covering map to a diffeomorphism.

**Subgoal decomposition:**

1. **$|J|^2$ is convex in $s$ for Jacobi fields $J$ vanishing at $s = 0$.**
   - *Hint:* Compute $\tfrac{1}{2}\tfrac{d^2}{ds^2}|J|^2$ using the Jacobi equation; use $K \le 0$ to bound the curvature term.
   - *Why needed:* Convexity + $J(0) = 0$ forces $|J| > 0$ for $s > 0$, hence no conjugate points.

2. **No conjugate points $\implies$ $\exp_p$ is a local diffeomorphism everywhere.**
   - *Hint:* The differential $d(\exp_p)_v : T_v(T_pM) \to T_{\exp_p(v)}M$ is computed via Jacobi fields with initial conditions $(0, w)$; nonvanishing of $J$ at $s = 1$ for $w \ne 0$ means $d(\exp_p)_v$ is injective.
   - *Why needed:* Local-diffeomorphism property is the starting point for the covering-map argument.

3. **Local diffeo + completeness $\implies$ covering map.**
   - *Hint:* Completeness of $g$ implies geodesics extend forever, which means the pulled-back metric on $T_pM$ via $\exp_p^* g$ is complete; standard covering-space argument shows $\exp_p$ is a covering map.
   - *Why needed:* Covering structure organises the global behaviour.

4. **Covering map + simply connected $\implies$ diffeomorphism.**
   - *Hint:* A covering map onto a simply-connected space, with simply-connected total space, must have trivial deck group, so it is a diffeomorphism.
   - *Why needed:* Final conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Convexity of $|J|^2$ under nonpositive sectional curvature
> **Statement:** For a Jacobi field $J$ along an arc-length geodesic $\gamma$ on a manifold with $K \le 0$, the function $s \mapsto |J(s)|^2$ is convex.
>
> **Hint:** Compute $\tfrac{d}{ds}|J|^2 = 2\langle\nabla_T J, J\rangle$ and $\tfrac{d^2}{ds^2}|J|^2 = 2|\nabla_T J|^2 + 2\langle\nabla_T\nabla_T J, J\rangle = 2|\nabla_T J|^2 - 2\langle R(J, T)T, J\rangle$; use $K \le 0$.
>
> **Why needed:** Convexity is the local key.
>
> > [!note]- Full proof
> > $\tfrac{d^2}{ds^2}|J|^2 = 2|\nabla_T J|^2 + 2\langle\nabla_T\nabla_T J, J\rangle$. Using Jacobi: $\nabla_T\nabla_T J = -R(J, T)T$, so $\langle\nabla_T\nabla_T J, J\rangle = -\langle R(J, T)T, J\rangle = -K(J \wedge T)|J \wedge T|^2$. For $K \le 0$, this is $\ge 0$. Hence $\tfrac{d^2}{ds^2}|J|^2 \ge 2|\nabla_T J|^2 \ge 0$ — convex.

> [!note]- Lemma 2: No conjugate points
> **Statement:** Under $K \le 0$, a Jacobi field $J$ along $\gamma$ with $J(0) = 0$ has no further zeros for $s > 0$.
>
> **Hint:** $|J|^2$ is convex with $|J|(0) = 0$ and $\tfrac{d}{ds}|J|^2(0) = 0$ (since $J(0) = 0$ implies $\langle J, \nabla_T J\rangle(0) = 0$). A convex function starting at $0$ with zero derivative is identically $0$ or strictly positive for $s > 0$.
>
> **Why needed:** No conjugate points = $\exp_p$ is a local diffeomorphism.
>
> > [!note]- Full proof
> > By Lemma 1, $|J|^2$ is convex. With $|J|^2(0) = 0$ and $(d/ds)|J|^2(0) = 0$ (from $J(0) = 0$), convexity forces $|J|^2(s) \ge 0$ with equality only at $s = 0$ for a nonzero Jacobi field. So $J(s) \ne 0$ for $s > 0$.

> [!note]- Lemma 3: $\exp_p$ has no critical points
> **Statement:** Under $K \le 0$, the exponential map $\exp_p : T_pM \to M$ is a local diffeomorphism at every $v \in T_pM$.
>
> **Hint:** The Jacobi-field characterisation of $d(\exp_p)_v$: $d(\exp_p)_v(w) = J(1)$ where $J$ is the Jacobi field along $\gamma(s) = \exp_p(sv)$ with $J(0) = 0$ and $\nabla_T J(0) = w$.
>
> **Why needed:** Critical points of $\exp_p$ are exactly conjugate points; absence of conjugates is local-diffeomorphism property.
>
> > [!note]- Full proof
> > The standard formula $d(\exp_p)_v(w) = J(1)$ holds where $J$ is the Jacobi field with $J(0) = 0, \nabla_T J(0) = w$. By Lemma 2, $J(1) \ne 0$ for $w \ne 0$ (since $1 > 0$). Hence $d(\exp_p)_v$ is injective, hence an isomorphism (same dimensions). So $\exp_p$ is a local diffeomorphism at $v$.

> [!note]- Lemma 4: $\exp_p$ is a covering map
> **Statement:** Under $K \le 0$ and $g$ complete, $\exp_p : T_pM \to M$ is a smooth covering map (when $T_pM$ is endowed with the pulled-back metric $\tilde g := \exp_p^* g$).
>
> **Hint:** Completeness of $g$ implies $\exp_p$ is surjective. Use the standard covering-space lemma: a local isometry between complete connected Riemannian manifolds is a covering map.
>
> **Why needed:** Final structural step before reducing to simple-connectedness.
>
> > [!note]- Full proof
> > Pull back $g$ to $T_pM$ via $\exp_p$: $\tilde g = \exp_p^* g$ is a smooth metric on $T_pM$ (well-defined because $\exp_p$ is a local diffeomorphism by Lemma 3). The map $\exp_p : (T_pM, \tilde g) \to (M, g)$ is by construction a local isometry. Both spaces are connected; $(M, g)$ is complete by hypothesis. Completeness of $(T_pM, \tilde g)$ follows because radial geodesics from $0 \in T_pM$ are linear and extend forever (they correspond to geodesics in $M$). A standard result (e.g., Lee, *Riemannian Manifolds*, Theorem 6.20): a local isometry between complete connected Riemannian manifolds is a covering map.

> [!note]- Lemma 5: $M$ simply connected $\implies$ $\exp_p$ is a diffeomorphism
> **Statement:** If $M$ is simply connected, then the covering map $\exp_p$ of Lemma 4 is a diffeomorphism.
>
> **Hint:** Total space $T_pM \cong \mathbb{R}^n$ is simply connected; covering map onto a simply-connected base is a bijection.
>
> **Why needed:** Final reduction to a diffeomorphism.
>
> > [!note]- Full proof
> > $T_pM \cong \mathbb{R}^n$ is connected and simply connected. A covering map $f : \tilde X \to X$ from a simply-connected $\tilde X$ onto a simply-connected $X$ is bijective (the universal-covering-space theorem identifies $\tilde X$ uniquely up to deck transformations; $\pi_1(X) = 0$ means no nontrivial deck transformations, so $f$ has degree $1$). Hence $\exp_p$ is a bijective local diffeomorphism — a diffeomorphism.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 (Well-posedness).** $\exp_p$ is defined on all of $T_pM$ by completeness of $g$ (every geodesic extends to all of $\mathbb{R}$, so $\exp_p$ extends to all of $T_pM$).
>
> By Lemma 1, $|J|^2$ is convex for Jacobi fields under $K \le 0$. By Lemma 2, this forces no conjugate points. By Lemma 3, $\exp_p$ is a local diffeomorphism everywhere. By Lemma 4, $\exp_p$ is a covering map (using completeness of $g$, which descends to completeness of $\tilde g = \exp_p^* g$ on $T_pM$).
>
> If $M$ is simply connected, by Lemma 5, $\exp_p$ is a diffeomorphism. Thus $M$ is diffeomorphic to $T_pM \cong \mathbb{R}^n$. The corollaries follow:
>
> 1. Uniqueness of geodesic between $p$ and $q$: $\exp_p$ bijective $\implies$ unique $v \in T_pM$ with $\exp_p(v) = q$.
> 2. Geodesic spheres are spheres: $\exp_p$ is a diffeomorphism on each radius $|v| = r$, mapping the sphere $S_r(0) \subset T_pM$ to a smooth embedded $(n-1)$-sphere in $M$.
> 3. No conjugate points: by Lemma 2.
> 4. $M$ contractible: $\exp_p$ gives a diffeomorphism with $\mathbb{R}^n$, which is contractible.
>
> If $M$ is not simply connected, lift to the universal cover $\widetilde M$ (with pulled-back metric, still complete and with $K \le 0$) and apply the simply-connected version.

---

# Cross-Field Exercise Suggestions

1. **Compact hyperbolic manifolds are aspherical $K(\pi_1, 1)$ spaces.** Apply Cartan–Hadamard to a compact hyperbolic $n$-manifold $M = H^n/\Gamma$ ($\Gamma$ a discrete torsion-free subgroup of $\mathrm{Iso}(H^n)$). The universal cover $H^n$ is diffeomorphic to $\mathbb{R}^n$, so $M$ is a $K(\Gamma, 1)$: its homotopy type is *entirely* the homotopy type of $\Gamma$. The cohomology of $M$ is the group cohomology $H^*(\Gamma; \mathbb{Z})$. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]].

2. **Symmetric spaces of noncompact type.** Every symmetric space of noncompact type (e.g., $\mathrm{SL}(n, \mathbb{R})/\mathrm{SO}(n)$, $\mathrm{Sp}(n, \mathbb{R})/\mathrm{U}(n)$, all Hermitian symmetric domains) has $K \le 0$ by an elementary $\mathfrak{p} \otimes \mathfrak{p}$ argument from the Lie-bracket structure. Cartan–Hadamard applies to give that they are diffeomorphic to $\mathbb{R}^d$ — they are the "noncompact duals" of the compact Riemannian symmetric spaces.

3. **CAT(0) groups and geometric group theory.** A finitely-generated group $\Gamma$ acts geometrically on a CAT(0) space (a metric-space generalisation of nonpositive curvature). The CAT(0)-analogue of Cartan–Hadamard gives that such a space is contractible; combined with cocompactness of the action, $\Gamma$ has a finite classifying space — a strong topological-finiteness consequence. **Gromov-hyperbolic groups** are the analogue for negative curvature.

---

# Bridges

- **Hopf–Rinow theorem.** Cartan–Hadamard uses completeness, and the relevant form of completeness is the **metric** completeness of $(M, d_g)$, the **geodesic** completeness ("every geodesic extends to all of $\mathbb{R}$"), and the **existence of length-minimising geodesics** between any two points. The [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow theorem]] establishes all three are equivalent for connected Riemannian manifolds; we are using these freely. The argument that $\exp_p$ is surjective and that the pulled-back metric is complete both use Hopf–Rinow.

- **Rauch comparison theorem.** A quantitative refinement: under $K \le K_0 \le 0$, Jacobi fields along $\gamma$ grow at least as fast as in the constant-curvature-$K_0$ model space. In Cartan–Hadamard's $K \le 0$ case, $K_0 = 0$ gives linear growth $|J(s)| \ge s|\nabla_T J(0)|$; $K \le -1$ gives exponential growth $|J(s)| \ge \sinh(s)|\nabla_T J(0)|$. **Rauch** is the standard quantitative comparison theorem of which Cartan–Hadamard is the topological consequence.

- **Bonnet–Myers (opposite-sign analogue).** Under positive Ricci curvature, geodesics *converge* and the manifold has finite diameter — the opposite phenomenon from Cartan–Hadamard. The Jacobi-field analysis is the same machinery with opposite-sign curvature bound. See [[Thm - Bonnet-Myers Theorem]].

- **Aspherical manifolds and $K(\pi_1, 1)$ classification.** A topological space $X$ is **aspherical** if $\pi_k(X) = 0$ for $k \ge 2$. Compact nonpositively-curved manifolds are aspherical by the corollary of Cartan–Hadamard, but the converse is open: **the Cannon conjecture** asks whether every aspherical closed $3$-manifold admits a nonpositively-curved Riemannian metric. The general statement that "every aspherical $n$-manifold is determined by $\pi_1$" is the **Borel conjecture**, one of the central open problems in geometric topology.

- **Geodesic uniqueness and convex optimisation.** On a simply-connected nonpositively-curved manifold, *any function whose Hessian is positive-definite at every point* has a unique critical point (a minimum) — a global theorem from the geodesic-uniqueness corollary. This is the cleanest setting for **convex optimisation on manifolds** and underlies the **Karcher mean** and other "average of points on a manifold" constructions.
