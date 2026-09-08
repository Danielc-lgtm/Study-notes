# PAGE SPEC

- **Filename:** `Thm - Connected Sum of Simply Connected Manifolds is Simply Connected.md`
- **Type:** theorem
- **Chapter:** Gauge Theory XII — Homotopy, Homology, Orientation, and Poincaré Duality  (folder `Gauge Theory XII/`)
- **Section:** §12.5 Mayer–Vietoris and Homology Computations

## Spec (from the manifest)

type: theorem; source items: T4.2.17, I4.2.6; prereqs: [Thm - Seifert-van Kampen Theorem for Two Open Sets, Def - Connected Sum of Manifolds, Thm - Spheres of Dimension at Least Two are Simply Connected]; statement: (i) For a connected topological $n$-manifold $M$ with $n \ge 3$ and $x \in M$, the inclusion $\dot M = M \setminus \{x\} \hookrightarrow M$ induces an isomorphism $\pi_1(\dot M) \to \pi_1(M)$. (ii) If $M$, $N$ are simply connected topological manifolds of dimension $n \ge 3$ then $M \# N$ is simply connected. (iii) For $n = 2$ the statement (ii) holds as well, because the only simply connected closed surface is $S^2$ and $S^2 \# S^2 \cong S^2$; the page proves only the direction it needs — that $S^2 \# S^2 \cong S^2$ by an explicit homeomorphism — and records that Bär's "dimension $\ge 2$" (Rem. 4.2.25) is used in the series only for $n = 4$; proof: source omitted; (i) apply `Thm - Seifert-van Kampen Theorem for Two Open Sets` to $M = \dot M \cup B$ with $B$ a chart ball around $x$: $\dot M \cap B \cong B \setminus \{x\} \simeq S^{n-1}$ is simply connected for $n \ge 3$, so $\pi_1(M) \cong \pi_1(\dot M) * \pi_1(B) = \pi_1(\dot M)$; (ii) apply it to $M \# N = \dot M \cup \dot N$ with $\dot M \cap \dot N \cong S^{n-1} \times (0,1)$ simply connected, giving $\pi_1(M \# N) \cong \pi_1(\dot M) * \pi_1(\dot N) = 0$ by (i). Purely topological; no smoothing is needed. spec: Sources: $\pi_1$ of punctured manifolds; Targets: chapter XIII standing hypotheses for $k\mathbb{CP}^2 \# l \overline{\mathbb{CP}^2}$ and $\pi_1(V) = 0$ in the exotic $\mathbb{R}^4$ argument.
