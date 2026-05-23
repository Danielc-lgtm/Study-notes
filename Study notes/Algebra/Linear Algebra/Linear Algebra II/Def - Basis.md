---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Linear Combination and Span"
  - "Def - Linear Independence"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a field $F$, and $v_1, \ldots, v_n$ is a list of vectors in $V$. We use $n$ for the length of a basis (reserving $m$ for arbitrary lists); the relation $n = \dim V$ will be established once dimension is defined in [[Def - Dimension]]. The full notation registry for this chapter is on the parent page [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

---

# Axiom Motivation

A vector space, in the abstract, gives us no way to *name* its vectors. We have addition and scalar multiplication, but not coordinates. The point of a basis is to install coordinates — to give every vector $v \in V$ a tuple of scalars that names it uniquely. The question is: what conditions on a list $v_1, \ldots, v_n$ make this work?

There are two desiderata. The list must be **complete** — every vector of $V$ must be expressible as a linear combination $a_1 v_1 + \cdots + a_n v_n$, otherwise some vectors have no coordinates at all. This is exactly the [[Def - Linear Combination and Span|spanning]] condition: $\operatorname{span}(v_1, \ldots, v_n) = V$. The list must also be **non-redundant** — the coordinate tuple $(a_1, \ldots, a_n)$ assigned to a vector must be *unique*, otherwise different tuples name the same vector and "coordinates" are not well-defined. This is exactly the [[Def - Linear Independence|linear independence]] condition: the only combination giving $0$ is the trivial one (equivalently, every vector in the span has a unique expansion).

A basis is the conjunction of these two: a spanning list that is linearly independent. The two clauses do entirely different work, and we should stress what each is *for*. Spanning ensures every vector is reached at least once; independence ensures every vector is reached at most once. **Together** they say every vector is reached exactly once, which is the precise sense in which a basis identifies $V$ with $F^n$.

The per-axiom failure analysis is illuminating. Drop **spanning** and keep independence: you get a linearly independent list whose span is a *proper* [[Def - Subspace|subspace]] of $V$. Such a list installs coordinates on its own span but on no more — the vectors of $V$ lying outside the span have no representation at all. The list is "honest but incomplete". Example: $(1, 0, 0)$ in $\mathbb{R}^3$ is independent but does not span; it installs coordinates on the $x$-axis only.

Drop **independence** and keep spanning: you get a redundant spanning list. Every vector of $V$ has a representation, but the representation is *not unique* — multiple coefficient tuples name the same vector. The list is "complete but ambiguous". Example: $(1, 0), (0, 1), (1, 1)$ in $\mathbb{R}^2$ spans, but $(1, 1) = 1 \cdot (1, 0) + 1 \cdot (0, 1) + 0 \cdot (1, 1) = 0 \cdot (1, 0) + 0 \cdot (0, 1) + 1 \cdot (1, 1)$, and there is no canonical choice of coordinates for $(1, 1)$. Coordinates become a quotient over redundancies, not a faithful naming.

The empty list is admitted: it is a basis of the trivial space $\{0\}$. Vacuously it spans (every element of $\{0\}$ is the empty sum) and is linearly independent.

What about *strengthening* either axiom? Strengthening spanning to "two distinct lists span" would not buy us anything — every basis is part of a continuum of spanning lists, since adding any redundant vector preserves spanning. Strengthening independence to "every sub-list is also a basis" would force every basis to be empty (a basis of length $\geq 2$ has a length-1 sub-list, which would have to be a basis, hence span $V$, contradicting length $\geq 2$). The axioms as stated are exactly right.

A subtle point: **a basis is a list, not a set**. The ordering matters because coordinates are indexed by position — the tuple $(a_1, \ldots, a_n)$ identifies which $v_i$ each coefficient attaches to. If we changed the order of a basis, we would get a different basis (with a permuted coordinate assignment). This is a feature, not a bug: it lets us talk about "the first basis vector", "the standard basis" in a fixed order, and change-of-basis matrices in [[Linear Algebra III — §3A–D Linear Maps]]. The set of basis *vectors* is unordered and is sometimes useful (as in the **set-theoretic basis**), but the list structure is built into our definition.

Finally, why bases at all? Because once a basis is fixed, the vector space $V$ becomes computationally indistinguishable from $F^n$: every vector is faithfully recorded by its tuple. Linear algebra "in the abstract" becomes arithmetic in $F^n$. Every later result of linear algebra — the matrix representation of linear maps, change of basis, rank-nullity, eigenvalues, the spectral theorems — is computed *with respect to* a chosen basis. The basis is the bridge between the platonic vector space and concrete numerical computation.

---

# The Definition

A **basis** of a vector space $V$ over a field $F$ is a list $v_1, \ldots, v_n$ of vectors in $V$ that is
1. **linearly independent** (the only solution of $a_1 v_1 + \cdots + a_n v_n = 0$ is $a_1 = \cdots = a_n = 0$), and
2. **spans $V$** ($\operatorname{span}(v_1, \ldots, v_n) = V$).

**Equivalent characterisation (LADR 2.28, criterion for basis).** A list $v_1, \ldots, v_n$ is a basis of $V$ if and only if every $v \in V$ can be written **uniquely** in the form $v = a_1 v_1 + \cdots + a_n v_n$ with $a_i \in F$.

The unique tuple $(a_1, \ldots, a_n)$ is the **coordinate tuple** of $v$ with respect to the basis $v_1, \ldots, v_n$. The map $v \mapsto (a_1, \ldots, a_n)$ from $V$ to $F^n$ is a bijection — and in fact a vector-space isomorphism, as will be unpacked in [[Linear Algebra III — §3A–D Linear Maps]].

---

# Categorical / Structural Definition

A basis is the data of an **isomorphism** $V \cong F^n$, presented in a particular form.

Concretely: a list $v_1, \ldots, v_n$ of vectors in $V$ determines a linear map
$$\Phi : F^n \to V, \qquad (a_1, \ldots, a_n) \mapsto a_1 v_1 + \cdots + a_n v_n.$$
This map is well-defined and linear for any list. The list is a basis of $V$ if and only if $\Phi$ is a *bijective* linear map — that is, an **isomorphism** of vector spaces. The two conditions disentangle:

- $\Phi$ is **injective** $\iff$ the kernel of $\Phi$ is trivial $\iff$ the only solution of $\sum a_i v_i = 0$ is the zero tuple $\iff$ the list is linearly independent.
- $\Phi$ is **surjective** $\iff$ the image of $\Phi$ is all of $V$ $\iff$ every vector of $V$ is a linear combination of $v_1, \ldots, v_n$ $\iff$ the list spans $V$.

So a basis is, categorically, the choice of an isomorphism $F^n \xrightarrow{\sim} V$, and the basis vectors are the images of the standard basis of $F^n$ under that isomorphism. This is the cleanest viewpoint: the role of the basis is to set up a privileged isomorphism between an abstract space and a concrete one.

The universal-property version: an $n$-element list $v_1, \ldots, v_n$ in $V$ is a basis if and only if for every vector space $W$ and every list $w_1, \ldots, w_n$ in $W$, there exists a *unique* linear map $T : V \to W$ with $T v_i = w_i$. This is the **universal property of free [[Def - Module|modules]]** specialised to vector spaces: a basis exhibits $V$ as the free $F$-[[Def - Module|module]] on $n$ generators. The dual viewpoint is then the next chapter's "linear map lemma" (LADR 3.4).

---

# Relate to Other Fields / Compression

A basis is the **free generating set** of a free module specialised to the case of a field. In [[Def - Module|module]] theory over a ring $R$, a **free module** of rank $n$ is one isomorphic to $R^n$; an isomorphism $R^n \xrightarrow{\sim} M$ corresponds to a "basis" — a list of module elements with the same uniqueness-of-expansion property. The wrinkle over a general ring is that not every module is free, and even free modules may admit no "preferred" basis. Over a field every module is free, and bases are abundant; this abundance is precisely what makes finite-dimensional linear algebra a uniquely clean subject.

**True name (of basis):** "a list with respect to which every vector has unique coordinates." The textbook definition (independence + spanning) is the right thing to *verify*. The operational meaning, and the reason the concept is useful, is unique coordinates. When you see "basis" in a problem, translate as "coordinates exist and are unique" — that translation tells you immediately what theorems about the space can be invoked.

Compression in the other direction: a basis is the **minimal spanning list** and equivalently the **maximal linearly independent list**. Minimal because any sub-list of a basis fails to span (the missing vector has a unique expansion that uses the missing vector); maximal because no vector can be appended without inducing dependence (the new vector is already in the span and so is reachable from the others). The two extremal characterisations are dual and both useful: think of a basis as the equilibrium between "small enough for independence" and "large enough for spanning".

---

# Examples / Corollaries

**Example (standard basis of $F^n$).** $e_1 = (1, 0, \ldots, 0), e_2 = (0, 1, 0, \ldots, 0), \ldots, e_n = (0, \ldots, 0, 1)$ is the **standard basis** of $F^n$. Spanning: $(x_1, \ldots, x_n) = x_1 e_1 + \cdots + x_n e_n$. Independence: $a_1 e_1 + \cdots + a_n e_n = (a_1, \ldots, a_n) = 0$ forces all $a_i = 0$. The coordinate tuple of a vector with respect to the standard basis is the vector itself.

**Example (a non-standard basis of $F^2$).** $(1, 2), (3, 5)$ is a basis of $F^2$. Independence: $a(1, 2) + b(3, 5) = (a + 3b, 2a + 5b) = (0, 0)$ forces $a + 3b = 0$ and $2a + 5b = 0$, hence $a = b = 0$. Spanning: solving the system $(x, y) = a(1, 2) + b(3, 5)$ in unknowns $a, b$ for any target $(x, y)$ — the matrix $\begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix}$ has determinant $-1 \neq 0$ and is therefore invertible, so solutions exist. The coordinate tuple of $(1, 0)$ in this basis is found by solving: $a + 3b = 1, 2a + 5b = 0$, giving $b = 2, a = -5$, so $(1, 0) = -5(1, 2) + 2(3, 5)$.

**Example (standard basis of $\mathcal{P}_m(F)$).** $1, z, z^2, \ldots, z^m$ is a basis of the polynomial space $\mathcal{P}_m(F)$ — see [[Ex - Polynomials of degree at most n form a basis]]. The coordinate tuple of a polynomial is just its tuple of coefficients.

**Example (a basis adapted to a [[Def - Subspace|subspace]]).** $(1, 1, 0), (0, 0, 1)$ is a basis of the subspace $\{(x, x, y) \in F^3 : x, y \in F\}$. Spanning: any $(x, x, y) = x(1, 1, 0) + y(0, 0, 1)$. Independence: $a(1, 1, 0) + b(0, 0, 1) = (a, a, b) = (0, 0, 0)$ forces $a = b = 0$.

**Example (a basis "by parametric solution").** The subspace $U = \{(x, y, z) \in F^3 : x + y + z = 0\}$ has basis $(1, -1, 0), (1, 0, -1)$. Set $z = 0$: solutions are $(x, -x, 0) = x(1, -1, 0)$. Set $y = 0$: solutions are $(x, 0, -x) = x(1, 0, -1)$. Two free parameters, two basis vectors. This is operation 4 from the topic page.

**Non-example (linearly independent but not a basis).** $(1, 2, -4), (7, -5, 6)$ is a linearly independent list in $F^3$, but it is not a basis: the span is a 2-dimensional plane, missing every vector outside that plane. To make it a basis of $F^3$ you would need to extend it by one more vector outside the plane.

**Non-example (spanning but not a basis).** $(1, 2), (3, 5), (4, 13)$ is a spanning list of $F^2$, but it is not a basis: the third vector is a linear combination of the first two ($(4, 13) = -11(1, 2) + 5(3, 5)$, as you may verify), so any expansion using all three is non-unique.

**Corollary (criterion for basis as unique expansion).** A list is a basis iff every vector has a unique expansion. *Proof:* If a basis, spanning gives existence and independence gives uniqueness (by the subtraction trick — see [[Def - Linear Independence]] axiom motivation). Conversely, unique expansion gives spanning (every vector has an expansion) and independence (in particular, $0$ has only the trivial expansion).

**Corollary (a basis is a minimal spanning list).** Removing any vector from a basis produces a list that no longer spans. *Proof:* If $v_1, \ldots, v_n$ is a basis and we remove $v_k$, then $v_k$ itself has the unique expansion $0 \cdot v_1 + \cdots + 1 \cdot v_k + \cdots + 0 \cdot v_n$ in the original basis; this uniqueness means $v_k$ cannot be in the span of the others.

**Corollary (a basis is a maximal linearly independent list).** Adjoining any vector $w$ to a basis produces a linearly dependent list. *Proof:* By spanning, $w \in \operatorname{span}(v_1, \ldots, v_n)$, so $w = \sum a_i v_i$ for some scalars $a_i$; then $\sum a_i v_i + (-1) w = 0$ is a non-trivial vanishing combination.

**Calibration check.** If you have understood basis, you should be able to verify quickly: (a) the list $(1, 0), (0, 1), (1, 1)$ in $F^2$ is not a basis (it spans, but $(1, 1)$ has multiple expansions); (b) the list $(1, 0)$ in $F^2$ is not a basis (it is independent, but does not span); (c) the standard basis gives the *identity* coordinate map $F^n \to F^n$, and the choice of any other basis gives a non-identity coordinate change.

---

# Unlocked by This

> [!tip] Linear Map Determined by Action on a Basis *(from §3A)*
> The universal property of a basis says: to specify a linear map $T : V \to W$, it suffices to specify $T v_i$ for each basis vector $v_i$, and *any* choice of values is admissible. This is the **linear map lemma** (LADR 3.4), and it is the foundation of the matrix representation of linear maps in [[Linear Algebra III — §3A–D Linear Maps]]. The matrix entries of $T$ with respect to chosen bases of $V$ and $W$ are exactly the coordinates of the $T v_i$'s in the basis of $W$.

> [!tip] Change-of-Basis Matrix *(from §3D)*
> When $V$ has two bases $B$ and $B'$, every vector $v \in V$ has two coordinate tuples, one in each basis. The relationship between them is governed by the **change-of-basis matrix**, whose columns are the $B'$-coordinates of the basis vectors of $B$. This matrix is invertible by basis-extension and basis-reduction arguments, and the same vector has coordinates that transform by this matrix when one changes basis. The bookkeeping of multiple bases is the price of admission for keeping linear algebra abstract enough to apply to spaces that do not come with privileged coordinates — like tangent spaces of manifolds or operator algebras in quantum mechanics.

> [!tip] Hamel Basis *(from Functional Analysis)*
> Every vector space — including infinite-dimensional ones, like the space $L^2[0, 1]$ of square-integrable functions on the unit interval — has a basis, by an application of **Zorn's lemma** to the partial order of linearly independent subsets. Such a basis is called a **Hamel basis**. It satisfies the same uniqueness-of-expansion property, but in infinite-dimensional Banach spaces it is uncountable, cannot be exhibited explicitly, and is useless for analysis. The right notion in infinite-dimensional analysis is the **Schauder basis**, where one allows convergent infinite series instead of finite combinations — but Schauder bases exist only in separable Banach spaces, and their construction is subtle. Hamel bases are the algebraic generalisation; Schauder bases are the topological one.
