---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are finite-dimensional [[Def - Inner Product Space|inner product spaces]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$ with norms $\|v\|_V = \sqrt{\langle v, v \rangle_V}$ and $\|w\|_W = \sqrt{\langle w, w \rangle_W}$. A linear map $S \in \mathcal{L}(V, W)$ has an [[Def - Adjoint of a Linear Map|adjoint]] $S^* \in \mathcal{L}(W, V)$. The identity operator on $V$ is $I_V$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

The distinction between "isometry" and "[[Def - Unitary Operator|unitary]]" is the distinction between "norm-preserving linear map" and "norm-preserving linear *operator*" (i.e., $V = W$ with the same inner product). On a finite-dimensional inner product space, an isometry $V \to V$ is automatically surjective, hence unitary. The distinction matters when $\dim W > \dim V$, where one can have non-surjective isometries.

---

# Axiom Motivation

An isometry is the linear analogue of a **rigid motion**: a map that preserves all the geometric structure encoded in the inner product. The motivating example is the rotation of $\mathbb{R}^3$ by some angle about some axis — it preserves distances, angles, and the volume element. The abstract definition strips this to its essence: an isometry is exactly a linear map that preserves the norm, and equivalently — over an inner product space — that preserves the inner product itself.

The equivalence of "preserves norm" and "preserves inner product" deserves a moment. If $S$ preserves the inner product, $\langle Sv, Sw \rangle = \langle v, w \rangle$, then setting $w = v$ gives $\|Sv\|^2 = \|v\|^2$, so $S$ preserves the norm. The converse, that a norm-preserving linear map preserves the inner product, is a consequence of the **polarisation identity** — the inner product is determined by the norm, via $\langle v, w \rangle = \tfrac{1}{4}(\|v + w\|^2 - \|v - w\|^2)$ over $\mathbb{R}$ (or its complex version). So an isometry's preservation of the norm forces preservation of the inner product, and the *full geometric structure* of the inner product space is preserved by an isometry, not merely the norm. This is why "isometry" — meaning "isos + metric", "same measure" — is the right term.

A third equivalent characterisation is the algebraic identity $S^* S = I_V$. The derivation is direct: $S^* S = I_V$ iff $\langle S^* S v, v \rangle = \langle v, v \rangle$ for all $v$ (using polarisation again) iff $\langle Sv, Sv \rangle = \langle v, v \rangle$ for all $v$, iff $S$ preserves the norm. The relation $S^* S = I_V$ is the cleanest algebraic statement and the one used in most proofs; the relation $\|Sv\| = \|v\|$ is the one used to verify isometry from a concrete description; the relation $\langle Sv, Sw \rangle = \langle v, w \rangle$ is the one used when the geometric meaning is wanted.

Why is the isometry a useful class of maps? Three reasons. First, the **composition of isometries is an isometry**, so the set of isometries on a fixed space $V$ forms a monoid (and, in finite [[Def - Dimension|dimensions]], a [[Def - Group|group]] — the orthogonal or unitary [[Def - Group|group]]). Second, isometries are exactly the **injective** norm-preserving linear maps — norm preservation forces injectivity, because $Sv = 0$ implies $\|v\| = 0$ implies $v = 0$. Third, an isometry can be inverted on its image (it is a linear isomorphism onto its range), so it provides an isomorphism of $V$ with a [[Def - Subspace|subspace]] of $W$.

What if you tried to drop "linear"? Then "isometry" in the metric-space sense includes translations and reflections about arbitrary points. A theorem of Mazur–Ulam says that a metric-space isometry $V \to W$ between normed real vector spaces is **affine** — that is, a linear map plus a translation. So "linear isometry" excludes translations but is otherwise as general as possible. In this chapter we work with linear maps from the outset, so "isometry" always means "linear isometry".

What if you tried to weaken to "preserves angles"? An angle-preserving linear map between Euclidean spaces is a scaling followed by an orthogonal transformation — a *similarity*. So similarities form a larger class than isometries; isometries are similarities with scaling factor $1$. Preserving the norm exactly (not just up to a positive factor) is what distinguishes isometries from similarities.

What if you tried to strengthen to "preserves the inner product *and* is surjective"? Then over a finite-dimensional space, you have promoted isometry to **unitary** (or **orthogonal** over $\mathbb{R}$). This is the right strengthening when $V = W$. Over infinite [[Def - Dimension|dimensions]] or for $\dim W > \dim V$, surjectivity is a genuinely new condition: the unilateral shift on $\ell^2(\mathbb{N})$ is an isometry that is not surjective and not unitary.

The relation $S^* S = I_V$ has a structural reading: it says **$S^*$ is a left inverse of $S$**. Since $S$ is injective (norm-preserving forces injectivity), $S^*$ is determined by $S$ on the range of $S$ (it is the inverse there); on the orthogonal complement of the range, $S^*$ can be anything. In particular, $S S^* \neq I_W$ in general — the relation $S S^* = I_W$ holds precisely when $S$ is also surjective. So $S^*S = I_V$ alone is the isometry condition; $SS^* = I_W$ added is the unitary/surjective condition.

---

# The Definition

A linear map $S \in \mathcal{L}(V, W)$ is an **isometry** if it preserves norms:

$$\|S v\|_W = \|v\|_V \quad \text{for all } v \in V.$$

**Equivalent characterisations** (each implies all others, in finite dimensions):
1. $\|Sv\| = \|v\|$ for all $v$. (Definition.)
2. $\langle Sv, Sw \rangle = \langle v, w \rangle$ for all $v, w$. (Inner product preservation.)
3. $S^* S = I_V$. (Algebraic identity.)
4. $S$ sends some orthonormal basis of $V$ to an orthonormal list in $W$.
5. $S$ sends every orthonormal basis of $V$ to an orthonormal list in $W$.
6. In orthonormal bases of $V$ and $W$, the matrix of $S$ has orthonormal columns.

The full theorem stating these equivalent is [[Thm - Characterization of Isometries]].

An isometry is automatically **injective**: $Sv = 0$ implies $\|v\| = \|Sv\| = 0$ implies $v = 0$. In finite dimensions, an isometry $V \to V$ is therefore surjective by dimension, hence an isomorphism (a [[Def - Unitary Operator|unitary operator]]). An isometry $V \to W$ with $\dim W > \dim V$ can be non-surjective.

---

# Categorical / Structural Definition

In the category of **finite-dimensional Hilbert spaces with bounded linear maps as morphisms**, the isometries are exactly the morphisms $S : V \to W$ satisfying $S^* S = I_V$, where $*$ is the dagger structure. The compositional and identity properties of isometries — composition of isometries is an isometry, identity is an isometry — make them a *wide* subcategory: same objects, but only the isometries as morphisms. The isometries of $V$ to itself form the **unitary group** $U(V)$ (over $\mathbb{C}$) or **orthogonal group** $O(V)$ (over $\mathbb{R}$), which are central objects in [[Def - Group|group theory]] and Lie theory.

Isometries are also the **monomorphisms in the category of inner product spaces with isometric maps** — they are the "injections that respect inner product structure". Their cokernels are isometric to the orthogonal complement of the image, in the canonical sense.

In **operator algebra theory**, the partial isometries of a $C^*$-algebra are operators $u$ with $u u^* u = u$; isometries are the special case $u^* u = I$. The polar decomposition expresses every operator as a positive operator times a partial isometry, and the partial isometric factor encodes "phase" while the positive factor encodes "magnitude".

---

# Relate to Other Fields / Compression

In **Euclidean geometry**, the isometries of $\mathbb{R}^n$ (with translations allowed) form the **Euclidean group** $E(n) = O(n) \ltimes \mathbb{R}^n$ — orthogonal transformations of $\mathbb{R}^n$ semidirect with translations. This is the symmetry group of Euclidean geometry, and the **Erlangen program** of Felix Klein characterised classical geometries by their isometry groups. The pure linear isometries are $O(n)$ (with the origin fixed).

In **special relativity**, the analogue of the orthogonal group for the indefinite Minkowski inner product is the **[[Def - The Lorentz Group|Lorentz group]]** $O(1, 3)$. It is the group of linear isometries of [[Def - Minkowski Space and the Metric|Minkowski space]] — the linear maps preserving the form $\eta(v, w) = -v^0 w^0 + v \cdot w$. The same algebraic theory applies, with the indefinite signature in place of positive definite.

In **operator theory and functional analysis**, the isometric embeddings of one Hilbert space into another are studied as **(non-surjective) isometries**. The unilateral shift on $\ell^2(\mathbb{N})$ is the prototype: $S(x_1, x_2, x_3, \ldots) = (0, x_1, x_2, \ldots)$. It is an isometry ($\|Sx\| = \|x\|$ trivially) but is not surjective (the constant vector $(1, 0, 0, \ldots)$ is not in its range). Its adjoint is the backward shift, which is not an isometry. The pair $(S, S^*)$ models the creation and annihilation operators of quantum field theory.

In **information theory**, an isometric encoder preserves "distinguishability" — distances in code space match distances in message space — and is the right notion for error-detection without amplification.

**True name:** The true name of an isometry is **"inner product preserving"**. The norm-preservation form $\|Sv\| = \|v\|$ is what one verifies, but the inner product preservation $\langle Sv, Sw \rangle = \langle v, w \rangle$ is what one *uses* — it lets you transfer any inner-product calculation in $V$ to the image in $W$. The algebraic form $S^* S = I_V$ is the cleanest for symbolic manipulation; it is the "true name" at the algebra level.

---

# Examples / Corollaries

The identity operator $I_V \in \mathcal{L}(V)$ is the trivial isometry.

A rotation of $\mathbb{R}^2$: $R_\theta = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$. Check: $R_\theta^t R_\theta = I$. Preserves the standard inner product, and so the norm; the eigenvalues are $e^{\pm i \theta}$, on the unit circle.

A reflection across a line through the origin in $\mathbb{R}^2$ — for instance reflection across the $x$-axis, $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$. Check: equals its own transpose, and squared is $I$, so $S^* S = I$. Preserves distances; eigenvalues are $\pm 1$.

A canonical (non-surjective) example in finite dimensions: the inclusion $\mathbb{F}^n \hookrightarrow \mathbb{F}^{n+1}$ via $(v_1, \ldots, v_n) \mapsto (v_1, \ldots, v_n, 0)$. This is an isometry from $\mathbb{F}^n$ to $\mathbb{F}^{n+1}$, but not a unitary operator (the codomain is bigger). Its matrix is $\begin{pmatrix} I_n \\ 0 \end{pmatrix}$, with $S^* S = I_n$ (the relation defining isometry) but $S S^*$ being the projection onto the first $n$ coordinates of $\mathbb{F}^{n+1}$ (not the identity on $\mathbb{F}^{n+1}$).

A geometric example: the **Cayley transform**. For a skew-adjoint operator $K$ (so $K^* = -K$), the operator $S = (I + K)(I - K)^{-1}$ is unitary (in particular, isometric). Conversely, every unitary operator without $-1$ as eigenvalue arises this way. The Cayley transform is the operator analogue of the Möbius map $z \mapsto \frac{1 + z}{1 - z}$ that sends $i\mathbb{R}$ to the unit circle.

A non-example: the projection $P : \mathbb{R}^2 \to \mathbb{R}^2$, $P(x, y) = (x, 0)$. It is not norm-preserving: $\|P(0, 1)\| = 0 \neq 1 = \|(0, 1)\|$. Projections preserve the norm on their range but kill the orthogonal complement.

Another non-example: the doubling map $D : \mathbb{R}^2 \to \mathbb{R}^2$, $D(v) = 2v$. It scales distances by $2$, so is a similarity but not an isometry.

A subtle non-example: the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ over $\mathbb{R}$. It is invertible (determinant $1$) but not norm-preserving: $\|(0, 1)^t\| = 1$, but the image is $(1, 1)^t$ with norm $\sqrt{2}$. Determinant $\pm 1$ does not imply isometry — the orthogonal group is the subset of $\operatorname{SL}_n$ satisfying $S^t S = I$, which is strictly smaller for $n \geq 2$.

A corollary: every isometry $S \in \mathcal{L}(V, W)$ has $\|S\|_{\text{op}} = 1$ (assuming $V \neq 0$), since $\|Sv\| = \|v\|$ gives $\|S\|_{\text{op}} = \sup_{\|v\| = 1} \|Sv\| = 1$.

Another corollary: an isometry between finite-dimensional inner product spaces of the same dimension is surjective (by rank-nullity, or by the dimension count $\dim \operatorname{range} S = \dim V$), so is a unitary operator. Isometries to a *higher-dimensional* space are non-surjective.

A third corollary: if $S \in \mathcal{L}(V, W)$ is an isometry, the orthogonal complement of its range $\operatorname{range}(S)^{\perp}$ has dimension $\dim W - \dim V$, and is exactly the kernel of $S^*$ (using $\operatorname{null} S^* = (\operatorname{range} S)^{\perp}$). So $S^*$ tells you "how much of $W$ is invisible to $S$".

**Calibration check.** Verify:
1. The matrix $\frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ is an isometry (in fact unitary/orthogonal). (Compute $S^t S$.)
2. The composition of two isometries is an isometry. ($\|S T v\| = \|Tv\| = \|v\|$ by sequential application.)
3. If $S \in \mathcal{L}(V, W)$ is an isometry and $V \neq 0$, then $S^* S = I_V$ but $S S^* \neq I_W$ in general (it equals the orthogonal projection onto the range of $S$).

If these check out, the definition is in your hands.

---

# Unlocked by This

> [!tip] Partial Isometry and the Polar Decomposition *(from Functional Analysis)*
> An operator $u \in \mathcal{L}(V)$ is a **partial isometry** if $u^* u$ is a projection, equivalently $u u^* u = u$. Every operator $T \in \mathcal{L}(V)$ factors as $T = S |T|$ where $S$ is a partial isometry whose initial space (the image of $S^* S$) is $(\operatorname{null} T)^{\perp}$ and whose final space (the image of $S S^*$) is $\overline{\operatorname{range} T}$ — this is the **polar decomposition**, the operator-theoretic analogue of $z = e^{i\theta} |z|$. The partial isometric factor encodes the phase, the positive factor encodes the magnitude. When $T$ is invertible, the partial isometry is actually a full unitary; the partial isometry concept is the right generalisation when invertibility fails.

> [!tip] The Stinespring Dilation and Completely Positive Maps *(from Operator Algebras)*
> A **completely positive map** $\Phi : A \to B$ between $C^*$-algebras has a Stinespring dilation: there exists a Hilbert space $K$, an isometry $V : H \to K$, and a $*$-homomorphism $\pi : A \to \mathcal{L}(K)$ such that $\Phi(a) = V^* \pi(a) V$. This is the operator-algebraic analogue of "every positive operator factors as $S^* S$" — every completely positive map factors as a $*$-homomorphism sandwiched between an isometry and its adjoint. In quantum information theory, this is the **Kraus representation** of a quantum channel, and the isometry $V$ is the dilation of the noisy channel to a noise-free isometric embedding into a larger system.

> [!tip] Conformal Maps and Riemann Surfaces *(from Complex Analysis)*
> A **conformal map** between Riemann surfaces is a map whose differential is an isometry up to scale — that is, an angle-preserving map. The Riemann mapping theorem says every simply connected proper open subset of $\mathbb{C}$ is conformally equivalent to the unit disk. The infinitesimal isometry condition lifts to a global isometry only on simply connected Riemannian manifolds of constant curvature, by a theorem of Liouville: the only conformal maps of $\mathbb{R}^n$ to itself for $n \geq 3$ are compositions of translations, rotations, scalings, and inversions. The fact that conformal maps in dimension $\geq 3$ are so rigid — while in dimension $2$ they are profusely available — is one of the most striking phenomena in geometry.
