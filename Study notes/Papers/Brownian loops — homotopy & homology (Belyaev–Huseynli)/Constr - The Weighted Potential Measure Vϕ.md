---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Subordinator"
  - "Constr - Assumption 2.3 (Strictly Increasing Subordinator)"
tags: [paper, probability, subordination]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | Bernstein satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)\|(A2.3)]]; triple $(a,b,\nu)$ |
| $\psi^\phi_t$ | law of $S_t$; measure on $[0,\infty)$, $\lvert\psi^\phi_t\rvert=e^{-at}$; $\psi^\phi_t(\{0\})=0$ by (A2.3) |
| $V_\phi$ | measure on $(0,\infty)$; $\sigma$-finite, **not** finite; absolutely continuous in every case here |
| $h$ | $(0,\infty)\to[0,\infty)$ measurable — a test function |
| $\eta^\alpha_t$ | $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(st^{-2/\alpha})$; $g_{\alpha/2}$ the standard $\alpha/2$-stable density, $\int g_{\alpha/2}=1$ |
| $\kappa$ | $\in[0,\infty)$; $\alpha\in(0,2)$ |

---

# Construction

> **Definition 2.9 (weighted potential measure).** $V_\phi$ is the $\sigma$-finite measure on $(0,\infty)$ characterised by
> $$\int_{(0,\infty)}h(s)\,V_\phi(\mathrm{d}s)\;=\;\int_0^\infty\frac{\mathrm{d}t}{t}\int_{(0,\infty)}h(s)\,\psi^\phi_t(\mathrm{d}s)\tag{7}$$
> for every measurable $h\geq0$ for which the right-hand side is finite. When $V_\phi\ll\mathrm{Leb}$ one writes $V_\phi(\mathrm{d}s)=V_\phi(s)\,\mathrm{d}s$.

**Two remarks on the statement.** (7) defines $V_\phi$ *by its action on test functions*, which is the form every use downstream takes. And the inner integral runs over $(0,\infty)$, not $[0,\infty)$ — legitimate, and losing no mass, exactly by (A2.3c): $\psi^\phi_t(\{0\})=0$.

**Name.** The *potential measure* of a subordinator is $\int_0^\infty\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}t$; this is the same with the Haar weight $\mathrm{d}t/t$ in place of $\mathrm{d}t$ — hence *weighted*. Technique from Schilling–Song–Vondraček Ch. 5.

---

# Type card

> [!abstract] Type card — Definition 2.9
> **Given.** **(H1)** $\phi$ Bernstein satisfying (A2.3), with laws $\{\psi^\phi_t\}_{t>0}$ on $[0,\infty)$.
>
> **Produces.** $V_\phi$: a $\sigma$-finite measure on $(0,\infty)$, **not finite** — in every case below it has a $\mathrm{d}s/s$ singularity at the origin. Absolutely continuous in every case treated.
>
> **Lets you.** Replace $\displaystyle\int_0^\infty\frac{\mathrm{d}t}{t}\int_{[0,\infty)}(\cdots)\,\psi^\phi_t(\mathrm{d}s)$ by $\displaystyle\int_{(0,\infty)}(\cdots)\,V_\phi(\mathrm{d}s)$ — the collapse performed by [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] and used in every mass computation of §3 and §7.

---

# Depends on

- [[Def - Subordinator]], [[Ext - Lévy–Khintchine Representation for Bernstein Functions]] — the laws $\psi^\phi_t$
- [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]] — (A2.3c), so $(0,\infty)$ suffices
- [[Thm - Fubini-Tonelli Theorem]] — Tonelli, for the exchange implicit in (7)

---

# Properties

**(P1) The four values (Example 2.10).**

| $\phi(\lambda)$ | process | $\psi^\phi_t$ | $V_\phi(\mathrm{d}s)$ |
|---|---|---|---|
| $\lambda$ | Brownian motion | $\delta_t$ | $\mathrm{d}s/s$ |
| $\lambda+\kappa$ | Brownian with killing | $e^{-\kappa t}\delta_t$ | $e^{-\kappa s}\,\mathrm{d}s/s$ |
| $\lambda^{\alpha/2}$ | $\alpha$-stable | $\eta^\alpha_t(s)\,\mathrm{d}s$ | $\tfrac{\alpha}{2}\,\mathrm{d}s/s$ |
| $(\lambda+\kappa)^{\alpha/2}$ | shifted $\alpha$-stable | $e^{-\kappa s}\eta^\alpha_t(s)\,\mathrm{d}s$ | $\tfrac{\alpha}{2}e^{-\kappa s}\,\mathrm{d}s/s$ |

> [!note]- Calculation of the four entries (skippable)
> **(a) $\phi(\lambda)=\lambda$.** $\psi^\phi_t=\delta_t$, so the inner integral in (7) is $h(t)$ and the $\mathrm{d}t/t$ integral **localises at $s=t$**: $\int_0^\infty h(t)\,\mathrm{d}t/t$. Hence $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$.
>
> **(b) $\phi(\lambda)=\lambda+\kappa$.** $\psi^\phi_t=e^{-\kappa t}\delta_t$; same localisation gives $\int_0^\infty h(t)e^{-\kappa t}\,\mathrm{d}t/t$, so $V_\phi(\mathrm{d}s)=e^{-\kappa s}\,\mathrm{d}s/s$.
>
> **(c) $\phi(\lambda)=\lambda^{\alpha/2}$.** $\psi^\phi_t(\mathrm{d}s)=t^{-2/\alpha}g_{\alpha/2}(st^{-2/\alpha})\,\mathrm{d}s$. For fixed $s$, substitute $u=st^{-2/\alpha}$; as $t$ ranges over $(0,\infty)$ so does $u$, with $\mathrm{d}t/t=\tfrac{\alpha}{2}\,\mathrm{d}u/u$ up to orientation, and
> $$\int_0^\infty\frac1t\,t^{-2/\alpha}g_{\alpha/2}\big(st^{-2/\alpha}\big)\,\mathrm{d}t=\frac{\alpha}{2s}\int_0^\infty g_{\alpha/2}(u)\,\mathrm{d}u=\frac{\alpha}{2s},$$
> using only $\int g_{\alpha/2}=1$. Hence $V_\phi(\mathrm{d}s)=\tfrac\alpha2\,\mathrm{d}s/s$. **The explicit form of $g_{\alpha/2}$ is never needed.**
>
> **(d) $\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$.** From
> $$e^{-t(\lambda+\kappa)^{\alpha/2}}=\int_0^\infty e^{-u(\lambda+\kappa)}\eta^\alpha_t(u)\,\mathrm{d}u=\int_0^\infty e^{-\lambda s}\,e^{-\kappa s}\eta^\alpha_t(s)\,\mathrm{d}s,$$
> the law is the exponential tilt $\psi^\phi_t(\mathrm{d}s)=e^{-\kappa s}\eta^\alpha_t(s)\,\mathrm{d}s$. Applying (c) to $h(s)e^{-\kappa s}$ gives $V_\phi(\mathrm{d}s)=\tfrac\alpha2 e^{-\kappa s}\,\mathrm{d}s/s$.

**(P2) Scale-invariance obstruction — structural, not accidental.** In row (c) the Haar measure is preserved up to the constant $\alpha/2$, and this is forced:
$$\{\text{self-similar subordinators}\}=\{\text{stable}\},\qquad \mathrm{d}t/t\ \text{is scale-invariant},$$
and the only measures on $(0,\infty)$ compatible with both scalings are constant multiples of $\mathrm{d}s/s$. **Consequence:** any scale-invariant subordination gives $\mu^\phi_X=c\,\mu_X$ and reveals nothing about the geometry of $X$ beyond what Brownian motion already reveals. Row (d) exists to break the scaling.

---

# Consumed by

- [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]] — the identity that makes $V_\phi$ usable
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — as (H1); $V_\phi$ is what the closed form integrates against
- [[Constr - The Weighted Heat-Kernel Integral Iϕ]] — $I_\phi:=\int(\cdots)\,V_\phi(\mathrm{d}s)$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — same role in $\mathbb{H}^3$
- [[Thm - Selberg Zeta Criterion]] — indirectly, through $I_\phi$
- [[§2.3–2.4 Subordination and the Weighted Potential Measure]] — the four special cases

---

# Commentary

> [!note]- Commentary (skippable)
> $V_\phi$ is what is left of the subordination after the loop-duration integral has been carried out. The situation it resolves: a subordinate loop measure carries two integrals, one over $t$ with weight $\mathrm{d}t/t$ and one over $s$ against $\psi^\phi_t$, and $t$ appears nowhere in the geometry. So integrate it out first; what remains is a single measure in $s$ carrying everything the loop measure can see about $\phi$.
>
> After [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] the choice of process appears in exactly one place: as the measure integrated against. Remembering the four-row table is enough to generate every special case in §3.1 and §7 without re-reading a proof.
>
> (P2) is the section's one negative result and is worth carrying forward: it says in advance that §3.1.3 will collapse, and why.
