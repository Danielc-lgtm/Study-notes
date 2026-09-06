---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - The Smooth Functions Ring"
  - "Def - Flow of a Vector Field"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold. $X, Y, Z \in \mathfrak{X}(M)$ are smooth [[Def - Smooth Vector Field|vector fields]]. $C^\infty(M)$ is the [[Def - The Smooth Functions Ring|ring of smooth functions]] on $M$. For $X \in \mathfrak{X}(M)$ and $f \in C^\infty(M)$, $Xf \in C^\infty(M)$ is the function $p \mapsto X_p f$, the action of $X$ on $f$ as a derivation. In a chart $(U, (x^i))$ with $X = X^i \partial_i$ and $Y = Y^j \partial_j$, the brackets satisfy $[\partial_i, \partial_j] = 0$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Axiom Motivation

The challenge that the Lie bracket addresses is: **given two smooth vector fields $X$ and $Y$, what is the natural way to combine them into a third?** The space $\mathfrak{X}(M)$ already has two algebraic structures — addition $(X, Y) \mapsto X + Y$, and multiplication by smooth functions $(f, X) \mapsto fX$ — making it a [[Def - Module|module]] over $C^\infty(M)$. But these are "linear" combinations; nothing in the module structure gives a way to *multiply* two vector fields and obtain a third.

The first attempt — multiply $X$ and $Y$ as operators on functions, $XYf = X(Yf)$ — fails because the composition $XY$ is not a derivation of $C^\infty(M)$: applying the product rule twice gives second-derivative terms that violate Leibniz. Explicitly, $XY(fg) = X(f Yg + g Yf) = Xf \cdot Yg + f \cdot XYg + Xg \cdot Yf + g \cdot XYf$, which has the unwanted cross terms $Xf \cdot Yg + Xg \cdot Yf$ that no derivation produces. So $XY$ is not a vector field.

But notice: the unwanted terms are *symmetric* in $X, Y$. If we form the **commutator** $XY - YX$, the cross terms cancel:

$$(XY - YX)(fg) = Xf \cdot Yg + Xg \cdot Yf - Yf \cdot Xg - Yg \cdot Xf + f(XY - YX)g + g(XY - YX)f$$
$$= f(XY - YX)g + g(XY - YX)f.$$

So $XY - YX$ *is* a derivation. We define $[X, Y] := XY - YX$, treating each side as an operator on $C^\infty(M)$; by [[Def - Smooth Vector Field|the derivation criterion]], this commutator is a smooth vector field. We have found a way to multiply vector fields.

Why is this *the* natural operation, and not just *an* operation? Four pieces of evidence cohere:

1. **It is the unique natural binary operation up to scaling.** Among all binary operations $\mathfrak{X}(M) \otimes \mathfrak{X}(M) \to \mathfrak{X}(M)$ that are invariant under [[Def - Diffeomorphism|diffeomorphisms]] (i.e. natural in the categorical sense), the Lie bracket is essentially the only one — a theorem of Kirillov, Janyška, and others. This is why the bracket appears in so many disguises: it is the unique natural binary operation available.

2. **It captures the infinitesimal failure of flows to commute.** Geometrically, $[X, Y]$ measures, to leading order, how much the parallelogram fails to close when you flow along $X$ for time $\sqrt{t}$, then along $Y$ for time $\sqrt{t}$, then back along $X$ and back along $Y$. The gap at the corner is $t [X, Y]_p + O(t^{3/2})$. This is the operational meaning of the bracket — see [[Thm - Commuting Flows Theorem]].

3. **It is the Lie derivative of $Y$ along $X$.** The Lie derivative $\mathcal{L}_X Y$ — the rate at which $Y$ changes when you push it forward along the flow of $X$ and compare to the original — turns out to equal $[X, Y]$ exactly (Lee Theorem 9.38). So the bracket has a geometric interpretation as a derivative; see [[Def - Lie Derivative of a Vector Field]].

4. **It makes $\mathfrak{X}(M)$ a Lie algebra.** The bracket is bilinear, antisymmetric, and satisfies the Jacobi identity. These are the defining axioms of a **Lie algebra**, and the whole edifice of Lie theory rests on this structure.

The **true name** of the bracket is the geometric one: $[X, Y]$ is the infinitesimal closure-failure of the flow parallelogram, equivalently the Lie derivative of $Y$ along $X$. The algebraic definition $[X, Y]f = X(Yf) - Y(Xf)$ is the right thing to *check* — it gives the coordinate formula directly — but the geometric meaning is the right thing to *think*.

A natural objection: why not symmetric $XY + YX$? This is *also* not a derivation (second-derivative terms reappear with the same sign, not cancelling), so it does not produce a vector field; it produces a second-order differential operator. The antisymmetric combination is the unique one that produces a vector field. So antisymmetry is not a choice — it is forced.

Could one have defined the bracket via the coordinate formula $[X, Y]^j = X^i \partial_i Y^j - Y^i \partial_i X^j$ directly? Yes, and one then has to prove the result is chart-independent. The derivation-commutator definition makes chart-independence automatic: the commutator of two intrinsically defined derivations is intrinsically defined.

---

# The Definition

The **Lie bracket** of two smooth vector fields $X, Y \in \mathfrak{X}(M)$ is the smooth vector field $[X, Y] \in \mathfrak{X}(M)$ defined by its action on smooth functions:

$$[X, Y] f \;:=\; X(Yf) - Y(Xf), \qquad f \in C^\infty(M).$$

By the cancellation of second-derivative terms (above) this is a derivation of $C^\infty(M)$, hence by [[Def - Smooth Vector Field|the derivation criterion]] a smooth vector field.

In a smooth chart $(U, (x^i))$ with $X = X^i \partial_i$ and $Y = Y^j \partial_j$, the bracket has the **coordinate formula**

$$[X, Y]^j = X^i \frac{\partial Y^j}{\partial x^i} - Y^i \frac{\partial X^j}{\partial x^i},$$

or equivalently $[X, Y] = (X Y^j - Y X^j)\partial_j$.

The bracket has the following equivalent characterizations:

1. **Commutator of derivations.** $[X, Y] = XY - YX$ as operators on $C^\infty(M)$.
2. **Lie derivative.** $[X, Y] = \mathcal{L}_X Y$, where $\mathcal{L}_X Y$ is the [[Def - Lie Derivative of a Vector Field|Lie derivative]] of $Y$ along the flow of $X$. (Lee Theorem 9.38; proved as part of [[Thm - Lie Bracket Properties]].)
3. **Infinitesimal commutator of flows.** Let $\phi^X$ and $\phi^Y$ denote the flows of $X$ and $Y$. Then at every point $p$,
$$[X, Y]_p = \frac{d}{dt}\bigg|_{t=0} (\phi^X_{-t})_* Y_{\phi^X_t(p)} = \lim_{t \to 0} \frac{1}{t}\big( (\phi^X_{-t})_* Y - Y \big)_p.$$
Equivalently, $[X, Y] = 0$ if and only if the flows of $X$ and $Y$ commute (see [[Thm - Commuting Flows Theorem]]).

---

# Categorical / Structural Definition

The Lie bracket equips $\mathfrak{X}(M)$ with the structure of a **Lie algebra over $\mathbb{R}$**: a real vector space $\mathfrak{g}$ together with a bilinear, antisymmetric operation $[\cdot,\cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ satisfying the **Jacobi identity** $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$.

This Lie algebra structure is *natural*: every diffeomorphism $F : M \to N$ induces a Lie algebra isomorphism $F_* : \mathfrak{X}(M) \to \mathfrak{X}(N)$, and more generally for any smooth map $F : M \to N$, $F$-relatedness is preserved by the bracket ($X \sim_F X'$, $Y \sim_F Y'$ imply $[X, Y] \sim_F [X', Y']$). So the bracket commutes with the only natural operations there are.

Algebraically, $\mathfrak{X}(M)$ is isomorphic, as a Lie algebra, to the **derivation Lie algebra** $\mathrm{Der}_\mathbb{R}(C^\infty(M))$ — the set of $\mathbb{R}$-linear maps $C^\infty(M) \to C^\infty(M)$ satisfying the Leibniz rule, with bracket the commutator. The bijection sends a vector field $X$ to the derivation $f \mapsto Xf$, and the bracket on one side matches the commutator on the other.

The Lie algebra $\mathfrak{X}(M)$ is infinite-dimensional in general. Its finite-dimensional subalgebras — for instance, the left-invariant vector fields on a Lie [[Def - Group|group]] — are the central objects of Lie theory. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

---

# Relate to Other Fields / Compression

In linear algebra, the analogue of the Lie bracket is the **commutator of matrices**: $[A, B] = AB - BA$. The matrix commutator makes the space of $n \times n$ matrices into a Lie algebra $\mathfrak{gl}(n)$, with subalgebras like $\mathfrak{sl}(n)$ (traceless matrices), $\mathfrak{o}(n)$ (skew-symmetric matrices), $\mathfrak{u}(n)$ (skew-Hermitian matrices). The Lie bracket of vector fields *specializes* to the matrix commutator when restricted to left-invariant vector fields on a matrix Lie group; see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

In quantum mechanics, the commutator $[\hat A, \hat B] = \hat A \hat B - \hat B \hat A$ of operators on a Hilbert space plays the structural role of the Lie bracket. The canonical commutation relation $[\hat x, \hat p] = i\hbar$ is a Lie bracket in $\mathfrak{gl}(\mathcal{H})$. The quantization map sends classical Poisson brackets to quantum commutators (in the leading semiclassical order), preserving the Lie algebra structure — see geometric quantization.

In Poisson geometry, the analogue is the **Poisson bracket** $\{f, g\}$ on a Poisson manifold, which makes $C^\infty(M)$ into a Lie algebra. The bracket of Hamiltonian vector fields satisfies $[X_f, X_g] = -X_{\{f, g\}}$, so the Lie bracket on vector fields and the Poisson bracket on functions are anti-isomorphic Lie algebras when restricted to Hamiltonian vector fields. See [[Differential Geometry VIII — Differential Forms]] forward.

**True name:** The Lie bracket is the **mixed second-order commutator of the flows**. With the convention used here, the loop $\phi^Y_{-t}\circ\phi^X_{-s}\circ\phi^Y_t\circ\phi^X_s$ has leading displacement $st[X,Y]$ in local coordinates. Reversing the loop reverses the sign. Algebraically the same object is the commutator of derivations; geometrically it is the rate at which $Y$ changes in the moving frame of $X$.

---

# Examples / Corollaries

**Is an instance: brackets of coordinate vector fields are zero.** $[\partial/\partial x^i, \partial/\partial x^j] = 0$ in any smooth chart, because in coordinates both fields have constant components, so the coordinate formula gives zero. This is equivalent to the equality of mixed partial derivatives.

**Is an instance: $[X, Y]$ for $X = \partial_x$, $Y = x \partial_y$ on $\mathbb{R}^2$.** The coordinate formula gives $[X, Y]^x = (1)(0) - (x)(0) = 0$ and $[X, Y]^y = (1)(1) - (x)(0) = 1$, so $[X, Y] = \partial_y$. This is nonzero everywhere, so the flows of $X$ (translation in $x$) and $Y$ (shear in $y$ by amount $x$) do not commute. See [[Ex - Two Vector Fields with Nonzero Lie Bracket]].

**Is an instance: function-product rule.** For $f, g \in C^\infty(M)$, $[fX, gY] = fg[X, Y] + f(Xg)Y - g(Yf)X$. Easy check: act on $h \in C^\infty(M)$ and expand using the Leibniz rule. The correction terms $f(Xg)Y - g(Yf)X$ are the obstruction to $C^\infty(M)$-bilinearity of the bracket.

**Is an instance: $[X, X] = 0$.** Antisymmetry forces $[X, X] = -[X, X]$, hence $[X, X] = 0$. So every vector field commutes with itself — Corollary 9.43 of Lee.

**Is an instance: matrix Lie group bracket.** On $\mathrm{GL}(n, \mathbb{R})$ — an open subset of $\mathbb{R}^{n^2}$ — the left-invariant vector field $A^L$ associated with $A \in \mathfrak{gl}(n)$ has value at $X \in \mathrm{GL}(n)$ given by $A^L_X = X^i_j A^j_k (\partial/\partial X^i_k)$. The Lie bracket of $A^L$ and $B^L$ at the identity reduces to the matrix commutator $[A, B] = AB - BA$. So the Lie algebra of $\mathrm{GL}(n)$ is exactly the matrix algebra with the commutator bracket — Lee Proposition 8.41.

**Is NOT an instance: a $C^\infty(M)$-bilinear operation.** Take $X=Y=\partial_x$ and $f=x$. Although $[X,Y]=0$, the product rule gives
$$[fX,Y]=f[X,Y]-Y(f)X=-\partial_x\ne0.$$
Thus the bracket is real-bilinear but not $C^\infty(M)$-bilinear.

**Is NOT an instance: the product $XY$ as an operator.** $XY$ is a second-order differential operator on $C^\infty(M)$, not a derivation, hence not a vector field. The commutator $XY - YX$ is the lowest-order cancellation that produces a vector field.

**Corollary (the bracket is $\mathbb{R}$-bilinear and antisymmetric).** Bilinearity over $\mathbb{R}$ is immediate from the bilinearity of multiplication and subtraction of operators. Antisymmetry $[X, Y] = -[Y, X]$ is built into the definition.

**Corollary (Jacobi identity).** $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$. Proof: expand each bracket as a commutator of operators on functions and observe that every term appears once with each sign, summing to zero. The Jacobi identity is the structural condition that $\mathrm{ad}_X := [X, \cdot\,] : \mathfrak{X}(M) \to \mathfrak{X}(M)$ is a derivation of the bracket. See [[Ex - The Jacobi Identity for Vector Fields]].

**Corollary (the bracket of $F$-related fields is $F$-related).** For a smooth map $F : M \to N$, if $X \sim_F X'$ and $Y \sim_F Y'$, then $[X, Y] \sim_F [X', Y']$. Naturality. In particular, if $F$ is a diffeomorphism, $F_*[X, Y] = [F_*X, F_*Y]$ — the pushforward is a Lie algebra homomorphism.

**Calibration check.** You should be able to: (a) compute the bracket $[r \partial_r, \partial_\theta]$ in polar coordinates on $\mathbb{R}^2 \setminus \{0\}$ (the radial and angular fields — answer: $0$, because both fields have components depending on only one coordinate, and the coordinate formula gives zero); (b) verify that $\mathrm{ad}_X = [X, \cdot\,]$ is a derivation of the Lie bracket using the Jacobi identity; (c) explain why the Lie bracket is *not* $C^\infty(M)$-bilinear and identify the obstruction in $[fX, gY]$.

---

# Unlocked by This

> [!tip] Lie Algebra of a Lie Group *(from Lie Theory)*
> The Lie bracket on $\mathfrak{X}(G)$ restricts to a finite-dimensional Lie subalgebra on the **left-invariant vector fields** of a Lie group $G$. This subalgebra, denoted $\mathfrak{g}$ and identified with $T_e G$ as a vector space, is the **Lie algebra of $G$**. For matrix Lie groups, this Lie algebra is the matrix algebra with the commutator bracket. The bracket on vector fields is the bridge between the geometric structure of $G$ and the algebraic structure of $\mathfrak{g}$ — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

> [!tip] Involutivity and the Frobenius Theorem *(from Distribution Theory)*
> A subbundle $D \subseteq TM$ is **involutive** if $[X, Y] \in \Gamma(D)$ whenever $X, Y \in \Gamma(D)$. The Frobenius theorem ([[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]]) says an involutive distribution is **integrable** — locally tangent to a foliation. So "closed under bracket" is exactly the integrability condition for a distribution to be the tangent space of a foliation. The single-field case $\dim D = 1$ reduces to the [[Thm - Canonical Form for a Nonvanishing Vector Field|Straightening Theorem]] in this chapter.

> [!tip] Lie Derivative on Tensor Fields and Forms *(from Multilinear Analysis on Manifolds)*
> The bracket $[X, Y]$ is the Lie derivative $\mathcal{L}_X Y$ of vector fields. The same construction extends to all tensor fields and differential forms ([[Differential Geometry VIII — Differential Forms]]): the Lie derivative $\mathcal{L}_X$ is a degree-zero derivation of the tensor algebra commuting with contractions. For differential forms, **Cartan's magic formula** $\mathcal{L}_X = d \iota_X + \iota_X d$ provides a remarkably compact formula relating the Lie derivative to the exterior derivative and the interior product.

> [!tip] Poisson Bracket and Hamiltonian Mechanics *(from Symplectic Geometry)*
> On a symplectic manifold $(M, \omega)$, functions $f, g$ have a **Poisson bracket** $\{f, g\} = \omega(X_f, X_g)$, and the Hamiltonian vector fields $X_f, X_g$ satisfy $[X_f, X_g] = -X_{\{f, g\}}$. So the Lie bracket on Hamiltonian vector fields is anti-isomorphic to the Poisson bracket on functions, and the Lie algebra structure of $\mathfrak{X}(M)$ inherits from this chapter the Poisson algebra of mechanics.
