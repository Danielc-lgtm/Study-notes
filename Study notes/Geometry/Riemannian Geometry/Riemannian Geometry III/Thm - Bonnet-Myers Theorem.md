---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Ricci Tensor"
  - "Def - Jacobi Field"
  - "Def - The Riemannian Exponential Map"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, comparison-theorem]
---

# Notation

$(M, g)$ is a complete connected Riemannian manifold of dimension $n$. The **diameter** is $\mathrm{diam}(M) := \sup\{d_g(p, q) : p, q \in M\}$, where $d_g$ is the Riemannian distance. The Ricci tensor is $\mathrm{Ric}$, and a lower Ricci bound is written $\mathrm{Ric} \ge \lambda\, g$, meaning $\mathrm{Ric}(v, v) \ge \lambda|v|^2$ for every tangent vector $v$. The fundamental group is $\pi_1(M)$, computed at any basepoint. A **conjugate point** along a geodesic $\gamma$ is a point $\gamma(s_0)$ where a nontrivial Jacobi field along $\gamma$ vanishes (with $\gamma(0)$ as the initial-zero point).

---

# Statement

> **Theorem (Bonnet–Myers).** Let $(M, g)$ be a complete Riemannian manifold of dimension $n$ with Ricci curvature satisfying
>
> $$\mathrm{Ric}(v, v) \ge (n-1)\kappa\, |v|^2 \qquad \forall v \in TM$$
>
> for some constant $\kappa > 0$. Then:
>
> 1. **Diameter bound**: $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$.
> 2. **Compactness**: $M$ is compact (since complete and of bounded diameter).
> 3. **Finite fundamental group**: $\pi_1(M)$ is finite.
>
> The bound is **sharp**: the round sphere $S^n_\kappa$ of constant sectional curvature $\kappa$ has $\mathrm{Ric} = (n-1)\kappa\, g$ exactly, with $\mathrm{diam}(S^n_\kappa) = \pi/\sqrt{\kappa}$.

---

# Motivation

Cartan–Hadamard gave us a global topological consequence of nonpositive sectional curvature: simply-connected manifolds with $K \le 0$ are diffeomorphic to $\mathbb{R}^n$. Bonnet–Myers is the analogous theorem for *positive* curvature, but with two important differences. First, it uses **Ricci curvature** rather than sectional curvature — a much weaker hypothesis, since Ricci is a single-direction average rather than a per-plane quantity. Second, the conclusion is quantitative: not only is the manifold compact, but its diameter is bounded by an *explicit* constant depending on the curvature lower bound.

The intuition is geodesic *convergence*. On a manifold with positive Ricci curvature, geodesics emanating from a point in nearby directions converge back together — analogous to longitudes on a sphere meeting at the antipodal pole. The convergence is so strong that no geodesic can be a length-minimising path between its endpoints if it is longer than $\pi/\sqrt{\kappa}$ — there will always be a conjugate point in its interior, after which (by the [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles|second variation analysis]]) the geodesic can be shortened.

The diameter bound is the strongest part of the theorem; compactness and finite $\pi_1$ are corollaries. Compactness follows because $M$ is complete (every geodesic extends to $\mathbb{R}$, so by Hopf–Rinow, $M$ is metrically complete) and metrically bounded — by the **Heine–Borel** part of Hopf–Rinow, complete + bounded = compact. Finite $\pi_1$ follows by lifting the same hypothesis to the universal cover: $\widetilde M$ is also complete with $\mathrm{Ric} \ge (n-1)\kappa g$, so $\widetilde M$ is compact too, and a compact covering of a compact space has finite degree.

The theorem was proved by **Bonnet** ($1855$) in dimension $2$ with sectional curvature hypothesis (where $K = \tfrac{1}{n-1}\mathrm{Ric}$), and generalised by **Myers** ($1941$) to arbitrary dimension with the Ricci hypothesis, using the now-standard Jacobi-field-conjugate-point argument.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: Positive sectional curvature $K \ge \kappa > 0$.* This implies positive Ricci ($\mathrm{Ric}(v, v) = \sum_{j \ne i}K(e_i \wedge e_j) \ge (n-1)\kappa$ for unit $v = e_i$). **The bridge:** sectional bounds always imply matching Ricci bounds; positive sectional is the most common way to verify Bonnet–Myers's hypothesis. **Example:** the round sphere $S^n$ has $K = 1$, hence $\mathrm{Ric} = (n-1)g$, hence diameter $\le \pi$ (in fact, exactly $\pi$).

*Source 2: Einstein with positive scalar curvature.* $\mathrm{Ric} = (S/n)g$ with $S > 0$ gives $\mathrm{Ric} = (S/n)g > 0$, so Bonnet–Myers applies with $\kappa = S/(n(n-1))$. **The bridge:** Einstein manifolds with positive scalar curvature are always Bonnet–Myers candidates. **Example:** $\mathbb{CP}^n$ with Fubini–Study metric is Einstein with positive scalar curvature; Bonnet–Myers gives compactness and finite $\pi_1$ (in fact $\pi_1 = 0$).

*Source 3: A matter-coupled Einstein equation in general relativity satisfying the strong energy condition.* In GR, the strong energy condition is $\mathrm{Ric}(v, v) \ge 0$ for every timelike $v$ — and a uniform positive bound on this gives a Bonnet–Myers analogue. **The bridge:** in cosmology, a closed (positively-curved) spatial slice in an FLRW spacetime satisfying the strong energy condition has finite diameter — there is a maximum spatial extent of the universe. This is one of the steps in **Penrose–Hawking singularity theorems**.

**Targets (Output Amplification).**

*Target 1: Finite $\pi_1$ + compactness $\implies$ certain algebraic-topology classifications.* Combining Bonnet–Myers with the universal-coefficient theorem and Poincaré duality: a compact orientable Riemannian manifold with $\mathrm{Ric} > 0$ has finite $\pi_1$, so its universal cover is also compact orientable with $\mathrm{Ric} > 0$ and so on. Bochner's vanishing theorem strengthens this: $\mathrm{Ric} > 0$ + compact $\implies$ first Betti number $b_1(M) = 0$. **Combined target:** Bonnet–Myers + Bochner = strong topological constraints from positive Ricci.

*Target 2: A diameter bound implies a Sobolev or Poincaré inequality.* The diameter bound $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$, combined with Bishop–Gromov volume comparison, gives quantitative control over geometric inequalities on $M$. **Combined target:** Bonnet–Myers + Bishop–Gromov = volume bounds + diameter bounds = compactness theorems for spaces of metrics (**Gromov–Hausdorff compactness**, **Cheeger–Gromov compactness**).

*Target 3: Application to cosmology — closed FLRW universes.* In **general relativity**, a spatial slice of an FLRW cosmology with positive curvature is a $3$-sphere (or its quotient). The size of this $3$-sphere, governed by the **scale factor** of the cosmology, has an explicit Bonnet–Myers-style upper bound in terms of the curvature parameter. **Combined target:** Bonnet–Myers in spacetime cosmology = bounded "size" of the spatial universe.

---

# Why Is It True

The key observation: on a manifold with $\mathrm{Ric} \ge (n-1)\kappa g$, a geodesic of length $> \pi/\sqrt{\kappa}$ must contain a **conjugate point** in its interior, hence (by [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles|the second variation analysis]]) is not minimising. Since geodesics joining two points must be minimising (by Hopf–Rinow), $d(p, q) \le \pi/\sqrt{\kappa}$ for all $p, q$ — the diameter bound.

To produce the conjugate point: along an arc-length geodesic $\gamma$ of length $L$, consider the variation field $J(s) = \sin(\pi s/L)\,e(s)$ where $e$ is a parallel unit vector field perpendicular to $\gamma$. Compute the second variation of arc length:

$$L''(0) = \int_0^L\bigl(|\nabla_T J|^2 - \langle R(J, T)T, J\rangle\bigr)ds.$$

Substituting $J(s) = \sin(\pi s/L)\,e$ with $|\nabla_T J|^2 = (\pi/L)^2\cos^2(\pi s/L)$ and $\langle R(J, T)T, J\rangle = \sin^2(\pi s/L)\,K(T \wedge e)$:

$$L''(0) = \int_0^L\bigl((\pi/L)^2\cos^2 - K(T \wedge e)\sin^2\bigr)ds.$$

Now **sum over $n - 1$ orthonormal parallel normal fields** $e_1, \ldots, e_{n-1}$ to get the total second variation in $n - 1$ orthogonal directions:

$$\sum_{i=1}^{n-1}L_i''(0) = \int_0^L\bigl((n-1)(\pi/L)^2\cos^2 - \mathrm{Ric}(T, T)\sin^2\bigr)ds.$$

Using $\mathrm{Ric}(T, T) \ge (n-1)\kappa$ and the integrals $\int_0^L\cos^2 = \int_0^L\sin^2 = L/2$:

$$\sum L_i''(0) \le (n-1)\cdot\tfrac{L}{2}\bigl((\pi/L)^2 - \kappa\bigr).$$

If $L > \pi/\sqrt{\kappa}$, the right side is negative: at least one of the $L_i''(0)$ is negative. So $\gamma$ is not a length-minimiser — contradicting that it joined its endpoints minimally.

**The bolded mechanism summary: the Ricci bound $\mathrm{Ric} \ge (n-1)\kappa g$ combined with the variation $J = \sin(\pi s/L)e$ makes the second variation of arc length negative for $L > \pi/\sqrt{\kappa}$, summed over $n - 1$ orthogonal parallel normal fields — forcing a conjugate point in the interior of any geodesic longer than $\pi/\sqrt{\kappa}$.**

Compactness is then: complete + bounded diameter = compact (Hopf–Rinow). Finite $\pi_1$: the universal cover $\widetilde M$ has the same Ricci hypothesis (covering is local isometry), so $\widetilde M$ is also compact. The covering map $\widetilde M \to M$ between two compact manifolds has finite degree, equal to $|\pi_1(M)|$.

---

# What Makes This Hard

The technical heart is the choice of the variation field $J(s) = \sin(\pi s/L)e$. The sine function is chosen because it vanishes at $s = 0$ and $s = L$ (so $J$ is a permissible variation field for fixed endpoints) and because its second derivative is $-(\pi/L)^2\sin$, so the $|\nabla_T J|^2$ term integrates against itself in a way matched to the trigonometric identity $\sin^2 + \cos^2 = 1$. The factor $\pi/L$ in the frequency is *forced* by the fixed-endpoint condition.

The summing over $n - 1$ orthonormal directions is the move that converts the per-direction sectional-curvature bound into the per-trace Ricci bound. The trick is that **summing the second variations over a parallel orthonormal frame produces the Ricci tensor**, which is the natural object to control via the hypothesis.

The most common error in the proof: forgetting that $\sum_i K(T \wedge e_i) = \mathrm{Ric}(T, T)$ requires $e_i$ to be *orthogonal to $T$*. If you sum over a frame including $T$ itself, you get $\mathrm{Ric}(T, T) + K(T \wedge T) = \mathrm{Ric}(T, T) + 0$. The $n - 1$ orthonormal normal directions are exactly what is needed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use the Jacobi-field-based second variation of arc length. Choose the variation field $J = \sin(\pi s/L)e$ for a parallel unit normal $e$. Sum over $n - 1$ orthonormal parallel normals; use $\mathrm{Ric} \ge (n-1)\kappa$ to show the summed second variation is negative when $L > \pi/\sqrt{\kappa}$. Conclude no minimising geodesic can be longer than $\pi/\sqrt{\kappa}$; hence diameter bound, hence compactness, hence finite $\pi_1$ via universal-cover argument.

**Subgoal decomposition:**

1. **Second variation formula along a geodesic.**
   - *Hint:* For a normal variation $J$ along an arc-length geodesic $\gamma$ of length $L$, $L''(0) = \int_0^L(|\nabla_T J|^2 - \langle R(J, T)T, J\rangle)ds$.
   - *Why needed:* The fundamental tool of variational Riemannian geometry, applied here to extract a curvature inequality.

2. **Choose the variation $J = \sin(\pi s/L)\,e$ for parallel $e \perp T$.**
   - *Hint:* This $J$ vanishes at both endpoints and has $|\nabla_T J|^2 = (\pi/L)^2\cos^2(\pi s/L)$.
   - *Why needed:* Cleanest choice that integrates against the curvature term via trigonometric identities.

3. **Sum over an orthonormal parallel frame of normals.**
   - *Hint:* Summing $\sum_i K(T \wedge e_i) = \mathrm{Ric}(T, T)$ over $n - 1$ orthonormal normal $e_i$ converts per-plane curvature into per-direction Ricci.
   - *Why needed:* This is what lets us replace the per-plane $K$ hypothesis with the per-trace Ricci hypothesis.

4. **Negative summed second variation $\implies$ non-minimising.**
   - *Hint:* If $\sum L_i''(0) < 0$, at least one $L_i''(0) < 0$, so that variation shortens $\gamma$.
   - *Why needed:* Connects the analytic inequality to the geometric statement.

5. **Bound diameter and apply to the universal cover.**
   - *Hint:* No minimising geodesic longer than $\pi/\sqrt{\kappa}$ $\implies$ no pair of points farther apart than that $\implies$ diameter bound. Compactness from completeness + bounded diameter (Hopf–Rinow). Finite $\pi_1$ from same hypothesis on universal cover.
   - *Why needed:* Final structural conclusions.

---

# Lemma Decomposition

> [!note]- Lemma 1: Second variation of arc length with parallel normal variation field
> **Statement:** For an arc-length geodesic $\gamma : [0, L] \to M$ and a parallel unit vector field $e \perp T$ along $\gamma$, with variation field $J(s) = f(s)e(s)$ where $f(0) = f(L) = 0$,
> $$L''(0) = \int_0^L\bigl(f'(s)^2 - f(s)^2 K(T \wedge e)\bigr)ds.$$
>
> **Hint:** Apply the general second variation formula and use $\nabla_T e = 0$ (parallel) to get $\nabla_T J = f'(s)e$ and $|\nabla_T J|^2 = f'(s)^2|e|^2 = f'(s)^2$; expand $\langle R(J, T)T, J\rangle = f^2\langle R(e, T)T, e\rangle = f^2 K(T \wedge e)$.
>
> **Why needed:** Specialises the second variation to the form that will be used.
>
> > [!note]- Full proof
> > Standard second variation: $L''(0) = \int_0^L(|\nabla_T J|^2 - \langle R(J, T)T, J\rangle)ds + \text{(boundary term)}$. Boundary term vanishes because $J(0) = J(L) = 0$ (the variation fixes endpoints). $J = fe$: $\nabla_T J = f'e + f\nabla_T e = f'e$ since $e$ parallel. $|\nabla_T J|^2 = f'^2$. $\langle R(J, T)T, J\rangle = f^2\langle R(e, T)T, e\rangle = f^2 K(T \wedge e)$ since $|e| = 1, |T| = 1, e \perp T$.

> [!note]- Lemma 2: $f(s) = \sin(\pi s/L)$ choice and the integral identity
> **Statement:** With $f(s) = \sin(\pi s/L)$, the integral in Lemma 1 evaluates to
> $$L''(0) = \tfrac{L}{2}\bigl((\pi/L)^2 - K(T \wedge e)\bigr)$$
> if $K(T \wedge e)$ is constant along $\gamma$. (In general, replace $K(T \wedge e)$ with its $\sin^2$-weighted average.)
>
> **Hint:** $\int_0^L \cos^2(\pi s/L)ds = \int_0^L\sin^2(\pi s/L)ds = L/2$.
>
> **Why needed:** Quantitative form of the second variation.
>
> > [!note]- Full proof
> > $f'(s) = (\pi/L)\cos(\pi s/L)$, $f'(s)^2 = (\pi/L)^2\cos^2$. $\int_0^L f'^2 ds = (\pi/L)^2 \cdot L/2 = \pi^2/(2L)$. $\int_0^L f^2 K(T \wedge e)ds = K(T \wedge e)\cdot L/2$ (in the constant case; for varying $K$, this is the $\sin^2$-weighted average times $L/2$). So $L''(0) = \pi^2/(2L) - K(T \wedge e)\cdot L/2 = (L/2)((\pi/L)^2 - K(T \wedge e))$.

> [!note]- Lemma 3: Sum over orthonormal parallel normal frame gives Ricci
> **Statement:** Choose $n - 1$ orthonormal parallel vector fields $e_1, \ldots, e_{n-1}$ along $\gamma$ with $e_i \perp T$. Summing Lemma 2 over $i$:
> $$\sum_{i=1}^{n-1} L_i''(0) = (n-1)\tfrac{\pi^2}{2L} - \tfrac{L}{2}\sum_{i=1}^{n-1}\overline{K(T \wedge e_i)} \le (n-1)\tfrac{L}{2}\bigl((\pi/L)^2 - \kappa\bigr)$$
> using $\mathrm{Ric}(T, T) = \sum_i K(T \wedge e_i) \ge (n-1)\kappa$.
>
> **Hint:** Parallel transport preserves orthonormality; an initial orthonormal basis of $T_p\gamma^\perp$ extends to an orthonormal parallel frame along $\gamma$. The sum $\sum K(T \wedge e_i) = \mathrm{Ric}(T, T)$.
>
> **Why needed:** Converts the per-plane sectional curvature into the per-direction Ricci.
>
> > [!note]- Full proof
> > Parallel transport along $\gamma$ is an orthogonal map $T_{\gamma(0)}M \to T_{\gamma(s)}M$ preserving the metric. Starting with an orthonormal basis $\{T(0), e_1(0), \ldots, e_{n-1}(0)\}$ of $T_{\gamma(0)}M$ with $e_i \perp T(0)$, parallel transport gives an orthonormal parallel frame along $\gamma$. The $e_i$ remain $\perp T$ since $\langle T, e_i\rangle$ is constant along $\gamma$ (both parallel) and starts at $0$.
> > 
> > $\sum_{i=1}^{n-1}K(T(s) \wedge e_i(s)) = \sum_i\langle R(e_i, T)T, e_i\rangle = \mathrm{tr}_{T^\perp}(R(\cdot, T)T) = \mathrm{Ric}(T, T)$ (using the orthonormal-frame definition of Ricci). For each $s$, $\mathrm{Ric}(T(s), T(s)) \ge (n-1)\kappa$. Integrating with weight $\sin^2$ and summing gives the displayed bound.

> [!note]- Lemma 4: $L > \pi/\sqrt{\kappa}$ forces a non-minimising geodesic
> **Statement:** If $L > \pi/\sqrt{\kappa}$, then $(\pi/L)^2 < \kappa$, so $\sum L_i''(0) < 0$. Hence at least one $L_i''(0) < 0$, meaning the variation in the $e_i$-direction shortens $\gamma$ — so $\gamma$ is not length-minimising.
>
> **Hint:** Bound the summed second variation; pigeonhole.
>
> **Why needed:** Sets up the contradiction with minimality.
>
> > [!note]- Full proof
> > By Lemma 3, $\sum L_i''(0) \le (n-1)(L/2)((\pi/L)^2 - \kappa)$. If $L > \pi/\sqrt{\kappa}$, then $(\pi/L)^2 < \kappa$, so $(\pi/L)^2 - \kappa < 0$, so the sum is negative. By pigeonhole, at least one $L_i''(0) < 0$. The corresponding variation strictly shortens $\gamma$ to second order, so $\gamma$ is not a local minimum of length — in particular, not a global length-minimiser.

> [!note]- Lemma 5: Diameter bound + compactness + finite $\pi_1$
> **Statement:** (a) $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$. (b) $M$ is compact. (c) $\pi_1(M)$ is finite.
>
> **Hint:** (a): Any two points $p, q$ are joined by a minimising geodesic (Hopf–Rinow), which by Lemma 4 has length $\le \pi/\sqrt{\kappa}$. (b): Complete + bounded $\Rightarrow$ compact (Hopf–Rinow). (c): Universal cover $\widetilde M$ has the same hypothesis, so is compact, so finite covering degree $|\pi_1(M)|$.
>
> **Why needed:** Final conclusions.
>
> > [!note]- Full proof
> > **(a)** By Hopf–Rinow, any two points $p, q \in M$ are joined by a length-minimising geodesic $\gamma$. By Lemma 4, $\mathrm{length}(\gamma) \le \pi/\sqrt{\kappa}$. So $d(p, q) = \mathrm{length}(\gamma) \le \pi/\sqrt{\kappa}$ for all $p, q$, giving the diameter bound.
> > **(b)** By Hopf–Rinow's "Heine–Borel" half, $M$ complete + metrically bounded (which follows from finite diameter) $\Rightarrow$ $M$ compact.
> > **(c)** The universal cover $\widetilde M$ with the pulled-back metric $\tilde g$ is also complete (covering of complete is complete) and satisfies the same Ricci bound (covering is local isometry). By (a) and (b), $\widetilde M$ is also compact with diameter $\le \pi/\sqrt{\kappa}$. The covering map $\widetilde M \to M$ between two compact manifolds has finite degree, which equals $|\pi_1(M)|$. Hence $\pi_1(M)$ is finite.

---

# Formal Proof

> [!note]- Complete formal proof
> Suppose for contradiction $\mathrm{diam}(M) > \pi/\sqrt{\kappa}$. Then there exist $p, q \in M$ with $d(p, q) > \pi/\sqrt{\kappa}$. By the Hopf–Rinow theorem (which uses completeness), there is a minimising geodesic $\gamma : [0, L] \to M$ from $p$ to $q$ with $L = d(p, q) > \pi/\sqrt{\kappa}$.
>
> Apply Lemmas 1–4 to this minimising geodesic $\gamma$. By Lemma 4, $\sum L_i''(0) < 0$ for the variations $J_i = \sin(\pi s/L)e_i$ with $e_i$ a parallel orthonormal frame of normals. At least one $L_i''(0) < 0$, so the corresponding variation shortens $\gamma$ — contradicting minimality.
>
> Hence $\mathrm{diam}(M) \le \pi/\sqrt{\kappa}$. Compactness follows from Hopf–Rinow (complete + bounded). Finite $\pi_1$ follows by applying the same argument to the universal cover (Lemma 5).

---

# Cross-Field Exercise Suggestions

1. **The Penrose–Hawking singularity theorems in GR.** In general relativity, the **strong energy condition** $\mathrm{Ric}(v, v) \ge 0$ for timelike $v$ combined with global hypotheses (existence of a closed trapped surface, etc.) leads to **singularity theorems** stating that geodesics in the spacetime must be incomplete. The proofs use the same Jacobi-field-conjugate-point analysis as Bonnet–Myers, adapted to Lorentzian signature. See **Wald**, *General Relativity*, Ch. 9, or **Hawking–Ellis**, *The Large Scale Structure of Spacetime*.

2. **Bochner vanishing of $b_1$.** On a compact manifold with $\mathrm{Ric} > 0$, the first Betti number $b_1(M) = 0$ — a strengthening of Bonnet–Myers's finite-$\pi_1$ conclusion in the abelianisation. Proof: the **Bochner formula** for harmonic $1$-forms is $\tfrac{1}{2}\Delta|\omega|^2 = |\nabla\omega|^2 + \mathrm{Ric}(\omega^\sharp, \omega^\sharp)$; integrating over $M$ and using $\mathrm{Ric} > 0$ forces $\omega = 0$, so no harmonic 1-forms, so $b_1 = 0$ by Hodge theory. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

3. **Compact homogeneous spaces.** Any compact connected Lie group $G$ with a left-invariant Riemannian metric of positive Ricci curvature satisfies Bonnet–Myers. Examples include $\mathrm{SO}(n+1)/\mathrm{SO}(n) = S^n$, $\mathrm{SU}(n+1)/\mathrm{S}(\mathrm{U}(n)\mathrm{U}(1)) = \mathbb{CP}^n$, and the **Wallach manifolds** (positively curved flag manifolds). These provide a rich source of examples where Bonnet–Myers's conclusions are tight.

---

# Bridges

- **Cartan–Hadamard (opposite-sign analogue).** [[Thm - Cartan-Hadamard Theorem|Cartan–Hadamard]] handles $K \le 0$ (with simple connectedness): the conclusion is that $M$ is diffeomorphic to $\mathbb{R}^n$ — infinite diameter, $\pi_1 = 0$. Bonnet–Myers handles $\mathrm{Ric} > 0$ (no simple connectedness needed): the conclusion is finite diameter, compact, finite $\pi_1$. The two theorems are mirror images; both use the Jacobi-field-second-variation machinery, with curvature sign flipping the convexity-vs-oscillation behaviour of $|J|^2$.

- **Bishop–Gromov volume comparison.** A quantitative refinement: under $\mathrm{Ric} \ge (n-1)\kappa g$, the volume of a geodesic ball $B_r(p) \subset M$ is bounded above by the corresponding volume in the constant-curvature model space $S^n_\kappa$. **Bishop–Gromov** integrates the per-direction Ricci bound to a global volume bound, and combined with Bonnet–Myers's diameter bound gives the **Gromov compactness theorem**: the collection of all complete $n$-Riemannian manifolds with $\mathrm{Ric} \ge (n-1)\kappa g$ and $\mathrm{diam} \le D$ is precompact in the Gromov–Hausdorff topology.

- **Bochner vanishing theorem.** On a compact Riemannian manifold with $\mathrm{Ric} > 0$, the first Betti number $b_1 = 0$ — sharpening Bonnet–Myers's finite-$\pi_1$ to no torsion-free part of $\pi_1$'s abelianisation. The mechanism is the **Bochner formula** integrated by parts; see [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

- **Sphere theorem and Brendle–Schoen.** A simply-connected complete manifold with strictly $1/4$-pinched sectional curvature ($1/4 < K \le 1$) is diffeomorphic to $S^n$ — the **differentiable sphere theorem** of **Brendle–Schoen** (2009) via Ricci flow. Bonnet–Myers is the much weaker statement that such a manifold has finite diameter and finite $\pi_1$; the sphere theorem is a sharpening that requires far more (Ricci-flow analysis of positive-curvature-operator preservation).

- **Singularity theorems in general relativity.** Penrose ($1965$) and Hawking ($1965$, $1967$) showed that under the strong energy condition (a Lorentzian Ricci positivity) and a trapped-surface condition, spacetime contains incomplete timelike or null geodesics — **singularities**. The proof structurally mirrors Bonnet–Myers: positive Ricci forces conjugate points along long geodesics, which combined with global topology rules out completeness. See [[General Relativity I — Einstein's Equations and Schwarzschild]] for the GR machinery.
