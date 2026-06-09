---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ideal"
  - "Def - Quotient Ring"
  - "Def - Prime and Maximal Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Integral Domain"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring and $\mathfrak{q} \subsetneq R$ a proper [[Def - Ideal|ideal]]. We write $R/\mathfrak{q}$ for the [[Def - Quotient Ring|quotient ring]], $\bar x = x + \mathfrak{q}$ for the image of $x \in R$, and $\sqrt{\mathfrak{q}} = \{r \in R : r^n \in \mathfrak{q} \text{ for some } n \geq 1\}$ for the [[Def - Radical of an Ideal and the Nilradical|radical]] of $\mathfrak{q}$. An element $\bar x \in R/\mathfrak{q}$ is a **zero-divisor** if $\bar x \neq 0$ and $\bar x \bar y = 0$ for some $\bar y \neq 0$, and **nilpotent** if $\bar x^n = 0$ for some $n \geq 1$. A prime ideal is denoted $\mathfrak{p}$, a maximal ideal $\mathfrak{m}$. The full symbol registry is on [[Commutative Algebra IX — Primary Decomposition]].

This page also recalls, for contrast, the parallel notions of **prime** and **radical** ideal, so that "primary" can be located precisely between them: an ideal is prime exactly when it is both radical and primary.

---

# Axiom Motivation

The goal is to find the **right generalisation of a prime power**. We want to factor an arbitrary ideal the way we factor an integer, $90 = 2 \cdot 3^2 \cdot 5$, into pieces that play the role of the prime powers $2, 3^2, 5$. The prime ideals are too rigid to be the pieces — $(3^2)$ is not prime — so we need a notion that is to "prime" what "prime power" is to "prime number": slightly looser, allowing a controlled amount of repetition, but still attached to a single prime. The notion that does this is *primary*, and the way to invent it is to ask: what is the weakest relaxation of "prime" that still forces the radical to be prime?

Start from the quotient characterisation of a prime ideal, which is the cleanest place to mutate the definition. Recall that $\mathfrak{p}$ is [[Thm - Maximal and Prime Ideals via Quotients|prime exactly when $R/\mathfrak{p}$ is an integral domain]] — a nonzero ring whose *only zero-divisor is $0$*. And $I$ is radical exactly when $R/I$ is **reduced** — a ring whose *only nilpotent is $0$*. These two conditions on a quotient ring are independent, and a ring is a domain precisely when it is *both* reduced and has no nonzero zero-divisors at all. The natural intermediate creature sits between them: a ring in which zero-divisors are allowed to exist, but only if they are *infinitesimally small*, i.e. nilpotent. An ideal whose quotient is such a ring is what we call primary.

**Why "every zero-divisor is nilpotent" and not something weaker or stronger.** The defining demand on $R/\mathfrak{q}$ is: *every zero-divisor is nilpotent*. Consider what each nearby choice would do. If we demanded the *stronger* "no nonzero zero-divisors", we would be back at prime ideals and would lose $(3^2)$, $(9)$, and every genuine prime power — the very objects we are trying to capture. If we demanded the *weaker* "the ring is nonzero" with no condition on zero-divisors, we would admit ideals like $(6) \subseteq \mathbb{Z}$, whose quotient $\mathbb{Z}/6$ has zero-divisors $\bar 2, \bar 3$ that are *not* nilpotent ($\bar 2^n = \bar 2$ or $\bar 4$ forever) — and then the radical $\sqrt{(6)} = (6)$ would not be prime, and the whole "attached to a single prime" structure would collapse. The condition "every zero-divisor is nilpotent" is exactly the dividing line: it is the weakest condition that still forces $\sqrt{\mathfrak{q}}$ to be prime. Here is the forcing argument, which is the real motivation for the definition. Suppose $xy \in \sqrt{\mathfrak{q}}$, so $(xy)^n = x^n y^n \in \mathfrak{q}$, and suppose $x \notin \sqrt{\mathfrak{q}}$. In $R/\mathfrak{q}$, $\overline{x^n}$ is not nilpotent (else $x \in \sqrt{\mathfrak{q}}$) but $\overline{x^n}\,\overline{y^n} = 0$; if $\overline{y^n} \neq 0$ then $\overline{x^n}$ would be a zero-divisor that is not nilpotent — forbidden. So $\overline{y^n} = 0$, i.e. $y \in \sqrt{\mathfrak{q}}$. That is exactly "$\sqrt{\mathfrak{q}}$ is prime". The definition is reverse-engineered from this one requirement.

**Why this is genuinely between prime and radical, and incomparable with "prime power".** The clean summary is the trichotomy in the [[Thm - Maximal and Prime Ideals via Quotients|quotient]] language: $R/I$ is a domain (prime) $\Leftrightarrow$ it is reduced *and* primary; reduced (radical) means only-nilpotent-is-zero; primary means every-zero-divisor-is-nilpotent. So **prime $=$ radical $\cap$ primary**, and dropping either half lands on a strictly larger class. Dropping "reduced" gives the primary ideals that are not radical, such as $(9) \subseteq \mathbb{Z}$ (its quotient $\mathbb{Z}/9$ has the nilpotent $\bar 3$, and every zero-divisor *is* a multiple of $\bar 3$, hence nilpotent). Dropping "primary" gives the radical ideals that are not prime, such as $(6)$. One might hope primary coincides with "power of a prime", since that holds in $\mathbb{Z}$ — but this is false in both directions, and the failure is instructive: $(X, Y^2) \subseteq k[X,Y]$ is primary but not a prime power (it is strictly between $(X,Y)^2$ and $(X,Y)$), while $(\bar X, \bar Z)^2 \subseteq k[X,Y,Z]/(XY - Z^2)$ is a prime power that is *not* primary (the cone's singularity injects a second, non-nilpotent zero-divisor). The lesson is that "primary" is the correct primitive notion and "prime power" is an accident of low dimension.

**Why the radical of a primary ideal deserves a name.** Once $\sqrt{\mathfrak{q}}$ is forced to be prime, it is *the* prime attached to $\mathfrak{q}$ — indeed the *smallest* prime containing $\mathfrak{q}$, since the radical is always the intersection of the primes above an ideal and here that intersection is a single prime. We call $\mathfrak{q}$ **$\mathfrak{p}$-primary** with $\mathfrak{p} = \sqrt{\mathfrak{q}}$, and this $\mathfrak{p}$ is what makes primary ideals assemble into a factorisation: in a decomposition $I = \bigcap \mathfrak{q}_i$ the primes $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$ are the [[Def - Associated and Minimal Primes|associated primes]], the invariant skeleton of $I$. Without the radical being prime, there would be no skeleton, and no theory.

---

# The Definition

Let $R$ be a commutative ring and $\mathfrak{q} \subsetneq R$ a proper ideal.

## Primary ideal

$\mathfrak{q}$ is **primary** if $R/\mathfrak{q} \neq 0$ and every zero-divisor of $R/\mathfrak{q}$ is nilpotent. Equivalently, written directly in $R$:
$$xy \in \mathfrak{q} \quad\Longrightarrow\quad x \in \mathfrak{q} \ \text{ or }\ y^n \in \mathfrak{q} \text{ for some } n \geq 1, \qquad\text{i.e.}\qquad x \in \mathfrak{q} \ \text{ or }\ y \in \sqrt{\mathfrak{q}}.$$

## The attached prime

If $\mathfrak{q}$ is primary, then $\sqrt{\mathfrak{q}}$ is a prime ideal, and it is the smallest prime containing $\mathfrak{q}$. One says $\mathfrak{q}$ is **$\mathfrak{p}$-primary**, where $\mathfrak{p} = \sqrt{\mathfrak{q}}$.

## For comparison: prime and radical

The same quotient language defines the neighbouring notions. $\mathfrak{q}$ is **prime** if $R/\mathfrak{q} \neq 0$ and its only zero-divisor is $0$ (equivalently $R/\mathfrak{q}$ is an [[Def - Integral Domain|integral domain]]); $\mathfrak{q}$ is **radical** if its only nilpotent is $0$ (equivalently $R/\mathfrak{q}$ is reduced). Thus:
$$\mathfrak{q} \text{ prime} \iff \mathfrak{q} \text{ radical and primary}.$$

---

# Categorical / Structural Definition

The structural reading is through the **reduced quotient**. For any ideal $\mathfrak{q}$, the reduced ring associated to $R/\mathfrak{q}$ is $(R/\mathfrak{q})_{\mathrm{red}} = (R/\mathfrak{q})/\operatorname{nil}(R/\mathfrak{q}) = R/\sqrt{\mathfrak{q}}$. Primariness says precisely that **the canonical surjection $R/\mathfrak{q} \twoheadrightarrow R/\sqrt{\mathfrak{q}}$ has the property that the source has no zero-divisors outside its nilradical** — equivalently, that $R/\sqrt{\mathfrak{q}}$ is a domain (so $\sqrt{\mathfrak{q}}$ is prime) *and* the kernel $\sqrt{\mathfrak{q}}/\mathfrak{q}$ consists of nilpotents through which every zero-divisor of $R/\mathfrak{q}$ factors. In the language of schemes this is the statement that $\operatorname{Spec}(R/\mathfrak{q})$ is an **irreducible scheme with a single generic point** $\mathfrak{p} = \sqrt{\mathfrak{q}}$, possibly non-reduced: a primary ideal is the algebraic incarnation of an irreducible (one-component) closed subscheme, where the non-reducedness records multiplicity. This is exactly why primary ideals are the right "pieces" — each one is geometrically a single irreducible component, thickened.

---

# Relate to Other Fields / Compression

The cleanest compression: **a $\mathfrak{p}$-primary ideal is a prime $\mathfrak{p}$ with a controlled, single-direction nilpotent thickening — its reduced quotient is the domain $R/\mathfrak{p}$, and everything killed in passing from $R/\mathfrak{q}$ to that domain is nilpotent.** Set the thickening to zero (demand $\mathfrak{q}$ radical) and you recover a prime ideal exactly.

**True name:** the true name of "$\mathfrak{q}$ is primary" is *not* the bare "every zero-divisor of $R/\mathfrak{q}$ is nilpotent" but the operational **"$R/\mathfrak{q}$ is a single prime $\mathfrak{p} = \sqrt{\mathfrak{q}}$ thickened by nilpotents"** — i.e. its reduced quotient $R/\sqrt{\mathfrak{q}}$ is a domain, and the rest is nilpotent. This is the form you actually use: to test primariness, compute the reduced quotient and check it is a domain, then check that the part you removed is nilpotent. The shortcut "radical maximal $\Rightarrow$ primary" is the most common instance, because then $R/\mathfrak{q}$ is a local ring with nilpotent maximal ideal — a single closed point thickened.

The construction is the algebraic analogue of a **multiplicity-bearing point or component** in geometry: where a variety records only the set $V(\mathfrak{p})$, a primary ideal records that set *together with* how many times it is counted. In intersection theory the primary components are exactly what carry the intersection multiplicities (Bézout's theorem counts points with the multiplicities encoded in the primary decomposition of the intersection ideal). In number theory, $(p^n) \subseteq \mathbb{Z}$ is the prototypical primary ideal: a single prime $p$ taken to multiplicity $n$.

---

# Examples / Corollaries

**Is an instance — prime powers in $\mathbb{Z}$.** In $R = \mathbb{Z}$, the ideal $(p^n)$ for $p$ prime is $(p)$-primary: $\mathbb{Z}/p^n$ has $\bar p$ as its only "direction" of zero-divisors, and $\bar a$ is a zero-divisor iff $p \mid a$ iff $\bar a$ is nilpotent (as $\bar a^n$ has $p^n \mid a^n$). The radical is $\sqrt{(p^n)} = (p)$, prime. In fact the primary ideals of $\mathbb{Z}$ are *exactly* $(0)$ and the prime powers $(p^n)$, which is why $\mathbb{Z}$ misleads one into "primary $=$ prime power".

**Is an instance — a primary ideal that is not a prime power.** $\mathfrak{q} = (X, Y^2) \subseteq k[X,Y]$ is $(X,Y)$-primary. Compute $R/\mathfrak{q} \cong k[Y]/(Y^2)$: every element is $a + b\bar Y$ with $a, b \in k$, the zero-divisors are exactly the multiples of $\bar Y$, and each is nilpotent ($(b\bar Y)^2 = 0$). The radical is $\sqrt{(X,Y^2)} = (X,Y)$, a maximal ideal. Yet $\mathfrak{q}$ is not a power of any prime: the only candidate is $(X,Y)$, but $(X,Y)^2 = (X^2, XY, Y^2) \subsetneq \mathfrak{q} \subsetneq (X,Y)$, so $\mathfrak{q}$ falls strictly between consecutive powers.

**Is an instance — every power of a maximal ideal.** If $\mathfrak{m}$ is maximal then each $\mathfrak{m}^n$ is $\mathfrak{m}$-primary, because $\sqrt{\mathfrak{m}^n} = \mathfrak{m}$ is maximal, and a maximal radical forces primariness (in $R/\mathfrak{m}^n$ the maximal ideal $\mathfrak{m}/\mathfrak{m}^n$ is nilpotent, so every non-unit is nilpotent, hence every zero-divisor is). See [[Ex - Powers of a maximal ideal are primary]].

**Is NOT an instance — a radical ideal that is not primary.** $(6) \subseteq \mathbb{Z}$ has $\mathbb{Z}/6 \cong \mathbb{Z}/2 \times \mathbb{Z}/3$, with zero-divisors $\bar 2, \bar 3, \bar 4$ that are *not* nilpotent. So $(6)$ is radical (it is $\sqrt{(6)}$) but not primary; indeed $2 \cdot 3 = 6 \in (6)$ with $2 \notin (6)$ and $3 \notin \sqrt{(6)} = (6)$. This is the canonical "radical but not primary" ideal.

**Is NOT an instance — a prime power that is not primary.** Let $R = k[X,Y,Z]/(XY - Z^2)$ (the affine cone over a conic) and $\mathfrak{p} = (\bar X, \bar Z)$, which is prime since $R/\mathfrak{p} \cong k[Y]$ is a domain. Then $\mathfrak{p}^2 = (\bar X^2, \bar X \bar Z, \bar Z^2)$ is **not** primary: $\bar X \bar Y = \bar Z^2 \in \mathfrak{p}^2$, but $\bar X \notin \mathfrak{p}^2$ and $\bar Y \notin \sqrt{\mathfrak{p}^2} = \mathfrak{p}$ (since $\bar Y$ does not vanish in $R/\mathfrak{p} \cong k[Y]$). So $\bar Y$ is a non-nilpotent zero-divisor of $R/\mathfrak{p}^2$. See [[Ex - A primary ideal need not be a prime power]].

**Calibration check.** Verify that $(9)$ is $(3)$-primary in $\mathbb{Z}$ by computing the zero-divisors of $\mathbb{Z}/9$ and checking each is nilpotent, and confirm $\sqrt{(9)} = (3)$. Confirm directly from the definition that *every* prime ideal is primary (the only zero-divisor of a domain is $0$, which is nilpotent), so "primary" really does contain "prime". Finally, check that for a primary $\mathfrak{q}$, if $xy \in \mathfrak{q}$ and neither $x$ nor $y$ lies in $\mathfrak{q}$, then *both* $x$ and $y$ lie in $\sqrt{\mathfrak{q}}$ — primariness only forces *one* of them into $\mathfrak{q}$, but pushes the other into the radical.

---

# Unlocked by This

> [!tip] Irreducible (one-component) closed subschemes *(from Algebraic Geometry)*
> A $\mathfrak{p}$-primary ideal is the algebra of an **irreducible closed subscheme with a single generic point**, possibly non-reduced. $\operatorname{Spec}(R/\mathfrak{q})$ has one irreducible component (the generic point is $\mathfrak{p} = \sqrt{\mathfrak{q}}$), and the nilpotents in $R/\mathfrak{q}$ record the multiplicity with which that component is taken. This is why primary ideals are the indecomposable pieces of a primary decomposition: each is a single thickened component, and decomposing an ideal into primaries is decomposing a scheme into its components-with-multiplicity.

> [!tip] Symbolic powers and the multiplicity of a component *(from Commutative Algebra / Intersection Theory)*
> For a prime $\mathfrak{p}$, the **$n$-th symbolic power** $\mathfrak{p}^{(n)}$ is defined as the $\mathfrak{p}$-primary component of $\mathfrak{p}^n$ — the smallest $\mathfrak{p}$-primary ideal containing $\mathfrak{p}^n$. The need for symbolic powers is exactly the phenomenon on this page: $\mathfrak{p}^n$ may fail to be primary (the cone example), so one must extract its $\mathfrak{p}$-primary part. Symbolic powers control the multiplicity of a component and are central to the theory of intersection multiplicities and to questions like the containment problem $\mathfrak{p}^{(n)} \subseteq \mathfrak{p}^m$.
