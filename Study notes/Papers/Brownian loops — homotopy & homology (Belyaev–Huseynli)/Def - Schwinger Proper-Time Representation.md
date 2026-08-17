---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Transition Density and Heat Kernel"
  - "Constr - The Brownian Loop Measure"
tags: [paper, spectral-theory, quantum]
---

# Signature

| symbol | type |
|---|---|
| $\Delta_X$ | the **positive** Laplacian on $X$; spectrum $\subseteq[0,\infty)$ |
| $\kappa$ | $>0$ — killing rate; in field-theory language $\kappa=m^2$ |
| $e^{-t\Delta_X}$ | the heat semigroup; **trace class** when $X$ is closed |
| $\mathrm{Tr}$ | $\{$trace-class operators on $L^2(X)\}\to\mathbb{C}$ |
| $\det(\Delta_X+\kappa)$ | $\in(0,\infty)$ — the [[Def - Zeta-Regularised Determinant of the Laplacian\|zeta-regularised determinant]] |
| $\mu^\kappa_X$ | the killing loop measure; $\lvert\mu^\kappa_X\rvert_{\mathrm{reg}}$ its **regularised** total mass |

---

# Definition

> **Definition (Schwinger proper-time representation).** For $\kappa>0$,
> $$-\log\det(\Delta_X+\kappa)\;\;\text{“}=\text{”}\;\;\int_0^\infty\frac{\mathrm{d}t}{t}\,e^{-\kappa t}\,\mathrm{Tr}\big(e^{-t\Delta_X}\big).\tag{S}$$
> The variable $t$ is the **proper time**; the weight $\mathrm{d}t/t$ is the Haar measure of $(0,\infty)$ under multiplication.

> [!warning] (S) is divergent as written
> $\mathrm{Tr}(e^{-t\Delta_X})\sim\frac{\mathrm{vol}_g(X)}{4\pi t}$ as $t\downarrow0$ by [[Def - Transition Density and Heat Kernel|(F3)]], so the integrand is $\sim\frac{1}{t^2}$ and the integral **diverges at $t=0$**. The quotation marks are the paper's; §5 supplies the regularisation. Everything in §3.2 is formal at this point.

> **(D1) Trace as a heat-kernel integral.** When $e^{-t\Delta_X}$ is trace class,
> $$\mathrm{Tr}\big(e^{-t\Delta_X}\big)=\int_Xp(t,x,x)\,\mathrm{d}\mathrm{vol}_g(x).$$
>
> **(D2) Identification with the loop mass.** Substituting (D1) into (S) and comparing with $\mu^\kappa_X=\int_0^\infty\frac{\mathrm{d}t}{t}e^{-\kappa t}\int_XW^t_{x\to x}\,\mathrm{d}\mathrm{vol}_g(x)$ gives, term by term,
> $$-\log\det(\Delta_X+\kappa)=\big\lvert\mu^\kappa_X\big\rvert_{\mathrm{reg}},$$
> the regularised **total** mass of loops with killing — contractible and peripheral classes included.
>
> **(D3) Partition function.** $Z^\kappa_X\propto\det(\Delta_X+\kappa)^{-1/2}$, hence
> $$Z^\kappa_X\propto\exp\Big(\tfrac12\big\lvert\mu^\kappa_X\big\rvert_{\mathrm{reg}}\Big).$$
> The $\tfrac12$ is the exponent $\det^{-1/2}$ of a **single real** scalar field.

---

# Type card

> [!abstract] Type card — Schwinger proper-time
> **Given.** **(H1)** $X$ closed, so $e^{-t\Delta_X}$ trace class. **(H2)** $\kappa>0$. **(H3)** a regularisation of the $t\downarrow0$ divergence — supplied in §5, **not** here.
>
> **Produces.** An identity between a **spectral** quantity, $\log\det(\Delta_X+\kappa)$, and a **path** quantity, the total mass $\lvert\mu^\kappa_X\rvert_{\mathrm{reg}}$.
>
> **Lets you.** Read every mass computation of §3–§4 as a computation of a determinant. This is the motivation for §5, where (H3) is discharged and the identity becomes a theorem.

---

# Depends on

- [[Def - Transition Density and Heat Kernel]] — (D1), and the short-time asymptotic (F3) that causes the divergence
- [[Constr - The Brownian Loop Measure]] — the $\int_0^\infty\frac{\mathrm{d}t}{t}\int_XW^t_{x\to x}$ shape that (D2) matches
- [[Ext - Feynman–Kac Formula|(F1)]] — why the killing weight is exactly $e^{-\kappa t}$
- 🟢 trace-class operators, functional calculus — *Functional Analysis* (8,10)
- **Deferred:** the definition of $\det$, and the regularisation — [[Def - Zeta-Regularised Determinant of the Laplacian]], §5

---

# Checks

**Instance.** $X$ closed, $\mathrm{Spec}(\Delta_X)=\{\lambda_j\}$ with $\lambda_j\to\infty$. Formally $\int_0^\infty\frac{\mathrm{d}t}{t}e^{-\kappa t}\sum_je^{-t\lambda_j}=\sum_j\int_0^\infty\frac{\mathrm{d}t}{t}e^{-(\lambda_j+\kappa)t}$, and each term is a divergent $\int\mathrm{d}t/t$ whose *derivative in $\kappa$* is the convergent $-\sum_j(\lambda_j+\kappa)^{-1}=-\frac{\mathrm{d}}{\mathrm{d}\kappa}\sum_j\log(\lambda_j+\kappa)$. So (S) is right **up to a $\kappa$-independent divergence**, which is precisely what zeta regularisation removes.

**Non-instance (fails H1).** $X$ non-compact of finite area: $e^{-t\Delta_X}$ is **not** trace class — the continuous spectrum contributes and $\int_Xp(t,x,x)\,\mathrm{d}\mathrm{vol}_g=\infty$ is not the issue, the failure is that the resolvent trace diverges. **Consequence:** (D1) fails, and §5.2 must replace $\mathrm{Tr}$ by the [[Def - Renormalised Integral and the 0-Trace|0-trace]].

**Non-instance (fails H2).** $\kappa=0$ with $X$ closed: $\Delta_X$ has the constant eigenfunction, $\lambda_0=0$, so $\det\Delta_X=0$ and $-\log\det=\infty$. In (S) the $j=0$ term is $\int_0^\infty\mathrm{d}t/t$, divergent at **both** ends. The determinant must be taken over the orthogonal complement of the constants.

---

# Used at

- [[§3.2 Euclidean Quantum Mechanics and the Path Integral]] — stated as motivation
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — the rigorous version
- [[Def - Zeta-Regularised Determinant of the Laplacian]] — the regularisation of (S)

---

# Commentary

> [!note]- Commentary (skippable)
> The one thing to keep from §3.2: **$\frac{\mathrm{d}t}{t}$ is not an aesthetic choice.** In physics it is the proper-time weight in the Schwinger representation of a one-loop determinant; in probability it is the weight that makes the loop measure invariant under time-shift of the parametrisation ([[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure|(LJ)]]) and under scaling. The two subjects wrote down the same measure for different reasons, and every identity in §4–§5 is a consequence of that coincidence.
>
> The field-theoretic packaging: a free real scalar of mass $m$ on $X$ has Euclidean action $S_E[\varphi]=\tfrac12\langle\varphi,(\Delta_X+\kappa)\varphi\rangle$ with $\kappa=m^2$. Gaussian integration gives $Z^\kappa_X\propto\det(\Delta_X+\kappa)^{-1/2}$, and the one-loop effective action is $\Gamma^{(1)}_X(\kappa)=-\log Z^\kappa_X=\tfrac12\log\det(\Delta_X+\kappa)$. So (D3) says the partition function of the field is the exponential of half the total Brownian-loop mass. "One loop" is literal here: the loops are the loops.
