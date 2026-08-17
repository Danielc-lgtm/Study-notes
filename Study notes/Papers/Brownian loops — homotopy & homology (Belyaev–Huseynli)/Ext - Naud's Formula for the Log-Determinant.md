---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, spectral-theory, zeta-functions]
---

# Signature

| symbol | type |
|---|---|
| $X$ | **closed** hyperbolic surface |
| $S_X$ | the geometric term of [[Ext - Selberg Trace Formula (Heat Kernel Form)\|(STF)]] |
| $E$ | $=\dfrac{4\zeta_{\mathbb{R}}'(-1)-\tfrac12+\log(2\pi)}{4\pi}\approx0.0538$ — a **universal** constant |
| $\gamma_{\mathrm{EM}}$ | $\approx0.5772$, Euler–Mascheroni |
| $\mathrm{Area}(X)$ | $=4\pi(g-1)=-2\pi\chi(X)$ by Gauss–Bonnet |

---

# Statement

> **(N) Naud's length-spectrum formula for the determinant.** *Precondition:*
> **(P1)** $X$ closed hyperbolic;
> **(P2)** $S_X$ the geometric term of (44), with the asymptotics [[Ext - Selberg Trace Formula (Heat Kernel Form)|(F1)]];
> **(P3)** the refined prime geodesic theorem (43) — [[Ext - Prime Geodesic Theorem|(PGT$'$)]].
>
> *Conclusion:*
> $$-\log{\det}_\zeta\Delta_X=-\mathrm{Area}(X)\,E-\gamma_{\mathrm{EM}}+\int_0^1\frac{S_X(t)}{t}\,\mathrm{d}t+\int_1^\infty\frac{S_X(t)-1}{t}\,\mathrm{d}t.\tag{45}$$

> **(F1) Both integrals converge.** At $t\downarrow0$ because $S_X(t)$ is exponentially small; at $t\to\infty$ because $\lvert S_X(t)-1\rvert$ is exponentially small.
>
> **(F2) The split at $t=1$ is the regularisation.** (45) is *not* $\int_0^\infty S_X(t)\,\mathrm{d}t/t$ — that diverges at $t\to\infty$. Subtracting $1$ in the tail is the truncation, and it is the length-spectrum analogue of removing the zero eigenvalue.
>
> **(F3) Everything $X$-dependent is in $\mathrm{Area}(X)$ and $S_X$.** $E$ and $\gamma_{\mathrm{EM}}$ are universal.

---

# Type card

> [!abstract] Type card — (N)
> **Given.** (P1),(P2),(P3).
>
> **Produces.** An identity expressing $\log{\det}_\zeta\Delta_X$ **entirely through the length spectrum**: an area term, two universal constants, and two convergent integrals of $S_X$.
>
> **Lets you.** Replace the spectral definition of the determinant by a geodesic one, at which point [[Ext - Selberg Trace Formula (Heat Kernel Form)|(F2)]] identifies $\int S_X\,\mathrm{d}t/t$ with the total loop mass. Theorem 5.1 is (45) with that substitution made carefully.

---

# Status

- **Proved here:** no.
- **Source:** Naud; the derivation from the Selberg trace formula (44) plus the refined prime geodesic theorem (43). Also used in this exact form by Wang–Xue [WX25].
- **DAG node that would close this:** 🔵 *Automorphic Forms / Selberg Trace Formula* + 🔵 *Spectral Geometry*. **A genuine gap**, and the deepest single import of §5.
- **What is safe to assume:** (45) and (F1)–(F3), including the value of $E$. Theorem 5.1's proof does not open the derivation; it only splits and re-groups the two integrals.
- **Scope:** §5.1 only. Both parts of Theorem 5.1 start from (45); nothing else in the paper cites it.

> [!warning] The constant $E$ is not a normalisation you may drop
> $\mathrm{Area}(X)E$ is the renormalised **identity contribution** — the loops that are contractible. It is the whole cost of discarding the trivial class, and it survives into every formula of §5, including Polyakov's. Setting $E=0$ would change (49) into a false statement.

---

# Used at

- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — the sole consumer, both (i) and (ii)
- [[Thm - Polyakov's Formula via Brownian Loop Measure]] — through Theorem 5.1
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]]

---

# Commentary

> [!note]- Commentary (skippable)
> (45) is the pivot of §5, and its shape says exactly what the section is doing. On the left, a spectral object defined by analytic continuation of $\sum\lambda_j^{-s}$. On the right, an area term (the local, contractible contribution), two universal constants (the price of regularising), and two integrals over the length spectrum (the global, topological contribution). Theorem 5.1 does nothing but recognise the last piece as a loop mass.
>
> There is a choice hidden in (45) worth naming. §5 could have regularised by quadratic variation — that is the route taken for Riemann surfaces in the literature the paper cites — but instead follows Wang–Xue and truncates **according to the length spectrum**, which is why the answer comes out in terms of $N_X(R)-\widetilde{\mathrm{Li}}(e^R)$: the renormalisation subtracts the *expected* number of long geodesics predicted by (43), leaving the fluctuation. That makes the final formula (46) a statement about how the actual geodesic count deviates from its prime-geodesic-theorem prediction.
