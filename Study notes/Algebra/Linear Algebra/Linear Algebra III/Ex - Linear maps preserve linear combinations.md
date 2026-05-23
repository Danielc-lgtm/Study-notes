---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $T : V \to W$ be a [[Def - Linear Map|linear map]]. Show that for every finite list of vectors $v_1, \ldots, v_n \in V$ and scalars $\lambda_1, \ldots, \lambda_n \in \mathbf{F}$,
$$T(\lambda_1 v_1 + \lambda_2 v_2 + \cdots + \lambda_n v_n) \;=\; \lambda_1 T v_1 + \lambda_2 T v_2 + \cdots + \lambda_n T v_n.$$

In words: a linear map preserves *every* linear combination, not just sums or scalar multiples in isolation.

**Recall:**

![[Def - Linear Map#The Definition]]

The two axioms — additivity and homogeneity — are individually about *one* operation at a time. The exercise asks us to show that the two combine to handle arbitrary linear combinations, by induction on the number of summands.

---

# Convergent Strategy

**Problem class.** This is a *prove a generalisation of the axioms* problem. The topic-page Problem-Solving Strategy classifies it as "show that two given properties combine to give a stronger property". The route runs through induction on the number of summands $n$, with additivity and homogeneity as the two ingredients combining at each step.

**Assumption pattern.** $T$ satisfies additivity ($T(u + v) = Tu + Tv$) and homogeneity ($T(\lambda v) = \lambda Tv$). We want to show the combined statement for any finite list of vectors. The defining feature: induction on $n$, with the inductive step being one application of additivity followed by one of homogeneity.

**Theorem routing.** No named theorem is needed beyond the axioms; the proof is a direct induction. The base case ($n = 1$) is just homogeneity. The inductive step splits an $n$-term sum as "$(n-1)$-term sum + last term" and applies additivity, then homogeneity to the last term.

**Key decision point.** The crucial choice is to induct on $n$, the number of summands, rather than (say) try a direct algebraic manipulation. Induction is the natural tool here because the statement is about *finite* lists of arbitrary length, and finite induction handles "all $n$" uniformly. The "key decision" is also to handle the inductive step by separating the last term from the others, which makes the application of additivity transparent.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Specify a linear map by its action on a basis** (operation 1) — implicit. The combined linearity proved here is exactly what makes the linear-map lemma work: once $T$ is specified on a basis, the formula $T(\sum c_k v_k) = \sum c_k Tv_k$ extends $T$ to all of $V$. So this exercise is *the lemma underlying* the linear-map lemma.

2. **Build new linear maps by sum, composition, restriction, and extension** (operation 10), implicitly. The pointwise sum and scalar product of linear maps are themselves linear *because* of this combined linearity — every step of the construction respects arbitrary linear combinations.

---

# Hints

> [!note]- Hint 1
> Induct on $n$, the number of summands. What is the case $n = 1$? What is the case $n = 2$?

> [!note]- Hint 2
> For the inductive step, write $\sum_{k=1}^n \lambda_k v_k$ as $\left(\sum_{k=1}^{n-1} \lambda_k v_k\right) + \lambda_n v_n$. Apply $T$ and use additivity, then apply the inductive hypothesis to the first part and homogeneity to the second.

> [!note]- Hint 3
> The base case $n = 1$ is $T(\lambda_1 v_1) = \lambda_1 T v_1$ — this is exactly the homogeneity axiom. For $n = 2$, $T(\lambda_1 v_1 + \lambda_2 v_2) = T(\lambda_1 v_1) + T(\lambda_2 v_2)$ by additivity, then $= \lambda_1 T v_1 + \lambda_2 T v_2$ by homogeneity applied twice.

---

# Solution

The plan is induction on $n$. The base case $n = 1$ is homogeneity. The inductive step splits an $n$-term linear combination into an $(n-1)$-term linear combination plus a single term, applies additivity to separate the two pieces, and applies the inductive hypothesis and homogeneity to finish.

**Step 1: Base case $n = 1$.**

$T(\lambda_1 v_1) = \lambda_1 T v_1$ — this is the homogeneity axiom applied directly.

> [!note]- Derivation
> By the homogeneity axiom of linearity, $T(\lambda v) = \lambda Tv$ for any $\lambda \in \mathbf{F}$ and $v \in V$. Applied with $\lambda = \lambda_1$ and $v = v_1$, we get $T(\lambda_1 v_1) = \lambda_1 T v_1$, which is the claim for $n = 1$.

**Step 2: Inductive step.**

Assume the claim holds for $n - 1$ summands: $T(\sum_{k=1}^{n-1} \lambda_k v_k) = \sum_{k=1}^{n-1} \lambda_k T v_k$. Prove it for $n$ summands.

> [!note]- Derivation
> Let $u := \sum_{k=1}^{n-1} \lambda_k v_k \in V$. Then $\sum_{k=1}^n \lambda_k v_k = u + \lambda_n v_n$, and
> $$T\!\left(\sum_{k=1}^n \lambda_k v_k\right) = T(u + \lambda_n v_n) = T(u) + T(\lambda_n v_n) \quad \text{(additivity)}.$$
> Now apply the inductive hypothesis to $T(u)$:
> $$T(u) = T\!\left(\sum_{k=1}^{n-1} \lambda_k v_k\right) = \sum_{k=1}^{n-1} \lambda_k T v_k,$$
> and homogeneity to $T(\lambda_n v_n)$:
> $$T(\lambda_n v_n) = \lambda_n T v_n.$$
> Combining,
> $$T\!\left(\sum_{k=1}^n \lambda_k v_k\right) = \sum_{k=1}^{n-1} \lambda_k T v_k + \lambda_n T v_n = \sum_{k=1}^n \lambda_k T v_k. \qquad \square$$

**Step 3: Conclude by induction.**

The claim holds for all $n \geq 1$ by induction.

> [!note]- Derivation
> Base case: $n = 1$ is the homogeneity axiom, proven in Step 1. Inductive step: if the claim holds for $n - 1$, it holds for $n$, as shown in Step 2. By the principle of mathematical induction, the claim holds for every $n \geq 1$.

> [!note]- Complete formal solution
> We prove the statement by induction on $n$, the number of summands.
>
> **Base case ($n = 1$).** By the homogeneity axiom of [[Def - Linear Map|linearity]],
> $$T(\lambda_1 v_1) = \lambda_1 T v_1.$$
>
> **Inductive step.** Assume the claim holds for $n - 1$ summands, where $n \geq 2$. Let $\lambda_1, \ldots, \lambda_n \in \mathbf{F}$ and $v_1, \ldots, v_n \in V$. Set $u := \sum_{k=1}^{n-1} \lambda_k v_k$. By additivity of $T$,
> $$T\!\left(\sum_{k=1}^n \lambda_k v_k\right) = T(u + \lambda_n v_n) = T(u) + T(\lambda_n v_n).$$
> By the inductive hypothesis, $T(u) = \sum_{k=1}^{n-1} \lambda_k T v_k$, and by homogeneity, $T(\lambda_n v_n) = \lambda_n T v_n$. Combining,
> $$T\!\left(\sum_{k=1}^n \lambda_k v_k\right) = \sum_{k=1}^{n-1} \lambda_k T v_k + \lambda_n T v_n = \sum_{k=1}^n \lambda_k T v_k.$$
>
> By induction, the claim holds for all $n \geq 1$. $\blacksquare$

---

# Key Takeaways

**Linearity is preserved by induction on linear combinations.** The two axioms — additivity and homogeneity — combine to produce the *true name* of linearity: $T(\sum \lambda_k v_k) = \sum \lambda_k T v_k$. The reusable principle is that two algebraic axioms, each handling one operation, combine via induction to handle the operation iterated arbitrarily many times. This is the same pattern that converts the [[Def - Group|group]] axiom "the product of two elements is in the [[Def - Group|group]]" into "the product of any finite list of elements is in the group", and similar combinations across algebra. The trigger is "axioms for two operations, want to handle finite combinations". The induction-on-length argument is the standard tool.

**The "true name" of linearity is preservation of linear combinations.** Every use of a linear map in practice — computing $T$ on a specific vector, matrix-vector multiplication, computing in coordinates, applying the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] — goes through this formula. The two axioms are what you *check*; this is what you *use*. The reusable principle is the operational characterisation of a definition. The trigger is "I have a linear map and a vector expressed as a linear combination" — apply the formula directly, no need to invoke additivity and homogeneity separately. This is the form of linearity used in the proof of every theorem in the chapter, from the matrix representation to rank–nullity to the composition theorem.

**Inductive proofs are the standard tool for "for all finite $n$".** When a statement involves a finite list of arbitrary length, induction on the length is almost always the right approach. The base case anchors the recursion; the inductive step does the real work, typically by isolating the last term from the rest. Other patterns in this style: induction on [[Def - Dimension|dimension]], induction on rank, induction on the number of factors in a product. The reusable principle is: whenever you see "$\sum_{k=1}^n$" with $n$ arbitrary, induction on $n$ is the first thing to try. The argument is mechanical once you set it up correctly, and it generalises immediately to "infinite linear combinations" in the appropriate convergence-based sense (e.g., Hilbert space basis expansions, formal power series).

---
