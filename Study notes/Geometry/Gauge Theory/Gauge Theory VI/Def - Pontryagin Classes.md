---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Chern Classes"
  - "Def - Constructions on Representations"
  - "Def - Euclidean Vector Bundle and Metric Connection"
  - "Def - Euler Class of an Oriented Vector Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold (smooth, Hausdorff, second countable) and $E \to M$ is a smooth **real** vector bundle of rank $n$. We write $\Gamma(E)$ for its smooth sections and $\Omega^p(M) = \Gamma(\Lambda^p T^*M)$ for the real-valued $p$-forms. The de Rham cohomology of $M$ is $H^\bullet_{dR}(M) = H^\bullet_{dR}(M; \mathbb{R})$, the cohomology of the complex $\big(\Omega^\bullet(M), d\big)$; it is defined and its ring structure (the cup product $[\alpha] \smile [\beta] = [\alpha \wedge \beta]$) developed on [[Def - de Rham Cohomology]]. Every characteristic class on this page is a **real** de Rham class, in keeping with the series convention that we work with de Rham classes and the proved integrality theorems rather than with singular cohomology until it is constructed in chapter XII.

The **complexification** of $E$ is the complex vector bundle
$$E \otimes \mathbb{C} = E \otimes_{\mathbb{R}} \underline{\mathbb{C}},$$
of complex rank $n$, whose fibre over $m \in M$ is the complexification $E_m \otimes_{\mathbb{R}} \mathbb{C}$ of the real fibre; the fibrewise complex structure and the conjugation construction are those of [[Def - Constructions on Representations]] applied to the transition functions of $E$. The **conjugate** of a complex bundle $V \to M$ is $\overline{V}$, the same underlying real bundle with the fibrewise scalar multiplication $z \cdot v := \bar z v$; on the level of transition functions $\overline{V}$ has the entrywise complex-conjugate cocycle.

For a complex bundle $V$ of rank $r$ we write $c(V) = 1 + c_1(V) + \dots + c_r(V) \in H^{\mathrm{even}}_{dR}(M)$ for its total Chern class, with $c_k(V) \in H^{2k}_{dR}(M)$, as defined on [[Def - Chern Classes]]. Our normalisation is the standing series convention: for a complex bundle with a unitary connection of curvature $F$,
$$c(V) = \Big[\det\!\Big(1 + \tfrac{i}{2\pi} F\Big)\Big],$$
the bracket denoting the de Rham class of a closed form. For a real bundle $E$ we write $F$ for the curvature $2$-form of a **metric connection** — a connection compatible with a fibre inner product, whose local curvature matrix is skew-symmetric, $F \in \Omega^2(U; \mathfrak{so}(n))$ — in an orthonormal local frame; the object and its existence are on [[Def - Euclidean Vector Bundle and Metric Connection]]. When $E$ is oriented of even rank $2m$ we write $e(E) \in H^{2m}_{dR}(M)$ for its Euler class, $e(E) = \big[\operatorname{Pf}\!\big(\tfrac{F}{2\pi}\big)\big]$ with $\operatorname{Pf}$ the Pfaffian, as on [[Def - Euler Class of an Oriented Vector Bundle]]. Matrix trace is $\operatorname{tr}$ ([[Def - Trace]]) and determinant is $\det$ ([[Def - Determinant]]); for a matrix $A = (A_{ij})$ whose entries are even-degree forms these are computed by the usual formulas, which make sense because even-degree forms commute under the wedge product ($\alpha \wedge \beta = \beta \wedge \alpha$ when $\deg\alpha, \deg\beta$ are even), a fact proved and used repeatedly on [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]].

> [!warning] Convention: the sign in the definition
> We adopt the Milnor–Stasheff sign $p_k(E) = (-1)^k c_{2k}(E \otimes \mathbb{C})$ (Milnor–Stasheff, *Characteristic Classes*, §15). Some authors define $\tilde p_k(E) = c_{2k}(E \otimes \mathbb{C})$ without the sign; the two are related by $\tilde p_k = (-1)^k p_k$. The sign is chosen precisely so that the total Pontryagin form of a metric connection is $\det\!\big(1 - \tfrac{F}{2\pi}\big)$ (proved below), which makes $p_1$ of a positively-curved bundle come out positive; concretely it makes $p_1$ of the tangent bundle of complex projective space positive. Kobayashi–Nomizu (*Foundations of Differential Geometry* II, Ch. XII §4) use the same sign convention.

---

# Axiom Motivation

The Chern classes of [[Def - Chern Classes]] are invariants of **complex** vector bundles: they are built from a curvature $F$ living in the complex Lie algebra $\mathfrak{gl}_n(\mathbb{C})$ through the invariant polynomial $\det\!\big(1 + \tfrac{i}{2\pi}F\big)$, and the factor of $i$ is what makes the resulting forms real and integral. A **real** vector bundle $E \to M$ has no complex structure, so this machine cannot be run on it directly. Yet real bundles are exactly what differential geometry hands us — the tangent bundle $TM$, the normal bundle of a submanifold, the bundle underlying an $SO(n)$- or $Sp(n)$-structure — and we want characteristic numbers for them: obstructions to triviality, terms in index formulas, the raw material of the signature theorem and of four-manifold topology. The question this definition answers is: **what is the right ring of real characteristic classes of a real vector bundle, and where does it come from?**

The desideratum is a family of classes $p_k(E) \in H^{4k}_{dR}(M)$ that (i) is natural under pullback, so that it is a genuine invariant of the isomorphism class of $E$; (ii) vanishes on trivial bundles, so that a nonzero value is a certificate of nontriviality; (iii) is multiplicative under Whitney sum in the sense $p(E_1 \oplus E_2) = p(E_1) \smile p(E_2)$, so that the classes of a bundle constrain the classes of its summands; and (iv) reduces to something we already understand — the Chern and Euler classes — whenever the real bundle carries extra structure. There is one construction that supplies all four for free, and it is forced on us by the observation that a real bundle *does* have a canonical complex bundle attached to it: its **complexification** $E \otimes \mathbb{C}$. The natural definition is therefore to import the Chern classes of $E \otimes \mathbb{C}$ and read off from them the invariants of $E$.

The one thing that must be checked before this can work is that the Chern classes of $E \otimes \mathbb{C}$ do not carry spurious information — information that depends on the (non-existent) complex structure of $E$ rather than on $E$ itself. Here the decisive structural fact appears: the complexification of a real bundle is isomorphic to its own conjugate,
$$E \otimes \mathbb{C} \;\cong\; \overline{E \otimes \mathbb{C}},$$
because the fibrewise map $v \otimes z \mapsto v \otimes \bar z$ is a bundle isomorphism $E \otimes \mathbb{C} \to \overline{E \otimes \mathbb{C}}$ that is complex-linear from the domain's structure to the conjugate structure. Complex conjugation acts on Chern classes by $c_k(\overline{V}) = (-1)^k c_k(V)$ (this is the dual-bundle computation, since for a unitary bundle $\overline{V} \cong V^*$; see the corollary below). Combining the two, $c_k(E \otimes \mathbb{C}) = (-1)^k c_k(E \otimes \mathbb{C})$, so every **odd** Chern class of $E \otimes \mathbb{C}$ is $2$-torsion, hence zero in real de Rham cohomology. The odd Chern classes are the spurious data; they vanish. Only the **even** Chern classes $c_{2k}(E \otimes \mathbb{C})$ survive, and these are the invariants of $E$ we keep. This is why Pontryagin classes are indexed by $k$ but live in degree $4k$: half the Chern degrees are gone.

What breaks if we drop, or alter, each clause of the definition? **If we tried to define $p_k(E)$ from an odd Chern class $c_{2k+1}(E \otimes \mathbb{C})$**, we would get nothing: those classes are zero in $H^\bullet_{dR}$ by the argument just given, so no real information would be captured — the degree $4k$ is not a choice but the only place the invariants can live. **If we dropped the sign $(-1)^k$** and set $\tilde p_k = c_{2k}(E \otimes \mathbb{C})$, we would still get a natural, Whitney-multiplicative family; the sign is a normalisation, not a structural necessity, but without it the clean Chern–Weil identity $p(E) = \big[\det\!\big(1 - \tfrac{F}{2\pi}\big)\big]$ (proved below) would instead read $\big[\det\!\big(1 + \tfrac{F}{2\pi}\big)\big]$ with alternating signs on the components, and the comparison with the Euler class $e(E)^2 = p_m(E)$ would carry a spurious sign in odd rank-halves. **If we used a bundle other than the complexification** — say we tried to extract real invariants from $E$ itself with a real invariant polynomial of the curvature — we would recover exactly the same classes: the real invariant polynomials of a skew matrix are generated by $\operatorname{tr}(F^{2k})$, and these are precisely what the even Chern classes of the complexification package (this is the content of the Chern–Weil formula below). Complexification is not an arbitrary device; it is the shortest route to the ring the curvature already generates.

A reader who has internalised the Chern classes could, from these remarks alone, invent the Pontryagin classes: take the only canonical complex bundle a real bundle owns, apply the invariants you already have, discard the half of them that the conjugation symmetry kills, and fix the sign so that the surviving invariant polynomial is the honest determinant $\det\!\big(1 - \tfrac{F}{2\pi}\big)$.

---

# The Definition

Let $E \to M$ be a smooth real vector bundle of rank $n$. For each integer $k \ge 1$ the **$k$-th Pontryagin class** of $E$ is the real de Rham cohomology class
$$p_k(E) \;:=\; (-1)^k\, c_{2k}(E \otimes \mathbb{C}) \;\in\; H^{4k}_{dR}(M),$$
where $c_{2k}(E \otimes \mathbb{C}) \in H^{4k}_{dR}(M)$ is the $2k$-th Chern class of the complexification of $E$ ([[Def - Chern Classes]]). We set $p_0(E) = 1 \in H^0_{dR}(M)$ and define the **total Pontryagin class**
$$p(E) \;=\; 1 + p_1(E) + p_2(E) + \dots \;\in\; H^{\mathrm{even}}_{dR}(M).$$
Because $c_j(E \otimes \mathbb{C}) = 0$ for $j > n$ (a complex bundle of rank $n$ has no Chern classes above $c_n$), $p_k(E) = 0$ for $2k > n$, so the sum is finite: $p_k$ can be nonzero only for $1 \le k \le \lfloor n/2 \rfloor$.

**Equivalent formulation (Chern–Weil).** Fix any metric connection on $E$ (one exists, and the class is independent of the choice; see [[Def - Euclidean Vector Bundle and Metric Connection]] and the Chern–Weil theorem restated below). Let $F \in \Omega^2(U; \mathfrak{so}(n))$ be its local curvature in an orthonormal frame. Then
$$p(E) \;=\; \Big[\det\!\Big(1 - \tfrac{1}{2\pi} F\Big)\Big], \qquad\text{so}\qquad p_k(E) \;=\; \Big[\big(\det\!\big(1 - \tfrac{1}{2\pi} F\big)\big)_{(4k)}\Big],$$
the subscript $(4k)$ selecting the degree-$4k$ component. In particular the odd-degree components (form-degrees $2, 6, 10, \dots$) of $\det\!\big(1 - \tfrac{1}{2\pi}F\big)$ vanish identically as forms, so the total Pontryagin form has components only in degrees $0, 4, 8, \dots$. The equivalence of the two formulations, and the vanishing of the intermediate degrees, are proved in the Examples / Corollaries section; the first component there computed is
$$p_1(E) \;=\; \Big[-\tfrac{1}{8\pi^2}\,\operatorname{tr}(F \wedge F)\Big].$$

The **smallest instance** to hold in mind is a rank-$2$ real bundle with a metric connection. Its curvature in an orthonormal frame is a single $2 \times 2$ skew matrix of $2$-forms, $F = \begin{pmatrix} 0 & \varphi \\ -\varphi & 0 \end{pmatrix}$ with $\varphi \in \Omega^2(U)$. Here $\operatorname{tr}(F \wedge F) = F_{11}\wedge F_{11} + F_{12}\wedge F_{21} + F_{21}\wedge F_{12} + F_{22}\wedge F_{22} = 2\,(\varphi \wedge(-\varphi)) = -2\,\varphi \wedge \varphi$, so $p_1(E) = \big[-\tfrac{1}{8\pi^2}(-2\,\varphi\wedge\varphi)\big] = \big[\tfrac{1}{4\pi^2}\varphi\wedge\varphi\big]$. But $\varphi$ is a $2$-form and $\varphi \wedge \varphi$ is a $4$-form, which forces $p_1(E) = 0$ unless $\dim M \ge 4$; over a surface a rank-$2$ bundle has no Pontryagin class, exactly as it should, since its only characteristic data is the Euler class in degree $2$.

---

# Categorical / Structural Definition

A **characteristic class** for real rank-$n$ bundles, valued in degree-$d$ real de Rham cohomology, is a natural transformation
$$\mathrm{Vect}^{\mathbb{R}}_n(-) \;\Longrightarrow\; H^d_{dR}(-;\mathbb{R})$$
between two contravariant functors on smooth manifolds: the functor $\mathrm{Vect}^{\mathbb{R}}_n$ sending $M$ to the set of isomorphism classes of real rank-$n$ bundles over $M$ and a smooth map $f\colon N \to M$ to the pullback $f^*$, and the de Rham functor $H^d_{dR}(-;\mathbb{R})$ with its own $f^*$. Concretely, "natural transformation" means: to every bundle $E \to M$ the class $p_k$ assigns $p_k(E) \in H^{4k}_{dR}(M)$, and for every smooth $f\colon N \to M$ the square
$$p_k(f^* E) \;=\; f^* p_k(E)$$
commutes. This is the categorical content of $p_k$: it is not merely a number attached to a bundle but a rule that respects pullback, and it is this respect for pullback that makes it an invariant of the homotopy type of the classifying map and hence of the bundle.

The Pontryagin classes acquire this structure for free from the Chern classes. Complexification is itself a natural operation, $f^*(E \otimes \mathbb{C}) = (f^* E) \otimes \mathbb{C}$ (the fibrewise complexification commutes with restriction along $f$), and the Chern classes are natural by construction. Composing the two natural operations — complexify, then take the $2k$-th Chern class, then multiply by the fixed scalar $(-1)^k$ — gives a natural transformation, which is $p_k$. The full naturality statement, that $c_k$ and hence $p_k$ commute with pullback, is proved on [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]; we restate and use it in the corollaries below. The upshot is that the Pontryagin classes are not tied to any connection, metric, or trivialisation: the Chern–Weil form computed from a connection is one concrete representative of a class that the categorical definition pins down connection-free.

---

# Relate to Other Fields / Compression

Pontryagin classes are the **real specialisation of the same Chern–Weil machine** that produces Chern classes, and the compression is exact: over $\mathbb{R}$, the graded ring of characteristic classes of a rank-$n$ real bundle is generated by the $p_k$ (together with the Euler class in the oriented even-rank case), just as the ring for complex bundles is generated by the $c_k$. The three great characteristic-class families — Chern for complex bundles, Pontryagin for real bundles, Euler for oriented real bundles — are not three separate theories but three readings of one construction, "evaluate an invariant polynomial of the curvature". Chern uses the invariant polynomials of $\mathfrak{u}(n)$; Pontryagin uses those of $\mathfrak{so}(n)$ that come from complexifying; the Euler class uses the one extra $\mathfrak{so}(2m)$-invariant polynomial, the Pfaffian, that is not a polynomial in the $\operatorname{tr}(F^{2k})$ but whose square is.

The connection to the wider theory is threefold. **In index theory**, Pontryagin classes are the building blocks of the $\hat A$-genus and the $L$-genus; the Hirzebruch signature theorem reads $\sigma(M^{4}) = \tfrac13 p_1(M)[M]$ in dimension four, so the first Pontryagin number of a four-manifold *is*, up to the factor $\tfrac13$, its signature. This is the entry point through which Pontryagin classes govern the classification of four-manifolds in chapter XIII. **In representation theory**, the fact that only even Chern classes of a complexification survive is the bundle-level shadow of the statement that a real representation, complexified, is isomorphic to its own dual; the machinery here (complexification, conjugation, self-duality) is exactly [[Def - Constructions on Representations]] read at the level of associated bundles. **In Riemannian geometry**, the Pontryagin classes of the tangent bundle are diffeomorphism invariants but, by Novikov's theorem, also topological invariants, which is why they are the natural home for curvature integrals like the four-dimensional Gauss–Bonnet–Chern integrand's Pontryagin partner.

**True name.** Operationally, $p_k(E)$ is *the degree-$4k$ curvature invariant of a real bundle that survives conjugation*: run the Chern–Weil determinant on a skew curvature matrix, keep the honest (real) part $\det\!\big(1 - \tfrac{1}{2\pi}F\big)$, and read off degree $4k$. The official definition through $c_{2k}(E \otimes \mathbb{C})$ and this operational determinant description are proved equal below; the determinant description is the one to compute with.

---

# Examples / Corollaries

Every corollary below is proved to the vault's floor. Several are also recorded as standalone drills among the sibling pages of this chapter; those are named at the point of use so that a reader may practise them in isolation.

### Corollary 1 — the odd Chern classes of a complexification vanish, so the definition loses nothing

**Claim.** For a real bundle $E \to M$ and every odd $j$, $c_j(E \otimes \mathbb{C}) = 0$ in $H^\bullet_{dR}(M)$. Consequently the classes discarded by the Pontryagin construction carry no real information, and the even ones $c_{2k}(E \otimes \mathbb{C})$ are the complete real content of $c(E \otimes \mathbb{C})$.

> [!note]- Full proof
> **What we assume and what we show.** We assume $E$ is a real bundle and $j$ is odd; we show $c_j(E \otimes \mathbb{C}) = 0$ in real de Rham cohomology. We use two facts, each restated with its source.
>
> **Step 1 — the complexification is self-conjugate.** The map $\Phi\colon E \otimes \mathbb{C} \to \overline{E \otimes \mathbb{C}}$ defined fibrewise by $\Phi(v \otimes z) = v \otimes \bar z$ (for $v \in E_m$, $z \in \mathbb{C}$) is $\mathbb{R}$-linear and satisfies $\Phi(i \cdot (v \otimes z)) = \Phi(v \otimes iz) = v \otimes \overline{iz} = v \otimes(-i\bar z) = -i(v \otimes \bar z) = \bar i \cdot \Phi(v \otimes z)$ (by the definition of the conjugate structure, in which $i$ acts as $\bar i = -i$; see [[Def - Constructions on Representations]]). Hence $\Phi$ is complex-linear as a map into $\overline{E \otimes \mathbb{C}}$, and it is fibrewise invertible, so it is a bundle isomorphism $E \otimes \mathbb{C} \cong \overline{E \otimes \mathbb{C}}$.
>
> **Step 2 — conjugation flips the sign of Chern classes.** For any complex bundle $V$ of rank $r$ carrying a Hermitian metric, the conjugate $\overline{V}$ is isomorphic to the dual $V^*$ (the metric gives a conjugate-linear fibre isomorphism $V \to V^*$, which is a complex-linear isomorphism $\overline{V} \to V^*$). By the dual-bundle Chern computation, restated: *for a complex bundle $V$, $c_k(V^*) = (-1)^k c_k(V)$* — this is [[Ex - Chern Classes of the Dual Bundle]], where it is proved by running Chern–Weil on the dual connection, whose curvature is $-F^{\mathsf{T}}$, so that $\det\!\big(1 + \tfrac{i}{2\pi}(-F^{\mathsf{T}})\big) = \det\!\big(1 - \tfrac{i}{2\pi}F\big)$, whose degree-$2k$ part is $(-1)^k$ times that of $\det\!\big(1 + \tfrac{i}{2\pi}F\big)$. Therefore $c_k(\overline{V}) = c_k(V^*) = (-1)^k c_k(V)$.
>
> **Step 3 — combine.** Apply Step 2 with $V = E \otimes \mathbb{C}$ and use Step 1, together with the isomorphism invariance of Chern classes ([[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]], which states that isomorphic bundles have equal characteristic classes):
> $$c_j(E \otimes \mathbb{C}) \;=\; c_j\big(\overline{E \otimes \mathbb{C}}\big) \qquad \text{(Step 1 and isomorphism invariance)}$$
> $$= (-1)^j\, c_j(E \otimes \mathbb{C}) \qquad \text{(Step 2 with } V = E \otimes \mathbb{C}\text{)}.$$
> For odd $j$ this reads $c_j(E \otimes \mathbb{C}) = -c_j(E \otimes \mathbb{C})$, hence $2\,c_j(E \otimes \mathbb{C}) = 0$. Since $H^\bullet_{dR}(M)$ is a real vector space, in which multiplication by $2$ is injective, $c_j(E \otimes \mathbb{C}) = 0$.
>
> **Conclusion.** Every odd Chern class of $E \otimes \mathbb{C}$ vanishes in real de Rham cohomology; the Pontryagin construction, which keeps only the even ones, discards exactly the classes that are already zero. This corollary is recorded as the standalone drill [[Ex - Odd Chern Classes of a Complexified Real Bundle Vanish]]. $\blacksquare$

### Corollary 2 — the Chern–Weil formula: $p(E) = \big[\det\!\big(1 - \tfrac{1}{2\pi}F\big)\big]$

**Claim.** Let $\nabla$ be a metric connection on $E$ with local curvature $F \in \Omega^2(U; \mathfrak{so}(n))$ in an orthonormal frame. Then the closed form $\det\!\big(1 - \tfrac{1}{2\pi}F\big)$ has components only in form-degrees divisible by $4$, its degree-$4k$ component represents $p_k(E)$, and its total class is $p(E)$. In particular the class does not depend on $\nabla$.

> [!note]- Full proof
> **What we assume and what we show.** We assume a metric connection with skew curvature $F$ (a matrix of $2$-forms with $F^{\mathsf{T}} = -F$ in an orthonormal frame, by the definition of a metric connection, [[Def - Euclidean Vector Bundle and Metric Connection]]). We must show, degree by degree, that $\det\!\big(1 - \tfrac{1}{2\pi}F\big) = \sum_{k\ge0} (2\pi)^{-2k}\,\sigma_{2k}(F)$ represents $\sum_k p_k(E)$, and that all odd-index terms vanish. Here $\sigma_j(F)$ denotes the sum of the principal $j \times j$ minors of $F$, a form of degree $2j$; these are the coefficients in the characteristic-polynomial expansion recalled next.
>
> **Step 0 — the class is defined and connection-independent.** By Chern–Weil, restated: *for a complex bundle $V$ with any connection of curvature $\Phi$, the form $\det\!\big(1 + \tfrac{i}{2\pi}\Phi\big)$ is closed, and its de Rham class is independent of the connection; it equals $c(V)$ under our normalisation* — this is [[Thm - Chern-Weil Theorem]], proved in full in this chapter. The complexified connection $\nabla \otimes \mathbb{C}$ on $E \otimes \mathbb{C}$ has curvature $F$ (the same real matrix, now read as $\mathfrak{gl}_n(\mathbb{C})$-valued), so $c(E \otimes \mathbb{C}) = \big[\det\!\big(1 + \tfrac{i}{2\pi}F\big)\big]$, independent of $\nabla$. The Pontryagin classes, being fixed scalar multiples of the components of this class, are therefore defined and connection-independent.
>
> **Step 1 — the determinant expansion.** For any $n \times n$ matrix $A$ whose entries are even-degree forms (so that the entries commute under $\wedge$ and the determinant is the ordinary Leibniz formula; [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]) and any scalar $z$,
> $$\det(1 + z A) \;=\; \sum_{j=0}^{n} z^j\, \sigma_j(A) \qquad \text{(Leibniz expansion, grouping by the number } j \text{ of off-diagonal-from-} 1 \text{ factors)},$$
> where $\sigma_j(A)$ is the sum of the $j \times j$ principal minors of $A$, of form-degree $2j$ when $A$ has $2$-form entries. Apply this with $A = F$ and $z = \tfrac{i}{2\pi}$:
> $$\det\!\Big(1 + \tfrac{i}{2\pi}F\Big) \;=\; \sum_{j=0}^{n} \Big(\tfrac{i}{2\pi}\Big)^j \sigma_j(F) \qquad \text{(Step 1 expansion)},$$
> so the Chern class in degree $2j$ is $c_j(E \otimes \mathbb{C}) = \big[\big(\tfrac{i}{2\pi}\big)^j \sigma_j(F)\big] = \big[i^j (2\pi)^{-j}\sigma_j(F)\big]$.
>
> **Step 2 — the odd minors vanish because $F$ is skew.** Because $F^{\mathsf{T}} = -F$ (metric connection) and the entries are $2$-forms, $\det(1 + zF) = \det\big((1 + zF)^{\mathsf{T}}\big) = \det(1 + zF^{\mathsf{T}}) = \det(1 - zF)$ (the first equality is invariance of $\det$ under transpose, [[Def - Determinant]], valid entrywise here because even forms commute). Substituting the expansion of Step 1 on both sides,
> $$\sum_{j} z^j \sigma_j(F) \;=\; \sum_j (-z)^j \sigma_j(F) \qquad \text{(} \det(1+zF) = \det(1-zF)\text{)},$$
> and comparing coefficients of $z^j$ gives $\sigma_j(F) = (-1)^j \sigma_j(F)$, hence $\sigma_j(F) = 0$ for every **odd** $j$. (Equivalently, by Newton's identities the odd $\sigma_j$ are polynomials in the odd power traces $\operatorname{tr}(F^{2r+1})$, and $\operatorname{tr}(F^{2r+1}) = \operatorname{tr}\big((F^{2r+1})^{\mathsf{T}}\big) = \operatorname{tr}\big((F^{\mathsf{T}})^{2r+1}\big) = \operatorname{tr}\big((-F)^{2r+1}\big) = -\operatorname{tr}(F^{2r+1})$, so $\operatorname{tr}(F^{2r+1}) = 0$; either route gives the same conclusion.) Thus only even-index minors $\sigma_{2k}(F)$ survive, and these have form-degree $4k$.
>
> **Step 3 — assemble the Pontryagin class.** By Step 1 and Step 2, the surviving Chern classes are, for each $k$,
> $$c_{2k}(E \otimes \mathbb{C}) \;=\; \big[i^{2k}(2\pi)^{-2k}\sigma_{2k}(F)\big] \;=\; \big[(-1)^k (2\pi)^{-2k}\sigma_{2k}(F)\big] \qquad \text{(Step 1 with } j = 2k;\ i^{2k} = (-1)^k\text{).}$$
> Therefore, by the definition $p_k(E) = (-1)^k c_{2k}(E \otimes \mathbb{C})$,
> $$p_k(E) \;=\; (-1)^k \big[(-1)^k (2\pi)^{-2k}\sigma_{2k}(F)\big] \;=\; \big[(2\pi)^{-2k}\sigma_{2k}(F)\big] \qquad \text{(the two factors } (-1)^k \text{ cancel).}$$
> On the other hand, expanding $\det\!\big(1 - \tfrac{1}{2\pi}F\big)$ by Step 1 with $z = -\tfrac{1}{2\pi}$ and using Step 2 to drop the odd minors,
> $$\det\!\Big(1 - \tfrac{1}{2\pi}F\Big) \;=\; \sum_{j} \big(-\tfrac{1}{2\pi}\big)^j \sigma_j(F) \;=\; \sum_{k} (2\pi)^{-2k}\sigma_{2k}(F) \qquad \text{(} (-1)^{2k} = 1;\ \text{odd } \sigma_j = 0\text{),}$$
> whose degree-$4k$ component is exactly $(2\pi)^{-2k}\sigma_{2k}(F)$, a representative of $p_k(E)$. Summing over $k$, $\big[\det\!\big(1 - \tfrac{1}{2\pi}F\big)\big] = \sum_k p_k(E) = p(E)$.
>
> **Conclusion.** The total Pontryagin class is represented by $\det\!\big(1 - \tfrac{1}{2\pi}F\big)$, which has only degree-$4k$ components; the degree-$(4k+2)$ components vanish identically as forms because the odd principal minors of a skew matrix vanish. $\blacksquare$

### Corollary 3 — the first Pontryagin class: $p_1(E) = \big[-\tfrac{1}{8\pi^2}\operatorname{tr}(F \wedge F)\big]$

**Claim.** With $F$ as above, $p_1(E)$ is represented by the $4$-form $-\tfrac{1}{8\pi^2}\operatorname{tr}(F \wedge F)$.

> [!note]- Full proof
> **What we show.** By Corollary 2, $p_1(E) = \big[(2\pi)^{-2}\sigma_2(F)\big]$, so it suffices to identify $\sigma_2(F)$, the sum of $2 \times 2$ principal minors of $F$.
>
> **Step 1 — express $\sigma_2$ through traces.** For an $n \times n$ matrix $A$ with commuting (even-form) entries, the sum of $2 \times 2$ principal minors is
> $$\sigma_2(A) \;=\; \sum_{i < j}\big(A_{ii}A_{jj} - A_{ij}A_{ji}\big) \qquad \text{(definition of the principal } 2\times2 \text{ minors)}.$$
> On the other hand $(\operatorname{tr} A)^2 = \big(\sum_i A_{ii}\big)^2 = \sum_i A_{ii}^2 + 2\sum_{i<j}A_{ii}A_{jj}$ and $\operatorname{tr}(A^2) = \sum_{i,j}A_{ij}A_{ji} = \sum_i A_{ii}^2 + 2\sum_{i<j}A_{ij}A_{ji}$ (using that even forms commute, so $A_{ij}\wedge A_{ji} = A_{ji}\wedge A_{ij}$). Subtracting,
> $$(\operatorname{tr} A)^2 - \operatorname{tr}(A^2) \;=\; 2\sum_{i<j}\big(A_{ii}A_{jj} - A_{ij}A_{ji}\big) \;=\; 2\,\sigma_2(A) \qquad \text{(combine the two displays),}$$
> so $\sigma_2(A) = \tfrac12\big((\operatorname{tr} A)^2 - \operatorname{tr}(A^2)\big)$.
>
> **Step 2 — specialise to the skew curvature.** Take $A = F$. Since $F$ is skew, $\operatorname{tr} F = \sum_i F_{ii} = 0$ (the diagonal entries of a skew matrix are $0$). Also $A^2 = F \wedge F$ (matrix product with wedge multiplication of entries), so $\operatorname{tr}(A^2) = \operatorname{tr}(F \wedge F)$. Hence, by Step 1,
> $$\sigma_2(F) \;=\; \tfrac12\big(0 - \operatorname{tr}(F \wedge F)\big) \;=\; -\tfrac12\operatorname{tr}(F \wedge F) \qquad \text{(} \operatorname{tr} F = 0\text{).}$$
>
> **Step 3 — insert the normalisation.** By Corollary 2,
> $$p_1(E) \;=\; \big[(2\pi)^{-2}\sigma_2(F)\big] \;=\; \Big[\tfrac{1}{4\pi^2}\cdot\big(-\tfrac12\operatorname{tr}(F \wedge F)\big)\Big] \;=\; \Big[-\tfrac{1}{8\pi^2}\operatorname{tr}(F \wedge F)\Big] \qquad \text{(Step 2).}$$
>
> **Conclusion.** The first Pontryagin class is represented by $-\tfrac{1}{8\pi^2}\operatorname{tr}(F \wedge F)$, a closed $4$-form whose class is independent of the metric connection by Corollary 2. $\blacksquare$

### Corollary 4 — naturality and the Whitney sum formula (exact over $\mathbb{R}$)

**Claim.** (a) For any smooth $f\colon N \to M$, $p_k(f^* E) = f^* p_k(E)$. (b) For real bundles $E_1, E_2 \to M$, the total Pontryagin classes satisfy $p(E_1 \oplus E_2) = p(E_1) \smile p(E_2)$ in $H^\bullet_{dR}(M)$; equivalently $p_k(E_1 \oplus E_2) = \sum_{a+b=k} p_a(E_1) \smile p_b(E_2)$.

> [!note]- Full proof
> **What we show.** Part (a) is naturality; part (b) is the product formula, exact in real de Rham cohomology (over the integers it holds only modulo $2$-torsion, a point discussed after the proof).
>
> **Part (a) — naturality.** Complexification commutes with pullback: $f^*(E \otimes \mathbb{C}) = (f^* E) \otimes \mathbb{C}$, because pulling a bundle back along $f$ and then complexifying fibrewise is, cocycle by cocycle, the same as complexifying and then pulling back (both produce the bundle with transition functions $g_{\alpha\beta}\circ f$ complexified). Therefore, invoking the naturality of Chern classes — restated: *for every smooth $f$ and complex bundle $V$, $c_k(f^* V) = f^* c_k(V)$*, which is [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]] —
> $$p_k(f^* E) \;=\; (-1)^k c_{2k}\big((f^* E)\otimes\mathbb{C}\big) \;=\; (-1)^k c_{2k}\big(f^*(E \otimes \mathbb{C})\big) \qquad \text{(complexification commutes with } f^*\text{)}$$
> $$= (-1)^k f^* c_{2k}(E \otimes \mathbb{C}) \;=\; f^*\big((-1)^k c_{2k}(E \otimes \mathbb{C})\big) \;=\; f^* p_k(E) \qquad \text{(Chern naturality; } f^* \text{ is linear).}$$
>
> **Part (b) — the product formula, Step 1: complexification is additive.** There is a canonical isomorphism $(E_1 \oplus E_2)\otimes\mathbb{C} \cong (E_1 \otimes \mathbb{C}) \oplus (E_2 \otimes \mathbb{C})$, since $(V \oplus W)\otimes_{\mathbb{R}}\mathbb{C} = (V\otimes_{\mathbb{R}}\mathbb{C})\oplus(W\otimes_{\mathbb{R}}\mathbb{C})$ fibrewise.
>
> **Step 2 — block-diagonal curvature.** Choose metric connections $\nabla_1, \nabla_2$ on $E_1, E_2$ ([[Def - Euclidean Vector Bundle and Metric Connection]] gives their existence); their direct sum $\nabla_1 \oplus \nabla_2$ is a metric connection on $E_1 \oplus E_2$ whose curvature, in a frame adapted to the splitting, is the block-diagonal skew matrix $F = \begin{pmatrix} F_1 & 0 \\ 0 & F_2 \end{pmatrix}$ with $F_i$ the curvature of $\nabla_i$.
>
> **Step 3 — multiplicativity of the determinant.** The determinant of a block-diagonal matrix of even-degree forms is the product of the block determinants ([[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]], which proves $\det\!\begin{pmatrix} A & 0 \\ 0 & B\end{pmatrix} = \det A \cdot \det B$ when the entries are even forms). Hence, representing each total Pontryagin class by its Chern–Weil form (Corollary 2),
> $$\det\!\Big(1 - \tfrac{1}{2\pi}F\Big) \;=\; \det\!\Big(1 - \tfrac{1}{2\pi}F_1\Big)\cdot\det\!\Big(1 - \tfrac{1}{2\pi}F_2\Big) \qquad \text{(block-diagonal multiplicativity).}$$
> Passing to de Rham classes and using that the cup product is represented by the wedge product ($[\alpha]\smile[\beta] = [\alpha \wedge \beta]$, [[Def - de Rham Cohomology]]),
> $$p(E_1 \oplus E_2) \;=\; p(E_1) \smile p(E_2) \qquad \text{(Corollary 2 on each factor; wedge } = \text{ cup).}$$
> Extracting the degree-$4k$ component gives $p_k(E_1 \oplus E_2) = \sum_{a+b=k} p_a(E_1)\smile p_b(E_2)$.
>
> **Conclusion.** Pontryagin classes are natural and multiplicative under Whitney sum, exactly, in real de Rham cohomology. $\blacksquare$

> [!warning] Scope: over the integers the product formula holds only modulo $2$-torsion
> The integral Pontryagin classes (defined with integral Chern classes) satisfy $p(E_1 \oplus E_2) = p(E_1)\smile p(E_2)$ only after tensoring with $\mathbb{Z}[\tfrac12]$, i.e. modulo elements of order a power of $2$. The obstruction is precisely that the odd Chern classes of the complexifications, which are killed in real cohomology by Corollary 1, are only $2$-torsion — not zero — integrally. Because the whole series works with **real de Rham classes** (series convention 2), the formula above is exact for us; the integral subtlety is recorded here and does not affect any computation in this chapter.

### Corollary 5 — the Euler class squares to the top Pontryagin class: $e(E)^2 = p_m(E)$

**Claim.** Let $E \to M$ be an oriented Euclidean real bundle of rank $2m$. Then $e(E)^2 = p_m(E)$ in $H^{4m}_{dR}(M)$, where $e(E) \in H^{2m}_{dR}(M)$ is the Euler class.

> [!note]- Full proof
> **What we assume and what we show.** We assume $E$ is oriented Euclidean of even rank $n = 2m$, so both the Euler class ([[Def - Euler Class of an Oriented Vector Bundle]]) and $p_m(E)$ are defined, and $e(E)$ lives in the top surviving degree $2m$ so $e(E)^2$ and $p_m(E)$ both live in degree $4m = 2n$. We show they are equal.
>
> **Step 1 — the two representatives.** Fix a metric connection compatible with the orientation, with skew curvature $F \in \Omega^2(U; \mathfrak{so}(2m))$ in an oriented orthonormal frame. The Euler class is $e(E) = \big[\operatorname{Pf}\!\big(\tfrac{1}{2\pi}F\big)\big]$ (definition of the Euler class via the Pfaffian, [[Def - Euler Class of an Oriented Vector Bundle]]), a class of degree $2m$; and by Corollary 2, $p_m(E) = \big[(2\pi)^{-2m}\sigma_{2m}(F)\big]$, the top ($k = m$) Pontryagin component.
>
> **Step 2 — identify the top minor with the determinant.** The only $2m \times 2m$ principal minor of the $2m \times 2m$ matrix $F$ is $F$ itself, so $\sigma_{2m}(F) = \det F$. Hence
> $$p_m(E) \;=\; \big[(2\pi)^{-2m}\det F\big] \;=\; \Big[\det\!\Big(\tfrac{1}{2\pi}F\Big)\Big] \qquad \text{(} \det(cA) = c^{n}\det A \text{ with } c = \tfrac1{2\pi},\ n = 2m\text{).}$$
>
> **Step 3 — apply $\operatorname{Pf}^2 = \det$.** For any $2m \times 2m$ skew-symmetric matrix $B$ (here with commuting even-form entries), the Pfaffian satisfies $\operatorname{Pf}(B)^2 = \det B$; this is [[Thm - Properties of the Pfaffian]], proved there for skew matrices over any commutative ring, hence applicable to matrices whose entries are even-degree forms. Apply it to $B = \tfrac{1}{2\pi}F$:
> $$\operatorname{Pf}\!\Big(\tfrac{1}{2\pi}F\Big)^2 \;=\; \det\!\Big(\tfrac{1}{2\pi}F\Big) \qquad \text{(} \operatorname{Pf}^2 = \det\text{).}$$
>
> **Step 4 — pass to cohomology.** The square of the class $e(E)$ is represented by the wedge square of its representative, $e(E)^2 = \big[\operatorname{Pf}\!\big(\tfrac1{2\pi}F\big) \wedge \operatorname{Pf}\!\big(\tfrac1{2\pi}F\big)\big] = \big[\operatorname{Pf}\!\big(\tfrac1{2\pi}F\big)^2\big]$ (cup $=$ wedge, [[Def - de Rham Cohomology]]). Combining,
> $$e(E)^2 \;=\; \Big[\operatorname{Pf}\!\Big(\tfrac1{2\pi}F\Big)^2\Big] \;=\; \Big[\det\!\Big(\tfrac1{2\pi}F\Big)\Big] \;=\; p_m(E) \qquad \text{(Step 3, then Step 2).}$$
>
> **Conclusion.** The square of the Euler class of an oriented rank-$2m$ bundle is its top Pontryagin class. In rank $2$ ($m = 1$) this reads $e(E)^2 = p_1(E)$, consistent with the rank-$2$ instance computed in The Definition, and with [[Ex - The Euler Class of an Oriented Rank-2 Bundle is its First Chern Class]] once $E$ carries a compatible complex structure. $\blacksquare$

### Example 6 — a verified computation: an $SU(2)$-bundle and its real rank-$4$ bundle, $p_1 = -2c_2$

Let $P \to M$ be a principal $SU(2)$-bundle and let $W = P \times_{SU(2)} \mathbb{C}^2$ be the associated complex rank-$2$ bundle for the defining representation; its Chern classes are $c(W) = 1 + c_2(W)$, because $c_1(W) = 0$ (the structure group $SU(2)$ has trivial determinant, so the induced connection on $\det W$ is flat and $c_1(W) = \big[\tfrac{i}{2\pi}\operatorname{tr}F\big] = 0$ as $\operatorname{tr}F = 0$ for $\mathfrak{su}(2)$-valued $F$). We write $c_2(P) := c_2(W)$ for the second Chern class of the bundle. Let $E$ be the **underlying real rank-$4$ bundle** of $W$ (forget the complex structure). We verify, step by step, that
$$p_1(E) \;=\; -2\,c_2(P).$$

**Verification.** The computation rests on one representation-theoretic fact, which we restate and check.

> [!note]- Step 1 — for $SU(2)$ the defining representation is self-conjugate: $\overline{\mathbb{C}^2} \cong \mathbb{C}^2$
> The defining representation $\rho\colon SU(2) \to GL(\mathbb{C}^2)$ is $\rho(g) = g$. Its conjugate $\bar\rho(g) = \bar g$ is isomorphic to $\rho$: the intertwiner is $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and we check $J \bar g = g J$ for all $g \in SU(2)$, i.e. $\bar g = J^{-1} g J$. Writing $g = \begin{pmatrix} \alpha & \beta \\ -\bar\beta & \bar\alpha \end{pmatrix}$ with $|\alpha|^2 + |\beta|^2 = 1$ (the general element of $SU(2)$),
> $$J^{-1} g J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} \alpha & \beta \\ -\bar\beta & \bar\alpha \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -\bar\beta & \bar\alpha \\ -\alpha & -\beta \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} \bar\alpha & \bar\beta \\ -\beta & \alpha \end{pmatrix} = \bar g.$$
> Hence $\bar\rho \cong \rho$; this self-conjugacy is the quaternionic structure of $\mathbb{C}^2 = \mathbb{H}$ (the map $J$ is left multiplication by the quaternion $j$). The statement, together with the full classification of the low-dimensional representations, is [[Thm - Complex Representations of U(1) and SU(2)]]; the intertwiner check above is the piece we use. At the level of associated bundles this gives $\overline{W} \cong W$ (the isomorphism $J$ is $SU(2)$-equivariant, so it globalises to a bundle isomorphism).

> [!note]- Step 2 — the complexification of the real bundle splits: $E \otimes \mathbb{C} \cong W \oplus \overline{W} \cong W \oplus W$
> For any complex bundle $W$ with underlying real bundle $E$, there is a canonical isomorphism $E \otimes \mathbb{C} \cong W \oplus \overline{W}$. Indeed, on a single fibre, let $V$ be a complex vector space of complex dimension $r$ and $V_{\mathbb{R}}$ its underlying real space (real dimension $2r$); the complexification $V_{\mathbb{R}} \otimes_{\mathbb{R}} \mathbb{C}$ has complex dimension $2r$ and carries the $\mathbb{C}$-linear operator $J_{\mathbb{C}} = J \otimes 1$, where $J$ is multiplication by $i$ on $V_{\mathbb{R}}$; since $J^2 = -1$, $J_{\mathbb{C}}$ has eigenvalues $\pm i$, and $V_{\mathbb{R}} \otimes \mathbb{C} = V^{+} \oplus V^{-}$ splits into its $(+i)$- and $(-i)$-eigenspaces. The map $v \mapsto v \otimes 1 - (Jv)\otimes i$ is a complex-linear isomorphism $V \to V^{+}$, and $v \mapsto v \otimes 1 + (Jv)\otimes i$ a complex-linear isomorphism $\overline{V} \to V^{-}$; each is checked by applying $J_{\mathbb{C}}$ and confirming the eigenvalue. These maps are natural in $V$ and $SU(2)$-equivariant, so they globalise to $E \otimes \mathbb{C} \cong W \oplus \overline{W}$. By Step 1, $\overline{W} \cong W$, hence $E \otimes \mathbb{C} \cong W \oplus W$.

> [!note]- Step 3 — compute $c_2(E \otimes \mathbb{C})$ and then $p_1(E)$
> By Step 2 and the Whitney product formula for Chern classes (the complex analogue of Corollary 4(b), proved on [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]] for Chern classes and used here as: *$c(V_1 \oplus V_2) = c(V_1)\smile c(V_2)$*),
> $$c(E \otimes \mathbb{C}) \;=\; c(W \oplus W) \;=\; c(W)\smile c(W) \;=\; (1 + c_2(P))^2 \;=\; 1 + 2\,c_2(P) + c_2(P)^2 \qquad \text{(Step 2; } c(W) = 1 + c_2(P)\text{).}$$
> The degree-$4$ component is $c_2(E \otimes \mathbb{C}) = 2\,c_2(P)$ (the term $c_2(P)^2$ has degree $8$). Therefore, by the definition $p_1(E) = (-1)^1 c_2(E \otimes \mathbb{C})$,
> $$p_1(E) \;=\; -\,c_2(E \otimes \mathbb{C}) \;=\; -2\,c_2(P) \qquad \text{(definition of } p_1;\ c_2(E\otimes\mathbb C) = 2c_2(P)\text{).}$$

Every clause is verified: $c_1(W) = 0$ from $\mathfrak{su}(2)$ being traceless; $\overline{W} \cong W$ from the explicit $SU(2)$-intertwiner $J$; $E \otimes \mathbb{C} \cong W \oplus \overline{W}$ from the eigenspace splitting of $J_{\mathbb{C}}$; and the final $p_1(E) = -2c_2(P)$ from the Chern product formula and the definition. This identity is what lets chapter XIII trade Pontryagin numbers of the base's tangent bundle for instanton numbers $c_2(P)$.

### Non-example — a flat bundle has vanishing Pontryagin classes

If $E \to M$ admits a flat metric connection — one with curvature $F = 0$ — then every Chern–Weil form of it vanishes, so by Corollary 2, $p_k(E) = \big[\det\!\big(1 - \tfrac1{2\pi}\cdot 0\big)\big]_{(4k)} = [1]_{(4k)} = 0$ for all $k \ge 1$. Thus a bundle carrying a flat connection is *not* an instance of "having a nonzero Pontryagin class": the classes are the obstruction that flatness removes. In particular a bundle whose holonomy is finite (so that a flat connection exists after passing to a finite cover, forcing the real classes to vanish) has zero Pontryagin classes. This is the failure mode the definition is designed to detect: $p_k(E) \ne 0$ certifies that $E$ admits **no** flat connection, hence no flat structure.

**Calibration check.** Three quick verifications a reader can carry out from the page. First, $p_k(E) = 0$ whenever $4k > \dim M$, because $p_k(E)$ lives in $H^{4k}_{dR}(M)$ and every form of degree exceeding $\dim M$ is zero; in particular a bundle over a surface or a three-manifold has no Pontryagin classes at all, and $p_1(TS^2) = 0$ since $4 > 2$. Second, $p_1$ of a trivial bundle $M \times \mathbb{R}^n$ is $0$: the product connection is flat, so by the non-example $p_1 = 0$; alternatively, a trivial complexification $M \times \mathbb{C}^n$ has all Chern classes zero by [[Thm - Trivial Bundles Have Vanishing Characteristic Classes]], hence $p_1 = -c_2 = 0$. Third, for an oriented rank-$2$ bundle $E$ one should be able to confirm $p_1(E) = e(E)^2$ directly: this is Corollary 5 with $m = 1$, and it can be cross-checked against the rank-$2$ instance in The Definition, where $p_1(E) = \big[\tfrac{1}{4\pi^2}\varphi\wedge\varphi\big]$ and $e(E) = \big[\tfrac{1}{2\pi}\varphi\big]$ (the Pfaffian of $\begin{pmatrix} 0 & \varphi \\ -\varphi & 0\end{pmatrix}$ is $\varphi$), so that $e(E)^2 = \big[\tfrac{1}{4\pi^2}\varphi\wedge\varphi\big] = p_1(E)$.

---

# Unlocked by This

> [!tip] The signature theorem *(from Gauge Theory XIII)*
> The **first Pontryagin number** $p_1(M)[M] = \int_M p_1(TM)$ of a closed oriented four-manifold equals $3\,\sigma(M)$, three times the signature of its intersection form. Pontryagin classes are the curvature side of this identity; the intersection form is the topological side. This is the bridge by which curvature integrals constrain the classification of four-manifolds.

> [!tip] The instanton number *(from Gauge Theory VI–VII)*
> For an $SU(2)$-bundle $P$, the identity $p_1(E) = -2c_2(P)$ of Example 6 ties the Pontryagin class of the associated real bundle to the **second Chern number** $c_2(P)[M]$, the instanton number that indexes anti-self-dual connections in Yang–Mills theory. The Pontryagin viewpoint is what makes the instanton number a Chern–Weil integral of the curvature.

> [!tip] The $\hat A$-genus and the index of the Dirac operator *(from Gauge Theory VIII)*
> Polynomials in the Pontryagin classes — the $\hat A$-genus $1 - \tfrac{1}{24}p_1 + \dots$ and the $L$-genus $1 + \tfrac13 p_1 + \dots$ — are the characteristic numbers that appear on the right-hand side of the Atiyah–Singer index theorem, expressing the index of the Dirac and signature operators as integrals of Pontryagin forms.
