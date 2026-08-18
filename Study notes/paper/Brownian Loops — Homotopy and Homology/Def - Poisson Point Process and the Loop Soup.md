---
type: definition
subject: probability
prereqs:
  - "Def - Signed and Infinite Measures for Loop Measures"
  - "Def - Brownian Loop Measure"
tags: [probability, point-processes, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$(S,\mathcal S)$ a measurable space (for the paper, $S=C_X$ the loop space); $\Lambda$ a [[Def - σ-Finite Measure|σ-finite measure]] on it, the **intensity**. A **point process** is a random locally-finite collection of points of $S$; for a measurable $A$ with $\Lambda(A)<\infty$, $N_A$ denotes the (random) number of points landing in $A$.

---

# Axiom Motivation

The loop measure $\mu^\phi_X$ assigns a *number* — the mass — to each set of loops, but a number is only an average. To ask distributional questions ("what is the *probability* that at least three loops wind around this handle?", "are the winding counts around two different handles independent?") one needs an actual random collection of loops whose average behaviour is governed by $\mu^\phi_X$. The **Poisson point process** is the canonical such object: from any σ-finite intensity measure it manufactures a random scatter of points in which disjoint regions are independent and each region's count is Poisson with mean equal to its intensity. Feeding the loop measure in as intensity gives the **loop soup** — a random ensemble of loops — and turns every mass computed in §3 into the mean of a Poisson variable (Proposition 3.8).

Two properties characterise the Poisson process and are exactly the two the paper uses. **Poisson counts:** the number of points in a region is Poisson-distributed with mean the region's intensity — so "expected count $=$ intensity" is built in. **Independence over disjoint regions:** counts in disjoint regions are independent — so winding numbers around distinct (disjoint) homotopy classes are automatically independent. Both hold for *any* σ-finite intensity, which is why an infinite-total-mass loop measure is still a legitimate intensity.

---

# The Definition

> **Definition (Poisson point process).** Given a [[Def - σ-Finite Measure|σ-finite measure]] $\Lambda$ on $(S,\mathcal S)$, a **Poisson point process** with intensity $\Lambda$ is a random countable subset $\Pi\subset S$ (formally, a random integer-valued measure $\sum_i\delta_{x_i}$) such that:
> 1. **Poisson counts.** For every measurable $A$ with $\Lambda(A)<\infty$, the count $N_A:=\#(\Pi\cap A)$ is a Poisson random variable of mean $\Lambda(A)$: $\mathbb{P}(N_A=k)=e^{-\Lambda(A)}\Lambda(A)^k/k!$.
> 2. **Independent scattering.** For disjoint measurable $A_1,\dots,A_n$, the counts $N_{A_1},\dots,N_{A_n}$ are independent.
>
> Such a process exists and is unique in law for every σ-finite $\Lambda$.

> **Definition (loop soup).** For a Bernstein $\phi$ (Assumption 2.3) and intensity parameter $c>0$, the **subordinate Brownian loop soup** $\mathcal L_c$ is the Poisson point process on the loop space $C_X$ with intensity measure $c\,\mu^\phi_X$. It is a random countable collection of loops; for any measurable set $A$ of loops with $\mu^\phi_X(A)<\infty$, the number $N_A=\#\{\eta\in\mathcal L_c:\eta\in A\}$ is Poisson with mean $c\,\mu^\phi_X(A)$. (For a jump process, where a homotopy class is not a measurable set of càdlàg loops, one takes the Poisson process of *marked* loops carrying the pair $(B,S)$, on which the class is measurable; see the paper's Remark 3.1.)

**Concrete unpacking.** A one-line worked case: if $\mu^\phi_X(C_X(\gamma))=\lambda$ (the mass in the class of a single wind around $\gamma$), then in the soup $\mathcal L_1$ the number of loops winding once around $\gamma$ is Poisson$(\lambda)$: it is $0$ with probability $e^{-\lambda}$, $1$ with probability $\lambda e^{-\lambda}$, and so on, with mean exactly $\lambda$. If $\gamma'$ is a different geodesic, the count around $\gamma'$ is an independent Poisson variable — even though both counts are read from the same random soup — because $C_X(\gamma)$ and $C_X(\gamma')$ are disjoint sets of loops.

**Standard names.** **Poisson point process** (Poisson random measure); **loop soup** (Lawler–Werner; Le Jan). The mean-equals-intensity and independent-scattering properties are the defining axioms. Reference: Kingman, *Poisson Processes*; Lawler–Werner, *The Brownian loop soup*.

---

# Examples and Non-Examples

**Is an instance.** Points of a homogeneous Poisson process on $\mathbb{R}$ with rate $\lambda$ (intensity $\lambda\,dx$). The Brownian loop soup $\mathcal L_c$ (intensity $c\,\mu_X$).

**Is NOT an instance.** A **binomial** process — a *fixed* number $n$ of i.i.d. points — is **not** Poisson: its total count is deterministic, not Poisson, and disjoint regions are *negatively correlated* (more points here means fewer there). Independence over disjoint sets fails, which is exactly the property Prop 3.8 needs.

**Calibration check.** (1) From axiom 1, verify $\mathbb{E}[N_A]=\Lambda(A)$ and $\operatorname{Var}(N_A)=\Lambda(A)$ (Poisson mean = variance). (2) Check that superimposing two independent Poisson processes with intensities $\Lambda_1,\Lambda_2$ gives a Poisson process with intensity $\Lambda_1+\Lambda_2$. (3) Explain why an infinite-total-mass $\Lambda$ still gives a well-defined process (each finite-mass region is fine; the total need not be).

---

# Where the paper uses this

§3.3 defines the loop soup $\mathcal L_c$ with intensity $c\,\mu^\phi_X$; Proposition 3.8 reads off that the number of soup loops in a free homotopy class $C_X(\gamma^m)$ is Poisson of mean $c\,\mu^\phi_X(C_X(\gamma^m))$ (computed in §3.1), and that counts over distinct classes are independent. §6.2 uses the same structure to get the *distribution* of the total homology of the soup, not just its mean. **[[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.3]]**.

---

# Verified against

Kingman, *Poisson Processes*, Ch. 2–3 (existence for σ-finite intensity, Poisson counts, independent scattering, superposition); Lawler–Werner, *The Brownian loop soup* (Probab. Theory Related Fields, 2004) for the loop-soup construction with intensity $c\,\mu_X$. Standard.
