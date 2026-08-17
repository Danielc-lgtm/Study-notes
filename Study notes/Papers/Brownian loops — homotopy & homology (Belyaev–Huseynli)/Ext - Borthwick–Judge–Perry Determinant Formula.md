---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, spectral-theory, zeta-functions]
---

# Signature

| symbol | type |
|---|---|
| $X$ | geometrically finite hyperbolic surface; $n_C$ cusps, $\chi=\chi(X)$ |
| $R_X(s)$ | $:=(\Delta_X-s(1-s))^{-1}$ — the resolvent |
| $\det_0$ | the renormalised determinant, [[Def - Renormalised Integral and the 0-Trace\|(62)]] |
| $G$ | the Barnes $G$-function; $G_\infty(s):=(2\pi)^{-s}\Gamma(s)G(s)^2$ |
| $M$ | $=\chi(X)\big(\tfrac12\log2\pi-2\zeta_{\mathbb{R}}'(-1)+\tfrac14\big)$ |
| $F$ | $=-\chi(X)$ |
| $D_X$ | defined in (66) below |
| $C_X$ | $=e^{M}(2\pi)^{-\chi(X)}\big(\sqrt{2\pi}\big)^{-n_C}$ |

---

# Statement

> **(BJP) Determinant–Selberg-zeta formula.** *Precondition:* **(P1)** $X$ geometrically finite hyperbolic with $n_C$ cusps and Euler characteristic $\chi$. *Conclusion:*
> $$\det{}_0\big(\Delta_X-s(1-s)\big)=Z_X(s)\,e^{M+Fs(1-s)}\,G_\infty(s)^{\chi}\left(\frac{(2\pi)^{s}}{\sqrt{\pi}\,\Gamma\big(s-\tfrac12\big)}\right)^{\!-n_C}\!\!\!\!,\tag{64}$$
> with $M,F$ as above. Consequently
> $$\det{}_0\Delta_X=\begin{cases}C_XZ_X'(1),&\mathrm{Area}(X)<\infty,\\ C_XZ_X(1),&\mathrm{Area}(X)=\infty.\end{cases}$$

> **(F1) How it is proved (not reproduced here).** From the resolvent identity
> $$\Big(\frac{1}{2s-1}\frac{\partial}{\partial s}\Big)^{2}\log\det{}_0\big(\Delta_X-s(1-s)\big)=-\,{}^0\mathrm{Tr}\big(R_X(s)^2\big),\tag{63}$$
> integrated in $s$; integration fixes the determinant up to a factor $e^{M+Fs(1-s)}$, whence the two constants.
>
> **(F2) The logarithmic form used in the paper.** Taking $-\log$ of (64) and separating the $Z_X$ term,
> $$-\log\det{}_0\big(\Delta_X-s(1-s)\big)=-Fs(1-s)-M-\log Z_X(s)-D_X(s),\tag{65}$$
> $$D_X(s):=\chi\log G_\infty(s)-\log\left(2^{sn_C}\big(\pi(s-\tfrac12)\big)^{n_C/2}\Gamma\big(s-\tfrac12\big)^{n_C}\right).\tag{66}$$
>
> **(F3) Why $Z_X'(1)$ in finite area (Remark 5.6).** $\mathrm{Area}(X)<\infty\Rightarrow0\in\mathrm{Spec}_{L^2}(\Delta_X)$, so $Z_X$ has a **simple zero at $s=1$**, which is divided out in forming $\det_0\Delta_X$. In infinite area $0$ is not an $L^2$ eigenvalue, $Z_X(1)\neq0$, and no derivative appears.

---

# Type card

> [!abstract] Type card — (BJP)
> **Given.** (P1).
>
> **Produces.** A closed-form identity: the renormalised determinant of $\Delta_X-s(1-s)$ equals $Z_X(s)$ times **explicit** elementary/Barnes factors depending only on $\chi$ and $n_C$.
>
> **Lets you.** Replace $\log Z_X(s)$ by a determinant, and — by [[Thm - Selberg Zeta Identity (Killing Case)|Cor 4.3]] — by a total loop mass. [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] is precisely (65) with that substitution.

---

# Status

- **Proved here:** no. (63) is quoted, and the integration is not carried out.
- **Source:** Borthwick–Judge–Perry, *Determinants of Laplacians and isopolar metrics on surfaces of infinite area*; see also Borthwick's book.
- **DAG node that would close this:** 🔵 *Spectral Geometry* + 🔵 *Automorphic Forms / Selberg Trace Formula*, plus the microlocal analysis of [[Ext - Melrose Renormalised Trace Expansion|(M)]]. **A genuine gap** — the deepest of §5.2.
- **What is safe to assume:** (64),(65),(66) and (F3), including the values of $M$, $F$, $C_X$ and the form of $G_\infty$. Theorem 5.7 manipulates (65) algebraically and takes one limit; it never reopens (63).
- **Scope:** §5.2.1 and Theorem 5.7. Also referenced in Remark 5.8 for the infinite-area case, where the identity holds directly at $s=1$.

> [!warning] The Barnes $G$ factor is where the "$-\mathrm{Area}(X)E$" of §5.1 went
> $G_\infty(s)^{\chi}$ and $e^{M}$ carry the local, contractible contribution — the same role as $\mathrm{Area}(X)E$ in (46),(49). By Gauss–Bonnet $\mathrm{Area}(X)=-2\pi\chi$, so both are "$\chi$ times a universal constant"; the packaging differs because the two sections regularise differently.

---

# Used at

- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)]] — the sole consumer, via (65)
- [[Def - Renormalised Integral and the 0-Trace]] — $\det_0$ is its subject
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.2.1

---

# Commentary

> [!note]- Commentary (skippable)
> (BJP) is the finite-area analogue of what Naud's formula does in §5.1, and it is instructive to line them up. Both express a determinant as (a local, $\chi$-dependent universal piece) $+$ ($\log$ of the Selberg zeta). §5.1 arrives there through the trace formula and a length-spectrum truncation; §5.2 arrives there through the resolvent and a b-calculus regularisation. The answers have the same shape because $Z_X$ is doing the same job in both: it is the spectral determinant's global factor.
>
> The one structural remark worth keeping is (F3). The appearance of $Z_X'(1)$ rather than $Z_X(1)$ in the finite-area case is not a technicality — it is the same phenomenon that made the total Brownian loop mass diverge in [[Thm - Finiteness of the Total Mass|Corollary 4.7]] when $\delta=1$. Finite area $\Rightarrow$ constants in $L^2$ $\Rightarrow$ $\lambda_0=0$ $\Rightarrow$ simple zero of $Z_X$ at $s=1$ $\Rightarrow$ $-\log Z_X(s)\to\infty$ as $s\downarrow1$. Three sections of the paper meet at that one zero.
