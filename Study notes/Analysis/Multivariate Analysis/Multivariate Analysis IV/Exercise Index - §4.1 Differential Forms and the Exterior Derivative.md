---
type: exercise-index
subject: multivariate-analysis
section: "4.1"
tags: [analysis, multivariate-analysis]
---

## §4.1 Differential Forms and the Exterior Derivative — Exercises

- [[Ex - Computing wedge products and exterior derivatives]] — drill the mechanics: expand a wedge product by distributivity-and-anticommutativity (deleting repeated-index terms), compute $d$ of $1$- and $2$-forms by the "differentiate through the missing coordinate" shortcut, verify $d(df) = 0$ by hand, and read off that $d$ on a $1$-form is the curl ([[Def - The Wedge Product]], [[Def - The Exterior Derivative]], [[Def - Differential Form]]).

- [[Ex - The exterior derivative squares to zero]] — prove $d\circ d = 0$ for every form by exposing the double sum $\sum_{\ell,m}\partial_m\partial_\ell a_j\,dx_m\wedge dx_\ell\wedge dx_j$ and pairing the $(\ell,m)$ term against the $(m,\ell)$ term: equal coefficients (Schwarz's theorem on mixed partials) against opposite basic forms (wedge antisymmetry) cancel, then deduce $\operatorname{curl}\operatorname{grad} = 0$ and $\operatorname{div}\operatorname{curl} = 0$ ([[Def - The Exterior Derivative]], [[Def - The Wedge Product]], [[Def - Differential Form]]).

- [[Ex - Pulling back a differential form]] — execute the pullback recipe (substitute into coefficients, replace $dx_j$ by $dF_j$, expand the wedge) for polar coordinates and a sphere parametrization, confirm the top-degree Jacobian identity $F^*(dx\wedge dy) = (\det DF)\,dr\wedge d\theta$, and verify the naturality identity $d(F^*\alpha) = F^*(d\alpha)$ in a concrete case ([[Def - Pullback of a Differential Form]], [[Def - The Exterior Derivative]], [[Def - The Wedge Product]], [[Def - Differential Form]]).
