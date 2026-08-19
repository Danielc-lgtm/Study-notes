---
type: definition
subject: geometry
prereqs:
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
tags: [paper, hyperbolic-geometry, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 3.10"
---

# Notation

- $(X, g)$ — a hyperbolic surface with metric $g$ (the paper: $X = \Gamma\backslash\mathbb{H}^2$).
- $C_X(\gamma^m)$ — the free homotopy class of the $m$-fold winding around a primitive closed geodesic $\gamma\in\mathcal{P}_X$.
- $\ell_g(\eta) := \int_0^1|\dot\eta(t)|_g\,dt$ — the arc-length of a piecewise-smooth loop $\eta:[0,1]\to X$ under the metric $g$.
- $\mathcal{P}_X$ — the set of primitive closed geodesics on $X$.
- $\mathrm{MLS}$ — the marked length spectrum function.

> [!recall]- Free homotopy class $C_X(\gamma^m)$
> **Formally:** an equivalence class of oriented closed loops on $X$ under free homotopy — two loops are equivalent if one continuously deforms into the other in $X$, with the basepoint allowed to move.
> **In words:** a topological "type" of loop, defined by "which holes it winds around and in what pattern"; the basepoint is not part of the data.
> **Concretely:** on the torus $T^2$, one class per integer pair $(a,b)$ ("$a$ times horizontal, $b$ times vertical"). On a genus-2 surface, one class per conjugacy class in a non-abelian rank-4 group. See [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length]].

> [!recall]- Closed geodesic and translation length in a hyperbolic surface
> **Formally:** a closed geodesic $\gamma$ in $(X, g)$ is a closed curve that is locally distance-minimising — every arc of $\gamma$ of length less than the injectivity radius is a shortest path between its endpoints. On a hyperbolic surface, every non-trivial non-peripheral free homotopy class contains a *unique* closed geodesic; its length equals the *translation length* of the corresponding primitive hyperbolic $\Gamma$-element (the axis-translation distance in $\mathbb{H}^2$).
> **In words:** a closed geodesic is a "taut" loop — one that cannot be shortened by any local perturbation. The class $C_X(\gamma^m)$ contains the geodesic $\gamma$ *traversed $m$ times*, whose length is $m\ell_\gamma$.
> **Concretely:** on the hyperbolic quotient $\Gamma\backslash\mathbb{H}^2$ with $\Gamma = \langle\tau_0\rangle$ ($\tau_0 : z\mapsto e^\ell z$), the imaginary half-line projects to a closed geodesic of length $\ell$; the doubly-wound class contains the same geodesic traversed twice, of length $2\ell$. Full detail: [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length]].

> [!recall]- Isospectral-but-non-isometric surfaces exist (Vignéras); marked spectrum determines the metric (Otal, Croke)
> **Formally:** Vignéras (1980) constructed pairs of arithmetic hyperbolic surfaces with the same Laplacian eigenvalue spectrum (hence, by the Selberg trace formula, the same length spectrum as a *set*) but non-isometric. Otal (1990) and Croke (1990) proved: on a *closed* (compact, no boundary) negatively-curved surface, the marked length spectrum determines the metric up to an isometry isotopic to the identity — a rigidity theorem.
> **In words:** knowing just the set of lengths of closed geodesics is not enough to reconstruct the surface (counterexamples exist). But knowing which class each length comes from (the "marking") is: on a closed negatively-curved surface, that data pins down the metric up to Teichmüller-space isotopy.
> **Concretely:** Vignéras's example: two genus-2 hyperbolic surfaces built by identifying elements of a certain non-commutative ring of hyperbolic isometries — the construction itself is above our floor, but the takeaway is that two specific surfaces exist, computed to have the same eigenvalue spectrum $\{\lambda_1,\lambda_2,\ldots\}$ (equivalently, the same *unmarked* geodesic-length multiset) yet visibly different geodesic-length markings. The marked-length-spectrum rigidity of Otal–Croke says these surfaces are distinguished by *which class* realises each length. **Sources:** Vignéras, *Variétés riemanniennes isospectrales et non isométriques*, Ann. Math. 112 (1980); Otal, *Le spectre marqué des longueurs des surfaces à courbure négative*, Ann. Math. 131 (1990); Croke, *Rigidity for surfaces of non-positive curvature*, Comment. Math. Helv. 65 (1990).

---

# Statement

> **Definition (marked length spectrum; Belyaev–Huseynli 3.10).** The **marked length spectrum** of the hyperbolic surface $(X, g)$ is the function
> $$\mathrm{MLS} : C_X(\gamma^m) \longmapsto \inf_{\eta \in C_X(\gamma^m)} \ell_g(\eta),$$
> assigning to each non-trivial free homotopy class the shortest length of a loop representing that class. On a hyperbolic surface the infimum is attained by the *unique* closed geodesic of the class, so $\mathrm{MLS}(C_X(\gamma^m)) = m\ell_\gamma$ where $\ell_\gamma$ is the primitive length. The word **marked** signals that the data is not just the *set* of lengths $\{m\ell_\gamma : \gamma\in\mathcal{P}_X, m\ge 1\}$, but the *labelled* assignment "class $\mapsto$ length" — the marking records *which class realises which length*.

---

# In One Line

The function that tells you, for each topological type of loop on a hyperbolic surface, the length of its unique taut (geodesic) representative — with the *class label* preserved.

---

# Motivation and Unpacking

**Why the marking matters.** The unmarked length spectrum (the multiset $\{m\ell_\gamma : \gamma\in\mathcal{P}_X, m\ge 1\}$) is *insufficient* to reconstruct the surface: Vignéras constructed pairs of arithmetic hyperbolic surfaces with the same set of geodesic lengths but non-isometric shape. The extra structure carried by the *marking* — remembering which class realises each length — turns out to be enough: on a closed negatively-curved surface (in particular, on any closed hyperbolic surface), Otal's and Croke's rigidity theorems (independently, 1990) show that the marked length spectrum determines the metric up to an isometry isotopic to the identity — that is, up to the natural equivalence in Teichmüller space.

**How the marking connects to the loop measure.** The Brownian loop mass of a free homotopy class,
$$\mu_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{1}{e^{m\ell_\gamma} - 1},$$
depends *only* on the primitive length $\ell_\gamma$ and the winding $m$. So the class-mass function $C_X(\gamma^m)\mapsto \mu_X(C_X(\gamma^m))$ *is essentially the marked length spectrum* — it is a bijection with the marked spectrum under the invertible transformation $x\mapsto 1/(m(e^{mx} - 1))$ (see [[Prop - Loop Masses Determine the Length Spectrum|Proposition 3.11]]). This is what makes the loop measure a candidate for a *complete* metric invariant of the surface: it encodes not the raw lengths but the full marking, and via Otal–Croke this marking is a rigid invariant of the metric.

**Compact concrete instance.** For the once-punctured torus with a specific hyperbolic metric $g$, the marking assigns:
- to class $(1, 0, 0)$ (once around the first handle, zero around the second, zero around the puncture) → length $\ell_1$,
- to class $(0, 1, 0)$ → length $\ell_2$,
- to class $(1, 1, 0)$ → length $\ell_3$,
- and so on, one length per non-peripheral class.

Two hyperbolic metrics $g_1, g_2$ with the same *sets* of lengths but different assignments (say, $(1,0,0)\mapsto\ell_1$ in $g_1$ but $(1,0,0)\mapsto\ell_2$ in $g_2$) would have different markings; Otal–Croke rules such pairs out for closed surfaces of negative curvature — the assignment is rigid.

**Standard names.** The "marked length spectrum" is the standard term in geometric analysis and Teichmüller theory (Otal, Croke). The unmarked version — the raw multiset of lengths — is variously called the *length spectrum* or *Selberg spectrum*.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.4]]. Immediately fed into [[Prop - Loop Masses Determine the Length Spectrum|Proposition 3.11]] (the loop masses determine the MLS by inversion of the closed-form) and [[Cor - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] (Otal–Croke rigidity + Proposition 3.11 pins down the surface).
