---
type: section
paper: "BH26"
subject: brownian-loops
prereqs:
  - "§3 Decomposition over Homotopy Classes"
tags: [paper, section, zeta-functions]
---

> [!info] Part of [[Map - Brownian Loops on Homotopy and Homology Classes]]

# Signature

| symbol | type |
|---|---|
| $\mathcal{P}_X$ | primitive closed geodesics; $\ell_\gamma$ their lengths |
| $\delta$ | $\in(0,1]$ — [[Def - Critical Exponent\|critical exponent]]; $\delta=1\iff\mathrm{area}(X)<\infty$ |
| $Z_X$ | [[Def - Selberg Zeta Function\|Selberg zeta]], $\mathrm{Re}(s)>\delta$ |
| $R_X(\cdot,\rho)$ | [[Def - Ruelle Zeta Function and its Twist\|twisted Ruelle zeta]], $\mathrm{Re}(s)>c_\rho$ |
| $I_\phi$ | [[Constr - The Weighted Heat-Kernel Integral Iϕ\|Definition 3.6]] |
| $s(\phi),C(\phi)$ | spectral parameter and constant attached to $\phi$ by (33) |
| $\ell_{\mathrm{sys}}$ | the [[Def - Systole\|systole]] |
| $N_X$ | $N_X(R)=\#\{\gamma\in\mathcal{P}_X:\ell_\gamma\leq R\}$ |

> **Convention.** *Total mass* means the sum over **non-trivial, non-peripheral** free homotopy classes. The full loop measure always has infinite mass, because of the trivial class.

---

# Exports

> **(E1) The criterion.** If $\dfrac{L}{2\sinh(L/2)}I_\phi(L)=C\dfrac{e^{(1-s)L}}{e^L-1}$ for all $L>0$, with $C>0$ and $s>\delta$ **independent of $L$**, then $\sum_{\gamma,m}\mu^\phi_X(\mathcal{C}_X(\gamma^m))=-C\log Z_X(s)$. *([[Thm - Selberg Zeta Criterion|Lem 4.2]], eq. (33)–(34).)*
>
> **(E2) The killing identity.** For $\kappa\geq-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}>\delta$,
> $$\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)=-\log Z_X\Big(\tfrac12+\sqrt{\tfrac14+\kappa}\Big).\tag{35}$$
> *([[Thm - Selberg Zeta Identity (Killing Case)|Cor 4.3]]; $C=1$.)*
>
> **(E3) The twisted Ruelle identity.** For $\mathrm{Re}(s)>\max(c_\rho,\tfrac12)$, with $\kappa_\mp(s)=s(s\mp1)$,
> $$-\log R_X(s,\rho)=\sum_{\gamma,m}\mathrm{tr}\,\rho(\tau^m)\Big[\mu^{\kappa_-(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)-\mu^{\kappa_+(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)\Big].\tag{39}$$
> *([[Thm - Twisted Ruelle Zeta Identity|Cor 4.6]]. Stated, then not used again.)*
>
> **(E4) Finiteness.** $s(\phi)>\delta\Rightarrow$ total mass finite; $s(\phi)\leq\delta\Rightarrow$ divergent, and $Z_X(s)\to0$ as $s\downarrow\delta$. *([[Thm - Finiteness of the Total Mass|Cor 4.7]].)*
>
> **(E5) The dichotomy.** Infinite area ($\delta<1$): Brownian total mass $=-\log Z_X(1)<\infty$. Finite area ($\delta=1$): Brownian total mass $=\infty$; **killing $\kappa>0$ is necessary**.
>
> **(E6) Bose-gas reading (Remark 4.4).** With $Z(s):=Z_X(s)^{-1}$, (35) reads: total mass $=\log Z(s)$, the free energy of a non-interacting Bose gas with modes $(\gamma,k)$ of energy $(s+k)\ell_\gamma$, at zero chemical potential.

---

# Which $\phi$ satisfy the criterion

| $\phi(\lambda)$ | $V_\phi(\mathrm{d}s)$ | $C$ | $s(\phi)$ | finite iff |
|---|---|---|---|---|
| $\lambda$ | $\mathrm{d}s/s$ | $1$ | $1$ | $\delta<1$ |
| $\lambda+\kappa$, $\kappa\geq-\tfrac14$ | $e^{-\kappa s}\mathrm{d}s/s$ | $1$ | $\tfrac12+\sqrt{\tfrac14+\kappa}$ | $s>\delta$ |
| $\lambda^{\alpha/2}$, $\alpha\in(0,2)$ | $\tfrac\alpha2\,\mathrm{d}s/s$ | $\alpha/2$ | $1$ | $\delta<1$ |
| $(\lambda+\kappa)^{\alpha/2}$ | $\tfrac\alpha2e^{-\kappa s}\mathrm{d}s/s$ | $\alpha/2$ | $\tfrac12+\sqrt{\tfrac14+\kappa}$ | $s>\delta$ |

---

# Imported results

| import | used for | gap? |
|---|---|---|
| [[Ext - Prime Geodesic Theorem\|(PGT)]] | (E4) Step 2 — the comparison $s$ vs $\delta$ | **yes** — trace-formula consequence, no DAG anchor |
| [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions\|(MC)]] | interpretation only; §4's identities live inside $\{\mathrm{Re}(s)>\delta\}$ | **yes**, but not load-bearing here |
| Patterson–Sullivan, entropy readings of $\delta$ | context in Definition 4.1 | not used |

---

# Subpages

- [[Def - Selberg Zeta Function]] — Definition 4.1, and the expansion (32) that everything matches
- [[Def - Critical Exponent]] — $\delta$, and the five readings of it
- [[Thm - Selberg Zeta Criterion]] — Lemma 4.2, (E1)
- [[Thm - Selberg Zeta Identity (Killing Case)]] — Corollary 4.3, (E2)
- [[Def - Ruelle Zeta Function and its Twist]] — Definition 4.5
- [[Thm - Twisted Ruelle Zeta Identity]] — Corollary 4.6, (E3)
- [[Def - Systole]] — the constant in the §4.2 bound, and the §6.1 limit object
- [[Ext - Prime Geodesic Theorem]] — (40),(43)
- [[Thm - Finiteness of the Total Mass]] — Corollary 4.7, (E4),(E5)
- [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions]] — (MC)

---

# Consumed by

- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] — (E5) finite-area divergence is what §5 renormalises
- [[§6 Probability Measures on Homotopy and Homology Classes]] — (E2) is the normalising constant, (E4) is the existence hypothesis
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]] — the criterion is what §7 **cannot** verify; see its open question

---

# Commentary

> [!note]- Commentary (skippable)
> §4 costs almost nothing and delivers the paper's headline. §3 computed one number per free homotopy class; §4 adds them up and recognises the answer. The recognition is two applications of $-\log(1-x)=\sum x^m/m$, one to the outer product and one to the inner, and the shape $\frac1m\frac{e^{(1-s)L}}{e^L-1}$ that came out of the Wang–Xue strip identity is *exactly* the shape a Selberg Euler factor produces. That coincidence is the paper.
>
> The structure of §4.1 is worth imitating: rather than proving four identities, it isolates the hypothesis (33) — a functional equation in one real variable, with all the geometry integrated out — and then verifies it four times, each in two lines. The criterion is also the honest statement of the limitation: a general Bernstein $\phi$ produces an $I_\phi$ with no reason to satisfy (33), and then the total mass is simply not a zeta value.
>
> §4.2 is where the paper's second half is set up. The comparison $s>\delta$ — decay rate against proliferation rate — is a prime-number-theorem argument with geodesics for primes, and it fails in the case one cares about most: a closed surface with no killing. That failure is not a technical annoyance to be routed around; it is the reason §5 exists, and the reason the finite answer turns out to be $\log\det\Delta_X$.
