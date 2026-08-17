---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Loop Masses Determine the Marked Length Spectrum"
  - "Ext - Otal–Croke Marked Length Spectrum Rigidity"
tags: [paper, hyperbolic-geometry, rigidity]
---

# Signature

| symbol | type |
|---|---|
| $X$ | a **closed** hyperbolic surface |
| $g_1,g_2$ | hyperbolic metrics on $X$ (curvature $\equiv-1$) |
| $\mu^\kappa_{X,g_i}$ | the killing loop measure computed in $g_i$; $\kappa\geq-\tfrac14$ fixed |
| $\mathcal{C}_X(\gamma^m)$ | a free homotopy class — **topological**, the same index set for both metrics |
| $\mathrm{MLS}_{g_i}$ | the marked length spectrum of $(X,g_i)$ |
| $\mathcal{T}(X)$ | Teichmüller space: hyperbolic metrics modulo diffeomorphisms isotopic to $\mathrm{id}_X$ |

---

# Type card

> [!abstract] Type card — Corollary 3.12
> **Given.**
> **(H1)** $X$ a **closed** hyperbolic surface.
> **(H2)** $g_1,g_2$ hyperbolic metrics on $X$.
> **(H3)** $\kappa\geq-\tfrac14$ fixed.
> **(H4)** $\mu^\kappa_{X,g_1}(\mathcal{C}_X(\gamma^m))=\mu^\kappa_{X,g_2}(\mathcal{C}_X(\gamma^m))$ **for every** free homotopy class.
>
> **Produces.** An isometry $(X,g_1)\to(X,g_2)$ isotopic to $\mathrm{id}_X$; equivalently, $g_1$ and $g_2$ define the **same point of $\mathcal{T}(X)$**.
>
> **Lets you.** Read the loop masses as a **complete invariant** of the marked hyperbolic structure: nothing is lost in passing from the metric to the family of class masses.

---

# Statement

> **Corollary 3.12.** Assume (H1)–(H4). Then $(X,g_1)$ and $(X,g_2)$ are isometric by an isometry isotopic to the identity, and hence define the same point in Teichmüller space.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Loop Masses Determine the Marked Length Spectrum\|Prop 3.11]] | (H4), class by class | $\mathrm{MLS}_{g_1}=\mathrm{MLS}_{g_2}$ as functions |
| [[Def - Marked Length Spectrum\|(F3)]] | the index set | free homotopy classes are topological, so the two $\mathrm{MLS}$ share a domain — the **identity marking** |
| [[Ext - Otal–Croke Marked Length Spectrum Rigidity\|(OC)]] | negatively curved $g_1,g_2$ with equal $\mathrm{MLS}$ | an isometry homotopic to $\mathrm{id}_X$ |
| [[Ext - Otal–Croke Marked Length Spectrum Rigidity\|(OC)(F1),(F2)]] | that isometry | isotopic to $\mathrm{id}_X$; same point of $\mathcal{T}(X)$ |

---

# Proof

**Strategy.** Prop 3.11 converts (H4) into equality of marked length spectra with the identity marking; (OC) converts that into an isometry; (F1) upgrades homotopic to isotopic.

> [!note]- Proof (skippable)
> By Prop 3.11 the mass in a class determines the length of its geodesic representative. (H4) gives equality class-by-class, and by (F3) the index set is the same for both metrics (free homotopy is topological), so
> $$\mathrm{MLS}_{g_1}=\mathrm{MLS}_{g_2}\quad\text{as functions, with the identity marking.}$$
> Hyperbolic metrics are negatively curved, so (OC) applies and yields an isometry homotopic to $\mathrm{id}_X$; by (F1) it is isotopic to $\mathrm{id}_X$; by (F2) the two metrics are the same point of $\mathcal{T}(X)$. $\;\square$

---

# What this assumes, and where to climb

- **Prop 3.11** — [[Thm - Loop Masses Determine the Marked Length Spectrum]], hence the §3 mass-formula stack.
- **Closedness** — needed twice: (OC) is stated for closed manifolds, and $\mathcal{T}(X)$ of a closed surface is the target. The corollary does **not** extend to cusped or funnelled surfaces as stated.
- **(OC)** — [[Ext - Otal–Croke Marked Length Spectrum Rigidity]]. Quoted; the **only** place in the paper it is used, and the only result in §3 with no DAG node.
- **Not assumed:** any relation between $g_1$ and $g_2$ beyond (H4). In particular they need **not** be conformally equivalent.

---

# Consumed by

Nothing. Terminal result of §3.4 and of the §3 coda; §4 onwards does not use it.

---

# Commentary

> [!note]- Commentary (skippable)
> **The mechanism in one line: the class masses see the geodesic lengths, the marking is automatic because free homotopy classes are metric-independent, and marked-length-spectrum rigidity does the rest.**
>
> Why (H4) is quantified over classes rather than over values: Vignéras's non-isometric isospectral surfaces agree on the *multiset* of lengths. If (H4) were weakened to "the two metrics produce the same multiset of masses", the corollary would be **false**. What rules that out is that free homotopy classes provide a common labelling that isospectrality lacks — see [[Def - Marked Length Spectrum|(F2),(F3)]].
>
> The corollary's role is interpretive: it answers the question a reader has after Theorem 3.5 — *how much geometry do these masses actually see?* — with the strongest possible answer for a closed surface: **all of it, up to the identifications Teichmüller space already makes.**
>
> What it does not say: nothing about *which* functions on classes arise as loop masses. The map $\mathcal{T}(X)\to\{$mass functions$\}$ is injective by this corollary; its image is not characterised, and the paper does not ask.
>
> Compare with [[Thm - Concentration on Systolic Classes]]: there the same masses, summed and normalised, return only the systole and its multiplicity. The two results bracket what aggregation costs.
