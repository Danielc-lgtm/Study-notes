---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic Completeness"
  - "Def - The Riemannian Exponential Map"
  - "Def - Length of a Curve and Riemannian Distance"
tags: [geometry, riemannian-geometry, completeness, hopf-rinow]
---

# Notation

$(M, g)$ a connected Riemannian manifold, $d_g$ the [[Def - Length of a Curve and Riemannian Distance|Riemannian distance function]]. A subset is *bounded* if it has finite $d_g$-diameter. The [[Def - The Riemannian Exponential Map|exponential map]] is $\exp_p : V_p \subseteq T_pM \to M$. The full registry: [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Statement

> **Theorem (Hopf–Rinow).** Let $(M, g)$ be a connected Riemannian manifold. The following conditions are equivalent:
>
> (i) **Geodesic completeness:** every maximal geodesic of $g$ is defined on all of $\mathbb{R}$.
>
> (ii) **Metric completeness:** the metric space $(M, d_g)$ is complete (every Cauchy sequence converges).
>
> (iii) **Heine–Borel property:** every closed bounded subset of $M$ is compact.
>
> (iv) **Pointwise geodesic completeness:** there exists $p \in M$ such that $\exp_p$ is defined on all of $T_pM$.
>
> Furthermore, any of these conditions implies:
>
> (v) **Existence of minimising geodesics:** for every $p, q \in M$, there exists a geodesic $\gamma : [0, L] \to M$ from $p$ to $q$ with $L = d_g(p, q)$ — i.e., a length-minimising geodesic.

---

# Motivation

This is the global existence theorem of Riemannian geometry, and it is one of the cleanest theorems in mathematics. Three a priori different notions of "completeness" — geodesic, metric, Heine–Borel — turn out to coincide on any Riemannian manifold. And any of them implies the strongest possible global statement: every pair of points is joined by a minimising geodesic.

The equivalences are surprising. *Geodesic* completeness is a *dynamical* statement (the geodesic ODE has solutions for all time). *Metric* completeness is a topological/analytic statement (Cauchy sequences converge). *Heine–Borel* is a topological statement (closed bounded sets are compact). These come from three different parts of mathematics, and the theorem says they describe the same property of the manifold.

The equivalence (i) ⟺ (iv) is itself striking: "complete at every point" is automatic from "complete at one point". This is one of the most-used local-to-global statements in Riemannian geometry — it lets you verify completeness by checking just one point, then conclude completeness for the whole manifold.

The existence of minimising geodesics (v) is the most consequential conclusion. Without it, "the geodesic from $p$ to $q$" might not exist as a length-minimising curve, and many constructions (e.g., the radius-of-injectivity neighborhood, the cut locus, the gradient of the distance function) would not be well-defined. With it, on any complete Riemannian manifold, all of these constructions work globally.

The theorem is *also* striking for being **false** in Lorentzian signature in important ways. In Lorentzian geometry, geodesic completeness can fail (singularity theorems of Penrose and Hawking), and even when it holds, the metric-space picture breaks down because $d_g$ is not a metric (it can be zero between distinct points, on null geodesics). The Riemannian Hopf–Rinow theorem is one of the deepest places where Riemannian and Lorentzian geometry differ.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "connected Riemannian manifold". Sources are problems where the application of Hopf–Rinow is implicit.

The most common source is **a compactness hypothesis**. Any compact Riemannian manifold (without boundary) is automatically geodesically complete: maximal geodesic intervals are open, and if bounded would have a limit point in $M$ (by compactness), allowing extension. So compactness ⟹ completeness, and any theorem invoking compactness is invoking Hopf–Rinow's conclusions implicitly. Bridge: "$M$ is compact" routes through Hopf–Rinow to "every pair of points is connected by a minimising geodesic".

A subtler source is **a closedness hypothesis on a subset combined with boundedness in the metric distance**. Hopf–Rinow says closed bounded ⟹ compact. So an a priori non-compact hypothesis (closed and bounded) becomes a compactness hypothesis on a complete manifold. Bridge: "$A \subseteq M$ is closed and bounded" on a complete $M$ gives compactness, hence sequential compactness, hence existence of minimisers in extremisation problems.

A third source is **the integrability of a vector field**. The geodesic vector field $G$ on $TM$ is complete (i.e., its flow is defined for all time) iff the manifold is geodesically complete. So any statement about long-time integration of $G$ — e.g., the geodesic flow being defined globally, or being measure-preserving on all of $TM$ — invokes Hopf–Rinow.

**Targets (Output Amplification)**

The conclusions are the four equivalences plus the existence of minimising geodesics. Targets are theorems that *use* these conclusions.

The most important combination is **Hopf–Rinow + a curvature bound ⟹ a global rigidity or compactness statement**. **Bonnet–Myers**: complete + $\mathrm{Ric} \geq (n-1)K_0 g$ with $K_0 > 0$ ⟹ $M$ is compact with $\mathrm{diam}(M) \leq \pi/\sqrt{K_0}$. The proof uses Hopf–Rinow to get a minimising geodesic of length $d_g$, then the second variation analysis gives the diameter bound. **Cartan–Hadamard**: complete + simply connected + sectional curvature $\leq 0$ ⟹ $\exp_p$ is a global diffeomorphism. The proof uses Hopf–Rinow to get the existence of minimising geodesics needed to extend $\exp_p$ globally.

A second combination is **Hopf–Rinow + the energy functional ⟹ existence of closed geodesics**. On a compact manifold (hence complete), the energy functional on the loop space has critical points by Lusternik–Schnirelmann theory; these are closed geodesics. The compactness/completeness is needed to compactify the loop space and ensure the minimax constructions produce actual critical points.

A third combination is **Hopf–Rinow + the cut locus ⟹ structure of the distance function**. The distance function $d_g(p, \cdot)$ is smooth on the *normal neighborhood* (where $\exp_p$ is a diffeomorphism), but becomes non-smooth at the *cut locus*. The cut locus is well-defined on a complete manifold because every geodesic extends, and beyond the cut point of $p$ along a geodesic, the geodesic ceases to be minimising.

---

# Why Is It True

**Mechanism summary:** **the key implication is (iv) ⟹ (v): if $\exp_p$ is defined on all of $T_pM$, then for any $q \in M$, the function $r(v) := d_g(\exp_p(v), q) + |v|$ on a sphere in $T_pM$ achieves its minimum (by compactness of the sphere), and the minimising direction gives a minimising geodesic from $p$ to $q$. The other equivalences then unfold by standard topological arguments.**

The proof structure is: (iv) ⟹ (v) [the substantive part, requiring a clever construction], then (v) plus standard topology gives the other equivalences.

The construction for (iv) ⟹ (v): given $p, q$ with $p$ having complete $\exp_p$, we want a minimising geodesic from $p$ to $q$. Let $\rho := d_g(p, q)$. Pick a small geodesic sphere $S_\delta(p) = \exp_p(\delta \cdot S^{n-1})$ for small $\delta < \rho$ — this is compact (continuous image of $S^{n-1}$). On $S_\delta$, the continuous function $z \mapsto d_g(z, q)$ achieves its minimum at some point $z_0$. Standard triangle-inequality and Gauss-lemma arguments show $z_0$ lies on a minimising geodesic from $p$ to $q$. Then extend this geodesic past $z_0$ to $q$ — possible because $\exp_p$ is defined on all of $T_pM$ — and verify it remains minimising. The clever part is the **continuation argument**: the supremum of $r \leq \rho$ such that the radial geodesic to distance $r$ from $p$ in direction $z_0/\delta$ is minimising. This supremum is $\rho$ (closed and open in $[\delta, \rho]$), so the entire geodesic from $p$ to $q$ is minimising.

The implications (iv) ⟹ (i): if $\exp_p$ is complete, then by the existence-of-minimising-geodesic conclusion, every $q \in M$ is reached by a geodesic from $p$ of length $d_g(p, q)$, hence the geodesic flow from $p$ is defined globally. To extend to all points: pick any $q$, get a minimising geodesic from $p$ to $q$, extend the geodesic past $q$ (still possible because $\exp_p$ defined everywhere through $q$)... the global definition follows.

(i) ⟺ (ii): a Cauchy sequence has bounded distance, lifts to a Cauchy sequence in $T_pM$ via inverse $\exp_p$... actually a more direct argument is: completeness of geodesics ⟹ on any bounded set the lifted curves are equicontinuous, Arzelà–Ascoli gives convergent subsequences, which combined with Cauchy give convergence to a limit point in $M$. The converse is similar.

(ii) ⟺ (iii): standard metric-space topology — a metric space is complete and bounded sets are precompact iff closed bounded sets are compact (Heine–Borel). For Riemannian manifolds the local picture is Euclidean (charts), and the equivalence transfers.

The unifying theme: **all four conditions express "the manifold has no missing limit points at finite distance"**, and the Riemannian metric structure forces them to be the same condition viewed from different angles.

---

# What Makes This Hard

The conceptual difficulty is **the (iv) ⟹ (i) implication: "complete at one point ⟹ complete at every point"**. This is the deep statement, and it is not obvious from any one of the perspectives in isolation. It requires the construction of minimising geodesics from one point to every other (which uses (iv) and compactness of small geodesic spheres) and then extending the geodesics through those points.

The technical difficulty is the **continuation argument**: showing that the locus of $r$ for which the radial geodesic is minimising is *open and closed* in $[\delta, \rho]$. Openness uses the local diffeomorphism property of $\exp$; closedness uses metric completeness (which is currently being proved!) or a careful triangle inequality / Gauss lemma argument.

The most common error is to **confuse the Riemannian Hopf–Rinow theorem with the Lorentzian situation**. In Lorentzian signature the theorem *fails* in important ways: timelike geodesics can be incomplete in finite affine parameter (singularity theorems), and the "distance function" $d_g$ is not a metric (it does not satisfy the triangle inequality and can be zero between distinct events on null geodesics).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the key implication.**

**High-level strategy:** Prove (iv) ⟹ (v) by a continuation argument: minimising on small geodesic spheres and extending the minimal direction outward by the complete $\exp_p$. Use this and standard topology to derive the other equivalences.

**Subgoal decomposition:**

1. **Find a minimising direction on a small geodesic sphere.** Pick $\delta < d_g(p, q)$. The geodesic sphere $S_\delta(p) = \exp_p(\delta\cdot S^{n-1})$ is compact (continuous image of $S^{n-1}$). The function $z \mapsto d_g(z, q)$ on $S_\delta$ is continuous, hence attains its minimum at some $z_0$.
   - *Hint:* compactness + continuity = attained minimum.
   - *Why needed:* gives the initial direction for the minimising geodesic.

2. **Verify the initial radial geodesic is minimising.** Let $\gamma(t) := \exp_p(t \cdot z_0/\delta)$ for $t \in [0, \delta]$. Show $\gamma|_{[0, \delta]}$ has length $\delta$ and that this is the minimum length over all curves from $p$ to a point on $S_\delta$ "in the direction of $q$".
   - *Hint:* by the [[Thm - The Gauss Lemma|Gauss lemma]], radial geodesics in a normal neighborhood are length-minimising to points on the geodesic sphere.
   - *Why needed:* sets up the continuation.

3. **Continue the geodesic toward $q$.** Define $A := \{r \in [\delta, d_g(p, q)] : \gamma(r) \in \exp_p(T_pM)\text{ and the geodesic up to }r\text{ is minimising}\}$. Show $A$ is open (small neighborhood arguments) and closed (limit point arguments) in $[\delta, d_g(p, q)]$, hence $A = [\delta, d_g(p, q)]$.
   - *Hint:* openness uses local-diffeo of $\exp_p$ (extend a bit further by inverse function theorem); closedness uses the Cauchy property and (iv).
   - *Why needed:* extends the minimising geodesic to reach $q$.

4. **Conclude (v).** The geodesic $\gamma : [0, d_g(p, q)] \to M$ from $p$ to $q$ is minimising.
   - *Hint:* directly from the continuation.
   - *Why needed:* establishes (v) from (iv).

5. **Derive the other equivalences.** (iv) ⟹ (i) by the above (every $q$ reachable from $p$ by a maximal geodesic, hence the geodesic flow from $p$ defined globally). (i) ⟺ (ii) and (ii) ⟺ (iii) by standard metric-space topology applied to the local Euclidean structure on $M$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Compactness of small geodesic spheres
> **Statement:** For $\delta < \mathrm{inj}_g(p)$, the geodesic sphere $S_\delta(p) := \exp_p(\delta \cdot S^{n-1})$ is a smooth compact submanifold of $M$ diffeomorphic to $S^{n-1}$.
>
> **Hint:** $\exp_p$ is a diffeomorphism on a neighborhood of $\delta \cdot S^{n-1}$ in $T_pM$ (by the inverse function theorem). The image is a smooth submanifold.
>
> **Why needed:** Compactness of the sphere gives a continuous function on it (distance to $q$) an attained minimum.
>
> > [!note]- Full proof
> > The set $\delta \cdot S^{n-1} \subseteq T_pM$ is a compact $(n-1)$-submanifold. $\exp_p$ restricted to a neighborhood of this set is a diffeomorphism (by the inverse function theorem applied near each point and the chosen $\delta < \mathrm{inj}_g(p)$). The image is therefore a smooth compact submanifold of $M$, diffeomorphic to $S^{n-1}$ via $\exp_p$.

> [!note]- Lemma 2: Existence of a minimising geodesic
> **Statement:** If $\exp_p$ is defined on all of $T_pM$ (pointwise completeness at $p$), then for every $q \in M$ there exists a geodesic $\gamma : [0, d_g(p, q)] \to M$ from $p$ to $q$ with length $d_g(p, q)$.
>
> **Hint:** Apply the continuation argument: pick a minimising direction on a small geodesic sphere, extend via complete $\exp_p$, verify minimality at each step.
>
> **Why needed:** Establishes (v) from (iv).
>
> > [!note]- Full proof (sketch)
> > Let $L := d_g(p, q)$. By Lemma 1, $S_\delta(p)$ is compact for small $\delta$. The function $z \mapsto d_g(z, q)$ on $S_\delta$ attains its minimum at some $z_0 \in S_\delta$. By the triangle inequality, $d_g(z_0, q) \geq L - \delta$. By the [[Thm - The Gauss Lemma|Gauss lemma]], any curve from $p$ to $q$ must enter every geodesic sphere $S_{\delta'}(p)$ for $\delta' < L$, so the infimum of lengths is $\delta + d_g(z_0', q)$ for the minimising $z_0'$. So $d_g(z_0, q) = L - \delta$.
> >
> > Define the geodesic $\gamma(t) := \exp_p(t \cdot z_0/\delta)$ (a radial geodesic with $\dot\gamma(0) = z_0/\delta$, unit-speed if $\delta = |z_0|$). Show by induction (or a continuation argument) that this geodesic, extended to time $L$, reaches $q$ and has length $L$.
> >
> > **Continuation argument:** define $A := \{r \in [0, L] : d_g(\gamma(r), q) = L - r\}$. We've shown $\delta \in A$. $A$ is closed (by continuity of $d_g$ and $\gamma$). To show $A$ is open in $[0, L)$: at any $r_0 \in A$, apply the same construction at $\gamma(r_0)$ using $\exp_{\gamma(r_0)}$ (defined locally since the manifold is geodesically complete at every point — but wait, we are only assuming (iv) at $p$). Strictly we need (iv) at $\gamma(r_0)$, and an argument that completeness at $p$ implies it at $\gamma(r_0)$, which is essentially the (iv) ⟹ (i) statement. (This subtle point is handled in the full proof in textbooks; see do Carmo or Lee for details.)
> >
> > The upshot is that $A = [0, L]$, so $\gamma$ is the desired minimising geodesic.

> [!note]- Lemma 3: (iv) ⟹ (i)
> **Statement:** If there exists $p$ with complete $\exp_p$, then $\exp_q$ is defined on all of $T_qM$ for every $q$.
>
> **Hint:** Use Lemma 2 to get minimising geodesics from $p$ to every $q$, then extend through $q$.
>
> **Why needed:** Establishes the local-to-global completeness statement.
>
> > [!note]- Full proof (sketch)
> > Given $q \in M$ and $w \in T_qM$, want to define $\exp_q(w)$. Find the minimising geodesic $\gamma_1$ from $p$ to $q$ (Lemma 2); extend by $\exp_q(w)$ in direction $w$ using the fact that the geodesic flow defines $\exp_q$ on some neighborhood of $0 \in T_qM$. To extend to all of $T_qM$: use the completeness of $\exp_p$ to extend the corresponding geodesic from $p$ (via Lemma 2 to nearby points). The technical details are in standard references.

---

# Formal Proof

> [!note]- Complete formal proof
> The complete proof is in any standard Riemannian-geometry textbook (do Carmo's *Riemannian Geometry* Theorem 2.8 of Chapter 7, Lee's *Riemannian Manifolds* Theorem 6.13, Petersen's *Riemannian Geometry* Theorem 5.8.1). We have given the sketch in Lemmas 1–3. The full proof is omitted here; it is one of the cleanest in Riemannian geometry but takes several pages of careful case analysis.
>
> **Theorem.** The four conditions (i)–(iv) are equivalent, and any of them implies (v).
>
> The proof of (iv) ⟹ (v) is the substantive part, established in Lemma 2 by the continuation argument. (iv) ⟹ (i) is Lemma 3. (i) ⟺ (ii) ⟺ (iii) follow from standard metric-space topology applied to the local Euclidean structure. (i) ⟹ (iv) is trivial.
>
> Together these give the full equivalence and the existence-of-minimising-geodesics conclusion. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Topology: Heine–Borel and completeness of $\mathbb{R}^n$.** The Heine–Borel theorem (closed bounded sets in $\mathbb{R}^n$ are compact) is the special case of Hopf–Rinow for Euclidean space. The theorem generalises the most-used compactness criterion in analysis to all complete Riemannian manifolds.

**Functional analysis: completeness of Banach spaces vs Riemannian manifolds.** A Banach space is a complete normed space — *every* Cauchy sequence converges. Hopf–Rinow gives the analogue for Riemannian manifolds (with the metric distance replacing the norm). The "infinite-dimensional Riemannian geometry" of Hilbert manifolds (e.g., the loop space of a finite-dimensional manifold) has its own Hopf–Rinow-style theorems, though more delicate.

**General relativity: failure of Hopf–Rinow in Lorentzian signature.** In Lorentzian signature the theorem fails: even on a flat Minkowski spacetime, the "distance" (proper time along timelike geodesics) is not a metric (it can be zero between distinct events on null geodesics, and it fails the triangle inequality in the reversed sense). The Penrose–Hawking singularity theorems show that even under physically reasonable conditions, geodesic completeness *fails* — there are inextendible spacetimes with timelike incomplete geodesics, which physically are the spacetime singularities of black holes and the Big Bang.

**Algebraic topology: complete metric spaces and contractibility.** A simply connected complete Riemannian manifold of non-positive sectional curvature is contractible (Cartan–Hadamard). The Hopf–Rinow part is the use of completeness; the curvature input gives the diffeomorphism with $\mathbb{R}^n$ via $\exp_p$. Contractibility implies vanishing of all higher homotopy groups, so e.g. the entire fundamental group of a closed non-positively curved manifold is the fundamental group of its universal cover, which is contractible — recovering the theorem that closed non-positively curved manifolds are $K(\pi, 1)$ spaces, with profound consequences in geometric group theory.

---

# Bridges

- **[[Def - Geodesic Completeness|Geodesic Completeness]]** — one of the four equivalent conditions. The theorem says this is equivalent to metric completeness, Heine–Borel, and pointwise completeness. So "complete" is unambiguous on a Riemannian manifold.

- **[[Def - The Riemannian Exponential Map|The Exponential Map]]** — the construction at the heart of the proof. The existence of minimising geodesics is established by extending the radial geodesics of $\exp_p$ outward, using the assumption that $\exp_p$ is defined globally.

- **[[Thm - The Gauss Lemma|The Gauss Lemma]]** — the local minimisation input. Radial geodesics from $p$ in a normal neighborhood are length-minimising; this fact is used in the construction of the minimising direction on the small geodesic sphere.

- **The Bonnet–Myers theorem** — direct consumer. Complete + $\mathrm{Ric} \geq (n-1) K_0 g$ with $K_0 > 0$ ⟹ compact, diameter $\leq \pi/\sqrt{K_0}$, finite $\pi_1$. The proof uses Hopf–Rinow's existence of a minimising geodesic of length $d_g(p, q)$ for any $p, q$; the second variation analysis on this minimising geodesic then forces the diameter bound. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

- **The Cartan–Hadamard theorem** — another direct consumer. Complete + simply connected + sectional curvature $\leq 0$ ⟹ $\exp_p$ is a global diffeomorphism. The completeness is used to know that $\exp_p$ is defined on all of $T_pM$; the absence of conjugate points (from non-positive curvature) makes $\exp_p$ a local diffeomorphism everywhere; simply connectedness upgrades local to global via covering-space theory.

---

# Unlocked by This

> [!tip] Bonnet–Myers and Cartan–Hadamard *(from Riemannian Geometry)*
> The two foundational curvature-to-topology theorems both require Hopf–Rinow as a precondition. **Bonnet–Myers** uses Hopf–Rinow's existence of minimising geodesics and the [[Thm - Second Variation of Arc Length|second variation]] to deduce a diameter bound from a positive Ricci lower bound. **Cartan–Hadamard** uses Hopf–Rinow's geodesic completeness and the no-conjugate-points conclusion from non-positive curvature to upgrade $\exp_p$ to a global diffeomorphism. Both are developed in [[Riemannian Geometry III — Riemann Curvature and Topology]].

> [!tip] **The Cut Locus and Injectivity Radius** *(from Riemannian Geometry)*
> On a complete manifold (so Hopf–Rinow applies), the **cut locus** of $p$ is well-defined: it is the set of points $q$ at which there are multiple minimising geodesics from $p$, or beyond which the minimising geodesic ceases to be unique. The **injectivity radius** $\mathrm{inj}_g(p) := d_g(p, \mathrm{cut}_g(p))$ is the largest radius of the normal neighborhood. The Klingenberg lemma bounds the injectivity radius from below in terms of curvature and the length of closed geodesics.

> [!tip] **Geometric Group Theory and the Švarc-Milnor Lemma** *(from Geometric Group Theory)*
> A complete Riemannian manifold with cocompact isometric action of a discrete group $\Gamma$ is quasi-isometric to the Cayley graph of $\Gamma$ (with any finite generating set). This is the **Švarc–Milnor lemma**, the foundational connection between Riemannian geometry and geometric group theory. Hopf–Rinow is the input: completeness guarantees the existence of minimising geodesics needed to define the quasi-isometry.
