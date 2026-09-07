---
type: theorem
subject: gauge-theory
prereqs: ["Def - Intersection Form of a Four-Manifold"]
tags: [four-manifolds, freedman, classification]
---

# Prerequisite Concepts

- [[Def - Intersection Form of a Four-Manifold]]

# Statements
> [!theorem] Whitehead and Freedman
> Closed simply connected oriented four-manifolds are homotopy equivalent exactly when their intersection forms are isomorphic. Every unimodular symmetric integral form occurs as the intersection form of such a topological four-manifold. An even form determines one homeomorphism type; an odd form determines two, distinguished by the Kirby–Siebenmann invariant.

For indefinite unimodular forms, rank, signature, and parity determine the integral isomorphism type. Odd forms are diagonal sums of $(1)$ and $(-1)$; even indefinite forms are sums of copies of $E_8$, $-E_8$, and the hyperbolic plane $H$, subject to signature and rank.

# Proof boundary
These are deep classification theorems, not formal consequences of homology. Their full proofs require CW-complex obstruction theory, surgery, Casson handles, and topological transversality. The reusable mechanism in this course is the input-output dictionary: topology produces a unimodular lattice; Freedman realizes and classifies topological manifolds from it; smooth gauge theory imposes stricter constraints.

# Characteristic elements
A vector $w$ is characteristic if $Q(x,x)\equiv Q(w,x)\pmod2$ for all $x$. Unimodularity guarantees existence. Van der Blij's congruence says $Q(w,w)\equiv\sigma(Q)\pmod8$; for even forms $w=0$, so the signature is divisible by eight. Rochlin strengthens eight to sixteen in the smooth spin case.
