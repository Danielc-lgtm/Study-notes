---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Ricci Tensor"
  - "Def - Scalar Curvature"
  - "Def - Constant Sectional Curvature"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a Riemannian (or pseudo-Riemannian) manifold of dimension $n \ge 3$. We write [[Def - Ricci Tensor|Ric]] for the Ricci tensor and [[Def - Scalar Curvature|S]] for the scalar curvature. Schur's lemma will use the second [[Thm - First and Second Bianchi Identities|Bianchi identity]] in its contracted form $\nabla^a \mathrm{Ric}_{ab} = \tfrac{1}{2}\nabla_b S$.

---

# Axiom Motivation

What is the next-most-restrictive curvature condition after "constant sectional curvature"? Constant sectional curvature is very strong: in dimension $\ge 3$ it forces the manifold to be locally isometric to one of the three model spaces (sphere, Euclidean, hyperbolic). We want a generalisation that captures "Ricci-homogeneous" or "as symmetric in Ricci as possible" without forcing the full constant-sectional-curvature constraint.

The natural such condition is $\mathrm{Ric} = \lambda g$ for some function $\lambda$. This says: the Ricci quadratic form is, at every point and in every direction, proportional to the metric — there is no preferred direction. Equivalently, $\mathrm{Ric}$ has only one eigenvalue (with multiplicity $n$). This is a much weaker condition than constant sectional curvature in dimension $\ge 4$ — for instance, $\mathbb{CP}^n$ with the Fubini–Study metric satisfies $\mathrm{Ric} = (n+1)g$ but has non-constant sectional curvature pinched in $[1/4, 1]$.

The first observation is that "$\lambda$ a function" automatically implies "$\lambda$ a constant" when $n \ge 3$. This is **Schur's lemma**: take the contracted second Bianchi identity $\nabla^a \mathrm{Ric}_{ab} = \tfrac{1}{2}\nabla_b S$. Substituting $\mathrm{Ric} = \lambda g$ gives $\nabla^a(\lambda g_{ab}) = \nabla_b \lambda$ on the left and $\tfrac{1}{2}\nabla_b(n\lambda) = \tfrac{n}{2}\nabla_b\lambda$ on the right. Equating, $\nabla_b\lambda = \tfrac{n}{2}\nabla_b\lambda$, so $(1 - \tfrac{n}{2})\nabla_b\lambda = 0$, forcing $\nabla\lambda = 0$ — $\lambda$ is constant — in dimension $n \ne 2$. So in dimension $\ge 3$, the apparently weaker definition "$\mathrm{Ric} = \lambda(p)g$ pointwise" coincides with the stronger one "$\mathrm{Ric} = \lambda g$ for a constant $\lambda$."

In dimension $2$, every Riemannian manifold trivially satisfies $\mathrm{Ric} = Kg$ (this is [[Ex - The Ricci Tensor of a 2-Manifold is g times K|a basic identity]]), with $K$ the Gauss curvature. So "Einstein" is a meaningful notion only in dimension $\ge 3$, and is most informative in dimension $\ge 4$ where it does *not* collapse to constant sectional curvature.

Why this specific definition rather than, say, $\mathrm{Ric}$ parallel ($\nabla \mathrm{Ric} = 0$)? Parallel Ricci is a stronger condition (it implies Einstein, but not conversely), and it forces $M$ to be **locally symmetric** ($\nabla R = 0$ in the highest-symmetry case). The Einstein condition is the right weakening: enough symmetry to give a tractable theory (Einstein manifolds form a finite-dimensional moduli space, controlled by an elliptic PDE), but not so much symmetry as to force homogeneity.

Why the dimension constraint $n \ge 3$? In dimension $2$, every manifold is Einstein, so the notion conveys no information. In dimension $3$, Einstein implies constant sectional curvature (by a representation-theoretic computation: the Riemann tensor in $3$D has the same number of components as the Ricci tensor, so they determine each other). In dimension $\ge 4$, Einstein is a genuinely strict generalisation of constant sectional curvature, and the moduli space of Einstein metrics is rich.

Why does Einstein's equation in general relativity correspond to this notion? The vacuum Einstein equations are $\mathrm{Ric} = 0$, an instance of Einstein with $\lambda = 0$ (called **Ricci-flat**). The Einstein equations with a **cosmological constant** $\Lambda$ are $\mathrm{Ric} - \tfrac{1}{2}g S + \Lambda g = 0$, which after a trace becomes $S = 4\Lambda$ in dimension $4$, and substituting back gives $\mathrm{Ric} = \Lambda g$ — pure Einstein. So an Einstein manifold with $\lambda = \Lambda$ is a vacuum solution of general relativity with cosmological constant $\Lambda$.

---

# The Definition

> **Definition (Einstein manifold).** A Riemannian (or pseudo-Riemannian) manifold $(M, g)$ of dimension $n \ge 3$ is **Einstein** if
>
> $$\mathrm{Ric} = \lambda\, g$$
>
> for some constant $\lambda \in \mathbb{R}$. (When $n \ge 3$, the condition "$\mathrm{Ric}(p) = \lambda(p) g(p)$ pointwise with $\lambda$ a function" automatically forces $\lambda$ to be constant — this is **Schur's lemma**.)
>
> The constant $\lambda$ equals $S/n$, where $S$ is the scalar curvature. **Ricci-flat** means $\lambda = 0$.

---

# Categorical / Structural Definition

An Einstein manifold is a critical point of the **Einstein–Hilbert functional**

$$S_{\mathrm{EH}}[g] := \frac{1}{\mathrm{vol}(M, g)^{(n-2)/n}} \int_M S_g\, dV_g$$

restricted to metrics of fixed volume (in compact case). The functional is dimensionless (under scaling $g \mapsto cg$) by construction. Its Euler–Lagrange equations, after the variational computation accounting for $\delta S$, $\delta dV$, and the volume constraint, are precisely $\mathrm{Ric} - \tfrac{S}{n}g = 0$ — the **traceless Ricci tensor vanishes**, equivalently $\mathrm{Ric} = (S/n)g$, equivalently Einstein. So Einstein metrics are the variationally-distinguished metrics among all metrics in a fixed conformal class or of fixed volume.

In **Riemannian holonomy theory**, special holonomy groups (Calabi–Yau with $\mathrm{SU}(n)$-holonomy, hyperkähler with $\mathrm{Sp}(n)$-holonomy, $G_2$ and $\mathrm{Spin}(7)$ in dimensions $7$ and $8$) automatically force Ricci-flatness, providing the main constructions of compact Einstein manifolds with $\lambda = 0$.

---

# Relate to Other Fields / Compression

In **general relativity**, Einstein manifolds with $\lambda > 0$ are **de Sitter** spaces (positive cosmological constant); with $\lambda < 0$, **anti-de Sitter** (negative cosmological constant). The vacuum Einstein equations with cosmological constant $\Lambda$ are exactly $\mathrm{Ric} = \Lambda g$. Both de Sitter and anti-de Sitter spaces are crucial in modern cosmology and in the **AdS/CFT correspondence** of string theory.

In **complex geometry**, **Kähler–Einstein metrics** are Kähler metrics that are also Einstein. The **Yau theorem** (1976) constructs Kähler–Einstein metrics with $\lambda \le 0$ on Kähler manifolds with $c_1(M) \le 0$, including the Calabi–Yau manifolds with $\lambda = 0$. The $\lambda > 0$ case was resolved by **Tian** and **Chen–Donaldson–Sun** ($2012$) via the **K-stability** condition.

**True name:** *An Einstein manifold is one whose Ricci tensor has only one eigenvalue — equivalently, one in which the Ricci tensor is "as symmetric as possible," carrying no preferred direction.* Operationally: $\mathrm{Ric}(v, v)/|v|^2 = \lambda$ is the *same constant* in every direction $v$ at every point. This is the natural intermediate condition between "constant sectional curvature" (extremely rigid) and "no constraint" (everything goes).

---

# Examples / Corollaries

**Example 1 (constant sectional curvature).** $S^n$, $\mathbb{R}^n$, $H^n$ — all the space forms — are Einstein with $\lambda = (n-1)K_0$. Every constant-sectional-curvature manifold is Einstein.

**Example 2 ($\mathbb{CP}^n$ with Fubini–Study).** Complex projective space with the Fubini–Study metric is Einstein with $\lambda = 2(n+1)$, but its sectional curvatures are pinched in $[1/4, 1]$ — not constant. This is the prototypical Einstein, non-constant-sectional-curvature manifold.

**Example 3 (Calabi–Yau, K3 surface).** A **Calabi–Yau manifold** is a compact Kähler manifold with $\lambda = 0$ (Ricci-flat). The first nontrivial example is the **K3 surface** (real dimension $4$), the unique simply-connected compact complex surface with trivial canonical bundle. Its existence as a Ricci-flat Kähler metric was proved by Yau ($1976$), settling Calabi's conjecture. K3 surfaces are central in string theory (compactifications) and in geometric topology.

**Example 4 ($S^p \times S^q$).** Products of round spheres of appropriate radii are Einstein. Specifically, $S^p(a) \times S^q(b)$ with the product metric is Einstein iff $(p-1)/a^2 = (q-1)/b^2$ (matching the Ricci eigenvalues on each factor). For $p = q = 2$ this means the two spheres have equal radii: $S^2 \times S^2$ with the standard product metric is Einstein.

**Non-example (a flat torus is not Einstein in dimension 3+).** The flat torus $T^n$ is Ricci-flat ($\mathrm{Ric} = 0$), so it *is* Einstein with $\lambda = 0$. But it is not of constant sectional curvature in the strict sense unless... wait — actually it *is* of constant sectional curvature $K \equiv 0$. So this is not actually a non-example.

**Non-example.** $S^2 \times H^2$ with the standard product metric has $\mathrm{Ric}$ with two different eigenvalues ($+1$ on $S^2$, $-1$ on $H^2$) — it is **not** Einstein.

**Non-example (Schwarzschild in vacuum).** The Schwarzschild metric is Ricci-flat ($\lambda = 0$), so it *is* Einstein in our sense, even though the Riemann tensor is highly nontrivial. This is the prototypical "non-trivial Ricci-flat" manifold.

**Calibration check.** If you have understood the definition correctly you should be able to: (a) verify $S^n$ is Einstein with $\lambda = n - 1$; (b) check that the trace gives $\lambda = S/n$; (c) state Schur's lemma and explain why $n \ge 3$ is needed; (d) recognise that every $2$-manifold is trivially Einstein.

---

# Unlocked by This

> [!tip] Cosmological Constant *(from General Relativity)*
> Einstein's field equations with a cosmological constant $\Lambda$ have vacuum solutions characterised by $\mathrm{Ric} = \Lambda g$ — exactly Einstein manifolds with $\lambda = \Lambda$. **De Sitter space** ($\Lambda > 0$) and **anti-de Sitter space** ($\Lambda < 0$) are the simply-connected maximally-symmetric examples. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] Calabi–Yau Manifolds *(from Complex Geometry / String Theory)*
> Compact Ricci-flat Kähler manifolds (called **Calabi–Yau manifolds**) play a central role in string compactifications. Yau's theorem (1976) proves their existence on Kähler manifolds with vanishing first Chern class. The **mirror symmetry** programme relates pairs of Calabi–Yau threefolds via deep dualities, with applications to enumerative geometry.

> [!tip] Hitchin–Thorpe Inequality *(from $4$-manifold topology)*
> A closed orientable $4$-dimensional Einstein manifold satisfies the topological inequality $2\chi(M) \ge 3|\tau(M)|$, where $\chi$ is the Euler characteristic and $\tau$ the signature. This is a serious obstruction: many smooth $4$-manifolds admit no Einstein metric. The connection between Einstein metrics and $4$-manifold topology is one of the most active areas in geometric analysis.

> [!tip] Ricci Solitons *(from Geometric Analysis)*
> A **Ricci soliton** is a generalisation of an Einstein metric satisfying $\mathrm{Ric} + \tfrac{1}{2}\mathcal{L}_X g = \lambda g$ for some vector field $X$. Ricci solitons are self-similar solutions of the **Ricci flow** and appear as the singularity models in Hamilton–Perelman analysis of $3$-manifolds.
