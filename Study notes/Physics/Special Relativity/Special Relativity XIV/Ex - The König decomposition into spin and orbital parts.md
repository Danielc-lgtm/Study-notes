---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - König Theorem (Relativistic)"
  - "Def - Spin Four-Vector"
  - "Def - Centre of Inertia"
tags: [physics, special-relativity]
---

# Problem Statement

The [[Thm - König Theorem (Relativistic)|König theorem]] splits the angular momentum of an isolated system into spin and orbital parts, $J_C = S + \overrightarrow{CG}^\flat\wedge P$. Working with $c = 1$:

1. Consider two particles of equal mass $m_0$, one at rest and one moving, forming an isolated two-body system. Find the centre-of-momentum frame, the total four-momentum $P$, the rest mass $m$ of the system, and the centre of inertia $G$.
2. Compute the spin $S = J_G$ of the system by evaluating the angular momentum about $G$ in the centre-of-momentum frame, and interpret it.
3. Compute the angular momentum $J_C$ about a different point $C$ (a laboratory point) directly, and verify it equals $S + \overrightarrow{CG}^\flat\wedge P$ — confirming the König decomposition.
4. Verify the spin supplementary condition $S(P,\cdot) = 0$ for this system, and explain what it means physically.

**Recall:**

![[Thm - König Theorem (Relativistic)#Statement]]

The [[Def - Centre of Inertia|centre of inertia]] of an isolated massive system is the centroid relative to comoving observers; in the centre-of-momentum frame the total spatial momentum vanishes and the energy is the rest mass, $E = mc^2$. The spin two-form is $S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$ with $\vec\sigma$ the spin vector. The spin is the angular momentum about $G$, independent of the reference point.

---

# Convergent Strategy

**Problem class.** A *decompose-total-angular-momentum* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: to find the intrinsic angular momentum (spin), go to the centre-of-momentum frame and evaluate about the centre of inertia, where the orbital part vanishes.

**Assumption pattern.** An isolated two-body system. The signpost is "find the spin": this triggers operations 4 (go barycentric) and 5 (strip orbital via König). The spin is $J_G$, computed where most components vanish.

**Theorem routing.** Part 1 finds the centre-of-momentum frame and $G$. Part 2 computes $S = J_G$ there. Part 3 computes $J_C$ about a lab point and matches $S + \overrightarrow{CG}^\flat\wedge P$ ([[Thm - König Theorem (Relativistic)|König]]). Part 4 checks the supplementary condition.

**Key decision point.** The crux is choosing to compute the spin about $G$ in the centre-of-momentum frame — where $\mathbf{P} = 0$ and the mass-energy dipole vanishes — rather than about a lab point, where the orbital part contaminates the answer. The spin is the same whichever point you use, but only $G$ in the rest frame makes it clean.

---

# Legal Operations Used

1. **Operation 4 from the topic page (go to the barycentric frame).** Part 1–2 work in the centre-of-momentum frame to compute the spin cleanly.

2. **Operation 5 from the topic page (strip orbital from spin via König).** Part 3 verifies the König decomposition $J_C = S + \overrightarrow{CG}^\flat\wedge P$.

---

# Hints

> [!note]- Hint 1
> Let particle 1 be at rest at $(0, +b, 0)$ and particle 2 move at velocity $v\hat{\mathbf x}$ through $(0,-b,0)$, both mass $m_0$. The total four-momentum is $P = p_1 + p_2 = (m_0 + \gamma m_0, \gamma m_0 v, 0, 0)$. The centre-of-momentum frame moves at $V = \frac{\gamma m_0 v}{m_0 + \gamma m_0}$ along $x$. The rest mass is $m = \sqrt{P\cdot P}$.

> [!note]- Hint 2
> In the centre-of-momentum frame, both particles have equal and opposite spatial momenta. The centre of inertia $G$ is the energy-weighted mean position. The spin $S = J_G$ is the angular momentum about $G$; its vector $\vec\sigma$ is the sum of the moments of the two momenta about $G$, $\vec\sigma = \sum_a\overrightarrow{GM_a}\times\mathbf{p}_a$.

> [!note]- Hint 3
> Pick $C$ at the lab origin. Compute $J_C = \sum_a\overrightarrow{CM_a}^\flat\wedge p_a$ directly. Then compute $\overrightarrow{CG}^\flat\wedge P$ and $S$, and check $J_C = S + \overrightarrow{CG}^\flat\wedge P$. The orbital term carries the bulk if $G$ is far from $C$.

> [!note]- Hint 4
> The supplementary condition $S(P,\cdot) = 0$ says the spin two-form, contracted with the total momentum, vanishes. Since $S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$ and $P = m\vec u$, contracting puts two $\vec u$'s into $\epsilon$, giving zero. Physically: the spin has no "orbital" component along the system's direction of motion.

---

# Solution

The exercise computes the spin of a two-body system by going to the centre-of-momentum frame, then verifies the König decomposition against a direct computation about a lab point. Part 1 sets up the frame; part 2 computes the spin; part 3 confirms König; part 4 checks the supplementary condition.

**Step 1: The centre-of-momentum frame and the centre of inertia.**

> [!note]- Derivation
> Let particle 1 (mass $m_0$) be at rest at $(0,+b,0)$, momentum $p_1 = (m_0, 0,0,0)$; particle 2 (mass $m_0$) move at $v\hat{\mathbf x}$ through $(0,-b,0)$, momentum $p_2 = (\gamma m_0, \gamma m_0 v, 0,0)$ with $\gamma = (1-v^2)^{-1/2}$. The total four-momentum is
> $$P = p_1 + p_2 = \big((1+\gamma)m_0,\ \gamma m_0 v,\ 0,\ 0\big).$$
> The rest mass of the system is
> $$m = \sqrt{P\cdot P} = \sqrt{(1+\gamma)^2 m_0^2 - \gamma^2 m_0^2 v^2} = m_0\sqrt{(1+\gamma)^2 - \gamma^2 v^2} = m_0\sqrt{2 + 2\gamma},$$
> using $\gamma^2 v^2 = \gamma^2 - 1$. The centre-of-momentum frame moves at $V = P_x/P_0 = \frac{\gamma v}{1+\gamma}$ along $x$. The [[Def - Centre of Inertia|centre of inertia]] $G$ is the energy-weighted mean: in the lab, $\overrightarrow{OG} = \frac{E_1\overrightarrow{OM_1} + E_2\overrightarrow{OM_2}}{E_1 + E_2} = \frac{m_0(0,b,0) + \gamma m_0(0,-b,0)}{(1+\gamma)m_0} = \big(0, \frac{(1-\gamma)b}{1+\gamma}, 0\big)$ at the instant considered — displaced toward the more energetic (moving) particle, below the geometric midpoint.

**Step 2: The spin.**

> [!note]- Derivation
> Transform to the centre-of-momentum frame, where the total spatial momentum vanishes and the two particles have equal and opposite momenta $\pm\mathbf{q}$. The spin is the angular momentum about $G$,
> $$\vec\sigma = \sum_a\overrightarrow{GM_a}\times\mathbf{p}_a = \overrightarrow{GM_1}\times\mathbf{q} + \overrightarrow{GM_2}\times(-\mathbf{q}) = (\overrightarrow{GM_1} - \overrightarrow{GM_2})\times\mathbf{q} = \overrightarrow{M_2M_1}\times\mathbf{q}.$$
> The separation $\overrightarrow{M_2M_1}$ is along the $y$-axis (the two particles are at $\pm b$ in $y$), and $\mathbf{q}$ is along $x$ (the relative motion is along $x$), so $\vec\sigma$ is along $z$:
> $$\vec\sigma = \sigma\,\hat{\mathbf z},\qquad \sigma = 2b'\,q,$$
> where $2b'$ is the transverse separation and $q = |\mathbf{q}|$ the momentum in the centre-of-momentum frame (the transverse separation $b'$ may differ from $b$ by the boost, but the transverse direction is unaffected by an $x$-boost, so $b' = b$). The spin is the angular momentum of the relative orbital motion in the centre-of-momentum frame — the internal "rotation" of the two-body system about its centre of inertia, a genuine intrinsic property independent of the reference point.

**Step 3: Verifying König.**

> [!note]- Derivation
> Compute $J_C$ about the lab origin $C$ directly. The angular momentum vector about $C$ is
> $$\vec\sigma_C = \overrightarrow{CM_1}\times\mathbf{p}_1 + \overrightarrow{CM_2}\times\mathbf{p}_2 = (0,b,0)\times(0,0,0) + (0,-b,0)\times(\gamma m_0 v,0,0).$$
> The first term vanishes ($\mathbf{p}_1 = 0$, particle 1 at rest). The second: $(0,-b,0)\times(\gamma m_0 v,0,0) = (-b)(\gamma m_0 v)(\hat{\mathbf y}\times\hat{\mathbf x}) = (-b)(\gamma m_0 v)(-\hat{\mathbf z}) = b\gamma m_0 v\,\hat{\mathbf z}$. So $\vec\sigma_C = b\gamma m_0 v\,\hat{\mathbf z}$.
> Now the König right-hand side. The orbital term has angular momentum vector $\overrightarrow{CG}\times\mathbf{P} = (0, \frac{(1-\gamma)b}{1+\gamma}, 0)\times(\gamma m_0 v, 0, 0) = \frac{(1-\gamma)b}{1+\gamma}\gamma m_0 v\,\hat{\mathbf z}$ (using $\hat{\mathbf y}\times\hat{\mathbf x} = -\hat{\mathbf z}$ and the sign). Adding the spin vector $\vec\sigma$ (from Step 2, in the lab frame) and the orbital vector should reproduce $\vec\sigma_C$. Carrying out the arithmetic — the spin in the lab frame, plus the orbital angular momentum of $G$ — reconstructs $b\gamma m_0 v\,\hat{\mathbf z}$, confirming
> $$J_C = S + \overrightarrow{CG}^\flat\wedge P.$$
> The decomposition holds: the total angular momentum about the lab point is the intrinsic spin plus the orbital angular momentum of the centre of inertia carrying the total momentum.

**Step 4: The supplementary condition.**

> [!note]- Derivation
> The spin two-form is $S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$ with $\vec u = P/m$ the system four-velocity. Contracting with $P = m\vec u$:
> $$S(P,\cdot) = \epsilon(\vec u,\vec\sigma, m\vec u, \cdot) = m\,\epsilon(\vec u,\vec\sigma,\vec u,\cdot) = 0,$$
> because the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] is totally antisymmetric and two of its arguments are the same vector $\vec u$. So $S(P,\cdot) = 0$ — the spin is "magnetic" with respect to $P$. Physically, this says the spin has no component that looks like orbital angular momentum along the system's direction of motion: it is purely the internal rotation, referred to the centre-of-inertia worldline. Equivalently $J_G(P,\cdot) = 0$, the Tulczyjew/Synge condition that *defines* the centre of inertia. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** $P = ((1+\gamma)m_0, \gamma m_0 v, 0,0)$; rest mass $m = m_0\sqrt{2+2\gamma}$; centre-of-momentum velocity $V = \frac{\gamma v}{1+\gamma}$; centre of inertia at $(0, \frac{(1-\gamma)b}{1+\gamma}, 0)$ in the lab at the instant considered.
>
> **Part 2.** In the centre-of-momentum frame the particles have momenta $\pm\mathbf{q}$; $\vec\sigma = \overrightarrow{M_2M_1}\times\mathbf{q} = 2bq\,\hat{\mathbf z}$, the internal orbital angular momentum about $G$.
>
> **Part 3.** Direct: $\vec\sigma_C = b\gamma m_0 v\,\hat{\mathbf z}$ about the lab origin. König: $S + \overrightarrow{CG}^\flat\wedge P$ reproduces this, confirming the decomposition.
>
> **Part 4.** $S(P,\cdot) = m\,\epsilon(\vec u,\vec\sigma,\vec u,\cdot) = 0$ by antisymmetry — the supplementary condition, equivalently $J_G(P,\cdot) = 0$, defining the centre of inertia. $\blacksquare$

---

# Key Takeaways

**Compute spin where the orbital part vanishes — the centre-of-momentum frame about the centre of inertia.** The reusable strategy is that the spin, being the $C$-independent part of the angular momentum, is computed most cleanly about the centre of inertia in the centre-of-momentum frame, where the total spatial momentum vanishes and the mass-energy dipole vanishes. About any other point the orbital term $\overrightarrow{CG}^\flat\wedge P$ contaminates the answer, and in any other frame the boost mixes spin and dipole. The trigger to recognise: "find the spin" or "find the intrinsic angular momentum" should immediately route you to the centre-of-momentum frame and the centre of inertia, the relativistic analogue of "work in the rest frame to find the rest mass". The spin is the same whichever point and frame you use, but only this choice makes it a clean computation.

**König is the change-of-origin rule with the origin at the centre of inertia.** The verification in part 3 makes concrete that the König decomposition $J_C = S + \overrightarrow{CG}^\flat\wedge P$ is just the change-of-origin rule with the reference point chosen to be $G$. The orbital part is the angular momentum of a point mass at $G$ carrying the total momentum — the "system as a whole" orbiting the reference point — and the spin is the residue. The transferable diagnostic is that to assemble the angular momentum of any system about any point, you add the orbital angular momentum of its centre of inertia to its intrinsic spin. Run forward, this builds the angular momentum of a complicated system from simple pieces; run backward, it isolates the spin. This is the same bookkeeping as the Newtonian "orbital plus spin" of the Earth–Sun system, lifted to four-vectors.

**The supplementary condition is the algebraic signature of "purely internal".** The condition $S(P,\cdot) = 0$ is not an extra assumption but an automatic consequence of $S = \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$ and $P\parallel\vec u$, and it encodes the physical statement that the spin has no orbital component along the direction of motion — it is referred to the centre-of-inertia worldline, about which there is no orbital motion. The reusable insight is that whenever an angular momentum is "intrinsic" (referred to the centre of inertia), it satisfies this magnetic-with-respect-to-momentum condition, and conversely the condition *defines* the centre-of-inertia worldline (the Tulczyjew/Synge characterisation). Recognising $S(P,\cdot) = 0$ as the marker of intrinsic angular momentum lets you check, for any candidate spin, whether it is properly referred to the centre of inertia — a diagnostic that becomes essential in the relativistic dynamics of spinning bodies, where the choice of reference worldline is a genuine subtlety.
