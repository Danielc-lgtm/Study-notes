---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Noetherian Ring"
  - "Def - Integral Domain"
  - "Def - Integral Closure and Normal Domain"
  - "Def - Krull Dimension and Height"
  - "Def - Local Ring and Residue Field"
  - "Def - Discrete Valuation and Valuation Ring"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A$ be an integral domain with [[Def - Field of Fractions|fraction field]] $K = \operatorname{Frac}(A)$. We write $\dim A$ for the [[Def - Krull Dimension and Height|Krull dimension]], $\operatorname{ht}\mathfrak{p}$ for the height of a prime $\mathfrak{p}$, $A_\mathfrak{p} = (A\setminus\mathfrak{p})^{-1}A$ for the [[Def - Multiplicative Set and Localization|localization]] at $\mathfrak{p}$, and $\operatorname{mSpec} A$ for the set of maximal ideals. A domain is **[[Def - Integral Closure and Normal Domain|integrally closed]]** (or **normal**) if it equals its integral closure in $K$. The full registry is on [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

---

# Axiom Motivation

The goal is to **isolate the rings in which ideals factor uniquely into primes**, in order to repair the failure of unique factorization of *elements* that wrecks rings like $\mathbb{Z}[\sqrt{-5}]$. We know the property we want — unique factorization of ideals — and we are reverse-engineering the hypotheses that guarantee it. The historical route is instructive: Dedekind's predecessors observed that in $\mathbb{Z}[\sqrt{-5}]$ the equation $6 = 2\cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ exhibits two genuinely different factorizations into irreducibles, so the ring is not a UFD. The cure was to factor *ideals* instead, where $(2) = \mathfrak{p}^2$, $(3) = \mathfrak{q}\bar{\mathfrak{q}}$, and the ambiguity vanishes. A Dedekind domain is exactly the abstract setting where this cure always works, and the three defining axioms are precisely the minimal conditions that force it. We motivate each by asking what would break without it.

**Why dimension $1$.** Unique factorization of ideals is a statement about *prime* ideals as the building blocks, and it presupposes that the relevant primes are all "the same size" — the maximal ideals, sitting just above the zero ideal. In a one-dimensional domain the prime spectrum is exactly $(0)$ together with the maximal ideals, with nothing in between: every nonzero prime is maximal. This is what lets "factor into primes" mean "factor into maximal ideals", which are mutually coprime and so multiply cleanly. Drop dimension $1$ and the theorem fails outright: in $k[x,y]$, which has dimension $2$, the ideal $(x, y)^2 = (x^2, xy, y^2)$ is not a product of prime ideals at all, because the prime $(x,y)$ is not invertible — there is no clean "to contain is to divide" calculus once primes can be nested. Dimension $1$ is the dimension at which ideal factorization is possible, no more, no less.

**Why integrally closed.** This is the subtle hypothesis, and the one most easily forgotten. Dimension $1$ and Noetherian are not enough: the cusp ring $A = k[t^2, t^3]$ is a Noetherian domain of dimension $1$ in which ideals do *not* factor uniquely, because its local ring at the singular point is not a DVR. What goes wrong is that the local valuation — the order of vanishing — becomes ill-defined at a singular point, since the cotangent space has the wrong dimension. Integral-closedness is exactly the condition that fixes this: by the [[Thm - Characterization of Discrete Valuation Rings|DVR characterization]], a one-dimensional Noetherian local domain is integrally closed iff its maximal ideal is principal iff it is a DVR. So integral-closedness is the algebraic name for "smooth at every point", and smoothness is what makes the per-prime valuation well-defined, which is what makes ideal factorization work. Drop it and you get $k[t^2,t^3]$, where $(t^2, t^3)$ has no unique prime factorization. The strengthening direction — what if we demanded the ring be a *PID*? — would exclude exactly the interesting examples like $\mathbb{Z}[\sqrt{-5}]$ where the class group is nontrivial; demanding only integral-closedness keeps them while still guaranteeing ideal factorization. That gap between "Dedekind" and "PID" is the whole subject.

**Why Noetherian.** Factorization of any kind — into irreducibles, into primes, into anything — requires that descending chains of divisors terminate, so that the factorization process *stops*. Noetherianity supplies this: every ideal is finitely generated, every ascending chain stabilizes, and in particular every ideal contains a power of its radical, which is the finiteness needed to pin an ideal between consecutive prime powers. Drop Noetherianity and even existence of a finite factorization can fail; the valuation-theoretic counting argument that gives each exponent $e_i$ relies on the descending chain of powers $\mathfrak{p} \supsetneq \mathfrak{p}^2 \supsetneq \cdots$ being strictly decreasing, which is a Noetherian (via Nakayama) phenomenon. A non-Noetherian one-dimensional integrally closed domain — a general valuation ring of higher rank — need not have unique factorization of ideals.

**Why the two definitions agree, and which to use.** The page gives two equivalent forms: *integrally closed* (a global condition) and *every localization $A_\mathfrak{p}$ is a DVR* (a pointwise condition). They agree by the local–global principle for integral closure: $A$ is integrally closed iff every $A_\mathfrak{m}$ is, and a one-dimensional Noetherian local domain is integrally closed iff it is a DVR. The global form is the one to *check* (it is a single condition on $A$); the local form is the one to *use* (it lets you reduce any ideal question to a DVR computation prime by prime). Keeping both in mind — verify globally, compute locally — is the rhythm of the entire chapter.

---

# The Definition

A **Dedekind domain** is a [[Def - Noetherian Ring|Noetherian]] [[Def - Integral Domain|integral domain]] $A$ of [[Def - Krull Dimension and Height|Krull dimension]] $1$ (equivalently: $A$ is not a field, and every nonzero prime ideal is maximal) that satisfies one — hence, by the theorem below, all — of the following equivalent conditions:

1. $A$ is **[[Def - Integral Closure and Normal Domain|integrally closed]]** in its fraction field $K = \operatorname{Frac}(A)$.
2. For every nonzero prime ideal $\mathfrak{p}$, the localization $A_\mathfrak{p}$ is a **[[Def - Discrete Valuation and Valuation Ring|discrete valuation ring]]**.

> **Equivalence of (1) and (2).** For each maximal ideal $\mathfrak{m}$, the localization $A_\mathfrak{m}$ is a Noetherian local domain of dimension $\operatorname{ht}\mathfrak{m} = 1$. By the [[Thm - Characterization of Discrete Valuation Rings|DVR characterization]], $A_\mathfrak{m}$ is a DVR if and only if $A_\mathfrak{m}$ is integrally closed. By the local–global principle for normality, $A$ is integrally closed if and only if $A_\mathfrak{m}$ is integrally closed for every maximal $\mathfrak{m}$. Chaining these gives (1) $\iff$ (2).

A nonzero ideal of a Dedekind domain admits a unique factorization $\mathfrak{a} = \mathfrak{p}_1^{e_1}\cdots\mathfrak{p}_n^{e_n}$ into powers of distinct nonzero primes — this is the [[Thm - A Dedekind Domain has Unique Factorization of Ideals|main theorem]], and it is often taken as a third equivalent definition.

---

# Categorical / Structural Definition

Structurally, a Dedekind domain is the one-dimensional case of a **regular**, or **normal**, scheme: $\operatorname{Spec} A$ is a *regular Noetherian integral scheme of dimension one* — a **nonsingular affine curve**. The two equivalent definitions are the affine shadow of two equivalent geometric conditions: "$A$ integrally closed" says the curve is **normal**, and "every $A_\mathfrak{p}$ a DVR" says it is **smooth at every closed point** — and in dimension one, normal and smooth coincide. The structural payoff is that the nonzero **fractional ideals** of $A$ form a *group* under multiplication (this characterizes Dedekind domains among Noetherian domains: $A$ is Dedekind iff every nonzero fractional ideal is invertible), and this group is *free abelian on the set of nonzero primes*. So a Dedekind domain is exactly a one-dimensional Noetherian domain whose ideal monoid embeds into a free abelian group — the algebraic skeleton from which divisors and the [[Def - Fractional Ideal and the Ideal Class Group|class group]] are built.

---

# Relate to Other Fields / Compression

The cleanest compression: **a Dedekind domain is a "ring of integers" — a Noetherian, integrally closed, one-dimensional domain — built so that ideals factor uniquely even when elements do not.** It is the global object whose every local piece is a [[Def - Discrete Valuation and Valuation Ring|DVR]], the way a smooth curve is glued from local models each of which is a smooth point.

**True name:** the true name of a Dedekind domain is "**a one-dimensional Noetherian domain in which every nonzero ideal factors uniquely into primes**" — equivalently, "**a domain whose nonzero fractional ideals form a group**". This is the operational form: it is what you use the ring *for*. The "Noetherian, integrally closed, dimension $1$" definition is what you *check*; the unique-factorization form is what you *exploit*.

A Dedekind domain generalizes a [[Def - Principal Ideal Domain|PID]] by **dropping principality while keeping unique factorization of ideals**: every PID is Dedekind (a PID is Noetherian, integrally closed since it is a UFD, and of dimension $\leq 1$), but $\mathbb{Z}[\sqrt{-5}]$ is Dedekind and not a PID. The exact discrepancy is the [[Def - Fractional Ideal and the Ideal Class Group|ideal class group]]: a Dedekind domain is a PID iff its class group is trivial. So "Dedekind" is "PID up to the class group", and the class group measures the gap.

In the geometry–algebra dictionary, Dedekind domains are the coordinate rings of **smooth affine curves**, and they are also the local-at-codimension-one pieces of any normal variety. Number rings $\mathcal{O}_K$ are the arithmetic curves; the analogy "$\mathbb{Z}$ is like $k[T]$, $\mathcal{O}_K$ is like the coordinate ring of a branched cover of the line" is the foundational analogy of arithmetic geometry, and Dedekind domains are where both sides of it live.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}$ and any PID.** The integers $\mathbb{Z}$ form a Dedekind domain: Noetherian, integrally closed (it is a UFD), dimension $1$. Every PID is Dedekind for the same reasons, including $k[T]$ and $\mathbb{Z}[i]$. For a PID the class group is trivial and ideal factorization reduces to ordinary factorization of generators.

**Is an instance — rings of integers.** For any number field $K$, the ring of integers $\mathcal{O}_K$ is Dedekind — this is [[Thm - The Ring of Integers of a Number Field is Dedekind|the main existence theorem]]. Concretely $\mathbb{Z}[\sqrt{-5}] = \mathcal{O}_{\mathbb{Q}(\sqrt{-5})}$ is Dedekind but *not* a PID, with class number $2$; it is the standard example where ideal factorization is unique but element factorization is not. See [[Ex - Unique factorization of ideals in Z[sqrt -5]]].

**Is an instance — smooth affine curves.** The coordinate ring $k[x,y]/(y^2 - x^3 - x)$ of a smooth elliptic curve (minus a point) is Dedekind: it is a one-dimensional integrally closed domain. Its class group is the curve's Picard group, an object of deep arithmetic interest.

**Is NOT an instance — the cusp ring.** $A = k[t^2, t^3]$ is a Noetherian domain of dimension $1$ but is *not* integrally closed ($t \in \operatorname{Frac}(A)$ is integral over $A$ but not in $A$), so it is not Dedekind. Its local ring at the cusp is a one-dimensional local domain that is not a DVR. Ideals do not factor uniquely here; this is the example showing dimension $1$ alone is insufficient.

**Is NOT an instance — $\mathbb{Z}[\sqrt{-3}]$.** This ring is Noetherian of dimension $1$ but not integrally closed: $\omega = \tfrac{1+\sqrt{-3}}{2}$ is integral over it (a root of $x^2 - x + 1$) but not in it. Its integral closure $\mathbb{Z}[\omega] = \mathcal{O}_{\mathbb{Q}(\sqrt{-3})}$ *is* Dedekind. The lesson: not every "$\mathbb{Z}[\alpha]$" is Dedekind — you must take the full ring of integers.

**Is NOT an instance — $k[x,y]$.** A polynomial ring in two variables is Noetherian and integrally closed but has dimension $2$, so it is not Dedekind, and indeed $(x,y)^2$ is not a product of primes. This shows integral-closedness alone is insufficient; dimension $1$ is needed too.

**Calibration check.** Verify that a PID is integrally closed (use that a UFD is integrally closed, and every PID is a UFD) and has dimension $\leq 1$, hence is Dedekind unless it is a field. Confirm that "dimension $1$" is equivalent to "$A$ is not a field and every nonzero prime is maximal". Check that $\mathbb{Z}[\sqrt{-3}]$ fails condition (1) by exhibiting an integral element not in the ring, and that $k[x,y]$ fails the dimension condition by exhibiting a chain $(0) \subsetneq (x) \subsetneq (x,y)$ of primes of length $2$.

---

# Unlocked by This

> [!tip] Nonsingular affine curves and their function fields *(from Algebraic Geometry)*
> A Dedekind domain is the coordinate ring of a **smooth affine curve** $C = \operatorname{Spec} A$. Its closed points are the nonzero primes, and the local ring at each is a DVR — a smooth point with a well-defined order of vanishing. The fraction field $K = \operatorname{Frac}(A)$ is the **function field** of the curve, and different Dedekind domains with the same fraction field correspond to different affine pieces of the same complete curve. This is the starting point for the theory of **algebraic curves**, where the genus, the Riemann–Roch theorem, and the Jacobian all live.

> [!tip] The ideal class group as the Picard group *(from Algebraic Geometry / Number Theory)*
> Because nonzero fractional ideals of a Dedekind domain form a group, one can take the quotient by principal ideals to get the **ideal class group** $\operatorname{Cl}(A)$, developed on [[Def - Fractional Ideal and the Ideal Class Group]]. Geometrically this is the **Picard group** of the curve — isomorphism classes of line bundles — and arithmetically it is the **class number** of the number field, a finite group whose order is one of the deepest invariants in number theory. Its triviality is exactly the condition for the ring to be a PID.

> [!tip] Extensions of Dedekind domains and ramification *(from Algebraic Number Theory)*
> If $A$ is Dedekind with fraction field $K$ and $L/K$ is a finite separable extension, the integral closure $B$ of $A$ in $L$ is again **Dedekind**. The factorization of an extended prime $\mathfrak{p}B = \prod \mathfrak{P}_i^{e_i}$ records the **splitting and ramification** of $\mathfrak{p}$ in the extension, governed by the fundamental identity $\sum e_i f_i = [L:K]$. This is the engine of algebraic number theory and of the geometry of finite maps of curves.
