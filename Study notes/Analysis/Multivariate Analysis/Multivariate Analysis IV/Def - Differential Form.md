---
type: definition
subject: multivariate-analysis
prereqs:
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Def - The Riemann Integral in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Notation

Throughout, $\Omega$ is an open subset of $\mathbb{R}^n$ with coordinates $x = (x_1, \dots, x_n)$. A multi-index is an increasing tuple $j = (j_1, \dots, j_k)$ with $1 \le j_1 < \cdots < j_k \le n$; its length is $k$. The basic $k$-form associated to $j$ is written $dx_{j_1} \wedge \cdots \wedge dx_{j_k}$, abbreviated $dx_j$. The space of smooth $k$-forms on $\Omega$ is $\Lambda^k(\Omega)$, and $\Lambda^k\mathbb{R}^n$ denotes $k$-forms with constant coefficients. A vector field is written $X = \sum_j b_j(x)\,\partial/\partial x_j$; the symbol $D_j = \partial/\partial x_j$. The Euclidean inner product is $\langle\cdot,\cdot\rangle$, and $\operatorname{sgn}\sigma$ is the sign of a permutation $\sigma$. The full symbol registry is on [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem]].

---

# Axiom Motivation

We want to invent the right notion of an "integrand" — the kind of object that can sit under an integral sign on a curved $k$-dimensional surface. The naive answer, "a function", fails the moment you ask the only question that matters: is the integral independent of how the surface was parametrized? Push the question and the definition of a differential form will be forced.

Begin with a curve. To integrate the work done by a vector field $F$ along a curve $\gamma : [a,b] \to \Omega$, you write $\int_a^b F(\gamma(t)) \cdot \gamma'(t)\,dt$. Now reparametrize: replace $\gamma$ by $\gamma \circ \psi$ for some monotone change of parameter $\psi$. The chain rule supplies a factor $\psi'$, and the one-variable change-of-variables formula absorbs it, leaving the integral unchanged — *provided* $\psi$ preserves direction. If $\psi$ reverses direction, the integral changes sign. So the object being integrated along a curve is not a function of position alone; it is something that pairs with the *velocity vector* $\gamma'(t)$ and is *linear* in that vector, so that the chain-rule factor $\psi'$ can be pulled out and cancelled by change of variables. That object is a $1$-form: at each point it is a linear map eating one tangent vector.

Now go up a dimension. To integrate over a $k$-surface you parametrize by $\varphi : O \to \Omega$ with $O \subseteq \mathbb{R}^k$, and the surface's infinitesimal $k$-dimensional element is the parallelepiped spanned by the $k$ partial-derivative vectors $\partial\varphi/\partial x_1, \dots, \partial\varphi/\partial x_k$. Reparametrize by a diffeomorphism, and the chain rule now produces not a scalar factor but a whole Jacobian matrix; the change-of-variables formula will cancel it only if what cancels it is the *determinant* of that matrix. So the integrand must pair with $k$ tangent vectors and produce a number that behaves like a determinant in those vectors. A determinant is multilinear and *alternating* — it changes sign when two arguments are swapped and vanishes when two arguments coincide. This is the desideratum: the integrand for a $k$-surface must be, at each point, an **alternating $k$-linear map** on tangent vectors. That is the definition of a $k$-form, and it has been reverse-engineered from the single demand that the integral not depend on the parametrization.

Why exactly *alternating*, and not merely multilinear? Because a non-alternating multilinear integrand would pick up the *full* Jacobian matrix under reparametrization, and there is no change-of-variables formula that cancels a matrix — only one that cancels its determinant. Alternation is precisely the condition that collapses the matrix to its determinant. Drop alternation and you lose invariance; that is what breaks if the definition is weakened. Strengthen it the other way — demand, say, that the integrand be a *symmetric* $k$-linear map — and you have built the integrand for a different kind of geometry (a metric, a quadratic form), one whose integral is *not* parametrization-invariant in the orientation-sensitive way we need. The alternating condition is the unique sweet spot.

One more design choice: why insist on smoothness of the coefficients, and why allow the form to *vary* with position? The variation is non-negotiable — the field $F$ in the work integral depends on where you are, so the integrand must too; a form is a *field* of alternating maps, one at each point. Smoothness is what makes the exterior derivative (the operation that takes the whole theory off the ground) well-defined and what makes the algebraic identities — most importantly $d \circ d = 0$ — hold, since that identity is the equality of mixed partials and needs the coefficients to be twice differentiable. A $0$-form, by the way, is just a smooth function: it pairs with zero tangent vectors and is integrated over a $0$-dimensional surface (a point), where "integration" is evaluation. The whole tower $\Lambda^0, \Lambda^1, \dots, \Lambda^n$ is one idea — invariant integrands — indexed by the dimension of the thing they integrate over.

---

# The Definition

Let $\Omega \subseteq \mathbb{R}^n$ be open. A **differential $k$-form** on $\Omega$ (for $0 \le k \le n$) is a smooth map $\alpha$ assigning to each point $x \in \Omega$ an **alternating $k$-linear map**
$$\alpha_x : \underbrace{\mathbb{R}^n \times \cdots \times \mathbb{R}^n}_{k} \longrightarrow \mathbb{R},$$
where "alternating" means that swapping any two arguments reverses the sign:
$$\alpha_x(v_1, \dots, v_i, \dots, v_\ell, \dots, v_k) = -\,\alpha_x(v_1, \dots, v_\ell, \dots, v_i, \dots, v_k).$$
Equivalently, viewing forms as multilinear maps on vector fields, $\alpha(X_1, \dots, X_k)$ is a smooth function on $\Omega$, antisymmetric in the $X_i$. A $0$-form is a smooth function $\Omega \to \mathbb{R}$.

**Coordinate expression.** Let $D_j = \partial/\partial x_j$ denote the standard basis vector fields. For each increasing multi-index $j = (j_1, \dots, j_k)$ set $a_j(x) = \alpha_x(D_{j_1}, \dots, D_{j_k})$. Then $\alpha$ is determined by its coefficients $a_j$, and one writes
$$\alpha = \sum_{j_1 < \cdots < j_k} a_j(x)\; dx_{j_1} \wedge \cdots \wedge dx_{j_k},$$
where the basic form $dx_{j_1} \wedge \cdots \wedge dx_{j_k}$ is the alternating $k$-linear map sending $(v_1, \dots, v_k)$ to the determinant of the $k \times k$ matrix whose $(\ell, m)$ entry is the $j_\ell$-th component of $v_m$. The symbol $dx_i$ alone is the $1$-form picking out the $i$-th component of a vector. Under reordering, the basic forms obey
$$dx_{j_1} \wedge \cdots \wedge dx_{j_k} = (\operatorname{sgn}\sigma)\; dx_{j_{\sigma(1)}} \wedge \cdots \wedge dx_{j_{\sigma(k)}},$$
and any basic form with a repeated index is zero. The set $\Lambda^k(\Omega)$ of all smooth $k$-forms on $\Omega$ is a vector space (a module over smooth functions); the constant-coefficient $k$-forms $\Lambda^k\mathbb{R}^n$ form a vector space of dimension $\binom{n}{k}$.

**Integration of a $1$-form over a curve.** For a $1$-form $\alpha = \sum_j a_j(x)\,dx_j$ and a smooth curve $\gamma : [a,b] \to \Omega$,
$$\int_\gamma \alpha = \int_a^b \sum_j a_j(\gamma(t))\,\gamma_j'(t)\;dt.$$
The general integral $\int_M\omega$ of a $k$-form over a $k$-surface is given in [[Def - Orientation and the Integral of a Form]].

---

# Categorical Definition

The differential $k$-forms on $\Omega$ are the smooth sections of the **$k$-th exterior power of the cotangent bundle**, $\Lambda^k T^*\Omega$. Unpacking this for a reader who has not met bundles: at each point $x$, the tangent space is $T_x\Omega \cong \mathbb{R}^n$, and its dual $T_x^*\Omega$ is the space of linear functionals on tangent vectors — these are the *covectors*, and a smooth field of them is a $1$-form. The exterior power $\Lambda^k$ is the universal construction that turns a vector space $V$ into the vector space $\Lambda^k V$ of formal alternating products: it is characterized by a universal property — every alternating $k$-linear map out of $V$ factors uniquely through the canonical alternating map $V^k \to \Lambda^k V$. A $k$-form is then a smooth choice, at each point, of an element of $\Lambda^k(T_x^*\Omega)$.

The deeper categorical fact is that the assignment $\Omega \mapsto \Lambda^k(\Omega)$ is a **contravariant functor**: a smooth map $F : O \to \Omega$ induces, *backward*, a linear map $F^* : \Lambda^k(\Omega) \to \Lambda^k(O)$, the [[Def - Pullback of a Differential Form|pullback]], respecting composition. Contravariance — the reversal of arrows — is not a quirk; it is the reason forms are the natural integrands. A surface is presented as a map *into* space; to integrate something *on* the surface you must pull the integrand *back* along that map, against the direction of the arrow. Forms are exactly the objects that transform contravariantly, which is what makes "integrate on the parametrized surface" well-posed.

---

# Relate to Other Fields / Compression

A differential form is the geometric analogue of a tensor with all indices down and fully antisymmetrized — it is the **antisymmetric covariant tensor field**. In the index notation of tensor calculus, a $k$-form has components $a_{j_1 \cdots j_k}$ totally antisymmetric under permutation of indices, and the basic forms $dx_{j_1}\wedge\cdots\wedge dx_{j_k}$ are the antisymmetrized tensor products $dx_{j_1}\otimes\cdots\otimes dx_{j_k}$. The reason forms, rather than general tensors, are the objects that get integrated is that integration is intrinsically alternating: the orientation of the integration domain is a sign, and only a fully antisymmetric integrand interacts correctly with that sign.

In the language of linear algebra alone, $\Lambda^k\mathbb{R}^n$ is the space of all alternating multilinear functions of $k$ vectors, and the single most important instance is $k = n$: $\Lambda^n\mathbb{R}^n$ is one-dimensional, spanned by $dx_1\wedge\cdots\wedge dx_n$, and that basic form *is* the determinant — it sends $n$ vectors to the signed volume of the parallelepiped they span. Every other statement about forms is, in this sense, a statement about determinants in disguise. A $1$-form is a covector field, the object dual to a vector field; the pairing of a $1$-form with a vector field is the natural evaluation of a linear functional on a vector, which is why a $1$-form is sometimes called a "covector field" or, in older physics texts, a "covariant vector".

---

# Examples / Corollaries

**Is an instance — the differential of a function.** For a smooth function $f$ on $\Omega$, its differential $df = \sum_j (\partial f/\partial x_j)\,dx_j$ is a $1$-form: at each point it is the linear map sending a vector $v$ to the directional derivative $\langle\nabla f, v\rangle$. This is the cleanest example, and it shows the symbols $dx_j$ are not mere notation — $dx_j$ is literally the differential of the $j$-th coordinate function. Every $0$-form (function) thus has a canonical $1$-form attached to it; the exterior derivative generalizes this to all degrees.

**Is an instance — the work form of a vector field.** Given a vector field $F = (F_1, \dots, F_n)$, the $1$-form $\varphi_F = \sum_j F_j(x)\,dx_j$ is the form whose line integral $\int_\gamma\varphi_F$ is the work of $F$ along $\gamma$. The correspondence $F \leftrightarrow \varphi_F$ between vector fields and $1$-forms is a bijection (it depends on the Euclidean inner product), and it is the dictionary by which vector calculus translates into the calculus of forms.

**Is an instance — the area form and the flux form in $\mathbb{R}^3$.** In $\mathbb{R}^3$ the $2$-form $dx\wedge dy$ measures signed area of the projection onto the $xy$-plane; more generally, given a vector field $G = (g_1, g_2, g_3)$, the $2$-form $g_1\,dy\wedge dz + g_2\,dz\wedge dx + g_3\,dx\wedge dy$ is the form whose integral over a surface is the flux of $G$ through it. That a $3$-component vector field corresponds to a $2$-form (rather than a $1$-form) is the coincidence $\binom{3}{1} = \binom{3}{2} = 3$ that makes vector calculus in $\mathbb{R}^3$ possible and that disappears in every other dimension.

**Is NOT an instance — a symmetric bilinear form.** The Euclidean metric, which assigns to two vectors $u, v$ the number $\langle u, v\rangle = \sum_j u_j v_j$, is a $2$-linear map on tangent vectors, but it is *symmetric*, not alternating: $\langle u, v\rangle = \langle v, u\rangle$. It is therefore not a $2$-form. It is a different kind of tensor — a metric tensor — and it is integrated in a different way (it produces lengths and areas, not signed fluxes). This non-example pins down that "alternating", not merely "multilinear", is the defining clause.

**Is NOT an instance — a $k$-form for $k > n$.** On $\Omega \subseteq \mathbb{R}^n$ there are no nonzero $k$-forms for $k > n$: an alternating $k$-linear map of more than $n$ vectors in $\mathbb{R}^n$ must vanish, because among $k > n$ vectors in an $n$-dimensional space two are necessarily linearly dependent, and an alternating map kills any linearly dependent tuple. Thus the tower $\Lambda^0(\Omega), \dots, \Lambda^n(\Omega)$ stops at degree $n$; this is why the de Rham complex has finite length.

**Corollary — counting components.** A $k$-form on $\mathbb{R}^n$ has exactly $\binom{n}{k}$ coefficient functions, one per increasing multi-index. In $\mathbb{R}^3$: $\binom{3}{0} = 1$ (functions), $\binom{3}{1} = 3$ ($1$-forms, like vector fields), $\binom{3}{2} = 3$ ($2$-forms, also like vector fields), $\binom{3}{3} = 1$ ($3$-forms, like functions). The palindrome $1, 3, 3, 1$ is the source of every "vector field" disguise in three-dimensional vector calculus.

**Calibration check.** Verify that $dx \wedge dx = 0$ directly from alternation; that $dx\wedge dy = -\,dy\wedge dx$; that a $1$-form on $\mathbb{R}^2$ has two components and a $2$-form on $\mathbb{R}^2$ has one; and that $df$ for $f(x,y) = x^2 y$ equals $2xy\,dx + x^2\,dy$. If you can also explain why no $3$-form exists on $\mathbb{R}^2$, you have understood every clause of the definition.

---

# Unlocked by This

> [!tip] The Volume Form *(from Riemannian Geometry)*
> A nowhere-vanishing $n$-form on an $n$-manifold is a **volume form**, and a choice of one is exactly a choice of orientation together with a notion of $n$-dimensional volume. On a Riemannian manifold the metric determines a canonical volume form $\sqrt{g}\,dx_1\wedge\cdots\wedge dx_n$, the object integrated to compute the volume of a region.

> [!tip] Symplectic Forms and Hamiltonian Mechanics *(from Geometric Mechanics)*
> A closed, nondegenerate $2$-form on a phase space is a **symplectic form**, the structure that turns a function (the Hamiltonian) into a flow. The whole of Hamiltonian mechanics is the geometry of a single $2$-form, and forms are the language in which Liouville's theorem (conservation of phase-space volume) becomes a one-line statement.
