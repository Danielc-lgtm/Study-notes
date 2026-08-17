---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Probability Measure on Free Homotopy Classes"
  - "Def - Systole"
tags: [paper, probability, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $\ell_{\mathrm{sys}}$ | $=\min_{\gamma\in\mathcal{P}_X}\ell_\gamma$ |
| $N_{\mathrm{sys}}$ | $=\#\{\gamma\in\mathcal{P}_X:\ell_\gamma=\ell_{\mathrm{sys}}\}\geq2$ — [[Def - Systole\|(F4)]] |
| $\mathbb{P}_s$ | the probability measure on classes; $s\to\infty$ |
| $C$ | $=\dfrac{N_{\mathrm{sys}}}{1-e^{-\ell_{\mathrm{sys}}}}$ |

---

# Type card

> [!abstract] Type card — §6.1 concentration
> **Given.** **(H1)** $X$ geometrically finite hyperbolic, $\mathbb{P}_s$ as constructed. **(H2)** $s\to\infty$ (equivalently $\kappa\to\infty$).
>
> **Produces.** Three limits:
> $$\mathbb{P}_s\big(\mathcal{C}_X(\gamma)\big)\xrightarrow[s\to\infty]{}\frac{1}{N_{\mathrm{sys}}}\ \ \text{for each systolic }\gamma;\qquad \mathbb{P}_s\big(\mathcal{C}_X(\gamma^m)\big)\to0\ \text{otherwise};\qquad \mathbb{E}_s[L]\to\ell_{\mathrm{sys}},$$
> together with the analytic shadow $-\log Z_X(s)\sim Ce^{-s\ell_{\mathrm{sys}}}$ and the two recovery formulas
> $$\ell_{\mathrm{sys}}=-\lim_{s\to\infty}\frac1s\log\big(-\log Z_X(s)\big),\qquad N_{\mathrm{sys}}=\big(1-e^{-\ell_{\mathrm{sys}}}\big)\lim_{s\to\infty}e^{s\ell_{\mathrm{sys}}}\big(-\log Z_X(s)\big).$$
>
> **Lets you.** Read the systole and its multiplicity off the large-$s$ asymptotics of the Selberg zeta function — and, equivalently, off the loop measure.

---

# Statement

> **§6.1 (concentration on systolic classes).** Assume (H1),(H2). As $s\to\infty$ the measure $\mathbb{P}_s$ concentrates on the systolic classes and distributes itself uniformly among them:
> $$\mathbb{P}_s\big(\mathcal{C}_X(\gamma)\big)\longrightarrow\frac{1}{N_{\mathrm{sys}}}\quad(\ell_\gamma=\ell_{\mathrm{sys}}),\qquad \mathbb{P}_s\big(\mathcal{C}_X(\gamma^m)\big)\longrightarrow0\ \ \text{for every other class},$$
> and consequently $\mathbb{E}_s[L]\to\ell_{\mathrm{sys}}$. On the analytic side $-\log Z_X(s)\sim Ce^{-s\ell_{\mathrm{sys}}}$ with $C=N_{\mathrm{sys}}/(1-e^{-\ell_{\mathrm{sys}}})$, whence the two recovery formulas above.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces\|(26)]] | large $s$ | $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))\sim\frac1m\frac{e^{-sm\ell_\gamma}}{1-e^{-m\ell_\gamma}}$, decay rate $e^{-sL}$ |
| minimisation of $L=m\ell_\gamma$ | over $(\gamma,m)$ | minimum at $m=1$, $\ell_\gamma=\ell_{\mathrm{sys}}$, attained $N_{\mathrm{sys}}$ times |
| [[Def - Systole\|(F4)]] | orientations | $N_{\mathrm{sys}}\geq2$, so the limit is never a point mass |
| [[Thm - Selberg Zeta Identity (Killing Case)\|Cor 4.3]] | the normalising constant | $-\log Z_X(s)\sim N_{\mathrm{sys}}\frac{e^{-s\ell_{\mathrm{sys}}}}{1-e^{-\ell_{\mathrm{sys}}}}$ |
| [[Thm - Moments of the Length via the Selberg Zeta Function\|(e)]] | monotonicity | $\mathbb{E}_s[L]$ decreases to its limit, which must then be $\ell_{\mathrm{sys}}$ |

---

# Proof

**Strategy.** Every weight decays like $e^{-sL}$; the smallest $L$ wins, and the smallest $L$ is $\ell_{\mathrm{sys}}$, attained by exactly the $N_{\mathrm{sys}}$ primitive systolic classes.

> [!note]- Proof (skippable)
> Write the weight as $\frac1m\frac{e^{-sL}}{1-e^{-L}}$ with $L=m\ell_\gamma$ (using $\frac{e^{(1-s)L}}{e^L-1}=\frac{e^{-sL}}{1-e^{-L}}$, an exact identity, not an approximation). For fixed $X$ the set of values $\{L\}$ is discrete with minimum $\ell_{\mathrm{sys}}$, attained precisely at $m=1$ and $\ell_\gamma=\ell_{\mathrm{sys}}$ — $N_{\mathrm{sys}}$ classes in all. Each such class has weight $\frac{e^{-s\ell_{\mathrm{sys}}}}{1-e^{-\ell_{\mathrm{sys}}}}$; every other class has weight $O(e^{-sL'})$ with $L'>\ell_{\mathrm{sys}}$ strictly.
>
> Summing, $-\log Z_X(s)=\sum_{\gamma,m}\frac1m\frac{e^{-sL}}{1-e^{-L}}\sim N_{\mathrm{sys}}\frac{e^{-s\ell_{\mathrm{sys}}}}{1-e^{-\ell_{\mathrm{sys}}}}=Ce^{-s\ell_{\mathrm{sys}}}$. Dividing a systolic weight by this gives $\to1/N_{\mathrm{sys}}$; any other weight divided by it gives $\to0$. Then $\mathbb{E}_s[L]\to\ell_{\mathrm{sys}}$ since the mass concentrates on classes of that length.
>
> Inverting the asymptotic: $\frac1s\log(-\log Z_X(s))\to-\ell_{\mathrm{sys}}$ gives the first recovery formula, and $e^{s\ell_{\mathrm{sys}}}(-\log Z_X(s))\to C$ with $C=N_{\mathrm{sys}}/(1-e^{-\ell_{\mathrm{sys}}})$ gives the second. $\;\square$

---

# What this assumes, and where to climb

- **$\ell_{\mathrm{sys}}>0$ attained, with finite multiplicity** — [[Def - Systole|(F1)]], hence [[Ext - Prime Geodesic Theorem|(PGT)(F1)]]. On an infinite-type surface with $\ell_{\mathrm{sys}}=0$ the statement is false as written.
- **$N_{\mathrm{sys}}\geq2$** — [[Def - Systole|(F4)]]: $\mathcal{P}_X$ consists of *oriented* geodesics and a hyperbolic element is never conjugate to its inverse. So the limiting measure is never a point mass; it is uniform on at least two classes.
- **The domination of the tail** — needs a gap between $\ell_{\mathrm{sys}}$ and the next value of $L$, which holds by discreteness of the length spectrum.
- **Not assumed:** anything about $Z_X$ beyond its Euler product in $\{\mathrm{Re}(s)>\delta\}$; $s\to\infty$ stays inside it.
- **The measure** — [[Constr - The Probability Measure on Free Homotopy Classes]]; the limit is taken in its parameter $s$.

---

# Consumed by

- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.1
- Nothing else; it is a terminal statement of §6.1.

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the weights are $e^{-sL}$ up to bounded factors, so as $s\to\infty$ the measure becomes uniform on the argmin of $L$.** This is zero-temperature limit behaviour and the answer is the ground state — here, the systolic classes.
>
> What makes it more than a formality is the pair of recovery formulas. They say the systole and its multiplicity are visible in the **large-$s$ asymptotics of $-\log Z_X$** alone: take a logarithm and divide by $s$ for the length, then strip the exponential for the count. Since $-\log Z_X(s)$ is the total loop mass, the same two numbers are visible in the loop measure without ever looking at an individual geodesic.
>
> The contrast with [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] is the useful one. There, the masses *class by class* determine the whole marked length spectrum, hence — by [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] — the surface. Here the masses are *summed* first, and what survives is only $(\ell_{\mathrm{sys}},N_{\mathrm{sys}})$. The two results bracket exactly what aggregation costs: everything except the ground state.
