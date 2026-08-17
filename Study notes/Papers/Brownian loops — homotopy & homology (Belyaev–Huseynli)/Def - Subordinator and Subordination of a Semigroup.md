---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Bernstein Function and the Lévy–Khintchine Representation"
  - "Def - Dirichlet Form and the Hunt Process Correspondence"
tags: [paper, probability, subordination, dirichlet-forms]
---

# Notation

- $S_t$ — the subordinator: an increasing Lévy process on $[0,\infty)$, possibly killed at a constant rate
- $\phi$ — its Laplace exponent, a [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] with triple $(a,b,\nu)$
- $\psi^\phi_t$ — the law of $S_t$, a measure on $[0,\infty)$ with $|\psi^\phi_t|=e^{-at}$; a probability measure exactly when $a=0$
- $A$ — the generator of the base form, non-negative self-adjoint on $L^2(X,\mathrm{vol}_g)$; $\phi(A)$ its image under functional calculus
- $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ — the subordinate Dirichlet form; $p^\phi(t,x,y)$ its transition density
- $\rho$ — the hyperbolic area measure on $\mathbb{H}^2$
- $F_t$, $Z_t$ — the quantum clock and Liouville Brownian motion of Remark 2.4; $\varphi$ the Gaussian free field, $\gamma\in[0,2)$ the coupling constant

---

# In plain language

Subordination is running a Markov process on a random clock — where the clock is an independent increasing process. Take Brownian motion $B$, take an independent subordinator $S$, and look at $Y_u=B_{S_u}$. Because $S$ is increasing, $Y$ is again Markov; because $S$ is independent of $B$, the effect on the semigroup is pure averaging.

Everything follows from that averaging. The semigroup becomes $e^{-t\phi(A)}=\int_{[0,\infty)}e^{-sA}\,\psi^\phi_t(\mathrm{d}s)$, so the generator turns from $-A$ into $-\phi(A)$, and the transition density becomes an average of the old one against the subordinator's law. The map on generators is exactly the Bernstein function applied by functional calculus, which is why the class of admissible clocks is the class of Bernstein functions.

The one qualitative thing to hold on to: **if the Lévy measure of $\phi$ is non-trivial, the subordinate process jumps, even though the process you started with was a diffusion.** The clock skips forward, and the path skips with it. That is the entire reason [[Constr - The Dirichlet-Form Loop Measure|Definition 2.2]] needed càdlàg paths.

---

# The definition

> **Definition (subordinator).** A **subordinator** $S_t$ is an increasing Lévy process on $[0,\infty)$, possibly killed at a constant rate, whose Laplace exponent is a Bernstein function $\phi$:
> $$\mathbb{E}\big[e^{-\lambda S_t}\big] = e^{-t\phi(\lambda)},\qquad\lambda>0,\ t\geq0.\tag{2}$$
> Its law at time $t$ is written $\psi^\phi_t$. When $a=0$ the subordinator is **conservative** and $\psi^\phi_t$ is a probability measure; when $a>0$ it is killed at rate $a$ and $|\psi^\phi_t|=e^{-at}$.

> **Definition (subordination of a semigroup).** Let $(\mathcal{E},\mathcal{F})$ be a regular symmetric Dirichlet form on $L^2(X,\mathrm{vol}_g)$ with generator $A$, and let $\phi$ be a Bernstein function whose subordinator is independent of the underlying process. The **subordinate semigroup** is
> $$e^{-t\phi(A)} = \int_{[0,\infty)}e^{-sA}\,\psi^\phi_t(\mathrm{d}s),\qquad t\geq0,\tag{3}$$
> whose operator is $\phi(A)=aI+bA+\int_0^\infty(I-e^{-sA})\,\nu(\mathrm{d}s)$, so the generator of the subordinate process is $-\phi(A)$. Its **transition density** is
> $$p^\phi(t,x,y) = \int_{[0,\infty)}p^{\mathcal{E}}(s,x,y)\,\psi^\phi_t(\mathrm{d}s).\tag{4}$$

The subordinate process is again a $\mathrm{vol}_g$-symmetric Hunt process, associated with a regular symmetric Dirichlet form $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ on $L^2(X,\mathrm{vol}_g)$ given explicitly by
$$\mathcal{E}^\phi(u,u) = a\|u\|^2 + b\,\mathcal{E}(u,u) + \int_0^\infty\big(\|u\|^2 - \langle e^{-sA}u,u\rangle\big)\,\nu(\mathrm{d}s),\tag{5}$$
with domain $\mathcal{F}^\phi := \{u\in L^2(X,\mathrm{vol}_g) : \mathcal{E}^\phi(u,u)<\infty\}$. Read (5) against the Lévy–Khintchine triple: the three terms are the killing, the surviving diffusive part, and the jump part, in the same order as in $\phi$ itself.

**On the hyperbolic plane.** Applying this to Brownian motion on $\mathbb{H}^2$, whose Riemannian volume measure is the hyperbolic area $\rho$, the subordinate form $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ on $L^2(\mathbb{H}^2,\rho)$ has operator $\phi(\Delta_{\mathbb{H}^2})$ and heat kernel
$$p^\phi_{\mathbb{H}^2}(t,z,w) = \int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,w)\,\psi^\phi_t(\mathrm{d}s).\tag{6}$$
**Since $\Delta_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant and $\phi$ acts by functional calculus, $p^\phi_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant too.** That is a small remark with a large consequence: it is the hypothesis §3 needs in order to periodise the kernel over $\Gamma$ at all.

---

# Types and signatures

- $S : [0,\infty)\times\Omega\to[0,\infty)$ — a càdlàg increasing process with stationary independent increments
- $\psi^\phi_t$ — a measure on $[0,\infty)$, of total mass $e^{-at}$; **a sub-probability measure in general, a probability measure only when $a=0$**
- $\phi(A)$ — an unbounded non-negative self-adjoint operator on $L^2(X,\mathrm{vol}_g)$, defined by the functional calculus of $A$
- $e^{-t\phi(A)}$ — a strongly continuous contraction semigroup
- $p^\phi : (0,\infty)\times X\times X\to[0,\infty)$ — jointly measurable, symmetric in the space variables, a density against $\mathrm{vol}_g$; exists by [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]

---

# Example

$\phi(\lambda)=\lambda^{\alpha/2}$ with $\alpha\in(0,2)$: the operator is the fractional Laplacian $\Delta^{\alpha/2}_{\mathbb{H}^2}$, and
$$p^\alpha_{\mathbb{H}^2}(t,z,w) = \int_0^\infty p_{\mathbb{H}^2}(s,z,w)\,\eta^\alpha_t(s)\,\mathrm{d}s.$$
The process is pure-jump for every $\alpha\in(0,2)$, since the triple is $(0,0,\nu_\alpha)$ with $\nu_\alpha$ infinite: no drift means the clock advances only by jumps, and an infinite Lévy measure means infinitely many of them per unit time. The boundary case $\alpha=2$ gives $\phi(\lambda)=\lambda$, $\psi^\phi_t=\delta_t$, and Brownian motion back.

**Near-miss non-example — subordination is not time change by an additive functional (Remark 2.4).** Both operations produce a new Markov process by running the original one on a different clock, but they act on *orthogonal parts* of the data $(\mathcal{E},\mathcal{F},\mathrm{vol}_g)$, and confusing them is easy.

| | subordination | time change by a positive continuous additive functional |
|---|---|---|
| the clock | independent of the process, **not adapted** to its filtration | built from the process's own trajectory, **adapted** |
| generator | $-A\;\mapsto\;-\phi(A)$ | unchanged in form; the process is reparametrised |
| Dirichlet form | changed, to (5) | the same paths, re-run |
| reference measure | $\mathrm{vol}_g$ **unchanged** | replaced by the **Revuz measure** of the additive functional |
| path continuity | **destroyed** whenever $\nu\neq0$ | **preserved** |

The canonical example of the second column is Liouville Brownian motion: planar Brownian motion $B_t$ time-changed by the inverse of the "quantum clock" $F_t=\int_0^t e^{\gamma\varphi(B_s)}\,\mathrm{d}s$, with $\varphi$ the Gaussian free field and the exponential defined via Gaussian multiplicative chaos, giving $Z_t=B_{F^{-1}(t)}$ with coupling constant $\gamma\in[0,2)$. Reference for the general theory: Revuz–Yor, Chapter 10.

---

# Used in this paper at

- [[Constr - The Subordinate Brownian Loop Measure]] — Definition 2.8 is the loop-measure construction applied to $(\mathcal{E}^\phi,\mathcal{F}^\phi)$
- [[Constr - The Weighted Potential Measure Vϕ]] — $V_\phi$ collapses the $t$-integral against the family $\{\psi^\phi_t\}$
- [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] — proved by substituting (4) and applying Tonelli
- [[Constr - The Periodised Kernel]] — the $\mathrm{PSL}(2,\mathbb{R})$-invariance of $p^\phi_{\mathbb{H}^2}$ noted above is what makes the periodisation legitimate
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — the jumps introduced here are exactly what breaks the homotopy-class reading

---

# Where this sits in my DAG

Two anchors and one non-anchor. Lévy processes, Laplace exponents, and independence of the clock come from *Advanced Probability* (🟢) and *SDEs* (🟢). The functional calculus $A\mapsto\phi(A)$ for a non-negative self-adjoint operator comes from *Functional Analysis* (🟢) — see [[Def - Self-Adjoint Operator]] and [[Thm - Complex Spectral Theorem]]. The non-anchor rung below is [[Def - Bernstein Function and the Lévy–Khintchine Representation]], which itself reduces to anchors.

That the subordinate object is again a regular symmetric Dirichlet form, with the explicit expression (5), is quoted from Schilling–Song–Vondraček and Fukushima–Oshima–Takeda rather than proved; nothing downstream depends on the proof, since in every concrete case the form and its kernel are written out.
