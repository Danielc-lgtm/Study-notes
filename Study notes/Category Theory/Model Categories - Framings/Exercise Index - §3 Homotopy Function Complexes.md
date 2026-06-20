---
type: exercise-index
subject: model-categories
section: "3"
tags: [category-theory, homotopy-theory, foundations]
---

## §3 Homotopy Function Complexes — Exercises

This section delivers the payoff: the [[Def - Homotopy Function Complex|homotopy function complex]] $\mathrm{map}(X, Y)$, the derived mapping space that upgrades the hom-*set* $[X,Y]$ of the homotopy category into a hom-*space* with all its higher homotopies. The exercises drill the three things one most needs to know about it. The first verifies the anchoring fact $\pi_0\,\mathrm{map}(X,Y) = [X,Y]$ by hand, translating $0$-simplices into maps and $1$-simplices into homotopies. The second computes the function complex in $\mathbf{sSet}$ and finds it is the internal hom $Y^X$ — the model case that makes the abstract construction concrete. The third, at the hardest tier, computes the function complex in chain complexes via a projective resolution and recovers the $\mathrm{Ext}$ groups as its homotopy groups, exhibiting $\mathrm{map}$ as the space-level $\mathbf{R}\mathrm{Hom}$ and revealing frame-independence and resolution-independence of $\mathrm{Ext}$ as one theorem. All three rest on [[Thm - Framings Compute Homotopy Function Complexes]] and the frames of §2.

- [[Ex - Pi-zero of the function complex is the homotopy classes]] (⭐) — $\pi_0\,\mathrm{map}(X,Y) = [X,Y]$ from the frame; $0$-simplices are maps, $1$-simplices are homotopies ([[Def - Homotopy Function Complex]], [[Def - Cosimplicial and Simplicial Frame]], [[Def - Cylinder Object, Path Object, and Homotopy]])
- [[Ex - The function complex of simplicial sets is the internal hom]] (⭐⭐) — $\mathrm{map}(X,Y)\cong Y^X$ via the frame $X\times\Delta^{\bullet}$ and cartesian closure ([[Def - Homotopy Function Complex]], [[Def - Simplicial Set]], [[Def - Cosimplicial and Simplicial Frame]])
- [[Ex - Homotopy function complexes in chain complexes compute Ext]] (⭐⭐⭐) — $\pi_n\,\mathrm{map}(M,N)\cong\mathrm{Ext}^n_R(M,N)$ via Dold–Kan and a projective resolution; the function complex as $\mathbf{R}\mathrm{Hom}$ ([[Def - Homotopy Function Complex]], [[Def - Cosimplicial and Simplicial Frame]], [[Def - Chain Map and Chain Homotopy]], [[Def - Module]])
