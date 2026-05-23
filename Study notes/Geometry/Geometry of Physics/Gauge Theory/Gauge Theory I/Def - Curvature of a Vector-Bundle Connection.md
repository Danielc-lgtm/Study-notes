---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
tags: [geometry, gauge-theory, curvature]
---

# Notation

$E \to M$ is a smooth (real or complex) vector bundle of rank $K$ with a connection $\nabla$ (see [[Def - Connection on a Vector Bundle]]). For $X, Y \in \mathfrak{X}(M)$ and $\sigma \in \Gamma(E)$, $\nabla_X\sigma \in \Gamma(E)$ is the covariant derivative; $[X, Y]$ is the [[Def - The Lie Bracket of Vector Fields|Lie bracket]] of vector fields. We write $\omega = (\omega^\alpha{}_\beta)$ for the connection 1-form matrix in a local frame, $F = (F^\alpha{}_\beta)$ for the curvature 2-form matrix. The wedge product of matrix-valued forms $\omega \wedge \omega$ is defined entry by entry: $(\omega \wedge \omega)^\alpha{}_\beta = \omega^\alpha{}_\gamma \wedge \omega^\gamma{}_\beta$ (note the matrix product). For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

The motivating question is: **does parallel transport remember the path, or only the endpoints?** Given a connection $\nabla$ on $E$ and two paths $\gamma_1, \gamma_2$ from $p$ to $q$, you can parallel-transport a vector $v_0 \in E_p$ along each, arriving at two vectors $v_1, v_2 \in E_q$. In general $v_1 \ne v_2$ — the connection has *holonomy*. The first question is whether you can detect this path-dependence *locally*, by infinitesimal probing, without going around large loops.

Here is the experiment. Take two commuting vector fields $X, Y$ on $M$ with flows $\phi^X_s, \phi^Y_t$. Build a small closed parallelogram by following $X$ for time $s$, then $Y$ for time $t$, then $-X$ for time $s$, then $-Y$ for time $t$. Parallel-transport $v_0 \in E_p$ around this loop and look at the result $v_{st} \in E_p$. If parallel transport is path-independent, $v_{st} = v_0$ for all $s, t$. If not, the deviation $v_{st} - v_0$ measures the path-dependence on this particular loop. Expanding in $s, t$, the leading term is $st \cdot R(X, Y)v_0 + O(s^2 + t^2)$ for some bilinear operator $R(X, Y) : E_p \to E_p$. This operator $R(X, Y)$ — the **curvature** — is the infinitesimal generator of the path-dependence.

The formula $R(X, Y)v = \nabla_X\nabla_Yv - \nabla_Y\nabla_Xv$ has the right meaning when $[X, Y] = 0$: each successive parallel transport corresponds to a covariant derivative, and the *difference* between transporting "$X$ then $Y$" versus "$Y$ then $X$" is the commutator $[\nabla_X, \nabla_Y] = \nabla_X\nabla_Y - \nabla_Y\nabla_X$. But for non-commuting $X, Y$ the parallelogram closes only modulo $st \cdot [X, Y]$, and we need to subtract the parallel-transport contribution along this closure to get a pure-curvature answer. That correction is exactly $\nabla_{[X, Y]}v$. The full formula is therefore:

$$\boxed{F(X, Y)\sigma := \nabla_X\nabla_Y\sigma - \nabla_Y\nabla_X\sigma - \nabla_{[X, Y]}\sigma.}$$

Why all three terms? Drop $\nabla_{[X, Y]}$ and the formula fails to be $C^\infty(M)$-bilinear in $X, Y$: replacing $X$ by $fX$ for a function $f$ generates extra terms $(Yf)\nabla_X$ that do not cancel. The $\nabla_{[X, Y]}$ piece soaks these up precisely because $[fX, Y] = f[X, Y] - (Yf)X$. With all three terms, $F(X, Y)\sigma$ is $C^\infty(M)$-linear in each of $X, Y, \sigma$ separately — this is the content of [[Thm - Curvature is C-Infinity Linear in Sections]], and is what makes $F$ a *tensor*, evaluable pointwise rather than depending on the field's behaviour in a neighbourhood.

Why care about *tensoriality*? Because a tensor has a value at every point that depends only on values at that point. The curvature $F$ thus defines an honest section of $\Lambda^2 T^*M \otimes \mathrm{End}(E)$ — an $\mathrm{End}(E)$-valued 2-form on $M$. It is a local geometric invariant of the connection; you can integrate it over surfaces (giving Chern numbers), contract it with itself (giving curvature scalars and Yang-Mills Lagrangians), or use it to detect non-triviality of the bundle (a non-zero curvature obstructs the existence of a flat connection).

What does this definition exclude? A naïve "discrepancy between $\nabla_X\nabla_Y$ and $\nabla_Y\nabla_X$" (without the bracket term) would not be tensorial, hence not a globally defined geometric object. A "deviation from flatness" defined only on simply-connected charts (without the global tensoriality) would not assemble into a class. The three-term formula is forced once you demand a *single global tensor* measuring the connection's failure to be flat.

The frame-version $F = d\omega + \omega \wedge \omega$ is the same formula expressed in a local trivialization. The $d\omega$ part is "differentiate the connection 1-form" (the analogue of $\partial_X\partial_Y - \partial_Y\partial_X$, which equals zero for ordinary partials — but $\omega$ is non-zero, so $d\omega$ captures one source of non-commutativity). The $\omega \wedge \omega$ part is the *non-abelian correction*: $\omega^\alpha{}_\gamma \wedge \omega^\gamma{}_\beta$ does not vanish unless the matrix entries commute, and this matrix non-commutativity is what makes Yang-Mills theory non-linear. For abelian structure groups like $U(1)$ all matrix entries are scalars and $\omega \wedge \omega = 0$, leaving $F = d\omega$ — the electromagnetic field strength as the exterior derivative of the potential.

---

# The Definition

Let $\nabla$ be a connection on a smooth vector bundle $E \to M$. The **curvature** of $\nabla$ is the operator $F : \mathfrak{X}(M) \times \mathfrak{X}(M) \times \Gamma(E) \to \Gamma(E)$ defined by

$$F(X, Y)\sigma := \nabla_X\nabla_Y\sigma - \nabla_Y\nabla_X\sigma - \nabla_{[X, Y]}\sigma.$$

**Tensoriality.** $F(X, Y)\sigma$ is $C^\infty(M)$-linear in each of $X$, $Y$, $\sigma$ separately (see [[Thm - Curvature is C-Infinity Linear in Sections]]). Hence $F$ defines a section of $\Lambda^2 T^*M \otimes \mathrm{End}(E)$ — an $\mathrm{End}(E)$-valued 2-form on $M$:

$$F \in \Omega^2(M; \mathrm{End}(E)) := \Gamma(\Lambda^2 T^*M \otimes \mathrm{End}(E)).$$

**Antisymmetry.** $F(X, Y) = -F(Y, X)$ by inspection.

**Local frame description (the structure equation).** Let $(e_\alpha)$ be a local frame for $E$ on $U$, and let $\omega = (\omega^\alpha{}_\beta)$ be the connection 1-form matrix: $\nabla e_\beta = e_\alpha \otimes \omega^\alpha{}_\beta$. Then the curvature 2-form matrix $F = (F^\alpha{}_\beta)$ is given by **Cartan's second structure equation**:

$$\boxed{F = d\omega + \omega \wedge \omega,}$$

componentwise $F^\alpha{}_\beta = d\omega^\alpha{}_\beta + \omega^\alpha{}_\gamma \wedge \omega^\gamma{}_\beta$. Acting on the frame: $F(e_\beta) = e_\alpha \otimes F^\alpha{}_\beta$.

**Change-of-frame transformation.** Under $e_V = e_U c_{UV}$, the curvature 2-form transforms as a **tensor by conjugation**:

$$F_V = c_{UV}^{-1}\,F_U\,c_{UV}.$$

The inhomogeneous $c^{-1}dc$ term that plagues $\omega$ is *absent* in the transformation of $F$ — this is exactly the statement that $F$ is a tensor. The trace $\mathrm{tr}(F^k)$ is therefore a globally defined $2k$-form, the basis of characteristic classes.

**Abelian special case.** If the structure group is abelian (e.g., $U(1)$, $\mathrm{GL}(1, \mathbb{C}) = \mathbb{C}^\times$, $\mathbb{R}^\times$), then the $\omega^\alpha{}_\gamma \wedge \omega^\gamma{}_\beta$ wedge in the structure equation vanishes (commuting 1-forms wedge to zero), giving simply $F = d\omega$. The curvature is *exact* in any trivializing patch.

---

# Categorical / Structural Definition

The curvature is the **failure of $\nabla$ to be a chain map** in the de Rham complex with coefficients in $E$. Extend $\nabla$ to $E$-valued forms via $d_\nabla(\sigma \otimes \alpha) := \nabla\sigma \wedge \alpha + \sigma \otimes d\alpha$. The operator $d_\nabla : \Omega^k(M; E) \to \Omega^{k+1}(M; E)$ would be a differential (i.e., $d_\nabla^2 = 0$) if $\nabla$ were "ordinary differentiation" — but it is not, and $d_\nabla^2\sigma = F \wedge \sigma$ for any section $\sigma$. The curvature 2-form $F$ is therefore $d_\nabla^2 = F \wedge \cdot$, the obstruction to the chain-complex structure. The **second Bianchi identity** $d_\nabla F = 0$ then follows automatically: it is $d_\nabla(d_\nabla^2) = (d_\nabla^2)d_\nabla$, true tautologically.

This also explains why curvature is naturally an $\mathrm{End}(E)$-valued 2-form: it is *the* obstruction at the level of operators on sections, and operators on $E$ are sections of $\mathrm{End}(E)$. In the principal-bundle viewpoint (see [[Gauge Theory III — Connections in Principal and Associated Bundles]]), the curvature lifts to a $\mathfrak{g}$-valued 2-form on the total space, equivariant under $G$ and horizontal (vanishing on vertical vectors); on the base $M$ it lives in $\Omega^2(M, \mathrm{ad}\,P)$, where $\mathrm{ad}\,P$ is the adjoint bundle.

---

# Relate to Other Fields / Compression

The curvature of a connection on a vector bundle is **"the obstruction to the connection being flat"** — i.e., to parallel transport being path-independent. Three concrete incarnations:

**In Riemannian geometry**, the curvature of the Levi-Civita connection on $TM$ is the **Riemann curvature tensor** $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$, exactly the same formula. The Riemann tensor measures the failure of "second covariant derivatives commute" and encodes all the local geometry — sectional, Ricci, scalar curvatures are contractions.

**In electromagnetism**, the curvature of the $U(1)$-connection $\omega = -(ie/\hbar)A$ is $\theta = -(ie/\hbar)F$ where $F = dA$ is the EM field strength 2-form: $F = E \wedge dt + B$ (with $E$ the electric and $B$ the magnetic 2-form). The Bianchi identity $dF = 0$ encodes the homogeneous Maxwell equations $\nabla \cdot B = 0$ and $\nabla \times E = -\partial_t B$.

**In Yang-Mills theory**, the curvature of a non-abelian $G$-connection is $F = dA + A \wedge A$ (with the bracket replaced by anticommutator-like structure of the Lie algebra). The $A \wedge A$ term is the source of *self-interaction* — gluons couple to themselves in QCD precisely because $SU(3)$ is non-abelian. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

**True name:** Curvature is **"how much parallel transport around an infinitesimal loop differs from the identity"**. Algebraically it's a 2-form valued in $\mathrm{End}(E)$. Geometrically it's the limit, as the loop shrinks, of $(\mathrm{holonomy} - \mathrm{id})/(\mathrm{area})$. Both faces are useful: the algebraic for computation in coordinates, the geometric for visualization.

---

# Examples / Corollaries

**Is an instance: Trivial connection on $M \times \mathbb{R}^K$.** In the standard global frame, $\omega = 0$, so $F = d\omega + \omega \wedge \omega = 0$. Curvature vanishes identically; the connection is *flat*. Parallel transport is path-independent and trivial.

**Is an instance: Levi-Civita connection on a flat manifold ($\mathbb{R}^n$ with standard metric).** The Christoffel symbols vanish in Cartesian coordinates, $\omega = 0$, $F = 0$. Riemann tensor vanishes — the manifold is flat in the standard sense.

**Is an instance: Levi-Civita connection on the round 2-sphere $S^2$.** In the orthonormal frame $(e_\theta = \partial_\theta, e_\phi = \frac{1}{\sin\theta}\partial_\phi)$, the connection 1-form is $\omega^\phi{}_\theta = -\omega^\theta{}_\phi = \cos\theta\,d\phi$. The curvature is $F^\theta{}_\phi = d\omega^\theta{}_\phi = \sin\theta\,d\theta \wedge d\phi$, which is the area form scaled by the Gaussian curvature $K = +1$. Integrating: $\int_{S^2} F^\theta{}_\phi = 4\pi = 2\pi\chi(S^2)$ — the Gauss-Bonnet theorem.

**Is an instance: EM connection of a uniform magnetic field.** Take $A = -\frac{1}{2}By\,dx + \frac{1}{2}Bx\,dy$ on $\mathbb{R}^3$ (symmetric gauge). Then $F = dA = B\,dx \wedge dy$ — a uniform magnetic field of strength $B$ in the $z$-direction. The curvature of the corresponding $U(1)$-connection $\omega = -(ie/\hbar)A$ is $\theta = -(ie/\hbar)B\,dx \wedge dy$.

**Is an instance: EM connection of a magnetic monopole.** Take $A_U = g(1 - \cos\theta)d\phi$ on $U = \mathbb{R}^3 \setminus \{\text{negative } z\text{-axis}\}$. Then $dA_U = g\sin\theta\,d\theta \wedge d\phi$, the standard area form of $S^2$ scaled by $g$. The curvature integrates over $S^2$ to $4\pi g$, the magnetic charge — see [[Def - The Dirac Monopole Bundle]].

**Is NOT an instance: $\omega \wedge \omega$ alone is not the curvature.** For non-abelian structure groups, the wedge of the connection with itself is generally non-zero, but it is not by itself a curvature — it is only one piece of $F = d\omega + \omega \wedge \omega$. Forgetting $d\omega$ gives a *non-closed* form that is not even tensorial.

**Corollary (curvature transforms as a tensor).** Under change of frame $e_V = e_U c_{UV}$, $F_V = c_{UV}^{-1}F_U c_{UV}$. The inhomogeneous Maurer-Cartan term that appears in the transformation of $\omega$ cancels in $F$. Proof: compute $F_V = d\omega_V + \omega_V \wedge \omega_V$ using $\omega_V = c^{-1}\omega_U c + c^{-1}dc$ — the cross-terms involving $dc$ cancel exactly.

**Corollary (Bianchi identity).** $d_\nabla F = dF + \omega \wedge F - F \wedge \omega = 0$. Equivalently in components, $\nabla_{[X}F_{YZ]} = 0$ after antisymmetrizing. See [[Thm - Bianchi Identity for a Vector-Bundle Connection]].

**Corollary (trace gives a closed 2-form).** $\mathrm{tr}\,F$ is a closed 2-form on $M$ (not just locally — globally, because $F$ is a tensor and trace commutes with conjugation). Its cohomology class $[\mathrm{tr}\,F/2\pi i]$ in $H^2(M, \mathbb{R})$ is *independent of the connection*: it is the **first Chern class** of $E$ (up to sign conventions). This is the simplest characteristic-class statement.

**Corollary (abelian case).** For $U(1)$ or other abelian structure group, $F = d\omega$ locally — $F$ is *exact* on every trivializing patch. But $F$ may fail to be exact *globally*: the field strength of a Dirac monopole, $F = g\sin\theta\,d\theta \wedge d\phi$, is closed on $\mathbb{R}^3 \setminus \{0\}$ but not exact (integral over $S^2$ is $4\pi g \ne 0$). The cohomology class $[F] \in H^2(M, \mathbb{R})$ is the obstruction.

**Calibration check.** (1) For the trivial connection on $\mathbb{R}^n \times \mathbb{R}$, verify $F = 0$ from both definitions (operator and structure equation). (2) For the EM connection $\omega = -(ie/\hbar)A$, compute $F = d\omega + \omega \wedge \omega$ and confirm $\omega \wedge \omega = 0$ (abelian case), giving $F = -(ie/\hbar)dA$. (3) For $S^2$ with the round metric, integrate $\int F^\theta{}_\phi$ over the sphere; you should get $4\pi$.

---

# Unlocked by This

> [!tip] Chern-Weil Theory and Characteristic Classes *(from Algebraic Topology)*
> Given a connection on a complex vector bundle $E$, the **Chern forms** $c_k(F) = \det(I + \frac{i}{2\pi}F)$-coefficients are closed differential forms whose de Rham cohomology classes are *independent of the connection*. These are the **Chern classes** $c_k(E) \in H^{2k}(M, \mathbb{Z})$, integer cohomology invariants of $E$ alone. For a line bundle, only $c_1 = \frac{i}{2\pi}\mathrm{tr}\,F$ is nontrivial, and its integral over closed surfaces gives the integer first Chern numbers — the topological data classifying line bundles. Chern-Weil theory is the general machinery converting curvature to characteristic classes for any structure group. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

> [!tip] Yang-Mills Action and Instantons *(from Mathematical Physics)*
> The **Yang-Mills action** $S_{\mathrm{YM}}[\nabla] = \frac{1}{2}\int_M \mathrm{tr}(F \wedge *F)$ is a gauge-invariant functional on the space of connections. Critical points are the **Yang-Mills equations** $d_\nabla * F = 0$, the non-abelian generalization of the source-free Maxwell equations. In four-dimensional Euclidean space, *self-dual* or *anti-self-dual* connections — those satisfying $F = \pm *F$ — automatically solve Yang-Mills and minimize the action in each topological sector; these are the **instantons**, with the second Chern number $\frac{1}{8\pi^2}\int \mathrm{tr}(F \wedge F)$ counting their topological charge. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]]. Instantons are at the heart of **Donaldson invariants**, **Seiberg-Witten theory**, and the modern study of 4-manifold topology.
