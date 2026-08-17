---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Weighted Potential Measure Vϕ"
  - "Ext - Phillips Subordination of Semigroups and Dirichlet Forms"
  - "Constr - Assumption 2.3 (Strictly Increasing Subordinator)"
tags: [paper, probability, subordination]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | Bernstein satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)\|(A2.3)]] |
| $\psi^\phi_t$ | law of $S_t$ on $[0,\infty)$; $\psi^\phi_t(\{0\})=0$ |
| $p^{\mathcal{E}}$ | $(0,\infty)\times X\times X\to[0,\infty)$; jointly measurable, symmetric, density w.r.t. $\operatorname{vol}_g$ |
| $p^\phi$ | $p^\phi(t,x,y)=\int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s)$ — [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms\|(PH)(C3)]] |
| $V_\phi$ | $\sigma$-finite measure on $(0,\infty)$, defined by (7) |
| $h$ | $(0,\infty)\to[0,\infty)$ measurable |

---

# Type card

> [!abstract] Type card — Lemma 2.11
> **Given.**
> **(H1)** $\phi$ Bernstein satisfying (A2.3).
> **(H2)** $(\mathcal{E},\mathcal{F})$ regular symmetric with jointly measurable density $p^{\mathcal{E}}$ against $\operatorname{vol}_g$.
> **(H3)** $x,y\in X$.
>
> **Produces.** An **identity in $[0,\infty]$** — both sides may be infinite; no integrability hypothesis is needed:
> $$\int_0^\infty\frac{\mathrm{d}t}{t}\,p^\phi(t,x,y)\;=\;\int_{(0,\infty)}p^{\mathcal{E}}(s,x,y)\,V_\phi(\mathrm{d}s).$$
>
> **Lets you.** Collapse in one step wherever a $\mathrm{d}t/t$ integral meets a subordinated kernel. Used twice, with the **same shape** both times: discharge the spatial integral first, name the result $h(s)$, then apply this lemma to $h$.

---

# Statement

> **Lemma 2.11.** Assume (H1),(H2). For all $x,y\in X$,
> $$\int_0^\infty\frac{\mathrm{d}t}{t}\,p^\phi(t,x,y) \;=\; \int_{(0,\infty)} p^{\mathcal{E}}(s,x,y)\,V_\phi(\mathrm{d}s).\tag{8}$$

**Form actually used downstream.** For any measurable $h\geq0$,
$$\int_0^\infty\frac{\mathrm{d}t}{t}\int_{[0,\infty)}h(s)\,\psi^\phi_t(\mathrm{d}s)\;=\;\int_{(0,\infty)}h(s)\,V_\phi(\mathrm{d}s),$$
which is (7) verbatim; (8) is the case $h=p^{\mathcal{E}}(\cdot,x,y)$.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms\|(PH)(C3)]] | $p^\phi(t,x,y)$ | $\int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s)$ |
| [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)\|(A2.3c)]] | $\psi^\phi_t(\{0\})$ | $=0$, so $[0,\infty)$ may be replaced by $(0,\infty)$ |
| [[Thm - Fubini-Tonelli Theorem\|Tonelli]] | non-negative jointly measurable integrand on $(0,\infty)\times(0,\infty)$ | exchange of $\int\mathrm{d}t/t$ and $\int\psi^\phi_t(\mathrm{d}s)$ |
| [[Constr - The Weighted Potential Measure Vϕ\|(7)]] | $h(s)=p^{\mathcal{E}}(s,x,y)$ | the right-hand side of (8) |

---

# Proof

**Strategy.** Substitute (PH)(C3) for $p^\phi$; exchange the two integrals by Tonelli, legitimate since everything is non-negative; read off (7) with $h(s)=p^{\mathcal{E}}(s,x,y)$.

> [!note]- Proof (skippable)
> Fix $x,y\in X$.
>
> **Step 1.** By (H1),(H2) and [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms|(PH)(C3)]],
> $$\int_0^\infty\frac{\mathrm{d}t}{t}\,p^\phi(t,x,y)=\int_0^\infty\frac{\mathrm{d}t}{t}\int_{(0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s),$$
> the inner integral over $(0,\infty)$ rather than $[0,\infty)$ by (A2.3c).
>
> **Step 2.** The integrand $(t,s)\mapsto p^{\mathcal{E}}(s,x,y)$ is non-negative — joint measurability of $p^{\mathcal{E}}$ is (H2), and $(t,s)\mapsto\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}t/t$ is a $\sigma$-finite kernel. [[Thm - Fubini-Tonelli Theorem|Tonelli]] applies with no further condition.
>
> **Step 3.** Take $h(s)=p^{\mathcal{E}}(s,x,y)$ in (7). $\;\square$

---

# Consumed by

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — with $h(s)=\dfrac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}$, the output of [[Ext - Wang–Xue Strip Identity|(WX)]]
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — with $h(s)=\dfrac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$, the output of [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity|(88)]]
- [[§2.3–2.4 Subordination and the Weighted Potential Measure]]

**As a move.** *Trigger:* a $\mathrm{d}t/t$ integral in front of a subordinated kernel, spatial integral already discharged. *Action:* name the discharged spatial integral $h(s)$ and collapse.

---

# Commentary

> [!note]- Commentary (skippable)
> The lemma says nothing that Definition 2.9 has not; its content is that Definition 2.9 was the right definition. **$t$ is a dummy variable of the subordination and appears nowhere in the geometry, so it can always be integrated out first, and $V_\phi$ is the name of the result.**
>
> Note what is *not* assumed: any finiteness. The identity holds in $[0,\infty]$, so both sides are simultaneously finite or infinite, and when finiteness matters downstream it is established separately — in §4 by [[Thm - Finiteness of the Total Mass|Corollary 4.7]].
>
> The technique is Schilling–Song–Vondraček's. What is specific to this paper is the weight: the classical potential measure uses $\mathrm{d}t$, and here the loop-measure construction forces $\mathrm{d}t/t$. That single change is what makes $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ in the Brownian case rather than Lebesgue measure, hence what produces the scale-invariance obstruction (P2) on [[Constr - The Weighted Potential Measure Vϕ]].
