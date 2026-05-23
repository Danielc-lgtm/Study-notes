---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Group Action"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group; $M$ is a smooth manifold. A left action is written $\theta : G \times M \to M$, $(g, p) \mapsto g \cdot p$ or $\theta_g(p) = g \cdot p$. Right actions are $\theta : M \times G \to M$, $(p, g) \mapsto p \cdot g$. The orbit of $p \in M$ is $G \cdot p$ and the stabilizer (isotropy group) is $G_p = \{g \in G : g \cdot p = p\}$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Axiom Motivation

The notion of a smooth Lie [[Def - Group|group]] action is built from two prior notions: the abstract [[Def - Group Action|group action]] of a [[Def - Group|group]] on a set (preserving multiplication and identity), and the requirement that the action map be smooth in the manifold sense. Together they give the right notion of "the Lie group $G$ acts smoothly on the manifold $M$": a smooth map $\theta : G \times M \to M$ that is a group action when restricted to the underlying set-theoretic structure.

Why the joint condition? Each axiom contributes something essential.

**The group action condition** $\theta(e, p) = p$ and $\theta(g_1, \theta(g_2, p)) = \theta(g_1 g_2, p)$ is what makes the action genuinely a "group of symmetries acting on $M$" — without it, $\theta$ is just a smooth map of manifolds with no algebraic content. The two equations say that the identity acts trivially and that composition of actions corresponds to group multiplication. They are the same as in [[Def - Group Action|abstract group theory]].

**The smoothness condition** is what makes the action interact with manifold-theoretic constructions: tangent vectors, vector fields, flows, differential forms, integration. A continuous action that fails to be smooth might not have well-defined infinitesimal generators, might not allow differentiation of orbits, and might not produce a smooth manifold structure on quotients. Smoothness is essential for the constructions of orbit-stabilizer (smooth version) and homogeneous-space theory. Like for [[Def - Lie Group Homomorphism|Lie group homomorphisms]], continuity is in fact sufficient (a continuous action of a Lie group on a smooth manifold by [[Def - Diffeomorphism|diffeomorphisms]] is automatically smooth, by a slightly weaker version of the Bochner–Montgomery theorem), but the cleanest statement of the definition demands smoothness.

**Left vs right actions.** A left action satisfies $\theta(g_1, \theta(g_2, p)) = \theta(g_1 g_2, p)$ — composing the $g_2$-action with the $g_1$-action equals the $(g_1 g_2)$-action, in that order. A right action reverses this: $\theta(\theta(p, g_1), g_2) = \theta(p, g_1 g_2)$. The conversion is via inversion: a left action $\theta_g(p)$ becomes a right action $\theta^{(g)}(p) = \theta_{g^{-1}}(p)$, and vice versa. Both conventions are common; Lee predominantly uses left actions for general considerations and right actions for principal bundles. We use both as the context requires.

**Why care about specific structural properties of actions?** Four properties dominate the theory:

- **Transitivity**: the action has a single orbit, $G \cdot p = M$ for any $p$. Transitive smooth actions are the source of homogeneous-space structure.
- **Freeness**: every stabilizer $G_p$ is trivial. Free actions admit quotient manifold structure (under additional properness).
- **Properness**: the map $G \times M \to M \times M$, $(g, p) \mapsto (g \cdot p, p)$, is a proper map (preimages of compacts are compact). Proper actions have Hausdorff orbit spaces; combined with freeness, the orbit space is a smooth manifold (the quotient manifold theorem).
- **Effectiveness**: the only $g \in G$ acting trivially is $e$. Effective actions are isomorphic to [[Def - Subgroup|subgroups]] of $\mathrm{Diff}(M)$ — the action faithfully represents $G$.

Each property captures a different qualitative feature, and the major theorems of the chapter (orbit-stabilizer, homogeneous-space) use specific combinations.

**Why not impose all four in the definition?** Because too restrictive. Many natural actions fail at least one: the trivial action is not effective or free, the conjugation action of $G$ on itself is not free (every $g$ fixes itself), the natural action of $\mathrm{GL}(n)$ on $\mathbb{R}^n$ is not free at $0$. The right approach is: define "smooth action" minimally, and label the additional properties as adjectives.

---

# The Definition

Let $G$ be a [[Def - Lie Group|Lie group]] and $M$ a [[Def - Smooth Manifold|smooth manifold]]. A **smooth left action** of $G$ on $M$ is a smooth map

$$\theta : G \times M \to M, \qquad \theta(g, p) =: g \cdot p,$$

satisfying

1. **Identity.** $e \cdot p = p$ for all $p \in M$.
2. **Compatibility.** $g_1 \cdot (g_2 \cdot p) = (g_1 g_2) \cdot p$ for all $g_1, g_2 \in G$ and $p \in M$.

A **smooth right action** is a smooth map $M \times G \to M$, $(p, g) \mapsto p \cdot g$, satisfying $p \cdot e = p$ and $(p \cdot g_1) \cdot g_2 = p \cdot (g_1 g_2)$. We say $M$ is a **left $G$-space** or **right $G$-space** correspondingly.

Each $\theta_g : M \to M$, $\theta_g(p) = g \cdot p$, is a [[Def - Diffeomorphism|diffeomorphism]] of $M$ (its inverse is $\theta_{g^{-1}}$). So a smooth action is equivalently a Lie group homomorphism $G \to \mathrm{Diff}(M)$ (where $\mathrm{Diff}(M)$ is the diffeomorphism group, an infinite-dimensional Lie group when treated with appropriate care).

For $p \in M$:
- The **orbit** of $p$ is $G \cdot p = \{g \cdot p : g \in G\} \subseteq M$.
- The **stabilizer** (or **isotropy group**) of $p$ is $G_p = \{g \in G : g \cdot p = p\}$, a closed [[Def - Subgroup|subgroup]] of $G$ (closed by continuity, hence an embedded Lie subgroup by [[Thm - The Closed Subgroup Theorem|the closed subgroup theorem]]).

An action is:
- **Transitive** if $G \cdot p = M$ for some (equivalently, every) $p$;
- **Free** if $G_p = \{e\}$ for every $p$;
- **Effective** (or **faithful**) if the only $g \in G$ with $g \cdot p = p$ for all $p$ is $g = e$;
- **Proper** if the map $\Theta : G \times M \to M \times M$, $\Theta(g, p) = (g \cdot p, p)$, is a proper map (preimages of compact subsets are compact).

---

# Relate to Other Fields / Compression

A smooth Lie group action is the **smooth manifold refinement** of the abstract [[Def - Group Action|group action]]: a group action $G \times M \to M$ subject to the additional condition that this map be smooth. Most of the abstract theory of group actions — orbits partitioning, stabilizer-as-subgroup, orbit-stabilizer — survives, with the addition that orbits are now immersed submanifolds and stabilizers are closed Lie subgroups.

From the [[Def - Lie Group Homomorphism|homomorphism side]], a smooth left action is equivalent to a Lie group homomorphism $\rho : G \to \mathrm{Diff}(M)$ (with appropriate functional-analytic care for $\mathrm{Diff}(M)$). The kernel of $\rho$ is the subgroup acting trivially on $M$, which is closed and hence a Lie subgroup.

**True name:** A smooth Lie group action is **a $G$-equivariant smooth structure on $M$**: a way of viewing $M$ as having a smoothly varying $G$-symmetry. Operationally, the most useful form is the **infinitesimal generator** map $\hat\theta : \mathfrak{g} \to \mathfrak{X}(M)$, which sends each Lie algebra element $X$ to the smooth vector field $\hat X$ on $M$ generating the one-parameter family of diffeomorphisms $p \mapsto \exp(tX) \cdot p$ (for left actions; with a sign for right actions). The image of $\hat\theta$ is a finite-dimensional Lie subalgebra of $\mathfrak{X}(M)$ — possibly an anti-homomorphism for left actions, see Lee Thm 20.18 — and contains the algebraic shadow of the action at every point.

---

# Examples / Corollaries

**Is an instance: $G$ acts on itself by left translation.** $\theta(g, h) = gh$. The action is smooth (multiplication is smooth), transitive (any $h$ can be sent to any other by $L_{h' h^{-1}}$), and free (only $e$ fixes any point). Orbits are all of $G$, stabilizers are trivial.

**Is an instance: $G$ acts on itself by conjugation.** $\theta(g, h) = ghg^{-1}$. Smooth, but **not** transitive in general (the conjugacy class of $h$ is the orbit) and **not** free ($h$ stabilizes itself, so $h \in G_h$). Orbits are conjugacy classes; the stabilizer of $h$ is the **centralizer** $C_G(h)$.

**Is an instance: $\mathrm{GL}(n, \mathbb{R})$ acts on $\mathbb{R}^n$ by matrix multiplication.** $\theta(A, v) = Av$. Smooth, not transitive (the origin is a separate orbit from $\mathbb{R}^n \setminus \{0\}$), not free (the origin is fixed by everything). On $\mathbb{R}^n \setminus \{0\}$ the action is transitive.

**Is an instance: $\mathrm{SO}(n+1)$ acts on $S^n$.** $\theta(A, v) = Av$ (restricting the matrix multiplication action to the unit sphere). Smooth, transitive (any unit vector can be rotated to any other), not free (stabilizers are copies of $\mathrm{SO}(n)$). See [[Ex - S^2 as a Homogeneous Space of SO(3)]] for the $n = 2$ case.

**Is an instance: $\mathbb{Z}$ acts on $\mathbb{R}$ by translation.** $\theta(n, x) = x + n$. Smooth (translations are smooth), free (only $0$ fixes any point), proper (preimages of compact sets are finite hence compact). Quotient $\mathbb{R}/\mathbb{Z} \cong S^1$ is a smooth manifold.

**Is an instance: $\mathbb{R}$ acts on $T^2$ by irrational winding.** $\theta(t, (z_1, z_2)) = (e^{2\pi i t} z_1, e^{2\pi i \alpha t} z_2)$ for irrational $\alpha$. Smooth, free, but **not proper** — preimages of compacts are non-compact, because the orbit through $(1, 1)$ is dense in $T^2$. The orbit space $T^2/\mathbb{R}$ has the trivial topology (only open sets are $\emptyset$ and the whole space) and is not Hausdorff. Compare Lee Example 21.3.

**Is NOT an instance: a continuous but non-smooth action.** Take $\mathbb{R}$ acting on itself by $\theta(t, x) = (x^3 + t^3)^{1/3}$. This is a continuous action (since the map is continuous and the group axioms are satisfied), but the action map is *not smooth* at $(t, x) = (0, 0)$ — the cube root creates a derivative singularity. So it is a continuous group action but not a smooth Lie group action.

**Is NOT an instance: a map that fails the group axioms.** Take $\mathrm{GL}(n)$ acting on $\mathbb{R}^n$ by $\theta(A, v) = A^2 v$. This is smooth and satisfies $\theta(I, v) = v$, but $\theta(A, \theta(B, v)) = A^2 B^2 v \neq (AB)^2 v = \theta(AB, v)$ in general, so it fails the compatibility axiom and is not a group action.

**Corollary (stabilizer is a closed Lie subgroup).** $G_p \subseteq G$ is closed (since $G_p = \theta^{-1}(\{p\})$ for the smooth map $\theta(\cdot, p) : G \to M$, and $\{p\}$ is closed). By the closed subgroup theorem, $G_p$ is an embedded Lie subgroup of $G$. Its Lie algebra is $\mathfrak{g}_p = \{X \in \mathfrak{g} : \widehat X|_p = 0\}$ where $\widehat X$ is the infinitesimal generator vector field.

**Corollary (orbits are immersed submanifolds).** The orbit $G \cdot p$ is the image of the orbit map $\theta^{(p)} : G \to M$, $g \mapsto g \cdot p$, which has constant rank (by equivariance) equal to $\dim G - \dim G_p$. By the rank theorem, $\theta^{(p)}$ factors through an immersion, and the orbit inherits a unique smooth manifold structure making it an immersed submanifold of $M$, diffeomorphic to $G/G_p$.

**Corollary (compact group ⟹ proper action).** Every continuous action of a compact Lie group on a manifold is proper (Lee Cor 21.6). *Proof:* properness is equivalent to: every sequence $(g_i, p_i)$ with $(g_i \cdot p_i, p_i)$ convergent has a convergent subsequence in $G \times M$; if $G$ is compact, $(g_i)$ has a convergent subsequence automatically.

**Corollary (orbit-stabilizer).** For a transitive smooth action of $G$ on $M$, $M \cong G/G_p$ as smooth manifolds. See [[Thm - Orbit-Stabilizer for Lie Group Actions]].

**Calibration check.** If you can (i) verify $\mathrm{SO}(n+1)$ acts smoothly and transitively on $S^n$ with stabilizer $\mathrm{SO}(n)$; (ii) explain why an irrational $\mathbb{R}$-action on $T^2$ is smooth and free but not proper; and (iii) state the equivalence "action = Lie group homomorphism $G \to \mathrm{Diff}(M)$" — you have understood the definition correctly.

---

# Unlocked by This

> [!tip] Orbit-Stabilizer Theorem (smooth version) *(from this chapter)*
> For a smooth transitive action of $G$ on $M$, the orbit map $\theta^{(p)} : G \to M$ descends to a diffeomorphism $G/G_p \cong M$. This is [[Thm - Orbit-Stabilizer for Lie Group Actions]] and it is the smooth analogue of the orbit-stabilizer theorem from finite group theory.

> [!tip] Homogeneous Space *(from this chapter)*
> A manifold equipped with a transitive smooth action is a **homogeneous space**; see [[Def - Homogeneous Space]] and [[Thm - Homogeneous Space is a Smooth Manifold]]. Every homogeneous space is of the form $G/H$ for a Lie group $G$ and closed subgroup $H \leq G$.

> [!tip] Quotient Manifold Theorem *(from Lie Groups, Advanced)*
> If $G$ acts smoothly, **freely**, and **properly** on $M$, then the quotient $M/G$ inherits a unique smooth manifold structure of dimension $\dim M - \dim G$ such that $M \to M/G$ is a smooth submersion (Lee Thm 21.10). This is the workhorse for constructing principal bundles, quotient manifolds in differential topology, and the bases of fibre bundles.

> [!tip] Infinitesimal Generator *(from this chapter)*
> Every smooth action $\theta : G \times M \to M$ has an **infinitesimal generator** $\hat\theta : \mathfrak{g} \to \mathfrak{X}(M)$, a Lie algebra homomorphism (or anti-homomorphism, depending on convention) sending $X \mapsto \hat X$ where $\hat X|_p = \frac{d}{dt}|_{t=0} (\exp(tX) \cdot p)$. The image is a finite-dimensional Lie subalgebra of $\mathfrak{X}(M)$, and conversely (for simply connected $G$) every such "Lie algebra action" lifts to a Lie group action (Lee Thm 20.16).
