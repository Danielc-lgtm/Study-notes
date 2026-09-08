# PAGE SPEC

- **Filename:** `Def - The Equivariant Deformation Complex and its Folded Operator.md`
- **Type:** definition
- **Chapter:** Gauge Theory X — Fredholm Maps, Transversality, and Degree  (folder `Gauge Theory X/`)
- **Section:** §10.5 The Equivariant Setup, Slices, and Moduli Spaces

## Spec (from the manifest)

type: definition (compound: the deformation complex (181); its cohomology; the folded operator $D_x$ (182)); source items: A-D6.6.3 (equation (181)), A-D6.6.4 (equation (182)), A-R6.6.1, A-R6.6.2; prereqs: [Def - Infinitesimal Action and Local Slice, Def - Fredholm Map and Its Index, Def - Elliptic Complex and Its Laplacians, Thm - A Short Complex is Elliptic iff its Folded Operator is Elliptic]; spec: for a $G$-equivariant $F_w:X\to Y$ and a fixed point $y$ ($g\cdot y = y$) and $x\in F_w^{-1}(y)$, the *deformation complex* is $0\to\operatorname{Lie}(G)\xrightarrow{R_x} T_xX\xrightarrow{d_xF_w} T_yY\to0$ (a complex because $d_xF_w\circ R_x = 0$ by equivariance and $y$ fixed); its cohomology: $H^0 = \operatorname{Lie}(\operatorname{Stab}_x)$ (trivial when the action is free), $H^1 = \ker d_xF_w/\operatorname{Im}R_x$ = Zariski tangent space of the moduli space $\mathcal M_w = F_w^{-1}(y)/G$ at $[x]$, $H^2 = \operatorname{coker}d_xF_w$ (trivial iff $y$ is a regular value of $F_w$); the *folded operator* $D_x := (R_x^*,d_xF_w):T_xX\to\operatorname{Lie}(G)\oplus T_yY$ (using the Hilbert structure for $R_x^*$), with $\ker D_x\cong H^1$ (R6.6.2: cf. the folding theorem `Thm - A Short Complex is Elliptic iff its Folded Operator is Elliptic`, IX); the complex is *elliptic*/$D_x$ *Fredholm* in the applications; examples: the Seiberg–Witten deformation complex (191) folded to $D_{(\psi,A)}$ (XI); non-example: at a reducible point $H^0\ne0$ and the moduli space is singular.
