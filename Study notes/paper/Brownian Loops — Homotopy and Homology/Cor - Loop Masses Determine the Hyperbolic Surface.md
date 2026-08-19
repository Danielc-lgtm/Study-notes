---
type: corollary
subject: probability-geometry
prereqs:
  - "Prop - Loop Masses Determine the Length Spectrum"
  - "Def - Marked Length Spectrum"
tags: [paper, brownian-loops, spectral-geometry, teichmuller-theory]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 3.12"
---

# Notation

- $X$ — a **closed** (compact, no boundary) topological surface of genus $g\ge 2$.
- $g_1, g_2$ — two hyperbolic metrics on $X$ (both making $X$ into a hyperbolic surface); the pair $(X, g_i)$ is a specific hyperbolic surface, and different $g_i$ give distinct points of Teichmüller space.
- $C_X(\gamma^m)$ — a free homotopy class of loops on the topological surface $X$; this class is *purely topological* (defined by $\pi_1(X)$'s conjugacy structure) and does not depend on the choice of $g_1$ or $g_2$.
- $\mu^\kappa_{X,g}$ — the killed Brownian loop measure on $(X, g)$ with parameter $\kappa\ge -\tfrac14$; depends on $g$ (which sets the Brownian process's law).
- Teichmüller space $\mathcal{T}(X)$ — the space of hyperbolic metrics on $X$ modulo isometries isotopic to the identity; a $(6g - 6)$-real-dimensional manifold for closed genus $g\ge 2$.

> [!recall]- Closed hyperbolic surface and Teichmüller space
> **Formally:** a **closed** surface has no boundary and is compact (so genus $g\ge 2$ if the surface is hyperbolic — genus $0$ is the sphere with curvature $+1$, genus $1$ is the torus with curvature $0$). Every hyperbolic metric on a closed genus-$g$ surface has constant curvature $-1$; **Teichmüller space** $\mathcal{T}(X)$ is the space of such metrics modulo isometries isotopic to the identity, and it is diffeomorphic to $\mathbb{R}^{6g-6}$.
> **In words:** given the topological surface (genus $g$, no boundary, no punctures), Teichmüller space is the moduli space of shapes it can be given as a hyperbolic surface, up to the natural equivalence "you and I get the same shape up to a continuous deformation of the identity map".
> **Concretely:** for a genus-2 closed surface, $\dim\mathcal{T} = 6$, parametrised (via a pants decomposition) by 3 pants-curve lengths and 3 twist parameters. Every point of $\mathcal{T}$ is a genuinely distinct hyperbolic metric — no two points give isometric surfaces (once one identifies "isometry isotopic to identity" as the equivalence).

> [!recall]- Marked length spectrum determines the metric — Otal–Croke rigidity
> **Formally:** Otal (1990) and Croke (1990) proved: on a *closed* surface of *negative* curvature, if two Riemannian metrics $g_1, g_2$ have the same *marked* length spectrum (same length assigned to each free homotopy class), then $g_1$ and $g_2$ are isometric by an isometry isotopic to the identity — the same point in Teichmüller space.
> **In words:** knowing the length of the shortest representative of each topological loop-type is a *complete* invariant of the metric on a closed negatively-curved surface: no two Teichmüller-distinct metrics give the same marked spectrum.
> **Concretely:** on a genus-2 closed hyperbolic surface with 6 real Teichmüller parameters, the marked length spectrum is an infinite labelled sequence of positive real numbers (one per free homotopy class), but the *rigidity* says the whole 6-parameter metric can be reconstructed from just this list. **Sources:** Otal, *Le spectre marqué des longueurs des surfaces à courbure négative*, Ann. Math. 131 (1990); Croke, *Rigidity for surfaces of non-positive curvature*, Comment. Math. Helv. 65 (1990). Both proofs use variational/rigidity arguments on the space of measures on the unit tangent bundle. See also [[Def - Marked Length Spectrum]].

> [!recall]- Loop-masses determine the marked length spectrum (Prop 3.11)
> **Formally:** by [[Prop - Loop Masses Determine the Length Spectrum|Proposition 3.11]], for the Brownian loop measure ($\kappa = 0$), $\ell_\gamma = \log(1 + 1/\mu_X(C_X(\gamma)))$; for the killed measure with $\kappa\ge -\tfrac14$, $\mu^\kappa_X(C_X(\gamma))$ is strictly decreasing in $\ell_\gamma$, hence determines it. Either way: the family of class-masses determines the marked length spectrum $\mathrm{MLS}$.
> **In words:** the closed-form formula for a Brownian (or killed-Brownian) class-mass is an invertible function of the geodesic's length; so knowing all class-masses, class by class, tells you every geodesic length together with which class realises it — that is, the marked length spectrum.
> **Concretely:** if $\mu_{X,g}(C_X(\gamma)) = 0.5$, then $\ell_\gamma = \log(1 + 1/0.5) = \log 3 \approx 1.099$. Applied for every class, this reconstructs the full marked spectrum from the loop-mass function. Full detail: [[Prop - Loop Masses Determine the Length Spectrum]].

---

# Statement

> **Corollary (loop masses determine the surface; Belyaev–Huseynli 3.12).** Let $X$ be a closed hyperbolic surface (genus $g\ge 2$), $g_1, g_2$ two hyperbolic metrics on $X$, and fix $\kappa\ge -\tfrac14$. If
> $$\mu^\kappa_{X,g_1}(C_X(\gamma^m)) \;=\; \mu^\kappa_{X,g_2}(C_X(\gamma^m)) \qquad\text{for every }(\gamma, m),$$
> (i.e. every free homotopy class of loops on $X$), then $(X, g_1)$ and $(X, g_2)$ are isometric by an isometry isotopic to the identity — the same point of Teichmüller space $\mathcal{T}(X)$.

---

# In One Line

The killed Brownian loop-mass function is a *complete* invariant of a closed hyperbolic surface's geometry: knowing it, class by class, pins down the metric up to Teichmüller-space isotopy — no ambiguity, no missing information.

---

# Why It's True

**Mechanism (one sentence).** *[[Prop - Loop Masses Determine the Length Spectrum|Proposition 3.11]] shows that the loop-mass function determines the marked length spectrum with its full class labelling; Otal–Croke rigidity then says the marked spectrum determines the metric up to Teichmüller-space equivalence.*

The corollary is a two-step chain:
1. **Loop-masses ⇒ Marked length spectrum** ([[Prop - Loop Masses Determine the Length Spectrum|Prop 3.11]]): the closed-form killed class-mass $\mu^\kappa_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{e^{(\frac12 - \sqrt{1/4+\kappa})m\ell_\gamma}}{e^{m\ell_\gamma} - 1}$ is a strictly-monotone function of $\ell_\gamma$ for every $m$, so its value at $(\gamma, m)$ uniquely recovers $\ell_\gamma$. Doing this for every class gives the complete $\mathrm{MLS}$ (values $\{m\ell_\gamma\}$ with labels $\{C_X(\gamma^m)\}$).
2. **Marked length spectrum ⇒ Metric** (Otal–Croke): on a closed negatively-curved surface, the marked spectrum is a complete invariant of the metric up to isometry isotopic to identity.

Together: equal loop-masses ⇒ equal marked spectra ⇒ equal metrics in $\mathcal{T}$.

**Why "closed" matters.** Otal–Croke rigidity is a theorem about *closed* negatively-curved surfaces. On surfaces with cusps or funnels, marked-spectrum rigidity is known in some cases but not all; the paper's Corollary is stated for closed surfaces to lean on the safe version of the rigidity theorem. The extension to more general surfaces is left as an open question in the paper's discussion.

**Why "$\kappa \ge -\tfrac14$" matters.** The strict-monotonicity argument of [[Prop - Loop Masses Determine the Length Spectrum|Prop 3.11]] (ii) is valid exactly on the range $\kappa\in[-\tfrac14, \infty)$ where the exponent $\tfrac12 - \sqrt{1/4+\kappa}$ is real — the spectral bottom of $\Delta_{\mathbb{H}^2}$. Below this threshold the class-mass formula ceases to have the correct sign/asymptotics and the inversion fails ([[Remark - The Range of the Killing Parameter|Remark 3.7]]).

---

# Proof

> [!note]- Gap-free proof
> **Given.** Two hyperbolic metrics $g_1, g_2$ on a closed genus-$g$ surface $X$ ($g\ge 2$), and $\kappa\ge -\tfrac14$, with
> $$\mu^\kappa_{X,g_1}(C_X(\gamma^m)) \;=\; \mu^\kappa_{X,g_2}(C_X(\gamma^m)) \qquad\forall\,(\gamma, m).$$
>
> **Step 1 — apply Proposition 3.11.** Let $\ell^{(i)}_\gamma := \text{length of }\gamma\text{ in }g_i$ (so $\ell^{(i)}_\gamma$ is a positive real per primitive geodesic $\gamma\in\mathcal{P}_X$, in each metric $g_i$). By [[Prop - Loop Masses Determine the Length Spectrum|Proposition 3.11]] (ii), the map $\ell\mapsto\mu^\kappa_X(C_X(\gamma))$ is strictly decreasing (log-derivative $\le -\tfrac12$), hence injective. Equality of masses in the two metrics forces $\ell^{(1)}_\gamma = \ell^{(2)}_\gamma$ for every $\gamma$. The same holds for every $m$: equal mass for the class $C_X(\gamma^m)$ ⇒ equal total length $m\ell^{(i)}_\gamma$ ⇒ same primitive length (divide by $m$; consistent with the $m=1$ case).
>
> **Step 2 — equality of marked length spectra.** Consequently, for every free homotopy class $C_X(\gamma^m)$:
> $$\mathrm{MLS}_{g_1}(C_X(\gamma^m)) \;=\; m\ell^{(1)}_\gamma \;=\; m\ell^{(2)}_\gamma \;=\; \mathrm{MLS}_{g_2}(C_X(\gamma^m)).$$
> So $\mathrm{MLS}_{g_1} = \mathrm{MLS}_{g_2}$ as marked spectra (functions on the same set of classes returning the same values).
>
> **Step 3 — apply Otal–Croke rigidity.** By Otal (1990) and Croke (1990), on a closed negatively-curved surface, equal marked length spectra imply the metrics are isometric by an isometry isotopic to the identity. Applied to $(X, g_1)$ and $(X, g_2)$ (both closed hyperbolic hence closed negatively-curved), $g_1$ and $g_2$ are isometric via an identity-isotopic map, hence represent the same point of Teichmüller space $\mathcal{T}(X)$. $\blacksquare$

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.4]] as the culminating application of the class-mass formula: the killed Brownian loop measure is a *complete* invariant of a closed hyperbolic surface's geometry, in the sense of Teichmüller-space rigidity. Consequently the loop measure serves as a fine geometric fingerprint, more refined than the raw eigenvalue spectrum of the Laplacian (which fails to be complete by Vignéras's counterexample). This result feeds the paper's motivating theme: probability measures on the loop soup are a viable diagnostic of the surface's hyperbolic geometry.
