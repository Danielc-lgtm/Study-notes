---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Weighted Potential Measure Vϕ"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
  - "Ext - Gaussian Reciprocal Integral Identity"
tags: [paper, probability, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | Bernstein satisfying (A2.3); $V_\phi$ its weighted potential measure on $(0,\infty)$ |
| $L$ | $\in(0,\infty)$; in applications $L=m\ell_\gamma$ |
| $I_\phi$ | $(0,\infty)\to(0,\infty]$; finite in every case treated |
| $I_{\mathrm{BM}},I_\kappa,I_\alpha$ | the specialisations $\phi(\lambda)=\lambda$, $\lambda+\kappa$, $\lambda^{\alpha/2}$ |
| $s$ | the **subordination** variable inside the integral |
| $\kappa,\alpha$ | $\kappa\geq0$; $\alpha\in(0,2)$ |

---

# Construction

> **Definition 3.6.** For $L>0$,
> $$I_\phi(L) \;:=\; \int_0^\infty\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s),\tag{23}$$
> so that [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] reads
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)=\frac1m\cdot\frac{L}{2\sinh(L/2)}\,I_\phi(L),\qquad L=m\ell_\gamma.\tag{24}$$

**Why name it.** (23) is the analytic half of the (WX) factorisation: **the only part of the mass formula that $\phi$ touches.** Naming it lets [[Thm - Selberg Zeta Criterion|Lemma 4.2]] state its hypothesis as a functional equation for one function of one real variable, with no geometry in it.

---

# Type card

> [!abstract] Type card — $I_\phi$
> **Given.** **(H1)** $\phi$ Bernstein satisfying (A2.3), hence $V_\phi$ on $(0,\infty)$. **(H2)** $L>0$.
>
> **Produces.** $I_\phi(L)\in(0,\infty]$; equivalently a function $I_\phi:(0,\infty)\to(0,\infty]$. Finite in every case treated.
>
> **Lets you.** State the Selberg zeta criterion with no geometry; and reduce every special case of §3.1 and §4.1 to one row of the table below.

---

# Depends on

- [[Constr - The Weighted Potential Measure Vϕ]] — the measure integrated against
- [[Ext - Wang–Xue Strip Identity]] — the integrand is (WX)'s analytic factor
- [[Ext - Gaussian Reciprocal Integral Identity]] — evaluates all four rows
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — the identity (24)

---

# Properties

**(P1) The four values.** All four are [[Ext - Gaussian Reciprocal Integral Identity|(GI)]] with $b=L^2/4$ and $a$ shifted by the killing rate.

| $\phi(\lambda)$ | $V_\phi(\mathrm{d}s)$ | (GI) at $(a,b)$ | $I_\phi(L)$ | $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ |
|---|---|---|---|---|
| $\lambda$ | $\mathrm{d}s/s$ | $(\tfrac14,\tfrac{L^2}4)$ | $\dfrac{e^{-L/2}}{L}$ | $\dfrac1m\cdot\dfrac{1}{e^L-1}$ |
| $\lambda+\kappa$ | $e^{-\kappa s}\,\mathrm{d}s/s$ | $(\tfrac14+\kappa,\tfrac{L^2}4)$ | $\dfrac{e^{-L\sqrt{1/4+\kappa}}}{L}$ | $\dfrac1m\cdot\dfrac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1}$ |
| $\lambda^{\alpha/2}$ | $\tfrac\alpha2\,\mathrm{d}s/s$ | $(\tfrac14,\tfrac{L^2}4)$ | $\tfrac\alpha2\cdot\dfrac{e^{-L/2}}{L}$ | $\tfrac\alpha2\cdot\dfrac1m\cdot\dfrac{1}{e^L-1}$ |
| $(\lambda+\kappa)^{\alpha/2}$ | $\tfrac\alpha2e^{-\kappa s}\,\mathrm{d}s/s$ | $(\tfrac14+\kappa,\tfrac{L^2}4)$ | $\tfrac\alpha2\cdot\dfrac{e^{-L\sqrt{1/4+\kappa}}}{L}$ | $\tfrac\alpha2\cdot\dfrac1m\cdot\dfrac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1}$ |

> [!note]- Calculation, rows 1 and 2 (skippable)
> **Row 1.** $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ gives $I_{\mathrm{BM}}(L)=\int_0^\infty\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt\pi\,s^{3/2}}\,\mathrm{d}s$. By (GI) with $a=\tfrac14$, $b=\tfrac{L^2}4$: the integral is $\sqrt{\pi/b}\,e^{-2\sqrt{ab}}=\frac{2\sqrt\pi}{L}e^{-L/2}$; dividing by $2\sqrt\pi$ gives $I_{\mathrm{BM}}(L)=e^{-L/2}/L$.
> Then, with $\ell_\gamma/L=1/m$ and $e^{-L/2}/2\sinh(L/2)=1/(e^L-1)$,
> $$\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-L/2}}{L}=\frac{\ell_\gamma}{L}\cdot\frac{e^{-L/2}}{2\sinh(L/2)}=\frac1m\cdot\frac1{e^L-1}.$$
> **Row 2.** Same with $a=\tfrac14+\kappa$: $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$, and with $s:=\tfrac12+\sqrt{\tfrac14+\kappa}$,
> $$\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac1m\cdot\frac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1}=\frac1m\cdot\frac{e^{(1-s)L}}{e^L-1}.$$
> **Rows 3, 4.** $V_\phi$ differs from rows 1, 2 by the constant $\tfrac\alpha2$ only.

**(P2) The shape the criterion wants.** In all four rows
$$\frac{L}{2\sinh(L/2)}\,I_\phi(L)=C\cdot\frac{e^{(1-s)L}}{e^L-1}$$
with $(C,s)$ equal to $(1,1)$, $\big(1,\tfrac12+\sqrt{\tfrac14+\kappa}\big)$, $\big(\tfrac\alpha2,1\big)$, $\big(\tfrac\alpha2,\tfrac12+\sqrt{\tfrac14+\kappa}\big)$. That all four satisfy [[Thm - Selberg Zeta Criterion|(33)]] is the content of §4.1.

**(P3) The stable collapse, visible here.** Rows 1,3 differ only by $\tfrac\alpha2$; likewise rows 2,4. **No stable subordination produces a mass with a different functional dependence on $L$.** Structural reason: [[Constr - The Weighted Potential Measure Vϕ|(P2) there]] — scale invariance forces $V_\phi\propto\mathrm{d}s/s$.

---

# Consumed by

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — restated as (24)
- [[Thm - Selberg Zeta Criterion]] — the hypothesis is a functional equation for $\frac{L}{2\sinh(L/2)}I_\phi(L)$
- [[Thm - Selberg Zeta Identity (Killing Case)]] — verifies it using row 2
- [[Thm - Finiteness of the Total Mass]] — the constant $C$ there is the $C$ of (P2)
- [[§3 Decomposition over Homotopy Classes]] — the four worked cases

---

# Commentary

> [!note]- Commentary (skippable)
> The whole content is a separation. (WX) produced a mass as (geometric prefactor) $\times$ (integral), and the two halves never interact — the prefactor depends only on the geodesic, the integral only on the process and $L$. Naming the integral separates them, and the point of the separation is §4: the criterion becomes checkable in one variable, so verifying a *new* Bernstein function is a one-variable calculation.
>
> The other reason to name it: the four values are computed once and reused. Every formula in §3.1 and §4.1 is a row of the table dropped into (24).
