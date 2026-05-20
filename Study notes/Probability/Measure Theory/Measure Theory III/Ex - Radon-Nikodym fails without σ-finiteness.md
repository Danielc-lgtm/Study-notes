---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Radon-Nikodym Theorem"
  - "Def - σ-Finite Measure"
  - "Def - Absolute Continuity and Density"
tags: [analysis, measure-theory]
---

# Problem Statement

On $X=[0,1]$ with the Borel $\sigma$-algebra, let $\mu=\#$ be **counting measure** and $\nu=\lambda$ be Lebesgue measure.

**(a)** Show $\lambda\ll\#$ (absolute continuity holds).

**(b)** Show $\#$ is **not $\sigma$-finite**.

**(c)** Show there is **no** density: no measurable $f\ge0$ with $\lambda(A)=\int_A f\,d\#$ for all Borel $A$. Conclude the $\sigma$-finiteness hypothesis of [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] is necessary.

**Recall:**

[[Thm - Radon-Nikodym Theorem|Radon–Nikodym]]: for **$\sigma$-finite** $\mu,\nu$, $\nu\ll\mu\Rightarrow\nu=f\mu$. Integration against counting measure: $\int_A f\,d\#=\sum_{x\in A}f(x)$.

---

# Convergent Strategy

**Problem class:** demonstrating a hypothesis is necessary by amputation.

**Assumption pattern:** Radon–Nikodym's proof maximises a sub-density and needs $\sigma$-finiteness to assemble finite pieces. Counting measure on the *uncountable* $[0,1]$ has no finite-measure exhaustion — the proof cannot run, and the conclusion genuinely fails.

**Theorem routing:** absolute continuity holds (the only $\#$-null set is $\emptyset$); but a density $f$ against $\#$ would have to satisfy $\sum_{x\in A}f(x)=\lambda(A)$, impossible for a continuous, atomless $\lambda$.

---

# Legal Operations Used

1. **Identify the null sets** of counting measure.
2. **Negate $\sigma$-finiteness** on an uncountable space.
3. **Derive a contradiction** from the putative density's pointwise values.

---

# Hints

> [!note]- Hint 1
> The only $\#$-null set is $\emptyset$ ($\#(A)=0\iff A=\emptyset$). So $\#(A)=0\Rightarrow\lambda(A)=0$ holds trivially — $\lambda\ll\#$.

> [!note]- Hint 2
> A $\#$-finite set is a *finite* set. Can countably many finite sets cover the uncountable $[0,1]$?

> [!note]- Hint 3
> If $\lambda=f\#$, then $0=\lambda(\{x\})=\int_{\{x\}}f\,d\#=f(x)$ for every $x$ — so $f\equiv0$, giving $\lambda\equiv0$, false.

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) observes that $\#(A) = 0 \iff A = \emptyset$, so $\lambda \ll \#$ holds vacuously; Step 2 (part b) negates $\sigma$-finiteness by noting that finite $\#$-measure means literally finite, and a countable union of finite sets cannot cover the uncountable $[0, 1]$; Step 3 (part c) shows a candidate density $f$ must satisfy $f(x) = \lambda(\{x\}) = 0$ for every $x$, hence $f \equiv 0$, contradicting $\lambda([0, 1]) = 1$. The non-obvious move is in Step 3 — testing the density at *singletons* exploits the fact that $\#$ has atoms at every point, which is exactly the structural feature that breaks Radon-Nikodym.

**Step 1 — (a).** For counting measure, $\#(A)=0$ if and only if $A=\emptyset$. So the implication "$\#(A)=0\Rightarrow\lambda(A)=0$" has only the trivial premise $A=\emptyset$, where it holds. Hence $\lambda\ll\#$ — absolute continuity is satisfied.

**Step 2 — (b).** A set of finite $\#$-measure is a *finite* set. If $\#$ were $\sigma$-finite, $[0,1]=\bigcup_k S_k$ with each $S_k$ finite — but a countable union of finite sets is countable, while $[0,1]$ is uncountable. So $\#$ is **not $\sigma$-finite**.

**Step 3 — (c).** Suppose $f\ge0$ measurable with $\lambda(A)=\int_A f\,d\#$ for all Borel $A$. Take $A=\{x\}$ a singleton:
$$0=\lambda(\{x\})=\int_{\{x\}}f\,d\#=f(x).$$
This holds for *every* $x\in[0,1]$, forcing $f\equiv0$. But then $\lambda(A)=\int_A 0\,d\#=0$ for all $A$ — contradicting $\lambda([0,1])=1$. So **no density exists**: $\lambda$ is not $f\#$ for any $f$.

Thus $\lambda\ll\#$ holds, yet the Radon–Nikodym conclusion fails — *because* $\#$ is not $\sigma$-finite. The $\sigma$-finiteness hypothesis is indispensable.

> [!note]- Complete formal solution
> (a) $\#(A)=0\iff A=\emptyset$, so $\lambda\ll\#$ holds vacuously. (b) $\#$-finite $=$ finite; a countable union of finite sets is countable $\neq[0,1]$, so $\#$ is not $\sigma$-finite. (c) A density $f$ would satisfy $f(x)=\lambda(\{x\})/1=0$ for every $x$, so $f\equiv0$ and $\lambda\equiv0$ — false. No density exists; Radon–Nikodym fails without $\sigma$-finiteness. $\blacksquare$

---

# Key Takeaways

**Radon–Nikodym genuinely *requires* $\sigma$-finiteness — absolute continuity alone is not enough.** Counting measure versus Lebesgue measure on $[0,1]$ is the canonical witness: $\lambda\ll\#$ holds (counting measure has no nontrivial null sets), yet $\lambda$ has no density, because a density would be forced to vanish at every point. The reference measure $\#$ being non-$\sigma$-finite is exactly what breaks the theorem's proof (the sub-density maximisation cannot be assembled from finite pieces) and the conclusion.

**The obstruction is the mismatch of *atoms*: $\#$ is purely atomic (every point has mass $1$), $\lambda$ is atomless (every point has mass $0$).** A density re-weights atoms; it cannot manufacture an atomless measure from an atomic one. This is the same structural lesson as [[Ex - The Dirac mass has no density|the Dirac mass]] (an atom has no density with respect to atomless $\lambda$) seen from the other side. Whenever one invokes "*the* Radon–Nikodym derivative" — and hence whenever one constructs a [[Def - Conditional Expectation|conditional expectation]] or a likelihood ratio — $\sigma$-finiteness of the reference measure is being silently used.
