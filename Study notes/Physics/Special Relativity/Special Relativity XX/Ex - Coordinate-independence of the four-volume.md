---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Integration of Forms and the Volume Element"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. Let $(x^\alpha)\mapsto(x'^\alpha)$ be a change of coordinates on spacetime, with Jacobian matrix $P^\alpha{}_\beta = \partial x^\alpha/\partial x'^\beta$ and $J = \det P$. Show that the metric determinants in the two systems are related by $\det g' = J^2\det g$, and deduce $\sqrt{|g'|} = |J|\,\sqrt{|g|}$.
2. Using the change-of-variables formula for a Lebesgue integral, $\mathrm{d}^4x = |J|\,\mathrm{d}^4x'$, show that $\mathrm{vol}\,\mathscr{V} = \int_{\mathscr{V}}\sqrt{|g|}\,\mathrm{d}^4x$ takes the same value in both coordinate systems.
3. Now show that the integral of a 4-form, $\int_{\mathscr{V}} A = \int_{\mathscr{V}} A_{0123}\,\mathrm{d}^4x$, is coordinate-independent *without using the metric at all* — i.e. directly from the transformation law of the component $A_{0123}$.
4. Explain in one or two sentences how parts 2 and 3 illustrate that "the four-volume is a metric quantity, but the integral of a form is not".

**Recall:**

The four-volume and the integral of a 4-form are defined as follows.

![[Def - Integration of Forms and the Volume Element#The Definition]]

The metric components transform as a type-$(0,2)$ tensor: $g'_{\alpha\beta} = g_{\mu\nu}\,P^\mu{}_\alpha P^\nu{}_\beta$, where $P^\mu{}_\alpha = \partial x^\mu/\partial x'^\alpha$. The single component of a 4-form transforms as $A'_{0123} = A_{\mu\nu\rho\sigma}\,P^\mu{}_0 P^\nu{}_1 P^\rho{}_2 P^\sigma{}_3$, which, by total antisymmetry of $A$, equals $A_{0123}\det P = A_{0123}\,J$.

---

# Convergent Strategy

**Problem class.** A *structural* problem: prove a definition is independent of the arbitrary choice (here the coordinate system) used to express it. The [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem#Sources and Targets|topic strategy]] names this as one of the recurring targets, and the prototype is exactly this $\sqrt{-\det g'} = |J|\sqrt{-\det g}$ calculation.

**Assumption pattern.** A change of coordinates is given, and the metric and the form transform as tensors. The signpost is that the *definition* of the four-volume mentions a particular coordinate system, so well-posedness *requires* checking the choice does not matter. The two transformation laws — the metric determinant picking up $J^2$, the form component picking up $J$ — are the only inputs.

**Theorem routing.** Part 1 is the multiplicativity of determinants applied to $g' = P^{\mathsf T} g P$. Part 2 combines $\sqrt{|g'|} = |J|\sqrt{|g|}$ with the change-of-variables $\mathrm{d}^4x = |J|\,\mathrm{d}^4x'$: substituting the old measure for the new one introduces a factor $|J|$, and the metric factor $\sqrt{|g|}$ supplies exactly that same $|J|$ when re-expressed as $\sqrt{|g'|}$, so the product $\sqrt{|g|}\,\mathrm{d}^4x$ regarded in the new coordinates equals $\sqrt{|g'|}\,\mathrm{d}^4x'$. Part 3 uses only $A'_{0123} = J\,A_{0123}$ and the same change-of-variables, the metric never appearing.

**Key decision point.** The crux is keeping the *direction* of the Jacobian straight: whether $J = \partial x/\partial x'$ or $\partial x'/\partial x$, and hence whether the two $|J|$ factors cancel or compound. The clean way is to fix one convention ($P = \partial x/\partial x'$, $J = \det P$) and track both the metric and the measure consistently; getting this wrong is the only way the proof fails.

---

# Legal Operations Used

1. **Operation 1 from the topic page (write the four-volume element as $\sqrt{|g|}\,\mathrm{d}^4x$).** The whole exercise is the proof that this prescription is well-defined: the factor $\sqrt{|g|}$ is exactly what makes the prescription coordinate-independent, and parts 1–2 verify it.

2. **Operation 2 from the topic page (integrate a 4-form by reading off its single component).** Part 3 shows the *form*-integral version of the prescription is coordinate-independent for a structurally different reason — the antisymmetry of the component, not the metric.

---

# Hints

> [!note]- Hint 1
> Write the metric transformation in matrix form, $g' = P^{\mathsf T} g P$ with $P^\mu{}_\alpha = \partial x^\mu/\partial x'^\alpha$. Take determinants and use $\det(P^{\mathsf T}) = \det P = J$: $\det g' = J^2\det g$. Since both determinants are negative, $\sqrt{|g'|} = |J|\sqrt{|g|}$.

> [!note]- Hint 2
> Under the substitution $x = x(x')$, the integral $\int f(x)\,\mathrm{d}^4x$ becomes $\int f(x(x'))\,|J|\,\mathrm{d}^4x'$ with $J = \det(\partial x/\partial x')$. Apply this to $f = \sqrt{|g|}$, and replace $\sqrt{|g|}\,|J|$ using part 1 — but be careful: $\sqrt{|g|}$ as a function of the new coordinates is the *old* metric factor, and $\sqrt{|g'|}$ is the *new* one. Show $\int\sqrt{|g|}\,\mathrm{d}^4x = \int\sqrt{|g'|}\,\mathrm{d}^4x'$.

> [!note]- Hint 3
> For part 3, the component transforms by $A'_{0123} = J\,A_{0123}$ (total antisymmetry of $A$ turns the sixteen-fold sum into the determinant). Then $\int A'_{0123}\,\mathrm{d}^4x' = \int J\,A_{0123}\,\mathrm{d}^4x'$, and the change-of-variables $\mathrm{d}^4x = |J|\,\mathrm{d}^4x'$ converts this back to $\int A_{0123}\,\mathrm{d}^4x$ (with $J > 0$ for orientation-preserving changes, $|J| = J$). No metric was used.

---

# Solution

The proof has two halves with the same shape but different inner workings. For the four-volume, the $\sqrt{|g|}$ factor and the measure each pick up a Jacobian and they cancel. For the form integral, the *component* and the measure each pick up a Jacobian and they cancel — with no metric anywhere. The crux is bookkeeping the direction of the Jacobian.

**Step 1: $\det g' = J^2\det g$, hence $\sqrt{|g'|} = |J|\sqrt{|g|}$.**

> [!note]- Derivation
> The metric components transform as a type-$(0,2)$ tensor, $g'_{\alpha\beta} = g_{\mu\nu}\,P^\mu{}_\alpha P^\nu{}_\beta$ with $P^\mu{}_\alpha = \partial x^\mu/\partial x'^\alpha$. In matrix notation $g' = P^{\mathsf T} g P$, so by multiplicativity of the determinant,
> $$\det g' = \det(P^{\mathsf T})\,\det g\,\det P = (\det P)^2\det g = J^2\det g,$$
> where $J = \det P = \det(\partial x^\mu/\partial x'^\alpha)$. Since a four-dimensional Lorentzian metric has $\det g < 0$ in either signature, $\det g' < 0$ too, and taking absolute values and square roots,
> $$\sqrt{|g'|} = |J|\,\sqrt{|g|}.$$

**Step 2: The four-volume is coordinate-independent.**

> [!note]- Derivation
> Write $\mathrm{vol}\,\mathscr{V}$ in the unprimed coordinates and substitute $x = x(x')$. The change-of-variables formula for the Lebesgue integral gives $\mathrm{d}^4x = |J|\,\mathrm{d}^4x'$, so
> $$\mathrm{vol}\,\mathscr{V} = \int_{\mathscr{V}}\sqrt{|g|}\,\mathrm{d}^4x = \int_{\mathscr{V}}\sqrt{|g|}\,|J|\,\mathrm{d}^4x' .$$
> Here $\sqrt{|g|}$ is the unprimed metric factor expressed as a function of the new coordinates. By Step 1, $\sqrt{|g'|} = |J|\sqrt{|g|}$, so $\sqrt{|g|}\,|J| = \sqrt{|g'|}$, and
> $$\mathrm{vol}\,\mathscr{V} = \int_{\mathscr{V}}\sqrt{|g'|}\,\mathrm{d}^4x' .$$
> This is exactly the definition of the four-volume in the *primed* coordinates. So the two expressions agree: the four-volume does not depend on the coordinate system. The factor $\sqrt{|g|}$ pulled its weight precisely by supplying the $|J|$ that the metric needs to cancel the $|J|^{-1}$ hidden in expressing the old measure in new coordinates.

**Step 3: The integral of a 4-form is coordinate-independent, with no metric.**

> [!note]- Derivation
> The single independent component of the 4-form transforms as
> $$A'_{0123} = A_{\mu\nu\rho\sigma}\,P^\mu{}_0 P^\nu{}_1 P^\rho{}_2 P^\sigma{}_3 .$$
> Because $A$ is totally antisymmetric, the sum over $\mu,\nu,\rho,\sigma$ collapses to the determinant of $P$ times $A_{0123}$ — this is the standard fact that contracting an antisymmetric tensor against a matrix in all four slots produces the determinant:
> $$A'_{0123} = A_{0123}\,\det P = J\,A_{0123}.$$
> Now compute the integral in the primed coordinates and change variables back. For an orientation-preserving change $J > 0$, so $|J| = J$:
> $$\int_{\mathscr{V}} A'_{0123}\,\mathrm{d}^4x' = \int_{\mathscr{V}} J\,A_{0123}\,\mathrm{d}^4x' = \int_{\mathscr{V}} A_{0123}\,(J\,\mathrm{d}^4x') = \int_{\mathscr{V}} A_{0123}\,\mathrm{d}^4x ,$$
> using $\mathrm{d}^4x = |J|\,\mathrm{d}^4x' = J\,\mathrm{d}^4x'$. So $\int A'_{0123}\,\mathrm{d}^4x' = \int A_{0123}\,\mathrm{d}^4x$: the integral is the same in both systems. **No metric appeared anywhere** — the cancellation is between the form's component (which picks up $J$) and the measure (which picks up $J^{-1}$ on going from primed to unprimed), entirely a consequence of antisymmetry.

**Step 4: The contrast.**

> [!note]- Derivation
> In Step 2 the four-volume's coordinate-independence *required* the metric: the factor $\sqrt{|g|}$ is what carries the compensating Jacobian, and without it the integral would be coordinate-dependent. In Step 3 the form-integral's coordinate-independence *did not use the metric at all*: the antisymmetric component $A_{0123}$ carries the compensating Jacobian on its own. So a four-volume is an intrinsically metric quantity (a "how big" question, answered only by $g$), while the integral of a form is an intrinsically metric-free quantity (a pairing between a form and a region that never measures a size). This is the chapter's central dichotomy, here proved at the level of transformation laws.

> [!note]- Complete formal solution
> Under $(x)\to(x')$ with $P^\mu{}_\alpha = \partial x^\mu/\partial x'^\alpha$ and $J = \det P$: the metric transforms as $g' = P^{\mathsf T} g P$, so $\det g' = J^2\det g$ and $\sqrt{|g'|} = |J|\sqrt{|g|}$. Then $\mathrm{vol}\,\mathscr{V} = \int\sqrt{|g|}\,\mathrm{d}^4x = \int\sqrt{|g|}\,|J|\,\mathrm{d}^4x' = \int\sqrt{|g'|}\,\mathrm{d}^4x'$, the four-volume in the new coordinates — coordinate-independent, with the metric supplying the cancelling Jacobian. Separately, the 4-form component transforms as $A'_{0123} = A_{0123}\det P = J A_{0123}$ by total antisymmetry, so $\int A'_{0123}\,\mathrm{d}^4x' = \int J A_{0123}\,\mathrm{d}^4x' = \int A_{0123}\,\mathrm{d}^4x$ (orientation-preserving, $|J|=J$) — coordinate-independent with no metric used. The four-volume is metric, the form integral is not. $\blacksquare$

---

# Key Takeaways

**Coordinate-independence is a cancellation between how the integrand transforms and how the measure transforms.** Every "this integral does not depend on coordinates" proof in differential geometry has the same anatomy: the integrand picks up a Jacobian factor under a change of coordinates, the measure $\mathrm{d}^n x$ picks up the reciprocal factor, and they cancel. The skill is identifying *what* in the integrand supplies the cancelling Jacobian. For a volume integral it is the metric factor $\sqrt{|g|}$, which transforms by $|J|$; for a form integral it is the antisymmetric component, which transforms by $J$. Recognising this anatomy lets you predict, before any calculation, that $\sqrt{|g|}\,\mathrm{d}^n x$ and the single component of a top-form are the coordinate-independent combinations — and that bare $\mathrm{d}^n x$ or a generic tensor component are not. The trigger is any well-posedness question of the form "show this geometric integral does not depend on the chart".

**The metric factor $\sqrt{|g|}$ *is* the Jacobian compensator — that is its entire job.** It is tempting to regard $\sqrt{|g|}$ as a mysterious geometric weight, but its meaning is completely pinned down by this exercise: it is the unique density-type object whose transformation law $\sqrt{|g'|} = |J|\sqrt{|g|}$ exactly cancels the change of the Lebesgue measure, making $\sqrt{|g|}\,\mathrm{d}^n x$ invariant. This demystifies it and tells you how to compute it in any coordinates (take $\det g_{\mu\nu}$, absolute value, square root) and why it appears (to make scalar integrals geometric). The same structure recurs throughout physics — it is why the Haar measure on a Lie group carries a $\sqrt{|\det h|}$, why the path-integral measure needs a metric on field space — and recognising "$\sqrt{|g|}$ = the thing that makes the measure invariant" is the portable insight.

**Antisymmetry is exactly the property that makes a tensor integrable without a metric.** The reason differential *forms*, and not arbitrary tensors, are the natural objects of integration is laid bare in Step 3: the total antisymmetry of $A$ is what turns the sixteen-term transformation of $A_{0123}$ into a single determinant factor $J$, which the measure then cancels. A generic type-$(0,4)$ tensor's component picks up all sixteen terms, only the alternating combination of which matches the Jacobian, so its integral is coordinate-dependent and meaningless. This is the structural answer to "why forms?": antisymmetry is precisely the algebraic condition under which a component transforms by the determinant of the coordinate change, which is precisely what the change-of-variables formula needs. Whenever you see a top-degree object being integrated coordinate-independently, antisymmetry is doing the work — and a companion exercise, [[Ex - Only an antisymmetric form integrates coordinate-independently]], drives this home by showing exactly how the non-antisymmetric case fails.
