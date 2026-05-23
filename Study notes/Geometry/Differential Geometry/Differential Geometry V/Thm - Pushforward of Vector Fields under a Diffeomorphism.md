---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Diffeomorphism"
  - "Def - F-Related Vector Fields"
  - "Def - The Differential of a Smooth Map"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds. When $F$ is a [[Def - Diffeomorphism|diffeomorphism]] (smooth with smooth inverse), we write $F^{-1}$ for the inverse and $dF_p : T_p M \to T_{F(p)} N$ for the [[Def - The Differential of a Smooth Map|differential]] at $p$. $X \in \mathfrak{X}(M)$ is a smooth [[Def - Smooth Vector Field|vector field]] on $M$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Statement

> **Theorem (Pushforward under a diffeomorphism; Lee Proposition 8.19).** Let $F : M \to N$ be a diffeomorphism. For every smooth vector field $X \in \mathfrak{X}(M)$, there is a unique smooth vector field $F_* X \in \mathfrak{X}(N)$ that is **$F$-related** to $X$:
> $$dF_p(X_p) = (F_*X)_{F(p)} \qquad \text{for every } p \in M.$$
>
> Equivalently, $F_* X$ is defined by the pointwise formula
> $$(F_* X)_q := dF_{F^{-1}(q)}\big(X_{F^{-1}(q)}\big) \qquad \text{for every } q \in N.$$

> **Corollary (Properties of $F_*$).** The map $F_* : \mathfrak{X}(M) \to \mathfrak{X}(N)$ has the following properties:
>
> (a) **$\mathbb{R}$-linearity.** $F_*(aX + bY) = aF_*X + bF_*Y$ for $a, b \in \mathbb{R}$.
>
> (b) **Lie algebra homomorphism.** $F_*[X, Y] = [F_*X, F_*Y]$ — the pushforward is a Lie algebra isomorphism, with inverse $(F^{-1})_*$.
>
> (c) **Function product rule.** $F_*(fX) = (f \circ F^{-1})(F_*X)$ for $f \in C^\infty(M)$.
>
> (d) **Flow naturality.** If $\phi^X_t$ is the flow of $X$, then the flow of $F_*X$ is $\phi^{F_*X}_t = F \circ \phi^X_t \circ F^{-1}$ wherever defined.

---

# Motivation

For a general smooth map $F : M \to N$, vector fields cannot be unambiguously transferred from $M$ to $N$: pointwise pushforward $dF_p(X_p)$ might be undefined at points of $N$ outside $F(M)$, or might be ambiguous at points with multiple preimages. So [[Def - F-Related Vector Fields|F-relatedness]] is a relation, not a construction.

When $F$ is a diffeomorphism, both obstructions vanish: $F$ is bijective so every $q \in N$ has a unique preimage, and the pointwise formula $(F_*X)_q := dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ unambiguously defines a vector field on $N$. The theorem certifies that this works: $F_* X$ is a well-defined smooth vector field, it is $F$-related to $X$, and it is unique with this property.

The role of this theorem in the chapter: it provides the **functoriality of vector fields under [[Def - Diffeomorphism|diffeomorphisms]]**. Every concept in the chapter — vector fields, integral curves, flows, Lie brackets, Lie derivatives — is preserved by diffeomorphism (in the pushforward sense). So the entire chapter is a *diffeomorphism-invariant* subject, and changing coordinates by a diffeomorphism is a free operation in any computation. The corollaries (a)–(d) say specifically: pushforward respects the vector-space structure, the Lie algebra structure, the [[Def - Module|module]] structure (with function pullback), and the flow structure.

The geometric content: a diffeomorphism produces a "renaming" of the manifold, and pushforward is the corresponding renaming of vector fields. Under this renaming, all geometric structures transfer cleanly. This is the precise version of "differential geometry is a topic about manifolds up to diffeomorphism".

Beyond diffeomorphisms, the formula $dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ breaks: the inverse $F^{-1}$ is unavailable in general, and "pushforward" loses meaning. The substitute is $F$-relatedness, which is a *relation* rather than a *map*; pushforward is the special case where the relation is single-valued.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$F : M \to N$ is a diffeomorphism". The skill is recognizing this hypothesis in problems where the map is presented in a different way.

The first disguised source is **a change of coordinates / chart**. Property $B$: passing from chart $(U, (x^i))$ to chart $(\tilde U, (\tilde x^j))$ via the transition map $\tilde x = \tilde x(x)$ — which is, on the overlap, a diffeomorphism. The bridge: the transition map *is* $F$, and the pushforward of a vector field in $x$-coordinates is its representation in $\tilde x$-coordinates. The transformation rule for components $\tilde X^j = X^i (\partial \tilde x^j / \partial x^i)$ is exactly the pointwise pushforward formula.

The second disguised source is **a Lie group acting on a manifold.** Property $B$: an action $G \times M \to M$ of a Lie group on a manifold; for each $g \in G$, the map $\Phi_g : M \to M$, $\Phi_g(p) = g \cdot p$, is a diffeomorphism. The bridge: $(\Phi_g)_*$ acts on $\mathfrak{X}(M)$, and equivariant vector fields are those fixed by every $(\Phi_g)_*$. This is the foundation of equivariant geometry.

The third disguised source is **a one-parameter family of diffeomorphisms.** Property $B$: a smooth one-parameter family $F_t$ of diffeomorphisms, e.g. the flow of some vector field. The bridge: each $F_t$ is a diffeomorphism, so $(F_t)_*$ acts on vector fields. Differentiating $(F_t)_* X$ at $t = 0$ when $F_t$ is the flow of $V$ recovers the Lie derivative $\mathcal{L}_V X = -[V, X]$ (with the sign coming from the pull-back convention).

**Targets (Output Amplification)**

The conclusion is "the pushforward is a unique smooth vector field with all the natural properties". Combined with one further property, this amplifies.

The first combination is **pushforward + Lie group structure gives an action on the Lie algebra.** Property $D$: a Lie group $G$ acting on $M$. The amplification: every $g \in G$ acts on $\mathfrak{X}(M)$ via $(\Phi_g)_*$, giving a representation of $G$ on $\mathfrak{X}(M)$. Differentiating at the identity gives an action of $\mathfrak{g}$ on $\mathfrak{X}(M)$ — the **infinitesimal generator** map plus the Lie derivative.

The second combination is **pushforward + the Lie bracket gives the naturality of the Lie algebra structure.** Property $D$: any diffeomorphism $F : M \to N$. The amplification: $F_*$ is a Lie algebra isomorphism, so the Lie algebra structure of $\mathfrak{X}(M)$ is a diffeomorphism invariant. In particular, two manifolds with non-isomorphic vector field Lie algebras cannot be diffeomorphic.

The third combination is **pushforward + the flow gives diffeomorphism invariance of dynamics.** Property $D$: a diffeomorphism $F$ that pushes $X$ to $F_* X$. The amplification: the flow of $F_* X$ is the conjugate flow $F \circ \phi^X_t \circ F^{-1}$ — so the dynamics of $X$ and $F_* X$ are equivalent up to the diffeomorphism $F$. This is the substance of "differentiable conjugacy" in dynamical systems.

---

# Why Is It True

**The mechanism in one sentence: a diffeomorphism $F$ has an invertible differential at every point, so the pointwise formula $(F_*X)_q = dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ unambiguously specifies a tangent vector at every $q \in N$, with smoothness following from the smoothness of $F$, $F^{-1}$, and $X$.**

Unpack the proof of each statement:

**Existence of $F_* X$.** The formula $(F_* X)_q := dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ defines $F_* X$ as a vector field on $N$: at each $q$ we evaluate $F^{-1}(q)$ (well-defined since $F$ is bijective), evaluate $X$ at that point (giving a tangent vector in $T_{F^{-1}(q)} M$), and apply $dF_{F^{-1}(q)}$ (giving a tangent vector in $T_q N$). Each step is well-defined for diffeomorphisms.

**Smoothness of $F_* X$.** $F_* X$ as a map $N \to TN$ is the composition $N \xrightarrow{F^{-1}} M \xrightarrow{X} TM \xrightarrow{dF} TN$. Each map is smooth: $F^{-1}$ by assumption on the diffeomorphism, $X$ by assumption on the vector field, $dF$ as the differential of a smooth map (a smooth bundle map). So $F_* X$ is smooth.

**$F$-relatedness.** Direct check: $dF_p(X_p) = (F_* X)_{F(p)}$ by the formula, with $p = F^{-1}(F(p))$.

**Uniqueness.** If $Y$ and $Y'$ on $N$ are both $F$-related to $X$, then for any $q \in N$, writing $p = F^{-1}(q)$, both $Y_q$ and $Y'_q$ equal $dF_p(X_p)$. Hence $Y = Y'$.

**Lie algebra homomorphism.** By the naturality of the Lie bracket ([[Thm - Lie Bracket Properties]], part (f)), $X \sim_F F_*X$ and $Y \sim_F F_*Y$ imply $[X, Y] \sim_F [F_*X, F_*Y]$. By uniqueness, $F_*[X, Y] = [F_*X, F_*Y]$.

**Function product rule.** $(F_*(fX))_q = dF_{F^{-1}(q)}(f(F^{-1}(q)) X_{F^{-1}(q)}) = f(F^{-1}(q)) \cdot dF_{F^{-1}(q)}(X_{F^{-1}(q)}) = (f \circ F^{-1})(q) \cdot (F_*X)_q$.

**Flow naturality.** By [[Def - F-Related Vector Fields]] characterization (iii) — applied to the $F$-relation $X \sim_F F_*X$ — $F$ takes the flow of $X$ to the flow of $F_* X$: $F \circ \phi^X_t = \phi^{F_*X}_t \circ F$ on the appropriate domain. Composing with $F^{-1}$: $\phi^{F_*X}_t = F \circ \phi^X_t \circ F^{-1}$ on $F(\text{flow domain of }\phi^X)$.

The whole theorem is therefore an unpacking of the diffeomorphism property and the naturality of $F$-related fields.

---

# What Makes This Hard

There is almost no "hard" content in this theorem at the level of differential geometry — it is a direct consequence of definitions and the naturality of the bracket. The subtle points are: (i) recognizing that pushforward is *only* defined for diffeomorphisms, not for arbitrary smooth maps (the general analogue is $F$-relatedness, which is a relation, not a map); (ii) the function product rule (c) requires careful tracking of $f$ vs $f \circ F^{-1}$ — the function on $N$ is the pullback of $f$ through $F^{-1}$, and getting this wrong is a common error.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Existence is by the pointwise formula. Smoothness is composition of smooth maps. Uniqueness follows from the value at each point being forced. The corollaries follow from the existing properties of the Lie bracket and $F$-related fields.

**Subgoal decomposition:**

1. **Pointwise formula.** $(F_*X)_q := dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ defines $F_*X$ as a section of $TN$.
   - *Hint:* Each step is well-defined for diffeomorphisms — $F^{-1}$ exists, $X$ evaluates, $dF$ is invertible.
   - *Why needed:* This is the construction.

2. **Smoothness.** $F_*X = dF \circ X \circ F^{-1}$ as a map $N \to TN$, composition of smooth maps.
   - *Hint:* $F, F^{-1}, X, dF$ are all smooth.
   - *Why needed:* Verifies that $F_*X$ is smooth.

3. **$F$-relatedness.** $dF_p(X_p) = (F_*X)_{F(p)}$ by definition.
   - *Hint:* Substitute $q = F(p)$ into the pointwise formula.
   - *Why needed:* Confirms $F_*X$ has the defining property.

4. **Uniqueness.** Any vector field on $N$ that is $F$-related to $X$ must equal $F_*X$ pointwise.
   - *Hint:* Both must satisfy $dF_p(X_p) = Y_{F(p)}$, so their values agree at every $q = F(p)$.
   - *Why needed:* Justifies the article "the unique vector field $F$-related to $X$".

5. **Lie algebra homomorphism property.** Naturality of the bracket plus uniqueness.
   - *Hint:* By [[Thm - Lie Bracket Properties]] (f), $[X, Y] \sim_F [F_*X, F_*Y]$; by uniqueness, $F_*[X, Y] = [F_*X, F_*Y]$.
   - *Why needed:* This is the most important structural property.

6. **Flow naturality.** $F$-related fields have $F$-related flows.
   - *Hint:* From [[Def - F-Related Vector Fields]] characterization (iii) or Lee Proposition 9.13.
   - *Why needed:* Shows pushforward respects the entire flow structure.

---

# Lemma Decomposition

> [!note]- Lemma 1: The pointwise formula defines a smooth vector field
> **Statement:** Let $F : M \to N$ be a diffeomorphism and $X \in \mathfrak{X}(M)$. The pointwise formula $(F_*X)_q := dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ for $q \in N$ defines a smooth section of $TN$.
>
> **Hint:** $F_*X = dF \circ X \circ F^{-1}$ as a map $N \to TN$; each factor is smooth.
>
> **Why needed:** Establishes that $F_*X$ is a well-defined smooth vector field.
>
> > [!note]- Full proof
> > Each step is well-defined: $F^{-1}(q)$ exists because $F$ is bijective, $X_{F^{-1}(q)} \in T_{F^{-1}(q)} M$ because $X$ is a section of $TM$, $dF_{F^{-1}(q)}(X_{F^{-1}(q)}) \in T_q N$ because $dF_{F^{-1}(q)}$ maps $T_{F^{-1}(q)} M$ to $T_{F(F^{-1}(q))} N = T_q N$. So $(F_*X)_q \in T_q N$, making $F_*X$ a section of $TN$.
> >
> > For smoothness, note that $F_*X : N \to TN$ is the composition $N \xrightarrow{F^{-1}} M \xrightarrow{X} TM \xrightarrow{dF} TN$, where $dF : TM \to TN$ is the global bundle map induced by $F$ (sending $(p, v) \mapsto (F(p), dF_p(v))$). Smoothness of $F, F^{-1}$ (diffeomorphism), $X$ (smooth vector field), $dF$ (differential of a smooth map) — all smooth — yields smoothness of $F_*X$.

> [!note]- Lemma 2: $F_*X$ is the unique $F$-related vector field
> **Statement:** $X \sim_F F_*X$. If $Y \in \mathfrak{X}(N)$ satisfies $X \sim_F Y$, then $Y = F_*X$.
>
> **Hint:** The $F$-related condition $dF_p(X_p) = Y_{F(p)}$ for all $p$ determines $Y$ pointwise at every $F(p) \in N$, and $F$ is surjective.
>
> **Why needed:** Justifies the article "the" in the statement.
>
> > [!note]- Full proof
> > Direct check: by the pointwise formula, $(F_*X)_{F(p)} = dF_p(X_p)$, so $X \sim_F F_*X$.
> >
> > For uniqueness: suppose $Y \in \mathfrak{X}(N)$ with $X \sim_F Y$. For any $q \in N$, write $q = F(p)$ for the unique $p = F^{-1}(q)$. Then $Y_q = Y_{F(p)} = dF_p(X_p) = (F_*X)_q$. Hence $Y = F_*X$.

> [!note]- Lemma 3: $F_*$ is a Lie algebra homomorphism
> **Statement:** $F_*$ is $\mathbb{R}$-linear and respects the Lie bracket: $F_*[X, Y] = [F_*X, F_*Y]$.
>
> **Hint:** Linearity follows from linearity of $dF$. Bracket-preservation follows from naturality of the bracket plus uniqueness.
>
> **Why needed:** This is the structural property that makes pushforward useful.
>
> > [!note]- Full proof
> > *Linearity:* $(F_*(aX + bY))_q = dF_{F^{-1}(q)}((aX + bY)_{F^{-1}(q)}) = a \cdot dF_{F^{-1}(q)}(X_{F^{-1}(q)}) + b \cdot dF_{F^{-1}(q)}(Y_{F^{-1}(q)}) = a (F_*X)_q + b (F_*Y)_q$.
> >
> > *Bracket:* by Lemma 2, $X \sim_F F_*X$ and $Y \sim_F F_*Y$. By the naturality of the Lie bracket ([[Thm - Lie Bracket Properties]] part (f)), $[X, Y] \sim_F [F_*X, F_*Y]$. By Lemma 2's uniqueness applied to the bracket, $F_*[X, Y] = [F_*X, F_*Y]$.

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $(F_*X)_q := dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ defines a smooth vector field on $N$.
>
> By Lemma 2, $F_*X$ is the unique vector field on $N$ that is $F$-related to $X$.
>
> By Lemma 3, $F_* : \mathfrak{X}(M) \to \mathfrak{X}(N)$ is $\mathbb{R}$-linear and a Lie algebra homomorphism. Since $F^{-1}$ is also a diffeomorphism, $(F^{-1})_*$ is similarly a Lie algebra homomorphism, and $(F^{-1})_* \circ F_* = \mathrm{id}_{\mathfrak{X}(M)}$ (by composing the $F$-relations) and $F_* \circ (F^{-1})_* = \mathrm{id}_{\mathfrak{X}(N)}$. So $F_*$ is a Lie algebra isomorphism with inverse $(F^{-1})_*$.
>
> **Function product rule.** $(F_*(fX))_q = dF_{F^{-1}(q)}((fX)_{F^{-1}(q)}) = f(F^{-1}(q)) \cdot dF_{F^{-1}(q)}(X_{F^{-1}(q)}) = (f \circ F^{-1})(q) \cdot (F_*X)_q$, where we used linearity of $dF_p$ over scalars. Hence $F_*(fX) = (f \circ F^{-1}) \cdot F_*X$.
>
> **Flow naturality.** From [[Def - F-Related Vector Fields]] characterization (iii), $F$-related vector fields have $F$-semiconjugate flows: $F \circ \phi^X_t = \phi^{F_*X}_t \circ F$ on the appropriate domain. Composing with $F^{-1}$ on the right gives $\phi^{F_*X}_t = F \circ \phi^X_t \circ F^{-1}$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Coordinate change for a vector field.** Given a vector field $X = X^i \partial/\partial x^i$ in one chart and a smooth transition $\tilde x = \tilde x(x)$ to another chart, the components in the new chart are $\tilde X^j = X^i \partial \tilde x^j / \partial x^i$ — exactly the pointwise pushforward formula. So all coordinate-change calculations for vector fields are instances of this theorem.

**Equivariant vector fields under a Lie [[Def - Group|group]] action.** A vector field $X$ on $M$ is **equivariant** under a Lie group action $G \times M \to M$ if $(\Phi_g)_* X = X$ for every $g \in G$. The pushforward gives the action of $G$ on $\mathfrak{X}(M)$; equivariant fields are the fixed points of this action. This is the setting of moment maps, reduction, and Hamiltonian symmetry.

**Linearization of a flow around a fixed point.** If $p \in M$ is a fixed point of the flow $\phi^X_t$ ($X_p = 0$), the differential $d(\phi^X_t)_p : T_p M \to T_p M$ defines a one-parameter group of linear transformations of $T_p M$, with generator $L_X := d X_p : T_p M \to T_p M$ in suitable coordinates. The Hartman–Grobman theorem says the local flow near $p$ is topologically conjugate to the linearized flow $e^{tL_X}$ — using pushforward by a (continuous) local conjugacy.

**Diffeomorphism invariance of the Lie algebra of left-invariant vector fields.** On a Lie group $G$, the Lie algebra $\mathfrak{g} = T_e G$ is identified with the left-invariant vector fields; on a different Lie group $G'$ diffeomorphic to $G$ via $F$, the same Lie algebra structure transfers via $F_*$, but $F_*$ does *not* preserve "left-invariant" unless $F$ is a group homomorphism. So the Lie algebra of $G$ as an abstract Lie algebra is a diffeomorphism invariant, but the identification with left-invariant fields depends on the group structure.

---

# Bridges

- **[[Def - F-Related Vector Fields]]** — the general framework. $F$-relatedness is the relation between vector fields on $M$ and on $N$ under any smooth map $F$; pushforward is the special case where $F$ is a diffeomorphism (so the relation is single-valued). All the algebraic identities (Lie bracket naturality, linearity, etc.) come from the $F$-related framework.

- **[[Thm - Lie Bracket Properties]] part (f), Naturality** — the input that gives $F_*[X, Y] = [F_*X, F_*Y]$. Naturality of the bracket is what makes the pushforward a Lie algebra homomorphism; without it, the bracket would not transport along diffeomorphisms.

- **[[Thm - Fundamental Theorem on Flows]] + Naturality of Flows (Lee 9.13)** — together give the flow naturality $\phi^{F_*X}_t = F \circ \phi^X_t \circ F^{-1}$. So a diffeomorphism pushes the flow of $X$ to the flow of $F_*X$, and the two flow domains are diffeomorphic via $F$.

- **Lie group homomorphism** — special case. A Lie group homomorphism $F : G \to H$ pushes left-invariant vector fields to left-invariant vector fields (proof: use the equivariance with respect to left translations), giving an induced Lie algebra homomorphism $\mathfrak{g} \to \mathfrak{h}$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

---

# Unlocked by This

> [!tip] Vector Bundle Pushforward *(from Bundle Theory)*
> The same construction with $TM$ replaced by any vector bundle $E \to M$ over a diffeomorphism gives a pushforward functor on sections. More generally, pullback of sections is always defined (for any smooth map), while pushforward requires a diffeomorphism. The asymmetry is one of the basic facts of bundle theory, and the [[Differential Geometry VIII — Differential Forms|differential forms]] chapter exploits the reverse asymmetry — forms pull back but do not push forward in general.

> [!tip] Lie Functor *(from Lie Theory)*
> The assignment $G \mapsto \mathrm{Lie}(G)$, $F \mapsto F_*$ (for $F$ a Lie group homomorphism) is a covariant functor from Lie groups to Lie algebras — the **Lie functor**. The structure theory of Lie groups and Lie algebras is governed by this functor: the deepest results (Lie's theorems, the exponential map, the closed subgroup theorem) are statements about the Lie functor. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].
