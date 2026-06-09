---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Dedekind Domain"
  - "Def - Discrete Valuation and Valuation Ring"
  - "Def - Integral Closure and Normal Domain"
  - "Def - Primary Ideal"
  - "Thm - Characterization of Discrete Valuation Rings"
  - "Thm - Prime Ideals of a Localization"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A$ be a [[Def - Dedekind Domain|Dedekind domain]] with fraction field $K$, and $\mathfrak{p}$ a nonzero (hence maximal) prime ideal. We write $A_\mathfrak{p} = (A\setminus\mathfrak{p})^{-1}A$ for the [[Def - Multiplicative Set and Localization|localization]] at $\mathfrak{p}$, with unique maximal ideal $\mathfrak{p}A_\mathfrak{p}$, and $\iota : A \to A_\mathfrak{p}$ for the localization map. An ideal $\mathfrak{q}$ is **[[Def - Primary Ideal|𝔭-primary]]** if $\sqrt{\mathfrak{q}} = \mathfrak{p}$ and $xy\in\mathfrak q,\,x\notin\mathfrak q\Rightarrow y\in\mathfrak p$; the contraction is $\mathfrak{q}^c = \iota^{-1}(\mathfrak{q}A_\mathfrak{p})$. The full registry is on [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

---

# Statement

> **Theorem (localization of a Dedekind domain).** Let $A$ be a Dedekind domain and $\mathfrak{p}$ a nonzero prime ideal. Then the localization $A_\mathfrak{p}$ is a [[Def - Discrete Valuation and Valuation Ring|discrete valuation ring]].

> **Companion fact (contraction of primary ideals).** For a multiplicative set $S$ with $S \cap \mathfrak{p} = \varnothing$ and a $\mathfrak{p}$-primary ideal $\mathfrak{q}$, $\mathfrak{q}$ is contracted from $S^{-1}A$: $\mathfrak{q} = (\mathfrak{q}\,S^{-1}A)^c$. In particular, with $S = A\setminus\mathfrak{p}$, every $\mathfrak{p}$-primary ideal — every power $\mathfrak{p}^n$ — is recovered from its extension to $A_\mathfrak{p}$.

---

# Motivation

This theorem is the bridge between the local and global theory, and it is the workhorse of the whole chapter even though its statement is a one-liner. The definition of a Dedekind domain already says, in its second form, that $A_\mathfrak{p}$ is a DVR for every nonzero prime — so in one sense this theorem *is* (half of) the definition. But stated as a theorem it earns its keep: it is the licence to compute. Every difficult global question about ideals — "what is the prime factorization of $\mathfrak{a}$?", "what is the exponent of $\mathfrak{p}$ in $\mathfrak{a}$?", "is $\mathfrak{a}$ a power of $\mathfrak{p}$?" — is hard in the complicated global ring $A$ but *trivial* in the DVR $A_\mathfrak{p}$, where every nonzero ideal is just a power of the maximal ideal and is measured by a single integer, the valuation. This theorem says you are always allowed to make that reduction.

The companion fact is what makes the reduction *reversible*, and it is the technically delicate half. Localizing computes the local exponent $v_\mathfrak{p}(\mathfrak{a})$; but to conclude anything about the *global* ideal $\mathfrak{a}$ you must be able to come back — to recover $\mathfrak{p}^n$ from $\mathfrak{p}^nA_\mathfrak{p}$. That recovery is exactly the statement that $\mathfrak{p}$-primary ideals are contracted from $A_\mathfrak{p}$, and it works because the multiplicative set $A\setminus\mathfrak{p}$ misses $\mathfrak{p}$, so it cannot introduce or erase any $\mathfrak{p}$-local information. Without this companion fact, localization would be a one-way street and the global factorization theorem would not follow.

So this theorem is best thought of as the formal foundation of the slogan **"to factor an ideal, localize at each prime, count in the DVR, and contract back"**. It is the reason a Dedekind domain, however globally complicated, is locally as simple as $\mathbb{Z}_{(p)}$ at every point — and the reason the local-to-global method works flawlessly in dimension one.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A$ Dedekind, $\mathfrak{p}$ a nonzero prime". The disguises are about recognizing the Dedekind hypothesis and the right prime.

The first disguised source is **a ring of integers and a prime above $p$**. The property $B$ is "$A = \mathcal{O}_K$ and $\mathfrak{p} \mid (p)$". The bridge: $\mathcal{O}_K$ is Dedekind, so $A_\mathfrak{p}$ is a DVR — the **local ring at $\mathfrak{p}$**, the setting for local number theory and the $\mathfrak{p}$-adic valuation $v_\mathfrak{p}$. The non-obvious value is that the global arithmetic of $K$ is studied *one prime at a time* in these DVRs, then reassembled. *Example problem:* compute $v_\mathfrak{p}(6)$ for a prime $\mathfrak{p}$ over $2$ in $\mathbb{Z}[\sqrt{-5}]$.

The second disguised source is **a smooth affine curve and a point on it**. The property $B$ is "$A$ is the coordinate ring of a smooth curve and $\mathfrak{p}$ a closed point". The bridge: such $A$ is Dedekind, so $A_\mathfrak{p}$ is a DVR — the **local ring at the point**, whose valuation is order of vanishing. The non-obviousness: a *geometric* localization (restricting functions to a neighbourhood of a point) produces exactly the algebraic DVR. *Example problem:* the order of vanishing of a function at a point of an elliptic curve.

The third disguised source is **any Noetherian integrally closed domain of dimension $1$**. The property $B$ is the three Dedekind axioms verified directly. The bridge is immediate, but recognizing the axioms in a concretely-presented ring is the skill. *Example problem:* localize $\mathbb{Z}[\sqrt{2}]$ at a prime and confirm it is a DVR.

**Targets (Output Amplification)**

The conclusion is "$A_\mathfrak{p}$ is a DVR (with valuation $v_\mathfrak{p}$), and $\mathfrak{p}$-primary ideals contract cleanly".

Combine "$A_\mathfrak{p}$ is a DVR" with **the contraction fact, to compute global exponents**. Localizing $\mathfrak{a}$ gives $(\mathfrak{p}A_\mathfrak{p})^e$ with $e = v_\mathfrak{p}(\mathfrak{a})$, and contraction recovers $\mathfrak{p}^e$. The further result $E$: the exponent of $\mathfrak{p}$ in the global factorization of $\mathfrak{a}$ is computed in the DVR — this is the engine of [[Thm - A Dedekind Domain has Unique Factorization of Ideals|unique factorization of ideals]]. Nonobvious because it converts a global factorization problem into integer arithmetic.

Combine "$A_\mathfrak{p}$ is a DVR" with **a finitely generated module over $A$**. After localizing, $M_\mathfrak{p}$ is a module over a DVR (a local PID), so $M_\mathfrak{p} \cong A_\mathfrak{p}^r \oplus \bigoplus A_\mathfrak{p}/(\pi^{n_i})$ — the structure theorem applies locally. The further result $E$: the local structure of any $A$-module at $\mathfrak{p}$ is completely classified, recovering torsion and rank prime by prime. Nonobvious because module theory over a Dedekind domain is governed by its DVR localizations.

Combine "$A_\mathfrak{p}$ is a DVR" with **the local–global principle**. A property checked in every $A_\mathfrak{p}$ — itself a DVR — assembles to a global statement. The further result $E$: facts that are easy over DVRs (e.g. every finitely generated torsion-free module is free over a DVR) glue to facts over $A$ (every finitely generated torsion-free $A$-module is **projective**, locally free of constant rank). Nonobvious because local triviality plus the local–global principle yields global projectivity.

---

# Why Is It True

The intuition is that **localizing a Dedekind domain at a prime keeps only the data near that one point, and "near one point" of a one-dimensional smooth space is exactly a DVR.**

**The bolded mechanism:** **$A_\mathfrak{p}$ inherits all four DVR hypotheses for free — Noetherian (localization of Noetherian), local with one nonzero prime (the localization carves out exactly the primes inside $\mathfrak{p}$, namely $(0)$ and $\mathfrak{p}$), dimension $1$, and integrally closed (normality is a local property) — and the DVR characterization theorem then upgrades "Noetherian local domain of dimension $1$ that is integrally closed" to "DVR".**

Trace each inheritance. *Noetherian:* a localization of a Noetherian ring is Noetherian (ideals of $A_\mathfrak{p}$ are extended from ideals of $A$, which are finitely generated). *Local of dimension $1$:* by the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]], the primes of $A_\mathfrak{p}$ are exactly the primes of $A$ contained in $\mathfrak{p}$; since $\dim A = 1$, these are just $(0)$ and $\mathfrak{p}$, so $A_\mathfrak{p}$ is local with maximal ideal $\mathfrak{p}A_\mathfrak{p}$ and $\dim A_\mathfrak{p} = \operatorname{ht}\mathfrak{p} = 1$. *Domain:* a localization of a domain is a domain. *Integrally closed:* this is the one that uses the Dedekind hypothesis essentially — $A$ is integrally closed, and being integrally closed is a *local property*, so $A_\mathfrak{p}$ is integrally closed too.

Now $A_\mathfrak{p}$ is a Noetherian, integrally closed, local domain of dimension $1$. By the [[Thm - Characterization of Discrete Valuation Rings|DVR characterization theorem]], such a ring *is* a DVR — that theorem's whole point is that these four conditions force the existence of a uniformizer and a valuation. So the localization theorem is really a corollary of the characterization theorem plus the locality of normality; the work was front-loaded into proving the characterization.

For the companion fact: why $\mathfrak{p}$-primary ideals contract cleanly. The contraction $\mathfrak{q}^{ec}$ equals $\mathfrak{q}$ precisely when the multiplicative set $S = A\setminus\mathfrak{p}$ introduces no new collapse. The obstruction would be an element $s \in S$ with $sa \in \mathfrak{q}$ but $a \notin \mathfrak{q}$ — but $\mathfrak{q}$ being $\mathfrak{p}$-primary means such an $s$ must lie in $\sqrt{\mathfrak{q}} = \mathfrak{p}$, contradicting $s \in A\setminus\mathfrak{p}$. So no element of $S$ can "clear" anything out of $\mathfrak{q}$, and the contraction recovers $\mathfrak{q}$ exactly. The condition $S \cap \mathfrak{p} = \varnothing$ is doing all the work: it says $S$ avoids the radical of $\mathfrak{q}$, so it cannot interfere.

---

# What Makes This Hard

The theorem itself is easy *given* the [[Thm - Characterization of Discrete Valuation Rings|DVR characterization]] — it is essentially "inherit the four hypotheses, then quote the characterization". The two places people slip are: forgetting that **integral-closedness is a local property** (this is the only nontrivial inheritance, and it is what uses the Dedekind hypothesis rather than just dimension $1$), and getting the **companion contraction fact** wrong by not seeing that $S \cap \mathfrak{p} = \varnothing$ is exactly what prevents the multiplicative set from collapsing the primary ideal. The common error is to think localization "always loses information" and that exponents cannot be recovered; the primary-contraction fact is precisely the guarantee that at the relevant prime, nothing is lost.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show $A_\mathfrak{p}$ inherits the four DVR hypotheses (Noetherian, local, dimension $1$, integrally closed), then invoke the DVR characterization. For the companion fact, show the multiplicative set $A\setminus\mathfrak{p}$ cannot collapse a $\mathfrak{p}$-primary ideal because it avoids $\sqrt{\mathfrak{q}} = \mathfrak{p}$.

**Subgoal decomposition:**

1. **$A_\mathfrak{p}$ is a Noetherian local domain of dimension $1$.**
   - *Hint:* Localization of Noetherian is Noetherian; primes of $A_\mathfrak{p}$ are the primes of $A$ inside $\mathfrak{p}$, i.e. $(0)$ and $\mathfrak{p}$; so it is local with $\dim = \operatorname{ht}\mathfrak{p} = 1$.
   - *Why needed:* It supplies three of the four hypotheses for the characterization.

2. **$A_\mathfrak{p}$ is integrally closed.**
   - *Hint:* $A$ is integrally closed (Dedekind), and being integrally closed is a local property.
   - *Why needed:* It supplies the fourth, decisive hypothesis.

3. **$A_\mathfrak{p}$ is a DVR.**
   - *Hint:* Apply the DVR characterization to the Noetherian, integrally closed, local domain of dimension $1$.
   - *Why needed:* It is the theorem.

4. **(Companion) $\mathfrak{p}$-primary ideals are contracted from $S^{-1}A$ when $S \cap \mathfrak{p} = \varnothing$.**
   - *Hint:* If $sa \in \mathfrak{q}$ with $s \in S$, primaryness forces $a \in \mathfrak{q}$ or $s \in \sqrt{\mathfrak{q}} = \mathfrak{p}$; the latter is excluded.
   - *Why needed:* It makes localization reversible, enabling exponent recovery.

---

# Lemma Decomposition

> [!note]- Lemma 1: $A_\mathfrak{p}$ is a Noetherian local domain of dimension $1$
> **Statement:** For a nonzero prime $\mathfrak{p}$ of a Dedekind domain $A$, the localization $A_\mathfrak{p}$ is a Noetherian local integral domain with $\operatorname{Spec} A_\mathfrak{p} = \{(0), \mathfrak{p}A_\mathfrak{p}\}$ and $\dim A_\mathfrak{p} = 1$.
>
> **Hint:** Use that localization preserves Noetherian and domain, and that primes of $A_\mathfrak{p}$ correspond to primes of $A$ inside $\mathfrak{p}$.
>
> **Why needed:** It establishes three of the four hypotheses of the DVR characterization.
>
> > [!note]- Full proof
> > $A_\mathfrak{p}$ is a localization of the domain $A$, hence a domain, with $\operatorname{Frac}(A_\mathfrak{p}) = K$. It is Noetherian: every ideal of $A_\mathfrak{p}$ is the extension of an ideal of $A$, which is finitely generated (as $A$ is Noetherian), so its extension is finitely generated, and the ascending chain condition is inherited. By the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]] for $S = A\setminus\mathfrak{p}$, the primes of $A_\mathfrak{p}$ are exactly $\{\mathfrak{q}A_\mathfrak{p} : \mathfrak{q} \in \operatorname{Spec} A,\ \mathfrak{q} \subseteq \mathfrak{p}\}$. Since $\dim A = 1$, the primes of $A$ contained in $\mathfrak{p}$ are just $(0)$ and $\mathfrak{p}$. So $\operatorname{Spec} A_\mathfrak{p} = \{(0), \mathfrak{p}A_\mathfrak{p}\}$, $A_\mathfrak{p}$ is local with maximal ideal $\mathfrak{p}A_\mathfrak{p} \neq (0)$, and $\dim A_\mathfrak{p} = 1$.

> [!note]- Lemma 2: $A_\mathfrak{p}$ is integrally closed
> **Statement:** The localization $A_\mathfrak{p}$ of an integrally closed domain $A$ is integrally closed in $K$.
>
> **Hint:** Being integrally closed is a local property; or argue directly by clearing denominators in an integral equation.
>
> **Why needed:** It supplies the fourth, decisive hypothesis — the one that uses the Dedekind property beyond dimension $1$.
>
> > [!note]- Full proof
> > Being integrally closed is a local property: a domain $A$ is integrally closed iff $A_\mathfrak{m}$ is integrally closed for every maximal $\mathfrak{m}$. We can also see it directly. Suppose $x \in K$ is integral over $A_\mathfrak{p}$:
> > $$x^n + \tfrac{a_1}{s_1}x^{n-1} + \cdots + \tfrac{a_n}{s_n} = 0, \qquad a_i \in A,\ s_i \in A\setminus\mathfrak{p}.$$
> > Let $s = s_1\cdots s_n \in A\setminus\mathfrak{p}$. Multiplying by $s^n$ and setting $y = sx$ gives a monic equation $y^n + (\text{terms in } A)\, y^{n-1} + \cdots = 0$ with coefficients in $A$, so $y = sx$ is integral over $A$; as $A$ is integrally closed, $sx \in A$, hence $x = \tfrac{sx}{s} \in A_\mathfrak{p}$. So $A_\mathfrak{p}$ is integrally closed.

> [!note]- Lemma 3: Primary ideals are contracted from localizations that avoid them
> **Statement:** Let $S \subseteq A$ be multiplicative, $\mathfrak{p} \in \operatorname{Spec} A$ with $S \cap \mathfrak{p} = \varnothing$, and $\mathfrak{q}$ a $\mathfrak{p}$-primary ideal. Then $\mathfrak{q} = (\mathfrak{q}\,S^{-1}A)^c$.
>
> **Hint:** Show no $s \in S$ can clear an element out of $\mathfrak{q}$: $sa \in \mathfrak{q}$, $s \notin \mathfrak{p} = \sqrt{\mathfrak{q}}$ forces $a \in \mathfrak{q}$.
>
> **Why needed:** It is the companion fact making localization reversible, used to recover global prime powers from local computations.
>
> > [!note]- Full proof
> > The contraction $(\mathfrak{q}\,S^{-1}A)^c = \{a \in A : \tfrac a1 \in \mathfrak{q}\,S^{-1}A\} = \{a \in A : sa \in \mathfrak{q} \text{ for some } s \in S\}$. The inclusion $\mathfrak{q} \subseteq (\mathfrak{q}\,S^{-1}A)^c$ is clear. Conversely, let $a$ satisfy $sa \in \mathfrak{q}$ for some $s \in S$. Since $\mathfrak{q}$ is $\mathfrak{p}$-primary and $sa \in \mathfrak{q}$, either $a \in \mathfrak{q}$, or $s \in \sqrt{\mathfrak{q}} = \mathfrak{p}$. The second is impossible since $s \in S$ and $S \cap \mathfrak{p} = \varnothing$. Hence $a \in \mathfrak{q}$, so $(\mathfrak{q}\,S^{-1}A)^c = \mathfrak{q}$. (Equivalently, by the contraction criterion, $\mathfrak{q}$ is contracted iff the image $\bar S$ of $S$ in $A/\mathfrak{q}$ has no zero-divisors; for a primary ideal a zero-divisor in $A/\mathfrak{q}$ is nilpotent, hence lies in $\mathfrak{p}/\mathfrak{q}$, contradicting $S \cap \mathfrak{p} = \varnothing$.)

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A$ be a Dedekind domain and $\mathfrak{p}$ a nonzero prime.
>
> ---
> **Step 1 — three hypotheses.** By Lemma 1, $A_\mathfrak{p}$ is a Noetherian local integral domain with $\operatorname{Spec} A_\mathfrak{p} = \{(0), \mathfrak{p}A_\mathfrak{p}\}$, so $\dim A_\mathfrak{p} = 1$ and the maximal ideal is $\mathfrak{p}A_\mathfrak{p}$.
>
> ---
> **Step 2 — the fourth hypothesis.** By Lemma 2, since $A$ is integrally closed (it is Dedekind) and integral-closedness is a local property, $A_\mathfrak{p}$ is integrally closed in $K = \operatorname{Frac}(A_\mathfrak{p})$.
>
> ---
> **Step 3 — apply the characterization.** $A_\mathfrak{p}$ is a Noetherian, integrally closed, local domain of dimension $1$. By the [[Thm - Characterization of Discrete Valuation Rings|DVR characterization theorem]] (condition (2) $\Rightarrow$ (1)), $A_\mathfrak{p}$ is a discrete valuation ring, with a uniformizer generating $\mathfrak{p}A_\mathfrak{p}$ and a valuation $v_\mathfrak{p}$ on $K$.
>
> ---
> **Companion fact.** For any multiplicative $S$ with $S \cap \mathfrak{p} = \varnothing$ and any $\mathfrak{p}$-primary $\mathfrak{q}$, Lemma 3 gives $\mathfrak{q} = (\mathfrak{q}\,S^{-1}A)^c$. In particular, with $S = A\setminus\mathfrak{p}$, every power $\mathfrak{p}^n$ (which is $\mathfrak{p}$-primary) is contracted from $A_\mathfrak{p}$: $\mathfrak{p}^n = (\mathfrak{p}^n A_\mathfrak{p})^c$. So the local valuation determines the global exponent. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Local fields in number theory.** Localizing $\mathcal{O}_K$ at a prime $\mathfrak{p}$ over $p$ gives a DVR $(\mathcal{O}_K)_\mathfrak{p}$; completing it gives the **local field** $K_\mathfrak{p}$ with ring of integers a complete DVR. The application: the local–global principle (Hasse–Minkowski for quadratic forms, the study of $L$-functions via local factors) studies $K$ by studying all its completions $K_\mathfrak{p}$ at once. This theorem is what makes each local piece a DVR, the prerequisite for the whole local theory.

**Order of vanishing on curves (algebraic geometry).** For a smooth affine curve $A$ and a closed point $\mathfrak{p}$, the DVR $A_\mathfrak{p}$ has valuation $v_\mathfrak{p}(f)$ equal to the order of vanishing of $f$ at the point. The application: this is the local model for the theory of **divisors** — a rational function's divisor $\operatorname{div}(f) = \sum_\mathfrak{p} v_\mathfrak{p}(f)[\mathfrak{p}]$ is computed point by point in these DVRs. The Riemann–Roch theorem is a global count of these local orders.

**Discrete valuations and tropical geometry.** Each $A_\mathfrak{p}$ provides a valuation $v_\mathfrak{p} : K^\times \to \mathbb{Z}$, and the collection of all of them is the data of a curve's points. The application: **tropicalization** replaces a variety over a valued field by its image under the valuation, turning algebraic geometry into piecewise-linear (polyhedral) geometry; the DVRs produced by this theorem are the source of the valuations that make tropical geometry run.

---

# Bridges

- **[[Thm - Characterization of Discrete Valuation Rings|The DVR characterization]]** — this theorem is essentially a corollary of it. The characterization does the hard work (proving that Noetherian + integrally closed + local + dimension $1$ forces a DVR); this theorem just supplies those four hypotheses by inheritance from the Dedekind domain. The two together say "Dedekind localizes to DVR", the global-to-local half of the chapter.

- **[[Thm - A Dedekind Domain has Unique Factorization of Ideals|Unique factorization of ideals]]** — this localization theorem, with its companion contraction fact, is the *engine* of unique factorization. The exponent of $\mathfrak{p}$ in the factorization of $\mathfrak{a}$ is the valuation $v_\mathfrak{p}(\mathfrak{a}A_\mathfrak{p})$ read in the DVR, and the contraction fact is what lets the local power $\mathfrak{p}^nA_\mathfrak{p}$ be pulled back to the global $\mathfrak{p}^n$. Without this theorem, unique factorization would have no local model to compute in.

- **[[Thm - Prime Ideals of a Localization|The prime-correspondence theorem]]** — this is what makes $A_\mathfrak{p}$ local with exactly the right primes: localizing at $\mathfrak{p}$ keeps precisely the primes of $A$ contained in $\mathfrak{p}$, which in dimension $1$ are just $(0)$ and $\mathfrak{p}$. This is the source of "local of dimension $1$" in the inheritance, and the geometric statement that localizing zooms in to a neighbourhood of the point $\mathfrak{p}$.

- **[[Def - Primary Ideal|Primary ideals]] and locality of normality** — the companion fact uses that $\mathfrak{p}$-primary ideals contract cleanly when $S$ avoids $\mathfrak{p}$, and the main theorem uses that integral-closedness is a local property. Both are instances of the broader theme that localization faithfully reflects local structure: it neither creates nor destroys information at the prime you localize at.

---

# Unlocked by This

> [!tip] Completions and local fields *(from Algebraic Number Theory)*
> Once $A_\mathfrak{p}$ is a DVR, completing it at $\mathfrak{p}A_\mathfrak{p}$ produces a **complete DVR** $\widehat{A}_\mathfrak{p}$, and for $A = \mathcal{O}_K$ this is the ring of integers of the **local field** $K_\mathfrak{p}$ (e.g. $\mathbb{Q}_p$ when $A = \mathbb{Z}$). Local fields are where **Hensel's lemma**, local class field theory, and the local–global principle live; the whole strategy of "study a global object via all its localizations and completions" rests on each localization being a DVR, which this theorem guarantees.

> [!tip] Modules over Dedekind domains are locally free *(from Commutative Algebra)*
> Because every $A_\mathfrak{p}$ is a DVR — a local PID — a finitely generated torsion-free $A$-module $M$ has $M_\mathfrak{p}$ free over $A_\mathfrak{p}$ at every prime, hence $M$ is **locally free**, i.e. **projective** of constant rank. This is the structure theorem for modules over a Dedekind domain: every finitely generated module is $A^{r-1} \oplus \mathfrak{a}$ for a fractional ideal $\mathfrak{a}$, with the class of $\mathfrak{a}$ in $\operatorname{Cl}(A)$ the only invariant beyond the rank. The local-DVR structure provided here is exactly what makes this classification possible.
