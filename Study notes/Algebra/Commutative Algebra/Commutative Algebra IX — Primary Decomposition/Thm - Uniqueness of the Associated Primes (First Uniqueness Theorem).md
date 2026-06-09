---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Primary Ideal"
  - "Def - Associated and Minimal Primes"
  - "Def - Ideal"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Prime and Maximal Ideal"
  - "Def - The Prime Spectrum (Spec)"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring and $I \subsetneq R$ a proper [[Def - Ideal|ideal]] with a minimal [[Def - Primary Ideal|primary decomposition]] $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$, $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$ (distinct primes). The **colon ideal** is $(I : x) = \{r \in R : rx \in I\}$ for $x \in R$. We write $\operatorname{Spec} R$ for the [[Def - The Prime Spectrum (Spec)|prime spectrum]] and $\sqrt{\,\cdot\,}$ for the [[Def - Radical of an Ideal and the Nilradical|radical]]. The set of [[Def - Associated and Minimal Primes|associated primes]] is $\operatorname{Ass}(I) = \{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$. The full registry is on [[Commutative Algebra IX — Primary Decomposition]].

---

# Statement

> **Theorem (First Uniqueness Theorem).** Let $I \subsetneq R$ have a minimal primary decomposition $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ with $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$. Then the set of primes $\{\mathfrak{p}_1, \dots, \mathfrak{p}_n\}$ depends only on $I$ — not on the chosen decomposition. Explicitly,
> $$\{\mathfrak{p}_1, \dots, \mathfrak{p}_n\} \;=\; \big\{\, \sqrt{(I : x)} \;:\; x \in R \,\big\} \cap \operatorname{Spec} R,$$
> the set of those colon-radicals $\sqrt{(I:x)}$ that happen to be prime. In particular $\operatorname{Ass}(I)$ is a well-defined invariant of $I$.

The right-hand side manifestly depends only on $I$ (it is built from $I$ and the colon operation), so the equality forces the left-hand side — the radicals of the components — to be an invariant.

---

# Motivation

A primary decomposition is a *presentation* of an ideal, and presentations are not unique: the same $I$ can be written as $\bigcap \mathfrak{q}_i$ in genuinely different ways. The running example $(X^2, XY) = (X) \cap (X,Y)^2 = (X) \cap (X^2, Y)$ has two distinct minimal decompositions. This raises an anxiety: if the decomposition is not canonical, is *any* of its data meaningful, or is the whole apparatus arbitrary? The First Uniqueness Theorem is the reassurance. It identifies the part of the decomposition that is forced by $I$ alone — the set of attached primes — and proves it is the same for every minimal decomposition.

The theorem matters because it converts a slippery, non-canonical object into a rigid invariant. Before it, "the associated primes of $I$" would be ill-defined, depending on a choice. After it, $\operatorname{Ass}(I)$ is as intrinsic to $I$ as its radical. This is what allows the rest of the theory to speak unambiguously of isolated primes, embedded primes, and the components of $V(I)$ — all of which are extracted from $\operatorname{Ass}(I)$.

The mechanism by which it achieves this is the *colon ideal*, and the deeper content of the theorem is that **the primes attached to $I$ can be detected without ever choosing a decomposition** — you compute $\sqrt{(I:x)}$ as $x$ ranges over $R$, collect those that are prime, and you have $\operatorname{Ass}(I)$. The decomposition is a scaffold used to prove the formula; once proved, the formula stands on its own. This is the same pattern as recovering an integer's prime divisors from $\gcd$ computations rather than from a particular factorisation: the invariant is read off by probing, not by factoring.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$I$ has a minimal primary decomposition" — notably *not* "$R$ is Noetherian". The skill is recognising when this weaker hypothesis is met.

The first disguised source is **$R$ is Noetherian**. The property $B$ is "every ideal has a primary decomposition" (by [[Thm - Primary Decomposition Exists in a Noetherian Ring (Lasker-Noether)|Lasker–Noether]]), and minimal ones exist by refinement. So in any Noetherian ring the theorem applies to every ideal, and $\operatorname{Ass}(I)$ is always defined. The non-obvious point: the uniqueness theorem needs *less* than the existence theorem — it never re-invokes Noetherianity, only the bare existence of a decomposition. *Example problem:* compute $\operatorname{Ass}$ of any ideal in $k[X_1, \dots, X_n]$.

The second disguised source is **$I$ is given explicitly as an intersection of primaries**. The property $B$ is "$I = \bigcap \mathfrak{q}_i$ is handed to you" — even in a non-Noetherian ring. Then the theorem applies directly, and you may read off $\operatorname{Ass}(I) = \{\sqrt{\mathfrak{q}_i}\}$ knowing it is canonical. The non-obviousness: uniqueness is a property of $I$, so a single exhibited decomposition certifies the invariant for *all* decompositions. *Example problem:* verify that two explicit decompositions of the same ideal have the same radicals.

The third disguised source is **$I$ is radical**. The property $B$ is "$\sqrt I = I$". Then the (unique) decomposition is $I = \bigcap \mathfrak{p}_i$ over the minimal primes, with no embedded primes, and $\operatorname{Ass}(I)$ is exactly the set of minimal primes over $I$. The non-obvious value: for radical ideals the theorem degenerates to "a radical ideal is the intersection of its minimal primes", recovering the variety–ideal dictionary. *Example problem:* read off the irreducible components of a reduced variety as $\operatorname{Ass}(I(X))$.

**Targets (Output Amplification)**

The conclusion is "$\operatorname{Ass}(I) = \{\sqrt{(I:x)}\} \cap \operatorname{Spec} R$ is an invariant".

Combine $\operatorname{Ass}(I)$ with **the inclusion order**. The minimal elements of $\operatorname{Ass}(I)$ are the isolated primes, equal to the minimal primes over $I$; the rest are embedded. The further result $E$: the canonical stratification of $\operatorname{Ass}(I)$ into isolated and embedded primes, which separates the irreducible components from the embedded subvarieties. This is nonobvious because the theorem only asserts the *set* is invariant; combining with the order extracts geometric meaning.

Combine $\operatorname{Ass}(I)$ with **the union of associated primes**. The zero-divisors of $R/I$ are exactly $\bigcup_i (\mathfrak{p}_i / I)$ — the union of the associated primes (mod $I$). The further result $E$: a precise description of where $R/I$ fails to be a domain, controlled entirely by the finite set $\operatorname{Ass}(I)$. This is nonobvious because zero-divisors are a multiplicative notion, yet they are pinned down by the additive structure of the associated primes.

Combine $\operatorname{Ass}(I)$ with **localization**. After localizing at a prime $\mathfrak{p}$, $\operatorname{Ass}(IR_{\mathfrak{p}}) = \{\mathfrak{p}_i R_{\mathfrak{p}} : \mathfrak{p}_i \subseteq \mathfrak{p}\}$ — only the associated primes contained in $\mathfrak{p}$ survive. The further result $E$: the components over isolated primes become canonical (Second Uniqueness), since localizing at an isolated $\mathfrak{p}_i$ leaves a single primary ideal. This is nonobvious because it is precisely the *isolated* primes, not the embedded ones, that localization isolates.

---

# Why Is It True

The theorem is true because **the colon ideal $(I : x)$ is a probe that reports exactly which primary components $x$ misses, and taking its radical reads off the corresponding primes**. Everything follows from watching the colon distribute through the decomposition.

Start with the key identity: colon distributes over intersection,
$$(I : x) = \Big(\bigcap_i \mathfrak{q}_i : x\Big) = \bigcap_i (\mathfrak{q}_i : x).$$
This is immediate — $rx \in \bigcap \mathfrak{q}_i$ iff $rx \in \mathfrak{q}_i$ for every $i$. Now examine each factor $(\mathfrak{q}_i : x)$. There are two cases. If $x \in \mathfrak{q}_i$, then $rx \in \mathfrak{q}_i$ for *every* $r$, so $(\mathfrak{q}_i : x) = R$ — this component contributes nothing. If $x \notin \mathfrak{q}_i$, then because $\mathfrak{q}_i$ is $\mathfrak{p}_i$-primary, the colon $(\mathfrak{q}_i : x)$ is again $\mathfrak{p}_i$-primary, so its radical is $\mathfrak{p}_i$. Taking radicals through the intersection,
$$\sqrt{(I:x)} = \bigcap_{i : x \notin \mathfrak{q}_i} \mathfrak{p}_i.$$
**The colon ideal, radicalised, is the intersection of exactly the primes whose components $x$ escapes.** That is the whole engine.

Now harvest the primes. To get a *single* prime $\mathfrak{p}_i$, choose $x$ inside every component except the $i$-th. In a minimal decomposition this is possible precisely because no component contains the intersection of the others — minimality is what guarantees there is an $x \in \bigcap_{j \neq i}\mathfrak{q}_j$ with $x \notin \mathfrak{q}_i$. For such an $x$, every term with $x \in \mathfrak{q}_j$ drops out and only $\mathfrak{p}_i$ survives: $\sqrt{(I:x)} = \mathfrak{p}_i$, a prime. So every $\mathfrak{p}_i$ appears on the right-hand side. Conversely, whenever $\sqrt{(I:x)} = \bigcap_{i \in S}\mathfrak{p}_i$ is itself prime, the dual form of prime avoidance forces this intersection to *be* one of the $\mathfrak{p}_i$ (a prime containing an intersection of primes contains, hence equals when minimal, one of them). So every prime colon-radical is some $\mathfrak{p}_i$. The two inclusions give the equality, and since the right-hand side is built from $I$ alone, the left-hand set $\{\mathfrak{p}_i\}$ is an invariant.

The one-line mechanism: **$\sqrt{(I:x)} = \bigcap_{x \notin \mathfrak{q}_i}\mathfrak{p}_i$, so choosing $x$ to lie in all components but one peels off a single associated prime.**

---

# What Makes This Hard

The crux is the lemma "$(\mathfrak{q} : x)$ is $\mathfrak{p}$-primary when $\mathfrak{q}$ is $\mathfrak{p}$-primary and $x \notin \mathfrak{q}$" — most people get stuck verifying the primary condition for the colon, where the case $x \in \sqrt{\mathfrak{q}}$ versus $x \notin \sqrt{\mathfrak{q}}$ must be handled. The non-obvious move is the harvesting step: to extract $\mathfrak{p}_i$ alone you must invoke *minimality* to find an $x$ in all other components but not in $\mathfrak{q}_i$, and it is easy to forget that minimality is exactly what makes this $x$ exist. The most common error is to think the formula gives the *components* uniquely; it gives only the *radicals* — the embedded components genuinely vary, and the theorem is silent about them.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Compute $\sqrt{(I:x)}$ by distributing the colon through the decomposition and using that $(\mathfrak{q}_i : x)$ is $\mathfrak{p}_i$-primary (radical $\mathfrak{p}_i$) when $x \notin \mathfrak{q}_i$ and $R$ when $x \in \mathfrak{q}_i$. Show every $\mathfrak{p}_i$ arises (by minimality) and every prime $\sqrt{(I:x)}$ is some $\mathfrak{p}_i$ (by prime avoidance).

**Subgoal decomposition:**

1. **Colon distributes; compute its radical.** Show $\sqrt{(I:x)} = \bigcap_{x \notin \mathfrak{q}_i}\mathfrak{p}_i$.
   - *Hint:* $(I:x) = \bigcap(\mathfrak{q}_i : x)$; each factor is $R$ (if $x \in \mathfrak{q}_i$) or $\mathfrak{p}_i$-primary (if $x \notin \mathfrak{q}_i$), so radicalise.
   - *Why needed:* It is the master formula from which both inclusions follow.

2. **Every $\mathfrak{p}_i$ is achieved.** For each $i$, find $x$ with $\sqrt{(I:x)} = \mathfrak{p}_i$.
   - *Hint:* By minimality choose $x \in \bigcap_{j \neq i}\mathfrak{q}_j \setminus \mathfrak{q}_i$; then only the $i$-th term survives.
   - *Why needed:* It gives the inclusion $\{\mathfrak{p}_i\} \subseteq \{\text{prime } \sqrt{(I:x)}\}$.

3. **Every prime colon-radical is some $\mathfrak{p}_i$.** If $\sqrt{(I:x)} = \bigcap_{i \in S}\mathfrak{p}_i$ is prime, it equals some $\mathfrak{p}_i$.
   - *Hint:* A prime containing $\bigcap_{i\in S}\mathfrak{p}_i$ contains some $\mathfrak{p}_i$; equality of a prime with an intersection of primes forces it to be one of them.
   - *Why needed:* It gives the reverse inclusion, completing the equality.

---

# Lemma Decomposition

> [!note]- Lemma 1: Colon distributes over intersection
> **Statement:** $\left(\bigcap_i \mathfrak{q}_i : x\right) = \bigcap_i (\mathfrak{q}_i : x)$ for any ideals $\mathfrak{q}_i$ and any $x \in R$.
>
> **Hint:** Unwind membership: $rx \in \bigcap \mathfrak{q}_i$ iff $rx \in \mathfrak{q}_i$ for all $i$.
>
> **Why needed:** It splits the colon of the whole ideal into colons of the components, the first move of the proof.
>
> > [!note]- Full proof
> > $r \in \left(\bigcap_i \mathfrak{q}_i : x\right)$ means $rx \in \bigcap_i \mathfrak{q}_i$, i.e. $rx \in \mathfrak{q}_i$ for every $i$, i.e. $r \in (\mathfrak{q}_i : x)$ for every $i$, i.e. $r \in \bigcap_i (\mathfrak{q}_i : x)$. The two membership conditions are identical, so the ideals are equal.

> [!note]- Lemma 2: The colon of a $\mathfrak{p}$-primary ideal
> **Statement:** Let $\mathfrak{q}$ be $\mathfrak{p}$-primary and $x \in R$. Then: (a) if $x \in \mathfrak{q}$, $(\mathfrak{q} : x) = R$; (b) if $x \notin \mathfrak{q}$, $(\mathfrak{q} : x)$ is $\mathfrak{p}$-primary, so $\sqrt{(\mathfrak{q} : x)} = \mathfrak{p}$; (c) if $x \notin \mathfrak{p}$, $(\mathfrak{q} : x) = \mathfrak{q}$.
>
> **Hint:** For (b), check $\mathfrak{q} \subseteq (\mathfrak{q}:x) \subseteq \mathfrak{p}$ and verify the primary condition directly.
>
> **Why needed:** It evaluates each factor in the distributed colon, giving the radical $\mathfrak{p}_i$ or $R$.
>
> > [!note]- Full proof
> > **(a)** If $x \in \mathfrak{q}$, then $rx \in \mathfrak{q}$ for all $r$, so $(\mathfrak{q} : x) = R$.
> >
> > **(c)** If $x \notin \mathfrak{p} = \sqrt{\mathfrak{q}}$: clearly $\mathfrak{q} \subseteq (\mathfrak{q}:x)$. Conversely if $rx \in \mathfrak{q}$ and $x \notin \sqrt{\mathfrak{q}}$, then since $\mathfrak{q}$ is primary, $r \in \mathfrak{q}$. So $(\mathfrak{q}:x) = \mathfrak{q}$, with radical $\mathfrak{p}$.
> >
> > **(b)** Suppose $x \notin \mathfrak{q}$. Then $\mathfrak{q} \subseteq (\mathfrak{q}:x)$. Taking radicals, $\mathfrak{p} = \sqrt{\mathfrak{q}} \subseteq \sqrt{(\mathfrak{q}:x)}$. For the reverse, let $r \in (\mathfrak{q}:x)$, so $rx \in \mathfrak{q}$; since $x \notin \mathfrak{q}$ and $\mathfrak{q}$ is primary, $r \in \sqrt{\mathfrak{q}} = \mathfrak{p}$. Hence $(\mathfrak{q}:x) \subseteq \mathfrak{p}$, so $\sqrt{(\mathfrak{q}:x)} \subseteq \mathfrak{p}$, giving $\sqrt{(\mathfrak{q}:x)} = \mathfrak{p}$. Finally $(\mathfrak{q}:x)$ is primary: if $ab \in (\mathfrak{q}:x)$ with $b \notin \sqrt{(\mathfrak{q}:x)} = \mathfrak{p}$, then $abx \in \mathfrak{q}$ and $b \notin \sqrt{\mathfrak{q}}$, so primariness of $\mathfrak{q}$ gives $ax \in \mathfrak{q}$, i.e. $a \in (\mathfrak{q}:x)$. So $(\mathfrak{q}:x)$ is $\mathfrak{p}$-primary.

> [!note]- Lemma 3: Minimality supplies a separating element
> **Statement:** In a minimal decomposition $I = \bigcap_j \mathfrak{q}_j$, for each $i$ there exists $x$ with $x \in \mathfrak{q}_j$ for all $j \neq i$ and $x \notin \mathfrak{q}_i$.
>
> **Hint:** Minimality says $\mathfrak{q}_i \not\supseteq \bigcap_{j \neq i}\mathfrak{q}_j$, so the latter intersection is not contained in $\mathfrak{q}_i$.
>
> **Why needed:** It produces the $x$ that isolates a single $\mathfrak{p}_i$ in the colon formula.
>
> > [!note]- Full proof
> > By minimality, $I = \bigcap_j \mathfrak{q}_j \subsetneq \bigcap_{j \neq i}\mathfrak{q}_j$ (no component is redundant), so $\bigcap_{j\neq i}\mathfrak{q}_j \not\subseteq \mathfrak{q}_i$ — otherwise $\bigcap_{j\neq i}\mathfrak{q}_j = \mathfrak{q}_i \cap \bigcap_{j\neq i}\mathfrak{q}_j = I$. Pick $x \in \bigcap_{j\neq i}\mathfrak{q}_j \setminus \mathfrak{q}_i$; this $x$ lies in every $\mathfrak{q}_j$ with $j \neq i$ and not in $\mathfrak{q}_i$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ be minimal, $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$.
>
> ---
> **Step 0 — well-posedness.** Each $(I:x)$ is an ideal containing $I$, and $\sqrt{(I:x)}$ is its radical; the right-hand side $\{\sqrt{(I:x)} : x \in R\} \cap \operatorname{Spec} R$ is defined purely from $I$.
>
> ---
> **The master formula.** Fix $x \in R$. By Lemma 1, $(I : x) = \bigcap_i (\mathfrak{q}_i : x)$. By Lemma 2, each factor is $R$ (if $x \in \mathfrak{q}_i$) or has radical $\mathfrak{p}_i$ (if $x \notin \mathfrak{q}_i$). Since radical commutes with finite intersection,
> $$\sqrt{(I : x)} = \bigcap_{i \,:\, x \notin \mathfrak{q}_i} \mathfrak{p}_i. \tag{$\ast$}$$
>
> ---
> **$\{\mathfrak{p}_i\} \subseteq \{\text{prime } \sqrt{(I:x)}\}$.** Fix $i$. By Lemma 3 choose $x \in \bigcap_{j\neq i}\mathfrak{q}_j \setminus \mathfrak{q}_i$. Then $x \in \mathfrak{q}_j$ for $j \neq i$ and $x \notin \mathfrak{q}_i$, so the only surviving index in $(\ast)$ is $i$, giving $\sqrt{(I:x)} = \mathfrak{p}_i$ — a prime. So $\mathfrak{p}_i$ is a prime of the form $\sqrt{(I:x)}$.
>
> ---
> **$\{\text{prime } \sqrt{(I:x)}\} \subseteq \{\mathfrak{p}_i\}$.** Suppose $\sqrt{(I:x)}$ is prime; by $(\ast)$ it equals $\bigcap_{i \in S}\mathfrak{p}_i$ for $S = \{i : x \notin \mathfrak{q}_i\}$. A prime ideal $\mathfrak{p} = \bigcap_{i \in S}\mathfrak{p}_i$ contains the product $\prod_{i\in S}\mathfrak{p}_i \subseteq \bigcap_{i\in S}\mathfrak{p}_i = \mathfrak{p}$, so $\mathfrak{p} \supseteq \mathfrak{p}_{i_0}$ for some $i_0 \in S$ (primeness); but $\mathfrak{p} = \bigcap_{i\in S}\mathfrak{p}_i \subseteq \mathfrak{p}_{i_0}$ as well, so $\mathfrak{p} = \mathfrak{p}_{i_0}$, one of the $\mathfrak{p}_i$.
>
> ---
> **Conclusion.** The two inclusions give $\{\mathfrak{p}_1, \dots, \mathfrak{p}_n\} = \{\sqrt{(I:x)} : x \in R\} \cap \operatorname{Spec} R$. The right-hand side depends only on $I$, so the set of radicals $\{\mathfrak{p}_i\}$ is independent of the minimal decomposition. Hence $\operatorname{Ass}(I)$ is well-defined. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Associated primes of a module and the zero-divisor locus.** Reading $I = \operatorname{Ann}(R/I)$, the theorem becomes the computation of $\operatorname{Ass}(R/I)$ as a module — the primes $\sqrt{\operatorname{Ann}(\bar x)}$ that are prime — and the union of these is the set of zero-divisors of $R/I$. The nonobvious recognition: the *additive* invariant $\operatorname{Ass}$ controls the *multiplicative* phenomenon of zero-divisors, and the colon ideal $(I:x) = \operatorname{Ann}(\bar x)$ is the bridge.

**Recovering prime divisors of an integer by gcd probing.** In $\mathbb{Z}$, $(I : x) = ((n) : x) = (n/\gcd(n,x))$, and $\sqrt{(I:x)}$ is prime exactly when $n/\gcd(n,x)$ is a prime power. So the theorem specialises to "the prime divisors of $n$ are recovered by computing $\gcd(n, x)$ over all $x$" — prime detection without factorisation. The nonobvious link: the colon ideal *is* the gcd construction in $\mathbb{Z}$, and the First Uniqueness Theorem is the abstract form of "the prime divisors of $n$ are a well-defined set".

**Detecting embedded points in a singular scheme.** For the ideal of a scheme with an embedded point, the embedded prime $\mathfrak{p}$ is *not* a minimal prime, yet it appears as $\sqrt{(I:x)}$ for suitable $x$ — it is exactly the colon that exposes the embedded structure invisible to the reduced scheme. The nonobvious application: the embedded primes, which no variety can see, are detected algorithmically by colon-ideal computation, which is how computer algebra systems find them.

---

# Bridges

- **[[Def - Associated and Minimal Primes|Associated and Minimal Primes]]** — this theorem is what *makes that definition well-posed*. Without uniqueness, "$\operatorname{Ass}(I) = \{\sqrt{\mathfrak{q}_i}\}$" would depend on a choice of decomposition; the First Uniqueness Theorem proves the set is intrinsic, so the definition of associated primes, isolated primes, and embedded primes all rest on it. The colon-ideal formula is simultaneously the proof of uniqueness and the computational definition of $\operatorname{Ass}$.

- **[[Thm - Primary Decomposition Exists in a Noetherian Ring (Lasker-Noether)|Lasker–Noether existence]]** — the complementary half. Existence produces a decomposition; this theorem extracts its canonical content. The two are deliberately decoupled by hypothesis: existence needs Noetherianity, uniqueness needs only that *a* decomposition exists, so the First Uniqueness Theorem is strictly more widely applicable than the existence theorem that usually supplies its input.

- **The Second Uniqueness Theorem (isolated components are unique)** — the sequel that this theorem sets up. Once the associated primes are known to be invariant, one asks which *components* are invariant; the answer is that the isolated components (over minimal primes) are unique, proved by localizing at an isolated prime $\mathfrak{p}_i$, where the decomposition collapses to a single primary ideal $\mathfrak{q}_i = I^{ec}$. The embedded components remain genuinely non-unique. The First Uniqueness Theorem isolates *which* primes are isolated; the Second uses that to canonicalise their components.

- **Prime avoidance / the dual form $\bigcap \mathfrak{a}_i \subseteq \mathfrak{p} \Rightarrow$ some $\mathfrak{a}_i \subseteq \mathfrak{p}$** — the lattice fact that powers the reverse inclusion. A prime equal to an intersection of primes must be one of them, and this is what forces every prime colon-radical to be an actual $\mathfrak{p}_i$ rather than a spurious intersection. The same fact reappears throughout the chapter whenever a prime sits over an intersection.

---

# Unlocked by This

> [!tip] Associated points of a sheaf / scheme *(from Algebraic Geometry)*
> The associated primes of $I$ globalise to the **associated points** of the closed subscheme $V(I)$ — the points (generic points of components, plus embedded points) where the structure sheaf has a section with that exact support. The First Uniqueness Theorem is what makes "associated points" a well-defined finite set attached to a subscheme, independent of any presentation. These points control the behaviour of sections, the failure of a sheaf to be torsion-free, and the embedded structure that distinguishes a scheme from its underlying variety.

> [!tip] Bourbaki's $\operatorname{Ass}(M)$ and primary decomposition of modules *(from Commutative Algebra)*
> Generalised to modules, $\operatorname{Ass}(M) = \{\mathfrak{p} : \mathfrak{p} = \operatorname{Ann}(m) \text{ for some } m \in M\}$, and the colon-ideal proof becomes the statement that the associated primes of $M$ are detected by annihilators of single elements. This is the foundation of the module-theoretic primary decomposition in [[Modules II — §6.2|Modules II]] and downstream of depth theory: the smallest associated prime governs the grade, and $\operatorname{Ass}(M) = \varnothing$ iff $M = 0$, giving a finiteness invariant that pervades homological commutative algebra.
