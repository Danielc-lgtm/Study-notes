---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $\mathbf{F}$ denotes a field (always $\mathbb{R}$ or $\mathbb{C}$ unless said otherwise) and $V, W$ are vector spaces over the same field $\mathbf{F}$. A linear map $T : V \to W$ has its function value at $v$ written either $T(v)$ or, more commonly, $Tv$ — when $T$ is linear, the parentheses serve no purpose and are dropped to make composition $STv$ read naturally. The set of all linear maps from $V$ to $W$ is $\mathcal{L}(V, W)$; when $V = W$ we write $\mathcal{L}(V)$ for $\mathcal{L}(V, V)$, and call its elements **operators** on $V$. The full notation registry for the chapter is on [[Linear Algebra III — §3A–D Linear Maps]].

**Standing convention.** "Linear map" always means $\mathbf{F}$-linear between $\mathbf{F}$-vector spaces over the *same* field $\mathbf{F}$. Maps between $\mathbb{R}$-spaces and $\mathbb{C}$-spaces require additional qualifications (real-linear vs. complex-linear, "antilinear", etc.) and are not what "linear map" means in this topic.

---

# Axiom Motivation

The thing we are trying to axiomatize is **a structure-preserving function between vector spaces**. A vector space has two operations — addition $+$ and scalar multiplication by $\mathbf{F}$ — and the notion of a "good" function $T : V \to W$ should be one that respects them: doing the operation in $V$ and then applying $T$ should give the same result as applying $T$ first and then doing the operation in $W$. This is the same templated definition that produces "group homomorphism" from a group structure or "ring homomorphism" from a ring structure: a structure-preserving map between objects of a given type. Vector spaces have two operations, so the demand splits into two axioms.

The first axiom is **additivity**, $T(u + v) = Tu + Tv$ for all $u, v \in V$. This is the statement that $T$ commutes with addition. Drop it and you no longer have a useful notion of function-between-vector-spaces: consider $f : \mathbb{R} \to \mathbb{R}$ with $f(x) = x^2$. We have $f(0) = 0$ correctly, but $f(1 + 1) = 4$ while $f(1) + f(1) = 2$, so $f$ does not commute with addition. Nothing about vector-space addition transfers through $f$, and statements about sums in the domain say nothing about sums in the codomain. If $T$ is not additive, the very phrase "$T$ takes the line $\{u + tv : t \in \mathbb{R}\}$ through $u$ to a line in $W$" has no meaning. Additivity is what makes linear maps **send lines to lines** (or possibly to single points).

The second axiom is **homogeneity**, $T(\lambda v) = \lambda Tv$ for all $\lambda \in \mathbf{F}$, $v \in V$. This is the statement that $T$ commutes with scalar multiplication. Drop it and you can construct surprises: there exist functions $T : \mathbb{R} \to \mathbb{R}$ that are additive but *not* homogeneous (over $\mathbb{R}$ this requires the axiom of choice, but counterexamples exist; over $\mathbb{C}$ as a real vector space, complex conjugation $z \mapsto \bar z$ is real-additive but not complex-homogeneous because $\overline{i \cdot 1} = -i \neq i \cdot \bar 1 = i$). Without homogeneity, $T$ would not respect the action of the field, and statements like "if $w_1, \ldots, w_n$ form a basis of the image, then they uniquely identify each output of $T$" would no longer follow. Homogeneity is what makes linear maps **respect direction and scaling**, not just addition.

One might ask whether to *weaken* the axioms by requiring only additivity, since over $\mathbb{Q}$-vector spaces additivity does imply homogeneity (because every rational is built from $1$ using $+$ and the rationals are the prime field). But the moment $\mathbf{F}$ contains irrationals — already in $\mathbb{R}$ — additivity alone is not enough: there exist additive functions $\mathbb{R} \to \mathbb{R}$ whose graphs are dense in the plane. The two axioms together are equivalent to the cleaner single axiom $T(\lambda u + \mu v) = \lambda Tu + \mu Tv$ for all $\lambda, \mu \in \mathbf{F}$ and $u, v \in V$, which by induction extends to *arbitrary linear combinations*: $T(\sum \lambda_k v_k) = \sum \lambda_k Tv_k$. This is the form of linearity one actually *uses* — it is the form that makes the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] work, because the value of $T$ on a basis determines (and is freely chosen for) the value of $T$ on every linear combination.

One might also ask whether to *strengthen* the axioms by requiring $T$ to be injective, or surjective, or to preserve additional structure (norms, inner products). Each strengthening cuts out a useful sub-class: injective linear maps are **monomorphisms**, surjective ones are **epimorphisms**, those preserving an inner product are **isometries** (see [[Linear Algebra VII — §7 Operators on Inner Product Spaces]]). But none of these is the right starting point: a linear map need not be injective (the zero map is linear but kills everything), need not be surjective (the inclusion $\mathbf{F}^n \hookrightarrow \mathbf{F}^{n+1}$ is linear but misses the last coordinate), and the unstructured definition captures exactly the right class — those that respect $+$ and scalar multiplication, no more, no less.

A final motivation: every "linear" object in mathematics is built from linear maps. The total derivative of a smooth map is the linear map approximating it to first order ([[Def - The Total Derivative and Differentiability]]); a representation of a group is a homomorphism into the group of invertible linear maps; a matrix is the coordinate version of a linear map (see [[Def - Matrix of a Linear Map]]). The definition is *the* foundation of every linearisation in mathematics, and so the demand that it capture exactly "respects the two operations" is non-negotiable.

---

# The Definition

Let $V$ and $W$ be vector spaces over the same field $\mathbf{F}$. A **linear map** from $V$ to $W$ is a function $T : V \to W$ satisfying:

1. **Additivity.** For all $u, v \in V$, $\quad T(u + v) = Tu + Tv$.
2. **Homogeneity.** For all $\lambda \in \mathbf{F}$ and all $v \in V$, $\quad T(\lambda v) = \lambda Tv$.

The set of all linear maps from $V$ to $W$ is denoted $\mathcal{L}(V, W)$; the set $\mathcal{L}(V) := \mathcal{L}(V, V)$ of linear maps from $V$ to itself is the set of **operators** on $V$.

Some authors use **linear transformation** as a synonym; this note uses the shorter "linear map".

The two axioms together are equivalent to the single condition

$$T(\lambda u + \mu v) = \lambda Tu + \mu Tv \quad \text{for all } \lambda, \mu \in \mathbf{F}, \; u, v \in V,$$

which extends by induction to: for any finite list $v_1, \ldots, v_n \in V$ and scalars $\lambda_1, \ldots, \lambda_n \in \mathbf{F}$,

$$T\!\left(\sum_{k=1}^n \lambda_k v_k\right) = \sum_{k=1}^n \lambda_k\, Tv_k.$$

This is the *operational* form of linearity — linear maps preserve **arbitrary linear combinations**.

The set $\mathcal{L}(V, W)$ is itself a vector space over $\mathbf{F}$ under pointwise operations:
$(S + T)(v) := Sv + Tv$ and $(\lambda T)(v) := \lambda Tv$.
Its zero vector is the zero map $0 : V \to W$, $0v = 0$ for every $v$.

---

# Categorical Definition

Linear maps are the **morphisms** in the category $\mathbf{Vect}_\mathbf{F}$, whose objects are $\mathbf{F}$-vector spaces. Composition of linear maps is composition of functions (well-defined as a linear map because the composition of two structure-preserving maps preserves structure), and the identity morphism on $V$ is the identity map $I_V$. Associativity and the identity axioms for a category are automatic from set-theoretic function composition. Two morphisms can be added — $\mathbf{Vect}_\mathbf{F}$ is an **enriched** category, with hom-set $\mathcal{L}(V, W)$ itself a vector space — and composition is **bilinear**: $(S_1 + S_2) T = S_1 T + S_2 T$ and $S(T_1 + T_2) = ST_1 + ST_2$, which is the abstract reason $\mathcal{L}(V)$ is a ring.

The category has **finite products** and **finite coproducts**, and they coincide: for finite-dimensional $V_1, V_2$, the **direct sum** $V_1 \oplus V_2$ is simultaneously the categorical product (with projections $\pi_i : V_1 \oplus V_2 \to V_i$) and the coproduct (with inclusions $\iota_i : V_i \to V_1 \oplus V_2$). A category with coinciding finite products and coproducts that match in this way is called **additive** or said to have **biproducts**, and $\mathbf{Vect}_\mathbf{F}$ is the prototypical additive category. A linear map $V_1 \oplus V_2 \to W$ is uniquely a pair of linear maps $V_1 \to W$ and $V_2 \to W$ (the coproduct universal property), and a linear map $V \to W_1 \oplus W_2$ is uniquely a pair $V \to W_1$ and $V \to W_2$ (the product universal property).

The category $\mathbf{Vect}_\mathbf{F}$ has a zero object (the zero space $\{0\}$, which is both initial and terminal), so there is a canonical zero morphism between any two objects — the composition $V \to \{0\} \to W$. The **kernel** and **cokernel** of a morphism are categorical kernels and cokernels in the sense of "equaliser with the zero morphism" and "coequaliser with the zero morphism"; these are exactly the [[Def - Null Space and Range|null space and the quotient by the range]]. Restricted to finite-dimensional spaces, $\mathbf{Vect}_\mathbf{F}$ is an **abelian** category (kernels and cokernels exist and behave correctly; every monomorphism is the kernel of its cokernel; every epimorphism is the cokernel of its kernel), and abelian-category formalism is the right level of abstraction for homological algebra, derived functors, and sheaf cohomology.

---

# Relate to Other Fields / Compression

A linear map is the same construction as a **group homomorphism**, specialised to the category of vector spaces. Under the addition operation alone, a vector space is just an [[Def - Abelian Group|abelian group]], and the additivity axiom of a linear map is precisely the homomorphism condition for abelian groups. The extra demand of homogeneity says that the homomorphism also respects the scalar action — i.e., it is compatible with the second piece of structure that distinguishes a vector space from a bare abelian group.

A linear map is, more precisely, a **module homomorphism** specialised to vector spaces. A [[Def - Module]] over a ring $R$ generalises a vector space by allowing the scalars to come from a ring rather than a field; a [[Def - Module Homomorphism|module homomorphism]] is an additive, homogeneous map. Take $R = \mathbf{F}$, a field, and the modules become vector spaces, and the module homomorphisms become linear maps. So linear maps are not a fundamentally new species — they are the field-coefficient case of module homomorphisms, which are themselves the abelian-category-respecting case of structured maps. The first isomorphism theorem, the second, the third — all of which go through for vector spaces — are special cases of theorems for modules, which are themselves special cases of theorems for groups.

**True name:** the operational characterization of a linear map — the form one uses in practice, not the one in the formal definition — is "$T(\sum \lambda_k v_k) = \sum \lambda_k Tv_k$ for every linear combination". This is what one reaches for when computing with $T$, what makes the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] work, and what underlies the matrix representation: once you know $Tv_1, \ldots, Tv_n$ on a basis, this formula computes $Tv$ for every $v$ as a linear combination.

---

# Examples / Corollaries

**Is an instance: the zero map $0 : V \to W$, $0v = 0$.** Additivity and homogeneity hold trivially. This is the additive identity of $\mathcal{L}(V, W)$ as a vector space, and the canonical "uninteresting" linear map.

**Is an instance: the identity operator $I : V \to V$, $Iv = v$.** Trivially linear, and the multiplicative identity in $\mathcal{L}(V)$ under composition. The matrix of $I$ in any basis $v_1, \ldots, v_n$ of $V$ is the $n$-by-$n$ identity matrix.

**Is an instance: differentiation $D : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$, $Dp = p'$.** Additivity is $(p + q)' = p' + q'$ and homogeneity is $(\lambda p)' = \lambda p'$ — both are basic facts of calculus. This is the canonical example of a linear map on an infinite-dimensional space, and its null space (constants) and range (everything) illustrate how kernel and image behave outside finite dimensions.

**Is an instance: integration $T : \mathcal{P}(\mathbb{R}) \to \mathbb{R}$, $Tp = \int_0^1 p(x)\, dx$.** Linearity is the additivity of the integral $\int(p + q) = \int p + \int q$ and the homogeneity $\int \lambda p = \lambda \int p$. Note that $W = \mathbb{R}$ here — the field itself is a one-dimensional vector space, so linear maps $V \to \mathbf{F}$ are perfectly meaningful and are called **linear functionals**; they live in the **dual space** $V^* = \mathcal{L}(V, \mathbf{F})$, the subject of [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

**Is an instance: the general linear map $\mathbf{F}^n \to \mathbf{F}^m$ specified by a matrix.** Pick scalars $A_{j, k} \in \mathbf{F}$ for $j = 1, \ldots, m$ and $k = 1, \ldots, n$. Define $T : \mathbf{F}^n \to \mathbf{F}^m$ by

$$T(x_1, \ldots, x_n) = \left( \sum_{k=1}^n A_{1, k} x_k,\; \ldots,\; \sum_{k=1}^n A_{m, k} x_k \right).$$

This is linear (both axioms are straightforward), and every linear map $\mathbf{F}^n \to \mathbf{F}^m$ is of this form (Exercise 3 of LADR §3A). The setup with $A_{j, k}$ already foreshadows the matrix representation in [[Def - Matrix of a Linear Map]].

**Is an instance: the multiplication-by-$x^2$ map.** Define $T : \mathcal{P}(\mathbb{R}) \to \mathcal{P}(\mathbb{R})$ by $(Tp)(x) = x^2 p(x)$. This is linear, injective (the only $p$ with $x^2 p(x) = 0$ for all $x$ is $p = 0$), but not surjective — the constant polynomial $1$ is not in the range. It is the easiest example of an injective non-surjective operator on an infinite-dimensional space.

**Is an instance: the backward shift on $\mathbf{F}^\infty$.** $T(x_1, x_2, x_3, \ldots) = (x_2, x_3, \ldots)$ on the space $\mathbf{F}^\infty$ of all sequences. Linear, surjective, but not injective — its null space is the sequences supported on the first coordinate. The forward shift $S(x_1, x_2, \ldots) = (0, x_1, x_2, \ldots)$ is its left-inverse: $TS = I$ but $ST \neq I$. The pair $S, T$ is the classical illustration that injective/surjective and "has a one-sided inverse" can fail to coincide outside finite dimensions.

**Is NOT an instance: $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x + 1$.** This is "linear" in the high-school sense (its graph is a straight line) but not linear in the linear-algebra sense, because $f(0) = 1 \neq 0$. Every linear map sends $0$ to $0$ (proof: $T(0) = T(0 + 0) = T(0) + T(0)$, subtract $T(0)$). The high-school usage is **affine**, and affine maps are linear maps composed with a translation. This non-example probes additivity.

**Is NOT an instance: $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$.** $f(0) = 0$ correctly, but $f(1 + 1) = 4 \neq 2 = f(1) + f(1)$, so additivity fails. This is the canonical "looks linear but isn't" function; it is what makes nonlinearity a real phenomenon and not a definitional accident. It probes additivity.

**Is NOT an instance: complex conjugation $\bar{} : \mathbb{C} \to \mathbb{C}$, viewed as $\mathbb{C}$-linear.** Conjugation $z \mapsto \bar z$ is additive ($\overline{z + w} = \bar z + \bar w$) and is $\mathbb{R}$-homogeneous ($\overline{\lambda z} = \lambda \bar z$ for $\lambda \in \mathbb{R}$), but it is *not* $\mathbb{C}$-homogeneous: $\overline{i \cdot 1} = \overline{i} = -i$, while $i \cdot \bar 1 = i$. So conjugation is a real-linear but not complex-linear map. This non-example probes homogeneity, and it illustrates why "linear" must specify the field.

**Corollary (linear maps fix zero).** Every linear map $T : V \to W$ satisfies $T(0) = 0$, using either axiom: $T(0) = T(0 + 0) = T(0) + T(0)$, then subtract; or $T(0) = T(0 \cdot v) = 0 \cdot Tv = 0$. So sending $0$ to $0$ is automatic, not a separate axiom.

**Corollary (linear maps respect inverses).** $T(-v) = -Tv$, by homogeneity with $\lambda = -1$.

**Corollary ($\mathcal{L}(V, W)$ is a vector space).** Pointwise addition and scalar multiplication make $\mathcal{L}(V, W)$ a vector space over $\mathbf{F}$ (Exercise 5 of LADR §3A). The zero map is the additive identity; the additive inverse of $T$ is $-T$, $(-T)v = -Tv$. This is what makes "linear maps as objects" a worthwhile concept: the maps themselves form a vector space, and linear-algebra constructions apply to them too.

**Corollary (composition is bilinear).** If $T_1, T_2 \in \mathcal{L}(U, V)$, $S \in \mathcal{L}(V, W)$, and $\lambda \in \mathbf{F}$, then $S(T_1 + T_2) = ST_1 + ST_2$ and $S(\lambda T_1) = \lambda(ST_1)$, and similarly on the other side. This is the algebraic content of "composition of linear maps is itself a linear-algebraic operation", and the reason $\mathcal{L}(V)$ is a [[Def - Ring|ring]] (under $+$ and composition).

**Calibration check.** A reader who has understood the definition should be able to verify the following three small facts in under a minute each: (1) the zero map and the identity map are linear; (2) the function $f(x) = x + 1$ on $\mathbb{R}$ is not linear, and the reason is the additivity axiom (specifically $f(0) \neq 0$); (3) the pointwise sum $S + T$ of two linear maps is again linear.

---

# Unlocked by This

> [!tip] Linear Functional and Dual Space *(from Linear Algebra IV)*
> A **linear functional** on $V$ is a linear map $\varphi : V \to \mathbf{F}$ — that is, an element of $\mathcal{L}(V, \mathbf{F})$. The set of all linear functionals is the **dual space** $V^* := \mathcal{L}(V, \mathbf{F})$, itself a vector space of the same dimension as $V$ (finite-dimensional case). Many natural objects are linear functionals: the integral of a polynomial against a fixed weight, the trace of an operator, the inner product with a fixed vector. The dual space, dual basis, and dual map are the content of [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

> [!tip] General Linear Group *(from Lie Theory)*
> The set of **invertible** elements of $\mathcal{L}(V)$, denoted $\operatorname{GL}(V)$, forms a group under composition. For finite-dimensional $V$ of dimension $n$, choosing a basis identifies $\operatorname{GL}(V)$ with the group $\operatorname{GL}_n(\mathbf{F})$ of invertible $n$-by-$n$ matrices. Over $\mathbf{F} = \mathbb{R}$ or $\mathbb{C}$, $\operatorname{GL}_n$ is also a smooth manifold, with the group operations smooth — it is a **Lie group**, and the entire subject of Lie theory begins with this and its closed subgroups ($\operatorname{SL}_n$, $\operatorname{O}(n)$, $\operatorname{U}(n)$, $\operatorname{Sp}_n$). Linear representations of groups, in turn, are homomorphisms into $\operatorname{GL}(V)$.

> [!tip] The Total Derivative and Differential Geometry *(from Multivariate Analysis)*
> For a smooth map $f : M \to N$ between manifolds at a point $x$, the **total derivative** $Df_x : T_x M \to T_{f(x)} N$ is by definition a linear map between tangent spaces. Linearity is what gives calculus its power: a smooth map is *locally* a linear map plus a higher-order correction, and "differentiate" *is* "find the best linear approximation". The chain rule reads $D(g \circ f)_x = Dg_{f(x)} \circ Df_x$ — composition of linear maps. See [[Def - The Total Derivative and Differentiability]].

> [!tip] Categorical Kernel and Cokernel *(from Homological Algebra)*
> In an abelian category like $\mathbf{Vect}_\mathbf{F}$, every morphism $T : V \to W$ has a categorical **kernel** (which is the inclusion $\operatorname{null} T \hookrightarrow V$) and a **cokernel** (which is the quotient map $W \twoheadrightarrow W / \operatorname{range} T$). The first isomorphism theorem $V / \operatorname{null} T \cong \operatorname{range} T$ then says every morphism factors canonically through its image. This is the structural content of [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] at the level of objects rather than dimensions, and the foundation of **homological algebra** — the study of complexes, exact sequences, and derived functors in abelian categories.
