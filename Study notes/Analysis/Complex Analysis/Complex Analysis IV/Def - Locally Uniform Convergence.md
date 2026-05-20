---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is an open set, $f_n : U \to \mathbb{C}$ for $n \in \mathbb{N}$ is a sequence of functions, $f : U \to \mathbb{C}$ is a function. We write $f_n \to f$ locally uniformly on $U$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Axiom Motivation

Uniform convergence is a strong notion: $f_n \to f$ uniformly on $U$ means $\sup_U |f_n - f| \to 0$. This is too strong for many natural situations in complex analysis — for instance, the partial sums of a power series $\sum z^n$ converge to $1/(1 - z)$ on the open disc $|z| < 1$ but *not uniformly* on the full disc (the convergence breaks down as $|z| \to 1$).

Yet for the purposes of complex analysis, we want a notion of convergence that:
(a) implies the limit is holomorphic when each $f_n$ is, and
(b) allows differentiating term-by-term (or otherwise commuting limits with calculus operations).

These two desiderata are satisfied by **locally uniform convergence**: $f_n \to f$ uniformly on every *compact subset* of $U$. The local uniform structure is exactly what is needed: locally (on small discs), the convergence is uniform, so Cauchy-integral-formula-style arguments commuting limits with integrals go through; globally, the topology of $U$ may prevent uniform convergence, but this doesn't matter because complex analysis is fundamentally local.

The "compact subset" formulation is equivalent to: for every $z_0 \in U$, there is a neighborhood $V \ni z_0$ on which $f_n \to f$ uniformly. The two are interchangeable because every compact subset is contained in such a finite union of neighborhoods, and every closed disc inside $U$ is compact.

This notion is the natural convergence for holomorphic function spaces. It corresponds to the *compact-open topology* on $C(U, \mathbb{C})$, which makes the space of holomorphic functions on $U$ a Fréchet space. All the major theorems of complex function theory — Vitali, Montel, Hurwitz, Riemann mapping — use locally uniform convergence as the basic notion.

What would break with a weaker definition? Pointwise convergence: doesn't preserve holomorphicity (limits of holomorphic functions pointwise need not be holomorphic, even continuous — think of pointwise limits of Lebesgue measurable functions). Convergence in $L^p$: also doesn't preserve holomorphicity in the obvious way.

What would break with a stronger definition? Uniform convergence on all of $U$: too restrictive; the power series example above shows that natural holomorphic sequences fail it.

---

# The Definition

Let $U \subseteq \mathbb{C}$ be open. A sequence of functions $f_n : U \to \mathbb{C}$ converges **locally uniformly** to $f : U \to \mathbb{C}$ if either of the following equivalent conditions holds:

**(i) Compact-set formulation.** For every compact $K \subset U$, $f_n \to f$ uniformly on $K$:
$$\sup_{z \in K}|f_n(z) - f(z)| \to 0 \text{ as } n \to \infty.$$

**(ii) Neighborhood formulation.** For every $z_0 \in U$, there exists a neighborhood $V \subset U$ of $z_0$ on which $f_n \to f$ uniformly:
$$\forall z_0 \in U,\ \exists V \ni z_0,\ \sup_V|f_n - f| \to 0.$$

Equivalence: (i) ⟹ (ii) by taking $V$ to be any closed disc around $z_0$ inside $U$ (compact). (ii) ⟹ (i) by compactness: cover the compact $K$ by finitely many neighborhoods on which convergence is uniform, take the max of the errors.

---

# Relate to Other Fields / Compression

In **topology**, locally uniform convergence is the **compact-open topology** on the function space $C(U, \mathbb{C})$. The compact-open topology has as a subbase $\{\phi : \phi(K) \subset V\}$ for $K$ compact and $V$ open; convergence in this topology is exactly locally uniform convergence (or, equivalently, uniform on compact sets). This is the "right" topology for many problems in topology and analysis where the relevant structure is local.

In **functional analysis**, the space of holomorphic functions $H(U)$ with locally uniform convergence is a **Fréchet space**: complete, locally convex, metrizable. The seminorms are $\|f\|_K = \sup_K |f|$ for $K$ compact, and locally uniform convergence is convergence with respect to all these seminorms simultaneously.

In **probability theory**, locally uniform convergence is the analog of **convergence in distribution on bounded sets** or **convergence in probability on compact sets**. The general principle "convergence on compact sets is enough" appears repeatedly: tightness arguments, weak convergence of measures restricted to compact sets, etc.

In **PDE**, locally uniform convergence of solutions to elliptic equations is the natural notion: the compactness theorems (Arzelà–Ascoli, Rellich-Kondrachov) work on compact subsets.

---

# Examples / Corollaries

**Is an instance — partial sums of a power series.** $\sum_{n=0}^N z^n \to 1/(1 - z)$ locally uniformly on $|z| < 1$. On the closed disc $|z| \leq r < 1$, the convergence is uniform by the standard radius-of-convergence argument; every compact subset of the open unit disc is contained in some such closed disc. Yet *uniform convergence on the full open disc $|z| < 1$ fails*: the supremum $\sup_{|z| < 1}|f_n(z) - f(z)| = \sup_{|z| < 1}|z^{n+1}/(1 - z)|$ is infinite (taking $z$ close to $1$).

**Is an instance — $(1 + z/n)^n \to e^z$ on $\mathbb{C}$.** On every compact $K \subset \mathbb{C}$, $(1 + z/n)^n \to e^z$ uniformly (by Taylor expansion and uniform bounds on $K$). So this convergence is locally uniform on $\mathbb{C}$. Used in [[Ex - Limit of nonvanishing functions]].

**Is NOT an instance — $z^n$ on the unit disc.** $z^n \to 0$ pointwise on $|z| < 1$, but on the boundary $|z| = 1$, $|z^n| = 1$ does not converge. On the open disc $|z| < 1$: locally uniform convergence to $0$ holds (on $|z| \leq r < 1$, $|z^n| \leq r^n \to 0$ uniformly). So this *is* locally uniform on $|z| < 1$, just not uniform.

**Is NOT an instance — $\sin(nz)$.** Does not converge locally uniformly anywhere (the values oscillate wildly).

**Is an instance — $\sum 1/(n^2 + z^2)$.** Locally uniform convergence on $\mathbb{C}\setminus\{\pm i, \pm 2i, \ldots\}$: on any compact set avoiding these points, the tail of the series is bounded by $\sum 1/n^2$, providing uniform Cauchy.

**Corollary — locally uniform limit is continuous.** If $f_n$ are continuous and $f_n \to f$ locally uniformly on $U$, then $f$ is continuous on $U$. Local uniformity is enough because continuity is a local property.

**Corollary — Cauchy criterion.** A sequence $f_n$ is locally uniformly Cauchy iff it is locally uniformly convergent (when the codomain is complete, which $\mathbb{C}$ is). So local uniform convergence is testable without knowing the limit.

**Calibration check.** Verify that the partial sums of $\sum z^n$ converge to $1/(1-z)$ *locally uniformly* on $|z| < 1$ but *not uniformly*, because the error $|z|^{n+1}/(1-z)$ blows up as $z \to 1$ within the disc. Verify that pointwise convergence is strictly weaker — for instance $\sin(nz)$ on $\mathbb{R}$ converges nowhere, but even where pointwise limits exist, holomorphicity need not be preserved. And verify that locally uniform convergence is exactly the *compact-open topology* on $C(U, \mathbb{C})$, the seminorm topology with one seminorm per compact subset — the same Fréchet structure that makes the space of holomorphic functions on $U$ a complete topological vector space.

---

# Unlocked by This

> [!tip] Limit of Holomorphic is Holomorphic *(from §3.6)*
> The cornerstone theorem [[Thm - Locally Uniform Limit of Holomorphic is Holomorphic|locally uniform limits of holomorphic functions are holomorphic]] is what makes this convergence the "right" notion for complex analysis.

> [!tip] Hurwitz's Theorem *(from §3.6)*
> [[Thm - Hurwitz's Theorem|Hurwitz's theorem]] (limit of nonvanishing is either zero or nonvanishing) uses locally uniform convergence.

> [!tip] Montel's Theorem and Normal Families *(from Mapping Theory)*
> A family $\mathcal{F}$ of holomorphic functions on $U$ is a **normal family** if every sequence in $\mathcal{F}$ has a locally uniformly convergent subsequence. Montel's theorem characterizes normal families by *local boundedness*, and is the key input to the Riemann mapping theorem proof.
