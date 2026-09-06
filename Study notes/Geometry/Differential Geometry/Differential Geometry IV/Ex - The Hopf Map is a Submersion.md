---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Immersion, Submersion, and Embedding"
  - "Def - Rank of a Smooth Map"
  - "Def - The Differential of a Smooth Map"
  - "Thm - Local Submersion Theorem"
tags: [geometry, differential-geometry]
---

# Problem Statement

The **Hopf map** $h : S^3 \to S^2$ is one of the most important examples in topology and geometry. View $S^3 \subseteq \mathbb{C}^2$ as the unit sphere $\{(z, w) \in \mathbb{C}^2 : |z|^2 + |w|^2 = 1\}$, and $S^2 \cong \mathbb{CP}^1$ as the space of complex lines through the origin in $\mathbb{C}^2$. Define
$$h : S^3 \to \mathbb{CP}^1 \cong S^2, \quad h(z, w) = [z : w] \in \mathbb{CP}^1,$$
where $[z : w]$ is the line through $(z, w)$ — equivalently, the equivalence class of $(z, w)$ under the action $\lambda \cdot (z, w) = (\lambda z, \lambda w)$ for $\lambda \in S^1 \subseteq \mathbb{C}$.

Show that $h$ is a smooth submersion. Identify the fibres of $h$ as great circles in $S^3$.

**Recall:**

A smooth map $F : M \to N$ is a **submersion** at $p$ if $dF_p$ is surjective. By [[Thm - Local Submersion Theorem|the local submersion theorem]], a submersion is locally a coordinate projection.

Complex projective space $\mathbb{CP}^1 = (\mathbb{C}^2 \setminus \{0\})/\mathbb{C}^*$, where $\mathbb{C}^* = \mathbb{C} \setminus \{0\}$ acts by scalar multiplication. Equivalently, $\mathbb{CP}^1 \cong S^2$ via stereographic projection: a complex line $[z : w]$ corresponds to the point on $S^2$ obtained by intersecting the line with $S^3$ and projecting stereographically.

The standard explicit formula for the Hopf map in real coordinates: writing $(z, w) = (a + bi, c + di)$ with $a^2 + b^2 + c^2 + d^2 = 1$,
$$h(z, w) = (2(ac + bd),\, 2(bc - ad),\, a^2 + b^2 - c^2 - d^2) \in S^2 \subseteq \mathbb{R}^3.$$

---

# Convergent Strategy

**Problem class:** This is a verification exercise: show a specific smooth map is a submersion. The route is to compute the differential at each point and verify surjectivity. The Hopf map is special because (a) it is a fibre bundle (every fibre is $S^1$), and (b) its fibres are linked great circles, making it the simplest nontrivial fibre bundle.

**Assumption pattern:** The source $S^3$ has [[Def - Dimension|dimension]] $3$, the target $S^2$ has dimension $2$. So at each point of $S^3$, the differential $dh_p : T_p S^3 \to T_{h(p)} S^2$ is a linear map between a $3$-dimensional and a $2$-dimensional space. For $h$ to be a submersion, this differential must be surjective, equivalently have rank $2$, equivalently have kernel of dimension $1$.

**Theorem routing:** The route is computational:
1. Compute the differential $dh_p$ in explicit coordinates (using the real or complex form).
2. Identify the kernel of $dh_p$ at each $p$ — it should be the tangent direction along the Hopf fibre (the great circle through $p$ in the orbit of the $S^1$-action).
3. Verify the kernel is $1$-dimensional, hence the rank of $dh_p$ is $2$, equal to the target's dimension; conclude $h$ is a submersion.

**Key decision point:** The cleanest way to compute the differential is via the $S^1$-action: $h$ is the quotient map of the $S^1$-action $\lambda \cdot (z, w) = (\lambda z, \lambda w)$ on $S^3$, restricted from the full $\mathbb{C}^*$-action on $\mathbb{C}^2 \setminus 0$. The vertical tangent vectors (tangent to fibres, i.e., to $S^1$-orbits) are spanned by the infinitesimal generator of the action: $(iz, iw)$ as a real tangent vector at $(z, w)$. This direction lies in $\ker dh_p$ by construction (the action is along fibres). Showing that $\ker dh_p$ is *exactly* this direction (not larger) is the verification.

---

# Legal Operations Used

1. **Operation 1 (compute the differential in coordinates):** core technique. Use the explicit formula $h(a+bi, c+di) = (2(ac+bd), 2(bc-ad), a^2+b^2-c^2-d^2)$ and differentiate, or work in complex coordinates and use the $\mathbb{C}^*$-action structure.

2. **Operation 5 (construct a local section):** an alternative way to verify submersion. Exhibit a smooth local section of $h$ through any point — for instance, near the north pole of $S^2$, parametrise the corresponding spherical cap of $S^3$ via stereographic-like coordinates and write down the inverse.

---

# Hints

> [!note]- Hint 1
> The Hopf map is the restriction of the quotient map $\mathbb{C}^2 \setminus 0 \to \mathbb{CP}^1$ to $S^3$. Equivalently, it is the quotient of the $S^1$-action $\lambda \cdot (z, w) = (\lambda z, \lambda w)$ on $S^3$.

> [!note]- Hint 2
> What are the fibres of $h$? Given a point $[z_0 : w_0] \in \mathbb{CP}^1$, the preimage in $S^3$ is the set of $(z, w) \in S^3$ with $[z : w] = [z_0 : w_0]$ — i.e., $(z, w) = \lambda(z_0, w_0)$ for some $\lambda \in \mathbb{C}^*$. Combined with $|z|^2 + |w|^2 = 1$, this restricts $\lambda$ to $|\lambda| = 1$. So the fibre is the great circle $\{(\lambda z_0, \lambda w_0) : \lambda \in S^1\}$.

> [!note]- Hint 3
> The infinitesimal generator of the $S^1$-action at $(z, w)$ is the velocity of the curve $t \mapsto (e^{it} z, e^{it} w)$ at $t = 0$, which is $(iz, iw)$ — a real tangent vector to $S^3$ at $(z, w)$. This is the "vertical" direction tangent to the Hopf fibre.

> [!note]- Hint 4
> The differential $dh_{(z,w)}$ vanishes on $(iz,iw)$ because this is the orbit direction. Containment alone does not determine the kernel: rank-nullity yields dimension one only **after** surjectivity is known. Instead, in the affine chart $[z:w]\mapsto w/z$, solve $d(w/z)_{(z,w)}(u,v)=0$ and use the tangent equation for $S^3$; the solution is exactly $\mathbb R(iz,iw)$.

> [!note]- Hint 5
> Alternative approach: differentiate the explicit real formula for $h$ and verify the Jacobian has rank $2$ at every point of $S^3$. (This is computationally laborious but direct.)

---

# Solution

The proof breaks into three steps. Step 1 identifies the vertical tangent direction (along Hopf fibres) using the $S^1$-action. Step 2 verifies $dh$ vanishes on this direction. Step 3 verifies $dh$ has rank exactly $2$, completing the submersion verification.

**Step 1: The vertical tangent direction at $(z, w) \in S^3$ is spanned by $(iz, iw)$.**

> [!note]- Derivation
> The Hopf map's fibres are great circles in $S^3$, given by the orbits of the $S^1$-action $\lambda \cdot (z, w) = (\lambda z, \lambda w)$ for $\lambda \in S^1$. At a point $(z, w) \in S^3$, the orbit is $\{(\lambda z, \lambda w) : \lambda \in S^1\}$ — a great circle in $S^3$.
>
> The tangent vector to this fibre at $(z, w)$ is obtained by differentiating the orbit curve $\gamma(t) = (e^{it} z, e^{it} w)$ at $t = 0$:
> $$\gamma'(0) = (iz, iw) \in T_{(z,w)} S^3 \subseteq \mathbb{C}^2.$$
> (We view $T_{(z,w)} S^3$ as a real [[Def - Subspace|subspace]] of $T_{(z,w)} \mathbb{C}^2 \cong \mathbb{C}^2 \cong \mathbb{R}^4$.)
>
> Verify $(iz, iw) \in T_{(z,w)} S^3$: differentiate $|z|^2 + |w|^2 = 1$ at $\gamma(t) = (e^{it}z, e^{it}w)$: $|e^{it}z|^2 + |e^{it}w|^2 = |z|^2 + |w|^2 = 1$, constant. So $\gamma(t) \in S^3$ for all $t$, confirming $\gamma'(0) = (iz, iw) \in T_{(z,w)} S^3$.

**Step 2: $dh_{(z,w)}(iz, iw) = 0$.**

> [!note]- Derivation
> The fibre of $h$ through $(z, w)$ is the orbit $\{(\lambda z, \lambda w) : \lambda \in S^1\}$, which is contained in the preimage $h^{-1}([z : w])$. Since the fibre is constant (mapped by $h$ to the single point $[z : w]$), the curve $\gamma(t) = (e^{it}z, e^{it}w)$ has $h(\gamma(t)) = [z : w]$ for all $t$ — i.e., $h \circ \gamma$ is constant.
>
> Differentiating at $t = 0$ by the chain rule:
> $$dh_{(z,w)}(\gamma'(0)) = 0,$$
> so $dh_{(z,w)}(iz, iw) = 0$. Hence $(iz, iw) \in \ker dh_{(z,w)}$, confirming that the vertical direction is in the kernel.

**Step 3: compute the kernel in projective coordinates.**

> [!note]- Derivation
> Regard the target as $\mathbb{CP}^1$. On the chart where $z\ne0$, the Hopf map has affine coordinate
> $$q(z,w)=\frac{w}{z}.$$
> For $(u,v)\in T_{(z,w)}S^3$,
> $$dq_{(z,w)}(u,v)=\frac{zv-wu}{z^2}.$$
> Thus $dq(u,v)=0$ exactly when $zv-wu=0$. Since $z\ne0$, this says $(u,v)=\lambda(z,w)$ for some $\lambda\in\mathbb C$. Tangency to $S^3$ means
> $$0=\operatorname{Re}(\bar zu+\bar wv)=\operatorname{Re}(\lambda)(|z|^2+|w|^2)=\operatorname{Re}(\lambda),$$
> so $\lambda=it$ for a unique $t\in\mathbb R$. Hence the kernel is precisely $\mathbb R(iz,iw)$.
>
> If $z=0$, then $w\ne0$ and the other affine coordinate $z/w$ gives the same conclusion. The kernel is therefore one-dimensional everywhere. Rank-nullity gives $\operatorname{rank}dh=3-1=2$, equal to $\dim S^2$, so $dh$ is surjective.

> [!note]- Complete formal solution
> The map $h:S^3\to\mathbb{CP}^1$, $(z,w)\mapsto[z:w]$, is smooth in the two standard affine charts. Its fibre through $(z,w)$ is the $S^1$-orbit $\{(e^{it}z,e^{it}w):t\in\mathbb R\}$, whose velocity at $t=0$ is $(iz,iw)$; hence $\mathbb R(iz,iw)\subseteq\ker dh_{(z,w)}$.
>
> Suppose first that $z\ne0$. In the target coordinate $q([z:w])=w/z$, the quotient rule gives
> $$d(q\circ h)_{(z,w)}(u,v)=\frac{zv-wu}{z^2}.$$
> If this vanishes, then $(u,v)=\lambda(z,w)$. Because $(u,v)$ is tangent to the unit sphere,
> $$0=\frac12d(|z|^2+|w|^2)_{(z,w)}(u,v)=\operatorname{Re}(\bar zu+\bar wv)=\operatorname{Re}\lambda,$$
> and therefore $(u,v)=t(iz,iw)$ for some real $t$. Conversely every such vector is killed because $h$ is constant on the orbit. Thus $\ker dh_{(z,w)}=\mathbb R(iz,iw)$ when $z\ne0$. When $w\ne0$, the coordinate $[z:w]\mapsto z/w$ proves the identical statement; these two cases cover $S^3$.
>
> Consequently $\dim\ker dh=1$ and $\operatorname{rank}dh=3-1=2$. Since the target tangent space has dimension $2$, $dh$ is surjective at every point. Hence the Hopf map is a smooth submersion, and every fibre is the great circle $\{(e^{it}z,e^{it}w):t\in\mathbb R\}$. $\qquad\blacksquare$

---

# Key Takeaways

**The Hopf map is a fibre bundle.** Beyond being a submersion, the Hopf map is a principal $S^1$-bundle $S^1\to S^3\to S^2$. Local triviality follows from the free proper $S^1$-action (or explicit local sections), not from submersivity alone: a general surjective submersion need not be a fibre bundle without additional hypotheses. The bundle is nontrivial because $S^3$ and $S^2\times S^1$ have different fundamental groups. Its principal-bundle class is the first Chern class, a generator of $H^2(S^2;\mathbb Z)$; the related Hopf invariant of the map records the linking of distinct fibres.

**Quotient maps under group actions are submersions.** The Hopf map is the quotient of the $S^1$-action on $S^3$; more generally, the quotient map of a free, proper Lie group action on a manifold is a smooth submersion (by the smooth quotient theorem). This is the cleanest source of submersions: take a manifold with a nice group action and project to the orbit space. The fibres are the orbits, each diffeomorphic to the group; the base is the orbit space, which is itself a manifold.

**Vertical and horizontal decomposition.** The proof above decomposed $T_{(z,w)} S^3$ into a vertical subspace (tangent to the fibre) and a horizontal complement (orthogonal in the Hermitian metric). This is the general pattern for fibre bundles: the tangent space at a point of the total space decomposes (after a choice of connection) into vertical (tangent to fibre) plus horizontal (chosen complement). The vertical-horizontal decomposition is the foundation of **connection theory** and **gauge theory** in differential geometry.

**Cross-link to companion exercises and forward bridges.** This exercise is the bridge between the local theory of submersions and the global theory of fibre bundles. It connects to [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]] (the vertical vector field $(iz, iw)$ is the infinitesimal generator of the $S^1$-action) and to [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]] (the Hopf [[Def - Fibration|fibration]] is the principal bundle $\mathrm{U}(1) \to S^3 \to S^2 = \mathrm{SU}(2)/\mathrm{U}(1)$).
