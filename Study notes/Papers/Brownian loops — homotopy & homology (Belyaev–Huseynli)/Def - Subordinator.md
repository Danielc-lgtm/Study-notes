---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Bernstein Function"
  - "Ext - Lévy–Khintchine Representation for Bernstein Functions"
tags: [paper, probability, subordination]
---

# Signature

| symbol | type |
|---|---|
| $S$ | $[0,\infty)\times\Omega\to[0,\infty)$; càdlàg, increasing, stationary independent increments; $S_0=0$ |
| $\phi$ | $(0,\infty)\to[0,\infty)$; the Laplace exponent, a [[Def - Bernstein Function\|Bernstein function]] with triple $(a,b,\nu)$ |
| $\psi^\phi_t$ | law of $S_t$; measure on $[0,\infty)$; $\lvert\psi^\phi_t\rvert=e^{-at}$ — a **sub**-probability unless $a=0$ |
| $B$ | the base process, independent of $S$ |
| $Y$ | $Y_u:=B_{S_u}$ — the subordinate process |
| $F$ | $\alpha$-stable case: $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(st^{-2/\alpha})$, density of $\psi^\phi_t$ |

---

# Definition

> **Definition (subordinator).** $S$ is a **subordinator** with Laplace exponent $\phi$ if
> **(D1)** $S$ is a Lévy process on $[0,\infty)$: $S_0=0$, càdlàg, stationary independent increments;
> **(D2)** $S$ is increasing: $u\leq v\implies S_u\leq S_v$ a.s.;
> **(D3)** $\ \mathbb{E}\big[e^{-\lambda S_t}\big]=e^{-t\phi(\lambda)}$ for all $\lambda>0$, $t\geq0$.
>
> Possibly *killed*: when $a>0$ the process is sent to $\partial$ at rate $a$ and $\lvert\psi^\phi_t\rvert=e^{-at}<1$.

> **Definition (the subordinate process).** Given a Markov process $B$ on $E$ and a subordinator $S$ **independent of $B$**, set
> $$Y_u := B_{S_u}.$$
> $Y$ is again Markov ($S$ increasing), and its semigroup is the $\psi^\phi_t$-average of $B$'s — see [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms|(PH)]] for the exact statement.

**Gloss.** Run the process on an independent random clock; the clock's law is $\psi^\phi_t$ and its Laplace exponent is $\phi$.

> **(F1) Independence is essential.** (PH) requires $S\perp B$. A clock built from $B$'s own trajectory is a different operation entirely — see the contrast table below.

---

# Type card

> [!abstract] Type card — subordinator and subordinate process
> **Given.** **(H1)** $\phi$ Bernstein. **(H2)** a Markov process $B$ on $E$. **(H3)** $S\perp B$.
>
> **Produces.** A process $S$ satisfying (D1)–(D3), unique in law by [[Ext - Lévy–Khintchine Representation for Bernstein Functions|(LK′)]]; and a Markov process $Y_u=B_{S_u}$ on $E$ whose generator is $-\phi(A)$ where $-A$ generates $B$.
>
> **Lets you.** Manufacture new [[Def - Regular Symmetric Dirichlet Form|regular symmetric Dirichlet forms]] from one, parametrised by $\phi$ — which is what makes §3's theorems cover four processes at once.

---

# Depends on

- [[Def - Bernstein Function]], [[Ext - Lévy–Khintchine Representation for Bernstein Functions]] — (H1) and existence of $S$
- [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]] — for what $Y$'s semigroup, generator and form are
- 🟢 Lévy processes; independence — *Advanced Probability*, *SDEs*

---

# Checks

**Instance.** $\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$, triple $(0,0,\nu_\alpha)$ with $\nu_\alpha(0,\infty)=\infty$. **No drift** $\Rightarrow$ the clock advances only by jumps; **infinite $\nu$** $\Rightarrow$ infinitely many jumps per unit time. So $Y$ is pure-jump even though $B$ is a diffusion. $\alpha=2$ gives $\phi(\lambda)=\lambda$, $\psi^\phi_t=\delta_t$, $Y=B$.

**Non-instance — subordination is not a PCAF time change (Remark 2.4).** Both run a process on a different clock; they act on **orthogonal parts** of the data $(\mathcal{E},\mathcal{F},\operatorname{vol}_g)$.

| | subordination | time change by a positive continuous additive functional |
|---|---|---|
| clock | **independent** of $B$, not adapted to its filtration | built from $B$'s own trajectory, **adapted** |
| generator | $-A\ \mapsto\ -\phi(A)$ | unchanged in form; paths reparametrised |
| Dirichlet form | changed, to [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms\|(5)]] | same paths, re-run |
| reference measure | $\operatorname{vol}_g$ **unchanged** | replaced by the **Revuz measure** of the additive functional |
| path continuity | **destroyed** whenever $\nu\neq0$ | **preserved** |

Canonical example of the right column: Liouville Brownian motion — planar $B_t$ time-changed by the inverse of $F_t=\int_0^te^{\gamma\varphi(B_s)}\,\mathrm{d}s$ with $\varphi$ the Gaussian free field and the exponential via Gaussian multiplicative chaos, giving $Z_t=B_{F^{-1}(t)}$, coupling $\gamma\in[0,2)$. Reference: Revuz–Yor Ch. 10.

---

# Used at

- [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]] — takes $S\perp B$ as (P3)
- [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]] — a condition on the law of $S_t$
- [[Constr - The Weighted Potential Measure Vϕ]] — $V_\phi$ collapses $\int_0^\infty\frac{\mathrm{d}t}{t}\psi^\phi_t$
- [[Constr - The Subordinate Brownian Loop Measure]] — the loop measure of $Y$
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — works on the space carrying the **pair** $(B,S)$, not on $Y$ alone

---

# Commentary

> [!note]- Commentary (skippable)
> The whole point of introducing subordination is that §2.2 licensed a loop measure for *any* regular symmetric Dirichlet form, and one then wants a supply of them. Subordination is a machine that takes one form and returns a one-parameter-family-of-families, indexed by Bernstein functions — and the indexing is by a function of one real variable, which is small enough to compute with.
>
> Remark 2.4 is worth reading rather than skipping: two operations that sound identical act on disjoint parts of the data, and the table above is the whole of it. The one line to remember is the last: subordination destroys path continuity, which is why §2.2 needed càdlàg paths and why §3 needs a separate convention for the jump case.
