---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Random Variable"
  - "Def - Distribution Function"
  - "Def - Modes of Convergence"
tags: [probability, advanced-probability]
---

# Notation

$\mu_n,\mu$ probability measures on a metric space $(M,d)$ (usually $\mathbb{R}^d$); $C_b(M)$ — bounded continuous functions; $\mu_n\Rightarrow\mu$ — weak convergence; $X_n\xrightarrow{d}X$.

---

# Axiom Motivation

To compare random variables living on *different* probability spaces — as one must when forming a limit like the [[Thm - Central Limit Theorem|CLT]]'s Gaussian — one cannot subtract them. The only common ground is their *laws*, measures on $\mathbb{R}^d$. So one needs a notion of *convergence of measures*.

Convergence "$\mu_n(A)\to\mu(A)$ for every set $A$" is *too strong*: $\delta_{1/n}\not\to\delta_0$ in that sense ($\delta_{1/n}(\{0\})=0\not\to1$), yet morally $\delta_{1/n}$ *should* converge to $\delta_0$. The fix: test against *continuous* functions. $\int f\,d\delta_{1/n}=f(1/n)\to f(0)=\int f\,d\delta_0$ for every continuous $f$. **Weak convergence** declares $\mu_n\Rightarrow\mu$ when $\int f\,d\mu_n\to\int f\,d\mu$ for all bounded continuous $f$ — convergence tested against the "smooth observables," ignoring the behaviour on individual sets whose boundary the limit charges.

This is exactly the right notion: it is the convergence in the **Portmanteau theorem**'s several equivalent forms ($\liminf\mu_n(G)\ge\mu(G)$ for open $G$; $\mu_n(A)\to\mu(A)$ for *$\mu$-continuity* sets; $F_{X_n}(t)\to F_X(t)$ at continuity points of $F_X$). It is the convergence of the [[Thm - Central Limit Theorem|CLT]], of [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]], and the topology in which [[Thm - Prokhorov's Theorem|tight families are compact]]. The companion notion **tightness** — no mass escapes to infinity — is what makes weak limits exist.

---

# The Definition

Let $\mu_n,\mu$ be probability measures on a metric space $(M,d)$ with its Borel $\sigma$-algebra. The sequence **converges weakly** to $\mu$, written $\mu_n\Rightarrow\mu$, if
$$\int_M f\,d\mu_n\ \longrightarrow\ \int_M f\,d\mu\qquad\text{for every }f\in C_b(M).$$
Random variables **converge in distribution**, $X_n\xrightarrow{d}X$, if $\mu_{X_n}\Rightarrow\mu_X$.

**Portmanteau theorem (equivalences).** $\mu_n\Rightarrow\mu$ iff any of: $\liminf_n\mu_n(G)\ge\mu(G)$ for all open $G$; $\limsup_n\mu_n(C)\le\mu(C)$ for all closed $C$; $\mu_n(A)\to\mu(A)$ for all $A$ with $\mu(\partial A)=0$; and (on $\mathbb{R}$) $F_{X_n}(t)\to F_X(t)$ at every continuity point of $F_X$.

**Tightness.** A family $(\mu_n)$ is **tight** if for every $\varepsilon>0$ there is a compact $K$ with $\sup_n\mu_n(M\setminus K)\le\varepsilon$ — uniformly, no mass escapes to infinity.

---

# Relate to Other Fields / Compression

Weak convergence is the **weak-* convergence** of measures viewed as functionals on $C_b(M)$ — the same notion as weak-* convergence of a dual space, here $C_b(M)^*$. It is genuinely weaker than [[Measure Theory III — §3–4 Product Measures and Differentiation|total-variation]] convergence (which would forbid $\delta_{1/n}\Rightarrow\delta_0$). [[Thm - Prokhorov's Theorem|Tightness]] is the analogue of *uniform integrability* one dimension up — both prevent escape (of probability mass to infinity, resp. of expected mass to the tail) and both yield compactness. The [[Thm - Central Limit Theorem|CLT]] is a weak-convergence statement; [[Thm - Lévy's Continuity Theorem|characteristic functions]] metrise it.

---

# Examples / Corollaries

$\delta_{x_n}\Rightarrow\delta_x$ when $x_n\to x$. The empirical measure $\frac1n\sum_{k=1}^n\delta_{k/n}\Rightarrow$ uniform on $[0,1]$. $N(0,\sigma_n^2)\Rightarrow\delta_0$ as $\sigma_n\to0$. The [[Thm - Central Limit Theorem|CLT]]: $\frac{S_n-n\mu}{\sigma\sqrt n}\Rightarrow N(0,1)$.

**Not tight:** $\mu_n=\delta_n$ on $\mathbb{R}$ — mass escapes to $+\infty$; no weak limit exists (any limit would have to be the zero measure). Tightness is exactly what rules this out.

Calibration: (i) Does $\mu_n\Rightarrow\mu$ imply $\mu_n(A)\to\mu(A)$ for *all* Borel $A$? No — only for $\mu$-continuity sets ($\mu(\partial A)=0$). (ii) Is weak convergence metrisable? Yes (Lévy–Prokhorov metric, or via characteristic functions). (iii) Does $X_n\xrightarrow{d}X$ need them on one space? No.

---

# Unlocked by This

> [!tip] Prokhorov and Lévy
> [[Thm - Prokhorov's Theorem|Prokhorov's theorem]] — tightness $\Leftrightarrow$ relative weak compactness — is the compactness engine; [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]] reduces weak convergence to pointwise convergence of [[Def - Characteristic Function|characteristic functions]].

> [!tip] The central limit theorem
> The [[Thm - Central Limit Theorem|CLT]] is the statement that normalised sums converge *weakly* to the Gaussian.
