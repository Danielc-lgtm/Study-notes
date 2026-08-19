---
type: proposition
subject: probability-geometry
prereqs:
  - "Def - Poisson Point Process and the Loop Soup"
  - "Thm - Mass of a Free Homotopy Class"
  - "Thm - Mass of a Subordinate Brownian Loop Class"
tags: [paper, brownian-loops, point-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Proposition 3.8"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ — geometrically finite hyperbolic surface.
- $\mu^\phi_X$ — the $\phi$-subordinate loop measure on $X$ (Def 2.7 for continuous processes; extended by Rem 3.1 for jump processes); a $\sigma$-finite measure on loop space (finite once one restricts to any non-trivial non-peripheral free homotopy class).
- $c > 0$ — an *intensity constant* (the paper's "concentration" parameter).
- $\mathcal{L}_c$ — the **loop soup** of intensity $c\mu^\phi_X$: a Poisson point process on loop space with intensity measure $c\mu^\phi_X$.
- $C_X(\gamma^m)$ — the free homotopy class of the $m$-fold winding around a primitive geodesic $\gamma\in\mathcal{P}_X$.
- $N_A := \#\{\eta \in \mathcal{L}_c : \eta \in A\}$ — the count of soup loops falling in a measurable set $A$ of loops.

> [!recall]- Poisson point process (PPP) with intensity measure $\mu$
> **Formally:** given a $\sigma$-finite measure space $(E, \mathcal{E}, \mu)$, a **Poisson point process** $\Pi$ on $E$ with intensity $\mu$ is a random countable collection $\{e_1, e_2, \ldots\}\subset E$ (equivalently a random integer-valued measure $\Pi = \sum_i \delta_{e_i}$) such that:
> (i) for every $A\in\mathcal{E}$ with $\mu(A) < \infty$, $N_A := \#\{e_i \in A\}$ is a Poisson random variable of mean $\mu(A)$: $\mathbb{P}(N_A = k) = e^{-\mu(A)}\mu(A)^k/k!$;
> (ii) for pairwise-disjoint $A_1, \ldots, A_n\in\mathcal{E}$, the counts $N_{A_1}, \ldots, N_{A_n}$ are jointly independent.
> **In words:** a random cloud of points in $E$ whose local density is $\mu$ — regions with more $\mu$-mass get proportionally more points on average, and disjoint regions are populated independently. The two axioms (Poisson-count and independent-scattering) uniquely characterise the process.
> **Concretely:** on the half-line $\mathbb{R}_+$ with $\mu = c\cdot\lambda$ (Lebesgue times a constant), the PPP is the classical Poisson process of rate $c$: independent arrivals, exponential inter-arrival times, and the count in $[a,b]$ is $\mathrm{Poisson}(c(b-a))$. On the plane with $\mu$ = uniform measure $\times$ a bounded density, the PPP is a "random scatter of dots" with local intensity given by the density. Replacing "the plane" by "loop space" and "density" by $\mu^\phi_X$ gives the loop soup. Full detail: [[Def - Poisson Point Process and the Loop Soup]].

> [!recall]- Loop soup $\mathcal{L}_c$
> **Formally:** for a $\sigma$-finite loop measure $\mu^\phi_X$ on the space $\mathcal{L}(X)$ of finite-time loops on $X$ and an intensity $c > 0$, the **loop soup** $\mathcal{L}_c$ is the Poisson point process on $\mathcal{L}(X)$ with intensity measure $c\mu^\phi_X$: a random countable collection of loops such that (i) for every measurable set of loops $A$ with $\mu^\phi_X(A) < \infty$, $N_A = \#\{\eta \in \mathcal{L}_c : \eta\in A\}$ is $\mathrm{Poisson}(c\mu^\phi_X(A))$; (ii) counts over disjoint $A$'s are independent.
> **In words:** scatter loops into loop-space at random, drawing each region's population from a Poisson distribution whose mean matches how much mass the loop measure assigns there — one random loop-configuration whose intensity is $c\mu^\phi_X$.
> **Concretely:** on the flat torus $T^2$, the Brownian loop soup at intensity $c = 1$ contains (on average) $\mu_{T^2}(A)$ loops in the class $A$ of "loops that wind $(1,0)$"; if $\mu_{T^2}(A) = 0.5$, the number of such loops in a sample is Poisson(0.5): 0 with probability $e^{-0.5}\approx 0.607$, 1 with probability $0.303$, 2 with probability $0.076$, etc. Full detail: [[Def - Poisson Point Process and the Loop Soup]].

> [!recall]- Free homotopy class $C_X(\gamma^m)$
> **Formally:** an equivalence class of loops on $X$ under *free homotopy* (continuous deformation with the basepoint allowed to move); in bijection with a conjugacy class $[\tau^m]_{\mathrm{conj}}\subset\Gamma$ under the universal-cover monodromy.
> **In words:** "loops that wind around the same holes in the same pattern, no matter where they started"; a single topological "type" of loop.
> **Concretely:** on the once-punctured torus, the class $C_X(\gamma^{(1,0,0)})$ (once around the first handle, zero around the second, zero around the puncture) is disjoint from $C_X(\gamma^{(2,0,0)})$ (twice around the first handle) — the two classes contain no loop in common. See [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] for the mass formula.

> [!recall]- Class-mass $\mu^\phi_X(C_X(\gamma^m))$ is finite
> **Formally:** by [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]], $\mu^\phi_X(C_X(\gamma^m)) = \frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)$ with $L = m\ell_\gamma > 0$; for every Bernstein $\phi$ this is a finite positive number.
> **In words:** each free homotopy class that genuinely wraps at least one hole (not one that just circles a puncture / cusp — a "peripheral" class, whose loops can be shrunk right up to the puncture and so have no shortest length) has finite loop-mass. The divergence of the total loop mass is a "small loop" (contractible class) effect, not present in any class of positive winding.
> **Concretely:** on a genus-2 surface with all geodesic lengths $\ge 1$, the Brownian mass of $C_X(\gamma)$ is $1/(e^{\ell_\gamma} - 1) \le 1/(e - 1) \approx 0.582$, and shrinks exponentially for longer geodesics.

---

# Statement

> **Proposition (Poissonian structure of homotopy classes; Belyaev–Huseynli 3.8).** Let $\mathcal{L}_c$ be the loop soup of intensity $c\mu^\phi_X$ on $X = \Gamma\backslash\mathbb{H}^2$. For every primitive geodesic $\gamma\in\mathcal{P}_X$ and every $m\ge 1$:
> (i) the number of soup loops in the free homotopy class $C_X(\gamma^m)$ (for jump processes, of *marked* loops as in Remark 3.1) is a Poisson random variable of mean $c\,\mu^\phi_X(C_X(\gamma^m))$;
> (ii) for any finite collection $\{(\gamma_1, m_1), \ldots, (\gamma_n, m_n)\}$ of pairwise-distinct pairs (so the classes $C_X(\gamma_i^{m_i})$ are pairwise disjoint), the counts $\{N_{C_X(\gamma_i^{m_i})}\}_{i=1}^n$ are jointly independent.

---

# In One Line

Each closed-form class-mass from §3.1 is literally the *mean* of a Poisson count of soup loops of that type, and winding-number counts around distinct handles are independent — so the loop soup upgrades expectations to *distributions*.

---

# Why It's True

**Mechanism (one sentence).** *Distinct free homotopy classes are pairwise-disjoint measurable subsets of loop space, so the two claims are exactly the Poisson-count and independent-scattering axioms of the defining Poisson point process applied to those subsets.*

There is nothing extra to prove: the Poisson point process is *defined* by the property that count-in-$A$ is Poisson-mean-$\mu(A)$ and counts over disjoint sets are independent. What is (mildly) nontrivial is verifying that:

1. Each $C_X(\gamma^m)$ is a **measurable** set of loops (in the natural $\sigma$-algebra on $\mathcal{L}(X)$).
2. Distinct classes $C_X(\gamma_1^{m_1})$ and $C_X(\gamma_2^{m_2})$ are **disjoint**.
3. Each $\mu^\phi_X(C_X(\gamma^m)) < \infty$ (so the Poisson count is well-defined, not almost-surely infinite).

Item 3 is [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]]. Items 1 and 2 are the standard topological content of "free homotopy class is a $\pi_0$-cell of loop space": free homotopy is an equivalence relation, and its equivalence classes are pairwise disjoint by definition; measurability follows from the fact that the class is determined by the loop's monodromy (a continuous function of the loop into $\Gamma$), and singletons in $\Gamma$'s conjugacy quotient are measurable in loop space.

For jump processes (Bernstein $\phi\ne\lambda$), the "class of a loop" is defined via the marked-loop process — the class is attached to the underlying Brownian arc (Remark 3.1) — and the same three items go through under that definition.

---

# Proof

> [!note]- Gap-free proof
> **Setup.** Let $\mathcal{L}_c$ be the Poisson point process on loop space $\mathcal{L}(X)$ with intensity measure $c\mu^\phi_X$. By definition, $\mathcal{L}_c$ satisfies: for every measurable $A\subseteq\mathcal{L}(X)$ with $\mu^\phi_X(A) < \infty$, the count $N_A := \#\{\eta \in \mathcal{L}_c : \eta \in A\}$ is a Poisson$(c\mu^\phi_X(A))$ random variable; and for disjoint $A_1, \ldots, A_n$, the counts $N_{A_1}, \ldots, N_{A_n}$ are jointly independent.
>
> **Verify: each $C_X(\gamma^m)$ is measurable.** For a continuous loop $\eta\in\mathcal{L}(X)$ rooted at some basepoint, the monodromy $h_\eta\in\Gamma$ is a Borel measurable function of $\eta$ (path lifting is a continuous operation from loop space to $\Gamma$; $\Gamma$ is discrete). Free homotopy classes correspond to conjugacy classes in $\Gamma$; the map $\eta\mapsto[h_\eta]_{\mathrm{conj}}$ is Borel measurable into the (discrete) set of conjugacy classes. So $C_X(\gamma^m) = \{\eta : [h_\eta]_{\mathrm{conj}} = [\tau^m]_{\mathrm{conj}}\}$ is a Borel subset of $\mathcal{L}(X)$. For jump processes, use the marked-loop version (Remark 3.1): the class is attached to the underlying Brownian arc, which is a Borel function of the marked loop, and the argument is identical.
>
> **Verify: distinct classes are disjoint.** Free homotopy is an equivalence relation on loops. Its equivalence classes partition loop space; if $C_X(\gamma_1^{m_1}) \ne C_X(\gamma_2^{m_2})$ (as classes), then they contain no loop in common: any loop in the intersection would be freely homotopic to both $\gamma_1^{m_1}$ and $\gamma_2^{m_2}$, forcing $C_X(\gamma_1^{m_1}) = C_X(\gamma_2^{m_2})$ by transitivity.
>
> **Verify: each $\mu^\phi_X(C_X(\gamma^m))$ is finite.** By [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]], $\mu^\phi_X(C_X(\gamma^m)) = \frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)$ with $L = m\ell_\gamma > 0$; each of $\ell_\gamma$, $\sinh(L/2)$, and $I_\phi(L)$ is a finite positive number (the closed forms of §3.1.1–3.1.4 are explicitly finite).
>
> **(i).** With $A := C_X(\gamma^m)$: $\mu^\phi_X(A) < \infty$, so $N_A$ is Poisson$(c\mu^\phi_X(A)) = \mathrm{Poisson}(c\mu^\phi_X(C_X(\gamma^m)))$.
>
> **(ii).** With $A_i := C_X(\gamma_i^{m_i})$ for pairwise-distinct $(\gamma_i, m_i)$: the $A_i$ are pairwise disjoint (by the equivalence-class disjointness), each has finite mass, so the counts $N_{A_1}, \ldots, N_{A_n}$ are jointly independent by the independence axiom of $\mathcal{L}_c$. $\blacksquare$

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.3]]. Turns each closed-form class-mass of [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] into a *distributional* statement about a random loop configuration. Fed into [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6]] to build a probability measure on homology classes from the loop soup (the Fourier-analysis-of-Poisson-counts identity).
