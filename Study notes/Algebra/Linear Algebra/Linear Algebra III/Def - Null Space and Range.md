---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $T \in \mathcal{L}(V, W)$ is a [[Def - Linear Map|linear map]] between $\mathbf{F}$-vector spaces. The **null space** is $\operatorname{null} T \subseteq V$ (the set of vectors mapped to zero); the **range** is $\operatorname{range} T \subseteq W$ (the set of actual outputs). Some sources write $\ker T$ for the null space and $\operatorname{im} T$ for the range; the terminology is identical, only the names differ. The full chapter's symbols are catalogued on [[Linear Algebra III — §3A–D Linear Maps]].

This is a compound page: it defines two interlocking notions — **null space** and **range** — because they are introduced together and the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] relates their dimensions in a single equation; neither is fully usable without the other.

---

# Axiom Motivation

Two questions are inevitable the moment a linear map $T : V \to W$ is in sight. **How injective is $T$?** A linear map is injective iff it sends only $0$ to $0$ (because $Tu = Tv$ iff $T(u - v) = 0$ iff $u - v$ is in the would-be "bad" set). So the obstruction to injectivity is the set of vectors $T$ kills: the null space. **How surjective is $T$?** The image of $T$ is the actual set of outputs it produces, and surjectivity is the statement that the image is all of $W$. The obstruction to surjectivity is "the rest of $W$" — what is left over after the image is removed. These two questions force the two definitions onto us.

The choice to single out the *zero vector* in defining the null space — rather than, say, the set of vectors mapped to some other specific output — is forced by the algebraic structure. Linear maps send $0$ to $0$ automatically, so the preimage of $0$ is always non-empty and contains the natural anchor of the linear-algebra game. More importantly, the preimage of $0$ is closed under sums and scalar multiples — it is a subspace of $V$. The preimage of any *other* point $w \in W$ is not a subspace; if $T v_0 = w$, the preimage of $w$ is the **affine subspace** $v_0 + \operatorname{null} T$ (a translate of the null space), which is a subspace if and only if $w = 0$. So $\operatorname{null} T$ is the unique preimage that carries the subspace structure of $V$. The other preimages are its translates, and so the null space, taken alone, determines all of them.

Why "range" and not, say, "the image of a basis of $V$"? The range is defined to be the *full* image of $T$ — every $w \in W$ that equals $Tv$ for some $v \in V$. This is the right notion because it is again a subspace: if $w_1 = Tv_1$ and $w_2 = Tv_2$, then $w_1 + w_2 = T(v_1 + v_2)$ is in the range, and $\lambda w_1 = T(\lambda v_1)$ is in the range. The image of a basis of $V$ *spans* the range but need not equal it (only if the basis maps to a basis of the range); the range itself is the subspace one wants, and its [[Def - Dimension|dimension]] — the **rank** of $T$ — is the structural invariant.

A subtler motivation: the null space and range are *complementary halves of $T$*. Roughly speaking, $T$ collapses the null space to a single point and stretches a complement of the null space onto the range. Make this precise: choose a complement $U$ of $\operatorname{null} T$ in $V$, so $V = \operatorname{null} T \oplus U$ as a direct sum. The restriction $T|_U : U \to \operatorname{range} T$ is then a bijection — injective because if $T u = 0$ then $u \in U \cap \operatorname{null} T = \{0\}$, surjective because every $Tv = T(v_0 + u) = Tu$ for $v_0 \in \operatorname{null} T$, $u \in U$. So $T$ is, in this sense, equal to "the zero map on $\operatorname{null} T$ direct-summed with the isomorphism $T|_U : U \to \operatorname{range} T$". The decomposition $V = \operatorname{null} T \oplus U$ exposes the structure of $T$ completely, and $\dim V = \dim \operatorname{null} T + \dim U = \dim \operatorname{null} T + \dim \operatorname{range} T$ is the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] read off this decomposition. The definitions of null space and range exist to make this picture statable.

If one *strengthened* the null space by demanding it contain not just kernel-of-$T$ but also kernel-of-$T^2$, $T^3$, etc., one would get the **generalised kernel** $\bigcup_k \operatorname{null} T^k$, important for the Jordan-form theory of [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]]. If one *weakened* the range by considering instead $T(S)$ for some subspace $S$, one would get a useful family of [[Def - Subspace|subspaces]] parametrised by $S$, including the range itself ($S = V$). Both directions are productive in later topics, but the cleanest and most fundamental notions are the raw $\operatorname{null} T$ and $\operatorname{range} T$.

---

# The Definition

Let $T \in \mathcal{L}(V, W)$ be a linear map between $\mathbf{F}$-vector spaces.

**Null space.** The **null space** of $T$, denoted $\operatorname{null} T$ (or $\ker T$), is the subset of $V$ consisting of vectors mapped to zero:

$$\operatorname{null} T \;:=\; \{\, v \in V \;:\; Tv = 0 \,\}.$$

**Range.** The **range** of $T$, denoted $\operatorname{range} T$ (or $\operatorname{im} T$), is the subset of $W$ consisting of actual outputs of $T$:

$$\operatorname{range} T \;:=\; \{\, Tv \;:\; v \in V \,\} \;=\; \{\, w \in W \;:\; \exists v \in V \text{ with } Tv = w \,\}.$$

**Both are [[Def - Subspace|subspaces]].** $\operatorname{null} T$ is a subspace of $V$, and $\operatorname{range} T$ is a subspace of $W$. (Each contains the zero vector of the respective space, and each is closed under addition and scalar multiplication; the verifications are one line apiece.)

**Injectivity and surjectivity, in terms of these.** The linear map $T$ is **injective** iff $\operatorname{null} T = \{0\}$; it is **surjective** iff $\operatorname{range} T = W$.

---

# Categorical / Structural Definition

In the category $\mathbf{Vect}_\mathbf{F}$ (objects: vector spaces; morphisms: linear maps), the null space is the **categorical kernel** of $T$: the equaliser of $T$ and the zero morphism $0 : V \to W$, i.e., the universal subobject of $V$ that $T$ sends to zero. The range, dually, is the source of the **image factorisation** of $T$: every morphism $T : V \to W$ in an abelian category factors uniquely as $V \twoheadrightarrow \operatorname{coim} T \xrightarrow{\sim} \operatorname{im} T \hookrightarrow W$, with the middle isomorphism being the "first isomorphism theorem" $V / \operatorname{null} T \cong \operatorname{range} T$ — see [[Thm - Fundamental Theorem of Linear Maps]] for the [[Def - Dimension|dimension]] count.

In categorical terms: $\operatorname{null} T \hookrightarrow V$ is a **mono**, and the cokernel of this mono is the canonical quotient $V \twoheadrightarrow V / \operatorname{null} T$. Composing with $T$ produces the unique injective linear map $\bar T : V / \operatorname{null} T \to W$ whose image is $\operatorname{range} T$, and $\bar T$ identifies $V / \operatorname{null} T$ with $\operatorname{range} T$ as isomorphic subspaces. This factorisation $V \to V/\operatorname{null} T \cong \operatorname{range} T \hookrightarrow W$ is the **canonical factorisation** of any linear map, and every property of $T$ that depends only on its image is a property of the middle isomorphism. The categorical content of rank–nullity is *not* the dimension equation but this image factorisation — the dimension equation is its shadow.

---

# Relate to Other Fields / Compression

**True name (null space):** "the obstruction to injectivity, packaged as a subspace". Whenever one tests whether a linear map is injective, one is testing whether the null space is trivial.

**True name (range):** "the actual reachable codomain", as opposed to the formal codomain $W$. A linear map $T : V \to W$ is honestly a map onto $\operatorname{range} T$; everything outside the range is "filler".

For [[Def - Group|group]] homomorphisms, the null space is exactly the **kernel**, the range is exactly the **image**, and the first isomorphism theorem $G / \ker \varphi \cong \operatorname{im} \varphi$ is the source of [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] in dimensions. For [[Def - Ring|ring]] homomorphisms, the kernel is a (two-sided) ideal and the image is a subring; the first isomorphism theorem reads $R / \ker \varphi \cong \operatorname{im} \varphi$. For [[Def - Module|module]] homomorphisms — of which linear maps are the special case where the ring is a field — the kernel is a submodule and the image is a submodule, with $M / \ker \varphi \cong \operatorname{im} \varphi$ once again. The pattern is universal: every structure-preserving map has a kernel (obstruction to injectivity, on the input side) and an image (the reachable part of the codomain), and the quotient by the kernel is isomorphic to the image.

In analysis, the null space of a differential operator is the *solution space of a homogeneous equation*. For the operator $D : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$, $Dp = p'$, the null space consists of polynomials with derivative zero — the constants. For the Laplacian $\Delta$ on a domain, the null space is the **harmonic functions** on that domain. So "find the null space" is "solve the homogeneous equation", and the range is *the set of right-hand sides for which the equation has a solution*. The Fredholm alternative for compact perturbations of the identity is the infinite-dimensional analogue of rank–nullity.

---

# Examples / Corollaries

**Example: the zero map.** $T = 0 : V \to W$ has $\operatorname{null} T = V$ (everything is killed) and $\operatorname{range} T = \{0\}$ (nothing is reached). This is the maximally non-injective and maximally non-surjective linear map.

**Example: the identity.** $I : V \to V$ has $\operatorname{null} I = \{0\}$ (only $0$ is sent to $0$, by injectivity) and $\operatorname{range} I = V$ (everything is hit). Maximally injective, maximally surjective.

**Example: a linear functional $\varphi : \mathbf{F}^3 \to \mathbf{F}$.** Define $\varphi(z_1, z_2, z_3) = z_1 + 2z_2 + 3z_3$. The null space is the plane $\{z_1 + 2z_2 + 3z_3 = 0\}$, a $2$-dimensional subspace of $\mathbf{F}^3$. The range is all of $\mathbf{F}$ (nonzero functionals are surjective). Rank–nullity: $3 = 2 + 1$. The general fact: every nonzero functional on an $n$-dimensional space has a $(n-1)$-dimensional null space (a **hyperplane**).

**Example: differentiation on polynomials.** $D : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$, $Dp = p'$. The null space is the constants — a one-dimensional subspace. The range is all of $\mathcal{P}(\mathbb{R})$: any polynomial $q$ is the derivative of some polynomial (take an antiderivative, fixing the constant). So $D$ is surjective but not injective. Rank–nullity does not directly apply because $\mathcal{P}(\mathbb{R})$ is infinite-dimensional, but its statement is honoured: $\infty = 1 + \infty$, in the loose sense.

**Example: multiplication by $x^2$.** $T : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$, $(Tp)(x) = x^2 p(x)$. The null space is $\{0\}$: if $x^2 p(x) = 0$ for all $x$, then $p = 0$. So $T$ is injective. The range is the polynomials with no constant or linear term, a proper subspace of $\mathcal{P}(\mathbb{R})$. So $T$ is injective but not surjective — the infinite-dimensional escape from the "injective iff surjective" slogan.

**Example: the backward shift on $\mathbf{F}^\infty$.** $T(x_1, x_2, x_3, \ldots) = (x_2, x_3, \ldots)$. The null space is the sequences with $x_2 = x_3 = \cdots = 0$, i.e., supported on the first coordinate — a one-dimensional subspace. The range is all of $\mathbf{F}^\infty$: every sequence is the shift of some sequence. So $T$ is surjective but not injective. (The forward shift $S(x_1, x_2, \ldots) = (0, x_1, x_2, \ldots)$ is the opposite: injective but not surjective.)

**Example: a projection.** Let $V = U \oplus W$ as a direct sum, and let $P : V \to V$ be the projection onto $U$ along $W$: $P(u + w) = u$. Then $\operatorname{null} P = W$ and $\operatorname{range} P = U$. Notice that the null space and range are *complementary subspaces of $V$* in this case — and the operator satisfies $P^2 = P$ (a **projection** by the algebraic definition).

**Non-example (null space is not a subset of $W$).** It is a common confusion to put the null space "in $W$" because $W$ is where zeros happen. But $\operatorname{null} T \subseteq V$ — the null space is the set of *inputs* mapped to zero, not the set of zero outputs (the latter is just $\{0\}$).

**Non-example (range need not contain $W$'s zero, structurally).** $\operatorname{range} T$ always contains $0_W$, because $T(0_V) = 0_W$, but it is a proper subspace of $W$ whenever $T$ is not surjective. The phrasing "the range of $T$" is sometimes used informally to mean "all $w$ such that $Tv = w$ has a solution", which is exactly the formal definition.

**Corollary (subspace test).** $\operatorname{null} T$ is a subspace of $V$: it contains $0_V$ (because $T(0) = 0$); if $u, v \in \operatorname{null} T$ then $T(u + v) = Tu + Tv = 0$, so $u + v \in \operatorname{null} T$; if $\lambda \in \mathbf{F}$ and $v \in \operatorname{null} T$ then $T(\lambda v) = \lambda Tv = 0$, so $\lambda v \in \operatorname{null} T$. The same three-line check shows $\operatorname{range} T$ is a subspace of $W$.

**Corollary ($T$ injective ⟺ $\operatorname{null} T = \{0\}$).** Suppose $Tu = Tv$. Then $T(u - v) = 0$, so $u - v \in \operatorname{null} T$. Injectivity means $Tu = Tv \Rightarrow u = v$, equivalently $u - v = 0$, equivalently the only element of $\operatorname{null} T$ is $0$. The converse direction is the same equation read backward. This is the *operational* criterion for injectivity: check that nothing is killed except $0$.

**Corollary (fibres are translates).** If $w \in \operatorname{range} T$ and $v_0$ is any element with $Tv_0 = w$, then the **fibre** $T^{-1}(w) = \{v \in V : Tv = w\}$ equals the affine subspace $v_0 + \operatorname{null} T = \{v_0 + n : n \in \operatorname{null} T\}$. Proof: if $Tv = w$ then $T(v - v_0) = 0$, so $v - v_0 \in \operatorname{null} T$; conversely, if $v = v_0 + n$ with $Tn = 0$, then $Tv = Tv_0 = w$. So every non-empty fibre is a translate of $\operatorname{null} T$, of the same dimension. This is the geometric content of "the null space tells you everything about non-injectivity".

**Calibration check.** A reader who has understood the definition should be able to verify, in under a minute each: (1) $\operatorname{null} T$ contains $0_V$ and is closed under sums; (2) $\operatorname{range} T$ contains $0_W$ and is closed under sums; (3) for the linear map $T : \mathbb{R}^2 \to \mathbb{R}$, $T(x, y) = x + y$, the null space is the line $y = -x$ and the range is all of $\mathbb{R}$.

---

# Unlocked by This

> [!tip] Rank of a Matrix *(in §3C)*
> The dimension of the range is the **rank** of $T$ (see [[Def - Rank of a Linear Map]]). After choosing bases, the rank of $T$ equals the rank of its matrix, equivalently the dimension of the column span of $\mathcal{M}(T)$ in $\mathbf{F}^{m, 1}$. The theorem that "column rank equals row rank" is one of the cleaner small surprises of the chapter.

> [!tip] Quotient Space *(from Linear Algebra IV)*
> The **quotient space** $V / \operatorname{null} T$ is the set of cosets $v + \operatorname{null} T$ under the equivalence relation "differ by an element of $\operatorname{null} T$". Equipped with the obvious vector-space structure, it is itself a vector space, and the map $\bar T : V / \operatorname{null} T \to \operatorname{range} T$, $v + \operatorname{null} T \mapsto Tv$, is well-defined and is an isomorphism. This is the **first isomorphism theorem** for vector spaces, and it is the source of [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] by dimension count. See [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

> [!tip] Solution Space of a Linear System
> A homogeneous linear system $Ax = 0$ has solution set $\operatorname{null} A \subseteq \mathbf{F}^n$. An inhomogeneous system $Ax = b$ either has empty solution set (when $b \notin \operatorname{range} A$) or has solution set $x_0 + \operatorname{null} A$ for any particular solution $x_0$. So the entire theory of linear systems is wrapped up in null spaces and ranges. The **rank** of the coefficient matrix counts the number of independent equations; the **nullity** counts the degrees of freedom in the solution.

> [!tip] Generalised Kernel and Jordan Form *(from Linear Algebra VIII)*
> The chain $\operatorname{null} T \subseteq \operatorname{null} T^2 \subseteq \operatorname{null} T^3 \subseteq \cdots$ stabilises after finitely many steps for an operator on a finite-dimensional space, and the limit is the **generalised null space**. For an eigenvalue $\lambda$ of $T$, the generalised null space of $T - \lambda I$ is the **generalised eigenspace** for $\lambda$, the right substitute for the eigenspace when $T$ is not diagonalisable. The Jordan-form theorem decomposes $V$ as a direct sum of generalised eigenspaces. See [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].
