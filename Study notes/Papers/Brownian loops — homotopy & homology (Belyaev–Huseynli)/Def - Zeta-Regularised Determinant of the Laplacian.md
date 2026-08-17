---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Schwinger Proper-Time Representation"
  - "Def - Transition Density and Heat Kernel"
tags: [paper, spectral-theory, zeta-functions]
---

# Signature

| symbol | type |
|---|---|
| $X$ | **closed** hyperbolic surface of genus $g$; $\mathrm{Area}(X)=4\pi(g-1)$ |
| $\{\lambda_j\}_{j\geq0}$ | $0=\lambda_0<\lambda_1\leq\lambda_2\leq\cdots\to\infty$, with multiplicity; $\lambda_0$ **simple** |
| $\zeta_X$ | $\{\mathrm{Re}(s)>1\}\to\mathbb{C}$, $\zeta_X(s):=\sum_{j\geq1}\lambda_j^{-s}$ — the **spectral** zeta |
| ${\det}_\zeta\Delta_X$ | $:=e^{-\zeta_X'(0)}\in(0,\infty)$ |
| $\chi(X)$ | $=2-2g$ |
| $\Delta_{\alpha/2}$ | the spectral fractional Laplacian; $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$ |

---

# Definition

> **Definition (zeta-regularised determinant).**
> $$\zeta_X(s):=\sum_{j\geq1}\frac{1}{\lambda_j^{s}}\ \ (\mathrm{Re}(s)>1),\qquad \log{\det}_\zeta\Delta_X:=-\zeta_X'(0).$$
> The $j=0$ term is omitted: $\lambda_0=0$ is excluded throughout.

> **(D1) Why $-\zeta_X'(0)$.** Formally $\zeta_X'(s)=-\sum_{j\geq1}\lambda_j^{-s}\log\lambda_j$, so $-\zeta_X'(0)\text{ “}=\text{”}\sum_{j\geq1}\log\lambda_j=\text{“}\log\prod_j\lambda_j\text{''}$ — the naive definition, which **diverges**. The zeta prescription (Ray–Singer) makes it finite.
>
> **(D2) Mellin form.** For $\mathrm{Re}(s)>1$,
> $$\zeta_X(s)=\frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}\Big(\mathrm{Tr}\big(e^{-t\Delta_X}\big)-1\Big)\,\mathrm{d}t,$$
> the $-1$ removing $\dim\ker\Delta_X=1$.
>
> **(D3) Why $\zeta_X$ continues, and is regular at $0$.** As $t\downarrow0$,
> $$\mathrm{Tr}\big(e^{-t\Delta_X}\big)-1\ \sim\ \frac{\mathrm{Area}(X)}{4\pi t}+\Big(\frac{\chi(X)}{6}-1\Big)+O(t).$$
> The $t^{-1}$ term gives $\zeta_X$ a simple pole at $s=1$; the constant term would give a pole at $s=0$, but the **simple zero of $1/\Gamma(s)$ at $s=0$ cancels it**. Hence $\zeta_X$ is analytic at $0$, with $\zeta_X(0)=\chi(X)/6-1$, and $\zeta_X'(0)$ is well defined.
>
> **(D4) Weyl's law.** $\lambda_j\sim4\pi j/\mathrm{Area}(X)$ as $j\to\infty$ — why $\zeta_X$ converges for $\mathrm{Re}(s)>1$.
>
> **(D5) Fractional case.** $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$, hence $\log{\det}_\zeta\Delta^{\alpha/2}=\tfrac\alpha2\log{\det}_\zeta\Delta_X$.

---

# Type card

> [!abstract] Type card — ${\det}_\zeta\Delta_X$
> **Given.** **(H1)** $X$ closed, so $\mathrm{Spec}(\Delta_X)$ discrete with finite multiplicities and $e^{-t\Delta_X}$ trace class. **(H2)** $\lambda_0=0$ excluded.
>
> **Produces.** A number ${\det}_\zeta\Delta_X\in(0,\infty)$ — a **regularised** product of the non-zero eigenvalues.
>
> **Lets you.** Attach a finite value to the divergent Schwinger integral of [[Def - Schwinger Proper-Time Representation|(S)]], hence to the divergent total Brownian loop mass on a closed surface. This finite value is what [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] expresses through the length spectrum.

---

# Depends on

- [[Def - Transition Density and Heat Kernel]] — the heat trace and its short-time expansion
- [[Def - Schwinger Proper-Time Representation]] — the divergent integral being regularised
- 🟢 Mellin transform, $\Gamma$-function, meromorphic continuation — *Complex Analysis*, *Functional Analysis* (8,10)
- Source: Ray–Singer (analytic torsion); Polyakov (bosonic string)

---

# Checks

**Instance (the answer, D'Hoker–Phong).** On a closed hyperbolic surface of genus $g$,
$${\det}_\zeta\Delta_X=Z_X'(1)\,e^{(2g-2)\left(2\zeta_{\mathbb{R}}'(-1)-\frac14+\frac12\log2\pi\right)}.$$
This is Remark 5.2, and it is exactly (49) rearranged: $\log{\det}_\zeta\Delta_X=\mathrm{Area}(X)E+\log Z_X'(1)$.

**Non-instance (fails H1).** $X$ non-compact of finite area. $\Delta_X$ has continuous spectrum $[\tfrac14,\infty)$, $e^{-t\Delta_X}$ is **not** trace class, and there is no sequence $\{\lambda_j\}$ to sum in $\zeta_X$. **Consequence:** §5.2 must replace $\mathrm{Tr}$ by the [[Def - Renormalised Integral and the 0-Trace|0-trace]] and $\zeta_X$ by $\zeta^0_X$.

**Non-instance (fails H2).** Including $\lambda_0=0$: then $\lambda_0^{-s}=\infty$ for every $s$ and $\zeta_X$ is undefined. On a **finite-area non-compact** surface $0$ is still an $L^2$ eigenvalue, which is why $\det_0\Delta_X$ is defined by dividing out a simple zero — see [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Thm 5.7]].

---

# Used at

- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — the object computed
- [[Ext - Naud's Formula for the Log-Determinant]] — its length-spectrum expression
- [[Ext - Polyakov Conformal Anomaly Formula]] — its transformation law under $g=e^{2\sigma}g_0$
- [[Def - Renormalised Integral and the 0-Trace]] — the non-compact replacement, (D5) there
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]]

---

# Commentary

> [!note]- Commentary (skippable)
> The regularisation is one clean trick and it is worth seeing why it is not arbitrary. $\sum_j\log\lambda_j$ diverges; $\sum_j\lambda_j^{-s}$ converges for $\mathrm{Re}(s)>1$ and its derivative at $s=0$ *would be* that sum if one could set $s=0$ naively. Analytic continuation gives the unique value compatible with the convergent regime, and (D3) shows the continuation is regular exactly at the point one needs — a fact about the heat expansion, not a coincidence one may assume.
>
> The place where this connects back to the paper: the total mass of Brownian loops on a closed surface is $\int_0^\infty\frac{\mathrm{d}t}{t}\mathrm{Tr}(e^{-t\Delta_X})$, divergent for the same $\mathrm{Area}(X)/4\pi t$ reason. §5.1 does **not** regularise it by zeta; it regularises by truncating along the **length spectrum**, following Wang–Xue, and then shows the answer agrees with $-\log\det_\zeta\Delta_X$ up to explicit constants. The two regularisations are different in method and identical in output, and that agreement is Theorem 5.1's content.
