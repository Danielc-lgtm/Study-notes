---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Self-Adjoint Operator"
  - "Def - Adjoint of a Linear Map"
  - "Def - Inner Product Space"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional inner product space over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$, and let $T \in \mathcal{L}(V)$ be a self-adjoint operator. Show that every eigenvalue of $T$ is real.

**Recall:**

![[Def - Self-Adjoint Operator#The Definition]]

An [[Def - Adjoint of a Linear Map|adjoint]] $T^*$ of $T$ is the unique operator satisfying $\langle Tv, w \rangle = \langle v, T^* w \rangle$ for all $v, w \in V$. Over $\mathbb{C}$, the inner product is conjugate-linear in the second slot: $\langle v, \alpha w \rangle = \overline{\alpha} \langle v, w \rangle$.

An [[Def - Inner Product Space|inner product]] satisfies $\langle v, v \rangle \geq 0$ with equality iff $v = 0$, so $\langle v, v \rangle$ is a positive real number for non-zero $v$.

---

# Convergent Strategy

**Problem class.** This is the most basic verification problem in the chapter: prove a structural property of self-adjoint operators directly from the definition. It is the kind of problem where the answer is obtained in one short calculation using the defining relation, with no machinery required beyond inner product manipulations.

**Assumption pattern.** The hypothesis is $T = T^*$, which translates to the relation $\langle Tv, w \rangle = \langle v, Tw \rangle$ for all $v, w$. The conclusion is about eigenvalues, so we need an eigenvector: pick a non-zero $v$ with $Tv = \lambda v$. The remaining computational task is to extract a real number from the eigenvalue equation, given the self-adjoint relation.

**Theorem routing.** The route is direct: compute $\langle Tv, v \rangle$ using both the eigenvalue equation and the self-adjoint relation $\langle Tv, v \rangle = \langle v, Tv \rangle$. This gives the equation $\lambda \langle v, v \rangle = \overline{\lambda} \langle v, v \rangle$ (using conjugate-linearity of $\langle \cdot, \cdot \rangle$ in the second slot). Since $\langle v, v \rangle > 0$, divide to get $\lambda = \overline{\lambda}$, i.e., $\lambda \in \mathbb{R}$.

**Key decision point.** The non-obvious move is computing $\langle Tv, v \rangle$ in *two different ways* using the same eigenvector. The first way uses $T v = \lambda v$ directly. The second way uses self-adjointness $\langle Tv, v \rangle = \langle v, Tv \rangle$, then plugs in $T v = \lambda v$ on the right side. The two ways yield expressions involving $\lambda$ vs $\overline{\lambda}$, and their equality forces reality.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VII — §7 Operators on Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Compute with the adjoint via the defining relation** — Push the operator across the inner product using $\langle Tv, w \rangle = \langle v, T^* w \rangle$. With $T = T^*$, this becomes $\langle Tv, w \rangle = \langle v, Tw \rangle$ — the inner product is symmetric in the action of $T$.

2. **Use the positivity of the inner product on the diagonal** — $\langle v, v \rangle > 0$ for $v \neq 0$, allowing division by this quantity.

3. **Use conjugate-linearity of the inner product in the second slot** — $\langle v, \alpha w \rangle = \overline{\alpha} \langle v, w \rangle$, converting $\lambda$ to $\overline{\lambda}$ when $\lambda$ moves across the comma.

---

# Hints

> [!note]- Hint 1
> The problem is asking you to prove $\lambda = \overline{\lambda}$. You have one piece of information about $T$: $T = T^*$. You have one piece of information about $\lambda$ and $v$: $Tv = \lambda v$ with $v \neq 0$. Combine these by computing a single inner product two different ways.

> [!note]- Hint 2
> Compute $\langle Tv, v \rangle$ in two ways: once using the eigenvalue equation, once using self-adjointness $T = T^*$.

> [!note]- Hint 3
> First way: $\langle Tv, v \rangle = \langle \lambda v, v \rangle = \lambda \langle v, v \rangle$. Second way: $\langle Tv, v \rangle = \langle v, T^* v \rangle = \langle v, Tv \rangle = \langle v, \lambda v \rangle = \overline{\lambda} \langle v, v \rangle$ (conjugate-linearity in the second slot moves the bar). Equate.

---

# Solution

The proof is a single inner product computed two ways: once using the eigenvalue equation to pull $\lambda$ out of the first slot, once using self-adjointness then the eigenvalue equation to push $\lambda$ into the second slot — where it acquires a conjugate. The equality forces $\lambda = \overline{\lambda}$, hence $\lambda$ is real.

**Step 1: Compute $\langle Tv, v \rangle$ using the eigenvalue equation in the first slot.**

$$\langle Tv, v \rangle = \langle \lambda v, v \rangle = \lambda \langle v, v \rangle.$$

> [!note]- Derivation
> Since $Tv = \lambda v$, the inner product $\langle Tv, v \rangle$ equals $\langle \lambda v, v \rangle$. By linearity of the inner product in the first slot (Axler convention), $\langle \lambda v, v \rangle = \lambda \langle v, v \rangle$. The eigenvalue $\lambda$ comes out as a scalar multiplier.

**Step 2: Compute $\langle Tv, v \rangle$ using self-adjointness, then the eigenvalue equation in the second slot.**

$$\langle Tv, v \rangle = \langle v, Tv \rangle = \langle v, \lambda v \rangle = \overline{\lambda} \langle v, v \rangle.$$

> [!note]- Derivation
> First, self-adjointness $T = T^*$ gives $\langle Tv, v \rangle = \langle v, T^* v \rangle = \langle v, Tv \rangle$. So $T$ can be moved from the first slot to the second slot.
>
> Now apply the eigenvalue equation $T v = \lambda v$ in the second slot: $\langle v, T v \rangle = \langle v, \lambda v \rangle$. By conjugate-linearity of the inner product in the second slot (this is where over-$\mathbb{C}$ care is essential): $\langle v, \lambda v \rangle = \overline{\lambda} \langle v, v \rangle$. The scalar $\lambda$ comes out *conjugated*.

**Step 3: Equate the two expressions and conclude $\lambda \in \mathbb{R}$.**

From Steps 1 and 2: $\lambda \langle v, v \rangle = \overline{\lambda} \langle v, v \rangle$. Since $v \neq 0$, $\langle v, v \rangle > 0$. Divide to get $\lambda = \overline{\lambda}$, i.e., $\lambda \in \mathbb{R}$. ✓

> [!note]- Derivation
> $(\lambda - \overline{\lambda}) \langle v, v \rangle = 0$. The inner product $\langle v, v \rangle = \|v\|^2$ is strictly positive since $v$ is a non-zero vector in an inner product space (positivity axiom). Dividing both sides by $\langle v, v \rangle$, $\lambda - \overline{\lambda} = 0$, so $\lambda = \overline{\lambda}$. By the definition of complex conjugation, this means $\lambda$ has zero imaginary part, i.e., $\lambda$ is real.

> [!note]- Complete formal solution
> Let $v \in V$ be a nonzero eigenvector of $T$ with eigenvalue $\lambda$: $Tv = \lambda v$.
>
> Compute the inner product $\langle Tv, v \rangle$ in two ways.
>
> *First way (eigenvalue equation in first slot):* $\langle Tv, v \rangle = \langle \lambda v, v \rangle = \lambda \langle v, v \rangle$, using linearity of the inner product in the first slot.
>
> *Second way (self-adjointness, then eigenvalue equation in second slot):* $\langle Tv, v \rangle = \langle v, T^* v \rangle = \langle v, T v \rangle = \langle v, \lambda v \rangle = \overline{\lambda} \langle v, v \rangle$, using the defining relation of the adjoint, self-adjointness $T = T^*$, the eigenvalue equation in the second slot, and conjugate-linearity in the second slot.
>
> Therefore $\lambda \langle v, v \rangle = \overline{\lambda} \langle v, v \rangle$, i.e., $(\lambda - \overline{\lambda}) \langle v, v \rangle = 0$. Since $v$ is nonzero, $\langle v, v \rangle = \|v\|^2 > 0$. So $\lambda = \overline{\lambda}$, i.e., $\lambda \in \mathbb{R}$. $\blacksquare$

---

# Key Takeaways

**The "compute one quantity two ways" technique is the workhorse of operator-theoretic proofs.** The whole proof of this exercise is a single inner product, $\langle Tv, v \rangle$, computed two ways. The first computation uses the eigenvalue equation in the first slot to extract $\lambda$. The second computation uses self-adjointness to move $T$ to the second slot, then applies the eigenvalue equation there to extract $\overline{\lambda}$. The two expressions must be equal (it is the same inner product), and the equality $\lambda = \overline{\lambda}$ is forced. This pattern — set up two expressions for the same quantity by exploiting two structural properties of $T$, equate them, and extract a constraint — recurs throughout inner product space theory. Other instances: orthogonality of eigenvectors for distinct eigenvalues of a normal operator, the relation $T^{**} = T$, the conjugation pairing for normal operators.

**Self-adjointness over $\mathbb{C}$ is meaningful only because of the conjugation in the inner product.** Over $\mathbb{R}$, the calculation $\lambda = \overline{\lambda}$ is vacuous: every real number equals its conjugate, so the calculation says nothing. The content of "self-adjoint implies real eigenvalues" is non-trivial only when the field is $\mathbb{C}$ — and the non-triviality comes from the conjugate-linearity of the inner product in the second slot. Whenever a complex inner product space calculation involves a conjugation moving across a slot, one is implicitly using the structure that makes $\mathbb{C}$ have an order-2 automorphism (complex conjugation). Real inner product spaces lack this automorphism, and many statements that look interesting in the complex case (like this one) become trivial in the real case.

**The eigenvalues live wherever the spectrum lives.** This exercise is the first appearance of a recurring theme: the location of the eigenvalues of an operator class in $\mathbb{C}$ characterises the class. Self-adjoint operators have all eigenvalues on the real line $\mathbb{R}$. [[Def - Unitary Operator|Unitary operators]] have all eigenvalues on the unit circle of $\mathbb{C}$. [[Def - Positive Operator|Positive operators]] have all eigenvalues on the non-negative real ray $[0, \infty)$. Skew-adjoint operators (with $T^* = -T$) have all eigenvalues on the imaginary axis $i\mathbb{R}$. Each operator class is the analogue of a region of $\mathbb{C}$, and the spectral theorem makes this analogy literal: normal operators with eigenvalues in a region $R \subseteq \mathbb{C}$ are exactly the operators of the corresponding class. This exercise establishes one entry in this dictionary: self-adjoint = real spectrum.
