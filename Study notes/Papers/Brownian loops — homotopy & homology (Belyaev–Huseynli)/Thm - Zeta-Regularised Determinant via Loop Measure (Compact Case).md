---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Ext - Naud's Formula for the Log-Determinant"
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Thm - Selberg Zeta Identity (Killing Case)"
tags: [paper, spectral-theory, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $X$ | **closed** hyperbolic surface of genus $g$; $\mathrm{Area}(X)=4\pi(g-1)$ |
| $\mathcal{G}(X)$ | **all** oriented closed geodesics; $\mathcal{G}(X)\setminus\mathcal{P}_X$ = the non-primitive ones, i.e. the pairs $(\gamma,m)$ with $m\geq2$ |
| $E$ | $=\frac{1}{4\pi}\big(4\zeta_{\mathbb{R}}'(-1)-\tfrac12+\log2\pi\big)\approx0.0538$ — universal |
| $C$ | $=-\gamma_{\mathrm{EM}}+C_1$ — a universal constant |
| $\widetilde{\mathrm{Li}}$ | $\widetilde{\mathrm{Li}}(x)=\int_2^x\frac{\mathrm{d}t}{\log t}$ for $x\geq2$, $=0$ for $x<2$ |
| $N_X$ | the counting function; $\lvert N_X(R)-\widetilde{\mathrm{Li}}(e^R)\rvert=O_X(e^{(1-\epsilon)R})$ by (43) |
| $M_\kappa$ | $:=\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=-\log Z_X(s)$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ |

---

# Type card

> [!abstract] Type card — Theorem 5.1
> **Given.**
> **(H1)** $X=\Gamma\backslash\mathbb{H}^2$ closed hyperbolic of genus $g$.
> **(H2)** $\phi$ one of the Bernstein functions treated in the paper.
> **(H3)** [[Ext - Naud's Formula for the Log-Determinant|(N)]], i.e. formula (45).
>
> **Produces.** Three identities expressing $\log{\det}_\zeta\Delta$ through loop masses:
> **(i)** Brownian, with an explicit renormalisation of the primitive part;
> **(ii)** killing, exactly for each $\kappa>0$ up to $O(\kappa)$, and in the limit $\kappa\to0^+$ the closed form $\log{\det}_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1)$;
> **(iii)** $\alpha$-stable, $=\tfrac\alpha2\times$ (i).
>
> **Lets you.** Assign a **finite** value to the divergent total Brownian loop mass on a closed surface, and identify that value with a determinant. This is the repair of [[Thm - Finiteness of the Total Mass|Cor 4.7]]'s finite-area divergence.

---

# Statement

> **Theorem 5.1.** Assume (H1)–(H3). Write ${\det}_\zeta\Delta$ for the determinant with $\lambda_0=0$ excluded.
>
> **(i) Brownian, $\phi(\lambda)=\lambda$.**
> $$-\log{\det}_\zeta\Delta=-\mathrm{Area}(X)E+C+\sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X\big(\mathcal{C}_X(\gamma)\big)+\int_{R=0}^{\infty}\frac{1}{e^R-1}\,\mathrm{d}\Big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\Big).\tag{46}$$
>
> **(ii) Killing, $\phi(\lambda)=\lambda+\kappa$, $\kappa>0$.**
> $$-\log{\det}_\zeta\Delta=-\mathrm{Area}(X)E+\log\kappa+M_\kappa+O(\kappa)\tag{47}$$
> $$=-\mathrm{Area}(X)E+\log\kappa-\log Z_X\Big(\tfrac12+\sqrt{\tfrac14+\kappa}\Big)+O(\kappa),\tag{48}$$
> and letting $\kappa\to0^+$,
> $$\boxed{\ \log{\det}_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1).\ }\tag{49}$$
>
> **(iii) $\alpha$-stable, $\phi(\lambda)=\lambda^{\alpha/2}$.** (50) $=\tfrac\alpha2\times$ (46), with $\mu^\alpha_X=\tfrac\alpha2\mu_X$ on each class.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Ext - Naud's Formula for the Log-Determinant\|(N)]] | $X$ closed | (45) — the starting identity of all three parts |
| [[Ext - Selberg Trace Formula (Heat Kernel Form)\|(F2)]] | $S_X-S_X^{\mathrm{p}}$ | $\int_0^\infty\frac{S_X-S_X^{\mathrm{p}}}{t}\mathrm{d}t=\sum_{m\geq2}$ masses $=\sum_{\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X$ |
| [[Ext - Prime Geodesic Theorem\|(PGT$'$)]] (43) | $N_X-\widetilde{\mathrm{Li}}(e^R)$ | $O_X(e^{(1-\epsilon)R})$, hence convergence of the (46) integral |
| Wang–Xue [WX25, (4.13)–(4.16)] | the primitive $t$-integrals | error-function evaluation, collapsing to $1/(e^R-1)$ |
| [[Ext - Selberg Trace Formula (Heat Kernel Form)\|(F1)]] | $R_\kappa$ | $\lvert R_\kappa\rvert\leq\kappa\big(\int_0^1S_X+\int_1^\infty\lvert S_X-1\rvert\big)=O(\kappa)$ |
| $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ | the exponential integral | the $\gamma_{\mathrm{EM}}$ cancellation and the $\log\kappa$ |
| [[Thm - Selberg Zeta Identity (Killing Case)\|Cor 4.3]] | $M_\kappa$ | $M_\kappa=-\log Z_X(s)$, giving (48) |
| [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions\|(MC)(F1)]] | the simple zero of $Z_X$ at $s=1$ | $-\log Z_X(s)\sim-\log Z_X'(1)-\log\kappa$ |
| [[Def - Zeta-Regularised Determinant of the Laplacian\|(D5)]] | $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$ | part (iii) from part (i) |

---

# Proof

**Strategy (i).** Split $S_X$ into primitive and non-primitive parts. The non-primitive part converges with **no** renormalisation and is literally the sum of $m\geq2$ class masses; the primitive part is written as an integral against $\mathrm{d}N_X$, and renormalised by subtracting $\mathrm{d}\widetilde{\mathrm{Li}}(e^R)$, which contributes a universal constant.

**Strategy (ii).** For $\kappa>0$ nothing diverges, so compare $M_\kappa=\int_0^\infty e^{-\kappa t}S_X(t)\,\mathrm{d}t/t$ directly with (45); the difference is an exponential integral $E_1(\kappa)$ plus an $O(\kappa)$ correction.

**Strategy (iii).** Scale: $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$ and $\mu^\alpha_X=\tfrac\alpha2\mu_X$, so multiply (46) by $\alpha/2$.

> [!note]- Proof of (i) (skippable)
> The integral $\int_0^\infty\frac{\mathrm{d}N_X(R)}{e^R-1}$ is the total mass $\sum_{\gamma\in\mathcal{P}_X}\mu_X(\mathcal{C}_X(\gamma))$ of loops homotopic to a **primitive** geodesic; subtracting $\int_0^\infty\frac{\mathrm{d}\widetilde{\mathrm{Li}}(e^R)}{e^R-1}$ renormalises the contribution of long primitive geodesics as (43) suggests. By (43), $\lvert N_X(R)-\widetilde{\mathrm{Li}}(e^R)\rvert=O_X(e^{(1-\epsilon)R})$ for some $\epsilon>0$, so the integral in (46) converges by parts, and so does the sum.
>
> Split (45) as
> $$\int_0^1\frac{S_X}{t}+\int_1^\infty\frac{S_X-1}{t}=\int_0^\infty\frac{S_X-S_X^{\mathrm{p}}}{t}\,\mathrm{d}t+\int_0^1\frac{S_X^{\mathrm{p}}}{t}\,\mathrm{d}t+\int_1^\infty\frac{S_X^{\mathrm{p}}-1}{t}\,\mathrm{d}t,\tag{51}$$
> where $S^{\mathrm{p}}_X$ is the $m=1$ part of $S_X$.
>
> **Non-primitive part.** Term by term (each is the $m\geq2$ Gaussian integral of §3),
> $$\int_0^\infty\frac{S_X-S^{\mathrm{p}}_X}{t}\,\mathrm{d}t=\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq2}\frac1m\frac{1}{e^{m\ell_\gamma}-1}=\sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X\big(\mathcal{C}_X(\gamma)\big).\tag{52}$$
> **No renormalisation is needed here** — the $m\geq2$ classes are summable on their own.
>
> **Primitive part.** Write $S^{\mathrm{p}}_X(t)=\int_0^\infty\frac{e^{-t/4}}{(4\pi t)^{1/2}}\frac{R}{2\sinh(R/2)}e^{-R^2/4t}\,\mathrm{d}N_X(R)$ and exchange the order of integration in each of the two $t$-integrals. The inner $t$-integrals evaluate via the error function [WX25, (4.13)–(4.16)]. Decomposing $N_X=\widetilde{\mathrm{Li}}(e^R)+(N_X-\widetilde{\mathrm{Li}}(e^R))$: the $\mathrm{d}\widetilde{\mathrm{Li}}(e^R)$ part has no $X$-dependence and contributes a universal constant $C_1$; in the remaining part the error-function expression **collapses to $1/(e^R-1)$**. Hence
> $$\int_0^1\frac{S^{\mathrm{p}}_X}{t}+\int_1^\infty\frac{S^{\mathrm{p}}_X-1}{t}=C_1+\int_0^\infty\frac{1}{e^R-1}\,\mathrm{d}\big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\big).\tag{53}$$
> Substituting (52),(53) into (51) and combining with (45) gives (46) with $C=-\gamma_{\mathrm{EM}}+C_1$. $\;\square$

> [!note]- Proof of (ii) (skippable)
> For $\kappa>0$ the total mass is finite ([[Thm - Finiteness of the Total Mass|Cor 4.7]], $s>1=\delta$), so no cutoff is needed. The killing heat trace is $e^{-\kappa t}S_X(t)$, so
> $$M_\kappa=\int_0^\infty e^{-\kappa t}\frac{S_X(t)}{t}\,\mathrm{d}t=\int_0^1e^{-\kappa t}\frac{S_X}{t}+\int_1^\infty e^{-\kappa t}\frac{S_X-1}{t}+E_1(\kappa),\tag{54}$$
> with $E_1(\kappa)=\int_1^\infty e^{-\kappa t}\,\mathrm{d}t/t$. Comparing with (45)'s integrals,
> $$\int_0^1\frac{S_X}{t}+\int_1^\infty\frac{S_X-1}{t}=M_\kappa-E_1(\kappa)+R_\kappa,\tag{55}$$
> $$R_\kappa:=\int_0^1\frac{(1-e^{-\kappa t})S_X}{t}\,\mathrm{d}t+\int_1^\infty\frac{(1-e^{-\kappa t})(S_X-1)}{t}\,\mathrm{d}t.$$
> Since $1-e^{-\kappa t}\leq\kappa t$, $\lvert R_\kappa\rvert\leq\kappa\int_0^1S_X+\kappa\int_1^\infty\lvert S_X-1\rvert=O(\kappa)$, both integrals finite by (F1). With $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$, substituting (55) into (45) gives
> $$-\log{\det}_\zeta\Delta=-\mathrm{Area}(X)E-\gamma_{\mathrm{EM}}+M_\kappa-E_1(\kappa)+R_\kappa=-\mathrm{Area}(X)E+\log\kappa+M_\kappa+O(\kappa),$$
> the two $\gamma_{\mathrm{EM}}$ cancelling. This is (47); Corollary 4.3 turns $M_\kappa$ into $-\log Z_X(s)$, giving (48).
>
> **The limit.** As $\kappa\to0^+$, $s\to1$ and $Z_X$ has a **simple zero** at $s=1$ (from $\lambda_0=0$), so $-\log Z_X(s)\sim-\log Z_X'(1)-\log(s-1)$; since $s-1\sim\kappa$, the $-\log\kappa$ so produced cancels the $+\log\kappa$ of (48), the $O(\kappa)$ vanishes, and (49) remains. $\;\square$

---

# What this assumes, and where to climb

- **(N)** — [[Ext - Naud's Formula for the Log-Determinant]]: the deepest import, itself resting on (STF) and (PGT$'$). **This is the gap of §5.1.**
- **The Wang–Xue error-function computation** [WX25, (4.13)–(4.16)] — quoted, not reproduced. It is what makes the collapse to $1/(e^R-1)$ happen; the paper says "see [WX25] for the exact constants".
- **The simple zero of $Z_X$ at $s=1$** — [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions|(MC)(F1)]], and it exists precisely because $\lambda_0=0$. This is the same fact as the divergence of the total mass at $\kappa=0$, seen from the other side.
- **Universal constants $E,C,C_1,\gamma_{\mathrm{EM}}$** are not computed here; only their $X$-independence is used.
- **Not assumed:** any finiteness at $\kappa=0$. (i) works by renormalisation, (ii) by taking a limit; they are two different repairs of the same divergence and they agree.

---

# Consumed by

- [[Thm - Polyakov's Formula via Brownian Loop Measure]] — (49) is one of its two inputs
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.1
- [[Constr - The Probability Measure on Free Homotopy Classes]] — the remark that $\kappa=0$ is available "using the expressions from §5"

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the divergence of the total Brownian loop mass on a closed surface and the simple zero of $Z_X$ at $s=1$ are the same fact, and (49) is what is left when the two $\log\kappa$'s cancel.**
>
> Formula (49) is worth reading slowly: $\log{\det}_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1)$. On the right, a purely local term (area times a universal constant — the contractible loops) plus a purely global one ($Z_X'(1)$ — the length spectrum). It is the classical D'Hoker–Phong formula, and the paper recovers it by a route that never mentions strings: renormalise the Brownian loop measure by its length spectrum and read off the answer. Remark 5.2 makes the comparison explicit.
>
> Part (i) and part (ii) are genuinely different renormalisations. Part (ii) adds killing, computes exactly, and takes a limit — the divergence appears as $\log\kappa$ and is cancelled analytically. Part (i) stays at $\kappa=0$ and instead subtracts, from the primitive geodesic count, the number of geodesics the prime geodesic theorem predicts; the surviving integral $\int\frac{\mathrm{d}(N_X-\widetilde{\mathrm{Li}}(e^R))}{e^R-1}$ measures the *fluctuation* of the length spectrum around its prediction. That the two agree is not obvious from either derivation, and is the reason the theorem lists them as parts of one statement.
>
> Part (iii) is free, and slightly deflationary: the $\alpha$-stable determinant is just $\tfrac\alpha2$ times the Brownian one, because $\mu^\alpha_X=\tfrac\alpha2\mu_X$ class by class and $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$. Subordination by a stable law adds no new spectral information — consistent with the §3.1.3 collapse.
