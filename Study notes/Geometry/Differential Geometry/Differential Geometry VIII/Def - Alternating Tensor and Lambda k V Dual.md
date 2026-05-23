---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Multilinear Form"
  - "Def - Alternating Multilinear Form"
  - "Def - Tensor Product of Vector Spaces"
  - "Def - Covariant Tensor on a Vector Space"
tags: [geometry, differential-geometry, multilinear-algebra]
---

# Notation

$V$ is a finite-dimensional real vector space, $\dim V = n \geq 1$. $V^*$ is its dual space, with basis $\varepsilon^1, \dots, \varepsilon^n$ dual to a chosen basis $E_1, \dots, E_n$ of $V$ (so $\varepsilon^i(E_j) = \delta^i_j$). $T^k(V^*) = V^* \otimes \cdots \otimes V^*$ ($k$ factors) is the vector space of [[Def - Covariant Tensor on a Vector Space|covariant k-tensors]] on $V$; equivalently, $k$-multilinear maps $V^k \to \mathbb{R}$. $S_k$ is the symmetric group on $k$ letters and $\operatorname{sgn}\sigma \in \{\pm 1\}$ the sign of $\sigma \in S_k$. A **multi-index** is an ordered tuple $I = (i_1, \dots, i_k)$ of integers in $\{1, \dots, n\}$; $I$ is **increasing** if $i_1 < \cdots < i_k$. The set of all increasing multi-indices of length $k$ from $\{1, \dots, n\}$ has cardinality $\binom{n}{k}$. The full notation registry is on [[Differential Geometry VIII — Differential Forms]].

---

# Axiom Motivation

The motivation for alternating $k$-tensors is the same as for alternating multilinear forms in linear algebra, but the higher stakes warrant restating: we want the objects whose values are the *signed* analogues of "$k$-dimensional content" — signed volume for $k = n$, signed area when $k = 2$ on a $3$-dimensional space, and so on. The decisive desideratum is that swapping two arguments reverses the sign, so that "orientation" is a meaningful concept; the algebraic encoding is that the tensor vanishes whenever two of its arguments are equal. The whole power of differential forms downstream rests on this single decision.

Why "vanishing on tuples with a repeat" rather than the equivalent "antisymmetry under swap"? The two are equivalent in characteristic $\neq 2$ (which is our setting), but the vanishing form is the one that automatically generalizes to "the tensor vanishes on every *linearly dependent* tuple": if $v_k = \sum_{j \neq k} a_j v_j$, expanding $\omega(v_1, \dots, v_n)$ by multilinearity gives a sum of terms each containing a repeated argument, hence each zero. This means an alternating $k$-tensor *cannot see* a vector whose presence is already implicit in the list — it is genuinely a measurement of $k$-dimensional content. This is the input-broadening that connects alternation to linear independence: $\omega(v_1, \dots, v_k) \neq 0$ is a proof that the $v_i$ are independent.

Why insist on the maximal generality of $k$-tensors and not stop at the bilinear ($k = 2$) case? Because the natural objects of differential geometry require multiple slots: an $n$-dimensional volume measurement on an $n$-dimensional manifold needs $n$ tangent-vector arguments at each point. Alternating bilinear forms ($k = 2$) suffice for symplectic geometry, which lives on even-dimensional manifolds with a chosen $2$-form, but for general-dimensional integration, orientation, and de Rham theory we need all values of $k$.

The **dimension theorem** $\dim \Lambda^k V^* = \binom{n}{k}$ is the load-bearing structural fact of this definition. Most importantly, the case $k = n$ gives $\dim \Lambda^n V^* = 1$, so all alternating $n$-tensors on an $n$-dimensional space are scalar multiples of one — and that one (with appropriate normalization on a basis) is the determinant. The cases $k > n$ give $\dim = 0$: no nonzero alternating $k$-tensor exists, because every tuple of $k > n$ vectors in an $n$-dimensional space is linearly dependent, and an alternating tensor kills dependent tuples.

The choice to package alternating tensors as a separate [[Def - Subspace|subspace]] $\Lambda^k V^*$ of $T^k(V^*)$, rather than working with general $k$-tensors and "antisymmetrising as needed", is forced by the wedge product. The wedge product $\Lambda^k \times \Lambda^\ell \to \Lambda^{k+\ell}$ is a natural multiplication; the analogous operation on general $T^k$ would require choosing an antisymmetrisation strategy at every multiplication, and the result would not be associative without bookkeeping. By restricting to alternating tensors from the start, we obtain a clean graded algebra $\Lambda^\bullet V^* = \bigoplus_k \Lambda^k V^*$ with an associative wedge, of total dimension $\sum_k \binom{n}{k} = 2^n$.

What breaks if we strengthen the axiom — demand, say, that the tensor be *symmetric* in addition to multilinear? Then we have built a symmetric tensor, not an alternating one, and the resulting algebra is the symmetric algebra $\operatorname{Sym}^\bullet V^*$ (the polynomial algebra in the dual basis). Symmetric tensors have their own importance — they are what Riemannian metrics are, with the inner product as a symmetric $2$-tensor — but they do not integrate invariantly over oriented surfaces, because their values do not flip sign under reorientation. The two algebras $\operatorname{Sym}^\bullet$ and $\Lambda^\bullet$ are the two halves of the tensor algebra under the $S_k$-action on $T^k$; alternating is the *signed* half, symmetric is the *unsigned* half.

---

# The Definition

Let $V$ be a finite-dimensional real vector space, $\dim V = n$. An **alternating $k$-tensor** on $V$ (also called a **$k$-covector**) is a covariant $k$-tensor $\omega : V^k \to \mathbb{R}$ — that is, a $k$-multilinear map — such that
$$\omega(v_1, \dots, v_k) = 0 \quad \text{whenever } v_i = v_j \text{ for some } i \neq j.$$
Equivalently (in any characteristic $\neq 2$), $\omega$ is alternating if and only if swapping any two arguments multiplies the value by $-1$:
$$\omega(v_1, \dots, v_i, \dots, v_j, \dots, v_k) = -\,\omega(v_1, \dots, v_j, \dots, v_i, \dots, v_k).$$
Equivalently, for every $\sigma \in S_k$,
$$\omega(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\operatorname{sgn}\sigma)\,\omega(v_1, \dots, v_k).$$
Equivalently, $\omega$ vanishes on any linearly dependent tuple.

The set of alternating $k$-tensors on $V$ is a vector subspace of $T^k(V^*)$, denoted $\Lambda^k(V^*)$ (or $\Lambda^k V^*$). By convention $\Lambda^0(V^*) = \mathbb{R}$ (the zero-tensors are scalars) and $\Lambda^1(V^*) = V^*$ (every linear functional is trivially alternating).

**The alternation projector.** The linear map $\operatorname{Alt} : T^k(V^*) \to \Lambda^k(V^*)$ defined by
$$\operatorname{Alt}\alpha(v_1, \dots, v_k) = \frac{1}{k!}\sum_{\sigma \in S_k}(\operatorname{sgn}\sigma)\,\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)})$$
is a projection: $\operatorname{Alt}^2 = \operatorname{Alt}$, $\operatorname{Alt}\alpha = \alpha$ if and only if $\alpha$ is alternating, and $\operatorname{Alt}\alpha$ is alternating for every $\alpha$.

**Elementary alternating tensors.** Given a basis $(\varepsilon^i)$ of $V^*$ and a multi-index $I = (i_1, \dots, i_k)$, define
$$\varepsilon^I(v_1, \dots, v_k) = \det\begin{pmatrix}\varepsilon^{i_1}(v_1) & \cdots & \varepsilon^{i_1}(v_k) \\ \vdots & \ddots & \vdots \\ \varepsilon^{i_k}(v_1) & \cdots & \varepsilon^{i_k}(v_k)\end{pmatrix}.$$
This $\varepsilon^I$ is alternating in the $v_j$ because the determinant is alternating in its columns. The generalized Kronecker delta
$$\delta^I_J = \det\begin{pmatrix}\delta^{i_1}_{j_1} & \cdots & \delta^{i_1}_{j_k} \\ \vdots & \ddots & \vdots \\ \delta^{i_k}_{j_1} & \cdots & \delta^{i_k}_{j_k}\end{pmatrix}$$
satisfies $\delta^I_J = \operatorname{sgn}\sigma$ if $J = I\sigma$ for some $\sigma \in S_k$ and neither $I$ nor $J$ has a repeated index; $\delta^I_J = 0$ otherwise. The defining property of $\varepsilon^I$ is $\varepsilon^I(E_{j_1}, \dots, E_{j_k}) = \delta^I_J$.

**Basis of $\Lambda^k(V^*)$ and dimension.** The elementary $k$-covectors $\{\varepsilon^I : I \text{ increasing of length } k\}$ form a basis of $\Lambda^k(V^*)$, so
$$\dim \Lambda^k(V^*) = \binom{n}{k}.$$
For $k > n$, $\Lambda^k(V^*) = \{0\}$. In particular $\dim \Lambda^n(V^*) = 1$: there is, up to scalar, a unique top-degree alternating $n$-form, and on $\mathbb{R}^n$ with the standard basis it is the determinant.

**Permutation-sum formula.** Every $\omega \in \Lambda^k(V^*)$ admits the expansion
$$\omega = \sum_{I \text{ increasing}} \omega_I\,\varepsilon^I, \qquad \omega_I = \omega(E_{i_1}, \dots, E_{i_k}).$$

---

# Categorical Definition

The alternating $k$-tensors on $V$ are the linear functionals on the **$k$-th exterior power** $\Lambda^k V$:
$$\Lambda^k(V^*) \cong (\Lambda^k V)^*.$$

The exterior power $\Lambda^k V$ is defined by a universal property: it is the universal target of an alternating $k$-multilinear map out of $V$. Concretely, $\Lambda^k V$ is the quotient of the $k$-fold tensor power $V^{\otimes k}$ by the subspace generated by all tensors of the form $v_1 \otimes \cdots \otimes v_k$ with $v_i = v_j$ for some $i \neq j$. The image of $v_1 \otimes \cdots \otimes v_k$ in this quotient is denoted $v_1 \wedge \cdots \wedge v_k$, the **wedge product** of vectors.

The universal property states that for any vector space $U$ and any alternating $k$-multilinear map $f : V^k \to U$, there is a unique linear map $\tilde f : \Lambda^k V \to U$ with $f(v_1, \dots, v_k) = \tilde f(v_1 \wedge \cdots \wedge v_k)$. Specializing $U = \mathbb{R}$ recovers the identification $\Lambda^k(V^*) \cong (\Lambda^k V)^*$ via $\omega \mapsto \tilde\omega$.

This characterization is what makes the construction natural under linear maps: a linear map $T : V \to W$ induces, by functoriality of $\Lambda^k$, a linear map $\Lambda^k T : \Lambda^k V \to \Lambda^k W$, and dualizing gives a linear map $(\Lambda^k T)^* : \Lambda^k(W^*) \to \Lambda^k(V^*)$ — the algebraic prototype of the pullback of forms.

**Direct sum structure.** Defining $\Lambda^\bullet V^* = \bigoplus_{k=0}^n \Lambda^k V^*$ gives a graded vector space of total dimension $2^n$. The wedge product makes it an associative graded-commutative algebra, the **exterior algebra** of $V^*$, and is the universal such algebra equipped with a degree-$1$ linear inclusion $V^* \hookrightarrow \Lambda^\bullet V^*$ subject to $v \wedge v = 0$ for $v \in V^*$ — see [[Def - The Wedge Product on a Manifold]] for the manifold version.

---

# Relate to Other Fields / Compression

An alternating $k$-tensor is the natural algebraic embodiment of "signed $k$-dimensional content". The case $k = n = \dim V$ specializes to the [[Def - Determinant|determinant]], which is the unique alternating $n$-form on $V$ taking value $1$ on a chosen basis. Lower-degree alternating tensors $\Lambda^k V^*$ for $k < n$ measure signed $k$-dimensional content of $k$-tuples of vectors in $V$ — geometrically the signed $k$-volume of a parallelepiped, but the parallelepiped need not span all of $V$.

The bridge to differential geometry is verbatim: a **differential $k$-form** on a manifold $M$ is a smooth choice $p \mapsto \omega_p \in \Lambda^k T_p^*M$, i.e., a smooth section of the **exterior power bundle** $\Lambda^k T^*M$. See [[Def - Differential k-Form on a Manifold]]. Every algebraic property of $\Lambda^k V^*$ — wedge product, dimension count, expansion in elementary covectors, determinant identity — propagates pointwise to the manifold setting.

The bridge to homological algebra is via [[Def - Tensor Product of Vector Spaces|tensor products]]: the exterior algebra $\Lambda^\bullet V$ is one of the three canonical "free graded algebras" attached to a vector space $V$, the others being the symmetric algebra $\operatorname{Sym}^\bullet V$ (commutative case) and the tensor algebra $T^\bullet V$ (no commutativity). The three together exhaust the irreducible $S_k$-representation content of $V^{\otimes k}$ for $k \leq 2$; for $k \geq 3$ there are additional **mixed-symmetry** representations indexed by Young diagrams, of which symmetric and alternating are the two extremes.

**True name:** An alternating $k$-tensor on $V$ is "a $k$-dimensional signed-volume measuring functional" — it accepts $k$ vectors and returns a number that flips sign under any permutation, vanishes on linearly dependent inputs, and on a basis spanning $V$ (in the case $k = n$) returns the determinant of the change-of-basis.

A trigger-reaction pattern: **see "alternating $k$-tensor / $k$-covector" → think "signed $k$-volume / exterior power $(\Lambda^k V)^* /$ basis $\varepsilon^I$ for increasing $I$ / determinant when $k = n$"**. This pattern is the bridge from the algebraic definition to every downstream construction (wedge product, differential form, integration with orientation, determinant of a linear map).

---

# Examples / Corollaries

**Is an instance — the determinant on $\mathbb{R}^n$.** The determinant $\det : (\mathbb{R}^n)^n \to \mathbb{R}$, viewing $\mathbb{R}^n$ vectors as columns, is alternating $n$-linear: swapping two columns flips the sign of the determinant, and a determinant with two equal columns vanishes. It is normalized so that $\det(e_1, \dots, e_n) = 1$. By the dimension theorem $\dim \Lambda^n((\mathbb{R}^n)^*) = 1$, every other alternating $n$-tensor on $\mathbb{R}^n$ is a scalar multiple of $\det$. This is the structural reason the determinant exists and is unique.

**Is an instance — the elementary alternating $2$-covector $\varepsilon^{12}$ on $\mathbb{R}^3$.** With the standard dual basis $e^1, e^2, e^3$, the $2$-covector $\varepsilon^{12}(v, w) = v^1 w^2 - v^2 w^1$ is alternating bilinear: it gives the signed area of the projection of the parallelogram spanned by $v, w$ onto the $xy$-plane. On $\mathbb{R}^3$, $\dim \Lambda^2 = \binom{3}{2} = 3$, with basis $\varepsilon^{12}, \varepsilon^{13}, \varepsilon^{23}$.

**Is an instance — the wedge of dual vectors.** For $\omega^1, \dots, \omega^k \in V^*$, the $k$-tensor $(\omega^1 \wedge \cdots \wedge \omega^k)(v_1, \dots, v_k) = \det(\omega^i(v_j))$ is alternating $k$-linear, by alternation of the determinant in columns. This is the construction that builds general alternating tensors from $1$-covectors via the wedge product; see [[Def - The Wedge Product on a Manifold]].

**Is NOT an instance — a symmetric bilinear form.** The Euclidean inner product $\langle u, v\rangle = u \cdot v$ is bilinear but symmetric, not alternating: $\langle u, v\rangle = \langle v, u\rangle$. It is a symmetric tensor, an element of $\operatorname{Sym}^2 V^*$, not of $\Lambda^2 V^*$. It is what Riemannian metrics are, and it is *not* what differential forms are.

**Is NOT an instance — a non-alternating multilinear form.** The $3$-tensor $\alpha(u, v, w) = u^1 v^1 w^1$ on $\mathbb{R}^3$ is trilinear but cubically symmetric in the inputs — it is invariant under permutations of $(u, v, w)$, not antisymmetric. It is an element of $\operatorname{Sym}^3 V^*$.

**Is NOT an instance — a $k$-tensor on $V$ for $k > n$.** On any $n$-dimensional $V$, $\Lambda^k(V^*) = \{0\}$ for $k > n$. Any $k > n$ vectors in $V$ are linearly dependent, so an alternating tensor vanishes on every input. This is what makes the de Rham complex on an $n$-manifold finite, ending at degree $n$.

**Corollary — counting.** $\dim \Lambda^k V^* = \binom{n}{k}$ is the number of $k$-element subsets of $\{1, \dots, n\}$; equivalently the number of increasing multi-indices. On $\mathbb{R}^3$ the [[Def - Dimension|dimensions]] are $1, 3, 3, 1$ for $k = 0, 1, 2, 3$, exhibiting the palindrome from Pascal's triangle that is the root of the vector-field-form identification specific to dimension $3$.

**Corollary — alternating $n$-tensors detect linear independence.** A nonzero $\omega \in \Lambda^n V^*$ satisfies $\omega(v_1, \dots, v_n) \neq 0$ if and only if $v_1, \dots, v_n$ are linearly independent (equivalently, a basis of $V$). This is the algebraic statement behind "$\det T \neq 0 \iff T$ is invertible" and behind the use of nonvanishing $n$-forms as volume forms in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]].

**Corollary — $\binom{n}{k} = \binom{n}{n-k}$.** The dimension count gives a pairing $\Lambda^k V^* \otimes \Lambda^{n-k} V^* \to \Lambda^n V^* \cong \mathbb{R}$ (the wedge into the top space), and once a nonzero top-form is fixed this pairing identifies $\Lambda^k V^*$ with $(\Lambda^{n-k} V^*)^*$. With a metric this identification becomes the **Hodge star** $\star : \Lambda^k \to \Lambda^{n-k}$.

**Calibration check.** Verify that $\dim \Lambda^2 (\mathbb{R}^4)^* = 6$; verify that the form $\omega(u, v, w) = \det(u\ v\ w)$ on $\mathbb{R}^3$ vanishes when $w = u + v$; compute $\varepsilon^{12}(e_1, e_3)$ and $\varepsilon^{12}(e_1 + e_2, e_2)$; check that $\varepsilon^{132} = -\varepsilon^{123}$ on $\mathbb{R}^3$. If you can explain why $\dim \Lambda^k V^* = 0$ for $k > \dim V$ in one sentence, you have understood the definition.

---

# Unlocked by This

> [!tip] Differential $k$-Forms on a Manifold *(this chapter)*
> Replacing $V$ by the tangent space $T_pM$ at each point of a smooth manifold $M$, and demanding smoothness in $p$, gives the bundle $\Lambda^k T^*M$ whose smooth sections are **differential $k$-forms** on $M$. The whole algebraic content of $\Lambda^k V^*$ — wedge product, dimension count, basis of elementary covectors, determinant identity — propagates to the manifold setting unchanged; see [[Def - Differential k-Form on a Manifold]].

> [!tip] The Determinant of a Linear Map *(from Linear Algebra)*
> Since $\dim \Lambda^n V^* = 1$, any linear map $T : V \to V$ induces, via $(T^*\omega)(v_1, \dots, v_n) = \omega(Tv_1, \dots, Tv_n)$, a map $T^* : \Lambda^n V^* \to \Lambda^n V^*$ that is scalar multiplication by some number; that number is $\det T$. The whole construction of the determinant — its multiplicativity, its behavior under change of basis, its vanishing on non-invertible maps — is captured by this one observation. See [[Def - Determinant]].

> [!tip] The Volume Form and Integration on a Manifold *(from Differential Geometry IX)*
> A nowhere-vanishing $n$-form on an $n$-manifold is the prerequisite for **integration**: orientation is a choice between the two connected components of $(\Lambda^n T^*M)_p \setminus \{0\}$ at every point, and the integral $\int_M \omega$ of a top-form $\omega$ is defined patch by patch using the alternating-tensor structure to make the chart overlap multiply by the Jacobian determinant — the *signed* one, which cancels against the determinant from the change-of-variables formula. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

> [!tip] Symplectic Form and Hamiltonian Mechanics *(from Symplectic Geometry)*
> A **symplectic form** on a $2m$-dimensional manifold is a closed, nondegenerate element of $\Lambda^2(V^*)$ at each point, varying smoothly. The nondegeneracy uses the case $k = 2$ of the dimension theorem to set up a bijection $V \to V^*$ via $X \mapsto \iota_X\omega$; the closedness uses the exterior derivative. The whole theory of Hamiltonian mechanics — Poisson brackets, Liouville's theorem on phase space volume, Darboux's theorem on local normal form — is the calculus of a single distinguished element of $\Lambda^2(V^*)$ varying over a manifold.

> [!tip] Spin Representations and Clifford Algebra *(from Representation Theory)*
> The exterior algebra $\Lambda^\bullet V$ (with $V$ replaced by its complexification when working over $\mathbb{C}$) is naturally a module over the **Clifford algebra** $\operatorname{Cl}(V, q)$ for a quadratic form $q$ on $V$. The action of Clifford generators interpolates between $\wedge$ and the metric-dependent contraction, and this is the algebraic underpinning of the spin representation. The whole Dirac-operator story in mathematical physics lives one step downstream from the construction $V \mapsto \Lambda^\bullet V$.
