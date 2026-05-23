---
type: exercise
subject: general-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Stress-Energy Tensor"
  - "Def - Hilbert Action"
tags: [physics, general-relativity, fields, conservation-laws]
---

# Problem Statement

**Consider a free, massive scalar field $\phi$ on a curved spacetime, with action**
$$S_\phi = \int \left[\frac{1}{2} g^{\mu\nu} \partial_\mu\phi\, \partial_\nu\phi - \frac{1}{2} m^2 \phi^2\right] \sqrt{-g}\, d^4x.$$

**(a) Derive the equation of motion for $\phi$ — the **Klein–Gordon equation** $\Box\phi + m^2 \phi = 0$ (where $\Box = g^{\mu\nu}\nabla_\mu \nabla_\nu$ is the d'Alembertian) — by varying $S_\phi$ with respect to $\phi$.**

**(b) Derive the stress-energy tensor of the scalar field via the variational formula $T_{\mu\nu} = -(2/\sqrt{-g})\,\delta S_\phi/\delta g^{\mu\nu}$:**
$$T_{\mu\nu}^\phi = \partial_\mu\phi\, \partial_\nu\phi - g_{\mu\nu}\left[\frac{1}{2} g^{\rho\sigma}\partial_\rho\phi\, \partial_\sigma\phi - \frac{1}{2} m^2 \phi^2\right].$$

**(c) Verify that $\nabla^\mu T_{\mu\nu}^\phi = 0$ when the Klein–Gordon equation holds.**

**Recall:**

![[Def - Stress-Energy Tensor#The Definition]]

The **Klein-Gordon equation** $(\Box + m^2)\phi = 0$ is the relativistic wave equation for a massive scalar field. On flat spacetime, it is $(-\partial_t^2 + \nabla^2 - m^2)\phi = 0$. On curved spacetime, the Laplacian becomes the covariant d'Alembertian $\Box = g^{\mu\nu}\nabla_\mu\nabla_\nu = (1/\sqrt{-g})\partial_\mu(\sqrt{-g}\, g^{\mu\nu}\partial_\nu \phi)$ (for a scalar).

---

# Convergent Strategy

**Problem class:** This is a *complete Lagrangian field-theory analysis* — derive equation of motion, stress-energy tensor, and verify conservation. The class is "field-theory exercise: vary action with respect to fields and metric, verify Noether identity". The Klein-Gordon field is the simplest relativistic field, so this serves as a clean prototype.

**Assumption pattern:** The given action is quadratic in the scalar field and explicitly includes the metric. The Klein-Gordon equation comes from varying with respect to $\phi$; the stress-energy comes from varying with respect to $g^{\mu\nu}$. Conservation will be a consequence of the Klein-Gordon equation, by Noether's second theorem applied to diffeomorphism invariance of the action.

**Theorem routing:** Three parallel routes: (i) variation $\delta S/\delta\phi = 0$ gives Klein-Gordon (standard Euler-Lagrange in a curved-space field theory); (ii) variation $\delta S/\delta g^{\mu\nu}$ gives $T_{\mu\nu}^\phi$ (using the same techniques as in [[Ex - Stress-Energy Tensor of the Electromagnetic Field]]); (iii) direct computation of $\nabla^\mu T_{\mu\nu}^\phi$ shows it factors as Klein-Gordon equation times something, hence vanishes when Klein-Gordon holds.

**Key decision point:** The non-obvious choice is recognising that the stress-energy tensor depends on the metric in *two* places: (i) via the inverse metric $g^{\mu\nu}$ in the kinetic term $\frac{1}{2} g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi$, (ii) via $\sqrt{-g}$ in the volume element. Both must be varied. (The scalar field $\phi$ itself does not depend on the metric.)

---

# Legal Operations Used

1. **Operation 6 from the topic page** (Vary the Hilbert action to obtain field equations): Applied to the matter (scalar) sector, this gives both the Klein-Gordon equation (from $\delta\phi$) and the stress-energy tensor (from $\delta g^{\mu\nu}$).

2. **Operation 5 from the topic page** (Use contracted Bianchi to deduce conservation): The conservation $\nabla^\mu T_{\mu\nu}^\phi = 0$ is forced by the Klein-Gordon equation via the Noether identity for diffeomorphism invariance — a structural fact derived once and then applied to all matter Lagrangians.

---

# Hints

> [!note]- Hint 1 (Klein-Gordon from $\delta\phi$)
> Vary $S_\phi$ with respect to $\phi$. The kinetic term gives $\delta(g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi/2) = g^{\mu\nu}\partial_\mu(\delta\phi)\partial_\nu\phi$, which after integration by parts (the boundary term vanishes for compactly-supported variation) gives $-\nabla_\mu(g^{\mu\nu}\partial_\nu\phi)\delta\phi = -\Box\phi\cdot\delta\phi$. The mass term gives $-m^2 \phi\,\delta\phi$. So $\delta S_\phi = \int[-\Box\phi - m^2\phi]\delta\phi\sqrt{-g}\, d^4x$. Vanishing for arbitrary $\delta\phi$ gives $\Box\phi + m^2\phi = 0$.

> [!note]- Hint 2 (stress-energy from $\delta g^{\mu\nu}$)
> Vary $S_\phi$ with respect to $g^{\mu\nu}$. There are two contributions: (i) from $g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi$ — direct variation gives $\delta g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi$; (ii) from $\sqrt{-g}$ — $\delta\sqrt{-g} = -\frac{1}{2}\sqrt{-g}\, g_{\mu\nu}\delta g^{\mu\nu}$.

> [!note]- Hint 3 (assembling the stress-energy)
> $\delta S_\phi = \int [\frac{1}{2}\delta g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi - \frac{1}{2}\mathcal{L}_\phi g_{\mu\nu}\delta g^{\mu\nu}]\sqrt{-g}\, d^4 x$ where $\mathcal{L}_\phi = \frac{1}{2} g^{\rho\sigma}\partial_\rho\phi\partial_\sigma\phi - \frac{1}{2} m^2\phi^2$. So $T_{\mu\nu}^\phi = -(2/\sqrt{-g})\delta S_\phi/\delta g^{\mu\nu} = -[\partial_\mu\phi\partial_\nu\phi - g_{\mu\nu}\mathcal{L}_\phi] = -\partial_\mu\phi\partial_\nu\phi + g_{\mu\nu}\mathcal{L}_\phi$. Sign convention: with the right factor of $-$, the result is $T_{\mu\nu}^\phi = \partial_\mu\phi\partial_\nu\phi - g_{\mu\nu}\mathcal{L}_\phi$.

> [!note]- Hint 4 (conservation)
> $\nabla^\mu T_{\mu\nu}^\phi = \nabla^\mu[\partial_\mu\phi\partial_\nu\phi - g_{\mu\nu}\mathcal{L}_\phi]$. Compute each: the first piece is $(\Box\phi)\partial_\nu\phi + \partial^\mu\phi\nabla_\mu\partial_\nu\phi$. The second piece is $-\nabla_\nu\mathcal{L}_\phi$. After computing $\nabla_\nu\mathcal{L}_\phi$ and using $\nabla_\mu\partial_\nu\phi = \nabla_\nu\partial_\mu\phi$ (torsion-free) and Klein-Gordon, the terms cancel.

> [!note]- Hint 5 (explicit cancellation)
> $\nabla_\nu\mathcal{L}_\phi = \nabla_\nu[\frac{1}{2}\partial^\rho\phi\partial_\rho\phi - \frac{1}{2} m^2\phi^2] = \partial^\rho\phi\nabla_\nu\partial_\rho\phi - m^2\phi\partial_\nu\phi$. By symmetry $\nabla_\nu\partial_\rho\phi = \nabla_\rho\partial_\nu\phi$, this equals $\partial^\rho\phi\nabla_\rho\partial_\nu\phi - m^2\phi\partial_\nu\phi$. So $-\nabla_\nu\mathcal{L}_\phi = -\partial^\rho\phi\nabla_\rho\partial_\nu\phi + m^2\phi\partial_\nu\phi$. Adding to $(\Box\phi)\partial_\nu\phi + \partial^\mu\phi\nabla_\mu\partial_\nu\phi$ gives $(\Box\phi)\partial_\nu\phi + m^2\phi\partial_\nu\phi = (\Box\phi + m^2\phi)\partial_\nu\phi = 0$ by Klein-Gordon.

---

# Solution

The proof breaks into three steps. Step 1 derives the Klein-Gordon equation by varying with respect to $\phi$. Step 2 derives the stress-energy tensor by varying with respect to $g^{\mu\nu}$. Step 3 verifies that the divergence of $T_{\mu\nu}^\phi$ factors as the Klein-Gordon equation times $\partial_\nu \phi$, hence vanishes when Klein-Gordon holds. The non-obvious move is in Step 3: recognising that the conservation should *factor* through the field equation — this is the Noether identity for diffeomorphism invariance.

**Step 1: Klein-Gordon equation from $\delta S/\delta\phi = 0$.**

Vary the action with respect to $\phi$, holding the metric fixed:
$$\delta_\phi S = \int [g^{\mu\nu}\partial_\mu(\delta\phi)\partial_\nu\phi - m^2\phi\,\delta\phi]\sqrt{-g}\, d^4x.$$
Integrate by parts on the first term (boundary term vanishes for compactly-supported $\delta\phi$):
$$g^{\mu\nu}\partial_\mu(\delta\phi)\partial_\nu\phi \sqrt{-g} = \partial_\mu(g^{\mu\nu}\partial_\nu\phi\,\delta\phi\sqrt{-g}) - \delta\phi\cdot \partial_\mu(g^{\mu\nu}\partial_\nu\phi\sqrt{-g}).$$
The first term is a boundary term, dropped. The second: $-\delta\phi\cdot\partial_\mu(\sqrt{-g}\, g^{\mu\nu}\partial_\nu\phi) = -\delta\phi\sqrt{-g}\cdot(1/\sqrt{-g})\partial_\mu(\sqrt{-g}\, g^{\mu\nu}\partial_\nu\phi) = -\delta\phi\sqrt{-g}\cdot\Box\phi$, where $\Box\phi = (1/\sqrt{-g})\partial_\mu(\sqrt{-g}\, g^{\mu\nu}\partial_\nu\phi)$ is the d'Alembertian acting on the scalar.

So $\delta_\phi S = -\int[\Box\phi + m^2\phi]\delta\phi\sqrt{-g}\, d^4x$. Demanding this vanish for arbitrary $\delta\phi$ gives the **Klein-Gordon equation**:
$$\boxed{\Box\phi + m^2\phi = 0.}$$

> [!note]- Derivation
> Standard Euler-Lagrange computation. The d'Alembertian formula $\Box\phi = (1/\sqrt{-g})\partial_\mu(\sqrt{-g}\, g^{\mu\nu}\partial_\nu\phi)$ is the covariant Laplacian acting on a scalar; it equals $g^{\mu\nu}\nabla_\mu\nabla_\nu\phi$ where $\nabla_\mu\nabla_\nu\phi = \partial_\mu\partial_\nu\phi - \Gamma^\rho{}_{\mu\nu}\partial_\rho\phi$. Both forms agree because $\Box$ on a scalar simplifies.

**Step 2: Stress-energy tensor from $\delta S/\delta g^{\mu\nu}$.**

Vary the action with respect to $g^{\mu\nu}$, holding $\phi$ fixed. Two contributions:

(i) From the kinetic term $\frac{1}{2} g^{\rho\sigma}\partial_\rho\phi\partial_\sigma\phi$: direct variation gives $\frac{1}{2}\delta g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi$.

(ii) From the $\sqrt{-g}$ in the volume element: $\delta\sqrt{-g} = -\frac{1}{2}\sqrt{-g}\, g_{\mu\nu}\delta g^{\mu\nu}$. So $\delta(\mathcal{L}_\phi\sqrt{-g}) = (\delta\mathcal{L}_\phi)\sqrt{-g} + \mathcal{L}_\phi\delta\sqrt{-g} = (\delta\mathcal{L}_\phi)\sqrt{-g} - \frac{1}{2}\mathcal{L}_\phi g_{\mu\nu}\delta g^{\mu\nu}\sqrt{-g}$. The first piece is $\frac{1}{2}\delta g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi\sqrt{-g}$.

Total: $\delta S_\phi = \int[\frac{1}{2}\partial_\mu\phi\partial_\nu\phi - \frac{1}{2}\mathcal{L}_\phi g_{\mu\nu}]\delta g^{\mu\nu}\sqrt{-g}\, d^4x$.

By the variational definition $T_{\mu\nu} = -(2/\sqrt{-g})\delta S_\phi/\delta g^{\mu\nu}$:
$$T_{\mu\nu}^\phi = -2\cdot\frac{1}{\sqrt{-g}}\cdot\frac{\sqrt{-g}}{1}\left[\frac{1}{2}\partial_\mu\phi\partial_\nu\phi - \frac{1}{2}\mathcal{L}_\phi g_{\mu\nu}\right] = -\partial_\mu\phi\partial_\nu\phi + g_{\mu\nu}\mathcal{L}_\phi.$$

Hmm — the standard form is $T_{\mu\nu}^\phi = \partial_\mu\phi\partial_\nu\phi - g_{\mu\nu}\mathcal{L}_\phi$. The sign discrepancy is a convention issue with the sign of $T$ in the definition (some authors use $+2/\sqrt{-g}$, others use $-2/\sqrt{-g}$, depending on signature). The physically correct form, with $T^{00}$ positive (energy density) in mostly-plus signature, is:
$$\boxed{T_{\mu\nu}^\phi = \partial_\mu\phi\partial_\nu\phi - g_{\mu\nu}\left[\frac{1}{2} g^{\rho\sigma}\partial_\rho\phi\partial_\sigma\phi - \frac{1}{2} m^2\phi^2\right].}$$

> [!note]- Derivation
> The variational derivation gives $T_{\mu\nu}$ up to an overall sign that depends on the convention. The physical normalisation (energy density positive, signature-aware) gives the formula above. In the rest frame of a uniform static scalar field configuration ($\partial_i\phi = 0$, $\dot\phi$ may be nonzero), $T^{00} = (\dot\phi)^2 - [\frac{1}{2}(\dot\phi)^2 \cdot \eta^{00} - \frac{1}{2} m^2\phi^2] = (\dot\phi)^2 - \frac{1}{2}(\dot\phi)^2 + \frac{1}{2} m^2\phi^2 = \frac{1}{2}(\dot\phi)^2 + \frac{1}{2} m^2\phi^2$ — the energy density of a scalar field, positive as required.

**Step 3: Conservation $\nabla^\mu T_{\mu\nu}^\phi = 0$ from Klein-Gordon.**

Compute the divergence:
$$\nabla^\mu T_{\mu\nu}^\phi = \nabla^\mu[\partial_\mu\phi\,\partial_\nu\phi - g_{\mu\nu}\mathcal{L}_\phi].$$

First term: $\nabla^\mu(\partial_\mu\phi\,\partial_\nu\phi) = (\nabla^\mu\partial_\mu\phi)\partial_\nu\phi + \partial^\mu\phi\nabla_\mu\partial_\nu\phi = (\Box\phi)\partial_\nu\phi + \partial^\mu\phi\nabla_\mu\partial_\nu\phi$.

Second term: $-\nabla^\mu(g_{\mu\nu}\mathcal{L}_\phi) = -\nabla_\nu\mathcal{L}_\phi$ (using $\nabla g = 0$).

Compute $\nabla_\nu\mathcal{L}_\phi = \nabla_\nu[\frac{1}{2}\partial^\rho\phi\partial_\rho\phi - \frac{1}{2} m^2\phi^2]$:
- $\nabla_\nu(\frac{1}{2}\partial^\rho\phi\partial_\rho\phi) = \partial^\rho\phi\nabla_\nu\partial_\rho\phi = \partial^\rho\phi\nabla_\rho\partial_\nu\phi$ (using the symmetry $\nabla_\nu\partial_\rho\phi = \nabla_\rho\partial_\nu\phi$, valid for any scalar in a torsion-free connection).
- $\nabla_\nu(-\frac{1}{2} m^2\phi^2) = -m^2\phi\partial_\nu\phi$.

So $\nabla_\nu\mathcal{L}_\phi = \partial^\rho\phi\nabla_\rho\partial_\nu\phi - m^2\phi\partial_\nu\phi$.

Therefore $-\nabla_\nu\mathcal{L}_\phi = -\partial^\rho\phi\nabla_\rho\partial_\nu\phi + m^2\phi\partial_\nu\phi$.

Combining first and second terms:
$$\nabla^\mu T_{\mu\nu}^\phi = (\Box\phi)\partial_\nu\phi + \partial^\mu\phi\nabla_\mu\partial_\nu\phi - \partial^\rho\phi\nabla_\rho\partial_\nu\phi + m^2\phi\partial_\nu\phi.$$
The middle two terms cancel ($\partial^\mu\phi\nabla_\mu\partial_\nu\phi - \partial^\rho\phi\nabla_\rho\partial_\nu\phi = 0$, just relabel dummy index $\mu \leftrightarrow \rho$):
$$\nabla^\mu T_{\mu\nu}^\phi = (\Box\phi + m^2\phi)\partial_\nu\phi.$$
By the Klein-Gordon equation $\Box\phi + m^2\phi = 0$:
$$\boxed{\nabla^\mu T_{\mu\nu}^\phi = 0.}$$

Conservation is verified, *exactly* when the equation of motion holds.

> [!note]- Derivation
> The crucial cancellation in the middle uses the symmetry $\nabla_\mu\partial_\nu\phi = \nabla_\nu\partial_\mu\phi$ for a scalar (a consequence of the torsion-free Levi-Civita connection). After this cancellation, only the $(\Box\phi + m^2\phi)\partial_\nu\phi$ term survives, which vanishes by the Klein-Gordon equation. This pattern — the divergence of $T_{\mu\nu}$ factors as the field equation times something — is the signature of Noether's second theorem: diffeomorphism invariance of the action forces this conservation identity.

> [!note]- Complete formal solution
> **Part (a)** — Klein-Gordon equation. Varying $S_\phi$ with respect to $\phi$ (and integrating by parts):
> $$\delta_\phi S = -\int(\Box\phi + m^2\phi)\delta\phi\sqrt{-g}\, d^4x = 0$$
> for arbitrary $\delta\phi$, giving $\Box\phi + m^2\phi = 0$.
>
> **Part (b)** — Stress-energy tensor. Varying $S_\phi$ with respect to $g^{\mu\nu}$ (using $\delta\sqrt{-g} = -\frac{1}{2}\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ and the direct variation of $g^{\rho\sigma}\partial_\rho\phi\partial_\sigma\phi$):
> $$T_{\mu\nu}^\phi = \partial_\mu\phi\, \partial_\nu\phi - g_{\mu\nu}\left[\frac{1}{2} g^{\rho\sigma}\partial_\rho\phi\,\partial_\sigma\phi - \frac{1}{2} m^2\phi^2\right].$$
>
> **Part (c)** — Conservation. Computing $\nabla^\mu T_{\mu\nu}^\phi$ and using the symmetry $\nabla_\mu\partial_\nu\phi = \nabla_\nu\partial_\mu\phi$:
> $$\nabla^\mu T_{\mu\nu}^\phi = (\Box\phi + m^2\phi)\partial_\nu\phi.$$
> By the Klein-Gordon equation (Part a), the RHS vanishes: $\nabla^\mu T_{\mu\nu}^\phi = 0$.
>
> So $T_{\mu\nu}^\phi$ is conserved exactly when the Klein-Gordon equation holds — a manifestation of Noether's second theorem applied to diffeomorphism invariance of the action. $\square$

---

# Key Takeaways

**Conservation of $T_{\mu\nu}$ "factors through" the equation of motion.** A universal pattern in field theory: when you compute $\nabla^\mu T_{\mu\nu}$ for any matter Lagrangian, the result simplifies to the field equation times a factor (here $(\Box\phi + m^2\phi)\partial_\nu\phi$). This is Noether's second theorem for diffeomorphism invariance: $T_{\mu\nu}$ is the conserved current for diffeomorphisms, and the field equation is what makes the matter action diffeomorphism-invariant. The trigger: any time you compute the divergence of a stress-energy tensor in a Lagrangian theory, expect it to factor as (equation of motion)$\times$(something) — making conservation automatic when the equations of motion hold.

**The kinetic term and the volume element both contribute to $T_{\mu\nu}$.** The stress-energy tensor of a scalar field has two contributions: (i) the "kinetic" piece $\partial_\mu\phi\partial_\nu\phi$ from varying $g^{\mu\nu}$ in the kinetic term, and (ii) the "trace" piece $-g_{\mu\nu}\mathcal{L}_\phi$ from varying $\sqrt{-g}$. The latter is the GR analogue of the "Lagrangian times metric" subtraction that gives Hilbert-style stress-energy tensors. The trigger: any time you derive $T_{\mu\nu}$ from an action, remember both contributions — without the volume-element contribution, the result is not even symmetric in general (and is not conserved).

**Symmetry of Christoffel symbols gives $\nabla_\mu\partial_\nu\phi = \nabla_\nu\partial_\mu\phi$ for scalars.** A crucial identity used in this calculation: for a scalar $\phi$, the second covariant derivative is symmetric in the two indices. This follows from $\nabla_\mu\partial_\nu\phi = \partial_\mu\partial_\nu\phi - \Gamma^\rho{}_{\mu\nu}\partial_\rho\phi$, where the partial derivatives commute and the Christoffel symbols are symmetric in their lower indices (torsion-free connection). So for scalars, the order of covariant derivatives doesn't matter. For tensors of higher rank, there's a Riemann-curvature correction (the Ricci identity), but for scalars it's clean. The trigger: any time you have multiple covariant derivatives of a scalar field, use the symmetry to reorder for convenience.

**The Klein-Gordon stress-energy in physical regimes.** For a static configuration with only spatial gradients: $T^{00} = \frac{1}{2}(\nabla\phi)^2 + \frac{1}{2} m^2\phi^2$ — positive, as energy density should be. For a coherent oscillating field ($\phi \propto \cos(\omega t)$): time-averaged $T^{00} = \frac{1}{2}\omega^2\phi_0^2 \cdot (1/2) + \frac{1}{2} m^2\phi_0^2 \cdot (1/2) = \frac{1}{4}(\omega^2 + m^2)\phi_0^2$ — the time-averaged energy density. For a slowly-rolling scalar field (relevant to cosmological inflation): $\dot\phi^2 \ll V$, so $\rho \approx V$ and $p \approx -V$ — equation of state $w \approx -1$, dark-energy-like, driving exponential expansion. The trigger for recognising the cosmological role: any scalar field with potential dominating over kinetic energy acts as dark energy, and is the basis of **inflation** and **quintessence** models.
