---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Def - Smooth Action of a Lie Group"
  - "Thm - SO(2) is Isomorphic to U(1)"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $S^2 = \{x = (x_1, x_2, x_3) \in \mathbb{R}^3 : x_1^2 + x_2^2 + x_3^2 = 1\}$ be the unit sphere, and let $SO(2) = \left\{ \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix} : \varphi \in \mathbb{R} \right\}$ be the rotation group of the plane. Define an action of $SO(2)$ on $S^2$ by rotation about the $z$-axis,
$$g \cdot x := \begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix} x = \begin{pmatrix} g_{11} & g_{12} & 0 \\ g_{21} & g_{22} & 0 \\ 0 & 0 & 1 \end{pmatrix} x, \qquad g = \begin{pmatrix} g_{11} & g_{12} \\ g_{21} & g_{22} \end{pmatrix} \in SO(2),$$
so that $g$ rotates the first two coordinates and leaves the third fixed.

Prove the following.

1. The action is **effective** but **not free** and **not transitive**.
2. The orbit of a point $x \in S^2$ is the circle of latitude through $x$ (the poles being one-point orbits), and the orbit space $SO(2) \backslash S^2$ is homeomorphic to the closed interval $[-1, 1]$ through the map induced by the height function $x \mapsto x_3$. Observe that $[-1, 1]$ is a one-dimensional manifold *with boundary* and not a manifold in the boundaryless sense, and explain why this is consistent with the failure of freeness.
3. Compute the fundamental vector field $\bar{X}$ associated with a generator $X$ of the Lie algebra $\mathfrak{so}(2)$, verify that it is tangent to the circles of latitude, and identify its zero set.

**Recall:**

The objects in play are a smooth left action of a Lie group, the properties effective, free, and transitive, the orbit and orbit space of an action, and the fundamental vector field of an action.

![[Def - Free, Transitive, Effective, and Proper Group Actions#The Definition]]

A smooth left action of a Lie group $G$ on a manifold $M$ is a smooth map $G \times M \to M$, $(g, x) \mapsto g \cdot x$, with $(gh) \cdot x = g \cdot (h \cdot x)$ and $e \cdot x = x$. Writing $\theta_g(x) := g \cdot x$, each $\theta_g$ is a diffeomorphism of $M$ and $g \mapsto \theta_g$ is a group homomorphism $G \to \operatorname{Diff}(M)$. The action is **effective** if this homomorphism is injective, that is, if $\theta_g = \operatorname{id}_M$ forces $g = e$; it is **free** if $g \cdot x = x$ for some single $x$ already forces $g = e$; it is **transitive** if for every $x, y \in M$ there is a $g \in G$ with $g \cdot x = y$. The **orbit** of $x$ is $G \cdot x := \{g \cdot x : g \in G\}$, and the **orbit space** $G \backslash M := \{G \cdot x : x \in M\}$ carries the quotient topology under the projection $\pi : M \to G \backslash M$, $\pi(x) = G \cdot x$. Every free action is effective (provided $M \neq \varnothing$).

![[Def - Fundamental Vector Field of a Group Action#The Definition]]

For a smooth left action of $G$ on $M$ and $X \in \mathfrak{g} = T_e G$, the **fundamental vector field** $\bar{X} \in \mathfrak{X}(M)$ is
$$\bar{X}(p) := \left.\frac{d}{dt}\right|_{t=0} \exp(tX) \cdot p = d_e \ell_p(X), \qquad \ell_p(g) := g \cdot p,$$
the infinitesimal generator of the flow $t \mapsto \theta_{\exp(tX)}$. It vanishes at $p$ if and only if $\exp(tX) \cdot p = p$ for all $t \in \mathbb{R}$.

> [!warning] Convention: $SO(2)$ versus $U(1)$
> Bär states the effectiveness/freeness/transitivity computation for this action with the group written as $SO(2)$ (Example 1.5.7.1) and the orbit-space computation with the group written as $U(1)$ (Example 1.5.9). The two are the same group: the map $\begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix} \mapsto e^{i\varphi}$ is an isomorphism of Lie groups, both diffeomorphic to $S^1$ (see **[[Thm - SO(2) is Isomorphic to U(1)]]**). We work throughout with $SO(2)$ acting by the block matrix above; under the isomorphism the element $e^{i\varphi} \in U(1)$ acts by the rotation of angle $\varphi$ in the $(x_1, x_2)$-plane, so every statement below transfers verbatim to the $U(1)$ phrasing.

---

# Convergent Strategy

**Problem class.** This is a *classify-an-action* problem: given an explicit action, decide which of the three standard properties — effective, free, transitive — hold, and describe the orbit decomposition. Every part is settled by finding the right *invariant* of the action and reading the answer off it. The single organising observation is that rotation about the $z$-axis leaves the third coordinate $x_3$ fixed, and this one conserved quantity drives the whole solution.

**Assumption pattern.** The recognisable trigger is that the action is *linear and block-diagonal*: it acts by a fixed rotation on the $(x_1, x_2)$-plane and by the identity on the $x_3$-axis. Whenever an action fixes a subspace pointwise, that subspace meets the manifold in a set of *fixed points*, which is exactly where freeness must fail; and whenever a coordinate is preserved, that coordinate *separates orbits* and blocks transitivity. Recognising the block structure tells us in advance that the action will be neither free (the $z$-axis meets $S^2$ in the two poles) nor transitive (the height $x_3$ is conserved).

**Theorem routing.** For part 1 we use the definitions directly: effectiveness by demanding that a group element fixing *every* point be the identity; failure of freeness by exhibiting *one* point (a pole) with non-trivial stabiliser; failure of transitivity by the conserved height $x_3$. For part 2 we identify each orbit as a level set $\{x_3 = c\}$, then push the height function $h(x) = x_3$ through the quotient to a continuous bijection $\bar{h} : SO(2) \backslash S^2 \to [-1, 1]$, and upgrade it to a homeomorphism because $S^2$ is compact and $[-1, 1]$ is Hausdorff. For part 3 we differentiate the one-parameter subgroup $\exp(tX)$ acting on a point, using the formula on **[[Def - Fundamental Vector Field of a Group Action]]**, and then read the zero set off the criterion $\bar{X}(p) = 0 \iff \exp(tX) \cdot p = p$ for all $t$, which ties part 3 back to the fixed points found in part 1.

**Key decision point.** The one genuine decision is to *organise everything around the invariant $x_3$*. Once we notice that $g \cdot x$ never changes $x_3$, effectiveness, non-freeness, non-transitivity, the orbits, and the orbit space all follow with almost no computation: the poles $x_3 = \pm 1$ are exactly the fixed points, hence exactly where freeness fails and exactly where the fundamental vector field vanishes, and they are exactly the images that become the *boundary* $\{-1, 1\}$ of the interval. The conceptual payoff to carry away is that the boundary of the quotient is not an accident of the picture; it is the precise topological trace of the two points where the action is not free.

---

# Legal Operations Used

This solution deploys the following operations, to be reconciled with the numbered Legal Operations of the (not-yet-written) topic page for §1.5.

1. **Test effectiveness by a pointwise-fixing element.** To show the action is effective, take a $g \in SO(2)$ with $g \cdot x = x$ for *all* $x \in S^2$ and deduce $g = e$; equivalently, show the homomorphism $g \mapsto \theta_g$ into $\operatorname{Diff}(S^2)$ has trivial kernel.

2. **Refute freeness by an isolated non-trivial stabiliser.** To show the action is *not* free, exhibit a single point $p$ (here a pole) whose stabiliser $\{g : g \cdot p = p\}$ is strictly larger than $\{e\}$.

3. **Refute transitivity by a conserved quantity.** To show the action is *not* transitive, produce a continuous function $h : S^2 \to \mathbb{R}$ constant on orbits ($h(g \cdot x) = h(x)$) that takes different values at two points; those two points then cannot lie in one orbit.

4. **Realise orbits as level sets of the invariant.** Show that the orbit of $x$ equals the fibre $h^{-1}(h(x))$ of the conserved height, by proving both inclusions.

5. **Descend the invariant to the quotient and upgrade compact-to-Hausdorff.** Factor the invariant $h$ through the projection $\pi$ to a continuous bijection $\bar{h}$ on the orbit space, then invoke that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

6. **Compute the fundamental vector field by differentiating the one-parameter subgroup.** Use $\bar{X}(p) = \left.\frac{d}{dt}\right|_0 \exp(tX) \cdot p$, evaluate for the explicit matrix flow, and check tangency by pairing against the position vector.

7. **Read fixed points off the zero set of the fundamental vector field.** Use $\bar{X}(p) = 0 \iff \exp(tX) \cdot p = p$ for all $t$ to match the vanishing locus of $\bar{X}$ with the fixed-point set found in operation 2.

---

# Hints

> [!note]- Hint 1
> Rotation about the $z$-axis does not touch the third coordinate: for every $g \in SO(2)$ and every $x \in S^2$, the height $x_3$ is unchanged. Almost every part of the problem is a consequence of this one conserved quantity. Which points of $S^2$ have their *first two* coordinates equal to zero, and what does the action do to them?

> [!note]- Hint 2
> For effectiveness, a $g$ fixing all of $S^2$ in particular fixes the equatorial points $(1,0,0)$ and $(0,1,0)$; what rotation of the plane fixes two independent vectors? For non-freeness, look at the north pole $N = (0,0,1)$ and compute its stabiliser. For non-transitivity, use the conserved height to separate $N$ from a point on the equator.

> [!note]- Hint 3
> The orbit of $x$ is contained in the latitude set $\{y \in S^2 : y_3 = x_3\}$ because height is conserved; for the reverse inclusion, given two points at the same height write them in the form $(\sqrt{1 - c^2}\cos\varphi, \sqrt{1 - c^2}\sin\varphi, c)$ and rotate one angle into the other. The height function then induces a continuous bijection from the quotient onto $[-1, 1]$; compactness of $S^2$ makes it a homeomorphism.

> [!note]- Hint 4
> The Lie algebra $\mathfrak{so}(2)$ is spanned by $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. Embed it as $\hat{X} = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ acting on $\mathbb{R}^3$, so that $\exp(t\hat{X})$ is the rotation of angle $t$ about the $z$-axis. Differentiate $t \mapsto \exp(t\hat{X}) x$ at $t = 0$; the derivative is simply $\hat{X}x$. Where on $S^2$ does $\hat{X}x = 0$?

---

# Solution

The entire solution turns on one fact: the action preserves the height $x_3$. From it, effectiveness follows because a plane rotation fixing two independent equatorial vectors is trivial; non-freeness follows because the poles lie on the fixed $z$-axis; non-transitivity follows because height separates the poles from the equator; the orbits are the latitude circles (the level sets of the height); and the orbit space is the range $[-1, 1]$ of the height, with the poles becoming the two boundary points. The fundamental vector field is the infinitesimal rotation $(-x_2, x_1, 0)$, tangent to the latitude circles and vanishing exactly at the two poles — the same two points at which freeness failed.

**Step 1: The action is well defined and effective.**

Each $g \in SO(2)$ sends $S^2$ to itself, and the only element acting as the identity on all of $S^2$ is $g = e$.

> [!note]- Derivation
> **Well-definedness.** Write $\hat{g} := \begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix} \in SO(3)$, since $\det \hat{g} = \det g \cdot 1 = 1$ and $\hat{g}^t \hat{g} = \begin{pmatrix} g^t g & 0 \\ 0 & 1 \end{pmatrix} = 1_3$ (because $g \in SO(2)$ satisfies $g^t g = 1_2$). An orthogonal matrix preserves the Euclidean norm, so $|\hat{g} x| = |x| = 1$ for $x \in S^2$; hence $g \cdot x = \hat{g} x \in S^2$, and the action is a well-defined map $SO(2) \times S^2 \to S^2$. It is smooth because it is the restriction of the bilinear matrix–vector multiplication, and it satisfies $(gh) \cdot x = \widehat{gh}\, x = \hat{g}\hat{h}x = g \cdot (h \cdot x)$ and $e \cdot x = 1_3 x = x$; it is therefore a smooth left action in the sense of **[[Def - Smooth Action of a Lie Group]]**.
>
> **Effectiveness.** Suppose $g \in SO(2)$ satisfies $g \cdot x = x$ for every $x \in S^2$. Apply this to the two equatorial points $e_1 = (1, 0, 0)$ and $e_2 = (0, 1, 0)$, both of which lie on $S^2$. Then $\hat{g} e_1 = e_1$ and $\hat{g} e_2 = e_2$, which read on the first two coordinates say $g \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $g \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ (since the third coordinate is fixed automatically). Thus the linear map $g$ fixes the two independent vectors $\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, so $g = 1_2$ (a linear map fixing a basis is the identity), i.e. $g = e$. Therefore the kernel of $g \mapsto \theta_g$ is trivial and the action is **effective**.

**Step 2: The action is not free and not transitive.**

The north pole is fixed by every rotation, so its stabiliser is all of $SO(2)$; and the conserved height keeps the north pole and an equatorial point in different orbits.

> [!note]- Derivation
> **Not free.** Let $N = (0, 0, 1) \in S^2$ be the north pole. For any $g \in SO(2)$,
> $$g \cdot N = \begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = N \qquad \text{(the first two entries of $N$ are zero, and the last is fixed).}$$
> Hence the stabiliser of $N$ is the whole group $SO(2) \neq \{e\}$. A single point with a non-trivial stabiliser refutes freeness (by the definition on **[[Def - Free, Transitive, Effective, and Proper Group Actions|the free/effective/transitive definition]]**, a free action would force any $g$ with a fixed point to equal $e$). So the action is **not free**. The south pole $S = (0, 0, -1)$ is fixed for the same reason.
>
> **Not transitive.** The height function $h : S^2 \to \mathbb{R}$, $h(x) := x_3$, is constant on orbits: for every $g \in SO(2)$,
> $$h(g \cdot x) = (\hat{g}x)_3 = x_3 = h(x) \qquad \text{(the third row of $\hat g$ is $(0,0,1)$).}$$
> Now $h(N) = 1$ while $h(e_1) = 0$ for the equatorial point $e_1 = (1, 0, 0)$. If some $g$ had $g \cdot e_1 = N$, then $h(N) = h(g \cdot e_1) = h(e_1)$, i.e. $1 = 0$, a contradiction. Hence no group element carries $e_1$ to $N$, and the action is **not transitive**. (This is consistent with the general fact that every free action is effective but a merely effective action, such as this one, need not be free.)

**Step 3: The orbits are the circles of latitude.**

For $x \in S^2$ with $x_3 = c$, the orbit $SO(2) \cdot x$ equals the latitude set $L_c := \{y \in S^2 : y_3 = c\}$.

> [!note]- Derivation
> Fix $x \in S^2$ and set $c := x_3 \in [-1, 1]$.
>
> **Inclusion $SO(2) \cdot x \subseteq L_c$.** For every $g$, $(g \cdot x)_3 = x_3 = c$ by the height computation of Step 2, so $g \cdot x \in L_c$.
>
> **Inclusion $L_c \subseteq SO(2) \cdot x$.** Let $y \in L_c$, so $y_3 = c = x_3$. Because $x, y \in S^2$, the planar parts satisfy $x_1^2 + x_2^2 = 1 - c^2 = y_1^2 + y_2^2 =: \rho^2$ with $\rho = \sqrt{1 - c^2} \geq 0$. If $\rho = 0$ (that is, $c = \pm 1$), then $x = y = (0, 0, c)$ and $y = e \cdot x$. If $\rho > 0$, write the planar parts in polar form,
> $$(x_1, x_2) = \rho(\cos\alpha, \sin\alpha), \qquad (y_1, y_2) = \rho(\cos\beta, \sin\beta),$$
> for angles $\alpha, \beta \in \mathbb{R}$. Let $g_\varphi := \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}$ with $\varphi := \beta - \alpha$. Then, by the addition theorems for sine and cosine,
> $$g_\varphi \begin{pmatrix} \rho\cos\alpha \\ \rho\sin\alpha \end{pmatrix} = \rho \begin{pmatrix} \cos\varphi\cos\alpha - \sin\varphi\sin\alpha \\ \sin\varphi\cos\alpha + \cos\varphi\sin\alpha \end{pmatrix} = \rho \begin{pmatrix} \cos(\varphi + \alpha) \\ \sin(\varphi + \alpha) \end{pmatrix} = \rho \begin{pmatrix} \cos\beta \\ \sin\beta \end{pmatrix} \qquad \text{(since $\varphi + \alpha = \beta$).}$$
> Therefore $g_\varphi \cdot x = (y_1, y_2, c) = y$, so $y \in SO(2) \cdot x$.
>
> Combining the two inclusions, $SO(2) \cdot x = L_c$. For $c \in (-1, 1)$ this is a genuine circle of radius $\rho = \sqrt{1 - c^2} > 0$; for $c = \pm 1$ it degenerates to the single pole $(0, 0, \pm 1)$, an orbit consisting of one fixed point.

**Step 4: The orbit space is homeomorphic to $[-1, 1]$.**

The height function induces a homeomorphism $\bar{h} : SO(2) \backslash S^2 \to [-1, 1]$.

> [!note]- Derivation
> The height $h : S^2 \to [-1, 1]$, $h(x) = x_3$, is continuous, surjective (for $c \in [-1, 1]$ the point $(\sqrt{1 - c^2}, 0, c)$ has height $c$), and constant on orbits (Step 2). By the universal property of the quotient topology on $SO(2) \backslash S^2$, there is a unique continuous map $\bar{h} : SO(2) \backslash S^2 \to [-1, 1]$ with $\bar{h} \circ \pi = h$, where $\pi(x) = SO(2) \cdot x$ is the projection.
>
> **$\bar{h}$ is a bijection.** It is surjective because $h$ is. It is injective because two orbits with the same height coincide: if $\bar{h}(SO(2) \cdot x) = \bar{h}(SO(2) \cdot y)$, then $x_3 = y_3 =: c$, so by Step 3 both orbits equal the same latitude set $L_c$, hence $SO(2) \cdot x = SO(2) \cdot y$.
>
> **$\bar{h}$ is a homeomorphism.** The sphere $S^2$ is compact and $\pi$ is continuous and surjective, so the quotient $SO(2) \backslash S^2 = \pi(S^2)$ is compact. The target $[-1, 1]$ is Hausdorff. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism (it is a closed map: it sends closed, hence compact, sets to compact, hence closed, sets, so its inverse is continuous). Therefore $\bar{h}$ is a homeomorphism and
> $$SO(2) \backslash S^2 \;\cong\; [-1, 1].$$
>
> **Why the quotient has a boundary.** The interval $[-1, 1]$ is a one-dimensional smooth manifold *with boundary*, its boundary being the two endpoints $\{-1, 1\}$; no neighbourhood of $\pm 1$ in $[-1, 1]$ is homeomorphic to an open interval of $\mathbb{R}$, so $[-1, 1]$ is not a manifold in the boundaryless sense. The two boundary points are exactly the images $\bar{h}^{-1}(\pm 1) = \pi(\text{poles})$ of the north and south poles — the two points where the action fails to be free (Step 2). The quotient-manifold theorem for free and proper actions (see **[[Thm - Quotient Manifold Theorem for Free Proper Actions]]**: a smooth, free, and proper action of $G$ on $M$ makes $G \backslash M$ a smooth boundaryless manifold of dimension $\dim M - \dim G$) does not apply here, because although the action is proper — $SO(2)$ is compact — it is *not* free. The dimension count $\dim M - \dim G = 2 - 1 = 1$ still predicts a one-dimensional quotient, and indeed the quotient is one-dimensional; but the hypothesis of freeness, which is precisely what fails at the poles, is exactly what would have been needed to rule out boundary points. The failure of freeness at two points thus leaves its topological trace as the two-point boundary of the interval.

**Step 5: The fundamental vector field.**

For the generator $X = J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ of $\mathfrak{so}(2)$, the fundamental vector field is $\bar{X}(x) = (-x_2, x_1, 0)$; it is tangent to the circles of latitude and vanishes exactly at the two poles.

> [!note]- Derivation
> The Lie algebra of $SO(2)$ is $\mathfrak{so}(2) = \{A \in \operatorname{Mat}(2 \times 2; \mathbb{R}) : A^t + A = 0\} = \mathbb{R} \cdot J$ with $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$; take the generator $X := J$. Under the block embedding used by the action, $X$ acts on $\mathbb{R}^3$ through
> $$\hat{X} := \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \in \mathfrak{so}(3), \qquad \exp(t\hat{X}) = \begin{pmatrix} \cos t & -\sin t & 0 \\ \sin t & \cos t & 0 \\ 0 & 0 & 1 \end{pmatrix},$$
> where the exponential is computed from $\exp(tJ) = \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix}$ (the standard planar-rotation exponential) placed in the upper-left block, the last row and column contributing $\exp(0) = 1$. This one-parameter subgroup $\exp(t\hat{X})$ is exactly the rotation of angle $t$ about the $z$-axis, so its action on $S^2$ is $\theta_{\exp(tX)}(x) = \exp(t\hat{X}) x$.
>
> **The vector field.** By the formula on **[[Def - Fundamental Vector Field of a Group Action|the fundamental-vector-field definition]]**, $\bar{X}(x) = \left.\frac{d}{dt}\right|_{t=0} \exp(tX) \cdot x = \left.\frac{d}{dt}\right|_{t=0} \exp(t\hat{X}) x = \hat{X} x$ (differentiating the linear map $x \mapsto \exp(t\hat{X})x$ at $t = 0$ gives $\hat{X}x$, since $\left.\frac{d}{dt}\right|_0 \exp(t\hat{X}) = \hat{X}$). Explicitly,
> $$\bar{X}(x) = \hat{X}\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} -x_2 \\ x_1 \\ 0 \end{pmatrix} = -x_2 \,\partial_{x_1} + x_1 \,\partial_{x_2}.$$
>
> **Tangency to $S^2$ and to the latitude circles.** The vector $\bar{X}(x)$ is tangent to $S^2$ at $x$ because it is orthogonal to the position vector:
> $$\langle \bar{X}(x), x \rangle = (-x_2)x_1 + x_1 x_2 + 0 \cdot x_3 = 0,$$
> so $\bar{X}(x) \in T_x S^2 = x^{\perp}$. It is moreover tangent to the circle of latitude through $x$, since its third component is zero, so it annihilates the height function: $\bar{X}(x)[h] = \langle \bar{X}(x), \nabla h \rangle = (\bar{X}(x))_3 = 0$. Concretely, on the latitude $L_c$ (for $c \in (-1, 1)$) parametrised by $\gamma(\varphi) = (\sqrt{1 - c^2}\cos\varphi, \sqrt{1 - c^2}\sin\varphi, c)$ we have $\gamma'(\varphi) = (-\sqrt{1 - c^2}\sin\varphi, \sqrt{1 - c^2}\cos\varphi, 0) = (-\gamma_2, \gamma_1, 0) = \bar{X}(\gamma(\varphi))$, so $\bar{X}$ is exactly the velocity field $\partial_\varphi$ of the latitude circles — it generates the rotation.
>
> **Zero set.** From $\bar{X}(x) = (-x_2, x_1, 0)$ we read $\bar{X}(x) = 0 \iff x_1 = x_2 = 0 \iff x = (0, 0, \pm 1)$, the two poles. This matches the general criterion (Bär's Remark 1.5.19, restated on **[[Def - Fundamental Vector Field of a Group Action]]**) that $\bar{X}(p) = 0$ if and only if $\exp(tX) \cdot p = p$ for all $t$: the poles are precisely the points fixed by every rotation about the $z$-axis, i.e. the points at which the action failed to be free in Step 2. The fundamental vector field thus vanishes exactly on the fixed-point set.

> [!note]- Complete formal solution
> **Claim.** The action of $SO(2)$ on $S^2$ by rotation about the $z$-axis is effective, not free, and not transitive; its orbits are the circles of latitude with the poles as one-point orbits; the orbit space is homeomorphic to $[-1, 1]$ via the height; and the fundamental vector field of $X = J \in \mathfrak{so}(2)$ is $\bar{X}(x) = (-x_2, x_1, 0)$, tangent to the latitude circles and vanishing exactly at the poles.
>
> Write $\hat{g} = \begin{pmatrix} g & 0 \\ 0 & 1 \end{pmatrix} \in SO(3)$ for $g \in SO(2)$; then $g \cdot x = \hat{g}x$ preserves $|x|$ and the height $x_3$, and defines a smooth left action.
>
> *Effective.* If $g \cdot x = x$ for all $x \in S^2$, then $\hat g$ fixes $e_1, e_2$, so $g$ fixes the standard basis of $\mathbb{R}^2$, whence $g = 1_2 = e$.
>
> *Not free.* Every $g$ fixes $N = (0,0,1)$, since $\hat g N = N$; so the stabiliser of $N$ is $SO(2) \neq \{e\}$.
>
> *Not transitive.* The height $h(x) = x_3$ satisfies $h(g \cdot x) = h(x)$, and $h(N) = 1 \neq 0 = h(e_1)$, so no $g$ sends $e_1$ to $N$.
>
> *Orbits.* For $x$ with $x_3 = c$, height-invariance gives $SO(2) \cdot x \subseteq L_c := \{y \in S^2 : y_3 = c\}$; conversely, two points of $L_c$ have planar parts of equal length $\sqrt{1 - c^2}$ and differ by a planar rotation $g_{\beta - \alpha}$, so $L_c \subseteq SO(2) \cdot x$. Thus $SO(2) \cdot x = L_c$: a circle for $c \in (-1, 1)$, a single pole for $c = \pm 1$.
>
> *Orbit space.* The continuous, surjective, orbit-constant map $h$ descends to a continuous bijection $\bar{h} : SO(2) \backslash S^2 \to [-1, 1]$ (injective because equal heights give equal latitude orbits). As $SO(2)\backslash S^2$ is compact (continuous image of the compact $S^2$) and $[-1, 1]$ is Hausdorff, $\bar{h}$ is a homeomorphism. Here $[-1, 1]$ is a manifold with boundary $\{-1, 1\}$; the boundary points are the images of the two poles, exactly the points at which freeness fails, so the quotient-manifold theorem (which needs a free and proper action to give a boundaryless quotient) does not apply, even though $SO(2)$ is compact and the action is proper.
>
> *Fundamental vector field.* With $X = J \in \mathfrak{so}(2)$ embedded as $\hat X = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, we have $\exp(t\hat X)$ the rotation of angle $t$ about the $z$-axis, so $\bar{X}(x) = \left.\frac{d}{dt}\right|_0 \exp(t\hat X)x = \hat X x = (-x_2, x_1, 0)$. Then $\langle \bar{X}(x), x \rangle = 0$ (tangent to $S^2$) and $(\bar{X}(x))_3 = 0$ (tangent to the latitude circles, indeed $\bar{X} = \partial_\varphi$ along them), and $\bar{X}(x) = 0 \iff x_1 = x_2 = 0 \iff x = (0,0,\pm 1)$, the poles — the fixed-point set, consistent with $\bar{X}(p) = 0 \iff \exp(tX)\cdot p = p\ \forall t$. $\blacksquare$

> [!warning] Illegal but tempting: "compact group acting properly, so the quotient is a manifold"
> It is true that a compact Lie group acts properly on any manifold, and one might be tempted to conclude from properness alone that $SO(2) \backslash S^2$ is a smooth boundaryless manifold. This is wrong: the quotient-manifold theorem requires the action to be *both* proper *and* free, and here freeness fails at the two poles. The resulting quotient $[-1, 1]$ is a manifold with boundary, not a boundaryless manifold. The extra condition that would restore the conclusion is exactly freeness — remove the poles and $SO(2)$ acts freely and properly on the open cylinder $S^2 \setminus \{N, S\}$, whose quotient is the boundaryless open interval $(-1, 1)$.

---

# Key Takeaways

**One conserved coordinate settles an entire action-classification problem.** The whole of this exercise is powered by the observation that rotation about the $z$-axis preserves the height $x_3$. A quantity that is constant on orbits does three jobs at once: it *blocks transitivity* (points of different height cannot be joined), it *labels the orbits* (each orbit lies in a single level set, and here fills it), and it *is* the orbit space (the range of the invariant, once we check the induced map is a homeomorphism). The reusable diagnostic is: when you meet an explicit action, first hunt for an invariant — a function $h$ with $h(g \cdot x) = h(x)$. If you find one that separates points, transitivity is dead; if its level sets are single orbits, you have simultaneously found the orbits and a model for the quotient. The trigger to look for an invariant is any action that fixes a subspace, preserves a norm, or commutes with a projection.

**Freeness is a *pointwise* condition, and its failure is visible as fixed points and as zeros of fundamental vector fields.** Effectiveness asks a global question — does any non-identity element move *nothing*? — whereas freeness asks a local one — does any non-identity element fix *even one point*? This is why the poles refute freeness but not effectiveness: they are fixed by the whole group, yet no single non-identity rotation fixes the entire sphere. The same fixed points reappear as the zeros of the fundamental vector field $\bar{X}$, because $\bar{X}(p) = 0$ exactly when the one-parameter subgroup through $X$ fixes $p$. The transferable pattern: to test freeness, compute stabilisers and look for a point with a large one; equivalently, compute the fundamental fields and look for common zeros. A positive-dimensional group acts freely only if every non-zero generator's fundamental field is nowhere vanishing — the obstruction that later forbids free circle actions on even spheres, since $S^{2n}$ carries no nowhere-vanishing vector field.

**The boundary of a quotient is the topological signature of where freeness fails.** The quotient-manifold theorem promises a *boundaryless* smooth manifold of dimension $\dim M - \dim G$ only when the action is free and proper; here the action is proper (the group is compact) but not free, and the two non-free points become exactly the two boundary points of $[-1, 1]$. The dimension count $2 - 1 = 1$ is still correct, but the quotient is a manifold with boundary rather than without. The lesson to carry into bundle theory is that properness is cheap for compact groups and controls *Hausdorffness and local compactness of the quotient*, while freeness is the delicate hypothesis that controls *smoothness and the absence of boundary or singular strata*. Whenever a quotient turns out to have corners, edges, or a boundary, look back for the orbits with non-trivial stabiliser — the "orbifold" points — and you will find them sitting under the singular locus. This exercise is the smallest complete instance of that phenomenon; the free case is treated in the companion exercise **[[Ex - The Scalar Action of U(1) on Odd Spheres is Free]]**, whose quotient $\mathbb{CP}^{n-1}$ is a genuine boundaryless manifold precisely because the scalar circle action there is free.
