---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Semi-Riemannian Metric and Signature"
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Metric-Compatible Connection"
  - "Def - Torsion Tensor"
  - "Def - Levi-Civita Connection"
  - "Thm - Koszul Formula"
tags: [geometry, riemannian-geometry, connections, levi-civita, fundamental-theorem]
---

# Notation

$(M, g)$ — a Riemannian or semi-Riemannian manifold. $\nabla$ — an affine connection on $TM$. $X, Y, Z$ — smooth vector fields. $[X, Y]$ — the Lie bracket. $g^{kl}$ — the inverse metric components. $\Gamma^k_{ij}$ — Christoffel symbols of a connection in a coordinate frame. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Statement

> **Theorem (Fundamental Theorem of Riemannian Geometry).** Let $(M, g)$ be a Riemannian or semi-Riemannian manifold. There exists a **unique** affine connection $\nabla$ on $TM$ that is both
>
> (i) **torsion-free:** $\nabla_X Y - \nabla_Y X = [X, Y]$ for all $X, Y \in \mathfrak{X}(M)$;
>
> (ii) **metric-compatible:** $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ for all $X, Y, Z \in \mathfrak{X}(M)$, equivalently $\nabla g = 0$.
>
> This unique connection is the **Levi-Civita connection** of $(M, g)$, denoted $\nabla^g$. It is characterised explicitly by the [[Thm - Koszul Formula|Koszul formula]]:
> $$
> 2g(\nabla_X Y, Z) = X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X).
> $$
> In any local coordinate chart $(x^i)$, the Christoffel symbols of $\nabla^g$ are given by the **Christoffel formula**:
> $$
> \Gamma^k_{ij} = \tfrac{1}{2}\,g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr).
> $$

---

# Motivation

A smooth manifold has tangent spaces at each point but no canonical way to compare them. An *affine connection* on $TM$ supplies the comparison (via parallel transport), but on a generic manifold there are infinitely many connections — the space of connections on $TM$ is an affine space of infinite [[Def - Dimension|dimension]]. Without further structure, there is no canonical choice.

On a *Riemannian* manifold $(M, g)$, the metric is the additional structure, and the natural question is: does the metric pick out a canonical connection? The fundamental theorem answers yes, by way of two natural conditions:

- **Torsion-freeness** is a *structural / symmetry* condition: it says that infinitesimal parallelograms close (the parallel transport of $\varepsilon X$ along $Y$ and of $\varepsilon Y$ along $X$ produce the same endpoint modulo the standard Lie-bracket correction). Equivalently, the Christoffel symbols are symmetric in their lower indices. This condition does *not* depend on $g$.

- **Metric-compatibility** is the *coupling* condition: it says the connection respects $g$, equivalently parallel transport preserves the inner product. Without this, parallel transport could rotate or scale vectors arbitrarily; with this, parallel transport is an [[Def - Isometry|isometry]]. This is the condition that ties $\nabla$ to $g$.

The remarkable structural fact — the content of this theorem — is that these two conditions together select *exactly one* connection. There are infinitely many torsion-free connections (e.g., the difference of two such is any symmetric tensor); there are infinitely many metric-compatible connections (e.g., on a Lie group with bi-invariant metric, both the Cartan-Schouten "+" and "$-$" connections are metric-compatible but neither is torsion-free for non-abelian [[Def - Group|groups]]). The two conditions together are *just enough*: a smaller condition is underdetermined, a larger condition would be inconsistent.

This theorem is the cornerstone of Riemannian geometry. Without it, every connection-dependent quantity ([[Def - Geodesic|geodesics]], parallel transport, curvature) would be ambiguous; with it, all of these are canonically determined by the metric, and the entire subsequent development — Riemannian curvature tensor, sectional/Ricci/scalar curvature, geodesic equation, exponential map, Bonnet-Myers, Cartan-Hadamard, Synge, Gauss-Bonnet — refers to *the* Levi-Civita connection of *the* metric.

The forward bridge from [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]] previewed this theorem at the end of that topic without proof; **the present chapter delivers the proof and the resulting connection**, and from this point on the entire Riemannian-geometry program (Chapters II, III, IV of [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian Geometry I]]'s sequel topics) builds on it.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypotheses are bare — a Riemannian or semi-Riemannian manifold — but recognising the theorem's applicability in disguised settings is what gives it operational power.

*Source 1: any Riemannian manifold $(M, g)$.* The direct application. The theorem guarantees a unique connection compatible with the metric. The bridge to recognise: any time you have a metric, you have a connection.

*Source 2: any semi-Riemannian (in particular Lorentzian) manifold.* The proof uses only non-degeneracy of $g$, not positive-definiteness. So the theorem applies equally to Lorentzian spacetimes in general relativity. The bridge is non-obvious because students often think Riemannian geometry is "easier" than Lorentzian — but the fundamental theorem works identically in both signatures, and the resulting Levi-Civita connection is the gravitational connection of GR.

*Source 3: any embedded submanifold of $\mathbb{R}^N$ with induced metric.* The Levi-Civita connection of the induced metric is the **tangential projection** of the flat $\mathbb{R}^N$-derivative: $\nabla^S_X Y = (\nabla^{\mathbb{R}^N}_X Y)^\top$. This is the original Levi-Civita construction (1917) and is verified by checking that the tangential projection is torsion-free and metric-compatible — both straightforward. The bridge is that "explicit submanifold construction" satisfies the abstract characterisation, so the abstract Levi-Civita and the concrete tangential projection are the same connection. See [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]] for the full treatment.

*Source 4: any Lie group with bi-invariant Riemannian metric.* On a compact Lie group (e.g., $SU(n), SO(n), \mathrm{Sp}(n)$), there exists a bi-invariant Riemannian metric (constructed by averaging any left-invariant metric over the compact group). The Koszul formula applied to left-invariant fields collapses to $\nabla_X Y = \tfrac{1}{2}[X, Y]$. The bridge is non-obvious: "bi-invariant metric on Lie group" → "Koszul formula collapses" → "Levi-Civita is half the Lie bracket". This collapse is the input to the beautiful theory of harmonic analysis on Lie groups.

**Targets (Output Amplification)**

The conclusion is the existence and uniqueness of the Levi-Civita connection. Combined with further structural inputs, this delivers:

*Target combination 1: Levi-Civita + variational characterisation ⟹ geodesics minimise length locally.* A geodesic is a curve with $\nabla_{\dot\gamma}\dot\gamma = 0$. Adding the variational characterisation (the **first variation formula** for arc length), one shows that geodesics are critical points of the length functional and locally minimising. This is the content of the **first variation formula** in [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]], and it works *only* for the Levi-Civita connection — for other torsion-free non-compatible connections, geodesics have no length-minimisation interpretation.

*Target combination 2: Levi-Civita + commutator of $\nabla$ ⟹ Riemann curvature tensor and its symmetries.* The Riemann tensor $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ has the symmetries: antisymmetric in $(X, Y)$ (from definition), antisymmetric in lowered $(a, b)$ (from metric-compatibility), pair-symmetric $R_{abcd} = R_{cdab}$ (from torsion-freeness plus metric-compatibility), and the **first Bianchi identity** $R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0$ (from torsion-freeness via the Jacobi identity). These symmetries reduce the $n^4$ components of $R$ to $\tfrac{n^2(n^2-1)}{12}$ independent ones, and they are all consequences of the fundamental theorem's two conditions. Without metric-compatibility, the pair-symmetry fails; without torsion-freeness, the first Bianchi identity fails.

*Target combination 3: Levi-Civita + Lorentzian metric ⟹ Einstein field equations.* In GR, the metric $g_{\mu\nu}$ is Lorentzian, the connection is the Levi-Civita $\nabla^g$, the Riemann tensor of $\nabla^g$ contracts to the Ricci tensor $R_{\mu\nu}$, and the **Einstein field equations** $R_{\mu\nu} - \tfrac{1}{2}R g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$ couple this Ricci tensor to the matter energy-momentum. The contracted second Bianchi identity $\nabla_\mu G^{\mu\nu} = 0$ — a consequence of the structure of the Levi-Civita curvature — automatically gives the **conservation law** $\nabla_\mu T^{\mu\nu} = 0$. The bridge: "the Lorentzian Levi-Civita connection delivers the curvature tensor whose Bianchi identity automatically enforces conservation of energy-momentum". Full development in [[General Relativity I — Einstein's Equations and Schwarzschild]].

*Target combination 4: Levi-Civita on Kähler manifold + complex structure ⟹ holomorphic / antiholomorphic decomposition.* On a Kähler manifold $(M, g, J)$ with complex structure $J$ such that $\nabla^g J = 0$, the Christoffel symbols are "type-pure": $\Gamma^\alpha_{\beta\gamma}$ vanishes unless all three indices are holomorphic or all three are antiholomorphic. This dramatically simplifies computations in complex geometry and is the foundation of Hodge theory on Kähler manifolds, the Calabi conjecture, and **Calabi-Yau geometry**. The bridge: "Levi-Civita + Kähler structure ⟹ type decomposition". Full development in **Calabi-Yau geometry** (forward reference, beyond the current vault scope).

---

# Why Is It True

**Mechanism summary:** **the Koszul formula determines $g(\nabla_X Y, Z)$ uniquely from $g$ and Lie brackets, and the non-degeneracy of $g$ then determines $\nabla_X Y$ itself. The two conditions (torsion-free + metric-compatible) overdetermine the connection by exactly the right amount — a smaller condition is underdetermined, a larger one is inconsistent.**

The intuition: metric-compatibility gives one identity relating six $\nabla$-terms, $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$. There are three such identities — one for each cyclic permutation of $(X, Y, Z)$. Three identities in six unknowns is underdetermined, but torsion-freeness $\nabla_Y X = \nabla_X Y - [X, Y]$ reduces the six unknowns to three "canonically ordered" ones (where the first slot of $\nabla$ is the "earliest" argument). Three identities in three unknowns has a unique solution, which is the Koszul formula. So the structural miracle is: **(three permuted metric-compatibility identities) + (torsion-freeness as constraint reducer) = (one explicit formula determining $\nabla$)**. The factor of $2$ in the Koszul formula reflects the fact that $g(\nabla_X Y, Z)$ appears in two of the three permuted identities.

A different way to see it: the antisymmetric part of $\nabla$ (the torsion) and the symmetric part of $\nabla$ (the "metric-derivative part") are two independent pieces, each of dimension $\tfrac{1}{2}n^2(n+1)$ (symmetric part) and $\tfrac{1}{2}n^2(n-1)$ (antisymmetric part). Setting torsion to zero kills the antisymmetric part. Metric-compatibility then determines the symmetric part uniquely (the inhomogeneous equation $\nabla g = 0$ has a unique solution in the symmetric Christoffel symbols, given by the Christoffel formula). So the two conditions decouple: torsion-free kills antisymmetric Christoffels, and metric-compatible determines the symmetric Christoffels.

---

# What Makes This Hard

The conceptual difficulty is **seeing why two innocuous-looking conditions select a unique connection**. Each condition alone is hugely underdetermined — there are infinite-dimensional families of torsion-free connections and infinite-dimensional families of metric-compatible connections. The conjunction is what selects the unique Levi-Civita connection, and the proof shows that the two conditions interact precisely (via the Koszul-formula symmetrisation) to overdetermine $\nabla$ by exactly the right amount. Students often gloss over uniqueness and accept it as obvious; the calculation is where the magic happens.

The mechanical hard part is the **symmetrisation move** in the Koszul derivation. Three cyclic permutations of metric-compatibility, added with signs $(+, +, -)$, with torsion-freeness used to eliminate cross terms, give exactly the Koszul formula. The choice of signs is what makes it work — try the same calculation with signs $(+, +, +)$ and you get nonsense; the asymmetry is what isolates $g(\nabla_X Y, Z)$. Students typically need to do the calculation twice to see why the signs are forced.

The third hard part is **verifying that defining $\nabla$ by the Koszul formula gives an honest connection**. After defining $\nabla_X Y$ via Koszul plus the sharp map, one must check four properties: $C^\infty$-linearity in $X$, Leibniz in $Y$, torsion-freeness, metric-compatibility. Each is a separate algebraic verification; the last two are easy (immediate from the symmetries of the Koszul formula); the first two require careful Leibniz manipulations of the function-derivative and bracket terms.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** *Uniqueness:* Apply Koszul-symmetrisation to any torsion-free metric-compatible connection to derive the Koszul formula. Any two such connections agree on the inner product $g(\nabla_X Y, Z)$ for all $Z$, hence agree by non-degeneracy. *Existence:* Define $\nabla_X Y$ to be the vector with $g(\nabla_X Y, Z) = \tfrac{1}{2}K(Z)$ where $K$ is the right side of Koszul. Verify the connection axioms and the two conditions by direct manipulation.

**Subgoal decomposition:**

1. **Uniqueness via Koszul.** Show that any torsion-free metric-compatible connection satisfies the Koszul formula. Conclude that any two such connections agree on $g(\nabla_X Y, Z)$ for every $Z$, and so are equal by non-degeneracy.
   - *Hint:* See the Koszul-formula proof; the symmetrisation move with signs $(+, +, -)$.
   - *Why needed:* This is uniqueness.

2. **Define $\nabla$ via the Koszul formula.** For $X, Y \in \mathfrak{X}(M)$, define $\nabla_X Y$ to be the unique vector field $V$ with $g(V, Z) = \tfrac{1}{2}K^{X, Y}(Z)$ for all $Z$. Well-definedness requires (a) $K^{X, Y}(\cdot)$ is $C^\infty(M)$-linear in $Z$ (so it is a 1-form), and (b) non-degeneracy of $g$ to convert the 1-form to a vector field via the sharp map.
   - *Hint:* See Lemma 1 of [[Thm - Koszul Formula]] for the $C^\infty$-linearity check.
   - *Why needed:* This is the candidate connection.

3. **Verify the connection axioms.** Show that $\nabla$ defined this way is $C^\infty(M)$-linear in $X$ and a Leibniz derivation in $Y$.
   - *Hint:* Replace $X \to fX$ and $Y \to fY$ in the Koszul formula and track the function-derivative terms; they precisely produce the required Leibniz behaviour.
   - *Why needed:* The candidate must actually be a connection.

4. **Verify torsion-freeness.** Show $\nabla_X Y - \nabla_Y X = [X, Y]$ by directly subtracting the Koszul formulas for $\nabla_X Y$ and $\nabla_Y X$ and using the antisymmetry $g([Y, X], Z) = -g([X, Y], Z)$.
   - *Hint:* The function-derivative terms are symmetric in $X, Y$; the bracket terms collect to $2g([X, Y], Z)$.
   - *Why needed:* The candidate must satisfy condition (i).

5. **Verify metric-compatibility.** Show $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ by adding Koszul formulas for $\nabla_X Y$ and $\nabla_X Z$ (note the second has arguments $(X, Z, Y)$ in the slots) and verifying the result is $X g(Y, Z)$.
   - *Hint:* The bracket terms cancel via antisymmetry of brackets.
   - *Why needed:* The candidate must satisfy condition (ii).

6. **The Christoffel formula in coordinates.** Apply the Koszul formula in a coordinate frame ($X = \partial_i, Y = \partial_j, Z = \partial_l$) using $[\partial_i, \partial_j] = 0$ and the fact that $g(\nabla_{\partial_i}\partial_j, \partial_l) = \Gamma^k_{ij}g_{kl}$. Solve for $\Gamma^k_{ij}$.
   - *Hint:* Lie brackets all vanish; only function-derivative terms remain.
   - *Why needed:* This gives the explicit coordinate formula one uses in practice.

---

# Lemma Decomposition

> [!note]- Lemma 1: Uniqueness via the Koszul formula
> **Statement:** If $\nabla, \tilde\nabla$ are two torsion-free metric-compatible connections on $(M, g)$, then $\nabla = \tilde\nabla$.
>
> **Hint:** Both connections satisfy the Koszul formula $2g(\nabla_X Y, Z) = K(Z)$ with the same right-hand side $K(Z)$ depending only on $g$ and Lie brackets. So $g(\nabla_X Y - \tilde\nabla_X Y, Z) = 0$ for every $Z$, and non-degeneracy of $g$ forces $\nabla_X Y = \tilde\nabla_X Y$.
>
> **Why needed:** This is the uniqueness half of the theorem.
>
> > [!note]- Full proof
> > By the Koszul formula derivation (see the Formal Proof below or the proof of [[Thm - Koszul Formula]]), any torsion-free metric-compatible connection $\nabla$ satisfies
> > $$
> > 2g(\nabla_X Y, Z) = X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X)
> > $$
> > for all $X, Y, Z$. The right-hand side depends only on $g$ and Lie brackets — not on $\nabla$. Applied to two such connections $\nabla, \tilde\nabla$:
> > $$
> > 2g(\nabla_X Y, Z) = 2g(\tilde\nabla_X Y, Z) \implies g(\nabla_X Y - \tilde\nabla_X Y, Z) = 0 \quad \forall Z.
> > $$
> > By non-degeneracy of $g$, this forces $\nabla_X Y - \tilde\nabla_X Y = 0$, hence $\nabla_X Y = \tilde\nabla_X Y$. This holds for arbitrary $X, Y$, so $\nabla = \tilde\nabla$. $\blacksquare$

> [!note]- Lemma 2: Symmetry of mixed second partials in the flat case (motivating the symmetric Christoffel formula)
> **Statement:** On the flat Riemannian manifold $(\mathbb{R}^n, g_{\mathrm{Eucl}})$ in Cartesian coordinates, the unique torsion-free metric-compatible connection has all Christoffel symbols zero, and this is consistent with the Christoffel formula because $\partial_i g_{jl} = 0$ identically.
>
> **Hint:** In Cartesian coordinates on $\mathbb{R}^n$, $g_{ij} = \delta_{ij}$ is constant, so all partial derivatives vanish. The Christoffel formula then gives $\Gamma^k_{ij} \equiv 0$, which is symmetric in $(i, j)$ (torsion-free) and trivially metric-compatible.
>
> **Why needed:** Provides the calibration that the Christoffel formula reduces to the correct answer in the flat case, and shows the symmetry of mixed partial derivatives of $g$ is what enforces torsion-freeness.
>
> > [!note]- Full proof
> > In Cartesian coordinates on $\mathbb{R}^n$, the Euclidean metric is $g_{ij}(x) = \delta_{ij}$, independent of $x$. Hence $\partial_k g_{ij} = 0$ for all $k, i, j$, and the Christoffel formula gives
> > $$
> > \Gamma^k_{ij} = \tfrac{1}{2}\delta^{kl}(0 + 0 - 0) = 0.
> > $$
> > The connection is the flat connection $\nabla_X Y = (X(Y^1), \ldots, X(Y^n))$ (componentwise differentiation), which is manifestly torsion-free ($\Gamma^k_{ij} = \Gamma^k_{ji}$ trivially) and metric-compatible ($\partial_k g_{ij} = 0 = \Gamma_{kij} + \Gamma_{kji}$ trivially). The symmetry of mixed partial derivatives $\partial_i\partial_j = \partial_j\partial_i$ on Cartesian coordinates is what makes the Christoffel formula symmetric in $(i, j)$ in general: the third term $-\partial_l g_{ij}$ in the Christoffel formula uses the symmetry $g_{ij} = g_{ji}$, and the first two terms $\partial_i g_{jl} + \partial_j g_{il}$ are manifestly symmetric in $(i, j)$.

> [!note]- Lemma 3: The Christoffel formula gives the Levi-Civita connection in coordinates
> **Statement:** In a local coordinate chart $(x^i)$, the Christoffel symbols of the Levi-Civita connection are
> $$
> \Gamma^k_{ij} = \tfrac{1}{2}\,g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr).
> $$
>
> **Hint:** Apply the Koszul formula with $X = \partial_i$, $Y = \partial_j$, $Z = \partial_l$, use $[\partial_i, \partial_j] = 0$ in any coordinate frame, and identify $g(\nabla_{\partial_i}\partial_j, \partial_l) = \Gamma^k_{ij}g_{kl}$. Raising the index with $g^{kl}$ gives the formula.
>
> **Why needed:** This is the explicit computational formula used in every concrete Riemannian-geometry calculation.
>
> > [!note]- Full proof
> > In a coordinate chart with coordinate frame $\partial_i$, the Lie brackets vanish: $[\partial_i, \partial_j] = 0$. The Koszul formula with $X = \partial_i, Y = \partial_j, Z = \partial_l$ becomes
> > $$
> > 2g(\nabla_{\partial_i}\partial_j, \partial_l) = \partial_i g(\partial_j, \partial_l) + \partial_j g(\partial_i, \partial_l) - \partial_l g(\partial_i, \partial_j) = \partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}.
> > $$
> > Writing $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$, we have $g(\nabla_{\partial_i}\partial_j, \partial_l) = \Gamma^k_{ij}\,g_{kl}$. Substituting:
> > $$
> > 2\Gamma^k_{ij}g_{kl} = \partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}.
> > $$
> > Multiplying both sides by $\tfrac{1}{2}g^{ml}$ and using $g^{ml}g_{kl} = \delta^m_k$:
> > $$
> > \Gamma^m_{ij} = \tfrac{1}{2}\,g^{ml}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr).
> > $$
> > Relabel $m \to k$ to get the stated formula. The formula is manifestly symmetric in $(i, j)$ — verifying torsion-freeness — and was derived from metric-compatibility (via the Koszul formula). $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Existence of a connection.** Every smooth manifold admits a connection on $TM$, constructed by partition of unity (cover by trivialising open sets, use the flat connection in each chart, patch by partition of unity). So the space of connections is non-empty. The theorem is asserting that *exactly one* connection in this non-empty space is torsion-free and metric-compatible.
>
> **Step 1 — Uniqueness.** Suppose $\nabla$ is any torsion-free metric-compatible connection on $(M, g)$. Apply the metric-compatibility identity $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ with three cyclic permutations of $(X, Y, Z)$:
> $$
> \begin{aligned}
> X g(Y, Z) &= g(\nabla_X Y, Z) + g(Y, \nabla_X Z) & (\ast_1) \\
> Y g(Z, X) &= g(\nabla_Y Z, X) + g(Z, \nabla_Y X) & (\ast_2) \\
> Z g(X, Y) &= g(\nabla_Z X, Y) + g(X, \nabla_Z Y) & (\ast_3)
> \end{aligned}
> $$
> Form $(\ast_1) + (\ast_2) - (\ast_3)$:
> $$
> X g(Y, Z) + Y g(Z, X) - Z g(X, Y) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z) + g(\nabla_Y Z, X) + g(Z, \nabla_Y X) - g(\nabla_Z X, Y) - g(X, \nabla_Z Y).
> $$
> Use torsion-freeness to convert the "swapped" $\nabla$ terms:
> $$
> \begin{aligned}
> g(Z, \nabla_Y X) &= g(Z, \nabla_X Y - [X, Y]) = g(\nabla_X Y, Z) - g([X, Y], Z), \\
> g(\nabla_Z X, Y) &= g(\nabla_X Z - [X, Z], Y) = g(\nabla_X Z, Y) - g([X, Z], Y), \\
> g(X, \nabla_Z Y) &= g(X, \nabla_Y Z - [Y, Z]) = g(\nabla_Y Z, X) - g([Y, Z], X).
> \end{aligned}
> $$
> Substituting and rearranging:
> $$
> X g(Y, Z) + Y g(Z, X) - Z g(X, Y) = 2g(\nabla_X Y, Z) - g([X, Y], Z) + g([X, Z], Y) + g([Y, Z], X),
> $$
> where the $g(Y, \nabla_X Z), g(\nabla_X Z, Y), g(\nabla_Y Z, X), g(X, \nabla_Y Z)$ terms cancel pairwise (each occurs once with $+$ and once with $-$). Solving for $2g(\nabla_X Y, Z)$:
> $$
> 2g(\nabla_X Y, Z) = X g(Y, Z) + Y g(Z, X) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X). \qquad (\text{Koszul})
> $$
> The right-hand side depends only on $g$ and Lie brackets, not on $\nabla$. So if $\tilde\nabla$ is another torsion-free metric-compatible connection, the same formula gives $2g(\tilde\nabla_X Y, Z) = \text{same RHS}$, hence $g(\nabla_X Y - \tilde\nabla_X Y, Z) = 0$ for every $Z$. By non-degeneracy of $g$, $\nabla_X Y = \tilde\nabla_X Y$ for all $X, Y$, hence $\nabla = \tilde\nabla$.
>
> **Step 2 — Existence.** Define $\nabla$ by the Koszul formula: for any $X, Y \in \mathfrak{X}(M)$, let $\nabla_X Y$ be the unique vector field $V$ satisfying
> $$
> g(V, Z) = \tfrac{1}{2}\bigl[X g(Y, Z) + Y g(Z, X) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X)\bigr]
> $$
> for every $Z \in \mathfrak{X}(M)$. The right side is $C^\infty(M)$-linear in $Z$ (a direct calculation: the Leibniz corrections from the function-derivative terms and from the Lie brackets cancel — see [[Thm - Koszul Formula]] Lemma 1 for details), so it defines a 1-form $\eta \in \Omega^1(M)$ via $\eta(Z) = \tfrac{1}{2}\,\text{RHS}$. By non-degeneracy of $g$, there is a unique vector field $V = \eta^\sharp$ with $g(V, Z) = \eta(Z)$ for all $Z$. Define $\nabla_X Y := \eta^\sharp$.
>
> Now verify the four required properties:
>
> *(a) $C^\infty$-linearity in $X$:* Replace $X$ by $fX$ in the Koszul RHS and verify $K^{fX, Y}(Z) = f K^{X, Y}(Z)$. The function-derivative terms transform via Leibniz: $(fX)g(Y, Z) = fXg(Y, Z)$ (just composition), $Yg((fX), Z) = Yg(fX, Z) = Y(f)g(X, Z) + fYg(X, Z)$, $Zg(fX, Y) = Z(f)g(X, Y) + fZg(X, Y)$. The bracket terms transform via $[fX, Y] = f[X, Y] - Y(f)X$, etc. After careful collection, all $X(f), Y(f), Z(f)$ terms cancel pairwise, leaving $K^{fX, Y}(Z) = fK^{X, Y}(Z)$. Hence $\nabla_{fX}Y = f\nabla_X Y$.
>
> *(b) Leibniz in $Y$:* Replace $Y$ by $fY$ in the Koszul RHS and verify $K^{X, fY}(Z) = X(f)g(Y, Z) + fK^{X, Y}(Z)$. The function-derivative term $Xg(fY, Z) = X(f)g(Y, Z) + fXg(Y, Z)$ provides the $X(f)g(Y, Z)$ contribution; other terms multiply by $f$ after Leibniz corrections cancel (similar to part (a)). Hence $\nabla_X(fY) = X(f)Y + f\nabla_X Y$.
>
> *(c) Torsion-free:* Compute $g(\nabla_X Y - \nabla_Y X, Z) = \tfrac{1}{2}(K^{X, Y}(Z) - K^{Y, X}(Z))$. The function-derivative pieces $Xg(Y, Z) + Yg(Z, X) - Zg(X, Y)$ are symmetric in $X \leftrightarrow Y$ (the first two swap, the third uses $g(X, Y) = g(Y, X)$). So they cancel in the subtraction. The bracket pieces: $g([X, Y], Z) \to g([Y, X], Z) = -g([X, Y], Z)$, contributing $2g([X, Y], Z)$; $-g([X, Z], Y) \to -g([Y, Z], X)$, contributing $-g([X, Z], Y) + g([Y, Z], X)$; $-g([Y, Z], X) \to -g([X, Z], Y)$, contributing $-g([Y, Z], X) + g([X, Z], Y)$. The last two cancel each other, leaving $2g([X, Y], Z)$. So $g(\nabla_X Y - \nabla_Y X, Z) = g([X, Y], Z)$ for all $Z$, hence $\nabla_X Y - \nabla_Y X = [X, Y]$, i.e., torsion-free.
>
> *(d) Metric-compatible:* Compute $g(\nabla_X Y, Z) + g(Y, \nabla_X Z) = \tfrac{1}{2}(K^{X, Y}(Z) + K^{X, Z}(Y))$. Expanding $K^{X, Y}(Z) + K^{X, Z}(Y)$ term by term: $Xg(Y, Z) + Xg(Z, Y) = 2Xg(Y, Z)$. The other terms $Yg(Z, X), Zg(X, Y), Zg(X, Y), Yg(X, Z)$ — wait, more carefully: $K^{X, Z}(Y) = X g(Z, Y) + Z g(Y, X) - Y g(X, Z) + g([X, Z], Y) - g([X, Y], Z) - g([Z, Y], X)$. Adding to $K^{X, Y}(Z)$: the $Yg(Z, X) - Yg(X, Z) = 0$; the $-Zg(X, Y) + Zg(Y, X) = 0$; the $g([X, Y], Z) - g([X, Y], Z) = 0$; the $-g([X, Z], Y) + g([X, Z], Y) = 0$; the $-g([Y, Z], X) - g([Z, Y], X) = -g([Y, Z], X) + g([Y, Z], X) = 0$. All but the $2Xg(Y, Z)$ vanish. So $\tfrac{1}{2}(K^{X, Y}(Z) + K^{X, Z}(Y)) = Xg(Y, Z)$, i.e., $g(\nabla_X Y, Z) + g(Y, \nabla_X Z) = Xg(Y, Z)$ — metric-compatibility.
>
> Thus $\nabla$ defined by Koszul is a torsion-free metric-compatible connection. Together with Step 1 (uniqueness), this completes the proof.
>
> **Step 3 — The Christoffel formula in coordinates.** Apply the Koszul formula with $X = \partial_i, Y = \partial_j, Z = \partial_l$ in a coordinate chart. Since $[\partial_i, \partial_j] = 0$, all bracket terms vanish:
> $$
> 2g(\nabla_{\partial_i}\partial_j, \partial_l) = \partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}.
> $$
> Writing $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$, the left side equals $2\Gamma^k_{ij}g_{kl}$. Multiplying both sides by $\tfrac{1}{2}g^{ml}$:
> $$
> \Gamma^m_{ij}\,\delta^l_l \cdot \delta^m_k = \Gamma^m_{ij} = \tfrac{1}{2}g^{ml}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}). \qquad \blacksquare
> $$

---

# Cross-Field Exercise Suggestions

**1. The Levi-Civita connection of polar coordinates on $\mathbb{R}^2$.** Apply the Christoffel formula to the Euclidean metric $g = dr^2 + r^2 d\theta^2$ in polar coordinates and verify the Christoffel symbols are $\Gamma^r_{\theta\theta} = -r$, $\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = 1/r$. Verify by direct computation that the curvature is zero (the connection is flat in polar coordinates, despite the nonzero Christoffel symbols). See [[Ex - The Levi-Civita Connection of Polar Coordinates]].

**2. The Levi-Civita connection on a compact bi-invariantly-metric Lie group.** Use the Koszul formula to show that for left-invariant vector fields $X, Y$ on a Lie group $G$ with bi-invariant Riemannian metric, $\nabla_X Y = \tfrac{1}{2}[X, Y]$. Deduce that geodesics through the identity are one-parameter [[Def - Subgroup|subgroups]] $t \mapsto \exp(tX)$, and that the Riemannian exponential map equals the Lie-group exponential map of [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]]. (Standard problem in Lie-group geometry.)

**3. The Levi-Civita connection of the Schwarzschild metric.** Apply the orthonormal-frame version of Cartan's first structural equation (a consequence of the fundamental theorem) to compute the connection 1-forms of the Schwarzschild metric, then apply Cartan's second structural equation to compute the curvature 2-forms. The result is the standard computation in every general relativity textbook; the elegance of the orthonormal-frame method is the operational virtue of the fundamental theorem. See [[Ex - Computing Curvature 2-Forms in an Orthonormal Frame]].

**4. Connection on a vector bundle from a fibre metric.** The same construction (torsion-free + metric-compatible) generalises to vector bundles equipped with a fibre metric — *except* that "torsion-free" requires the bundle to be the tangent bundle (because torsion uses the Lie bracket on $TM$). On a general Riemannian vector bundle $(E, h) \to M$, "metric-compatible" alone is one condition and does *not* determine a unique connection; one needs an additional choice. The bridge: the fundamental theorem is special to $TM$ because of the soldering form that identifies $TM$ with the base's tangent bundle.

---

# Bridges

- **[[Thm - Koszul Formula]]** — The Koszul formula is the technical heart of the proof. Uniqueness follows because any torsion-free metric-compatible connection satisfies Koszul (by the symmetrisation derivation), and the RHS depends only on $g$ and Lie brackets, so any two such connections agree. Existence follows because defining $\nabla$ by Koszul plus the sharp map gives a connection that one verifies is torsion-free and metric-compatible.

- **[[Def - Christoffel Symbols|Christoffel formula]]** — Specialising the Koszul formula to a coordinate frame gives the explicit Christoffel formula $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. This is the most-used computational form of the Levi-Civita connection and is the direct output of the fundamental theorem in coordinates.

- **[[Thm - Cartan's First Structural Equation]]** — The moving-frame version of the same uniqueness argument: torsion-freeness becomes $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$, and metric-compatibility in an orthonormal frame becomes $\omega^a{}_b + \omega^b{}_a = 0$. The two conditions together determine the connection 1-forms $\omega^a{}_b$ uniquely from the coframe $\sigma^a$ — exactly as Koszul determines $\nabla_X Y$ uniquely from $g$ and Lie brackets. Cartan's structural equations are the practical computational tool that follows from the fundamental theorem.

- **General relativity** — In GR, the metric is Lorentzian (signature $(1, n-1)$) and the proof of the fundamental theorem goes through unchanged (only non-degeneracy is used, not positive-definiteness). The Lorentzian Levi-Civita connection is the **gravitational connection**, whose geodesics are the worldlines of freely-falling particles and whose curvature enters the Einstein field equations $R_{\mu\nu} - \tfrac{1}{2}R g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$. The full theory is in [[General Relativity I — Einstein's Equations and Schwarzschild]].

- **First Bianchi identity** — The torsion-free condition feeds into the proof of the first Bianchi identity: $R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0$. The proof uses torsion-freeness plus the Jacobi identity for Lie brackets. Without torsion-freeness, the first Bianchi identity acquires correction terms involving $T$ and $\nabla T$. This is the algebraic symmetry that reduces the number of independent components of $R$ from $n^4$ to $\tfrac{n^2(n^2-1)}{12}$.

- **Information geometry — alpha-connections** — On a statistical manifold (a parametric family of probability distributions), the **Fisher information metric** $g$ admits the Levi-Civita connection — but also a family of "$\alpha$-connections" $\nabla^{(\alpha)}$ for $\alpha \in \mathbb{R}$, of which the Levi-Civita is the $\alpha = 0$ case. The **e-connection** ($\alpha = 1$, exponential families are flat) and **m-connection** ($\alpha = -1$, mixture families are flat) are not metric-compatible but are **dually flat** with respect to each other. This is Amari's information geometry, and it shows that the fundamental theorem's "unique" connection is selected by a *specific* compatibility condition; relaxing the conditions gives interesting alternative connections.

---

# Unlocked by This

> [!tip] The Entire Subsequent Development of Riemannian Geometry *(from Riemannian Geometry II, III, IV)*
> The fundamental theorem is the gateway to all of Riemannian geometry: it gives the unique connection from which everything else follows. **Geodesics** (curves with $\nabla_{\dot\gamma}\dot\gamma = 0$), **parallel transport** (as an isometry of tangent spaces by metric-compatibility), the **exponential map** $\exp_p : T_pM \to M$ and normal coordinates, the **first and second variation formulas** for arc length, **Jacobi fields** and the Jacobi equation, the **Riemann curvature tensor** $R$ with its symmetries (antisymmetry, pair-symmetry, first Bianchi), **sectional/Ricci/scalar curvatures**, **comparison theorems** (Bonnet-Myers, Cartan-Hadamard, Synge), the **Gauss-Bonnet theorem** for surfaces and its generalisations, the entire theory of **holonomy** and Berger's classification — all of this uses the Levi-Civita connection essentially. Without the fundamental theorem, every one of these results would depend on an arbitrary choice of connection and would have no canonical form.

> [!tip] Einstein's General Relativity *(from General Relativity)*
> In general relativity, spacetime is a 4-dimensional Lorentzian manifold and the connection is the Lorentzian Levi-Civita. The fundamental theorem applied in Lorentzian signature delivers the Christoffel symbols $\Gamma^\lambda_{\mu\nu} = \tfrac{1}{2}g^{\lambda\sigma}(\partial_\mu g_{\nu\sigma} + \partial_\nu g_{\mu\sigma} - \partial_\sigma g_{\mu\nu})$ that act as the "gravitational field" — the geodesic equation $\ddot x^\lambda + \Gamma^\lambda_{\mu\nu}\dot x^\mu \dot x^\nu = 0$ is Newton's second law for a freely-falling test particle. The Riemann tensor of the Lorentzian Levi-Civita contracts to the **Ricci tensor** $R_{\mu\nu}$ that enters the **Einstein field equations** $R_{\mu\nu} - \tfrac{1}{2}R g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$. The contracted second Bianchi identity (a consequence of the structure of the Levi-Civita curvature) gives the conservation law $\nabla_\mu T^{\mu\nu} = 0$ automatically. Full development in [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] Special Holonomy and Berger's Classification *(from Riemannian Geometry)*
> The holonomy group of the Levi-Civita connection — i.e., the group of parallel-transport maps along loops at a point — is a subgroup of $\mathrm{SO}(n)$ for an orientable Riemannian manifold. **Berger's classification** (1955) lists the possible irreducible holonomy groups of complete simply-connected non-symmetric Riemannian manifolds: $\mathrm{SO}(n)$ (generic), $U(n)$ (Kähler), $SU(n)$ (Calabi-Yau), $\mathrm{Sp}(n)$ (hyperkähler), $\mathrm{Sp}(n)\mathrm{Sp}(1)$ (quaternion-Kähler), $G_2$, $\mathrm{Spin}(7)$. Each special holonomy corresponds to additional parallel tensor fields and to deep connections to complex geometry, algebraic geometry, mirror symmetry, and string compactifications. The fundamental theorem is what makes "the holonomy of $(M, g)$" a well-defined object — without it, holonomy would depend on which torsion-free metric-compatible connection one chose, and there would be no canonical answer.
