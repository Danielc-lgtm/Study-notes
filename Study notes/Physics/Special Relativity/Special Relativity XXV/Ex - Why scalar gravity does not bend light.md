---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Nordström's Scalar Theory of Gravity"
  - "Thm - Light Deflection"
  - "Def - The Electromagnetic Field Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

In Nordström's scalar theory of gravity the gravitational field $\Phi$ couples to matter only through the interaction Lagrangian $\mathscr{L}_{\mathrm{inter}} = \tfrac{1}{c^3}\Phi T$, where $T = T^\mu{}_\mu$ is the trace of the energy-momentum tensor.

1. Compute the trace $T^{\mathrm{em}} = T^{\mathrm{em}\,\mu}{}_\mu$ of the electromagnetic energy-momentum tensor $T^{\mathrm{em}}_{\mu\nu} = \varepsilon_0\big(F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14\eta_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\big)$ and show it vanishes identically.
2. Conclude that the electromagnetic field — and therefore light — produces no scalar gravitational field and feels none, so scalar gravity predicts *no* deflection of light.
3. Contrast with general relativity, which predicts $\delta\theta = 1.75''$ for a ray grazing the Sun, and explain why light deflection is the cleanest observational discriminator between scalar gravity and general relativity.
4. Express the tracelessness as a statement about the *conformal invariance* of electromagnetism, and explain the connection to the absence of light bending.

**Recall:**

In [[Def - Nordström's Scalar Theory of Gravity|Nordström's scalar theory]] the source of the field equation is the trace $T$, and matter couples to $\Phi$ only through $T$; matter with $T = 0$ is invisible to scalar gravity.

![[Thm - Light Deflection#Statement]]

The **electromagnetic field tensor** $F_{\mu\nu}$ ([[Def - The Electromagnetic Field Tensor]]) is antisymmetric; its energy-momentum tensor is $T^{\mathrm{em}}_{\mu\nu} = \varepsilon_0(F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14\eta_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta})$, and the two field invariants are $F_{\mu\nu}F^{\mu\nu} \propto B^2 - E^2$ and ${}^\star F_{\mu\nu}F^{\mu\nu} \propto \vec E\cdot\vec B$. The trace uses $\eta^{\mu\nu}\eta_{\mu\nu} = \delta^\mu_\mu = 4$.

---

# Convergent Strategy

**Problem class.** A *test-a-theory-by-an-observation* problem: confront a candidate gravity theory with a requirement (it must bend light) and find it fails. The computation reduces to a one-line trace, but the *significance* — that this single fact kills the scalar theory — is the point.

**Assumption pattern.** The given is that scalar gravity couples only to the trace $T$. The recognisable feature is that the electromagnetic stress tensor has a very particular structure (the $-\tfrac14\eta_{\mu\nu}F^2$ term is engineered to make it traceless), so computing its trace is the whole problem. The condition $\eta^{\mu\nu}\eta_{\mu\nu} = 4$ in four dimensions is what makes the cancellation exact — it would fail in any other dimension.

**Theorem routing.** Compute $T^{\mathrm{em}}$ by contracting $T^{\mathrm{em}}_{\mu\nu}$ with $\eta^{\mu\nu}$ ([[Def - The Electromagnetic Field Tensor]]); the two terms cancel because of the factor $\tfrac14\cdot 4 = 1$. Then [[Def - Nordström's Scalar Theory of Gravity|the scalar coupling]] gives zero interaction, hence no field and no force on light, hence no deflection ([[Thm - Light Deflection]]).

**Key decision point.** The crux is recognising that the deflection question reduces to a *trace* question — that whether light bends in scalar gravity is decided entirely by whether $T^{\mathrm{em}}$ has a trace, with no need to solve any field equation or compute any trajectory. The natural (harder) alternative — trying to compute the actual light path in the scalar field — is unnecessary: the trace being zero means there *is* no field for light to bend in.

---

# Legal Operations Used

1. **Compute the trace of the energy-momentum tensor** (operation 3 from the topic page): the entire problem is the trace $T^{\mathrm{em}} = \eta^{\mu\nu}T^{\mathrm{em}}_{\mu\nu}$, which vanishes; matter with zero trace is invisible to scalar gravity.

2. **Identify a conformal rescaling / conformal invariance** (operation 9 from the topic page): the tracelessness of $T^{\mathrm{em}}$ is the conformal invariance of electromagnetism, and a conformally-invariant field is precisely one that ignores a conformal (scalar) gravitational field, which is what Nordström's theory is in the Einstein-Fokker picture.

---

# Hints

> [!note]- Hint 1
> Contract the stress tensor with $\eta^{\mu\nu}$. The first term gives $\eta^{\mu\nu}F_{\mu\alpha}F_\nu{}^\alpha = F^{\nu}{}_\alpha F_\nu{}^\alpha = F_{\nu\alpha}F^{\nu\alpha}$. The second gives $-\tfrac14(\eta^{\mu\nu}\eta_{\mu\nu})F_{\alpha\beta}F^{\alpha\beta}$, and $\eta^{\mu\nu}\eta_{\mu\nu} = 4$.

> [!note]- Hint 2
> So $T^{\mathrm{em}} = \varepsilon_0(F_{\nu\alpha}F^{\nu\alpha} - \tfrac14\cdot 4\cdot F_{\alpha\beta}F^{\alpha\beta}) = \varepsilon_0(F^2 - F^2) = 0$, since $F_{\nu\alpha}F^{\nu\alpha}$ and $F_{\alpha\beta}F^{\alpha\beta}$ are the same scalar.

> [!note]- Hint 3
> Because the scalar field couples only via $\Phi T$ and $T^{\mathrm{em}} = 0$, the interaction Lagrangian for the electromagnetic field vanishes: light neither sources $\Phi$ nor responds to it. No coupling means no force means no deflection.

> [!note]- Hint 4
> The factor $\tfrac14$ and the dimension $4$ conspire: tracelessness holds precisely in four dimensions, and it is the infinitesimal statement that electromagnetism is invariant under conformal rescalings $\eta \to \Omega^2\eta$. Nordström's metric is conformal to $\eta$, and a conformally-invariant field cannot tell it apart from flat space — so light is unbent.

---

# Solution

The argument is short and decisive. Step 1 computes the trace and finds it zero. Step 2 draws the immediate consequence: light decouples from scalar gravity. Step 3 contrasts with general relativity's nonzero deflection, making this the discriminating test. The non-obvious move is realising the whole deflection question collapses to a trace computation.

**Step 1: The electromagnetic stress tensor is traceless.**

> [!note]- Derivation
> Contract $T^{\mathrm{em}}_{\mu\nu} = \varepsilon_0(F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14\eta_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta})$ with $\eta^{\mu\nu}$:
> $$T^{\mathrm{em}} = \eta^{\mu\nu}T^{\mathrm{em}}_{\mu\nu} = \varepsilon_0\Big(\eta^{\mu\nu}F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14\,\eta^{\mu\nu}\eta_{\mu\nu}\,F_{\alpha\beta}F^{\alpha\beta}\Big).$$
> The first term: $\eta^{\mu\nu}F_{\mu\alpha}F_\nu{}^\alpha = F^\nu{}_\alpha F_\nu{}^\alpha = F_{\nu\alpha}F^{\nu\alpha}$ (raising the $\mu$ index on the first $F$). The second term uses $\eta^{\mu\nu}\eta_{\mu\nu} = \delta^\mu_\mu = 4$ in four dimensions:
> $$T^{\mathrm{em}} = \varepsilon_0\Big(F_{\nu\alpha}F^{\nu\alpha} - \tfrac14\cdot 4\cdot F_{\alpha\beta}F^{\alpha\beta}\Big) = \varepsilon_0\big(F_{\nu\alpha}F^{\nu\alpha} - F_{\alpha\beta}F^{\alpha\beta}\big) = 0,$$
> since $F_{\nu\alpha}F^{\nu\alpha}$ and $F_{\alpha\beta}F^{\alpha\beta}$ are the same scalar (dummy indices). The trace vanishes **identically** — for any electromagnetic field whatsoever. The $-\tfrac14\eta_{\mu\nu}F^2$ term is precisely engineered, with the factor $\tfrac14$, so that in $d = 4$ dimensions the trace cancels.

**Step 2: Light does not couple to scalar gravity.**

> [!note]- Derivation
> In [[Def - Nordström's Scalar Theory of Gravity|Nordström's theory]] the interaction Lagrangian between the gravitational field and any matter is $\mathscr{L}_{\mathrm{inter}} = \tfrac{1}{c^3}\Phi T$, proportional to the trace $T$ of that matter's energy-momentum tensor. For the electromagnetic field $T^{\mathrm{em}} = 0$, so
> $$\mathscr{L}_{\mathrm{inter}}^{\mathrm{em}} = \frac{1}{c^3}\Phi\,T^{\mathrm{em}} = 0$$
> identically. The electromagnetic field thus neither sources the scalar field (it contributes nothing to $\Box\Phi = -4\pi G T/c^2$) nor experiences any gravitational force (there is no interaction term to vary). Light is completely decoupled from scalar gravity. Therefore a light ray passing a massive body in Nordström's theory travels in a straight line: $\delta\theta_{\mathrm{scalar}} = 0$. **No deflection.**

**Step 3: The discriminating test against general relativity.**

> [!note]- Derivation
> General relativity, by contrast, couples gravity to the *full* energy-momentum tensor through the metric, not merely to its trace, so light — which carries energy and momentum even though its stress is traceless — does respond. The general-relativistic deflection for a ray grazing the Sun is ([[Thm - Light Deflection]])
> $$\delta\theta_{\mathrm{GR}} = \frac{4GM_\odot}{R_\odot c^2} = 1.75''.$$
> The two theories give starkly different predictions for the *same* observation:
> $$\delta\theta_{\mathrm{scalar}} = 0 \qquad\text{versus}\qquad \delta\theta_{\mathrm{GR}} = 1.75''.$$
> The 1919 eclipse measured a nonzero deflection consistent with $1.75''$, which simultaneously *confirmed* general relativity and *refuted* Nordström's scalar theory. This is why light deflection is the cleanest discriminator: the redshift cannot distinguish them (every metric theory, including Nordström's, predicts a redshift — see [[Thm - Gravitational Redshift]]), but the deflection does, because it tests how light couples to gravity, and light couples to the trace (zero) in scalar gravity but to the full tensor (nonzero) in general relativity.

**Step 4: Tracelessness as conformal invariance.**

> [!note]- Derivation
> The vanishing of $T^{\mathrm{em}}$ in four dimensions is the infinitesimal statement of the **conformal invariance** of source-free electromagnetism: Maxwell's equations in vacuum are invariant under a position-dependent rescaling of the metric $\eta \to \Omega^2(x)\,\eta$, and the trace of the stress tensor is the generator of such rescalings, so conformal invariance $\Leftrightarrow$ traceless stress. Now recall that Nordström's theory, in the Einstein-Fokker form, has physical metric $\tilde g = (1+\Phi/c^2)^2\eta = \Omega^2\eta$ — a conformal rescaling of $\eta$. A conformally-invariant field cannot distinguish $\tilde g$ from $\eta$: its dynamics are identical in the two, so it propagates exactly as in flat space. Light, being conformally invariant, sees Nordström's "curved" metric as flat and travels in straight lines. The absence of light bending is therefore not an accident of the trace computation but the deep statement that *electromagnetism does not feel a conformal (scalar) gravitational field*, because both are conformally invariant. General relativity's metric is *not* merely conformal to $\eta$ (it has nonzero Weyl curvature), which is exactly why it bends light where Nordström's does not.

> [!note]- Complete formal solution
> Contracting $T^{\mathrm{em}}_{\mu\nu} = \varepsilon_0(F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14\eta_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta})$ with $\eta^{\mu\nu}$ gives $T^{\mathrm{em}} = \varepsilon_0(F_{\nu\alpha}F^{\nu\alpha} - \tfrac14\cdot 4\,F_{\alpha\beta}F^{\alpha\beta}) = 0$, using $\eta^{\mu\nu}\eta_{\mu\nu} = 4$. Since Nordström's theory couples gravity to matter only through $\mathscr{L}_{\mathrm{inter}} = \tfrac{1}{c^3}\Phi T$, the electromagnetic field has $\mathscr{L}_{\mathrm{inter}}^{\mathrm{em}} = 0$: light neither sources nor feels the scalar field, so $\delta\theta_{\mathrm{scalar}} = 0$. General relativity couples to the full stress tensor and gives $\delta\theta_{\mathrm{GR}} = 4GM_\odot/(R_\odot c^2) = 1.75''$ for a grazing solar ray; the 1919 eclipse measured this, refuting scalar gravity. The tracelessness is the conformal invariance of electromagnetism, and since Nordström's metric is conformal to $\eta$, light cannot tell it from flat space — hence no bending. $\blacksquare$

---

# Key Takeaways

**A traceless stress tensor is invisible to scalar gravity — this single fact decides the fate of the scalar theory.** The deepest lesson is that whether matter gravitates in a scalar theory is decided entirely by its trace, and the electromagnetic field (and any conformally invariant matter, i.e. radiation) is traceless, hence decoupled. The trigger to deploy this: any question about how light or radiation interacts with a scalar field — the answer is "it does not", because the coupling is to the trace and the trace is zero. This is why the scalar theory, despite being mathematically well-posed and reproducing Newtonian gravity, is observationally dead: it cannot bend light, and light bending is observed. The same tracelessness underlies the conformal anomaly, the masslessness of the photon under scale transformations, and the decoupling of radiation from any scalar (dilaton) field — one structural fact with consequences across gravity and field theory.

**Reduce a hard dynamical question to an algebraic one whenever a coupling vanishes.** The exercise looks like it should require computing a light trajectory in a gravitational field — a hard problem. Instead it collapses to a one-line trace: if the coupling vanishes, there is no force, and no trajectory computation is needed. The reusable diagnostic: before solving the equations of motion, check whether the relevant coupling is even nonzero — a vanishing coupling (here, a vanishing trace) settles the dynamics instantly. This pattern recurs whenever a symmetry or a structural identity (tracelessness, a selection rule, a conservation law) forbids an interaction: the "computation" is to verify the coupling is zero, after which the answer is immediate. It is far more powerful than grinding through the dynamics, and it is how one recognises that scalar gravity gives *exactly* zero deflection, not merely a small one.

**Conformal invariance is the geometric statement of "blind to a scalar gravitational field".** The connection between tracelessness and conformal invariance is worth internalising as a two-way street: a field is conformally invariant if and only if its stress tensor is traceless, and a conformally-invariant field cannot distinguish a conformally-rescaled metric $\Omega^2\eta$ from $\eta$. Since Nordström's theory makes spacetime conformally flat ($\tilde g = (1+\Phi/c^2)^2\eta$), conformally-invariant light propagates as in flat space — no bending. This is the precise sense in which scalar gravity is "only able to rescale clocks, not tilt light cones": the conformal factor rescales proper times (giving a redshift) but preserves null cones (giving no deflection). The general lesson for distinguishing gravity theories: the redshift tests the conformal (time) part of the metric, which every metric theory has, while light deflection tests the *non-conformal* (Weyl curvature) part, which only general relativity has — so deflection is the discriminating observable.
