---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Primary Ideal"
  - "Def - Associated and Minimal Primes"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

This exercise assembles the colon-ideal toolkit behind the [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]] (parts (h), (i), (j) of ES3.9). For an ideal $I$ of $R$ and $x \in R$, write $(I : x) = \{r \in R : rx \in I\}$.

**Part (a) — the colon is an ideal (ES3.9h).** Show $(I : x)$ is an ideal of $R$ containing $I$, and that $(I : x) = R$ if $x \in I$.

**Part (b) — colon of a primary ideal (ES3.9i).** Let $\mathfrak{q}$ be [[Def - Primary Ideal|𝔭-primary]] and $x \in R \setminus \mathfrak{q}$. Show $(\mathfrak{q} : x)$ is again $\mathfrak{p}$-primary. (And if $x \in \mathfrak{q}$ then $(\mathfrak{q} : x) = R$ by (a).)

**Part (c) — the colon formula (ES3.9j).** Let $I = \mathfrak{q}_1 \cap \cdots \cap \mathfrak{q}_n$ be a minimal primary decomposition, $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$. Show
$$(I : x) = \bigcap_{i} (\mathfrak{q}_i : x), \qquad\text{hence}\qquad \sqrt{(I : x)} = \bigcap_{i \,:\, x \notin \mathfrak{q}_i} \mathfrak{p}_i,$$
and deduce $\{\mathfrak{p}_1, \dots, \mathfrak{p}_n\} = \{\sqrt{(I:x)} : x \in R\} \cap \operatorname{Spec} R$, so $\operatorname{Ass}(I)$ is independent of the decomposition.

**Recall:**

The objects in play are the colon ideal, primary ideals and their radicals, and minimal primary decompositions.

![[Def - Primary Ideal#The Definition]]

![[Def - Associated and Minimal Primes#Associated primes]]

The [[Def - Associated and Minimal Primes|associated primes]] $\operatorname{Ass}(I) = \{\sqrt{\mathfrak{q}_i}\}$ are the radicals of the components of a minimal primary decomposition. A decomposition is **minimal** when the $\sqrt{\mathfrak{q}_i}$ are distinct and no component contains the intersection of the others — which guarantees, for each $i$, an element in all components but the $i$-th.

---

# Convergent Strategy

**Problem class.** This is a *build-the-machine* problem: it proves the three lemmas that, assembled, give the colon-ideal computation of associated primes. As the [[Commutative Algebra IX — Primary Decomposition#Problem-Solving Strategy|topic page strategy]] records, "find the associated primes" routes through colon ideals, and this exercise is the justification of that route.

**Assumption pattern.** The hypothesis "$\mathfrak{q}$ is $\mathfrak{p}$-primary" is used through its operational form $xy \in \mathfrak{q}, y \notin \sqrt{\mathfrak{q}} \Rightarrow x \in \mathfrak{q}$, which is exactly what controls $(\mathfrak{q} : x)$. The hypothesis "minimal decomposition" supplies, for each $i$, a separating element $x$ in all components but the $i$-th — the trigger that lets you isolate a single prime in the formula.

**Theorem routing.** Part (a) is a direct ideal-axiom check. Part (b) is the heart: bound $\mathfrak{q} \subseteq (\mathfrak{q}:x) \subseteq \mathfrak{p}$ using primariness, then verify the primary condition for $(\mathfrak{q}:x)$ directly. Part (c) distributes the colon through the intersection (operation 3), evaluates each factor via (a) and (b) — $R$ if $x \in \mathfrak{q}_i$, radical $\mathfrak{p}_i$ if not — and then harvests every $\mathfrak{p}_i$ by choosing a separating $x$, and conversely uses prime-avoidance to show every prime colon-radical is some $\mathfrak{p}_i$.

**Key decision point.** The non-obvious move in (b) is the *two-sided squeeze* $\mathfrak{q} \subseteq (\mathfrak{q}:x) \subseteq \sqrt{\mathfrak{q}}$ when $x \notin \mathfrak{q}$: the lower bound is trivial, but the upper bound $(\mathfrak{q}:x) \subseteq \mathfrak{p}$ uses primariness in the form "$rx \in \mathfrak{q}, x \notin \mathfrak{q} \Rightarrow r \in \sqrt{\mathfrak{q}}$". In (c) the non-obvious move is recognising that *minimality* is exactly the hypothesis that makes the separating element exist — without it, you could not isolate a single $\mathfrak{p}_i$, and the formula would only give intersections.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra IX — Primary Decomposition#Legal Operations|the topic page's Legal Operations]]:

1. **Probe with a colon ideal (operation 3).** The entire exercise is the construction and analysis of $(I : x)$, the probe that detects associated primes.

2. **Take radicals to find the attached prime (operation 2).** Radicalise $(I:x) = \bigcap(\mathfrak{q}_i:x)$ to get $\bigcap_{x \notin \mathfrak{q}_i}\mathfrak{p}_i$.

3. **Use $\bigcap \mathfrak{a}_i \subseteq \mathfrak{p} \Rightarrow$ some $\mathfrak{a}_i \subseteq \mathfrak{p}$ (operation 8).** Show a prime colon-radical must be one of the $\mathfrak{p}_i$.

4. **Group / order primes to isolate one (minimality).** Choose $x$ in all components but the $i$-th to peel off $\mathfrak{p}_i$ alone.

---

# Hints

> [!note]- Hint 1 (part a)
> $(I : x) = \{r : rx \in I\}$. Check the ideal axioms directly: if $r_1 x, r_2 x \in I$ then $(r_1 - r_2)x \in I$; if $rx \in I$ and $s \in R$ then $(sr)x = s(rx) \in I$. For $I \subseteq (I:x)$: if $r \in I$ then $rx \in I$. For $x \in I \Rightarrow (I:x) = R$: then $rx \in I$ for all $r$.

> [!note]- Hint 2 (part b)
> When $x \notin \mathfrak{q}$, sandwich: $\mathfrak{q} \subseteq (\mathfrak{q}:x)$ always; and if $r \in (\mathfrak{q}:x)$ then $rx \in \mathfrak{q}$ with $x \notin \mathfrak{q}$, so primariness gives $r \in \sqrt{\mathfrak{q}} = \mathfrak{p}$. Hence $\mathfrak{q} \subseteq (\mathfrak{q}:x) \subseteq \mathfrak{p}$, so $\sqrt{(\mathfrak{q}:x)} = \mathfrak{p}$. Then verify $(\mathfrak{q}:x)$ is itself primary.

> [!note]- Hint 3 (part b, primary check)
> Suppose $ab \in (\mathfrak{q}:x)$ with $b \notin \sqrt{(\mathfrak{q}:x)} = \mathfrak{p}$. Then $abx \in \mathfrak{q}$ and $b \notin \sqrt{\mathfrak{q}}$, so by primariness of $\mathfrak{q}$, $ax \in \mathfrak{q}$, i.e. $a \in (\mathfrak{q}:x)$. That is the primary condition for $(\mathfrak{q}:x)$.

> [!note]- Hint 4 (part c)
> Distribute: $r \in (I:x) = (\bigcap \mathfrak{q}_i : x)$ iff $rx \in \mathfrak{q}_i$ for all $i$ iff $r \in (\mathfrak{q}_i:x)$ for all $i$. Radicalise using (a),(b): $(\mathfrak{q}_i:x) = R$ if $x \in \mathfrak{q}_i$ (contributes nothing) and has radical $\mathfrak{p}_i$ if $x \notin \mathfrak{q}_i$. To get $\mathfrak{p}_i$ alone, pick $x \in \bigcap_{j\neq i}\mathfrak{q}_j \setminus \mathfrak{q}_i$ (exists by minimality). For the converse, a prime $\sqrt{(I:x)} = \bigcap_{i\in S}\mathfrak{p}_i$ must equal one $\mathfrak{p}_i$.

---

# Solution

The three parts build up to the colon formula. Part (a) checks $(I:x)$ is an ideal containing $I$, equal to $R$ when $x \in I$. Part (b) shows the colon of a $\mathfrak{p}$-primary ideal by a non-zero-divisor-class $x$ is again $\mathfrak{p}$-primary, via the squeeze $\mathfrak{q} \subseteq (\mathfrak{q}:x) \subseteq \mathfrak{p}$ plus a direct primary check. Part (c) distributes the colon through a minimal decomposition, radicalises to $\bigcap_{x\notin\mathfrak{q}_i}\mathfrak{p}_i$, harvests each $\mathfrak{p}_i$ with a separating $x$ (minimality), and uses prime-avoidance for the converse — yielding the intrinsic formula for $\operatorname{Ass}(I)$. The non-obvious step is the squeeze in (b), where primariness supplies the upper bound.

**Step 1 (a): $(I : x)$ is an ideal containing $I$, and $= R$ if $x \in I$.**

> [!note]- Derivation
> *Ideal.* If $r_1, r_2 \in (I:x)$ then $r_1 x, r_2 x \in I$, so $(r_1 - r_2)x = r_1 x - r_2 x \in I$, giving $r_1 - r_2 \in (I:x)$. If $r \in (I:x)$ and $s \in R$ then $(sr)x = s(rx) \in I$ (as $I$ absorbs multiplication), so $sr \in (I:x)$. And $0 \in (I:x)$. So $(I:x)$ is an [[Def - Ideal|ideal]].
>
> *Contains $I$.* If $r \in I$ then $rx \in I$ (ideal absorbs $x$), so $r \in (I:x)$. Thus $I \subseteq (I:x)$.
>
> *Equals $R$ when $x \in I$.* If $x \in I$ then for every $r \in R$, $rx \in I$, so $r \in (I:x)$; hence $(I:x) = R$.

**Step 2 (b): $(\mathfrak{q} : x)$ is $\mathfrak{p}$-primary when $\mathfrak{q}$ is $\mathfrak{p}$-primary and $x \notin \mathfrak{q}$.**

The squeeze $\mathfrak{q} \subseteq (\mathfrak{q}:x) \subseteq \mathfrak{p}$ gives radical $\mathfrak{p}$; a direct check gives primariness.

> [!note]- Derivation
> *Radical is $\mathfrak{p}$.* By (a), $\mathfrak{q} \subseteq (\mathfrak{q}:x)$, so $\mathfrak{p} = \sqrt{\mathfrak{q}} \subseteq \sqrt{(\mathfrak{q}:x)}$. Conversely, let $r \in (\mathfrak{q}:x)$, so $rx \in \mathfrak{q}$; since $x \notin \mathfrak{q}$ and $\mathfrak{q}$ is [[Def - Primary Ideal|primary]], primariness ($rx \in \mathfrak{q}, x \notin \mathfrak{q} \Rightarrow r \in \sqrt{\mathfrak{q}}$) gives $r \in \sqrt{\mathfrak{q}} = \mathfrak{p}$. Hence $(\mathfrak{q}:x) \subseteq \mathfrak{p}$, so $\sqrt{(\mathfrak{q}:x)} \subseteq \mathfrak{p}$, and therefore $\sqrt{(\mathfrak{q}:x)} = \mathfrak{p}$. (Also $(\mathfrak{q}:x) \neq R$ since $x \notin \mathfrak{q}$ means $1 \cdot x \notin \mathfrak{q}$, so $1 \notin (\mathfrak{q}:x)$.)
>
> *Primary.* Suppose $ab \in (\mathfrak{q}:x)$ with $b \notin \sqrt{(\mathfrak{q}:x)} = \mathfrak{p}$. Then $abx = a(bx) \in \mathfrak{q}$, and $b \notin \mathfrak{p} = \sqrt{\mathfrak{q}}$; primariness of $\mathfrak{q}$ (applied to the product $(ax)\cdot b$: $(ax)b \in \mathfrak{q}$, $b \notin \sqrt{\mathfrak{q}}$) gives $ax \in \mathfrak{q}$, i.e. $a \in (\mathfrak{q}:x)$. So $(\mathfrak{q}:x)$ is primary, with radical $\mathfrak{p}$: it is $\mathfrak{p}$-primary.

**Step 3 (c): the colon formula and the intrinsic description of $\operatorname{Ass}(I)$.**

$(I:x) = \bigcap_i(\mathfrak{q}_i:x)$, so $\sqrt{(I:x)} = \bigcap_{x \notin \mathfrak{q}_i}\mathfrak{p}_i$; harvesting and prime-avoidance give $\operatorname{Ass}(I) = \{\sqrt{(I:x)}\} \cap \operatorname{Spec} R$.

> [!note]- Derivation
> *Distribution.* $r \in (I:x) = \left(\bigcap_i \mathfrak{q}_i : x\right)$ iff $rx \in \bigcap_i \mathfrak{q}_i$ iff $rx \in \mathfrak{q}_i$ for all $i$ iff $r \in \bigcap_i(\mathfrak{q}_i:x)$. So $(I:x) = \bigcap_i (\mathfrak{q}_i:x)$.
>
> *Radical.* Radical commutes with finite intersection. By (a), if $x \in \mathfrak{q}_i$ then $(\mathfrak{q}_i:x) = R$ (radical $R$, contributes nothing to the intersection); by (b), if $x \notin \mathfrak{q}_i$ then $\sqrt{(\mathfrak{q}_i:x)} = \mathfrak{p}_i$. Hence
> $$\sqrt{(I:x)} = \bigcap_i \sqrt{(\mathfrak{q}_i:x)} = \bigcap_{i \,:\, x \notin \mathfrak{q}_i}\mathfrak{p}_i.$$
>
> *Every $\mathfrak{p}_i$ is achieved.* By minimality, $\bigcap_{j\neq i}\mathfrak{q}_j \not\subseteq \mathfrak{q}_i$, so choose $x \in \bigcap_{j\neq i}\mathfrak{q}_j \setminus \mathfrak{q}_i$. Then $x \in \mathfrak{q}_j$ for $j \neq i$ and $x \notin \mathfrak{q}_i$, so only $i$ survives: $\sqrt{(I:x)} = \mathfrak{p}_i$, a prime. So each $\mathfrak{p}_i \in \{\sqrt{(I:x)}\} \cap \operatorname{Spec} R$.
>
> *Converse via prime-avoidance.* Suppose $\sqrt{(I:x)} = \bigcap_{i\in S}\mathfrak{p}_i$ is prime, $S = \{i : x \notin \mathfrak{q}_i\}$. Then $\bigcap_{i\in S}\mathfrak{p}_i$ is a prime $\mathfrak{P}$, and $\mathfrak{P} \supseteq \prod_{i\in S}\mathfrak{p}_i$, so by primeness $\mathfrak{P} \supseteq \mathfrak{p}_{i_0}$ for some $i_0 \in S$; but also $\mathfrak{P} = \bigcap_{i\in S}\mathfrak{p}_i \subseteq \mathfrak{p}_{i_0}$, so $\mathfrak{P} = \mathfrak{p}_{i_0}$, one of the $\mathfrak{p}_i$.
>
> *Conclusion.* The two inclusions give $\{\mathfrak{p}_1, \dots, \mathfrak{p}_n\} = \{\sqrt{(I:x)} : x \in R\} \cap \operatorname{Spec} R$. The right side is built from $I$ alone, so the set of radicals is independent of the minimal decomposition; $\operatorname{Ass}(I)$ is well-defined.

> [!note]- Complete formal solution
> **(a)** $(I:x)$ is closed under subtraction and under multiplication by $R$ (since $(sr)x = s(rx) \in I$), so it is an ideal; $I \subseteq (I:x)$ as $r \in I \Rightarrow rx \in I$; and $x \in I \Rightarrow rx \in I$ for all $r \Rightarrow (I:x) = R$.
>
> **(b)** For $x \notin \mathfrak{q}$: $\mathfrak{q} \subseteq (\mathfrak{q}:x)$, and $r \in (\mathfrak{q}:x) \Rightarrow rx \in \mathfrak{q}, x \notin \mathfrak{q} \Rightarrow r \in \sqrt{\mathfrak{q}} = \mathfrak{p}$, so $(\mathfrak{q}:x) \subseteq \mathfrak{p}$ and $\sqrt{(\mathfrak{q}:x)} = \mathfrak{p}$. Primary: $ab \in (\mathfrak{q}:x), b \notin \mathfrak{p} \Rightarrow (ax)b \in \mathfrak{q}, b \notin \sqrt{\mathfrak{q}} \Rightarrow ax \in \mathfrak{q} \Rightarrow a \in (\mathfrak{q}:x)$. So $(\mathfrak{q}:x)$ is $\mathfrak{p}$-primary.
>
> **(c)** $(I:x) = \bigcap_i(\mathfrak{q}_i:x)$ by unwinding membership, so $\sqrt{(I:x)} = \bigcap_{x\notin\mathfrak{q}_i}\mathfrak{p}_i$. Choosing $x \in \bigcap_{j\neq i}\mathfrak{q}_j\setminus\mathfrak{q}_i$ (minimality) gives $\sqrt{(I:x)} = \mathfrak{p}_i$; and any prime $\sqrt{(I:x)} = \bigcap_{i\in S}\mathfrak{p}_i$ equals some $\mathfrak{p}_i$ by prime-avoidance. Hence $\operatorname{Ass}(I) = \{\sqrt{(I:x)}:x\in R\}\cap\operatorname{Spec} R$, independent of the decomposition. $\blacksquare$

---

# Key Takeaways

**The colon ideal is the universal probe for "which primes are attached", and it distributes through any intersection.** The single fact $(I : x) = \bigcap_i (\mathfrak{q}_i : x)$ is what makes associated primes computable: it converts a question about the (non-canonical) decomposition into a finite intersection of colon ideals whose radicals are either $R$ or a single $\mathfrak{p}_i$. The trigger to reach for the colon is any appearance of $\operatorname{Ass}(I)$, any "is this prime associated", and — in module language — any annihilator computation, since $(I : x) = \operatorname{Ann}_R(\bar x)$ for $\bar x \in R/I$. The transferable diagnostic: to isolate a single associated prime, choose the probe element $x$ to lie in *every* primary component except the one you want, and the colon collapses to that component's prime. This "kill all but one" technique is the computational heart of every associated-prime calculation, by hand or by machine.

**Primariness is exactly the closure property that makes $(\mathfrak{q} : x)$ stay $\mathfrak{p}$-primary.** The squeeze $\mathfrak{q} \subseteq (\mathfrak{q} : x) \subseteq \mathfrak{p}$ in part (b) is where the definition of primary pays off: the upper bound $(\mathfrak{q}:x) \subseteq \mathfrak{p}$ is *precisely* the primary condition "$rx \in \mathfrak{q}, x \notin \mathfrak{q} \Rightarrow r \in \sqrt{\mathfrak{q}}$" read as a containment. This is the deeper reason primary ideals are the right pieces: they are stable under colon by elements outside them, so the operation that probes for primes never leaves the class. The transferable lesson: when a closure operation must preserve a class of ideals, the defining axiom of the class is usually exactly the bound that closure needs — here, primariness is engineered (in hindsight) to make the colon-probe well-behaved.

**Minimality is the hypothesis that makes a single prime extractable.** Without minimality, the colon formula $\sqrt{(I:x)} = \bigcap_{x \notin \mathfrak{q}_i}\mathfrak{p}_i$ would still hold, but you could not guarantee a choice of $x$ that isolates a single $\mathfrak{p}_i$ — a redundant component would always drag along extra primes. The condition "no component contains the intersection of the others" is *defined* to provide, for each $i$, an element of $\bigcap_{j\neq i}\mathfrak{q}_j$ outside $\mathfrak{q}_i$. The takeaway for spaced practice: whenever a uniqueness or extraction argument uses a "minimal" decomposition, the minimality is almost always there to supply a separating element — recognising this tells you immediately how to use the hypothesis. This same colon machinery, assembled here, is what proves the [[Thm - Uniqueness of the Associated Primes (First Uniqueness Theorem)|First Uniqueness Theorem]]; see [[Ex - Embedded primes are not unique]] for what the colon formula does *not* pin down — the embedded components.
