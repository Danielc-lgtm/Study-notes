---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - Regular and Critical Points"
  - "Def - Embedded Submanifold"
  - "Def - Tangent Space of a Submanifold"
  - "Thm - The Implicit Function Theorem"
  - "Thm - Local Submersion Theorem"
tags: [geometry, differential-geometry]
---

# Notation

$\Phi : M \to N$ is a smooth map between smooth manifolds, $m = \dim M$, $n = \dim N$. For $c \in N$, the **level set** is $\Phi^{-1}(c) = \{x \in M : \Phi(x) = c\}$. A point $p \in M$ is a **regular point** if $d\Phi_p$ is surjective ([[Def - Regular and Critical Points]]); a value $c \in N$ is a **regular value** if every point of $\Phi^{-1}(c)$ is regular. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Statement

> **Theorem ([[Thm - The Regular Value Theorem|Regular Value Theorem]] on Manifolds).** Let $\Phi : M \to N$ be a smooth map between smooth manifolds, and let $c \in N$ be a regular value of $\Phi$. Then the level set
> $$S \;=\; \Phi^{-1}(c) \;\subseteq\; M,$$
> if nonempty, is a properly embedded smooth submanifold of $M$ of codimension $\dim N = n$ (hence of dimension $\dim M - \dim N = m - n$). For every $p \in S$, the tangent space of $S$ at $p$ as a subspace of $T_p M$ is
> $$T_p S \;=\; \ker d\Phi_p.$$

> **Corollary (Constant-rank level set theorem).** More generally, if $\Phi:M\to N$ has constant rank $r$ on a neighbourhood of $\Phi^{-1}(c)$, then this level set is a properly embedded smooth submanifold of codimension $r$ in $M$. If the hypothesis holds near every fibre, the conclusion holds for every fibre.

---

# Motivation

This is the **standard manufacturing device for embedded submanifolds**. Almost every concrete submanifold one encounters — the sphere $S^n \subseteq \mathbb{R}^{n+1}$, the orthogonal group $\mathrm{O}(n) \subseteq \mathrm{GL}(n)$, the special linear group $\mathrm{SL}(n) \subseteq \mathrm{GL}(n)$, energy surfaces, mass shells, configuration manifolds of mechanical systems — is presented as a level set of a smooth map, and proving it is a submanifold means applying this theorem.

The result answers the most natural geometric question one asks about a level set: when is $\{\Phi = c\}$ a *clean smooth space*, with no corners, no crossings, no cusps, no vertices? The answer is: exactly when the value $c$ is regular, that is, when at every point of the preimage, the linearisation $d\Phi_p$ is surjective. The hypothesis is computable from a single Jacobian calculation; the conclusion is a global geometric structure (submanifold) plus an explicit tangent space.

The theorem is the **manifold-level upgrade of the [[Thm - The Regular Value Theorem|Euclidean regular value theorem]]** from [[Multivariate Analysis II — Inverse and Implicit Function Theorems|MA II]]. The Euclidean theorem says: for $\Phi : U \to \mathbb{R}^{n-d}$ smooth on $U \subseteq \mathbb{R}^n$ open, a regular level set is a $d$-dimensional embedded submanifold of $\mathbb{R}^n$. The manifold version replaces $\mathbb{R}^n$ by an arbitrary smooth manifold $M$ and proceeds by applying the Euclidean theorem chart-by-chart. The proof's structural backbone is the same as the Euclidean one — *the [[Thm - The Implicit Function Theorem|implicit function theorem]] gives local product structure; gluing these local pieces gives the manifold structure of the level set.*

The theorem also gives the **tangent space for free**, as the kernel of the differential of the defining map. This is the most computationally direct way to identify the tangent space of a submanifold: rather than parametrising, one differentiates the defining equation. For matrix Lie [[Def - Group|groups]] this is the foundational identification: $T_I \mathrm{SL}(n) = \mathfrak{sl}(n)$ (trace-zero matrices), $T_I \mathrm{O}(n) = \mathfrak{o}(n)$ (antisymmetric matrices). The dimension of the submanifold falls out for free as $\dim M - \dim N$.

There is a subtle but important point about *which* points of $M$ need to be regular. The hypothesis is that every point *in the preimage of $c$* is regular — not that every point of $M$ is regular. This is a strictly weaker condition, and it is exactly what is needed: the rank condition is checked along the level set, not globally. If even one point of the preimage is critical, the level set can fail to be a submanifold *at that point*, while remaining a submanifold elsewhere. The conical example $\{z^2 = x^2 + y^2\}$ in $\mathbb{R}^3$ is exactly this: it is a $2$-submanifold everywhere except at the origin, which is the unique critical point on the level set.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$c$ is a regular value of $\Phi$: $d\Phi_p$ is surjective at every $p \in \Phi^{-1}(c)$". The skill is recognising regularity from indirect data.

The first disguised source is **a defining map whose differential is nowhere-zero on the candidate set** (scalar codomain case). Property $B$: $\Phi : M \to \mathbb{R}$ is a scalar function with $d\Phi_p \neq 0$ for every $p$ where $\Phi(p) = c$. The bridge: for a scalar function, "$d\Phi_p$ is surjective onto $\mathbb{R}$" is equivalent to "$d\Phi_p \neq 0$", since $\mathbb{R}$ is one-dimensional. So *any* level set of a scalar function with nowhere-vanishing differential is a hypersurface. The non-obviousness: a single nonvanishing-differential condition gives the entire submanifold structure. *Example:* the sphere $S^n$ is the level set of $|x|^2 - 1$, and $d(|x|^2)_p = 2 \langle p, \cdot \rangle$ is nonzero whenever $p \neq 0$, hence everywhere on the sphere — see [[Ex - The Sphere as a Level Set]].

The second disguised source is **independent constraint gradients** (vector codomain case). Property $B$: $\Phi = (\Phi^1, \dots, \Phi^k) : M \to \mathbb{R}^k$ has the property that the differentials $d\Phi^1_p, \dots, d\Phi^k_p$ are linearly independent (in $T_p^* M$) at every $p \in \Phi^{-1}(c)$. The bridge: the rows of the Jacobian of $\Phi$ at $p$ are exactly the differentials $d\Phi^i_p$, and the rank of the Jacobian is the dimension of the row space — equal to $k$ iff the differentials are independent, iff $d\Phi_p$ is surjective. So linear independence of constraint gradients *is* regularity. The non-obviousness: a single linear-algebra check on $k$ covectors confirms a global submanifold structure. *Example:* this is exactly the *constraint-qualification* hypothesis from [[Thm - The Method of Lagrange Multipliers|Lagrange multipliers]] — the regular value theorem and Lagrange multipliers share the same regularity source.

The third disguised source is **an algebraic structure that propagates rank**. Property $B$: $\Phi$ is equivariant under a Lie group acting transitively on $\Phi^{-1}(c)$. The bridge: if the group action preserves the level set and acts transitively on it, then the rank of $d\Phi_p$ at one point equals the rank at every other point (because the action's differential is a linear isomorphism). So one only needs to check regularity at a single point. The non-obviousness: a single rank computation extends to the whole level set by symmetry. *Example:* for $\mathrm{O}(n) = \{A^T A = I\}$, the orthogonal group acts on itself by left multiplication, which is transitive; checking regularity at the identity ($d\Phi_I$ surjective onto symmetric matrices) suffices for the whole group — see [[Ex - The Orthogonal Group as a Regular Level Set]].

**Targets (Output Amplification)**

The conclusion is "$\Phi^{-1}(c)$ is a properly embedded submanifold of codimension $n$, with tangent space $\ker d\Phi_p$".

Combine the conclusion with **a function to be optimised on the level set.** Property $D$: you want to extremise $f\in C^\infty(M)$ subject to $\Phi=c$. At an extremum, $df_p$ annihilates $T_pS=\ker d\Phi_p$. Linear duality gives $(\ker d\Phi_p)^\circ=\operatorname{im}(d\Phi_p)^*$, so for $N=\mathbb R^k$ there are multipliers with $df_p=\sum_i\lambda_i,d\Phi^i_p$. This uses the annihilator, not an orthogonal complement unless a metric has separately been chosen.

Combine the conclusion with **closedness of the level set.** Property $D$: $\Phi^{-1}(c)$ is closed in $M$. The amplified result $E$: $\Phi^{-1}(c)$ is a properly embedded submanifold — closed in $M$, hence proper. Closed embedded submanifolds have the cleanest behaviour: smooth functions on them extend to smooth functions on $M$; they admit tubular neighbourhoods; the extension lemma applies; integration is unambiguous. (The level set is automatically closed in $M$ as the continuous preimage of the closed singleton $\{c\}$ — so *every* level set is closed in $M$, and *every* regular level set is automatically properly embedded.) The combination "regular value + ambient manifold structure" gives proper embedding without extra work.

Combine the conclusion with **a group structure on the level set.** If the regular level set is a subgroup of an ambient matrix Lie group, ambient multiplication and inversion restrict to smooth maps on it; it is therefore a Lie group. Both subgroup closure and smoothness of the two restricted operations matter—closure under multiplication alone does not supply inverses. Its tangent space at the identity, $\ker d\Phi_e$, is its Lie algebra.

Combine the conclusion with **a fibre bundle structure.** Property $D$: $\Phi : M \to N$ is a surjective submersion (so every value is regular), and $M$ is fibrewise locally trivial over $N$. The amplified result $E$: $\Phi$ exhibits $M$ as a fibre bundle over $N$, with fibres the level sets $\Phi^{-1}(c)$. The regular value theorem produces the fibres as submanifolds; the local triviality is the bundle structure. *Example:* the Hopf fibration $S^3 \to S^2$, with all fibres great circles — see [[Ex - The Hopf Map is a Submersion]].

---

# Why Is It True

The intuition is the same as for the [[Thm - The Regular Value Theorem|Euclidean regular value theorem]], but transported to the manifold setting via charts.

**The bolded one-liner mechanism summary: the implicit function theorem gives local product structure; gluing these local pieces gives the manifold structure of the level set.**

Here is the picture. Fix a regular point $p$ of the level set $S = \Phi^{-1}(c)$. By hypothesis $d\Phi_p$ is surjective, so [[Thm - Local Submersion Theorem|by the local submersion theorem]] there are smooth charts $(U, \varphi)$ around $p$ in $M$ and $(V, \psi)$ around $c$ in $N$ in which $\Phi$ has the coordinate representation
$$\hat\Phi(x^1, \dots, x^n, x^{n+1}, \dots, x^m) = (x^1, \dots, x^n).$$
The level set $\Phi^{-1}(c)$, in these coordinates, becomes the set $\{x : \hat\Phi(x) = 0\} = \{x : x^1 = \dots = x^n = 0\}$ — a flat $(m - n)$-dimensional coordinate slice in $\varphi(U) \subseteq \mathbb{R}^m$.

This means $S$, near $p$, is literally a *flat slice* in suitable coordinates — and this is the slice characterisation of an embedded submanifold ([[Def - Embedded Submanifold]]). So $S$ is locally an embedded $(m - n)$-submanifold of $M$ at $p$.

The point $p$ was arbitrary on $S$ (every point is regular by hypothesis), so the local slice condition is satisfied at every point of $S$. By the local-to-global principle for submanifolds, $S$ is then a global embedded submanifold of $M$ of dimension $m - n$.

The tangent space comes from the same coordinate setup. In the normal-form coordinates, $T_p S$ is the tangent space of the coordinate slice $\{x^1 = \dots = x^n = 0\}$ at $0$, which is spanned by $\partial/\partial x^{n+1}, \dots, \partial/\partial x^m$. The kernel of $d\Phi_p$ in these coordinates is the kernel of the linear projection $(v^1, \dots, v^m) \mapsto (v^1, \dots, v^n)$, which is exactly the span of $\partial/\partial x^{n+1}, \dots, \partial/\partial x^m$. So $T_p S = \ker d\Phi_p$.

Why is it the kernel of the differential, intrinsically? Because for any smooth curve $\gamma$ in $S$ with $\gamma(0) = p$, we have $\Phi(\gamma(t)) = c$ for all $t$ (it's a constant), so $d\Phi_p(\gamma'(0)) = 0$ by the chain rule. Every tangent vector to $S$ is the velocity of such a curve, so $T_p S \subseteq \ker d\Phi_p$. The reverse inclusion is by dimension count: both spaces have dimension $m - n$ ($T_p S$ because $\dim S = m - n$, and $\ker d\Phi_p$ by rank-nullity: $\dim T_p M - \dim\mathrm{im}\, d\Phi_p = m - n$). A subspace of the same dimension is equal.

The local-to-global principle is the key conceptual content: the theorem assembles local IFT structure into a global manifold structure. The IFT works one point at a time; the regular value hypothesis guarantees it works at every point of the level set simultaneously; the assembly is automatic because the slice charts at nearby points are smoothly compatible (their transition maps are smooth, inherited from $M$'s smooth structure).

The properness of the embedding is a final observation: $S = \Phi^{-1}(c)$ is closed in $M$ as the preimage of the closed singleton $\{c\}$, and a closed embedded submanifold is automatically properly embedded.

---

# What Makes This Hard

The non-obvious step is recognising the theorem *is* the [[Thm - The Implicit Function Theorem|implicit function theorem]] applied at every point of the level set simultaneously, then assembled via the local-to-global principle. The most common error is to check regularity *at only one point* and assume the level set is a submanifold globally — the hypothesis demands regularity at *every* point of the preimage. A second frequent slip: confusing critical *points* of $\Phi$ (anywhere in $M$) with critical points *on the level set* (in $\Phi^{-1}(c)$); only the latter affect whether $c$ is regular. A third pitfall: choosing the wrong codomain for $\Phi$, so that "surjective onto the apparent codomain" fails when "surjective onto the actual image" holds — the $\mathrm{O}(n)$ example illustrates this trap (see [[Ex - The Orthogonal Group as a Regular Level Set]]).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
At each point $p$ of the level set, regularity of $d\Phi_p$ activates the local submersion theorem (a manifold-level version of the implicit function theorem), producing charts in which $\Phi$ is a coordinate projection. The level set in these charts is then a flat coordinate slice — the local slice condition for an embedded submanifold. Since this holds at every point of the level set, the level set is a global embedded submanifold. The tangent space is the kernel of the differential by a chain-rule argument combined with a dimension count.

**Subgoal decomposition:**

1. **Apply the local submersion theorem at each level-set point.** At any $p \in S = \Phi^{-1}(c)$, the differential $d\Phi_p$ is surjective by hypothesis. The [[Thm - Local Submersion Theorem|local submersion theorem]] gives charts $(U, \varphi)$ around $p$ in $M$ and $(V, \psi)$ around $c$ in $N$, both centred at the respective points, in which $\Phi$ has the form $\hat\Phi(x^1, \dots, x^m) = (x^1, \dots, x^n)$.
   - *Hint:* This is the rank theorem in its submersion specialisation.
   - *Why needed:* It produces the standard coordinate setup in which the level set is a coordinate slice.

2. **Identify the level set as a slice in the chart.** In the chart $\varphi(U)$, the level set $S \cap U$ corresponds to $\{x \in \varphi(U) : \hat\Phi(x) = 0\} = \{x \in \varphi(U) : x^1 = \dots = x^n = 0\}$ — a flat $(m - n)$-dimensional slice of $\varphi(U)$.
   - *Hint:* $\hat\Phi$ is the coordinate projection, and its zero set is the coordinate complement.
   - *Why needed:* It verifies the local $(m-n)$-slice condition for $S$ at $p$.

3. **Assemble globally.** Since $p \in S$ was arbitrary, the local slice condition holds at every point of $S$. By the local-slice characterisation of embedded submanifolds ([[Def - Embedded Submanifold]]), $S$ is a $(m - n)$-dimensional embedded submanifold of $M$.
   - *Hint:* The local slice condition is precisely the criterion for being an embedded submanifold.
   - *Why needed:* This is the local-to-global step.

4. **Compute the tangent space.** Take $v \in T_p S$, represented as $\gamma'(0)$ for some smooth curve $\gamma$ in $S$ with $\gamma(0) = p$. The composite $\Phi \circ \gamma$ is constantly $c$, so by the chain rule $d\Phi_p(\gamma'(0)) = 0$. Hence $T_p S \subseteq \ker d\Phi_p$.
   - *Hint:* Constancy of $\Phi$ on $S$ gives the chain-rule identity.
   - *Why needed:* It gives one inclusion.

5. **Match [[Def - Dimension|dimensions]].** Both $T_p S$ and $\ker d\Phi_p$ have dimension $m - n$: the former because $S$ has dimension $m - n$; the latter because $d\Phi_p$ is surjective onto $T_c N$ (which has dimension $n$), so by rank-nullity $\dim\ker d\Phi_p = \dim T_p M - n = m - n$. A subspace of the same dimension is equal, so $T_p S = \ker d\Phi_p$.
   - *Hint:* Rank-nullity from surjectivity.
   - *Why needed:* It completes the tangent-space identification.

6. **Verify proper embedding.** $S$ is closed in $M$ as the preimage $\Phi^{-1}(\{c\})$ of the closed singleton $\{c\}$ under the continuous map $\Phi$. A closed embedded submanifold is properly embedded.
   - *Hint:* Closedness of the level set follows from continuity of $\Phi$ and Hausdorffness of $N$.
   - *Why needed:* It strengthens "embedded" to "properly embedded".

---

# Lemma Decomposition

> [!note]- Lemma 1: Regular level set is locally a coordinate slice
> **Statement:** Let $\Phi : M \to N$ be smooth and $c \in N$ a regular value. For every $p \in \Phi^{-1}(c)$, there exist smooth charts $(U, \varphi)$ around $p$ in $M$ and $(V, \psi)$ around $c$ in $N$, with $\Phi(U) \subseteq V$ and both charts centred at the respective points, such that
> $$\varphi(\Phi^{-1}(c) \cap U) = \varphi(U) \cap (\{0\}^n \times \mathbb{R}^{m-n}).$$
>
> **Hint:** Apply the local submersion theorem to $\Phi$ at $p$.
>
> **Why needed:** This is the local slice property; assembling these gives the global submanifold structure.
>
> > [!note]- Full proof
> > By hypothesis $d\Phi_p$ is surjective. By the [[Thm - Local Submersion Theorem|local submersion theorem]], there are smooth charts $(U, \varphi)$ around $p$ in $M$ centred at $p$ and $(V, \psi)$ around $c$ in $N$ centred at $c$, with $\Phi(U) \subseteq V$, such that the coordinate representation $\hat\Phi = \psi \circ \Phi \circ \varphi^{-1}$ is the projection $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^n)$. Then for $q \in U$:
> > $$\Phi(q) = c \iff \psi(\Phi(q)) = \psi(c) = 0 \iff \hat\Phi(\varphi(q)) = 0 \iff \text{the first } n \text{ coordinates of } \varphi(q) \text{ are } 0.$$
> > So $\varphi(\Phi^{-1}(c) \cap U) = \varphi(U) \cap (\{0\}^n \times \mathbb{R}^{m-n})$, which is a coordinate slice in $\varphi(U)$.

> [!note]- Lemma 2: The tangent space of a regular level set is the kernel of the differential
> **Statement:** With $S = \Phi^{-1}(c)$ a regular level set, $T_p S = \ker d\Phi_p$ as [[Def - Subspace|subspaces]] of $T_p M$, for every $p \in S$.
>
> **Hint:** One inclusion comes from differentiating $\Phi \circ \gamma = c$ along curves; the other from a dimension count.
>
> **Why needed:** It gives the explicit tangent-space formula, which is the most useful operational output of the theorem.
>
> > [!note]- Full proof
> > *$T_p S \subseteq \ker d\Phi_p$.* Take $v \in T_p S$; by [[Def - Tangent Space of a Submanifold|the curve characterisation]] there is a smooth curve $\gamma : J \to S$ with $\gamma(0) = p$ and $\gamma'(0) = v$, smooth as a map into $S$. Since $S$ is embedded (by Lemma 1's assembly), smoothness into $S$ is the same as smoothness into $M$ with image in $S$ — so $\gamma : J \to M$ is smooth. Then $\Phi \circ \gamma$ is constantly $c$ on $J$. Differentiate at $t = 0$ by the chain rule: $0 = (d/dt)|_{t=0} \Phi(\gamma(t)) = d\Phi_p(\gamma'(0)) = d\Phi_p(v)$. So $v \in \ker d\Phi_p$.
> >
> > *$\dim T_p S = \dim \ker d\Phi_p$.* By Lemma 1's assembly, $\dim S = m - n$, so $\dim T_p S = m - n$. The differential $d\Phi_p : T_p M \to T_c N$ is surjective (since $p$ is a regular point), so by rank-nullity $\dim \ker d\Phi_p = \dim T_p M - \dim T_c N = m - n$. So $\dim T_p S = \dim \ker d\Phi_p$.
> >
> > A subspace of a vector space is equal to a larger space iff their dimensions match, so $T_p S = \ker d\Phi_p$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Phi : M \to N$ be smooth, $c \in N$ a regular value, and $S = \Phi^{-1}(c)$ nonempty.
>
> **Step 0 (closedness).** $\{c\}$ is closed in $N$ since $N$ is Hausdorff. So $S = \Phi^{-1}(\{c\})$ is closed in $M$ by continuity of $\Phi$. (This step verifies that *any* level set is closed in $M$, before checking the embedded-submanifold structure.)
>
> **Step 1 (slice condition at each point).** Let $p \in S$. By hypothesis $d\Phi_p$ is surjective. Apply the [[Thm - Local Submersion Theorem|local submersion theorem]]: there exist smooth charts $(U, \varphi)$ around $p$ in $M$ and $(V, \psi)$ around $c$ in $N$, both centred at the respective points, with $\Phi(U) \subseteq V$, in which the coordinate representation is the standard projection
> $$\psi \circ \Phi \circ \varphi^{-1}(x^1, \dots, x^m) = (x^1, \dots, x^n).$$
> In this chart $\varphi(S \cap U) = \{x \in \varphi(U) : x^1 = \dots = x^n = 0\}$, which is a flat $(m-n)$-dimensional slice of $\varphi(U)$.
>
> **Step 2 (embedded submanifold).** Since the slice condition is satisfied at every point $p \in S$, the local slice criterion for embedded submanifolds applies (this is the equivalent characterisation in [[Def - Embedded Submanifold]]). Hence $S$ is an embedded $(m-n)$-dimensional smooth submanifold of $M$.
>
> **Step 3 (properly embedded).** By Step 0, $S$ is closed in $M$. A closed embedded submanifold is properly embedded.
>
> **Step 4 (tangent space).** By Lemma 2, $T_p S = \ker d\Phi_p$ at every $p \in S$.
>
> $\qquad\blacksquare$
>
> The constant-rank generalisation (corollary) is identical with the rank theorem replacing the local submersion theorem in Step 1. The slice produced has the same shape, and the rest of the argument runs unchanged.

---

# Cross-Field Exercise Suggestions

**Matrix Lie groups as smooth groups.** The orthogonal group $\mathrm{O}(n) = \{A : A^T A = I\}$, the special linear group $\mathrm{SL}(n) = \{\det A = 1\}$, the symplectic group $\mathrm{Sp}(2n) = \{A^T J A = J\}$, the unitary group $\mathrm{U}(n) = \{A^* A = I\}$, are all level sets of smooth maps on the matrix space. Checking regularity at the identity (sometimes with a careful codomain choice) shows that the identity is a regular value, so each is an embedded submanifold of dimension $\dim \mathrm{Mat}_n - \dim(\text{constraint space})$. Each is also closed under multiplication, hence a Lie group; the tangent space at the identity (computed as $\ker d\Phi_I$) is the corresponding Lie algebra. This is the principal industrial application of the theorem. See [[Ex - The Special Linear Group is a Submanifold of GL(n)|Ex - The Special Linear Group is a Submanifold of GL(n)]] and [[Ex - The Orthogonal Group as a Regular Level Set]].

**Energy surfaces in classical mechanics.** A conservative mechanical system on phase space has energy function $H(q, p)$, and every trajectory of the Hamiltonian flow is confined to a level set $\{H = E\}$. For non-critical values of $E$ (energies not corresponding to equilibria), the regular value theorem gives the energy surface a smooth $(2n - 1)$-dimensional submanifold structure of phase space, on which the dynamics is a smooth flow. The qualitative theory of dynamical systems — phase portraits, separatrices, KAM theory — rests on energy surfaces being genuine manifolds at non-critical values.

**The Stiefel manifold of orthonormal frames.** The set $V_k(\mathbb{R}^n) = \{(v_1, \dots, v_k) : v_i \in \mathbb{R}^n,\, \langle v_i, v_j \rangle = \delta_{ij}\}$ of orthonormal $k$-frames in $\mathbb{R}^n$ is a level set of the map sending $(v_1, \dots, v_k)$ to the Gram matrix $[\langle v_i, v_j \rangle]_{ij}$ valued in symmetric matrices. The identity Gram matrix $I_k$ is a regular value, so $V_k(\mathbb{R}^n)$ is an embedded submanifold of $(\mathbb{R}^n)^k$ of dimension $nk - k(k+1)/2$. This is the central example in the topology of homogeneous spaces.

**The mass shell in special relativity.** A particle of positive mass $m$ in [[Special Relativity III — Minkowski Spacetime and the Metric|Minkowski space]] has four-momentum on the level set $\{p^\mu p_\mu = -m^2 c^2\}$ — a hyperboloid in momentum space. The defining function $\Phi(p) = \langle p, p \rangle = -p_0^2 + |\vec p|^2$ has $d\Phi_p(v) = 2\langle p, v \rangle$ nonzero off the origin (in the Minkowski inner product), so any non-origin value is regular and the mass shell is a smooth submanifold. The application is out-of-distribution because the inner product is *indefinite* (Lorentzian), yet the regular value theorem applies verbatim.

---

# Bridges

- **[[Thm - The Implicit Function Theorem|Implicit Function Theorem]]** — the engine. The regular value theorem on manifolds is the implicit function theorem applied at every point of a level set and assembled chart-by-chart. The rank condition at each point activates the IFT there, giving local graph structure; the local-to-global principle assembles these graphs into a global submanifold. The relationship is exact, not analogous.

- **[[Thm - The Rank Theorem|Rank Theorem]]** — the parent. The regular value theorem on manifolds is the constant-rank-equals-$\dim N$ specialisation of the rank theorem, restricted to the action on level sets. The rank theorem provides the coordinate normal form; the regular value theorem reads off the level-set consequence.

- **[[Thm - The Regular Value Theorem|Regular Value Theorem (Euclidean)]]** — the special case. When $M = \mathbb{R}^m$ and $N = \mathbb{R}^n$ this is just the Euclidean regular value theorem. The manifold version is its global-chart-independent upgrade.

- **[[Def - Embedded Submanifold|Embedded Submanifold]]** — the output. The theorem produces an embedded submanifold; conversely, every embedded submanifold is *locally* a regular level set ([[Def - Embedded Submanifold|Proposition 5.16 of Lee]]). So "regular level set" and "embedded submanifold" are two names for largely the same class of objects (with the qualification that the level-set presentation is local for general embedded submanifolds).

- **[[Def - Tangent Space of a Submanifold|Tangent Space of a Submanifold]]** — the kernel formula. The theorem identifies the tangent space as $\ker d\Phi_p$ — the most computationally efficient tangent-space characterisation, used everywhere matrix-group tangent spaces are computed.

- **[[Thm - Sard's Theorem|Sard's Theorem]]** — the genericity companion. Sard's theorem says the set of critical values has measure zero, so almost every value is regular. The regular value theorem says regular values give submanifolds. Together: *almost every* level set of a smooth map is a submanifold. This is the genericity statement at the heart of differential topology.

---

# Unlocked by This

> [!tip] Transversality *(from Differential Topology)*
> The regular value theorem generalises to **transversality**: a smooth map $\Phi : M \to N$ is transverse to a submanifold $S' \subseteq N$ if at every point $p \in \Phi^{-1}(S')$, the image of $d\Phi_p$ and $T_{\Phi(p)} S'$ together span $T_{\Phi(p)} N$. The preimage $\Phi^{-1}(S')$ is then a smooth submanifold of $M$ of codimension $\dim N - \dim S'$. The regular value case is $S' = \{c\}$, where transversality reduces to surjectivity of $d\Phi_p$.

> [!tip] Cobordism *(from Algebraic Topology)*
> Two compact $n$-manifolds $M_0, M_1$ are **cobordant** if there is a compact $(n+1)$-manifold $W$ with boundary $\partial W = M_0 \sqcup M_1$. Cobordism classes form a ring under disjoint union and Cartesian product. The Pontryagin–Thom construction realises cobordism classes as preimages of regular values of maps to spheres — the regular value theorem provides the cobordism's manifold structure.

> [!tip] Morse Theory *(from Differential Topology)*
> A **Morse function** $f : M \to \mathbb{R}$ has only non-degenerate critical points. By the regular value theorem, every non-critical level set of $f$ is a smooth hypersurface; **Morse theory** studies how these level sets change topologically as one crosses a critical value. The handlebody decomposition of $M$ is built from this — at each critical value, a handle is attached based on the Morse index.

> [!tip] Quotient Manifolds and Homogeneous Spaces *(from Lie Theory)*
> When a Lie group $G$ acts freely and properly on $M$, the quotient theorem makes $M/G$ a smooth manifold and the projection a surjective submersion; its fibres are the orbits. Their regular-level-set structure follows only after that quotient submersion is constructed. Independently, the constant-rank theorem applied to an orbit map $G\to M$ gives each orbit its immersed-submanifold structure; embeddedness requires additional hypotheses such as properness of the action.

> [!tip] The Mass Shell in Quantum Field Theory *(from Physics)*
> The on-shell condition $p^\mu p_\mu = -m^2 c^2$ in [[Special Relativity III — Minkowski Spacetime and the Metric|Minkowski space]] defines the mass shell as a regular level set — a $3$-dimensional hyperboloid in $4$-momentum space. Quantum field theory's on-shell scattering amplitudes are defined precisely on this submanifold; off-shell extensions to all of momentum space are propagators integrated against. The submanifold structure of the mass shell is what makes the on-shell / off-shell distinction precise.
