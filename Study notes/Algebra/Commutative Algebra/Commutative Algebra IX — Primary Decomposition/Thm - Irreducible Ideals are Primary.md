---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Irreducible Ideal"
  - "Def - Primary Ideal"
  - "Def - Noetherian Ring"
  - "Def - Ideal"
  - "Def - Annihilator"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a [[Def - Noetherian Ring|Noetherian ring]] and $I \subsetneq R$ a proper [[Def - Ideal|ideal]]. We pass to $\bar R = R/I$ and work there; $\bar y = y + I$ denotes the image of $y \in R$. For $\bar y \in \bar R$, the [[Def - Annihilator|annihilator]] is $\operatorname{Ann}(\bar y) = \{\bar r \in \bar R : \bar r \bar y = 0\}$. An [[Def - Irreducible Ideal|irreducible ideal]] is one not equal to an intersection of two strictly larger ideals; a [[Def - Primary Ideal|primary ideal]] $\mathfrak{q}$ is one in which every zero-divisor of $R/\mathfrak{q}$ is nilpotent. The full registry is on [[Commutative Algebra IX — Primary Decomposition]].

---

# Statement

> **Theorem (Irreducible $\Rightarrow$ Primary).** In a Noetherian ring $R$, every [[Def - Irreducible Ideal|irreducible ideal]] is [[Def - Primary Ideal|primary]].

> **Lemma (the form actually proved).** It suffices to prove: in a Noetherian ring, if the zero ideal $(0)$ is irreducible then $(0)$ is primary. The general statement follows by passing to $R/I$, since $I$ is irreducible (resp. primary) in $R$ exactly when $(0)$ is irreducible (resp. primary) in $R/I$.

The converse is false: $(X,Y)^2$ is primary but reducible. So "irreducible" is strictly stronger than "primary".

---

# Motivation

This theorem is the single ring-theoretic input of the existence half of primary decomposition. The [[Thm - Primary Decomposition Exists in a Noetherian Ring (Lasker-Noether)|Lasker–Noether theorem]] is proved in two moves: every ideal is a finite intersection of irreducible ideals (a soft, order-theoretic fact needing only the ascending chain condition), and every irreducible ideal is primary (the present theorem). The first move produces *pieces*; this theorem certifies that the pieces are *good* — that the indivisible-by-intersection ideals are exactly the arithmetically meaningful primary ones.

Why should one expect indivisibility to entail primariness? The two notions look unrelated: irreducibility is a *lattice* condition (not a meet of two larger ideals), primariness is an *arithmetic* condition (zero-divisors are nilpotent). The theorem asserts a bridge between them, and the bridge is the content worth understanding. It exists because a failure of primariness — a zero-divisor that is not nilpotent — can be *converted into a splitting*, an expression of the ideal as an intersection of two strictly larger ideals. Indivisibility forbids the splitting, hence forbids the bad zero-divisor. The conversion uses the ascending chain condition through a stabilising chain of annihilators, which is the one place Noetherianity enters.

The reason the theorem matters beyond the existence proof: it explains *why* primary ideals are the right pieces. They are not chosen arbitrarily; they are forced as the indivisible atoms of the intersection structure. Decomposition into irreducibles is the natural thing to do (split until you cannot), and this theorem says the natural thing produces primary pieces automatically.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$I$ is irreducible (in a Noetherian ring)". The skill is recognising irreducibility, which is most often verified *negatively*.

The first disguised source is **$I$ arises as a leaf of an irreducible decomposition**. The property $B$ is "$I$ cannot be split as $J_1 \cap J_2$ with both strictly larger" — exactly what the Noetherian-induction splitting process produces at its leaves. So every component delivered by the existence algorithm is irreducible, hence primary by this theorem. The non-obvious value: you never check irreducibility positively in practice; you obtain it for free as the terminus of repeated splitting. *Example problem:* certify that the leaves of a splitting tree are primary.

The second disguised source is **$(0)$ is irreducible in $R/I$, detected via the socle**. The property $B$ is "$R/I$ has an irreducible zero ideal", which holds iff the *socle* (sum of minimal nonzero ideals) of $R/I$ is contained in a single one — i.e. $R/I$ has a unique minimal nonzero ideal at each associated prime. This is a checkable condition in concrete quotients. The non-obviousness: irreducibility of an ideal is a property of the *bottom* of the lattice of $R/I$, computable from its minimal nonzero ideals. *Example problem:* check $(X, Y^2)$ is irreducible by seeing $k[Y]/(Y^2)$ has a unique minimal ideal $(\bar Y)$.

The third disguised source is **$I$ is $\mathfrak{m}$-primary with a one-dimensional socle**. The property $B$ is "$R/I$ is local Artinian with $\dim_k(\operatorname{socle}) = 1$" (a *Gorenstein-Artinian* condition). Such ideals are irreducible, and the theorem says (conversely-flavoured) they are primary. The non-obvious value: the irreducible $\mathfrak{m}$-primary ideals are exactly those with simple socle, linking irreducibility to the Gorenstein property. *Example problem:* recognise that $(\pi^n)$ in a discrete valuation ring is irreducible because its quotient has a one-dimensional socle.

**Targets (Output Amplification)**

The conclusion is "$I$ is primary".

Combine "$I$ irreducible $\Rightarrow$ primary" with **the irreducible-decomposition step**. Every ideal is a finite intersection of irreducibles, each of which is now primary. The further result $E$: existence of primary decompositions — the [[Thm - Primary Decomposition Exists in a Noetherian Ring (Lasker-Noether)|Lasker–Noether theorem]]. This is the headline application and is nonobvious only in that it needs *both* the soft splitting and this hard upgrade.

Combine "$I$ primary" with **taking the radical**. A primary $I$ has $\sqrt I$ prime. The further result $E$: each irreducible component is attached to a single prime, so the irreducible decomposition refines the prime structure of $V(I)$. This is nonobvious because irreducibility alone says nothing about primes; the theorem injects the prime via primariness.

Combine "irreducible $\Rightarrow$ primary" with **grouping by radical**. After splitting into irreducible-hence-primary pieces, components with equal radical merge into a single primary component. The further result $E$: passage from a (fine) irreducible decomposition to a (coarse) minimal primary decomposition. This is nonobvious because the irreducible decomposition is typically *finer* than the minimal primary one — the theorem's pieces are smaller than the final components.

---

# Why Is It True

The theorem is true because **a non-nilpotent zero-divisor in $R/I$ lets you split $(0)$ into two larger ideals, and irreducibility forbids the split.** Work in $\bar R = R/I$, where irreducibility of $I$ means $(0)$ is irreducible.

Suppose, for contradiction, that $(0)$ is *not* primary: there is a zero-divisor $\bar y$ that is not nilpotent. "$\bar y$ is a zero-divisor" means $\bar x \bar y = 0$ for some $\bar x \neq 0$, i.e. $\operatorname{Ann}(\bar y) \neq 0$. "$\bar y$ is not nilpotent" means $\bar y^k \neq 0$ for all $k$. Now watch the chain of annihilators of powers of $\bar y$:
$$\operatorname{Ann}(\bar y) \subseteq \operatorname{Ann}(\bar y^2) \subseteq \operatorname{Ann}(\bar y^3) \subseteq \cdots$$
(each containment because if $\bar r \bar y^k = 0$ then $\bar r \bar y^{k+1} = 0$). The ring is [[Def - Noetherian Ring|Noetherian]], so this ascending chain stabilises: $\operatorname{Ann}(\bar y^n) = \operatorname{Ann}(\bar y^{n+1}) = \cdots$ for some $n$.

Here is the splitting. Consider the two ideals
$$(\bar y^n) \quad\text{and}\quad \operatorname{Ann}(\bar y^n).$$
I claim $(\bar y^n) \cap \operatorname{Ann}(\bar y^n) = (0)$. Take $\bar z$ in both: $\bar z = \bar a \bar y^n$ for some $\bar a$, and $\bar z \bar y^n = 0$. Then $\bar a \bar y^{2n} = 0$, so $\bar a \in \operatorname{Ann}(\bar y^{2n}) = \operatorname{Ann}(\bar y^n)$ (by stabilisation), whence $\bar z = \bar a \bar y^n = 0$. So the intersection is $(0)$.

Now both ideals are *strictly larger* than $(0)$: $(\bar y^n) \neq 0$ because $\bar y$ is not nilpotent, and $\operatorname{Ann}(\bar y^n) \supseteq \operatorname{Ann}(\bar y) \neq 0$ because $\bar y$ is a zero-divisor. So $(0) = (\bar y^n) \cap \operatorname{Ann}(\bar y^n)$ exhibits $(0)$ as an intersection of two strictly larger ideals — contradicting irreducibility of $(0)$. Hence no non-nilpotent zero-divisor exists, i.e. $(0)$ is primary, i.e. $I$ is primary.

The one-line mechanism: **stabilise the annihilator chain of a would-be bad zero-divisor $\bar y$, and the pair $\big((\bar y^n), \operatorname{Ann}(\bar y^n)\big)$ splits $(0)$ — which irreducibility forbids.**

The role of each hypothesis is now visible. Noetherianity is used *only* to stabilise the annihilator chain (so that $\bar a \bar y^{2n} = 0 \Rightarrow \bar a \bar y^n = 0$). Irreducibility is used *only* at the end, to derive the contradiction from the splitting. Strip either and the theorem fails: without Noetherianity the chain need not stabilise and the splitting argument breaks; without irreducibility there is no contradiction and reducible-but-not-primary ideals like $(X,Y)^2$ exist.

---

# What Makes This Hard

The non-obvious step is the *construction of the splitting* — pairing $(\bar y^n)$ with $\operatorname{Ann}(\bar y^n)$ and showing their intersection is zero, which requires the annihilator chain to have stabilised so that $\bar a \bar y^{2n} = 0$ forces $\bar a \bar y^n = 0$. Most people get stuck seeing *why* a bad zero-divisor produces a splitting at all; the trick of squaring (using $\bar y^{2n}$ to collapse back to $\bar y^n$) is the crux and is easy to miss. The common error is to forget that *both* ideals in the split must be strictly larger than $(0)$ — checking $(\bar y^n) \neq 0$ uses non-nilpotence, checking $\operatorname{Ann}(\bar y^n) \neq 0$ uses zero-divisor-ness, and omitting either leaves the contradiction incomplete.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Reduce to "$(0)$ irreducible $\Rightarrow$ $(0)$ primary" in $R/I$. Assume a non-nilpotent zero-divisor $\bar y$; stabilise the annihilator chain $\operatorname{Ann}(\bar y^k)$; build the splitting $(0) = (\bar y^n) \cap \operatorname{Ann}(\bar y^n)$ with both factors nonzero; contradict irreducibility.

**Subgoal decomposition:**

1. **Reduce to the quotient.** Show $I$ irreducible/primary in $R$ iff $(0)$ is irreducible/primary in $R/I$.
   - *Hint:* Both notions are defined via the lattice of ideals above $I$ / the quotient ring, which is the ideal lattice / ring of $R/I$.
   - *Why needed:* It lets you work with $(0)$, simplifying the annihilator bookkeeping.

2. **Stabilise the annihilator chain.** From a non-nilpotent zero-divisor $\bar y$, get $n$ with $\operatorname{Ann}(\bar y^n) = \operatorname{Ann}(\bar y^{2n})$.
   - *Hint:* The chain $\operatorname{Ann}(\bar y^k)$ ascends; Noetherian rings have stabilising chains.
   - *Why needed:* Stabilisation is what makes the intersection in the splitting vanish.

3. **Build the splitting and contradict.** Show $(\bar y^n) \cap \operatorname{Ann}(\bar y^n) = (0)$ with both ideals nonzero.
   - *Hint:* For the intersection: $\bar z = \bar a \bar y^n$ and $\bar z \bar y^n = 0$ give $\bar a \bar y^{2n} = 0$, so $\bar a \bar y^n = \bar z = 0$. For nonzero: non-nilpotence and zero-divisor-ness.
   - *Why needed:* It is the contradiction with irreducibility, completing the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: Irreducibility and primariness are quotient properties
> **Statement:** $I$ is irreducible (resp. primary) in $R$ if and only if $(0)$ is irreducible (resp. primary) in $R/I$.
>
> **Hint:** Ideals of $R$ containing $I$ correspond to ideals of $R/I$; this bijection preserves intersections and the "strictly larger" relation. Primariness is defined through $R/I$ already.
>
> **Why needed:** It reduces the theorem to the clean statement about $(0)$, simplifying every later computation.
>
> > [!note]- Full proof
> > By the [[Thm - Ideal Correspondence|ideal correspondence]], ideals of $R$ containing $I$ correspond bijectively and inclusion-preservingly to ideals of $R/I$, with $I \leftrightarrow (0)$ and intersection going to intersection. So $I = J_1 \cap J_2$ with $J_1, J_2 \supsetneq I$ corresponds to $(0) = \bar J_1 \cap \bar J_2$ with $\bar J_1, \bar J_2 \supsetneq (0)$; hence $I$ irreducible $\iff (0)$ irreducible in $R/I$. Primariness of $I$ is by definition a condition on zero-divisors of $R/I$, which is exactly primariness of $(0)$ in $R/I$ (as $(R/I)/(0) = R/I$).

> [!note]- Lemma 2: The annihilator chain of a power stabilises
> **Statement:** In a Noetherian ring, for any $\bar y$ the chain $\operatorname{Ann}(\bar y) \subseteq \operatorname{Ann}(\bar y^2) \subseteq \cdots$ stabilises: $\operatorname{Ann}(\bar y^n) = \operatorname{Ann}(\bar y^{2n})$ for some $n$.
>
> **Hint:** Each containment holds because $\bar r \bar y^k = 0 \Rightarrow \bar r \bar y^{k+1} = 0$; apply the ascending chain condition.
>
> **Why needed:** Stabilisation is the only use of Noetherianity, and it is what makes the splitting's intersection vanish.
>
> > [!note]- Full proof
> > If $\bar r \bar y^k = 0$ then $\bar r \bar y^{k+1} = (\bar r \bar y^k)\bar y = 0$, so $\operatorname{Ann}(\bar y^k) \subseteq \operatorname{Ann}(\bar y^{k+1})$: the chain ascends. In a [[Def - Noetherian Ring|Noetherian ring]] every ascending chain of ideals stabilises, so there is $N$ with $\operatorname{Ann}(\bar y^k) = \operatorname{Ann}(\bar y^N)$ for all $k \geq N$. Taking $n = N$ gives $\operatorname{Ann}(\bar y^n) = \operatorname{Ann}(\bar y^{2n})$.

> [!note]- Lemma 3: The splitting of $(0)$
> **Statement:** If $\bar y$ is a non-nilpotent zero-divisor and $\operatorname{Ann}(\bar y^n) = \operatorname{Ann}(\bar y^{2n})$, then $(0) = (\bar y^n) \cap \operatorname{Ann}(\bar y^n)$ with both ideals strictly larger than $(0)$.
>
> **Hint:** Intersection: an element $\bar a \bar y^n$ killed by $\bar y^n$ has $\bar a \in \operatorname{Ann}(\bar y^{2n}) = \operatorname{Ann}(\bar y^n)$, so it is zero. Nonzero: non-nilpotence and zero-divisor-ness.
>
> **Why needed:** It is the splitting that contradicts irreducibility — the heart of the theorem.
>
> > [!note]- Full proof
> > *Intersection is $(0)$.* Let $\bar z \in (\bar y^n) \cap \operatorname{Ann}(\bar y^n)$. Write $\bar z = \bar a \bar y^n$; from $\bar z \in \operatorname{Ann}(\bar y^n)$, $\bar z \bar y^n = \bar a \bar y^{2n} = 0$, so $\bar a \in \operatorname{Ann}(\bar y^{2n}) = \operatorname{Ann}(\bar y^n)$, whence $\bar z = \bar a \bar y^n = 0$. Thus the intersection is $(0)$.
> >
> > *Both strictly larger.* $(\bar y^n) \neq (0)$ since $\bar y$ is not nilpotent, so $\bar y^n \neq 0$. And $\operatorname{Ann}(\bar y^n) \supseteq \operatorname{Ann}(\bar y) \neq (0)$ since $\bar y$ is a zero-divisor (some nonzero $\bar x$ kills it). So both ideals strictly contain $(0)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be Noetherian and $I$ irreducible. By Lemma 1, it suffices to show $(0)$ is primary in $\bar R = R/I$, given that $(0)$ is irreducible there.
>
> ---
> **Step 0 — setup.** Suppose for contradiction that $(0) \subseteq \bar R$ is not primary. Then there is a zero-divisor $\bar y \in \bar R$ that is not nilpotent: $\bar x \bar y = 0$ for some $\bar x \neq 0$, while $\bar y^k \neq 0$ for all $k \geq 1$.
>
> ---
> **Step 1 — stabilise.** By Lemma 2 the chain $\operatorname{Ann}(\bar y^k)$ stabilises; fix $n$ with $\operatorname{Ann}(\bar y^n) = \operatorname{Ann}(\bar y^{2n})$.
>
> ---
> **Step 2 — split.** By Lemma 3,
> $$(0) = (\bar y^n) \cap \operatorname{Ann}(\bar y^n),$$
> and both $(\bar y^n)$ and $\operatorname{Ann}(\bar y^n)$ strictly contain $(0)$.
>
> ---
> **Step 3 — contradiction.** This exhibits $(0)$ as the intersection of two strictly larger ideals, contradicting the irreducibility of $(0)$ in $\bar R$. Hence no non-nilpotent zero-divisor exists: every zero-divisor of $\bar R$ is nilpotent, so $(0)$ is primary in $\bar R$, and therefore $I$ is primary in $R$. $\blacksquare$
>
> ---
> **Remark (converse fails).** $(X,Y)^2 \subseteq k[X,Y]$ is $(X,Y)$-primary but reducible: $(X,Y)^2 = (X^2, Y) \cap (X, Y^2)$. So irreducible is strictly stronger than primary, and the theorem's one-way direction is sharp.

---

# Cross-Field Exercise Suggestions

**Gorenstein-Artinian rings and one-dimensional socles.** An $\mathfrak{m}$-primary ideal $I$ in a Noetherian local ring is irreducible exactly when $R/I$ has a *simple socle* (a unique minimal nonzero ideal), the defining feature of an Artinian Gorenstein ring. The theorem then says such $I$ are primary — automatic, but the link to the socle is the content. The nonobvious recognition: irreducibility is the algebraic shadow of the Gorenstein duality condition, and the splitting argument fails precisely when the socle has dimension $\geq 2$.

**The structure theorem over a PID via irreducible submodules.** For a finitely generated module over a [[Def - Principal Ideal Domain|PID]], the primary cyclic factors $R/(p^a)$ are irreducible submodules (their quotients have totally ordered ideal lattices, so no splitting), and the theorem certifies them primary. The nonobvious link: the indecomposability of the cyclic factors in the structure theorem is exactly irreducibility, and "irreducible $\Rightarrow$ primary" is why the elementary-divisor decomposition is a primary decomposition.

**Detecting reducibility through the socle in computer algebra.** Algorithms that compute irreducible decompositions test reducibility by examining the socle of $R/I$ at each associated prime; a socle of dimension $\geq 2$ signals a splitting, which the algorithm performs. This theorem guarantees the irreducible leaves are primary, so the irreducible decomposition refines to a primary one. The nonobvious application: the abstract splitting argument of the proof is implemented literally as a reducibility test.

---

# Bridges

- **[[Thm - Primary Decomposition Exists in a Noetherian Ring (Lasker-Noether)|Lasker–Noether existence]]** — the theorem this one exists to serve. Existence is "finite intersection of irreducibles (chain condition) $+$ irreducible is primary (this theorem)". This page supplies the second, ring-theoretic, half; the first half is a soft maximal-counterexample induction. Without this theorem the existence proof would deliver only irreducible decompositions, with no link to the prime structure.

- **[[Def - Irreducible Ideal|Irreducible Ideal]]** — the definition whose payoff is this theorem. Irreducible ideals are introduced precisely so that they can be shown primary; the converse failure ($(X,Y)^2$) is what keeps them strictly stronger, hence finer, than primary, which is why an irreducible decomposition refines the minimal primary one.

- **[[Def - Noetherian Ring|Noetherian Ring]] and the ascending chain condition** — the hypothesis enters this theorem at exactly one point, the stabilisation of the annihilator chain $\operatorname{Ann}(\bar y^k)$. This is a recurring template: many commutative-algebra finiteness results reduce to "an ascending chain of annihilators stabilises", and recognising this pattern is half the battle. The same stabilisation underlies the existence of associated primes and the finiteness of $\operatorname{Ass}(M)$.

- **The socle and Gorenstein duality** — the structural refinement. Irreducibility of an $\mathfrak{m}$-primary ideal is equivalent to the socle of $R/I$ being one-dimensional, which is the Artinian-Gorenstein condition; this links the lattice notion of irreducibility to the homological notion of Gorenstein duality, where irreducible ideals are the ones with a unique "bottom".

---

# Unlocked by This

> [!tip] Irreducible (indecomposable) closed subschemes *(from Algebraic Geometry)*
> An irreducible ideal corresponds to a closed subscheme that does not split as a union of two strictly smaller closed subschemes within its scheme structure — the indecomposable pieces of a scheme under intersection. This theorem says these indecomposable pieces are single-component (primary) subschemes, which is why decomposing a scheme by repeatedly splitting yields components-with-multiplicity, each supported on a single irreducible variety.

> [!tip] The socle, injective hulls, and Gorenstein rings *(from Homological Algebra)*
> Irreducibility of an ideal $I$ is governed by the **socle** of $R/I$, and a one-dimensional socle is the Artinian-Gorenstein condition. This connects to injective hulls (the injective hull of the residue field has a one-dimensional socle) and to Matlis duality, where irreducible $\mathfrak{m}$-primary ideals correspond to cyclic submodules of the injective hull. The theorem's annihilator-chain argument is an early instance of the depth-and-socle reasoning that pervades the homological theory of Cohen–Macaulay and Gorenstein rings.
