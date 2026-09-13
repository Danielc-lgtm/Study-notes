---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Continuity Equation and Conservation of Charge"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Charge-Current 3-Form"
  - "Def - Manifold with Boundary and Induced Orientation"
tags: [geometry, gauge-theory]
---

# Problem Statement

Work on Minkowski space $M = \mathbb{R}^4$ with coordinates $(t, x, y, z)$, Lorentzian metric of signature $(-,+,+,+)$, $c = 1$, and volume form $\mathrm{vol} = dt \wedge dx \wedge dy \wedge dz$. Let the electromagnetic field of a critical connection have charge-current $3$-form
$$J = \varrho\, dx \wedge dy \wedge dz - j_x\, dt \wedge dy \wedge dz - j_y\, dt \wedge dz \wedge dx - j_z\, dt \wedge dx \wedge dy \;\in\; \Omega^3(M; \mathbb{R}),$$
where $\varrho \in C^\infty(M)$ is the charge density and $\vec{j} = (j_x, j_y, j_z)$ is the (time-dependent) current density. The Maxwell equation $d\star F + J = 0$ gives, on applying $d$ and using $d^2 = 0$, the closedness
$$dJ = 0.$$

Fix a **compact three-dimensional submanifold with boundary** $B \subset \mathbb{R}^3$ (a spatial region — think of a ball or a solid torus) with smooth boundary surface $\partial B$, and two times $t_0 < t_1$. The **spacetime cylinder** is the compact set
$$N := [t_0, t_1] \times B \;\subset\; \mathbb{R}_t \times \mathbb{R}^3 = M.$$

**Prove**, purely from $dJ = 0$ and Stokes' theorem applied on $N$, the integral conservation of charge
$$\int_B \varrho(t_1, \cdot)\, dx\, dy\, dz \;-\; \int_B \varrho(t_0, \cdot)\, dx\, dy\, dz \;+\; \int_{t_0}^{t_1}\!\!\int_{\partial B} \langle \vec{j}, \nu \rangle\, \mathrm{dvol}_{\partial B}\, dt \;=\; 0,$$
where $\nu$ is the outward unit normal of $\partial B$ in $\mathbb{R}^3$. The three terms are, in order, the electric charge inside $B$ at the final time, the charge inside $B$ at the initial time, and the total current flux out through $\partial B$ over the interval. The content of the identity is that the change in charge stored in $B$ is exactly minus the charge that flowed out through its walls.

The single technical demand is to **compute the orientation induced on each of the three boundary faces of $N$ explicitly**, so that every sign in the identity is derived rather than guessed. The face that traps the unwary is the initial-time face $\{t_0\} \times B$: its induced orientation is the *reverse* of the standard orientation of $B$, and that reversal is exactly the minus sign in front of the $t_0$-integral.

> [!warning] Convention:
> We use Bär's sign convention $d\star F + J = 0$ for the inhomogeneous Maxwell equation throughout the series. (Bär's text prints "$d\star F = J$" once on p. 95, which is inconsistent with the Euler–Lagrange derivation on p. 86; we use the p. 86 form $d\star F + J = 0$, from which $dJ = 0$ follows regardless of the sign of $J$.) The boundary-orientation convention is the **outward-normal-first** rule of [[Def - Manifold with Boundary and Induced Orientation|the induced-orientation page]], stated in the Recall below; the whole computation is a bookkeeping of that one rule across three faces.

**Recall:**

The objects in play are the charge-current $3$-form, the fact that it is closed, Stokes' theorem on an oriented manifold with boundary, and the outward-normal-first rule for the induced boundary orientation.

![[Def - Charge-Current 3-Form#The Definition]]

![[Thm - Continuity Equation and Conservation of Charge#Statement]]

The theorem [[Thm - Continuity Equation and Conservation of Charge|Continuity Equation and Conservation of Charge]] records both the differential law and — as its second part — the very identity we are asked to prove; this exercise is the drill that reconstructs that second part from scratch, so we lean only on its **first part**, the closedness $dJ = 0$, and never quote its conclusion.

![[Thm - Stokes' Theorem on Manifolds#Statement]]

In the form we use it, [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] says: if $N$ is a compact oriented $n$-dimensional manifold with boundary, $\partial N$ carries the induced boundary orientation, $\iota : \partial N \hookrightarrow N$ is the inclusion, and $\alpha \in \Omega^{n-1}(N)$, then
$$\int_N d\alpha = \int_{\partial N} \iota^* \alpha.$$
Here $n = 4$ and $\alpha = J$ is a $3$-form.

![[Def - Manifold with Boundary and Induced Orientation#The Definition]]

The **outward-normal-first rule**: at a boundary point $p \in \partial N$, choose the outward-pointing normal vector $\nu_{\mathrm{out}} \in T_p N$ (the one pointing out of $N$). A basis $(e_1, \dots, e_{n-1})$ of $T_p(\partial N)$ is declared **positively oriented** for the induced orientation of $\partial N$ if and only if the basis $(\nu_{\mathrm{out}}, e_1, \dots, e_{n-1})$ of $T_p N$ is positively oriented for the orientation of $N$. Every sign below is an instance of this rule.

---

# Convergent Strategy

**Problem class.** This is a *conservation-law-from-a-closed-form* problem: a quantity written as an integral of a closed differential form over the boundary of a region is shown to balance, by turning the boundary integral into an integral of $d(\text{form}) = 0$ over the interior. It is the geometric skeleton shared by the divergence theorem, the fundamental theorem of calculus, Cauchy's theorem in complex analysis, and every physical conservation law expressed through a flux. The distinguishing feature of *this* instance is that the region $N$ is a product $[t_0, t_1] \times B$, so its boundary splits into a top, a bottom, and a side, and the arithmetic of the three induced orientations is the whole of the work.

**Assumption pattern.** The hypothesis is used in exactly one place: $dJ = 0$ makes the interior integral $\int_N dJ$ vanish, so Stokes turns the total boundary integral into zero. The recognisable trigger is a target identity that is a *sum of boundary integrals set equal to zero* — whenever a physical statement has the shape "stored + outflow = 0" or "final $-$ initial $+$ flux $= 0$", the move is to recognise the three terms as the three faces of a spacetime region and the vanishing as the closedness of a current form.

**Theorem routing.** The route is short and forced: (1) assemble the region $N = [t_0, t_1] \times B$ and observe it is a compact oriented $4$-manifold with corners; (2) apply [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] to $J$ on $N$, so that $0 = \int_N dJ = \int_{\partial N} J$; (3) split $\partial N$ into the top face $\{t_1\} \times B$, the bottom face $\{t_0\} \times B$, and the lateral face $[t_0, t_1] \times \partial B$; (4) on each face pull back $J$, kill the terms whose differentials collapse, and read off the induced orientation with the [[Def - Manifold with Boundary and Induced Orientation|outward-normal-first rule]]; (5) collect the three surviving integrals into the claimed identity.

**Key decision point.** The one genuinely non-mechanical decision is *how to keep the orientation signs honest*. There are two temptations, both wrong. The first is to write $\int_{\partial N} J = \int_{\{t_1\}\times B} + \int_{\{t_0\}\times B} + \int_{[t_0,t_1]\times \partial B}$ with all three "natural" (product) orientations and forget that the induced orientation of the bottom face and of the lateral face differ from the product orientation by a sign. The second is to compute the pullbacks first and hope the signs sort themselves out. The disciplined route is to fix one orientation of the ambient $\mathbb{R}^4$ (namely $dt \wedge dx \wedge dy \wedge dz$), then *derive* the induced orientation of each face from the outward-normal-first rule as a specific $\pm$ multiple of a product orientation, and only then integrate. The reversal on the $\{t_0\}$-face is not an accident to be memorised; it falls out of the rule because the outward normal there is $-\partial_t$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory#Legal Operations|the topic page's Legal Operations]] (named descriptively where the topic page is not yet assembled):

1. **Close a current form by nilpotence of $d$.** From the field equation $d\star F + J = 0$, apply $d$ and use $d \circ d = 0$ ([[Thm - d-Squared-is-Zero|nilpotence of d]]) to obtain $dJ = 0$. Here this is supplied as a hypothesis; the exercise uses only the closedness, not how it arose.

2. **Convert a closed-form boundary integral to zero via Stokes.** Integrate $dJ$ over a compact region $N$; because $dJ = 0$ the interior integral vanishes, and [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] equates it to $\int_{\partial N} J$, forcing the total boundary integral to be zero.

3. **Decompose the boundary of a product region into faces.** Write $\partial([t_0, t_1] \times B)$ as the disjoint union (up to a measure-zero corner set) of the top, bottom, and lateral faces, and integrate face by face.

4. **Read off an induced orientation by the outward-normal-first rule.** On each face, identify the outward normal and apply the rule from [[Def - Manifold with Boundary and Induced Orientation|the induced-orientation page]] to express the induced orientation as an explicit $\pm$ multiple of a product orientation.

5. **Annihilate a pulled-back form by a collapsing differential.** On a face where a coordinate is held constant (top and bottom: $t$ fixed) or confined to a lower-dimensional set (lateral: the spatial point lies on the surface $\partial B$), the corresponding wedge of differentials pulls back to zero, so only some terms of $J$ survive on that face.

6. **Recognise a spatial flux $2$-form.** On the lateral face, identify the surviving part of $J$ as $-\,dt \wedge \iota_{\vec j}(dx \wedge dy \wedge dz)$ and use that the interior product $\iota_{\vec j}(dx\wedge dy \wedge dz)$ restricts on an oriented surface with outward normal $\nu$ to the flux density $\langle \vec j, \nu\rangle\,\mathrm{dvol}_{\partial B}$.

7. **Reassemble faces by Fubini.** Integrate the product-orientation lateral integral by iterated integration, $\int_{[t_0,t_1]\times\partial B} = \int_{t_0}^{t_1}\!\int_{\partial B}$, to land on the stated flux term.

---

# Hints

> [!note]- Hint 1
> You are asked to prove that a sum of three boundary integrals is zero, and you are handed exactly one fact, $dJ = 0$. What single theorem turns "$\int$ over a boundary" into "$\int$ of $d(\cdot)$ over the inside"? Apply it to $J$ on the region $N = [t_0,t_1]\times B$ and see that the right-hand side is $\int_N dJ = 0$.

> [!note]- Hint 2
> The boundary $\partial N$ has three pieces: the top $\{t_1\}\times B$, the bottom $\{t_0\}\times B$, and the side $[t_0,t_1]\times\partial B$. On the top and the bottom, $t$ is *constant*, so $dt$ pulls back to $0$; which terms of $J$ survive? On the side, the spatial point is pinned to the surface $\partial B$, so $dx\wedge dy\wedge dz$ pulls back to $0$; which terms survive there?

> [!note]- Hint 3
> Orient all of $\mathbb{R}^4$ by $dt\wedge dx\wedge dy\wedge dz$, i.e. by the ordered frame $(\partial_t,\partial_x,\partial_y,\partial_z)$. On the top face the outward normal is $+\partial_t$; on the bottom face it is $-\partial_t$. Feed each into the outward-normal-first rule $(\nu_{\mathrm{out}}, e_1,e_2,e_3)$ positive $\iff$ $(e_1,e_2,e_3)$ positive on the face. The bottom face inherits $(\partial_x,\partial_y,\partial_z)$ with a *minus* sign — that is the entire subtlety.

> [!note]- Hint 4
> For the lateral face, the outward normal is the spatial outward normal $\nu$ of $\partial B$ (no $\partial_t$ component). Test the frame $(\partial_t, f_1, f_2)$, where $(f_1,f_2)$ is a positively oriented frame of $\partial B$ for *its* induced orientation as $\partial B \subset \mathbb{R}^3$. Compare $(\nu,\partial_t,f_1,f_2)$ with $(\partial_t,\nu,f_1,f_2)$ by one swap; conclude that $(\partial_t,f_1,f_2)$ is a *negative* frame of the lateral face, so the induced orientation is $-\big(dt\wedge\mathrm{dvol}_{\partial B}\big)$. The surviving current terms are $-dt\wedge\big(j_x\,dy\wedge dz + j_y\,dz\wedge dx + j_z\,dx\wedge dy\big)$; the two minus signs cancel and give $+\langle\vec j,\nu\rangle$.

---

# Solution

The proof is one application of Stokes' theorem followed by careful sign accounting. We integrate the closed $3$-form $J$ over the boundary of the spacetime cylinder $N = [t_0,t_1]\times B$; Stokes turns this into $\int_N dJ = 0$; the boundary is a top, a bottom, and a side; on each we pull $J$ back, discard the terms whose differentials collapse, and derive the induced orientation from the outward-normal-first rule. The top gives $+\int_B\varrho(t_1)$, the bottom gives $-\int_B\varrho(t_0)$ (the reversal is forced by the outward normal $-\partial_t$), and the side gives the outward current flux; their sum is zero.

**Step 0: The region is a compact oriented $4$-manifold with corners, and Stokes applies to it.**

The set $N = [t_0,t_1]\times B$ is compact, oriented by the restriction of $dt\wedge dx\wedge dy\wedge dz$, and is a manifold with corners along $\{t_0,t_1\}\times\partial B$; Stokes' theorem holds for it, with the corner set contributing nothing.

> [!note]- Derivation
> $N = [t_0,t_1]\times B$ is a product of a compact interval and a compact manifold-with-boundary, hence compact. We orient it, and all of $\mathbb{R}^4 = \mathbb{R}_t\times\mathbb{R}^3$, by the volume form $\mathrm{vol} = dt\wedge dx\wedge dy\wedge dz$; equivalently, the ordered frame $(\partial_t,\partial_x,\partial_y,\partial_z)$ is declared positive. The topological boundary of $N$ is
> $$\partial N = \big(\{t_1\}\times B\big)\;\cup\;\big(\{t_0\}\times B\big)\;\cup\;\big([t_0,t_1]\times\partial B\big),$$
> the three faces meeting along the edge set $\{t_0,t_1\}\times\partial B$, which is a finite union of $2$-dimensional submanifolds and hence has $3$-dimensional measure zero inside $\partial N$.
>
> Strictly, $N$ is a manifold with corners, whereas [[Thm - Stokes' Theorem on Manifolds|the vault's Stokes theorem]] is stated for a manifold with smooth boundary. The theorem extends to manifolds with corners without change of value, and we use it in that form. Concretely: round each edge inside an $\varepsilon$-collar to obtain a smooth-boundary compact manifold $N_\varepsilon \subset N$ with $\int_{N_\varepsilon} dJ = \int_{\partial N_\varepsilon} \iota^* J$ (Stokes for smooth boundary). As $\varepsilon \to 0$, the smoothed boundary $\partial N_\varepsilon$ agrees with the three flat faces off an $\varepsilon$-neighbourhood of the edges; since $J$ is smooth and hence bounded on the compact set $N$, and the smoothing region has area $O(\varepsilon)$, dominated convergence gives $\int_{\partial N_\varepsilon}\iota^* J \to \sum_{\text{faces}} \int_{\text{face}} \iota^* J$ and $\int_{N_\varepsilon} dJ \to \int_N dJ$. Thus
> $$\int_N dJ = \int_{\{t_1\}\times B} J + \int_{\{t_0\}\times B} J + \int_{[t_0,t_1]\times\partial B} J,$$
> each face carrying its induced boundary orientation. (This is the only place where the manifold-with-corners refinement enters; nothing below depends on the details of the smoothing.)

**Step 1: Stokes kills the interior integral.**

Because $J$ is closed, the left-hand side of Stokes' identity vanishes.

> [!note]- Derivation
> By hypothesis $dJ = 0$ on all of $M$ (it is the differential consequence of the Maxwell equation $d\star F + J = 0$, obtained by applying $d$ and using [[Thm - d-Squared-is-Zero|nilpotence of d]]; we take it as given). Therefore
> $$\int_N dJ = \int_N 0 = 0 \qquad \text{(since } dJ = 0 \text{ pointwise).}$$
> Combined with Step 0,
> $$0 = \int_{\{t_1\}\times B} J + \int_{\{t_0\}\times B} J + \int_{[t_0,t_1]\times\partial B} J. \tag{$\ast$}$$
> It remains to evaluate the three face integrals, which is entirely a matter of pullbacks and induced orientations.

**Step 2: The top face $\{t_1\}\times B$ contributes $+\int_B \varrho(t_1)$.**

On the constant-time slice at $t_1$ the differential $dt$ pulls back to zero, only the $\varrho$-term of $J$ survives, and the induced orientation is the standard orientation of $B$.

> [!note]- Derivation
> Let $\Sigma_1 := \{t_1\}\times B$ with inclusion $\iota_1 : \Sigma_1 \hookrightarrow N$. On $\Sigma_1$ the coordinate $t$ is constant, so $\iota_1^* dt = 0$; consequently every term of $J$ containing a factor $dt$ pulls back to $0$:
> $$\iota_1^* J = \iota_1^*\big(\varrho\, dx\wedge dy\wedge dz\big) = \varrho(t_1,\cdot)\, dx\wedge dy\wedge dz \qquad \text{(the three } dt\text{-terms vanish since } \iota_1^* dt = 0\text{).}$$
> **Induced orientation.** The outward normal to $N$ along $\Sigma_1$ points in the direction of *increasing* $t$, i.e. $\nu_{\mathrm{out}} = +\partial_t$ (leaving the cylinder through its top). By the [[Def - Manifold with Boundary and Induced Orientation|outward-normal-first rule]], a frame $(e_1,e_2,e_3)$ is positive on $\Sigma_1$ iff $(\partial_t, e_1,e_2,e_3)$ is positive in $N$. Taking $(e_1,e_2,e_3) = (\partial_x,\partial_y,\partial_z)$ gives $(\partial_t,\partial_x,\partial_y,\partial_z)$, which is positive in $N$ by our choice of orientation; hence $(\partial_x,\partial_y,\partial_z)$ is a positive frame of $\Sigma_1$. Thus the induced orientation of $\Sigma_1$ is the **standard** orientation of $B$, represented by $dx\wedge dy\wedge dz$. Therefore
> $$\int_{\Sigma_1} J = \int_{\Sigma_1} \varrho(t_1,\cdot)\, dx\wedge dy\wedge dz = +\int_B \varrho(t_1,\cdot)\, dx\, dy\, dz \qquad \text{(standard orientation, no sign).}$$

**Step 3: The bottom face $\{t_0\}\times B$ contributes $-\int_B \varrho(t_0)$.**

The pullback is the same, but the outward normal is now $-\partial_t$, which flips the induced orientation of $B$ and hence the sign of the integral.

> [!note]- Derivation
> Let $\Sigma_0 := \{t_0\}\times B$ with inclusion $\iota_0$. Exactly as in Step 2, $\iota_0^* dt = 0$, so
> $$\iota_0^* J = \varrho(t_0,\cdot)\, dx\wedge dy\wedge dz \qquad \text{(the } dt\text{-terms vanish).}$$
> **Induced orientation.** Here the outward normal points toward *decreasing* $t$, i.e. $\nu_{\mathrm{out}} = -\partial_t$ (one leaves the cylinder through its bottom by moving to smaller $t$). By the outward-normal-first rule, $(e_1,e_2,e_3)$ is positive on $\Sigma_0$ iff $(-\partial_t, e_1,e_2,e_3)$ is positive in $N$. Test $(e_1,e_2,e_3) = (\partial_x,\partial_y,\partial_z)$:
> $$(-\partial_t,\partial_x,\partial_y,\partial_z) \ \text{has the orientation} \ -(\partial_t,\partial_x,\partial_y,\partial_z) \qquad \text{(replacing } \partial_t \text{ by } -\partial_t \text{ flips one basis vector, hence the sign),}$$
> so $(-\partial_t,\partial_x,\partial_y,\partial_z)$ is *negative* in $N$. Therefore $(\partial_x,\partial_y,\partial_z)$ is a **negative** frame of $\Sigma_0$: the induced orientation of $\Sigma_0$ is the standard orientation of $B$ **reversed**. Reversing the orientation of the domain of integration reverses the sign of the integral of any top form, so
> $$\int_{\Sigma_0} J = \int_{\Sigma_0} \varrho(t_0,\cdot)\, dx\wedge dy\wedge dz = -\int_B \varrho(t_0,\cdot)\, dx\, dy\, dz \qquad \text{(induced orientation} = -\text{standard).}$$
> This minus sign is the one the illegal route below drops; it is not optional, and it is exactly what makes ($\ast$) the statement "final charge $-$ initial charge $+$ outflow $= 0$" rather than "sum of charges $= 0$".

**Step 4: The lateral face $[t_0,t_1]\times\partial B$ contributes $+\int_{t_0}^{t_1}\!\int_{\partial B}\langle\vec j,\nu\rangle$.**

On the side, $dx\wedge dy\wedge dz$ pulls back to zero, only the current terms survive, the induced orientation is minus the product orientation, and the surviving form restricts to the current flux.

> [!note]- Derivation
> Let $\Sigma_L := [t_0,t_1]\times\partial B$ with inclusion $\iota_L$. On $\Sigma_L$ the spatial point lies on the $2$-dimensional surface $\partial B$, so the three spatial differentials $dx, dy, dz$ pull back to a rank-$2$ system: any wedge of all three vanishes, $\iota_L^*(dx\wedge dy\wedge dz) = 0$. Hence the $\varrho$-term of $J$ dies and only the current terms survive. Group them:
> $$\iota_L^* J = -\iota_L^*\big(j_x\, dt\wedge dy\wedge dz + j_y\, dt\wedge dz\wedge dx + j_z\, dt\wedge dx\wedge dy\big) = -\iota_L^*\big(dt\wedge \sigma\big),$$
> $$\text{where}\quad \sigma := j_x\, dy\wedge dz + j_y\, dz\wedge dx + j_z\, dx\wedge dy = \iota_{\vec j}\big(dx\wedge dy\wedge dz\big) \qquad \text{(the interior product of } \mathrm{vol}_{\mathbb{R}^3} \text{ with } \vec j\text{).}$$
> The identity $\sigma = \iota_{\vec j}(dx\wedge dy\wedge dz)$ is the definition of the interior product applied term by term: $\iota_{\vec j}(dx\wedge dy\wedge dz) = j_x\, dy\wedge dz - j_y\, dx\wedge dz + j_z\, dx\wedge dy = j_x\, dy\wedge dz + j_y\, dz\wedge dx + j_z\, dx\wedge dy$ (using $dz\wedge dx = -dx\wedge dz$).
>
> **The flux identity on the surface.** Restricting $\sigma$ to the surface $\partial B$ (with its induced orientation as the boundary of $B \subset \mathbb{R}^3$, and outward unit normal $\nu$) gives the classical flux $2$-form:
> $$\iota_{\partial B}^*\, \sigma = \langle \vec j, \nu\rangle\, \mathrm{dvol}_{\partial B} \qquad \text{(the restriction of } \iota_{\vec j}\mathrm{vol}_{\mathbb{R}^3} \text{ to an oriented hypersurface is its normal-flux density).}$$
> To see this pointwise: at $p \in \partial B$ choose a positively oriented orthonormal frame $(f_1,f_2)$ of $T_p\partial B$; then $(\nu, f_1, f_2)$ is a positively oriented orthonormal frame of $\mathbb{R}^3$ (outward-normal-first), so $\mathrm{dvol}_{\mathbb{R}^3}(\nu,f_1,f_2) = 1$ and $\mathrm{dvol}_{\partial B}(f_1,f_2) = 1$. Decompose $\vec j = \langle\vec j,\nu\rangle\,\nu + \vec j_\parallel$ with $\vec j_\parallel$ tangent to $\partial B$. Then
> $$\big(\iota_{\vec j}\mathrm{vol}_{\mathbb{R}^3}\big)(f_1,f_2) = \mathrm{vol}_{\mathbb{R}^3}(\vec j, f_1, f_2) = \langle\vec j,\nu\rangle\,\mathrm{vol}_{\mathbb{R}^3}(\nu,f_1,f_2) = \langle\vec j,\nu\rangle \qquad \text{(the tangential part } \vec j_\parallel \text{ is a combination of } f_1,f_2 \text{, so } \mathrm{vol}_{\mathbb{R}^3}(\vec j_\parallel,f_1,f_2) = 0\text{),}$$
> which equals $\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}(f_1,f_2)$. As both sides are $2$-forms on a $2$-manifold agreeing on one positive frame, they agree.
>
> **Induced orientation of $\Sigma_L$.** The outward normal to $N$ along $\Sigma_L$ is the spatial outward normal $\nu$ of $\partial B$ (it has no $\partial_t$-component: moving in $\pm\partial_t$ stays inside the cylinder for $t \in (t_0,t_1)$). Let $(f_1,f_2)$ be a positive frame of $\partial B$ for its induced orientation, and consider the candidate frame $(\partial_t, f_1, f_2)$ of $\Sigma_L$. Apply the outward-normal-first rule: $(\partial_t,f_1,f_2)$ is positive on $\Sigma_L$ iff $(\nu, \partial_t, f_1, f_2)$ is positive in $N$. Compute
> $$(\nu,\partial_t,f_1,f_2) \ \text{has orientation} \ -(\partial_t,\nu,f_1,f_2) \qquad \text{(one transposition of the first two vectors),}$$
> and $(\partial_t,\nu,f_1,f_2)$ is positive in $N$, because $(\nu,f_1,f_2)$ is positive in $\mathbb{R}^3$ (that is what "$(f_1,f_2)$ positive on $\partial B$" means, outward-normal-first) and $N$ is oriented by $dt \wedge (\text{positive spatial } 3\text{-frame})$. Hence $(\nu,\partial_t,f_1,f_2)$ is *negative* in $N$, so $(\partial_t, f_1, f_2)$ is a **negative** frame of $\Sigma_L$: the induced orientation of $\Sigma_L$ equals $-1$ times the product orientation $dt \wedge \mathrm{dvol}_{\partial B}$.
>
> **Integrate.** Writing $\int_{\Sigma_L}^{\mathrm{ind}}$ for the induced orientation and $\int_{\Sigma_L}^{\mathrm{prod}}$ for the product orientation,
> $$\int_{\Sigma_L}^{\mathrm{ind}} \iota_L^* J = -\int_{\Sigma_L}^{\mathrm{prod}} \iota_L^* J = -\int_{\Sigma_L}^{\mathrm{prod}} \big(-dt\wedge \langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}\big) = +\int_{\Sigma_L}^{\mathrm{prod}} dt\wedge \langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B},$$
> where the first equality is "induced $= -$ product", and the middle equality substitutes $\iota_L^* J = -dt\wedge\sigma$ and the flux identity. By Fubini's theorem on the product $[t_0,t_1]\times\partial B$ with the product orientation $dt\wedge\mathrm{dvol}_{\partial B}$,
> $$\int_{\Sigma_L}^{\mathrm{prod}} dt\wedge\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B} = \int_{t_0}^{t_1}\!\left(\int_{\partial B}\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}\right) dt.$$
> The two minus signs — one from the current terms of $J$, one from "induced $= -$ product" — cancel, so the lateral contribution is $+\int_{t_0}^{t_1}\!\int_{\partial B}\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}\,dt$.

**Step 5: Assemble the three faces.**

Substituting the three evaluated integrals into ($\ast$) gives the identity.

> [!note]- Derivation
> Insert Steps 2, 3, 4 into ($\ast$):
> $$0 = \underbrace{+\int_B\varrho(t_1)\,dx\,dy\,dz}_{\text{top, Step 2}} \;\underbrace{-\int_B\varrho(t_0)\,dx\,dy\,dz}_{\text{bottom, Step 3}} \;+\; \underbrace{\int_{t_0}^{t_1}\!\!\int_{\partial B}\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}\,dt}_{\text{lateral, Step 4}}.$$
> This is precisely the asserted conservation of charge. In words: the charge in $B$ at the final time minus the charge at the initial time equals minus the total current that flowed out through $\partial B$; equivalently, whatever charge leaves $B$ through its walls is exactly the charge lost from its interior.

> [!note]- Complete formal solution
> **Claim.** With $J$, $B$, $t_0 < t_1$ as above and $dJ = 0$,
> $$\int_B\varrho(t_1)\,dx\,dy\,dz - \int_B\varrho(t_0)\,dx\,dy\,dz + \int_{t_0}^{t_1}\!\!\int_{\partial B}\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}\,dt = 0.$$
>
> Orient $\mathbb{R}^4$ by $\mathrm{vol} = dt\wedge dx\wedge dy\wedge dz$ and restrict this orientation to $N = [t_0,t_1]\times B$, a compact oriented $4$-manifold with corners along $\{t_0,t_1\}\times\partial B$. Stokes' theorem for manifolds with corners (obtained from the smooth-boundary case by rounding the edges within an $\varepsilon$-collar and letting $\varepsilon\to 0$; the corner set is $3$-measure zero and contributes nothing) gives
> $$\int_N dJ = \int_{\{t_1\}\times B} J + \int_{\{t_0\}\times B} J + \int_{[t_0,t_1]\times\partial B} J,$$
> each face carrying its induced orientation. Since $dJ = 0$, the left-hand side is $0$.
>
> *Top face* $\Sigma_1 = \{t_1\}\times B$: as $t$ is constant, $\iota_1^* dt = 0$, so $\iota_1^* J = \varrho(t_1)\,dx\wedge dy\wedge dz$. The outward normal is $+\partial_t$; by the outward-normal-first rule $(\partial_t,\partial_x,\partial_y,\partial_z)$ positive in $N$ forces $(\partial_x,\partial_y,\partial_z)$ positive on $\Sigma_1$, so the induced orientation is standard and $\int_{\Sigma_1}J = +\int_B\varrho(t_1)$.
>
> *Bottom face* $\Sigma_0 = \{t_0\}\times B$: likewise $\iota_0^* J = \varrho(t_0)\,dx\wedge dy\wedge dz$. The outward normal is $-\partial_t$; since $(-\partial_t,\partial_x,\partial_y,\partial_z)$ is negative in $N$, the frame $(\partial_x,\partial_y,\partial_z)$ is negative on $\Sigma_0$, the induced orientation is the reverse of standard, and $\int_{\Sigma_0}J = -\int_B\varrho(t_0)$.
>
> *Lateral face* $\Sigma_L = [t_0,t_1]\times\partial B$: as the spatial point lies on $\partial B$, $\iota_L^*(dx\wedge dy\wedge dz) = 0$, so $\iota_L^* J = -dt\wedge\sigma$ with $\sigma = \iota_{\vec j}(dx\wedge dy\wedge dz)$, whose restriction to $\partial B$ is $\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}$. The outward normal is the spatial $\nu$; testing $(\partial_t,f_1,f_2)$ against $(\nu,\partial_t,f_1,f_2) = -(\partial_t,\nu,f_1,f_2)$ (negative in $N$) shows the induced orientation is $-1$ times the product orientation, so
> $$\int_{\Sigma_L}J = -\int^{\mathrm{prod}}(-dt\wedge\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}) = +\int_{t_0}^{t_1}\!\!\int_{\partial B}\langle\vec j,\nu\rangle\,\mathrm{dvol}_{\partial B}\,dt.$$
>
> Summing the three faces and equating to $0$ yields the claim. $\blacksquare$

> [!warning] Illegal but tempting: forgetting the sign on the $t_0$-face
> The seductive shortcut is to write $\int_{\partial N} J = \int_{\{t_1\}\times B}\varrho + \int_{\{t_0\}\times B}\varrho + (\text{flux})$ with *both* time-slices carrying the standard orientation of $B$, giving the physically nonsensical "$\int_B\varrho(t_1) + \int_B\varrho(t_0) + \text{flux} = 0$". This is wrong because the induced boundary orientation is dictated by the outward normal, and the outward normal on the initial-time face points toward *decreasing* $t$, i.e. $-\partial_t$, which reverses the orientation of $B$ and flips the sign of that integral. The corrected rule is the whole content of Step 3: *always derive a time-slice's orientation from its outward normal, never copy the slice's "natural" orientation*. The same reversal is why, in the fundamental theorem of calculus $\int_{[a,b]} f' = f(b) - f(a)$, the endpoint $a$ enters with a minus: the oriented boundary of $[a,b]$ is $\{b\} - \{a\}$, the outward normal at $a$ being $-\partial_t$.

> [!note]- Independent sanity check: the static case
> Take $\vec j = 0$ (no currents) and $\varrho$ independent of $t$. Then the continuity equation $\partial_t\varrho + \operatorname{div}\vec j = 0$ holds trivially, and the identity reads $\int_B\varrho\,-\int_B\varrho + 0 = 0$, which is correct. Now take a single point charge moving uniformly out of $B$ across the interval: the interior charge decreases from $1$ to $0$, so $\int_B\varrho(t_1) - \int_B\varrho(t_0) = -1$, and the flux term must equal $+1$ — indeed the charge crossed $\partial B$ outward once, contributing $+\int\langle\vec j,\nu\rangle = +1$. The signs balance, confirming the orientation bookkeeping.

---

# Key Takeaways

**A conservation law is the closedness of a current form read through Stokes, and the entire subtlety is orientation bookkeeping on the faces of the region.** The physics content — charge in a box changes only by flowing through the walls — is encoded once and for all in the single equation $dJ = 0$, and Stokes' theorem is the machine that converts that local, differential statement into the global, integral balance. The lesson to carry forward is that whenever a physical quantity is conserved and expressed as a flux, one should look for the differential form whose closedness expresses the law, integrate it over a spacetime region built to match the desired terms, and let Stokes do the rest. The region is chosen so that its boundary faces *are* the terms of the target identity: a top and a bottom time-slice for the "final minus initial stored quantity", and a lateral wall for the "flux out". This is the reusable template behind energy conservation (integrate the Poynting $3$-form), probability conservation in quantum mechanics (integrate the probability-current form), and mass conservation in fluid dynamics (integrate the mass-current form); the differential forms differ, the Stokes-plus-orientation skeleton does not.

**The outward-normal-first rule is the only source of signs, and it must be applied to each face separately rather than transported by intuition.** The three faces of the cylinder look symmetric, but they are not: the top face keeps the standard spatial orientation, the bottom face reverses it, and the lateral face reverses the product orientation. Each reversal is *derived*, not remembered, from the position of the outward normal — $+\partial_t$ on top, $-\partial_t$ on the bottom, spatial $\nu$ on the side — fed into the rule "$(\nu_{\mathrm{out}}, e_1,\dots,e_{n-1})$ positive $\iff$ $(e_1,\dots,e_{n-1})$ positive on the face". The trigger for deploying this discipline is any Stokes computation on a *product* region or a region with several flat faces: the moment the boundary has more than one piece, the naive impulse to give every piece its "obvious" orientation is exactly where sign errors enter. The transferable diagnostic is to ask, for each face, "which way does one leave the region here?", read off the outward normal, and only then fix the orientation; the notorious minus sign on the initial-time slice is the canonical instance, and it is the same minus that puts $-f(a)$ into the fundamental theorem of calculus and that flips the two ends of a Feynman-diagram time contour.

**Terms of a differential form vanish on a face precisely when their differentials are "used up" by the constraint defining that face, and this is what sorts charge density from current flux.** On a constant-time slice the constraint is "$t$ fixed", so $dt$ pulls back to zero and only the $dx\wedge dy\wedge dz$ (charge-density) term of $J$ survives; on the lateral wall the constraint is "the spatial point lies on the surface $\partial B$", so the full spatial volume $dx\wedge dy\wedge dz$ pulls back to zero and only the $dt$-current terms survive. Recognising which monomials die on which face is a fast, mechanical filter that halves the work before any orientation is computed: a $k$-form monomial restricts nontrivially to a submanifold only if its differentials are linearly independent along that submanifold. The pattern recurs throughout the vault — it is why, in the coordinate proof of Maxwell's equations, $dF$ and $d\star F$ split cleanly into a purely spatial $3$-form (the divergence laws) and mixed $dt$-terms (the evolution laws), and why boundary terms in variational problems localise to the pieces of $\partial M$ where the relevant field does not vanish. When facing a face integral, first strike out the monomials whose differentials collapse; only the survivors need orientation care.
