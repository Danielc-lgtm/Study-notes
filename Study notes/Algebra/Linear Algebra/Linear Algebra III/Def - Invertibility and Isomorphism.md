---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $T \in \mathcal{L}(V, W)$ is a linear map between $\mathbf{F}$-vector spaces. The inverse, when it exists, is $T^{-1} \in \mathcal{L}(W, V)$. The identity operator on $V$ is $I_V$, or just $I$ when context is clear. Two vector spaces being isomorphic is written $V \cong W$. The group of invertible operators on $V$ is $\operatorname{GL}(V)$. For matrices, $A^{-1}$ is the inverse and $\operatorname{GL}_n(\mathbf{F}) = \{A \in \mathbf{F}^{n, n} : A \text{ invertible}\}$.

This is a compound page: it defines four interlocking notions — **invertible linear map**, **inverse**, **isomorphism**, and **isomorphic vector spaces** — because they share a single underlying construction and one is not fully usable without the others.

**Standing convention.** When we say "$V$ and $W$ are isomorphic" without further qualification, we mean isomorphic as vector spaces — there is an invertible linear map between them. Vector spaces over different fields are not "isomorphic" in this sense; they require extra qualifiers (e.g., "real-isomorphic" when viewing $\mathbb{C}$-spaces over $\mathbb{R}$).

---

# Axiom Motivation

The motivation for "invertible" in linear algebra is the same as in [[Def - Group|group]] theory: a transformation should be **reversible**. If $T : V \to W$ converts elements of $V$ into elements of $W$ — possibly losing some information, possibly missing some outputs — when is this conversion *fully reversible*? When there exists an inverse map $S : W \to V$ that *undoes* $T$ from both sides: $ST = I_V$ and $TS = I_W$. The first equation says "apply $T$, then $S$, and you are back where you started (in $V$)"; the second says "apply $S$, then $T$, and you are back where you started (in $W$)". Together they say $T$ is a perfectly reversible relabelling of elements.

Why two equations and not one? Each one alone is weaker. The equation $ST = I_V$ says $T$ has a **left inverse**, equivalently that $T$ is injective (the proof: if $Tu = Tv$ then $u = STu = STv = v$). The equation $TS = I_W$ says $T$ has a **right inverse**, equivalently that $T$ is surjective (proof: every $w = T(Sw) \in \operatorname{range} T$). One-sided inverses are common in infinite [[Def - Dimension|dimensions]] and capture only half the picture: the forward shift on $\mathbf{F}^\infty$ has a left inverse (the backward shift) but no right inverse — it is injective but not surjective. In finite dimensions with $\dim V = \dim W$, one-sided inverses coincide with two-sided ones ([[Thm - Injectivity Equals Surjectivity in Finite Dimensions]]), but the *definition* must accommodate both cases, so requiring *both* equations is the right thing to do.

Why must $S$ be linear and not merely a function? The remarkable fact (Exercise 1 of LADR §3D, and the proof of LADR 3.63) is that if a linear bijection $T$ has a set-theoretic inverse, that inverse is *automatically* linear. So one could just demand that $T$ be a bijective linear map, and the inverse-as-linear-map would come for free. But stating the definition with explicit linearity of $S$ from the start makes the inverse a first-class citizen of $\mathcal{L}(W, V)$ and avoids the small detour through set-theoretic bijectivity.

The motivation for **isomorphism** is the same construction renamed. An *isomorphism* is an invertible linear map; two vector spaces are *isomorphic* if some isomorphism between them exists. The renaming is to emphasise that, when two spaces are isomorphic, we can think of them as "the same vector space with different labels" — every property that depends only on the vector-space structure transfers via $T$ and back via $T^{-1}$. This is the same as the situation in group theory ([[Def - Isomorphism]] for [[Def - Group|groups]]): isomorphism is "structural equality up to relabelling".

The deep payoff of this view is **dimension is the complete invariant of a finite-dimensional vector space**. Two such spaces over the same field are isomorphic iff their dimensions agree ([[Thm - Two Vector Spaces Isomorphic iff Same Dimension]]). So every $n$-dimensional space over $\mathbf{F}$ is "the same as" $\mathbf{F}^n$ — and abstract calculations can be reduced to concrete calculations in $\mathbf{F}^n$ once a basis (i.e., an isomorphism with $\mathbf{F}^n$) is chosen. This is why we can do *any* computation in linear algebra by passing to coordinates: choosing a basis *is* choosing an isomorphism.

One might ask whether to *strengthen* the definition by demanding $T$ preserve some extra structure — an inner product, a norm, a specific basis. Each strengthening cuts out a finer equivalence relation: [[Def - Isometry|isometries]] preserve inner products ([[Linear Algebra VII — §7 Operators on Inner Product Spaces]]), unitaries preserve sesquilinear forms, and so on. The bare-vector-space-isomorphism notion captures exactly "the same vector space", with no extra structure.

One might *weaken* the definition by demanding only injectivity, or only surjectivity. These are useful concepts (a **monomorphism** is an injective linear map; an **epimorphism** is a surjective one), but neither alone makes $V$ and $W$ "the same" — an injection might have a smaller codomain after restricting to the image, and a surjection might forget structure in its kernel. Invertibility is the cleanest notion of equivalence.

---

# The Definition

Let $V, W$ be vector spaces over a field $\mathbf{F}$, and $T \in \mathcal{L}(V, W)$.

**Invertible linear map.** $T$ is **invertible** if there exists $S \in \mathcal{L}(W, V)$ with

$$ST \;=\; I_V \quad \text{and} \quad TS \;=\; I_W.$$

**Inverse.** Such an $S$ is called an **inverse** of $T$. When $T$ is invertible, the inverse is unique (Proposition 3.60 of LADR; the proof is one line: if $S_1, S_2$ are both inverses, $S_1 = S_1 I = S_1 (T S_2) = (S_1 T) S_2 = I S_2 = S_2$). The unique inverse is denoted $T^{-1}$.

**Isomorphism.** An **isomorphism** is an invertible linear map.

**Isomorphic vector spaces.** Two vector spaces $V$ and $W$ over the same field are **isomorphic**, written $V \cong W$, if there exists an isomorphism $T : V \to W$.

**Characterisation.** $T$ is invertible iff $T$ is both injective and surjective:
$$T \text{ invertible} \;\iff\; \operatorname{null} T = \{0\} \text{ and } \operatorname{range} T = W.$$

**Square matrix.** An $n$-by-$n$ matrix $A \in \mathbf{F}^{n, n}$ is **invertible** if there exists $B \in \mathbf{F}^{n, n}$ with $AB = BA = I_n$. The unique such $B$ is $A^{-1}$. Equivalently, $A$ is invertible iff the linear map $\mathbf{F}^n \to \mathbf{F}^n$, $x \mapsto Ax$, is invertible. Also, the set $\operatorname{GL}_n(\mathbf{F})$ of invertible matrices forms a group under multiplication.

---

# Categorical / Structural Definition

In any category, a morphism $f : X \to Y$ is **invertible** (or an **isomorphism**) iff there exists $g : Y \to X$ with $g \circ f = \mathrm{id}_X$ and $f \circ g = \mathrm{id}_Y$. The inverse, if it exists, is unique by the same one-line argument used above. Two objects are **isomorphic** if there is an isomorphism between them, an equivalence relation under which all categorical structure is preserved.

For $\mathbf{Vect}_\mathbf{F}$, this specialises to invertible linear maps. The collection of [[Def - Isomorphism|isomorphisms]] $V \to V$ from a single object to itself forms a [[Def - Group|group]] under composition — the **automorphism group** of $V$, written $\operatorname{Aut}(V)$ or $\operatorname{GL}(V)$ when $V$ is a vector space. In a basis of $V$, $\operatorname{GL}(V) \cong \operatorname{GL}_n(\mathbf{F})$, the group of invertible matrices.

The category $\mathbf{Vect}_\mathbf{F}^{\mathrm{fin}}$ of finite-dimensional vector spaces is, up to equivalence, very simple: its **skeleton** is the category whose objects are non-negative integers $\{0, 1, 2, \ldots\}$ (representing $\mathbf{F}^0, \mathbf{F}^1, \mathbf{F}^2, \ldots$) and whose hom-sets are $\mathbf{F}^{m, n}$ (matrices). Two finite-dimensional vector spaces are isomorphic iff they have the same dimension; up to isomorphism, there is one $n$-dimensional vector space per non-negative integer $n$.

The **functor category** perspective: every linear map can be encoded as a matrix (after choosing bases), every invertible map as an invertible matrix, and every isomorphism class of vector space as a non-negative integer (its dimension). The category-theoretic statements are mirrored exactly in the world of matrices.

---

# Relate to Other Fields / Compression

**True name (invertible):** "perfectly reversible relabelling" — neither information is lost (injectivity) nor outputs are missed (surjectivity). The operator transports vectors back and forth without distortion.

**True name (isomorphism):** "structural equality up to relabelling" — $V \cong W$ says $V$ and $W$ are the same vector space, dressed in different notation. Every vector-space property of $V$ is a vector-space property of $W$, and vice versa.

This is the same construction as **group isomorphism** ([[Def - Isomorphism]] for groups): structure-preserving bijection. The fact that two finite-dimensional vector spaces over $\mathbf{F}$ are isomorphic iff their dimensions agree is the linear-algebraic shadow of the classification of objects in a category by their *invariants* — and dimension is the *only* invariant of a finite-dimensional vector space.

In **set theory**, the analogue of "isomorphic" is "of the same cardinality". Two sets are isomorphic in the category of sets iff there is a bijection, iff they have the same cardinality. Cardinality is the complete invariant of a set, just as dimension is the complete invariant of a finite-dimensional vector space — both are one-number classifications. The difference: cardinality classifies sets, dimension classifies vector spaces, but both are "the simplest invariant".

In **topology**, the analogue is **homeomorphism**: a continuous bijection whose inverse is continuous. Homeomorphism does *not* have a simple numerical invariant — topological spaces have arbitrarily complex topology — but the same definitional pattern applies. The interesting topological structures are not classified by a single number.

In **representation theory**, two representations $\rho : G \to \operatorname{GL}(V)$ and $\rho' : G \to \operatorname{GL}(V')$ are **isomorphic representations** if there is a linear isomorphism $T : V \to V'$ with $\rho'(g) \circ T = T \circ \rho(g)$ for every $g \in G$ — an "intertwining isomorphism". The classification of representations up to isomorphism is the subject of representation theory.

In **algebraic geometry**, two algebraic varieties are **isomorphic** if there are inverse morphisms (polynomial maps) between them. Vector spaces are the simplest case — affine spaces with no extra structure — and the classification is just by dimension.

---

# Examples / Corollaries

**Example: every finite-dimensional space is isomorphic to $\mathbf{F}^n$.** If $V$ has basis $v_1, \ldots, v_n$, the map $T : \mathbf{F}^n \to V$, $(c_1, \ldots, c_n) \mapsto c_1 v_1 + \cdots + c_n v_n$, is an isomorphism. Existence: it is linear, injective (the $v_k$ are linearly independent), and surjective (they span). The inverse sends $v \in V$ to its coordinate column.

**Example: $\mathcal{P}_n(\mathbb{R}) \cong \mathbb{R}^{n+1}$.** The polynomial space has dimension $n + 1$, so it is isomorphic to $\mathbb{R}^{n+1}$. The isomorphism sends $a_0 + a_1 x + \cdots + a_n x^n$ to $(a_0, a_1, \ldots, a_n)$. So polynomial algebra of bounded degree is just $\mathbb{R}^{n+1}$ in disguise.

**Example: $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$.** With bases fixed, the matrix map $\mathcal{M}$ is an isomorphism between linear maps and matrices, of dimension $mn$ on each side. See [[Ex - The space of linear maps has dimension mn]].

**Example: $\mathbf{F}^{m, n} \cong \mathbf{F}^{mn}$.** A matrix can be "vectorised" by stacking its columns (or rows): the map $\mathbf{F}^{m, n} \to \mathbf{F}^{mn}$ sending a matrix to its column-stacked vector is an isomorphism. So a matrix is, abstractly, just a list of $mn$ scalars in a particular arrangement.

**Example: rotation in $\mathbb{R}^2$.** The map $R_\theta : \mathbb{R}^2 \to \mathbb{R}^2$ rotating by angle $\theta$ is invertible with inverse $R_{-\theta}$. The matrix in the standard basis is $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, with determinant $1$ — always invertible.

**Non-example (no inverse exists): $T : \mathbb{R}^3 \to \mathbb{R}^2$.** Any linear map from a $3$-dimensional space to a $2$-dimensional space has $\operatorname{null} T \neq \{0\}$ by [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]], so $T$ is not injective and not invertible. [[Def - Dimension|Dimensions]] block invertibility before any specific computation: an invertible map between finite-dimensional spaces requires equal dimensions.

**Non-example (one-sided inverse only): forward shift on $\mathbf{F}^\infty$.** The forward shift $S : (x_1, x_2, \ldots) \mapsto (0, x_1, x_2, \ldots)$ has left inverse $T(y_1, y_2, \ldots) = (y_2, y_3, \ldots)$ (the backward shift): $TS(x_1, x_2, \ldots) = T(0, x_1, x_2, \ldots) = (x_1, x_2, \ldots)$. But $ST(y_1, y_2, \ldots) = S(y_2, y_3, \ldots) = (0, y_2, y_3, \ldots) \neq (y_1, y_2, \ldots)$ unless $y_1 = 0$. So $S$ is injective but not surjective; it is not invertible. This is the canonical counterexample to "left inverse implies right inverse" in infinite dimensions.

**Non-example (multiplication by $x^2$).** $T : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$, $(Tp)(x) = x^2 p(x)$, is injective but not surjective — $1 \notin \operatorname{range} T$. Hence not invertible. Same lesson as the forward shift: in infinite dimensions, injectivity is not enough.

**Corollary (uniqueness of inverse).** If $S_1, S_2$ are both inverses of $T$, then $S_1 = S_2$. Proof: $S_1 = S_1 I_W = S_1 (T S_2) = (S_1 T) S_2 = I_V S_2 = S_2$.

**Corollary (composition of [[Def - Isomorphism|isomorphisms]]).** If $T : U \to V$ and $S : V \to W$ are isomorphisms, then $ST : U \to W$ is an isomorphism, with inverse $(ST)^{-1} = T^{-1} S^{-1}$ (the "socks-and-shoes" order reversal). Proof: $(ST)(T^{-1} S^{-1}) = S(T T^{-1}) S^{-1} = S I S^{-1} = SS^{-1} = I$, and similarly $(T^{-1} S^{-1})(ST) = I$.

**Corollary (inverse of inverse).** $(T^{-1})^{-1} = T$. The inverse of $T^{-1}$ is the unique map $S$ with $ST^{-1} = I$ and $T^{-1} S = I$; both are satisfied by $S = T$.

**Corollary (invertibility for square matrices).** A square matrix $A \in \mathbf{F}^{n, n}$ is invertible iff: (i) the columns of $A$ are linearly independent; iff (ii) the columns span $\mathbf{F}^n$; iff (iii) the rows are linearly independent; iff (iv) the rows span; iff (v) $\operatorname{rank} A = n$ (full rank); iff (vi) the only solution to $Ax = 0$ is $x = 0$; iff (vii) the equation $Ax = b$ has a solution for every $b \in \mathbf{F}^n$ (and the solution is unique). All equivalences are one-line applications of [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]].

**Corollary (isomorphism is an equivalence relation).** Isomorphism is reflexive ($V \cong V$ via the identity), symmetric ($V \cong W$ via $T$ implies $W \cong V$ via $T^{-1}$), and transitive ($U \cong V$ and $V \cong W$ implies $U \cong W$ via composition).

**Calibration check.** A reader who has understood the definition should be able to verify, in under a minute each: (1) the identity operator on $V$ is invertible, with inverse itself; (2) the zero operator is not invertible (unless $V = \{0\}$); (3) $\mathbb{R}^2$ and $\mathcal{P}_1(\mathbb{R})$ (polynomials of degree at most $1$) are isomorphic, with one explicit isomorphism sending $(a, b)$ to $a + bx$.

---

# Unlocked by This

> [!tip] General Linear Group *(from Group Theory and Lie Theory)*
> The set of invertible operators on a fixed vector space $V$, under composition, forms a [[Def - Group|group]] $\operatorname{GL}(V)$, the **general linear group** of $V$. In a basis, $\operatorname{GL}(V) \cong \operatorname{GL}_n(\mathbf{F})$. Over $\mathbf{F} = \mathbb{R}$ or $\mathbb{C}$, $\operatorname{GL}_n$ is also a smooth manifold (an open subset of $\mathbf{F}^{n^2}$, the matrices with nonzero determinant), and a **Lie group**. The classical matrix Lie groups — $\operatorname{SL}_n$ (determinant 1), $\operatorname{O}(n)$ (orthogonal), $\operatorname{U}(n)$ (unitary), $\operatorname{Sp}_n$ (symplectic) — are subgroups defined by preservation of extra structure, and together they organise the geometry of homogeneous spaces, representations of finite groups, and the gauge groups of physics.

> [!tip] Group Representation *(from Representation Theory)*
> A **linear representation** of a group $G$ on $V$ is a [[Def - Homomorphism|homomorphism]] $\rho : G \to \operatorname{GL}(V)$ — that is, an action of $G$ on $V$ by invertible linear maps. The entire subject of representation theory is the study of such homomorphisms: their irreducible decomposition, their characters, the regular representation, and the structure of $G$ visible through its representations.

> [!tip] Inverse Function Theorem *(from Multivariate Analysis)*
> The smooth analogue of "invertible linear map" is **local diffeomorphism**. The [[Thm - The Inverse Function Theorem|inverse function theorem]] says: a smooth map $f : M \to N$ between manifolds is locally invertible near a point $x$ iff its [[Def - The Total Derivative and Differentiability|total derivative]] $Df_x$ is an invertible linear map. The invertibility of $Df_x$ (a *linear* condition) lifts to the local invertibility of $f$ (a *smooth* condition). This is the principle of *linearisation*: complicated nonlinear questions become tractable by reducing them to questions about the linear approximation.

> [!tip] Change of Basis as Conjugation *(in §3D)*
> When the linear map is an operator $T : V \to V$ and the basis changes, the matrix of $T$ transforms by **conjugation** by the change-of-basis matrix: $A = C^{-1} B C$, where $C \in \operatorname{GL}_n(\mathbf{F})$. So the equivalence classes of matrices under "same operator, different basis" are the **conjugacy classes** of $\operatorname{GL}_n(\mathbf{F})$ acting on $M_n(\mathbf{F})$ by conjugation — also called the **similarity classes**. The structure of similarity classes is the entire content of operator theory: eigenvalues, Jordan form, the minimal and characteristic polynomials are all similarity invariants. See [[Thm - Change of Basis Formula]].
