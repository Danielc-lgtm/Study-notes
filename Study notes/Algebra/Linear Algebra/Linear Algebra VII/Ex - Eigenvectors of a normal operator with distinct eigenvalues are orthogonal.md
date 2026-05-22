---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Normal Operator"
  - "Def - Adjoint of a Linear Map"
  - "Thm - Normal Operators Commute with Their Adjoint"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional inner product space over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$, and let $T \in \mathcal{L}(V)$ be [[Def - Normal Operator|normal]] ($TT^* = T^*T$). Suppose $v, w \in V$ are eigenvectors with eigenvalues $\lambda, \mu$ respectively, and $\lambda \neq \mu$. Show that $\langle v, w \rangle = 0$.

**Recall:**

![[Def - Normal Operator#The Definition]]

The key consequence of normality is the **eigenvector-eigenvalue conjugation pairing**: for normal $T$, if $Tv = \lambda v$ then $T^* v = \overline{\lambda} v$. This says that $T$ and $T^*$ have the same eigenvectors, with conjugated eigenvalues. (See [[Thm - Normal Operators Commute with Their Adjoint]] for the proof.)

An [[Def - Adjoint of a Linear Map|adjoint]] satisfies $\langle Tv, w \rangle = \langle v, T^* w \rangle$.

---

# Convergent Strategy

**Problem class.** This is the eigenvector-orthogonality calculation that underpins the [[Thm - Complex Spectral Theorem|spectral theorem]]'s "orthonormal eigenbasis" conclusion. The problem class is the same as for [[Ex - Self-adjoint operators have real eigenvalues]] — compute one quantity (an inner product) two ways using the operator's defining property — but with the additional twist that we need the conjugation pairing for normal operators rather than direct self-adjointness.

**Assumption pattern.** The hypothesis is that $T$ is normal, $Tv = \lambda v$, $Tw = \mu w$, $\lambda \neq \mu$. The conclusion is $\langle v, w \rangle = 0$. The strategy: compute $\langle Tv, w \rangle$ two ways. First way: use the eigenvalue equation $Tv = \lambda v$. Second way: push $T$ to the other slot using the adjoint relation, then use the conjugation pairing $T^* w = \overline{\mu} w$.

**Theorem routing.** The route invokes [[Thm - Normal Operators Commute with Their Adjoint]] for the conjugation pairing: for normal $T$, $Tw = \mu w$ implies $T^* w = \overline{\mu} w$. Then the standard "compute two ways" technique applies: $\langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle$ (the conjugation in $\overline{\mu}$ cancels with conjugate-linearity in the second slot, leaving $\mu$). Comparing with $\langle Tv, w \rangle = \lambda \langle v, w \rangle$ from the first way gives $(\lambda - \mu) \langle v, w \rangle = 0$, so $\langle v, w \rangle = 0$.

**Key decision point.** The non-obvious move is applying the eigenvector-eigenvalue conjugation pairing to $w$ — specifically, that $Tw = \mu w$ implies $T^* w = \overline{\mu} w$. This is the *normality* in action; without it, $T^* w$ would not be a scalar multiple of $w$, and the second computation of $\langle Tv, w \rangle$ would not collapse to a scalar times $\langle v, w \rangle$. Without normality, the proof fails — and indeed, eigenvectors of a non-normal operator for distinct eigenvalues are not in general orthogonal.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VII — §7 Operators on Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Compute with the adjoint via the defining relation** — Push $T$ across the inner product using $\langle Tv, w \rangle = \langle v, T^* w \rangle$.

2. **Use the eigenvector-eigenvalue conjugation pairing for normal operators** — Apply the result that $Tw = \mu w$ implies $T^* w = \overline{\mu} w$ for normal $T$.

3. **Use conjugate-linearity of the inner product in the second slot** — $\langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle$, since the conjugation in $\overline{\mu}$ and the conjugation in the second slot cancel.

---

# Hints

> [!note]- Hint 1
> The strategy is to compute $\langle Tv, w \rangle$ in two ways. The first way uses $Tv = \lambda v$ directly. The second way needs the action of $T$ to move to the other slot — but that requires the adjoint $T^*$.

> [!note]- Hint 2
> Use the [[Thm - Normal Operators Commute with Their Adjoint|conjugation pairing for normal operators]]: $Tw = \mu w$ implies $T^* w = \overline{\mu} w$. This is the crucial input — without normality, $T^* w$ has no clean expression in terms of $w$.

> [!note]- Hint 3
> First way: $\langle Tv, w \rangle = \langle \lambda v, w \rangle = \lambda \langle v, w \rangle$. Second way: $\langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle$ (the conjugate-linearity in the second slot moves $\overline{\mu}$ to its conjugate, $\mu$). Equate.

---

# Solution

The proof is a single inner product, $\langle Tv, w \rangle$, computed two ways. The first way uses $Tv = \lambda v$. The second uses the adjoint relation to move $T$ to the second slot, then the conjugation pairing $T^* w = \overline{\mu} w$ (valid because $T$ is normal), then conjugate-linearity to extract $\mu$ as a scalar. The two expressions $\lambda \langle v, w \rangle$ and $\mu \langle v, w \rangle$ must be equal, forcing $(\lambda - \mu) \langle v, w \rangle = 0$. Since $\lambda \neq \mu$, $\langle v, w \rangle = 0$.

**Step 1: Apply the conjugation pairing to $w$.**

Since $T$ is normal and $Tw = \mu w$, $T^* w = \overline{\mu} w$.

> [!note]- Derivation
> This is the content of [[Thm - Normal Operators Commute with Their Adjoint|the conjugation pairing for normal operators]]. The proof: for normal $T$, $\|Sv\| = \|S^* v\|$ for any $v$, applied to $S = T - \mu I$ (also normal because shifts of normal operators are normal). So $\|(T - \mu I) v\| = \|(T - \mu I)^* v\| = \|(T^* - \overline{\mu} I) v\|$, hence $(T - \mu I) v = 0$ iff $(T^* - \overline{\mu} I) v = 0$, i.e., $T v = \mu v$ iff $T^* v = \overline{\mu} v$.

**Step 2: Compute $\langle Tv, w \rangle$ using the eigenvalue equation in the first slot.**

$$\langle Tv, w \rangle = \langle \lambda v, w \rangle = \lambda \langle v, w \rangle.$$

> [!note]- Derivation
> From $Tv = \lambda v$, $\langle Tv, w \rangle = \langle \lambda v, w \rangle$. By linearity of the inner product in the first slot, this equals $\lambda \langle v, w \rangle$.

**Step 3: Compute $\langle Tv, w \rangle$ using the adjoint and the conjugation pairing.**

$$\langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle.$$

> [!note]- Derivation
> By the defining relation of the adjoint, $\langle Tv, w \rangle = \langle v, T^* w \rangle$. By Step 1, $T^* w = \overline{\mu} w$, so $\langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle$. By conjugate-linearity in the second slot, $\langle v, \overline{\mu} w \rangle = \overline{\overline{\mu}} \langle v, w \rangle = \mu \langle v, w \rangle$.
>
> The two conjugations cancel: the $\overline{\mu}$ inside the inner product, and the conjugate-linearity in the second slot which adds a conjugation when extracting a scalar. The net effect is to bring $\mu$ out of the inner product with no conjugation.

**Step 4: Conclude $\langle v, w \rangle = 0$.**

From Steps 2 and 3: $\lambda \langle v, w \rangle = \mu \langle v, w \rangle$, i.e., $(\lambda - \mu) \langle v, w \rangle = 0$. Since $\lambda \neq \mu$, $\langle v, w \rangle = 0$.

> [!note]- Derivation
> $(\lambda - \mu) \langle v, w \rangle = 0$. By hypothesis $\lambda \neq \mu$, so $\lambda - \mu$ is a non-zero scalar. Dividing both sides by $\lambda - \mu$ gives $\langle v, w \rangle = 0$.

> [!note]- Complete formal solution
> Let $T$ be normal, $Tv = \lambda v$, $Tw = \mu w$ with $\lambda \neq \mu$.
>
> By the eigenvector-eigenvalue conjugation pairing for normal operators ([[Thm - Normal Operators Commute with Their Adjoint]]), $T^* w = \overline{\mu} w$.
>
> Compute $\langle Tv, w \rangle$ in two ways:
>
> *First way:* $\langle Tv, w \rangle = \langle \lambda v, w \rangle = \lambda \langle v, w \rangle$, using linearity in the first slot.
>
> *Second way:* $\langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, \overline{\mu} w \rangle = \mu \langle v, w \rangle$, using the defining relation of the adjoint, the conjugation pairing for $w$, and conjugate-linearity in the second slot.
>
> So $\lambda \langle v, w \rangle = \mu \langle v, w \rangle$, hence $(\lambda - \mu) \langle v, w \rangle = 0$. Since $\lambda \neq \mu$, $\langle v, w \rangle = 0$. $\blacksquare$

> [!warning] Illegal but tempting alternative: skipping the conjugation pairing.
> A common error is to write the second way as $\langle Tv, w \rangle = \langle v, T^* w \rangle = \langle v, Tw \rangle$ (treating $T^*$ as $T$ without using normality), then proceeding $= \langle v, \mu w \rangle = \overline{\mu} \langle v, w \rangle$. This yields $\lambda = \overline{\mu}$, *not* $\lambda = \mu$. For self-adjoint $T$, the eigenvalues are real, so $\mu = \overline{\mu}$ and the conclusion still holds — but for general normal $T$ with non-real eigenvalues (e.g., a unitary operator with eigenvalues on the unit circle), the conclusion would fail. The normality hypothesis is what gives $T^*w = \overline{\mu}w$ (not $\mu w$), and the conjugation cancellation in Step 3 is essential.

---

# Key Takeaways

**The conjugation pairing $T^*w = \overline{\mu} w$ is the source of orthogonality.** This exercise reveals what makes normal operators special: their eigenvectors are simultaneously eigenvectors of the adjoint, with conjugated eigenvalues. This pairing is what creates the "tension" between the first slot (eigenvalue $\lambda$) and the second slot (eigenvalue $\mu$, after pushing $T$ across) that forces orthogonality when the eigenvalues are distinct. Without the conjugation pairing — that is, for non-normal operators — the proof fails, and indeed non-normal operators can have non-orthogonal eigenvectors for distinct eigenvalues. The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ has distinct real eigenvalues $1, 2$ but its eigenvectors $(1, 0)$ and $(1, 1)$ are not orthogonal. Normality is exactly what makes eigenvectors orthogonal.

**The "compute two ways" pattern is the structural method for inner product proofs.** This is the second instance of the pattern (see also [[Ex - Self-adjoint operators have real eigenvalues]]). Compute one quantity — here $\langle Tv, w \rangle$ — using two different properties of the operator (eigenvalue equation in the first slot vs adjoint relation + conjugation pairing). The equality forces a constraint on the quantities involved. This pattern is the engine of countless inner-product-space proofs, including the proofs that eigenvalues of unitary operators have modulus $1$, that eigenvalues of self-adjoint operators are real, and that eigenvalues of positive operators are non-negative.

**This exercise is the central calculation of the spectral theorem.** The [[Thm - Complex Spectral Theorem|complex spectral theorem]] says normal operators have orthonormal eigenbases. The orthogonality of distinct-eigenvalue eigenvectors is exactly this exercise. Combined with the fact that eigenspaces span $V$ (the *complete* diagonalisability, proved by induction in the spectral theorem's proof), this gives the orthonormal eigenbasis. So this short calculation is one of the two pillars of the spectral theorem, the other being "every operator on a complex inner product space has an eigenvalue" (the fundamental theorem of algebra). Internalising this exercise makes the spectral theorem feel inevitable.
