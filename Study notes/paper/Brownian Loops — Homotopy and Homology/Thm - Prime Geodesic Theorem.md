---
type: theorem
subject: geometry
prereqs:
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
tags: [geometry, hyperbolic-geometry, spectral-geometry, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$X=\Gamma\backslash\mathbb{H}^2$ a geometrically finite hyperbolic surface; $\mathcal P_X$ its primitive closed [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length|geodesics]] of lengths $\ell_\gamma$; $\delta$ the [[Def - Selberg and Ruelle Zeta Functions and the Critical Exponent|critical exponent]]. $N_X(R):=\#\{\gamma\in\mathcal P_X:\ell_\gamma\le R\}$ the geodesic counting function.

---

# Statement

> **Theorem (prime geodesic theorem).** As $R\to\infty$,
> $$N_X(R)=\#\{\gamma\in\mathcal P_X:\ell_\gamma\le R\}\sim\frac{e^{\delta R}}{\delta R}.$$
> The number of primitive closed geodesics of length $\le R$ grows exponentially at rate exactly the critical exponent $\delta$.

---

# Why It's True

**One-line mechanism:** primitive closed geodesics are the "primes" of a hyperbolic surface, and their counting function obeys the same $e^{x}/x$ law as $\pi(x)\sim x/\log x=e^{\log x}/\log x$ for ordinary primes — with "length" playing the role of "log of a prime" and $\delta$ the growth rate. The exponential rate $\delta$ is forced because $\delta$ is *defined* as the proliferation rate of the orbit $\Gamma z$, and closed geodesics are in bijection with primitive conjugacy classes, whose count tracks the orbit.

The proof (not reproduced; see the source) runs through the Selberg zeta function: the geodesics' generating function $Z_X(s)$ has its first singularity at $s=\delta$, and a Tauberian/contour argument converts that analytic fact into the asymptotic count, exactly as the prime number theorem is proved from the Riemann zeta's behaviour at $s=1$.

---

# Where the paper uses this

Corollary 4.7 (finiteness of the total loop mass) reduces to whether $\sum_{\gamma\in\mathcal P_X}e^{-s\ell_\gamma}<\infty$; the prime geodesic theorem gives $N_X(R)\asymp e^{\delta R}/R$, so integrating by parts the sum behaves like $\int^\infty e^{-(s-\delta)R}/R\,dR$, convergent iff $s>\delta$. This is the crux of the finiteness threshold. **[[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.2]]**.

---

# Verified against

Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces*, Ch. 14 (prime geodesic theorem for geometrically finite surfaces, $N_X(R)\sim e^{\delta R}/(\delta R)$); for the cocompact case $\delta=1$ see Buser, *Geometry and Spectra of Compact Riemann Surfaces*, Ch. 9, or Iwaniec, *Spectral Methods of Automorphic Forms*. The exponential rate $\delta$ and the $1/R$ correction match the paper's eq. (40).
