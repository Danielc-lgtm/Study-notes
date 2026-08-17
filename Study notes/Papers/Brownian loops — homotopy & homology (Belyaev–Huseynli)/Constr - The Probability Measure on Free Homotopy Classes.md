---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Selberg Zeta Identity (Killing Case)"
  - "Thm - Finiteness of the Total Mass"
tags: [paper, probability, zeta-functions]
---

# Notation

- $\kappa>0$ — the killing rate; $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, assumed $>\delta$
- $\mu^\kappa_X$ — the killing loop measure; $Z_X(s)$ the [[Def - Selberg Zeta Function|Selberg zeta function]]
- $\mathbb{P}_s$ — the probability measure on non-trivial non-peripheral free homotopy classes; $\mathbb{E}_s$, $\mathrm{Var}_s$ its moments
- $L=m\ell_\gamma$ — the length of the geodesic representative, regarded as a random variable
- $F(s):=-\log Z_X(s)$ — the total mass as a function of the spectral parameter

---

# In plain language

Divide the masses by their sum.

That is the whole construction, and everything before it in the paper was making the division legal. The masses $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ are non-negative; by [[Thm - Finiteness of the Total Mass|Corollary 4.7]] they sum to a finite number when $s>\delta$; and by [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] that number is $-\log Z_X(s)$. So the normalised weights are a genuine probability measure on the set of non-trivial non-peripheral free homotopy classes, and its normalising constant is a named object.

**Why the resulting measure is natural rather than merely available.** Two reasons, and the second is the one that makes §6.1 work. Its normalising constant is $-\log Z_X(s)$, the object of Corollary 4.3. And because the masses depend on $s$ only through $e^{(1-s)m\ell_\gamma}$, differentiating in $s$ is the same as multiplying by $-L$ — so the family $\{\mathbb{P}_s\}$ is an **exponential family** with $s$ as natural parameter, $L$ as sufficient statistic, and $F(s)=-\log Z_X(s)$ as partition function. Every cumulant of $L$ is then a derivative of $\log F$, and every moment a ratio of derivatives of $F$. That structure is [[Thm - Moments of the Length via the Selberg Zeta Function|the whole of §6.1]].

The paper's stated motivation: an explicit weighting per class allows one to better understand the geometry of the surface — for instance the probability of intersections of closed geodesics. Having every such question reduce to a derivative of one function is what makes that tractable.

---

# The construction

> **Construction (the probability measure on free homotopy classes).** With all the finiteness conditions established, normalise the mass of Brownian loop measure to form a probability measure on free homotopy classes:
> $$\mathbb{P}_s\big(\mathcal{C}_X(\gamma^m)\big) := \frac{\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)}{-\log Z_X(s)} = \frac{\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)}{\sum_{\gamma'\in\mathcal{P}_X}\sum_{m'\geq1}\mu^\kappa_X\big(\mathcal{C}_X(\gamma'^{m'})\big)},\qquad s=\tfrac12+\sqrt{\tfrac14+\kappa},$$
> where throughout §6 the killing rate is $\kappa>0$.

The $\kappa=0$ case can also be treated, using the renormalised expressions of §5.

Under $\mathbb{P}_s$ each homotopy class is assigned a probability proportional to its mass under the loop measure, and any function of the class becomes a random variable. The most natural one is the length $L:=m\ell_\gamma$ of the geodesic representative, whose expectation, variance and moments are computed on [[Thm - Moments of the Length via the Selberg Zeta Function]].

---

# Type card

> [!abstract] Type card — the probability measure $\mathbb{P}_s$
> **Given.** A killing rate $\kappa>0$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ satisfying $s>\delta$, so that [[Thm - Finiteness of the Total Mass|Corollary 4.7]] gives a finite total mass and [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] identifies it as $-\log Z_X(s)$.
>
> **Produces.** A genuine probability measure $\mathbb{P}_s$ on the countable set of non-trivial non-peripheral free homotopy classes — equivalently on $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$. Total mass exactly $1$; atoms at every class; no continuous part.
>
> **Lets you.** Turn any function of a free homotopy class into a random variable with computable moments, and in particular make the geodesic length $L$ a random variable whose every cumulant is a derivative of $\log(-\log Z_X)$.

---

# Properties relied on later

**The exponential-family structure.** The mass depends on $s$ only through $e^{(1-s)m\ell_\gamma}$, so
$$\frac{\mathrm{d}}{\mathrm{d}s}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = -(m\ell_\gamma)\,\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big).\tag{69}$$
**Differentiating in $s$ is multiplying by $-L$.** This single identity generates every result in §6.1: the tilting identity $\mathbb{E}_s[e^{-rL}]=\log Z_X(s+r)/\log Z_X(s)$, all moments $\mathbb{E}_s[L^n]=(-1)^nF^{(n)}(s)/F(s)$, and the first two cumulants as derivatives of $\log F$.

**The support is the non-trivial non-peripheral classes only.** The trivial class has infinite mass and is excluded; peripheral classes have no geodesic representative and are excluded. So $\mathbb{P}_s$ lives on $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$, and $L$ is well defined on its support. See [[Def - Geometrically Finite Surfaces, Cusps and Funnels]].

**Monotonicity in $s$.** $\log F$ is strictly convex on $(1,\infty)$, so $s\mapsto\mathbb{E}_s[L]$ is strictly decreasing: **increasing the killing rate shortens the typical class.** This is what one would expect — killing suppresses long loops — and it is the qualitative check that the normalisation behaves sensibly.

**Concentration as $s\to\infty$.** The weights $\sim e^{-sm\ell_\gamma}$ become dominated by the shortest classes, so $\mathbb{P}_s$ concentrates on the systolic ones. See [[Thm - Concentration on Systolic Classes]].

**Dependence on $\kappa$ is genuine.** $\mathbb{P}_s$ is a *family* of measures, not a single canonical one; different killing rates give genuinely different weightings, and the family is the object with structure. Sending $s\to\infty$ or $s\downarrow\delta$ explores its two extremes: concentration on the systole at one end, and — since the total mass blows up at $\delta$ — spreading over ever longer classes at the other.

---

# Consumed by

- [[Thm - Moments of the Length via the Selberg Zeta Function]] — the moments of $L$ under $\mathbb{P}_s$, all at once via the tilting identity
- [[Thm - Concentration on Systolic Classes]] — the $s\to\infty$ limit, recovering $\ell_{\mathrm{sys}}$ and $N_{\mathrm{sys}}$
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.1 — the construction and its consequences

The homology analogue of §6.2 is **not** built by normalising this measure. [[Constr - The Mass in a Homology Class]] groups the same masses by homology class rather than dividing them, and the resulting $\mu^\kappa_X(\beta)$ is a mass, not a probability. The two constructions are parallel, not nested.

---

# Where this sits in my DAG

Two theorems above it and nothing else: [[Thm - Selberg Zeta Identity (Killing Case)]] for the closed form of the normalising constant, and [[Thm - Finiteness of the Total Mass]] for the fact that it is finite. Both reduce through §3 and §4 to the anchors already recorded on [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes]].

The probability content is elementary: normalising a summable family of non-negative weights, and the exponential-family formalism of natural parameter, sufficient statistic and cumulant generating function — *Advanced Probability* (🟢) and *Theoretical Statistics*. Nothing here needs a further page.
