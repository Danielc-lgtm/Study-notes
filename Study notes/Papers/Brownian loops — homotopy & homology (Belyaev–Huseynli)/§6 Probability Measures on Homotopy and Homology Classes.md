---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "6"
prereqs:
  - "Constr - The Probability Measure on Free Homotopy Classes"
  - "Thm - Moments of the Length via the Selberg Zeta Function"
  - "Constr - The Mass in a Homology Class"
  - "Def - Selberg L-Function"
  - "Thm - Fourier Expansion and Inversion by Homology Class"
tags: [paper, probability, homology, zeta-functions]
---

# Notation

**Standing convention.** Throughout this section $\kappa>0$, with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ and $\operatorname{Re}(s)>\delta$; the $\kappa=0$ case can be run using the renormalised expressions of §5.

- $\mathbb{P}_s$ — the [[Constr - The Probability Measure on Free Homotopy Classes|normalised probability measure]] on non-trivial non-peripheral free homotopy classes; $\mathbb{E}_s$, $\mathrm{Var}_s$ its expectation and variance
- $L := m\ell_\gamma$ — the length of the geodesic representative, regarded as a random variable under $\mathbb{P}_s$
- $F(s) := -\log Z_X(s)$ — the total mass, as a function of the spectral parameter
- $\ell_{\mathrm{sys}} := \min_{\gamma\in\mathcal{P}_X}\ell_\gamma$ — the [[Def - Systole|systole]]; $N_{\mathrm{sys}} := \#\{\gamma\in\mathcal{P}_X : \ell_\gamma=\ell_{\mathrm{sys}}\}\geq2$ its multiplicity
- $H_1(X,\mathbb{Z})$ — first homology, the abelianisation of $\pi_1(X)\cong\Gamma$; $\Gamma\twoheadrightarrow H_1(X,\mathbb{Z})$ the abelianisation map; $[\gamma]$ the image of $\gamma$, so $[\gamma^m]=m[\gamma]$
- $r$ — the rank of $H_1(X,\mathbb{Z})$: $r=2g$ for a closed surface of genus $g$; $r=2g+b-1$ with $b=n_C+n_F$ ends otherwise
- $\chi : H_1(X,\mathbb{Z})\to\mathbb{C}^\times$ — a character; unitary when the image lies in $S^1$
- $\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^r\cong(\mathbb{R}/\mathbb{Z})^r$ — the [[Def - Character Torus and the Pontryagin Dual|character torus]]; $\mathrm{d}\chi$ its normalised Haar measure
- $L_X(s,\chi)=\prod_{\gamma\in\mathcal{P}_X}\prod_{k=0}^\infty(1-\chi([\gamma])e^{-(s+k)\ell_\gamma})$ — the [[Def - Selberg L-Function|Selberg $L$-function]]; $L_X(s,\mathbf{1})=Z_X(s)$
- $\mathcal{H}^1(X)$, $\mathcal{H}^1_{\mathbb{Z}}(X)$ — real harmonic $1$-forms, and those with integral periods; $\mathrm{Jac}(X)$ the Jacobian
- $\mathcal{L}_\lambda$ — the loop soup of intensity $\lambda$; $\mathcal{L}^*_\lambda$ its non-contractible, non-cusp-homotopic loops; $\beta(\lambda)=\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]$ the total homology

---

# What this section is for

All the finiteness work of §4 and §5 was so that this section could divide.

The masses $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ are non-negative and, when $s>\delta$, sum to the finite number $-\log Z_X(s)$. So dividing by that sum produces a **probability measure on the set of free homotopy classes**. The weights are natural in a specific sense worth stating: their normalising constant is the object of Corollary 4.3, and — because the masses depend on $s$ only through $e^{(1-s)m\ell_\gamma}$ — every moment of the resulting distribution is a derivative of $\log Z_X$. That is the whole of §6.1: an exponential-family structure in which the spectral parameter $s$ is the natural parameter and the geodesic length $L$ is the sufficient statistic.

The consequence is a genuine dictionary. Want the mean geodesic length under $\mathbb{P}_s$? It is $-\frac{\mathrm{d}}{\mathrm{d}s}\log(-\log Z_X(s))$. Want the variance? Second derivative of the same. Want the systole? Take $s\to\infty$ and read off the exponential rate. The paper's stated motivation — understanding the geometry of the surface through an explicit per-class weighting, for instance the probability of intersections of closed geodesics — is served by having every such question reduce to a derivative of one function.

§6.2 then coarsens. A free homotopy class is a conjugacy class in $\Gamma$, which for genus $g\geq2$ is non-abelian and remembers the *order* in which handles are traversed, up to conjugation. Passing to **homology** — the abelianisation — discards that and keeps only the net winding around each cycle. It is a much coarser partition: a fixed homology class $\beta$ collects contributions from infinitely many distinct free homotopy classes, so $\mu^\kappa_X(\beta)$ is an infinite sum with no obvious closed form.

The device that computes it is exactly the twisting anticipated in [[§3.2 Euclidean Quantum Mechanics and the Path Integral|Remark 3.3]]. Weight each geodesic by a unitary character $\chi$ of $H_1(X,\mathbb{Z})$; the weight $\chi([\gamma])^m=\chi(m[\gamma])=\chi(\beta)$ depends only on the homology class of the iterate, so the double sum regroups by homology. The twisted object is the [[Def - Selberg L-Function|Selberg $L$-function]], and it plays exactly the role Dirichlet $L$-functions play for primes in arithmetic progressions: **$-\log L_X(s,\chi)$ is the Fourier transform, on the character torus, of the function $\beta\mapsto\mu^\kappa_X(\beta)$.** Fourier inversion then computes a single homology class's mass as one integral over a compact torus — infinitely many homotopy classes summed by a finite-dimensional integral.

For a closed surface the character torus is not merely a torus: by Hodge theory it is the Jacobian. Every de Rham class has a unique harmonic representative, so $H^1_{\mathrm{dR}}(X,\mathbb{R})\cong\mathcal{H}^1(X)$, and $H^1(X,\mathbb{Z})$ corresponds to the lattice $\mathcal{H}^1_{\mathbb{Z}}(X)$ of harmonic forms with integral periods. Attaching to a harmonic $1$-form $\omega$ the unitary holonomy $\chi_\omega(\beta)=e^{2\pi i\int_\beta\omega}$ identifies
$$\widehat{H_1(X,\mathbb{Z})}\;\cong\;\frac{H^1_{\mathrm{dR}}(X,\mathbb{R})}{H^1(X,\mathbb{Z})}\;\cong\;\frac{\mathcal{H}^1(X)}{\mathcal{H}^1_{\mathbb{Z}}(X)}\;\cong\;\mathrm{Jac}(X),$$
and since $*^2=-1$ on $1$-forms the Hodge star gives the real $2g$-torus a complex structure, which with the intersection pairing makes $\mathrm{Jac}(X)$ a principally polarised abelian variety. In the non-compact case this identification is unavailable and the paper does not pursue partial analogues.

---

# §6.1 The measure on free homotopy classes

## The measure itself

> [!abstract] Type card — the probability measure $\mathbb{P}_s$
> **Given.** A killing rate $\kappa>0$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ satisfying $s>\delta$, so that [[Thm - Finiteness of the Total Mass|Corollary 4.7]] gives a finite total mass and [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] identifies it as $-\log Z_X(s)$.
>
> **Produces.** A genuine probability measure on the set of non-trivial non-peripheral free homotopy classes,
> $$\mathbb{P}_s\big(\mathcal{C}_X(\gamma^m)\big) := \frac{\mu^\kappa_X(\mathcal{C}_X(\gamma^m))}{-\log Z_X(s)} = \frac{\mu^\kappa_X(\mathcal{C}_X(\gamma^m))}{\sum_{\gamma'\in\mathcal{P}_X}\sum_{m'\geq1}\mu^\kappa_X(\mathcal{C}_X(\gamma'^{m'}))}.$$
>
> **Lets you.** Turn any function of a free homotopy class into a random variable with computable moments — most naturally the length $L=m\ell_\gamma$ of the geodesic representative.

Full construction: [[Constr - The Probability Measure on Free Homotopy Classes]].

## Moments, all at once

The observation that generates everything is one line: the mass depends on $s$ only through $e^{(1-s)m\ell_\gamma}$, so
$$\frac{\mathrm{d}}{\mathrm{d}s}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = -(m\ell_\gamma)\,\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big).$$
Differentiating in $s$ *is* multiplying by $-L$. Rather than treat each moment separately, note that **shifting the spectral parameter is the same as tilting by the length**.

> [!abstract] Type card — moments of $L$ under $\mathbb{P}_s$
> **Given.** $F(s):=-\log Z_X(s)$ for $s>\delta$, and $r>1-s$.
>
> **Produces.** The tilting identity and all moments:
> $$\mathbb{E}_s\big[e^{-rL}\big] = \frac{-\log Z_X(s+r)}{-\log Z_X(s)} = \frac{\log Z_X(s+r)}{\log Z_X(s)},\qquad \mathbb{E}_s\big[L^n\big] = \frac{(-1)^nF^{(n)}(s)}{F(s)},\ n\geq1,$$
> together with the first two cumulants
> $$\mathbb{E}_s[L] = -\frac{\mathrm{d}}{\mathrm{d}s}\log\big(-\log Z_X(s)\big) = -\frac{Z'_X(s)}{Z_X(s)\log Z_X(s)},\qquad \mathrm{Var}_s(L) = \frac{\mathrm{d}^2}{\mathrm{d}s^2}\log\big(-\log Z_X(s)\big).$$
>
> **Lets you.** Read every moment of the geodesic length off the Selberg zeta function and its derivatives, with no geometric input beyond it.

**Strategy.** The summand at parameter $s$ multiplied by $e^{-rm\ell_\gamma}$ is exactly the summand at parameter $s+r$; that single observation gives the tilting identity, and differentiating $F$ repeatedly gives the moments.

Full derivation, including the explicit variance in terms of $Z_X, Z'_X, Z''_X$: [[Thm - Moments of the Length via the Selberg Zeta Function]]. One structural consequence: $\log F$ is strictly convex on $(1,\infty)$, so $s\mapsto\mathbb{E}_s[L]$ is strictly decreasing — **increasing the killing rate shortens the typical class**, which is what one would expect since killing suppresses long loops.

## The $s \to \infty$ limit and the systole

> [!abstract] Type card — concentration on systolic classes
> **Given.** The [[Def - Systole|systole]] $\ell_{\mathrm{sys}}=\min_{\gamma\in\mathcal{P}_X}\ell_\gamma$ and its multiplicity $N_{\mathrm{sys}}\geq2$ — at least two because $\mathcal{P}_X$ consists of *oriented* geodesics and a hyperbolic element of a torsion-free Fuchsian group is never conjugate to its inverse.
>
> **Produces.** As $s\to\infty$: $\mathbb{P}_s(\mathcal{C}_X(\gamma))\to 1/N_{\mathrm{sys}}$ for each systolic $\gamma$ and $\to0$ for every other class; hence $\mathbb{E}_s[L]\to\ell_{\mathrm{sys}}$. On the analytic side, $-\log Z_X(s)\sim Ce^{-s\ell_{\mathrm{sys}}}$ with $C=N_{\mathrm{sys}}/(1-e^{-\ell_{\mathrm{sys}}})$, so
> $$\ell_{\mathrm{sys}} = -\lim_{s\to\infty}\frac1s\log\big(-\log Z_X(s)\big),\qquad N_{\mathrm{sys}} = \big(1-e^{-\ell_{\mathrm{sys}}}\big)\lim_{s\to\infty}e^{s\ell_{\mathrm{sys}}}\big(-\log Z_X(s)\big).$$
>
> **Lets you.** Extract both the systole and its multiplicity analytically from the Selberg zeta function, purely from its large-$s$ asymptotics.

**Strategy.** The weights $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))\sim e^{-sm\ell_\gamma}$ are dominated as $s\to\infty$ by the slowest-decaying terms, which are the primitive ($m=1$) classes realising the systole; the probabilistic and the analytic statements are the same computation read on the two sides of the normalisation.

Full statement: [[Thm - Concentration on Systolic Classes]]. Note the orientation point in the "Given" — it is the reason the limiting measure is uniform on at least two atoms rather than a point mass, and it is a genuine fact about torsion-free Fuchsian groups rather than a convention.

---

# §6.2 The measure on homology classes

## Definition 6.1 — the mass in a homology class

> [!abstract] Type card — Definition 6.1 (mass in a homology class)
> **Given.** $\beta\in H_1(X,\mathbb{Z})$, and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$.
>
> **Produces.** The number
> $$\mu^\kappa_X(\beta) := \sum_{\substack{\gamma\in\mathcal{P}_X,\ m\geq1\\ m[\gamma]=\beta}}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = \sum_{\substack{\gamma\in\mathcal{P}_X,\ m\geq1\\ m[\gamma]=\beta}}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},$$
> an infinite sum over the homotopy classes lying above $\beta$, with no closed form available directly.
>
> **Lets you.** Ask homological questions — in particular about *algebraic* intersection numbers, which unlike geometric intersection numbers are defined on homology classes rather than free homotopy classes.

Page: [[Constr - The Mass in a Homology Class]]. The paper notes that a definition of loop measure in homology classes first appeared in Le Jan, that the conventions differed enough that theirs was developed independently, and that the $L$-function route recovers Le Jan's results in greater generality — extending to the non-compact case.

## Corollary 6.4 and Theorem 6.5 — the Fourier pair

> [!abstract] Type card — Corollary 6.4 (Selberg $L$-function identity)
> **Given.** A unitary character $\chi:H_1(X,\mathbb{Z})\to S^1$, and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$.
>
> **Produces.** The identity
> $$-\log L_X(s,\chi) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty \chi([\gamma])^m\,\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac1m\cdot\frac{\chi([\gamma])^m e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.$$
>
> **Lets you.** Twist Corollary 4.3 by a character; setting $\chi=\mathbf{1}$ recovers it exactly, since $L_X(s,\mathbf{1})=Z_X(s)$.

**Strategy.** Take logarithms of the absolutely convergent Euler product term by term, expand $-\log(1-z)=\sum_m z^m/m$ with $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$ — legitimate because $|\chi([\gamma])|=1$ gives $|z|=e^{-(\operatorname{Re}(s)+k)\ell_\gamma}<1$ — and sum the geometric series over $k$ to get $e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$.

> [!abstract] Type card — Theorem 6.5 (Fourier expansion and inversion)
> **Given.** A geometrically finite $X$ with $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$; $\kappa\geq-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ and $\operatorname{Re}(s)>\delta$.
>
> **Produces.** The absolutely convergent **Fourier expansion**, for every unitary $\chi\in\widehat{H_1(X,\mathbb{Z})}$,
> $$-\log L_X(s,\chi) = \sum_{\beta\in H_1(X,\mathbb{Z})}\chi(\beta)\,\mu^\kappa_X(\beta),$$
> and the **inversion formula**, for each $\beta$,
> $$\mu^\kappa_X(\beta) = \int_{\widehat{H_1(X,\mathbb{Z})}}\big(-\log L_X(s,\chi)\big)\,\overline{\chi(\beta)}\,\mathrm{d}\chi,$$
> with $\mathrm{d}\chi$ normalised Haar measure on $\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^r$.
>
> **Lets you.** Compute the mass in a single homology class — an infinite sum over free homotopy classes with no closed form — as one integral over a compact $r$-dimensional torus. This is the payoff of the whole section.

**Strategy.** Regroup the double sum of Corollary 6.4 by the value of $m[\gamma]$, using that $\chi([\gamma])^m=\chi(m[\gamma])$ depends only on the homology class; then multiply by $\overline{\chi(\beta)}$, exchange sum and integral by absolute convergence, and apply orthogonality of characters, which kills every term but $\beta'=\beta$.

Full proofs: [[Thm - Selberg L-Function Identity]], [[Thm - Fourier Expansion and Inversion by Homology Class]].

> [!note] Remark 6.6 — the closed case, over the Jacobian
> When $X$ is closed, the identification $\widehat{H_1(X,\mathbb{Z})}\cong\mathrm{Jac}(X)$ has natural pairing $\langle\beta,[\omega]\rangle=\int_\beta\omega \pmod{\mathbb{Z}}$, so the inversion formula may be written as an integral over the Jacobian against $e^{-2\pi i\int_\beta\omega}$:
> $$\mu^\kappa_X(\beta) = \int_{\mathrm{Jac}(X)}\big(-\log L_X(s,\chi_{[\omega]})\big)\,e^{-2\pi i\int_\beta\omega}\,\mathrm{d}[\omega],$$
> with $\mathrm{d}[\omega]$ the normalised Haar measure on the underlying real Jacobian torus. See [[Def - The Jacobian as a Principally Polarised Abelian Variety]].

## Proposition 6.7 — the total homology of the loop soup

> [!abstract] Type card — Proposition 6.7 (distribution of the total homology)
> **Given.** $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$; the [[Thm - Poissonian Structure of Homotopy Classes|loop soup]] $\mathcal{L}_\lambda$ of intensity $\lambda>0$; and $\beta(\lambda):=\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]\in H_1(X,\mathbb{Z})$, the total homology of the non-contractible, non-cusp-homotopic loops. The sum is finite because $\#\mathcal{L}^*_\lambda$ is Poisson with finite mean $-\lambda\log Z_X(s)$.
>
> **Produces.** The characteristic function on the character torus and the pointwise law:
> $$\mathbb{E}\big[\chi(\beta(\lambda))\big] = \Big(\frac{Z_X(s)}{L_X(s,\chi)}\Big)^\lambda,\qquad \mathbb{P}\big(\beta(\lambda)=\beta\big) = Z_X(s)^\lambda\int_{\widehat{H_1(X,\mathbb{Z})}}L_X(s,\chi)^{-\lambda}\,\overline{\chi(\beta)}\,\mathrm{d}\chi,$$
> with complex powers defined by $L_X(s,\chi)^{-\lambda}:=\exp(-\lambda\log L_X(s,\chi))$ using the expansion of Corollary 6.4.
>
> **Lets you.** Describe the full distribution of a random homology class built from a Poissonian ensemble of loops in closed form — the strongest statement in the paper, and the one that most clearly justifies having built a *measure* on loops rather than a family of expectations.

**Strategy.** Apply the exponential formula for a Poisson point process with $e^{F(\eta)}=\chi([\eta])$, so the product over the soup becomes $\chi(\beta(\lambda))$ and the right-hand side becomes $\exp(\lambda\sum_{\gamma,m}(\chi([\gamma])^m-1)\mu^\kappa_X(\mathcal{C}_X(\gamma^m)))$; recognise the two sums as the Selberg $L$-function identity applied to $\chi$ and to the trivial character. Then multiply by $\overline{\chi(\beta)}$, integrate, and use orthogonality.

Full proof: [[Thm - Distribution of the Total Homology of the Loop Soup]].

---

# What to carry forward

**The exponential-family structure.** $s$ is the natural parameter, $L$ is the sufficient statistic, $F(s)=-\log Z_X(s)$ is the partition function, and every cumulant is a derivative of $\log F$. Once seen this way, §6.1 needs no memorisation.

**Twisting as the general move.** $\chi=\mathbf{1}$ gives the Selberg zeta and the homotopy decomposition; a unitary character of $H_1$ gives the Selberg $L$-function and the homology decomposition; a general finite-dimensional $\rho$ of $\Gamma$ gives the twisted Ruelle zeta of [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]]. Three sections of the paper are three instances of [[§3.2 Euclidean Quantum Mechanics and the Path Integral|Remark 3.3]].

**Fourier duality on the character torus** as the computational engine: $-\log L_X(s,\cdot)$ and $\mu^\kappa_X(\cdot)$ are a Fourier pair, and the whole of §6.2 is the pair plus orthogonality of characters.

**That the systole is analytically visible.** $\ell_{\mathrm{sys}} = -\lim_{s\to\infty}\frac1s\log(-\log Z_X(s))$, and $N_{\mathrm{sys}}$ from the constant. This is the sharpest illustration in the paper of the general principle that geometric data is recoverable from the zeta function's asymptotics.

Next: [[§7 Brownian Loops on Hyperbolic 3-Manifolds]], the extension — and note that none of §6 has been carried there, for the reason recorded on [[Map - Brownian Loops on Homotopy and Homology Classes]].
