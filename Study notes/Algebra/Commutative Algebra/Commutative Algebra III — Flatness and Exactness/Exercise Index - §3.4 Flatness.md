---
type: exercise-index
subject: commutative-algebra
section: "3.4"
tags: [algebra, commutative-algebra]
---

## §3.4 Flatness — Exercises

The exercises of §3.4 drill the central question of the chapter: *is this module flat, and where does it sit on the tower* free $\Rightarrow$ projective $\Rightarrow$ flat $\Rightarrow$ torsion-free? Two skills are practiced throughout. To *prove* flatness, recognise the module as free (an explicit basis), as a localization, or as a base change of something flat — the [[Thm - Characterization of Flat Modules|finitely generated criterion]] is what makes such checks finite. To *refute* flatness, hunt for torsion (the contrapositive of flat $\Rightarrow$ torsion-free kills flatness with a single element), and when the module is torsion-free, tensor the inclusion of a finitely generated ideal and look for a Koszul-type relation in the kernel of multiplication. The geometric refrain is that flatness is the algebra of a family whose fibres do not jump: a monic-quotient is a finite flat family of points, while $(X,Y)$ and $k[X,Y]/(XY)$ are the canonical pictures of tearing.

- [[Ex - A monic-polynomial quotient is a flat algebra]] (⭐⭐) — prove flatness by exhibiting a free basis: division with remainder by a *monic* polynomial gives $A[T]/(f)$ the basis $1, T, \dots, T^{d-1}$ over any base $A$ (free $\Rightarrow$ flat), and refute flatness of $k[X,Y]/(XY)$ over $k[X]$ by the torsion element $\bar Y$ — the flat-family / tearing-family contrast ([[Def - Flat Module]], [[Def - Free Module]], [[Thm - Characterization of Flat Modules]], [[Def - Polynomial Ring]], [[Def - Ideal]]).

- [[Ex - The maximal ideal (X,Y) is torsion-free but not flat]] (⭐⭐⭐) — the sharpest separation: $\mathfrak m = (X,Y)\trianglelefteq k[X,Y]$ is torsion-free (submodule of a domain) yet not flat, shown via the [[Thm - Characterization of Flat Modules|ideal criterion]] by exhibiting the non-zero Koszul element $Y\otimes X - X\otimes Y\in\mathfrak m\otimes\mathfrak m$ in the kernel of multiplication, with non-vanishing certified by a bilinear map built from the cotangent space $\mathfrak m/\mathfrak m^2$ ([[Def - Flat Module]], [[Def - Tensor Product of Modules]], [[Thm - Tensoring is Right Exact]], [[Thm - Characterization of Flat Modules]], [[Def - Ideal]]).

- [[Ex - Free implies projective implies flat implies torsion-free]] (⭐⭐) — establish the chapter's structural backbone, each implication a clean lemma: free is a summand of itself (projective), projective is a summand of free with flatness inherited through the direct sum, and flat is torsion-free because tensoring the injection $\mu_r : R\to R$ recovers multiplication by $r$ on $M$ ([[Def - Free Module]], [[Def - Projective Module]], [[Def - Flat Module]], [[Thm - Projective iff Direct Summand of a Free Module]], [[Thm - Characterization of Flat Modules]]).
