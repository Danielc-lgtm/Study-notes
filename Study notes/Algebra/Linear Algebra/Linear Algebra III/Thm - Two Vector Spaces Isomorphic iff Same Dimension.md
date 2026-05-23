---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Invertibility and Isomorphism"
  - "Def - Dimension"
  - "Def - Basis"
  - "Thm - Linear Map Determined by Action on Basis"
  - "Thm - Fundamental Theorem of Linear Maps"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ and $W$ are finite-dimensional vector spaces over the same field $\mathbf{F}$. The full notation registry is on [[Linear Algebra III — §3A–D Linear Maps]].

---

# Statement

> **Theorem.** Two finite-dimensional vector spaces $V$ and $W$ over $\mathbf{F}$ are [[Def - Invertibility and Isomorphism|isomorphic]] if and only if they have the same dimension:
>
> $$V \cong W \iff \dim V = \dim W.$$

> **Corollary 1.** Every $n$-dimensional vector space over $\mathbf{F}$ is isomorphic to $\mathbf{F}^n$. Hence dimension is the **complete invariant** of a finite-dimensional vector space.

> **Corollary 2.** With bases of $V$ and $W$ fixed, the matrix isomorphism $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ is an isomorphism of vector spaces; in particular,
> $$\dim \mathcal{L}(V, W) = (\dim V)(\dim W) = mn.$$

---

# Motivation

This theorem completes the project of identifying which finite-dimensional vector spaces are "the same". Vector spaces are abstract structures — sets with operations — and two of them might be presented in very different ways (polynomials, sequences, matrices, function spaces) while being "structurally identical". The theorem tells us when this happens: their [[Def - Dimension|dimensions]] agree, and that single number is everything.

The conclusion is at once trivial-seeming and profound. *Trivially*, dimension is the only invariant of a finite-dimensional vector space that one can write down, so it had better be the classification. *Profoundly*, this means that **every $n$-dimensional vector space over $\mathbf{F}$ is, structurally, just $\mathbf{F}^n$**. The space of polynomials of degree at most $n - 1$ is isomorphic to $\mathbf{F}^n$. The space of $m$-by-$n$ matrices is isomorphic to $\mathbf{F}^{mn}$. The space of functions on a finite set of size $n$ is isomorphic to $\mathbf{F}^n$. As vector spaces alone, all these are interchangeable — the abstract structure does not see the difference.

The practical payoff: every abstract problem about finite-dimensional vector spaces reduces to a concrete problem in $\mathbf{F}^n$ by choosing a basis (i.e., an isomorphism with $\mathbf{F}^n$). This is the **"choose coordinates"** strategy. Compute in $\mathbf{F}^n$, then translate the answer back. The matrix isomorphism $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$ is the analogous reduction for linear maps: choose bases, work with matrices, translate back.

The motivation has a deeper layer: the theorem says that **finite-dimensional vector spaces over $\mathbf{F}$ are *boring* up to isomorphism — they are classified by a single integer**. The interesting structure begins when you add: an inner product (creates dim-classified-up-to-isomorphism inner-product spaces, but the spaces gain notions of length and angle), a specific operator on $V$ (creates the rich similarity classification of operators), additional algebraic operations ([[Def - Ring|rings]], algebras), and so on. The abstract vector-space layer is the simplest layer; everything interesting is added structure.

This rigidity is special to vector spaces over a *field*. For [[Def - Module|modules]] over a general ring, the analogous theorem fails badly: the rank of a free module is well-defined (for commutative [[Def - Ring|rings]]), but not every module is free, and dimension-counting does not classify [[Def - Module|modules]]. For vector spaces, the structure is so simple that one number suffices.

---

# Sources and Targets

**Sources (Input Broadening)**

**Source: "are these two spaces the same?"** Compute their dimensions; if they agree, they are isomorphic, full stop. No explicit isomorphism needs to be constructed (although one can be — see the proof). Example problem: are $\mathcal{P}_4(\mathbb{R})$ (polynomials of degree at most $4$) and $\mathbb{R}^5$ isomorphic? Both have dimension $5$; yes.

**Source: "what is this space, abstractly?"** A space $V$ over $\mathbf{F}$ is, up to isomorphism, $\mathbf{F}^{\dim V}$. The "name" of a finite-dimensional space is its dimension. The non-obvious step: even when a space is presented in an exotic way (function spaces, quotient spaces, intersections of subspaces, dual spaces), the answer to "what is it?" is just $\mathbf{F}^n$ for some $n$. Example: what is $\mathcal{L}(\mathbb{R}^2, \mathbb{R}^3)$? Dimension $6$, so it is $\mathbb{R}^6$ — a $6$-dimensional real vector space.

**Source: "show $V$ and $W$ have the same dimension".** Direct application: build *any* isomorphism between them. The isomorphism need not be canonical or unique; it just needs to exist. Often the easiest isomorphism to find is via the matrix representation: choose bases on both sides, observe that both spaces map to $\mathbf{F}^n$, and the composition gives an isomorphism. Example: show $\mathcal{P}_n(\mathbb{R}) \cong \mathbb{R}^{n+1}$, by sending $a_0 + a_1 x + \cdots + a_n x^n \mapsto (a_0, a_1, \ldots, a_n)$.

**Source: "an injection between two equal-dimension spaces".** Combined with [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]], an injection automatically becomes an isomorphism. The non-obvious step: instead of constructing the *inverse* directly, construct an injection — much easier. Example: show $V \cong W$ where $V = \{p \in \mathcal{P}_3(\mathbb{R}) : p(0) = 0\}$ and $W = \mathcal{P}_2(\mathbb{R})$. The map $p \mapsto p'$ (or $p \mapsto p / x$, dividing out the root at zero) is an injection from $V$ to $W$, and both are $3$-dimensional, so it is an isomorphism.

**Targets (Output Amplification)**

**Combined with the matrix representation.** Given bases of $V$ and $W$, the matrix isomorphism $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ identifies the space of linear maps with the space of matrices, and dimension counts give $\dim \mathcal{L}(V, W) = mn$. The further result: every result about $\mathcal{L}(V, W)$ — its dimension, its structure as a vector space, its subspaces — has a matrix counterpart, and the dimension formula is the most basic application.

**Combined with rank–nullity.** For a linear map $T : V \to W$, rank–nullity gives $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$. Both terms on the right are dimensions of *vector spaces*: the null space and the range. By the theorem, each is determined up to isomorphism by its dimension. So the structure of $T$ is, abstractly, "a map sending an $\dim \operatorname{null} T$-dimensional kernel to zero and an $\dim \operatorname{range} T$-dimensional complement onto an $\dim \operatorname{range} T$-dimensional image" — every linear map of given rank looks "the same" up to choice of bases.

**Combined with subspace dimension equality.** A subspace $U \subseteq V$ with $\dim U = \dim V$ equals $V$ (a fact used in proving the previous theorem). This is the consequence: in finite dimensions, the only $\dim V$-dimensional subspace of $V$ is $V$ itself, so the "isomorphism" between $U$ and $V$ is the *identity*. Subspaces are not just isomorphic but equal when their dimensions match the ambient space.

**Combined with classification of operators up to similarity.** Two operators $T, T' \in \mathcal{L}(V)$ are **similar** if there is an invertible $S \in \mathcal{L}(V)$ with $T' = S T S^{-1}$. The theorem of this page says that *any two* $n$-dimensional vector spaces are isomorphic; but operators on them are *not* automatically similar — operators have additional invariants beyond dimension. So while the vector-space layer is one-parameter, the operator-on-$n$-dimensional-space layer has a much richer classification (eigenvalues, [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces|Jordan blocks]]). The dimension is necessary but not sufficient for operator equivalence.

---

# Why Is It True

Forget the formal proof and reason concretely. Two vector spaces are "the same" when there is a relabelling of their elements that preserves the vector-space operations. A relabelling is a bijection; preserving the operations makes it a linear isomorphism. So *isomorphism* means *invertible relabelling that respects the vector-space structure*.

Now: when can two finite-dimensional spaces be relabelled to match? The structure of a vector space is captured by its basis: every element is uniquely a linear combination of basis elements. If $V$ has a basis of $n$ elements and $W$ has a basis of $n$ elements, then there is an obvious bijection sending the $k$-th basis element of $V$ to the $k$-th basis element of $W$, and the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] extends this to a unique linear isomorphism. So same dimension forces isomorphism.

Conversely, if there is an isomorphism $T : V \to W$, then $T$ is an injection from $V$ into $W$. Injections send linearly independent lists to linearly independent lists (because $\sum c_k T v_k = 0$ implies $T(\sum c_k v_k) = 0$ implies $\sum c_k v_k = 0$ by injectivity), so a basis of $V$ maps to a linearly independent list of $\dim V$ vectors in $W$. Surjectivity of $T$ makes this list span $W$. So $T$ sends a basis of $V$ to a basis of $W$, both of length $\dim V$. Hence $\dim W = \dim V$.

> **The whole intuition in one sentence: a basis is finite data, and finite data of the same size can be matched up element by element, then extended by linearity to a structure-preserving bijection.**

The deeper reason this works for finite-dimensional spaces is that every linearly independent list of length $\dim V$ in $V$ is a basis. There is no "wiggle room" — once you have $\dim V$ independent vectors, they automatically span. In infinite [[Def - Dimension|dimensions]], this fails: a list of countably many linearly independent vectors might not span, even in a countably-dimensional space. The rigid coincidence "independent + maximally long = basis" is the technical heart of why dimension classifies vector spaces.

A second reason: vector spaces over a field are **free**, in the technical sense that they always have a basis. So they are classified by their "rank" (= dimension). For modules over more general rings, the analogue would be "free modules over $R$ are classified by their rank", but most modules are not free, and the classification is much more complex.

---

# What Makes This Hard

The theorem itself is easy — both directions are one-paragraph proofs from the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] and rank–nullity. The trap is in *forgetting that the field $\mathbf{F}$ matters*: $\mathbb{R}^2$ is *not* isomorphic to $\mathbb{C}$ as a vector space when both are viewed over the appropriate field. Over $\mathbb{R}$, $\mathbb{R}^2$ has dimension $2$ and $\mathbb{C}$ has dimension $2$ (as a real vector space), so they are isomorphic *as real vector spaces*. But $\mathbb{C}$ has dimension $1$ as a *complex* vector space, while $\mathbb{R}^2$ is not even a complex vector space (you cannot multiply real $2$-tuples by complex scalars in the natural way). The classification is sensitive to the scalar field.

A second subtle point: the theorem says "isomorphic as vector spaces", not "equal as sets" or "isomorphic as algebras" or "isomorphic as topological spaces". Two isomorphic vector spaces may have completely different additional structure — different inner products, different norms, different distinguished operators. The vector-space classification is the coarsest level.

A third subtle point: the theorem is **non-canonical** — there are many [[Def - Isomorphism|isomorphisms]] $V \cong W$, not just one. Choosing one requires choosing bases on both sides, and different choices give different [[Def - Isomorphism|isomorphisms]] (related by elements of $\operatorname{GL}_n$). The space of isomorphisms $V \to W$, when both have dimension $n$, is a torsor for $\operatorname{GL}_n(\mathbf{F})$. There is no preferred isomorphism unless extra structure is fixed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Use the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] to construct the isomorphism explicitly when dimensions agree; use the fact that an isomorphism sends a basis to a basis (preserving lengths of independent lists) to derive equality of dimensions when an isomorphism exists.

**Subgoal decomposition:**

1. **$\dim V = \dim W \Rightarrow V \cong W$.** Let $v_1, \ldots, v_n$ be a basis of $V$ and $w_1, \ldots, w_n$ be a basis of $W$ (both of length $n = \dim V = \dim W$).
   - By the linear-map lemma, there is a unique linear map $T : V \to W$ with $T v_k = w_k$ for each $k$.
   - $T$ is surjective: $w_1, \ldots, w_n$ spans $W$.
   - $T$ is injective: if $T(\sum c_k v_k) = \sum c_k w_k = 0$, linear independence of $w_k$ forces $c_k = 0$ for all $k$, hence $\sum c_k v_k = 0$.
   - So $T$ is a linear bijection, hence an isomorphism.
   
2. **$V \cong W \Rightarrow \dim V = \dim W$.** Let $T : V \to W$ be an isomorphism.
   - $T$ is injective, so $\dim \operatorname{null} T = 0$.
   - $T$ is surjective, so $\dim \operatorname{range} T = \dim W$.
   - By rank–nullity, $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T = 0 + \dim W = \dim W$.

---

# Lemma Decomposition

> [!note]- Lemma 1: An injection sends a basis to an independent list
> **Statement:** If $T : V \to W$ is an injective linear map and $v_1, \ldots, v_n \in V$ is linearly independent, then $T v_1, \ldots, T v_n \in W$ is also linearly independent.
>
> **Hint:** A linear relation $\sum c_k T v_k = 0$ pulls back via $T$ to $\sum c_k v_k \in \operatorname{null} T$, and injectivity makes $\operatorname{null} T = \{0\}$.
>
> **Why needed:** Used in proving "$V \cong W \Rightarrow \dim V = \dim W$": the isomorphism preserves linear independence, hence basis length.
>
> > [!note]- Full proof
> > Suppose $\sum_{k=1}^n c_k T v_k = 0$. By linearity, $T(\sum c_k v_k) = 0$, so $\sum c_k v_k \in \operatorname{null} T$. Since $T$ is injective, $\operatorname{null} T = \{0\}$, so $\sum c_k v_k = 0$. Linear independence of $v_1, \ldots, v_n$ forces $c_k = 0$ for each $k$. Hence $T v_1, \ldots, T v_n$ is linearly independent.

> [!note]- Lemma 2: A surjection sends a spanning set to a spanning set
> **Statement:** If $T : V \to W$ is a surjective linear map and $v_1, \ldots, v_n$ spans $V$, then $T v_1, \ldots, T v_n$ spans $W$.
>
> **Hint:** Every $w \in W$ is $Tv$ for some $v$; expand $v$ as a linear combination of $v_1, \ldots, v_n$ and apply $T$.
>
> **Why needed:** Combined with Lemma 1, an isomorphism sends a basis to a basis.
>
> > [!note]- Full proof
> > Let $w \in W$. By surjectivity, $w = Tv$ for some $v \in V$. Since $v_1, \ldots, v_n$ spans $V$, write $v = \sum c_k v_k$. Then $w = Tv = T(\sum c_k v_k) = \sum c_k T v_k$, so $w \in \operatorname{span}(T v_1, \ldots, T v_n)$. As $w$ was arbitrary, the spanning property holds.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V, W$ be finite-dimensional vector spaces over $\mathbf{F}$.
>
> **Direction 1: $\dim V = \dim W \Rightarrow V \cong W$.**
>
> Let $n = \dim V = \dim W$, $v_1, \ldots, v_n$ a basis of $V$, $w_1, \ldots, w_n$ a basis of $W$. By the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]], there is a unique linear map $T : V \to W$ with $T v_k = w_k$ for each $k$.
>
> Define $T$ explicitly: $T(c_1 v_1 + \cdots + c_n v_n) = c_1 w_1 + \cdots + c_n w_n$.
>
> $T$ is surjective: the basis $w_1, \ldots, w_n$ spans $W$, so every $w \in W$ is $\sum c_k w_k = T(\sum c_k v_k)$.
>
> $T$ is injective: suppose $T(\sum c_k v_k) = 0$. Then $\sum c_k w_k = 0$, and linear independence of $w_1, \ldots, w_n$ forces $c_k = 0$ for all $k$, hence $\sum c_k v_k = 0$.
>
> So $T$ is a linear bijection, hence an [[Def - Invertibility and Isomorphism|isomorphism]] (its set-theoretic inverse is automatically linear). Therefore $V \cong W$.
>
> **Direction 2: $V \cong W \Rightarrow \dim V = \dim W$.**
>
> Let $T : V \to W$ be an isomorphism. Then $T$ is injective and surjective.
>
> By [[Def - Null Space and Range|null-space-injectivity criterion]], $\operatorname{null} T = \{0\}$, so $\dim \operatorname{null} T = 0$.
>
> By surjectivity, $\operatorname{range} T = W$, so $\dim \operatorname{range} T = \dim W$.
>
> By [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] (using that $V$ is finite-dimensional):
> $$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T = 0 + \dim W = \dim W.$$
>
> Hence $\dim V = \dim W$. $\blacksquare$
>
> **Proof of Corollary 1: every $n$-dimensional space over $\mathbf{F}$ is isomorphic to $\mathbf{F}^n$.**
>
> $\mathbf{F}^n$ has dimension $n$ (with standard basis $e_1, \ldots, e_n$). Any $n$-dimensional $V$ also has dimension $n$. By the theorem, $V \cong \mathbf{F}^n$.
>
> **Proof of Corollary 2: $\dim \mathcal{L}(V, W) = mn$.**
>
> With bases of $V$ and $W$ fixed, the matrix map $\mathcal{M} : \mathcal{L}(V, W) \to \mathbf{F}^{m, n}$ is linear (its linearity is the content of LADR Propositions 3.35 and 3.38). It is injective: if $\mathcal{M}(T) = 0$, then $T v_k = 0$ for each basis vector $v_k$, so $T = 0$ by linearity. It is surjective: any matrix $A$ specifies the values of a linear map on a basis, and the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] constructs the corresponding $T$. So $\mathcal{M}$ is an isomorphism, and $\dim \mathcal{L}(V, W) = \dim \mathbf{F}^{m, n} = mn$. (The dimension of $\mathbf{F}^{m, n}$ is $mn$ by the standard basis of $mn$ matrix units $E_{j, k}$, each with a single $1$.) $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Pólya enumeration in combinatorics.** The space of polynomial functions $\mathbf{F}^n \to \mathbf{F}$ of degree at most $d$ is isomorphic to $\mathbf{F}^N$ for some $N$. Computing the dimension $N$ — counting monomials of total degree at most $d$ in $n$ variables — is a combinatorial exercise (Pólya counting), and the result is $N = \binom{n + d}{d}$. So the space of low-degree polynomial functions on $\mathbf{F}^n$ is *just* a finite-dimensional vector space of this size, classified abstractly by the formula. This explains why polynomial interpolation works: given $N$ data points, there is a unique polynomial of degree at most $d$ interpolating them — because the evaluation map at $N$ points is an isomorphism between two $N$-dimensional spaces.

**Hodge theory and harmonic forms.** On a compact Riemannian manifold, the **Hodge theorem** says the space of harmonic $k$-forms is finite-dimensional and isomorphic to the $k$-th de Rham cohomology $H^k_{dR}(M)$, which is a finite-dimensional real vector space. The dimensions $\dim H^k_{dR}(M)$ are the **Betti numbers** of $M$ — topological invariants. So the analytic problem (find harmonic forms) reduces to a topological problem (compute Betti numbers), via the dimension-classification theorem for finite-dimensional vector spaces.

**Representations of finite [[Def - Group|groups]].** A finite [[Def - Group|group]] $G$ has finitely many irreducible representations up to isomorphism (over an algebraically closed field of characteristic zero), each a finite-dimensional vector space. The classification of representations up to isomorphism is by dimension, character (which is finer than dimension for non-equivalent reps), and the regular-representation decomposition: the sum of squares of dimensions of irreducibles equals $|G|$. The starting point is the dimension classification: each irrep is, abstractly, just $\mathbf{F}^d$ for some $d$.

**Quantum information and qudits.** A **qudit** is a quantum system with finite-dimensional state space — a vector in $\mathbb{C}^d$, normalised. Two qudit systems of the same dimension are "the same" up to choice of basis (the theorem at play). In quantum information theory, the choice of basis corresponds to the choice of measurement — the same qudit can be measured in many "bases", and the choice does not change the abstract Hilbert space (it does change the physical measurement). The dimension classification is the foundation of "all $d$-level quantum systems are mathematically equivalent".

---

# Bridges

- **[[Thm - Linear Map Determined by Action on Basis]]** — supplies the construction of the isomorphism in the "$\Leftarrow$" direction. Given bases of equal length, the lemma builds a linear map sending one to the other; this map is automatically an isomorphism by injectivity and surjectivity on bases.

- **[[Thm - Fundamental Theorem of Linear Maps]]** — supplies the proof of the "$\Rightarrow$" direction. An isomorphism has $\dim \operatorname{null} T = 0$ and $\operatorname{range} T = W$, and rank–nullity converts this to $\dim V = \dim W$.

- **[[Thm - Injectivity Equals Surjectivity in Finite Dimensions]]** — works in conjunction with this theorem. In equal finite dimensions, an injection is automatically an isomorphism, so to *prove* two equal-dimension spaces are isomorphic it suffices to construct an injection from one to the other. The pair of theorems compresses isomorphism-construction to the easier task of injection-construction.

- **Cayley's theorem (group theory analogue)** — every group is a subgroup of a symmetric group $S_n$ for some $n$ (or some infinite cardinal). The vector-space analogue: every finite-dimensional vector space is *equal to* $\mathbf{F}^n$, not just a subspace of $\mathbf{F}^n$. The greater rigidity in linear algebra (equality, not just embedding) reflects that vector spaces are simpler structures than groups.

- **Structure theorem for finitely-generated abelian groups** — every finitely-generated abelian group is isomorphic to $\mathbb{Z}^r \oplus \bigoplus \mathbb{Z}/n_i$, with $r$ the **rank** and the $n_i$ the **torsion** elementary divisors. The torsion-free part is classified by a single integer $r$ (the rank), just like vector spaces. The whole structure is the abelian-group analogue of the dimension classification.

---

# Unlocked by This

> [!tip] Coordinate Reduction Strategy *(throughout linear algebra)*
> Every abstract problem in finite-dimensional linear algebra has a concrete coordinate version, by choosing a basis (= an isomorphism with $\mathbf{F}^n$). Compute in coordinates, then translate back. This is the standard problem-solving strategy in the subject, and the theorem of this page is its theoretical justification.

> [!tip] Matrix Representation as a Functor *(category theory)*
> The choice of basis on every finite-dimensional vector space simultaneously gives a functor from $\mathbf{Vect}_\mathbf{F}^{\mathrm{fin}, \mathrm{basis}}$ to the category $\mathbf{Mat}_\mathbf{F}$ of matrices. The theorem says this functor is essentially surjective (every $\mathbf{F}^n$ has dimension $n$, witnessing every dimension), and the [[Thm - Composition Corresponds to Matrix Multiplication|composition theorem]] says it is faithful. So $\mathbf{Vect}_\mathbf{F}^{\mathrm{fin}}$ and $\mathbf{Mat}_\mathbf{F}$ are equivalent categories.

> [!tip] Classification of Inner Product Spaces *(from Linear Algebra VI)*
> Two finite-dimensional inner-product spaces over $\mathbf{F}$ ($= \mathbb{R}$ or $\mathbb{C}$) are isometric (isomorphic preserving the inner product) iff they have the same dimension. So inner-product spaces over $\mathbf{F}$ are *also* classified by a single number — but the inner product gives an extra structure (length, angle) not seen by the vector-space layer. Every $n$-dim Euclidean space is isomorphic to $\mathbb{R}^n$ with the standard inner product. See [[Linear Algebra VI — §6 Inner Product Spaces]].

> [!tip] Classification of Operators up to Similarity *(from Linear Algebra V and VIII)*
> The classification of operators on $V$ up to similarity ($T \sim T' \iff T' = STS^{-1}$ for some invertible $S$) is *not* trivial — it depends on the eigenvalues, multiplicities, and Jordan-block structure. Two operators on isomorphic vector spaces of the same dimension can have wildly different structure. The dimension classifies the vector space; the **Jordan canonical form** (over algebraically closed fields) classifies the operator. See [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces]].

> [!tip] The Yoneda Embedding and Hom-Spaces *(category theory)*
> The matrix isomorphism $\mathcal{L}(V, W) \cong \mathbf{F}^{m, n}$ has a categorical analogue: the **Yoneda embedding** identifies an object of a category with the functor "$\operatorname{Hom}(-, X)$". The theorem of this page is one instance of "objects are determined by their hom-spaces", with dimensions being the only invariant of a vector space and matrices encoding all the hom-space data.
