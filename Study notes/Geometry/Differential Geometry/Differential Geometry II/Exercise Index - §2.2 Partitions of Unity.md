---
type: exercise-index
subject: differential-geometry
section: "2.2"
tags: [geometry, differential-geometry]
---

## §2.2 Partitions of Unity — Exercises

The exercises of §2.2 drill the **bump-and-normalize construction** — the canonical mechanism by which local objects on a smooth manifold are blended into global ones. The pattern is the same in every problem: build smooth bump functions on $\mathbb{R}^n$ from the $\psi_0(t) = e^{-1/t^2}$ germ; pull back through charts to get bumps on the manifold; cover the manifold by open sets where the local construction is defined; build bumps for a closed shrinkage of the cover; sum and normalize. The exercises below test the construction in two stages: first the Euclidean bump (the atomic building block), then the partition of unity itself (the assembly).

The key takeaway is that the construction has two pieces — a **real-analysis input** (the $\psi_0$-trick and the resulting smooth cutoff, which is essentially what distinguishes the smooth from the analytic categories) and a **topological input** (paracompactness, normality, and the closed shrinking step). Together they produce the smooth partition of unity, which is the workhorse of global differential geometry.

- [[Ex - Constructing a Bump Function on Euclidean Space]] (⭐⭐) — constructs the prototype smooth bump $\psi : \mathbb{R} \to [0, 1]$ equal to $1$ on $[-1, 1]$ and $0$ outside $[-2, 2]$ via the $\psi_0(t) = e^{-1/t^2}$-trick and the quotient form of the smooth cutoff; the atomic building block of all later partition-of-unity constructions ([[Def - Bump Function and Smooth Cutoff]], [[Def - Smooth Function on a Manifold]], [[Def - Support of a Function]])

- [[Ex - Smooth Partition of Unity Subordinate to a Cover]] (⭐⭐) — constructs an explicit smooth partition of unity for a finite open cover via the "shrink, bump, sum, normalize" pattern; the finite case of [[Thm - Existence of Smooth Partitions of Unity]] without the paracompactness machinery, drilling the closed shrinking and normalization steps ([[Def - Partition of Unity on a Manifold]], [[Def - Bump Function and Smooth Cutoff]], [[Thm - Existence of Smooth Bump Functions]])

- [[Ex - A Continuous Function on a Compact Manifold Attains its Maximum]] (⭐) — uses compactness + continuity to derive extremum existence, illustrating how compactness restricts the behaviour of functions on the manifold; appears here as a continuation of §2.1 in spirit, since compact manifolds are also the setting where partition-of-unity constructions are simplest (no infinite refinement needed) ([[Def - Compact Space]], [[Thm - Smooth Maps are Continuous]])
