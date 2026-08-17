---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Poissonian Structure of Homotopy Classes"
  - "Thm - Selberg L-Function Identity"
  - "Thm - Fourier Expansion and Inversion by Homology Class"
tags: [paper, probability, homology, loop-soup]
---

# Notation

- $\lambda>0$ — the intensity of the loop soup $\mathcal{L}_\lambda$; $\mathcal{L}^*_\lambda$ its loops that are non-contractible and not homotopic into a cusp
- $\beta(\lambda):=\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]\in H_1(X,\mathbb{Z})$ — the **total homology** of the loop soup
- $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$; $Z_X$, $L_X(s,\chi)$ the Selberg zeta and $L$-functions
- $\chi\in\widehat{H_1(X,\mathbb{Z})}$ — a unitary character; $\mathrm{d}\chi$ normalised Haar measure
- $L_X(s,\chi)^{-\lambda}:=\exp(-\lambda\log L_X(s,\chi))$ — the complex power, defined via the expansion (76)

---

# Type card

> [!abstract] Type card — Proposition 6.7 (distribution of the total homology)
> **Given.** $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$; the [[Thm - Poissonian Structure of Homotopy Classes|loop soup]] $\mathcal{L}_\lambda$ of intensity $\lambda>0$; and $\beta(\lambda):=\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]$, the total homology of the non-contractible, non-cusp-homotopic loops. The sum is finite, since $\#\mathcal{L}^*_\lambda$ is Poisson with finite mean $\lambda\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=-\lambda\log Z_X(s)$.
>
> **Produces.** The characteristic function on the character torus, $\mathbb{E}[\chi(\beta(\lambda))]=(Z_X(s)/L_X(s,\chi))^\lambda$; and the pointwise law $\mathbb{P}(\beta(\lambda)=\beta)$ as a single torus integral.
>
> **Lets you.** Describe the **full distribution** of a random homology class built from a Poissonian ensemble of loops, in closed form. This is the strongest statement in the paper, and the one that most clearly justifies having built a *measure* on loops rather than a family of expectations.

---

# Statement

> **Proposition 6.7 (distribution of the total homology of the loop soup).** Let $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}(s)>\delta$, let $\mathcal{L}_\lambda$ be the loop soup of intensity $\lambda>0$, and let
> $$\beta(\lambda) := \sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]\;\in\;H_1(X,\mathbb{Z})$$
> be the total homology of the loop soup, where $\mathcal{L}^*_\lambda$ denotes the loops of $\mathcal{L}_\lambda$ that are non-contractible and not homotopic into a cusp. The sum is finite, since $\#\mathcal{L}^*_\lambda$ is Poisson with finite mean $\lambda\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=-\lambda\log Z_X(s)$. Then for every unitary character $\chi\in\widehat{H_1(X,\mathbb{Z})}$,
> $$\mathbb{E}\big[\chi(\beta(\lambda))\big] = \left(\frac{Z_X(s)}{L_X(s,\chi)}\right)^{\lambda},\tag{80}$$
> and consequently, for each $\beta\in H_1(X,\mathbb{Z})$,
> $$\mathbb{P}\big(\beta(\lambda)=\beta\big) = Z_X(s)^\lambda\int_{\widehat{H_1(X,\mathbb{Z})}}L_X(s,\chi)^{-\lambda}\,\overline{\chi(\beta)}\,\mathrm{d}\chi,\tag{81}$$
> where $\mathrm{d}\chi$ is the normalised Haar measure on $\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^r$, and the complex powers are defined via $L_X(s,\chi)^{-\lambda}:=\exp(-\lambda\log L_X(s,\chi))$ with $\log L_X(s,\chi)$ given by (76).

---

# Why it is true

The exponential formula for a Poisson point process, applied with the character as the multiplicative functional. Everything then falls out of identities already proved.

**Setting it up.** $\beta(\lambda)$ is a **sum over a random collection of loops**, so $\chi(\beta(\lambda))$ — the character being a homomorphism — is a **product** over that collection:
$$\chi\big(\beta(\lambda)\big) = \chi\Big(\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]\Big) = \prod_{\eta\in\mathcal{L}^*_\lambda}\chi\big([\eta]\big).$$
A product over a Poisson process is exactly what the exponential formula computes.

**The exponential formula.** For a Poisson process of intensity $\lambda\mu$ and measurable $F$ on loops,
$$\mathbb{E}\Big[\prod_{\eta\in\mathcal{L}_\lambda}e^{F(\eta)}\Big] = \exp\Big(\lambda\int\big(e^{F(\eta)}-1\big)\,\mu(\mathrm{d}\eta)\Big).$$
Applying it with $e^{F(\eta)}=\chi([\eta])$ turns the expectation into $\exp\big(\lambda\sum_{\gamma,m}(\chi([\gamma])^m-1)\mu^\kappa_X(\mathcal{C}_X(\gamma^m))\big)$ — and the two halves of that sum are recognisable. The $\chi([\gamma])^m$ half is $-\log L_X(s,\chi)$ by [[Thm - Selberg L-Function Identity|Corollary 6.4]]; the $-1$ half is $+\log Z_X(s)$ by the same corollary at the trivial character. Exponentiating gives (80).

**The mechanism in one line: the character turns a random sum of homology classes into a random product over the soup, the exponential formula turns that product into an exponential of a $(\chi-1)$-weighted total mass, and the Selberg $L$-function identity — applied at $\chi$ and at $\mathbf{1}$ — evaluates both halves.**

**The pointwise law.** (80) says $\chi\mapsto\mathbb{E}[\chi(\beta(\lambda))]$ is the characteristic function of $\beta(\lambda)$ on the character torus. Inverting a characteristic function on a compact abelian group is the same multiply-and-integrate manoeuvre as in [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]]: multiply by $\overline{\chi(\beta)}$, integrate, and orthogonality isolates the atom at $\beta$. That is (81).

**Why the $-1$ matters.** The exponential formula computes $\mathbb{E}[\prod(e^{F}-1+1)]$ in effect — the subtraction is what makes the integral converge, since $\chi([\eta])-1$ vanishes on the trivial class where the mass is infinite. Structurally, it is why the answer is a **ratio** $Z_X/L_X$ rather than $1/L_X$: the trivial-character term supplies the denominator's normalisation.

---

# Strategy

**Strategy.** Apply the exponential formula for a Poisson point process with $e^{F(\eta)}=\chi([\eta])$, so the product over the soup becomes $\chi(\beta(\lambda))$; recognise the two resulting sums as the Selberg $L$-function identity applied to $\chi$ and to the trivial character. Then multiply by $\overline{\chi(\beta)}$, integrate over the torus, and use orthogonality.

> [!note]- Proof (skippable)
> For a Poisson process of intensity $\lambda\mu^\kappa_X$ and any measurable $F$ on loops, the exponential formula gives
> $$\mathbb{E}\Big[\prod_{\eta\in\mathcal{L}_\lambda}e^{F(\eta)}\Big] = \exp\Big(\lambda\int\big(e^{F(\eta)}-1\big)\,\mu^\kappa_X(\mathrm{d}\eta)\Big).$$
> Apply this with $e^{F(\eta)}=\chi([\eta])$ for $\eta\in\mathcal{L}^*_\lambda$, so that $\prod_\eta e^{F(\eta)}=\chi\big(\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]\big)=\chi(\beta(\lambda))$. The right-hand side is
> $$\exp\left(\lambda\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\big(\chi([\gamma])^m-1\big)\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)\right) = \exp\Big(-\lambda\log L_X(s,\chi)+\lambda\log Z_X(s)\Big) = \left(\frac{Z_X(s)}{L_X(s,\chi)}\right)^\lambda,$$
> by [[Thm - Selberg L-Function Identity|Corollary 6.4]] applied to $\chi$ and to the trivial character. This proves (80).
>
> Multiplying by $\overline{\chi(\beta)}$ and integrating over $\widehat{H_1(X,\mathbb{Z})}$, orthogonality of characters isolates the class $\beta$ and gives (81). $\;\square$

---

# What this assumes, and where to climb

**The loop soup and the exponential formula** — [[Thm - Poissonian Structure of Homotopy Classes]]. The exponential formula is the anchor tool from *Advanced Probability* (🟢), and it is the only probabilistic input.

**Finiteness of $\#\mathcal{L}^*_\lambda$**, so that $\beta(\lambda)$ is a finite sum and well defined. This is a Poisson count with mean $-\lambda\log Z_X(s)$, finite by [[Thm - Finiteness of the Total Mass|Corollary 4.7]] under $\operatorname{Re}(s)>\delta$. **Note the exclusions in $\mathcal{L}^*_\lambda$ are exactly the classes with infinite or undefined mass** — contractible loops and loops homotopic into a cusp — so the restriction is forced.

**Corollary 6.4, twice** — [[Thm - Selberg L-Function Identity]], once at $\chi$ and once at $\mathbf{1}$.

**Orthogonality of characters and Haar measure** — [[Def - Character Torus and the Pontryagin Dual]].

**The marked-space convention in the jump case.** For a process with jumps, $[\eta]$ is not defined on a càdlàg path; the soup is taken to be the process of marked loops carrying $(B,S)$, as in [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]] and Proposition 3.8. The paper's §6 works throughout with killing, so the diffusion case, but the convention is inherited.

**The complex power** $L_X(s,\chi)^{-\lambda}=\exp(-\lambda\log L_X(s,\chi))$ is defined via the expansion (76) rather than by a branch choice — which is well posed precisely because the expansion converges absolutely in the region considered.

---

# What consumes this

Nothing. This is the terminal result of §6 and of the paper's probabilistic strand.

---

# Reading it against the rest of the paper

**This is the result that justifies the whole construction.** §2 built a measure on loops rather than a probability; §3.3 observed that a $\sigma$-finite measure can be a Poisson intensity; §3 computed the masses; §4 summed them; §6.2 sorted them by homology. The payoff is here: a random homology class, built from a Poissonian ensemble of Brownian loops, has a characteristic function in closed form and a pointwise law given by one torus integral. **No step of that chain works with a probability measure on paths** — the loop measure has to be a measure, and it has to be $\sigma$-finite rather than finite, for the soup to exist at all.

Compare the two payoffs of §6. §6.1 gives every moment of the geodesic *length* as a derivative of $-\log Z_X$; §6.2 gives the full law of the total *homology* as a Fourier integral of $L_X^{-\lambda}$. Both are complete answers, and they are answers about different structures on the same index set — length ordering in one case, group structure in the other.

The physical reading, from [[§3.2 Euclidean Quantum Mechanics and the Path Integral|§3.2]], is worth carrying to the end: for $\phi(\lambda)=\lambda+\kappa$ the soup is the loop ensemble of a Euclidean quantum particle in a constant potential $\kappa$. So (81) is a statement about the distribution of the total winding of that ensemble around the handles of $X$ — a physically meaningful quantity with a closed-form law.
