---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Lie Algebra"
  - "Def - Smooth Vector Field"
  - "Def - F-Related Vector Fields"
  - "Thm - Pushforward of Vector Fields under a Diffeomorphism"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ and $N$ are smooth manifolds — smooth, Hausdorff, second countable, with "smooth" meaning $C^\infty$, as fixed for the whole series. We write $\mathfrak{X}(M)$ for the real vector space of smooth [[Def - Smooth Vector Field|vector fields]] on $M$ and $C^\infty(M)$ for the ring of smooth real-valued functions on $M$. A vector field $X \in \mathfrak{X}(M)$ acts on a function $f \in C^\infty(M)$ as a derivation: $Xf \in C^\infty(M)$ is the function $p \mapsto X_p f$, where $X_p \in T_pM$ is a tangent vector at $p$ regarded as a derivation of germs at $p$. In a smooth chart $(U, (x^1, \dots, x^n))$ we write $\partial_i := \partial/\partial x^i$ for the coordinate vector fields and expand $X = X^i \partial_i$, $Y = Y^j \partial_j$ with component functions $X^i, Y^j \in C^\infty(U)$; the Einstein summation convention (sum over an index repeated once up, once down) is in force inside charts.

The [[Def - The Lie Bracket of Vector Fields|Lie bracket]] of $X, Y \in \mathfrak{X}(M)$ is the operator
$$[X, Y]f := X(Yf) - Y(Xf), \qquad f \in C^\infty(M),$$
equivalently the commutator $[X, Y] = XY - YX$ of $X$ and $Y$ viewed as $\mathbb{R}$-linear operators on $C^\infty(M)$. Part of the theorem is that this operator is again a smooth vector field.

For a smooth map $F : M \to N$ and $p \in M$, $dF_p : T_pM \to T_{F(p)}N$ is the [[Def - The Differential of a Smooth Map|differential]], characterised on tangent-vectors-as-derivations by
$$(dF_p v)(f) = v(f \circ F) \qquad \text{for all } v \in T_pM,\ f \in C^\infty(N). \tag{$\ast$}$$
Two fields $X \in \mathfrak{X}(M)$ and $X' \in \mathfrak{X}(N)$ are **$F$-related**, written $X \sim_F X'$, iff $dF_p(X_p) = X'_{F(p)}$ for every $p \in M$ (this is [[Def - F-Related Vector Fields|$F$-relatedness]]). When $F$ is a diffeomorphism, the **pushforward** $F_*X \in \mathfrak{X}(N)$ is the unique field $F$-related to $X$, given pointwise by $(F_*X)_q = dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ (this is [[Thm - Pushforward of Vector Fields under a Diffeomorphism|the pushforward theorem]]). Bär writes $dF(X)$ for what we write $F_*X$; the two notations denote the same field.

> [!warning] Convention: source misprint of the antisymmetry axiom
> Bär's Definition 1.2.1 prints the antisymmetry axiom as "$[v, w] = -[v, w]$", which — read literally — forces $[v,w] = 0$ and would collapse every Lie algebra to an abelian one. The intended axiom, used throughout this series and verified below, is
> $$[v, w] = -[w, v] \qquad \text{for all } v, w.$$
> We prove the correct form, $[X, Y] = -[Y, X]$, for the bracket of vector fields. (Content map, typo appendix.)

> [!warning] Convention: naturality generalised from $F : M \to M$ to $F : M \to N$
> Bär's Remark 1.2.4 and equation (1.5) state naturality for a diffeomorphism $F : M \to M$ of a single manifold to itself. Nothing in the argument uses $M = N$; we state and prove the naturality identity for a diffeomorphism $F : M \to N$ between two manifolds, which is the form used later in the series (for orbit maps of group actions, §1.5, and for coordinate changes).

The full symbol registry for the chapter is on the topic page [[Gauge Theory I — Lie Groups, Representations, and Group Actions]].

---

# Statement

> **Theorem (the Lie algebra of vector fields).** Let $M$ be a smooth manifold and let $\mathfrak{X}(M)$ carry the Lie bracket $[X, Y]f = X(Yf) - Y(Xf)$. Then:
>
> **(i) Lie algebra structure.** For all $X, Y \in \mathfrak{X}(M)$ the operator $[X, Y]$ is again a smooth vector field, and with this bracket $(\mathfrak{X}(M), [\cdot, \cdot])$ is a [[Def - Lie Algebra|Lie algebra]] over $\mathbb{R}$: the bracket is $\mathbb{R}$-bilinear, antisymmetric ($[X, Y] = -[Y, X]$), and satisfies the Jacobi identity
> $$\big[[X, Y], Z\big] + \big[[Y, Z], X\big] + \big[[Z, X], Y\big] = 0 \qquad \text{for all } X, Y, Z \in \mathfrak{X}(M).$$
> When $\dim M \geq 1$ this Lie algebra is infinite-dimensional.
>
> **(ii) Naturality under diffeomorphisms.** For every diffeomorphism $F : M \to N$ and all $X, Y \in \mathfrak{X}(M)$,
> $$F_*[X, Y] = [F_*X, F_*Y].$$
> Thus $F_* : \mathfrak{X}(M) \to \mathfrak{X}(N)$ is an isomorphism of Lie algebras, with inverse $(F^{-1})_*$.

The naturality identity (ii) is Bär's equation (1.5); in his notation, $dF([X, Y]) = [dF(X), dF(Y)]$.

---

# Motivation

The space $\mathfrak{X}(M)$ of smooth vector fields comes into the world with two algebraic operations already attached: it is a real vector space under pointwise addition and scalar multiplication, and it is a module over the ring $C^\infty(M)$ under multiplication by smooth functions. Neither of these lets one *multiply* two vector fields to get a third. The Lie bracket is the operation that fills this gap, and the present theorem is the statement that the operation it provides is not an ad hoc trick but a genuine, and in a precise sense the *only*, algebraic structure of its kind on $\mathfrak{X}(M)$.

Why does this matter for gauge theory? Because every Lie algebra one meets in the subject is, at bottom, a Lie algebra of vector fields. The Lie algebra $\mathfrak{g}$ of a Lie group $G$ is the algebra of [[Def - Left-Invariant Vector Field|left-invariant vector fields]] on $G$ under this very bracket; for a matrix group it turns into the commutator $XY - YX$ of matrices, but the *reason* the commutator is a Lie bracket is that it is inherited from the bracket of vector fields. The fundamental vector fields of a group action on a manifold — the infinitesimal generators of the symmetry, which drive the whole theory of connections and curvature — form the image of $\mathfrak{g}$ inside $\mathfrak{X}(M)$, and whether that image is a Lie subalgebra, and with which sign, is exactly a question about the bracket of vector fields. So this theorem is the foundation on which the algebraic side of the entire series is built.

There is a second reason the theorem is indispensable, and it is the naturality clause (ii). A vector field is a coordinate-free object, but every calculation with one is done in coordinates, and coordinates are changed by diffeomorphisms. Naturality says the bracket does not care: computing $[X, Y]$ and then transporting the result along a diffeomorphism gives the same field as transporting $X$ and $Y$ first and bracketing afterwards. This is what licenses the free change of chart in every later computation of a curvature, a structure equation, or a fundamental vector field, and it is what makes the Lie algebra structure a diffeomorphism *invariant* of the manifold rather than an artefact of a chosen atlas.

Bär's lecture notes list $(\mathfrak{X}(M), [\cdot, \cdot])$ as an example of a Lie algebra (Example 1.2.2.4) and state naturality (equation (1.5), Remark 1.2.4) without proof, calling both standard. We supply the proofs in full. The verification is the model computation for the whole subject: it shows exactly how the second-order terms in $XY$ and $YX$ cancel to leave a first-order operator, and how the naturality of the bracket is a two-line consequence of the way vector fields act on pulled-back functions.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypotheses — a smooth manifold and two of its vector fields — are so mild that the interesting question is the reverse one: when does a problem secretly present a Lie algebra of vector fields, so that this theorem's structure (bilinearity, antisymmetry, Jacobi, naturality) may be used without further checking?

The first disguised source is **a family of first-order linear differential operators on $C^\infty(M)$ that is closed under the commutator**. Property $B$: one is handed operators $D_1, D_2, \dots$ on smooth functions, each of the form $D = a^i \partial_i$ in coordinates (no zeroth-order or higher-order part), and asked whether they close into an algebra. The bridge $B \Rightarrow A$ is the identification of first-order operators-without-constant-term with vector fields, together with Lemma 1 below, which says the commutator of two such is again one of the same kind; so "closed under commutator" is exactly "a Lie subalgebra of $\mathfrak{X}(M)$", and Jacobi and antisymmetry are free. *Example problem:* the operators $\partial_x$, $x\partial_x$, and $x^2\partial_x$ on $\mathbb{R}$ satisfy $[\partial_x, x\partial_x] = \partial_x$, $[\partial_x, x^2\partial_x] = 2x\partial_x$, $[x\partial_x, x^2\partial_x] = x^2\partial_x$, so they span a three-dimensional Lie subalgebra of $\mathfrak{X}(\mathbb{R})$ isomorphic to $\mathfrak{sl}(2; \mathbb{R})$ — and one knows it is a Lie algebra the instant one recognises them as vector fields.

The second disguised source is **left-invariant data on a Lie group, or more generally a subspace of $\mathfrak{X}(M)$ preserved by the bracket**. Property $B$: a linear subspace $\mathfrak{h} \subseteq \mathfrak{X}(M)$ with $[\mathfrak{h}, \mathfrak{h}] \subseteq \mathfrak{h}$. The bridge is that a bracket-closed subspace of a Lie algebra is a Lie subalgebra, inheriting bilinearity, antisymmetry, and Jacobi verbatim; the naturality clause (ii) is what proves such subspaces are closed in the first place (left-invariant fields are exactly the fields fixed by every $(L_g)_*$, and (ii) shows the bracket of two of them is again fixed). *Example problem:* show that the left-invariant vector fields on a Lie group form a finite-dimensional Lie algebra — precisely the route [[Thm - Left-Invariant Vector Fields Form a Lie Algebra|the Lie algebra of a Lie group]] takes, using clause (ii) with $F = L_g$.

The third disguised source is **an infinitesimal symmetry, that is, the generator of a one-parameter family of diffeomorphisms**. Property $B$: one is given a flow $\phi_t$ (a one-parameter group of diffeomorphisms) and its generating field $X = \frac{d}{dt}\big|_{0}\phi_t$; a second symmetry gives $Y$. The bridge is that the bracket $[X, Y]$ measures the infinitesimal failure of the two symmetries to commute, and by naturality (ii) the bracket of the generators generates the commutator flow; so questions about whether two symmetries commute become bracket computations governed by this theorem. *Example problem:* the fundamental vector fields of a smooth group action are generators of the one-parameter subgroups' flows, and [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions|the fundamental-vector-field map]] uses exactly clauses (i) and (ii) to turn the group's bracket into their bracket.

**Targets (Output Amplification)**

The bare conclusion is that $\mathfrak{X}(M)$ is a Lie algebra and the bracket is diffeomorphism-natural. Combined with extra structure it yields the load-bearing results of the theory.

Combine clause (i) with **left-invariance on a Lie group $G$**. The subspace $\mathfrak{g} \subseteq \mathfrak{X}(G)$ of left-invariant fields is closed under the bracket (by clause (ii) applied to $F = L_g$), and it is linearly isomorphic to $T_eG$, hence finite-dimensional of dimension $\dim G$. The amplified result $E$ is that every Lie group carries a finite-dimensional Lie algebra, the object that linearises it; this is the starting point of all of Lie theory and is developed on [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]].

Combine clause (i) and clause (ii) with **a smooth action of $G$ on a manifold $M$**. Pushing the left-invariant fields forward along the orbit maps produces the fundamental vector fields $\xi \mapsto \xi_M$, and naturality forces this map to respect brackets (up to the sign fixed by left versus right actions). The amplified result $E$ is the fundamental-vector-field homomorphism $\mathfrak{g} \to \mathfrak{X}(M)$, the infinitesimal form of the action and the engine of the structure equation in gauge theory; see [[Def - Fundamental Vector Field of a Group Action]] and [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]].

Combine clause (i) with **a rank-$k$ distribution $D \subseteq TM$ whose sections are closed under the bracket**. The Jacobi identity is not what does the work here, but the fact that the bracket lands back in $\mathfrak{X}(M)$ and is $C^\infty$-antisymmetric is: the Frobenius theorem says a distribution is integrable — tangent to a foliation — if and only if its sections are bracket-closed. The amplified result $E$ is the integrability criterion that converts an algebraic condition ($[D, D] \subseteq D$) into a geometric conclusion (through every point passes an integral submanifold), and it is the mechanism behind flat connections and horizontal foliations later in the series.

---

# Why Is It True

Strip away the formalism and ask what could possibly go wrong. We want to multiply two vector fields. The obvious attempt, "compose them as operators", $f \mapsto X(Yf)$, fails for one concrete reason: composing two first-order operators produces a *second-order* operator. Written in a chart, $X(Yf)$ contains a term $X^i Y^j \partial_i\partial_j f$ carrying second derivatives of $f$, and an operator that reaches the second derivative of a function is not a vector field — vector fields differentiate once.

The whole theorem turns on a single observation: **the second-order part of $XY$ is symmetric in $X$ and $Y$, because mixed partial derivatives commute, so it is annihilated exactly by the antisymmetric combination $XY - YX$.** The term $X^i Y^j \partial_i\partial_j f$ in $X(Yf)$ is matched by the term $Y^i X^j \partial_i\partial_j f$ in $Y(Xf)$; relabelling the summation indices and using $\partial_i\partial_j f = \partial_j\partial_i f$ shows these are the same function, so they cancel in the difference. What survives is first-order — a genuine vector field, with the coordinate formula $[X, Y]^j = X(Y^j) - Y(X^j)$. This is why the bracket is antisymmetric *by necessity* rather than by choice: the symmetric combination $XY + YX$ keeps its second-order part and is not a vector field at all. Antisymmetry is forced by the demand that the output be a vector field.

Once the bracket is known to be the operator commutator $XY - YX$, the remaining two axioms are pure algebra of associative operators. Bilinearity is the bilinearity of composition. The Jacobi identity is the statement that the cyclic sum of double commutators of any three associative operators vanishes — a mechanical cancellation of twelve triple products, valid for matrices, for bounded operators, for any associative algebra at all. In this sense the Jacobi identity is, as Bär's Remark 1.2.1 puts it, "a replacement for associativity": it is precisely what associativity of composition leaves behind after one antisymmetrises.

Naturality is the last piece and it is a statement about how vector fields act on functions. A vector field is determined by how it differentiates functions; a diffeomorphism transports functions by pullback; and the differential is *defined* so that a transported field differentiates a function exactly as the original field differentiates its pullback. Chaining this twice — once for $X$, once for $Y$ — makes the bracket transport correctly, because the bracket is built out of nothing but the two actions on functions. **A diffeomorphism relabels the manifold, and the bracket, being defined through the action on functions, relabels with it.**

---

# What Makes This Hard

The single non-obvious step is the cancellation of the second-order terms, and the common error is to overlook that it *needs* the equality of mixed partial derivatives: without $\partial_i\partial_j f = \partial_j\partial_i f$ (which holds because $f$ is $C^2$, and here $C^\infty$), the two second-order sums would not match and $[X, Y]$ would not be first-order. A second, subtler trap in the naturality proof is to confuse the two things a vector field can be pushed along: one must apply the defining relation $(dF_p v)(f) = v(f \circ F)$ in the correct direction and to the correct test function ($Y'f$ on the target, pulled back to $M$), and it is easy to write down a formula that is off by a pullback. The Jacobi computation is long but not deep; the error there is bookkeeping, losing one of the twelve triple-product terms.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** First establish that the bracket is a smooth vector field by computing $X(Yf) - Y(Xf)$ in an arbitrary chart and watching the second-order terms cancel; this simultaneously delivers the coordinate formula and the fact that the bracket equals the operator commutator $XY - YX$. With that identification, bilinearity and antisymmetry are one-line consequences of the algebra of operators, and the Jacobi identity is the vanishing of a cyclic sum of twelve triple compositions. Finally, prove naturality by characterising $F$-relatedness through the action on pulled-back functions and applying that characterisation twice inside the bracket.

**Subgoal decomposition:**

1. **The bracket is a smooth vector field.**
   - *Hint:* In a chart, expand $X(Yf)$ and $Y(Xf)$ by the product rule; the second-order terms are $X^iY^j\partial_i\partial_j f$ and $Y^iX^j\partial_i\partial_j f$, equal after relabelling and Schwarz, so they cancel, leaving $(X(Y^j) - Y(X^j))\partial_j f$.
   - *Why needed:* Until the bracket is known to land back in $\mathfrak{X}(M)$, "Lie algebra structure on $\mathfrak{X}(M)$" is not even a well-posed claim.

2. **Bilinearity and antisymmetry.**
   - *Hint:* Both follow from $[X, Y] = XY - YX$ as operators: composition is $\mathbb{R}$-bilinear, and swapping $X, Y$ negates the commutator.
   - *Why needed:* These are two of the three Lie algebra axioms; antisymmetry is also what makes the second-slot linearity follow from the first.

3. **The Jacobi identity.**
   - *Hint:* Write each double bracket as a commutator of operators, expand into triple compositions $XYZ, XZY, \dots$, and check that the cyclic sum cancels term by term.
   - *Why needed:* It is the third and only non-formal Lie algebra axiom, and the one that makes the structure genuinely a Lie algebra rather than a mere antisymmetric algebra.

4. **The $F$-related bracket lemma.**
   - *Hint:* Prove $X \sim_F X'$ iff $X(f \circ F) = (X'f) \circ F$ for all $f$, using the defining relation $(\ast)$ of the differential; then compute $[X, Y](f \circ F)$ using this twice to get $([X', Y']f) \circ F$.
   - *Why needed:* It is the general functoriality of the bracket, from which the diffeomorphism naturality clause (ii) drops out by the uniqueness of the $F$-related field for a diffeomorphism.

5. **Naturality under diffeomorphisms.**
   - *Hint:* $F_*X \sim_F X$ and $F_*Y \sim_F Y$ by definition of pushforward; the lemma gives $[X, Y] \sim_F [F_*X, F_*Y]$; but also $[X, Y] \sim_F F_*[X, Y]$; uniqueness forces equality.
   - *Why needed:* It is clause (ii), and it upgrades $F_*$ to a Lie algebra isomorphism.

---

# Lemma Decomposition

> [!note]- Lemma 1: The bracket is a smooth vector field, with coordinate formula
> **Statement:** For $X, Y \in \mathfrak{X}(M)$, the operator $[X, Y] = XY - YX$ on $C^\infty(M)$ is a smooth vector field. In any chart $(U, (x^i))$ with $X = X^i\partial_i$, $Y = Y^j\partial_j$, it is
> $$[X, Y]\big|_U = \big(X(Y^j) - Y(X^j)\big)\,\partial_j, \qquad \text{i.e.} \qquad [X, Y]^j = X^i\frac{\partial Y^j}{\partial x^i} - Y^i\frac{\partial X^j}{\partial x^i}.$$
>
> **Hint:** Expand $X(Yf)$ and $Y(Xf)$ by the product rule and cancel the second-order terms using the equality of mixed partials.
>
> **Why needed:** It certifies that the bracket takes values in $\mathfrak{X}(M)$, so that clause (i) is a well-posed statement, and it identifies the bracket with the operator commutator, which is what makes Lemmas 2 and 3 pure operator algebra.
>
> > [!note]- Full proof
> > Fix $f \in C^\infty(M)$ and a chart $(U, (x^i))$, and write $X = X^i\partial_i$, $Y = Y^j\partial_j$ with $X^i, Y^j \in C^\infty(U)$. Since $Yf = Y^j\,\partial_j f$, the product rule for the derivation $X^i\partial_i$ gives
> > $$X(Yf) = X^i\,\partial_i\!\big(Y^j\,\partial_j f\big) = X^i\,(\partial_i Y^j)\,(\partial_j f) + X^i Y^j\,\partial_i\partial_j f \qquad \text{(product rule } \partial_i(gh) = (\partial_i g)h + g\,\partial_i h\text{).}$$
> > Interchanging the roles of $X$ and $Y$ (a legitimate relabelling, as both are smooth fields on $U$) gives, by the identical computation,
> > $$Y(Xf) = Y^i\,(\partial_i X^j)\,(\partial_j f) + Y^i X^j\,\partial_i\partial_j f.$$
> > **Cancellation of the second-order part.** Subtract the two displays. The second-order terms are $X^i Y^j\,\partial_i\partial_j f$ and $Y^i X^j\,\partial_i\partial_j f$. In the second, relabel the summation indices $i \leftrightarrow j$ (both are summed over $1, \dots, n$, so the sum is unchanged), obtaining $Y^j X^i\,\partial_j\partial_i f$; and $\partial_j\partial_i f = \partial_i\partial_j f$ because $f$ is smooth, hence $C^2$, so mixed partials commute (Schwarz's theorem, whose hypothesis — continuity of the second partials — holds as $f \in C^\infty$). Therefore $Y^i X^j\,\partial_i\partial_j f = X^i Y^j\,\partial_i\partial_j f$, and the two second-order sums are equal and cancel in the difference. What remains is
> > $$[X, Y]f = X(Yf) - Y(Xf) = \big(X^i\,\partial_i Y^j - Y^i\,\partial_i X^j\big)\,\partial_j f = \big(X(Y^j) - Y(X^j)\big)\,\partial_j f, \qquad \text{(the second-order terms cancelled).}$$
> > **This is a smooth vector field.** The coefficient functions $c^j := X(Y^j) - Y(X^j) = X^i\,\partial_i Y^j - Y^i\,\partial_i X^j$ are smooth on $U$, being sums of products of the smooth functions $X^i, Y^j$ and their smooth partial derivatives. Hence on $U$ the operator $[X, Y]$ acts as $c^j\partial_j$, which is the smooth vector field with components $c^j$ in the chart. The operator $[X, Y] = XY - YX$ is defined on $C^\infty(M)$ without reference to any chart, so its restriction to each chart domain is chart-independent as a value; the local expressions $c^j\partial_j$ therefore agree on overlaps and patch to a single globally defined smooth vector field, which we call $[X, Y] \in \mathfrak{X}(M)$. (Independently, the Leibniz rule holds directly: for $f, g \in C^\infty(M)$, expanding $XY(fg)$ and $YX(fg)$ by the product rule twice, the cross terms $Xf\,Yg + Xg\,Yf$ appear symmetrically in both and cancel in the difference, leaving $[X, Y](fg) = f\,[X, Y]g + g\,[X, Y]f$; so $[X, Y]$ is a derivation of $C^\infty(M)$, which is the coordinate-free way to see it is a vector field.) $\qquad\blacksquare$

> [!note]- Lemma 2: The bracket is $\mathbb{R}$-bilinear and antisymmetric
> **Statement:** For all $X, X_1, X_2, Y \in \mathfrak{X}(M)$ and $a, b \in \mathbb{R}$,
> $$[aX_1 + bX_2,\, Y] = a[X_1, Y] + b[X_2, Y], \qquad [X, Y] = -[Y, X].$$
> Bilinearity in the second slot follows from these two.
>
> **Hint:** Use $[X, Y] = XY - YX$ and the $\mathbb{R}$-bilinearity of operator composition.
>
> **Why needed:** These are the first two Lie algebra axioms; antisymmetry is also what reduces second-slot linearity to first-slot linearity.
>
> > [!note]- Full proof
> > By Lemma 1, $[X, Y] = XY - YX$ as operators on $C^\infty(M)$, where juxtaposition is composition. **Antisymmetry.** For every $f \in C^\infty(M)$,
> > $$[X, Y]f = X(Yf) - Y(Xf) = -\big(Y(Xf) - X(Yf)\big) = -[Y, X]f \qquad \text{(regrouping the two terms with an overall sign).}$$
> > As this holds for all $f$, the fields agree: $[X, Y] = -[Y, X]$. In particular $[X, X] = -[X, X]$, so $[X, X] = 0$. **Linearity in the first slot.** Composition of operators is $\mathbb{R}$-linear in each argument, and the operator attached to $aX_1 + bX_2$ is $a\,X_1 + b\,X_2$ (the action of vector fields on functions is $\mathbb{R}$-linear in the field). Hence for $f \in C^\infty(M)$,
> > $$[aX_1 + bX_2,\, Y]f = (aX_1 + bX_2)(Yf) - Y\big((aX_1 + bX_2)f\big) \qquad \text{(definition of the bracket)}$$
> > $$= a\,X_1(Yf) + b\,X_2(Yf) - a\,Y(X_1 f) - b\,Y(X_2 f) \qquad \text{($\mathbb{R}$-linearity of the operators } X_1, X_2, Y\text{)}$$
> > $$= a\big(X_1(Yf) - Y(X_1 f)\big) + b\big(X_2(Yf) - Y(X_2 f)\big) = a\,[X_1, Y]f + b\,[X_2, Y]f \qquad \text{(regrouping).}$$
> > **Linearity in the second slot.** By antisymmetry, $[X,\, aY_1 + bY_2] = -[aY_1 + bY_2,\, X] = -a[Y_1, X] - b[Y_2, X] = a[X, Y_1] + b[X, Y_2]$, using first-slot linearity and then antisymmetry again. Therefore the bracket is $\mathbb{R}$-bilinear and antisymmetric. $\qquad\blacksquare$

> [!note]- Lemma 3: The Jacobi identity
> **Statement:** For all $X, Y, Z \in \mathfrak{X}(M)$,
> $$\big[[X, Y], Z\big] + \big[[Y, Z], X\big] + \big[[Z, X], Y\big] = 0.$$
>
> **Hint:** Write every bracket as an operator commutator and expand into the eight triple compositions of each double bracket; the twelve resulting triple products cancel in pairs.
>
> **Why needed:** It is the third Lie algebra axiom and the one that gives the structure its name.
>
> > [!note]- Full proof
> > By Lemma 1, each bracket of vector fields is the operator commutator, and $[X, Y]$ is itself a vector field, so $\big[[X, Y], Z\big]$ is again an operator commutator: $\big[[X, Y], Z\big] = [X, Y]Z - Z[X, Y]$, where all products are compositions of operators on $C^\infty(M)$. **Expand the first double bracket.** Using $[X, Y] = XY - YX$,
> > $$\big[[X, Y], Z\big] = (XY - YX)Z - Z(XY - YX) = XYZ - YXZ - ZXY + ZYX \qquad \text{(distribute composition over the differences).}$$
> > **Expand the other two by cyclic rotation $X \to Y \to Z \to X$.** The same computation with $(X, Y, Z)$ replaced by $(Y, Z, X)$ and by $(Z, X, Y)$ gives
> > $$\big[[Y, Z], X\big] = YZX - ZYX - XYZ + XZY, \qquad \big[[Z, X], Y\big] = ZXY - XZY - YZX + YXZ.$$
> > **Add the three lines.** Collect the twelve triple products by type; each appears exactly twice, once with each sign:
> > $$
> > \begin{aligned}
> > XYZ:\ &+1\ (\text{line 1}) - 1\ (\text{line 2}) = 0, & YXZ:\ &-1\ (\text{line 1}) + 1\ (\text{line 3}) = 0,\\
> > ZXY:\ &-1\ (\text{line 1}) + 1\ (\text{line 3}) = 0, & ZYX:\ &+1\ (\text{line 1}) - 1\ (\text{line 2}) = 0,\\
> > YZX:\ &+1\ (\text{line 2}) - 1\ (\text{line 3}) = 0, & XZY:\ &+1\ (\text{line 2}) - 1\ (\text{line 3}) = 0.
> > \end{aligned}
> > $$
> > Every triple product cancels, so the sum of the three double brackets is the zero operator, and hence the zero vector field. (The computation uses only that composition of operators is associative and distributes over addition; this is the sense in which the Jacobi identity is the residue of associativity after antisymmetrisation — Bär's Remark 1.2.1.) $\qquad\blacksquare$

> [!note]- Lemma 4: Naturality of the bracket under $F$-relatedness
> **Statement:** Let $F : M \to N$ be smooth. Then for $X \in \mathfrak{X}(M)$ and $X' \in \mathfrak{X}(N)$,
> $$X \sim_F X' \iff X(f \circ F) = (X'f) \circ F \ \text{ for every } f \in C^\infty(N).$$
> Consequently, if $X \sim_F X'$, $Y \sim_F Y'$ with $X, Y \in \mathfrak{X}(M)$ and $X', Y' \in \mathfrak{X}(N)$, then
> $$[X, Y] \sim_F [X', Y'].$$
>
> **Hint:** The equivalence is the defining relation $(\ast)$ of the differential, read pointwise. For the bracket, act on $f \in C^\infty(N)$ and apply the equivalence twice.
>
> **Why needed:** It is the general functoriality of the bracket; the diffeomorphism naturality clause (ii) follows from it and the uniqueness of the pushforward.
>
> > [!note]- Full proof
> > **The equivalence.** Fix $f \in C^\infty(N)$ and $p \in M$, and write $q = F(p)$. By the defining relation $(\ast)$ of the differential, $dF_p(X_p)$ acts on $f$ by $dF_p(X_p)f = X_p(f \circ F) = (X(f \circ F))(p)$. On the other hand, if $X' \in \mathfrak{X}(N)$ then $X'_q f = (X'f)(q) = ((X'f) \circ F)(p)$. Now $X \sim_F X'$ means $dF_p(X_p) = X'_{q}$ as tangent vectors at $q$ for every $p$; two tangent vectors at $q$ are equal precisely when they agree as derivations on every $f \in C^\infty(N)$. Comparing the two computations, this holds for all $p$ and all $f$ if and only if $X(f \circ F) = (X'f) \circ F$ for every $f \in C^\infty(N)$. This proves the equivalence in both directions.
> >
> > **The bracket is preserved.** Assume $X \sim_F X'$ and $Y \sim_F Y'$. Let $f \in C^\infty(N)$. Then
> > $$[X, Y](f \circ F) = X\big(Y(f \circ F)\big) - Y\big(X(f \circ F)\big) \qquad \text{(definition of the bracket on } M\text{)}$$
> > $$= X\big((Y'f) \circ F\big) - Y\big((X'f) \circ F\big) \qquad \text{(equivalence applied to } Y \sim_F Y' \text{ with test } f\text{, and to } X \sim_F X' \text{ with test } f\text{)}$$
> > $$= \big(X'(Y'f)\big) \circ F - \big(Y'(X'f)\big) \circ F \qquad \text{(equivalence applied to } X \sim_F X' \text{ with test } Y'f \in C^\infty(N)\text{, and to } Y \sim_F Y' \text{ with test } X'f\text{)}$$
> > $$= \big(X'(Y'f) - Y'(X'f)\big) \circ F = \big([X', Y']f\big) \circ F \qquad \text{(definition of the bracket on } N\text{).}$$
> > Since this holds for every $f \in C^\infty(N)$, the equivalence (used now in the reverse direction, with the fields $[X, Y]$ on $M$ and $[X', Y']$ on $N$) gives $[X, Y] \sim_F [X', Y']$. Both applications require only that $Y'f, X'f \in C^\infty(N)$, which holds because $X', Y'$ are smooth fields and $f$ is smooth. $\qquad\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be a smooth manifold and $X, Y, Z \in \mathfrak{X}(M)$.
>
> **Part I — $(\mathfrak{X}(M), [\cdot, \cdot])$ is a Lie algebra over $\mathbb{R}$.**
>
> **Step 0 — the bracket is a smooth vector field.** By Lemma 1, the operator $[X, Y] = XY - YX$ on $C^\infty(M)$ is a smooth vector field on $M$, with local expression $[X, Y]^j = X(Y^j) - Y(X^j)$ in any chart. Hence $[\cdot, \cdot] : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ is a well-defined map into $\mathfrak{X}(M)$, and the statement "Lie algebra structure on $\mathfrak{X}(M)$" is well-posed. The set $\mathfrak{X}(M)$ is a real vector space under pointwise addition and scalar multiplication (this is part of [[Def - Smooth Vector Field|the definition of $\mathfrak{X}(M)$]]).
>
> **Step 1 — bilinearity.** By Lemma 2, $[\cdot, \cdot]$ is $\mathbb{R}$-linear in each of its two arguments.
>
> **Step 2 — antisymmetry.** By Lemma 2, $[X, Y] = -[Y, X]$ for all $X, Y$ (the corrected form of Bär's axiom (ii); see the Notation convention callout).
>
> **Step 3 — Jacobi identity.** By Lemma 3, $\big[[X, Y], Z\big] + \big[[Y, Z], X\big] + \big[[Z, X], Y\big] = 0$.
>
> **Step 4 — conclusion of Part I.** A real vector space equipped with an $\mathbb{R}$-bilinear, antisymmetric map satisfying the Jacobi identity is by definition a [[Def - Lie Algebra|Lie algebra]] over $\mathbb{R}$ (Bär Definition 1.2.1, corrected). Steps 0–3 verify exactly these axioms, so $(\mathfrak{X}(M), [\cdot, \cdot])$ is a Lie algebra over $\mathbb{R}$.
>
> **Step 5 — infinite-dimensionality when $\dim M \geq 1$.** Choose a chart $(U, (x^1, \dots, x^n))$ with $n = \dim M \geq 1$ and a bump function $\chi \in C^\infty(M)$ with $\chi \equiv 1$ on a smaller neighbourhood $V \Subset U$ and $\operatorname{supp}\chi \subset U$ (such $\chi$ exists by [[Thm - Existence of Smooth Partitions of Unity|the existence of bump functions]]). For $k = 0, 1, 2, \dots$ the fields $\chi\,(x^1)^k\,\partial_1$ (extended by zero outside $U$) are smooth vector fields on $M$. If a finite $\mathbb{R}$-linear combination $\sum_{k=0}^{m} a_k\,\chi\,(x^1)^k\,\partial_1$ vanishes, then on $V$ (where $\chi \equiv 1$) the polynomial $\sum_{k=0}^m a_k (x^1)^k$ vanishes identically in $x^1$, forcing every $a_k = 0$. Thus $\{\chi\,(x^1)^k\,\partial_1\}_{k \geq 0}$ is an infinite $\mathbb{R}$-linearly independent family, and $\mathfrak{X}(M)$ is infinite-dimensional. (This realises the parenthetical claim of Bär's Example 1.2.2.4.)
>
> **Part II — naturality under a diffeomorphism $F : M \to N$.**
>
> Let $F : M \to N$ be a diffeomorphism and $X, Y \in \mathfrak{X}(M)$.
>
> **Step 6 — the pushforwards are $F$-related to $X$ and $Y$.** By [[Thm - Pushforward of Vector Fields under a Diffeomorphism|the pushforward theorem]] — for a diffeomorphism $F$, the field $F_*X \in \mathfrak{X}(N)$ defined by $(F_*X)_q = dF_{F^{-1}(q)}(X_{F^{-1}(q)})$ is the *unique* vector field on $N$ that is $F$-related to $X$ — we have $X \sim_F F_*X$ and $Y \sim_F F_*Y$.
>
> **Step 7 — bracket of pushforwards is $F$-related to bracket.** By Lemma 4 (naturality of the bracket under $F$-relatedness), $X \sim_F F_*X$ and $Y \sim_F F_*Y$ give
> $$[X, Y] \sim_F [F_*X, F_*Y].$$
>
> **Step 8 — pushforward of the bracket is $F$-related to the same bracket.** Applying Step 6 to the field $[X, Y] \in \mathfrak{X}(M)$ (legitimate, as $[X, Y]$ is a smooth vector field by Step 0), the pushforward $F_*[X, Y]$ is the unique field on $N$ that is $F$-related to $[X, Y]$; in particular
> $$[X, Y] \sim_F F_*[X, Y].$$
>
> **Step 9 — uniqueness forces equality.** By Step 6's uniqueness clause (for the diffeomorphism $F$ there is exactly one vector field on $N$ that is $F$-related to the given field $[X, Y]$), the two fields $[F_*X, F_*Y]$ and $F_*[X, Y]$ — both $F$-related to $[X, Y]$ by Steps 7 and 8 — coincide:
> $$F_*[X, Y] = [F_*X, F_*Y].$$
>
> **Step 10 — $F_*$ is a Lie algebra isomorphism.** The map $F_* : \mathfrak{X}(M) \to \mathfrak{X}(N)$ is $\mathbb{R}$-linear (its pointwise formula is $dF_{F^{-1}(q)}$ applied to $X_{F^{-1}(q)}$, and $dF$ is linear on each tangent space) and, by Step 9, preserves the bracket, so it is a Lie algebra homomorphism. Since $F$ is a diffeomorphism, $F^{-1} : N \to M$ is one too, and $(F^{-1})_*$ is a Lie algebra homomorphism by the same argument; composing the defining $F$-relations gives $(F^{-1})_* \circ F_* = \mathrm{id}_{\mathfrak{X}(M)}$ and $F_* \circ (F^{-1})_* = \mathrm{id}_{\mathfrak{X}(N)}$. Hence $F_*$ is a Lie algebra isomorphism with inverse $(F^{-1})_*$.
>
> **Conclusion.** Part I shows $(\mathfrak{X}(M), [\cdot, \cdot])$ is a Lie algebra over $\mathbb{R}$, infinite-dimensional when $\dim M \geq 1$; Part II shows every diffeomorphism $F : M \to N$ induces a Lie algebra isomorphism $F_*$ with $F_*[X, Y] = [F_*X, F_*Y]$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Witt algebra of vector fields on the circle.** On $S^1$ with angular coordinate $\theta$, consider the fields $L_n := e^{in\theta}\,\partial_\theta$ for $n \in \mathbb{Z}$ (as real fields, work with $\cos(n\theta)\partial_\theta$ and $\sin(n\theta)\partial_\theta$). A direct application of the coordinate formula from Lemma 1 gives $[L_m, L_n] = i(n - m)L_{m+n}$, so these fields close into an infinite-dimensional Lie algebra — the Witt algebra. This is non-obvious as an application because the answer, a clean structure constant $i(n-m)$, emerges only after one trusts that the bracket is a genuine vector field (Lemma 1) and computes; the theorem guarantees the Jacobi identity holds without a separate check, which would otherwise be a substantial computation. The Witt algebra and its central extension, the Virasoro algebra, are the symmetry algebras of two-dimensional conformal field theory.

**Killing fields on a Riemannian manifold.** The vector fields whose flows are isometries of a Riemannian metric $g$ — the Killing fields — form a subspace of $\mathfrak{X}(M)$. One shows the bracket of two Killing fields is again Killing, so they form a Lie subalgebra; the theorem supplies bilinearity, antisymmetry, and Jacobi for free, so only bracket-closure needs checking. The application is non-obvious because "isometry" is a metric condition while the bracket is purely differential-topological; the bridge is that Killing fields are infinitesimal isometries, and clause (ii)'s naturality (with $F$ an isometry) is what makes the subspace bracket-closed.

**Commuting flows in a dynamical system.** Given two complete vector fields $X, Y$ on a manifold whose flows model two conserved evolutions, the flows commute if and only if $[X, Y] = 0$. Using Lemma 1 to compute the bracket in coordinates turns the geometric question "do these two evolutions commute?" into an algebraic one. This is non-obvious because commuting *flows* is a statement about the global time-$t$ maps, whereas the bracket is an infinitesimal, first-order quantity; the equivalence (proved on [[Thm - Commuting Flows Theorem|the commuting flows theorem]]) is exactly what makes the infinitesimal Lie algebra structure control the global dynamics.

---

# Bridges

- **The Lie algebra of a Lie group.** Specialise $M$ to a Lie group $G$ and restrict the bracket to the subspace $\mathfrak{g} \subseteq \mathfrak{X}(G)$ of [[Def - Left-Invariant Vector Field|left-invariant fields]]. Naturality (clause (ii)) applied to $F = L_g$ shows $[X, Y]$ is again left-invariant whenever $X, Y$ are, so $\mathfrak{g}$ is a Lie subalgebra; the evaluation-at-the-identity map $\mathfrak{g} \to T_eG$ is a linear isomorphism, giving the finite-dimensional Lie algebra of $G$. This is developed in full on [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]], and it is the reason the abstract commutator on a matrix Lie algebra is a Lie bracket at all.

- **The fundamental-vector-field map of a group action.** For a smooth action of $G$ on $M$, each $\xi \in \mathfrak{g}$ generates a [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] $\xi_M \in \mathfrak{X}(M)$, obtained by pushing the left-invariant field forward along an orbit map. Because orbit maps intertwine the fields, Lemma 4's $F$-related bracket identity forces $\xi \mapsto \xi_M$ to respect brackets (with a sign determined by whether the action is on the left or the right), giving the Lie algebra homomorphism $\mathfrak{g} \to \mathfrak{X}(M)$ proved on [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]. This map is the infinitesimal action that underlies the structure equation of a principal connection.

- **The Frobenius integrability theorem.** A smooth distribution $D \subseteq TM$ — a rank-$k$ subbundle — is tangent to a foliation exactly when its space of sections is closed under the bracket, $[\Gamma(D), \Gamma(D)] \subseteq \Gamma(D)$. The bracket entering this criterion is the one this theorem constructs; that it lands in $\mathfrak{X}(M)$ (Lemma 1) is what makes the condition meaningful, and antisymmetry is what makes it a condition on the $C^\infty$-module $\Gamma(D)$ rather than on individual fields. Flat connections and horizontal foliations in the later chapters are instances.

- **The commutator on an associative algebra.** For any associative algebra $A$ over $\mathbb{R}$, the commutator $[a, b] = ab - ba$ makes $A$ a Lie algebra, by exactly the Lemma 2–Lemma 3 computations (they used only associativity and distributivity of composition). The bracket of vector fields is the case $A = \operatorname{Der}_\mathbb{R}(C^\infty(M))$, the derivations of the function ring under composition; the matrix commutator on $\operatorname{Mat}(n \times n; \mathbb{K})$ is the case $A = \operatorname{Mat}(n \times n; \mathbb{K})$, and its Jacobi identity (Bär Example 1.2.2.2, drilled in [[Ex - The Jacobi Identity for the Matrix Commutator Follows from Associativity]]) is the same cancellation.

---

# Unlocked by This

> [!tip] The Lie algebra of a Lie group *(from Lie theory)*
> Restricting the vector-field bracket to left-invariant fields on a Lie group produces the finite-dimensional Lie algebra $\mathfrak{g} = T_eG$ that linearises the group. Every classical matrix Lie algebra ($\mathfrak{gl}$, $\mathfrak{so}$, $\mathfrak{su}$, $\mathfrak{sp}$) arises this way, with the bracket becoming the matrix commutator. See [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]] and [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]].

> [!tip] The fundamental vector fields of a group action *(from gauge theory)*
> The bracket lets a $G$-action on a manifold be differentiated into a Lie algebra homomorphism $\mathfrak{g} \to \mathfrak{X}(M)$, the fundamental-vector-field map, whose image is the space of infinitesimal symmetries. This is the object that defines a principal connection through the condition $\omega(\xi_P) = \xi$. See [[Def - Fundamental Vector Field of a Group Action]].

> [!tip] The Lie bracket in coordinates *(from differential geometry)*
> Lemma 1's coordinate formula $[X, Y]^j = X^i\,\partial_i Y^j - Y^i\,\partial_i X^j$ is the everyday computational tool for brackets; the drill [[Ex - The Lie Bracket in Coordinates]] and the Jacobi-identity exercise [[Ex - The Jacobi Identity for Vector Fields]] rehearse it.
