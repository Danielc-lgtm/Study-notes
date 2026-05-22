---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Subspace"
  - "Def - Dual Space"
  - "Def - Dual Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over $\mathbb{F}$, $U \subseteq V$ is a subset (usually a subspace), and $V'$ is the [[Def - Dual Space|dual space]]. The **annihilator** of $U$ is
$$U^0 = \{\varphi \in V' : \varphi(u) = 0 \text{ for all } u \in U\}.$$
It is a subspace of $V'$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

**Convention.** The annihilator $U^0$ depends on the ambient space $V$, not just on $U$. A more precise notation would be $U^0_V$. Since $V$ is always clear from context in this topic, we use the simpler $U^0$.

---

# Axiom Motivation

The annihilator is the bridge between two pictures: subspaces of $V$ on one side, and subspaces of $V'$ on the other. It is the dual analogue of the subspace, in the same sense that the dual functional is the dual analogue of the vector.

The desideratum: given a subspace $U \leq V$, find the subspace of $V'$ "corresponding to $U$". There are two natural candidates.

The first candidate is the *restriction subspace* $\{\varphi|_U : \varphi \in V'\}$ — the linear functionals on $U$ obtained by restricting functionals on $V$. This is a subspace of $U'$ (not $V'$), and by extension-of-functionals it equals all of $U'$. So this construction does not produce a subspace of $V'$.

The second candidate is the *vanishing subspace*: the functionals in $V'$ that *vanish on $U$*. This is $U^0$, and it is naturally a subspace of $V'$. It has a clean dimension formula ($\dim U^0 = \dim V - \dim U$), it interacts well with subspace operations ($(U + W)^0 = U^0 \cap W^0$, $(U \cap W)^0 = U^0 + W^0$), and it sets up an *order-reversing bijection* between subspaces of $V$ and subspaces of $V'$. So the vanishing subspace — the annihilator — is the right answer.

Why is the order reversing? Because if $U \subseteq W$, then a functional vanishing on $W$ automatically vanishes on $U$ (the smaller set is contained in the larger), so $W^0 \subseteq U^0$. The smaller subspace has the *bigger* annihilator. This is the same order-reversal seen in "the smaller the subspace $U$, the more functionals annihilate it"; in the extremes, $\{0\}^0 = V'$ (every functional vanishes on $0$) and $V^0 = \{0\}$ (only the zero functional vanishes on all of $V$).

The deeper motivation is Galois-theoretic. A *Galois connection* between two posets $A$ and $B$ is a pair of order-reversing maps $f : A \to B$ and $g : B \to A$ satisfying $a \leq g(f(a))$ and $b \leq f(g(b))$ for all $a, b$. The pair $f, g$ becomes a bijection on the "closed" elements (those satisfying $a = g(f(a))$ or $b = f(g(b))$). The annihilator construction is the prototypical example in linear algebra.

Specifically: with $A$ = subspaces of $V$ and $B$ = subspaces of $V'$, define
$$f : U \mapsto U^0, \qquad g : \Omega \mapsto \Omega^0 = \{v \in V : \varphi(v) = 0 \text{ for all } \varphi \in \Omega\}.$$
Both are order-reversing. The closed elements on both sides are *all* subspaces (in finite dimensions), and the bijection $U \leftrightarrow U^0$ is a *contravariant Galois connection* — order-reversing, with $(U^0)^0 = U$. This is the universal property of the annihilator: it is the unique order-reversing bijection between the subspace lattices of $V$ and $V'$ that uses *only* the pairing $V' \times V \to \mathbb{F}$.

Why a Galois connection rather than a simple bijection? Because the construction generalises. The same shape of definition produces:
- the **annihilator** in algebraic geometry (variety $\leftrightarrow$ ideal);
- the **fixed field / fixed subgroup** in Galois theory (subgroup of automorphisms $\leftrightarrow$ subfield);
- the **polarity** in projective geometry (point $\leftrightarrow$ hyperplane);
- the **orthogonal complement** in an inner product space (subspace $\leftrightarrow$ its perpendicular subspace).

Each is a Galois connection associated to a bilinear pairing. The linear-algebraic annihilator is the simplest example, and it teaches the pattern.

---

# The Definition

Let $V$ be a vector space over $\mathbb{F}$ and $U \subseteq V$ a subset. The **annihilator** of $U$ is the set of linear functionals on $V$ that vanish on $U$:
$$U^0 := \{\varphi \in V' : \varphi(u) = 0 \text{ for all } u \in U\}.$$
The annihilator $U^0$ is a subspace of $V'$, even when $U$ is merely a subset of $V$ (not a subspace). Proof: the zero functional $0 \in V'$ lies in $U^0$ since $0(u) = 0$ for every $u$; if $\varphi, \psi \in U^0$ then $(\varphi + \psi)(u) = \varphi(u) + \psi(u) = 0$ for every $u \in U$, so $\varphi + \psi \in U^0$; and $\lambda \varphi \in U^0$ for $\lambda \in \mathbb{F}$ by linearity.

**Key properties** (proved in [[Thm - Null Space and Range of Dual Map]] and the exercise [[Ex - Annihilator of a subspace has complementary dimension]]):
- $\{0\}^0 = V'$ and $V^0 = \{0\}$.
- If $V$ is finite-dimensional and $U \leq V$ is a subspace, then $\dim U^0 = \dim V - \dim U$.
- $U \subseteq W$ implies $W^0 \subseteq U^0$ (order reversal).
- Under the canonical identification $V \cong V''$, $(U^0)^0 = U$ for subspaces $U \leq V$.

**Subspace lattice identities** (Exercise 22 of LADR §3F):
- $(U + W)^0 = U^0 \cap W^0$.
- $(U \cap W)^0 = U^0 + W^0$.

These two identities are the structural content of "annihilator turns sum into intersection and vice versa" — the standard signature of order reversal.

---

# Categorical / Structural Definition

The annihilator construction is a **contravariant Galois connection** between the lattice $L(V)$ of subspaces of $V$ and the lattice $L(V')$ of subspaces of $V'$, induced by the canonical bilinear pairing
$$\langle \cdot, \cdot \rangle : V' \times V \to \mathbb{F}, \qquad \langle \varphi, v \rangle = \varphi(v).$$

A bilinear pairing $\langle \cdot, \cdot \rangle : W \times V \to \mathbb{F}$ between two vector spaces automatically defines an annihilator-type Galois connection:
- For $U \subseteq V$, define $U^\perp \subseteq W$ as $\{w \in W : \langle w, u \rangle = 0 \text{ for all } u \in U\}$.
- For $\Omega \subseteq W$, define $\Omega^\perp \subseteq V$ as $\{v \in V : \langle w, v \rangle = 0 \text{ for all } w \in \Omega\}$.

These two operations are mutually inverse on "closed" subspaces (those equal to their double perp). For the canonical pairing $V' \times V \to \mathbb{F}$, every finite-dimensional subspace is closed, and the Galois connection becomes an *order-reversing bijection* of subspace lattices.

**Properties of any Galois connection.** From the order-reversal alone, the following are formal:
- $\{0\}^\perp = W$ and $W^\perp = \{0\}$;
- $U \subseteq W \Rightarrow W^\perp \subseteq U^\perp$;
- $(U + W)^\perp = U^\perp \cap W^\perp$ (smallest containing $U + W$ corresponds to largest contained in both perps);
- $(U \cap W)^\perp \supseteq U^\perp + W^\perp$, with equality on closed subspaces.

The dimension formula $\dim U + \dim U^\perp = \dim V$ is *not* a general Galois-connection property — it requires the *non-degeneracy* of the pairing (every nonzero $v$ has some $\varphi$ with $\varphi(v) \neq 0$, and vice versa). The pairing $V' \times V \to \mathbb{F}$ is non-degenerate in finite dimensions, which is why the dimension formula holds.

**The annihilator as part of a bigger functorial picture.** The map $U \mapsto U^0$ extends to a contravariant functor from "subspaces of finite-dimensional vector spaces and inclusions" to itself: it reverses inclusions and respects dualization. The same construction reappears in algebraic geometry as the variety-ideal correspondence (Nullstellensatz), in commutative algebra as the radical-of-ideal correspondence, and in algebraic topology as the cohomology-homology pairing.

---

# Relate to Other Fields / Compression

The annihilator is the linear-algebraic instance of a Galois connection. Across mathematics, whenever a bilinear pairing exists between two objects, an annihilator-type construction follows. The recurring shape: a subset of one side gets matched to "everything orthogonal to it" on the other side, the matching reverses inclusion, and under nondegeneracy double-orthogonalization recovers the original.

**True name:** the annihilator is "the subspace of $V'$ corresponding to $U$ under the canonical pairing" — the dual analogue of $U$, with dimension complementing $\dim U$ and order reversed.

In inner product spaces (Chapter 6), the annihilator collapses to the **orthogonal complement**: under the Riesz isomorphism $V \cong V'$ via $w \mapsto \langle \cdot, w \rangle$, the annihilator $U^0 \subseteq V'$ corresponds to the orthogonal complement $U^\perp \subseteq V$, and the formulas become the familiar ones from inner-product geometry.

In algebraic geometry, the **ideal of a variety** $I(V) = \{f : f(p) = 0 \text{ for all } p \in V\}$ and the **variety of an ideal** $V(I) = \{p : f(p) = 0 \text{ for all } f \in I\}$ form a Galois connection identical in shape to the annihilator. The Nullstellensatz says this connection becomes a bijection on the "closed" elements (radical ideals and Zariski-closed varieties).

In Galois theory, the connection between subgroups of $\operatorname{Gal}(L/K)$ and intermediate fields $K \subseteq M \subseteq L$ is again order-reversing under the pairing "is fixed by". This is the historical source of the term "Galois connection".

---

# Examples / Corollaries

**Is an instance — annihilator of $\operatorname{span}(e_1, e_2)$ in $\mathbb{R}^5$.** Let $V = \mathbb{R}^5$ with standard basis $e_1, \dots, e_5$ and dual basis $\varphi_1, \dots, \varphi_5$ (coordinate projections $\varphi_j(x) = x_j$). Let $U = \operatorname{span}(e_1, e_2) = \{(x_1, x_2, 0, 0, 0)\}$. A functional $\varphi = \sum c_k \varphi_k$ vanishes on $U$ iff $c_1 = c_2 = 0$ (computing $\varphi(e_1) = c_1$ and $\varphi(e_2) = c_2$). So $U^0 = \operatorname{span}(\varphi_3, \varphi_4, \varphi_5)$, a three-dimensional subspace of $V'$. Dimensions check: $\dim U = 2$, $\dim U^0 = 3$, $\dim V = 5$.

**Is an instance — annihilator of polynomials divisible by $x^2$.** Let $V = \mathcal{P}(\mathbb{R})$ and $U = x^2 \mathcal{P}(\mathbb{R}) = \{x^2 q(x) : q \in \mathcal{P}(\mathbb{R})\}$. The functional $\varphi(p) = p'(0)$ vanishes on $U$: for $p = x^2 q$, $p'(x) = 2x q(x) + x^2 q'(x)$, so $p'(0) = 0$. So $\varphi \in U^0$. Similarly $\psi(p) = p(0)$ is in $U^0$ since $p(0) = 0^2 q(0) = 0$. In fact $U^0 = \operatorname{span}(\psi, \varphi) = \operatorname{span}(\operatorname{ev}_0, \operatorname{ev}'_0)$, the "value at zero" and "derivative at zero" functionals.

**Is an instance — annihilator of the entire space.** $V^0 = \{0\}$: a functional vanishing on *all* of $V$ is the zero functional, so the annihilator of $V$ contains only the zero functional. Dimensions: $\dim V^0 = 0 = \dim V - \dim V$, the formula.

**Is an instance — annihilator of zero subspace.** $\{0\}^0 = V'$: every functional vanishes on the zero vector, so every functional is in the annihilator of $\{0\}$. The annihilator of the smallest subspace is the entire dual space — the order-reversing maximum.

**Is NOT an annihilator — a non-subspace of $V'$.** Some subsets of $V'$ are not annihilators of any subspace of $V$. For instance the set of functionals $\varphi$ with $\varphi(v) = 1$ for a fixed nonzero $v$ is not a subspace (it does not contain $0$). The annihilator construction always produces a *subspace*, so the question "is this set an annihilator?" is equivalent to "is this set a subspace, and does it equal the annihilator of its $0^0$-image?".

**Corollary — order reversal.** If $U \subseteq W$ (subspaces), then $W^0 \subseteq U^0$: any functional vanishing on $W$ vanishes on the smaller $U$ as well. The inclusion reverses.

**Corollary — annihilator complements dimension.** For finite-dimensional $V$ and $U \leq V$, $\dim U^0 = \dim V - \dim U$. Proof in [[Ex - Annihilator of a subspace has complementary dimension]] or via the inclusion-and-dualisation argument of LADR 3.125.

**Corollary — double annihilator recovers $U$.** Under the canonical identification $V \cong V''$, the double annihilator $(U^0)^0 \subseteq V$ equals $U$. This is the closed-element identity in the Galois connection. See LADR Exercise 20 (§3F): in finite dimensions, $U = \{v \in V : \varphi(v) = 0 \text{ for all } \varphi \in U^0\}$.

**Corollary — annihilator turns sum into intersection.** $(U + W)^0 = U^0 \cap W^0$ and $(U \cap W)^0 = U^0 + W^0$, for subspaces $U, W \leq V$. These convert subspace-arithmetic on $V$ into subspace-arithmetic on $V'$, swapping $+$ and $\cap$.

**Calibration check.** Verify that $\{0\}^0 = V'$ and $V^0 = \{0\}$. Compute $U^0$ for $U = \operatorname{span}(e_1)$ in $\mathbb{R}^3$, and confirm $\dim U^0 = 2$. Verify the order-reversing identity on inclusions: for $U \subseteq W \subseteq V$, that $W^0 \subseteq U^0$.

---

# Unlocked by This

> [!tip] Null Space and Range of Dual Map *(from this topic)*
> The annihilator is the structural tool for analysing the dual map: $\operatorname{null} T' = (\operatorname{range} T)^0$ and $\operatorname{range} T' = (\operatorname{null} T)^0$ — see [[Thm - Null Space and Range of Dual Map]]. The four-corner identity is the operational form of duality.

> [!tip] Orthogonal Complement *(from Linear Algebra VI)*
> In an [[Def - Inner Product Space|inner product space]] the annihilator becomes the **orthogonal complement** $U^\perp = \{v : \langle v, u \rangle = 0 \text{ for all } u \in U\}$, a subspace of $V$ itself. The dimension formula $\dim U + \dim U^\perp = \dim V$ is identical to the annihilator formula, and double-perp recovers $U$: $(U^\perp)^\perp = U$. The orthogonal complement is the *natural* (basis-free) version of the annihilator that exists when an inner product is available. See [[Def - Orthogonal Complement]] in [[Linear Algebra VI — §6 Inner Product Spaces|Chapter 6]].

> [!tip] Nullstellensatz *(from Algebraic Geometry)*
> The Galois connection between subsets of $\mathbb{F}^n$ and ideals in $\mathbb{F}[x_1, \dots, x_n]$ — variety $V(I) \leftrightarrow$ ideal $I(S)$ — is the polynomial analogue of the annihilator. Over an algebraically closed field, the **Hilbert Nullstellensatz** says the bijection is between *Zariski-closed varieties* and *radical ideals*, the closed elements of the connection. The same shape of theorem reappears in scheme theory and beyond.

> [!tip] Galois Theory *(from Algebra)*
> The fundamental theorem of Galois theory establishes a Galois connection between subgroups of $\operatorname{Gal}(L/K)$ and intermediate fields. The annihilator is the linear-algebraic prototype of this far deeper theorem.
