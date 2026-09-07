---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Lie Algebra"
  - "Def - Smooth Vector Field"
  - "Def - F-Related Vector Fields"
  - "Def - The Differential of a Smooth Map"
  - "Def - Left and Right Translations and Conjugation on a Lie Group"
tags: [geometry, gauge-theory, lie-algebras, differential-geometry]
---

# Notation

Throughout, manifolds are smooth, Hausdorff, and second countable, and "smooth" means $C^\infty$ (the standing convention of the series). $M$ and $N$ are smooth manifolds, of dimensions $m$ and $n$ respectively. $C^\infty(M)$ is the [[Def - The Smooth Functions Ring|ring of smooth real-valued functions]] on $M$; it is a commutative $\mathbb{R}$-algebra under the pointwise operations. For $p \in M$, the [[Def - The Tangent Space|tangent space]] $T_pM$ is the real vector space of [[Def - Derivation at a Point|derivations at $p$]]: the $\mathbb{R}$-linear maps $v : C^\infty(M) \to \mathbb{R}$ satisfying the Leibniz rule at $p$, $v(fg) = f(p)\,v(g) + g(p)\,v(f)$ for all $f, g \in C^\infty(M)$. A [[Def - Smooth Chart|smooth chart]] is written $(U, \varphi)$ with coordinate functions $x^1, \dots, x^m : U \to \mathbb{R}$, so that $\varphi(q) = (x^1(q), \dots, x^m(q))$; for a function $f$ on $M$ we write $\hat f := f \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}$ for its coordinate representative, and $\partial_i \hat f$ for its $i$-th partial derivative on the open set $\varphi(U) \subset \mathbb{R}^m$. The [[Def - Coordinate Tangent Vectors|coordinate tangent vectors]] $\partial/\partial x^i|_p \in T_pM$ act by $\partial/\partial x^i|_p(f) = \partial_i \hat f(\varphi(p))$; they form a basis of $T_pM$. We do not use the summation convention: every sum is written out with $\sum$.

A [[Def - Vector Field on a Manifold|vector field]] $X$ on $M$ assigns to every $p \in M$ a tangent vector $X(p) \in T_pM$; following Bär and the sibling page [[Def - Left and Right Translations and Conjugation on a Lie Group]], we write $X(p)$ for the value of $X$ at $p$ (the vault's differential-geometry chapters write $X_p$ for the same vector). In a chart $(U, \varphi)$ the field has the expansion $X(p) = \sum_{i=1}^m X^i(p)\,\partial/\partial x^i|_p$ for $p \in U$, with **component functions** $X^i : U \to \mathbb{R}$. The field is [[Def - Smooth Vector Field|smooth]] if it is smooth as a map $X : M \to TM$ into the [[Def - The Tangent Bundle|tangent bundle]]; because the smooth structure of $TM$ is the one whose natural charts are $(\pi^{-1}(U), (x^1 \circ \pi, \dots, x^m \circ \pi, v^1, \dots, v^m))$ ([[Thm - The Tangent Bundle is a Smooth Manifold]]), in which $X$ has the coordinate representation $\varphi(p) \mapsto (\varphi(p), X^1(p), \dots, X^m(p))$, a vector field is smooth if and only if its component functions are smooth in every smooth chart; this is criterion 1 of [[Def - Smooth Vector Field]], and it is the form of smoothness we use. $\mathfrak{X}(M)$ is the set of smooth vector fields on $M$; it is a real vector space under the pointwise operations $(X + Y)(p) = X(p) + Y(p)$, $(cX)(p) = c\,X(p)$, and a module over $C^\infty(M)$ under $(fX)(p) = f(p)\,X(p)$. For $X \in \mathfrak{X}(M)$ and $f \in C^\infty(M)$, $Xf : M \to \mathbb{R}$ is the function $p \mapsto X(p)f$; it is smooth (this is proved on the page, in Lemma 1, from the chart criterion). The map $f \mapsto Xf$ is a derivation of the algebra $C^\infty(M)$: it is $\mathbb{R}$-linear and $X(fg) = f\,(Xg) + g\,(Xf)$, both statements holding pointwise by the derivation property of each $X(p)$.

The [[Def - The Lie Bracket of Vector Fields|Lie bracket]] of $X, Y \in \mathfrak{X}(M)$ is the vector field $[X, Y]$ characterised by $[X, Y]f = X(Yf) - Y(Xf)$ for all $f \in C^\infty(M)$; Part (i) of the theorem below proves that this prescription defines exactly one smooth vector field. A [[Def - Lie Algebra|Lie algebra]] over $\mathbb{R}$ is a real vector space $\mathfrak{g}$ with a map $[\cdot, \cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ that is bilinear, antisymmetric ($[u, v] = -[v, u]$), and satisfies the Jacobi identity $[u, [v, w]] + [v, [w, u]] + [w, [u, v]] = 0$; a [[Def - Lie Subalgebra and Abelian Lie Algebra|Lie subalgebra]] is a vector subspace closed under the bracket.

For a smooth map $F : M \to N$ and $p \in M$, $d_pF : T_pM \to T_{F(p)}N$ is the [[Def - The Differential of a Smooth Map|differential]] of $F$ at $p$, the linear map defined on a derivation $v$ at $p$ by $(d_pF(v))(h) = v(h \circ F)$ for $h \in C^\infty(N)$; the vault's differential-geometry chapters write $dF_p$ for it. Vector fields $X \in \mathfrak{X}(M)$ and $X' \in \mathfrak{X}(N)$ are [[Def - F-Related Vector Fields|$F$-related]], written $X \sim_F X'$, if $d_pF(X(p)) = X'(F(p))$ for every $p \in M$. When $F$ is a [[Def - Diffeomorphism|diffeomorphism]] and $X \in \mathfrak{X}(M)$, the **push-forward** of $X$ along $F$ is the vector field $dF(X) \in \mathfrak{X}(N)$ defined by $dF(X)(q) := d_{F^{-1}(q)}F\big(X(F^{-1}(q))\big)$ for $q \in N$ (Bär, Remark 1.2.4); the vault's chapter [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] writes $F_*X$ for the same field. For a [[Def - Lie Group|Lie group]] $G$ and $g \in G$, $L_g : G \to G$, $L_g(h) = gh$, is the left translation, a diffeomorphism with inverse $L_{g^{-1}}$ ([[Def - Left and Right Translations and Conjugation on a Lie Group]], Proposition A); a field $X \in \mathfrak{X}(G)$ is [[Def - Left-Invariant Vector Field|left-invariant]] if $dL_g(X) = X$ for every $g \in G$, and $\mathfrak{g}$ denotes the vector space of left-invariant fields. The full registry for the chapter is on [[Gauge Theory I — Lie Groups, Representations, and Group Actions]].

> [!warning] Convention: the notation for differentials and push-forwards, the form of the Jacobi identity, and a misprint in the source
> Bär writes the differential of $F$ at $p$ as $d_pF$ and the push-forward of a vector field as $dF(X)$; the vault's differential-geometry chapters (following Lee) write $dF_p$ and $F_*X$. The series uses Bär's notation, and the conversion is the identity of symbols $F_*X = dF(X)$ and $dF_p = d_pF$; the theorem below is stated in both notations so that either can be quoted. Bär (Definition 1.2.1) writes the Jacobi identity with the nested bracket on the left, $[\,[u, v], w] + [\,[v, w], u] + [\,[w, u], v] = 0$, while [[Def - Lie Algebra]] nests on the right, $[u, [v, w]] + [v, [w, u]] + [w, [u, v]] = 0$; in the presence of antisymmetry the two left-hand sides are negatives of each other (Lemma 3 below), so either may be used. Finally, Bär's Definition 1.2.1(ii) is misprinted as "$[v, w] = -[v, w]$"; the intended axiom, used throughout, is $[v, w] = -[w, v]$.

---

# Statement

> **Theorem (the Lie algebra of vector fields; Bär Example 1.2.2.4 and Remark 1.2.4, equation (1.5); Lee, *Introduction to Smooth Manifolds*, 2nd ed., Lemma 8.25, Proposition 8.28, Proposition 8.30, Corollary 8.31).** Let $M$ be a smooth manifold.
>
> **(i) The bracket is a smooth vector field.** For $X, Y \in \mathfrak{X}(M)$ there is exactly one smooth vector field $[X, Y] \in \mathfrak{X}(M)$ such that
> $$[X, Y]f = X(Yf) - Y(Xf) \qquad \text{for every } f \in C^\infty(M).$$
> In every smooth chart $(U, (x^1, \dots, x^m))$, with $X = \sum_i X^i\,\partial/\partial x^i$ and $Y = \sum_j Y^j\,\partial/\partial x^j$ on $U$, its component functions are
> $$[X, Y]^j = X(Y^j) - Y(X^j) = \sum_{i=1}^m \Big( X^i\,\frac{\partial Y^j}{\partial x^i} - Y^i\,\frac{\partial X^j}{\partial x^i} \Big) \qquad (j = 1, \dots, m),$$
> where $\partial Y^j/\partial x^i$ denotes the function $\partial_i \widehat{Y^j} \circ \varphi$ on $U$.
>
> **(ii) Lie algebra.** The bracket $[\cdot, \cdot] : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ is $\mathbb{R}$-bilinear, antisymmetric, and satisfies the Jacobi identity: for all $X, Y, Z \in \mathfrak{X}(M)$ and $a, b \in \mathbb{R}$,
> $$[aX + bY, Z] = a[X, Z] + b[Y, Z], \qquad [Z, aX + bY] = a[Z, X] + b[Z, Y], \qquad [X, Y] = -[Y, X],$$
> $$[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0 .$$
> Hence $(\mathfrak{X}(M), [\cdot, \cdot])$ is a real Lie algebra. If $\dim M \geq 1$ it is infinite-dimensional; if $\dim M = 0$ it is the zero Lie algebra.
>
> **(iii) Function product rule.** For $X, Y \in \mathfrak{X}(M)$ and $f, g \in C^\infty(M)$,
> $$[fX, gY] = fg\,[X, Y] + f\,(Xg)\,Y - g\,(Yf)\,X .$$
> In particular $[fX, Y] = f[X, Y] - (Yf)X$ and $[X, gY] = g[X, Y] + (Xg)Y$.
>
> **(iv) Naturality.** Let $F : M \to N$ be a smooth map and $X, Y \in \mathfrak{X}(M)$, $X', Y' \in \mathfrak{X}(N)$. If $X \sim_F X'$ and $Y \sim_F Y'$, then $[X, Y] \sim_F [X', Y']$.
>
> **(v) Push-forward along a diffeomorphism preserves the bracket (Bär's equation (1.5)).** Let $F : M \to N$ be a diffeomorphism. Then for all $X, Y \in \mathfrak{X}(M)$,
> $$dF([X, Y]) = [\,dF(X),\, dF(Y)\,], \qquad \text{that is,} \qquad F_*[X, Y] = [F_*X, F_*Y],$$
> and $dF : \mathfrak{X}(M) \to \mathfrak{X}(N)$ is an isomorphism of Lie algebras with inverse $d(F^{-1})$.

> **Corollary (left-invariant vector fields form a Lie subalgebra; Bär, p. 11–12).** Let $G$ be a Lie group. If $X, Y \in \mathfrak{X}(G)$ are left-invariant, then $[X, Y]$ is left-invariant. Consequently the vector space $\mathfrak{g}$ of left-invariant vector fields is a Lie subalgebra of $(\mathfrak{X}(G), [\cdot, \cdot])$, and is itself a Lie algebra.

The theorem is Bär's Example 1.2.2.4 (the Lie algebra structure) together with his equation (1.5) (naturality under diffeomorphisms), neither of which he proves; the corollary is the two-line deduction he draws from (1.5) on his page 11, and it is the reason the Lie algebra of a Lie group ([[Def - The Lie Algebra of a Lie Group]]) is a Lie algebra at all. Parts (iii) and (iv) are not stated by Bär; they are included because (iv) is the mechanism behind (v), and because (iii) is the identity through which every curvature and torsion computation of chapters II and IV passes. Part (v) is the Corollary (b) of the vault's [[Thm - Pushforward of Vector Fields under a Diffeomorphism]]; the proof given there routes through the differential-geometry page `Thm - Lie Bracket Properties`, which the vault's proof scanner flags as incomplete, so the present page proves (v) — and everything it rests on — in full and replaces that page as the vault's reference for the Lie algebra structure of $\mathfrak{X}(M)$.

---

# Motivation

Why does gauge theory begin with the vector fields on a manifold? The Lie algebra $\mathfrak{g}$ of a Lie group $G$ is defined, in Bär's development and in [[Def - The Lie Algebra of a Lie Group]], as the space of left-invariant vector fields on $G$ with the bracket of vector fields; the whole infinitesimal theory of the group — the exponential map, the adjoint representation, the identification of $\mathfrak{so}(n)$ with antisymmetric matrices — is then the study of this bracket restricted to a finite-dimensional subspace. Everything therefore rests on two facts about the ambient space $\mathfrak{X}(G)$: that its bracket satisfies the Lie algebra axioms, so that the axioms are inherited by every subspace closed under it, and that the bracket is preserved by diffeomorphisms, so that the left-invariant fields do form such a subspace. Bär states both facts without proof (Example 1.2.2.4 and equation (1.5)). This page supplies the proofs.

There is a second reason the result deserves its own page. The definition $[X, Y]f = X(Yf) - Y(Xf)$ is a definition by *action on functions*, and it is not obvious that the right-hand side is the action of any vector field at all. The composition $f \mapsto X(Yf)$ is a second-order differential operator: in coordinates it involves the second partial derivatives $\partial_i\partial_j \hat f$, which no tangent vector can see, since a derivation at a point annihilates every function vanishing to second order there. The content of Part (i) is that the second-order terms of $X(Yf)$ and $Y(Xf)$ are *the same* — because mixed partial derivatives commute — and so cancel in the difference, leaving a first-order operator. The Lie bracket is thus the unique first-order combination of two vector fields that measures their failure to commute, and the fact that it exists at all is a small theorem, not a notational convenience.

The third reason is naturality. The bracket is defined without reference to any coordinates, metric, or connection; Part (iv) says that it is preserved by every smooth map in the only sense in which a vector field can be transported by a map that is not a diffeomorphism, namely $F$-relatedness, and Part (v) says that a diffeomorphism induces an isomorphism of Lie algebras. This is what makes the Lie algebra of a Lie group intrinsic — a different choice of coordinates on $G$ cannot change $\mathfrak{g}$ — and what makes the fundamental vector fields of a group action (chapter I §1.5) a Lie algebra homomorphism rather than an arbitrary linear map. Every later use of the phrase "infinitesimal symmetry" in the series depends on this page.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypotheses are minimal — a smooth manifold, smooth vector fields, a smooth map — so the disguised sources are the situations in which a *bracket* is what one is secretly looking at.

The first disguised source is **a pair of derivations of an algebra of functions**. If a problem presents two $\mathbb{R}$-linear operators $D_1, D_2 : C^\infty(M) \to C^\infty(M)$ each satisfying the Leibniz rule $D(fg) = f\,Dg + g\,Df$ — for instance two first-order differential operators without zeroth-order term, or two "infinitesimal generators" of one-parameter families of transformations — then each $D_k$ is the action of a smooth vector field, and the theorem applies to their commutator $D_1 D_2 - D_2 D_1$. The bridge is the observation that a global derivation of $C^\infty(M)$ restricts, at each point $p$, to a derivation at $p$, namely $f \mapsto (Df)(p)$, so $D$ is the action of the rough vector field $p \mapsto (f \mapsto (Df)(p))$; smoothness of the field follows from smoothness of $D(x^i)$ on charts. *Example problem:* show that the operators $D_1 = x\,\partial_y - y\,\partial_x$ and $D_2 = \partial_x$ on $\mathbb{R}^2$ have commutator $D_1 D_2 - D_2 D_1 = \partial_y$ and that this is again a derivation, without computing any second derivatives.

The second disguised source is **a finite-dimensional space of vector fields that one wishes to show is a Lie algebra**. The problem may hand over an $r$-dimensional space $V \subset \mathfrak{X}(M)$ — the infinitesimal generators of a group action, the left-invariant fields on a Lie group, the Killing fields of a metric — and ask whether $V$ is a Lie algebra. The bridge is that the axioms are *inherited*: by Part (ii) the ambient $\mathfrak{X}(M)$ satisfies bilinearity, antisymmetry, and Jacobi, and these are identities among elements, so they hold on $V$ as soon as $V$ is closed under the bracket. All that must be checked is closure. *Example problem:* show that the three fields $\partial_x$, $\partial_y$, $x\,\partial_y - y\,\partial_x$ on $\mathbb{R}^2$ span a three-dimensional Lie algebra (the Lie algebra of the Euclidean group of the plane) by computing the three brackets and checking that they lie in the span.

The third disguised source is **a symmetry of a geometric structure**. A diffeomorphism $F : M \to M$ preserving some structure — a metric, a symplectic form, a foliation — often preserves a distinguished class of vector fields, and one wants to know that it preserves the brackets of those fields too. The bridge is Part (v): the push-forward along *any* diffeomorphism preserves *all* brackets, so the structure-preservation is irrelevant to the bracket computation and matters only for identifying which fields are distinguished. *Example problem:* given that the flow $\phi_t$ of a vector field $X$ consists of diffeomorphisms, and that $Y, Z$ are fields with $d\phi_t(Y) = Y$ and $d\phi_t(Z) = Z$ for all $t$, conclude that $d\phi_t([Y, Z]) = [Y, Z]$, that is, that the bracket of two $\phi$-invariant fields is $\phi$-invariant.

**Targets (Output Amplification)**

Combine Part (v) with **left-invariance under a group of diffeomorphisms**. Property $D$: a Lie group $G$ with its left translations $L_g$, which are diffeomorphisms of $G$. Then the fields fixed by every $dL_g$ — the left-invariant fields — are closed under the bracket, which is the Corollary; combining further with the evaluation isomorphism $\mathfrak{g} \to T_eG$ ([[Def - Left and Right Translations and Conjugation on a Lie Group]], Proposition D) turns $T_eG$ into a finite-dimensional Lie algebra of dimension $\dim G$. The payoff is the whole of [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]]: the bracket on $\mathfrak{gl}(n; \mathbb{R})$ is the matrix commutator, and the Lie algebras of the classical groups are the commutator-closed subspaces that page computes.

Combine Part (iv) with **the orbit maps of a group action**. Property $D$: a smooth right action of $G$ on $M$, with orbit maps $\ell_p : G \to M$, $g \mapsto p \cdot g$, which are smooth but in general neither injective nor surjective. Then the fundamental vector field $\xi_M$ of $\xi \in \mathfrak{g}$ is $\ell_p$-related to the left-invariant field $\tilde\xi$ for every $p$, and Part (iv) — which, unlike Part (v), needs no diffeomorphism — gives $[\xi, \eta]_M = [\xi_M, \eta_M]$. The payoff is that $\xi \mapsto \xi_M$ is a Lie algebra homomorphism $\mathfrak{g} \to \mathfrak{X}(M)$ ([[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]), the starting point for the vertical distribution of a principal bundle in chapter III.

Combine Part (iii) with **a connection on a vector bundle**. Property $D$: a covariant derivative $\nabla$ on a bundle $E \to M$, which is $C^\infty(M)$-linear in the vector-field slot and satisfies the Leibniz rule in the section slot. Then the expression $\nabla_X \nabla_Y s - \nabla_Y \nabla_X s - \nabla_{[X, Y]}s$ is $C^\infty(M)$-linear in $X$ and $Y$ precisely because, by (iii), $[fX, Y] = f[X, Y] - (Yf)X$, and the term $-(Yf)X$ in the bracket cancels the term $-(Yf)\nabla_X s$ produced by the Leibniz rule. The payoff is that curvature is a tensor, $F_\nabla \in \Omega^2(M; \operatorname{End} E)$, which is the model proof of the series' proof standard and the foundation of chapter II.

Combine Part (ii) with **a subspace closed under the bracket and a linear map out of it**. Property $D$: a Lie algebra homomorphism $\phi : \mathfrak{h} \to \mathfrak{X}(M)$ from an abstract Lie algebra, injective on a subspace. Then the Jacobi identity on $\mathfrak{X}(M)$ forces the Jacobi identity on the image, and any identity among brackets that holds in $\mathfrak{X}(M)$ holds in $\mathfrak{h}$ wherever $\phi$ is injective. The payoff is the standard route to proving that an abstractly defined bracket (the cross product on $\mathbb{R}^3$, say) satisfies Jacobi: realise it as a bracket of vector fields, or of matrices, and inherit.

---

# Why Is It True

Think of a smooth vector field $X$ as the differential operator $f \mapsto Xf$ on $C^\infty(M)$, a first-order operator with no zeroth-order term. The composition $XY : f \mapsto X(Yf)$ is a second-order operator; in a chart it reads
$$X(Yf) = \sum_{i,j} X^i\,\frac{\partial Y^j}{\partial x^i}\,\frac{\partial f}{\partial x^j} + \sum_{i,j} X^i Y^j\,\frac{\partial^2 f}{\partial x^i\,\partial x^j},$$
one first-order piece and one second-order piece. The second-order piece is *symmetric* in the roles of $X$ and $Y$ once the dummy indices are renamed, because the matrix of second partial derivatives is symmetric — Schwarz's theorem. Hence the second-order pieces of $X(Yf)$ and $Y(Xf)$ coincide and vanish in the difference, and what survives is a first-order operator with coefficients $X(Y^j) - Y(X^j)$. **The bracket exists because the commutator of two first-order operators has no second-order part, and it has no second-order part because mixed partial derivatives commute.**

The Lie algebra axioms are then consequences of the fact that $[X, Y]$ is a commutator $XY - YX$ inside the *associative* algebra of all $\mathbb{R}$-linear operators on $C^\infty(M)$. Bilinearity and antisymmetry of a commutator are immediate from the bilinearity of composition. The Jacobi identity is the statement that, when the three cyclically nested commutators are expanded into the twelve triple products $\pm X(Y(Zf))$, each of the six orderings of the letters $X, Y, Z$ appears exactly once with each sign. This is Bär's Remark on his page 10 made precise: **the Jacobi identity is the shadow that associativity of operator composition casts on the commutator.** No geometry enters; the same computation proves Jacobi for the matrix commutator.

Naturality has a different mechanism. A smooth map $F : M \to N$ pulls functions back, $h \mapsto h \circ F$, and $F$-relatedness of $X$ and $X'$ is exactly the statement that $X$ acting on pulled-back functions equals the pull-back of $X'$ acting on the original functions: $X(h \circ F) = (X'h) \circ F$. This identity is *stable under composition*: applying it twice gives $X(Y(h \circ F)) = (X'(Y'h)) \circ F$, and subtracting the version with $X$ and $Y$ exchanged gives the same identity for the brackets. **Naturality holds because $F$-relatedness is a statement about pull-back of functions, and pull-back of functions is a ring homomorphism that the bracket, being built from actions on functions, cannot distinguish from the identity.** When $F$ is a diffeomorphism, every field on $N$ is $F$-related to exactly one field on $M$, so the relation becomes a map, and the map preserves brackets.

---

# What Makes This Hard

The non-obvious step is the one that is usually skipped: that $[X, Y]$ is a vector field at all. Both $X(Yf)$ and $Y(Xf)$ are second-order operators, and the reader must see that the cancellation of second-order terms uses the symmetry of mixed partials — that is, an analytic fact about $C^2$ functions — and not merely algebra. The common error in the Jacobi computation is a sign slip in one of the twelve terms, which then appears to leave a residue; the safeguard is to list the six words $XYZ, XZY, YXZ, YZX, ZXY, ZYX$ and record beside each the two nested brackets that produce it. In the naturality argument the common error is to apply the relatedness identity to the wrong function: one must apply $Y \sim_F Y'$ to $h$ and then $X \sim_F X'$ to the *new* function $Y'h \in C^\infty(N)$, and the identity used in each step must be written with its function displayed. Finally, Part (v) is *not* a consequence of Part (iv) alone: one also needs that a diffeomorphism admits a unique $F$-related field, and the uniqueness is the step that turns "$[X, Y]$ is related to $[dF(X), dF(Y)]$" into the equality $dF([X, Y]) = [dF(X), dF(Y)]$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show first that $f \mapsto X(Yf) - Y(Xf)$ is, at each point, a derivation — this is a two-line Leibniz computation in which the cross terms cancel — so that $[X, Y]$ is a rough vector field, and then compute its components in a chart, where the symmetry of mixed partials kills the second-order terms and exhibits smooth components. The Lie algebra axioms follow by expanding commutators; naturality follows by applying the functional form of $F$-relatedness twice; the diffeomorphism statement follows from naturality and the uniqueness of related fields.

**Subgoal decomposition:**

1. **$[X, Y](p)$ is a derivation at $p$.** Show that $f \mapsto X(p)(Yf) - Y(p)(Xf)$ is $\mathbb{R}$-linear and satisfies the Leibniz rule at $p$.
   - *Hint:* Expand $X(p)(Y(fg))$ using $Y(fg) = f\,Yg + g\,Yf$ and then the derivation property of $X(p)$; four terms appear, two of which are symmetric in $X, Y$ and cancel against their partners from $Y(p)(X(fg))$.
   - *Why needed:* Without it, there is no vector field to speak of; this is the step that makes the bracket a first-order object.

2. **Coordinate formula and smoothness.** In a chart, compute $X(Yf)$ and $Y(Xf)$ and show that the second-order terms cancel by Schwarz's theorem, leaving components $X(Y^j) - Y(X^j)$, which are smooth.
   - *Hint:* Write $Yf = \sum_j Y^j\,(\partial_j \hat f \circ \varphi)$ on $U$ and differentiate the product; rename the dummy indices in the second-order term of $Y(Xf)$.
   - *Why needed:* Smoothness of $[X, Y]$ is what makes $\mathfrak{X}(M)$ closed under the bracket, and the coordinate formula is the working tool for every later computation.

3. **Bilinearity and antisymmetry.** Both follow from the definition by the linearity of the actions.
   - *Hint:* $(aX + bY)f = a\,Xf + b\,Yf$ pointwise, and $X(Yf) - Y(Xf) = -(Y(Xf) - X(Yf))$.
   - *Why needed:* Two of the three Lie algebra axioms.

4. **Jacobi identity.** Expand the three nested brackets as operators on a function $f$ into twelve terms and show they cancel in pairs.
   - *Hint:* $[X, [Y, Z]]f = XYZf - XZYf - YZXf + ZYXf$; cyclically permute and tabulate the six words.
   - *Why needed:* The third Lie algebra axiom; it is inherited by every subalgebra, in particular by $\mathfrak{g}$.

5. **Infinite dimension.** Exhibit infinitely many linearly independent fields when $\dim M \geq 1$.
   - *Hint:* Multiply $(x^1)^k\,\partial/\partial x^1$ by a bump function supported in a chart, and use that a polynomial vanishing on an interval is zero.
   - *Why needed:* This is the one quantitative clause of Bär's Example 1.2.2.4.

6. **Function product rule.** Compute $[fX, gY]h$ from the definition using $(fX)h = f\,(Xh)$ and the Leibniz rule.
   - *Hint:* $f\,X(g\,Yh) = f\,(Xg)(Yh) + fg\,X(Yh)$.
   - *Why needed:* Part (iii); it is the identity behind the tensoriality of curvature.

7. **Functional form of $F$-relatedness.** Show that $X \sim_F X'$ if and only if $X(h \circ F) = (X'h) \circ F$ for all $h \in C^\infty(N)$.
   - *Hint:* Evaluate both sides at $p$ and use the definition $(d_pF(v))(h) = v(h \circ F)$; for the converse, two derivations at $F(p)$ agreeing on all $h$ are equal.
   - *Why needed:* It converts a pointwise statement about differentials into a statement about operators on functions, which is the form in which the bracket can be handled.

8. **Naturality.** Apply subgoal 7 twice and subtract.
   - *Hint:* $X(Y(h \circ F)) = X((Y'h) \circ F) = (X'(Y'h)) \circ F$.
   - *Why needed:* Part (iv), the mechanism of Part (v).

9. **Push-forward and the Lie algebra isomorphism.** Use that $dF(X)$ is the unique field $F$-related to $X$ and combine with subgoal 8; prove linearity and invertibility from the chain rule.
   - *Hint:* $[X, Y] \sim_F [dF(X), dF(Y)]$ and $[X, Y] \sim_F dF([X, Y])$; uniqueness gives equality.
   - *Why needed:* Part (v) and the Corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: The bracket is a well-defined rough vector field, and $Xf$ is smooth
> **Statement:** Let $X, Y \in \mathfrak{X}(M)$. (a) For every $f \in C^\infty(M)$ the function $Xf : p \mapsto X(p)f$ is smooth, and $f \mapsto Xf$ is $\mathbb{R}$-linear with $X(fg) = f\,(Xg) + g\,(Xf)$. (b) For every $p \in M$ the map
> $$[X, Y](p) : C^\infty(M) \to \mathbb{R}, \qquad f \mapsto X(p)(Yf) - Y(p)(Xf),$$
> is a derivation at $p$, hence an element of $T_pM$. Consequently $p \mapsto [X, Y](p)$ is a vector field on $M$ (not yet known to be smooth), and it is the *only* vector field $W$ on $M$ with $Wf = X(Yf) - Y(Xf)$ for all $f \in C^\infty(M)$.
>
> **Hint:** For (a), expand in a chart. For (b), the Leibniz rule for $X(p)$ applied to $Y(fg) = f\,Yg + g\,Yf$ produces four terms; the two involving $(Xf)(p)(Yg)(p)$ and $(Xg)(p)(Yf)(p)$ are symmetric in $X$ and $Y$ and cancel against the corresponding terms of $Y(p)(X(fg))$.
>
> **Why needed:** It is the step that makes $[X, Y]$ a first-order object — a tangent vector at each point — rather than a second-order differential operator; uniqueness is what allows every later identity to be proved by testing on functions.
>
> > [!note]- Full proof
> > **Part (a): $Xf$ is smooth and $X$ acts as a derivation.** Fix $f \in C^\infty(M)$ and a point $p_0 \in M$, and let $(U, \varphi)$ be a smooth chart with $p_0 \in U$. For $p \in U$, expand $X(p) = \sum_{i=1}^m X^i(p)\,\partial/\partial x^i|_p$ in the coordinate basis (the basis property of [[Def - Coordinate Tangent Vectors]]). Then
> > $$(Xf)(p) = X(p)f = \sum_{i=1}^m X^i(p)\,\frac{\partial}{\partial x^i}\Big|_p(f) = \sum_{i=1}^m X^i(p)\,\partial_i \hat f(\varphi(p)) \qquad \text{(definition of } Xf \text{; expansion of } X(p) \text{; definition of the coordinate tangent vectors)}.$$
> > On $U$, therefore, $Xf = \sum_i X^i \cdot (\partial_i \hat f \circ \varphi)$. Each $X^i$ is smooth on $U$ because $X$ is a smooth vector field (the chart criterion of smoothness recorded in the Notation section); $\hat f = f \circ \varphi^{-1}$ is smooth on the open set $\varphi(U) \subset \mathbb{R}^m$ because $f$ is smooth and $\varphi^{-1}$ is smooth, so $\partial_i \hat f$ is smooth, and $\partial_i \hat f \circ \varphi$ is smooth on $U$ as a composition of smooth maps ([[Ex - Composition of Smooth Maps is Smooth]]). A finite sum of products of smooth functions is smooth. Hence $Xf$ is smooth on $U$, and since $p_0$ was arbitrary, $Xf \in C^\infty(M)$.
> >
> > For the linearity and Leibniz rule: for $f, g \in C^\infty(M)$, $a, b \in \mathbb{R}$, and every $p \in M$,
> > $$(X(af + bg))(p) = X(p)(af + bg) = a\,X(p)f + b\,X(p)g = (a\,Xf + b\,Xg)(p) \qquad \text{(} X(p) \text{ is } \mathbb{R}\text{-linear, being a derivation at } p\text{)},$$
> > $$(X(fg))(p) = X(p)(fg) = f(p)\,X(p)g + g(p)\,X(p)f = (f\,Xg + g\,Xf)(p) \qquad \text{(Leibniz rule at } p \text{ for the derivation } X(p)\text{)}.$$
> > Since these hold at every $p$, $X(af + bg) = a\,Xf + b\,Xg$ and $X(fg) = f\,Xg + g\,Xf$ as functions.
> >
> > **Part (b), Step 1: the map is well defined and linear.** Fix $p \in M$. For $f \in C^\infty(M)$, the functions $Yf$ and $Xf$ lie in $C^\infty(M)$ by Part (a), so $X(p)(Yf)$ and $Y(p)(Xf)$ are real numbers and $[X, Y](p)f := X(p)(Yf) - Y(p)(Xf)$ is well defined. For $a, b \in \mathbb{R}$ and $f, g \in C^\infty(M)$,
> > $$[X, Y](p)(af + bg) = X(p)\big(Y(af + bg)\big) - Y(p)\big(X(af + bg)\big) = X(p)(a\,Yf + b\,Yg) - Y(p)(a\,Xf + b\,Xg) \qquad \text{(linearity of } f \mapsto Yf \text{ and } f \mapsto Xf \text{, Part (a))}$$
> > $$= a\big(X(p)(Yf) - Y(p)(Xf)\big) + b\big(X(p)(Yg) - Y(p)(Xg)\big) = a\,[X, Y](p)f + b\,[X, Y](p)g \qquad \text{(linearity of the derivations } X(p), Y(p)\text{)}.$$
> >
> > **Part (b), Step 2: the Leibniz rule at $p$.** Let $f, g \in C^\infty(M)$. By Part (a), $Y(fg) = f\,Yg + g\,Yf$, so
> > $$X(p)\big(Y(fg)\big) = X(p)\big(f\,Yg + g\,Yf\big) = X(p)(f\,Yg) + X(p)(g\,Yf) \qquad \text{(Part (a) for } Y \text{; linearity of } X(p)\text{)}$$
> > $$= f(p)\,X(p)(Yg) + (Yg)(p)\,X(p)f + g(p)\,X(p)(Yf) + (Yf)(p)\,X(p)g \qquad \text{(Leibniz rule at } p \text{ for } X(p) \text{, applied to each product)}.$$
> > Exchanging the roles of $X$ and $Y$ in this computation — every step used only Part (a) and the derivation property, which hold for both fields — gives
> > $$Y(p)\big(X(fg)\big) = f(p)\,Y(p)(Xg) + (Xg)(p)\,Y(p)f + g(p)\,Y(p)(Xf) + (Xf)(p)\,Y(p)g .$$
> > Subtracting the second display from the first, and writing $X(p)f = (Xf)(p)$ and so on,
> > $$[X, Y](p)(fg) = f(p)\big(X(p)(Yg) - Y(p)(Xg)\big) + g(p)\big(X(p)(Yf) - Y(p)(Xf)\big) + \big[(Yg)(p)(Xf)(p) - (Xf)(p)(Yg)(p)\big] + \big[(Yf)(p)(Xg)(p) - (Xg)(p)(Yf)(p)\big]$$
> > $$= f(p)\,[X, Y](p)g + g(p)\,[X, Y](p)f \qquad \text{(the two bracketed differences vanish, since multiplication of real numbers is commutative; definition of } [X, Y](p)\text{)}.$$
> > So $[X, Y](p)$ is $\mathbb{R}$-linear and satisfies the Leibniz rule at $p$: it is a derivation at $p$, that is, an element of $T_pM$ ([[Def - Derivation at a Point]]).
> >
> > **Part (b), Step 3: uniqueness.** Suppose $W$ is a vector field on $M$ with $Wf = X(Yf) - Y(Xf)$ for every $f \in C^\infty(M)$. Evaluating at $p$, $W(p)f = X(p)(Yf) - Y(p)(Xf) = [X, Y](p)f$ for every $f$. Two derivations at $p$ are, by definition, maps $C^\infty(M) \to \mathbb{R}$; two such maps agreeing on every $f$ are equal. Hence $W(p) = [X, Y](p)$ for every $p$, that is, $W = [X, Y]$. Therefore $[X, Y]$ is the unique vector field acting on functions by $f \mapsto X(Yf) - Y(Xf)$.

> [!note]- Lemma 2: The coordinate formula, and smoothness of the bracket
> **Statement:** Let $X, Y \in \mathfrak{X}(M)$ and let $(U, \varphi)$ be a smooth chart with coordinates $x^1, \dots, x^m$, in which $X = \sum_i X^i\,\partial/\partial x^i$ and $Y = \sum_j Y^j\,\partial/\partial x^j$. Then for every $p \in U$,
> $$[X, Y](p) = \sum_{j=1}^m \big( X(Y^j) - Y(X^j) \big)(p)\,\frac{\partial}{\partial x^j}\Big|_p, \qquad X(Y^j) - Y(X^j) = \sum_{i=1}^m \Big( X^i\,\frac{\partial Y^j}{\partial x^i} - Y^i\,\frac{\partial X^j}{\partial x^i} \Big),$$
> where $\partial Y^j/\partial x^i := \partial_i \widehat{Y^j} \circ \varphi$ with $\widehat{Y^j} = Y^j \circ \varphi^{-1}$. The component functions $[X, Y]^j = X(Y^j) - Y(X^j)$ are smooth on $U$. Consequently $[X, Y] \in \mathfrak{X}(M)$.
>
> **Hint:** Write $Yf = \sum_j Y^j\,(\partial_j \hat f \circ \varphi)$ on $U$, apply $X(p)$, and use the product rule in $\mathbb{R}^m$; the second-order terms $\sum_{i,j} X^i Y^j\,\partial_i\partial_j \hat f$ and $\sum_{i,j} Y^i X^j\,\partial_i\partial_j \hat f$ coincide after renaming $i \leftrightarrow j$ and invoking the symmetry of mixed partials.
>
> **Why needed:** It proves that the bracket of smooth fields is smooth, so that $\mathfrak{X}(M)$ is closed under the bracket, and it supplies the formula by which every bracket in the series is actually computed.
>
> > [!note]- Full proof
> > Fix the chart $(U, \varphi)$ and a point $p \in U$. We need to show that the derivation $[X, Y](p)$ of Lemma 1 equals $\sum_j (X(Y^j) - Y(X^j))(p)\,\partial/\partial x^j|_p$, and that the coefficients are smooth functions on $U$.
> >
> > **Step 0: the coefficient functions are smooth on $U$.** Here $Y^j \in C^\infty(U)$, and $X$ restricts to a smooth vector field on the open submanifold $U$, so $X(Y^j)$ is defined on $U$ and smooth there by Lemma 1(a) applied to the manifold $U$; explicitly, by the computation in Lemma 1(a), $X(Y^j) = \sum_i X^i \cdot (\partial_i \widehat{Y^j} \circ \varphi) = \sum_i X^i\,\partial Y^j/\partial x^i$ on $U$, which is the second formula in the statement, and each summand is a product of smooth functions on $U$. The same holds for $Y(X^j)$. Hence $[X, Y]^j := X(Y^j) - Y(X^j) \in C^\infty(U)$.
> >
> > **Step 1: express $Yf$ in the chart.** Let $f \in C^\infty(M)$. By the computation in Lemma 1(a), on $U$ we have
> > $$Yf = \sum_{j=1}^m Y^j \cdot \big(\partial_j \hat f \circ \varphi\big) \qquad \text{(Lemma 1(a), expansion in the coordinate basis)}.$$
> > Its coordinate representative on $\varphi(U)$ is therefore
> > $$\widehat{Yf} = (Yf) \circ \varphi^{-1} = \sum_{j=1}^m \widehat{Y^j}\;\partial_j \hat f \qquad \text{(compose the previous line with } \varphi^{-1}\text{; } \varphi \circ \varphi^{-1} = \mathrm{id}\text{)}.$$
> >
> > **Step 2: apply $X(p)$.** Since $Yf \in C^\infty(M)$ (Lemma 1(a)), the same expansion applied to $X$ and the function $Yf$ gives
> > $$X(p)(Yf) = \sum_{i=1}^m X^i(p)\,\partial_i \widehat{Yf}(\varphi(p)) = \sum_{i=1}^m X^i(p)\,\partial_i\Big( \sum_{j=1}^m \widehat{Y^j}\,\partial_j \hat f \Big)(\varphi(p)) \qquad \text{(Lemma 1(a) for } X \text{; Step 1)}$$
> > $$= \sum_{i=1}^m \sum_{j=1}^m X^i(p)\Big( \partial_i \widehat{Y^j}(\varphi(p))\,\partial_j \hat f(\varphi(p)) + \widehat{Y^j}(\varphi(p))\,\partial_i \partial_j \hat f(\varphi(p)) \Big) \qquad \text{(product rule for partial derivatives in } \mathbb{R}^m \text{; linearity of } \partial_i\text{)}.$$
> > Writing $\widehat{Y^j}(\varphi(p)) = Y^j(p)$ and $\partial_i\widehat{Y^j}(\varphi(p)) = (\partial Y^j/\partial x^i)(p)$, this is
> > $$X(p)(Yf) = \sum_{i,j} X^i(p)\,\frac{\partial Y^j}{\partial x^i}(p)\,\partial_j \hat f(\varphi(p)) + \sum_{i,j} X^i(p)\,Y^j(p)\,\partial_i\partial_j \hat f(\varphi(p)) . \tag{2.1}$$
> >
> > **Step 3: the same with $X$ and $Y$ exchanged.** Every step of Steps 1–2 used only Lemma 1(a) and the product rule, which apply equally with the roles of $X$ and $Y$ exchanged; carrying out the substitution $X \leftrightarrow Y$ (so $X^i \leftrightarrow Y^i$ and $\widehat{X^j} \leftrightarrow \widehat{Y^j}$) in (2.1) gives
> > $$Y(p)(Xf) = \sum_{i,j} Y^i(p)\,\frac{\partial X^j}{\partial x^i}(p)\,\partial_j \hat f(\varphi(p)) + \sum_{i,j} Y^i(p)\,X^j(p)\,\partial_i\partial_j \hat f(\varphi(p)) . \tag{2.2}$$
> >
> > **Step 4: the second-order terms cancel.** In the second sum of (2.2), rename the bound indices, $i \to j$ and $j \to i$ (a bijection of the index set $\{1, \dots, m\}^2$ onto itself, which does not change a finite sum):
> > $$\sum_{i,j} Y^i(p)\,X^j(p)\,\partial_i\partial_j \hat f(\varphi(p)) = \sum_{i,j} Y^j(p)\,X^i(p)\,\partial_j\partial_i \hat f(\varphi(p)) = \sum_{i,j} X^i(p)\,Y^j(p)\,\partial_i\partial_j \hat f(\varphi(p)) \qquad \text{(renaming; then } \partial_j\partial_i \hat f = \partial_i\partial_j \hat f\text{)}.$$
> > The last equality is [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]] — for $g \in C^2(V)$ on an open $V \subset \mathbb{R}^m$, $\partial_i\partial_j g = \partial_j\partial_i g$ on $V$ — applied to $g = \hat f$ on $V = \varphi(U)$, which is legitimate because $\hat f$ is $C^\infty$, in particular $C^2$, on $\varphi(U)$. Hence the second sums of (2.1) and (2.2) are equal.
> >
> > **Step 5: subtract.** Subtracting (2.2) from (2.1), the second-order sums cancel by Step 4, and
> > $$[X, Y](p)f = X(p)(Yf) - Y(p)(Xf) = \sum_{j=1}^m \Big( \sum_{i=1}^m X^i(p)\,\frac{\partial Y^j}{\partial x^i}(p) - Y^i(p)\,\frac{\partial X^j}{\partial x^i}(p) \Big)\,\partial_j \hat f(\varphi(p)) \qquad \text{(definition of } [X, Y](p) \text{; (2.1), (2.2), Step 4)}$$
> > $$= \sum_{j=1}^m \big( X(Y^j) - Y(X^j) \big)(p)\;\frac{\partial}{\partial x^j}\Big|_p(f) \qquad \text{(Step 0 for the coefficient; definition of } \partial/\partial x^j|_p\text{)}.$$
> > Thus the two derivations $[X, Y](p)$ and $\sum_j (X(Y^j) - Y(X^j))(p)\,\partial/\partial x^j|_p$ at $p$ agree on every $f \in C^\infty(M)$, and are therefore equal as elements of $T_pM$. This is the first formula of the statement; the second was established in Step 0.
> >
> > **Step 6: smoothness of $[X, Y]$.** The component functions of $[X, Y]$ in the chart $(U, \varphi)$ are $[X, Y]^j = X(Y^j) - Y(X^j)$, which are smooth on $U$ by Step 0. Since the chart was arbitrary, the components of $[X, Y]$ are smooth in every smooth chart, so $[X, Y]$ is a smooth vector field by the chart criterion of smoothness (criterion 1 of [[Def - Smooth Vector Field]], which is the definition of smoothness of the map $M \to TM$ read in the natural charts of $TM$). Therefore $[X, Y] \in \mathfrak{X}(M)$.

> [!note]- Lemma 3: Bilinearity and antisymmetry; the two forms of the Jacobi identity
> **Statement:** (a) For $X, Y, Z \in \mathfrak{X}(M)$ and $a, b \in \mathbb{R}$: $[aX + bY, Z] = a[X, Z] + b[Y, Z]$, $[Z, aX + bY] = a[Z, X] + b[Z, Y]$, and $[X, Y] = -[Y, X]$. (b) In any real vector space with an antisymmetric bilinear bracket, for all $u, v, w$,
> $$[\,[u, v], w] + [\,[v, w], u] + [\,[w, u], v] = -\big( [u, [v, w]] + [v, [w, u]] + [w, [u, v]] \big),$$
> so Bär's form of the Jacobi identity and the form of [[Def - Lie Algebra]] are equivalent.
>
> **Hint:** Test on functions and use Lemma 1's uniqueness; for (b), apply $[x, y] = -[y, x]$ to each of the three terms.
>
> **Why needed:** Two of the three Lie algebra axioms, and the reconciliation of the two sources' conventions.
>
> > [!note]- Full proof
> > **Part (a), bilinearity in the first slot.** By Lemmas 1 and 2, all brackets appearing are smooth vector fields, and by Lemma 1(b) a vector field is determined by its action on functions. For $f \in C^\infty(M)$,
> > $$[aX + bY, Z]f = (aX + bY)(Zf) - Z\big((aX + bY)f\big) \qquad \text{(definition of the bracket)}$$
> > $$= a\,X(Zf) + b\,Y(Zf) - Z\big(a\,Xf + b\,Yf\big) \qquad \text{(} (aX + bY)(p) = aX(p) + bY(p) \text{ for every } p\text{, the pointwise vector-space structure of } \mathfrak{X}(M)\text{)}$$
> > $$= a\,X(Zf) + b\,Y(Zf) - a\,Z(Xf) - b\,Z(Yf) \qquad \text{(linearity of } f \mapsto Zf\text{, Lemma 1(a))}$$
> > $$= a\big(X(Zf) - Z(Xf)\big) + b\big(Y(Zf) - Z(Yf)\big) = \big(a[X, Z] + b[Y, Z]\big)f \qquad \text{(regroup; definition of the bracket; pointwise linear structure)}.$$
> > Since this holds for every $f$, Lemma 1(b) (uniqueness) gives $[aX + bY, Z] = a[X, Z] + b[Y, Z]$.
> >
> > **Part (a), antisymmetry.** For $f \in C^\infty(M)$,
> > $$[X, Y]f = X(Yf) - Y(Xf) = -\big( Y(Xf) - X(Yf) \big) = -[Y, X]f = (-[Y, X])f \qquad \text{(definition of the bracket twice; pointwise scalar multiplication)},$$
> > so $[X, Y] = -[Y, X]$ by uniqueness (Lemma 1(b)).
> >
> > **Part (a), bilinearity in the second slot.** Combining the two results just proved,
> > $$[Z, aX + bY] = -[aX + bY, Z] = -\big( a[X, Z] + b[Y, Z] \big) = a\big(-[X, Z]\big) + b\big(-[Y, Z]\big) = a[Z, X] + b[Z, Y] \qquad \text{(antisymmetry; first-slot bilinearity; vector-space axioms; antisymmetry)}.$$
> >
> > **Part (b).** Let $u, v, w$ be elements of a real vector space with an antisymmetric bilinear bracket. Applying antisymmetry $[x, y] = -[y, x]$ to each term with $x$ the nested bracket,
> > $$[\,[u, v], w] = -[w, [u, v]], \qquad [\,[v, w], u] = -[u, [v, w]], \qquad [\,[w, u], v] = -[v, [w, u]] \qquad \text{(antisymmetry, three times)}.$$
> > Adding the three equations and reordering the right-hand side,
> > $$[\,[u, v], w] + [\,[v, w], u] + [\,[w, u], v] = -\big( [u, [v, w]] + [v, [w, u]] + [w, [u, v]] \big) \qquad \text{(sum of the three lines; commutativity of addition)}.$$
> > Hence the left-hand side vanishes if and only if the right-hand side does: Bär's Jacobi identity holds if and only if the Jacobi identity of [[Def - Lie Algebra]] holds.

> [!note]- Lemma 4: The Jacobi identity
> **Statement:** For all $X, Y, Z \in \mathfrak{X}(M)$,
> $$[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0 .$$
>
> **Hint:** Write $XYZf$ for $X(Y(Zf))$. Then $[X, [Y, Z]]f = XYZf - XZYf - YZXf + ZYXf$. The cyclic sum contains each of the six words $XYZ, XZY, YXZ, YZX, ZXY, ZYX$ exactly once with a plus sign and once with a minus sign.
>
> **Why needed:** The third Lie algebra axiom. It is inherited by every subspace closed under the bracket, which is how $\mathfrak{g}$ acquires it.
>
> > [!note]- Full proof
> > By Lemmas 1 and 2, all the brackets are smooth vector fields, so the left-hand side is a smooth vector field, and by Lemma 1(b) it suffices to show that it annihilates every $f \in C^\infty(M)$. Fix $f$. For fields $A, B, C$ we abbreviate $A(B(Cf))$ as $ABCf$; this is a real-valued smooth function by Lemma 1(a) applied three times.
> >
> > **Step 1: expand one nested bracket.**
> > $$[X, [Y, Z]]f = X\big([Y, Z]f\big) - [Y, Z](Xf) \qquad \text{(definition of the outer bracket)}$$
> > $$= X\big( Y(Zf) - Z(Yf) \big) - \big( Y(Z(Xf)) - Z(Y(Xf)) \big) \qquad \text{(definition of the inner bracket, applied to } f \text{ and to } Xf\text{)}$$
> > $$= XYZf - XZYf - YZXf + ZYXf \qquad \text{(linearity of } g \mapsto Xg \text{, Lemma 1(a); abbreviation)}. \tag{4.1}$$
> >
> > **Step 2: the two cyclic permutations.** The computation in Step 1 used only the definition of the bracket and the linearity of Lemma 1(a), which hold for every triple of smooth fields; applying it to the triples $(Y, Z, X)$ and $(Z, X, Y)$ in place of $(X, Y, Z)$ — that is, substituting $X \to Y \to Z \to X$ in (4.1), once and then twice — gives
> > $$[Y, [Z, X]]f = YZXf - YXZf - ZXYf + XZYf, \tag{4.2}$$
> > $$[Z, [X, Y]]f = ZXYf - ZYXf - XYZf + YXZf. \tag{4.3}$$
> >
> > **Step 3: tabulate and cancel.** Adding (4.1), (4.2), and (4.3), we collect the coefficient of each of the six words:
> > - $XYZf$: $+1$ from (4.1), $-1$ from (4.3); total $0$.
> > - $XZYf$: $-1$ from (4.1), $+1$ from (4.2); total $0$.
> > - $YZXf$: $-1$ from (4.1), $+1$ from (4.2); total $0$.
> > - $ZYXf$: $+1$ from (4.1), $-1$ from (4.3); total $0$.
> > - $YXZf$: $-1$ from (4.2), $+1$ from (4.3); total $0$.
> > - $ZXYf$: $-1$ from (4.2), $+1$ from (4.3); total $0$.
> >
> > These six words are all the words that occur in (4.1)–(4.3) (each line contains four of them, twelve occurrences in all, and the table accounts for all twelve). Hence
> > $$\big( [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] \big)f = 0 \qquad \text{(sum of (4.1)–(4.3); the table; pointwise addition in } \mathfrak{X}(M)\text{)}.$$
> >
> > **Step 4: conclude.** The smooth vector field $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]]$ acts on every $f \in C^\infty(M)$ as the zero function; so does the zero vector field; by the uniqueness in Lemma 1(b) (two vector fields that agree on every function are equal), it is the zero vector field. Therefore the Jacobi identity holds in $\mathfrak{X}(M)$.

> [!note]- Lemma 5: $\mathfrak{X}(M)$ is infinite-dimensional when $\dim M \geq 1$, and zero when $\dim M = 0$
> **Statement:** If $m = \dim M \geq 1$, then $\mathfrak{X}(M)$ contains an infinite linearly independent set, so it is not finite-dimensional. If $m = 0$, then $\mathfrak{X}(M) = \{0\}$.
>
> **Hint:** Choose a chart $(U, \varphi)$ and a bump function $\psi$ with $\psi = 1$ near a point of $U$ and $\operatorname{supp}\psi \subset U$; the fields $\psi\,(x^1)^k\,\partial/\partial x^1$, $k = 0, 1, 2, \dots$, are linearly independent because a polynomial in one variable vanishing on an interval is the zero polynomial.
>
> **Why needed:** It is the clause "infinite dimensional" of Bär's Example 1.2.2.4.
>
> > [!note]- Full proof
> > **Case $m = 0$.** Each $T_pM$ is a real vector space of dimension $\dim M = 0$ ([[Thm - Dimension of the Tangent Space]]), so $T_pM = \{0\}$ and every vector field is the zero field. Hence $\mathfrak{X}(M) = \{0\}$, the zero Lie algebra.
> >
> > **Case $m \geq 1$, Step 0: the bump function and the fields.** Fix $p_0 \in M$ and a smooth chart $(U, \varphi)$ with $p_0 \in U$. Choose an open set $W$ with $p_0 \in W$ and $\overline{W} \subset U$ compact (take $W = \varphi^{-1}(B)$ for an open ball $B$ around $\varphi(p_0)$ whose closure lies in $\varphi(U)$; then $\overline{W} = \varphi^{-1}(\overline{B})$ is compact as the continuous image of a compact set under $\varphi^{-1}$, and closed in $M$ because $M$ is Hausdorff). By [[Thm - Existence of Smooth Bump Functions]] — for a closed set $A \subset M$ and an open $U \supset A$ there is $\psi \in C^\infty(M)$ with values in $[0, 1]$, $\psi \equiv 1$ on $A$, and $\operatorname{supp}\psi \subset U$ — applied with $A = \overline{W}$, we obtain such a $\psi$. For each integer $k \geq 0$ define a vector field $X_k$ on $M$ by
> > $$X_k(p) := \begin{cases} \psi(p)\,\big(x^1(p)\big)^k\,\dfrac{\partial}{\partial x^1}\Big|_p, & p \in U, \\[4pt] 0, & p \in M \setminus \operatorname{supp}\psi . \end{cases}$$
> > The two open sets $U$ and $M \setminus \operatorname{supp}\psi$ cover $M$ (because $\operatorname{supp}\psi \subset U$), and on their intersection $U \setminus \operatorname{supp}\psi$ both prescriptions give $0$ (since $\psi = 0$ there), so $X_k$ is well defined. It is smooth: on $U$ its only nonzero component in the chart $(U, \varphi)$ is $\psi\,(x^1)^k$, a product of smooth functions, and on $M \setminus \operatorname{supp}\psi$ it is the zero field; smoothness is a local property and every point lies in one of these two open sets. So $X_k \in \mathfrak{X}(M)$.
> >
> > **Step 1: linear independence.** Suppose $K \geq 0$ and $c_0, \dots, c_K \in \mathbb{R}$ satisfy $\sum_{k=0}^K c_k X_k = 0$ in $\mathfrak{X}(M)$. Evaluating at $p \in W \subset U$ and reading off the $\partial/\partial x^1|_p$ component (the coordinate tangent vectors form a basis of $T_pM$, so components are unique),
> > $$0 = \psi(p) \sum_{k=0}^K c_k \big(x^1(p)\big)^k = \sum_{k=0}^K c_k \big(x^1(p)\big)^k \qquad \text{(definition of } X_k \text{; } \psi(p) = 1 \text{ for } p \in W \subset \overline{W}\text{)}.$$
> > Thus the real polynomial $P(t) := \sum_{k=0}^K c_k t^k$ vanishes at every point of the set $x^1(W) \subset \mathbb{R}$. This set is open in $\mathbb{R}$ and nonempty: $\varphi(W) = B$ is a nonempty open ball in $\mathbb{R}^m$, and $x^1(W)$ is its image under the projection $(t^1, \dots, t^m) \mapsto t^1$, which is an open map (it maps a ball of radius $r$ about $(a^1, \dots, a^m)$ onto the interval $(a^1 - r, a^1 + r)$). A nonempty open subset of $\mathbb{R}$ contains an interval, hence infinitely many points, and a polynomial of degree at most $K$ with more than $K$ roots is the zero polynomial (a nonzero polynomial of degree $d$ over a field has at most $d$ roots). Hence $c_0 = \dots = c_K = 0$.
> >
> > **Step 2: conclude.** Every finite subfamily of $\{X_k : k \geq 0\}$ is linearly independent, so $\{X_k\}$ is an infinite linearly independent subset of $\mathfrak{X}(M)$. A vector space containing an infinite linearly independent set is not finite-dimensional (a finite-dimensional space of dimension $d$ has no linearly independent set of more than $d$ elements, [[Def - Dimension]]). Therefore $\mathfrak{X}(M)$ is infinite-dimensional.

> [!note]- Lemma 6: The function product rule
> **Statement:** For $X, Y \in \mathfrak{X}(M)$ and $f, g \in C^\infty(M)$,
> $$[fX, gY] = fg\,[X, Y] + f\,(Xg)\,Y - g\,(Yf)\,X .$$
>
> **Hint:** $(fX)h = f\,(Xh)$ pointwise; expand $[fX, gY]h = f\,X(g\,Yh) - g\,Y(f\,Xh)$ with the Leibniz rule of Lemma 1(a).
>
> **Why needed:** Part (iii) of the theorem; it is the identity that makes curvature a tensor in chapter II.
>
> > [!note]- Full proof
> > First, $fX \in \mathfrak{X}(M)$: in a chart its components are $f X^i$, products of smooth functions, so it is smooth; likewise $gY$. For $h \in C^\infty(M)$ and $p \in M$, $((fX)h)(p) = (fX)(p)h = f(p)\,X(p)h = (f\,Xh)(p)$ by the definition of $fX$ and the pointwise vector-space structure of $T_pM$; thus $(fX)h = f\,(Xh)$ as functions. Now, for $h \in C^\infty(M)$,
> > $$[fX, gY]h = (fX)\big((gY)h\big) - (gY)\big((fX)h\big) = f\,X\big(g\,(Yh)\big) - g\,Y\big(f\,(Xh)\big) \qquad \text{(definition of the bracket; } (fX)h = f\,Xh \text{ and } (gY)h = g\,Yh \text{, twice each)}$$
> > $$= f\big( (Xg)(Yh) + g\,X(Yh) \big) - g\big( (Yf)(Xh) + f\,Y(Xh) \big) \qquad \text{(Leibniz rule } X(g\,k) = (Xg)\,k + g\,(Xk) \text{ of Lemma 1(a), applied to } k = Yh \text{ and to } k = Xh\text{)}$$
> > $$= fg\big( X(Yh) - Y(Xh) \big) + f\,(Xg)\,(Yh) - g\,(Yf)\,(Xh) \qquad \text{(regroup, using commutativity of multiplication in } C^\infty(M)\text{)}$$
> > $$= \big( fg\,[X, Y] + f\,(Xg)\,Y - g\,(Yf)\,X \big)h \qquad \text{(definition of the bracket; } (kZ)h = k\,(Zh) \text{ for } k \in C^\infty(M) \text{ and the pointwise linear structure)}.$$
> > Both sides are smooth vector fields (the right-hand side is a $C^\infty(M)$-linear combination of smooth fields, hence smooth by the chart criterion), and they agree on every $h$; by Lemma 1(b) they are equal. The two special cases in the statement are $g = 1$ (then $Xg = 0$, since a derivation annihilates constants: $X(p)(1) = X(p)(1 \cdot 1) = 2\,X(p)(1)$, so $X(p)(1) = 0$) and $f = 1$.

> [!note]- Lemma 7: $F$-relatedness in terms of functions
> **Statement:** Let $F : M \to N$ be smooth, $X \in \mathfrak{X}(M)$, $X' \in \mathfrak{X}(N)$. Then $X \sim_F X'$ if and only if
> $$X(h \circ F) = (X'h) \circ F \qquad \text{for every } h \in C^\infty(N).$$
>
> **Hint:** Evaluate at $p$: the left side is $(d_pF(X(p)))(h)$ by the definition of the differential, the right side is $X'(F(p))h$. For the converse use that a derivation at $F(p)$ is determined by its values on $C^\infty(N)$.
>
> **Why needed:** It is the form of relatedness on which the bracket, an operator on functions, can act; Lemma 8 is nothing but this lemma applied twice.
>
> > [!note]- Full proof
> > Note first that for $h \in C^\infty(N)$ the function $h \circ F$ lies in $C^\infty(M)$ ([[Ex - Composition of Smooth Maps is Smooth]]), so $X(h \circ F)$ is defined, and $X'h \in C^\infty(N)$ by Lemma 1(a) applied on $N$, so $(X'h) \circ F$ is defined; both sides of the displayed identity are functions on $M$. For every $p \in M$ and $h \in C^\infty(N)$,
> > $$\big( X(h \circ F) \big)(p) = X(p)(h \circ F) = \big( d_pF(X(p)) \big)(h) \qquad \text{(definition of } Xf \text{; definition of the differential, } (d_pF(v))(h) = v(h \circ F)\text{)}, \tag{7.1}$$
> > $$\big( (X'h) \circ F \big)(p) = (X'h)(F(p)) = X'(F(p))\,h \qquad \text{(definition of composition; definition of } X'h\text{)}. \tag{7.2}$$
> >
> > **Direction 1 ($\Rightarrow$).** Assume $X \sim_F X'$, that is, $d_pF(X(p)) = X'(F(p))$ in $T_{F(p)}N$ for every $p$. Then for every $h$ and $p$, $(d_pF(X(p)))(h) = X'(F(p))\,h$, so by (7.1) and (7.2) the functions $X(h \circ F)$ and $(X'h) \circ F$ agree at every $p$; hence they are equal.
> >
> > **Direction 2 ($\Leftarrow$).** Assume $X(h \circ F) = (X'h) \circ F$ for every $h \in C^\infty(N)$. Fix $p \in M$. By (7.1) and (7.2), the two derivations $d_pF(X(p))$ and $X'(F(p))$ at $F(p)$ take the same value on every $h \in C^\infty(N)$. A derivation at $F(p)$ is by definition a map $C^\infty(N) \to \mathbb{R}$, and two maps agreeing on every argument are equal; so $d_pF(X(p)) = X'(F(p))$. As $p$ was arbitrary, $X \sim_F X'$.

> [!note]- Lemma 8: Naturality of the bracket under $F$-relatedness
> **Statement:** Let $F : M \to N$ be smooth, $X, Y \in \mathfrak{X}(M)$, $X', Y' \in \mathfrak{X}(N)$ with $X \sim_F X'$ and $Y \sim_F Y'$. Then $[X, Y] \sim_F [X', Y']$.
>
> **Hint:** For $h \in C^\infty(N)$: $X(Y(h \circ F)) = X((Y'h) \circ F) = (X'(Y'h)) \circ F$, using Lemma 7 for $Y$ and then for $X$ with the function $Y'h$.
>
> **Why needed:** Part (iv), and the engine of Part (v) and of the fundamental-vector-field homomorphism in §1.5.
>
> > [!note]- Full proof
> > By Lemma 2, $[X, Y] \in \mathfrak{X}(M)$ and $[X', Y'] \in \mathfrak{X}(N)$, so by Lemma 7 (Direction 2) it suffices to show that $[X, Y](h \circ F) = ([X', Y']h) \circ F$ for every $h \in C^\infty(N)$. Fix $h$. **Apply the relatedness of $Y$ to $h$, then of $X$ to $Y'h$:**
> > $$X\big( Y(h \circ F) \big) = X\big( (Y'h) \circ F \big) \qquad \text{(Lemma 7, Direction 1, for } Y \sim_F Y' \text{ and the function } h\text{)}$$
> > $$= \big( X'(Y'h) \big) \circ F \qquad \text{(Lemma 7, Direction 1, for } X \sim_F X' \text{ and the function } Y'h \in C^\infty(N)\text{)}. \tag{8.1}$$
> > **The same with the roles exchanged:** the computation used only the two relatedness hypotheses, so exchanging $(X, X')$ with $(Y, Y')$ gives
> > $$Y\big( X(h \circ F) \big) = \big( Y'(X'h) \big) \circ F \qquad \text{(Lemma 7 for } X \sim_F X' \text{ with } h \text{, then for } Y \sim_F Y' \text{ with } X'h\text{)}. \tag{8.2}$$
> > **Subtract:**
> > $$[X, Y](h \circ F) = X\big( Y(h \circ F) \big) - Y\big( X(h \circ F) \big) = \big( X'(Y'h) - Y'(X'h) \big) \circ F = \big( [X', Y']h \big) \circ F \qquad \text{(definition of the bracket on } M \text{; (8.1) and (8.2), composition being linear; definition of the bracket on } N\text{)}.$$
> > This holds for every $h \in C^\infty(N)$, so by Lemma 7 (Direction 2), $[X, Y] \sim_F [X', Y']$.

> [!note]- Lemma 9: Push-forward along a diffeomorphism is a Lie algebra isomorphism
> **Statement:** Let $F : M \to N$ be a diffeomorphism. (a) For $X \in \mathfrak{X}(M)$, the push-forward $dF(X)$, defined by $dF(X)(q) = d_{F^{-1}(q)}F(X(F^{-1}(q)))$, is a smooth vector field on $N$, and it is the unique vector field on $N$ that is $F$-related to $X$. (b) $dF([X, Y]) = [dF(X), dF(Y)]$ for all $X, Y \in \mathfrak{X}(M)$. (c) $dF : \mathfrak{X}(M) \to \mathfrak{X}(N)$ is $\mathbb{R}$-linear and bijective with inverse $d(F^{-1})$; hence it is an isomorphism of Lie algebras.
>
> **Hint:** (a) is the sibling page's Proposition C; for (b) apply Lemma 8 to $X \sim_F dF(X)$, $Y \sim_F dF(Y)$, then use uniqueness; for (c) use the chain rule $d_{F(p)}(F^{-1}) \circ d_pF = \mathrm{id}_{T_pM}$.
>
> **Why needed:** Part (v) and the Corollary.
>
> > [!note]- Full proof
> > **Part (a).** This is Proposition C, parts (i) and (ii), of [[Def - Left and Right Translations and Conjugation on a Lie Group]], proved in full there: *for a diffeomorphism $F : M \to N$ and $X \in \mathfrak{X}(M)$, the field $dF(X)$ is smooth, satisfies $d_pF(X(p)) = dF(X)(F(p))$ for every $p \in M$, and is the only vector field on $N$ with this property.* We restate the two-line argument for the relatedness and the uniqueness, since they are used below. For $p \in M$, put $q = F(p)$, so $F^{-1}(q) = p$; then $dF(X)(F(p)) = dF(X)(q) = d_{F^{-1}(q)}F(X(F^{-1}(q))) = d_pF(X(p))$ (definition of $dF(X)$), which says $X \sim_F dF(X)$. If $Z \in \mathfrak{X}(N)$ also satisfies $X \sim_F Z$, then for every $q \in N$, with $p := F^{-1}(q)$ (which exists and is unique because $F$ is bijective), $Z(q) = Z(F(p)) = d_pF(X(p)) = dF(X)(q)$ (relatedness of $Z$; definition of $dF(X)$), so $Z = dF(X)$.
> >
> > **Part (b).** Let $X, Y \in \mathfrak{X}(M)$. By Part (a), $X \sim_F dF(X)$ and $Y \sim_F dF(Y)$. By Lemma 8 applied with $X' = dF(X)$ and $Y' = dF(Y)$,
> > $$[X, Y] \sim_F [\,dF(X), dF(Y)\,] \qquad \text{(Lemma 8)}.$$
> > On the other hand, by Part (a) applied to the smooth field $[X, Y]$ (smooth by Lemma 2), $[X, Y] \sim_F dF([X, Y])$, and $dF([X, Y])$ is the *unique* field on $N$ that is $F$-related to $[X, Y]$. Since $[dF(X), dF(Y)]$ is a smooth vector field on $N$ (Lemma 2 on $N$) that is $F$-related to $[X, Y]$, uniqueness gives
> > $$dF([X, Y]) = [\,dF(X), dF(Y)\,] \qquad \text{(uniqueness in Part (a))}.$$
> >
> > **Part (c), linearity.** For $X, Y \in \mathfrak{X}(M)$, $a, b \in \mathbb{R}$, and $q \in N$, with $p := F^{-1}(q)$,
> > $$dF(aX + bY)(q) = d_pF\big( (aX + bY)(p) \big) = d_pF\big( aX(p) + bY(p) \big) = a\,d_pF(X(p)) + b\,d_pF(Y(p)) = \big( a\,dF(X) + b\,dF(Y) \big)(q) \qquad \text{(definition of } dF \text{; pointwise structure; linearity of } d_pF \text{; definition of } dF \text{ twice)}.$$
> >
> > **Part (c), invertibility.** $F^{-1} : N \to M$ is a diffeomorphism, so $d(F^{-1}) : \mathfrak{X}(N) \to \mathfrak{X}(M)$ is defined by Part (a) applied to $F^{-1}$. For $X \in \mathfrak{X}(M)$ and $p \in M$, with $q := F(p)$ so that $(F^{-1})^{-1}(p) = F(p) = q$,
> > $$d(F^{-1})\big( dF(X) \big)(p) = d_q(F^{-1})\big( dF(X)(q) \big) = d_q(F^{-1})\big( d_pF(X(p)) \big) = d_p(F^{-1} \circ F)(X(p)) = d_p(\mathrm{id}_M)(X(p)) = X(p) \qquad \text{(definition of } d(F^{-1}) \text{; definition of } dF(X) \text{ with } F^{-1}(q) = p \text{; the chain rule; } F^{-1} \circ F = \mathrm{id}_M \text{; } d_p\mathrm{id}_M = \mathrm{id}_{T_pM}\text{)}.$$
> > The chain rule used is [[Thm - Chain Rule for the Differential]]: *for smooth $F : M \to N$ and $G : N \to P$ and $p \in M$, $d_p(G \circ F) = d_{F(p)}G \circ d_pF$, and $d_p(\mathrm{id}_M) = \mathrm{id}_{T_pM}$.* Hence $d(F^{-1}) \circ dF = \mathrm{id}_{\mathfrak{X}(M)}$. The same computation with $F$ and $F^{-1}$ exchanged (every step applies, since $F^{-1}$ is a diffeomorphism with inverse $F$, and $F \circ F^{-1} = \mathrm{id}_N$) gives $dF \circ d(F^{-1}) = \mathrm{id}_{\mathfrak{X}(N)}$. So $dF$ is a linear bijection with inverse $d(F^{-1})$.
> >
> > **Part (c), the inverse preserves brackets.** Part (b) applied to the diffeomorphism $F^{-1}$ gives $d(F^{-1})([X', Y']) = [d(F^{-1})(X'), d(F^{-1})(Y')]$ for all $X', Y' \in \mathfrak{X}(N)$. Hence $dF$ is a bijective linear map preserving brackets whose inverse also preserves brackets: an isomorphism of Lie algebras.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a smooth manifold and $X, Y, Z \in \mathfrak{X}(M)$. We need to show the five parts of the theorem and the corollary.
>
> **Step 0 — the objects exist.** By Lemma 1(a), for every smooth vector field $X$ and $f \in C^\infty(M)$ the function $Xf$ is smooth, so the iterated expressions $X(Yf)$, $Y(Xf)$ are smooth functions and the prescription $f \mapsto X(Yf) - Y(Xf)$ is meaningful.
>
> **Part (i) — the bracket is a unique smooth vector field with the stated components.** By Lemma 1(b), $[X, Y](p) : f \mapsto X(p)(Yf) - Y(p)(Xf)$ is a derivation at $p$ for every $p \in M$, so $[X, Y] : p \mapsto [X, Y](p)$ is a vector field on $M$ satisfying $[X, Y]f = X(Yf) - Y(Xf)$ for every $f$, and by the uniqueness clause of Lemma 1(b) it is the only vector field with this property. By Lemma 2, in every smooth chart $(U, (x^i))$ its components are $[X, Y]^j = X(Y^j) - Y(X^j) = \sum_i (X^i\,\partial Y^j/\partial x^i - Y^i\,\partial X^j/\partial x^i)$, which are smooth on $U$; hence $[X, Y]$ is smooth, $[X, Y] \in \mathfrak{X}(M)$. This proves (i).
>
> **Part (ii) — the Lie algebra axioms.** $\mathfrak{X}(M)$ is a real vector space under the pointwise operations (Notation). By Part (i), $[\cdot, \cdot]$ is a map $\mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$. By Lemma 3(a) it is bilinear over $\mathbb{R}$ and antisymmetric; by Lemma 4 it satisfies the Jacobi identity $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$. These are the three axioms of [[Def - Lie Algebra]] — a real vector space with a bilinear, antisymmetric bracket satisfying the Jacobi identity — so $(\mathfrak{X}(M), [\cdot, \cdot])$ is a real Lie algebra; by Lemma 3(b) it also satisfies Bär's form of the Jacobi identity. By Lemma 5, it is infinite-dimensional if $\dim M \geq 1$ and is the zero Lie algebra if $\dim M = 0$. This proves (ii).
>
> **Part (iii) — the function product rule.** This is Lemma 6: for $f, g \in C^\infty(M)$, $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$, with the two special cases obtained by setting $g = 1$ or $f = 1$ and using that a vector field annihilates constant functions (shown at the end of Lemma 6).
>
> **Part (iv) — naturality.** Let $F : M \to N$ be smooth, $X' , Y' \in \mathfrak{X}(N)$ with $X \sim_F X'$ and $Y \sim_F Y'$. By Lemma 8 (whose proof applies Lemma 7 — $X \sim_F X'$ if and only if $X(h \circ F) = (X'h) \circ F$ for all $h \in C^\infty(N)$ — twice and subtracts), $[X, Y] \sim_F [X', Y']$. This proves (iv).
>
> **Part (v) — push-forward along a diffeomorphism.** Let $F : M \to N$ be a diffeomorphism. By Lemma 9(a), $dF(X)$ is the unique smooth vector field on $N$ that is $F$-related to $X$; by Lemma 9(b), which combines Part (iv) with this uniqueness, $dF([X, Y]) = [dF(X), dF(Y)]$, which in the notation $F_* = dF$ reads $F_*[X, Y] = [F_*X, F_*Y]$; by Lemma 9(c), $dF : \mathfrak{X}(M) \to \mathfrak{X}(N)$ is linear and bijective with inverse $d(F^{-1})$, and both $dF$ and $d(F^{-1})$ preserve brackets, so $dF$ is an isomorphism of Lie algebras. This proves (v), and with it the theorem.
>
> **The Corollary — left-invariant fields form a Lie subalgebra.** Let $G$ be a Lie group and let $X, Y \in \mathfrak{X}(G)$ be left-invariant, so that $dL_g(X) = X$ and $dL_g(Y) = Y$ for every $g \in G$ ([[Def - Left-Invariant Vector Field]]). For each $g$, the left translation $L_g$ is a diffeomorphism of $G$ with inverse $L_{g^{-1}}$ (Proposition A(iii) of [[Def - Left and Right Translations and Conjugation on a Lie Group]]: $L_g$ is smooth as the restriction of the smooth multiplication to $\{g\} \times G$, and $L_{g^{-1}} \circ L_g = L_e = \mathrm{id}_G = L_g \circ L_{g^{-1}}$). Hence, by Part (v) applied to $F = L_g$,
> $$dL_g([X, Y]) = [\,dL_g(X), dL_g(Y)\,] = [X, Y] \qquad \text{(Part (v); left-invariance of } X \text{ and } Y\text{)}.$$
> Since $g \in G$ was arbitrary, $[X, Y]$ is left-invariant. The set $\mathfrak{g}$ of left-invariant fields is a vector subspace of $\mathfrak{X}(G)$: if $dL_g(X) = X$ and $dL_g(Y) = Y$ then $dL_g(aX + bY) = a\,dL_g(X) + b\,dL_g(Y) = aX + bY$ by the linearity of $dL_g$ (Lemma 9(c)), and $dL_g(0) = 0$. So $\mathfrak{g}$ is a vector subspace closed under the bracket, that is, a Lie subalgebra of $\mathfrak{X}(G)$ in the sense of [[Def - Lie Subalgebra and Abelian Lie Algebra]]; and a Lie subalgebra is a Lie algebra, because bilinearity, antisymmetry, and the Jacobi identity are identities among elements of $\mathfrak{X}(G)$ (Part (ii)) and therefore hold among elements of $\mathfrak{g}$. The same closure statement, with the bracket transported to $T_eG$, is proved on [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]].
>
> Therefore $(\mathfrak{X}(M), [\cdot, \cdot])$ is a real Lie algebra, the bracket is natural with respect to $F$-related fields and is preserved by push-forward along diffeomorphisms, and the left-invariant vector fields on a Lie group form a Lie subalgebra. $\blacksquare$

**The smallest concrete case, checked by hand.** On $M = \mathbb{R}^2$ with coordinates $(x, y)$, take $X = \partial/\partial x$, $Y = x\,\partial/\partial y$, $Z = y\,\partial/\partial x$; their component pairs are $(1, 0)$, $(0, x)$, $(y, 0)$. The coordinate formula of Part (i) gives $[X, Y]^j = X(Y^j) - Y(X^j)$: $X$ applied to the components $(0, x)$ of $Y$ gives $(0, 1)$, and $Y$ applied to the constant components of $X$ gives $(0, 0)$, so $[X, Y] = \partial/\partial y$. Likewise $Y(Z^1, Z^2) = (x\,\partial_y y, 0) = (x, 0)$ and $Z(Y^1, Y^2) = (0, y\,\partial_x x) = (0, y)$, so $[Y, Z] = x\,\partial/\partial x - y\,\partial/\partial y$; and $Z(X^1, X^2) = (0, 0)$, $X(Z^1, Z^2) = (\partial_x y, 0) = (0, 0)$, so $[Z, X] = 0$. For the Jacobi identity: $[X, [Y, Z]] = [\partial_x, x\,\partial_x - y\,\partial_y]$ has components $X(x, -y) - (x\partial_x - y\partial_y)(1, 0) = (1, 0)$, so it equals $\partial/\partial x$; $[Y, [Z, X]] = [Y, 0] = 0$; $[Z, [X, Y]] = [y\,\partial_x, \partial_y]$ has components $Z(0, 1) - \partial_y(y, 0) = (0, 0) - (1, 0) = (-1, 0)$, so it equals $-\partial/\partial x$. The cyclic sum is $\partial/\partial x + 0 - \partial/\partial x = 0$, as Part (ii) asserts. For naturality, take the diffeomorphism $F : \mathbb{R} \to (0, \infty)$, $F(x) = e^x$, with coordinate $u$ on the target, and the fields $X = \partial/\partial x$, $Y = x\,\partial/\partial x$ on $\mathbb{R}$, so that $[X, Y] = (\partial_x x)\,\partial/\partial x = \partial/\partial x$. The push-forwards are $dF(X)(u) = e^{x}\,\partial/\partial u|_{u}$ with $x = \log u$, that is, $dF(X) = u\,\partial/\partial u$, and $dF(Y) = u \log u\,\partial/\partial u$. Then $[dF(X), dF(Y)] = \big( u\,\partial_u(u \log u) - u \log u\,\partial_u u \big)\,\partial/\partial u = (u \log u + u - u \log u)\,\partial/\partial u = u\,\partial/\partial u = dF([X, Y])$, as Part (v) asserts.

---

# Cross-Field Exercise Suggestions

**Angular momentum operators in quantum mechanics.** The operators $L_x = y\,\partial_z - z\,\partial_y$, $L_y = z\,\partial_x - x\,\partial_z$, $L_z = x\,\partial_y - y\,\partial_x$ on $\mathbb{R}^3$ are smooth vector fields (the infinitesimal rotations about the three axes), and the commutation relations $[L_x, L_y] = -L_z$ and cyclic permutations — the classical form of the angular momentum algebra, up to the factor $i\hbar$ and a sign that depends on the convention — are instances of Part (i)'s coordinate formula. The theorem applies because the $L$'s are first-order operators without zeroth-order term; the non-obvious point is that the second-order terms of $L_x L_y$, which physicists never write down, cancel in the commutator for the reason given in Lemma 2, so that the commutator is again a first-order operator. The exercise is to compute the three brackets by the coordinate formula, confirm that they close, and deduce from the Corollary's mechanism (closure under the bracket plus inheritance of the axioms) that the span of $L_x, L_y, L_z$ is a three-dimensional Lie algebra, which the reader will later recognise as $\mathfrak{so}(3)$ ([[Ex - R^3 with the Cross Product is the Lie Algebra so(3)]]).

**Hamiltonian vector fields and the Poisson bracket.** On $\mathbb{R}^{2n}$ with coordinates $(q^i, p_i)$, each smooth function $H$ has the Hamiltonian vector field $X_H = \sum_i (\partial H/\partial p_i)\,\partial/\partial q^i - (\partial H/\partial q^i)\,\partial/\partial p_i$, and the Poisson bracket is $\{H, K\} := X_H K$. The exercise is to show by the coordinate formula of Part (i) that $[X_H, X_K] = -X_{\{H, K\}}$ (the sign depends on the convention for $\{\cdot, \cdot\}$; the reader should fix one and verify), and then to deduce the Jacobi identity for the Poisson bracket from Part (ii)'s Jacobi identity for vector fields together with the injectivity of $H \mapsto X_H$ on functions modulo constants. The theorem applies because $X_H$ and $X_K$ are smooth vector fields; the non-obvious point is that the Jacobi identity of classical mechanics, usually verified by a lengthy expansion, is inherited from the vector-field Jacobi identity through a single linear map.

**Involutive distributions and the Frobenius theorem.** A rank-$r$ [[Def - Distribution on a Manifold|distribution]] $D \subset TM$ is [[Def - Involutive Distribution|involutive]] if $[X, Y]$ is a section of $D$ whenever $X$ and $Y$ are; the [[Thm - The Frobenius Theorem|Frobenius theorem]] says that involutive distributions are exactly the integrable ones. The exercise is to show that involutivity can be checked on a local frame $E_1, \dots, E_r$ of $D$: if $[E_a, E_b] = \sum_c c_{ab}^c E_c$ for smooth functions $c_{ab}^c$, then $[X, Y] \in D$ for all sections $X = \sum_a f^a E_a$, $Y = \sum_b g^b E_b$. The theorem applies through Part (iii): $[f^a E_a, g^b E_b] = f^a g^b [E_a, E_b] + f^a (E_a g^b) E_b - g^b (E_b f^a) E_a$, and every term is a section of $D$. The non-obvious point is that the bracket is *not* $C^\infty(M)$-bilinear, so closure on a frame does not trivially imply closure on all sections; it is the explicit form of the correction terms in Part (iii) that saves the argument.

**The bracket of $F$-related fields on a submersion.** Let $F : M \to N$ be a smooth surjective submersion, and call $X \in \mathfrak{X}(M)$ *projectable* if there is $X' \in \mathfrak{X}(N)$ with $X \sim_F X'$ (the field $X'$ is then unique, because $F$ is surjective). The exercise is to show that the projectable fields form a Lie subalgebra of $\mathfrak{X}(M)$ and that $X \mapsto X'$ is a Lie algebra homomorphism onto its image. The theorem applies through Part (iv), which needs no diffeomorphism; the non-obvious point is that Part (v) is *not* available (a submersion has no push-forward of arbitrary fields), and the reader must see that naturality for related fields is exactly the tool that survives. This is the structure used in chapter III, where the projection of a principal bundle is a submersion and the invariant fields are the projectable ones.

---

# Bridges

**To the Lie algebra of a Lie group.** The Corollary is the bridge from this page to the whole of Lie theory. Given a Lie group $G$, the left-invariant fields $\mathfrak{g} \subset \mathfrak{X}(G)$ are closed under the bracket by the Corollary, and evaluation at $e$ is a linear isomorphism $\mathfrak{g} \to T_eG$ (Proposition D of [[Def - Left and Right Translations and Conjugation on a Lie Group]]; the inverse sends $X_0 \in T_eG$ to the field $g \mapsto d_eL_g(X_0)$). Transporting the bracket along this isomorphism makes $T_eG$ a Lie algebra of dimension $\dim G$, which is [[Def - The Lie Algebra of a Lie Group]]. The construction is intrinsic — it uses only the group structure and the smooth structure — and the theorem's Part (v) is what makes it so: the bracket transported to $T_eG$ does not depend on any choice, because no choice was made in defining $[\cdot, \cdot]$ on $\mathfrak{X}(G)$. For a matrix group $G \subset GL(n; \mathbb{K})$ the transported bracket is the matrix commutator ([[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]), which is the form in which [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]] computes $\mathfrak{o}(n)$, $\mathfrak{sl}(n; \mathbb{R})$, $\mathfrak{u}(n)$, and $\mathfrak{su}(n)$.

**To fundamental vector fields of a group action.** If $G$ acts smoothly on $M$ on the right, every $\xi \in \mathfrak{g}$ determines the fundamental vector field $\xi_M(p) = \frac{d}{dt}\big|_{t=0}\, p \cdot \exp(t\xi)$ ([[Def - Fundamental Vector Field of a Group Action]]). The construction is the push-forward of the left-invariant field $\tilde\xi$ on $G$ along the orbit map $\ell_p : G \to M$, $g \mapsto p \cdot g$: one checks that $\tilde\xi \sim_{\ell_p} \xi_M$ for every $p$. The orbit map is not a diffeomorphism, so Part (v) does not apply; but Part (iv) does, and it gives $[\tilde\xi, \tilde\eta] \sim_{\ell_p} [\xi_M, \eta_M]$, whence $[\xi, \eta]_M = [\xi_M, \eta_M]$. This is [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]; the same argument with left actions produces right-invariant fields on $G$ and an anti-homomorphism, the sign being the one recorded on that page. It is the first place in the series where naturality for *related* fields, rather than for push-forwards, is indispensable.

**To curvature on a vector bundle.** For a covariant derivative $\nabla$ on a vector bundle $E \to M$, the curvature is $F_\nabla(X, Y)s = \nabla_X\nabla_Y s - \nabla_Y\nabla_X s - \nabla_{[X, Y]}s$. That this expression is $C^\infty(M)$-linear in $X$ — and hence, by the tensor characterisation lemma, that $F_\nabla$ is a $2$-form with values in $\operatorname{End} E$ — is a direct consequence of Part (iii) in the form $[fX, Y] = f[X, Y] - (Yf)X$: the term $-(Yf)X$ inside $\nabla_{[fX, Y]}$ produces $+(Yf)\nabla_X s$, which cancels the $-(Yf)\nabla_X s$ coming from the Leibniz rule in $\nabla_Y(f\nabla_X s)$. The bracket's failure to be $C^\infty(M)$-bilinear is thus exactly what is needed to make curvature tensorial; a bracket that *were* function-bilinear would leave the Leibniz cross-terms uncancelled. This is the model proof of the series' proof standard and the entry point to chapter II.

**To the Lie derivative and to flows.** The bracket $[X, Y]$ coincides with the [[Def - Lie Derivative of a Vector Field|Lie derivative]] $\mathcal{L}_X Y = \frac{d}{dt}\big|_{t=0}\, d(\phi^X_{-t})(Y \circ \phi^X_t)$, the rate of change of $Y$ transported along the flow of $X$, and $[X, Y] = 0$ if and only if the flows of $X$ and $Y$ commute. These identifications give the bracket its geometric meaning — it measures the failure of two flows to commute — but they are **not proved on this page and no page in this series leans on them**; the series uses only the algebraic characterisation $[X, Y]f = X(Yf) - Y(Xf)$ and the properties proved above. The one flow-theoretic fact the series does need, that the flow of a left-invariant field is a right translation, is proved on [[Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields]] without reference to the Lie derivative.

---

# Unlocked by This

> [!tip] The Lie algebra of a Lie group *(from Lie theory)*
> With $\mathfrak{X}(G)$ a Lie algebra and left-invariant fields closed under the bracket, $\mathfrak{g} = T_eG$ becomes a finite-dimensional Lie algebra; see [[Def - The Lie Algebra of a Lie Group]] and [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]] for the classical groups.

> [!tip] The infinitesimal action of a Lie group *(from the theory of group actions)*
> Part (iv) makes $\xi \mapsto \xi_M$ a Lie algebra homomorphism for right actions, [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]; on a principal bundle this is the vertical distribution, the object a connection complements.

> [!tip] Curvature is a tensor *(from the theory of connections)*
> The function product rule of Part (iii) is the identity that makes $\nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X, Y]}$ function-linear in $X$ and $Y$; it is used on every curvature page of [[Gauge Theory II — Vector Bundles, Covariant Derivatives, and Curvature]].
