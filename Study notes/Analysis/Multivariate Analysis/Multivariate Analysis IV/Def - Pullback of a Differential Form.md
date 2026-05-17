---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - Differential Form"
  - "Def - The Wedge Product"
  - "Def - The Exterior Derivative"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - The Chain Rule"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $F : O \to \Omega$ is a smooth map between open sets, $O \subseteq \mathbb{R}^m$ with coordinates $y = (y_1, \dots, y_m)$ and $\Omega \subseteq \mathbb{R}^n$ with coordinates $x = (x_1, \dots, x_n)$. The components of $F$ are $F_1, \dots, F_n$, and $DF$ is the Jacobian matrix with entries $\partial F_j/\partial y_\ell$. A $k$-form on $\Omega$ is $\alpha$; its pullback is $F^*\alpha$, a $k$-form on $O$. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Axiom Motivation

A surface is almost never handed to us as a subset of space; it is handed to us as a *parametrization* — a map $\varphi$ from a flat parameter domain into space, with the surface as its image. To integrate a form over the surface, or to do any calculus on the surface at all, we must move the form from where it lives (on the surface, in the ambient space) to where we can compute (on the flat domain). The pullback is the operation that does this move. The motivation is to find the *right* way to transport a form along a map, and "right" will be pinned down by two non-negotiable demands.

The first demand: the transported form must reproduce the change-of-variables formula. If $\alpha$ is a top-degree $n$-form on $\Omega \subseteq \mathbb{R}^n$ and $F : O \to \Omega$ is a diffeomorphism, then $\int_\Omega\alpha$ should equal $\int_O(\text{transported }\alpha)$ — and the change-of-variables formula tells us the transported $n$-form must carry a factor of the Jacobian determinant $\det DF$. This is not a stylistic choice; the integral simply will not be invariant otherwise. So whatever the pullback is, on top-degree forms it must multiply by $\det DF$.

The second demand: the transported form must pair correctly with transported vectors. A $1$-form $\alpha$ at a point of $\Omega$ eats a tangent vector there and returns a number. A tangent vector to $O$ is pushed *forward* by $F$ — the derivative $DF$ sends it to a tangent vector in $\Omega$. So the pulled-back $1$-form $F^*\alpha$, to eat a vector $v$ in $O$, should first push $v$ forward by $DF$ and then feed the result to $\alpha$: $(F^*\alpha)(v) = \alpha(DF\cdot v)$. Notice the direction reversal. Vectors go *forward* along $F$; forms, being things that *eat* vectors, must go *backward*. This is why the operation is a *pull*-back. The reversal is forced: a form is a machine for evaluating on vectors, and to compose a machine on $\Omega$ with vectors from $O$ you must route the vectors to $\Omega$ first, which means the machine effectively moves to $O$ in the opposite direction.

These two demands determine the pullback uniquely, and they cohere beautifully. The recipe is: substitute $F$ into the coefficient functions, and replace each coordinate differential $dx_j$ by $dF_j = \sum_\ell(\partial F_j/\partial y_\ell)\,dy_\ell$ — which is exactly $d$ of the $j$-th component, the differential of "the $j$-th coordinate composed with $F$". The second demand is then visible directly: $dx_j$ eats a vector and returns its $j$-th component, so $F^*dx_j = dF_j$ eats a vector and returns the $j$-th component of $DF\cdot v$, which is the chain rule. And the first demand falls out: pulling back $dx_1\wedge\cdots\wedge dx_n$ wedges together the $n$ rows $dF_1, \dots, dF_n$, and by the [[Def - The Wedge Product|determinant identity for wedges]] the result carries exactly $\det DF$.

What breaks under a different definition? If you tried to transport forms *forward* (a "pushforward" of forms) you would fail immediately for non-invertible $F$ — you cannot push a form forward along a map that collapses dimensions, because you would not know which preimage's data to use. The pullback works for *every* smooth map, invertible or not, because pulling back only ever evaluates coefficients and the chain rule, never inverts anything. This universal applicability — pullback along any smooth map — is what makes it the structural operation of the theory and the reason the assignment "$\Omega \mapsto$ forms on $\Omega$" is a *contravariant* functor.

---

# The Definition

Let $F : O \to \Omega$ be a smooth map between open sets, $O \subseteq \mathbb{R}^m$, $\Omega \subseteq \mathbb{R}^n$. The **pullback** $F^*$ sends a $k$-form on $\Omega$ to a $k$-form on $O$, as follows.

**On $0$-forms.** For a function $f$ on $\Omega$, $F^*f = f \circ F$.

**On the coordinate $1$-forms.** $F^*dx_j = dF_j = \displaystyle\sum_{\ell=1}^{m}\frac{\partial F_j}{\partial y_\ell}\,dy_\ell.$

**On a general $k$-form.** For $\alpha = \sum_j a_j(x)\,dx_{j_1}\wedge\cdots\wedge dx_{j_k}$,
$$F^*\alpha = \sum_j a_j\big(F(y)\big)\;\big(F^*dx_{j_1}\big)\wedge\cdots\wedge\big(F^*dx_{j_k}\big),$$
the wedge products being expanded by the algebra of [[Def - The Wedge Product|wedge products]]. Equivalently, on vector fields: if $F$ is a diffeomorphism and $F_\#X$ denotes the pushforward of a vector field, $(F^*\alpha)(F_\#X_1, \dots, F_\#X_k) = \alpha(X_1, \dots, X_k)\circ F$; for general smooth $F$, $(F^*\alpha)_y(v_1, \dots, v_k) = \alpha_{F(y)}(DF\cdot v_1, \dots, DF\cdot v_k)$.

The pullback satisfies the following identities, valid for all smooth maps and all forms.

1. **(Wedge.)** $F^*(\alpha\wedge\beta) = (F^*\alpha)\wedge(F^*\beta)$ — pullback is an algebra homomorphism.
2. **(Composition / contravariance.)** $(F\circ G)^*\alpha = G^*(F^*\alpha)$ — pullback reverses composition.
3. **(Commutes with $d$.)** $F^*(d\alpha) = d(F^*\alpha)$ — pullback commutes with the [[Def - The Exterior Derivative|exterior derivative]].
4. **(Top-degree / Jacobian.)** If $m = n$ and $\alpha = A(x)\,dx_1\wedge\cdots\wedge dx_n$, then
$$F^*\alpha = A\big(F(y)\big)\,\big(\det DF(y)\big)\;dy_1\wedge\cdots\wedge dy_n.$$
5. **(Change of variables.)** If $F : O\to\Omega$ is a diffeomorphism with $\det DF > 0$, then $\displaystyle\int_\Omega\alpha = \int_O F^*\alpha$ for any $n$-form $\alpha$.

---

# Categorical Definition

The pullback is what makes the calculus of differential forms a **contravariant functor**. A functor is an assignment that sends objects to objects and arrows to arrows, compatibly with composition. Here the objects are open sets (and, more generally, smooth manifolds), the arrows are smooth maps, and the functor sends an open set $\Omega$ to the algebra $\Lambda^\bullet(\Omega)$ of forms on it. *Contravariant* means the functor reverses arrows: a smooth map $F : O\to\Omega$ is sent not to a map $\Lambda^\bullet(O)\to\Lambda^\bullet(\Omega)$ but to the *backward* map $F^* : \Lambda^\bullet(\Omega)\to\Lambda^\bullet(O)$. Identity 2, $(F\circ G)^* = G^*\circ F^*$, is precisely the statement that $F^*$ respects composition with the order reversed — the defining law of a contravariant functor.

Identities 1 and 3 say the pullback is more than a functor on vector spaces: it is a functor into the category of **differential graded algebras**. The forms on $\Omega$ carry a multiplication (the wedge) and a differential (the exterior derivative); $F^*$ preserves both. This is the strongest possible sense in which "calculus of forms" is coordinate-independent — every structure of the theory (wedge, $d$, integration up to orientation) is transported by pullback with no choices and no corrections.

---

# Relate to Other Fields / Compression

The pullback is the change-of-variables formula, promoted from a theorem about integrals to an algebraic operation. In [[Multivariate Analysis III — Integration in Several Variables]] the [[Thm - The Change of Variables Formula|change of variables formula]] is proved as a substantial theorem about Riemann integrals: $\int_\Omega f = \int_O(f\circ F)|\det DF|$. Identity 5 above shows that, for forms, this *is* the definition of pullback combined with the definition of the integral — the Jacobian factor $\det DF$ is produced automatically by identity 4, with no proof, because the wedge of the rows of $DF$ is the determinant. The theorem has been compressed into a one-line algebraic identity. The only residue is the sign: the integral of forms uses $\det DF$, not $|\det DF|$, which is why the integral of a form needs an *orientation* — see [[Def - Orientation and the Integral of a Form]].

In the language of tensor calculus, the pullback is the operation that transforms covariant tensors under a change of coordinates, and identity 3 — that $F^*$ commutes with $d$ — is the statement that the exterior derivative is a tensorial operation, the same in every chart. The "lower indices transform covariantly" rule of classical tensor analysis is identity (the pullback of $dx_j$ is $\sum_\ell(\partial F_j/\partial y_\ell)\,dy_\ell$, the classical transformation law for a covariant index) written without indices.

---

# Examples / Corollaries

**Is an instance — pulling back $dx$ under polar coordinates.** Let $F(r, \theta) = (r\cos\theta, r\sin\theta)$, so $F_1 = r\cos\theta$, $F_2 = r\sin\theta$. Then $F^*dx = dF_1 = \cos\theta\,dr - r\sin\theta\,d\theta$ and $F^*dy = dF_2 = \sin\theta\,dr + r\cos\theta\,d\theta$. Wedging, $F^*(dx\wedge dy) = (F^*dx)\wedge(F^*dy) = (\cos\theta\,dr - r\sin\theta\,d\theta)\wedge(\sin\theta\,dr + r\cos\theta\,d\theta) = r\cos^2\theta\,dr\wedge d\theta - r\sin^2\theta\,d\theta\wedge dr = r\,dr\wedge d\theta$. The coefficient $r$ is exactly the polar Jacobian $\det DF = r$, confirming identity 4 — and recovering the familiar $dx\,dy = r\,dr\,d\theta$.

**Is an instance — pullback of a $1$-form along a curve.** A curve is a map $\gamma : [a,b]\to\Omega$, and $\gamma^*\alpha$ for a $1$-form $\alpha = \sum a_j\,dx_j$ is the $1$-form $\sum_j a_j(\gamma(t))\,\gamma_j'(t)\,dt$ on the interval. The line integral $\int_\gamma\alpha$ is by definition $\int_{[a,b]}\gamma^*\alpha$ — pullback is the mechanism that turns a line integral into an ordinary one-variable integral.

**Is an instance — pullback commutes with $d$.** With $F(r,\theta) = (r\cos\theta, r\sin\theta)$ again, take the $0$-form $f(x,y) = x$. Then $F^*f = r\cos\theta$, and $d(F^*f) = \cos\theta\,dr - r\sin\theta\,d\theta$. On the other side, $df = dx$, and $F^*(df) = F^*dx = \cos\theta\,dr - r\sin\theta\,d\theta$. The two agree — identity 3 holds in this case, as it must.

**Is NOT an instance — forms cannot be pushed forward along a non-invertible map.** The projection $F(x,y) = x$ from $\mathbb{R}^2$ to $\mathbb{R}$ pulls back the $1$-form $dx$ on $\mathbb{R}$ to the $1$-form $dx$ on $\mathbb{R}^2$ — fine. But there is no way to *push* the $1$-form $dy$ on $\mathbb{R}^2$ *forward* to $\mathbb{R}$: the fibres of $F$ are vertical lines, and $dy$ takes different "values along the fibre" with no canonical choice. This is why the theory uses pullback, which works for *every* smooth map, and never a pushforward of forms.

**Is NOT an instance — pullback does not preserve degree-raising in the naive sense.** It is tempting to think $F^*$ might change the degree of a form when $\dim O \neq \dim\Omega$. It does not: $F^*$ always sends $k$-forms to $k$-forms. What can happen is that the pullback *vanishes* — if $\alpha$ is a $k$-form on $\Omega$ and $k > \dim O$, then $F^*\alpha = 0$ identically, because a $k$-form on a domain of dimension $< k$ is zero. For instance the volume form $dx\wedge dy\wedge dz$ of $\mathbb{R}^3$ pulls back to zero along any map from a $2$-dimensional domain.

**Corollary — invariance of $\int_M\omega$ under reparametrization.** Identity 5, together with identity 2, is exactly what proves that the integral $\int_M\omega$ of a form over a surface does not depend on the chosen parametrization, provided orientations match. If $\varphi$ and $\psi$ are two charts and $F = \psi^{-1}\circ\varphi$ the transition diffeomorphism, then $\varphi^*\omega = F^*(\psi^*\omega)$ by identity 2, and identity 5 gives $\int\varphi^*\omega = \int\psi^*\omega$. The well-definedness of [[Def - Orientation and the Integral of a Form|the integral of a form]] rests entirely on the pullback identities.

**Calibration check.** Verify that $F^*dx_j = dF_j$ is the chain rule; compute $F^*(x\,dy)$ for $F(u,v) = (u^2, v)$ (answer: $u^2\,dv$); confirm $F^*(dx\wedge dy) = (\det DF)\,du\wedge dv$ for any $F : \mathbb{R}^2\to\mathbb{R}^2$; and check that pulling a $2$-form on $\mathbb{R}^3$ back along a curve $\gamma : \mathbb{R}\to\mathbb{R}^3$ gives zero. If you can also explain why pullback reverses the direction of composition, you have understood the operation.

---

# Unlocked by This

> [!tip] Naturality of the de Rham Complex *(from Algebraic Topology)*
> Because $F^*$ commutes with $d$, a smooth map $F : O\to\Omega$ induces a map on de Rham cohomology, $F^* : H^k_{\mathrm{dR}}(\Omega)\to H^k_{\mathrm{dR}}(O)$. Homotopic maps induce the same map on cohomology — the homotopy invariance of de Rham cohomology — which is the engine behind the [[Thm - The Poincaré Lemma|Poincaré lemma]] and the computation of cohomology in general.

> [!tip] Gauge Transformations *(from Electromagnetism / Gauge Theory)*
> The pullback is the mathematical content of a **change of gauge** or a **change of frame**. In gauge theory the connection and curvature forms transform by pullback under a change of local trivialization, and the physically meaningful quantities are exactly those invariant under all such pullbacks — a direct continuation of the principle that forms exist to make constructions coordinate-free.
