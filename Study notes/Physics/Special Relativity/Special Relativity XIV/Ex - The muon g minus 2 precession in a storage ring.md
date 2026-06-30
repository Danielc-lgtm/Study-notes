---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The BMT Equation"
  - "Def - Spin Four-Vector"
  - "Def - Four-Force"
tags: [physics, special-relativity]
---

# Problem Statement

A muon of charge $q$, mass $m$, and Landé factor $g$ circulates in the horizontal plane of a storage ring, held on its circular orbit by a uniform vertical magnetic field $\mathbf{B} = B\hat{\mathbf z}$ (the field of the muon $g-2$ experiments). The spin obeys the [[Thm - The BMT Equation|BMT equation]]; the momentum obeys the Lorentz-force equation of motion. Working with $c = 1$:

1. Show that the muon's momentum direction rotates in the orbital plane at the **cyclotron frequency** $\omega_c = qB/(\gamma m)$ (the angular velocity of the velocity vector seen in the laboratory).
2. Using the BMT equation specialised to a pure magnetic field with velocity perpendicular to $\mathbf{B}$, show that the in-plane spin direction rotates at the **spin precession frequency** $\omega_s = \frac{qB}{\gamma m}\big(1 + \gamma(\tfrac{g}{2}-1)\big)$.
3. Subtract the two to obtain the **anomalous precession frequency** — the rate at which the spin turns *relative to the momentum* — and show it is the remarkably simple, $\gamma$-independent
$$
\omega_a \;=\; \omega_s - \omega_c \;=\; \frac{q}{m}\,a\,B,\qquad a := \frac{g-2}{2}.
$$
4. Explain why the $\gamma$-cancellation in part 3 is the feature that makes the experiment work, and connect $\omega_a$ to the $(\frac g2 - 1)$ Thomas term of the BMT equation.

**Recall:**

![[Thm - The BMT Equation#Statement]]

The Lorentz [[Def - Four-Force|four-force]] is $f = qF(\cdot,\vec u)$, giving the three-dimensional equation of motion $\frac{d\mathbf{p}}{dt} = q\mathbf{v}\times\mathbf{B}$ with $\mathbf{p} = \gamma m\mathbf{v}$. A pure magnetic field does no work, so $\gamma$ and the speed $|\mathbf{v}|$ are constant; only the *direction* of $\mathbf{v}$ rotates. The [[Def - Spin Four-Vector|spin four-vector]] satisfies $\vec s\cdot\vec u = 0$, so in the laboratory it has both a time component and a spatial part; the experimentally relevant quantity is the angle between the spatial spin and the momentum.

---

# Convergent Strategy

**Problem class.** An *apply-an-evolution-law-and-extract-a-frequency* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: for an evolution law, differentiate the defining relation and impose the constraint; the BMT equation is the four-torque with the torque supplied by the electromagnetic field, and the subtlety is the $(\frac g2 - 1)$ Thomas term.

**Assumption pattern.** A charged spin in a pure magnetic field, velocity perpendicular to the field. The signpost is "storage ring" / "$g-2$": this triggers the BMT equation (operation 8) specialised to magnetostatics, with the momentum precession from the Lorentz force compared against the spin precession.

**Theorem routing.** Part 1 is the cyclotron frequency from $\frac{d\mathbf{p}}{dt} = q\mathbf{v}\times\mathbf{B}$. Part 2 specialises the [[Thm - The BMT Equation|BMT equation]] to $\mathbf{B}$-only, perpendicular geometry. Part 3 subtracts. Part 4 interprets the $\gamma$-cancellation and links to the [[Thm - The BMT Equation|Thomas term]].

**Key decision point.** The crux is that *both* the momentum and the spin precess, at frequencies that each depend on $\gamma$, but their *difference* does not — the $\gamma$ inside the spin frequency's $\gamma(\frac g2 - 1)$ term is exactly cancelled by the $1/\gamma$ in $\omega_c$ when one forms $\omega_s - \omega_c$. Recognising that the experiment measures the *difference*, not either frequency alone, is the whole physics.

---

# Legal Operations Used

1. **Operation 8 from the topic page (use the spin transport / BMT equation).** Part 2 is the BMT equation specialised to a magnetic field.

2. **Operation 9 from the topic page (kill a contraction with antisymmetry).** The norm $\|\vec s\|$ is conserved, so the spin merely rotates — this is what lets "spin precession" be a single frequency.

3. **Go to the rest-space three-vector description.** Both precessions are read off as rotations of three-vectors (momentum direction, spatial spin) in the laboratory.

---

# Hints

> [!note]- Hint 1
> A pure magnetic field does no work: $\frac{dE}{dt} = q\mathbf{v}\cdot(\mathbf{v}\times\mathbf{B}) = 0$, so $\gamma$ and $|\mathbf{v}|$ are constant. Then $\frac{d\mathbf{p}}{dt} = \gamma m\frac{d\mathbf{v}}{dt} = q\mathbf{v}\times\mathbf{B}$ gives $\frac{d\mathbf{v}}{dt} = \frac{q}{\gamma m}\mathbf{v}\times\mathbf{B}$ — a rotation of $\mathbf{v}$ about $\mathbf{B}$ at angular speed $\omega_c = qB/(\gamma m)$. This is the cyclotron frequency, with the relativistic $\gamma$ in the denominator.

> [!note]- Hint 2
> Translate the covariant BMT equation into a three-dimensional precession of the spatial spin $\mathbf{s}$ in the laboratory. For a pure magnetic field with $\mathbf{v}\perp\mathbf{B}$, the laboratory spin precesses about $\mathbf{B}$ at $\omega_s = \frac{qB}{\gamma m}\big(1 + \gamma(\frac g2 - 1)\big) = \frac{qB}{m}\big(\frac1\gamma + \frac g2 - 1\big)$. The first piece $\frac{1}{\gamma}\frac{qB}{m}$ is the Thomas/cyclotron part; the $(\frac g2 - 1)$ piece is the dynamical magnetic-moment excess.

> [!note]- Hint 3
> Subtract: $\omega_a = \omega_s - \omega_c = \frac{qB}{m}\big(\frac1\gamma + \frac g2 - 1\big) - \frac{qB}{m}\frac1\gamma = \frac{qB}{m}\big(\frac g2 - 1\big) = \frac{q}{m}\,a\,B$. The two $\frac{1}{\gamma}$ terms cancel exactly, leaving a frequency with no $\gamma$ in it.

> [!note]- Hint 4
> If $g = 2$ exactly, $\omega_a = 0$: the spin stays locked to the momentum at all energies. Any nonzero $\omega_a$ is a direct, magnified readout of $a = (g-2)/2$. The $\gamma$-independence means the experiment does not need to know the beam energy precisely — a decisive practical advantage. The $(\frac g2 - 1)$ that survives is exactly the Thomas term of the BMT equation.

---

# Solution

The exercise compares two precessions — of the momentum (cyclotron) and of the spin (BMT) — and finds that their difference isolates the anomalous magnetic moment in a particularly clean, energy-independent way. Part 1 gets the cyclotron frequency; part 2 the spin frequency; part 3 their difference; part 4 the interpretation.

**Step 1: The cyclotron frequency.**

> [!note]- Derivation
> The magnetic force is $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$, always perpendicular to $\mathbf{v}$, so it does no work:
> $$\frac{dE}{dt} = \mathbf{F}\cdot\mathbf{v} = q(\mathbf{v}\times\mathbf{B})\cdot\mathbf{v} = 0.$$
> Hence the energy $E = \gamma m$ is constant, $\gamma$ is constant, and the speed $|\mathbf{v}|$ is constant — only the *direction* of $\mathbf{v}$ changes. The relativistic equation of motion is $\frac{d\mathbf{p}}{dt} = q\mathbf{v}\times\mathbf{B}$ with $\mathbf{p} = \gamma m\mathbf{v}$; since $\gamma$ is constant,
> $$\gamma m\frac{d\mathbf{v}}{dt} = q\mathbf{v}\times\mathbf{B}\qquad\Longrightarrow\qquad \frac{d\mathbf{v}}{dt} = \frac{q}{\gamma m}\,\mathbf{v}\times\mathbf{B}.$$
> This is the equation of a vector $\mathbf{v}$ rotating about $\mathbf{B} = B\hat{\mathbf z}$ at constant angular speed. The momentum direction therefore rotates in the orbital plane at the **cyclotron frequency**
> $$\omega_c = \frac{qB}{\gamma m}.$$
> Restoring $c$, $\omega_c = qB/(\gamma m c)$ in Gaussian units; the relativistic factor $1/\gamma$ is the statement that a faster (heavier, in the $\gamma m$ sense) particle is harder to turn.

**Step 2: The spin precession frequency.**

> [!note]- Derivation
> The spatial spin $\mathbf{s}$ in the laboratory precesses according to the laboratory form of the [[Thm - The BMT Equation|BMT equation]]. For a *pure magnetic field* with the velocity perpendicular to $\mathbf{B}$ (the storage-ring geometry), the standard reduction of the covariant BMT equation to a three-vector precession $\frac{d\mathbf{s}}{dt} = \boldsymbol{\omega}_s\times\mathbf{s}$ gives the precession vector
> $$\boldsymbol{\omega}_s = -\frac{q}{m}\Big[\Big(\frac g2 - 1 + \frac1\gamma\Big)\mathbf{B} - \Big(\frac g2 - 1\Big)\frac{\gamma}{\gamma+1}(\boldsymbol\beta\cdot\mathbf{B})\boldsymbol\beta\Big],$$
> and with $\boldsymbol\beta\perp\mathbf{B}$ the second term drops, leaving a precession about $\mathbf{B}$ at angular speed
> $$\omega_s = \frac{qB}{m}\Big(\frac g2 - 1 + \frac1\gamma\Big) = \frac{qB}{\gamma m}\Big(1 + \gamma\big(\tfrac g2 - 1\big)\Big).$$
> Two contributions are visible. The $\frac{1}{\gamma}\frac{qB}{m}$ piece is the *kinematic* part — it is precisely the cyclotron rate $\omega_c$, the Thomas precession that any spin (even $g=1$, no anomalous moment) would undergo just from being carried around the bent worldline. The $(\frac g2 - 1)\frac{qB}{m}$ piece is the *dynamical* excess — the precession of the magnetic moment $\boldsymbol\mu = \frac{gq}{2m}\mathbf{s}$ in the field, beyond what the kinematics already supplies. The split into "kinematic $\frac1\gamma$" and "dynamical $\frac g2 - 1$" is the three-vector shadow of the two terms of the covariant BMT equation.

**Step 3: The anomalous precession frequency.**

> [!note]- Derivation
> The experimentally measured quantity is the rate at which the spin turns *relative to the momentum* — the rate of change of the angle between $\mathbf{s}$ and $\mathbf{v}$. Since both rotate in the same plane about the same axis $\mathbf{B}$, this relative rate is the difference of the two frequencies:
> $$\omega_a = \omega_s - \omega_c = \frac{qB}{m}\Big(\frac g2 - 1 + \frac1\gamma\Big) - \frac{qB}{m}\cdot\frac1\gamma = \frac{qB}{m}\Big(\frac g2 - 1\Big).$$
> The two $\frac{1}{\gamma}$ terms — the cyclotron rate and the kinematic part of the spin rate — **cancel exactly**, leaving
> $$\boxed{\;\omega_a = \frac{q}{m}\,a\,B,\qquad a = \frac{g-2}{2}.\;}$$
> The anomalous precession frequency is **independent of $\gamma$** (hence of the beam energy) and is directly proportional to the **anomaly** $a$. Restoring $c$, $\omega_a = qaB/(mc)$. If $g$ were exactly $2$, $\omega_a$ would vanish and the spin would stay rigidly locked to the momentum at every energy; the small nonzero value of $a\approx 1.16\times10^{-3}$ makes the spin slowly rotate ahead of the momentum, and $\omega_a$ is what the experiment counts.

**Step 4: Why the cancellation matters.**

> [!note]- Derivation
> The $\gamma$-cancellation in Step 3 is not an accident of the algebra; it is the design principle of the entire muon $g-2$ programme. A storage ring contains muons with a spread of energies (a spread of $\gamma$), and both $\omega_s$ and $\omega_c$ depend on $\gamma$. If the measured signal depended on either frequency alone, the energy spread would smear it out. But the *difference* $\omega_a = qaB/m$ has no $\gamma$ in it — every muon, regardless of energy, precesses relative to its momentum at the *same* rate. The signal stays sharp, and $\omega_a$ can be measured to sub-ppm precision by detecting the decay positrons, whose emission direction correlates with the muon spin: the count rate oscillates at exactly $\omega_a$.
>
> The surviving $(\frac g2 - 1) = a$ is precisely the *coefficient of the longitudinal Thomas term* in the covariant [[Thm - The BMT Equation|BMT equation]], $\frac{d\vec s}{d\tau} = \frac{q}{mc}[\frac g2\vec F(\cdot,\vec s) + (\frac g2 - 1)F(\vec u,\vec s)\vec u]$. The kinematic Thomas precession ($-1$) is universal and tracks the momentum; the dynamical magnetic-moment precession ($\frac g2$) is what would, for $g=2$, *also* exactly track the momentum. Their interplay is engineered so that only the deviation $\frac g2 - 1 = a$ survives in the relative precession. This is why the BMT equation, and specifically its Thomas term, is the indispensable theoretical tool of precision $g-2$ physics: it is the equation that turns a quantum-field-theory prediction of $a$ into a frequency one can put on an oscilloscope. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** A magnetic field does no work ($\mathbf{F}\cdot\mathbf{v} = 0$), so $\gamma$ is constant and $\gamma m\,d\mathbf{v}/dt = q\mathbf{v}\times\mathbf{B}$ rotates $\mathbf{v}$ about $\mathbf{B}$ at $\omega_c = qB/(\gamma m)$.
>
> **Part 2.** The BMT equation reduced to a three-vector precession in a pure magnetic field with $\boldsymbol\beta\perp\mathbf{B}$ gives the spin precessing about $\mathbf{B}$ at $\omega_s = \frac{qB}{m}(\frac g2 - 1 + \frac1\gamma)$.
>
> **Part 3.** $\omega_a = \omega_s - \omega_c = \frac{qB}{m}(\frac g2 - 1 + \frac1\gamma) - \frac{qB}{m}\frac1\gamma = \frac{qB}{m}(\frac g2 - 1) = \frac{q}{m}aB$, independent of $\gamma$.
>
> **Part 4.** The $\frac1\gamma$ terms cancel, so the relative precession is energy-independent — the key to a sharp signal despite the beam's energy spread. The surviving $a = \frac g2 - 1$ is the coefficient of the Thomas term in the BMT equation; $g=2$ would give $\omega_a = 0$, so $\omega_a$ is a direct readout of the anomaly. $\blacksquare$

---

# Key Takeaways

**The experiment measures a *difference* of precession frequencies, and that is what makes it energy-independent.** The single most important structural fact is that neither the cyclotron frequency $\omega_c = qB/(\gamma m)$ nor the spin precession frequency $\omega_s$ is the observable — both depend on $\gamma$ and would be smeared by the beam's energy spread. The observable is their difference $\omega_a = qaB/m$, in which the $\gamma$-dependence cancels identically, leaving a frequency that every muon shares regardless of energy. The reusable lesson is that when two quantities precess in the same plane about the same axis, the physically clean object is often their *relative* rate, and a cancellation that removes a nuisance parameter (here $\gamma$) is frequently the design principle of a precision measurement. Whenever a problem offers two frequencies that individually depend on something you cannot control, check whether their difference does not.

**The anomalous frequency is the Thomas term made measurable.** The frequency $\omega_a$ is proportional to $a = (g-2)/2 = \frac g2 - 1$, which is exactly the coefficient of the kinematic $(\frac g2 - 1)F(\vec u,\vec s)\vec u$ term in the covariant [[Thm - The BMT Equation|BMT equation]]. This is the deep reason the BMT equation, and not merely the non-relativistic Larmor formula, is the right tool: the Larmor precession alone would give the $\frac g2$ piece, but it is the *interplay* of the dynamical magnetic-moment precession with the kinematic Thomas precession of the bent worldline that arranges for only the deviation from $g=2$ to survive in the relative rate. For $g=2$ — the Dirac value — the spin tracks the momentum exactly at all energies, and the entire $g-2$ enterprise is the measurement of the small failure of this tracking. Understanding which part of $\omega_a$ is kinematic and which is dynamical is the conceptual core of the measurement.

**The anomalous magnetic moment is one of the sharpest confrontations of theory and experiment, and this kinematics is the bridge.** The muon anomaly $a_\mu$ is measured in storage rings by inverting exactly the relation $\omega_a = qaB/m$ derived here, and compared against a Standard Model prediction computed to many loops in quantum electrodynamics, electroweak theory, and hadronic corrections. A persistent small discrepancy between the measured and predicted $a_\mu$ is among the most closely watched possible signals of physics beyond the Standard Model. None of this precision physics is reachable without the classical kinematics of spin precession — the BMT equation and the $\gamma$-cancellation of this exercise are the lever that turns a many-loop field-theory number into a frequency counted in a laboratory. The transferable point is that even the most quantum of precision measurements rests on a classical relativistic equation of motion for the spin, and the cleanliness of the extraction (the $\gamma$-independence) is a gift of relativistic kinematics, not of the quantum theory.
