# PAGE SPEC

- **Filename:** `Def - Parametric Family of Fredholm Maps.md`
- **Type:** definition
- **Chapter:** Gauge Theory X — Fredholm Maps, Transversality, and Degree  (folder `Gauge Theory X/`)
- **Section:** §10.3 The Mod-2 Degree and Parametric Transversality

## Spec (from the manifest)

type: definition (compound: the hypotheses (A)–(D); the parametric-count definition of the degree; path spaces as Banach manifolds); source items: A-D6.3.1, A-D6.3.2, A-R6.3.1, A-R6.3.3, A-I6.3.2; prereqs: [Def - Fredholm Map and Its Index, Def - Regular Value and Transversality for Fredholm Maps, Def - Mod-2 Degree of a Proper Fredholm Map, Def - Banach Manifold and Smooth Maps between Banach Spaces]; spec: a connected Banach manifold $W$ (parameters) and a smooth Fredholm $\mathcal F:X\times W\to Y$ with (A) each $\mathcal F_w := \mathcal F(\cdot,w)$ Fredholm; (B) $\mathcal F_{w_0} = F$ for some $w_0$; (C) $y$ a regular value of $\mathcal F$; (D) each $\mathcal F_w$ proper; the *generic-parameter degree* $\deg_2 F := \#\mathcal F_w^{-1}(y)\bmod 2$ for any $w$ in the residual set $W_0$ of good parameters (well-definedness on the next-but-one page); the path space $\Gamma(w_1,w_2) := \{\gamma\in C^k([1,2];W) : \gamma(1) = w_1,\gamma(2) = w_2\}$ is a Banach manifold (the writer proves the model: $C^k([1,2];W)$ is a Banach manifold with charts from those of $W$, `Def - Banach Manifold and Smooth Maps between Banach Spaces`; the fixed-endpoint condition cuts out a closed affine subspace); Axiom Motivation (R6.3.1): in equivariant problems the value $y$ must be a fixed point of a group action and cannot be moved, so one perturbs the map through $w$ instead of the value — this is exactly the Seiberg–Witten setup (XI), where $\eta$ is the parameter; examples: $\mathcal F(u,w) = \Delta u + u^3 - w$ ($w\in Y$ the value, recovering ordinary Sard–Smale); non-example: a family failing (D) (non-proper $\mathcal F_w$) has no well-defined count.
