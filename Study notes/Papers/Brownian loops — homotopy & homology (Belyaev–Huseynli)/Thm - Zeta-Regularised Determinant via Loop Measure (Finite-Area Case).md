---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Ext - Borthwick–Judge–Perry Determinant Formula"
  - "Thm - Selberg Zeta Identity (Killing Case)"
  - "Def - Renormalised Integral and the 0-Trace"
tags: [paper, spectral-theory, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $X$ | geometrically finite hyperbolic surface of **finite area**; $n_C$ cusps, $\chi=\chi(X)$ |
| $\kappa$ | $\geq0$; $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$, so $s(s-1)=\kappa$ and $\Delta_X-s(1-s)=\Delta_X+\kappa$ |
| $M,F,D_X$ | as in [[Ext - Borthwick–Judge–Perry Determinant Formula\|(BJP)]]: $M=\chi(\tfrac12\log2\pi-2\zeta_{\mathbb{R}}'(-1)+\tfrac14)$, $F=-\chi$, $D_X$ from (66) |
| $C_X$ | $=e^{M}(2\pi)^{-\chi}(\sqrt{2\pi})^{-n_C}$; $D_X(1)=\log C_X-M$ |
| $\det_0$ | the [[Def - Renormalised Integral and the 0-Trace\|renormalised determinant]] |

> **Convention.** $s>1$ throughout, since $\delta=1$ in finite area and $\kappa\geq0$; the identification $s(1-s)=-\kappa$ is used repeatedly.

---

# Type card

> [!abstract] Type card — Theorem 5.7
> **Given.**
> **(H1)** $X$ geometrically finite, $\mathrm{Area}(X)<\infty$, $n_C$ cusps, Euler characteristic $\chi$.
> **(H2)** $\kappa\geq0$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$.
> **(H3)** [[Ext - Borthwick–Judge–Perry Determinant Formula|(BJP)]], in the form (65).
>
> **Produces.**
> $$-\log\det{}_0\big(\Delta_X+\kappa\big)=F\kappa-M+\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)-D_X(s),\tag{67}$$
> and, dividing out the simple zero and letting $\kappa\to0^+$,
> $$\log\det{}_0\Delta_X=M+D_X(1)+\log Z_X'(1)=\log C_X+\log Z_X'(1).\tag{68}$$
>
> **Lets you.** Extend §5.1's identification "determinant $=$ regularised total loop mass" from closed surfaces to **cusped finite-area** ones, with the cusp corrections isolated in the explicit function $D_X$.

---

# Statement

> **Theorem 5.7.** Assume (H1)–(H3). Then (67) holds. Defining
> $$\det{}_0\Delta_X:=\lim_{s\to1}\frac{\det_0\big(\Delta_X-s(1-s)\big)}{s(s-1)},$$
> the limit $\kappa\to0^+$ gives (68), where $D_X(1)=-\chi\log(2\pi)-n_C\log\sqrt{2\pi}$.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Ext - Borthwick–Judge–Perry Determinant Formula\|(65)]] | $s$ with $s(1-s)=-\kappa$ | $-\log\det_0(\Delta_X+\kappa)=F\kappa-M-\log Z_X(s)-D_X(s)$ |
| [[Thm - Selberg Zeta Identity (Killing Case)\|Cor 4.3]] | $-\log Z_X(s)$, valid since $s>1=\delta$ | $\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ — giving (67) |
| [[Ext - Borthwick–Judge–Perry Determinant Formula\|(F3)]] | $\mathrm{Area}(X)<\infty$ | $Z_X(s)=Z_X'(1)(s-1)+O((s-1)^2)$ |
| $s(s-1)=\kappa$, $s-1\sim\kappa$ as $\kappa\to0^+$ | the division | $-\log(s-1)$ cancels the divergence of $-\log Z_X(s)$ |
| $D_X(s)\to D_X(1)$, $F\kappa\to0$ | the limit | (68), using $D_X(1)=\log C_X-M$ |

---

# Proof

**Strategy.** (67) is (65) with $-\log Z_X(s)$ replaced by the total loop mass. For (68), the simple zero of $Z_X$ at $s=1$ produces a $-\log(s-1)$ which the division by $s(s-1)$ exactly cancels.

> [!note]- Proof (skippable)
> Substituting $-\log Z_X(s)=\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ into (65), and using $s(1-s)=-\kappa$, gives (67) directly.
>
> For the limit: $\mathrm{Area}(X)<\infty$ forces a simple zero, $Z_X(s)=Z_X'(1)(s-1)+O((s-1)^2)$, so
> $$-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1).$$
> Dividing $\det_0(\Delta_X-s(1-s))$ by $s(s-1)$ subtracts $\log\big(s(s-1)\big)$ from its logarithm; since $s(s-1)=\kappa$ and $s-1\sim\kappa$ as $\kappa\to0^+$, the resulting $-\log(s-1)$ cancels the divergence in $-\log Z_X(s)$. Together with $F\kappa\to0$, $D_X(s)\to D_X(1)$ and $D_X(1)=\log C_X-M$, this yields (68). $\;\square$

---

# What this assumes, and where to climb

- **(BJP)** — [[Ext - Borthwick–Judge–Perry Determinant Formula]], itself resting on [[Ext - Melrose Renormalised Trace Expansion|(M)]]. **The gap of §5.2**; nothing in the theorem's own argument is unproved.
- **$s>1$ strictly**, hence $\kappa\geq0$ with the limit taken from above. At $\kappa=0$ exactly, Corollary 4.3's sum diverges — which is the divergence being cancelled, not a hypothesis violation.
- **The simple zero** — [[Def - Eisenstein Series and the Continuous Spectrum|(F2)]]: finite area $\Rightarrow$ constants in $L^2$ $\Rightarrow$ $\lambda_0=0$ $\Rightarrow$ simple zero of $Z_X$ at $s=1$.
- **Infinite area (Remark 5.8).** $\delta<1$, so the total mass is already finite by [[Thm - Finiteness of the Total Mass|Cor 4.7]] and the identity holds **directly at $s=1$**, with $Z_X(1)\neq0$ and no derivative. The corresponding statement via the resonance divisor is in Lemonde–Wang [LW26].

---

# Consumed by

- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.2
- [[Constr - The Probability Measure on Free Homotopy Classes]] — the "$\kappa=0$ case using the expressions from §5" remark
- Nothing in §6–§7 uses (67) or (68) computationally.

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: (65) says $-\log\det_0=-\log Z_X+\text{explicit}$, Corollary 4.3 says $-\log Z_X=\text{total loop mass}$, and the theorem is the composition.** The only real work is the $\kappa\to0^+$ limit, and it is the same cancellation as in [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(ii)]]: a $\log\kappa$ from the divergence of the total mass against a $\log\kappa$ from dividing out the zero.
>
> Comparing (68) with the closed-surface result (49) is the right way to see what the cusps cost. Closed: $\log{\det}_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1)$. Finite area with cusps: $\log\det_0\Delta_X=\log C_X+\log Z_X'(1)$, where $C_X=e^M(2\pi)^{-\chi}(\sqrt{2\pi})^{-n_C}$. Same global factor $Z_X'(1)$; the local factor changes from "area times a universal constant" to "Euler characteristic and cusp count times universal constants" — which, given $\mathrm{Area}(X)=-2\pi\chi$, differ only in how the cusps are accounted.
>
> The theorem is also the paper's cleanest demonstration that the loop-measure language is doing genuine work rather than translating. Corollary 4.3 was proved by elementary series manipulation in §4; here it is the *input* to a statement about renormalised determinants on non-compact surfaces, a setting where the heat semigroup is not even trace class.
