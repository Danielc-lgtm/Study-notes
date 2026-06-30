---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Integration of Forms and the Volume Element"
  - "Def - Alternate Forms and the Exterior Product"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. For a differential 4-form $A$, show that the single component $A_{0123}$ transforms under a change of coordinates $(x^\alpha)\mapsto(x'^\alpha)$ by $A'_{0123} = A_{0123}\,\det(\partial x/\partial x')$, and conclude that $\int A_{0123}\,\mathrm{d}^4x$ is coordinate-independent.
2. Now let $T$ be a *generic* (not necessarily antisymmetric) type-$(0,4)$ tensor field. Write the transformation law for the component $T'_{0123}$ and show that, in general, it is **not** simply $T_{0123}\det(\partial x/\partial x')$ — so $\int T_{0123}\,\mathrm{d}^4x$ is **not** coordinate-independent.
3. Exhibit a concrete two-dimensional toy version: a symmetric type-$(0,2)$ tensor $T$ on $\mathbb{R}^2$ and a linear change of coordinates for which $\int T_{12}\,\mathrm{d}^2x$ changes value, demonstrating the failure explicitly.
4. Explain in one or two sentences why this is *the* reason differential forms, rather than arbitrary tensors, are the objects one integrates over submanifolds.

**Recall:**

The integral of a 4-form is defined via its single component.

![[Def - Integration of Forms and the Volume Element#The Definition]]

A type-$(0,4)$ tensor $T$ transforms as $T'_{\alpha\beta\gamma\delta} = T_{\mu\nu\rho\sigma}\,P^\mu{}_\alpha P^\nu{}_\beta P^\rho{}_\gamma P^\sigma{}_\delta$, with $P^\mu{}_\alpha = \partial x^\mu/\partial x'^\alpha$. A [[Def - Alternate Forms and the Exterior Product|differential form]] is a totally antisymmetric such tensor: $A_{\mu\nu\rho\sigma}$ changes sign under any transposition of indices.

---

# Convergent Strategy

**Problem class.** A *structural / why-this-definition* problem. It probes the axiom motivation of [[Def - Integration of Forms and the Volume Element]] — why the integration theory is built on forms — by showing what goes wrong for non-forms.

**Assumption pattern.** A change of coordinates and a tensor's transformation law. The key structural fact in play is that contracting a *totally antisymmetric* tensor against a matrix in all its slots yields the *determinant* of the matrix, whereas a generic tensor produces a full multi-index sum. The signpost is the phrase "single component": only for an antisymmetric tensor does that one component carry all the information and transform by the determinant.

**Theorem routing.** Part 1 is the determinant-from-antisymmetry fact, $A'_{0123} = A_{0123}\det P$, plus the change-of-variables, exactly as in the companion exercise [[Ex - Coordinate-independence of the four-volume]]. Part 2 writes the generic transformation, which has $4^4 = 256$ terms collapsing (for a form) to one but (for a generic tensor) staying a genuine sum. Part 3 makes the failure concrete with a $2\times 2$ symmetric example.

**Key decision point.** The crux is recognising that "the integral uses only one component" is *only* legitimate when that component determines the rest by antisymmetry. For a generic tensor the other components are independent and *do* contribute to how $T'_{0123}$ transforms, breaking the determinant structure. Choosing a *symmetric* example in part 3 is the cleanest demonstration, because symmetry is the maximal departure from antisymmetry.

---

# Legal Operations Used

1. **Operation 2 from the topic page (integrate a 4-form by reading off its single component).** The exercise is precisely a study of *when this operation is legal*: part 1 confirms it for forms, part 2 shows it fails for generic tensors.

2. **Illegal-but-tempting operation 2 from the topic page (integrating a generic tensor component and expecting coordinate-independence).** This exercise *is* that warning, worked out: it exhibits the concrete failure the warning describes.

---

# Hints

> [!note]- Hint 1
> For part 1, contract the antisymmetric $A_{\mu\nu\rho\sigma}$ against $P^\mu{}_0 P^\nu{}_1 P^\rho{}_2 P^\sigma{}_3$. Total antisymmetry means the sum equals $A_{0123}$ times the signed sum over permutations of the products of $P$'s — which is the Leibniz formula for $\det P$.

> [!note]- Hint 2
> For part 2, the generic $T'_{0123} = T_{\mu\nu\rho\sigma}P^\mu{}_0 P^\nu{}_1 P^\rho{}_2 P^\sigma{}_3$ does not collapse: every assignment of $(\mu,\nu,\rho,\sigma)$ contributes, not just permutations of $(0,1,2,3)$, and the symmetric part of $T$ produces terms with repeated indices that the determinant does not contain. So $T'_{0123}$ depends on components of $T$ other than $T_{0123}$.

> [!note]- Hint 3
> For part 3, take $T = \mathrm{d}x\otimes\mathrm{d}x$ on $\mathbb{R}^2$ (so $T_{11}=1$, all others $0$, symmetric) and the rotation/shear $x = x'+y'$, $y = y'$. Compute $T'_{12}$ and compare $\int T_{12}\,\mathrm{d}x\,\mathrm{d}y$ (which is $0$) with $\int T'_{12}\,\mathrm{d}x'\,\mathrm{d}y'$ (which is not).

---

# Solution

The point is a single algebraic fact: contracting a totally antisymmetric tensor against a matrix in every slot gives the determinant of that matrix, and the determinant is exactly the Jacobian the change-of-variables formula needs. A generic tensor's contraction is not a determinant, so the cancellation fails. Part 3 makes the failure visible in two dimensions.

**Step 1: For a 4-form, $A'_{0123} = A_{0123}\det P$, so the integral is coordinate-independent.**

> [!note]- Derivation
> The component transforms as $A'_{0123} = A_{\mu\nu\rho\sigma}\,P^\mu{}_0 P^\nu{}_1 P^\rho{}_2 P^\sigma{}_3$. Because $A$ is totally antisymmetric, $A_{\mu\nu\rho\sigma}$ is nonzero only when $(\mu,\nu,\rho,\sigma)$ is a permutation of $(0,1,2,3)$, and then $A_{\mu\nu\rho\sigma} = \mathrm{sgn}(\pi)\,A_{0123}$ for the permutation $\pi$. Thus
> $$A'_{0123} = A_{0123}\sum_{\pi\in S_4}\mathrm{sgn}(\pi)\,P^{\pi(0)}{}_0 P^{\pi(1)}{}_1 P^{\pi(2)}{}_2 P^{\pi(3)}{}_3 = A_{0123}\,\det P,$$
> the sum being the Leibniz expansion of $\det P$. Writing $J = \det P = \det(\partial x/\partial x')$ and using the change of variables $\mathrm{d}^4x = |J|\,\mathrm{d}^4x'$ (with $J>0$ for orientation-preserving changes, $|J|=J$),
> $$\int A'_{0123}\,\mathrm{d}^4x' = \int J\,A_{0123}\,\mathrm{d}^4x' = \int A_{0123}\,\mathrm{d}^4x,$$
> so the integral is the same in both coordinate systems. The form's component supplies precisely the determinant that the measure's transformation cancels.

**Step 2: For a generic tensor, the transformation is not by the determinant.**

> [!note]- Derivation
> For a generic type-$(0,4)$ tensor $T$, the same contraction
> $$T'_{0123} = T_{\mu\nu\rho\sigma}\,P^\mu{}_0 P^\nu{}_1 P^\rho{}_2 P^\sigma{}_3$$
> runs over *all* $4^4 = 256$ index assignments, not just the $24$ permutations of $(0,1,2,3)$. Decompose $T = T^{\mathrm{alt}} + T^{\mathrm{rest}}$ into its totally antisymmetric part and the rest. The antisymmetric part contributes $T^{\mathrm{alt}}_{0123}\det P$ as in Step 1. But $T^{\mathrm{rest}}$ contributes terms in which some indices among $(\mu,\nu,\rho,\sigma)$ coincide — for instance $T_{0012}P^0{}_0 P^0{}_1 P^1{}_2 P^2{}_3$ — and such terms appear in *no* determinant (the determinant has no repeated-index products). So
> $$T'_{0123} = T^{\mathrm{alt}}_{0123}\det P + (\text{terms from }T^{\mathrm{rest}}\text{ not proportional to }\det P),$$
> and the extra terms depend on components of $T$ other than $T_{0123}$. Consequently $\int T'_{0123}\,\mathrm{d}^4x'$ does not in general reduce to $\int T_{0123}\,\mathrm{d}^4x$: the prescription "integrate the single component" is coordinate-dependent for a generic tensor. Only the antisymmetric part transforms cleanly.

**Step 3: An explicit two-dimensional failure.**

> [!note]- Derivation
> Work on $\mathbb{R}^2$ with the symmetric tensor $T = \mathrm{d}x\otimes\mathrm{d}x$, so $T_{11} = 1$ and $T_{12} = T_{21} = T_{22} = 0$. Then the prescription gives $\int_{[0,1]^2} T_{12}\,\mathrm{d}x\,\mathrm{d}y = \int 0 = 0$.
>
> Now change coordinates by the shear $x = x' + y'$, $y = y'$, so $\partial x/\partial x' = 1$, $\partial x/\partial y' = 1$, $\partial y/\partial x' = 0$, $\partial y/\partial y' = 1$ (Jacobian $J = 1$). The component $T'_{1'2'}$ (writing $1'\leftrightarrow x'$, $2'\leftrightarrow y'$) is
> $$T'_{1'2'} = T_{\mu\nu}\frac{\partial x^\mu}{\partial x'}\frac{\partial x^\nu}{\partial y'} = T_{11}\frac{\partial x}{\partial x'}\frac{\partial x}{\partial y'} = 1\cdot 1\cdot 1 = 1,$$
> the only surviving term being $\mu=\nu=x$ since $T_{11}$ is the lone nonzero component. So in the new coordinates the prescription gives $\int_{[0,1]^2} T'_{1'2'}\,\mathrm{d}x'\,\mathrm{d}y' = \int 1 = 1$.
>
> The "integral of the off-diagonal component" went from $0$ to $1$ under a coordinate change of unit Jacobian. The prescription is coordinate-dependent for this symmetric tensor — exactly the failure Step 2 predicted, made concrete. (For an antisymmetric $T$, $T_{12}$ would carry the whole tensor and transform by $\det P = 1$, giving the same value in both frames.)

**Step 4: Why forms are the integrable objects.**

> [!note]- Derivation
> Integration over a $p$-submanifold uses only the single "tangential" component of the integrand, and for that prescription to be coordinate-independent the component must transform by the determinant of the coordinate change — because that is precisely the Jacobian the change-of-variables formula produces. *Total antisymmetry is exactly the algebraic condition under which a tensor's component transforms by the determinant* (Step 1), and it fails for any tensor with a non-antisymmetric part (Steps 2–3). So differential forms are not a stylistic preference: they are the unique tensors whose integrals over submanifolds are geometric (coordinate-independent), which is why the entire integration theory of the chapter is built on them and not on arbitrary tensors. To integrate a generic tensor invariantly one must instead pair it with the metric volume element $\sqrt{|g|}\,\mathrm{d}^4x$, reintroducing the metric.

> [!note]- Complete formal solution
> For a 4-form, total antisymmetry gives $A'_{0123} = A_{\mu\nu\rho\sigma}P^\mu{}_0\cdots P^\sigma{}_3 = A_{0123}\sum_\pi\mathrm{sgn}(\pi)\prod_i P^{\pi(i)}{}_i = A_{0123}\det P$, so with $\mathrm{d}^4x = J\,\mathrm{d}^4x'$ ($J=\det P>0$), $\int A'_{0123}\mathrm{d}^4x' = \int A_{0123}\mathrm{d}^4x$ — coordinate-independent. For a generic type-$(0,4)$ tensor the contraction runs over all $256$ index assignments; its symmetric part produces repeated-index terms absent from any determinant, so $T'_{0123} \ne T_{0123}\det P$ in general and the single-component integral is coordinate-dependent. Concretely on $\mathbb{R}^2$ with $T = \mathrm{d}x\otimes\mathrm{d}x$ and the shear $x=x'+y',\,y=y'$ ($J=1$): $T_{12}=0$ but $T'_{1'2'}=T_{11}\partial_{x'}x\,\partial_{y'}x = 1$, so $\int T_{12} = 0 \ne 1 = \int T'_{1'2'}$. Hence only totally antisymmetric tensors — differential forms — integrate coordinate-independently over submanifolds, which is why the integration theory is built on forms. $\blacksquare$

---

# Key Takeaways

**Contracting a totally antisymmetric tensor against a matrix in every slot yields the determinant — this is the algebraic heart of why forms integrate.** The Leibniz formula $\det P = \sum_\pi\mathrm{sgn}(\pi)\prod_i P^{\pi(i)}{}_i$ is exactly what the contraction $A_{\mu\nu\rho\sigma}P^\mu{}_0\cdots P^\sigma{}_3$ produces when $A$ is antisymmetric, because antisymmetry restricts the surviving terms to permutations and supplies the signs. The trigger to recall this is any computation where an antisymmetric object meets a change of basis: the answer will involve the determinant, and in an integration context that determinant is the Jacobian that makes things coordinate-independent. The same fact underlies the appearance of determinants throughout multilinear algebra — the wedge product, orientation, the Pfaffian — and recognising "antisymmetric contraction = determinant" is a portable shortcut.

**The integration theory is built on forms for a forced reason, not a conventional one.** It is easy to absorb "we integrate differential forms" as an arbitrary choice of language, but this exercise shows it is forced: integration over a submanifold necessarily uses one component of the integrand, and *only* a totally antisymmetric tensor has a component that transforms by the determinant, which is *exactly* what coordinate-independence demands. Any non-antisymmetric tensor's single-component integral changes value under a coordinate change of unit Jacobian (Step 3), so it is not a geometric quantity. The transferable principle is that whenever a construction in geometry insists on antisymmetric/alternating objects — forms, the wedge product, the determinant line bundle, orientations — it is because antisymmetry is the precise condition for the determinant (hence the Jacobian, hence coordinate-independence) to appear. The choice of forms is dictated by the change-of-variables formula.

**To integrate a non-form invariantly, you must spend the metric.** The flip side of "forms integrate without a metric" is that *non-forms* — scalars, generic tensors, densities — can only be integrated invariantly by pairing them with the metric volume element $\sqrt{|g|}\,\mathrm{d}^n x$, which carries the compensating Jacobian. This is why a scalar density's integral $\int f\sqrt{|g|}\,\mathrm{d}^4x$ needs the metric while a 4-form's integral $\int A_{0123}\,\mathrm{d}^4x$ does not, and it is the precise origin of the chapter's recurring dichotomy. The diagnostic for any integral is: if the integrand is an alternating form of the right degree, no metric; otherwise, a metric volume element is mandatory. This exercise is the proof that the dichotomy is real and not a notational accident — the companion exercise [[Ex - Coordinate-independence of the four-volume]] shows the volume side of the same coin.
