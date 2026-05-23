---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Distribution on a Manifold"
  - "Def - Integral Manifold of a Distribution"
  - "Def - Involutive Distribution"
tags: [geometry, differential-geometry, frobenius]
---

# Notation

$M$ is a smooth manifold; $D$ is a smooth distribution on $M$. A **flat chart** for $D$ is a smooth coordinate chart $(U, \varphi)$ with $\varphi(U)$ a cube in $\mathbb{R}^n$ such that at every point of $U$, $D$ is spanned by the first $k$ coordinate vector fields $\partial/\partial x^1, \dots, \partial/\partial x^k$. In a flat chart, the **slices** of the form $x^{k+1} = c^{k+1}, \dots, x^n = c^n$ are local integral manifolds of $D$.

This is a compound page: it defines two interlocking notions — **integrability** and **complete integrability** — because they are introduced together and the [[Thm - The Frobenius Theorem|Frobenius theorem]] is the assertion that they coincide.

---

# Axiom Motivation

The desideratum is to formalize "the distribution admits integral submanifolds through every point." This is the geometric property we are trying to capture, and it has two natural strengths.

**Weak integrability** ("integrable" in Lee's sense): every point of $M$ lies in *some* integral manifold of $D$. This is the bare-minimum geometric content — the integral manifolds exist, but we say nothing about how they fit together. A priori, the integral manifolds at different points could intersect awkwardly, or be very different in size.

**Strong integrability** ("completely integrable" in Lee's sense): there exists a *flat chart* through every point — local coordinates in which $D$ is the span of the first $k$ coordinate vector fields, and the integral manifolds are the parallel slices. This is the local model — the distribution looks just like the canonical example $\mathrm{span}(\partial_1, \dots, \partial_k)$ in suitable local coordinates.

The point of the [[Thm - The Frobenius Theorem|Frobenius theorem]] is that these three conditions — *integrable*, *completely integrable*, and *involutive* — are all equivalent. The diagram is

$$\text{completely integrable} \Longrightarrow \text{integrable} \Longrightarrow \text{involutive},$$

with the first implication immediate (a flat chart provides explicit integral manifolds — the slices) and the second the necessity direction we already addressed in [[Def - Involutive Distribution]] (integral manifolds force the bracket of tangent vector fields to remain tangent). The Frobenius theorem is the deep reverse implication: **involutive $\Longrightarrow$ completely integrable**.

So why have two definitions if they are equivalent? Three reasons. First, *integrable* is the easier-to-state geometric definition — it captures "what we want" before we know that flat charts exist. Second, *completely integrable* is the precise local-model statement — it tells us *exactly* how the integral manifolds fit together (parallel slices in coordinates), which is the form that is then patched into a global [[Def - Foliation|foliation]]. Third, the equivalence between the two is itself a theorem (a consequence of the Frobenius theorem), so even though they end up the same we want to track which formulation we are using in any given context.

The choice of "flat chart" as the local model deserves a sentence. A flat chart is a coordinate system in which the distribution becomes the simplest possible — spanned by a subset of the coordinate vector fields. Such coordinates always exist when they exist (by Frobenius), and they make all subsequent computations trivial — integral manifolds are level sets, sections of $D$ have a canonical normal form, and the entire local structure is transparent. The fact that the flat-chart structure is locally rigid (any flat chart for the same $D$ differs from any other by a coordinate change preserving the slicing) is what makes [[Def - Foliation|foliations]] a well-defined global structure rather than a coordinate-dependent artifact.

A weaker local model — "coordinates in which $D$ contains $\partial_1, \dots, \partial_k$ but is not exactly spanned by them" — would be more permissive but is not what we want. The point of the flat chart is to make the integral manifolds *exactly* the slices, not just *contained in* the slices. This is what eventually allows the global gluing into a foliation.

---

# The Definition

Let $D$ be a smooth distribution of rank $k$ on a smooth $n$-manifold $M$.

**(Integrability.)** $D$ is **integrable** if every point of $M$ is contained in some [[Def - Integral Manifold of a Distribution|integral manifold]] of $D$.

**(Complete integrability.)** $D$ is **completely integrable** if every point of $M$ has a neighborhood on which there exists a **flat chart** for $D$ — a coordinate chart $(U, \varphi)$ with $\varphi(U) \subseteq \mathbb{R}^n$ a cube, such that on $U$, $D$ is spanned by $\partial/\partial x^1, \dots, \partial/\partial x^k$. In such a chart, the **slices** $\{x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ for constants $c^{k+1}, \dots, c^n$ are each local integral manifolds of $D$ (the connected slice through any given point being the local integral manifold there).

The implications

$$\text{completely integrable} \Longrightarrow \text{integrable} \Longrightarrow \text{involutive}$$

hold by direct argument (Lee, Proposition 19.3). The [[Thm - The Frobenius Theorem|Frobenius theorem]] is the deep converse:

$$\text{involutive} \Longrightarrow \text{completely integrable},$$

so all three conditions are equivalent.

---

# Relate to Other Fields / Compression

**True name:** *Integrability is local linearizability.* The operational meaning: a distribution is integrable iff there are local coordinates that *straighten it out*, making it look like the linear-algebra trivial example $\mathrm{span}(\partial_1, \dots, \partial_k)$. This is the same kind of "canonical form" theorem as straightening a vector field by its flow ([[Thm - Canonical Form for a Nonvanishing Vector Field]]) — Frobenius is precisely the higher-rank generalization, with the bracket-closure condition playing the role of "vanishing of the field is the only obstacle."

**Compression to canonical form theorems.** Many theorems in differential geometry have the form "object $X$ admits canonical local coordinates iff some algebraic condition holds." Examples: a nowhere-vanishing vector field always admits *straightening coordinates* (no condition needed); a Riemannian metric admits *normal coordinates* (no condition); a symplectic form admits *Darboux coordinates* (closed + nondegenerate); an involutive distribution admits *flat coordinates* (involutivity, by Frobenius). The pattern: an infinitesimal algebraic condition is equivalent to existence of a canonical local form.

**Compression to PDE solvability.** For an overdetermined system, the question "do solutions exist locally?" is the question "is the associated distribution completely integrable?" The compatibility condition (which is involutivity) is then both necessary (mixed-partials must agree) and sufficient (by Frobenius) for local solvability. Existence of flat coordinates corresponds to *being able to solve the PDE in coordinates aligned with the solution graphs*.

---

# Examples / Corollaries

**Is an instance: any rank-$1$ distribution is integrable.** Every rank-$1$ smooth distribution is locally spanned by a nowhere-vanishing vector field $V$, and the canonical-form theorem [[Thm - Canonical Form for a Nonvanishing Vector Field]] produces coordinates in which $V = \partial/\partial x^1$ — exactly the flat-chart condition for rank $1$. So rank-$1$ distributions are *automatically* integrable; the Frobenius theorem at this rank just recovers the ODE existence-uniqueness theorem.

**Is an instance: $\mathrm{span}(\partial_1, \dots, \partial_k)$ on $\mathbb{R}^n$.** This is the model integrable distribution: the coordinates already *are* flat coordinates, and the slices $\{x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ are global integral manifolds. The Frobenius theorem says every involutive distribution looks locally like this.

**Is an instance: the kernel of a submersion $F : M \to N$.** The fibers $F^{-1}(q)$ are integral manifolds (an embedded $\dim M - \dim N$-dimensional submanifold for each regular $q$); flat charts come from the local-form theorem for submersions (a submersion looks locally like a coordinate projection, in coordinates centered at any point). So $\ker dF$ is completely integrable.

**Is an instance: an involutive rank-$2$ distribution on $\mathbb{R}^4$ given by commuting vector fields.** Take $X = \partial_1$, $Y = \partial_2$; $[X, Y] = 0$, so $D = \mathrm{span}(X, Y)$ is involutive. Frobenius (or direct construction) gives the flat chart $(x^1, x^2, x^3, x^4)$ in which $D = \mathrm{span}(\partial_1, \partial_2)$ and the integral manifolds are the $2$-planes $\{x^3 = c^3, x^4 = c^4\}$.

**Is NOT an instance: the standard contact distribution on $\mathbb{R}^3$.** $\ker(dz - y\,dx)$ is non-involutive (computed in [[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]]), so by Frobenius it is *not* integrable — no integral $2$-manifold passes through any point. No flat chart exists.

**Is NOT an instance: a generic rank-$(n-1)$ distribution on $\mathbb{R}^n$ for $n \geq 3$.** As noted under [[Def - Involutive Distribution]], a generic rank-$(n-1)$ distribution defined by a single $1$-form $\alpha$ is involutive iff $\alpha \wedge d\alpha = 0$, which is a non-trivial PDE on the coefficients of $\alpha$. Generic $\alpha$ fails this condition, so generic distributions of this type are not integrable.

**Corollary (integrable $\Longrightarrow$ involutive — easy direction).** If $D$ is integrable, then for any sections $X, Y \in \Gamma(D)$ and any $p \in M$, there is an integral manifold $N$ containing $p$. Restricted to $N$, $X$ and $Y$ are tangent vector fields, so their bracket $[X, Y]$ is tangent to $N$ (by `Corollary 8.32` in Lee — brackets of vector fields tangent to a submanifold remain tangent). So $[X, Y]_p \in T_pN = D_p$; this holds at every point, proving involutivity.

**Corollary (completely integrable $\Longrightarrow$ integrable — easy direction).** In a flat chart, each slice $\{x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ is an explicit integral manifold of $D$, and one passes through every point of the chart (take $c^{k+i} = x^{k+i}(p)$ for $i = 1, \dots, n-k$). So every point lies in an integral manifold, i.e. $D$ is integrable.

**Corollary (the deep direction: involutive $\Longrightarrow$ completely integrable).** This is the [[Thm - The Frobenius Theorem|Frobenius theorem]]. The proof exhibits a flat chart through every point by reducing to the canonical form for commuting vector fields, applied to a re-engineered local frame.

**Calibration check.** If you have understood the definition you should be able to (i) state in one sentence the three equivalent conditions (integrable, completely integrable, involutive), (ii) verify that any rank-$1$ distribution is integrable using the ODE-style canonical form, and (iii) identify the standard contact distribution as a non-example by reference to its non-involutivity.

---

# Unlocked by This

> [!tip] **The Frobenius theorem** *(from this same topic)*
> The central theorem: involutive iff completely integrable. See [[Thm - The Frobenius Theorem]] for the statement and proof.

> [!tip] **Global Frobenius theorem and foliations** *(from this same topic)*
> Beyond the local statement, the global Frobenius theorem says an involutive distribution gives rise to a *foliation* — a partition of $M$ into maximal connected integral manifolds, each "leaf" being a maximal integral submanifold. The local flat charts patch together into a global foliated structure.

> [!tip] **Holonomic constraints in classical mechanics** *(from Mechanics)*
> A constraint distribution $D \subseteq TQ$ on configuration space is **holonomic** iff $D$ is integrable — equivalently iff $D$ is involutive. Holonomic constraints come from configuration equations $f_1 = \cdots = f_r = 0$; nonholonomic ones (skating, rolling) genuinely restrict velocity without restricting position.
