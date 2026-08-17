---
type: section
paper: "BH26"
subject: brownian-loops
prereqs:
  - "§4 Zeta Identities and Finiteness of the Total Mass"
tags: [paper, section, spectral-theory]
---

# Signature

| symbol | type |
|---|---|
| $E$ | $=\frac{1}{4\pi}\big(4\zeta_{\mathbb{R}}'(-1)-\tfrac12+\log2\pi\big)\approx0.0538$ — universal |
| $C,C_1,\gamma_{\mathrm{EM}}$ | universal constants; $C=-\gamma_{\mathrm{EM}}+C_1$ |
| $S_X$ | the geometric term of [[Ext - Selberg Trace Formula (Heat Kernel Form)\|(STF)]]; $\int_0^\infty e^{-\kappa t}S_X(t)\frac{\mathrm{d}t}{t}=M_\kappa$ |
| $M_\kappa$ | $=\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=-\log Z_X(s)$ |
| $\widetilde{\mathrm{Li}}$ | cutoff logarithmic integral, $=0$ below $x=2$ |
| $P_X(\sigma)$ | the Polyakov correction relative to $g_{\mathrm{hyp}}$ |
| $\det_0$, ${}^0\mathrm{Tr}$ | renormalised determinant and 0-trace, for the non-compact case |
| $M,F,D_X,C_X$ | the (BJP) constants; $F=-\chi$, $D_X(1)=\log C_X-M$ |

> **Convention.** $\mathcal{G}(X)$ is **all** oriented closed geodesics, $\mathcal{P}_X$ the primitive ones; $\mathcal{G}(X)\setminus\mathcal{P}_X$ indexes the pairs $(\gamma,m)$ with $m\geq2$.

---

# The problem this section solves

> [!warning] On a finite-area surface the Brownian total mass is infinite
> By [[Thm - Finiteness of the Total Mass|Cor 4.7]], $\delta=1$ and $s=1$ gives divergence. §5 supplies a finite substitute, and identifies it with a determinant. **Two independent repairs are given and they agree**: killing plus a $\kappa\to0^+$ limit (§5.1(ii)), and length-spectrum truncation at $\kappa=0$ (§5.1(i)).

---

# Exports

> **(E1) Compact, Brownian.** $-\log{\det}_\zeta\Delta=-\mathrm{Area}(X)E+C+\sum_{\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X+\int_0^\infty\frac{\mathrm{d}(N_X(R)-\widetilde{\mathrm{Li}}(e^R))}{e^R-1}$. *([[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Thm 5.1(i)]], eq. (46).)*
>
> **(E2) Compact, killing.** $-\log{\det}_\zeta\Delta=-\mathrm{Area}(X)E+\log\kappa-\log Z_X(s)+O(\kappa)$, and in the limit
> $$\log{\det}_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1).\tag{49}$$
> *(Thm 5.1(ii), eqs. (47)–(49). Remark 5.2: this is D'Hoker–Phong's formula.)*
>
> **(E3) Compact, $\alpha$-stable.** $\log{\det}_\zeta\Delta^{\alpha/2}=\tfrac\alpha2\log{\det}_\zeta\Delta$, from $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$ and $\mu^\alpha_X=\tfrac\alpha2\mu_X$. *(Thm 5.1(iii), eq. (50).)*
>
> **(E4) Any metric in the conformal class.** $\log{\det}_\zeta\Delta_{X,g}=P_X(\sigma)+\mathrm{Area}(X)E+\log Z_X'(1)$ for $g=e^{2\sigma}g_{\mathrm{hyp}}$. *([[Thm - Polyakov's Formula via Brownian Loop Measure|Cor 5.4]], eqs. (57),(58).)*
>
> **(E5) Finite area with cusps.** $-\log\det_0(\Delta_X+\kappa)=F\kappa-M+\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))-D_X(s)$, and $\log\det_0\Delta_X=\log C_X+\log Z_X'(1)$. *([[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Thm 5.7]], eqs. (67),(68).)*
>
> **(E6) Infinite area (Remark 5.8).** $\delta<1$, total mass already finite, identity holds directly at $s=1$ with $Z_X(1)\neq0$ — no derivative, no renormalisation.

---

# The three regimes, side by side

| $X$ | trace class? | $0\in\mathrm{Spec}_{L^2}$? | determinant | global factor | local factor |
|---|---|---|---|---|---|
| closed | yes | yes ($\lambda_0=0$ simple) | ${\det}_\zeta$ | $Z_X'(1)$ | $\mathrm{Area}(X)E$ |
| finite area, $n_C$ cusps | **no** | yes | $\det_0$ | $Z_X'(1)$ | $\log C_X$ ($\chi$, $n_C$) |
| infinite area | no | **no** | $\det_0$ | $Z_X(1)$ | $\log C_X$ |

---

# Imported results

| import | used for | gap? |
|---|---|---|
| [[Ext - Selberg Trace Formula (Heat Kernel Form)\|(STF)]] | identifies $\int S_X\,\mathrm{d}t/t$ with the total loop mass | **yes** |
| [[Ext - Naud's Formula for the Log-Determinant\|(N)]] | the starting identity (45) of all of §5.1 | **yes** — deepest of §5.1 |
| [[Ext - Prime Geodesic Theorem\|(PGT$'$)]] (43) | convergence of the (46) integral | **yes** |
| Wang–Xue [WX25, (4.13)–(4.16)] | the error-function evaluation collapsing to $1/(e^R-1)$ | quoted, not reproduced |
| [[Ext - Polyakov Conformal Anomaly Formula\|(P)]] | (E4) | **yes**, shallow |
| [[Ext - Melrose Renormalised Trace Expansion\|(M)]] | well-posedness of $\det_0$ | **yes** — no DAG node at all |
| [[Ext - Borthwick–Judge–Perry Determinant Formula\|(BJP)]] | (E5) | **yes** — deepest of §5.2 |

---

# Subpages

- [[Def - Zeta-Regularised Determinant of the Laplacian]] — the compact-case definition
- [[Ext - Selberg Trace Formula (Heat Kernel Form)]] — (44), and $S_X$
- [[Ext - Naud's Formula for the Log-Determinant]] — (45)
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — Theorem 5.1
- [[Ext - Polyakov Conformal Anomaly Formula]] — Theorem 5.3
- [[Thm - Polyakov's Formula via Brownian Loop Measure]] — Corollary 5.4
- [[Def - Eisenstein Series and the Continuous Spectrum]] — why §5.1 breaks
- [[Def - Renormalised Integral and the 0-Trace]] — the replacement objects
- [[Ext - Melrose Renormalised Trace Expansion]] — their well-posedness
- [[Ext - Borthwick–Judge–Perry Determinant Formula]] — Theorem 5.5
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)]] — Theorem 5.7

---

# Consumed by

- [[§6 Probability Measures on Homotopy and Homology Classes]] — only through the remark that the $\kappa=0$ case is available via §5's expressions
- Nothing else. §6–§7 work with $\kappa>0$ and finite total mass.

---

# Commentary

> [!note]- Commentary (skippable)
> §5 is the section with the highest import-to-argument ratio in the paper, and it is worth being honest about that: the analysis (Selberg trace formula, Naud's formula, Melrose's b-calculus, Borthwick–Judge–Perry) is all quoted, and the paper's own contribution is a **substitution** — recognising $\int_0^\infty e^{-\kappa t}S_X(t)\,\mathrm{d}t/t$ and $-\log Z_X(s)$ as the total mass of Brownian loops in non-trivial free homotopy classes. That substitution is cheap, and it is also the point: it converts a spectral quantity into a statement about a random object.
>
> The structural lesson is that the divergence of the total loop mass is not an accident to be worked around but *the same phenomenon as the vanishing of $Z_X$ at $s=1$*, which is *the same phenomenon as $\lambda_0=0$*, which is *the same phenomenon as finite area*. Every repair in this section is a way of cancelling one $\log\kappa$ against another, and (49) and (68) are what survives.
>
> One asymmetry deserves emphasis. Part (i) of Theorem 5.1 renormalises by subtracting the prime-geodesic-theorem prediction $\widetilde{\mathrm{Li}}(e^R)$ from the actual count $N_X(R)$; what remains, $\int\frac{\mathrm{d}(N_X-\widetilde{\mathrm{Li}}(e^R))}{e^R-1}$, is a measure of how the length spectrum *fluctuates* around its asymptotic law. Part (ii) never mentions $N_X$ and works purely analytically. That the two produce the same number is the least obvious statement in the section, and the paper's proof establishes it by computing both against (45) rather than by comparing them directly.
