---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Filtration and Stable Filtration"
  - "Def - The Associated Graded Ring and the Rees Algebra"
  - "Def - Noetherian Ring"
  - "Def - Finitely Generated Module"
  - "Thm - The Artin-Rees Lemma"
  - "Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $R$ be a [[Def - Noetherian Ring|Noetherian ring]], $\mathfrak{a} \trianglelefteq R$ an [[Def - Ideal|ideal]], $M$ a [[Def - Finitely Generated Module|finitely generated]] $R$-module, and $(M_n)_{n \geq 0}$ an [[Def - Filtration and Stable Filtration|𝔞-filtration]] of $M$. Let $R^* = \bigoplus_n \mathfrak{a}^n$ be the [[Def - The Associated Graded Ring and the Rees Algebra|Rees algebra]] and $M^* = \bigoplus_n M_n$ the Rees module.

**(a)** Prove the **stability criterion**: $(M_n)$ is a stable $\mathfrak{a}$-filtration $\iff$ $M^*$ is a finitely generated $R^*$-module.

**(b)** Using (a), give the structural proof of the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]]: for a submodule $N \subseteq M$ and a *stable* $\mathfrak{a}$-filtration $(M_n)$, the induced filtration $(N \cap M_n)$ is stable.

**(c)** Deduce that any two stable $\mathfrak{a}$-filtrations of $M$ have **bounded difference**: there is $n_0$ with $M_{n + n_0} \subseteq M_n'$ and $M_{n + n_0}' \subseteq M_n$ for all $n$ (they are equivalent), and conclude that all stable $\mathfrak{a}$-filtrations of a finitely generated module induce the same $\mathfrak{a}$-adic topology.

**Recall:**

![[Def - Filtration and Stable Filtration#The Definition]]

![[Def - The Associated Graded Ring and the Rees Algebra#The Definition]]

The Rees module $M^* = \bigoplus_n M_n$ is a graded $R^*$-module via $\mathfrak{a}^i \cdot M_n \subseteq M_{i+n}$ (using that $(M_n)$ is an $\mathfrak{a}$-filtration). The whole exercise is the statement that the *analytic* property "stable" of a filtration is *exactly* the *algebraic* property "finitely generated" of its Rees module — and that this dictionary, run over the Noetherian Rees algebra, proves Artin–Rees and the equivalence of stable filtrations in one stroke.

---

# Convergent Strategy

**Problem class.** This is a *prove-an-equivalence-then-harvest-corollaries* problem, and the equivalence is a **dictionary between two categories** — filtrations of $M$ over $R$, and graded modules over the Rees algebra $R^*$. The topic-page strategy flags this as the deepest move of the chapter: translate a filtration question into a module-finiteness question, where the Noetherian property of $R^*$ does the work.

**Assumption pattern.** The decisive structural device is the *ascending chain of $R^*$-submodules* $M_n^* = M_0 \oplus \dots \oplus M_n \oplus \bigoplus_{i \geq 1}\mathfrak{a}^i M_n$, which "freezes" the filtration at level $n$ and continues $\mathfrak{a}$-adically above. The recognisable trigger: the filtration is stable iff this ascending chain *stabilizes*, and the chain stabilizes iff $M^*$ is Noetherian — which holds iff $M^*$ is finitely generated, because $R^*$ is Noetherian. So "stable" $\leftrightarrow$ "chain stabilizes" $\leftrightarrow$ "$M^*$ finitely generated" is a chain of equivalences, each a standard Noetherian fact.

**Theorem routing.** For (a): build $M_n^*$, show "$(M_n)$ stable $\iff (M_n^*)$ stabilizes" by direct comparison, and "$(M_n^*)$ stabilizes $\iff M^* = \bigcup M_n^*$ is finitely generated over the Noetherian $R^*$" by the Noetherian-module dictionary; the Noetherian-ness of $R^*$ comes from [[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One|the graded criterion]] / [[Ex - The Rees algebra is Noetherian|the Rees-algebra exercise]]. For (b): $M^*$ is finitely generated (forward direction of (a)) hence Noetherian; the induced filtration's Rees module $N^* = \bigoplus(N \cap M_n)$ is a submodule of $M^*$, hence finitely generated, hence (backward direction of (a)) the induced filtration is stable. For (c): two stable filtrations are each equivalent to the $\mathfrak{a}$-adic one (via the comparison lemma), hence to each other; equivalence is the same as same-topology.

**Key decision point.** The crux — and the reason this is ⭐⭐⭐ — is *inventing the right ascending chain $M_n^*$*. The naive choice "$M_0 \oplus \dots \oplus M_n$ truncated" is not an $R^*$-submodule (it is not closed under multiplication by $\mathfrak{a}$, which raises degree). The correct object freezes at $M_n$ and then *continues $\mathfrak{a}$-adically*: $\bigoplus_{i \geq 0}\mathfrak{a}^i M_n$ above degree $n$. This is the unique modification making it an $R^*$-submodule, and the comparison "$M_n^* = M_{n+1}^* \iff \mathfrak{a}M_n = M_{n+1}$" then reads stability directly off chain-stabilization. Recognising that the *whole* theory (Artin–Rees, equivalence of stable filtrations) is a corollary of this one dictionary — rather than three separate theorems — is the conceptual payoff.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma#Legal Operations|the topic page's Legal Operations]]:

1. **Translate a filtration into its Rees module (operation 9).** Pass from $(M_n)$ to $M^* = \bigoplus M_n$ over $R^*$.

2. **Build the freezing chain $M_n^*$ to detect stability (new, operation 9 refined).** Construct the ascending chain whose stabilization is equivalent to filtration stability.

3. **Use that the Rees algebra is Noetherian (operation 3 / [[Ex - The Rees algebra is Noetherian]]).** Convert "$M^*$ finitely generated" into "$M^*$ Noetherian", licensing submodule finiteness.

4. **Read stability off submodule finiteness (operation 4).** For (b), the submodule $N^* \subseteq M^*$ is finitely generated, so its filtration is stable.

5. **Replace equivalence by same-topology (operation 9, topology form).** For (c), equivalent filtrations induce the same topology.

---

# Hints

> [!note]- Hint 1
> The slogan is "stable $\iff$ finitely generated Rees module". One direction (stable $\Rightarrow$ finitely generated) is easy: if $\mathfrak{a}M_n = M_{n+1}$ for $n \geq n_0$, then $M^*$ is generated by $M_0 \oplus \dots \oplus M_{n_0}$ over $R^*$. The hard direction needs a chain of $R^*$-submodules of $M^*$ that stabilizes exactly when the filtration is stable. What chain?

> [!note]- Hint 2
> The truncation $M_0 \oplus \dots \oplus M_n$ is *not* an $R^*$-submodule — multiplying by $\mathfrak{a}$ raises degree and escapes it. Fix this: freeze at $M_n$ and continue $\mathfrak{a}$-adically. Define $M_n^* = M_0 \oplus \dots \oplus M_n \oplus \mathfrak{a}M_n \oplus \mathfrak{a}^2 M_n \oplus \cdots$. Check this *is* an $R^*$-submodule, and that $\bigcup_n M_n^* = M^*$.

> [!note]- Hint 3
> Compare $M_n^*$ and $M_{n+1}^*$ in degree $n+1$: $M_n^*$ has $\mathfrak{a}M_n$ there, $M_{n+1}^*$ has $M_{n+1}$. So $M_n^* = M_{n+1}^* \iff \mathfrak{a}M_n = M_{n+1}$. Hence the chain $(M_n^*)$ stabilizes iff the filtration is stable. Now use that $R^*$ is Noetherian ([[Ex - The Rees algebra is Noetherian]]): an ascending chain in $M^*$ stabilizes iff... and $M^*$ is finitely generated iff it is Noetherian iff every ascending chain stabilizes.

> [!note]- Hint 4
> For (b): the *stable* filtration $(M_n)$ has $M^*$ finitely generated by (a), hence Noetherian (over Noetherian $R^*$). The induced filtration $(N \cap M_n)$ has Rees module $N^* = \bigoplus(N \cap M_n)$, a *submodule* of $M^*$ — hence finitely generated. Apply (a) backward to $N$. For (c): each stable filtration is equivalent to $(\mathfrak{a}^n M)$; equivalence is transitive; equivalent filtrations have cofinal neighbourhood bases.

---

# Solution

The solution proves one dictionary and harvests two theorems from it. Step 1 builds the freezing chain $M_n^*$ and proves the stability criterion (a) by matching chain-stabilization with filtration-stability and with finite generation. Step 2 deduces Artin–Rees (b) by placing the induced filtration's Rees module inside the Noetherian $M^*$. Step 3 deduces equivalence of stable filtrations (c) and hence same-topology. The hard part is the freezing chain.

**Step 1 (part a): The stability criterion via the freezing chain.**

Define $M_n^* = \big(\bigoplus_{i \leq n} M_i\big) \oplus \big(\bigoplus_{i \geq 1}\mathfrak{a}^i M_n\big) \subseteq M^*$; the ascending chain $(M_n^*)$ stabilizes iff $(M_n)$ is stable, and (over the Noetherian $R^*$) iff $M^*$ is finitely generated.

> [!note]- Derivation
> *The freezing chain is an $R^*$-submodule.* For $n \geq 0$, set
> $$M_n^* = M_0 \oplus M_1 \oplus \cdots \oplus M_n \oplus \mathfrak{a}M_n \oplus \mathfrak{a}^2 M_n \oplus \cdots,$$
> i.e. $(M_n^*)_i = M_i$ for $i \leq n$ and $(M_n^*)_i = \mathfrak{a}^{i - n}M_n$ for $i > n$. This is closed under the $R^*$-action: a degree-$j$ element $\mathfrak{a}^j$ times the degree-$i$ part lands in degree $i + j$, and one checks $\mathfrak{a}^j \cdot M_i \subseteq M_{i+j}$ (for $i + j \leq n$, using the $\mathfrak{a}$-filtration property iterated) $\subseteq (M_n^*)_{i+j}$, while $\mathfrak{a}^j \cdot \mathfrak{a}^{i-n}M_n = \mathfrak{a}^{i+j-n}M_n = (M_n^*)_{i+j}$ for $i > n$. So $M_n^*$ is a graded $R^*$-submodule of $M^*$.
>
> *The chain is ascending with union $M^*$.* $M_n^* \subseteq M_{n+1}^*$: they agree in degrees $\leq n$; in degree $n+1$, $M_n^*$ has $\mathfrak{a}M_n \subseteq M_{n+1} = (M_{n+1}^*)_{n+1}$ (as $(M_i)$ is an $\mathfrak{a}$-filtration); in degree $i > n+1$, $\mathfrak{a}^{i-n}M_n = \mathfrak{a}^{i - n - 1}(\mathfrak{a}M_n) \subseteq \mathfrak{a}^{i-n-1}M_{n+1}$. And $\bigcup_n M_n^* = M^*$ because each $M_m = (M_m^*)_m$ appears.
>
> *Stabilization $\iff$ stability.* Compare $M_n^*$ and $M_{n+1}^*$ in degree $n+1$: the former contributes $\mathfrak{a}M_n$, the latter $M_{n+1}$, and they agree in all other degrees that matter. Working through the comparison, $M_n^* = M_{n+1}^*$ exactly when $\mathfrak{a}M_n = M_{n+1}$. Hence the chain $M_0^* \subseteq M_1^* \subseteq \cdots$ stabilizes from index $n_0$ on $\iff \mathfrak{a}M_n = M_{n+1}$ for all $n \geq n_0$ $\iff (M_n)$ is a stable $\mathfrak{a}$-filtration.
>
> *Stabilization $\iff$ finite generation.* The Rees algebra $R^*$ is Noetherian ([[Ex - The Rees algebra is Noetherian]] / [[Thm - A Graded Ring is Noetherian iff Finitely Generated in Degree One|graded criterion]]). For a module over a Noetherian ring, "finitely generated" $\iff$ "Noetherian" $\iff$ "every ascending chain of submodules stabilizes". Apply this to $M^*$:
> - If $M^*$ is finitely generated, it is Noetherian, so the chain $(M_n^*)$ stabilizes.
> - If the chain $(M_n^*)$ stabilizes at $n_0$, then $M^* = \bigcup_n M_n^* = M_{n_0}^*$, which is generated over $R^*$ by $M_0 \oplus \dots \oplus M_{n_0}$ (a finitely generated $R$-module, since $M$ is Noetherian, so finitely many elements generate it over $R^*$). So $M^*$ is finitely generated.
>
> Combining: $(M_n)$ stable $\iff$ chain stabilizes $\iff M^*$ finitely generated over $R^*$. This proves (a).

**Step 2 (part b): Artin–Rees from the criterion.**

Apply (a) forward to the stable $(M_n)$ to get $M^*$ finitely generated, hence Noetherian; the induced filtration's Rees module $N^*$ is a submodule, hence finitely generated; apply (a) backward to get $(N \cap M_n)$ stable.

> [!note]- Derivation
> Let $(M_n)$ be a stable $\mathfrak{a}$-filtration and $N \subseteq M$. By (a), $M^*$ is a finitely generated $R^*$-module; since $R^*$ is Noetherian, $M^*$ is a Noetherian $R^*$-module.
>
> The induced filtration $(N \cap M_n)$ is an $\mathfrak{a}$-filtration of $N$ (because $\mathfrak{a}(N \cap M_n) \subseteq N \cap \mathfrak{a}M_n \subseteq N \cap M_{n+1}$), and its Rees module is
> $$N^* = \bigoplus_n (N \cap M_n) \subseteq \bigoplus_n M_n = M^*,$$
> a graded $R^*$-submodule of $M^*$. Since $M^*$ is Noetherian, $N^*$ is finitely generated over $R^*$.
>
> $N$ is finitely generated over Noetherian $R$, so (a) applies to $N$ and its filtration $(N \cap M_n)$: $N^*$ finitely generated $\Rightarrow (N \cap M_n)$ is a stable $\mathfrak{a}$-filtration of $N$. This is exactly the [[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]].

**Step 3 (part c): Equivalence of stable filtrations and same topology.**

Each stable filtration is equivalent to the $\mathfrak{a}$-adic one (a two-sided sandwich), hence stable filtrations are mutually equivalent, hence induce the same topology.

> [!note]- Derivation
> Let $(M_n)$ be any stable $\mathfrak{a}$-filtration of $M$. Two inclusions:
> - *Free direction.* Iterating $\mathfrak{a}M_k \subseteq M_{k+1}$ from $M_0 = M$ gives $\mathfrak{a}^n M \subseteq M_n$ for all $n$.
> - *Stability direction.* With $\mathfrak{a}M_k = M_{k+1}$ for $k \geq n_0$, $M_{n + n_0} = \mathfrak{a}^n M_{n_0} \subseteq \mathfrak{a}^n M$.
>
> So $\mathfrak{a}^n M \subseteq M_n$ and $M_{n+n_0} \subseteq \mathfrak{a}^n M$: the filtration $(M_n)$ is equivalent to the $\mathfrak{a}$-adic filtration $(\mathfrak{a}^n M)$. Now if $(M_n)$ and $(M_n')$ are two stable filtrations, each is equivalent to $(\mathfrak{a}^n M)$, and equivalence is transitive, so $(M_n) \sim (M_n')$ — there is $n_0$ with $M_{n+n_0} \subseteq M_n'$ and $M_{n+n_0}' \subseteq M_n$ for all $n$. This is the claimed bounded difference.
>
> *Same topology.* A filtration topology has the filtration submodules as a neighbourhood basis of $0$. The equivalence $M_{n+n_0} \subseteq M_n'$ and $M_{n+n_0}' \subseteq M_n$ says each basic neighbourhood of one filtration contains a basic neighbourhood of the other — the two bases are cofinal — so they generate the same topology. Hence all stable $\mathfrak{a}$-filtrations of $M$ induce the same topology, the $\mathfrak{a}$-adic topology (cf. [[Thm - Stable Filtrations Induce the Same Topology]]).

> [!note]- Complete formal solution
> **(a)** Define $M_n^* = M_0 \oplus \dots \oplus M_n \oplus \bigoplus_{i \geq 1}\mathfrak{a}^i M_n \subseteq M^*$, an ascending chain of graded $R^*$-submodules with union $M^*$, satisfying $M_n^* = M_{n+1}^* \iff \mathfrak{a}M_n = M_{n+1}$. Hence the chain stabilizes iff $(M_n)$ is stable. Since $R^*$ is Noetherian, $M^*$ is finitely generated iff Noetherian iff every ascending chain stabilizes; in particular $M^*$ finitely generated $\iff$ $(M_n^*)$ stabilizes $\iff$ $(M_n)$ stable. (For the backward implication, chain-stabilization at $n_0$ gives $M^* = M_{n_0}^*$, generated by the finitely generated $R$-module $M_0 \oplus \dots \oplus M_{n_0}$.)
>
> **(b)** For stable $(M_n)$, $M^*$ is finitely generated (a), hence Noetherian over the Noetherian $R^*$. The induced filtration $(N \cap M_n)$ has Rees module $N^* = \bigoplus(N \cap M_n) \subseteq M^*$, a submodule of a Noetherian module, hence finitely generated. By (a) applied to $N$, $(N \cap M_n)$ is stable — the Artin–Rees Lemma.
>
> **(c)** Any stable $(M_n)$ satisfies $\mathfrak{a}^n M \subseteq M_n$ (iterate the filtration property) and $M_{n+n_0} = \mathfrak{a}^n M_{n_0} \subseteq \mathfrak{a}^n M$ (stability), so $(M_n) \sim (\mathfrak{a}^n M)$. Two stable filtrations are thus mutually equivalent; equivalence means cofinal neighbourhood bases, so they induce the same topology. $\blacksquare$

---

# Key Takeaways

**The master move of the chapter: translate "stable filtration" into "finitely generated Rees module", and let the Noetherian Rees algebra prove everything at once.** This exercise is the conceptual keystone, because it shows that Artin–Rees and the equivalence of stable filtrations are not two theorems but *one dictionary* viewed twice. The dictionary is "$(M_n)$ stable $\iff M^* = \bigoplus M_n$ finitely generated over $R^*$", and once you have it, Artin–Rees is the single observation "a submodule of a finitely generated module over a Noetherian ring is finitely generated". The trigger to deploy this: any statement comparing filtrations, asserting stability, or controlling a submodule's filtration — set up the Rees modules over $R^*$ and the question becomes pure module-finiteness. The reason this is the deepest technique in the chapter is that it performs a *change of category*: from the category of filtered $R$-modules (where stability is an awkward eventual condition) to the category of graded $R^*$-modules (where stability is the clean condition "finitely generated"), and the second category is governed by the Noetherian property.

**Inventing the right ascending chain is the hard, creative step; the chain must be an honest $R^*$-submodule, which forces the "freeze-then-continue-adically" shape.** The single insight that makes (a) work is that the naive truncation $M_0 \oplus \dots \oplus M_n$ fails to be a Rees-algebra submodule — multiplication by $\mathfrak{a}$ raises degree and escapes the truncation. The repair, $M_n^* = (M_0 \oplus \dots \oplus M_n) \oplus \bigoplus_{i \geq 1}\mathfrak{a}^i M_n$, is the *unique* way to make the truncation $R^*$-stable: freeze the filtration at level $n$, then let $\mathfrak{a}$ drive it from there. This "freeze and continue adically" construction is a reusable device for converting an eventual filtration condition into a chain-stabilization condition — whenever you want to detect "eventually the filtration is $\mathfrak{a}$-driven", build the chain of modules that *assume* it is $\mathfrak{a}$-driven from level $n$ onward, and ask when consecutive members coincide. The transferable lesson for ⭐⭐⭐ problems: when you must detect an *eventual* property by a *chain-stabilization* (to invoke Noetherian-ness), the chain you need usually freezes the data at level $n$ and extrapolates by the expected rule above it.

**Equivalence of filtrations, not equality, is the right invariant — and it is exactly what the topology and the completion see.** Part (c) makes precise that the "right" notion of sameness for filtrations is *bounded difference* (equivalence), not equality, and that this is forced by what is invariant: the induced topology and the completion depend only on the filtration up to a finite shift. Two stable filtrations of $M$ are almost never equal — they differ by the shift $n_0$ — yet they are interchangeable for every topological and limit-theoretic purpose. The diagnostic: whenever a construction (topology, completion, graded pieces' eventual behaviour, Hilbert polynomial) is invariant under finite reindexing, the correct equivalence on the inputs is "equal up to bounded shift", and demanding strict equality both over-constrains and produces false statements. This is the same principle that makes "the $\mathfrak{a}$-adic topology" and "the completion $\hat{M}$" well-defined phrases independent of the chosen stable filtration — see [[Thm - Stable Filtrations Induce the Same Topology]] and the application in [[Ex - The Artin-Rees lemma and the subspace topology]].
