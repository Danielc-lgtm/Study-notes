---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Complex Spectral Theorem"
  - "Thm - Real Spectral Theorem"
  - "Def - Self-Adjoint Operator"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $S, T \in \mathcal{L}(V)$ be two self-adjoint operators on a finite-dimensional inner product space, with $ST = TS$. Show that $S$ and $T$ have a *common* orthonormal eigenbasis: there is an orthonormal basis $\{e_j\}$ of $V$ such that each $e_j$ is an eigenvector of both $S$ and $T$.

**Recall:**

![[Thm - Complex Spectral Theorem#Statement]]

For self-adjoint operators on a real or complex inner product space, the [[Thm - Real Spectral Theorem|real]] or [[Thm - Complex Spectral Theorem|complex]] spectral theorem gives an orthonormal eigenbasis. The question here is whether two commuting self-adjoint operators share such a basis.

---

# Convergent Strategy

**Problem class.** This is a *joint diagonalisation* problem: extend the single-operator spectral theorem to a pair of commuting operators.

**Assumption pattern.** The hypothesis is that $S$ and $T$ are self-adjoint and commute. The conclusion is the existence of a common orthonormal eigenbasis.

**Theorem routing.** The route: spectrally decompose $S$ first, then observe that each eigenspace of $S$ is invariant under $T$ (because $T$ commutes with $S$, so preserves the eigenspaces of $S$). On each eigenspace of $S$, restrict $T$ and apply the spectral theorem again. Combine the resulting orthonormal eigenbases of $T$ across all $S$-eigenspaces.

**Key decision point.** The non-obvious move is recognising that **the eigenspaces of $S$ are $T$-invariant when $S$ and $T$ commute**. This is the bridge that lets one apply the spectral theorem twice — once for $S$, then once for $T$ on each eigenspace.

---

# Legal Operations Used

1. **Spectral theorem for self-adjoint operators** — Apply to both $S$ and $T$ separately, then within eigenspaces.
2. **Commuting operators preserve each other's eigenspaces** — Standard fact, derived from $ST = TS$ acting on an eigenvector.
3. **Restriction of self-adjoint operator to invariant [[Def - Subspace|subspace]] remains self-adjoint** — Self-adjointness restricts.

---

# Hints

> [!note]- Hint 1
> Diagonalise $S$ first: $V = \bigoplus_\lambda E(\lambda, S)$ with eigenspaces orthogonal. Show that each $E(\lambda, S)$ is invariant under $T$.

> [!note]- Hint 2
> If $v \in E(\lambda, S)$, what is $S(Tv)$? Use $ST = TS$.

> [!note]- Hint 3
> $S(Tv) = T(Sv) = T(\lambda v) = \lambda (Tv)$, so $Tv \in E(\lambda, S)$. Now diagonalise $T$ restricted to each $E(\lambda, S)$.

---

# Solution

**Step 1: Each eigenspace of $S$ is $T$-invariant.**

Let $E_\lambda = E(\lambda, S)$. For $v \in E_\lambda$: $S(Tv) = (ST) v = (TS) v = T(Sv) = T(\lambda v) = \lambda (Tv)$. So $Tv$ is in the $\lambda$-eigenspace of $S$, i.e., $Tv \in E_\lambda$. Hence $T(E_\lambda) \subseteq E_\lambda$.

> [!note]- Derivation
> The commutation $ST = TS$ is what allows pushing $S$ past $T$. Without commutation, $S(Tv)$ has no clean expression in terms of $v$ alone.

**Step 2: $T$ restricted to $E_\lambda$ is self-adjoint.**

For $v, w \in E_\lambda$: $\langle T|_{E_\lambda} v, w \rangle = \langle Tv, w \rangle$ (using the inherited inner product on $E_\lambda$). And $\langle Tv, w \rangle = \langle v, Tw \rangle$ (using self-adjointness of $T$ on $V$). So $T|_{E_\lambda}$ is self-adjoint.

> [!note]- Derivation
> The restriction's adjoint is the restriction of the adjoint, provided the [[Def - Subspace|subspace]] is preserved by both. By Step 1, $E_\lambda$ is $T$-invariant; trivially also $T^*$-invariant (since $T = T^*$). So self-adjointness restricts.

**Step 3: Apply spectral theorem to $T|_{E_\lambda}$ for each eigenvalue $\lambda$ of $S$.**

By the spectral theorem applied to the self-adjoint operator $T|_{E_\lambda}$, each $E_\lambda$ has an orthonormal basis of eigenvectors of $T$. Each such eigenvector $e$ satisfies:
- $S e = \lambda e$ (since $e \in E_\lambda$),
- $T e = \mu e$ for some $\mu$ (eigenvector of $T|_{E_\lambda}$ with eigenvalue $\mu$).

So $e$ is a common eigenvector of $S$ and $T$.

**Step 4: Combine into a common orthonormal eigenbasis of $V$.**

Concatenate the orthonormal bases of all the eigenspaces $E_\lambda$. Vectors from different eigenspaces are orthogonal (eigenspaces of $S$ for distinct eigenvalues are orthogonal). The union is an orthonormal basis of $V = \bigoplus_\lambda E_\lambda$. Every basis vector is a common eigenvector of $S$ and $T$.

> [!note]- Complete formal solution
> By the spectral theorem applied to $S$, $V = \bigoplus_\lambda E(\lambda, S)$, an orthogonal direct sum of eigenspaces.
>
> For each $\lambda$: since $ST = TS$, $E(\lambda, S)$ is $T$-invariant. Restrict $T$ to $E(\lambda, S)$; this is still self-adjoint (restriction of a self-adjoint operator to an invariant subspace, with both operator and adjoint preserving the subspace). By the spectral theorem applied to $T|_{E(\lambda, S)}$, $E(\lambda, S)$ has an orthonormal basis of eigenvectors of $T|_{E(\lambda, S)}$, hence of $T$. Each such vector is also an eigenvector of $S$ with eigenvalue $\lambda$ (by definition of $E(\lambda, S)$).
>
> Concatenate these bases across all $\lambda$: the resulting orthonormal list is a basis of $V$ (since $V = \bigoplus E(\lambda, S)$) consisting of common eigenvectors of $S$ and $T$. $\blacksquare$

---

# Key Takeaways

**Commutation is the precise condition for joint diagonalisation.** Two self-adjoint operators $S, T$ have a common orthonormal eigenbasis if and only if they commute. The proof uses commutation in the form "$T$ preserves the eigenspaces of $S$", which is the structural content of commutation. Without commutation, the proof fails — and indeed non-commuting self-adjoint operators in general have no common eigenbasis. The matrix pair $\sigma_x, \sigma_z$ (Pauli matrices) do not commute and have no common eigenbasis; this is the operator-theoretic content of the Heisenberg uncertainty principle for spin observables.

**The argument extends to commuting normal operators.** The same proof works for any pair of commuting normal operators (not just self-adjoint), with the conjugation pairing replacing the eigenvalue-reality property. The key fact — that $T$ preserves the eigenspaces of $S$ when $ST = TS$ — is purely algebraic and does not need self-adjointness; what self-adjointness contributes is that the eigenvalues are real, but the *eigenspaces* exist either way.

**Heisenberg uncertainty principle is exactly this theorem's failure.** Two observables $\hat A, \hat B$ in quantum mechanics can be jointly measured with arbitrary precision if and only if they share an eigenbasis, if and only if they commute. When they do not commute, the variances of measurements are bounded below by $\frac{1}{2} |\langle [\hat A, \hat B] \rangle|$. For position $\hat x$ and momentum $\hat p$, $[\hat x, \hat p] = i\hbar$, giving the famous $\sigma_x \sigma_p \geq \hbar / 2$. The uncertainty principle is the quantitative version of "non-commuting normal operators have no common eigenbasis". This exercise is the qualitative side; the uncertainty principle is the quantitative refinement.
