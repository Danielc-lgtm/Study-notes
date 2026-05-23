---
type: exercise-index
subject: differential-geometry
section: "5.4"
tags: [geometry, differential-geometry]
---

## §5.4 The Straightening Theorem — Exercises

These exercises explore the local rigidity of nonvanishing smooth vector fields: the [[Thm - Canonical Form for a Nonvanishing Vector Field|Straightening Theorem]] says any such field looks like $\partial/\partial s^1$ in suitable coordinates. The exercises in the wider sections of the chapter — especially the explicit linear-flow exercise — illustrate the meaning of the straightening (the linear flow $e^{tA} x$ is locally straightenable away from $0$), and the coordinate-commutation exercise gives the multi-field analogue (joint straightening of commuting fields). The recurring technique is to construct the straightening map by flowing a transverse hypersurface and applying the inverse function theorem.

- [[Ex - Constructing the Flow of a Linear Vector Field]] (⭐⭐) — The linear flow $\phi_t(x) = e^{tA} x$ on $\mathbb{R}^n$ is a concrete instance where the Straightening Theorem applies away from the singular set $\{x : Ax = 0\}$; in straightened coordinates the linear flow becomes the constant $\partial/\partial s^1$. ([[Def - Smooth Vector Field]], [[Def - Flow of a Vector Field]], [[Def - Complete Vector Field]], [[Thm - Fundamental Theorem on Flows]])

- [[Ex - The Coordinate Vector Fields Commute]] (⭐) — The multi-field Straightening Theorem (Lee 9.46) says a commuting frame is locally a coordinate frame. This exercise establishes the converse direction: in any coordinate chart, the coordinate vector fields automatically commute. So bracket-vanishing is a *necessary* condition for joint straightening — the converse is the harder direction of Lee 9.46. ([[Def - The Lie Bracket of Vector Fields]], [[Def - Smooth Vector Field]])

- [[Ex - Two Vector Fields with Nonzero Lie Bracket]] (⭐) — $X = \partial_x$ and $Y = x \partial_y$ on $\mathbb{R}^2$ have nonzero bracket and non-commuting flows, hence cannot be jointly straightened to coordinate vector fields. The single-field Straightening Theorem still applies — straighten $X$ (already in straightened form), and $Y$ in the same coordinates is $x \partial_y$ (with components depending on $s^1 = x$, the straightening coordinate of $X$). The obstruction to *joint* straightening is exactly the bracket $[X, Y] = \partial_y \neq 0$. ([[Def - The Lie Bracket of Vector Fields]], [[Def - Flow of a Vector Field]], [[Thm - Commuting Flows Theorem]], [[Thm - Canonical Form for a Nonvanishing Vector Field]])
