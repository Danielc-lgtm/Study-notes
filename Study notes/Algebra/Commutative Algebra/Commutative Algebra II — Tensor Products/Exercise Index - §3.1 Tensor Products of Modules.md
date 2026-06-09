---
type: exercise-index
subject: commutative-algebra
section: "3.1"
tags: [algebra, commutative-algebra]
---

## §3.1 Tensor Products of Modules — Exercises

The exercises of §3.1 drill the two phenomena that make tensor products of modules subtle: *collapse* (a tensor can vanish though neither factor does) and *non-purity* (most tensors are not pure, and purity is a rank-one condition). Each exercise practises the two-sided method for vanishing — slide scalars to prove a tensor is zero, build one surviving [[Def - Bilinear and Multilinear Maps|bilinear map]] to prove it is nonzero — together with the workhorse quotient isomorphism $R/I\otimes R/J\cong R/(I+J)$ and the functorial map $f\otimes g$ made concrete as the Kronecker product. The unifying lesson is that the [[Thm - Universal Property of the Tensor Product of Modules|universal property]] turns every "build a map out of $M\otimes N$" or "is this tensor zero?" question into a statement about bilinear maps.

- [[Ex - Z mod m tensor Z mod n is Z mod gcd]] (⭐) — compute $\mathbb{Z}/m\otimes_{\mathbb{Z}}\mathbb{Z}/n\cong\mathbb{Z}/\gcd(m,n)$ two ways: by sliding scalars to bound the order of $\bar1\otimes\bar1$ above and a surviving multiplication map to bound it below, and by the quotient isomorphism with $I+J = m\mathbb{Z}+n\mathbb{Z} = \gcd(m,n)\mathbb{Z}$; the model collapse example ([[Def - Tensor Product of Modules]], [[Thm - Standard Isomorphisms of Tensor Products]], [[Thm - Universal Property of the Tensor Product of Modules]], [[Def - Ideal]]).

- [[Ex - A pure tensor that is zero without either factor being zero]] (⭐⭐) — show $2\otimes\bar1 = 0$ in $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2$ but $2\otimes\bar1\neq 0$ in $(2\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}/2$, by sliding scalars one way and constructing the bilinear certificate $b(2x,\bar y)=\overline{xy}$ the other, concluding that tensor vanishing is ambient-dependent and inherited only from submodule to ambient ([[Def - Tensor Product of Modules]], [[Def - Bilinear and Multilinear Maps]], [[Thm - Universal Property of the Tensor Product of Modules]], [[Def - Submodule]], [[Thm - Functoriality of the Tensor Product]]).

- [[Ex - The Kronecker product of matrices]] (⭐⭐) — derive the block-matrix form of $T\otimes S$ from $f\otimes g$, the eigenvalue rules $\lambda\mu$ for $A\otimes B$ and $\lambda+\mu$ for $A\otimes I+I\otimes B$, the master isomorphism $V^*\otimes W\cong\operatorname{Hom}(V,W)$, the basis-free trace and $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, and tensor rank = operator rank — all one identification of tensors with matrices ([[Thm - Functoriality of the Tensor Product]], [[Thm - Standard Isomorphisms of Tensor Products]], [[Thm - Universal Property of the Tensor Product of Modules]], [[Def - Free Module]], [[Def - Tensor Product of Modules]]).
