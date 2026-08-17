---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Brownian Loop Measure"
tags: [paper, physics, determinants, path-integral]
---

# Notation

- $\Delta_X$ — the positive Laplace–Beltrami operator; $\kappa\geq0$ a constant potential, physically the squared mass $m^2$ of a scalar field
- $\operatorname{Tr}(e^{-t\Delta_X})=\int_X p(t,x,x)\,\mathrm{d}\mathrm{vol}_g(x)$ — the heat trace, when $e^{-t\Delta_X}$ is trace class
- $\det(\Delta_X+\kappa)$ — the determinant, formal until regularised; $\det_\zeta$ its zeta-regularisation
- $\big|\mu^\kappa_X\big|_{\mathrm{reg}}$ — the **regularised** total mass of the killing loop measure over all loops, including the contractible and peripheral classes
- $\varphi$ — a free real scalar field; $S_E[\varphi]$ its Euclidean action; $Z^\kappa_X$ the partition function; $\Gamma^{(1)}_X(\kappa)$ the one-loop effective action

---

# In plain language

The Schwinger proper-time representation writes a log-determinant as a time integral of a heat trace:
$$-\log\det(\Delta_X+\kappa) = \int_0^\infty\frac{\mathrm{d}t}{t}\,e^{-\kappa t}\operatorname{Tr}\big(e^{-t\Delta_X}\big).$$
The name comes from quantum field theory, where $t$ is the "proper time" of a particle worldline; the identity itself is the operator version of $-\log\lambda = \int_0^\infty\frac{\mathrm{d}t}{t}e^{-t\lambda}$, which diverges at $t=0$ for every $\lambda$ and is therefore formal until regularised.

**Why it belongs in this paper.** Look at the right-hand side and compare it with [[Constr - The Brownian Loop Measure|Definition 2.1]]. Both integrate a diagonal heat kernel over $X$; both then integrate over $t$ against the multiplicative Haar weight $\mathrm{d}t/t$; and the extra factor $e^{-\kappa t}$ is exactly the killing weight that turns $\mu_X$ into $\mu^\kappa_X$. **Term for term, the Schwinger representation is the total mass of the Brownian loop measure with killing.** So
$$-\log\det(\Delta_X+\kappa) = \big|\mu^\kappa_X\big|_{\mathrm{reg}},$$
and this is the reason §5 exists: it is the identification that makes a probabilistic object (a loop mass) and a spectral object (a determinant) the same thing, and it explains why killing rates rather than plain Brownian motion are the natural parameter throughout §4–§6.

The word carrying all the weight is **regularised**. The mass is infinite, because of the small loops, and the $t$-integral above diverges at $t=0$ for the same reason. §5 supplies the regularisation, and its choice — truncation by the length spectrum, following Wang–Xue — is one of several possible; the alternative in the literature truncates by quadratic variation.

---

# The definition

> **Definition (Schwinger proper-time representation).** For a non-negative self-adjoint operator $\Delta_X$ with trace-class heat semigroup and a constant $\kappa\geq0$,
> $$-\log\det\big(\Delta_X+\kappa\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\,e^{-\kappa t}\operatorname{Tr}\big(e^{-t\Delta_X}\big),$$
> where, when $e^{-t\Delta_X}$ is trace class,
> $$\operatorname{Tr}\big(e^{-t\Delta_X}\big) = \int_X p(t,x,x)\,\mathrm{d}\mathrm{vol}_g(x).$$
> The identity is formal — the integral diverges at $t=0$ — and is made precise by the zeta-regularisation of [[Def - Zeta-Regularised Determinant of the Laplacian]].

> **The loop-measure reading.** The heat trace is built from Brownian paths that start and return to the same point; integration over $t$ with the Haar weight $\mathrm{d}t/t$ together with the killing weight $e^{-\kappa t}$ is precisely the structure of the Brownian loop measure with killing. Hence
> $$-\log\det\big(\Delta_X+\kappa\big) = \big|\mu^\kappa_X\big|_{\mathrm{reg}},$$
> the regularised total mass of the killing loop measure over **all** loops, including the divergent contractible class and, where present, the peripheral classes.

---

# Types and signatures

- $\operatorname{Tr}(e^{-t\Delta_X}) : (0,\infty)\to(0,\infty]$ — finite for each $t>0$ exactly when the semigroup is trace class; on a closed hyperbolic surface it behaves like $\mathrm{Area}(X)/4\pi t$ as $t\downarrow0$
- $\det(\Delta_X+\kappa)$ — not a number until regularised; $\det_\zeta$ and $\det_0$ are the two regularisations used in §5
- $|\mu^\kappa_X|_{\mathrm{reg}}$ — a real number after regularisation; **not** the same as $\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$, which excludes the trivial and peripheral classes and is finite outright when $s>\delta$

The distinction in the last line is the one most worth keeping straight in §5: **"total mass" in §4 means the sum over non-trivial non-peripheral classes; "total mass" in the Schwinger identity means all loops.** The gap between them is exactly the divergent contribution that §5 renormalises.

---

# Example

The field-theoretic derivation, which is where the identity earns its physical reading. Take a free real scalar field $\varphi$ of mass $\sqrt\kappa$ on $X$, with Euclidean action
$$S_E[\varphi] = \tfrac12\int_X\big(|\nabla\varphi|^2+\kappa\varphi^2\big)\,\mathrm{d}\mathrm{vol}_g = \tfrac12\langle\varphi,(\Delta_X+\kappa)\varphi\rangle,$$
the second equality using that $\Delta_X$ is the positive Laplacian. The action is quadratic, so the Euclidean path integral is Gaussian:
$$Z^\kappa_X = \int\mathcal{D}\varphi\,e^{-S_E[\varphi]} \propto \det(\Delta_X+\kappa)^{-1/2},$$
and the one-loop effective action is $\Gamma^{(1)}_X(\kappa)=-\log Z^\kappa_X = \tfrac12\log\det(\Delta_X+\kappa)$. Combining with the Schwinger representation,
$$Z^\kappa_X \propto \exp\Big(\tfrac12\big|\mu^\kappa_X\big|_{\mathrm{reg}}\Big):$$
**the partition function of a free real scalar field of mass $\sqrt\kappa$ is, up to normalisation, the exponential of half the regularised total mass of Brownian loops on $X$ with killing rate $\kappa$.** The factor $\tfrac12$ is the power $\det^{-1/2}$ of a single real field; a complex field would give $\det^{-1}$ and no half.

**Near-miss non-example.** Without the regularisation, every step above is false as an equality of numbers: $\int_0^\infty\frac{\mathrm{d}t}{t}e^{-\kappa t}\operatorname{Tr}(e^{-t\Delta_X})$ diverges at $t=0$ like $\int_0 \mathrm{Area}(X)/(4\pi t^2)\,\mathrm{d}t$, and $\prod_j\lambda_j$ diverges too. The two divergences are the same divergence seen from the two sides of the Mellin transform, which is why the zeta-regularisation of [[Def - Zeta-Regularised Determinant of the Laplacian]] cures both at once — and why the renormalisation is *forced* rather than chosen.

---

# Used in this paper at

- [[§3.2 Euclidean Quantum Mechanics and the Path Integral]] — where the identification is set out
- [[Def - Zeta-Regularised Determinant of the Laplacian]] — the rigorous version of the same $\int_0^\infty t^{s-1}(\cdots)\,\mathrm{d}t$ structure, via the Mellin transform
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] — makes the identification precise on a closed hyperbolic surface, with the length-spectrum truncation
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)|Theorem 5.7]] — the cusped analogue, with $\det_0$ in place of $\det_\zeta$

---

# Where this sits in my DAG

The operator theory — non-negative self-adjoint operators, trace-class semigroups, Lidskii's theorem computing the trace as the integral of the diagonal — is *Functional Analysis* (🟢). The heat trace and its short-time asymptotics are *Analysis of PDEs* (🟢). The Feynman–Kac formula that makes $p^V$ a Brownian expectation is *SDEs* (🟢) and is used in §3.2 alongside this.

The Gaussian path integral $\int\mathcal{D}\varphi\,e^{-\frac12\langle\varphi,A\varphi\rangle}\propto\det(A)^{-1/2}$ is a physicist's identity: $\mathcal{D}\varphi$ is the formal Lebesgue measure on fields, which does not exist as a measure. It is used here as motivation only; nothing in §5 depends on it, and the rigorous content is the Mellin-transform definition of $\det_\zeta$.
