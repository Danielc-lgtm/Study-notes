---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Bianchi Identity for Principal Connections"
  - "Def - Curvature 2-Form on a Principal Bundle"
  - "Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection"
tags: [geometry, gauge-theory, electromagnetism, maxwell, bianchi]
---

# Problem Statement

Specialise the **Bianchi identity** $d_\omega\Omega = d\Omega + [\omega, \Omega] = 0$ for principal connections to the abelian case $G = U(1)$ — equivalently $\mathfrak{g} = \mathfrak{u}(1) = i\mathbb{R}$, $[\,\cdot\,,\,\cdot\,]_{\mathfrak{u}(1)} = 0$ — and verify it reduces to the **electromagnetic Bianchi identity**
$$
dF = 0.
$$

**(a)** Show that for an abelian gauge group $G$, the principal-bundle Bianchi identity collapses to the statement that the curvature 2-form is closed: $dF = 0$.

**(b)** In Minkowski space $\mathbb{R}^{1,3}$ with $F = \tfrac{1}{2}F_{\mu\nu}dx^\mu \wedge dx^\nu$ and $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, explicitly expand $dF = 0$ in components. Show the four equations $\partial_{[\rho}F_{\mu\nu]} = 0$ (cyclic in $\rho, \mu, \nu$) reduce to the two physical Maxwell equations:
$$
\nabla \cdot \mathbf{B} = 0, \quad \nabla \times \mathbf{E} + \partial_t \mathbf{B} = 0,
$$
where $\mathbf{E}^i = F^{0i}$ and $\mathbf{B}^k = -\tfrac{1}{2}\varepsilon^{ijk}F_{ij}$ are the electric and magnetic fields.

**(c)** Verify that the Bianchi identity holds automatically when $F = dA$ for some 1-form $A$ (which holds locally on any contractible region of $M$): $dF = d^2A = 0$. Conclude that the Bianchi identity is "$F$ is locally exact", and this *is* the statement of the absence of magnetic monopoles.

**Recall:**

The Bianchi identity: ![[Thm - Bianchi Identity for Principal Connections#Statement]]

For abelian Lie algebras (like $\mathfrak{u}(1)$), the bracket $[\,\cdot\,,\,\cdot\,]$ vanishes identically: $[\xi, \eta] = 0$ for all $\xi, \eta \in \mathfrak{u}(1)$.

The electromagnetic field strength tensor in Minkowski space is $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ with $\mu, \nu \in \{0, 1, 2, 3\}$. The 4-potential is $A_\mu = (\phi, -\mathbf{A})$ in MTW/Wald convention or $(\phi, \mathbf{A})$ depending on signature.

The electromagnetic invariants: $\mathbf{E}^i = F^{0i} = \partial^0 A^i - \partial^i A^0$ (electric field), $\mathbf{B}^k = -\tfrac{1}{2}\varepsilon^{ijk}F_{ij} = \nabla \times \mathbf{A}$ (magnetic field).

---

# Convergent Strategy

**Problem class:** This is a *specialisation* problem: take a general principal-bundle theorem (Bianchi for any $G$) and reduce it to a familiar special case (electromagnetism for $G = U(1)$). The general pattern recognises that the abelian special case of any gauge-theoretic formula simplifies dramatically — the bracket $[\,\cdot\,,\,\cdot\,]$ vanishes, the inhomogeneous gauge term becomes $d\chi$, the adjoint bundle becomes trivial.

**Assumption pattern:** $G = U(1)$ — abelian, 1-dimensional, $\mathfrak{u}(1) = i\mathbb{R}$. Base $M = \mathbb{R}^{1,3}$ (Minkowski space) with a Lorentzian metric. A $U(1)$-connection with gauge potential $A_\mu(x)$ and field strength $F_{\mu\nu}$.

**Theorem routing:** [[Thm - Bianchi Identity for Principal Connections|principal Bianchi identity]] → set $[\omega, \Omega] = 0$ (abelian) → $d\Omega = 0$ → pull back to $dF = 0$ on the base. Expand in components: $dF = 0 \Leftrightarrow \partial_{[\rho}F_{\mu\nu]} = 0 \Leftrightarrow$ the four equations, two of which are $\nabla \cdot \mathbf{B} = 0$ and two of which are $\nabla \times \mathbf{E} + \partial_t \mathbf{B} = 0$.

**Key decision point:** The non-obvious physical content is that the *geometric* identity $dF = 0$ is *exactly* the two "magnetic / inductive" Maxwell equations — half of Maxwell's electromagnetism. The other two equations ($\nabla \cdot \mathbf{E} = \rho$ and $\nabla \times \mathbf{B} - \partial_t \mathbf{E} = \mathbf{j}$) come from the *dynamical* Yang-Mills equation $d_\omega \star F = \star j$, derived from a variational principle, not from a geometric identity. Distinguishing the two is the conceptual point.

---

# Legal Operations Used

4. **Operation 4 (Bianchi identity).** Apply the abelian Bianchi $dF = 0$ to derive the magnetic and inductive Maxwell equations.

10. **Operation 10 (abelian sanity check).** $G = U(1)$ abelian: $[A, F] = 0$, $\mathrm{Ad}_g\xi = \xi$, $F = dA$. Use this to simplify the general formulas.

---

# Hints

> [!note]- Hint 1
> For part (a): in the general Bianchi $d_\omega F = dF + [A, F] = 0$, the term $[A, F]$ is the bracket of a 1-form $A$ and a 2-form $F$, both valued in $\mathfrak{g} = \mathfrak{u}(1)$. The bracket on $\mathfrak{u}(1)$ vanishes ($\mathfrak{u}(1)$ is abelian), so $[A, F] = 0$ as a $\mathfrak{u}(1)$-valued 3-form on $M$. Hence Bianchi reduces to $dF = 0$.

> [!note]- Hint 2
> For part (b): $F = \tfrac{1}{2}F_{\mu\nu}dx^\mu \wedge dx^\nu$. Compute $dF = \tfrac{1}{2}\partial_\rho F_{\mu\nu}\,dx^\rho \wedge dx^\mu \wedge dx^\nu = \tfrac{1}{6}(\partial_\rho F_{\mu\nu} + \partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu})\,dx^\rho \wedge dx^\mu \wedge dx^\nu$ (after antisymmetrising in the wedge). Setting equal to zero gives $\partial_{[\rho}F_{\mu\nu]} = 0$ for all $\rho, \mu, \nu$.

> [!note]- Hint 3
> There are $\binom{4}{3} = 4$ choices for $(\rho, \mu, \nu)$ in 4D: $(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)$. The first three (those involving the time index $0$) give the **inductive Maxwell equations** $\nabla \times \mathbf{E} + \partial_t \mathbf{B} = 0$ (three components). The last one $(1, 2, 3)$ (purely spatial) gives the **magnetic Gauss law** $\nabla \cdot \mathbf{B} = 0$.

> [!note]- Hint 4
> Explicitly: $(\rho, \mu, \nu) = (1, 2, 3)$ gives $\partial_1 F_{23} + \partial_2 F_{31} + \partial_3 F_{12} = 0$. Using $F_{ij} = -\varepsilon_{ijk}B^k$ (with appropriate signs in Lorentzian), this is $\partial_1 B^1 + \partial_2 B^2 + \partial_3 B^3 = \nabla \cdot \mathbf{B} = 0$.

> [!note]- Hint 5
> $(\rho, \mu, \nu) = (0, 1, 2)$ gives $\partial_0 F_{12} + \partial_1 F_{20} + \partial_2 F_{01} = 0$. Using $F_{01} = -E^1, F_{02} = -E^2, F_{12} = -B^3$ (signs depend on convention), this becomes $-\partial_t B^3 + \partial_1 E^2 - \partial_2 E^1 = 0$, i.e., $(\nabla \times \mathbf{E})^3 + \partial_t B^3 = 0$ — the 3-component of Faraday's law. The other two components come from $(\rho, \mu, \nu) = (0, 1, 3)$ and $(0, 2, 3)$.

---

# Solution

**Plan:** Apply the abelian special case $[A, F] = 0$ to the general Bianchi identity, reducing it to $dF = 0$. Expand $dF = 0$ in Minkowski-space components and identify the magnetic Gauss law and Faraday's law. Note that the Bianchi identity is automatic from $F = dA$ via $d^2 = 0$.

**Step 1: Abelian Bianchi reduces to $dF = 0$.**

> [!note]- Derivation
> General Bianchi: $d_\omega F = dF + [A, F] = 0$. For $G = U(1)$, $\mathfrak{g} = \mathfrak{u}(1) = i\mathbb{R}$ is abelian — the Lie bracket on $\mathfrak{u}(1)$ vanishes identically: $[\xi, \eta] = 0$ for all $\xi, \eta \in i\mathbb{R}$.
> 
> The bracket of a $\mathfrak{u}(1)$-valued 1-form $A$ with a $\mathfrak{u}(1)$-valued 2-form $F$ is, by the [[Def - Bracket of g-Valued Forms|bracket-of-forms definition]],
> $$
> [A, F] = (A \wedge F) \otimes [\xi_A, \xi_F]_{\mathfrak{u}(1)} = 0.
> $$
> (More carefully: in a basis $\{i\}$ of $\mathfrak{u}(1)$, $A = i \cdot A^{(1)}$ and $F = i \cdot F^{(1)}$ with $A^{(1)}, F^{(1)}$ ordinary forms; $[A, F] = [i, i] \otimes A^{(1)} \wedge F^{(1)} = 0 \otimes A^{(1)} \wedge F^{(1)} = 0$.)
> 
> So the Bianchi identity reduces to $dF = 0$. ✓

**Step 2: $dF = 0$ in Minkowski components.**

$F = \tfrac{1}{2}F_{\mu\nu}dx^\mu \wedge dx^\nu \in \Omega^2(\mathbb{R}^{1,3})$ with $F_{\mu\nu} = -F_{\nu\mu}$. Compute $dF$:

> [!note]- Derivation
> $$
> dF = \tfrac{1}{2}\partial_\rho F_{\mu\nu}\,dx^\rho \wedge dx^\mu \wedge dx^\nu.
> $$
> Antisymmetrising over $(\rho, \mu, \nu)$:
> $$
> dF = \tfrac{1}{2}\cdot\tfrac{1}{3}(\partial_\rho F_{\mu\nu} + \partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu})\,dx^\rho \wedge dx^\mu \wedge dx^\nu \cdot 3 = \tfrac{1}{2}(\partial_\rho F_{\mu\nu} + \partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu})\,(dx^\rho \wedge dx^\mu \wedge dx^\nu)/3,
> $$
> 
> wait — let me re-do this. We have $dx^\rho \wedge dx^\mu \wedge dx^\nu$ is totally antisymmetric in $(\rho, \mu, \nu)$, so summing $\partial_\rho F_{\mu\nu}$ over all permutations gives $6\partial_{[\rho}F_{\mu\nu]}$ — the totally antisymmetric combination. So
> $$
> dF = \tfrac{1}{2}\,3!\partial_{[\rho}F_{\mu\nu]}\,dx^\rho \wedge dx^\mu \wedge dx^\nu/3! = \partial_{[\rho}F_{\mu\nu]}\,dx^\rho \wedge dx^\mu \wedge dx^\nu.
> $$
> Setting $dF = 0$:
> $$
> \partial_{[\rho}F_{\mu\nu]} = 0 \iff \partial_\rho F_{\mu\nu} + \partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu} = 0
> $$
> for all $\rho, \mu, \nu$. ✓

**Step 3: Identify the magnetic and inductive Maxwell equations.**

> [!note]- Derivation
> In Minkowski signature $(-, +, +, +)$ (or $(+, -, -, -)$, with conventions adjusted), define $\mathbf{E}^i = F^{0i}$ and $\mathbf{B}^k = -\tfrac{1}{2}\varepsilon^{ijk}F_{ij}$ (signs depending on convention; we use the convention where $F^{0i} = -F_{0i}$ in $(-, +, +, +)$ but $F^{0i} = F_{0i}$ in $(+, -, -, -)$).
> 
> **Equation $(\rho, \mu, \nu) = (1, 2, 3)$:**
> $$
> \partial_1 F_{23} + \partial_2 F_{31} + \partial_3 F_{12} = 0.
> $$
> Using $F_{23} = -B^1, F_{31} = -B^2, F_{12} = -B^3$ (the signs are such that $\mathbf{B}^k = -\tfrac{1}{2}\varepsilon^{ijk}F_{ij}$):
> $$
> -\partial_1 B^1 - \partial_2 B^2 - \partial_3 B^3 = 0 \iff \nabla \cdot \mathbf{B} = 0.
> $$
> **Magnetic Gauss law: no magnetic monopoles.** ✓
> 
> **Equations involving $(\rho, \mu, \nu) = (0, j, k)$ for spatial $j, k$:**
> $$
> \partial_0 F_{jk} + \partial_j F_{k0} + \partial_k F_{0j} = 0.
> $$
> With $F_{jk} = -\varepsilon_{jkl}B^l$, $F_{j0} = -E^j$ (or $E^j$, convention), so $F_{k0} = -E^k$ and $F_{0j} = E^j$:
> $$
> -\partial_0 \varepsilon_{jkl}B^l + \partial_j(-E^k) + \partial_k E^j = -\partial_t \varepsilon_{jkl}B^l - (\partial_j E^k - \partial_k E^j) = 0.
> $$
> Recognising $\partial_j E^k - \partial_k E^j = \varepsilon_{jkn}(\nabla \times \mathbf{E})^n$ (3D curl in components):
> $$
> -\partial_t \varepsilon_{jkl}B^l - \varepsilon_{jkn}(\nabla \times \mathbf{E})^n = 0 \iff \varepsilon_{jkl}[\partial_t B^l + (\nabla \times \mathbf{E})^l] = 0.
> $$
> Since this holds for all $(j, k)$, the bracket vanishes: $\partial_t \mathbf{B} + \nabla \times \mathbf{E} = 0$. **Faraday's law of induction.** ✓
> 
> (Sign conventions differ in the literature; the structure of the derivation is the same. The four equations $\partial_{[\rho}F_{\mu\nu]} = 0$ in 4D reduce to the *one* magnetic Gauss equation $(1, 2, 3)$ + the *three* components of Faraday's law $(0, j, k)$, exactly the two "geometric / inductive" Maxwell equations.)

**Step 4: Bianchi from $F = dA$.**

> [!note]- Derivation
> Locally (on contractible regions of $M$), the gauge potential $A$ is defined, and $F = dA$ — this is the abelian Cartan structural equation. Then $dF = d(dA) = d^2 A = 0$ by the fundamental property of the exterior derivative.
> 
> So the Bianchi identity $dF = 0$ is *automatic* whenever $F = dA$ locally. The non-existence of magnetic monopoles is then the statement "$F$ is the exterior derivative of a 1-form locally — i.e., $F$ is closed". This is *geometric*, not *physical*.
> 
> **Why monopoles violate Bianchi:** if a magnetic monopole exists, then $F$ is *not* exact globally (the Dirac string is the failure of $F = dA$ to hold on a closed surface enclosing the monopole), and $\int_S F \neq 0$ for a sphere $S$ around the monopole — which would violate $dF = 0$ if integrated naively, but in the proper bundle-theoretic formulation, $dF = 0$ holds locally on each chart and the integral $\int_S F = 4\pi g$ (with $g$ the magnetic charge) is the topological invariant of the $U(1)$-bundle, *not* a violation of Bianchi.

> [!note]- Complete formal solution
> **Step 1.** The Bianchi identity $d_\omega F = dF + [A, F] = 0$ for principal connections. For $G = U(1)$ abelian: $[A, F] = 0$ (bracket on $\mathfrak{u}(1)$ vanishes). So Bianchi reduces to
> $$
> dF = 0
> $$
> on Minkowski space (or any base $M$).
> 
> **Step 2.** In components $F = \tfrac{1}{2}F_{\mu\nu}dx^\mu \wedge dx^\nu$, $dF = \partial_{[\rho}F_{\mu\nu]}\,dx^\rho \wedge dx^\mu \wedge dx^\nu$. Setting equal to zero:
> $$
> \partial_\rho F_{\mu\nu} + \partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu} = 0 \quad \forall (\rho, \mu, \nu).
> $$
> 
> **Step 3.** With $E^i = F^{0i}$ and $B^k = -\tfrac{1}{2}\varepsilon^{ijk}F_{ij}$, the four equations reduce to:
> - $(\rho, \mu, \nu) = (1, 2, 3)$: $\nabla \cdot \mathbf{B} = 0$ (magnetic Gauss law: no monopoles).
> - $(\rho, \mu, \nu) = (0, j, k)$: $\partial_t \mathbf{B} + \nabla \times \mathbf{E} = 0$ (Faraday's law of induction).
> 
> **Step 4.** Locally $F = dA$, so $dF = d^2A = 0$ automatically. The Bianchi identity is the geometric statement that $F$ is locally exact — physically, the absence of magnetic monopoles in the *local* picture. Globally, the absence requires the principal $U(1)$-bundle to have trivial first Chern class $c_1(P) = 0$. ∎

---

# Key Takeaways

**Bianchi is a geometric identity, not a dynamical equation.** The two halves of Maxwell's equations are *fundamentally different*. The "geometric" half ($dF = 0$: magnetic Gauss + Faraday) is the **Bianchi identity**, an automatic consequence of $F = dA$. It contains no physics — it is true for every connection. The "dynamical" half ($d \star F = \star j$: electric Gauss + Ampère-Maxwell) is the **Yang-Mills equation**, derived from extremising the action $S = -\tfrac{1}{4}\int F \wedge \star F$ on the space of connections. It contains all the physical content of electromagnetism. Distinguishing these two is one of the most important conceptual points in classical field theory.

**The absence of magnetic monopoles is geometric.** $\nabla \cdot \mathbf{B} = 0$ is a Bianchi-identity consequence of $\mathbf{B} = \nabla \times \mathbf{A}$ — automatic, not physical. Dirac's monopole construction shows that magnetic monopoles can be accommodated by relaxing "$\mathbf{B} = \nabla \times \mathbf{A}$ globally" to "$\mathbf{A}$ exists only locally, on charts, with transition functions on overlaps", which is exactly the principal-bundle picture. The Dirac quantisation condition $eg = 2\pi n$ then follows from the cocycle condition for $U(1)$-valued transition functions.

**The non-abelian generalisation $dF + [A, F] = 0$ contains additional "cross-coupling" terms.** For non-abelian $G$, the Bianchi identity is $dF + [A, F] = 0$, with the extra term $[A, F]$ coupling the gauge field to the field strength via the structure constants. In QCD components: $\partial_\mu F^a_{\nu\rho} + \text{cyclic} + f^a{}_{bc}(A^b_\mu F^c_{\nu\rho} + \text{cyclic}) = 0$. The non-abelian Bianchi is the cleanest way to write down the analogous "magnetic Gauss + Faraday" conditions for colour fields, and it is what would be violated by a "colour magnetic monopole" — though no such object is known in nature.

**Trigger-reaction pattern: "verify dF = 0" → "$F$ is closed, locally exact, no obstruction to magnetic potential".** This pattern recognises that the abelian Bianchi identity is equivalent to $F$ being closed, hence locally exact (by Poincaré's lemma). Globally exact requires the second cohomology class $[F] \in H^2(M; \mathbb{R})$ to vanish — and for non-trivial bundles, $[F] \neq 0$, the integral $\int_{\Sigma} F$ over a 2-cycle is the topological invariant of the bundle (the first Chern number for $U(1)$-bundles, the magnetic charge for Dirac monopoles).
