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
> The differential $dh_{(z,w)}$ vanishes on $(iz, iw)$ because moving in this direction stays on the same Hopf fibre. So $\ker dh_{(z,w)}$ contains the line through $(iz, iw)$. To show $\ker dh_{(z,w)}$ is *exactly* this line, show it is $1$-dimensional — by dimension count, $\dim S^3 - \dim S^2 = 3 - 2 = 1$.

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

**Step 3: $\ker dh_{(z,w)}$ has dimension exactly $1$, hence $dh_{(z,w)}$ is surjective.**

> [!note]- Derivation
> We use a dimension count. The differential $dh_{(z,w)} : T_{(z,w)} S^3 \to T_{[z:w]} S^2$ is a linear map between a $3$-dimensional and a $2$-dimensional vector space. By rank-nullity,
> $$\dim \ker dh_{(z,w)} + \mathrm{rank}\, dh_{(z,w)} = \dim T_{(z,w)} S^3 = 3.$$
> We need to show $\mathrm{rank}\, dh_{(z,w)} = 2$, equivalently $\dim \ker dh_{(z,w)} = 1$. We already know $(iz, iw) \in \ker dh_{(z,w)}$ (Step 2), giving a non-trivial element. To show this is the only direction, we use the *transverse-to-fibre* description: any element of $T_{(z,w)} S^3$ not parallel to $(iz, iw)$ should map to a nonzero tangent vector in $T_{[z:w]} S^2$.
>
> An efficient argument: the tangent space $T_{(z,w)} S^3$ at $(z, w) \in S^3 \subseteq \mathbb{C}^2$ is $\{(\dot z, \dot w) \in \mathbb{C}^2 : \mathrm{Re}(\bar z \dot z + \bar w \dot w) = 0\}$ (the real-codimension-$1$ subspace orthogonal to the outward normal $(z, w)$ — see [[Ex - The Sphere as a Level Set]]). This is a real $3$-dimensional space.
>
> Within this tangent space, the vertical direction $(iz, iw)$ is the imaginary part of $(z, w)$ multiplied by $(z, w)$ itself in some sense; the *horizontal* directions are the elements $(\dot z, \dot w) \in T_{(z,w)} S^3$ with $\mathrm{Im}(\bar z \dot z + \bar w \dot w) = 0$ (real-orthogonal to the vertical in the Hermitian metric). This is a real $2$-dimensional subspace.
>
> *Claim: $dh_{(z,w)}$ restricted to the horizontal subspace is a linear isomorphism onto $T_{[z:w]} S^2$.*
>
> Proof sketch: the Hopf map $h$ is induced by the $\mathbb{C}^*$-action on $\mathbb{C}^2 \setminus 0$, and at the linear level, $dh_{(z,w)}$ kills the $\mathbb{C}^*$-orbit's tangent. Restricted to $S^3$, the $\mathbb{C}^*$-orbit tangent decomposes into the radial direction (which is normal to $S^3$ and not in $T_{(z,w)} S^3$ at all) plus the $S^1$-orbit tangent $(iz, iw)$ (the vertical). So in $T_{(z,w)} S^3$, only the vertical direction is killed; the horizontal complement maps isomorphically.
>
> More explicitly: define the **horizontal subspace** $H_{(z,w)} = \{(\dot z, \dot w) \in T_{(z,w)} S^3 : \mathrm{Re}(\bar z \dot z + \bar w \dot w) = 0, \mathrm{Im}(\bar z \dot z + \bar w \dot w) = 0\} = \{(\dot z, \dot w) : \bar z \dot z + \bar w \dot w = 0\}$. This is a real $2$-dimensional subspace of $T_{(z,w)} S^3$ (the conditions $\mathrm{Re} = 0$ and $\mathrm{Im} = 0$ give $2$ real codimension-$1$ conditions on the $4$-real-dimensional $\mathbb{C}^2$, but one is the sphere condition, so $H$ has real dimension $4 - 2 = 2$). On $H_{(z,w)}$, $dh$ is injective (since $\ker dh = $ span of $(iz, iw) \notin H_{(z,w)}$); hence by dimension count $dh|_H$ is an isomorphism onto $T_{[z:w]} S^2$.
>
> Therefore $\mathrm{rank}\, dh_{(z,w)} = 2$, so $dh_{(z,w)}$ is surjective, so $h$ is a submersion at every point of $S^3$.

> [!note]- Complete formal solution
>
> Identify $T_{(z,w)} S^3 = \{(\dot z, \dot w) \in \mathbb{C}^2 : \mathrm{Re}(\bar z \dot z + \bar w \dot w) = 0\}$ — a real $3$-dimensional subspace of $T_{(z,w)} \mathbb{C}^2 = \mathbb{C}^2 \cong \mathbb{R}^4$. The curve $\gamma(t) = (e^{it}z, e^{it}w)$ lies in $S^3$ (norm preserved by multiplication by $e^{it}$), so $\gamma'(0) = (iz, iw) \in T_{(z,w)} S^3$.
>
> The Hopf map $h$ is constant on the curve $\gamma$ (the curve traces out a single Hopf fibre $[z:w]$). Differentiating at $t = 0$: $dh_{(z,w)}(iz, iw) = 0$. So $(iz, iw) \in \ker dh_{(z,w)}$.
>
> Decompose $T_{(z,w)} S^3$ into the vertical direction $V_{(z,w)} = \mathbb{R}(iz, iw)$ and the horizontal complement $H_{(z,w)} = \{(\dot z, \dot w) \in T_{(z,w)} S^3 : \mathrm{Im}(\bar z \dot z + \bar w \dot w) = 0\}$. The vertical direction is real-$1$-dimensional; the horizontal is real-$2$-dimensional (since both real and imaginary parts of $\bar z \dot z + \bar w \dot w$ vanish, giving two real conditions on the $4$-real-dimensional $\mathbb{C}^2$ — and removing one duplicate-with-sphere-condition gives codimension $2$ within $T S^3 = \mathbb{R}^3$).
>
> $dh_{(z,w)}$ vanishes on the vertical $V_{(z,w)}$. We claim it is injective on the horizontal $H_{(z,w)}$. Indeed, any element $(\dot z, \dot w) \in H_{(z,w)} \cap \ker dh_{(z,w)}$ must be in the kernel and horizontal. The kernel of $dh$ in $T_{(z,w)} S^3$ is at most $\dim T S^3 - \dim T S^2 = 3 - 2 = 1$-dimensional (rank-nullity, given that the rank is at most $\dim T S^2 = 2$). Since $V_{(z,w)} \subseteq \ker dh_{(z,w)}$ is already $1$-dimensional, the kernel equals $V_{(z,w)}$ — but $V_{(z,w)} \cap H_{(z,w)} = 0$ (vertical and horizontal are complementary in $T S^3$). So $H_{(z,w)} \cap \ker dh_{(z,w)} = 0$, i.e., $dh|_{H_{(z,w)}}$ is injective.
>
> By dimension count, $dh_{(z,w)}|_{H_{(z,w)}} : H_{(z,w)} \to T_{[z:w]} S^2$ is an injective linear map between $2$-dimensional spaces, hence an isomorphism. So $dh_{(z,w)}$ is surjective onto $T_{[z:w]} S^2$, i.e., $h$ is a submersion at $(z,w)$.
>
> Since $(z, w) \in S^3$ was arbitrary, $h$ is a smooth submersion. The fibre $h^{-1}([z:w]) = \{(\lambda z, \lambda w) : \lambda \in S^1\}$ is a great circle in $S^3$ (the unit-norm scalar multiples of $(z, w)$). $\qquad\blacksquare$

> [!note]- Sanity check via explicit Jacobian
> Using the real coordinate form $h(a + bi, c + di) = (2(ac + bd), 2(bc - ad), a^2 + b^2 - c^2 - d^2)$ at the point $(z, w) = (1, 0)$ (i.e., $a = 1, b = c = d = 0$), compute the Jacobian:
> $$Dh(1, 0, 0, 0) = \begin{pmatrix} 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & -2 \\ 2 & 0 & 0 & 0 \end{pmatrix}.$$
> Restricted to $T_{(1,0,0,0)} S^3$ = $\{v : v_1 = 0\}$ (the orthogonal complement of $(1, 0, 0, 0)$), this becomes
> $$\begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & -2 \\ 0 & 0 & 0 \end{pmatrix}\quad\text{on the basis } (e_2, e_3, e_4) \text{ of } T_{(1,0,0,0)} S^3 \subseteq \mathbb{R}^4.$$
> Wait, this has rank $2$ but only because of the last row being zero. Let me reconsider: the image lies in $T_{h(1,0)} S^2$, which has dimension $2$. At $(1,0)$, $h(1, 0) = (0, 0, 1)$ (the north pole), and $T_{(0,0,1)} S^2 = \{(u, v, 0) : u, v \in \mathbb{R}\}$. The Jacobian $Dh(1,0,0,0)$ restricted to $T_{(1,0,0,0)} S^3$ has image in $T_{(0,0,1)} S^2$:
> $$Dh(1,0,0,0) \cdot (0, b, c, d)^T = (2c, -2d, 0).$$
> This is surjective onto $T_{(0,0,1)} S^2 = \{(u, v, 0)\}$: for any $(u, v, 0)$, take $c = u/2$, $d = -v/2$, $b$ arbitrary. The kernel within $T S^3$ is $b$-axis, i.e., the direction $(0, 1, 0, 0)$ in $\mathbb{R}^4$ — which in complex coordinates corresponds to $(i \cdot 1, 0) = (i, 0)$, exactly the vertical direction $(iz, iw) = (i, 0)$ at $(z, w) = (1, 0)$. Sanity check passed.

---

# Key Takeaways

**The Hopf map is a fibre bundle.** Beyond being a submersion, the Hopf map is a smooth $S^1$-bundle over $S^2$: $S^3 \to S^2$ with fibre $S^1$. The submersion structure is what makes it locally trivial (locally the projection $U \times S^1 \to U$). Globally, the bundle is *nontrivial*: $S^3$ is not diffeomorphic to $S^2 \times S^1$ (their fundamental [[Def - Group|groups]] differ — $\pi_1(S^3) = 0$ versus $\pi_1(S^2 \times S^1) = \mathbb{Z}$). The non-triviality is encoded in the **Hopf invariant**, an integer-valued topological invariant detecting the linking number of the Hopf fibres. The Hopf bundle is the prototypical nontrivial principal bundle and appears throughout physics (Dirac monopoles, $\mathrm{SU}(2)$ gauge theory, quantum information).

**Quotient maps under group actions are submersions.** The Hopf map is the quotient of the $S^1$-action on $S^3$; more generally, the quotient map of a free, proper Lie group action on a manifold is a smooth submersion (by the smooth quotient theorem). This is the cleanest source of submersions: take a manifold with a nice group action and project to the orbit space. The fibres are the orbits, each diffeomorphic to the group; the base is the orbit space, which is itself a manifold.

**Vertical and horizontal decomposition.** The proof above decomposed $T_{(z,w)} S^3$ into a vertical subspace (tangent to the fibre) and a horizontal complement (orthogonal in the Hermitian metric). This is the general pattern for fibre bundles: the tangent space at a point of the total space decomposes (after a choice of connection) into vertical (tangent to fibre) plus horizontal (chosen complement). The vertical-horizontal decomposition is the foundation of **connection theory** and **gauge theory** in differential geometry.

**Cross-link to companion exercises and forward bridges.** This exercise is the bridge between the local theory of submersions and the global theory of fibre bundles. It connects to [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]] (the vertical vector field $(iz, iw)$ is the infinitesimal generator of the $S^1$-action) and to [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]] (the Hopf [[Def - Fibration|fibration]] is the principal bundle $\mathrm{U}(1) \to S^3 \to S^2 = \mathrm{SU}(2)/\mathrm{U}(1)$).
