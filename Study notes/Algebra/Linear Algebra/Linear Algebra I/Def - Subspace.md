---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
  - "Def - Field"
tags: [algebra, linear-algebra]
---

# Notation

$V$ denotes a vector space over a [[Def - Field|field]] $\mathbb{F}$. A subspace is typically denoted $U, W$, or $V_1, V_2, \dots$. The notation $U \leq V$ is not standard in linear algebra; instead one writes "$U$ is a subspace of $V$" or simply $U \subseteq V$ with the qualifier "subspace" understood. The zero subspace is $\{0\}$, often just written $0$. See [[Linear Algebra I — §1 Vector Spaces]] for the full notation registry.

---

# Axiom Motivation

The thing we are trying to axiomatize is **the notion of a "sub-vector-space" — a subset of a vector space that is itself a vector space under the same operations**. This is the right thing to want for two reasons. First, an enormous fraction of the objects you encounter in linear algebra are subspaces of larger vector spaces: the kernel and image of a linear map, the span of a set of vectors, the eigenspaces of an operator, the intersection of two subspaces, the orthogonal complement of a set in an inner product space. Second, a subspace inherits the vector-space axioms automatically from the ambient space — so the question is not "what axioms does a subspace satisfy", but rather "what is the smallest set of conditions on a subset that guarantee it is a subspace".

The brute force answer is to demand the subset satisfy all eight vector-space axioms. But almost all of them are inherited for free. Commutativity, associativity, the multiplicative-identity axiom, and the two distributive laws all hold on any subset of $V$ — they are equations between elements that lie automatically in any superset of those elements. The axioms that are *not* automatic are the existence claims: that the additive identity exists in the subset, that addition lands inside the subset, that scalar multiplication lands inside the subset, and that additive inverses lie in the subset. Of these four, the last is redundant (it follows from closure under scalar multiplication via $-u = (-1) \cdot u$, see [[Def - Vector Space]]). So the minimal closure conditions are three: contains $0$, closed under addition, closed under scalar multiplication.

Each condition captures one feature, and dropping it kills exactly that feature. **Drop "$0 \in U$"**: then $U$ might be empty. The empty set fails to be a vector space because a vector space must contain an additive identity; without the explicit $0 \in U$ axiom the conditions are vacuously satisfied on the empty set, which we want to outlaw. One could replace "$0 \in U$" by "$U$ is nonempty" (LADR remarks on this), since then taking any $u \in U$ and multiplying by the scalar $0$ produces $0 \in U$ via closure under scalar multiplication. So nonemptiness plus closure under scalar multiplication is equivalent to having $0 \in U$. The reason "$0 \in U$" is preferred is that checking it is usually the fastest way to demonstrate nonemptiness — you just verify the zero vector satisfies the defining condition.

**Drop "closed under addition"**: take $U = \{(x, 0) : x \in \mathbb{R}\} \cup \{(0, y) : y \in \mathbb{R}\}$ in $\mathbb{R}^2$, the union of the two coordinate axes. This set contains $0$ and is closed under scalar multiplication (scaling stays on the same axis), but $(1, 0) + (0, 1) = (1, 1)$ is on neither axis. So the union of two subspaces is rarely a subspace — see [[Ex - Union of subspaces is a subspace iff one contains the other]] for the precise characterization. This is why we work with **sums** of subspaces (see [[Def - Sum of Subspaces]]) instead of unions: the sum is built to be closed under addition, the union is not.

**Drop "closed under scalar multiplication"**: take $U = \mathbb{Z}^2 \subset \mathbb{R}^2$. The integer lattice is closed under addition and contains $0$, but multiplying $(1, 0)$ by the scalar $\frac{1}{2}$ produces $(\frac{1}{2}, 0) \notin \mathbb{Z}^2$. So $\mathbb{Z}^2$ is a *subgroup* of $\mathbb{R}^2$ but not a subspace. This non-example exposes what scalar closure adds: it forces the subset to contain entire **lines through the origin**, not just discrete points. A subspace of $\mathbb{R}^n$ is a union of lines through the origin (plus the origin itself), and that union must additionally close under taking parallelograms.

A subtle alternative formulation: "$U$ is closed under linear combinations" — for all $u, v \in U$ and $a, b \in \mathbb{F}$, $au + bv \in U$. This single condition packages the three above, since taking $a = b = 1$ gives closure under addition, taking $b = 0$ gives closure under scalar multiplication, and (together with nonemptiness) it forces $0 \in U$. The three-condition formulation is preferred in practice because each piece is independently checkable; the one-condition formulation is conceptually cleaner. Both are common.

The combination of the three conditions admits an aesthetic reading: a subspace is **a non-empty subset of $V$ that is closed under both operations of $V$**. The phrase "closed under both operations" is the right cognitive handle, because the same idea (subgroup, subring, submodule, subalgebra, sub-anything) appears throughout algebra, always meaning "non-empty subset closed under the structure's operations".

---

# The Definition

Let $V$ be a vector space over a field $\mathbb{F}$. A **subspace** of $V$ is a subset $U \subseteq V$ that is itself a vector space under the addition and scalar multiplication inherited from $V$ — with the same additive identity.

The following test — the **subspace criterion** — is the standard way to verify that a subset is a subspace.

> **Subspace criterion.** A subset $U \subseteq V$ is a subspace of $V$ if and only if all three of the following hold:
> 1. **Contains zero.** $0 \in U$.
> 2. **Closed under addition.** For all $u, v \in U$, $u + v \in U$.
> 3. **Closed under scalar multiplication.** For all $\lambda \in \mathbb{F}$ and $u \in U$, $\lambda u \in U$.

Equivalently, $U$ is a subspace if and only if it is non-empty and closed under linear combinations: $au + bv \in U$ for all $u, v \in U$ and $a, b \in \mathbb{F}$.

The proof of the criterion is short. The "only if" direction is part of the definition of vector space restricted to $U$. For the "if" direction, the seven non-existence axioms (commutativity, associativity, identity behaviour, multiplicative identity, distributivity) are inherited from $V$; closure under addition makes addition a well-defined operation on $U$; closure under scalar multiplication makes scalar multiplication a well-defined operation on $U$; and $-u = (-1) u \in U$ by closure under scalar multiplication, so additive inverses lie in $U$. The condition "$0 \in U$" identifies the additive identity of $V$ as also serving as the additive identity of $U$, and ensures $U$ is nonempty.

---

# Categorical / Structural Definition

A subspace is **a monomorphism in $\mathbf{Vect}_{\mathbb{F}}$ that is the inclusion of an actual subset, up to canonical identification**. More usefully, the inclusion $U \hookrightarrow V$ is a [[Linear Algebra III — §3A–D Linear Maps|linear map]] that is injective. The collection of subspaces of $V$ forms a complete lattice under inclusion: the meet (intersection) of any family of subspaces is the set-theoretic intersection, and the join is the [[Def - Sum of Subspaces|sum]] $\sum_\alpha U_\alpha$ — note **not** the union, which generally fails to be a subspace.

In the language of [[Def - Module|modules]], a subspace is precisely a **[[Def - Submodule|submodule]]** of the underlying $\mathbb{F}$-module structure on $V$. The categorical content is the same: a subspace is a sub-object in $\mathbf{Vect}_{\mathbb{F}}$, equivalently a kernel of some quotient map $V \to V/U$ (every subspace is the kernel of its own quotient projection). The quotient construction — and the recognition that subspaces are exactly the kernels of linear maps out of $V$ — will be developed in [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

A subspace also has a **categorical universal property** with respect to the inclusion: for any linear map $T : W \to V$ whose image lies in $U$, there is a unique factorization $T = \iota \circ T'$ through the inclusion $\iota : U \hookrightarrow V$. This is the precise sense in which "a subspace is the largest vector space sitting inside $V$ with a given underlying set".

---

# Relate to Other Fields / Compression

A subspace is **a submodule** in the special case where the ring is a field — see [[Def - Submodule]]. The closure conditions are identical: contains zero, closed under addition, closed under scalar multiplication. The reason subspaces are easier to study than submodules in general is that vector spaces have bases, so every subspace is itself a free module with a basis that can be extended to a basis of the ambient space. Submodules of free modules over a ring are not generally free, which is the technical heart of why module theory is harder.

A subspace is also the **"linear" analogue of a subgroup** in group theory (see [[Def - Subgroup]]). The pattern repeats throughout algebra: sub-X is a non-empty subset closed under the operations defining X. The vector-space case is distinctive in that scalar closure forces lines through the origin to lie wholly inside the subspace, giving subspaces a geometric character (they are linear, hence flat) that sub-groups in general lack.

**True name:** the operational true name of a subspace is "a subset closed under linear combinations". This is what you actually check and what you actually use: every proof that something is a subspace amounts to verifying that an arbitrary linear combination of its elements still lies in the set, and every proof using a subspace exploits exactly the same closure.

---

# Examples / Corollaries

**Is an instance: lines and planes through the origin in $\mathbb{R}^3$.** Every line through the origin is a subspace of $\mathbb{R}^3$ — closed under scalar multiplication (the line is the set of multiples of a direction vector) and trivially closed under addition. Every plane through the origin is a subspace — the set $\{au + bv : a, b \in \mathbb{R}\}$ for two linearly independent vectors $u, v$. These plus $\{0\}$ and $\mathbb{R}^3$ itself are the *only* subspaces of $\mathbb{R}^3$. The constraint "through the origin" is exactly the requirement $0 \in U$: a line not through the origin fails the test immediately. See [[Ex - Subspaces of F^2 are classified]] for the $\mathbb{F}^2$ case.

**Is an instance: $\{(x_1, x_2, x_3, x_4) \in \mathbb{F}^4 : x_3 = 5 x_4\}$.** This subset of $\mathbb{F}^4$ is a subspace. To verify: $0 = (0,0,0,0)$ has $0 = 5 \cdot 0$, so $0$ is in the set. If $(x_1, x_2, x_3, x_4)$ and $(y_1, y_2, y_3, y_4)$ are both in the set, then their sum has third coordinate $x_3 + y_3 = 5 x_4 + 5 y_4 = 5(x_4 + y_4)$, so the sum is in the set. Scalar closure is analogous. The general rule: a subset of $\mathbb{F}^n$ defined by *homogeneous linear equations* is always a subspace; defined by *inhomogeneous* equations like $x_3 = 5 x_4 + b$ with $b \neq 0$, it is not.

**Is an instance: $C[0,1]$, continuous functions on $[0,1]$.** The continuous real-valued functions on the unit interval form a subspace of $\mathbb{R}^{[0,1]}$ (all functions $[0,1] \to \mathbb{R}$). The zero function is continuous; the sum of two continuous functions is continuous; a scalar multiple of a continuous function is continuous. These facts are the basic theorems of calculus, and verifying that $C[0,1]$ is a subspace is a packaging of those theorems into one structural claim. The same applies to $C^k$, $C^\infty$, integrable, differentiable, and polynomial functions: each is a subspace, and each inclusion strictly refines the previous one.

**Is an instance: $\mathcal{P}_m(\mathbb{F}) \subset \mathcal{P}(\mathbb{F})$.** The polynomials of degree at most $m$ form a finite-dimensional subspace (dimension $m + 1$, with basis $1, x, \dots, x^m$) of the infinite-dimensional space of all polynomials. The zero polynomial has degree $-\infty < m$, the sum of two polynomials of degree $\leq m$ has degree $\leq m$, and any scalar multiple stays in the same degree class.

**Is NOT an instance: $\{(x_1, x_2, x_3, x_4) \in \mathbb{F}^4 : x_3 = 5 x_4 + b\}$ with $b \neq 0$.** This **fails $0 \in U$**: the zero vector has $x_3 = 0$ and $5 x_4 + b = b \neq 0$. Such an "affine subset" is a translate of a subspace by the vector $(0, 0, b, 0)$, but it is not itself a subspace. The general principle: linear equations with right-hand side zero define subspaces; with nonzero right-hand side they define affine subsets. Affine subsets are the subject of quotient spaces — see [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

**Is NOT an instance: $\{(a, b, c) \in \mathbb{R}^3 : a^3 = b^3\} = \{(a, a, c) : a, c \in \mathbb{R}\}$.** Once you realize the cube root is unique in $\mathbb{R}$, this is the subspace $a = b$ — so it *is* a subspace, by accident. But over $\mathbb{C}$ the set $\{(a, b, c) \in \mathbb{C}^3 : a^3 = b^3\}$ contains $(1, 1, 0)$ and $(1, \omega, 0)$ for $\omega$ a primitive cube root of unity, and their sum $(2, 1 + \omega, 0)$ has $2^3 = 8 \neq (1+\omega)^3 = 1 + 3\omega + 3\omega^2 + \omega^3 = 1 + 3(-1) + 1 = -1$. So the set fails closure under addition over $\mathbb{C}$. This non-example probes the subtle point that the field matters: closure can hold over $\mathbb{R}$ and fail over $\mathbb{C}$.

**Is NOT an instance: $\{(x, y) \in \mathbb{R}^2 : xy = 0\}$, the union of the coordinate axes.** This fails closure under addition: $(1, 0) + (0, 1) = (1, 1)$, and $1 \cdot 1 = 1 \neq 0$. It is closed under scalar multiplication and contains $0$, so the union of two subspaces need not be a subspace. This non-example is the cleanest illustration of why we take sums, not unions, of subspaces — see [[Def - Sum of Subspaces]].

**Is NOT an instance: $\mathbb{Z}^2 \subset \mathbb{R}^2$.** The integer lattice contains $0$ and is closed under addition (and negation), but it **fails closure under scalar multiplication by non-integer reals**: $\frac{1}{2} \cdot (1, 0) = (\frac{1}{2}, 0) \notin \mathbb{Z}^2$. The lattice is a *subgroup* of $(\mathbb{R}^2, +)$ but not a subspace of $(\mathbb{R}^2)_{/\mathbb{R}}$. It is, however, a $\mathbb{Z}$-submodule.

**Is NOT an instance: the set of periodic functions $\mathbb{R} \to \mathbb{R}$.** A function $f$ is periodic if there exists $p > 0$ with $f(x + p) = f(x)$ for all $x$. This contains the zero function, is closed under scalar multiplication ($\lambda f$ has the same period as $f$), but **fails closure under addition**: $\sin(x)$ has period $2\pi$ and $\sin(\sqrt{2} x)$ has period $\sqrt{2}\pi$, but their sum is not periodic, because $2\pi$ and $\sqrt{2}\pi$ are incommensurable. The non-example shows that closure under addition is genuinely a constraint, separate from closure under scalar multiplication.

**Corollary (a subspace contains the additive identity of the ambient space).** A subspace $U \subseteq V$ contains $0_V$ (the zero of $V$), not some "different" zero. This is what is meant by the phrase "with the same additive identity" in the definition. It is a consequence of: if $u \in U$ then $u + 0_U = u$, and $u + 0_V = u$, and additive inverses in $V$ are unique, so $0_U = 0_V$. The corollary explains why we test "$0 \in U$" and not "$U$ has some additive identity": there is no choice.

**Corollary (additive inverses in $U$).** If $U$ is a subspace and $u \in U$, then $-u \in U$. The proof is $-u = (-1) u \in U$ by closure under scalar multiplication. This is why no separate "closed under additive inverses" axiom is needed in the subspace criterion.

**Corollary (intersection of subspaces is a subspace).** The intersection $U \cap W$ of two subspaces is a subspace. It contains $0$ (since both do), and if $u, v \in U \cap W$ then $u + v \in U$ (since $U$ is a subspace) and $u + v \in W$ (since $W$ is), hence $u + v \in U \cap W$. Scalar closure is analogous. The same argument extends to arbitrary intersections — see [[Ex - Intersection of subspaces is a subspace]]. This is the closure property under which the **span** of a set of vectors is defined: $\operatorname{span}(S) = \bigcap \{U : U \text{ is a subspace and } S \subseteq U\}$.

**Calibration check.** If you have understood the definition you should be able to (i) write down all subspaces of $\mathbb{R}^2$ (only $\{0\}$, all lines through the origin, and $\mathbb{R}^2$ itself — see [[Ex - Subspaces of F^2 are classified]]); (ii) check that the set of differentiable functions $f : \mathbb{R} \to \mathbb{R}$ with $f'(0) = 0$ is a subspace of $\mathbb{R}^\mathbb{R}$ (yes, it is, the derivative at $0$ is a linear functional on the differentiable functions); (iii) explain in one sentence why the set of monic polynomials of degree exactly $n$ is *not* a subspace ($0$ is not monic, also the sum of two monic polynomials of degree $n$ may have degree $< n$).

---

# Unlocked by This

> [!tip] Quotient Space *(from Linear Algebra IV)*
> Once you have a subspace $U \subseteq V$, you can form the **quotient space** $V/U$ — the set of affine translates $v + U$ of $U$, made into a vector space by defining $(v + U) + (w + U) = (v + w) + U$ and $\lambda(v + U) = (\lambda v) + U$. This is exactly the construction parallel to quotients in [[Def - Quotient Group|group theory]] and [[Def - Quotient Ring|ring theory]]. See [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

> [!tip] Span and Linear Independence *(from Linear Algebra II)*
> The intersection of all subspaces containing a set $S$ is itself a subspace, called the **span** of $S$. The span is the "smallest subspace containing $S$", and characterizing it concretely (as the set of finite linear combinations of elements of $S$) is the gateway to bases and dimension. See [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]].

> [!tip] Kernel and Image of a Linear Map *(from Linear Algebra III)*
> The kernel of a linear map $T : V \to W$ is a subspace of $V$; the image is a subspace of $W$. Conversely, *every* subspace of $V$ is the kernel of some linear map out of $V$ (the quotient map $V \to V/U$). This identifies subspaces with the "things you can quotient by" and is the linear analogue of the kernel-versus-normal-subgroup correspondence in [[Def - Normal Subgroup|group theory]].

> [!tip] Orthogonal Complement *(from Linear Algebra VI)*
> In an inner-product space, every subspace $U$ has an **orthogonal complement** $U^\perp = \{v : \langle v, u \rangle = 0 \text{ for all } u \in U\}$, which is also a subspace and which decomposes $V = U \oplus U^\perp$. This is the structural device behind orthogonal projections and Fourier series; it generalizes the geometric "drop a perpendicular" from $\mathbb{R}^3$ to arbitrary inner-product spaces.

> [!tip] Closed Subspace of a Banach Space *(from Functional Analysis)*
> In an infinite-dimensional **Banach space** or **Hilbert space**, one distinguishes general subspaces from **closed** subspaces — those that are also closed in the topology induced by the norm. Many subspaces of analytical interest (the kernel of a continuous linear operator, the closure of a span) are automatically closed; many are not. The theorem that finite-dimensional subspaces are always closed is one of the rare cases where finite-dimensionality alone gives a topological fact.

> [!tip] Subvariety and Closed Subscheme *(from Algebraic Geometry)*
> The notion of "a subset defined by polynomial equations" generalizes the linear-algebraic "subset defined by linear equations" to **subvarieties** of affine and projective space, and further to closed subschemes. Linear subspaces are the simplest case — subvarieties of degree one — and the geometric intuition built in linear algebra (intersection, sum, projection) carries over with corrections for higher degree.
