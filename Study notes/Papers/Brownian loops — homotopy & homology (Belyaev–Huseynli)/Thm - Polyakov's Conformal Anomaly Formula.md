---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Thm - Gauss-Bonnet Theorem for Surfaces"
tags: [paper, spectral-geometry, determinants, conformal-geometry]
---

# Notation

- $X$ — a closed surface; $g_0$ and $g=e^{2\sigma}g_0$ conformally equivalent smooth metrics, $\sigma\in C^\infty(X,\mathbb{R})$
- $K_0$ — the Gauss curvature of $g_0$; $\mathrm{vol}_{g}(X)$ the total area in the metric $g$
- $g_{\mathrm{hyp}}$ — the unique hyperbolic representative in the conformal class; $\mathrm{d}A_{\mathrm{hyp}}$ its area element
- $P_X(\sigma)$ — the Polyakov correction relative to $g_{\mathrm{hyp}}$
- $g$ — the genus (an unfortunate collision with the metric $g$; the paper uses both, and context disambiguates)
- $\det_\zeta\Delta_g$ — the [[Def - Zeta-Regularised Determinant of the Laplacian|zeta-regularised determinant]] of the Laplacian of the metric $g$

---

# Type card

> [!abstract] Type card — Theorem 5.3 (Polyakov's conformal anomaly formula)
> **Given.** Conformally equivalent smooth metrics $g_0$ and $g=e^{2\sigma}g_0$ on a closed surface $X$, with $K_0$ the Gauss curvature of $g_0$.
>
> **Produces.** An explicit transformation law for $\log\det_\zeta\Delta_X$ under the rescaling: the difference of the two log-determinants is a **local** functional of $\sigma$ — a Dirichlet energy plus a curvature coupling — plus a global volume ratio.
>
> **Lets you.** Move between any two metrics in a conformal class without recomputing a determinant; hence, combined with [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]], obtain $\log\det_\zeta\Delta$ for **every** metric in the conformal class from its value at the hyperbolic representative.

---

# Statement

> **Theorem 5.3 (Polyakov's conformal anomaly formula).** Let $g_0$ and $g=e^{2\sigma}g_0$ be conformally equivalent smooth metrics on a closed surface $X$, with $K_0$ the Gauss curvature of $g_0$. Then
> $$\log\det{}_\zeta\Delta_X = -\frac{1}{12\pi}\int_X|\nabla_{g_0}\sigma|^2\,\mathrm{d}\mathrm{vol}_{g_0} - \frac{1}{6\pi}\int_X K_0\,\sigma\,\mathrm{d}\mathrm{vol}_{g_0} + \log\frac{\mathrm{vol}_g(X)}{\mathrm{vol}_{g_0}(X)} + \log\det{}_\zeta\Delta_{g_0}.\tag{56}$$

> **Specialisation to the hyperbolic representative.** Take $g_0=g_{\mathrm{hyp}}$, the unique hyperbolic representative in the conformal class of $X$, so $K_0\equiv-1$ and, by Gauss–Bonnet, $\mathrm{vol}_{g_0}(X)=\mathrm{Area}(X)=4\pi(g-1)$. The curvature coupling reduces to $+\frac{1}{6\pi}\int_X\sigma\,\mathrm{d}A_{\mathrm{hyp}}$, and writing
> $$P_X(\sigma) := -\frac{1}{12\pi}\int_X|\nabla\sigma|^2\,\mathrm{d}A_{\mathrm{hyp}} + \frac{1}{6\pi}\int_X\sigma\,\mathrm{d}A_{\mathrm{hyp}} + \log\frac{\mathrm{vol}_g(X)}{4\pi(g-1)}$$
> for the **Polyakov correction** relative to $g_{\mathrm{hyp}}$, one has
> $$\log\det{}_\zeta\Delta_g = P_X(\sigma) + \log\det{}_\zeta\Delta_{g_{\mathrm{hyp}}}.$$

The paper quotes this theorem rather than proving it.

---

# Why it is true

The name "anomaly" is the explanation. Classically, in two dimensions, the Laplacian is conformally covariant: $\Delta_{e^{2\sigma}g}=e^{-2\sigma}\Delta_g$. So the *spectrum* rescales in a controlled way and one might hope the determinant does too — that the log-determinant would be conformally invariant up to something trivial. It is not, and the failure is the anomaly.

The reason the failure is *local* — an integral of $|\nabla\sigma|^2$ and of $K_0\sigma$, rather than something depending on the global geometry — is the structure of the short-time heat-trace expansion. The zeta-regularised determinant is defined through $\zeta'_X(0)$, and $\zeta_X$ near $s=0$ is controlled by the small-$t$ asymptotics of $\operatorname{Tr}(e^{-t\Delta})$, whose coefficients are integrals of **local** curvature invariants. Differentiating the determinant along a conformal family therefore produces a local expression, and in two dimensions the only available local invariants of the right weight are $|\nabla\sigma|^2$ and $K_0\sigma$. The coefficients $-1/12\pi$ and $-1/6\pi$ are fixed by the heat coefficients.

**The mechanism in one line: $\log\det_\zeta$ is $\zeta'(0)$, $\zeta$ near $0$ is governed by the local heat coefficients, so the conformal variation of the log-determinant is an integral of local curvature quantities — and in two dimensions there are only two of them.**

The volume ratio $\log(\mathrm{vol}_g(X)/\mathrm{vol}_{g_0}(X))$ is the one non-local term, and it is there for a bookkeeping reason: $\det_\zeta$ excludes the zero eigenvalue, whose eigenfunction is the constant, and normalising that constant depends on the total volume.

**Why this matters here.** Theorem 5.1 computes $\log\det_\zeta\Delta$ at the *hyperbolic* representative of each conformal class. Polyakov's formula supplies the transformation law within the class. The two together cover every metric on $X$, which is what [[Thm - Polyakov's Formula via Brownian Loop Measure|Corollary 5.4]] states.

---

# Strategy

**Strategy.** Differentiate $\log\det_\zeta\Delta_{e^{2u\sigma}g_0}$ in the parameter $u$, express the derivative through $\zeta'(0)$ of the varied operator, and use the local heat-coefficient expansion to identify it with the local functional; then integrate in $u$ from $0$ to $1$.

> [!note]- Proof (skippable)
> Not reproduced in the paper, which cites the standard references. The variational argument sketched in the strategy is the classical one: the conformal variation of $\zeta_X(s)$ at $s=0$ is computed from the $t^0$ heat coefficient, which in two dimensions is $\frac{1}{4\pi}\int_X\big(\frac{K}{3}\big)\,\mathrm{d}\mathrm{vol}$ up to the null-space contribution, and integrating the resulting first-order ODE in the conformal parameter produces (56). Polyakov's original derivation was in the context of the quantum geometry of bosonic strings, where the anomaly is what obstructs conformal invariance of the string path integral away from the critical dimension.

---

# What this assumes, and where to climb

**The zeta-regularised determinant and its heat-kernel definition** — [[Def - Zeta-Regularised Determinant of the Laplacian]]. In particular the fact that $\zeta_X$ is regular at $0$ and that its behaviour there is governed by the local heat coefficients.

**Conformal covariance of the Laplacian in two dimensions**, $\Delta_{e^{2\sigma}g}=e^{-2\sigma}\Delta_g$ — an anchor via the Riemannian-geometry strand, and the same identity whose *failure* under $\phi$ kills [[Thm - Length-Spectrum Identity under Puncturing|Theorem 3.9]] for subordinate processes. That the identity is special to dimension two is why the formula is a two-dimensional one.

**Gauss–Bonnet** — [[Thm - Gauss-Bonnet Theorem for Surfaces]], used in the specialisation to give $\mathrm{Area}(X)=4\pi(g-1)$ for a closed hyperbolic surface of genus $g$; equivalently $\mathrm{Area}(X)=-2\pi\chi(X)$.

**Closedness of $X$.** The formula as stated is for closed surfaces. The paper notes that a Polyakov conformal anomaly formula for non-compact surfaces exists in the literature but does not use it.

**The theorem itself is quoted.** It is not on the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|recorded gaps]] list because it is classical and its statement is fully explicit here; nothing downstream needs its proof, only its formula.

---

# What consumes this

- [[Thm - Polyakov's Formula via Brownian Loop Measure|Corollary 5.4]] — the sole consumer, combining this transformation law with Theorem 5.1's value at $g_{\mathrm{hyp}}$
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.1.1

---

# Reading it against the rest of the paper

Polyakov's formula and [[Constr - The Brownian Loop Measure|conformal invariance of the Brownian loop measure]] fit together in a way worth naming. The loop-measure terms in Theorem 5.1 are conformally invariant — that is exactly what §2.1's second structural property says — so they do not move when $g_{\mathrm{hyp}}$ is rescaled to $g$. **All the metric dependence of $\log\det_\zeta\Delta_g$ therefore collects into $P_X(\sigma)$, and the probabilistic content is untouched.** That is the observation making Corollary 5.4 immediate.

This is also the second and last place in the paper where conformal invariance is spent; the first was §3.4. Both times the mechanism is identical: an object built from $\mu_X$ is conformally invariant, so a conformal change moves only the explicitly computable remainder. Read the two together to see what the property is worth — and remember that for any nonlinear subordination it is unavailable, which is why §5.1.1 has no $\alpha$-stable analogue.

Historically, the spread of zeta-regularised determinants into theoretical physics was catalysed by Polyakov's paper on the quantum geometry of bosonic strings, where this anomaly is the obstruction to conformal invariance of the string path integral. The paper mentions this lineage explicitly when introducing §5.
