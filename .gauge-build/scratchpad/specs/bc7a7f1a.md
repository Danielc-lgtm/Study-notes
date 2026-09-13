# PAGE SPEC

- **Filename:** `Thm - Higher Homotopy Groups are Abelian via the Eckmann-Hilton Argument.md`
- **Type:** theorem
- **Chapter:** Gauge Theory XII — Homotopy, Homology, Orientation, and Poincaré Duality  (folder `Gauge Theory XII/`)
- **Section:** §12.1 Homotopy and Homotopy Groups

## Spec (from the manifest)

type: theorem; source items: T4.1.7; prereqs: [Thm - Group Structure on Homotopy Groups and the Cube Model]; statement: For $n \ge 2$ and any pointed space $(X,x)$, $\pi_n(X,x)$ is abelian; proof: source gives a six-picture sketch; the page proves it in full by the Eckmann–Hilton route: define the second concatenation $*_2$ in the second coordinate, prove (Lemma 1) $*_2$ is well defined on classes and has the constant map as a two-sided unit up to homotopy rel $\partial I^n$; (Lemma 2) the interchange law $(g_1 *_1 g_2) *_2 (g_3 *_1 g_4) = (g_1 *_2 g_3) *_1 (g_2 *_2 g_4)$ holds on the nose (write both sides on the four sub-cubes); (Lemma 3) from interchange with units, $[g_1] *_1 [g_2] = [g_1] *_2 [g_2] = [g_2] *_1 [g_1]$ (the standard four-line Eckmann–Hilton computation, each equality justified by Lemma 2 with explicit substitutions of the constant map). Also record Bär's picture proof as the intuition in Why Is It True. Reference: Hatcher §4.1 p. 340 (the picture); for the interchange-law argument, tom Dieck, *Algebraic Topology* (2008), §2.3, or Bredon VII.2; the writer follows the interchange law exactly as written here. spec: Sources: any $H$-space has abelian $\pi_1$ (link `Ex - Pi_1 of a Topological Group is Abelian`); targets: the Hurewicz theorem for $n \ge 2$ needs no abelianisation (Bär Rem. 4.2.23).
