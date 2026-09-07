---
type: theorem
subject: gauge-theory
prereqs: ["Def - Intersection Form of a Four-Manifold", "Def - Instanton"]
tags: [four-manifolds, donaldson, instantons]
---

# Prerequisite Concepts

- [[Def - Intersection Form of a Four-Manifold]]
- [[Def - Instanton]]

# Statement
> [!theorem] Donaldson diagonalization
> If $X$ is a closed simply connected oriented smooth four-manifold and $Q_X$ is positive definite, then $Q_X$ is isomorphic over $\mathbb Z$ to the identity form. Equivalently, a negative-definite form is diagonal with entries $-1$ after reversing orientation.

# Gauge-theoretic mechanism
Choose an $SU(2)$-bundle with instanton number one and study the compactified moduli space of anti-self-dual connections. Its expected dimension is five. After generic perturbation, the irreducible part is smooth; Uhlenbeck compactness adds ideal instantons, while reducibles correspond to integral lattice vectors of prescribed square. An oriented cobordism extracted from the compactification forces those vectors to provide an integral orthonormal basis. Hence the definite unimodular lattice is diagonal.

# Proof boundary
A full proof requires the slice theorem, generic metrics, removal of singularities, Uhlenbeck compactification, gluing near ideal instantons and reducibles, and orientation compatibility. Gauge Theory VII–VIII supply the Fredholm and transversality pattern, but not the complete bubbling/gluing package. This page records the theorem with its exact hypotheses and the logical role of every missing analytic block rather than presenting the source's sketch as a complete proof.

# Consequences
The topological manifold with form $E_8\oplus E_8$ exists by Freedman but cannot be smooth: if smooth, its positive-definite non-diagonal form would contradict Donaldson. Related decompositions yield exotic smooth structures, including exotic $\mathbb R^4$s.
