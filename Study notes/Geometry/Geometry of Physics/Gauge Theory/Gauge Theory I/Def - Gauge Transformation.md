---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Bundle"
  - "Def - Local Trivialization"
  - "Def - Connection on a Vector Bundle"
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
tags: [geometry, gauge-theory, gauge-transformation, symmetry]
---

# Notation

$E \to M$ is a smooth vector bundle (real or complex) of rank $K$ with structure group $G \subseteq \mathrm{GL}(K)$ (typically $U(K)$ for hermitian bundles, $U(1)$ for line bundles in EM). A **gauge transformation** $g$ is a smooth function $g : M \to G$ (when the bundle is trivialized globally) or more generally a smooth section of the adjoint bundle $\mathrm{Ad}(P) \to M$ for the associated principal bundle $P$. For $U(1)$, $g : M \to U(1)$ is written $g(x) = e^{i\lambda(x)/\hbar}$ or $g(x) = e^{(ie/\hbar)f(x)}$ depending on parameterization. For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

The motivating question: **two physicists, working in different "gauges", describe the same electromagnetic field. What is the precise relationship between their descriptions?** Each physicist chooses a local trivialization of the wave-function bundle (a "gauge") and writes the connection as a specific 1-form $A_\mu$ in that frame. The two frames may differ by an arbitrary phase at each point — a smooth function $g(x)$ to $U(1)$ — and the question is: what equations relate $A^{(1)}$, $A^{(2)}$, $\psi^{(1)}$, $\psi^{(2)}$?

The first answer, on the wave function: $\psi^{(2)} = g \cdot \psi^{(1)}$. This is automatic — a section of a bundle, expressed in two frames, transforms by the change-of-frame matrix. There is no choice here; this is the definition of how components of a vector transform.

The second answer, on the connection: $A^{(2)} = A^{(1)} - (\hbar/ie)g^{-1}dg$ (for the EM dictionary $\omega = -(ie/\hbar)A$). This is *not* automatic — it is forced by the requirement that the covariant derivative $\nabla\psi$ should transform like $\psi$ itself. If $\psi^{(2)} = g\psi^{(1)}$ and we want $\nabla^{(2)}\psi^{(2)} = g\nabla^{(1)}\psi^{(1)}$ — so that "the derivative transforms like the thing being differentiated" — then expanding:

$$d(g\psi) + \omega^{(2)}(g\psi) = g\,d\psi + g\,\omega^{(1)}\psi$$

The left side is $dg\,\psi + g\,d\psi + \omega^{(2)}g\,\psi$, and the right is $g\,d\psi + g\,\omega^{(1)}\psi$. Cancelling and using $\omega^{(2)}g = g(g^{-1}\omega^{(2)}g)$:

$$dg\,\psi + g(g^{-1}\omega^{(2)}g)\,\psi = g\,\omega^{(1)}\psi$$

so $g^{-1}\omega^{(2)}g = \omega^{(1)} - g^{-1}dg$, i.e. $\omega^{(2)} = g\omega^{(1)}g^{-1} + dg\,g^{-1}$. For abelian $U(1)$ this simplifies to $\omega^{(2)} = \omega^{(1)} + g^{-1}dg$ (commuting scalars), and via $\omega = -(ie/\hbar)A$ this is $A^{(2)} = A^{(1)} - (\hbar/ie)\,g^{-1}dg$. Writing $g = e^{(ie/\hbar)f}$ gives $g^{-1}dg = (ie/\hbar)df$, hence $A^{(2)} = A^{(1)} - df$ (or $+df$ in the opposite convention). The familiar classical gauge transformation $A \to A + df$ is exactly the change-of-frame law in the $U(1)$-bundle.

Why **only $G$-valued** transformations, not arbitrary $\mathrm{GL}(K)$? Because the structure group reduction (from $\mathrm{GL}(K)$ to $G$) is part of the bundle's data. For a hermitian bundle, only $U(K)$ transformations preserve the hermitian metric; non-unitary frame changes would not be compatible with the bundle's structure. For a Riemannian connection on $TM$, only $O(n)$ frame changes preserve the metric. The gauge group $G$ is determined by what structure is being preserved.

Why are gauge transformations called **"symmetries"**? Because they leave the physics invariant: $|\psi|^2$, the curvature $F$, all observable consequences are gauge-invariant. The two descriptions $(\psi^{(1)}, A^{(1)})$ and $(\psi^{(2)}, A^{(2)}) = (g\psi^{(1)}, A^{(1)} - df)$ are physically equivalent — they describe the same physical state of the world, just labelled differently. This is a redundancy, not a physical change.

What does this exclude? A gauge transformation that "rotates the wave function but not the connection" would break covariance: the Schrödinger equation in the new wave function $\psi' = g\psi$ would *not* be the same equation in the old connection $A$. The combined transformation rule $(\psi, A) \to (g\psi, A + df)$ is forced by demanding the *same* equation holds in both descriptions. Forgetting the connection transformation gives "physically inequivalent" descriptions of allegedly the same system — a contradiction.

Why insist on **smooth** gauge transformations? Because the connection and section are smooth, and gauge-transforming them must produce smooth fields. Distributional gauge transformations are studied (e.g. in QFT, "large" gauge transformations connected to topology), but for classical gauge theory we require smoothness.

---

# The Definition

Let $E \to M$ be a smooth vector bundle with structure group $G \subseteq \mathrm{GL}(K)$. A **gauge transformation** of $E$ is a smooth section $g$ of the **adjoint bundle** $\mathrm{Ad}(P) \to M$, where $P$ is the principal $G$-bundle associated with $E$. Equivalently, in any local trivialization, $g$ is a smooth function $g : U \to G$ on each patch, with the compatibility condition $g_V = c_{VU}\,g_U\,c_{VU}^{-1}$ on overlaps (where $c_{VU}$ are the transition functions of $E$).

**The action on sections and connections.** A gauge transformation $g$ acts on sections $\sigma \in \Gamma(E)$ and connections $\nabla$ (with local 1-form $\omega$) by:

$$\sigma \,\mapsto\, g \cdot \sigma, \qquad \omega \,\mapsto\, g\,\omega\,g^{-1} + dg\,g^{-1}.$$

(Equivalently $\omega \mapsto g^{-1}\omega g + g^{-1}dg$ for the *inverse* convention used in some sources, including Frankel — the only difference is whether $g$ acts on $E$ on the left or right.)

**Abelian special case ($G = U(1)$, EM gauge).** For the EM gauge group $G = U(1)$, write $g(x) = e^{(ie/\hbar)f(x)}$ for real $f \in C^\infty(M)$. The transformations are:

$$\psi \,\mapsto\, e^{(ie/\hbar)f}\,\psi, \qquad A \,\mapsto\, A - df, \qquad \omega \,\mapsto\, \omega + \tfrac{ie}{\hbar}\,df.$$

(Sign conventions vary; Frankel uses $A \to A + df$ corresponding to $g = e^{-(ie/\hbar)f}$.) The classical "gauge freedom" of electromagnetism $A \to A + df$ is exactly the action of $g(x) = e^{-(ie/\hbar)f(x)}$.

**Covariance of the covariant derivative.** Under a gauge transformation, the covariant derivative $\nabla_X\sigma$ transforms covariantly: $\nabla_X^{\text{new}}(g\sigma) = g\,\nabla_X^{\text{old}}\sigma$. This is automatic from the connection transformation rule.

**Gauge group.** The set of all gauge transformations forms an infinite-dimensional group $\mathcal{G}(M) = \Gamma(\mathrm{Ad}(P))$ under pointwise multiplication, called the **gauge group** of the bundle. For $U(1)$, $\mathcal{G}(M) = C^\infty(M, U(1))$.

**Gauge invariance of physics.** Two pairs $(\sigma, \nabla)$ and $(g\sigma, g \cdot \nabla)$ describe the *same physics*: all observables ($|\sigma|^2$, the curvature $F$, expectation values, holonomies of $\nabla$ around closed loops) are gauge-invariant.

---

# Categorical / Structural Definition

Gauge transformations are the **vertical automorphisms** of the principal bundle $P \to M$ — bundle isomorphisms $\Phi : P \to P$ covering the identity on $M$. (Compare: ordinary bundle isomorphisms cover *some* diffeomorphism of $M$; gauge transformations are the trivial-on-base case.) The group of vertical automorphisms is isomorphic to $\Gamma(\mathrm{Ad}(P)) = \mathcal{G}(M)$.

The **moduli space of connections** is $\mathcal{A}(P) / \mathcal{G}(M)$, the quotient of the affine space $\mathcal{A}(P)$ of connections by the action of the gauge group. This quotient is the geometric setting for all of gauge theory: the Yang-Mills functional, the Chern-Simons functional, the Donaldson invariants of 4-manifolds all live on this quotient (or its compactifications). The quotient can be quite singular — generally one works with the smooth subquotient of *irreducible* connections — and its topology encodes deep information about the underlying 4-manifold (Donaldson's theorem on the non-smoothability of certain topological manifolds).

In algebraic geometry, the analogous moduli is the moduli of *holomorphic bundles* on a complex variety, with the corresponding "gauge group" being holomorphic automorphisms. The relation between unitary and holomorphic moduli is the **Kobayashi-Hitchin correspondence**.

---

# Relate to Other Fields / Compression

A gauge transformation is **"a change of local trivialization in the principal bundle"**, equivalently a smooth $G$-valued function on $M$ (in a trivialized setting). The fact that gauge transformations form a *group* and that "physics is invariant under the gauge group" is the **gauge principle** — the organizing structural principle of modern fundamental physics.

**In electromagnetism**, the gauge transformation $A \to A + df$ has been known since Maxwell (mid-1800s) as a *mathematical convenience* — choosing different $f$ gives different-looking but physically equivalent $A$'s. Weyl in 1929 reinterpreted it as a *gauge symmetry* — a local $U(1)$ symmetry of the wave function — and noticed the deep parallel with general relativity's local Lorentz invariance.

**In general relativity**, the analogue is **diffeomorphism invariance**: physical observables are invariant under smooth coordinate changes $\phi : M \to M$. The "gauge group" is $\mathrm{Diff}(M)$, the gauge transformations are diffeomorphisms, the connection is the Levi-Civita connection (Christoffel symbols), the curvature is the Riemann tensor, and the gauge-invariant equation is Einstein's $G_{\mu\nu} = 8\pi T_{\mu\nu}$. Diffeomorphism invariance is the original gauge symmetry that motivated Weyl's generalization.

**In Yang-Mills theory**, gauge transformations are $G$-valued functions for non-abelian $G$ (e.g. $SU(2)$, $SU(3)$), and the transformation law $\omega \to g\omega g^{-1} + dg\,g^{-1}$ acquires the full non-abelian structure. This is the foundation of QCD (gauge group $SU(3)$, with quarks transforming in the fundamental representation and gluons in the adjoint) and the electroweak theory (gauge group $SU(2) \times U(1)$, with the Higgs breaking $SU(2) \times U(1) \to U(1)_{\mathrm{EM}}$).

**True name:** A gauge transformation is **"a redundancy in our description of the same physical system"**. Different choices of gauge give different mathematical descriptions $(\psi, A)$, $(\psi', A')$, $\ldots$ of *one* physical situation. The gauge symmetry is *not* a physical symmetry (it does not relate distinct physical states like rotation does); it is a *mathematical redundancy* we have to factor out to identify the true physical content. The reason to call it a "symmetry" anyway is structural: the redundancy is precisely a group, and the formalism of group actions on configurations is the natural language for it.

---

# Examples / Corollaries

**Is an instance: The constant gauge transformation $g(x) \equiv e^{i\alpha}$.** A constant phase rotation of the wave function. Leaves the connection $A$ invariant (since $dg = 0$). This is the *global* $U(1)$-symmetry of QM, and the conserved current it generates via Noether's theorem is the **electric charge**.

**Is an instance: Position-dependent phase $g(x) = e^{(ie/\hbar)f(x)}$.** A spatially varying phase rotation. Changes both the wave function ($\psi \to e^{(ie/\hbar)f}\psi$) and the vector potential ($A \to A - df$). This is the *local* $U(1)$-symmetry of QED.

**Is an instance: Gauge transformation between the symmetric and Landau gauges for a magnetic field.** Both $A^{(1)} = \frac{1}{2}B(-y\,dx + x\,dy)$ (symmetric) and $A^{(2)} = Bx\,dy$ (Landau) give the same $B = B\,dx \wedge dy$. They differ by $A^{(2)} - A^{(1)} = \frac{1}{2}B(y\,dx + x\,dy)$... wait, that's *not* an exact form. Compute: $A^{(2)} - A^{(1)} = Bx\,dy - \frac{1}{2}B(-y\,dx + x\,dy) = \frac{1}{2}B(y\,dx + x\,dy) = \frac{1}{2}d(Bxy)$. Yes, exact: $f = \frac{1}{2}Bxy$. So $A^{(1)} \to A^{(2)} = A^{(1)} + df$ with $f = \frac{1}{2}Bxy$, and correspondingly $\psi \to e^{-(ie/2\hbar)Bxy}\psi$.

**Is an instance: Large gauge transformation on $S^1 \to U(1)$.** A "large" gauge transformation is one not connected to the identity in $\mathcal{G}(M)$. For $M = S^1$, $\mathcal{G}(S^1) = C^\infty(S^1, U(1))$ has $\pi_0 = \mathbb{Z}$ (winding number of $g$ around the circle), so two large gauge transformations with different winding number are not connected by a homotopy. Large gauge transformations are physically important in non-perturbative QCD (the $\theta$-angle).

**Is NOT an instance: A non-smooth gauge transformation.** A discontinuous $g : M \to G$ would not produce smooth fields and is excluded by our smoothness requirement. (Distributional generalizations exist but require care.)

**Is NOT an instance: A "transformation" that mixes $\psi$ and its complex conjugate $\bar\psi$.** Charge conjugation $\psi \to \bar\psi$ takes a section of $L$ to a section of $\bar L$ (the conjugate bundle); this is a *different* bundle from $L$. So charge conjugation is not a gauge transformation in the standard sense.

**Corollary (curvature is gauge-invariant).** Under $\omega \to g\omega g^{-1} + dg\,g^{-1}$, the curvature transforms as $F = d\omega + \omega \wedge \omega \to gFg^{-1}$. For abelian $G$ this means $F$ is invariant: $F \to F$. For non-abelian $G$, $F$ transforms tensorially (by conjugation). Either way, the *gauge-invariant* combinations of $F$ — $\mathrm{tr}(F)$, $\mathrm{tr}(F \wedge F)$, $\mathrm{tr}(F \wedge *F)$ — are unaffected. The Yang-Mills Lagrangian $\mathrm{tr}(F \wedge *F)$ and the topological term $\mathrm{tr}(F \wedge F)$ are both gauge-invariant.

**Corollary (gauge transformations form a group).** The composition of gauge transformations $g_1, g_2$ is the pointwise product $(g_1 g_2)(x) = g_1(x)g_2(x) \in G$; the inverse is the pointwise inverse $g^{-1}(x)$; the identity is the constant function $1$. So $\mathcal{G}(M)$ is a group under pointwise operations. For abelian $G = U(1)$, $\mathcal{G}(M)$ is abelian; for non-abelian $G$, it is not.

**Corollary (Aharonov-Bohm phase is gauge-invariant).** The line integral $\oint_\gamma A$ around a closed loop transforms under $A \to A + df$ as $\oint A + \oint df = \oint A + 0$ (since $f$ is single-valued on a closed loop in a simply-connected domain), hence invariant. On a non-simply-connected domain, if $f$ is a *multi-valued* function (winding $n$ times around the loop), then $\oint df = 2\pi n \cdot (\text{period})$, but the *exponential* $e^{(ie/\hbar)\oint A}$ remains invariant modulo $2\pi$ in the exponent.

**Calibration check.** (1) Verify that $\omega = 0$ is invariant under the constant gauge transformation $g(x) \equiv e^{i\alpha}$ (i.e., constant phases don't change anything). (2) For $g = e^{(ie/\hbar)f}$ on $\mathbb{R}^n$, compute $g^{-1}dg = (ie/\hbar)df$, confirming the abelian connection transforms by $\omega \to \omega + (ie/\hbar)df$, equivalently $A \to A - df$. (3) Verify directly that the covariant derivative is covariant: for $\nabla\psi = (\partial - (ie/\hbar)A)\psi$ and gauge transformation $(\psi, A) \to (g\psi, A - df)$ with $g = e^{(ie/\hbar)f}$, compute $\nabla'(g\psi) = (\partial - (ie/\hbar)(A - df))(g\psi) = g(\partial - (ie/\hbar)A)\psi = g\nabla\psi$.

---

# Unlocked by This

> [!tip] The Gauge Principle and the Standard Model *(from Theoretical Physics)*
> The **gauge principle** says: matter fields enjoy a local symmetry under a Lie group $G$ (called the gauge group), and the dynamics of matter and gauge fields is fixed by demanding that all interactions respect this local symmetry. Applied with $G = U(1)$, the gauge principle generates QED from electron and photon fields. Applied with $G = SU(3)$, it generates QCD with quarks and gluons. Applied with $G = SU(2) \times U(1)$ and a Higgs sector, it generates the electroweak theory. The entire **Standard Model** is determined by its gauge group $SU(3) \times SU(2) \times U(1)$ plus the matter content (quarks, leptons, Higgs) — this is the most precise description of physics ever achieved.

> [!tip] BRST Cohomology and Gauge-Fixing *(from Quantum Field Theory)*
> To quantize a gauge theory, one must "fix the gauge" — pick a representative connection from each gauge equivalence class. Naïve gauge-fixing breaks manifest gauge invariance and introduces unphysical "ghost" fields (Faddeev-Popov ghosts). The **BRST symmetry** is a residual fermionic supersymmetry that survives gauge-fixing and encodes the gauge invariance cohomologically: physical states are the cohomology of the BRST operator $Q$. This is the framework in which gauge theories are renormalized, and it generalizes to **BV (Batalin-Vilkovisky) formalism** for the most general field theories with constraints.
