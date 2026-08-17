---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Weighted Heat-Kernel Integral Iϕ"
  - "Def - Selberg Zeta Function"
tags: [paper, zeta-functions, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $I_\phi$ | $(0,\infty)\to(0,\infty)$ — [[Constr - The Weighted Heat-Kernel Integral Iϕ\|Definition 3.6]] |
| $C$ | $\in(0,\infty)$, **independent of $L$** |
| $s$ | $\in\mathbb{R}$, $s>\delta$, **independent of $L$** |
| $L$ | $\in(0,\infty)$; in the application $L=m\ell_\gamma$ |
| $Z_X$ | the [[Def - Selberg Zeta Function\|Selberg zeta function]] |

---

# Type card

> [!abstract] Type card — Lemma 4.2
> **Given.**
> **(H1)** $\phi$ Bernstein with [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]], $I_\phi$ as in Definition 3.6.
> **(H2)** constants $C>0$ and $s>\delta$, **both independent of $L$**, such that
> $$\frac{L}{2\sinh(L/2)}\,I_\phi(L)=C\cdot\frac{e^{(1-s)L}}{e^L-1}\qquad\text{for all }L>0.\tag{33}$$
>
> **Produces.** The identity
> $$\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=-C\log Z_X(s).\tag{34}$$
>
> **Lets you.** Reduce "does the total mass equal a zeta value?" to a **functional equation in one real variable with no geometry in it**. Every corollary of §4.1 is one verification of (33).

---

# Statement

> **Lemma 4.2 (Selberg zeta criterion).** Assume (H1),(H2). Then (34) holds, with the sum absolutely convergent.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Constr - The Weighted Heat-Kernel Integral Iϕ\|(24)]] | $L=m\ell_\gamma$ | $\mu^\phi_X(\mathcal{C}_X(\gamma^m))=\frac1m\cdot\frac{L}{2\sinh(L/2)}I_\phi(L)$ |
| **(H2)**, i.e. (33) | that expression | $\mu^\phi_X(\mathcal{C}_X(\gamma^m))=C\cdot\frac1m\cdot\frac{e^{(1-s)L}}{e^L-1}$ |
| [[Def - Selberg Zeta Function\|(F1)]], eq. (32) | summing over $\gamma\in\mathcal{P}_X$, $m\geq1$ | $-C\log Z_X(s)$ |
| [[Def - Critical Exponent\|$s>\delta$]] | the double sum | absolute convergence |

---

# Proof

**Strategy.** Substitute (33) into (24); the resulting summand is term-by-term equal to the summand of the $-\log Z_X$ expansion (32).

> [!note]- Proof (skippable)
> By (24) with $L=m\ell_\gamma$,
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)=\frac1m\cdot\frac{L}{2\sinh(L/2)}I_\phi(L),$$
> using $\ell_\gamma=L/m$. Applying (33) to the second factor gives
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=C\cdot\frac1m\cdot\frac{e^{(1-s)L}}{e^L-1}.$$
> Summing over $\gamma\in\mathcal{P}_X$ and $m\geq1$ and comparing with (32) gives (34). Absolute convergence holds because $s>\delta$. $\;\square$

---

# What this assumes, and where to climb

- **The mass formula (24)** — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] and hence the whole §3 stack: unfolding, the (WX) strip identity, the [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11 collapse]].
- **Independence of $L$ in (H2)** is the entire content of the hypothesis. If $C$ or $s$ were allowed to depend on $L=m\ell_\gamma$, (33) would be vacuous — it could be solved for $C(L)$ pointwise — and the sum would not collapse to a zeta value.
- **$s>\delta$** — [[Def - Critical Exponent]]. Needed only for convergence, not for the term-by-term identity.
- **Not assumed:** any property of $\phi$ beyond Assumption 2.3. The lemma is a statement about the *function* $I_\phi$, and does not know where it came from.

---

# Which $\phi$ satisfy (33)

| $\phi(\lambda)$ | $C$ | $s$ | verification |
|---|---|---|---|
| $\lambda+\kappa$, $\kappa\geq-\tfrac14$ | $1$ | $\tfrac12+\sqrt{\tfrac14+\kappa}$ | §4.1.1, see below |
| $\lambda$ (Brownian) | $1$ | $1$ | the $\kappa=0$ case |
| $\lambda^{\alpha/2}$, $\alpha\in(0,2)$ | $\alpha/2$ | $1$ | §3.1.3: $V_\phi(\mathrm{d}s)=\tfrac\alpha2\,\mathrm{d}s/s$, so $I_\alpha=\tfrac\alpha2I_{\mathrm{BM}}$ |
| $(\lambda+\kappa)^{\alpha/2}$ shifted stable | $\alpha/2$ | $\tfrac12+\sqrt{\tfrac14+\kappa}$ | same collapse with killing |

> **§4.1.1 (the killing verification).** $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$ by (25), so
> $$\frac{L}{2\sinh(L/2)}I_\kappa(L)=\frac{e^{-L\sqrt{1/4+\kappa}}}{2\sinh(L/2)}=\frac{e^{(1-s)L}}{e^L-1},\qquad s=\tfrac12+\sqrt{\tfrac14+\kappa},$$
> using $2\sinh(L/2)=e^{L/2}-e^{-L/2}=e^{-L/2}(e^L-1)$. Hence $C=1$.

---

# Consumed by

- [[Thm - Selberg Zeta Identity (Killing Case)]] — the $\phi(\lambda)=\lambda+\kappa$ row
- [[Thm - Finiteness of the Total Mass]] — the four rows, and their constants $C$
- [[§4 Zeta Identities and Finiteness of the Total Mass]] §4.1

---

# Commentary

> [!note]- Commentary (skippable)
> The lemma is the paper's cleanest piece of factoring. §3 produced a mass formula in which the geometry ($\ell_\gamma$, $\sinh$) and the analysis ($I_\phi$) sit in separate factors; the criterion says that the zeta identity holds **iff the analytic factor happens to reproduce the geometric shape $e^{(1-s)L}/(e^L-1)$ up to a constant.** So a question about subordinators becomes a question about whether one explicit integral has one explicit closed form.
>
> The remarkable thing is how many $\phi$ pass. Killing works because the Gaussian integral $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ produces $e^{-L\sqrt{1/4+\kappa}}$, exactly the exponential the $\sinh$ needs. The stable case works for a different reason — scale invariance forces $V_\phi\propto\mathrm{d}s/s$ and the whole integral collapses to $\tfrac\alpha2$ times the Brownian one, with $s=1$ unchanged. Two mechanisms, one criterion.
>
> What does **not** pass is worth noting, and is the source of the paper's open question in §7: a general Bernstein $\phi$ gives an $I_\phi$ with no reason to be of the required shape, and then the total mass is simply not a zeta value.
