---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Alternating Tensor and Lambda^k V*"
  - "Def - Differential k-Form on a Manifold"
  - "Def - The Wedge Product"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold; $V$ is a finite-dimensional real vector space (typically $V = T_pM$); $\Lambda^k V^*$ is the space of alternating $k$-tensors on $V$; $\Omega^k(M) = \Gamma(\Lambda^k T^*M)$ is the space of smooth differential $k$-forms on $M$. Forms are denoted $\omega, \eta, \alpha, \beta$ with degrees $\deg\omega = k$, $\deg\eta = \ell$. $\operatorname{Alt} : T^k(V^*) \to \Lambda^k(V^*)$ is the alternation projector, $\operatorname{Alt}\alpha(v_1, \dots, v_k) = \tfrac{1}{k!}\sum_\sigma (\operatorname{sgn}\sigma)\,\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)})$.

**Standing convention — the determinant convention.** Two conventions for $\wedge$ are common in the literature. We use the **determinant convention** throughout, defined so that $(\omega^1 \wedge \cdots \wedge \omega^k)(v_1, \dots, v_k) = \det(\omega^i(v_j))$. The competing **Alt convention** would give the right-hand side a $1/k!$ factor instead. The conversion between the two conventions is $\omega \wedge_{\text{det}} \eta = \frac{(k+\ell)!}{k!\,\ell!}\omega \wedge_{\text{Alt}} \eta$. See [[Differential Geometry VIII — Differential Forms]] for the registry-level discussion. Bridges to [[Def - The Wedge Product]] in [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|MA IV]], which uses the same determinant convention.

---

# Axiom Motivation

We have alternating tensors in $\Lambda^k V^*$ — the right algebraic shape for signed $k$-dimensional measurement — and we want to *multiply* them. Two demands force the multiplication, with no freedom in between.

The first demand: the multiplication must produce alternating tensors of additive degree. We want a bilinear, associative map $\Lambda^k \times \Lambda^\ell \to \Lambda^{k+\ell}$ that turns the disjoint union $\Lambda^\bullet = \bigoplus_k \Lambda^k$ into a graded algebra. A naive tensor-product multiplication $\omega \otimes \eta$ would land in $T^{k+\ell}(V^*)$, not in the alternating piece — so we must "alternate" the result. The cleanest fix is to define $\omega \wedge \eta = \operatorname{const} \cdot \operatorname{Alt}(\omega \otimes \eta)$ for some normalising constant; the only question is the choice of constant.

The second demand pins the constant down: **the wedge of $n$ one-forms on an $n$-dimensional space should be the determinant of the coefficient matrix**, with no further normalisation. Specifically, for $1$-forms $\omega^1, \dots, \omega^n$ and vectors $v_1, \dots, v_n$, the demand is
$$(\omega^1 \wedge \cdots \wedge \omega^n)(v_1, \dots, v_n) = \det(\omega^i(v_j)).$$
This determinant is the signed $n$-dimensional volume of the parallelepiped spanned by the vectors $v_j$ as seen by the covectors $\omega^i$, and the integration theory of [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]] depends crucially on the wedge giving exactly this — no factor, no normalisation. Working out what $\operatorname{Alt}(\omega^1 \otimes \cdots \otimes \omega^n)$ evaluates to and comparing, one finds the determinant convention requires the factor $\frac{(k+\ell)!}{k!\,\ell!}$:
$$\omega \wedge \eta = \frac{(k+\ell)!}{k!\,\ell!}\,\operatorname{Alt}(\omega \otimes \eta).$$
The Alt convention drops this factor; the price is that the determinant identity acquires a $1/k!$ factor. We accept the cumbersome-looking front constant because it makes the determinant identity clean.

Once the constant is chosen, the rest follows automatically. Bilinearity: from the bilinearity of $\otimes$ and the linearity of $\operatorname{Alt}$. Associativity: a slightly involved combinatorial check, but the final form is $\omega \wedge \eta \wedge \zeta = \frac{(k+\ell+m)!}{k!\,\ell!\,m!}\operatorname{Alt}(\omega \otimes \eta \otimes \zeta)$, manifestly associative. Graded anticommutativity $\omega \wedge \eta = (-1)^{k\ell}\eta \wedge \omega$: each $1$-form of $\omega$ passed across each $1$-form of $\eta$ produces one sign by anticommutativity at the bilinear level, and there are $k\ell$ such passes.

What breaks if the front constant is set wrong? The whole change-of-variables story. The top-degree wedge $dx^1 \wedge \cdots \wedge dx^n$ on $\mathbb{R}^n$ is the integrand for ordinary multiple integration, and the pullback under a coordinate change must reproduce the Jacobian determinant exactly — not with a $1/n!$ factor, not with a $(n!)$ factor. The determinant convention is what makes this identity have no extra factors.

What breaks if we demand symmetric multiplication instead — drop anticommutativity? Then $\omega \wedge \omega$ does not vanish for $1$-forms; the algebra becomes commutative; the top-degree wedge produces the *permanent* of the coefficient matrix, not the determinant. The whole theory of orientation, integration, and Stokes' theorem requires the wedge to be antisymmetric on $1$-forms — orientation is a sign, and only antisymmetric multiplication carries signs.

On a manifold the construction extends pointwise: $(\omega \wedge \eta)_p = \omega_p \wedge \eta_p$ in $\Lambda^{k+\ell} T_p^*M$, and the result is smooth in $p$ because the operations are bilinear and smooth in the coefficients of $\omega, \eta$ in any chart.

---

# The Definition

**The vector-space wedge.** For a finite-dimensional real vector space $V$ and $\omega \in \Lambda^k V^*$, $\eta \in \Lambda^\ell V^*$, the **wedge product** $\omega \wedge \eta \in \Lambda^{k+\ell} V^*$ in the **determinant convention** is
$$\omega \wedge \eta = \frac{(k+\ell)!}{k!\,\ell!}\,\operatorname{Alt}(\omega \otimes \eta).$$

Equivalently, the wedge product is the *unique* $\mathbb{R}$-bilinear, associative, anticommutative operation $\Lambda^\bullet V^* \times \Lambda^\bullet V^* \to \Lambda^\bullet V^*$ satisfying, for any $1$-covectors $\omega^1, \dots, \omega^k \in V^*$,
$$(\omega^1 \wedge \cdots \wedge \omega^k)(v_1, \dots, v_k) = \det\!\big(\omega^i(v_j)\big). \tag{$\ast$}$$
Equivalently (Lee Exercise 14.12), the wedge product is the unique associative bilinear operation satisfying $\omega \wedge \eta = (-1)^{k\ell}\eta \wedge \omega$ and $\varepsilon^{i_1} \wedge \cdots \wedge \varepsilon^{i_k} = \varepsilon^I$ for the elementary $k$-covectors of a basis.

**Wedge on a manifold.** For differential forms $\omega \in \Omega^k(M)$ and $\eta \in \Omega^\ell(M)$, define $\omega \wedge \eta \in \Omega^{k+\ell}(M)$ pointwise:
$$(\omega \wedge \eta)_p = \omega_p \wedge \eta_p \quad \text{in } \Lambda^{k+\ell} T_p^* M.$$
If $\omega = \sum'_I \omega_I\,dx^I$ and $\eta = \sum'_J \eta_J\,dx^J$ in a chart, then
$$\omega \wedge \eta = \sum_{I, J} \omega_I\,\eta_J\,dx^I \wedge dx^J,$$
where each $dx^I \wedge dx^J$ is reduced to an increasing multi-index by anticommuting $1$-forms and using $dx^i \wedge dx^j = -dx^j \wedge dx^i$, with terms containing a repeated index set to zero. By the determinant identity, $dx^I \wedge dx^J = dx^{IJ}$ where $IJ$ is the concatenation; reducing to increasing form picks up the sign of the sorting permutation.

**Algebraic properties.** The wedge product on $\Omega^\bullet(M) = \bigoplus_{k=0}^n \Omega^k(M)$ is:
1. **Bilinear** over $\mathbb{R}$ — and in fact over $C^\infty(M)$, since the wedge of a $0$-form (function) with a $k$-form is ordinary scalar multiplication.
2. **Associative**: $(\omega \wedge \eta) \wedge \zeta = \omega \wedge (\eta \wedge \zeta)$.
3. **Graded anticommutative**: $\omega \wedge \eta = (-1)^{k\ell}\eta \wedge \omega$ for $\omega \in \Omega^k$, $\eta \in \Omega^\ell$.
4. **Determinant identity**: For $1$-forms $\omega^1, \dots, \omega^k$ on $M$ and tangent vectors $v_1, \dots, v_k \in T_pM$, $(\omega^1 \wedge \cdots \wedge \omega^k)_p(v_1, \dots, v_k) = \det(\omega^i_p(v_j))$.
5. **Natural under pullback**: $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$ for any smooth map $F$.

Thus $(\Omega^\bullet(M), \wedge)$ is an associative graded-anticommutative algebra over $C^\infty(M)$ of total rank $2^n$.

**A useful corollary of graded anticommutativity.** A form of odd degree wedged with itself vanishes: $\omega \in \Omega^{2k+1}(M) \Rightarrow \omega \wedge \omega = -\omega \wedge \omega \Rightarrow \omega \wedge \omega = 0$. This is *false* for forms of even degree — a $2$-form may have nonzero square.

---

# Categorical Definition

The wedge product is the multiplication of the **exterior algebra of $V^*$**, which is the universal associative graded algebra equipped with a degree-$1$ map $V^* \hookrightarrow \Lambda^\bullet V^*$ subject to the single relation $v \wedge v = 0$ for $v \in V^*$. Universality means: any associative $\mathbb{R}$-algebra $A$ together with a linear map $\phi : V^* \to A$ such that $\phi(v)^2 = 0$ for every $v$ factors uniquely through $V^* \hookrightarrow \Lambda^\bullet V^* \to A$. The exterior algebra is the *freest* such algebra.

The relation $v \wedge v = 0$ encodes anticommutativity in disguise: expand $(v + w) \wedge (v + w) = 0$ to obtain $v \wedge w + w \wedge v = 0$, i.e., anticommutativity of $1$-forms. The graded-anticommutativity rule for higher-degree forms is a *consequence* of this single relation plus associativity, not a separate axiom.

**The exterior algebra functor.** The assignment $V \mapsto \Lambda^\bullet V^*$ is a contravariant functor from finite-dimensional vector spaces to graded-anticommutative algebras: a linear map $T : V \to W$ induces, by precomposition, an algebra homomorphism $\Lambda^\bullet T^* : \Lambda^\bullet W^* \to \Lambda^\bullet V^*$ in the reverse direction. The manifold version is the corresponding statement at the level of forms: a smooth map $F : M \to N$ induces an algebra homomorphism $F^* : \Omega^\bullet(N) \to \Omega^\bullet(M)$, the [[Def - Pullback of a Differential Form on a Manifold|pullback]] of forms.

**Differential graded algebra (DGA).** With the [[Def - Exterior Derivative on a Manifold|exterior derivative]] $d$, the algebra $(\Omega^\bullet(M), \wedge, d)$ becomes a **differential graded algebra**: an associative graded algebra with a derivation $d$ of degree $+1$ satisfying $d^2 = 0$ and the graded Leibniz rule $d(\omega \wedge \eta) = d\omega \wedge \eta + (-1)^{\deg\omega}\,\omega \wedge d\eta$. DGAs are the basic objects of rational homotopy theory; the de Rham DGA is one of the two paradigmatic examples (the other is singular cochains).

---

# Relate to Other Fields / Compression

The wedge product is the **algebraic content of the determinant**, lifted from a numerical operation on matrices to an algebraic operation on forms. The determinant of an $n \times n$ matrix is usually defined by an explicit alternating sum over permutations; the wedge product shows this formula is forced. Take $n$ column vectors of the matrix as inputs to the wedge of $n$ standard dual basis vectors: $(\varepsilon^1 \wedge \cdots \wedge \varepsilon^n)(v_1, \dots, v_n) = \det(\varepsilon^i(v_j))$, which is the determinant of the original matrix. Every property of determinants — multiplicativity $\det(AB) = \det A \det B$, alternation in columns, vanishing on dependent columns — is a property of the wedge product, read in top degree.

**True name:** The wedge product is "the unique associative bilinear multiplication on forms such that the product of $k$ one-forms reproduces the determinant."

In the language of [[Differential Geometry VII — Tensors and Tensor Fields|DG VII tensor fields]], the wedge product is, up to the combinatorial factor in the determinant convention, the alternation of the tensor product: $\omega \wedge \eta = \frac{(k+\ell)!}{k!\,\ell!} \operatorname{Alt}(\omega \otimes \eta)$. The reason wedge is preferred over plain $\otimes$ in differential geometry is that the alternating piece is what integrates invariantly over oriented submanifolds, and the wedge is the natural multiplication on the alternating piece.

The bridge to [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|MA IV]] is verbatim: the wedge product of forms on a manifold restricts in any chart to the [[Def - The Wedge Product|wedge product on Euclidean space]]. The MA IV theory is the local model; this chapter is the global theory, with the wedge respecting chart overlaps because, by the determinant identity, it transforms by the Jacobian determinant — the same factor the change of variables for top-degree forms produces.

In **physics** the wedge product is the algebraic content of cross products in dimension $3$ (under the identification $\wedge : T^*\mathbb{R}^3 \times T^*\mathbb{R}^3 \to \Lambda^2 T^*\mathbb{R}^3 \cong T\mathbb{R}^3$ via Hodge duality), of angular momentum in mechanics (an alternating bilinear form in position and momentum), and of magnetic flux (a $2$-form whose integral over a surface measures flux through it). In **electromagnetism** the field strength $F = dA$ is a $2$-form and the action is $\int F \wedge \star F$, the wedge appearing intrinsically.

---

# Examples / Corollaries

**Is an instance — wedging $1$-forms on $\mathbb{R}^3$.** Take $\omega = dx + 2\,dy$ and $\eta = dy + 3\,dz$. Then
$$\omega \wedge \eta = (dx + 2\,dy) \wedge (dy + 3\,dz) = dx \wedge dy + 3\,dx \wedge dz + 2\,dy \wedge dy + 6\,dy \wedge dz.$$
By anticommutativity $dy \wedge dy = 0$, leaving $\omega \wedge \eta = dx \wedge dy + 3\,dx \wedge dz + 6\,dy \wedge dz$, a $2$-form. Note that all the *non-repeated* products survive — only the repeated-factor term dies.

**Is an instance — the determinant identity in dimension $2$.** With $\omega = a\,dx + b\,dy$ and $\eta = c\,dx + d\,dy$ on $\mathbb{R}^2$,
$$\omega \wedge \eta = (ad - bc)\,dx \wedge dy.$$
The coefficient $ad - bc$ is $\det\begin{pmatrix}a & b \\ c & d\end{pmatrix}$. This confirms the determinant identity in degree $2$.

**Is an instance — symplectic form has nonzero square.** On $\mathbb{R}^4$ the $2$-form $\omega = dx^1 \wedge dx^2 + dx^3 \wedge dx^4$ satisfies
$$\omega \wedge \omega = 2\,dx^1 \wedge dx^2 \wedge dx^3 \wedge dx^4 \neq 0.$$
This is the **Liouville volume form** on $\mathbb{R}^4$ thought of as the phase space of a $2$-dof Hamiltonian system. Even-degree forms can have nonzero squares; this is what distinguishes symplectic geometry from generic differential geometry.

**Is an instance — pullback respects $\wedge$.** Let $F(u, v) = (u, v, u^2 - v^2)$ from $\mathbb{R}^2$ to $\mathbb{R}^3$. Compute $F^*(y\,dx \wedge dz)$: $F^*dx = du$, $F^*dy = dv$, $F^*dz = d(u^2 - v^2) = 2u\,du - 2v\,dv$. Then $F^*(y\,dx \wedge dz) = v\,du \wedge (2u\,du - 2v\,dv) = -2v^2\,du \wedge dv$ (using $du \wedge du = 0$). This is the pullback of a single basic $2$-form; for more complicated forms one expands by linearity.

**Is NOT an instance — $\omega \wedge \omega = 0$ for all forms.** False in even degree. The symplectic example above is the standard counterexample. The correct rule is: $\omega \wedge \omega = 0$ if and only if $\deg\omega$ is odd. The error is to confuse "alternating in each argument" (true) with "self-product vanishes" (only for odd degree).

**Is NOT an instance — commutativity of wedge.** False in general. The wedge is *graded* anticommutative: $\omega \wedge \eta = (-1)^{k\ell}\eta \wedge \omega$. Two odd-degree forms anticommute; an even-degree form commutes with everything (since $(-1)^{2k\ell} = 1$). The standard error is to write $\omega \wedge \eta = \eta \wedge \omega$ for two $1$-forms; this differs from the truth by a sign.

**Is NOT an instance — cross product equals wedge product.** Tempting in dimension $3$ because both are bilinear and antisymmetric, but the cross product $u \times v \in \mathbb{R}^3$ and the wedge $u \wedge v \in \Lambda^2 \mathbb{R}^3$ live in different vector spaces. They *correspond* under the dimension-$3$ Hodge star $\star : \Lambda^2 \mathbb{R}^3 \to \Lambda^1 \mathbb{R}^3 \cong \mathbb{R}^3$, but the wedge exists in every dimension while the cross product exists only in $\mathbb{R}^3$ (and degenerately in $\mathbb{R}^7$).

**Corollary — dimension of $\Omega^\bullet(M)$ at a point.** $\dim_{\mathbb{R}} \Lambda^\bullet T_p^*M = \sum_{k=0}^n \binom{n}{k} = 2^n$. So at every point, $\Omega^\bullet(M)$ has a $2^n$-dimensional fibre, on which the wedge product makes it a graded-anticommutative algebra. This is the same $2^n$ as the number of subsets of $\{1, \dots, n\}$, and the correspondence "subset $\leftrightarrow$ basis $dx^I$" is the combinatorial heart of the algebra.

**Corollary — linear independence test.** $1$-forms $\omega^1, \dots, \omega^k$ are linearly independent at $p$ if and only if $\omega^1 \wedge \cdots \wedge \omega^k \neq 0$ at $p$. The proof: if dependent, the determinant identity $(\omega^1 \wedge \cdots \wedge \omega^k)(v_1, \dots, v_k) = \det(\omega^i(v_j))$ shows the wedge vanishes on any input (since dependent rows force determinant zero). Conversely, if independent, extend to a basis of $T_p^*M$ and apply the basis-evaluation formula.

**Calibration check.** Compute $(dx + dy) \wedge (dx - dy)$ on $\mathbb{R}^2$ (answer: $-2\,dx \wedge dy$); verify $(\omega \wedge \omega) = 0$ for $\omega = 3\,dx^1 + 4\,dx^2$ on $\mathbb{R}^2$; show that a $2$-form on $\mathbb{R}^3$ has at most $\binom{3}{2} = 3$ independent coefficients; show that for $\omega \in \Omega^k(M)$ with $k$ odd, $\omega \wedge \omega = 0$. If you can also state the sign $(-1)^{k\ell}$ when wedging a $k$-form past an $\ell$-form for $(k, \ell) = (2, 3)$ (answer: $-1$), you have understood the graded rule.

---

# Unlocked by This

> [!tip] The Exterior Derivative *(this chapter)*
> The wedge product is the multiplication on $\Omega^\bullet(M)$; the [[Def - Exterior Derivative on a Manifold|exterior derivative]] is the derivation. Together they make $(\Omega^\bullet(M), \wedge, d)$ a differential graded algebra, the **de Rham complex** of $M$.

> [!tip] Volume Form and Orientation *(from Differential Geometry IX)*
> A nowhere-vanishing top-degree form on an $n$-manifold is, by the dimension theorem $\dim \Lambda^n V^* = 1$, a positive scalar multiple of a fixed choice of generator on each connected component — making the choice of generator equivalent to a choice of orientation. The wedge product is what builds top-degree forms from $1$-forms; specifically, $dx^1 \wedge \cdots \wedge dx^n$ is the local model for every volume form. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

> [!tip] Hodge Star and the Inner Product on Forms *(from Riemannian Geometry)*
> On a Riemannian manifold, the wedge product pairs $\Lambda^k$ with $\Lambda^{n-k}$ into $\Lambda^n$, and the metric identifies $\Lambda^n$ with $\mathbb{R}$ via the volume form. The composite is a non-degenerate bilinear pairing $\Lambda^k \otimes \Lambda^{n-k} \to \mathbb{R}$, equivalently an isomorphism $\star : \Lambda^k \to \Lambda^{n-k}$ — the **Hodge star**. The whole codifferential / Laplacian theory on a Riemannian manifold is built from $\wedge$ and $\star$.

> [!tip] Cartan Structure Equations *(from Gauge Theory)*
> On a principal bundle with structure group $G$ and Lie algebra $\mathfrak{g}$, the connection $\omega$ is a $\mathfrak{g}$-valued $1$-form and the curvature is the $\mathfrak{g}$-valued $2$-form $\Omega = d\omega + \tfrac12 [\omega, \omega]$, where the bracket $[\cdot, \cdot]$ combines the wedge product on forms with the Lie bracket on $\mathfrak{g}$. The wedge is the form-side ingredient that makes the structure equation meaningful.
