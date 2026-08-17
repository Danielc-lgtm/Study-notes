---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Group Action"
tags: [paper, group-theory, topology]
---

# Signature

| symbol | type |
|---|---|
| $M$ | a locally compact Hausdorff space; here $\mathbb{H}^2$ or $\mathbb{H}^3$ |
| $G$ | a group acting on $M$ by homeomorphisms; here $\Gamma\subset\mathrm{PSL}(2,\mathbb{R})$ or $\mathrm{PSL}(2,\mathbb{C})$ acting by isometries |
| $1$ | the identity element of $G$ |
| $K\Subset M$ | $K$ compact in $M$ |
| $\#S$ | cardinality of $S$ |
| $G\backslash M$ | the orbit space, with the quotient topology; $\pi:M\to G\backslash M$ the projection |

---

# Definition

> **Definition (free, properly discontinuous).** Let $G$ act on $M$ by homeomorphisms.
> **(D1) Free.** $\ \forall h\in G\setminus\{1\}\ \forall z\in M:\ hz\neq z.$
> Equivalently, every point stabiliser is trivial: $\operatorname{Stab}_G(z)=\{1\}$ for all $z\in M$.
> **(D2) Properly discontinuous.** $\ \forall K\Subset M:\ \#\{h\in G:\ hK\cap K\neq\emptyset\}<\infty.$

> **Consequence (used, not re-proved).** If (D1) and (D2) hold and $M$ is a connected manifold, then $\pi:M\to G\backslash M$ is a covering map, $G\backslash M$ is a manifold, and $G$ is the deck transformation group of $\pi$. If $M$ is additionally simply connected, $\pi$ is the universal cover and $\pi_1(G\backslash M,\pi(z))\cong G$ after a choice of $\tilde z\in\pi^{-1}(\pi(z))$.

**Gloss.** (D1) is what makes the quotient a manifold rather than an orbifold; (D2) is what makes it Hausdorff and the projection a covering.

> **Specialisation used in this paper.** For $\Gamma\subset\mathrm{PSL}(2,\mathbb{R})$ or $\mathrm{PSL}(2,\mathbb{C})$:
> $$\Gamma\text{ discrete}\iff\text{(D2)},\qquad \Gamma\text{ torsion-free}\iff\Gamma\text{ has no elliptic elements}\ \Longrightarrow\ \text{(D1)}.$$
> So "torsion-free discrete" is exactly "(D1) and (D2)" in this setting. The implication "no elliptics $\Rightarrow$ free" uses that a non-identity parabolic or hyperbolic (loxodromic) isometry has no fixed point *in* $\mathbb{H}^n$; only elliptics do.

---

# Type card

> [!abstract] Type card — free and properly discontinuous
> **Given.** **(H1)** $M$ locally compact Hausdorff. **(H2)** $G$ acting on $M$ by homeomorphisms.
>
> **Produces.** Two propositions (D1), (D2) about the pair $(G,M)$. When both hold and $M$ is a simply connected manifold: a covering $\pi:M\to G\backslash M$ with deck group $G$ and $\pi_1(G\backslash M)\cong G$.
>
> **Lets you.** Replace the phrase "acts freely and properly discontinuously" by two checkable quantified statements, and cite the covering-space consequence as a single named implication rather than as background.

---

# Depends on

- [[Def - Group Action]] — for the action itself
- 🟢 compactness, quotient topology — *Topology* basics

---

# Checks

**Instance.** $G=\langle\tau\rangle$ with $\tau:z\mapsto e^{\ell}z$ on $M=\mathbb{H}^2$, $\ell>0$. **(D1):** $\tau^kz=e^{k\ell}z=z$ forces $e^{k\ell}=1$, so $k=0$. **(D2):** for $K\Subset\mathbb{H}^2$ the set $\{\operatorname{Im}w:w\in K\}$ has compact closure in $(0,\infty)$, so $\tau^kK\cap K\neq\emptyset$ for only finitely many $k$.

**Non-instance (fails D1).** $G=\langle\sigma\rangle$ with $\sigma$ elliptic of order $n$, rotating by $2\pi/n$ about $z_0\in\mathbb{H}^2$. **(D2) holds** ($G$ finite). **(D1) fails:** $\sigma z_0=z_0$. Consequence: $G\backslash\mathbb{H}^2$ has a cone point of angle $2\pi/n$, is not a manifold there, and $\pi$ is not a covering at that point — so the whole free-homotopy/conjugacy dictionary of §3 breaks.

**Non-instance (fails D2).** $G=\mathrm{PSL}(2,\mathbb{Z})$ acting on $\mathbb{H}^2$ is discrete, hence satisfies (D2) — but $G=\mathrm{PSL}(2,\mathbb{R})$ itself does not: it acts transitively, so $hK\cap K\neq\emptyset$ for uncountably many $h$ whenever $K$ has non-empty interior. The orbit space is a point.

---

# Used at

- [[Def - Fuchsian Group and the Quotient Surface]] — (D1)+(D2) are the standing hypothesis on $\Gamma$
- [[Def - Kleinian Group and Loxodromic Complex Length]] — same, in $\mathrm{PSL}(2,\mathbb{C})$
- [[Def - Deck Transformations and the Lift of a Rooted Loop]] — the covering consequence
- [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] — (D1) via torsion-freeness, to exclude an axis-reversing elliptic

---

# Commentary

> [!note]- Commentary (skippable)
> The paper writes "let $\Gamma\subset\mathrm{PSL}(2,\mathbb{R})$ be a torsion-free Fuchsian group, acting freely and properly discontinuously on $\mathbb{H}^2$" — four adjectives for two conditions, with the redundancy unmarked. Untangled: *Fuchsian* $=$ discrete $=$ (D2); *torsion-free* $\Rightarrow$ no elliptics $\Rightarrow$ (D1). The two named properties in the sentence are consequences of the two structural ones, not extra assumptions.
>
> Worth keeping in view: (D1) is used exactly twice in the paper with real force. Once to make $X$ a manifold, so that "free homotopy class" means anything. And once, much more sharply, in the centraliser computation — where torsion-freeness rules out an elliptic rotation by $\pi$ about a point of the axis, which would conjugate $\tau$ to $\tau^{-1}$ and make the stabiliser of the axis infinite dihedral rather than infinite cyclic. That second use is what produces the factor $1/m$ in every mass formula in the paper.
