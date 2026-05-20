---
type: definition
subject: topology
prereqs:
  - "Def - Homotopy"
  - "Def - Homotopy Equivalence and Contractible Space"
  - "Def - Subspace Topology"
tags: [analysis, topology, homotopy]
---

# Notation

$X$ a topological space, $A \subseteq X$ a subspace. $i : A \hookrightarrow X$ the inclusion. $r : X \to A$ a retraction (continuous, $r|_A = 1_A$). $F : X \times I \to X$ a deformation. The full registry is on the topic page.

---

# Axiom Motivation

A deformation retract is a *constructive* way to certify that $A \subseteq X$ and $X$ are homotopy equivalent. We have $A$ sitting inside $X$ as a subspace, and we want to say: $X$ can be continuously squished onto $A$ while $A$ stays put. The "while $A$ stays put" part is what makes it a *retraction* rather than an arbitrary homotopy: the inclusion $i : A \hookrightarrow X$ and the squishing map $r : X \to A$ are honest geometric maps, and $r \circ i = 1_A$ on the nose, not just up to homotopy.

The three conditions encode the geometry:

1. **$F(x, 0) = x$** — at time zero, nothing has moved. This is the start of the deformation.
2. **$F(x, 1) \in A$** — at time one, everything has landed in $A$. The squishing is complete.
3. **$F(a, 1) = a$ for $a \in A$** — points already in $A$ end up where they started. The map $r(x) := F(x, 1)$ is a retraction.

The map $r$ is a retraction of $X$ onto $A$, and $r \circ i = 1_A$. The deformation $F$ provides a homotopy from $1_X$ to $i \circ r$. So $A \simeq X$ via $i, r$, with the homotopy equivalence witnessed by the explicit deformation $F$.

A **strong** deformation retract strengthens condition (3) to: **$F(a, t) = a$ for all $a \in A$ and all $t \in I$** — points of $A$ are fixed *throughout* the deformation, not just at the end. The deformation is "rel $A$" in the language of relative homotopy. This is the version one usually wants: it ensures the homotopy on $A$ is the constant one, so the deformation doesn't wiggle $A$ around before pinning it in place.

Why both notions? Because the weaker (non-strong) version is sometimes all you have. If your retraction $r$ moves points of $A$ around mid-homotopy, you still get a homotopy equivalence, just without the "rel $A$" guarantee. The strong version is preferable when available — it's the standard setup for the homotopy extension property and for proving theorems about CW pairs.

If we *weaken* the axioms further — drop conditions (2) or (3) — we lose the connection to retraction theory: arbitrary $F$ with $F(\cdot, 0) = 1_X$ is just a "homotopy starting at the identity", which need not land in any particular $A$. Conversely, *strengthening* (asking $F$ to be a homotopy of homeomorphisms throughout, an *isotopy*) gives a strictly stronger notion useful in differential and PL topology but not equivalent to the standard one. Bredon's choice — homotopy from $1_X$ to a retraction onto $A$ — is the sweet spot for algebraic topology.

---

# The Definition

Let $X$ be a topological space and $A \subseteq X$ a subspace.

**Retraction.** A continuous map $r : X \to A$ with $r(a) = a$ for every $a \in A$ (i.e., $r|_A = 1_A$) is a **retraction**. The subspace $A$ is then called a **retract** of $X$.

**Deformation retract.** $A$ is a **deformation retract** of $X$ if there is a continuous map $F : X \times I \to X$ (a **deformation**) satisfying:

1. $F(x, 0) = x$ for all $x \in X$;
2. $F(x, 1) \in A$ for all $x \in X$;
3. $F(a, 1) = a$ for all $a \in A$.

Equivalently: there is a retraction $r : X \to A$ such that $i \circ r \simeq 1_X$, where $i : A \hookrightarrow X$ is the inclusion.

**Strong deformation retract.** $A$ is a **strong deformation retract** of $X$ if condition (3) is strengthened to
$$F(a, t) = a \quad \text{for all } a \in A \text{ and all } t \in I.$$
Equivalently: $i \circ r \simeq 1_X$ rel $A$.

---

# Relate to Other Fields / Compression

A deformation retraction $r : X \to A$ is a homotopy equivalence with a particular structure: the homotopy inverse $i$ is an inclusion, and $r \circ i = 1_A$ *strictly* (not just up to homotopy). It is the **stronger** of two possible witnesses of $A \simeq X$: any deformation retract pair $(i, r)$ gives a homotopy equivalence, but most homotopy equivalences are not realizable as deformation retracts. So "deformation retract of" is a stronger relation than "homotopy equivalent to a subspace".

In differential topology, the smooth analogue is a **smooth deformation retract**, and the same definitions transfer. The Whitney approximation theorem ensures a continuous deformation retract can be smoothed for smooth $X, A$.

In algebraic topology, a (strong) deformation retract pair $(X, A)$ is a **CW pair** if both spaces have CW structures and $A$ is a subcomplex. CW pairs always have the homotopy extension property — a homotopy on $A$ extends to one on $X$ — and this is the source of many computational tools.

---

# Examples and Corollaries

**Is an instance — sphere as deformation retract of punctured Euclidean space.** $S^{n-1}$ is a strong deformation retract of $\mathbb{R}^n \setminus \{0\}$ via $F(x, t) = (1-t)x + t \cdot x/\|x\|$. At $t = 0$, $F(x, 0) = x$; at $t = 1$, $F(x, 1) = x/\|x\| \in S^{n-1}$; for $a \in S^{n-1}$, $\|a\| = 1$, so $F(a, t) = (1-t)a + ta = a$ for all $t$. See [[Ex - Sphere is a deformation retract of punctured Euclidean space]].

**Is an instance — central circle in the Möbius strip.** The Möbius band $M$ deformation retracts to its central circle via the obvious projection. The deformation slides each point along the perpendicular cross-section to the central circle.

**Is an instance — the mapping cylinder.** For any $f : X \to Y$, the target $Y$ is a strong deformation retract of $M_f$ via $F([(x, s)], t) = [(x, (1-t)s)]$, $F([y], t) = [y]$. See [[Thm - Mapping Cylinder is Deformation Retract of Target]].

**Is NOT an instance — the circle in the disk.** $S^1$ is *not* a deformation retract of $D^2$. The reason: if it were, the inclusion $S^1 \hookrightarrow D^2$ would be a homotopy equivalence, so $S^1$ and $D^2$ would have the same fundamental group. But $\pi_1(D^2) = 0$ (the disk is contractible) and $\pi_1(S^1) = \mathbb{Z}$. Contradiction. This non-retraction fact is the key input to the no-retraction proof of the Brouwer fixed-point theorem.

**Is NOT an instance — discontinuous "retraction".** If we drop the continuity requirement on $r$, the definition becomes trivial: every nonempty $A$ is a "set-theoretic retract" of any $X$ containing it (define $r$ to be the identity on $A$ and constant on $X \setminus A$). The continuity is what gives the notion topological content.

**Corollary — deformation retracts are homotopy equivalences.** If $A$ is a deformation retract of $X$, then $i : A \hookrightarrow X$ and $r : X \to A$ are mutually homotopy inverse: $r \circ i = 1_A$ (strict) and $i \circ r \simeq 1_X$ (by the deformation $F$). Hence $A \simeq X$.

**Corollary — being a deformation retract is transitive.** If $A$ is a deformation retract of $B$, and $B$ of $C$, then $A$ is a deformation retract of $C$. Compose the deformations.

**Corollary — every contractible space is a deformation retract of any point in it.** If $X$ is contractible via $H : X \times I \to X$ with $H(\cdot, 1) = c_{x_0}$, then $\{x_0\}$ is a deformation retract of $X$. If additionally $H(x_0, t) = x_0$ for all $t$ (often achievable but requires care), it's a strong deformation retract.

**Calibration check.** Verify: a point is a strong deformation retract of $\mathbb{R}^n$ (the homotopy $H(x, t) = (1-t)x$ fixes the origin); the central circle is a strong deformation retract of the cylinder $S^1 \times I$; the wedge of two circles $S^1 \vee S^1$ is *not* a deformation retract of the torus $T^2$ (would imply $\pi_1$ injects, but the torus's $\pi_1 = \mathbb{Z}^2$ is abelian while $\pi_1(S^1 \vee S^1) = F_2$ is free, not abelian).

---

# Unlocked by This

> [!tip] Cofibration *(from Algebraic Topology)*
> An inclusion $A \hookrightarrow X$ is a **cofibration** if it has the homotopy extension property: any homotopy on $A$ extends to a homotopy on $X$. A subspace that is a strong deformation retract is automatically a cofibration, and the converse is nearly true (CW pairs have both properties).

> [!tip] Mapping Cylinder Trick *(from Algebraic Topology)*
> The mapping cylinder $M_f$ deformation-retracts onto $Y$, providing the canonical way to replace any continuous map by an inclusion. This is the engine of many constructions: cofibre sequences, Puppe sequences, and the topological pushout.
