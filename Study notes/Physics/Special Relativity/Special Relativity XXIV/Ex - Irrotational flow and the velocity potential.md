---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Vorticity 2-Form"
  - "Def - The Exterior Derivative"
  - "Def - Baryon Four-Current and Its Conservation"
  - "Def - Equation of State and Speed of Sound"
tags: [physics, special-relativity]
---

# Problem Statement

A perfect fluid is in **irrotational flow** if its vorticity two-form vanishes, $\Omega = 0$.

1. Show that $\Omega = 0$ is equivalent to $d\pi = 0$ (the fluid momentum one-form is closed), hence by the Poincaré lemma $\pi = hu = d\Psi$ for a scalar **velocity potential** $\Psi$.
2. Emphasise the relativistic subtlety: it is $hu$ (the enthalpy-weighted velocity), not $u$, that is a gradient — contrast with the nonrelativistic condition $\mathbf{V} = \nabla\Psi$.
3. Substituting $u = h^{-1}d\Psi$ into baryon conservation $\nabla_\mu(nu^\mu) = 0$, derive the potential equation $\square\Psi + \nabla\ln(n/h)\cdot\nabla\Psi = 0$, and show it reduces to a wave equation $\square\Psi = 0$ when $h \propto n$ (the stiff equation of state $p = \rho$).

**Recall:**

The vorticity two-form is $\Omega = d\pi$ with $\pi = hu$, $h = (\rho+p)/n$ the enthalpy per baryon (see [[Def - Vorticity 2-Form]]). The [[Special Relativity XIX/Def - The Exterior Derivative|exterior derivative]] satisfies $d^2 = 0$, and the **Poincaré lemma** states that a closed form ($d\omega = 0$) is locally exact ($\omega = d\Psi$). Baryon conservation is $\nabla_\mu(nu^\mu) = 0$ (see [[Def - Baryon Four-Current and Its Conservation]]). The four-velocity normalisation $u\cdot u = 1$ becomes, via $u = h^{-1}d\Psi$, a relation $h = (\nabla\Psi\cdot\nabla\Psi)^{1/2}$. The d'Alembertian is $\square = \eta^{\mu\nu}\partial_\mu\partial_\nu$.

---

# Convergent Strategy

**Problem class.** An *exploit-vanishing-vorticity* problem: when $\Omega = 0$, the closed momentum one-form becomes a gradient, introducing a potential. Per the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]], the exterior-calculus formulation makes this immediate via the Poincaré lemma.

**Assumption pattern.** The assumption is irrotationality, $\Omega = 0$. This forces $d\pi = 0$, and (Poincaré) $\pi = d\Psi$. The signpost is "irrotational" or "potential flow" or "vorticity-free".

**Theorem routing.** Part 1 uses $\Omega = d\pi$ and the Poincaré lemma (closed $\Rightarrow$ locally exact). Part 3 substitutes $u = h^{-1}d\Psi$ into [[Def - Baryon Four-Current and Its Conservation|baryon conservation]] $\nabla_\mu(nu^\mu) = 0$ and expands.

**Key decision point.** The decisive subtlety is that the relativistic irrotational condition gives $\pi = hu = d\Psi$, *not* $u = d\Psi$. The enthalpy factor sits between the velocity and the potential. The natural error — translating the nonrelativistic $\mathbf{V} = \nabla\Psi$ directly to $u = d\Psi$ — is wrong, and the correct statement requires recognising that the vorticity is built from $hu$, not $u$.

---

# Legal Operations Used

1. **Form the fluid momentum one-form and take its exterior derivative** (operation 5 from the topic page): $\Omega = d\pi = d(hu)$, and $\Omega = 0$ means $\pi$ is closed.

2. **Apply the Poincaré lemma to a closed one-form** (operation 9): $d\pi = 0 \Rightarrow \pi = d\Psi$ locally.

3. **Invoke baryon-number conservation** (operation 6): $\nabla_\mu(nu^\mu) = 0$ becomes the equation for the potential $\Psi$.

---

# Hints

> [!note]- Hint 1
> $\Omega = d\pi$, so $\Omega = 0 \iff d\pi = 0$, i.e. $\pi$ is closed. By the Poincaré lemma, a closed one-form is locally exact: $\pi = d\Psi$. Since $\pi = hu$, this is $hu = d\Psi$.

> [!note]- Hint 2
> Nonrelativistically, $h \to m_{\mathrm b}c^2$ is constant, so $hu = d\Psi$ becomes $u \propto d\Psi$, i.e. $\mathbf{V} = \nabla(\Psi/m_{\mathrm b}c^2)$ — the classical potential. Relativistically $h$ varies, so it is $hu$, not $u$, that is the gradient.

> [!note]- Hint 3
> $u^\mu = h^{-1}\partial^\mu\Psi$. Then $nu^\mu = (n/h)\partial^\mu\Psi$, and $\nabla_\mu(nu^\mu) = \partial_\mu[(n/h)\partial^\mu\Psi] = (n/h)\square\Psi + \partial_\mu(n/h)\partial^\mu\Psi = 0$. Divide by $n/h$: $\square\Psi + \partial_\mu\ln(n/h)\partial^\mu\Psi = 0$.

> [!note]- Hint 4
> If $h = \alpha n$ (constant $\alpha$), then $n/h = 1/\alpha$ is constant, $\nabla\ln(n/h) = 0$, and the potential equation is $\square\Psi = 0$ — a wave equation. This corresponds to $p = \rho$ (the stiff equation of state, $c_s = c$).

---

# Solution

Vanishing vorticity makes the fluid momentum one-form closed, hence a gradient $hu = d\Psi$; the enthalpy weighting distinguishes the relativistic potential from the classical one, and baryon conservation turns into a quasilinear equation for $\Psi$ that becomes a wave equation for the stiffest matter.

**Step 1: Irrotational flow has a velocity potential.**

> [!note]- Derivation
> Irrotational means $\Omega = 0$. Since $\Omega = d\pi$ (see [[Def - Vorticity 2-Form]]),
> $$\Omega = 0 \iff d\pi = 0,$$
> i.e. the fluid momentum one-form $\pi$ is **closed**. By the **Poincaré lemma**, a closed one-form is locally exact: there exists a scalar field $\Psi$ (the velocity potential) with
> $$\pi = d\Psi, \qquad\text{i.e.}\qquad h\,u = d\Psi.$$
> (Globally, $\Psi$ exists if the flow domain is simply connected; otherwise it may be multivalued, which is exactly how circulation around an obstacle enters.)

**Step 2: It is $hu$, not $u$, that is a gradient.**

> [!note]- Derivation
> The result is $hu = d\Psi$, the *enthalpy-weighted* four-velocity is the gradient of the potential. This contrasts sharply with the nonrelativistic condition: classically, irrotational flow means $\nabla\times\mathbf{V} = 0$, hence $\mathbf{V} = \nabla\Psi$ — the velocity itself is a gradient. The naive relativistic translation $u = d\Psi$ is **wrong**. The reason is that the vorticity two-form is built from $hu$ (because the dynamics, via the enthalpy factor in $\pi = hu$, demands it), not from $u$. In the nonrelativistic limit $h \to m_{\mathrm b}c^2$ is constant and can be divided out, recovering $u \propto d\Psi$ and the classical statement. So the enthalpy weighting, invisible classically, is the whole relativistic content of irrotational flow: a flow with varying enthalpy can have $hu$ exact while $u$ is not.

**Step 3: The potential equation.**

> [!note]- Derivation
> From $hu = d\Psi$, the four-velocity is $u^\mu = h^{-1}\partial^\mu\Psi$. Substitute into [[Def - Baryon Four-Current and Its Conservation|baryon conservation]] $\nabla_\mu(nu^\mu) = 0$:
> $$\nabla_\mu\Big(\frac{n}{h}\partial^\mu\Psi\Big) = \frac{n}{h}\square\Psi + \partial_\mu\Big(\frac{n}{h}\Big)\partial^\mu\Psi = 0.$$
> Divide by $n/h$:
> $$\boxed{\square\Psi + \nabla\ln\Big(\frac{n}{h}\Big)\cdot\nabla\Psi = 0,}$$
> a single (generally nonlinear) equation for $\Psi$ — nonlinear because $h$ and $n$ depend on $\Psi$ through $h = (\nabla\Psi\cdot\nabla\Psi)^{1/2}$ (from $u\cdot u = 1$) and the equation of state.
>
> *Stiff case.* If $h = \alpha n$ for a constant $\alpha$ (the equation of state with $\rho = \tfrac\alpha2 n^2 = p$, i.e. $p = \rho$, $c_s = c$; see [[Def - Equation of State and Speed of Sound]]), then $n/h = 1/\alpha$ is constant, $\nabla\ln(n/h) = 0$, and the potential equation collapses to the **wave equation**
> $$\square\Psi = 0.$$
> The hardest causal fluid has a linear potential equation — irrotational flow of stiff matter is governed by the ordinary d'Alembertian, as for a massless scalar field.

> [!note]- Complete formal solution
> Irrotational flow has $\Omega = d\pi = 0$, so $\pi = hu$ is closed and (Poincaré) locally exact: $hu = d\Psi$. The relativistic potential weights the velocity by the enthalpy per baryon — it is $hu$, not $u$, that is a gradient, in contrast to the classical $\mathbf{V} = \nabla\Psi$; the difference washes out as $h \to m_{\mathrm b}c^2$ nonrelativistically. Substituting $u^\mu = h^{-1}\partial^\mu\Psi$ into $\nabla_\mu(nu^\mu) = 0$ gives $\square\Psi + \nabla\ln(n/h)\cdot\nabla\Psi = 0$, quasilinear in general (since $h = (\nabla\Psi\cdot\nabla\Psi)^{1/2}$), reducing to the wave equation $\square\Psi = 0$ when $h \propto n$, i.e. for the stiff equation of state $p = \rho$. $\blacksquare$

---

# Key Takeaways

**Vanishing vorticity gives a potential, by the Poincaré lemma.** The cleanest lesson is the chain $\Omega = 0 \Rightarrow d\pi = 0 \Rightarrow \pi = d\Psi$: a vorticity-free flow has a closed momentum one-form, and a closed form is locally a gradient. This is the exterior-calculus version of "curl-free implies gradient", and it is exactly the same logic that, in [[Special Relativity XXII — Maxwell's Equations|electromagnetism]], lets a curl-free field be written as a gradient or a closed field-strength as $dA$. The transferable insight is that whenever a problem says "irrotational", the immediate move is to introduce a potential via the Poincaré lemma, converting a vector (or one-form) unknown into a single scalar unknown $\Psi$. The catch — and the source of the deepest insight here — is *which* one-form is closed: the enthalpy-weighted momentum $hu$, not the bare velocity $u$.

**The enthalpy weighting is the entire relativistic content of irrotational flow.** The single most important point is that the relativistic irrotational condition is $hu = d\Psi$, not $u = d\Psi$. The vorticity two-form is built from the momentum-per-baryon $\pi = hu$, so its vanishing makes $hu$ exact, and only because the enthalpy is constant nonrelativistically ($h \to m_{\mathrm b}c^2$) does the classical $\mathbf{V} = \nabla\Psi$ emerge. The diagnostic to carry forward: never translate a nonrelativistic fluid statement by replacing $\mathbf{V}$ with $u$ — check whether the enthalpy factor belongs. A flow with non-uniform enthalpy (a temperature or composition gradient along the flow) can have $hu$ a gradient while $u$ is not, which is a genuinely relativistic possibility with no classical analogue. This is the same enthalpy weighting that makes the inertia $\rho + p$ rather than $\rho_{\mathrm m}$ — the enthalpy is the recurring relativistic correction in fluid dynamics.

**Irrotational flow reduces a vector problem to a scalar potential equation.** The practical payoff is that irrotationality plus baryon conservation collapses the full fluid system to a single equation for $\Psi$, $\square\Psi + \nabla\ln(n/h)\cdot\nabla\Psi = 0$. This is the relativistic analogue of the Laplace/potential-flow theory that makes classical aerodynamics tractable: instead of solving the coupled Euler and continuity equations for a velocity field, one solves one (quasilinear) equation for a scalar. The trigger to exploit this: an irrotational, isentropic (or barotropic) flow — there the canonical equation is automatically satisfied, and the *only* remaining equation is baryon conservation written for $\Psi$. The beautiful special case is the stiff fluid $p = \rho$, where $h \propto n$ and the equation becomes the linear wave equation $\square\Psi = 0$ — the densest causal matter flows like a free massless field, a fact that makes its irrotational dynamics exactly solvable.
