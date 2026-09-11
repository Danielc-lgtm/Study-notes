---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Transition Functions and the Cocycle Condition"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Transition Function of a Vector Bundle"
  - "Def - Local Frame"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Equip the two-sphere $S^2 = \{\xi = (\xi_1, \xi_2, \xi_3) \in \mathbb{R}^3 : \xi_1^2 + \xi_2^2 + \xi_3^2 = 1\}$ with its two stereographic charts, taken **orientation-compatibly** (both inducing the complex orientation of $S^2 = \mathbb{CP}^1$):
$$\varphi_1 : U_1 = S^2 \setminus \{N\} \to \mathbb{C}, \quad \varphi_1(\xi) = \frac{\xi_1 + i \xi_2}{1 - \xi_3} =: z \quad (N = (0,0,1)), \qquad \varphi_2 : U_2 = S^2 \setminus \{S\} \to \mathbb{C}, \quad \varphi_2(\xi) = \frac{\xi_1 - i \xi_2}{1 + \xi_3} =: w \quad (S = (0,0,-1)).$$
(The conjugating sign $\xi_1 - i\xi_2$ in $\varphi_2$ is exactly what keeps the atlas oriented; the naive choice $\xi_1 + i\xi_2$ would reverse orientation — see the warning in the solution.) Over each chart the coordinate vector fields give a **local frame** of the tangent bundle,
$$e^{(1)} = (\partial_{x_1}, \partial_{y_1}) \text{ on } U_1 \quad (z = x_1 + i y_1), \qquad e^{(2)} = (\partial_{x_2}, \partial_{y_2}) \text{ on } U_2 \quad (w = x_2 + i y_2),$$
and a local frame is precisely a local section of the frame bundle $\operatorname{Fr}(TS^2)$, the principal $GL_2(\mathbb{R})$-bundle of ordered bases of the tangent spaces. Let $g_{12} : U_{12} = U_1 \cap U_2 = S^2 \setminus \{N, S\} \to GL_2(\mathbb{R})$ be the transition function of $\operatorname{Fr}(TS^2)$ with respect to these two frames. By the theorem that the frame bundle's transition functions coincide with the vector bundle's, and the chain rule for coordinate vector fields, it is the Jacobian of the change of coordinates $\phi = \varphi_2 \circ \varphi_1^{-1}$: the chain rule gives $e^{(1)} = e^{(2)} \cdot g_{12}$ with $g_{12} = D\phi$ (it re-expresses the chart-1 frame in the chart-2 frame). Under the series' section convention $s_\beta = s_\alpha g_{\alpha\beta}$ this same matrix would carry the label $g_{21}$; the labelling does not affect the magnitude-$2$ winding number that is the point of the exercise, and we flag it in the Convention callout below.

**Prove the following.**

1. **(Chart change.)** The coordinate change is $\phi(z) = \varphi_2 \circ \varphi_1^{-1}(z) = 1/z$ on $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$, and its real Jacobian is
$$g_{12}(z) = \frac{1}{|z|^4} \begin{pmatrix} y^2 - x^2 & -2xy \\ 2xy & y^2 - x^2 \end{pmatrix}, \qquad z = x + iy \in \mathbb{C}^\times.$$
2. **(Conformal factor times rotation.)** Show $g_{12}(z)$ is complex multiplication by $\phi'(z) = -1/z^2 = -\overline{z}^2/|z|^4$, and that consequently
$$g_{12}(z) = |z|^{-2} \, R(z), \qquad R(z) = -\left(\frac{\overline{z}}{|z|}\right)^2 \in SO(2),$$
a positive scalar $|z|^{-2}$ times a rotation. In particular $\det g_{12}(z) = |z|^{-4} > 0$, so the frames are orientation-compatible.
3. **(Reduction to $SO(2) = U(1)$.)** On the orthonormal (rotation) frame bundle the scalar $|z|^{-2}$ is absorbed by normalising the frames, leaving the $SO(2) = U(1)$-valued transition function
$$\widehat{g}_{12}(z) = R(z) = -\left(\frac{\overline{z}}{|z|}\right)^2 = \left(\frac{z}{|z|}\right)^{\mp 2} \quad (\text{up to the constant rotation } -1),$$
whose restriction to the equator $\{|z| = 1\}$ has **winding number** $\mp 2$.
4. **(Foreshadowing $c_1$.)** Conclude that the degree of the $U(1)$-transition function of $TS^2$ has magnitude $2$, matching $c_1(TS^2)[S^2] = \chi(S^2) = 2$, the value proved by curvature integration in chapter VI.

> [!warning] Convention: which Jacobian, and the sign of the winding
> The transition function of a rank-$k$ vector bundle depends on a chart-ordering convention. We take $g_{12}$ to be the Jacobian $D\phi$ of the coordinate change $\phi = \varphi_2 \circ \varphi_1^{-1}$, which is what the chain rule delivers for the frame relation $e^{(1)} = e^{(2)} g_{12}$ and which produces the $|z|^{-2}$-times-rotation form the spec requests. In [[Def - Transition Functions and the Cocycle Condition|the series' section convention]] $s_\beta = s_\alpha g_{\alpha\beta}$ (i.e. $e^{(2)} = e^{(1)} g_{12}^{\text{sec}}$) the same object is labelled $g_{21}^{\text{sec}}$, so $g_{12}^{\text{sec}} = (D\phi)^{-1} = D(\varphi_1 \circ \varphi_2^{-1})$ is complex multiplication by $-z^2$, a factor $|z|^{2}$ times the inverse rotation, with winding $\pm 2$. The *magnitude* of the winding, $2$, is convention-independent and equals $|\chi(S^2)|$; the *sign* is fixed to $+2$ by the complex orientation of $S^2$ (equivalently $TS^2 \cong \mathcal{O}(2)$ over $\mathbb{CP}^1$), which is the datum chapter VI pins down. We therefore compute the winding of our $g_{12}$ as $-2$, and the orientation-fixed invariant $c_1(TS^2)[S^2] = +2$.

**Recall:**

The objects in play are the frame bundle of a vector bundle, the transition function that glues two local frames, and the winding number of a circle map.

![[Def - Frame Bundle of a Vector Bundle#The Definition]]

The [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E) = \bigsqcup_{m} \operatorname{Fr}(E_m)$ of a rank-$k$ real vector bundle $E \to M$ has, as fibre over $m$, the set of ordered bases (equivalently, linear isomorphisms $\mathbb{R}^k \to E_m$) of $E_m$, with the free transitive right $GL_k(\mathbb{R})$-action $(b_1, \dots, b_k) \cdot h = \big(\sum_i b_i h_{i1}, \dots, \sum_i b_i h_{ik}\big)$ that reshuffles a basis by a matrix. A local frame $e = (e_1, \dots, e_k)$ over $U$ is a local section $U \to \operatorname{Fr}(E)|_U$. For $E = TS^2$ and $k = 2$ the structure group is $GL_2(\mathbb{R})$.

![[Def - Transition Functions and the Cocycle Condition#The Definition]]

![[Def - Transition Function of a Vector Bundle#The Definition]]

The bridge that turns this into a computation — *the frame bundle's cocycle is the vector bundle's cocycle*: for two local frames $e^{(\alpha)}, e^{(\beta)}$ of a vector bundle $E$, the principal-bundle transition function is exactly the [[Def - Transition Function of a Vector Bundle|vector-bundle transition matrix]] expressing one frame in terms of the other. For $E = TM$ with coordinate frames from two charts $\varphi_\alpha, \varphi_\beta$, the chain rule $\partial_{x_\alpha^i} = \sum_j \tfrac{\partial x_\beta^j}{\partial x_\alpha^i}\, \partial_{x_\beta^j}$ says the matrix re-expressing $e^{(\alpha)}$ in the frame $e^{(\beta)}$ is the Jacobian of the change of coordinates $\varphi_\beta \circ \varphi_\alpha^{-1}$, that is, $e^{(\alpha)} = e^{(\beta)} \cdot D(\varphi_\beta \circ \varphi_\alpha^{-1})$. It is this Jacobian that we take as $g_{12}$ (with $\alpha = 1, \beta = 2$), so that $e^{(1)} = e^{(2)} g_{12}$; the reciprocal labelling is recorded in the Convention callout.

![[Def - Local Frame#The Definition]]

![[Def - Winding Number#The Definition]]

The [[Def - Winding Number|winding number]] of a continuous loop $\gamma : S^1 \to \mathbb{C}^\times$ (equivalently $\gamma : S^1 \to U(1)$ after normalising) counts the net number of times $\gamma$ encircles the origin; for $\gamma(\theta) = c\, e^{ik\theta}$ with $c \neq 0$ it equals the integer $k$. It is the degree of the induced map $S^1 \to S^1$, and by [[Thm - Pi_1 of S^1 is Z|the computation of $\pi_1(S^1)$]] it is a complete homotopy invariant of such loops. The stereographic charts themselves are set up on [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection|the sphere's smooth-manifold page]].

---

# Convergent Strategy

**Problem class.** This is a *compute-the-cocycle* problem: from an explicit atlas, produce the group-valued transition function of a tangent frame bundle and read its topology off the winding number. It is the tangent-bundle twin of [[Ex - Explicit Local Sections and the Transition Function of the Hopf Bundle|the Hopf-bundle transition computation]], and it is the concrete calculation underneath the statement $c_1(TS^2)[S^2] = 2$: the first Chern (equivalently Euler) number of an oriented plane bundle over a surface *is* the winding number of the $SO(2)$-transition function around the boundary circle of a disc covering the two-chart overlap. The entire computation reduces to differentiating one holomorphic map, $z \mapsto 1/z$.

**Assumption pattern.** The decisive simplification is that the transition map $\phi(z) = 1/z$ is *holomorphic*. For a holomorphic map the real Jacobian is not an arbitrary $2 \times 2$ matrix but complex multiplication by the derivative $\phi'(z)$ — a matrix of the special form $\begin{pmatrix} p & -q \\ q & p \end{pmatrix}$, i.e. a positive scalar times a rotation. This is the recognisable trigger: whenever a chart change is holomorphic, do not grind out four partial derivatives; write down $\phi'(z)$ and read the conformal-plus-rotation structure directly. The orientation-compatibility of the atlas is precisely the condition that makes the transition holomorphic (rather than antiholomorphic $z \mapsto 1/\overline{z}$), so $\det g_{12} > 0$ everywhere.

**Theorem routing.** The route is: (i) invert $\varphi_1$ and compose to get $\phi(z) = 1/z$, using the identity $z \cdot \varphi_2 = 1$ that the sphere relation supplies; (ii) invoke the frame-bundle/vector-bundle cocycle identity to declare $g_{12} = D\phi$; (iii) compute $D\phi$ either by four partial derivatives or, faster, as complex multiplication by $\phi'(z) = -1/z^2$; (iv) polar-decompose $g_{12} = |z|^{-2} R(z)$ into conformal factor and rotation, checking $R \in SO(2)$; (v) pass to the orthonormal frame bundle, where the conformal factor cancels because it is the ratio of the two charts' metric conformal factors, leaving $\widehat{g}_{12} = R$; (vi) restrict to the equator and compute the winding number as the degree of $\theta \mapsto -e^{-2i\theta}$, obtaining $\mp 2$, then quote the chapter-VI identification with $c_1(TS^2)[S^2]$.

**Key decision point.** Two non-obvious moves. First, *use holomorphy to shortcut the Jacobian*: recognising $\phi(z) = 1/z$ as complex-differentiable turns a Jacobian computation into a one-line derivative and exposes the conformal-times-rotation form for free. Second, *the reduction of the structure group from $GL_2(\mathbb{R})$ to $SO(2)$ is where the topology becomes visible*: the full $GL_2(\mathbb{R})$-cocycle $|z|^{-2} R$ is homotopically trivial as a map into the contractible-onto-$O(2)$ group, but its $SO(2)$-part $R$ is a genuine loop in $U(1)$ whose winding number is a homotopy invariant. The insight is that *the scalar carries no topology and the rotation carries all of it*; discarding the (positive, hence contractible) conformal factor is exactly the reduction to the maximal compact subgroup that makes the Euler number appear.

---

# Legal Operations Used

Keyed to the topic page's Legal Operations (numbers to be reconciled by the topic page).

1. **Identify the frame-bundle cocycle with the vector-bundle Jacobian.** For coordinate frames of $TM$, the transition function of $\operatorname{Fr}(TM)$ is the Jacobian of the chart change; this is the operation that converts a bundle question into a calculus computation.

2. **Differentiate a holomorphic chart change as complex multiplication.** A holomorphic $\phi$ has real Jacobian equal to multiplication by $\phi'(z)$, a matrix $\begin{pmatrix} p & -q \\ q & p \end{pmatrix}$ with $p + iq = \phi'(z)$. This bypasses four separate partial derivatives.

3. **Polar-decompose a conformal linear map into scalar and rotation.** A nonzero complex number $\zeta = |\zeta| \cdot (\zeta/|\zeta|)$ factors as (positive scalar) $\times$ ($SO(2)$-rotation); applied to $\phi'(z) = -1/z^2$ this gives $g_{12} = |z|^{-2} R$.

4. **Reduce the structure group by normalising frames against the metric.** Dividing each coordinate frame by its metric length (Gram–Schmidt for an already-orthogonal conformal frame) reduces $GL_2(\mathbb{R})$ to $SO(2)$; the positive conformal scalar, being the ratio of the two charts' conformal factors, cancels in the reduced cocycle.

5. **Extract topology as a winding number / degree of a circle map.** The $SO(2) = U(1)$-transition, restricted to the equatorial loop, is a map $S^1 \to S^1$ whose winding number (degree) is a homotopy invariant computed by counting the net rotation; here it equals $\mp 2$.

---

# Hints

> [!note]- Hint 1
> To find $\phi = \varphi_2 \circ \varphi_1^{-1}$ you do not need $\varphi_1^{-1}$ in closed form. Set $z = \varphi_1(\xi) = \tfrac{\xi_1 + i\xi_2}{1 - \xi_3}$ and $w = \varphi_2(\xi) = \tfrac{\xi_1 - i\xi_2}{1 + \xi_3}$, and compute the product $z \cdot w$. The numerator is $(\xi_1 + i\xi_2)(\xi_1 - i\xi_2) = \xi_1^2 + \xi_2^2$ and the denominator is $(1 - \xi_3)(1 + \xi_3) = 1 - \xi_3^2$; the sphere relation makes these equal. What does that force $w$ to be in terms of $z$?

> [!note]- Hint 2
> $\phi(z) = 1/z$ is holomorphic. For any holomorphic $\phi$, the real derivative at $z$ is "multiply by the complex number $\phi'(z)$". Writing $\phi'(z) = p + iq$, multiplication by $p + iq$ on $\mathbb{R}^2 = \mathbb{C}$ is the matrix $\begin{pmatrix} p & -q \\ q & p \end{pmatrix}$. Compute $\phi'(z) = -1/z^2$ and put it in this matrix form; you should not need to differentiate the real and imaginary parts separately.

> [!note]- Hint 3
> Write $-1/z^2 = -\overline{z}^2/|z|^4$ (multiply top and bottom by $\overline{z}^2$). The factor $1/|z|^4$ has modulus $1/|z|^4$; pull out $1/|z|^2$ to leave a unit complex number. What is left, $-(\overline{z}/|z|)^2$, has modulus $1$, so it is a rotation. That is the polar decomposition $g_{12} = |z|^{-2} R$.

> [!note]- Hint 4
> To see the topology, restrict to the equator $|z| = 1$, so $z = e^{i\theta}$. Then $R = -(\overline{z}/|z|)^2 = -e^{-2i\theta}$. As $\theta$ runs $0 \to 2\pi$ (once around the equator), how many times does $-e^{-2i\theta}$ wind around $U(1)$? The constant $-1 = e^{i\pi}$ shifts the phase but does not change the winding; the winding is the coefficient of $\theta$ in the exponent.

---

# Solution

The plan is to reduce everything to differentiating $z \mapsto 1/z$. First the sphere relation forces the two stereographic coordinates to be reciprocals, $w = 1/z$. Because this map is holomorphic, its Jacobian is complex multiplication by $\phi'(z) = -1/z^2$, which we read off in matrix form and factor as conformal scalar times rotation. Normalising the coordinate frames to unit length reduces the structure group to $SO(2)$ and cancels the scalar, leaving a $U(1)$-valued transition whose winding number around the equator is $\mp 2$ — the Euler number of $S^2$.

**Step 1: The chart change is $\phi(z) = 1/z$.**

The sphere relation makes the two stereographic coordinates reciprocal.

> [!note]- Derivation
> **Multiply the two coordinates.** For $\xi \in U_{12}$ write $z = \varphi_1(\xi) = \tfrac{\xi_1 + i\xi_2}{1 - \xi_3}$ and $w = \varphi_2(\xi) = \tfrac{\xi_1 - i\xi_2}{1 + \xi_3}$. Then
> $$z \cdot w = \frac{(\xi_1 + i\xi_2)(\xi_1 - i\xi_2)}{(1 - \xi_3)(1 + \xi_3)} = \frac{\xi_1^2 + \xi_2^2}{1 - \xi_3^2} \qquad (\text{product of conjugate numerators; difference of squares in the denominator}).$$
> By the sphere relation $\xi_1^2 + \xi_2^2 + \xi_3^2 = 1$, the numerator equals $1 - \xi_3^2$, which is the denominator, so
> $$z \cdot w = \frac{1 - \xi_3^2}{1 - \xi_3^2} = 1 \qquad (\text{using } \xi_1^2 + \xi_2^2 = 1 - \xi_3^2).$$
> Hence $w = 1/z$, i.e. $\phi(z) = \varphi_2 \circ \varphi_1^{-1}(z) = 1/z$ on $\mathbb{C}^\times$ (on $U_{12}$ neither pole is present, so $\xi_3 \neq \pm 1$ and $z \neq 0, \infty$). This is a diffeomorphism of $\mathbb{C}^\times$, holomorphic and with holomorphic inverse (it is its own inverse).

**Step 2: The transition function is the Jacobian $g_{12}(z) = D\phi_z$.**

By the frame-bundle/vector-bundle cocycle identity, $g_{12}$ is the real Jacobian of $\phi$, which we compute in two ways.

> [!note]- Derivation
> **Reduce to a Jacobian.** By [[Def - Transition Function of a Vector Bundle|the vector-bundle cocycle identity]], the coordinate frames satisfy $e^{(1)} = e^{(2)} \cdot g_{12}$ with $g_{12}$ the Jacobian matrix of the coordinate change $\phi = \varphi_2 \circ \varphi_1^{-1}$: the coordinate vector fields transform by the chain rule, $\partial_{x_1^i} = \sum_j \tfrac{\partial x_2^j}{\partial x_1^i} \partial_{x_2^j}$, whose coefficient matrix (rows indexed by the output coordinate $x_2^j$, columns by the input $x_1^i$) is $D\phi$. So $g_{12}(z) = D\phi_z$.
>
> **Compute $D\phi$ by real partial derivatives.** Write $\phi(z) = 1/z = \overline{z}/|z|^2 = \tfrac{x - iy}{x^2 + y^2}$, so $\phi = (u, v)$ with
> $$u(x, y) = \frac{x}{x^2 + y^2}, \qquad v(x, y) = \frac{-y}{x^2 + y^2}, \qquad r^2 := x^2 + y^2.$$
> Differentiating (quotient rule, $\partial_x r^2 = 2x$, $\partial_y r^2 = 2y$):
> $$u_x = \frac{(x^2 + y^2) - x(2x)}{r^4} = \frac{y^2 - x^2}{r^4}, \qquad u_y = \frac{-x(2y)}{r^4} = \frac{-2xy}{r^4} \qquad (\text{quotient rule on } u),$$
> $$v_x = -y \cdot \frac{-2x}{r^4} = \frac{2xy}{r^4}, \qquad v_y = \frac{-(x^2 + y^2) - (-y)(2y)}{r^4} = \frac{y^2 - x^2}{r^4} \qquad (\text{quotient rule on } v).$$
> Assembling $D\phi = \begin{pmatrix} u_x & u_y \\ v_x & v_y \end{pmatrix}$,
> $$g_{12}(z) = \frac{1}{|z|^4} \begin{pmatrix} y^2 - x^2 & -2xy \\ 2xy & y^2 - x^2 \end{pmatrix} \qquad (r^2 = |z|^2, \text{ so } r^4 = |z|^4).$$
> This is claim 1.

**Step 3: $g_{12}$ is complex multiplication by $-1/z^2$, hence conformal factor times rotation.**

The matrix has the special form $\begin{pmatrix} p & -q \\ q & p \end{pmatrix}$, so it is multiplication by $p + iq = -1/z^2$; factoring out the modulus gives $|z|^{-2} R(z)$ with $R \in SO(2)$.

> [!note]- Derivation
> **Match to complex multiplication.** A real $2 \times 2$ matrix of the form $\begin{pmatrix} p & -q \\ q & p \end{pmatrix}$ acts on $\mathbb{R}^2 = \mathbb{C}$ as multiplication by the complex number $p + iq$ (this is the standard embedding $\mathbb{C} \hookrightarrow M_2(\mathbb{R})$). Our matrix has $p = \tfrac{y^2 - x^2}{|z|^4}$ and $q = \tfrac{2xy}{|z|^4}$, so
> $$p + iq = \frac{(y^2 - x^2) + 2ixy}{|z|^4} = \frac{-\big((x^2 - y^2) - 2ixy\big)}{|z|^4} = \frac{-\overline{z}^2}{|z|^4} \qquad (\text{since } \overline{z}^2 = (x - iy)^2 = (x^2 - y^2) - 2ixy).$$
> Because $\tfrac{-\overline{z}^2}{|z|^4} = \tfrac{-\overline{z}^2}{(\overline{z} z)^2} = \tfrac{-1}{z^2}$, we recover $g_{12}(z) = $ multiplication by $\phi'(z) = -1/z^2$, exactly the derivative of $\phi(z) = 1/z$. This confirms the holomorphic shortcut: for holomorphic $\phi$, $D\phi_z$ is multiplication by $\phi'(z)$.
>
> **Polar decomposition.** Factor the modulus out of $\phi'(z) = -\overline{z}^2/|z|^4$:
> $$g_{12}(z) = \frac{-\overline{z}^2}{|z|^4} = \frac{1}{|z|^2} \cdot \left(\frac{-\overline{z}^2}{|z|^2}\right) = |z|^{-2} \, R(z), \qquad R(z) := -\left(\frac{\overline{z}}{|z|}\right)^2 \qquad (\text{split off the positive scalar } |z|^{-2}).$$
> Here $R(z)$ is a unit complex number, $|R(z)| = \big|{-1}\big| \cdot \big(\tfrac{|\overline{z}|}{|z|}\big)^2 = 1$, hence a rotation: as a matrix $R(z) \in SO(2)$. Writing $z = |z| e^{i\theta}$ gives $R(z) = -e^{-2i\theta} = e^{i(\pi - 2\theta)}$, the rotation by angle $\pi - 2\theta$. Finally
> $$\det g_{12}(z) = \det\!\big(|z|^{-2} R\big) = (|z|^{-2})^2 \det R = |z|^{-4} > 0 \qquad (\det R = 1 \text{ for } R \in SO(2)),$$
> which also equals $|\phi'(z)|^2 = |{-1/z^2}|^2 = 1/|z|^4$, the general fact that a holomorphic map's real Jacobian determinant is $|\phi'|^2$. Positivity of the determinant says the two coordinate frames induce the *same* orientation — the atlas is oriented, as promised.

**Step 4: Reduction to $SO(2) = U(1)$ absorbs the conformal factor.**

Normalising the coordinate frames against the round metric cancels the scalar $|z|^{-2}$, leaving the $U(1)$-valued transition $\widehat{g}_{12} = R$.

> [!note]- Derivation
> **The round metric in each chart.** The round metric of $S^2$ pulled back to the stereographic chart $z$ is conformal to the flat metric,
> $$ds^2 = \Lambda_1(z)^2 \, |dz|^2, \qquad \Lambda_1(z) = \frac{2}{1 + |z|^2},$$
> and identically $ds^2 = \Lambda_2(w)^2 |dw|^2$ with $\Lambda_2(w) = \tfrac{2}{1 + |w|^2}$ in the chart $w$. The coordinate frame $e^{(1)} = (\partial_{x_1}, \partial_{y_1})$ is orthogonal with each vector of length $\Lambda_1$, so the orthonormal frame is $\widehat{e}^{(1)} = \Lambda_1^{-1} e^{(1)}$, and likewise $\widehat{e}^{(2)} = \Lambda_2^{-1} e^{(2)}$.
>
> **The scalar is the ratio of conformal factors.** With $w = 1/z$, so $|w|^2 = 1/|z|^2$,
> $$\Lambda_2(w) = \frac{2}{1 + |1/z|^2} = \frac{2 |z|^2}{|z|^2 + 1}, \qquad \frac{\Lambda_2(w)}{\Lambda_1(z)} = \frac{2|z|^2/(|z|^2 + 1)}{2/(1 + |z|^2)} = |z|^{2} \qquad (\text{cancel } 1 + |z|^2).$$
> **Cancel it in the reduced cocycle.** Substitute $e^{(i)} = \Lambda_i \widehat{e}^{(i)}$ into the coordinate-frame relation $e^{(1)} = e^{(2)} g_{12}$ from Step 2:
> $$\Lambda_1 \widehat{e}^{(1)} = \Lambda_2 \widehat{e}^{(2)} g_{12} \quad\Longrightarrow\quad \widehat{e}^{(1)} = \widehat{e}^{(2)} \cdot \big(\tfrac{\Lambda_2}{\Lambda_1} \, g_{12}\big) \qquad (\text{divide by the positive scalar } \Lambda_1; \text{ scalars commute with matrices}).$$
> The orthonormal-frame transition function $\widehat{g}_{12}$, defined by $\widehat{e}^{(1)} = \widehat{e}^{(2)} \widehat{g}_{12}$, is therefore
> $$\widehat{g}_{12} = \frac{\Lambda_2}{\Lambda_1} \, g_{12} = |z|^{2} \cdot \big(|z|^{-2} R\big) = R(z) \qquad (\tfrac{\Lambda_2}{\Lambda_1} = |z|^{2} \text{ exactly cancels the scalar } |z|^{-2} \text{ in } g_{12}),$$
> the positive conformal factor cancelling precisely because it is the frames' length ratio. This is the polar decomposition $g_{12} = (|z|^{-2} I)\, R$ with the positive scalar part scaled away, leaving
> $$\widehat{g}_{12}(z) = R(z) = -\left(\frac{\overline{z}}{|z|}\right)^2 \in SO(2) = U(1).$$
> Writing $z/|z| = e^{i\theta}$, we have $\overline{z}/|z| = e^{-i\theta}$, so $\widehat{g}_{12} = -e^{-2i\theta} = e^{i\pi}\big(\tfrac{z}{|z|}\big)^{-2}$. Up to the constant rotation $e^{i\pi} = -1$ (a global gauge rotation of one orthonormal frame, homotopically trivial), $\widehat{g}_{12} = \big(z/|z|\big)^{-2}$, i.e. $\big(z/|z|\big)^{\mp 2}$ after fixing the chart order and orientation. This is claim 3.

**Step 5: Winding number $\mp 2$ and the Euler number.**

The equatorial restriction of $\widehat{g}_{12}$ winds $\mp 2$ times, and this integer is $c_1(TS^2)[S^2] = 2$.

> [!note]- Derivation
> **Compute the winding number.** Restrict $\widehat{g}_{12}$ to the equator $\{|z| = 1\} = \{z = e^{i\theta} : \theta \in [0, 2\pi]\}$, a generating loop of $U_{12} \simeq S^1$:
> $$\gamma(\theta) := \widehat{g}_{12}(e^{i\theta}) = -\left(\frac{\overline{e^{i\theta}}}{1}\right)^2 = -e^{-2i\theta} = e^{i(\pi - 2\theta)} \qquad (\overline{e^{i\theta}} = e^{-i\theta}).$$
> By [[Def - Winding Number|the definition]], the winding number is the net change of the argument divided by $2\pi$:
> $$\operatorname{wind}(\gamma) = \frac{1}{2\pi}\int_0^{2\pi} \frac{d}{d\theta}\big(\pi - 2\theta\big)\, d\theta = \frac{1}{2\pi}\int_0^{2\pi} (-2)\, d\theta = \frac{1}{2\pi}(-2)(2\pi) = -2 \qquad (\arg \gamma = \pi - 2\theta).$$
> The additive constant $\pi$ drops out under differentiation, confirming that the global rotation $-1$ is topologically invisible. With the opposite chart ordering ($g_{21} = g_{12}^{-1}$, rotation $R^{-1}$) the winding is $+2$; either way the magnitude is $2$. By [[Thm - Pi_1 of S^1 is Z|the isomorphism $\pi_1(S^1) \cong \mathbb{Z}$]], this winding number is a complete homotopy invariant of the loop $\gamma$, so no change of frames can remove it.
>
> **Identification with the Euler / first Chern number.** For an oriented rank-$2$ real bundle over a closed oriented surface, covered by two charts whose overlap deformation-retracts onto the equator, the Euler number is the winding number of the $SO(2)$-transition function around that equator (this is the clutching description; the two charts play the roles of the northern and southern discs). Orienting $S^2$ by its complex structure, so that $TS^2 \cong \mathcal{O}(2)$ as a complex line bundle over $\mathbb{CP}^1$, fixes the sign to $+2$, and
> $$c_1(TS^2)[S^2] = e(TS^2)[S^2] = \operatorname{wind}\big(\widehat{g}_{12}\big|_{\text{equator}}\big) = 2 = \chi(S^2).$$
> The equality $c_1 = e$ for a complex line bundle, and the computation of $c_1$ by a curvature integral $\tfrac{i}{2\pi}\int_{S^2} F$, are proved in chapter VI (**[[Thm - First Chern Class of a Line Bundle from Curvature]]**, **[[Def - Euler Class of an Oriented Vector Bundle]]**); here the *same* integer $2$ has been obtained purely from the transition cocycle, with no connection or curvature, foreshadowing that agreement.

> [!note]- Complete formal solution
> **Claim.** With the orientation-compatible stereographic charts $\varphi_1(\xi) = \tfrac{\xi_1 + i\xi_2}{1 - \xi_3}$ and $\varphi_2(\xi) = \tfrac{\xi_1 - i\xi_2}{1 + \xi_3}$, the change of coordinates is $\phi(z) = 1/z$; the frame-bundle transition function is $g_{12}(z) = \tfrac{1}{|z|^4}\big(\begin{smallmatrix} y^2 - x^2 & -2xy \\ 2xy & y^2 - x^2 \end{smallmatrix}\big) = |z|^{-2} R(z)$ with $R(z) = -(\overline{z}/|z|)^2 \in SO(2)$ and $\det g_{12} = |z|^{-4} > 0$; the orthonormal-frame transition is $\widehat{g}_{12} = R(z) = (z/|z|)^{\mp 2}$ up to a constant rotation, with equatorial winding number $\mp 2$; and $c_1(TS^2)[S^2] = 2$.
>
> *Proof.* For $\xi \in U_{12}$, $z \varphi_2(\xi) = \tfrac{(\xi_1 + i\xi_2)(\xi_1 - i\xi_2)}{(1 - \xi_3)(1 + \xi_3)} = \tfrac{\xi_1^2 + \xi_2^2}{1 - \xi_3^2} = 1$ by $\xi_1^2 + \xi_2^2 + \xi_3^2 = 1$; hence $\phi(z) = 1/z$. By the vector-bundle cocycle identity for coordinate frames, $g_{12} = D\phi$. Writing $1/z = \tfrac{x - iy}{x^2 + y^2}$ and differentiating gives $g_{12}(z) = \tfrac{1}{|z|^4}\big(\begin{smallmatrix} y^2 - x^2 & -2xy \\ 2xy & y^2 - x^2 \end{smallmatrix}\big)$. This matrix has the form $\big(\begin{smallmatrix} p & -q \\ q & p \end{smallmatrix}\big)$ with $p + iq = \tfrac{(y^2 - x^2) + 2ixy}{|z|^4} = \tfrac{-\overline{z}^2}{|z|^4} = -1/z^2 = \phi'(z)$, so $g_{12}$ is multiplication by $-1/z^2$ and factors as $|z|^{-2} R(z)$, $R(z) = -(\overline{z}/|z|)^2$, $|R| = 1$, $R \in SO(2)$; then $\det g_{12} = |z|^{-4} > 0$. The round metric is $\Lambda_i^2 |dz_i|^2$ with $\Lambda_1(z) = \tfrac{2}{1 + |z|^2}$ and $\Lambda_2(1/z) = \tfrac{2|z|^2}{1 + |z|^2}$, so the frame-length ratio $\Lambda_2/\Lambda_1 = |z|^2$ cancels the $|z|^{-2}$ upon normalising: the orthonormal transition is the rotation part $\widehat{g}_{12} = R(z) = -(\overline{z}/|z|)^2$, equal to $(z/|z|)^{-2}$ up to the constant $-1$. On the equator $z = e^{i\theta}$, $\widehat{g}_{12} = -e^{-2i\theta} = e^{i(\pi - 2\theta)}$, whose argument changes by $-4\pi$ as $\theta: 0 \to 2\pi$, giving winding number $-2$ (and $+2$ for the reverse ordering); by $\pi_1(S^1) \cong \mathbb{Z}$ this is a homotopy invariant. By the clutching description of the Euler number of an oriented plane bundle over $S^2$ and the complex orientation $TS^2 \cong \mathcal{O}(2)$, this equals $c_1(TS^2)[S^2] = e(TS^2)[S^2] = 2 = \chi(S^2)$. $\blacksquare$

> [!warning] Illegal but tempting: the naive south-pole chart reverses orientation
> The seductive shortcut is to define the second chart by the *same* formula as the first, $\varphi_2^{\text{naive}}(\xi) = \tfrac{\xi_1 + i\xi_2}{1 + \xi_3}$ (no conjugating sign). Then $z \cdot \overline{\varphi_2^{\text{naive}}} = \tfrac{(\xi_1 + i\xi_2)(\xi_1 - i\xi_2)}{(1 - \xi_3)(1 + \xi_3)} = 1$, so $\varphi_2^{\text{naive}} = 1/\overline{z}$: the transition is the *antiholomorphic* map $z \mapsto 1/\overline{z}$, whose real Jacobian is complex-*conjugate*-linear with $\det = -1/|z|^4 < 0$. The two coordinate frames then induce *opposite* orientations, so the atlas is not oriented and $\operatorname{Fr}(TS^2)$ does not reduce to $GL_2^+(\mathbb{R})$, let alone $SO(2)$, in a globally consistent way; one cannot even speak of a single winding number. The extra condition that makes the reduction legal is precisely the conjugating sign in $\varphi_2$, which renders the transition holomorphic ($\det > 0$) and the atlas oriented. This is why orientation-compatibility is a hypothesis of the problem and not a cosmetic choice.

---

# Key Takeaways

**A holomorphic chart change turns a Jacobian into a single complex derivative, and hands you the conformal-plus-rotation structure for free.** The real Jacobian of a smooth map $\mathbb{R}^2 \to \mathbb{R}^2$ is a general $2 \times 2$ matrix with four independent entries. But the moment the map is holomorphic, the Cauchy–Riemann equations force the Jacobian into the two-parameter family $\begin{pmatrix} p & -q \\ q & p \end{pmatrix}$ — multiplication by the single complex number $\phi'(z) = p + iq$ — which is automatically a positive scalar times a rotation, with determinant $|\phi'(z)|^2 \ge 0$. The transferable diagnostic: whenever a transition function, a coordinate change, or a symmetry is holomorphic, do not compute four partial derivatives; write the complex derivative and read off (i) the conformal factor $|\phi'|$, (ii) the rotation $\phi'/|\phi'|$, and (iii) orientation-preservation $\det = |\phi'|^2 > 0$. This is exactly the computation that makes every oriented surface's tangent bundle a *complex line bundle*, and it is why the language of $\mathbb{CP}^1$, $\mathcal{O}(k)$, and winding numbers governs surface topology.

**Reducing the structure group to its maximal compact subgroup is where a bundle's topology becomes computable.** The full transition cocycle here, $g_{12} = |z|^{-2} R(z)$, takes values in $GL_2(\mathbb{R})$, and $GL_2^+(\mathbb{R})$ deformation-retracts onto $SO(2)$ — the positive scalar $|z|^{-2}$ and, more generally, the positive-definite symmetric part of any $GL^+$-valued cocycle can be continuously scaled away without changing the bundle. All of the topology survives in the $SO(2) = U(1)$-valued rotation part, whose winding number is a genuine homotopy invariant. The trigger condition is "an oriented vector bundle with a metric"; the reaction is "reduce $GL_n^+(\mathbb{R})$ to $O(n)$ (here $SO(2)$) by orthonormalising frames, then read the characteristic number off the compact-group-valued cocycle". The conformal factor being exactly the ratio of the two charts' metric conformal factors is not a coincidence: it is the statement that the *same* Riemannian metric, expressed in two charts, dictates how the coordinate frames must be rescaled, and this is what guarantees the scalar cancels cleanly.

**The winding number of the $SO(2)$-transition function is the Euler number, computed with no calculus of connections.** This exercise obtains the integer $2$ — the Euler characteristic of $S^2$, the first Chern number of $TS^2$, the self-intersection of the zero section — purely from a cocycle, by counting how many times a rotation-valued gluing map turns as one circles the overlap. Chapter VI will obtain the *same* integer by a completely different route: choosing a connection, computing its curvature $F$, and integrating $\tfrac{i}{2\pi}\int_{S^2} F = 2$ (**[[Thm - First Chern Class of a Line Bundle from Curvature]]**). That two such different computations — combinatorial gluing data versus a differential-geometric curvature integral — must agree is the content of Chern–Weil theory and the clutching-construction description of characteristic classes. The reusable principle for spaced practice: a characteristic number can be read *either* off the transition cocycle (winding / clutching degree) *or* off the curvature (Chern–Weil integral), and matching the two is both a powerful consistency check and the conceptual bridge between the topological and the geometric faces of gauge theory. The companion computation for the Hopf bundle, [[Ex - Explicit Local Sections and the Transition Function of the Hopf Bundle]], runs the same machinery on a $U(1)$-bundle and finds winding $\pm 1$; the doubling to $\pm 2$ here is exactly the passage from $\mathcal{O}(1)$ to $TS^2 \cong \mathcal{O}(2)$.
