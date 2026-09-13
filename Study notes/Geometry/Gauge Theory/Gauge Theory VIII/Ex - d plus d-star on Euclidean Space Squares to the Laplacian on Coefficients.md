---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Hodge-de Rham Operator is a Dirac Operator"
  - "Def - The Codifferential"
  - "Def - Interior Product (Contraction with a Vector Field)"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Hodge Laplacian"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Work on $\mathbb{R}^n$ with the flat Euclidean metric $g = \sum_{i=1}^n dx^i\otimes dx^i$ and the standard global orthonormal frame $(e_i)_{i=1}^n = (\partial_1,\dots,\partial_n)$, with dual coframe $(e^i) = (dx^1,\dots,dx^n)$. Let $d : \Omega^k(\mathbb{R}^n)\to\Omega^{k+1}(\mathbb{R}^n)$ be the exterior derivative and $d^* : \Omega^k(\mathbb{R}^n)\to\Omega^{k-1}(\mathbb{R}^n)$ the codifferential (the formal adjoint of $d$), so that $D := d + d^*$ is the Hodge–de Rham operator acting on $\Omega^\bullet(\mathbb{R}^n) = \bigoplus_k \Omega^k(\mathbb{R}^n)$.

Prove that
$$
(d + d^*)^2 \;=\; d\,d^* + d^*d \;=\; -\sum_{i=1}^n \partial_i^2,
$$
where the operator on the right acts **coefficientwise**: on a $k$-form $\omega = \sum_{I}\omega_I\,dx^I$ (the sum over increasing multi-indices $I = (i_1 < \dots < i_k)$, $dx^I = dx^{i_1}\wedge\dots\wedge dx^{i_k}$, and $\omega_I\in C^\infty(\mathbb{R}^n)$), it returns $-\sum_i\partial_i^2\,\omega = \sum_I\big(-\sum_i\partial_i^2\omega_I\big)\,dx^I$.

You may use the **frame formulas** for $d$ and $d^*$ established on the Hodge–de Rham page,
$$
d = \sum_{i=1}^n e^i\wedge\nabla_{e_i}, \qquad d^* = -\sum_{i=1}^n \iota_{e_i}\nabla_{e_i},
$$
valid in any local orthonormal frame with $\nabla$ the Levi-Civita connection, and the **anticommutation relation** between contraction and exterior multiplication,
$$
\{\iota_{e_i},\, e^j\wedge\} \;:=\; \iota_{e_i}\circ(e^j\wedge) + (e^j\wedge)\circ\iota_{e_i} \;=\; \delta_{ij}\cdot\mathrm{id}.
$$

**Recall:**

The objects in play are the exterior derivative and codifferential in an orthonormal frame, the interior product (contraction), and the Hodge Laplacian.

![[Thm - The Hodge-de Rham Operator is a Dirac Operator#Statement]]

By [[Thm - The Hodge-de Rham Operator is a Dirac Operator|the Hodge–de Rham theorem]], the exterior bundle $\Lambda T^*M = \bigoplus_k\Lambda^k T^*M$ with Clifford multiplication $v\cdot\phi = v^\flat\wedge\phi - \iota_v\phi$, the induced metric, and the Levi-Civita connection is a Dirac bundle whose Dirac operator is $D = d + d^*$; in any local orthonormal frame $(e_i)$ with dual coframe $(e^i)$,
$$
d = \sum_i e^i\wedge\nabla_{e_i}, \qquad d^* = -\sum_i \iota_{e_i}\nabla_{e_i}.
$$

![[Def - Interior Product (Contraction with a Vector Field)#The Definition]]

The **[[Def - Interior Product (Contraction with a Vector Field)|interior product]]** $\iota_v$ with a vector field $v$ is the antiderivation of degree $-1$ on $\Omega^\bullet$ determined by $\iota_v f = 0$ on functions and $\iota_v\alpha = \alpha(v)$ on $1$-forms; on the coframe, $\iota_{e_i}e^j = \delta_{ij}$. Being an antiderivation, it satisfies $\iota_v(\alpha\wedge\omega) = (\iota_v\alpha)\wedge\omega + (-1)^{|\alpha|}\alpha\wedge\iota_v\omega$; for a $1$-form $\alpha$ this reads $\iota_v(\alpha\wedge\omega) = \alpha(v)\,\omega - \alpha\wedge\iota_v\omega$.

![[Def - The Codifferential#The Definition]]

![[Def - Hodge Laplacian#The Definition]]

The **[[Def - Hodge Laplacian|Hodge Laplacian]]** is $\Delta := d\,d^* + d^*d$; the assertion of this exercise is that on flat $\mathbb{R}^n$ it equals the coefficientwise operator $-\sum_i\partial_i^2$, the sign making $\Delta$ non-negative (Haydys's / the series' convention). Throughout, $\{P, Q\} := PQ + QP$ denotes the anticommutator of two operators; the bracket $[\iota_{e_i}, e^j\wedge] = \delta_{ij}$ of the source is this anticommutator, being the graded commutator of the two odd (degree $\mp 1$) operators $\iota_{e_i}$ and $e^j\wedge$.

> [!warning] Convention: the flat frame is parallel
> On $\mathbb{R}^n$ with the flat metric the Levi-Civita connection is the trivial (coordinate) connection: $\nabla_{e_i} = \partial_i$ acts on a form $\omega = \sum_I\omega_I\,dx^I$ by differentiating its coefficients, $\nabla_{\partial_i}\omega = \sum_I(\partial_i\omega_I)\,dx^I$, because the coframe $(dx^i)$ is parallel, $\nabla_{\partial_i}dx^j = 0$. Consequently, in the frame formulas $d = \sum_i e^i\wedge\nabla_{e_i}$ and $d^* = -\sum_i\iota_{e_i}\nabla_{e_i}$, the operator $\nabla_{e_i}$ is literally $\partial_i$ acting coefficientwise, and it commutes with the constant-coefficient algebraic operators $e^j\wedge$ and $\iota_{e_j}$ (these do not depend on the base point).

---

# Convergent Strategy

**Problem class.** This is a *square-of-a-Dirac-operator* computation carried out in the flattest possible case, where the Dirac operator has constant coefficients. The class is recognisable from the target: an operator of Dirac type squares to a Laplacian (this is the defining feature of a Dirac operator), and on flat space with a parallel frame the curvature and connection terms vanish, so the square is exactly the scalar Laplacian with no zero-order correction. The computation is the mechanism behind the general [[Thm - Weitzenbock Formula for the Dirac Operator|Weitzenböck formula]] $D^2 = \nabla^*\nabla + \mathcal{R}$, seen in the case $\mathcal{R} = 0$ and $\nabla^*\nabla = -\sum_i\partial_i^2$.

**Assumption pattern.** The flat-frame hypothesis is used in exactly one way: it makes the two algebraic operators $e^i\wedge$ (exterior multiplication) and $\iota_{e_i}$ (contraction) *constant* — independent of the base point — so that they commute with the derivatives $\partial_j$ and carry no derivatives of their own. This turns the operator identity into a purely algebraic manipulation of the constants $e^i\wedge$, $\iota_{e_i}$ against the commuting family $\partial_1,\dots,\partial_n$. The trigger for the approach is the pairing of a first-order operator built from a Clifford symbol with a *parallel* orthonormal frame.

**Theorem routing.** The route is: (i) name the two algebraic operators $a_i := e^i\wedge$ and $b_i := \iota_{e_i}$ and record the three anticommutation relations they satisfy — $\{a_i, a_j\} = 0$, $\{b_i, b_j\} = 0$, $\{b_i, a_j\} = \delta_{ij}$ (the first two from [[Def - Interior Product (Contraction with a Vector Field)|the antiderivation property]] and the antisymmetry of the wedge, the third the given relation); (ii) write $d = \sum_i a_i\partial_i$ and $d^* = -\sum_i b_i\partial_i$ from [[Thm - The Hodge-de Rham Operator is a Dirac Operator|the frame formulas]]; (iii) expand $(d + d^*)^2 = d^2 + d\,d^* + d^*d + (d^*)^2$ and evaluate each of the four terms using the relations and the symmetry $\partial_i\partial_j = \partial_j\partial_i$; (iv) collect: $d^2 = 0$, $(d^*)^2 = 0$, and $d\,d^* + d^*d = -\sum_i\partial_i^2$.

**Key decision point.** The decisive move is to split the mixed sum $\sum_{i,j}(\cdots)\partial_i\partial_j$ according to the symmetry of $\partial_i\partial_j$ in $(i, j)$: an operator coefficient that is *antisymmetric* in $(i, j)$ (such as $a_ia_j$) contracts against the *symmetric* $\partial_i\partial_j$ to give zero, while for $d\,d^* + d^*d$ the coefficient that survives is the *symmetric* anticommutator $\{a_i, b_j\} = \delta_{ij}$, which collapses the double sum to a single trace $\sum_i\partial_i^2$. Recognising that the two cross terms $d\,d^*$ and $d^*d$ must be added *before* simplifying — so that the anticommutator, not the individual products, appears — is the whole art of the computation.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (numbering to be reconciled with the topic page's Legal Operations once it is written):

1. **Replace $d$ and $d^*$ by their frame formulas.** Use $d = \sum_i e^i\wedge\nabla_{e_i}$ and $d^* = -\sum_i\iota_{e_i}\nabla_{e_i}$ from the Hodge–de Rham page, and specialise $\nabla_{e_i} = \partial_i$ on flat $\mathbb{R}^n$.

2. **Abbreviate the constant algebraic operators and record their Clifford (anticommutation) relations.** Set $a_i := e^i\wedge$, $b_i := \iota_{e_i}$; establish $\{a_i, a_j\} = 0$, $\{b_i, b_j\} = 0$, $\{a_i, b_j\} = \delta_{ij}$ from the antiderivation property of contraction and the antisymmetry of the wedge.

3. **Commute algebraic operators past derivatives.** On flat space $a_i, b_j$ are point-independent, so $a_i\partial_i b_j\partial_j = a_i b_j\partial_i\partial_j$ and likewise for every product; the derivatives commute among themselves, $\partial_i\partial_j = \partial_j\partial_i$.

4. **Kill an antisymmetric-coefficient sum against a symmetric derivative sum.** For $d^2$ and $(d^*)^2$, the operator coefficient is antisymmetric in $(i, j)$ while $\partial_i\partial_j$ is symmetric, so the double sum vanishes by relabelling.

5. **Collapse a double sum through the anticommutator.** Add the two cross terms first: $d\,d^* + d^*d = -\sum_{i,j}\{a_i, b_j\}\partial_i\partial_j = -\sum_{i,j}\delta_{ij}\partial_i\partial_j = -\sum_i\partial_i^2$.

---

# Hints

> [!note]- Hint 1
> Do not compute $d\omega$ and then $d^*(d\omega)$ on an explicit form. Work at the level of operators. Substitute the frame formulas and abbreviate the two point-independent building blocks: exterior multiplication $a_i := e^i\wedge = dx^i\wedge$ and contraction $b_i := \iota_{e_i} = \iota_{\partial_i}$. Then $d = \sum_i a_i\partial_i$ and $d^* = -\sum_i b_i\partial_i$.

> [!note]- Hint 2
> You will need three relations among the $a$'s and $b$'s. Two are free: wedging two $1$-forms anticommutes ($\{a_i, a_j\} = 0$, so $a_i^2 = 0$), and contractions anticommute ($\{b_i, b_j\} = 0$, so $b_i^2 = 0$). The third is the one you are given: $\{b_i, a_j\} = a_j b_i + b_i a_j = \delta_{ij}$. Prove the first two from the antiderivation rule $\iota_v(\alpha\wedge\omega) = \alpha(v)\omega - \alpha\wedge\iota_v\omega$ and $dx^i\wedge dx^j = -dx^j\wedge dx^i$.

> [!note]- Hint 3
> Expand $(d + d^*)^2 = d^2 + d\,d^* + d^*d + (d^*)^2$. In each term move all $a$'s and $b$'s to the left of all $\partial$'s (legal because they are constant), leaving a double sum $\sum_{i,j}(\text{operator})_{ij}\,\partial_i\partial_j$. Now use that $\partial_i\partial_j$ is *symmetric* in $(i,j)$: any coefficient antisymmetric in $(i,j)$ sums to zero.

> [!note]- Hint 4
> $d^2 = \sum_{i,j}a_ia_j\,\partial_i\partial_j = 0$ and $(d^*)^2 = \sum_{i,j}b_ib_j\,\partial_i\partial_j = 0$ because $a_ia_j$ and $b_ib_j$ are antisymmetric in $(i,j)$. For the cross terms, do not simplify them separately — *add them first*: $d\,d^* + d^*d = -\sum_{i,j}(a_ib_j + b_ja_i)\partial_i\partial_j$. Recognise $a_ib_j + b_ja_i = \{a_i, b_j\} = \delta_{ij}$, and the double sum collapses to $-\sum_i\partial_i^2$.

---

# Solution

The computation is entirely algebraic once the frame formulas are in hand: on flat space $d$ and $d^*$ are constant-coefficient combinations of exterior multiplication and contraction with the partial derivatives, and squaring them reduces, through the anticommutation relations of exterior multiplication against contraction, to a single trace of second derivatives. We record the three relations (Step 1), rewrite $d$ and $d^*$ (Step 2), and expand the square term by term (Step 3).

**Step 1: The three anticommutation relations of $a_i := e^i\wedge$ and $b_i := \iota_{e_i}$.**

As operators on $\Omega^\bullet(\mathbb{R}^n)$,
$$
\{a_i, a_j\} = 0, \qquad \{b_i, b_j\} = 0, \qquad \{a_i, b_j\} = \delta_{ij}\cdot\mathrm{id}.
$$

> [!note]- Derivation
> Write $a_i = e^i\wedge = dx^i\wedge$ for exterior multiplication and $b_i = \iota_{e_i} = \iota_{\partial_i}$ for contraction; both are $C^\infty(\mathbb{R}^n)$-linear, point-independent, order-zero (algebraic) operators, because the coframe $(dx^i)$ is constant.
>
> **$\{a_i, a_j\} = 0$.** For any form $\omega$, $a_ia_j\omega = dx^i\wedge dx^j\wedge\omega$ and $a_ja_i\omega = dx^j\wedge dx^i\wedge\omega$. Since $dx^i\wedge dx^j = -dx^j\wedge dx^i$ (antisymmetry of the wedge on $1$-forms) and the wedge is associative,
> $$a_ia_j\omega + a_ja_i\omega = (dx^i\wedge dx^j + dx^j\wedge dx^i)\wedge\omega = 0 \qquad \text{(antisymmetry of } \wedge \text{).}$$
> In particular $a_i^2 = 0$.
>
> **$\{b_i, b_j\} = 0$.** The interior product is an antiderivation of degree $-1$, and for two such contractions $\iota_{\partial_i}\iota_{\partial_j} = -\iota_{\partial_j}\iota_{\partial_i}$; indeed on any form, applying the antiderivation rule shows $\iota_v\iota_w = -\iota_w\iota_v$ (a standard identity for interior products, provable by induction on form-degree from $\iota_v(\alpha\wedge\omega) = \alpha(v)\omega - \alpha\wedge\iota_v\omega$). Hence $b_ib_j + b_jb_i = 0$, and $b_i^2 = 0$.
>
> **$\{a_i, b_j\} = \delta_{ij}$.** This is the given relation, and it is the antiderivation rule specialised to the parallel coframe. For any form $\omega$,
> $$b_j(a_i\omega) = \iota_{\partial_j}(dx^i\wedge\omega) = (\iota_{\partial_j}dx^i)\,\omega - dx^i\wedge\iota_{\partial_j}\omega = \delta_{ji}\,\omega - a_i(b_j\omega) \qquad \text{(antiderivation rule; } \iota_{\partial_j}dx^i = dx^i(\partial_j) = \delta_{ji}\text{),}$$
> so $b_ja_i\omega + a_ib_j\omega = \delta_{ij}\omega$, that is $\{a_i, b_j\} = \delta_{ij}\cdot\mathrm{id}$ (using $\delta_{ij} = \delta_{ji}$).

**Step 2: The frame formulas on flat space.**

$$
d = \sum_{i=1}^n a_i\,\partial_i, \qquad d^* = -\sum_{i=1}^n b_i\,\partial_i,
$$
with each $a_i, b_i$ constant and commuting with every $\partial_j$.

> [!note]- Derivation
> By [[Thm - The Hodge-de Rham Operator is a Dirac Operator|the Hodge–de Rham theorem]], in an orthonormal frame $d = \sum_i e^i\wedge\nabla_{e_i}$ and $d^* = -\sum_i\iota_{e_i}\nabla_{e_i}$. On $\mathbb{R}^n$ with the flat metric the frame $(\partial_i)$ is parallel, so $\nabla_{e_i} = \partial_i$ acts coefficientwise (**flat-frame convention**): $\nabla_{\partial_i}\omega = \sum_I(\partial_i\omega_I)dx^I$. Substituting $e^i\wedge = a_i$, $\iota_{e_i} = b_i$, and $\nabla_{e_i} = \partial_i$ gives the two formulas. Because $a_i, b_i$ are point-independent order-zero operators, they commute with the coefficientwise derivatives: $a_i\partial_j = \partial_j a_i$ and $b_i\partial_j = \partial_j b_i$ for all $i, j$ (differentiating $a_i\omega = dx^i\wedge\omega$ along $\partial_j$ differentiates only the coefficients of $\omega$, since $dx^i$ is constant, and likewise for $b_i$). Finally $\partial_i\partial_j = \partial_j\partial_i$ on smooth functions (equality of mixed partials).

**Step 3: Expand the square and evaluate the four terms.**

$$
(d + d^*)^2 = \underbrace{d^2}_{=\,0} + \underbrace{d\,d^* + d^*d}_{=\,-\sum_i\partial_i^2} + \underbrace{(d^*)^2}_{=\,0} = -\sum_{i=1}^n\partial_i^2.
$$

> [!note]- Derivation
> Expand $(d + d^*)^2 = d^2 + d\,d^* + d^*d + (d^*)^2$ and treat each term. In every product, move the constant operators $a_i, b_j$ to the left of the derivatives (Step 2), producing a double sum $\sum_{i,j}(\cdots)_{ij}\,\partial_i\partial_j$.
>
> **The term $d^2$.**
> $$d^2 = \Big(\sum_i a_i\partial_i\Big)\Big(\sum_j a_j\partial_j\Big) = \sum_{i,j} a_ia_j\,\partial_i\partial_j \qquad \text{(} a_j \text{ commutes with } \partial_i \text{).}$$
> Symmetrise in $(i,j)$: since $\partial_i\partial_j = \partial_j\partial_i$, relabelling the summation indices gives $\sum_{i,j}a_ia_j\partial_i\partial_j = \tfrac12\sum_{i,j}(a_ia_j + a_ja_i)\partial_i\partial_j = \tfrac12\sum_{i,j}\{a_i,a_j\}\partial_i\partial_j = 0$ (by $\{a_i, a_j\} = 0$, **Step 1**). Hence $d^2 = 0$, as it must be.
>
> **The term $(d^*)^2$.** Identically,
> $$(d^*)^2 = \Big(\!-\!\sum_i b_i\partial_i\Big)\Big(\!-\!\sum_j b_j\partial_j\Big) = \sum_{i,j} b_ib_j\,\partial_i\partial_j = \tfrac12\sum_{i,j}\{b_i, b_j\}\partial_i\partial_j = 0 \qquad \text{(} \{b_i, b_j\} = 0 \text{, } \partial_i\partial_j \text{ symmetric).}$$
>
> **The cross terms $d\,d^* + d^*d$.** Do not simplify them separately; add them. Using $b_j\partial_j$ commutes with $a_i$, and $\partial_i$ commutes with $b_j$,
> $$d\,d^* = \Big(\sum_i a_i\partial_i\Big)\Big(\!-\!\sum_j b_j\partial_j\Big) = -\sum_{i,j} a_ib_j\,\partial_i\partial_j,$$
> $$d^*d = \Big(\!-\!\sum_j b_j\partial_j\Big)\Big(\sum_i a_i\partial_i\Big) = -\sum_{i,j} b_ja_i\,\partial_i\partial_j.$$
> Adding, and grouping the two operator coefficients over the same $\partial_i\partial_j$,
> $$d\,d^* + d^*d = -\sum_{i,j}(a_ib_j + b_ja_i)\,\partial_i\partial_j = -\sum_{i,j}\{a_i, b_j\}\,\partial_i\partial_j \qquad \text{(definition of the anticommutator)}$$
> $$= -\sum_{i,j}\delta_{ij}\,\partial_i\partial_j \qquad \text{(} \{a_i, b_j\} = \delta_{ij} \text{, } \textbf{Step 1}\text{)}$$
> $$= -\sum_{i=1}^n\partial_i^2 \qquad \text{(the } \delta_{ij} \text{ collapses the double sum to its diagonal).}$$
>
> **Collecting.** $(d + d^*)^2 = 0 + \big(-\sum_i\partial_i^2\big) + 0 = -\sum_i\partial_i^2$, acting coefficientwise: on $\omega = \sum_I\omega_I dx^I$ every $\partial_i^2$ differentiates the coefficient functions $\omega_I$ only (the $dx^I$ being constant), so $(d + d^*)^2\omega = \sum_I\big(-\sum_i\partial_i^2\omega_I\big)dx^I$. Since $d^2 = (d^*)^2 = 0$ we also have $(d + d^*)^2 = d\,d^* + d^*d = \Delta$, the [[Def - Hodge Laplacian|Hodge Laplacian]].

> [!note]- Complete formal solution
> **Claim.** On $\mathbb{R}^n$ with the flat metric, $(d + d^*)^2 = d\,d^* + d^*d = -\sum_{i=1}^n\partial_i^2$ coefficientwise on $\Omega^\bullet(\mathbb{R}^n)$.
>
> Abbreviate $a_i := dx^i\wedge$ and $b_i := \iota_{\partial_i}$, both point-independent order-zero operators on $\Omega^\bullet(\mathbb{R}^n)$. From the antisymmetry $dx^i\wedge dx^j = -dx^j\wedge dx^i$, the antiderivation rule $\iota_{\partial_j}(dx^i\wedge\omega) = \delta_{ij}\omega - dx^i\wedge\iota_{\partial_j}\omega$, and the anticommutativity of interior products, we obtain
> $$\{a_i, a_j\} = 0, \qquad \{b_i, b_j\} = 0, \qquad \{a_i, b_j\} = \delta_{ij}.$$
> By the Hodge–de Rham frame formulas and the flatness of the frame ($\nabla_{\partial_i} = \partial_i$ coefficientwise), $d = \sum_i a_i\partial_i$ and $d^* = -\sum_i b_i\partial_i$, with $a_i, b_i$ commuting with all $\partial_j$ and $\partial_i\partial_j = \partial_j\partial_i$. Then
> $$d^2 = \sum_{i,j}a_ia_j\partial_i\partial_j = \tfrac12\sum_{i,j}\{a_i,a_j\}\partial_i\partial_j = 0, \qquad (d^*)^2 = \sum_{i,j}b_ib_j\partial_i\partial_j = \tfrac12\sum_{i,j}\{b_i,b_j\}\partial_i\partial_j = 0,$$
> using the symmetry of $\partial_i\partial_j$ against the antisymmetric $a_ia_j$ and $b_ib_j$. Adding the cross terms,
> $$d\,d^* + d^*d = -\sum_{i,j}(a_ib_j + b_ja_i)\partial_i\partial_j = -\sum_{i,j}\delta_{ij}\partial_i\partial_j = -\sum_i\partial_i^2.$$
> Therefore $(d + d^*)^2 = d^2 + d\,d^* + d^*d + (d^*)^2 = -\sum_i\partial_i^2$, and since $d^2 = (d^*)^2 = 0$ this is also $d\,d^* + d^*d = \Delta$. On $\omega = \sum_I\omega_I\,dx^I$ the operator acts coefficientwise, $(d+d^*)^2\omega = \sum_I(-\sum_i\partial_i^2\omega_I)dx^I$. $\blacksquare$

> [!note]- Independent sanity check on $0$-forms and $1$-forms
> On a function $g\in\Omega^0(\mathbb{R}^n)$: $d^*g = 0$ (there are no $(-1)$-forms), $dg = \sum_i(\partial_i g)dx^i$, and $d^*(dg) = -\sum_i\iota_{\partial_i}\partial_i\big(\sum_j(\partial_j g)dx^j\big) = -\sum_{i,j}(\partial_i\partial_j g)\iota_{\partial_i}dx^j = -\sum_i\partial_i^2 g$, while $d\,d^*g = 0$; so $\Delta g = -\sum_i\partial_i^2 g$, agreeing with the claim. On a $1$-form $\omega = \sum_k\omega_k\,dx^k$: $d^*\omega = -\sum_i\partial_i\omega_i$ (minus the divergence), $d(d^*\omega) = -\sum_i\sum_k\partial_k\partial_i\omega_i\,dx^k$; and $d\omega = \sum_{i<k}(\partial_i\omega_k - \partial_k\omega_i)dx^i\wedge dx^k$, $d^*(d\omega) = -\sum_k\big(\sum_i\partial_i(\partial_i\omega_k - \partial_k\omega_i)\big)dx^k = -\sum_k\big(\sum_i\partial_i^2\omega_k - \sum_i\partial_k\partial_i\omega_i\big)dx^k$. Adding, the divergence-type terms $\pm\sum_{i,k}\partial_k\partial_i\omega_i\,dx^k$ cancel and $\Delta\omega = -\sum_k\big(\sum_i\partial_i^2\omega_k\big)dx^k$, again coefficientwise as claimed.

---

# Key Takeaways

**A Dirac operator squares to a Laplacian because the Clifford relations are exactly the algebraic identities that make the second-order cross terms cancel.** The reusable content is the bookkeeping: writing $d + d^* = \sum_i(a_i - b_i)\partial_i$ with $a_i = e^i\wedge$, $b_i = \iota_{e_i}$, the square is $\sum_{i,j}(a_i - b_i)(a_j - b_j)\partial_i\partial_j$, and only the part of the operator coefficient that is *symmetric* in $(i,j)$ survives the contraction against the symmetric $\partial_i\partial_j$. The symmetric part is $\tfrac12\{a_i - b_i, a_j - b_j\} = \tfrac12(\{a_i,a_j\} + \{b_i,b_j\} - \{a_i,b_j\} - \{b_i,a_j\}) = -\delta_{ij}$ by the three anticommutation relations, and $-\sum_{i,j}\delta_{ij}\partial_i\partial_j = -\sum_i\partial_i^2$. This is the same mechanism as in [[Thm - The Dirac Operator on Flat Space Squares to the Laplacian|the flat quaternionic Dirac operator]], where the roles of $\{a_i, b_j\} = \delta_{ij}$ are played by $i^2 = j^2 = k^2 = -1$ and the anticommutation of the imaginary units — the Clifford relations of $\mathbb{R}^3$ and $\mathbb{R}^4$. The trigger, whenever one meets a first-order operator whose "symbol" satisfies Clifford relations, is to expect its square to be a Laplacian, and to look for the zero-order remainder (here zero, in general the curvature term).

**On flat space with a parallel frame the connection and curvature terms of the Weitzenböck formula vanish, isolating the principal symbol.** The general identity $D^2 = \nabla^*\nabla + \mathcal{R}$ of [[Thm - Weitzenbock Formula for the Dirac Operator|the Weitzenböck formula]] has three potential sources of terms: the second-order principal part, the first-order terms involving $\nabla e_i$ (the failure of the frame to be parallel), and the zero-order curvature $\mathcal{R}$. This exercise switches off the last two by choosing $\mathbb{R}^n$ and the coordinate frame, so that $\nabla_{e_i} = \partial_i$ with $\nabla e_i = 0$ and $\mathcal{R} = 0$, and what remains is $\nabla^*\nabla = -\sum_i\partial_i^2$. The transferable diagnostic: to isolate the principal symbol of any Dirac-type operator, compute in a *synchronous* orthonormal frame at a point (one with $\nabla e_i = 0$ there) — the same device [[Thm - Existence of Synchronous Orthonormal Frames|used to prove the Weitzenböck formula]] on a general manifold; on flat space the frame is globally synchronous, so the pointwise computation is the whole answer.

**"Add the cross terms before simplifying" is the recurring move whenever an anticommutator is the object that carries the content.** Individually $d\,d^*$ and $d^*d$ are complicated second-order operators with no clean form; their *sum* is a scalar Laplacian, because the sum is where the symmetric anticommutator $\{a_i, b_j\}$ — and hence the Clifford relation $\delta_{ij}$ — appears. The same pattern governs the connection Laplacian $\nabla^*\nabla = -\sum_i(\nabla_{e_i}\nabla_{e_i} - \nabla_{\nabla_{e_i}e_i})$ and the splitting of $\nabla_{e_i}\nabla_{e_j}$ into its symmetric part (which contracts to the trace Laplacian) and its antisymmetric part (which becomes curvature) in the proof of the Weitzenböck formula. Whenever a computation produces two products $PQ$ and $QP$ of operators satisfying known (anti)commutation relations, resist simplifying them apart: form $PQ + QP$ or $PQ - QP$ and read off the relation. The companion exercise [[Ex - The Twisted Bundle of a Dirac Bundle is a Dirac Bundle]] shows the other half of this circle of ideas — how coupling a Dirac operator to an auxiliary connection adds a first-order term — so that between the two, the full anatomy of $D^2 = \nabla^*\nabla + \mathcal{R}$ on flat and twisted bundles is visible.
