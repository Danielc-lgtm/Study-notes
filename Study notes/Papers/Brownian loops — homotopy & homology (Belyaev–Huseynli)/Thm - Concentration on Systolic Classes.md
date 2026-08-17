---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Probability Measure on Free Homotopy Classes"
  - "Def - Systole"
  - "Thm - Moments of the Length via the Selberg Zeta Function"
tags: [paper, probability, hyperbolic-geometry, zeta-functions]
---

# Notation

- $\mathbb{P}_s$, $\mathbb{E}_s$ — the [[Constr - The Probability Measure on Free Homotopy Classes|probability measure]] on free homotopy classes and its expectation; $s=\tfrac12+\sqrt{\tfrac14+\kappa}$
- $\ell_{\mathrm{sys}}=\min_{\gamma\in\mathcal{P}_X}\ell_\gamma$ — the [[Def - Systole|systole]]; $N_{\mathrm{sys}}=\#\{\gamma\in\mathcal{P}_X : \ell_\gamma=\ell_{\mathrm{sys}}\}\geq2$ its multiplicity
- $L=m\ell_\gamma$ — the length of the geodesic representative; $Z_X(s)$ the Selberg zeta function
- $C=N_{\mathrm{sys}}/(1-e^{-\ell_{\mathrm{sys}}})$ — the constant in the asymptotic

---

# Type card

> [!abstract] Type card — concentration on systolic classes ($s\to\infty$)
> **Given.** The [[Def - Systole|systole]] $\ell_{\mathrm{sys}}$ and its multiplicity $N_{\mathrm{sys}}\geq2$ — at least two because $\mathcal{P}_X$ consists of **oriented** primitive closed geodesics and a hyperbolic element of a torsion-free Fuchsian group is never conjugate to its inverse.
>
> **Produces.** Three limits as $s\to\infty$: $\mathbb{P}_s(\mathcal{C}_X(\gamma))\to1/N_{\mathrm{sys}}$ for each systolic $\gamma$ and $\to0$ for every other class; $\mathbb{E}_s[L]\to\ell_{\mathrm{sys}}$; and the asymptotic $-\log Z_X(s)\sim Ce^{-s\ell_{\mathrm{sys}}}$ with $C=N_{\mathrm{sys}}/(1-e^{-\ell_{\mathrm{sys}}})$, from which **both** $\ell_{\mathrm{sys}}$ and $N_{\mathrm{sys}}$ are recoverable.
>
> **Lets you.** Extract the systole and its multiplicity analytically from the Selberg zeta function, purely from its large-$s$ asymptotics — a geometric quantity read off a spectral one.

---

# Statement

> **Concentration.** As $s\to\infty$ the weights $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))\sim e^{-sm\ell_\gamma}$ are dominated by the primitive classes ($m=1$) whose geodesic realises the systole. Writing
> $$N_{\mathrm{sys}} := \#\big\{\gamma\in\mathcal{P}_X : \ell_\gamma=\ell_{\mathrm{sys}}\big\}\;\geq\;2,$$
> the measure $\mathbb{P}_s$ concentrates on the set of systolic classes and distributes itself uniformly among them:
> $$\mathbb{P}_s\big(\mathcal{C}_X(\gamma)\big)\xrightarrow{\;s\to\infty\;}\frac{1}{N_{\mathrm{sys}}}\quad\text{for each }\gamma\in\mathcal{P}_X\text{ with }\ell_\gamma=\ell_{\mathrm{sys}},$$
> and $\mathbb{P}_s(\mathcal{C}_X(\gamma^m))\to0$ for every other class. Consequently the mean length converges to the systole,
> $$\mathbb{E}_s[L]\xrightarrow{\;s\to\infty\;}\ell_{\mathrm{sys}}.$$

> **The analytic side.** As $s\to\infty$, the dominant contribution to
> $$-\log Z_X(s) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$$
> comes from the $N_{\mathrm{sys}}$ primitive systolic terms, each of order $e^{-s\ell_{\mathrm{sys}}}$, so
> $$-\log Z_X(s)\sim C\,e^{-s\ell_{\mathrm{sys}}},\qquad C=\frac{N_{\mathrm{sys}}}{1-e^{-\ell_{\mathrm{sys}}}}\qquad(s\to\infty),$$
> and both the systole and the multiplicity with which it occurs are recovered from the asymptotics:
> $$\ell_{\mathrm{sys}} = -\lim_{s\to\infty}\frac1s\log\big(-\log Z_X(s)\big),\qquad N_{\mathrm{sys}} = \big(1-e^{-\ell_{\mathrm{sys}}}\big)\lim_{s\to\infty}e^{s\ell_{\mathrm{sys}}}\big(-\log Z_X(s)\big).$$

---

# Why it is true

A sum of exponentials with distinct rates is asymptotically its slowest-decaying terms, and here the rates are the geodesic lengths.

Each class contributes weight of order $e^{-sm\ell_\gamma}$. As $s$ grows, the ratio between any two contributions is $e^{-s(L_1-L_2)}$, which goes to $0$ or $\infty$ according to which length is larger. So all classes are suppressed relative to the shortest ones, and the shortest are the primitive ($m=1$) geodesics of length $\ell_{\mathrm{sys}}$ — note that $m\geq2$ is already suppressed since $m\ell_\gamma\geq2\ell_{\mathrm{sys}}>\ell_{\mathrm{sys}}$. There are $N_{\mathrm{sys}}$ of them, all with identical weight, so the normalised measure spreads uniformly over them.

**The mechanism in one line: the weights are exponentials in $-sL$, so as $s\to\infty$ only the minimal $L$ survives, and since the minimal $L$ is achieved by exactly $N_{\mathrm{sys}}$ classes with equal weight, the limit is uniform on them.**

**Why the limit is not a point mass.** $N_{\mathrm{sys}}\geq2$ always, and the reason is orientation: $\mathcal{P}_X$ consists of *oriented* geodesics, and a hyperbolic element of a torsion-free Fuchsian group is never conjugate to its inverse — a conjugating element would have to reverse the axis, which no orientation-preserving element of a torsion-free discrete group does. So $\gamma$ and $\bar\gamma$ are two distinct classes of the same length. This is a genuine fact about the geometry, not a convention; see [[Def - Systole]].

**The two sides are the same computation.** The probabilistic statement divides by the total mass; the analytic statement is about the total mass itself. The constant $C=N_{\mathrm{sys}}/(1-e^{-\ell_{\mathrm{sys}}})$ comes from summing the $m$-series for a single systolic geodesic — $\sum_{m\geq1}\frac1m\frac{e^{(1-s)m\ell_{\mathrm{sys}}}}{e^{m\ell_{\mathrm{sys}}}-1}\sim\frac{e^{-s\ell_{\mathrm{sys}}}}{1-e^{-\ell_{\mathrm{sys}}}}$ as $s\to\infty$, keeping the $m=1$ term — and multiplying by the multiplicity.

**Recovering the two invariants** is then two limits at different orders. The exponential *rate* gives the systole; having the rate, the *amplitude* gives the multiplicity.

---

# Strategy

**Strategy.** The weights $\sim e^{-sm\ell_\gamma}$ are dominated as $s\to\infty$ by the slowest-decaying terms, which are the primitive classes realising the systole; the probabilistic and the analytic statements are the same computation read on the two sides of the normalisation.

> [!note]- Derivation (skippable)
> **The analytic asymptotic.** For a single $\gamma$, as $s\to\infty$,
> $$\sum_{m\geq1}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1} = \frac{e^{(1-s)\ell_\gamma}}{e^{\ell_\gamma}-1} + O\big(e^{-2s\ell_\gamma}\big) \sim \frac{e^{-s\ell_\gamma}}{1-e^{-\ell_\gamma}},$$
> using $e^{(1-s)\ell}/(e^\ell-1)=e^{-s\ell}/(1-e^{-\ell})$ and that the $m\geq2$ terms decay at rate $2\ell_\gamma$ or faster. Summing over $\gamma$, the terms with $\ell_\gamma>\ell_{\mathrm{sys}}$ are exponentially smaller, so
> $$-\log Z_X(s)\sim\frac{N_{\mathrm{sys}}}{1-e^{-\ell_{\mathrm{sys}}}}e^{-s\ell_{\mathrm{sys}}}.$$
>
> **Recovery of $\ell_{\mathrm{sys}}$.** Taking $\log$ and dividing by $s$: $\frac1s\log(-\log Z_X(s))\to-\ell_{\mathrm{sys}}$.
>
> **Recovery of $N_{\mathrm{sys}}$.** Multiplying by $e^{s\ell_{\mathrm{sys}}}$ and taking the limit gives $C$, and $N_{\mathrm{sys}}=(1-e^{-\ell_{\mathrm{sys}}})C$.
>
> **Concentration.** $\mathbb{P}_s(\mathcal{C}_X(\gamma)) = \mu^\kappa_X(\mathcal{C}_X(\gamma))/(-\log Z_X(s))$; for systolic $\gamma$ the numerator is $\sim e^{-s\ell_{\mathrm{sys}}}/(1-e^{-\ell_{\mathrm{sys}}})$ and the denominator is $N_{\mathrm{sys}}$ times that, giving $1/N_{\mathrm{sys}}$. For any other class the numerator is $o(e^{-s\ell_{\mathrm{sys}}})$ and the ratio tends to $0$.
>
> **The mean.** $\mathbb{E}_s[L]=\sum_{\gamma,m}L\,\mathbb{P}_s(\mathcal{C}_X(\gamma^m))\to\ell_{\mathrm{sys}}\cdot N_{\mathrm{sys}}\cdot\frac{1}{N_{\mathrm{sys}}}=\ell_{\mathrm{sys}}$, the convergence being dominated by the exponential decay of the non-systolic terms. Equivalently, via $\mathbb{E}_s[L]=-(\log F)'(s)$ and $\log F(s)\sim\log C-s\ell_{\mathrm{sys}}$.

---

# What this assumes, and where to climb

**The measure and its normalising constant** — [[Constr - The Probability Measure on Free Homotopy Classes]] and hence [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]].

**The systole and $N_{\mathrm{sys}}\geq2$** — [[Def - Systole]]. The multiplicity bound rests on a hyperbolic element never being conjugate to its inverse in a torsion-free Fuchsian group; **it is the only place in §6 where a genuinely group-theoretic fact is used**, and getting it wrong turns the limit into a point mass.

**The moment formalism**, for the alternative derivation of $\mathbb{E}_s[L]\to\ell_{\mathrm{sys}}$ via $-(\log F)'$ — [[Thm - Moments of the Length via the Selberg Zeta Function]].

**Finiteness of $N_X(R)$**, so that the systole is attained and only finitely many classes compete at each length — [[Def - Critical Exponent and the Prime Geodesic Theorem]].

**Large $s$, hence large $\kappa$.** The whole result is about the deep-killing regime, which sits comfortably inside the convergence region $s>\delta$ since $\delta\leq1$. No delicacy is needed at this end; the delicacy is at $s\downarrow\delta$, which is [[Thm - Finiteness of the Total Mass|Corollary 4.7]]'s territory.

---

# What consumes this

Nothing downstream; this is a terminal result of §6.1.

Its interest is as a **recovery statement**: a geometric invariant — in fact two — extracted from the large-$s$ behaviour of a spectral function. Together with [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] it brackets what the loop measure sees.

---

# Reading it against the rest of the paper

The contrast with §3.4 is the sharpest illustration in the paper of what aggregation costs. [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] inverts the *individual* masses and recovers *every* geodesic length, hence the entire marked length spectrum, hence — by [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] — the whole hyperbolic structure up to isotopy. Here the masses have been summed into one function and normalised; what survives is the shortest length and how many classes achieve it. **Summing discards the marking, normalising discards the scale, and the asymptotics return only the extreme.**

The result is also the paper's clearest instance of a general principle in spectral geometry: **geometric data is recoverable from the asymptotics of a zeta function.** Here $s\to\infty$ returns the systole. At the other end, $s\downarrow\delta$, the total mass blows up and the critical exponent is what governs the rate — so the two ends of the real axis return the shortest geodesic and the exponential growth rate of all of them respectively.
