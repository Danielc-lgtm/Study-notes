---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Regular Symmetric Dirichlet Form"
  - "Constr - The Brownian Loop Measure"
  - "Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure"
tags: [paper, probability, dirichlet-forms, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $X$ | a Riemannian surface (state space from §2.2.1 on); $\operatorname{vol}_g$ its volume measure |
| $(\mathcal{E},\mathcal{F})$ | a [[Def - Regular Symmetric Dirichlet Form\|regular symmetric Dirichlet form]] on $L^2(X,\operatorname{vol}_g)$; generator $A$ |
| $p^{\mathcal{E}}$ | $(0,\infty)\times X\times X\to[0,\infty)$; jointly measurable, symmetric; density w.r.t. $\operatorname{vol}_g$ |
| $D([0,t];X)$ | càdlàg path space; $\supseteq C([0,t];X)$ |
| $W^{t,\mathcal{E}}_{x\to y}$ | measure on $D([0,t];X)$; $\lvert W^{t,\mathcal{E}}_{x\to y}\rvert=p^{\mathcal{E}}(t,x,y)$ |
| $\mathcal{C}^*_X,\ \mathcal{C}_X$ | càdlàg rooted / unrooted loop spaces from here on; $q$ the quotient map |
| $\mu^{*,\mathcal{E}}_X$ | measure on $\mathcal{C}^*_X$; $\sigma$-finite |
| $\mu^{\mathcal{E}}_X$ | $:=q_*\mu^{*,\mathcal{E}}_X$; $\sigma$-finite measure on $\mathcal{C}_X$ |
| $\mathcal{E}_{X'}$ | the part form on open $X'\subseteq X$ |

---

# Construction

> **Definition 2.2 (Dirichlet form loop measure).** For $(\mathcal{E},\mathcal{F})$ regular symmetric on $L^2(X,\operatorname{vol}_g)$ with transition density $p^{\mathcal{E}}$, the **parametrised loop measure** on $\mathcal{C}^*_X$ is
> $$\mu^{*,\mathcal{E}}_X := \int_0^\infty\frac{\mathrm{d}t}{t}\int_X W^{t,\mathcal{E}}_{x\to x}\,\mathrm{d}\operatorname{vol}_g(x),$$
> and the **loop measure** is $\mu^{\mathcal{E}}_X:=q_*\mu^{*,\mathcal{E}}_X$.

**Difference from (2.1):** exactly two substitutions — $C([0,t];X)\rightsquigarrow D([0,t];X)$ and $p_X\rightsquigarrow p^{\mathcal{E}}$. Nothing else changes.

**Well-definedness.** Existence of $W^{t,\mathcal{E}}_{x\to x}$ is [[Def - Unnormalised Bridge Measure by Disintegration|(D1),(D2)]] given $p^{\mathcal{E}}$; the pushforward is [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure|(LJ)]]. That $\sim$ still makes sense on càdlàg paths is [[Def - The Space of Unrooted Unparametrised Loops|(F1)]]: circular shifts and increasing continuous reparametrisations preserve the càdlàg property.

> **(M) Total mass.** $\ \displaystyle\lvert\mu^{*,\mathcal{E}}_X\rvert=\int_0^\infty\frac1t\int_X p^{\mathcal{E}}(t,x,x)\,\mathrm{d}\operatorname{vol}_g(x)\,\mathrm{d}t$, generally $=\infty$.

---

# Type card

> [!abstract] Type card — Definition 2.2
> **Given.**
> **(H1)** $(\mathcal{E},\mathcal{F})$ regular symmetric Dirichlet form on $L^2(X,\operatorname{vol}_g)$.
> **(H2)** $e^{-tA}$ admits a jointly measurable symmetric density $p^{\mathcal{E}}$ against $\operatorname{vol}_g$.
> **(H3)** [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure|(LJ)]].
>
> **Produces.** $\mu^{\mathcal{E}}_X$: a $\sigma$-finite measure on the càdlàg loop space $\mathcal{C}_X$, of rooted total mass (M).
>
> **Lets you.** Run the loop-measure construction for jump processes as well as diffusions, so that every theorem of §3 and §7 is proved once for the whole subordinate family. **Retains (P1); loses (P2).**

---

# Depends on

- [[Def - Regular Symmetric Dirichlet Form]] — (H1),(H2)
- [[Def - The Space of Unrooted Unparametrised Loops]] — (F1) for the càdlàg quotient
- [[Def - Unnormalised Bridge Measure by Disintegration]] — the bridges
- [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure]] — (H3)
- [[Constr - The Brownian Loop Measure]] — the case $\mathcal{E}(u,u)=\int_X\lvert\nabla u\rvert^2$

---

# Properties

**(P1) Restriction — retained.** $X'\subseteq X$ open $\implies\mathrm{d}\mu^{\mathcal{E}}_{X'}(\eta)=\mathbf{1}_{\{\eta\subseteq X'\}}\,\mathrm{d}\mu^{\mathcal{E}}_X(\eta)$.
*Why:* [[Def - Regular Symmetric Dirichlet Form|(F3)]] — the part form $\mathcal{E}_{X'}$ **is** the form of the process killed on leaving $X'$, so its bridges are the ambient ones restricted to paths staying inside.
*Consumed by:* [[Ext - Wang–Xue Length-Spectrum Identity]] (killing case).

**(P2) Conformal invariance — LOST for nonlinear $\phi$.**
$$\phi\big(e^{-2\sigma}\Delta_{X,g}\big)\neq e^{-2\sigma}\phi\big(\Delta_{X,g}\big)\quad\text{unless }\phi(\lambda)=c\lambda .$$
*Consequence:* from §2.3 on, $X$ is a **Riemannian** surface, not a Riemann surface.

**(P3) Homotopy classes need not be measurable.** If the process has jumps, $\mathcal{C}_X(\gamma^m)$ is **not** a measurable subset of $\mathcal{C}_X$ — by [[Def - The Space of Unrooted Unparametrised Loops|(F4)]], a càdlàg loop admits no lift. Repair: [[Constr - Loop Mass in a Homotopy Class for Jump Processes]].

---

# Consumed by

- [[Constr - The Subordinate Brownian Loop Measure]] — Definition 2.8 is this applied to $(\mathcal{E}^\phi,\mathcal{F}^\phi)$
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — as (H1); the theorem is stated at exactly this generality
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — same on $\mathbb{H}^3$
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — repairs (P3)

---

# Commentary

> [!note]- Commentary (skippable)
> The generalisation is not for its own sake. §2.3 manufactures a family of processes from Brownian motion by subordination, and most of them jump; stating the loop-measure construction at Dirichlet-form level means every theorem in §3 is proved once rather than four times.
>
> The cost is exactly (P2), and it is worth being precise that this is not a technical gap. For a subordinate process the operator is $\phi(\Delta_{X,g})$, which depends on $g$ itself and not merely on $[g]$. §3.4 is the section that cashes this out, and its content is largely negative.
