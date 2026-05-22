---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Polar Decomposition"
  - "Def - Positive Operator"
  - "Def - Unitary Operator"
  - "Thm - Positive Operators Have a Unique Square Root"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional complex inner product space and $T \in \mathcal{L}(V)$ an invertible operator. Show that:

(a) The polar decomposition $T = SR$ with $S$ unitary and $R$ positive has both factors uniquely determined.

(b) If $T$ is not invertible, the factor $R$ is still unique, but $S$ has freedom on the kernel of $T$.

**Recall:**

![[Thm - Polar Decomposition#Statement]]

A positive operator has a [[Thm - Positive Operators Have a Unique Square Root|unique positive square root]]; in particular, $|T| = \sqrt{T^* T}$ is uniquely determined by $T$.

A [[Def - Unitary Operator|unitary]] operator $S$ satisfies $S^* S = SS^* = I$, equivalently $S^{-1} = S^*$.

---

# Convergent Strategy

**Problem class.** This is a *uniqueness analysis* problem: identify exactly which factors of a decomposition are uniquely determined and which have gauge freedom. The class is: given a factorisation theorem with existence already proved, examine what hypotheses determine the factors uniquely.

**Assumption pattern.** The hypothesis is the polar decomposition $T = SR$ (with $S$ isometric/unitary and $R$ positive). The question is uniqueness, which decomposes into uniqueness of $R$ (always) and uniqueness of $S$ (when $T$ is invertible).

**Theorem routing.** The route exploits the uniqueness of the positive square root. From $T^* T = R^* S^* S R = R^2$ (using $S^*S = I$ on the range of $R$, but we need it on all of $V$ — see the subtlety in the proof), $R = \sqrt{T^*T}$ uniquely. Once $R$ is fixed, $S$ is determined as $T R^{-1}$ when $R$ is invertible, i.e., when $T$ is invertible. When $T$ is not invertible, $R$ has a non-trivial kernel, and $S$ is not uniquely pinned down on this kernel.

**Key decision point.** The non-obvious move is recognising that **uniqueness of $S$ is tied to invertibility of $T$, not directly to anything about $S$**. The polar factor $R = |T|$ is always unique by the unique-square-root theorem. The isometric factor $S$ inherits the rest of the structure: when $T$ has trivial kernel (i.e., is invertible), $S$ is determined by $S R = T$ with $R$ invertible; when $T$ has a kernel, $S$ is determined on $\operatorname{range} R$ but free on $\operatorname{null} R$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VII — §7 Operators on Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Use uniqueness of the positive square root** — Apply [[Thm - Positive Operators Have a Unique Square Root]] to conclude $R = \sqrt{T^*T}$ is uniquely determined.

2. **Solve for an unknown factor algebraically when the other is known and invertible** — Once $R = |T|$ is fixed and invertible (when $T$ is invertible), $S = T R^{-1}$ is uniquely determined.

3. **Diagnose gauge freedom by examining the kernel** — When the equation $S \cdot 0 = 0$ does not constrain $S$ on a subspace, that subspace is the locus of gauge freedom.

---

# Hints

> [!note]- Hint 1
> The positive factor $R = |T| = \sqrt{T^*T}$ is unique by [[Thm - Positive Operators Have a Unique Square Root]]. Verify that $R$ is uniquely determined by computing $T^*T$ in terms of any polar decomposition $T = SR$.

> [!note]- Hint 2
> Once $R$ is fixed, the equation $T = SR$ for $S$ is solvable for $S$ when $R$ is invertible (which is equivalent to $T$ invertible). When $R$ is not invertible, $S$ is determined on $\operatorname{range} R$ but free on $\operatorname{null} R = \operatorname{null} T$.

> [!note]- Hint 3
> For the non-invertible case, construct two different unitary operators $S$ and $S'$ such that $S R = S' R = T$, by modifying their action on the kernel of $R$.

---

# Solution

The proof has two parts: uniqueness of $R$ (always), and uniqueness of $S$ (when $T$ is invertible).

**Step 1: $R = \sqrt{T^*T}$ is uniquely determined.**

Suppose $T = SR$ with $S$ unitary (or isometric) and $R$ positive. Compute $T^* T$:
$$T^* T = (SR)^* (SR) = R^* S^* S R = R^* I R = R^* R = R^2,$$
using $S^* S = I$ (isometry/unitary) and $R^* = R$ (positive operators are self-adjoint).

So $T^*T = R^2$, which uniquely determines $R$ as the [[Thm - Positive Operators Have a Unique Square Root|unique positive square root]] of $T^*T$. Hence $R = \sqrt{T^*T} = |T|$.

> [!note]- Derivation
> The expansion $T^*T = R^* S^* S R = R^* R = R^2$ uses two facts: $S^*S = I$ (this is the isometry condition), and $R^* = R$ (positive implies self-adjoint).
>
> If $S$ is only an isometry (not full unitary), $S^* S = I$ only on $\operatorname{range} S^*$, but the equation $S^* S R = R$ still holds because... wait, this requires care. Let us be careful: for $S$ an isometry $V \to V$ in finite dimensions, $S$ is automatically surjective and hence unitary by [[Thm - Characterization of Isometries]]. So $S^* S = I_V$ on the whole space, and the computation goes through.
>
> The uniqueness of $R$ follows from the [[Thm - Positive Operators Have a Unique Square Root]]: $R$ is a positive operator with $R^2 = T^*T$, and there is only one such operator.

**Step 2: When $T$ is invertible, $S$ is uniquely determined.**

If $T$ is invertible, then $T^* T$ is invertible (composition of invertibles), so $R = \sqrt{T^*T}$ is invertible (a positive operator is invertible iff its eigenvalues are all positive iff $0$ is not an eigenvalue, and the square root preserves this). Then from $T = SR$:
$$S = T R^{-1},$$
uniquely determined. Verify $S$ is unitary: $S^* S = R^{-1} T^* T R^{-1} = R^{-1} R^2 R^{-1} = I$, and $S$ is invertible (composition of invertibles), so $SS^* = I$ also. So $S$ is unitary.

> [!note]- Derivation
> Invertibility chain: $T$ invertible $\Leftrightarrow$ $T^* T$ invertible $\Leftrightarrow$ $R = \sqrt{T^*T}$ invertible. Each step uses that products and square roots preserve invertibility for positive operators.
>
> Given $R$ invertible, $T = SR$ gives $S = T R^{-1}$ in closed form, uniquely determined. The unitarity check $S^* S = R^{-1} T^* T R^{-1}$ uses $R$ self-adjoint so $(R^{-1})^* = R^{-1}$.

**Step 3: When $T$ is not invertible, $S$ has gauge freedom on $\operatorname{null} T$.**

If $T$ is not invertible, then $\operatorname{null} T \neq \{0\}$, and $R = |T|$ also has $\operatorname{null} R = \operatorname{null} T \neq \{0\}$ (since $\|Rv\| = \|Tv\|$). On $\operatorname{null} R$, the equation $SR \cdot v = T \cdot v = 0$ becomes $S \cdot 0 = 0$, which is satisfied by any $S$. So $S$ restricted to $\operatorname{null} R$ is free.

To make $S$ a full unitary on $V$, $S$ must map $\operatorname{null} R$ isometrically to some subspace of $V$. The natural choice is $S(\operatorname{null} R) = \operatorname{null} T^* = (\operatorname{range} T)^\perp$ (matching the dimensions, since $\dim \operatorname{null} T = \dim \operatorname{null} T^*$ in finite dimensions for any operator).

The polar decomposition $T = SR$ thus has $S$ determined on $\operatorname{range} R = (\operatorname{null} T)^\perp$ by $S(Rv) = Tv$, and *any* unitary extension to $\operatorname{null} R = \operatorname{null} T$ works. Different extensions give different polar decompositions of $T$.

> [!note]- Derivation
> $\operatorname{null} R = \operatorname{null} T$ by the calculation $\|Rv\|^2 = \langle R^2 v, v \rangle = \langle T^*T v, v \rangle = \|Tv\|^2$, so $Rv = 0$ iff $Tv = 0$.
>
> On $\operatorname{range} R = (\operatorname{null} R)^\perp = (\operatorname{null} T)^\perp$, define $S(Rv) = Tv$; this is well-defined by Lemma 2 of [[Thm - Polar Decomposition]] and isometric by Lemma 1.
>
> On $\operatorname{null} R = \operatorname{null} T$, $S$ is unconstrained by the equation $T = SR$. To make $S$ a unitary on $V$, choose any isometric isomorphism $\operatorname{null} T \to (\operatorname{range} T)^\perp = \operatorname{null} T^*$. The dimensions match since $\dim \operatorname{null} T = \dim \operatorname{null} T^*$ in finite dimensions.
>
> **Concrete example of non-uniqueness.** Take $T = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. Then $T^* T = T$, so $R = \sqrt{T} = T$ (since $T$ is already positive). For $S$: need $SR = T$, i.e., $S \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$. This forces the first column of $S$ to be $(1, 0)^t$; the second column is unconstrained (other than being a unit vector orthogonal to the first). So $S = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}$ for any $\theta$ — a one-parameter family of unitaries, each giving a valid polar decomposition.

> [!note]- Complete formal solution
> *(a) Uniqueness of $R$.* Given $T = SR$ with $S$ isometric and $R$ positive, $T^*T = R^* S^*S R = R^*R = R^2$. By [[Thm - Positive Operators Have a Unique Square Root]], $R = \sqrt{T^*T}$ is uniquely determined.
>
> *Uniqueness of $S$ when $T$ is invertible.* If $T$ is invertible, $R = \sqrt{T^*T}$ is invertible (positive with all eigenvalues positive). Then $S = T R^{-1}$ is uniquely determined. Verify $S$ is unitary: $S^* S = R^{-1} T^* T R^{-1} = R^{-1} R^2 R^{-1} = I$, and by finite-dimensional dimension count, also $S S^* = I$.
>
> *(b) Non-uniqueness when $T$ is not invertible.* If $T$ has $\operatorname{null} T \neq \{0\}$, then $\operatorname{null} R = \operatorname{null} T \neq \{0\}$. The equation $SR v = Tv$ determines $S$ on $\operatorname{range} R = (\operatorname{null} T)^\perp$ via $S(Rv) = Tv$, but does not constrain $S$ on $\operatorname{null} R$. To make $S$ a unitary on $V$, choose any isometric isomorphism $\operatorname{null} R \to (\operatorname{range} T)^\perp$ — different choices give different polar decompositions. Concrete example: for $T = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $R = T$ and $S$ is any unitary of the form $\operatorname{diag}(1, e^{i\theta})$ for $\theta \in \mathbb{R}$. $\blacksquare$

---

# Key Takeaways

**Uniqueness of polar decomposition factors mirrors uniqueness of the complex polar form.** The polar form $z = r e^{i\theta}$ of a complex number has $r = |z|$ uniquely determined (always) and $\theta$ determined modulo $2\pi$ when $z \neq 0$ (when $z = 0$, $\theta$ is undefined). The operator-theoretic polar decomposition $T = S |T|$ has $|T|$ uniquely determined (always, by the unique square root theorem) and $S$ uniquely determined when $T$ is invertible (the operator analogue of $z \neq 0$). When $T$ is non-invertible, $S$ has gauge freedom on $\operatorname{null} T$, the operator analogue of $\theta$ being undefined at $z = 0$. The two pictures are exact analogues.

**Invertibility is the condition that removes gauge freedom in many decompositions.** This phenomenon — uniqueness when invertible, gauge freedom otherwise — recurs throughout linear algebra. The Cholesky decomposition $T = R^* R$ is uniquely determined for positive definite $T$ but has gauge freedom for positive semidefinite $T$. The QR factorisation $A = QR$ is uniquely determined when $A$ has linearly independent columns but has gauge freedom otherwise. The pattern is: the decomposition's "rotational" factor is determined wherever the "stretching" factor is invertible, and free where the stretching factor is degenerate.

**The gauge freedom is precisely a unitary action on the kernel.** For a non-invertible $T$ with $k = \dim \operatorname{null} T$, the set of unitary $S$ giving valid polar decompositions $T = SR$ is parameterised by the unitary group $U(k)$, acting on $\operatorname{null} T \subseteq V$. This is a *concrete*, *computable* gauge group: not an abstract equivalence, but a literal $U(k)$ of choices. In quantum information theory, this gauge freedom underlies the freedom in choosing **Stinespring dilations** of a quantum channel — different choices of the dilation correspond to different choices of $S$ in the operator polar decomposition of the channel's representation. The uniqueness vs gauge phenomenon is real-world, not just an artefact.
