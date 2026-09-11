---
type: definition
subject: gauge-theory
prereqs:
  - "Thm - Chern-Weil Theorem"
  - "Def - Chern-Weil Form of an Invariant Polynomial"
  - "Def - Ad-Invariant Polynomial"
  - "Def - Complex Vector Bundle and Hermitian Structure"
  - "Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group"
  - "Thm - Naturality and Isomorphism Invariance of Characteristic Classes"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Ex - Every Complex Vector Bundle Admits a Hermitian Structure"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold (compact whenever an integral over $M$ is taken), and $P \to M$ is a principal $U(r)$-bundle carrying a connection. We write $\omega \in \Omega^1(P; \mathfrak{u}(r))$ for the connection form on the total space, $A$ for a local connection potential $A = s^* \omega \in \Omega^1(U; \mathfrak{u}(r))$ of a local section $s$, and $F_A = dA + \tfrac12[A \wedge A]$ for the corresponding local curvature; for the matrix group $U(r)$ this is $F_A = dA + A \wedge A$, an $\mathfrak{u}(r)$-valued $2$-form, that is, a matrix whose entries are $2$-forms and which at each point is skew-Hermitian. The global curvature is a section $F \in \Omega^2(M; \operatorname{ad} P)$; we systematically write $F_A$ for its local matrix representative and evaluate invariant polynomials on it, as licensed by [[Def - Chern-Weil Form of an Invariant Polynomial|the Chern–Weil construction]]. The Lie algebra $\mathfrak{u}(r) = \{\xi \in \operatorname{Mat}(r \times r; \mathbb{C}) : \xi^* = -\xi\}$ is the skew-Hermitian matrices; $\mathfrak{su}(r) = \{\xi \in \mathfrak{u}(r) : \operatorname{tr} \xi = 0\}$; $\mathfrak{gl}_r(\mathbb{C}) = \operatorname{Mat}(r \times r; \mathbb{C})$. We write $\mathbf{1}$ for the $r \times r$ identity matrix, $\operatorname{tr}$ for the matrix [[Def - Trace|trace]] and $\det$ for the [[Def - Determinant|determinant]]. For a complex vector bundle $E \to M$ of rank $r$, a **Hermitian structure** $h$ is a smooth field of Hermitian inner products on the fibres (see [[Def - Complex Vector Bundle and Hermitian Structure]]), and $\operatorname{Fr}_U(E, h) \to M$ is its **unitary frame bundle**, the principal $U(r)$-bundle of $h$-orthonormal frames; $\operatorname{Fr}(E) \to M$ is the full frame bundle, a principal $GL_r(\mathbb{C})$-bundle. We write $H^k_{dR}(M)$ for de Rham cohomology with real coefficients (see [[Def - de Rham Cohomology]]) and $[\alpha]$ for the class of a closed form $\alpha$. The imaginary unit is $i$; $\pi = 3.14159\ldots$ is the circle constant.

This is a compound page: it defines four interlocking notions — the individual Chern classes $c_j(P)$ of a principal $U(r)$-bundle, the total Chern class $c(P)$, the Chern classes $c_j(E)$ of a complex vector bundle, and the standing normalisation $c(E) = \det(\mathbf{1} + \tfrac{i}{2\pi} F)$ — because they are one construction seen from four sides, and the content that makes the definition legitimate (independence of the connection, of the Hermitian structure, and of the chosen reduction of the structure group) can only be stated once all four are on the table.

> [!warning] Convention: the factor $\tfrac{i}{2\pi}$ versus $\tfrac{1}{2\pi i}$, and the sign of $c_2$
> The series normalises the total Chern class by
> $$c(E) = \Big[\det\!\Big(\mathbf{1} + \tfrac{i}{2\pi} F\Big)\Big],$$
> which is Haydys's convention (his Example 81(b)). Bär instead builds $c_1$ from the invariant polynomial $\lambda(\xi) = \tfrac{1}{2\pi i}\operatorname{tr}(\xi)$ and $c_n$ from $\tfrac{1}{(2\pi i)^n}$ (his Examples 2.5.11 and 2.5.13). Since $\tfrac{1}{2\pi i} = -\tfrac{i}{2\pi}$, the two conventions are related, degree by degree, by
> $$c_j^{\,\text{Bär}} = (-1)^j\, c_j^{\,\text{series}}, \qquad \text{because } \tfrac{1}{(2\pi i)^j} = (-1)^j\Big(\tfrac{i}{2\pi}\Big)^{j}.$$
> Thus the odd Chern classes ($c_1, c_3, \ldots$) flip sign between the two books and the even ones ($c_2, c_4, \ldots$) agree. The series follows Haydys, so that $\int_{\mathbb{CP}^1} c_1(\mathcal{O}(-1)) = -1$ for the tautological line bundle (the standard algebraic-geometry sign); Bär's convention would give $+1$. Every formula below is written in the series' convention; where Bär's differs, the recipe is: replace $\tfrac{i}{2\pi}$ by $\tfrac{1}{2\pi i}$ and multiply $c_j$ by $(-1)^j$.
>
> One sign inside this page must be flagged. Expanding $\det(\mathbf{1} + \tfrac{i}{2\pi}F)$ (computed in **The Definition** below) gives
> $$c_2(F) = \frac{1}{8\pi^2}\big(\operatorname{tr}(F \wedge F) - \operatorname{tr} F \wedge \operatorname{tr} F\big),$$
> and hence, on an $SU(2)$-bundle where $\operatorname{tr} F = 0$, $c_2(P) = \big[\tfrac{1}{8\pi^2}\operatorname{tr}(F_A \wedge F_A)\big]$. This is the sign the series uses, and it agrees with Haydys's Remark 93 and equation (94). (A draft of the manifest printed the opposite intermediate sign $\tfrac{1}{8\pi^2}(\operatorname{tr}F\wedge\operatorname{tr}F - \operatorname{tr}(F\wedge F))$; that would force $c_2 = -\tfrac{1}{8\pi^2}\operatorname{tr}(F\wedge F)$ on $SU(2)$, contradicting (94), and is corrected here.) Because $c_2$ is an even class, this formula is the same in Bär's convention as in the series'.

---

# Axiom Motivation

We already possess, from chapter III, topological Chern classes for the two special cases that geometry hands us most often: the first Chern class $c_1(P) = -f^* a$ of a principal $U(1)$-bundle, pulled back by its classifying map $f \colon M \to \mathbb{CP}^\infty$, and the second Chern class $c_2(P) = -f^* b$ of a principal $Sp(1) = SU(2)$-bundle, pulled back from $\mathbb{HP}^\infty$. Haydys's Remark 80 observes that these are the cases $r = 1$ and (via $SU(2)$) $j = 2$ of a family: for a principal $U(r)$-bundle one expects $r$ characteristic classes $c_1(P), \ldots, c_r(P)$ with $c_j(P)$ living in degree $2j$. The classifying-space construction gives integral classes but is homotopy-theoretic and computes nothing directly from the geometry of a connection. The question this page answers is: **can we manufacture all of $c_1, \ldots, c_r$ out of the curvature of any connection, in a way that is manifestly a differential-geometric invariant of the bundle, and that reproduces the topological classes we already have?**

The desiderata are sharp. We want a rule $P \mapsto (c_1(P), \ldots, c_r(P))$, with $c_j(P) \in H^{2j}_{dR}(M)$, that (a) is computed from the curvature $F_A$ of any connection $A$; (b) does not depend on which connection we chose; (c) is natural, $c(f^* P) = f^* c(P)$; (d) vanishes in positive degree on the trivial bundle; and (e) is normalised so that it agrees with the topological classes of chapter III. The [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] already delivers (a), (b), (c), and (d) for **any** $\operatorname{Ad}$-invariant polynomial $p$ on $\mathfrak{u}(r)$: the form $p(F_A)$ is closed, its de Rham class $c_p(P) = [p(F_A)]$ is independent of the connection, natural, and zero on a bundle with a flat connection. So the entire design problem reduces to choosing the right polynomials, and to pinning down the normalisation constant that secures (e).

Why the specific polynomials $c_j$ defined by $\det(\lambda \mathbf{1} + \tfrac{i}{2\pi}\xi) = \lambda^r + c_1(\xi)\lambda^{r-1} + \cdots + c_r(\xi)$, and not, say, the power sums $\operatorname{tr}(\xi^j)$? Three clauses of the definition each earn their place, and dropping any one breaks something concrete.

First, **the determinant, not the individual traces.** The coefficients of the characteristic polynomial are the elementary symmetric functions of the eigenvalues, and they are exactly the invariants that behave multiplicatively under direct sums: for a block-diagonal curvature $F_1 \oplus F_2$ one has $\det(\mathbf{1} + \tfrac{i}{2\pi}(F_1 \oplus F_2)) = \det(\mathbf{1} + \tfrac{i}{2\pi}F_1)\det(\mathbf{1} + \tfrac{i}{2\pi}F_2)$, which is the Whitney sum formula $c(E_1 \oplus E_2) = c(E_1) \smile c(E_2)$ in embryo (proved on [[Thm - Axioms and Properties of Chern Classes]]). Had we packaged the invariants as the power sums $\operatorname{tr}(\xi^j)$, this product structure would be invisible: $\operatorname{tr}$ is additive on blocks, not multiplicative, so the "total" class would not be a unit and the Whitney formula would take an ugly logarithmic form. The determinant is the unique choice for which the total class is grouplike.

Second, **the factor $\tfrac{i}{2\pi}$.** The imaginary unit $i$ is present so that the classes are real. For $\xi \in \mathfrak{u}(r)$, skew-Hermitian, the eigenvalues of $\xi$ are purely imaginary, so those of $\tfrac{i}{2\pi}\xi$ are real; equivalently $\tfrac{i}{2\pi}\xi$ is Hermitian, hence has real characteristic polynomial, so each $c_j(\xi) \in \mathbb{R}$. Drop the $i$ and the polynomial $\det(\lambda\mathbf{1} + \tfrac{1}{2\pi}\xi)$ has non-real coefficients on $\mathfrak{u}(r)$: for $r = 1$, $\xi = it$ gives $c_1(\xi) = \tfrac{1}{2\pi}it$, imaginary, and the "first Chern class" would be an imaginary cohomology class, which is meaningless as an invariant. The $2\pi$ is the normalisation that makes periods integers rather than integer multiples of $2\pi$; drop it and the theorem "$\int_\Sigma c_1(L) \in \mathbb{Z}$" (the next section's theorem, [[Thm - First Chern Class of a Line Bundle from Curvature]]) would read "$\in 2\pi\mathbb{Z}$", and the correspondence with the topological, integer-valued classes of chapter III would fail — desideratum (e) would be lost.

Third, **the de Rham class, not the form.** We record $c_j(P) = [c_j(F_A)]$, the cohomology class, not the form $c_j(F_A)$ itself. Drop the brackets and the object depends on the connection: different connections give cohomologous but distinct forms (this is precisely the content of part (ii) of the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]]). A curvature form is a geometric datum of a particular connection; only its class is a topological invariant of the bundle. Forgetting to pass to cohomology would produce a "Chern class" that changes when we move the connection, and hence detects nothing about $P$ alone.

Finally, a word on **why a complex bundle at all.** The polynomials $c_j$ live on $\mathfrak{u}(r)$ (or $\mathfrak{gl}_r(\mathbb{C})$); they use the complex structure of the fibres. A real vector bundle has structure group $GL_n(\mathbb{R})$, on whose Lie algebra $\det(\lambda\mathbf{1} + \tfrac{i}{2\pi}\xi)$ is not naturally $\operatorname{Ad}$-invariant in a way that produces real classes, and there is no canonical reduction to $U(r)$. This is not a defect to be strengthened away; it is the statement that Chern classes are invariants of complex, not merely real, bundles — the real analogue is the theory of [[Def - Pontryagin Classes|Pontryagin classes]], built from the even Chern classes of the complexification $E_{\mathbb{R}} \otimes \mathbb{C}$ (which is canonically a complex bundle) via $p_k(E_{\mathbb{R}}) = (-1)^k c_{2k}(E_{\mathbb{R}} \otimes \mathbb{C})$. A reader who has internalised the three clauses above could reconstruct the definition unaided: take the curvature, make it Hermitian with $\tfrac{i}{2\pi}$, read off the coefficients of its characteristic polynomial, and pass to cohomology.

---

# The Definition

We give the principal-bundle version first, then transfer it to complex vector bundles, then prove the transfer is legitimate.

## The Chern polynomials

For $\xi \in \mathfrak{u}(r)$ define the polynomials $c_1, \ldots, c_r$, with $c_j$ homogeneous of degree $j$, by expanding the characteristic polynomial of $\tfrac{i}{2\pi}\xi$:
$$\det\!\Big(\lambda \mathbf{1} + \tfrac{i}{2\pi}\xi\Big) = \lambda^r + c_1(\xi)\,\lambda^{r-1} + \cdots + c_r(\xi), \qquad \lambda \in \mathbb{R}.$$
Setting $\lambda = 1$ gives the generating identity we use constantly:
$$\det\!\Big(\mathbf{1} + \tfrac{i}{2\pi}\xi\Big) = 1 + c_1(\xi) + \cdots + c_r(\xi). \tag{$\star$}$$
Each $c_j$ is an $\operatorname{Ad}$-invariant homogeneous polynomial of degree $j$ on $\mathfrak{u}(r)$ (indeed on $\mathfrak{gl}_r(\mathbb{C})$), and is real-valued on $\mathfrak{u}(r)$; this is verified on [[Def - Ad-Invariant Polynomial]] and drilled in [[Ex - The Coefficients of the Characteristic Polynomial are Ad-Invariant]], but the argument is short enough to give here.

> [!note]- Verification that $c_j \in I(U(r))$ and is real on $\mathfrak{u}(r)$
> **$\operatorname{Ad}$-invariance.** For $g \in U(r)$ and $\xi \in \mathfrak{u}(r)$, $\operatorname{Ad}_g \xi = g\xi g^{-1}$, and
> $$\det\!\Big(\lambda\mathbf{1} + \tfrac{i}{2\pi} g\xi g^{-1}\Big) = \det\!\Big(g\big(\lambda\mathbf{1} + \tfrac{i}{2\pi}\xi\big)g^{-1}\Big) = \det(g)\det\!\Big(\lambda\mathbf{1} + \tfrac{i}{2\pi}\xi\Big)\det(g)^{-1} = \det\!\Big(\lambda\mathbf{1} + \tfrac{i}{2\pi}\xi\Big)$$
> (by [[Thm - Determinant is Multiplicative|multiplicativity of the determinant]], and $\det(g)\det(g)^{-1} = 1$). Matching coefficients of $\lambda^{r-j}$ gives $c_j(\operatorname{Ad}_g\xi) = c_j(\xi)$ for every $g$; the same computation works verbatim for $g \in GL_r(\mathbb{C})$, so in fact $c_j \in I(GL_r(\mathbb{C}))$.
>
> **Homogeneity.** Replacing $\xi$ by $t\xi$ ($t \in \mathbb{R}$) and $\lambda$ by $t\lambda$ multiplies the whole determinant by $t^r$, and comparing the coefficient of $(t\lambda)^{r-j}$ shows $c_j(t\xi) = t^j c_j(\xi)$, so $c_j$ is homogeneous of degree $j$.
>
> **Reality on $\mathfrak{u}(r)$.** If $\xi^* = -\xi$ then $\big(\tfrac{i}{2\pi}\xi\big)^* = -\tfrac{i}{2\pi}\xi^* = \tfrac{i}{2\pi}\xi$, so $\tfrac{i}{2\pi}\xi$ is Hermitian. A Hermitian matrix has real eigenvalues, hence a real characteristic polynomial; the $c_j(\xi)$ are (up to sign) its coefficients, so each $c_j(\xi) \in \mathbb{R}$. This is exactly why the factor $i$ appears.

## Chern classes of a principal $U(r)$-bundle

> **Definition (Chern classes of a principal bundle).** Let $P \to M$ be a principal $U(r)$-bundle with a connection $A$, and let $c_j$ be the degree-$j$ polynomial above. The **$j$-th Chern class** of $P$ is the de Rham class
> $$c_j(P) := [\,c_j(F_A)\,] \in H^{2j}_{dR}(M), \qquad j = 1, \ldots, r,$$
> where $c_j(F_A)$ is the Chern–Weil form of $c_j$ (its construction is [[Def - Chern-Weil Form of an Invariant Polynomial]]). With $c_0(P) := 1$, the **total Chern class** is
> $$c(P) := 1 + c_1(P) + \cdots + c_r(P) = \Big[\det\!\Big(\mathbf{1} + \tfrac{i}{2\pi} F_A\Big)\Big] \in \bigoplus_{j=0}^{r} H^{2j}_{dR}(M).$$

The two forms of the total class agree by ($\star$): expanding $\det(\mathbf{1} + \tfrac{i}{2\pi}F_A)$ into homogeneous pieces, the degree-$2j$ piece is exactly $c_j(F_A)$, because $c_j$ is homogeneous of degree $j$ in the matrix entries and each entry of $F_A$ is a $2$-form. (The determinant of a matrix whose entries are even-degree forms is well-defined because even forms commute, so the entries lie in the commutative ring $\Omega^{\mathrm{even}}(M)$; this and its multiplicativity are established in [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]].)

**Well-posedness (Step 0).** For the classes to be defined we need $c_j(F_A)$ closed with a connection-independent cohomology class. This is precisely the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]], which we restate at the point of use:

> **Theorem (Chern–Weil).** For a principal $G$-bundle $P \to M$ with connection $\omega$ and $p \in I(G)$ of degree $d$: (i) the Chern–Weil form $p(F_\omega) \in \Omega^{2d}(M)$ is closed; (ii) for two connections $\omega_0, \omega_1$ the difference $p(F_{\omega_1}) - p(F_{\omega_0})$ is exact. Hence $c_p(P) := [p(F_\omega)] \in H^{2d}_{dR}(M)$ is independent of the connection, and $p \mapsto c_p(P)$ is a ring homomorphism $I(G) \to H^{\mathrm{even}}_{dR}(M)$.

Applying part (i) with $G = U(r)$ and $p = c_j$ shows $c_j(F_A)$ is closed; part (ii) shows $[c_j(F_A)]$ does not depend on $A$. So $c_j(P)$ is well-defined. A connection exists on every principal bundle ([[Thm - Existence of Connections on Principal Bundles|existence of connections]]), so the definition is never vacuous.

## Chern classes of a complex vector bundle

> **Definition (Chern classes of a complex vector bundle).** Let $E \to M$ be a complex vector bundle of rank $r$. Choose a Hermitian structure $h$ on $E$ — one exists by [[Ex - Every Complex Vector Bundle Admits a Hermitian Structure|a partition-of-unity argument]] — and form the unitary frame bundle $\operatorname{Fr}_U(E, h)$, a principal $U(r)$-bundle (this is the reduction of the structure group described in [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group]]). Set
> $$c_j(E) := c_j\big(\operatorname{Fr}_U(E, h)\big), \qquad c(E) := c\big(\operatorname{Fr}_U(E, h)\big).$$

For this to define an invariant of $E$ we must show it does not depend on the Hermitian structure $h$. We prove this now, in full.

> [!note]- Independence of the Hermitian structure — complete proof
> **Claim.** If $h_0, h_1$ are two Hermitian structures on $E$, then $c_j(\operatorname{Fr}_U(E, h_0)) = c_j(\operatorname{Fr}_U(E, h_1))$ for every $j$.
>
> We use two results, restated here:
>
> > **Theorem (homotopic maps pull back isomorphic bundles).** If $f_0, f_1 \colon N \to M$ are smooth homotopic maps and $Q \to M$ is a principal $G$-bundle, then the pullbacks $f_0^* Q$ and $f_1^* Q$ are isomorphic principal $G$-bundles over $N$. (Proof: [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles]].)
>
> > **Theorem (isomorphism invariance of characteristic classes).** If $\phi \colon Q \to Q'$ is an isomorphism of principal $G$-bundles over $M$, then $c_p(Q) = c_p(Q')$ for every $p \in I(G)$; in particular $c_p(Q)$ depends only on the isomorphism class of $Q$. (Proof: [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]].)
>
> **Step 0 (the segment of Hermitian structures is contained in the Hermitian structures).** For $t \in [0,1]$ set $h_t := (1 - t)h_0 + t h_1$. At each point $m \in M$ and each fibre $E_m$, the form $h_t|_{E_m}(v, w) = (1-t)h_0(v,w) + t h_1(v,w)$ is sesquilinear and Hermitian-symmetric, being a real-linear combination of two such forms. It is positive-definite: for $v \neq 0$,
> $$h_t(v, v) = (1-t)\,h_0(v,v) + t\,h_1(v,v) > 0 \qquad \text{(since } h_0(v,v) > 0,\ h_1(v,v) > 0,\ \text{and } 1-t, t \geq 0 \text{ are not both } 0\text{)}.$$
> So $h_t$ is a Hermitian structure on $E$ for every $t \in [0,1]$, and $(m, t) \mapsto h_t|_{E_m}$ is smooth.
>
> **Step 1 (a single bundle over $M \times [0,1]$).** Let $\pi_M \colon M \times [0,1] \to M$ be the projection and $\tilde{E} := \pi_M^* E$, a complex vector bundle of rank $r$ over $M \times [0,1]$ whose fibre over $(m, t)$ is $E_m$. Define a Hermitian structure $\tilde{h}$ on $\tilde{E}$ by $\tilde{h}_{(m,t)} := h_t|_{E_m}$; it is smooth by Step 0. Let $\tilde{P} := \operatorname{Fr}_U(\tilde{E}, \tilde{h})$, a principal $U(r)$-bundle over $M \times [0,1]$.
>
> **Step 2 (the endpoints recover the two frame bundles).** For $j \in \{0, 1\}$ let $\iota_j \colon M \to M \times [0,1]$, $\iota_j(m) = (m, j)$. Then $\iota_j^* \tilde{E} = E$ (pullback of a pullback along $\pi_M \circ \iota_j = \operatorname{id}_M$) and $\iota_j^* \tilde{h} = h_j$ (the fibre inner product at $(m, j)$ is $h_j|_{E_m}$). Taking unitary frame bundles commutes with pullback along any smooth map, because the fibre of $\iota_j^* \operatorname{Fr}_U(\tilde{E}, \tilde{h})$ over $m$ is by definition the fibre of $\operatorname{Fr}_U(\tilde{E}, \tilde{h})$ over $\iota_j(m) = (m,j)$, namely the set of $\tilde{h}_{(m,j)}$-orthonormal frames of $\tilde{E}_{(m,j)} = E_m$, and this is exactly the fibre of $\operatorname{Fr}_U(\iota_j^*\tilde{E}, \iota_j^*\tilde{h})$ over $m$ once the identifications $\iota_j^*\tilde{E} = E$ and $\iota_j^*\tilde{h} = h_j$ above are used; the identification is smooth because it is induced by the smooth bundle map covering $\iota_j$. Hence
> $$\iota_j^* \tilde{P} = \iota_j^* \operatorname{Fr}_U(\tilde{E}, \tilde{h}) = \operatorname{Fr}_U(\iota_j^* \tilde{E}, \iota_j^* \tilde{h}) = \operatorname{Fr}_U(E, h_j).$$
>
> **Step 3 ($\iota_0$ and $\iota_1$ are homotopic).** The map $G \colon M \times [0,1] \to M \times [0,1]$, $G(m, s) = (m, s)$, is smooth (it is the identity) and satisfies $G(\cdot, 0) = \iota_0$ and $G(\cdot, 1) = \iota_1$; regarding the second coordinate as the homotopy parameter, $G$ is a smooth homotopy from $\iota_0$ to $\iota_1$. Hence $\iota_0 \simeq \iota_1$.
>
> **Step 4 (combine).** By the homotopic-maps theorem applied to $\tilde{P}$ and the homotopic maps $\iota_0 \simeq \iota_1$,
> $$\operatorname{Fr}_U(E, h_0) = \iota_0^* \tilde{P} \cong \iota_1^* \tilde{P} = \operatorname{Fr}_U(E, h_1) \qquad \text{(by Steps 2 and 3)}.$$
> By the isomorphism-invariance theorem applied to $p = c_j$,
> $$c_j\big(\operatorname{Fr}_U(E, h_0)\big) = c_j\big(\operatorname{Fr}_U(E, h_1)\big).$$
> **Conclusion.** The Chern classes $c_j(E)$ are independent of the Hermitian structure, so the definition of $c_j(E)$ is legitimate. $\blacksquare$

## Independence of the reduction: the $GL_r(\mathbb{C})$ formulation

The construction can be freed from any Hermitian structure at all, which both re-proves the independence just shown and reveals that Chern classes are invariants of $E$ as a complex bundle, not of any auxiliary metric.

> [!note]- The Chern class equals $[c_j(F_\nabla)]$ for any connection on $E$ — complete proof
> **Claim.** Let $E \to M$ be a complex vector bundle of rank $r$ and $\nabla$ any connection on $E$ (equivalently, any connection on the full frame bundle $\operatorname{Fr}(E)$, a principal $GL_r(\mathbb{C})$-bundle), with curvature $F_\nabla \in \Omega^2(M; \operatorname{End} E)$. Then $c_j(E) = [c_j(F_\nabla)]$; in particular the right-hand side is independent of $\nabla$ and of any reduction of the structure group.
>
> **Step 1 ($c_j \in I(GL_r(\mathbb{C}))$).** By the verification above, $c_j$ is $\operatorname{Ad}(GL_r(\mathbb{C}))$-invariant and homogeneous of degree $j$ on $\mathfrak{gl}_r(\mathbb{C})$, so $c_j$ is a genuine invariant polynomial for the group $GL_r(\mathbb{C})$.
>
> **Step 2 (independence of $\nabla$).** Apply the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] (restated above) with $G = GL_r(\mathbb{C})$, the bundle $\operatorname{Fr}(E)$, and $p = c_j$: the form $c_j(F_\nabla)$ is closed and $[c_j(F_\nabla)]$ is independent of the connection $\nabla$. A connection exists (average local connections with a partition of unity), so this class is defined.
>
> **Step 3 (a unitary connection realises it).** Fix a Hermitian structure $h$ and a unitary connection $\nabla^h$ for $h$ (one exists: take any connection and project onto the $\mathfrak{u}(r)$-part in an orthonormal frame). Viewed on $\operatorname{Fr}_U(E, h)$ it is a $U(r)$-connection; viewed on $\operatorname{Fr}(E)$ it is a $GL_r(\mathbb{C})$-connection; either way it induces the same covariant derivative on $E$ and hence the same curvature $F_{\nabla^h} \in \Omega^2(M; \operatorname{End} E)$. The polynomial $c_j$ is the same in both readings, so the Chern–Weil form $c_j(F_{\nabla^h})$ is literally the same $2j$-form. Therefore
> $$c_j(E) = c_j\big(\operatorname{Fr}_U(E, h)\big) = [c_j(F_{\nabla^h})] \qquad \text{(definition, then the } U(r)\text{ reading)}.$$
>
> **Step 4 (combine).** By Step 2 the class $[c_j(F_\nabla)]$ is the same for every connection $\nabla$ on $\operatorname{Fr}(E)$, and by Step 3 one such connection (a unitary one) gives $c_j(E)$. Hence $c_j(E) = [c_j(F_\nabla)]$ for every $\nabla$. Since no Hermitian structure or reduction was used except to name one connection, $c_j(E)$ does not depend on any of these choices. $\blacksquare$

## Explicit low-degree formulas

Expanding ($\star$) in the entries of $\xi$ (or of the curvature matrix $F$) gives the two classes used most:
$$c_1(F) = \frac{i}{2\pi}\operatorname{tr}(F), \qquad c_2(F) = \frac{1}{8\pi^2}\big(\operatorname{tr}(F \wedge F) - \operatorname{tr} F \wedge \operatorname{tr} F\big),$$
and the top class is $c_r(F) = \det\!\big(\tfrac{i}{2\pi}F\big) = \big(\tfrac{i}{2\pi}\big)^r \det F$.

> [!note]- Derivation of $c_1$ and $c_2$
> Write $B = \tfrac{i}{2\pi}F$, a matrix of $2$-forms. The determinant $\det(\mathbf{1} + B)$ is the generating function of the elementary symmetric polynomials of the eigenvalues of $B$; its degree-$1$ and degree-$2$ homogeneous parts are $e_1(B) = \operatorname{tr}(B)$ and $e_2(B) = \tfrac12\big((\operatorname{tr} B)^2 - \operatorname{tr}(B^2)\big)$ (Newton's identity for the second elementary symmetric function). Hence, matching against ($\star$),
> $$c_1(F) = \operatorname{tr}(B) = \operatorname{tr}\!\Big(\tfrac{i}{2\pi}F\Big) = \frac{i}{2\pi}\operatorname{tr}(F) \qquad \text{(trace is linear)},$$
> $$c_2(F) = \tfrac12\big((\operatorname{tr} B)^2 - \operatorname{tr}(B^2)\big) = \tfrac12\Big(\tfrac{i}{2\pi}\Big)^2\big(\operatorname{tr}(F)\wedge\operatorname{tr}(F) - \operatorname{tr}(F\wedge F)\big) \qquad \text{(pulling out the scalar } \tfrac{i}{2\pi}\text{)}.$$
> Now $\big(\tfrac{i}{2\pi}\big)^2 = \tfrac{i^2}{4\pi^2} = -\tfrac{1}{4\pi^2}$, so
> $$c_2(F) = -\frac{1}{8\pi^2}\big(\operatorname{tr} F \wedge \operatorname{tr} F - \operatorname{tr}(F \wedge F)\big) = \frac{1}{8\pi^2}\big(\operatorname{tr}(F \wedge F) - \operatorname{tr} F \wedge \operatorname{tr} F\big).$$
> Here $\operatorname{tr}(F \wedge F) = \sum_{k,l} F_{kl} \wedge F_{lk}$ and $\operatorname{tr} F \wedge \operatorname{tr} F = (\sum_k F_{kk}) \wedge (\sum_l F_{ll})$; both are $4$-forms, and the manipulation is legal because the entries of $F$ are $2$-forms, which commute under $\wedge$.

**The $SU(r)$ case.** For a principal $SU(r)$-bundle the curvature is $\mathfrak{su}(r)$-valued, so $\operatorname{tr} F = 0$; consequently
$$c_1(P) = 0, \qquad c_2(P) = \Big[\frac{1}{8\pi^2}\operatorname{tr}(F_A \wedge F_A)\Big].$$
This is Haydys's equation (94), and it is the normalisation that defines the **instanton number** $k(P) = \int_M c_2(P)$ in chapter VI's Chern–Simons section. The passage from the determinant form to $\tfrac{1}{8\pi^2}\operatorname{tr}(F\wedge F)$ uses, for the rank-two case, the identity $\operatorname{tr}\xi^2 = -2\det\xi$ on $\mathfrak{su}(2)$, verified in the Examples below.

## Scope remark on integrality

The classes defined here live in de Rham cohomology $H^{2j}_{dR}(M)$, that is, in real cohomology. In fact each $c_j(P)$ is the image, under the natural map $H^{2j}(M; \mathbb{Z}) \to H^{2j}_{dR}(M)$, of an **integral** class; this is what justifies the name "class" and matches the classifying-space construction of chapter III. The series does **not** construct the integral lift $c_j \in H^{2j}(M; \mathbb{Z})$, because that requires singular cohomology, which becomes available only in chapter XII. What the series does prove is the integrality of periods in the two cases it needs: for $c_1$ over a closed oriented surface, $\tfrac{i}{2\pi}\int_\Sigma F_A \in \mathbb{Z}$ ([[Thm - First Chern Class of a Line Bundle from Curvature]]), and for $c_2$ over a closed oriented $4$-manifold, $\tfrac{1}{8\pi^2}\int_M \operatorname{tr}(F_A \wedge F_A) \in \mathbb{Z}$ (established in chapter VI's Chern–Simons material). The **classifying-space classification of bundles by integral characteristic classes** for a general compact structure group, and the integral cohomology rings of $\mathbb{CP}^\infty$ and $\mathbb{HP}^\infty$, are not proved and not used in this series.

---

# Categorical / Structural Definition

The total Chern class is best read as a **natural transformation**. Let $\mathbf{Man}$ be the category of smooth manifolds and $\mathbf{Vect}_{\mathbb{C}}(-)$ the functor sending $M$ to the set of isomorphism classes of complex vector bundles over $M$ and a smooth map $f \colon N \to M$ to pullback $f^* \colon \mathbf{Vect}_{\mathbb{C}}(M) \to \mathbf{Vect}_{\mathbb{C}}(N)$; let $H^{\mathrm{even}}_{dR}(-)^\times$ be the functor sending $M$ to the group of units of the ring $H^{\mathrm{even}}_{dR}(M)$ (with pullback on maps). Then
$$c \colon \mathbf{Vect}_{\mathbb{C}}(-) \longrightarrow H^{\mathrm{even}}_{dR}(-)^\times, \qquad E \longmapsto c(E),$$
is a natural transformation: $c(f^* E) = f^* c(E)$ (naturality, [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]), and $c$ carries the monoid $(\mathbf{Vect}_{\mathbb{C}}(M), \oplus)$ into the group $(H^{\mathrm{even}}_{dR}(M)^\times, \cdot)$ by the Whitney sum formula $c(E_1 \oplus E_2) = c(E_1) \smile c(E_2)$ ([[Thm - Axioms and Properties of Chern Classes]]). That $c(E)$ genuinely lands in the units is the calibration check at the end of Examples.

At the level of Lie algebras the same structure is the **Chern–Weil homomorphism**: the ring of invariant polynomials $I(U(r))$ maps to $H^{\mathrm{even}}_{dR}(M)$ by $p \mapsto [p(F_A)]$, a ring homomorphism natural in $M$ (part of the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]]). The Chern classes are the images of the distinguished generators $c_1, \ldots, c_r$ of $I(U(r))$ under this homomorphism. In this reading a Chern class is not "attached to a bundle" so much as it is the value on a bundle of a fixed universal recipe, exactly as a characteristic class ought to be (see [[Def - Characteristic Class]] for the general notion).

---

# Relate to Other Fields / Compression

**True name.** Officially $c_j(E)$ is the de Rham class of a curvature polynomial. Operationally, its true name is *an obstruction, measured by counting zeros of sections*. The top Chern class $c_r(E)$ is the Euler class of the underlying oriented real bundle and equals the class Poincaré-dual to the zero set of a generic smooth section of $E$: where the geometry of $E$ forces a section to vanish, and with what sign, is what $c_r$ records. For a line bundle ($r = 1$), $c_1(L)$ is the number of zeros of a generic section, counted with sign, i.e. the degree; its true name over a surface is the winding number of the transition function ([[Thm - First Chern Class of a Line Bundle from Curvature]]). This operational reading — Chern classes count the obstructions to trivialising a bundle by sections — is why they detect non-triviality and why $c(E) = 1$ signals (though does not by itself prove) triviality.

In **algebraic geometry** the first Chern class of a holomorphic line bundle is its divisor class in $\operatorname{Pic}(M)$, and the normalisation $\int_{\mathbb{CP}^1} c_1(\mathcal{O}(-1)) = -1$ (equivalently $\deg \mathcal{O}(1) = +1$) is the seed of the entire degree calculus of line bundles on projective varieties. In **index theory** the Chern character $\operatorname{ch}(E) = \operatorname{tr}\exp(\tfrac{i}{2\pi}F)$ — a universal power series in the $c_j$ — is the cohomological input to the Atiyah–Singer index theorem, and $c_2$ of an $SU(2)$-bundle over a $4$-manifold is the topological charge appearing in the index of the Dirac operator. In **gauge theory and physics**, $c_1$ is the magnetic charge of a $U(1)$ connection (Dirac's quantisation of magnetic monopoles is exactly the integrality of $\int_\Sigma c_1$), and $c_2(P) = k(P)$ is the instanton number that grades the Yang–Mills moduli space. In **differential geometry**, for a rank-two oriented real bundle with a compatible complex structure, $c_1$ coincides with the Euler class ([[Def - Euler Class of an Oriented Vector Bundle]]), so that $c_1(TS^2)[S^2] = \chi(S^2) = 2$ is the Gauss–Bonnet number.

The compression worth remembering: **Chern classes are the multiplicative invariants of complex bundles that curvature can see.** Everything about them — reality, connection-independence, naturality, the Whitney product — is forced once one asks for a real, additive-under-pullback, multiplicative-under-direct-sum invariant computed from $\tfrac{i}{2\pi}F$.

---

# Examples / Corollaries

**Is an instance — the trivial bundle, $c = 1$.** Let $\underline{\mathbb{C}}^r = M \times \mathbb{C}^r$ be the trivial rank-$r$ bundle. It carries the product connection $d$, which is flat: $F = 0$. Each $c_j$ ($j \geq 1$) is homogeneous of degree $j \geq 1$, so $c_j(0) = 0$, and the Chern–Weil form $c_j(F) = c_j(0) = 0$ pointwise. Hence $c_j(\underline{\mathbb{C}}^r) = [0] = 0$ for $j \geq 1$, and $c(\underline{\mathbb{C}}^r) = 1$. (Independently: $\det(\mathbf{1} + \tfrac{i}{2\pi}\cdot 0) = \det(\mathbf{1}) = 1$.) This is the vanishing of characteristic classes on trivial bundles, [[Thm - Trivial Bundles Have Vanishing Characteristic Classes|proved in general here]].

**Is an instance — a Hermitian line bundle, $c = 1 + c_1$.** Let $L \to M$ be a complex line bundle ($r = 1$) with Hermitian structure and unitary connection $A$; then $F_A$ is a single $2$-form valued in $\mathfrak{u}(1) = i\mathbb{R}$, that is, $F_A = i\beta$ for a real $2$-form $\beta$. The $1 \times 1$ determinant is $\det(1 + \tfrac{i}{2\pi}F_A) = 1 + \tfrac{i}{2\pi}F_A$, so
$$c(L) = 1 + c_1(L), \qquad c_1(L) = \Big[\tfrac{i}{2\pi}F_A\Big] = \Big[-\tfrac{1}{2\pi}\beta\Big] \in H^2_{dR}(M).$$
Every clause checks: $c_1(L)$ is real because $\tfrac{i}{2\pi}F_A = -\tfrac{1}{2\pi}\beta$ is a real $2$-form; $c_j(L) = 0$ for $j \geq 2$ because the determinant of a $1 \times 1$ matrix has no higher terms (equivalently $j > \operatorname{rk} L = 1$); and $c_1$ is closed and connection-independent by Chern–Weil. Its computation from a connection is drilled in [[Ex - The Chern-Weil Form of the Trace on a U(1)-Bundle is the Curvature]].

**Is an instance (the normalisation) — the tautological bundle $\mathcal{O}(-1) \to \mathbb{CP}^1$.** As a $U(1)$-bundle, $\mathcal{O}(-1)$ has $c(\mathcal{O}(-1)) = 1 + c_1(\mathcal{O}(-1))$, and the defining normalisation is
$$\int_{\mathbb{CP}^1} c_1(\mathcal{O}(-1)) = -1.$$
The structural part is verifiable here: $\mathcal{O}(-1)$ is a line bundle, so its total Chern class is $1 + c_1$, with $c_1(\mathcal{O}(-1)) = [\tfrac{i}{2\pi}F]$ for the curvature $F$ of the connection induced by the Hopf connection. The numerical value $-1$ is the content of the normalisation axiom, [[Thm - Axioms and Properties of Chern Classes|proved here]] via the curvature computation of [[Thm - First Chern Class of a Line Bundle from Curvature]], which shows $\tfrac{i}{2\pi}\int_{\mathbb{CP}^1} F = -1$; we point to that page rather than reproduce the Hopf-curvature calculation. This value is the entire reason the series adopts the $\tfrac{i}{2\pi}$ convention, and it fixes the sign of every downstream Chern number.

**Is an instance (verified in full) — $c_2$ of an $SU(2)$-bundle.** Let $P$ be a principal $SU(2)$-bundle with $\mathfrak{su}(2)$-valued curvature $F$. Then $\operatorname{tr} F = 0$, so from the explicit formula $c_2(F) = \tfrac{1}{8\pi^2}(\operatorname{tr}(F\wedge F) - \operatorname{tr} F \wedge \operatorname{tr} F) = \tfrac{1}{8\pi^2}\operatorname{tr}(F\wedge F)$. We verify this against the determinant form, using the pointwise identity $\operatorname{tr}\xi^2 = -2\det\xi$ on $\mathfrak{su}(2)$.

> [!note]- Verification of $\operatorname{tr}\xi^2 = -2\det\xi$ and hence $c_2 = \tfrac{1}{8\pi^2}\operatorname{tr}(F\wedge F)$
> **The matrix identity.** A general element of $\mathfrak{su}(2)$ (traceless, skew-Hermitian) is
> $$\xi = \begin{pmatrix} ia & b + ic \\ -b + ic & -ia \end{pmatrix}, \qquad a, b, c \in \mathbb{R}.$$
> Its determinant is
> $$\det\xi = (ia)(-ia) - (b + ic)(-b + ic) = a^2 - \big(-b^2 - c^2\big) = a^2 + b^2 + c^2 \qquad \text{(expanding } (b+ic)(-b+ic) = -b^2 + c^2 i^2 = -b^2 - c^2\text{)}.$$
> Being traceless with eigenvalues $\mu, -\mu$, we have $\det\xi = -\mu^2$, so $\mu^2 = -(a^2+b^2+c^2)$, and
> $$\operatorname{tr}\xi^2 = \mu^2 + (-\mu)^2 = 2\mu^2 = -2(a^2 + b^2 + c^2) = -2\det\xi.$$
> In particular $\operatorname{tr}\xi^2 = -2(a^2+b^2+c^2) \leq 0$, as it must be for a skew-Hermitian $\xi$.
>
> **Matching the two forms of $c_2$.** For $r = 2$ the top Chern polynomial is $c_2(\xi) = \big(\tfrac{i}{2\pi}\big)^2 \det\xi = -\tfrac{1}{4\pi^2}\det\xi$. Substituting $\det\xi = -\tfrac12\operatorname{tr}\xi^2$,
> $$c_2(\xi) = -\frac{1}{4\pi^2}\Big(-\tfrac12 \operatorname{tr}\xi^2\Big) = \frac{1}{8\pi^2}\operatorname{tr}\xi^2.$$
> Replacing the Lie-algebra element $\xi$ by the curvature $2$-form $F$ (so $\xi^2 \rightsquigarrow F \wedge F$) gives $c_2(F) = \tfrac{1}{8\pi^2}\operatorname{tr}(F\wedge F)$, matching the general formula once $\operatorname{tr} F = 0$. The two routes — expand $\det(\mathbf 1 + \tfrac{i}{2\pi}F)$ to second order, or evaluate the top coefficient $\det(\tfrac{i}{2\pi}F)$ — agree.

**Is NOT an instance — a real vector bundle has no Chern classes.** Let $E_{\mathbb{R}} \to M$ be a real vector bundle of rank $n$, with structure group $GL_n(\mathbb{R})$. The polynomials $c_j$ are defined on $\mathfrak{gl}_r(\mathbb{C})$ using the factor $\tfrac{i}{2\pi}$ and the complex structure of the fibres; there is no canonical way to feed a $\mathfrak{gl}_n(\mathbb{R})$-valued curvature into them and obtain a real, well-defined class. Concretely, "$\tfrac{i}{2\pi}\operatorname{tr}(F)$" for a real connection would be an imaginary $2$-form, and choosing a complex structure $J$ on $E_{\mathbb{R}}$ to reduce to $U(r)$ can be done in inequivalent ways (or not at all), giving different candidate classes — so "the Chern class of a real bundle" is not a function of $E_{\mathbb{R}}$ alone. The correct real analogue is [[Def - Pontryagin Classes|Pontryagin classes]], built from the even Chern classes of the complexification $E_{\mathbb{R}} \otimes \mathbb{C}$, which is canonically complex; there the odd terms vanish and $p_k(E_{\mathbb{R}}) = (-1)^k c_{2k}(E_{\mathbb{R}} \otimes \mathbb{C})$ is a genuine invariant of the real bundle.

**Calibration check.** First, $c_j(E) = 0$ for $j > \operatorname{rk} E = r$: the total class is $\det(\mathbf{1} + \tfrac{i}{2\pi}F)$, the determinant of an $r \times r$ matrix, a polynomial of degree $r$ in the entries, so its expansion ($\star$) has no term of degree $> r$; hence $c_j = 0$ for $j > r$. Second, $c(E)$ is a unit in $H^{\mathrm{even}}_{dR}(M)$: write $c(E) = 1 + n$ with $n = c_1(E) + \cdots + c_r(E)$ a sum of positive-degree classes. In the graded-commutative ring $H^{\mathrm{even}}_{dR}(M)$ any positive-degree element is nilpotent (a product of enough of them exceeds the dimension of $M$ and so vanishes), so $n^{N+1} = 0$ for $N = \lfloor \dim M / 2 \rfloor$, and $c(E)^{-1} = 1 - n + n^2 - \cdots + (-1)^N n^N$ is a finite, well-defined inverse. This unit structure is what makes the Whitney formula a statement about a group, and what lets one solve for the Chern classes of a quotient or sub-bundle. As a third check, on a Hermitian line bundle the two claims combine: $c(L) = 1 + c_1(L)$ with $c_1(L)$ nilpotent of order $\leq \lfloor \dim M/2\rfloor + 1$, so the multiplicative inverse of $c(L)$ is the finite geometric series
$$c(L)^{-1} = 1 - c_1(L) + c_1(L)^2 - \cdots + (-1)^N c_1(L)^N \qquad (N = \lfloor \dim M/2\rfloor).$$
This inverse is not, in general, the total Chern class of the dual bundle. From the dual rule $c_1(L^\vee) = -c_1(L)$ (proved on [[Thm - Axioms and Properties of Chern Classes]]) we get $c(L^\vee) = 1 - c_1(L)$, which equals $c(L)^{-1}$ only when $c_1(L)^2 = 0$ — for instance over a base of dimension at most two, where $c_1(L)^2 \in H^4_{dR}(M) = 0$. In general the two differ: by the Whitney formula $c(L)\smile c(L^\vee) = (1 + c_1(L))(1 - c_1(L)) = 1 - c_1(L)^2 = c(L \oplus L^\vee)$, which fails to be $1$ precisely when $c_1(L)^2 \neq 0$, consistently with the direct sum $L \oplus L^\vee$ being nontrivial there. The correct universal identity relating a bundle and its dual is the degreewise rule $c_j(E^\vee) = (-1)^j c_j(E)$, not the inversion of the total class.

---

# Unlocked by This

> [!tip] Axioms and Properties of Chern Classes *(from Gauge Theory VI)*
> With the definition in hand, [[Thm - Axioms and Properties of Chern Classes]] proves that $c$ is the natural, Whitney-multiplicative, normalised invariant: naturality, $c(E_1 \oplus E_2) = c(E_1) \smile c(E_2)$, $c(\mathcal{O}(-1)) = 1 - [\omega_1]$, the dual rule $c_j(E^\vee) = (-1)^j c_j(E)$, and the additivity $c_1(L_1 \otimes L_2) = c_1(L_1) + c_1(L_2)$.

> [!tip] First Chern Class of a Line Bundle from Curvature *(from Gauge Theory VI)*
> [[Thm - First Chern Class of a Line Bundle from Curvature]] identifies the Chern–Weil $c_1$ with the topological first Chern class of chapter III, proves the integrality $\tfrac{i}{2\pi}\int_\Sigma F_A \in \mathbb{Z}$, and shows $c_1$ is a complete invariant of line bundles over closed oriented surfaces.

> [!tip] The Euler Class *(from Gauge Theory VI)*
> [[Def - Euler Class of an Oriented Vector Bundle]] is the Pfaffian analogue for oriented real bundles; for an oriented rank-two bundle regarded as a Hermitian line bundle it coincides with $c_1$, and $e(TS^2)[S^2] = 2$.

> [!tip] Pontryagin Classes *(from Gauge Theory VI)*
> [[Def - Pontryagin Classes]] extends the theory to real bundles via the complexification, with $p_1(E) = -c_2(E \otimes \mathbb{C})$ and, for the real bundle underlying an $SU(2)$-bundle, $p_1 = -2c_2(P)$.

> [!tip] The Chern–Simons functional and the instanton number *(from Gauge Theory VI)*
> The Chern number $\int_M c_2(P) = k(P)$ of an $SU(2)$-bundle over a closed $4$-manifold is the topological charge whose transgression is the **Chern–Simons form** $\operatorname{cs}(A) = \operatorname{tr}(A \wedge dA + \tfrac23 A^{\wedge 3})$, the subject of §6.4.
