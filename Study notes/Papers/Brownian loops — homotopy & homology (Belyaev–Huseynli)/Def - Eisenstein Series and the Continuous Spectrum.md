---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Geometrically Finite Surfaces, Cusps and Funnels"
  - "Def - Self-Adjoint Operator"
tags: [paper, spectral-geometry, automorphic-forms]
---

# Notation

- $X$ — a geometrically finite hyperbolic surface of **finite area** with $n_C$ cusps
- $\Delta_X$ — the positive Laplace–Beltrami operator; $\lambda_0=0$ its smallest $L^2$ eigenvalue
- $E_j(z,s)$ — the Eisenstein series attached to the $j$-th cusp, $j=1,\dots,n_C$
- $s$ — the spectral parameter, with $\Delta_X E_j = s(1-s)E_j$
- $P$ — the orthogonal projection onto the $L^2$ null space of $\Delta_X$

---

# In plain language

On a **closed** hyperbolic surface the Laplacian has purely discrete spectrum: a sequence of eigenvalues $0=\lambda_0<\lambda_1\leq\cdots$ marching off to infinity, each with an honest $L^2$ eigenfunction. Everything in §5.1 rests on that.

On a **cusped** finite-area surface it fails. Alongside the $L^2$ eigenvalues starting at $\lambda_0=0$ there is now a **continuous spectrum filling $[\tfrac14,\infty)$**, with multiplicity equal to the number of cusps. Its generalised eigenfunctions are the **Eisenstein series** $E_j(z,s)$, one per cusp: they solve the eigenvalue equation $\Delta_X E_j=s(1-s)E_j$ but **do not lie in $L^2$** — they do not decay in the cusps, so they are not square-integrable and are not eigenfunctions in the operator-theoretic sense.

Two consequences, and both break §5.1 outright. There is no longer a discrete sequence of eigenvalues to feed into $\sum_j\lambda_j^{-s}$, so the spectral zeta function has no definition. And the heat semigroup $e^{-t\Delta_X}$ is **not trace class**, so $\operatorname{Tr}(e^{-t\Delta_X})=\int_X p(t,z,z)\,\mathrm{d}\mathrm{vol}$ diverges — the diagonal does not decay fast enough in the cusps. Since the whole of §5.1 runs through the Mellin transform of the heat trace, none of it parses.

**The number $\tfrac14$ is the same $\tfrac14$ as everywhere else in the paper.** It is the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$, it appears as $e^{-s/4}$ in [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]], it is inside the square root in $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, and it bounds the range $\kappa\geq-\tfrac14$. Here it appears as the bottom of the continuous spectrum, which is the same statement about $\mathbb{H}^2$ seen through the quotient.

---

# The definition

> **The spectral decomposition on a cusped finite-area surface.** Let $X$ be a geometrically finite hyperbolic surface of finite area with $n_C$ cusps. Then the spectrum of $\Delta_X$ consists of:
>
> - a set of **$L^2$ eigenvalues** starting at $\lambda_0=0$, with genuine square-integrable eigenfunctions; and
> - a **continuous spectrum** filling $[\tfrac14,\infty)$, with multiplicity equal to $n_C$.

> **Definition (Eisenstein series).** The generalised eigenfunctions of the continuous spectrum are the **Eisenstein series** $E_j(z,s)$, one for each cusp $j=1,\dots,n_C$, which solve
> $$\Delta_X E_j(\cdot,s) = s(1-s)\,E_j(\cdot,s)$$
> but do **not** lie in $L^2(X)$.

> **Consequences.** There is no longer a discrete sequence of eigenvalues to feed into $\sum_j\lambda_j^{-s}$, and the heat semigroup $e^{-t\Delta_X}$ is no longer trace class. The determinant of the Laplacian must therefore be constructed in a different way — see [[Def - Renormalised Integral and the 0-Trace]].

---

# Types and signatures

- $E_j : X\times\{s\in\mathbb{C}\}\to\mathbb{C}$ — smooth in $z$, meromorphic in $s$; **not** in $L^2(X)$
- $s(1-s)$ — the eigenvalue parameter; the continuous spectrum $[\tfrac14,\infty)$ corresponds to $s\in\tfrac12+i\mathbb{R}$, where $s(1-s)=\tfrac14+r^2$ for $s=\tfrac12+ir$
- multiplicity $n_C$ — the number of independent generalised eigenfunctions at each point of the continuous spectrum, one per cusp
- $P$ — the projection onto the $L^2$ null space; finite rank, and in the finite-area case rank $1$ (the constants)
- $e^{-t\Delta_X}$ — bounded, self-adjoint, but **not** trace class when $n_C\geq1$

---

# Example

The modular surface $\mathrm{PSL}(2,\mathbb{Z})\backslash\mathbb{H}^2$, or any once-punctured hyperbolic surface: $n_C=1$, so the continuous spectrum $[\tfrac14,\infty)$ has multiplicity $1$, with a single Eisenstein series $E_1(z,s)$. The $L^2$ eigenfunctions below $\tfrac14$ are finitely many; the discrete eigenvalues above $\tfrac14$ — the Maass cusp forms — are embedded in the continuous spectrum. $\lambda_0=0$ is simple with constant eigenfunction, so $P$ has rank $1$.

**Near-miss non-example — a funnel is not a cusp.** An infinite-area surface with funnels also has continuous spectrum, but the situation differs in an important way: there $\delta<1$ and $0$ is **not** an $L^2$ eigenvalue, so $Z_X(1)\neq0$ and no derivative is needed in the determinant formula. This is exactly the dichotomy in [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]]: $\det_0\Delta_X=C_XZ'_X(1)$ when $\mathrm{Area}(X)<\infty$, and $C_XZ_X(1)$ when $\mathrm{Area}(X)=\infty$. **The presence or absence of $\lambda_0=0$ in the $L^2$ spectrum is what decides between $Z'_X$ and $Z_X$**, and Remark 5.6 says so explicitly.

**Second near-miss — a closed surface.** No ends, no continuous spectrum, $e^{-t\Delta_X}$ trace class, and the $0$-trace of §5.2 reduces to the ordinary trace with $\det_0=\det_\zeta$. §5.2 contains §5.1 as a special case, at the cost of considerably more machinery.

---

# Used in this paper at

- [[Def - Renormalised Integral and the 0-Trace]] — the construction built to replace the trace that this page shows does not exist
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] — the finite-area determinant formula, which exists only because of that replacement
- [[Thm - Borthwick–Judge–Perry Determinant Formula|Theorem 5.5]] — $n_C$ appears explicitly in the factorisation
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.2 — where the breakdown and the repair are set out
- [[Def - Geometrically Finite Surfaces, Cusps and Funnels]] — the cusp/funnel distinction that decides which regime one is in

---

# Where this sits in my DAG

The operator-theoretic content — discrete versus continuous spectrum, generalised eigenfunctions, trace-class operators — is *Functional Analysis* (🟢); see [[Def - Self-Adjoint Operator]] and [[Thm - Complex Spectral Theorem]].

The **specific spectral decomposition of $\Delta_X$ on a cusped surface**, and the existence and meromorphic continuation of the Eisenstein series, are quoted. Their home node is *Automorphic Forms / Selberg Trace Formula* (🔵), whose description names exactly this: "on the modular surface the spectrum splits into cusp forms (Maass forms — non-holomorphic Laplace eigenfunctions, the discrete spectrum) and Eisenstein series (the continuous spectrum, whose meromorphic continuation is Langlands' first theorem)". So this page and the Selberg-trace-formula gap on [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes]] close together, with Iwaniec or Bergeron as the reference.

Nothing in the paper uses the Eisenstein series *computationally* — they are named to explain why the §5.1 construction fails, and the repair (Melrose's renormalised trace) proceeds without them.
