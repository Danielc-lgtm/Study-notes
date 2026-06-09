---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Going Up"
  - "Thm - Lying Over"
  - "Thm - Incomparability"
  - "Def - Krull Dimension and Height"
  - "Def - The Induced Map on Spectra"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $A \subseteq B$ be an integral extension of rings. Let
$$\mathfrak{p}_0 \subsetneq \mathfrak{p}_1 \subsetneq \cdots \subsetneq \mathfrak{p}_n$$
be a strict chain of prime ideals of $A$, and let $\mathfrak{q}_0 \in \operatorname{Spec} B$ be a prime lying over $\mathfrak{p}_0$ (that is, $\mathfrak{q}_0 \cap A = \mathfrak{p}_0$). Prove that there is a strict chain
$$\mathfrak{q}_0 \subsetneq \mathfrak{q}_1 \subsetneq \cdots \subsetneq \mathfrak{q}_n$$
of prime ideals of $B$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ for every $i$.

Deduce that $\dim B \geq \dim A$ for any integral extension. (If $\mathfrak{q}_0$ is not given, [[Thm - Lying Over|lying over]] supplies one over $\mathfrak{p}_0$.)

**Recall:**

The objects in play are integral extensions, the contraction map, going up, lying over, incomparability, and Krull dimension.

![[Thm - Going Up#Statement]]

![[Thm - Incomparability#Statement]]

[[Thm - Lying Over|Lying over]] gives, for an integral extension, a prime of $B$ over any given prime of $A$. [[Def - Krull Dimension and Height|Krull dimension]] $\dim R$ is the supremum of $n$ over strict chains $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ in $\operatorname{Spec} R$.

---

# Convergent Strategy

**Problem class.** This is a *lift-a-chain* problem — the canonical use of going up. As the [[Commutative Algebra VIII — Going Up and Going Down#Problem-Solving Strategy|topic-page strategy]] records, to lift an ascending chain you anchor it with lying over and march it up with going up, using incomparability to keep it strict.

**Assumption pattern.** The hypothesis "$A \subseteq B$ integral, plus $\mathfrak{q}_0$ over $\mathfrak{p}_0$" is exactly the input that primes a chain-lift. Integrality supplies all three lifting tools: going up to extend, lying over to anchor (if needed), incomparability for strictness. The recognisable trigger is a *chain of primes in the base together with a partial lift* — which always calls for iterating going up.

**Theorem routing.** The route is a finite induction: starting from $\mathfrak{q}_0$ over $\mathfrak{p}_0$, apply [[Thm - Going Up|going up]] to $\mathfrak{p}_i \subsetneq \mathfrak{p}_{i+1}$ and $\mathfrak{q}_i$ to produce $\mathfrak{q}_{i+1} \supseteq \mathfrak{q}_i$ over $\mathfrak{p}_{i+1}$; at each step, [[Thm - Incomparability|incomparability]] (via distinct contractions $\mathfrak{p}_i \neq \mathfrak{p}_{i+1}$) upgrades the inclusion $\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1}$ to a *strict* one. After $n$ steps the full chain is built. Taking the supremum over chains of $A$ gives $\dim B \geq \dim A$.

**Key decision point.** The only subtlety is *strictness*. Going up alone yields $\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1}$ with $\subseteq$, not $\subsetneq$ — a priori the chain could stall with two equal primes, losing length. The genuine insight is that strictness is *free*: since $\mathfrak{q}_i \cap A = \mathfrak{p}_i \neq \mathfrak{p}_{i+1} = \mathfrak{q}_{i+1} \cap A$, the two primes have *different contractions*, so they cannot be equal. (One does not even need incomparability for *this* direction — distinct contractions trivially force distinct primes; incomparability is the deeper statement used when contracting.) This is why a strict base chain lifts to a strict chain of the *same length*, not merely a chain.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VIII — Going Up and Going Down#Legal Operations|the topic page's Legal Operations]]:

1. **Lift a chain to get $\dim A \leq \dim B$ (operation 8).** Anchor with lying over, extend with going up, keep strict via distinct contractions.

2. **Pass to the quotient to apply going up (operation 3).** Each going-up step internally reduces to lying over in the quotient extension $A/\mathfrak{p}_i \hookrightarrow B/\mathfrak{q}_i$.

3. **Use distinct contractions to force strictness.** $\mathfrak{q}_i \cap A = \mathfrak{p}_i \neq \mathfrak{p}_{i+1}$ gives $\mathfrak{q}_i \neq \mathfrak{q}_{i+1}$ immediately.

---

# Hints

> [!note]- Hint 1
> You have a prime $\mathfrak{q}_0$ over the bottom of the chain $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$, and you want to follow the chain *up*. Which theorem lets you enlarge a prime over $\mathfrak{p}_i$ to one over $\mathfrak{p}_{i+1}$ while keeping the containment?

> [!note]- Hint 2
> [[Thm - Going Up|Going up]]: given $\mathfrak{q}_i$ over $\mathfrak{p}_i$ and $\mathfrak{p}_i \subseteq \mathfrak{p}_{i+1}$, there is $\mathfrak{q}_{i+1} \supseteq \mathfrak{q}_i$ over $\mathfrak{p}_{i+1}$. Apply this $n$ times, building the chain one link at a time by induction.

> [!note]- Hint 3
> Going up only gives $\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1}$, not strict. But why must it be strict? Compare their contractions: $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ and $\mathfrak{q}_{i+1}\cap A = \mathfrak{p}_{i+1}$, and $\mathfrak{p}_i \neq \mathfrak{p}_{i+1}$. Two ideals with different contractions cannot be equal.

> [!note]- Hint 4
> For the dimension consequence: a strict chain of $A$ of length $n$ lifts to a strict chain of $B$ of length $n$, so $\dim B \geq n$. Take the supremum over all chains of $A$. (If no $\mathfrak{q}_0$ is handed to you, lying over produces one over $\mathfrak{p}_0$ to start.)

---

# Solution

The proof is a finite induction: starting from $\mathfrak{q}_0$ over $\mathfrak{p}_0$, each going-up step adds one link to the lifted chain, and the strictness of each link comes free from the fact that consecutive primes have different contractions. Iterating $n$ times builds the whole chain; taking suprema gives $\dim B \geq \dim A$.

**Step 1: Build the chain by iterating going up.**

By induction on $i$, construct $\mathfrak{q}_0 \subseteq \mathfrak{q}_1 \subseteq \cdots \subseteq \mathfrak{q}_n$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$.

> [!note]- Derivation
> *Base case.* $\mathfrak{q}_0$ is given, with $\mathfrak{q}_0 \cap A = \mathfrak{p}_0$.
>
> *Inductive step.* Suppose $\mathfrak{q}_i \in \operatorname{Spec} B$ has been constructed with $\mathfrak{q}_{i-1} \subseteq \mathfrak{q}_i$ and $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ (for $i < n$). Since $\mathfrak{p}_i \subseteq \mathfrak{p}_{i+1}$ and $\mathfrak{q}_i$ lies over $\mathfrak{p}_i$, apply [[Thm - Going Up|going up]] to the integral extension $A \subseteq B$: there is $\mathfrak{q}_{i+1} \in \operatorname{Spec} B$ with
> $$\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1} \qquad \text{and} \qquad \mathfrak{q}_{i+1} \cap A = \mathfrak{p}_{i+1}.$$
> After $n$ steps we have $\mathfrak{q}_0 \subseteq \mathfrak{q}_1 \subseteq \cdots \subseteq \mathfrak{q}_n$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$ for all $i$.

**Step 2: The chain is strict.**

Each inclusion $\mathfrak{q}_i \subseteq \mathfrak{q}_{i+1}$ is strict, because the contractions differ.

> [!note]- Derivation
> Suppose $\mathfrak{q}_i = \mathfrak{q}_{i+1}$ for some $i$. Then contracting to $A$,
> $$\mathfrak{p}_i = \mathfrak{q}_i \cap A = \mathfrak{q}_{i+1} \cap A = \mathfrak{p}_{i+1},$$
> contradicting the strictness $\mathfrak{p}_i \subsetneq \mathfrak{p}_{i+1}$ of the base chain. Hence $\mathfrak{q}_i \subsetneq \mathfrak{q}_{i+1}$ for each $i$, and
> $$\mathfrak{q}_0 \subsetneq \mathfrak{q}_1 \subsetneq \cdots \subsetneq \mathfrak{q}_n$$
> is a strict chain of length $n$ in $\operatorname{Spec} B$. (This direction needs only "distinct contractions $\Rightarrow$ distinct primes"; the deeper [[Thm - Incomparability|incomparability]] is what guarantees strictness in the *reverse* direction, when one contracts a chain of $B$.)

**Step 3: Deduce $\dim B \geq \dim A$.**

Every strict chain of $A$ lifts to a strict chain of $B$ of the same length, so $\dim B \geq \dim A$.

> [!note]- Derivation
> Let $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ be any strict chain in $\operatorname{Spec} A$. By [[Thm - Lying Over|lying over]] there is $\mathfrak{q}_0 \in \operatorname{Spec} B$ over $\mathfrak{p}_0$; by Steps 1–2 the chain lifts to a strict chain of length $n$ in $\operatorname{Spec} B$. Hence $\dim B \geq n$. Taking the supremum over all strict chains in $A$ gives $\dim B \geq \dim A$. (The reverse inequality $\dim B \leq \dim A$ is the contraction argument using incomparability; see [[Ex - Dimension is preserved under integral extension]].)

> [!note]- Complete formal solution
> Let $A \subseteq B$ be integral, $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_n$ a strict chain in $\operatorname{Spec} A$, and $\mathfrak{q}_0$ over $\mathfrak{p}_0$.
>
> Construct $\mathfrak{q}_1, \dots, \mathfrak{q}_n$ inductively: given $\mathfrak{q}_i$ over $\mathfrak{p}_i$, [[Thm - Going Up|going up]] applied to $\mathfrak{p}_i \subseteq \mathfrak{p}_{i+1}$ yields $\mathfrak{q}_{i+1} \supseteq \mathfrak{q}_i$ over $\mathfrak{p}_{i+1}$. This gives $\mathfrak{q}_0 \subseteq \cdots \subseteq \mathfrak{q}_n$ with $\mathfrak{q}_i \cap A = \mathfrak{p}_i$.
>
> Each step is strict: $\mathfrak{q}_i = \mathfrak{q}_{i+1}$ would give $\mathfrak{p}_i = \mathfrak{q}_i\cap A = \mathfrak{q}_{i+1}\cap A = \mathfrak{p}_{i+1}$, contradicting $\mathfrak{p}_i \subsetneq \mathfrak{p}_{i+1}$. So $\mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_n$ is strict of length $n$.
>
> For the dimension bound: any strict chain of $A$ (anchored over its bottom by lying over) lifts to a strict chain of $B$ of equal length, so $\dim B \geq \dim A$. $\blacksquare$

---

# Key Takeaways

**Lifting a chain is going-up iterated, with strictness for free from distinct contractions.** The reusable principle: to transport an ascending chain of primes across an integral extension, lift it one link at a time with going up, and observe that the lifted primes are automatically distinct because their contractions (the base primes) are distinct. The trigger is any "follow this chain upstairs" or "$\dim A \leq \dim B$" task. The pattern generalises beyond integral extensions to any map satisfying going up: the chain-lifting is a formal consequence of the going-up property plus the triviality that a map cannot identify two primes with different images. This is the upward half of every dimension-preservation argument.

**Strictness has two sources, and only one of them is incomparability.** When *lifting* a chain (this exercise), strictness is cheap: distinct base primes $\mathfrak{p}_i \neq \mathfrak{p}_{i+1}$ force distinct lifts $\mathfrak{q}_i \neq \mathfrak{q}_{i+1}$, no deep theorem needed. When *contracting* a chain of $B$ to test $\dim B \leq \dim A$, strictness is *not* free — two distinct primes of $B$ could in principle share a contraction, collapsing the chain — and there one genuinely needs [[Thm - Incomparability|incomparability]] to forbid the collapse. Internalising *which* direction needs incomparability is the key diagnostic: lifting needs only "distinct contractions $\Rightarrow$ distinct primes" (trivial), contracting needs "comparable primes with equal contraction are equal" (incomparability). Confusing the two leads to either over-citing or under-citing incomparability.

**This is half of dimension preservation; the other half is its mirror.** What you have proved gives $\dim B \geq \dim A$. The full theorem $\dim A = \dim B$ ([[Thm - Integral Extensions Preserve Dimension]], drilled in [[Ex - Dimension is preserved under integral extension]]) needs also $\dim B \leq \dim A$, obtained by *contracting* a chain of $B$ — the exact mirror of this argument, with incomparability replacing going up. Holding both halves together: going up lifts chains *up* (length preserved because contractions are distinct), incomparability pushes them *down* (length preserved because contractions cannot collapse). The symmetry is what makes a finite map preserve dimension, and this exercise is the upward girder. With Noether normalization it computes $\dim k[X_1,\dots,X_n] = n$ — the headline application.
