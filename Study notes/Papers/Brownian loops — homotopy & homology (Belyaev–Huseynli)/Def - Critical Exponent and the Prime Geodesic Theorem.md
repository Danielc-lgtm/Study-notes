---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Geometrically Finite Surfaces, Cusps and Funnels"
tags: [paper, spectral-geometry, hyperbolic-geometry]
---

# Notation

- $\delta$ — the critical exponent of $\Gamma$
- $\sum_{h\in\Gamma}e^{-s\,d(z,hz)}$ — the Poincaré series; $\delta$ is its exponent of convergence
- $\Lambda(\Gamma)\subset\partial\mathbb{H}^2$ — the limit set; $\Omega\subset T^1X$ the non-wandering set of the geodesic flow
- $N_X(R)=\#\{\gamma\in\mathcal{P}_X : \ell_\gamma\leq R\}$ — the prime geodesic counting function
- $\lambda_0$ — the smallest $L^2$-eigenvalue of $\Delta_X$; $s_j=\tfrac12+\sqrt{\tfrac14-\lambda_j}$
- $\mathrm{Li}(x)=\int_2^x\mathrm{d}t/\log t$; $\widetilde{\mathrm{Li}}$ its cutoff, equal to $\mathrm{Li}$ for $x\geq2$ and $0$ for $x<2$

---

# In plain language

**The critical exponent $\delta$ is the exponential rate at which the group $\Gamma$ proliferates.** Formally it is the exponent of convergence of the Poincaré series $\sum_{h\in\Gamma}e^{-s\,d(z,hz)}$ — the value of $s$ at which the series switches from convergent to divergent — which measures how fast the orbit $\Gamma z$ accumulates in $\mathbb{H}^2$.

The same rate governs the proliferation of closed geodesics, and that is the **prime geodesic theorem**:
$$N_X(R) := \#\{\gamma\in\mathcal{P}_X : \ell_\gamma\leq R\}\;\sim\;\frac{e^{\delta R}}{\delta R}\qquad(R\to\infty).$$
This is the exact analogue of the prime number theorem $\pi(x)\sim x/\log x$, with primitive closed geodesics playing the role of primes and $e^{\delta R}$ playing the role of $x$. Its status in the paper is the same as the prime number theorem's in analytic number theory: quoted, deep, and used constantly.

**Why the paper needs it.** [[Thm - Finiteness of the Total Mass|Corollary 4.7]] is a competition between two exponential rates. The mass of a class decays like $e^{-s\ell_\gamma}$; the number of classes of length up to $R$ grows like $e^{\delta R}$. **Finite total mass is exactly $s>\delta$: decay beats proliferation.** That single inequality determines whether §6's probability measure exists, whether §5's renormalisation is needed, and where every convergence hypothesis in the paper comes from.

Over the decades $\delta$ has accumulated four other descriptions, and the paper lists them because they are genuinely the same number and each is useful somewhere. It is the **Hausdorff dimension of the limit set** $\Lambda(\Gamma)\subset\partial\mathbb{H}^2$, by Patterson–Sullivan theory. It is the **topological entropy of the geodesic flow** on the non-wandering set $\Omega\subset T^1X$. When $\delta>\tfrac12$ it determines the **smallest $L^2$-eigenvalue** by $\lambda_0=\delta(1-\delta)$, lying below $\tfrac14$, the bottom of the continuous spectrum when $X$ is non-compact. And in the finite-area case $\delta=1$, giving $\Omega=T^1X$ and $\lambda_0=0$.

That last identity is the one §5 uses: $\delta=1$ and $\lambda_0=0$ is why $Z_X$ has a simple zero at $s=1$ on a finite-area surface, and hence why $Z'_X(1)$ appears in every determinant formula there.

---

# The definition

> **Definition (critical exponent).** The **critical exponent** $\delta$ of a Fuchsian group $\Gamma$ is the exponent of convergence of the Poincaré series
> $$\sum_{h\in\Gamma}e^{-s\,d(z,h\cdot z)},$$
> measuring the rate at which the orbit $\Gamma z$ accumulates in $\mathbb{H}^2$. It is independent of $z$.

> **Theorem (prime geodesic theorem).** The number of primitive closed geodesics of length at most $R$ satisfies
> $$N_X(R) := \#\{\gamma\in\mathcal{P}_X : \ell_\gamma\leq R\} \;\sim\;\frac{e^{\delta R}}{\delta R}\qquad(R\to\infty),\tag{40}$$
> so the number grows exponentially at rate $\delta$.

> **Theorem (refined prime geodesic theorem, closed surfaces).** For a closed hyperbolic surface, where $\delta=1$,
> $$N_X(R) = \mathrm{Li}(e^{\delta R}) + \sum_{0<\lambda_j\leq1/4}\mathrm{Li}\big(e^{s_jR}\big) + O_X\big(e^{3R/4}/R\big)\qquad(R\to\infty),\tag{43}$$
> where $\mathrm{Li}(x)=\int_2^x\mathrm{d}t/\log t\sim x/\log x$ and $s_j=\tfrac12+\sqrt{\tfrac14-\lambda_j}$.

**Other interpretations of $\delta$**, all quoted:

- **Patterson–Sullivan.** $\delta = \dim_H\Lambda(\Gamma)$, the Hausdorff dimension of the limit set in $\partial\mathbb{H}^2$.
- **Dynamics.** $\delta$ is the topological entropy of the geodesic flow on the non-wandering set $\Omega\subset T^1X$.
- **Spectrum.** When $\delta>\tfrac12$, $\lambda_0=\delta(1-\delta)$, lying below $\tfrac14$ — the bottom of the continuous spectrum when $X$ is non-compact.
- **Area dichotomy.** $\delta=1$ when $X$ has finite area, giving $\Omega=T^1X$ and $\lambda_0=0$; $\delta<1$ when $X$ has infinite area.

---

# Types and signatures

- $\delta\in(0,1]$ — a real number, an invariant of $\Gamma$ alone
- $N_X : [0,\infty)\to\mathbb{Z}_{\geq0}$ — a non-decreasing step function, $N_X(R)=0$ for $R<\ell_{\mathrm{sys}}$, finite for every $R$
- $\mathrm{Li} : [2,\infty)\to(0,\infty)$; $\widetilde{\mathrm{Li}} : (0,\infty)\to[0,\infty)$ its cutoff at $x=2$, so that $\widetilde{\mathrm{Li}}(e^R)$ makes sense for all $R\geq0$
- $s_j=\tfrac12+\sqrt{\tfrac14-\lambda_j}$ — real for $\lambda_j\leq\tfrac14$, which is why only the small eigenvalues contribute terms to (43)

---

# Example

The dichotomy in two concrete cases.

**A closed surface of genus $g\geq2$**: finite area, so $\delta=1$ and $\lambda_0=0$. Then $N_X(R)\sim e^R/R$, and $\sum_\gamma e^{-s\ell_\gamma}$ converges exactly for $s>1$. So the *Brownian* total mass ($s=1$) **diverges**, and a killing rate $\kappa>0$ — equivalently $s>1$ — is needed to restore finiteness. This is why §5 exists.

**A three-funnelled sphere**: infinite area, so $\delta<1$. Now $s=1>\delta$ already, and the Brownian total mass is finite with no killing at all. §6's probability measure exists directly, and §5 is unnecessary.

**Near-miss non-example — the borderline $s=\delta$.** The divergence at $s=\delta$ is as gentle as it could be. Writing $\sum_{\ell_\gamma\leq T}e^{-s\ell_\gamma}$ as a Stieltjes integral against $N_X$ and integrating by parts, the large-$R$ integrand is $e^{-(s-\delta)R}/R$, and
$$\int^\infty\frac{e^{-(s-\delta)R}}{R}\,\mathrm{d}R\quad\begin{cases}\text{converges},& s>\delta,\\ \text{diverges like }\int^\infty \mathrm{d}R/R,& s=\delta,\\ \text{diverges},& s<\delta.\end{cases}$$
So at $s=\delta$ the sum diverges only logarithmically — but it diverges, and correspondingly $-\log Z_X(s)\to\infty$ and $Z_X(s)\to0$ as $s\downarrow\delta$ by monotone convergence. **The failure is exactly at the boundary and not before it**, which is what makes the criterion $s>\delta$ sharp.

---

# Used in this paper at

- [[Def - Selberg Zeta Function]] — the Euler product converges absolutely exactly for $\operatorname{Re}(s)>\delta$
- [[Thm - Selberg Zeta Criterion|Lemma 4.2]] — the hypothesis requires $s>\delta$, which supplies absolute convergence
- [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] — stated under $s>\delta$
- [[Thm - Finiteness of the Total Mass|Corollary 4.7]] — the whole proof is (40) plus integration by parts
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] — the refined form (43) is what makes the renormalising subtraction $N_X(R)-\widetilde{\mathrm{Li}}(e^R)$ the right one; the error bound $|N_X(R)-\widetilde{\mathrm{Li}}(e^R)|=O_X(e^{(1-\epsilon)R})$ is what makes the integral converge
- [[Def - Ruelle Zeta Function and its Twist]] — $c_\rho=\delta$ for unitary $\rho$
- [[Constr - The Probability Measure on Free Homotopy Classes]] — the standing hypothesis $\operatorname{Re}(s)>\delta$ throughout §6

---

# Where this sits in my DAG

The definition of $\delta$ is elementary — an exponent of convergence of an explicit series — and reduces to [[Def - Fuchsian Group and the Quotient Surface]] plus the hyperbolic distance function, both anchors or one step from them.

**The prime geodesic theorem is quoted, not proved**, and it is the second of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|recorded gaps]]. It is a corollary of the Selberg trace formula, so it closes with the same study as the first gap; home node *Automorphic Forms / Selberg Trace Formula* (🔵), whose own description names "the prime geodesic theorem" among what it unlocks. The refined form (43), with the small-eigenvalue corrections, is likewise quoted.

The four alternative descriptions of $\delta$ are all quoted. **Only one is used**: $\lambda_0=\delta(1-\delta)$, hence $\lambda_0=0$ when $\delta=1$, hence the simple zero of $Z_X$ at $s=1$ that §5's limits turn on. The Patterson–Sullivan and entropy descriptions are context, and the vault's DAG node for *Ergodic Theory* is where the entropy one would be developed.
