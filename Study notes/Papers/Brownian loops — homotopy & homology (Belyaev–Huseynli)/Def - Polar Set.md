---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs: []
tags: [paper, probability, potential-theory]
---

# Notation

- $P\subset X$ — a Borel set, the candidate polar set
- $\sigma$-ideal — a family of sets closed under subsets and countable unions
- $\kappa\geq0$ — a killing rate; $\phi(\lambda)=\lambda+\kappa$ the corresponding Bernstein function
- $X'=X\setminus P$ — the punctured surface

---

# In plain language

A set is **polar** for a process if the process never hits it — from any starting point, almost surely, at any positive time.

On a Riemann surface, polar for Brownian motion means: zero logarithmic capacity in every local chart. The consequence that matters here is that **every singleton is polar** — planar Brownian motion does not hit points. Since polar sets form a $\sigma$-ideal (closed under subsets and countable unions), every countable set is polar too, and in particular every closed discrete set.

That is the entire content used in §3.4, and it is used for one purpose. If $P$ is polar, then $\mu^\kappa_X$ is supported on loops avoiding $P$; so by [[Constr - The Brownian Loop Measure|restriction]], removing $P$ from $X$ does not change the mass of any class. Puncturing at a discrete set is invisible to the loop measure.

One further point, small but load-bearing: **a killing rate does not change the paths of the process**, only their weight. So for $\phi(\lambda)=\lambda+\kappa$ the polar sets are exactly the Brownian ones. This is why §3.4's statement covers the killing case at no extra cost — and, by contrast, why it does *not* extend to the stable cases, whose paths jump and whose polar sets are genuinely different (a jump process can land on a small set that a diffusion would step over, so stable processes have strictly fewer polar sets).

---

# The definition

> **Definition (polar set).** From the potential theory of Markov processes, a Borel set $P\subset X$ is **polar** for a given process if, from every starting point, the process almost surely never hits $P$ at a positive time.

> **Characterisation for Brownian motion on a Riemann surface.** $P$ is polar for Brownian motion exactly when $P$ has **zero logarithmic capacity in every local chart**. In particular every singleton is polar. Polar sets form a $\sigma$-ideal, being closed under subsets and countable unions, so every countable set is polar.

> **The killing case.** A killing rate does not change the paths of the process, so for $\phi(\lambda)=\lambda+\kappa$ the polar sets are again those of Brownian motion.

The paper takes $P$ to be a **closed discrete** set, hence countable, hence polar.

---

# Types and signatures

- $P\subset X$ — a Borel subset; in §3.4 additionally closed and discrete
- "polar" — a property depending on the **process**, not on $X$ alone; the same set may be polar for one process and not another
- logarithmic capacity — a set function $\mathrm{cap} : \{\text{compact subsets of a chart}\}\to[0,\infty)$; $P$ polar iff $\mathrm{cap}(K)=0$ for every compact $K\subset P$ in every chart
- the polar sets — a $\sigma$-ideal in the Borel $\sigma$-algebra

---

# Example

A single point $\{p\}\subset X$, or any closed discrete set such as an infinite sequence with no accumulation point in $X$. Both are polar for Brownian motion and for Brownian motion with killing, so both are invisible to $\mu^\kappa_X$: the loops that would have hit $P$ form a null set.

**Near-miss non-example.** A smooth curve $\Sigma\subset X$ — say a geodesic arc — is **not** polar: planar Brownian motion hits curves with probability one, and a curve has positive logarithmic capacity. So restriction to $X\setminus\Sigma$ genuinely changes the loop measure: the loops crossing $\Sigma$ are discarded, and they carry positive mass. Cutting along a curve is a real operation on the surface; puncturing at points is not.

**Second near-miss — polarity depends on the process.** For an $\alpha$-stable process with $\alpha$ small, the paths jump and can land anywhere; such processes hit sets that Brownian motion misses, so the polar sets shrink as $\alpha$ decreases. §3.4's statement is therefore restricted to the diffusion cases not by convenience but by necessity — and the paper says so, restricting attention to "the diffusion cases (where homotopy classes make sense)".

---

# Used in this paper at

- [[Thm - Length-Spectrum Identity under Puncturing|Theorem 3.9]] — $P$ is hypothesised non-empty, closed and polar; polarity is what makes $X\setminus P$ carry the same class masses as $X$
- [[§3 Decomposition over Homotopy Classes]] §3.4 — the surviving restriction identity $\mu^\kappa_{X,g}(\mathcal{C}_X(\gamma^m))=\mu^\kappa_{X\setminus P,g}(\mathcal{C}_X(\gamma^m))$
- [[Constr - The Brownian Loop Measure]] — the restriction property is what polarity is combined with

---

# Where this sits in my DAG

Potential theory of Markov processes — hitting probabilities, capacity, polar sets — sits under *Advanced Probability* (🟢) and *SDEs* (🟢), and logarithmic capacity is classical potential theory adjacent to *Complex Analysis*. The paper's reference is Blumenthal–Getoor, *Markov processes and potential theory*.

The specific facts quoted rather than derived: that polar-for-Brownian-motion on a Riemann surface equals zero logarithmic capacity in charts, and that singletons are polar in two dimensions. Both are standard; the second is the familiar statement that planar Brownian motion is neighbourhood-recurrent but point-recurrent only in one dimension.
