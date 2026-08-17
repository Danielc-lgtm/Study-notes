---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Selberg Zeta Identity (Killing Case)"
  - "Thm - Finiteness of the Total Mass"
tags: [paper, probability, zeta-functions]
---

# Signature

| symbol | type |
|---|---|
| $\mathcal{C}_X(\gamma^m)$ | ranges over non-trivial non-peripheral free homotopy classes, indexed by $(\gamma,m)\in\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ |
| $\kappa$ | $>0$ throughout §6 |
| $s$ | $=\tfrac12+\sqrt{\tfrac14+\kappa}$; the hypothesis is $s>\delta$ |
| $\mathbb{P}_s$ | a probability measure on $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ |
| $L$ | $\mathcal{P}_X\times\mathbb{Z}_{\geq1}\to(0,\infty)$, $L(\gamma,m)=m\ell_\gamma$ — a **random variable** under $\mathbb{P}_s$ |
| $F$ | $F(s):=-\log Z_X(s)\in(0,\infty)$ — the total mass |

---

# Construction

> **Definition 6.0 (the probability measure).**
> $$\mathbb{P}_s\big(\mathcal{C}_X(\gamma^m)\big):=\frac{\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)}{-\log Z_X(s)}=\frac{\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)}{\sum_{\gamma'\in\mathcal{P}_X}\sum_{m'\geq1}\mu^\kappa_X\big(\mathcal{C}_X(\gamma'^{m'})\big)}.$$

> **(P1) Well-definedness.** Requires $0<\sum_{\gamma,m}\mu^\kappa_X<\infty$: positivity is clear from the closed form, finiteness is [[Thm - Finiteness of the Total Mass|Cor 4.7]] under $s>\delta$, and the value of the denominator is [[Thm - Selberg Zeta Identity (Killing Case)|Cor 4.3]]. *Consumer:* everything in §6.
>
> **(P2) The normalising constant is $-\log Z_X(s)$.** Not an abstract partition function: an explicit zeta value. *Consumer:* [[Thm - Moments of the Length via the Selberg Zeta Function]], where every moment is a derivative of it.
>
> **(P3) $\kappa=0$ is available on a finite-area surface via §5.** There $F(1)=\infty$; the renormalised expressions of [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Thm 5.1]] supply a finite substitute. On an infinite-area surface $\kappa=0$ needs nothing, since $\delta<1$. *Consumer:* the paper's remark; not used computationally.
>
> **(P4) The support is the non-trivial non-peripheral classes.** The contractible class carries infinite mass and is excluded by construction, not by a limiting argument. *Consumer:* [[Thm - Distribution of the Total Homology of the Loop Soup]], where $\mathcal{L}^*_\lambda$ is the corresponding subset of the soup.

> [!warning] $\mathbb{P}_s$ is a measure on **classes**, not on loops
> The underlying set is $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ — a countable set — and $\mathbb{P}_s$ is a discrete probability measure on it. It is *not* the loop measure normalised, which is impossible: $\mu^\kappa_X$ is infinite on the space of loops.

---

# Type card

> [!abstract] Type card — $\mathbb{P}_s$
> **Given.** **(H1)** $X$ geometrically finite hyperbolic. **(H2)** $\kappa>0$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$. **(H3)** $s>\delta$.
>
> **Produces.** A probability measure on the countable set of non-trivial non-peripheral free homotopy classes, with explicit weights $\dfrac{1}{m}\dfrac{e^{(1-s)m\ell_\gamma}}{(e^{m\ell_\gamma}-1)\,(-\log Z_X(s))}$.
>
> **Lets you.** Turn any function of a free homotopy class into a **random variable** with computable moments — and, since the weights are explicit in $\ell_\gamma$, read geometric information (systole, marked length spectrum) off the distribution.

---

# Depends on

- [[Thm - Selberg Zeta Identity (Killing Case)]] — the normalising constant
- [[Thm - Finiteness of the Total Mass]] — (P1)
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — the weights
- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — the index set: every class is $\mathcal{C}_X(\gamma^m)$ for a **unique** $(\gamma,m)$

---

# Consumed by

- [[Thm - Moments of the Length via the Selberg Zeta Function]] — (P2)
- [[Thm - Concentration on Systolic Classes]] — the $s\to\infty$ limit
- [[Constr - The Mass in a Homology Class]] — the pushforward under $(\gamma,m)\mapsto m[\gamma]$
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.1

---

# Commentary

> [!note]- Commentary (skippable)
> Everything before §6 was preparation for this one line. The mass of a class was computed in §3, its summability decided in §4, and the sum evaluated in closed form — so the normalisation is not merely possible but *explicit*, and the partition function is a Selberg zeta value. That explicitness is what makes §6.1 more than a definition: because $\mathbb{P}_s$ depends on $s$ only through $e^{(1-s)L}$, differentiating in $s$ brings down a factor $-L$, and every moment of the length falls out of derivatives of $\log Z_X$.
>
> The paper's stated motivation is geometric: with a canonical weighting of free homotopy classes one can ask for the probability that two independently sampled classes have geodesic representatives that intersect, and similar questions where a natural measure on classes was previously missing. Nothing in §6 pursues that, but it explains the design — the weights are *natural* in the sense of coming from a canonical measure on loops rather than being imposed.
>
> The choice $\kappa>0$ throughout §6 is a simplification, not a restriction of substance: it guarantees $s>1\geq\delta$ in every case at once, so no dichotomy between finite and infinite area needs to be carried through the section.
