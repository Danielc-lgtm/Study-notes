---
type: exercise-index
subject: differential-geometry
section: "2.1"
tags: [geometry, differential-geometry]
---

## §2.1 Smooth Functions and Smooth Maps — Exercises

The exercises of §2.1 drill the **chart-pulling-back routine** — the mechanical move that reduces every smoothness verification on a manifold to a smoothness verification on a Euclidean open set. The pattern is the same in every problem: pick charts on the source and target manifolds, ensure the chart-containment condition $F(U) \subseteq V$ (shrinking the source via continuity if needed), write the coordinate representation $\widehat F = \psi \circ F \circ \varphi^{-1}$, and recognize it as a smooth Euclidean map. The exercises below test this routine in increasing complexity: trivial (identity, inclusion of an open submanifold), routine (composition), and applied (continuity-based arguments on compact manifolds).

The most important takeaway from this section is *automaticity*: once the chart-pull-back template is internalized, smoothness verifications become straightforward and almost mechanical. The exercises also surface the role of the chart-containment condition (operation 2 from the topic's Legal Operations) and its companion, [[Thm - Smooth Maps are Continuous]] — which is used to shrink charts to satisfy the containment.

- [[Ex - Composition of Smooth Maps is Smooth]] (⭐) — drills the chart-pulling-back routine and the use of continuity (from [[Thm - Smooth Maps are Continuous]]) to satisfy the chart-containment condition when chaining two smooth maps ([[Def - Smooth Map between Manifolds]], [[Thm - Smooth Maps are Continuous]])

- [[Ex - The Inclusion of an Open Submanifold is Smooth]] (⭐) — verifies smoothness of the inclusion via identity-in-coordinates and shows it is a diffeomorphism, drilling the easiest case of the chart-pull-back routine ([[Def - Smooth Manifold]], [[Def - Smooth Map between Manifolds]], [[Def - Diffeomorphism]])

- [[Ex - A Continuous Function on a Compact Manifold Attains its Maximum]] (⭐) — applies compactness + continuity to derive extremum existence; uses [[Thm - Smooth Maps are Continuous]] as the bridge from smoothness to continuity, then applies pure topology ([[Def - Compact Space]], [[Thm - Smooth Maps are Continuous]])
