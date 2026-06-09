---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Field of Fractions"
  - "Def - Integral Domain"
  - "Def - Local Ring and Residue Field"
  - "Def - Noetherian Ring"
  - "Def - Krull Dimension and Height"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $K$ be a field with multiplicative group $K^\times = K\setminus\{0\}$. A **discrete valuation** is a map $v : K^\times \to \mathbb{Z}$; we extend it by $v(0) = \infty$, with the conventions $n + \infty = \infty$ and $\min\{n, \infty\} = n$. We write $A_v$ for its valuation ring, $\mathfrak{m}$ for the maximal ideal of a [[Def - Local Ring and Residue Field|local ring]], $k = A/\mathfrak{m}$ for the residue field, and $\pi$ for a **uniformizer** (an element with $v(\pi) = 1$). The leading example is the $p$-adic valuation $v_p$ on $\mathbb{Q}$ with valuation ring $\mathbb{Z}_{(p)}$. The full registry is on [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

This is a compound page: it defines three interlocking notions — the **discrete valuation** $v$, its **valuation ring** $A_v$, and the resulting class of **discrete valuation rings (DVRs)** — because they are introduced together and none is fully usable without the others. (The DVR is the valuation ring viewed abstractly, forgetting which $v$ produced it; part of the point is that $v$ is then recoverable from $A_v$ alone.)

---

# Axiom Motivation

The goal is to **measure divisibility by a single prime, abstractly**. Fix the integers and a prime $p$. Every nonzero rational number can be written $x = p^n \tfrac{a}{b}$ with $p \nmid a$ and $p \nmid b$, and the exponent $n$ — positive if $p$ divides the numerator, negative if it divides the denominator — is a complete record of "how $p$-divisible $x$ is". Call it $v_p(x)$. This single integer governs everything local to $p$: $x$ is a $p$-adic integer (no $p$ in the denominator) exactly when $v_p(x) \geq 0$, it is a $p$-adic unit exactly when $v_p(x) = 0$, and divisibility $x \mid y$ at $p$ is just $v_p(x) \leq v_p(y)$. The definition on this page is the distillation of this function into axioms, asked to make sense for an arbitrary field, so that "order of divisibility by one prime" becomes a structure we can impose anywhere — on number fields, on function fields, on the local ring of a curve.

**Why a surjective homomorphism to $\mathbb{Z}$.** We want $v$ to turn multiplication into addition, because divisibility is multiplicative: if $x$ is divisible by $p$ to order $m$ and $y$ to order $n$, then $xy$ is divisible to order $m+n$. So $v(xy) = v(x) + v(y)$ — $v$ is a group homomorphism from $(K^\times, \cdot)$ to $(\mathbb{Z}, +)$. Why land in $\mathbb{Z}$ rather than $\mathbb{Q}$ or $\mathbb{R}$? Because "discrete" is the whole content: we are counting copies of a single prime, and the count is an integer. Why *surjective*? Drop surjectivity and the image is a subgroup $d\mathbb{Z}$ of $\mathbb{Z}$; rescaling $v$ by $1/d$ recovers a surjective valuation with the same valuation ring, so surjectivity is a harmless normalization that pins down the uniformizer to have $v(\pi) = 1$ exactly. Without it, "the" uniformizer would be ambiguous and the bijection between ideals and integers (below) would skip values. The homomorphism axiom alone already forces $v(1) = 0$ (since $v(1) = v(1\cdot 1) = 2v(1)$) and then $v(-1) = 0$ (since $2v(-1) = v(1) = 0$), hence $v(-x) = v(x)$: signs are invisible to a valuation, as they must be, since $\pm$ does not change divisibility.

**Why the ultrametric inequality $v(x+y) \geq \min\{v(x), v(y)\}$.** Multiplication is easy; the subtlety is *addition*. If $p^m \mid x$ and $p^n \mid y$ with $m \leq n$, then $p^m$ divides both, hence divides $x + y$ — so $v(x+y) \geq m = \min\{v(x), v(y)\}$. This is the exact analogue of the triangle inequality, but *stronger*: instead of $v(x+y) \geq$ some combination, the valuation of a sum is at least the *smaller* of the two, never mind the larger. This "ultrametric" or "non-Archimedean" strength is what makes valuation theory rigid and combinatorial rather than analytic. Drop this axiom and the set $\{v \geq 0\}$ is no longer closed under addition — it would not be a ring, defeating the entire purpose. Note the inequality can be *strict*: $v_p(p + p) = v_p(2p) = 1 = \min$, but $v_p(p - p) = v_p(0) = \infty > 1$; in general one has equality whenever $v(x) \neq v(y)$ (the smaller term cannot be cancelled), and only the equal-valuation case can jump up. This "equality unless the valuations tie" phenomenon is one of the most-used facts in the subject.

**Why the valuation ring is the right object, and why it is a DVR.** Having $v$, the natural ring to extract is $A_v = \{x \in K : v(x) \geq 0\}$ — the elements that are "integral at the prime", with no negative powers of $\pi$ in them. The axioms make this a ring: closed under multiplication because $v(xy) = v(x) + v(y) \geq 0$, and under addition because of the ultrametric inequality. It is local: its non-units are exactly $\{v(x) > 0\} = \{v(x) \geq 1\}$, which is closed under addition and absorption, hence the unique maximal ideal $\mathfrak{m}$. And its entire ideal structure is dictated by $v$: every nonzero ideal is $(\pi^n) = \{v \geq n\}$ for exactly one $n \geq 0$, so the ideals form the single descending chain $A \supsetneq (\pi) \supsetneq (\pi^2) \supsetneq \cdots$, making $A_v$ Noetherian, local, a domain, of dimension $1$. An integral domain that arises this way — as $A_v$ for some discrete valuation on its *own* fraction field — is what we name a **discrete valuation ring**. The deep payoff, established in the [[Thm - Characterization of Discrete Valuation Rings|characterization theorem]], is that this single chapter of structure is forced by far weaker-looking hypotheses (Noetherian, local, dimension $1$, integrally closed), so "DVR" turns out to be a robust, intrinsic notion and the valuation $v$ is recoverable from the ring alone — there was never any extra data.

---

# The Definition

Let $K$ be a field.

## Discrete valuation

A **discrete valuation** on $K$ is a surjective group homomorphism
$$v : K^\times \to \mathbb{Z}, \qquad v(xy) = v(x) + v(y),$$
satisfying the **ultrametric inequality**
$$v(x + y) \geq \min\{v(x), v(y)\} \quad \text{for all } x, y \in K^\times \text{ with } x + y \neq 0.$$
One extends $v$ to all of $K$ by setting $v(0) = \infty$. It follows that $v(1) = 0$, $v(-1) = 0$, and $v(-x) = v(x)$. When $v(x) \neq v(y)$ the inequality is an equality: $v(x+y) = \min\{v(x), v(y)\}$.

## Valuation ring

The **valuation ring** of $v$ is
$$A_v = \{x \in K : v(x) \geq 0\} \cup \{0\}.$$
It is a subring of $K$ (hence an integral domain) with $\operatorname{Frac}(A_v) = K$. Its group of units is $A_v^\times = \{x : v(x) = 0\}$, and its unique maximal ideal is $\mathfrak{m} = \{x : v(x) \geq 1\} \cup \{0\}$, so $A_v$ is a [[Def - Local Ring and Residue Field|local ring]] $(A_v, \mathfrak{m})$.

A **uniformizer** (or uniformizing parameter) is any $\pi \in A_v$ with $v(\pi) = 1$; equivalently any generator of $\mathfrak{m}$. For any uniformizer $\pi$, every nonzero $x \in K$ is uniquely $x = u\pi^n$ with $u \in A_v^\times$ and $n = v(x) \in \mathbb{Z}$, and the nonzero ideals of $A_v$ are exactly
$$A_v = (\pi^0) \supsetneq (\pi^1) \supsetneq (\pi^2) \supsetneq \cdots, \qquad (\pi^n) = \{x : v(x) \geq n\}.$$
Hence $\operatorname{Spec} A_v = \{(0), (\pi)\}$ and $\dim A_v = 1$.

## Discrete valuation ring

An integral domain $A$ is a **discrete valuation ring (DVR)** if $A = A_v$ for some discrete valuation $v$ on its fraction field $K = \operatorname{Frac}(A)$. The valuation is uniquely determined by $A$: $v(x) = n$ iff $(x) = \mathfrak{m}^n$ as ideals of $A$.

---

# Categorical / Structural Definition

The structural content is that a DVR is the same data as a *totally ordered, rank-one, discrete* way of comparing the sizes of elements. The map $A \setminus \{0\} \to \mathbb{Z}_{\geq 0}$, $x \mapsto v(x)$, makes the monoid of nonzero ideals of $A$ isomorphic to $(\mathbb{Z}_{\geq 0}, +)$ via $\mathfrak{m}^n \leftrightarrow n$, and the monoid of nonzero principal *fractional* ideals isomorphic to $(\mathbb{Z}, +)$ — so a DVR is precisely the local ring whose nonzero fractional ideals form the group $\mathbb{Z}$. Equivalently, in the language of [[Commutative Algebra V — Nakayama's Lemma|cotangent spaces]], a DVR is a **regular local ring of dimension one**: a Noetherian local ring whose maximal ideal can be generated by $\dim A = 1$ element. Both descriptions say the ideal theory is "one-dimensional and as simple as it can be", and the valuation is the resulting linear ruler. The full equivalence of these with the fraction-and-valuation definition is the content of [[Thm - Characterization of Discrete Valuation Rings]].

---

# Relate to Other Fields / Compression

The cleanest compression: **a discrete valuation is the $p$-adic order function $v_p$, abstracted away from $\mathbb{Z}$ to an arbitrary field, and a DVR is "$\mathbb{Z}_{(p)}$ in disguise".** Set $K = \mathbb{Q}$, $v = v_p$, and you recover $\mathbb{Z}_{(p)}$; set $K = k(T)$ and $v = v_f$ for an irreducible $f$, and you recover $k[T]_{(f)}$, the local ring of the affine line at the point $f = 0$.

**True name:** the true name of a DVR is *not* "the valuation ring of some $v$" but "**a local PID** — equivalently, a Noetherian local domain whose maximal ideal is principal". This is the form you actually use: to recognize one (find a single generator of $\mathfrak{m}$), to compute in one (everything is a unit times a power of $\pi$), and to spot one inside a Dedekind domain (localize and check integral-closedness). The valuation is then a *derived* gadget, the exponent of $\pi$, not the primary datum.

The valuation is the algebraic incarnation of **order of vanishing** in analysis and geometry: a meromorphic function on a Riemann surface has, at each point, an integer order — positive for a zero, negative for a pole — and this order is a discrete valuation on the field of meromorphic functions, whose valuation ring is the local ring of holomorphic germs at the point. The ultrametric inequality is the statement "a sum of functions vanishes at least to the order of the least-vanishing summand". Under this dictionary a uniformizer is a **local coordinate** $z - z_0$, and $v(f) = 3$ means $f$ has a triple zero.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}_{(p)}$ and the $p$-adic valuation.** With $K = \mathbb{Q}$ and $v = v_p$, the valuation ring is $\mathbb{Z}_{(p)} = \{\tfrac ab : p\nmid b\}$, a DVR with uniformizer $\pi = p$, units the fractions with $p$ in neither numerator nor denominator, and residue field $\mathbb{Z}_{(p)}/p\mathbb{Z}_{(p)} = \mathbb{F}_p$. Every nonzero rational is uniquely $p^n u$ with $u$ a unit. This is *the* model; see [[Ex - The valuation ring of the p-adic valuation]].

**Is an instance — the local ring of a curve.** With $K = k(T)$ and $f$ an irreducible polynomial, $v_f(g) = $ the multiplicity of $f$ in $g$ defines a discrete valuation whose ring is $k[T]_{(f)}$. For $f = T - a$ this is the ring of rational functions regular at $a$, with uniformizer $T - a$ and $v(g) = $ order of vanishing of $g$ at $a$. The field of formal Laurent series $k((T))$ with $v = $ order of the lowest term is another, with valuation ring $k[[T]]$.

**Is NOT an instance — a non-discrete valuation.** The order function on $K = \mathbb{C}((T^\mathbb{Q}))$ (Puiseux series) takes values in $\mathbb{Q}$, not $\mathbb{Z}$, so it is a valuation but not a *discrete* one; its valuation ring is local but not Noetherian and not a DVR (the maximal ideal is not principal — there is no smallest positive exponent). This shows "discrete" (image $\mathbb{Z}$) is essential, not cosmetic.

**Is NOT an instance — a PID that is not local.** The ring $\mathbb{Z}$ is a PID and a domain of dimension $1$, but it is *not* a DVR: it has infinitely many maximal ideals $(2), (3), (5), \dots$, so it is not local, and there is no single valuation measuring all primes at once. A DVR is what you get after localizing $\mathbb{Z}$ at *one* prime. Likewise $k[T]$ is a non-local PID, not a DVR.

**Is NOT an instance — a one-dimensional local domain that is singular.** The localized cusp ring $A = k[t^2, t^3]_{(t^2,t^3)}$ is a Noetherian local domain of dimension $1$, but its maximal ideal $\mathfrak{m} = (t^2, t^3)$ needs two generators ($\dim_k\mathfrak{m}/\mathfrak{m}^2 = 2$), so $\mathfrak{m}$ is not principal and $A$ is not a DVR. Equivalently $A$ is not integrally closed: $t = t^3/t^2 \in \operatorname{Frac}(A)$ is integral over $A$ but not in $A$. This is the example that shows the four hypotheses of the [[Thm - Characterization of Discrete Valuation Rings|characterization]] do not include integral-closedness for free.

**Corollary — the valuation is intrinsic.** Since $(x) = \mathfrak{m}^{v(x)}$, the integer $v(x)$ is read off the ideal $(x)$ alone, so two discrete valuations on the same field with the same valuation ring are equal. There is exactly one valuation per DVR.

**Calibration check.** From the axioms alone, derive $v(1) = 0$, $v(-1) = 0$, and $v(x^{-1}) = -v(x)$. Verify that $\{v \geq 0\}$ is closed under addition using the ultrametric inequality, and that $\{v \geq 1\}$ is an ideal. Confirm that in $\mathbb{Z}_{(p)}$ the units are exactly the elements of $v_p$-value $0$, and that $(p^n) = \{x : v_p(x) \geq n\}$. Finally, check that $v(x+y) = \min\{v(x),v(y)\}$ whenever $v(x) \neq v(y)$, and find an $x, y$ where the inequality is strict.

---

# Unlocked by This

> [!tip] The local ring of a smooth point and the order of vanishing *(from Algebraic Geometry)*
> A DVR is the local ring $\mathcal{O}_{C,p}$ of a **smooth point $p$ on an algebraic curve** $C$. The uniformizer $\pi$ is a **local coordinate**, and the valuation $v(f)$ is the **order of vanishing** of the regular function $f$ at $p$ — the integer with $f = (\text{unit})\cdot\pi^{v(f)}$. This is the basic local model from which the theory of **divisors** ($\sum_p v_p(f)[p]$ = zeros minus poles of $f$) on a curve is built. A point that is *not* smooth has a one-dimensional local ring that is *not* a DVR, and resolving the singularity is taking its integral closure.

> [!tip] The p-adic numbers and completion *(from Number Theory / Analysis)*
> Completing $\mathbb{Z}_{(p)}$ with respect to the metric $|x|_p = p^{-v_p(x)}$ produces the **$p$-adic integers** $\mathbb{Z}_p$, itself a DVR (now complete), and its fraction field $\mathbb{Q}_p$ the **$p$-adic numbers**. The ultrametric inequality is precisely what makes $|\cdot|_p$ a non-Archimedean absolute value. This is the entry point to local fields, Hensel's lemma, and the local–global methods of number theory; the completion is built from the same valuation defined here.

> [!tip] Valuation rings and birational geometry *(from Algebraic Geometry)*
> More general **valuation rings** (dropping "discrete") are the centerpiece of the valuative criteria for **separatedness and properness** of schemes, and DVRs specifically test these: a morphism is proper iff every DVR-valued point of the base extends uniquely. The DVR is the algebraic stand-in for "a small disk and its puncture", making it the right object to probe limits and specializations.
