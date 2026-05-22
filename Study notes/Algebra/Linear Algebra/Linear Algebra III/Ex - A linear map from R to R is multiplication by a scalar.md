---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Linear Map"
tags: [algebra, linear-algebra]
---

# Problem Statement

Show that every linear map $T : \mathbb{R} \to \mathbb{R}$ is of the form $T(x) = \lambda x$ for some $\lambda \in \mathbb{R}$. Identify $\lambda$ in terms of $T$.

**Recall:**

A [[Def - Linear Map|linear map]] $T : V \to W$ between $\mathbf{F}$-vector spaces is a function satisfying:

![[Def - Linear Map#The Definition]]

The vector space $\mathbb{R}$ over the field $\mathbb{R}$ has dimension $1$, with standard basis $\{1\}$ (the single real number $1$). Every element of $\mathbb{R}$ is uniquely $x \cdot 1$ for $x \in \mathbb{R}$.

---

# Convergent Strategy

**Problem class.** This is a *find the form of all linear maps between specified spaces* problem. The topic-page Problem-Solving Strategy identifies this as the "characterise $\mathcal{L}(V, W)$" task: given $V = W = \mathbb{R}$ (one-dimensional), describe every element of $\mathcal{L}(\mathbb{R}, \mathbb{R})$. The route is via the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]], which says a linear map is determined by its values on a basis.

**Assumption pattern.** The defining assumptions are minimal: $V = W = \mathbb{R}$, $T$ linear, no further structure. The non-trivial input is the *dimension*: $\dim \mathbb{R} = 1$ over $\mathbb{R}$ as a vector space, so a basis consists of a single non-zero vector. Choosing $1 \in \mathbb{R}$ as that basis vector, the value $T(1)$ determines $T$ entirely.

**Theorem routing.** The route is: $T$ linear $\Rightarrow$ by [[Thm - Linear Map Determined by Action on Basis|the linear-map lemma]], $T$ is determined by $T(1)$ $\Rightarrow$ for every $x \in \mathbb{R}$, $T(x) = T(x \cdot 1) = x \cdot T(1)$ by homogeneity $\Rightarrow$ setting $\lambda = T(1)$, $T(x) = \lambda x$.

**Key decision point.** The crucial recognition is that $\mathbb{R}$ is a *one-dimensional* vector space, so the action on a basis is the action on a single vector. Once $T(1)$ is named, homogeneity carries the value to every $x$. The "key decision" is in choosing $1$ as the basis vector — but any non-zero real would work, with the formula rescaled.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra III — §3A–D Linear Maps#Legal Operations|the topic page's Legal Operations]]:

1. **Specify a linear map by its action on a basis** (operation 1). This is the operation we exploit *in reverse*: instead of building a linear map with specified action, we recognise that $T$ — given to us as linear — must be a particular kind of map once its action on $1$ is known. The trigger is "linear map from a one-dimensional space".

2. **Compute the null space and range by reduction to coordinates** (operation 2), in degenerate form. With only one basis vector, the "matrix" is the $1$-by-$1$ matrix $(\lambda)$, and the formula $T(x) = \lambda x$ is matrix-vector multiplication in this trivial case.

---

# Hints

> [!note]- Hint 1
> $\mathbb{R}$ is a one-dimensional vector space over $\mathbb{R}$. What is the dimension of $\mathcal{L}(\mathbb{R}, \mathbb{R})$, and what does that tell you about how many "kinds" of linear maps exist?

> [!note]- Hint 2
> Every $x \in \mathbb{R}$ can be written as $x = x \cdot 1$. Apply $T$ and use homogeneity. The answer $T(x)$ should be expressible in terms of one specific value of $T$.

> [!note]- Hint 3
> Set $\lambda := T(1)$. Then $T(x) = T(x \cdot 1) = x \cdot T(1) = \lambda x$.

---

# Solution

The strategy is one line. Use homogeneity of $T$ with scalar $x \in \mathbb{R}$ and vector $1 \in \mathbb{R}$: $T(x) = T(x \cdot 1) = x \cdot T(1)$. So $T(x) = \lambda x$ for $\lambda = T(1)$.

**Step 1: Every $x \in \mathbb{R}$ equals $x \cdot 1$.**

This is the trivial vector-space fact that $\mathbb{R}$ is one-dimensional over $\mathbb{R}$, with basis $\{1\}$.

> [!note]- Derivation
> $\mathbb{R}$, as a vector space over the field $\mathbb{R}$, has $1$ as a basis vector: every real number $x$ is uniquely a scalar multiple of $1$, namely $x = x \cdot 1$. Hence $\dim_\mathbb{R}(\mathbb{R}) = 1$, and the basis $\{1\}$ realises this. (Equivalently: the set $\{1\}$ is linearly independent in $\mathbb{R}$, and spans $\mathbb{R}$ via $x = x \cdot 1$.)

**Step 2: Define $\lambda := T(1)$ and apply homogeneity.**

By the homogeneity axiom of [[Def - Linear Map|linearity]], $T(x \cdot 1) = x \cdot T(1)$ for every $x \in \mathbb{R}$.

> [!note]- Derivation
> The homogeneity axiom of a linear map says $T(\lambda v) = \lambda T(v)$ for $\lambda \in \mathbf{F}$ and $v \in V$. Here $V = \mathbb{R}$, $\mathbf{F} = \mathbb{R}$. Take $v = 1$ and $\lambda = x$: $T(x \cdot 1) = x \cdot T(1)$. Setting $\lambda := T(1)$ (a fixed real number determined by $T$), we get $T(x \cdot 1) = x \cdot \lambda = \lambda x$.

**Step 3: Conclude $T(x) = \lambda x$ for $\lambda = T(1)$.**

Since $x = x \cdot 1$ for every $x \in \mathbb{R}$,
$$T(x) = T(x \cdot 1) = x \cdot T(1) = \lambda x.$$

> [!note]- Derivation
> Combining Steps 1 and 2: for any $x \in \mathbb{R}$, $T(x) = T(x \cdot 1) = x \cdot T(1) = \lambda x$, where $\lambda = T(1)$. This holds for every $x$, so $T$ is the multiplication-by-$\lambda$ map.

> [!note]- Complete formal solution
> Let $T : \mathbb{R} \to \mathbb{R}$ be linear. Define $\lambda := T(1) \in \mathbb{R}$.
>
> For any $x \in \mathbb{R}$, by the homogeneity axiom of a [[Def - Linear Map|linear map]],
> $$T(x) = T(x \cdot 1) = x \cdot T(1) = \lambda x.$$
> Hence $T$ is the multiplication-by-$\lambda$ map for $\lambda = T(1)$. $\blacksquare$

---

# Key Takeaways

**A linear map from a one-dimensional space is a scalar multiplication.** This is the simplest case of the [[Thm - Linear Map Determined by Action on Basis|linear-map lemma]]: a linear map is determined by its values on a basis, and a one-dimensional space has a one-element basis, so the data is one vector in the codomain — equivalently, one scalar if the codomain is also one-dimensional. The reusable principle is that "linear maps between one-dimensional spaces are scalars", and this is what underlies the identification of a linear functional on $V$ with its value on a fixed basis vector, and of operators on a one-dimensional invariant subspace with their eigenvalue restricted to that subspace. The trigger is any one-dimensional space appearing in the problem; the move is to identify the linear map with a scalar.

**The matrix of a one-dimensional linear map is a $1$-by-$1$ matrix.** This is the trivial case of the matrix representation. With basis $\{1\}$ on both sides, the matrix of $T$ is $(\lambda) \in \mathbf{F}^{1, 1}$. The vector $x$ has coordinate column $(x) \in \mathbf{F}^{1, 1}$. The matrix-vector product $(\lambda)(x) = (\lambda x)$ is the coordinate column of $Tx = \lambda x$. So the entire matrix machinery — at the level of one-dimensional spaces — collapses to multiplication of scalars. The reusable principle is that small special cases of general theory are worth working out explicitly, because they make the general structure visible without computational distraction.

**Dimension counting gives $\dim \mathcal{L}(\mathbb{R}, \mathbb{R}) = 1$.** The result of this exercise is that $\mathcal{L}(\mathbb{R}, \mathbb{R}) \cong \mathbb{R}$ — every linear map is determined by a single scalar. Dimension-counting: $\dim \mathcal{L}(V, W) = (\dim V)(\dim W) = 1 \cdot 1 = 1$, by [[Ex - The space of linear maps has dimension mn|the $mn$ theorem]]. This is the smallest non-trivial confirmation of the dimension formula, and it generalises: $\dim \mathcal{L}(\mathbb{R}^n, \mathbb{R}^m) = mn$, so the space of $n$-input-$m$-output linear maps is itself an $mn$-dimensional space. Every map is "$mn$ scalars", arranged as a matrix.

---
