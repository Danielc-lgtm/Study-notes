---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Prime and Maximal Ideal"
  - "Def - Quotient Ring"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Multiplicative Set and Localization"
  - "Def - The Prime Spectrum (Spec)"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. For an [[Def - Ideal|ideal]] $I\trianglelefteq R$, its [[Def - Radical of an Ideal and the Nilradical|radical]] is $\sqrt I = \{r : r^n\in I \text{ for some } n\geq 1\}$, and the **nilradical** is $\operatorname{nil} R = \sqrt{(0)}$. We write $\operatorname{Spec} R$ for the [[Def - Prime and Maximal Ideal|primes]], $\mathfrak{p}$ for a prime, $R_x = \{x^n\}^{-1}R$ for the localization at $x$, and $\bar x$ for the image of $x$ in a quotient. The full registry is on [[Commutative Algebra IV — Localization]].

---

# Statement

> **Theorem (Krull; Becker Prop. 4.18).** For every ideal $I\trianglelefteq R$,
> $$\sqrt I = \bigcap_{\substack{\mathfrak{p}\in\operatorname{Spec} R \\ I\subseteq\mathfrak{p}}}\mathfrak{p}.$$
> In particular, taking $I = (0)$, the nilradical is the intersection of all prime ideals:
> $$\operatorname{nil} R = \bigcap_{\mathfrak{p}\in\operatorname{Spec} R}\mathfrak{p}.$$

> **Corollary (collapse criterion).** $x\in R$ is nilpotent $\iff R_x = 0 \iff D(x) = \varnothing$. More generally, $x\in\sqrt I \iff (R/I)_{\bar x} = 0$.

---

# Motivation

This theorem is where the chapter's geometry pays a debt to its algebra. The [[Def - Radical of an Ideal and the Nilradical|radical]] $\sqrt I$ was *defined* by a power condition, "some $r^n$ lands in $I$", which is concrete but opaque — it tells you how to test membership but not what the radical *is*. This theorem gives the conceptual identity: $\sqrt I$ is the intersection of all primes above $I$, equivalently the set of functions vanishing on the entire vanishing set $V(I)$. The power-condition definition and the prime-intersection characterisation are the two faces of the radical, and the theorem is the bridge.

The geometric reading is the Nullstellensatz in embryo. A prime $\mathfrak{p}\supseteq I$ is a point of $V(I)$, and "$r\in\mathfrak{p}$" means "$r$ vanishes at that point". So $\bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$ is exactly "the functions vanishing at *every* point of $V(I)$" — and the theorem says these are precisely the $r$ with some power in $I$. This matches the geometric fact that a function vanishes on a variety iff a power of it lies in the defining ideal, which is why a polynomial and its powers cut out the same set. Over an algebraically closed field this becomes Hilbert's Nullstellensatz $I(V(I)) = \sqrt I$; the present theorem is the field-free skeleton that holds for *any* ring.

What makes the proof memorable — and why it belongs in *this* chapter — is the $\supseteq$ direction, the only place in the entire chapter where a prime must be *manufactured from nothing*. To show that an element not in $\sqrt I$ misses some prime above $I$, you cannot just point to a prime; you must *produce* one. The construction is the chapter's signature move: localize at $x$. If $\bar x$ is not nilpotent in $R/I$, then the localization $(R/I)_{\bar x}$ is a *nonzero* ring, so it has a maximal ideal, which pulls back to a prime of $R$ containing $I$ and avoiding $x$. The nonexistence of a prime is converted into the collapse $R_x = 0$, and the collapse criterion "$R_x = 0\iff x$ nilpotent" is the lever. This is the deepest single idea in the chapter: *you force a prime into existence by making a localization nonzero.*

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition for using this theorem is *a question about radicals, nilpotents, or "vanishing everywhere"*.

The first disguised source is **"is $x$ nilpotent?"** or **"is $x\in\sqrt I$?"**. Property $B$: a nilpotence/radical-membership question. The bridge is the collapse criterion: $x$ nilpotent $\iff R_x = 0$, and $x\in\sqrt I\iff(R/I)_{\bar x} = 0$. The non-obvious value: a membership question becomes a "does this ring vanish?" question, often decided by exhibiting or excluding a prime. *Example problem:* show an element lies in $\sqrt I$ by checking it lies in every prime over $I$.

The second disguised source is **"manufacture a prime avoiding a given element"**. Property $B$: a proof needs a prime ideal $\mathfrak{p}\supseteq I$ with $x\notin\mathfrak{p}$. The bridge is the $\supseteq$ construction: if $x\notin\sqrt I$ then $(R/I)_{\bar x}\neq 0$ has a maximal ideal, contracting to such a $\mathfrak{p}$. The non-obvious value: existence of a prime is produced by a nonvanishing localization. *Example problem:* showing a non-nilpotent element is detected at some point of the spectrum.

The third disguised source is **"$r$ vanishes on all of $V(I)$"**. Property $B$: a function vanishes at every point of a variety. The bridge is that $r\in\bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p} = \sqrt I$, so $r^n\in I$. The non-obvious value: "vanishes everywhere on $V(I)$" upgrades to the *algebraic* statement "a power lies in $I$". *Example problem:* the Nullstellensatz correspondence, where vanishing-on-a-variety is converted to radical membership.

**Targets (Output Amplification)**

The conclusion is *$\sqrt I = \bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$ (and $\operatorname{nil} R = \bigcap\mathfrak{p}$)*.

Combine with **$\sqrt I = I$ for radical ideals**. A radical ideal equals the intersection of the primes above it, so *radical ideals are exactly the intersections of primes*. The further result $E$: the closed sets $V(I)$ of $\operatorname{Spec} R$ biject with radical ideals, the basic dictionary of [[Def - The Prime Spectrum (Spec)|the spectrum]]. Nonobvious because it characterises which ideals "come from geometry".

Combine with **$V(I) = V(\sqrt I)$ and the topology**. The theorem implies $V(I)$ depends only on $\sqrt I$, so the operation $I\mapsto\sqrt I$ is "topological closure of the defining data". The further result $E$: the radical is the largest ideal cutting out $V(I)$, and the assignment $V\mapsto I(V) = \bigcap_{\mathfrak{p}\in V}\mathfrak{p}$ is its inverse on radical ideals. Nonobvious because it makes $\sqrt{\cdot}$ a closure operator matching topological closure.

Combine with **$\operatorname{nil} R = \bigcap\mathfrak{p}$ and reducedness**. A ring is reduced iff $\operatorname{nil} R = 0$ iff the primes intersect in $0$ iff functions are determined by values. The further result $E$: reducedness is "no function vanishes everywhere without being zero", and it is a [[Def - Local Property (Localizable and Local-to-Global)|local property]] — see [[Ex - Being reduced is a local property]]. Nonobvious because it links the global intersection of primes to a pointwise (local) condition.

---

# Why Is It True

The two inclusions have completely different flavours, and the asymmetry is the whole story.

The $\subseteq$ direction is trivial and uses only what a prime *is*: if $x\in\sqrt I$ then $x^n\in I$ for some $n$, and any prime $\mathfrak{p}\supseteq I$ contains $x^n$, hence contains $x$ (primality: $x\cdot x^{n-1}\in\mathfrak{p}\Rightarrow x\in\mathfrak{p}$ or $x^{n-1}\in\mathfrak{p}$, induct). So $x$ lies in every prime above $I$. A prime "swallows roots" — this direction is automatic.

The $\supseteq$ direction is the content, and it is a pure *existence* problem: given $x\notin\sqrt I$, we must produce a prime $\mathfrak{p}\supseteq I$ with $x\notin\mathfrak{p}$, certifying that $x$ is *not* in the intersection. Where does such a prime come from? It cannot be written down. It is *forced into existence* by a nonvanishing ring. Pass to $R/I$ and the image $\bar x$; "$x\notin\sqrt I$" means "$\bar x$ is not nilpotent in $R/I$". By the collapse criterion, the localization $(R/I)_{\bar x}$ is therefore *nonzero*. Every nonzero ring has a maximal ideal (Zorn). That maximal ideal is prime, and under the [[Thm - Prime Ideals of a Localization|prime correspondence]] it pulls back to a prime $\mathfrak{p}$ of $R/I$ disjoint from $\{\bar x^n\}$, then lifts to a prime of $R$ containing $I$ and avoiding $x$. Done.

**One-line mechanism: $x\notin\sqrt I\iff\bar x$ not nilpotent $\iff(R/I)_{\bar x}\neq 0\iff(R/I)_{\bar x}$ has a maximal ideal $\iff$ there is a prime over $I$ missing $x$. The radical is the intersection of primes because *the only way to be in every prime is to be nilpotent.***

The pivot is the collapse criterion $R_x = 0\iff x$ nilpotent, itself immediate: $R_x = \{x^n\}^{-1}R = 0\iff 0\in\{x^n\}\iff x^n = 0$ for some $n$ ($S^{-1}R = 0\iff 0\in S$, from the [[Def - Multiplicative Set and Localization|fraction model]]). So localizing at $x$ converts "is $x$ nilpotent?" into "does this ring collapse?", and a non-collapse manufactures a prime. This single manoeuvre — *localize at an element to force a prime into existence* — is worth memorising as a unit; it recurs throughout commutative algebra wherever a prime avoiding a given element is needed.

---

# What Makes This Hard

The $\subseteq$ direction lulls you; the difficulty is entirely in $\supseteq$, and specifically in realising that it is an *existence* statement requiring a prime to be *built*, not found. The non-obvious step is the localize-at-$x$ construction: passing to $(R/I)_{\bar x}$ precisely so that non-nilpotence becomes non-vanishing, and then invoking "nonzero ring has a maximal ideal" to summon the prime. The common error is to attempt $\supseteq$ by direct manipulation of the power condition, which goes nowhere because you cannot produce a prime without the localization-plus-Zorn machine. The reliance on the axiom of choice (Zorn) here is essential and unavoidable.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The $\subseteq$ inclusion is immediate from primality. For $\supseteq$, prove the contrapositive: if $x\notin\sqrt I$, manufacture a prime over $I$ avoiding $x$ by localizing at $x$ in $R/I$ — the localization is nonzero because $\bar x$ is non-nilpotent, so it has a maximal ideal, which contracts and lifts to the desired prime.

**Subgoal decomposition:**

1. **Easy inclusion.** Show $\sqrt I\subseteq\bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$.
   - *Hint:* $x^n\in I\subseteq\mathfrak{p}$ and $\mathfrak{p}$ prime force $x\in\mathfrak{p}$.
   - *Why needed:* the trivial half; "primes swallow roots".

2. **Collapse criterion.** Show $R_x = 0\iff x$ nilpotent.
   - *Hint:* $\{x^n\}^{-1}R = 0\iff 0\in\{x^n\}\iff x^n = 0$.
   - *Why needed:* converts non-nilpotence to non-vanishing, the engine of step 3.

3. **Hard inclusion via manufactured prime.** Show $x\notin\sqrt I\Rightarrow\exists\mathfrak{p}\supseteq I$ with $x\notin\mathfrak{p}$.
   - *Hint:* in $R/I$, $\bar x$ non-nilpotent $\Rightarrow(R/I)_{\bar x}\neq 0\Rightarrow$ it has a maximal ideal $\Rightarrow$ contract and lift to a prime of $R$ over $I$ missing $x$.
   - *Why needed:* it is the existence statement; without it the intersection could be larger than $\sqrt I$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Primes swallow roots
> **Statement:** If $\mathfrak{p}$ is prime and $x^n\in\mathfrak{p}$ for some $n\geq 1$, then $x\in\mathfrak{p}$.
>
> **Hint:** Induct on $n$ using the defining property of a prime.
>
> **Why needed:** It is the entire $\subseteq$ inclusion: a power in $I\subseteq\mathfrak{p}$ forces the element into $\mathfrak{p}$.
>
> > [!note]- Full proof
> > For $n = 1$ there is nothing to prove. For $n > 1$, $x^n = x\cdot x^{n-1}\in\mathfrak{p}$, and $\mathfrak{p}$ prime gives $x\in\mathfrak{p}$ or $x^{n-1}\in\mathfrak{p}$; in the latter case the inductive hypothesis gives $x\in\mathfrak{p}$. Hence $\sqrt{\mathfrak{p}} = \mathfrak{p}$, and for any $\mathfrak{p}\supseteq I$ with $x\in\sqrt I$ (so $x^n\in I\subseteq\mathfrak{p}$) we get $x\in\mathfrak{p}$.

> [!note]- Lemma 2: The collapse criterion
> **Statement:** $R_x = \{x^n\}^{-1}R = 0\iff x$ is nilpotent.
>
> **Hint:** $S^{-1}R = 0\iff 0\in S$, and $S = \{x^n\}$ contains $0$ iff a power of $x$ is $0$.
>
> **Why needed:** It translates "non-nilpotent" into "nonzero localization", which then yields a prime.
>
> > [!note]- Full proof
> > From the [[Def - Multiplicative Set and Localization|fraction model]], $S^{-1}R = 0$ iff $\tfrac11 = \tfrac01$ iff $0\in S$ (take $u = 0$ in the relation $u(1) = 0$). For $S = \{x^n : n\geq 0\}$, $0\in S\iff x^n = 0$ for some $n\geq 0\iff x$ is nilpotent. Hence $R_x = 0\iff x$ nilpotent. (Applied in $R/I$: $(R/I)_{\bar x} = 0\iff\bar x$ nilpotent$\iff x^n\in I$ for some $n\iff x\in\sqrt I$.)

> [!note]- Lemma 3: Manufacturing a prime by localizing at $x$
> **Statement:** If $x\notin\sqrt I$, there is a prime $\mathfrak{p}\supseteq I$ with $x\notin\mathfrak{p}$.
>
> **Hint:** $(R/I)_{\bar x}$ is nonzero, so has a maximal ideal; pull it back through the prime correspondence and the quotient.
>
> **Why needed:** It is the $\supseteq$ inclusion, the heart of the theorem and the chapter's prime-manufacturing technique.
>
> > [!note]- Full proof
> > Since $x\notin\sqrt I$, by Lemma 2 the ring $A := (R/I)_{\bar x}$ is nonzero, where $\bar x$ is the image of $x$ in $R/I$. A nonzero ring has a maximal ideal $\mathfrak{m}_A$ (Zorn), which is prime. By the [[Thm - Prime Ideals of a Localization|prime correspondence]] for the localization $R/I\to(R/I)_{\bar x}$, $\mathfrak{m}_A$ contracts to a prime $\bar{\mathfrak{p}}$ of $R/I$ disjoint from $\{\bar x^n\}$ — in particular $\bar x\notin\bar{\mathfrak{p}}$. Pulling back along $R\to R/I$, the preimage $\mathfrak{p}$ of $\bar{\mathfrak{p}}$ is a prime of $R$ with $I\subseteq\mathfrak{p}$ (as $\bar{\mathfrak{p}}\trianglelefteq R/I$) and $x\notin\mathfrak{p}$ (since $\bar x\notin\bar{\mathfrak{p}}$). So $x$ misses a prime above $I$, i.e. $x\notin\bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$.

---

# Formal Proof

> [!note]- Complete formal proof
> **($\subseteq$).** Let $x\in\sqrt I$, so $x^n\in I$ for some $n\geq 1$. For any prime $\mathfrak{p}\supseteq I$, $x^n\in I\subseteq\mathfrak{p}$, and by Lemma 1, $x\in\mathfrak{p}$. As $\mathfrak{p}$ was an arbitrary prime above $I$, $x\in\bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$.
>
> **($\supseteq$).** We prove the contrapositive: if $x\notin\sqrt I$, then $x\notin\bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$, i.e. some prime above $I$ omits $x$. This is exactly Lemma 3: $x\notin\sqrt I$ makes $(R/I)_{\bar x}$ nonzero (Lemma 2), hence it has a maximal ideal, which contracts and lifts to a prime $\mathfrak{p}\supseteq I$ with $x\notin\mathfrak{p}$.
>
> Combining, $\sqrt I = \bigcap_{\mathfrak{p}\supseteq I}\mathfrak{p}$. Taking $I = (0)$ gives $\operatorname{nil} R = \bigcap_{\mathfrak{p}\in\operatorname{Spec} R}\mathfrak{p}$.
>
> **Corollary.** $x$ nilpotent $\iff x\in\operatorname{nil} R = \sqrt{(0)}\iff R_x = 0$ (Lemma 2) $\iff D(x) = \varnothing$ (no prime omits $x$, i.e. $\operatorname{Spec}(R_x) = \varnothing$); and $x\in\sqrt I\iff(R/I)_{\bar x} = 0$ likewise. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Detecting nilpotence in a quotient of a polynomial ring.** To decide whether $\bar f\in k[X_1,\dots,X_n]/I$ is nilpotent, the criterion says: check whether $f$ vanishes on $V(I)$, equivalently whether $(R/I)_{\bar f} = 0$. Over an algebraically closed field this is the Nullstellensatz test. Nonobvious recognition: nilpotence is "vanishing at every point", checkable geometrically.

**The Jacobson radical versus the nilradical.** The intersection of all *maximal* ideals (the Jacobson radical $J(R)$) contains $\operatorname{nil} R = \bigcap$ all primes, and they coincide for rings where every prime is an intersection of maximals (Jacobson rings, e.g. finitely generated algebras over a field). The present theorem is the prime-side half. Nonobvious because it isolates exactly when "vanishing at closed points" equals "vanishing everywhere".

**Reduced rings embed in products of domains.** Since $\operatorname{nil} R = \bigcap\mathfrak{p}$, a reduced ring injects into $\prod_{\mathfrak{p}} R/\mathfrak{p}$, a product of domains — an element is zero iff it vanishes modulo every prime. This is the structural meaning of "reduced". Nonobvious because it turns the abstract $\operatorname{nil} R = 0$ into a concrete embedding into domains, used in [[Ex - Being reduced is a local property]].

---

# Bridges

- **[[Def - Radical of an Ideal and the Nilradical|Radical and nilradical]]** — this theorem is the geometric *characterisation* of the radical defined there by a power condition: $\sqrt I$ is the intersection of the primes above $I$, equivalently the functions vanishing on $V(I)$. It is what makes "radical ideal" mean "intersection of primes".

- **[[Thm - Prime Ideals of a Localization|Prime ideals of a localization]]** — supplies the manufacturing step: a maximal ideal of the nonzero ring $(R/I)_{\bar x}$ contracts to a prime of $R/I$ avoiding $\bar x$, which is exactly the prime correspondence for the localization at $x$.

- **[[Def - The Prime Spectrum (Spec)|The prime spectrum]]** — the theorem says $\sqrt I$ is the radical-ideal closure matching the topological closure $V(I)$, and that a function vanishing at every point is nilpotent: $\bigcap_{\mathfrak{p}}\mathfrak{p} = \operatorname{nil} R$ is "the functions invisible to the topology".

- **Nullstellensatz** — over an algebraically closed field, [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz|Hilbert's Nullstellensatz]] upgrades this to $I(V(I)) = \sqrt I$ with $V(I)$ a genuine subset of $k^n$. The present theorem is the field-free, point-free skeleton that holds in any ring.

---

# Unlocked by This

> [!tip] The Nullstellensatz and the radical-ideal/variety dictionary *(from Algebraic Geometry)*
> Over an algebraically closed field, **Hilbert's Nullstellensatz** strengthens this theorem to $I(V(I)) = \sqrt I$, making $I\mapsto V(I)$ a bijection between *radical ideals* of $k[X_1,\dots,X_n]$ and algebraic subsets of $k^n$. The present statement is exactly the part that survives without algebraic closure: a function lies in $\sqrt I$ iff it vanishes at every point (prime) of $V(I)$. So this theorem is the ring-theoretic engine of the entire ideal–variety dictionary, developed in [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

> [!tip] Manufacturing primes: the existence backbone of commutative algebra *(from Commutative Algebra)*
> The technique "localize at $x$; if $x$ is not nilpotent then $R_x\neq 0$ has a maximal ideal, which contracts to a prime missing $x$" is the standard way primes are **produced** throughout the subject — in proofs that minimal primes exist, that the support of a module is closed, that integral extensions have primes lying over (going up). Whenever a proof needs "choose a prime avoiding this element" or "there is a prime with this property", this localization-plus-Zorn manoeuvre is the tool, and it is the one genuinely non-constructive (choice-dependent) idea localization contributes.
