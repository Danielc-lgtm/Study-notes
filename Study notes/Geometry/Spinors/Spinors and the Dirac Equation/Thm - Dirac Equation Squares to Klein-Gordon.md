---
type: theorem
subject: spinors
prereqs:
  - "Def - The Dirac Equation"
  - "Def - Dirac Gamma Matrices"
tags: [geometry, spinors, quantum-mechanics, relativity]
---

# Notation

$\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu = -\partial_t^2 + \partial_x^2 + \partial_y^2 + \partial_z^2$ is the d'Alembertian (Frankel signature $\eta = \mathrm{diag}(-1, +1, +1, +1)$). $\not\partial = \gamma^\mu\partial_\mu$ is the Dirac operator on Minkowski space. The Klein–Gordon equation for a scalar field $\phi$ of mass $m$ is $\Box\phi = m^2\phi$. The Dirac equation for a spinor field $\psi$ of mass $m$ is $\not\partial\psi = m\psi$ (in our convention).

---

# Statement

> **Theorem.** Let $\psi: \mathbb{R}^{1,3} \to \mathbb{C}^4$ be a solution of the Dirac equation $\not\partial\psi = m\psi$ on Minkowski space. Then each component of $\psi$ satisfies the Klein–Gordon equation:
> $$\Box\psi = m^2 \psi.$$
> The operator identity behind this is
> $$\not\partial^2 = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu = \Box \cdot I,$$
> which follows from the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$.

> **Corollary.** Every Dirac spinor satisfies the relativistic dispersion relation $E^2 = \vec p^2 + m^2$, i.e., it represents a particle of mass $m$.

> **Corollary (curved-spacetime version).** On a curved spin manifold $M$ with Riemannian metric, the Dirac operator squared decomposes as $\not D^2 = -\nabla^{S*}\nabla^S + R/4$, where $R$ is the scalar curvature; see [[Thm - Lichnerowicz Formula]]. The flat-space identity $\not\partial^2 = \Box$ is the $R = 0$ case.

---

# Motivation

This theorem is the **justification for the Dirac equation**: it confirms that the Dirac equation is *consistent with relativity*. A relativistic particle of mass $m$ satisfies $E^2 = \vec p^2 + m^2$, which classically becomes the Klein-Gordon equation $\Box\phi = m^2\phi$. The Dirac equation is *first-order*, so it cannot directly express this quadratic relation; the squaring identity $\not\partial^2 = \Box$ is what restores the correct relativistic dispersion relation when one squares the linear Dirac operator.

The historical motivation: when Dirac was searching for a first-order relativistic wave equation in 1928, his criterion was exactly that "squaring should give Klein-Gordon". The Klein-Gordon equation was already known (and known to have problems with negative probability), but it was the *unique* relativistic wave equation if one allowed only scalar fields. The Dirac equation generalized this by allowing the wave function to be a multi-component object, with the gamma-matrix structure providing exactly the algebraic input needed to make a first-order operator square to a Lorentz scalar.

The structural content of the theorem: the Dirac operator is *literally* a square root of the d'Alembertian. The "square root" is taken in a non-commutative matrix algebra (the Dirac algebra $M_4(\mathbb{C})$), not in the ordinary commutative algebra of operators — this is why the wave function must have 4 components, and why the gamma matrices satisfy the Clifford relation rather than being scalars.

This squaring identity also generalizes profoundly to curved manifolds, where $\not D^2 = -\nabla^{S*}\nabla^S + R/4$ (the Lichnerowicz formula); the curvature term $R/4$ is a "quantum correction" that vanishes only in flat space. It is the source of all vanishing theorems for harmonic spinors and of much of the deep geometry of Dirac operators on curved spaces.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: Any solution of the Dirac equation.* By the theorem, the wave function $\psi$ automatically satisfies the Klein-Gordon equation. So solving the Dirac equation is "more refined" than solving Klein-Gordon: every Dirac solution is a Klein-Gordon solution (componentwise), but not conversely. Bridge: in computing scattering amplitudes, one often verifies that external particle wave functions satisfy Klein-Gordon as a consistency check, even when they were derived from the Dirac equation.

*Source 2: A first-order differential operator whose square is the Laplacian.* The theorem says that for the d'Alembertian (or Riemannian Laplacian, after Wick rotation), the Dirac operator $\not\partial$ is such a square root. Bridge: the same construction works in any signature and any dimension where Clifford-algebra-valued matrices exist; in $D$ dimensions, the gamma matrices are $2^{\lfloor D/2 \rfloor} \times 2^{\lfloor D/2\rfloor}$ matrices satisfying the Clifford relation.

*Source 3: The Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$.* The theorem's identity $\not\partial^2 = \Box$ follows from this single algebraic input, plus the commutativity of partial derivatives $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$.

**Targets (Output Amplification)**

*Target 1: Construction of conserved currents from Dirac bilinears.* The conserved Dirac current $j^\mu = \bar\psi\gamma^\mu\psi$ satisfies $\partial_\mu j^\mu = 0$, with the conservation following from the Dirac equation and its conjugate. The squared equation $\Box\psi = m^2\psi$ is what makes the second-order conserved quantities (energy-momentum tensor, etc.) work out. See [[Ex - The Square of a Dirac Spinor Gives a 4-Current]].

*Target 2: Plane-wave solutions.* Looking for solutions $\psi(x) = u(p)e^{-ip\cdot x}$, the squared equation $\Box\psi = m^2\psi$ gives $p^2 = -m^2$ — the mass-shell condition. The first-order Dirac equation $(\not p + im)u = 0$ then picks out which polarization spinors $u(p)$ are allowed on the mass shell. See [[Ex - Plane-Wave Solutions of the Free Dirac Equation]].

*Target 3: Lichnerowicz formula in curved space.* The flat-space identity $\not\partial^2 = \Box$ generalizes to $\not D^2 = -\nabla^{S*}\nabla^S + R/4$ on curved manifolds; the additional $R/4$ scalar-curvature term encodes the spin-Riemann coupling. The proof technique — manipulating the Clifford relation on indices — is the same.

*Target 4: Negative-energy solutions.* The Klein-Gordon equation $E^2 = \vec p^2 + m^2$ admits both positive and negative roots for $E$, leading to the negative-energy solutions of the Dirac equation that Dirac initially interpreted as "holes" and now are recognized as antiparticles.

---

# Why Is It True

The theorem is true because of the **Clifford relation** and the **commutativity of partial derivatives**. The Dirac operator squared is

$$\not\partial^2 = \gamma^\mu\partial_\mu(\gamma^\nu\partial_\nu) = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu.$$

Since $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$, we can symmetrise the gamma matrix factor:

$$\gamma^\mu\gamma^\nu\partial_\mu\partial_\nu = \tfrac{1}{2}(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu)\partial_\mu\partial_\nu = \tfrac{1}{2}\{\gamma^\mu, \gamma^\nu\}\partial_\mu\partial_\nu.$$

Apply the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$:

$$= \tfrac{1}{2}(2\eta^{\mu\nu})\partial_\mu\partial_\nu \cdot I = \eta^{\mu\nu}\partial_\mu\partial_\nu \cdot I = \Box \cdot I.$$

So $\not\partial^2\psi = \Box\psi$ for any spinor field $\psi$. Combined with the Dirac equation $\not\partial\psi = m\psi$:

$$\not\partial^2\psi = \not\partial(m\psi) = m\not\partial\psi = m^2\psi,$$

so $\Box\psi = m^2\psi$ — the Klein-Gordon equation.

**Mechanism in one line: the Clifford relation symmetrises the product of gamma matrices into a scalar (the metric), so the square of the linear Dirac operator becomes the quadratic d'Alembertian.**

The deeper insight: the Dirac operator is *literally* a square root of the d'Alembertian, in the sense that $\not\partial \cdot \not\partial = \Box$ as operators. This kind of "square root" is impossible in commutative algebra (the d'Alembertian is *not* a perfect square of a linear scalar operator); it becomes possible in the non-commutative matrix algebra where the gamma matrices live. The non-commutativity of the gammas — the failure of the naive square — is exactly what creates the cross-terms $\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu$ that the Clifford relation absorbs into scalar form.

---

# What Makes This Hard

The "hard" step is recognizing the symmetrisation trick: $\gamma^\mu\gamma^\nu\partial_\mu\partial_\nu$ looks like a sum that *might* fail to simplify, but using $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$ to symmetrize forces the gamma matrices into their symmetric combination, which by the Clifford relation is a scalar. A common error is to compute $\not\partial^2$ component-by-component (writing out $(\gamma^0\partial_0 + \gamma^1\partial_1 + \cdots)^2$ as a sum of 16 cross-terms), each of which must be carefully handled with signs; the symmetrisation trick collapses all this into a one-line calculation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Expand $\not\partial^2 = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu$; use $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$ to symmetrize the gamma matrix factor; apply the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$ to get $\not\partial^2 = \Box \cdot I$. Combined with the Dirac equation, this gives $\Box\psi = m^2\psi$.

**Subgoal decomposition:**

1. **Subgoal 1: $\not\partial^2 = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu$.**
   - *Hint:* Apply $\not\partial = \gamma^\mu\partial_\mu$ twice. The gamma matrices are constants, so they commute with the partial derivatives.
   - *Why needed:* Sets up the calculation.

2. **Subgoal 2: $\gamma^\mu\gamma^\nu\partial_\mu\partial_\nu = \tfrac{1}{2}\{\gamma^\mu, \gamma^\nu\}\partial_\mu\partial_\nu$.**
   - *Hint:* Symmetrize using $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$.
   - *Why needed:* This is the key algebraic step that forces the use of the Clifford relation.

3. **Subgoal 3: Apply Clifford to conclude $\not\partial^2 = \Box \cdot I$.**
   - *Hint:* $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$, then $\eta^{\mu\nu}\partial_\mu\partial_\nu = \Box$.
   - *Why needed:* This gives the explicit identification $\not\partial^2 = \Box$.

4. **Subgoal 4: Apply to a Dirac solution to get Klein-Gordon.**
   - *Hint:* $\not\partial(m\psi) = m\not\partial\psi = m^2\psi$ using the Dirac equation twice.
   - *Why needed:* This gives the final statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: Symmetrisation by commuting partial derivatives.
> **Statement:** For any tensor $T^{\mu\nu}$ that we contract with $\partial_\mu\partial_\nu$, only the symmetric part $T^{(\mu\nu)} = \tfrac{1}{2}(T^{\mu\nu} + T^{\nu\mu})$ contributes:
> $$T^{\mu\nu}\partial_\mu\partial_\nu = T^{(\mu\nu)}\partial_\mu\partial_\nu.$$
>
> **Hint:** $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$ (commutativity of partials on smooth functions). Decompose $T^{\mu\nu}$ into symmetric and antisymmetric parts; the antisymmetric part $T^{[\mu\nu]} = \tfrac{1}{2}(T^{\mu\nu} - T^{\nu\mu})$ contracts to zero with the symmetric $\partial_\mu\partial_\nu$.
>
> **Why needed:** This is the conceptual step justifying the symmetrisation of $\gamma^\mu\gamma^\nu$.
>
> > [!note]- Full proof
> > Write $T^{\mu\nu} = T^{(\mu\nu)} + T^{[\mu\nu]}$. Then $T^{\mu\nu}\partial_\mu\partial_\nu = T^{(\mu\nu)}\partial_\mu\partial_\nu + T^{[\mu\nu]}\partial_\mu\partial_\nu$. For the second term: $T^{[\mu\nu]}\partial_\mu\partial_\nu = -T^{[\nu\mu]}\partial_\mu\partial_\nu = -T^{[\mu\nu]}\partial_\nu\partial_\mu = -T^{[\mu\nu]}\partial_\mu\partial_\nu$ (relabeling dummy indices and using $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$). So the antisymmetric part equals its own negative, hence is zero.

> [!note]- Lemma 2: $\not\partial^2 = \Box \cdot I$.
> **Statement:** $\gamma^\mu\partial_\mu \circ \gamma^\nu\partial_\nu = \eta^{\mu\nu}\partial_\mu\partial_\nu \cdot I = \Box \cdot I$.
>
> **Hint:** Symmetrize by Lemma 1; apply the Clifford relation.
>
> **Why needed:** This is the main operator identity.
>
> > [!note]- Full proof
> > $(\gamma^\mu\partial_\mu)(\gamma^\nu\partial_\nu) = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu$ (gammas are constants). By Lemma 1, this equals $\tfrac{1}{2}(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu)\partial_\mu\partial_\nu$ (the symmetric part of $\gamma^\mu\gamma^\nu$). By the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$, this is $\eta^{\mu\nu}\partial_\mu\partial_\nu \cdot I = \Box \cdot I$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Setup.** The Dirac equation is $\not\partial\psi = m\psi$ with $\not\partial = \gamma^\mu\partial_\mu$ and the gamma matrices satisfying $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$ in Frankel's signature $\eta = \mathrm{diag}(-1, +1, +1, +1)$.
>
> **Step 1 — Compute $\not\partial^2$ as an operator.** $\not\partial^2 = (\gamma^\mu\partial_\mu)(\gamma^\nu\partial_\nu) = \gamma^\mu\gamma^\nu\partial_\mu\partial_\nu$, since the gamma matrices are constant matrices (independent of position).
>
> **Step 2 — Symmetrise the indices.** Since $\partial_\mu\partial_\nu = \partial_\nu\partial_\mu$ on smooth functions (Lemma 1), the contraction $\gamma^\mu\gamma^\nu\partial_\mu\partial_\nu$ depends only on the *symmetric* part of $\gamma^\mu\gamma^\nu$:
> $$\gamma^\mu\gamma^\nu\partial_\mu\partial_\nu = \tfrac{1}{2}(\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu)\partial_\mu\partial_\nu = \tfrac{1}{2}\{\gamma^\mu, \gamma^\nu\}\partial_\mu\partial_\nu.$$
>
> **Step 3 — Apply the Clifford relation.** Substituting $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I$:
> $$\not\partial^2 = \tfrac{1}{2} \cdot 2\eta^{\mu\nu}I \cdot \partial_\mu\partial_\nu = \eta^{\mu\nu}\partial_\mu\partial_\nu \cdot I = \Box \cdot I.$$
>
> **Step 4 — Apply to a Dirac solution.** Let $\psi$ satisfy $\not\partial\psi = m\psi$. Apply $\not\partial$ again: $\not\partial^2\psi = \not\partial(m\psi) = m\not\partial\psi = m^2\psi$. Combined with Step 3, $\Box\psi = m^2\psi$ — the Klein-Gordon equation.

---

# Cross-Field Exercise Suggestions

1. **Curved-spacetime Lichnerowicz formula.** Generalize the calculation to a curved spin manifold: compute $\not D^2$ for the curved-spacetime Dirac operator, using the spin connection's curvature to pick up the additional $R/4$ scalar-curvature term. See [[Thm - Lichnerowicz Formula]].

2. **Twisted Dirac operator on a gauge field.** Compute the square of $\not D_A = \gamma^\mu(\partial_\mu - ieA_\mu)$ for an electromagnetic potential $A_\mu$. The result includes the gauge curvature: $\not D_A^2 = (D^\mu D_\mu) I - \tfrac{ie}{2}\sigma^{\mu\nu}F_{\mu\nu}$, where $\sigma^{\mu\nu} = \tfrac{i}{2}[\gamma^\mu, \gamma^\nu]$. The second term is the **Pauli term** that couples the spin to the electromagnetic field, predicting the electron's gyromagnetic ratio $g = 2$.

3. **Higher-dimensional Dirac operators.** In $D$ spacetime dimensions, the gamma matrices are $2^{\lfloor D/2\rfloor} \times 2^{\lfloor D/2\rfloor}$, and the same calculation gives $\not\partial^2 = \Box \cdot I$ on a $2^{\lfloor D/2\rfloor}$-component spinor. The $D = 10$ case is fundamental for superstring theory.

---

# Bridges

- **[[Thm - Lichnerowicz Formula|Lichnerowicz formula]] — the curved generalisation.** On a closed Riemannian spin manifold, $\not D^2 = -\nabla^{S*}\nabla^S + R/4$. The flat-space identity $\not\partial^2 = \Box$ is the special case where the scalar curvature $R$ vanishes. The proof uses the same symmetrisation trick on the gamma matrices, but the cross-terms $[\nabla^S_\mu, \nabla^S_\nu]$ now include the curvature of the spin connection, leading to the $R/4$ term.

- **Maxwell-type equations as square roots.** The Dirac equation isn't the only example of "first-order = square root of second-order"; the **Cauchy–Riemann equations** $\partial_x u = \partial_y v, \partial_y u = -\partial_x v$ are first-order, and their solutions $u + iv$ satisfy the *Laplace equation* $(\partial_x^2 + \partial_y^2)(u + iv) = 0$. Squaring the Dirac equation is the relativistic spin-$\tfrac{1}{2}$ analog of squaring the Cauchy–Riemann equations.

- **Maxwell's equations as a "Dirac equation" for spin-1.** Free Maxwell's equations in curved space can be written as $(d + d^*)F = 0$ for the 2-form field strength $F$; here $d + d^*$ is the Hodge–de Rham operator, which squares to the Hodge Laplacian. This is exactly analogous: Dirac is to spin-$\tfrac{1}{2}$ as Hodge is to all forms; both are "square roots" of Laplacian-type operators. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

---

# Unlocked by This

> [!tip] Lichnerowicz Vanishing Theorem
> The flat-space identity $\not\partial^2 = \Box$ generalises to the curved case via the [[Thm - Lichnerowicz Formula|Lichnerowicz formula]] $\not D^2 = -\nabla^{S*}\nabla^S + R/4$. The immediate consequence: on a closed Riemannian spin manifold of strictly positive scalar curvature ($R > 0$), the integral $\int_M \langle\not D\psi, \not D\psi\rangle = \int_M(\|\nabla^S\psi\|^2 + R|\psi|^2/4) > 0$ for $\psi \neq 0$, so $\ker\not D = 0$ — no nontrivial harmonic spinors. This is the **Lichnerowicz vanishing theorem**, giving a topological obstruction to positive-scalar-curvature metrics on spin manifolds.

> [!tip] Negative-Energy Solutions and Antimatter
> The Klein-Gordon equation $\Box\psi = m^2\psi$ admits *both* positive- and negative-energy plane-wave solutions $\psi \propto e^{\mp i Et}$ with $E^2 = \vec p^2 + m^2$. Since the Dirac equation implies Klein-Gordon, the Dirac equation also has negative-energy solutions, which Dirac (1928–1931) interpreted as a "sea" of filled negative-energy states with "holes" appearing as positively-charged particles — the **positron**. Experimental discovery (Anderson, 1932) confirmed this; in modern quantum field theory, the negative-energy solutions become antiparticle creation operators in the second-quantized Dirac field. The very existence of antimatter is forced by the squared-equation structure.

> [!tip] Spinor Helicity and Massless Limit
> For *massless* particles ($m = 0$), the Dirac equation $\not\partial\psi = 0$ implies $\Box\psi = 0$, the standard wave equation. The corresponding plane-wave solutions $\psi(x) = u(p)e^{-ip\cdot x}$ are on the light-cone $p^2 = 0$. In this case the Dirac equation reduces (via chirality decomposition) to two independent Weyl equations, and the polarisation spinor $u(p)$ has half as many independent components — the **massless helicity** structure. See [[Def - Weyl Spinor]].
