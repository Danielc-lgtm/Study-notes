---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Multilinear Form"
  - "Def - Symmetric and Alternating Bilinear Form"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $\mathbb{F}$ of characteristic $\neq 2$, and $m \geq 1$ is a positive integer with $n = \dim V$. The space of $m$-linear forms on $V$ is $V^{(m)}$; the subspace of alternating $m$-linear forms is $V^{(m)}_{\mathrm{alt}}$. The set of permutations of $\{1, \dots, m\}$ is $\operatorname{perm}(m)$, and $\operatorname{sign}(\sigma) \in \{\pm 1\}$ is the sign of a permutation.

---

# Axiom Motivation

An alternating multilinear form is the natural generalisation of an alternating [[Def - Symmetric and Alternating Bilinear Form|bilinear form]] to more than two inputs. The motivating examples are the determinant $\det(v_1, \dots, v_n)$ of $n$ column vectors, which is $n$-linear and *vanishes when two columns are equal*; the volume form $\omega(v_1, \dots, v_n)$ that gives the signed volume of a parallelepiped, which vanishes when the parallelepiped degenerates (two edges coincide); and the wedge product $\varphi_1 \wedge \cdots \wedge \varphi_m$ on a vector space, which vanishes on any tuple with repeated entries.

The axiom — vanishing on tuples with a repeated entry — is the algebraic encoding of "this form measures something *intrinsically directional*, like signed volume, that becomes zero when two directions coincide". The reason this generalisation is so structurally rich is the **one-dimensionality theorem**: for $m = n = \dim V$, the space $V^{(n)}_{\mathrm{alt}}$ is *one-dimensional*. There is essentially one alternating $n$-linear form on an $n$-dimensional space, up to scalar — that form is what we will *define* to be the determinant. So the alternating multilinear axiom is not just a curious property; it is the precise condition that makes the determinant well-defined and unique.

**Why the "vanishing on tuples with a repeat" formulation is the right axiom (rather than antisymmetry under swap).** The two are equivalent in characteristic $\neq 2$: from $\alpha(v_1, \dots, v_m) = 0$ when $v_j = v_k$ for some $j \neq k$, applying multilinearity to $\alpha(\dots, u + w, \dots, u + w, \dots) = 0$ (with $u + w$ in slots $j$ and $k$) and expanding gives $\alpha(\dots, u, \dots, w, \dots) + \alpha(\dots, w, \dots, u, \dots) = 0$ — that is, swap of any two slots multiplies by $-1$. Conversely, swap-antisymmetry plus characteristic $\neq 2$ gives $\alpha(v, \dots, v, \dots) = -\alpha(v, \dots, v, \dots)$, hence $2\alpha(v, \dots, v, \dots) = 0$, hence zero.

The "vanishing" form is correct in *every* characteristic, while the "antisymmetric" form is wrong in characteristic 2. More importantly: the vanishing-on-repeats form generalises immediately to "$\alpha = 0$ on linearly dependent lists" (LADR 9.28), which is the structural input-broadening that hooks alternation onto linear independence. The antisymmetric form does not generalise as naturally. So conceptually: an alternating multilinear form is one that *cannot see* the direction of a vector that is already represented in the list, even by linear combinations.

**Per-axiom failure analysis of the alternating condition.** The alternating axiom is a single equation $\alpha(v_1, \dots, v_m) = 0$ whenever some $v_j = v_k$. What breaks if we drop it: the form is not antisymmetric under swap, so $\alpha(v_1, v_2) \neq -\alpha(v_2, v_1)$ in general, and the form has nothing to do with signed volume. What breaks: the form can be nonzero on linearly dependent lists, so it does not detect "spanning" or "independence". What is excluded if we strengthen: there is no natural strengthening of "alternating" — it is already maximally restrictive among the natural conditions on multilinear forms.

**Why the permutation formula matters.** The most important *consequence* of the alternating axiom is that the value of $\alpha$ on any tuple is determined up to a sign by its value on a reordered tuple: for any permutation $\sigma$,

$$\alpha(v_{\sigma(1)}, \dots, v_{\sigma(m)}) = \operatorname{sign}(\sigma)\, \alpha(v_1, \dots, v_m).$$

This is what reduces *all* values of an alternating form on $m$-tuples to one canonical value plus a sign. Combined with multilinearity in each slot, it gives the explicit Leibniz-like formula: an alternating $m$-linear form on $V$ (with $m = n$) is determined by its value on one basis $(e_1, \dots, e_n)$, and the value on a general tuple is computed by expanding each $v_k$ in the basis and using the permutation rule. This is where the formula

$$\alpha(v_1, \dots, v_n) = \alpha(e_1, \dots, e_n) \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma)\, b_{\sigma(1), 1} \cdots b_{\sigma(n), n}$$

comes from (with $v_k = \sum_j b_{jk} e_j$). The sum is the determinant of the matrix $(b_{jk})$, so this single identity simultaneously defines and characterises the determinant.

---

# The Definition

An $m$-linear form $\alpha \in V^{(m)}$ on $V$ is **alternating** if

$$\alpha(v_1, \dots, v_m) = 0$$

whenever the list $v_1, \dots, v_m$ contains a repeated entry — that is, whenever there exist $j \neq k$ in $\{1, \dots, m\}$ with $v_j = v_k$.

The set of alternating $m$-linear forms on $V$ is denoted $V^{(m)}_{\mathrm{alt}}$. It is a [[Def - Subspace|subspace]] of $V^{(m)}$.

**Equivalent characterisations (in characteristic $\neq 2$).** For an $m$-linear form $\alpha$, the following are equivalent:

1. $\alpha$ is alternating: $\alpha(v_1, \dots, v_m) = 0$ when some $v_j = v_k$.
2. **Antisymmetric under transposition.** Swapping any two arguments multiplies the value by $-1$: $\alpha(\dots, v_j, \dots, v_k, \dots) = -\alpha(\dots, v_k, \dots, v_j, \dots)$.
3. **Permutation formula.** For any permutation $\sigma \in \operatorname{perm}(m)$,
$$\alpha(v_{\sigma(1)}, \dots, v_{\sigma(m)}) = \operatorname{sign}(\sigma)\, \alpha(v_1, \dots, v_m).$$
4. **Vanishing on linear dependence.** If $v_1, \dots, v_m$ are linearly dependent, then $\alpha(v_1, \dots, v_m) = 0$.

**[[Def - Dimension|Dimension]] theorem (LADR 9.37).** When $m = n = \dim V$, the space of alternating $n$-linear forms on $V$ is **one-dimensional**:

$$\dim V^{(n)}_{\mathrm{alt}} = 1.$$

More generally, $\dim V^{(m)}_{\mathrm{alt}} = \binom{n}{m}$ for $1 \leq m \leq n$, and $\dim V^{(m)}_{\mathrm{alt}} = 0$ for $m > n$.

**Permutation-sum formula.** Let $(e_1, \dots, e_n)$ be a basis of $V$, with $n = \dim V$. The alternating $n$-linear form satisfying $\alpha(e_1, \dots, e_n) = 1$ — the unique such form, given the one-dimensionality theorem — has explicit formula

$$\alpha(v_1, \dots, v_n) = \sum_{\sigma \in \operatorname{perm}(n)} \operatorname{sign}(\sigma)\, b_{\sigma(1), 1}\, b_{\sigma(2), 2}\, \cdots b_{\sigma(n), n},$$

where $v_k = \sum_j b_{jk} e_j$. The right-hand side is the Leibniz formula for $\det(b_{jk})$, the determinant of the matrix whose columns are the coordinates of $v_1, \dots, v_n$ in the basis $(e_j)$. This is the route by which the determinant emerges as "the unique alternating $n$-linear form normalised to give 1 on the standard basis".

---

# Categorical / Structural Definition

The categorical formulation places alternating multilinear forms in their natural home.

**An alternating $m$-linear form on $V$ is a linear functional on the exterior power $\Lambda^m V$.** The **exterior power** $\Lambda^m V$ is the quotient of $V^{\otimes m}$ by the [[Def - Subspace|subspace]] generated by tensors of the form $v_1 \otimes \cdots \otimes v_m$ with $v_j = v_k$ for some $j \neq k$. The image of $v_1 \otimes \cdots \otimes v_m$ in this quotient is denoted $v_1 \wedge \cdots \wedge v_m$ — the **wedge product**.

The universal property of the exterior power: every alternating $m$-linear map $V^m \to U$ (any vector space $U$) factors uniquely through the canonical projection $V^m \to \Lambda^m V$, $(v_1, \dots, v_m) \mapsto v_1 \wedge \cdots \wedge v_m$. Specialising to $U = \mathbb{F}$ gives the natural isomorphism

$$V^{(m)}_{\mathrm{alt}} \;\cong\; (\Lambda^m V)^*.$$

The [[Def - Dimension|dimension]] $\binom{n}{m}$ of $V^{(m)}_{\mathrm{alt}}$ matches $\dim \Lambda^m V$, with the top dimension $\dim \Lambda^n V = 1$ matching $\dim V^{(n)}_{\mathrm{alt}} = 1$ — which is *the* fact that makes the determinant well-defined.

**A direct sum reading.** The whole tensor algebra splits as

$$V^{\otimes m} \;=\; \operatorname{Sym}^m V \;\oplus\; \Lambda^m V \;\oplus\; (\text{mixed symmetry types})$$

— at least for $m = 2$. For $m \geq 3$, the decomposition into "irreducible representations of the symmetric [[Def - Group|group]] $S_m$" includes more than just symmetric and antisymmetric pieces (it includes Young-diagram-indexed components). But the alternating part is always one specific piece of this decomposition, picked out by antisymmetrisation.

---

# Relate to Other Fields / Compression

An alternating multilinear form is **the natural multi-input generalisation of the determinant**. The single-input case ($m = 1$) is just a linear functional, the two-input alternating bilinear form is a "signed area" measure, and the $n$-input case on an $n$-dimensional space is the determinant. The intermediate cases ($1 < m < n$) measure signed volumes of $m$-dimensional parallelepipeds embedded in an $n$-dimensional space, and they form the **wedge product algebra** $\Lambda^* V^*$ used throughout differential geometry.

From the algebraic viewpoint, alternating multilinear forms are the dual of the exterior algebra: $V^{(m)}_{\mathrm{alt}} \cong (\Lambda^m V)^*$. The whole structure of differential forms on a manifold lives in the alternating multilinear framework applied pointwise to tangent spaces.

**True name:** An alternating multilinear form is "a signed-volume gadget" — it measures the oriented $m$-dimensional content of an $m$-tuple of vectors, and it vanishes when the tuple is degenerate (linearly dependent).

A trigger-reaction pattern: **see "alternating multilinear" → think "exterior algebra / wedge product / signed volume / determinant"**. Whenever a construction is multilinear and antisymmetric in some arguments, the right framework is the alternating-multilinear-forms space, and the natural objects are wedge products.

---

# Examples / Corollaries

**Is an instance: the determinant of $n$ columns.** $\det : (\mathbb{F}^n)^n \to \mathbb{F}$, $(v_1, \dots, v_n) \mapsto \det(v_1\ v_2\ \cdots\ v_n)$, is alternating $n$-linear by definition (or by the multilinear-alternating-uniqueness characterisation). It is the unique alternating $n$-linear form on $\mathbb{F}^n$ with $\det(e_1, \dots, e_n) = 1$.

**Is an instance: the cross product (regarded as $\mathbb{R}^3$-valued).** On $\mathbb{R}^3$, the cross product $u \times v$ is a vector, but the bilinear form $\omega(u, v, w) = (u \times v) \cdot w$ is alternating trilinear: it vanishes when any two of $u, v, w$ coincide (e.g., $u = v$ gives $u \times u = 0$). It is exactly the volume form on $\mathbb{R}^3$, equal to the determinant of the matrix $(u\ v\ w)$.

**Is an instance: the wedge product of dual vectors.** For $\varphi_1, \dots, \varphi_m \in V^*$, define

$$(\varphi_1 \wedge \cdots \wedge \varphi_m)(v_1, \dots, v_m) := \det[\varphi_i(v_j)]_{i, j = 1}^m.$$

The determinant of the $m \times m$ matrix $[\varphi_i(v_j)]$ is alternating in the columns $(v_j)$ (because [[Def - Determinant|determinants]] are alternating in columns), so this is alternating $m$-linear in $(v_1, \dots, v_m)$. Wedge products of basis dual vectors $e^*_{i_1} \wedge \cdots \wedge e^*_{i_m}$ (with $i_1 < \cdots < i_m$) form a basis of $V^{(m)}_{\mathrm{alt}}$.

**Is an instance: any alternating bilinear form (from §9A).** When $m = 2$, the alternating $m$-linear forms are exactly the alternating bilinear forms of §9A: $\dim V^{(2)}_{\mathrm{alt}} = \binom{n}{2}$, parametrised by antisymmetric $n \times n$ matrices.

**Is an instance: the "[[Def - Pfaffian|Pfaffian]]" associated with a symplectic form.** For an antisymmetric $2n \times 2n$ matrix $A$, the **[[Def - Pfaffian|Pfaffian]]** $\operatorname{Pf}(A)$ is the unique polynomial in entries of $A$ with $\operatorname{Pf}(A)^2 = \det(A)$ and $\operatorname{Pf}(J) = 1$ for the standard symplectic matrix. It arises naturally from alternating bilinear-form theory and has interpretation as a top wedge product.

**Is NOT an instance: a general (non-alternating) multilinear form.** The trace product $\operatorname{tr}(T_1 T_2 \cdots T_m)$ on $\mathcal{L}(V)^m$ is multilinear but only cyclic, not antisymmetric. In particular $\operatorname{tr}(T_1 T_2) = \operatorname{tr}(T_2 T_1)$ is *symmetric* in two slots, not antisymmetric.

**Is NOT an instance: a symmetric multilinear form.** The form $(v_1, \dots, v_m) \mapsto \prod_i \varphi(v_i)$ for a fixed linear functional $\varphi$ is multilinear and symmetric in all arguments (because each slot uses the same $\varphi$). It is the opposite extreme from alternating.

**Is NOT an instance for $m > n$.** When $m > n = \dim V$, *every* alternating $m$-linear form is zero. This is because any $m$-tuple in an $n$-dimensional space is linearly dependent (for $m > n$), and alternating forms vanish on dependent lists. So $V^{(m)}_{\mathrm{alt}} = \{0\}$ for $m > n$.

**Corollary (alternating forms on linearly dependent lists).** If $\alpha \in V^{(m)}_{\mathrm{alt}}$ and $v_1, \dots, v_m$ are linearly dependent, then $\alpha(v_1, \dots, v_m) = 0$. Proof: by linear dependence, some $v_k = \sum_{j \neq k} a_j v_j$; substituting and expanding by multilinearity gives a sum of terms each having a repeated vector, all of which are zero by the alternating axiom. This is LADR 9.28.

**Corollary (alternating $n$-linear forms are nonzero exactly on bases).** For a nonzero $\alpha \in V^{(n)}_{\mathrm{alt}}$, the value $\alpha(v_1, \dots, v_n) \neq 0$ if and only if $v_1, \dots, v_n$ is linearly independent (equivalently, a basis since $n = \dim V$). This is LADR 9.39, and it is the structural fact that makes the determinant detect invertibility: $\det T \neq 0$ iff $T$ sends a basis to a basis.

**Corollary (one-dimensionality at top).** $\dim V^{(n)}_{\mathrm{alt}} = 1$ when $n = \dim V$. So any two nonzero alternating $n$-linear forms differ by a nonzero scalar. This is the structural foundation for the determinant.

**Calibration check.** If you have understood the definition, you should be able to: (i) compute $\dim V^{(m)}_{\mathrm{alt}} = \binom{n}{m}$ by counting the number of strictly increasing tuples $1 \leq i_1 < i_2 < \cdots < i_m \leq n$; (ii) verify that on $\mathbb{F}^3$ the form $\alpha(u, v, w) = u_1 v_2 w_3 - u_2 v_1 w_3 + u_3 v_1 w_2 - u_1 v_3 w_2 + u_2 v_3 w_1 - u_3 v_2 w_1$ is alternating 3-linear with $\alpha(e_1, e_2, e_3) = 1$ (it is the determinant); and (iii) verify that the wedge product $e^*_1 \wedge e^*_2 \in V^{(2)}_{\mathrm{alt}}$ evaluated on $(v_1, v_2)$ gives $\det\begin{pmatrix} v_1^1 & v_2^1 \\ v_1^2 & v_2^2 \end{pmatrix}$ — the upper-left $2 \times 2$ minor of the column-arrangement.

---

# Unlocked by This

> [!tip] Determinant *(LADR §9C)*
> The unique scalar attached to an operator by its action on the one-dimensional space $V^{(n)}_{\mathrm{alt}}$. See [[Def - Determinant]]. The whole § 9C is built on the alternating-multilinear framework defined here.

> [!tip] Wedge Product and Exterior Algebra *(from Algebra and Differential Geometry)*
> The exterior algebra $\Lambda^* V = \bigoplus_m \Lambda^m V$ packages all alternating multilinear constructions into a single graded algebra. The wedge product $v_1 \wedge \cdots \wedge v_m$ is the universal alternating multilinear gadget, and $\Lambda^m V$ has dimension $\binom{n}{m}$. **Differential forms** are sections of the exterior bundle $\Lambda^m T^*M$.

> [!tip] Stokes' Theorem *(from Differential Geometry)*
> The generalised Stokes' theorem $\int_M d\omega = \int_{\partial M} \omega$ for a differential $k$-form $\omega$ on an oriented $(k+1)$-dimensional manifold $M$ with boundary. The entire machinery requires the integrand to be an *alternating* multilinear form (so that orientation reversal flips its sign and the integral changes sign under reorientation, matching the boundary orientation).

> [!tip] Volume Form *(from Differential Geometry)*
> A non-vanishing top-degree alternating form on an oriented manifold gives the natural volume measure. Two distinct volume forms differ by a positive scalar function. See [[Linear Algebra IX — §9 Multilinear Algebra and Determinants#Concept Map]] for the connection to the Riemannian volume form $\sqrt{\det g}\, dx^1 \wedge \cdots \wedge dx^n$.
