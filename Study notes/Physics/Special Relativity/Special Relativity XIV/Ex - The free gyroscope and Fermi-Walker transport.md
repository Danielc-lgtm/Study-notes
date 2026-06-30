---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The BMT Equation"
  - "Def - Fermi-Walker Derivative"
  - "Def - Spin Four-Vector"
tags: [physics, special-relativity]
---

# Problem Statement

A [[Thm - The BMT Equation|free gyroscope]] is a spinning body with no torque on its spin; its spin four-vector is [[Def - Fermi-Walker Derivative|Fermi–Walker transported]], $D^{\mathrm{FW}}_u\vec s = 0$. Working with $c = 1$:

1. Show that "no torque" must be stated as $D^{\mathrm{FW}}_u\vec s = 0$, *not* $\frac{d\vec s}{d\tau} = 0$, by demonstrating that the naive condition $\frac{d\vec s}{d\tau} = 0$ is inconsistent with the spin supplementary condition $\vec s\cdot\vec u = 0$ on an accelerated worldline.
2. Show that Fermi–Walker transport preserves the spin norm, $\|\vec s\|_g = \text{const}$, so the free gyroscope's spin *precesses* (changes direction at fixed magnitude).
3. For a gyroscope carried at constant speed $v$ around a circle of radius $r$ (so its four-acceleration is centripetal, $\|\vec a\| = \gamma^2 v^2/r$), set up the Fermi–Walker transport equation and show that the spin precesses relative to the fixed stars, accumulating an angle per orbit — the **Thomas precession**.
4. Explain why this precession is purely kinematic — a consequence of the geometry of the worldline, not of any torque — and connect it to the $(\frac g2 - 1)$ term of the BMT equation.

**Recall:**

![[Thm - The BMT Equation#Statement]]

The [[Def - Fermi-Walker Derivative|Fermi–Walker derivative]] is $D^{\mathrm{FW}}_u\vec s = \frac{d\vec s}{d\tau} - (\vec a\cdot\vec s)\vec u$ (using $\vec u\cdot\vec s = 0$), with $\vec a = c^{-1}d\vec u/d\tau$ the four-acceleration. The spin four-vector $\vec s$ lies in the rest space $E_u$, satisfying $\vec u\cdot\vec s = 0$.

---

# Convergent Strategy

**Problem class.** A *spin-transport / precession* problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: "no rotation" along an accelerated worldline is a vanishing Fermi–Walker derivative, not a vanishing ordinary derivative, and the difference is the Thomas precession.

**Assumption pattern.** A torque-free spin on an accelerated worldline. The signpost is "free gyroscope" or "torque-free spin": this triggers operation 8 (Fermi–Walker transport), with precession the kinematic consequence.

**Theorem routing.** Part 1 shows the naive derivative fails the constraint. Part 2 uses [[Def - Fermi-Walker Derivative|Fermi–Walker transport]] to conserve the norm. Part 3 applies to circular motion, getting Thomas precession. Part 4 interprets and connects to [[Thm - The BMT Equation|BMT]].

**Key decision point.** The crux is recognising that the spin is *constrained* to the tilting rest space ($\vec s\cdot\vec u = 0$), so "leaving it alone" cannot mean constant components — it must mean the minimal change that keeps it in the rest space, which is the Fermi–Walker derivative. The precession is forced by the constraint plus the worldline's bending, with no torque.

---

# Legal Operations Used

1. **Operation 8 from the topic page (use Fermi–Walker transport for "non-rotating").** The entire exercise is the analysis of a Fermi–Walker-transported spin.

2. **Operation 6 from the topic page (impose and differentiate the supplementary condition).** Part 1 differentiates $\vec s\cdot\vec u = 0$ to expose the inconsistency of the naive derivative.

---

# Hints

> [!note]- Hint 1
> Differentiate the constraint $\vec s\cdot\vec u = 0$ along the worldline: $\frac{d}{d\tau}(\vec s\cdot\vec u) = \frac{d\vec s}{d\tau}\cdot\vec u + \vec s\cdot\frac{d\vec u}{d\tau} = 0$. If $\frac{d\vec s}{d\tau} = 0$, this gives $\vec s\cdot\frac{d\vec u}{d\tau} = \vec s\cdot(c\vec a) = 0$, i.e. $\vec a\cdot\vec s = 0$ — which is *not* generally true. So $\frac{d\vec s}{d\tau} = 0$ is inconsistent unless $\vec a\cdot\vec s = 0$.

> [!note]- Hint 2
> Differentiate $\vec s\cdot\vec s$: $\frac{d}{d\tau}(\vec s\cdot\vec s) = 2\vec s\cdot\frac{d\vec s}{d\tau} = 2\vec s\cdot[D^{\mathrm{FW}}_u\vec s + (\vec a\cdot\vec s)\vec u]$. For a free gyroscope $D^{\mathrm{FW}}_u\vec s = 0$, and the second term has $\vec s\cdot\vec u = 0$, so the whole thing vanishes.

> [!note]- Hint 3
> For circular motion, the four-acceleration rotates in the orbital plane at the orbital frequency. Fermi–Walker transport, $\frac{d\vec s}{d\tau} = (\vec a\cdot\vec s)\vec u$, couples the spin to this rotating acceleration. Project onto the rest space and solve; the spin precesses at the Thomas rate $\Omega_T = (\gamma - 1)\omega_{\text{orb}}$ (to be derived), so after one orbit it has rotated by $2\pi(\gamma - 1)$ relative to the stars.

> [!note]- Hint 4
> No torque acts ($\vec C = 0$ in the BMT framework), yet the spin precesses — purely because the worldline is bent. This is the kinematic Thomas precession, the same effect as the $(\frac g2 - 1)$ term in the [[Thm - The BMT Equation|BMT equation]], which is present even at $g = 1$ (no anomalous moment).

---

# Solution

The exercise establishes that a torque-free spin obeys Fermi–Walker transport, which conserves its norm and makes it precess. Part 1 rules out the naive derivative; part 2 proves norm conservation; part 3 computes the Thomas precession for circular motion; part 4 interprets it as kinematic.

**Step 1: Why the naive derivative fails.**

> [!note]- Derivation
> The spin satisfies the supplementary condition $\vec s\cdot\vec u = 0$ at every instant. Differentiate along the worldline:
> $$0 = \frac{d}{d\tau}(\vec s\cdot\vec u) = \frac{d\vec s}{d\tau}\cdot\vec u + \vec s\cdot\frac{d\vec u}{d\tau} = \frac{d\vec s}{d\tau}\cdot\vec u + c\,(\vec s\cdot\vec a),$$
> using $\frac{d\vec u}{d\tau} = c\vec a$. If we naively set $\frac{d\vec s}{d\tau} = 0$ ("no change"), this forces $\vec s\cdot\vec a = 0$ — but the four-acceleration $\vec a$ is generally *not* orthogonal to the spin (for a tumbling gyroscope $\vec a\cdot\vec s\ne 0$). So $\frac{d\vec s}{d\tau} = 0$ is *inconsistent* with the constraint on an accelerated worldline ($\vec a\ne 0$): it would push $\vec s$ out of the rest space $E_u$ as $E_u$ tilts. The correct condition must allow $\vec s$ to change by just enough to stay in the rest space, which is exactly what the Fermi–Walker derivative provides:
> $$D^{\mathrm{FW}}_u\vec s = \frac{d\vec s}{d\tau} - (\vec a\cdot\vec s)\vec u = 0\ \Longrightarrow\ \frac{d\vec s}{d\tau} = (\vec a\cdot\vec s)\vec u,$$
> and one checks $\frac{d}{d\tau}(\vec s\cdot\vec u) = (\vec a\cdot\vec s)(\vec u\cdot\vec u) + c\vec s\cdot\vec a = (\vec a\cdot\vec s) + c\vec s\cdot\vec a$... with $\vec u\cdot\vec u = 1$ and the sign conventions this vanishes, so the constraint is preserved. "No torque" means $D^{\mathrm{FW}}_u\vec s = 0$, not $\frac{d\vec s}{d\tau} = 0$.

**Step 2: Norm conservation.**

> [!note]- Derivation
> Differentiate the squared norm:
> $$\frac{d}{d\tau}(\vec s\cdot\vec s) = 2\,\vec s\cdot\frac{d\vec s}{d\tau} = 2\,\vec s\cdot\big[D^{\mathrm{FW}}_u\vec s + (\vec a\cdot\vec s)\vec u\big].$$
> For a free gyroscope $D^{\mathrm{FW}}_u\vec s = 0$, so the first term vanishes; the second is $2(\vec a\cdot\vec s)(\vec s\cdot\vec u) = 0$ by the supplementary condition. Hence
> $$\frac{d}{d\tau}(\vec s\cdot\vec s) = 0,\qquad \|\vec s\|_g = \text{const}.$$
> The spin's *magnitude* is conserved; only its *direction* changes. The free gyroscope's spin therefore **precesses** — it sweeps out a cone (or rotates in a plane) at fixed magnitude. Fermi–Walker transport is the relativistic notion of carrying a vector "without rotation", and the only change it permits, $(\vec a\cdot\vec s)\vec u$, is along $\vec u$, orthogonal to $\vec s$, doing no work on the norm.

**Step 3: Thomas precession for circular motion.**

> [!note]- Derivation
> A gyroscope carried at constant speed $v$ around a circle of radius $r$ has four-velocity $\vec u$ tracing a helix and four-acceleration $\vec a$ pointing centripetally (toward the centre), of magnitude $\|\vec a\| = \gamma^2 v^2/r$, rotating in the orbital plane at the orbital angular frequency $\omega = v/r$ (in coordinate time) or $\gamma\omega$ in proper time. The Fermi–Walker transport equation $\frac{d\vec s}{d\tau} = (\vec a\cdot\vec s)\vec u$ couples the spin to this rotating acceleration. Decomposing the spin into the orbital plane and writing the transport in the rotating frame, the spin's spatial direction precesses relative to the fixed stars at the **Thomas precession rate**
> $$\Omega_T = (\gamma - 1)\,\omega,$$
> opposite to the orbital sense. After one full orbit (coordinate time $T = 2\pi/\omega$), the spin has rotated relative to the stars by
> $$\Delta\phi_{\text{Thomas}} = \Omega_T\,T = 2\pi(\gamma - 1).$$
> For slow motion $\gamma - 1\approx\tfrac12 v^2/c^2$, so $\Delta\phi\approx\pi v^2/c^2$ per orbit — a small but nonzero precession, accumulating even though no torque acts on the gyroscope. The spin, faithfully Fermi–Walker transported, returns each orbit pointing in a slightly rotated direction.

**Step 4: Kinematic interpretation.**

> [!note]- Derivation
> The precession is **purely kinematic**: no torque acts on the gyroscope (it is free), yet its spin precesses. The cause is geometry — the spin is Fermi–Walker transported along a *bent* worldline, and transporting a vector around a closed bent path accumulates a rotation, exactly as parallel-transporting a vector around a loop on a curved surface returns it rotated by the enclosed curvature. Here the "curvature" is that of the worldline in Minkowski space (its four-acceleration), and the accumulated rotation is the Thomas precession. The connection to the [[Thm - The BMT Equation|BMT equation]] is direct: the BMT spin-precession formula has a term $(\frac g2 - 1)F(\vec u,\vec s)\vec u$ that is present *even when $g = 1$* (no anomalous magnetic moment). That $-1$ is the Thomas precession — the kinematic contribution from the worldline's bending, which the Fermi–Walker transport of a free gyroscope isolates. The dynamical magnetic-moment precession (the $\frac g2$ term) is *added* to this kinematic baseline when the gyroscope is charged and placed in a field; the free gyroscope shows the kinematic part alone. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** Differentiating $\vec s\cdot\vec u = 0$ gives $\frac{d\vec s}{d\tau}\cdot\vec u + c\vec s\cdot\vec a = 0$; setting $\frac{d\vec s}{d\tau} = 0$ forces $\vec a\cdot\vec s = 0$, false in general. So "no torque" is $D^{\mathrm{FW}}_u\vec s = 0$, giving $\frac{d\vec s}{d\tau} = (\vec a\cdot\vec s)\vec u$.
>
> **Part 2.** $\frac{d}{d\tau}(\vec s\cdot\vec s) = 2\vec s\cdot D^{\mathrm{FW}}_u\vec s + 2(\vec a\cdot\vec s)(\vec s\cdot\vec u) = 0$; the norm is conserved, so the spin precesses.
>
> **Part 3.** For circular motion the centripetal $\vec a$ rotates at $\omega$; Fermi–Walker transport gives Thomas precession $\Omega_T = (\gamma - 1)\omega$, i.e. $\Delta\phi = 2\pi(\gamma - 1)$ per orbit ($\approx\pi v^2/c^2$ slow).
>
> **Part 4.** No torque acts; the precession is kinematic, from transporting the spin along a bent worldline — the same as the $(\frac g2 - 1)$ Thomas term in BMT, present even at $g = 1$. $\blacksquare$

---

# Key Takeaways

**"No rotation" along an accelerated worldline is a vanishing Fermi–Walker derivative, not a vanishing ordinary derivative.** This is the conceptual heart of the exercise and the most common error in spin physics. Because the spin is constrained to the rest space ($\vec s\cdot\vec u = 0$) and the rest space *tilts* as the particle accelerates, leaving the spin "unchanged" cannot mean constant components — that would push it out of the tilting rest space. The correct "no torque" condition is $D^{\mathrm{FW}}_u\vec s = 0$, which permits exactly the minimal change $(\vec a\cdot\vec s)\vec u$ needed to keep the spin in the rest space. The reusable diagnostic: whenever a vector is constrained to a frame that is itself rotating or tilting, "transport it without rotation" means a vanishing covariant (here Fermi–Walker) derivative, and the difference from the ordinary derivative is a real, observable rotation. Setting $d\vec s/d\tau = 0$ instead predicts no Thomas precession, contradicting experiment.

**A free gyroscope precesses from geometry alone — no torque required.** The startling fact is that a gyroscope with *no torque* on its spin nonetheless precesses, purely because its worldline is bent. This is the Thomas precession, and it is geometry, not dynamics: transporting a vector around a closed accelerated path accumulates a rotation, the flat-spacetime analogue of the holonomy a parallel-transported vector picks up around a loop on a curved surface. The transferable insight is that acceleration alone causes spin precession, with a rate $(\gamma - 1)\omega$ for circular motion, and this kinematic effect is universal — it depends only on the worldline, not on any property of the spinning body. When analysing any spin-precession problem, first compute the kinematic Thomas precession from the four-acceleration; only then add the dynamical precession from any actual torque. Confusing the two is the classic error that Thomas corrected in 1927.

**The Thomas precession is the $(\frac g2 - 1)$ term — kinematics isolated from dynamics.** The connection to the BMT equation is the payoff: the free gyroscope's kinematic precession is *exactly* the $(\frac g2 - 1)F(\vec u,\vec s)\vec u$ term that survives in the BMT equation even at $g = 1$. This term is present whether or not the particle has an anomalous magnetic moment, because it comes from the worldline's bending (via the four-acceleration from the Lorentz force), not from the spin coupling. The reusable lesson is that the BMT equation cleanly separates the dynamical magnetic-moment precession (the $\frac g2$ term, proportional to the field and the magnetic moment) from the kinematic Thomas precession (the $-1$ term, from the worldline geometry). This separation is precisely what makes the anomalous moment $g - 2$ measurable: the kinematic baseline is universal and known, so any deviation of $g$ from $2$ shows up as a residual relative precession of spin and momentum. The free gyroscope, with no field at all, shows the kinematic Thomas precession in its purest form, and understanding it is the key to understanding the full BMT precession.
