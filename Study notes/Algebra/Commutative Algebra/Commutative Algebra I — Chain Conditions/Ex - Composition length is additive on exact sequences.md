---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Composition Series and Length"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Thm - Length is Additive and Finite iff Noetherian and Artinian"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $\mathcal{C}$ be a class of $R$-modules closed under the relevant subquotients, and let $\lambda : \mathcal{C} \to \mathbb{Z}$ be an **additive** function: $\lambda(M) = \lambda(M')$ whenever $M \cong M'$, and for every short exact sequence $0 \to M' \to M \to M'' \to 0$ of modules in $\mathcal{C}$,
$$\lambda(M) = \lambda(M') + \lambda(M'').$$
(The length $\ell(\cdot)$ on finite-length modules is the prototype.) Prove that for any exact sequence of modules in $\mathcal{C}$
$$0 \longrightarrow M_0 \longrightarrow M_1 \longrightarrow \cdots \longrightarrow M_n \longrightarrow 0,$$
the **alternating sum** vanishes:
$$\sum_{i=0}^{n} (-1)^i \lambda(M_i) = 0.$$

(This is Example Sheet 1 Question 12 / Example Sheet 2 Question 1(c). Specialising $\lambda = \ell$ gives additivity of composition length; specialising $\lambda = \dim_k$ over a field gives the alternating-sum form of rank–nullity.)

**Recall:**

![[Def - Exact Sequence and Short Exact Sequence#The Definition]]

A sequence is [[Def - Exact Sequence and Short Exact Sequence|exact]] if image equals kernel at each internal spot. The function $\lambda$ being **additive** means it adds across short exact sequences; the prototype is the [[Def - Composition Series and Length|length]] $\ell$, which is additive by [[Thm - Length is Additive and Finite iff Noetherian and Artinian|the additivity theorem]]. The task is to lift additivity from the three-term (short exact) case to an arbitrary finite exact sequence, with the signs $(-1)^i$ appearing exactly to make the intermediate contributions cancel.

---

# Convergent Strategy

**Problem class.** This is a *telescoping / Euler-characteristic* problem from [[Commutative Algebra I — Chain Conditions#Problem-Solving Strategy|the chapter's length-computation family]]. The target is an identity, and the strategy is structural: chop the long exact sequence into short exact pieces, apply the known three-term additivity to each, and sum with signs so the shared terms cancel. This is the universal mechanism by which any additive invariant produces an Euler characteristic.

**Assumption pattern.** The exploitable structure is that a long exact sequence is *built from* short exact sequences via its images. The recognisable trigger is "additive on short exact sequences, want a statement about a long one": the only tool is additivity, so the long sequence must be decomposed into three-term pieces. The images $Z_i = \operatorname{im}(M_{i-1} \to M_i) = \ker(M_i \to M_{i+1})$ are the cutting points — exactness is precisely what makes image equal kernel, so each $M_i$ sits in a short exact sequence $0 \to Z_i \to M_i \to Z_{i+1} \to 0$.

**Theorem routing.** The route is: (1) define $Z_i = \ker(M_i \to M_{i+1})$, with $Z_0 = 0$ and $Z_{n+1} = 0$ from exactness at the ends; (2) exactness gives short exact sequences $0 \to Z_i \to M_i \to Z_{i+1} \to 0$ for each $i$; (3) apply additivity to get $\lambda(M_i) = \lambda(Z_i) + \lambda(Z_{i+1})$; (4) form $\sum_i (-1)^i \lambda(M_i)$ and observe each $\lambda(Z_j)$ appears twice with opposite signs, cancelling, with boundary terms zero. The key tool is the three-term additivity, applied $n+1$ times.

**Key decision point.** The non-obvious move is introducing the **images $Z_i$** as the splice points and recognising that exactness makes $0 \to Z_i \to M_i \to Z_{i+1} \to 0$ short exact. Without this, one is stuck staring at a long sequence with no three-term pieces to feed additivity. The signs $(-1)^i$ are then *forced*: each $Z_j$ enters once from the $i = j$ short exact sequence (as the kernel, with sign $(-1)^j$) and once from the $i = j-1$ sequence (as the cokernel, with sign $(-1)^{j-1}$), so the alternating signs are exactly what cancels them. The decision is to let the images do the cutting; the signs come along for free.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra I — Chain Conditions#Legal Operations|the topic page's Legal Operations]]:

1. **Operation 1 (build short exact sequences), at each image.** Cut the long exact sequence at every spot using the image $Z_i = \ker(M_i \to M_{i+1})$, producing short exact sequences $0 \to Z_i \to M_i \to Z_{i+1} \to 0$.

2. **Operation 9 (add the invariant across each short exact sequence).** Apply additivity of $\lambda$ to each three-term piece: $\lambda(M_i) = \lambda(Z_i) + \lambda(Z_{i+1})$.

3. **Telescoping with signs.** Form the alternating sum and cancel each $\lambda(Z_j)$ against its oppositely-signed twin, using $Z_0 = Z_{n+1} = 0$ at the boundary.

---

# Hints

> [!note]- Hint 1
> You only know that $\lambda$ adds across *short* (three-term) exact sequences, but you are handed a *long* one. The whole game is to break the long exact sequence into short exact pieces. What natural submodules of each $M_i$ let you do this?

> [!note]- Hint 2
> Set $Z_i = \operatorname{im}(M_{i-1} \to M_i) = \ker(M_i \to M_{i+1})$ (these are equal by exactness). By convention $Z_0 = 0$ and $Z_{n+1} = 0$ (exactness at the ends). Then for each $i$, the sequence $0 \to Z_i \to M_i \to Z_{i+1} \to 0$ is short exact — check it.

> [!note]- Hint 3
> Additivity gives $\lambda(M_i) = \lambda(Z_i) + \lambda(Z_{i+1})$ for each $i$. Substitute into $\sum_i (-1)^i \lambda(M_i)$ and watch each $\lambda(Z_j)$ appear twice — from the $i = j$ term and the $i = j-1$ term — with opposite signs.

---

# Solution

The proof decomposes the long exact sequence into short exact pieces via its images, applies the given three-term additivity to each, and telescopes the alternating sum. The non-obvious move is introducing the images $Z_i$ as splice points; the signs then force the cancellation.

**Step 1: Cut the long exact sequence into short exact sequences at the images.**

> [!note]- Derivation
> Write the maps as $M_{i-1} \xrightarrow{d_{i-1}} M_i \xrightarrow{d_i} M_{i+1}$, and set
> $$Z_i = \operatorname{im}(d_{i-1}) = \ker(d_i) \subseteq M_i,$$
> the two being equal by exactness at $M_i$. By exactness at the left end ($0 \to M_0 \to M_1$), the map $d_0$ is injective, so $Z_0 = \ker(d_0) = 0$; by exactness at the right end ($M_{n-1} \to M_n \to 0$), the map $M_n \to 0$ has kernel all of $M_n$, and $Z_{n+1} := 0$. Now for each $0 \leq i \leq n$ consider
> $$0 \longrightarrow Z_i \xrightarrow{\ \subseteq\ } M_i \xrightarrow{\ d_i\ } Z_{i+1} \longrightarrow 0.$$
> This is exact: the inclusion $Z_i = \ker d_i \hookrightarrow M_i$ is injective; the corestriction $d_i : M_i \to \operatorname{im}(d_i) = Z_{i+1}$ is surjective; and $\ker(d_i) = Z_i = \operatorname{im}(\text{inclusion})$. So it is a short exact sequence.

**Step 2: Apply additivity to each short exact sequence.**

> [!note]- Derivation
> Since $\lambda$ is additive, applying it to $0 \to Z_i \to M_i \to Z_{i+1} \to 0$ gives, for every $0 \leq i \leq n$,
> $$\lambda(M_i) = \lambda(Z_i) + \lambda(Z_{i+1}).$$

**Step 3: Telescope the alternating sum.**

> [!note]- Derivation
> Substitute Step 2 into the alternating sum:
> $$\sum_{i=0}^{n} (-1)^i \lambda(M_i) = \sum_{i=0}^{n} (-1)^i \big(\lambda(Z_i) + \lambda(Z_{i+1})\big) = \sum_{i=0}^{n} (-1)^i \lambda(Z_i) + \sum_{i=0}^{n} (-1)^i \lambda(Z_{i+1}).$$
> Re-index the second sum by $j = i+1$ (so $i = j-1$, $(-1)^i = (-1)^{j-1} = -(-1)^j$), giving $\sum_{j=1}^{n+1} -(-1)^{j} \lambda(Z_{j})$. Adding to the first sum:
> $$\sum_{i=0}^{n} (-1)^i \lambda(Z_i) - \sum_{j=1}^{n+1} (-1)^{j} \lambda(Z_{j}).$$
> The two sums agree term-by-term for $1 \leq i \leq n$ and cancel there. The leftover terms are $(-1)^0 \lambda(Z_0)$ from the first sum and $-(-1)^{n+1}\lambda(Z_{n+1})$ from the second. But $Z_0 = 0$ and $Z_{n+1} = 0$, so $\lambda(Z_0) = \lambda(Z_{n+1}) = 0$ (additivity applied to $0 \to 0 \to 0 \to 0 \to 0$ gives $\lambda(0) = 0$). Hence
> $$\sum_{i=0}^{n} (-1)^i \lambda(M_i) = 0.$$

> [!note]- Complete formal solution
> **Claim.** For an exact sequence $0 \to M_0 \to \cdots \to M_n \to 0$ in $\mathcal{C}$ and additive $\lambda$, $\sum_{i=0}^n (-1)^i \lambda(M_i) = 0$.
>
> Let $Z_i = \ker(M_i \to M_{i+1}) = \operatorname{im}(M_{i-1} \to M_i)$, with $Z_0 = Z_{n+1} = 0$ by exactness at the ends. Exactness gives short exact sequences $0 \to Z_i \to M_i \to Z_{i+1} \to 0$, so additivity yields $\lambda(M_i) = \lambda(Z_i) + \lambda(Z_{i+1})$. Then
> $$\sum_{i=0}^n (-1)^i \lambda(M_i) = \sum_{i=0}^n (-1)^i\lambda(Z_i) + \sum_{i=0}^n (-1)^i \lambda(Z_{i+1}) = \lambda(Z_0) - (-1)^{n+1}\lambda(Z_{n+1}) = 0,$$
> the middle terms cancelling and the boundary terms vanishing since $Z_0 = Z_{n+1} = 0$. $\blacksquare$

---

# Key Takeaways

**Any invariant additive on short exact sequences extends to an Euler characteristic on long ones — cut at the images and telescope.** This is the master template for Euler-characteristic identities, and length is just one instance. The reusable procedure: given a long exact sequence and an additive invariant, define the images $Z_i = \ker(d_i)$, form the short exact sequences $0 \to Z_i \to M_i \to Z_{i+1} \to 0$, apply additivity, and sum with alternating signs so the $\lambda(Z_i)$ cancel pairwise. The trigger is "additive on short exact, asked about long exact"; the response is always "splice at the images". This exact argument, with $\lambda$ replaced by $\dim_k$, proves the alternating sum of dimensions in a complex of vector spaces vanishes; with $\lambda$ replaced by the rank of homology, it proves the Euler characteristic is computable from any chain complex.

**The alternating signs are not decoration — they are forced by each image appearing as both a kernel and a cokernel.** Every intermediate module $Z_j$ enters the computation twice: once as the *sub* (kernel) in the sequence $0 \to Z_j \to M_j \to Z_{j+1} \to 0$ and once as the *quotient* (cokernel) in $0 \to Z_{j-1} \to M_{j-1} \to Z_j \to 0$. These two appearances carry consecutive indices $j$ and $j-1$, so with alternating signs they cancel exactly. The general lesson: whenever an object is simultaneously a kernel of one map and an image of the previous one — which is precisely what *exactness* asserts — an alternating sum will telescope through it. This is why Euler characteristics are *signed* counts, and why the signs are tied to homological degree.

**Specialising $\lambda$ recovers familiar identities, which is the fastest sanity check.** Setting $\lambda = \ell$ (length) recovers [[Thm - Length is Additive and Finite iff Noetherian and Artinian|additivity of composition length]]; setting $\lambda = \dim_k$ over a field and $n = 2$ recovers rank–nullity ($\dim M_1 = \dim M_0 + \dim M_2$ for $0 \to M_0 \to M_1 \to M_2 \to 0$); setting $\lambda = \dim_k$ for a general $n$ recovers "the alternating sum of dimensions in an exact complex is zero". When you derive a general additivity statement, immediately test it on the length and dimension specialisations — if it does not reduce to rank–nullity in the three-term vector-space case, the general statement is wrong. This habit of checking the degenerate cases is the cheapest way to catch sign errors and off-by-one mistakes in Euler-characteristic computations.
