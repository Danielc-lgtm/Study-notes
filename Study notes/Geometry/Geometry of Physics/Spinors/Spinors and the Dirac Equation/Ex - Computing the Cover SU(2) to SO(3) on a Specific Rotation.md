---
type: exercise
subject: spinors
difficulty: "⭐⭐"
prereqs:
  - "Def - The Pauli Matrices"
  - "Def - SU(2) Action on Spinors"
  - "Thm - SU(2) is the Double Cover of SO(3)"
tags: [geometry, spinors, lie-groups]
---

# Problem Statement

Let $u = \exp(-i\tfrac{\pi}{4}\sigma_3) \in SU(2)$. Compute $u$ explicitly as a $2 \times 2$ matrix; determine the corresponding rotation $R \in SO(3)$ via the cover $\mathrm{Ad}: SU(2) \to SO(3)$; verify by computing $\mathrm{Ad}_u(\vec e_1)$, $\mathrm{Ad}_u(\vec e_2)$, $\mathrm{Ad}_u(\vec e_3)$ for the standard basis $\vec e_j$ of $\mathbb{R}^3$. Then show that $u^2 = \exp(-i\tfrac{\pi}{2}\sigma_3)$ corresponds to a $\pi$ rotation in $\mathbb{R}^3$ (a single rotation by $\pi$, *not* by $2 \times \pi/2 = \pi$), and that $u^4 = \exp(-i\pi\sigma_3) = -I$ corresponds to a $2\pi$ rotation — the identity in $SO(3)$.

**Recall:**

The cover $\mathrm{Ad}: SU(2) \to SO(3)$ is defined by:

![[Thm - SU(2) is the Double Cover of SO(3)#Statement]]

The Pauli matrices are:

![[Def - The Pauli Matrices#The Definition]]

A rotation about the $z$-axis by angle $\theta$ corresponds in $SU(2)$ to $u(\hat e_3, \theta) = \exp(-i\tfrac{\theta}{2}\sigma_3) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2}\end{pmatrix}$.

---

# Convergent Strategy

**Problem class:** *Direct computation of the $SU(2) \to SO(3)$ cover map on a specific element.* This is a routine exercise in the spinor formalism, exercising the explicit construction of the cover via conjugation by the Pauli matrices.

**Assumption pattern:** We are given a specific $u \in SU(2)$ written in the form $\exp(-i\theta\sigma_3/2)$, signalling that $u$ is a $\pi/2$-rotation-spinor about the $z$-axis. The exponent and the Pauli matrix involved together encode the axis (here $\hat e_3$) and angle (here $\pi/2$) of the corresponding $SO(3)$ rotation.

**Theorem routing:** Use the formula $u(\hat n, \theta) = \exp(-i\tfrac{\theta}{2}\vec\sigma\cdot\hat n)$ from [[Thm - SU(2) is the Double Cover of SO(3)]] to identify the rotation directly; verify by explicit conjugation $\mathrm{Ad}_u(\vec e_j \cdot \vec\sigma) = u(\vec e_j \cdot \vec\sigma)u^{-1}$, using $\sigma_j \sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$ from [[Def - The Pauli Matrices]] for the matrix products.

**Key decision point:** The non-obvious part is recognizing the factor of $\tfrac{1}{2}$ in the exponent — a spinor rotation by angle $\theta$ corresponds to a vector rotation by *twice* the angle, $2\theta$. So $u = \exp(-i\tfrac{\pi}{4}\sigma_3)$ does *not* correspond to a $\pi/4$ rotation but to a $\pi/2$ rotation. This factor of $2$ is the geometric content of "spin-$\tfrac{1}{2}$" and is the source of the $4\pi$-periodicity.

---

# Legal Operations Used

1. **Operation 2 from the topic page (express a rotation as conjugation by an $SU(2)$ element):** The formula $u(\hat n, \theta) = \exp(-i\tfrac{\theta}{2}\vec\sigma \cdot \hat n) = \cos(\theta/2)I - i\sin(\theta/2)\vec\sigma\cdot\hat n$ converts a rotation axis and angle directly into an $SU(2)$ matrix. In this exercise, $\hat n = \hat e_3$ and $\theta = \pi/2$, giving $u = \cos(\pi/4)I - i\sin(\pi/4)\sigma_3 = \tfrac{1}{\sqrt 2}(I - i\sigma_3)$.

2. **Operation 1 from the topic page (use the Pauli product identity):** To compute $\mathrm{Ad}_u(\vec e_j \cdot \vec\sigma) = u(\vec e_j \cdot \vec\sigma)u^{-1}$, expand using $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$ and track each Pauli term. In particular, $\sigma_3 \sigma_j \sigma_3^{-1} = \pm\sigma_j$ depending on whether $\sigma_j$ commutes or anticommutes with $\sigma_3$ ($\sigma_3$ commutes with itself, anticommutes with $\sigma_1, \sigma_2$).

---

# Hints

> [!note]- Hint 1
> The formula $u(\hat n, \theta) = \exp(-i\tfrac{\theta}{2}\vec\sigma\cdot\hat n)$ tells you: rotation by $\theta$ in $\mathbb{R}^3$ corresponds to multiplication by $\exp(-i\theta\vec\sigma\cdot\hat n/2)$ on spinors. Here $-i\tfrac{\pi}{4}\sigma_3$ corresponds to half-angle $\pi/4$, hence vector-angle $\pi/2$.

> [!note]- Hint 2
> To verify the cover, compute $u(\vec e_j \cdot \vec\sigma)u^{-1}$ for $j = 1, 2, 3$. Use $u\sigma_j u^{-1}$ formulas: $u = \exp(-i\tfrac{\pi}{4}\sigma_3)$ commutes with $\sigma_3$ (so $u\sigma_3 u^{-1} = \sigma_3$); for $\sigma_1, \sigma_2$, use the anticommutation $\{\sigma_3, \sigma_j\} = 0$ for $j = 1, 2$ to deduce the action.

> [!note]- Hint 3
> An efficient approach: $u\sigma_1 u^{-1} = u\sigma_1 u^* = (\cos(\pi/4)I - i\sin(\pi/4)\sigma_3)\sigma_1(\cos(\pi/4)I + i\sin(\pi/4)\sigma_3)$. Expand using $\sigma_3\sigma_1 = i\sigma_2$ and $\sigma_1\sigma_3 = -i\sigma_2$. The result should be $\sigma_2$ — i.e., $\vec e_1$ rotates to $\vec e_2$ under the corresponding rotation, consistent with a $\pi/2$ rotation about $\hat e_3$.

---

# Solution

The proof breaks into three steps. Step 1 computes $u$ explicitly as a matrix and identifies it with the half-angle $\pi/4$ rotation-spinor about $\hat e_3$. Step 2 verifies by direct conjugation that the corresponding $SO(3)$ rotation is the standard $\pi/2$ rotation about $\hat e_3$. Step 3 computes $u^2, u^4$ and identifies their geometric meaning, demonstrating the $4\pi$-periodicity of spinors.

**Step 1: Compute $u = \exp(-i\tfrac{\pi}{4}\sigma_3)$ explicitly.**

The matrix $u$ is the spin-$\tfrac{1}{2}$ representation of a $\pi/2$-rotation about $\hat e_3$.

> [!note]- Derivation
> Using $\sigma_3 = \mathrm{diag}(1, -1)$:
> $$\exp(-i\tfrac{\pi}{4}\sigma_3) = \exp(\mathrm{diag}(-i\pi/4, +i\pi/4)) = \mathrm{diag}(e^{-i\pi/4}, e^{+i\pi/4}) = \mathrm{diag}\left(\tfrac{1 - i}{\sqrt 2}, \tfrac{1 + i}{\sqrt 2}\right).$$
> 
> Alternatively, using the general formula $\exp(-i\tfrac{\theta}{2}\vec\sigma\cdot\hat n) = \cos(\theta/2)I - i\sin(\theta/2)\vec\sigma\cdot\hat n$ with $\theta = \pi/2$, $\hat n = \hat e_3$:
> $$u = \cos(\pi/4)I - i\sin(\pi/4)\sigma_3 = \tfrac{1}{\sqrt 2}(I - i\sigma_3) = \tfrac{1}{\sqrt 2}\begin{pmatrix} 1 - i & 0 \\ 0 & 1 + i\end{pmatrix},$$
> matching the direct calculation. So $u$ is a diagonal unitary matrix with diagonal entries $(1 \mp i)/\sqrt 2$.
>
> Geometrically: the formula identifies this as the rotation-spinor for a vector rotation by $2 \cdot (\pi/4) = \pi/2$ about $\hat e_3$.

**Step 2: Verify the corresponding $SO(3)$ rotation by computing $\mathrm{Ad}_u(\vec e_j)$ for $j = 1, 2, 3$.**

The $SO(3)$ rotation is $R = R_z(\pi/2)$, the standard $\pi/2$-rotation about the $z$-axis: $R\vec e_1 = \vec e_2$, $R\vec e_2 = -\vec e_1$, $R\vec e_3 = \vec e_3$.

> [!note]- Derivation
> By the theorem, $\mathrm{Ad}_u(\vec e_j) \cdot \vec\sigma = u(\vec e_j \cdot \vec\sigma)u^{-1} = u\sigma_j u^{-1}$, so we compute each $u\sigma_j u^{-1}$:
>
> *Case $j = 3$ (the rotation axis).* Since $u = \exp(-i\tfrac{\pi}{4}\sigma_3)$ is a function of $\sigma_3$, $u$ commutes with $\sigma_3$, so $u\sigma_3 u^{-1} = \sigma_3$. So $\mathrm{Ad}_u(\vec e_3) = \vec e_3$ — the rotation axis is fixed, as expected.
>
> *Case $j = 1$.* Use $u\sigma_1 = \exp(-i\tfrac{\pi}{4}\sigma_3)\sigma_1$. Since $\{\sigma_3, \sigma_1\} = 0$, we have $\sigma_3\sigma_1 = -\sigma_1\sigma_3$, so $\sigma_3^k\sigma_1 = \sigma_1(-\sigma_3)^k$, hence $\exp(-i\tfrac{\pi}{4}\sigma_3)\sigma_1 = \sigma_1\exp(+i\tfrac{\pi}{4}\sigma_3)$ (the $\sigma_3$ flips sign across $\sigma_1$). Therefore
> $$u\sigma_1 u^{-1} = \sigma_1 \exp(+i\tfrac{\pi}{4}\sigma_3) \exp(+i\tfrac{\pi}{4}\sigma_3) = \sigma_1 \exp(+i\tfrac{\pi}{2}\sigma_3) = \sigma_1 \cdot i\sigma_3 = i\sigma_1\sigma_3 = i(-i\sigma_2) = \sigma_2.$$
> So $\mathrm{Ad}_u(\vec e_1) = \vec e_2$ — the $x$-axis rotates to the $y$-axis. ✓
>
> *Case $j = 2$.* Similarly $\{\sigma_3, \sigma_2\} = 0$, so $u\sigma_2 u^{-1} = \sigma_2 \exp(+i\tfrac{\pi}{2}\sigma_3) = \sigma_2 \cdot i\sigma_3 = i\sigma_2\sigma_3 = i(i\sigma_1) = -\sigma_1$. So $\mathrm{Ad}_u(\vec e_2) = -\vec e_1$ — the $y$-axis rotates to the negative $x$-axis. ✓
>
> Conclusion: the rotation $R = \mathrm{Ad}_u$ acts as $\vec e_1 \mapsto \vec e_2$, $\vec e_2 \mapsto -\vec e_1$, $\vec e_3 \mapsto \vec e_3$ — the standard $\pi/2$ rotation about $\hat e_3$, matching the prediction.

**Step 3: Compute $u^2$ and $u^4$, identify their geometric meaning.**

$u^2 = \exp(-i\tfrac{\pi}{2}\sigma_3)$ corresponds to a $\pi$-rotation; $u^4 = \exp(-i\pi\sigma_3) = -I$ corresponds to a $2\pi$ rotation, which is the identity in $SO(3)$ but $-I$ in $SU(2)$.

> [!note]- Derivation
> $u^2 = \exp(-i\tfrac{\pi}{4}\sigma_3) \cdot \exp(-i\tfrac{\pi}{4}\sigma_3) = \exp(-i\tfrac{\pi}{2}\sigma_3) = \cos(\pi/2)I - i\sin(\pi/2)\sigma_3 = -i\sigma_3 = \mathrm{diag}(-i, +i)$.
>
> Corresponding rotation: $R(\hat e_3, \pi)$ — a $\pi$-rotation about $\hat e_3$. We have $\mathrm{Ad}_{u^2}(\vec e_1) = -\vec e_1$, $\mathrm{Ad}_{u^2}(\vec e_2) = -\vec e_2$, $\mathrm{Ad}_{u^2}(\vec e_3) = \vec e_3$ — consistent with a $\pi$ rotation about the $z$-axis.
>
> $u^4 = (u^2)^2 = (-i\sigma_3)^2 = -\sigma_3^2 = -I$. Corresponding rotation: $R(\hat e_3, 2\pi) = I \in SO(3)$ — the identity rotation. But in $SU(2)$, $u^4 = -I \neq I$ — the spinor has picked up a phase of $-1$ after a $2\pi$ rotation. Going around twice more (i.e., $u^8 = +I$) returns the spinor to itself, consistent with the $4\pi$-periodicity of spinors.

> [!note]- Complete formal solution
> Let $u = \exp(-i\tfrac{\pi}{4}\sigma_3) \in SU(2)$.
>
> By the formula $\exp(-i\tfrac{\theta}{2}\vec\sigma\cdot\hat n) = \cos(\theta/2)I - i\sin(\theta/2)\vec\sigma\cdot\hat n$ applied with $\theta = \pi/2$, $\hat n = \hat e_3$: $u = \cos(\pi/4)I - i\sin(\pi/4)\sigma_3 = \tfrac{1}{\sqrt 2}(I - i\sigma_3) = \tfrac{1}{\sqrt 2}\begin{pmatrix} 1-i & 0 \\ 0 & 1+i\end{pmatrix}$.
>
> The corresponding $SO(3)$ rotation $R = \mathrm{Ad}_u$ is determined by computing $u\sigma_j u^{-1}$ for $j = 1, 2, 3$. Since $u$ commutes with $\sigma_3$, $\mathrm{Ad}_u(\vec e_3) = \vec e_3$. For $j = 1, 2$, the anticommutation $\{\sigma_3, \sigma_j\} = 0$ implies $u\sigma_j = \sigma_j u^{-1}$, hence $u\sigma_j u^{-1} = \sigma_j u^{-2} = \sigma_j \exp(+i\tfrac{\pi}{2}\sigma_3) = i\sigma_j\sigma_3$. Using $\sigma_1\sigma_3 = -i\sigma_2$ and $\sigma_2\sigma_3 = i\sigma_1$: $u\sigma_1 u^{-1} = \sigma_2$, $u\sigma_2 u^{-1} = -\sigma_1$. So $R\vec e_1 = \vec e_2$, $R\vec e_2 = -\vec e_1$, $R\vec e_3 = \vec e_3$ — the $\pi/2$-rotation about $\hat e_3$.
>
> Higher powers: $u^2 = \exp(-i\tfrac{\pi}{2}\sigma_3) = -i\sigma_3$, corresponding to the $\pi$-rotation about $\hat e_3$. $u^4 = -I$, corresponding to $R(\hat e_3, 2\pi) = I$ in $SO(3)$ — the $2\pi$-rotation that fixes vectors but multiplies spinors by $-1$. $u^8 = I$, the $4\pi$-rotation that returns spinors to themselves.

> [!warning] Illegal but tempting alternative route: matrix exponential by hand
> One could try to compute $\exp(-i\tfrac{\pi}{4}\sigma_3)$ by writing out the matrix exponential as a power series $\sum (-i\tfrac{\pi}{4})^k \sigma_3^k / k!$. This works but is tedious; the *cleaner* route uses $\sigma_3^2 = I$ to terminate the series after even and odd terms: $\exp(-it\sigma_3) = \cos(t) I - i\sin(t)\sigma_3$. The general formula $\exp(-i\theta\vec\sigma\cdot\hat n/2) = \cos(\theta/2) I - i\sin(\theta/2)\vec\sigma\cdot\hat n$ encapsulates this pattern; deploying it directly is the fluent move.

---

# Key Takeaways

**The factor of $\tfrac{1}{2}$ in $u(\hat n, \theta) = \exp(-i\tfrac{\theta}{2}\vec\sigma\cdot\hat n)$ is the spin-$\tfrac{1}{2}$ name.** A rotation by angle $\theta$ in $\mathbb{R}^3$ corresponds to multiplication by $\exp(-i\theta\vec\sigma\cdot\hat n/2)$ on spinors — i.e., spinors rotate at *half* the rate of vectors. So an electron's wave function, when its laboratory frame is rotated by $\pi/2$, picks up only a "half-rotation" phase $e^{-i\pi/4}$ — and only when the lab rotates by $4\pi$ (the *spinor* picks up phase $e^{-i\pi \cdot 2} = +1$) does the wave function return to itself. The slogan "spinors rotate at half speed" captures this: it is the physical face of the $2:1$ cover, and is the source of all the strange $4\pi$-periodic behaviour of spin-$\tfrac{1}{2}$ particles. Every time you see the half-angle convention in physics — Euler angles, spinor parameterizations, quaternion rotations — this is the underlying fact.

**The Pauli identity $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$ is the master tool for all spinor calculations.** Every conjugation $u\sigma_j u^{-1}$, every product $\sigma_a\sigma_b\sigma_c$, every commutator and anticommutator reduces to this single identity. The strategy in this exercise — pushing $u$ through $\sigma_1$ to get $\sigma_1 u^{-1}$ using anticommutation, then absorbing the $u^{-1}$ into $u^{-2} = \exp(i\pi\sigma_3/2) = i\sigma_3$ — is a model calculation. When you see $\exp$-of-Pauli factors and need to manipulate them, the routine is: use $(\vec\sigma\cdot\hat n)^2 = I$ to terminate the exponential into $\cos + i\sin$ form, then use the product identity to simplify.

**The $4\pi$-periodicity is a topological fact accessible by direct calculation.** Computing $u^2$ as the $\pi$-rotation spinor and $u^4 = -I$ as the $2\pi$-rotation spinor (which the $SO(3)$ rotation sees as $+I$) shows the topological $\mathbb{Z}/2$ ambiguity in the cover $SU(2) \to SO(3)$ in action: $\pm u^2$ both project to the same $SO(3)$ rotation, but only their squares (the $4\pi$-rotation spinors) coincide. This is the explicit version of $\pi_1(SO(3)) = \mathbb{Z}/2$, made concrete in a single exercise. Compare with [[Ex - SU(2) is Diffeomorphic to S^3]] for the topological side.
