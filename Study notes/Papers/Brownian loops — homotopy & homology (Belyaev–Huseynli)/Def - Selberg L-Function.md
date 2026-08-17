---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Selberg Zeta Function"
  - "Def - Character Torus and the Pontryagin Dual"
tags: [paper, zeta-functions, harmonic-analysis]
---

# Signature

| symbol | type |
|---|---|
| $\chi$ | $H_1(X,\mathbb{Z})\to S^1$, a **unitary** character |
| $[\gamma]$ | image of $\gamma\in\mathcal{P}_X$ in $H_1(X,\mathbb{Z})$ |
| $L_X(\cdot,\chi)$ | $\{\mathrm{Re}(s)>\delta\}\to\mathbb{C}$, continued meromorphically to $\mathbb{C}$ |
| $\delta$ | the critical exponent — **the same abscissa as for $Z_X$**, because $\lvert\chi\rvert\equiv1$ |

---

# Definition

> **Definition 6.3 (Selberg $L$-function).**
> $$L_X(s,\chi):=\prod_{\gamma\in\mathcal{P}_X}\prod_{k=0}^{\infty}\Big(1-\chi([\gamma])\,e^{-(s+k)\ell_\gamma}\Big),\qquad\mathrm{Re}(s)>\delta.\tag{75}$$
> The **double** Euler product of [[Def - Selberg Zeta Function|(31)]], twisted by $\chi$.

> **(F1) Trivial character.** $\chi\equiv1\Rightarrow L_X(s,\chi)=Z_X(s)$.
>
> **(F2) Same convergence region.** $\lvert\chi([\gamma])e^{-(s+k)\ell_\gamma}\rvert=e^{-(\mathrm{Re}(s)+k)\ell_\gamma}<1$, so (75) converges absolutely exactly where (31) does. **Unitarity is what makes the abscissa $\delta$ rather than something larger** — contrast [[Def - Ruelle Zeta Function and its Twist|$c_\rho$]].
>
> **(F3) It is a one-dimensional twisted Selberg zeta.** $\chi$ is a one-dimensional abelian representation of $\Gamma$ factoring through $H_1(X,\mathbb{Z})$; $L_X(\cdot,\chi)$ is the corresponding twisted Selberg zeta, and admits a meromorphic continuation to $\mathbb{C}$ by [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions|(MC)]].
>
> **(F4) Logarithmic expansion.** For $\mathrm{Re}(s)>\delta$, taking logarithms term by term with $-\log(1-z)=\sum_{m\geq1}z^m/m$ at $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$, and summing the inner geometric series $\sum_{k\geq0}e^{-(s+k)m\ell_\gamma}=\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$:
> $$-\log L_X(s,\chi)=\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\frac1m\cdot\frac{\chi([\gamma])^m\,e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.$$
> **This is [[Thm - Selberg L-Function Identity|Corollary 6.4]].**
>
> **(F5) The weight is a function of the homology class.** $\chi([\gamma])^m=\chi(m[\gamma])=\chi([\gamma^m])$, so the $(\gamma,m)$ summand of (F4) depends on the pair only through $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ and the homology class $m[\gamma]$. **This is what makes regrouping by homology legitimate.**

---

# Type card

> [!abstract] Type card — $L_X(\cdot,\chi)$
> **Given.** **(H1)** $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite. **(H2)** $\chi\in\widehat{H_1(X,\mathbb{Z})}$ unitary. **(H3)** $\mathrm{Re}(s)>\delta$.
>
> **Produces.** A number $L_X(s,\chi)\in\mathbb{C}^\times$; via (F4), the twisted total mass $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$.
>
> **Lets you.** Generate the homology-class masses: $\chi\mapsto-\log L_X(s,\chi)$ **is the Fourier transform** of $\beta\mapsto\mu^\kappa_X(\beta)$. Everything in §6.2–§6.3 is inversion applied to this one fact.

---

# Depends on

- [[Def - Selberg Zeta Function]] — the untwisted product, and (F1)
- [[Def - Character Torus and the Pontryagin Dual]] — $\chi$, and (F5)
- [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions]] — (F3)
- 🟢 $-\log(1-z)=\sum z^m/m$, geometric series — elementary

---

# Checks

**Instance.** $\chi\equiv1$: (75) is (31) and (F4) is (32). Corollary 6.4 degenerates to Corollary 4.3.

**Instance.** $\chi$ non-trivial on a closed genus-2 surface: $\lvert L_X(s,\chi)\rvert$ need not equal $\lvert Z_X(s)\rvert$, and the ratio $Z_X(s)/L_X(s,\chi)$ is exactly what appears in [[Thm - Distribution of the Total Homology of the Loop Soup|(80)]].

**Non-instance (fails H2's unitarity).** $\chi:H_1\to\mathbb{C}^\times$ with $\lvert\chi(e_1)\rvert=2$: then $\lvert\chi([\gamma])e^{-(s+k)\ell_\gamma}\rvert$ can exceed $1$ for short $\gamma$, the expansion in (F4) is invalid there, and the abscissa moves. **Consequence:** §6 is stated for unitary characters throughout, and the character torus — not the full character group — is the domain of integration.

**Non-instance (fails the Euler-product region).** $s=\delta$: (75) diverges just as (31) does. All of §6 assumes $\mathrm{Re}(s)>\delta$, which for $\kappa>0$ is automatic.

---

# Used at

- [[Thm - Selberg L-Function Identity]] — (F4) is its statement
- [[Thm - Fourier Expansion and Inversion by Homology Class]] — (F5) is what licenses the regrouping
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — $(Z_X/L_X)^\lambda$
- [[Constr - The Mass in a Homology Class]] — the object generated
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

---

# Commentary

> [!note]- Commentary (skippable)
> The analogy with Dirichlet $L$-functions is the paper's own and it is structurally exact. To count primes in an arithmetic progression one twists the Euler product by a character of $(\mathbb{Z}/q)^\times$ and inverts; to weigh geodesics by homology class one twists the Selberg Euler product by a character of $H_1(X,\mathbb{Z})$ and inverts. Primitive closed geodesics are the primes; $\ell_\gamma$ is $\log p$; $H_1(X,\mathbb{Z})$ is the group the "congruence class" lives in.
>
> The one design decision is unitarity. It is what keeps the abscissa at $\delta$, keeps every $\lvert z\rvert<1$ in the logarithmic expansion, and makes the dual group **compact** so Haar measure is finite and inversion is an integral rather than a limit. The twisted *Ruelle* zeta of §4.1.2 allowed general finite-dimensional $\rho$ and paid for it with a worse abscissa $c_\rho$ and — the paper says so plainly — identities that are hard to use. §6 restricts to the abelian unitary case and gets a clean Fourier theory.
