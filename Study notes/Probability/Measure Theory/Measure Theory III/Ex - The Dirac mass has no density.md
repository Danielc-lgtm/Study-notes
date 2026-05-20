---
type: exercise
subject: measure-theory
difficulty: "⭐"
prereqs:
  - "Def - Absolute Continuity and Density"
  - "Def - Mutual Singularity"
  - "Thm - Radon-Nikodym Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $\lambda$ be Lebesgue measure on $\mathbb{R}$ and $\delta_0$ the Dirac mass at $0$.

**(a)** Show $\delta_0$ is **not** absolutely continuous with respect to $\lambda$, hence has no [[Def - Absolute Continuity and Density|density]] — there is no $f\ge0$ with $\delta_0(A)=\int_A f\,d\lambda$.

**(b)** Show $\delta_0\perp\lambda$ ([[Def - Mutual Singularity|mutually singular]]).

**(c)** Compute the [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]] of $\nu=\delta_0+g\lambda$ (where $g\ge0$, $g\in L^1$) with respect to $\lambda$, identifying the absolutely continuous and singular parts.

**Recall:**

$\nu\ll\mu$: $\mu(A)=0\Rightarrow\nu(A)=0$. [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]]: $\nu=\nu_{ac}+\nu_s$, $\nu_{ac}\ll\mu$, $\nu_s\perp\mu$.

---

# Convergent Strategy

**Problem class:** recognising the singular extreme — a measure concentrated on a null set.

**Assumption pattern:** $\delta_0$ puts all its mass on $\{0\}$, which is $\lambda$-null. Absolute continuity would forbid exactly this; so $\delta_0$ is the prototype *singular* measure, and a point mass is the prototype obstruction to having a density.

**Theorem routing:** $\lambda(\{0\})=0$ but $\delta_0(\{0\})=1$ violates $\nu\ll\lambda$; $A=\{0\}$ witnesses $\delta_0\perp\lambda$.

---

# Legal Operations Used

1. **Exhibit a $\lambda$-null set of positive $\nu$-measure** to refute absolute continuity.
2. **Exhibit the concentrating set** for mutual singularity.
3. **Read off the decomposition** from the definition.

---

# Hints

> [!note]- Hint 1
> $\lambda(\{0\})=0$ but $\delta_0(\{0\})=1$. Does $\delta_0\ll\lambda$?

> [!note]- Hint 2
> If $\delta_0=f\lambda$, then $1=\delta_0(\{0\})=\int_{\{0\}}f\,d\lambda=0$ — contradiction.

> [!note]- Hint 3
> For (c): $\delta_0$ is singular, $g\lambda$ is absolutely continuous. The decomposition is staring at you.

---

# Solution

The proof breaks into three short steps, one per sub-part. Step 1 (part a) refutes $\delta_0 \ll \lambda$ at the single point $A = \{0\}$, where $\lambda(A) = 0$ but $\delta_0(A) = 1$, and observes that a density would force $1 = \int_{\{0\}} f\, d\lambda = 0$; Step 2 (part b) exhibits mutual singularity by partitioning $\mathbb{R}$ into $\{0\}$ (the support of $\delta_0$) and $\mathbb{R} \setminus \{0\}$ (a set of full $\lambda$-measure that $\delta_0$ ignores); Step 3 (part c) reads off the Lebesgue decomposition of $\nu = \delta_0 + g\lambda$ as $\nu_{ac} = g\lambda$ and $\nu_s = \delta_0$. The single non-obvious move is the recognition that a single $\lambda$-null set is enough to certify both failure of absolute continuity and mutual singularity — there is no need for a complicated test set.

**Step 1 — (a).** $\{0\}$ is a $\lambda$-null set: $\lambda(\{0\})=0$. But $\delta_0(\{0\})=1\neq0$. So absolute continuity $\delta_0\ll\lambda$ — which would require $\lambda(A)=0\Rightarrow\delta_0(A)=0$ — *fails* at $A=\{0\}$. Hence $\delta_0$ has no density: if $\delta_0=f\lambda$ for some $f\ge0$, then $1=\delta_0(\{0\})=\int_{\{0\}}f\,d\lambda=0$, since the integral over a $\lambda$-null set vanishes. Contradiction.

**Step 2 — (b).** Take $A=\{0\}$: $\lambda(A)=0$ and $\delta_0(A^c)=\delta_0(\mathbb{R}\setminus\{0\})=0$. So $\delta_0$ is concentrated on $\{0\}$, $\lambda$ on $\{0\}^c$ — they are [[Def - Mutual Singularity|mutually singular]], $\delta_0\perp\lambda$.

**Step 3 — (c).** For $\nu=\delta_0+g\lambda$: the part $g\lambda$ satisfies $g\lambda\ll\lambda$ (if $\lambda(A)=0$ then $\int_A g\,d\lambda=0$), and $\delta_0\perp\lambda$ by (b). So
$$\nu_{ac}=g\lambda,\qquad\nu_s=\delta_0,\qquad\nu=\underbrace{g\lambda}_{\ll\lambda}+\underbrace{\delta_0}_{\perp\lambda}$$
is the [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]], unique by the theorem. The Radon–Nikodym derivative of the absolutely continuous part is $\mathrm{d}\nu_{ac}/\mathrm{d}\lambda=g$; the singular part $\delta_0$ has *no* derivative.

> [!note]- Complete formal solution
> (a) $\lambda(\{0\})=0\neq1=\delta_0(\{0\})$ refutes $\delta_0\ll\lambda$; a density $f$ would force $1=\int_{\{0\}}f\,d\lambda=0$. (b) $A=\{0\}$: $\lambda(A)=0$, $\delta_0(A^c)=0$, so $\delta_0\perp\lambda$. (c) $g\lambda\ll\lambda$ and $\delta_0\perp\lambda$, so $\nu_{ac}=g\lambda$, $\nu_s=\delta_0$ is the (unique) Lebesgue decomposition. $\blacksquare$

---

# Key Takeaways

**A point mass is the prototype *singular* measure: it concentrates all its mass on a Lebesgue-null set, so it cannot have a density.** Absolute continuity $\nu\ll\lambda$ is precisely the prohibition "$\nu$ puts no mass where $\lambda$ has none"; a Dirac mass violates it at the single point it lives on. This is why discrete distributions (atoms) have no probability density function with respect to Lebesgue measure — only the absolutely continuous distributions do.

**Every measure splits, uniquely, into an absolutely continuous part (which *has* a density) and a singular part (which does not) — the [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]].** For a mixed measure $\delta_0+g\lambda$ the split is read off by inspection; in general the [[Thm - Radon-Nikodym Theorem|theorem]] guarantees and the [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]] computes it (the density is $\lim_r\nu(B(x,r))/\lambda(B(x,r))$, finite a.e. for the a.c. part, $+\infty$ on the singular part's support). In probability this is the classification of a distribution into *atomic* + *singular-continuous* + *absolutely continuous* parts.
