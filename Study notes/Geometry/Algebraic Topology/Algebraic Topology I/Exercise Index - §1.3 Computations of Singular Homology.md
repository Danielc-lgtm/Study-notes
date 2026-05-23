---
type: exercise-index
subject: algebraic-topology
section: "1.3"
tags: [geometry, algebraic-topology]
---

## §1.3 Computations of Singular Homology — Exercises

This section computes the singular homology of the standard examples: spheres, tori, projective spaces, and the orientable surfaces of genus $g$. The exercises drill the three main computational techniques — Mayer–Vietoris induction on a two-piece cover, simplicial computation from an explicit triangulation, and switching coefficient groups to expose torsion. The single most important conceptual point is that the *coefficient group matters*: integer homology sees both Betti numbers and torsion, real homology sees only Betti numbers, $\mathbb{Z}/2$ homology sees mod-$2$ torsion and free parts modulo $2$. Mastery of this section means being able to compute $H_*(M; G)$ for any standard manifold by the appropriate method, and being able to interpret the answer in terms of the topology of $M$ (connectedness, orientability, genus, fundamental group).

- [[Ex - Computing H_n of S^n via Mayer-Vietoris]] (⭐⭐) — Compute $H_*(S^n; \mathbb{Z})$ inductively. Drills the Mayer–Vietoris cover, the connecting homomorphism's dimension shift, and the base-case handling for $S^0$ and $H_1(S^1)$. ([[Thm - Mayer-Vietoris for Singular Homology]], [[Thm - Singular Homology of the Sphere]])

- [[Ex - Computing H_* of the Torus]] (⭐⭐) — Compute $H_*(T^2; \mathbb{Z})$ from the polygon triangulation, identifying the generating $1$-cycles and verifying $\partial[T^2] = 0$ from the boundary identifications. Drills simplicial chain-complex computation, fundamental-class construction, and the Künneth-like product structure of $H_*(T^n) = H_*(S^1)^{\otimes n}$. ([[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]], [[Def - Singular Homology]], [[Def - Euler Characteristic]])

- [[Ex - Singular Homology of RP^2]] (⭐⭐⭐) — Compute $H_*(\mathbb{RP}^2; G)$ for $G = \mathbb{Z}, \mathbb{R}, \mathbb{Z}/2$, observing that the answer changes with the coefficient group. Drills the torsion phenomenon ($\partial[\mathbb{RP}^2] = 2A$, giving $H_1 = \mathbb{Z}/2$ with $\mathbb{Z}$-coefficients but $0$ with $\mathbb{R}$-coefficients), and the universal-coefficient-theorem-in-action structure of $\mathbb{Z}/2$-homology. ([[Def - Singular Homology]], [[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]], [[Def - Betti Numbers]])

- [[Ex - Euler Characteristic of a Closed Orientable Surface is 2 - 2g]] (⭐⭐) — Compute $\chi(\Sigma_g) = 2 - 2g$ in two ways: from the Betti numbers $(1, 2g, 1)$ and from the minimal CW structure ($V = 1$, $E = 2g$, $F = 1$). Drills the cell-count method, the topological invariance of the alternating sum, and the cross-check via two methods. ([[Def - Euler Characteristic]], [[Def - Betti Numbers]], [[Thm - Euler Characteristic via Alternating Betti Numbers]])
