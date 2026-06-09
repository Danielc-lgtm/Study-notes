---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - The Induced Map on Spectra"
  - "Def - Lying Over, Going Up, Going Down"
  - "Def - Prime and Maximal Ideal"
  - "Def - Local Ring and Residue Field"
  - "Thm - Integral Extensions and Fields (Domain Criterion)"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A \subseteq B$ be an [[Def - Integral Element and Integral Extension|integral extension]], $\iota : A \hookrightarrow B$ the inclusion, and [[Def - The Induced Map on Spectra|ι* : Spec B → Spec A]] the contraction map $\mathfrak{q} \mapsto \mathfrak{q} \cap A$. For $\mathfrak{p} \in \operatorname{Spec} A$ write $S = A \setminus \mathfrak{p}$ (multiplicative because $\mathfrak{p}$ is prime) and $B_{\mathfrak{p}} = S^{-1}B$ — the localization of $B$ at the elements of $S \subseteq A$, **not** a localization of $B$ at a prime of $B$, and generally **not** a local ring. We write $\operatorname{mSpec}$ for maximal ideals and $A_{\mathfrak{p}} = S^{-1}A$ for the [[Def - Local Ring and Residue Field|local ring]] of $A$ at $\mathfrak{p}$. The full registry is on [[Commutative Algebra VIII — Going Up and Going Down]].

---

# Statement

> **Theorem (Lying Over).** Let $A \subseteq B$ be an integral extension of rings and let $\mathfrak{p} \in \operatorname{Spec} A$. Then there exists $\mathfrak{q} \in \operatorname{Spec} B$ with $\mathfrak{q} \cap A = \mathfrak{p}$. Equivalently, the contraction map $\iota^* : \operatorname{Spec} B \to \operatorname{Spec} A$ is surjective.

> **Companion (fibre description).** The primes of $B$ lying over $\mathfrak{p}$ are in bijection with the maximal ideals of $B_{\mathfrak{p}} = (A \setminus \mathfrak{p})^{-1}B$, via extension and contraction along the localization map $B \to B_{\mathfrak{p}}$:
> $$\{\mathfrak{q} \in \operatorname{Spec} B : \mathfrak{q} \cap A = \mathfrak{p}\} \;\longleftrightarrow\; \operatorname{mSpec} B_{\mathfrak{p}}.$$

The companion is the load-bearing statement: lying over is the special case "$\operatorname{mSpec} B_{\mathfrak{p}} \neq \varnothing$", which holds because $B_{\mathfrak{p}} \neq 0$.

---

# Motivation

This is the theorem that turns an integral extension into a *covering* of spaces. Before it, the contraction map $\iota^* : \operatorname{Spec} B \to \operatorname{Spec} A$ is just a continuous map, and for a general ring map it can miss most of the base — the localization $\mathbb{Z} \hookrightarrow \mathbb{Q}$ has $\operatorname{Spec}\mathbb{Q}$ a single point hitting only $(0)$. Lying over says that integrality forbids this: *every* point of $\operatorname{Spec} A$ has a point above it. The fibres are all non-empty, so $\operatorname{Spec} B$ genuinely sits over the whole of $\operatorname{Spec} A$, the way a covering space sits over its base.

The role this plays in the chapter is foundational: it is the *anchor* for every chain-lifting argument. To lift an ascending chain $\mathfrak{p}_0 \subseteq \cdots \subseteq \mathfrak{p}_n$ upward you first need *some* prime over the bottom $\mathfrak{p}_0$ — that is lying over — and then [[Thm - Going Up|going up]] does the rest. To prove $\dim A \leq \dim B$ you need to start a chain upstairs, which again is lying over. And going up itself is proved by reducing to lying over in a quotient. So although lying over is the simplest of the four Cohen–Seidenberg theorems, it is the one the others stand on.

Why should one *expect* it? Because the obstruction to a prime existing over $\mathfrak{p}$ is the vanishing of a certain ring, and integrality (or rather, just the algebra of localization) makes that ring non-zero. The fibre over $\mathfrak{p}$ is governed by the ring $B_{\mathfrak{p}}$ obtained by inverting everything in $A$ outside $\mathfrak{p}$; a prime over $\mathfrak{p}$ exists iff $B_{\mathfrak{p}}$ has a maximal ideal contracting correctly, and the only way to have *no* such ideal is for $B_{\mathfrak{p}}$ to be the zero ring. But $B_{\mathfrak{p}}$ is a localization at a set not containing $0$, so it is non-zero — and a non-zero ring always has a maximal ideal. That is the entire mechanism, and it is why the proof is one line once the fibre is correctly identified.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is "$A \subseteq B$ is an integral extension". The skill is recognising disguised forms of it.

The first disguised source is **a module-finite extension**: $B$ is a finitely generated $A$-module. This implies $B$ is integral over $A$ (each $b \in B$ satisfies the characteristic polynomial of multiplication-by-$b$ on the finite module, a monic relation over $A$ — the determinant trick). So whenever $B$ appears as a finite $A$-module, lying over is available even though "integral" was never said. *Example problem:* the ring of integers $\mathcal{O}_K$ of a number field is a finite $\mathbb{Z}$-module, so every rational prime has a prime of $\mathcal{O}_K$ over it — the existence half of "primes split in number fields".

The second disguised source is **the conclusion of [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Noether normalization]]**: a finitely generated $k$-algebra $A$ is module-finite over a polynomial subring $k[X_1,\dots,X_d]$. That inclusion is integral, so lying over applies to it. *Example problem:* every maximal ideal of $k[X_1,\dots,X_d]$ has a prime of $A$ over it, which is how one transports the Nullstellensatz across a normalization.

The third disguised source is **a finite ring map that is not an inclusion**: $f : A \to B$ integral but possibly non-injective. Factor $f = (A \twoheadrightarrow f(A)) \circ (f(A) \hookrightarrow B)$; the second factor is an integral *extension*, the first a quotient (which is onto on spectra). So lying over for the extension plus surjectivity of the quotient on $V(\ker f)$ gives surjectivity of $f^*$ onto $V(\ker f)$. *Example problem:* any integral $f : A \to B$ has $f^*$ surjective onto $\operatorname{Spec} A$ when $f$ is injective.

**Targets (Output Amplification)**

The conclusion is "$\iota^*$ is surjective / the fibre over $\mathfrak{p}$ is non-empty".

Combine surjectivity with **[[Thm - Going Up|going up]]** to lift *chains*, not just points. Lying over plants a prime over the bottom of an ascending chain; going up extends it. The combined result $E$ is that any ascending chain of $A$ lifts to one of $B$ — the half of dimension theory giving $\dim A \leq \dim B$.

Combine the fibre description with **the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain/field criterion]]** to locate *maximal* ideals. The fibre is $\operatorname{mSpec} B_{\mathfrak{p}}$; if $\mathfrak{p}$ is maximal, the primes over it are maximal in $B$ (contraction of maximal is maximal, for integral extensions). The result $E$: over a maximal ideal sit only maximal ideals — closed points map to closed points, the defining feature of finite morphisms.

Combine surjectivity with **[[Thm - Incomparability|incomparability]]** to bound fibre size. Lying over says the fibre is non-empty; incomparability says it is an antichain; module-finiteness says it is finite. The result $E$: every fibre of a finite map is a non-empty finite set, the algebraic form of "a finite map is a finite-to-one cover".

---

# Why Is It True

Strip the theorem to its mechanism and it is almost nothing — which is the point. The question "is there a prime of $B$ over $\mathfrak{p}$?" is, after the right reduction, the question "is a certain ring non-zero?", and that ring is a localization at a set avoiding $0$, so of course it is non-zero.

The reduction is the fibre dictionary. A prime $\mathfrak{q}$ of $B$ with $\mathfrak{q} \cap A = \mathfrak{p}$ is the same data as a prime of $B$ disjoint from $S = A \setminus \mathfrak{p}$ (that is what "$\mathfrak{q} \cap A \subseteq \mathfrak{p}$" means) *and* containing $\mathfrak{p}$ (that is the reverse inclusion). Localizing $B$ at $S$ throws away exactly the primes meeting $S$, leaving the primes with $\mathfrak{q} \cap A \subseteq \mathfrak{p}$; among those, the ones with $\mathfrak{q} \cap A = \mathfrak{p}$ *exactly* are the maximal ones, because in the integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ a prime contracts to the maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$ iff it is itself maximal (domain criterion). So the fibre is $\operatorname{mSpec} B_{\mathfrak{p}}$.

Now the punchline. **The only way the fibre could be empty is for $B_{\mathfrak{p}}$ to have no maximal ideal — that is, to be the zero ring; but $B_{\mathfrak{p}} = S^{-1}B$ with $0 \notin S$, so $B_{\mathfrak{p}} \neq 0$, and a non-zero ring always has a maximal ideal.** That single sentence is the whole proof. Integrality enters only to upgrade "$\operatorname{Spec} B_{\mathfrak{p}} \neq \varnothing$" to "the fibre $= \operatorname{mSpec} B_{\mathfrak{p}}$" via the domain criterion; the *existence* of a prime is pure localization. This is the same "localize to force a prime into existence" move that powers the radical-equals-intersection-of-primes theorem in [[Commutative Algebra IV — Localization|the localization chapter]].

---

# What Makes This Hard

The difficulty is entirely conceptual, not technical: one must see that the *fibre* over $\mathfrak{p}$ is $\operatorname{mSpec} B_{\mathfrak{p}}$ — the *maximal* spectrum of the localization, not its full spectrum — and that $B_{\mathfrak{p}}$ is "$B$ localized at a subset of $A$", an unfamiliar object that is not a local ring. The most common error is to localize at a prime *of $B$* (which begs the question) or to forget that one needs $\mathfrak{q} \cap A = \mathfrak{p}$ *exactly*, settling for $\subseteq$ and so landing on $\operatorname{Spec} B_{\mathfrak{p}}$ rather than $\operatorname{mSpec} B_{\mathfrak{p}}$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Identify the fibre over $\mathfrak{p}$ with $\operatorname{mSpec} B_{\mathfrak{p}}$ using the prime-correspondence theorem for the localization $B \to B_{\mathfrak{p}}$ together with the domain criterion (contraction of maximal is maximal for the integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$). Then observe $B_{\mathfrak{p}} \neq 0$, so it has a maximal ideal, so the fibre is non-empty.

**Subgoal decomposition:**

1. **Set up the localization $B_{\mathfrak{p}} = S^{-1}B$, $S = A \setminus \mathfrak{p}$, and note $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral.**
   - *Hint:* Integrality is stable under localization by a multiplicative subset of $A$.
   - *Why needed:* It lets the domain criterion apply inside $B_{\mathfrak{p}}$.

2. **Show the fibre $\{\mathfrak{q} : \mathfrak{q} \cap A = \mathfrak{p}\}$ corresponds to $\operatorname{mSpec} B_{\mathfrak{p}}$.**
   - *Hint:* The localization correspondence gives $\{\mathfrak{q} : \mathfrak{q} \cap A \subseteq \mathfrak{p}\} \leftrightarrow \operatorname{Spec} B_{\mathfrak{p}}$; restrict to $\mathfrak{q} \cap A = \mathfrak{p}$, which by the domain criterion is exactly $\mathfrak{q}B_{\mathfrak{p}}$ contracting to the maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$ of $A_{\mathfrak{p}}$, i.e. $\mathfrak{q}B_{\mathfrak{p}}$ maximal.
   - *Why needed:* It converts "non-empty fibre" into "$B_{\mathfrak{p}}$ has a maximal ideal".

3. **Conclude $B_{\mathfrak{p}} \neq 0$, so $\operatorname{mSpec} B_{\mathfrak{p}} \neq \varnothing$.**
   - *Hint:* $S^{-1}B = 0 \iff 0 \in S$; here $0 \notin A \setminus \mathfrak{p}$.
   - *Why needed:* It supplies the existence of the prime, finishing the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: The localized extension stays integral
> **Statement:** If $A \subseteq B$ is integral and $S \subseteq A$ is multiplicative, then $S^{-1}A \subseteq S^{-1}B$ is integral.
>
> **Hint:** Take $b \in B$ integral over $A$ with $b^n + a_1 b^{n-1} + \cdots + a_n = 0$; divide the equation for $b/s$ by suitable powers of $s$ to get a monic equation over $S^{-1}A$.
>
> **Why needed:** It puts the integral hypothesis inside $B_{\mathfrak{p}}$, where the domain criterion is applied.
>
> > [!note]- Full proof
> > Let $b/s \in S^{-1}B$ with $b \in B$, $s \in S$. As $b$ is integral over $A$, there are $a_i \in A$ with $b^n + a_1 b^{n-1} + \cdots + a_n = 0$. Divide by $s^n$:
> > $$\left(\tfrac{b}{s}\right)^n + \tfrac{a_1}{s}\left(\tfrac{b}{s}\right)^{n-1} + \tfrac{a_2}{s^2}\left(\tfrac{b}{s}\right)^{n-2} + \cdots + \tfrac{a_n}{s^n} = 0,$$
> > a monic equation for $b/s$ with coefficients $a_i/s^i \in S^{-1}A$. Hence $b/s$ is integral over $S^{-1}A$, and as $b/s$ was arbitrary, $S^{-1}A \subseteq S^{-1}B$ is integral.

> [!note]- Lemma 2: The fibre is $\operatorname{mSpec} B_{\mathfrak{p}}$
> **Statement:** Extension and contraction along $B \to B_{\mathfrak{p}}$ give a bijection $\{\mathfrak{q} \in \operatorname{Spec} B : \mathfrak{q} \cap A = \mathfrak{p}\} \leftrightarrow \operatorname{mSpec} B_{\mathfrak{p}}$.
>
> **Hint:** Use the localization prime-correspondence to reduce to $\mathfrak{q} \cap A \subseteq \mathfrak{p}$, then the domain criterion to single out $\mathfrak{q} \cap A = \mathfrak{p}$ as maximality of $\mathfrak{q}B_{\mathfrak{p}}$.
>
> **Why needed:** It is the dictionary turning the existence of a prime over $\mathfrak{p}$ into the existence of a maximal ideal of $B_{\mathfrak{p}}$.
>
> > [!note]- Full proof
> > By the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]] applied to the localization $B \to B_{\mathfrak{p}} = S^{-1}B$, extension $\mathfrak{q} \mapsto \mathfrak{q}B_{\mathfrak{p}}$ and contraction give a bijection $\{\mathfrak{q} \in \operatorname{Spec} B : \mathfrak{q} \cap S = \varnothing\} \leftrightarrow \operatorname{Spec} B_{\mathfrak{p}}$. Now $\mathfrak{q} \cap S = \varnothing$ means $\mathfrak{q} \cap (A \setminus \mathfrak{p}) = \varnothing$, i.e. $\mathfrak{q} \cap A \subseteq \mathfrak{p}$. So this bijection restricts the primes of $B$ to those with $\mathfrak{q} \cap A \subseteq \mathfrak{p}$. Among these, take $\mathfrak{q}$ with $\mathfrak{q} \cap A = \mathfrak{p}$. By the [[Thm - Prime Ideals of a Localization|localization theorem]] applied to $A$, $(\mathfrak{q}B_{\mathfrak{p}}) \cap A_{\mathfrak{p}} = (\mathfrak{q} \cap A)A_{\mathfrak{p}} = \mathfrak{p}A_{\mathfrak{p}}$, which is the unique maximal ideal of the local ring $A_{\mathfrak{p}}$. By Lemma 1 the extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral, so by the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain/field criterion]] (contraction of maximal is maximal, and conversely), $\mathfrak{q}B_{\mathfrak{p}}$ contracts to a maximal ideal of $A_{\mathfrak{p}}$ if and only if $\mathfrak{q}B_{\mathfrak{p}}$ is itself maximal in $B_{\mathfrak{p}}$. Hence $\mathfrak{q} \cap A = \mathfrak{p} \iff \mathfrak{q}B_{\mathfrak{p}} \in \operatorname{mSpec} B_{\mathfrak{p}}$, and the bijection restricts as claimed.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A \subseteq B$ be an integral extension and $\mathfrak{p} \in \operatorname{Spec} A$. Set $S = A \setminus \mathfrak{p}$, a multiplicative subset of $A$ (and of $B$) because $\mathfrak{p}$ is prime, and $B_{\mathfrak{p}} = S^{-1}B$.
>
> **Step 0 — $B_{\mathfrak{p}}$ is a non-zero ring.** Since $\mathfrak{p}$ is a proper ideal, $0 \in \mathfrak{p}$, so $0 \notin A \setminus \mathfrak{p} = S$. A localization $S^{-1}B$ is the zero ring if and only if $0 \in S$; hence $B_{\mathfrak{p}} \neq 0$.
>
> **Step 1 — the fibre over $\mathfrak{p}$ equals $\operatorname{mSpec} B_{\mathfrak{p}}$.** By Lemma 1, $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral. By Lemma 2, extension and contraction along $B \to B_{\mathfrak{p}}$ give a bijection
> $$\{\mathfrak{q} \in \operatorname{Spec} B : \mathfrak{q} \cap A = \mathfrak{p}\} \;\longleftrightarrow\; \operatorname{mSpec} B_{\mathfrak{p}}.$$
>
> **Step 2 — conclude.** As $B_{\mathfrak{p}} \neq 0$, it has at least one maximal ideal $\mathfrak{m}$ (every non-zero ring does, by Zorn's lemma). By Step 1, $\mathfrak{m} = \mathfrak{q}B_{\mathfrak{p}}$ for a prime $\mathfrak{q} \in \operatorname{Spec} B$ with $\mathfrak{q} \cap A = \mathfrak{p}$. Thus the fibre over $\mathfrak{p}$ is non-empty: a prime of $B$ lies over $\mathfrak{p}$. Since $\mathfrak{p}$ was arbitrary, $\iota^* : \operatorname{Spec} B \to \operatorname{Spec} A$ is surjective. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Existence of primes above a rational prime in a number ring.** For a number field $K$ with ring of integers $\mathcal{O}_K$, the extension $\mathbb{Z} \subseteq \mathcal{O}_K$ is integral, so lying over guarantees that every rational prime $(p)$ has at least one prime of $\mathcal{O}_K$ over it. This is the existence half of "primes split in number fields", and it is non-obvious that it requires *no* computation — purely that $\mathcal{O}_K$ is integral over $\mathbb{Z}$ and a localization is non-zero.

**Surjectivity of a finite map of affine varieties onto its target.** For a module-finite $k$-algebra map $A \hookrightarrow B$ of coordinate rings, lying over says the finite morphism $\operatorname{Spec} B \to \operatorname{Spec} A$ hits every point. Applied after Noether normalization — $A$ finite over $k[X_1,\dots,X_d]$ — it says the projection of a variety onto an affine space (normalizing coordinates) is *onto*, the geometric statement that a variety of dimension $d$ genuinely covers $\mathbb{A}^d$. The application is non-obvious because surjectivity of a projection usually fails (e.g. the hyperbola misses the origin) — integrality is exactly what rescues it.

**A non-zero finitely generated module over a local ring is non-zero after reduction.** Recasting Step 0: the non-vanishing of $B_{\mathfrak{p}}$ is the statement that localizing a non-zero ring at a multiplicative set avoiding $0$ keeps it non-zero. The same "non-zero ring has a maximal ideal" engine recurs in proving that the support of a module is non-empty and that $\operatorname{Spec}$ of a non-zero ring is non-empty — the foundational existence statements of commutative algebra.

---

# Bridges

- **[[Thm - Going Up|Going Up]]** — lying over is the base case of going up and is *implied by* it; conversely going up is *proved from* lying over by passing to the quotient extension $A/\mathfrak{p}_1 \subseteq B/\mathfrak{q}_1$ and applying lying over there. The two together lift ascending chains, which is why they are always invoked as a pair when bounding dimension from below.

- **[[Thm - Incomparability|Incomparability]]** — lying over gives a non-empty fibre; incomparability gives that the fibre is an antichain (zero-dimensional). Combined with module-finiteness (so the fibre ring is finite over a field), they say every fibre of a finite map is a non-empty finite set — the precise sense in which a finite map is finite-to-one and onto.

- **[[Thm - The Radical is the Intersection of the Primes Above It|Radical equals intersection of primes]]** — the proof here is the same manoeuvre as in that theorem: localize to force a prime into existence in a non-zero ring. The shared engine is "$S^{-1}R \neq 0 \iff 0 \notin S$, and a non-zero ring has a maximal ideal", the single most-used existence tool across commutative algebra.

- **[[Thm - Prime Ideals of a Localization|Prime ideals of a localization]]** — this is the dictionary that identifies the fibre with $\operatorname{mSpec} B_{\mathfrak{p}}$: primes of $S^{-1}B$ correspond to primes of $B$ disjoint from $S$, and the domain criterion picks out the maximal ones as the fibre. Without it, the fibre would be an inert set of primes rather than the spectrum of one computable ring.

---

# Unlocked by This

> [!tip] Surjectivity of finite morphisms *(from Algebraic Geometry)*
> Lying over is the algebraic content of "a **finite morphism of varieties** is surjective onto its image" — equivalently, with going up, that finite morphisms are surjective and closed, hence **proper**. The branched cover $\operatorname{Spec}\mathbb{Z}[i] \to \operatorname{Spec}\mathbb{Z}$ and the projection of a normalized variety to affine space are the prototypes; the general theory of proper and finite morphisms of **schemes** is the upgrade.
