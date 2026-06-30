---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Lie Algebra sl(2,C) and the Exponential Map"
  - "Def - The Spinor Map and SL(2,C)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Problem Statement

Consider the Hermitian $SL(2,\mathbb{C})$ matrix $A(\psi) = \exp\!\big(\tfrac{\psi}{2}\sigma_3\big)$ for a boost of rapidity $\psi$ along the $z$-axis.

1. Compute $A(\psi)$ in closed form and verify $A(\psi) \in SL(2,\mathbb{C})$ and is Hermitian (not unitary).
2. Compute its action by the [[Def - The Spinor Map and SL(2,C)|spinor map]], $\underline X \mapsto A(\psi)\underline X A(\psi)^\dagger$, and show $\mathscr{S}(A(\psi))$ is the Lorentz boost $t' = \cosh\psi\,t + \sinh\psi\,z$, $z' = \sinh\psi\,t + \cosh\psi\,z$, fixing $x, y$.
3. Show why a *Hermitian* (rather than unitary) matrix is required: a unitary matrix fixes the time direction, so it cannot produce a boost. Identify the eigenvalues of $A(\psi)$ and relate them to the Doppler/redshift factors $e^{\pm\psi}$.
4. (General axis.) Write down, without recomputing, the $SL(2,\mathbb{C})$ matrix for a boost of rapidity $\psi$ along a general unit axis $\mathbf n$, and state the corresponding generator in $\mathfrak{sl}(2,\mathbb{C})$.

**Recall:**

![[Def - Lie Algebra sl(2,C) and the Exponential Map#The Definition]]

A boost of rapidity $\psi$ has velocity $\beta = \tanh\psi$, with $\cosh\psi = \gamma$ and $\sinh\psi = \gamma\beta$. The [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|correspondence]] sends $X$ to $\underline X = x^\mu\sigma_\mu$. A boost is the [[Def - The Spinor Map and SL(2,C)|image]] under $\mathscr{S}$ of a Hermitian $SL(2,\mathbb{C})$ element; the sign convention for $\psi$ matches Gourgoulhon ($A = \exp(+\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma)$ boosts the vector), Tong's passive convention uses $A = \exp(-\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma)$.

---

# Convergent Strategy

**Problem class.** A *concrete boost computation* — the boost counterpart of the rotation exercise, showing that the non-unitary (Hermitian) elements of $SL(2,\mathbb{C})$ are exactly the boosts. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Problem-Solving Strategy|topic strategy]] says to diagnose the type from unitary versus Hermitian; this exercise establishes the Hermitian-equals-boost half.

**Assumption pattern.** The generator $\sigma_3$ is again diagonal, but now multiplied by a *real* coefficient $\psi/2$ rather than imaginary, so the exponential gives real exponentials $e^{\pm\psi/2}$ rather than phases — the matrix is Hermitian, not unitary, and this is precisely what lets it touch the time component. The signpost is the absence of the $i$ in the exponent.

**Theorem routing.** This applies the boost formula of [[Def - Lie Algebra sl(2,C) and the Exponential Map|the exponential-map page]] and the congruence action of [[Def - The Spinor Map and SL(2,C)|the spinor map]]. Part 3 invokes the structural fact from [[Thm - The Spinor Map SU(2) to SO(3)]] that unitarity fixes time, contrasting it with the present Hermitian case.

**Key decision point.** The crux is the same off-diagonal/diagonal split as for rotations, but now reversed: the *diagonal* entries of $\underline X$ (which carry $t \pm z$) are scaled by $e^{\pm\psi}$, while the off-diagonal entries ($x \mp iy$) are untouched. Recognising that scaling $t + z$ by $e^{\psi}$ and $t - z$ by $e^{-\psi}$ is precisely the rapidity form of the boost (the light-cone coordinates $t \pm z$ are the boost eigenvectors) is what makes the answer immediate. The contrast with the rotation case — diagonal scaling versus off-diagonal phase — is the whole lesson.

---

# Legal Operations Used

1. **Exponentiate a generator to build the group element** (operation 4 from the topic page): part 1 computes $A(\psi) = \exp(\tfrac\psi2\sigma_3)$ via $\sigma_3^2 = I$, giving $\cosh\tfrac\psi2 I + \sinh\tfrac\psi2\sigma_3$.

2. **Act by congruence $\underline X \mapsto A\underline X A^\dagger$** (operation 2 from the topic page): part 2 conjugates $\underline X$ by the Hermitian $A(\psi)$.

3. **Diagnose the type from unitary versus Hermitian** (operation 5 from the topic page): part 3 contrasts the Hermitian boost with the unitary rotation, explaining why only the former touches time.

---

# Hints

> [!note]- Hint 1
> Since $\sigma_3$ is diagonal, $\exp(\tfrac\psi2\sigma_3) = \mathrm{diag}(e^{\psi/2}, e^{-\psi/2})$. Equivalently $\cosh\tfrac\psi2 I + \sinh\tfrac\psi2\sigma_3$ using $\sigma_3^2 = I$. Check $A^\dagger = A$ (Hermitian, since the entries are real) and $\det A = e^{\psi/2}e^{-\psi/2} = 1$.

> [!note]- Hint 2
> Conjugating $\underline X = \begin{pmatrix}t+z & x-iy\\x+iy & t-z\end{pmatrix}$ by the *diagonal* $A = \mathrm{diag}(e^{\psi/2}, e^{-\psi/2})$ multiplies the $(1,1)$ entry $t+z$ by $e^{\psi}$, the $(2,2)$ entry $t-z$ by $e^{-\psi}$, and leaves the off-diagonal entries (and so $x, y$) unchanged.

> [!note]- Hint 3
> From $t' + z' = e^{\psi}(t+z)$ and $t' - z' = e^{-\psi}(t-z)$, add and subtract: $t' = \cosh\psi\,t + \sinh\psi\,z$ and $z' = \sinh\psi\,t + \cosh\psi\,z$. The eigenvalues of $A$, $e^{\pm\psi/2}$, square to the boost eigenvalues $e^{\pm\psi}$ acting on the null directions $t \pm z$ — the Doppler factors.

> [!note]- Hint 4
> Replace $\sigma_3$ by $\mathbf n\cdot\boldsymbol\sigma$: $A(\psi, \mathbf n) = \exp(\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma) = \cosh\tfrac\psi2 I + \sinh\tfrac\psi2\,(\mathbf n\cdot\boldsymbol\sigma)$, with generator $\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma \in \mathfrak{sl}(2,\mathbb{C})$.

---

# Solution

The exercise runs the boost machinery on the $z$-axis, the mirror of the rotation exercise. The plan: exponentiate the diagonal generator with a *real* coefficient to get the Hermitian $A(\psi) = \mathrm{diag}(e^{\psi/2}, e^{-\psi/2})$; conjugate $\underline X$ and observe the *diagonal* entries $t \pm z$ scale by $e^{\pm\psi}$, which is the rapidity boost; explain why Hermitian (not unitary) is needed; and generalise the axis.

**Step 1: $A(\psi) = \mathrm{diag}(e^{\psi/2}, e^{-\psi/2})$, Hermitian, in $SL(2,\mathbb{C})$.**

> [!note]- Derivation
> Since $\sigma_3$ is diagonal,
> $$A(\psi) = \exp\!\Big(\tfrac{\psi}{2}\sigma_3\Big) = \begin{pmatrix}e^{\psi/2} & 0 \\ 0 & e^{-\psi/2}\end{pmatrix},$$
> equivalently $\cosh\tfrac\psi2 I + \sinh\tfrac\psi2\sigma_3$ (using $\sigma_3^2 = I$, so the even powers sum to $\cosh\tfrac\psi2 I$ and the odd to $\sinh\tfrac\psi2\sigma_3$). The entries are real, so $A^\dagger = A^{\mathsf T} = A$ — **Hermitian**, and *not* unitary (since $A^\dagger = A \neq A^{-1} = \mathrm{diag}(e^{-\psi/2}, e^{\psi/2})$ unless $\psi = 0$). The determinant is $e^{\psi/2}\cdot e^{-\psi/2} = 1$, so $A(\psi) \in SL(2,\mathbb{C})$.

**Step 2: $\mathscr{S}(A(\psi))$ is the boost of rapidity $\psi$ along $z$.**

> [!note]- Derivation
> Conjugate (with $A^\dagger = A$ Hermitian):
> $$A\underline X A^\dagger = \begin{pmatrix}e^{\psi/2} & 0 \\ 0 & e^{-\psi/2}\end{pmatrix}\begin{pmatrix}t+z & x-iy \\ x+iy & t-z\end{pmatrix}\begin{pmatrix}e^{\psi/2} & 0 \\ 0 & e^{-\psi/2}\end{pmatrix} = \begin{pmatrix}e^{\psi}(t+z) & x-iy \\ x+iy & e^{-\psi}(t-z)\end{pmatrix}.$$
> The $(1,1)$ entry scales by $e^{\psi/2}\cdot e^{\psi/2} = e^{\psi}$, the $(2,2)$ by $e^{-\psi}$, and the off-diagonal entries by $e^{\psi/2}e^{-\psi/2} = 1$ (unchanged). Reading off the new four-vector: $x, y$ are fixed, and
> $$t' + z' = e^{\psi}(t + z), \qquad t' - z' = e^{-\psi}(t - z).$$
> Adding and subtracting, with $\cosh\psi = \tfrac12(e^\psi + e^{-\psi})$ and $\sinh\psi = \tfrac12(e^\psi - e^{-\psi})$:
> $$t' = \cosh\psi\,t + \sinh\psi\,z, \qquad z' = \sinh\psi\,t + \cosh\psi\,z.$$
> This is the Lorentz boost of rapidity $\psi$ along $z$, with $\gamma = \cosh\psi$ and $\beta = \tanh\psi$ — so $\mathscr{S}(A(\psi))$ is exactly the $z$-boost.

**Step 3: Why Hermitian, and the eigenvalue–Doppler relation.**

> [!note]- Derivation
> A boost *must* change the time component (it relates frames in relative motion), so its $SL(2,\mathbb{C})$ matrix cannot fix the time direction. By [[Thm - The Spinor Map SU(2) to SO(3)|the rotation theorem]], a *unitary* $A$ has $A\sigma_0 A^\dagger = AA^\dagger = I = \sigma_0$, fixing the time axis $e_0$ — so unitary matrices give only rotations. To touch time, $A$ must be non-unitary, and the natural non-unitary $SL(2,\mathbb{C})$ elements are the **Hermitian** ones; here $AA^\dagger = A^2 = \mathrm{diag}(e^\psi, e^{-\psi}) \neq I$, which is exactly the failure to fix $e_0$ that allows the boost.
>
> The eigenvalues of $A(\psi)$ are $e^{\psi/2}$ and $e^{-\psi/2}$, with eigenvectors $\begin{pmatrix}1\\0\end{pmatrix}$ and $\begin{pmatrix}0\\1\end{pmatrix}$. Under the spinor map these square to the boost's action on the null directions: the light-cone coordinate $t + z$ (the forward null direction) is scaled by $e^{\psi}$, and $t - z$ (the backward null direction) by $e^{-\psi}$. These factors $e^{\pm\psi}$ are the **Doppler factors**: a photon travelling in the $+z$ direction has its frequency multiplied by $e^{\psi} = \sqrt{(1+\beta)/(1-\beta)}$ (blueshift if approaching), and one in $-z$ by $e^{-\psi}$ (redshift). The eigenvectors of the $2\times 2$ matrix are the momentum spinors of the two on-axis light rays.

**Step 4: General axis.**

> [!note]- Derivation
> Replacing $\sigma_3$ by the general unit combination $\mathbf n\cdot\boldsymbol\sigma$ (which also squares to $I$), the boost of rapidity $\psi$ along $\mathbf n$ is
> $$A(\psi, \mathbf n) = \exp\!\Big(\tfrac{\psi}{2}\,\mathbf n\cdot\boldsymbol\sigma\Big) = \cosh\tfrac\psi2\,I + \sinh\tfrac\psi2\,(\mathbf n\cdot\boldsymbol\sigma),$$
> a Hermitian matrix with determinant $\cosh^2\tfrac\psi2 - \sinh^2\tfrac\psi2 = 1$. The generator is $B = \tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma \in \mathfrak{sl}(2,\mathbb{C})$ (traceless, since $\mathrm{tr}(\mathbf n\cdot\boldsymbol\sigma) = 0$), and under the differential of the spinor map $\mathscr{S}'(\sigma_i) = 2K_i$ it maps to $\psi\,n^i K_i$, the Lorentz boost generator — confirming $\mathscr{S}(\exp B) = \exp(\psi\,n^i K_i)$.

> [!note]- Complete formal solution
> $A(\psi) = \exp(\tfrac\psi2\sigma_3) = \mathrm{diag}(e^{\psi/2}, e^{-\psi/2})$ is Hermitian with $\det = 1$. Conjugating $\underline X$ scales the diagonal entries $t \pm z$ by $e^{\pm\psi}$ and fixes the off-diagonal ($x, y$), giving $t' = \cosh\psi\,t + \sinh\psi\,z$, $z' = \sinh\psi\,t + \cosh\psi\,z$ — the rapidity-$\psi$ boost along $z$. A Hermitian (not unitary) matrix is required because a unitary one fixes $\sigma_0 = e_0$ and so gives only rotations; here $AA^\dagger = \mathrm{diag}(e^\psi, e^{-\psi}) \neq I$. The eigenvalues $e^{\pm\psi/2}$ square to the Doppler factors $e^{\pm\psi} = \sqrt{(1\pm\beta)/(1\mp\beta)}$ acting on the on-axis null directions $t \pm z$. For a general axis, $A(\psi,\mathbf n) = \cosh\tfrac\psi2 I + \sinh\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma = \exp(\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma)$, generator $\tfrac\psi2\,\mathbf n\cdot\boldsymbol\sigma$. $\blacksquare$

---

# Key Takeaways

**Boost equals diagonal scaling of light-cone coordinates; rotation equals off-diagonal phase — the two are mirror images.** In the $SL(2,\mathbb{C})$ picture, the difference between a boost and a rotation is the difference between a real and an imaginary coefficient in the exponent of $\sigma_3$. A rotation $\exp(-\tfrac{i\theta}{2}\sigma_3)$ has unit-modulus diagonal entries (phases), which leave the diagonal of $\underline X$ — and hence $t, z$ — fixed and rotate the off-diagonal plane $(x,y)$. A boost $\exp(\tfrac\psi2\sigma_3)$ has real positive diagonal entries, which scale the diagonal of $\underline X$ — the light-cone coordinates $t \pm z$ — by $e^{\pm\psi}$ and leave the perpendicular plane fixed. This is the cleanest possible statement of "a boost is a rotation through an imaginary angle": replace $\theta$ by $-i\psi$ and the phase $e^{\pm i\theta/2}$ becomes the real scaling $e^{\pm\psi/2}$. The reusable diagnostic: real exponent of a Pauli matrix means boost (Hermitian, scales light-cone coordinates), imaginary exponent means rotation (unitary, rotates the transverse plane).

**Unitary fixes time, so boosts must be Hermitian — the type of the matrix dictates the type of the motion.** The reason a boost cannot be implemented by a unitary matrix is structural and worth holding onto: $AA^\dagger = I$ means $A\sigma_0 A^\dagger = \sigma_0$, i.e. the time direction is fixed, and a Lorentz transformation fixing the time direction is a spatial rotation. So the unitary subgroup $SU(2)$ exhausts the rotations, and the boosts live entirely among the non-unitary elements, naturally the Hermitian ones. This gives an instant classification tool: handed any $A \in SL(2,\mathbb{C})$, check $AA^\dagger$ — if it is $I$, you have a rotation; if $A = A^\dagger$, a boost; in general, polar-decompose $A = (\text{Hermitian})(\text{unitary})$ to read off the boost-times-rotation factorisation. The transferable principle is that an algebraic property of the matrix (unitary, Hermitian) corresponds to a geometric property of the transformation (rotation, boost), and recognising the correspondence saves computing the full $4\times 4$ matrix.

**The eigenvalues of the $2\times 2$ boost are the square roots of the Doppler factors.** The Hermitian boost matrix has eigenvalues $e^{\pm\psi/2}$, and these square — through the two factors of $A$ in the congruence — to the factors $e^{\pm\psi}$ by which the on-axis null directions are scaled. Those factors $e^{\pm\psi} = \sqrt{(1\pm\beta)/(1\mp\beta)}$ are exactly the relativistic Doppler shift for light travelling along or against the boost. So the $2\times 2$ eigenvalue problem of the spinor map *is* the Doppler effect: the eigenvectors are the momentum spinors of the forward and backward light rays, and the eigenvalues are the (square roots of the) frequency-shift factors. This is the seed of the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|celestial-sphere]] result, where a boost along the line of sight is the Möbius dilation $\omega \mapsto e^{-\psi}\omega$ — the same $e^{\pm\psi}$ acting on the Riemann sphere as aberration. Recognising the boost's eigenvalues as Doppler factors connects the abstract group element to the measurable frequency shift in one step.
