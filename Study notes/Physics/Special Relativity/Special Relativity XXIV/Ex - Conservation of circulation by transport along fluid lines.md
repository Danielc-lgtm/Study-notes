---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Kelvin's Circulation Theorem (exterior-calculus formulation)"
  - "Def - Vorticity 2-Form"
  - "Thm - Stokes Theorem on Spacetime"
  - "Thm - Energy-Momentum Conservation projected (Euler + energy equation)"
tags: [physics, special-relativity]
---

# Problem Statement

1. Define the fluid circulation $C(\mathcal{C}) = \oint_\mathcal{C}\pi$ and use Stokes' theorem to write it as the flux $\int_\mathcal{S}\Omega$ of the vorticity two-form.
2. Carry a closed loop $\mathcal{C}$ along the fluid lines to a loop $\mathcal{C}'$, sweeping out a fluid tube $\mathcal{T}$. By applying Stokes' theorem to the tube and using the canonical equation $\Omega(u,\cdot) = T\,dS$, prove $C(\mathcal{C}') = C(\mathcal{C}) - \int_\mathcal{T} T\,\nabla_{e_3}S$.
3. Conclude that circulation is conserved for a barotropic ($T=0$) or isentropic ($\nabla S = 0$ on $\mathcal{C}$) flow, and explain how, in the baroclinic case, the same formula gives the *generation* of vorticity by crossed pressure and entropy gradients.

**Recall:**

![[Thm - Kelvin's Circulation Theorem (exterior-calculus formulation)#Statement]]

The fluid momentum one-form is $\pi = hu$, the vorticity two-form $\Omega = d\pi$, obeying $\Omega(u,\cdot) = T\,dS$ (see [[Def - Vorticity 2-Form]]). [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] gives $\oint_{\partial\mathcal{S}}\pi = \int_\mathcal{S} d\pi$. The entropy per baryon is conserved along fluid lines, $\nabla_u S = 0$ (see [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]).

---

# Convergent Strategy

**Problem class.** An *establish-a-conservation-law-along-the-flow* problem, the hardest in the chapter because it combines a transport argument with two applications of Stokes' theorem. Per the [[Special Relativity XXIV — Relativistic Hydrodynamics#Problem-Solving Strategy|topic strategy]], the exterior-calculus formulation is essential: circulation is the flux of a closed two-form, and its conservation is a statement about that flux.

**Assumption pattern.** The structural assumption is that the loop is *transported by the flow* (its points move along fluid lines), so the swept tube has the four-velocity tangent to its walls. The thermodynamic assumption for conservation is $T\,dS = 0$ — barotropic or isentropic. The signpost is "circulation around a material loop", "Kelvin", or "vortex persistence".

**Theorem routing.** Part 1 is [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] applied to $\Omega = d\pi$. Part 2 builds a closed curve $\mathcal{K}$ from the two loops and two fluid-line segments, applies Stokes to the tube wall, and reduces $\Omega(u,\cdot)$ by the [[Def - Vorticity 2-Form|canonical equation]]. Part 3 imposes $T\,dS = 0$ and uses entropy conservation to propagate $S$ from $\mathcal{C}$ to $\mathcal{T}$.

**Key decision point.** The crux is the construction of the auxiliary closed curve $\mathcal{K}$ — stitching $\mathcal{C}$, a fluid-line segment up to $\mathcal{C}'$, $\mathcal{C}'$ reversed, and a fluid-line segment back — whose bounded surface is the *side wall* of the tube. Only on this side wall, where the four-velocity is tangent, does the canonical equation $\Omega(u,\cdot) = T\,dS$ reduce the integrand. The natural error is to try to compare $\mathcal{C}$ and $\mathcal{C}'$ directly without the tube-wall surface, which obscures where the thermodynamic source enters.

---

# Legal Operations Used

1. **Convert a circulation into a flux by Stokes' theorem** (operation 8 from the topic page): both $C(\mathcal{C}) = \int_\mathcal{S}\Omega$ and the comparison of $\mathcal{C}$ with $\mathcal{C}'$ via the tube wall use Stokes.

2. **Form the fluid momentum one-form and take its exterior derivative** (operation 5): $\Omega = d\pi$ is closed, and $\Omega(u,\cdot) = T\,dS$ is the canonical equation that reduces the wall flux.

3. **Invoke baryon-number and entropy conservation together** (operation 6): $\nabla_u S = 0$ propagates constancy of $S$ from the initial loop to the whole tube.

---

# Hints

> [!note]- Hint 1
> $\pi$ is a one-form, $\mathcal{C}$ a closed curve, $\mathcal{S}$ a surface with $\partial\mathcal{S} = \mathcal{C}$. Stokes: $\oint_\mathcal{C}\pi = \int_\mathcal{S} d\pi = \int_\mathcal{S}\Omega$. (Independent of $\mathcal{S}$ because $d\Omega = d^2\pi = 0$.)

> [!note]- Hint 2
> Build $\mathcal{K} = \mathcal{L}_{A\to A'}\cup\mathcal{C}'_{A'\to B'}\cup\mathcal{L}_{B'\to B}\cup\mathcal{C}_{B\to A}$ from two fluid-line segments $\mathcal{L}$ and (most of) the two loops. $\mathcal{K}$ bounds the tube wall $\mathcal{S}$. Apply Stokes: $\oint_\mathcal{K}\pi = \int_\mathcal{S}\Omega$.

> [!note]- Hint 3
> On the tube wall the four-velocity $u$ is tangent (the wall is made of fluid lines). In coordinates with $e_2 = u$, $\int_\mathcal{S}\Omega = \int\Omega(u, e_3)\,dx^2 dx^3$, and the canonical equation gives $\Omega(u, e_3) = T\langle dS, e_3\rangle = T\nabla_{e_3}S$.

> [!note]- Hint 4
> As $A \to B$, the two fluid-line segments cancel, $\mathcal{C}_{B\to A}\to C(\mathcal{C})$, $\mathcal{C}'_{A'\to B'}\to -C(\mathcal{C}')$, $\mathcal{S}\to\mathcal{T}$. So $C(\mathcal{C}) - C(\mathcal{C}') = \int_\mathcal{T} T\nabla_{e_3}S$. Set $T = 0$ or $\nabla S = 0$ to conserve.

---

# Solution

Circulation is the flux of the closed vorticity two-form; comparing the circulations of a loop and its transported image reduces, via Stokes on the swept tube and the canonical equation, to a baroclinic integral that vanishes for barotropic or isentropic flow.

**Step 1: Circulation is a flux.**

> [!note]- Derivation
> The fluid circulation around a closed oriented curve $\mathcal{C}$ is $C(\mathcal{C}) = \oint_\mathcal{C}\pi$. Since $\pi$ is a one-form and $\Omega = d\pi$, [[Thm - Stokes Theorem on Spacetime|Stokes' theorem]] gives, for any surface $\mathcal{S}$ with $\partial\mathcal{S} = \mathcal{C}$,
> $$C(\mathcal{C}) = \oint_\mathcal{C}\pi = \int_\mathcal{S} d\pi = \int_\mathcal{S}\Omega.$$
> This is well-defined independently of $\mathcal{S}$ because $\Omega$ is closed, $d\Omega = d^2\pi = 0$ (the fluid Bianchi identity): two surfaces with the same boundary differ by a closed surface, over which the closed form $\Omega$ integrates to zero.

**Step 2: The master formula via the tube wall.**

> [!note]- Derivation
> Transport $\mathcal{C}$ along the fluid lines to $\mathcal{C}'$, sweeping the fluid tube $\mathcal{T}$. Pick neighbouring points $A, B$ on $\mathcal{C}$ with images $A', B'$ on $\mathcal{C}'$, and form the closed curve
> $$\mathcal{K} = \mathcal{L}_{A\to A'}\cup\mathcal{C}'_{A'\to B'}\cup\mathcal{L}_{B'\to B}\cup\mathcal{C}_{B\to A},$$
> where $\mathcal{L}_{A\to A'}$, $\mathcal{L}_{B'\to B}$ are fluid-line segments and the two loop pieces cover most of $\mathcal{C}'$ and $\mathcal{C}$. Let $\mathcal{S}$ be the piece of tube wall bounded by $\mathcal{K}$. By Stokes, $\oint_\mathcal{K}\pi = \int_\mathcal{S}\Omega$.
>
> Evaluate $\int_\mathcal{S}\Omega$ using coordinates adapted to the wall: since $\mathcal{S}$ is generated by fluid lines, the four-velocity $u$ is tangent, so choose the basis vector $e_2 = u$ (then $x^2$ is proper time along the lines and $x^3$ runs across). Then
> $$\int_\mathcal{S}\Omega = \int_\mathcal{S}\Omega(e_2, e_3)\,dx^2 dx^3 = \int_\mathcal{S}\Omega(u, e_3)\,dx^2 dx^3 = \int_\mathcal{S} T\langle dS, e_3\rangle\,dx^2 dx^3 = \int_\mathcal{S} T\nabla_{e_3}S\,dx^2 dx^3,$$
> using the [[Def - Vorticity 2-Form|canonical equation]] $\Omega(u,\cdot) = T\,dS$.
>
> Now decompose $\oint_\mathcal{K}\pi$ into its four pieces. As $A\to B$: the fluid-line segments $\mathcal{L}_{A\to A'}$ and $\mathcal{L}_{B'\to B}$ contribute equal and opposite amounts and cancel; $\int_{\mathcal{C}_{B\to A}}\pi\to C(\mathcal{C})$; $\int_{\mathcal{C}'_{A'\to B'}}\pi\to -C(\mathcal{C}')$ (opposite orientation); and $\mathcal{S}$ fills the whole tube $\mathcal{T}$. Hence
> $$C(\mathcal{C}) - C(\mathcal{C}') = \int_\mathcal{T} T\,\nabla_{e_3}S\;dx^2 dx^3, \qquad\text{i.e.}\qquad C(\mathcal{C}') = C(\mathcal{C}) - \int_\mathcal{T} T\,\nabla_{e_3}S\;dx^2 dx^3.$$

**Step 3: Conservation, and the baroclinic source.**

> [!note]- Derivation
> *Conservation.* If the fluid is **barotropic**, $T = 0$, so the integral vanishes and $C(\mathcal{C}') = C(\mathcal{C})$ — circulation is conserved. If $S$ is **constant on $\mathcal{C}$**, then since the entropy per baryon is conserved along each fluid line ($\nabla_u S = 0$, from [[Thm - Energy-Momentum Conservation projected (Euler + energy equation)]]), $S$ keeps that value along every line of the tube, so $S$ is constant on all of $\mathcal{T}$, $\nabla_{e_3}S = 0$, and again $C(\mathcal{C}') = C(\mathcal{C})$. In either case **circulation is conserved by transport along the flow** — the relativistic Kelvin theorem.
>
> *Baroclinic generation.* When $T\,dS \ne 0$ on the tube — when pressure and entropy (or density) surfaces *cross*, a baroclinic flow — the integral $\int_\mathcal{T} T\nabla_{e_3}S$ does not vanish, and circulation *changes*: vorticity is generated. The same formula, read backwards, is the *source* law for vorticity. Nonrelativistically this is the familiar baroclinic term $\nabla p\times\nabla\rho$ in the vorticity equation, the mechanism behind the sea breeze (horizontal temperature gradient under a vertical pressure gradient) and baroclinic instability in the atmosphere.

> [!note]- Complete formal solution
> Circulation $C(\mathcal{C}) = \oint_\mathcal{C}\pi = \int_\mathcal{S}\Omega$ by Stokes ($\Omega = d\pi$, closed). To compare with the transported loop $\mathcal{C}'$, form the closed curve $\mathcal{K}$ from $\mathcal{C}$, $\mathcal{C}'$ (reversed), and two fluid-line segments; its bounded surface is the tube wall $\mathcal{S}$, on which $u$ is tangent. Stokes gives $\oint_\mathcal{K}\pi = \int_\mathcal{S}\Omega$, and in adapted coordinates ($e_2 = u$) the canonical equation reduces this to $\int_\mathcal{S} T\nabla_{e_3}S\,dx^2 dx^3$. Taking $A\to B$, the fluid-line segments cancel and the loops give $C(\mathcal{C}) - C(\mathcal{C}')$, so $C(\mathcal{C}') = C(\mathcal{C}) - \int_\mathcal{T} T\nabla_{e_3}S$. Circulation is conserved for barotropic ($T=0$) or isentropic ($\nabla S = 0$ on $\mathcal{C}$, hence on $\mathcal{T}$ by $\nabla_u S = 0$) flow; otherwise the baroclinic integral generates vorticity. $\blacksquare$

---

# Key Takeaways

**Circulation is the flux of a closed two-form, and that is why it is conserved.** The deepest lesson is that the conservation of circulation is, at bottom, a statement about a closed two-form: $C(\mathcal{C}) = \int_\mathcal{S}\Omega$ with $d\Omega = 0$, so the flux depends only on the boundary loop, and sliding the loop along the flow changes the flux only by what crosses the side wall of the swept tube. The whole proof is the evaluation of that side-wall flux. This reframing — from "circulation is a line integral to be differentiated" (the classical view) to "circulation is the flux of a closed form" (the exterior-calculus view) — is what makes the relativistic proof clean. The transferable insight is that any quantity expressible as the flux of a closed two-form through a transported surface is a candidate conserved quantity, and its conservation hinges on what the closed form does on the swept side walls. This is exactly the structure shared with magnetic flux in a perfect conductor.

**The conservation is conditional: $T\,dS = 0$, or vorticity is generated.** The single most important caveat is that circulation is *not* universally conserved — the obstruction is the baroclinic integral $\int_\mathcal{T} T\nabla_{e_3}S$, which vanishes only for barotropic ($T = 0$) or isentropic ($\nabla S = 0$) flow. When pressure and entropy gradients cross, vorticity is *created*, and the same formula is the generation law. The diagnostic to carry: before invoking Kelvin's theorem, check whether the flow is barotropic or isentropic; in a stratified medium with crossed gradients (a star with composition layers, an atmosphere with horizontal temperature variation), circulation grows and vortices are spun up. The role of entropy conservation $\nabla_u S = 0$ is subtle but essential — it is what lets constancy of $S$ on the *initial* loop propagate to the *whole* tube, so that "isentropic initial data" suffices for conservation throughout the flow's history.

**Kelvin and Alfvén are one theorem about closed two-forms.** The structural payoff is the exact parallel with magnetohydrodynamics. The vorticity two-form $\Omega = d\pi$ and the electromagnetic field two-form $F = dA$ play identical roles: both are exact (hence closed) two-forms, and both have a flux through a transported loop that is conserved by the same argument — Kelvin's circulation theorem for the fluid, Alfvén's frozen-in theorem for a perfectly conducting plasma (field lines frozen into the matter). Recognising this identity is high-leverage: it means the persistence of vortices in an ideal fluid and the freezing of magnetic flux into a plasma are the same mathematics, and the baroclinic vorticity source has its analogue in the battery term that generates magnetic field. The trigger to deploy this parallel: any "flux conserved by transport" statement — vorticity, magnetic flux, or any closed two-form — is governed by whether the form's contraction with the flow velocity vanishes, which is the canonical equation in the fluid case and the ideal-MHD condition in the plasma case.
