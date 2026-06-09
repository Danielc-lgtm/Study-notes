---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Multiplicative Set and Localization"
  - "Def - Extension and Contraction of Ideals"
  - "Def - The Prime Spectrum (Spec)"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $S \subseteq R$ be a [[Def - Multiplicative Set and Localization|multiplicative subset]] and $\iota : R \to S^{-1}R$, $r\mapsto\tfrac r1$, the localization map; [[Def - Extension and Contraction of Ideals|extension]] $(-)^e = S^{-1}(-)$ and [[Def - Extension and Contraction of Ideals|contraction]] $(-)^c = \iota^{-1}(-)$ are taken along $\iota$. We write $\operatorname{Spec} R$ for the set of [[Def - Prime and Maximal Ideal|prime ideals]], $\mathfrak{p},\mathfrak{q}$ for primes, $\mathfrak{a}$ for a general ideal of $R$, $\mathfrak{b}$ for an ideal of $S^{-1}R$. The two key cases are $S = R\setminus\mathfrak{p}$ (giving $R_{\mathfrak{p}}$) and $S = \{f^n\}$ (giving $R_f$). The full registry is on [[Commutative Algebra IV — Localization]].

---

# Statement

> **Theorem (Prime ideals of a localization; Becker Prop. 4.16).** Let $S\subseteq R$ be multiplicative and $\iota : R\to S^{-1}R$ the localization map. Then:
> 1. **(Every ideal is extended.)** Every ideal $\mathfrak{b}\trianglelefteq S^{-1}R$ satisfies $\mathfrak{b} = \mathfrak{b}^{ce} = (\mathfrak{b}^c)^e$.
> 2. **(Contracted ideals.)** An ideal $\mathfrak{a}\trianglelefteq R$ is contracted ($\mathfrak{a} = \mathfrak{a}^{ec}$) if and only if the image $\bar S$ of $S$ in $R/\mathfrak{a}$ contains no zero-divisor.
> 3. **(Unit detection.)** $\mathfrak{a}^e = S^{-1}R$ if and only if $\mathfrak{a}\cap S\neq\varnothing$.
> 4. **(The prime correspondence.)** Extension and contraction are mutually inverse, inclusion-preserving bijections
> $$\{\mathfrak{p}\in\operatorname{Spec} R : \mathfrak{p}\cap S = \varnothing\} \;\xrightarrow{\ \sim\ }\; \operatorname{Spec}(S^{-1}R), \qquad \mathfrak{p}\mapsto\mathfrak{p}^e = S^{-1}\mathfrak{p}, \qquad \mathfrak{q}^c\mapsfrom\mathfrak{q}.$$

> **Corollary (the two cases).** For $S = R\setminus\mathfrak{p}$: $\operatorname{Spec}(R_{\mathfrak{p}}) = \{\mathfrak{q}^e : \mathfrak{q}\subseteq\mathfrak{p}\}$, so $R_{\mathfrak{p}}$ is local with unique maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$. For $S = \{f^n\}$: $\operatorname{Spec}(R_f) = \{\mathfrak{q}^e : f\notin\mathfrak{q}\} \cong D(f)$, the open set where $f\neq 0$.

---

# Motivation

This is the geometric soul of the chapter. Everything before it — fractions, the universal property, exactness — was machinery; this theorem says what localization *does to space*. The answer is as clean as one could wish: **localizing does not scramble the prime spectrum, it carves out a clean piece of it.** The primes of $S^{-1}R$ are exactly the primes of $R$ that avoid $S$, with every inclusion relation preserved. So $\operatorname{Spec}(S^{-1}R)$ is literally a sub-poset of $\operatorname{Spec} R$ — a subspace, not a distortion.

Once you have this, the two pillars of the chapter fall out instantly. Take $S = R\setminus\mathfrak{p}$: the primes avoiding $S$ are exactly the primes *contained in* $\mathfrak{p}$, and among them $\mathfrak{p}$ itself is the largest — so $R_{\mathfrak{p}}$ has a unique maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$ and is therefore **local**. This is *why* localizing at a prime produces a local ring; it is not a separate fact but a reading of the prime correspondence. Geometrically, the primes $\subseteq\mathfrak{p}$ are exactly the points of an arbitrarily small neighbourhood of $\mathfrak{p}$ — the points that specialise to $\mathfrak{p}$ or generalise from it within the local picture — so $R_{\mathfrak{p}}$ sees a neighbourhood of the point. Take $S = \{f^n\}$ instead: the primes avoiding $S$ are the primes *not containing* $f$, which is exactly the basic open set $D(f) = \{\mathfrak{q} : f\notin\mathfrak{q}\}$. So $\operatorname{Spec}(R_f) \cong D(f)$, and **inverting $f$ is restricting to the open set where $f\neq 0$**.

The slogan to carry is that localization is a *faithful zoom*: it isolates a piece of the geometry — a point's neighbourhood, or an open set — without distorting what it isolates. This is the precise content behind "commutative algebra is the local study of algebraic geometry", and it is the theorem that lets the structure sheaf be built, since $D(f)\cong\operatorname{Spec}(R_f)$ is exactly the statement that the basic opens are themselves spectra of localizations.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is *a localization whose primes, maximal ideal, or dimension you want to understand*.

The first disguised source is **"what is the maximal ideal / are the primes / is the dimension of this local ring?"**. Property $B$: a localization $R_{\mathfrak{p}}$ or $S^{-1}R$ is given and a spectral question is asked. The bridge is part 4: translate to "which primes of $R$ avoid $S$", an entirely $R$-side computation. The non-obvious value: you never look inside $S^{-1}R$; you list primes of $R$. *Example problem:* find the maximal ideal of $R_{\mathfrak{p}}$ — it is the extension of the largest prime $\subseteq\mathfrak{p}$, namely $\mathfrak{p}$ itself.

The second disguised source is **"is this localization local?" or "is it a field?"**. Property $B$: you must decide whether $S^{-1}R$ has a unique maximal ideal (or only $(0)$). The bridge is counting survivors: a unique maximal survivor means local; only $(0)$ surviving means a field (e.g. $R_{(0)} = \operatorname{Frac} R$ for a domain). The non-obviousness: locality is a *counting* statement about the surviving primes. *Example problem:* $R_{\mathfrak{p}}$ is local because $\mathfrak{p}$ is the unique maximal survivor — see [[Ex - Localizing at a prime gives a local ring]].

The third disguised source is **"restrict a geometric/spectral statement to an open set or a neighbourhood"**. Property $B$: a question about $D(f)$ or a neighbourhood of a point. The bridge is $\operatorname{Spec}(R_f)\cong D(f)$ and "$\operatorname{Spec}(R_{\mathfrak{p}})$ is a neighbourhood of $\mathfrak{p}$". The non-obvious value: open-set questions become localization questions. *Example problem:* the basic opens form a basis because each is a spectrum of a localization — see [[Ex - The prime spectrum of a localization]].

**Targets (Output Amplification)**

The conclusion is *the bijection between survivor primes of $R$ and all primes of $S^{-1}R$*.

Combine the correspondence with **chains of primes**. Because the bijection preserves inclusions, a chain $\mathfrak{p}_0\subsetneq\dots\subsetneq\mathfrak{p}_n$ of survivors corresponds to a chain in $\operatorname{Spec}(S^{-1}R)$. The further result $E$: $\dim R_{\mathfrak{p}} = \operatorname{ht}\mathfrak{p}$ (the height of $\mathfrak{p}$, the length of the longest chain below it), and $\dim R_f \leq \dim R$. Nonobvious because it connects localization to the dimension theory of [[Commutative Algebra XII — Dimension Theory]].

Combine with **"$\mathfrak{q}^c$ is prime and survives"**. The contraction of any prime of $S^{-1}R$ is a prime of $R$ disjoint from $S$, giving a *section* of "$\operatorname{Spec} R\to$ points". The further result $E$: a way to *manufacture* a prime of $R$ avoiding $S$ from any prime of $S^{-1}R$ — and since $S^{-1}R\neq 0$ has a maximal ideal whenever $0\notin S$, this produces primes avoiding $S$ on demand. Nonobvious because it is the existence half of "$R_x\neq 0\Rightarrow$ a prime misses $x$", the lever of the [[Thm - The Radical is the Intersection of the Primes Above It|radical theorem]].

Combine with **"every ideal is extended"** and a quotient. Since every ideal of $S^{-1}R$ is $\mathfrak{a}^e$, and $S^{-1}R/\mathfrak{a}^e \cong S^{-1}(R/\mathfrak{a})$ (with $\bar S$ the image of $S$), spectral questions about quotients of localizations reduce to localizations of quotients. The further result $E$: the local ring of a point on a subvariety, $R_{\mathfrak{p}}/\mathfrak{q}R_{\mathfrak{p}}\cong(R/\mathfrak{q})_{\mathfrak{p}}$. Nonobvious because it combines this theorem with [[Thm - Localization Commutes with Quotients and Finite Operations|localization-quotient commutation]].

---

# Why Is It True

The whole theorem turns on one disjointness equivalence: **a prime $\mathfrak{p}$ survives localization (i.e. $\mathfrak{p}^e$ is a proper prime and $\mathfrak{p}^{ec} = \mathfrak{p}$) if and only if $\mathfrak{p}\cap S = \varnothing$.** Read each direction.

If $\mathfrak{p}\cap S\neq\varnothing$, pick $x\in\mathfrak{p}\cap S$. Then $\tfrac xx = 1\in\mathfrak{p}^e$, so the extension is the whole ring — $\mathfrak{p}$ does *not* survive, it blows up. (This is part 3: meeting $S$ makes the extension improper, because you have inverted an element of the ideal.) Conversely, if $\mathfrak{p}\cap S = \varnothing$, two things happen. First, $\mathfrak{p}^e$ is proper (again part 3). Second, $\mathfrak{p}^e$ is prime: take $\tfrac{x_1}{s_1}\tfrac{x_2}{s_2}\in\mathfrak{p}^e$, clear denominators to land $x_1 x_2$ (times a unit-to-be from $S$) in $\mathfrak{p}$, use primality of $\mathfrak{p}$ to put $x_1$ or $x_2$ in $\mathfrak{p}$, hence $\tfrac{x_i}{s_i}\in\mathfrak{p}^e$. And $\mathfrak{p}^{ec} = \mathfrak{p}$ because $\mathfrak{p}$ is contracted (part 2: $R/\mathfrak{p}$ is a domain, so $\bar S$ has no zero-divisors exactly when $\bar 0\notin\bar S$, i.e. $\mathfrak{p}\cap S = \varnothing$).

**One-line mechanism: $\mathfrak{p}$ survives $\iff\mathfrak{p}\cap S=\varnothing$ — meeting $S$ inverts an element of $\mathfrak{p}$ and detonates the extension; avoiding $S$ keeps $R/\mathfrak{p}$ a domain so the extension stays prime and the round-trip is the identity.**

The bijection is then bookkeeping. Going down ($\mathfrak{q}\mapsto\mathfrak{q}^c$): contraction of a prime is always prime ([[Def - Extension and Contraction of Ideals|general fact]]), and $\mathfrak{q}^c\cap S = \varnothing$ because any $s\in\mathfrak{q}^c\cap S$ would give $\tfrac s1\in\mathfrak{q}$ with $\tfrac s1$ a unit, forcing $\mathfrak{q} = S^{-1}R$, contradiction. Going up ($\mathfrak{p}\mapsto\mathfrak{p}^e$): just shown to land in $\operatorname{Spec}(S^{-1}R)$. The two round trips are identities: $\mathfrak{q}^{ce} = \mathfrak{q}$ because *every ideal of $S^{-1}R$ is extended* (part 1, itself from $\mathfrak{b}\supseteq\mathfrak{b}^{ce}$ always, and $\subseteq$ here by clearing denominators), and $\mathfrak{p}^{ec} = \mathfrak{p}$ for survivors as above.

Part 1 — every ideal extended — is the cleanest piece: given $\mathfrak{b}\trianglelefteq S^{-1}R$ and $\tfrac rs\in\mathfrak{b}$, multiply by the unit $\tfrac s1$ to get $\tfrac r1\in\mathfrak{b}$, so $r\in\mathfrak{b}^c$, so $\tfrac rs = \tfrac1s\cdot\tfrac r1\in(\mathfrak{b}^c)^e$. Every element of $\mathfrak{b}$ is built from a numerator already in $\mathfrak{b}^c$. **This is the structural reason localization is so faithful: you cannot have an ideal in the localization without its numerators forming an ideal downstairs.**

---

# What Makes This Hard

The crux is internalising the disjointness dichotomy and *which* direction each implication runs: meeting $S$ *destroys* the prime (extension becomes the unit ideal), avoiding $S$ *preserves* it. People reverse this. The second subtlety is proving $\mathfrak{p}^e$ is genuinely prime when $\mathfrak{p}\cap S = \varnothing$ — the clearing-denominator step $\tfrac{x_1 x_2}{s_1 s_2} = \tfrac pt\Rightarrow ut x_1 x_2 = us_1 s_2 p\in\mathfrak{p}$ with $ut\notin\mathfrak{p}$, so $x_1 x_2\in\mathfrak{p}$ — is fiddly and easy to botch. The common error is to assume $\mathfrak{p}^e = S^{-1}\mathfrak{p}$ is automatically prime; it is not, primality of $\mathfrak{p}$ and disjointness from $S$ are both needed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Establish the three preparatory facts — every ideal of $S^{-1}R$ is extended (part 1), the unit-detection criterion $\mathfrak{a}^e = S^{-1}R\iff\mathfrak{a}\cap S\neq\varnothing$ (part 3), and contractedness via zero-divisors in $R/\mathfrak{a}$ (part 2). Then assemble the bijection: contraction sends primes to disjoint primes, extension sends disjoint primes to primes, and the two round trips are identities by parts 1 and 2.

**Subgoal decomposition:**

1. **Every ideal extended.** Show $\mathfrak{b} = (\mathfrak{b}^c)^e$.
   - *Hint:* $\tfrac rs\in\mathfrak{b}\Rightarrow\tfrac r1 = \tfrac s1\cdot\tfrac rs\in\mathfrak{b}\Rightarrow r\in\mathfrak{b}^c\Rightarrow\tfrac rs\in(\mathfrak{b}^c)^e$; reverse inclusion always holds.
   - *Why needed:* gives $\mathfrak{q}^{ce} = \mathfrak{q}$, one of the two round-trips.

2. **Unit detection.** Show $\mathfrak{a}^e = S^{-1}R\iff\mathfrak{a}\cap S\neq\varnothing$.
   - *Hint:* if $x\in\mathfrak{a}\cap S$ then $\tfrac xx = 1\in\mathfrak{a}^e$; conversely $1\in\mathfrak{a}^e$ gives $\tfrac11 = \tfrac as$, clear to $us\in\mathfrak{a}\cap S$.
   - *Why needed:* tells you exactly which primes survive (proper extension).

3. **Survivors extend to primes, and the bijection.** Show $\mathfrak{p}\cap S = \varnothing\Rightarrow\mathfrak{p}^e\in\operatorname{Spec}(S^{-1}R)$ with $\mathfrak{p}^{ec} = \mathfrak{p}$; and $\mathfrak{q}^c$ is a disjoint prime.
   - *Hint:* primality of $\mathfrak{p}^e$ by clearing denominators and using $\mathfrak{p}$ prime; $\mathfrak{p}^{ec} = \mathfrak{p}$ since $R/\mathfrak{p}$ a domain makes $\mathfrak{p}$ contracted; $\mathfrak{q}^c\cap S=\varnothing$ else $\mathfrak{q}$ contains a unit.
   - *Why needed:* it is the correspondence; the two cases ($R_{\mathfrak{p}}$, $R_f$) are read off it.

---

# Lemma Decomposition

> [!note]- Lemma 1: Every ideal of $S^{-1}R$ is extended
> **Statement:** For every $\mathfrak{b}\trianglelefteq S^{-1}R$, $\mathfrak{b} = (\mathfrak{b}^c)^e = \mathfrak{b}^{ce}$.
>
> **Hint:** Multiply a fraction in $\mathfrak{b}$ by its denominator (a unit) to land its numerator in $\mathfrak{b}^c$.
>
> **Why needed:** It supplies the round-trip $\mathfrak{q}^{ce} = \mathfrak{q}$ and the statement that $S^{-1}R$'s ideal theory is governed by $R$.
>
> > [!note]- Full proof
> > The inclusion $\mathfrak{b}^{ce}\subseteq\mathfrak{b}$ holds for any ring map. For $\supseteq$: take $\tfrac rs\in\mathfrak{b}$. Since $\tfrac s1\in S^{-1}R$ and $\mathfrak{b}$ is an ideal, $\tfrac s1\cdot\tfrac rs = \tfrac r1\in\mathfrak{b}$, so $r\in\iota^{-1}(\mathfrak{b}) = \mathfrak{b}^c$. Then $\tfrac rs = \tfrac1s\cdot\tfrac r1\in(\mathfrak{b}^c)^e = \mathfrak{b}^{ce}$. Hence $\mathfrak{b}\subseteq\mathfrak{b}^{ce}$, and equality holds.

> [!note]- Lemma 2: Unit detection
> **Statement:** $\mathfrak{a}^e = S^{-1}R\iff\mathfrak{a}\cap S\neq\varnothing$.
>
> **Hint:** A common element of $\mathfrak{a}$ and $S$ is its own inverse-up-to-itself; conversely $1\in\mathfrak{a}^e$ produces one by clearing denominators.
>
> **Why needed:** It is the precise survival criterion: $\mathfrak{p}$ survives iff its extension stays proper iff $\mathfrak{p}\cap S=\varnothing$.
>
> > [!note]- Full proof
> > ($\Leftarrow$) If $x\in\mathfrak{a}\cap S$, then $\tfrac xx = \tfrac11 = 1\in\mathfrak{a}^e$ (as $\tfrac x1\in\mathfrak{a}^e$ and $\tfrac1x\in S^{-1}R$), so $\mathfrak{a}^e = S^{-1}R$.
> >
> > ($\Rightarrow$) If $\mathfrak{a}^e = S^{-1}R$ then $1\in\mathfrak{a}^e = S^{-1}\mathfrak{a}$, so $\tfrac11 = \tfrac as$ for some $a\in\mathfrak{a}$, $s\in S$. Hence $u(s - a) = 0$ for some $u\in S$, i.e. $us = ua$. Now $us\in S$ (multiplicative) and $ua\in\mathfrak{a}$ (ideal), so $us = ua\in\mathfrak{a}\cap S\neq\varnothing$.

> [!note]- Lemma 3: Survivors extend to primes, with $\mathfrak{p}^{ec} = \mathfrak{p}$
> **Statement:** If $\mathfrak{p}\in\operatorname{Spec} R$ and $\mathfrak{p}\cap S = \varnothing$, then $\mathfrak{p}^e\in\operatorname{Spec}(S^{-1}R)$ and $\mathfrak{p}^{ec} = \mathfrak{p}$.
>
> **Hint:** Proper by Lemma 2; prime by clearing denominators into $\mathfrak{p}$ and using primality; contracted because $R/\mathfrak{p}$ is a domain.
>
> **Why needed:** It is the heart of the correspondence — the survivors really do map to primes bijectively.
>
> > [!note]- Full proof
> > By Lemma 2, $\mathfrak{p}^e$ is proper (since $\mathfrak{p}\cap S = \varnothing$). Primality: take $\tfrac{x_1}{s_1},\tfrac{x_2}{s_2}\in S^{-1}R$ with $\tfrac{x_1 x_2}{s_1 s_2}\in\mathfrak{p}^e = S^{-1}\mathfrak{p}$. Then $\tfrac{x_1 x_2}{s_1 s_2} = \tfrac pt$ for some $p\in\mathfrak{p}$, $t\in S$, so $u(t x_1 x_2 - s_1 s_2 p) = 0$ for some $u\in S$, giving $ut\,x_1 x_2 = u s_1 s_2 p\in\mathfrak{p}$. Since $ut\in S$ and $\mathfrak{p}\cap S = \varnothing$, $ut\notin\mathfrak{p}$; as $\mathfrak{p}$ is prime, $x_1 x_2\in\mathfrak{p}$, so $x_1\in\mathfrak{p}$ or $x_2\in\mathfrak{p}$, whence $\tfrac{x_1}{s_1}\in\mathfrak{p}^e$ or $\tfrac{x_2}{s_2}\in\mathfrak{p}^e$. So $\mathfrak{p}^e$ is prime.
> >
> > Contracted: $\mathfrak{p}^{ec} = \bigcup_{s\in S}(\mathfrak{p} : s)$. If $rs\in\mathfrak{p}$ for some $s\in S$, then since $s\notin\mathfrak{p}$ and $\mathfrak{p}$ is prime, $r\in\mathfrak{p}$. So $(\mathfrak{p}:s)\subseteq\mathfrak{p}$ for every $s\in S$, giving $\mathfrak{p}^{ec}\subseteq\mathfrak{p}$; the reverse $\mathfrak{p}\subseteq\mathfrak{p}^{ec}$ always holds. Hence $\mathfrak{p}^{ec} = \mathfrak{p}$.

---

# Formal Proof

> [!note]- Complete formal proof
> **(1) Every ideal is extended.** Lemma 1.
>
> **(3) Unit detection.** Lemma 2.
>
> **(2) Contracted ideals.** $\mathfrak{a}$ is contracted iff $\mathfrak{a}^{ec}\subseteq\mathfrak{a}$ (the reverse always holds), i.e. iff $\bigcup_{s\in S}(\mathfrak{a}:s)\subseteq\mathfrak{a}$, i.e. iff "$rs\in\mathfrak{a}$ for some $s\in S\Rightarrow r\in\mathfrak{a}$". Passing to $R/\mathfrak{a}$ with image $\bar S$ of $S$: this says "$\bar r\,\bar s = \bar 0$ with $\bar s\in\bar S\Rightarrow\bar r = \bar 0$", i.e. no element of $\bar S$ is a zero-divisor in $R/\mathfrak{a}$.
>
> **(4) The prime correspondence.** The contraction of a prime is prime ([[Def - Extension and Contraction of Ideals|general fact]]). For $\mathfrak{q}\in\operatorname{Spec}(S^{-1}R)$, $\mathfrak{q}^c$ is prime; and $\mathfrak{q}^c\cap S = \varnothing$, since $s\in\mathfrak{q}^c\cap S$ would give $\tfrac s1\in\mathfrak{q}$ with $\tfrac s1$ a unit, forcing $\mathfrak{q} = S^{-1}R$, impossible. So contraction maps $\operatorname{Spec}(S^{-1}R)\to\{\mathfrak{p} : \mathfrak{p}\cap S = \varnothing\}$.
>
> Conversely, by Lemma 3, $\mathfrak{p}\cap S = \varnothing\Rightarrow\mathfrak{p}^e\in\operatorname{Spec}(S^{-1}R)$, so extension maps the other way.
>
> The two are mutually inverse: $\mathfrak{q}^{ce} = \mathfrak{q}$ by Lemma 1 (every ideal extended), and $\mathfrak{p}^{ec} = \mathfrak{p}$ for survivors by Lemma 3. Both maps preserve inclusions ($e$ and $c$ are order-preserving). Hence the stated bijection.
>
> **Corollary.** For $S = R\setminus\mathfrak{p}$: $\mathfrak{q}\cap S = \varnothing\iff\mathfrak{q}\subseteq\mathfrak{p}$, so the survivors are exactly the primes $\subseteq\mathfrak{p}$, with $\mathfrak{p}$ the largest; thus $\mathfrak{p}^e = \mathfrak{p}R_{\mathfrak{p}}$ is the unique maximal ideal and $R_{\mathfrak{p}}$ is local. For $S = \{f^n\}$: $\mathfrak{q}\cap S = \varnothing\iff f\notin\mathfrak{q}$ (a power of $f$ in $\mathfrak{q}$ would put $f\in\mathfrak{q}$ by primality), so the survivors are $D(f)$, and $\operatorname{Spec}(R_f)\cong D(f)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Primes of $\mathbb{Z}_{(p)}$ and the height of a prime.** Localizing $\mathbb{Z}$ at $(p)$, the surviving primes are those $\subseteq(p)$: only $(0)$ and $(p)$. So $\operatorname{Spec}(\mathbb{Z}_{(p)}) = \{(0)\subsetneq(p)\mathbb{Z}_{(p)}\}$, a two-element chain, giving $\dim\mathbb{Z}_{(p)} = 1 = \operatorname{ht}(p)$. Nonobvious recognition: the dimension of a local ring is the height of the prime, read directly off the surviving chain.

**Basic opens form a basis for the Zariski topology.** Because $\operatorname{Spec}(R_f)\cong D(f)$ as topological spaces and $D(f)\cap D(g) = D(fg)$, the sets $D(f)$ are a basis closed under finite intersection — exactly the data needed to define a sheaf. Nonobvious because it identifies the open-set lattice of $\operatorname{Spec} R$ with localizations, the foundation of the structure sheaf — see [[Ex - The prime spectrum of a localization]].

**Localizing a number ring at a prime keeps only one prime above.** For $\mathcal{O}_K$ and a prime $\mathfrak{p}$, $(\mathcal{O}_K)_{\mathfrak{p}}$ is a discrete valuation ring with the single nonzero prime $\mathfrak{p}(\mathcal{O}_K)_{\mathfrak{p}}$ — all other primes are inverted away. This is how one studies ramification "one prime at a time". Nonobvious because the global ring has infinitely many primes but the localization isolates exactly one, the geometric content of [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

---

# Bridges

- **[[Def - Extension and Contraction of Ideals|Extension and contraction]]** — this theorem is the spectacular special case of the contracted/extended bijection for the localization map, where it becomes a bijection of *primes* (not just ideals) because every ideal of $S^{-1}R$ is extended and survivor primes are contracted.

- **[[Def - The Prime Spectrum (Spec)|The prime spectrum]]** — the geometric reading: $\operatorname{Spec}(S^{-1}R)\hookrightarrow\operatorname{Spec} R$ is a homeomorphism onto $\{\mathfrak{p} : \mathfrak{p}\cap S = \varnothing\}$, which for $S = \{f^n\}$ is the basic open $D(f)$. Localization realises the open subspace algebraically.

- **[[Def - Local Ring and Residue Field|Local ring]]** — the corollary "$R_{\mathfrak{p}}$ is local with maximal ideal $\mathfrak{p}R_{\mathfrak{p}}$" *is* this theorem applied to $S = R\setminus\mathfrak{p}$: the survivors are the primes $\subseteq\mathfrak{p}$, $\mathfrak{p}$ is the unique maximal survivor, hence the unique maximal ideal.

- **[[Thm - The Radical is the Intersection of the Primes Above It|The radical theorem]]** — uses the contraction half: a prime of the nonzero ring $R_x$ contracts to a prime of $R$ avoiding $x$, manufacturing the prime needed for the $\supseteq$ inclusion of $\sqrt I = \bigcap\mathfrak{p}$.

---

# Unlocked by This

> [!tip] Restriction to an open subscheme; the basic opens as affine charts *(from Algebraic Geometry)*
> The homeomorphism $\operatorname{Spec}(R_f)\cong D(f)$ is the statement that **inverting $f$ is restricting to the open set $D(f)$**, and that every basic open is itself an affine scheme. This is what lets $\operatorname{Spec} R$ be covered by affine charts $\operatorname{Spec}(R_f)$ and the structure sheaf be defined by $\mathcal{O}(D(f)) = R_f$ — the basic opens are the coordinate charts of the scheme, closed under intersection by $D(f)\cap D(g) = D(fg)$. Gluing schemes along such open immersions builds all of scheme theory, and this theorem is the algebraic guarantee that the gluing data is consistent.

> [!tip] Height, codimension, and the local ring of a point *(from Algebraic Geometry / Dimension Theory)*
> Because the correspondence preserves inclusions, $\dim R_{\mathfrak{p}} = \operatorname{ht}\mathfrak{p}$ — the dimension of the local ring at a point equals the **codimension** of the corresponding subvariety. A closed point of a surface has a $2$-dimensional local ring; the generic point of a curve on the surface has a $1$-dimensional local ring. This is the bridge from localization to the dimension theory of [[Commutative Algebra XII — Dimension Theory]], where Krull's principal ideal theorem ("a hypersurface drops dimension by one") is proved by localizing and counting surviving primes.
