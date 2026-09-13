---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Chern Classes"
  - "Def - Induced Connections on Dual, Hom, and Endomorphism Bundles"
  - "Thm - Chern-Weil Theorem"
  - "Thm - Naturality and Isomorphism Invariance of Characteristic Classes"
  - "Thm - Axioms and Properties of Chern Classes"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ be a complex vector bundle of rank $r$ over a smooth manifold $M$, with dual bundle $E^{\vee}:=\operatorname{Hom}(E,\underline{\mathbb{C}})$ (the bundle whose fibre over $m$ is the space $E_m^{*}$ of $\mathbb{C}$-linear functionals on $E_m$) and conjugate bundle $\overline{E}$ (the same underlying real bundle with the complex structure $I$ replaced by $-I$). Prove Haydys' Exercise 88(b) together with its two Hermitian companions:

- **(b) The dual bundle.** $c_j(E^{\vee})=(-1)^{j}\,c_j(E)$ for all $j$; equivalently $c(E^{\vee})=\sum_{j}(-1)^{j}c_j(E)$.
- **The conjugate bundle.** $c_j(\overline{E})=(-1)^{j}\,c_j(E)$ for all $j$.
- **The comparison.** If $E$ carries a Hermitian structure then $E^{\vee}\cong\overline{E}$ as complex vector bundles, which makes the second identity a corollary of the first.

The route named by the spec is: compute the curvature of the induced connection on $E^{\vee}$ (its connection matrix is $-A^{t}$, so its curvature is $-F^{t}$), read off $\det\!\big(1-\tfrac{i}{2\pi}F\big)=\sum_j(-1)^jc_j(F)$, then obtain the conjugate case from the natural isomorphism $E^{\vee}\cong\overline{E}$ available once a Hermitian metric is fixed.

**Recall:**

The objects in play are the Chern classes defined from curvature, the induced connection on the dual bundle, the Chern–Weil independence of the connection, and the multiplicativity and transpose-invariance of determinants of matrices of even-degree forms.

![[Def - Chern Classes#The Definition]]

For a complex vector bundle $E$ of rank $r$ with a connection $\nabla$ of curvature $F\in\Omega^2(M;\operatorname{End}E)$, the total Chern class is $c(E)=\big[\det(1+\tfrac{i}{2\pi}F)\big]$ and $c_j(E)=[c_j(F)]$ is the class of the degree-$j$ part $c_j(F)$ of $\det(1+\tfrac{i}{2\pi}F)$, a closed real-valued $2j$-form. In a local frame $e=(e_1,\dots,e_r)$ the curvature is represented by the matrix of $2$-forms $F=dA+A\wedge A$, where $A\in\Omega^1(U;\mathfrak{gl}_r(\mathbb{C}))$ is the connection matrix ($\nabla e=e\cdot A$, series convention). The page **[[Def - Chern Classes]]** proves the class is independent of the connection and of the Hermitian structure.

![[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles#The Definition]]

The **[[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles|induced connection on the dual bundle]]** $\nabla^{\vee}$ on $E^{\vee}$ is the unique connection satisfying the Leibniz rule against the canonical pairing $\langle\cdot,\cdot\rangle\colon E^{\vee}\otimes E\to\underline{\mathbb{C}}$:
$$d\,\langle\xi,s\rangle=\langle\nabla^{\vee}\xi,s\rangle+\langle\xi,\nabla s\rangle\qquad(\xi\in\Gamma(E^{\vee}),\ s\in\Gamma(E)).$$
That page proves this determines $\nabla^{\vee}$ and that, in the dual coframe $e^{*}=(e^{1},\dots,e^{r})$ of a frame $e$ with connection matrix $A$, the connection matrix of $\nabla^{\vee}$ is $A^{\vee}=-A^{t}$.

![[Thm - Chern-Weil Theorem#Statement]]

The **[[Thm - Chern-Weil Theorem|Chern–Weil theorem]]** guarantees that $c_j(F)$ is closed and that its de Rham class is independent of the chosen connection; this is what lets us compute $c(E^{\vee})$ and $c(\overline{E})$ using whichever induced connection is convenient. We also use, from **[[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]**, that matrices whose entries are even-degree differential forms have commuting entries, so their determinants are well defined, multiplicative, and transpose-invariant, $\det(N^{t})=\det(N)$, exactly as for scalar matrices.

The bridge that runs the whole page is a single algebraic identity, once the curvature of the dual connection is known: writing $\det(1+\tfrac{i}{2\pi}\xi)=\sum_j c_j(\xi)$ with $c_j$ homogeneous of degree $j$, the substitution $\xi\mapsto-\xi$ multiplies the degree-$j$ term by $(-1)^{j}$.

---

# Convergent Strategy

**Problem class.** This is a *transport-a-connection-and-track-the-curvature* problem. The Chern class of a derived bundle ($E^{\vee}$, $\overline{E}$, $E_1\oplus E_2$, $E_1\otimes E_2$) is computed by equipping the derived bundle with the *induced* connection, whose curvature is an explicit algebraic operation applied to the curvature of $E$; the answer is then read off the Chern polynomial. For the dual bundle the operation is $F\mapsto-F^{t}$, and everything reduces to how $\det(1+\tfrac{i}{2\pi}\cdot)$ behaves under negation and transpose.

**Assumption pattern.** The rank-$r$ complex bundle $E$ comes with a connection $\nabla$; the recognisable trigger is that the dual bundle inherits a *canonical* induced connection $\nabla^{\vee}$ (no new choice is made), and the Chern–Weil theorem lets us compute $c(E^{\vee})$ with that particular connection while knowing the answer is connection-independent. The conjugate-bundle claim adds the hypothesis of a Hermitian structure, whose only role is to furnish the conjugate-linear isomorphism $E\to E^{*}$.

**Theorem routing.** For (b): take the induced connection $\nabla^{\vee}$ on $E^{\vee}$; quote from **[[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]]** that its connection matrix is $-A^{t}$; compute its curvature $F^{\vee}=-F^{t}$; then $\det(1+\tfrac{i}{2\pi}F^{\vee})=\det(1-\tfrac{i}{2\pi}F^{t})=\det(1-\tfrac{i}{2\pi}F)$ (transpose-invariance from **[[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]**) $=\sum_j(-1)^jc_j(F)$ (homogeneity); pass to classes with **[[Thm - Chern-Weil Theorem]]**. For the conjugate bundle: build the metric isomorphism $\overline{E}\cong E^{\vee}$ and apply isomorphism invariance from **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]** together with (b).

**Key decision point.** Two moves carry the argument. First, *computing the curvature of the dual connection correctly*: the connection matrix is the plain transpose-negative $-A^{t}$ (not the conjugate-transpose), and one must track that transposition reverses the order of a wedge of matrix-valued forms, $(A\wedge A)^{t}=-A^{t}\wedge A^{t}$, or the sign of the quadratic term comes out wrong. Second, *seeing that the conjugate bundle need not be recomputed*: rather than differentiate a conjugated connection (which invites confusion about whether the normalising $i$ conjugates too), one proves $\overline{E}\cong E^{\vee}$ from the metric and lets isomorphism invariance transport (b) to $\overline{E}$.

---

# Legal Operations Used

This solution deploys the following legal operations from **[[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional#Legal Operations|the topic page's Legal Operations]]** (numbering to be reconciled when the topic page is assembled):

1. **Equip a derived bundle with its induced connection.** On $E^{\vee}$ use the canonical $\nabla^{\vee}$ characterised by the Leibniz rule against the pairing $\langle\cdot,\cdot\rangle$; from **[[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]]** its connection matrix is $-A^{t}$.

2. **Compute the curvature of the induced connection algebraically.** From $A^{\vee}=-A^{t}$ obtain $F^{\vee}=dA^{\vee}+A^{\vee}\wedge A^{\vee}=-F^{t}$, using that transposition reverses wedge order on matrix-valued $1$-forms.

3. **Apply the Chern polynomial to the derived curvature.** Substitute $F^{\vee}=-F^{t}$ into $\det(1+\tfrac{i}{2\pi}\cdot)$.

4. **Use transpose-invariance and multiplicativity of determinants of even-form matrices.** From **[[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]**, $\det(N^{t})=\det(N)$ for a matrix $N$ of even-degree forms.

5. **Use homogeneity of the Chern polynomial.** $c_j$ is homogeneous of degree $j$, so $c_j(-F)=(-1)^{j}c_j(F)$.

6. **Pass from forms to classes via connection-independence.** Quote **[[Thm - Chern-Weil Theorem]]** to conclude $c_j(E^{\vee})=[c_j(F^{\vee})]$ regardless of which connection defines $c_j(E^{\vee})$.

7. **Construct the metric isomorphism $\overline{E}\cong E^{\vee}$ and transport by isomorphism invariance.** A Hermitian structure gives a conjugate-linear isomorphism $E\to E^{*}$, hence a $\mathbb{C}$-linear isomorphism $\overline{E}\to E^{\vee}$; apply **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]** with (b) to get $c_j(\overline{E})=(-1)^{j}c_j(E)$.

---

# Hints

> [!note]- Hint 1
> The Chern class of a bundle built from $E$ is computed by giving that bundle its *induced* connection and finding what algebraic operation the induction performs on the curvature. For the dual bundle, what is the connection matrix of the induced connection in terms of $A$?

> [!note]- Hint 2
> The induced connection $\nabla^{\vee}$ on $E^{\vee}$ has connection matrix $A^{\vee}=-A^{t}$ (from [[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]]). Compute its curvature $F^{\vee}=dA^{\vee}+A^{\vee}\wedge A^{\vee}$. Be careful: transposing a product of matrix-valued $1$-forms reverses the order *and* the wedge of two $1$-forms is anti-commutative, so $(A\wedge A)^{t}=-A^{t}\wedge A^{t}$. You should land on $F^{\vee}=-F^{t}$.

> [!note]- Hint 3
> Now feed $F^{\vee}=-F^{t}$ into $\det(1+\tfrac{i}{2\pi}\cdot)$. Use $\det(N^{t})=\det(N)$ (valid because the entries are even-degree forms and commute) to drop the transpose, then use that $c_j$ is homogeneous of degree $j$ to see how the sign of $-F$ propagates.

> [!note]- Hint 4
> For the conjugate bundle, resist recomputing. A Hermitian metric $h$ gives a map $E\to E^{*}$, $v\mapsto h(\cdot,v)$, which is *conjugate-linear* in $v$. A conjugate-linear isomorphism $E\to E^{*}$ is the same thing as a $\mathbb{C}$-linear isomorphism $\overline{E}\to E^{*}=E^{\vee}$. With $\overline{E}\cong E^{\vee}$ in hand, isomorphism invariance turns part (b) into the conjugate statement.

---

# Solution

The dual bundle inherits a canonical connection whose curvature is $-F^{t}$, and the Chern polynomial is transpose-blind and degree-$j$ homogeneous, so passing to the dual sends each $c_j$ to $(-1)^{j}c_j$. The conjugate bundle is handled without a second curvature computation: a Hermitian metric identifies $\overline{E}$ with $E^{\vee}$, so isomorphism invariance carries the dual result across.

**Step 1: The induced connection on $E^{\vee}$ has connection matrix $-A^{t}$.**

Let $\nabla$ be a connection on $E$ with connection matrix $A\in\Omega^1(U;\mathfrak{gl}_r(\mathbb{C}))$ in a local frame $e$. The induced connection $\nabla^{\vee}$ on $E^{\vee}$ has connection matrix $A^{\vee}=-A^{t}$ in the dual coframe $e^{*}$.

> [!note]- Derivation
> We must recover the dual connection matrix from the defining Leibniz rule; the page **[[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]]** proves existence and uniqueness of $\nabla^{\vee}$, and we restate the local computation to keep this page self-contained.
>
> **Set up the frames and pairing.** Let $e=(e_1,\dots,e_r)$ be a local frame of $E$ over $U$ and $e^{*}=(e^{1},\dots,e^{r})$ its dual coframe, characterised by the constant pairings $\langle e^{i},e_k\rangle=\delta^{i}_{k}$. The series convention writes the connection matrix through the right action on the frame row, $\nabla e=e\cdot A$, that is $\nabla e_k=\sum_{m}e_m\,A^{m}{}_{k}$ (so $A=(A^{m}{}_{k})$, with $A^m{}_k$ the entry in row $m$, column $k$). To stay in the same convention we define the dual connection matrix by the identical right action on the coframe row, $\nabla^{\vee}e^{*}=e^{*}\cdot A^{\vee}$, whose $i$-th entry is $\nabla^{\vee}e^{i}=\sum_{m}e^{m}\,(A^{\vee})^{m}{}_{i}$ for the unknown matrix $A^{\vee}=((A^{\vee})^{m}{}_{i})$. Keeping both matrices in the *same* row convention is exactly what will make the transpose appear; had we instead written $\nabla^{\vee}e^{i}=\sum_{k}(A^{\vee})^{i}{}_{k}e^{k}$ we would be using a different convention for the two frames and would land on $-A$, not $-A^{t}$.
> **Apply the Leibniz rule to the constant pairing.** Since $\langle e^{i},e_k\rangle=\delta^{i}_{k}$ is a constant function, $d\langle e^{i},e_k\rangle=0$. The defining Leibniz rule gives
> $$0=d\langle e^{i},e_k\rangle=\langle\nabla^{\vee}e^{i},e_k\rangle+\langle e^{i},\nabla e_k\rangle\qquad\text{(Leibniz rule for the induced dual connection).}$$
> **Evaluate the two pairings.** Using bilinearity of $\langle\cdot,\cdot\rangle$ over forms and $\langle e^{m},e_k\rangle=\delta^{m}_{k}$,
> $$\langle\nabla^{\vee}e^{i},e_k\rangle=\sum_{m}(A^{\vee})^{m}{}_{i}\langle e^{m},e_k\rangle=(A^{\vee})^{k}{}_{i},\qquad
> \langle e^{i},\nabla e_k\rangle=\sum_{m}A^{m}{}_{k}\langle e^{i},e_m\rangle=A^{i}{}_{k}.$$
> **Solve.** Substituting, $0=(A^{\vee})^{k}{}_{i}+A^{i}{}_{k}$, so $(A^{\vee})^{k}{}_{i}=-A^{i}{}_{k}$ for all $i,k$. Read as a statement about matrix entries, the entry of $A^{\vee}$ in row $k$, column $i$ equals minus the entry of $A$ in row $i$, column $k$; since $(A^{t})^{k}{}_{i}=A^{i}{}_{k}$, this is precisely
> $$A^{\vee}=-A^{t}\qquad\big((A^{\vee})^{k}{}_{i}=-A^{i}{}_{k}=-(A^{t})^{k}{}_{i}\text{ for all }k,i\big).$$
> This is the local formula recorded on **[[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]]**.

**Step 2: The curvature of $\nabla^{\vee}$ is $F^{\vee}=-F^{t}$.**

From $A^{\vee}=-A^{t}$ and the local curvature formula, the curvature matrix of $\nabla^{\vee}$ is minus the transpose of the curvature matrix of $\nabla$.

> [!note]- Derivation
> We compute $F^{\vee}=dA^{\vee}+A^{\vee}\wedge A^{\vee}$ and compare with $F=dA+A\wedge A$.
>
> **Record the transpose rule for matrix-valued $1$-forms.** For matrices $\alpha,\beta$ of $1$-forms, the $(i,k)$ entry of $\alpha\wedge\beta$ is $\sum_m\alpha^{i}{}_{m}\wedge\beta^{m}{}_{k}$; the $(i,k)$ entry of $(\alpha\wedge\beta)^{t}$ is $\sum_m\alpha^{k}{}_{m}\wedge\beta^{m}{}_{i}$, while the $(i,k)$ entry of $\beta^{t}\wedge\alpha^{t}$ is $\sum_m\beta^{m}{}_{i}\wedge\alpha^{k}{}_{m}$. Since $1$-forms anti-commute under the wedge, $\alpha^{k}{}_{m}\wedge\beta^{m}{}_{i}=-\beta^{m}{}_{i}\wedge\alpha^{k}{}_{m}$, hence
> $$(\alpha\wedge\beta)^{t}=-\,\beta^{t}\wedge\alpha^{t}\qquad\text{(transposition reverses order and, for }1\text{-forms, contributes a sign).}$$
> In particular $(A\wedge A)^{t}=-A^{t}\wedge A^{t}$.
> **Differentiate the dual connection matrix.** Exterior differentiation commutes with taking the transpose entrywise, so $d(A^{\vee})=d(-A^{t})=-dA^{t}=-(dA)^{t}$.
> **Assemble the curvature.**
> $$F^{\vee}=dA^{\vee}+A^{\vee}\wedge A^{\vee}=-(dA)^{t}+(-A^{t})\wedge(-A^{t})=-(dA)^{t}+A^{t}\wedge A^{t}\qquad\text{(Step 1 and }d(A^{\vee})=-(dA)^{t}).$$
> **Recognise the transpose of $F$.** Using $(A\wedge A)^{t}=-A^{t}\wedge A^{t}$, that is $A^{t}\wedge A^{t}=-(A\wedge A)^{t}$,
> $$F^{\vee}=-(dA)^{t}-(A\wedge A)^{t}=-\big(dA+A\wedge A\big)^{t}=-F^{t}\qquad\text{(collecting the transpose; }F=dA+A\wedge A).$$
> Thus $F^{\vee}=-F^{t}$. (The sign of the quadratic term is exactly what makes the answer the clean $-F^{t}$: had one forgotten that transposition reverses the wedge order, the term $A^{t}\wedge A^{t}$ would have carried the wrong sign.)

**Step 3: $c_j(E^{\vee})=(-1)^{j}c_j(E)$.**

Substituting $F^{\vee}=-F^{t}$ into the Chern polynomial and using transpose-invariance of the determinant and homogeneity of $c_j$ gives the sign.

> [!note]- Derivation
> We compute the total Chern form of $\nabla^{\vee}$ and match degrees.
>
> **Substitute the dual curvature.** By definition the total Chern form of $\nabla^{\vee}$ is
> $$\det\!\Big(1+\tfrac{i}{2\pi}F^{\vee}\Big)=\det\!\Big(1+\tfrac{i}{2\pi}(-F^{t})\Big)=\det\!\Big(1-\tfrac{i}{2\pi}F^{t}\Big)\qquad\text{(Step 2, }F^{\vee}=-F^{t}).$$
> **Drop the transpose.** The matrix $1-\tfrac{i}{2\pi}F^{t}=\big(1-\tfrac{i}{2\pi}F\big)^{t}$ has entries that are even-degree forms ($0$-forms on the diagonal, $2$-forms off it), which commute; by **[[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]** the determinant of such a matrix equals the determinant of its transpose, so
> $$\det\!\Big(1-\tfrac{i}{2\pi}F^{t}\Big)=\det\!\Big(\big(1-\tfrac{i}{2\pi}F\big)^{t}\Big)=\det\!\Big(1-\tfrac{i}{2\pi}F\Big)\qquad\text{(transpose-invariance of }\det\text{ on even-form matrices).}$$
> **Expand by degree and apply homogeneity.** Writing $\det(1+\tfrac{i}{2\pi}\xi)=\sum_{j=0}^{r}c_j(\xi)$ with $c_j$ homogeneous of degree $j$, we substitute $\xi=-F$:
> $$\det\!\Big(1-\tfrac{i}{2\pi}F\Big)=\sum_{j=0}^{r}c_j(-F)=\sum_{j=0}^{r}(-1)^{j}c_j(F)\qquad\text{(homogeneity: }c_j(-F)=(-1)^{j}c_j(F)).$$
> **Match degrees and pass to cohomology.** The left-hand side, being the total Chern form of $\nabla^{\vee}$, has degree-$j$ part $c_j(F^{\vee})$; the right-hand side has degree-$j$ part $(-1)^{j}c_j(F)$. Equating the degree-$2j$ components,
> $$c_j(F^{\vee})=(-1)^{j}c_j(F)\qquad\text{(equality of the degree-}2j\text{ forms).}$$
> By **[[Thm - Chern-Weil Theorem]]**, $c_j(E^{\vee})=[c_j(F^{\vee})]$ for the induced connection (its class is connection-independent), and $c_j(E)=[c_j(F)]$; taking de Rham classes,
> $$c_j(E^{\vee})=(-1)^{j}c_j(E)\qquad(j=0,1,\dots,r).$$
> This is part (b).

**Step 4: For Hermitian $E$, $E^{\vee}\cong\overline{E}$.**

A Hermitian structure furnishes a conjugate-linear fibrewise isomorphism $E\to E^{*}$, which is the same as a $\mathbb{C}$-linear isomorphism $\overline{E}\to E^{\vee}$.

> [!note]- Derivation
> We construct the isomorphism and check it is $\mathbb{C}$-linear as a map out of the conjugate bundle.
>
> **Use the metric to map $E$ into $E^{*}$.** Fix a Hermitian structure $h$ on $E$, with $h_m(\cdot,\cdot)$ linear in the first slot and conjugate-linear in the second. Define fibrewise
> $$\Psi_m\colon E_m\to E_m^{*},\qquad \Psi_m(v):=h_m(\,\cdot\,,v)\quad\text{(the functional }w\mapsto h_m(w,v)).$$
> **Check the linearity type.** For $w\in E_m$ the value $\Psi_m(v)(w)=h_m(w,v)$ is linear in $w$, so $\Psi_m(v)\in E_m^{*}$ is indeed a $\mathbb{C}$-linear functional. In the argument $v$, conjugate-linearity of $h_m$ in its second slot gives
> $$\Psi_m(\lambda v)=h_m(\,\cdot\,,\lambda v)=\overline{\lambda}\,h_m(\,\cdot\,,v)=\overline{\lambda}\,\Psi_m(v)\qquad(\lambda\in\mathbb{C}),$$
> so $\Psi_m$ is **conjugate-linear** in $v$, and additive.
> **Check bijectivity.** $\Psi_m$ is injective: if $\Psi_m(v)=0$ then $h_m(w,v)=0$ for all $w$, in particular $h_m(v,v)=0$, so $v=0$ by positive definiteness. Since $\dim_{\mathbb{C}}E_m=\dim_{\mathbb{C}}E_m^{*}=r$ and a conjugate-linear injection between complex vector spaces of equal finite dimension is a real-linear injection between real spaces of equal dimension $2r$, it is a bijection. Smooth dependence on $m$ follows from smoothness of $h$.
> **Reinterpret as a map out of $\overline{E}$.** By definition of the conjugate bundle, scalar multiplication on $\overline{E}$ is $\lambda\cdot_{\overline{E}}v=\overline{\lambda}\,v$. A conjugate-linear map $\Psi\colon E\to E^{*}$ therefore satisfies $\Psi(\lambda\cdot_{\overline{E}}v)=\Psi(\overline{\lambda}v)=\lambda\,\Psi(v)$, i.e. $\Psi$ is $\mathbb{C}$-**linear** as a map $\overline{E}\to E^{*}=E^{\vee}$. Being fibrewise bijective and smooth over $\mathrm{id}_M$, it is an isomorphism of complex vector bundles,
> $$\overline{E}\ \cong\ E^{\vee}.$$

**Step 5: $c_j(\overline{E})=(-1)^{j}c_j(E)$.**

Isomorphism invariance combined with part (b) gives the conjugate identity.

> [!note]- Derivation
> Every complex vector bundle admits a Hermitian structure, so Step 4 applies to $E$ (choosing any Hermitian structure changes neither $\overline{E}$ nor its Chern classes). By **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]** — restated: *isomorphic complex vector bundles have equal Chern classes* — the isomorphism $\overline{E}\cong E^{\vee}$ of Step 4 gives
> $$c_j(\overline{E})=c_j(E^{\vee})\qquad\text{(isomorphism invariance).}$$
> Combining with Step 3, $c_j(E^{\vee})=(-1)^{j}c_j(E)$,
> $$c_j(\overline{E})=(-1)^{j}c_j(E)\qquad(j=0,1,\dots,r).$$
> This proves the conjugate-bundle identity.

> [!note]- Complete formal solution
> **Claim.** For a complex vector bundle $E\to M$ of rank $r$: $c_j(E^{\vee})=(-1)^{j}c_j(E)$; if $E$ is Hermitian then $E^{\vee}\cong\overline{E}$ and $c_j(\overline{E})=(-1)^{j}c_j(E)$, for all $j$.
>
> **Dual bundle.** Let $\nabla$ be a connection on $E$ with connection matrix $A$ in a local frame $e$. The induced connection $\nabla^{\vee}$ on $E^{\vee}$ has, in the dual coframe with the same right-action convention $\nabla^{\vee}e^{*}=e^{*}\cdot A^{\vee}$, connection matrix $A^{\vee}=-A^{t}$: applying the Leibniz rule to $\langle e^{i},e_k\rangle=\delta^{i}_{k}$ (constant) gives $(A^{\vee})^{k}{}_{i}+A^{i}{}_{k}=0$, i.e. $(A^{\vee})^{k}{}_{i}=-(A^{t})^{k}{}_{i}$. Its curvature is
> $$F^{\vee}=dA^{\vee}+A^{\vee}\wedge A^{\vee}=-(dA)^{t}+A^{t}\wedge A^{t}=-\big(dA+A\wedge A\big)^{t}=-F^{t},$$
> using $(A\wedge A)^{t}=-A^{t}\wedge A^{t}$ (transposition reverses the wedge order of matrix-valued $1$-forms, contributing a sign). Hence
> $$\det\!\Big(1+\tfrac{i}{2\pi}F^{\vee}\Big)=\det\!\Big(1-\tfrac{i}{2\pi}F^{t}\Big)=\det\!\Big(1-\tfrac{i}{2\pi}F\Big)=\sum_{j}(-1)^{j}c_j(F),$$
> where the middle equality is transpose-invariance of the determinant of a matrix of (commuting) even-degree forms, and the last uses that $c_j$ is homogeneous of degree $j$. Matching degree-$2j$ parts, $c_j(F^{\vee})=(-1)^{j}c_j(F)$; by the connection-independence in the Chern–Weil theorem, $c_j(E^{\vee})=(-1)^{j}c_j(E)$.
>
> **Conjugate bundle.** Fix a Hermitian structure $h$ on $E$. The map $\Psi(v)=h(\cdot,v)$ is a fibrewise conjugate-linear isomorphism $E\to E^{*}$ (injective by positive definiteness, bijective by dimension count), hence a $\mathbb{C}$-linear isomorphism $\overline{E}\to E^{\vee}$ (since $\Psi(\lambda\cdot_{\overline{E}}v)=\Psi(\overline{\lambda}v)=\lambda\Psi(v)$). Thus $\overline{E}\cong E^{\vee}$, and by isomorphism invariance of Chern classes together with the dual result, $c_j(\overline{E})=c_j(E^{\vee})=(-1)^{j}c_j(E)$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> A tempting fast route to the conjugate case is: "$\overline{E}$ has curvature $\overline{F}$, so $c(\overline{E})=\det(1+\tfrac{i}{2\pi}\overline{F})$, and for a unitary connection $F$ is skew-Hermitian, so $\overline{F}=-F^{t}$, giving the same answer as the dual." Each equality here is in fact correct for a *unitary* connection, but the step $c(\overline{E})=\det(1+\tfrac{i}{2\pi}\overline{F})$ hides a subtlety: the normalising constant $\tfrac{i}{2\pi}$ carries an $i$, and one must be sure it is *not* conjugated when passing to $\overline{E}$ (it is a fixed scalar in the definition of the Chern class, not part of the bundle's complex structure). The route in Step 4–5 sidesteps the subtlety entirely by proving the *bundle isomorphism* $\overline{E}\cong E^{\vee}$ and quoting isomorphism invariance; it needs only that a Hermitian metric is conjugate-linear in one slot, and never differentiates a conjugated connection. The extra condition that would make the shortcut rigorous is a careful check that the definition of $c(\overline{E})$ uses the same scalar $\tfrac{i}{2\pi}$ (equivalently, that conjugating the bundle does not conjugate the normalisation) — a check the isomorphism route makes unnecessary.

> [!note]- Sanity check: line bundles and the tautological bundle
> For a line bundle $L$ ($r=1$) the identity reads $c_1(L^{\vee})=-c_1(L)$, which matches Haydys' Theorem 77(iii) and the first-Chern-class computation: the dual of the tautological bundle $\mathcal{O}(-1)^{\vee}=\mathcal{O}(1)$ over $\mathbb{CP}^1$ has $\int_{\mathbb{CP}^1}c_1(\mathcal{O}(1))=+1$, whereas $\int_{\mathbb{CP}^1}c_1(\mathcal{O}(-1))=-1$ (see **[[Ex - The Chern Number of the Hopf Line Bundle over CP^1 is Minus One]]**). The signs are opposite, as $(-1)^{1}=-1$ demands.

---

# Key Takeaways

**The Chern class of a functorially derived bundle is computed by inducing a connection and reading the algebraic operation off the curvature.** Every construction on vector bundles — dual, conjugate, direct sum, tensor product, exterior power — comes with a *canonical* induced connection, and the curvature of the induced connection is a fixed algebraic function of the original curvature: $-F^{t}$ for the dual, $\overline{F}$ for the conjugate, block-diagonal $F_1\oplus F_2$ for the direct sum, $F_1\otimes1+1\otimes F_2$ for the tensor product. Since the Chern class is the class of an invariant polynomial in the curvature, computing $c$ of the derived bundle is then a matter of applying that polynomial to the transformed curvature. The reusable principle: to find the characteristic class of a derived bundle, do not seek a topological formula first — write the induced connection, transform the curvature, and evaluate. The trigger is any "$c$ of $F(E)$" question for a natural bundle operation $F$; the diagnostic is "what does the induction do to $F$?" This is the same engine that produces the Whitney sum formula (block-diagonal curvature, multiplicative determinant) and the tensor-product formula for first Chern classes.

**The sign $(-1)^{j}$ is homogeneity of the Chern polynomial in disguise, and dualising is the cleanest way to see it.** The Chern classes are the homogeneous pieces of $\det(1+\tfrac{i}{2\pi}\xi)$, graded by degree, so any operation that negates the curvature multiplies $c_j$ by $(-1)^{j}$. Dualising negates the curvature (after a transpose that the determinant cannot see), which is exactly why $c_j(E^{\vee})=(-1)^{j}c_j(E)$; the odd Chern classes flip sign and the even ones are preserved. This immediately explains several downstream facts: a bundle isomorphic to its own dual (for instance, one admitting a nondegenerate bilinear form) has $2c_{2k+1}=0$, so its odd Chern classes are torsion and vanish in real cohomology; the odd Chern classes of a complexified real bundle vanish because $E\otimes\mathbb{C}\cong\overline{E\otimes\mathbb{C}}$ forces $c_j=(-1)^{j}c_j$ (see **[[Ex - Odd Chern Classes of a Complexified Real Bundle Vanish]]**), which is precisely how the Pontryagin classes are defined from the surviving even ones. The transferable diagnostic: whenever a bundle equals its dual or conjugate up to isomorphism, the identity $c_j=(-1)^{j}c_j$ kills the odd classes rationally.

**Prefer transporting a known result across a bundle isomorphism to recomputing with a fiddly connection.** The conjugate-bundle identity could be attacked by differentiating a conjugated connection, but that invites a genuine trap — whether the normalising $i$ conjugates along with the bundle. The disciplined move is to prove the *isomorphism* $\overline{E}\cong E^{\vee}$ (a Hermitian metric is conjugate-linear in one slot, and a conjugate-linear iso into $E^{*}$ is a linear iso out of $\overline{E}$) and then invoke isomorphism invariance to inherit the dual result. This is a recurring pattern: when two derived bundles are abstractly isomorphic, compute the invariant on whichever one is easier and transport. The trigger condition is a pair of bundles related by a natural, if not obvious, isomorphism (here supplied by a metric); the reaction is to *establish the isomorphism as a bundle map first*, so that every isomorphism-invariant quantity — Chern classes, but also ranks, determinant lines, and $K$-theory classes — comes across for free. The companion drill **[[Ex - Chern Classes Depend only on the Isomorphism Class and Vanish for Trivial Bundles]]** proves the invariance this step relies on.
