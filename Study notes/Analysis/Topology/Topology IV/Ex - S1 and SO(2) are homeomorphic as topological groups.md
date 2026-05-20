---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Topological Group"
  - "Def - Topological Subgroup, Homomorphism, Action"
  - "Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism"
tags: [analysis, topology, topological-group]
---

# Problem Statement

Show that $S^1 = \{z \in \mathbb{C} : |z| = 1\}$ (with multiplication of complex numbers) and $\operatorname{SO}(2) = \{R(\theta) : \theta \in \mathbb{R}\}$ (with matrix multiplication, where $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$) are isomorphic as topological groups.

**Recall:**

A [[Def - Topological Group|topological group]] isomorphism is a continuous bijective group homomorphism with continuous inverse. $S^1$ is the unit circle as a topological group under complex multiplication; $\operatorname{SO}(2)$ is the special orthogonal group in dimension 2, consisting of all $2 \times 2$ rotations.

A [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism|continuous bijection from a compact space to a Hausdorff space]] is automatically a homeomorphism. Combined with the group-homomorphism property, this gives a topological group isomorphism.

---

# Convergent Strategy

**Problem class:** Construct an isomorphism between two compact abelian topological groups by exhibiting an explicit homomorphism.

**Assumption pattern:** Both $S^1$ and $\operatorname{SO}(2)$ are parametrized by an angle $\theta \in \mathbb{R}/2\pi\mathbb{Z}$. The natural map $\theta \mapsto R(\theta)$ from $\mathbb{R}$ to $\operatorname{SO}(2)$ is a continuous homomorphism with kernel $2\pi\mathbb{Z}$.

**Theorem routing:** Define $\varphi : S^1 \to \operatorname{SO}(2)$ by $\varphi(e^{i\theta}) = R(\theta)$. Verify: (i) well-defined, (ii) continuous, (iii) group homomorphism, (iv) bijective. Then apply the compact-to-Hausdorff upgrade.

**Key decision point:** Identifying $S^1$ with $\mathbb{R}/2\pi\mathbb{Z}$ (additively) and $\operatorname{SO}(2)$ with $\mathbb{R}/2\pi\mathbb{Z}$ (via $\theta \mapsto R(\theta)$). The "double identification" makes the isomorphism transparent.

---

# Legal Operations Used

1. **Construct an explicit map.** The angle parametrization gives a continuous group homomorphism $\mathbb{R} \to S^1$ and $\mathbb{R} \to \operatorname{SO}(2)$.

2. **Verify group homomorphism.** The angle addition formula $R(\theta_1 + \theta_2) = R(\theta_1) R(\theta_2)$ matches the complex multiplication $e^{i\theta_1} e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$.

3. **Upgrade to homeomorphism.** Continuous bijection, $S^1$ compact, $\operatorname{SO}(2)$ Hausdorff.

---

# Hints

> [!note]- Hint 1
> Define $\varphi : S^1 \to \operatorname{SO}(2)$ by $\varphi(e^{i\theta}) = R(\theta)$ where $R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

> [!note]- Hint 2
> Well-defined: $e^{i\theta_1} = e^{i\theta_2}$ iff $\theta_1 - \theta_2 \in 2\pi\mathbb{Z}$, and $R(\theta_1) = R(\theta_2)$ iff $\theta_1 - \theta_2 \in 2\pi\mathbb{Z}$ too (the rotation depends only on angle mod $2\pi$). So $\varphi$ is well-defined.

> [!note]- Hint 3
> Homomorphism: $\varphi(e^{i\theta_1} \cdot e^{i\theta_2}) = \varphi(e^{i(\theta_1 + \theta_2)}) = R(\theta_1 + \theta_2) = R(\theta_1) R(\theta_2) = \varphi(e^{i\theta_1}) \varphi(e^{i\theta_2})$. The first equality uses the multiplicativity of $e^{i\theta}$; the last uses the angle-addition formula for rotation matrices.

> [!note]- Hint 4
> Continuity: $\varphi$ is continuous as a function of the angle parameter $\theta$. Bijection: distinct $e^{i\theta}$ give distinct rotations (since both depend only on $\theta \mod 2\pi$). Apply compact-Hausdorff upgrade.

---

# Solution

The proof breaks into six steps that build $\varphi: S^1 \to \operatorname{SO}(2)$, $e^{i\theta} \mapsto R(\theta)$, and verify it is a topological-group isomorphism. Step 1 defines $\varphi$; Step 2 checks well-definedness (both sides depend only on $\theta \mod 2\pi$); Step 3 verifies the group-homomorphism property via the angle-addition formula $R(\theta_1+\theta_2) = R(\theta_1)R(\theta_2)$; Step 4 checks continuity using the explicit formula $\varphi(z) = \begin{pmatrix} \operatorname{Re}(z) & -\operatorname{Im}(z) \\ \operatorname{Im}(z) & \operatorname{Re}(z) \end{pmatrix}$; Step 5 verifies bijectivity; Step 6 invokes compact-to-Hausdorff to upgrade to a homeomorphism. The non-obvious move is in Step 6 — the compact-to-Hausdorff lemma saves the explicit construction of $\varphi^{-1}$, which would require continuous extraction of the angle from a rotation matrix.

**Step 1: Define $\varphi$.**

$\varphi : S^1 \to \operatorname{SO}(2)$, $\varphi(e^{i\theta}) := R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

**Step 2: Verify well-definedness.**

> [!note]- Derivation
> If $e^{i\theta_1} = e^{i\theta_2}$, then $\theta_1 - \theta_2 \in 2\pi\mathbb{Z}$, so $\cos\theta_1 = \cos\theta_2$ and $\sin\theta_1 = \sin\theta_2$. Hence $R(\theta_1) = R(\theta_2)$, and $\varphi$ is well-defined.

**Step 3: Verify $\varphi$ is a group homomorphism.**

> [!note]- Derivation
> $\varphi(e^{i\theta_1} \cdot e^{i\theta_2}) = \varphi(e^{i(\theta_1+\theta_2)}) = R(\theta_1 + \theta_2)$.
>
> By the angle-addition formula:
> $$R(\theta_1 + \theta_2) = \begin{pmatrix} \cos(\theta_1+\theta_2) & -\sin(\theta_1+\theta_2) \\ \sin(\theta_1+\theta_2) & \cos(\theta_1+\theta_2) \end{pmatrix}$$
> $$= \begin{pmatrix} \cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2 & -\cos\theta_1\sin\theta_2 - \sin\theta_1\cos\theta_2 \\ \sin\theta_1\cos\theta_2 + \cos\theta_1\sin\theta_2 & \cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2 \end{pmatrix}$$
> $$= R(\theta_1) R(\theta_2).$$
> So $\varphi(z_1 z_2) = \varphi(z_1) \varphi(z_2)$.
>
> Also: $\varphi(1) = R(0) = I$ (identity).

**Step 4: Verify $\varphi$ is continuous.**

> [!note]- Derivation
> Parametrize $S^1$ by the angle $\theta$ (modulo $2\pi$). The map $\theta \mapsto (\cos\theta, \sin\theta)$ from $\mathbb{R}$ to $S^1$ is continuous, and the map $\theta \mapsto R(\theta)$ from $\mathbb{R}$ to $M_2(\mathbb{R})$ is continuous (matrix entries are sines and cosines of $\theta$). Both descend to continuous maps $S^1 \to S^1$ and $S^1 \to \operatorname{SO}(2)$. The composition is $\varphi : S^1 \to \operatorname{SO}(2)$, continuous.
>
> More directly: $\varphi(z) = \begin{pmatrix} \operatorname{Re}(z) & -\operatorname{Im}(z) \\ \operatorname{Im}(z) & \operatorname{Re}(z) \end{pmatrix}$, where each entry is a continuous function of $z \in S^1$.

**Step 5: Verify $\varphi$ is a bijection.**

> [!note]- Derivation
> *Injective.* If $\varphi(e^{i\theta_1}) = \varphi(e^{i\theta_2})$, then $R(\theta_1) = R(\theta_2)$, so $\cos\theta_1 = \cos\theta_2$ and $\sin\theta_1 = \sin\theta_2$. Hence $\theta_1 - \theta_2 \in 2\pi\mathbb{Z}$, so $e^{i\theta_1} = e^{i\theta_2}$.
>
> *Surjective.* Every $A \in \operatorname{SO}(2)$ has the form $R(\theta)$ for some $\theta \in \mathbb{R}$. (Proof: $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $AA^T = I$ gives $a^2 + b^2 = 1$, $c^2 + d^2 = 1$, $ac + bd = 0$. With $\det A = 1$: $ad - bc = 1$. Setting $a = \cos\theta, c = \sin\theta$ gives $b = -\sin\theta, d = \cos\theta$. So $A = R(\theta)$.) Hence $A = \varphi(e^{i\theta})$.

**Step 6: Upgrade to homeomorphism via compact-Hausdorff.**

> [!note]- Derivation
> $S^1$ is compact (closed bounded subset of $\mathbb{C} = \mathbb{R}^2$). $\operatorname{SO}(2)$ is Hausdorff (subspace of $M_2(\mathbb{R}) = \mathbb{R}^4$).
>
> By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $\varphi$ is a homeomorphism. Combined with the group homomorphism property (Step 3), $\varphi$ is an isomorphism of topological groups.

> [!note]- Complete formal solution
> Define $\varphi : S^1 \to \operatorname{SO}(2)$ by
> $$\varphi(e^{i\theta}) := \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
> $\varphi$ is well-defined (depends only on $\theta \mod 2\pi$), continuous (matrix entries are continuous functions of $z = e^{i\theta}$, namely real and imaginary parts), a group homomorphism (angle-addition formula), bijective ($S^1$ and $\operatorname{SO}(2)$ both parametrized by $\theta \in \mathbb{R}/2\pi\mathbb{Z}$ via these formulas).
>
> $S^1$ is compact and $\operatorname{SO}(2)$ is Hausdorff. By [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]], $\varphi$ is a homeomorphism. Combined with being a group homomorphism, $\varphi$ is an isomorphism of topological groups. $\blacksquare$

---

# Key Takeaways

**Angle parametrization unifies $S^1$ and $\operatorname{SO}(2)$.** Both groups are parametrized by an angle $\theta \in \mathbb{R}/2\pi\mathbb{Z}$, with addition of angles corresponding to multiplication in each group (multiplication of complex numbers and composition of rotations). This is the prototype example of the universal cover: $\mathbb{R} \to \mathbb{R}/2\pi\mathbb{Z}$ is the universal cover of $S^1$, and the same map covers $\operatorname{SO}(2)$.

**Compact-Hausdorff bijection upgrade saves work.** Once you have a continuous group homomorphism between two compact Hausdorff groups that is bijective, the inverse is automatically continuous — saving you from constructing the inverse explicitly. Without this lemma, one would need to verify continuity of $\varphi^{-1} : \operatorname{SO}(2) \to S^1$ separately, which requires extracting $\theta$ from the matrix continuously (e.g., $\theta = \operatorname{atan2}(\sin\theta, \cos\theta)$).

**Generalizes to $\operatorname{SU}(2) \cong S^3$ and $\operatorname{Sp}(1) \cong S^3$.** Similar isomorphisms hold in higher dimensions:
- $\operatorname{SU}(2) \cong S^3$: the special unitary group is parametrized by unit quaternions.
- $\operatorname{Sp}(1) \cong S^3$: the unit quaternions are the symplectic group of dimension 1.

The pattern: a classical matrix Lie group is sometimes homeomorphic to a sphere because the angle parametrization extends to higher-dimensional sphere parametrizations.

**The dual perspective.** $S^1$ and $\operatorname{SO}(2)$ are both compact, abelian, 1-dimensional Lie groups. In fact, they are the *unique* connected compact 1-dimensional Lie group (up to isomorphism) — every such group is isomorphic to $S^1$. So the result here is forced by the classification: in any one-dimensional connected compact Lie group setting, you must be looking at $S^1$.
