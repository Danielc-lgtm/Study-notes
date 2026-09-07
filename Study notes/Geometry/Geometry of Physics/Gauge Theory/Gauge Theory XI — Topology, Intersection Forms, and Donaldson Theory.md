---
type: topic
subject: gauge-theory
chapter: "Gauge Theory XI"
title: "Gauge Theory XI — Topology, Intersection Forms, and Donaldson Theory"
tags: [gauge-theory, algebraic-topology, four-manifolds, donaldson]
---

# Motivation

Gauge theory becomes a tool for topology only after three translations. Homotopy and homology turn spaces into computable algebra. Poincaré duality turns cup product into the integral intersection lattice of a four-manifold. Moduli spaces of anti-self-dual connections then impose restrictions invisible to purely topological classification. Freedman says which unimodular forms occur topologically; Donaldson shows that smooth definite forms are extraordinarily rigid.

# Notation Registry

$X$ is a closed connected oriented four-manifold. The torsion-free lattice is $H=H^2(X;\mathbb Z)/\operatorname{Tor}$, its intersection form is $Q_X$, and $b_2^\pm$ are the positive and negative indices of its real extension. Thus $\sigma(X)=b_2^+-b_2^-$. For an $SU(2)$-bundle $P$, $\mathcal M_k$ denotes the anti-self-dual moduli space with $c_2(P)=k$.

# Concept Map

- [[Def - Homotopy Groups and Homotopy Equivalence]] packages deformation-invariant information about maps.
- [[Thm - Long Exact Homotopy Sequence of a Fibre Bundle]] computes topology from fibre, total space, and base.
- [[Def - Singular Homology and Cohomology Operations]] gives the linear, computable theory and its exact sequences.
- [[Def - Orientation Fundamental Class and Poincare Duality]] turns cohomology into complementary-dimensional geometry.
- [[Def - Intersection Form of a Four-Manifold]] packages oriented surface intersections into a unimodular lattice.
- [[Thm - Spin Parity and Rochlin Divisibility]] exhibits a first smooth constraint.
- [[Thm - Classification of Simply Connected Topological Four-Manifolds]] states the Whitehead–Freedman topological classification and the arithmetic of indefinite forms.
- [[Def - Donaldson Moduli Space and Uhlenbeck Compactification]] supplies the nonabelian gauge-theory input.
- [[Thm - Donaldson Diagonalization Theorem]] gives the smooth definite constraint and its analytic proof architecture.

# Sources and Targets

A bundle targets homotopy computations through its long exact sequence. A closed oriented manifold targets an integral lattice through Poincaré duality and cup product. A simply connected topological four-manifold targets classification data through its intersection form. A hypothetical smooth structure targets a contradiction by comparing Rochlin or Donaldson restrictions with that lattice.

# Legal Operations

1. Replace a space by a homotopy-equivalent one before computing homotopy or homology.
2. Use exactness to trade an unknown homotopy group for neighbouring groups of a fibration.
3. Represent Poincaré-dual degree-two classes by transverse oriented surfaces and count intersections.
4. Reverse orientation to negate the form, and take connected sums to form orthogonal sums.
5. Read parity, rank, and signature before invoking lattice classification.
6. Use Freedman only in the topological category and Donaldson only in the smooth category.
7. Compactify an instanton moduli space by ideal connections rather than pretending bubbling cannot occur.

## Illegal but tempting

Homotopy equivalence is not homeomorphism. Equal homology groups do not determine the intersection form. A real diagonalization does not imply an integral diagonalization. Freedman's existence theorem does not provide a smooth manifold. Donaldson's theorem does not classify indefinite forms. Uhlenbeck compactness is not convergence without energy loss; the lost charge is recorded at bubbling points.

# Problem-Solving Strategy

Compute the algebraic-topology input first: connectivity, (co)homology, orientation, and cup products. Build $Q_X$ and reduce the question to its rank, signature, parity, and definiteness. In the topological category apply Whitehead, Freedman, and the classification of indefinite unimodular forms. For smoothability, test spin parity and Rochlin first; if the form is definite, apply Donaldson. Keep category changes explicit at every step.

# Rederivation Handles

The chapter rests on three handles. The boundary map of a fibration measures the failure of a lifted sphere to close. Poincaré duality makes $Q_X$ unimodular because complementary-dimensional cycles pair perfectly. Donaldson's moduli space converts analysis into lattice vectors: compactification and boundary orientation force a definite form to possess an integral orthonormal basis.

# Exercises

- [[Ex - Intersection Forms of Basic Four-Manifolds]]
- [[Ex - Freedman versus Donaldson for the E8 Form]]
- [[Exercise Index - §11.1 Topology and Four-Manifold Gauge Theory]]

# Sources

- Konstantin Wernli, *Mathematical Gauge Theory*, Preface and §§4.1–5.3.
