---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Bundle-Valued Differential Forms"
  - "Thm - Existence of Smooth Bump Functions"
  - "Def - Section of a Vector Bundle"
  - "Def - Local Frame"
  - "Thm - Local Frames Span Sections"
  - "Def - Operations on Vector Bundles and Pull-Back Bundles"
tags: [geometry, gauge-theory, vector-bundles, connections]
---

# Notation

This page depends on the following standing conventions of the series. Manifolds are smooth, Hausdorff, and second countable, and "smooth" means $C^\infty$. For a vector bundle $E \to M$ we write $\Gamma(E)$ for its smooth global sections and $\Gamma(U; E)$ for the smooth sections over an open subset $U \subseteq M$; we write $\Omega^p(M; E) = \Gamma(\Lambda^p T^*M \otimes E)$ for the $E$-valued $p$-forms. A connection on a vector bundle is a covariant derivative $\nabla : \Gamma(E) \to \Omega^1(M; E)$ satisfying the Leibniz rule $\nabla(fs) = df \otimes s + f \nabla s$; the directional derivative of a section $s$ along a vector field $v$ is $\nabla_v s := \iota_v \nabla s$. No connection matrix, Hodge star, or orientation enters this page.

The symbols used on this page are the following.

- $M$ is a smooth manifold of dimension $n$. $C^\infty(M)$ is the commutative ring of smooth real-valued functions on $M$.
- $\pi_E : E \to M$ and $\pi_F : F \to M$ are smooth real [[Def - Vector Bundle|vector bundles]] of ranks $k$ and $l$ respectively, with fibres $E_m = \pi_E^{-1}(m)$ and $F_m = \pi_F^{-1}(m)$, real vector spaces of dimensions $k$ and $l$. In Part II of the theorem, $E_1, \dots, E_r$ are smooth real vector bundles over $M$ of ranks $k_1, \dots, k_r$.
- $\Gamma(E)$ is the space of smooth [[Def - Section of a Vector Bundle|sections]] $s : M \to E$, $\pi_E \circ s = \mathrm{id}_M$. It is a real vector space and a $C^\infty(M)$-module under the pointwise operations $(s + t)(m) = s(m) + t(m)$ and $(fs)(m) = f(m)\, s(m)$, the right-hand sides computed in the vector space $E_m$. We write $s(m) \in E_m$ for the value of $s$ at $m$ and $s|_U \in \Gamma(U; E)$ for its restriction to an open set $U$.
- $\Omega^p(M; F) = \Gamma(\Lambda^p T^*M \otimes F)$ is the space of [[Def - Bundle-Valued Differential Forms|$F$-valued $p$-forms]]: smooth sections of the bundle whose fibre at $m$ is $\Lambda^p T^*_m M \otimes F_m$. It is again a $C^\infty(M)$-module under pointwise operations, $(f\omega)(m) = f(m)\, \omega(m)$. For $p = 0$, $\Lambda^0 T^*_m M = \mathbb{R}$ and $\Omega^0(M; F) = \Gamma(F)$.
- $\operatorname{Hom}(E, F) \to M$ is the homomorphism bundle, the vector bundle of rank $kl$ whose fibre at $m$ is $\operatorname{Hom}(E_m, F_m)$, the space of linear maps $E_m \to F_m$; it is constructed on [[Def - Operations on Vector Bundles and Pull-Back Bundles]], where its local trivialisations are $\phi \mapsto \tau_F \, \phi \, \tau_E^{-1}$ for local trivialisations $\tau_E$ of $E$ and $\tau_F$ of $F$. When $F = E$ we write $\operatorname{End} E := \operatorname{Hom}(E, E)$. In Part II we also use $\operatorname{Hom}(E_1 \otimes \cdots \otimes E_r, F)$, the homomorphism bundle from the iterated tensor-product bundle to $F$, whose fibre at $m$ is $\operatorname{Hom}(E_{1,m} \otimes \cdots \otimes E_{r,m}, F_m)$; by the universal property of the [[Def - Tensor Product of Vector Spaces|tensor product]] (a linear map out of $V_1 \otimes \cdots \otimes V_r$ is the same thing as an $r$-linear map out of $V_1 \times \cdots \times V_r$), we regard an element of this fibre as an $r$-linear map $E_{1,m} \times \cdots \times E_{r,m} \to F_m$.
- $\Omega^p(M; \operatorname{Hom}(E, F)) = \Gamma(\Lambda^p T^*M \otimes \operatorname{Hom}(E, F))$ is the space of $\operatorname{Hom}(E, F)$-valued $p$-forms; an element is written $a$, with value $a(m) \in \Lambda^p T^*_m M \otimes \operatorname{Hom}(E_m, F_m)$ at $m$.
- $\Theta_m : \Lambda^p T^*_m M \otimes \operatorname{Hom}(E_m, F_m) \longrightarrow \operatorname{Hom}\!\big(E_m, \Lambda^p T^*_m M \otimes F_m\big)$ is the linear map determined by $\Theta_m(\alpha \otimes \phi)(v) := \alpha \otimes \phi(v)$ for $\alpha \in \Lambda^p T^*_m M$, $\phi \in \operatorname{Hom}(E_m, F_m)$, $v \in E_m$. Lemma 1 below proves that $\Theta_m$ is a linear isomorphism. Through $\Theta_m$ we write $a_m := \Theta_m(a(m))$, a linear map $E_m \to \Lambda^p T^*_m M \otimes F_m$, and we use the two descriptions of $a(m)$ interchangeably.
- **The pairing $a \cdot s$.** For $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ and $s \in \Gamma(E)$, $a \cdot s$ is the $F$-valued $p$-form defined pointwise by $(a \cdot s)(m) := a_m(s(m)) = \Theta_m(a(m))(s(m)) \in \Lambda^p T^*_m M \otimes F_m$. On decomposable elements this is the contraction $\alpha \otimes \phi \otimes v \mapsto \alpha \otimes \phi(v)$, which is the pairing $\Omega^p(M; \operatorname{Hom}(E,F)) \times \Omega^0(M; E) \to \Omega^p(M; F)$ of [[Def - Bundle-Valued Differential Forms]] (that page writes it for $\operatorname{End} E$; the definition is verbatim the same with $\operatorname{Hom}(E, F)$ in place of $\operatorname{End} E$). That $a \cdot s$ is a smooth section is Step 0 of the Formal Proof. For an $r$-linear version we write $a_m(v_1, \dots, v_r)$ for the value of the $r$-linear map $a_m$ on $(v_1, \dots, v_r)$ and $(a \cdot (s_1, \dots, s_r))(m) := a_m(s_1(m), \dots, s_r(m))$.
- $A : \Gamma(E) \to \Omega^p(M; F)$ is the operator in the theorem (this is Haydys's notation in Lemma 12). **On this page $A$ never denotes a connection matrix**; connection matrices do not appear here.
- $e = (e_1, \dots, e_k)$ is a [[Def - Local Frame|local frame]] of $E$ over an open set $U \subseteq M$: each $e_j \in \Gamma(U; E)$ and $e_1(m), \dots, e_k(m)$ is a basis of $E_m$ for each $m \in U$. Likewise $h = (h_1, \dots, h_l)$ is a local frame of $F$ over $U$, and in Part II, $e^{(q)} = (e^{(q)}_1, \dots, e^{(q)}_{k_q})$ is a local frame of $E_q$ over $U$. By [[Thm - Local Frames Span Sections]], every $s \in \Gamma(U; E)$ is uniquely $s = \sum_{j=1}^k \sigma_j e_j$ with $\sigma_j \in C^\infty(U)$, and conversely every $k$-tuple of smooth functions defines a smooth section by this formula; the $\sigma_j$ are the components of $s$ in the frame $e$.
- $\phi_{ij} \in \Gamma(U; \operatorname{Hom}(E, F))$, for $1 \le i \le l$ and $1 \le j \le k$, is the section with $\phi_{ij}(m)(e_{j'}(m)) = \delta_{jj'} h_i(m)$ for all $m \in U$ and $1 \le j' \le k$ (the "matrix unit" sections); Lemma 5 proves that these form a local frame of $\operatorname{Hom}(E, F)$ over $U$.
- On a chart $(U; x^1, \dots, x^n)$ we write $\partial_i = \partial/\partial x^i$ for the coordinate vector fields and $dx^i$ for the coordinate $1$-forms; for an increasing multi-index $I = (i_1 < \cdots < i_p)$ we set $dx^I := dx^{i_1} \wedge \cdots \wedge dx^{i_p}$, and for $p = 0$ the unique (empty) multi-index gives $dx^{\varnothing} := 1$. The $dx^I$ with $I$ increasing form a local frame of $\Lambda^p T^*M$ over $U$ ([[Def - Differential k-Form on a Manifold]]; fibrewise this is the basis of elementary alternating tensors of [[Def - Alternating Tensor and Lambda k V Dual]]).
- $\psi \in C^\infty(M)$ denotes a bump function. We use [[Thm - Existence of Smooth Bump Functions]] in the following form: for every closed set $K \subseteq M$ and every open set $U \supseteq K$ there is a smooth $\psi : M \to [0, 1]$ with $\psi \equiv 1$ on $K$ and $\operatorname{supp} \psi \subseteq U$, where $\operatorname{supp} \psi = \overline{\{m : \psi(m) \neq 0\}}$.
- **Extension by zero.** If $U \subseteq M$ is open, $\psi \in C^\infty(M)$ has $\operatorname{supp} \psi \subseteq U$, and $t \in \Gamma(U; E)$, then $\widetilde{\psi t} \in \Gamma(E)$ denotes the section equal to $\psi t$ on $U$ and to $0$ on $M \setminus U$; Lemma 2 proves it is smooth. The same notation is used for functions $\sigma \in C^\infty(U)$.
- $\mathfrak{X}(M) = \Gamma(TM)$ is the space of smooth vector fields, $[v, w]$ the [[Def - The Lie Bracket of Vector Fields|Lie bracket]], defined by $[v, w] g = v(wg) - w(vg)$ for $g \in C^\infty(M)$, and $T(v, w) = \nabla_v w - \nabla_w v - [v, w]$ is the torsion of a connection $\nabla$ on $TM$ ([[Def - Torsion Tensor]]).

> [!warning] Convention: notation for bundle-valued forms, and what the source states
> Haydys writes $\Omega^p(F)$ and $\Omega^p\big(\operatorname{Hom}(E, F)\big)$ for what the series writes $\Omega^p(M; F)$ and $\Omega^p(M; \operatorname{Hom}(E, F))$; the objects are identical. Haydys's Lemma 12 (p. 7) asserts only the existence of $a$ and leaves the proof as an exercise. The statement below adds the uniqueness of $a$, the converse, and the multilinear version, because all three are used in this chapter — uniqueness is what makes "the curvature form" and "the torsion form" well-defined objects rather than merely existing ones, the converse is what makes $\nabla + a$ a connection in [[Thm - The Space of Connections is an Affine Space]], and the multilinear version is what Haydys applies on p. 22 to the torsion. The proof is supplied by these notes; it is the bump-function argument of Lee, *Introduction to Smooth Manifolds*, second edition, Lemma 12.24, adapted from scalar-valued tensor fields to bundle-valued forms.

---

# Statement

> **Theorem (Tensoriality lemma for $C^\infty(M)$-linear maps; Haydys Lemma 12).** Let $M$ be a smooth manifold, let $E \to M$ and $F \to M$ be smooth real vector bundles of ranks $k$ and $l$, and let $p \geq 0$ be an integer.
>
> **Part I (linear maps).** Let $A : \Gamma(E) \to \Omega^p(M; F)$ be an $\mathbb{R}$-linear map which is also $C^\infty(M)$-linear, that is,
> $$A(fs) = f\, A(s) \qquad \text{for all } f \in C^\infty(M) \text{ and all } s \in \Gamma(E).$$
> Then:
>
> (a) *(Existence.)* There exists $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ such that $A(s) = a \cdot s$ for all $s \in \Gamma(E)$.
>
> (b) *(Uniqueness and formula.)* The form $a$ in (a) is unique, and it is given pointwise by
> $$a_m(v) = A(s)(m) \qquad \text{for every } m \in M,\ v \in E_m, \text{ and every } s \in \Gamma(E) \text{ with } s(m) = v;$$
> in particular the right-hand side does not depend on the choice of $s$, and such an $s$ always exists.
>
> (c) *(Converse.)* For every $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ the map $s \mapsto a \cdot s$ is an $\mathbb{R}$-linear, $C^\infty(M)$-linear map $\Gamma(E) \to \Omega^p(M; F)$.
>
> Consequently $a \mapsto (s \mapsto a \cdot s)$ is a bijection from $\Omega^p(M; \operatorname{Hom}(E, F))$ onto the set of $C^\infty(M)$-linear maps $\Gamma(E) \to \Omega^p(M; F)$, and it is an isomorphism of $C^\infty(M)$-modules.
>
> **Part II (multilinear maps).** Let $E_1, \dots, E_r \to M$ be smooth real vector bundles and let $A : \Gamma(E_1) \times \cdots \times \Gamma(E_r) \to \Omega^p(M; F)$ be $C^\infty(M)$-multilinear: for each slot $q \in \{1, \dots, r\}$, each $f \in C^\infty(M)$, and all sections,
> $$A(s_1, \dots, s_q + f s'_q, \dots, s_r) = A(s_1, \dots, s_q, \dots, s_r) + f\, A(s_1, \dots, s'_q, \dots, s_r).$$
> Then there exists a unique smooth section $a$ of $\Lambda^p T^*M \otimes \operatorname{Hom}(E_1 \otimes \cdots \otimes E_r, F)$ — that is, a smooth family of $r$-linear maps $a_m : E_{1,m} \times \cdots \times E_{r,m} \to \Lambda^p T^*_m M \otimes F_m$ — such that
> $$A(s_1, \dots, s_r)(m) = a_m\big(s_1(m), \dots, s_r(m)\big) \qquad \text{for all } s_q \in \Gamma(E_q) \text{ and all } m \in M.$$
> Conversely every such smooth section $a$ defines a $C^\infty(M)$-multilinear map by this formula.

> **Corollary (the torsion is a $TM$-valued $2$-form; Haydys p. 22).** Let $\nabla$ be a connection on the tangent bundle $TM$ and define, for vector fields $v, w \in \mathfrak{X}(M)$,
> $$T(v, w) := \nabla_v w - \nabla_w v - [v, w] \in \mathfrak{X}(M).$$
> Then $T(w, v) = -T(v, w)$ and $T(f_1 v, f_2 w) = f_1 f_2\, T(v, w)$ for all $f_1, f_2 \in C^\infty(M)$. Consequently there is a unique $T \in \Omega^2(M; TM) = \Gamma(\Lambda^2 T^*M \otimes TM)$, the torsion form, with $T(v, w)(m) = T_m(v(m), w(m))$ for all $v, w$ and all $m$.

The two blocks are tied as follows. The corollary is Part II with $r = 2$, $E_1 = E_2 = F = TM$, and $p = 0$, followed by the observation that an antisymmetric bilinear map $T_m M \times T_m M \to T_m M$ is the same thing as an element of $\Lambda^2 T^*_m M \otimes T_m M$. The scalar special case of Part II — $E_q = TM$ for every $q$, $F = \underline{\mathbb{R}} = M \times \mathbb{R}$, $p = 0$ — is the tensor characterisation lemma of Differential Geometry VII, [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions]], which states that a map $\mathfrak{X}(M)^r \to C^\infty(M)$ is induced by a smooth covariant $r$-tensor field if and only if it is $C^\infty(M)$-multilinear; the proof below is the same bump-function argument with the target $\mathbb{R}$ replaced by the fibres $\Lambda^p T^*_m M \otimes F_m$.

**The statement in the smallest case.** Take $E = F = \underline{\mathbb{R}} = M \times \mathbb{R}$, the trivial line bundle, so that $\Gamma(E) = C^\infty(M)$, $\operatorname{Hom}(E, F) = \underline{\mathbb{R}}$, and $\Omega^p(M; \operatorname{Hom}(E, F)) = \Omega^p(M)$. Part I then says: a map $A : C^\infty(M) \to \Omega^p(M)$ with $A(fs) = f A(s)$ is multiplication by the single fixed $p$-form $a := A(1)$, because $A(s) = A(s \cdot 1) = s\, A(1)$ by $C^\infty(M)$-linearity with $f = s$. In this case the whole content of the lemma is the one-line computation just made, and no bump function is needed, because the trivial bundle has the *global* frame $1$. The exterior derivative $d : C^\infty(M) \to \Omega^1(M)$ is not of this kind — $d(fs) = f\, ds + s\, df \neq f\, ds$ — and indeed $d$ is not multiplication by any $1$-form, since $d(1) = 0$ would force the form to be zero. On the other hand, if $\nabla = d + \alpha$ and $\nabla' = d + \beta$ are two connections on $\underline{\mathbb{R}}$ with $\alpha, \beta \in \Omega^1(M)$, then $(\nabla - \nabla')(s) = (\alpha - \beta)\, s$: the derivative terms cancel, the difference is $C^\infty(M)$-linear, and the lemma identifies it with the $1$-form $\alpha - \beta$. The general theorem is this computation carried out on a bundle that has only local frames, and the bump functions are the price of patching the local computations together.

---

# Motivation

The chapter needs, over and over, to recognise that a certain operator on sections is "really" a bundle-valued differential form — an object with a *value at each point* — rather than a differential operator, which looks at a section in a whole neighbourhood of a point. The difference of two connections, the torsion of a connection on $TM$, and the square $d^\nabla \circ d^\nabla$ of the exterior covariant derivative are all defined by formulas involving derivatives, and yet each of them turns out to be pointwise. The present lemma is the single tool that certifies this, and it does so by an algebraic test that is much easier to apply than the pointwise property itself: one checks that the operator commutes with multiplication by smooth functions.

Why is that the right test? A connection satisfies $\nabla(fs) = df \otimes s + f \nabla s$; the term $df \otimes s$ is exactly the trace of the fact that $\nabla$ differentiates. An operator $A$ with $A(fs) = f A(s)$ has no such term: it sees $f$ only through its values, never through its derivatives, and so it cannot be differentiating anything. The lemma turns this heuristic into a theorem: $C^\infty(M)$-linearity forces $A(s)(m)$ to depend on $s(m)$ alone, and a rule that assigns to each $s(m) \in E_m$ a vector $A(s)(m) \in \Lambda^p T^*_m M \otimes F_m$ linearly is precisely a section of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$. The word "tensoriality" is the standard name for this phenomenon: an operator that is linear over the ring of functions is a tensor.

The lemma is the hinge of §2.2 and §2.3. Haydys's Theorem 11 — [[Thm - The Space of Connections is an Affine Space]] — uses Part I(a) to identify $\nabla - \hat\nabla$ with an element of $\Omega^1(M; \operatorname{End} E)$ and Part I(c) to see that $\nabla + a$ is a connection; Haydys's Proposition 15 — [[Thm - Existence of the Curvature Form]] — uses Part I with $p = 2$ to produce the curvature form $F_\nabla \in \Omega^2(M; \operatorname{End} E)$ from the $C^\infty(M)$-linear operator $d^\nabla \circ \nabla$; and §2.5 uses the corollary to know that the torsion is a $TM$-valued $2$-form. Haydys leaves the proof as an exercise. These notes supply it in full, because the argument — locality by bump functions, then pointwise dependence by a local frame, then smoothness of the resulting family of linear maps — is the template for every "is this operator a tensor?" question in the series, including the tensoriality of the curvature of a principal connection in chapter IV.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of the lemma is that an operator is $C^\infty(M)$-linear. No problem hands one such an operator with that label attached; the skill is to recognise the operators that are secretly $C^\infty(M)$-linear because their derivative terms cancel.

The first disguised source is **the difference of two operators that satisfy the same Leibniz rule**. If $\nabla$ and $\hat\nabla$ are connections on $E$, then $(\nabla - \hat\nabla)(fs) = (df \otimes s + f \nabla s) - (df \otimes s + f \hat\nabla s) = f(\nabla - \hat\nabla)(s)$: the inhomogeneous term $df \otimes s$ is the same for both and cancels, so the difference is $C^\infty(M)$-linear and the lemma (with $F = E$, $p = 1$) identifies it with an element of $\Omega^1(M; \operatorname{End} E)$. The bridge from "both satisfy the Leibniz rule" to the hypothesis is the cancellation, and it is not obvious from the definitions that the difference of two differential operators is a tensor. *Example problem:* show that the connections on $E$ form an affine space modelled on $\Omega^1(M; \operatorname{End} E)$ — this is [[Thm - The Space of Connections is an Affine Space]].

The second disguised source is **an antisymmetrised combination of first derivatives in which the bracket absorbs the derivative terms**. The torsion $T(v, w) = \nabla_v w - \nabla_w v - [v, w]$ contains derivatives of $w$ in the first term and of $v$ in the second, so it is not obviously tensorial; but replacing $v$ by $f v$ produces $-(wf) v$ from $\nabla_w(fv)$ and $+(wf) v$ from $-[fv, w]$, and these cancel (the corollary's proof, Lemma 6). The bridge is the identity $[fv, w] = f[v, w] - (wf) v$, which says the Lie bracket differentiates its arguments in exactly the way needed to cancel the Leibniz terms of $\nabla$. *Example problem:* prove that $T$ is a $TM$-valued $2$-form (the corollary), and then that $\nabla$ is torsion-free if and only if $\nabla_v w - \nabla_w v = [v, w]$ for all $v, w$.

The third disguised source is **a second-order operator whose two Leibniz corrections cancel by antisymmetry of the wedge product**. For a connection $\nabla$, the composite $d^\nabla \circ \nabla : \Gamma(E) \to \Omega^2(M; E)$ satisfies $d^\nabla(\nabla(fs)) = d^\nabla(df \otimes s + f \nabla s) = (d\,df) \otimes s - df \wedge \nabla s + df \wedge \nabla s + f\, d^\nabla \nabla s = f\, d^\nabla \nabla s$, because $d \circ d = 0$ and the two $df \wedge \nabla s$ terms carry opposite signs (one from the $(-1)^p$ in the definition of $d^\nabla$ with $p = 0$, one from the Leibniz rule for $d^\nabla$ with a $1$-form). The bridge is a sign cancellation, and the payoff is the existence of the curvature form via the lemma with $p = 2$. *Example problem:* [[Thm - Existence of the Curvature Form]].

A fourth source, in the same family, is **the commutator of a connection with a $C^\infty(M)$-linear operator**: if $a \in \Omega^1(M; \operatorname{End} E)$ then $s \mapsto d^\nabla(a \cdot s) - a \wedge \nabla s$ is $C^\infty(M)$-linear (both terms produce $df \wedge (a \cdot s)$, with the same sign, and they cancel), and the lemma identifies it with $(d^\nabla a) \cdot s$; this is how the induced connection on $\operatorname{End} E$ acts on $1$-forms in [[Thm - Curvature of a Shifted Connection]].

**Targets (Output Amplification)**

The bare conclusion is that a $C^\infty(M)$-linear operator equals $s \mapsto a \cdot s$ for a unique bundle-valued form $a$. Combined with other facts it does more.

Combine the conclusion with **the existence of local connections and a partition of unity**. Once $\nabla - \hat\nabla \in \Omega^1(M; \operatorname{End} E)$ and $\nabla + a$ is a connection for every $a$, the set $\mathcal{A}(E)$ of connections is an affine space over the vector space $\Omega^1(M; \operatorname{End} E)$; adding the existence of one connection (glued from local ones by a partition of unity) makes $\mathcal{A}(E)$ non-empty. The further result is that "the space of connections" has a topology, a notion of convergence, and a tangent space $\Omega^1(M; \operatorname{End} E)$ at every point — the setting in which the gauge group acts in §2.4 and in which the Yang–Mills functional is differentiated in chapter VII.

Combine the conclusion with **uniqueness**. Because the form $a$ is unique, an identity between operators becomes an identity between forms: if $d^\nabla \circ \nabla = F_\nabla \cdot (\,\cdot\,)$ and also $d^\nabla \circ \nabla = F' \cdot (\,\cdot\,)$, then $F_\nabla = F'$. This is what allows the curvature to be *computed* in a local frame — the local formula $F = dA + A \wedge A$ of [[Thm - Local Formula for the Curvature of a Connection]] is proved by checking that the operator $d^\nabla \circ \nabla$ acts on the frame sections through $dA + A \wedge A$, and uniqueness then identifies this with $F_\nabla$ on $U$.

Combine the conclusion with **the fibrewise linear algebra of alternating maps**. Part II produces a section of $\operatorname{Hom}(E_1 \otimes \cdots \otimes E_r, F)$; if the operator was antisymmetric in two slots then the section is fibrewise antisymmetric in those slots, and the identification $\operatorname{Alt}^2(V; W) \cong \Lambda^2 V^* \otimes W$ (Lemma 7) upgrades it to a $2$-form. This is how the torsion becomes an element of $\Omega^2(M; TM)$ and, with the same argument, how the curvature operator $(X, Y, s) \mapsto \nabla_X \nabla_Y s - \nabla_Y \nabla_X s - \nabla_{[X, Y]} s$ becomes an element of $\Omega^2(M; \operatorname{End} E)$ ([[Def - Curvature of a Vector-Bundle Connection]]).

Combine the conclusion with **restriction to open sets**. Lemma 3 (locality) shows that a $C^\infty(M)$-linear operator $A$ restricts to an operator $A|_U : \Gamma(U; E) \to \Omega^p(U; F)$ on every open set, and the form $a|_U$ represents the restriction. This is what allows local computations in a frame to be meaningful: $a$ is computed on each chart domain and the results agree on overlaps because they compute the same pointwise map.

---

# Why Is It True

The intuition is that a differential operator is exactly an operator that fails to commute with multiplication by functions, and the failure is measured by how it treats the derivatives of the multiplier. The exterior derivative satisfies $d(fs) = f\, ds + df \wedge s$, and the term $df \wedge s$ records that $d$ looked at $f$ in a neighbourhood. An operator with $A(fs) = f A(s)$ treats $f$ as a *number at each point*: it cannot tell the function $f$ from the function $g$ if they agree near $m$ — but more is true, and this is the heart of the matter. The smooth functions include the bump functions, and a bump function can be $1$ at a chosen point $m$ while vanishing outside any prescribed neighbourhood of $m$. Multiplying by such a $\psi$ and using $A(\psi s) = \psi A(s)$, we can compare $A(s)(m)$ with $A$ of a section that has been modified far from $m$, and conclude that the modification is invisible at $m$. So $A(s)(m)$ depends only on the germ of $s$ at $m$. But then a second application of the same trick, with $s$ written near $m$ as $\sum_j \sigma_j e_j$ in a local frame, shows that $A(s)(m) = \sum_j \sigma_j(m) A(\tilde e_j)(m)$: the operator sees only the *numbers* $\sigma_j(m)$, that is, the value $s(m)$. **The mechanism in one sentence: $C^\infty(M)$-linearity lets bump functions pass through $A$, and bump functions isolate points, so $A$ cannot transport information between points and is therefore a pointwise linear map — which is what a section of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$ is.**

Two further points make the conclusion inevitable rather than merely plausible. First, the pointwise maps $a_m$ are automatically linear, because $A$ is $\mathbb{R}$-linear and the sections with prescribed values at $m$ form a vector space; nothing needs to be constructed. Second, the family $m \mapsto a_m$ is automatically smooth, because on the sections $\tilde e_j$ of a (cut-off) local frame $a$ agrees with the smooth forms $A(\tilde e_j)$, and a section whose components in a local frame are smooth is smooth. The only place where anything must be *arranged* is the passage from local frames, which exist only over open sets, to global sections, on which $A$ is defined; bump functions are the arrangement.

The converse — that $s \mapsto a \cdot s$ is $C^\infty(M)$-linear — is the trivial half: a pointwise linear map composed with pointwise multiplication by $f(m)$ commutes with $f$ because $a_m$ is linear. The lemma says that this trivial mechanism is the *only* one: every $C^\infty(M)$-linear operator is pointwise.

---

# What Makes This Hard

The one non-obvious step is that $A$ is defined only on *global* sections, while the pointwise map $a_m$ must be defined on a single fibre $E_m$. To evaluate $a_m$ on $v \in E_m$ one must extend $v$ to a global section, apply $A$, and prove that the answer does not depend on the extension; this independence is precisely the pointwise-dependence lemma (Lemma 4), which itself needs the locality lemma (Lemma 3) and a local frame cut off by a bump function so that the frame sections become global. The common error is to "define $a_m(v) := A(v)$" as though $A$ could be applied to a vector, or to define $a$ on a chart by $a(e_j) := A(e_j)$ as though $A$ could be applied to a local section; neither is meaningful until Lemma 3 has shown that $A$ restricts to open sets. A second, smaller trap is smoothness: one must show that $m \mapsto a_m$ is a smooth section of a specific vector bundle, which requires a frame of that bundle and the fact that smooth components in a frame give a smooth section, not merely that each $a_m$ is linear.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show in three steps that $A(s)(m)$ depends only on $s(m)$: first that it depends only on $s$ near $m$ (locality, via a bump function equal to $1$ at $m$ and supported where $s$ vanishes), then that it depends only on $s(m)$ (write $s$ in a local frame cut off by a bump function, and use $C^\infty(M)$-linearity to pull the component functions out of $A$ and evaluate them at $m$). Define $a_m(v) := A(s)(m)$ for any global $s$ with $s(m) = v$, check that this is a well-defined linear map, and check smoothness by comparing $a$ with $A$ on cut-off frame sections. The converse and the multilinear version are the same argument slot by slot.

**Subgoal decomposition:**

1. **Fibrewise linear algebra.** Show $\Theta_m : \Lambda^p T^*_m M \otimes \operatorname{Hom}(E_m, F_m) \to \operatorname{Hom}(E_m, \Lambda^p T^*_m M \otimes F_m)$ is an isomorphism, so that a pointwise linear map $E_m \to \Lambda^p T^*_m M \otimes F_m$ *is* an element of the fibre of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$.
   - *Hint:* $\Theta_m$ sends the basis $\alpha_I \otimes \phi_{ij}$ to the basis "$e_{j'} \mapsto \delta_{jj'} \alpha_I \otimes h_i$".
   - *Why needed:* Without it, the conclusion "there is a form $a$ with $a \cdot s = A(s)$" is not even a statement about the object that Steps 2–4 construct.

2. **Cut-off sections exist.** Given $m \in U$ and a local frame $e$ on $U$, produce a bump function $\psi$ with $\psi \equiv 1$ on an open $V \ni m$ and $\operatorname{supp} \psi \subseteq U$, and show that $\psi e_j$ extended by zero is a smooth global section agreeing with $e_j$ on $V$; deduce that every $v \in E_m$ is the value at $m$ of some global section.
   - *Hint:* A closed coordinate ball around $m$ inside $U$ is a compact, hence closed, neighbourhood; apply the bump-function theorem to it. Smoothness of the extension by zero is local: check it on $U$ and on $M \setminus \operatorname{supp} \psi$, two open sets covering $M$.
   - *Why needed:* $A$ accepts only global sections; the cut-off frame sections are the global sections on which the local computation is carried out.

3. **Locality.** If $s$ vanishes on an open set $U$, then $A(s)$ vanishes on $U$.
   - *Hint:* For $m \in U$ take $\psi$ with $\psi(m) = 1$ and $\operatorname{supp} \psi \subseteq U$; then $\psi s \equiv 0$, so $0 = A(\psi s) = \psi A(s)$; evaluate at $m$.
   - *Why needed:* It shows $A$ restricts to open sets and is the first half of pointwise dependence.

4. **Pointwise dependence.** If $s(m) = 0$ then $A(s)(m) = 0$.
   - *Hint:* Near $m$, $s = \sum_j \sigma_j e_j$ with $\sigma_j(m) = 0$. With $\psi(m) = 1$, the global section $\sum_j \widetilde{\psi \sigma_j}\, \widetilde{\psi e_j}$ equals $\psi^2 s$ everywhere; apply $A$, pull the functions out, evaluate at $m$.
   - *Why needed:* It is exactly the well-definedness of $a_m(v) := A(s)(m)$.

5. **Define $a$ and verify $A(s) = a \cdot s$, linearity, uniqueness.** Set $a_m(v) := A(s)(m)$ for any $s$ with $s(m) = v$.
   - *Hint:* Well-defined by subgoal 4 applied to the difference of two extensions; linear because $A$ is $\mathbb{R}$-linear and sums of extensions extend sums; $A(s) = a \cdot s$ by taking $s$ itself as the extension of $s(m)$; unique because any $a'$ with $a' \cdot s = A(s)$ satisfies $a'_m(v) = A(s)(m)$ for the same $s$.
   - *Why needed:* This is the conclusion, apart from smoothness.

6. **Smoothness of $a$.** Show $m \mapsto a_m$ is a smooth section.
   - *Hint:* On the open set $V$ where the cut-off frame sections agree with the frame, $a_m(e_j(m)) = A(\tilde e_j)(m)$; the right-hand side is a smooth $F$-valued $p$-form on $V$, so its components in the frame $dx^I \otimes h_i$ are smooth, and these components are the components of $a$ in the frame $dx^I \otimes \phi_{ij}$.
   - *Why needed:* The conclusion asserts a *smooth* section.

7. **Converse and multilinear version.** For the converse, compute $(a \cdot (fs))(m) = a_m(f(m) s(m)) = f(m)\, a_m(s(m))$. For Part II, run subgoals 3–6 in each slot with the other slots frozen, and prove well-definedness by a telescoping sum over the slots.
   - *Hint:* $A(s_1, \dots, s_r)(m) - A(s'_1, \dots, s'_r)(m) = \sum_{q} A(s'_1, \dots, s'_{q-1}, s_q - s'_q, s_{q+1}, \dots, s_r)(m)$ and each term vanishes by the one-slot pointwise lemma.
   - *Why needed:* Part II is what the torsion and the curvature use.

8. **The corollary.** Prove $[fv, w] = f[v, w] - (wf) v$ from the definition of the bracket; deduce $T(f_1 v, f_2 w) = f_1 f_2 T(v, w)$; apply Part II; identify antisymmetric bilinear maps with $\Lambda^2 T^*_m M \otimes T_m M$.
   - *Hint:* Apply both sides of the bracket identity to a test function $g$ and expand with the Leibniz rule for vector fields.
   - *Why needed:* This is Haydys's application on p. 22.

---

# Lemma Decomposition

> [!note]- Lemma 1: The fibrewise identification $\Theta$ is an isomorphism, and the pairing is evaluation
> **Statement:** Let $\Lambda$, $V$, $W$ be finite-dimensional real vector spaces of dimensions $N$, $k$, $l$. The linear map $\Theta : \Lambda \otimes \operatorname{Hom}(V, W) \to \operatorname{Hom}(V, \Lambda \otimes W)$ determined by $\Theta(\alpha \otimes \phi)(v) = \alpha \otimes \phi(v)$ is well defined and is a linear isomorphism. Explicitly, if $(\alpha_I)_{I=1}^N$ is a basis of $\Lambda$, $(v_j)_{j=1}^k$ a basis of $V$, $(w_i)_{i=1}^l$ a basis of $W$, and $\phi_{ij} \in \operatorname{Hom}(V, W)$ is defined by $\phi_{ij}(v_{j'}) = \delta_{jj'} w_i$, then $\Theta$ maps the basis $\{\alpha_I \otimes \phi_{ij}\}$ of $\Lambda \otimes \operatorname{Hom}(V, W)$ bijectively onto the basis $\{\chi_{Iij}\}$ of $\operatorname{Hom}(V, \Lambda \otimes W)$, where $\chi_{Iij}(v_{j'}) := \delta_{jj'}\, \alpha_I \otimes w_i$. Consequently, for $a = \sum_{I, i, j} a^I_{ij}\, \alpha_I \otimes \phi_{ij}$ and $v = \sum_j \sigma_j v_j$,
> $$\Theta(a)(v) = \sum_{I, i, j} a^I_{ij}\, \sigma_j\; \alpha_I \otimes w_i .$$
>
> **Hint:** Well-definedness is the universal property of the tensor product applied to the bilinear map $(\alpha, \phi) \mapsto (v \mapsto \alpha \otimes \phi(v))$. For the isomorphism, compare the images of the basis $\alpha_I \otimes \phi_{ij}$ with the basis $\chi_{Iij}$.
>
> **Why needed:** The theorem's conclusion is a section of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$, while the proof constructs, at each point, a linear map $E_m \to \Lambda^p T^*_m M \otimes F_m$. Lemma 1 says these are the same thing, fibre by fibre, and it gives the component formula used in the smoothness step and in the converse.
>
> > [!note]- Full proof
> > We are given finite-dimensional spaces $\Lambda, V, W$ and must show that $\Theta$ is well defined, that it is an isomorphism, and that the displayed component formula holds.
> >
> > **Well-definedness of $\Theta$.** The map $B : \Lambda \times \operatorname{Hom}(V, W) \to \operatorname{Hom}(V, \Lambda \otimes W)$, $B(\alpha, \phi) := (v \mapsto \alpha \otimes \phi(v))$, takes values in linear maps (since $v \mapsto \phi(v)$ is linear and $\alpha \otimes (\,\cdot\,)$ is linear) and is bilinear in $(\alpha, \phi)$ (since $\alpha \otimes \phi(v)$ is bilinear in $(\alpha, \phi(v))$ and $\phi(v)$ is linear in $\phi$). By the universal property of the [[Def - Tensor Product of Vector Spaces|tensor product]] — every bilinear map $\Lambda \times \operatorname{Hom}(V, W) \to X$ factors uniquely through a linear map $\Lambda \otimes \operatorname{Hom}(V, W) \to X$ — there is a unique linear $\Theta$ with $\Theta(\alpha \otimes \phi) = B(\alpha, \phi)$. This is the $\Theta$ of the statement.
> >
> > **The $\phi_{ij}$ form a basis of $\operatorname{Hom}(V, W)$.** A linear map $\phi : V \to W$ is determined by the vectors $\phi(v_{j'})$, $1 \le j' \le k$, each of which expands uniquely as $\phi(v_{j'}) = \sum_i c_{ij'} w_i$ (since $(w_i)$ is a basis of $W$); then $\phi = \sum_{i, j} c_{ij} \phi_{ij}$, because both sides take the value $\sum_i c_{ij'} w_i$ on $v_{j'}$ (by the definition $\phi_{ij}(v_{j'}) = \delta_{jj'} w_i$) and a linear map is determined by its values on a basis. The expansion is unique because $\sum_{i,j} c_{ij} \phi_{ij} = 0$ evaluated on $v_{j'}$ gives $\sum_i c_{ij'} w_i = 0$, hence $c_{ij'} = 0$ for all $i$ (linear independence of the $w_i$). Therefore $\{\phi_{ij}\}$ is a basis of $\operatorname{Hom}(V, W)$, which has dimension $kl$.
> >
> > **The $\alpha_I \otimes \phi_{ij}$ form a basis of $\Lambda \otimes \operatorname{Hom}(V, W)$.** The tensor product of a basis of $\Lambda$ with a basis of $\operatorname{Hom}(V, W)$ is a basis of $\Lambda \otimes \operatorname{Hom}(V, W)$ (the basis property of tensor products, [[Def - Tensor Product of Vector Spaces]]). So $\{\alpha_I \otimes \phi_{ij}\}$ is a basis, of cardinality $N k l$.
> >
> > **The $\chi_{Iij}$ form a basis of $\operatorname{Hom}(V, \Lambda \otimes W)$.** By the same basis property, $\{\alpha_I \otimes w_i\}$ is a basis of $\Lambda \otimes W$. A linear map $L : V \to \Lambda \otimes W$ is determined by the vectors $L(v_{j'})$, each of which expands uniquely as $L(v_{j'}) = \sum_{I, i} c^I_{ij'}\, \alpha_I \otimes w_i$. Then $L = \sum_{I, i, j} c^I_{ij} \chi_{Iij}$, since both sides take the value $\sum_{I, i} c^I_{ij'} \alpha_I \otimes w_i$ on $v_{j'}$ (by the definition of $\chi_{Iij}$), and the expansion is unique by the same evaluation argument as for the $\phi_{ij}$. Hence $\{\chi_{Iij}\}$ is a basis of $\operatorname{Hom}(V, \Lambda \otimes W)$.
> >
> > **$\Theta$ maps basis to basis.** For each $j'$,
> > $$\Theta(\alpha_I \otimes \phi_{ij})(v_{j'}) = \alpha_I \otimes \phi_{ij}(v_{j'}) = \alpha_I \otimes \delta_{jj'} w_i = \delta_{jj'}\, \alpha_I \otimes w_i = \chi_{Iij}(v_{j'}) \qquad \text{(definition of } \Theta \text{, then of } \phi_{ij} \text{, then of } \chi_{Iij}\text{)},$$
> > so $\Theta(\alpha_I \otimes \phi_{ij}) = \chi_{Iij}$ (two linear maps agreeing on a basis are equal). A linear map that sends a basis bijectively onto a basis is an isomorphism (it is surjective because its image contains a spanning set, and injective because the images of the basis vectors are linearly independent). Therefore $\Theta$ is a linear isomorphism.
> >
> > **The component formula.** For $a = \sum_{I, i, j} a^I_{ij}\, \alpha_I \otimes \phi_{ij}$ and $v = \sum_{j'} \sigma_{j'} v_{j'}$,
> > $$\Theta(a)(v) = \sum_{I, i, j} a^I_{ij}\, \chi_{Iij}\Big(\sum_{j'} \sigma_{j'} v_{j'}\Big) = \sum_{I, i, j} \sum_{j'} a^I_{ij}\, \sigma_{j'}\, \delta_{jj'}\, \alpha_I \otimes w_i = \sum_{I, i, j} a^I_{ij}\, \sigma_j\, \alpha_I \otimes w_i \qquad \text{(linearity of } \Theta \text{ and of } \chi_{Iij} \text{; definition of } \chi_{Iij} \text{; the Kronecker delta collapses the } j' \text{ sum).}$$
> >
> > Therefore $\Theta$ is a well-defined linear isomorphism with the stated component formula. $\blacksquare$

> [!note]- Lemma 2: Cut-off frame sections, and extension of a vector to a global section
> **Statement:** Let $m \in M$, let $U \subseteq M$ be an open neighbourhood of $m$, and let $e = (e_1, \dots, e_k)$ be a local frame of $E$ over $U$. Then:
>
> (i) there is an open neighbourhood $V$ of $m$ and a smooth $\psi : M \to [0, 1]$ with $\psi \equiv 1$ on $V$ and $\operatorname{supp} \psi \subseteq U$;
>
> (ii) for every $t \in \Gamma(U; E)$ the map $\widetilde{\psi t} : M \to E$, equal to $\psi t$ on $U$ and to the zero vector of $E_{m'}$ at every $m' \in M \setminus U$, is a smooth global section of $E$, and $\widetilde{\psi t} = t$ on $V$; likewise for every $\sigma \in C^\infty(U)$ the function $\widetilde{\psi \sigma}$, equal to $\psi \sigma$ on $U$ and to $0$ off $U$, is in $C^\infty(M)$ and equals $\sigma$ on $V$;
>
> (iii) in particular $\tilde e_j := \widetilde{\psi e_j} \in \Gamma(E)$ satisfies $\tilde e_j = e_j$ on $V$, and for every $v \in E_m$ there is $s \in \Gamma(E)$ with $s(m) = v$.
>
> Moreover, every point of $M$ has an open neighbourhood over which $E$ admits a local frame.
>
> **Hint:** For (i), a closed coordinate ball around $m$ inside $U$ is compact, hence closed in the Hausdorff space $M$; apply [[Thm - Existence of Smooth Bump Functions]] to it. For (ii), smoothness is a local property; the open sets $U$ and $M \setminus \operatorname{supp} \psi$ cover $M$. For (iii), expand $v$ in the basis $e_j(m)$ and take the corresponding combination of the $\tilde e_j$.
>
> **Why needed:** $A$ is defined only on global sections. Every local computation in the proof is carried out on the global sections $\tilde e_j$ and $\widetilde{\psi \sigma_j}$, which agree with the frame and the components on $V$.
>
> > [!note]- Full proof
> > We are given $m \in U$ and a local frame $e$ over $U$; we must produce $V$ and $\psi$, prove the smoothness of the extensions by zero, and construct a global section through any prescribed vector.
> >
> > **Local frames exist.** Let $m' \in M$. By the definition of a [[Def - Vector Bundle|vector bundle]], there is an open $U' \ni m'$ and a [[Def - Local Trivialization|local trivialisation]] $\psi_{U'} : E|_{U'} \to U' \times \mathbb{R}^k$, a diffeomorphism which is a linear isomorphism $E_{m''} \to \{m''\} \times \mathbb{R}^k$ on each fibre. Define $e_j(m'') := \psi_{U'}^{-1}(m'', \epsilon_j)$ for $m'' \in U'$, where $\epsilon_j$ is the $j$-th standard basis vector of $\mathbb{R}^k$. Then $e_j : U' \to E$ is smooth (the composite of the smooth map $m'' \mapsto (m'', \epsilon_j)$ with the diffeomorphism $\psi_{U'}^{-1}$), it is a section (since $\psi_{U'}^{-1}$ maps $\{m''\} \times \mathbb{R}^k$ into $E_{m''}$), and $e_1(m''), \dots, e_k(m'')$ is a basis of $E_{m''}$ (the image of the basis $\epsilon_1, \dots, \epsilon_k$ under the linear isomorphism $\psi_{U'}^{-1}|_{\{m''\} \times \mathbb{R}^k}$). So $e$ is a local frame over $U'$. (This is one direction of [[Ex - Local Frames Correspond to Local Trivialisations]].)
> >
> > **(i) A closed neighbourhood inside $U$, and the bump function.** Since $M$ is a smooth manifold, there is a chart $(U_0, \varphi)$ with $m \in U_0$; replacing $U_0$ by $U_0 \cap U$ (still open, still containing $m$, and $\varphi|_{U_0 \cap U}$ is still a chart) we may assume $U_0 \subseteq U$. The set $\varphi(U_0) \subseteq \mathbb{R}^n$ is open and contains $\varphi(m)$, so there is $\rho > 0$ with the closed ball $\overline{B}_\rho(\varphi(m)) = \{x \in \mathbb{R}^n : |x - \varphi(m)| \le \rho\}$ contained in $\varphi(U_0)$. Set
> > $$K := \varphi^{-1}\big(\overline{B}_\rho(\varphi(m))\big), \qquad V := \varphi^{-1}\big(B_\rho(\varphi(m))\big) = \varphi^{-1}\big(\{x : |x - \varphi(m)| < \rho\}\big).$$
> > Then $V$ is open in $U_0$, hence in $M$ (as $\varphi$ is a homeomorphism onto an open subset of $\mathbb{R}^n$ and $U_0$ is open in $M$), and $m \in V$. The set $K$ is compact, being the image of the compact set $\overline{B}_\rho(\varphi(m))$ under the continuous map $\varphi^{-1}$; since $M$ is Hausdorff (standing convention), compact subsets are closed, so $K$ is closed in $M$. Also $V \subseteq K \subseteq U_0 \subseteq U$. By [[Thm - Existence of Smooth Bump Functions]] — for every closed $K \subseteq M$ and open $U \supseteq K$ there is a smooth $\psi : M \to [0, 1]$ with $\psi \equiv 1$ on $K$ and $\operatorname{supp} \psi \subseteq U$ — we obtain $\psi$ with $\psi \equiv 1$ on $K \supseteq V$ and $\operatorname{supp} \psi \subseteq U$. This proves (i).
> >
> > **(ii) Extension by zero is smooth.** Let $t \in \Gamma(U; E)$ and define $\widetilde{\psi t}$ as in the statement. It is a section, since at $m' \in U$ its value $\psi(m') t(m')$ lies in $E_{m'}$ and at $m' \notin U$ its value is $0 \in E_{m'}$. For smoothness, consider the two open sets $U$ and $W := M \setminus \operatorname{supp} \psi$ (open because $\operatorname{supp} \psi$ is closed). They cover $M$: if $m' \notin U$ then $m' \notin \operatorname{supp} \psi$ (as $\operatorname{supp} \psi \subseteq U$), so $m' \in W$. On $U$, $\widetilde{\psi t} = \psi t$ is smooth, being the product of the smooth function $\psi|_U$ with the smooth section $t$ (the $C^\infty(U)$-module structure on $\Gamma(U; E)$ from [[Def - Section of a Vector Bundle]]). On $W$, $\widetilde{\psi t}$ is the zero section: at $m' \in W \cap U$ we have $\psi(m') = 0$ (since $m' \notin \operatorname{supp} \psi \supseteq \{\psi \neq 0\}$), so $\psi(m') t(m') = 0$; at $m' \in W \setminus U$ the value is $0$ by definition. The zero section is smooth. A map $M \to E$ which is smooth on each set of an open cover is smooth (smoothness is a local property, [[Def - Smooth Map between Manifolds]]). Hence $\widetilde{\psi t} \in \Gamma(E)$. On $V$ we have $\psi \equiv 1$, so $\widetilde{\psi t} = t$ there. The argument for $\widetilde{\psi \sigma}$, $\sigma \in C^\infty(U)$, is identical with $E$ replaced by the trivial bundle $M \times \mathbb{R}$: on $U$ it is the smooth function $\psi \sigma$, on $W$ it is $0$, the two open sets cover $M$, and on $V$ it equals $\sigma$.
> >
> > **(iii) Cut-off frame sections and extension of vectors.** Applying (ii) to $t = e_j$ gives $\tilde e_j \in \Gamma(E)$ with $\tilde e_j = e_j$ on $V$. Now let $v \in E_m$. Since $e_1(m), \dots, e_k(m)$ is a basis of $E_m$, there are unique real numbers $v_1, \dots, v_k$ with $v = \sum_{j=1}^k v_j e_j(m)$. Define $s := \sum_{j=1}^k v_j \tilde e_j \in \Gamma(E)$ (a real linear combination of smooth sections is smooth). Then
> > $$s(m) = \sum_{j=1}^k v_j \tilde e_j(m) = \sum_{j=1}^k v_j e_j(m) = v \qquad \text{(pointwise definition of the operations; } \tilde e_j = e_j \text{ on } V \ni m \text{; choice of the } v_j\text{)}.$$
> >
> > Therefore the cut-off sections are smooth global sections agreeing with the frame near $m$, and every vector in $E_m$ is the value of a global section. $\blacksquare$

> [!note]- Lemma 3: Locality — a $C^\infty(M)$-linear operator does not see a section outside where it lives
> **Statement:** Let $A : \Gamma(E) \to \Omega^p(M; F)$ be $\mathbb{R}$-linear and $C^\infty(M)$-linear. If $s \in \Gamma(E)$ vanishes on an open set $U \subseteq M$, then $A(s)$ vanishes on $U$. More generally, if $A : \Gamma(E_1) \times \cdots \times \Gamma(E_r) \to \Omega^p(M; F)$ is $C^\infty(M)$-multilinear and $s_q$ vanishes on $U$ for some slot $q$, then $A(s_1, \dots, s_r)$ vanishes on $U$.
>
> **Hint:** Fix $m \in U$, take a bump function $\psi$ with $\psi(m) = 1$ and $\operatorname{supp} \psi \subseteq U$, and observe that $\psi s$ is the zero section.
>
> **Why needed:** It is the first half of pointwise dependence, and it shows that $A$ restricts to open sets (used in the smoothness step, where $A(\tilde e_j)$ is compared with $a$ on $V$).
>
> > [!note]- Full proof
> > Assume $A$ is $\mathbb{R}$-linear and $C^\infty(M)$-linear and that $s|_U = 0$. We must show $A(s)(m) = 0$ for every $m \in U$.
> >
> > **Choose a bump function at $m$.** Fix $m \in U$. The singleton $\{m\}$ is closed in $M$ because $M$ is Hausdorff (standing convention), and $U \supseteq \{m\}$ is open, so [[Thm - Existence of Smooth Bump Functions]] — for a closed set $K$ inside an open set $U$ there is a smooth $\psi : M \to [0, 1]$ with $\psi \equiv 1$ on $K$ and $\operatorname{supp} \psi \subseteq U$ — gives $\psi \in C^\infty(M)$ with $\psi(m) = 1$ and $\operatorname{supp} \psi \subseteq U$.
> >
> > **$\psi s$ is the zero section.** At a point $m' \in U$, $(\psi s)(m') = \psi(m') s(m') = \psi(m') \cdot 0 = 0$ (since $s$ vanishes on $U$). At a point $m' \notin U$, $m' \notin \operatorname{supp} \psi$, so $\psi(m') = 0$ and $(\psi s)(m') = 0 \cdot s(m') = 0$. Hence $\psi s = 0$ in $\Gamma(E)$.
> >
> > **Apply $A$ and evaluate at $m$.**
> > $$0 = A(0) = A(\psi s) = \psi\, A(s) \qquad \text{(} A(0) = 0 \text{ by } \mathbb{R}\text{-linearity; } \psi s = 0 \text{; } C^\infty(M)\text{-linearity of } A\text{)},$$
> > and evaluating this identity of $F$-valued $p$-forms at $m$,
> > $$0 = (\psi\, A(s))(m) = \psi(m)\, A(s)(m) = A(s)(m) \qquad \text{(pointwise module structure on } \Omega^p(M; F) \text{; } \psi(m) = 1\text{)}.$$
> > Since $m \in U$ was arbitrary, $A(s)$ vanishes on $U$.
> >
> > **The multilinear case.** Let $A$ be $C^\infty(M)$-multilinear and let $s_q$ vanish on $U$. Fix $m \in U$ and $\psi$ as above. Then $\psi s_q = 0$ by the same pointwise computation, so
> > $$0 = A(s_1, \dots, \psi s_q, \dots, s_r) = \psi\, A(s_1, \dots, s_q, \dots, s_r) \qquad \text{(} A \text{ of a tuple with a zero entry is } 0 \text{ by linearity in slot } q \text{; } C^\infty(M)\text{-linearity in slot } q\text{)},$$
> > and evaluating at $m$ with $\psi(m) = 1$ gives $A(s_1, \dots, s_r)(m) = 0$.
> >
> > Therefore a $C^\infty(M)$-linear (or multilinear) operator applied to a section vanishing on an open set vanishes on that open set. $\blacksquare$

> [!note]- Lemma 4: Pointwise dependence — if $s(m) = 0$ then $A(s)(m) = 0$
> **Statement:** Let $A : \Gamma(E) \to \Omega^p(M; F)$ be $\mathbb{R}$-linear and $C^\infty(M)$-linear. If $s \in \Gamma(E)$ and $s(m) = 0$ for some $m \in M$, then $A(s)(m) = 0$. More generally, if $A : \Gamma(E_1) \times \cdots \times \Gamma(E_r) \to \Omega^p(M; F)$ is $C^\infty(M)$-multilinear and $s_q(m) = 0$ for some slot $q$, then $A(s_1, \dots, s_r)(m) = 0$.
>
> **Hint:** Take a local frame $e$ on $U \ni m$, write $s = \sum_j \sigma_j e_j$ on $U$ with $\sigma_j(m) = 0$, and build the global section $\sum_j \widetilde{\psi \sigma_j}\, \tilde e_j$, which equals $\psi^2 s$ on all of $M$; then pull the functions $\widetilde{\psi \sigma_j}$ out of $A$ and evaluate at $m$.
>
> **Why needed:** This is exactly the statement that $a_m(v) := A(s)(m)$ does not depend on the choice of $s$ with $s(m) = v$.
>
> > [!note]- Full proof
> > Assume $A$ is $\mathbb{R}$-linear and $C^\infty(M)$-linear, and $s(m) = 0$. We must show $A(s)(m) = 0$.
> >
> > **Set up a cut-off frame at $m$.** By Lemma 2 there is an open $U \ni m$ carrying a local frame $e = (e_1, \dots, e_k)$ of $E$; by Lemma 2(i) there are an open $V$ with $m \in V \subseteq U$ and $\psi \in C^\infty(M)$ with $\psi \equiv 1$ on $V$ and $\operatorname{supp} \psi \subseteq U$; by Lemma 2(ii)–(iii) the sections $\tilde e_j = \widetilde{\psi e_j}$ are in $\Gamma(E)$. By [[Thm - Local Frames Span Sections]] — every section over $U$ is uniquely a $C^\infty(U)$-combination of the frame — write $s|_U = \sum_{j=1}^k \sigma_j e_j$ with $\sigma_j \in C^\infty(U)$. Evaluating at $m$: $0 = s(m) = \sum_j \sigma_j(m) e_j(m)$, and since $e_1(m), \dots, e_k(m)$ is a basis of $E_m$, all $\sigma_j(m) = 0$. By Lemma 2(ii) the functions $\tilde \sigma_j := \widetilde{\psi \sigma_j}$ are in $C^\infty(M)$.
> >
> > **The global section $\sum_j \tilde\sigma_j \tilde e_j$ equals $\psi^2 s$.** Both sides are elements of $\Gamma(E)$ ($\psi^2 s$ is a smooth function times a smooth section). At $m' \in U$,
> > $$\Big(\sum_j \tilde\sigma_j \tilde e_j\Big)(m') = \sum_j \psi(m') \sigma_j(m')\, \psi(m') e_j(m') = \psi(m')^2 \sum_j \sigma_j(m') e_j(m') = \psi(m')^2 s(m') \qquad \text{(definitions of } \tilde\sigma_j, \tilde e_j \text{ on } U \text{; the expansion of } s|_U\text{)}.$$
> > At $m' \notin U$, the left side is $\sum_j 0 \cdot 0 = 0$ (both extensions are zero off $U$) and the right side is $\psi(m')^2 s(m') = 0$ because $\psi(m') = 0$ off $\operatorname{supp} \psi \subseteq U$. So $\sum_j \tilde\sigma_j \tilde e_j = \psi^2 s$ in $\Gamma(E)$.
> >
> > **Apply $A$ and evaluate at $m$.**
> > $$\psi^2\, A(s) = A(\psi^2 s) = A\Big(\sum_j \tilde\sigma_j \tilde e_j\Big) = \sum_j A(\tilde\sigma_j \tilde e_j) = \sum_j \tilde\sigma_j\, A(\tilde e_j) \qquad \text{(} C^\infty(M)\text{-linearity with } f = \psi^2 \text{; the identity just proved; } \mathbb{R}\text{-linearity; } C^\infty(M)\text{-linearity with } f = \tilde\sigma_j\text{)}.$$
> > Evaluating at $m$ and using the pointwise module structure of $\Omega^p(M; F)$,
> > $$\psi(m)^2 A(s)(m) = \sum_j \tilde\sigma_j(m)\, A(\tilde e_j)(m) = \sum_j \psi(m) \sigma_j(m)\, A(\tilde e_j)(m) = 0 \qquad \text{(} m \in U \text{ so } \tilde\sigma_j(m) = \psi(m)\sigma_j(m) \text{; } \sigma_j(m) = 0\text{)}.$$
> > Since $\psi(m) = 1$ (as $m \in V$), this reads $A(s)(m) = 0$.
> >
> > **The multilinear case.** Let $A$ be $C^\infty(M)$-multilinear and $s_q(m) = 0$. With the cut-off frame $e^{(q)}$ of $E_q$ at $m$, the sections $\tilde e^{(q)}_j$, and the functions $\tilde\sigma_j$ built from $s_q|_U = \sum_j \sigma_j e^{(q)}_j$ exactly as above (so that $\sigma_j(m) = 0$ and $\sum_j \tilde\sigma_j \tilde e^{(q)}_j = \psi^2 s_q$), linearity in slot $q$ gives
> > $$\psi^2 A(s_1, \dots, s_q, \dots, s_r) = A(s_1, \dots, \psi^2 s_q, \dots, s_r) = \sum_j \tilde\sigma_j\, A(s_1, \dots, \tilde e^{(q)}_j, \dots, s_r) \qquad \text{(} C^\infty(M)\text{-linearity in slot } q \text{, twice, and additivity in slot } q\text{)},$$
> > and evaluating at $m$, where $\psi(m) = 1$ and $\tilde\sigma_j(m) = \sigma_j(m) = 0$, gives $A(s_1, \dots, s_r)(m) = 0$.
> >
> > Therefore the value of $A(s)$ at $m$ vanishes whenever $s(m) = 0$, in one slot at a time. $\blacksquare$

> [!note]- Lemma 5: Local frames of the target bundles, and the smoothness criterion
> **Statement:** Let $(U; x^1, \dots, x^n)$ be a chart of $M$ over which $E$ has a local frame $e = (e_j)_{j=1}^k$ and $F$ has a local frame $h = (h_i)_{i=1}^l$. Then:
>
> (i) the sections $dx^I \otimes h_i$, for $I$ increasing of length $p$ and $1 \le i \le l$, form a local frame of $\Lambda^p T^*M \otimes F$ over $U$;
>
> (ii) the sections $\phi_{ij}$ (defined by $\phi_{ij}(m)(e_{j'}(m)) = \delta_{jj'} h_i(m)$) form a local frame of $\operatorname{Hom}(E, F)$ over $U$, and the sections $dx^I \otimes \phi_{ij}$ form a local frame of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$ over $U$;
>
> (iii) a section $\omega$ of either bundle over $U$ (not assumed smooth), written pointwise as $\omega(m) = \sum \omega^{I}_{i}(m)\, dx^I|_m \otimes h_i(m)$, respectively $\omega(m) = \sum \omega^I_{ij}(m)\, dx^I|_m \otimes \phi_{ij}(m)$, is smooth on $U$ if and only if all the coefficient functions $\omega^I_i$, respectively $\omega^I_{ij}$, are smooth on $U$;
>
> (iv) under the pointwise identification $\Theta_m$ of Lemma 1, the section $a = \sum a^I_{ij}\, dx^I \otimes \phi_{ij}$ satisfies $a_m(e_{j'}(m)) = \sum_{I, i} a^I_{ij'}(m)\, dx^I|_m \otimes h_i(m)$; that is, the coefficients of $a$ in the frame (ii) are the coefficients of the forms $a(e_{j'})$ in the frame (i).
>
> The same statements hold, with the same proofs, for $\Lambda^p T^*M \otimes \operatorname{Hom}(E_1 \otimes \cdots \otimes E_r, F)$ with the frame $dx^I \otimes \phi_{i; j_1 \cdots j_r}$, where $\phi_{i; j_1 \cdots j_r}(m)$ is the $r$-linear map sending $(e^{(1)}_{j'_1}(m), \dots, e^{(r)}_{j'_r}(m))$ to $\delta_{j_1 j'_1} \cdots \delta_{j_r j'_r} h_i(m)$.
>
> **Hint:** Fibrewise, tensor products of bases are bases and the matrix units are a basis of $\operatorname{Hom}$ (Lemma 1). Smoothness of the frame sections: in the local trivialisations of the derived bundles constructed on [[Def - Operations on Vector Bundles and Pull-Back Bundles]], each frame section is a constant section. Then (iii) is [[Thm - Local Frames Span Sections]].
>
> **Why needed:** The conclusion of the theorem asserts that $a$ is a *smooth* section of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$; (iii) reduces this to the smoothness of finitely many functions, and (iv) identifies those functions with the components of the smooth forms $A(\tilde e_j)$.
>
> > [!note]- Full proof
> > We must show that the listed sections are smooth, that they are pointwise bases, and that smoothness of a section is equivalent to smoothness of its coefficients.
> >
> > **Pointwise bases.** At $m \in U$: the $dx^I|_m$ ($I$ increasing) form a basis of $\Lambda^p T^*_m M$ (the elementary alternating tensors of [[Def - Alternating Tensor and Lambda k V Dual]] built from the basis $dx^1|_m, \dots, dx^n|_m$ of $T^*_m M$); the $h_i(m)$ form a basis of $F_m$; the $\phi_{ij}(m)$ form a basis of $\operatorname{Hom}(E_m, F_m)$ (Lemma 1, second paragraph, with $v_j = e_j(m)$, $w_i = h_i(m)$); and a tensor product of bases is a basis ([[Def - Tensor Product of Vector Spaces]]). Hence $\{dx^I|_m \otimes h_i(m)\}$ is a basis of $\Lambda^p T^*_m M \otimes F_m$ and $\{dx^I|_m \otimes \phi_{ij}(m)\}$ is a basis of $\Lambda^p T^*_m M \otimes \operatorname{Hom}(E_m, F_m)$. For the multilinear version, $\{\phi_{i; j_1 \cdots j_r}(m)\}$ is a basis of the space of $r$-linear maps $E_{1,m} \times \cdots \times E_{r,m} \to F_m$ by the same argument as in Lemma 1: an $r$-linear map is determined by its values on the tuples of basis vectors $(e^{(1)}_{j'_1}(m), \dots, e^{(r)}_{j'_r}(m))$, each such value expands uniquely in the basis $h_i(m)$, and the coefficients are the coordinates with respect to $\{\phi_{i; j_1 \cdots j_r}(m)\}$.
> >
> > **Smoothness of the frame sections.** The coordinate $1$-forms $dx^i$ are smooth sections of $T^*M$ over $U$, and $dx^I = dx^{i_1} \wedge \cdots \wedge dx^{i_p}$ is a smooth section of $\Lambda^p T^*M$ ([[Def - Differential k-Form on a Manifold]]; in the chart-induced trivialisation of $\Lambda^p T^*M$ it is the constant section $m \mapsto (m, \epsilon_I)$). By [[Ex - Local Frames Correspond to Local Trivialisations]] the frames $e$ and $h$ are induced by local trivialisations $\tau_E : E|_U \to U \times \mathbb{R}^k$ and $\tau_F : F|_U \to U \times \mathbb{R}^l$ with $e_j(m) = \tau_E^{-1}(m, \epsilon_j)$ and $h_i(m) = \tau_F^{-1}(m, \epsilon_i)$; likewise $dx^I$ is induced by a trivialisation $\tau_\Lambda$ of $\Lambda^p T^*M|_U$. On [[Def - Operations on Vector Bundles and Pull-Back Bundles]], the bundle $\operatorname{Hom}(E, F)$ is given the local trivialisation $\phi \mapsto (m, \tau_{F, m} \circ \phi \circ \tau_{E, m}^{-1})$ over $U$, and a tensor product bundle $B_1 \otimes B_2$ the trivialisation $\tau_{B_1} \otimes \tau_{B_2}$; the smooth structures on these bundles are, by the [[Thm - Vector Bundle Construction Lemma|vector bundle construction lemma]], exactly the ones for which these maps are smooth local trivialisations. In the trivialisation of $\operatorname{Hom}(E, F)$, the section $\phi_{ij}$ becomes $m \mapsto (m, \tau_{F, m} \phi_{ij}(m) \tau_{E, m}^{-1})$, and $\tau_{F,m} \phi_{ij}(m) \tau_{E,m}^{-1}(\epsilon_{j'}) = \tau_{F,m} \phi_{ij}(m)(e_{j'}(m)) = \delta_{jj'} \tau_{F,m} h_i(m) = \delta_{jj'} \epsilon_i$: the matrix of $\phi_{ij}$ is the constant matrix unit $E_{ij}$. A section that is constant in a trivialisation is smooth (it is $\tau^{-1}$ composed with the smooth map $m \mapsto (m, \text{constant})$). So $\phi_{ij}$ is smooth. In the trivialisation $\tau_\Lambda \otimes \tau_F$ of $\Lambda^p T^*M \otimes F$, the section $dx^I \otimes h_i$ is the constant section $m \mapsto (m, \epsilon_I \otimes \epsilon_i)$, hence smooth; in the trivialisation $\tau_\Lambda \otimes \tau_{\operatorname{Hom}}$ of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$, the section $dx^I \otimes \phi_{ij}$ is the constant section $m \mapsto (m, \epsilon_I \otimes E_{ij})$, hence smooth. The multilinear frame sections $\phi_{i; j_1 \cdots j_r}$ are, in the trivialisation of $\operatorname{Hom}(E_1 \otimes \cdots \otimes E_r, F)$ built from $\tau_{E_1} \otimes \cdots \otimes \tau_{E_r}$ and $\tau_F$, the constant sections given by the elementary tensors $\epsilon_i \otimes (\epsilon_{j_1} \otimes \cdots \otimes \epsilon_{j_r})^*$, hence smooth. This proves (i) and (ii).
> >
> > **(iii) The smoothness criterion.** Given (i) and (ii), the statement is [[Thm - Local Frames Span Sections]] applied to the bundle $\Lambda^p T^*M \otimes F$, respectively $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$, over $U$: a smooth section has a unique expression as a combination of the frame with smooth coefficients, and conversely any tuple of smooth coefficient functions defines a smooth section. Since the frame is a pointwise basis, the coefficients of a not-necessarily-smooth section are uniquely determined pointwise, and the section is smooth if and only if these coefficients are smooth: "if" is the converse direction of the theorem, and "only if" is its direct direction together with the pointwise uniqueness of the coefficients.
> >
> > **(iv) The coefficient identification.** For $a(m) = \sum_{I, i, j} a^I_{ij}(m)\, dx^I|_m \otimes \phi_{ij}(m)$, the component formula of Lemma 1 (with $\alpha_I = dx^I|_m$, $v_j = e_j(m)$, $w_i = h_i(m)$, and $v = e_{j'}(m)$, i.e. $\sigma_j = \delta_{jj'}$) gives
> > $$a_m(e_{j'}(m)) = \Theta_m(a(m))(e_{j'}(m)) = \sum_{I, i, j} a^I_{ij}(m)\, \delta_{jj'}\, dx^I|_m \otimes h_i(m) = \sum_{I, i} a^I_{ij'}(m)\, dx^I|_m \otimes h_i(m) \qquad \text{(Lemma 1, component formula).}$$
> >
> > Therefore the derived bundles have the stated local frames, smoothness of a section is smoothness of its coefficients, and the coefficients of $a$ are read off from the forms $a(e_{j'})$. $\blacksquare$

> [!note]- Lemma 6: The bracket identity and the $C^\infty(M)$-bilinearity of the torsion
> **Statement:** Let $\nabla$ be a connection on $TM$, and for $v, w \in \mathfrak{X}(M)$ let $T(v, w) = \nabla_v w - \nabla_w v - [v, w]$. Then for all $f, f_1, f_2 \in C^\infty(M)$:
>
> (i) $[fv, w] = f[v, w] - (wf)\, v$ and $[v, fw] = f[v, w] + (vf)\, w$;
>
> (ii) $\nabla_{fv} w = f \nabla_v w$ and $\nabla_v(fw) = (vf)\, w + f \nabla_v w$;
>
> (iii) $T(w, v) = -T(v, w)$, $T(f_1 v, w) = f_1 T(v, w)$, $T(v, f_2 w) = f_2 T(v, w)$, and hence $T(f_1 v, f_2 w) = f_1 f_2 T(v, w)$.
>
> **Hint:** For (i), apply both sides to a test function $g$ and use that vector fields are derivations. For (ii), contract the Leibniz rule $\nabla(fw) = df \otimes w + f \nabla w$ with $v$. Then (iii) is bookkeeping in which the $(wf) v$ terms cancel.
>
> **Why needed:** (iii) is the hypothesis of Part II for the torsion; this lemma is Haydys's "easy to check" on p. 22, written out.
>
> > [!note]- Full proof
> > We assume $\nabla$ is a connection on $TM$ and must prove the three groups of identities.
> >
> > **(i) The bracket identity.** By [[Def - The Lie Bracket of Vector Fields]], $[X, Y]$ is the vector field acting on $g \in C^\infty(M)$ by $[X, Y] g = X(Yg) - Y(Xg)$, and a vector field $X$ acts on functions as a derivation: $X(g_1 g_2) = (Xg_1) g_2 + g_1 (Xg_2)$, and $(fX) g = f\, (Xg)$ by the pointwise definition of $fX$. For any $g \in C^\infty(M)$,
> > $$[fv, w] g = (fv)(wg) - w\big((fv) g\big) = f\, v(wg) - w\big(f\, (vg)\big) \qquad \text{(definition of the bracket; } (fv)(\cdot) = f\, v(\cdot)\text{)}$$
> > $$= f\, v(wg) - (wf)(vg) - f\, w(vg) = f\big(v(wg) - w(vg)\big) - (wf)(vg) \qquad \text{(derivation property of } w \text{ on the product } f \cdot (vg)\text{; regrouping)}$$
> > $$= f\, [v, w] g - (wf)\, (vg) = \big(f[v, w] - (wf)\, v\big) g \qquad \text{(definition of the bracket; pointwise operations on vector fields).}$$
> > Two vector fields that agree on every smooth function are equal (a tangent vector is determined by its action on functions, [[Def - Vector Field on a Manifold]]), so $[fv, w] = f[v, w] - (wf) v$. For the second identity, by antisymmetry of the bracket ($[X, Y] g = X(Yg) - Y(Xg) = -[Y, X] g$),
> > $$[v, fw] = -[fw, v] = -\big(f[w, v] - (vf)\, w\big) = f[v, w] + (vf)\, w \qquad \text{(antisymmetry; the first identity with } (v, w) \text{ replaced by } (w, v) \text{; antisymmetry again).}$$
> >
> > **(ii) The directional derivative.** By definition $\nabla_v w = \iota_v \nabla w$, where for an $E$-valued $1$-form $\omega$ the contraction $\iota_v \omega$ is the section with $(\iota_v \omega)(m) = \omega(m)(v(m))$ (evaluate the $T^*_m M$-factor on $v(m)$; [[Def - Interior Product (Contraction with a Vector Field)]] and [[Def - Connection on a Vector Bundle]]). Since $\omega(m) \in T^*_m M \otimes E_m$ is evaluated linearly on $v(m)$, $(\iota_{fv} \omega)(m) = \omega(m)(f(m) v(m)) = f(m)\, \omega(m)(v(m))$, so $\iota_{fv} \omega = f\, \iota_v \omega$ and hence $\nabla_{fv} w = f \nabla_v w$. For the second identity, by the Leibniz rule (the defining property of a connection, [[Def - Connection on a Vector Bundle]]),
> > $$\nabla_v(fw) = \iota_v\big(df \otimes w + f \nabla w\big) = df(v)\, w + f\, \iota_v \nabla w = (vf)\, w + f \nabla_v w \qquad \text{(Leibniz rule; } \iota_v \text{ is additive and } \iota_v(df \otimes w) = df(v) w \text{; } df(v) = vf \text{ by definition of the differential).}$$
> >
> > **(iii) Antisymmetry and bilinearity of $T$.** Antisymmetry: $T(w, v) = \nabla_w v - \nabla_v w - [w, v] = -(\nabla_v w - \nabla_w v - [v, w]) = -T(v, w)$, using $[w, v] = -[v, w]$. Linearity in the first slot:
> > $$T(f_1 v, w) = \nabla_{f_1 v} w - \nabla_w(f_1 v) - [f_1 v, w] \qquad \text{(definition of } T\text{)}$$
> > $$= f_1 \nabla_v w - (wf_1)\, v - f_1 \nabla_w v - f_1 [v, w] + (wf_1)\, v \qquad \text{(by (ii) for the first two terms and (i) for the bracket)}$$
> > $$= f_1\big(\nabla_v w - \nabla_w v - [v, w]\big) = f_1 T(v, w) \qquad \text{(the two } (wf_1) v \text{ terms cancel).}$$
> > Linearity in the second slot: by antisymmetry and the first-slot identity,
> > $$T(v, f_2 w) = -T(f_2 w, v) = -f_2 T(w, v) = f_2 T(v, w).$$
> > Combining, $T(f_1 v, f_2 w) = f_1 T(v, f_2 w) = f_1 f_2 T(v, w)$. Additivity in each slot follows from the additivity of $\nabla_v$ in the section, of $v \mapsto \nabla_v$ (by (ii) with the pointwise linearity of $\iota_v$ in $v$), and of the bracket in each argument (immediate from $[X, Y] g = X(Yg) - Y(Xg)$).
> >
> > Therefore the torsion is antisymmetric and $C^\infty(M)$-bilinear. $\blacksquare$

> [!note]- Lemma 7: Antisymmetric bilinear maps are elements of $\Lambda^2 V^* \otimes W$
> **Statement:** Let $V$, $W$ be finite-dimensional real vector spaces with bases $(v_j)_{j=1}^n$ and $(w_i)_{i=1}^l$, and let $(v^j)$ be the dual basis of $V^*$. Identify $\Lambda^2 V^*$ with the alternating bilinear forms on $V$, with $v^{j_1} \wedge v^{j_2}$ the alternating form $(x, y) \mapsto v^{j_1}(x) v^{j_2}(y) - v^{j_2}(x) v^{j_1}(y)$ ([[Def - Alternating Tensor and Lambda k V Dual]], the elementary alternating tensor $\varepsilon^{(j_1, j_2)}$). Then the linear map
> $$\Xi : \Lambda^2 V^* \otimes W \longrightarrow \operatorname{Alt}^2(V; W) := \{\text{alternating bilinear maps } V \times V \to W\}, \qquad \Xi(\beta \otimes w)(x, y) := \beta(x, y)\, w,$$
> is a linear isomorphism. If $\tau \in \operatorname{Alt}^2(V; W)$ has $\tau(v_{j_1}, v_{j_2}) = \sum_i \tau^i_{j_1 j_2} w_i$, then $\Xi^{-1}(\tau) = \sum_{j_1 < j_2} \sum_i \tau^i_{j_1 j_2}\, v^{j_1} \wedge v^{j_2} \otimes w_i$.
>
> **Hint:** $\Xi$ is well defined by the universal property; it sends the basis $v^{j_1} \wedge v^{j_2} \otimes w_i$ ($j_1 < j_2$) to the alternating maps determined by "$(v_{j_1}, v_{j_2}) \mapsto w_i$", which form a basis of $\operatorname{Alt}^2(V; W)$.
>
> **Why needed:** It turns the antisymmetric bilinear map $T_m$ delivered by Part II into an element of $\Lambda^2 T^*_m M \otimes T_m M$, and its explicit inverse shows that the resulting section is smooth when $T_m$ depends smoothly on $m$.
>
> > [!note]- Full proof
> > We must show that $\Xi$ is well defined, that it is an isomorphism, and that its inverse is given by the displayed formula.
> >
> > **Well-definedness.** The map $(\beta, w) \mapsto \big((x, y) \mapsto \beta(x, y) w\big)$ is bilinear in $(\beta, w)$ and takes values in bilinear maps $V \times V \to W$ that are alternating because $\beta$ is; by the universal property of the tensor product ([[Def - Tensor Product of Vector Spaces]]) it induces a unique linear $\Xi$ on $\Lambda^2 V^* \otimes W$.
> >
> > **A basis of $\operatorname{Alt}^2(V; W)$.** An alternating bilinear map $\tau$ is determined by the values $\tau(v_{j_1}, v_{j_2})$ for $j_1 < j_2$: bilinearity determines $\tau$ from all $\tau(v_{j_1}, v_{j_2})$, alternation gives $\tau(v_j, v_j) = 0$ and $\tau(v_{j_2}, v_{j_1}) = -\tau(v_{j_1}, v_{j_2})$. Conversely, for each $j_1 < j_2$ and $i$, the map $\chi_{i; j_1 j_2}(x, y) := \big(v^{j_1}(x) v^{j_2}(y) - v^{j_2}(x) v^{j_1}(y)\big) w_i$ is bilinear and alternating (it is $\Xi(v^{j_1} \wedge v^{j_2} \otimes w_i)$) and satisfies $\chi_{i; j_1 j_2}(v_{j'_1}, v_{j'_2}) = (\delta_{j_1 j'_1} \delta_{j_2 j'_2} - \delta_{j_2 j'_1} \delta_{j_1 j'_2}) w_i$, which for $j'_1 < j'_2$ equals $\delta_{j_1 j'_1} \delta_{j_2 j'_2} w_i$ (the second product vanishes since $j_2 > j_1$ and $j'_1 < j'_2$ cannot both hold with $j_2 = j'_1$ and $j_1 = j'_2$). Hence for any $\tau$ with $\tau(v_{j_1}, v_{j_2}) = \sum_i \tau^i_{j_1 j_2} w_i$, the alternating maps $\tau$ and $\sum_{j_1 < j_2} \sum_i \tau^i_{j_1 j_2} \chi_{i; j_1 j_2}$ agree on all pairs $(v_{j'_1}, v_{j'_2})$ with $j'_1 < j'_2$, hence everywhere; and the expansion is unique since evaluating $\sum c^i_{j_1 j_2} \chi_{i; j_1 j_2} = 0$ on $(v_{j'_1}, v_{j'_2})$ gives $\sum_i c^i_{j'_1 j'_2} w_i = 0$, so all coefficients vanish. Thus $\{\chi_{i; j_1 j_2} : j_1 < j_2,\ 1 \le i \le l\}$ is a basis of $\operatorname{Alt}^2(V; W)$.
> >
> > **$\Xi$ maps basis to basis.** The elements $v^{j_1} \wedge v^{j_2}$ with $j_1 < j_2$ form a basis of $\Lambda^2 V^*$ ([[Def - Alternating Tensor and Lambda k V Dual]]: the elementary alternating tensors with increasing multi-index), so $\{v^{j_1} \wedge v^{j_2} \otimes w_i\}$ is a basis of $\Lambda^2 V^* \otimes W$ (tensor product of bases), and $\Xi(v^{j_1} \wedge v^{j_2} \otimes w_i) = \chi_{i; j_1 j_2}$ by the definition of $\Xi$ and of $v^{j_1} \wedge v^{j_2}$. A linear map sending a basis bijectively to a basis is an isomorphism, and the inverse formula is the expansion just established.
> >
> > Therefore $\Lambda^2 V^* \otimes W$ is canonically the space of alternating bilinear maps $V \times V \to W$, with the stated coordinate formula. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout, $A : \Gamma(E) \to \Omega^p(M; F)$ is $\mathbb{R}$-linear and $C^\infty(M)$-linear (Part I), or $A : \Gamma(E_1) \times \cdots \times \Gamma(E_r) \to \Omega^p(M; F)$ is $C^\infty(M)$-multilinear (Part II). We must prove: in Part I, the existence (a), uniqueness and formula (b), and converse (c), and the module-isomorphism statement; in Part II, existence, uniqueness, and the converse for multilinear maps; and finally the corollary on the torsion.
>
> **Step 0 — Preconditions: the objects in the statement are well defined.**
>
> *The pairing $a \cdot s$ is a smooth $F$-valued $p$-form.* Let $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ and $s \in \Gamma(E)$. By Lemma 1, $\Theta_m$ is a linear isomorphism at each $m$, so $a_m = \Theta_m(a(m))$ is a well-defined linear map $E_m \to \Lambda^p T^*_m M \otimes F_m$ and $(a \cdot s)(m) := a_m(s(m))$ is a well-defined element of $\Lambda^p T^*_m M \otimes F_m$. To see that $m \mapsto (a \cdot s)(m)$ is smooth, fix $m_0 \in M$ and, by Lemma 2 and the definition of a manifold, choose a chart $(U; x^i)$ around $m_0$ over which $E$ has a frame $e$ and $F$ a frame $h$ (intersect the chart domain with the two frame domains). By Lemma 5(iii), $a|_U = \sum_{I, i, j} a^I_{ij}\, dx^I \otimes \phi_{ij}$ with $a^I_{ij} \in C^\infty(U)$, and by [[Thm - Local Frames Span Sections]], $s|_U = \sum_j \sigma_j e_j$ with $\sigma_j \in C^\infty(U)$. By the component formula of Lemma 1 (applied at each $m \in U$ with $\alpha_I = dx^I|_m$, $v_j = e_j(m)$, $w_i = h_i(m)$),
> $$(a \cdot s)(m) = \sum_{I, i, j} a^I_{ij}(m)\, \sigma_j(m)\; dx^I|_m \otimes h_i(m) \qquad (m \in U) \qquad \text{(Lemma 1, component formula).}$$
> The coefficients $\sum_j a^I_{ij} \sigma_j$ are smooth on $U$ (finite sums of products of smooth functions), so by Lemma 5(iii) $a \cdot s$ is smooth on $U$. Since $m_0$ was arbitrary and smoothness is local, $a \cdot s \in \Omega^p(M; F)$.
>
> *Every $v \in E_m$ is the value of a global section.* This is Lemma 2(iii).
>
> **Part I. Linear maps.**
>
> **Step 1 — Locality.** By Lemma 3, if $s \in \Gamma(E)$ vanishes on an open set $U$, then $A(s)$ vanishes on $U$.
>
> **Step 2 — Pointwise dependence.** By Lemma 4, if $s(m) = 0$ then $A(s)(m) = 0$. Consequently, if $s, s' \in \Gamma(E)$ satisfy $s(m) = s'(m)$, then
> $$A(s)(m) - A(s')(m) = A(s - s')(m) = 0 \qquad \text{(} \mathbb{R}\text{-linearity of } A \text{ and pointwise subtraction in } \Omega^p(M; F) \text{; Lemma 4 applied to } s - s' \text{, which vanishes at } m\text{)},$$
> so $A(s)(m) = A(s')(m)$.
>
> **Step 3 — Definition of $a_m$, well-definedness, and linearity.** For $m \in M$ and $v \in E_m$ define
> $$a_m(v) := A(s)(m) \in \Lambda^p T^*_m M \otimes F_m, \qquad \text{where } s \in \Gamma(E) \text{ is any section with } s(m) = v.$$
> *Existence of $s$:* Lemma 2(iii). *Independence of $s$:* Step 2. So $a_m : E_m \to \Lambda^p T^*_m M \otimes F_m$ is a well-defined map. *Linearity:* let $v, v' \in E_m$ and $\lambda \in \mathbb{R}$, and choose $s, s' \in \Gamma(E)$ with $s(m) = v$, $s'(m) = v'$. Then $s + \lambda s' \in \Gamma(E)$ has $(s + \lambda s')(m) = v + \lambda v'$ (pointwise operations), so
> $$a_m(v + \lambda v') = A(s + \lambda s')(m) = A(s)(m) + \lambda A(s')(m) = a_m(v) + \lambda\, a_m(v') \qquad \text{(definition of } a_m \text{ with the extension } s + \lambda s' \text{; } \mathbb{R}\text{-linearity of } A \text{ and pointwise operations; definition of } a_m\text{)}.$$
> Hence $a_m \in \operatorname{Hom}(E_m, \Lambda^p T^*_m M \otimes F_m)$, and by Lemma 1 there is a unique $a(m) := \Theta_m^{-1}(a_m) \in \Lambda^p T^*_m M \otimes \operatorname{Hom}(E_m, F_m)$. This defines $a$ as a (so far not necessarily smooth) section of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$.
>
> **Step 4 — Smoothness of $a$.** Fix $m_0 \in M$. Choose a chart $(U; x^i)$ around $m_0$ over which $E$ has a frame $e$ and $F$ a frame $h$ (as in Step 0). By Lemma 2(i)–(iii) applied at $m_0$, there are an open $V$ with $m_0 \in V \subseteq U$, a bump function $\psi$ with $\psi \equiv 1$ on $V$ and $\operatorname{supp} \psi \subseteq U$, and global sections $\tilde e_j = \widetilde{\psi e_j} \in \Gamma(E)$ with $\tilde e_j = e_j$ on $V$. For every $m \in V$ and every $j$,
> $$a_m(e_j(m)) = a_m(\tilde e_j(m)) = A(\tilde e_j)(m) \qquad \text{(} \tilde e_j(m) = e_j(m) \text{ for } m \in V \text{; definition of } a_m \text{ with the extension } \tilde e_j\text{)}.$$
> Now $A(\tilde e_j) \in \Omega^p(M; F)$ is smooth, so by Lemma 5(iii) its restriction to $U$ — and hence to $V$ — has smooth coefficients in the frame $dx^I \otimes h_i$: $A(\tilde e_j)|_V = \sum_{I, i} c^I_{ij}\, dx^I \otimes h_i$ with $c^I_{ij} \in C^\infty(V)$. By Lemma 5(iv), the coefficients of $a$ in the frame $dx^I \otimes \phi_{ij}$ are read off from $a_m(e_j(m))$: writing $a(m) = \sum_{I, i, j} a^I_{ij}(m)\, dx^I|_m \otimes \phi_{ij}(m)$ (pointwise expansion in the basis of Lemma 5(ii)), we have $a_m(e_j(m)) = \sum_{I, i} a^I_{ij}(m)\, dx^I|_m \otimes h_i(m)$, and comparing with the display above, $a^I_{ij}(m) = c^I_{ij}(m)$ for all $m \in V$ (uniqueness of coefficients in a basis). So the coefficients $a^I_{ij}$ are smooth on $V$, and by Lemma 5(iii) $a$ is smooth on $V$. Since $m_0$ was arbitrary and smoothness is local, $a \in \Omega^p(M; \operatorname{Hom}(E, F))$.
>
> **Step 5 — $A(s) = a \cdot s$ for every $s$.** Let $s \in \Gamma(E)$ and $m \in M$. The section $s$ itself is a global section with value $s(m)$ at $m$, so by the definition of $a_m$ in Step 3 with this choice of extension,
> $$(a \cdot s)(m) = a_m(s(m)) = A(s)(m) \qquad \text{(definition of the pairing; definition of } a_m \text{ with extension } s\text{)}.$$
> As $m$ is arbitrary, $a \cdot s = A(s)$. Together with Step 4 this proves (a).
>
> **Step 6 — Uniqueness of $a$ and the formula (b).** Suppose $a' \in \Omega^p(M; \operatorname{Hom}(E, F))$ also satisfies $a' \cdot s = A(s)$ for all $s$. Let $m \in M$ and $v \in E_m$; choose $s \in \Gamma(E)$ with $s(m) = v$ (Lemma 2(iii)). Then
> $$a'_m(v) = a'_m(s(m)) = (a' \cdot s)(m) = A(s)(m) = a_m(v) \qquad \text{(} s(m) = v \text{; definition of the pairing; hypothesis on } a' \text{; Step 3).}$$
> So $a'_m = a_m$ for all $m$, hence $a'(m) = \Theta_m^{-1}(a'_m) = \Theta_m^{-1}(a_m) = a(m)$ for all $m$ (Lemma 1, $\Theta_m$ injective), i.e. $a' = a$. The formula $a_m(v) = A(s)(m)$ for any $s$ with $s(m) = v$ is the definition of Step 3, whose independence of $s$ was Step 2 and whose existence of $s$ was Lemma 2(iii). This proves (b).
>
> **Step 7 — The converse (c).** Let $a \in \Omega^p(M; \operatorname{Hom}(E, F))$. By Step 0, $s \mapsto a \cdot s$ maps $\Gamma(E)$ into $\Omega^p(M; F)$. For $s, s' \in \Gamma(E)$, $f \in C^\infty(M)$, $\lambda \in \mathbb{R}$, and $m \in M$,
> $$\big(a \cdot (s + \lambda s')\big)(m) = a_m\big(s(m) + \lambda s'(m)\big) = a_m(s(m)) + \lambda\, a_m(s'(m)) = \big(a \cdot s + \lambda\, a \cdot s'\big)(m) \qquad \text{(pointwise operations; linearity of } a_m \text{; pointwise operations)},$$
> $$\big(a \cdot (fs)\big)(m) = a_m\big(f(m)\, s(m)\big) = f(m)\, a_m(s(m)) = \big(f\, (a \cdot s)\big)(m) \qquad \text{(pointwise module structure; linearity of } a_m \text{; pointwise module structure).}$$
> Hence $s \mapsto a \cdot s$ is $\mathbb{R}$-linear and $C^\infty(M)$-linear. This proves (c).
>
> **Step 8 — The bijection is a $C^\infty(M)$-module isomorphism.** By (a) and (c) the map $\Phi : a \mapsto (s \mapsto a \cdot s)$ sends $\Omega^p(M; \operatorname{Hom}(E, F))$ into the $C^\infty(M)$-linear maps $\Gamma(E) \to \Omega^p(M; F)$ and is surjective; by (b) it is injective. It is $C^\infty(M)$-linear: for $a, a'$ and $g \in C^\infty(M)$, $\big((a + g a') \cdot s\big)(m) = \Theta_m\big(a(m) + g(m) a'(m)\big)(s(m)) = a_m(s(m)) + g(m)\, a'_m(s(m))$ by linearity of $\Theta_m$, which is $\big(a \cdot s + g\,(a' \cdot s)\big)(m)$. A bijective module homomorphism is a module isomorphism.
>
> Therefore Part I holds.
>
> **Part II. Multilinear maps.**
>
> Assume $A : \Gamma(E_1) \times \cdots \times \Gamma(E_r) \to \Omega^p(M; F)$ is $C^\infty(M)$-multilinear. We must produce a unique smooth section $a$ of $\Lambda^p T^*M \otimes \operatorname{Hom}(E_1 \otimes \cdots \otimes E_r, F)$ with $A(s_1, \dots, s_r)(m) = a_m(s_1(m), \dots, s_r(m))$, and prove the converse.
>
> **Step 1′ — Locality and pointwise dependence in each slot.** By the multilinear parts of Lemma 3 and Lemma 4: if some $s_q$ vanishes on an open set $U$ then $A(s_1, \dots, s_r)$ vanishes on $U$, and if some $s_q(m) = 0$ then $A(s_1, \dots, s_r)(m) = 0$.
>
> **Step 2′ — Definition of $a_m$ and well-definedness by telescoping.** For $m \in M$ and $v_q \in E_{q, m}$ ($1 \le q \le r$), choose $s_q \in \Gamma(E_q)$ with $s_q(m) = v_q$ (Lemma 2(iii) for each $E_q$) and define
> $$a_m(v_1, \dots, v_r) := A(s_1, \dots, s_r)(m).$$
> If $s'_q \in \Gamma(E_q)$ are other choices with $s'_q(m) = v_q$, then
> $$A(s_1, \dots, s_r)(m) - A(s'_1, \dots, s'_r)(m) = \sum_{q=1}^r \Big[ A(s'_1, \dots, s'_{q-1}, s_q, s_{q+1}, \dots, s_r)(m) - A(s'_1, \dots, s'_{q-1}, s'_q, s_{q+1}, \dots, s_r)(m) \Big] \qquad \text{(telescoping sum: the } q\text{-th bracket's second term is the } (q+1)\text{-st bracket's first term; the first term of } q = 1 \text{ is } A(s_1, \dots, s_r)(m) \text{ and the second term of } q = r \text{ is } A(s'_1, \dots, s'_r)(m)\text{)}$$
> $$= \sum_{q=1}^r A(s'_1, \dots, s'_{q-1}, s_q - s'_q, s_{q+1}, \dots, s_r)(m) = 0 \qquad \text{(additivity in slot } q \text{; Step 1′, since } (s_q - s'_q)(m) = v_q - v_q = 0\text{)}.$$
> So $a_m$ is well defined.
>
> **Step 3′ — $a_m$ is $r$-linear.** Fix a slot $q$, vectors $v_{q'} \in E_{q', m}$ for $q' \neq q$, and $v_q, v'_q \in E_{q,m}$, $\lambda \in \mathbb{R}$; choose extensions $s_{q'}$ of the $v_{q'}$ and $s_q, s'_q$ of $v_q, v'_q$. Then $s_q + \lambda s'_q$ extends $v_q + \lambda v'_q$, so
> $$a_m(\dots, v_q + \lambda v'_q, \dots) = A(\dots, s_q + \lambda s'_q, \dots)(m) = A(\dots, s_q, \dots)(m) + \lambda A(\dots, s'_q, \dots)(m) = a_m(\dots, v_q, \dots) + \lambda\, a_m(\dots, v'_q, \dots) \qquad \text{(definition of } a_m \text{; } \mathbb{R}\text{-linearity of } A \text{ in slot } q \text{ with pointwise operations; definition of } a_m\text{)}.$$
> Hence $a_m$ is an $r$-linear map $E_{1,m} \times \cdots \times E_{r,m} \to \Lambda^p T^*_m M \otimes F_m$, which by the universal property of the tensor product is an element of $\operatorname{Hom}(E_{1,m} \otimes \cdots \otimes E_{r,m}, \Lambda^p T^*_m M \otimes F_m)$ and, by Lemma 1 with $V = E_{1,m} \otimes \cdots \otimes E_{r,m}$ and $W = F_m$, an element $a(m)$ of $\Lambda^p T^*_m M \otimes \operatorname{Hom}(E_{1,m} \otimes \cdots \otimes E_{r,m}, F_m)$.
>
> **Step 4′ — Smoothness.** Fix $m_0$ and a chart $(U; x^i)$ around $m_0$ over which each $E_q$ has a frame $e^{(q)}$ and $F$ a frame $h$. By Lemma 2 there are $V \ni m_0$, $\psi$, and cut-off sections $\tilde e^{(q)}_j = \widetilde{\psi e^{(q)}_j} \in \Gamma(E_q)$ with $\tilde e^{(q)}_j = e^{(q)}_j$ on $V$. For $m \in V$,
> $$a_m\big(e^{(1)}_{j_1}(m), \dots, e^{(r)}_{j_r}(m)\big) = A\big(\tilde e^{(1)}_{j_1}, \dots, \tilde e^{(r)}_{j_r}\big)(m) \qquad \text{(} \tilde e^{(q)}_{j} = e^{(q)}_{j} \text{ on } V \text{; definition of } a_m\text{)}.$$
> The right-hand side is a smooth $F$-valued $p$-form on $M$, so by Lemma 5(iii) its coefficients $c^I_{i; j_1 \cdots j_r}$ in the frame $dx^I \otimes h_i$ are smooth on $V$; by the multilinear version of Lemma 5(iv) these are the coefficients of $a$ in the frame $dx^I \otimes \phi_{i; j_1 \cdots j_r}$ on $V$; by the multilinear version of Lemma 5(iii), $a$ is smooth on $V$. As $m_0$ is arbitrary, $a$ is a smooth section.
>
> **Step 5′ — The identity, uniqueness, and the converse.** For any $s_q \in \Gamma(E_q)$ and $m \in M$, taking the $s_q$ themselves as the extensions of the $s_q(m)$ gives $a_m(s_1(m), \dots, s_r(m)) = A(s_1, \dots, s_r)(m)$. If $a'$ is another smooth section with this property, then for $v_q \in E_{q,m}$ with extensions $s_q$, $a'_m(v_1, \dots, v_r) = A(s_1, \dots, s_r)(m) = a_m(v_1, \dots, v_r)$, so $a' = a$. Conversely, for a smooth section $a$ of $\Lambda^p T^*M \otimes \operatorname{Hom}(E_1 \otimes \cdots \otimes E_r, F)$, the map $(s_1, \dots, s_r) \mapsto \big(m \mapsto a_m(s_1(m), \dots, s_r(m))\big)$ takes values in smooth forms (in a chart, its coefficients are $\sum_{j_1, \dots, j_r} a^I_{i; j_1 \cdots j_r}\, \sigma^{(1)}_{j_1} \cdots \sigma^{(r)}_{j_r}$, products of smooth functions, where $\sigma^{(q)}_j$ are the components of $s_q$; Lemma 5(iii)) and is $C^\infty(M)$-linear in each slot because $a_m$ is linear in each slot and $(f s_q)(m) = f(m) s_q(m)$:
> $$a_m\big(s_1(m), \dots, f(m) s_q(m), \dots, s_r(m)\big) = f(m)\, a_m\big(s_1(m), \dots, s_q(m), \dots, s_r(m)\big) \qquad \text{(linearity of } a_m \text{ in slot } q\text{).}$$
>
> Therefore Part II holds.
>
> **Part III. The corollary on the torsion.**
>
> Let $\nabla$ be a connection on $TM$ and $T(v, w) = \nabla_v w - \nabla_w v - [v, w]$. By Lemma 6(iii), $T : \mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M) = \Omega^0(M; TM)$ is antisymmetric and $C^\infty(M)$-bilinear. By Part II with $r = 2$, $E_1 = E_2 = F = TM$, $p = 0$, there is a unique smooth section $\tau$ of $\operatorname{Hom}(TM \otimes TM, TM)$, i.e. a smooth family of bilinear maps $\tau_m : T_m M \times T_m M \to T_m M$, with $T(v, w)(m) = \tau_m(v(m), w(m))$. Each $\tau_m$ is antisymmetric: for $x, y \in T_m M$ choose $v, w \in \mathfrak{X}(M)$ with $v(m) = x$, $w(m) = y$ (Lemma 2(iii)); then $\tau_m(y, x) = T(w, v)(m) = -T(v, w)(m) = -\tau_m(x, y)$ (Lemma 6(iii)). Hence $\tau_m \in \operatorname{Alt}^2(T_m M; T_m M)$ (an antisymmetric bilinear map over $\mathbb{R}$ is alternating: $\tau_m(x, x) = -\tau_m(x, x)$ forces $\tau_m(x, x) = 0$). By Lemma 7 with $V = W = T_m M$, $\tau_m = \Xi_m(T_m)$ for a unique $T_m \in \Lambda^2 T^*_m M \otimes T_m M$, given in a chart by
> $$T_m = \sum_{j_1 < j_2} \sum_i \tau^i_{j_1 j_2}(m)\; dx^{j_1}|_m \wedge dx^{j_2}|_m \otimes \partial_i|_m, \qquad \tau_m(\partial_{j_1}|_m, \partial_{j_2}|_m) = \sum_i \tau^i_{j_1 j_2}(m)\, \partial_i|_m \qquad \text{(Lemma 7, inverse formula).}$$
> The coefficient functions $\tau^i_{j_1 j_2}$ are the coefficients of the smooth section $\tau$ in the frame $\phi_{i; j_1 j_2}$ of $\operatorname{Hom}(TM \otimes TM, TM)$ (multilinear version of Lemma 5(iv) with $p = 0$), hence smooth (Lemma 5(iii)); therefore $m \mapsto T_m$ has smooth coefficients in the frame $dx^{j_1} \wedge dx^{j_2} \otimes \partial_i$ of $\Lambda^2 T^*M \otimes TM$ and is smooth by Lemma 5(iii) (with $F = TM$, $p = 2$). So $T \in \Omega^2(M; TM)$, and $T_m(v(m), w(m)) = \tau_m(v(m), w(m)) = T(v, w)(m)$ under the identification $\Xi_m$. Uniqueness of $T$ follows from the uniqueness of $\tau$ (Part II) and the injectivity of $\Xi_m$ (Lemma 7).
>
> Therefore every $C^\infty(M)$-linear map $\Gamma(E) \to \Omega^p(M; F)$ is given by a unique $\operatorname{Hom}(E, F)$-valued $p$-form, every $C^\infty(M)$-multilinear map is given by a unique smooth family of multilinear maps on the fibres, and the torsion of a connection on $TM$ is a $TM$-valued $2$-form. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: the difference of the Levi-Civita connections of two metrics.** Let $g$ and $\tilde g = e^{2u} g$ be conformally related metrics on $M$, with Levi-Civita connections $\nabla$ and $\tilde\nabla$. Since both satisfy the Leibniz rule, $\tilde\nabla - \nabla$ is $C^\infty(M)$-linear in the section and, by the lemma with $E = F = TM$, $p = 1$, is a section $a$ of $T^*M \otimes \operatorname{End}(TM)$; compute it explicitly from the [[Thm - Koszul Formula|Koszul formula]] as $a(X) Y = (Xu) Y + (Yu) X - g(X, Y)\, \operatorname{grad} u$. The lemma applies because the derivative terms cancel; it is non-obvious because each of $\nabla$ and $\tilde\nabla$ separately is a differential operator, and the tensor $a$ is what a physicist would call the "conformal connection coefficients".

**Analysis on manifolds: a $C^\infty(M)$-linear map $\mathfrak{X}(M) \to C^\infty(M)$ is a $1$-form, but a derivation is not.** Show that a map $D : C^\infty(M) \to C^\infty(M)$ satisfying $D(fg) = f\, Dg + g\, Df$ (a derivation) is *never* $C^\infty(M)$-linear unless $D = 0$, and that conversely every $C^\infty(M)$-linear map $\mathfrak{X}(M) \to C^\infty(M)$ is $X \mapsto \omega(X)$ for a unique $1$-form $\omega$ (the case $E = TM$, $F = \underline{\mathbb{R}}$, $p = 0$ of the lemma, which is also the $k = 1$ case of [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions]]). The point of the exercise is the dichotomy between operators of order zero (tensors) and order one (derivations), which the lemma makes exact.

**Hodge theory and Clifford modules: the symbol of a first-order operator.** For a first-order differential operator $P : \Gamma(E) \to \Gamma(F)$ and $f \in C^\infty(M)$, the commutator $s \mapsto P(fs) - f\, P(s)$ is $C^\infty(M)$-linear (compute $P(gfs) - gf P(s) - g(P(fs) - fP(s)) = f(P(gs) - gP(s))$ using the Leibniz rule of a first-order operator) and depends only on $df$; the lemma identifies it with a bundle map $\sigma_P(df) : E \to F$, the principal symbol of $P$. For $P = d^\nabla$ on $\Omega^p(M; E)$ the symbol is $\sigma(\xi) = \xi \wedge (\,\cdot\,)$; for the Dirac operator of chapter VIII it is Clifford multiplication. The lemma is what makes the symbol a well-defined section of $\operatorname{Hom}(\pi^* E, \pi^* F)$ over $T^*M$, which is the starting point of the ellipticity theory of chapter IX.

**Gauge theory on a principal bundle: tensoriality of the curvature of a principal connection.** In chapter IV, the curvature $\Omega = d\omega + \tfrac12 [\omega \wedge \omega]$ of a connection $\omega$ on a principal bundle is shown to be horizontal and $\operatorname{Ad}$-equivariant, hence to descend to a $2$-form on $M$ with values in the adjoint bundle. The vector-bundle route to the same fact is the present lemma applied to $(X, Y, s) \mapsto \nabla_X \nabla_Y s - \nabla_Y \nabla_X s - \nabla_{[X, Y]} s$ (Part II with $r = 3$, $E_1 = E_2 = TM$, $E_3 = F = E$, $p = 0$), whose $C^\infty(M)$-trilinearity is the model proof of the series' proof standard. Comparing the two routes on an associated bundle is a worthwhile exercise: the bump-function argument and the horizontality argument establish the same pointwise dependence by different means.

---

# Bridges

**To the tensor characterisation lemma of differential geometry.** The page [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions]] proves that a map $\mathfrak{X}(M)^k \to C^\infty(M)$ is induced by a smooth covariant $k$-tensor field if and only if it is $C^\infty(M)$-multilinear. That is Part II of the present theorem with $E_1 = \cdots = E_k = TM$, $F = \underline{\mathbb{R}}$, and $p = 0$: the fibre $\operatorname{Hom}(T_m M^{\otimes k}, \mathbb{R}) = (T_m M^{\otimes k})^*$ is the space of covariant $k$-tensors at $m$, and the smooth family $m \mapsto a_m$ is a tensor field. The proof there is the same three-stage argument (locality, pointwise dependence, construction of the pointwise tensor), and the present page generalises it in two directions at once: the inputs may be sections of arbitrary bundles $E_q$, not only vector fields, and the outputs may be $F$-valued $p$-forms, not only functions. Nothing in the argument uses that $TM$ is a tangent bundle; what it uses is that $\Gamma(E)$ is a $C^\infty(M)$-module with local frames and that bump functions exist.

**To the affine structure on the space of connections.** In [[Thm - The Space of Connections is an Affine Space]], two connections $\nabla, \hat\nabla$ on $E$ have a difference satisfying $(\nabla - \hat\nabla)(fs) = f(\nabla - \hat\nabla)(s)$, because the term $df \otimes s$ in the Leibniz rule is the same for both. Part I(a) with $F = E$, $p = 1$ then gives $\nabla - \hat\nabla = a \cdot (\,\cdot\,)$ for a unique $a \in \Omega^1(M; \operatorname{End} E)$, and Part I(c) gives that $\nabla + a$ is again $\mathbb{R}$-linear and satisfies the Leibniz rule (since $a \cdot (fs) = f\, (a \cdot s)$ contributes no derivative term). The two halves of the present lemma are thus exactly the two halves of the statement "$\mathcal{A}(E)$ is a torsor for $\Omega^1(M; \operatorname{End} E)$".

**To the curvature form.** In [[Thm - Existence of the Curvature Form]], the operator $d^\nabla \circ \nabla : \Gamma(E) \to \Omega^2(M; E)$ is shown to be $C^\infty(M)$-linear by two applications of the Leibniz rule, the two $df \wedge \nabla s$ terms cancelling by the sign $(-1)^p$ in the definition of $d^\nabla$. Part I with $F = E$, $p = 2$ produces the unique $F_\nabla \in \Omega^2(M; \operatorname{End} E)$ with $d^\nabla(\nabla s) = F_\nabla \cdot s$; the uniqueness clause is what allows [[Thm - Local Formula for the Curvature of a Connection]] to compute $F_\nabla$ in a frame and know that the answer is the curvature. The three-slot form $(X, Y, s) \mapsto F_\nabla(X, Y) s$, used in [[Def - Curvature of a Vector-Bundle Connection]], is Part II with $r = 3$ followed by Lemma 7 in the two vector-field slots.

**To torsion and the Levi-Civita connection.** The corollary is Haydys's remark on p. 22 and the reason the torsion appears in [[Def - Torsion Tensor]] as a $(1, 2)$-tensor field: a $C^\infty(M)$-bilinear antisymmetric map $\mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$ is a section of $\Lambda^2 T^*M \otimes TM$. The torsion-free condition $T = 0$ is then a pointwise condition, which is what makes the uniqueness part of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]] a statement about a tensor vanishing rather than about an identity among differential operators; and the [[Def - Levi-Civita Connection|Levi-Civita connection]] is characterised by two tensorial conditions (torsion-free, metric-compatible), both of which are recognised as tensorial by the mechanism of this page.

**To the principal symbol and ellipticity.** In chapter IX, a differential operator $P$ of order $\ell$ between vector bundles has a principal symbol, a bundle map $\sigma_P(\xi) : E \to F$ for each covector $\xi$, defined through the $\ell$-fold commutator of $P$ with multiplication by functions. That the $\ell$-fold commutator is $C^\infty(M)$-linear — and hence, by the present lemma, a bundle map — is what makes the symbol a well-defined geometric object independent of coordinates, and ellipticity ($\sigma_P(\xi)$ invertible for $\xi \neq 0$) a pointwise condition. The tensoriality lemma is therefore the first step of the analytic theory as well as of the geometric one.

---

# Unlocked by This

> [!tip] The space of connections as an affine space *(from gauge theory)*
> With Part I(a) and (c) in hand, [[Thm - The Space of Connections is an Affine Space]] needs only the existence of one connection: every other connection is $\nabla + a$ for a unique $a \in \Omega^1(M; \operatorname{End} E)$.

> [!tip] The curvature form *(from gauge theory)*
> [[Thm - Existence of the Curvature Form]] is the lemma with $p = 2$ applied to $d^\nabla \circ \nabla$; the whole theory of curvature — the local formula, the Bianchi identity, Chern–Weil theory in chapter VI — begins with the fact that $F_\nabla$ is a form and not an operator.

> [!tip] Tensorial operators everywhere *(from differential geometry and analysis)*
> The same test — "does it commute with multiplication by functions?" — identifies the torsion, the second fundamental form of a submanifold, the principal symbol of a differential operator, and the curvature of a principal connection as bundle-valued forms. The forward references to the **second fundamental form** and to the **principal symbol** are to chapters not yet written in this series.
