---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, zeta-functions, spectral-theory]
---

# Signature

| symbol | type |
|---|---|
| $Z_X$ | $\{\mathrm{Re}(s)>\delta\}\to\mathbb{C}$, defined by the Euler product (31) |
| $L_X(\cdot,\chi)$ | the [[Def - Selberg L-Function\|Selberg L-function]] for a unitary character $\chi$ |
| $R_X$ | the [[Def - Ruelle Zeta Function and its Twist\|Ruelle zeta]]; $R_X(s)=Z_X(s)/Z_X(s+1)$ |
| $\lambda_j$ | eigenvalues of $\Delta_X$; $s_j=\tfrac12\pm\sqrt{\tfrac14-\lambda_j}$ |

---

# Statement

> **(MC) Meromorphic continuation.** *Precondition:*
> **(P1)** $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite;
> **(P2)** $Z_X$ defined by the absolutely convergent product (31) on $\{\mathrm{Re}(s)>\delta\}$.
>
> *Conclusion:* $Z_X$ extends to a meromorphic function on all of $\mathbb{C}$. The same holds for $L_X(\cdot,\chi)$ ($\chi$ unitary) and, by $R_X(s)=Z_X(s)/Z_X(s+1)$, for $R_X$.

> **(F1) Zeros and the spectrum (closed $X$).** $Z_X$ is **entire** and its non-trivial zeros are at $s_j=\tfrac12\pm\sqrt{\tfrac14-\lambda_j}$, one pair per Laplace eigenvalue $\lambda_j$, with matching multiplicity. In particular $s=1$ is a simple zero (from $\lambda_0=0$).
>
> **(F2) Where the paper needs it.** Only to make sense of $Z_X(s)$, $L_X(s,\chi)$, and $\log\det$ expressions **outside** the region of absolute convergence, and to legitimise the derivative $Z_X'/Z_X$. Every identity of §4 is proved inside $\{\mathrm{Re}(s)>\delta\}$ by term-by-term matching and needs no continuation.

> [!warning] Continuation is never used to prove an identity here
> §4's identities are equalities of absolutely convergent series. (MC) is used only for *interpretation* — e.g. reading §5's $\log\det\Delta_X$ through $Z_X'(1)$ — and once in §6.1, where $\partial_s\log Z_X(s)$ is differentiated inside the convergence region anyway.

---

# Type card

> [!abstract] Type card — (MC)
> **Given.** (P1),(P2).
>
> **Produces.** A meromorphic function on $\mathbb{C}$ agreeing with the Euler product on $\{\mathrm{Re}(s)>\delta\}$; for closed $X$, entire, with zero set given by (F1).
>
> **Lets you.** Evaluate and differentiate $Z_X$ at points the product does not reach — notably $s=1$ on a closed surface, where the product diverges but the continued function has a simple zero. This is what makes [[Ext - Naud's Formula for the Log-Determinant|(N)]] and §5 meaningful.

---

# Status

- **Proved here:** no.
- **Source:** Selberg (finite area, via the trace formula); Patterson–Perry, Guillopé–Zworski, Borthwick (geometrically finite / infinite area).
- **DAG node that would close this:** 🔵 *Automorphic Forms / Selberg Trace Formula* (non-anchor), together with 🔵 *Spectral Geometry*. **A genuine gap**, shared with [[Ext - Prime Geodesic Theorem]] — both are trace-formula consequences.
- **What is safe to assume:** (MC) and (F1). Nothing in §4 depends on the proof, and (F1) is used only in §5.
- **Scope:** Definition 4.1 (F3), Definition 4.5 (F2), and §5–§6 wherever $Z_X$ is evaluated or differentiated.

---

# Used at

- [[Def - Selberg Zeta Function]] — (F3) there
- [[Def - Ruelle Zeta Function and its Twist]] — continuation of $R_X$ via (37)
- [[Def - Selberg L-Function]] — the twisted case
- [[Ext - Naud's Formula for the Log-Determinant]] — needs $Z_X'(1)$
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]]

---

# Commentary

> [!note]- Commentary (skippable)
> Worth being clear about how little §4 owes this import. The Selberg zeta identity (35) is proved by expanding two products and comparing summands, entirely inside the half-plane where both converge absolutely. If (MC) were false, §4 would survive unchanged.
>
> Where it bites is §5. There the object of interest is $\log\det\Delta_X$ on a **closed** surface, where $\delta=1$ and the Euler product diverges exactly at the point $s=1$ one wants to evaluate. The continued $Z_X$ has a simple zero there, coming from $\lambda_0=0$, and the finite quantity that survives is $Z_X'(1)$ — which is precisely what appears in Naud's formula. So the divergence of the total Brownian loop mass on a closed surface, and the vanishing of $Z_X$ at $s=1$, are the same phenomenon; (MC) is what lets one extract a finite number from it.
