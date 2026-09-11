---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Chern Classes"
  - "Thm - Chern-Weil Theorem"
  - "Thm - Naturality and Isomorphism Invariance of Characteristic Classes"
  - "Thm - Trivial Bundles Have Vanishing Characteristic Classes"
  - "Thm - First Chern Class of a Line Bundle from Curvature"
  - "Def - Induced Connections on Dual, Hom, and Endomorphism Bundles"
  - "Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ and $N$ are smooth manifolds (Hausdorff, second countable), $f\colon N\to M$ is a smooth map, and $E,E_1,E_2\to M$ are complex vector bundles; $\operatorname{rk}E$ denotes the (complex) rank. We write $E_1\oplus E_2$ for the Whitney sum, $E_1\otimes E_2$ for the tensor product, $E^\vee=\operatorname{Hom}(E;\mathbb C)$ for the dual bundle, $\Lambda^rE$ for the $r$-th exterior power (with $r=\operatorname{rk}E$ this is the determinant line bundle $\det E$), $\underline{\mathbb C}^k=M\times\mathbb C^k$ for the trivial rank-$k$ bundle, and $f^*E\to N$ for the pull-back; these constructions are recorded on [[Def - Operations on Vector Bundles and Pull-Back Bundles]] and the connections they induce on [[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]].

The [[Def - Chern Classes|Chern classes]] are the de Rham cohomology classes obtained from curvature. Choose a [[Def - Complex Vector Bundle and Hermitian Structure|Hermitian structure]] on $E$ and a compatible (unitary) connection $\nabla$ with curvature $F_\nabla\in\Omega^2(M;\operatorname{End}E)$; in a local unitary frame $F_\nabla$ is an $r\times r$ matrix of complex-valued $2$-forms, skew-Hermitian pointwise. The total Chern class is
$$c(E)=\Big[\det\!\Big(1+\tfrac{i}{2\pi}F_\nabla\Big)\Big]=1+c_1(E)+\dots+c_r(E),\qquad c_j(E)\in H^{2j}_{\mathrm{dR}}(M;\mathbb R),$$
where the determinant is computed in the commutative ring $\Omega^{\mathrm{even}}(M)$ of even-degree forms and $c_j(E)$ is the class of the degree-$2j$ component $c_j(F_\nabla)$; the polynomial coefficients are those of Example 81(b) of Haydys, so that $c_0(F)=1$, $c_1(F)=\tfrac{i}{2\pi}\operatorname{tr}F$, and $c_r(F)=\det\!\big(\tfrac{i}{2\pi}F\big)$. That $c_j(F_\nabla)$ is closed and that its class is independent of the Hermitian structure and the connection are the content of the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] together with [[Def - Chern Classes]]; we take these as established. The symbol $\smile$ is the cup product on $H^\bullet_{\mathrm{dR}}(M;\mathbb R)$, which by definition of the ring structure on [[Def - de Rham Cohomology|de Rham cohomology]] is induced by the wedge product of representative forms, $[\alpha]\smile[\beta]=[\alpha\wedge\beta]$. We write $\operatorname{tr}$ for the [[Def - Trace|matrix trace]] and $\det$ for the [[Def - Determinant|determinant]].

The manifold $\mathbb{CP}^1$ carries its complex orientation, and $[\omega_1]\in H^2_{\mathrm{dR}}(\mathbb{CP}^1;\mathbb R)$ denotes the generator normalised by $\int_{\mathbb{CP}^1}[\omega_1]=1$; $\mathcal O(-1)\to\mathbb{CP}^1$ is the tautological line bundle, the sub-bundle of $\mathbb{CP}^1\times\mathbb C^2$ whose fibre over a line $\ell$ is $\ell$ itself, carrying the connection induced by the standard connection on [[Def - The Hopf Bundle|the Hopf bundle]]. Finally $\Sigma$ denotes a closed (compact, boundaryless) oriented surface.

> [!warning] Convention: the factor $\tfrac{i}{2\pi}$ and the generator of $H^2(\mathbb{CP}^1)$
> Haydys writes property (iv) as $c(\mathcal O(-1))=1-a$, where $a$ is the integral generator of $H^2(\mathbb{CP}^1;\mathbb Z)$ fixed by $\langle a,[\mathbb{CP}^1]\rangle=1$ (his equation (73)). The series works in de Rham cohomology and uses the real generator $[\omega_1]$ with $\int_{\mathbb{CP}^1}[\omega_1]=1$; the image of $a$ under $H^2(\mathbb{CP}^1;\mathbb Z)\to H^2_{\mathrm{dR}}(\mathbb{CP}^1;\mathbb R)$ is exactly $[\omega_1]$, so "$1-a$" reads "$1-[\omega_1]$" here. Bär defines $c_1$ from $\lambda(A)=\tfrac{1}{2\pi i}\operatorname{tr}A$ (his Example 2.5.11), whereas the series normalises with $\tfrac{i}{2\pi}\operatorname{tr}$. Since $\tfrac{1}{2\pi i}=-\tfrac{i}{2\pi}$, Bär's $c_j$ differs from the series' by the sign $(-1)^j$ in degree $j$; the series fixes $\tfrac{i}{2\pi}$ so that $\int_{\mathbb{CP}^1}c_1(\mathcal O(-1))=-1$, and every formula below is written in that convention.

---

# Statement

> **Theorem (axioms and properties of Chern classes).** Let $E,E_1,E_2\to M$ be complex vector bundles over a smooth manifold and $f\colon N\to M$ a smooth map. The total Chern class $c(E)=1+c_1(E)+\dots+c_{\operatorname{rk}E}(E)\in H^{\mathrm{even}}_{\mathrm{dR}}(M;\mathbb R)$ satisfies:
> - **(i) (rank-zero part)** $c_0(E)=1$, and $c_j(E)=0$ for $j>\operatorname{rk}E$.
> - **(ii) (naturality)** $c(f^*E)=f^*c(E)$.
> - **(iii) (Whitney sum formula)** $c(E_1\oplus E_2)=c(E_1)\smile c(E_2)$, realised at the level of forms by the wedge product of Chern-form representatives.
> - **(iv) (normalisation)** on $\mathbb{CP}^1$, $c(\mathcal O(-1))=1-[\omega_1]$; equivalently $\displaystyle\int_{\mathbb{CP}^1}c_1(\mathcal O(-1))=-1$.
>
> Consequently:
> - **(v) (isomorphism invariance)** $c(E)$ depends only on the isomorphism class of $E$.
> - **(vi) (dual bundle)** $c_j(E^\vee)=(-1)^j c_j(E)$ for all $j$.
> - **(vii) (trivial and split-off-trivial bundles)** if $E$ is trivial then $c(E)=1$; and if $E\cong E_1\oplus\underline{\mathbb C}^k$ then $c_j(E)=0$ for all $j>\operatorname{rk}E-k$.
> - **(viii) (line bundles and the determinant line)** for complex line bundles $L_1,L_2$, $c_1(L_1\otimes L_2)=c_1(L_1)+c_1(L_2)$; and for any $E$ of rank $r$, $c_1(E)=c_1(\Lambda^rE)$.
> - **(ix) (curvature detects a circle bundle over a surface)** if $P\to\Sigma$ is a principal $U(1)$-bundle over a closed oriented surface with curvature $\bar\Omega$ (equivalently a Hermitian line bundle $L\to\Sigma$ with unitary curvature $F_\nabla$), and $\int_\Sigma\bar\Omega\neq0$, then $P$ (respectively $L$) is not trivial.

The theorem collects Haydys's Theorem 87 (properties (i)–(iv)) and Exercise 88 (properties (v)–(vii)), the additivity theorem (Haydys's Theorem 77(ii), here property (viii)), and Bär's Example 2.5.12 (property (ix)).

---

# Motivation

The [[Def - Chern Classes|Chern classes]] were manufactured from curvature by the [[Thm - Chern-Weil Theorem|Chern–Weil]] machine, and that construction, taken on its own, is opaque: it says only that a certain determinant of a curvature matrix is a closed form whose cohomology class does not move when the connection moves. What one actually wants from a characteristic class is a *bookkeeping device* — an invariant that assigns to each bundle a cohomology class, that behaves predictably under the operations one performs on bundles (pulling back, adding, dualising, tensoring), and that is pinned down by its value in one reference case so that every other value can be computed. The theorem on this page is the statement that the Chern class is exactly such a device.

The four properties (i)–(iv) are not incidental; they are the *characterisation* of Chern classes in algebraic topology. In the axiomatic treatment of Milnor and Stasheff one proves that any rule assigning to complex bundles cohomology classes and satisfying naturality, the Whitney sum formula, and the normalisation on $\mathcal O(-1)$ must be the Chern class — no other invariant obeys all four. Our Chern class, defined analytically through curvature, is therefore *the* Chern class, and the properties below are the certificate. This is why the section spends its effort proving that the curvature construction obeys the axioms rather than checking any single computation: once the axioms hold, the splitting principle and every classical formula follow formally.

Property (iv) deserves a word, because its minus sign is where all the arithmetic is anchored. The bundle $\mathcal O(-1)$ over $\mathbb{CP}^1$ is the tautological line bundle, whose fibre over a point of $\mathbb{CP}^1$ — a complex line in $\mathbb C^2$ — is that very line. It is the fundamental non-trivial line bundle over the simplest non-trivial base, and its first Chern class integrates to $-1$ rather than $+1$ because the tautological bundle winds the "wrong way" relative to the complex orientation. Fixing this one number fixes the normalisation of the whole theory; every Chern number computed downstream — the degree of a line bundle over a surface, the second Chern number of an $SU(2)$-instanton, the Euler number of $TS^2$ — is calibrated against $\int_{\mathbb{CP}^1}c_1(\mathcal O(-1))=-1$.

The remaining properties (v)–(ix) are the working consequences. Isomorphism invariance (v) is what makes $c(E)$ an invariant of $E$ at all rather than of a choice of connection; the dual and tensor formulas (vi) and (viii) are the computational engine that lets one reduce any Chern class to those of line bundles; the vanishing statements (vii) turn "$c_j(E)\neq0$" into a genuine obstruction to $E$ splitting off trivial summands; and (ix) is the first and cleanest instance of a Chern class *detecting* topology — over a closed surface, a single number, the integral of the curvature, decides whether a circle bundle is trivial. We assume the reader has the Chern–Weil theorem, the naturality and isomorphism-invariance theorem, the vanishing theorem for trivial bundles, and the first-Chern-from-curvature theorem in hand, together with the elementary linear algebra of the determinant over a commutative ring.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypotheses of the individual properties are mild — a complex vector bundle, a smooth map, a Hermitian line bundle over a surface — so the useful "source" question is: in what disguises does a problem hand you one of these, so that a Chern-class computation becomes available?

The first disguised source is **a bundle presented by a construction rather than by a curvature**. A great many bundles arrive as pull-backs, sums, tensor products, duals, or exterior powers of simpler bundles — the tangent bundle of a product is a sum, a determinant line is an exterior power, an endomorphism bundle is $E\otimes E^\vee$. The bridge is that properties (ii), (iii), (vi), (viii) turn each such presentation into an arithmetic identity among Chern classes: one never needs the curvature of the constructed bundle, only the Chern classes of its constituents. The non-obvious step is to *recognise the construction*: to see that $T\mathbb{CP}^n$ sits in an exact sequence built from $\mathcal O(-1)$, so that the Whitney formula computes $c(T\mathbb{CP}^n)$ without ever writing a connection. *Example problem:* compute the total Chern class of $\operatorname{End}(E)=E\otimes E^\vee$ for a rank-$2$ bundle $E$ using (iii), (vi), and (viii).

The second disguised source is **a topological obstruction question phrased without any mention of cohomology**. "Does $E$ have a nowhere-vanishing section?", "Is $E$ trivial?", "Does $E$ split off a trivial line?" are questions about sections, but each is answered by a vanishing statement in (vii): a nowhere-vanishing section reduces the structure group and forces the top Chern class to vanish, and a splitting $E\cong E_1\oplus\underline{\mathbb C}^k$ forces $c_j=0$ above $\operatorname{rk}E-k$. The bridge is the contrapositive: a non-zero Chern class is a certificate that no such section, triviality, or splitting exists. The non-obviousness is that a purely geometric non-existence statement is decided by computing a single cohomology class. *Example problem:* show $TS^2$ has no nowhere-vanishing vector field by exhibiting $c_1(TS^2)\neq0$ (the hairy-ball theorem through Chern classes).

The third disguised source is **an integer that one wishes to read off a geometric integral**. Property (ix), and its refinement on [[Thm - First Chern Class of a Line Bundle from Curvature|the first-Chern-from-curvature page]], say that $\tfrac{i}{2\pi}\int_\Sigma F_\nabla$ is not merely a real number but an integer, the degree of the line bundle. Whenever a problem produces an integral of a curvature — a magnetic flux, a Berry phase, a winding number — over a closed surface, the source property is "this integral is quantised", and the bridge is that it equals a Chern number. The non-obvious content is quantisation: the integral cannot vary continuously because it computes a discrete invariant. *Example problem:* derive Dirac's quantisation of magnetic charge from the integrality of $\tfrac{i}{2\pi}\int_{S^2}F$.

**Targets (Output Amplification)**

The bare properties combine with further ingredients to produce the standard structural results of the subject.

Combine (ii), (iii), and (iv) with **the tautological exact sequence on projective space**. On $\mathbb{CP}^n$ the Euler sequence $0\to\underline{\mathbb C}\to\mathcal O(1)^{\oplus(n+1)}\to T\mathbb{CP}^n\to0$ expresses the tangent bundle through the dual $\mathcal O(1)=\mathcal O(-1)^\vee$ of the tautological bundle. Feeding this into the Whitney formula (iii), with $c_1(\mathcal O(1))=+[\omega_1]$ from (iv) and (vi), yields $c(T\mathbb{CP}^n)=(1+[\omega_1])^{n+1}$ — the entire Chern class of projective space from one normalisation and the sum formula. The payoff is that every Chern number of $\mathbb{CP}^n$ becomes a binomial coefficient.

Combine (iii) and the additivity (viii) with **the splitting principle**. Because $c_1$ is additive on line bundles and the Whitney formula multiplies total classes, one may compute as though every bundle were a sum of line bundles: pull back to a flag bundle where $E$ splits, do the line-bundle arithmetic, and descend by injectivity of the pull-back on cohomology. The extra ingredient is the flag-bundle computation; the payoff is that the Chern classes of $E^{\otimes m}$, $\operatorname{Sym}^m E$, $\Lambda^m E$, and any Schur functor are polynomials in the $c_j(E)$, computed formally.

Combine (ix) and its integrality refinement with **the Chern–Simons functional and the second Chern number** (§6.4). The same Stokes-theorem mechanism that quantises $\tfrac{i}{2\pi}\int_\Sigma F$ over a surface reappears one dimension up: the integrality of $\tfrac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)$ over a closed $4$-manifold is what makes the Chern–Simons functional $\mathbb R/\mathbb Z$-valued, and (ix) is the two-dimensional prototype of that four-dimensional fact. The extra ingredient is the transgression formula; the payoff is the instanton number and the topological energy bound for Yang–Mills (§6.4, and chapter VII).

---

# Why Is It True

Set the formal proof aside and look at what the total Chern class *is*: it is the determinant $\det(1+\tfrac{i}{2\pi}F)$ read off the curvature matrix $F$. Every one of the properties is the shadow, under this determinant, of the way curvature is assembled when one performs the corresponding operation on the underlying bundle.

Take the four operations one at a time. When you form a direct sum $E_1\oplus E_2$, the natural connection is the one that differentiates each summand separately, so its curvature is *block-diagonal*: the matrix $\begin{pmatrix}F_1&0\\0&F_2\end{pmatrix}$. The determinant of a block-diagonal matrix is the product of the block determinants, and so $c(E_1\oplus E_2)=c(E_1)\smile c(E_2)$ — the Whitney formula is nothing but "$\det$ of a block-diagonal matrix is a product", carried out in the ring of even forms where the entries commute. When you dualise, the induced connection has connection matrix $-A^t$, so the curvature becomes $-F^t$; the determinant is transpose-invariant and $\det(1-\tfrac{i}{2\pi}F)$ differs from $\det(1+\tfrac{i}{2\pi}F)$ by replacing $F$ with $-F$, which negates the degree-$j$ piece exactly $j$ times — hence the sign $(-1)^j$ in (vi). When you tensor two line bundles, the curvatures simply add, because the connection on the product acts by the Leibniz rule and the self-wedge of a scalar $1$-form vanishes; the first Chern class, being the trace, is additive, giving (viii). And when you take the top exterior power, the induced connection differentiates $e_1\wedge\dots\wedge e_r$ term by term and only the diagonal survives, so its connection form is $\operatorname{tr}A$ and its curvature $\operatorname{tr}F$ — the first Chern class of the determinant line equals that of $E$.

The properties that look topological rather than algebraic have the same source. Naturality (ii) holds because pulling back the bundle pulls back the connection, hence the curvature, hence the determinant; it is the statement that $\det(1+\tfrac{i}{2\pi}(\cdot))$ commutes with $f^*$. Isomorphism invariance (v) holds because an isomorphism conjugates the curvature, and the determinant does not see conjugation. Triviality (vii) holds because a trivial bundle carries a flat connection, whose curvature is zero, whose determinant is $1$. And the detection statement (ix) holds because a trivial bundle would make the Chern form exact, and Stokes' theorem kills the integral of an exact form over a closed surface — so a non-zero integral is incompatible with triviality.

**The single mechanism behind every axiom is that the Chern class is $\det(1+\tfrac{i}{2\pi}F)$, and this determinant converts the way curvature is built under a bundle operation — block-diagonal under $\oplus$, negative-transpose under $(-)^\vee$, additive under $\otimes$ of lines, trace under $\Lambda^{\mathrm{top}}$, pulled-back under $f^*$, conjugated under isomorphism, zero under a flat connection — into the corresponding operation on cohomology classes.**

---

# What Makes This Hard

The genuinely non-obvious step is that the determinant computation happens *in the commutative ring of even-degree forms*, not in a field: the entries $\tfrac{i}{2\pi}F_{ij}$ are $2$-forms, and one must know that even forms commute (so that "determinant" and "$\det$ is multiplicative" even make sense) before the block-diagonal argument for the Whitney formula is legitimate. The common error is to treat $\det(1+\tfrac{i}{2\pi}F)$ as an ordinary numerical determinant and forget that a step like $\det(AB)=\det A\det B$ needs the ring to be commutative — which for forms is true only in even degree. A second subtlety is the sign in (vi): one must correctly compute that the dual connection has curvature $-F^{t}$ (both the negation and the transpose, and the fact that $A^t\wedge A^t=-(A\wedge A)^t$ for matrices of $1$-forms), and then track that homogeneity turns $F\mapsto-F$ into $(-1)^j$ in degree $j$ — dropping either the transpose or the homogeneity gives the wrong sign. Finally, properties (ii), (iv), (v), and (vii) are not proved from scratch here: they are the specialisations to $U(r)$ of theorems established on their own pages, and the work is to invoke each with its hypotheses named, not to re-derive it.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Write $c(E)=[\det(1+\tfrac{i}{2\pi}F_\nabla)]$ and prove each property by identifying the curvature of the constructed bundle and applying the determinant. Properties (i), (iii), (vi), (viii) are direct determinant computations from the curvature of the relevant construction; (ii), (iv), (v), (vii-trivial) are invocations of already-proved theorems, restated; (ix) is one application of Stokes to an exact form.

**Subgoal decomposition:**

1. **Algebraic skeleton of the total Chern form.** Show $\det(1+\tfrac{i}{2\pi}F)=\sum_{j=0}^r c_j(F)$ with $c_0=1$, $c_1=\tfrac{i}{2\pi}\operatorname{tr}F$, $c_r=\det(\tfrac{i}{2\pi}F)$, each $c_j$ homogeneous of degree $j$ in $F$, and $c_j=0$ for $j>r$.
   - *Hint:* Expand the determinant of an $r\times r$ matrix $1+N$ by the Leibniz formula; group by the number of factors drawn from $N$.
   - *Why needed:* Gives (i) outright, the homogeneity $c_j(-F)=(-1)^jc_j(F)$ used in (vi), and the vanishing above the rank used in (vii).

2. **Curvature under the four constructions.** Compute the curvature of the direct-sum, dual, tensor-of-lines, and top-exterior-power connections: block-diagonal $F_1\oplus F_2$; $-F^t$; $F_1+F_2$; $\operatorname{tr}F$.
   - *Hint:* Use the local connection matrix in a unitary frame and the formula $F=dA+A\wedge A$; for the dual note $A\mapsto-A^t$, for $\Lambda^r$ note only diagonal terms survive the wedge.
   - *Why needed:* These are the inputs to the determinant computations for (iii), (vi), (viii).

3. **Whitney formula (iii).** Apply "$\det$ of a block-diagonal matrix over $\Omega^{\mathrm{even}}$ is the product of the blocks' determinants".
   - *Hint:* Invoke the even-form determinant exercise; recognise the product of the two even forms as their wedge, and wedge as cup on cohomology.
   - *Why needed:* It is the multiplicativity that (vii) and every splitting argument rest on.

4. **Dual (vi).** From $F^\vee=-F^t$, compute $\det(1+\tfrac{i}{2\pi}F^\vee)=\det(1-\tfrac{i}{2\pi}F)$ and read off degree $2j$ via homogeneity.
   - *Hint:* Use transpose-invariance of $\det$ and subgoal 1.
   - *Why needed:* Supplies the sign and, at $r=1$, the line-bundle dual formula.

5. **Additivity and the determinant line (viii).** From $F^\otimes=F_1+F_2$ on line bundles and $F^{\Lambda^r}=\operatorname{tr}F$, take first Chern classes.
   - *Hint:* $c_1=\tfrac{i}{2\pi}\operatorname{tr}$ is additive; $\operatorname{tr}(A\wedge A)=0$.
   - *Why needed:* Reduces multi-line computations to addition and lets one replace $E$ by its determinant line for $c_1$.

6. **Invocations (ii), (iv), (v), (vii-trivial) and Stokes (ix).** Restate and apply the naturality/isomorphism-invariance theorem, the first-Chern-from-curvature normalisation, and the trivial-bundle vanishing theorem; run the Stokes argument for (ix).
   - *Hint:* Each invoked theorem is a sibling page whose proof is complete; name its hypotheses.
   - *Why needed:* Completes the list without re-proving results proved elsewhere.

---

# Lemma Decomposition

> [!note]- Lemma 1: Algebraic structure of the total Chern form
> **Statement:** Let $F=(F_{k\ell})$ be an $r\times r$ matrix whose entries are $2$-forms on $M$, regarded as elements of the commutative ring $\Omega^{\mathrm{even}}(M)$. Then
> $$\det\!\Big(1+\tfrac{i}{2\pi}F\Big)=\sum_{j=0}^r c_j(F),\qquad c_j(F)\in\Omega^{2j}(M),$$
> with $c_0(F)=1$, $c_1(F)=\tfrac{i}{2\pi}\operatorname{tr}F$, $c_r(F)=\det(\tfrac{i}{2\pi}F)$; each $c_j(F)$ is a homogeneous polynomial of degree $j$ in the entries of $F$, so that $c_j(-F)=(-1)^jc_j(F)$; and $c_j(F)=0$ for $j>r$.
>
> **Hint:** Expand $\det(1+N)$ with $N=\tfrac{i}{2\pi}F$ by the Leibniz sum over permutations and collect terms by how many off-"$1$" factors they use.
>
> **Why needed:** It gives property (i) directly, the homogeneity used to extract the sign in (vi), and the "vanishing above the rank" used in (vii).
>
> > [!note]- Full proof
> > Write $N:=\tfrac{i}{2\pi}F$, an $r\times r$ matrix with entries $N_{k\ell}=\tfrac{i}{2\pi}F_{k\ell}\in\Omega^2(M)$; by the [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative|even-form commutativity exercise]] (whose statement is that $\Omega^{\mathrm{even}}(M)$ is a commutative ring, so that products of even-degree forms commute), the determinant of a matrix with entries in $\Omega^{\mathrm{even}}(M)$ is defined by the ordinary Leibniz formula and has all the usual properties.
> >
> > **Leibniz expansion.** By the [[Def - Determinant|Leibniz formula for the determinant]] over a commutative ring,
> > $$\det(1+N)=\sum_{\sigma\in S_r}\operatorname{sign}(\sigma)\prod_{k=1}^r(1+N)_{k\,\sigma(k)}\qquad\text{(Leibniz formula, entries in }\Omega^{\mathrm{even}}\text{)},$$
> > where $(1+N)_{k\ell}=\delta_{k\ell}+N_{k\ell}$. Expanding each factor $(1+N)_{k\sigma(k)}$ into its "$\delta$" part and its "$N$" part and multiplying out, a typical term selects a subset $S\subseteq\{1,\dots,r\}$ of rows at which the $N$-factor is chosen; the remaining rows contribute $\delta_{k\sigma(k)}$, forcing $\sigma(k)=k$ there. The total form-degree of such a term is $2|S|$, since each chosen $N_{k\sigma(k)}$ is a $2$-form and the $\delta$-factors carry degree $0$.
> >
> > **Grading by $|S|$.** Collecting all terms with $|S|=j$ gives a form of pure degree $2j$; call it $c_j(F)$. Hence $\det(1+N)=\sum_{j=0}^r c_j(F)$ with $c_j(F)\in\Omega^{2j}(M)$, and the sum stops at $j=r$ because $|S|\le r$. In particular $c_j(F)=0$ for $j>r$.
> >
> > **The three named coefficients.** For $j=0$ the only term has $S=\varnothing$, all factors $\delta_{k\sigma(k)}$, forcing $\sigma=\mathrm{id}$ and contributing $\operatorname{sign}(\mathrm{id})\cdot1=1$; thus $c_0(F)=1$. For $j=1$ the subset $S=\{k\}$ is a single row, the other factors force $\sigma$ to fix every other index and hence $\sigma=\mathrm{id}$, so the term is $N_{kk}$; summing over $k$, $c_1(F)=\sum_k N_{kk}=\operatorname{tr}N=\tfrac{i}{2\pi}\operatorname{tr}F$. For $j=r$ every factor is an $N$-factor, so $c_r(F)=\det N=\det(\tfrac{i}{2\pi}F)$.
> >
> > **Homogeneity.** Each $c_j(F)$ is a sum of products of exactly $j$ entries of $N=\tfrac{i}{2\pi}F$, hence a homogeneous polynomial of degree $j$ in the entries of $F$. Replacing $F$ by $-F$ replaces $N$ by $-N$ and multiplies every degree-$j$ term by $(-1)^j$, so $c_j(-F)=(-1)^jc_j(F)$. $\blacksquare$

> [!note]- Lemma 2: Curvature under the four bundle constructions
> **Statement:** Let $E,E_1,E_2\to M$ be Hermitian complex vector bundles with unitary connections, curvatures $F,F_1,F_2$ written as matrices in local unitary frames, and let $L_1,L_2$ be Hermitian line bundles with unitary connections of local connection $1$-forms $\alpha_1,\alpha_2$ and curvatures $F_1=d\alpha_1,F_2=d\alpha_2$. Then, for the induced connections of [[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]]:
> - **(a)** the direct-sum connection on $E_1\oplus E_2$ has curvature the block-diagonal matrix $\begin{pmatrix}F_1&0\\0&F_2\end{pmatrix}$;
> - **(b)** the dual connection on $E^\vee$ has curvature $-F^t$;
> - **(c)** the tensor connection on $L_1\otimes L_2$ has curvature $F_1+F_2$;
> - **(d)** the connection on $\Lambda^rE$ ($r=\operatorname{rk}E$) has curvature $\operatorname{tr}F$.
>
> **Hint:** Use the local connection matrix $A$ and $F=dA+A\wedge A$; for the dual, the connection matrix becomes $-A^t$; for $\Lambda^r$, only diagonal terms survive the wedge of frame vectors.
>
> **Why needed:** These four curvatures are the inputs to the determinant computations that prove (iii), (vi), and (viii).
>
> > [!note]- Full proof
> > **(a) Direct sum.** The direct-sum connection is $\nabla=\nabla_1\oplus\nabla_2$, acting by $\nabla_X(s_1,s_2)=((\nabla_1)_Xs_1,(\nabla_2)_Xs_2)$. Using the curvature formula $F_\nabla(X,Y)s=\nabla_X\nabla_Ys-\nabla_Y\nabla_Xs-\nabla_{[X,Y]}s$ applied to $s=(s_1,s_2)$, every operation acts on the two components separately, so
> > $$F_\nabla(X,Y)(s_1,s_2)=\big(F_1(X,Y)s_1,\;F_2(X,Y)s_2\big)\qquad\text{(each term of the bracket splits over the two summands)}.$$
> > Thus $F_\nabla=F_1\oplus F_2$ as an endomorphism-valued form; in the frame obtained by concatenating unitary frames of $E_1$ and $E_2$ it is the block-diagonal matrix $\begin{pmatrix}F_1&0\\0&F_2\end{pmatrix}$.
> >
> > **(b) Dual.** Let $e=(e_1,\dots,e_r)$ be a local unitary frame of $E$ with connection matrix $A$, so $\nabla e_k=\sum_\ell A_{\ell k}e_\ell$, and let $e^*=(e^1,\dots,e^r)$ be the dual coframe of $E^\vee$. The dual connection $\nabla^\vee$ is defined by the compatibility $d\langle\xi,s\rangle=\langle\nabla^\vee\xi,s\rangle+\langle\xi,\nabla s\rangle$ for $\xi\in\Gamma(E^\vee)$, $s\in\Gamma(E)$ (this is the definition on [[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]]). Applying it to $\xi=e^k$, $s=e_m$ and using $\langle e^k,e_m\rangle=\delta^k_m$ (a constant, so $d\langle e^k,e_m\rangle=0$):
> > $$0=\langle\nabla^\vee e^k,e_m\rangle+\langle e^k,\nabla e_m\rangle=\langle\nabla^\vee e^k,e_m\rangle+A_{km}\qquad\text{(since }\langle e^k,\nabla e_m\rangle=\langle e^k,\textstyle\sum_\ell A_{\ell m}e_\ell\rangle=A_{km}\text{)},$$
> > so $\langle\nabla^\vee e^k,e_m\rangle=-A_{km}$, i.e. $\nabla^\vee e^k=-\sum_m A_{km}e^m=\sum_m(-A^t)_{mk}e^m$. Hence the connection matrix of $E^\vee$ in the coframe $e^*$ is $A^\vee=-A^t$. Its curvature is
> > $$F^\vee=dA^\vee+A^\vee\wedge A^\vee=-dA^t+(-A^t)\wedge(-A^t)=-dA^t+A^t\wedge A^t\qquad\text{(curvature formula }F=dA+A\wedge A\text{)}.$$
> > For matrices of $1$-forms, $(A^t\wedge A^t)_{k\ell}=\sum_m A_{mk}\wedge A_{\ell m}=-\sum_m A_{\ell m}\wedge A_{mk}=-\big((A\wedge A)^t\big)_{k\ell}$ (using that $1$-forms anticommute in the middle equality), so $A^t\wedge A^t=-(A\wedge A)^t$. Therefore
> > $$F^\vee=-dA^t-(A\wedge A)^t=-\big(dA+A\wedge A\big)^t=-F^t.$$
> >
> > **(c) Tensor of line bundles.** The tensor connection is $\nabla^\otimes(s_1\otimes s_2)=\nabla_1 s_1\otimes s_2+s_1\otimes\nabla_2 s_2$. In local unitary frames $e_1$ of $L_1$ and $e_2$ of $L_2$, with $\nabla_1e_1=\alpha_1e_1$ and $\nabla_2e_2=\alpha_2e_2$ ($\alpha_i$ scalar $1$-forms since the bundles have rank $1$), the frame $e_1\otimes e_2$ of $L_1\otimes L_2$ satisfies
> > $$\nabla^\otimes(e_1\otimes e_2)=\alpha_1e_1\otimes e_2+e_1\otimes\alpha_2e_2=(\alpha_1+\alpha_2)(e_1\otimes e_2)\qquad\text{(Leibniz rule for }\nabla^\otimes\text{)},$$
> > so the connection $1$-form is $\alpha_1+\alpha_2$. Its curvature is $F^\otimes=d(\alpha_1+\alpha_2)+(\alpha_1+\alpha_2)\wedge(\alpha_1+\alpha_2)=d\alpha_1+d\alpha_2$, because a scalar $1$-form wedged with itself vanishes, $(\alpha_1+\alpha_2)\wedge(\alpha_1+\alpha_2)=0$. Since likewise $F_i=d\alpha_i+\alpha_i\wedge\alpha_i=d\alpha_i$, we get $F^\otimes=F_1+F_2$.
> >
> > **(d) Top exterior power.** Let $e=(e_1,\dots,e_r)$ be a local unitary frame with connection matrix $A$, so $\Lambda^rE$ has the local frame $e_1\wedge\dots\wedge e_r$. The induced connection differentiates by the Leibniz rule:
> > $$\nabla^{\Lambda^r}(e_1\wedge\dots\wedge e_r)=\sum_{k=1}^r e_1\wedge\dots\wedge\nabla e_k\wedge\dots\wedge e_r=\sum_{k=1}^r e_1\wedge\dots\wedge\Big(\sum_\ell A_{\ell k}e_\ell\Big)\wedge\dots\wedge e_r.$$
> > In the $k$-th summand only the term $\ell=k$ survives, because any $\ell\neq k$ repeats a frame vector and the wedge vanishes; that surviving term is $A_{kk}(e_1\wedge\dots\wedge e_r)$. Summing, $\nabla^{\Lambda^r}(e_1\wedge\dots\wedge e_r)=\big(\sum_k A_{kk}\big)(e_1\wedge\dots\wedge e_r)=\operatorname{tr}(A)\,(e_1\wedge\dots\wedge e_r)$, so the connection $1$-form is $\operatorname{tr}A$. Its curvature is $F^{\Lambda^r}=d(\operatorname{tr}A)=\operatorname{tr}(dA)$. Finally $\operatorname{tr}(A\wedge A)=\sum_{k,\ell}A_{k\ell}\wedge A_{\ell k}=0$, since interchanging the summation labels $k\leftrightarrow\ell$ and using anticommutativity of $1$-forms sends the sum to its own negative; therefore $\operatorname{tr}F=\operatorname{tr}(dA+A\wedge A)=\operatorname{tr}(dA)=F^{\Lambda^r}$. $\blacksquare$

> [!note]- Lemma 3: Determinant identities over the ring of even forms
> **Statement:** Let $R=\Omega^{\mathrm{even}}(M)$, a commutative ring. For square matrices $P,Q$ over $R$ of the same size, $\det(PQ)=\det(P)\det(Q)$; for a block-diagonal matrix, $\det\begin{pmatrix}P&0\\0&Q\end{pmatrix}=\det(P)\det(Q)$; and $\det(P^t)=\det(P)$.
>
> **Hint:** These are the standard determinant identities over any commutative ring; the only thing to verify is that $R$ is commutative, which is the even-form exercise.
>
> **Why needed:** Block-multiplicativity gives the Whitney formula (iii); transpose-invariance gives the dual formula (vi).
>
> > [!note]- Full proof
> > **Commutativity of $R$.** By the [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative|even-form exercise]], forms of even degree commute under the wedge product, so $R=\Omega^{\mathrm{even}}(M)$ is a commutative (unital, associative) ring, and the determinant of a matrix over $R$ is defined by the Leibniz formula $\det(P)=\sum_{\sigma\in S_n}\operatorname{sign}(\sigma)\prod_k P_{k\sigma(k)}$, the product being unambiguous because $R$ is commutative.
> >
> > **Multiplicativity $\det(PQ)=\det(P)\det(Q)$.** The multiplicativity of the determinant is proved on [[Thm - Determinant is Multiplicative|the multiplicativity page]] over a field — its statement there is $\det(AB)=\det(A)\det(B)$ for $n\times n$ matrices over a field, proved from the one-dimensionality of the space of alternating $n$-linear forms. That argument uses division and does not apply verbatim to $R$, which has zero divisors; we deduce the identity over $R$ from the field case by specialising a universal polynomial identity, as follows. Let $x_{k\ell},y_{k\ell}$ ($1\le k,\ell\le n$) be $2n^2$ independent indeterminates and let $X=(x_{k\ell})$, $Y=(y_{k\ell})$ over the polynomial ring $\mathbb Z[x_{k\ell},y_{k\ell}]$. Both $\det(XY)$ and $\det(X)\det(Y)$ are elements of $\mathbb Z[x_{k\ell},y_{k\ell}]$, which embeds in its fraction field $\mathbb Q(x_{k\ell},y_{k\ell})$; over that field the multiplicativity page gives $\det(XY)=\det(X)\det(Y)$, and since the embedding is injective this equality already holds in $\mathbb Z[x_{k\ell},y_{k\ell}]$ as an identity of polynomials with integer coefficients. Given $P,Q\in\operatorname{Mat}_n(R)$, the unique ring homomorphism $\varphi\colon\mathbb Z[x_{k\ell},y_{k\ell}]\to R$ with $\varphi(x_{k\ell})=P_{k\ell}$ and $\varphi(y_{k\ell})=Q_{k\ell}$ sends $\det(XY)\mapsto\det(PQ)$ and $\det(X)\det(Y)\mapsto\det(P)\det(Q)$, because both matrix multiplication and the Leibniz determinant are polynomials with integer coefficients in the matrix entries and are therefore preserved by any ring homomorphism; applying $\varphi$ to the polynomial identity yields $\det(PQ)=\det(P)\det(Q)$ over $R$.
> >
> > **Block-diagonal determinant.** Expanding $\det\begin{pmatrix}P&0\\0&Q\end{pmatrix}$ by the Leibniz formula, only permutations preserving the two index blocks contribute (any permutation mixing the blocks lands on a zero entry in one factor, killing the term), and such a permutation is uniquely a permutation $\tau$ of the $P$-block together with a permutation $\rho$ of the $Q$-block with $\operatorname{sign}=\operatorname{sign}(\tau)\operatorname{sign}(\rho)$; collecting these terms and re-ordering the product by commutativity of $R$ gives $\det\begin{pmatrix}P&0\\0&Q\end{pmatrix}=\det(P)\det(Q)$.
> >
> > **Transpose-invariance.** $\det(P^t)=\det(P)$ follows from the Leibniz formula by re-indexing the sum over $\sigma$ by $\sigma^{-1}$: $\det(P^t)=\sum_\sigma\operatorname{sign}(\sigma)\prod_k P_{\sigma(k)k}=\sum_\sigma\operatorname{sign}(\sigma^{-1})\prod_k P_{k\sigma^{-1}(k)}=\det(P)$, using $\operatorname{sign}(\sigma)=\operatorname{sign}(\sigma^{-1})$ and that the product may be re-ordered because $R$ is commutative. The Leibniz formula and cofactor expansion for the number field are on [[Def - Determinant]] and [[Thm - Cofactor Expansion and Cramer's Rule|the cofactor-expansion page]]. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix a Hermitian structure and a compatible connection $\nabla$ on $E$ (and on $E_1,E_2$, $L_1,L_2$ as needed), with curvature matrix $F$ in a local unitary frame. Throughout, $c(E)=[\det(1+\tfrac{i}{2\pi}F)]$ and $c_j(F)$ denotes the degree-$2j$ component of Lemma 1; by [[Def - Chern Classes]] the class $c_j(E)=[c_j(F)]$ is independent of the frame, the Hermitian structure, and the connection, and $c_j(F)$ is closed, by the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] (statement: for a principal $G$-bundle with connection and an $\operatorname{Ad}$-invariant polynomial $p$ of degree $d$, the form $p(F)$ is closed and its de Rham class is independent of the connection).
>
> **Property (i) — rank-zero part.** By Lemma 1, $\det(1+\tfrac{i}{2\pi}F)=\sum_{j=0}^r c_j(F)$ with $c_0(F)=1$ and $c_j(F)=0$ for $j>r=\operatorname{rk}E$. Passing to cohomology, $c_0(E)=[1]=1\in H^0_{\mathrm{dR}}(M)$ and $c_j(E)=[0]=0$ for $j>\operatorname{rk}E$.
>
> **Property (ii) — naturality.** This is part (a) of the [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes|naturality and isomorphism-invariance theorem]], whose statement is: for a smooth map $f\colon N\to M$, a principal $G$-bundle $P\to M$, and $p\in I(G)$, one has $c_p(f^*P)=f^*c_p(P)$. Applied to the frame bundle of $E$ with $G=U(r)$ and $p=c_j$, and using $\operatorname{Fr}_U(f^*E)\cong f^*\operatorname{Fr}_U(E)$, this reads $c_j(f^*E)=f^*c_j(E)$ for every $j$; summing over $j$ gives $c(f^*E)=f^*c(E)$. Concretely, pulling back a unitary connection $\nabla$ on $E$ gives a unitary connection $f^*\nabla$ on $f^*E$ with curvature $f^*F$, and since $f^*$ is a homomorphism of the algebras of forms commuting with the entrywise determinant, $\det(1+\tfrac{i}{2\pi}f^*F)=f^*\det(1+\tfrac{i}{2\pi}F)$; taking classes and using that $f^*$ on closed forms descends to $f^*$ on cohomology yields the claim.
>
> **Property (iii) — Whitney sum formula.** Equip $E_1,E_2$ with Hermitian structures and unitary connections $\nabla_1,\nabla_2$ of curvatures $F_1,F_2$, and give $E_1\oplus E_2$ the direct-sum Hermitian structure and the direct-sum connection $\nabla_1\oplus\nabla_2$, which is unitary. By Lemma 2(a) its curvature is the block-diagonal matrix $F=\begin{pmatrix}F_1&0\\0&F_2\end{pmatrix}$. Hence, over the commutative ring $\Omega^{\mathrm{even}}(M)$,
> $$\det\!\Big(1+\tfrac{i}{2\pi}F\Big)=\det\begin{pmatrix}1+\tfrac{i}{2\pi}F_1&0\\0&1+\tfrac{i}{2\pi}F_2\end{pmatrix}=\det\!\Big(1+\tfrac{i}{2\pi}F_1\Big)\cdot\det\!\Big(1+\tfrac{i}{2\pi}F_2\Big)\qquad\text{(block-diagonal determinant, Lemma 3)}.$$
> The right-hand product is the wedge product of the two even forms $c(F_1)\wedge c(F_2)$ (multiplication in $\Omega^{\mathrm{even}}(M)$ *is* the wedge product). Passing to cohomology and using that the cup product on [[Def - de Rham Cohomology|de Rham cohomology]] is induced by the wedge, $c(E_1\oplus E_2)=[c(F_1)\wedge c(F_2)]=[c(F_1)]\smile[c(F_2)]=c(E_1)\smile c(E_2)$. (The connection $\nabla_1\oplus\nabla_2$ is used only to compute a representative; the class is connection-independent by Chern–Weil.)
>
> **Property (iv) — normalisation.** The bundle $\mathcal O(-1)\to\mathbb{CP}^1$ is a line bundle, so by Lemma 1 its total Chern class is $c(\mathcal O(-1))=1+c_1(\mathcal O(-1))$. The value of the first Chern class is the normalisation computed on the [[Thm - First Chern Class of a Line Bundle from Curvature|first-Chern-from-curvature theorem]], whose part (a) states: for a Hermitian line bundle $L$ with unitary connection of curvature $F_\nabla$, $c_1(L)=[\tfrac{i}{2\pi}F_\nabla]$ equals the topological first Chern class, and for $\mathcal O(-1)\to\mathbb{CP}^1$ with the connection induced by the Hopf connection, $\int_{\mathbb{CP}^1}\tfrac{i}{2\pi}F=-1$. Since $\int_{\mathbb{CP}^1}[\omega_1]=1$ and integration is an isomorphism $H^2_{\mathrm{dR}}(\mathbb{CP}^1)\xrightarrow{\ \sim\ }\mathbb R$, the class with integral $-1$ is $c_1(\mathcal O(-1))=-[\omega_1]$. Therefore $c(\mathcal O(-1))=1-[\omega_1]$, which is Haydys's "$1-a$" under the identification $a\mapsto[\omega_1]$ of the Convention callout.
>
> **Property (v) — isomorphism invariance.** This is part (b) of the [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes|naturality and isomorphism-invariance theorem]]: if $\phi\colon P\to P'$ is an isomorphism of principal $G$-bundles over $M$ then $c_p(P)=c_p(P')$ for every invariant polynomial $p$. Applied to $G=U(r)$ and the unitary frame bundles, an isomorphism $E\cong E'$ of complex vector bundles induces an isomorphism of unitary frame bundles (after transporting the Hermitian structure), so $c_j(E)=c_j(E')$ for all $j$, hence $c(E)=c(E')$. Equivalently, an isomorphism transports a unitary connection on $E$ to one on $E'$ whose curvature is the conjugate $\phi F\phi^{-1}$, and $\det(1+\tfrac{i}{2\pi}\phi F\phi^{-1})=\det(1+\tfrac{i}{2\pi}F)$ by multiplicativity and $\det(\phi)\det(\phi^{-1})=1$ (Lemma 3), so the Chern forms agree.
>
> **Property (vi) — dual bundle.** Equip $E^\vee$ with the dual Hermitian structure and the dual connection, whose curvature is $F^\vee=-F^t$ by Lemma 2(b). Then, using Lemma 3 (transpose-invariance) and Lemma 1 (homogeneity),
> $$\det\!\Big(1+\tfrac{i}{2\pi}F^\vee\Big)=\det\!\Big(1-\tfrac{i}{2\pi}F^t\Big)=\det\!\Big(\big(1-\tfrac{i}{2\pi}F\big)^{t}\Big)=\det\!\Big(1-\tfrac{i}{2\pi}F\Big)=\sum_{j}c_j(-F)=\sum_j(-1)^jc_j(F).$$
> Comparing degree-$2j$ components gives $c_j(F^\vee)=(-1)^jc_j(F)$; taking classes, $c_j(E^\vee)=(-1)^jc_j(E)$. (For $r=1$ this recovers $c_1(L^\vee)=-c_1(L)$, Haydys's Theorem 77(iii).)
>
> **Property (vii) — trivial and split-off-trivial bundles.** If $E$ is trivial, it admits the flat product connection, whose curvature is $F=0$; then $\det(1+\tfrac{i}{2\pi}\cdot0)=\det(1)=1$, so $c_j(F)=0$ for $j\ge1$ and $c(E)=1$. (This is the specialisation to $U(r)$ and $p=c_j$ of the [[Thm - Trivial Bundles Have Vanishing Characteristic Classes|vanishing theorem for trivial bundles]], whose statement is: if $P$ is trivial and $\deg p=d\ge1$ then $c_p(P)=0$.) For the second assertion, suppose $E\cong E_1\oplus\underline{\mathbb C}^k$. By isomorphism invariance (v) and the Whitney formula (iii), $c(E)=c(E_1)\smile c(\underline{\mathbb C}^k)$; and $c(\underline{\mathbb C}^k)=1$ by the trivial case just proved, so $c(E)=c(E_1)$. Now $\operatorname{rk}E_1=\operatorname{rk}E-k$, and by property (i) (the "$c_j=0$ for $j>\operatorname{rk}$" clause of Lemma 1) $c_j(E_1)=0$ for $j>\operatorname{rk}E_1=\operatorname{rk}E-k$. Therefore $c_j(E)=c_j(E_1)=0$ for all $j>\operatorname{rk}E-k$.
>
> **Property (viii) — line bundles and the determinant line.** For line bundles $L_1,L_2$ with unitary connections of curvatures $F_1,F_2$, the tensor connection on $L_1\otimes L_2$ has curvature $F_1+F_2$ by Lemma 2(c). Since $L_1\otimes L_2$ is a line bundle, $c_1(L_1\otimes L_2)=\big[\tfrac{i}{2\pi}\operatorname{tr}(F_1+F_2)\big]=\big[\tfrac{i}{2\pi}(F_1+F_2)\big]=\big[\tfrac{i}{2\pi}F_1\big]+\big[\tfrac{i}{2\pi}F_2\big]=c_1(L_1)+c_1(L_2)$, using $c_1(F)=\tfrac{i}{2\pi}\operatorname{tr}F$ from Lemma 1 and that trace on $1\times1$ matrices is the identity. (This is Haydys's Theorem 77(ii).) For the determinant line, let $E$ have rank $r$ and let $F$ be the curvature of a unitary connection on $E$. By Lemma 2(d) the induced connection on $\Lambda^rE$ has curvature $\operatorname{tr}F$, so, again by Lemma 1,
> $$c_1(\Lambda^rE)=\Big[\tfrac{i}{2\pi}\operatorname{tr}(\operatorname{tr}F)\Big]=\Big[\tfrac{i}{2\pi}\operatorname{tr}F\Big]=c_1(E),$$
> where the middle equality holds because $\operatorname{tr}F$ is already the ($1\times1$) curvature of the line bundle $\Lambda^rE$, so its own trace is itself, and the last equality is the definition of $c_1(E)$ as $[\tfrac{i}{2\pi}\operatorname{tr}F]$.
>
> **Property (ix) — curvature detects a circle bundle over a surface.** Let $P\to\Sigma$ be a principal $U(1)$-bundle over a closed oriented surface, equivalently a Hermitian line bundle $L\to\Sigma$, with curvature $\bar\Omega=F_\nabla\in\Omega^2(\Sigma;i\mathbb R)$; then $c_1(P)=[\tfrac{i}{2\pi}\bar\Omega]\in H^2_{\mathrm{dR}}(\Sigma;\mathbb R)$. Suppose, for the contrapositive, that $P$ is trivial. By the trivial-bundle case of (vii), $c_1(P)=0$, so the real closed $2$-form $\tfrac{i}{2\pi}\bar\Omega$ is exact: $\tfrac{i}{2\pi}\bar\Omega=d\eta$ for some $\eta\in\Omega^1(\Sigma;\mathbb R)$ (exactness is the definition of the zero class in $H^2_{\mathrm{dR}}$). Integrating over $\Sigma$ and applying [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — for a smooth form $\eta$ on a compact oriented manifold with boundary, $\int_\Sigma d\eta=\int_{\partial\Sigma}\eta$ — with $\partial\Sigma=\varnothing$ (the surface is closed), we get
> $$\frac{i}{2\pi}\int_\Sigma\bar\Omega=\int_\Sigma d\eta=\int_{\partial\Sigma}\eta=0\qquad\text{(Stokes, closed surface)},$$
> hence $\int_\Sigma\bar\Omega=0$. By contraposition, if $\int_\Sigma\bar\Omega\neq0$ then $P$ (respectively $L$) is not trivial.
>
> This proves (i)–(iv), the consequences (v)–(viii), and the detection statement (ix). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebraic geometry — the degree of a divisor on a Riemann surface.** On a compact Riemann surface $\Sigma$, a divisor $D=\sum n_pp$ determines a holomorphic line bundle $\mathcal O(D)$, and its degree $\deg D=\sum n_p$ equals $\int_\Sigma c_1(\mathcal O(D))$. Property (viii) is exactly what makes the assignment $D\mapsto\int_\Sigma c_1(\mathcal O(D))$ additive under addition of divisors (tensor product of line bundles), and property (ix) is what forces the answer to be an integer. The theorem here is the differential-geometric shadow of the statement that $\deg$ is a homomorphism $\operatorname{Pic}(\Sigma)\to\mathbb Z$; the application is non-obvious because divisors are combinatorial data while Chern classes are curvature integrals, and only the additivity (viii) bridges them.

**Condensed matter physics — the Chern number of a band structure.** For a gapped two-dimensional crystal the occupied Bloch states form a Hermitian vector bundle over the Brillouin torus $T^2$, and the quantised Hall conductance is $\tfrac{e^2}{h}$ times the Chern number $\int_{T^2}c_1$. Property (ix) is the statement that this number cannot change continuously — a non-zero curvature integral is a topological obstruction — and the Whitney formula (iii) is what lets one add the contributions of several bands. The application is non-obvious because the physical input is a family of Hamiltonians, and recognising that it assembles into a bundle whose $c_1$ is the observable is the entire step.

**Representation theory — Chern classes of homogeneous bundles.** Over a flag manifold $G/P$ every irreducible representation of $P$ induces a homogeneous vector bundle, and its Chern classes are computed by the splitting principle: pull back to a maximal torus where the bundle splits into line bundles indexed by weights, use additivity (viii) and the Whitney formula (iii), and descend. The theorem here supplies precisely the two ingredients — additivity of $c_1$ on line bundles and multiplicativity of $c$ on sums — that make Weyl-character-style computations of Chern classes purely combinatorial. The application is non-obvious because it converts a question about curvature into one about weights of a representation.

---

# Bridges

- **The splitting principle.** The Whitney formula (iii) together with the additivity (viii) is the analytic content behind the splitting principle: to prove an identity among Chern classes one may assume every bundle is a direct sum of line bundles, because pulling back to a flag bundle makes it so and the pull-back is injective on cohomology (property (ii) and the Leray–Hirsch structure of the flag bundle). Every polynomial identity among Chern classes — the formula for $c(E\otimes F)$, the Chern character being a ring homomorphism — is proved by reducing through this bridge to the line-bundle case, where (viii) does all the work.

- **From $c_1$ over surfaces to $c_2$ over four-manifolds.** Property (ix) is the two-dimensional instance of a mechanism that recurs one dimension up. Over a closed oriented four-manifold the second Chern number $\tfrac1{8\pi^2}\int_M\operatorname{tr}(F\wedge F)$ is an integer, and the proof of that integrality (chapter §6.2, `Thm - First Chern Class of a Line Bundle from Curvature` and Remark 93/(94) of Haydys) runs the same Stokes-and-exactness argument on a $4$-manifold that (ix) runs on a surface. This is the bridge from the present page to the [[Def - Chern-Simons Functional|Chern–Simons functional]] and the instanton number of §6.4.

- **The Euler class comparison.** For an oriented real rank-$2$ bundle, viewed as a Hermitian line bundle, the Euler class equals the first Chern class, $e(E)=c_1(E)$; this identification (Bär's Example 2.5.15) uses the normalisation fixed here in (iv) to match signs. More generally the top Chern class $c_r(E)$ of a rank-$r$ complex bundle equals the Euler class of its underlying oriented real rank-$2r$ bundle, so the vanishing statements (vii) about top Chern classes become vanishing statements about Euler classes, hence about the existence of nowhere-vanishing sections. This is the bridge from §6.2 to the Euler class of §6.3.

- **Naturality as a functor.** Property (ii) says $c$ is a natural transformation from the functor "isomorphism classes of complex vector bundles" to the functor $H^{\mathrm{even}}_{\mathrm{dR}}(-;\mathbb R)$; combined with the homotopy invariance of pull-back (homotopic maps pull back isomorphic bundles), it shows $c(E)$ depends only on the homotopy class of the classifying map of $E$. This is the bridge to the classifying-space description of characteristic classes and to the fact — used implicitly throughout — that a Chern class is a homotopy invariant of the base together with the bundle data.

---

# Unlocked by This

> [!tip] The Chern character and the Riemann–Roch theorem *(from Algebraic Geometry / Index Theory)*
> The additivity and multiplicativity proved here let one define the Chern character $\operatorname{ch}(E)=\operatorname{tr}\exp(\tfrac{i}{2\pi}F)$, which satisfies $\operatorname{ch}(E\oplus F)=\operatorname{ch}(E)+\operatorname{ch}(F)$ and $\operatorname{ch}(E\otimes F)=\operatorname{ch}(E)\smile\operatorname{ch}(F)$ — a ring homomorphism from $K$-theory to cohomology. It is the coefficient in the Hirzebruch–Riemann–Roch and Atiyah–Singer index formulas.

> [!tip] Chern classes of the tangent bundle of projective space *(from Complex Geometry)*
> Using (ii), (iii), (iv), and (vi) on the Euler sequence gives $c(T\mathbb{CP}^n)=(1+[\omega_1])^{n+1}$, so $c_1(T\mathbb{CP}^n)=(n+1)[\omega_1]$ and the top Chern (Euler) number is $\int_{\mathbb{CP}^n}c_n(T\mathbb{CP}^n)=n+1=\chi(\mathbb{CP}^n)$. This computation is carried out as a target of the present theorem.
