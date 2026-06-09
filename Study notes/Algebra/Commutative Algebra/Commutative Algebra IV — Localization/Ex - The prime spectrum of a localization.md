---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Prime and Maximal Ideal"
  - "Def - Multiplicative Set and Localization"
  - "Def - The Prime Spectrum (Spec)"
  - "Def - Extension and Contraction of Ideals"
  - "Thm - Prime Ideals of a Localization"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $S\subseteq R$ be a [[Def - Multiplicative Set and Localization|multiplicative subset]] and $\iota : R\to S^{-1}R$ the localization map. Prove:

1. The map $\mathfrak{p}\mapsto\mathfrak{p}^e = S^{-1}\mathfrak{p}$ is an inclusion-preserving bijection $\{\mathfrak{p}\in\operatorname{Spec} R : \mathfrak{p}\cap S = \varnothing\}\xrightarrow{\sim}\operatorname{Spec}(S^{-1}R)$, with inverse $\mathfrak{q}\mapsto\mathfrak{q}^c = \iota^{-1}(\mathfrak{q})$.
2. For $f\in R$ and $S = \{f^n\}$, the resulting $D(f) := \operatorname{Spec}(R_f)$ is homeomorphic to $\{\mathfrak{p} : f\notin\mathfrak{p}\}\subseteq\operatorname{Spec} R$, the basic open set; and $D(f)\cap D(g) = D(fg)$.
3. Concretely, list $\operatorname{Spec}(\mathbb{Z}_{(p)})$ and $\operatorname{Spec}(\mathbb{Z}[\tfrac1p]) = \operatorname{Spec}((\mathbb{Z})_p)$ — for the latter $S = \{p^n\}$ — and identify which primes of $\mathbb{Z}$ survive each.

**Recall:**

![[Thm - Prime Ideals of a Localization#Statement]]

![[Def - The Prime Spectrum (Spec)#Basic open sets]]

The [[Def - The Prime Spectrum (Spec)|Zariski topology]] on $\operatorname{Spec} R$ has closed sets $V(I) = \{\mathfrak{p} : I\subseteq\mathfrak{p}\}$, and the basic opens $D(f) = \{\mathfrak{p} : f\notin\mathfrak{p}\}$ form a basis. The [[Def - Extension and Contraction of Ideals|extension/contraction]] maps along $\iota$ are $\mathfrak{p}^e = S^{-1}\mathfrak{p}$ and $\mathfrak{q}^c = \iota^{-1}(\mathfrak{q})$.

---

# Convergent Strategy

**Problem class.** This is a *spectral computation* problem: determine the prime spectrum of a localization and its topology. Per the [[Commutative Algebra IV — Localization#Problem-Solving Strategy|topic strategy]], any question about primes of a localization is settled by the disjointness criterion $\mathfrak{p}\cap S = \varnothing$, and the geometric upgrade is that this criterion is a topological embedding onto a subspace.

**Assumption pattern.** The only data is the multiplicative set $S$. Recognising *which* $S$ is in play tells you the geometric picture: $S = R\setminus\mathfrak{p}$ gives a neighbourhood of a point, $S = \{f^n\}$ gives the open set $D(f)$. The surviving-prime criterion is the same in both cases; the difference is which primes the criterion selects.

**Theorem routing.** Part 1 is exactly the [[Thm - Prime Ideals of a Localization|prime-correspondence theorem]], so the work is to *cite and apply* it. Part 2 adds the topological layer: the bijection of part 1 is continuous in both directions for the Zariski topology, hence a homeomorphism, and the identity $D(f)\cap D(g) = D(fg)$ is a primality computation. Part 3 instantiates with $\mathbb{Z}$, where the primes are $(0)$ and $(q)$.

**Key decision point.** The genuinely new content beyond part 1 is *checking the bijection is a homeomorphism*, which requires identifying how closed sets correspond: $V(\mathfrak{a}^e)$ in $\operatorname{Spec}(S^{-1}R)$ pulls back to $V(\mathfrak{a})\cap\{$survivors$\}$ in $\operatorname{Spec} R$. The decision is to verify continuity via the *preimage-of-closed-is-closed* formulation $\operatorname{Spec}(\iota)^{-1}(V(\mathfrak{a})) = V(\mathfrak{a}^e)$, rather than chasing open sets, because extension and contraction interact cleanly with $V(-)$.

---

# Legal Operations Used

This solution deploys the following [[Commutative Algebra IV — Localization#Legal Operations|legal operations from the topic page]]:

1. **Operation 6 (read primes off the disjointness condition).** The core of part 1: surviving primes are exactly those disjoint from $S$.

2. **Operation 7 (detect nilpotence by collapse).** Used in part 2: $D(f) = \varnothing\iff f$ nilpotent, the degenerate case of the basic-open identification.

3. **Operation 3 / Operation 9 (localize through constructions).** Used to verify $D(f)\cap D(g) = D(fg)$ via $R_{fg} = (R_f)_g$, i.e. localizing twice equals localizing at the product.

---

# Hints

> [!note]- Hint 1
> Part 1 *is* the prime-correspondence theorem; do not reprove it, apply it. The content of this exercise is the topology in part 2 and the concrete lists in part 3. For part 2, ask: under the bijection, what does a closed set $V(\mathfrak{a}^e)$ of $\operatorname{Spec}(R_f)$ correspond to in $\operatorname{Spec} R$?

> [!note]- Hint 2
> A prime $\mathfrak{q}$ of $R_f$ contains $\mathfrak{a}^e$ iff its contraction $\mathfrak{q}^c$ contains $\mathfrak{a}$ (extension–contraction adjunction). So the bijection carries $V(\mathfrak{a}^e)$ to $V(\mathfrak{a})\cap D(f)$ — closed sets to closed sets (relatively), which is exactly continuity both ways, i.e. a homeomorphism onto $D(f)$.

> [!note]- Hint 3
> For $D(f)\cap D(g) = D(fg)$: $\mathfrak{p}$ avoids both $f$ and $g$ iff $\mathfrak{p}$ avoids $fg$ — use primality ($fg\in\mathfrak{p}\iff f\in\mathfrak{p}$ or $g\in\mathfrak{p}$). For part 3, recall $\operatorname{Spec}\mathbb{Z} = \{(0)\}\cup\{(q) : q\text{ prime}\}$, and apply the disjointness criterion with $S = \mathbb{Z}\setminus(p)$ and then with $S = \{p^n\}$.

---

# Solution

Part 1 is a direct citation of the prime-correspondence theorem. Part 2 upgrades the bijection to a homeomorphism by checking that closed sets correspond ($V(\mathfrak{a}^e)\leftrightarrow V(\mathfrak{a})\cap D(f)$) and computes $D(f)\cap D(g) = D(fg)$ from primality. Part 3 instantiates with $\mathbb{Z}$, where the two localizations select complementary sets of primes.

**Step 1: The bijection (part 1).**

By the prime-correspondence theorem, extension and contraction are mutually inverse, inclusion-preserving bijections between the survivor primes and $\operatorname{Spec}(S^{-1}R)$.

> [!note]- Derivation
> This is precisely [[Thm - Prime Ideals of a Localization|Becker Prop. 4.16(4)]]: for $\mathfrak{p}\cap S = \varnothing$, $\mathfrak{p}^e$ is a prime of $S^{-1}R$ with $\mathfrak{p}^{ec} = \mathfrak{p}$; for $\mathfrak{q}\in\operatorname{Spec}(S^{-1}R)$, $\mathfrak{q}^c$ is a prime disjoint from $S$ with $\mathfrak{q}^{ce} = \mathfrak{q}$ (every ideal of $S^{-1}R$ is extended). Both $e$ and $c$ preserve inclusions. Hence the stated bijection.

**Step 2: It is a homeomorphism onto $D(f)$ (part 2).**

Closed sets correspond: $V(\mathfrak{a}^e)\subseteq\operatorname{Spec}(R_f)$ maps bijectively to $V(\mathfrak{a})\cap D(f)\subseteq\operatorname{Spec} R$, so the bijection and its inverse are continuous.

> [!note]- Derivation
> Write $\Phi : \{\mathfrak{p} : f\notin\mathfrak{p}\}\to\operatorname{Spec}(R_f)$, $\mathfrak{p}\mapsto\mathfrak{p}^e$, the bijection of Step 1 (here $\mathfrak{p}\cap\{f^n\} = \varnothing\iff f\notin\mathfrak{p}$, by primality). For an ideal $\mathfrak{a}\trianglelefteq R$ and a survivor $\mathfrak{p}$:
> $$\mathfrak{p}^e\in V(\mathfrak{a}^e)\iff\mathfrak{a}^e\subseteq\mathfrak{p}^e\iff\mathfrak{a}\subseteq\mathfrak{p}^{ec} = \mathfrak{p}\iff\mathfrak{p}\in V(\mathfrak{a}),$$
> using the [[Def - Extension and Contraction of Ideals|extension–contraction adjunction]] $\mathfrak{a}^e\subseteq\mathfrak{b}\iff\mathfrak{a}\subseteq\mathfrak{b}^c$ and $\mathfrak{p}^{ec} = \mathfrak{p}$. So $\Phi^{-1}(V(\mathfrak{a}^e)) = V(\mathfrak{a})\cap D(f)$, a relatively closed set, and conversely every relatively closed set $V(\mathfrak{a})\cap D(f)$ is the $\Phi$-preimage of the closed set $V(\mathfrak{a}^e)$ (every ideal of $R_f$ is $\mathfrak{a}^e$ for some $\mathfrak{a}$). Hence $\Phi$ is a homeomorphism of $\operatorname{Spec}(R_f)$ onto the subspace $D(f)$ of $\operatorname{Spec} R$.

**Step 3: $D(f)\cap D(g) = D(fg)$ (part 2).**

A prime avoids both $f$ and $g$ iff it avoids $fg$, by primality.

> [!note]- Derivation
> $\mathfrak{p}\in D(f)\cap D(g)\iff f\notin\mathfrak{p}\text{ and }g\notin\mathfrak{p}$. By [[Def - Prime and Maximal Ideal|primality]], $fg\in\mathfrak{p}\iff f\in\mathfrak{p}$ or $g\in\mathfrak{p}$; the contrapositive is $fg\notin\mathfrak{p}\iff f\notin\mathfrak{p}$ and $g\notin\mathfrak{p}$. Hence $D(f)\cap D(g) = \{\mathfrak{p} : fg\notin\mathfrak{p}\} = D(fg)$. (Correspondingly $R_{fg}\cong(R_f)_g$, so localizing at $fg$ is restricting to the intersection.) In particular $D(f) = \varnothing\iff f\in\bigcap_{\mathfrak{p}}\mathfrak{p} = \operatorname{nil} R\iff f$ nilpotent.

**Step 4: The two $\mathbb{Z}$-examples (part 3).**

$\operatorname{Spec}(\mathbb{Z}_{(p)})$ keeps only the primes $\subseteq(p)$; $\operatorname{Spec}(\mathbb{Z}[\tfrac1p])$ keeps the primes not containing $p$.

> [!note]- Derivation
> $\operatorname{Spec}\mathbb{Z} = \{(0)\}\cup\{(q) : q\text{ prime}\}$, with $(0)\subseteq(q)$ for all $q$.
>
> *Localize at $(p)$:* $S = \mathbb{Z}\setminus(p)$, survivors are primes $\mathfrak{q}\subseteq(p)$, i.e. $(0)$ and $(p)$. So $\operatorname{Spec}(\mathbb{Z}_{(p)}) = \{(0),\ (p)\mathbb{Z}_{(p)}\}$, a two-point chain $(0)\subsetneq(p)\mathbb{Z}_{(p)}$ — confirming $\mathbb{Z}_{(p)}$ local of dimension $1$. Every prime $(q)$ with $q\neq p$ is killed (it meets $S$, as $q\notin(p)$).
>
> *Invert $p$:* $S = \{p^n\}$, survivors are primes not containing $p$, i.e. $(0)$ and $(q)$ for all primes $q\neq p$; only $(p)$ is killed. So $\operatorname{Spec}(\mathbb{Z}[\tfrac1p]) = \{(0)\}\cup\{(q)\mathbb{Z}[\tfrac1p] : q\neq p\} \cong D(p)$ — all of $\operatorname{Spec}\mathbb{Z}$ except the point $(p)$. The two localizations are *complementary*: $\mathbb{Z}_{(p)}$ keeps only $\{(0), (p)\}$, $\mathbb{Z}[\tfrac1p]$ keeps everything but $(p)$.

> [!note]- Complete formal solution
> **(1)** Immediate from [[Thm - Prime Ideals of a Localization|Prop. 4.16(4)]]: $e, c$ are mutually inverse inclusion-preserving bijections between $\{\mathfrak{p} : \mathfrak{p}\cap S = \varnothing\}$ and $\operatorname{Spec}(S^{-1}R)$.
>
> **(2)** For $S = \{f^n\}$, $\mathfrak{p}\cap S = \varnothing\iff f\notin\mathfrak{p}$, so the bijection $\Phi : D(f)\to\operatorname{Spec}(R_f)$ holds setwise. For ideals, $\mathfrak{p}^e\in V(\mathfrak{a}^e)\iff\mathfrak{a}\subseteq\mathfrak{p}\iff\mathfrak{p}\in V(\mathfrak{a})$ (adjunction + $\mathfrak{p}^{ec} = \mathfrak{p}$), so $\Phi$ matches closed sets, giving a homeomorphism onto the subspace $D(f)$. And $D(f)\cap D(g) = \{\mathfrak{p} : f\notin\mathfrak{p}, g\notin\mathfrak{p}\} = \{\mathfrak{p} : fg\notin\mathfrak{p}\} = D(fg)$ by primality.
>
> **(3)** $\operatorname{Spec}(\mathbb{Z}_{(p)}) = \{(0)\subsetneq(p)\mathbb{Z}_{(p)}\}$ (survivors $\subseteq(p)$). $\operatorname{Spec}(\mathbb{Z}[\tfrac1p]) = \{(0)\}\cup\{(q)\mathbb{Z}[\tfrac1p] : q\neq p\}$ (survivors avoiding $p$), homeomorphic to $D(p) = \operatorname{Spec}\mathbb{Z}\setminus\{(p)\}$. $\blacksquare$

---

# Key Takeaways

**The single disjointness criterion answers every spectral question about a localization.** Whether you want the maximal ideal of $R_{\mathfrak{p}}$, the dimension of $R_f$, or the full list of primes, the answer is computed entirely on the $R$-side by "which primes avoid $S$?". For $S = R\setminus\mathfrak{p}$ the survivors are the primes *inside* $\mathfrak{p}$ (a neighbourhood); for $S = \{f^n\}$ the survivors avoid $f$ (the open set $D(f)$). The transferable habit: when a localization's spectrum is asked for, immediately translate $S$ into a survival condition on primes of $R$ and read off the answer — you never compute inside $S^{-1}R$. This is the same move that gives $\dim R_{\mathfrak{p}} = \operatorname{ht}\mathfrak{p}$ and underlies all of dimension theory.

**A bijection of spectra becomes a homeomorphism precisely because extension and contraction respect $V(-)$.** The upgrade from "bijection of sets" to "homeomorphism" is the genuinely geometric content, and the mechanism is the adjunction $\mathfrak{a}^e\subseteq\mathfrak{b}\iff\mathfrak{a}\subseteq\mathfrak{b}^c$, which translates "containment of ideals" — the data defining closed sets — across the bijection. The trigger to recognise: whenever a map of spectra comes from a ring map, check continuity not by chasing opens but by the identity "preimage of $V(\mathfrak{a})$ is $V(\mathfrak{a}^e)$". This is exactly how one proves $\operatorname{Spec}$ is a functor to topological spaces, and the basic-open case here is its most important instance — it is what makes $D(f)$ an affine chart and lets the structure sheaf be glued.

**$R_{\mathfrak{p}}$ and $R_f$ select complementary pieces of $\operatorname{Spec} R$ — the point's neighbourhood versus an open set.** The $\mathbb{Z}$ computation makes vivid that localizing at a prime and inverting an element pull in opposite directions: $\mathbb{Z}_{(p)}$ retains only $\{(0), (p)\}$ (zooming *in* to the point $(p)$), while $\mathbb{Z}[\tfrac1p]$ retains everything *except* $(p)$ (deleting the point, restricting to its open complement). Both are "restriction to an open piece", but $D(p) = \operatorname{Spec}\mathbb{Z}\setminus\{(p)\}$ is a large open set whereas $\operatorname{Spec}(\mathbb{Z}_{(p)})$ is an infinitesimal neighbourhood. Holding this contrast prevents the common confusion between "localize at $\mathfrak{p}$" and "invert an element of $\mathfrak{p}$", and it is the concrete shadow of the open-cover $\{D(f)\}$ that builds a scheme — see [[Ex - The prime spectrum of a localization]]'s companion [[Ex - Localizing at a prime gives a local ring]] for the local-ring side.
