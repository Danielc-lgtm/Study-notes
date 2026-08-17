---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, hyperbolic-geometry, rigidity]
---

# Signature

| symbol | type |
|---|---|
| $X$ | a **closed** surface |
| $g_1,g_2$ | negatively curved smooth metrics on $X$ (in the paper: hyperbolic, so curvature $\equiv-1$) |
| $\mathrm{MLS}_{g_i}$ | the [[Def - Marked Length Spectrum\|marked length spectrum]] of $(X,g_i)$; a function on free homotopy classes |
| $\mathcal{T}(X)$ | Teichmüller space: hyperbolic metrics on $X$ modulo diffeomorphisms isotopic to $\mathrm{id}_X$ |

---

# Statement

> **(OC) Marked length spectrum rigidity in dimension 2.** *Precondition:*
> **(P1)** $X$ a closed surface;
> **(P2)** $g_1,g_2$ negatively curved metrics on $X$;
> **(P3)** $\mathrm{MLS}_{g_1}=\mathrm{MLS}_{g_2}$ as functions on the set of free homotopy classes of $X$ — i.e. **with the identity marking**.
>
> *Conclusion:* there is an isometry $(X,g_1)\to(X,g_2)$ **homotopic to the identity**.

> **(F1) Homotopic $\Rightarrow$ isotopic on a surface.** A diffeomorphism of a closed surface homotopic to the identity is isotopic to it.
>
> **(F2) Teichmüller reading.** Two hyperbolic metrics related by a diffeomorphism isotopic to $\mathrm{id}_X$ define the **same point** of $\mathcal{T}(X)$. So (OC)+(F1) says: $\mathrm{MLS}$ is injective on $\mathcal{T}(X)$.

> [!warning] The marking is not decorative
> (P3) is equality of **functions**, not of value multisets. Vignéras produced non-isometric hyperbolic surfaces with equal length spectra as multisets, so the multiset version of (OC) is **false**.

---

# Type card

> [!abstract] Type card — (OC)
> **Given.** (P1),(P2),(P3).
>
> **Produces.** An isometry $(X,g_1)\to(X,g_2)$ homotopic — hence, by (F1), isotopic — to $\mathrm{id}_X$; equivalently, equality of the two points of $\mathcal{T}(X)$.
>
> **Lets you.** Convert an equality of marked length spectra into an equality of hyperbolic structures. This is the second and final step of [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]].

---

# Status

- **Proved here:** no.
- **Source:** Otal (1990) and Croke (1990), independently; the two-dimensional case of the **Burns–Katok conjecture**, which asserts the same for negatively curved metrics on a closed manifold of any dimension. Still open in general.
- **DAG node that would close this:** **none exists.** This belongs to a *hyperbolic geometry / Teichmüller theory* strand with no node in `Study notes/Prerequisite DAG.md`. Adding one would also cover (F2) and Vignéras.
- **What is safe to assume:** the conclusion under (P1)–(P3), plus (F1) and the description (F2) of $\mathcal{T}(X)$. Nothing about the proof is used.
- **Scope:** used **once** in the paper, in Corollary 3.12. Removing it removes that corollary and nothing else.

---

# Used at

- [[Thm - Loop Masses Determine the Hyperbolic Surface]] — the sole consumer
- [[Def - Marked Length Spectrum]] — (F2) there is the motivation for the marking

---

# Commentary

> [!note]- Commentary (skippable)
> This is the deepest imported result in §3, and it is imported wholesale. Its role is to close a gap the paper cannot close itself: [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] gets from loop masses to $\mathrm{MLS}$ by an elementary inversion, and (OC) gets from $\mathrm{MLS}$ to the metric by a hard theorem.
>
> Worth noting how little is required at the interface. Proposition 3.11 delivers exactly (P3) — equality of functions on a common, topologically defined index set — because free homotopy classes do not depend on the metric. So the two halves fit without any adjustment, and a reader who accepts (OC) on faith loses nothing in following Corollary 3.12.
