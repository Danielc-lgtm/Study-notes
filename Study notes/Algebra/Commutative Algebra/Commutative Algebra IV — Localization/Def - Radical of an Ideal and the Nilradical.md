---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Quotient Ring"
  - "Def - Multiplicative Set and Localization"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. For an [[Def - Ideal|ideal]] $I \trianglelefteq R$, its **radical** is $\sqrt{I} = \{r \in R : r^n \in I \text{ for some } n \geq 1\}$. The **nilradical** is $\operatorname{nil} R := \sqrt{(0)} = \{r \in R : r^n = 0 \text{ for some } n \geq 1\}$, the set of **nilpotent** elements. An ideal $I$ is **radical** if $\sqrt{I} = I$, and a ring $R$ is **reduced** if $\operatorname{nil} R = (0)$. We write $\mathfrak{p}, \mathfrak{q}$ for [[Def - Prime and Maximal Ideal|primes]] and $R_f$ for the localization inverting $\{f^n\}$. The full registry is on [[Commutative Algebra IV — Localization]].

This is a compound page: it defines four interlocking notions — the **radical** $\sqrt{I}$, the **nilradical** $\operatorname{nil} R$ (the radical of the zero ideal), a **radical ideal**, and a **reduced ring** — because they are one construction applied at different ideals, and each is the test object for the next: $\operatorname{nil} R$ is $\sqrt{(0)}$, a radical ideal is a fixed point of $\sqrt{\,\cdot\,}$, and "reduced" is "$(0)$ is radical".

---

# Axiom Motivation

The radical answers a question that geometry forces on you: **a polynomial and its square have exactly the same zero set, so when should algebra refuse to distinguish them?** If $f$ vanishes on a set, so does $f^2$, $f^3$, and conversely if $f^n$ vanishes at a point then $f$ does too. The radical $\sqrt{I}$ is the construction that makes the algebra match this geometric fact: it is the largest ideal with the same vanishing locus as $I$.

**Why "some power lands in $I$" is the right closure condition.** Begin with the geometry. The vanishing set of an ideal $I$ is $V(I) = \{\mathfrak{p} : I \subseteq \mathfrak{p}\}$, and a function $f$ "vanishes on $V(I)$" when $f \in \mathfrak{p}$ for every prime $\mathfrak{p} \supseteq I$. Now ask: which elements vanish on $V(I)$ but might not lie in $I$ itself? Exactly those $f$ such that some power $f^n$ lies in $I$ — because a prime $\mathfrak{p}$ contains $f^n$ iff it contains $f$ (primality), so $f^n \in I \subseteq \mathfrak{p}$ forces $f \in \mathfrak{p}$ for all $\mathfrak{p} \supseteq I$, i.e. $f$ vanishes on $V(I)$. This is the content of the [[Thm - The Radical is the Intersection of the Primes Above It|radical theorem]] $\sqrt{I} = \bigcap_{\mathfrak{p} \supseteq I}\mathfrak{p}$, but the *definition* $\sqrt{I} = \{r : r^n \in I\}$ is engineered to capture exactly this set without yet invoking primes. The condition "$r^n \in I$ for some $n$" is the algebraic translation of "vanishes wherever $I$ does", and it is the minimal such translation.

**Why $\sqrt{I}$ is an ideal at all — the binomial trick.** It is not obvious that the radical is closed under addition: if $x^n \in I$ and $y^m \in I$, why should $(x+y)^k \in I$ for some $k$? The answer is the binomial theorem with the exponent chosen large enough. Expand $(x+y)^{n+m-1} = \sum_k \binom{n+m-1}{k} x^k y^{n+m-1-k}$. In each term either $k \geq n$ (so $x^k$ is a multiple of $x^n \in I$) or $n+m-1-k \geq m$ (so $y^{n+m-1-k}$ is a multiple of $y^m \in I$) — because if both failed we would have $k \leq n-1$ and $n+m-1-k \leq m-1$, summing to $n+m-2 \geq n+m-1$, impossible. Every term lies in $I$, so the sum does, so $x+y \in \sqrt{I}$. Closure under multiplication by ring elements is immediate ($(rx)^n = r^n x^n \in I$). This binomial-exponent argument is the one genuinely non-trivial fact in the definition, and it is worth holding because it recurs (it is exactly why $\operatorname{nil} R$ is an ideal). Note also $I \subseteq \sqrt{I}$ always (take $n=1$), and $\sqrt{\sqrt{I}} = \sqrt{I}$ (radicals are idempotent).

**Why the nilradical is the special case that matters most.** Take $I = (0)$. Then $\sqrt{(0)} = \operatorname{nil} R$ is the set of *nilpotent* elements — those with $r^n = 0$. Geometrically these are the functions that vanish at *every* point of $\operatorname{Spec} R$ yet may be nonzero: they are invisible to the topology, the algebraic ghosts. A nonzero nilpotent is precisely a function whose value $r(\mathfrak{p}) = r \bmod \mathfrak{p}$ is $0$ in every residue field, even though $r \neq 0$. So $\operatorname{nil} R$ measures the failure of "a function is determined by its values". The condition $\operatorname{nil} R = (0)$ — the ring is **reduced** — says values *do* determine functions, which is exactly the condition under which $R$ is the ring of genuine functions on its spectrum, with no infinitesimal fuzz. Dropping reducedness is not a defect to avoid; non-reduced rings like $k[\varepsilon]/(\varepsilon^2)$ are how algebra records tangent directions and multiplicities, and the nilradical is the tool that isolates that extra data.

**Why "radical ideal" is the right notion of a fixed point.** An ideal is **radical** when $\sqrt{I} = I$, i.e. when it already contains every element whose power it contains. The slogan is that radical ideals are exactly the ideals expressible as an intersection of primes — the ideals that "come from geometry", in the sense that $I = I(V(I))$, the full ideal of functions vanishing on the variety $V(I)$. Equivalently, $I$ is radical iff the quotient $R/I$ is reduced (no nonzero nilpotents): a nilpotent in $R/I$ is an element $r$ with $r^n \in I$ but $r \notin I$, so "$R/I$ reduced" is "$\sqrt{I} = I$". This makes "radical ideal" and "reduced quotient" two phrasings of one condition, and it is the link the [[Thm - The Radical is the Intersection of the Primes Above It|Nullstellensatz-in-embryo]] makes precise: radical ideals biject with closed subvarieties.

---

# The Definition

Let $R$ be a commutative ring and $I \trianglelefteq R$ an [[Def - Ideal|ideal]].

## Radical of an ideal

The **radical** of $I$ is
$$\sqrt{I} := \{r \in R : r^n \in I \text{ for some } n \geq 1\}.$$
It is an ideal of $R$ containing $I$, satisfies $\sqrt{\sqrt{I}} = \sqrt{I}$, and under the quotient map $\pi : R \to R/I$ one has $\sqrt{I}/I = \operatorname{nil}(R/I)$ — that is, $\sqrt{I} = \pi^{-1}(\operatorname{nil}(R/I))$. For nested ideals $J \subseteq I$, $\sqrt{I/J} = \sqrt{I}/J$ in $R/J$.

## Nilradical and nilpotent elements

An element $r \in R$ is **nilpotent** if $r^n = 0$ for some $n \geq 1$. The **nilradical** is the radical of the zero ideal:
$$\operatorname{nil} R := \sqrt{(0)} = \{r \in R : r^n = 0 \text{ for some } n \geq 1\},$$
an ideal of $R$ (the binomial argument shows it is closed under addition).

## Radical ideals

The ideal $I$ is **radical** if $\sqrt{I} = I$, equivalently if $r^n \in I \Rightarrow r \in I$, equivalently if $R/I$ is reduced. Every [[Def - Prime and Maximal Ideal|prime ideal]] is radical (and so is every intersection of primes).

## Reduced rings

A ring $R$ is **reduced** if $\operatorname{nil} R = (0)$ — its only nilpotent element is $0$. Equivalently, the zero ideal is radical. Quotients $R/\sqrt{I}$ are always reduced; in particular $R_{\mathrm{red}} := R/\operatorname{nil} R$ is the **reduction** of $R$, the universal reduced quotient.

## Key facts (proved on the theorem pages)

$$\sqrt{I} = \bigcap_{I \subseteq \mathfrak{p} \in \operatorname{Spec} R} \mathfrak{p}, \qquad\text{in particular}\qquad \operatorname{nil} R = \bigcap_{\mathfrak{p} \in \operatorname{Spec} R}\mathfrak{p}.$$
See [[Thm - The Radical is the Intersection of the Primes Above It]]. Under localization, $(\sqrt{I})^e = \sqrt{I^e}$ and $\operatorname{nil}(S^{-1}R) = S^{-1}(\operatorname{nil} R)$; and being reduced is a [[Def - Local Property (Localizable and Local-to-Global)|local property]].

---

# Categorical / Structural Definition

The radical is a **closure operator** on the lattice of ideals: $I \mapsto \sqrt{I}$ is increasing ($I \subseteq \sqrt{I}$), order-preserving, and idempotent ($\sqrt{\sqrt{I}} = \sqrt{I}$), with the radical ideals as its closed (fixed) points. Structurally, taking the radical corresponds under the [[Def - The Prime Spectrum (Spec)|spectrum]] to taking topological closure: $V(I) = V(\sqrt{I})$, and $\sqrt{I}$ is the *largest* ideal cutting out the closed set $V(I)$. The reduction functor $R \mapsto R_{\mathrm{red}} = R/\operatorname{nil} R$ is **left adjoint** to the inclusion of reduced rings into all rings: any map from $R$ to a reduced ring factors uniquely through $R_{\mathrm{red}}$, because a nilpotent must map to a nilpotent must map to $0$. This is the precise sense in which "reduced" is the property of "having no ghost functions": $R_{\mathrm{red}}$ is the universal best reduced approximation, and on spectra $\operatorname{Spec}(R_{\mathrm{red}}) \to \operatorname{Spec}(R)$ is a homeomorphism — killing nilpotents does not change the topology, only the structure sheaf.

---

# Relate to Other Fields / Compression

The cleanest compression: **$\sqrt{I}$ is the largest ideal with the same zero set as $I$; the nilradical is the functions that vanish everywhere yet may be nonzero; reduced means values determine functions.** The whole circle of ideas is the algebra of "a polynomial and its powers have the same roots".

**True name:** the true name of $\sqrt{I}$ is "**the intersection of the primes containing $I$**" — the geometric characterisation, $\sqrt{I} = \bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$. The power-condition definition is for computation; the prime-intersection form is what you reason with and what links radicals to varieties. Correspondingly, the true name of "$R$ is reduced" is "$R$ embeds in a product of domains / fields" — no ghost functions, every element detected at some point.

This is the algebraic core of the **Nullstellensatz**: for $R = k[X_1,\dots,X_n]$ with $k$ algebraically closed, Hilbert's theorem says the radical ideals are *exactly* the ideals of the form $I(W)$ for an algebraic set $W$, and $\sqrt{I} = I(V(I))$ — the radical is the operation $I \mapsto I(V(I))$ of "pass to the variety and take all functions vanishing on it". The full statement is developed in [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]]. In differential geometry the nilradical has no nonzero elements (rings of smooth functions are reduced), which is *why* schemes are richer than manifolds: algebra permits nilpotents and thereby records infinitesimal thickenings — the dual numbers $k[\varepsilon]/(\varepsilon^2)$ encode a tangent vector, and $k[\varepsilon]/(\varepsilon^{n+1})$ an $n$-jet.

---

# Examples / Corollaries

**Is an instance — $\sqrt{(12)}$ in $\mathbb{Z}$.** Since $12 = 2^2 \cdot 3$, an integer $r$ has a power divisible by $12$ iff $r$ is divisible by both $2$ and $3$, i.e. by $6$. So $\sqrt{(12)} = (6)$. In general $\sqrt{(n)} = (\operatorname{rad}(n))$, the ideal generated by the product of the distinct primes dividing $n$ — the radical of the *ideal* recovers the radical of the *integer*. Note $(6)$ is radical ($6$ is squarefree) while $(12)$ is not.

**Is an instance — the nilradical of $\mathbb{Z}/12$.** In $R = \mathbb{Z}/12$, an element $\bar{r}$ is nilpotent iff every prime $2, 3$ divides $r$, i.e. $6 \mid r$: $\operatorname{nil}(\mathbb{Z}/12) = \{\bar{0}, \bar{6}\} = (6)/(12)$, and indeed $6^2 = 36 \equiv 0$. The reduction is $(\mathbb{Z}/12)_{\mathrm{red}} = \mathbb{Z}/12 / (6) \cong \mathbb{Z}/6 \cong \mathbb{F}_2 \times \mathbb{F}_3$, a reduced ring.

**Is an instance — a radical ideal that is not prime.** In $k[X,Y]$, the ideal $(XY)$ is radical (it is the intersection $(X) \cap (Y)$ of two primes), so $\sqrt{(XY)} = (XY)$, yet it is not prime — $X \cdot Y \in (XY)$ with neither factor in it. This is the algebra of the *reducible* variety "union of the two axes": radical but not irreducible.

**Is NOT an instance — a non-radical ideal, the double line.** In $k[X,Y]$, the ideal $(X^2)$ is *not* radical: $X^2 \in (X^2)$ but $X \notin (X^2)$, so $X \in \sqrt{(X^2)} = (X)$ strictly larger. Geometrically $V((X^2)) = V((X))$ is the $Y$-axis, but $(X^2)$ remembers it as a *doubled* line — the quotient $k[X,Y]/(X^2)$ is non-reduced, carrying a nilpotent $\bar{X}$ that records the multiplicity. The radical $(X)$ forgets the doubling.

**Is NOT an instance — a non-reduced ring.** $R = k[\varepsilon]/(\varepsilon^2)$ has $\operatorname{nil} R = (\varepsilon) \neq (0)$, since $\varepsilon^2 = 0$ but $\varepsilon \neq 0$. So $R$ is not reduced; $\varepsilon$ is a ghost function, vanishing at the single point of $\operatorname{Spec} R$ yet nonzero. This is the dual-number ring, the algebraic tangent vector.

**Corollary — detecting nilpotence by collapse.** $f \in R$ is nilpotent $\iff 0 \in \{f^n\} \iff R_f = 0$. So a localization collapsing to the zero ring is a test for nilpotence: $f \in \operatorname{nil} R \iff R_f = 0 \iff D(f) = \varnothing$. This is the lever behind the $\supseteq$ direction of the radical theorem.

**Calibration check.** Verify $\operatorname{nil} R$ is closed under addition via the binomial-exponent argument (choose exponent $n+m-1$). Confirm $\sqrt{I} = I \iff R/I$ reduced by translating a nilpotent of $R/I$ back to an element with $r^n \in I$. Compute $\sqrt{(72)}$ in $\mathbb{Z}$ (answer $(6)$) and check $(\mathbb{Z}/8)_{\mathrm{red}} \cong \mathbb{F}_2$. Finally, confirm that every prime ideal is radical directly from primality.

---

# Unlocked by This

> [!tip] The Nullstellensatz dictionary: radical ideals are varieties *(from Algebraic Geometry)*
> Over an algebraically closed field $k$, Hilbert's **Nullstellensatz** makes $I \mapsto V(I)$ and $W \mapsto I(W)$ a bijection between *radical ideals* of $k[X_1,\dots,X_n]$ and *algebraic subsets* of $k^n$, with $I(V(I)) = \sqrt{I}$. The radical is exactly the operation needed to make this a clean correspondence — without it, $(X^2)$ and $(X)$ would both name the line and the dictionary would not be injective. So the radical is the algebraic side of "a closed subvariety knows only the reduced functions on it". The full theory is [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

> [!tip] Non-reduced schemes, multiplicities, and tangent data *(from Algebraic Geometry)*
> Allowing nonzero nilpotents is precisely what makes **schemes** strictly more expressive than classical varieties. The scheme $\operatorname{Spec} k[X]/(X^2)$ is a single point carrying a nilpotent $\bar{X}$ — a "point with a tangent direction", the **fat point** or dual-number scheme used to define tangent spaces and deformations. A finite morphism's fibres carry multiplicities exactly as the non-reduced structure of $\operatorname{Spec}$ of the fibre ring; Bézout's theorem counts intersection points *with multiplicity* by reading the length of the non-reduced intersection scheme. The reduction $R_{\mathrm{red}}$ forgets all of this and returns the underlying classical variety.

> [!tip] Reducedness as a local property and the structure sheaf *(from Algebraic Geometry)*
> That "reduced" is a [[Def - Local Property (Localizable and Local-to-Global)|local property]] (a ring is reduced iff every localization $R_{\mathfrak{p}}$ is reduced) means a scheme is reduced iff all its stalks are — the nilradical is computed point by point. This is the prototype for how properties of schemes are checked locally on the structure sheaf, and it is proved purely algebraically in [[Ex - Being reduced is a local property]] from the [[Thm - The Local-Global Principle|local–global principle]].
