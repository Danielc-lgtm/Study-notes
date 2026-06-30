---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Observer and Local Rest Space"
  - "Def - The Levi-Civita Tensor"
  - "Def - Tensors on Minkowski Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a timelike vector $X$ has $X\cdot X > 0$. Points of Minkowski space $\mathscr{E}$ are events; $C$ is a fixed reference event and $M$ a point on a particle's [[Def - Worldline of a Particle|worldline]] $\mathscr{L}$. The displacement from $C$ to $M$ is the four-vector $\overrightarrow{CM}$, with components $x^\alpha$ in a frame; its metric-dual one-form is written $\overrightarrow{CM}^\flat$, with components $x_\alpha = \eta_{\alpha\beta}x^\beta$. The particle's [[Def - Four-Momentum and Rest Mass|four-momentum]] is $p$, components $p^\alpha = (E, \mathbf{p})$ relative to an observer of four-velocity $U_0$, with $E = P\cdot U_0$ the energy and $\mathbf{p}$ the spatial momentum. The exterior product of two one-forms is $a\wedge b = a\otimes b - b\otimes a$. The cross product on an observer's rest space $E_{u_0}$ is the one induced by the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] $\epsilon$. Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

> [!warning] Convention
> Gourgoulhon defines this object in the mostly-plus signature $(-,+,+,+)$ as the two-form $J_C = \overrightarrow{CM}^\flat\wedge p$, with $\vec u_0\cdot\vec u_0 = -c^2$. The observer-relative split he derives carries his signs. The contravariant tensor $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$ is metric-free and reads identically in both signatures; we take it as primary and recover the observer-relative pieces natively in mostly-minus.

---

# Axiom Motivation

We have a particle with a [[Def - Four-Momentum and Rest Mass|four-momentum]] $p$, and we want an object that captures its *angular* momentum — the moment of its momentum about a chosen reference event $C$. In Newtonian mechanics the recipe is unambiguous: $\mathbf{L} = \mathbf{r}\times\mathbf{p}$, the cross product of the position vector with the momentum. The whole motivation of this definition is the discovery that the cross product does not survive the passage to four dimensions, and that what replaces it is not a vector but a tensor.

Why does the cross product fail? The cross product takes two vectors in $\mathbb{R}^3$ and returns a third, and it does so because the antisymmetric pairs of the three coordinate axes — the planes $xy$, $yz$, $zx$ — are themselves three in number, $\binom{3}{2}=3$, so they can be relabelled as a vector. The "angular momentum vector" $\mathbf{L}$ is really a bookkeeping of the three *planes* of rotation, disguised as three axes. In four dimensions there are $\binom{4}{2}=6$ planes — $tx, ty, tz, xy, yz, zx$ — and six is not four. The disguise is impossible. The honest object that records "moment of momentum in each plane" is the **antisymmetric rank-two tensor** with one component per plane, and that is what we must build.

So the desideratum is an object, one number per coordinate plane, that (i) reduces to $\mathbf{r}\times\mathbf{p}$ in its space-space components, (ii) is built only from $\overrightarrow{CM}$ and $p$, and (iii) transforms correctly under Lorentz transformations so that it has frame-independent meaning. The unique antisymmetric bilinear combination of two four-vectors $\overrightarrow{CM}$ and $p$ is their antisymmetrised product, $x^\alpha p^\beta - x^\beta p^\alpha$. Its $\alpha\beta = ij$ (spatial) components are $x^ip^j - x^jp^i$, which are exactly the components of $\mathbf{r}\times\mathbf{p}$ written as a $3\times 3$ antisymmetric matrix. So this combination passes test (i) automatically. It passes (ii) by construction. And it passes (iii) because the antisymmetrised product of two tensors is a tensor — a fact that needs no metric, which is why the upper-index form $J^{\alpha\beta}$ is the cleanest statement.

Could we have chosen a different antisymmetrisation, or added a symmetric piece? A symmetric piece $x^\alpha p^\beta + x^\beta p^\alpha$ would not reduce to a cross product (it is not antisymmetric, so it cannot record planes of rotation) and would not be conserved for a free particle. Dropping the antisymmetry entirely, keeping the full $x^\alpha p^\beta$, gives an object that is *not* conserved even for a free particle — the symmetric part grows linearly in proper time. Antisymmetry is forced by conservation: only the antisymmetric combination has the property that its proper-time derivative for a free particle vanishes (the symmetric part's derivative is $cU^\alpha p^\beta + cp^\alpha U^\beta \ne 0$). The antisymmetry is not an aesthetic choice; it is what makes the object a *conserved* angular momentum.

One more decision: the object depends on a reference event $C$. There is no canonical origin in Minkowski space — it is an affine space — so angular momentum, like its Newtonian ancestor, is always *about a point*. Changing the point shifts the tensor by the angular momentum of the total momentum acting at the displacement, $\overrightarrow{C'C}^\flat\wedge P$; the part that does not shift is the intrinsic spin. The dependence on $C$ is therefore not a defect but the very structure that will let us separate orbital from intrinsic angular momentum in the [[Thm - König Theorem (Relativistic)|König theorem]].

---

# The Definition

Let $\mathscr{P}$ be a particle with [[Def - Four-Momentum and Rest Mass|four-momentum]] $p$, and let $C\in\mathscr{E}$ be an event. The **angular momentum of $\mathscr{P}$ with respect to $C$** is the antisymmetric rank-two tensor with components, in any inertial frame with origin at $C$,
$$
J^{\alpha\beta} \;=\; x^\alpha p^\beta - x^\beta p^\alpha,
\qquad
J_{\alpha\beta} \;=\; x_\alpha p_\beta - x_\beta p_\alpha,
$$
where $x^\alpha$ are the components of the displacement $\overrightarrow{CM}$ and $p^\alpha$ those of $p$. Equivalently, it is the **angular momentum two-form**
$$
J_C \;:=\; \overrightarrow{CM}^\flat \wedge p \;=\; \overrightarrow{CM}^\flat\otimes p - p\otimes\overrightarrow{CM}^\flat,
$$
acting on a pair of vectors $(\vec v,\vec w)$ by $J_C(\vec v,\vec w) = (\overrightarrow{CM}\cdot\vec v)(p\cdot\vec w) - (p\cdot\vec v)(\overrightarrow{CM}\cdot\vec w)$. It is manifestly antisymmetric, $J_C(\vec v,\vec w) = -J_C(\vec w,\vec v)$, hence has six independent components.

Relative to an observer of four-velocity $U_0$, with local rest space $E_{u_0}$, the tensor decomposes into two three-vectors. Writing $\overrightarrow{CM} = h\,U_0 + \vec X$ with $\vec X\in E_{u_0}$ and $p = E\,U_0 + \mathbf{p}$ with $\mathbf{p}\in E_{u_0}$ (so $E = p\cdot U_0$ is the energy and $\mathbf{p}$ the spatial momentum), the space-space components form the **angular momentum vector**
$$
\vec\sigma_C \;=\; \vec X \times \mathbf{p} \;=\; \overrightarrow{CM}\times\mathbf{p},
\qquad
\sigma_C^1 = X^2p^3 - X^3p^2,\quad \sigma_C^2 = X^3p^1 - X^1p^3,\quad \sigma_C^3 = X^1p^2 - X^2p^1,
$$
the cross product in the rest space, and the time-space components form the **mass-energy dipole moment** contribution $E\,\vec X - h\,\mathbf{p}$. In matrix form, relative to an orthonormal frame $(\vec e_\alpha)$ of the observer with $\vec e_0 = U_0$,
$$
(J_{\alpha\beta}) =
\begin{pmatrix}
0 & E X^1 - h p^1 & E X^2 - h p^2 & E X^3 - h p^3\\
-(E X^1 - h p^1) & 0 & \sigma_C^3 & -\sigma_C^2\\
-(E X^2 - h p^2) & -\sigma_C^3 & 0 & \sigma_C^1\\
-(E X^3 - h p^3) & \sigma_C^2 & -\sigma_C^1 & 0
\end{pmatrix}.
$$
The structure is identical to that of the electromagnetic field tensor $F_{\mu\nu}$: the time-space block is "electric" (the mass-energy dipole, the analogue of $\mathbf{E}$) and the space-space block is "magnetic" (the angular momentum vector, the analogue of $\mathbf{B}$).

For a **system** $\mathscr{S}$ of particles with worldlines $\mathscr{L}_a$ and four-momenta $p_a$, evaluated on a spacelike hypersurface $\Sigma$ that each worldline meets once at $M_a$, the angular momentum is the sum
$$
J_C\big|_\Sigma \;=\; \sum_a \overrightarrow{CM_a}^\flat \wedge p_a(M_a),
$$
again an antisymmetric two-form.

---

# Categorical / Structural Definition

The angular momentum tensor is an element of $\Lambda^2 V^*$, the space of **alternating two-forms** on the model vector space $V$ of Minkowski space (equivalently, raising indices, of $\Lambda^2 V$, the antisymmetric two-tensors). It is the image of the pair $(\overrightarrow{CM}^\flat, p)$ under the canonical antisymmetrisation map
$$
\wedge : V^*\times V^* \longrightarrow \Lambda^2 V^*,
\qquad (a,b)\longmapsto a\otimes b - b\otimes a,
$$
which is the universal bilinear alternating map out of $V^*\times V^*$ — the defining [[Thm - Universal Property of the Tensor Product|universal property]] of the [[Def - Tensor Product of Vector Spaces|exterior power]] $\Lambda^2 V^*$ as the quotient of $V^*\otimes V^*$ by the symmetric two-tensors. Concretely, $\Lambda^2 V^*$ is six-dimensional with basis $\{e^\alpha\wedge e^\beta : \alpha < \beta\}$, the six coordinate planes, and $J_C = x_\alpha p_\beta\, e^\alpha\wedge e^\beta$ (sum over $\alpha < \beta$).

This places relativistic angular momentum in the same categorical box as the electromagnetic field two-form $F$ and as the area element $dx\wedge dy$ of integration: all three are sections of (or values in) the second exterior power, the universal recipient of antisymmetric bilinear data. The Lorentz group acts on $\Lambda^2 V^*$ by the induced representation $\Lambda^2\rho$, and under the proper orthochronous subgroup this six-dimensional representation splits into two three-dimensional complex pieces, the self-dual and anti-self-dual two-forms — the same splitting that, for the field tensor, organises $\mathbf{E}\pm i\mathbf{B}$. The angular momentum tensor is thus not merely *analogous* to the field tensor; it lives in the identical representation of the Lorentz group, which is the structural reason every decomposition theorem transfers between them.

---

# Relate to Other Fields / Compression

This is, in pure mathematics, the **wedge of a one-form with a vector** — the simplest nonzero element of an exterior algebra built from two given pieces of data. In differential geometry the same construction $X^\flat\wedge p$ appears whenever one antisymmetrises a position against a momentum, for instance in the symplectic form of phase space; in the mechanics of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]] the angular momentum map of the rotation group is exactly this antisymmetrisation, the moment map for the $SO(3)$ (here $SO(1,3)$) action.

In physics it is the **mechanical analogue of the electromagnetic field strength**. Both are antisymmetric two-forms; both split, relative to an observer, into an "electric" rest-space vector and a "magnetic" rest-space vector; both have the same pair of Lorentz invariants. The dictionary is $\mathbf{E}\leftrightarrow\vec D$ (mass-energy dipole) and $\mathbf{B}\leftrightarrow\vec\sigma$ (angular momentum vector). This is why a physicist who has internalised how a boost mixes $\mathbf{E}$ and $\mathbf{B}$ already knows how a boost mixes the mass-energy dipole and the angular momentum vector.

**True name:** the operational characterisation, more useful than "$\overrightarrow{CM}^\flat\wedge p$", is *the unique antisymmetric tensor whose space-space block is $\mathbf{r}\times\mathbf{p}$ and that is conserved for a free particle*. When you need to recognise or reconstruct it, do not memorise the wedge — remember that angular momentum in four dimensions is the antisymmetric tensor extension of $\mathbf{r}\times\mathbf{p}$, antisymmetrised because antisymmetry is what conservation demands, and tensor-valued because $\binom 42 = 6 \ne 4$ kills the vector disguise.

---

# Examples / Corollaries

**Is an instance — a free particle's angular momentum about the origin.** A particle of four-momentum $p^\alpha = (E,\mathbf{p})$ at event $x^\alpha = (t,\mathbf{r})$ has $J^{0i} = t p^i - x^i E$ and $J^{ij} = x^ip^j - x^jp^i$. The spatial block $J^{ij}$ is the ordinary angular momentum $\mathbf{r}\times\mathbf{p}$; the mixed block $J^{0i} = tp^i - x^iE$ is the mass-energy dipole, which for a free particle equals $-(x^i - v^i t)E$ where $\mathbf{v} = \mathbf{p}/E$ — proportional to the displacement of the particle from where it would be at $t=0$, weighted by energy.

**Is an instance — a photon's angular momentum.** A [[Def - The Four-Momentum of a Photon|photon]] has null $p$, $p\cdot p = 0$, but its angular momentum tensor $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$ is defined exactly as for a massive particle. The construction requires no mass and no four-velocity — it is built from position and momentum alone — which is why it applies to massless particles where $P = mU$ fails.

**Is NOT an instance — a putative angular momentum four-vector.** The expression $L^\mu = \epsilon^{\mu\nu\rho\sigma}x_\nu p_\rho U_\sigma$ is *not* "the angular momentum as a vector"; it is a derived quantity (essentially the spin part contracted with a four-velocity), and without the four-velocity $U_\sigma$ the formula $\epsilon^{\mu\nu\rho\sigma}x_\nu p_\rho$ has a free index and is not even a vector. There is no four-vector carrying the full six components of angular momentum — the antisymmetric tensor is irreducibly six-dimensional. Mistaking $J^{\alpha\beta}$ for a vector is the cardinal error the definition exists to prevent.

**Is NOT an instance — the symmetric moment.** The tensor $x^\alpha p^\beta + x^\beta p^\alpha$ is built from the same data but is *not* an angular momentum: it is symmetric, so its space-space block is not a cross product, and it is not conserved for a free particle (its proper-time derivative is $cU^\alpha p^\beta + cp^\alpha U^\beta$, nonzero). Only the antisymmetric part deserves the name.

**Corollary — the angular momentum vector is a cross product.** Contracting the spatial block with the Levi-Civita symbol, $\sigma_C^i = \tfrac12\epsilon^{ijk}J_{jk} = (\overrightarrow{CM}\times\mathbf{p})^i$, recovers the rest-space cross product. This is the calibration that the tensor really does generalise $\mathbf{r}\times\mathbf{p}$.

**Corollary — change of reference point.** From the definition, replacing $C$ by $C'$ gives $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge p$ for a particle (and with $P$ the total momentum for a system), because $\overrightarrow{C'M} = \overrightarrow{C'C} + \overrightarrow{CM}$ and the wedge is bilinear. The change vanishes iff $\overrightarrow{C'C}\parallel p$ or $p = 0$.

**Calibration check.** You should be able to: (1) write out $J^{12}$ for a particle at $(t,x,y,z)$ with momentum $(E,p_x,p_y,p_z)$ and recognise it as $xp_y - yp_x$, the $z$-component of $\mathbf{r}\times\mathbf{p}$; (2) verify that $J^{\alpha\beta}$ has exactly six independent components by antisymmetry; and (3) confirm that under a boost along $x$, the components $J^{02}$ and $J^{12}$ mix the way $E_y$ and $B_z$ would for the field tensor, by applying $J'^{\alpha\beta} = \Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu J^{\mu\nu}$.

---

# Unlocked by This

> [!tip] The Pauli–Lubanski Vector and Wigner's Classification *(from Quantum Field Theory)*
> Contracting the angular momentum tensor with the four-momentum through the Levi-Civita tensor produces the [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] $W^\mu = -\tfrac12\epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$, whose square is the second **Casimir invariant** of the Poincaré group. Together with $P^2 = m^2$, the invariant $W^2 = -m^2 s(s+1)$ labels every irreducible representation, and Wigner's theorem identifies these representations with elementary particles. The full six-component tensor $J^{\alpha\beta}$ generates the Lorentz subalgebra; the spin part it contains, distilled through $W^\mu$, is the relativistic **spin** of the particle.

> [!tip] The Energy–Momentum Tensor's Angular Momentum Current *(from Field Theory and General Relativity)*
> For a continuous system the discrete sum $\sum_a\overrightarrow{CM_a}^\flat\wedge p_a$ becomes an integral of an **angular momentum current** $M^{\lambda\mu\nu} = x^\mu T^{\lambda\nu} - x^\nu T^{\lambda\mu}$ built from the **energy-momentum tensor** $T^{\mu\nu}$ of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]]. Conservation of angular momentum, $\partial_\lambda M^{\lambda\mu\nu} = 0$, holds precisely when $T^{\mu\nu}$ is symmetric — the symmetry of the energy-momentum tensor *is* the local conservation of angular momentum, a fact that becomes structural in general relativity where $T^{\mu\nu}$ sources the metric.
