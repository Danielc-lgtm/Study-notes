---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Spinor Map SU(2) to SO(3)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Problem Statement

Consider the $SU(2)$ matrix $A(\theta) = \exp\!\big(-\tfrac{i\theta}{2}\sigma_3\big)$ for a rotation about the $z$-axis.

1. Compute $A(\theta)$ in closed form and verify $A(\theta) \in SU(2)$.
2. Compute its action by the [[Thm - The Spinor Map SU(2) to SO(3)|spinor map]], $\underline X \mapsto A(\theta)\underline X A(\theta)^\dagger$, on a general $\underline X = x^\mu\sigma_\mu$, and show $\mathscr{S}(A(\theta))$ is the rotation of $(x^1,x^2)$ by angle $\theta$, fixing $x^0$ and $x^3$.
3. Show that $A(\theta)$ and $A(\theta + 2\pi)$ differ by a sign but produce the *same* $SO(3)$ rotation, exhibiting the two-to-one cover. Confirm that the rotation has period $2\pi$ but the $SU(2)$ matrix has period $4\pi$.
4. (Quaternion form.) Express $A(\theta)$ as a unit quaternion and verify the rotation by the conjugation formula $\mathbf v \mapsto q\mathbf v q^{-1}$ for $\mathbf v$ a pure-imaginary quaternion.

**Recall:**

![[Thm - The Spinor Map SU(2) to SO(3)#Statement]]

The [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|correspondence]] sends $X$ to $\underline X = x^\mu\sigma_\mu$; the spatial part $(x^1,x^2,x^3)$ corresponds to the traceless part $x^i\sigma_i$. The quaternion realisation is $\mathbf 1 = I$, $\mathbf i = -i\sigma_1$, $\mathbf j = -i\sigma_2$, $\mathbf k = -i\sigma_3$ (see [[Def - Quaternions]]).

---

# Convergent Strategy

**Problem class.** A *concrete double-cover computation* — taking the abstract $SU(2)\to SO(3)$ theorem and running it on the simplest nontrivial case to make the half-angle and the sign flip tangible. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Problem-Solving Strategy|topic strategy]] says that when handed an $A$ you compute $A\sigma_\nu A^\dagger$; this exercise does that for a one-parameter family.

**Assumption pattern.** The single generator $\sigma_3$ is diagonal, which makes everything explicit: $A(\theta)$ is diagonal, and its action on $\underline X$ multiplies the off-diagonal entries by phases while fixing the diagonal. The signpost that this is the "compute directly" case is that the generator is diagonal, so no Pauli multiplication beyond $\sigma_3^2 = I$ is needed.

**Theorem routing.** This is a worked instance of [[Thm - The Spinor Map SU(2) to SO(3)]], specialising its Rodrigues computation to $\mathbf n = \hat z$. Part 3 illustrates [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|the kernel \{± I\}]] concretely; part 4 uses the [[Def - Quaternions|quaternion]] realisation.

**Key decision point.** The crux is recognising that for a diagonal $A(\theta) = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$, the congruence acts trivially on the diagonal of $\underline X$ (fixing $x^0, x^3$) and multiplies the off-diagonal entry $x^1 - ix^2$ by $e^{-i\theta}$, which is exactly a rotation of the complex number $x^1 - ix^2$ — hence of the vector $(x^1, x^2)$ — by angle $\theta$. Seeing the off-diagonal entry as the complex coordinate $x^1 - ix^2$ of the plane is what makes the rotation manifest without trigonometric expansion.

---

# Legal Operations Used

1. **Exponentiate a generator to build the group element** (operation 4 from the topic page): part 1 computes $A(\theta) = \exp(-\tfrac{i\theta}{2}\sigma_3)$ via $\sigma_3^2 = I$.

2. **Act by congruence $\underline X \mapsto A\underline X A^\dagger$** (operation 2 from the topic page): part 2 computes the action on the four basis matrices (equivalently on a general $\underline X$).

3. **Lift to the two preimages $\pm A$** (operation 6 from the topic page): part 3 shows $A(\theta)$ and $A(\theta+2\pi) = -A(\theta)$ give the same rotation.

---

# Hints

> [!note]- Hint 1
> Since $\sigma_3$ is diagonal, $\exp(-\tfrac{i\theta}{2}\sigma_3) = \mathrm{diag}(e^{-i\theta/2}, e^{+i\theta/2})$ directly (exponentiate each diagonal entry). Check $A^\dagger = \mathrm{diag}(e^{i\theta/2}, e^{-i\theta/2}) = A^{-1}$ and $\det A = e^{-i\theta/2}e^{i\theta/2} = 1$.

> [!note]- Hint 2
> Write $\underline X = \begin{pmatrix}x^0+x^3 & x^1-ix^2\\x^1+ix^2 & x^0-x^3\end{pmatrix}$. Conjugating by $A = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$ leaves the diagonal entries fixed and multiplies the upper-right entry $x^1 - ix^2$ by $e^{-i\theta/2}\cdot e^{-i\theta/2} = e^{-i\theta}$.

> [!note]- Hint 3
> $A(\theta + 2\pi) = \mathrm{diag}(e^{-i(\theta+2\pi)/2}, e^{i(\theta+2\pi)/2}) = \mathrm{diag}(e^{-i\theta/2}e^{-i\pi}, e^{i\theta/2}e^{i\pi}) = -A(\theta)$. Since the rotation depends only on $e^{-i\theta}$ (period $2\pi$ in $\theta$), $A(\theta)$ and $-A(\theta)$ give the same rotation.

> [!note]- Hint 4
> $A(\theta) = \cos\tfrac\theta2 I - i\sin\tfrac\theta2\,\sigma_3 = \cos\tfrac\theta2\,\mathbf 1 + \sin\tfrac\theta2\,\mathbf k$ (using $\mathbf k = -i\sigma_3$), a unit quaternion $q = \cos\tfrac\theta2 + \sin\tfrac\theta2\,\mathbf k$.

---

# Solution

The exercise runs the $SU(2)\to SO(3)$ machinery on the $z$-axis. The plan: exponentiate the diagonal generator to get $A(\theta) = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$; conjugate $\underline X$ and observe the off-diagonal phase $e^{-i\theta}$ rotates $(x^1, x^2)$ by $\theta$; note the period mismatch ($2\pi$ for the rotation, $4\pi$ for $A$); and reconcile with the quaternion conjugation formula.

**Step 1: $A(\theta) = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2}) \in SU(2)$.**

> [!note]- Derivation
> Since $\sigma_3 = \mathrm{diag}(1,-1)$ is diagonal, the exponential acts entrywise:
> $$A(\theta) = \exp\!\Big(-\tfrac{i\theta}{2}\sigma_3\Big) = \exp\begin{pmatrix}-i\theta/2 & 0 \\ 0 & i\theta/2\end{pmatrix} = \begin{pmatrix}e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2}\end{pmatrix}.$$
> Equivalently, using $\sigma_3^2 = I$: $A(\theta) = \cos\tfrac\theta2 I - i\sin\tfrac\theta2\,\sigma_3 = \mathrm{diag}(\cos\tfrac\theta2 - i\sin\tfrac\theta2, \cos\tfrac\theta2 + i\sin\tfrac\theta2)$, the same. Then $A^\dagger = \mathrm{diag}(e^{i\theta/2}, e^{-i\theta/2}) = A^{-1}$ (unitary) and $\det A = e^{-i\theta/2}\cdot e^{i\theta/2} = 1$, so $A(\theta) \in SU(2)$.

**Step 2: $\mathscr{S}(A(\theta))$ rotates $(x^1, x^2)$ by $\theta$, fixing $x^0, x^3$.**

> [!note]- Derivation
> Conjugate the Hermitian matrix:
> $$A\underline X A^\dagger = \begin{pmatrix}e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2}\end{pmatrix}\begin{pmatrix}x^0+x^3 & x^1-ix^2 \\ x^1+ix^2 & x^0-x^3\end{pmatrix}\begin{pmatrix}e^{i\theta/2} & 0 \\ 0 & e^{-i\theta/2}\end{pmatrix}.$$
> The diagonal entries pick up $e^{-i\theta/2}e^{i\theta/2} = 1$ and are unchanged: $x^0 + x^3$ and $x^0 - x^3$ stay, so $x^0, x^3$ are fixed. The upper-right entry picks up $e^{-i\theta/2}\cdot e^{-i\theta/2} = e^{-i\theta}$:
> $$(x^1 - ix^2) \mapsto e^{-i\theta}(x^1 - ix^2).$$
> Writing $w = x^1 - ix^2$ (the complex coordinate of the point $(x^1, x^2)$ with a conjugation convention), $w \mapsto e^{-i\theta}w$ is the rotation of the plane by angle $\theta$: explicitly, $x^1 - ix^2 \mapsto (\cos\theta - i\sin\theta)(x^1 - ix^2)$, giving
> $$x'^1 = \cos\theta\,x^1 + \sin\theta\,x^2, \qquad x'^2 = -\sin\theta\,x^1 + \cos\theta\,x^2,$$
> the standard rotation of $(x^1, x^2)$ by $\theta$. So $\mathscr{S}(A(\theta))$ is the spatial rotation by $\theta$ about the $z$-axis, fixing time and the $z$-direction — exactly the embedding of $SO(2) \subset SO(3) \subset SO^+(1,3)$.

**Step 3: The two-to-one cover and the period mismatch.**

> [!note]- Derivation
> The rotation in Step 2 depends on $\theta$ only through $e^{-i\theta}$, which has period $2\pi$: the $SO(3)$ rotation $R(\theta)$ satisfies $R(\theta + 2\pi) = R(\theta)$. But the $SU(2)$ matrix has period $4\pi$:
> $$A(\theta + 2\pi) = \mathrm{diag}(e^{-i(\theta+2\pi)/2}, e^{i(\theta+2\pi)/2}) = \mathrm{diag}(e^{-i\theta/2}e^{-i\pi}, e^{i\theta/2}e^{i\pi}) = \mathrm{diag}(-e^{-i\theta/2}, -e^{i\theta/2}) = -A(\theta),$$
> and $A(\theta + 4\pi) = A(\theta)$. So $A(\theta)$ and $A(\theta + 2\pi) = -A(\theta)$ are *different* $SU(2)$ matrices producing the *same* $SO(3)$ rotation — the two preimages $\{A, -A\}$ of the [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|double cover]]. As $\theta$ runs from $0$ to $2\pi$, the rotation returns to the identity but the $SU(2)$ matrix travels from $I$ to $-I$; only at $\theta = 4\pi$ does $A$ return to $I$. This is the source of the spinor's $4\pi$ periodicity: a spin state $\xi \mapsto A(2\pi)\xi = -\xi$ flips sign under one full rotation.

**Step 4: Quaternion form and the conjugation rotation.**

> [!note]- Derivation
> Using $\mathbf k = -i\sigma_3$, the matrix is the unit quaternion
> $$A(\theta) = \cos\tfrac\theta2\,I - i\sin\tfrac\theta2\,\sigma_3 = \cos\tfrac\theta2\,\mathbf 1 + \sin\tfrac\theta2\,\mathbf k =: q, \qquad \|q\|^2 = \cos^2\tfrac\theta2 + \sin^2\tfrac\theta2 = 1.$$
> The spatial vector $\mathbf v = (v^1, v^2, v^3)$ is the pure quaternion $v^1\mathbf i + v^2\mathbf j + v^3\mathbf k = -i(v^1\sigma_1 + v^2\sigma_2 + v^3\sigma_3) = -i\,\mathbf v\cdot\boldsymbol\sigma$. The conjugation $q\mathbf v q^{-1}$ corresponds, under the identification, to $A(-i\,\mathbf v\cdot\boldsymbol\sigma)A^\dagger = -i\,A(\mathbf v\cdot\boldsymbol\sigma)A^\dagger$ (since $q^{-1} = \bar q = A^\dagger$ for a unit quaternion), which by Step 2 (applied to the traceless part) rotates $\mathbf v$ by $\theta$ about $\hat z$. Explicitly $q\,\mathbf i\,q^{-1} = \cos\theta\,\mathbf i + \sin\theta\,\mathbf j$ and $q\,\mathbf j\,q^{-1} = -\sin\theta\,\mathbf i + \cos\theta\,\mathbf j$, fixing $\mathbf k$ — the rotation about the $z$-axis. The double cover reappears: $q$ and $-q$ give the same conjugation, so the same rotation.

> [!note]- Complete formal solution
> $A(\theta) = \exp(-\tfrac{i\theta}{2}\sigma_3) = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$, which is unitary with unit determinant. Conjugating $\underline X$ fixes the diagonal (so $x^0, x^3$) and multiplies the upper-right entry $x^1 - ix^2$ by $e^{-i\theta}$, rotating $(x^1, x^2)$ by $\theta$; hence $\mathscr{S}(A(\theta))$ is the rotation by $\theta$ about $z$. Since the rotation depends on $\theta$ through $e^{-i\theta}$ (period $2\pi$) while $A(\theta + 2\pi) = -A(\theta)$ (period $4\pi$), the matrices $A(\theta)$ and $-A(\theta)$ give the same rotation — the two-to-one cover — and a spinor $\xi \mapsto A(2\pi)\xi = -\xi$ flips sign under one turn. In quaternions $A(\theta) = \cos\tfrac\theta2\,\mathbf 1 + \sin\tfrac\theta2\,\mathbf k$, and conjugation $q\mathbf v q^{-1}$ rotates $\mathbf v$ by $\theta$ about $\hat z$, with $q, -q$ giving the same rotation. $\blacksquare$

---

# Key Takeaways

**A diagonal generator makes the spinor map a phase rotation of the off-diagonal entry.** When the rotation axis is a coordinate axis, the $SU(2)$ matrix is diagonal and the congruence does something transparent: it leaves the diagonal of $\underline X$ alone (fixing the time and the axis direction) and multiplies the off-diagonal entry — which *is* the complex coordinate $x^1 - ix^2$ of the perpendicular plane — by a phase. Seeing the off-diagonal entry as a complex number whose phase rotation is the spatial rotation is the reusable trick; it bypasses all trigonometric expansion and shows directly why a half-angle in the matrix produces a full angle in the plane (each of the two factors of $A$ contributes $e^{-i\theta/2}$, multiplying to $e^{-i\theta}$). Whenever a rotation is about a coordinate axis, diagonalise and watch the off-diagonal phase; the rotation reads off immediately.

**The period mismatch $2\pi$ vs $4\pi$ is the double cover made visible in one parameter.** Running $\theta$ from $0$ to $4\pi$ traces a path in $SU(2)$ that covers the rotation about $\hat z$ *twice*: at $\theta = 2\pi$ the rotation is back to the identity but the matrix is at $-I$, and only at $\theta = 4\pi$ does the matrix return. This single one-parameter computation is the most economical demonstration of the entire double-cover theorem — it shows the fibre $\{A, -A\}$, the noncontractible loop in $SO(3)$ (the $\theta \in [0,2\pi]$ path, which lifts to a non-closed path $I \to -I$), and the spinor's sign flip, all at once. When you want to *see* a double cover rather than prove it abstractly, find a one-parameter subgroup and watch how many times the base is traversed before the cover closes; here it is twice.

**Quaternion conjugation $\mathbf v \mapsto q\mathbf v q^{-1}$ is the spinor map in disguise, and it is what graphics engines compute.** The abstract congruence $A\underline X A^\dagger$, restricted to the traceless (spatial) part and rewritten in quaternions, is the classical "rotate a vector by conjugating with a unit quaternion." This is not a separate fact — it is the same $SU(2) \to SO(3)$ map, with $A^\dagger = q^{-1}$ for a unit quaternion — but it is the form used in practice, because composing rotations becomes quaternion multiplication ($q_1 q_2$) rather than $3\times 3$ matrix multiplication, which is cheaper, numerically stabler, and free of gimbal lock. The double cover that this exercise exhibits ($q$ and $-q$ giving the same rotation) is a daily concern for the programmer, who must choose the sign for smooth interpolation. The transferable point: the same mathematical object wears a "physics" face (the spinor map) and an "engineering" face (quaternion rotation), and recognising they are identical lets insight flow both ways.
