---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - Local Frame"
tags: [geometry, gauge-theory, holonomy, parallel-transport]
---

# Notation

$E \to M$ is a smooth (real or complex) vector bundle with a connection $\nabla$ (see [[Def - Connection on a Vector Bundle]]) and local connection 1-form $\omega$ in a chosen frame. $\gamma : [0, 1] \to M$ is a smooth (or piecewise smooth) curve with endpoints $\gamma(0) = p$ and $\gamma(1) = q$. The **parallel transport** along $\gamma$ is denoted $P_\gamma : E_p \to E_q$. For closed loops ($p = q$), the **holonomy** is $\mathrm{Hol}_p(\gamma) = P_\gamma \in \mathrm{GL}(E_p)$. The **Wilson line** $W_\gamma$ is the matrix of $P_\gamma$ in a chosen frame, $W_\gamma = \mathcal{P}\exp\bigl(-\int_\gamma\omega\bigr)$ where $\mathcal{P}$ denotes path-ordering. For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

The motivating question is: **given a connection on $E \to M$, how do you compare vectors in different fibres along a path?** A connection differentiates sections — it tells you the rate of change of a section in a given direction. But for many purposes you want the *finite* version: not "the rate of change of $\sigma$ as you move from $p$", but "what does it mean for a vector at $p$ to be 'the same' as a vector at $q$, when $q$ is far from $p$, with comparison made along a specific path $\gamma$?".

The answer is **parallel transport**. A section $\sigma$ along $\gamma$ is *parallel* if $\nabla_{\dot\gamma}\sigma = 0$ everywhere along $\gamma$ — it has zero covariant derivative in the direction of the path. This is a first-order linear ODE in $t$: at each point $\gamma(t)$, $\sigma(t) \in E_{\gamma(t)}$, and the equation $\nabla_{\dot\gamma}\sigma = 0$ is a linear constraint on the rate of change of $\sigma$'s components. Given an initial vector $v_0 \in E_p$, the ODE has a unique solution $\sigma : [0, 1] \to E$ with $\sigma(t) \in E_{\gamma(t)}$ and $\sigma(0) = v_0$, and the value $\sigma(1) \in E_q$ is the **parallel transport** of $v_0$ along $\gamma$.

Why does this define a *linear map*? Because the ODE is linear: if $v_0$ and $v_0'$ both parallel-transport to $v_1$ and $v_1'$, then $av_0 + bv_0'$ parallel-transports to $av_1 + bv_1'$ (just sum the solutions). The parallel transport $P_\gamma : E_p \to E_q$ is therefore a linear map between the fibres.

Why is it an *isomorphism*? Because you can run time backwards: the parallel transport along $\gamma^{-1}$ (the reversed path) from $q$ to $p$ is the inverse linear map $P_\gamma^{-1}$. The composition $P_\gamma \circ P_{\gamma^{-1}} = \mathrm{id}$ by uniqueness of the ODE solution. So $P_\gamma$ is in $\mathrm{Iso}(E_p, E_q)$, equivalently, $P_\gamma \in \mathrm{GL}(K)$ after choosing bases.

For a *closed* loop ($p = q$), $P_\gamma \in \mathrm{GL}(E_p)$ — the parallel transport is an automorphism of the single fibre. This is the **holonomy** of $\nabla$ around $\gamma$. The collection of all holonomies, for all loops based at $p$, forms a subgroup $\mathrm{Hol}_p(\nabla) \subseteq \mathrm{GL}(E_p)$ — the **holonomy group** of the connection at $p$. Its structure encodes much of the geometry: a flat connection has discrete (or zero-dimensional) holonomy on simply-connected manifolds; the Levi-Civita connection on a generic Riemannian manifold has full holonomy $O(n)$; *special holonomy* (proper subgroups like $U(n) \subset O(2n)$ for Kähler, $\mathrm{Sp}(n) \subset O(4n)$ for hyperkähler) corresponds to extra geometric structure.

Why call this a **Wilson line**? Kenneth Wilson introduced this object into physics in the 1970s in the context of lattice gauge theory, where it became the basic non-perturbative observable: in QCD, the Wilson loop around a closed contour measures the area-law behaviour of the chromoelectric flux ("Wilson area law" being the confinement criterion). The name "Wilson line" emphasizes the gauge-theoretic perspective (parallel transport as a physical observable in a gauge theory), while "parallel transport" emphasizes the differential-geometric perspective. Both refer to the same mathematical object.

Why is the formula a **path-ordered exponential**? Because the ODE $\nabla_{\dot\gamma}\sigma = 0$ in components reads $\frac{d\sigma}{dt} + \omega(\dot\gamma(t))\sigma(t) = 0$, a linear first-order matrix ODE. The solution is $\sigma(t) = \mathcal{P}\exp\bigl(-\int_0^t\omega(\dot\gamma)\,ds\bigr)\sigma(0)$, where the path-ordering symbol $\mathcal{P}$ is needed because the matrices $\omega(\dot\gamma(t))$ at different times generally do not commute. For abelian connections like $U(1)$, the path-ordering is unnecessary (all the $\omega$'s commute, being scalars) and the formula reduces to $\sigma(t) = e^{-\int_0^t\omega(\dot\gamma)\,ds}\sigma(0)$.

---

# The Definition

Let $\nabla$ be a connection on a smooth vector bundle $E \to M$ and let $\gamma : [0, 1] \to M$ be a smooth (or piecewise smooth) curve.

**Parallel transport.** Given $v_0 \in E_{\gamma(0)}$, there is a unique smooth section $\sigma : [0, 1] \to E$ with $\sigma(t) \in E_{\gamma(t)}$ for all $t$, satisfying

$$\nabla_{\dot\gamma(t)}\sigma(t) = 0, \qquad \sigma(0) = v_0.$$

The **parallel transport** along $\gamma$ is the linear map

$$P_\gamma : E_{\gamma(0)} \to E_{\gamma(1)}, \qquad v_0 \mapsto \sigma(1).$$

$P_\gamma$ is a linear isomorphism with inverse $P_{\gamma^{-1}}$.

**Wilson line.** Choose a local frame $(e_\alpha)$ for $E$ along (a neighbourhood of) $\gamma$, and let $\omega$ be the connection 1-form in this frame. The **Wilson line** is the matrix of $P_\gamma$ in this frame:

$$\boxed{W_\gamma := \mathcal{P}\exp\Bigl(-\int_\gamma\omega\Bigr) = \mathcal{P}\exp\Bigl(-\int_0^1\omega(\dot\gamma(t))\,dt\Bigr).}$$

Here $\omega(\dot\gamma(t)) \in \mathrm{End}(E_{\gamma(t)})$ is the connection 1-form contracted with the velocity, and $\mathcal{P}$ denotes **path-ordering**: for a partition $0 = t_0 < t_1 < \dots < t_n = 1$ and $\Delta t_k = t_k - t_{k-1}$,

$$W_\gamma = \lim_{\Delta t \to 0}\prod_{k=n}^1\bigl(I - \omega(\dot\gamma(t_k))\Delta t_k\bigr) = \lim_{n \to \infty}\Bigl[I - \omega(\dot\gamma(t_n))\Delta t_n\Bigr]\cdots\Bigl[I - \omega(\dot\gamma(t_1))\Delta t_1\Bigr],$$

with later times to the left (the product is *ordered* from right to left, with $t = 1$ leftmost).

**Holonomy.** For a *closed* loop $\gamma$ based at $p$ (so $\gamma(0) = \gamma(1) = p$), the parallel transport $P_\gamma : E_p \to E_p$ is an automorphism of $E_p$. The **holonomy** of $\nabla$ around $\gamma$ at $p$ is

$$\mathrm{Hol}_p(\gamma) := P_\gamma \in \mathrm{GL}(E_p).$$

The **holonomy group** of $\nabla$ at $p$ is

$$\mathrm{Hol}_p(\nabla) := \{P_\gamma : \gamma \text{ a piecewise smooth loop based at } p\} \subseteq \mathrm{GL}(E_p).$$

It is a Lie subgroup of $\mathrm{GL}(E_p)$ (the *Ambrose-Singer theorem* identifies its Lie algebra with the span of all values of the curvature 2-form at all points reachable from $p$).

**Abelian special case.** For an abelian structure group (e.g., $U(1)$), the path-ordering is trivial since all $\omega(\dot\gamma(t))$ values commute. The Wilson line becomes simply

$$W_\gamma = \exp\Bigl(-\int_\gamma\omega\Bigr),$$

and for closed loops the holonomy is $\mathrm{Hol}(\gamma) = \exp\bigl(-\oint_\gamma\omega\bigr)$. With the EM dictionary $\omega = -(ie/\hbar)A$, this gives

$$\mathrm{Hol}_{\mathrm{EM}}(\gamma) = \exp\Bigl(\tfrac{ie}{\hbar}\oint_\gamma A\Bigr).$$

For a closed surface $\Sigma$ with $\partial\Sigma = \gamma$, Stokes' theorem (when applicable — the surface must lie in the domain of $A$) gives the alternative expression $\oint_\gamma A = \int_\Sigma F$, so

$$\mathrm{Hol}_{\mathrm{EM}}(\gamma) = \exp\Bigl(\tfrac{ie}{\hbar}\int_\Sigma F\Bigr).$$

---

# Categorical / Structural Definition

In the language of *parallel-transport functors*, a connection on $E \to M$ is a **smooth functor** $\mathcal{P} : \mathrm{Path}(M) \to \mathrm{Iso}_{\mathrm{Vec}}$ from the **path groupoid** of $M$ (objects are points of $M$, morphisms are paths up to thin homotopy, composition by concatenation, inverses by reversal) to the groupoid of vector spaces and isomorphisms. The functor sends a point $p$ to $E_p$ and a path $\gamma : p \to q$ to $P_\gamma : E_p \to E_q$. Holonomy is the restriction to the *loop groupoid* (objects are points, morphisms are loops at that point), giving a homomorphism $\pi_1(M, p) \to \mathrm{GL}(E_p)$ when the connection is *flat* (and more generally a "non-flat" version when curvature is present).

For flat connections, holonomy is *homotopy-invariant*: $\mathrm{Hol}_p(\gamma_1) = \mathrm{Hol}_p(\gamma_2)$ whenever $\gamma_1$ and $\gamma_2$ are homotopic loops based at $p$. So a flat connection on a connected manifold $M$ is determined (up to gauge) by its holonomy representation $\rho : \pi_1(M, p) \to \mathrm{GL}(K)$. This is the basis of the **Riemann-Hilbert correspondence**: flat connections on $M$ are in bijection with representations of $\pi_1(M)$.

For general (non-flat) connections, the **Ambrose-Singer theorem** says the Lie algebra of the holonomy group $\mathrm{Hol}_p$ is the span of all values of the curvature $F(X, Y)$ at all points reachable from $p$, regarded as elements of $\mathrm{End}(E_p)$ via parallel transport. This makes precise the slogan **"curvature is the infinitesimal generator of holonomy"**.

---

# Relate to Other Fields / Compression

The Wilson line / holonomy is **"the basic gauge-invariant observable of a connection"**.

**In quantum field theory**, Wilson loops $\mathrm{tr}\,W_\gamma$ around closed contours are the basic gauge-invariant operators of non-abelian gauge theory. In QCD, the expectation value of a large rectangular Wilson loop decays exponentially in its area (the **Wilson area law**) — this is the criterion for quark confinement, and the qualitative behaviour distinguishing the confining from the Higgs phase of a gauge theory. In **lattice gauge theory**, all gauge-invariant operators are products of Wilson lines along edges of the lattice.

**In quantum mechanics**, the Aharonov-Bohm phase is the holonomy of the EM connection around a loop encircling a magnetic flux tube — a directly observable physical phase. The **Berry phase** of an adiabatically transported quantum system is the holonomy of the **Berry connection** (a $U(1)$-connection on the line bundle of energy eigenstates) over the parameter loop traced out. Both are special cases of the general holonomy concept.

**In Riemannian geometry**, the holonomy of the Levi-Civita connection on a Riemannian manifold encodes the local geometry. **Special holonomy** — when $\mathrm{Hol} \subset O(n)$ is a proper Lie subgroup like $U(n)$ (Kähler), $SU(n)$ (Calabi-Yau), $\mathrm{Sp}(n)$ (hyperkähler), $G_2$ or $\mathrm{Spin}(7)$ — corresponds to extra geometric structure, classified by **Berger's theorem**.

**In topology**, the *parallel-transport functor* of a flat connection gives the **monodromy representation** $\pi_1(M) \to \mathrm{GL}(K)$, which classifies covering spaces and local systems. The bridge between connections and topology is the **Riemann-Hilbert correspondence**.

**True name:** The Wilson line is **"the finite version of the covariant derivative"** — it tells you not the rate of change of a section, but the actual transport law for vectors along curves. It is the *integrated* form of the connection, and for gauge theory it is the basic observable.

---

# Examples / Corollaries

**Is an instance: Trivial connection on $M \times \mathbb{R}^K$.** With $\omega = 0$ in the standard frame, the parallel-transport ODE is $d\sigma/dt = 0$, so $\sigma$ is constant in components. Parallel transport is the identity in components, holonomy is trivial for every loop, $\mathrm{Hol}_p = \{I\}$.

**Is an instance: Levi-Civita connection on a sphere $S^2$.** Walk a tangent vector around a small geodesic triangle on $S^2$ with the round metric. The vector returns rotated by the angle equal to the area enclosed times the Gaussian curvature ($K = 1$ for unit sphere). For a large triangle with three right angles (one octant of $S^2$), the vector returns rotated by $\pi/2$. The holonomy group of $S^2$ at any point is the full $SO(2)$.

**Is an instance: EM connection around a magnetic flux tube.** Take $A = \frac{\Phi}{2\pi}d\phi$ on $\mathbb{R}^3 \setminus \{z\text{-axis}\}$ (an Aharonov-Bohm solenoid with flux $\Phi$). The holonomy of the EM connection around a loop encircling the $z$-axis once is $\exp\bigl((ie/\hbar)\oint A\bigr) = \exp\bigl((ie/\hbar)\Phi\bigr)$. This is the **Aharonov-Bohm phase**, observable in interference experiments. See [[Ex - The Aharonov-Bohm Phase from the Magnetic Solenoid]].

**Is an instance: Hopf line bundle holonomy.** On the Dirac monopole bundle $L_g$ over $S^2$, the holonomy around the equator is $\exp\bigl((ie/\hbar)\oint_{\mathrm{eq}}A\bigr)$ for either patch's $A$. Using $A_N = g(1 - \cos\theta)d\phi$ at $\theta = \pi/2$: $A_N = g\,d\phi$, so $\oint A_N = 2\pi g$, giving holonomy $e^{2\pi i eg/\hbar}$. For the bundle to exist (Dirac quantization $2eg/\hbar \in \mathbb{Z}$), this is $e^{i\pi n}$ for integer $n = 2eg/\hbar$.

**Is an instance: Non-trivial holonomy on a flat torus.** Take $M = T^2 = \mathbb{R}^2/\mathbb{Z}^2$ with the trivial line bundle and connection $\omega = i\alpha\,dx + i\beta\,dy$ for constants $\alpha, \beta$. The connection is flat ($d\omega = 0$). Holonomy around the two generators of $\pi_1(T^2) = \mathbb{Z}^2$ is $e^{i\alpha}$ and $e^{i\beta}$ respectively. The space of flat $U(1)$-connections modulo gauge on $T^2$ is therefore $U(1)^2 = T^2$ itself, the **Jacobian variety**.

**Is NOT an instance: An operator that violates the parallel-transport ODE.** A linear map $E_p \to E_q$ that does not arise from solving $\nabla_{\dot\gamma}\sigma = 0$ along some path is not a parallel transport — for example, a *random* unitary in $U(K)$ has no geometric meaning relative to $\nabla$ unless it happens to equal $P_\gamma$ for some $\gamma$.

**Corollary (gauge transformation of Wilson line).** Under a gauge transformation $\omega \to g\omega g^{-1} + dg\,g^{-1}$, the Wilson line transforms as $W_\gamma \to g(\gamma(1)) W_\gamma g(\gamma(0))^{-1}$. For a closed loop $\gamma$ (so $\gamma(0) = \gamma(1)$): $W_\gamma \to g(p) W_\gamma g(p)^{-1}$, i.e., by conjugation. Hence $\mathrm{tr}\,W_\gamma$ is gauge-invariant — the basis for Wilson loops as physical observables.

**Corollary (holonomy is homotopy-invariant for flat connections).** If $\nabla$ is flat ($F = 0$) and $\gamma_1, \gamma_2$ are homotopic loops based at $p$, then $\mathrm{Hol}_p(\gamma_1) = \mathrm{Hol}_p(\gamma_2)$. This gives a well-defined homomorphism $\pi_1(M, p) \to \mathrm{Hol}_p(\nabla) \subseteq \mathrm{GL}(E_p)$, the **monodromy representation**. Flat connections on connected $M$ are classified (up to gauge) by such representations modulo conjugation.

**Corollary (curvature controls infinitesimal holonomy).** For a small loop $\gamma_{s, t}$ enclosing an area-element of size $st$ spanned by vectors $X, Y$, the holonomy is $\mathrm{Hol}(\gamma_{s, t}) = I + st\,F(X, Y) + O(s^2 + t^2)$. This is the precise sense in which $F$ is "infinitesimal holonomy per unit area". The **Ambrose-Singer theorem** integrates this: the Lie algebra of $\mathrm{Hol}_p$ is the span of all such $F(X, Y)$ at all points reachable from $p$.

**Calibration check.** (1) For the trivial connection, verify that the path-ordered exponential of $0$ is the identity: $\mathcal{P}\exp(0) = I$. ✓ (2) For an abelian connection, verify that the holonomy around a loop bounding a disc $\Sigma$ equals $\exp(-\int_\Sigma F)$ by Stokes' theorem applied to $\oint_\gamma\omega = \int_\Sigma d\omega = \int_\Sigma F$ (since abelian $\omega \wedge \omega = 0$). ✓ (3) On $S^2$ with the Levi-Civita connection, compute the holonomy of a triangle with three right angles — answer: $\pi/2$ rotation, matching $\int\int K\,dA = \pi/2$ for one-eighth of a unit sphere.

---

# Unlocked by This

> [!tip] Ambrose-Singer Theorem and Special Holonomy *(from Differential Geometry)*
> The **Ambrose-Singer theorem** identifies the Lie algebra $\mathfrak{hol}_p(\nabla)$ of the holonomy group with the span of $\{P_\sigma^{-1}F(X, Y)P_\sigma\,|\,X, Y \in T_qM, \sigma \text{ a path from } p \text{ to } q\}$. So curvature determines holonomy. For Riemannian manifolds, **Berger's theorem** classifies the possible holonomy groups of a generic, irreducible, non-symmetric Riemannian manifold: the only options beyond the full $SO(n)$ are $U(n) \subset SO(2n)$ (Kähler), $SU(n)$ (Calabi-Yau), $\mathrm{Sp}(n) \subset SO(4n)$ (hyperkähler), $\mathrm{Sp}(n) \cdot \mathrm{Sp}(1)$ (quaternionic Kähler), $G_2 \subset SO(7)$, and $\mathrm{Spin}(7) \subset SO(8)$. Each of these special holonomies corresponds to a rich geometric structure on the manifold.

> [!tip] Wilson Loops and Confinement *(from Quantum Field Theory)*
> The vacuum expectation value of a Wilson loop in lattice QCD displays the **area law** $\langle\mathrm{tr}\,W_\gamma\rangle \sim e^{-\sigma\,\mathrm{Area}(\gamma)}$ for large loops in the confining phase (with $\sigma$ the **string tension**), versus the **perimeter law** $\sim e^{-\sigma'\,\mathrm{Perimeter}(\gamma)}$ in the Higgs/Coulomb phase. The transition between these regimes is the **confinement-deconfinement phase transition** of pure gauge theory, of central importance to understanding the QCD vacuum. The Wilson loop is therefore not just a mathematical curiosity but the basic non-perturbative order parameter of gauge theory.

> [!tip] Riemann-Hilbert Correspondence *(from Algebraic Geometry and Mathematical Physics)*
> Flat connections on a complex manifold $X$ are in bijection with representations of $\pi_1(X)$ via the monodromy. More precisely, the **Riemann-Hilbert correspondence** establishes an equivalence between regular holonomic $\mathcal{D}$-modules on $X$ and perverse sheaves on $X$, of which "flat connections $\leftrightarrow$ representations" is the basic case. This is the framework in which one studies **Gauss-Manin connections** (connections on cohomology bundles of families of varieties), **mixed Hodge structures**, and the **Hodge theory of period maps**. In conformal field theory, the **Knizhnik-Zamolodchikov connection** is a flat connection on moduli spaces whose monodromy gives the braid-group representations defining quantum groups.
