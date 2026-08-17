---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "4"
prereqs:
  - "Def - Selberg Zeta Function"
  - "Def - Critical Exponent and the Prime Geodesic Theorem"
  - "Thm - Selberg Zeta Criterion"
  - "Thm - Selberg Zeta Identity (Killing Case)"
  - "Thm - Finiteness of the Total Mass"
tags: [paper, spectral-geometry, zeta-functions, loop-measures]
---

# Notation

**Standing convention.** *Total mass* in this section always means the sum over **non-trivial, non-peripheral** free homotopy classes. The full loop measure has infinite mass unconditionally, because of the trivial (contractible) class; that divergence is never in question and is dealt with only in §5.

- $Z_X(s) = \prod_{\gamma\in\mathcal{P}_X}\prod_{k=0}^\infty(1-e^{-(s+k)\ell_\gamma})$ — the [[Def - Selberg Zeta Function|Selberg zeta function]], absolutely convergent for $\operatorname{Re}(s)>\delta$, meromorphically continued to $\mathbb{C}$
- $\delta$ — the [[Def - Critical Exponent and the Prime Geodesic Theorem|critical exponent]] of $\Gamma$: the exponent of convergence of the Poincaré series $\sum_{h\in\Gamma}e^{-s\,d(z,hz)}$
- $N_X(R) = \#\{\gamma\in\mathcal{P}_X : \ell_\gamma\leq R\}$ — the prime geodesic counting function; $N_X(R)\sim e^{\delta R}/\delta R$
- $\ell_{\mathrm{sys}}$ — the [[Def - Systole|systole]], the length of the shortest closed geodesic on $X$
- $I_\phi(L)$ — the [[Constr - The Weighted Heat-Kernel Integral Iϕ|weighted heat-kernel integral]] of Definition 3.6
- $s(\phi)$ — the spectral parameter attached to $\phi$: $s=1$ for Brownian motion and for $\alpha$-stable, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ for killing at rate $\kappa\geq-\tfrac14$ and for the shifted $\alpha$-stable case
- $R_X(s) = \prod_{\gamma\in\mathcal{P}_X}(1-e^{-s\ell_\gamma})$ — the [[Def - Ruelle Zeta Function and its Twist|Ruelle zeta function]]; $R_X(s,\rho)=\prod_\gamma\det(I-\rho(\tau)e^{-s\ell_\gamma})$ its twist by a representation $\rho:\Gamma\to\mathrm{GL}(V_\rho)$
- $c_\rho$ — the abscissa of convergence for the twisted product, governed by the growth $\|\rho(\tau)\|\leq C_\rho e^{c\ell_\gamma}$; one may take $c_\rho=\delta$ for unitary $\rho$
- $\kappa_-(s):=s(s-1)$, $\kappa_+(s):=s(s+1)$ — the two killing rates paired in Corollary 4.6

---

# What this section is for

§3 computed the mass of one class. This section sums over all of them, and the answer is a zeta function.

The reason to expect that is visible before any calculation. Take the killing formula $\mu^\kappa_X(\mathcal{C}_X(\gamma^m)) = \frac1m\frac{e^{(1-s)L}}{e^L-1}$ with $L=m\ell_\gamma$, and take the logarithm of the [[Def - Selberg Zeta Function|Selberg zeta function]]'s double Euler product. Expanding $-\log(1-x)=\sum_{m\geq1}x^m/m$ and summing the inner geometric series over $k$ gives
$$-\log Z_X(s) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},\qquad \operatorname{Re}(s)>\delta,$$
which is *term for term* the sum of the loop masses. So the identity
$$\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = -\log Z_X\Big(\tfrac12+\sqrt{\tfrac14+\kappa}\Big)$$
is not a coincidence to be explained but a *matching of two expansions of the same shape*. What §3 really proved is that the loop mass has exactly the functional form that the Selberg zeta's logarithm has.

That observation is what [[Thm - Selberg Zeta Criterion|Lemma 4.2]] formalises, and formalising it is worth the trouble because it turns "does this process give a zeta identity?" into a scalar question with no geometry in it: does $\frac{L}{2\sinh(L/2)}I_\phi(L)$ equal $C\frac{e^{(1-s)L}}{e^L-1}$ for constants $C>0$ and $s>\delta$ independent of $L$? If yes, the total mass is $-C\log Z_X(s)$. Checking this for a new Bernstein function is a one-variable calculation.

The section then does two more things. It asks **which other zeta functions the loop measure reaches**, and the answer is instructive: the [[Def - Ruelle Zeta Function and its Twist|Ruelle zeta function]] and its twists are reachable, but only through a *difference* of two loop measures at two different killing rates, rather than a single one. This is precisely why the Selberg identity is the natural one — Selberg's double product $\prod_k$ is what a single loop mass produces, and Ruelle's single product needs the extra $k$-sum removed by hand.

And it asks **when the total mass is finite**, which is the question §6 needs answered before it can normalise. The answer is a competition between two exponential rates. The mass of a class decays like $e^{-s\ell_\gamma}$; the number of primitive geodesics of length up to $R$ grows like $e^{\delta R}/\delta R$ by the prime geodesic theorem — the exact analogue of the prime number theorem, with primitive closed geodesics playing the role of primes. **Finite total mass is exactly $s>\delta$: decay beats proliferation.** Since $\delta=1$ when $X$ has finite area and $\delta<1$ when $X$ has infinite area, this says: infinite-area surfaces are fine as they stand, finite-area surfaces need a killing rate $\kappa>0$ (equivalently $s>1$), and at $s=\delta$ the sum diverges — with $Z_X(s)\to0$ as $s\downarrow\delta$, which is the analytic face of the same divergence.

---

# Results

## Lemma 4.2 — the Selberg zeta criterion

> [!abstract] Type card — Lemma 4.2 (Selberg zeta criterion)
> **Given.** The [[Constr - The Weighted Heat-Kernel Integral Iϕ|integral]] $I_\phi$ of Definition 3.6, and the existence of a constant $C>0$ and a real number $s>\delta$, **both independent of $L$**, such that
> $$\frac{L}{2\sinh(L/2)}\,I_\phi(L) = C\cdot\frac{e^{(1-s)L}}{e^{L}-1}\qquad\text{for all }L>0.$$
>
> **Produces.** The identity $\displaystyle\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty \mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = -C\log Z_X(s)$ — an equality of finite non-negative numbers.
>
> **Lets you.** Certify a zeta identity for a *new* Bernstein function by checking one scalar functional equation in one variable. No geometry, no group theory, no heat kernel: the entire geometric content has been absorbed into the shape of the right-hand side.

**Strategy.** Rewrite Theorem 3.5 as $\mu^\phi_X(\mathcal{C}_X(\gamma^m)) = \frac1m\cdot\frac{L}{2\sinh(L/2)}I_\phi(L)$ using $\ell_\gamma = L/m$; substitute the hypothesis; then match term by term against the expansion of $-\log Z_X(s)$, with absolute convergence supplied by $s>\delta$.

Full proof: [[Thm - Selberg Zeta Criterion]].

## Corollary 4.3 — the Selberg zeta identity, killing case

> [!abstract] Type card — Corollary 4.3 (Selberg zeta identity, killing case)
> **Given.** A killing rate $\kappa\geq-\tfrac14$; set $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, and assume $s>\delta$ (the [[Def - Critical Exponent and the Prime Geodesic Theorem|critical exponent]]).
>
> **Produces.** The identity: total mass of the killing loop measure over all non-trivial non-peripheral classes $= -\log Z_X(s)$, that is
> $$\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = -\log Z_X\Big(\tfrac12+\sqrt{\tfrac14+\kappa}\Big).$$
>
> **Lets you.** Read the total loop mass straight off the Selberg zeta function, and — at $\kappa=0$, $s=1$ — recover the Brownian total mass as $-\log Z_X(1)$.

**Strategy.** Verify the hypothesis of Lemma 4.2 with $C=1$: from $I_\kappa(L)=e^{-L\sqrt{1/4+\kappa}}/L$ one gets $\frac{L}{2\sinh(L/2)}I_\kappa(L) = \frac{e^{-L\sqrt{1/4+\kappa}}}{2\sinh(L/2)} = \frac{e^{(1-s)L}}{e^L-1}$ for $s=\tfrac12+\sqrt{\tfrac14+\kappa}$.

Full statement: [[Thm - Selberg Zeta Identity (Killing Case)]]. When $X$ has infinite area, $\delta<1$ and the $\kappa=0$ quantity is finite; when $X$ has finite area, $\delta=1$ and it diverges. The identity was originally shown by Lemonde–Wang.

> [!note] Remark 4.4 — bosonic partition function reading
> Set $Z_\gamma(s):=\prod_{k=0}^\infty(1-e^{-(s+k)\ell_\gamma})^{-1}$ and $Z(s):=\prod_{\gamma\in\mathcal{P}_X}Z_\gamma(s) = Z_X(s)^{-1}$, both for $\operatorname{Re}(s)>\delta$. Then Corollary 4.3 reads $\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m)) = \log Z(s) = -\log Z_X(s)$. Each $Z_\gamma(s)$ is the partition function of a family of bosonic modes indexed by $k\geq0$ with weights $(s+k)\ell_\gamma$, and $Z(s)$ is the grand canonical partition function of a free non-interacting Bose gas at zero chemical potential. The reading is worth keeping alongside the field-theoretic one of [[§3.2 Euclidean Quantum Mechanics and the Path Integral|§3.2]]: there the total mass was half a log-determinant, here it is a log-partition-function, and the two are the same statement seen from the two sides of the Gaussian integral.

## Corollary 4.6 — the twisted Ruelle zeta identity

> [!abstract] Type card — Corollary 4.6 (twisted Ruelle zeta identity)
> **Given.** A finite-dimensional complex representation $\rho:\Gamma\to\mathrm{GL}(V_\rho)$, not necessarily unitary, with abscissa $c_\rho$; and $\operatorname{Re}(s)>\max(c_\rho,\tfrac12)$. Set $\kappa_-(s)=s(s-1)$ and $\kappa_+(s)=s(s+1)$, so that the principal square root gives $\tfrac12+\sqrt{\tfrac14+\kappa_-(s)}=s$ and $\tfrac12+\sqrt{\tfrac14+\kappa_+(s)}=s+1$.
>
> **Produces.** The identity
> $$-\log R_X(s,\rho) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\operatorname{tr}\rho(\tau^m)\Big[\mu^{\kappa_-(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)-\mu^{\kappa_+(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)\Big] = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac{\operatorname{tr}\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m}.$$
>
> **Lets you.** See exactly which zeta functions the loop measure reaches, and why the Selberg one is canonical: the Ruelle identity requires a *difference* of two loop measures at two killing rates, where Selberg requires one.

**Strategy.** Expand $-\log\det(I-M)=\sum_{m\geq1}\operatorname{tr}(M^m)/m$ on the twisted product; separately, compute the difference of the two killing masses from formula (26) and observe that $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$ makes the denominator cancel, leaving $e^{-sL}/m$. Match term by term.

Full proof and discussion: [[Thm - Twisted Ruelle Zeta Identity]]. The paper's own verdict is worth recording: the loop-measure identity holds "in principle for any zeta function built from the length spectrum", but for dynamical zeta functions such as Ruelle's the resulting identities "are more difficult to use in a meaningful way". Reading the difference structure explains why — the object being expressed is not a mass but a signed combination, so the Poissonian interpretation of §3.3 does not survive. What the difference *does* have is a clean meaning: passing from $\kappa_-$ to $\kappa_+$ suppresses longer loops more strongly, so the difference isolates the net contribution of each class between the two rates.

## Corollary 4.7 — finiteness of the total mass

> [!abstract] Type card — Corollary 4.7 (finiteness)
> **Given.** Any of the Bernstein functions treated in the paper, with its spectral parameter $s=s(\phi)$; and the [[Def - Critical Exponent and the Prime Geodesic Theorem|prime geodesic theorem]] $N_X(R)\sim e^{\delta R}/\delta R$ for $\Gamma$.
>
> **Produces.** Finiteness: if $s(\phi)>\delta$ then $\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\mu^\phi_X(\mathcal{C}_X(\gamma^m))<\infty$. At $s=\delta$ the sum diverges, and $Z_X(s)\to0$ as $s\downarrow\delta$.
>
> **Lets you.** Know in advance whether the normalisation of §6 is available. Infinite-area surfaces have $\delta<1$ and need nothing; finite-area surfaces have $\delta=1$ and need either a killing rate $\kappa>0$ or the renormalisation of §5.

**Strategy.** Sum over the iterates $m$ first, sandwiching $\sum_{m\geq1}\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ between $Ce^{-s\ell_\gamma}$ and $-\frac{C}{1-e^{-\ell_{\mathrm{sys}}}}\log(1-e^{-s\ell_\gamma})$, so that finiteness reduces to convergence of $\sum_{\gamma}e^{-s\ell_\gamma}$; then write that sum as a Riemann–Stieltjes integral against $N_X$ and integrate by parts, so the prime geodesic theorem turns the integrand into $e^{-(s-\delta)R}/R$.

Full proof: [[Thm - Finiteness of the Total Mass]]. **This is one of the three proofs worth reading in full** — the integration-by-parts-against-the-counting-function move is the template for every convergence question in this circle of ideas, and the borderline behaviour at $s=\delta$ (divergence like $\int^\infty \mathrm{d}R/R$, the gentlest possible) is worth seeing.

---

# What to carry forward

**The identity $\sum_{\gamma,m}\mu^\kappa_X = -\log Z_X(s)$, with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$.** This is the single most reused statement in the second half of the paper: it is the normalising constant of §6, it is what §5 substitutes into the determinant formulas, and it is the trivial-character case of the Selberg $L$-function identity of §6.2.

**The criterion as a shape.** A mass of the form $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$ gives a Selberg identity with constant $C$. Brownian and killing give $C=1$; both stable cases give $C=\alpha/2$. Anything not of this shape — [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]], for instance — falls outside the criterion, which is why §7 has no zeta identity.

**The finiteness dichotomy $s>\delta$**, and the two regimes $\delta<1$ (infinite area) versus $\delta=1$ (finite area) it splits into. Everything in §5 exists to handle the second regime.

**That $\delta$ carries many meanings.** Exponent of convergence of the Poincaré series; Hausdorff dimension of the limit set $\Lambda(\Gamma)\subset\partial\mathbb{H}^2$ by Patterson–Sullivan theory; topological entropy of the geodesic flow on the non-wandering set; and, when $\delta>\tfrac12$, the determinant of the smallest $L^2$-eigenvalue via $\lambda_0=\delta(1-\delta)$. All four are collected on [[Def - Critical Exponent and the Prime Geodesic Theorem]]; the equality $\lambda_0=\delta(1-\delta)$ is the one §5 uses.

Next: [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] handles the divergent finite-area case; [[§6 Probability Measures on Homotopy and Homology Classes]] normalises the convergent one.
