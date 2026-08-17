---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Selberg L-Function Identity"
  - "Constr - The Mass in a Homology Class"
  - "Def - Character Torus and the Pontryagin Dual"
tags: [paper, spectral-geometry, homology, harmonic-analysis]
---

# Notation

- $X=\Gamma\backslash\mathbb{H}^2$ — geometrically finite, with $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$; $r=2g+b-1$ for a non-compact surface of genus $g$ with $b\geq1$ ends, and $r=2g$ when $X$ is closed
- $\kappa\geq-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ satisfying $\operatorname{Re}(s)>\delta$
- $\chi\in\widehat{H_1(X,\mathbb{Z})}$ — a unitary character; $\mathrm{d}\chi$ the normalised Haar measure on the torus $\cong(S^1)^r$
- $L_X(s,\chi)$ — the [[Def - Selberg L-Function|Selberg L-function]]; $\mu^\kappa_X(\beta)$ the [[Constr - The Mass in a Homology Class|mass in a homology class]]
- $\mathrm{Jac}(X)$ — the [[Def - The Jacobian as a Principally Polarised Abelian Variety|Jacobian]], for the closed-case restatement

---

# Type card

> [!abstract] Type card — Theorem 6.5 (Fourier expansion and inversion by homology class)
> **Given.** A geometrically finite $X$ with $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$; $\kappa\geq-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ satisfying $\operatorname{Re}(s)>\delta$.
>
> **Produces.** Two identities. The **Fourier expansion** $-\log L_X(s,\chi)=\sum_{\beta}\chi(\beta)\mu^\kappa_X(\beta)$, absolutely convergent, valid for every unitary $\chi$. And the **inversion formula** $\mu^\kappa_X(\beta)=\int_{\widehat{H_1}}(-\log L_X(s,\chi))\overline{\chi(\beta)}\,\mathrm{d}\chi$, valid for each $\beta$.
>
> **Lets you.** Compute the mass in a **single homology class** — an infinite sum over free homotopy classes with no closed form — as **one integral over a compact $r$-dimensional torus**. This is the payoff of §6.2.

---

# Statement

> **Theorem 6.5 (Fourier expansion and inversion by homology class).** Let $X=\Gamma\backslash\mathbb{H}^2$ be a geometrically finite hyperbolic surface with $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$, where $r=2g+b-1$ for a non-compact surface of genus $g$ with $b\geq1$ ends and $r=2g$ when $X$ is closed. Let $\kappa\geq-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ satisfying $\operatorname{Re}(s)>\delta$. Then the logarithm of the Selberg $L$-function admits the absolutely convergent **Fourier expansion**
> $$-\log L_X(s,\chi) = \sum_{\beta\in H_1(X,\mathbb{Z})}\chi(\beta)\,\mu^\kappa_X(\beta)\tag{77}$$
> for every unitary character $\chi\in\widehat{H_1(X,\mathbb{Z})}$. Moreover, for each $\beta\in H_1(X,\mathbb{Z})$ one has the **inversion formula**
> $$\mu^\kappa_X(\beta) = \int_{\widehat{H_1(X,\mathbb{Z})}}\Big(-\log L_X(s,\chi)\Big)\,\overline{\chi(\beta)}\,\mathrm{d}\chi,\tag{78}$$
> where $\mathrm{d}\chi$ is the normalised Haar measure on $\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^r$.

> [!note] Remark 6.6 — the closed case, over the Jacobian
> When $X$ is closed, under $\widehat{H_1(X,\mathbb{Z})}\cong\mathrm{Jac}(X)$ the natural pairing is $\langle\beta,[\omega]\rangle=\int_\beta\omega\pmod{\mathbb{Z}}$, so (78) may equivalently be written as an integral over the Jacobian against $e^{-2\pi i\int_\beta\omega}$:
> $$\mu^\kappa_X(\beta) = \int_{\mathrm{Jac}(X)}\Big(-\log L_X\big(s,\chi_{[\omega]}\big)\Big)\,e^{-2\pi i\int_\beta\omega}\,\mathrm{d}[\omega],\tag{79}$$
> with $\mathrm{d}[\omega]$ the normalised Haar measure on the underlying real Jacobian torus. See [[Def - The Jacobian as a Principally Polarised Abelian Variety]].

---

# Why it is true

Fourier analysis on $\mathbb{Z}^r$, with the loop masses as the coefficients.

**The expansion.** [[Thm - Selberg L-Function Identity|Corollary 6.4]] gives $-\log L_X(s,\chi)$ as a double sum over $(\gamma,m)$ with weight $\chi([\gamma])^m$. The observation that makes everything work is that the weight depends only on the homology class of the iterate: whenever $m[\gamma]=\beta$,
$$\chi([\gamma])^m = \chi(m[\gamma]) = \chi(\beta).$$
So group the terms by the value of $m[\gamma]$. All terms in a group share the same weight $\chi(\beta)$, and their masses sum to $\mu^\kappa_X(\beta)$ by [[Constr - The Mass in a Homology Class|Definition 6.1]]. That is (77) — and it is literally a Fourier series on the group $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$, with $\mu^\kappa_X(\cdot)$ as the coefficient function and $-\log L_X(s,\cdot)$ as the transform on the dual torus.

**The inversion.** Standard: multiply by $\overline{\chi(\beta)}$, integrate over the torus, exchange sum and integral, and use orthogonality of characters, which annihilates every term but $\beta'=\beta$.

**The mechanism in one line: a character of $H_1$ cannot distinguish two homotopy classes with the same homology, so it acts as a constant on each homology group of terms — making $-\log L_X(s,\cdot)$ the Fourier transform of the homology masses, and Fourier inversion computes one mass.**

**Why this is worth doing.** The left side of (78) is an infinite sum over the homotopy classes lying above $\beta$, with no closed form. The right side is an integral over a **compact $r$-dimensional torus** of an explicitly-expanded function. So an infinite combinatorial sum has been traded for a finite-dimensional integral, and that is the whole content of §6.2.

**What makes the exchange legal.** Absolute convergence, which comes from positivity plus finiteness: the masses $\mu^\kappa_X(\beta)$ are non-negative and $\sum_\beta\mu^\kappa_X(\beta)=-\log Z_X(s)<\infty$ by [[Thm - Finiteness of the Total Mass|Corollary 4.7]]. Since $|\chi(\beta)|=1$, the series (77) converges absolutely and uniformly in $\chi$, so Fubini applies with no further care.

---

# Strategy

**Strategy.** Regroup the double sum of Corollary 6.4 by the value of $m[\gamma]$, using that $\chi([\gamma])^m=\chi(m[\gamma])$ depends only on the homology class; then multiply by $\overline{\chi(\beta)}$, exchange sum and integral by absolute convergence, and apply orthogonality of characters.

> [!note]- Proof (skippable)
> **The expansion.** Starting from (76), group together all terms for which the iterate $\gamma^m$ has the same homology class $\beta=m[\gamma]$. Since $\chi([\gamma])^m=\chi(m[\gamma])=\chi(\beta)$ for all such terms,
> $$-\log L_X(s,\chi) = \sum_{\beta\in H_1(X,\mathbb{Z})}\left(\sum_{\substack{\gamma\in\mathcal{P}_X,\ m\geq1\\ m[\gamma]=\beta}}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)\right)\chi(\beta) = \sum_{\beta}\mu^\kappa_X(\beta)\,\chi(\beta),$$
> by [[Constr - The Mass in a Homology Class|Definition 6.1]]. This is (77).
>
> **The inversion.** To recover the coefficient of a fixed $\beta$, multiply both sides of (77) by $\overline{\chi(\beta)}$ and integrate over the character torus. Since the Fourier series is absolutely convergent, the sum and the integral may be interchanged, giving
> $$\int_{\widehat{H_1(X,\mathbb{Z})}}\Big(-\log L_X(s,\chi)\Big)\overline{\chi(\beta)}\,\mathrm{d}\chi = \sum_{\beta'\in H_1(X,\mathbb{Z})}\mu^\kappa_X(\beta')\int_{\widehat{H_1(X,\mathbb{Z})}}\chi(\beta')\overline{\chi(\beta)}\,\mathrm{d}\chi.$$
> By orthogonality of characters on $\widehat{H_1(X,\mathbb{Z})}$, the inner integral is $1$ if $\beta'=\beta$ and $0$ otherwise. Therefore only the term $\beta'=\beta$ survives, giving (78). $\;\square$

---

# What this assumes, and where to climb

**Corollary 6.4** — [[Thm - Selberg L-Function Identity]], and through it [[Def - Selberg L-Function]], the killing mass formula, and unitarity of $\chi$.

**Definition 6.1** — [[Constr - The Mass in a Homology Class]], which is what the grouped sums are called.

**The character torus, Haar measure and orthogonality** — [[Def - Character Torus and the Pontryagin Dual]]. Orthogonality is the entire proof of the inversion half; **compactness of the torus is what makes $\mathrm{d}\chi$ a probability measure and the integral finite.**

**$H_1(X,\mathbb{Z})$ free of finite rank $r$** — geometric finiteness, via [[Def - Geometrically Finite Surfaces, Cusps and Funnels]]. If there were torsion the dual would not be a torus and the analysis would change; for a surface there is none.

**Absolute convergence**, from non-negativity of the masses plus [[Thm - Finiteness of the Total Mass|Corollary 4.7]]. This is the only analytic input, and it is what licenses the interchange.

**Note the hypothesis is $\kappa\geq-\tfrac14$, not $\kappa>0$.** The theorem holds on the whole extended range of Remark 3.7, subject only to $\operatorname{Re}(s)>\delta$.

---

# What consumes this

- [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] — the pointwise law $\mathbb{P}(\beta(\lambda)=\beta)$ is obtained by exactly the same multiply-and-integrate manoeuvre, applied to the characteristic function instead of to $-\log L_X$
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2 — the section's central result

---

# Reading it against the rest of the paper

The analogy the paper draws is with **Dirichlet $L$-functions and primes in arithmetic progressions**, and it is exact rather than decorative. There, one weights each prime by a character of $(\mathbb{Z}/q)^\times$, forms $L(s,\chi)$, and uses orthogonality to isolate a single residue class. Here, one weights each geodesic by a character of $H_1(X,\mathbb{Z})$, forms $L_X(s,\chi)$, and uses orthogonality to isolate a single homology class. The sorting problem is the same shape; only the group changes.

Compare also with §6.1, which handles a different sorting problem by a different method. There the classes are indexed by $(\gamma,m)$ and the quantity of interest is a function of $L$ alone, so the exponential-family structure gives every moment as a derivative. Here the classes are grouped by an abelian invariant, and the tool is Fourier duality on that abelian group. **Both sections take the same masses and extract different information by exploiting different structures on the index set** — one ordered by length, the other by a group.

Attribution, from Remark 6.2: Le Jan first defined a loop measure on homology classes; the authors developed theirs independently owing to differing conventions, and note that the $L$-function route is a **dual approach** which recovers Le Jan's results in greater generality, extending in particular to the non-compact case.
