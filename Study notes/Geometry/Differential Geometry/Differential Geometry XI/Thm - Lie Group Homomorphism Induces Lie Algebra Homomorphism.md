---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Lie Group Homomorphism"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - Lie Algebra"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ and $H$ are Lie groups with Lie algebras $\mathfrak{g}$ and $\mathfrak{h}$, identities $e_G$ and $e_H$. A Lie group homomorphism is $F : G \to H$. Its differential at the identity is $F_* = dF_{e_G} : \mathfrak{g} \to \mathfrak{h}$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Statement

> **Theorem.** Let $F : G \to H$ be a Lie group homomorphism between Lie groups. Then the differential $F_* = dF_{e_G} : \mathfrak{g} \to \mathfrak{h}$ is a Lie algebra homomorphism: it is linear and preserves the bracket,
> $$F_*[X, Y]_{\mathfrak{g}} = [F_* X, F_* Y]_{\mathfrak{h}} \qquad \text{for all } X, Y \in \mathfrak{g}.$$

> **Corollary (functoriality).** The assignment $G \mapsto \mathfrak{g}$, $F \mapsto F_*$ defines a functor $\mathrm{Lie} : \mathbf{LieGrp} \to \mathbf{LieAlg}$ from the category of Lie groups to the category of (finite-dimensional real) Lie algebras.

---

# Motivation

Lie groups have two structures — a smooth manifold and a group — and the natural morphisms (Lie group homomorphisms) respect both. The Lie algebra is the linearization of a Lie group at the identity, capturing infinitesimal data. A natural question is: do the morphisms of Lie groups linearize to morphisms of Lie algebras? More precisely, given a Lie group homomorphism $F : G \to H$, does $F_* = dF_e$ preserve the Lie algebra structure?

The answer, yes, is what makes the Lie functor possible. If $F_*$ only preserved linearity (which is automatic for a differential), then $\mathrm{Lie}$ would be a functor only into vector spaces. The bracket-preservation is what upgrades it to a functor into Lie algebras, and this is what makes the Lie correspondence meaningful: a Lie group homomorphism is the same data as a Lie algebra homomorphism (at the level of differentials), at least when the target side is simply connected.

The functoriality is the bookkeeping payoff: $(F \circ G)_* = F_* \circ G_*$ and $(\mathrm{id})_* = \mathrm{id}$. This is just the chain rule for differentials, combined with the bracket-preservation property. Together, functoriality makes the Lie functor a well-defined arrow between categories.

The theorem matters most because it underlies the strategy of converting Lie group questions into Lie algebra questions. A question about $F : G \to H$ — whether it is surjective, whether it has a section, whether two such $F$ agree — frequently becomes a question about $F_* : \mathfrak{g} \to \mathfrak{h}$, which is linear and finite-dimensional. This is the strategic content of the Lie correspondence.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a Lie group homomorphism. Recognition of when one is present is straightforward in classical cases; the non-obvious sources are when a homomorphism "appears" out of geometric data.

The first source is **a smooth representation** $\rho : G \to \mathrm{GL}(V)$ of $G$ on a vector space. Property $B$ is "$G$ acts smoothly and linearly on a vector space". The bridge is that $\rho$ is then a Lie group homomorphism into $\mathrm{GL}(V)$, and this theorem gives a Lie algebra representation $\rho_* : \mathfrak{g} \to \mathfrak{gl}(V)$, $\rho_*(X)(v) = \frac{d}{dt}|_{t=0} \rho(\exp(tX))(v)$. This is how Lie algebra representations are extracted from group representations.

A second source is **the adjoint action** $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$. Property $B$ is "$G$ acts on $\mathfrak{g}$ by linearization of conjugation". The bridge: $\mathrm{Ad}$ is a Lie group homomorphism, hence $\mathrm{Ad}_* : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ is a Lie algebra homomorphism. By Lee Thm 20.27, $\mathrm{Ad}_* = \mathrm{ad}$, the Lie algebra adjoint $\mathrm{ad}_X(Y) = [X, Y]$. See [[Def - Adjoint Representation]].

A third source is **a Lie group action** $\theta : G \to \mathrm{Diff}(M)$ on a smooth manifold (treating $\mathrm{Diff}(M)$ formally as an infinite-dimensional Lie group). Property $B$ is "$G$ acts smoothly on $M$". The bridge: the differential at $e_G$ is a Lie algebra homomorphism $\mathfrak{g} \to \mathfrak{X}(M)$ (with care about left vs right actions — left actions give an anti-homomorphism, Lee Thm 20.18). This is the **infinitesimal generator** of the action.

A fourth source is **an inclusion of Lie subgroups** $H \hookrightarrow G$. Property $B$ is "$H$ is a Lie subgroup". The bridge: $\iota_* : \mathfrak{h} \to \mathfrak{g}$ is a Lie algebra homomorphism, which by linearity of $\iota_*$ is just the inclusion $\mathfrak{h} \subseteq \mathfrak{g}$ (with $\mathfrak{h}$ a Lie subalgebra by the theorem).

**Targets (Output Amplification)**

The conclusion is "$F_*$ is a Lie algebra homomorphism". Combined with further structure, this conclusion amplifies.

The first amplification is **functorial properties**: $(F \circ G)_* = F_* \circ G_*$ and $(\mathrm{id})_* = \mathrm{id}$. Hence Lie group isomorphisms give Lie algebra isomorphisms. So if $G \cong H$ as Lie groups, then $\mathfrak{g} \cong \mathfrak{h}$ as Lie algebras. The converse fails (as $\mathrm{SO}(3) \not\cong \mathrm{SU}(2)$ illustrates), and this failure is what motivates the Lie correspondence on the simply-connected side.

A second amplification is **kernel and image**. The kernel $\ker F_* \subseteq \mathfrak{g}$ is a Lie subalgebra (in fact an ideal); the image $\mathrm{im}(F_*) \subseteq \mathfrak{h}$ is a Lie subalgebra. These correspond to closed Lie subgroups: $\ker F$ is a closed normal Lie subgroup of $G$ with $\mathrm{Lie}(\ker F) = \ker F_*$, and $\mathrm{im}(F) \leq H$ is a (possibly non-embedded) Lie subgroup with $\mathrm{Lie}(\mathrm{im}(F)) = \mathrm{im}(F_*)$.

A third amplification is **isomorphism criterion**. For a Lie group homomorphism $F : G \to H$ between connected Lie groups, $F_* : \mathfrak{g} \to \mathfrak{h}$ being an isomorphism implies $F$ is a local diffeomorphism (by the inverse function theorem applied at $e$, plus the constant-rank theorem). When $G$ is simply connected, $F$ is then a covering map onto its image — a strong structural conclusion.

A fourth amplification is **the Lie correspondence**: when $G$ is simply connected, every Lie algebra homomorphism $\varphi : \mathfrak{g} \to \mathfrak{h}$ is $F_*$ for a unique Lie group homomorphism $F : G \to H$. This is the integration direction of the correspondence (Lee Thm 20.19), and it makes the Lie functor an equivalence of categories on the simply-connected side.

---

# Why Is It True

The proof rests on the same fact as [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]]: pushforward of vector fields by a smooth map commutes with the Lie bracket *when the relevant vector fields are $F$-related*. For a Lie group homomorphism $F : G \to H$, the key observation is that left-invariant vector fields on $G$ are $F$-related to left-invariant vector fields on $H$.

Specifically: for $X \in \mathfrak{g}$, the left-invariant vector field $X^L$ on $G$ is $F$-related to the left-invariant vector field $(F_* X)^L$ on $H$. To see this, note that $F$ is **equivariant** with respect to left translations: $F \circ L_g = L_{F(g)} \circ F$. Differentiating at any point $g'$:

$$dF_{gg'} \circ d(L_g)_{g'} = d(L_{F(g)})_{F(g')} \circ dF_{g'}.$$

Apply both sides to $X^L|_{g'} = d(L_{g'})_e(X_e)$, and trace through: $dF_{gg'}(X^L|_{gg'})$ vs $(F_* X)^L|_{F(gg')}$... The cleanest version is to use the "$F$-related" definition: $X^L$ and $(F_* X)^L$ are $F$-related iff $dF_g(X^L|_g) = (F_* X)^L|_{F(g)}$ for all $g$. The verification:

$$dF_g(X^L|_g) = dF_g \circ d(L_g)_e(X_e) = d(F \circ L_g)_e(X_e) = d(L_{F(g)} \circ F)_e(X_e) = d(L_{F(g)})_{F(e)} \circ dF_e(X_e) = d(L_{F(g)})_{e_H}(F_* X) = (F_* X)^L|_{F(g)},$$

using equivariance of $F$ in the second-to-last equality.

**The bolded mechanism summary: left-invariant vector fields on $G$ push forward to left-invariant vector fields on $H$ under a Lie group homomorphism, and the pushforward of a bracket equals the bracket of pushforwards — so $F_*$ preserves the bracket.**

The second ingredient is the **naturality of the Lie bracket under $F$-relation** (Lee Prop 8.30): if $X_1$ is $F$-related to $Y_1$ and $X_2$ is $F$-related to $Y_2$, then $[X_1, X_2]$ is $F$-related to $[Y_1, Y_2]$. Applied to $X^L \sim (F_* X)^L$ and $Y^L \sim (F_* Y)^L$, this gives $[X^L, Y^L]$ is $F$-related to $[(F_* X)^L, (F_* Y)^L]$. Evaluating at $e_G$: $dF_e([X, Y]_e^L) = [F_* X, F_* Y]^L|_e = [F_* X, F_* Y]_{\mathfrak{h}}$. The left side is $F_*[X, Y]_\mathfrak{g}$. Done.

---

# What Makes This Hard

The main subtlety is **the $F$-relation step**: a Lie group homomorphism $F$ takes left-invariant vector fields on $G$ to left-invariant vector fields on $H$, but only in the "$F$-related" sense — pushforward at each point of $G$, but with the result varying smoothly over $G$. The most common error is to skip this step and try to compute the bracket of $X$ and $Y$ via local coordinate formulas; the equivariance of $F$ is what makes the result clean.

A second subtlety is **the bracket on $\mathfrak{g}$ being the vector-field bracket evaluated at $e$**, not some other operation. The definition of the bracket on $\mathfrak{g}$ as the transport of the vector-field bracket from $\mathrm{Lie}(G)$ is essential here: without it, "bracket-preservation" would be ambiguous.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Show that the left-invariant vector field $X^L$ on $G$ is $F$-related to the left-invariant vector field $(F_* X)^L$ on $H$, using equivariance of $F$ under left translation. Then apply the general $F$-related bracket lemma: $F$-related vector fields have $F$-related brackets. Evaluating at $e_G$ gives $F_*[X, Y] = [F_* X, F_* Y]$.

**Subgoal decomposition:**

1. **$F$-relation of left-invariant vector fields.** Show $X^L$ on $G$ is $F$-related to $(F_* X)^L$ on $H$: $dF_g(X^L|_g) = (F_* X)^L|_{F(g)}$.
   - *Hint:* Use $F \circ L_g = L_{F(g)} \circ F$ (equivariance of $F$) and differentiate at $e$.
   - *Why needed:* This is what lets the bracket of left-invariant vector fields transport correctly under $F$.

2. **$F$-related brackets are $F$-related.** Apply the general lemma: if $X_1 \sim_F Y_1$ and $X_2 \sim_F Y_2$ (meaning $dF \circ X_i = Y_i \circ F$), then $[X_1, X_2] \sim_F [Y_1, Y_2]$.
   - *Hint:* Test against functions: $X_1(f \circ F) = (Y_1 f) \circ F$, iterate, take bracket.
   - *Why needed:* It is the smooth-map generalization of Lemma 1 in [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]]; combined with Step 1 it gives the bracket-preservation conclusion.

3. **Evaluate at $e_G$.** Use $[X^L, Y^L]$ is $F$-related to $[(F_* X)^L, (F_* Y)^L]$; evaluate at $e_G$ to extract $F_*$ on $T_e G \to T_{e_H} H$.
   - *Hint:* The bracket on $\mathfrak{g} \cong T_e G$ is $[X, Y]_\mathfrak{g} = [X^L, Y^L]_e$ (definition of the transported bracket), and the bracket on $\mathfrak{h}$ similarly.
   - *Why needed:* This is where the bracket-preservation conclusion is extracted from $F$-relation of vector fields.

---

# Lemma Decomposition

> [!note]- Lemma 1: Equivariance of $F$ under left translation
> **Statement:** For a Lie group homomorphism $F : G \to H$ and any $g \in G$, $F \circ L_g = L_{F(g)} \circ F$ as smooth maps $G \to H$.
>
> **Hint:** Direct computation from the homomorphism property.
>
> **Why needed:** It is the algebraic identity that makes $F$ transport left-invariant vector fields to left-invariant vector fields.
>
> > [!note]- Full proof
> > For $g' \in G$, $(F \circ L_g)(g') = F(g g') = F(g) F(g') = L_{F(g)}(F(g')) = (L_{F(g)} \circ F)(g')$.

> [!note]- Lemma 2: $X^L$ is $F$-related to $(F_* X)^L$
> **Statement:** Let $F : G \to H$ be a Lie group homomorphism, $X \in \mathfrak{g}$. Then the left-invariant vector field $X^L$ on $G$ is $F$-related to $(F_* X)^L$ on $H$: $dF_g(X^L|_g) = (F_* X)^L|_{F(g)}$ for all $g \in G$.
>
> **Hint:** Use Lemma 1 to factor $F \circ L_g$, differentiate at $e$, and apply chain rule.
>
> **Why needed:** It says Lie group homomorphisms preserve left-invariance at the level of vector fields, so brackets transport correctly.
>
> > [!note]- Full proof
> > $$dF_g(X^L|_g) = dF_g \circ d(L_g)_e(X_e) = d(F \circ L_g)_e(X_e) = d(L_{F(g)} \circ F)_e(X_e) = d(L_{F(g)})_{F(e)} \circ dF_e(X_e) = d(L_{F(g)})_{e_H}(F_* X) = (F_* X)^L|_{F(g)}.$$
> > The third equality uses Lemma 1, the fifth uses $F(e) = e_H$.

> [!note]- Lemma 3: $F$-related brackets
> **Statement:** Suppose $F : M \to N$ is smooth and $X_1, X_2 \in \mathfrak{X}(M)$, $Y_1, Y_2 \in \mathfrak{X}(N)$ with $X_i \sim_F Y_i$. Then $[X_1, X_2] \sim_F [Y_1, Y_2]$.
>
> **Hint:** Test against $f \in C^\infty(N)$ by tracking $X_1 X_2 (f \circ F)$ and $Y_1 Y_2 f \circ F$.
>
> **Why needed:** It is the smooth-map (not-necessarily-diffeomorphism) generalization of "pushforward preserves bracket", and combined with Lemma 2 it gives the bracket-preservation property of $F_*$.
>
> > [!note]- Full proof
> > For $f \in C^\infty(N)$, $X_i \sim_F Y_i$ means $X_i(f \circ F) = (Y_i f) \circ F$ for every $f$. Applying twice:
> > $$X_1 X_2 (f \circ F) = X_1 ((Y_2 f) \circ F) = (Y_1 Y_2 f) \circ F.$$
> > Similarly $X_2 X_1 (f \circ F) = (Y_2 Y_1 f) \circ F$. Subtracting,
> > $$[X_1, X_2](f \circ F) = (Y_1 Y_2 f - Y_2 Y_1 f) \circ F = ([Y_1, Y_2] f) \circ F,$$
> > so $[X_1, X_2] \sim_F [Y_1, Y_2]$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : G \to H$ be a Lie group homomorphism, with Lie algebras $\mathfrak{g}, \mathfrak{h}$. Let $X, Y \in \mathfrak{g}$, identified with their left-invariant vector fields $X^L, Y^L$ on $G$.
>
> **Linearity of $F_*$.** $F_* = dF_{e_G}$ is the differential of a smooth map at a point, hence is a linear map $T_{e_G} G \to T_{e_H} H$, i.e., $\mathfrak{g} \to \mathfrak{h}$.
>
> **Bracket preservation.** By Lemma 2, $X^L \sim_F (F_* X)^L$ and $Y^L \sim_F (F_* Y)^L$. By Lemma 3, $[X^L, Y^L] \sim_F [(F_* X)^L, (F_* Y)^L]$. Evaluating both sides at $e_G$ and using $F(e_G) = e_H$:
> $$dF_{e_G}([X^L, Y^L]|_{e_G}) = [(F_* X)^L, (F_* Y)^L]|_{e_H}.$$
> By definition of the bracket on $\mathfrak{g}$ via left-invariant vector fields, $[X^L, Y^L]|_{e_G} = [X, Y]_\mathfrak{g}$, and similarly on the right. Hence
> $$F_*[X, Y]_\mathfrak{g} = [F_* X, F_* Y]_\mathfrak{h}. \qquad\blacksquare$$
>
> **Functoriality.** $(F \circ G)_* = F_* \circ G_*$ is the chain rule for differentials at $e$. $(\mathrm{id}_G)_* = \mathrm{id}_\mathfrak{g}$ is immediate. Hence $G \mapsto \mathfrak{g}$, $F \mapsto F_*$ is a functor $\mathbf{LieGrp} \to \mathbf{LieAlg}$.

---

# Cross-Field Exercise Suggestions

**Representation theory — differentiating a Lie group representation.** Given a Lie group representation $\rho : G \to \mathrm{GL}(V)$, the differential $\rho_* : \mathfrak{g} \to \mathfrak{gl}(V)$ is a Lie algebra representation, by this theorem. Concrete computation: for $G = \mathrm{SU}(2)$ and the defining representation $\rho : \mathrm{SU}(2) \to \mathrm{GL}(\mathbb{C}^2)$, compute $\rho_* : \mathfrak{su}(2) \to \mathfrak{gl}(\mathbb{C}^2)$ as the inclusion of skew-Hermitian traceless matrices into $\mathfrak{gl}(2, \mathbb{C})$. Then differentiate the adjoint representation $\mathrm{Ad} : \mathrm{SU}(2) \to \mathrm{SO}(3)$ to recover $\mathrm{ad} : \mathfrak{su}(2) \to \mathfrak{so}(3)$, the bracket on $\mathfrak{su}(2)$ — a self-referential consistency check.

**Algebraic topology — covering maps via Lie group homomorphisms.** A Lie group homomorphism $F : G \to H$ with $F_*$ an isomorphism and $G$ connected is a covering map (it is a local diffeomorphism by the inverse function theorem applied at $e$, plus constant rank, plus surjectivity onto the identity component of $H$). The kernel $\ker F$ is then a discrete normal subgroup of $G$, hence central. The canonical example: $\mathrm{SU}(2) \to \mathrm{SO}(3)$, kernel $\{\pm I\}$.

**Quantum mechanics — angular momentum operators as Lie algebra representations.** The angular momentum operators $L_x, L_y, L_z$ on $L^2(\mathbb{R}^3)$ are obtained as the differential of the rotation action $\rho : \mathrm{SO}(3) \to \mathrm{U}(L^2(\mathbb{R}^3))$. They satisfy the $\mathfrak{so}(3)$ commutation relations $[L_x, L_y] = i\hbar L_z$ (and cyclic) — exactly the Lie algebra bracket of $\mathfrak{so}(3)$ pushed forward to the unitary group's Lie algebra. The bracket-preservation conclusion of this theorem is the source of the canonical commutation relations.

---

# Bridges

- **[[Thm - Naturality of the Exponential Map|Naturality of exp]]** — once $F_*$ is established as a Lie algebra homomorphism, the natural next question is whether $F$ and $F_*$ are compatible with the exponential map. The answer is yes: $F \circ \exp_G = \exp_H \circ F_*$. So the two functors "Lie algebra at $e$" and "exponential map" cohere on Lie group homomorphisms. This is the bridge between Lie group homomorphisms and Lie algebra homomorphisms via the exponential.

- **The Lie correspondence** (Lee Thm 20.19) — the converse to this theorem on the simply-connected side. Every Lie algebra homomorphism $\varphi : \mathfrak{g} \to \mathfrak{h}$ with $G$ simply connected integrates uniquely to a Lie group homomorphism $F : G \to H$ with $F_* = \varphi$. So $\mathrm{Lie}$ is an equivalence of categories on $\mathbf{LieGrp}^{1\text{-conn}}$, with this theorem providing the linearization direction.

- **The functor $\mathrm{Lie}$ to vector bundles** — more abstractly, the Lie functor is part of a larger family of "linearization" functors. For a Lie groupoid (rather than just a Lie group), the analogue is the **Lie algebroid functor**. For a Lie group acting on a manifold, the analogue is the **infinitesimal generator** map $\mathfrak{g} \to \mathfrak{X}(M)$.

---

# Unlocked by This

> [!tip] Lie Functor *(from Category Theory of Lie Theory)*
> $\mathrm{Lie} : \mathbf{LieGrp} \to \mathbf{LieAlg}$ is a functor from Lie groups to finite-dimensional Lie algebras. Combined with the integration direction of the Lie correspondence on the simply-connected side, it becomes an equivalence of categories between simply connected Lie groups and Lie algebras.

> [!tip] Lie Algebra Representation from Lie Group Representation *(from Representation Theory)*
> Every Lie group representation $\rho : G \to \mathrm{GL}(V)$ differentiates to a Lie algebra representation $\rho_* : \mathfrak{g} \to \mathfrak{gl}(V)$. This is how representation theory of Lie groups is reduced to representation theory of Lie algebras, the algebraic theory of which (highest-weight theory, Verma modules, Weyl character formula) gives the structural classification.

> [!tip] Infinitesimal Generator of a Lie Group Action *(from this chapter)*
> A smooth Lie group action $\theta : G \times M \to M$ gives a Lie algebra **anti-homomorphism** (for left actions) $\hat\theta : \mathfrak{g} \to \mathfrak{X}(M)$, the infinitesimal generator. See Lee Thm 20.18 for the sign conventions.

> [!tip] Covering Maps from Lie Algebra Isomorphisms *(from this chapter)*
> If $F : G \to H$ is a Lie group homomorphism between connected Lie groups and $F_*$ is an isomorphism, then $F$ is a covering map (Lee Thm 21.32). The kernel of a covering homomorphism is a discrete central subgroup. This is the source of the classification of connected Lie groups with a fixed Lie algebra by their central subgroups.
