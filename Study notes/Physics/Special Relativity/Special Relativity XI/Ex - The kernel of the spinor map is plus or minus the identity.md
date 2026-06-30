---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group"
  - "Def - The Spinor Map and SL(2,C)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Problem Statement

1. Compute the kernel of the [[Def - The Spinor Map and SL(2,C)|spinor map]]: find all $A \in SL(2,\mathbb{C})$ with $\mathscr{S}(A) = \mathrm{Id}$, i.e. $A\underline X A^\dagger = \underline X$ for every Hermitian $\underline X$. Show the kernel is exactly $\{I, -I\}$.
2. Deduce that $\mathscr{S}$ is two-to-one: $\mathscr{S}(A) = \mathscr{S}(B) \iff B = \pm A$.
3. Verify the simplest case of the double cover directly: show that the two $SU(2)$ matrices $A = I$ (rotation angle $\theta = 0$) and $A = -I$ (angle $\theta = 2\pi$, from $\exp(-i\pi\,\mathbf n\cdot\boldsymbol\sigma) = -I$) both produce the identity rotation, and that a left Weyl spinor $\xi$ is mapped to $+\xi$ by the first and $-\xi$ by the second.

**Recall:**

![[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group#Statement]]

The spinor map acts by $\underline X \mapsto A\underline X A^\dagger$ on [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Hermitian matrices]] $\underline X = x^\mu\sigma_\mu$. A [[Def - Weyl Spinors (Left and Right Handed)|left Weyl spinor]] transforms by $\xi \mapsto A\xi$ (one factor of $A$), unlike a four-vector which transforms by two factors.

---

# Convergent Strategy

**Problem class.** A *kernel computation* — the algebraic core of the double-cover theorem. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Sources and Targets|topic's target list]] names "establish a homomorphism or covering property" as a recurring goal; the kernel is the single calculation that turns "homomorphism" into "double cover."

**Assumption pattern.** The assumption is $A\underline X A^\dagger = \underline X$ for *all* Hermitian $\underline X$ — a strong condition, since it must hold for the four basis matrices $\sigma_\mu$ simultaneously. The signpost is "for all $\underline X$," which means you may *choose* convenient test matrices to extract constraints, and the right choices ($I$ first, then the $\sigma_i$) collapse the condition to "$A$ is a scalar."

**Theorem routing.** This exercise proves [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|Lemma 3 of the double-cover theorem]] and then applies the homomorphism property (from [[Def - The Spinor Map and SL(2,C)|the spinor map]]) to deduce two-to-one-ness via the first isomorphism theorem. The key fact routed through is Schur's lemma in its concrete form: only scalars commute with all Pauli matrices.

**Key decision point.** The crux is the *order* of test matrices. Testing $\underline X = I$ first yields $AA^\dagger = I$ (unitarity), which simplifies the remaining condition to $A\underline X A^{-1} = \underline X$ — commutation with all Hermitian matrices. Then testing $\sigma_3$ forces $A$ diagonal, and $\sigma_1$ forces the two diagonal entries equal. Choosing the test matrices in this order ($I$, then $\sigma_3$, then $\sigma_1$) is what makes the computation short; testing them in a different order works but is messier. The second decision is remembering that $\det A = 1$ allows *two* scalars $\pm 1$, not one.

---

# Legal Operations Used

1. **Act by congruence $\underline X \mapsto A\underline X A^\dagger$** (operation 2 from the topic page): the kernel condition is that this congruence is the identity, tested on the basis matrices.

2. **Lift to the two preimages $\pm A$** (operation 6 from the topic page): part 2 is the statement that the fibres of $\mathscr{S}$ are exactly the pairs $\{A, -A\}$, which this exercise establishes.

3. **Read $\xi \mapsto A\xi$ as the spinor law, distinct from the four-vector law** (operation 7 / warning 3 from the topic page): part 3 contrasts the spinor's sign flip under $-I$ with the four-vector's invariance.

---

# Hints

> [!note]- Hint 1
> Test the kernel condition on $\underline X = \sigma_0 = I$ first: $A I A^\dagger = AA^\dagger = I$, so $A$ is unitary and $A^\dagger = A^{-1}$. The condition becomes $A\underline X A^{-1} = \underline X$, i.e. $A$ commutes with every Hermitian matrix.

> [!note]- Hint 2
> $A$ commuting with $\sigma_3 = \mathrm{diag}(1,-1)$ forces $A$ to be diagonal. $A$ commuting with $\sigma_1 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ then forces the two diagonal entries to be equal, so $A = \lambda I$.

> [!note]- Hint 3
> The determinant condition $\det(\lambda I) = \lambda^2 = 1$ gives $\lambda = \pm 1$. So the kernel is $\{I, -I\}$ — two elements, not one.

> [!note]- Hint 4
> For part 2, use that $\mathscr{S}$ is a homomorphism: $\mathscr{S}(A) = \mathscr{S}(B) \iff \mathscr{S}(AB^{-1}) = \mathrm{Id} \iff AB^{-1} \in \ker = \{\pm I\} \iff B = \pm A$.

---

# Solution

The exercise computes the kernel by testing the congruence condition on well-chosen matrices, then leverages the homomorphism property to read off the two-to-one structure, and finally exhibits the simplest concrete instance — the identity rotation with its two preimages $\pm I$ and their opposite effect on a spinor. The plan: $I$ forces unitarity, $\sigma_3$ forces diagonal, $\sigma_1$ forces scalar, $\det$ forces $\pm 1$.

**Step 1: The kernel is $\{I, -I\}$.**

> [!note]- Derivation
> Suppose $\mathscr{S}(A) = \mathrm{Id}$, i.e. $A\underline X A^\dagger = \underline X$ for all Hermitian $\underline X$.
>
> *Test $\underline X = I$:* $A I A^\dagger = AA^\dagger = I$. So $A$ is **unitary**, $A^\dagger = A^{-1}$, and the kernel condition simplifies to
> $$A\underline X A^{-1} = \underline X \quad\text{for all Hermitian } \underline X,$$
> i.e. $A$ commutes with every Hermitian matrix.
>
> *Test $\underline X = \sigma_3 = \mathrm{diag}(1,-1)$:* $A\sigma_3 = \sigma_3 A$. Writing $A = \begin{pmatrix}a&b\\c&d\end{pmatrix}$, $A\sigma_3 = \begin{pmatrix}a&-b\\c&-d\end{pmatrix}$ and $\sigma_3 A = \begin{pmatrix}a&b\\-c&-d\end{pmatrix}$; equality forces $b = -b$ and $c = -c$, so $b = c = 0$ and $A = \mathrm{diag}(a,d)$ is diagonal.
>
> *Test $\underline X = \sigma_1 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$:* for diagonal $A = \mathrm{diag}(a,d)$, $A\sigma_1 = \begin{pmatrix}0&a\\d&0\end{pmatrix}$ and $\sigma_1 A = \begin{pmatrix}0&d\\a&0\end{pmatrix}$; equality forces $a = d$. Hence $A = aI = \lambda I$ is scalar.
>
> *Determinant:* $\det(\lambda I) = \lambda^2 = 1$, so $\lambda = \pm 1$, giving $A = \pm I$. Conversely both $\pm I$ are in the kernel: $(\pm I)\underline X(\pm I)^\dagger = \underline X$. Therefore $\ker\mathscr{S} = \{I, -I\}$.

**Step 2: $\mathscr{S}$ is two-to-one.**

> [!note]- Derivation
> Since $\mathscr{S}$ is a homomorphism ([[Def - The Spinor Map and SL(2,C)]]),
> $$\mathscr{S}(A) = \mathscr{S}(B) \iff \mathscr{S}(A)\mathscr{S}(B)^{-1} = \mathrm{Id} \iff \mathscr{S}(AB^{-1}) = \mathrm{Id} \iff AB^{-1} \in \ker\mathscr{S} = \{\pm I\}.$$
> The last condition is $AB^{-1} = I$ (so $A = B$) or $AB^{-1} = -I$ (so $A = -B$), i.e. $B = \pm A$. Thus every fibre $\mathscr{S}^{-1}(\Lambda)$ is the two-element set $\{A, -A\}$: the map is exactly two-to-one, and $SO^+(1,3) \cong SL(2,\mathbb{C})/\{\pm I\}$ by the first isomorphism theorem.

**Step 3: The identity rotation has preimages $\pm I$, with opposite effect on a spinor.**

> [!note]- Derivation
> Take any axis $\mathbf n$. The $SU(2)$ matrix for a rotation by $\theta$ is $A(\theta) = \exp(-\tfrac{i\theta}{2}\mathbf n\cdot\boldsymbol\sigma) = \cos\tfrac\theta2 I - i\sin\tfrac\theta2\,\mathbf n\cdot\boldsymbol\sigma$.
>
> At $\theta = 0$: $A(0) = I$, and $\mathscr{S}(I) = \mathrm{Id}$, the identity rotation.
>
> At $\theta = 2\pi$: $A(2\pi) = \cos\pi\,I - i\sin\pi\,\mathbf n\cdot\boldsymbol\sigma = -I + 0 = -I$, and $\mathscr{S}(-I) = \mathrm{Id}$, again the identity rotation. So a "full $2\pi$ rotation" returns the *Lorentz transformation* to the identity but returns the $SU(2)$ matrix to $-I$, not $I$ — the visible signature of the double cover.
>
> *Effect on a spinor.* A [[Def - Weyl Spinors (Left and Right Handed)|left Weyl spinor]] transforms by $\xi \mapsto A\xi$. Under $A(0) = I$: $\xi \mapsto \xi$. Under $A(2\pi) = -I$: $\xi \mapsto -\xi$. So while the four-vector world sees no difference between $\theta = 0$ and $\theta = 2\pi$ (the rotation is the identity both times), the spinor world distinguishes them by a sign — the spinor must rotate through $4\pi$ to return, since $A(4\pi) = \cos 2\pi\,I = I$ gives $\xi \mapsto \xi$.

> [!note]- Complete formal solution
> Testing $\mathscr{S}(A) = \mathrm{Id}$ on $\underline X = I$ gives $AA^\dagger = I$ (unitary); on $\sigma_3$ gives $A$ diagonal; on $\sigma_1$ gives the diagonal entries equal, so $A = \lambda I$; and $\det A = \lambda^2 = 1$ gives $A = \pm I$, so $\ker\mathscr{S} = \{\pm I\}$. By the homomorphism property, $\mathscr{S}(A) = \mathscr{S}(B) \iff AB^{-1} \in \{\pm I\} \iff B = \pm A$, so $\mathscr{S}$ is two-to-one and $SO^+(1,3) \cong SL(2,\mathbb{C})/\{\pm I\}$. Concretely, $A(\theta) = \exp(-\tfrac{i\theta}{2}\mathbf n\cdot\boldsymbol\sigma)$ gives $A(0) = I$ and $A(2\pi) = -I$, both mapping to the identity rotation; a left Weyl spinor is sent to $+\xi$ by the first and $-\xi$ by the second, returning only after $\theta = 4\pi$. $\blacksquare$

---

# Key Takeaways

**"For all $\underline X$" is a licence to choose test matrices, and the right basis collapses the problem.** The kernel condition holds for *every* Hermitian matrix, which means you are free to feed it whichever matrices extract the cleanest constraints. The disciplined choice — $I$ to force unitarity, then $\sigma_3$ to force diagonality, then $\sigma_1$ to force scalarity — turns an apparently infinite family of conditions into three computations. This "universally quantified hypothesis $\Rightarrow$ test on a basis" move is ubiquitous: it is how one proves a bilinear form is determined by its values on basis pairs, how one shows an operator commuting with an irreducible family is scalar (Schur's lemma), and how one computes any kernel defined by an all-quantifier. The trigger is the phrase "for all," and the reaction is "choose the test inputs that isolate each unknown."

**The factor of two in the kernel is the factor of two in spin — they are literally the same.** The kernel has two elements, $\pm I$, because the determinant equation $\lambda^2 = 1$ has two roots; this is the entire arithmetic source of the double cover. And the same $\pm I$ is what a spinor sees and a four-vector does not: the four-vector law $A(\cdot)A^\dagger$ is blind to the sign (two factors, $(-A)(\cdot)(-A)^\dagger = A(\cdot)A^\dagger$), while the spinor law $A(\cdot)$ flips sign. So "the kernel has two elements," "a rotation has two preimages," "a spinor needs $4\pi$ to return," and "half-integer spin exists" are four phrasings of the one fact that $\lambda^2 = 1$ has the two solutions $\pm 1$. Whenever a factor of two surfaces in this chapter, trace it to this root, and the apparent collection of curiosities becomes one mechanism.

**The homomorphism property converts a kernel into a fibre structure for free.** Once the kernel is known, the two-to-one-ness is automatic and requires no further computation: for any homomorphism, two elements have the same image exactly when their "ratio" $AB^{-1}$ lies in the kernel, so the fibres are the cosets of the kernel. This is the first isomorphism theorem in action, and it is the reason that computing the kernel is the *entire* content of a covering claim — once you know $\ker = \{\pm I\}$, you know the map is two-to-one and the quotient is the base. The reusable principle: to understand the fibres of any homomorphism, compute its kernel; the fibres are then its translates, with no additional work. This is why the double-cover theorem's real labour is concentrated in the single kernel lemma.
