---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. The metric is $\eta = \mathrm{diag}(1,-1,-1,-1)$; the scalar square of a four-vector is $X\cdot X = (X^0)^2 - |\mathbf{X}|^2$ where $|\mathbf{X}|^2 = (X^1)^2 + (X^2)^2 + (X^3)^2$. The null cone is $\mathcal{I}$, its future sheet $\mathcal{I}^+$, its past sheet $\mathcal{I}^-$. For an event $O$, the corresponding affine sets are $\mathcal{I}^+_O, \mathcal{I}^-_O$. Full registry on [[Special Relativity III — Minkowski Spacetime and the Metric]].

This is a compound page: it defines two interlocking notions — the **null cone** (a structure on the vector space $E$) and the **time arrow** (a choice that orients it into future and past) — because the time arrow is meaningless without the cone and the cone has no future/past until the arrow is chosen.

> [!warning] Convention: signature
> We use **"mostly minus"**, so timelike means $X\cdot X > 0$; the null cone is the *boundary* between the timelike interior and the spacelike exterior. Gourgoulhon uses the opposite sign but the same geometry. He reserves "null cone" for the structure on vectors and "light cone" for its affine counterpart (straight lines through an event); we follow that usage.

---

# Axiom Motivation

The [[Def - Classification of Four-Vectors|classification]] partitions four-vectors into timelike, spacelike, and null. The null vectors are special: they are the boundary case, the vectors of zero scalar square, and they assemble into a single geometric object — a **cone** — that organises the entire causal structure. The motivation for naming this object is that it does three jobs at once: it separates the timelike from the spacelike, it is the set of directions light travels, and (once oriented) it gives spacetime its arrow of time.

Why a cone? Because the null condition $X\cdot X = 0$ is *homogeneous of degree two*: if $X$ is null then so is $\lambda X$ for every real $\lambda$, since $(\lambda X)\cdot(\lambda X) = \lambda^2 (X\cdot X) = 0$. A set closed under scalar multiplication is a cone, and this one is the zero set of the quadratic form — geometrically, the surface $(X^0)^2 = |\mathbf{X}|^2$, a double cone with apex at the origin. The timelike vectors $(X^0)^2 > |\mathbf{X}|^2$ are *inside* it; the spacelike vectors $(X^0)^2 < |\mathbf{X}|^2$ are *outside*. So the cone is the wall between "can be travelled along" and "cannot", which is exactly the causal boundary one wants to single out.

Why *two sheets*? The equation $(X^0)^2 = |\mathbf{X}|^2$ factors as $X^0 = +|\mathbf{X}|$ or $X^0 = -|\mathbf{X}|$, two half-cones meeting only at the apex. One opens towards positive time, the other towards negative time. This two-sheetedness is not an accident of coordinates: it is a genuine topological fact (the cone minus its apex has two connected components), and it is what makes a *consistent* notion of "future" possible. The **time arrow** is the choice of which sheet to call the future, $\mathcal{I}^+$. There is nothing in the metric or the affine structure that picks one sheet over the other — both are geometrically identical — so the time arrow is *additional* structure, a binary choice, exactly as Gourgoulhon lists it as a separate ingredient of the Minkowski four-tuple. Physically it is the distinction between the future and the past, which the laws of mechanics (time-reversal symmetric) do not themselves provide; mathematically it is the orientation of the time direction.

Once the future sheet is chosen, every causal vector inherits an orientation. A timelike or null vector lies inside or on one of the two sheets, and it is **future-directed** if that sheet is $\mathcal{I}^+$, **past-directed** otherwise. The crucial fact — proved algebraically in the [[Thm - Two Lemmas on Causal Vectors|two lemmas]] — is that this orientation is *consistent*: $U\cdot V > 0$ certifies that two causal vectors lie in the same sheet, and the sum of two future-directed causal vectors is again future-directed. Without this consistency, "future" would be a frame-dependent or path-dependent notion and the arrow of time would be incoherent; with it, the future-causal vectors form a convex cone and the time arrow is a genuine global structure.

The affine version is the **light cone**. The null cone lives in the vector space $E$; transplanting it to a point $O \in \mathcal{E}$ — taking all events $M$ with $\overrightarrow{OM}$ null — gives the light cone *of* $O$, the set of events a light flash at $O$ can reach (future) or be reached from (past). This is the object that bounds causal influence: $O$ can affect exactly the events on or inside its future light cone.

---

# The Definition

The **null cone** of the [[Def - Minkowski Space and the Metric|Minkowski metric]] is the subset of the vector space $E$
$$
\mathcal{I} \;:=\; \{0\} \cup \{X \in E : X \neq 0,\ X\cdot X = 0\},
$$
the zero vector together with all null vectors. It is a **cone**: $X \in \mathcal{I}$ and $\lambda \in \mathbb{R}$ imply $\lambda X \in \mathcal{I}$. It separates $E$ into the timelike interior ($X\cdot X > 0$) and the spacelike exterior ($X\cdot X < 0$), and — apex excluded — it consists of **two sheets** (nappes), the two connected components of $\{X \neq 0 : X\cdot X = 0\}$, namely $\{X^0 = +|\mathbf{X}|\}$ and $\{X^0 = -|\mathbf{X}|\}$.

A **time arrow** (time orientation) is a choice of one of the two sheets, designated the **future null cone** $\mathcal{I}^+$; the other is the **past null cone** $\mathcal{I}^-$. Given a time arrow, a causal (timelike or null) vector $X$ is:
- **future-directed** if it lies inside or on $\mathcal{I}^+$ (equivalently $X^0 > 0$ in an orthonormal frame adapted to the arrow);
- **past-directed** if it lies inside or on $\mathcal{I}^-$ (equivalently $X^0 < 0$).

The affine counterpart at an event $O \in \mathcal{E}$ is the **light cone** of $O$: the set of events $M$ with $\overrightarrow{OM} \in \mathcal{I}$. Its future half $\mathcal{I}^+_O = \{M : \overrightarrow{OM} \in \mathcal{I}^+ \text{ or its interior}\}$ and past half $\mathcal{I}^-_O$ bound the events $O$ can causally influence and be influenced by. The **chronological future** of $O$ is the set of events reachable from $O$ by a future-directed *timelike* vector (strictly inside the cone); the **causal future** is reachable by a future-directed *causal* vector (inside or on the cone — including light rays).

---

# Relate to Other Fields / Compression

The null cone is the **zero set (light cone, or null variety) of the quadratic form** $X\cdot X$, and its two-sheeted structure is the geometric signature of an indefinite form of Lorentzian type. For a Euclidean (positive-definite) form the zero set is the single point $\{0\}$; the appearance of a two-dimensional double cone is precisely the signature being $(1,3)$. In the theory of quadratic forms the null vectors are the *isotropic* vectors, and the cone is the *isotropic cone*; the existence of nonzero isotropic vectors is what distinguishes an isotropic (indefinite) form from an anisotropic (definite) one.

The time arrow is a **time orientation**, the temporal analogue of an orientation of a vector space. Just as orienting a vector space means choosing one of two equivalence classes of bases, time-orienting Minkowski space means choosing one of two sheets of the null cone — a binary choice that the metric alone does not make. In general relativity a spacetime is called *time-orientable* if such a choice can be made consistently and globally; flat Minkowski space always is.

**True name:** the null cone is *the boundary between the causally-connectible and the causally-disconnected*, and the time arrow is *the choice of future*. Operationally: a vector is causal iff it is on or inside the cone ($X\cdot X \geq 0$), and future-directed iff (additionally) $X^0 > 0$ in an adapted frame — two sign checks that decide every causal question.

---

# Examples / Corollaries

**Is an instance — a future light ray.** $X = (1,1,0,0)$ has $X\cdot X = 0$, $X^0 = 1 > 0$: a future-directed null vector, on the future sheet $\mathcal{I}^+$, the tangent to a light ray moving in $+x$.

**Is an instance — the interior of the future cone.** $X = (2,1,0,0)$ has $X\cdot X = 3 > 0$, $X^0 = 2 > 0$: future-directed timelike, *inside* $\mathcal{I}^+$, the displacement to an event in the chronological future.

**Is NOT an instance of the cone — a spacelike vector.** $X = (1,2,0,0)$ has $X\cdot X = -3 < 0$: it lies *outside* the null cone, in the spacelike exterior, and connects events that cannot causally influence each other.

**Is NOT a sheet — the apex.** The zero vector is the apex, the single point both sheets share; it is in $\mathcal{I}$ but belongs to neither sheet. Removing it disconnects the cone into its two sheets — the topological fact that makes the future/past split possible.

**Corollary — the cone is boost-invariant but its sheets are individually invariant only under orthochronous boosts.** A Lorentz transformation maps the null cone to itself (it preserves $X\cdot X = 0$); an *orthochronous* one ($\Lambda^0{}_0 > 0$) maps each sheet to itself, while a time-reversal swaps the sheets. This is why the time arrow is preserved exactly by the orthochronous subgroup — the physically relevant one.

**Corollary — the future-causal cone is convex.** By the [[Thm - Two Lemmas on Causal Vectors|two lemmas]], the sum of two future-directed causal vectors is future-directed causal: the set of future-causal vectors is closed under addition and positive scaling, hence a convex cone. This is the property that makes "future-directed" coherent under the addition of worldline segments and four-momenta.

**Calibration check.** If you have understood the definition you can: (i) sketch (in coordinates, not by drawing) why $(X^0)^2 = |\mathbf{X}|^2$ is a double cone and identify which vectors sit inside; (ii) explain why the apex must be removed to speak of two sheets; (iii) state why a time-reversal swaps $\mathcal{I}^+$ and $\mathcal{I}^-$ while a boost does not.

---

# Unlocked by This

> [!tip] The Two Lemmas on Causal Vectors *(from §3.2)*
> The consistency of the time arrow — that "future-directed" is well-defined and closed under addition — is exactly the content of the [[Thm - Two Lemmas on Causal Vectors|two lemmas]]: $U\cdot V > 0$ certifies same-sheet for causal vectors, and future-causal vectors sum to future-causal. These are proved frame-independently and are the algebraic foundation of the causal structure.

> [!tip] Chronology, Causality and Global Structure *(from General Relativity)*
> The chronological and causal futures defined here generalise to curved spacetime, where light cones tilt and may close up; the resulting **causal structure** — chronological future $I^+$, causal future $J^+$, the conditions of time-orientability, stable causality, and global hyperbolicity — is the framework of the **singularity theorems** and the analysis of black-hole horizons in **general relativity**. The flat light cone of this page is the local model that every spacetime's causal structure is built on.
