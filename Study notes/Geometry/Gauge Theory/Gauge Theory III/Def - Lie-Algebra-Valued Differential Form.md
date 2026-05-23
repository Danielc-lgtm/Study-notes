---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - Vector Bundle"
tags: [geometry, gauge-theory, differential-forms, lie-algebras]
---

# Notation

Throughout, $M$ is a smooth manifold of dimension $n$ and $\mathfrak{g}$ is a fixed finite-dimensional real (or complex) Lie algebra — usually $\mathfrak{g} = T_e G$ for a Lie group $G$. $\Omega^p(M)$ denotes the space of ordinary smooth $p$-forms on $M$; $\Omega^p(M; \mathfrak{g})$ the space of $\mathfrak{g}$-valued $p$-forms. We use a basis $\{E_R\}_{R=1}^{\dim\mathfrak{g}}$ of $\mathfrak{g}$ with structure constants $[E_R, E_S] = C^T_{RS}E_T$ (Einstein summation throughout).

---

# Axiom Motivation

The starting point of gauge theory is that the gauge field is not a real-valued or vector-valued 1-form on spacetime — it is a 1-form valued in the Lie algebra $\mathfrak{g}$ of the gauge group. Why? Because the gauge group $G$ acts on the matter fields by linear transformations in some representation $V$, and the *infinitesimal* version of this — the data of a "small" gauge transformation at each point — is a $\mathfrak{g}$-valued function. Integrating an infinitesimal gauge transformation along a path requires evaluating $\mathfrak{g}$-valued 1-forms along tangent vectors; integrating to obtain the curvature requires $\mathfrak{g}$-valued 2-forms. The entire kinematic structure of gauge theory is built from $\mathfrak{g}$-valued differential forms on the base manifold (or the total space of a principal bundle), so we need a definition that captures them cleanly and that supports the standard operations of differential geometry: exterior derivative, wedge product, pullback under maps.

The cleanest definition is to take the tensor product. An ordinary $p$-form is an element of $\Omega^p(M) = \Gamma(\Lambda^p T^*M)$. To get a $\mathfrak{g}$-valued version, we tensor with $\mathfrak{g}$: 
$$
\Omega^p(M; \mathfrak{g}) := \Omega^p(M) \otimes_\mathbb{R} \mathfrak{g} = \Gamma(\Lambda^p T^*M \otimes (M \times \mathfrak{g})).
$$
The right-hand side is the space of smooth sections of the bundle $\Lambda^p T^*M \otimes (M \times \mathfrak{g})$ — antisymmetric multilinear maps from tangent vectors to $\mathfrak{g}$. The tensor product structure is what makes the definition operationally clean: every $\mathfrak{g}$-valued $p$-form decomposes uniquely as $\varphi = E_R \otimes \varphi^R$ where each $\varphi^R$ is an ordinary $p$-form and $\{E_R\}$ is a basis of $\mathfrak{g}$. The decomposition is the basis-component picture; the bundle-section picture is basis-free. Both are useful.

A natural alternative would be to define a $\mathfrak{g}$-valued $p$-form as a smooth map $\varphi : TM^{\oplus p} \to \mathfrak{g}$ that is alternating and $C^\infty(M)$-multilinear. This produces the same space — the universal property of the tensor product makes the two definitions equivalent — but it obscures the decomposition structure. We use the tensor-product definition as primary because it makes everything mechanical.

Why does the exterior derivative extend immediately? Because $\mathfrak{g}$ is a fixed vector space (not varying with $p \in M$), so the basis vectors $E_R$ are constant, and differentiation commutes with the tensor product: $d(E_R \otimes \varphi^R) := E_R \otimes d\varphi^R$. This is the right definition because it satisfies $d^2 = 0$ (inherited from ordinary $d^2 = 0$) and the graded Leibniz rule for wedge with ordinary forms (inherited from ordinary Leibniz). It does *not* satisfy the Leibniz rule for the bracket of $\mathfrak{g}$-valued forms in the naive way — the correct version is $d[\alpha, \beta] = [d\alpha, \beta] + (-1)^p [\alpha, d\beta]$, which is part of the [[Def - Bracket of g-Valued Forms|bracket definition]] not the exterior derivative.

What if we wanted to define a vector-bundle-valued form rather than a $\mathfrak{g}$-valued one? That generalisation is also natural — an $E$-valued $r$-form is a section of $\Lambda^r T^*M \otimes E$ — and gives the space $\Omega^r(M; E)$ used for sections of associated bundles in §3.4. The $\mathfrak{g}$-valued forms of this definition are the special case where $E = M \times \mathfrak{g}$ is the trivial bundle with fibre $\mathfrak{g}$. The genuinely $E$-valued forms (where $E$ is non-trivial) require a *connection* on $E$ to differentiate, since the basis sections of $E$ vary across $M$; the exterior covariant derivative $d_\nabla$ replaces $d$. See [[Def - Exterior Covariant Derivative on Associated Bundles]].

The test of a successful definition is: can we recover the standard structure of differential geometry, while accommodating the new $\mathfrak{g}$-value? The answer is yes — every operation (exterior derivative, pullback, wedge with ordinary forms, integration when paired against an $\mathfrak{g}^*$-valued form) extends linearly through the tensor product. The new operation needed for gauge theory — the *bracket* of two $\mathfrak{g}$-valued forms — is a separate definition (the next page).

---

# The Definition

A **$\mathfrak{g}$-valued differential $p$-form** on a smooth manifold $M$, where $\mathfrak{g}$ is a fixed finite-dimensional Lie algebra, is a smooth section of the vector bundle $\Lambda^p T^*M \otimes (M \times \mathfrak{g})$ over $M$. Equivalently, it is an element of the tensor product
$$
\Omega^p(M; \mathfrak{g}) := \Omega^p(M) \otimes_\mathbb{R} \mathfrak{g}.
$$
For any choice of basis $\{E_R\}_{R=1}^{\dim\mathfrak{g}}$ of $\mathfrak{g}$, every $\varphi \in \Omega^p(M; \mathfrak{g})$ decomposes uniquely as
$$
\varphi = E_R \otimes \varphi^R = \sum_R E_R \otimes \varphi^R,
$$
where each $\varphi^R \in \Omega^p(M)$ is an ordinary smooth $p$-form. Evaluated on $p$ tangent vectors $X_1, \ldots, X_p$ at a point $q \in M$, $\varphi(X_1, \ldots, X_p) = E_R\, \varphi^R(X_1, \ldots, X_p) \in \mathfrak{g}$.

The **exterior derivative** on $\Omega^p(M; \mathfrak{g})$ is defined by linear extension:
$$
d\varphi := E_R \otimes d\varphi^R, \quad \text{equivalently } d(\alpha \otimes \xi) := d\alpha \otimes \xi \text{ for } \alpha \in \Omega^p(M),\ \xi \in \mathfrak{g}.
$$
This operator satisfies $d^2 = 0$ and the graded Leibniz rule with respect to wedge product against ordinary forms: $d(\alpha \wedge \varphi) = d\alpha \wedge \varphi + (-1)^p \alpha \wedge d\varphi$.

The space $\Omega^\bullet(M; \mathfrak{g}) = \bigoplus_p \Omega^p(M; \mathfrak{g})$ is a graded $\Omega^\bullet(M)$-module, with the wedge product against ordinary forms acting on the first factor. To make it a graded Lie algebra one needs the bracket of [[Def - Bracket of g-Valued Forms]].

---

# Relate to Other Fields / Compression

A $\mathfrak{g}$-valued $p$-form is literally the same construction as an $E$-valued $p$-form (a section of $\Lambda^p T^*M \otimes E$) for any vector bundle $E$ — specialised to the trivial bundle $E = M \times \mathfrak{g}$. The general vector-bundle-valued case requires a connection to differentiate (because basis sections of $E$ are not constant); the $\mathfrak{g}$-valued case does not, because the trivial bundle has the canonical flat connection given by $d$. This is the geometric reason for the asymmetry: ordinary forms and $\mathfrak{g}$-valued forms have a canonical $d$; sections of non-trivial bundles do not.

A $\mathfrak{g}$-valued form is also a special case of a **tensor field of mixed type**: it is a section of $\Lambda^p T^*M \otimes \mathfrak{g}$ where the second factor is a fixed (rather than tangent or cotangent) vector space. In physics, such objects appear constantly: the electromagnetic 4-potential $A_\mu$ is a real-valued (i.e., $\mathfrak{u}(1) \cong i\mathbb{R}$-valued) 1-form; the Yang-Mills potential $A^a_\mu$ is a $\mathfrak{g}$-valued 1-form with components in a Lie-algebra basis; the spin connection $\omega^a{}_b$ is an $\mathfrak{so}(n)$-valued 1-form (a matrix of 1-forms).

**True name:** the operational characterisation is that a $\mathfrak{g}$-valued $p$-form is a *matrix of ordinary $p$-forms when $\mathfrak{g}$ is a matrix Lie algebra* (or equivalently a tuple of $p$-forms indexed by a basis of $\mathfrak{g}$). Frankel emphasises this: the connection 1-form on the orthonormal frame bundle of a Riemannian manifold is "a skew-symmetric matrix of ordinary 1-forms" — that is, an $\mathfrak{o}(n)$-valued 1-form, decomposed in the basis of antisymmetric matrices. Every computation works this way: you have a basis $E_R$ of $\mathfrak{g}$, and your $\mathfrak{g}$-valued form is a tuple $(\varphi^1, \ldots, \varphi^{\dim\mathfrak{g}})$ of ordinary forms, manipulated component-wise.

---

# Examples / Corollaries

The **Maurer-Cartan form** on a Lie group $G$ is the canonical example: $\theta_G \in \Omega^1(G; \mathfrak{g})$ is the $\mathfrak{g}$-valued 1-form that left-translates each tangent vector to the identity. In a basis of left-invariant 1-forms $\sigma^R$ dual to the left-invariant vector fields $X^R$ obtained from a basis $E_R$ of $\mathfrak{g}$, $\theta_G = E_R \otimes \sigma^R$. See [[Def - The Maurer-Cartan Form]] for the full development.

The **connection 1-form** $\omega$ on a principal $G$-bundle $P \to M$ is a $\mathfrak{g}$-valued 1-form on the total space $P$: $\omega \in \Omega^1(P; \mathfrak{g})$. See [[Def - Connection 1-Form on a Principal Bundle]].

The **gauge potential** in a local trivialisation is a $\mathfrak{g}$-valued 1-form on an open subset of the base: $A_\alpha \in \Omega^1(U_\alpha; \mathfrak{g})$. See [[Def - Local Connection 1-Form (Gauge Potential)]].

The **curvature 2-form** is a $\mathfrak{g}$-valued 2-form on $P$: $\Omega \in \Omega^2(P; \mathfrak{g})$. See [[Def - Curvature 2-Form on a Principal Bundle]].

**Is NOT an instance:** the electromagnetic field strength $F$ on a non-trivial $U(1)$-bundle, *globally as a section of a bundle*, is *not* a $\mathfrak{u}(1)$-valued 2-form on $M$ in the sense of this page — it is a 2-form section of the adjoint bundle $\Omega^2(M; \mathrm{Ad}\,P)$, which happens to be trivial since $U(1)$ is abelian. The two coincide *only* because $\mathrm{Ad}\,P$ is trivial in the abelian case. For non-abelian $G$, the curvature is a section of the *non-trivial* bundle $\mathrm{Ad}\,P$, not a $\mathfrak{g}$-valued form on $M$ in the sense of this definition.

**Is NOT an instance:** a $\mathbb{R}^n$-valued 1-form on $M$ (e.g., the position differential $dx = (\partial_i, dx^i)$) is not a $\mathfrak{g}$-valued form unless $\mathbb{R}^n$ is the Lie algebra of some specific group — $\mathbb{R}^n$ with the trivial (abelian) Lie bracket is the Lie algebra of $\mathbb{R}^n$ as an additive Lie group, in which case yes, but the bracket is zero. A meaningful $\mathfrak{g}$-valued form needs $\mathfrak{g}$ to have a non-trivial bracket to be useful for gauge theory.

A **corollary**: if $f : M \to N$ is a smooth map and $\varphi \in \Omega^p(N; \mathfrak{g})$, then the pullback $f^*\varphi \in \Omega^p(M; \mathfrak{g})$ is well defined and equals $E_R \otimes f^*\varphi^R$ in any basis. Pullback commutes with $d$: $f^*(d\varphi) = d(f^*\varphi)$.

A **corollary**: $\Omega^0(M; \mathfrak{g}) = C^\infty(M; \mathfrak{g})$ is the space of smooth $\mathfrak{g}$-valued functions on $M$ — for instance, an infinitesimal gauge transformation parameter.

**Calibration check.** If you have understood the definition, you should be able to: (i) write down explicitly a $\mathfrak{su}(2)$-valued 1-form on $\mathbb{R}^3$ in components, choosing the Pauli-matrix basis $\sigma_1, \sigma_2, \sigma_3$ of $\mathfrak{su}(2)$ — e.g., $A = i\sigma_a \otimes A^a_\mu(x)\,dx^\mu$ with $A^a_\mu(x)$ nine real functions; (ii) compute $dA$ for this example using the rule $d(E_R \otimes \varphi^R) = E_R \otimes d\varphi^R$ — answer: $dA = i\sigma_a \otimes \partial_\nu A^a_\mu\,dx^\nu \wedge dx^\mu$; (iii) explain why this differentiation does not require any connection or extra structure — because $\mathfrak{g}$ is a fixed vector space and the trivial bundle $M \times \mathfrak{g}$ has the canonical flat connection $d$.

---

# Unlocked by This

> [!tip] Bracket of g-Valued Forms *(from Gauge Theory III)*
> Once $\mathfrak{g}$-valued forms exist, they support a graded bracket combining the Lie bracket of $\mathfrak{g}$ with the wedge product of forms. The bracket is what turns $\Omega^\bullet(M; \mathfrak{g})$ from a graded module into a **graded Lie algebra** (the "differential graded Lie algebra of forms valued in $\mathfrak{g}$"). The bracket is the operation that appears in every gauge-theory formula: the structural equation $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$, the gauge transformation law, the Bianchi identity. See [[Def - Bracket of g-Valued Forms]].

> [!tip] Differential Graded Lie Algebras *(from Deformation Theory and Higher Algebra)*
> The pair $(\Omega^\bullet(M; \mathfrak{g}), d, [\,\cdot\,,\,\cdot\,])$ is the prototypical **differential graded Lie algebra (DGLA)**: a $\mathbb{Z}$-graded vector space with a degree-$+1$ differential $d$ satisfying $d^2 = 0$, and a graded bracket satisfying the graded Jacobi and graded Leibniz with $d$. Solutions of the **Maurer-Cartan equation** $d\omega + \tfrac{1}{2}[\omega, \omega] = 0$ in a DGLA are the local data of a deformation theory — they classify deformations of geometric structures, complex structures, Poisson structures, and (most relevantly here) flat connections on $G$-bundles. This is the entry point to **deformation theory** in the sense of Kontsevich, Goldman-Millson, and others — the unifying framework in which gauge theory, complex geometry, and homotopy theory all live.
