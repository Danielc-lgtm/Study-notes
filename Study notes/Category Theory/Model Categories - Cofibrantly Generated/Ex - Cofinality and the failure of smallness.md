---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Transfinite Composition and Smallness"
  - "Def - Limit and Colimit"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Smallness of an object $A$ relative to a class $D$ is required only for *regular* cardinals $\lambda$. This exercise shows the regularity hypothesis is essential, by exhibiting failures at singular and at too-short lengths.

(a) Let $A = \mathbb{N}$ in $\mathbf{Set}$. Build an $\omega$-sequence $X_0\to X_1\to\cdots$ whose colimit is $\mathbb{N}$, and a map $A\to\mathrm{colim}$ that factors through *no* finite stage. Conclude $\mathbb{N}$ is not $\aleph_0$-small "at length $\omega$," and explain why this is consistent with $\mathbb{N}$ being small.

(b) Let $A = \mathbb{N}$ and $\lambda = \aleph_\omega$ (a *singular* cardinal, with cofinality $\mathrm{cf}(\aleph_\omega) = \aleph_0$). Build a $\lambda$-sequence and a map $\mathbb{N}\to\mathrm{colim}_{\beta<\lambda} X_\beta$ that factors through no bounded stage $X_\beta$ with $\beta<\lambda$, even though $|\mathbb{N}| = \aleph_0 < \aleph_\omega = \lambda$. Pinpoint where the argument of [[Ex - Every set is small in the category of sets]] breaks, and identify the role of cofinality.

(c) Conclude that "$A$ is $\kappa$-small relative to $D$" must quantify over *regular* $\lambda\geq\kappa$, not all $\lambda\geq\kappa$.

**Recall:**

![[Def - Transfinite Composition and Smallness#The Definition]]

The **cofinality** $\mathrm{cf}(\lambda)$ is the least cardinality of a cofinal subset of $\lambda$; $\lambda$ is **regular** if $\mathrm{cf}(\lambda) = \lambda$ and **singular** otherwise. The cardinal $\aleph_\omega = \sup_n\aleph_n$ is singular: the countable set $\{\aleph_n : n\in\mathbb{N}\}$ is cofinal, so $\mathrm{cf}(\aleph_\omega) = \aleph_0 < \aleph_\omega$.

---

# Convergent Strategy

**Problem class:** This is a counterexample-construction problem — exhibiting the *failure* of smallness to delineate the exact hypotheses. It is the ⭐⭐⭐ stress test of the smallness definition, complementary to the positive certifications in the other two §1 exercises.

**Assumption pattern:** The constructions exploit two ways a map can escape to infinity: (a) length $\omega$ is *below* the threshold $\kappa = \aleph_1$ for $\mathbb{N}$, so escape is allowed there; (b) singular cofinality lets a countable map climb a *short cofinal ladder* even when the total length $\lambda$ exceeds $|A|$. The key recognition is that smallness is about *cofinality*, not raw cardinality of $\lambda$.

**Theorem routing:** The route in (a) is to make the colimit $\mathbb{N}$ itself and use the identity map, which by construction meets every stage. The route in (b) is to index the tower so that a countable cofinal subsequence $\{\aleph_n\}$ carries genuinely new data at each rung, and route a function $\mathbb{N}\to\mathrm{colim}$ to hit the $n$-th rung with its $n$-th value — exploiting $\mathrm{cf}(\aleph_\omega) = \aleph_0 = |A|$.

**Key decision point:** The non-obvious choice in (b) is to make the *cofinal* subsequence, not the whole tower, carry the escape. A naive tower where new elements appear at every successor would still be probed boundedly by $\mathbb{N}$ at a regular $\lambda$; the singular construction must concentrate the novelty on a length-$\mathrm{cf}(\lambda)$ cofinal ladder so a map of size $|A| = \mathrm{cf}(\lambda)$ can ride it to the top.

---

# Legal Operations Used

1. **Operation 5 from the topic page (certify smallness by cardinality), used in reverse.** Here we exhibit where the cardinality/regularity certification *fails*, isolating the regularity hypothesis as the load-bearing one.

2. **Operation 1 from the topic page (form the closures of a set).** The constructions are colimits of $\lambda$-sequences, the diagrams against which smallness is tested.

---

# Hints

> [!note]- Hint 1 (part a)
> Take $X_n = \{0, 1, \dots, n-1\}$ with inclusions. The colimit is $\mathbb{N}$. The identity $\mathbb{N}\to\mathbb{N} = \mathrm{colim}$ cannot factor through any finite $X_n$, since $X_n$ omits $n$.

> [!note]- Hint 2 (part a)
> This does not contradict smallness of $\mathbb{N}$: smallness is only claimed for $\lambda\geq\kappa = \aleph_1$, and $\omega < \aleph_1$. At length $\omega$ the threshold is not met, so no factorization is promised. Restore $\lambda\geq\aleph_1$ regular and the factorization returns (a countable image is bounded below $\aleph_1$).

> [!note]- Hint 3 (part b)
> Index a $\lambda$-sequence ($\lambda = \aleph_\omega$) so that at the cofinal stages $\aleph_0 < \aleph_1 < \aleph_2 < \cdots$ a brand-new "marker" element $m_n$ is added that survives to the colimit, while between consecutive markers nothing essential changes. Then $\mathrm{colim}$ contains all markers $\{m_n\}$.

> [!note]- Hint 4 (part b)
> Define $f : \mathbb{N}\to\mathrm{colim}$ by $f(n) = m_n$. Each $m_n$ first appears at stage $\aleph_n$, so any stage $X_\beta$ containing the whole image must have $\beta\geq\sup_n\aleph_n = \aleph_\omega = \lambda$ — not a bounded stage. The supremum argument of the positive exercise breaks because $\sup_n\aleph_n$ is *not* $<\lambda$: cofinality $\mathrm{cf}(\lambda) = \aleph_0 = |A|$ lets the $|A|$-many per-element stages be cofinal.

---

# Solution

Part (a) shows escape below the threshold; part (b) shows escape at a singular length despite $|A|<\lambda$; part (c) extracts the conclusion. The unifying point: smallness fails exactly when the per-element stages of a map out of $A$ can be cofinal in $\lambda$, which happens when $\mathrm{cf}(\lambda)\leq|A|$ — impossible for regular $\lambda > |A|$, possible for singular $\lambda$ or for $\lambda\leq|A|$.

**Step 1 (part a): $\mathbb{N}$ escapes at length $\omega$, but this is below threshold.**

> [!note]- Derivation
> Let $X_n = \{0,\dots,n-1\}\subseteq\mathbb{N}$ with the inclusions $X_n\hookrightarrow X_{n+1}$; this is an $\omega$-sequence with $\mathrm{colim}_n X_n = \mathbb{N}$. The identity $\mathrm{id} : \mathbb{N}\to\mathbb{N} = \mathrm{colim}$ does not factor through any $X_n$, because $n\in\mathbb{N}$ but $n\notin X_n$. So the surjectivity half of the smallness map fails at $\lambda = \omega$.
>
> This is consistent with $\mathbb{N}$ being small: smallness of $\mathbb{N}$ is the statement that the bijection holds for all *regular* $\lambda\geq\aleph_1$, and $\omega = \aleph_0 < \aleph_1 = |\mathbb{N}|^+$ is below the threshold $\kappa$. Indeed at any regular $\lambda\geq\aleph_1$, a map $\mathbb{N}\to\mathrm{colim}$ uses $\aleph_0 < \lambda$ stages, whose sup is $<\lambda$ by regularity, so it factors — $\mathbb{N}$ *is* small. The length-$\omega$ failure merely shows the threshold cannot be lowered to $\aleph_0$.

**Step 2 (part b): $\mathbb{N}$ escapes at the singular length $\aleph_\omega$ despite $\aleph_0 < \aleph_\omega$.**

> [!note]- Derivation
> Build a $\lambda$-sequence of length $\lambda = \aleph_\omega$ as follows. For each $n\in\mathbb{N}$ introduce a marker symbol $m_n$. Define $X_\beta = \{m_n : \aleph_n\leq\beta\}$ for $\beta < \aleph_\omega$ (so $m_n$ first appears exactly at stage $\beta = \aleph_n$), with the evident inclusions $X_\beta\hookrightarrow X_{\beta'}$ for $\beta\leq\beta'$; at limit ordinals this is already the union, so the colimit-preservation condition holds and it is a genuine $\lambda$-sequence. The colimit is $\mathrm{colim}_{\beta<\aleph_\omega} X_\beta = \{m_n : n\in\mathbb{N}\}$, the full set of markers.
>
> Define $f : \mathbb{N}\to\mathrm{colim}$ by $f(n) = m_n$. Suppose $f$ factored through some bounded $X_\beta$ with $\beta < \aleph_\omega$. Then $X_\beta$ would contain every marker $m_n$, so $\aleph_n\leq\beta$ for every $n$, giving $\beta\geq\sup_n\aleph_n = \aleph_\omega$ — contradicting $\beta < \aleph_\omega$. So $f$ factors through no bounded stage: smallness fails at $\lambda = \aleph_\omega$, even though $|\mathbb{N}| = \aleph_0 < \aleph_\omega = \lambda$.
>
> **Where the positive argument breaks.** In [[Ex - Every set is small in the category of sets]], surjectivity rested on $\beta^* = \sup_a\beta(a) < \lambda$. Here $\beta(n) = \aleph_n$ and $\beta^* = \sup_n\aleph_n = \aleph_\omega = \lambda$, *not* $<\lambda$. The supremum of $|A| = \aleph_0$ ordinals below $\lambda$ reached $\lambda$ precisely because $\mathrm{cf}(\lambda) = \aleph_0\leq|A|$: the countably many per-element stages form a cofinal ladder. Regularity ($\mathrm{cf}(\lambda) = \lambda > |A|$) is exactly what forbids this.

**Step 3 (part c): the definition must quantify over regular $\lambda$.**

> [!note]- Derivation
> Part (b) exhibits, for $A = \mathbb{N}$ and any cardinal threshold $\kappa$, a *singular* $\lambda\geq\kappa$ (take $\aleph_\omega$ or any singular cardinal of cofinality $\leq\aleph_0$ above $\kappa$) at which the smallness bijection fails. So "the bijection holds for all $\lambda\geq\kappa$" is *never* satisfiable for any $A$ with infinitely many elements — the definition would make nothing small. Restricting to regular $\lambda\geq\kappa$ removes exactly the singular counterexamples, because for regular $\lambda > |A|$ the supremum of $\leq|A|$ stages stays below $\lambda$. Hence the definition of [[Def - Transfinite Composition and Smallness|smallness]] quantifies over regular $\lambda\geq\kappa$, and must.

> [!note]- Complete formal solution
> (a) $X_n = \{0,\dots,n-1\}$, colimit $\mathbb{N}$; the identity escapes every finite stage, so smallness fails at $\lambda = \omega$. Consistent with $\mathbb{N}$ small because $\omega = \aleph_0 < \aleph_1 = |\mathbb{N}|^+ = \kappa$, below threshold; at regular $\lambda\geq\aleph_1$ a countable image is bounded by regularity.
>
> (b) $\lambda = \aleph_\omega$, $X_\beta = \{m_n : \aleph_n\leq\beta\}$ with inclusions; colimit $\{m_n : n\in\mathbb{N}\}$. The map $f(n) = m_n$ factors through $X_\beta$ only if $\beta\geq\sup_n\aleph_n = \aleph_\omega$, impossible for $\beta<\lambda$. The positive supremum argument fails because $\sup_n\beta(n) = \aleph_\omega = \lambda$: the $|A| = \aleph_0$ per-element stages are cofinal, since $\mathrm{cf}(\aleph_\omega) = \aleph_0\leq|A|$.
>
> (c) For any $\kappa$ there is a singular $\lambda\geq\kappa$ with $\mathrm{cf}(\lambda)\leq\aleph_0\leq|A|$ (for infinite $A$), giving an escape; so the bijection cannot hold for all $\lambda\geq\kappa$. Restricting to regular $\lambda$ excludes these, and is necessary and sufficient for the definition to be non-vacuous. $\blacksquare$

---

# Key Takeaways

**Smallness is governed by cofinality, not by the raw size of the tower.** The headline lesson is that a map out of $A$ escapes to infinity exactly when the per-element stages can be made cofinal, which requires $\mathrm{cf}(\lambda)\leq|A|$. A long tower ($\lambda$ huge) is not enough to prevent escape if it is *singular* with small cofinality; conversely a regular $\lambda$ just above $|A|$ already forces boundedness. This is why the definition's quantifier is "regular $\lambda\geq\kappa$" — the regularity is doing all the work, and the bare inequality $|A|<\lambda$ is insufficient. Whenever you reason about whether a transfinite construction terminates, ask about the cofinality of its length, not its cardinality.

**Below-threshold failures are not contradictions; they calibrate the threshold.** Part (a) shows $\mathbb{N}$ escaping at length $\omega$, which feels like $\mathbb{N}$ being "not small" — but smallness is a statement about *large enough* $\lambda$, and $\omega$ is below $\kappa = \aleph_1$. The failure precisely calibrates the threshold: it shows $\kappa$ cannot be lowered to $\aleph_0$. This distinction — between a genuine failure of smallness (escape at arbitrarily large regular $\lambda$) and a below-threshold artifact (escape only at small or singular $\lambda$) — is essential when certifying smallness for the small object argument, where one must choose the length $\lambda$ above *all* generator thresholds and ensure it is regular.

**Counterexamples delineate hypotheses better than proofs do.** The positive exercises establish smallness; this one shows what each clause of the hypothesis buys by removing it. Dropping regularity (singular $\lambda$) destroys smallness for every infinite object; dropping the strict threshold ($\lambda = |A|$) destroys it at one length. The general methodological point — that the cleanest way to understand why a definition has exactly its quantifiers is to build the object that fails the moment a quantifier is relaxed — recurs across the subject: it is how one understands why generators must be a *set*, why factorizations need smallness, and why both recognition-theorem conditions (i) and (ii) are independent. Reaching for the minimal-failure construction is a transferable diagnostic habit.
