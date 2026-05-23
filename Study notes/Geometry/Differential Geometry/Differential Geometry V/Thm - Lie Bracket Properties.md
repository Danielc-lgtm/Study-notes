---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Lie Derivative of a Vector Field"
  - "Def - F-Related Vector Fields"
tags: [geometry, differential-geometry]
---

# Notation

$M, N$ are smooth manifolds, $X, Y, Z \in \mathfrak{X}(M)$ smooth [[Def - Smooth Vector Field|vector fields]], $f, g \in C^\infty(M)$ smooth functions, $F : M \to N$ a smooth map. The Lie bracket is the operator $[\cdot, \cdot] : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ defined by $[X, Y]h = X(Yh) - Y(Xh)$ for $h \in C^\infty(M)$ — see [[Def - The Lie Bracket of Vector Fields]]. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Statement

> **Theorem (Properties of the Lie bracket).** For smooth vector fields $X, Y, Z \in \mathfrak{X}(M)$, smooth functions $f, g \in C^\infty(M)$, and a smooth map $F : M \to N$, the Lie bracket has the following properties:
>
> (a) **Bilinearity over $\mathbb{R}$.** For $a, b \in \mathbb{R}$,
> $$[aX + bY, Z] = a[X, Z] + b[Y, Z], \qquad [Z, aX + bY] = a[Z, X] + b[Z, Y].$$
>
> (b) **Antisymmetry.** $[X, Y] = -[Y, X]$.
>
> (c) **Jacobi identity.** $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$.
>
> (d) **Function product rule.** $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$.
>
> (e) **Coordinate formula.** In any smooth chart $(U, (x^i))$ with $X = X^i \partial_i$, $Y = Y^j \partial_j$,
> $$[X, Y] = \left(X^i \frac{\partial Y^j}{\partial x^i} - Y^i \frac{\partial X^j}{\partial x^i}\right) \partial_j.$$
>
> (f) **Naturality.** If $X \sim_F X'$ and $Y \sim_F Y'$, then $[X, Y] \sim_F [X', Y']$.
>
> (g) **Lie derivative identification.** $\mathcal{L}_X Y = [X, Y]$ for all $X, Y \in \mathfrak{X}(M)$.

In particular, $(\mathfrak{X}(M), [\cdot, \cdot])$ is a **Lie algebra over $\mathbb{R}$**: a real vector space with a bilinear antisymmetric bracket satisfying the Jacobi identity.

---

# Motivation

These are the **structural properties** of the Lie bracket that make it the central object of differential geometry. Each one is the precise statement of a different intuition about what the bracket should do, and together they characterize the bracket as the unique natural binary operation on $\mathfrak{X}(M)$ (up to scaling).

The roles:

(a) **Bilinearity** is a closure-and-compatibility statement: the bracket respects the vector-space structure of $\mathfrak{X}(M)$.

(b) **Antisymmetry** is forced by the commutator definition $[X, Y] = XY - YX$ — you cannot have a symmetric "commutator". It rules out positive-definite alternatives.

(c) **Jacobi identity** is the structural axiom of a Lie algebra. It is the precise statement that $\mathrm{ad}_X = [X, \cdot]$ is a derivation of the bracket, equivalently that the bracket admits a meaningful notion of "module of derivations". Without Jacobi, $\mathfrak{X}(M)$ would not be a Lie algebra.

(d) **Function product rule** is the most subtle of the algebraic identities. It encodes that the bracket is *not* $C^\infty(M)$-bilinear but instead has correction terms — this distinguishes the Lie bracket from a naive bilinear operation, and the correction is what makes the bracket "alive" rather than algebraically dead.

(e) **Coordinate formula** is the computational backbone: every concrete bracket calculation uses this. The cancellation of second derivatives in the calculation is non-trivial and is *the* reason the commutator $XY - YX$ produces a derivation rather than a second-order operator.

(f) **Naturality** says the bracket is functorial under smooth maps: a Lie algebra structure on $\mathfrak{X}(M)$ that transfers to $\mathfrak{X}(N)$ via any smooth map preserving the $F$-relatedness data. This is the categorical content of the Lie bracket and the reason every diffeomorphism produces a Lie algebra isomorphism.

(g) **Lie derivative identification** is the *geometric* identification of the bracket: $[X, Y]$ is the rate of change of $Y$ along the flow of $X$. This is what makes the bracket measurable, predictable, and useful for [[Thm - Commuting Flows Theorem|controlling flow commutators]].

The Lie derivative identification (g) deserves separate emphasis: it bridges the algebraic definition of the bracket (commutator of derivations) and the geometric definition of the Lie derivative (flow-pullback derivative). The two were defined separately to be operationally useful in different contexts — algebraic when computing, geometric when interpreting — but they coincide as a *theorem*, not an obvious identity. Lee Theorem 9.38 is the precise statement; the proof is a coordinate computation in straightened coordinates.

---

# Sources and Targets

**Sources (Input Broadening)**

The "precondition" of these properties is just "$X, Y, Z$ are smooth vector fields". The sources are the recognisable situations where you would invoke each property.

The first source is **a bracket appearing in a computation that you want to simplify**. The bilinearity (a), antisymmetry (b), and coordinate formula (e) are the basic computational tools. Trigger: any explicit bracket. Pattern: "rewrite using bilinearity to split off constants, use antisymmetry to put the more convenient field first, then apply the coordinate formula if needed".

The second source is **a Jacobi identity used to prove a structural result.** The Jacobi identity (c) is the engine of every "$\mathrm{ad}_X$ is a derivation" argument, of the existence of the **adjoint representation** of a Lie algebra, and of the construction of the **universal enveloping algebra**. Whenever a result has the shape "the bracket satisfies a non-obvious algebraic identity", the proof routes through Jacobi. Source: any algebra-of-derivations question.

The third source is **a function-product rule expression $[fX, gY]$.** The function product rule (d) is the only way to compute brackets involving functions times vector fields. Trigger: a bracket where at least one entry is multiplied by a smooth function. Pattern: expand $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$ to separate the "bilinear" part from the correction terms.

The fourth source is **a bracket on $M$ that you want to transfer to $N$.** The naturality (f) lets you push brackets through any smooth map (when the corresponding fields are $F$-related) or, in the diffeomorphism case, push them forward unambiguously. Trigger: you have a bracket computation on $M$ but it is easier on $N$. Pattern: find $F$-related fields, compute the bracket on the easier side, transfer the answer back.

The fifth source is **a question about flow invariance or rate of change along a flow.** The Lie derivative identification (g) is the bridge between algebraic and geometric statements. Trigger: a question of the form "is $Y$ invariant under the flow of $X$?" or "how does $Y$ change along the flow of $X$?" Pattern: compute $[X, Y]$; if zero, $Y$ is invariant; if nonzero, $[X, Y]$ is the rate.

**Targets (Output Amplification)**

The "conclusion" is a structural property of the bracket. Combined with one further property, each becomes a positive geometric result.

The first combination is **Jacobi + a Lie subalgebra structure gives the [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie algebra of a Lie group]].** Property $D$: a finite-dimensional subspace $\mathfrak{g} \subseteq \mathfrak{X}(M)$ closed under the bracket. Then $\mathfrak{g}$ is a finite-dimensional real Lie algebra, with all the structure theory available (Killing form, semi-simplicity, root systems). The first non-trivial case is left-invariant vector fields on a Lie group; the bracket-closure follows from naturality, giving the Lie algebra of the group.

The second combination is **naturality + a diffeomorphism gives a Lie algebra isomorphism.** Property $D$: $F : M \to N$ is a diffeomorphism. Then $F_* : \mathfrak{X}(M) \to \mathfrak{X}(N)$ is a Lie algebra isomorphism (combining the pushforward structure of [[Thm - Pushforward of Vector Fields under a Diffeomorphism]] with the naturality of the bracket). This is the reason "Lie algebra of vector fields" is a diffeomorphism invariant.

The third combination is **Lie derivative + the commuting flows theorem gives geometric commutator vanishing.** Property $D$: $[X, Y] = 0$. The amplification (via Lie derivative identification + [[Thm - Commuting Flows Theorem]]): the flows of $X$ and $Y$ commute, $\phi^X_s \circ \phi^Y_t = \phi^Y_t \circ \phi^X_s$. So a bracket calculation, via $\mathcal{L}_X Y = [X, Y]$, becomes a flow-commutation statement.

The fourth combination is **function product rule + a vector field of constant length gives angular vs radial decomposition.** Property $D$: $X$ is a unit vector field with respect to some metric (so $|X|^2 = 1$). The function product rule applied to $[f X, X]$ separates the bracket into the radial change of $f$ and the "transverse" component of $fX$. This is the geometric source of the **scalar curvature** decomposition in Riemannian geometry.

---

# Why Is It True

**The mechanism in one sentence: the algebraic identities follow from the commutator structure $[X, Y] = XY - YX$ on derivations, while the geometric identifications (naturality, Lie derivative) follow from the chart-by-chart agreement of "commutator of derivations" with "infinitesimal commutator of flows".**

Each property unpacks as follows:

**(a) Bilinearity** is the bilinearity of the commutator: $[aX + bY, Z] = (aX + bY)Z - Z(aX + bY) = a(XZ - ZX) + b(YZ - ZY) = a[X, Z] + b[Y, Z]$.

**(b) Antisymmetry** is built in: $[X, Y] = XY - YX = -(YX - XY) = -[Y, X]$.

**(c) Jacobi identity.** The proof is a cancellation calculation. Expand $[X, [Y, Z]] = X(YZ - ZY) - (YZ - ZY)X = XYZ - XZY - YZX + ZYX$. Sum the three cyclic terms; the twelve summands cancel in pairs (each $XYZ$, $YZX$, etc. appears once with each sign). This was the proof of part (c) of Lee Proposition 8.28.

**(d) Function product rule.** Compute $[fX, gY]h$ for $h \in C^\infty(M)$, expanding each $fX$ and $gY$ as derivations and applying the Leibniz rule. The cross-terms reorganize to $fg[X, Y]h + f(Xg)Yh - g(Yf)Xh$.

**(e) Coordinate formula.** In coordinates, write the commutator $XY - YX$ as a second-order operator $(X^i Y^j \partial_i \partial_j - Y^i X^j \partial_i \partial_j) + (X^i (\partial_i Y^j) \partial_j - Y^i (\partial_i X^j) \partial_j)$. The second-order part cancels by equality of mixed partials; what remains is the first-order part $(X^i \partial_i Y^j - Y^i \partial_i X^j) \partial_j$.

**(f) Naturality.** If $X \sim_F X'$ and $Y \sim_F Y'$, then $X(f \circ F) = (X'f) \circ F$ and similarly for $Y$, by the characterization in [[Def - F-Related Vector Fields]]. So $[X, Y](f \circ F) = XY(f \circ F) - YX(f \circ F) = X((Y'f) \circ F) - Y((X'f) \circ F) = (X'Y'f) \circ F - (Y'X'f) \circ F = ([X', Y']f) \circ F$, which is the characterization "$[X, Y] \sim_F [X', Y']$".

**(g) Lie derivative identification.** This is the deepest of the seven. The Lie derivative is defined geometrically by flow-pullback; the bracket is defined algebraically by the commutator. They agree, point by point. The cleanest proof (Lee 9.38) is to *straighten* the vector field $X$: at any regular point of $X$ choose coordinates so $X = \partial/\partial s^1$ (by [[Thm - Canonical Form for a Nonvanishing Vector Field]]). In these coordinates, the flow of $X$ is $\phi^X_t(s) = (s^1 + t, s^2, \dots, s^n)$, and the pullback of $Y_{\phi^X_t(p)} = Y^j(s^1 + t, \dots, s^n)\partial_j$ is again $Y^j(s^1 + t, \dots, s^n)\partial_j$ (since $\phi^X_{-t}$ has identity Jacobian). Differentiating in $t$ at $t = 0$ gives $\partial Y^j/\partial s^1 \cdot \partial_j = X^i \partial_i Y^j \partial_j$, which is the first-order part of the bracket formula (the second term $-Y^i \partial_i X^j$ vanishes since the components of $X$ are constants). For singular points of $X$, the identification follows by continuity from the regular points (since both sides depend continuously on $p$ and the singular set has empty interior unless $X$ is identically zero, in which case both sides are zero).

---

# What Makes This Hard

Where most people get stuck is **the Lie derivative identification $\mathcal{L}_X Y = [X, Y]$**: the two definitions look unrelated, and seeing why they agree requires straightening coordinates. The most common error is to try to prove the identification directly from the flow definition without coordinates — this leads to a tangled chain-rule calculation, where the cleaner route is to straighten $X$ first. A second subtle point is the function product rule (d): the correction terms $f(Xg)Y - g(Yf)X$ are easy to mis-sign or omit, and the precise statement is what makes the bracket "live" on the $C^\infty(M)$-module structure of $\mathfrak{X}(M)$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Bilinearity, antisymmetry, Jacobi, and the coordinate formula follow from the commutator structure $[X, Y] = XY - YX$ plus second-derivative cancellation. The function product rule is a direct computation expanding $[fX, gY]h$. Naturality follows from the $F$-related characterization $X(f \circ F) = (X' f) \circ F$, applied twice. The Lie derivative identification is proved by straightening $X$ at a regular point and computing the flow-pullback derivative in those coordinates; continuity handles singular points.

**Subgoal decomposition:**

1. **Bilinearity, antisymmetry, Jacobi.** Apply $[X, Y] = XY - YX$ and expand.
   - *Hint:* Each identity is a direct algebraic manipulation of commutators of operators.
   - *Why needed:* These are the Lie algebra axioms; without them $\mathfrak{X}(M)$ is not a Lie algebra.

2. **Function product rule.** Expand $[fX, gY]h$ using the derivation properties.
   - *Hint:* $[fX, gY]h = (fX)((gY)h) - (gY)((fX)h)$; apply the Leibniz rule (or just the smooth-function action) to each.
   - *Why needed:* This is the failure of $C^\infty(M)$-bilinearity; the correction terms are intrinsic to the bracket.

3. **Coordinate formula.** Expand $XY - YX$ in coordinates with $X = X^i \partial_i$, $Y = Y^j \partial_j$; second-derivative terms cancel.
   - *Hint:* Mixed partial derivatives commute for smooth functions, so $X^i Y^j \partial_i \partial_j - Y^i X^j \partial_i \partial_j$ cancels (after renaming dummy indices).
   - *Why needed:* This is the practical computational tool.

4. **Naturality.** Apply the $F$-related characterization $X(h \circ F) = (X'h) \circ F$ twice.
   - *Hint:* $[X, Y](h \circ F) = X(Y(h \circ F)) - Y(X(h \circ F))$; each inner term is $(Y'h) \circ F$ and $(X'h) \circ F$ respectively.
   - *Why needed:* Without naturality, the Lie bracket is not a functorial construction.

5. **Lie derivative identification.** Straighten $X$ at a regular point and compute in those coordinates.
   - *Hint:* In coordinates with $X = \partial/\partial s^1$, the flow is $\phi^X_t = (s^1 + t, s^2, \dots, s^n)$, the pullback of $Y$ is $Y^j(s^1 + t, \dots) \partial_j$, and the derivative at $t = 0$ is $X^i \partial_i Y^j \partial_j$ — matching the bracket since the components of $X$ are constants.
   - *Why needed:* This bridges the algebraic and geometric definitions of the bracket.

---

# Lemma Decomposition

> [!note]- Lemma 1: Bilinearity, antisymmetry, Jacobi
> **Statement:** The Lie bracket is $\mathbb{R}$-bilinear, antisymmetric, and satisfies the Jacobi identity.
>
> **Hint:** All three follow from $[X, Y] = XY - YX$. Bilinearity and antisymmetry are immediate; for Jacobi, expand all three nested commutators and observe that the twelve terms cancel in pairs.
>
> **Why needed:** Together these are the defining axioms of a Lie algebra; they make $\mathfrak{X}(M)$ a Lie algebra over $\mathbb{R}$.
>
> > [!note]- Full proof
> > *Bilinearity:* $[aX + bY, Z] = (aX + bY)Z - Z(aX + bY) = a(XZ - ZX) + b(YZ - ZY) = a[X, Z] + b[Y, Z]$. The other slot is symmetric.
> >
> > *Antisymmetry:* $[X, Y] = XY - YX = -(YX - XY) = -[Y, X]$.
> >
> > *Jacobi:* Expand $[X, [Y, Z]] = X(YZ - ZY) - (YZ - ZY)X = XYZ - XZY - YZX + ZYX$. Cyclically permuting $X \to Y \to Z \to X$:
> > - $[X, [Y, Z]] = XYZ - XZY - YZX + ZYX$
> > - $[Y, [Z, X]] = YZX - YXZ - ZXY + XZY$
> > - $[Z, [X, Y]] = ZXY - ZYX - XYZ + YXZ$
> >
> > Summing: each of the twelve products $XYZ, XZY, YXZ, YZX, ZXY, ZYX$ appears exactly twice with opposite signs, so everything cancels.

> [!note]- Lemma 2: Function product rule
> **Statement:** $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$ for $X, Y \in \mathfrak{X}(M)$ and $f, g \in C^\infty(M)$.
>
> **Hint:** Apply $[fX, gY]h = (fX)(gYh) - (gY)(fXh)$ and use the smooth-function action of vector fields on products.
>
> **Why needed:** Expresses the failure of $C^\infty(M)$-bilinearity of the bracket; the correction terms are essential.
>
> > [!note]- Full proof
> > For $h \in C^\infty(M)$,
> > $$(fX)(gYh) = f \cdot X(g Yh) = f \cdot \big((Xg)(Yh) + g \cdot X(Yh)\big) = f(Xg)(Yh) + fg X(Yh).$$
> > Similarly $(gY)(fXh) = g(Yf)(Xh) + gf Y(Xh)$. Subtracting:
> > $$[fX, gY]h = fg \big(X(Yh) - Y(Xh)\big) + f(Xg)(Yh) - g(Yf)(Xh) = fg [X, Y]h + f(Xg)Yh - g(Yf)Xh.$$
> > Since this holds for all $h$, $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$.

> [!note]- Lemma 3: Coordinate formula
> **Statement:** In a smooth chart $(U, (x^i))$ with $X = X^i \partial_i$, $Y = Y^j \partial_j$,
> $$[X, Y] = (X^i \partial_i Y^j - Y^i \partial_i X^j) \partial_j.$$
>
> **Hint:** Expand $XY - YX$ as a second-order operator and use equality of mixed partials.
>
> **Why needed:** Gives the explicit computational rule for brackets.
>
> > [!note]- Full proof
> > For $h \in C^\infty(U)$,
> > $$XYh = X^i \partial_i (Y^j \partial_j h) = X^i (\partial_i Y^j)(\partial_j h) + X^i Y^j \partial_i \partial_j h,$$
> > $$YXh = Y^i \partial_i (X^j \partial_j h) = Y^i (\partial_i X^j)(\partial_j h) + Y^i X^j \partial_i \partial_j h.$$
> >
> > Subtracting:
> > $$[X, Y]h = (X^i \partial_i Y^j - Y^i \partial_i X^j) \partial_j h + (X^i Y^j - Y^j X^i) \partial_i \partial_j h.$$
> >
> > The second term vanishes by equality of mixed partials: $\partial_i \partial_j h = \partial_j \partial_i h$ since $h$ is smooth, and swapping $i \leftrightarrow j$ in the second sum (just dummy indices) shows the second term is zero. So $[X, Y]h = (X^i \partial_i Y^j - Y^i \partial_i X^j) \partial_j h$, giving the formula.

> [!note]- Lemma 4: Naturality under smooth maps
> **Statement:** If $F : M \to N$ is smooth, $X \sim_F X'$ and $Y \sim_F Y'$, then $[X, Y] \sim_F [X', Y']$.
>
> **Hint:** Use the $F$-related characterization $X(h \circ F) = (X'h) \circ F$ and apply twice.
>
> **Why needed:** Without naturality, the Lie bracket is not a functorial construction; pushforward under diffeomorphisms would not be a Lie algebra homomorphism.
>
> > [!note]- Full proof
> > For $h \in C^\infty(N)$,
> > $$X(Y(h \circ F)) = X((Y'h) \circ F) = (X'(Y'h)) \circ F = (X'Y'h) \circ F,$$
> > using $X \sim_F X'$ on the outer step and $Y \sim_F Y'$ on the inner. Similarly $Y(X(h \circ F)) = (Y'X'h) \circ F$. Hence
> > $$[X, Y](h \circ F) = (X'Y'h - Y'X'h) \circ F = ([X', Y']h) \circ F,$$
> > which is the characterization of $[X, Y] \sim_F [X', Y']$.

> [!note]- Lemma 5: Lie derivative identification (Lee 9.38)
> **Statement:** $\mathcal{L}_X Y = [X, Y]$ for all $X, Y \in \mathfrak{X}(M)$.
>
> **Hint:** At a regular point of $X$ (where $X_p \neq 0$), use [[Thm - Canonical Form for a Nonvanishing Vector Field]] to choose coordinates with $X = \partial/\partial s^1$. In these coordinates, the flow of $X$ is translation in $s^1$, and the pullback derivative reduces to $\partial_1 Y^j$. At singular points (where $X_p = 0$), use the support criterion or continuity from regular points.
>
> **Why needed:** This is the geometric meaning of the bracket — the Lie derivative — and the bridge between algebraic and geometric definitions.
>
> > [!note]- Full proof
> > **Case 1: $p$ is a regular point of $X$.** Choose coordinates $(s^i)$ near $p$ with $X = \partial/\partial s^1$ ([[Thm - Canonical Form for a Nonvanishing Vector Field]]). In these coordinates the flow is $\phi^X_t(s^1, \dots, s^n) = (s^1 + t, s^2, \dots, s^n)$, and the Jacobian matrix of $\phi^X_t$ at every point is the identity. So for $Y = Y^j(s) \partial_j$,
> > $$d(\phi^X_{-t})_{\phi^X_t(s)}(Y_{\phi^X_t(s)}) = Y^j(s^1 + t, s^2, \dots, s^n) \partial_j\big|_s.$$
> > Differentiating in $t$ at $t = 0$:
> > $$(\mathcal{L}_X Y)_s = \frac{\partial Y^j}{\partial s^1}(s) \partial_j\big|_s.$$
> > On the other hand, by the coordinate formula for the bracket with $X^i = \delta^i_1$:
> > $$[X, Y]_s = (X^i \partial_i Y^j - Y^i \partial_i X^j) \partial_j = \partial_1 Y^j \partial_j - 0 = \frac{\partial Y^j}{\partial s^1} \partial_j.$$
> > The two match, so $(\mathcal{L}_X Y)_p = [X, Y]_p$ at every regular point $p$.
> >
> > **Case 2: $p \in \overline{\{q : X_q \neq 0\}}$ but not regular.** By continuity of both sides in $p$ (both depend smoothly on $p$ by Lemma 9.36 of Lee for $\mathcal{L}_X Y$ and by the smoothness of the bracket for $[X, Y]$), the identification extends from the regular points.
> >
> > **Case 3: $p$ has $X = 0$ in a neighbourhood.** Then $\phi^X_t = \mathrm{id}$ near $p$ for all $t$, so $d(\phi^X_{-t})_{\phi^X_t(p)}(Y_{\phi^X_t(p)}) = Y_p$ for all $t$, hence $\mathcal{L}_X Y = 0$ at $p$. On the other hand, the coordinate formula gives $[X, Y]_p = 0$ since both terms vanish. Equality holds.

---

# Formal Proof

> [!note]- Complete formal proof
> Lemmas 1–5 give the seven claims (a)–(g) of the theorem. Lemma 1 gives (a), (b), (c). Lemma 2 gives (d). Lemma 3 gives (e). Lemma 4 gives (f). Lemma 5 gives (g). Together they show that $(\mathfrak{X}(M), [\cdot, \cdot])$ is a real Lie algebra: the vector-space structure of $\mathfrak{X}(M)$ is from pointwise operations, and the bilinearity + antisymmetry + Jacobi identity from Lemma 1 are the Lie algebra axioms. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Lie algebra of a matrix Lie group.** The left-invariant vector fields on $\mathrm{GL}(n, \mathbb{R})$ form a finite-dimensional Lie subalgebra of $\mathfrak{X}(\mathrm{GL}(n))$, isomorphic to $\mathfrak{gl}(n)$ with the matrix commutator bracket. The naturality of the bracket (f) is what certifies that this subspace is closed under the bracket; the coordinate formula (e) at the identity reduces to the matrix commutator. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

**Jacobi identity for Poisson brackets.** On a symplectic manifold $(M, \omega)$, the Poisson bracket $\{f, g\} = \omega(X_f, X_g)$ satisfies its own Jacobi identity, which is *equivalent* to the closedness $d\omega = 0$ of the symplectic form. The vector-field Jacobi identity (c) is the prerequisite: $[X_f, X_g] = -X_{\{f, g\}}$, and Jacobi for vector fields gives Jacobi for $\{f, g\}$. See [[Differential Geometry VIII — Differential Forms]] forward.

**The bracket calculation in fluid dynamics.** In ideal fluid dynamics, the velocity field $v$ on a manifold $M$ satisfies the Euler equation $\partial_t v + [v, v] = -\nabla p$ (with $[v, v]$ interpreted in coordinates). The bracket is just the advective term $(v \cdot \nabla)v$, and the equation is the Newton's law on $\mathrm{Diff}(M)$ — a beautiful coincidence interpreted in Arnold's geometric mechanics.

**Vector fields under a covering map.** If $\pi : \tilde M \to M$ is a smooth covering map, every vector field $X$ on $M$ lifts uniquely to a vector field $\tilde X$ on $\tilde M$ with $\tilde X \sim_\pi X$, and the bracket lifts: $\widetilde{[X, Y]} = [\tilde X, \tilde Y]$. The naturality (f) is what guarantees this. This is the basic functoriality used in studying flows on universal covers.

---

# Bridges

- **[[Def - The Lie Bracket of Vector Fields|Lie bracket]]** — the object whose properties this theorem establishes. The bracket is defined as the commutator of derivations; this theorem upgrades that definition into the full Lie algebra structure with naturality and geometric meaning.

- **[[Def - Lie Derivative of a Vector Field|Lie derivative]]** — identified with the bracket by part (g). The Lie derivative is a geometric operation (rate of change along a flow); the bracket is an algebraic operation (commutator of derivations); they are the same. This identification is *the* bridge between the algebraic and geometric pictures of the bracket.

- **[[Thm - Commuting Flows Theorem]]** — uses naturality (f) and the Lie derivative identification (g). The proof that "$[X, Y] = 0$ iff flows commute" routes through: (a) $\mathcal{L}_X Y = [X, Y] = 0$ is "$Y$ is invariant under the flow of $X$"; (b) flow invariance gives commuting flows.

- **[[Thm - Pushforward of Vector Fields under a Diffeomorphism]]** — applies naturality (f) in the diffeomorphism case. When $F$ is a diffeomorphism, the pushforward $F_*$ is the unique vector field on $N$ that is $F$-related to $X$, and naturality says $F_*[X, Y] = [F_* X, F_* Y]$ — pushforward is a Lie algebra homomorphism. See the pushforward theorem.

- **The Lie algebra of derivations of a commutative ring** — the theorem reformulates this. $\mathfrak{X}(M) \cong \mathrm{Der}_\mathbb{R}(C^\infty(M))$ as Lie algebras under the commutator bracket; the theorem certifies the Lie algebra structure on the derivation side. The commutator of derivations is the model for the Lie bracket on $\mathfrak{X}(M)$.

---

# Unlocked by This

> [!tip] Universal Enveloping Algebra *(from Lie Theory)*
> Given a Lie algebra $\mathfrak{g}$, the **universal enveloping algebra** $U(\mathfrak{g})$ is the associative algebra with the universal property "every Lie algebra homomorphism $\mathfrak{g} \to A$ (with $A$ associative, taking the bracket to the commutator) factors through $U(\mathfrak{g})$". The Jacobi identity (c) is the precise condition that makes this construction well-defined. The Poincaré–Birkhoff–Witt theorem identifies a vector-space basis of $U(\mathfrak{g})$ in terms of a basis of $\mathfrak{g}$; this is the foundation of representation theory of Lie algebras.

> [!tip] Lie's Third Theorem *(from Lie Theory)*
> Every finite-dimensional real Lie algebra is the Lie algebra of some Lie group (in fact, a unique connected, simply connected Lie group). The proof builds the Lie group as integral leaves of a foliation defined by the Lie algebra; the foliation is involutive because of the Jacobi identity, and integrability comes from the [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|Frobenius theorem]]. So the Jacobi identity is exactly the integrability condition that lets you integrate "infinitesimal symmetry" to "global symmetry".

> [!tip] Adjoint Representation *(from Lie Theory)*
> The map $\mathrm{ad} : \mathfrak{g} \to \mathrm{End}(\mathfrak{g})$, $\mathrm{ad}_X(Y) = [X, Y]$, is a Lie algebra homomorphism by the Jacobi identity (c). This is the **adjoint representation** of $\mathfrak{g}$ on itself, and the **Killing form** $K(X, Y) = \mathrm{tr}(\mathrm{ad}_X \mathrm{ad}_Y)$ is the natural inner product on a Lie algebra. The Killing form distinguishes semisimple Lie algebras (Killing form non-degenerate) from solvable ones (Killing form degenerate), giving the basic dichotomy of Lie algebra structure theory.
