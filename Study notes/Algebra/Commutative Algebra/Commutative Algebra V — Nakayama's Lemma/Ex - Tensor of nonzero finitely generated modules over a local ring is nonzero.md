---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Finitely Generated Module"
  - "Def - Local Ring and Residue Field"
  - "Thm - Nakayama's Lemma"
  - "Thm - Universal Property of the Tensor Product of Modules"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $(A, \mathfrak m)$ be a [[Def - Local Ring and Residue Field|local ring]] with residue field $k = A/\mathfrak m$, and let $M, N$ be [[Def - Finitely Generated Module|finitely generated]] $A$-modules. Prove that
$$M \otimes_A N = 0 \quad\Longrightarrow\quad M = 0 \ \text{ or } \ N = 0.$$

*Hint (Becker).* First solve the case where $A$ is a field. Then tensor with $A/\mathfrak m$ and use Nakayama.

(This is Becker Example Sheet 3, Q1(d).)

**Recall:**

The objects in play are a local ring, finitely generated modules, the tensor product, and Nakayama's lemma.

![[Def - Local Ring and Residue Field#Local ring]]

The [[Thm - Universal Property of the Tensor Product of Modules|tensor product]] $M \otimes_A N$ is the universal target of bilinear maps out of $M \times N$. The two facts used here are its compatibility with base change and its behaviour over a field:

- **Base change:** for any $A$-algebra $B$, $(M \otimes_A N) \otimes_A B \cong (M \otimes_A B) \otimes_B (N \otimes_A B)$. With $B = k = A/\mathfrak m$ this reads $(M \otimes_A N) \otimes_A k \cong (M/\mathfrak m M) \otimes_k (N/\mathfrak m N)$.
- **Over a field:** for $k$-vector spaces $V, W$, $\dim_k(V \otimes_k W) = (\dim_k V)(\dim_k W)$, so $V \otimes_k W = 0 \iff V = 0$ or $W = 0$.

The finishing tool — Nakayama's lemma:

![[Thm - Nakayama's Lemma#Statement]]

For a local ring, $J(A) = \mathfrak m$, so "$M/\mathfrak m M = 0$" forces "$M = 0$" when $M$ is finitely generated.

---

# Convergent Strategy

**Problem class.** This is a *reduce-to-the-field-then-lift* problem, the purest instance of the chapter's central method. The [[Commutative Algebra V — Nakayama's Lemma#Problem-Solving Strategy|topic strategy]]'s third paragraph names it: reduce the structure modulo $\mathfrak m$ to a vector-space statement you can settle, then lift the conclusion with Nakayama.

**Assumption pattern.** Both modules are finitely generated (the Nakayama hypothesis), and $A$ is local (so $\mathfrak m = J(A)$). The recognisable trigger is "$M \otimes_A N = 0$ over a local ring": tensoring is hard over $A$ but easy over $k$, so the move is to base-change the *whole equation* to $k$, where the tensor product of vector spaces is transparent.

**Theorem routing.** The route is: tensor the hypothesis $M \otimes_A N = 0$ with $k$; by base change this gives $(M/\mathfrak m M) \otimes_k (N/\mathfrak m N) = 0$; the field case forces $M/\mathfrak m M = 0$ or $N/\mathfrak m N = 0$; and [[Thm - Nakayama's Lemma|Nakayama's lemma]] lifts "$M/\mathfrak m M = 0$" to "$M = 0$" (and likewise for $N$), using finite generation and $\mathfrak m = J(A)$.

**Key decision point.** The non-obvious move is to **tensor the equation $M \otimes_A N = 0$ with $k$** rather than trying to argue about $M \otimes_A N$ directly over $A$. The payoff is that base change converts a tensor over $A$ into a tensor of *vector spaces* over $k$, where vanishing factors cleanly through dimension. The natural alternative — manipulating $M \otimes_A N$ with generators and relations over $A$ — is intractable because tensor products over a general ring can vanish unexpectedly. The whole insight is that the obstruction is visible already at the residue field, and Nakayama guarantees nothing is lost in passing there.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra V — Nakayama's Lemma#Legal Operations|the topic page's Legal Operations]]:

1. **Reduce modulo $\mathfrak m$ to land in a vector space** (operation 5). Base-change the hypothesis to $k$, turning $M \otimes_A N$ into $(M/\mathfrak m M) \otimes_k (N/\mathfrak m N)$.

2. **Use the field case of tensor vanishing.** Over $k$, $V \otimes_k W = 0 \iff V = 0$ or $W = 0$ (dimensions multiply).

3. **Invert $1 + (\text{Jacobson element})$ via Nakayama** (operations 4 and the bare lemma). Lift $M/\mathfrak m M = 0$ to $M = 0$ using finite generation and $\mathfrak m = J(A)$.

---

# Hints

> [!note]- Hint 1
> Tensor products over a general ring are hard; over a field they are easy ($\dim$ multiplies). You have a residue field $k = A/\mathfrak m$. Try to transport the whole hypothesis $M \otimes_A N = 0$ down to $k$. What does $(M \otimes_A N) \otimes_A k$ simplify to?

> [!note]- Hint 2
> Base change: $(M \otimes_A N) \otimes_A k \cong (M \otimes_A k) \otimes_k (N \otimes_A k) = (M/\mathfrak m M) \otimes_k (N/\mathfrak m N)$. Since $M \otimes_A N = 0$, the left side is $0$, so this $k$-vector-space tensor product is $0$. Now use the field case.

> [!note]- Hint 3
> Over a field, $V \otimes_k W = 0 \Rightarrow V = 0$ or $W = 0$. So $M/\mathfrak m M = 0$ or $N/\mathfrak m N = 0$. Say $M/\mathfrak m M = 0$, i.e. $\mathfrak m M = M$. With $M$ finitely generated and $\mathfrak m = J(A)$, what does Nakayama give?

---

# Solution

The proof reduces the tensor-vanishing hypothesis to the residue field, settles it there by dimension-counting, and lifts the conclusion with Nakayama. Step 1 base-changes the equation to $k$; Step 2 applies the field case; Step 3 lifts via Nakayama.

**Step 1: Base-change the hypothesis to $k$, obtaining a vanishing tensor of vector spaces.**

Tensoring $M \otimes_A N = 0$ with $k$ gives $(M/\mathfrak m M) \otimes_k (N/\mathfrak m N) = 0$.

> [!note]- Derivation
> Tensor the hypothesis with the residue field $k = A/\mathfrak m$ over $A$. Since $M \otimes_A N = 0$,
> $$0 = (M \otimes_A N) \otimes_A k.$$
> By the base-change identity for tensor products — $(M \otimes_A N)\otimes_A B \cong (M\otimes_A B)\otimes_B (N \otimes_A B)$ for any $A$-algebra $B$, applied with $B = k$ — and using $M \otimes_A k = M/\mathfrak m M$ (and similarly for $N$),
> $$(M \otimes_A N)\otimes_A k \;\cong\; (M/\mathfrak m M) \otimes_k (N/\mathfrak m N).$$
> Here $V := M/\mathfrak m M$ and $W := N/\mathfrak m N$ are $k$-vector spaces. So
> $$V \otimes_k W = 0.$$

**Step 2: The field case forces $V = 0$ or $W = 0$.**

Over a field, a tensor product vanishes only if a factor vanishes; so $M/\mathfrak m M = 0$ or $N/\mathfrak m N = 0$.

> [!note]- Derivation
> For $k$-vector spaces $V, W$ with bases of sizes $\dim_k V, \dim_k W$, the tensor product $V \otimes_k W$ has basis the products of basis elements, so
> $$\dim_k(V \otimes_k W) = (\dim_k V)(\dim_k W).$$
> Thus $V \otimes_k W = 0$ iff $\dim_k V = 0$ or $\dim_k W = 0$, i.e. $V = 0$ or $W = 0$. Applying this to $V \otimes_k W = 0$ from Step 1,
> $$M/\mathfrak m M = 0 \quad\text{or}\quad N/\mathfrak m N = 0.$$

**Step 3: Lift the vanishing to $M$ or $N$ via Nakayama.**

Say $M/\mathfrak m M = 0$, i.e. $\mathfrak m M = M$; Nakayama gives $M = 0$.

> [!note]- Derivation
> Suppose $M/\mathfrak m M = 0$ (the case $N/\mathfrak m N = 0$ is symmetric). This means $\mathfrak m M = M$. Now $M$ is finitely generated and, since $A$ is local, $\mathfrak m = J(A)$, so $\mathfrak m \subseteq J(A)$. By [[Thm - Nakayama's Lemma|Nakayama's lemma]],
> $$M = 0.$$
> Symmetrically, if $N/\mathfrak m N = 0$ then $N = 0$. Hence $M = 0$ or $N = 0$, as required. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For finitely generated modules $M, N$ over a local ring $(A,\mathfrak m)$: $M \otimes_A N = 0 \Rightarrow M = 0$ or $N = 0$.
>
> Tensoring $M \otimes_A N = 0$ with $k = A/\mathfrak m$ over $A$, base change gives
> $$0 = (M\otimes_A N)\otimes_A k \cong (M/\mathfrak m M)\otimes_k (N/\mathfrak m N).$$
> Over the field $k$, $\dim_k(V \otimes_k W) = (\dim_k V)(\dim_k W)$, so $(M/\mathfrak m M)\otimes_k(N/\mathfrak m N) = 0$ forces $M/\mathfrak m M = 0$ or $N/\mathfrak m N = 0$. In the first case $\mathfrak m M = M$ with $M$ finitely generated and $\mathfrak m = J(A)$, so Nakayama gives $M = 0$; in the second, symmetrically, $N = 0$. $\blacksquare$

---

# Key Takeaways

**A vanishing over a local ring is often a vanishing over the residue field in disguise — base-change down, solve, lift.** The architecture of this proof is the universal three-step pattern of the chapter: (1) reduce the structure modulo $\mathfrak m$ to land in $k$-vector spaces, where the question is linear algebra; (2) solve the linear-algebra question; (3) lift the conclusion with Nakayama, which guarantees the reduction lost nothing essential. Here the question is "when does a tensor product vanish?", easy over a field (dimensions multiply) and obscure over a general ring. Whenever you face a hard structural question over a local ring — vanishing, freeness, generation, rank — the first instinct should be to tensor with $k$ and see whether the residue-field version is tractable. The lifting back is Nakayama's gift.

**Base change is the tool that moves an equation between rings; tensoring the hypothesis with $k$ is the key step.** The decisive computation is $(M \otimes_A N) \otimes_A k \cong (M/\mathfrak m M) \otimes_k (N/\mathfrak m N)$ — the tensor product commutes with base change, turning a tensor over $A$ into a tensor of vector spaces over $k$. This is worth holding as a standalone trigger: to reduce a tensor-product statement to the residue field, tensor the *whole equation* with $k$ and use that $M \otimes_A k = M/\mathfrak m M$. The same base-change move pervades commutative algebra — it is how one computes fibres of sheaves, reduces flatness questions to the residue field, and relates $\operatorname{Tor}$ over $A$ to $\operatorname{Tor}$ over $k$. The "fibre" $M \otimes_A k$ is the recurring object.

**The proof needs locality for Nakayama and a single residue field; it fails over a non-local ring.** Both hypotheses are essential and route to different steps. Finite generation is consumed by Nakayama in Step 3. Locality is needed twice: it provides the *single* residue field $k$ to base-change to, and it makes $\mathfrak m = J(A)$ so Nakayama accepts the lift. Over a non-local ring the result is false: take $A = \mathbb Z$, $M = \mathbb Z/2$, $N = \mathbb Z/3$; then $M \otimes_{\mathbb Z} N = \mathbb Z/\gcd(2,3) = \mathbb Z/1 = 0$, yet $M, N \neq 0$. The two modules are supported at *different* maximal ideals — $M$ at $(2)$, $N$ at $(3)$ — and their supports being disjoint is exactly why the tensor vanishes without either factor doing so. Localizing at any single prime would make one of them zero, restoring the implication. This is the diagnostic for spaced practice: tensor-vanishing without factor-vanishing means *disjoint supports*, which a local ring forbids. Compare [[Ex - Tensoring with R over I gives M over IM]] for the base-change identity in another guise.
