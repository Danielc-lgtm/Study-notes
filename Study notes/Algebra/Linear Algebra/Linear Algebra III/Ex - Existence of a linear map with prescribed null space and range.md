---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
  - "Thm - Fundamental Theorem of Linear Maps"
  - "Thm - Linear Map Determined by Action on Basis"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional vector space, $W$ any vector space, $X \subseteq V$ a [[Def - Subspace|subspace]], and $Y \subseteq W$ a finite-dimensional subspace. Prove that there exists $T \in \mathcal{L}(V, W)$ with $\operatorname{null} T = X$ and $\operatorname{range} T = Y$ if and only if
$$\dim X + \dim Y = \dim V.$$

(This is Exercise 31 of LADR §3B.)

**Recall:**

![[Def - Null Space and Range#The Definition]]

![[Thm - Fundamental Theorem of Linear Maps#Statement]]

The [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] supplies the existence: given a basis of $V$ and chosen images, there is a unique linear map.

---

# Convergent Strategy

**Problem class.** This is a *if-and-only-if existence* problem: characterise when a linear map with prescribed kernel and range exists. The topic-page Problem-Solving Strategy categorises it under "build maps with prescribed properties" plus "dimensional obstructions via rank–nullity": the necessary condition is dimensional, and the sufficient direction is constructive via the linear-map lemma.

**Assumption pattern.** $V$ finite-dimensional, $X \subseteq V$, $Y \subseteq W$ with $Y$ finite-dimensional. The defining feature: rank–nullity gives a necessary dimensional condition ("$\Rightarrow$"); the linear-map lemma gives a constructive sufficient condition ("$\Leftarrow$").

**Theorem routing.** Two routes, one for each direction.

- ($\Rightarrow$) If $T$ exists with $\operatorname{null} T = X$ and $\operatorname{range} T = Y$, then by [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]], $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T = \dim X + \dim Y$. So the dimensional condition is necessary.
- ($\Leftarrow$) Given $\dim X + \dim Y = \dim V$, construct $T$ via the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]]. Take a basis $x_1, \ldots, x_k$ of $X$, extend to a basis $x_1, \ldots, x_k, v_1, \ldots, v_m$ of $V$ (so $k + m = \dim V$, hence $m = \dim Y$). Take a basis $y_1, \ldots, y_m$ of $Y$. Define $T$ by $T(x_i) = 0$ for all $i$ and $T(v_j) = y_j$ for all $j$.

**Key decision point.** The crucial recognition is to choose a basis of $V$ that is *adapted* to $X$ — i.e., a basis whose first $\dim X$ vectors are a basis of $X$. This makes the construction of $T$ transparent: send the $X$-basis to zero, send the extension to a basis of $Y$. The "key decision" is also in choosing the *target* of the extension vectors $v_j$: pick a basis of $Y$ (not arbitrary vectors of $W$) to ensure $\operatorname{range} T = Y$ exactly.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Specify a linear map by its action on a basis** (operation 1). The entire construction is one application of the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] with a basis of $V$ adapted to $X$.

2. **Apply rank–nullity to convert one [[Def - Dimension|dimension]] into another** (operation 3). Used for the necessity direction.

3. **Decompose a domain via $V = \operatorname{null} T \oplus U$** (operation 9). The basis-extension construction implicitly produces a complement of $X$ in $V$ — the span of the extension vectors.

---

# Hints

> [!note]- Hint 1
> ($\Rightarrow$) is one line of rank–nullity. ($\Leftarrow$) is constructive: build $T$ by specifying its values on a basis of $V$.

> [!note]- Hint 2
> For the construction: choose a basis of $X$, extend to a basis of $V$. Choose a basis of $Y$. Send the $X$-basis to zero, and the *extension vectors* to the $Y$-basis, in order.

> [!note]- Hint 3
> Verify the construction: the null space is exactly $X$ (by construction of the kernel from the $X$-basis), and the range is exactly $Y$ (because the extension vectors span $Y$ via $T$).

---

# Solution

The plan: ($\Rightarrow$) apply [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] to derive the necessary dimensional condition. ($\Leftarrow$) construct $T$ explicitly by specifying its values on a basis of $V$ adapted to $X$, using the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]] to guarantee well-definedness.

**Step 1: Necessity ($\Rightarrow$).**

If $T$ exists with $\operatorname{null} T = X$ and $\operatorname{range} T = Y$, then $\dim V = \dim X + \dim Y$ by rank–nullity.

> [!note]- Derivation
> By [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] applied to $T \in \mathcal{L}(V, W)$ with $V$ finite-dimensional:
> $$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T.$$
> Substituting $\operatorname{null} T = X$ and $\operatorname{range} T = Y$:
> $$\dim V = \dim X + \dim Y.$$
> This is the necessary condition.

**Step 2: Sufficiency ($\Leftarrow$), construction.**

Given $\dim X + \dim Y = \dim V$, construct $T$.

> [!note]- Derivation
> Choose a basis $x_1, \ldots, x_k$ of $X$, where $k = \dim X$. By the basis-extension lemma, extend to a basis $x_1, \ldots, x_k, v_1, \ldots, v_m$ of $V$, with $k + m = \dim V$. The dimensional condition gives $m = \dim V - k = \dim Y$.
>
> Choose a basis $y_1, \ldots, y_m$ of $Y$, where $m = \dim Y$.
>
> By the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]], there exists a unique linear map $T : V \to W$ defined on the basis by
> $$T(x_i) = 0 \quad \text{for } i = 1, \ldots, k,$$
> $$T(v_j) = y_j \quad \text{for } j = 1, \ldots, m.$$

**Step 3: Sufficiency ($\Leftarrow$), verification.**

Check that the constructed $T$ has $\operatorname{null} T = X$ and $\operatorname{range} T = Y$.

> [!note]- Derivation
> **$\operatorname{null} T = X$.** Clearly $X \subseteq \operatorname{null} T$, since $T$ kills each $x_i$ and hence (by linearity) every element of $\operatorname{span}(x_1, \ldots, x_k) = X$.
>
> Conversely, suppose $v \in \operatorname{null} T$. Expand $v$ in the basis: $v = \sum a_i x_i + \sum b_j v_j$. Apply $T$:
> $$0 = T v = \sum a_i T x_i + \sum b_j T v_j = 0 + \sum b_j y_j.$$
> Linear independence of the $y_j$ forces $b_j = 0$ for all $j$. So $v = \sum a_i x_i \in X$. Hence $\operatorname{null} T \subseteq X$.
>
> Combining the inclusions: $\operatorname{null} T = X$.
>
> **$\operatorname{range} T = Y$.** Clearly $\operatorname{range} T \subseteq Y$: every $Tv = T(\sum a_i x_i + \sum b_j v_j) = \sum b_j y_j \in Y$.
>
> Conversely, every $y \in Y$ is $\sum c_j y_j = T(\sum c_j v_j)$, so $y \in \operatorname{range} T$. Hence $Y \subseteq \operatorname{range} T$.
>
> Combining: $\operatorname{range} T = Y$.

> [!note]- Complete formal solution
> Let $V$ be finite-dimensional, $W$ any vector space, $X \subseteq V$ a subspace, $Y \subseteq W$ a finite-dimensional subspace.
>
> **($\Rightarrow$) Necessity.** Suppose $T \in \mathcal{L}(V, W)$ has $\operatorname{null} T = X$ and $\operatorname{range} T = Y$. By [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]],
> $$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T = \dim X + \dim Y.$$
>
> **($\Leftarrow$) Sufficiency.** Suppose $\dim X + \dim Y = \dim V$. Set $k := \dim X$ and $m := \dim Y$, so $k + m = \dim V$.
>
> Choose a basis $x_1, \ldots, x_k$ of $X$, extend to a basis $x_1, \ldots, x_k, v_1, \ldots, v_m$ of $V$. Choose a basis $y_1, \ldots, y_m$ of $Y$.
>
> By the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]], define $T \in \mathcal{L}(V, W)$ by
> $$T(x_i) = 0 \;\; (i = 1, \ldots, k), \qquad T(v_j) = y_j \;\; (j = 1, \ldots, m).$$
>
> Verify $\operatorname{null} T = X$: $X \subseteq \operatorname{null} T$ since $T(x_i) = 0$ for the basis of $X$. Conversely, if $v = \sum a_i x_i + \sum b_j v_j$ satisfies $T v = 0$, then $\sum b_j y_j = 0$, forcing $b_j = 0$ (linear independence of $y_j$), so $v = \sum a_i x_i \in X$.
>
> Verify $\operatorname{range} T = Y$: $\operatorname{range} T \subseteq Y$ since every $T v$ is a linear combination of $y_j \in Y$. Conversely, $y_j = T(v_j) \in \operatorname{range} T$, so the basis of $Y$ is in the range, hence $Y \subseteq \operatorname{range} T$.
>
> Thus $T$ has the required properties. $\blacksquare$

---

# Key Takeaways

**Dimensional conditions are exactly what rank–nullity enforces.** The "iff" structure of this exercise — a *dimensional* condition is both necessary and sufficient for a *qualitative* existence statement — is the canonical pattern of how [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]] is used. The necessary direction reads off the [[Def - Dimension|dimension]] equation; the sufficient direction *uses* the dimension equation as the only constraint, building the map via the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]]. The reusable principle: whenever a problem asks "does a linear map with property X exist", check whether X has a dimensional shadow, and use rank–nullity + the linear-map lemma to settle the question. The trigger is "existence of a map with kernel/range/rank/nullity of a specific kind".

**Basis adapted to a subspace is the standard construction trick.** Whenever you need to control what a linear map does on a specific subspace $X \subseteq V$, choose a basis of $X$ and *extend* to a basis of $V$. The extension vectors then represent the "complement" of $X$, and you have full control over what $T$ does on each. This is the same trick used in the proof of [[Thm - Fundamental Theorem of Linear Maps|rank–nullity]], and it is the construction-engine of essentially every existence proof in this chapter. The reusable principle: basis extension converts "control on a subspace" into "control everywhere". The trigger is any problem about linear maps with prescribed behaviour on a subspace.

**Constructions via the linear-map lemma are templated.** The lemma's pattern — "pick a basis of the domain, specify the images, extend by linearity" — is mechanical. The skill is in choosing the right basis and the right images. Here we chose a basis adapted to $X$ and images that span $Y$, but other constructions use bases adapted to other structures: an eigenbasis adapted to an operator, a basis adapted to an inner product (orthonormal), a basis adapted to a chain of invariant [[Def - Subspace|subspaces]] (giving an upper-triangular matrix). The reusable principle: for any "build a linear map with property P" problem, identify the right basis structure, and the construction follows. The trigger: "show there exists $T$ with [structural property]". See [[Thm - Linear Map Determined by Action on Basis]] for the underlying construction tool.

---
