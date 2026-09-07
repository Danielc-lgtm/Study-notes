---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Bundle-Valued Differential Forms"
  - "Def - Lie Algebra"
  - "Def - Representation of a Lie Algebra"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold (smooth means $C^\infty$; manifolds are Hausdorff and second countable), $G$ is a Lie group with Lie algebra $\mathfrak{g} = T_eG$, and $[\cdot,\cdot]\colon \mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}$ is the Lie bracket of $\mathfrak{g}$ (bilinear, antisymmetric, satisfying the Jacobi identity — see [[Def - Lie Algebra]]). For matrix groups $G\subseteq GL(k;\mathbb{R})$ the bracket is the commutator $[\xi,\eta] = \xi\eta - \eta\xi$ of $k\times k$ matrices (proved on [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]), and $\mathfrak{g}\subseteq \mathfrak{gl}(k;\mathbb{R}) = \operatorname{End}(\mathbb{R}^k)$.

We write $\Omega^p(M) = \Gamma(\Lambda^p T^*M)$ for the ordinary real-valued differential $p$-forms on $M$, with $\Omega^0(M) = C^\infty(M)$, and $\wedge$ for the [[Def - The Wedge Product on a Manifold|wedge product]] $\Omega^p(M)\times\Omega^q(M)\to\Omega^{p+q}(M)$. For a fixed finite-dimensional real vector space $W$ (below, $W = \mathfrak{g}$ or $W = V$) we write $\Omega^p(M;W) = \Gamma(\Lambda^p T^*M\otimes W)$ for the $W$-valued $p$-forms; this is the special case of [[Def - Bundle-Valued Differential Forms|bundle-valued forms]] in which the coefficient bundle is the trivial bundle $M\times W\to M$. The evaluation of $\alpha\in\Omega^p(M;W)$ on tangent vectors $X_1,\dots,X_p\in T_mM$ is $\alpha(X_1,\dots,X_p)\in W$, and for $\alpha\in\Omega^1(M;W)$ a $W$-valued $1$-form, $\alpha(X)\in W$.

The symbols on this page: $\alpha,\beta,\gamma$ denote $\mathfrak{g}$-valued forms; $a,b\in\Omega^\bullet(M)$ scalar forms; $\xi,\eta\in\mathfrak{g}$ fixed Lie-algebra elements; $\{E_i\}_{i=1}^{\dim\mathfrak{g}}$ a fixed basis of $\mathfrak{g}$; $A,B$ matrix-valued (that is, $\mathfrak{gl}(k;\mathbb{R})$-valued) $1$-forms; $\rho\colon G\to GL(V)$ a representation with differential $\rho_* = d_e\rho\colon \mathfrak{g}\to\operatorname{End}(V)$; $\phi$ a $V$-valued form and $\hat{s}$ a $V$-valued function; $X,Y$ vector fields or tangent vectors on $M$.

This is a compound page: it defines four interlocking notions — the space $\Omega^p(M;\mathfrak{g})$ of $\mathfrak{g}$-valued forms, the graded **bracket** $[\alpha\wedge\beta]$ that combines the wedge of the form parts with the Lie bracket of the values, the **wedge-action** $\rho_*(\alpha)\wedge\phi$ of $\mathfrak{g}$-valued forms on $V$-valued forms through a representation, and the **exterior derivative** $d$ acting componentwise — because all four appear together the moment one writes down a connection $\omega\in\Omega^1(P;\mathfrak{g})$ and its curvature, and none of them is meaningful without the others.

> [!warning] Convention: bracket notation, $[\omega\wedge\omega]$ versus $[\omega,\omega]$
> Bär (Definition 2.4.2) writes the bracket of two $\mathfrak{g}$-valued $1$-forms as $[\eta,\varphi]$, and the structure equation as $\Omega = d\omega + \tfrac12[\omega,\omega]$. Haydys writes $[A\wedge A]$ (equation (20)) to make visible that a wedge of the form parts is taken. This series follows Haydys and writes $[\alpha\wedge\beta]$ throughout, reserving the comma bracket $[\xi,\eta]$ for the Lie bracket of two elements of $\mathfrak{g}$. The one-line conversion is purely notational: Bär's $[\eta,\varphi]$ **is** our $[\eta\wedge\varphi]$; nothing about the operation changes.

> [!warning] Convention: the factor of $\tfrac12$
> The same operation is written two ways in the literature, and this is the source of a factor of $\tfrac12$ that confuses every first reading. For an abstract Lie algebra there is no product on $\mathfrak{g}$ other than the bracket, so the curvature of a matrix connection can only be written $F = dA + \tfrac12[A\wedge A]$ (Haydys (20)). For a **matrix** Lie algebra there is also the ambient matrix product, giving the equivalent shorter form $F = dA + A\wedge A$ (Haydys (18)). The two agree because $[A\wedge A] = 2\,A\wedge A$ for matrix-valued $1$-forms — this identity is proved below, and it is the whole reason (18) carries no $\tfrac12$ while (20) does.

---

# Axiom Motivation

The problem that forces this definition is concrete. A connection on a principal $G$-bundle is a $\mathfrak{g}$-valued $1$-form $\omega\in\Omega^1(P;\mathfrak{g})$, and its curvature will turn out to be $d\omega$ plus a quadratic correction built from $\omega$ alone. To even write the correction we must be able to multiply two $\mathfrak{g}$-valued forms and get a third. So the question is: **given $\alpha\in\Omega^p(M;\mathfrak{g})$ and $\beta\in\Omega^q(M;\mathfrak{g})$, what is a natural $\mathfrak{g}$-valued $(p+q)$-form built from them?** Answering it well is the entire content of the page, and the answer is not the naive one.

A $\mathfrak{g}$-valued $p$-form carries two pieces of data at each point: an alternating multilinear gadget in the tangent directions (the "form part") and a value in $\mathfrak{g}$ (the "algebra part"). To combine two of them we must combine both parts. On the form part there is exactly one natural bilinear associative graded-commutative product landing in higher-degree forms, the [[Def - The Wedge Product on a Manifold|wedge product]] $\wedge$; nothing else respects the alternating structure. On the algebra part we need a bilinear map $\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}$, and here is the decisive point: **a general Lie algebra has no associative product at all.** The elements of $\mathfrak{su}(2)$, for instance, are trace-free anti-Hermitian $2\times2$ matrices, and the matrix product of two of them is in general neither trace-free nor anti-Hermitian, so it lands outside $\mathfrak{su}(2)$. The only bilinear operation that keeps values inside $\mathfrak{g}$ — indeed the only one available on an abstract $\mathfrak{g}$ — is the Lie bracket $[\cdot,\cdot]$. This is what "$\mathfrak{g}$ is a Lie algebra, not an associative algebra" costs us and buys us: we lose the freedom to multiply values associatively, and we are handed instead the bracket, which is the unique natural product.

So the definition writes itself: on decomposable forms $\alpha = a\otimes\xi$ and $\beta = b\otimes\eta$ (a scalar form times a constant algebra element) we must set
$$[\alpha\wedge\beta] := (a\wedge b)\otimes[\xi,\eta],$$
wedging the form parts and bracketing the algebra parts, and then extend by bilinearity. Every desideratum is met: the result is a $\mathfrak{g}$-valued $(p+q)$-form; the construction uses only structure that every $\mathfrak{g}$-valued form has; and, because the bracket is $\operatorname{Ad}$-equivariant, the operation will commute with the group action, which is exactly what is needed for the curvature it builds to descend to the base manifold.

It is worth seeing, clause by clause, why no competing choice works. **If we drop the wedge on the form part** and use, say, the symmetric tensor product, the result is no longer alternating and is not a differential form; the degree count $p+q$ and Stokes' theorem both break, and the exterior derivative would not satisfy a Leibniz rule against it. **If we drop the bracket and try to multiply the algebra parts directly** — writing "$\alpha\cdot\beta$" with $\xi\eta$ in place of $[\xi,\eta]$ — the expression is undefined for an abstract $\mathfrak{g}$ because there is no product $\xi\eta$, and even for a matrix algebra $\xi\eta$ leaves $\mathfrak{g}$ (the trace-free anti-Hermitian example above), so the output is not a $\mathfrak{g}$-valued form. The one case where a direct product is available is the matrix wedge $A\wedge B$ of $\mathfrak{gl}(k)$-valued forms, and even there the honest bracket and the matrix wedge are related but not equal: we shall find $[A\wedge B] = A\wedge B + B\wedge A$, and only the left-hand side is defined for a general $\mathfrak{g}$. **If we forget that the bracket is antisymmetric** and imagine it were symmetric, the striking sign phenomenon below — that $[\omega\wedge\omega]$ need not vanish for a $1$-form $\omega$, even though the scalar wedge $a\wedge a$ always does — would be impossible; it is precisely the interaction of the antisymmetry of $\wedge$ on odd-degree forms with the antisymmetry of $[\cdot,\cdot]$ that makes the self-bracket of an odd form nonzero. A reader who has internalised "wedge the forms, bracket the values, and keep track of both antisymmetries" can reconstruct every formula on this page.

---

# The Definition

Let $W$ be a finite-dimensional real vector space. The space of **$W$-valued $p$-forms** on $M$ is
$$\Omega^p(M;W) := \Gamma(\Lambda^p T^*M\otimes W) \;=\; \Omega^p(M)\otimes_{\mathbb{R}} W,$$
the sections of the trivial coefficient bundle $M\times W$; the second equality holds because $W$ is finite-dimensional, so a $W$-valued form is a finite sum $\sum_i \alpha^i\otimes w_i$ with $\alpha^i\in\Omega^p(M)$ and $w_i\in W$, and choosing a basis $\{w_i\}$ of $W$ makes the sum unique. Taking $W = \mathfrak{g}$ gives the **$\mathfrak{g}$-valued $p$-forms** $\Omega^p(M;\mathfrak{g})$, the objects of this page.

**The bracket.** Define the bracket
$$[\;\cdot\wedge\cdot\;]\colon \Omega^p(M;\mathfrak{g})\times\Omega^q(M;\mathfrak{g})\longrightarrow \Omega^{p+q}(M;\mathfrak{g})$$
to be the unique $\mathbb{R}$-bilinear map determined on decomposable forms $\alpha = a\otimes\xi$ ($a\in\Omega^p(M)$, $\xi\in\mathfrak{g}$) and $\beta = b\otimes\eta$ ($b\in\Omega^q(M)$, $\eta\in\mathfrak{g}$) by
$$[\,a\otimes\xi \;\wedge\; b\otimes\eta\,] := (a\wedge b)\otimes[\xi,\eta].$$
Concretely, in a fixed basis $\{E_i\}_{i=1}^{r}$ of $\mathfrak{g}$ (where $r = \dim\mathfrak{g}$), writing $\alpha = \sum_i \alpha^i\otimes E_i$ and $\beta = \sum_j \beta^j\otimes E_j$ with scalar forms $\alpha^i\in\Omega^p(M)$, $\beta^j\in\Omega^q(M)$,
$$[\alpha\wedge\beta] = \sum_{i,j}(\alpha^i\wedge\beta^j)\otimes[E_i,E_j].$$

> [!note]- Why the bracket is well-defined
> We must check that the formula does not depend on how a form is written as a sum of decomposables. The map
> $$\Phi\colon \Omega^p(M)\times\mathfrak{g}\times\Omega^q(M)\times\mathfrak{g}\longrightarrow \Omega^{p+q}(M;\mathfrak{g}),\qquad \Phi(a,\xi,b,\eta) := (a\wedge b)\otimes[\xi,\eta],$$
> is $\mathbb{R}$-multilinear in its four arguments: it is bilinear in $(a,b)$ because the [[Def - The Wedge Product on a Manifold|wedge product]] $\Omega^p(M)\times\Omega^q(M)\to\Omega^{p+q}(M)$ is $\mathbb{R}$-bilinear, and bilinear in $(\xi,\eta)$ because the Lie bracket $\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}$ is $\mathbb{R}$-bilinear (an axiom of a [[Def - Lie Algebra|Lie algebra]]). By the universal property of the tensor product, a multilinear map factors through the tensor product; hence $\Phi$ induces a well-defined $\mathbb{R}$-bilinear map on $(\Omega^p(M)\otimes\mathfrak{g})\times(\Omega^q(M)\otimes\mathfrak{g}) = \Omega^p(M;\mathfrak{g})\times\Omega^q(M;\mathfrak{g})$, and this induced map is exactly the basis formula above. Therefore the value $[\alpha\wedge\beta]$ is independent of the chosen decomposition, and independent of the chosen basis $\{E_i\}$. $\blacksquare$

**Evaluation on $1$-forms.** When $p = q = 1$ the bracket has the pointwise evaluation formula that Bär takes as his definition (Definition 2.4.2): for $\alpha,\beta\in\Omega^1(M;\mathfrak{g})$ and vector fields $X,Y$,
$$[\alpha\wedge\beta](X,Y) = [\alpha(X),\beta(Y)] - [\alpha(Y),\beta(X)].$$
In particular, taking $\alpha = \beta = \omega$ and using the antisymmetry $[u,v] = -[v,u]$ of the Lie bracket,
$$[\omega\wedge\omega](X,Y) = [\omega(X),\omega(Y)] - [\omega(Y),\omega(X)] = 2[\omega(X),\omega(Y)].$$
This evaluation formula agrees with the tensor definition, as the collapsed proof verifies; it is the single most-used special case, because $\tfrac12[\omega\wedge\omega]$ is the quadratic term of the curvature and the factor $2$ here is exactly what the $\tfrac12$ there cancels.

> [!note]- Proof that the tensor definition gives the evaluation formula
> Both the tensor bracket $[\alpha\wedge\beta]$ and the right-hand side $R(\alpha,\beta)(X,Y) := [\alpha(X),\beta(Y)] - [\alpha(Y),\beta(X)]$ are $\mathbb{R}$-bilinear in $(\alpha,\beta)\in\Omega^1(M;\mathfrak{g})\times\Omega^1(M;\mathfrak{g})$: the left side by construction, the right side because evaluation $\alpha\mapsto\alpha(X)$ is linear and the Lie bracket is bilinear. **Hence it suffices to check the identity on decomposable forms** $\alpha = a\otimes\xi$ and $\beta = b\otimes\eta$ with $a,b\in\Omega^1(M)$ and $\xi,\eta\in\mathfrak{g}$, since both sides then extend to all forms by the same bilinear extension. **Left side.** By the definition of the bracket, $[\alpha\wedge\beta] = (a\wedge b)\otimes[\xi,\eta]$, so evaluating on $(X,Y)$ and using the scalar wedge formula $(a\wedge b)(X,Y) = a(X)b(Y) - a(Y)b(X)$ ([[Def - The Wedge Product on a Manifold|wedge product of $1$-forms]]),
> $$[\alpha\wedge\beta](X,Y) = \big(a(X)b(Y) - a(Y)b(X)\big)\,[\xi,\eta]\qquad\text{(definition of the bracket; scalar wedge on }1\text{-forms).}$$
> **Right side.** Here $\alpha(X) = a(X)\,\xi$ and $\beta(Y) = b(Y)\,\eta$ are scalar multiples of $\xi,\eta$, so by bilinearity of the Lie bracket,
> $$R(\alpha,\beta)(X,Y) = [a(X)\xi,\,b(Y)\eta] - [a(Y)\xi,\,b(X)\eta] = a(X)b(Y)[\xi,\eta] - a(Y)b(X)[\xi,\eta]\qquad\text{(bilinearity of }[\cdot,\cdot]\text{)},$$
> which equals $\big(a(X)b(Y) - a(Y)b(X)\big)[\xi,\eta]$. **Conclusion.** The two evaluations coincide on every decomposable pair, hence on all of $\Omega^1(M;\mathfrak{g})\times\Omega^1(M;\mathfrak{g})$ by bilinearity. Therefore $[\alpha\wedge\beta](X,Y) = [\alpha(X),\beta(Y)] - [\alpha(Y),\beta(X)]$. $\blacksquare$

**The wedge-action through a representation.** Let $\rho\colon G\to GL(V)$ be a [[Def - Representation of a Lie Algebra|representation]] with differential $\rho_* = d_e\rho\colon \mathfrak{g}\to\operatorname{End}(V)$, a Lie-algebra homomorphism, meaning $\rho_*[\xi,\eta] = \rho_*(\xi)\rho_*(\eta) - \rho_*(\eta)\rho_*(\xi)$ (composition of endomorphisms). For $\alpha\in\Omega^p(M;\mathfrak{g})$ and $\phi\in\Omega^q(M;V)$ define
$$\rho_*(\alpha)\wedge\phi \in \Omega^{p+q}(M;V),\qquad \rho_*(a\otimes\xi)\wedge(b\otimes v) := (a\wedge b)\otimes\rho_*(\xi)v,$$
extended $\mathbb{R}$-bilinearly (well-defined by the same universal-property argument, now using the bilinearity of $(\xi,v)\mapsto\rho_*(\xi)v$). In a basis, with $\phi = \sum_m \phi^m\otimes v_m$,
$$\rho_*(\alpha)\wedge\phi = \sum_{i,m}(\alpha^i\wedge\phi^m)\otimes\rho_*(E_i)v_m.$$
The degree-zero case $q = 0$ is Haydys's notation $a\cdot\hat{s}$ from equations (45) and (47): if $a\in\Omega^1(M;\mathfrak{g})$ is a connection form and $\hat{s}\in\Omega^0(M;V) = C^\infty(M;V)$ a $V$-valued function, then
$$a\cdot\hat{s} := \rho_*(a)\wedge\hat{s} = \rho_*(a)\,\hat{s}\ \in\ \Omega^1(M;V),\qquad (a\cdot\hat{s})(X) = \rho_*(a(X))\,\hat{s}.$$

**The exterior derivative, componentwise.** The exterior derivative $d\colon \Omega^p(M;W)\to\Omega^{p+1}(M;W)$ acts on the scalar coefficients and leaves the constant vector-space part alone:
$$d(a\otimes w) := (da)\otimes w,\qquad\text{equivalently } d\Big(\sum_i \alpha^i\otimes E_i\Big) = \sum_i (d\alpha^i)\otimes E_i.$$
This is the [[Def - Exterior Covariant Derivative on a Vector Bundle|exterior covariant derivative]] of the flat product connection on $M\times W$; it is well-defined because $d$ on scalar forms is well-defined and $\mathbb{R}$-linear, so the same universal-property argument applies. It satisfies $d\circ d = 0$ (inherited from the scalar $d$, [[Thm - d-Squared-is-Zero]]) and the graded Leibniz rule against scalar forms, $d(a\wedge\alpha) = da\wedge\alpha + (-1)^{|a|}a\wedge d\alpha$.

---

# Relate to Other Fields / Compression

The construction $[\alpha\wedge\beta] = \sum(\alpha^i\wedge\beta^j)\otimes[E_i,E_j]$ is an instance of a single algebraic pattern: **given a graded-commutative algebra $\Omega^\bullet(M)$ and any bilinear "product" $\mu\colon W\times W\to W'$, there is a unique graded product on $W$-valued forms sending $(a\otimes w)\wedge(b\otimes w') \mapsto (a\wedge b)\otimes\mu(w,w')$.** Different choices of $\mu$ give the different operations that pervade gauge theory: taking $\mu = [\cdot,\cdot]$ gives this page's bracket; taking $\mu$ to be matrix multiplication on $\mathfrak{gl}(k)$ gives the matrix wedge $A\wedge B$; taking $\mu = \rho_*(\cdot)(\cdot)\colon \mathfrak{g}\times V\to V$ gives the wedge-action; taking $\mu$ to be an $\operatorname{Ad}$-invariant polarisation gives the Chern–Weil pairing of chapter VI. They are one construction with the value-level product varying, which is why they all obey the same graded Leibniz rule and the same graded-antisymmetry bookkeeping — the signs come from $\Omega^\bullet(M)$, the algebra of the values comes from $\mu$, and the two are simply tensored.

A second compression names what the bracket *is*, operationally. **True name:** $[\alpha\wedge\beta]$ is the image of $\alpha\otimes\beta$ under "wedge the forms, then bracket the values" — the composite
$$\Omega^p(M;\mathfrak{g})\otimes\Omega^q(M;\mathfrak{g}) \xrightarrow{\ \wedge\ } \Omega^{p+q}(M;\mathfrak{g}\otimes\mathfrak{g}) \xrightarrow{\ [\cdot,\cdot]_*\ } \Omega^{p+q}(M;\mathfrak{g}),$$
where the first arrow is the ordinary wedge on $(\mathfrak{g}\otimes\mathfrak{g})$-valued forms and the second applies the bracket pointwise to the values. This is the definition already; the operation is operational as stated. The only subtlety worth flagging is that the bracket is *not* the antisymmetrisation of an associative product in general, so intuitions imported from the matrix wedge (where $[A\wedge B] = A\wedge B + B\wedge A$ does exhibit it as a symmetrised product) must be dropped for abstract $\mathfrak{g}$.

---

# Examples / Corollaries

**Is an instance — abelian $\mathfrak{g}$: all brackets vanish.** If $\mathfrak{g}$ is [[Def - Lie Algebra|abelian]], meaning $[\xi,\eta] = 0$ for all $\xi,\eta\in\mathfrak{g}$ (as for $\mathfrak{g} = \mathfrak{u}(1) = i\mathbb{R}$, or any Lie algebra of an abelian Lie group), then for all $\alpha,\beta$,
$$[\alpha\wedge\beta] = \sum_{i,j}(\alpha^i\wedge\beta^j)\otimes[E_i,E_j] = \sum_{i,j}(\alpha^i\wedge\beta^j)\otimes 0 = 0.$$
Every clause checks: the bracket $[E_i,E_j]$ is zero by abelianness, so every summand is zero. This is why for abelian structure groups the curvature reduces to $F = dA$ with no quadratic term, and Maxwell's electromagnetic field strength is simply $dA$.

**Is an instance — the self-bracket of a constant $1$-form.** Take $M = \mathbb{R}^2$ with coordinates $(x,y)$, fix $X,Y\in\mathfrak{g}$, and let
$$A = X\,dx + Y\,dy \ \in\ \Omega^1(\mathbb{R}^2;\mathfrak{g}),$$
a $\mathfrak{g}$-valued $1$-form with the two *constant* algebra coefficients $X$ (attached to $dx$) and $Y$ (attached to $dy$). We compute $[A\wedge A]$ from the basis formula, treating $\{X,Y\}$ as (part of) the algebra data rather than a basis of $\mathfrak{g}$; the bilinearity of the bracket lets us expand directly:
$$[A\wedge A] = [\,X\,dx + Y\,dy \;\wedge\; X\,dx + Y\,dy\,].$$
Expanding bilinearly into four terms and applying the decomposable rule $[\,a\otimes U\wedge b\otimes V\,] = (a\wedge b)\otimes[U,V]$ to each:
$$[A\wedge A] = (dx\wedge dx)\otimes[X,X] + (dx\wedge dy)\otimes[X,Y] + (dy\wedge dx)\otimes[Y,X] + (dy\wedge dy)\otimes[Y,Y].$$
Now $dx\wedge dx = dy\wedge dy = 0$ (a scalar $1$-form wedged with itself vanishes), $[X,X] = 0$ (antisymmetry of the Lie bracket), $dy\wedge dx = -\,dx\wedge dy$ (graded-commutativity of $\wedge$ on $1$-forms), and $[Y,X] = -[X,Y]$ (antisymmetry). Substituting,
$$[A\wedge A] = 0 + (dx\wedge dy)\otimes[X,Y] + (-\,dx\wedge dy)\otimes(-[X,Y]) + 0 = 2\,[X,Y]\,dx\wedge dy.$$
Every displayed simplification carried its reason; the result $[A\wedge A] = 2[X,Y]\,dx\wedge dy$ is nonzero whenever $X$ and $Y$ do not commute, which already shows that the self-bracket of a $1$-form is genuinely nonzero. It also cross-checks the evaluation formula: $[A\wedge A](\partial_x,\partial_y) = 2[A(\partial_x),A(\partial_y)] = 2[X,Y]$, and indeed $(2[X,Y]\,dx\wedge dy)(\partial_x,\partial_y) = 2[X,Y]$.

**Is an instance — the matrix identity $[A\wedge A] = 2\,A\wedge A$.** Let $\mathfrak{g} = \mathfrak{gl}(k;\mathbb{R}) = \operatorname{End}(\mathbb{R}^k)$ with the commutator bracket, and let $A,B\in\Omega^1(M;\mathfrak{gl}(k;\mathbb{R}))$ be matrix-valued $1$-forms. Recall from [[Def - Bundle-Valued Differential Forms|the wedge-composition of matrix-valued forms]] that $A\wedge B$ is the matrix-valued $2$-form obtained by matrix multiplication with the wedge of the scalar entries, $(A\wedge B)_{ik} = \sum_j A_{ij}\wedge B_{jk}$, whose evaluation on vector fields is the matrix product
$$(A\wedge B)(X,Y) = A(X)B(Y) - A(Y)B(X).$$
Using the evaluation formula for the bracket (proved above, in "The Definition") together with the commutator bracket $[\,\cdot,\cdot\,] = (\cdot)(\cdot) - (\cdot)(\cdot)$,
$$[A\wedge B](X,Y) = [A(X),B(Y)] - [A(Y),B(X)] \qquad\text{(evaluation formula)}$$
$$= \big(A(X)B(Y) - B(Y)A(X)\big) - \big(A(Y)B(X) - B(X)A(Y)\big) \qquad\text{(commutator bracket).}$$
On the other side,
$$(A\wedge B + B\wedge A)(X,Y) = \big(A(X)B(Y) - A(Y)B(X)\big) + \big(B(X)A(Y) - B(Y)A(X)\big) \qquad\text{(matrix-wedge evaluation, twice).}$$
Reordering the four terms of each line shows they are the *same* four matrix products with the *same* signs: both equal $A(X)B(Y) - A(Y)B(X) + B(X)A(Y) - B(Y)A(X)$. Since two $2$-forms agreeing on every pair $(X,Y)$ are equal,
$$[A\wedge B] = A\wedge B + B\wedge A.$$
Setting $B = A$ gives $[A\wedge A] = A\wedge A + A\wedge A = 2\,A\wedge A$, as claimed. This identity is precisely what reconciles Haydys's (18) $F = dA + A\wedge A$ with (20) $F = dA + \tfrac12[A\wedge A]$: substituting $[A\wedge A] = 2A\wedge A$ into (20) returns (18).

**Is NOT antisymmetric in the naive sense.** For scalar $1$-forms the wedge is antisymmetric, $a\wedge b = -\,b\wedge a$, so in particular $a\wedge a = 0$. One might expect the same of $[\alpha\wedge\beta]$, but this fails, and the failure is the whole reason the curvature has a quadratic term. The correct rule, proved on [[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms]] — which states, for $\alpha\in\Omega^p(M;\mathfrak{g})$ and $\beta\in\Omega^q(M;\mathfrak{g})$, that $[\alpha\wedge\beta] = -(-1)^{pq}[\beta\wedge\alpha]$ — carries an extra sign $-(-1)^{pq}$ coming from *both* antisymmetries interacting. For two $1$-forms ($p = q = 1$) this reads
$$[\alpha\wedge\beta] = -(-1)^{1\cdot1}[\beta\wedge\alpha] = +\,[\beta\wedge\alpha],$$
so the bracket of $1$-forms is *symmetric*, not antisymmetric. Consequently the self-bracket $[\omega\wedge\omega]$ of a $1$-form need not vanish — as the constant example above exhibited concretely, $[A\wedge A] = 2[X,Y]\,dx\wedge dy \ne 0$. The scalar intuition "an odd form wedged with itself is zero" is exactly wrong here; the algebra's antisymmetry flips the sign back.

**Corollary — $d$ is compatible with the bracket and the action (statements).** Two identities used constantly downstream follow from the definitions and are proved on the theorem page just cited: the graded Leibniz rule $d[\alpha\wedge\beta] = [d\alpha\wedge\beta] + (-1)^p[\alpha\wedge d\beta]$ for $\alpha\in\Omega^p(M;\mathfrak{g})$, and the naturality $\rho_*([\alpha\wedge\beta]) = [\rho_*(\alpha)\wedge\rho_*(\beta)]$ of a representation (using $\rho_*[\xi,\eta] = [\rho_*\xi,\rho_*\eta]$), where on the right the bracket of $\operatorname{End}(V)$-valued forms is the commutator wedge. We record them here as the outputs the bracket exists to feed; their complete proofs are on **[[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms]]**.

**Calibration check.** First, the self-bracket of an *even*-degree form vanishes. For $\alpha\in\Omega^p(M;\mathfrak{g})$ with $p$ even, relabel $i\leftrightarrow j$ in the basis formula:
$$[\alpha\wedge\alpha] = \sum_{i,j}(\alpha^i\wedge\alpha^j)\otimes[E_i,E_j] = \sum_{i,j}(\alpha^j\wedge\alpha^i)\otimes[E_j,E_i] = \sum_{i,j}(-1)^{p^2}(\alpha^i\wedge\alpha^j)\otimes(-[E_i,E_j]) = -(-1)^{p^2}[\alpha\wedge\alpha],$$
using $\alpha^j\wedge\alpha^i = (-1)^{p\cdot p}\alpha^i\wedge\alpha^j$ and $[E_j,E_i] = -[E_i,E_j]$; for $p$ even $(-1)^{p^2} = 1$, so $[\alpha\wedge\alpha] = -[\alpha\wedge\alpha]$ and hence $[\alpha\wedge\alpha] = 0$. (For $p$ odd the same computation gives $[\alpha\wedge\alpha] = [\alpha\wedge\alpha]$, no constraint — consistent with the nonzero $1$-form example.) Second, $\operatorname{tr}[A\wedge B] = 0$ for matrix-valued $1$-forms: from $[A\wedge B] = A\wedge B + B\wedge A$ and the fact that $\operatorname{tr}(B\wedge A) = \sum_{i,j}B_{ij}\wedge A_{ji} = \sum_{i,j}A_{ji}\wedge B_{ij}\cdot(-1)^{1\cdot1} = -\operatorname{tr}(A\wedge B)$ (relabel $i\leftrightarrow j$ and use graded-commutativity of the scalar wedge on $1$-forms), we get $\operatorname{tr}[A\wedge B] = \operatorname{tr}(A\wedge B) + \operatorname{tr}(B\wedge A) = 0$. This is the reason the trace of a commutator term drops out of Chern–Weil integrands. A reader who can reproduce these two computations, and who can say why the odd-degree self-bracket is *not* forced to vanish, has understood the definition.

---

# Unlocked by This

> [!tip] The structure equation and the curvature $2$-form *(from Gauge Theory IV, §4.3)*
> With the bracket in hand, the curvature of a principal connection $\omega\in\Omega^1(P;\mathfrak{g})$ is $\Omega = d\omega + \tfrac12[\omega\wedge\omega]$, and locally $F_\alpha = dA_\alpha + \tfrac12[A_\alpha\wedge A_\alpha]$. The factor $\tfrac12$ is there exactly to cancel the $2$ in $[\omega\wedge\omega](X,Y) = 2[\omega(X),\omega(Y)]$. See **[[Def - Curvature of a Principal Connection]]** and **[[Thm - Structure Equation for the Curvature]]**.

> [!tip] The Maurer–Cartan equation *(from Gauge Theory IV, §4.1)*
> The left Maurer–Cartan form $\theta\in\Omega^1(G;\mathfrak{g})$ satisfies $d\theta + \tfrac12[\theta\wedge\theta] = 0$; for matrix groups this is $d(g^{-1}dg) = -\,g^{-1}dg\wedge g^{-1}dg$, the matrix identity $[A\wedge A] = 2A\wedge A$ turning the $\tfrac12$-bracket into a plain wedge square. See **[[Def - The Maurer-Cartan Form]]** and **[[Thm - The Maurer-Cartan Equation]]**.

> [!tip] The Bianchi identity *(from Gauge Theory IV, §4.3)*
> The graded Jacobi identity for the bracket of $\mathfrak{g}$-valued forms is what makes the Bianchi identity $dF_\alpha + [A_\alpha\wedge F_\alpha] = 0$ hold; differentiating a structure equation produces a Jacobi identity. See **[[Thm - Bianchi Identity for a Principal Connection]]**.

> [!tip] Coupling matter fields *(from Gauge Theory IV, §4.4 and Gauge Theory VII)*
> The wedge-action $\rho_*(A)\wedge\phi$ and the notation $a\cdot\hat{s}$ are how a connection differentiates sections of an associated bundle: the induced covariant derivative is $d + \rho_*(A)\wedge$. See **[[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]]**.
