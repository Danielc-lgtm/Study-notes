# PAGE SPEC

- **Filename:** `Thm - Zig-Zag Lemma for Short Exact Sequences of Chain Complexes.md`
- **Type:** theorem
- **Chapter:** Gauge Theory XII — Homotopy, Homology, Orientation, and Poincaré Duality  (folder `Gauge Theory XII/`)
- **Section:** §12.4 Singular Homology, Homotopy Invariance, and Excision

## Spec (from the manifest)

type: theorem; source items: (Hatcher Thm 2.16, needed for the pair sequence and Mayer–Vietoris); prereqs: [Def - Chain Complex and Its Homology, Def - Exact Sequence and Short Exact Sequence]; statement: A short exact sequence $0 \to A_\bullet \xrightarrow{i} B_\bullet \xrightarrow{j} C_\bullet \to 0$ of chain complexes of $R$-modules induces a long exact sequence $\cdots \to H_n(A) \xrightarrow{i_*} H_n(B) \xrightarrow{j_*} H_n(C) \xrightarrow{\partial} H_{n-1}(A) \to \cdots$, with $\partial [c] := [i^{-1} \partial j^{-1} c]$; the construction is natural with respect to maps of short exact sequences; proof: source: none; the page gives the full diagram chase: well-definedness of $\partial$ (choice of preimage under $j$, choice of representative), $\partial$ is a homomorphism, exactness at the three spots (six inclusions, each written out), naturality. Reference: Hatcher Thm 2.16, pp. 116–117. spec: Why-true: "the connecting map is the boundary that the quotient hid"; Targets: pair sequence, Mayer–Vietoris, universal coefficients (§12.7), compactly supported cohomology (§12.8).
