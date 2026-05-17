---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - Differential Form"
  - "Def - The Wedge Product"
  - "Def - Partial Derivatives and the Jacobian Matrix"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $\Omega \subseteq \mathbb{R}^n$ is open with coordinates $x = (x_1, \dots, x_n)$, and $\partial_\ell = \partial/\partial x_\ell$. Forms are $\alpha, \beta, \omega$; $\Lambda^k(\Omega)$ is the space of smooth $k$-forms; $df = \sum_\ell(\partial_\ell f)\,dx_\ell$ is the differential of a function $f$. The wedge product is $\wedge$. The operator $\wedge_\ell$ denotes "wedge $dx_\ell$ on the left". A form $\alpha$ is **closed** if $d\alpha = 0$ and **exact** if $\alpha = d\beta$ for some $\beta$. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Axiom Motivation

We have forms — invariant integrands — and a way to multiply them. The theory is still inert: nothing *happens*. The Fundamental Theorem of Calculus suggests what is missing. In one variable, the theorem connects a function to its derivative across a boundary; the entire calculus of forms will rest on a higher-dimensional version, and for that we need a notion of *derivative of a form*. The exterior derivative $d$ is that notion, and it can be invented by listing what it must do.

It must extend the differential of a function. A $0$-form is a function $f$, and its natural derivative is the $1$-form $df = \sum_\ell(\partial_\ell f)\,dx_\ell$ — the object whose line integral recovers $f$ across endpoints, by the chain rule. So $d$ on degree $0$ is already determined: it is the differential. The question is how to extend it to all degrees so that $d : \Lambda^k \to \Lambda^{k+1}$ raises degree by one.

It must be linear, and it must satisfy a product rule — because differentiation is, by its nature, a derivation. But the product here is the wedge, which carries signs, so the product rule must carry signs too. The right form is the *graded* Leibniz rule, $d(\alpha\wedge\beta) = d\alpha\wedge\beta + (-1)^k\alpha\wedge d\beta$ for $\alpha$ of degree $k$: the sign $(-1)^k$ is the cost of sliding the degree-raising operator $d$ past the $k$ factors of $\alpha$. Linearity plus the Leibniz rule plus the value on $0$-forms plus one more condition determine $d$ completely. The last condition is the deepest, and it is what makes the whole theory work.

That condition is $d \circ d = 0$. Why demand it? Because it is the abstract shadow of a fact you already know: mixed partial derivatives commute. Apply $d$ to a function twice and you get $d(df) = d\big(\sum_\ell\partial_\ell f\,dx_\ell\big) = \sum_{\ell, m}\partial_m\partial_\ell f\,dx_m\wedge dx_\ell$. The coefficient $\partial_m\partial_\ell f$ is *symmetric* in $m$ and $\ell$ (Schwarz's theorem on mixed partials), while the basic form $dx_m\wedge dx_\ell$ is *antisymmetric* in $m$ and $\ell$. A symmetric thing summed against an antisymmetric thing is zero — the contributions of $(m, \ell)$ and $(\ell, m)$ cancel in pairs. So $d(df) = 0$ is *automatic*, not an extra axiom; it is the equality of mixed partials, dressed in the antisymmetry of the wedge. The exterior derivative is built so that the symmetry of second derivatives and the antisymmetry of forms collide and annihilate.

What does demanding $d^2 = 0$ buy us? Everything downstream. It makes "exact $\Rightarrow$ closed" a triviality: if $\alpha = d\beta$ then $d\alpha = d(d\beta) = 0$. It is the homogeneous Maxwell equation. It is the vector-calculus identities $\operatorname{curl}\operatorname{grad} = 0$ and $\operatorname{div}\operatorname{curl} = 0$ — both are $d^2 = 0$ in degrees $0$ and $1$. And it is what makes the de Rham complex a *complex* — the property "image of one $d$ sits inside kernel of the next" — without which cohomology could not be defined. What breaks if we drop it? Then $d$ would not deserve to be called a derivative: there would be no notion of closed-versus-exact, no Stokes-compatible structure, no connection to the topology of the domain. The single equation $d^2 = 0$ is the spine of the subject.

One last requirement, and it is what distinguishes $d$ from every other conceivable degree-raising operator: $d$ must commute with pullback, $d(F^*\alpha) = F^*(d\alpha)$. This says $d$ does not depend on the coordinate system — it is the *same* operator no matter how you parametrize. An operator defined by a coordinate formula but not commuting with coordinate changes would be useless for invariant integration. It is a theorem (not an axiom) that the $d$ defined by the formula below does commute with pullback; that theorem is what certifies $d$ is geometrically meaningful.

---

# The Definition

Let $\Omega \subseteq \mathbb{R}^n$ be open. The **exterior derivative** is the linear operator
$$d : \Lambda^k(\Omega) \longrightarrow \Lambda^{k+1}(\Omega), \qquad 0 \le k \le n-1,$$
defined as follows. For a $k$-form $\alpha = \sum_j a_j(x)\,dx_{j_1}\wedge\cdots\wedge dx_{j_k}$,
$$d\alpha = \sum_{j}\sum_{\ell=1}^{n} \frac{\partial a_j}{\partial x_\ell}\; dx_\ell \wedge dx_{j_1}\wedge\cdots\wedge dx_{j_k}.$$
On a $0$-form (a function) $f$, this reads $df = \sum_\ell(\partial f/\partial x_\ell)\,dx_\ell$, the ordinary differential. On forms of degree $n$, $d$ is the zero map (there are no $(n+1)$-forms). Compactly, $d = \sum_\ell \partial_\ell \circ \wedge_\ell$ where $\wedge_\ell\alpha = dx_\ell\wedge\alpha$.

The exterior derivative is the *unique* linear operator $d : \Lambda^k(\Omega)\to\Lambda^{k+1}(\Omega)$, for all $k$, satisfying:

1. **(Differential on functions.)** On $0$-forms, $df = \sum_\ell(\partial_\ell f)\,dx_\ell$.
2. **(Graded Leibniz rule.)** For $\alpha\in\Lambda^k(\Omega)$ and $\beta\in\Lambda^j(\Omega)$,
$$d(\alpha\wedge\beta) = (d\alpha)\wedge\beta + (-1)^k\,\alpha\wedge(d\beta).$$
3. **(Nilpotence.)** $d(d\alpha) = 0$ for every form $\alpha$.

**Closed and exact.** A form $\alpha$ is **closed** if $d\alpha = 0$, and **exact** if there exists a form $\beta$ with $\alpha = d\beta$. By property 3, every exact form is closed. The converse holds locally but not globally; see [[Thm - The Poincaré Lemma]].

**Naturality.** For any smooth map $F : O\to\Omega$ and any form $\alpha$ on $\Omega$,
$$d(F^*\alpha) = F^*(d\alpha),$$
where $F^*$ is the [[Def - Pullback of a Differential Form|pullback]]. This identity says $d$ is independent of the choice of coordinates.

**The three classical operators.** Under the identification of vector fields with forms in $\mathbb{R}^3$: $d$ on a $0$-form is the **gradient**; $d$ on a $1$-form $\sum F_j\,dx_j$ produces the $2$-form encoding the **curl** of $F$; $d$ on a $2$-form produces the $3$-form encoding the **divergence**. Thus grad, curl, div are $d$ in degrees $0, 1, 2$.

---

# Categorical Definition

The exterior derivative is the differential of the **de Rham cochain complex**. A cochain complex is a sequence of vector spaces connected by linear maps whose consecutive composites vanish; here the sequence is
$$\Lambda^0(\Omega) \xrightarrow{\;d\;} \Lambda^1(\Omega) \xrightarrow{\;d\;} \cdots \xrightarrow{\;d\;} \Lambda^n(\Omega),$$
and the property $d\circ d = 0$ is exactly the defining condition of a complex. The point of packaging $d$ this way is that a complex has *cohomology*: at each spot, the kernel of the outgoing $d$ (the closed forms) contains the image of the incoming $d$ (the exact forms), and the quotient $H^k = \ker d/\operatorname{im} d$ is a vector space measuring the failure of closed to be exact. This is **de Rham cohomology**, and the exterior derivative is the operator that makes it definable.

The naturality identity $d(F^*\alpha) = F^*(d\alpha)$ says that $d$ is a **natural transformation** between functors: the functor $\Omega\mapsto\Lambda^k(\Omega)$ and the functor $\Omega\mapsto\Lambda^{k+1}(\Omega)$ are connected by $d$, and naturality means $d$ commutes with the morphisms (pullbacks) of both functors. A reader unfamiliar with the terminology should read this as the strongest possible statement that $d$ is coordinate-independent: not merely "$d$ has a coordinate-free description" but "$d$ is the *same* operator in every coordinate system, compatibly with all smooth maps between domains at once".

---

# Relate to Other Fields / Compression

The exterior derivative is the universal generalization of the three operators of vector calculus, and the compression it achieves is dramatic: grad, curl, and div — three operators with three notations, three sets of identities, three product rules — are the *single* operator $d$, restricted to degrees $0$, $1$, $2$. The vector-calculus identities $\operatorname{curl}\operatorname{grad} = 0$ and $\operatorname{div}\operatorname{curl} = 0$ are both the *single* identity $d^2 = 0$. The product rules $\operatorname{grad}(fg)$, $\operatorname{curl}(fF)$, $\operatorname{div}(fF)$, $\operatorname{div}(F\times G)$ are all the *single* graded Leibniz rule. The reason the classical picture looked like a zoo is the dimension-three coincidence $\binom{3}{1} = \binom{3}{2} = 3$, which lets both $1$-forms and $2$-forms masquerade as vector fields; the masquerade hides the fact that there was only ever one operator.

There is also a bridge to the theory of partial differential equations and to physics. The exterior derivative is the prototype of a *first-order differential operator that is geometric* — defined without reference to a metric, depending only on the smooth structure. The Laplacian, by contrast, needs a metric. The split between the metric-free $d$ and the metric-dependent Hodge star $\star$ organizes a great deal of mathematical physics: Maxwell's equations are $dF = 0$ and $d\star F = J$, with the *topology* in the first equation and the *geometry* (the metric, hence the spacetime structure) in the second. Recognizing which facts need only $d$ and which need $\star$ is recognizing which facts are topological and which are geometric.

---

# Examples / Corollaries

**Is an instance — $d$ of a function is the gradient.** For $f(x, y, z) = x^2 y + z$, $df = 2xy\,dx + x^2\,dy + dz$. The coefficient triple $(2xy, x^2, 1)$ is exactly $\nabla f$. The differential of a $0$-form *is* the gradient, repackaged as a $1$-form.

**Is an instance — $d$ of a $1$-form in the plane.** For the $1$-form $\alpha = P(x,y)\,dx + Q(x,y)\,dy$ on $\mathbb{R}^2$, the formula gives $d\alpha = \partial_y P\,dy\wedge dx + \partial_x Q\,dx\wedge dy = (\partial_x Q - \partial_y P)\,dx\wedge dy$. The single coefficient $\partial_x Q - \partial_y P$ is the planar curl, and this $2$-form is precisely the integrand of [[Thm - Green's Theorem|Green's theorem]].

**Is an instance — $d$ of a $1$-form in space is the curl.** For $\varphi = F_1\,dx + F_2\,dy + F_3\,dz$ on $\mathbb{R}^3$, the exterior derivative is the $2$-form $d\varphi = (\partial_y F_3 - \partial_z F_2)\,dy\wedge dz + (\partial_z F_1 - \partial_x F_3)\,dz\wedge dx + (\partial_x F_2 - \partial_y F_1)\,dx\wedge dy$. The three coefficients are exactly the three components of $\operatorname{curl} F$. Applying $d$ once more, $d(d\varphi) = (\partial_x(\partial_y F_3 - \partial_z F_2) + \cdots)\,dx\wedge dy\wedge dz = (\operatorname{div}\operatorname{curl} F)\,dx\wedge dy\wedge dz$, and this is zero — the identity $\operatorname{div}\operatorname{curl} = 0$ is $d^2 = 0$.

**Is NOT an instance — partial differentiation alone is not $d$.** It is tempting to think $d$ "just differentiates the coefficients". It does, but the wedge-on of $dx_\ell$ is essential: without it, differentiating $a\,dx$ would give the meaningless $(\partial_x a)\,dx + (\partial_y a)\,dx$ rather than the $2$-form $(\partial_y a)\,dy\wedge dx$. The degree-raising wedge is what makes $d$ map $\Lambda^k$ to $\Lambda^{k+1}$, and it is what makes $d^2 = 0$ work via antisymmetry.

**Is NOT an instance — a closed form need not be exact.** The form $d\theta = (x\,dy - y\,dx)/(x^2+y^2)$ on the punctured plane satisfies $d(d\theta) = 0$ (it is closed) but is *not* $df$ for any globally-defined function $f$ on $\mathbb{R}^2\setminus\{0\}$. Closedness is necessary for exactness but not sufficient — the gap is the subject of [[Thm - The Poincaré Lemma]] and of [[Ex - A closed form that is not exact]]. This non-example is the warning that $d\alpha = 0$ does not let you write $\alpha = d\beta$ without knowing the domain.

**Corollary — exact implies closed.** If $\alpha = d\beta$ then $d\alpha = d(d\beta) = 0$. This is the cheapest and most-used consequence: it is the mandatory *first test* for exactness — compute $d\alpha$, and if it is nonzero, $\alpha$ is not exact and you are done.

**Corollary — the de Rham complex.** The maps $\Lambda^0\xrightarrow{d}\Lambda^1\xrightarrow{d}\cdots\xrightarrow{d}\Lambda^n$ satisfy $\operatorname{im}(d : \Lambda^{k-1}\to\Lambda^k) \subseteq \ker(d : \Lambda^k\to\Lambda^{k+1})$, because the composite of two consecutive $d$'s is zero. The quotient $\ker/\operatorname{im}$ in degree $k$ is the $k$-th de Rham cohomology group.

**Calibration check.** Compute $d$ of $\omega = x\,dy\wedge dz$ on $\mathbb{R}^3$ (answer: $dx\wedge dy\wedge dz$); verify $d(df) = 0$ for $f = xy$ by direct computation; check the graded Leibniz rule on $\alpha = x\,dx$, $\beta = y\,dy$; and confirm that $d$ of any $3$-form on $\mathbb{R}^3$ is zero. If you can also explain why $d^2 = 0$ is the equality of mixed partials, you have understood the operator.

---

# Unlocked by This

> [!tip] de Rham Cohomology *(from Algebraic Topology)*
> Because $d\circ d = 0$, the closed forms contain the exact forms, and the quotient $H^k_{\mathrm{dR}}(\Omega) = \{\text{closed }k\text{-forms}\}/\{\text{exact }k\text{-forms}\}$ is a vector space. It is a topological invariant: by de Rham's theorem it equals the singular cohomology of $\Omega$. The exterior derivative is the operator that makes this invariant exist.

> [!tip] Connections and Curvature *(from Differential Geometry)*
> The exterior derivative is the flat prototype of a **covariant exterior derivative** $d_\nabla$ on a vector bundle. There $d_\nabla\circ d_\nabla$ need *not* vanish; the obstruction is the **curvature** $2$-form. The whole of gauge theory and general relativity lives in the failure of $d^2 = 0$ to survive the passage from functions to bundle-valued forms.
