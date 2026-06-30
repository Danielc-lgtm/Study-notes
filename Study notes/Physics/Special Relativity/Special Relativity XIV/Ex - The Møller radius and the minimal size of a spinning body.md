---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Minimal Size of a Spinning System"
  - "Def - Spin Four-Vector"
  - "Def - Centre of Inertia"
tags: [physics, special-relativity]
---

# Problem Statement

The [[Thm - Minimal Size of a Spinning System|Møller theorem]] bounds the size of a spinning body from below by $R \geq R_0 = \|\vec\sigma\|/(mc)$. Working with $c$ restored:

1. Give Møller's heuristic derivation: argue that to carry a spin $\|\vec\sigma\|$ in a body of radius $R$, the constituents must circulate at speed $v \sim \|\vec\sigma\|/(mR)$, and impose $v < c$ to obtain the bound $R > \|\vec\sigma\|/(mc)$.
2. Derive the bound rigorously from the displacement formula $\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\vec\sigma\times\vec V_\mathcal{O}$: show the centroids fill a disk of radius $R_0$ perpendicular to $\vec\sigma$, that every centroid is an interior point, and conclude $R \geq R_0$.
3. Express the Møller radius in terms of the [[Def - Casimir Invariants of the Poincaré Group|Poincaré Casimirs]]: show $R_0 = \sqrt{-W^2}/(P^2)$ (with $c = 1$), where $W$ is the Pauli–Lubanski vector and $P^2 = m^2$.
4. Apply the bound to the electron: with $\|\vec\sigma\| = \frac{\sqrt 3}{2}\hbar$ (spin $\tfrac12$) and the electron mass, compute $R_0$ numerically and compare with the "classical electron radius" $r_e = e^2/(4\pi\varepsilon_0 m_e c^2)$. What does the comparison tell you about classical models of the electron?

**Recall:**

![[Thm - Minimal Size of a Spinning System#Statement]]

The displacement between the [[Def - Centre of Inertia|centre of inertia]] $G$ and the centroid $G_\mathcal{O}$ relative to an observer moving at $\vec V_\mathcal{O}$ is $\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\vec\sigma\times\vec V_\mathcal{O}$. The [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] satisfies $W^2 = -m^2\|\vec\sigma\|^2$ (with $c = 1$). The Compton wavelength is $\lambda_C = \hbar/(mc)$.

---

# Convergent Strategy

**Problem class.** A *derive-and-apply-a-bound* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: the observer-dependence of the centroid is bounded by the spin, and the bound, inverted, forbids a spinning body from being too small.

**Assumption pattern.** A spinning body with intrinsic angular momentum. The signpost is "minimal size" or "how small can it be": the Møller radius $R_0 = \|\vec\sigma\|/(mc)$ is the answer, derivable heuristically (circulation speed) or rigorously (disk of centroids).

**Theorem routing.** Part 1 is Møller's heuristic ($v < c$). Part 2 is the rigorous [[Thm - Minimal Size of a Spinning System|disk-of-centroids]] argument. Part 3 rewrites in [[Def - Casimir Invariants of the Poincaré Group|Casimir]] form. Part 4 plugs in electron numbers.

**Key decision point.** The crux of part 2 is the inversion of logic: a statement about the *observer-dependence of the centroid* (it fills a disk) becomes a statement about the *size of the body* (it must contain the disk) via the fact that every centroid is an interior point. The heuristic of part 1 gives the same answer by a different route — circulation speed capped by $c$.

---

# Legal Operations Used

1. **Operation 4 from the topic page (go to the barycentric frame).** Parts 1–3 work relative to the centre of inertia and barycentric observers.

2. **Operation 9 from the topic page (bound a cross product).** Part 2 bounds $\|\vec\sigma\times\vec V_\mathcal{O}\|$ using $\|\vec V_\mathcal{O}\| < c$.

---

# Hints

> [!note]- Hint 1
> Dimensionally, angular momentum is (mass)(velocity)(length): $\|\vec\sigma\| \sim mvR$. Solve for $v$: $v\sim\|\vec\sigma\|/(mR)$. Now impose $v < c$: $\|\vec\sigma\|/(mR) < c$, i.e. $R > \|\vec\sigma\|/(mc)$.

> [!note]- Hint 2
> The displacement $\frac{1}{mc^2}\vec\sigma\times\vec V_\mathcal{O}$ has magnitude $\frac{\|\vec\sigma\|\|\vec V_\mathcal{O}\||\sin\theta|}{mc^2} < \frac{\|\vec\sigma\| c}{mc^2} = \frac{\|\vec\sigma\|}{mc}$ since $\|\vec V_\mathcal{O}\| < c$. As $\vec V_\mathcal{O}$ ranges over all directions perpendicular to $\vec\sigma$, the displacement sweeps a disk of radius $R_0$. Each centroid lies inside the body (positive-energy-weighted average), so the body contains the disk, hence $R \geq R_0$.

> [!note]- Hint 3
> With $c = 1$, $R_0 = \|\vec\sigma\|/m$. The Pauli–Lubanski invariant is $W^2 = -m^2\|\vec\sigma\|^2$, so $\sqrt{-W^2} = m\|\vec\sigma\|$ and $\|\vec\sigma\| = \sqrt{-W^2}/m$. Also $P^2 = m^2$. So $R_0 = \|\vec\sigma\|/m = \sqrt{-W^2}/m^2 = \sqrt{-W^2}/P^2$.

> [!note]- Hint 4
> $R_0 = \frac{\sqrt 3}{2}\frac{\hbar}{m_e c} = \frac{\sqrt 3}{2}\lambda_C$, where $\lambda_C = \hbar/(m_e c)\approx 3.86\times 10^{-13}$ m is the reduced Compton wavelength. So $R_0\approx 3.3\times 10^{-13}$ m. The classical electron radius is $r_e\approx 2.8\times 10^{-15}$ m, about 140 times smaller. So a classical spinning charge distribution of size $r_e$ is *far too small* to carry the electron's spin without superluminal circulation.

---

# Solution

The exercise derives the Møller bound two ways and applies it to the electron. Part 1 is Møller's circulation heuristic; part 2 is the rigorous disk-of-centroids argument; part 3 recasts in Casimir form; part 4 exposes the failure of classical electron models.

**Step 1: Møller's heuristic.**

> [!note]- Derivation
> To carry an intrinsic angular momentum (spin) $\|\vec\sigma\|$ in a body of radius $R$ and mass $m$, the constituents must circulate. Dimensionally, angular momentum is mass times velocity times lever arm, so
> $$\|\vec\sigma\| \sim m\,v\,R,$$
> giving the required circulation speed
> $$v \sim \frac{\|\vec\sigma\|}{mR}.$$
> As the body shrinks ($R\to 0$), the required speed $v$ grows without bound. But no constituent can move faster than light: $v < c$. Imposing this,
> $$\frac{\|\vec\sigma\|}{mR} < c\quad\Longrightarrow\quad R > \frac{\|\vec\sigma\|}{mc} = R_0.$$
> The body cannot be smaller than its Møller radius, because to keep a fixed spin in a smaller body the parts would have to circulate faster than light. This is the physical content in one line: **spin needs room to circulate, and the speed of light sets how little room.**

**Step 2: The rigorous derivation.**

> [!note]- Derivation
> Start from the [[Thm - Minimal Size of a Spinning System|displacement formula]]
> $$\overrightarrow{GG_\mathcal{O}} = \frac{1}{mc^2}\vec\sigma\times\vec V_\mathcal{O}.$$
> Its magnitude is $\|\overrightarrow{GG_\mathcal{O}}\| = \frac{\|\vec\sigma\|\,\|\vec V_\mathcal{O}\|\,|\sin\theta|}{mc^2}$, where $\theta$ is the angle between $\vec\sigma$ and $\vec V_\mathcal{O}$. Since a barycentric observer is inertial, $\|\vec V_\mathcal{O}\| < c$, and $|\sin\theta|\leq 1$, so
> $$\|\overrightarrow{GG_\mathcal{O}}\| < \frac{\|\vec\sigma\|\,c}{mc^2} = \frac{\|\vec\sigma\|}{mc} = R_0.$$
> As $\vec V_\mathcal{O}$ ranges over all sub-light velocities perpendicular to $\vec\sigma$ (and all directions in the transverse plane), the displacement $\vec\sigma\times\vec V_\mathcal{O}$ sweeps the full open disk of radius $R_0$ perpendicular to $\vec\sigma$, centred on $G$. Now the key step: each centroid $G_\mathcal{O}$ is a *positive-energy-weighted average* of the particle positions, all of which lie inside the body; since the energies $E_a > 0$ (inertial observer), the average lies in the convex hull of the positions, i.e. *inside the body*. So every point of the disk of centroids is inside the body, the body contains the disk, and its radius satisfies
> $$R \geq R_0 = \frac{\|\vec\sigma\|}{mc}.$$
> The same bound as the heuristic, now rigorous: the observer-dependence of the centroid fills a disk, the centroids are interior points, so the body is at least as big as the disk.

**Step 3: The Casimir form.**

> [!note]- Derivation
> Work with $c = 1$, so $R_0 = \|\vec\sigma\|/m$. The [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski invariant]] is
> $$W^2 = -m^2\|\vec\sigma\|^2\quad\Longrightarrow\quad \sqrt{-W^2} = m\|\vec\sigma\|\quad\Longrightarrow\quad \|\vec\sigma\| = \frac{\sqrt{-W^2}}{m}.$$
> And the first Casimir is $P^2 = m^2$. Substituting,
> $$R_0 = \frac{\|\vec\sigma\|}{m} = \frac{\sqrt{-W^2}}{m^2} = \frac{\sqrt{-W^2}}{P^2}.$$
> The Møller radius is built entirely from the two [[Def - Casimir Invariants of the Poincaré Group|Casimir invariants]] of the Poincaré group — mass ($P^2$) and spin ($W^2$). It is a Lorentz-invariant length, intrinsic to the system, determined by the same two numbers that label the particle in Wigner's classification. A *length* emerges from the invariants that classify a particle, which is the deep reason the minimal size is a fundamental property, not a model-dependent quantity.

**Step 4: The electron.**

> [!note]- Derivation
> For a spin-$\tfrac12$ electron, $\|\vec\sigma\| = \sqrt{s(s+1)}\,\hbar = \sqrt{\tfrac12\cdot\tfrac32}\,\hbar = \frac{\sqrt 3}{2}\hbar$. The Møller radius is
> $$R_0 = \frac{\|\vec\sigma\|}{m_e c} = \frac{\sqrt 3}{2}\frac{\hbar}{m_e c} = \frac{\sqrt 3}{2}\lambda_C,$$
> where $\lambda_C = \hbar/(m_e c) \approx 3.86\times 10^{-13}$ m is the reduced Compton wavelength. Numerically,
> $$R_0 \approx 0.87\times 3.86\times 10^{-13}\,\text{m} \approx 3.3\times 10^{-13}\,\text{m}.$$
> Compare with the **classical electron radius**,
> $$r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \approx 2.8\times 10^{-15}\,\text{m},$$
> which is about 140 times *smaller* than $R_0$. The conclusion is decisive: a classical model of the electron as a spinning charge distribution of size $r_e$ is impossible, because such a small body cannot carry the electron's spin $\frac{\sqrt 3}{2}\hbar$ without its surface moving far faster than light (by a factor of ${\sim}140$). The electron's spin forbids any classical point-like or $r_e$-sized model; spin is irreducibly quantum, and the natural scale for the electron's "size" is the Compton wavelength, not $r_e$. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** $\|\vec\sigma\|\sim mvR\Rightarrow v\sim\|\vec\sigma\|/(mR)$; imposing $v < c$ gives $R > \|\vec\sigma\|/(mc) = R_0$.
>
> **Part 2.** $\|\overrightarrow{GG_\mathcal{O}}\| = \frac{\|\vec\sigma\|\|\vec V_\mathcal{O}\||\sin\theta|}{mc^2} < R_0$ since $\|\vec V_\mathcal{O}\| < c$; the centroids fill the disk of radius $R_0$; each is an interior point, so $R\geq R_0$.
>
> **Part 3.** $W^2 = -m^2\|\vec\sigma\|^2$ and $P^2 = m^2$ give $R_0 = \|\vec\sigma\|/m = \sqrt{-W^2}/P^2$ — a length from the two Casimirs.
>
> **Part 4.** $R_0 = \frac{\sqrt 3}{2}\lambda_C\approx 3.3\times 10^{-13}$ m, about 140 times the classical electron radius $r_e\approx 2.8\times 10^{-15}$ m; so a classical $r_e$-sized spinning electron would require superluminal circulation — classical models of the electron's spin are impossible. $\blacksquare$

---

# Key Takeaways

**The Møller bound is the speed of light forbidding a thing from being too small.** Most relativistic theorems forbid going *fast* (faster than light); the Møller bound is the rare one that forbids being *small*. The mechanism is the same speed limit seen from a new angle: to carry a fixed spin in a shrinking body, the constituents must circulate ever faster, and the speed of light caps the circulation, hence caps the smallness. The reusable insight is that spin is angular momentum, angular momentum is (mass)(velocity)(lever arm), and a fixed angular momentum with a capped velocity forces a minimum lever arm. The trigger to recognise: any question about the minimal size of a spinning object should invoke the Møller radius $R_0 = \|\vec\sigma\|/(mc)$, and the order of magnitude is set by the Compton wavelength once the spin is quantised. This bound has no Newtonian analogue — in Newtonian mechanics a point particle can spin — and it is a genuine prediction of relativity.

**A length built from the Casimirs is a fundamental, model-independent scale.** The Casimir form $R_0 = \sqrt{-W^2}/P^2$ shows the Møller radius is constructed entirely from the two invariants that *define* a particle in Wigner's classification — its mass and its spin. This is why the minimal size is not a feature of any particular model but an intrinsic, Lorentz-invariant property of the system. The transferable diagnostic is that whenever a length, time, or other dimensional quantity can be written purely in terms of the Casimir invariants, it is a fundamental scale of the system, frame-independent and model-independent. For a massive spinning particle, $\sqrt{-W^2}/P^2$ is *the* natural length, and it sets the scale below which the classical or single-particle description fails — the Compton wavelength, up to the spin factor. The same logic identifies the Compton wavelength $\hbar/(mc)$ from $P^2$ and $\hbar$ as the fundamental length of any massive particle.

**The electron is not a classical spinning ball — the numbers prove it.** The numerical comparison $R_0\approx 140\,r_e$ is a clean, decisive refutation of the naive picture of the electron as a small charged sphere spinning to produce its magnetic moment. To carry spin $\frac{\sqrt 3}{2}\hbar$ in a body of size $r_e$, the surface would move at ${\sim}140c$ — absurd. The electron's "size" for the purpose of spin is the Compton wavelength, two orders of magnitude larger than $r_e$, and even there the classical picture is only suggestive: spin is irreducibly quantum, a property of the Poincaré representation, not of a rotating mass distribution. The reusable lesson is that order-of-magnitude estimates from fundamental bounds can settle physical questions decisively — here, that classical models of intrinsic spin fail by a large factor, motivating the quantum-mechanical treatment where spin is an algebraic property of the wavefunction's transformation under the Lorentz group, realised dynamically in the Dirac equation and observed as the Zitterbewegung trembling at exactly the Compton-wavelength scale.
