---
type: definition
subject: gauge-theory
prereqs:
  - "Def - The Yang-Mills Field Strength"
  - "Def - The Lie Algebra of a Lie Group"
  - "Def - Lorentzian Manifold"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

$M$ is a (pseudo-)Riemannian 4-manifold with metric $g_{\mu\nu}$ (Lorentzian signature $(-,+,+,+)$ in physics applications, Riemannian for instanton calculations), $G$ a compact Lie group with Lie algebra $\mathfrak{g}$. Indices are raised and lowered with $g^{\mu\nu}$ and $g_{\mu\nu}$. The volume form is $\operatorname{vol}_g = \sqrt{|g|}\, d^4x$ (with the absolute value for Lorentzian signature).

The trace pairing on $\mathfrak{g} \subset \mathfrak{u}(N)$ is $\langle X, Y\rangle = -\operatorname{tr}(XY)$, real symmetric positive-definite on skew-Hermitian matrices. The field strength is $F = F_{\mu\nu}\,\tfrac12 dx^\mu\wedge dx^\nu$, with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - iq[A_\mu, A_\nu]$.

The wider conventions are in [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons]].

---

# Axiom Motivation

The Yang–Mills Lagrangian $\mathcal{L}_{\text{YM}} = -\tfrac{1}{4}\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})$ is the unique gauge-invariant scalar built from the gauge field that is quadratic in $F$, second-order in derivatives of $A$, and Lorentz-invariant. Each of these conditions plays a non-trivial role; the Lagrangian is what survives when all of them are imposed simultaneously.

*Quadratic in $F$.* The action must produce equations of motion linear in second derivatives of $A$ (and hence in first derivatives of $F$), which is the standard requirement for a wave equation. A term linear in $F$ — schematically $\operatorname{tr}(F)$ — would give equations of motion $0 = 0$ (linear in $A$ gives constants in EOM), and is moreover zero for $G = SU(N)$ where $\operatorname{tr}(F) = 0$. A term cubic in $F$ — $\operatorname{tr}(F\wedge F\wedge F)$ — would give equations of motion non-linear even at the level of the kinetic term, ruining the standard wave propagation. Quadratic is the right "kinetic energy" degree.

*Gauge-invariant.* The integrand must be gauge-invariant for $\int_M \mathcal{L}_{\text{YM}}\, d^4x$ to be well-defined as a functional on the space of gauge-equivalence classes $\mathcal{A}/\mathcal{G}$. The candidate scalars quadratic in $F$ are: $\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})$ (the metric-contracted square), $\operatorname{tr}(F\wedge F)$ (the topological term), and their wedge-star variants. All three are gauge-invariant: $F$ transforms as $F \to gFg^{-1}$, the trace eliminates the conjugation, and the result is a scalar 4-form on $M$. The action splits into two pieces: the kinetic Yang–Mills term and the topological (or $\theta$-) term.

*Choice of sign and normalisation: $-\tfrac{1}{4}$.* The minus sign is forced by requiring positive kinetic energy. On a Lorentzian manifold with signature $(-,+,+,+)$, $F^{\mu\nu}F_{\mu\nu} = -2\vec E^2 + 2\vec B^2$ (negative for electric fields), so $-\tfrac14 F^{\mu\nu}F_{\mu\nu} = \tfrac12(\vec E^2 - \vec B^2)$ — the Lagrangian is $T - V$ for the electromagnetic field (kinetic minus potential), as required. The factor $1/4$ is chosen so that for $G = U(1)$ the Yang–Mills Lagrangian reduces *exactly* to the standard Maxwell Lagrangian, with the canonical factor $-\tfrac14$ in front of $F^{\mu\nu}F_{\mu\nu}$ — variation with respect to $A_\mu$ produces Maxwell's equations with no extraneous constants. The non-trivial-trace generalisation to non-abelian $G$ uses the trace inner product $\langle X, Y\rangle = -\operatorname{tr}(XY)/2$ to compensate for the Pauli-matrix normalisation $\operatorname{tr}(T^a T^b) = \tfrac12\delta^{ab}$ — different sources adopt different conventions, and the constant absorbs them.

*Trace structure and compact group requirement.* The trace $\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})$ is taken in the matrix representation of $\mathfrak{g}$. For this to define a positive-definite norm on $\mathfrak{g}$-valued objects, the trace pairing $\langle X, Y\rangle = -\operatorname{tr}(XY)$ must be positive-definite on $\mathfrak{g}$, which holds for $\mathfrak{g} \subset \mathfrak{u}(N)$ (skew-Hermitian matrices). This is the technical reason the gauge group must be *compact*: only compact Lie groups admit faithful unitary representations and hence positive-definite trace forms. For non-compact $G$ (e.g., $SL(2, \mathbb{R})$), the trace form is indefinite, the "kinetic energy" can be negative, and the theory is sick. This is why every fundamental gauge group of nature is compact.

If one were to drop the metric contraction and use only the topological term $\operatorname{tr}(F\wedge F)$, one would get a closed 4-form whose integral is the second Chern number — a topological invariant, not a dynamical Lagrangian. Adding $\theta\cdot\operatorname{tr}(F\wedge F)$ to the YM Lagrangian for a real parameter $\theta$ is allowed (and physically meaningful — the QCD $\theta$-angle) but does not change the classical equations of motion, since $\operatorname{tr}(F\wedge F) = d\operatorname{CS}(A)$ is locally exact and contributes only a boundary term to $\delta S$.

A subtle point: in *Lorentzian* signature, the YM Lagrangian density is $\mathcal{L}_{\text{YM}} = -\tfrac14 \operatorname{tr}(F^{\mu\nu}F_{\mu\nu})$ with the *plain trace*, giving the action $S = \int_M \mathcal{L}_{\text{YM}}\sqrt{-g}\, d^4x$. In *Euclidean* signature (relevant for instantons), the Lagrangian becomes $\mathcal{L}_{\text{YM}}^E = +\tfrac14\operatorname{tr}(F^{\mu\nu}F_{\mu\nu})$ with the opposite sign, giving the action $S = \tfrac12\int|F|^2\, d^4x$ as a manifestly positive-definite functional. The sign flip comes from Wick rotation $t \to it$ flipping the metric signature.

---

# The Definition

Let $(M, g)$ be an oriented 4-dimensional (pseudo-)Riemannian manifold, $G$ a compact Lie group with Lie algebra $\mathfrak{g} \subset \mathfrak{u}(N)$ (for some $N$), and $A$ a $\mathfrak{g}$-valued connection 1-form on a principal $G$-bundle over $M$, with field strength $F$. The **Yang–Mills Lagrangian density** is the real-valued function on $M$ defined by

$$\mathcal{L}_{\text{YM}} = -\frac{1}{4}\operatorname{tr}(F_{\mu\nu}F^{\mu\nu}),$$

where the trace is in the matrix representation of $\mathfrak{g}$ and the indices are contracted with the inverse metric $g^{\mu\nu}$.

Equivalently, in coordinate-free form,

$$\mathcal{L}_{\text{YM}}\,\operatorname{vol}_g = -\frac{1}{2}\operatorname{tr}(F \wedge \star F),$$

where $\star : \Omega^2(M) \to \Omega^2(M)$ is the Hodge star defined by the metric and orientation. (The factor $1/2$ rather than $1/4$ in this form accounts for the antisymmetry of $F_{\mu\nu}$.)

The corresponding **action functional** is

$$S_{\text{YM}}[A] = \int_M \mathcal{L}_{\text{YM}}\,\sqrt{|g|}\, d^4x = -\frac{1}{2}\int_M \operatorname{tr}(F \wedge \star F).$$

In Lorentzian signature this is the action that produces the Yang–Mills equations $d_A \star F = 0$ via the variational principle. In Euclidean signature, $S_{\text{YM}}[A] = \tfrac{1}{2}\int_M |F|^2\,\operatorname{vol}_g$ is a manifestly non-negative functional, with $|F|^2 = -\tfrac12\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})\,\sqrt{g}\,d^4x$ a positive-definite norm.

---

# Categorical / Structural Definition

Structurally, the Yang–Mills Lagrangian is the **squared norm of the curvature** $\|F\|^2_{L^2(M)}$ with respect to the natural pairing on $\mathfrak{g}$-valued 2-forms: the wedge product combined with the trace and the Hodge star. This pairing is the unique (up to scale) bilinear pairing on $\Omega^2(M; \operatorname{ad} P)$ that is symmetric, positive-definite, gauge-invariant, and metric-compatible.

The space of $\mathfrak{g}$-valued $k$-forms $\Omega^k(M; \operatorname{ad} P)$ on a compact manifold becomes a Hilbert space with this inner product:
$$(\alpha, \beta) = \int_M \langle \alpha, \beta\rangle\,\operatorname{vol}_g = -\int_M \operatorname{tr}(\alpha \wedge \star\beta).$$
The Yang–Mills Lagrangian is then $\mathcal{L}_{\text{YM}} = -\tfrac12 \langle F, F\rangle$, and the action $S_{\text{YM}} = \tfrac12 (F, F) = \tfrac12 \|F\|^2$. This places Yang–Mills theory in the framework of *infinite-dimensional Riemannian geometry on the space of connections* $\mathcal{A}$: $S_{\text{YM}}$ is a "height function" on $\mathcal{A}$ whose critical points are the Yang–Mills connections.

This structural definition makes manifest several properties: $S_{\text{YM}} \ge 0$ (squared norm), $S_{\text{YM}} = 0$ iff $F = 0$ (flat connection), and the first variation $\delta S_{\text{YM}} = (\delta F, F) = (d_A\delta A, F) = (\delta A, d_A^* F)$ produces the YM equation $d_A^* F = 0$ via the adjoint operator $d_A^* = -\star d_A\star$.

---

# Relate to Other Fields / Compression

**The Yang–Mills Lagrangian generalises the Maxwell Lagrangian**: for $G = U(1)$, the commutator vanishes, $F = dA$, and $\mathcal{L}_{\text{YM}}$ reduces to $-\tfrac14 F_{\mu\nu}F^{\mu\nu} = \tfrac12(\vec E^2 - \vec B^2)$, the standard Maxwell Lagrangian. The non-abelian generalisation adds cubic and quartic self-interaction terms — explicit expansion $\mathcal{L}_{\text{YM}} = -\tfrac14(\partial A - \partial A)^2 + (\text{cubic in } A) + (\text{quartic in } A)$ — which become the three-gluon and four-gluon vertices when the theory is quantised. These self-interactions are absent in QED (photons do not interact directly with photons) but central to QCD (gluons interact directly with each other).

**It is also the natural action for gauge connections in dimensions other than 4.** In dimension $n$ the YM action $S = -\tfrac12\int_M\operatorname{tr}(F\wedge\star F)$ produces YM equations $d_A\star F = 0$ for any $n$, but the *conformal invariance* of $S_{\text{YM}}$ is special to $n = 4$: in 4 dimensions, the action is invariant under conformal rescalings $g \to e^{2\sigma}g$ of the metric, because the volume form $\operatorname{vol}_g$ scales as $e^{4\sigma}$ and $\star F$ on a 2-form scales as $e^{(4-2\cdot 2)\sigma} = e^0$, so $\operatorname{vol}_g \star F$ has total scaling weight $0$. This conformal invariance is one of the special features of Yang–Mills in 4D and is the reason instantons exist as scale-free solutions parameterised by a continuous size $\rho$.

**True name:** the YM Lagrangian is the *squared norm of the curvature*. The operational form $S_{\text{YM}} = \tfrac12\|F\|^2$ is what you reach for when you want to prove positivity, derive the BPS bound, set up an existence theorem via minimisation, or argue about Morse theory on the space of connections. The component formula $-\tfrac14 \operatorname{tr}(F^{\mu\nu}F_{\mu\nu})$ is the *expression* of the squared norm in a chart; the true name is the structural identity.

---

# Examples / Corollaries

**Example 1 — Maxwell on Minkowski $\mathbb{R}^4$.** For $G = U(1)$ and $A_\mu$ the EM 4-potential, $\mathcal{L}_{\text{YM}} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} = \tfrac12(\vec E^2 - \vec B^2)$ in Lorentzian signature $(-,+,+,+)$. This is the famous "kinetic minus potential" form, with $\vec E$ playing the role of kinetic and $\vec B$ of potential. Varying with respect to $A_\mu$ produces Maxwell's equations $\partial_\mu F^{\mu\nu} = 0$ (sourceless) or $\partial_\mu F^{\mu\nu} = J^\nu$ (with current $J^\nu$ from coupling to matter).

**Example 2 — Pure $SU(2)$ Yang–Mills on Euclidean $\mathbb{R}^4$.** With $A = A^a_\mu (\sigma_a/2)\, dx^\mu$ ($a = 1, 2, 3$), the field strength is $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + g\epsilon^{abc}A^b_\mu A^c_\nu$, and the Lagrangian is $\mathcal{L}_{\text{YM}} = +\tfrac{1}{4}F^a_{\mu\nu}F^{a,\mu\nu}$ (Euclidean, with $\operatorname{tr}(\sigma_a\sigma_b) = 2\delta_{ab}$ giving an extra factor). The cubic and quartic self-interaction terms become $\mathcal{L}^{(3)} = g\epsilon^{abc}(\partial_\mu A^a_\nu)A^{b,\mu}A^{c,\nu}$ and $\mathcal{L}^{(4)} = \tfrac{g^2}{4}\epsilon^{abc}\epsilon^{ade}A^b_\mu A^c_\nu A^{d,\mu}A^{e,\nu}$, the famous three-gluon and four-gluon vertices of QCD (after replacing $\epsilon^{abc}$ by the $SU(3)$ structure constants $f^{abc}$).

**Example 3 — The $\theta$-term and its non-contribution to EOM.** Adding the topological term $\mathcal{L}_\theta = \theta\cdot\operatorname{tr}(F\wedge F)/8\pi^2$ to the YM Lagrangian does *not* change the equations of motion, because $\operatorname{tr}(F\wedge F) = d\operatorname{CS}(A)$ is locally exact: $\delta\int \operatorname{tr}(F\wedge F) = \int d(\text{boundary terms})$ vanishes on the bulk EOM. However, the $\theta$-term contributes a topological piece $\theta\cdot k$ to the action (where $k$ is the instanton number), which has measurable consequences in the quantum theory — the QCD $\theta$-vacuum.

**Non-example — A naive "Lagrangian" $\operatorname{tr}(F_{\mu\nu})$ is identically zero for $G = SU(N)$.** The trace of an element of $\mathfrak{su}(N)$ vanishes by definition: $\operatorname{tr}(F) = \operatorname{tr}(F^a T^a) = F^a \operatorname{tr}(T^a) = 0$. So one cannot build a linear-in-$F$ Lagrangian for $SU(N)$ — the quadratic term $\operatorname{tr}(F\wedge\star F)$ is the leading non-trivial gauge-invariant scalar, justifying the choice in the YM Lagrangian. For $G = U(1)$ the trace is replaced by the identity (since $\mathfrak{u}(1) = i\mathbb{R}$ is one-dimensional), and a linear term $iqA$ would also be possible, but is forbidden by gauge invariance: $\int A$ is not gauge-invariant.

**Calibration check.** A reader who has internalised the definition should be able to: (a) reduce $\mathcal{L}_{\text{YM}}$ for $G = U(1)$ on Minkowski space to $\tfrac12(\vec E^2 - \vec B^2)$ explicitly, verifying the conventional Maxwell form; (b) verify gauge-invariance of $\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})$ from the homogeneous transformation $F \to gFg^{-1}$ and the cyclic property of the trace; (c) explain why a Yang–Mills Lagrangian for a non-compact gauge group like $SL(2, \mathbb{R})$ would have indefinite kinetic energy and is therefore unphysical.

---

# Unlocked by This

> [!tip] BRST Quantisation and Faddeev–Popov Ghosts *(from Quantum Field Theory)*
> Quantising the Yang–Mills Lagrangian via the path integral $\int \mathcal{D}A\, e^{iS_{\text{YM}}}$ requires fixing the gauge to avoid integrating over an infinite-dimensional orbit of gauge-equivalent configurations. The **Faddeev–Popov procedure** introduces auxiliary fermionic "ghost" fields $c$ and $\bar c$ with a quadratic ghost Lagrangian $\mathcal{L}_{\text{gh}} = -\bar c\,\partial^\mu D_\mu c$, and **BRST symmetry** (Becchi–Rouet–Stora–Tyutin) provides a nilpotent supersymmetry $Q$ with $Q^2 = 0$ whose cohomology defines the physical Hilbert space. The full gauge-fixed action $S_{\text{YM}} + S_{\text{gh}} + S_{\text{GF}}$ is no longer gauge-invariant but is BRST-invariant, and renormalisability of Yang–Mills theory (proved by 't Hooft and Veltman in 1972) hinges entirely on the BRST cohomological structure. This is one of the most important developments in twentieth-century theoretical physics.

> [!tip] The Standard Model Lagrangian *(from Particle Physics)*
> The full **Standard Model Lagrangian** is built from three Yang–Mills Lagrangians — one for $U(1)_Y$ (hypercharge), one for $SU(2)_L$ (weak isospin), and one for $SU(3)_C$ (colour) — coupled to matter Lagrangians for the quarks and leptons (three generations of Dirac spinors) via gauge-covariant derivatives, plus a Higgs Lagrangian $\mathcal{L}_H = |D_\mu H|^2 - V(H)$ that breaks $SU(2)_L \times U(1)_Y$ down to electromagnetic $U(1)_{\text{em}}$ via the Higgs mechanism. The fact that all four fundamental interactions of physics — strong, weak, electromagnetic, and (separately) gravitational — fit into one Lagrangian whose structure is dictated by the gauge principle is the central achievement of twentieth-century theoretical physics, and the Higgs discovery at CERN in 2012 was the final experimental confirmation.
