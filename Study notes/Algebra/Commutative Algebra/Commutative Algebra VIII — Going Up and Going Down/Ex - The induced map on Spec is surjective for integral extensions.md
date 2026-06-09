---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Lying Over"
  - "Def - The Induced Map on Spectra"
  - "Def - Lying Over, Going Up, Going Down"
  - "Thm - Prime Ideals of a Localization"
  - "Thm - Integral Extensions and Fields (Domain Criterion)"
  - "Def - Multiplicative Set and Localization"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A \subseteq B$ be an integral extension of rings. Prove that the induced map
$$\iota^* : \operatorname{Spec} B \longrightarrow \operatorname{Spec} A, \qquad \mathfrak{q} \mapsto \mathfrak{q} \cap A$$
is **surjective**. That is, show directly that for every $\mathfrak{p} \in \operatorname{Spec} A$ there is a prime $\mathfrak{q} \in \operatorname{Spec} B$ with $\mathfrak{q} \cap A = \mathfrak{p}$.

The intended route: localize at $\mathfrak{p}$, forming $B_{\mathfrak{p}} = (A \setminus \mathfrak{p})^{-1}B$; show $B_{\mathfrak{p}} \neq 0$, so it has a maximal ideal $\mathfrak{m}$; show that the integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ forces $\mathfrak{m}$ to contract to the maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$ of the local ring $A_{\mathfrak{p}}$; then contract $\mathfrak{m}$ back to a prime $\mathfrak{q}$ of $B$ and verify $\mathfrak{q} \cap A = \mathfrak{p}$.

**Recall:**

The objects in play are the induced (contraction) map, lying over as surjectivity, localization at a prime, the prime-correspondence theorem, and the domain/field criterion for integral extensions.

![[Def - Lying Over, Going Up, Going Down#Lying over]]

By [[Def - Lying Over, Going Up, Going Down|definition]], "$\iota$ satisfies lying over" *means* $\iota^*$ is surjective; this exercise is the proof that integral extensions satisfy it.

![[Thm - Prime Ideals of a Localization#Statement]]

For a multiplicative set $S \subseteq A$, [[Def - Multiplicative Set and Localization|localization]] $B_{\mathfrak{p}} = S^{-1}B$ ($S = A \setminus \mathfrak{p}$) has $B_{\mathfrak{p}} = 0 \iff 0 \in S$. The [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]] makes primes of $S^{-1}B$ correspond to primes of $B$ disjoint from $S$.

The [[Thm - Integral Extensions and Fields (Domain Criterion)|domain/field criterion]]: for an integral extension of rings, a prime $\mathfrak{m}$ of the bigger ring is maximal iff its contraction is maximal — because the quotient extension is an integral extension of domains, and there one is a field iff the other is.

---

# Convergent Strategy

**Problem class.** This is a *prove-surjectivity-of-the-fibre-map* problem — equivalently, the existence form of lying over. As the [[Commutative Algebra VIII — Going Up and Going Down#Problem-Solving Strategy|topic-page strategy]] records, to produce a prime over a given prime you translate the fibre into $\operatorname{mSpec} B_{\mathfrak{p}}$ and use that a non-zero ring has a maximal ideal.

**Assumption pattern.** The single hypothesis "$A \subseteq B$ integral" does two jobs. It makes $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ integral (integrality survives localization), which is what lets the domain criterion promote "contracts to $\mathfrak{p}A_{\mathfrak{p}}$" to "is maximal". And, combined with $\mathfrak{p}$ being prime (so $A \setminus \mathfrak{p}$ avoids $0$), it makes $B_{\mathfrak{p}}$ non-zero. The recognisable trigger is "show *some* prime exists with a prescribed contraction" — which always routes through a non-vanishing localization.

**Theorem routing.** The route is: form $B_{\mathfrak{p}} = (A\setminus\mathfrak{p})^{-1}B$; observe $0 \notin A \setminus \mathfrak{p}$, so by [[Def - Multiplicative Set and Localization|the localization]] $B_{\mathfrak{p}} \neq 0$, hence it has a maximal ideal $\mathfrak{m}$; the integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ and the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain criterion]] force $\mathfrak{m} \cap A_{\mathfrak{p}}$ to be the maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$; the [[Thm - Prime Ideals of a Localization|prime correspondence]] contracts $\mathfrak{m}$ to a prime $\mathfrak{q}$ of $B$ with $\mathfrak{q} \cap A = \mathfrak{p}$.

**Key decision point.** The non-obvious move is to localize at the *base* prime $\mathfrak{p}$, forming the unusual ring $B_{\mathfrak{p}} = (A\setminus\mathfrak{p})^{-1}B$ — "$B$ localized at a subset of $A$", which is *not* a local ring and *not* a localization of $B$ at a prime of $B$. The temptation is to localize $B$ at a prime of $B$, which begs the question (you would need the prime you are trying to construct). The second decision is to take a *maximal* ideal of $B_{\mathfrak{p}}$ rather than any prime — only maximal ideals are guaranteed to contract to $\mathfrak{p}$ exactly, via the domain criterion; an arbitrary prime of $B_{\mathfrak{p}}$ contracts to some prime $\subseteq \mathfrak{p}$, which is too weak.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VIII — Going Up and Going Down#Legal Operations|the topic page's Legal Operations]]:

1. **Translate the fibre into $\operatorname{mSpec} B_{\mathfrak{p}}$ (operation 1).** Recognise that primes over $\mathfrak{p}$ are exactly the maximal ideals of $B_{\mathfrak{p}}$.

2. **Force a prime into existence by non-vanishing of a localization (operation 2).** $0 \notin A \setminus \mathfrak{p}$, so $B_{\mathfrak{p}} \neq 0$; a non-zero ring has a maximal ideal.

3. **Use that integrality passes to localizations (operation 4).** $A \subseteq B$ integral $\Rightarrow A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ integral, keeping the hypothesis alive in the localized ring.

4. **Reduce maximality to the base via the domain criterion (operation 6).** $\mathfrak{m}$ maximal in $B_{\mathfrak{p}}$ contracts to the maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$ of $A_{\mathfrak{p}}$.

---

# Hints

> [!note]- Hint 1
> You want *some* prime of $B$ over $\mathfrak{p}$. The existence of a prime is almost always the existence of a maximal ideal in a *non-zero* ring. Which ring's maximal ideals are the primes over $\mathfrak{p}$? (Not $B$ itself — localize.)

> [!note]- Hint 2
> Localize at the base prime: $B_{\mathfrak{p}} = (A \setminus \mathfrak{p})^{-1}B$. This is *not* a local ring, and *not* "$B$ at a prime of $B$" — it is $B$ with the elements of $A$ outside $\mathfrak{p}$ inverted. Why is $B_{\mathfrak{p}} \neq 0$? Because $0 \notin A \setminus \mathfrak{p}$ (as $\mathfrak{p}$ is a proper ideal). A non-zero ring has a maximal ideal $\mathfrak{m}$.

> [!note]- Hint 3
> The extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral (integrality survives localization). By the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain criterion]], a prime of $B_{\mathfrak{p}}$ is maximal iff its contraction to $A_{\mathfrak{p}}$ is maximal. So the maximal ideal $\mathfrak{m}$ contracts to a maximal ideal of $A_{\mathfrak{p}}$ — and $A_{\mathfrak{p}}$ has *only one*, namely $\mathfrak{p}A_{\mathfrak{p}}$.

> [!note]- Hint 4
> So $\mathfrak{m} \cap A_{\mathfrak{p}} = \mathfrak{p}A_{\mathfrak{p}}$. Contract $\mathfrak{m}$ all the way to $B$: let $\mathfrak{q}$ be the preimage of $\mathfrak{m}$ under $B \to B_{\mathfrak{p}}$. By the localization correspondence $\mathfrak{q}$ is prime, and chasing the commuting square $A \to B \to B_{\mathfrak{p}}$ versus $A \to A_{\mathfrak{p}} \to B_{\mathfrak{p}}$ gives $\mathfrak{q} \cap A = \mathfrak{p}$.

---

# Solution

The proof is the "localize to force a prime into existence" manoeuvre. Localizing $B$ at the multiplicative set $A \setminus \mathfrak{p}$ produces a non-zero ring (because $0 \notin A \setminus \mathfrak{p}$); a non-zero ring has a maximal ideal; and the integral extension plus the domain criterion guarantee that this maximal ideal contracts to $\mathfrak{p}$ exactly, delivering the required prime of $B$.

**Step 1: Localize at $\mathfrak{p}$; the localized extension is integral and $B_{\mathfrak{p}} \neq 0$.**

Set $S = A \setminus \mathfrak{p}$, $B_{\mathfrak{p}} = S^{-1}B$, $A_{\mathfrak{p}} = S^{-1}A$. Then $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral, and $B_{\mathfrak{p}} \neq 0$.

> [!note]- Derivation
> $S = A \setminus \mathfrak{p}$ is multiplicative because $\mathfrak{p}$ is prime ($1 \in S$, and $a, b \notin \mathfrak{p} \Rightarrow ab \notin \mathfrak{p}$). Integrality survives localization: for $b/s \in B_{\mathfrak{p}}$ with $b^n + a_1 b^{n-1} + \cdots + a_n = 0$ ($a_i \in A$), dividing by $s^n$ gives a monic relation for $b/s$ over $A_{\mathfrak{p}}$, so $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral. Finally, since $\mathfrak{p}$ is a proper ideal, $0 \in \mathfrak{p}$, so $0 \notin S$; and [[Def - Multiplicative Set and Localization|$S^{-1}B = 0 \iff 0 \in S$]], so $B_{\mathfrak{p}} \neq 0$.

**Step 2: Take a maximal ideal $\mathfrak{m}$ of $B_{\mathfrak{p}}$; it contracts to $\mathfrak{p}A_{\mathfrak{p}}$ in $A_{\mathfrak{p}}$.**

Being non-zero, $B_{\mathfrak{p}}$ has a maximal ideal $\mathfrak{m}$. The integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ and the domain criterion force $\mathfrak{m} \cap A_{\mathfrak{p}}$ to be maximal, hence $= \mathfrak{p}A_{\mathfrak{p}}$.

> [!note]- Derivation
> Every non-zero ring has a maximal ideal (Zorn's lemma applied to proper ideals), so $\operatorname{mSpec} B_{\mathfrak{p}} \neq \varnothing$; fix $\mathfrak{m} \in \operatorname{mSpec} B_{\mathfrak{p}}$. By the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain/field criterion]] applied to the integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$, a prime of $B_{\mathfrak{p}}$ is maximal if and only if its contraction to $A_{\mathfrak{p}}$ is maximal. (Reason: $A_{\mathfrak{p}}/(\mathfrak{m} \cap A_{\mathfrak{p}}) \hookrightarrow B_{\mathfrak{p}}/\mathfrak{m}$ is an integral extension of domains, and there one is a field iff the other is; $B_{\mathfrak{p}}/\mathfrak{m}$ is a field as $\mathfrak{m}$ is maximal, so $A_{\mathfrak{p}}/(\mathfrak{m}\cap A_{\mathfrak{p}})$ is a field, i.e. $\mathfrak{m}\cap A_{\mathfrak{p}}$ is maximal.) But $A_{\mathfrak{p}}$ is a [[Def - Local Ring and Residue Field|local ring]] with unique maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$. Hence
> $$\mathfrak{m} \cap A_{\mathfrak{p}} = \mathfrak{p}A_{\mathfrak{p}}.$$

**Step 3: Contract $\mathfrak{m}$ to a prime $\mathfrak{q}$ of $B$ with $\mathfrak{q} \cap A = \mathfrak{p}$.**

Let $\mathfrak{q}$ be the contraction of $\mathfrak{m}$ along $B \to B_{\mathfrak{p}}$. Then $\mathfrak{q} \in \operatorname{Spec} B$ and $\mathfrak{q} \cap A = \mathfrak{p}$.

> [!note]- Derivation
> Let $\lambda : B \to B_{\mathfrak{p}}$ be the localization map and $\mathfrak{q} = \lambda^{-1}(\mathfrak{m})$. As the contraction of a prime, $\mathfrak{q} \in \operatorname{Spec} B$. To compute $\mathfrak{q} \cap A$, use the commuting square
> $$\begin{array}{ccc} A & \hookrightarrow & B \\ \downarrow & & \downarrow\lambda \\ A_{\mathfrak{p}} & \hookrightarrow & B_{\mathfrak{p}} \end{array}$$
> An element $a \in A$ lies in $\mathfrak{q} \cap A$ iff $\lambda(a) \in \mathfrak{m}$ iff (by commutativity, $\lambda(a)$ is the image of $a$ in $A_{\mathfrak{p}}$ under $A \to A_{\mathfrak{p}} \to B_{\mathfrak{p}}$) the image $a/1 \in A_{\mathfrak{p}}$ lies in $\mathfrak{m} \cap A_{\mathfrak{p}} = \mathfrak{p}A_{\mathfrak{p}}$. And $a/1 \in \mathfrak{p}A_{\mathfrak{p}} \iff a \in \mathfrak{p}$ (the contraction of $\mathfrak{p}A_{\mathfrak{p}}$ to $A$ is $\mathfrak{p}$, since $\mathfrak{p}$ is disjoint from $S$). Hence $\mathfrak{q} \cap A = \mathfrak{p}$. This is the required prime of $B$ over $\mathfrak{p}$.

> [!note]- Complete formal solution
> Let $A \subseteq B$ be integral and $\mathfrak{p} \in \operatorname{Spec} A$. Set $S = A \setminus \mathfrak{p}$ (multiplicative, as $\mathfrak{p}$ is prime), $B_{\mathfrak{p}} = S^{-1}B$, $A_{\mathfrak{p}} = S^{-1}A$.
>
> $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$ is integral (divide a monic relation by powers of $s$). Since $\mathfrak{p}$ is proper, $0 \notin S$, so $B_{\mathfrak{p}} \neq 0$ and has a maximal ideal $\mathfrak{m}$.
>
> By the [[Thm - Integral Extensions and Fields (Domain Criterion)|domain/field criterion]] for the integral extension $A_{\mathfrak{p}} \subseteq B_{\mathfrak{p}}$, the contraction $\mathfrak{m} \cap A_{\mathfrak{p}}$ is maximal in $A_{\mathfrak{p}}$; as $A_{\mathfrak{p}}$ is local with unique maximal ideal $\mathfrak{p}A_{\mathfrak{p}}$, $\mathfrak{m} \cap A_{\mathfrak{p}} = \mathfrak{p}A_{\mathfrak{p}}$.
>
> Let $\mathfrak{q} = \lambda^{-1}(\mathfrak{m})$ for the localization map $\lambda : B \to B_{\mathfrak{p}}$; it is prime. By the commuting square of localization maps, $a \in \mathfrak{q} \cap A \iff a/1 \in \mathfrak{m} \cap A_{\mathfrak{p}} = \mathfrak{p}A_{\mathfrak{p}} \iff a \in \mathfrak{p}$. Hence $\mathfrak{q} \cap A = \mathfrak{p}$.
>
> Since $\mathfrak{p}$ was arbitrary, $\iota^* : \operatorname{Spec} B \to \operatorname{Spec} A$ is surjective. $\blacksquare$

---

# Key Takeaways

**Surjectivity of a fibre map is existence of a prime, which is non-vanishing of a localization.** The reusable principle: to show "every point of the base is hit", show "for each $\mathfrak{p}$ the relevant ring is non-zero, so has a maximal ideal". Here the relevant ring is $B_{\mathfrak{p}} = (A\setminus\mathfrak{p})^{-1}B$, and its non-vanishing is automatic from $0 \notin A \setminus \mathfrak{p}$. This is the same engine that proves the nilradical is the intersection of the primes (localize at a non-nilpotent element to manufacture a prime missing it) and that the support of a non-zero module is non-empty. The trigger is any "*some* prime exists with property $X$" — recast $X$ as "this localization is non-zero" and invoke "a non-zero ring has a maximal ideal".

**Localize at the base prime, not at a prime upstairs — and take a maximal ideal, not any prime.** The decisive and counterintuitive choice is the ring $B_{\mathfrak{p}} = (A\setminus\mathfrak{p})^{-1}B$: you invert elements of the *small* ring $A$, not of $B$, because the prime of $B$ you seek does not yet exist to localize at. This ring is unusual — not local, not a localization of $B$ at a $B$-prime — and getting comfortable with it is half the battle. The second subtlety is that only the *maximal* ideals of $B_{\mathfrak{p}}$ contract to $\mathfrak{p}$ *exactly*; an arbitrary prime of $B_{\mathfrak{p}}$ contracts to some prime $\subseteq \mathfrak{p}$, which is the fibre over a *smaller* point. The domain criterion is precisely the tool that converts "maximal in $B_{\mathfrak{p}}$" into "contracts to $\mathfrak{p}$".

**This exercise *is* lying over — and lying over is the anchor of all chain-lifting.** What you have proved, [[Thm - Lying Over|lying over]], is the simplest of the four Cohen–Seidenberg theorems, but it is the base case the others stand on. [[Thm - Going Up|Going up]] is proved by reducing to lying over in a quotient; the dimension inequality $\dim A \leq \dim B$ starts by lying a prime over the bottom of a chain. So mastering this one-paragraph argument — localize, non-zero, maximal ideal, domain criterion, contract — unlocks the proof technique for the whole chapter. The companion [[Ex - A chain of primes lifts along a finite extension]] shows lying over in its role as the anchor of an iterated going-up lift.
