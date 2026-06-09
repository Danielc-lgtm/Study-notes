---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Module"
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Field of Fractions"
  - "Def - Integral Domain"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring and $M$ an [[Def - Module|$R$-module]]. We write $S \subseteq R$ for a multiplicative subset, $S^{-1}R$ for the localized ring, $S^{-1}M$ for the localized module, and $\tfrac{r}{s}$, $\tfrac{m}{s}$ for the fractions ($r \in R$, $m \in M$, $s \in S$). The localization map is $\iota : R \to S^{-1}R$, $r \mapsto \tfrac{r}{1}$. Two recurring special cases: $R_f := S^{-1}R$ with $S = \{1, f, f^2, \dots\}$, and $R_{\mathfrak p} := (R\setminus\mathfrak p)^{-1}R$ for a [[Def - Prime and Maximal Ideal|prime ideal]] $\mathfrak p$. The full registry is on [[Commutative Algebra IV — Localization]].

This is a compound page: it defines three interlocking notions — the **multiplicative subset** $S$, the **localized module** $S^{-1}M$, and the **localized ring** $S^{-1}R$ — because they are introduced together and none is fully usable without the others. ($S^{-1}R$ is the special case $M = R$ equipped, in addition, with a multiplication; and $S^{-1}M$ is a module not just over $R$ but over $S^{-1}R$.)

---

# Axiom Motivation

The goal is to **adjoin inverses**. We have a ring $R$ and a chosen set of elements we wish were invertible, and we want the smallest, most economical ring in which they become units — while bending the original ring as little as possible. The model is already in your hands: from [[Def - Integral Domain|the integers]] one builds [[Def - Field of Fractions|the rationals]] by inverting every non-zero element, with $\tfrac ab$ a formal symbol and $\tfrac ab = \tfrac cd \iff ad = bc$. Everything on this page is that construction, asked to survive two generalisations: we will not invert everything (only a chosen set $S$), and we will not assume $R$ has no zero-divisors. Watching what each generalisation forces is the way to *invent* the definition rather than memorise it.

**Why $S$ must be multiplicatively closed and contain $1$.** Suppose we want elements of some set $U$ to become units. In *any* ring, the units are closed under multiplication ($u, v$ invertible $\Rightarrow uv$ invertible, inverse $v^{-1}u^{-1}$) and contain $1$. So the moment we force the elements of $U$ to be units, we have forced everything in the multiplicative closure of $U \cup \{1\}$ to be a unit as well — there is no extra cost and no choice. We may therefore assume from the start that our set of denominators is a **multiplicative subset**: $1 \in S$ and $ab \in S$ whenever $a, b \in S$. This is not a restriction but a normalisation: working with $S$ rather than an arbitrary $U$ loses no generality, because the universal ring that inverts $U$ is the same as the one that inverts the multiplicative closure of $U$. Drop "$1 \in S$" and the fraction $\tfrac11$ — the would-be identity — has no meaning; drop "closed under products" and $\tfrac{r}{s_1}\cdot\tfrac{r'}{s_2} = \tfrac{rr'}{s_1 s_2}$ produces a denominator $s_1 s_2$ that may not be allowed, so the set of fractions is not closed under multiplication. Both axioms are exactly what it takes for "fractions with denominators in $S$" to be a self-contained algebraic system.

**Why fractions, and why this equivalence relation.** Having fixed $S$, the elements of the new ring should be formal fractions $\tfrac ms$. When are two equal? In $\mathbb Q$ the answer is "$\tfrac{m_1}{s_1} = \tfrac{m_2}{s_2} \iff s_2 m_1 = s_1 m_2$": cross-multiply. Try this naive relation in general and it *fails to be transitive* unless we can cancel, and cancellation is exactly what zero-divisors forbid. The fix is dictated by the goal itself. The whole point of $S^{-1}R$ is that each $s \in S$ becomes invertible; but in any module, **multiplying by an invertible element is injective** — if $s$ is a unit and $sm = 0$ then $m = s^{-1}sm = 0$. So if our construction is to make $s$ a unit, it *must* already treat "$sm = 0$" as "$m = 0$": any element annihilated by some $s \in S$ has to die. That is the missing ingredient. Declare
$$\tfrac{m_1}{s_1} = \tfrac{m_2}{s_2} \quad\Longleftrightarrow\quad u\,(s_2 m_1 - s_1 m_2) = 0 \ \text{ for some } u \in S.$$
The clearing factor $u$ is precisely "kill the difference using something we are about to invert anyway". With it, transitivity goes through (the proof multiplies the two relations by suitable elements of $S$ and uses that $S$ is closed under products), and one checks the relation is reflexive and symmetric trivially. When $R$ is a domain and $0 \notin S$, no element of $S$ is a zero-divisor, so $u$ can be cancelled and the relation collapses to plain cross-multiplication — recovering $\mathbb Q$. The clearing factor is the *only* new idea beyond the field-of-fractions construction, and it is forced, not invented.

**Why $S^{-1}M$ is a module and $S^{-1}R$ is a ring.** Addition $\tfrac{m_1}{s_1} + \tfrac{m_2}{s_2} = \tfrac{s_2 m_1 + s_1 m_2}{s_1 s_2}$ is the only formula compatible with "clear to a common denominator", and one verifies it respects the equivalence relation (this is where closure of $S$ and the clearing factor pay off). Scalar multiplication $r \cdot \tfrac ms = \tfrac{rm}{s}$ makes $S^{-1}M$ an $R$-module; taking $M = R$ and adding the multiplication $\tfrac{r_1}{s_1}\cdot\tfrac{r_2}{s_2} = \tfrac{r_1 r_2}{s_1 s_2}$ makes $S^{-1}R$ a ring with identity $\tfrac11$. Crucially $S^{-1}M$ is a module not merely over $R$ but over $S^{-1}R$, via $\tfrac rs \cdot \tfrac mt = \tfrac{rm}{st}$: once the denominators are invertible in the scalar ring, they are invertible in their action on the module too. The structural payoff to keep in view is that **$S^{-1}R$ is the universal ring in which $S$ becomes invertible** — the fractions are one model of it, and its real identity is the [[Thm - Universal Property of Localization|universal property]] proved separately.

**What the localization map records, and why it can fail to be injective.** The canonical map $\iota : R \to S^{-1}R$, $r \mapsto \tfrac r1$, is the bridge back to the original ring. Reading off the equivalence relation at $\tfrac r1 = \tfrac 01$ gives $\ker\iota = \{r \in R : ur = 0 \text{ for some } u \in S\}$. So $\iota$ is injective exactly when $S$ contains no zero-divisor — automatic for a domain with $0 \notin S$, which is why the field-of-fractions case hides this subtlety. And $S^{-1}R$ is the zero ring exactly when $0 \in S$, because then $\tfrac11 = \tfrac01$. These are not pathologies to avoid but features to use: $R_f = 0 \iff f$ is nilpotent is later turned into a *tool* for detecting nilpotence.

---

# The Definition

Let $R$ be a commutative ring and $M$ an $R$-module.

## Multiplicative subset

A **multiplicative subset** of $R$ is a subset $S \subseteq R$ such that $1 \in S$ and $ab \in S$ whenever $a, b \in S$. The **multiplicative closure** of a subset $U \subseteq R$ is the smallest multiplicative subset containing $U$, namely the set of all finite products $s_1 \cdots s_n$ ($n \geq 0$, the empty product being $1$) with each $s_i \in U$.

## Localization of a module

On the set of pairs $\{(m, s) : m \in M,\ s \in S\}$ define
$$(m_1, s_1) \sim (m_2, s_2) \quad\Longleftrightarrow\quad \exists\, u \in S \text{ with } u(s_2 m_1 - s_1 m_2) = 0.$$
This is an equivalence relation. Write $\tfrac ms$ for the class of $(m, s)$ and $S^{-1}M = \{\tfrac ms : m \in M, s \in S\}$. It is an abelian group under
$$\tfrac{m_1}{s_1} + \tfrac{m_2}{s_2} = \tfrac{s_2 m_1 + s_1 m_2}{s_1 s_2}, \qquad 0_{S^{-1}M} = \tfrac01,$$
and an $R$-module under $r\cdot\tfrac ms = \tfrac{rm}{s}$.

## Localization of a ring

Taking $M = R$, the set $S^{-1}R$ becomes a commutative ring under the same addition and the multiplication
$$\tfrac{r_1}{s_1}\cdot\tfrac{r_2}{s_2} = \tfrac{r_1 r_2}{s_1 s_2}, \qquad 1_{S^{-1}R} = \tfrac11.$$
For a general module $M$, the localization $S^{-1}M$ is moreover an **$S^{-1}R$-module** via $\tfrac rs\cdot\tfrac mt = \tfrac{rm}{st}$.

## The localization map

The map $\iota = \iota_{S^{-1}R} : R \to S^{-1}R$, $\iota(r) = \tfrac r1$, is a ring homomorphism sending every $s \in S$ to a unit (with inverse $\tfrac1s$). It satisfies:
$$\tfrac rs = 0 \iff ur = 0 \text{ for some } u \in S; \qquad \ker\iota = \{r : ur = 0,\ \exists u \in S\}; \qquad S^{-1}R = 0 \iff 0 \in S.$$

**Two standard cases.** For $f \in R$, $R_f := S^{-1}R$ with $S = \{f^n : n \geq 0\}$ ("invert $f$"). For a prime $\mathfrak p$, $R_{\mathfrak p} := (R\setminus\mathfrak p)^{-1}R$ ("localize at $\mathfrak p$"); here $S = R\setminus\mathfrak p$ is multiplicative precisely because $\mathfrak p$ is prime.

---

# Categorical / Structural Definition

The fractions are one *model*; the object's real definition is by a universal property. $S^{-1}R$ is the universal ring under $R$ in which $S$ becomes invertible: the localization map $\iota : R \to S^{-1}R$ inverts $S$, and any ring homomorphism $f : R \to B$ with $f(S) \subseteq B^\times$ factors uniquely as $f = h\circ\iota$. In the language of [[Def - Ring Homomorphism|category theory]], localization is the **left adjoint** to the inclusion of the full subcategory of $R$-algebras in which the elements of $S$ act invertibly; equivalently $S^{-1}R$ *represents* the functor $B \mapsto \{f : R \to B : f(S) \subseteq B^\times\}$. For the module, $S^{-1}M \cong S^{-1}R \otimes_R M$, i.e. localization of modules is the [[Commutative Algebra II — Tensor Products|extension of scalars]] along $\iota$ — the cleanest structural description, from which exactness and flatness follow. The full statement and proof are on [[Thm - Universal Property of Localization]].

---

# Relate to Other Fields / Compression

The cleanest compression: **localization is the field-of-fractions construction with the denominators chosen and the domain hypothesis dropped, paid for by a single clearing factor $u$.** Set $S = R\setminus\{0\}$ for a domain $R$ and you recover $\operatorname{Frac}(R)$ exactly. Replace $R\setminus\{0\}$ by $R\setminus\mathfrak p$ and you get the local ring $R_{\mathfrak p}$; by $\{f^n\}$ and you get $R_f$.

**True name:** the true name of $S^{-1}R$ is *not* "the set of fractions $\tfrac rs$" but "**the universal ring in which the elements of $S$ become units**". This is the form you actually use: to build maps out of it, to identify it with a known ring, to prove constructions agree. The fraction model is for hands-on computation (kernels, ideal extensions); the universal property is for everything structural.

The construction is the algebraic analogue of forming **germs of functions** in analysis and topology: a fraction $\tfrac rs$ with $s$ invertible-near-$\mathfrak p$ is a function defined where $s \neq 0$, and the equivalence relation "$u(s_2 m_1 - s_1 m_2) = 0$ for some $u \in S$" is exactly "the two functions agree on a neighbourhood (after discarding the locus where $u$ vanishes)". Under this dictionary $S^{-1}R$ for $S = \{f^n\}$ is the ring of functions on the open set $f \neq 0$, and $R_{\mathfrak p}$ is the ring of germs at the point $\mathfrak p$.

---

# Examples / Corollaries

**Is an instance — $\mathbb Z_{(p)}$ and the dyadic rationals.** With $R = \mathbb Z$ and $\mathfrak p = (p)$, $S = \mathbb Z \setminus (p) = \{n : p \nmid n\}$, so $\mathbb Z_{(p)} = \{\tfrac ab : p \nmid b\} \subseteq \mathbb Q$ — the local ring of rationals with denominator prime to $p$. With $S = \{2^n\}$ instead, $\mathbb Z_2 \text{ (i.e. } R_2) = \{\tfrac a{2^n}\} = \mathbb Z[\tfrac12]$, the dyadic rationals. Both are honest subrings of $\mathbb Q$ because $\mathbb Z$ is a domain, so $\iota$ is injective.

**Is an instance — collapsing a product.** With $R = \mathbb C\times\mathbb C$ and $S = \mathbb C\times(\mathbb C\setminus\{0\})$, the map $(x,y)\mapsto y$ inverts $S$, and $S^{-1}R \cong \mathbb C$: every $\tfrac{(x,0)}{(a,b)} = 0$ because $(0,1)\in S$ annihilates $(x,0)$. Here $\iota$ is far from injective — the whole factor $\mathbb C\times\{0\}$ dies. This is $R_{\mathfrak p_1}$ for the prime $\mathfrak p_1 = \{0\}\times\mathbb C$, and it shows localizing at a prime of a non-domain can erase an entire component.

**Is NOT an instance (of the field-of-fractions relation) — a zero-divisor forces the clearing factor.** In $R = \mathbb Z/6$ with $S = \{1,2,4\}$, naive cross-multiplication would distinguish $\tfrac31$ from $\tfrac01$, but $2\cdot(3 - 0) = 6 = 0$, so $\tfrac31 = \tfrac01$ in $S^{-1}R$: the clearing factor $u = 2$ is essential, and indeed $S^{-1}R \cong \mathbb Z/3$. This is the example that justifies the $u$ in the definition; without it $\sim$ is not even transitive.

**Is NOT an instance — the zero ring.** If $0 \in S$ then $S^{-1}R = 0$, since $\tfrac11 = \tfrac01$ (take $u = 0$, or note $0$ already kills everything). In particular $R_f = 0 \iff 0 \in \{f^n\} \iff f$ is nilpotent. So $(\mathbb Z/4)_2 = 0$ because $2^2 = 0$. This non-example is the seed of a *tool*: collapse of a localization detects nilpotence.

**Corollary — units already in $R$ change nothing.** If every element of $S$ is already a unit of $R$, then $\iota$ is an isomorphism: there is nothing to adjoin. In particular $S^{-1}R = R$ when $S \subseteq R^\times$.

**Calibration check.** Verify directly that $\sim$ is transitive using the clearing factor (multiply $u(s_2 m_1 - s_1 m_2) = 0$ and $v(s_3 m_2 - s_2 m_3) = 0$ appropriately and add). Confirm $\tfrac r1 = \tfrac01 \iff ur = 0$ for some $u\in S$, and deduce both "$\iota$ injective $\iff$ $S$ has no zero-divisor" and "$R_f = 0 \iff f$ nilpotent". Finally check that for $R$ a domain and $S = R\setminus\{0\}$ the relation reduces to $s_2 m_1 = s_1 m_2$, recovering $\operatorname{Frac}(R)$.

---

# Unlocked by This

> [!tip] Basic open sets $D(f)$ and the structure sheaf *(from Algebraic Geometry)*
> The rings $R_f$ are the sections of the **structure sheaf** over the basic open sets $D(f) = \{\mathfrak p : f \notin \mathfrak p\}$ of $\operatorname{Spec} R$. That $R_f$ localizes further to $R_{fg}$ is exactly the restriction map of the sheaf, and gluing these rings is how an **affine scheme** is built. Inverting $f$ *is* restricting to the open set where $f$ is non-vanishing.

> [!tip] Stalks and germs *(from Algebraic Geometry / Sheaf Theory)*
> The local ring $R_{\mathfrak p}$ is the **stalk** of the structure sheaf at $\mathfrak p$ — the ring of germs of functions near the point. The clearing-factor equivalence relation is the germ relation "agree on a neighbourhood", making this chapter's algebra the literal model for stalks in sheaf theory.

> [!tip] Rings of fractions as a flat base change *(from Homological Algebra)*
> Because $S^{-1}M \cong S^{-1}R \otimes_R M$ and $S^{-1}R$ is **flat**, localization is an exact base change. This is the entry point to the local–global computation of $\operatorname{Tor}$ and $\operatorname{Ext}$, which are computed prime-by-prime exactly because localization commutes with them.
