---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Complex Representations of U(1) and SU(2)"
  - "Def - Constructions on Representations"
  - "Def - Representation of a Lie Group"
  - "Def - Representation of a Lie Algebra"
  - "Def - Tensor Product of Vector Spaces"
  - "Thm - Determinant is Multiplicative"
tags: [geometry, gauge-theory, representation-theory]
---

# Problem Statement

Let $\varrho_1 = \varrho_{\mathrm{st}} \colon SU(2) \to GL(2; \mathbb{C})$ be the **standard representation** of $SU(2)$ on $V = \mathbb{C}^2$, the inclusion $g \mapsto g$; let $(e_1, e_2)$ be the standard basis of $\mathbb{C}^2$. Let $\varrho_0$ be the trivial one-dimensional representation and $\varrho_2 = \odot^2 \varrho_1$ the symmetric-square representation on $\odot^2 \mathbb{C}^2$ (complex dimension $3$). Prove the smallest Clebsch–Gordan decomposition for $SU(2)$,
$$\varrho_1 \otimes \varrho_1 \;\cong\; \varrho_2 \oplus \varrho_0,$$
by the following two-part route, and thereby account for the full decomposition of the four-dimensional space $\mathbb{C}^2 \otimes \mathbb{C}^2$ into irreducible pieces.

1. **Weight bookkeeping.** Compute the weights (the eigenvalues of the diagonal generator $H = \operatorname{diag}(1, -1) \in \mathfrak{sl}(2; \mathbb{C})$) of $\varrho_1 \otimes \varrho_1$, obtaining the multiset $\{2, 0, 0, -2\}$, and deduce from the classification of $SU(2)$-representations that the only decomposition into irreducibles compatible with this multiset is $\varrho_2 \oplus \varrho_0$.
2. **The invariant vector.** Exhibit the concrete one-dimensional invariant subspace realising the $\varrho_0$ summand: the antisymmetric vector
$$\omega \;=\; e_1 \otimes e_2 - e_2 \otimes e_1 \;\in\; \mathbb{C}^2 \otimes \mathbb{C}^2,$$
verify $(\varrho_1 \otimes \varrho_1)(g)\,\omega = \omega$ for every $g \in SU(2)$, and identify the complementary symmetric subspace as a copy of $\varrho_2$.

This is the base case ($j = \tfrac12$ coupled to $j = \tfrac12$ gives spin $1$ plus spin $0$, the physicist's singlet–triplet splitting) of the general rule $\varrho_k \otimes \varrho_l \cong \varrho_{k+l} \oplus \varrho_{k+l-2} \oplus \dots \oplus \varrho_{|k-l|}$.

**Recall:**

The objects in play are the standard, trivial, symmetric-square, and tensor-product representations of $SU(2)$, the classification of its complex representations, and the notion of an invariant subspace.

![[Thm - Complex Representations of U(1) and SU(2)#Statement]]

Only Part (B) is used here: with $\varrho_0$ the trivial representation of $SU(2)$ on $\mathbb{C}$, $\varrho_1$ the standard representation on $\mathbb{C}^2$, and $\varrho_k = \odot^k \varrho_1$ on $\odot^k \mathbb{C}^2$ (dimension $k+1$), each $\varrho_k$ is irreducible, the $\varrho_k$ are pairwise inequivalent, and every finite-dimensional complex representation of $SU(2)$ is equivalent to a direct sum of the $\varrho_k$, uniquely up to the order of the summands. We also use one fact drawn from that theorem's proof (its weight computation, Lemma 7): the representation $\varrho_k$ has, as the eigenvalues of $H = \operatorname{diag}(1, -1)$ on its representation space, exactly the integers $k, k-2, k-4, \dots, -k$, each occurring once. In particular $\varrho_2$ has weights $\{2, 0, -2\}$ and $\varrho_0$ has the single weight $\{0\}$.

![[Def - Constructions on Representations#The Definition]]

The three constructions we use are the [[Def - Constructions on Representations|direct sum]], [[Def - Constructions on Representations|tensor product]], and [[Def - Constructions on Representations|exterior power]] of representations. For representations $\sigma_i \colon G \to GL(W_i)$, the **tensor product** $\sigma_1 \otimes \sigma_2$ acts on $W_1 \otimes W_2$ by $(\sigma_1 \otimes \sigma_2)(g) = \sigma_1(g) \otimes \sigma_2(g)$, the linear map determined on decomposable tensors by $(\sigma_1(g) \otimes \sigma_2(g))(w_1 \otimes w_2) = \sigma_1(g)w_1 \otimes \sigma_2(g)w_2$. The **direct sum** $\sigma_1 \oplus \sigma_2$ acts on $W_1 \oplus W_2$ by $g \mapsto \sigma_1(g) \oplus \sigma_2(g)$. The **second exterior power** $\Lambda^2 \sigma$ acts on the line $\Lambda^2 W$ (for $\dim W = 2$) by $g \mapsto \det \sigma(g)$, since a linear map $T$ on a two-dimensional space acts on $\Lambda^2 W$ as multiplication by $\det T$. For $W = \mathbb{C}^2$, the two-dimensional tensor space splits canonically as the $G$-invariant direct sum $\mathbb{C}^2 \otimes \mathbb{C}^2 = \odot^2 \mathbb{C}^2 \oplus \Lambda^2 \mathbb{C}^2$ of symmetric and antisymmetric tensors, of dimensions $3$ and $1$.

![[Def - Representation of a Lie Algebra#The Definition]]

We shall pass to the complexified Lie algebra $\mathfrak{sl}(2; \mathbb{C}) = \mathfrak{su}(2) \otimes_{\mathbb{R}} \mathbb{C}$, whose standard basis is
$$H = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad F = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \qquad [H, E] = 2E,\ \ [H, F] = -2F,\ \ [E, F] = H,$$
following the conventions of [[Thm - Complex Representations of U(1) and SU(2)|the classification theorem]]. Note that $H$ itself is not anti-Hermitian, so $H \notin \mathfrak{su}(2)$; but $iH = \operatorname{diag}(i, -i) \in \mathfrak{su}(2)$, and $H \in \mathfrak{sl}(2; \mathbb{C})$. For a representation $\varrho$ of $SU(2)$ we write $\lambda = \varrho_* \colon \mathfrak{su}(2) \to \mathfrak{gl}(V)$ for its differential at the identity, extended complex-linearly to $\mathfrak{sl}(2; \mathbb{C})$; a **weight** of $\varrho$ is an eigenvalue $\mu \in \mathbb{C}$ of $\lambda(H)$, and a **weight vector** is a corresponding eigenvector. For the standard representation $\varrho_1$ the differential is the inclusion, so $\lambda_1(H) = H$, giving $H e_1 = e_1$ and $H e_2 = -e_2$: the weights of $\varrho_1$ are $\{+1, -1\}$.

> [!warning] Convention: which generator carries the weight
> The weight of a representation is read off from $H = \operatorname{diag}(1, -1)$, the diagonal element of $\mathfrak{sl}(2; \mathbb{C})$, not from $iH = \operatorname{diag}(i, -i) \in \mathfrak{su}(2)$. On the compact group the relevant one-parameter subgroup is $t \mapsto \exp(t\, iH) = \operatorname{diag}(e^{it}, e^{-it})$; its restriction to the standard representation has eigenvalues $e^{\pm it}$, and the integers $\pm 1$ in the exponents are precisely the weights. Some sources use $j = k/2$ ("spin") in place of the highest weight $k$; here every weight and every highest weight is the integer $k$, never the half-integer $j$.

---

# Convergent Strategy

**Problem class.** This is a *decompose-a-representation* problem: we are given a reducible representation ($\varrho_1 \otimes \varrho_1$) built by a functorial construction from a known irreducible, and we must express it as a direct sum of irreducibles from a known classified list. Such problems are the atoms of the Clebsch–Gordan calculus, and for a compact group with a fully classified representation theory they are *always solvable by counting a single discrete invariant* — here the multiset of weights. The lesson of the problem class is that once a representation theory is classified up to isomorphism by a numerical invariant, decomposition stops being an act of construction and becomes an act of arithmetic.

**Assumption pattern.** Two hypotheses about $SU(2)$ are doing all the work, and it is worth naming exactly where each is used. First, **complete reducibility**: because $SU(2)$ is compact, every finite-dimensional complex representation is a direct sum of irreducibles, so $\varrho_1 \otimes \varrho_1$ is *guaranteed in advance* to be $\bigoplus_i \varrho_{k_i}$ for some multiset $\{k_i\}$ — we never have to worry that it might be an indecomposable-but-reducible extension. Second, the **weight dictionary**: each irreducible $\varrho_k$ is pinned down by, and its weight multiset is exactly, the ladder $\{k, k-2, \dots, -k\}$. Together these convert "which irreducibles appear, and with what multiplicity?" into "which ladders $\{k, k-2, \dots, -k\}$ partition the observed weight multiset?", a finite combinatorial question with a unique answer.

**Theorem routing.** The route is: (i) compute the weights of $\varrho_1 \otimes \varrho_1$ from the weights of $\varrho_1$ via the additivity of weights under tensor product — the differential of a tensor product satisfies the Leibniz rule $\lambda_{\otimes}(H) = \lambda_1(H) \otimes I + I \otimes \lambda_1(H)$, so weights add — obtaining $\{1+1, 1-1, -1+1, -1-1\} = \{2, 0, 0, -2\}$; (ii) invoke [[Thm - Complex Representations of U(1) and SU(2)|complete reducibility]] to know $\varrho_1 \otimes \varrho_1 \cong \bigoplus_i \varrho_{k_i}$; (iii) run the *peel-off-the-highest-weight* algorithm on the multiset $\{2, 0, 0, -2\}$, forced by the weight dictionary, to conclude $\{k_i\} = \{2, 0\}$, hence $\varrho_1 \otimes \varrho_1 \cong \varrho_2 \oplus \varrho_0$; (iv) confirm the abstract count concretely by exhibiting the invariant vector $\omega = e_1 \otimes e_2 - e_2 \otimes e_1$ spanning the $\varrho_0$ summand and identifying its symmetric complement with $\varrho_2 = \odot^2 \varrho_1$.

**Key decision point.** The single non-obvious move is *to change categories* — to leave the group $SU(2)$, where the tensor product $\varrho_1(g) \otimes \varrho_1(g)$ is a $4 \times 4$ matrix depending on a continuum of parameters, and pass to the one diagonalisable operator $\lambda_{\otimes}(H)$ on $\mathbb{C}^2 \otimes \mathbb{C}^2$, whose four integer eigenvalues carry the entire decomposition. The temptation is to try to spot invariant subspaces of the $4 \times 4$ group action by inspection; the disciplined move is to compute one operator's spectrum and let the classification theorem read the answer off it. The second decision point, in the constructive half, is recognising that the antisymmetric line is the invariant one *because* $SU(2)$ consists of determinant-one matrices, so that $\Lambda^2 \varrho_1 = \det \varrho_1 = \varrho_0$ is forced by the defining constraint $\det g = 1$; the symmetric complement then absorbs the remaining three dimensions, which can only be $\varrho_2$ once one dimension of trivial has been split off.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory I — Lie Groups, Representations, and Group Actions#Legal Operations|the topic page's Legal Operations]]; where the topic page numbers them differently, the descriptive names below identify each.

1. **Differentiate a group representation to its Lie algebra.** Replace the standard group representation $\varrho_1$ by its differential $\lambda_1 = \varrho_{1*}$, and the tensor product $\varrho_1 \otimes \varrho_1$ by its differential $\lambda_\otimes$, in order to work with the single diagonal operator $\lambda_\otimes(H)$ instead of a family of group elements.

2. **Apply the Leibniz rule for the differential of a tensor product.** From $(\varrho_1 \otimes \varrho_1)(g) = \varrho_1(g) \otimes \varrho_1(g)$ derive, by the product rule, $\lambda_\otimes(X) = \lambda_1(X) \otimes I + I \otimes \lambda_1(X)$; this is the operation that makes weights *add* under tensor product.

3. **Read off weights as eigenvalues of $H$.** Diagonalise $\lambda_\otimes(H)$ on the basis $\{e_i \otimes e_j\}$ to obtain the weight multiset $\{2, 0, 0, -2\}$.

4. **Invoke complete reducibility of a compact-group representation.** Use the classification theorem to assert that $\varrho_1 \otimes \varrho_1$ is a direct sum of the irreducibles $\varrho_k$, so that its isomorphism class is determined by the multiplicities of the $\varrho_k$.

5. **Peel off the highest weight to identify irreducible summands.** Using that $\varrho_k$ contributes exactly the ladder $\{k, k-2, \dots, -k\}$, extract from the observed weight multiset the largest weight (which must be a highest weight of some summand), remove the ladder it heads, and repeat until the multiset is exhausted.

6. **Split $V \otimes V$ into symmetric and antisymmetric tensors as an invariant decomposition.** Use that the diagonal $G$-action commutes with the transposition of tensor factors, so $\mathbb{C}^2 \otimes \mathbb{C}^2 = \odot^2 \mathbb{C}^2 \oplus \Lambda^2 \mathbb{C}^2$ is a decomposition into subrepresentations.

7. **Identify a top exterior power with a determinant character.** On the line $\Lambda^2 \mathbb{C}^2$ the representation $\Lambda^2 \varrho_1$ acts by $\det \varrho_1(g) = \det g$; the constraint $\det g = 1$ defining $SU(2)$ makes this the trivial representation $\varrho_0$.

---

# Hints

> [!note]- Hint 1
> Do not try to find invariant subspaces of the $4 \times 4$ matrices $\varrho_1(g) \otimes \varrho_1(g)$ by staring at them. Instead, leave the group and go to the Lie algebra: the whole decomposition is encoded in the eigenvalues of one operator. Which operator? The image of $H = \operatorname{diag}(1, -1)$ under the differential of $\varrho_1 \otimes \varrho_1$.

> [!note]- Hint 2
> The standard representation $\varrho_1$ has $H e_1 = e_1$ and $H e_2 = -e_2$, so its weights are $+1$ and $-1$. Weights *add* under tensor product, because the differential of a tensor product obeys the Leibniz rule $\lambda_\otimes(H) = \lambda_1(H) \otimes I + I \otimes \lambda_1(H)$. Apply this to each of the four basis tensors $e_i \otimes e_j$ and list the four weights.

> [!note]- Hint 3
> You should find the weight multiset $\{2, 0, 0, -2\}$. Now recall two facts from the classification theorem: (a) $\varrho_1 \otimes \varrho_1$ is a direct sum of irreducibles $\varrho_k$ (compactness); (b) $\varrho_k$ has weights exactly $\{k, k-2, \dots, -k\}$. The largest weight present, $2$, must be the top of some $\varrho_k$ — so $k = 2$ appears. Remove the ladder $\{2, 0, -2\}$ from $\{2, 0, 0, -2\}$. What is left, and which $\varrho_k$ has that weight?

> [!note]- Hint 4
> After removing $\{2, 0, -2\}$ you are left with the single weight $\{0\}$, which is the weight set of $\varrho_0$. So $\varrho_1 \otimes \varrho_1 \cong \varrho_2 \oplus \varrho_0$. To make the trivial summand concrete: the one place a trivial $SU(2)$-subrepresentation of $\mathbb{C}^2 \otimes \mathbb{C}^2$ can hide is the antisymmetric line, because $SU(2)$ matrices have determinant $1$. Write down the antisymmetric vector $e_1 \otimes e_2 - e_2 \otimes e_1$ and act on it by a general $g = \begin{pmatrix} a & -\bar b \\ b & \bar a \end{pmatrix}$.

---

# Solution

The proof has two independent halves that confirm each other. The first is pure arithmetic: differentiate the tensor product, read the four weights $\{2, 0, 0, -2\}$ off the diagonal operator $\lambda_\otimes(H)$, and let the classification theorem convert this multiset into the summand list $\{2, 0\}$ by peeling off the highest weight. The second is an explicit construction: split $\mathbb{C}^2 \otimes \mathbb{C}^2$ into its three-dimensional symmetric and one-dimensional antisymmetric parts, recognise the antisymmetric line as the trivial representation because $SU(2)$ acts on it by $\det g = 1$, and recognise the symmetric part as $\varrho_2 = \odot^2 \varrho_1$ by definition. The invariant vector $\omega = e_1 \otimes e_2 - e_2 \otimes e_1$ is the visible generator of the singlet, and computing $g \cdot \omega$ for a general $g$ shows directly that it is fixed.

**Step 1: The differential of the tensor product satisfies the Leibniz rule, so weights add.**

Let $\lambda_1 = \varrho_{1*}$ be the differential of the standard representation and $\lambda_\otimes = (\varrho_1 \otimes \varrho_1)_*$ the differential of the tensor square. Then, extended complex-linearly to $\mathfrak{sl}(2; \mathbb{C})$,
$$\lambda_\otimes(H) = \lambda_1(H) \otimes I + I \otimes \lambda_1(H).$$

> [!note]- Derivation
> Fix $X \in \mathfrak{su}(2)$ and consider the smooth curve $t \mapsto \exp(tX) \in SU(2)$, which passes through the identity at $t = 0$ with velocity $X$. By the definition of the tensor product of representations, $(\varrho_1 \otimes \varrho_1)(\exp tX) = \varrho_1(\exp tX) \otimes \varrho_1(\exp tX)$. Differentiating at $t = 0$ and using the product rule for the bilinear map $(A, B) \mapsto A \otimes B$ (which is legitimate because $\otimes$ is bilinear, hence smooth, and its derivative is computed factorwise),
> $$\lambda_\otimes(X) = \frac{d}{dt}\Big|_{t=0} \big[\varrho_1(\exp tX) \otimes \varrho_1(\exp tX)\big] \qquad \text{(definition of the differential of } \varrho_1 \otimes \varrho_1\text{)}$$
> $$= \Big(\frac{d}{dt}\Big|_{0}\varrho_1(\exp tX)\Big) \otimes \varrho_1(\exp 0) + \varrho_1(\exp 0) \otimes \Big(\frac{d}{dt}\Big|_{0}\varrho_1(\exp tX)\Big) \qquad \text{(product rule for the bilinear map } \otimes\text{)}$$
> $$= \lambda_1(X) \otimes I + I \otimes \lambda_1(X) \qquad \text{(since } \varrho_1(\exp 0) = \varrho_1(e) = I \text{ and } \tfrac{d}{dt}|_0\varrho_1(\exp tX) = \lambda_1(X)\text{)}.$$
> This identity holds for every $X \in \mathfrak{su}(2)$, and both sides are complex-linear in $X$, so it extends to every $X \in \mathfrak{su}(2) \otimes_{\mathbb{R}} \mathbb{C} = \mathfrak{sl}(2; \mathbb{C})$. In particular it holds for $X = H = \operatorname{diag}(1, -1)$, even though $H \notin \mathfrak{su}(2)$: we obtain it by applying the real identity to $iH \in \mathfrak{su}(2)$ and dividing by $i$, which is exactly the complex-linear extension. This is the sense in which **weights add under tensor product**: if $u$ is a weight vector of the first factor with weight $\mu$ and $v$ a weight vector of the second with weight $\nu$, then
> $$\lambda_\otimes(H)(u \otimes v) = (\lambda_1(H)u) \otimes v + u \otimes (\lambda_1(H)v) = \mu\, u \otimes v + \nu\, u \otimes v = (\mu + \nu)\, u \otimes v,$$
> so $u \otimes v$ is a weight vector of $\varrho_1 \otimes \varrho_1$ with weight $\mu + \nu$.

**Step 2: The weights of $\varrho_1 \otimes \varrho_1$ are the multiset $\{2, 0, 0, -2\}$.**

Applying $\lambda_\otimes(H)$ to the four basis tensors $e_i \otimes e_j$ gives eigenvalues $2, 0, 0, -2$.

> [!note]- Derivation
> The standard representation has $\lambda_1(H) = H$, with $H e_1 = e_1$ (weight $+1$) and $H e_2 = -e_2$ (weight $-1$); the basis $(e_1, e_2)$ therefore consists of weight vectors of $\varrho_1$ with weights $+1$ and $-1$. The four tensors $e_i \otimes e_j$ ($i, j \in \{1, 2\}$) form a basis of $\mathbb{C}^2 \otimes \mathbb{C}^2$, and each is a weight vector of $\varrho_1 \otimes \varrho_1$ by the additivity established in Step 1:
> $$\lambda_\otimes(H)(e_1 \otimes e_1) = (1 + 1)\, e_1 \otimes e_1 = 2\, e_1 \otimes e_1 \qquad \text{(weight } 2\text{)},$$
> $$\lambda_\otimes(H)(e_1 \otimes e_2) = (1 + (-1))\, e_1 \otimes e_2 = 0 \qquad \text{(weight } 0\text{)},$$
> $$\lambda_\otimes(H)(e_2 \otimes e_1) = ((-1) + 1)\, e_2 \otimes e_1 = 0 \qquad \text{(weight } 0\text{)},$$
> $$\lambda_\otimes(H)(e_2 \otimes e_2) = ((-1) + (-1))\, e_2 \otimes e_2 = -2\, e_2 \otimes e_2 \qquad \text{(weight } -2\text{)}.$$
> Since these four tensors form a basis, the operator $\lambda_\otimes(H)$ is diagonal in this basis with diagonal entries $2, 0, 0, -2$; its spectrum, counted with multiplicity, is the **weight multiset**
> $$\mathcal{W}(\varrho_1 \otimes \varrho_1) = \{2,\ 0,\ 0,\ -2\}.$$
> The weight $0$ occurs twice — from $e_1 \otimes e_2$ and from $e_2 \otimes e_1$ — and this is the sole multiplicity above one; it is exactly this doubled zero that will force a $\varrho_0$ summand alongside the $\varrho_2$.

**Step 3: The classification forces $\varrho_1 \otimes \varrho_1 \cong \varrho_2 \oplus \varrho_0$.**

By complete reducibility $\varrho_1 \otimes \varrho_1 \cong \bigoplus_i \varrho_{k_i}$, and matching weight multisets forces the multiset $\{k_i\}$ to be $\{2, 0\}$.

> [!note]- Derivation
> By Part (B) of [[Thm - Complex Representations of U(1) and SU(2)|the classification theorem]] — *every finite-dimensional complex representation of $SU(2)$ is equivalent to a direct sum $\bigoplus_i \varrho_{k_i}$ of the irreducibles $\varrho_k$, uniquely up to the order of the summands* — there is a multiset of nonnegative integers $\{k_1, \dots, k_r\}$ with
> $$\varrho_1 \otimes \varrho_1 \;\cong\; \varrho_{k_1} \oplus \dots \oplus \varrho_{k_r}.$$
> Weights are additive over direct sums: a weight vector of $\varrho_{k_i}$ is a weight vector of the sum with the same weight, and a basis of weight vectors of the sum is the union of bases of weight vectors of the summands. Hence the weight multiset of the sum is the disjoint union of the weight multisets of the summands. Using the weight computation of the theorem's proof (Lemma 7), *the weight multiset of $\varrho_k$ is exactly the ladder $\{k, k-2, k-4, \dots, -k\}$, each weight once*, we get
> $$\mathcal{W}(\varrho_1 \otimes \varrho_1) = \bigsqcup_{i} \{k_i,\ k_i - 2,\ \dots,\ -k_i\}.$$
> Combined with Step 2, the right-hand side must equal $\{2, 0, 0, -2\}$. We solve this by the **peel-off-the-highest-weight** procedure.
>
> *Extract the top ladder.* The largest weight appearing in $\{2, 0, 0, -2\}$ is $2$. In the disjoint union $\bigsqcup_i \{k_i, \dots, -k_i\}$ the largest weight present equals $\max_i k_i$, because each ladder tops out at its own $k_i$. Therefore $\max_i k_i = 2$, so some summand is $\varrho_2$, contributing the ladder $\{2, 0, -2\}$. Removing this ladder from the total multiset,
> $$\{2, 0, 0, -2\} \setminus \{2, 0, -2\} = \{0\}.$$
> *Extract the next ladder.* The remaining multiset $\{0\}$ has largest weight $0$, so a further summand $\varrho_0$ contributes the ladder $\{0\}$. Removing it leaves the empty multiset, and the procedure terminates.
>
> Hence $\{k_i\} = \{2, 0\}$, and no other multiset of nonnegative integers reproduces $\{2, 0, 0, -2\}$: any decomposition must contain a top ladder headed by the maximum $2$ and, after its removal, a ladder headed by $0$, and these are uniquely $\varrho_2$ and $\varrho_0$. By the uniqueness clause of the classification, this determines the isomorphism class, so
> $$\varrho_1 \otimes \varrho_1 \;\cong\; \varrho_2 \oplus \varrho_0.$$
> A dimension check confirms consistency: $\dim(\varrho_1 \otimes \varrho_1) = 2 \cdot 2 = 4$ and $\dim \varrho_2 + \dim \varrho_0 = 3 + 1 = 4$.

**Step 4: The invariant vector $\omega = e_1 \otimes e_2 - e_2 \otimes e_1$ spans the $\varrho_0$ summand.**

The antisymmetric line $\mathbb{C}\omega$ is a trivial subrepresentation, because $SU(2)$ acts on $\Lambda^2 \mathbb{C}^2$ by $\det g = 1$; a direct group-level computation confirms $(\varrho_1 \otimes \varrho_1)(g)\,\omega = \omega$.

> [!note]- Derivation
> **The abstract reason.** The tensor square splits, invariantly under the diagonal action, into symmetric and antisymmetric parts,
> $$\mathbb{C}^2 \otimes \mathbb{C}^2 = \odot^2 \mathbb{C}^2 \oplus \Lambda^2 \mathbb{C}^2, \qquad \dim \odot^2 \mathbb{C}^2 = 3,\ \dim \Lambda^2 \mathbb{C}^2 = 1.$$
> This decomposition is $G$-invariant because the transposition operator $\tau(u \otimes v) = v \otimes u$ commutes with $\varrho_1(g) \otimes \varrho_1(g)$ — indeed $\tau \circ (\varrho_1(g) \otimes \varrho_1(g))(u \otimes v) = \tau(\varrho_1(g)u \otimes \varrho_1(g)v) = \varrho_1(g)v \otimes \varrho_1(g)u = (\varrho_1(g) \otimes \varrho_1(g)) \circ \tau(u \otimes v)$ — so the $\pm 1$ eigenspaces of $\tau$, namely the symmetric ($+1$) and antisymmetric ($-1$) tensors, are each invariant subspaces. The antisymmetric part is the line $\Lambda^2 \mathbb{C}^2 = \mathbb{C}\omega$ with $\omega = e_1 \otimes e_2 - e_2 \otimes e_1$. On this line $\varrho_1 \otimes \varrho_1$ acts as $\Lambda^2 \varrho_1$, and a linear operator $T$ on a two-dimensional space acts on its top exterior power $\Lambda^2$ by multiplication by $\det T$; hence
> $$(\varrho_1 \otimes \varrho_1)(g)\big|_{\Lambda^2 \mathbb{C}^2} = \det \varrho_1(g) = \det g = 1 \qquad \text{(by the definition of } SU(2)\text{, whose elements have determinant } 1\text{)}.$$
> Therefore $\mathbb{C}\omega$ is a one-dimensional invariant subspace on which every group element acts as the identity: it is a copy of the trivial representation $\varrho_0$. (The multiplicativity $\det(\varrho_1(g)) = \det g$ and the fact that $T$ acts on $\Lambda^2$ by $\det T$ are the content of [[Thm - Determinant is Multiplicative|the determinant's characterisation as the induced action on the top exterior power]].)
>
> **The concrete verification.** Every element of $SU(2)$ has the form $g = \begin{pmatrix} a & -\bar b \\ b & \bar a \end{pmatrix}$ with $a, b \in \mathbb{C}$ and $|a|^2 + |b|^2 = 1$. Then $\varrho_1(g)e_1 = a e_1 + b e_2$ and $\varrho_1(g)e_2 = -\bar b\, e_1 + \bar a\, e_2$. Acting on $\omega$,
> $$(\varrho_1 \otimes \varrho_1)(g)\,\omega = (\varrho_1(g)e_1) \otimes (\varrho_1(g)e_2) - (\varrho_1(g)e_2) \otimes (\varrho_1(g)e_1) \qquad \text{(definition of the tensor-product action on } \omega\text{)}.$$
> Expand the first term:
> $$(a e_1 + b e_2) \otimes (-\bar b\, e_1 + \bar a\, e_2) = -a\bar b\, e_1{\otimes}e_1 + a\bar a\, e_1{\otimes}e_2 - b\bar b\, e_2{\otimes}e_1 + b\bar a\, e_2{\otimes}e_2,$$
> and the second term:
> $$(-\bar b\, e_1 + \bar a\, e_2) \otimes (a e_1 + b e_2) = -\bar b a\, e_1{\otimes}e_1 - \bar b b\, e_1{\otimes}e_2 + \bar a a\, e_2{\otimes}e_1 + \bar a b\, e_2{\otimes}e_2.$$
> Subtracting the second from the first and collecting the four basis coefficients:
> $$e_1{\otimes}e_1:\quad -a\bar b - (-\bar b a) = -a\bar b + a\bar b = 0,$$
> $$e_1{\otimes}e_2:\quad a\bar a - (-\bar b b) = |a|^2 + |b|^2 = 1 \qquad \text{(by } |a|^2 + |b|^2 = 1\text{)},$$
> $$e_2{\otimes}e_1:\quad -b\bar b - \bar a a = -(|b|^2 + |a|^2) = -1 \qquad \text{(by } |a|^2 + |b|^2 = 1\text{)},$$
> $$e_2{\otimes}e_2:\quad b\bar a - \bar a b = 0.$$
> Hence $(\varrho_1 \otimes \varrho_1)(g)\,\omega = e_1 \otimes e_2 - e_2 \otimes e_1 = \omega$ for every $g \in SU(2)$, confirming that $\omega$ is invariant. The two unimodularity uses ($|a|^2 + |b|^2 = 1$) are exactly where the determinant-one constraint enters; for a general $g \in GL(2; \mathbb{C})$ the vector $\omega$ would instead be scaled by $\det g$.

**Step 5: The symmetric complement is $\varrho_2$, completing the decomposition.**

The symmetric part $\odot^2 \mathbb{C}^2$ is, by definition, the representation $\varrho_2 = \odot^2 \varrho_1$, and it is the invariant complement of $\mathbb{C}\omega$.

> [!note]- Derivation
> By Step 4 the transposition operator $\tau$ splits $\mathbb{C}^2 \otimes \mathbb{C}^2 = \odot^2 \mathbb{C}^2 \oplus \Lambda^2 \mathbb{C}^2$ into invariant subspaces, with $\Lambda^2 \mathbb{C}^2 = \mathbb{C}\omega \cong \varrho_0$. The symmetric summand $\odot^2 \mathbb{C}^2$ has basis
> $$e_1 \odot e_1 = e_1 \otimes e_1,\quad e_1 \odot e_2 = \tfrac12(e_1 \otimes e_2 + e_2 \otimes e_1),\quad e_2 \odot e_2 = e_2 \otimes e_2,$$
> and carries the restriction of $\varrho_1 \otimes \varrho_1$, which is by the very definition of the symmetric power the representation $\odot^2 \varrho_1 = \varrho_2$: for $g \in SU(2)$, $\varrho_2(g)(u \odot v) = \varrho_1(g)u \odot \varrho_1(g)v$, and this is precisely $(\varrho_1(g) \otimes \varrho_1(g))$ restricted to symmetric tensors. Thus
> $$\varrho_1 \otimes \varrho_1 = \big(\varrho_1 \otimes \varrho_1\big)\big|_{\odot^2 \mathbb{C}^2} \oplus \big(\varrho_1 \otimes \varrho_1\big)\big|_{\Lambda^2 \mathbb{C}^2} = \varrho_2 \oplus \varrho_0,$$
> an equality of representations (not merely of isomorphism classes) once we present $\mathbb{C}^2 \otimes \mathbb{C}^2$ in the symmetric–antisymmetric basis. This matches the abstract count of Step 3 and gives the explicit realisation of each summand: $\varrho_2$ on the three symmetric tensors, $\varrho_0$ on the antisymmetric line $\mathbb{C}\omega$.

> [!note]- Complete formal solution
> **Claim.** $\varrho_1 \otimes \varrho_1 \cong \varrho_2 \oplus \varrho_0$ as complex representations of $SU(2)$, where $\varrho_1$ is the standard representation on $\mathbb{C}^2$, $\varrho_2 = \odot^2 \varrho_1$, and $\varrho_0$ is trivial.
>
> Write $\lambda_1 = \varrho_{1*}$ and $\lambda_\otimes = (\varrho_1 \otimes \varrho_1)_*$ for the differentials, extended complex-linearly to $\mathfrak{sl}(2; \mathbb{C})$, and let $H = \operatorname{diag}(1, -1)$.
>
> Differentiating $(\varrho_1 \otimes \varrho_1)(\exp tX) = \varrho_1(\exp tX) \otimes \varrho_1(\exp tX)$ at $t = 0$ and applying the product rule for the bilinear map $\otimes$ gives the Leibniz identity $\lambda_\otimes(X) = \lambda_1(X) \otimes I + I \otimes \lambda_1(X)$ for $X \in \mathfrak{su}(2)$, hence, by complex linearity, for $X = H$. Since $\lambda_1(H) = H$ with $He_1 = e_1$, $He_2 = -e_2$, the basis $\{e_i \otimes e_j\}$ diagonalises $\lambda_\otimes(H)$ with eigenvalues $2, 0, 0, -2$; the weight multiset is $\{2, 0, 0, -2\}$.
>
> By Part (B) of the classification theorem, $\varrho_1 \otimes \varrho_1 \cong \bigoplus_i \varrho_{k_i}$ for nonnegative integers $k_i$, and the weight multiset of the sum is the disjoint union of the ladders $\{k_i, k_i - 2, \dots, -k_i\}$. The maximum weight $2$ forces a summand $\varrho_2$ (ladder $\{2, 0, -2\}$); removing this ladder from $\{2, 0, 0, -2\}$ leaves $\{0\}$, forcing a summand $\varrho_0$ (ladder $\{0\}$); the multiset is then exhausted. Hence $\{k_i\} = \{2, 0\}$ uniquely, so $\varrho_1 \otimes \varrho_1 \cong \varrho_2 \oplus \varrho_0$. (Dimension check: $4 = 3 + 1$.)
>
> Concretely, the transposition $\tau(u \otimes v) = v \otimes u$ commutes with the diagonal action, so $\mathbb{C}^2 \otimes \mathbb{C}^2 = \odot^2 \mathbb{C}^2 \oplus \Lambda^2 \mathbb{C}^2$ is a decomposition into subrepresentations. On $\odot^2 \mathbb{C}^2$ the representation is $\odot^2 \varrho_1 = \varrho_2$ by definition. On $\Lambda^2 \mathbb{C}^2 = \mathbb{C}\omega$, $\omega = e_1 \otimes e_2 - e_2 \otimes e_1$, the action is by $\det \varrho_1(g) = \det g = 1$, so this line is a copy of $\varrho_0$; the direct computation with $g = \begin{pmatrix} a & -\bar b \\ b & \bar a \end{pmatrix}$, $|a|^2 + |b|^2 = 1$, gives $(\varrho_1 \otimes \varrho_1)(g)\omega = \omega$. Therefore $\varrho_1 \otimes \varrho_1 = \varrho_2 \oplus \varrho_0$, with $\varrho_2$ on the symmetric tensors and $\varrho_0$ on $\mathbb{C}\omega$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "$\varrho_1 \otimes \varrho_1 \cong \varrho_2$ because $\odot^2 \varrho_1 = \varrho_2$ has the right top weight"
> One is tempted to argue: the highest weight of $\varrho_1 \otimes \varrho_1$ is $2$, and the irreducible with highest weight $2$ is $\varrho_2 = \odot^2 \varrho_1$, so $\varrho_1 \otimes \varrho_1 \cong \varrho_2$. This is false — it drops the trivial summand entirely. The highest weight identifies *one* irreducible summand (the one heading the top ladder), never the whole representation, unless the representation happens to be irreducible. The tell is the dimension: $\dim(\varrho_1 \otimes \varrho_1) = 4 \neq 3 = \dim \varrho_2$, and the doubled weight $0$ in the multiset $\{2, 0, 0, -2\}$ signals that a second summand ($\varrho_0$) is present. The shortcut becomes legal only when the weight multiset is *exactly* a single ladder $\{k, k-2, \dots, -k\}$ with no repeats, which certifies irreducibility; here the repeat at $0$ forbids it.

> [!note]- Independent sanity check by characters on the maximal torus
> Restrict to the diagonal torus $T = \{\operatorname{diag}(z, z^{-1}) : |z| = 1\} \subset SU(2)$ and compare characters (traces of the representing matrices). On $\operatorname{diag}(z, z^{-1})$ the standard representation has trace $\chi_{\varrho_1} = z + z^{-1}$. Traces multiply under tensor product and add under direct sum, so
> $$\chi_{\varrho_1 \otimes \varrho_1} = (z + z^{-1})^2 = z^2 + 2 + z^{-2}.$$
> The symmetric square $\varrho_2$ has eigenvalues $z^2, z\cdot z^{-1}, z^{-2}$ on $\odot^2 \mathbb{C}^2$, so $\chi_{\varrho_2} = z^2 + 1 + z^{-2}$, and $\chi_{\varrho_0} = 1$. Then
> $$\chi_{\varrho_2} + \chi_{\varrho_0} = (z^2 + 1 + z^{-2}) + 1 = z^2 + 2 + z^{-2} = \chi_{\varrho_1 \otimes \varrho_1}.$$
> The characters agree, corroborating $\varrho_1 \otimes \varrho_1 \cong \varrho_2 \oplus \varrho_0$ (for a compact group, equality of characters is equivalent to equivalence of representations, so this check is in fact a second complete proof).

---

# Key Takeaways

**To decompose a representation of a group with classified representation theory, compute a single discrete invariant and let the classification do the arithmetic.** The whole solution turns on refusing to look at the four-parameter family of $4 \times 4$ matrices $\varrho_1(g) \otimes \varrho_1(g)$ and instead computing the spectrum of one operator, $\lambda_\otimes(H)$, on a basis of four tensors. This is the recurring pattern for compact groups: their finite-dimensional complex representations are semisimple, and semisimple objects are determined up to isomorphism by numerical invariants (weights, characters, dimensions), so a decomposition problem collapses into a bookkeeping problem. The trigger for the pattern is "I have a representation built by a functor ($\otimes$, $\odot^k$, $\Lambda^k$, restriction, induction) from irreducibles I already understand, and I want its irreducible content." The move is always the same — push the functor down to the invariant, decompose the invariant, and read the summands back off. Weights are the invariant of choice when the group has a maximal torus, because they behave additively under $\otimes$ and $\oplus$; characters are the alternative and are often faster, as the sanity check above shows.

**Weights add under tensor product, and the highest weight names only one summand.** The Leibniz rule $\lambda_\otimes(H) = \lambda_1(H) \otimes I + I \otimes \lambda_1(H)$ is the engine that makes weight bookkeeping possible: it says the weight of $u \otimes v$ is the sum of the weights of $u$ and $v$, so the weight multiset of a tensor product is the sumset (with multiplicity) of the factor multisets. Internalising this turns Clebsch–Gordan into elementary combinatorics of ladders. Equally important is the discipline of the "peel off the highest weight" algorithm and its failure mode: the maximum weight present certifies the presence of the irreducible heading that ladder, but *never* the whole representation. The doubled zero in $\{2, 0, 0, -2\}$ is the fingerprint of the second summand, and the illegal shortcut above — collapsing the tensor square to $\varrho_2$ — is exactly the error of forgetting that the leftover weights after peeling the top ladder must themselves be accounted for. When you see a repeated weight, expect a lower-dimensional summand; when the multiset is a single gap-two ladder with no repeats, the representation is irreducible.

**The antisymmetric line is the singlet precisely because $SU(2)$ has determinant one, and this is a portable recognition principle.** The concrete half of the proof identifies the trivial summand not by solving for invariant vectors but by recognising that $\Lambda^2 \varrho_1 = \det \varrho_1 = \det$, and that the defining constraint $\det g = 1$ makes this the trivial representation. The general principle: the top exterior power $\Lambda^n V$ of the standard representation of a matrix group $G \subseteq GL(n)$ is the one-dimensional determinant representation, so it is trivial exactly when $G \subseteq SL(n)$. This is why $SU(2)$ and $SU(n)$ carry a natural invariant antisymmetric tensor (the singlet coupling of two fundamentals, the $\epsilon$-tensor of physics), why the tensor square of the fundamental of $SU(2)$ always sheds a trivial factor, and why the same computation fails for $U(2)$ or $GL(2)$, where the antisymmetric line transforms by the nontrivial character $\det$. The transferable diagnostic is: whenever a tensor construction on a special-linear or special-unitary group produces an alternating slot, look there first for the invariant subspace, because unimodularity has pre-installed one. This exercise is the $k = l = 1$ base case of the Clebsch–Gordan series $\varrho_k \otimes \varrho_l \cong \bigoplus_{m} \varrho_{k+l-2m}$, developed further in [[Ex - Tensor Products and Duals of the Representations of U(1)]] on the abelian side and in [[Ex - rho_2 of SU(2) is the Complexified Adjoint Representation]], where the summand $\varrho_2$ met here is identified with the adjoint representation carrying the curvature of an $SU(2)$-connection.
