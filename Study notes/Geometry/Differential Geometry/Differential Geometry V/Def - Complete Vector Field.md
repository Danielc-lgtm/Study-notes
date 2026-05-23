---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Integral Curve of a Vector Field"
  - "Def - Flow of a Vector Field"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth manifold, $X \in \mathfrak{X}(M)$ a smooth [[Def - Smooth Vector Field|vector field]]. $\phi^X : \mathcal{D} \to M$ is the maximal smooth flow of $X$, with flow domain $\mathcal{D} \subseteq \mathbb{R} \times M$ open and $\mathcal{D}^{(p)} = \{t : (t, p) \in \mathcal{D}\}$ the open interval through $0$ giving the time of existence of the integral curve starting at $p$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] for the full notation registry.

---

# Axiom Motivation

After the Fundamental Theorem on Flows ([[Thm - Fundamental Theorem on Flows]]), every smooth vector field has a unique maximal flow, but this flow is in general only *local*: its domain $\mathcal{D}$ is an open subset of $\mathbb{R} \times M$, possibly strictly smaller than $\mathbb{R} \times M$. The question "for which vector fields is the flow defined for all time?" is the question of **completeness**, and the definition records the answer.

The single condition to capture is: **every maximal integral curve is defined for all $t \in \mathbb{R}$.** This is equivalent to $\mathcal{D}^{(p)} = \mathbb{R}$ for every $p$, equivalent to $\mathcal{D} = \mathbb{R} \times M$, equivalent to $\phi^X$ being a *global* flow. Failure of completeness is always the same phenomenon: some integral curve **escapes** — to infinity, through a removed point, or out of a compact set — in finite time. The escape lemma (Lee 9.19) makes this precise: a maximal integral curve with finite right endpoint leaves every compact subset of $M$.

Why do we need this notion at all? Because the cleanest version of every flow theorem — the [[Thm - Commuting Flows Theorem]], the construction of one-parameter subgroups of $\mathrm{Diff}(M)$, the assignment $v \mapsto \phi^X_1(p)$ as a smooth function of $v$ — requires the flow to be defined for $t = \pm 1$ at least, ideally for all $t$. So we identify the class of vector fields for which the theory has its cleanest statements and call them complete.

The two sufficient conditions to remember are:

1. **Compact support.** If $\operatorname{supp} X = \overline{\{p : X_p \neq 0\}}$ is compact, then $X$ is complete (see [[Ex - Compactly Supported Vector Fields are Complete]]). The proof uses a uniform-time lemma: by compactness of the support, there is a single $\varepsilon > 0$ such that every integral curve through a point of the support exists at least on $(-\varepsilon, \varepsilon)$, and outside the support the field is zero so integral curves are constant. Patching these together gives existence for all time.

2. **Compact manifold.** Every smooth vector field on a compact manifold has compact support (it equals all of $M$), so every smooth vector field on a compact manifold is complete.

The two non-examples to keep:

1. **Escape to infinity on a non-compact manifold.** $X = x^2 \partial_x$ on $\mathbb{R}$ has integral curve $\gamma(t) = x_0 / (1 - t x_0)$, blowing up at $t = 1/x_0$ for $x_0 > 0$.

2. **Escape through a hole.** $X = \partial_x$ on $\mathbb{R}^2 \setminus \{0\}$: the integral curve starting at $(1, 0)$ runs along the $x$-axis and would hit the removed origin at $t = -1$. The maximal interval is $(-1, +\infty)$, not $\mathbb{R}$.

The definition is binary: a vector field is either complete or it is not. Quantifying *how complete* — what is the largest interval of existence, how does it vary with $p$ — is the business of the maximal flow theorem, not of this definition.

Why pick this specific condition and not, say, "every integral curve through every point of a compact set is defined for all $t$"? Because the cleaner definition (every maximal integral curve is global) is what matches the cleanest theorems. And because completeness is *automatic* under the standard sufficient conditions; in practice one almost never needs to verify the definition directly — one verifies compact support or compactness of $M$, and completeness follows.

---

# The Definition

A smooth vector field $X \in \mathfrak{X}(M)$ is **complete** if its maximal flow $\phi^X : \mathcal{D} \to M$ has flow domain $\mathcal{D} = \mathbb{R} \times M$; equivalently, $\mathcal{D}^{(p)} = \mathbb{R}$ for every $p \in M$; equivalently, every maximal integral curve of $X$ is defined for all $t \in \mathbb{R}$.

When $X$ is complete, $\{\phi^X_t\}_{t \in \mathbb{R}}$ is a **one-parameter group of diffeomorphisms** of $M$: each $\phi^X_t : M \to M$ is a diffeomorphism, with $\phi^X_0 = \mathrm{id}_M$ and $\phi^X_t \circ \phi^X_s = \phi^X_{t+s}$ for all $s, t \in \mathbb{R}$.

---

# Relate to Other Fields / Compression

In ordinary differential equations, completeness is the property "the autonomous ODE has solutions for all time, regardless of initial condition". On $\mathbb{R}^n$ the most useful sufficient condition is **sublinear growth**: $|X(x)| \leq C(1 + |x|)$ implies completeness, because the linear growth gives a Grönwall bound preventing finite-time blowup. Superlinear growth like $|X(x)| \sim |x|^2$ permits blowup, as in the standard example.

In dynamical systems and physics, completeness is the property that the time-evolution is globally defined — a basic requirement for any physical theory of time evolution that purports to apply at all times. Hamiltonian systems with bounded energy and conservative forces are usually complete; systems with finite-time singularities (gravitational collapse, geodesic incompleteness in general relativity) are not, and the incompleteness is a physically meaningful statement.

**True name:** A vector field is complete if and only if its **integral curves never escape** — they remain in $M$ for all $t \in \mathbb{R}$, never leaving via an asymptote to infinity, never hitting a removed point, never running out of space.

---

# Examples / Corollaries

**Is an instance: any smooth vector field on a compact manifold.** Every vector field has compact support (the support is contained in the compact manifold), so completeness follows from the support criterion. Examples: every vector field on $S^n$, on $T^n$, on a compact Lie group, on $\mathbb{RP}^n$.

**Is an instance: $\partial/\partial x$ on $\mathbb{R}^n$.** Linear growth (in fact, constant growth), so complete; the flow is $\phi_t(x_1, \dots, x_n) = (x_1 + t, x_2, \dots, x_n)$, defined for all $t$.

**Is an instance: $-y \partial_x + x \partial_y$ on $\mathbb{R}^2$.** The rotation field, with flow $\phi_t(x, y) = (x \cos t - y \sin t,\, x \sin t + y \cos t)$. Bounded on every compact set; integral curves are circles, which are bounded, so they cannot escape. Complete.

**Is an instance: any compactly supported smooth vector field.** See [[Ex - Compactly Supported Vector Fields are Complete]]: bumping a vector field by a compactly supported cutoff produces a complete field that agrees with the original on a smaller set.

**Is an instance: every left-invariant vector field on a Lie group.** A consequence of the homogeneity (left translation is a diffeomorphism that takes the integral curve from $e$ to the integral curve from $g$): if the integral curve from $e$ exists on $(-\varepsilon, \varepsilon)$, it exists from every $g$ on the same interval, and the uniform time lemma gives completeness. This is Lee Theorem 9.18 and the foundation of the exponential map; see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

**Is an instance: a linear vector field $X(x) = Ax$ on $\mathbb{R}^n$.** Its flow is $\phi_t(x) = e^{tA} x$, defined for all $t$ since the matrix exponential is defined for all real $t$. Linear vector fields are always complete.

**Is NOT an instance: $x^2 \partial_x$ on $\mathbb{R}$.** Superlinear growth. The integral curve starting at $x_0 > 0$ is $\gamma(t) = x_0/(1 - t x_0)$, blowing up at $t = 1/x_0$. Not complete.

**Is NOT an instance: $\partial_x$ on $\mathbb{R} \setminus \{0\}$.** The integral curve starting at $1$ reaches the removed point $0$ at $t = -1$. The maximal interval is $(-1, +\infty)$, not $\mathbb{R}$. Not complete.

**Is NOT an instance: $\partial_x$ on the open unit interval $(0, 1)$.** The integral curve starting at $1/2$ reaches the boundary at $t = 1/2$ (heading right) and at $t = -1/2$ (heading left), but $(0, 1)$ excludes both endpoints, so the curve cannot be continued. Maximal interval $(-1/2, 1/2)$.

**Corollary (compactness criterion).** Every smooth vector field on a compact smooth manifold is complete. The proof has two lines: every smooth vector field has support contained in $M$, which is compact; by the compact support criterion, the field is complete.

**Corollary (linear vector fields on $\mathbb{R}^n$).** Every linear vector field $X(x) = Ax$ on $\mathbb{R}^n$ is complete: $\phi_t(x) = e^{tA} x$ is defined for all $t$. Sublinear-growth vector fields are also complete, by a Grönwall argument.

**Corollary (one-parameter group structure).** If $X$ is complete, then $t \mapsto \phi^X_t$ is a smooth group homomorphism $(\mathbb{R}, +) \to (\mathrm{Diff}(M), \circ)$. So a complete vector field is the same data as a smooth $\mathbb{R}$-action on $M$; differentiating the action at $t = 0$ recovers the vector field.

**Calibration check.** You should be able to: (a) decide whether $X = x^3 \partial_x$ on $\mathbb{R}$ is complete (answer: no, superlinear growth gives finite-time blowup; integral curve $x_0/\sqrt{1 - 2t x_0^2}$ blows up at $t = 1/(2x_0^2)$); (b) verify that $X = \sin(x) \partial_x$ on $\mathbb{R}$ *is* complete (bounded by $1$, so sublinear growth — in fact bounded — and integral curves cannot escape any compact set); (c) recognize that incompleteness can come either from blowup or from the manifold being "incomplete" (having holes or being non-Hausdorff), and these have different remedies.

---

# Unlocked by This

> [!tip] One-Parameter Group of Diffeomorphisms *(from Lie Theory and Dynamical Systems)*
> A complete vector field is exactly the same data as a smooth group homomorphism $\mathbb{R} \to \mathrm{Diff}(M)$. Complete vector fields are therefore the "infinitesimal generators" of one-parameter subgroups of the diffeomorphism group, and the entire theory of [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie groups and their exponential maps]] specializes this picture to finite-dimensional Lie groups acting on themselves.

> [!tip] Geodesic Completeness *(from Riemannian / Lorentzian Geometry)*
> A Riemannian manifold is **geodesically complete** if the geodesic equation — itself a vector field on the tangent bundle, the **geodesic spray** — is complete. The Hopf–Rinow theorem says geodesic completeness is equivalent to metric completeness for Riemannian manifolds; for Lorentzian manifolds it is the question of whether spacetime has "edges", and the Hawking–Penrose **incompleteness theorems** show that physically realistic spacetimes are typically geodesically incomplete, with the incompleteness signalling singularities.
