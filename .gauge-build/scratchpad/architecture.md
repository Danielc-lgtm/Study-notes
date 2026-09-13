# Gauge Theory series — chapter architecture (draft, to be reconciled with the content maps)

Location: `Study notes/Geometry/Gauge Theory/` — a peer of `Differential Geometry/`.
Layout per chapter: `Gauge Theory N — <Title>.md` (topic page) + folder `Gauge Theory N/` holding Def/Thm/Ex/Exercise Index pages.
Sources: A = Haydys, *Introduction to Gauge Theory* (haydys.txt, 73 PDF pages); B = Bär, *Gauge Theory* (Potsdam lecture notes, 2011; file mathematical_gauge_theory.pdf) (wernli.txt, 155 PDF pages).
Rule: every source item (definition, theorem, proof, example, exercise, load-bearing remark) has a destination page; every theorem proved in full.

| Ch. | Title | Source sections | Existing vault pages to link (not duplicate) |
|---|---|---|---|
| I | Lie Groups, Representations, the Exponential Map, and Group Actions | B §1.1–1.5 | DG XI (Lie group, Lie algebra, exponential map, adjoint representation, one-parameter subgroup, smooth action, homogeneous space, closed subgroup theorem, orbit–stabiliser) |
| II | Vector Bundles, Covariant Derivatives, and Curvature | A §2.1.1–2.1.6, §2.3 (Levi-Civita as a connection on $TM$); B's vector-bundle remarks | DG VI (vector bundle, section, local frame, transition function, subbundle, bundle homomorphism), DG VIII (forms), RG I (affine connection, Levi-Civita) |
| III | Fibre Bundles, Principal Bundles, and Associated Bundles | A §2.2.1–2.2.2, §2.4; B §2.1–2.2 | DG XI (actions), AT II (covering spaces as bundles), AT III (Hopf map) |
| IV | Connections and Curvature on Principal Bundles | A §2.2.3–2.2.4; B §2.3–2.4 | RG I (Cartan structural equations, connection 1-forms), DG VIII |
| V | Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections | A §2.1.6, §2.2.5, §3.3; B §2.6–2.7 | AT II (fundamental group, covering spaces), RG I (parallel transport) |
| VI | Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional | A §3.1–3.2; B §2.5 | DG X (de Rham cohomology, homotopy invariance), AT III (Chern forms — but its Chern–Weil page is statement-only: prove here) |
| VII | The Hodge Star, Electrodynamics, and Yang–Mills Theory | B §3.1–3.3 | Hodge I (Hodge star, codifferential), SR XXI–XXIII (Maxwell, four-potential, stress-energy), DG IX (integration, Stokes) |
| VIII | Clifford Algebras, Spin Structures, and Dirac Operators | A §4.1–4.4 | Spinors (Clifford algebra, Pin/Spin, spin structure, Lichnerowicz — check proof completeness) |
| IX | Sobolev Spaces, Elliptic Operators, and Elliptic Complexes | A §5.1–5.3 | Hodge I (Hodge decomposition — prove here for elliptic complexes), Measure Theory / Advanced Probability (Lᵖ) |
| X | Fredholm Maps, Transversality, Determinant Lines, and Degree | A §6.1–6.6 | DG IV (Sard's theorem — its page is flagged; prove Sard–Smale fully here, with the finite-dimensional Sard as a lemma), DG IX (orientation) |
| XI | The Seiberg–Witten Equations, Moduli Spaces, and Invariants | A §7.1–7.2 | VIII–X of this series |
| XII | Homotopy, Homology, Orientation, and the Fundamental Class | B §4.1–4.3 | AT I–III (singular homology, Mayer–Vietoris, fundamental group, higher homotopy, long exact sequence of a fibration — check proof completeness; Hurewicz and Seifert–van Kampen there are statement-only: prove here if needed) |
| XIII | Intersection Forms, Four-Manifold Classification, and Donaldson's Theorem | B §5.1–5.3 | XII, VI, VII of this series; Linear Algebra (bilinear forms) |

Open questions to settle from the maps:
- Does B §1 contain enough beyond DG XI to justify a full chapter (representations, Schur, complete reducibility, exponential-map properties, proper/free actions and the quotient theorem)? If it is thin, fold the new items into III as a "§3.0 Lie-theoretic preliminaries" section instead.
- Which of B §4's results are stated without proof (Hurewicz, Whitehead, Poincaré duality, universal coefficients, Künneth)? Each needs a proved page; decide which are provable at chapter length and which (if any) are genuinely book-length.
- Which results in B §5 are imports (Freedman, Donaldson, Rokhlin, Serre's classification of indefinite unimodular forms, Whitehead's homotopy classification of simply connected 4-complexes, Wall)?
- Conventions: curvature formula ($F = dA + A \wedge A$ for matrix groups vs $dA + \tfrac12[A \wedge A]$), right principal action, $\operatorname{Ad}_{g^{-1}}$ equivariance, Clifford relation sign, Hodge-star and signature conventions, Sobolev norm conventions, orientation of moduli spaces.
