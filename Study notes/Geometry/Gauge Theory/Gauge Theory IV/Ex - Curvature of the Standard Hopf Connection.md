---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Standard Connection on the Hopf Bundle"
  - "Thm - Structure Equation for the Curvature"
  - "Def - Curvature of a Principal Connection"
  - "Def - Connection on a Principal Bundle"
  - "Thm - Coordinate Expression for the Exterior Derivative"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Consider the Hopf bundle in its lowest dimension, the principal $U(1)$-bundle
$$\pi\colon S^3 \longrightarrow \mathbb{CP}^1 \cong S^2, \qquad \pi(z) = [z],$$
where $S^3 = \{z = (z_0, z_1) \in \mathbb{C}^2 : |z_0|^2 + |z_1|^2 = 1\}$ and $U(1) = \{\lambda \in \mathbb{C} : |\lambda| = 1\}$ acts diagonally by $z \cdot \lambda = (\lambda z_0, \lambda z_1)$. We identify $\mathbb{C}^2 = \mathbb{R}^4$ with real coordinates $(x_0, x_1, x_2, x_3)$ through $z_0 = x_0 + i x_1$, $z_1 = x_2 + i x_3$, and write $\langle\cdot,\cdot\rangle$ for the standard real inner product of $\mathbb{R}^4$. The Lie algebra is $\mathfrak{u}(1) = i\mathbb{R}$, and the fundamental vector field of $i \in \mathfrak{u}(1)$ is $v(z) = i z$, that is, the position vector rotated by the ambient complex structure $J$ (multiplication by $i$). The standard Hopf connection is the $\mathfrak{u}(1)$-valued $1$-form
$$a_z(u) = \langle i z, u\rangle\, i \in \mathfrak{u}(1), \qquad u \in T_z S^3,$$
which in the real coordinates above reads
$$a = \big({-}x_1\, dx_0 + x_0\, dx_1 - x_3\, dx_2 + x_2\, dx_3\big)\, i.$$

**The task has three parts.**

1. Compute the exterior derivative $da$ in the ambient coordinates and show that $\pi^* F_a = da = 2\big(dx_0 \wedge dx_1 + dx_2 \wedge dx_3\big)\, i$, where $F_a \in \Omega^2(S^2; i\mathbb{R})$ is the curvature $2$-form on the base determined by $\pi^* F_a = \Omega$.

2. Using the ambient orthonormal frame
$$v_1 = ({-}x_1, x_0, {-}x_3, x_2), \quad v_2 = ({-}x_2, x_3, x_0, {-}x_1), \quad v_3 = ({-}x_3, {-}x_2, x_1, x_0),$$
in which $v_1 = v$ is vertical and $v_2, v_3$ are horizontal, evaluate the curvature on the projected frame and obtain $F_a(\pi_* v_2, \pi_* v_3) = 2i$.

3. Verify Bär's intrinsic formula for the curvature form on the total space,
$$\Omega_p(X, Y) = 2i\,\langle i X, Y\rangle \qquad (p \in S^3,\ X, Y \in T_p S^3),$$
directly from the invariant coordinate formula for the exterior derivative, and check that $\Omega_p$ vanishes whenever either argument is vertical.

The identification of $F_a$ with a multiple of the round area form, $F_a = 2\,\mathrm{vol}_{S^2_{1/2}}\, i$, and the resulting integral $\int_{S^2} F_a = 2\pi i$, require the quotient-metric computation and belong to the Chern–Weil chapter; they are not part of this exercise. Here we compute the curvature as a differential form.

**Recall:**

The objects in play are the Hopf bundle and its canonical connection, the curvature of a principal connection, the structure equation, and the invariant coordinate formula for the exterior derivative of a $1$-form.

![[Thm - The Standard Connection on the Hopf Bundle#Statement]]

On $S^3 \to S^2$ with $\mathfrak{u}(1) = i\mathbb{R}$, the form $a_z(u) = \langle i z, u\rangle\, i$ is the unique connection whose horizontal space $\ker a_z$ is the real-orthogonal complement of the vertical line $\mathbb{R}\, v(z)$; because $U(1)$ is abelian and acts by isometries of the round metric, $\operatorname{Ad}$-equivariance reduces to $U(1)$-invariance, which holds. See [[Thm - The Standard Connection on the Hopf Bundle]] and [[Def - The Hopf Bundle]].

![[Thm - Structure Equation for the Curvature#Statement]]

For a connection $\omega$ on a principal $G$-bundle with curvature form $\Omega$, the structure equation is $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$; when $G$ is abelian the bracket term vanishes and $\Omega = d\omega$. See [[Thm - Structure Equation for the Curvature]].

![[Def - Curvature of a Principal Connection#The Definition]]

The curvature form of $\omega$ is $\Omega(X, Y) = d\omega(\pi_H X, \pi_H Y) \in \Omega^2(P; \mathfrak{g})$, where $\pi_H$ is the horizontal projection; it is horizontal and $\operatorname{Ad}$-equivariant, hence basic, so there is a unique $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ with $\pi^* F_\omega = \Omega$. For abelian $G$ the bundle $\operatorname{ad}P$ is trivial and $F_\omega \in \Omega^2(M; \mathfrak{g})$. See [[Def - Curvature of a Principal Connection]].

For a $1$-form $\alpha$ and vector fields $X, Y$, the **invariant coordinate formula for the exterior derivative** ([[Thm - Coordinate Expression for the Exterior Derivative|Bär's convention]]) is
$$d\alpha(X, Y) = X\big(\alpha(Y)\big) - Y\big(\alpha(X)\big) - \alpha([X, Y]),$$
where $[X, Y]$ is the [[Def - The Lie Bracket of Vector Fields|Lie bracket of vector fields]], equal in Euclidean coordinates to $[X, Y] = \partial_X Y - \partial_Y X$. Because the inclusion $\iota\colon S^3 \hookrightarrow \mathbb{R}^4$ satisfies $\iota^* \circ d = d \circ \iota^*$ ([[Thm - Pull-Back Commutes with the Exterior Derivative|pull-back commutes with $d$]]), the curvature of $a$ on $S^3$ is the restriction to $S^3$ of the exterior derivative of the ambient extension $\tilde a_p(u) = \langle i p, u\rangle\, i$, defined for all $p \in \mathbb{R}^4$ and all $u \in \mathbb{R}^4$.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-curvature-in-coordinates* problem for the simplest nonabelian-looking but in fact abelian gauge field, the magnetic monopole of charge one. It is the canonical worked example that shows the abstract curvature $2$-form is a concrete, computable object, and it is the source of the number $\int_{S^2} F = 2\pi i$ that in the Chern–Weil chapter becomes the first Chern number of the Hopf line bundle. The whole computation reduces to the exterior derivative of an explicit polynomial $1$-form, because the group is abelian.

**Assumption pattern.** The single structural hypothesis doing all the work is that $U(1)$ is *abelian*. An abelian structure group has $\mathfrak{u}(1)$ commutative, so the bracket term $\tfrac12[a \wedge a]$ in the structure equation vanishes identically, and the curvature collapses to $\Omega = da$. The recognisable trigger is: whenever the structure group is $U(1)$ or any torus, expect the curvature to be *linear* in the connection, $F = dA$, and to be a closed, ordinary (not adjoint-twisted) $\mathfrak{g}$-valued form on the base. This is exactly the feature that makes electromagnetism a linear theory.

**Theorem routing.** The route is: recall the connection form $a$ from [[Thm - The Standard Connection on the Hopf Bundle]]; apply the [[Thm - Structure Equation for the Curvature|structure equation]] in its abelian form $\Omega = da$; compute $da$ by the two available routes and check they agree — the *ambient route* (differentiate the polynomial $1$-form term by term, [[Thm - Pull-Back Commutes with the Exterior Derivative|restricting from $\mathbb{R}^4$]]) and the *intrinsic route* (the [[Thm - Coordinate Expression for the Exterior Derivative|invariant formula for $d$]] on tangent vectors). The descent $\pi^* F_a = \Omega$ from [[Def - Curvature of a Principal Connection]] then lets us read the value of $F_a$ on the base off the value of $\Omega$ on horizontal lifts.

**Key decision point.** The one genuine choice is *which pair of vectors to evaluate on*. The frame $v_1, v_2, v_3$ is engineered so that $v_1 = i p$ is the vertical (fundamental) direction and $v_2, v_3$ are horizontal; moreover $i v_2 = v_3$, so $(v_2, v_3)$ is a complex-oriented orthonormal basis of the horizontal plane. Evaluating $\Omega$ on this specific horizontal pair, rather than on abstract vectors, is what converts the form-level identity $\Omega = 2i\,\langle i\cdot, \cdot\rangle$ into the single number $2i$ — and recognising that $\pi_* v_2, \pi_* v_3$ is an oriented orthonormal basis downstairs is what will later turn that number into the area form.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (see the topic page's Legal Operations; numbers to be reconciled with the topic page once written):

1. **Reduce the structure equation to the abelian curvature $\Omega = d\omega$.** When the structure group is abelian, drop the bracket term $\tfrac12[\omega \wedge \omega]$ from $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$, because $[\cdot, \cdot] = 0$ on a commutative Lie algebra. This is the specialisation of the structure equation used throughout.

2. **Differentiate a polynomial connection form term by term in ambient coordinates, then restrict.** The connection form is the restriction to $S^3$ of an ambient $1$-form with polynomial coefficients; compute its exterior derivative in $\mathbb{R}^4$ and restrict, justified by $\iota^* d = d\, \iota^*$.

3. **Use the invariant coordinate formula for $d$ of a $1$-form.** Evaluate $d\alpha(X, Y) = X(\alpha(Y)) - Y(\alpha(X)) - \alpha([X, Y])$ on tangent vector fields to obtain the curvature intrinsically, without choosing a chart on the base.

4. **Descend a horizontal equivariant form through $\pi^* F_\omega = \Omega$.** Read the value of the base curvature $F_a$ on $\pi_* v_2, \pi_* v_3$ off the value of $\Omega$ on the horizontal lifts $v_2, v_3$, using that $\Omega$ is basic.

5. **Exploit the complex structure to simplify inner products.** Use that multiplication by $i$ is an isometry, $\langle i X, i Y\rangle = \langle X, Y\rangle$, and $i^2 = -1$, to collapse $\langle i X, Y\rangle - \langle i Y, X\rangle$ to $2\langle i X, Y\rangle$ and to check verticality.

---

# Hints

> [!note]- Hint 1
> The structure group is $U(1)$, whose Lie algebra $\mathfrak{u}(1) = i\mathbb{R}$ is one-dimensional and therefore commutative. What does the structure equation $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ become when every bracket is zero? Once you see that, the entire problem is the exterior derivative of one explicit $1$-form.

> [!note]- Hint 2
> Write $a = ({-}x_1\, dx_0 + x_0\, dx_1 - x_3\, dx_2 + x_2\, dx_3)\, i$ and differentiate. Recall $d(f\, dx_j) = df \wedge dx_j$ and $d(dx_j) = 0$, and that $dx_k \wedge dx_j = -\, dx_j \wedge dx_k$. Two of the four terms reinforce each other rather than cancel — watch the sign of $-\,dx_1 \wedge dx_0$.

> [!note]- Hint 3
> For the intrinsic route, apply $d\alpha(X, Y) = X(\alpha(Y)) - Y(\alpha(X)) - \alpha([X, Y])$ to $\alpha = a$ with $\alpha_p(u) = i\langle i p, u\rangle$. Extend $X, Y$ to vector fields; then $X(\alpha(Y))$ differentiates $p \mapsto i\langle i p, Y(p)\rangle$ along $X$. The derivative of $p \mapsto i p$ in the direction $X$ is $i X$ (it is linear), and $[X, Y] = \partial_X Y - \partial_Y X$ in $\mathbb{R}^4$. Three of your terms will collect into $i\langle i p,\, \partial_X Y - \partial_Y X - [X, Y]\rangle$ — which is zero.

> [!note]- Hint 4
> After the cancellation you are left with $i\langle i X, Y\rangle - i\langle i Y, X\rangle$. Use that $i$ is an isometry: $\langle i Y, X\rangle = \langle i(iY), iX\rangle = \langle -Y, i X\rangle = -\langle i X, Y\rangle$. Hence the two terms add. For verticality, substitute $X = i p$ and remember $i(i p) = -p$ and $Y \perp p$ for $Y$ tangent to the sphere.

> [!note]- Hint 5
> To reconcile the two routes and get a number: check that $i v_2 = v_3$, so $\langle i v_2, v_3\rangle = |v_3|^2 = 1$ on the unit sphere. Both routes then give $\Omega(v_2, v_3) = 2i$, and since $v_2, v_3$ are horizontal, $F_a(\pi_* v_2, \pi_* v_3) = \pi^* F_a(v_2, v_3) = \Omega(v_2, v_3) = 2i$.

---

# Solution

The computation is short because the group is abelian: the structure equation degenerates to $\Omega = da$, and everything reduces to the exterior derivative of one polynomial $1$-form. We carry it out twice — once by differentiating in the ambient coordinates of $\mathbb{R}^4$ and once by the invariant formula on tangent vectors — and check that the two agree and that the common answer, evaluated on the horizontal frame, is $2i$. Throughout, $J$ denotes multiplication by $i$ on $\mathbb{C}^2 = \mathbb{R}^4$, so that $J(x_0, x_1, x_2, x_3) = ({-}x_1, x_0, {-}x_3, x_2)$ and $v(p) = i p = J p$.

**Step 1: The abelian structure equation reduces the curvature to $\Omega = da$.**

Because $\mathfrak{u}(1) = i\mathbb{R}$ is commutative, the bracket term drops out of the structure equation, leaving $\Omega = da$; hence $\pi^* F_a = da$.

> [!note]- Derivation
> By the [[Thm - Structure Equation for the Curvature|structure equation]], the curvature form of the connection $a$ on the total space $S^3$ is
> $$\Omega = da + \tfrac12[a \wedge a] \qquad \text{(structure equation).}$$
> The bracket of $\mathfrak{u}(1)$-valued $1$-forms is computed value-by-value from the Lie bracket of $\mathfrak{u}(1)$ ([[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|definition of the bracket of Lie-algebra-valued forms]]): for $1$-forms $[a \wedge a](X, Y) = 2[a(X), a(Y)]$. Since $\mathfrak{u}(1) = i\mathbb{R}$ is one-dimensional, its Lie bracket vanishes identically, $[\xi, \eta] = 0$ for all $\xi, \eta \in \mathfrak{u}(1)$; therefore
> $$\tfrac12[a \wedge a] = 0 \qquad \text{(}\mathfrak{u}(1)\text{ abelian).}$$
> Consequently $\Omega = da$. By [[Def - Curvature of a Principal Connection|the definition of the base curvature]], $F_a \in \Omega^2(S^2; i\mathbb{R})$ is the unique form with $\pi^* F_a = \Omega$, so
> $$\pi^* F_a = da \qquad \text{(}\Omega = da\text{ and }\pi^* F_a = \Omega\text{).}$$
> The adjoint bundle $\operatorname{ad}P$ is trivial here because $\operatorname{Ad}$ is trivial for an abelian group, which is why $F_a$ is an ordinary $i\mathbb{R}$-valued $2$-form on $S^2$ rather than a section of a twisted bundle.

**Step 2: Compute $da$ in ambient coordinates.**

Differentiating the polynomial $1$-form term by term gives $da = 2(dx_0 \wedge dx_1 + dx_2 \wedge dx_3)\, i$.

> [!note]- Derivation
> The connection form is the restriction to $S^3$ of the ambient $1$-form $\tilde a = ({-}x_1\, dx_0 + x_0\, dx_1 - x_3\, dx_2 + x_2\, dx_3)\, i$ on $\mathbb{R}^4$. Since [[Thm - Pull-Back Commutes with the Exterior Derivative|pull-back commutes with the exterior derivative]], $da = \iota^*(d\tilde a)$, so it suffices to differentiate $\tilde a$ in $\mathbb{R}^4$ and restrict. Using $d(f\, dx_j) = df \wedge dx_j$ and $d(dx_j) = 0$, and that $i \in \mathfrak{u}(1)$ is a constant coefficient,
> $$d\tilde a = \big({-}dx_1 \wedge dx_0 + dx_0 \wedge dx_1 - dx_3 \wedge dx_2 + dx_2 \wedge dx_3\big)\, i \qquad \text{(Leibniz rule term by term).}$$
> Now $-\,dx_1 \wedge dx_0 = dx_0 \wedge dx_1$ and $-\,dx_3 \wedge dx_2 = dx_2 \wedge dx_3$ (antisymmetry of the wedge product), so the four terms collect in pairs:
> $$d\tilde a = \big(2\, dx_0 \wedge dx_1 + 2\, dx_2 \wedge dx_3\big)\, i = 2\big(dx_0 \wedge dx_1 + dx_2 \wedge dx_3\big)\, i \qquad \text{(combining like terms).}$$
> Restricting to $S^3$ and combining with Step 1,
> $$\pi^* F_a = da = 2\big(dx_0 \wedge dx_1 + dx_2 \wedge dx_3\big)\, i.$$
> The $2$-form $\sigma := dx_0 \wedge dx_1 + dx_2 \wedge dx_3$ is (the restriction of) the standard Kähler form of $\mathbb{C}^2$; we shall meet it again in Step 4 as $\sigma(X, Y) = \langle J X, Y\rangle$.

**Step 3: Evaluate on the horizontal frame to obtain $F_a(\pi_* v_2, \pi_* v_3) = 2i$.**

The vectors $v_2, v_3$ are horizontal; evaluating $da$ on them gives $2i$, and by descent this is $F_a$ on the projected frame.

> [!note]- Derivation
> First we confirm the geometric roles of the frame. Each $v_k$ is tangent to $S^3$ at $p$ because $\langle p, v_k\rangle = 0$, which we check for all three vectors by direct expansion:
> $$\langle p, v_1\rangle = x_0({-}x_1) + x_1 x_0 + x_2({-}x_3) + x_3 x_2 = 0 \qquad \text{(direct expansion; the four terms cancel in pairs),}$$
> $$\langle p, v_2\rangle = x_0({-}x_2) + x_1 x_3 + x_2 x_0 + x_3({-}x_1) = 0 \qquad \text{(direct expansion),}$$
> $$\langle p, v_3\rangle = x_0({-}x_3) + x_1({-}x_2) + x_2 x_1 + x_3 x_0 = 0 \qquad \text{(direct expansion).}$$
> The vector $v_1 = i p = v(p)$ is the fundamental vector field, hence vertical. The vectors $v_2, v_3$ are horizontal because they are orthogonal to $v_1$:
> $$\langle v_1, v_2\rangle = x_1 x_2 + x_0 x_3 - x_3 x_0 - x_2 x_1 = 0, \qquad \langle v_1, v_3\rangle = x_1 x_3 - x_0 x_2 - x_3 x_1 + x_2 x_0 = 0 \qquad \text{(direct expansion).}$$
> Therefore $a(v_2) = i\langle i p, v_2\rangle = i\langle v_1, v_2\rangle = 0$ (using $i p = v_1$ and the first vanishing inner product) and $a(v_3) = i\langle i p, v_3\rangle = i\langle v_1, v_3\rangle = 0$ (using the second), which is exactly the condition $v_2, v_3 \in \ker a = H$ (see [[Def - Horizontal Subspace and Horizontal Lift]]). Thus $v_2, v_3$ are the horizontal lifts of $\pi_* v_2, \pi_* v_3$.
>
> Now evaluate $da = 2i\,\sigma$ with $\sigma = dx_0 \wedge dx_1 + dx_2 \wedge dx_3$ on $(v_2, v_3)$. Reading off the coordinates $v_2 = ({-}x_2, x_3, x_0, {-}x_1)$ and $v_3 = ({-}x_3, {-}x_2, x_1, x_0)$,
> $$(dx_0 \wedge dx_1)(v_2, v_3) = ({-}x_2)({-}x_2) - ({-}x_3)(x_3) = x_2^2 + x_3^2 \qquad \text{(}dx_0 \wedge dx_1 \text{ picks out the first two components),}$$
> $$(dx_2 \wedge dx_3)(v_2, v_3) = (x_0)(x_0) - (x_1)({-}x_1) = x_0^2 + x_1^2 \qquad \text{(}dx_2 \wedge dx_3 \text{ picks out the last two components).}$$
> Adding and using $|p|^2 = x_0^2 + x_1^2 + x_2^2 + x_3^2 = 1$ on $S^3$,
> $$da(v_2, v_3) = 2i\,(x_2^2 + x_3^2 + x_0^2 + x_1^2) = 2i \qquad \text{(sum of the two terms; }|p| = 1\text{).}$$
> Because $v_2, v_3$ are horizontal, $\pi^* F_a(v_2, v_3) = F_a(\pi_* v_2, \pi_* v_3)$ (definition of pull-back), and by Step 1 $\pi^* F_a = da$, so
> $$F_a(\pi_* v_2, \pi_* v_3) = da(v_2, v_3) = 2i.$$

**Step 4: The intrinsic formula $\Omega_p(X, Y) = 2i\,\langle i X, Y\rangle$ and vanishing on vertical vectors.**

Applying the invariant coordinate formula for $d$ to $a_p(u) = i\langle i p, u\rangle$ gives $\Omega_p(X, Y) = 2i\,\langle i X, Y\rangle$, which vanishes as soon as $X$ or $Y$ is vertical.

> [!note]- Derivation
> Extend $X, Y \in T_p S^3$ to vector fields on $S^3$ (equivalently, to ambient vector fields tangent along $S^3$). By the [[Thm - Coordinate Expression for the Exterior Derivative|invariant formula for the exterior derivative of a $1$-form]],
> $$d a(X, Y) = X\big(a(Y)\big) - Y\big(a(X)\big) - a([X, Y]) \qquad \text{(invariant formula for } d\text{).}$$
> Here $a(Y)$ is the function $p \mapsto i\langle i p, Y(p)\rangle$. Differentiating it along $X$ by the Leibniz rule for the inner product, and using that $p \mapsto i p$ is linear so its directional derivative in the direction $X$ is $i X$,
> $$X\big(a(Y)\big) = i\langle i X, Y\rangle + i\langle i p, \partial_X Y\rangle \qquad \text{(Leibniz rule; } \partial_X(i p) = i X\text{).}$$
> Interchanging the roles of $X$ and $Y$,
> $$Y\big(a(X)\big) = i\langle i Y, X\rangle + i\langle i p, \partial_Y X\rangle \qquad \text{(same computation with } X \leftrightarrow Y\text{).}$$
> The third term uses that $[X, Y] = \partial_X Y - \partial_Y X$ in Euclidean coordinates ([[Def - The Lie Bracket of Vector Fields|Lie bracket of vector fields]]):
> $$a([X, Y]) = i\langle i p, \partial_X Y - \partial_Y X\rangle \qquad \text{(evaluate } a \text{ on } [X, Y]\text{).}$$
> Substituting the three lines into the invariant formula, the terms carrying $i\langle i p, \cdot\rangle$ combine to
> $$i\langle i p, \partial_X Y\rangle - i\langle i p, \partial_Y X\rangle - i\langle i p, \partial_X Y - \partial_Y X\rangle = 0 \qquad \text{(these three terms cancel exactly),}$$
> leaving
> $$d a(X, Y) = i\langle i X, Y\rangle - i\langle i Y, X\rangle \qquad \text{(after the cancellation).}$$
> Finally, since multiplication by $i$ is an isometry of $\mathbb{R}^4$ and $i^2 = -1$,
> $$\langle i Y, X\rangle = \langle i(iY), i X\rangle = \langle {-}Y, i X\rangle = -\langle i X, Y\rangle \qquad \text{(}i \text{ isometry, } i^2 = -1\text{, symmetry of }\langle\cdot,\cdot\rangle\text{),}$$
> so the two terms add:
> $$\Omega_p(X, Y) = d a(X, Y) = i\big(\langle i X, Y\rangle + \langle i X, Y\rangle\big) = 2i\,\langle i X, Y\rangle,$$
> where we used $\Omega = da$ from Step 1.
>
> **Vanishing on vertical vectors.** The vertical vectors at $p$ are the multiples of $v(p) = i p$. Putting $X = i p$,
> $$\Omega_p(i p, Y) = 2i\,\langle i(i p), Y\rangle = 2i\,\langle {-}p, Y\rangle = -2i\,\langle p, Y\rangle = 0 \qquad \text{(}i^2 = -1\text{; } Y \in T_p S^3 = p^\perp\text{),}$$
> because every tangent vector to the sphere is orthogonal to the position vector. By antisymmetry $\Omega_p(X, i p) = 0$ as well. Thus $\Omega_p$ is horizontal, consistent with $\Omega(X, Y) = da(\pi_H X, \pi_H Y)$.

**Step 5: The two routes agree, and the number is $2i$.**

The form-level identities of Steps 2 and 4 are the same, and both give $\Omega(v_2, v_3) = 2i$.

> [!note]- Derivation
> The two expressions for $\Omega = da$ coincide as $2$-forms: for any $X, Y$,
> $$2i\,\sigma(X, Y) = 2i\big((dx_0 \wedge dx_1) + (dx_2 \wedge dx_3)\big)(X, Y) = 2i\,(X_0 Y_1 - X_1 Y_0 + X_2 Y_3 - X_3 Y_2),$$
> while, writing $i X = J X = ({-}X_1, X_0, {-}X_3, X_2)$,
> $$2i\,\langle i X, Y\rangle = 2i\big({-}X_1 Y_0 + X_0 Y_1 - X_3 Y_2 + X_2 Y_3\big) = 2i\,(X_0 Y_1 - X_1 Y_0 + X_2 Y_3 - X_3 Y_2),$$
> which is the same expression; hence $\sigma(X, Y) = \langle J X, Y\rangle$, as anticipated in Step 2. Evaluating the intrinsic formula directly on the horizontal pair confirms Step 3: since $i v_2 = J v_2 = J({-}x_2, x_3, x_0, {-}x_1) = ({-}x_3, {-}x_2, x_1, x_0) = v_3$,
> $$\Omega(v_2, v_3) = 2i\,\langle i v_2, v_3\rangle = 2i\,\langle v_3, v_3\rangle = 2i\,|v_3|^2 = 2i \qquad \text{(}i v_2 = v_3\text{; } |v_3| = 1\text{).}$$
> The identity $i v_2 = v_3$ says precisely that $(v_2, v_3)$ is a complex-oriented orthonormal basis of the horizontal plane $H_p$, which is why the curvature attains its maximal value on this pair.

> [!note]- Complete formal solution
> **Claim.** For the standard Hopf connection $a_z(u) = \langle i z, u\rangle\, i$ on $\pi\colon S^3 \to S^2$, the curvature on the total space is $\Omega = da = 2(dx_0 \wedge dx_1 + dx_2 \wedge dx_3)\, i$, equivalently $\Omega_p(X, Y) = 2i\,\langle i X, Y\rangle$; it vanishes on vertical vectors, and the base curvature satisfies $F_a(\pi_* v_2, \pi_* v_3) = 2i$ on the horizontal frame $v_2, v_3$.
>
> Since $\mathfrak{u}(1) = i\mathbb{R}$ is commutative, $[a \wedge a] = 0$, so the structure equation $\Omega = da + \tfrac12[a \wedge a]$ reduces to $\Omega = da$; and $\pi^* F_a = \Omega = da$ with $F_a \in \Omega^2(S^2; i\mathbb{R})$ because $\operatorname{ad}P$ is trivial for abelian $G$.
>
> The connection form is the restriction of $\tilde a = ({-}x_1\, dx_0 + x_0\, dx_1 - x_3\, dx_2 + x_2\, dx_3)\, i$. As pull-back commutes with $d$,
> $$da = \iota^* d\tilde a = \big({-}dx_1 \wedge dx_0 + dx_0 \wedge dx_1 - dx_3 \wedge dx_2 + dx_2 \wedge dx_3\big)\, i = 2\big(dx_0 \wedge dx_1 + dx_2 \wedge dx_3\big)\, i,$$
> using $-\,dx_1 \wedge dx_0 = dx_0 \wedge dx_1$ and $-\,dx_3 \wedge dx_2 = dx_2 \wedge dx_3$.
>
> Alternatively, extending $X, Y$ to vector fields and applying $da(X, Y) = X(a(Y)) - Y(a(X)) - a([X, Y])$ to $a_p(u) = i\langle i p, u\rangle$, the derivative of $p \mapsto i p$ in the direction $X$ is $i X$, and $[X, Y] = \partial_X Y - \partial_Y X$, so the terms $i\langle i p, \partial_X Y - \partial_Y X - [X, Y]\rangle$ cancel, leaving $da(X, Y) = i\langle i X, Y\rangle - i\langle i Y, X\rangle$. As $i$ is an isometry with $i^2 = -1$, $\langle i Y, X\rangle = -\langle i X, Y\rangle$, whence $\Omega_p(X, Y) = 2i\,\langle i X, Y\rangle$. Substituting $X = i p$ gives $\Omega_p(i p, Y) = 2i\,\langle {-}p, Y\rangle = 0$ since $Y \perp p$; so $\Omega$ vanishes on vertical vectors.
>
> The frame $v_1 = i p$, $v_2, v_3$ is orthonormal and tangent to $S^3$, with $v_1$ vertical and $v_2, v_3$ horizontal (each is orthogonal to $v_1$, hence annihilated by $a$). Since $i v_2 = v_3$,
> $$F_a(\pi_* v_2, \pi_* v_3) = \pi^* F_a(v_2, v_3) = \Omega(v_2, v_3) = 2i\,\langle i v_2, v_3\rangle = 2i\,|v_3|^2 = 2i. \qquad \blacksquare$$

> [!warning] Illegal but tempting shortcut
> One is tempted to declare $\Omega = da$ "obvious from $F = dA$" and skip the descent, evaluating $da$ on an *arbitrary* orthonormal pair of tangent vectors and expecting to read off the curvature of the base. This is wrong unless the pair is *horizontal*: on a vertical–horizontal pair $\Omega$ vanishes, and on two vertical vectors it also vanishes, so an arbitrary pair generally underestimates the base curvature. The value $F_a(\pi_* v_2, \pi_* v_3)$ is meaningful only because $v_2, v_3 \in \ker a$; this is exactly the content of $\Omega(X, Y) = da(\pi_H X, \pi_H Y)$. The extra condition that makes the naive reading legal is that both vectors be horizontal.

---

# Key Takeaways

**For an abelian structure group the curvature is linear in the connection: $F = dA$, and the whole computation is one exterior derivative.** The bracket term $\tfrac12[A \wedge A]$ in the structure equation is quadratic in the connection and is precisely the mark of a nonabelian gauge field; it vanishes identically for $U(1)$, for tori, and for any group with commutative Lie algebra. The reusable principle is that the *nonlinearity* of a gauge theory lives entirely in the bracket term, so the trigger "structure group $U(1)$" should immediately license the replacement $F \rightsquigarrow dA$. The diagnostic transfers directly to electromagnetism, where $F = dA$ is Maxwell's field strength and its linearity is the superposition principle for electromagnetic fields; the same reduction is what makes the Chern number $\int_{S^2} F$ computable by an elementary integral in the next chapter.

**Two computations of the same curvature — ambient differentiation and the invariant formula — should always agree, and checking that they do is a free correctness test.** The ambient route (differentiate the polynomial $1$-form in $\mathbb{R}^4$, restrict) is fastest when a connection is given by an explicit formula; the intrinsic route (the invariant coordinate formula for $d$) is indispensable when no ambient extension is available and reveals structural facts, here the clean expression $\Omega_p(X, Y) = 2i\,\langle i X, Y\rangle = 2i\,\sigma(X, Y)$ exhibiting the curvature as (twice, times $i$) the Kähler form. Whenever both routes are available, computing a curvature twice and matching the answers catches sign errors in the wedge product and factor-of-two errors in the bracket convention — the two most common mistakes in this subject. The identity $\sigma(X, Y) = \langle J X, Y\rangle$ obtained by matching is itself the definition of the Kähler form and recurs whenever a complex structure and a compatible metric are present.

**Curvature vanishes on vertical directions by construction, so its only nonzero values live on horizontal pairs, and evaluating on a complex-oriented horizontal frame extracts the invariant.** The horizontal frame here is engineered so that $i v_2 = v_3$; this single relation says $(v_2, v_3)$ is a positively oriented orthonormal complex basis of the horizontal plane, and it is what turns the form identity into the number $2i$. The transferable lesson is that to read a geometric invariant off a curvature form one evaluates on an *adapted* frame — horizontal for a principal connection, oriented and orthonormal for a metric quantity — never on arbitrary vectors, because the bundle projection $\pi_*$ only sees the horizontal part. This is the computational counterpart of the fact that the nonintegrability of the horizontal distribution, shown in the companion exercise [[Ex - The Horizontal Distribution of the Hopf Connection is Not Integrable]] via $[v_2, v_3] = -2 v_1$, is *the same number $2$* that appears in the curvature: curvature is the vertical component of the bracket of horizontal lifts. The metric refinement $F_a = 2\,\mathrm{vol}_{S^2_{1/2}}\, i$ and the integral **$\int_{S^2} F_a = 2\pi i$** belong to the Chern–Weil chapter and are recorded there.
