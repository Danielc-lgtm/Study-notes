---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Chern-Weil Form of an Invariant Polynomial"
  - "Thm - Determinant is Multiplicative"
  - "Thm - Wedge Product Properties"
  - "Def - Determinant"
  - "Def - Curvature of a Vector-Bundle Connection"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a smooth manifold and let $\Omega^{\bullet}(M)=\bigoplus_{k\ge 0}\Omega^{k}(M)$ be its algebra of differential forms under the wedge product, with the graded subspace of even-degree forms written
$$\Omega^{\mathrm{even}}(M)=\bigoplus_{k\ge 0}\Omega^{2k}(M).$$
We allow forms to be complex-valued, so $\Omega^{\mathrm{even}}(M;\mathbb{C})=\Omega^{\mathrm{even}}(M)\otimes_{\mathbb{R}}\mathbb{C}$ is a $\mathbb{C}$-algebra under $\wedge$, with multiplicative unit the constant function $1\in\Omega^{0}(M)$. Prove the following three statements, which together justify that the total Chern form $\det\!\big(1+\tfrac{i}{2\pi}F\big)$ of a curvature is a well-defined, frame-independent, and multiplicatively-behaved even form.

1. **Even forms commute.** The subspace $\Omega^{\mathrm{even}}(M;\mathbb{C})$ is closed under $\wedge$ and is a *commutative* ring with unit $1$. Explicitly, $\alpha\wedge\beta=\beta\wedge\alpha$ for all $\alpha,\beta\in\Omega^{\mathrm{even}}(M;\mathbb{C})$.

2. **Determinants over a commutative ring are multiplicative and block-multiplicative.** Let $R$ be any commutative ring with unit and let $\det\colon\operatorname{Mat}_{n}(R)\to R$ be the determinant given by the Leibniz formula. Then
$$\det(PQ)=\det(P)\,\det(Q)\qquad\text{for all }P,Q\in\operatorname{Mat}_{n}(R),$$
and, for a block-diagonal matrix with square diagonal blocks $A\in\operatorname{Mat}_{p}(R)$ and $B\in\operatorname{Mat}_{q}(R)$,
$$\det\begin{pmatrix}A&0\\0&B\end{pmatrix}=\det(A)\,\det(B).$$

3. **Consequence for the total Chern form.** Let $E\to M$ be a complex vector bundle of rank $r$ with connection $\nabla$ and curvature $F=F_{\nabla}\in\Omega^{2}(M;\operatorname{End}E)$, a matrix of $2$-forms in any local frame. Deduce that
$$c(F):=\det\!\Big(1+\tfrac{i}{2\pi}F\Big)\in\Omega^{\mathrm{even}}(M;\mathbb{C})$$
is a well-defined even form, *independent of the choice of local frame*, and that for a Whitney sum $E=E_{1}\oplus E_{2}$ carrying the direct-sum connection $\nabla=\nabla_{1}\oplus\nabla_{2}$,
$$c\big(F_{\nabla_{1}\oplus\nabla_{2}}\big)=c\big(F_{\nabla_{1}}\big)\wedge c\big(F_{\nabla_{2}}\big).$$
This is the form-level content of the Whitney sum formula for Chern classes (Haydys, Theorem 87(iii)); Haydys asserts the two displayed determinant identities of statement 2 without proof, and this exercise supplies them.

**Recall:**

The objects in play are the graded-commutative wedge product, the Leibniz determinant over a commutative ring, the Chern–Weil construction of an invariant polynomial evaluated on a curvature, and the transformation of a curvature matrix under a change of local frame.

![[Def - Chern-Weil Form of an Invariant Polynomial#The Definition]]

For the total Chern class one takes the $\operatorname{Ad}$-invariant polynomial $p=\det(1+\tfrac{i}{2\pi}\,\cdot\,)$ on $\mathfrak{gl}_{r}(\mathbb{C})$ (a sum of the homogeneous invariant polynomials $c_{0},c_{1},\dots,c_{r}$) and evaluates it on the curvature $F$; the value is the even form $c(F)$ above. The point of the present exercise is precisely that "evaluate a matrix polynomial on a matrix of $2$-forms" makes unambiguous sense, and that the resulting form transforms correctly.

![[Thm - Wedge Product Properties#Statement]]

The one property used below is **graded commutativity**: for $\alpha\in\Omega^{k}(M)$ and $\beta\in\Omega^{l}(M)$,
$$\alpha\wedge\beta=(-1)^{kl}\,\beta\wedge\alpha .$$

![[Def - Determinant#The Definition]]

For a matrix $P=(P_{ij})$ with entries in a commutative ring $R$, the **determinant** is given by the Leibniz formula
$$\det(P)=\sum_{\sigma\in S_{n}}\operatorname{sign}(\sigma)\,\prod_{i=1}^{n}P_{i\,\sigma(i)},$$
a sum over the symmetric group $S_{n}$; equivalently, $\det$ is the unique function of the $n$ columns of $P$ that is $R$-linear in each column and alternating (it changes sign when two columns are swapped, hence vanishes when two columns coincide), normalised by $\det(1)=1$. Both descriptions require only that $R$ be a commutative ring: no division is used, so the entries may be even-degree differential forms.

![[Def - Curvature of a Vector-Bundle Connection#The Definition]]

Under a change of local frame $e'=e\,g$ with $g\colon U\to GL(r,\mathbb{C})$ a smooth matrix of functions, the curvature matrix transforms by conjugation, $F'=g^{-1}Fg$; this is the identity that statement 3 must be compatible with.

---

# Convergent Strategy

**Problem class.** This is a *well-definedness and structural-compatibility* exercise: we must show that a construction borrowed from linear algebra over a field — the characteristic-polynomial coefficients of a matrix — survives being applied to a matrix whose entries are differential forms, and that it retains its two defining algebraic features (conjugation invariance and multiplicativity across a direct sum). The recognisable shape is "an operation defined over a field is invoked over a stranger ring; check the axioms the field proof actually used." Here the only field fact used by the classical determinant is *commutativity of the coefficient ring*, so the whole exercise reduces to isolating that hypothesis and verifying it for even forms.

**Assumption pattern.** The load-bearing hypothesis is a *parity* condition, not a size or rank condition: the entries of $\tfrac{i}{2\pi}F$ are $2$-forms, hence of even degree, and even forms commute. Every place where the classical determinant proof would silently reorder scalars is legitimised by this single fact. The trigger to watch for is a matrix whose entries live in a *graded* algebra: the wedge product is only *graded*-commutative, so a matrix of odd forms would carry genuine sign obstructions, and the determinant would neither be well defined nor multiplicative. Restricting to even degrees is exactly what removes the signs.

**Theorem routing.** The route is: (i) from **graded commutativity** of the wedge product deduce that $\Omega^{\mathrm{even}}$ is a commutative ring; (ii) re-run the column-multilinearity proof of multiplicativity of $\det$ — the argument on [[Thm - Determinant is Multiplicative]], which is written for a field but never divides — verbatim over the commutative ring $\Omega^{\mathrm{even}}(M;\mathbb{C})$; (iii) obtain block-multiplicativity from the Leibniz formula by counting which permutations respect the blocks; (iv) feed the frame-change law $F'=g^{-1}Fg$ from [[Def - Curvature of a Vector-Bundle Connection|the curvature definition]] into multiplicativity to get frame-independence, and feed the block-diagonal form of a direct-sum curvature into block-multiplicativity to get the Whitney formula.

**Key decision point.** Two non-obvious moves. First, the decision to *reprove* multiplicativity rather than cite the field statement: the vault's [[Thm - Determinant is Multiplicative]] is stated over a field, and $\Omega^{\mathrm{even}}(M;\mathbb{C})$ is not a field (a nonzero positive-degree form is nilpotent, hence non-invertible), so the theorem cannot be applied as a black box; what *can* be reused is its proof, because that proof only ever multiplies and adds ring elements. Second, the recognition that frame-independence is not a separate computation but *is* conjugation invariance of $\det$ — the same $\det(g^{-1}Xg)=\det X$ that in the field case says the determinant is a similarity invariant — and that this invariance is a one-line corollary of multiplicativity once the entries are known to commute.

---

# Legal Operations Used

This solution deploys the following legal operations (numbered as descriptive operations; the orchestrator will reconcile them with the numbering on the [[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional|topic page]]'s Legal Operations section once it is written):

1. **Read off the sign of a wedge reordering from the degrees.** For any two homogeneous forms, $\alpha\wedge\beta=(-1)^{(\deg\alpha)(\deg\beta)}\beta\wedge\alpha$; when both degrees are even the sign is $+1$. This is the sole input to statement 1.

2. **Expand a determinant by multilinearity in the columns.** Write each column of a product $PQ$ as an $R$-linear combination of the columns of $P$, then distribute $\det$ across those combinations using its column-linearity, and discard the terms with a repeated column using its alternation.

3. **Reorder ring factors freely once commutativity is known.** In the expansion of a determinant, the entries of $Q$ appear as scalar coefficients multiplied in an order dictated by a summation index; commutativity of $\Omega^{\mathrm{even}}$ lets us reorder them into the order dictated by a permutation, which is what turns the double sum into $\det(P)\det(Q)$.

4. **Restrict the Leibniz sum to block-respecting permutations.** When a matrix is block-diagonal, every summand of the Leibniz formula that pairs a row of one block with a column of another block contains a zero entry and vanishes; only permutations preserving each block survive, and the sign of such a permutation factors across the blocks.

5. **Convert a conjugation into a determinant identity via multiplicativity.** From $F'=g^{-1}Fg$ and $\det(g^{-1})\det(g)=\det(1)=1$, obtain $\det(1+\tfrac{i}{2\pi}F')=\det(1+\tfrac{i}{2\pi}F)$; the degree-zero factors $\det(g^{\pm 1})$ are functions and commute with the even form they multiply.

---

# Hints

> [!note]- Hint 1
> Statement 1 is one line. Take $\alpha\in\Omega^{2k}(M)$ and $\beta\in\Omega^{2l}(M)$ and apply graded commutativity $\alpha\wedge\beta=(-1)^{(2k)(2l)}\beta\wedge\alpha$. What is the parity of $(2k)(2l)$?

> [!note]- Hint 2
> For multiplicativity, do *not* try to cite the field theorem — $\Omega^{\mathrm{even}}$ has non-invertible nonzero elements. Instead look at the proof of $\det(PQ)=\det P\det Q$ and ask which ring operations it uses. It expands $\det$ in the columns of $PQ$; the $j$-th column of $PQ$ is $\sum_{k}Q_{kj}\,(\text{$k$-th column of }P)$. Push $\det$ through this linear combination.

> [!note]- Hint 3
> After the expansion you get $\det(PQ)=\sum_{k_{1},\dots,k_{n}}Q_{k_{1}1}\cdots Q_{k_{n}n}\,\det\!\big(P_{\cdot k_{1}},\dots,P_{\cdot k_{n}}\big)$. Alternation kills every term in which two of the indices $k_{j}$ coincide, so only the terms where $j\mapsto k_{j}$ is a permutation $\sigma$ survive. To collect $\sum_{\sigma}\operatorname{sign}(\sigma)\prod_{j}Q_{\sigma(j)j}=\det Q$ you must reorder the scalar factors $Q_{\sigma(j)j}$ — this is where you need the entries of $Q$ to commute, i.e. where even degree is essential.

> [!note]- Hint 4
> For statement 3, frame-independence is conjugation invariance: $1+\tfrac{i}{2\pi}F'=g^{-1}\big(1+\tfrac{i}{2\pi}F\big)g$ because $g^{-1}1g=1$. Apply multiplicativity three times. For the Whitney formula, note that the curvature of a direct-sum connection is block-diagonal — $F_{\nabla_{1}\oplus\nabla_{2}}=F_{\nabla_{1}}\oplus F_{\nabla_{2}}$ — and use block-multiplicativity.

---

# Solution

The proof has four steps. Step 1 is the parity computation that makes $\Omega^{\mathrm{even}}$ a commutative ring. Steps 2 and 3 are pure commutative algebra: the two determinant identities, proved by re-running the classical column-expansion argument over an arbitrary commutative ring, so that they apply with $R=\Omega^{\mathrm{even}}(M;\mathbb{C})$. Step 4 harvests the geometric payoff — frame-independence from conjugation invariance, and the Whitney formula from block-multiplicativity.

**Step 1: The even forms form a commutative ring — even forms commute.**

The subspace $\Omega^{\mathrm{even}}(M;\mathbb{C})$ is closed under $\wedge$ and every pair of its elements commutes.

> [!note]- Derivation
> We first check closure. If $\alpha\in\Omega^{2k}(M;\mathbb{C})$ and $\beta\in\Omega^{2l}(M;\mathbb{C})$, then $\alpha\wedge\beta\in\Omega^{2k+2l}(M;\mathbb{C})=\Omega^{2(k+l)}(M;\mathbb{C})$, which is again of even degree; sums of even forms are even; and the unit $1\in\Omega^{0}(M)$ is even. Hence $\Omega^{\mathrm{even}}(M;\mathbb{C})$ is a unital subalgebra of $\big(\Omega^{\bullet}(M;\mathbb{C}),\wedge\big)$.
>
> We now show commutativity. By **graded commutativity** of the wedge product (restated in the Recall from [[Thm - Wedge Product Properties]]), for homogeneous $\alpha\in\Omega^{k}$ and $\beta\in\Omega^{l}$,
> $$\alpha\wedge\beta=(-1)^{kl}\,\beta\wedge\alpha\qquad\text{(graded commutativity of }\wedge\text{)}.$$
> Take both degrees even, $k=2k'$ and $l=2l'$. Then the exponent is
> $$kl=(2k')(2l')=4\,k'l',$$
> an even integer, so $(-1)^{kl}=(-1)^{4k'l'}=+1$ (since $4k'l'$ is even). Therefore
> $$\alpha\wedge\beta=+\,\beta\wedge\alpha\qquad\text{(the reordering sign is }+1\text{ for even degrees).}$$
> A general element of $\Omega^{\mathrm{even}}(M;\mathbb{C})$ is a finite sum of homogeneous even forms; since $\wedge$ is bilinear and each homogeneous pair commutes, the sums commute as well. Hence $\Omega^{\mathrm{even}}(M;\mathbb{C})$ is a commutative unital ring. We write $R:=\Omega^{\mathrm{even}}(M;\mathbb{C})$ from now on.

**Step 2: $\det$ is multiplicative over any commutative ring.**

For $P,Q\in\operatorname{Mat}_{n}(R)$ with $R$ commutative, $\det(PQ)=\det(P)\det(Q)$.

> [!note]- Derivation
> We regard $\det$ as a function of the $n$ columns of its argument, $R$-linear in each column and alternating; this is the column description recalled from [[Def - Determinant]], and it is equivalent to the Leibniz formula over any commutative ring. Write $P_{\cdot k}\in R^{n}$ for the $k$-th column of $P$. The definition of matrix multiplication gives, for the $j$-th column of $PQ$,
> $$(PQ)_{\cdot j}=\sum_{k=1}^{n}Q_{kj}\,P_{\cdot k}\qquad\text{(entry }(PQ)_{ij}=\sum_{k}P_{ik}Q_{kj}\text{, read column-wise).}$$
> Expanding $\det(PQ)=\det\big((PQ)_{\cdot 1},\dots,(PQ)_{\cdot n}\big)$ and using **$R$-linearity in each column** to distribute the sum out of every slot,
> $$\det(PQ)=\sum_{k_{1}=1}^{n}\cdots\sum_{k_{n}=1}^{n}\Big(\prod_{j=1}^{n}Q_{k_{j}\,j}\Big)\,\det\big(P_{\cdot k_{1}},\dots,P_{\cdot k_{n}}\big)\qquad\text{(multilinearity of }\det\text{).}$$
> Pulling the scalars $Q_{k_{j}j}\in R$ out of the determinant is legitimate precisely because $\det$ is $R$-linear in each column; and collecting them into the single product $\prod_{j}Q_{k_{j}j}$ requires that these ring elements multiply in any order — which holds because $R$ is **commutative** (Step 1). This is the one and only place commutativity is used, and it is exactly the step that fails for a matrix of odd forms.
>
> By **alternation**, $\det\big(P_{\cdot k_{1}},\dots,P_{\cdot k_{n}}\big)=0$ whenever two of the indices $k_{1},\dots,k_{n}$ are equal (a determinant with two equal columns vanishes). Hence only the tuples $(k_{1},\dots,k_{n})$ that are permutations of $(1,\dots,n)$ contribute: writing $k_{j}=\sigma(j)$ for $\sigma\in S_{n}$,
> $$\det(PQ)=\sum_{\sigma\in S_{n}}\Big(\prod_{j=1}^{n}Q_{\sigma(j)\,j}\Big)\,\det\big(P_{\cdot\sigma(1)},\dots,P_{\cdot\sigma(n)}\big)\qquad\text{(only permutation terms survive alternation).}$$
> For each $\sigma$, reordering the columns of $P$ from the order $\big(P_{\cdot\sigma(1)},\dots,P_{\cdot\sigma(n)}\big)$ back to the standard order $\big(P_{\cdot 1},\dots,P_{\cdot n}\big)$ costs the sign of $\sigma$:
> $$\det\big(P_{\cdot\sigma(1)},\dots,P_{\cdot\sigma(n)}\big)=\operatorname{sign}(\sigma)\,\det(P)\qquad\text{(alternation: a permutation of columns multiplies }\det\text{ by its sign).}$$
> Substituting and factoring out $\det(P)$ (which no longer depends on $\sigma$),
> $$\det(PQ)=\det(P)\sum_{\sigma\in S_{n}}\operatorname{sign}(\sigma)\prod_{j=1}^{n}Q_{\sigma(j)\,j}=\det(P)\,\det(Q),$$
> where the last equality is the Leibniz formula for $\det(Q)$ (with the product taken over $j$, matching $Q_{\sigma(j)j}$). Every operation used was an addition or multiplication in the commutative ring $R$; no division occurred, so although $R$ is not a field the argument is valid. This reproves, over a commutative ring, the field statement [[Thm - Determinant is Multiplicative]], which cannot be cited directly here because $R=\Omega^{\mathrm{even}}(M;\mathbb{C})$ is not a field (a nonzero form of positive degree is nilpotent, so not invertible).

**Step 3: The determinant of a block-diagonal matrix is the product of the blocks' determinants.**

For $A\in\operatorname{Mat}_{p}(R)$ and $B\in\operatorname{Mat}_{q}(R)$ with $n=p+q$, $\det\begin{pmatrix}A&0\\0&B\end{pmatrix}=\det(A)\det(B)$.

> [!note]- Derivation
> Let $M=\begin{pmatrix}A&0\\0&B\end{pmatrix}\in\operatorname{Mat}_{n}(R)$, so that
> $$M_{ij}=\begin{cases}A_{ij},& 1\le i,j\le p,\\[2pt] B_{(i-p)(j-p)},& p<i,j\le n,\\[2pt] 0,& \text{otherwise (}i,j\text{ in different blocks).}\end{cases}$$
> By the Leibniz formula,
> $$\det(M)=\sum_{\sigma\in S_{n}}\operatorname{sign}(\sigma)\prod_{i=1}^{n}M_{i\,\sigma(i)}\qquad\text{(definition of }\det\text{ over }R\text{).}$$
> A summand is nonzero only if $M_{i\,\sigma(i)}\ne 0$ for every $i$, which by the block structure forces $\sigma(i)$ to lie in the *same* block as $i$: $\sigma\big(\{1,\dots,p\}\big)=\{1,\dots,p\}$ and $\sigma\big(\{p+1,\dots,n\}\big)=\{p+1,\dots,n\}$. Such a $\sigma$ is determined by a pair $(\alpha,\beta)$ with $\alpha\in S_{p}$ acting on the first block and $\beta\in S_{q}$ acting on the second; write $\sigma=\alpha\times\beta$. The sign is multiplicative under this decomposition,
> $$\operatorname{sign}(\alpha\times\beta)=\operatorname{sign}(\alpha)\,\operatorname{sign}(\beta)\qquad\text{(the two blocks are disjoint cycles, and }\operatorname{sign}\text{ is a homomorphism }S_{n}\to\{\pm1\}\text{).}$$
> Splitting the product over $i$ across the two blocks and using commutativity of $R$ (Step 1) to regroup the factors,
> $$\prod_{i=1}^{n}M_{i\,\sigma(i)}=\Big(\prod_{i=1}^{p}A_{i\,\alpha(i)}\Big)\Big(\prod_{i=1}^{q}B_{i\,\beta(i)}\Big).$$
> Therefore the block-respecting summands factor as a product of two independent Leibniz sums:
> $$\det(M)=\sum_{\alpha\in S_{p}}\sum_{\beta\in S_{q}}\operatorname{sign}(\alpha)\operatorname{sign}(\beta)\Big(\prod_{i=1}^{p}A_{i\,\alpha(i)}\Big)\Big(\prod_{i=1}^{q}B_{i\,\beta(i)}\Big)=\Big(\sum_{\alpha\in S_{p}}\operatorname{sign}(\alpha)\prod_{i}A_{i\,\alpha(i)}\Big)\Big(\sum_{\beta\in S_{q}}\operatorname{sign}(\beta)\prod_{i}B_{i\,\beta(i)}\Big),$$
> the last equality by distributivity in the commutative ring $R$. The two factors are exactly $\det(A)$ and $\det(B)$, so $\det(M)=\det(A)\det(B)$.

**Step 4: The total Chern form is a well-defined, frame-independent even form, multiplicative on Whitney sums.**

Applying Steps 1–3 to the matrix $1+\tfrac{i}{2\pi}F$ over $R=\Omega^{\mathrm{even}}(M;\mathbb{C})$ yields all three geometric conclusions.

> [!note]- Derivation
> **Well-definedness as an even form.** In a local frame the curvature $F=(F^{i}{}_{j})$ is an $r\times r$ matrix whose entries $F^{i}{}_{j}\in\Omega^{2}(M;\mathbb{C})$ are $2$-forms; hence the entries of $1+\tfrac{i}{2\pi}F$ lie in $\Omega^{0}(M;\mathbb{C})\oplus\Omega^{2}(M;\mathbb{C})\subset R$. By Step 1, $R$ is a commutative ring, so the Leibniz formula
> $$c(F)=\det\!\Big(1+\tfrac{i}{2\pi}F\Big)=\sum_{\sigma\in S_{r}}\operatorname{sign}(\sigma)\prod_{i=1}^{r}\Big(1+\tfrac{i}{2\pi}F\Big)^{i}{}_{\sigma(i)}$$
> evaluates to a well-defined element of $R$: each summand is a wedge product of $r$ entries of even degree, and by commutativity (Step 1) the value of that product does not depend on the order in which the factors are wedged, so no ordering ambiguity arises. The result is a form of even degree at most $2r$, i.e. $c(F)\in\Omega^{\mathrm{even}}(M;\mathbb{C})$.
>
> **Frame-independence.** Under a change of local frame $e'=e\,g$ with $g\colon U\to GL(r,\mathbb{C})$, the curvature matrix transforms by $F'=g^{-1}Fg$ (recalled from [[Def - Curvature of a Vector-Bundle Connection]]). Since the entries of $g$ are functions, that is degree-zero forms, they commute with every form and with $1$, so
> $$1+\tfrac{i}{2\pi}F'=1+\tfrac{i}{2\pi}\,g^{-1}Fg=g^{-1}\Big(1+\tfrac{i}{2\pi}F\Big)g\qquad\text{(using }g^{-1}1g=1\text{).}$$
> Applying multiplicativity (Step 2) three times,
> $$c(F')=\det\!\Big(g^{-1}\big(1+\tfrac{i}{2\pi}F\big)g\Big)=\det(g^{-1})\,\det\!\Big(1+\tfrac{i}{2\pi}F\Big)\,\det(g)\qquad\text{(by Step 2).}$$
> The factors $\det(g^{-1})$ and $\det(g)$ are degree-zero forms (functions on $U$), hence central in $R$, so they may be moved next to each other; and by Step 2 again, $\det(g^{-1})\det(g)=\det(g^{-1}g)=\det(1)=1$. Therefore
> $$c(F')=\det\!\Big(1+\tfrac{i}{2\pi}F\Big)=c(F),$$
> so the locally-computed forms agree on overlaps and glue to a single global form $c(F)\in\Omega^{\mathrm{even}}(M;\mathbb{C})$, independent of the trivialising frame. (This is the same computation that, in the field case, shows the determinant is a conjugation invariant; here it is what makes $c(F)$ a well-defined characteristic form, in agreement with the descent established on [[Def - Chern-Weil Form of an Invariant Polynomial]].)
>
> **The Whitney sum formula at the level of forms.** Let $E=E_{1}\oplus E_{2}$ carry the direct-sum connection $\nabla=\nabla_{1}\oplus\nabla_{2}$, defined by $\nabla(s_{1}\oplus s_{2})=\nabla_{1}s_{1}\oplus\nabla_{2}s_{2}$. The associated exterior covariant derivative acts block-diagonally on $\Omega^{\bullet}(M;E_{1})\oplus\Omega^{\bullet}(M;E_{2})$, so its square, the curvature, is block-diagonal too:
> $$F_{\nabla_{1}\oplus\nabla_{2}}=\begin{pmatrix}F_{\nabla_{1}}&0\\0&F_{\nabla_{2}}\end{pmatrix}\qquad\text{(curvature of a direct sum splits along the summands).}$$
> Choosing a local frame adapted to the splitting (the first $r_{1}=\operatorname{rk}E_{1}$ frame vectors spanning $E_{1}$, the last $r_{2}=\operatorname{rk}E_{2}$ spanning $E_{2}$), the matrix $1+\tfrac{i}{2\pi}F$ is block-diagonal with blocks $1+\tfrac{i}{2\pi}F_{\nabla_{1}}$ and $1+\tfrac{i}{2\pi}F_{\nabla_{2}}$. By block-multiplicativity (Step 3),
> $$c\big(F_{\nabla_{1}\oplus\nabla_{2}}\big)=\det\begin{pmatrix}1+\tfrac{i}{2\pi}F_{\nabla_{1}}&0\\0&1+\tfrac{i}{2\pi}F_{\nabla_{2}}\end{pmatrix}=\det\!\Big(1+\tfrac{i}{2\pi}F_{\nabla_{1}}\Big)\,\det\!\Big(1+\tfrac{i}{2\pi}F_{\nabla_{2}}\Big)=c\big(F_{\nabla_{1}}\big)\wedge c\big(F_{\nabla_{2}}\big),$$
> the product in $R$ being the wedge product. This is the form-level Whitney sum formula; passing to de Rham cohomology (each $c(F_{\nabla_{j}})$ is closed, by the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]]) turns the wedge into the cup product and yields the cohomological statement $c(E_{1}\oplus E_{2})=c(E_{1})\smile c(E_{2})$, proved in full on [[Thm - Axioms and Properties of Chern Classes]].

> [!note]- Complete formal solution
> **Claim.** For a complex vector bundle $E\to M$ of rank $r$ with connection $\nabla$ and curvature $F$, the form $c(F)=\det(1+\tfrac{i}{2\pi}F)$ is a well-defined, frame-independent element of $\Omega^{\mathrm{even}}(M;\mathbb{C})$, and $c(F_{\nabla_{1}\oplus\nabla_{2}})=c(F_{\nabla_{1}})\wedge c(F_{\nabla_{2}})$ for a direct-sum connection.
>
> *Even forms commute.* For $\alpha\in\Omega^{2k}$, $\beta\in\Omega^{2l}$, graded commutativity gives $\alpha\wedge\beta=(-1)^{4kl}\beta\wedge\alpha=\beta\wedge\alpha$. Since $\Omega^{\mathrm{even}}(M;\mathbb{C})$ is closed under $\wedge$, contains the unit $1$, and every pair of its elements commutes, it is a commutative unital ring $R$.
>
> *Multiplicativity of $\det$ over a commutative ring $R$.* Viewing $\det$ as alternating and $R$-linear in the columns, and writing the $j$-th column of $PQ$ as $\sum_{k}Q_{kj}P_{\cdot k}$,
> $$\det(PQ)=\sum_{k_{1},\dots,k_{n}}\Big(\prod_{j}Q_{k_{j}j}\Big)\det(P_{\cdot k_{1}},\dots,P_{\cdot k_{n}}).$$
> Alternation removes terms with a repeated index; the survivors are indexed by $\sigma\in S_{n}$ with $k_{j}=\sigma(j)$, and $\det(P_{\cdot\sigma(1)},\dots,P_{\cdot\sigma(n)})=\operatorname{sign}(\sigma)\det(P)$. Commutativity of $R$ lets the scalars $Q_{\sigma(j)j}$ be reordered, giving $\det(PQ)=\det(P)\sum_{\sigma}\operatorname{sign}(\sigma)\prod_{j}Q_{\sigma(j)j}=\det(P)\det(Q)$. No division is used, so this holds over any commutative ring.
>
> *Block-multiplicativity.* For $M=\operatorname{diag}(A,B)$ with square blocks, the only nonvanishing Leibniz terms come from permutations $\sigma=\alpha\times\beta$ preserving each block, with $\operatorname{sign}(\sigma)=\operatorname{sign}(\alpha)\operatorname{sign}(\beta)$; distributing the resulting double sum gives $\det(M)=\det(A)\det(B)$.
>
> *Application.* The entries of $1+\tfrac{i}{2\pi}F$ are even forms, so $c(F)\in R$ is unambiguous. Under $F'=g^{-1}Fg$, $1+\tfrac{i}{2\pi}F'=g^{-1}(1+\tfrac{i}{2\pi}F)g$, whence $c(F')=\det(g^{-1})\det(1+\tfrac{i}{2\pi}F)\det(g)=c(F)$ since $\det(g^{-1})\det(g)=1$; so $c(F)$ is frame-independent and globally defined. For $E=E_{1}\oplus E_{2}$ the curvature is block-diagonal $F=\operatorname{diag}(F_{\nabla_{1}},F_{\nabla_{2}})$, and block-multiplicativity gives $c(F)=c(F_{\nabla_{1}})\wedge c(F_{\nabla_{2}})$. $\blacksquare$

> [!warning] Illegal but tempting: dropping the even-degree restriction
> One is tempted to say "the determinant of a matrix of forms is always well defined and multiplicative." It is not — the parity restriction is essential. Consider the $2\times 2$ matrix of $1$-forms $\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}$ over the *non*-commutative ring of odd forms, where $\alpha\wedge\delta=-\delta\wedge\alpha$. Its naive determinant $\alpha\wedge\delta-\beta\wedge\gamma$ is not conjugation-invariant, so it would not descend to a global form, and $\det(PQ)=\det(P)\det(Q)$ fails because the reordering step in Step 2 introduces uncancelled signs. What makes the extra condition legal is exactly *even degree*: restricting the entries of $\tfrac{i}{2\pi}F$ to $2$-forms places them in the commutative ring $\Omega^{\mathrm{even}}$, and every sign that would obstruct the argument becomes $+1$. This is why invariant polynomials are evaluated on the curvature $F\in\Omega^{2}$ — an even form — and never on, say, the connection $A\in\Omega^{1}$.

---

# Key Takeaways

**The natural coefficient ring for characteristic forms is $\Omega^{\mathrm{even}}(M)$, and it is commutative for a parity reason, not by accident.** The wedge product is only *graded*-commutative: reordering two homogeneous forms costs the sign $(-1)^{(\deg\alpha)(\deg\beta)}$. That sign is $+1$ precisely when at least one of the two degrees is even, and it is $+1$ for *every* pair when both are even. So the even-degree forms carve out an honest commutative ring inside the graded-commutative algebra of all forms. This is the structural fact underlying the entire Chern–Weil construction: an $\operatorname{Ad}$-invariant polynomial is a gadget built from the multiplication of a commutative ring (its monomials are unordered products of matrix entries), so to evaluate it on a matrix one needs the entries to live in a commutative ring — and curvatures oblige because they are $2$-forms. The transferable diagnostic: whenever you meet a linear-algebra construction "matrix $\mapsto$ scalar built by multiplying entries" applied to forms, the first question is *what is the parity of the entries?* Even parity buys you the whole commutative-ring toolkit; odd parity does not, and you must instead work with graded or super-determinants.

**A theorem proved over a field extends to a commutative ring exactly when its proof never divides — and one must reprove, not cite.** The vault's [[Thm - Determinant is Multiplicative]] is stated for a field, and $\Omega^{\mathrm{even}}(M;\mathbb{C})$ is decidedly not a field: any nonzero positive-degree form squares (or cubes, ...) to something that eventually vanishes, so it is nilpotent and non-invertible. One therefore cannot apply the field theorem as a black box. What one *can* do is inspect its proof: the column-multilinearity argument for $\det(PQ)=\det P\det Q$ uses only addition, multiplication, and the sign of a permutation, never an inverse, so it survives verbatim over any commutative ring. This "audit the proof for its actual hypotheses" move is a recurring pattern in passing from linear algebra to bundle theory (the Cayley–Hamilton theorem, the characteristic polynomial, and the adjugate identity all generalise the same way), and it is the reason the entire theory of characteristic classes can be phrased as invariant polynomials evaluated on curvature. When you see a familiar identity invoked over an unfamiliar ring, do not ask "is this ring a field?"; ask "does the proof divide?".

**The Whitney sum formula is, at the level of forms, nothing more than the determinant of a block-diagonal matrix.** The impressive-sounding statement $c(E_{1}\oplus E_{2})=c(E_{1})\smile c(E_{2})$ dissolves once one notices that the curvature of a direct-sum connection is block-diagonal — because the connection itself acts diagonally on the two summands — so the matrix $1+\tfrac{i}{2\pi}F$ is block-diagonal, and a block-diagonal determinant factors. This is the payoff of having isolated block-multiplicativity as a separate, purely combinatorial fact about the Leibniz formula: the geometry contributes only the observation "direct sums give block-diagonal curvature," and everything else is bookkeeping over the commutative ring of even forms. The same reduction powers the computation of $c_{j}(E^{\vee})$ (via the block/dual structure) and the splitting principle, where one pretends every bundle is a sum of line bundles precisely because the sum formula makes the pretence consistent. The trigger to reach for this exercise: any time a characteristic class of a *sum* or a *conjugate* of bundles is needed, translate the bundle operation into a block or conjugation operation on the curvature matrix and let multiplicativity of $\det$ do the rest.
