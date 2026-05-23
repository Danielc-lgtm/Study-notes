---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Vector Space"
  - "Thm - Uniqueness of Additive Identity and Inverses"
tags: [algebra, linear-algebra]
---

# Problem Statement

Show that in the [[Def - Vector Space|definition of a vector space]], the **additive-inverse axiom** (axiom 4: for every $v$ there exists $w$ with $v + w = 0$) can be replaced by the condition

$$0 \cdot v = 0 \text{ for every } v \in V$$

(where the $0$ on the left is the scalar zero and the $0$ on the right is the additive identity of $V$).

That is: a set $V$ with the seven non-inverse axioms (commutativity, associativity, additive identity, multiplicative identity, associativity of scalar multiplication, distributivity over vector addition, distributivity over scalar addition) plus the new axiom $0 \cdot v = 0$ is *automatically* a vector space — additive inverses exist and are given by $-v = (-1) v$.

(LADR Exercise 1B.5.)

**Recall:**

The [[Def - Vector Space|vector space axioms]]:

![[Def - Vector Space#The Definition]]

In the standard formulation, additive inverses are axiomatized; the corollary $0 \cdot v = 0$ is a theorem ([[Thm - Uniqueness of Additive Identity and Inverses]]). The exercise asks the converse: if $0 \cdot v = 0$ is taken as an axiom, can additive inverses be derived?

---

# Convergent Strategy

**Problem class:** This is an **axiom-trading** problem: replace one axiom in a set with another, and show the resulting axiom set defines the same class of objects. The pattern is to derive the replaced axiom from the new set, and vice versa.

**Assumption pattern:** All of axioms 1, 2, 3, 5, 6, 7, 8 (everything except the inverse axiom) plus the new axiom $0 \cdot v = 0$. We are *not* assuming axiom 4. The goal is to derive axiom 4.

**Theorem routing:** Define a candidate inverse $w = (-1) v$ and verify $v + w = 0$. This requires using the multiplicative identity (axiom 5), distributivity over scalar addition (axiom 8), and the new $0 \cdot v = 0$ axiom.

**Key decision point:** The cleanest argument **defines** $w = (-1) \cdot v$ and computes $v + w$. The computation uses $v = 1 \cdot v$ (axiom 5), distributivity to combine $1$ and $-1$ in $\mathbb{F}$, and the new axiom. This is the same computation that proves $(-1) v = -v$ in [[Thm - Uniqueness of Additive Identity and Inverses]], but now it is the existence proof for inverses rather than an identification of an existing inverse.

---

# Legal Operations Used

1. **Construct a candidate object by combining the given operations and verify it.** Here the candidate inverse is $(-1) v$, built by multiplying $v$ by the scalar $-1$. We then verify $v + (-1)v = 0$ using the other axioms. The "construct-and-verify" pattern is the standard technique whenever existence must be derived rather than assumed.

2. **Use distributivity over scalar addition to "factor" scalar identities.** Operation 1's pointwise verification, instantiated here: $1 \cdot v + (-1) \cdot v = (1 + (-1)) v = 0 \cdot v$. The distributive law axiom 8 is what bridges field arithmetic ($1 + (-1) = 0$) to vector identities ($1 v + (-1) v = 0 v$).

3. **Apply the substitute axiom $0 \cdot v = 0$ as a final step.** This is the new axiom under consideration; its use is the load-bearing step in deriving the original inverse axiom from the substitute set.

---

# Hints

> [!note]- Hint 1
> Take $w = (-1) \cdot v$ as the candidate inverse. Verify $v + w = 0$ using the other axioms.

> [!note]- Hint 2
> $v + (-1) v = 1 \cdot v + (-1) \cdot v = (1 + (-1)) v = 0 \cdot v = 0$, using axiom 5, axiom 8, and the new axiom.

---

# Solution

Plan: define $w = (-1) v$ and verify $v + w = 0$ using the other axioms.

**Step 1: Verify $(-1) v$ is well-defined.**

> [!note]- Derivation
> $(-1) \in \mathbb{F}$ (the additive inverse of $1$ in the field $\mathbb{F}$) and $v \in V$, so $(-1) v$ is well-defined as the scalar product.

**Step 2: Compute $v + (-1) v$.**

> [!note]- Derivation
> $$v + (-1) v = 1 \cdot v + (-1) \cdot v$$
> by axiom 5 (multiplicative identity in $V$). Then
> $$1 \cdot v + (-1) \cdot v = (1 + (-1)) v = 0 \cdot v$$
> by axiom 8 (distributivity over scalar addition). Finally
> $$0 \cdot v = 0$$
> by the new axiom. Combining: $v + (-1) v = 0$. So $w = (-1) v$ is an additive inverse of $v$.

**Step 3: Verify the original additive-inverse axiom.**

> [!note]- Derivation
> By Step 2, every $v \in V$ has the additive inverse $w = (-1) v$ satisfying $v + w = 0$. This is exactly the original axiom 4.

> [!note]- Complete formal solution
> Assume axioms 1, 2, 3, 5, 6, 7, 8 of a vector space, plus the new axiom $0 \cdot v = 0$ for all $v \in V$ (where the $0$ on the left is the scalar zero in $\mathbb{F}$ and the $0$ on the right is the additive identity in $V$). Let $v \in V$. Then
> $$v + (-1) v = 1 \cdot v + (-1) \cdot v = (1 + (-1)) v = 0 \cdot v = 0,$$
> using axiom 5, axiom 8 (distributivity over scalar addition), and the new axiom. So $(-1) v$ is an additive inverse of $v$. The original axiom 4 holds. $\blacksquare$
>
> *Converse.* Conversely, given a vector space satisfying axiom 4, the corollary $0 \cdot v = 0$ follows from $0 v = (0 + 0) v = 0 v + 0 v$ by axiom 8 and cancellation using axiom 4 (see [[Thm - Uniqueness of Additive Identity and Inverses]]). So the two axiom sets describe the same class of objects.

---

# Key Takeaways

**Axiom systems often admit equivalent reformulations.** The vector-space axioms are not unique — they are *clean*, not minimal, and various subsets imply equivalent collections of objects. This exercise illustrates one such trade: dropping "additive inverses exist" and adding "$0 \cdot v = 0$" gives the same class. The same flexibility appears in [[Def - Group|group theory]] (e.g. one-sided identity plus one-sided inverses imply the two-sided versions) and elsewhere. Knowing that an axiom can be replaced sometimes simplifies verification: to show a candidate is a vector space, it might be easier to prove $0 \cdot v = 0$ than to construct additive inverses directly.

**The corollary $0 \cdot v = 0$ is doing real work, not just bookkeeping.** In the standard formulation, $0 \cdot v = 0$ is a *theorem* ([[Thm - Uniqueness of Additive Identity and Inverses]]) derived from the axioms; in this exercise's reformulation it is an *axiom* generating additive inverses. The fact that the same identity can play either role — theorem or axiom — depending on the formulation reveals that it encodes nontrivial structural content. In other algebraic settings ([[Def - Ring|rings]], [[Def - Module|modules]], algebras over a field), the analogous "zero-scalar kills" identity is similarly load-bearing.

**The role of distributivity over scalar addition (axiom 8) is to make zero kill everything.** The proof in Step 2 uses axiom 8 ($(a + b) v = av + bv$) to convert $1 \cdot v + (-1) \cdot v$ into $(1 + (-1)) v = 0 \cdot v$. Without axiom 8, scalar arithmetic in $\mathbb{F}$ would not propagate to vectors, and there would be no reason to expect $0 \cdot v$ to be the zero vector. So axiom 8 is the bridge that exports algebra from $\mathbb{F}$ to $V$, and it is the structural reason this exercise works. Recognizing which distributivity does which work — axiom 7 makes scaling commute with summing, axiom 8 makes summing of scalars commute with scaling — sharpens one's grip on the axiom system.
