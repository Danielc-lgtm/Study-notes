---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, harmonic-analysis]
---

# Signature

| symbol | type |
|---|---|
| $A$ | a discrete abelian group; here $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ |
| $\widehat A$ | its Pontryagin dual, compact; here $\cong(S^1)^r$ |
| $\mathrm{d}\chi$ | normalised Haar measure on $\widehat A$; $\int_{\widehat A}\mathrm{d}\chi=1$ |
| $\beta,\beta'$ | elements of $A$ |

---

# Statement

> **(OC) Orthogonality of characters.** *Precondition:* **(P1)** $A$ discrete abelian, $\widehat A$ its compact dual with normalised Haar measure. *Conclusion:*
> $$\int_{\widehat A}\chi(\beta')\,\overline{\chi(\beta)}\,\mathrm{d}\chi=\begin{cases}1,&\beta'=\beta,\\0,&\beta'\neq\beta.\end{cases}$$

> **(F1) Fourier inversion, the form used.** If $f:A\to\mathbb{C}$ satisfies $\sum_{\beta}\lvert f(\beta)\rvert<\infty$ and $\widehat f(\chi):=\sum_{\beta\in A}f(\beta)\chi(\beta)$, then
> $$f(\beta)=\int_{\widehat A}\widehat f(\chi)\,\overline{\chi(\beta)}\,\mathrm{d}\chi.$$
> Absolute convergence is what licenses exchanging $\sum_\beta$ with $\int_{\widehat A}$.
>
> **(F2) Concrete form for $A=\mathbb{Z}^r$.** $\widehat A=(\mathbb{R}/\mathbb{Z})^r$, $\chi_\theta(\beta)=e^{2\pi i\langle\theta,\beta\rangle}$, and (OC) is $\int_{[0,1)^r}e^{2\pi i\langle\theta,\beta'-\beta\rangle}\,\mathrm{d}\theta=\mathbb{1}[\beta'=\beta]$ — the orthogonality of the multi-dimensional Fourier basis.

---

# Type card

> [!abstract] Type card — (OC)
> **Given.** (P1); for (F1) additionally absolute summability of $f$.
>
> **Produces.** The orthogonality relation, hence Fourier inversion on $A$.
>
> **Lets you.** Isolate the coefficient of a **single** homology class $\beta$ from the generating function $-\log L_X(s,\chi)$, by multiplying by $\overline{\chi(\beta)}$ and integrating. Used twice: [[Thm - Fourier Expansion and Inversion by Homology Class|(78)]] and [[Thm - Distribution of the Total Homology of the Loop Soup|(81)]].

---

# Status

- **Proved here:** no.
- **Source:** standard Pontryagin duality; Rudin, *Fourier Analysis on Groups*; Folland, *A Course in Abstract Harmonic Analysis*.
- **DAG node that would close this:** 🟢 *Functional Analysis* (8,10) and 🟢 *Advanced Probability* (7,9) — Fourier inversion on $\mathbb{Z}^r$/$(S^1)^r$ is inside both. **Not a gap.**
- **What is safe to assume:** (OC),(F1),(F2). In practice only (F2) is needed — the group is always $\mathbb{Z}^r$ here.
- **Scope:** Theorem 6.5's inversion formula (78) and Proposition 6.7's (81).

> [!warning] Absolute convergence is a real hypothesis
> Exchanging $\sum_{\beta'}$ with $\int_{\widehat A}$ in the proof of (78) requires (F1)'s summability. It holds because $\sum_\beta\mu^\kappa_X(\beta)=\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))<\infty$ by [[Thm - Finiteness of the Total Mass|Cor 4.7]] — so $s>\delta$ is doing work here too, not only in §4.

---

# Used at

- [[Thm - Fourier Expansion and Inversion by Homology Class]] — the inversion (78)
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — the inversion (81)
- [[Def - Character Torus and the Pontryagin Dual]] — (F2) there
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

---

# Commentary

> [!note]- Commentary (skippable)
> A completely standard tool, listed here for one reason: it makes explicit that the "$L$-function" language of §6 is not an analogy but a Fourier transform. The homology-class masses $\{\mu^\kappa_X(\beta)\}_{\beta\in\mathbb{Z}^r}$ are the Fourier coefficients of the function $\chi\mapsto-\log L_X(s,\chi)$ on the torus, and everything §6.2–§6.3 proves about them is inversion plus the exponential formula.
>
> The parallel with Dirichlet characters is exact in structure and different in one respect worth noting: for primes in arithmetic progressions the character group is finite, so the inversion is a finite sum and one may ask for individual character values. Here the group is a torus, the inversion is an integral, and individual characters are not distinguished — which is why the results come out as integral formulas rather than as explicit counts.
