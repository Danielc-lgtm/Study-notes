---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds, $dF_p : T_p M \to T_{F(p)} N$ its [[Def - The Differential of a Smooth Map|differential]] at $p$. $X \in \mathfrak{X}(M)$ and $X' \in \mathfrak{X}(N)$ are smooth [[Def - Smooth Vector Field|vector fields]] on the source and target. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Axiom Motivation

Given a smooth map $F : M \to N$ and a vector field $X$ on $M$, can we transfer $X$ to a vector field on $N$? The naive attempt is to push every value forward: define $X'_q := dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ when this makes sense. But it makes sense only when $F$ is a diffeomorphism — otherwise $F^{-1}(q)$ might be empty (if $F$ is not surjective) or might contain multiple points giving different tangent vectors at $q$ (if $F$ is not injective). So for a generic smooth map there is no "pushforward" of vector fields.

What we *can* always ask is whether *some* vector field $X'$ on $N$ exhibits the matching behaviour: at every $p \in M$, the value of $X'$ at $F(p)$ should be $dF_p(X_p)$. This is a *relation* between $X$ and $X'$, not a construction of one from the other:

$$X \sim_F X' \quad :\Longleftrightarrow \quad dF_p(X_p) = X'_{F(p)} \text{ for every } p \in M.$$

The terminology "$F$-related" is deliberately weak: it does not assert existence, only the matching condition. For a given $X$ there may be no $X'$ that $F$-relates to it, exactly one (if $F$ is a diffeomorphism), or many (if $F$ is not injective and we have freedom outside the image).

Why is this the right concept? Because it captures exactly the data we need for **functoriality** of all the constructions of the chapter:

1. **Flow naturality.** $X \sim_F X'$ if and only if $F$ maps integral curves of $X$ to integral curves of $X'$, equivalently $F \circ \phi^X_t = \phi^{X'}_t \circ F$ wherever defined. So $F$-relatedness is the geometric statement "the flow on $M$ projects to the flow on $N$".

2. **Function pullback.** $X \sim_F X'$ if and only if $X(f \circ F) = (X' f) \circ F$ for every $f \in C^\infty(N)$. So $F$-relatedness is the algebraic statement "$X$ acts on pullbacks the same way $X'$ acts before pullback".

3. **Bracket naturality.** If $X \sim_F X'$ and $Y \sim_F Y'$, then $[X, Y] \sim_F [X', Y']$. So $F$-relatedness is preserved by the Lie bracket; this is *the* functoriality of the bracket under smooth maps (see [[Thm - Lie Bracket Properties]]).

These three equivalent characterizations are the reason $F$-relatedness is the natural concept rather than pushforward. Pushforward, $F_* X$, is the *special case* of $F$-relatedness when $F$ is a diffeomorphism, so that there is a unique $X'$ to call $F_* X$ — see [[Thm - Pushforward of Vector Fields under a Diffeomorphism]].

Why insist on the relation in this form? Because differential geometry is full of situations where vector fields exist on both source and target of a map but neither is a pushforward of the other. Examples:

- The inclusion $S^1 \hookrightarrow \mathbb{R}^2$ has the unit tangent field on $S^1$ $F$-related to the rotation field $-y \partial_x + x \partial_y$ on $\mathbb{R}^2$.
- A submersion $\pi : E \to M$ in a fibre bundle has horizontal vector fields on $E$ $F$-related to their projections on $M$, but the inclusion of fibres is not a diffeomorphism.
- A projection $\mathbb{R}^2 \to \mathbb{R}$ has $\partial_x$ on $\mathbb{R}^2$ $F$-related to $\partial_x$ on $\mathbb{R}$, but is not injective.

In all these cases the natural statement is $F$-relatedness, not pushforward.

A test of correctness: "Could a reader who has never seen this definition invent it from the motivation?" Yes — the chase is essentially forced. The differential $dF_p$ is the only natural way to map $T_p M \to T_{F(p)} N$, and the matching condition $dF_p(X_p) = X'_{F(p)}$ is the only thing one can say about pairs of vector fields under a smooth map.

---

# The Definition

Let $F : M \to N$ be a smooth map between smooth manifolds. Smooth vector fields $X \in \mathfrak{X}(M)$ and $X' \in \mathfrak{X}(N)$ are **$F$-related**, written $X \sim_F X'$, if for every $p \in M$,

$$dF_p(X_p) = X'_{F(p)}.$$

Equivalently (Lee Proposition 8.16):

1. For every $f \in C^\infty(N)$, $\quad X(f \circ F) = (X' f) \circ F$.

2. $F$ takes integral curves of $X$ to integral curves of $X'$: if $\gamma : J \to M$ is an integral curve of $X$, then $F \circ \gamma : J \to N$ is an integral curve of $X'$.

3. The flows commute with $F$: $F \circ \phi^X_t = \phi^{X'}_t \circ F$ wherever both sides are defined (Lee Proposition 9.13).

When $F$ is a diffeomorphism, there is a *unique* vector field on $N$ that is $F$-related to a given $X$, called the **pushforward** $F_* X$ — see [[Thm - Pushforward of Vector Fields under a Diffeomorphism]].

The fundamental **naturality property** of the Lie bracket: if $X_1 \sim_F X'_1$ and $X_2 \sim_F X'_2$, then $[X_1, X_2] \sim_F [X'_1, X'_2]$. (Lee Proposition 8.30, restated in [[Thm - Lie Bracket Properties]].)

---

# Relate to Other Fields / Compression

In category theory, $F$-relatedness is the condition for a square diagram to commute:

$$\begin{array}{ccc} TM & \xrightarrow{dF} & TN \\ X \uparrow & & \uparrow X' \\ M & \xrightarrow{F} & N \end{array}$$

Here $X$ and $X'$ are sections of the tangent bundles, and $F$-relatedness says the diagram commutes — equivalently, the bundle map $dF : TM \to TN$ over $F : M \to N$ intertwines the sections $X$ and $X'$. This is the precise statement that a vector field is a "natural transformation" data when restricted appropriately.

In dynamical systems, $F$-relatedness corresponds to **semiconjugacy** of flows: $F$ semiconjugates the flow of $X$ to the flow of $X'$ via $F \circ \phi^X_t = \phi^{X'}_t \circ F$. Semiconjugacy is the right notion of "equivalence" for non-invertible maps; conjugacy (the diffeomorphism case) is the special case.

In linear algebra, the analogue is intertwining of linear maps: if $A : V \to V$ and $A' : V' \to V'$ are linear maps and $L : V \to V'$ is a linear map with $L \circ A = A' \circ L$, then $A$ and $A'$ are "$L$-intertwined". This is the categorical predecessor of $F$-relatedness; in particular when $V = T_p M$ and $V' = T_{F(p)} N$ at every $p$, smooth vector fields on $M$ and $N$ are $F$-related precisely when their pointwise values are $dF_p$-intertwined at every $p$.

**True name:** $X \sim_F X'$ means **$F$ semiconjugates the flow of $X$ to the flow of $X'$**, equivalently **$dF$ intertwines $X$ and $X'$ at every point**, equivalently **$F$ pulls back $X' f$ to $X(f \circ F)$ for all $f$**.

---

# Examples / Corollaries

**Is an instance: $d/dt$ on $\mathbb{R}$ $F$-related to $-y \partial_x + x \partial_y$ on $\mathbb{R}^2$ under $F(t) = (\cos t, \sin t)$.** Compute: $dF_t(\partial_t) = (-\sin t)\partial_x + (\cos t)\partial_y$, and at the image point $(\cos t, \sin t)$, the rotation field evaluates to $-(\sin t)\partial_x + (\cos t)\partial_y$ — they match. So $F$ takes the integral curves of $d/dt$ (translations on $\mathbb{R}$) to the integral curves of the rotation field (circles in $\mathbb{R}^2$).

**Is an instance: $\partial_x$ on $\mathbb{R}^2$ $F$-related to $\partial_x$ on $\mathbb{R}$ under the projection $F(x, y) = x$.** Check: $dF_{(x, y)}(\partial_x) = \partial_x \in T_x \mathbb{R}$. So the projection takes horizontal translation on $\mathbb{R}^2$ to translation on $\mathbb{R}$. The map $F$ is not injective, but the $F$-relatedness still holds because the choice of $X'$ on the image side is consistent across all preimages.

**Is an instance: pushforward of $X$ by a diffeomorphism $F$.** For $F : M \to N$ a diffeomorphism, $X \sim_F (F_* X)$ where $(F_* X)_q := dF_{F^{-1}(q)}(X_{F^{-1}(q)})$. The pushforward is the unique vector field on $N$ that is $F$-related to $X$.

**Is an instance: the inclusion of an embedded submanifold.** If $S \hookrightarrow M$ is the inclusion of an embedded submanifold, a vector field $X$ on $S$ is $\iota$-related to a vector field $Y$ on $M$ if and only if $Y$ is tangent to $S$ at every point of $S$ and $Y|_S = X$. So $F$-relatedness for an inclusion is "tangency to $S$ plus agreement on $S$".

**Is NOT an instance: arbitrary pairs.** Given $X = \partial_x$ on $\mathbb{R}$ and the constant map $F : \mathbb{R} \to \mathbb{R}$, $F(x) = 0$. For any $X'$ on $\mathbb{R}$, $dF_p(X_p) = 0 \neq X'_{F(p)}$ unless $X' \equiv 0$. So the only vector field on $\mathbb{R}$ that is $F$-related to $\partial_x$ is the zero field, and $X = \partial_x$ does not have a meaningful "transfer" under the constant map.

**Is NOT an instance: $X = \partial_x$ on $\mathbb{R}^2$ and $X' = \partial_y$ on $\mathbb{R}$ under the projection $F(x, y) = x$.** Check: $dF_{(x, y)}(\partial_x) = \partial_x \neq \partial_y = X'_x$. The components do not match. There exists a vector field $X'$ on $\mathbb{R}$ that *is* $F$-related to $\partial_x$ (namely $X' = \partial_x$), but $\partial_y$ on the target is not it.

**Corollary (existence of pushforward for [[Def - Diffeomorphism|diffeomorphisms]]).** If $F$ is a diffeomorphism, the pushforward $F_* X$ defined by $(F_*X)_q = dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ is the unique vector field on $N$ $F$-related to $X$. Smoothness of $F_* X$ follows from the smoothness of $F$, $F^{-1}$, $dF$, and $X$.

**Corollary (bracket naturality).** If $X_1 \sim_F X'_1$ and $X_2 \sim_F X'_2$ for any smooth map $F$ (not necessarily a diffeomorphism), then $[X_1, X_2] \sim_F [X'_1, X'_2]$. This is the central functoriality of the bracket. Proof: act on $f \in C^\infty(N)$ and use characterization (1) twice.

**Corollary (restriction of a vector field tangent to a submanifold).** If $S \subseteq M$ is an embedded submanifold and $Y$ is a smooth vector field on $M$ that is tangent to $S$ (i.e. $Y_p \in T_p S$ for all $p \in S$), then $Y|_S$ is a well-defined smooth vector field on $S$, and the inclusion $\iota : S \hookrightarrow M$ satisfies $Y|_S \sim_\iota Y$. Together with bracket naturality, this gives Lee Corollary 8.32: the bracket of two vector fields on $M$ tangent to $S$ is also tangent to $S$.

**Calibration check.** You should be able to: (a) verify directly that $d/dt$ on $\mathbb{R}$ is $F$-related to the rotation field on $\mathbb{R}^2$ for $F(t) = (\cos t, \sin t)$; (b) explain why the bracket is *natural* under smooth maps (the bracket of $F$-related pairs is $F$-related, even when no pushforward exists); (c) write down two vector fields on $\mathbb{R}^2$ that are $F$-related under the projection to $\mathbb{R}$ but cannot be obtained as a pushforward.

---

# Unlocked by This

> [!tip] Pushforward and Pullback Functoriality *(from Bundle Theory)*
> The $F$-related concept is the differential-geometric heart of all "covariant" functorial constructions: pushforward of vector fields (when $F$ is a diffeomorphism), pullback of differential forms, naturality of cohomology, equivariance of group actions. In every case the underlying principle is the same — the construction commutes with the relevant smooth map — and $F$-relatedness is the cleanest formulation.

> [!tip] Lie Group Homomorphism induces Lie Algebra Homomorphism *(from Lie Theory)*
> If $F : G \to H$ is a Lie group homomorphism, then every left-invariant vector field $X \in \mathfrak{g}$ is $F$-related to a unique left-invariant vector field on $H$, denoted $F_* X$; the resulting map $F_* : \mathfrak{g} \to \mathfrak{h}$ is a Lie algebra homomorphism. The functoriality $G \mapsto \mathrm{Lie}(G)$, $F \mapsto F_*$ is the **Lie functor** from Lie groups to Lie algebras, and the entire theory of Lie groups is structured by this functor. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

> [!tip] Equivariant Vector Field *(from Equivariant Geometry)*
> A vector field $X$ on $M$ is **equivariant** under a smooth group action $G \times M \to M$ if $X$ is $g$-related to itself for every $g \in G$, where $g : M \to M$ is the action of $g$. Equivariant vector fields are the natural objects of equivariant geometry; their flows commute with the group action.
