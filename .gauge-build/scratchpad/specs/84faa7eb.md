# PAGE SPEC

- **Filename:** `Thm - Nonzero Degree Implies Surjectivity.md`
- **Type:** theorem
- **Chapter:** Gauge Theory X — Fredholm Maps, Transversality, and Degree  (folder `Gauge Theory X/`)
- **Section:** §10.4 Determinant Line Bundles, Orientations, and the Integer Degree

## Spec (from the manifest)

type: theorem; source items: A-T6.2.2 (Corollary 168); prereqs: [Thm - Well-Definedness and Homotopy Invariance of the Degree, Thm - Regular Values of a Proper Fredholm Map are Open and Dense, Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper]; statement: Let $F:X\to Y$ be a proper Fredholm map of index $0$, $Y$ connected. If $\deg_2 F\ne0$ (or $\deg F\ne0$) then $F$ is surjective; proof: every $y\in Y$ is a limit of regular values (`Thm - Regular Values ...` density); a regular value $y'$ has $\#F^{-1}(y') \ge |\deg F| > 0$ (or odd $\ge1$), so $F^{-1}(y')\ne\varnothing$; picking $y'_n\to y$ regular with $x_n\in F^{-1}(y'_n)$, properness (closedness of $F$, `Thm - Proper Maps ...`) gives $y\in F(X)$; spec: **Haydys omits the proof; the closedness-of-proper-maps step is supplied**; mechanism: **a nonzero degree forces every regular value to have a preimage, and a proper map has closed image, so the image is everything**; targets: existence of solutions to the Seiberg–Witten and Yang–Mills equations by degree arguments (bold context; XI uses the signed count directly).
