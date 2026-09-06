---
type: theorem
subject: gauge-theory
prereqs: ["Thm - Seiberg-Witten Deformation Complex is Elliptic", "Thm - Sard-Smale and Parametric Transversality"]
tags: [gauge-theory, seiberg-witten, slice, transversality]
---

# Statement

> [!theorem] Slice and generic regularity
> At an irreducible configuration, the affine space $(\psi,A)+\ker R^*_{(\psi,A)}$ is a local slice. For a residual set of self-dual perturbations $\eta$, every irreducible solution is regular, and the irreducible moduli space is a smooth manifold of expected dimension
> $$d=\frac14\left(c_1(L)^2-2\chi(M)-3\sigma(M)\right).$$

# Proof Architecture

> [!proof]- Formal Proof
> Freeness at an irreducible and invertibility of $R^*R$ on the complement of constants let the implicit-function theorem solve uniquely for a nearby gauge transformation satisfying the slice equation.
>
> For universal perturbations, variation of $\eta$ is surjective onto the self-dual-form component. If a negative spinor annihilates the remaining Dirac component, variations of the connection and nonvanishing of $\psi$ force it to vanish on an open set; unique continuation for $D_A^-$ makes it vanish globally. Thus the universal section is transverse, and Sard–Smale gives generic regularity.
>
> The gauge-fixed linearization is homotopic through Fredholm operators to $D_A^+\oplus(d^+\oplus d^*)$. Atiyah–Singer gives the complex Dirac index $\frac18(c_1(L)^2-\sigma)$, counted twice over the reals, while $\operatorname{ind}(d^+\oplus d^*)=b_1-b_0-b_2^+=-\frac12(\chi+\sigma)$. Their sum is the stated $d$.

