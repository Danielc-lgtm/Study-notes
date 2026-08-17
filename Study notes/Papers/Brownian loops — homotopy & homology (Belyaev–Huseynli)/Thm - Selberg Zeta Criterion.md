---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Weighted Heat-Kernel Integral Iϕ"
  - "Def - Selberg Zeta Function"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, spectral-geometry, zeta-functions, loop-measures]
---

# Notation

- $I_\phi(L)$ — the [[Constr - The Weighted Heat-Kernel Integral Iϕ|weighted heat-kernel integral]] of Definition 3.6
- $C>0$, $s>\delta$ — constants **independent of $L$**; $\delta$ the [[Def - Critical Exponent and the Prime Geodesic Theorem|critical exponent]]
- $L=m\ell_\gamma$; $Z_X(s)$ the [[Def - Selberg Zeta Function|Selberg zeta function]]
- $\mu^\phi_X$ — the subordinate Brownian loop measure

---

# Type card

> [!abstract] Type card — Lemma 4.2 (Selberg zeta criterion)
> **Given.** The function $I_\phi$ of [[Constr - The Weighted Heat-Kernel Integral Iϕ|Definition 3.6]], and the existence of a constant $C>0$ and a real number $s>\delta$, **both independent of $L$**, such that
> $$\frac{L}{2\sinh(L/2)}\,I_\phi(L) = C\cdot\frac{e^{(1-s)L}}{e^L-1}\qquad\text{for all }L>0.\tag{33}$$
>
> **Produces.** The identity $\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\phi_X(\mathcal{C}_X(\gamma^m)) = -C\log Z_X(s)$ — an equality of finite non-negative numbers.
>
> **Lets you.** Certify a zeta identity for a **new** Bernstein function by checking one scalar functional equation in one variable. No geometry, no group theory, no heat kernel appears in the hypothesis: the entire geometric content has been absorbed into the *shape* of the right-hand side of (33).

---

# Statement

> **Lemma 4.2 (Selberg zeta criterion).** Let $I_\phi$ be as in Definition 3.6 and suppose there exist a constant $C>0$ and a real number $s>\delta$, both independent of $L$, such that
> $$\frac{L}{2\sinh(L/2)}I_\phi(L) = C\cdot\frac{e^{(1-s)L}}{e^L-1},\qquad L>0.\tag{33}$$
> Then
> $$\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = -C\log Z_X(s).\tag{34}$$

---

# Why it is true

The lemma is a shape-matching statement, and seeing it that way explains both why it is easy and why it is worth having.

[[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] gives the mass as $\frac1m\cdot\frac{L}{2\sinh(L/2)}I_\phi(L)$, where the factor $1/m$ is separated out and everything else is a function of $L=m\ell_\gamma$ alone. Separately, the logarithmic expansion (32) of the Selberg zeta function is
$$-\log Z_X(s) = \sum_{\gamma}\sum_{m\geq1}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},$$
which has *exactly the same shape*: a factor $1/m$ times a function of $L$. So the two agree term by term precisely when the two functions of $L$ agree, which is (33).

**The mechanism in one line: the loop mass and the logarithm of the Selberg zeta function are both of the form $\frac1m f(L)$ summed over $\gamma$ and $m$, so an identity between them is an identity between two functions of one variable.**

What makes this worth stating as a lemma rather than an observation is what it *removes*. The hypothesis (33) contains no surface, no group, no kernel — it is a functional equation for a function $(0,\infty)\to(0,\infty)$ built from $V_\phi$. So the question "does this process give a Selberg zeta identity?" is answerable without any geometry, by a one-variable calculation. **All four of the paper's processes are verified this way in §4.1, and a fifth would be too.**

The requirement that $C$ and $s$ be **independent of $L$** is the whole substance of the hypothesis. Any $I_\phi$ can be forced into the form (33) pointwise by letting $C$ depend on $L$; the content is that a single pair $(C,s)$ works for all $L$ at once, which is what allows the sum to be recognised as $-C\log Z_X(s)$ with a *fixed* argument $s$.

---

# Strategy

**Strategy.** Rewrite Theorem 3.5 as $\mu^\phi_X(\mathcal{C}_X(\gamma^m))=\frac1m\cdot\frac{L}{2\sinh(L/2)}I_\phi(L)$ using $\ell_\gamma=L/m$; substitute the hypothesis (33); then match term by term against the expansion (32) of $-\log Z_X(s)$, with absolute convergence supplied by $s>\delta$.

> [!note]- Proof (skippable)
> By (24) and $L=m\ell_\gamma$,
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L) = \frac1m\cdot\frac{L}{2\sinh(L/2)}I_\phi(L),$$
> using $\ell_\gamma=L/m$.
>
> Substituting the hypothesis (33) gives
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = C\cdot\frac1m\cdot\frac{e^{(1-s)L}}{e^L-1} = C\cdot\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.$$
>
> Summing over $\gamma\in\mathcal{P}_X$ and $m\geq1$ matches, term for term, $C$ times the right-hand side of the expansion (32) of $-\log Z_X(s)$. Absolute convergence — which is what licenses summing in any order and identifying the result with the value of the Euler product's logarithm — is ensured by $s>\delta$. Hence (34). $\;\square$

---

# What this assumes, and where to climb

**Theorem 3.5**, in the form (24) — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]], and through it the entire §3 stack. Note the lemma uses (24) rather than (21): the separation of the factor $1/m$ from the function of $L$ is the shape the argument needs, and it comes from $\ell_\gamma=L/m$.

**The logarithmic expansion of $Z_X$** — [[Def - Selberg Zeta Function]], equation (32). The double Euler product is what produces the $1/(e^{m\ell_\gamma}-1)$ factor, and hence what makes the shapes match at all. This is the reason the criterion produces a *Selberg* identity and not a Ruelle one; see the discussion on [[Def - Ruelle Zeta Function and its Twist]].

**$s>\delta$** — [[Def - Critical Exponent and the Prime Geodesic Theorem]]. Two jobs: it puts $s$ in the region of absolute convergence of the Euler product, and by [[Thm - Finiteness of the Total Mass|Corollary 4.7]] it is exactly the condition making both sides of (34) finite. The lemma would be vacuous without it.

**Independence of $C$ and $s$ from $L$** — the hypothesis, restated because it is easy to lose. A pointwise-in-$L$ version of (33) is no hypothesis at all.

---

# What consumes this

- [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] — verifies (33) with $C=1$ and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, giving the paper's central identity
- [[§4 Zeta Identities and Finiteness of the Total Mass]] — §4.1.1 and §4.1.2, where the four cases are checked
- [[Thm - Finiteness of the Total Mass|Corollary 4.7]] — its proof begins by writing every case in the form $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$, which is exactly what (33) delivers
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]] — **by its failure**: [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]] gives $\frac1m|e^{mL_\gamma}-1|^{-2}$, which is not of the form (33), so the criterion does not apply and §7 has no zeta identity

The four verified cases and their constants:

| $\phi(\lambda)$ | $C$ | $s$ |
|---|---|---|
| $\lambda$ | $1$ | $1$ |
| $\lambda+\kappa$ | $1$ | $\tfrac12+\sqrt{\tfrac14+\kappa}$ |
| $\lambda^{\alpha/2}$ | $\alpha/2$ | $1$ |
| $(\lambda+\kappa)^{\alpha/2}$ | $\alpha/2$ | $\tfrac12+\sqrt{\tfrac14+\kappa}$ |

---

# Reading it against the rest of the paper

The lemma is the paper's clearest example of a good abstraction: it factors a family of results through a single checkable condition, and the condition has no geometry in it. Its practical value is forward-looking — a reader who invents a new Bernstein function needs only compute $I_\phi$ and check one functional equation.

Its limits are equally informative. The criterion demands the *specific* shape $C e^{(1-s)L}/(e^L-1)$, which is a strong constraint: it is precisely the shape produced by a double Euler product with the $k$-index summed geometrically. Anything outside that shape needs a different zeta function, and the paper's two examples of that are [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]] (which needs a *difference* of two loop measures) and §7 (which has no candidate at all). **What zeta function replaces (33) for a hyperbolic 3-manifold is the paper's most concrete unfinished question.**
