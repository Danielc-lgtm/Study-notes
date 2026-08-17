---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Character Torus and the Pontryagin Dual"
  - "Thm - Selberg Zeta Identity (Killing Case)"
tags: [paper, probability, homology, loop-measures]
---

# Notation

- $\beta\in H_1(X,\mathbb{Z})$ — a homology class; $[\gamma]$ the image of $\gamma\in\mathcal{P}_X$ under $\Gamma\twoheadrightarrow H_1(X,\mathbb{Z})$, so $[\gamma^m]=m[\gamma]$
- $\kappa$ — the killing rate; $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$
- $\mu^\kappa_X(\beta)$ — the mass of the Brownian loop measure with killing in the homology class $\beta$
- $\chi$ — a unitary character of $H_1(X,\mathbb{Z})$; $L_X(s,\chi)$ the [[Def - Selberg L-Function|Selberg L-function]]

---

# In plain language

Group the homotopy-class masses by homology class and add them up.

The homotopy-class decomposition of §3 is a very fine partition of the loop measure by topology: two loops contribute to the same term exactly when they are freely homotopic. Homology is much coarser. For a surface of genus $g\geq2$ the fundamental group $\pi_1(X)\cong\Gamma$ is **non-abelian**, and a free homotopy class — a conjugacy class in $\Gamma$ — retains non-abelian information such as the order in which different handles are traversed, up to conjugation. Passing to homology, the abelianisation, discards all of that and records only the net winding around each cycle.

The consequence is that the sum defining $\mu^\kappa_X(\beta)$ is **infinite**: a fixed homology class collects contributions from infinitely many distinct free homotopy classes, and there is no closed form for the sum. That is the problem §6.2 exists to solve, and it solves it by Fourier analysis on the character torus rather than by evaluating the sum directly — see [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]].

**Why one would want the homology grouping at all.** The paper gives a concrete reason: **intersections of closed geodesics.** Geometric intersection numbers are well defined on free homotopy classes, but *algebraic* intersection numbers are defined on homology classes. So questions about signed intersection counts live at the homology level, and need a measure there.

The technical reason the $L$-function works is a one-line observation. In the logarithmic expansion of $L_X(s,\chi)$ the weight is $\chi([\gamma])^m$, and whenever $m[\gamma]=\beta$,
$$\chi([\gamma])^m = \chi(m[\gamma]) = \chi(\beta),$$
so **the weight depends only on the homology class of the iterate $\gamma^m$, not on the particular geodesic representative.** That is exactly what licenses regrouping the double sum by homology class.

---

# The construction

> **Definition 6.1 (mass of Brownian loop measure in a homology class).** For $\beta\in H_1(X,\mathbb{Z})$ and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$, the mass of the Brownian loop measure with killing in homology class $\beta$ is
> $$\mu^\kappa_X(\beta) := \sum_{\substack{\gamma\in\mathcal{P}_X,\ m\geq1\\ m[\gamma]=\beta}}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = \sum_{\substack{\gamma\in\mathcal{P}_X,\ m\geq1\\ m[\gamma]=\beta}}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.\tag{74}$$

Via the Hurewicz theorem one writes $\Gamma\twoheadrightarrow H_1(X,\mathbb{Z})$ for the abelianisation map and $[\gamma]$ for the image in homology of an oriented primitive closed geodesic $\gamma\in\mathcal{P}_X$; in particular $[\gamma^m]=m[\gamma]$. Grouping the loop measure by homology class amounts to summing the homotopy-class contributions $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ over all pairs $(\gamma,m)$ for which $[\gamma^m]$ equals a fixed $\beta$.

---

# Type card

> [!abstract] Type card — Definition 6.1 (mass in a homology class)
> **Given.** A homology class $\beta\in H_1(X,\mathbb{Z})$, and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$.
>
> **Produces.** A non-negative number $\mu^\kappa_X(\beta)$, defined as an **infinite** sum over the homotopy classes lying above $\beta$; finite because it is a sub-sum of the total mass, which [[Thm - Finiteness of the Total Mass|Corollary 4.7]] bounds. **No closed form is available directly.**
>
> **Lets you.** Ask homological questions — in particular about *algebraic* intersection numbers, which unlike geometric intersection numbers are defined on homology classes rather than free homotopy classes.

---

# Properties relied on later

**Finiteness.** $\mu^\kappa_X(\beta)$ is a sub-sum of $\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=-\log Z_X(s)$, which is finite for $s>\delta$ by [[Thm - Finiteness of the Total Mass|Corollary 4.7]], and all terms are non-negative. So every $\mu^\kappa_X(\beta)$ is finite and $\sum_\beta\mu^\kappa_X(\beta)=-\log Z_X(s)$ — **the homology masses partition the total mass.** This is what makes the Fourier expansion of Theorem 6.5 absolutely convergent.

**The character weight depends only on $\beta$.** Whenever $m[\gamma]=\beta$,
$$\chi([\gamma])^m = \chi(m[\gamma]) = \chi(\beta),$$
so the double sum in the $L$-function expansion (76) may be regrouped by homology class. **This is the entire mechanism of §6.2**, and it is why a *character* rather than any other weight is used.

**The Fourier pair.** By Theorem 6.5, $\beta\mapsto\mu^\kappa_X(\beta)$ and $\chi\mapsto-\log L_X(s,\chi)$ are a Fourier pair on $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ and its dual torus. The expansion direction is $-\log L_X(s,\chi)=\sum_\beta\chi(\beta)\mu^\kappa_X(\beta)$; the inversion direction computes $\mu^\kappa_X(\beta)$ as one integral over the compact torus.

**Not a probability measure.** Unlike $\mathbb{P}_s$ of §6.1, the homology masses are **not** normalised in the paper. They sum to $-\log Z_X(s)$ and one could divide, but §6.2 does not; the objects of interest are the masses themselves and the law of the loop soup's total homology.

---

# Consumed by

- [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]] — $\mu^\kappa_X(\beta)$ is the Fourier coefficient in both the expansion and the inversion formula
- [[Thm - Selberg L-Function Identity|Corollary 6.4]] — the identity whose regrouping by homology gives Theorem 6.5
- [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] — the pointwise law $\mathbb{P}(\beta(\lambda)=\beta)$ is obtained by the same inversion
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.2

---

# Where this sits in my DAG

The homology side is *Algebraic Topology* (🔵): the abelianisation map is [[Def - Hurewicz Map]] and [[Thm - Hurewicz Theorem (Statement)]] in the vault, and the rank computation is on [[Def - Character Torus and the Pontryagin Dual]]. The mass formula is [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] and §3.1.2 upstream; finiteness is [[Thm - Finiteness of the Total Mass|Corollary 4.7]].

> [!note] Remark 6.2 — attribution
> The first definition of Brownian loop measure in homology classes appeared, to the authors' knowledge, in Le Jan's *Markov paths, loops and fields*. The definition there was initially unclear to them owing to differing conventions and techniques, so they developed theirs independently, and have since found that the methods of §6.2 — in particular invoking the Selberg $L$-function — provide a **dual approach**, recovering Le Jan's results in greater generality, for instance extending to the non-compact case.
