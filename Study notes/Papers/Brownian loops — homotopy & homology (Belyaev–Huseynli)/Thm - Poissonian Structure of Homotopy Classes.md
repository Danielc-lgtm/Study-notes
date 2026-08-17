---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Subordinate Brownian Loop Measure"
  - "Constr - Loop Mass in a Homotopy Class for Jump Processes"
tags: [paper, probability, loop-soup, poisson-process]
---

# Notation

- $\phi$ — a Bernstein function satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; $\mu^\phi_X$ the [[Constr - The Subordinate Brownian Loop Measure|subordinate Brownian loop measure]] on $\mathcal{C}_X$
- $c>0$ — the intensity of the soup
- $\mathcal{L}_c$ — the **loop soup**: the Poisson point process of loops on $X$ with intensity measure $c\,\mu^\phi_X$; a random countable collection of loops
- $A$ — a measurable set of loops with $\mu^\phi_X(A)<\infty$; $N_A=\#\{\eta\in\mathcal{L}_c : \eta\in A\}$ its count
- $\mathcal{C}_X(\gamma^m)$ — the free homotopy class winding $m$ times around $\gamma\in\mathcal{P}_X$

---

# Type card

> [!abstract] Type card — Proposition 3.8 (Poissonian structure of homotopy classes)
> **Given.** An intensity $c>0$; the loop soup $\mathcal{L}_c$ with intensity measure $c\,\mu^\phi_X$ for a Bernstein function $\phi$ satisfying Assumption 2.3; a primitive closed geodesic $\gamma\in\mathcal{P}_X$ and a winding number $m\geq1$. For jump processes, $\mathcal{L}_c$ is the Poisson point process of **marked** loops carrying the pair $(B,S)$, as in [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]].
>
> **Produces.** A distributional statement: the count of loops of $\mathcal{L}_c$ in $\mathcal{C}_X(\gamma^m)$ is a **Poisson random variable** of mean $c\,\mu^\phi_X(\mathcal{C}_X(\gamma^m))$; and across any finite collection of pairwise distinct classes, these variables are **jointly independent**.
>
> **Lets you.** Upgrade every mass computation of §3 from a statement about an expectation to a statement about a distribution — so that, for instance, the probability that the soup contains no loop in a given class is $\exp(-c\,\mu^\phi_X(\mathcal{C}_X(\gamma^m)))$, an explicit function of $\ell_\gamma$ and $m$ by [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]].

---

# Statement

> **Proposition 3.8 (Poissonian structure of homotopy classes).** For $\gamma\in\mathcal{P}_X$ and $m\geq1$, the number of loops of $\mathcal{L}_c$ in the free homotopy class $\mathcal{C}_X(\gamma^m)$ (for jump processes, of marked loops, as in Remark 3.1) is a Poisson random variable of mean $c\,\mu^\phi_X(\mathcal{C}_X(\gamma^m))$, and for any finite collection of pairwise distinct, hence disjoint, classes these variables are jointly independent.

The construction of the soup itself, following Lawler–Werner and Le Jan: for $c>0$, let $\mathcal{L}_c$ be the Poisson point process of loops on $X$ with intensity measure $c\,\mu^\phi_X$. Thus $\mathcal{L}_c$ is a random countable collection of loops, and for any measurable set $A$ of loops with $\mu^\phi_X(A)<\infty$ the number $N_A := \#\{\eta\in\mathcal{L}_c : \eta\in A\}$ is Poisson with mean $c\,\mu^\phi_X(A)$. The parameter $c$ is the intensity of the soup.

---

# Why it is true

The whole content is that **any $\sigma$-finite measure can serve as the intensity of a Poisson point process**, and $\mu^\phi_X$ is $\sigma$-finite. Once the soup exists, the proposition is the defining property of a Poisson process applied to sets that happen to be homotopy classes.

But the change of viewpoint is worth stating properly, because it is what §6 needs. Before this proposition, $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ is a number: the mass of a class. After it, that number is the *mean of a random variable* — and a random variable has a distribution, moments, tails and joint laws with other random variables. This is what makes it possible to speak of the distribution of a topological quantity rather than only its expectation, which is exactly what [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] does for the total homology of the soup.

**The independence deserves more attention than the Poisson part**, because it is stronger than intuition suggests. Free homotopy classes on a hyperbolic surface are geometrically entangled: geodesics in different classes cross, and the loops realising them share regions of the surface. Yet the counts are *exactly* independent, with no correction. That is not a fact about hyperbolic geometry; it is a fact about Poisson processes, which are independent across disjoint sets no matter how those sets sit in space. **The geometry enters only through the means.**

**The mechanism in one line: distinct free homotopy classes are disjoint, and a Poisson point process is independent across disjoint sets — so all the geometry is in the intensities and none of it is in the dependence structure.**

---

# Strategy

**Strategy.** Distinct free homotopy classes are disjoint measurable sets; both statements are then immediate from the defining properties of a Poisson point process.

> [!note]- Proof (skippable)
> By [[Def - Free Homotopy Class and Conjugacy Class Correspondence|the correspondence]], distinct free homotopy classes correspond to distinct conjugacy classes in $\Gamma$, and conjugacy classes are disjoint. Hence distinct classes are disjoint measurable subsets of $\mathcal{C}_X$ — in the jump case, of the marked loop space.
>
> For a Poisson point process with intensity $c\,\mu^\phi_X$, the count over a measurable set $A$ with $\mu^\phi_X(A)<\infty$ is Poisson of mean $c\,\mu^\phi_X(A)$, and counts over disjoint sets are jointly independent. Applying this with $A=\mathcal{C}_X(\gamma^m)$ gives both assertions. $\;\square$

---

# What this assumes, and where to climb

**$\sigma$-finiteness of $\mu^\phi_X$** — [[Constr - The Subordinate Brownian Loop Measure]]. This is all that is needed for the soup to exist; the infinite total mass is not an obstruction, since a Poisson point process with $\sigma$-finite intensity is perfectly well defined (it has infinitely many points, almost surely, which is the correct picture: the soup contains infinitely many tiny loops).

**Finiteness of $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$**, so that $N_A$ is a genuine Poisson variable rather than almost surely infinite. This holds for every non-trivial non-peripheral class by [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]], whose right-hand side is finite for $L>0$. It fails for the trivial class, whose mass is infinite — and that is the one class the soup contains infinitely many representatives of.

**Measurability of the class** — [[Constr - Loop Mass in a Homotopy Class for Jump Processes]]. In the jump case $\mathcal{C}_X(\gamma^m)$ is not a measurable set of càdlàg loops and there is nothing to count. The repair is to take $\mathcal{L}_c$ to be the Poisson point process of marked loops carrying the pair $(B,S)$, on which the monodromy class *is* measurable and has the same intensity $c\,\mu^\phi_X(\mathcal{C}_X(\gamma^m))$. This convention is inherited silently by §6.2.

---

# What consumes this

- [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] — the direct and essentially only substantive consumer: the total homology $\beta(\lambda)=\sum_{\eta\in\mathcal{L}^*_\lambda}[\eta]$ is a finite sum precisely because $\#\mathcal{L}^*_\lambda$ is Poisson with finite mean $-\lambda\log Z_X(s)$
- [[§3.3 The Loop Soup and its Poissonian Structure]] — the section's sole result
- [[§6 Probability Measures on Homotopy and Homology Classes]] — §6.2 uses the soup and its exponential formula

The tool actually used downstream is not the proposition itself but the **exponential formula** for a Poisson point process: for intensity $\lambda\mu$ and measurable $F$ on loops,
$$\mathbb{E}\Big[\prod_{\eta\in\mathcal{L}_\lambda}e^{F(\eta)}\Big] = \exp\Big(\lambda\int\big(e^{F(\eta)}-1\big)\,\mu(\mathrm{d}\eta)\Big).$$
Proposition 6.7 is this formula with $e^{F(\eta)}=\chi([\eta])$, a unitary character evaluated on the homology class of a loop.

---

# Reading it against the rest of the paper

The loop soup is Lawler–Werner's construction, from *The Brownian loop soup*; the general theory of Poissonian ensembles of Markov loops is Le Jan's. What this paper adds is the observation that the homotopy-class decomposition of §3 makes the soup's *topological* statistics explicitly computable — the means are the closed forms of Theorem 3.5, so questions like "how many loops of the soup wrap the geodesic $\gamma$ exactly once" have answers in terms of $\ell_\gamma$ alone.

The physical reading, from [[§3.2 Euclidean Quantum Mechanics and the Path Integral|§3.2]], is that for $\phi(\lambda)=\lambda+\kappa$ the soup is the loop ensemble of a Euclidean quantum particle in a constant potential $\kappa$, with $\mu^\kappa_X$ its intensity. That makes the soup a physically meaningful object rather than a probabilistic convenience.
