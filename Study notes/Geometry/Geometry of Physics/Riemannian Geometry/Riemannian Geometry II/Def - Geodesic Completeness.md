---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic"
  - "Def - The Riemannian Exponential Map"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, completeness]
---

# Notation

$(M, g)$ a connected Riemannian manifold, $p \in M$, $T_pM$ its tangent space, and $\gamma_v$ the unique maximal [[Def - Geodesic|geodesic]] with $\gamma_v(0) = p, \dot\gamma_v(0) = v$, defined on a maximal open interval $I_v \subseteq \mathbb{R}$ containing $0$. The Riemannian distance is $d_g(p, q) := \inf_\gamma L(\gamma)$ over piecewise-smooth curves from $p$ to $q$. See [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] for the full registry.

---

# Axiom Motivation

The motivation is: **on a Riemannian manifold, what does "no boundary at infinity" mean, and what should it imply?** In $\mathbb{R}^n$ the answer is intuitive — there is no boundary, any straight line goes on forever, and the metric distance has no upper bound at all. But on a general manifold we can lose this in two distinct ways: the manifold might have a *real* boundary (open set, manifold with boundary) where curves stop, or it might be metrically incomplete in some subtler way ([[Def - Geodesic|geodesics]] that approach infinity in finite time, like the punctured plane).

Three a priori different notions are candidates for "no boundary":

1. **Geodesic completeness**: every maximal geodesic has $I_v = \mathbb{R}$ — geodesics can be extended for all time, in both forward and backward direction.
2. **Metric completeness**: the metric space $(M, d_g)$ is complete — every Cauchy sequence converges.
3. **Heine–Borel property**: every closed and bounded subset of $M$ is compact.

The startling content of the [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow theorem]] is that **on a connected Riemannian manifold these three are equivalent**, and any of them additionally implies that every pair of points is connected by a length-minimising geodesic. So "no boundary" has, on Riemannian manifolds, a single coherent meaning, and the geodesic-completeness formulation is the most operational because it is the one ODE theory directly produces.

The choice of *geodesic* completeness — extending geodesics, not arbitrary curves — is significant. Curve-extension is not a useful notion: any smooth curve can be extended to a slightly longer smooth curve (just continue smoothly), so the entire interior of any manifold is "curve-complete" in the trivial sense. What singles out geodesics is that they are *forced* by the metric — once you know $(p, v)$ you have no choice in $\gamma_v$ — so the question of whether $\gamma_v$ can be extended is a genuine geometric question, not a question about which curves we choose to draw.

The natural relaxation is **forward** vs **two-sided** completeness. *Forward geodesically complete* means every maximal geodesic is defined on $[0, \infty)$ (forward in time). This is the relevant notion for general relativity, where "the future of a freely-falling observer extends indefinitely" is the meaningful condition, and the failure of forward completeness corresponds to *physical* singularities (the Big Bang, the black-hole singularity). For Riemannian (positive-definite) manifolds, by reversing the parameter $t \mapsto -t$ one sees that forward and backward completeness are equivalent — every geodesic can be reversed — so two-sided completeness is the standard notion. In Lorentzian signature this fails: a Lorentzian manifold can be future-complete but past-incomplete (this is the entire subject of singularity theorems in GR).

A subtler design question is whether to demand completeness at *some* point or at *every* point. The Hopf–Rinow theorem includes the result that if $\exp_p$ is defined on all of $T_pM$ for *some* $p$, then the manifold is geodesically complete (and hence $\exp_q$ is defined on all of $T_qM$ for *every* $q$). So the local-looking condition is automatically global. This is one of the most useful single facts about Riemannian manifolds: completeness is a property of the manifold, not of a point.

Why **not** drop completeness and just work with incomplete manifolds? Because most of the structure theorems we want — *every* pair of points joined by a minimising geodesic, the existence of minimisers in [[Def - Homotopy|homotopy]] classes, the relationship between curvature bounds and diameter bounds (Bonnet–Myers), the duality between Riemannian completeness and metric-space completeness — all *use* completeness essentially. On an incomplete manifold one can construct examples where every nice theorem fails: e.g., the punctured plane $\mathbb{R}^2 \setminus \{0\}$ is incomplete, and there is no minimising geodesic between a point and itself going through the deleted origin. Completeness rules out this kind of pathology.

When completeness fails, the standard remedy is to *complete* the manifold — but the metric completion $\overline{(M, d_g)}$ may not be a manifold (it can have singular points where curves run together). So the proper response to incompleteness is to either restrict attention to a sub-manifold that *is* complete (e.g., shrink the domain to a relatively compact subset), or to upgrade to a singular setting (CAT($k$) spaces, Aleksandrov spaces). The "all geodesics extend forever" condition is the cleanest sufficient condition for the entire theory to work.

---

# The Definition

A connected Riemannian manifold $(M, g)$ is **geodesically complete** if every maximal [[Def - Geodesic|geodesic]] of $g$ is defined on all of $\mathbb{R}$.

Equivalently — and this is the form we use most often — for every $p \in M$, the [[Def - The Riemannian Exponential Map|exponential map]] $\exp_p$ is defined on the entire tangent space $T_pM$ (rather than on a proper open star-shaped subset $V_p \subsetneq T_pM$).

A point $p$ is said to **have a complete exponential** if $\exp_p$ is defined on all of $T_pM$; the [[Thm - Hopf-Rinow Theorem (Statement)|Hopf–Rinow theorem]] then says that if one point has a complete exponential, *every* point does, and the manifold is geodesically complete in the global sense.

A weaker notion is **forward geodesic completeness**: every maximal geodesic is defined at least on $[0, \infty)$ (extends forward in time). For Riemannian (positive-definite) metrics this is equivalent to two-sided completeness by reversing the parameter; the distinction matters only in Lorentzian / pseudo-Riemannian settings.

---

# Relate to Other Fields / Compression

**True name:** **the manifold has no metric boundary "at finite distance"**. Geodesic completeness is the strongest form of the statement: a geodesic never falls off the manifold in finite affine parameter. Metric completeness is the equivalent form in metric-space language. Heine–Borel is the topological form. The unifying picture is that the manifold is *the maximal* arena for the metric $g$ — there is no further geometric content that should be added.

**Compactness implies completeness.** A compact Riemannian manifold (without boundary) is automatically geodesically complete: the maximal interval of existence of any geodesic is open, and if it were a bounded interval $(\alpha, \beta) \subsetneq \mathbb{R}$ then by compactness the geodesic would have a limit point in $M$ at $t = \beta$, contradicting maximality. So all the geometric theorems requiring completeness apply automatically to compact manifolds, which is why most introductory examples are compact.

**Completeness and the Cauchy problem.** ODE theory always gives *local* existence and uniqueness; *global* existence (for all time) is a separate question depending on the vector field. The geodesic vector field $G$ on $TM$ is locally Lipschitz (smooth, in fact), so always has local solutions; the question is whether the solutions can be extended indefinitely. The Hopf–Rinow theorem says: yes, iff the metric ball-completeness holds, iff every closed bounded set is compact.

---

# Examples / Corollaries

**Is an instance: Euclidean space $\mathbb{R}^n$.** Geodesics are straight lines $\gamma_v(t) = p + tv$, defined for all $t \in \mathbb{R}$. So $\mathbb{R}^n$ is geodesically complete. The metric space $(\mathbb{R}^n, d)$ with Euclidean distance is complete; closed and bounded sets are compact (the original Heine–Borel theorem). Everything checks out.

**Is an instance: the sphere $S^n$.** Compact, so geodesically complete. Geodesics (great circles) are defined for all $t$, periodically wrapping around the sphere with period $2\pi$. Every pair of points is joined by a minimising geodesic (the shorter great-circle arc).

**Is an instance: hyperbolic space $\mathbb{H}^n$.** Geodesically complete: all geodesics (vertical lines and orthogonal semicircles in the half-space model) are defined for all $t$. Non-compact but complete; the exponential map at any point is a [[Def - Diffeomorphism|diffeomorphism]] $T_p\mathbb{H}^n \to \mathbb{H}^n$ (this is the [[Riemannian Geometry III — Riemann Curvature and Topology|Cartan–Hadamard theorem]] specialised to constant negative curvature).

**Is an instance: any compact Riemannian manifold.** As noted above, compactness implies completeness automatically.

**Is an instance: a Lie [[Def - Group|group]] with bi-invariant metric.** Geodesically complete: the geodesics through the identity are the one-parameter [[Def - Subgroup|subgroups]] $t \mapsto \exp(tX)$, defined for all $t \in \mathbb{R}$, and translating by other group elements gives all geodesics, again defined for all $t$.

**Is NOT an instance: the open unit ball $B^n \subseteq \mathbb{R}^n$ with the Euclidean metric.** Geodesics that head radially outward from the centre reach the boundary $|x| = 1$ in finite affine time and cannot be extended further. So $B^n$ is *not* geodesically complete. The metric space $(B^n, d)$ is incomplete (Cauchy sequences can converge to points on the boundary, which are not in $B^n$). The metric completion is the closed ball $\overline{B^n}$, which is a manifold with boundary, not a manifold. This shows the necessity of distinguishing "complete" from just "open".

**Is NOT an instance: the punctured plane $\mathbb{R}^2 \setminus \{0\}$ with the Euclidean metric.** Geodesics that head toward the deleted origin reach it in finite time. Equivalently, the Cauchy sequence $(1/n, 0)$ does not converge in $\mathbb{R}^2 \setminus \{0\}$. Not complete. To make it complete one could add the origin back (recovering $\mathbb{R}^2$) or change the metric to make the origin infinitely far away — for example, use the Poincaré upper-half-plane-like metric $dx^2 + dy^2 / (x^2 + y^2)$, which makes the puncture an infinity rather than a finite boundary.

**Is NOT an instance: a flat torus $T^2$ with a single point removed.** Topologically still a manifold, but again the geodesics that aim at the puncture reach it in finite time. Removing any point from a complete manifold breaks completeness.

**Corollary (compactness ⟹ completeness).** A compact Riemannian manifold without boundary is geodesically complete. *Calibration check:* a maximal geodesic on an open finite interval would have, by compactness, a convergent subsequence at the endpoint, hence a limit in $M$; this limit could be used as initial data for further extension, contradicting maximality of the original interval.

**Corollary (Hopf–Rinow's existence-of-minimisers).** If $(M, g)$ is connected and geodesically complete, then for any $p, q \in M$ there is a geodesic from $p$ to $q$ whose length equals $d_g(p, q)$. *Calibration check:* this is a non-trivial consequence of completeness — minimisation requires both lower semicontinuity of length (true) and existence of a minimum (which fails on incomplete manifolds like the punctured plane). See [[Thm - Hopf-Rinow Theorem (Statement)]].

**Corollary (the exponential map is surjective on complete manifolds).** If $(M, g)$ is connected and geodesically complete, then for every $p \in M$, $\exp_p : T_pM \to M$ is surjective. *Calibration check:* every $q \in M$ is reached by a minimising geodesic from $p$ (by Hopf–Rinow), which is $\gamma_v$ for some $v$, and then $q = \exp_p(v)$.

**Calibration check.** If you can verify (a) that the open unit disk is not geodesically complete with the Euclidean metric but *is* with the Poincaré metric, (b) that compactness automatically implies completeness, and (c) that completeness lets you talk about minimising geodesics between arbitrary pairs of points — then you have understood the definition.

---

# Unlocked by This

> [!tip] The Hopf–Rinow Theorem *(from Riemannian Geometry)*
> Geodesic completeness is just one face of a single condition that also includes metric completeness, the Heine–Borel property, and the existence of minimising geodesics between any pair of points. [[Thm - Hopf-Rinow Theorem (Statement)]] is the master theorem that ties all of these together; on a connected Riemannian manifold, any one of these implies all the others.

> [!tip] Curvature-and-Completeness Theorems *(from Riemannian Geometry)*
> Many of the deepest theorems in Riemannian geometry combine completeness with a curvature hypothesis: **Bonnet–Myers** (Ricci $\geq (n-1)K_0 g$ with $K_0 > 0$ + completeness ⟹ compact, diameter $\leq \pi/\sqrt{K_0}$); **Cartan–Hadamard** (sectional curvature $\leq 0$ + complete + simply connected ⟹ $\exp_p$ is a diffeomorphism, $M$ diffeomorphic to $\mathbb{R}^n$); **Synge** (compact + sectional curvature $> 0$ + even dimension + orientable ⟹ simply connected). Each uses completeness in an essential way to upgrade local curvature data to global topology. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] **Singularity Theorems in General Relativity** *(from General Relativity)*
> In Lorentzian signature, completeness fails — a Lorentzian manifold can be *geodesically incomplete* (in the forward, backward, timelike, null, or causal sense), and the **Penrose–Hawking singularity theorems** show that under reasonable physical conditions (positive energy, trapped surfaces) Lorentzian incompleteness *must* occur. So black-hole singularities and the Big Bang are not artefacts of specific solutions — they are forced by completeness failing under generic gravitational collapse. This is the deepest difference between Riemannian and Lorentzian geometry.
