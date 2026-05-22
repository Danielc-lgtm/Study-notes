---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Vector Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a vector space over a [[Def - Field|field]] $\mathbb{F}$. The additive identity is $0 \in V$; the additive inverse of $v \in V$ is $-v$, defined by $v + (-v) = 0$. The scalar zero in $\mathbb{F}$ is also denoted $0$ — context distinguishes the two. See [[Linear Algebra I — §1 Vector Spaces]] for the full notation registry.

---

# Statement

> **Theorem.** Let $V$ be a vector space over $\mathbb{F}$. Then:
> 1. **Uniqueness of the additive identity.** $V$ has exactly one additive identity. If $0$ and $0'$ both satisfy $v + 0 = v$ and $v + 0' = v$ for all $v \in V$, then $0 = 0'$.
> 2. **Uniqueness of additive inverses.** Each $v \in V$ has exactly one additive inverse. If $w, w' \in V$ both satisfy $v + w = 0$ and $v + w' = 0$, then $w = w'$.

> **Corollaries.** For every $v \in V$ and every $a \in \mathbb{F}$:
> - $0 \cdot v = 0$ (where the left $0$ is the scalar zero and the right $0$ is the vector zero).
> - $a \cdot 0 = 0$ (where both zeros are the vector zero).
> - $(-1) \cdot v = -v$.

The uniqueness claims justify writing "the" additive identity and "the" additive inverse, and the corollaries are the first computational consequences of the vector-space axioms — they look obvious but require proof from the axioms.

---

# Motivation

The vector space axioms (see [[Def - Vector Space]]) demand that an additive identity *exists* and that every vector *has* an additive inverse, but they say nothing about uniqueness. A priori, $V$ could have several different additive identities, and a single vector could have several different additive inverses. The theorem says no — both are unique, and the proofs are short consequences of the axioms.

The point of the theorem is not the proof but the conclusion: it licenses the notation "$0_V$" (the zero vector) and "$-v$" (the inverse of $v$) as referring to unique objects. Without uniqueness, the notation would be ambiguous and the entire algebra of subtraction $u - v = u + (-v)$ would be ill-defined.

The corollaries are equally essential. They are the rules by which one manipulates scalar multiplication in proofs: "scaling by zero gives the zero vector", "scaling the zero vector gives the zero vector", and "scaling by $-1$ gives the additive inverse". These look obvious — and they are, once proved — but in a structure as abstract as a vector space, each must be checked against the axioms. The proofs reveal which axioms are loadbearing: $0 \cdot v = 0$ uses distributivity (axiom 8), $a \cdot 0 = 0$ uses distributivity (axiom 7), and $(-1) \cdot v = -v$ uses the distributive law and uniqueness of inverses.

A subtle pedagogical point: the proof of uniqueness for the additive inverse uses **associativity** in a load-bearing way (just as in [[Def - Group|group theory]]: without associativity, "two cancelling partners" need not be equal). So associativity is not just bookkeeping; it is what makes inverses well-defined.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: any vector space. The interest of this theorem is what it lets you assume in *other* arguments — almost every later proof in linear algebra silently invokes one of these corollaries.

A first source is **a proof that needs to manipulate $v + (-v) = 0$ to derive cancellation**. From $v + u = v + w$, the standard move is to add $-v$ to both sides: $-v + (v + u) = -v + (v + w)$, then associate to get $(-v + v) + u = (-v + v) + w$, then use $-v + v = 0$ to get $0 + u = 0 + w$, hence $u = w$. This left-cancellation is what licenses solving equations in a vector space, and it depends on the additive inverse being well-defined.

A second source is **a proof that needs to certify a complicated expression equals zero**. The cleanest way to show $X = 0$ is often to exhibit it as $X = Y + (-Y)$ for some $Y$, then invoke uniqueness of the inverse and the fact that $0$ is the only thing $Y + (-Y)$ can equal. This is the engine of many algebraic verifications, e.g. the proof that $(-1) v = -v$ above: show $(-1)v + v = 0$, conclude by uniqueness that $(-1)v$ is the additive inverse of $v$.

A third source is **a proof that exploits "additive zero is unique"**. The proof of [[Thm - Conditions for a Direct Sum]] hinges on this: if $0 \in V_1 + \dots + V_m$ admits two decompositions, both must equal the same $0$, hence their difference is also zero — and so on. Throughout linear algebra, "there is only one zero vector" is what lets uniqueness arguments terminate.

**Targets (Output Amplification)**

The conclusion is that the zero vector and inverses are well-defined, and that scaling by zero and $-1$ behave as expected. Combining with one more property gives:

A first combination is **uniqueness of $0$ plus a linear map gives that the kernel is a subspace**. Conclusion $C$: $V$ has a unique zero vector $0_V$. Property $D$: $T : V \to W$ is a linear map. Result $E$: $\ker T = \{v \in V : T v = 0_W\}$ is well-defined as a set (since $0_W$ is unique) and is a subspace (since $T (au + bv) = a T u + b T v = 0_W$ if $u, v \in \ker T$). The uniqueness of $0_W$ is the silent step that makes the definition of $\ker T$ unambiguous.

A second combination is **$(-1) v = -v$ plus a subspace criterion gives closure under inverses**. Conclusion $C$: $-v = (-1) v$. Property $D$: $U$ is a subspace, closed under scalar multiplication. Result $E$: $U$ is closed under additive inverses, since $-u = (-1) u \in U$ by scalar closure. This is the structural reason the subspace criterion (see [[Def - Subspace]]) does not need a separate "closed under inverses" condition: the scalar $-1$ does that work via this corollary.

A third combination is **$0 \cdot v = 0$ plus a linear independence argument forces nonzero scalars**. Conclusion $C$: $0 \cdot v = 0$ for all $v$. Property $D$: a candidate linear-dependence relation $a_1 v_1 + \dots + a_n v_n = 0$ with the $v_k$ candidate-independent. Result $E$: the relation gives information only when some $a_k \neq 0$ — the trivial case $a_1 = \dots = a_n = 0$ is always available by the corollary and carries no information. This is the structural rationale behind the definition of linear independence: the trivial relation is "free" and must be excluded.

---

# Why Is It True

The intuition is **algebraic cancellation: in any structure with associative addition and inverses, "having two of something" forces the two to coincide**.

For the additive identity: suppose $0$ and $0'$ are both identities. Then $0 = 0 + 0' = 0'$. The first equality uses that $0'$ is an identity (acts as $+0'$); the second uses that $0$ is an identity (acts as $0 + $). Each identity makes the other invisible, and the chain forces them equal.

For inverses: suppose $w, w'$ are both inverses of $v$. Then $w = w + 0 = w + (v + w') = (w + v) + w' = 0 + w' = w'$. The crucial step is the parenthesization in the middle: associativity lets us re-bracket so the cancellation $w + v = 0$ is exposed. Without associativity the argument would fail; this is why associativity is more than bookkeeping.

For the corollaries: each is a specific instance of the cancellation principle. $0 v$ satisfies $0 v + 0 v = (0 + 0) v = 0 v$ by distributivity, so adding $-(0 v)$ to both sides gives $0 v = 0$. Similarly $a \cdot 0 = a (0 + 0) = a \cdot 0 + a \cdot 0$, and again cancel. And $(-1) v + v = (-1) v + 1 \cdot v = (-1 + 1) v = 0 \cdot v = 0$, so $(-1) v$ is *the* inverse of $v$.

**The single one-liner: in a vector space, anything you can write as "$X + X = X$" must equal $0$, and anything that cancels with $v$ must be $-v$.**

---

# What Makes This Hard

The proof is short, but the trap is conceptual: students often think these facts are part of the definition or follow trivially from "common sense", and miss that they require explicit derivation from the axioms. The non-obvious step in the inverse-uniqueness proof is the parenthesization $w + (v + w') = (w + v) + w'$, which depends on associativity (axiom 2 of vector spaces). Without associativity the chain of equalities does not work. The corollaries similarly require attention to *which* axiom is invoked at each step — distributivity over scalars for $0 v = 0$, distributivity over vectors for $a \cdot 0 = 0$.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
For uniqueness of the additive identity, compute $0 + 0'$ in two ways using each identity's defining property. For uniqueness of the inverse, use associativity to expose a cancellation. For the corollaries, use the appropriate distributive law to write the candidate "$X + X = X$" form, then cancel.

**Subgoal decomposition:**

1. **Unique additive identity:** If $0, 0'$ are both additive identities, then $0 = 0'$.
   - *Hint:* Compute $0 + 0'$ using each side.
   - *Why needed:* This is part (1) of the theorem.

2. **Unique additive inverse:** If $w, w'$ both satisfy $v + w = v + w' = 0$, then $w = w'$.
   - *Hint:* $w = w + 0 = w + (v + w') = (w + v) + w' = 0 + w' = w'$, using associativity.
   - *Why needed:* This is part (2) and the proof exhibits the role of associativity.

3. **Corollary $0 \cdot v = 0$:** Use distributivity over scalar addition: $0 v = (0 + 0) v = 0 v + 0 v$, then add $-(0 v)$ to both sides.
   - *Hint:* The defining equation $X = X + X$ forces $X = 0$ in any group, via cancellation.
   - *Why needed:* Standard corollary used everywhere.

4. **Corollary $a \cdot 0 = 0$:** Use distributivity over vector addition: $a \cdot 0 = a (0 + 0) = a \cdot 0 + a \cdot 0$, then cancel.
   - *Hint:* Same pattern as the previous corollary, on the other distributive law.
   - *Why needed:* Standard corollary.

5. **Corollary $(-1) v = -v$:** Use both distributivity and the multiplicative identity: $(-1) v + v = (-1) v + 1 \cdot v = (-1 + 1) v = 0 \cdot v = 0$, so $(-1) v$ is an additive inverse of $v$, and by uniqueness equals $-v$.
   - *Hint:* Express the candidate inverse explicitly and verify it satisfies the inverse property.
   - *Why needed:* This corollary is invoked in nearly every subspace argument and is the reason subspaces don't need a separate "closure under inverses" axiom.

---

# Lemma Decomposition

> [!note]- Lemma 1: Uniqueness of the additive identity
> **Statement:** If $0$ and $0'$ both satisfy axiom 3 ($v + 0 = v$ and $v + 0' = v$ for all $v$), then $0 = 0'$.
>
> **Hint:** Compute $0 + 0'$ in two ways, using each as an identity.
>
> **Why needed:** Licenses the notation "the zero vector" and is the building block for [[Thm - Conditions for a Direct Sum]] (in which uniqueness at zero propagates).
>
> > [!note]- Full proof
> > Suppose $0, 0' \in V$ both satisfy $v + 0 = v$ and $v + 0' = v$ for all $v \in V$. Then $0' = 0' + 0$ (taking $v = 0'$ in $v + 0 = v$) and $0' + 0 = 0 + 0'$ (commutativity, axiom 1) and $0 + 0' = 0$ (taking $v = 0$ in $v + 0' = v$). Concatenating: $0' = 0' + 0 = 0 + 0' = 0$, so $0' = 0$.

> [!note]- Lemma 2: Uniqueness of additive inverses
> **Statement:** If $w$ and $w'$ both satisfy $v + w = 0$ and $v + w' = 0$, then $w = w'$.
>
> **Hint:** Use associativity to re-bracket $w + (v + w')$ and expose the cancellation.
>
> **Why needed:** Licenses the notation $-v$ for "the inverse of $v$" and underlies all of subtraction.
>
> > [!note]- Full proof
> > Suppose $v + w = 0$ and $v + w' = 0$. Then
> > $$w = w + 0 = w + (v + w') = (w + v) + w' = (v + w) + w' = 0 + w' = w' + 0 = w'.$$
> > In order: the identity axiom (3); the assumption $v + w' = 0$; associativity (2); commutativity (1); the assumption $v + w = 0$; commutativity (1); the identity axiom (3). The load-bearing step is the associative re-bracketing — without it, the cancellation could not be exposed.

> [!note]- Lemma 3: Three computational corollaries
> **Statement:** For all $v \in V$ and $a \in \mathbb{F}$: $0 v = 0$, $a \cdot 0 = 0$, and $(-1) v = -v$.
>
> **Hint:** Each corollary uses one distributive law to produce an equation of the form $X = X + X$ or $X + v = 0$, then cancels using inverses.
>
> **Why needed:** These corollaries are invoked silently in nearly every later proof — by [[Def - Subspace|subspace closure]] (no separate inverses axiom is needed because $(-1) v = -v$), by linear-dependence relations (the trivial relation $0 = 0 \cdot v_1 + \dots$ is always valid), and by direct sums (the trivial decomposition of zero).
>
> > [!note]- Full proof
> > **$0 v = 0$:** Using distributivity over scalar addition (axiom 8), $0 v = (0 + 0) v = 0 v + 0 v$. Adding $-(0 v)$ to both sides (using uniqueness of inverses): $0 = 0 v$.
> >
> > **$a \cdot 0 = 0$:** Using distributivity over vector addition (axiom 7), $a \cdot 0 = a (0 + 0) = a \cdot 0 + a \cdot 0$. Adding $-(a \cdot 0)$ to both sides: $0 = a \cdot 0$.
> >
> > **$(-1) v = -v$:** Using axioms 5 (multiplicative identity), 8 (distributivity over scalar addition), and the first corollary,
> > $$(-1) v + v = (-1) v + 1 \cdot v = (-1 + 1) v = 0 \cdot v = 0.$$
> > So $(-1) v$ satisfies $(-1) v + v = 0$, hence $(-1) v$ is the additive inverse of $v$. By Lemma 2 (uniqueness of inverses), $(-1) v = -v$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $V$ be a vector space over $\mathbb{F}$. Then $V$ has exactly one additive identity, and each $v \in V$ has exactly one additive inverse.
>
> *Proof of uniqueness of the additive identity.* Suppose $0, 0' \in V$ both satisfy $v + 0 = v$ and $v + 0' = v$ for all $v$. Then
> $$0' = 0' + 0 = 0 + 0' = 0,$$
> where the first equality applies $v + 0 = v$ with $v = 0'$, the second uses commutativity, and the third applies $v + 0' = v$ with $v = 0$.
>
> *Proof of uniqueness of the additive inverse.* Suppose $v + w = 0$ and $v + w' = 0$. Then
> $$w = w + 0 = w + (v + w') = (w + v) + w' = (v + w) + w' = 0 + w' = w'.$$
> The crucial step is the associative re-bracketing $w + (v + w') = (w + v) + w'$.
>
> *Proof of $0 v = 0$:* $0 v = (0 + 0) v = 0 v + 0 v$ by distributivity over scalar addition; subtracting $0 v$ gives $0 = 0 v$.
>
> *Proof of $a \cdot 0 = 0$:* $a \cdot 0 = a (0 + 0) = a \cdot 0 + a \cdot 0$ by distributivity over vector addition; subtracting $a \cdot 0$ gives $0 = a \cdot 0$.
>
> *Proof of $(-1) v = -v$:* $(-1) v + v = (-1) v + 1 \cdot v = (-1 + 1) v = 0 \cdot v = 0$ by the multiplicative identity, distributivity over scalar addition, and the corollary $0 v = 0$. So $(-1) v$ is an additive inverse of $v$, and by uniqueness $(-1) v = -v$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Uniqueness of group identities and inverses.** The proofs given here are nearly identical to the proofs in [[Def - Group|group theory]] that group identities and inverses are unique — the only difference is that the underlying operation is addition rather than abstract multiplication. The argument for inverses uses associativity in exactly the same way, exposing that associativity is what makes inverses well-defined in any algebraic structure, not just vector spaces.

**Uniqueness of identity in monoids and semigroups.** A *monoid* is a set with an associative operation and a two-sided identity (no inverses required). The proof of uniqueness of the identity transfers verbatim to monoids. The inverse-uniqueness proof, however, requires actual inverses to exist; for monoids one talks instead about elements *with* inverses (units) and verifies uniqueness for those.

**Uniqueness of the additive identity in a ring or a field.** The same argument shows that a ring's (and a field's, see [[Def - Field]]) additive identity is unique. The multiplicative identity in a ring with $1$ is also unique by the same argument. In a field, multiplicative inverses are also unique by the same associative re-bracketing. The argument is purely about additive-group structure.

**Uniqueness of solutions to linear equations.** Given a linear equation $v + 3 x = w$ in a vector space, the solution is unique: $x = \frac{1}{3}(w - v)$. The uniqueness comes from the well-definedness of $-v$ (this theorem), the well-definedness of scalar inverses (since the field has multiplicative inverses), and the well-definedness of subtraction $w - v = w + (-v)$. This is LADR Exercise 1B.3, and it is the simplest application of the theorem.

---

# Bridges

- **[[Def - Group|Group theory: uniqueness of identity and inverses]]** — the proofs here are word-for-word the same as the proofs that a group has a unique identity and that every element has a unique inverse. The reason is that the additive structure $(V, +, 0)$ of a vector space is an abelian group, and the uniqueness proofs use only the group axioms (associativity, identity, inverses). Reading both proofs side by side exposes that "vector space" inherits all the additive structure-theorems from "abelian group" for free.

- **[[Thm - Conditions for a Direct Sum]]** — the theorem here ensures that the additive identity of a vector space is a single well-defined point, which is the hypothesis on which the directness-via-zero criterion rests. Without uniqueness of $0$, one could not even formulate "the only decomposition of zero is trivial" cleanly.

- **The subspace criterion** — the corollary $(-1) v = -v$ is what licenses the omission of a "closed under additive inverses" axiom in the [[Def - Subspace|subspace criterion]]. Closure under scalar multiplication includes closure by the scalar $-1$, which by the corollary takes $v$ to $-v$. So scalar closure subsumes inverse closure, and the subspace criterion is correspondingly shorter.

- **Cancellation and the rank-nullity theorem** — left- and right-cancellation in a vector space come from this theorem: $v + u = v + w$ implies $u = w$ by adding $-v$ to both sides. Cancellation is what allows the rank-nullity argument in [[Linear Algebra III — §3A–D Linear Maps]] to identify the image with a quotient by the kernel.
