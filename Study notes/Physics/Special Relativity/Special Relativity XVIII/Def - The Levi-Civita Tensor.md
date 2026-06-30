---
type: definition
subject: special-relativity
prereqs:
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - Spacetime Orientation"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. $E$ is the vector space of [[Def - Minkowski Space and the Metric|Minkowski space]], $(e_\alpha)$ a basis with [[Def - Metric Duality and Index Manipulation|dual basis]] $(e^\alpha)$, not necessarily orthonormal; $g_{\alpha\beta} = g(e_\alpha, e_\beta)$ are the metric components in that basis and $\det g$ the determinant of the matrix $(g_{\alpha\beta})$. The **Levi-Civita symbol** $[\alpha,\beta,\gamma,\delta]$ (also written $\epsilon_{\alpha\beta\gamma\delta}$ in some texts) is the purely combinatorial object equal to $0$ if two indices coincide, $+1$ if $(\alpha,\beta,\gamma,\delta)$ is an even permutation of $(0,1,2,3)$, and $-1$ if odd. The **Levi-Civita tensor** is $\varepsilon$ (boldface in Gourgoulhon), a genuine type-$(0,4)$ [[Def - Tensors on Minkowski Space|tensor]]. Greek indices run $0$–$3$; the Einstein convention sums an up–down pair. Full registry on [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality]].

> [!warning] Convention: the Levi-Civita symbol versus the Levi-Civita tensor
> Keep two objects apart. The **symbol** $[\alpha,\beta,\gamma,\delta] \in \{-1,0,+1\}$ is the same array of numbers in every basis — it is *not* a tensor. The **tensor** $\varepsilon$ is basis-independent as a multilinear map, and its *components* in an orthonormal right-handed basis happen to equal the symbol: $\varepsilon_{\alpha\beta\gamma\delta} = [\alpha,\beta,\gamma,\delta]$. In a non-orthonormal basis the components pick up a factor $\sqrt{-\det g}$. Crucially, $\det g < 0$ in **both** metric signatures (mostly-plus and mostly-minus give $\det g = -1$ in an orthonormal basis), so $\varepsilon_{0123} = +1$ and the lowered components are **signature-independent**. The one place a sign genuinely depends on convention is the *raised* component $\varepsilon^{0123}$ and the contraction identities, addressed below.

---

# Axiom Motivation

Minkowski space comes with a [[Def - Minkowski Space and the Metric|metric]], which measures lengths and angles, but the metric alone does not know **orientation** or **oriented volume** — it cannot distinguish a right-handed frame from a left-handed one, because reflections are isometries. Yet physics needs oriented volume constantly: the cross product of three-vectors, the sense of a magnetic field, the direction of angular momentum, the [[Def - The Hodge Star|Hodge dual]], and the very notion of "the volume element $d^4x$" all require a choice of orientation and a way to compute signed four-volume. The Levi-Civita tensor is the object that supplies this. The motivation is: build, from the metric and an [[Def - Spacetime Orientation|orientation]], the canonical antisymmetric four-linear form that returns $+1$ on a right-handed orthonormal frame — the **volume form** of spacetime.

Start from the fact that the space of $4$-forms is **one-dimensional** ($\dim\mathscr{A}_4(E) = 1$, an [[Def - Alternate Forms and the Exterior Product|exterior-algebra]] fact). So up to a single scalar there is exactly one alternate four-linear form, and to pin it down we need only fix its value on one frame. The natural normalisation is to demand $\varepsilon(\vec e_0, \vec e_1, \vec e_2, \vec e_3) = 1$ on a right-handed *orthonormal* basis. That this is consistent — that the same form gives $\pm 1$ on *every* orthonormal basis, with sign tracking handedness — is exactly the content of the dimension-one statement: any two normalisations on orthonormal frames differ by the determinant of the change of basis, and that determinant is $\pm 1$ for a [[Def - The Lorentz Group|Lorentz]] change of frame. So "value $1$ on a right-handed orthonormal frame" determines a unique tensor.

Why must the metric enter the *components* in a general basis, via $\sqrt{-\det g}$? Because the value of $\varepsilon$ on a non-orthonormal frame is the oriented volume of the parallelepiped that frame spans, and that volume is measured by the metric. If $(\vec e_\alpha)$ is related to an orthonormal frame by a matrix $P$, then $\varepsilon(\vec e_0, \dots, \vec e_3) = \det P$, while the metric components satisfy $g = {}^tP\,\eta\,P$, so $\det g = -(\det P)^2$ and hence $\det P = \pm\sqrt{-\det g}$. The factor $\sqrt{-\det g}$ is therefore not an arbitrary insertion: it is the oriented volume of the basis parallelepiped, the Jacobian relating a general frame to an orthonormal one. The minus sign under the square root is forced by the Lorentzian signature ($\det g < 0$), and it is what makes $\sqrt{-\det g}$ real — the same minus sign that makes the metric indefinite makes the volume form well-defined.

The orientation choice is genuinely separate from the metric, and dropping it has a concrete cost. The metric is invariant under the full [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$, including the parity and time reversals that flip handedness. The volume form is invariant only under the *orientation-preserving* subgroup $SO(1,3)$ (determinant $+1$); under a reflection it changes sign, $\varepsilon \mapsto -\varepsilon$. So $\varepsilon$ carries strictly more information than $g$: it knows handedness. This is why $\varepsilon$ is the right tool for **pseudo**-quantities — the magnetic field, the angular momentum vector, the cross product — which all flip under parity. An object built with $\varepsilon$ is a tensor under $SO(1,3)$ but a *pseudo*-tensor under the full $O(1,3)$, and that distinction is physical (it is why a mirror sends a right hand to a left hand).

Finally, the **full antisymmetry** is not optional — it is what makes $\varepsilon$ measure *volume* rather than some other multilinear quantity. A parallelepiped with two coincident edges is degenerate (zero volume), which forces $\varepsilon$ to vanish when two arguments agree, hence to be alternating. And it is what produces the beautiful **contraction identities** $\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = -24 = -4!$ (the signed count of permutations) and their partial contractions, which are the algebraic workhorses behind every Hodge-star computation and every cross-product identity. Those identities are pure combinatorics of the symmetric group, dressed with the signature sign $\mathrm{sgn}(\det g) = -1$.

---

# The Definition

The **Levi-Civita tensor** $\varepsilon$ is the unique alternate four-linear form (type-$(0,4)$ tensor, $\varepsilon \in \mathscr{A}_4(E)$) that takes the value $+1$ on every right-handed orthonormal basis of $(E, g)$. Its components in an arbitrary basis $(e_\alpha)$ are
$$
\boxed{\ \varepsilon_{\alpha\beta\gamma\delta} = \pm\sqrt{-\det g}\;[\alpha,\beta,\gamma,\delta]\ }, \qquad \det g < 0,
$$
with the $+$ sign for a right-handed basis and $-$ for a left-handed one; $[\alpha,\beta,\gamma,\delta]$ is the Levi-Civita **symbol**. Equivalently $\varepsilon(\vec e_0, \vec e_1, \vec e_2, \vec e_3) = \pm\sqrt{-\det g}$. In an orthonormal basis $\det g = \det\eta = -1$, so $\varepsilon_{0123} = +1$ (right-handed). As a form,
$$
\varepsilon = \varepsilon_{\alpha\beta\gamma\delta}\, e^\alpha\otimes e^\beta\otimes e^\gamma\otimes e^\delta = \varepsilon_{0123}\, e^0\wedge e^1\wedge e^2\wedge e^3,
\qquad
\varepsilon(\vec u, \vec v, \vec w, \vec z) = \varepsilon_{\alpha\beta\gamma\delta}\, u^\alpha v^\beta w^\gamma z^\delta.
$$

**Raised components.** Raising all four indices with the inverse metric $g^{\alpha\beta}$ gives
$$
\boxed{\ \varepsilon^{\alpha\beta\gamma\delta} = \mp\frac{1}{\sqrt{-\det g}}\;[\alpha,\beta,\gamma,\delta]\ },
$$
with $-$ for a right-handed basis. The sign is **opposite** to the lowered component: in an orthonormal basis $\varepsilon^{0123} = -1$, whereas $\varepsilon_{0123} = +1$. (The flip is the determinant $\det\eta = -1$ acquired in raising four indices, and equals $-1$ in both signatures.)

**Associated tensors.** Raising $1,2,3,4$ indices defines tensors $^{p}\varepsilon$ of types $(1,3), (2,2), (3,1), (4,0)$:
$$
\varepsilon^\alpha{}_{\beta\gamma\delta} = g^{\alpha\mu}\varepsilon_{\mu\beta\gamma\delta}, \quad
\varepsilon^{\alpha\beta}{}_{\gamma\delta} = g^{\alpha\mu}g^{\beta\nu}\varepsilon_{\mu\nu\gamma\delta}, \quad
\varepsilon^{\alpha\beta\gamma}{}_{\delta} = g^{\alpha\mu}g^{\beta\nu}g^{\gamma\rho}\varepsilon_{\mu\nu\rho\delta}, \quad
\varepsilon^{\alpha\beta\gamma\delta} = g^{\alpha\mu}g^{\beta\nu}g^{\gamma\rho}g^{\delta\sigma}\varepsilon_{\mu\nu\rho\sigma}.
$$

**Contraction identities.** Contracting a raised $\varepsilon$ against a lowered $\varepsilon$ on $p$ index pairs gives (Gourgoulhon 14.67–14.72), with the overall sign $\mathrm{sgn}(\det g) = -1$:
$$
\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = -24, \qquad
\varepsilon^{\mu\nu\rho\alpha}\varepsilon_{\mu\nu\rho\beta} = -6\,\delta^\alpha{}_\beta, \qquad
\varepsilon^{\mu\nu\alpha\beta}\varepsilon_{\mu\nu\gamma\delta} = -2\big(\delta^\alpha{}_\gamma\delta^\beta{}_\delta - \delta^\alpha{}_\delta\delta^\beta{}_\gamma\big),
$$
and in general $\varepsilon^{\mu_1\dots\mu_{4-p}\alpha_1\dots\alpha_p}\varepsilon_{\mu_1\dots\mu_{4-p}\beta_1\dots\beta_p} = -(4-p)!\sum_{\sigma\in\mathfrak{S}_p}(-1)^{k(\sigma)}\delta^{\alpha_{\sigma(1)}}{}_{\beta_1}\cdots\delta^{\alpha_{\sigma(p)}}{}_{\beta_p}$.

---

# Categorical / Structural Definition

$\varepsilon$ is the **metric volume form** of the oriented inner-product space $(E, g, \mathfrak{o})$ — the canonical generator of the one-dimensional top exterior power $\Lambda^4 E^*$ normalised by the metric. Equivalently, it is the image of $1$ under the composite of the orientation isomorphism $\Lambda^4 E^* \cong \mathbb{R}$ and the metric normalisation. Among all generators of $\Lambda^4 E^*$, the metric singles out the two with $|\varepsilon(\text{orthonormal frame})| = 1$, and the orientation picks one of the two. Under the [[Def - The Lorentz Group|Lorentz group]], $\varepsilon$ transforms as a four-linear form by $\det$ of the transformation: it is invariant under $SO(1,3)$ (determinant $+1$) and changes sign under the reflections in $O(1,3)\setminus SO(1,3)$ — that is, $\varepsilon$ is a **pseudo-tensor**, an invariant of the *oriented* structure group only.

In the language of the [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|Riemannian volume form]] on a manifold, $\varepsilon$ is the fibrewise volume element; promoted to a field on a [[Def - Riemannian Manifold|(pseudo-)Riemannian manifold]] it is $\sqrt{-\det g}\,dx^0\wedge dx^1\wedge dx^2\wedge dx^3$, the object one integrates to get four-volume and the object whose Hodge dual of a function gives the integrand of $\int f\,d^4x$. The contraction identities are the structural fingerprint of the symmetric group $\mathfrak{S}_4$ acting on the four-dimensional defining representation: $\varepsilon\otimes\varepsilon$, fully antisymmetrised, is the signed sum over permutations, and contracting recovers the generalised Kronecker delta — the determinant of a matrix of $\delta$'s — scaled by $\mathrm{sgn}(\det g)$.

---

# Relate to Other Fields / Compression

The Levi-Civita tensor is the four-dimensional, Lorentzian generalisation of the **scalar triple product / determinant** of vector calculus. In $\mathbb{R}^3$ the symbol $\epsilon_{ijk}$ gives the cross product $(\mathbf a\times\mathbf b)_i = \epsilon_{ijk}a^j b^k$ and the determinant $\det(\mathbf a,\mathbf b,\mathbf c) = \epsilon_{ijk}a^i b^j c^k$; in $\mathbb{R}^4$ with a metric, $\varepsilon$ plays both roles and, through the [[Def - The Hodge Star|Hodge star]], converts a $2$-form into another $2$-form (the magnetic-from-electric swap). The famous $\epsilon$–$\delta$ identity of vector calculus, $\epsilon_{ijk}\epsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$, is the three-dimensional sibling of the contraction identities above; relativists use the four-dimensional versions constantly to reduce Hodge-star and field-invariant computations to Kronecker deltas.

**True name:** $\varepsilon$ is *the volume form — the unique alternating four-linear gadget that reads $+1$ on a right-handed orthonormal frame and the signed four-volume on any frame, equal to $\sqrt{-\det g}\,[\alpha\beta\gamma\delta]$ in components*. Its operational essence is captured by the contraction identities: whenever two $\varepsilon$'s appear in a product, replace $\varepsilon\varepsilon$ by the appropriate signed combination of Kronecker deltas (with the relativistic minus sign), and the computation collapses. The reflex: any oriented-volume, cross-product, or duality construction is "contract with $\varepsilon$," and any product of two such constructions is "expand $\varepsilon\varepsilon$ into deltas."

---

# Examples / Corollaries

**Is an instance — the orthonormal components.** In a right-handed orthonormal frame, $\varepsilon_{0123} = +1$, $\varepsilon_{1023} = -1$, $\varepsilon_{0023} = 0$, and every component equals the sign of the permutation taking $(0,1,2,3)$ to the index order (or $0$ for a repeat).

**Is an instance — the four-volume of a frame.** For a general basis with $\det g = -V^2$ ($V > 0$), $\varepsilon(\vec e_0, \vec e_1, \vec e_2, \vec e_3) = \pm V$ — the signed four-volume of the parallelepiped the basis spans, positive for a right-handed frame.

**Is an instance — the cross product in an observer's space.** Restricting $\varepsilon$ to the [[Def - Observer and Local Rest Space|local rest space]] of an observer with four-velocity $\vec u$, the trilinear form $\varepsilon_{\vec u}(\vec v, \vec w, \cdot) := \varepsilon(\vec u, \vec v, \vec w, \cdot)$ gives, by metric duality, the ordinary three-dimensional cross product $\vec v\times_{\vec u}\vec w$ in that observer's Euclidean space.

**Is NOT an instance — the Levi-Civita symbol.** The symbol $[\alpha,\beta,\gamma,\delta]$ is **not** a tensor: it is the same array in every basis, so it does not transform by the tensor law. Treating it as a tensor (forgetting the $\sqrt{-\det g}$) gives wrong answers in any non-orthonormal frame, e.g. curvilinear coordinates.

**Is NOT an instance — a generic type-$(0,4)$ tensor.** A four-linear form that is not fully antisymmetric (e.g. $g\otimes g$) is not proportional to $\varepsilon$; only the alternating ones are, because $\dim\mathscr{A}_4(E) = 1$ but $\dim\mathscr{T}_{(0,4)}(E) = 256$.

**Corollary — the raised and lowered top components have opposite sign.** $\varepsilon^{0123} = -1$ while $\varepsilon_{0123} = +1$ in an orthonormal frame. The product is the full contraction $\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = -24 = -4!$.

**Corollary — $\varepsilon$ flips under parity.** A spatial reflection has determinant $-1$, so $\varepsilon \mapsto -\varepsilon$; quantities built linearly from $\varepsilon$ (magnetic field, angular momentum, cross products) are pseudovectors, changing sign in a mirror.

**Calibration check.** If you have understood the definition you can: (i) state why $\varepsilon_{0123} = +1$ in *both* signatures but $\varepsilon^{0123} = -1$; (ii) compute $\varepsilon^{\mu\nu\rho\sigma}\varepsilon_{\mu\nu\rho\sigma} = -24$ from the contraction identity; (iii) explain why $\varepsilon$ is a pseudo-tensor (invariant under $SO(1,3)$, sign-flipping under reflections).

---

# Unlocked by This

> [!tip] The Hodge Star *(from §18.3)*
> The Levi-Civita tensor is the engine of the [[Def - The Hodge Star|Hodge star]] $\star$: dualising a $p$-form means contracting it (after raising its indices with $g^{-1}$) against $\varepsilon$. The contraction identities above are exactly what is needed to prove $\star\star = (-1)^{p+1}$ and the field-strength duality relations; see [[Thm - Hodge Star and the Exterior Product]].

> [!tip] The Volume Element and Integration *(from §18.3 and Stokes' Theorem)*
> Promoted to a field, $\varepsilon = \sqrt{-\det g}\;dx^0\wedge dx^1\wedge dx^2\wedge dx^3$ is the spacetime **volume element**, the $4$-form integrated to compute four-volume and the measure in every action integral. It is the relativistic [[Def - Riemannian Volume Form|Riemannian volume form]]; see [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem]].

> [!tip] The Pauli-Lubanski Vector and Dual Field Strength *(from Particle Physics and Electromagnetism)*
> Contracting $\varepsilon$ with the angular-momentum tensor and four-momentum builds the **Pauli-Lubanski vector** $W^\mu = -\tfrac12\varepsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$, whose square is a Casimir of the [[Def - The Poincaré Group|Poincaré group]] fixing the spin of a particle; contracting $\varepsilon$ with the field-strength builds the **dual field** $\star F$ whose invariant $\star F^{\mu\nu}F_{\mu\nu} \propto \mathbf E\cdot\mathbf B$ classifies the electromagnetic field. Both are pseudo-quantities, born from $\varepsilon$.
