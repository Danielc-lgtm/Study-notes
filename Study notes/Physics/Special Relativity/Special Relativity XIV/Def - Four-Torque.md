---
type: definition
subject: special-relativity
prereqs:
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Four-Force"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. A particle $\mathscr{P}$ of mass $m > 0$ has [[Def - Worldline of a Particle|worldline]] $\mathscr{L}$, [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$, proper time $\tau$, and [[Def - Four-Momentum and Rest Mass|four-momentum]] $p = mU$. The [[Def - Four-Force|four-force]] acting on it is $f = dp/d\tau$. The [[Def - Angular Momentum Four-Tensor|angular momentum]] about an event $C$ is the two-form $J_C = \overrightarrow{CM}^\flat\wedge p$, with $\overrightarrow{CM}$ the displacement from $C$ to the particle's position $M$. The exterior product is $a\wedge b = a\otimes b - b\otimes a$. Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

---

# Axiom Motivation

For an isolated particle the [[Def - Angular Momentum Four-Tensor|angular momentum]] $J_C$ is constant along the worldline — that is the [[Thm - Conservation of Angular Momentum|conservation law]]. The question this definition answers is: when the particle is *not* isolated, when a [[Def - Four-Force|four-force]] acts on it, at what rate does its angular momentum change, and what drives that change? In Newtonian mechanics the answer is the torque, $\frac{d\mathbf{L}}{dt} = \boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$, and we want the relativistic, covariant version.

The desideratum is an object $N_C$ that (i) equals the proper-time rate of change of the angular momentum, $N_C = dJ_C/d\tau$, so that vanishing torque is equivalent to conservation; (ii) is built from the position and the four-force, generalising the moment $\mathbf{r}\times\mathbf{F}$; and (iii) reduces to the Newtonian torque in the appropriate limit. The natural candidate is forced by differentiating the definition of angular momentum.

Differentiate $J_C = \overrightarrow{CM}^\flat\wedge p$ along the worldline. By the Leibniz rule for the wedge,
$$
\frac{dJ_C}{d\tau} = \frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p + \overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau}.
$$
The first term is where the relativistic structure pays off. Since $\overrightarrow{CM}$ runs from a *fixed* event $C$ to the moving particle, $\frac{d\overrightarrow{CM}}{d\tau} = \frac{dM}{d\tau} = cU$ (the four-velocity), and $p = mU$ is parallel to $U$, so $cU\wedge p = cm\,U\wedge U = 0$. The first term vanishes identically — the displacement's rate of change is parallel to the momentum, and a vector wedged with itself is zero. This is a genuinely relativistic simplification: it is the statement that "the velocity is parallel to the momentum", $p = mU$, which has no role in the Newtonian torque derivation but here kills a whole term.

What remains is $\overrightarrow{CM}^\flat\wedge\frac{dp}{d\tau} = \overrightarrow{CM}^\flat\wedge f$, the wedge of the displacement with the four-force. This is the unique surviving combination, and it is manifestly the relativistic moment of the force about $C$. Its space-space block is exactly $\mathbf{r}\times\mathbf{F}$, recovering the Newtonian torque; its time-space block drives the evolution of the mass-energy dipole. So the definition $N_C := dJ_C/d\tau = \overrightarrow{CM}^\flat\wedge f$ is not a choice — it is what differentiating the angular momentum forces, with the relativistic identity $p\parallel U$ doing the work that makes only the moment-of-force term survive.

Why a two-form rather than a vector? For the same reason angular momentum itself is a two-form: in four dimensions the moment of a force has $\binom 42 = 6$ components, one per coordinate plane, and they form an antisymmetric tensor, not a vector. The Newtonian torque vector $\mathbf{r}\times\mathbf{F}$ is again the three-dimensional disguise of the space-space block.

---

# The Definition

Let $\mathscr{P}$ be a particle of mass $m > 0$, worldline $\mathscr{L}$, four-velocity $U$, proper time $\tau$, on which a [[Def - Four-Force|four-force]] $f = dp/d\tau$ acts. The **four-torque** (or **4-torque**) on $\mathscr{P}$ with respect to an event $C$ is the proper-time derivative of the angular momentum two-form,
$$
N_C \;:=\; \frac{dJ_C}{d\tau}.
$$
It is a field of antisymmetric bilinear forms (two-forms) along $\mathscr{L}$, of the same type as $J_C$. Carrying out the differentiation, using $\frac{d\overrightarrow{CM}}{d\tau} = cU$ and $p = mU$ (so that $\frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p = cm\,U^\flat\wedge U = 0$), gives the explicit form
$$
\boxed{\,N_C \;=\; \overrightarrow{CM}^\flat \wedge f\,}
$$
— the relativistic **moment of the four-force** about $C$. In components, $N_C^{\alpha\beta} = x^\alpha f^\beta - x^\beta f^\alpha$.

Relative to an observer, the four-torque splits like any two-form: its space-space block is the Newtonian torque $\overrightarrow{CM}\times\mathbf{F}$ (with $\mathbf{F}$ the spatial force), driving the angular momentum vector, and its time-space block drives the mass-energy dipole moment. The defining property is that **vanishing four-torque is equivalent to conservation of angular momentum**: $N_C = 0$ for all $\tau$ iff $J_C$ is constant along $\mathscr{L}$.

For the evolution of the *spin* of a particle with spin, the four-torque splits into an orbital part and a spin part: writing the angular momentum as $J_C = S + \overrightarrow{CM}^\flat\wedge p$ (the [[Thm - König Theorem (Relativistic)|König form]] for a single particle), one has
$$
N_C = N_{\text{spin}} + N_C^{\text{orb}},
\qquad
N_{\text{spin}} = \frac{dS}{d\tau},
\qquad
N_C^{\text{orb}} = \overrightarrow{CM}^\flat\wedge f,
$$
where $N_{\text{spin}}$, the **four-torque on the spin**, is independent of the reference point $C$, and $N_C^{\text{orb}}$ is the **orbital four-torque**.

---

# Relate to Other Fields / Compression

This is the **moment of a covector with respect to a point**, the exterior-algebra version of the Newtonian moment $\mathbf{r}\times\mathbf{F}$. The same construction $\overrightarrow{CM}^\flat\wedge(\cdot)$ appears wherever one takes the moment of a flux or current about a point — in the angular momentum balance of a continuous medium, the moment is $x^\mu T^{\lambda\nu} - x^\nu T^{\lambda\mu}$ built from the energy-momentum tensor.

In Hamiltonian mechanics the four-torque is the rate of change of the **moment map** of the Lorentz action under a non-symmetry perturbation: the angular momentum is conserved exactly when the perturbation respects Lorentz invariance, and the four-torque measures the failure. This is the dynamical face of the Noether correspondence developed in [[Special Relativity XV — The Principle of Least Action]].

**True name:** the four-torque is *the moment of the four-force*, $\overrightarrow{CM}^\flat\wedge f$ — and the operationally crucial fact is that the term involving $d\overrightarrow{CM}/d\tau$ drops out because the four-velocity is parallel to the four-momentum. When computing $dJ/d\tau$, do not carry the $d\overrightarrow{CM}/d\tau\wedge p$ term; it is always zero for a particle, and the entire change in angular momentum is the moment of the force.

---

# Examples / Corollaries

**Is an instance — the torque of the Lorentz force.** A charge $q$ in an electromagnetic field feels the [[Def - Four-Force|four-force]] $f = qF(\cdot,U)$, and the four-torque about $C$ is $N_C = \overrightarrow{CM}^\flat\wedge qF(\cdot,U)$. Its space-space block is the ordinary torque $\overrightarrow{CM}\times(q\mathbf{E} + q\mathbf{v}\times\mathbf{B})$ that a charged particle feels in laboratory electromagnetism, recovered as the spatial part of the covariant four-torque.

**Is an instance — zero torque for a central force.** If the four-force points along $\overrightarrow{CM}$ (a central force about $C$), then $N_C = \overrightarrow{CM}^\flat\wedge f = 0$ because the wedge of parallel vectors vanishes, and the angular momentum about $C$ is conserved. This is the relativistic version of "central forces conserve angular momentum", and it is why the angular momentum about the centre is constant in a relativistic Kepler problem.

**Is NOT an instance — the four-force itself.** The four-force $f = dp/d\tau$ is *not* the four-torque: it drives the *linear* momentum, not the angular momentum. The four-torque is its *moment*, $\overrightarrow{CM}^\flat\wedge f$, and depends on the reference point $C$ while $f$ does not. Confusing the two is confusing force with torque.

**Is NOT an instance — a symmetric "moment".** The symmetric combination $\overrightarrow{CM}^\flat\otimes f + f\otimes\overrightarrow{CM}^\flat$ is not a four-torque; only the antisymmetric wedge is, because it is the derivative of the antisymmetric angular momentum.

**Corollary — the dropped term.** For any particle, $\frac{d\overrightarrow{CM}^\flat}{d\tau}\wedge p = 0$, because $\frac{d\overrightarrow{CM}}{d\tau} = cU$ and $p = mU$ are parallel. Hence $N_C = \overrightarrow{CM}^\flat\wedge f$ exactly, with no contribution from the motion of the particle's position relative to $C$.

**Corollary — conservation criterion.** $J_C$ is constant along $\mathscr{L}$ iff $N_C = 0$ iff the four-force is either zero or parallel to $\overrightarrow{CM}$ at every instant. This is the precise statement of when angular momentum about a given point is conserved.

**Calibration check.** You should be able to: (1) derive $N_C = \overrightarrow{CM}^\flat\wedge f$ by differentiating $J_C = \overrightarrow{CM}^\flat\wedge p$ and explaining why the $d\overrightarrow{CM}/d\tau\wedge p$ term vanishes; (2) identify the space-space block of $N_C$ as the Newtonian torque $\mathbf{r}\times\mathbf{F}$; and (3) state the condition on the four-force for angular momentum about $C$ to be conserved.

---

# Unlocked by This

> [!tip] Spin Precession and the BMT Equation *(from Particle Physics)*
> Splitting the four-torque into orbital and spin parts isolates the **four-torque on the spin** $N_{\text{spin}} = dS/d\tau$, which is what drives spin precession. When the spin couples to an electromagnetic field through a magnetic moment, $N_{\text{spin}}$ becomes the torque in the [[Thm - The BMT Equation|Bargmann–Michel–Telegdi equation]], and the precession of an electron's or muon's spin is read directly from it. The four-torque of this page is the covariant origin of every spin-precession calculation, including the muon $g-2$ measurement.

> [!tip] The Angular Momentum Balance of a Continuum *(from Relativistic Hydrodynamics)*
> For a continuous medium the four-torque becomes the divergence of an **angular momentum current** $M^{\lambda\mu\nu} = x^\mu T^{\lambda\nu} - x^\nu T^{\lambda\mu}$ built from the energy-momentum tensor $T^{\mu\nu}$ of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]]. The local balance $\partial_\lambda M^{\lambda\mu\nu} = T^{\nu\mu} - T^{\mu\nu}$ says the rate of change of angular momentum density is the *antisymmetric part* of the stress tensor — so angular momentum is locally conserved precisely when $T^{\mu\nu}$ is symmetric. The four-torque of this page is the point-particle ancestor of that continuum balance law.
