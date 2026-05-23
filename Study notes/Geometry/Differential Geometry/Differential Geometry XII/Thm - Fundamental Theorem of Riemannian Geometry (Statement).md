---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Semi-Riemannian Metric and Signature"
  - "Def - Vector Field on a Manifold"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, differential-geometry, riemannian-geometry, connections]
---

# Notation

$(M, g)$ — a (semi-)Riemannian manifold. $\nabla$ — a connection on $TM$: an $\mathbb{R}$-bilinear operation $(X, Y) \mapsto \nabla_X Y$ from $\mathfrak{X}(M) \times \mathfrak{X}(M)$ to $\mathfrak{X}(M)$ satisfying $\nabla_{fX}Y = f \nabla_X Y$ (tensorial in $X$) and the Leibniz rule $\nabla_X(fY) = X(f) Y + f \nabla_X Y$ (derivation in $Y$) for $f \in C^\infty(M)$. The **Christoffel symbols** of a connection in a chart are $\Gamma^k_{ij}$, defined by $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Statement

> **Theorem (Fundamental Theorem of Riemannian Geometry — Statement).** Let $(M, g)$ be a Riemannian (or semi-Riemannian) manifold. There exists a unique connection $\nabla$ on $TM$ that is both
>
> (i) **torsion-free**: $\nabla_X Y - \nabla_Y X = [X, Y]$ for all vector fields $X, Y$;
>
> (ii) **metric-compatible**: $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ for all vector fields $X, Y, Z$.
>
> This unique connection is the **Levi-Civita connection** of $(M, g)$. It is characterised by the **Koszul formula**:
> $$
> 2 g(\nabla_X Y, Z) = X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X).
> $$

We state this without proof; the full proof, and the entire development of the Levi-Civita connection (geodesics, parallel transport, curvature, exponential map) is the content of a future "Riemannian Geometry I" topic.

---

# Motivation

A Riemannian metric installs an inner product on every tangent space, which is enough for *static* notions — length, angle, distance, gradient. But for *dynamic* notions — how to differentiate a vector field along a curve, how to compare tangent vectors at different points, what a "straight line" is on a curved manifold — the metric alone is not enough. We need a **connection**: an additional piece of data that tells us how to differentiate vector fields.

The trouble is that there are *many* connections on $TM$. The space of connections is an affine space (the difference of two connections is a tensor field, the **difference tensor**), so given any one connection, the others form a huge family parametrised by tensor fields. Choosing a connection is therefore choosing one out of an infinite-dimensional family. This is unsatisfactory: without a canonical choice, every construction depending on the connection (geodesics, curvature, parallel transport) becomes ambiguous.

The fundamental theorem resolves this completely: among all connections, *exactly one* is "compatible with the metric" in the two precise senses of torsion-freeness and metric-compatibility. So the metric *selects* a canonical connection — the **Levi-Civita connection** — and all of Riemannian geometry (geodesics, curvature, exponential map, Bonnet–Myers, Cartan–Hadamard, ...) refers to this canonical choice.

The two conditions are not arbitrary; each has a clean geometric meaning:

- **Torsion-free** ($\nabla_X Y - \nabla_Y X = [X, Y]$): the connection's antisymmetric part is the Lie bracket, which is forced by the smooth structure alone. Equivalently, the Christoffel symbols are symmetric in their lower indices: $\Gamma^k_{ij} = \Gamma^k_{ji}$. This is the condition that "second mixed partial derivatives commute" in the connection's calculus.

- **Metric-compatible** (Leibniz rule for the metric): parallel transport along any curve preserves the inner product of vectors. So lengths, angles, and orthogonality are preserved by parallel transport — the metric is "constant" with respect to $\nabla$.

The Koszul formula gives an explicit expression for $\nabla_X Y$ in terms of the metric and Lie brackets alone, so the construction is fully concrete: the metric *determines* the connection, no further choices required.

This theorem is the cornerstone of Riemannian geometry. Without it, every notion downstream (geodesics, curvature, etc.) would be ambiguous; with it, everything is canonical.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: A Riemannian metric.* The hypothesis. Once you have $g$, the theorem gives you a connection for free, and via it everything else.

*Source 2: A semi-Riemannian metric.* The theorem holds for any non-degenerate symmetric $(0, 2)$-tensor field, not just positive-definite ones. So Lorentzian manifolds also have a unique Levi-Civita connection, and the entire Riemannian-geometry machinery transfers to general relativity. This is what makes the Einstein field equations possible: they involve the Ricci tensor of the Levi-Civita connection of the Lorentzian metric.

*Source 3: Implicit: a manifold-intrinsic notion of differentiation.* The theorem gives a notion of "how to differentiate a vector field along a curve" that is *manifold-intrinsic* — does not depend on a choice of embedding or chart. This is significant: ordinary calculus in $\mathbb{R}^n$ has the standard derivative built in, but a generic manifold has no a priori differentiation; the metric supplies one via the Levi-Civita connection.

**Targets (Output Amplification)**

*Target combination 1: Levi-Civita connection + curve gives geodesic equation.* A **geodesic** is a curve $\gamma$ with $\nabla_{\dot\gamma}\dot\gamma = 0$ — the velocity is parallel-transported along the curve. In coordinates this becomes $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$, the **geodesic equation**. Combining the existence of the Levi-Civita connection with the existence-and-uniqueness theorem for ODEs gives existence and uniqueness of geodesics with given initial position and velocity. This is the entry point into the variational and dynamical study of Riemannian manifolds.

*Target combination 2: Levi-Civita connection + commutator gives curvature.* The **Riemann curvature tensor** is $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]} Z$, measuring the failure of $\nabla$ to commute. From it: **sectional curvature** (curvature of a 2-plane), **Ricci tensor** (a trace), **scalar curvature** (further trace). The entire curvature theory of Riemannian geometry is built on the Levi-Civita connection.

*Target combination 3: Levi-Civita on a Lie group with bi-invariant metric.* For a Lie group $G$ with a bi-invariant Riemannian metric, the Levi-Civita connection has the elegant formula $\nabla_X Y = \tfrac{1}{2}[X, Y]$ for left-invariant vector fields $X, Y$. The geodesics through the identity are one-parameter subgroups, and the Riemannian exponential map coincides with the Lie-group exponential of [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]]. This is the bridge between Lie theory and Riemannian geometry.

---

# Why Is It True

**Mechanism summary:** **the Koszul formula determines $g(\nabla_X Y, Z)$ uniquely from the metric and Lie brackets, and non-degeneracy of $g$ then determines $\nabla_X Y$ itself uniquely. Existence is by setting $\nabla$ according to the formula; uniqueness is by symmetrising the conditions.**

The proof, which we do not give in full here, runs as follows. *Uniqueness:* Suppose $\nabla$ satisfies both conditions. Apply metric-compatibility to permutations of $(X, Y, Z)$:
$$
X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z),
$$
$$
Y g(Z, X) = g(\nabla_Y Z, X) + g(Z, \nabla_Y X),
$$
$$
-Z g(X, Y) = -g(\nabla_Z X, Y) - g(X, \nabla_Z Y).
$$
Add them and use torsion-freeness ($\nabla_X Y - \nabla_Y X = [X, Y]$) to eliminate cross terms; the result is the Koszul formula:
$$
2 g(\nabla_X Y, Z) = X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X).
$$
This determines $g(\nabla_X Y, Z)$ for every $Z$, and non-degeneracy of $g$ then determines $\nabla_X Y$ uniquely.

*Existence:* The right-hand side of the Koszul formula is $C^\infty(M)$-linear in $Z$ (because the Lie brackets cancel out the $Z$-derivatives at the right level), so it defines a smooth 1-form for each $X, Y$. Apply the [[Def - Musical Isomorphism (Flat and Sharp)|sharp map]] to convert to a vector field $\nabla_X Y$. Check that the resulting $\nabla$ is a connection (tensorial in $X$, derivation in $Y$), torsion-free, and metric-compatible. The verification is mechanical but uses the symmetries of the Koszul formula essentially.

The decisive insight is that **the two conditions overdetermine the connection just enough** — there are exactly enough constraints to pin down all $n^3$ Christoffel symbols (or equivalently, all values of $\nabla_X Y$), and the two conditions are precisely compatible (no inconsistency, no further freedom). This is a remarkable algebraic coincidence: a smaller condition would be underdetermined, a larger one would be over-determined. The torsion-free and metric-compatible conditions hit the sweet spot.

---

# What Makes This Hard

The conceptual difficulty is **seeing why the two conditions together determine $\nabla$ uniquely, when neither alone does**. There are torsion-free connections that are not metric-compatible (e.g., on $\mathbb{R}^n$ with a non-Euclidean Riemannian metric, the connection $\nabla_{\partial_i}\partial_j = 0$ is torsion-free but not metric-compatible with a non-trivial $g$). There are metric-compatible connections that are not torsion-free (start with the Levi-Civita and add a non-zero antisymmetric difference tensor; the result is still metric-compatible if the antisymmetric tensor is chosen carefully). The uniqueness comes from the interplay of the two conditions in the Koszul derivation, not from either one alone. Students often gloss over this and assume uniqueness is "obvious"; the calculation is where the magic happens.

The other hard part is **the explicit form of the Christoffel symbols**:
$$
\Gamma^k_{ij} = \tfrac{1}{2} g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr).
$$
Memorising this formula is a rite of passage; the symmetrisation pattern $(i, j, l)$ → $(j, i, l)$ → $-(l, i, j)$ reflects the symmetrisation of the Koszul formula and is what enforces the metric-compatibility condition. The first time one sees this formula it looks arbitrary; the Koszul derivation shows it is forced.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the proof of uniqueness; existence is then forced.**

**High-level strategy:** Symmetrise metric-compatibility over the three arguments and use torsion-freeness to eliminate cross terms; obtain the Koszul formula expressing $g(\nabla_X Y, Z)$ in terms of $g$ and brackets. Then non-degeneracy of $g$ gives uniqueness of $\nabla_X Y$.

**Subgoal decomposition:**

1. **Write down three metric-compatibility equations.** $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ and the cyclic variants.
   - *Hint:* Cyclic permutation $(X, Y, Z) \to (Y, Z, X) \to (Z, X, Y)$.
   - *Why needed:* Three relations with different sign combinations give a system to solve.

2. **Add the three equations with appropriate signs.** $X g(Y, Z) + Y g(X, Z) - Z g(X, Y)$.
   - *Hint:* The sign on the third is chosen so that one of the unknowns (specifically $g(Z, \nabla_X Y)$) emerges, while others cancel.
   - *Why needed:* Isolates the desired quantity.

3. **Apply torsion-freeness to convert remaining $\nabla$ terms to Lie brackets.** $\nabla_X Y - \nabla_Y X = [X, Y]$, hence $g(\nabla_Y X, Z) = g(\nabla_X Y, Z) - g([X, Y], Z)$ etc.
   - *Hint:* This is where torsion-freeness enters; it lets you reduce different orderings of $\nabla_a b$ to a single ordering plus a Lie bracket.
   - *Why needed:* Eliminates the unknown cross terms.

4. **Read off the Koszul formula.** $2g(\nabla_X Y, Z) = X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X)$.
   - *Hint:* The factor of $2$ comes from collecting $\nabla_X Y$ from both the first and second metric-compatibility equations.
   - *Why needed:* The explicit formula for $\nabla$ in terms of $g$.

5. **Uniqueness follows from non-degeneracy.** $g(\nabla_X Y, Z)$ is determined for every $Z$ by Koszul; non-degeneracy then determines $\nabla_X Y$.
   - *Hint:* If $g(v, Z) = g(w, Z)$ for every $Z$, then $g(v - w, Z) = 0$ for every $Z$, hence $v = w$ by non-degeneracy.
   - *Why needed:* Concludes uniqueness.

6. **Existence: define $\nabla$ by the Koszul formula and verify the conditions.** Show the resulting $\nabla$ is a connection (tensorial in $X$, derivation in $Y$), is torsion-free, and is metric-compatible.
   - *Hint:* The verifications are straightforward but require attention to how Lie brackets and metric derivatives interact.
   - *Why needed:* Completes the existence half.

---

# Lemma Decomposition

> [!note]- Lemma 1: Uniqueness of the Levi-Civita connection
> **Statement:** If two connections $\nabla, \tilde\nabla$ on $TM$ are both torsion-free and metric-compatible with respect to the same metric $g$, then $\nabla = \tilde\nabla$.
>
> **Hint:** Apply the Koszul formula. Both $\nabla$ and $\tilde\nabla$ satisfy the Koszul formula, so $g(\nabla_X Y, Z) = g(\tilde\nabla_X Y, Z)$ for all $Z$; non-degeneracy of $g$ gives $\nabla_X Y = \tilde\nabla_X Y$.
>
> **Why needed:** The uniqueness half of the fundamental theorem.
>
> > [!note]- Full proof (sketch)
> > As outlined in the rederivation scaffold: add three permuted metric-compatibility equations, use torsion-freeness to eliminate cross terms, obtain the Koszul formula. Apply to both $\nabla$ and $\tilde\nabla$; both satisfy the same Koszul formula, so $g(\nabla_X Y, Z) = g(\tilde\nabla_X Y, Z)$. By non-degeneracy of $g$, $\nabla_X Y = \tilde\nabla_X Y$. Hence $\nabla = \tilde\nabla$.

> [!note]- Lemma 2: Existence — the Koszul formula defines a connection
> **Statement:** Defining $\nabla_X Y$ via the Koszul formula (with the sharp map applied to extract a vector field from a 1-form-valued expression) gives a connection on $TM$ that is torsion-free and metric-compatible.
>
> **Hint:** Check the connection axioms (tensoriality in $X$, derivation in $Y$); the torsion-freeness and metric-compatibility properties follow from the symmetrisation built into the Koszul formula.
>
> **Why needed:** The existence half of the fundamental theorem.
>
> > [!note]- Full proof (sketch)
> > Define $\nabla_X Y$ by requiring $g(\nabla_X Y, Z)$ to equal $\tfrac{1}{2}$ times the right-hand side of the Koszul formula, then apply the sharp map (using non-degeneracy of $g$) to extract a vector field. The verifications:
> >
> > - **Tensorial in $X$**: $g(\nabla_{fX}Y, Z) = f g(\nabla_X Y, Z)$ for $f \in C^\infty(M)$, by direct check of the Koszul formula.
> > - **Derivation in $Y$**: $g(\nabla_X(fY), Z) = X(f) g(Y, Z) + f g(\nabla_X Y, Z)$, by direct check.
> > - **Torsion-free**: $g(\nabla_X Y - \nabla_Y X, Z) = g([X, Y], Z)$, by subtracting the $(X, Y)$ and $(Y, X)$ versions of the Koszul formula.
> > - **Metric-compatible**: $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$, by adding the $(X, Y, Z)$ and $(X, Z, Y)$ versions of the Koszul formula.
> >
> > Each of these is a (somewhat tedious) algebraic verification that does not require any deeper input.

---

# Formal Proof

The full proof is the content of a Riemannian Geometry course; we have provided the rederivation scaffold and lemma decomposition above. The full proof appears in Lee's *Riemannian Manifolds* (Theorem 5.10), do Carmo's *Riemannian Geometry* (Theorem 3.6), and most other standard references.

We do not include a complete formal proof here. The statement is the contribution to this chapter; the proof is the entry to the next.

---

# Cross-Field Exercise Suggestions

*1. The connection on a Lie group is determined by the metric (if bi-invariant).* For a bi-invariant Riemannian metric on a Lie group $G$, the Levi-Civita connection on left-invariant vector fields is $\nabla_X Y = \tfrac{1}{2}[X, Y]$. The geodesics through the identity are one-parameter subgroups, and the Riemannian exponential map equals the Lie group exponential. This is one of the cleanest examples of the Levi-Civita connection in action.

*2. Christoffel symbols in polar coordinates.* For $(\mathbb{R}^2 \setminus \{0\}, \bar g)$ in polar coordinates $(r, \theta)$, $g = dr^2 + r^2 d\theta^2$. Computing $\Gamma^k_{ij}$ gives the nonzero entries $\Gamma^r_{\theta\theta} = -r$, $\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = 1/r$. This is the canonical first computation that illustrates how Christoffel symbols capture the "non-trivial" part of the connection in non-Cartesian coordinates.

*3. Lorentzian Levi-Civita on Schwarzschild.* For the Schwarzschild metric in $(t, r, \theta, \varphi)$ coordinates, the Christoffel symbols can be computed explicitly. The resulting geodesic equations describe the orbits of test particles in the gravitational field of a non-rotating black hole; perihelion precession of Mercury, gravitational deflection of light, and gravitational redshift are all consequences.

*4. Connection on a vector bundle from a fibre metric.* The same construction (torsion-free metric-compatible) can be applied to any vector bundle equipped with a fibre metric, but in general the conditions are not sufficient to determine a unique connection (only the symmetric/skew-symmetric difference is constrained). The reason it works for $TM$ specifically is that the "torsion" depends on the special role of the tangent bundle (it has Lie brackets); for general vector bundles, torsion is not defined and metric-compatibility alone leaves freedom.

---

# Bridges

- **[[Def - Riemannian Metric]]** — the input. The theorem turns metric data into connection data, uniquely. Without the metric, no canonical connection on $TM$ exists; with the metric, exactly one connection is selected.

- **Levi-Civita connection** (forward bridge — page does not exist yet). The unique connection given by the theorem. From it: parallel transport, geodesic equation, curvature tensor, exponential map, all of Riemannian geometry's machinery. The page **Def - Levi-Civita Connection** is reserved for the Riemannian Geometry I topic.

- **Christoffel symbols** (forward bridge). The component form of the Levi-Civita connection in coordinates: $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. The formula reads off the symbols from the metric components, and the geodesic equation $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$ uses them directly.

- **General relativity** (forward bridge). The Lorentzian version of the theorem applies to spacetime metrics, giving the Levi-Civita connection of the Lorentzian metric and through it the **Ricci tensor** $R_{\mu\nu}$ that appears in the Einstein field equations. So the geometry of GR is the Lorentzian shadow of Riemannian geometry, built on this same theorem.

---

# Unlocked by This

> [!tip] **Levi-Civita Connection and Geodesics** *(from Riemannian Geometry)*
> The fundamental theorem hands us a unique connection, and the unfolding of Riemannian geometry begins. We sketch the development that follows; the full treatment belongs to a future **Riemannian Geometry I** topic.
>
> **Christoffel symbols.** In local coordinates the connection is encoded in the **Christoffel symbols** $\Gamma^k_{ij}$, defined by $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$. The torsion-free condition becomes $\Gamma^k_{ij} = \Gamma^k_{ji}$ (symmetric in lower indices). Metric-compatibility becomes the explicit formula
> $$
> \Gamma^k_{ij} = \tfrac{1}{2} g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr),
> $$
> reading the symbols directly off the metric and its first derivatives. This is the formula one memorises and computes from forever after — every concrete Riemannian-geometry calculation begins by computing these symbols from the metric.
>
> **Parallel transport.** Given a curve $\gamma : [a, b] \to M$ and a vector $v_0 \in T_{\gamma(a)} M$, there is a unique vector field $V(t)$ along $\gamma$ with $V(a) = v_0$ and $\nabla_{\dot\gamma} V = 0$ — the **parallel transport** of $v_0$ along $\gamma$. Equivalently, $V$ satisfies the linear ODE $\dot V^k + \Gamma^k_{ij}(\gamma(t))\, V^j \dot\gamma^i = 0$. Parallel transport gives a linear isomorphism $P_\gamma : T_{\gamma(a)}M \to T_{\gamma(b)}M$ between tangent spaces; by metric-compatibility, it is a *linear isometry* — lengths and angles are preserved. This is the formal mechanism for "comparing tangent vectors at different points": there is no canonical comparison, but a choice of path gives one, and the path-dependence of parallel transport is what is measured by curvature.
>
> **Geodesics.** A **geodesic** is a curve $\gamma$ whose velocity is parallel-transported along itself: $\nabla_{\dot\gamma}\dot\gamma = 0$. In coordinates, this is the **geodesic equation**
> $$
> \ddot\gamma^k + \Gamma^k_{ij}(\gamma(t))\dot\gamma^i\dot\gamma^j = 0.
> $$
> By the ODE existence-and-uniqueness theorem applied to this second-order system, given any $p \in M$ and $v \in T_pM$, there is a unique geodesic $\gamma_v : (-\varepsilon, \varepsilon) \to M$ with $\gamma_v(0) = p$ and $\dot\gamma_v(0) = v$ — defined on some maximal open interval. The variational characterisation: geodesics are critical points of the length functional $L_g(\gamma)$ (up to reparametrisation) and of the energy functional $E(\gamma) = \tfrac{1}{2}\int g(\dot\gamma, \dot\gamma)\, dt$ (at fixed parametrisation). Constant-speed geodesics are extrema of $E$; geodesics generalise the notion of "straight line" to curved manifolds.
>
> **The exponential map.** Define $\exp_p : V_p \subseteq T_pM \to M$ by $\exp_p(v) = \gamma_v(1)$, where $V_p$ is the set of $v$ for which $\gamma_v$ extends to parameter $1$. The exponential map is smooth and is a local diffeomorphism around $0 \in T_pM$ (with differential at $0$ equal to the identity — Gauss lemma). The local inverse gives **normal coordinates** around any point, in which $g_{ij}(p) = \delta_{ij}$ and $\Gamma^k_{ij}(p) = 0$ — the cleanest possible coordinates at one point.
>
> **The Riemann curvature tensor.** The connection $\nabla$ is in general non-commutative: $\nabla_X \nabla_Y Z \neq \nabla_Y \nabla_X Z$. The failure to commute is measured by the **Riemann curvature tensor**:
> $$
> R(X, Y)Z := \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z.
> $$
> $R$ is $C^\infty(M)$-linear in all three arguments (a tensor field, despite being defined via the connection), with components $R^l{}_{ijk}$ that capture the second derivatives of the metric. The metric is *flat* (locally Euclidean) if and only if $R = 0$. Curvature has rich symmetry properties (the **first** and **second Bianchi identities**) and is the central object of Riemannian geometry.
>
> **Sectional, Ricci, scalar curvature.** Tracing $R$ in various ways yields lower-rank tensors:
> - The **sectional curvature** in a 2-plane $\sigma \subseteq T_pM$ is $K(\sigma) = g(R(e_1, e_2)e_2, e_1) / (|e_1 \wedge e_2|_g^2)$ for an orthonormal basis $(e_1, e_2)$ of $\sigma$; this generalises the Gaussian curvature of a surface.
> - The **Ricci tensor** is $\mathrm{Ric}_{ij} = R^k{}_{ikj}$, the trace of $R$ over one index pair.
> - The **scalar curvature** is $S = g^{ij}\mathrm{Ric}_{ij}$, the full trace.
>
> Each is a "compression" of the full curvature into a simpler object, and each has its own role: sectional curvature controls comparison theorems (Toponogov, Rauch), Ricci controls volume comparison and the Bonnet–Myers theorem, and scalar curvature is the simplest curvature invariant.
>
> **Comparison theorems.** Curvature bounds yield global geometric conclusions:
> - **Bonnet–Myers theorem**: if $\mathrm{Ric} \geq (n-1)\kappa\, g$ for some $\kappa > 0$, then $M$ is compact with diameter $\leq \pi / \sqrt\kappa$.
> - **Cartan–Hadamard theorem**: if $M$ is complete, simply connected, with non-positive sectional curvature, then $\exp_p$ is a diffeomorphism $T_pM \to M$ for every $p$; in particular $M$ is diffeomorphic to $\mathbb{R}^n$.
> - **Synge's theorem**: a compact orientable even-dimensional Riemannian manifold with positive sectional curvature is simply connected.
>
> These are paradigmatic curvature-to-topology theorems and show the depth of consequences flowing from the Levi-Civita connection.
>
> **Jacobi fields.** A **Jacobi field** along a geodesic $\gamma$ is a vector field $J$ satisfying the **Jacobi equation** $\nabla_{\dot\gamma}\nabla_{\dot\gamma} J + R(J, \dot\gamma)\dot\gamma = 0$. Jacobi fields measure variations of $\gamma$ through nearby geodesics: if $\Gamma(s, t)$ is a family of geodesics with $\Gamma(0, \cdot) = \gamma$, then $\partial_s \Gamma(0, t)$ is a Jacobi field. The Jacobi equation governs how curvature spreads or focuses families of geodesics, and conjugate points (where Jacobi fields vanish) signal the breakdown of the exponential map's injectivity. The **second variation formula** for the length functional uses Jacobi fields and underlies the proof of Bonnet–Myers and the Morse index theorem.
>
> **Connection forms and Cartan's structure equations.** The Levi-Civita connection can be encoded in **connection 1-forms** $\omega^i{}_j$ (encoding $\nabla$ in terms of a moving frame) and **curvature 2-forms** $\Omega^i{}_j$ (encoding $R$). Cartan's **first structure equation** $d\theta^i + \omega^i{}_j \wedge \theta^j = 0$ encodes torsion-freeness; the **second structure equation** $d\omega^i{}_j + \omega^i{}_k \wedge \omega^k{}_j = \Omega^i{}_j$ encodes curvature. This is the language of moving frames, central to physics applications and to higher-dimensional generalisations (gauge theory, fibre bundles).
>
> All of this — Christoffel symbols, parallel transport, geodesics, exponential map, curvature, sectional/Ricci/scalar, comparison theorems, Jacobi fields, Cartan equations — is the unfolding of consequences of the single fundamental theorem above. The metric uniquely determines the connection, and the connection generates the entire geometric theory.
>
> The Lorentzian version is parallel. The same fundamental theorem holds for any non-degenerate metric, including Lorentzian, and the Lorentzian Levi-Civita connection is the connection of **general relativity**. Geodesics of a Lorentzian metric are the worldlines of free-falling particles (timelike for massive, null for light), and the Einstein field equations $R_{\mu\nu} - \tfrac{1}{2}R\, g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ relate the Ricci tensor of this connection to the matter energy–momentum tensor. The whole subject of mathematical general relativity — Schwarzschild and Kerr black holes, gravitational waves, the singularity theorems, cosmological models, the cosmic censorship conjecture — runs on the Lorentzian shadow of this development.
>
> The **Riemannian Geometry I** topic, when written, will carry out this entire development in full. For now, the fundamental theorem is the gateway, and what follows from it is the substantive content of the subject.
