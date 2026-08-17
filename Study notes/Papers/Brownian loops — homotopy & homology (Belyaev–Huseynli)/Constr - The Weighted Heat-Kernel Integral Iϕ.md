---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Weighted Potential Measure Vϕ"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, probability, loop-measures]
---

# Notation

- $\phi$ — a Bernstein function satisfying Assumption 2.3; $V_\phi$ its [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] on $(0,\infty)$
- $L>0$ — a length; in applications $L=m\ell_\gamma$
- $I_\phi : (0,\infty)\to(0,\infty]$ — the weighted heat-kernel integral
- $I_{\mathrm{BM}}$, $I_\kappa$, $I_\alpha$ — the specialisations to Brownian motion, killing at rate $\kappa$, and $\alpha$-stable
- $s$ — the subordination variable inside the integral; in §4 the same letter is the spectral parameter

---

# In plain language

The name for the analytic half of [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]].

That theorem produced a mass as a geometric prefactor times an integral, and the two halves never interact: the prefactor depends only on the geodesic, the integral only on the process and the length $L$. Naming the integral $I_\phi(L)$ separates them cleanly, and the point of the separation is §4. [[Thm - Selberg Zeta Criterion|Lemma 4.2]] states a criterion for a Selberg zeta identity as a **functional equation for $I_\phi$ alone** — one function of one real variable, with no geometry, no group theory and no heat kernel in the statement. Verifying that a new Bernstein function yields a zeta identity becomes a one-variable calculation.

The other reason to name it is that $I_\phi$ is where all four special cases differ, and once computed they are reusable. Every formula in §3.1 and §4.1 is $I_\phi$ from the table below, dropped into (24).

---

# The construction

> **Definition 3.6.** For the following we isolate the integral against the weighted potential measure
> $$I_\phi(L) := \int_0^\infty\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s),\qquad L>0,\tag{23}$$
> so that Theorem 3.5 reads
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L),\qquad L=m\ell_\gamma.\tag{24}$$

Using $\ell_\gamma=L/m$, the equivalent form
$$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{L}{2\sinh(L/2)}\,I_\phi(L)$$
is the one Lemma 4.2 operates on: it separates the factor $1/m$, which will be summed into a logarithm, from the factor $\frac{L}{2\sinh(L/2)}I_\phi(L)$, which is a function of $L$ alone.

---

# Type card

> [!abstract] Type card — the weighted heat-kernel integral $I_\phi$
> **Given.** A Bernstein function $\phi$ satisfying Assumption 2.3, hence its weighted potential measure $V_\phi$ on $(0,\infty)$; a length $L>0$.
>
> **Produces.** A number $I_\phi(L)\in(0,\infty]$; equivalently a function $I_\phi : (0,\infty)\to(0,\infty]$ of one real variable. Finite in every case the paper treats.
>
> **Lets you.** State [[Thm - Selberg Zeta Criterion|Lemma 4.2]] as a condition on a single function of one variable, with no geometry in it; and reduce every special case of §3.1 and §4.1 to substituting one line of the table below.

---

# Properties relied on later

**The four values.** All four follow from the single integral identity
$$\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s = \sqrt{\frac{\pi}{b}}\,e^{-2\sqrt{ab}},$$
applied with $b=L^2/4$ throughout and $a$ shifted by the killing rate.

| $\phi(\lambda)$ | $V_\phi(\mathrm{d}s)$ | $I_\phi(L)$ | resulting mass $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ |
|---|---|---|---|
| $\lambda$ | $\mathrm{d}s/s$ | $\dfrac{e^{-L/2}}{L}$ | $\dfrac1m\cdot\dfrac{1}{e^L-1}$ |
| $\lambda+\kappa$ | $e^{-\kappa s}\,\mathrm{d}s/s$ | $\dfrac{e^{-L\sqrt{1/4+\kappa}}}{L}$ | $\dfrac1m\cdot\dfrac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1}$ |
| $\lambda^{\alpha/2}$ | $\tfrac\alpha2\,\mathrm{d}s/s$ | $\dfrac{\alpha}{2}\cdot\dfrac{e^{-L/2}}{L}$ | $\dfrac{\alpha}{2}\cdot\dfrac1m\cdot\dfrac{1}{e^L-1}$ |
| $(\lambda+\kappa)^{\alpha/2}$ | $\tfrac\alpha2 e^{-\kappa s}\,\mathrm{d}s/s$ | $\dfrac{\alpha}{2}\cdot\dfrac{e^{-L\sqrt{1/4+\kappa}}}{L}$ | $\dfrac{\alpha}{2}\cdot\dfrac1m\cdot\dfrac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1}$ |

> [!note]- Calculation (skippable) — the Brownian and killing entries
> **Brownian.** With $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$,
> $$I_{\mathrm{BM}}(L) = \int_0^\infty\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi}\,s^{3/2}}\,\mathrm{d}s.$$
> The identity with $a=1/4$, $b=L^2/4$ gives $\int_0^\infty s^{-3/2}e^{-s/4-L^2/4s}\,\mathrm{d}s = \sqrt{\pi/(L^2/4)}\,e^{-2\sqrt{L^2/16}} = \frac{2\sqrt\pi}{L}e^{-L/2}$. Dividing by $2\sqrt\pi$ gives $I_{\mathrm{BM}}(L)=e^{-L/2}/L$.
>
> Then $\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-L/2}}{L} = \frac{\ell_\gamma}{L}\cdot\frac{e^{-L/2}}{2\sinh(L/2)} = \frac1m\cdot\frac{1}{e^L-1}$, using $\ell_\gamma/L=1/m$ and $e^{-L/2}/(2\sinh(L/2))=e^{-L/2}/(e^{L/2}-e^{-L/2})=1/(e^L-1)$.
>
> **Killing.** With $V_\phi(\mathrm{d}s)=e^{-\kappa s}\,\mathrm{d}s/s$ the same identity applies with $a=\tfrac14+\kappa$, giving $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$ and hence, writing $s=\tfrac12+\sqrt{\tfrac14+\kappa}$,
> $$\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1} = \frac1m\cdot\frac{e^{(1-s)L}}{e^L-1}.$$
> The stable rows follow because $V_\phi$ differs from the corresponding non-stable row only by the constant $\alpha/2$.

**The shape that Lemma 4.2 wants.** In all four rows,
$$\frac{L}{2\sinh(L/2)}I_\phi(L) = C\cdot\frac{e^{(1-s)L}}{e^L-1}$$
with $(C,s)$ equal to $(1,1)$, $(1,\tfrac12+\sqrt{\tfrac14+\kappa})$, $(\tfrac\alpha2,1)$ and $(\tfrac\alpha2,\tfrac12+\sqrt{\tfrac14+\kappa})$ respectively. That the four all satisfy the criterion is the content of §4.1.

**The stable collapse, visible here.** Rows 1 and 3 differ only by the constant $\alpha/2$, and rows 2 and 4 likewise. So no stable subordination produces a mass with a genuinely different functional dependence on $L$ — the constant is all that moves. The structural reason is on [[Constr - The Weighted Potential Measure Vϕ]]: scale invariance forces $V_\phi\propto\mathrm{d}s/s$.

---

# Consumed by

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — restated as (24) in terms of $I_\phi$
- [[Thm - Selberg Zeta Criterion|Lemma 4.2]] — the hypothesis is a functional equation for $\frac{L}{2\sinh(L/2)}I_\phi(L)$; this is the reason $I_\phi$ was named
- [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] — verifies the criterion using $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$
- [[Thm - Finiteness of the Total Mass|Corollary 4.7]] — the constant $C$ in its proof is the $C$ of the table
- [[§3 Decomposition over Homotopy Classes]] §3.1.1–3.1.4 — the four worked cases

---

# Where this sits in my DAG

Reduces to [[Constr - The Weighted Potential Measure Vϕ]] and to [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]], adding no new dependency. The only analysis in it is the identity $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$, which is a standard Gaussian-type evaluation — anchor material from *Analysis of PDEs* (🟢), provable by the substitution $u=\sqrt{a s}-\sqrt{b/s}$ and is worth having by heart, since it discharges four cases in §3.1 and one more in [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]].
