---
type: definition
subject: module-theory
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Module Homomorphism"
  - "Def - Ring"
  - "Def - Abelian Group"
tags: [algebra, module-theory]
---

# Notation

Throughout, $R$ is a fixed ring (commutative, with $1$, unless stated otherwise) and all modules are left $R$-modules. Given $R$-modules $M_1, M_2, \dots, M_k$, their **direct sum** is written $M_1 \oplus M_2 \oplus \cdots \oplus M_k$, or $\bigoplus_{i=1}^k M_i$. Its elements are tuples $(m_1, \dots, m_k)$ with $m_i \in M_i$; module addition and the $R$-action are both componentwise. The $n$-fold direct sum of the ring $R$ with itself, viewed as a module over itself, is written $R^n = R \oplus \cdots \oplus R$ and is the prototype of a [[Def - Free Module|free module]]. The canonical inclusion of the $i$-th summand is $\iota_i : M_i \hookrightarrow \bigoplus_j M_j$, and the canonical projection onto it is $\pi_i : \bigoplus_j M_j \twoheadrightarrow M_i$. The full notation registry lives on the parent page [[Modules I — §3.1–3.2]].

---

# Axiom Motivation

The thing we are trying to build is a way to **bundle several [[Def - Module|modules]] into one module so that each original sits inside the bundle untouched and independent of the others**, and so that the bundled module's structure is completely transparent in terms of the pieces. This is the most basic constructive move in module theory: we have a stock of modules and we want a machine that glues them with no interaction at all. For [[Def - Abelian Group|abelian groups]] this machine is the direct product; the direct sum is that same machine carried over to modules, where there is one extra piece of structure — the $R$-action — that must also be glued.

Begin with the desiderata. We want an $R$-module, call it $S$, that contains a faithful copy of each $M_i$, where "faithful copy" means three things at once. First, each $M_i$ should embed as a genuine [[Def - Submodule|submodule]] of $S$ — an undistorted copy, closed under addition and under the $R$-action. Second, the copies should be **independent**: the $M_i$-component of an element should be readable off without reference to the other components, so an element of $S$ is exactly a free choice of one element from each $M_i$, and nothing is identified across summands. Third, the copies should not interfere: adding an element of the copy of $M_i$ to an element of the copy of $M_j$ should produce a genuinely new element with both components recorded, and the copies should overlap only in the zero element. If these hold, $S$ deserves to be called "the $M_i$ laid side by side", and all of its structure is recoverable from the $M_i$ alone.

Now ask what operations on tuples $(m_1, \dots, m_k)$ deliver exactly this. The underlying set must be the Cartesian product $M_1 \times \cdots \times M_k$, because independence demands every choice-of-one-from-each and a product of sets is the only thing parametrised by one coordinate per summand. For the addition, the only candidate respecting independence is **componentwise** addition, $(m_1, \dots, m_k) + (m'_1, \dots, m'_k) = (m_1 + m'_1, \dots, m_k + m'_k)$: any rule that mixed coordinates would make the $M_i$-component of a sum depend on the other summands, destroying independence. The genuinely module-theoretic question is the $R$-action. An $R$-module is an abelian group together with a map $R \times M \to M$ scaling elements by [[Def - Ring|ring]] elements; to glue $k$ modules we must say how a ring element $r$ scales a tuple. Again independence forces the answer: $r$ must act **componentwise**, $r \cdot (m_1, \dots, m_k) = (r m_1, \dots, r m_k)$, scaling each coordinate by the action it already carries in its own $M_i$. Any action that let $r$ move mass between coordinates would couple the summands. Componentwise addition and componentwise scaling are both forced the instant one insists on independence.

Check that these componentwise operations give an $R$-module, and notice that every module axiom is inherited coordinate by coordinate. The tuples form an abelian group under componentwise addition because each $M_i$ is one; the zero is $(0, \dots, 0)$ and the negative of $(m_1, \dots, m_k)$ is $(-m_1, \dots, -m_k)$. The module axioms — $r(x + y) = rx + ry$, $(r + s)x = rx + sx$, $(rs)x = r(sx)$, $1 \cdot x = x$ — each reduce to the same axiom holding separately in every slot, because both operations act slot by slot. Nothing new has to be checked. This is the sense in which the direct sum is the **free glue**: it demands no compatibility whatsoever between the $M_i$, and there is exactly one module structure on the product set making each inclusion a [[Def - Module Homomorphism|module homomorphism]].

It is worth seeing the desiderata realised concretely inside $S = \bigoplus_i M_i$. The copy of $M_j$ is the [[Def - Submodule|submodule]] $\bar M_j = \{(0, \dots, 0, m_j, 0, \dots, 0) : m_j \in M_j\}$ of tuples supported in the $j$-th slot; it is a genuine submodule, isomorphic to $M_j$ via $m_j \mapsto \iota_j(m_j)$, and $\bar M_i \cap \bar M_j = \{0\}$ for $i \neq j$ because a tuple supported in slot $i$ and also in slot $j$ must be zero. Every element decomposes uniquely as $(m_1, \dots, m_k) = \iota_1(m_1) + \cdots + \iota_k(m_k)$, one piece per copy. These are exactly the independence and non-interference demands made flesh. Now ask what breaks under perturbation. If we weakened the construction by passing to a *quotient* of the direct sum — identifying some elements of $\bar M_i$ with elements of $\bar M_j$ — the copies would cease to be independent and an element would no longer determine its components. If we strengthened it by demanding the $M_i$ be equal we would lose the ability to bundle *different* modules and recover only diagonal copies. The direct sum is calibrated exactly at "finitely many arbitrary modules, glued with no interaction".

The reason to fix this definition rather than a nearby variant is what it must support downstream: a [[Def - Free Module|free module]] is by construction a direct sum of copies of $R$, and the [[Thm - Finitely Generated Modules and Surjections from a Free Module|surjection theorem]] says every finitely generated module is a quotient of some $R^n$. If "direct sum" allowed the copies of $R$ to overlap, the [[Thm - Invariance of Rank|invariance of rank]] result $R^n \cong R^m \Rightarrow n = m$ would fail, because the integer $n$ would no longer faithfully count independent copies. The untwisted, trivially-intersecting direct sum is the precise notion for which "$R^n$ has a well-defined rank $n$" comes out true.

---

# The Definition

Let $R$ be a ring and let $M_1, M_2, \dots, M_k$ be left $R$-modules. The **direct sum**

$$M_1 \oplus M_2 \oplus \cdots \oplus M_k$$

is the $R$-module whose underlying set is the Cartesian product $M_1 \times M_2 \times \cdots \times M_k$ — the set of all tuples $(m_1, \dots, m_k)$ with $m_i \in M_i$ — equipped with **componentwise addition**

$$(m_1, \dots, m_k) + (m'_1, \dots, m'_k) = (m_1 + m'_1,\ \dots,\ m_k + m'_k)$$

and the **componentwise $R$-action**

$$r \cdot (m_1, \dots, m_k) = (r m_1,\ \dots,\ r m_k), \qquad r \in R.$$

These operations make $M_1 \oplus \cdots \oplus M_k$ a left $R$-module: it is an abelian group with zero $(0, \dots, 0)$ and negatives $-(m_1, \dots, m_k) = (-m_1, \dots, -m_k)$, and every module axiom holds because it holds coordinate by coordinate in each $M_i$.

The **prototype**, used constantly, is the $n$-fold direct sum of the ring $R$ — regarded as a module over itself — with itself:

$$R^n = \underbrace{R \oplus R \oplus \cdots \oplus R}_{n \text{ times}},$$

the module of $n$-tuples of ring elements, with componentwise addition and $r \cdot (a_1, \dots, a_n) = (r a_1, \dots, r a_n)$.

Inside $\bigoplus_{i=1}^k M_i$ there are two canonical families of [[Def - Module Homomorphism|module homomorphisms]]. The **canonical inclusions**

$$\iota_j : M_j \longrightarrow \bigoplus_{i=1}^k M_i, \qquad \iota_j(m) = (0, \dots, 0, \underset{j}{m}, 0, \dots, 0),$$

place an element into the $j$-th slot and zero elsewhere; each $\iota_j$ is an injective module homomorphism, and its image $\bar M_j = \iota_j(M_j)$ is a [[Def - Submodule|submodule]] isomorphic to $M_j$. The **canonical projections**

$$\pi_j : \bigoplus_{i=1}^k M_i \longrightarrow M_j, \qquad \pi_j(m_1, \dots, m_k) = m_j,$$

read off the $j$-th coordinate; each $\pi_j$ is a surjective module homomorphism. They satisfy $\pi_j \circ \iota_j = \mathrm{id}_{M_j}$, while $\pi_i \circ \iota_j = 0$ for $i \neq j$, and $\sum_{j=1}^k \iota_j \circ \pi_j = \mathrm{id}$ on the whole direct sum — every element is the sum of its slot-projections re-included.

**Direct sum equals direct product, for finitely many summands.** The *direct product* $\prod_{i=1}^k M_i$ is the same product set with the same componentwise operations. For a **finite** index set the two constructions therefore coincide as $R$-modules, $M_1 \oplus \cdots \oplus M_k = M_1 \times \cdots \times M_k$, and the notations are interchangeable. The distinction appears only for an **infinite** family $\{M_i\}_{i \in I}$: the direct product $\prod_{i \in I} M_i$ allows tuples with *every* coordinate nonzero, whereas the direct sum $\bigoplus_{i \in I} M_i$ is the submodule of those tuples with only **finitely many nonzero coordinates**. The whole of this section concerns finitely many summands, where no such distinction arises.

---

# Categorical Definition

The direct sum is characterised, without ever mentioning tuples, by a **universal property**: a property phrased purely in terms of [[Def - Homomorphism|homomorphisms]] into and out of the object, which pins the object down up to unique isomorphism. For finitely many summands the direct sum carries *two* universal properties at once — one for maps in, one for maps out — because for finite index sets it is simultaneously the categorical *product* and the categorical *coproduct* of the $M_i$.

The property singled out here is the one for **maps out**, the coproduct property, because it is the property the [[Def - Free Module|free module]] inherits and the one phrased "a map out of the direct sum is the same as a map out of each summand". State it as follows. The direct sum $S = \bigoplus_{i=1}^k M_i$ comes equipped with the canonical inclusions $\iota_i : M_i \to S$. The claim is that this data is **universal among modules receiving a map from every $M_i$**: for any $R$-module $N$ and any family of [[Def - Module Homomorphism|module homomorphisms]] $f_i : M_i \to N$, one for each summand, there exists a **unique** module homomorphism

$$f : \bigoplus_{i=1}^k M_i \longrightarrow N \qquad \text{with} \qquad f \circ \iota_i = f_i \ \text{ for every } i.$$

Concretely the unique $f$ is $f(m_1, \dots, m_k) = f_1(m_1) + f_2(m_2) + \cdots + f_k(m_k)$: to map the tuple, split it into slots, push each slot through its own $f_i$, and add the results in $N$. It is a homomorphism because addition and the $R$-action in the direct sum are componentwise; it is forced to take this value because $f(m_1, \dots, m_k) = f\bigl(\sum_j \iota_j(m_j)\bigr) = \sum_j f(\iota_j(m_j)) = \sum_j f_j(m_j)$, so any homomorphism agreeing with the $f_i$ on the slots must be this one.

The slogan is therefore precise: **a homomorphism out of $M_1 \oplus \cdots \oplus M_k$ is exactly the same data as a homomorphism out of each $M_i$ separately**. There is a bijection
$$\operatorname{Hom}_R\Bigl(\bigoplus_i M_i,\ N\Bigr) \ \cong \ \prod_i \operatorname{Hom}_R(M_i,\ N),$$
natural in $N$, sending $f$ to the tuple $(f \circ \iota_i)_i$. Maps out of a direct sum decouple summand by summand; there is no compatibility condition to satisfy, which is the homomorphism-level shadow of the summands being glued with no interaction. This is the property that makes the direct sum the right *domain* for defining maps, and it is exactly the property the free module will turn into "a map out of a free module is a free choice of where each basis element goes".

Dually, the same object with the **projections** $\pi_i : S \to M_i$ satisfies the universal property for **maps in** — the categorical product property — giving a unique $g : T \to \bigoplus_i M_i$ for every family $g_i : T \to M_i$, namely $g(t) = (g_1(t), \dots, g_k(t))$, and a bijection $\operatorname{Hom}_R(T, \bigoplus_i M_i) \cong \prod_i \operatorname{Hom}_R(T, M_i)$. That product and coproduct coincide here is exactly the statement, made categorical, that for finitely many summands the direct sum equals the direct product. The universal properties, not the tuple recipe, are the true content: they determine $\bigoplus_i M_i$ up to a unique isomorphism, and the componentwise operations are *forced* by them rather than chosen.

---

# Relate to Other Fields / Compression

The direct sum of $R$-modules is, when $R = \mathbb{Z}$, **literally the direct product of abelian groups**. A $\mathbb{Z}$-module is exactly an abelian group — the $\mathbb{Z}$-action $n \cdot m$ is forced to be the $n$-fold sum $m + \cdots + m$ — and componentwise addition of tuples is the abelian-group direct product operation. So $M \oplus N$ of two $\mathbb{Z}$-modules is the group [[Def - Direct Product|direct product]] $M \times N$, and the module-theoretic notion is the abelian-group one with the redundant $\mathbb{Z}$-action made explicit. This is why the classification of finite abelian groups as products of cyclic groups is the same statement as the structure theorem decomposing a finitely generated $\mathbb{Z}$-module into a direct sum of cyclic modules $\mathbb{Z}/(d_i)$.

When $R = k$ is a field, the direct sum of $R$-modules is **the direct sum of vector spaces** from linear algebra. A module over a field is exactly a vector space, the $R$-action being scalar multiplication, and $V_1 \oplus \cdots \oplus V_k$ is the vector space of tuples with componentwise operations, of dimension $\dim V_1 + \cdots + \dim V_k$. The internal decomposition $V = U \oplus W$ of a space into complementary subspaces, met in any first linear-algebra course, is this construction recognised from the inside. Module theory is the single framework in which "direct product of abelian groups" and "direct sum of vector spaces" are revealed as one construction, taken over $\mathbb{Z}$ and over a field respectively.

One sharp compression: the direct sum is the **biproduct** — the construction that is simultaneously product and coproduct. In a general category these are different universal properties and need not be inhabited by the same object; the special feature of modules (and of abelian categories generally) is that for finitely many objects they coincide. The reason is that a module has a *zero* element and *addition* of homomorphisms, which lets one build the comparison map $\bigoplus M_i \to \prod M_i$ and show it is the identity. So "$\oplus$ and $\times$ agree for finitely many summands" is not a coincidence of the tuple description but a structural fact about categories rich enough to add their morphisms.

---

# Examples / Corollaries

**Is an instance: $R^n$, the standard free module.** Taking every summand equal to the ring $R$ acting on itself by left multiplication gives $R^n = R \oplus \cdots \oplus R$, the module of $n$-tuples of ring elements. For $R = \mathbb{Z}$ this is $\mathbb{Z}^n$, the free abelian group of rank $n$; for $R = k$ a field it is the coordinate space $k^n$. This is the single most important instance of the direct sum: it is the prototype of a [[Def - Free Module|free module]], and the $n$-tuples $e_i = (0, \dots, 0, 1, 0, \dots, 0)$ form its standard basis.

**Is an instance: $\mathbb{Z}/6 \cong \mathbb{Z}/2 \oplus \mathbb{Z}/3$ as $\mathbb{Z}$-modules.** The cyclic group of order $6$ decomposes as the direct sum of the cyclic [[Def - Group|groups]] of orders $2$ and $3$, because $\gcd(2,3) = 1$ — this is the Chinese remainder theorem read at the level of $\mathbb{Z}$-modules. The decomposition shows the direct sum genuinely produces *new* modules: the bundle $\mathbb{Z}/2 \oplus \mathbb{Z}/3$ is not visibly cyclic, yet it is, with generator $(1,1)$ of order $\operatorname{lcm}(2,3) = 6$.

**Is an instance (internal): $V = U \oplus W$ for complementary [[Def - Subspace|subspaces]] of a vector space.** If $U$ and $W$ are subspaces of a $k$-vector space $V$ with $U \cap W = \{0\}$ and $U + W = V$, then $V$ is the internal direct sum of $U$ and $W$: every vector splits uniquely as $u + w$. This is the direct-sum construction recognised inside a module already given whole — the abstract bundle $U \oplus W$ and the subspace $V$ are identified by the isomorphism $(u, w) \mapsto u + w$.

**Is NOT an instance: $\mathbb{Z}/6$ is not $\mathbb{Z}/2 \oplus \mathbb{Z}/2$.** Both modules have six... — *correction:* both are finite, but $\mathbb{Z}/6$ has $6$ elements while $\mathbb{Z}/2 \oplus \mathbb{Z}/2$ has $4$, so they are not even of the same size. More instructively, $\mathbb{Z}/4$ and $\mathbb{Z}/2 \oplus \mathbb{Z}/2$ both have four elements but are *not* isomorphic as $\mathbb{Z}$-modules: $\mathbb{Z}/4$ has an element of additive order $4$, namely $1$, whereas in $\mathbb{Z}/2 \oplus \mathbb{Z}/2$ every nonzero element $(a,b)$ satisfies $2 \cdot (a,b) = (0,0)$. Equal cardinality does not make modules isomorphic; the direct-sum structure records strictly more than the count of elements.

**Is NOT an instance: the submodule $\{(m, m) : m \in M\}$ of $M \oplus M$ is a copy of $M$, not a direct summand decomposition.** The diagonal $\Delta = \{(m,m)\}$ is a genuine submodule of $M \oplus M$ isomorphic to $M$, but $M \oplus M$ is *not* the internal direct sum of $\Delta$ with the first canonical copy $\bar M_1 = \{(m, 0)\}$ unless one checks $\Delta \cap \bar M_1 = \{0\}$ (true) *and* $\Delta + \bar M_1 = M \oplus M$ (also true here, since $(a,b) = (b,b) + (a-b, 0)$) — so in fact this *is* a valid internal decomposition $M \oplus M = \Delta \oplus \bar M_1$. The lesson is the cautionary one: a submodule isomorphic to a summand is not automatically *the* summand, and an internal direct sum requires both the trivial-intersection and the spanning condition to be verified, never assumed.

**Corollary (a homomorphism out of $R^n$ is $n$ free choices of target).** By the universal property, a module homomorphism $f : R^n \to N$ is the same data as $n$ homomorphisms $R \to N$, one per summand. A homomorphism $R \to N$ is in turn determined by where it sends $1 \in R$, since $f(r) = f(r \cdot 1) = r \cdot f(1)$, and *any* element of $N$ is a legal image of $1$. Hence $f : R^n \to N$ is exactly a free choice of $n$ elements $f(e_1), \dots, f(e_n) \in N$, with $f(a_1, \dots, a_n) = \sum_i a_i f(e_i)$. *Calibration check:* if you can reconstruct this, you have understood that maps out of a direct sum decouple summand by summand — and this corollary is precisely the [[Def - Free Module|free]] property of $R^n$.

**Corollary (projections split the inclusions).** For each $j$, $\pi_j \circ \iota_j = \mathrm{id}_{M_j}$, so $\iota_j$ is a *split* injection and $\pi_j$ a *split* surjection. Consequently $\ker \pi_j = \bigoplus_{i \neq j} \bar M_i$ and the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]] gives $\bigl(\bigoplus_i M_i\bigr) / \ker \pi_j \cong M_j$ — quotienting a direct sum by all-but-one summand returns the remaining one. *Calibration check:* this is the module-theoretic shadow of "the summands are independent", and verifying it tests that you have the inclusions and projections straight.

**Corollary (additivity of rank for free modules).** Since $R^m \oplus R^n$ is the module of $(m+n)$-tuples of ring elements with componentwise operations, $R^m \oplus R^n \cong R^{m+n}$. Thus the direct sum of free modules is free, and — once [[Thm - Invariance of Rank|invariance of rank]] is in hand — rank adds: $\operatorname{rank}(F \oplus G) = \operatorname{rank} F + \operatorname{rank} G$. *Calibration check:* writing down the isomorphism $R^m \oplus R^n \to R^{m+n}$ explicitly confirms that you can manipulate the componentwise operations.

---

# Unlocked by This

> [!tip] Free Module *(from Modules I — §3.2)*
> A direct sum of copies of the ring $R$ is the free module $R^{(S)}$, and its universal property — a map out is a free choice of image for each basis element — is exactly the maps-out universal property of the direct sum, specialised to summands all equal to $R$. See [[Def - Free Module]].

> [!tip] Structure Theorem for Modules over a PID *(from Modules II)*
> Once the direct sum is in hand, the structure theorem reads: every finitely generated module over a principal ideal domain $R$ is a direct sum $R^r \oplus R/(d_1) \oplus \cdots \oplus R/(d_t)$ of a free part and cyclic torsion pieces. Read at $R = \mathbb{Z}$ this is the classification of finitely generated abelian groups; read at $R = k[x]$ it yields the rational and Jordan canonical forms.
