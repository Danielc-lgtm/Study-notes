---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - Differential k-Form on a Manifold"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

$M$ is a smooth manifold (spacetime); $G$ is a compact Lie group with Lie algebra $\mathfrak{g}$; $E \to M$ is a vector bundle whose structure group is $G$, with fibre $V$ (typically $\mathbb{C}^N$) carrying a representation $\rho : G \to GL(V)$. The "matter field" $\psi$ is a section of $E$, locally an $N$-component column $\psi^a(x)$.

A **gauge transformation** is a (local) change of frame in $E$, equivalently a smooth function $g : U \to G$ on an open set $U \subseteq M$, acting on sections by $\psi \to \rho(g)\psi$ — most commonly written simply as $\psi \to g\psi$ when the representation is understood.

The **gauge potential** $A$ is a $\mathfrak{g}$-valued 1-form on $M$, locally $A = A_\mu(x)\,dx^\mu$ with each $A_\mu(x) \in \mathfrak{g}$. The constant $q$ is a "coupling" / "generalised charge"; the conventional relation to the geometric connection 1-form $\omega$ is $\omega = -iq A$ (so $\omega$ is skew-Hermitian when $A$ is Hermitian).

Index conventions: Greek indices $\mu, \nu = 0, 1, 2, 3$ run over spacetime; lowercase Latin $a, b = 1, \dots, N$ run over fibre components; capital Latin $A, B = 1, \dots, \dim\mathfrak{g}$ run over a basis of the Lie algebra. The Einstein summation convention applies.

---

# Axiom Motivation

The gauge-covariant derivative exists to solve one specific problem: when a Lagrangian has a *global* internal symmetry $\psi \to g\psi$ for constant $g$, the *local* version $\psi \to g(x)\psi$ destroys it, because $\partial_\mu(g(x)\psi) = g(x)\partial_\mu\psi + (\partial_\mu g(x))\psi$. The extra $(\partial_\mu g)\psi$ term is non-zero whenever $g$ depends on position, and it ruins any Lagrangian containing $\partial_\mu\psi$. The covariant derivative $D_\mu = \partial_\mu - iqA_\mu$ is the unique modification of $\partial_\mu$ that absorbs this extra term, provided the new field $A_\mu$ transforms in a specific compensating way.

The motivation breaks naturally into three steps, each addressing a separate question.

*Step 1 — Why must one introduce a new field at all?* In principle one could try other modifications: a non-derivative correction $\partial_\mu \to \partial_\mu + f(\psi)$, a higher-derivative correction $\partial_\mu \to \partial_\mu + h(\partial^2\psi)$, etc. None of these work. The unwanted term $(\partial_\mu g)\psi$ is *linear in $\psi$* and *carries the same Lie-algebra index structure* as $\psi$ itself. The only way to cancel it pointwise is by adding a term that is *also* linear in $\psi$ with a $\mathfrak{g}$-valued coefficient. This forces the form $D_\mu\psi = \partial_\mu\psi + \omega_\mu\psi$ for some $\mathfrak{g}$-valued 1-form $\omega_\mu$.

*Step 2 — Why must $A$ transform inhomogeneously?* The transformation law of $A_\mu$ under $\psi \to g\psi$ is *forced* by the requirement that $D_\mu\psi \to g(D_\mu\psi)$ — that is, that the covariant derivative transform like a tensor (homogeneously). Demanding $D'_\mu(g\psi) = g(D_\mu\psi)$ and computing both sides:
$$(\partial_\mu - iqA'_\mu)(g\psi) = g(\partial_\mu - iqA_\mu)\psi$$
$$g\partial_\mu\psi + (\partial_\mu g)\psi - iqA'_\mu g\psi = g\partial_\mu\psi - iq g A_\mu\psi$$
$$A'_\mu = g A_\mu g^{-1} + (i/q) g(\partial_\mu g^{-1})\cdot g \cdot g^{-1} = g A_\mu g^{-1} - (i/q)(\partial_\mu g)g^{-1}.$$
The inhomogeneous $-(i/q)(\partial_\mu g)g^{-1}$ term is *forced*: it is the unique correction making the covariant derivative transform homogeneously. If $A$ instead transformed homogeneously like a tensor, $A'_\mu = gA_\mu g^{-1}$, the unwanted $(\partial_\mu g)\psi$ would survive.

*Step 3 — Why is the factor $-iq$ specifically?* The choice $D_\mu = \partial_\mu - iqA_\mu$ versus, say, $D_\mu = \partial_\mu + qA_\mu$ or $D_\mu = \partial_\mu + i\omega_\mu$ is a convention. The factor $-i$ is fixed by the convention that $A_\mu$ is Hermitian (a *real* field, in physics terminology) while the corresponding connection $\omega_\mu = -iqA_\mu$ is skew-Hermitian (an element of $\mathfrak{u}(N)$, the Lie algebra of the unitary group). The factor $q$ is the physical coupling constant — the electric charge for $U(1)$, the strong-coupling constant for $SU(3)$. Different fields carrying different charges receive different covariant derivatives ($D^{(e)}_\mu = \partial_\mu - ieA_\mu$ for electrons, $D^{(2e/3)}_\mu = \partial_\mu - i(2e/3)A_\mu$ for up quarks).

Drop any one of these axioms and the construction fails. Drop the homogeneous transformation law of $D_\mu\psi$ and you do not have a covariant operator — the equations built from it are not gauge-invariant. Drop the inhomogeneous transformation of $A$ and the unwanted $\partial_\mu g$ term survives. Drop the linearity in $\psi$ and you cannot cancel the linear-in-$\psi$ correction term. The covariant derivative is the unique object satisfying all three constraints; this is the gauge principle in its purest form.

A useful forward-reference: the proof that $D_\mu D_\nu - D_\nu D_\mu = -iqF_{\mu\nu}$ (the commutator of covariant derivatives equals the field strength) is the *geometric meaning* of the field strength. $F$ measures the failure of covariant differentiation to commute, exactly as the Riemann tensor measures the failure of covariant differentiation of *tensors* to commute on a manifold with a metric. The two facts are special cases of the same general identity for a connection on a vector bundle.

---

# The Definition

Let $E \to M$ be a vector bundle with structure group $G$, and let $A$ be a $\mathfrak{g}$-valued 1-form on $M$ (a *gauge potential*) representing a connection on $E$ in a chosen local frame. The **gauge-covariant derivative** in the direction of a vector field $X$ on $M$, acting on a section $\psi$ of $E$, is the operator

$$D_X \psi = X^\mu D_\mu\psi, \qquad D_\mu\psi = \partial_\mu\psi - iqA_\mu\psi,$$

where $q$ is the coupling constant and the matrix multiplication $A_\mu\psi$ uses the representation of $\mathfrak{g}$ on the fibre $V$ in which $\psi$ takes values. Equivalently, writing $\omega = -iqA$ for the geometric connection 1-form, $D_\mu\psi = \partial_\mu\psi + \omega_\mu\psi$.

The defining property is that under a gauge transformation $\psi(x) \to g(x)\psi(x)$ accompanied by

$$A_\mu \to g A_\mu g^{-1} - \frac{i}{q}(\partial_\mu g)g^{-1},$$

the covariant derivative transforms homogeneously: $D_\mu\psi \to g\,(D_\mu\psi)$. Equivalently, $D_\mu(g\psi) = g\,(D_\mu\psi)$.

When acting on a general tensor section — for example a section of $E \otimes E^*$, transforming as $T \to g T g^{-1}$ — the covariant derivative becomes $D_\mu T = \partial_\mu T - iq[A_\mu, T]$, with the commutator in place of multiplication. This generalises to any tensor product: for each factor in the representation, the covariant derivative adds a connection term in the appropriate representation.

---

# Categorical / Structural Definition

A **connection on a principal $G$-bundle** $P \to M$ is a $\mathfrak{g}$-valued 1-form $\omega$ on $P$ satisfying two conditions: (i) $\omega(\xi^*) = \xi$ for the fundamental vector field $\xi^*$ generated by any $\xi \in \mathfrak{g}$ (vertical compatibility); (ii) $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$ for all $g \in G$ (right-equivariance). The connection 1-form $\omega$ pulled back by a local section $s : U \to P$ gives the local gauge potential $A = -i q s^*\omega$ (with the sign and factor of $q$ being a convention), and the covariant derivative $D_\mu$ on sections of an associated vector bundle $E = P \times_\rho V$ is the operator induced by $\omega$ via the representation $\rho$.

In categorical language, a connection is a *splitting of the Atiyah exact sequence*
$$0 \to \operatorname{ad} P \to TP/G \to TM \to 0$$
of $G$-equivariant vector bundles on $M$. The covariant derivative is then the "differentiation along horizontal lifts" induced by this splitting. The covariant derivative is the manifestation of the splitting at the level of sections of $E$.

A more elementary structural definition uses parallel transport: a connection on $E$ is a choice, for every smooth curve $\gamma : [0, 1] \to M$, of a linear isomorphism $P_\gamma : E_{\gamma(0)} \to E_{\gamma(1)}$ between fibres at the endpoints, smooth in the curve, satisfying $P_{\gamma_1 \cdot \gamma_2} = P_{\gamma_2}\circ P_{\gamma_1}$ for concatenation. The covariant derivative is then the infinitesimal version of parallel transport: $D_X\psi|_p = \lim_{t\to 0} (P_{\gamma_{|[0,t]}}^{-1}\psi(\gamma(t)) - \psi(p))/t$ for a curve $\gamma$ with $\gamma(0) = p$, $\dot\gamma(0) = X$.

See [[Gauge Theory III — Principal Connections, Curvature, Holonomy, and Gauge Symmetry]] for the full development.

---

# Relate to Other Fields / Compression

**The covariant derivative of differential geometry is the same idea applied to the *tangent* bundle**: for a Riemannian metric on $M$, the Levi-Civita connection $\nabla_\mu$ acts on tangent vectors as $\nabla_\mu V^\nu = \partial_\mu V^\nu + \Gamma^\nu{}_{\mu\sigma}V^\sigma$, with the Christoffel symbols $\Gamma^\nu{}_{\mu\sigma}$ playing the role of the gauge potential. The gauge group is $GL(n)$ (or $SO(n)$ in the orthonormal-frame formulation), the matter field is a tangent vector $V^\nu$, and the covariant derivative makes tensor calculus on a curved manifold possible. The structural identity is the same: $\nabla_\mu - \partial_\mu = \Gamma_\mu$ is *not* a tensor, but the difference of two connections *is*. See [[Riemannian Geometry I — Connections and Covariant Differentiation]].

**It is also the natural operator on holomorphic vector bundles**: replacing $\mathfrak{u}(N)$-valued connections by $\mathfrak{gl}(N, \mathbb{C})$-valued ones and demanding compatibility with both a Hermitian metric and a holomorphic structure, one obtains the **Chern connection** on a Hermitian holomorphic vector bundle — the gauge-theoretic analogue of the holomorphic Cauchy–Riemann operator $\bar\partial$. This is the entry point to Yang–Mills theory in complex geometry, the **Hermitian–Yang–Mills equations** $F^{0,2} = 0$ and $\Lambda F = c\cdot\operatorname{id}$, and the **Donaldson–Uhlenbeck–Yau theorem** identifying solutions with polystable holomorphic bundles.

**True name:** the covariant derivative is the *unique modification of $\partial_\mu$ that commutes with gauge transformations*. Operationally, the test of whether you have computed $D_\mu$ correctly is: apply $D_\mu$ to $g\psi$, push the $g$ through, and check that you get $g\,D_\mu\psi$. If you do not, you have either the wrong sign on the $-iqA$ term, the wrong transformation law for $A$, or the wrong representation. The "commutes with gauge transformations" criterion is what you actually use to debug a gauge-theory calculation; the formal definition $D_\mu = \partial_\mu - iqA_\mu$ is just the formula that satisfies this criterion.

---

# Examples / Corollaries

**Example 1 — Minimal coupling of QED.** For $G = U(1)$, $A_\mu$ is the electromagnetic 4-potential (real-valued), $q = e$ (electron charge), and the covariant derivative is $D_\mu\psi = (\partial_\mu - ieA_\mu)\psi$. This is the "minimal coupling" prescription that takes the free Dirac Lagrangian $\bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ to the QED Lagrangian $\bar\psi(i\gamma^\mu D_\mu - m)\psi$ — adding the interaction term $e\bar\psi\gamma^\mu A_\mu\psi$ that couples electrons to the electromagnetic field. The covariant derivative on the conjugate spinor $\bar\psi$ uses the conjugate transformation $\bar\psi \to \bar\psi g^{-1}$, giving $D_\mu\bar\psi = \partial_\mu\bar\psi + ieA_\mu\bar\psi$, with the opposite sign.

**Example 2 — Non-abelian covariant derivative for $SU(2)$ acting on the nucleon doublet.** For $G = SU(2)$ acting on $\psi = (p, n)^T$ by the fundamental representation, $A_\mu = A_\mu^a (\sigma_a/2)$ with $\sigma_a$ the Pauli matrices and $A_\mu^a$ three real-valued 1-forms (the three Yang–Mills fields). The covariant derivative is $D_\mu\psi = \partial_\mu\psi - igA_\mu^a (\sigma_a/2)\psi$, and acting on the doublet structure mixes the proton and neutron components. The commutator $[D_\mu, D_\nu]\psi = -ig F_{\mu\nu}\psi$ produces the field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - ig[A_\mu, A_\nu]$ — the new $[A_\mu, A_\nu]$ term is the entire content of "non-abelian" YM theory.

**Example 3 — Covariant derivative on the adjoint bundle.** Sections of $\operatorname{ad} P$ are $\mathfrak{g}$-valued functions transforming as $\phi \to g\phi g^{-1}$. The covariant derivative is then $D_\mu\phi = \partial_\mu\phi - iq[A_\mu, \phi]$ (or $D_\mu\phi = \partial_\mu\phi + [\omega_\mu, \phi]$ in geometric notation). The Bianchi identity for the curvature reads $D_\mu F_{\nu\rho} + D_\nu F_{\rho\mu} + D_\rho F_{\mu\nu} = 0$, using exactly this adjoint covariant derivative on the $\mathfrak{g}$-valued 2-form $F$.

**Non-example — The plain partial derivative $\partial_\mu$ is not gauge-covariant.** Under $\psi \to g(x)\psi$, $\partial_\mu(g\psi) = g\partial_\mu\psi + (\partial_\mu g)\psi$. The second term destroys covariance, and this is exactly the failure that the introduction of $A$ repairs. The Lagrangian $\bar\psi i\gamma^\mu\partial_\mu\psi$ is invariant under *global* gauge transformations (constant $g$) but transforms inhomogeneously under *local* ones: $\delta\mathcal{L} = -\bar\psi\gamma^\mu(\partial_\mu g)g^{-1}\psi \neq 0$ in general. The minimally-coupled Lagrangian $\bar\psi i\gamma^\mu D_\mu\psi$ is invariant under both.

**Calibration check.** A reader who has internalised the definition should be able to: (a) write down the covariant derivative on the *complex conjugate* spinor $\bar\psi$ (it carries the opposite charge), and verify that $\bar\psi D_\mu\psi - (D_\mu\bar\psi)\psi$ is gauge-invariant; (b) compute the commutator $[D_\mu, D_\nu]\psi$ explicitly for an abelian $U(1)$ gauge field, obtaining $-ieF_{\mu\nu}\psi$ with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ (the commutator term vanishes for $U(1)$); (c) explain why the covariant derivative on a section transforming in the *trivial* representation reduces to the ordinary partial derivative — the connection acts as zero on the trivial representation.

---

# Unlocked by This

> [!tip] Minimal Coupling and the Equivalence Principle *(from General Relativity)*
> The recipe "replace $\partial_\mu$ by $\nabla_\mu$" in general relativity is the gravitational version of "replace $\partial_\mu$ by $D_\mu$" in gauge theory. Just as gauge invariance of the Dirac Lagrangian forces the coupling $\partial_\mu \to D_\mu = \partial_\mu - ieA_\mu$ to the electromagnetic field, general covariance of any field equation forces the coupling $\partial_\mu \to \nabla_\mu = \partial_\mu + \Gamma_\mu$ to the gravitational field. The Einstein equivalence principle — locally a freely-falling frame is indistinguishable from inertial — is the statement that $\nabla_\mu$ reduces to $\partial_\mu$ in normal coordinates at any point, exactly as $D_\mu$ reduces to $\partial_\mu$ in a gauge where $A_\mu$ vanishes at a point. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] The Aharonov–Bohm Effect *(from Quantum Mechanics)*
> The covariant derivative reveals that the *gauge potential* $A_\mu$ — not just the field strength $F_{\mu\nu}$ — has physical consequences in quantum mechanics. An electron travelling around a region of zero magnetic field but non-zero $\oint A$ picks up a measurable phase $\exp(ie\oint A)$, even though it never experiences a force. This phase shift was predicted by Aharonov and Bohm in 1959 and experimentally observed by Tonomura in 1986. The phase is a holonomy of the gauge connection — the path-ordered exponential $\operatorname{Pexp}\oint_C A$ — and it depends on $A$ in a way that no $F$-based formula could detect. This is the experimental proof that the gauge connection (and not merely its curvature) is physically real, and is one of the cleanest manifestations of the geometric content of gauge theory.
