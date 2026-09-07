---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Berry Phase Equals Holonomy of the Berry Connection"
  - "Def - Berry Connection"
tags: [geometry, gauge-theory, quantum-mechanics, berry-phase]
---

# Prerequisite Concepts

- [[Thm - Berry Phase Equals Holonomy of the Berry Connection]]
- [[Def - Berry Connection]]

# Problem Statement

A spin-$\tfrac{1}{2}$ particle in a magnetic field $\mathbf{B}$ has Hamiltonian
$$H(\mathbf{B}) = -\mu\,\mathbf{B}\cdot\hat\sigma/2 = -\frac{\mu}{2}(B_x\hat\sigma_x + B_y\hat\sigma_y + B_z\hat\sigma_z),$$
where $\hat\sigma = (\hat\sigma_x, \hat\sigma_y, \hat\sigma_z)$ are the Pauli matrices and $\mu > 0$ is the magnetic moment. Fix $|\mathbf{B}| = B$ constant (so only the direction $\hat n = \mathbf{B}/B \in S^2$ varies).

Let $\hat n(t)$ trace a closed loop $C$ on the unit sphere $S^2$ of directions, in the adiabatic limit. Show that the Berry phase accumulated by the lowest-energy eigenstate around $C$ is
$$\gamma(C) = -\frac{1}{2}\Omega(C),$$
where $\Omega(C)$ is the **solid angle** subtended by $C$ on $S^2$ (i.e., the area enclosed by $C$ on the unit sphere, with $0 \leq \Omega \leq 4\pi$).

**Recall:**

![[Thm - Berry Phase Equals Holonomy of the Berry Connection#Statement]]

![[Def - Berry Connection#The Definition]]

The Pauli matrices: $\hat\sigma_x = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$, $\hat\sigma_y = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}$, $\hat\sigma_z = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$. They satisfy $\hat\sigma_a\hat\sigma_b = \delta_{ab}I + i\epsilon_{abc}\hat\sigma_c$. The eigenvalues of $\hat n \cdot \hat\sigma$ are $\pm 1$, with eigenstates $|\pm\hat n\rangle$.

The lowest-energy eigenvalue of $H(\mathbf{B})$ is $-\mu B/2$, with eigenstate $|+\hat n\rangle$ (the "+1" eigenstate of $\hat n\cdot\hat\sigma$, since $H = -\mu B \hat n\cdot\hat\sigma/2$).

In spherical coordinates $\hat n = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$, an explicit form of the eigenstate is $|+\hat n\rangle = \begin{pmatrix}\cos(\theta/2) \\ \sin(\theta/2)e^{i\phi}\end{pmatrix}$.

---

# Convergent Strategy

**Problem class:** *Explicit computation of a Berry phase for an experimentally observable system.* The topic-page strategy is "compute the Berry connection in coordinates, integrate around the loop".

**Assumption pattern:** The key assumption is the **adiabatic limit**: $|\mathbf{B}|$ is large enough that the energy gap $\mu B$ between the two eigenvalues is much larger than the rate $\|\dot{\hat n}\|$ of parameter change. In this limit, [[Thm - Berry Phase Equals Holonomy of the Berry Connection]] applies.

**Theorem routing:** The Berry phase is $\gamma(C) = i\oint_C \omega$ where $\omega = \langle+\hat n, d|+\hat n\rangle$. Compute $\omega$ in spherical coordinates, get $\omega = -i\sin^2(\theta/2)\,d\phi$, integrate around $C$, use Stokes to convert to surface integral, recognize result as half the solid angle.

**Key decision point:** The non-obvious step is recognizing that the **half-solid-angle** answer reflects the **double-cover** of $\mathrm{SO}(3)$ by $\mathrm{SU}(2)$: a spin-$\tfrac{1}{2}$ is acted on by $\mathrm{SU}(2)$ (which is the *double cover* of $\mathrm{SO}(3)$, the rotation group acting on physical space), and a full rotation in physical space gives a *half*-rotation in spin space. This is what makes the Berry phase "half" the solid angle.

---

# Legal Operations Used

1. **Operation 9 from the topic page (Integrate around a small loop to detect curvature).** Apply: compute the Berry curvature $\theta = d\omega$ first, then integrate over the bounding surface; gives the answer via Stokes.

2. **Operation 4 from the topic page (Pfaffian / invariant polynomial of curvature).** Apply: the curvature $\theta$ for the spin-$\tfrac{1}{2}$ Berry line bundle is a globally defined 2-form on $S^2$, and integrating over the full $S^2$ gives the first Chern number (here, $\frac{i}{2\pi}\int_{S^2}\theta = -1/2$... wait that's not integer; see calibration).

3. **Operation 2 from the topic page (Lift to principal bundle).** Apply: the Hopf bundle structure $S^3 \to S^2$ underlies the geometry — the spin-$\tfrac{1}{2}$ Hilbert space $\mathbb{C}^2$ has the unit sphere $S^3$, projectivized to $\mathbb{CP}^1 = S^2 =$ space of physical states. The Berry connection is exactly the Hopf-bundle connection.

---

# Hints

> [!note]- Hint 1
> Write the lowest-energy eigenstate $|+\hat n\rangle = (\cos(\theta/2), \sin(\theta/2)e^{i\phi})^T$ in spherical coordinates. Verify $\hat n\cdot\hat\sigma|+\hat n\rangle = +|+\hat n\rangle$.

> [!note]- Hint 2
> Compute $\omega = \langle+\hat n | d|+\hat n\rangle\rangle$. The derivative is $d|+\hat n\rangle =$ partial derivatives in $\theta$ and $\phi$. Result: $\omega = i\sin^2(\theta/2)d\phi$ (a pure-imaginary 1-form on the parameter $S^2$, with a singularity at the south pole $\theta = \pi$).

> [!note]- Hint 3
> Compute $\theta = d\omega = i\sin(\theta/2)\cos(\theta/2)d\theta\wedge d\phi = (i/2)\sin\theta\,d\theta\wedge d\phi$.

> [!note]- Hint 4
> For a loop $C = \partial S$ bounding a surface $S$ on $S^2$, $\gamma(C) = i\oint_C\omega = i\int_S\theta = (i)(i/2)\int_S\sin\theta\,d\theta\wedge d\phi = -(1/2)\mathrm{Area}(S) = -(1/2)\Omega(C)$, since $\sin\theta\,d\theta\wedge d\phi$ is the area form on $S^2$.

---

# Solution

The proof has four steps. Step 1 sets up the explicit eigenstate. Step 2 computes the Berry connection 1-form. Step 3 computes the curvature 2-form. Step 4 integrates and identifies the half-solid-angle result. The non-obvious move is in Step 3-4, where the explicit form $\theta = (i/2)\sin\theta\,d\theta\wedge d\phi$ is recognized as "half the area form on $S^2$" — the factor of $1/2$ being the imprint of the $\mathrm{SU}(2) \to \mathrm{SO}(3)$ double cover on the geometry.

**Step 1: Explicit eigenstate.**

The lowest-energy eigenstate of $H(\mathbf{B}) = -(\mu B/2)\hat n\cdot\hat\sigma$ (with $\hat n = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$) is the "+1" eigenstate of $\hat n\cdot\hat\sigma$, namely
$$|+\hat n\rangle = \begin{pmatrix}\cos(\theta/2) \\ e^{i\phi}\sin(\theta/2)\end{pmatrix}.$$

> [!note]- Derivation
> Compute $\hat n\cdot\hat\sigma = \sin\theta\cos\phi\,\hat\sigma_x + \sin\theta\sin\phi\,\hat\sigma_y + \cos\theta\,\hat\sigma_z = \begin{pmatrix}\cos\theta & \sin\theta\,e^{-i\phi} \\ \sin\theta\,e^{i\phi} & -\cos\theta\end{pmatrix}$.
>
> Verify: $\hat n\cdot\hat\sigma \begin{pmatrix}\cos(\theta/2) \\ e^{i\phi}\sin(\theta/2)\end{pmatrix} = \begin{pmatrix}\cos\theta\cos(\theta/2) + \sin\theta\,e^{-i\phi}\cdot e^{i\phi}\sin(\theta/2) \\ \sin\theta\,e^{i\phi}\cos(\theta/2) - \cos\theta\cdot e^{i\phi}\sin(\theta/2)\end{pmatrix} = \begin{pmatrix}\cos\theta\cos(\theta/2) + \sin\theta\sin(\theta/2) \\ e^{i\phi}[\sin\theta\cos(\theta/2) - \cos\theta\sin(\theta/2)]\end{pmatrix}$.
>
> Use $\cos\theta = \cos^2(\theta/2) - \sin^2(\theta/2)$, $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$. Top entry: $(\cos^2(\theta/2) - \sin^2(\theta/2))\cos(\theta/2) + 2\sin(\theta/2)\cos(\theta/2)\sin(\theta/2) = \cos^3(\theta/2) - \sin^2(\theta/2)\cos(\theta/2) + 2\sin^2(\theta/2)\cos(\theta/2) = \cos^3(\theta/2) + \sin^2(\theta/2)\cos(\theta/2) = \cos(\theta/2)(\cos^2(\theta/2) + \sin^2(\theta/2)) = \cos(\theta/2)$. ✓
>
> Bottom entry: $e^{i\phi}[2\sin(\theta/2)\cos^2(\theta/2) - (\cos^2(\theta/2)-\sin^2(\theta/2))\sin(\theta/2)] = e^{i\phi}\sin(\theta/2)[2\cos^2(\theta/2) - \cos^2(\theta/2) + \sin^2(\theta/2)] = e^{i\phi}\sin(\theta/2)[\cos^2(\theta/2)+\sin^2(\theta/2)] = e^{i\phi}\sin(\theta/2)$. ✓
>
> So $\hat n\cdot\hat\sigma |+\hat n\rangle = |+\hat n\rangle$. Eigenvalue $+1$.

**Step 2: Berry connection 1-form.**

$$\omega = \langle+\hat n, d|+\hat n\rangle = i\sin^2(\theta/2)\,d\phi.$$

> [!note]- Derivation
> $d|+\hat n\rangle = \begin{pmatrix}-\tfrac{1}{2}\sin(\theta/2) \\ \tfrac{1}{2}e^{i\phi}\cos(\theta/2)\end{pmatrix}d\theta + \begin{pmatrix}0 \\ ie^{i\phi}\sin(\theta/2)\end{pmatrix}d\phi$.
>
> Inner product $\langle+\hat n| \cdot d|+\hat n\rangle$: $\langle+\hat n|$ is the row $(\cos(\theta/2), e^{-i\phi}\sin(\theta/2))$.
>
> $d\theta$ component: $(\cos(\theta/2))(-\tfrac{1}{2}\sin(\theta/2)) + (e^{-i\phi}\sin(\theta/2))(\tfrac{1}{2}e^{i\phi}\cos(\theta/2)) = -\tfrac{1}{2}\sin(\theta/2)\cos(\theta/2) + \tfrac{1}{2}\sin(\theta/2)\cos(\theta/2) = 0$.
>
> $d\phi$ component: $(\cos(\theta/2)) \cdot 0 + (e^{-i\phi}\sin(\theta/2))(ie^{i\phi}\sin(\theta/2)) = i\sin^2(\theta/2)$.
>
> So $\omega = i\sin^2(\theta/2)\,d\phi$, pure imaginary as expected. (Singular at $\theta = 0$: $\omega = 0$; well-behaved. Singular at $\theta = \pi$ (south pole): $\omega = i \cdot 1 \cdot d\phi$, but $d\phi$ is singular at the poles since $\phi$ is undefined. The gauge choice is well-defined off the south pole; a different gauge is needed at the south pole.)

**Step 3: Berry curvature.**

$$\theta = d\omega = \frac{i}{2}\sin\theta\,d\theta\wedge d\phi.$$

> [!note]- Derivation
> $\omega = i\sin^2(\theta/2)\,d\phi$. Differentiating: $d\omega = i \cdot d(\sin^2(\theta/2)) \wedge d\phi = i \cdot 2\sin(\theta/2)\cos(\theta/2)\,d\theta \wedge d\phi = i\sin\theta\,d\theta\wedge d\phi / 1$... wait, $2\sin(\theta/2)\cos(\theta/2) = \sin\theta$.
>
> So $d\omega = i\sin\theta\,d\theta\wedge d\phi$. Hmm, but I claimed $(i/2)\sin\theta$. Let me redo.
>
> Actually: $\omega = i\sin^2(\theta/2)\,d\phi$, $\frac{d}{d\theta}\sin^2(\theta/2) = 2\sin(\theta/2) \cdot \cos(\theta/2) \cdot (1/2) = \sin(\theta/2)\cos(\theta/2) = (1/2)\sin\theta$. So $d\sin^2(\theta/2) = (1/2)\sin\theta\,d\theta$. Therefore $d\omega = i \cdot (1/2)\sin\theta\,d\theta\wedge d\phi = (i/2)\sin\theta\,d\theta\wedge d\phi$. ✓

**Step 4: Berry phase = half the solid angle.**

For a loop $C = \partial S$ bounding a surface $S$ on $S^2$:
$$\gamma(C) = i\oint_C\omega = i\int_S d\omega = i\int_S \theta = i \cdot \frac{i}{2}\int_S\sin\theta\,d\theta\wedge d\phi = -\frac{1}{2}\Omega(C),$$
where $\Omega(C) = \int_S \sin\theta\,d\theta\wedge d\phi = \mathrm{Area}(S \subset S^2)$ is the solid angle.

> [!note]- Derivation
> By Stokes' theorem on $S^2$ (with the gauge above well-defined off the south pole — strictly, the computation uses a smooth interpolation, or restricts to loops that don't go around the south pole, or uses a different gauge on the south-pole region and tracks the gauge change), $\oint_C \omega = \int_S d\omega = \int_S\theta$.
>
> Apply $\gamma(C) = i\int_S\theta$, with $\theta = (i/2)\sin\theta\,d\theta\wedge d\phi$:
> $$\gamma(C) = i\cdot\frac{i}{2}\int_S\sin\theta\,d\theta\wedge d\phi = -\frac{1}{2}\int_S\sin\theta\,d\theta\wedge d\phi = -\frac{1}{2}\Omega(C).$$
> $\Omega(C) = \int_S\sin\theta\,d\theta\wedge d\phi$ is the standard solid-angle formula: this is the area of $S$ on the unit sphere.
>
> So $\gamma(C) = -\Omega(C)/2$. ∎

> [!note]- Complete formal solution
> The lowest-energy eigenstate of $H = -(\mu B/2)\hat n\cdot\hat\sigma$ in spherical coordinates is $|+\hat n\rangle = (\cos(\theta/2), e^{i\phi}\sin(\theta/2))^T$ (Step 1, verified by direct computation). The Berry connection 1-form is $\omega = \langle+\hat n, d|+\hat n\rangle = i\sin^2(\theta/2)\,d\phi$ (Step 2, by computing the $d\theta$ component to be zero and the $d\phi$ component to be $i\sin^2(\theta/2)$). The Berry curvature is $\theta = d\omega = (i/2)\sin\theta\,d\theta\wedge d\phi$ (Step 3). For a closed loop $C = \partial S$ in parameter space $S^2$, Stokes gives $\gamma(C) = i\int_S\theta = -(1/2)\int_S\sin\theta\,d\theta\wedge d\phi = -\Omega(C)/2$ (Step 4). ∎

> [!warning] Sanity-check: Frame-invariance and the Hopf-bundle connection
> The result $\gamma(C) = -\Omega(C)/2$ is independent of the choice of gauge (different eigenstate choice $|+\hat n\rangle \to |+\hat n\rangle e^{i\chi}$ gives $\omega \to \omega + i d\chi$, $\theta$ unchanged, integral unchanged).
>
> **Important consistency check:** integrating $\theta$ over the full $S^2$ gives $\frac{i}{2\pi}\int_{S^2}\theta = \frac{i}{2\pi}\cdot\frac{i}{2}\cdot 4\pi = -1$. So $c_1$ of the Berry line bundle for spin-$\tfrac{1}{2}$ is $-1$ — confirming the relation to the Hopf bundle (with $c_1 = -1$): the spin-$\tfrac{1}{2}$ Berry line bundle *is* the Hopf bundle, up to dualization.
>
> But wait: for spin-$\tfrac{1}{2}$ the "geometric phase for a full rotation" is $-\pi$, half of $-2\pi$. And the Berry phase for going all the way around the sphere ($\Omega = 4\pi$) is $-2\pi$, equivalent to $0$ modulo $2\pi$... no, $-2\pi \neq 0$ modulo $2\pi$ in the wavefunction (it gives a $-1$ phase). This is the famous **$4\pi$-periodicity** of spinors: rotating by $2\pi$ in physical space rotates the spin by $-1$, requiring a full $4\pi$ rotation to return to the original state. ✓

---

# Key Takeaways

**The half-solid-angle answer encodes the $\mathrm{SU}(2) \to \mathrm{SO}(3)$ double cover.** A rotation by $2\pi$ in physical space corresponds to a rotation by $\pi$ (half) in spin space; a closed loop of solid angle $4\pi$ on the sphere of directions accumulates Berry phase $-2\pi$, exhibiting the $-1$ "spinor phase" of a full $2\pi$ rotation. The factor of $\tfrac{1}{2}$ in $\gamma(C) = -\Omega(C)/2$ is the geometric imprint of the **double cover** $\mathrm{Spin}(3) = \mathrm{SU}(2) \to \mathrm{SO}(3)$. The trigger-reaction pattern: "spin-$\tfrac{1}{2}$ Berry phase" → "half the solid angle, with the half tracking the spin/rotation double cover."

**The Berry curvature is half the area form on $S^2$ — and this is the connection on the Hopf bundle.** $\theta = (i/2)\sin\theta\,d\theta\wedge d\phi$. The factor of $\tfrac{1}{2}$ makes the first Chern number $c_1 = -1$ (integer!), not $-2$ (which would be the area form alone). The Berry line bundle for spin-$\tfrac{1}{2}$ over the sphere of magnetic-field directions *is* the Hopf bundle: the same geometric object Frankel computes in [[Thm - First Chern Class of the Hopf Bundle is One]]. So Berry's discovery of the geometric phase is, mathematically, the discovery that the spin-$\tfrac{1}{2}$ Hilbert space carries a Hopf-bundle structure over the sphere of states.

**Experimental verification of geometric phase.** Berry's prediction was experimentally verified within a year of the 1984 paper (Tomita and Chiao, 1986, for photons in optical fibres; Bitter and Dubbers, 1987, for neutrons in a rotating magnetic field). The half-solid-angle answer is what was measured — confirming the quantum-mechanical reality of the geometric phase, distinct from the dynamical phase. The trigger-reaction pattern: "cyclic adiabatic evolution of a quantum system" → "Berry phase = holonomy of eigenspace line bundle = geometric quantity computable from the connection."

This exercise prefigures the **Wilczek-Zee non-abelian Berry phase** (degenerate-band case, parameterized by Wilczek-Zee gauge fields), the **Aharonov-Anandan phase** (non-adiabatic cyclic case, with the projective Hilbert space replacing the eigenspace bundle), and the **topological-insulator invariants** (Berry-curvature integrals over the Brillouin zone giving $\mathbb{Z}_2$ topological invariants).
