---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Integral Extensions Preserve Dimension"
  - "Thm - Lying Over"
  - "Thm - Going Up"
  - "Thm - Incomparability"
  - "Thm - Going Down for Integrally Closed Domains"
  - "Def - Krull Dimension and Height"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A \subseteq B$ be an integral extension of rings. Prove that
$$\dim A = \dim B.$$

Then deduce two consequences:

1. **(Polynomial ring dimension.)** $\dim k[X_1, \dots, X_n] = n$, using [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Noether normalization]] and the fact that a finitely generated $k$-domain is integral over a polynomial subring.

2. **(The dimension formula, ES4 Q3b.)** For a finitely generated $k$-algebra $A$ that is a domain, and any $\mathfrak{p} \in \operatorname{Spec} A$,
$$\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A.$$

**Recall:**

The objects in play are integral extensions, Krull dimension and height, the four Cohen–Seidenberg theorems, and Noether normalization.

![[Thm - Integral Extensions Preserve Dimension#Statement]]

[[Def - Krull Dimension and Height|Krull dimension]] $\dim R$ is the supremum of lengths $n$ of strict chains $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ of primes; the **height** $\operatorname{ht}\mathfrak{p}$ is the supremum of lengths of chains descending from $\mathfrak{p}$, equal to $\dim A_{\mathfrak{p}}$; $\dim A/\mathfrak{p}$ is the supremum of lengths of chains *ascending* from $\mathfrak{p}$ (primes $\supseteq \mathfrak{p}$).

[[Thm - Lying Over|Lying over]], [[Thm - Going Up|going up]], [[Thm - Incomparability|incomparability]] hold for every integral extension; [[Thm - Going Down for Integrally Closed Domains|going down]] needs $A$ normal. [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Noether normalization]]: a finitely generated $k$-domain $A$ is module-finite over a polynomial subring $k[X_1,\dots,X_d]$, $d = \operatorname{trdeg}_k \operatorname{Frac} A$.

---

# Convergent Strategy

**Problem class.** This is a *compare-dimensions* problem — the capstone of the chapter, assembling the four theorems into the headline result and its refinements. As the [[Commutative Algebra VIII — Going Up and Going Down#Problem-Solving Strategy|topic-page strategy]] records, dimension is settled by a two-sided chain comparison, and the two inequalities use *different* theorems.

**Assumption pattern.** "$A \subseteq B$ integral" is the master hypothesis, unlocking lying over, going up, incomparability. The recognisable structure: $\dim A \leq \dim B$ is a *lifting* statement (route through lying over + going up), while $\dim B \leq \dim A$ is a *contraction* statement (route through incomparability). For the *finer* formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$, the extra hypotheses "$A$ a finitely generated $k$-domain" bring in Noether normalization (a normal polynomial base) and hence going down.

**Theorem routing.** For the equality: lift a chain of $A$ to $B$ via lying over (anchor) and going up (extend), strict by distinct contractions, giving $\dim A \leq \dim B$; contract a chain of $B$ to $A$, strict by incomparability (no collapse), giving $\dim B \leq \dim A$. For $\dim k[X_1,\dots,X_n] = n$: exhibit the length-$n$ chain $(0) \subsetneq (X_1) \subsetneq \cdots \subsetneq (X_1,\dots,X_n)$ for "$\geq n$", and route "$\leq n$" through transcendence degree (or accept it from [[Commutative Algebra XII — Dimension Theory|the dimension chapter]]). For the formula: Noether-normalize, splice a chain below $\mathfrak{p}$ (built by going down over the normal polynomial base) to a chain above $\mathfrak{p}$ (built by going up), and count.

**Key decision point.** The decisive realisation is that **dimension equality uses only three of the four theorems — not going down, not normality.** $\dim B \leq \dim A$ is pure incomparability; $\dim A \leq \dim B$ is lying over plus going up. The temptation is to think both directions need chain-lifting in both senses (hence going down); they do not — one direction *lifts* (going up), the other *contracts* (incomparability). Going down enters *only* for the finer formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$, where the *position* of $\mathfrak{p}$ in the chain matters and a chain below $\mathfrak{p}$ must be lifted *downward*.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VIII — Going Up and Going Down#Legal Operations|the topic page's Legal Operations]]:

1. **Lift a chain to get $\dim A \leq \dim B$ (operation 8).** Lying over anchors, going up extends, distinct contractions keep strict.

2. **Contract a chain to get $\dim B \leq \dim A$ (operation 7).** Incomparability prevents the contracted chain from collapsing.

3. **Splice with going down for the dimension formula (operation, going-down form).** Over the normal polynomial base, going down builds the part of a chain below $\mathfrak{p}$.

4. **Transport a known dimension across the integral extension.** Noether normalization makes $A$ integral over $k[X_1,\dots,X_d]$, and dimension preservation transfers $\dim = d$.

---

# Hints

> [!note]- Hint 1
> Dimension is a supremum over chains. To prove $\dim A = \dim B$, prove two inequalities. One direction takes a chain of $A$ and produces one of $B$; the other takes a chain of $B$ and produces one of $A$. Which theorems move chains in which direction?

> [!note]- Hint 2
> $\dim A \leq \dim B$: take a chain of $A$, anchor a prime over its bottom with [[Thm - Lying Over|lying over]], extend with [[Thm - Going Up|going up]]. Strictness is free (distinct base primes force distinct lifts). $\dim B \leq \dim A$: take a chain of $B$ and *contract* it — but why does it stay strict?

> [!note]- Hint 3
> Contracting a chain of $B$ could a priori collapse two primes onto one contraction. [[Thm - Incomparability|Incomparability]] forbids exactly this: two comparable primes of $B$ with the same contraction are equal. So the contracted chain stays strict, giving $\dim A \geq \dim B$. Note: *no going down was used* — only three theorems.

> [!note]- Hint 4
> For $\dim k[X_1,\dots,X_n] = n$: the chain $(0) \subsetneq (X_1) \subsetneq \cdots \subsetneq (X_1,\dots,X_n)$ gives $\geq n$; combine with the upper bound. For the formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$: Noether-normalize so $A$ is integral over a polynomial ring (which is *normal*, so going down applies); build a chain below $\mathfrak{p}$ with going down and above $\mathfrak{p}$ with going up, then count $\operatorname{ht}\mathfrak{p}$ links below plus $\dim A/\mathfrak{p}$ links above.

---

# Solution

The equality is the marriage of two one-directional chain arguments: lift a chain of $A$ upstairs (lying over + going up) for $\dim A \leq \dim B$, contract a chain of $B$ downstairs (incomparability) for $\dim B \leq \dim A$. The consequences follow by feeding a Noether normalization into the equality, with going down supplying the downward splice for the finer formula.

**Step 1: $\dim A \leq \dim B$ by lifting a chain.**

Every strict chain of $A$ lifts to a strict chain of $B$ of the same length.

> [!note]- Derivation
> Let $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ be a strict chain in $\operatorname{Spec} A$. By [[Thm - Lying Over|lying over]], choose $\mathfrak{q}_0 \in \operatorname{Spec} B$ over $\mathfrak{p}_0$. By [[Thm - Going Up|going up]], inductively extend to $\mathfrak{q}_0 \subseteq \cdots \subseteq \mathfrak{q}_n$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ (see [[Ex - A chain of primes lifts along a finite extension]]). Each inclusion is strict: $\mathfrak{q}_i = \mathfrak{q}_{i+1}$ would force $\mathfrak{p}_i = \mathfrak{p}_{i+1}$, contradicting strictness. So $B$ has a strict chain of length $n$, giving $\dim B \geq n$; sup over chains of $A$ yields $\dim B \geq \dim A$.

**Step 2: $\dim B \leq \dim A$ by contracting a chain.**

Every strict chain of $B$ contracts to a strict chain of $A$ of the same length.

> [!note]- Derivation
> Let $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_n$ be a strict chain in $\operatorname{Spec} B$. Contraction is order-preserving: $\mathfrak{q}_0 \cap A \subseteq \cdots \subseteq \mathfrak{q}_n \cap A$. If $\mathfrak{q}_i \cap A = \mathfrak{q}_{i+1}\cap A$ for some $i$, then $\mathfrak{q}_i \subsetneq \mathfrak{q}_{i+1}$ are comparable primes with equal contraction, so by [[Thm - Incomparability|incomparability]] $\mathfrak{q}_i = \mathfrak{q}_{i+1}$ — contradiction. Hence the contracted chain is strict of length $n$, giving $\dim A \geq n$; sup over chains of $B$ yields $\dim A \geq \dim B$. Combining with Step 1, $\dim A = \dim B$. **(No going down was used.)**

**Step 3: $\dim k[X_1,\dots,X_n] = n$.**

The polynomial ring has dimension exactly $n$, and any finitely generated $k$-domain has dimension equal to its transcendence degree.

> [!note]- Derivation
> *Lower bound.* The chain $(0) \subsetneq (X_1) \subsetneq (X_1, X_2) \subsetneq \cdots \subsetneq (X_1,\dots,X_n)$ is strict and consists of primes: each quotient $k[X_1,\dots,X_n]/(X_1,\dots,X_i) \cong k[X_{i+1},\dots,X_n]$ is a domain, so $(X_1,\dots,X_i)$ is prime. Hence $\dim k[X_1,\dots,X_n] \geq n$.
>
> *Upper bound.* $\dim k[X_1,\dots,X_n] \leq n$ is proved via transcendence degree in [[Commutative Algebra XII — Dimension Theory|the dimension chapter]] (each strict prime inclusion drops the transcendence degree of the quotient field by at least one, and the transcendence degree starts at $n$). Granting it, $\dim k[X_1,\dots,X_n] = n$.
>
> *General $k$-domain.* By [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Noether normalization]], a finitely generated $k$-domain $A$ is module-finite (hence integral) over $k[X_1,\dots,X_d]$ with $d = \operatorname{trdeg}_k \operatorname{Frac} A$. By Step 1–2, $\dim A = \dim k[X_1,\dots,X_d] = d$. So $\dim A = \operatorname{trdeg}_k \operatorname{Frac} A$.

**Step 4: The dimension formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$ (ES4 Q3b).**

For a finitely generated $k$-domain $A$ and $\mathfrak{p} \in \operatorname{Spec} A$, the codimension and dimension of the subvariety add to the ambient dimension.

> [!note]- Derivation
> Set $d = \dim A$, $h = \operatorname{ht}\mathfrak{p}$, $c = \dim A/\mathfrak{p}$.
>
> *Inequality $h + c \leq d$.* A chain of length $h$ descending from $\mathfrak{p}$ (witnessing $\operatorname{ht}\mathfrak{p} = h$) and a chain of length $c$ ascending from $\mathfrak{p}$ (witnessing $\dim A/\mathfrak{p} = c$, i.e. primes $\supseteq \mathfrak{p}$) splice at $\mathfrak{p}$ into a single chain $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_h = \mathfrak{p} \subsetneq \cdots \subsetneq \mathfrak{p}_{h+c}$ of length $h + c$ in $A$. Hence $d = \dim A \geq h + c$.
>
> *Inequality $h + c \geq d$ (equality).* The reverse — that *every* maximal chain through $\mathfrak{p}$ has full length $d$ — is where going down and Noether normalization enter. The key fact (ES4 Q3a) is that in a finitely generated $k$-domain *all* maximal chains of primes have the same length $d$ (the ring is *catenary* and *equidimensional*). Granting this: a maximal chain refining $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p} \subsetneq \cdots \subsetneq \mathfrak{p}_{\text{top}}$ has length $d$, its part below $\mathfrak{p}$ has length exactly $\operatorname{ht}\mathfrak{p} = h$ (else $\mathfrak{p}$ would have a longer descending chain), and its part above has length exactly $\dim A/\mathfrak{p} = c$; so $h + c = d$.
>
> *Why going down is needed for ES4 Q3a.* To show all maximal chains have length $d$, Noether-normalize: $A$ is integral over $P = k[X_1,\dots,X_d]$, which is *normal* (a UFD), so [[Thm - Going Down for Integrally Closed Domains|going down]] holds for $P \subseteq A$. A chain of $A$ contracts to a chain of $P$ (incomparability keeps it strict); conversely a maximal chain of $P$ (all of length $d$, since $P$ is a polynomial ring) lifts to a maximal chain of $A$ of length $d$ using *both* going up (above each contracted prime) and going down (below it) to fill in without skipping. The going-down step is what guarantees no chain of $A$ over a full chain of $P$ is *shorter* than $d$ — it lets one descend along the preimage to match the base chain link for link. Hence every maximal chain of $A$ has length $d$, and $h + c = d$. $\blacksquare$

> [!note]- Complete formal solution
> Let $A \subseteq B$ be integral.
>
> **$\dim A = \dim B$.** ($\leq$) A strict chain of $A$ is anchored over its bottom by [[Thm - Lying Over|lying over]] and extended by [[Thm - Going Up|going up]] to a strict chain of $B$ of equal length (strict because distinct base primes force distinct lifts); so $\dim B \geq \dim A$. ($\geq$) A strict chain of $B$ contracts to a strict chain of $A$ of equal length, strict because [[Thm - Incomparability|incomparability]] forbids two comparable primes from sharing a contraction; so $\dim A \geq \dim B$. Hence $\dim A = \dim B$, using only lying over, going up, incomparability.
>
> **$\dim k[X_1,\dots,X_n] = n$.** The chain $(0) \subsetneq (X_1) \subsetneq \cdots \subsetneq (X_1,\dots,X_n)$ gives $\geq n$; the bound $\leq n$ comes from transcendence degree. For a finitely generated $k$-domain $A$, Noether normalization makes $A$ integral over $k[X_1,\dots,X_d]$, $d = \operatorname{trdeg}_k\operatorname{Frac} A$, so $\dim A = d$.
>
> **$\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$.** Splicing a height-realising chain below $\mathfrak{p}$ with a chain above $\mathfrak{p}$ gives $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A$. Equality is the catenary/equidimensional property of finitely generated $k$-domains, proved by Noether-normalizing to a polynomial ring and transporting maximal chains using going up *and* going down (the polynomial base being normal); all maximal chains then have length $\dim A$, forcing $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} = \dim A$. $\blacksquare$

> [!warning] Why $\dim A = \dim B$ does NOT need going down, but the formula does
> A natural error is to think the dimension formula and dimension equality are the same difficulty. They are not. **$\dim A = \dim B$** uses only lying over, going up, incomparability — it holds even for non-normal $A$ (it survives the [[Ex - Going down can fail without normality|two-lines-glued counterexample]], where going down fails but $\dim A = \dim B = 1$). **$\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$** is strictly finer: it asserts every maximal chain *through a specific prime* has full length, which can fail in non-catenary rings, and its proof genuinely needs going down (hence normality of the polynomial base from Noether normalization). The lesson: gross dimension is robust; the *position* of an intermediate prime in a maximal chain is the delicate datum that costs normality.

---

# Key Takeaways

**Dimension equality is two one-directional chain arguments, using different theorems.** The reusable principle: to prove $\dim A = \dim B$ across a map, prove $\dim A \leq \dim B$ by *lifting* a chain (going up, anchored by lying over) and $\dim B \leq \dim A$ by *contracting* a chain (incomparability). The asymmetry is the whole insight — one direction goes up, the other comes down, and they use disjoint theorems. The trigger is any "preserve dimension across an integral/finite extension" task. This pattern is the template for *every* dimension-comparison: identify which direction lifts chains and which contracts them, and supply the strictness guarantee for each (distinct contractions for lifting, incomparability for contracting).

**Noether normalization plus dimension preservation is the engine that computes dimension.** Krull dimension is a supremum over chains — uncomputable directly — but a ring integral over a *simple* ring inherits the simple ring's dimension. The standard route: Noether-normalize a finitely generated $k$-domain to a polynomial subring $k[X_1,\dots,X_d]$ (whose dimension $d$ is visible from the obvious chain), then transport $d$ across the integral extension by this theorem, getting $\dim A = d = \operatorname{trdeg}_k\operatorname{Frac} A$. Internalise the pairing "normalize, then preserve dimension" as the way one actually *computes* dimensions of varieties — it reduces every such computation to a transcendence-degree count.

**Distinguish gross dimension (three theorems) from the catenary formula (needs going down).** The sharpest diagnostic from this exercise: $\dim A = \dim B$ is robust and needs no normality, but the formula $\dim A/\mathfrak{p} + \operatorname{ht}\mathfrak{p} = \dim A$ asserts something finer — that the dimension splits cleanly across any prime — and this *position-sensitive* statement requires going down (via a normal Noether-normalization base), because going down is the only tool that lifts a chain *below* $\mathfrak{p}$ to match it link for link. When a problem asks merely for total dimension, reach for the three free theorems; when it asks where an intermediate prime sits or for codimension-plus-dimension, reach for going down and check normality. The going-down-failure exercise [[Ex - Going down can fail without normality]] is the witness that this distinction is real: there $\dim A = \dim B$ holds while going down — and hence the fine structure — fails.
