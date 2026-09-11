---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - A Covariant Derivative Determines a Connection on the Frame Bundle"
  - "Thm - Structure Equation for the Curvature"
  - "Thm - Bianchi Identity for a Principal Connection"
  - "Def - Curvature 2-Forms (Cartan)"
  - "Thm - Cartan's Second Structural Equation"
  - "Thm - First and Second Bianchi Identities"
tags: [geometry, gauge-theory]
---

# Problem Statement

This exercise continues Bär's Example 2.3.3 (the fundamental example: the connection a covariant derivative induces on a frame bundle) into curvature. Let $(M, g)$ be a Riemannian manifold of dimension $n$, let $\nabla$ be its [[Def - Levi-Civita Connection|Levi-Civita connection]] on the tangent bundle $TM$, and let $\operatorname{Fr}(TM) \xrightarrow{\pi} M$ be the frame bundle of $TM$, a principal $G$-bundle with structure group $G = GL(n, \mathbb{R})$ and Lie algebra $\mathfrak{g} = \mathfrak{gl}(n, \mathbb{R}) = \operatorname{Mat}(n \times n; \mathbb{R})$. Write $\omega \in \Omega^1(\operatorname{Fr}(TM); \mathfrak{g})$ for the principal connection on $\operatorname{Fr}(TM)$ induced by $\nabla$ and $\Omega \in \Omega^2(\operatorname{Fr}(TM); \mathfrak{g})$ for its curvature.

Fix a coordinate chart $(U, x^1, \dots, x^n)$ on $M$ and let
$$
s = (\partial_1, \dots, \partial_n) : U \to \operatorname{Fr}(TM)|_U, \qquad \partial_k := \frac{\partial}{\partial x^k},
$$
be the associated coordinate section (the local frame of $TM$ read as a section of the frame bundle). Prove the following two identifications.

1. **The local curvature form is the matrix of Cartan's curvature 2-forms.** The local curvature form $F := s^* \Omega \in \Omega^2(U; \mathfrak{gl}(n, \mathbb{R}))$ has as its entries exactly the curvature 2-forms $\Omega^a{}_b$ of the Levi-Civita connection in the frame $(\partial_a)$, that is
$$
F^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b = \Omega^a{}_b, \qquad \omega^a{}_b := \Gamma^a{}_{bk}\, dx^k,
$$
where $\omega^a{}_b$ are the Cartan connection 1-forms and $\Gamma^a{}_{bk}$ the Christoffel symbols of $\nabla$; equivalently $F^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$, with $R^a{}_{bcd}$ the components of the Riemann curvature tensor.

2. **The principal Bianchi identity is the second Bianchi identity of Riemannian geometry.** The Bianchi identity for the principal connection $\omega$, written in the coordinate section, reads
$$
dF^a{}_b + \omega^a{}_c \wedge F^c{}_b - F^a{}_c \wedge \omega^c{}_b = 0,
$$
and this differential-form identity is equivalent to the componentwise second Bianchi identity of the Levi-Civita connection,
$$
\nabla_e R^a{}_{bcd} + \nabla_c R^a{}_{bde} + \nabla_d R^a{}_{bec} = 0.
$$

You may use the two frame-bundle theorems of this chapter as black boxes; the task is to *identify* the principal-bundle objects with the Riemannian-geometry objects, not to reprove the Riemannian second Bianchi identity from scratch.

**Recall:**

The standing conventions are those of the series. Lie groups act on principal bundles on the right, $R_g(p) = p \cdot g$. A connection on a principal bundle is a form $\omega \in \Omega^1(P; \mathfrak{g})$ with $\omega(\xi_P) = \xi$ and $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$; its local connection form in a local section $s$ is $A_s = s^*\omega \in \Omega^1(U; \mathfrak{g})$, and its local curvature form is $F_s = s^*\Omega$. For a matrix Lie algebra the bracket of $\mathfrak{g}$-valued forms is the matrix commutator wedge: for $\alpha \in \Omega^p(M; \mathfrak{g})$ and $\beta \in \Omega^q(M; \mathfrak{g})$,
$$
[\alpha \wedge \beta] = \alpha \wedge \beta - (-1)^{pq}\, \beta \wedge \alpha,
$$
so that for a 1-form $A$ one has $[A \wedge A] = 2\, A \wedge A$, and for a 1-form $A$ and a 2-form $F$ one has $[A \wedge F] = A \wedge F - F \wedge A$. Throughout, repeated indices are summed, all indices $a, b, c, d, e, f, g, k, m$ run over $1, \dots, n$ (with $f, g$ used only as dummy coframe indices in Step 4), and $\partial_k f = \partial f / \partial x^k$.

The Christoffel symbols are fixed by $\nabla_{\partial_k}\partial_b = \Gamma^a{}_{bk}\, \partial_a$; because the Levi-Civita connection is torsion-free, $\nabla_{\partial_k}\partial_b - \nabla_{\partial_b}\partial_k = [\partial_k, \partial_b] = 0$ (coordinate vector fields commute), so the Christoffel symbols are symmetric in the two lower indices, $\Gamma^a{}_{bk} = \Gamma^a{}_{kb}$ (see [[Def - Christoffel Symbols]]). The Riemann curvature tensor is $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$, with coordinate components $R(\partial_c, \partial_d)\partial_b = R^a{}_{bcd}\,\partial_a$ (see [[Def - Riemann Curvature Tensor]]); in particular $R^a{}_{bcd} = -R^a{}_{bdc}$.

The two frame-bundle results that supply the setup:

![[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle#Statement]]

![[Thm - Structure Equation for the Curvature#Statement]]

The principal Bianchi identity, which drives part 2:

![[Thm - Bianchi Identity for a Principal Connection#Statement]]

The two Riemannian-geometry objects the exercise identifies these with:

![[Def - Curvature 2-Forms (Cartan)#The Definition]]

![[Thm - First and Second Bianchi Identities#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *dictionary* exercise: two theories — the principal-bundle calculus of $\operatorname{Fr}(TM)$ and the classical Cartan calculus of moving frames on a Riemannian manifold — describe the same connection, and the task is to check that their formulas are literally the same formula once the objects are named consistently. The whole difficulty is one of translation, not of new geometry. Whenever two frameworks compute the curvature of *the same* covariant derivative, the outputs must agree; the exercise is to see *why the symbols line up*, term by term, so that the agreement is a proof rather than a slogan.

**Assumption pattern.** The hypotheses are that $\nabla$ is the Levi-Civita connection (torsion-free and metric) and that the structure group of the frame bundle is $G = GL(n, \mathbb{R})$. The structure group being a *matrix* group is what collapses the bracket $[\alpha \wedge \beta]$ of $\mathfrak{g}$-valued forms into the ordinary matrix wedge, so that the principal structure equation $F = dA + \tfrac{1}{2}[A \wedge A]$ becomes Cartan's $\Omega = d\omega + \omega \wedge \omega$ with no factor of $\tfrac{1}{2}$. Torsion-freeness is used only in part 2, and only through the symmetry $\Gamma^a{}_{bk} = \Gamma^a{}_{kb}$, which is exactly what kills two of the five terms of $\nabla_e R^a{}_{bcd}$ under antisymmetrisation and turns the form-Bianchi into the *cyclic* tensor identity.

**Theorem routing.** Part 1 routes through [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]] (which gives $s^*\omega = A(\nabla, s)$, the connection matrix, with entries the Cartan connection 1-forms) followed by [[Thm - Structure Equation for the Curvature]] (which gives $s^*\Omega = dA + \tfrac{1}{2}[A \wedge A]$, equal to $dA + A \wedge A$ for $GL(n, \mathbb{R})$); comparing with [[Def - Curvature 2-Forms (Cartan)]] and [[Thm - Cartan's Second Structural Equation]] finishes it. Part 2 routes through [[Thm - Bianchi Identity for a Principal Connection]] (local form $dF + [A \wedge F] = 0$) and then a direct component expansion that reduces the resulting 3-form identity to [[Thm - First and Second Bianchi Identities|the second Bianchi identity]] of Riemannian geometry.

**Key decision point.** The one move that makes part 2 rigorous rather than hand-waving is to recognise that *a $\mathfrak{gl}(n)$-valued 3-form vanishes if and only if the total antisymmetrisation of its component array vanishes*, and to combine this with the antisymmetry $R^a{}_{bcd} = -R^a{}_{bdc}$ already present in the last two indices. The torsion-free symmetry of the Christoffel symbols then removes the two terms of the covariant derivative that carry a symmetric lower-index pair against an antisymmetric wedge, and the remaining antisymmetrisation over three indices, applied to an array already antisymmetric in two of them, collapses to the three-term *cyclic* sum. Naming these two symmetries at the right moment is the entire exercise.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory IV — Connections and Curvature on Principal Bundles#Legal Operations|the topic page's Legal Operations]]. The topic page is assembled after the subpages, so the operations are named descriptively here.

1. **Pull a global principal form back by a local section to read it off in a gauge.** Both the connection $\omega$ and the curvature $\Omega$ live on the total space $\operatorname{Fr}(TM)$; to compute with them one applies $s^*$ for a chosen local section $s$, producing the local connection form $A_s = s^*\omega$ and the local curvature form $F_s = s^*\Omega$ on the base. Here the section is the coordinate frame $s = (\partial_1, \dots, \partial_n)$, and the pull-back turns the abstract structure equation on $P$ into an equation among ordinary matrix-valued forms on $U$, using that pull-back commutes with $d$ and with the wedge product.

2. **Replace the bracket of matrix-valued forms by the matrix wedge for $GL(n)$.** For the structure group $GL(n, \mathbb{R})$, whose Lie algebra bracket is the commutator, the bracket $[\alpha \wedge \beta]$ of $\mathfrak{g}$-valued forms equals $\alpha \wedge \beta - (-1)^{pq}\beta \wedge \alpha$. This is the operation that removes the factor $\tfrac{1}{2}$ from the structure equation ($[A \wedge A] = 2\, A \wedge A$) and rewrites the covariant-derivative bracket $[A \wedge F]$ in the Bianchi identity as $A \wedge F - F \wedge A$, matching Cartan's form of the identity exactly.

3. **Recognise a differential-form identity as a tensor identity by antisymmetrising components.** A $k$-form is zero if and only if its fully antisymmetric component array is zero. Applying this to the $\mathfrak{gl}(n)$-valued 3-form $dF + [\omega \wedge F]$ converts the form-level Bianchi identity into a statement about the antisymmetrisation of $\nabla_e R^a{}_{bcd}$, which — because $R$ is already antisymmetric in its last two indices — is the cyclic second Bianchi identity.

---

# Hints

> [!note]- Hint 1
> You are not asked to compute any Christoffel symbol or any curvature component in a specific chart. Every quantity you need is delivered by a theorem of this chapter. Start by writing down what [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]] says the pull-back $s^*\omega$ is for the coordinate section $s = (\partial_1, \dots, \partial_n)$, and compare that matrix of 1-forms with the Cartan connection 1-forms $\omega^a{}_b$ of the same frame.

> [!note]- Hint 2
> For part 1, apply [[Thm - Structure Equation for the Curvature]] to get $s^*\Omega = dA + \tfrac{1}{2}[A \wedge A]$ with $A = s^*\omega$. The structure group is $GL(n, \mathbb{R})$, a matrix group; what does $\tfrac{1}{2}[A \wedge A]$ equal for a matrix-valued 1-form? Once the $\tfrac{1}{2}$ is gone you are looking at Cartan's second structural equation.

> [!note]- Hint 3
> For part 2, write the local Bianchi identity from [[Thm - Bianchi Identity for a Principal Connection]] as $dF + [A \wedge F] = 0$ and expand the matrix bracket of a 1-form with a 2-form. You should land on $dF + \omega \wedge F - F \wedge \omega = 0$ entrywise. Now substitute $F^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$ and $\omega^a{}_b = \Gamma^a{}_{bk}\, dx^k$ and expand the three terms in the coordinate coframe.

> [!note]- Hint 4
> After substituting, you have a $\mathfrak{gl}(n)$-valued 3-form set to zero. Two of the terms coming from the derivatives of $R$ will contain a Christoffel symbol symmetric in two indices wedged against $dx^e \wedge dx^c$ (or $dx^e \wedge dx^d$) antisymmetric in the same two indices — these vanish. The surviving three terms are $\tfrac{1}{2}(\nabla_e R^a{}_{bcd})\, dx^e \wedge dx^c \wedge dx^d$. A 3-form with these components vanishes if and only if the antisymmetrisation over $(e, c, d)$ vanishes; use $R^a{}_{bcd} = -R^a{}_{bdc}$ to reduce that antisymmetrisation to a cyclic sum.

---

# Solution

The plan has two independent halves. In part 1 we pull the principal connection and curvature back by the coordinate section and read off, from the two frame-bundle theorems of this chapter, that the resulting matrices of forms are the Cartan connection and curvature 1- and 2-forms of the Levi-Civita connection; the only nontrivial point is that for the matrix group $GL(n, \mathbb{R})$ the principal structure equation is Cartan's second structural equation on the nose. In part 2 we take the local principal Bianchi identity, expand it in the coordinate coframe, use the torsion-free symmetry of the Christoffel symbols to discard two terms, and use the antisymmetry of the Riemann tensor in its last two indices to collapse the surviving 3-form identity to the cyclic second Bianchi identity.

**Step 1: The local connection form is the Cartan connection matrix.**

Applying $s^*$ to the induced principal connection $\omega$ in the coordinate section gives the connection matrix of $\nabla$ in the coordinate frame, whose entries are the Cartan connection 1-forms $\omega^a{}_b = \Gamma^a{}_{bk}\, dx^k$.

> [!note]- Derivation
> By [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]], part (a): the principal connection $\omega$ on $\operatorname{Fr}(TM)$ induced by $\nabla$ is the unique connection satisfying $e^*\omega = A(\nabla, e)$ for every local frame $e$, where $A(\nabla, e)$ is the connection matrix defined by $\nabla e = e \cdot A(\nabla, e)$ (the convention of [[Def - Connection Matrix and Local Form of a Connection|chapter II]]). Taking $e = s = (\partial_1, \dots, \partial_n)$ and writing $A := s^*\omega$, this says
> $$
> \nabla \partial_b = \partial_a \, A^a{}_b \qquad \text{(definition of the connection matrix, } e = s\text{)}.
> $$
> Evaluating against the coordinate direction $\partial_k$ and using the definition of the Christoffel symbols $\nabla_{\partial_k}\partial_b = \Gamma^a{}_{bk}\,\partial_a$ (from [[Def - Christoffel Symbols]]),
> $$
> \partial_a\, A^a{}_b(\partial_k) = \nabla_{\partial_k}\partial_b = \Gamma^a{}_{bk}\,\partial_a \qquad \text{(evaluate the previous line on } \partial_k\text{)},
> $$
> and since $(\partial_a)$ is a basis of each fibre this forces $A^a{}_b(\partial_k) = \Gamma^a{}_{bk}$ for every $k$, i.e.
> $$
> A^a{}_b = \Gamma^a{}_{bk}\, dx^k =: \omega^a{}_b \qquad \text{(read off each coefficient in the coframe } dx^k\text{)}.
> $$
> This is precisely the definition of the **Cartan connection 1-forms** $\omega^a{}_b$ of $\nabla$ in the frame $(\partial_a)$ (see [[Def - Connection 1-Forms (Cartan)]]). The equality $A^a{}_b(\partial_k) = \Gamma^a{}_{bk}$ is part (c) of the frame-bundle theorem specialised from a general frame to the coordinate frame, and confirms the standing convention $\Gamma^a{}_{bk} = (s^*\omega(\partial_k))^a{}_b$.

**Step 2: The local curvature form is the Cartan curvature matrix.**

Pulling the principal curvature back by the same section and using the structure equation gives $F = dA + A \wedge A$, whose entries are Cartan's curvature 2-forms $\Omega^a{}_b$; expanding in the coframe yields $F^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$.

> [!note]- Derivation
> By [[Thm - Structure Equation for the Curvature]], part (d): for any local section $s_\alpha$ the local curvature form satisfies
> $$
> F_\alpha := s_\alpha^*\Omega = dA_\alpha + \tfrac{1}{2}[A_\alpha \wedge A_\alpha] \qquad \text{(local structure equation)},
> $$
> and for a matrix group $F_\alpha = dA_\alpha + A_\alpha \wedge A_\alpha$. Here the structure group is $G = GL(n, \mathbb{R})$, whose Lie-algebra bracket is the commutator, so by the matrix-bracket identity $[A \wedge A] = A \wedge A - (-1)^{1 \cdot 1} A \wedge A = 2\, A \wedge A$ for the 1-form $A$; therefore $\tfrac{1}{2}[A \wedge A] = A \wedge A$ and, with $A = s^*\omega = (\omega^a{}_b)$ from Step 1,
> $$
> F^a{}_b = (dA)^a{}_b + (A \wedge A)^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b \qquad \text{(structure equation, } \tfrac{1}{2}[A\wedge A] = A\wedge A\text{, matrix multiplication of forms)}.
> $$
> The right-hand side is, by definition, the matrix of **Cartan's curvature 2-forms** $\Omega^a{}_b := d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$, which is [[Thm - Cartan's Second Structural Equation|Cartan's second structural equation]]. Hence $F^a{}_b = \Omega^a{}_b$, establishing the first identification.
>
> For the coframe expansion, recall from [[Def - Curvature 2-Forms (Cartan)]] that for $E = TM$ the curvature 2-forms have components $\Omega^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$, where $R^a{}_{bcd}$ are the components of the Riemann curvature tensor in the coordinate frame (the coefficient $\tfrac{1}{2}$ compensates the double-count in the antisymmetric sum over $c, d$). This is verified directly: evaluating the tensorial identity $\nabla\nabla s = e\, \Omega\, s$ on $\partial_c, \partial_d$ recovers $\Omega^a{}_b(\partial_c, \partial_d) = R^a{}_{bcd}$, and a 2-form $\Omega^a{}_b$ with these values on the basis pairs is $\Omega^a{}_b = \tfrac{1}{2}\Omega^a{}_b(\partial_c, \partial_d)\, dx^c \wedge dx^d = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$. Combining with $F^a{}_b = \Omega^a{}_b$,
> $$
> F^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d, \qquad R^a{}_{bcd} = -R^a{}_{bdc}.
> $$

**Step 3: The principal Bianchi identity, written locally, is $dF + \omega \wedge F - F \wedge \omega = 0$.**

The Bianchi identity for the induced principal connection, pulled back to the coordinate section, becomes the exterior covariant derivative of the curvature matrix set to zero.

> [!note]- Derivation
> By [[Thm - Bianchi Identity for a Principal Connection]], part (c): the local curvature form of any principal connection satisfies
> $$
> dF_\alpha + [A_\alpha \wedge F_\alpha] = 0 \qquad \text{(local Bianchi identity)},
> $$
> the coordinate expression of $d^{\nabla_\omega} F_\omega = 0$ for the induced connection on the adjoint bundle. For the matrix group $GL(n, \mathbb{R})$ we expand the bracket of the 1-form $A = (\omega^a{}_b)$ with the 2-form $F = (F^a{}_b)$ using the matrix-bracket identity with $p = 1$, $q = 2$, so $(-1)^{pq} = (-1)^2 = 1$:
> $$
> [A \wedge F] = A \wedge F - (-1)^{1 \cdot 2} F \wedge A = A \wedge F - F \wedge A \qquad \text{(matrix-bracket identity, } p=1,\, q=2\text{)}.
> $$
> Entrywise, with $A = (\omega^a{}_b)$ and $F = (F^a{}_b)$, matrix multiplication of forms gives $(A \wedge F)^a{}_b = \omega^a{}_c \wedge F^c{}_b$ and $(F \wedge A)^a{}_b = F^a{}_c \wedge \omega^c{}_b$, so the local Bianchi identity is
> $$
> dF^a{}_b + \omega^a{}_c \wedge F^c{}_b - F^a{}_c \wedge \omega^c{}_b = 0 \qquad \text{(substitute the expanded bracket).}
> $$
> This is exactly the exterior covariant derivative $d^\nabla F$ of the $\operatorname{End}(TM)$-valued 2-form $F$ in the frame $(\partial_a)$, set to zero — the differential-form second Bianchi identity as it appears in [[Def - Curvature 2-Forms (Cartan)]].

**Step 4: The form-Bianchi identity is equivalent to the cyclic tensorial second Bianchi identity.**

Substituting $F^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$ and $\omega^a{}_b = \Gamma^a{}_{bk}\, dx^k$ into $dF + \omega \wedge F - F \wedge \omega = 0$, discarding the two terms carrying a symmetric Christoffel pair against an antisymmetric wedge, and antisymmetrising, we recover $\nabla_e R^a{}_{bcd} + \nabla_c R^a{}_{bde} + \nabla_d R^a{}_{bec} = 0$.

> [!note]- Derivation
> **Compute each of the three terms in the coordinate coframe.** Write $F^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$ and $\omega^a{}_b = \Gamma^a{}_{bk}\, dx^k$.
>
> The exterior derivative:
> $$
> dF^a{}_b = \tfrac{1}{2}\, \partial_e R^a{}_{bcd}\; dx^e \wedge dx^c \wedge dx^d \qquad \text{(differentiate the coefficient; } d(dx^c\wedge dx^d)=0\text{).}
> $$
>
> The first connection term, relabelling the summed frame index and the coframe indices:
> $$
> \omega^a{}_c \wedge F^c{}_b = \Gamma^a{}_{ce}\, dx^e \wedge \tfrac{1}{2} R^c{}_{bfg}\, dx^f \wedge dx^g = \tfrac{1}{2}\, \Gamma^a{}_{me} R^m{}_{bcd}\; dx^e \wedge dx^c \wedge dx^d
> $$
> (the dummy $c \mapsto m$, $f \mapsto c$, $g \mapsto d$ after collecting the coframe factors).
>
> The second connection term, reordering the wedge $dx^f \wedge dx^g \wedge dx^e = dx^e \wedge dx^f \wedge dx^g$ (a cyclic permutation of three factors, sign $+1$):
> $$
> F^a{}_c \wedge \omega^c{}_b = \tfrac{1}{2} R^a{}_{cfg}\, dx^f \wedge dx^g \wedge \Gamma^c{}_{be}\, dx^e = \tfrac{1}{2}\, \Gamma^m{}_{be} R^a{}_{mcd}\; dx^e \wedge dx^c \wedge dx^d
> $$
> (the same relabelling $c \mapsto m$, $f \mapsto c$, $g \mapsto d$).
>
> **Assemble the left-hand side.** Adding the first two and subtracting the third,
> $$
> dF^a{}_b + \omega^a{}_c \wedge F^c{}_b - F^a{}_c \wedge \omega^c{}_b = \tfrac{1}{2}\Big(\partial_e R^a{}_{bcd} + \Gamma^a{}_{me} R^m{}_{bcd} - \Gamma^m{}_{be} R^a{}_{mcd}\Big)\, dx^e \wedge dx^c \wedge dx^d \qquad \text{(combine the three displayed lines).}
> $$
>
> **Recognise the bracketed array as a partial covariant derivative.** The covariant derivative of the $(1,3)$-tensor $R$ in the coordinate frame is
> $$
> \nabla_e R^a{}_{bcd} = \partial_e R^a{}_{bcd} + \Gamma^a{}_{me} R^m{}_{bcd} - \Gamma^m{}_{be} R^a{}_{mcd} - \Gamma^m{}_{ce} R^a{}_{bmd} - \Gamma^m{}_{de} R^a{}_{bcm} \qquad \text{(covariant-derivative rule, one }+\Gamma\text{ per upper index, one }-\Gamma\text{ per lower index).}
> $$
> The last two terms of $\nabla_e R^a{}_{bcd}$ vanish when contracted against $dx^e \wedge dx^c \wedge dx^d$: the coefficient $-\Gamma^m{}_{ce} R^a{}_{bmd}$ is symmetric in $(c, e)$ because $\Gamma^m{}_{ce} = \Gamma^m{}_{ec}$ (**torsion-freeness of the Levi-Civita connection**, from [[Def - Levi-Civita Connection]]), while $dx^e \wedge dx^c$ is antisymmetric in $(c, e)$, so the contraction of a symmetric with an antisymmetric array is zero; identically, $-\Gamma^m{}_{de} R^a{}_{bcm}$ is symmetric in $(d, e)$ against $dx^e \wedge dx^d$ antisymmetric in $(d, e)$, hence also drops. Therefore
> $$
> \big(\nabla_e R^a{}_{bcd}\big)\, dx^e \wedge dx^c \wedge dx^d = \big(\partial_e R^a{}_{bcd} + \Gamma^a{}_{me} R^m{}_{bcd} - \Gamma^m{}_{be} R^a{}_{mcd}\big)\, dx^e \wedge dx^c \wedge dx^d \qquad \text{(the two symmetric-against-antisymmetric terms vanish),}
> $$
> and combining with the assembled left-hand side,
> $$
> dF^a{}_b + \omega^a{}_c \wedge F^c{}_b - F^a{}_c \wedge \omega^c{}_b = \tfrac{1}{2}\, \big(\nabla_e R^a{}_{bcd}\big)\, dx^e \wedge dx^c \wedge dx^d \qquad \text{(substitute the previous identity).}
> $$
>
> **Convert vanishing of the 3-form to a component identity.** A differential 3-form is zero if and only if its totally antisymmetric component array is zero. Writing $T_{ecd} := \nabla_e R^a{}_{bcd}$ (with $a, b$ fixed spectator indices), the form $\tfrac{1}{2} T_{ecd}\, dx^e \wedge dx^c \wedge dx^d$ vanishes if and only if the antisymmetrisation $T_{[ecd]} = 0$. Because $T_{ecd}$ is already antisymmetric in its last two indices — $T_{ecd} = \nabla_e R^a{}_{bcd} = -\nabla_e R^a{}_{bdc} = -T_{edc}$, since $\nabla_e$ preserves the antisymmetry $R^a{}_{bcd} = -R^a{}_{bdc}$ — the six signed permutations of $(e, c, d)$ pair up:
> $$
> 6\, T_{[ecd]} = \sum_{\sigma \in S_3} \operatorname{sgn}(\sigma)\, T_{\sigma(e)\sigma(c)\sigma(d)} = 2\big(T_{ecd} + T_{cde} + T_{dec}\big) \qquad \text{(each cyclic term appears twice with equal sign, by antisymmetry in the last two slots).}
> $$
> Hence $T_{[ecd]} = \tfrac{1}{3}\big(T_{ecd} + T_{cde} + T_{dec}\big)$, and the form-Bianchi identity of Step 3 is equivalent to the vanishing of the cyclic sum:
> $$
> T_{ecd} + T_{cde} + T_{dec} = \nabla_e R^a{}_{bcd} + \nabla_c R^a{}_{bde} + \nabla_d R^a{}_{bec} = 0 \qquad \text{(vanishing of the 3-form } \Longleftrightarrow \text{ vanishing of the cyclic sum).}
> $$
> This is exactly the componentwise **second Bianchi identity** of the Levi-Civita connection, [[Thm - First and Second Bianchi Identities]]. We have therefore shown the two Bianchi identities coincide, without invoking the Riemannian-geometry proof of the identity: the principal-bundle Bianchi identity, specialised to $\operatorname{Fr}(TM)$ and written in the coordinate section, *is* the second Bianchi identity of Riemannian geometry.

> [!note]- Complete formal solution
> **Setup.** Let $(M, g)$ be a Riemannian $n$-manifold, $\nabla$ its Levi-Civita connection on $TM$, $\operatorname{Fr}(TM) \xrightarrow{\pi} M$ the frame bundle with structure group $G = GL(n, \mathbb{R})$ and $\mathfrak{g} = \mathfrak{gl}(n, \mathbb{R})$, $\omega$ the induced principal connection, $\Omega$ its curvature, and $s = (\partial_1, \dots, \partial_n)$ the coordinate section over a chart $(U, x^1, \dots, x^n)$. Write $A := s^*\omega$, $F := s^*\Omega$.
>
> **Part 1.** By [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle]] (part a), $\omega$ is characterised by $e^*\omega = A(\nabla, e)$ for every local frame $e$, where $\nabla e = e \cdot A(\nabla, e)$. For $e = s$ this gives $\nabla \partial_b = \partial_a A^a{}_b$; evaluating on $\partial_k$ and using $\nabla_{\partial_k}\partial_b = \Gamma^a{}_{bk}\partial_a$ (definition of the Christoffel symbols) yields $A^a{}_b(\partial_k) = \Gamma^a{}_{bk}$, hence $A^a{}_b = \Gamma^a{}_{bk}\, dx^k =: \omega^a{}_b$, the Cartan connection 1-forms. By [[Thm - Structure Equation for the Curvature]] (part d), $F = dA + \tfrac{1}{2}[A \wedge A]$; since $G$ is a matrix group and $A$ is a 1-form, $[A \wedge A] = 2 A \wedge A$, so $F = dA + A \wedge A$, i.e. entrywise
> $$
> F^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b = \Omega^a{}_b,
> $$
> which is Cartan's second structural equation ([[Thm - Cartan's Second Structural Equation]]); the $F^a{}_b$ are precisely the curvature 2-forms of $\nabla$ in the frame $(\partial_a)$. By [[Def - Curvature 2-Forms (Cartan)]], $\Omega^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$ with $R^a{}_{bcd}$ the Riemann tensor components; hence $F^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$. This proves the first identification.
>
> **Part 2.** By [[Thm - Bianchi Identity for a Principal Connection]] (part c), $dF + [A \wedge F] = 0$. For $GL(n, \mathbb{R})$ with $A$ a 1-form and $F$ a 2-form, $[A \wedge F] = A \wedge F - F \wedge A$, so entrywise
> $$
> dF^a{}_b + \omega^a{}_c \wedge F^c{}_b - F^a{}_c \wedge \omega^c{}_b = 0. \tag{$\ast$}
> $$
> Substituting $F^a{}_b = \tfrac{1}{2} R^a{}_{bcd}\, dx^c \wedge dx^d$ and $\omega^a{}_b = \Gamma^a{}_{bk}\, dx^k$ and collecting coframe factors (relabelling dummy indices and using the cyclic reordering $dx^f \wedge dx^g \wedge dx^e = dx^e \wedge dx^f \wedge dx^g$):
> $$
> dF^a{}_b = \tfrac{1}{2}\partial_e R^a{}_{bcd}\, dx^e \wedge dx^c \wedge dx^d, \quad \omega^a{}_c \wedge F^c{}_b = \tfrac{1}{2}\Gamma^a{}_{me} R^m{}_{bcd}\, dx^e \wedge dx^c \wedge dx^d, \quad F^a{}_c \wedge \omega^c{}_b = \tfrac{1}{2}\Gamma^m{}_{be} R^a{}_{mcd}\, dx^e \wedge dx^c \wedge dx^d.
> $$
> Thus $(\ast)$ reads $\tfrac{1}{2}(\partial_e R^a{}_{bcd} + \Gamma^a{}_{me} R^m{}_{bcd} - \Gamma^m{}_{be} R^a{}_{mcd})\, dx^e \wedge dx^c \wedge dx^d = 0$. The covariant derivative $\nabla_e R^a{}_{bcd} = \partial_e R^a{}_{bcd} + \Gamma^a{}_{me} R^m{}_{bcd} - \Gamma^m{}_{be} R^a{}_{mcd} - \Gamma^m{}_{ce} R^a{}_{bmd} - \Gamma^m{}_{de} R^a{}_{bcm}$ has its last two terms killed under the wedge because $\Gamma^m{}_{ce} = \Gamma^m{}_{ec}$ and $\Gamma^m{}_{de} = \Gamma^m{}_{ed}$ (torsion-freeness) are symmetric against the antisymmetric $dx^e \wedge dx^c$, $dx^e \wedge dx^d$. Hence $(\ast)$ is equivalent to $\tfrac{1}{2}(\nabla_e R^a{}_{bcd})\, dx^e \wedge dx^c \wedge dx^d = 0$. A 3-form vanishes if and only if its total antisymmetrisation does; setting $T_{ecd} = \nabla_e R^a{}_{bcd}$, which is antisymmetric in $(c, d)$, the antisymmetrisation collapses to $T_{[ecd]} = \tfrac{1}{3}(T_{ecd} + T_{cde} + T_{dec})$. Therefore $(\ast)$ holds if and only if
> $$
> \nabla_e R^a{}_{bcd} + \nabla_c R^a{}_{bde} + \nabla_d R^a{}_{bec} = 0,
> $$
> the second Bianchi identity of [[Thm - First and Second Bianchi Identities]]. This proves the second identification. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to declare part 2 finished the moment one writes $dF + [A \wedge F] = 0$ and says "this is the Bianchi identity", identifying it with the Riemannian one by inspection. That is a coincidence of *names*, not a proof: the principal Bianchi identity is a statement about a $\mathfrak{gl}(n)$-valued 3-form, whereas the Riemannian second Bianchi identity is a statement about the cyclic sum of covariant derivatives of a $(1,3)$-tensor. The two are equal only after (i) rewriting the matrix bracket $[A \wedge F]$ as $A \wedge F - F \wedge A$, (ii) using torsion-freeness to discard two terms of $\nabla_e R^a{}_{bcd}$, and (iii) converting the 3-form's vanishing into the cyclic component identity via antisymmetrisation. Omitting step (ii) is the common error: without torsion-freeness the form identity would still hold (it holds for any affine connection on any vector bundle), but it would translate into a *corrected* cyclic identity carrying torsion terms, not the clean second Bianchi identity — the corrected version is what one gets for a general connection with torsion. The clean coincidence is special to the Levi-Civita connection.

> [!note]- Independent sanity check
> Two consistency checks. First, the **abelian reduction**: if instead of $GL(n)$ the structure group were abelian (as for a $U(1)$ line bundle), the terms $\omega \wedge F$ and $F \wedge \omega$ would cancel and $(\ast)$ would read $dF = 0$; correspondingly, for a $1 \times 1$ curvature the "cyclic" tensor identity degenerates to $\partial_{[e} R_{cd]} = 0$, i.e. $dF = 0$ again — the two pictures agree in the abelian case, as they must. Second, the **low-dimensional check**: on a surface ($n = 2$) the space of $3$-forms on the base is the zero space, so the form-Bianchi identity $(\ast)$ holds automatically; and indeed the cyclic second Bianchi sum $\nabla_e R^a{}_{bcd} + \nabla_c R^a{}_{bde} + \nabla_d R^a{}_{bec}$ equals $3\,\nabla_{[e} R^a{}_{|b|cd]}$ (the total antisymmetrisation over $(e, c, d)$, since $R$ is already antisymmetric in $(c, d)$), and a totally antisymmetric array in three indices each ranging over a two-element set must vanish, because any triple $(e, c, d)$ then repeats a value. Both sides are therefore identically zero. The identification survives both degenerations.

---

# Key Takeaways

**The frame bundle is where "connection" and "gauge field" become the same object, and this exercise is the proof that the two curvature calculi built on top of them agree line for line.** The Cartan moving-frame formalism ($\omega^a{}_b$, $\Omega^a{}_b = d\omega + \omega \wedge \omega$) and the principal-bundle formalism ($A = s^*\omega$, $F = dA + \tfrac{1}{2}[A \wedge A]$) are not two analogies for the curvature of a metric connection; they are two coordinate presentations of one geometric object, the connection on $\operatorname{Fr}(TM)$. The reusable principle is that whenever a covariant derivative on a vector bundle is reinterpreted as a principal connection on its frame bundle, every downstream invariant — connection matrix, curvature matrix, Bianchi identity, characteristic form — is carried across by pulling back along a local section, and the transported formula is the classical one with the group's bracket written out. The trigger for reaching for this identification is any statement that mixes the language of Christoffel symbols with the language of gauge potentials; the response is to fix a local frame, pull the principal forms back by it, and compare.

**The factor of $\tfrac{1}{2}$ in the structure equation and the disappearance of two terms in the Bianchi identity are both governed by a single diagnostic: symmetric-versus-antisymmetric pairing under the wedge.** In the structure equation, the bracket $[A \wedge A] = 2 A \wedge A$ carries a $2$ precisely because the wedge of a matrix-valued 1-form with itself already antisymmetrises the two slots, doubling the commutator; this is why the principal $\tfrac{1}{2}[A \wedge A]$ and the Cartan $A \wedge A$ are the same. In the Bianchi identity, the torsion-free symmetry $\Gamma^a{}_{bk} = \Gamma^a{}_{kb}$ pairs against an antisymmetric $dx \wedge dx$ and annihilates two of the five terms of $\nabla_e R^a{}_{bcd}$. The transferable diagnostic is: **before expanding any contraction of a Christoffel or curvature array against wedge products, sort each index pair into symmetric and antisymmetric parts, because only the matching parity survives.** This single habit turns most moving-frame computations from bookkeeping into two-line arguments, and it is the mechanism behind the algebraic Bianchi identity as well (there the torsion-free symmetry kills the inhomogeneous term of $\Omega^a{}_b \wedge \sigma^b$).

**A differential-form identity and a tensor identity are interconvertible through antisymmetrisation, and knowing which direction is cheaper is a genuine strategic choice.** The form-level Bianchi identity $dF + [\omega \wedge F] = 0$ is one clean equation; its tensor avatar is a cyclic sum over three indices. This exercise moved from the form to the tensor because the target ([[Thm - First and Second Bianchi Identities|the Riemannian second Bianchi identity]]) was stated tensorially, but the converse translation is equally routine and is often the better one — Chern–Weil theory, for instance, keeps everything at the form level precisely to avoid the index proliferation. The reusable recognition is that *a rank-$k$ form is zero if and only if the total antisymmetrisation of its component array is zero*, and that when the array already has some antisymmetry (here $R^a{}_{b[cd]}$), the total antisymmetrisation collapses to a smaller sum (here the three-term cyclic sum) with a computable combinatorial factor. The trigger is any identity that is natural on one side (forms) but demanded on the other (components); the response is to antisymmetrise and count.

This exercise is the curvature companion to [[Ex - Christoffel Symbols are the Local Connection Form of the Frame Bundle]], which performs the same identification one level down for the connection form; together they establish the full dictionary between the covariant derivative on $TM$ and the principal connection on $\operatorname{Fr}(TM)$. The abelian analogue is worked in [[Ex - Curvature of a Connection on a Trivial Bundle and the Abelian Case]], and the same structure-equation-to-Cartan comparison, run for the tautological line bundle instead of the tangent bundle, appears in [[Ex - The Induced Connection on the Tautological Bundle from the Hopf Connection]].
