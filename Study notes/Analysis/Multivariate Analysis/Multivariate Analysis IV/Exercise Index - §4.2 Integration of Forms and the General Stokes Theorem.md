---
type: exercise-index
subject: multivariate-analysis
section: "4.2"
tags: [analysis, multivariate-analysis]
---

## §4.2 Integration of Forms and the General Stokes Theorem — Exercises

The exercises of §4.2 drill the integration of forms and the general Stokes theorem. Integration over a graph reduces to pullback to the parameter domain, where the orientation-tracking and the Jacobian sign appear together; the angular form $(x\,dy - y\,dx)/(x^2 + y^2)$ on the punctured plane is closed but not exact (the topological obstruction is the hole at $0$); and verifying Stokes on the cube boundary reveals the Fundamental Theorem of Calculus as the slab-integration case. The unifying observation: Stokes unifies all the classical integral theorems (Green's, Gauss's, the divergence theorem) under one form-language identity $\int_M d\omega = \int_{\partial M} \omega$.

- [[Ex - Integrating a 2-form over a surface]] (⭐⭐) — integrate explicit $2$-forms over a graph surface by pulling them back to the flat parameter domain, see that a graph chart makes two of the three differential-pullbacks trivial, track the reorder signs that a non-coordinate differential produces, and confirm that swapping parameters (negative Jacobian) reverses the orientation and negates the integral ([[Def - Pullback of a Differential Form]], [[Def - Orientation and the Integral of a Form]], [[Def - The Wedge Product]], [[Def - Differential Form]]).

- [[Ex - A closed form that is not exact]] (⭐⭐⭐) — show the angular form $(x\,dy - y\,dx)/(x^2+y^2)$ on the punctured plane is closed by checking $\partial_x Q = \partial_y P$, compute its period $\int_{S^1}\omega = 2\pi$, and conclude via the Stokes corollary "exact forms have zero period" that it is not exact — the contractibility hypothesis of the Poincaré lemma fails on a domain with a hole ([[Def - The Exterior Derivative]], [[Thm - The General Stokes Theorem]], [[Thm - The Poincaré Lemma]], [[Def - Pullback of a Differential Form]], [[Def - Differential Form]]).

- [[Ex - Stokes' theorem on the boundary of a cube]] (⭐⭐) — verify $\int_M d\beta = \int_{\partial M}\beta$ for a $2$-form on the solid cube by computing both sides directly, finding that four of the six faces kill the form (a differential of a constant coordinate restricts to zero) and the two transverse faces combine — via opposite induced orientations — into the Fundamental Theorem of Calculus across the slab ([[Thm - The General Stokes Theorem]], [[Def - The Exterior Derivative]], [[Def - Orientation and the Integral of a Form]], [[Def - Pullback of a Differential Form]], [[Def - Differential Form]]).
