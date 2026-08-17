---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Loop Masses Determine the Marked Length Spectrum"
  - "Def - Marked Length Spectrum"
tags: [paper, hyperbolic-geometry, rigidity]
---

# Notation

- $X$ — a **closed** hyperbolic surface; $g_1,g_2$ two hyperbolic metrics on it
- $\mu^\kappa_{X,g_i}$ — the killing loop measure computed in the metric $g_i$; $\kappa\geq-\tfrac14$ fixed
- $\mathcal{C}_X(\gamma^m)$ — a free homotopy class, a purely topological object, the same for both metrics
- $\mathrm{MLS}$ — the [[Def - Marked Length Spectrum|marked length spectrum]]
- **isotopic to the identity** — homotopic to the identity map through diffeomorphisms
- Teichmüller space — the space of hyperbolic metrics on $X$ modulo diffeomorphisms isotopic to the identity

---

# Type card

> [!abstract] Type card — Corollary 3.12 (loop masses determine the hyperbolic surface)
> **Given.** A closed hyperbolic surface $X$; two hyperbolic metrics $g_1,g_2$ on it; a fixed $\kappa\geq-\tfrac14$; and the hypothesis $\mu^\kappa_{X,g_1}(\mathcal{C}_X(\gamma^m))=\mu^\kappa_{X,g_2}(\mathcal{C}_X(\gamma^m))$ **for every** free homotopy class.
>
> **Produces.** An isometry between $(X,g_1)$ and $(X,g_2)$ **isotopic to the identity** — hence the two metrics define the **same point in Teichmüller space**.
>
> **Lets you.** Read the loop masses as a complete invariant of the marked hyperbolic structure: no geometric information is lost in passing from the metric to the family of class masses.

---

# Statement

> **Corollary 3.12 (loop masses determine the hyperbolic surface).** Let $X$ be a closed hyperbolic surface, let $g_1,g_2$ be hyperbolic metrics on $X$, and fix $\kappa\geq-\tfrac14$. If
> $$\mu^\kappa_{X,g_1}\big(\mathcal{C}_X(\gamma^m)\big) = \mu^\kappa_{X,g_2}\big(\mathcal{C}_X(\gamma^m)\big)$$
> for every free homotopy class $\mathcal{C}_X(\gamma^m)$, then $(X,g_1)$ and $(X,g_2)$ are isometric by an isometry isotopic to the identity, and hence define the same point in the Teichmüller space.

---

# Why it is true

Two steps, and the second is borrowed.

The hypothesis is an equality of *functions on free homotopy classes*, and free homotopy classes are topological — they do not depend on which metric $X$ carries. So the hypothesis compares two metrics through a common index set. By [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]], each mass determines the length of the class's geodesic representative in the corresponding metric. Hence equality of masses class-by-class gives $\mathrm{MLS}_{g_1}=\mathrm{MLS}_{g_2}$ as functions on the same index set — that is, the two metrics have the same marked length spectrum, **with the identity marking**.

Then Otal and Croke: a negatively curved metric on a closed surface is determined up to isometry by its marked length spectrum. Hyperbolic metrics are negatively curved, so there is an isometry between $g_1$ and $g_2$, and because the marking is the identity, that isometry is homotopic — hence isotopic, on a surface — to the identity. Two hyperbolic metrics related by a diffeomorphism isotopic to the identity are by definition the same point of Teichmüller space.

**The mechanism in one line: the class masses see the geodesic lengths, the marking is automatic because free homotopy classes are metric-independent, and marked-length-spectrum rigidity does the rest.**

**Why the marking is the whole point.** Vignéras's non-isometric isospectral surfaces have the same length spectrum as a multiset. If the hypothesis were weakened to "the two metrics produce the same *multiset* of masses", the corollary would be false. What rules that out is that the hypothesis quantifies over classes — it says *this* class has *this* mass under both metrics — and free homotopy classes provide the common labelling that isospectrality lacks.

---

# Strategy

**Strategy.** Use Proposition 3.11 to convert equality of masses into equality of marked length spectra with the identity marking; then quote Otal–Croke for marked-length-spectrum rigidity in negative curvature, and note that "homotopic to the identity" upgrades to "isotopic" on a surface.

> [!note]- Proof (skippable)
> By [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] the mass in a free homotopy class determines the length of its geodesic representative. Since the hypothesis gives equality of masses class-by-class, and the index set of classes is the same for both metrics (free homotopy is a topological notion), $g_1$ and $g_2$ have the same marked length spectrum, with the identity marking.
>
> Hyperbolic metrics are negatively curved, so by Otal and Croke there is an isometry between $g_1$ and $g_2$ homotopic to the identity. On a closed surface, a diffeomorphism homotopic to the identity is isotopic to it. Two hyperbolic metrics differing by a diffeomorphism isotopic to the identity define the same point of Teichmüller space. $\;\square$

---

# What this assumes, and where to climb

**Proposition 3.11** — [[Thm - Loop Masses Determine the Marked Length Spectrum]], hence the whole mass-formula stack behind it.

**Closedness of $X$.** Needed twice: Otal–Croke is stated for closed manifolds, and Teichmüller space of a closed surface is the object being landed in. The corollary does not extend to cusped or funnelled surfaces as stated.

**Otal's and Croke's theorem** — quoted, and one of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|five recorded gaps]]. It is the two-dimensional case of the Burns–Katok conjecture: a negatively curved metric on a closed manifold is determined up to isometry by its marked length spectrum. This is genuinely outside everything in the vault — it belongs to a hyperbolic-geometry / Teichmüller-theory strand with no DAG node — and it is the only place in the paper where it is used.

**The description of Teichmüller space** as hyperbolic metrics modulo diffeomorphisms isotopic to the identity, also quoted. Same gap.

Notably **not** assumed: any relation between $g_1$ and $g_2$ beyond the mass equality; in particular they need not be conformally equivalent.

---

# What consumes this

Nothing. This is the terminal result of §3.4 and of the whole §3 coda; §4 onwards does not use it.

Its role is interpretive. It answers the question a reader will have after Theorem 3.5 — *how much geometry do these masses actually see?* — with the strongest possible answer for a closed surface: **all of it, up to the identifications Teichmüller space already makes.**

---

# Reading it against the rest of the paper

Set this beside [[Thm - Concentration on Systolic Classes|the $s\to\infty$ analysis of §6.1]] to see the trade-off the paper makes. Corollary 3.12 uses the *entire function* of class masses and recovers the *entire* hyperbolic structure. Section 6.1 normalises those masses into a probability measure, which necessarily discards the overall scale, and from the resulting single function $-\log Z_X(s)$ recovers only the systole and its multiplicity, asymptotically. Aggregation costs information, and these two results bracket how much.

Note also what the corollary does **not** say: nothing about which functions on classes arise as loop masses. The map from Teichmüller space to mass functions is injective by this corollary; its image is not characterised, and the paper does not ask.
