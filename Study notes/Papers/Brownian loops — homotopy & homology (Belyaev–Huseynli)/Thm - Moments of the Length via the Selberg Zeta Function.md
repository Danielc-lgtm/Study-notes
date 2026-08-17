---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Probability Measure on Free Homotopy Classes"
  - "Def - Selberg Zeta Function"
tags: [paper, probability, zeta-functions]
---

# Notation

- $\mathbb{P}_s$, $\mathbb{E}_s$, $\mathrm{Var}_s$ — the [[Constr - The Probability Measure on Free Homotopy Classes|probability measure]] on free homotopy classes and its moments; $\kappa>0$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}>\delta$
- $L:=m\ell_\gamma$ — the length of the geodesic representative, as a random variable under $\mathbb{P}_s$
- $F(s):=-\log Z_X(s)$ — the total mass as a function of $s$; $F^{(n)}$ its $n$-th derivative
- $r>1-s$ — the tilting parameter

---

# Type card

> [!abstract] Type card — moments of $L$ under $\mathbb{P}_s$
> **Given.** $F(s):=-\log Z_X(s)$ for $s>\delta$, the [[Constr - The Probability Measure on Free Homotopy Classes|measure $\mathbb{P}_s$]], and a tilting parameter $r>1-s$.
>
> **Produces.** The tilting identity and **all moments at once**: $\mathbb{E}_s[e^{-rL}] = \log Z_X(s+r)/\log Z_X(s)$ and $\mathbb{E}_s[L^n]=(-1)^nF^{(n)}(s)/F(s)$ for $n\geq1$; together with the first two cumulants as first and second derivatives of $\log F$.
>
> **Lets you.** Read every moment of the geodesic length off the Selberg zeta function and its derivatives, with **no geometric input beyond it** — no genus, no individual geodesic, no counting function.

---

# Statement

> **The tilting identity.** For every $r>1-s$,
> $$\mathbb{E}_s\big[e^{-rL}\big] = \frac{\sum_{\gamma,m}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)e^{-rm\ell_\gamma}}{-\log Z_X(s)} = \frac{-\log Z_X(s+r)}{-\log Z_X(s)} = \frac{\log Z_X(s+r)}{\log Z_X(s)},\tag{70}$$
> because the summand at parameter $s$ multiplied by $e^{-rm\ell_\gamma}$ is exactly the summand at parameter $s+r$.

> **All moments.** Writing $F(s):=-\log Z_X(s)$, the identity (69) gives $\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))(m\ell_\gamma)^n = (-1)^nF^{(n)}(s)$, and hence
> $$\mathbb{E}_s\big[L^n\big] = \frac{(-1)^nF^{(n)}(s)}{F(s)},\qquad n\geq1.\tag{71}$$

> **The first two cumulants.** For the mean,
> $$\mathbb{E}_s[L] = -\frac{\mathrm{d}}{\mathrm{d}s}\log\big(-\log Z_X(s)\big) = -\frac{F'(s)}{F(s)} = -\frac{Z'_X(s)}{Z_X(s)\log Z_X(s)},\tag{72}$$
> and for the variance,
> $$\mathrm{Var}_s(L) = \frac{\mathrm{d}^2}{\mathrm{d}s^2}\log\big(-\log Z_X(s)\big) = \frac{F''(s)F(s)-F'(s)^2}{F(s)^2} = \frac{Z_XZ''_X-(Z'_X)^2}{\log Z_X}-\frac{(Z'_X)^2}{Z_X^2\log^2Z_X}.\tag{73}$$

**In particular $\log F$ is strictly convex on $(1,\infty)$, so $s\mapsto\mathbb{E}_s[L]$ is strictly decreasing: increasing the killing rate shortens the typical class, as expected.**

---

# Why it is true

One observation generates everything, and it is worth isolating because it is the entire content.

**The mass depends on $s$ only through $e^{(1-s)m\ell_\gamma}$**, so
$$\frac{\mathrm{d}}{\mathrm{d}s}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = -(m\ell_\gamma)\,\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big).$$
Differentiating in $s$ *is* multiplying by $-L$. So the operator $-\mathrm{d}/\mathrm{d}s$ acts on the unnormalised weights exactly as multiplication by the random variable $L$ acts, and $n$-fold differentiation of the total mass $F(s)$ produces the $n$-th unnormalised moment. Dividing by $F(s)$ normalises. That is (71).

Rather than treat each moment separately, note the stronger statement: **shifting the spectral parameter is the same as tilting by the length.** Multiplying the summand at $s$ by $e^{-rm\ell_\gamma}$ gives literally the summand at $s+r$, so the exponential moment $\mathbb{E}_s[e^{-rL}]$ is a ratio of total masses at two parameters. That is (70), and it contains (71) by differentiating in $r$ at $r=0$.

**The mechanism in one line: $\{\mathbb{P}_s\}$ is an exponential family with natural parameter $s$, sufficient statistic $L$ and partition function $F(s)=-\log Z_X(s)$, so cumulants are derivatives of $\log F$ and moments are ratios of derivatives of $F$.**

Once seen this way §6.1 needs no memorisation. The mean is $-(\log F)'$, the variance is $(\log F)''$, and the strict convexity of $\log F$ — which is just the statement that a variance is positive — gives the monotonicity of $\mathbb{E}_s[L]$ for free. **Killing suppresses long loops, so raising $\kappa$ lowers the typical length; the analytic face of that is convexity of the cumulant generating function.**

The condition $r>1-s$ is exactly what keeps $s+r>1$, hence in the region where $Z_X(s+r)$ is defined by its convergent product; it is a convergence condition on the tilt, nothing more.

---

# Strategy

**Strategy.** The summand at parameter $s$ multiplied by $e^{-rm\ell_\gamma}$ is exactly the summand at parameter $s+r$; that single observation gives the tilting identity, and differentiating $F$ repeatedly gives the moments.

> [!note]- Derivation (skippable)
> **The mass depends on $s$ via $e^{(1-s)m\ell_\gamma}$**, so differentiating,
> $$\frac{\mathrm{d}}{\mathrm{d}s}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = -(m\ell_\gamma)\,\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big).\tag{69}$$
>
> **The tilting identity.** For $r>1-s$,
> $$\mathbb{E}_s\big[e^{-rL}\big] = \frac{\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))\,e^{-rm\ell_\gamma}}{-\log Z_X(s)}.$$
> The numerator's summand is $\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}e^{-rm\ell_\gamma} = \frac1m\frac{e^{(1-(s+r))m\ell_\gamma}}{e^{m\ell_\gamma}-1}$, which is the summand of $-\log Z_X(s+r)$ by (32). Hence (70).
>
> **All moments.** Iterating (69), $\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))(m\ell_\gamma)^n=(-1)^nF^{(n)}(s)$, and dividing by $F(s)$ gives (71).
>
> **Cumulants.** $\mathbb{E}_s[L]=-F'(s)/F(s)=-(\log F)'(s)$, which with $F=-\log Z_X$ gives $F'=-Z'_X/Z_X$ and hence (72). Differentiating once more, $\mathrm{Var}_s(L)=\mathbb{E}_s[L^2]-\mathbb{E}_s[L]^2=\frac{F''}{F}-\frac{(F')^2}{F^2}=(\log F)''$, giving (73).
>
> **Monotonicity.** $(\log F)''=\mathrm{Var}_s(L)>0$, so $\log F$ is strictly convex on $(1,\infty)$ and $\mathbb{E}_s[L]=-(\log F)'$ is strictly decreasing.

---

# What this assumes, and where to climb

**The measure $\mathbb{P}_s$ and its normalising constant** — [[Constr - The Probability Measure on Free Homotopy Classes]], hence [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] and [[Thm - Finiteness of the Total Mass|Corollary 4.7]].

**The explicit $s$-dependence of the mass**, $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$ — [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]], §3.1.2. **Everything here depends on the mass being an exponential in $s$ with exponent linear in $L$**; a mass with any other $s$-dependence would break the exponential-family structure entirely.

**$s>\delta$ and $s+r>\delta$** — [[Def - Critical Exponent and the Prime Geodesic Theorem]], for convergence of both $F(s)$ and $F(s+r)$. The stated condition $r>1-s$ is the version of this used in the paper.

**Term-by-term differentiation under the sum**, justified by local uniform convergence of the series for $s>\delta$ — the terms are positive and decay exponentially in $\ell_\gamma$ with a rate bounded below on compacts.

---

# What consumes this

- [[Thm - Concentration on Systolic Classes]] — the $s\to\infty$ asymptotics of $\mathbb{E}_s[L]$, whose limit is $\ell_{\mathrm{sys}}$
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.1

---

# Reading it against the rest of the paper

Set this beside [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] to see what aggregation costs. There, the *individual* masses are inverted to recover the *individual* geodesic lengths — the full marked length spectrum, hence by [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] the whole hyperbolic structure. Here, the masses have been summed into a single function $F(s)$, and what is recoverable is only what $F$ knows: its derivatives, hence the moments of $L$, hence (in the $s\to\infty$ limit) the systole and its multiplicity. **Normalising to a probability measure discards the scale, and summing discards the marking; what remains is one function of one variable and everything it encodes.**

The exponential-family reading also explains the paper's stated motivation. Wanting "the probability of intersections of closed geodesics" means wanting the law of some functional of a random class; if that functional is a function of $L$, the tilting identity computes it. Functionals that are not functions of $L$ — intersection numbers among them — are not reached by §6.1, and §6.2's homology grouping is the paper's move towards them.
