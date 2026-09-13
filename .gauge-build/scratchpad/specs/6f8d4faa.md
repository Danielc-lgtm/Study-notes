# PAGE SPEC

- **Filename:** `Thm - Long Exact Sequence of a Pair in Singular Homology.md`
- **Type:** theorem
- **Chapter:** Gauge Theory XII — Homotopy, Homology, Orientation, and Poincaré Duality  (folder `Gauge Theory XII/`)
- **Section:** §12.4 Singular Homology, Homotopy Invariance, and Excision

## Spec (from the manifest)

type: theorem; source items: (Hatcher Thm 2.16 applied to pairs); prereqs: [Def - Relative Singular Homology, Thm - Zig-Zag Lemma for Short Exact Sequences of Chain Complexes, Thm - Homotopy Invariance of Singular Homology (Gauge Theory)]; statement: For $A \subset X$: $\cdots \to H_n(A;R) \to H_n(X;R) \to H_n(X,A;R) \xrightarrow{\partial} H_{n-1}(A;R) \to \cdots \to H_0(X,A;R) \to 0$ is exact and natural; the same with reduced homology when $A \ne \emptyset$; $\partial$ sends the class of a relative cycle $z$ to the class of $\partial z$; the long exact sequence of a triple $(X, A, B)$ likewise; if $A$ is a deformation retract of $X$ then $H_n(X, A) = 0$; and $H_n(D^k, S^{k-1}; R) \cong \tilde H_{n-1}(S^{k-1}; R)$; proof: page applies the zig-zag lemma, proves the reduced version and the triple version (Hatcher p. 118), and the deformation-retract corollary via homotopy invariance and exactness; the disc computation is deferred to §12.5 (needs sphere homology) and stated there. Reference: Hatcher §2.1 pp. 117–118. spec: Targets: local homology $H_n(M, M \setminus \{x\})$ in §12.8; the relative fundamental class.
