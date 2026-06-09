---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Dedekind Domain"
  - "Def - Discrete Valuation and Valuation Ring"
  - "Def - Primary Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Thm - Localization of a Dedekind Domain is a DVR"
  - "Thm - Chinese Remainder Theorem for Modules"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A$ be a [[Def - Dedekind Domain|Dedekind domain]] with fraction field $K$. We write $\mathfrak{a}, \mathfrak{b}$ for nonzero ideals, $\mathfrak{p}, \mathfrak{q}$ for nonzero (hence maximal) prime ideals, $\mathfrak{p}^n$ for the ideal power, and $A_\mathfrak{p}$ for the [[Def - Multiplicative Set and Localization|localization]] at $\mathfrak{p}$ — a [[Def - Discrete Valuation and Valuation Ring|DVR]] by [[Thm - Localization of a Dedekind Domain is a DVR|the localization theorem]], with valuation $v_\mathfrak{p}$. An ideal $\mathfrak{q}$ is **[[Def - Primary Ideal|$\mathfrak{p}$-primary]]** if $\sqrt{\mathfrak{q}} = \mathfrak{p}$ and $xy \in \mathfrak{q},\, x \notin \mathfrak{q} \Rightarrow y \in \sqrt{\mathfrak{q}}$. We write $\mathfrak{q}^c = \iota^{-1}(\mathfrak{q}A_\mathfrak{p})$ for the [[Def - Extension and Contraction of Ideals|contraction]] along $\iota : A \to A_\mathfrak{p}$. The full registry is on [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

---

# Statement

> **Theorem (unique factorization of ideals).** Let $A$ be a Dedekind domain and $\mathfrak{a}$ a nonzero ideal of $A$. Then
> $$\mathfrak{a} = \mathfrak{p}_1^{e_1} \cdots \mathfrak{p}_n^{e_n}$$
> for distinct nonzero prime ideals $\mathfrak{p}_1, \dots, \mathfrak{p}_n$ and integers $e_i \geq 1$. The primes $\mathfrak{p}_i$ and the exponents $e_i$ are uniquely determined by $\mathfrak{a}$, up to reordering.

> **Corollary.** The exponent of $\mathfrak{p}_i$ is the local valuation, $e_i = v_{\mathfrak{p}_i}(\mathfrak{a}A_{\mathfrak{p}_i})$, read in the DVR $A_{\mathfrak{p}_i}$. A prime $\mathfrak{p}$ divides $\mathfrak{a}$ (appears with $e > 0$) iff $\mathfrak{a} \subseteq \mathfrak{p}$, so the $\mathfrak{p}_i$ are exactly the primes containing $\mathfrak{a}$.

---

# Motivation

This is the theorem that justifies the entire concept of a Dedekind domain. In $\mathbb{Z}$, unique factorization of integers is the foundation of arithmetic, but in rings like $\mathbb{Z}[\sqrt{-5}]$ it fails — $6 = 2\cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ shows two different factorizations of one element into irreducibles. For a while in the nineteenth century this looked like a fatal obstruction to doing number theory in such rings. Kummer's insight, made rigorous by Dedekind, was that the right objects to factor are not *numbers* but *ideals*: at the level of ideals the ambiguity disappears, and one regains a clean, unique factorization. The theorem on this page is that recovery, stated in full generality.

What it buys you is enormous. Once ideals factor uniquely into primes, the multiplicative structure of ideals becomes as transparent as that of integers: divisibility is comparison of exponents, the greatest common divisor and least common multiple are min and max of exponents, "to contain is to divide", and the whole apparatus of fractional ideals and the class group becomes available. Every later computation in the chapter — finding the factorization of $(6)$ in $\mathbb{Z}[\sqrt{-5}]$, computing a class group, deciding whether an ideal is principal — runs on this theorem. It is the substitute for unique factorization of elements, and it recovers the latter exactly when every ideal is principal (when the class group is trivial).

The proof is a perfect illustration of the local-to-global method. Rather than factoring directly in $A$ — which is hard, since $A$ is a complicated global ring — one localizes at each prime $\mathfrak{p}$, where $A_\mathfrak{p}$ is a DVR and *every* ideal is trivially a power of the maximal ideal. The factorization is read off locally, prime by prime, and then reassembled globally using that the primary decomposition of $\mathfrak{a}$ (which exists by Noetherianity) has primary components that are exactly prime powers, and that distinct maximal primes are coprime so the intersection collapses to a product. The hard work was done in establishing that $A_\mathfrak{p}$ is a DVR; this theorem is the harvest.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$A$ is a Dedekind domain and $\mathfrak{a} \neq 0$". The skill is recognizing when this applies.

The first disguised source is **a ring of integers**. The property $B$ is "$A = \mathcal{O}_K$ for a number field $K$". The bridge is [[Thm - The Ring of Integers of a Number Field is Dedekind|$\mathcal{O}_K$ is Dedekind]], after which factorization applies. The non-obvious part is that an arithmetic object — the integral closure of $\mathbb{Z}$ — automatically carries unique ideal factorization, even when it is wildly non-UFD as a ring of elements. *Example problem:* factor $(6)$ in $\mathbb{Z}[\sqrt{-5}]$ into primes — see [[Ex - Unique factorization of ideals in Z[sqrt -5]]].

The second disguised source is **a PID**. The property $B$ is "$A$ is a PID". Every PID is Dedekind, and here the prime factorization of ideals *is* the prime factorization of generators: $(n) = \prod (p_i)^{e_i}$ reflects $n = \prod p_i^{e_i}$. The non-obvious value is that the abstract theorem specializes exactly to ordinary integer factorization, certifying the abstraction is faithful. *Example problem:* recover unique factorization in $\mathbb{Z}$ as the ideal-theoretic statement.

The third disguised source is **a coordinate ring of a smooth affine curve**. The property $B$ is "$A$ is a one-dimensional integrally closed finitely generated $k$-algebra". The bridge is that such a ring is Dedekind, so an ideal factors into primes — geometrically, a closed subscheme of the curve is a sum of points with multiplicities. The non-obviousness: a *geometric* divisor decomposes into points exactly because of this *algebraic* theorem. *Example problem:* decompose the ideal of a degree-$3$ divisor on a curve.

**Targets (Output Amplification)**

The conclusion is "$\mathfrak{a} = \prod \mathfrak{p}_i^{e_i}$ uniquely".

Combine factorization with **the exponent-vector viewpoint**. Writing each ideal as its vector of exponents $(v_\mathfrak{p}(\mathfrak{a}))_\mathfrak{p}$ turns multiplication into addition, containment into coordinatewise $\geq$, gcd/lcm into min/max. The further result $E$: ideals form the free abelian monoid on primes, the cleanest possible multiplicative structure, on which the [[Def - Fractional Ideal and the Ideal Class Group|fractional ideal group]] is built. Nonobvious because it linearizes all of ideal theory.

Combine factorization with **"to contain is to divide"**. The corollary $\mathfrak{a} \subseteq \mathfrak{p} \iff \mathfrak{p} \mid \mathfrak{a}$, extended to $\mathfrak{a} \supseteq \mathfrak{b} \iff \mathfrak{a} \mid \mathfrak{b}$, converts containment problems into divisibility problems. The further result $E$: cancellation holds ($\mathfrak{a}\mathfrak{c} = \mathfrak{b}\mathfrak{c} \Rightarrow \mathfrak{a} = \mathfrak{b}$), and one can "divide" ideals. Nonobvious because containment and divisibility are *opposite* inclusions in general rings but coincide here.

Combine factorization with **the class group**. If $\mathfrak{a}^n = (x)$ is principal then $[\mathfrak{a}]$ has order dividing $n$ in $\operatorname{Cl}(A)$, and triviality of $\operatorname{Cl}(A)$ makes every ideal principal, hence $A$ a PID and a UFD. The further result $E$: **a Dedekind domain is a UFD iff it is a PID iff $\operatorname{Cl}(A) = 0$**. Nonobvious because it ties element-factorization to a group cohomology-flavored invariant.

---

# Why Is It True

The intuition is that **factoring an ideal is the same as recording, for each prime $\mathfrak{p}$, how divisible the ideal is by $\mathfrak{p}$ — and "how divisible" is a single integer because $A_\mathfrak{p}$ is a DVR.**

**The bolded mechanism:** **the exponent $e_\mathfrak{p}$ of $\mathfrak{p}$ in $\mathfrak{a}$ is just the valuation $v_\mathfrak{p}(\mathfrak{a})$ computed in the DVR $A_\mathfrak{p}$, the global ideal $\mathfrak{a}$ is determined by all these local exponents because it can be recovered as the intersection $\bigcap_\mathfrak{p} (\mathfrak{a}A_\mathfrak{p} \cap A)$, and the intersection collapses to a product because distinct maximal ideals are coprime.**

Here is the chain of ideas. *First*, why each prime contributes a prime *power*. Localize $\mathfrak{a}$ at a prime $\mathfrak{p}$ containing it; the result $\mathfrak{a}A_\mathfrak{p}$ is a nonzero proper ideal of the DVR $A_\mathfrak{p}$, hence equals $(\mathfrak{p}A_\mathfrak{p})^e$ for a unique $e \geq 1$ — that is the *only* kind of ideal a DVR has. Contracting back, $\mathfrak{p}^e$ is recovered (this is where one needs $\mathfrak{p}$-primary ideals to be contracted from $A_\mathfrak{p}$). So locally, near each prime, $\mathfrak{a}$ looks exactly like a power of that prime, and the exponent is forced.

*Second*, why the local data assembles into a global factorization. Because $A$ is Noetherian, $\mathfrak{a}$ has a primary decomposition $\mathfrak{a} = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ into primary ideals. The crucial fact — proved separately — is that in a Dedekind domain the $\mathfrak{p}$-primary ideals are *exactly the powers* $\{\mathfrak{p}^e\}$, nothing more exotic. So each $\mathfrak{q}_i = \mathfrak{p}_i^{e_i}$ is a prime power. The decomposition becomes $\mathfrak{a} = \mathfrak{p}_1^{e_1} \cap \cdots \cap \mathfrak{p}_n^{e_n}$, an intersection.

*Third*, why intersection becomes product. The $\mathfrak{p}_i$ are distinct nonzero primes, hence distinct maximal ideals, hence *pairwise coprime* ($\mathfrak{p}_i + \mathfrak{p}_j = A$), and their powers are too. For pairwise coprime ideals the [[Thm - Chinese Remainder Theorem for Modules|Chinese Remainder Theorem]] gives $\bigcap \mathfrak{p}_i^{e_i} = \prod \mathfrak{p}_i^{e_i}$. So the intersection collapses to the product, yielding $\mathfrak{a} = \prod \mathfrak{p}_i^{e_i}$.

*Finally*, uniqueness is inherited from uniqueness of primary decomposition: the primes $\mathfrak{p}_i$ are the (isolated) associated primes of $\mathfrak{a}$, uniquely determined, and the exponents are pinned down by the strictly-decreasing chain $\mathfrak{p}^e \supsetneq \mathfrak{p}^{e+1}$ — which is exactly the DVR fact that the local powers strictly decrease, via Nakayama. So both the primes and the exponents are forced, and the factorization is unique.

The whole proof is "the global factorization is the bookkeeping of all the local DVR factorizations, and the bookkeeping is lossless because distinct primes do not interfere".

---

# What Makes This Hard

The two genuinely substantive steps are easy to overlook because each is a separate proposition. The first is that **$\mathfrak{p}$-primary ideals in a Dedekind domain are exactly the powers $\mathfrak{p}^e$** — this is where the DVR structure of $A_\mathfrak{p}$ is used (a $\mathfrak{p}$-primary ideal localizes to a power of $\mathfrak{p}A_\mathfrak{p}$ and contracts back), and it requires the lemma that $\mathfrak{p}$-primary ideals are contracted from $A_\mathfrak{p}$. The second is the **collapse of intersection to product via coprimality and CRT**. Most people get stuck either by trying to factor directly in $A$ (instead of localizing) or by forgetting that primary decomposition only gives an *intersection*, which must be upgraded to a *product*. The common error is to assume "primary $=$ prime power" without proof; it is true here only because $A$ is Dedekind, and is false in general rings.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use Noetherianity to get a primary decomposition $\mathfrak{a} = \bigcap \mathfrak{q}_i$. Identify each $\mathfrak{q}_i$ as a prime power $\mathfrak{p}_i^{e_i}$ by localizing to the DVR $A_{\mathfrak{p}_i}$ and contracting. Collapse the intersection to a product via coprimality and CRT. Uniqueness comes from uniqueness of the associated primes and the strict decrease of prime powers.

**Subgoal decomposition:**

1. **Primary ideals are prime powers.** Show: in a Dedekind domain, every $\mathfrak{p}$-primary ideal is $\mathfrak{p}^e$ for a unique $e \geq 1$, and the powers $\mathfrak{p}^e$ strictly decrease.
   - *Hint:* Localize: $\mathfrak{q}A_\mathfrak{p}$ is a nonzero proper ideal of the DVR $A_\mathfrak{p}$, so $= (\mathfrak{p}A_\mathfrak{p})^e$; contract back using that $\mathfrak{p}$-primary ideals are contracted from $A_\mathfrak{p}$. Strict decrease is Nakayama in the DVR.
   - *Why needed:* It converts the primary components into prime powers.

2. **Primary decomposition.** Show: $\mathfrak{a} = \mathfrak{p}_1^{e_1} \cap \cdots \cap \mathfrak{p}_n^{e_n}$ with the $\mathfrak{p}_i$ distinct nonzero primes.
   - *Hint:* $A$ Noetherian gives a minimal primary decomposition $\mathfrak{a} = \bigcap \mathfrak{q}_i$; apply step 1 to each $\mathfrak{q}_i$. The $\mathfrak{p}_i$ are the associated primes, all maximal since $\dim A = 1$.
   - *Why needed:* It writes $\mathfrak{a}$ as an intersection of prime powers.

3. **Intersection equals product.** Show: $\bigcap \mathfrak{p}_i^{e_i} = \prod \mathfrak{p}_i^{e_i}$.
   - *Hint:* Distinct maximal ideals are coprime, so their powers are coprime; apply CRT (the kernel of $A \to \prod A/\mathfrak{p}_i^{e_i}$ is both the intersection and the product).
   - *Why needed:* It upgrades the intersection to a product, giving existence.

4. **Uniqueness.** Show: the $\mathfrak{p}_i$ and $e_i$ are determined by $\mathfrak{a}$.
   - *Hint:* The $\mathfrak{p}_i$ are the (isolated, hence unique) associated primes; $e_i$ is pinned by $\mathfrak{a}A_{\mathfrak{p}_i} = (\mathfrak{p}_iA_{\mathfrak{p}_i})^{e_i}$ and strict decrease of the powers.
   - *Why needed:* It completes the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\mathfrak{p}$-primary ideals are contracted from $A_\mathfrak{p}$
> **Statement:** Let $\mathfrak{p}$ be a nonzero prime of a Dedekind domain $A$ and $\mathfrak{q}$ a $\mathfrak{p}$-primary ideal. Then $\mathfrak{q} = (\mathfrak{q}A_\mathfrak{p})^c$ — $\mathfrak{q}$ is contracted from its extension to $A_\mathfrak{p}$.
>
> **Hint:** Show the image of $S = A\setminus\mathfrak{p}$ in $A/\mathfrak{q}$ has no zero-divisors, which for a primary ideal means no nilpotents; a nilpotent in the image would land in $\sqrt{\mathfrak{q}} = \mathfrak{p}$, contradicting $S \cap \mathfrak{p} = \varnothing$.
>
> **Why needed:** It is what lets the local exponent be pulled back to the global prime power; without it, localizing would lose information.
>
> > [!note]- Full proof
> > For the localization map $\iota : A \to S^{-1}A = A_\mathfrak{p}$ with $S = A\setminus\mathfrak{p}$, the contraction $\mathfrak{q}^{ec} = \{a \in A : sa \in \mathfrak{q} \text{ for some } s \in S\}$. We must show this equals $\mathfrak{q}$. The inclusion $\mathfrak{q} \subseteq \mathfrak{q}^{ec}$ is automatic. For the reverse: suppose $sa \in \mathfrak{q}$ with $s \in S = A\setminus\mathfrak{p}$. Since $\mathfrak{q}$ is $\mathfrak{p}$-primary and $sa \in \mathfrak{q}$, either $a \in \mathfrak{q}$ (done) or $s \in \sqrt{\mathfrak{q}} = \mathfrak{p}$. But $s \notin \mathfrak{p}$ by choice. Hence $a \in \mathfrak{q}$, so $\mathfrak{q}^{ec} = \mathfrak{q}$. (Equivalently: the image $\bar{S}$ of $S$ in $A/\mathfrak{q}$ contains no zero-divisors, since a zero-divisor would be nilpotent — $A/\mathfrak{q}$ has nilradical $\mathfrak{p}/\mathfrak{q}$ as it is primary — and lie in $\mathfrak{p}$.)

> [!note]- Lemma 2: $\mathfrak{p}$-primary ideals are exactly the powers $\mathfrak{p}^e$
> **Statement:** In a Dedekind domain $A$, the set of $\mathfrak{p}$-primary ideals (for a fixed nonzero prime $\mathfrak{p}$) is exactly $\{\mathfrak{p}^e : e \geq 1\}$, and $\mathfrak{p} \supsetneq \mathfrak{p}^2 \supsetneq \mathfrak{p}^3 \supsetneq \cdots$ is strictly decreasing.
>
> **Hint:** $\sqrt{\mathfrak{p}^e} = \mathfrak{p}$ shows each power is $\mathfrak{p}$-primary; conversely localize a $\mathfrak{p}$-primary $\mathfrak{q}$ to the DVR $A_\mathfrak{p}$, get $(\mathfrak{p}A_\mathfrak{p})^e$, contract via Lemma 1.
>
> **Why needed:** It identifies the primary components of any ideal as prime powers — the structural heart of the theorem.
>
> > [!note]- Full proof
> > **Each $\mathfrak{p}^e$ is $\mathfrak{p}$-primary.** Since $\mathfrak{p}$ is maximal, $\sqrt{\mathfrak{p}^e} = \mathfrak{p}$, and an ideal whose radical is maximal is primary; so $\mathfrak{p}^e$ is $\mathfrak{p}$-primary.
> >
> > **Every $\mathfrak{p}$-primary $\mathfrak{q}$ is some $\mathfrak{p}^e$.** Extend $\mathfrak{q}$ to the DVR $A_\mathfrak{p}$. Then $\mathfrak{q}A_\mathfrak{p}$ is a nonzero (as $\mathfrak{q} \neq 0$) proper (as $\mathfrak{q} \subseteq \mathfrak{p}$, so $\mathfrak{q}A_\mathfrak{p} \subseteq \mathfrak{p}A_\mathfrak{p}$) ideal of $A_\mathfrak{p}$. By [[Thm - Characterization of Discrete Valuation Rings|the DVR characterization]], $\mathfrak{q}A_\mathfrak{p} = (\mathfrak{p}A_\mathfrak{p})^e = \mathfrak{p}^e A_\mathfrak{p}$ for some $e \geq 1$. Now contract: by Lemma 1, $\mathfrak{q} = (\mathfrak{q}A_\mathfrak{p})^c = (\mathfrak{p}^e A_\mathfrak{p})^c$, and $\mathfrak{p}^e$ is itself $\mathfrak{p}$-primary so also contracted, $\mathfrak{p}^e = (\mathfrak{p}^e A_\mathfrak{p})^c$. Hence $\mathfrak{q} = \mathfrak{p}^e$.
> >
> > **Strict decrease.** If $\mathfrak{p}^{e+1} = \mathfrak{p}^e$, extend to $A_\mathfrak{p}$: $(\mathfrak{p}A_\mathfrak{p})^{e+1} = (\mathfrak{p}A_\mathfrak{p})^e$, so by Nakayama $(\mathfrak{p}A_\mathfrak{p})^e = 0$, forcing $\mathfrak{p}A_\mathfrak{p} = 0$ (domain), so $\mathfrak{p} = 0$ — contradiction. Hence the powers strictly decrease, and the exponent $e$ in $\mathfrak{q} = \mathfrak{p}^e$ is unique.

> [!note]- Lemma 3: Distinct nonzero primes are coprime; intersection equals product
> **Statement:** If $\mathfrak{p}_1, \dots, \mathfrak{p}_n$ are distinct nonzero primes of a Dedekind domain and $e_i \geq 1$, then the $\mathfrak{p}_i^{e_i}$ are pairwise coprime and $\bigcap_i \mathfrak{p}_i^{e_i} = \prod_i \mathfrak{p}_i^{e_i}$.
>
> **Hint:** Distinct nonzero primes are distinct maximal ideals, so $\mathfrak{p}_i + \mathfrak{p}_j = A$; coprimality passes to powers; then CRT.
>
> **Why needed:** It upgrades the primary-decomposition intersection to the product factorization.
>
> > [!note]- Full proof
> > Since $\dim A = 1$, every nonzero prime is maximal, so for $i \neq j$, $\mathfrak{p}_i + \mathfrak{p}_j$ is an ideal strictly containing the maximal ideal $\mathfrak{p}_i$, hence equals $A$: $\mathfrak{p}_i, \mathfrak{p}_j$ are coprime. Coprimality passes to powers: if $\mathfrak{p}_i + \mathfrak{p}_j = A$ then $\mathfrak{p}_i^{e_i} + \mathfrak{p}_j^{e_j} = A$ (raise $1 = a + b$ with $a \in \mathfrak{p}_i$, $b \in \mathfrak{p}_j$ to a high power; every term lies in $\mathfrak{p}_i^{e_i}$ or $\mathfrak{p}_j^{e_j}$). So the $\mathfrak{p}_i^{e_i}$ are pairwise coprime. By the [[Thm - Chinese Remainder Theorem for Modules|Chinese Remainder Theorem]] for pairwise coprime ideals, the natural map $A \to \prod_i A/\mathfrak{p}_i^{e_i}$ is surjective with kernel both $\bigcap_i \mathfrak{p}_i^{e_i}$ and $\prod_i \mathfrak{p}_i^{e_i}$ (for pairwise coprime ideals these coincide). Hence $\bigcap_i \mathfrak{p}_i^{e_i} = \prod_i \mathfrak{p}_i^{e_i}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A$ be a Dedekind domain and $\mathfrak{a} \neq 0$ a proper ideal (the case $\mathfrak{a} = A$ is the empty product).
>
> ---
> **Step 0 — primary decomposition exists.** Since $A$ is [[Def - Noetherian Ring|Noetherian]], $\mathfrak{a}$ has a minimal primary decomposition $\mathfrak{a} = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ with $\mathfrak{q}_i$ being $\mathfrak{p}_i$-primary for distinct primes $\mathfrak{p}_i$. As $\mathfrak{a} \neq 0$, all $\mathfrak{p}_i$ are nonzero, hence maximal (dimension $1$); so there are no inclusions among them, and they are the isolated associated primes of $\mathfrak{a}$, uniquely determined by $\mathfrak{a}$.
>
> ---
> **Step 1 — components are prime powers.** By Lemma 2, each $\mathfrak{p}_i$-primary ideal $\mathfrak{q}_i$ equals $\mathfrak{p}_i^{e_i}$ for a unique $e_i \geq 1$. Thus
> $$\mathfrak{a} = \mathfrak{p}_1^{e_1} \cap \cdots \cap \mathfrak{p}_n^{e_n}.$$
>
> ---
> **Step 2 — intersection equals product.** By Lemma 3, the $\mathfrak{p}_i^{e_i}$ are pairwise coprime, so
> $$\mathfrak{a} = \mathfrak{p}_1^{e_1} \cap \cdots \cap \mathfrak{p}_n^{e_n} = \mathfrak{p}_1^{e_1} \cdots \mathfrak{p}_n^{e_n}.$$
> This is the asserted factorization; existence is proved.
>
> ---
> **Step 3 — uniqueness.** The primes $\mathfrak{p}_i$ are the associated primes of $\mathfrak{a}$, which are uniquely determined (they are the radicals of the isolated primary components, and all are isolated since all are maximal). Given the primes, each exponent is determined by localizing: extending $\mathfrak{a} = \prod \mathfrak{p}_j^{e_j}$ to $A_{\mathfrak{p}_i}$ kills every factor $\mathfrak{p}_j$ with $j \neq i$ (since $\mathfrak{p}_j \not\subseteq \mathfrak{p}_i$ makes $\mathfrak{p}_j A_{\mathfrak{p}_i} = A_{\mathfrak{p}_i}$), leaving $\mathfrak{a}A_{\mathfrak{p}_i} = (\mathfrak{p}_i A_{\mathfrak{p}_i})^{e_i}$; by strict decrease of the powers in the DVR $A_{\mathfrak{p}_i}$ (Lemma 2), $e_i = v_{\mathfrak{p}_i}(\mathfrak{a}A_{\mathfrak{p}_i})$ is uniquely determined. Hence the factorization is unique up to reordering. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Recovering integer factorization (elementary number theory).** Specializing to $A = \mathbb{Z}$, the theorem says $(n) = \prod (p_i)^{e_i}$, which is exactly the fundamental theorem of arithmetic $n = \prod p_i^{e_i}$ read at the level of ideals. The nonobvious recognition is that the abstract Dedekind machinery, applied to the simplest Dedekind domain, returns the most familiar theorem in mathematics — a sanity check that the abstraction is faithful, and a template for how it generalizes.

**Divisors on algebraic curves (algebraic geometry).** On a smooth affine curve $C = \operatorname{Spec} A$, a nonzero ideal $\mathfrak{a}$ corresponds to an effective **divisor** $D = \sum e_i [\mathfrak{p}_i]$, and this theorem is the statement that every effective divisor is a sum of points with multiplicities. The application battle-tests the theorem geometrically: the multiplicity $e_i$ is the order of vanishing along the curve at the point $\mathfrak{p}_i$, computed in the DVR local ring, and the whole theory of linear systems and Riemann–Roch is built on this point-decomposition.

**Splitting of primes in number fields (algebraic number theory).** For $\mathcal{O}_K$ and a rational prime $p$, the factorization $(p)\mathcal{O}_K = \prod \mathfrak{p}_i^{e_i}$ is unique by this theorem, and the exponents $e_i$ are the **ramification indices** governing how $p$ splits in $K$. The application is the foundation of explicit number theory: Dedekind's criterion computes the factorization from the factorization of the minimal polynomial mod $p$, and the identity $\sum e_i f_i = [K:\mathbb{Q}]$ is its first consequence.

---

# Bridges

- **[[Thm - Localization of a Dedekind Domain is a DVR|Localization gives a DVR]]** — this is the engine of the proof. The entire factorization is computed by localizing at each prime, reading off the exponent in the DVR $A_\mathfrak{p}$ as a valuation, and contracting back; without the DVR structure of $A_\mathfrak{p}$ there would be no local model in which factoring is trivial. The localization theorem is the "hard part" and this theorem is its global payoff.

- **[[Def - Primary Ideal|Primary decomposition]] and [[Thm - Chinese Remainder Theorem for Modules|CRT]]** — the proof routes through primary decomposition (which exists by Noetherianity) and then collapses the resulting intersection to a product using coprimality and the Chinese Remainder Theorem. The Dedekind hypothesis enters by making primary components into prime powers (Lemma 2) and primes into coprime maximal ideals (Lemma 3); CRT does the rest.

- **[[Def - Fractional Ideal and the Ideal Class Group|Fractional ideals and the class group]]** — unique factorization is what makes the fractional ideals a *free abelian group* $\bigoplus_\mathfrak{p}\mathbb{Z}$ on the primes: a fractional ideal is $\prod \mathfrak{p}^{n_\mathfrak{p}}$ with $n_\mathfrak{p} \in \mathbb{Z}$, and the class group is the cokernel of $K^\times$ inside it. This theorem is the structural foundation of all of divisor and class-group theory.

- **[[Def - Unique Factorization Domain|Unique factorization of elements]]** — this theorem is the *ideal-theoretic substitute* for element factorization, and the two agree exactly when ideals are principal. The precise relationship: a Dedekind domain is a UFD iff a PID iff its class group is trivial, so ideal factorization always holds while element factorization holds only when the class group vanishes. The gap is the failure of $\mathbb{Z}[\sqrt{-5}]$ to be a UFD despite ideal factorization being perfectly fine.

---

# Unlocked by This

> [!tip] Divisors, the divisor class group, and Riemann–Roch *(from Algebraic Geometry)*
> Unique factorization of ideals says a nonzero ideal *is* an effective **divisor** $\sum e_i[\mathfrak{p}_i]$ on the curve $\operatorname{Spec} A$, and the group of fractional ideals is the full **divisor group**. The quotient by principal divisors is the **divisor class group** $= \operatorname{Pic}$, and on a complete curve the **Riemann–Roch theorem** computes the dimension of the space of functions with prescribed zeros and poles in terms of the degree of a divisor and the genus. All of this rests on the point-decomposition this theorem provides.

> [!tip] Ramification theory and the fundamental identity *(from Algebraic Number Theory)*
> Factoring an extended prime $\mathfrak{p}B = \prod \mathfrak{P}_i^{e_i}$ in an extension of Dedekind domains gives the **ramification indices** $e_i$ and, with the residue degrees $f_i$, the fundamental identity $\sum e_i f_i = [L:K]$. Whether $\mathfrak{p}$ **splits**, **ramifies**, or stays **inert** is read directly from this factorization, which is well-defined precisely because of unique factorization. This is the gateway to decomposition groups, the Frobenius, and class field theory.
