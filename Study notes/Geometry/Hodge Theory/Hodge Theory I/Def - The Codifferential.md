---
type: definition
subject: hodge-theory
prereqs:
  - "Def - Exterior Derivative on a Manifold"
  - "Def - The Hodge Star Operator"
  - "Def - The L2 Inner Product on Differential Forms"
  - "Def - Riemannian Manifold"
tags: [geometry, hodge-theory, differential-forms]
---

# Notation

$(M, g)$ is a smooth oriented Riemannian $n$-manifold (or pseudo-Riemannian with signature $(n - s, s)$); we take $M$ closed (compact, without boundary) for the adjoint property to hold without boundary terms. The exterior derivative is $d : \Omega^k(M) \to \Omega^{k+1}(M)$; the Hodge star is $\star : \Omega^k(M) \to \Omega^{n-k}(M)$; the $L^2$ inner product is $\langle\cdot,\cdot\rangle = \langle\cdot,\cdot\rangle_{L^2}$. The codifferential is denoted $\delta$ or $d^*$ (we use $\delta$). The Levi-Civita connection is $\nabla$, with covariant derivative $\nabla_j$. The full notation registry is in [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

---

# Axiom Motivation

The exterior derivative $d : \Omega^k \to \Omega^{k+1}$ is the natural first-order differential operator on a smooth manifold; it raises degree by $1$. With a Riemannian metric we can construct an operator going the other way — lowering degree by $1$ — that is the natural $L^2$-adjoint of $d$. Three structural demands force the definition.

**Why an adjoint?** Many manipulations in PDE and variational calculus require integration by parts. On Euclidean $\mathbb{R}^n$, the basic identity is $\int (Du)v = -\int u (Dv)$ for compactly supported $u, v$, the analytic content of integration by parts. The forms analogue should be $\int_M d\alpha \wedge \star\beta = \pm\int_M \alpha\wedge d\star\beta + \text{boundary}$, derived from Stokes' theorem applied to $d(\alpha\wedge\star\beta)$. We seek an operator $d^*$ such that the boundary-free part reads $\langle d\alpha, \beta\rangle = \langle\alpha, d^*\beta\rangle$ — making $d^*$ the formal $L^2$-adjoint of $d$.

**Why $d^* = (-1)^{?}\star d\star$?** Compute. We have $\langle d\alpha, \beta\rangle_{L^2} = \int_M d\alpha\wedge\star\beta$ by the defining identity of $\star$. Now use the graded Leibniz rule for $d$ on the product $\alpha\wedge\star\beta$:
$$d(\alpha\wedge\star\beta) = d\alpha\wedge\star\beta + (-1)^{k-1}\alpha\wedge d\star\beta,$$
where $k - 1$ is the degree of $\alpha$ ($\alpha \in \Omega^{k-1}$, $\beta \in \Omega^k$). Integrating both sides and applying Stokes' theorem to the left side ($\int_M d(\alpha\wedge\star\beta) = 0$ on a closed manifold) gives
$$\langle d\alpha, \beta\rangle = -(-1)^{k-1}\int_M \alpha\wedge d\star\beta.$$
For the right side to be a wedge product whose star-conversion gives back an $L^2$ inner product, we need to write $\alpha\wedge d\star\beta = \alpha\wedge\star\star^{-1}d\star\beta$ and identify the result as $\langle\alpha,\star^{-1}d\star\beta\rangle_g\operatorname{vol}_n$. Since $\star^{-1}\omega = (-1)^{(k)(n-k)+s}\star\omega$ on $k$-forms (by the double-star formula), the desired operator $\delta\beta = \star^{-1}d\star\beta$ up to the overall sign, and the explicit sign tracking gives the standard formula.

**Why $\delta^2 = 0$?** This is forced by $d^2 = 0$: $\delta^2 = \pm\star d\star\star d\star = \pm\star d\,(\pm 1)\,d\star = \pm\star d^2\star = 0$. The $\pm$ signs are tracked carefully, but the inner $d^2$ kills the whole expression regardless. The vanishing of $\delta^2$ is the *dual* statement to $d^2 = 0$ — and it is what makes the Hodge Laplacian $\Delta = d\delta + \delta d$ symmetric: $\Delta = (d + \delta)^2 - 2(\delta d + d\delta)$… no, more simply: $\Delta^2 \neq 0$, but the cross-terms in $(d + \delta)^2 = d^2 + d\delta + \delta d + \delta^2 = d\delta + \delta d = \Delta$ vanish, so $\Delta = (d + \delta)^2$, making $\Delta$ a square of a first-order operator.

**Why the sign $(-1)^{n(k+1)+1}$ on Riemannian manifolds?** This is the unique sign that makes the adjoint identity $\langle d\alpha,\beta\rangle = \langle\alpha,\delta\beta\rangle$ hold without a sign. The computation: rewriting $\alpha\wedge d\star\beta$ requires shuffling $\alpha$ (degree $k - 1$) past $d\star\beta$ (degree $n - k + 1$), which costs $(-1)^{(k-1)(n-k+1)}$ in graded commutativity; combined with the leading $-(-1)^{k-1}$ from Stokes and the sign from $\star\star^{-1}$, the net result is $(-1)^{n(k+1) + 1}$, the standard formula. The detailed sign tracking is unedifying, and the operational content is just "the unique sign making $\delta$ the adjoint of $d$."

**Why the convention varies.** Some authors (e.g., Lee) define $\delta$ with the opposite overall sign, making $\delta = -d^*$ in our convention. The choice does not affect the Hodge Laplacian $\Delta = d\delta + \delta d$ (since $\delta$ appears bilinearly), nor harmonicity ($\delta\omega = 0 \iff -\delta\omega = 0$), so the two conventions are interconvertible by a sign flip. Frankel and Warner use our sign convention.

**What if we strengthen — demand $\delta$ commute with isometries?** It does, by construction. The Hodge star commutes with orientation-preserving isometries; the exterior derivative commutes with all smooth maps via pullback. So $\delta = \pm\star d\star$ commutes with orientation-preserving isometries, which is exactly the equivariance we want.

---

# The Definition

Let $(M, g)$ be a smooth oriented (pseudo-)Riemannian $n$-manifold. The **codifferential** (or **adjoint exterior derivative**, sometimes written $d^*$) is the operator $\delta : \Omega^k(M) \to \Omega^{k-1}(M)$ defined by
$$\delta = \begin{cases} (-1)^{n(k+1) + 1}\,\star d\star & \text{Riemannian case}, \\ (-1)^{n(k+1)}\,\star d\star & \text{pseudo-Riemannian case (sign by signature)}, \end{cases}$$
acting on $k$-forms. By convention, $\delta : \Omega^0(M) \to \Omega^{-1}(M) = 0$ is the zero map; equivalently, $\delta f = 0$ for any function $f$.

**Equivalent form.** Using $\star\star = (-1)^{k(n-k)+s}$, the formula can be rewritten as $\delta = -\star^{-1}d\star = -(\star\star)^{-1}\star d\star$, giving the cleaner-looking but sign-variable identity.

**$\delta^2 = 0$.** The codifferential squares to zero: $\delta^2 = \pm\star d\star\star d\star = \pm\star d^2 \star \cdot (\text{double-star sign}) = 0$, because $d^2 = 0$.

**$L^2$ adjoint property.** On a closed oriented Riemannian manifold $M$, for any $\alpha \in \Omega^{k-1}(M)$ and $\beta \in \Omega^k(M)$,
$$\langle d\alpha, \beta\rangle_{L^2} = \langle\alpha, \delta\beta\rangle_{L^2}.$$
On a compact Riemannian manifold with boundary $\partial M$, the same identity acquires a boundary correction:
$$\langle d\alpha, \beta\rangle_{L^2} - \langle\alpha, \delta\beta\rangle_{L^2} = \int_{\partial M}\alpha\wedge\star\beta.$$

**Coordinate formula.** In local coordinates $(x^i)$ on a Riemannian manifold with metric $g_{ij}$, the codifferential of a $k$-form $\beta = \beta_{i_1\cdots i_k} dx^{i_1}\wedge\cdots\wedge dx^{i_k}/k!$ has components
$$(\delta\beta)_{i_1\cdots i_{k-1}} = -\nabla^j\beta_{j i_1\cdots i_{k-1}} = -\frac{1}{\sqrt{|g|}}\partial_j(\sqrt{|g|}\,\beta^{j i_1\cdots i_{k-1}}).$$
On $1$-forms $\beta = \beta_i dx^i$, $\delta\beta = -\nabla^i\beta_i = -g^{ij}\nabla_i\beta_j$, which is the negative of the divergence of the vector field dual to $\beta$. The name "**codifferential**" reflects this: $\delta$ is the form-version of the divergence, dual to $d$ which is the form-version of the gradient/curl.

---

# Relate to Other Fields / Compression

**The codifferential is the form-version of the divergence on vector fields.** For a vector field $X = X^i\partial_i$ with metric dual $1$-form $X^\flat = g_{ij}X^j dx^i$, the divergence is $\operatorname{div} X = \nabla_i X^i = \frac{1}{\sqrt{|g|}}\partial_i(\sqrt{|g|}X^i)$, and $\delta X^\flat = -\operatorname{div} X$. So the codifferential on $1$-forms recovers (the negative of) the Riemannian divergence on vector fields, with the negative sign tracking the convention $\delta = -\star^{-1}d\star + \text{signs}$.

**The Laplace–Beltrami operator on functions is $-\delta d$.** For a function $f \in C^\infty(M) = \Omega^0(M)$, $df$ is a $1$-form, $\delta(df) = -\nabla^i\partial_i f = -\nabla^2 f$ is the negative Laplace–Beltrami of $f$. So the Hodge Laplacian on functions is $\Delta f = d\delta f + \delta d f = 0 + \delta df = -\nabla^2 f$. The negative sign is what makes $\Delta$ a *nonnegative* operator (with positive eigenvalues), whereas $\nabla^2$ on Euclidean space is a *negative* operator with negative eigenvalues.

**True name:** the codifferential is the *unique* differential operator $\Omega^k \to \Omega^{k-1}$ that is the formal $L^2$-adjoint of $d$ on a closed Riemannian manifold. The explicit formula $\delta = \pm\star d\star$ is a *derivation*: one can prove that any operator with the adjoint property must be given by this formula, by computing how $d$ interacts with $\star$ through the integration-by-parts identity. The Hodge star is the necessary intermediary because $\Omega^k$ and $\Omega^{k-1}$ are different spaces; without $\star$, there is no canonical way to convert "differentiate, raising degree" into "differentiate, lowering degree" via the metric.

---

# Examples / Corollaries

**Is an instance: codifferential on functions vanishes.** $\delta : \Omega^0(M) \to \Omega^{-1}(M) = 0$. So $\delta f = 0$ for any function $f$. This is consistent with the adjoint identity: $\langle df, \alpha\rangle = \langle f, \delta\alpha\rangle$ for $1$-forms $\alpha$, and "no $\delta$ on $\Omega^{-1}$" is the dual statement to "no $d$ from $\Omega^{n+1}$."

**Is an instance: codifferential of a $1$-form on $\mathbb{R}^3$.** For $\beta = a\,dx + b\,dy + c\,dz$ on Euclidean $\mathbb{R}^3$, $\star\beta = a\,dy\wedge dz + b\,dz\wedge dx + c\,dx\wedge dy$, $d\star\beta = (\partial_x a + \partial_y b + \partial_z c)\,dx\wedge dy\wedge dz$, $\star d\star\beta = \partial_x a + \partial_y b + \partial_z c$ (a function), and finally $\delta\beta = -(\partial_x a + \partial_y b + \partial_z c)$. So $\delta$ on a $1$-form is the negative divergence of the dual vector field — confirming the formula above.

**Is an instance: codifferential of a $2$-form on $\mathbb{R}^3$.** For $\eta = p\,dx\wedge dy + q\,dy\wedge dz + r\,dz\wedge dx$, $\star\eta = p\,dz + q\,dx + r\,dy$, $d\star\eta = (\partial_y r - \partial_z q)\,dy\wedge dz + (\partial_z p - \partial_x r)\,dz\wedge dx + (\partial_x q - \partial_y p)\,dx\wedge dy$, and applying $\star$ once more (with the appropriate sign) gives a $1$-form whose components are essentially the curl of $(q, r, p)$. So $\delta$ on $2$-forms in $\mathbb{R}^3$ is the curl-like operator, again with a sign.

**Is NOT an instance: a "codifferential" on a manifold without a metric.** Without a Riemannian (or pseudo-Riemannian) metric, the Hodge star $\star$ does not exist, and so $\delta = \pm\star d\star$ has no meaning. On a bare smooth manifold, the only natural first-order operators on forms are $d$ and the contractions $\iota_X$ (interior products). There is no canonical degree-lowering operator. This is why Hodge theory is a *Riemannian* invariant, not a topological one — it uses the metric structure to introduce $\delta$, and the metric is exactly what is missing in pure de Rham theory.

**Corollary ($\delta^2 = 0$).** Direct calculation: $\delta^2\omega = \pm\star d\star\star d\star\omega = \pm\star d\,(\text{const})\,d\star\omega = \pm(\text{const})\star d^2\star\omega = 0$.

**Corollary ($\delta$ commutes with isometries).** For an orientation-preserving isometry $F : (M, g) \to (M, g)$, $F^*\delta = \delta F^*$. The proof: $F^*\star = \star F^*$ (since $F$ preserves $g$ and orientation), and $F^* d = d F^*$ (naturality of $d$), so $F^* \delta = F^*(\pm \star d\star) = \pm \star d\star F^* = \delta F^*$.

**Corollary (variational formulation).** The harmonic representative of a cohomology class is the minimizer of $\|\omega\|_{L^2}^2$ subject to $[\omega] = c$. Setting the first variation to zero on $\omega + d\eta$ gives $\langle\omega, d\eta\rangle = 0$ for all $\eta$, equivalently $\langle\delta\omega, \eta\rangle = 0$ for all $\eta$, equivalently $\delta\omega = 0$. So the variational equation is "coclosed", and the harmonic representative is closed-and-coclosed. This is the heart of Dirichlet's principle for Hodge theory.

**Calibration check.** If you can verify (i) $\delta$ on functions is zero (no degree below $0$), (ii) $\delta$ on a $1$-form on Euclidean $\mathbb{R}^3$ is the negative divergence, and (iii) $\delta^2 = 0$ from $d^2 = 0$ and the double-star formula, you have understood the operator correctly.

---

# Unlocked by This

> [!tip] The Hodge Laplacian as a Square *(from Functional Analysis)*
> The codifferential is what makes the **Hodge Laplacian** $\Delta = d\delta + \delta d$ a sum-of-squares: $\Delta = (d + \delta)^2$ (since the cross-terms $d^2 = 0 = \delta^2$ vanish, leaving only $d\delta + \delta d$). The operator $D = d + \delta : \Omega^\bullet(M) \to \Omega^\bullet(M)$ shifts degree by $\pm 1$ and is self-adjoint with respect to the $L^2$ inner product (since $d$ and $\delta$ are adjoints of each other). So $D$ is a *first-order* elliptic operator whose square is the Hodge Laplacian — this is the form-analogue of the Dirac operator on a spin manifold, and is the **signature operator** when restricted to even / odd forms.

> [!tip] The $L^2$-Adjoint of Differential Operators *(from PDE and Geometric Analysis)*
> The codifferential is the prototype for taking $L^2$-adjoints of differential operators on geometric vector bundles. For any first-order differential operator $D : \Gamma(E) \to \Gamma(F)$ between sections of two metric vector bundles on $M$, the formal adjoint $D^* : \Gamma(F) \to \Gamma(E)$ is defined by $\langle D\sigma, \tau\rangle_{L^2} = \langle\sigma, D^*\tau\rangle_{L^2}$ for compactly supported $\sigma, \tau$. The codifferential $\delta = d^*$ is the case $E = \Lambda^k T^*M$, $F = \Lambda^{k-1}T^*M$, $D = d$. The general construction gives rise to elliptic operators like the Dirac operator $D^* + D$ on spinors, and the entire theory of elliptic operators and index theory.
