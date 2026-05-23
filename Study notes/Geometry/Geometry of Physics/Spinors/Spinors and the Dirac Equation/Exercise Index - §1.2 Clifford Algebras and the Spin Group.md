---
type: exercise-index
subject: spinors
section: "1.2"
tags: [geometry, algebra, spinors, clifford]
---

## §1.2 Clifford Algebras and the Spin Group — Exercises

This section drills the algebraic mechanics of Clifford algebras and their associated spin groups. The unifying technique is the **universal property of Clifford algebras** combined with **dimension counting**: any matrix representation of generators satisfying the Clifford relation $\{e_j, e_k\} = 2g_{jk}I$ extends uniquely to an algebra homomorphism, which is an isomorphism iff the dimensions match. The classification table provides the explicit matrix algebra in each signature. The signature pattern: encountering anticommuting matrices that square to $\pm I$, recognizing the Clifford structure, and identifying the resulting spin group as a known matrix group via the table.

- [[Ex - Pauli Matrices Generate Cl(R^3)]] (⭐⭐) — explicit identification of $\mathrm{Cl}(3, 0)$ with $M_2(\mathbb{C})$ via the Pauli matrices as generators; the volume form $e_1 e_2 e_3$ corresponds to $iI$, the imaginary scalar that makes $\mathrm{Cl}(3, 0)$ naturally complex ([[Def - Clifford Algebra]], [[Def - The Pauli Matrices]], [[Thm - Clifford Algebra Universal Property]]).
- **Identify $\mathrm{Cl}(0, 2) = \mathbb{H}$ via the quaternionic units.** Using $i, j \in \mathbb{H}$ as generators of $\mathrm{Cl}(0, 2)$, verify the Clifford relation $i^2 = j^2 = -1$, $ij = -ji = k$, and conclude $\mathrm{Cl}(0, 2) \cong \mathbb{H}$ as $\mathbb{R}$-algebras. (⭐) ([[Def - Quaternions]], [[Def - Clifford Algebra]], [[Thm - Clifford Algebra Universal Property]]).
- **Show $\mathrm{Spin}(4) \cong SU(2) \times SU(2)$.** Using $\mathrm{Cl}^0(4) \cong \mathbb{H} \oplus \mathbb{H}$ from the classification, identify $\mathrm{Spin}(4)$ as the product of two unit-quaternion groups; relate this to the decomposition of $4$-vectors as left- and right-handed Weyl pairs. (⭐⭐⭐) ([[Def - Pin and Spin Groups]], [[Thm - Spin(n) is the Double Cover of SO(n)]], [[Thm - Classification of Clifford Algebras over R]]).
