# PAGE SPEC

- **Filename:** `Thm - Intersection Form is Unimodular.md`
- **Type:** theorem
- **Chapter:** Gauge Theory XIII — Intersection Forms, Four-Manifold Classification, and Donaldson's Theorem  (folder `Gauge Theory XIII/`)
- **Section:** §13.2 The Intersection Form and the Cup-Product Form

## Spec (from the manifest)

type: theorem; source items: T5.1.10, I5.1.4, T5.1.9 (basis independence, restated); prereqs: [Thm - Intersection Form Equals the Cup Product Form, Thm - Cup Product Pairing is Unimodular on a Closed Oriented Manifold, Thm - Homology of a Simply Connected Closed Four-Manifold, Def - Unimodular Symmetric Bilinear Form, Parity, and Signature]; statement: For a closed, oriented, simply connected four-manifold $X$ with finitely generated homology (topological suffices; smooth automatic), $Q_X$ is a symmetric bilinear form on the free abelian group $H_2(X;\mathbb{Z}) \cong \mathbb{Z}^{b_2}$ whose matrix in any basis has determinant $\pm 1$; equivalently $a \mapsto Q_X(a, \cdot)$ is an isomorphism $H_2(X;\mathbb{Z}) \to \operatorname{Hom}(H_2(X;\mathbb{Z}), \mathbb{Z})$; proof: source: "Poincaré duality"; the page composes $H_2 \xrightarrow{D^{-1}} H^2 \xrightarrow{\text{ev}} \operatorname{Hom}(H_2, \mathbb{Z})$ (both isomorphisms: Poincaré duality; the universal coefficient theorem with $H_1 = 0$) and identifies the composite with $a \mapsto Q_X(a, \cdot)$ via the cap–cup identity and the previous page; the determinant statement via `Def - Unimodular Symmetric Bilinear Form, Parity, and Signature` (an integer matrix with an integer inverse has determinant $\pm 1$). spec: Sources: any simply connected closed four-manifold, smooth or topological (with the finite-generation hypothesis supplied by Freedman's import in the topological case); Targets: Serre's classification applies to $Q_X$; Donaldson's theorem; Freedman's theorem's hypothesis.
