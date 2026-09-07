---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Adjoint Representation"
  - "Def - Multilinear Form"
  - "Thm - Symmetrization and Alternation Projectors"
  - "Thm - Ad is a Smooth Representation and its Differential is ad"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group with Lie algebra $\mathfrak{g}=T_eG$, and $\mathbb{K}$ denotes the ground field, either $\mathbb{R}$ or $\mathbb{C}$. Haydys works over $\mathbb{C}$ for definiteness and remarks that the real case needs only straightforward modifications; we keep $\mathbb{K}$ general and specialise where a computation demands it. We write $\operatorname{Ad}\colon G\to GL(\mathfrak{g})$ for the [[Def - Adjoint Representation|adjoint representation]], $\operatorname{Ad}_g=d_e\alpha_g$ the differential at the identity of the conjugation $\alpha_g(h)=ghg^{-1}$; for a **matrix Lie group** $G\subseteq GL(n;\mathbb{K})$ this is $\operatorname{Ad}_g\xi=g\xi g^{-1}$, and the adjoint action of the Lie algebra is $\operatorname{ad}_\xi\eta=[\xi,\eta]=\xi\eta-\eta\xi$, the matrix commutator (all of this is recorded on [[Thm - Ad is a Smooth Representation and its Differential is ad]]). Every polynomial computation below is carried out for a matrix Lie group, as in both sources; the abstract definition and the infinitesimal-invariance corollary are stated for a general $G$.

A homogeneous polynomial of degree $d$ on $\mathfrak{g}$ is a function $p\colon\mathfrak{g}\to\mathbb{K}$ that, in linear coordinates $x_1,\dots,x_n$ associated to a basis $\xi_1,\dots,\xi_n$ of $\mathfrak{g}$ (so $\xi=\sum_ix_i\xi_i$), is given by a homogeneous polynomial of degree $d$ in $x_1,\dots,x_n$. A $d$-linear form on $\mathfrak{g}$ is a map $\lambda\colon\mathfrak{g}^d\to\mathbb{K}$ that is $\mathbb{K}$-linear in each of its $d$ arguments when the others are fixed (this is [[Def - Multilinear Form|the notion of a multilinear form]]); it is **symmetric** if $\lambda(\xi_{\sigma(1)},\dots,\xi_{\sigma(d)})=\lambda(\xi_1,\dots,\xi_d)$ for every permutation $\sigma\in S_d$. We write $S_d$ for the symmetric group on $d$ letters, $|S|$ for the cardinality of a finite set $S$, and $\operatorname{Sym}^d(\mathfrak{g}^*)$ for the space of symmetric $d$-linear forms on $\mathfrak{g}$. The full symbol registry for the chapter is on [[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional]].

> [!warning] Convention: two sources, one object
> Haydys (Introduction to Gauge Theory, §3.1) defines the object as an $\operatorname{Ad}$-invariant homogeneous **polynomial** $p\colon\mathfrak{g}\to\mathbb{K}$ satisfying three conditions. Bär (Gauge Theory, Definition 2.5.1) defines instead an invariant symmetric **multilinear form** $\lambda\colon\mathfrak{g}^d\to\mathbb{K}$. These are two views of the same data: the diagonal restriction $\xi\mapsto\lambda(\xi,\dots,\xi)$ turns a form into a polynomial, and the **polarisation identity** turns a polynomial back into a form. We prove the equivalence in full on this page, so that either source's definition may be used interchangeably in the sequel.

> [!warning] Convention: a typo in Haydys's Example 81(a)
> Haydys prints the invariant polynomial on $\mathfrak{u}(r)$ as $p_d(\xi)=i\operatorname{tr}\xi^d$. The factor $i$ makes $p_1$ real-valued but does **not** make $p_d$ real-valued for $d\ge2$. The correct $\mathbb{C}$-valued invariant is $p_d(\xi)=\operatorname{tr}\xi^d$, and the correct real-valued normalisation on $\mathfrak{u}(r)$ is $i^d\operatorname{tr}\xi^d$; we use these corrected forms and flag the change where it occurs.

---

# Axiom Motivation

We are building towards the Chern–Weil homomorphism, the machine that manufactures closed differential forms — and hence de Rham cohomology classes — out of the curvature of a connection. The curvature $F_a$ of a connection on a principal $G$-bundle is a $2$-form with values in the adjoint bundle; in a local frame it is a matrix of ordinary $2$-forms, a $\mathfrak{g}$-valued object. To extract from it a genuine, honest, scalar-valued form on the base manifold — something we can integrate and whose cohomology class we can compare across bundles — we must feed the matrix into a function $\mathfrak{g}\to\mathbb{K}$. The question this definition answers is: **which functions of the curvature descend to the base and produce closed forms whose class is a bundle invariant?** The three conditions below are precisely the answer, and each condition earns its place by ruling out a specific failure.

First, the function must be a **polynomial**. Curvature enters through wedge products of matrix-valued forms, and the operations available on forms are addition and the wedge product; a polynomial in the matrix entries is exactly what these operations can compute. A non-polynomial function — a trace of $\exp\xi$, say, or $\det(1+\xi)^{1/2}$ before expansion — cannot be evaluated on a matrix of $2$-forms by wedge and sum alone, because such forms are nilpotent (on a finite-dimensional manifold high wedge powers vanish) and only the polynomial part survives; asking for anything but a polynomial is asking for structure the differential-form calculus does not provide. The polynomiality condition is what lets $p(\pi^*F_a)$ even be defined.

Second, the polynomial must be **homogeneous of a fixed degree** $d$. This is the bookkeeping that makes the output land in a single cohomological degree. The curvature is a $2$-form; a monomial of degree $d$ in its entries is a wedge of $d$ two-forms, hence a $2d$-form. If the polynomial mixed degrees — a sum $p_2+p_3$, say — the output would mix a $4$-form and a $6$-form, and it could not represent a class in any one $H^k_{\mathrm{dR}}$. Dropping homogeneity is not fatal to the construction, since one may split any polynomial into its homogeneous pieces and treat each separately; but keeping it is the clean normalisation, and it is what makes "the degree of the invariant polynomial" a well-defined attribute equal to half the cohomological degree of the class it produces.

Third — and this is the condition with real content — the polynomial must be **$\operatorname{Ad}$-invariant**: $p(\operatorname{Ad}_g\xi)=p(\xi)$ for every $g\in G$. Here is what breaks without it. In a local frame the curvature is $F_a\in\Omega^2(U;\mathfrak{g})$, but the frame is not canonical: over an overlap $U\cap U'$ the two local curvatures are related by $F'=\operatorname{Ad}_{g^{-1}}F=g^{-1}Fg$ for the transition function $g$ (this is the transformation law recorded on [[Thm - Transformation of Local Connection and Curvature Forms]]). If we apply a polynomial $p$ that is not invariant under conjugation, we get $p(F')\ne p(F)$ on the overlap, so the locally defined forms $p(F_a)$ do not glue into a global form on $M$ at all. Concretely, the entry $\xi\mapsto\xi_{11}$ (the upper-left matrix entry, a perfectly good homogeneous polynomial of degree one) is destroyed by conjugation, and the "form" it would build is not even well-defined. Invariance is exactly the condition that the value of $p$ depends only on the $\operatorname{Ad}$-orbit of the curvature, and the orbit is the frame-independent datum. Equivalently, invariance is what allows $p(\pi^*F_a)$ on the total space to descend through the projection $\pi$ to the base, because the fibres of a principal bundle are $\operatorname{Ad}$-orbits.

There is one more thing the definition must capture, invisible in the three conditions but forced by them: invariance makes $p$ a function of the **eigenvalues** of $\xi$ alone (for the classical matrix groups), and this is why the invariant polynomials of the unitary group turn out to be generated by the elementary symmetric functions of the eigenvalues, which are the coefficients of the characteristic polynomial. A reader who has internalised "invariant under conjugation" and "polynomial" could, presented with the single example $\det(\lambda\mathbf{1}+\xi)$, reconstruct the entire ring of invariants; the definition is not arbitrary but the minimal frame under which the characteristic polynomial becomes the universal source of invariants. Finally, the invariance condition is genuinely tied to the group and not only to the Lie algebra: on $\mathfrak{so}(2m)$ the Pfaffian is invariant under $\operatorname{Ad}$ of the connected group $SO(2m)$ but changes sign under the extra component of $O(2m)$, which is exactly the algebraic shadow of the fact that the Euler class needs an orientation. Weaken "for all $g\in G$" to "for all $g$ in the identity component" and one admits the Pfaffian; that is the sense in which the quantifier over the whole group is load-bearing.

---

# The Definition

We give the polynomial form (Haydys) first, then the multilinear form (Bär), then prove they carry the same information.

**Primary form (invariant polynomial).** Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$. A function $p\colon\mathfrak{g}\to\mathbb{K}$ is an **$\operatorname{Ad}$-invariant homogeneous polynomial of degree $d$** if it satisfies all three of the following:

1. **Polynomiality.** For some (equivalently every) basis $\xi_1,\dots,\xi_n$ of $\mathfrak{g}$, the function $(x_1,\dots,x_n)\mapsto p(x_1\xi_1+\dots+x_n\xi_n)$ is a polynomial of degree $d$ in $x_1,\dots,x_n$.
2. **Invariance.** $p(\operatorname{Ad}_g\xi)=p(\xi)$ for all $g\in G$ and all $\xi\in\mathfrak{g}$.
3. **Homogeneity.** $p(\lambda\xi)=\lambda^d\,p(\xi)$ for all $\lambda\in\mathbb{K}$ and all $\xi\in\mathfrak{g}$.

(That polynomiality is basis-independent is immediate: a change of basis is a linear substitution $x_i\mapsto\sum_j a_{ij}x_j'$, which sends a polynomial of degree $d$ to a polynomial of degree $d$.)

**Equivalent form (invariant symmetric multilinear form).** A symmetric $d$-linear form $\lambda\colon\mathfrak{g}^d\to\mathbb{K}$ is **$\operatorname{Ad}$-invariant** if
$$\lambda(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)=\lambda(\xi_1,\dots,\xi_d)\qquad\text{for all }g\in G,\ \xi_1,\dots,\xi_d\in\mathfrak{g}.$$

**The two are equivalent — the polarisation identity.** The following proposition makes the correspondence precise. We write "$\lambda$ polarises $p$" to mean $p(\xi)=\lambda(\xi,\dots,\xi)$ for all $\xi$ (the diagonal restriction).

> **Proposition (polarisation).** Fix $d\ge1$.
> 1. **(Restriction.)** If $\lambda\in\operatorname{Sym}^d(\mathfrak{g}^*)$ is symmetric $d$-linear, then $p(\xi):=\lambda(\xi,\dots,\xi)$ is a homogeneous polynomial of degree $d$; and $p$ is $\operatorname{Ad}$-invariant if $\lambda$ is.
> 2. **(Polarisation.)** If $p\colon\mathfrak{g}\to\mathbb{K}$ is a homogeneous polynomial of degree $d$, then there is a **unique** symmetric $d$-linear form $\lambda$ polarising $p$, given by the explicit formula
> $$\lambda(\xi_1,\dots,\xi_d)=\frac{1}{d!}\sum_{S\subseteq\{1,\dots,d\}}(-1)^{d-|S|}\,p\!\left(\sum_{i\in S}\xi_i\right);\tag{$\ast$}$$
> and $\lambda$ is $\operatorname{Ad}$-invariant if $p$ is.
>
> Consequently the diagonal-restriction map $\operatorname{Sym}^d(\mathfrak{g}^*)\to\{\text{homogeneous degree-}d\text{ polynomials}\}$ is a linear isomorphism carrying invariant forms bijectively onto invariant polynomials.

In the smallest non-trivial case $d=2$ the formula $(\ast)$ reads
$$\lambda(\xi_1,\xi_2)=\tfrac12\big(p(\xi_1+\xi_2)-p(\xi_1)-p(\xi_2)\big),$$
the familiar recovery of a symmetric bilinear form from its associated quadratic form; the general formula is the same "inclusion–exclusion over the sum $\sum_{i\in S}\xi_i$" carried out in $d$ variables. Because of this equivalence we use the same symbol for a polynomial and its polar form, writing $p(\xi_1,\dots,\xi_d)$ for the multilinear form and $p(\xi)=p(\xi,\dots,\xi)$ for the polynomial, exactly as both sources do.

> [!note]- Proof of the polarisation proposition
> We prove the two parts, then the invariance transfer.
>
> **Part 1 (restriction gives a polynomial).** Let $\lambda\in\operatorname{Sym}^d(\mathfrak{g}^*)$ and set $p(\xi)=\lambda(\xi,\dots,\xi)$.
>
> **Homogeneity.** For $c\in\mathbb{K}$, pulling the scalar out of each of the $d$ slots by linearity,
> $$p(c\xi)=\lambda(c\xi,\dots,c\xi)=c^d\,\lambda(\xi,\dots,\xi)=c^d\,p(\xi)\qquad\text{($d$-linearity, one factor }c\text{ per slot).}$$
>
> **Polynomiality.** Fix a basis $\xi_1,\dots,\xi_n$ and write $\xi=\sum_i x_i\xi_i$. Expanding each of the $d$ slots by multilinearity,
> $$p(\xi)=\lambda\Big(\textstyle\sum_i x_i\xi_i,\dots,\sum_i x_i\xi_i\Big)=\sum_{i_1,\dots,i_d=1}^{n}x_{i_1}\cdots x_{i_d}\,\lambda(\xi_{i_1},\dots,\xi_{i_d})\qquad\text{(expand each slot; }d\text{-linearity),}$$
> a homogeneous polynomial of degree $d$ in $x_1,\dots,x_n$ with constant coefficients $\lambda(\xi_{i_1},\dots,\xi_{i_d})\in\mathbb{K}$.
>
> **Part 2 (polarisation gives a form).** Let $p$ be a homogeneous polynomial of degree $d$, and define $\lambda$ by $(\ast)$. We must show $\lambda$ is symmetric, $d$-linear, polarises $p$, and is unique.
>
> **Step 0 — a normalisation.** Since $p$ is homogeneous of degree $d\ge1$, $p(0)=p(0\cdot\xi)=0^d\,p(\xi)=0$, so the term $S=\varnothing$ in $(\ast)$ contributes $(-1)^d\,p(0)=0$ and may be kept or dropped freely; we keep it, as it simplifies the bookkeeping.
>
> **Step 1 — reduce to monomials.** Both sides of the assertions "$\lambda$ is $d$-linear, symmetric, and polarises $p$" are $\mathbb{K}$-linear in $p$: the map $p\mapsto\lambda$ defined by $(\ast)$ is linear, and diagonal restriction is linear. Every homogeneous degree-$d$ polynomial is a $\mathbb{K}$-linear combination of monomials $x^\alpha=x_1^{\alpha_1}\cdots x_n^{\alpha_n}$ with $|\alpha|:=\alpha_1+\dots+\alpha_n=d$. It therefore suffices to prove all the claims for a fixed monomial $p=x^\alpha$, viewing $x_i=e_i^*$ as the $i$-th coordinate functional on $\mathfrak{g}$ (the dual basis to $\xi_1,\dots,\xi_n$), and then extend by linearity.
>
> **Step 2 — an explicit symmetric form with the right diagonal.** Let $(m_1,\dots,m_d)$ be the multiset of indices in which the index $i$ appears exactly $\alpha_i$ times (so $\{m_1,\dots,m_d\}$ lists, with multiplicity, the variables occurring in $x^\alpha$). Define
> $$\mu(\eta_1,\dots,\eta_d):=\frac{1}{d!}\sum_{\sigma\in S_d}\;\prod_{k=1}^{d}x_{m_k}\big(\eta_{\sigma(k)}\big).$$
> Each factor $x_{m_k}(\eta_{\sigma(k)})$ is linear in the argument $\eta_{\sigma(k)}$, so $\mu$ is $d$-linear; and averaging over all of $S_d$ makes $\mu$ symmetric, since precomposing the arguments with a permutation $\tau$ merely reindexes the sum over $\sigma$. Its diagonal is
> $$\mu(\xi,\dots,\xi)=\frac{1}{d!}\sum_{\sigma\in S_d}\prod_{k=1}^{d}x_{m_k}(\xi)=\frac{1}{d!}\cdot d!\cdot\prod_{k=1}^d x_{m_k}(\xi)=x^\alpha(\xi)=p(\xi)\qquad\text{(each summand equals }\textstyle\prod_k x_{m_k}(\xi)\text{; there are }d!\text{ of them).}$$
> So **every homogeneous degree-$d$ polynomial is the diagonal of some symmetric $d$-linear form** (namely $\mu$, extended linearly in $p$). This establishes existence of a polar form; it remains to identify it with $(\ast)$ and prove uniqueness.
>
> **Step 3 — the polarisation formula inverts diagonal restriction.** We show: for **any** symmetric $d$-linear $\nu$, if $q(\xi)=\nu(\xi,\dots,\xi)$ is its diagonal, then formula $(\ast)$ applied to $q$ returns $\nu$. Substitute $q$ into $(\ast)$ and expand the inner diagonal by multilinearity: writing $\eta_S:=\sum_{i\in S}\xi_i$,
> $$q(\eta_S)=\nu(\eta_S,\dots,\eta_S)=\sum_{f\colon\{1,\dots,d\}\to S}\nu(\xi_{f(1)},\dots,\xi_{f(d)})\qquad\text{(expand each of the }d\text{ slots over }S\text{),}$$
> the sum running over all functions $f$ from the $d$ slots into the index set $S$. Hence
> $$\frac{1}{d!}\sum_{S\subseteq\{1,\dots,d\}}(-1)^{d-|S|}q(\eta_S)=\frac{1}{d!}\sum_{f\colon\{1,\dots,d\}\to\{1,\dots,d\}}\Big(\sum_{S\supseteq\operatorname{im}f}(-1)^{d-|S|}\Big)\,\nu(\xi_{f(1)},\dots,\xi_{f(d)}),$$
> where we regrouped by the function $f\colon\{1,\dots,d\}\to\{1,\dots,d\}$ and used that $f$ contributes to the $S$-term precisely when $\operatorname{im}f\subseteq S$. For a fixed $f$ with image size $m:=|\operatorname{im}f|$, the inner coefficient is, setting $N:=d-m$ and summing over the $\binom{N}{j}$ sets $S$ with $j$ elements beyond $\operatorname{im}f$,
> $$\sum_{S\supseteq\operatorname{im}f}(-1)^{d-|S|}=\sum_{j=0}^{N}\binom{N}{j}(-1)^{N-j}=(-1+1)^{N}=0^{N}\qquad\text{(binomial theorem with }a=-1,b=1\text{),}$$
> which is $0$ unless $N=0$, i.e. $m=d$, in which case it equals $1$. Thus only functions $f$ with $|\operatorname{im}f|=d$ survive; these are the bijections, that is, the permutations $\sigma\in S_d$. For each such $\sigma$, symmetry of $\nu$ gives $\nu(\xi_{\sigma(1)},\dots,\xi_{\sigma(d)})=\nu(\xi_1,\dots,\xi_d)$, and there are $d!$ of them. Therefore
> $$\frac{1}{d!}\sum_{S}(-1)^{d-|S|}q(\eta_S)=\frac{1}{d!}\cdot d!\cdot\nu(\xi_1,\dots,\xi_d)=\nu(\xi_1,\dots,\xi_d).$$
> This proves the claim: $(\ast)$ applied to the diagonal of $\nu$ returns $\nu$.
>
> **Step 4 — assemble existence, the formula, and uniqueness.** By Step 2, given $p$ there exists a symmetric $d$-linear $\mu$ with diagonal $p$. By Step 3 applied to $\nu=\mu$, formula $(\ast)$ applied to $p$ returns $\mu$; in particular the form defined by $(\ast)$ is symmetric and $d$-linear (it equals $\mu$) and polarises $p$ (its diagonal is that of $\mu$, namely $p$). For **uniqueness**, suppose $\nu_1,\nu_2$ are symmetric $d$-linear forms both polarising $p$. Then $(\ast)$ applied to $p$ returns $\nu_1$ (Step 3 with $\nu=\nu_1$) and equally returns $\nu_2$ (Step 3 with $\nu=\nu_2$); since $(\ast)$ is a single well-defined form, $\nu_1=\nu_2$. Hence the polar form is unique and given by $(\ast)$.
>
> **Isomorphism.** Diagonal restriction $R\colon\operatorname{Sym}^d(\mathfrak{g}^*)\to\{\text{homogeneous degree-}d\text{ polynomials}\}$ is linear; Step 2 shows it is surjective and Step 3 shows the linear map $P$ given by $(\ast)$ satisfies $R\circ P=\mathrm{id}$ and $P\circ R=\mathrm{id}$ (the latter is exactly Step 3). So $R$ is a linear isomorphism with inverse $P$.
>
> **Invariance transfer.** Suppose first $\lambda$ is $\operatorname{Ad}$-invariant and $p$ is its diagonal. Then for every $g\in G$,
> $$p(\operatorname{Ad}_g\xi)=\lambda(\operatorname{Ad}_g\xi,\dots,\operatorname{Ad}_g\xi)=\lambda(\xi,\dots,\xi)=p(\xi)\qquad\text{(invariance of }\lambda\text{),}$$
> so $p$ is invariant. Conversely, suppose $p$ is invariant and $\lambda$ is its polar form $(\ast)$. Fix $g\in G$. Because $\operatorname{Ad}_g$ is $\mathbb{K}$-linear, $\sum_{i\in S}\operatorname{Ad}_g\xi_i=\operatorname{Ad}_g\big(\sum_{i\in S}\xi_i\big)$, so
> $$\lambda(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)=\frac{1}{d!}\sum_{S}(-1)^{d-|S|}p\Big(\operatorname{Ad}_g\textstyle\sum_{i\in S}\xi_i\Big)=\frac{1}{d!}\sum_{S}(-1)^{d-|S|}p\Big(\textstyle\sum_{i\in S}\xi_i\Big)=\lambda(\xi_1,\dots,\xi_d),$$
> using the formula $(\ast)$, linearity of $\operatorname{Ad}_g$, and then invariance of $p$ term by term. So $\lambda$ is invariant. $\blacksquare$

**The ring of invariant polynomials.** Collect all invariant polynomials of all degrees. Write $I^d(G)$ for the set of $\operatorname{Ad}$-invariant homogeneous polynomials of degree $d$ (including $I^0(G)=\mathbb{K}$, the constants), and set
$$I(G):=\bigoplus_{d\ge0}I^d(G).$$
This is a graded commutative $\mathbb{K}$-algebra under pointwise addition and multiplication of functions, the **ring of invariant polynomials** of $G$. It is a subring of the full polynomial algebra $\operatorname{Sym}(\mathfrak{g}^*)=\bigoplus_d\operatorname{Sym}^d(\mathfrak{g}^*)$: if $p\in I^d(G)$ and $q\in I^e(G)$, then the product $pq$ is homogeneous of degree $d+e$ (a product of homogeneous polynomials of degrees $d,e$ is homogeneous of degree $d+e$) and invariant, since
$$(pq)(\operatorname{Ad}_g\xi)=p(\operatorname{Ad}_g\xi)\,q(\operatorname{Ad}_g\xi)=p(\xi)\,q(\xi)=(pq)(\xi)\qquad\text{(invariance of }p\text{ and of }q\text{),}$$
so $pq\in I^{d+e}(G)$; likewise a sum of two invariants of the same degree is invariant, and the constants are trivially invariant. Thus $I(G)$ is closed under the algebra operations, a graded subalgebra of $\operatorname{Sym}(\mathfrak{g}^*)$. It is this ring whose elements the Chern–Weil homomorphism sends to de Rham cohomology.

---

# Categorical / Structural Definition

There is a clean structural reading that unifies the two forms and names the object once and for all. The adjoint action of $G$ on $\mathfrak{g}$ induces, by transpose, an action on the dual $\mathfrak{g}^*$ (the coadjoint action $g\cdot\phi=\phi\circ\operatorname{Ad}_{g^{-1}}$), hence on the symmetric algebra $\operatorname{Sym}(\mathfrak{g}^*)$ — the algebra of polynomial functions on $\mathfrak{g}$ — by algebra automorphisms, $(g\cdot p)(\xi)=p(\operatorname{Ad}_{g^{-1}}\xi)$. A polynomial $p$ is $\operatorname{Ad}$-invariant exactly when it is a **fixed point** of this action, $g\cdot p=p$ for all $g$. Therefore
$$I(G)=\operatorname{Sym}(\mathfrak{g}^*)^{G},\qquad I^d(G)=\big(\operatorname{Sym}^d(\mathfrak{g}^*)\big)^{G},$$
the ring of $G$-invariants of the symmetric algebra of the coadjoint representation, graded piece by graded piece. The polarisation proposition then says that the two descriptions of a degree-$d$ invariant — as an invariant element of $\operatorname{Sym}^d(\mathfrak{g}^*)$ (a symmetric multilinear form fixed by $G$) and as an invariant homogeneous polynomial (a fixed function) — are the two names for the same invariant vector under the $G$-linear isomorphism $\operatorname{Sym}^d(\mathfrak{g}^*)\cong\{$homogeneous degree-$d$ polynomials$\}$; the isomorphism is $G$-equivariant precisely because of the invariance-transfer clause. In one sentence: **an $\operatorname{Ad}$-invariant polynomial is a $G$-fixed vector in the symmetric algebra of the coadjoint representation, viewed either as a symmetric tensor or as its associated polynomial function.** This is the frame in which classical invariant theory operates, and it is why the answer to "what are the invariant polynomials?" is a statement about a fixed subalgebra.

---

# Relate to Other Fields / Compression

The definition is the gauge-theoretic entry point into **classical invariant theory**, the nineteenth-century subject of polynomials unchanged by a group of linear substitutions. For a connected compact Lie group $G$ with maximal torus $T$ and Weyl group $W$, the Chevalley restriction theorem identifies $I(G)$ with the far smaller ring $\mathbb{K}[\mathfrak{t}]^{W}$ of Weyl-invariant polynomials on the Cartan subalgebra $\mathfrak{t}$ — invariance under the whole group is detected on the torus, modulo the finite Weyl symmetry. For the unitary group $U(r)$ this recovers the fact that $I(U(r))$ is the ring of symmetric polynomials in the $r$ eigenvalues, freely generated by the elementary symmetric functions; those generators are, up to the normalising constant $\tfrac{i}{2\pi}$, exactly the coefficients $c_1,\dots,c_r$ of the characteristic polynomial that appear below and produce the Chern classes. We do not prove Chevalley's theorem here — it belongs to Lie theory rather than gauge theory — but it is the structural reason the examples are as few and as familiar as they are.

**True name.** Officially an invariant polynomial is a function satisfying three axioms; operationally, for a classical matrix group, it is **a polynomial in the coefficients of the characteristic polynomial of $\xi$** — equivalently, a symmetric polynomial in the eigenvalues of $\xi$. This is the working characterisation one actually computes with: to write down an invariant of degree $d$ on $\mathfrak{gl}_n$ one either takes $\operatorname{tr}(\xi^d)$, the $d$-th power sum of the eigenvalues, or the elementary symmetric function $\sigma_d(\text{eigenvalues})$, the degree-$d$ coefficient of $\det(\lambda\mathbf{1}+\xi)$; Newton's identities convert between the two families. Every invariant is a polynomial combination of these because conjugation can bring $\xi$ to (block) triangular form without changing the value, so the value depends only on the diagonal spectrum, symmetrically. The single most compressed way to hold the definition: **invariant polynomials are the spectral functions of $\xi$ that happen to be polynomial.**

---

# Examples / Corollaries

Every example below is verified against the three defining conditions; the two non-examples are shown to fail a specific condition against an explicit witness.

**Is an instance — the power trace $\operatorname{tr}(\xi^d)$ on $\mathfrak{gl}_n(\mathbb{K})$.** Define $p_d(\xi)=\operatorname{tr}(\xi^d)$ for $\xi\in\mathfrak{gl}_n(\mathbb{K})$ (all $n\times n$ matrices). We check the three conditions. *Polynomiality:* the entries of $\xi^d$ are homogeneous polynomials of degree $d$ in the entries $\xi_{ij}$ (a $d$-fold matrix product), and the trace is the linear form $\sum_k(\xi^d)_{kk}$, so $p_d$ is a homogeneous polynomial of degree $d$ in the coordinates. *Homogeneity:* $p_d(c\xi)=\operatorname{tr}((c\xi)^d)=c^d\operatorname{tr}(\xi^d)=c^dp_d(\xi)$. *Invariance:* for the matrix group $GL(n;\mathbb{K})$, $\operatorname{Ad}_g\xi=g\xi g^{-1}$, so $(\operatorname{Ad}_g\xi)^d=(g\xi g^{-1})^d=g\xi^dg^{-1}$ (the inner factors $g^{-1}g$ telescope), whence
$$p_d(\operatorname{Ad}_g\xi)=\operatorname{tr}(g\xi^dg^{-1})=\operatorname{tr}(\xi^d)=p_d(\xi)\qquad\text{(cyclic invariance of the trace, }\operatorname{tr}(ABA^{-1})=\operatorname{tr}B\text{).}$$
All three hold, so $\operatorname{tr}(\xi^d)\in I^d(GL(n;\mathbb{K}))$. Its polar form is $p_d(\xi_1,\dots,\xi_d)=\tfrac{1}{d!}\sum_{\sigma\in S_d}\operatorname{tr}(\xi_{\sigma(1)}\cdots\xi_{\sigma(d)})$, the symmetrised trace of a product (its diagonal is $\operatorname{tr}(\xi^d)$ because all $d!$ orderings of $d$ equal factors coincide).

**Is an instance — the real normalisation $i^d\operatorname{tr}(\xi^d)$ on $\mathfrak{u}(n)$.** Restrict attention to $\mathfrak{g}=\mathfrak{u}(n)$, the skew-Hermitian matrices ($\xi^*=-\xi$). The $\mathbb{C}$-valued polynomial $\operatorname{tr}(\xi^d)$ is still invariant and homogeneous of degree $d$ by the previous verification (which used only $\operatorname{Ad}_g\xi=g\xi g^{-1}$, valid for $g\in U(n)$). To obtain a **real-valued** invariant — the corrected form of Haydys's Example 81(a), whose printed $i\operatorname{tr}\xi^d$ is real only for $d=1$ — multiply by the constant $i^d$ and set $q_d(\xi):=i^d\operatorname{tr}(\xi^d)$. Multiplying by a fixed scalar preserves all three conditions, so $q_d$ is an invariant homogeneous polynomial of degree $d$; the point is that it takes values in $\mathbb{R}$. Indeed, $\xi$ skew-Hermitian means $i\xi$ is Hermitian ($(i\xi)^*=-i\xi^*=i\xi$), hence $i\xi$ is diagonalisable with **real** eigenvalues $\mu_1,\dots,\mu_n\in\mathbb{R}$; therefore
$$q_d(\xi)=i^d\operatorname{tr}(\xi^d)=\operatorname{tr}\big((i\xi)^d\big)=\sum_{k=1}^n\mu_k^{\,d}\in\mathbb{R}\qquad\text{(}(i\xi)^d=i^d\xi^d\text{; trace = sum of eigenvalues, here of }(i\xi)^d\text{).}$$
So $q_d=i^d\operatorname{tr}(\xi^d)\in I^d(U(n))$ is real-valued, as required. (For $d=1$ this is $i\operatorname{tr}\xi$, matching the printed formula; for $d\ge2$ the exponent must be $i^d$, not $i$.)

**Is an instance — the Chern coefficients $c_j$ on $\mathfrak{u}(r)$.** Define homogeneous polynomials $c_1,\dots,c_r$ of degrees $1,\dots,r$ on $\mathfrak{u}(r)$ by expanding a determinant in $\lambda$:
$$\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)=\lambda^r+c_1(\xi)\,\lambda^{r-1}+\dots+c_r(\xi),\qquad\text{so}\quad c_j(\xi)=\Big(\tfrac{i}{2\pi}\Big)^{j}\sigma_j(\xi),$$
where $\sigma_j(\xi)$ is the sum of the $j\times j$ principal minors of $\xi$ (the degree-$j$ elementary symmetric function of the eigenvalues); in particular $c_1(\xi)=\tfrac{i}{2\pi}\operatorname{tr}\xi$ and $c_r(\xi)=\big(\tfrac{i}{2\pi}\big)^r\det\xi$. The normalising constant $\tfrac{i}{2\pi}$ is the series' Chern-class convention $c(E)=\det\!\big(1+\tfrac{i}{2\pi}F\big)$. We verify the three conditions for each $c_j$. *Polynomiality and homogeneity:* $\sigma_j$ is a homogeneous polynomial of degree $j$ in the entries of $\xi$ (a sum of $j\times j$ minors), so $c_j$ is homogeneous of degree $j$; equivalently, substituting $\xi\mapsto s\xi$ multiplies the $\lambda^{r-j}$-coefficient by $s^j$. *Invariance:* for $g\in U(r)$, multiplicativity of the determinant gives
$$\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\operatorname{Ad}_g\xi\Big)=\det\!\Big(g\big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\big)g^{-1}\Big)=\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)\qquad\text{(}\operatorname{Ad}_g\xi=g\xi g^{-1},\ \lambda\mathbf 1=g\lambda\mathbf 1g^{-1},\ \det(gAg^{-1})=\det A\text{),}$$
an identity of polynomials in $\lambda$; equating the coefficient of $\lambda^{r-j}$ on both sides yields $c_j(\operatorname{Ad}_g\xi)=c_j(\xi)$. So each $c_j\in I^j(U(r))$ (over $\mathbb{C}$). *Real-valuedness (Haydys's conjugation argument, written in full):* for $\xi\in\mathfrak{u}(r)$ skew-Hermitian, $\overline{\xi}=-\xi^{\mathsf T}$ (conjugate of $\xi^*=\overline{\xi}^{\mathsf T}=-\xi$), so for any $\lambda\in\mathbb{C}$,
$$\overline{\det\!\Big(\bar\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big)}=\det\!\Big(\lambda\mathbf{1}+\overline{\tfrac{i}{2\pi}\xi}\Big)=\det\!\Big(\lambda\mathbf{1}-\tfrac{i}{2\pi}\overline{\xi}\Big)=\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi^{\mathsf T}\Big)=\det\!\Big(\lambda\mathbf{1}+\tfrac{i}{2\pi}\xi\Big),$$
using in turn $\overline{\det M}=\det\overline{M}$ and $\overline{\bar\lambda}=\lambda$; the reality $\overline{i/2\pi}=-i/2\pi$; the identity $\overline{\xi}=-\xi^{\mathsf T}$; and $\det(A^{\mathsf T})=\det A$ with $A=\lambda\mathbf 1+\tfrac{i}{2\pi}\xi$. Now expand both ends as polynomials in $\lambda$: the right end is $\lambda^r+\sum_j c_j(\xi)\lambda^{r-j}$, while the left end is $\overline{\bar\lambda^r+\sum_j c_j(\xi)\bar\lambda^{r-j}}=\lambda^r+\sum_j\overline{c_j(\xi)}\,\lambda^{r-j}$. Equating the coefficient of $\lambda^{r-j}$ gives $\overline{c_j(\xi)}=c_j(\xi)$, so $c_j(\xi)\in\mathbb{R}$. Hence each $c_j$ is a real-valued $\operatorname{Ad}$-invariant homogeneous polynomial on $\mathfrak{u}(r)$; these are the polynomials whose Chern–Weil forms are the Chern classes (see [[Def - Chern Classes]]).

**Is an instance — the determinant $\det$ on $\mathfrak{gl}_n$.** The determinant $\xi\mapsto\det\xi$ is a homogeneous polynomial of degree $n$ (the Leibniz expansion $\det\xi=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_k\xi_{k\sigma(k)}$ is a sum of degree-$n$ monomials), it is homogeneous ($\det(c\xi)=c^n\det\xi$), and it is invariant ($\det(g\xi g^{-1})=\det\xi$ by multiplicativity). So $\det\in I^n(GL(n;\mathbb{K}))$. It is the top coefficient of the characteristic polynomial and, on $\mathfrak{u}(r)$, equals $(2\pi/i)^r c_r$ up to the normalising constant.

**Is NOT an instance — the entry functional $\xi\mapsto\xi_{11}$ on $\mathfrak{gl}_2$.** The function $q(\xi)=\xi_{11}$, the upper-left entry, is a homogeneous polynomial of degree $1$ and satisfies homogeneity ($q(c\xi)=c\,q(\xi)$), so it passes conditions (1) and (3). It **fails invariance**. Take the specific witness
$$\xi=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad g=\begin{pmatrix}0&1\\1&0\end{pmatrix}\in GL_2\quad(g^{-1}=g).$$
Then, computing the conjugate step by step,
$$\xi g^{-1}=\begin{pmatrix}1&0\\0&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad \operatorname{Ad}_g\xi=g\,(\xi g^{-1})=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\0&1\end{pmatrix}.$$
Hence $q(\operatorname{Ad}_g\xi)=(\operatorname{Ad}_g\xi)_{11}=0$, whereas $q(\xi)=\xi_{11}=1$. Since $0\ne1$, $q$ is not $\operatorname{Ad}$-invariant, and $q\notin I(GL_2)$. This is the algebraic form of the gluing failure described in the Axiom Motivation: an entry functional depends on the frame, so it cannot build a global form on the base. (The witness $g$ is even unitary, $g\in U(2)$, so $q$ fails invariance already for the compact group.)

**Is NOT an instance across a component change — the Pfaffian on $\mathfrak{so}(2m)$.** The Pfaffian $\operatorname{Pf}\colon\mathfrak{so}(2m)\to\mathbb{R}$ is a homogeneous polynomial of degree $m$ on the skew-symmetric matrices, characterised by $\operatorname{Pf}(\xi)^2=\det\xi$ and the congruence law $\operatorname{Pf}(A\xi A^{\mathsf T})=\det(A)\,\operatorname{Pf}(\xi)$ for $A\in GL_{2m}(\mathbb{R})$ (its defining algebraic property, established on [[Def - Pfaffian]]). For $A$ orthogonal, $A^{\mathsf T}=A^{-1}$, so $A\xi A^{\mathsf T}=A\xi A^{-1}=\operatorname{Ad}_A\xi$ and the congruence law becomes
$$\operatorname{Pf}(\operatorname{Ad}_A\xi)=\det(A)\,\operatorname{Pf}(\xi).$$
For $A\in SO(2m)$ we have $\det A=+1$, so $\operatorname{Pf}$ **is** invariant under $\operatorname{Ad}$ of the connected group $SO(2m)$: it is a genuine element of $I^m(SO(2m))$, and its Chern–Weil form is the Euler class ([[Def - Euler Class of an Oriented Vector Bundle]]). But for the larger group $O(2m)$, an orientation-reversing $A$ has $\det A=-1$, giving $\operatorname{Pf}(\operatorname{Ad}_A\xi)=-\operatorname{Pf}(\xi)\ne\operatorname{Pf}(\xi)$ (for $\xi$ with $\operatorname{Pf}(\xi)\ne0$); so $\operatorname{Pf}\notin I(O(2m))$. The definition's quantifier "for all $g\in G$" is therefore sensitive to which group one takes: the Pfaffian is the invariant that separates $SO(2m)$ from $O(2m)$, which is exactly why the Euler class of a real rank-$2m$ bundle requires an orientation. (This is a forward-looking non-example; the Pfaffian's properties are developed on its own page.)

**Corollary — infinitesimal invariance $(83)$.** We prove the differentiated form of the invariance condition, which is the identity Haydys uses to show the Chern–Weil form is closed.

> **Corollary (infinitesimal invariance).** Let $p$ be an $\operatorname{Ad}$-invariant homogeneous polynomial of degree $d$ on the Lie algebra $\mathfrak{g}$ of a Lie group $G$, and let $p(\cdot,\dots,\cdot)$ denote its polar form. Then for all $\xi,\xi_1,\dots,\xi_d\in\mathfrak{g}$,
> $$\sum_{j=1}^{d}p\big(\xi_1,\dots,\xi_{j-1},[\xi,\xi_j],\xi_{j+1},\dots,\xi_d\big)=0.\tag{83}$$

> [!note]- Proof of the infinitesimal-invariance corollary
> **What is assumed and shown.** We assume $p$ is $\operatorname{Ad}$-invariant, so its polar form $\lambda:=p(\cdot,\dots,\cdot)$ is $\operatorname{Ad}$-invariant (invariance-transfer clause of the polarisation proposition). We must show $(83)$.
>
> **Step 1 — a one-parameter family of invariance equations.** For the fixed $\xi\in\mathfrak{g}$ and any $t\in\mathbb{R}$, take $g=\exp(t\xi)\in G$. Invariance of $\lambda$ at this group element reads
> $$\lambda\big(\operatorname{Ad}_{\exp t\xi}\xi_1,\dots,\operatorname{Ad}_{\exp t\xi}\xi_d\big)=\lambda(\xi_1,\dots,\xi_d)\qquad\text{for all }t\in\mathbb{R}.$$
> The right-hand side is independent of $t$.
>
> **Step 2 — differentiate at $t=0$.** The map $t\mapsto\operatorname{Ad}_{\exp t\xi}\xi_j$ is smooth with derivative at $t=0$
> $$\frac{d}{dt}\Big|_{t=0}\operatorname{Ad}_{\exp t\xi}\xi_j=\operatorname{ad}_\xi\xi_j=[\xi,\xi_j],$$
> which is part (iii) of [[Thm - Ad is a Smooth Representation and its Differential is ad]] (the differential of the adjoint representation is $\operatorname{ad}$; for a matrix group this reads $\tfrac{d}{dt}\big|_0 e^{t\xi}\xi_j e^{-t\xi}=[\xi,\xi_j]$). Since $\lambda$ is a multilinear form, it is a polynomial in the entries of its arguments, hence smooth, and the chain rule together with the product rule for multilinear maps gives
> $$\frac{d}{dt}\Big|_{t=0}\lambda\big(\operatorname{Ad}_{\exp t\xi}\xi_1,\dots,\operatorname{Ad}_{\exp t\xi}\xi_d\big)=\sum_{j=1}^{d}\lambda\Big(\xi_1,\dots,\underbrace{\tfrac{d}{dt}\big|_0\operatorname{Ad}_{\exp t\xi}\xi_j}_{=[\xi,\xi_j]},\dots,\xi_d\Big)=\sum_{j=1}^{d}\lambda(\xi_1,\dots,[\xi,\xi_j],\dots,\xi_d),$$
> where each summand differentiates one slot and evaluates the others at $t=0$ (where $\operatorname{Ad}_{\exp0\cdot\xi}=\operatorname{Ad}_e=\mathrm{id}$, so the undifferentiated slots hold $\xi_j$).
>
> **Step 3 — conclude.** The derivative of the constant right-hand side is $0$. Equating, $\sum_{j}\lambda(\xi_1,\dots,[\xi,\xi_j],\dots,\xi_d)=0$, which is $(83)$ since $\lambda=p(\cdot,\dots,\cdot)$. This holds for every $\xi,\xi_1,\dots,\xi_d\in\mathfrak{g}$. $\blacksquare$
>
> **Remark.** Connectedness of $G$ is not needed here: differentiation only samples $g=\exp(t\xi)$, which lies in $G$ for every group. Connectedness enters in the converse below, where infinitesimal invariance must be integrated back up to invariance under *all* of $G$.

**Corollary — the converse, for connected $G$.** For a connected group the differentiated condition $(83)$ is not merely necessary but sufficient: a symmetric form satisfying it is already invariant.

> **Corollary (integration, connected case).** Let $G$ be **connected** with Lie algebra $\mathfrak{g}$, and let $\lambda\in\operatorname{Sym}^d(\mathfrak{g}^*)$ satisfy the infinitesimal invariance $\sum_j\lambda(\xi_1,\dots,[\xi,\xi_j],\dots,\xi_d)=0$ for all $\xi,\xi_1,\dots,\xi_d\in\mathfrak{g}$. Then $\lambda$ is $\operatorname{Ad}$-invariant, and its diagonal $p$ is an $\operatorname{Ad}$-invariant homogeneous polynomial.

> [!note]- Proof of the converse (connected case)
> **What is assumed and shown.** We assume $G$ connected and $\lambda$ symmetric $d$-linear satisfying $(83)$ for every tuple. We show $\lambda(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)=\lambda(\xi_1,\dots,\xi_d)$ for all $g\in G$.
>
> **Step 1 — invariance along one-parameter subgroups.** Fix $\xi,\xi_1,\dots,\xi_d\in\mathfrak{g}$ and define $\eta_j(t):=\operatorname{Ad}_{\exp t\xi}\xi_j$ and $\phi(t):=\lambda(\eta_1(t),\dots,\eta_d(t))$. We compute $\phi'(t)$. First,
> $$\eta_j'(t)=\frac{d}{ds}\Big|_{s=0}\operatorname{Ad}_{\exp(t+s)\xi}\xi_j=\frac{d}{ds}\Big|_{s=0}\operatorname{Ad}_{\exp t\xi}\operatorname{Ad}_{\exp s\xi}\xi_j=\operatorname{Ad}_{\exp t\xi}[\xi,\xi_j]\qquad\text{(}\operatorname{Ad}\text{ a homomorphism; part (iii) of the Ad theorem),}$$
> and since $\operatorname{Ad}_g$ is a Lie-algebra automorphism — for a matrix group $\operatorname{Ad}_g[\alpha,\beta]=g[\alpha,\beta]g^{-1}=[g\alpha g^{-1},g\beta g^{-1}]=[\operatorname{Ad}_g\alpha,\operatorname{Ad}_g\beta]$ — and $\operatorname{Ad}_{\exp t\xi}\xi=\xi$ (because $\xi$ commutes with $\exp t\xi$), we get
> $$\eta_j'(t)=[\operatorname{Ad}_{\exp t\xi}\xi,\operatorname{Ad}_{\exp t\xi}\xi_j]=[\xi,\eta_j(t)].$$
> By the product rule for the multilinear $\lambda$,
> $$\phi'(t)=\sum_{j=1}^{d}\lambda\big(\eta_1(t),\dots,\eta_j'(t),\dots,\eta_d(t)\big)=\sum_{j=1}^{d}\lambda\big(\eta_1(t),\dots,[\xi,\eta_j(t)],\dots,\eta_d(t)\big)=0,$$
> the last equality by the hypothesis $(83)$ applied to the tuple $(\xi;\eta_1(t),\dots,\eta_d(t))$ — which is legitimate because $(83)$ is assumed for *all* tuples of algebra elements, and $\eta_1(t),\dots,\eta_d(t)\in\mathfrak{g}$. Hence $\phi$ is constant, so $\phi(t)=\phi(0)=\lambda(\xi_1,\dots,\xi_d)$; that is,
> $$\lambda(\operatorname{Ad}_{\exp t\xi}\xi_1,\dots,\operatorname{Ad}_{\exp t\xi}\xi_d)=\lambda(\xi_1,\dots,\xi_d)\qquad\text{for all }t\in\mathbb{R},\ \xi\in\mathfrak{g}.$$
> Setting $t=1$: $\lambda$ is invariant under $\operatorname{Ad}_g$ for every $g\in\exp(\mathfrak{g})$, the image of the exponential map.
>
> **Step 2 — from the exponential image to all of $G$.** The exponential map is a local diffeomorphism at $0\in\mathfrak{g}$ ([[Thm - The Exponential Map is a Local Diffeomorphism at the Origin]]), so $\exp(\mathfrak{g})$ contains an open neighbourhood $U$ of the identity $e\in G$. In a **connected** topological group the subgroup $\langle U\rangle$ generated by any neighbourhood of $e$ is all of $G$: $\langle U\rangle$ is open (it is a union of translates $h\,U$, each open), and an open subgroup is also closed (its complement is a union of its cosets, each open), so $\langle U\rangle$ is a non-empty clopen subset of the connected space $G$, forcing $\langle U\rangle=G$. Hence every $g\in G$ is a finite product $g=g_1g_2\cdots g_k$ with each $g_\ell\in U\subseteq\exp(\mathfrak{g})$.
>
> **Step 3 — invariance is multiplicative.** Because $\operatorname{Ad}$ is a group homomorphism, $\operatorname{Ad}_g=\operatorname{Ad}_{g_1}\operatorname{Ad}_{g_2}\cdots\operatorname{Ad}_{g_k}$. Applying Step 1's invariance one factor at a time — first pushing $\operatorname{Ad}_{g_k}$ through $\lambda$, then $\operatorname{Ad}_{g_{k-1}}$, and so on, each $g_\ell$ lying in $\exp(\mathfrak{g})$ where invariance is known —
> $$\lambda(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)=\lambda\big(\operatorname{Ad}_{g_1}\!\cdots\operatorname{Ad}_{g_k}\xi_1,\dots\big)=\dots=\lambda(\xi_1,\dots,\xi_d).$$
> Therefore $\lambda$ is $\operatorname{Ad}$-invariant, and its diagonal $p(\xi)=\lambda(\xi,\dots,\xi)$ is an $\operatorname{Ad}$-invariant homogeneous polynomial by the polarisation proposition. $\blacksquare$
>
> **Why connectedness is essential.** The Pfaffian non-example is the counterexample to dropping connectedness: on $\mathfrak{so}(2m)$ the Pfaffian satisfies $(83)$ (it is invariant under the connected group $SO(2m)$, hence infinitesimally invariant), yet it is not invariant under all of $O(2m)$. Infinitesimal invariance only sees the identity component; for a disconnected group there are genuinely more constraints in the finite condition than in the differentiated one.

**Calibration check.** First, on an **abelian** Lie group every homogeneous polynomial is invariant. Indeed, for $G$ abelian the conjugations $\alpha_g$ are all the identity, so $\operatorname{Ad}_g=d_e\alpha_g=\mathrm{id}_{\mathfrak{g}}$ for every $g$ (part (iv) of [[Thm - Ad is a Smooth Representation and its Differential is ad]]); hence $p(\operatorname{Ad}_g\xi)=p(\xi)$ holds automatically for any $p$, and $I(G)=\operatorname{Sym}(\mathfrak{g}^*)$ is the *entire* polynomial ring. For $G=U(1)$, with $\mathfrak{u}(1)=i\mathbb{R}$, this says every $p(\xi)=c\,\xi^d$ is invariant — consistent with the fact that a $U(1)$-connection's Chern–Weil forms use the single generator $\xi\mapsto\xi$ and its powers. Second, at the opposite extreme, $I(SU(2))=\mathbb{K}[\det]$ is a polynomial ring on one generator: because the adjoint action of $SU(2)$ on $\mathfrak{su}(2)\cong\mathbb{R}^3$ is by rotations (it is the double cover $SU(2)\to SO(3)$), an invariant polynomial is a polynomial in the squared length $|\xi|^2$, and for traceless $2\times2$ skew-Hermitian $\xi$ the characteristic polynomial is $\lambda^2+\det\xi$ with $\det\xi=-\tfrac12\operatorname{tr}(\xi^2)=\tfrac12|\xi|^2\ge0$, so $\det$ is the single generator. We state this as an exercise-level claim: the full proof — that every $\operatorname{Ad}_{SU(2)}$-invariant polynomial is a polynomial in $\det$ — is carried out in the exercise on the characteristic polynomial of $\mathfrak{su}(2)$. A reader who can verify the abelian calibration and can see why $\det$ generates on $\mathfrak{su}(2)$ has understood both the definition and the role of the group.

---

# Unlocked by This

> [!tip] Chern–Weil form *(from this chapter)*
> Feeding the curvature $F_a$ of a connection into an invariant polynomial produces the closed form $p(F_a)\in\Omega^{2d}(M)$, the **[[Def - Chern-Weil Form of an Invariant Polynomial|Chern–Weil form]]**. Invariance is exactly what makes the local expressions glue and descend to the base; homogeneity of degree $d$ is exactly what puts the output in degree $2d$. This is the construction the entire chapter is built to run.

> [!tip] Chern, Pontryagin, and Euler classes *(from this chapter)*
> The specific invariants isolated above are the sources of the standard characteristic classes: the coefficients $c_j$ of $\det(1+\tfrac{i}{2\pi}\xi)$ give the **[[Def - Chern Classes|Chern classes]]**, the invariants of $O(n)$ give the **[[Def - Pontryagin Classes|Pontryagin classes]]**, and the Pfaffian on $\mathfrak{so}(2m)$ gives the **[[Def - Euler Class of an Oriented Vector Bundle|Euler class]]**. Each is the Chern–Weil form of one element of $I(G)$.

> [!tip] The ring structure and the Whitney formula *(from this chapter)*
> That $I(G)$ is a ring, not just a vector space, is what makes the total Chern class $c=1+c_1+\dots+c_r$ multiply under Whitney sums; the product in $I(G)$ becomes the cup product in cohomology under the **[[Thm - Chern-Weil Theorem|Chern–Weil theorem]]**. The algebra structure defined here is the algebraic skeleton of the characteristic-class calculus.
