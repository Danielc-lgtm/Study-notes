---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Impossibility of Global Clock Synchronization on a Rotating Disk"
  - "Def - Uniformly Rotating Observer"
  - "Def - Einstein-Poincaré Simultaneity"
tags: [physics, special-relativity]
---

# Problem Statement

Corotating observers on a disk attempt to synchronize their clocks. Working with $c = 1$ where convenient:

1. Two neighbouring corotating observers, separated by proper vector $d\vec\ell$, synchronize by Einstein–Poincaré radar. Derive the condition $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$ on the central-coordinate-time gap, starting from the orthogonality of the corotating four-velocity to the separation.
2. A family of corotating observers all at the same radius $r$ forms a closed loop around the rim. Integrate the local gap around the loop to find the accumulated desynchronization $\Delta t'_{\text{desync}}$, and show it is $\pm 2\pi\Gamma r^2\omega/c^2 \ne 0$.
3. For small rim speeds, recast the loop integral using Stokes' theorem and the identity $\mathrm{curl}\,\vec V = 2\vec\omega$, obtaining $\Delta t'_{\text{desync}} \simeq \frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$. Interpret this as a vorticity flux.
4. Explain why this is *not* a Newtonian limit despite the small-velocity approximation, and what feature of the formula gives this away.

**Recall:**

![[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk#Statement]]

[[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré simultaneity]] of two events relative to an observer means their separation is orthogonal to the observer's four-velocity (lies in its local rest space). A [[Def - Uniformly Rotating Observer|corotating observer]] has four-velocity $U' = \Gamma(U + c^{-1}\vec V)$ with $\vec V = r\omega\,\vec n$ and $\Gamma = (1 - r^2\omega^2/c^2)^{-1/2}$.

---

# Convergent Strategy

**Problem class.** A *global-obstruction* problem, the chapter's signature type. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]]: a quantity vanishing locally but wanted globally is tested by a loop integral; nonzero means the global construction is impossible.

**Assumption pattern.** A closed loop of corotating observers. The signpost is "synchronize around a loop and return to the start": the local synchronization gaps, individually harmless, accumulate to a nonzero circulation because the velocity field has nonzero curl (vorticity $2\vec\omega$).

**Theorem routing.** Part 1 expands the orthogonality condition $U'\cdot\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = 0$ from [[Def - Einstein-Poincaré Simultaneity]] to get the local gap, as in [[Thm - Impossibility of Global Clock Synchronization on a Rotating Disk]]; part 2 integrates at constant radius; part 3 applies Stokes with $\mathrm{curl}\,\vec V = 2\vec\omega$; part 4 examines the surviving $c^2$.

**Key decision point.** The crux is recognizing that local synchronizability does *not* imply global synchronizability — the obstruction is the nonzero loop integral, not any failure at a single step. The natural but wrong move is to assume the local gaps can be "patched" into a global time; the patching fails by exactly $\Delta t'_{\text{desync}}$. The non-obvious recognition is that the synchronization condition is a one-form whose curl (the vorticity) is nonzero.

---

# Legal Operations Used

1. **Operation 3 from the topic page (local Einstein–Poincaré synchronization).** The orthogonality of $U'$ to the separation gives the local gap $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$.

2. **Operation 4 from the topic page (integrate the local gap around a loop).** Summing the local gaps around the closed loop tests for the global obstruction; nonzero means no global synchronization.

3. **Operation 5 from the topic page (Stokes' theorem and $\mathrm{curl}\,\vec V = 2\vec\omega$).** Converts the circulation to a vorticity flux, giving the universal area-proportional form for small velocities.

---

# Hints

> [!note]- Hint 1
> The two simultaneous events have separation $\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = c\,dt\,U + d\vec\ell + dt\,\vec V$ (central-time gap $dt$, proper separation $d\vec\ell$, drift $dt\,\vec V$ from the rotation of the frame). Impose orthogonality to $U' = \Gamma(U + c^{-1}\vec V)$ and use $U\cdot U = 1$, $U\cdot\vec V = 0$, $U\cdot d\vec\ell = 0$, $1 - \vec V\cdot\vec V/c^2 = \Gamma^{-2}$.

> [!note]- Hint 2
> At constant radius $r$, $\Gamma$ is constant and $\vec V\cdot d\vec\ell = (r\omega\,\vec n)\cdot(r\,d\varphi\,\vec n) = r^2\omega\,d\varphi$ (both along the azimuthal direction $\vec n$). So $\oint\Gamma^2\vec V\cdot d\vec\ell = \Gamma^2 r^2\omega\int_0^{2\pi}d\varphi = 2\pi\Gamma^2 r^2\omega$. Divide by $\Gamma_{(0)} = \Gamma$ (to convert to the proper time of the observer at radius $r$) to get $\Delta t'_{\text{desync}} = 2\pi\Gamma r^2\omega/c^2$.

> [!note]- Hint 3
> For small velocities $\Gamma\to 1$, so $\Delta t'_{\text{desync}}\to \frac{1}{c^2}\oint\vec V\cdot d\vec\ell$. Stokes' theorem turns the circulation into the flux of $\mathrm{curl}\,\vec V$ through the enclosed surface $S$: $\oint_{\mathscr{C}}\vec V\cdot d\vec\ell = \int_S(\mathrm{curl}\,\vec V)\cdot d\vec{\mathcal{A}}$. For rigid rotation $\mathrm{curl}\,\vec V = 2\vec\omega$ (the curl of $\vec\omega\times\vec r$). So $\Delta t'_{\text{desync}}\simeq\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$.

> [!note]- Hint 4
> A genuine Newtonian limit ($c\to\infty$) would kill the effect: $\Delta t'_{\text{desync}}\to 0$. But the small-velocity formula $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$ still contains $c^2$ in the denominator — so it is a small-*velocity* approximation of a relativistic effect, not the $c\to\infty$ classical limit. In true Newtonian physics, all observers share absolute time and $\Delta t'_{\text{desync}} = 0$ identically.

---

# Solution

The route has four steps. Step 1 derives the local gap from orthogonality. Step 2 integrates around the rim to get the nonzero desynchronization $2\pi\Gamma r^2\omega/c^2$. Step 3 recasts it via Stokes as a vorticity flux $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$. Step 4 explains that the surviving $c^2$ marks it as relativistic, not Newtonian. The non-obvious move is recognizing the loop integral as the obstruction to global synchronization.

**Step 1: The local synchronization gap is $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$.**

> [!note]- Derivation
> Two neighbouring corotating observers $\mathcal{O}'_{(\lambda)}$, $\mathcal{O}'_{(\lambda+d\lambda)}$ synchronize by radar: the events on their worldlines deemed simultaneous by $\mathcal{O}'_{(\lambda)}$ are those whose separation is orthogonal to $U'_{(\lambda)}$ ([[Def - Einstein-Poincaré Simultaneity]]). The separation between the simultaneous events, decomposed through the central worldline, is
> $$\overrightarrow{A_{(\lambda)}A_{(\lambda+d\lambda)}} = c\,dt\,U + d\vec\ell + dt\,\vec V,$$
> where $dt$ is the central-coordinate-time gap, $d\vec\ell$ the proper separation in $\mathcal{O}$'s rest space, and $dt\,\vec V$ the drift due to the rotation of the frame between $t$ and $t + dt$. Imposing orthogonality to $U'_{(\lambda)} = \Gamma(U + c^{-1}\vec V)$:
> $$\big(U + c^{-1}\vec V\big)\cdot\big(c\,dt\,U + d\vec\ell + dt\,\vec V\big) = 0.$$
> Using $U\cdot U = 1$, $U\cdot\vec V = 0$, $U\cdot d\vec\ell = 0$ (the separation and velocity are spacelike, in $\mathcal{O}$'s rest space), and $\vec V\cdot\vec V/c^2 = 1 - \Gamma^{-2}$:
> $$c\,dt\,(1) + c^{-1}\big[dt\,(\vec V\cdot\vec V) + \vec V\cdot d\vec\ell\big] = 0 \;\Rightarrow\; c\,dt\,\Gamma^{-2} = c^{-1}\vec V\cdot d\vec\ell,$$
> hence
> $$dt = \Gamma^2\,\frac{\vec V\cdot d\vec\ell}{c^2}.$$
> Two neighbours can always satisfy this — local synchronization is unobstructed.

**Step 2: Around the rim, the gap accumulates to $\Delta t'_{\text{desync}} = \pm 2\pi\Gamma r^2\omega/c^2 \ne 0$.**

> [!note]- Derivation
> Take a closed loop of corotating observers at constant radius $r$, traversed once. The central-coordinate-time gap accumulated is
> $$\Delta t = \oint\frac{\Gamma^2\vec V\cdot d\vec\ell}{c^2}.$$
> At constant $r$, $\Gamma$ is constant, and both $\vec V = r\omega\,\vec n$ and $d\vec\ell = r\,d\varphi\,\vec n$ are azimuthal, so $\vec V\cdot d\vec\ell = r^2\omega\,d\varphi$. Then
> $$\Delta t = \frac{\Gamma^2 r^2\omega}{c^2}\int_0^{2\pi}d\varphi = \frac{2\pi\Gamma^2 r^2\omega}{c^2}.$$
> Converting to the proper time of the observer on the loop (dividing by $\Gamma_{(0)} = \Gamma$, since $d\tau = \Gamma^{-1}dt$):
> $$\Delta t'_{\text{desync}} = \frac{1}{\Gamma}\cdot\frac{2\pi\Gamma^2 r^2\omega}{c^2} = \pm\frac{2\pi\Gamma r^2\omega}{c^2}\;\ne\;0,$$
> the sign depending on the sense of traversal. **The gap is nonzero**: synchronizing around the loop and returning to the starting observer, the clock disagrees with itself by $\Delta t'_{\text{desync}}$. No global time exists on the disk.

**Step 3: For small velocities, $\Delta t'_{\text{desync}} \simeq \frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$, a vorticity flux.**

> [!note]- Derivation
> For small rim speeds $\Gamma\to 1$, so the desynchronization reduces to the circulation
> $$\Delta t'_{\text{desync}} \simeq \frac{1}{c^2}\oint_{\mathscr{C}}\vec V\cdot d\vec\ell.$$
> By Stokes' theorem, the circulation of a vector field around a closed loop equals the flux of its curl through any enclosed surface $S$:
> $$\oint_{\mathscr{C}}\vec V\cdot d\vec\ell = \int_S(\mathrm{curl}\,\vec V)\cdot d\vec{\mathcal{A}}.$$
> For a rigidly rotating velocity field $\vec V = \vec\omega\times\vec r$, the curl is uniform: $\mathrm{curl}\,(\vec\omega\times\vec r) = 2\vec\omega$ (the standard rigid-rotation vorticity). Since $\vec\omega$ is constant, the flux is $2\vec\omega\cdot\vec{\mathcal{A}}$, so
> $$\Delta t'_{\text{desync}} \simeq \frac{2}{c^2}\,\vec\omega\cdot\vec{\mathcal{A}}.$$
> The desynchronization is the enclosed **vorticity flux**: the rotation $\vec\omega$ is the local vorticity, and the gap measures how much of it the loop encircles. This is why every effect in the chapter is $\propto\omega A$ — they are all enclosed vorticity fluxes.

**Step 4: This is not a Newtonian limit — the surviving $c^2$ gives it away.**

> [!note]- Derivation
> The small-velocity formula $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$ might be mistaken for a classical (Newtonian) result, since it arises in the limit of small rim speed. It is not. A genuine Newtonian limit is $c\to\infty$, and taking $c\to\infty$ here gives $\Delta t'_{\text{desync}}\to 0$ — there is *no* desynchronization in Newtonian physics, because all observers share one absolute time. The tell is the $c^2$ in the denominator: a true Newtonian formula contains no factors of $c$. So $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$ is a small-*velocity approximation of a genuinely relativistic effect*, not the classical limit. The desynchronization exists only because simultaneity is relative — a purely special-relativistic fact — and the small-velocity approximation merely simplifies the relativistic result, it does not classicalize it.

> [!note]- Complete formal solution
> Local synchronization of neighbours: orthogonality of $U' = \Gamma(U + c^{-1}\vec V)$ to the separation $c\,dt\,U + d\vec\ell + dt\,\vec V$ gives $dt = \Gamma^2(\vec V\cdot d\vec\ell)/c^2$. Around a rim loop at constant $r$, $\vec V\cdot d\vec\ell = r^2\omega\,d\varphi$, so $\Delta t = 2\pi\Gamma^2 r^2\omega/c^2$ and (dividing by $\Gamma$) $\Delta t'_{\text{desync}} = \pm 2\pi\Gamma r^2\omega/c^2\ne 0$ — no global synchronization. For small velocities, Stokes' theorem and $\mathrm{curl}\,\vec V = 2\vec\omega$ give $\Delta t'_{\text{desync}}\simeq\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$, the enclosed vorticity flux. This is not the Newtonian limit: $c\to\infty$ gives zero, and the surviving $c^2$ marks the effect as relativistic — it exists because simultaneity is relative. $\blacksquare$

---

# Key Takeaways

**Local synchronizability does not imply global synchronizability — the obstruction is a loop integral.** Any two neighbouring corotating observers can synchronize their clocks perfectly; yet the disk as a whole cannot be globally synchronized, because the local gaps accumulate to a nonzero $\Delta t'_{\text{desync}}$ around any loop. The trigger for this pattern is any "patch together local solutions" attempt: ask whether the local data integrates consistently around closed loops, and if a loop integral is nonzero, the global object does not exist. This is the same logic as integrating a vector field to find a potential (possible iff the curl vanishes), or extending a local solution of a differential equation (obstructed by holonomy). The lesson transfers everywhere: a quantity that is locally trivial can carry a global obstruction, detectable only by going around a loop. The desynchronization is the cleanest physical example.

**Every effect in this chapter is an enclosed vorticity flux, $\propto\vec\omega\cdot\vec{\mathcal{A}}$.** The desynchronization gap, recast by Stokes' theorem, is $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$ — the flux of the vorticity $2\vec\omega$ through the enclosed area. This is the unifying structure: the rotation $\vec\omega$ is the local vorticity of the corotating congruence, and the global effects (desynchronization, Sagnac delay) are all how much vorticity a loop encircles. The trigger is any loop integral of the rotating velocity: convert it to a vorticity flux, and the answer is immediately $\propto\omega A$. The Sagnac delay is twice this, the GPS correction is this, International Atomic Time corrects for this. Recognizing the vorticity-flux structure unifies what otherwise look like separate phenomena and makes every formula predictable: there must be a circulation, it must equal a $2\vec\omega$ flux, hence it must be $\propto\omega A$.

**A surviving factor of $c$ in a "small-velocity" formula marks it as relativistic, not classical.** The small-velocity desynchronization $\frac{2}{c^2}\vec\omega\cdot\vec{\mathcal{A}}$ is not a Newtonian result: the Newtonian limit $c\to\infty$ kills it, because Newtonian physics has absolute time and no desynchronization. The tell is the $c^2$ in the denominator — a genuine classical formula contains no $c$. The trigger to apply this diagnostic is any approximation reached by "small velocity": check whether the result still contains $c$, and if so, it is a low-speed approximation of a relativistic effect, not the classical limit. The two limits — small velocity ($v/c\to 0$) and Newtonian ($c\to\infty$) — are *different*, and conflating them is a common error. The desynchronization exists only because simultaneity is relative; no amount of slowing down removes it, only sending $c\to\infty$ does, and that is exactly the limit that abolishes relativity. See [[Ex - The line element on the rotating disk]] for the metric cross term $g_{0\varphi}$ that is the local source of this global obstruction.
