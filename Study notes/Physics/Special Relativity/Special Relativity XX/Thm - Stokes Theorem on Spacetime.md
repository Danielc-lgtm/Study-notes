---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Submanifolds of Spacetime"
  - "Def - The Exterior Derivative"
  - "Def - Integration of Forms and the Volume Element"
  - "Def - Alternate Forms and the Exterior Product"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. $\mathscr{V}$ is an oriented compact submanifold-with-boundary of spacetime $\mathscr{E}$, of dimension $p$, with boundary $\partial\mathscr{V}$ of dimension $p-1$ carrying the [[Def - Submanifolds of Spacetime|induced (outward-normal-first) orientation]]. $A$ is a differential $(p-1)$-form on $\mathscr{E}$ and $\mathrm{d}A$ its [[Def - The Exterior Derivative|exterior derivative]], a $p$-form. Integration of a $p$-form over a $p$-submanifold is as defined in [[Def - Integration of Forms and the Volume Element]]. Full registry on [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem]].

---

# Statement

> **Stokes' theorem on spacetime.** Let $\mathscr{V}$ be an oriented, compact submanifold-with-boundary of $\mathscr{E}$, of dimension $p \in \{1,2,3,4\}$, with boundary $\partial\mathscr{V}$ of dimension $p-1$. Let $A$ be a differential $(p-1)$-form. Then
> $$\int_{\mathscr{V}} \mathrm{d}A \;=\; \int_{\partial\mathscr{V}} A,$$
> where $\partial\mathscr{V}$ is endowed with the orientation induced from $\mathscr{V}$ (outward-normal-first). When $\partial\mathscr{V} = \emptyset$, the right-hand side is $0$.

> **Corollary (low-dimensional cases).** The identity specialises to: the fundamental theorem of calculus ($p=1$); the Green–Riemann formula ($p=2$, planar region, $A = P\,\mathrm{d}x + Q\,\mathrm{d}y$); and the Kelvin–Stokes curl theorem ($p=2$, spacelike surface, $\int_{\mathscr{V}}\mathrm{curl}\,\vec{A}\cdot\mathrm{d}\vec{S} = \oint_{\partial\mathscr{V}}\vec{A}\cdot\mathrm{d}\vec{\ell}$).

The theorem is **metric-independent**: both integrals are integrals of differential forms ([[Def - Integration of Forms and the Volume Element|defined without the metric]]), so the identity does not involve $g$.

---

# Motivation

The fundamental theorem of calculus, $\int_a^b f'\,\mathrm{d}x = f(b) - f(a)$, has a shape that is easy to miss: it equates the integral of a *derivative* over a region $[a,b]$ with the values of the original function on the *boundary* $\{a, b\}$ of that region, the endpoint $b$ counted positively and $a$ negatively. Read this way it is a statement of the form "$\int_{\text{region}}(\text{derivative}) = \int_{\text{boundary}}(\text{original})$", and the question this theorem answers is: does that shape persist in higher dimensions, with the right notion of "derivative" (the exterior derivative) and "boundary" (the geometric boundary with its induced orientation)?

It does, exactly, and the persistence is one of the great unifications in mathematics. Green's theorem, the Kelvin–Stokes curl theorem, and the Gauss divergence theorem are not three separate facts to be memorised; they are the cases $p = 2, 2, 3$ of this single identity, distinguished only by the dimension of the region and by which classical object the abstract $(p-1)$-form $A$ unpacks into. The role of this theorem in the chapter is to be the *one* integral theorem from which all the others, and in particular the Gauss–Ostrogradsky theorems that the conservation laws of relativity run on, are extracted by specialisation.

Why should one expect the exterior derivative and the boundary operator to be partners? The deepest reason is that both square to zero — $\mathrm{d}\circ\mathrm{d} = 0$ and $\partial\circ\partial = 0$ (the boundary of a boundary is empty). Two operations that both square to zero, related by an integral pairing, are *adjoint*, and Stokes' theorem $\langle\mathrm{d}A,\mathscr{V}\rangle = \langle A,\partial\mathscr{V}\rangle$ is precisely that adjointness made explicit. This is why the theorem is metric-independent: adjointness is about the pairing between forms and regions, which never measures a length. Penrose, struck by how completely this one identity subsumes the classical theorems, suggested abandoning Stokes' name and calling it *the fundamental theorem of exterior calculus* — the multidimensional generalisation of the fundamental theorem of calculus, no more and no less.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$A$ is a $(p-1)$-form on an oriented compact $p$-region $\mathscr{V}$ with boundary". The art is recognising the many disguises this wears.

The first disguised source is **"an integrand is the exterior derivative of something"**. Whenever you face $\int_{\mathscr{V}}\omega$ for a $p$-form $\omega$, ask whether $\omega = \mathrm{d}A$ for some $(p-1)$-form $A$ — if so, the integral collapses to a boundary integral $\int_{\partial\mathscr{V}} A$, which is one dimension lower and often trivial. The bridge is the recognition of an exact form, and it is nonobvious because $\omega$ is rarely *presented* as a derivative; you must spot it. *Example problem:* the integral of a curl over a surface is the integral of $\mathrm{d}$(the potential 1-form), so it reduces to a line integral of the potential around the boundary ([[Ex - Green and Kelvin-Stokes as cases of the master theorem]]).

The second disguised source is **"a flux through a closed hypersurface"**. The Hodge dual $\star\underline{v}$ of a vector's 1-form is a 3-form, and the flux of $\vec{v}$ through a closed hypersurface $\partial\mathscr{V}$ is $\int_{\partial\mathscr{V}}\star\underline{v}$ — exactly the right-hand side of Stokes' theorem with $A = \star\underline{v}$. The bridge is the flux-as-Hodge-dual identity ([[Def - Volume, Area, Length Elements and Flux Integrals]]). The nonobviousness is that a "flux", which looks like a physical measurement, is secretly a boundary integral of a form, hence convertible to a volume integral of $\mathrm{d}\star\underline{v}$. *Example problem:* deriving the 4D Gauss theorem ([[Ex - Stokes' theorem for a three-form gives the four-dimensional Gauss theorem]]).

The third disguised source is **"a quantity defined on a boundary should be recast as a bulk integral"**. Any quantity living on $\partial\mathscr{V}$ — a boundary charge, a circulation, a winding — can be lifted to an integral over the interior $\mathscr{V}$ of $\mathrm{d}A$, which is sometimes easier to evaluate or to bound. The bridge is just reading Stokes' theorem right-to-left. *Example problem:* showing a circulation $\oint_{\partial\mathscr{V}}\vec{A}\cdot\mathrm{d}\vec{\ell}$ vanishes by exhibiting it as $\int_{\mathscr{V}}\mathrm{d}(\underline{A})$ with $\mathrm{d}\underline{A} = 0$ (an irrotational field).

**Targets (Output Amplification)**

The conclusion is "$\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$".

Combine the conclusion with **$\mathrm{d}A = 0$ (a closed form)**. Then $\int_{\partial\mathscr{V}} A = \int_{\mathscr{V}} 0 = 0$: the integral of a closed form over any boundary vanishes. The further result is that the integral of a closed form over a cycle depends only on the cycle's homology class — the foundation of de Rham cohomology. The combination is nonobvious because it turns a vanishing-derivative condition into a statement about integrals over *boundaries*, not over the region itself. *Example:* the integral of a closed-but-not-exact form over a non-bounding cycle is a topological invariant (a monopole flux).

Combine the conclusion with **the identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$**. Then the boundary flux $\int_{\partial\mathscr{V}}\star\underline{v}$ equals the bulk integral $\int_{\mathscr{V}}(\nabla\cdot\vec{v})\epsilon = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$. The further result is the four-dimensional Gauss–Ostrogradsky theorem ([[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)]]), the engine of every relativistic conservation law. The combination is useful because it is the precise bridge from "flux out of a boundary" to "integral of a divergence inside".

Combine the conclusion with **$\nabla\cdot\vec{v} = 0$ and a closed boundary**. Then the total flux out of any closed hypersurface vanishes, and applied to a slab between two spacelike slices this says the flux through the two slices agree. The further result is the conservation and slice-independence of a total charge ([[Ex - Charge conservation as a flux statement]]). The combination closes the loop between local and global conservation: a vanishing four-divergence everywhere *is* a vanishing net boundary flux.

---

# Why Is It True

The intuition is "everything cancels in the interior, only the boundary survives" — and seeing it clearly in the one-dimensional case makes the general statement unsurprising.

Take the fundamental theorem of calculus. Chop $[a,b]$ into tiny cells $[x_i, x_{i+1}]$. Over each cell, $\int_{x_i}^{x_{i+1}} f' \approx f(x_{i+1}) - f(x_i)$ — the derivative integrated over a cell equals the change of $f$ across the cell, which is $f$ evaluated on the cell's two boundary points with opposite signs. Now sum over all cells. The interior boundary points each appear *twice*, once as the right end of one cell ($+f(x_i)$) and once as the left end of the next ($-f(x_i)$), and these cancel in pairs. Only the two *outermost* points, $a$ and $b$, appear once, and they survive: the sum telescopes to $f(b) - f(a)$. The boundary of the whole region is what is left when all the internal boundaries annihilate each other.

The general case is the same telescoping in higher dimensions. Chop the region $\mathscr{V}$ into tiny coordinate cells. Over each cell, $\int_{\text{cell}}\mathrm{d}A$ equals (by the definition of $\mathrm{d}$ and a one-cell computation) the integral of $A$ around the cell's boundary, with the induced orientation. Sum over all cells. Each internal face is shared by two adjacent cells, and the outward-normal-first orientation makes the two cells traverse that shared face with *opposite* orientations — so the two contributions cancel. Only the faces lying on the *true* boundary $\partial\mathscr{V}$ are unshared, and they survive. The grand sum telescopes to $\int_{\partial\mathscr{V}} A$. **The whole theorem is the cancellation of every internal boundary against its neighbour, leaving only the outer skin — and the outward-normal-first orientation is exactly the convention under which adjacent cells cancel.**

This is why the orientation convention is not a technicality but the load-bearing hypothesis: it is what guarantees that shared faces cancel rather than add. Reverse it and the internal faces would *double* instead of cancelling, and the theorem would fail. And this is why the theorem is metric-free: the cancellation is a combinatorial fact about how cells share faces, with no reference to lengths or angles — the metric never appears.

---

# What Makes This Hard

The proof of the general statement is genuinely hard — it requires partitions of unity to patch local computations together, and the careful book-keeping of induced orientations on cell faces — which is why the source (and this page) cite the manifold version rather than reproving it. The conceptual stumbling block for most readers is the *orientation* of the boundary: getting the outward-normal-first convention right, and in particular seeing that for a four-region between two spacelike slices the past slice acquires a *reversed* orientation, so that "flux out of the future slice minus flux out of the past slice" comes out with the correct sign. The most common error is to apply the theorem with a boundary orientation chosen by some other rule (counterclockwise, inward-first), which flips the sign of the entire result.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire argument** (taking the manifold version of Stokes as a cited black box, exactly as the source does).

**High-level strategy:**
Reduce to the manifold version of Stokes' theorem by recognising Minkowski spacetime as a flat oriented $4$-manifold and a submanifold-with-boundary as an oriented $p$-manifold-with-boundary; the integrals of forms defined in this chapter coincide with the manifold integrals; the induced orientation is the outward-normal-first one. Then specialise to the classical cases by choosing $A$.

**Subgoal decomposition:**

1. **Identify the objects with their manifold counterparts.** A $p$-dimensional submanifold-with-boundary of $\mathscr{E}$ is an oriented smooth $p$-manifold-with-boundary; the integral $\int_{\mathscr{V}} A$ of a $p$-form is the manifold integral; $\mathrm{d}A$ is the manifold exterior derivative.
   - *Hint:* The chapter's "integrate the single tangential component over adapted coordinates" is exactly the chart-by-chart definition of the manifold integral.
   - *Why needed:* It licenses citing the manifold theorem, which is proved in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

2. **Match the orientations.** The induced (outward-normal-first) orientation on $\partial\mathscr{V}$ defined in this chapter is the standard induced boundary orientation of the manifold theorem.
   - *Hint:* Both declare a boundary frame positive iff prepending the outward vector gives a positive frame of $\mathscr{V}$.
   - *Why needed:* The sign in $\int_{\mathscr{V}}\mathrm{d}A = +\int_{\partial\mathscr{V}} A$ depends entirely on this match.

3. **Invoke the manifold theorem.** Conclude $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$.
   - *Hint:* No new computation — the work is the identification.
   - *Why needed:* This is the statement.

4. **Specialise to recover classical theorems.** Choose $A = f$ ($p=1$, FTC); $A = P\,\mathrm{d}x + Q\,\mathrm{d}y$ ($p=2$, Green); a 1-form on a 2-surface ($p=2$, Kelvin–Stokes).
   - *Hint:* Compute $\mathrm{d}A$ in coordinates and read off the classical "derivative" (the difference $\partial Q/\partial x - \partial P/\partial y$, or a curl component).
   - *Why needed:* It confirms the abstract statement reduces correctly and supplies the worked examples.

---

# Lemma Decomposition

> [!note]- Lemma 1: One-cell case is the definition of the exterior derivative
> **Statement:** For a single small coordinate cell $C = [0,h]^p$ and a $(p-1)$-form $A$, $\int_C \mathrm{d}A = \int_{\partial C} A$ to leading order in $h$.
>
> **Hint:** Expand $\mathrm{d}A$ in coordinates; each term $\partial_a A_{\dots}$ integrates over the cell to a difference of $A$ on opposite faces, by the one-dimensional fundamental theorem applied in the $x^a$ direction.
>
> **Why needed:** It is the atom from which the global theorem is assembled by summing over cells; it is where the exterior derivative's coordinate formula meets the boundary.
>
> > [!note]- Full proof
> > Write $A = \sum_a A_a\,\mathrm{d}x^{b_1}\wedge\dots\widehat{\mathrm{d}x^a}\dots$, omitting the $a$-th differential. Then $\mathrm{d}A = \sum_a (\partial_a A_a)\,\mathrm{d}x^1\wedge\dots\wedge\mathrm{d}x^p$ (with signs absorbed by reordering), so $\int_C\mathrm{d}A = \sum_a\int_C\partial_a A_a\,\mathrm{d}^p x$. For each $a$, the integral $\int\partial_a A_a\,\mathrm{d}x^a$ over $[0,h]$ in the $a$-direction is $A_a|_{x^a=h} - A_a|_{x^a=0}$ by the fundamental theorem of calculus; integrating the remaining $p-1$ coordinates over their faces gives the difference of $\int A$ over the two faces $x^a = h$ and $x^a = 0$, which with the induced orientations is their oriented sum. Summing over $a$ gives $\int_{\partial C} A$, the integral over all $2p$ faces with induced orientation. $\blacksquare$

> [!note]- Lemma 2: Internal faces cancel
> **Statement:** When $\mathscr{V}$ is subdivided into cells, the contributions of every face shared by two adjacent cells cancel, leaving only the faces on $\partial\mathscr{V}$.
>
> **Hint:** Two cells sharing a face induce *opposite* orientations on it (the outward direction of one is the inward direction of the other).
>
> **Why needed:** It is the telescoping that turns the sum of one-cell identities into the global identity; it is where the outward-normal-first convention does its work.
>
> > [!note]- Full proof
> > Let $F$ be a face shared by adjacent cells $C_1$ and $C_2$. The induced orientation on $F$ as part of $\partial C_1$ uses the outward normal of $C_1$ at $F$; the induced orientation on $F$ as part of $\partial C_2$ uses the outward normal of $C_2$ at $F$. But the outward normal of $C_1$ at the shared face points *into* $C_2$, i.e. it is the *inward* normal of $C_2$ — the two outward normals are opposite. By the outward-normal-first rule, the two induced orientations on $F$ are therefore opposite, so $\int_F A$ (as part of $\partial C_1$) and $\int_F A$ (as part of $\partial C_2$) are negatives of each other and cancel in the sum $\sum_i\int_{\partial C_i} A$. Only faces belonging to a single cell — those on the outer boundary $\partial\mathscr{V}$ — survive. $\blacksquare$

> [!note]- Lemma 3: The chapter's form-integral is the manifold integral
> **Statement:** The integral $\int_{\mathscr{V}} A$ defined in [[Def - Integration of Forms and the Volume Element]] (integrate the single tangential component $A_{(4-p)\dots 3}$ over adapted coordinates) coincides with the standard manifold integral of a form over an oriented manifold-with-boundary.
>
> **Hint:** Both reduce, in a chart, to a Lebesgue integral of the form's top-degree component over the coordinate domain, with orientation fixing the sign.
>
> **Why needed:** It is what licenses importing the manifold version of Stokes' theorem; without it the present statement would be a separate theorem to prove from scratch.
>
> > [!note]- Full proof
> > In adapted coordinates $(x^a)_{4-p\le a\le 3}$ on $\mathscr{V}$, a $p$-form $A$ pulls back to $A_{(4-p)\dots 3}\,\mathrm{d}x^{4-p}\wedge\dots\wedge\mathrm{d}x^3$, and the manifold integral of a form in a single chart is by definition $\int A_{(4-p)\dots 3}\,\mathrm{d}^p x$ over the chart's coordinate domain, with the orientation determining whether to use $+$ or $-$ the coordinate measure. This is verbatim the chapter's definition (16.16). For submanifolds covered by several adapted charts the manifold integral uses a partition of unity to sum chart contributions; since the regions of interest in flat spacetime are typically single coordinate boxes, this reduces to the single-chart formula. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** The right-hand side $\int_{\partial\mathscr{V}} A$ is well defined because $\partial\mathscr{V}$, by [[Def - Submanifolds of Spacetime|the definition of a submanifold with boundary]], is a $(p-1)$-dimensional submanifold (without boundary), oriented by the induced orientation, and $A$ is a $(p-1)$-form — so it integrates over $\partial\mathscr{V}$ by [[Def - Integration of Forms and the Volume Element|the form-integration definition]]. The left-hand side is well defined because $\mathrm{d}A$ is a $p$-form and $\mathscr{V}$ a $p$-submanifold.
>
> By Lemma 3, the integrals $\int_{\mathscr{V}}\mathrm{d}A$ and $\int_{\partial\mathscr{V}} A$ of this chapter coincide with the manifold integrals over $\mathscr{V}$ and $\partial\mathscr{V}$ regarded as oriented smooth manifolds-with-boundary, $\mathscr{V}$ being an oriented compact $p$-manifold-with-boundary embedded in flat $\mathbb{R}^4 = \mathscr{E}$ and $\partial\mathscr{V}$ its boundary with the induced orientation (which, by the matching of orientation conventions, is the standard outward-normal-first manifold boundary orientation). The manifold version of Stokes' theorem ([[Thm - Stokes' Theorem on Manifolds]]), proved via partitions of unity and the half-space model in [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]], states that for a compactly supported $(p-1)$-form $A$ on such a manifold,
> $$\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A .$$
> Since $\mathscr{V}$ is compact, $A$ restricted to $\mathscr{V}$ is compactly supported, so the hypothesis is met and the identity holds.
>
> The structure of that proof is exactly Lemmas 1 and 2: locally (in each chart of a partition of unity) the one-cell identity of Lemma 1 holds, and summing over the subdivision the internal faces cancel by Lemma 2, leaving only $\partial\mathscr{V}$. When $\partial\mathscr{V} = \emptyset$ there are no surviving faces and the right-hand side is $0$.
>
> **Specialisations.** With $p=1$, $\mathscr{V} = \{t=x=y=0,\ a\le z\le b\}$ and $A = f$ a scalar, $\mathrm{d}A = (\partial_z f)\,\mathrm{d}z$, so the left side is $\int_a^b\partial_z f\,\mathrm{d}z$ and the right side, over $\partial\mathscr{V} = \{B\}-\{A\}$, is $f(B)-f(A)$ — the fundamental theorem of calculus. With $p=2$ and $A = P\,\mathrm{d}x + Q\,\mathrm{d}y$ on a planar region, $\mathrm{d}A = (\partial_x Q - \partial_y P)\,\mathrm{d}x\wedge\mathrm{d}y$, giving the Green–Riemann formula $\int_{\mathscr{V}}(\partial_x Q - \partial_y P)\,\mathrm{d}x\,\mathrm{d}y = \oint_{\partial\mathscr{V}} P\,\mathrm{d}x + Q\,\mathrm{d}y$. With $p=2$ on a spacelike 2-surface, recognising $\partial_2 A_3 - \partial_3 A_2$ as a component of $\mathrm{curl}\,\vec{A}$ and $\mathrm{d}x^2\mathrm{d}x^3$ as the area element gives $\int_{\mathscr{V}}\mathrm{curl}\,\vec{A}\cdot\mathrm{d}\vec{S} = \oint_{\partial\mathscr{V}}\vec{A}\cdot\mathrm{d}\vec{\ell}$, the Kelvin–Stokes theorem. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The winding number of a planar curve.** For the closed 1-form $A = \frac{-y\,\mathrm{d}x + x\,\mathrm{d}y}{x^2+y^2}$ on the punctured plane, $\mathrm{d}A = 0$ away from the origin, yet $\oint_C A = 2\pi$ for a loop $C$ encircling the origin. The apparent contradiction with "$\int_{\partial\mathscr{V}} A = \int_{\mathscr{V}}\mathrm{d}A = 0$" is resolved by noting that no $\mathscr{V}$ with $\partial\mathscr{V} = C$ avoids the puncture, so $A$ is not exact on any such region. This is the prototype of how a closed-but-not-exact form detects a topological hole — the application is out-of-distribution because it uses Stokes' theorem to *prove a non-vanishing* by exhibiting an obstruction.

**Cauchy's integral theorem in complex analysis.** Writing $f(z)\,\mathrm{d}z$ as a complex 1-form, holomorphicity is the statement $\mathrm{d}(f\,\mathrm{d}z) = 0$ (the Cauchy–Riemann equations), and Stokes' theorem then gives $\oint_{\partial\mathscr{V}} f\,\mathrm{d}z = \int_{\mathscr{V}}\mathrm{d}(f\,\mathrm{d}z) = 0$ — Cauchy's theorem. The residue theorem is the punctured-domain version, with the residues the periods of the form around the punctures. The application is surprising because complex contour integration looks unrelated to spacetime integration, yet both are Stokes.

**Conservation of probability in quantum mechanics.** The probability current $j^\mu = (\rho, \mathbf{j})$ of a wavefunction satisfies $\partial_\mu j^\mu = 0$ (continuity), so $\star\underline{j}$ is closed and its flux through any closed hypersurface vanishes — total probability is conserved and the same on every time slice. This is the identical structure to charge conservation, with the probability current in place of the electric current, and it shows the master theorem governs the unitarity of quantum mechanics just as it governs charge conservation.

---

# Bridges

- **[[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)]]** — the two divergence theorems are this theorem applied to flux integrals. The 4D version is Stokes for the 3-form $A = \star\underline{v}$ combined with the identity $\mathrm{d}\star\underline{v} = (\nabla\cdot\vec{v})\epsilon$, so that $\int_{\partial\mathscr{V}}\star\underline{v} = \int_{\mathscr{V}}\nabla\cdot\vec{v}\,\mathrm{d}U$; the 3D version is the case of a region inside a spatial slice. Stokes' theorem is metric-free, but inserting the divergence identity makes the Gauss–Ostrogradsky corollaries metric-dependent.

- **[[Thm - Stokes' Theorem on Manifolds]]** — the general statement, of which this is the affine-spacetime specialisation. The manifold version holds on any oriented smooth manifold-with-boundary for compactly supported forms and is proved by partitions of unity; the present version restricts the manifold to a region of flat $\mathbb{R}^4$ and adds explicit Minkowski formulas (the volume element $\sqrt{|g|}\,\mathrm{d}^4x$, the flux $\int\star\underline{v}$). The two are the same theorem; this page is where it is put to work on spacetime regions, and it is a *different file* from the manifold version because it carries the Minkowski-specific apparatus.

- **The classical integral theorems of vector calculus** — the fundamental theorem of calculus, the Green–Riemann formula, the Kelvin–Stokes curl theorem, and the Gauss divergence theorem are the cases $p=1,2,2,3$ of this single identity. Each is obtained by choosing $A$ and reading off which component of $\mathrm{d}A$ the classical "derivative" (gradient, curl, divergence) corresponds to — the gradient, curl, and divergence being the exterior derivative on $0$-, $1$-, and $2$-forms in three dimensions dressed with the Hodge star.

- **[[Def - The Exterior Derivative]]** — the property $\mathrm{d}\circ\mathrm{d} = 0$ is the dual of $\partial\circ\partial = 0$ (the boundary of a boundary is empty), and Stokes' theorem is the pairing that makes them adjoint. This is why a form that is exact ($A = \mathrm{d}B$) integrates to zero over any cycle, and a region that is a boundary ($\mathscr{V} = \partial W$) gives zero for any closed form — the two halves of de Rham theory.

---

# Unlocked by This

> [!tip] de Rham Cohomology and the de Rham Theorem *(from Algebraic Topology)*
> Because $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$ holds universally, the integral of a **closed** form over a **cycle** depends only on the form's cohomology class and the cycle's homology class. This bilinear pairing between **de Rham cohomology** (closed forms modulo exact ones) and singular homology (cycles modulo boundaries) is an isomorphism — the **de Rham theorem** — identifying the analytic invariants of a manifold (which forms can be integrated to give nonzero periods) with its topological invariants (which cycles fail to bound). Stokes' theorem is the engine of the entire correspondence, and it is why physical fluxes of closed forms can be topologically quantised.

> [!tip] Conserved Charges in Field Theory and Gravitation *(from Field Theory and General Relativity)*
> Every conservation law in relativistic physics is this theorem applied to a current. **Electric charge** ($\nabla\cdot J = 0$), **energy-momentum** ($\nabla_\mu T^{\mu\nu} = 0$), **baryon number**, and **probability** all become "the flux through any closed hypersurface vanishes", hence "the total on a spacelike slice is conserved and slice-independent", by exactly the argument in [[Ex - Charge conservation as a flux statement]]. In general relativity, where no global spacelike slice need carry a conserved energy, the only conserved charges are flux integrals over a **sphere at spatial infinity** (the ADM and Komar masses) — Stokes' theorem taken in the asymptotic region, which is the deepest manifestation of the theorem in physics.
