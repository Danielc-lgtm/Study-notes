---
type: exercise-index
subject: special-relativity
section: "4.1"
tags: [physics, special-relativity]
---

## §4.1 The Invariant Interval and Its Characterisation of the Lorentz Group — Exercises

The exercises of §4.1 turn the [[Thm - Invariance of the Spacetime Interval|invariance theorem]] from a fact into a definition. The central move of the whole chapter is the converse: the [[Def - The Lorentz Group|Lorentz group]] *is* the set of linear maps preserving the interval, equivalently the solution set of the congruence equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$. The first exercise establishes the group structure abstractly and names the pseudo-orthogonal viewpoint ($I \to \eta$); the second makes precise the standing convention $c = 1$ and the dimensional-analysis recipe for restoring $c$; the third derives the Lorentz group from the weaker hypothesis of light-cone preservation plus the relativity principle, isolating the role of each postulate. The unifying technique is to work from the defining equation algebraically, never from matrix entries, so the arguments transfer to every $O(p,q)$.

- [[Ex - The Lorentz group as pseudo-orthogonal transformations]] (⭐⭐) — prove $O(1,3)$ is a group directly from $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ without coordinates, show the equation means "preserves the inner product", explain the name pseudo-orthogonal as the substitution $I \to \eta$, and read off $(\det\Lambda)^2 = 1$ and $\Lambda^{-1} = \eta\,\Lambda^{\mathsf T}\eta$ ([[Def - The Lorentz Group]], [[Thm - Invariance of the Spacetime Interval]], [[Def - Minkowski Space and the Metric]], [[Def - Group]]).

- [[Ex - Why c=1 and restoring units by dimensional analysis]] (⭐) — explain via Tong's cm-vs-inches analogy why $c = 1$ is a unit choice reflecting the similarity of space and time, fix the light-second conversion, and apply the dimensional-analysis recipe to restore $c$ in the interval, the Lorentz factor, the boost, and the rapidity relations ([[Def - The Lorentz Transformation]], [[Def - The Spacetime Interval]], [[Def - Rapidity]]).

- [[Ex - The interval determines the boost up to a scale]] (⭐⭐) — show a linear map preserving the light cone rescales the interval by a constant $\kappa$, then use the relativity principle ($\kappa(v)\kappa(-v) = 1$, $\kappa(v) = \kappa(-v)$) to force $\kappa = 1$ and recover the Lorentz group, identifying the conformal/dilation group as what is excluded ([[Thm - Invariance of the Spacetime Interval]], [[Def - The Lorentz Group]], [[Def - The Spacetime Interval]], [[Def - Classification of Four-Vectors]]).
