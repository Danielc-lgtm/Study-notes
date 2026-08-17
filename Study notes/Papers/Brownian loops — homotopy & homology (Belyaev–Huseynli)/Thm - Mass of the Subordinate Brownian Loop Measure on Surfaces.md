---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces"
  - "Ext - Wang–Xue Strip Identity"
  - "Thm - Collapsing the Time Integral into the Weighted Potential Measure"
  - "Constr - The Weighted Potential Measure Vϕ"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | Bernstein satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)\|(A2.3)]] |
| $V_\phi$ | $\sigma$-finite measure on $(0,\infty)$; not finite |
| $\mu^\phi_X$ | subordinate Brownian loop measure on $\mathcal{C}_X$; $\sigma$-finite |
| $\gamma$ | $\in\mathcal{P}_X$, length $\ell_\gamma>0$; $m\in\mathbb{Z}_{\geq1}$ |
| $L$ | $:=m\ell_\gamma\in(0,\infty)$ — **real**; note $\ell_\gamma/L=1/m$ |
| $s$ | the **subordination** variable in this page; from §4 the same letter is the spectral parameter |
| $F_\tau$ | the fundamental strip; $\psi^\phi_t$ the subordinator law; $p_{\mathbb{H}^2}$ the speed-2 kernel |
| $I_\phi$ | $(0,\infty)\to(0,\infty]$; $I_\phi(L)=\int_0^\infty\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}V_\phi(\mathrm{d}s)$ |

---

# Type card

> [!abstract] Type card — Theorem 3.5
> **Given.**
> **(H1)** $\phi$ a [[Def - Bernstein Function|Bernstein function]] satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|(A2.3)]].
> **(H2)** $\gamma\in\mathcal{P}_X$ with translation length $\ell_\gamma>0$.
> **(H3)** $m\in\mathbb{Z}_{\geq1}$; set $L:=m\ell_\gamma$.
> **(H4)** For jump processes, the left side is read via [[Constr - Loop Mass in a Homotopy Class for Jump Processes|(13)]].
>
> **Produces.** $\mu^\phi_X(\mathcal{C}_X(\gamma^m))\in[0,\infty]$ in closed form:
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s).$$
>
> **Lets you.** Replace the double $(t,s)$ integral by **one** integral against $V_\phi$ — which makes every special case (Brownian, killing, $\alpha$-stable, shifted $\alpha$-stable) a one-line substitution of a measure on $(0,\infty)$.

---

# Statement

> **Theorem 3.5.** Assume (H1)–(H4). Then
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s),\qquad L=m\ell_\gamma.\tag{21}$$

> **Equivalent form used by §4.** With $I_\phi$ as in [[Constr - The Weighted Heat-Kernel Integral Iϕ|Definition 3.6]] and $\ell_\gamma=L/m$,
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)=\frac1m\cdot\frac{L}{2\sinh(L/2)}\,I_\phi(L).\tag{24}$$
> **(24) is the form [[Thm - Selberg Zeta Criterion|Lemma 4.2]] operates on**, because it isolates the $1/m$ that will become a logarithm.

**Not asserted:** any finiteness. (21) is an identity in $[0,\infty]$; finiteness of the *sum over all classes* is [[Thm - Finiteness of the Total Mass|Corollary 4.7]].

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces\|Thm 3.2]] | $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ | $\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^\phi_{\mathbb{H}^2}(t,z,\tau^mz)\,\mathrm{d}\rho(z)$ |
| [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms\|(PH)(C3)]] | $p^\phi_{\mathbb{H}^2}(t,\cdot,\cdot)$ | $\int_{[0,\infty)}p_{\mathbb{H}^2}(s,\cdot,\cdot)\,\psi^\phi_t(\mathrm{d}s)$ — eq. (6) |
| [[Thm - Fubini-Tonelli Theorem\|Tonelli]] | non-negative integrand on $(0,\infty)\times F_\tau\times[0,\infty)$ | exchange of $\int\mathrm{d}\rho$ and $\int\psi^\phi_t$ |
| [[Ext - Wang–Xue Strip Identity\|(WX)]] | $\int_{F_\tau}p_{\mathbb{H}^2}(s,z,\tau^mz)\,\mathrm{d}\rho(z)$ | $\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}$ |
| [[Thm - Collapsing the Time Integral into the Weighted Potential Measure\|Lem 2.11]] | $h(s)=\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}$ | $\int_0^\infty\frac{\mathrm{d}t}{t}\int h\,\mathrm{d}\psi^\phi_t=\int h\,\mathrm{d}V_\phi$ |

---

# Proof

**Strategy.** Evaluate the spatial integral by (WX), then collapse the $\mathrm{d}t/t$ integral into $V_\phi$ by Lemma 2.11.

> [!note]- Proof (skippable)
> **Step 0.** By Theorem 3.2 with $p^{\mathcal{E}}_{\mathbb{H}^2}=p^\phi_{\mathbb{H}^2}$, and expanding by (PH)(C3),
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}\int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,\tau^mz)\,\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}\rho(z).\tag{19}$$
> Note the three variables: geometry lives in $z$, subordination in $s$, and $t$ occurs **only** inside $\psi^\phi_t$.
>
> **Step 1 — the spatial integral.** Everything is non-negative, so Tonelli exchanges the $z$- and $s$-integrals. By (WX), for each fixed $s>0$,
> $$\int_{F_\tau}p_{\mathbb{H}^2}(s,z,\tau^mz)\,\mathrm{d}\rho(z)=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}.$$
> The prefactor is independent of $s,t$, so it exits both integrals:
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{\mathrm{d}t}{t}\int_{[0,\infty)}\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}\,\psi^\phi_t(\mathrm{d}s).\tag{22}$$
>
> **Step 2 — the time integral.** Apply Lemma 2.11 with $h(s)=\dfrac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}$, non-negative and measurable. This is (21). $\;\square$

---

# Consumed by

- [[Constr - The Weighted Heat-Kernel Integral Iϕ]] — names the integral, giving (24)
- [[§3 Decomposition over Homotopy Classes]] — §3.1.1–3.1.4, four substitutions
- [[Thm - Selberg Zeta Criterion]] — operates on (24)
- [[Thm - Loop Masses Determine the Marked Length Spectrum]] — inverts the Brownian and killing cases
- [[Constr - The Probability Measure on Free Homotopy Classes]] — the numerator of $\mathbb{P}_s$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — identical two-step strategy

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the geometry and the subordination live in different variables of the same triple integral, so each can be integrated out completely without touching the other, and the answer is their product.**
>
> Expanding (19) *looks* worse — three integrals instead of two — but the three variables are almost independent, and discharging them in the right order kills two. The spatial one goes first, by (WX), taking all the hyperbolic geometry with it; the time one second, by Lemma 2.11, taking all the subordination.
>
> The consequence is the architecture of the second half of the paper. **The prefactor is inert under changes of $\phi$; the integral is inert under changes of the surface.** Change the surface and only $\ell_\gamma$ moves; change the process and only $V_\phi$ moves. That is why §3.1's four cases are four table look-ups, and why §4's zeta criterion can be stated with no geometry in it.
>
> One narrowing to notice: Theorem 3.2 holds for any $\Gamma$-invariant Dirichlet form, but (WX) is about the *Brownian* kernel on $\mathbb{H}^2$. This is where the paper descends from Dirichlet-form generality to subordinate Brownian motion — (6) writes $p^\phi_{\mathbb{H}^2}$ as an average of $p_{\mathbb{H}^2}(s,\cdot,\cdot)$, and it is the inner Brownian kernel that (WX) evaluates. A form not obtained by subordinating Brownian motion leaves the spatial integral undischargeable, and Theorem 3.2 is as far as one could go.
>
> The Brownian specialisation recovers Wang–Xue [WX25, Lemma 3.2]; the killing one recovers Lemonde–Wang [LW26, Lemma 3.1]. The novelty is the *uniformity*, and the isolation of exactly where a new process would enter.
