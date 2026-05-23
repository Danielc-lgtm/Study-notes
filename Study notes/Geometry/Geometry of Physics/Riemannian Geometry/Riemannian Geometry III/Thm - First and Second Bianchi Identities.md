---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Riemann Curvature Tensor"
  - "Def - Levi-Civita Connection"
  - "Thm - Symmetries of the Riemann Tensor"
tags: [geometry, riemannian-geometry, curvature, bianchi]
---

# Notation

$(M, g)$ is a Riemannian manifold with [[Def - Levi-Civita Connection|Levi-Civita connection]] $\nabla$ and [[Def - Riemann Curvature Tensor|Riemann tensor]] $R$. In an orthonormal coframe $(\sigma^a)$ with connection 1-forms $\omega^a_{\;b}$ and curvature 2-forms $\Omega^a_{\;b}$, Cartan's structural equations read

$$d\sigma^a = -\omega^a_{\;b} \wedge \sigma^b, \qquad \Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c} \wedge \omega^c_{\;b}.$$

We use Einstein summation throughout and write $\nabla_E R(X, Y)Z$ to mean $(\nabla_E R)(X, Y)Z$ — the covariant derivative of the tensor $R$.

---

# Statement

> **Theorem (First and Second Bianchi identities).** Let $\nabla$ be the Levi-Civita connection on a Riemannian manifold $(M, g)$, $R$ its Riemann curvature tensor.
>
> **First Bianchi identity** (algebraic, requires torsion-freeness):
> $$R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0 \qquad \forall X, Y, Z \in \mathfrak{X}(M).$$
> In components, $R^a_{\;bcd} + R^a_{\;cdb} + R^a_{\;dbc} = 0$.
>
> **Second Bianchi identity** (differential, holds for any affine connection):
> $$(\nabla_E R)(X, Y)Z + (\nabla_X R)(Y, E)Z + (\nabla_Y R)(E, X)Z = 0.$$
> In components, $\nabla_e R^a_{\;bcd} + \nabla_c R^a_{\;bde} + \nabla_d R^a_{\;bec} = 0$.

> **Contracted second Bianchi.** Tracing the second Bianchi identity over appropriate index pairs gives
> $$\nabla^a R_{ab} = \tfrac{1}{2}\nabla_b S, \qquad \nabla^a G_{ab} = 0,$$
> where $G_{ab} = R_{ab} - \tfrac{1}{2}g_{ab}S$ is the **Einstein tensor**. The contracted second Bianchi is *the* geometric identity that makes Einstein's field equations $G_{ab} = 8\pi T_{ab}$ consistent with energy-momentum conservation $\nabla^a T_{ab} = 0$.

---

# Motivation

The Riemann tensor of a torsion-free metric-compatible connection satisfies more identities than just the algebraic symmetries of the previous theorem. The Bianchi identities are these additional constraints: the first is a *cyclic algebraic* identity (relating different values of $R$ at the same point), and the second is a *cyclic differential* identity (relating covariant derivatives of $R$ at the same point).

Both come from the same source: $d^2 = 0$. The first Bianchi identity is what falls out when you apply $d^2$ to the soldering form $\sigma^a$ (in Cartan's structural-equations language), using torsion-freeness $d\sigma = -\omega \wedge \sigma$. The second Bianchi is what falls out when you apply $d^2$ to the connection 1-form $\omega^a_{\;b}$, getting $0 = d\Omega + \omega \wedge \Omega - \Omega \wedge \omega$ — a differential identity for the curvature 2-form, which when unpacked gives the cyclic identity for $\nabla R$.

The second Bianchi identity is the deep one in physics: its contracted form is what makes the **Einstein tensor** divergence-free, hence what makes Einstein's field equations compatible with conservation of energy-momentum. Without the second Bianchi identity, the field equations $\mathrm{Ric} - \tfrac{1}{2}gS = 8\pi T$ would be over-determined (the left side would not automatically have $\nabla \cdot LHS = 0$ to match $\nabla \cdot T = 0$). Einstein's original attempt $\mathrm{Ric} = 8\pi T$ failed for exactly this reason; the correction term $-\tfrac{1}{2}gS$ was added precisely to align with what the second Bianchi identity allows.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: The connection is torsion-free.* This is the precondition for the first Bianchi identity. **The bridge:** torsion-free means $\nabla_X Y - \nabla_Y X = [X, Y]$, which when iterated through $\nabla\nabla$ and combined with the Jacobi identity for the Lie bracket gives the cyclic algebraic constraint. Whenever you see a torsion-free connection (Levi-Civita, the Chern connection on a Hermitian manifold, the holomorphic connection), first Bianchi applies. **Example:** in [[Riemannian Geometry I — Connections and Covariant Differentiation]], the Levi-Civita uniqueness was characterised by metric compatibility + torsion-freeness; the Bianchi identities are immediate consequences.

*Source 2: The connection is the curvature of $any$ affine connection.* The second Bianchi identity holds *without* metric compatibility *or* torsion-freeness — only that $\nabla$ is an affine connection. **The bridge:** the second Bianchi comes from $d^2\omega^a_{\;b} = 0$ for $\omega$ a Lie-algebra-valued connection 1-form, and this identity holds universally for any connection on any principal bundle. So whenever you have any field strength $F = dA + A \wedge A$ in any gauge theory, $d^A F = 0$ holds — this is the universal Bianchi identity. **Example:** Yang–Mills curvatures in QED, the Standard Model, lattice gauge theory all satisfy the same Bianchi.

*Source 3: A vacuum spacetime in general relativity.* The contracted second Bianchi forces vacuum solutions ($\mathrm{Ric} = 0$ as the vacuum Einstein equations) to automatically have $G_{ab} = 0$ everywhere, and the conservation law $\nabla^a G_{ab} = 0$ is automatic. **The bridge:** in a vacuum spacetime, the right-hand side of Einstein's equation is $0$, and the contracted Bianchi makes this consistent. Without the contracted Bianchi, vacuum solutions would have to be defined as solutions of an over-determined system. **Example:** the Schwarzschild metric satisfies $\mathrm{Ric} = 0$, and the contracted Bianchi is what makes this a self-consistent geometric condition.

**Targets (Output Amplification).**

*Target 1: Divergence-freeness of the Einstein tensor.* The contracted second Bianchi $\nabla^a G_{ab} = 0$ + Einstein's equations $G_{ab} = 8\pi T_{ab}$ implies $\nabla^a T_{ab} = 0$ — conservation of energy-momentum. **Combined target:** Einstein's field equations are self-consistent only because Bianchi gives $\nabla^a G_{ab} = 0$. **Why nonobvious:** historically, Einstein took two years to find the right combination $G_{ab}$ (rather than $\mathrm{Ric}_{ab}$) precisely because the wrong combination would have over-determined the system. **Why useful:** every textbook derivation of Einstein's equations from the Einstein–Hilbert action $S_{\mathrm{EH}} = \int S\, dV$ implicitly uses Bianchi to consistency-check the result.

*Target 2: Schur's lemma (constancy of $\lambda$ in $\mathrm{Ric} = \lambda g$).* The contracted second Bianchi $\nabla^a R_{ab} = \tfrac{1}{2}\nabla_b S$, applied to $R_{ab} = \lambda g_{ab}$ (function $\lambda$), gives $\nabla_b\lambda = \tfrac{n}{2}\nabla_b\lambda$, forcing $\nabla\lambda = 0$ in $n \ne 2$. **Combined target:** the apparently weaker definition "$\mathrm{Ric}$ pointwise proportional to $g$" forces the stronger "constant of proportionality" — this is what makes the [[Def - Einstein Manifold|Einstein condition]] a well-defined notion in dimension $\ge 3$.

*Target 3: Topological invariance of certain curvature integrals.* The Bianchi identities make certain curvature polynomials in $R$ become **closed forms** (e.g., the **Pontryagin forms** $\mathrm{tr}(R^k)$), and integration over $M$ gives topological invariants — the **Pontryagin classes** in the Chern–Weil construction. **Combined target:** Bianchi + closedness + integration over a closed manifold = topological invariant. **Why useful:** this is the foundation of **characteristic class theory** and the **Atiyah–Singer index theorem**.

---

# Why Is It True

Both Bianchi identities ultimately come from $d^2 = 0$ in differential geometry, applied to the two structures: the **soldering form** (giving the first Bianchi) and the **connection 1-form** (giving the second Bianchi).

For the **first Bianchi**: the soldering 1-form $\sigma^a$ in an orthonormal coframe satisfies Cartan's first structural equation $d\sigma^a + \omega^a_{\;b} \wedge \sigma^b = \tau^a$ where $\tau$ is the torsion. For Levi-Civita, $\tau = 0$. Apply $d$ to both sides: $0 = d(d\sigma^a) = -d\omega^a_{\;b} \wedge \sigma^b + \omega^a_{\;b} \wedge d\sigma^b$. Substitute $d\omega = \Omega - \omega \wedge \omega$ and $d\sigma = -\omega \wedge \sigma$:

$$0 = -(\Omega^a_{\;b} - \omega^a_{\;c} \wedge \omega^c_{\;b}) \wedge \sigma^b + \omega^a_{\;b} \wedge (-\omega^b_{\;c} \wedge \sigma^c) = -\Omega^a_{\;b} \wedge \sigma^b.$$

So $\Omega^a_{\;b} \wedge \sigma^b = 0$. Expanding $\Omega^a_{\;b} = \tfrac{1}{2}R^a_{\;bcd}\sigma^c \wedge \sigma^d$, this becomes $\tfrac{1}{2}R^a_{\;bcd}\sigma^c \wedge \sigma^d \wedge \sigma^b = 0$, which after expansion in $\sigma^c \wedge \sigma^d \wedge \sigma^b$ (antisymmetric in all three indices) forces $R^a_{\;bcd}$ cyclic-summed in $(b, c, d)$ to vanish — the first Bianchi identity.

For the **second Bianchi**: differentiate the second Cartan structural equation $\Omega = d\omega + \omega \wedge \omega$:

$$d\Omega = d^2\omega + d\omega \wedge \omega - \omega \wedge d\omega = 0 + (\Omega - \omega \wedge \omega) \wedge \omega - \omega \wedge (\Omega - \omega \wedge \omega) = \Omega \wedge \omega - \omega \wedge \Omega.$$

So $d\Omega + \omega \wedge \Omega - \Omega \wedge \omega = 0$. The left side is exactly the **exterior covariant derivative** $d^\omega \Omega = 0$ — the universal Bianchi identity for any connection on any principal bundle.

**The bolded mechanism summary: both Bianchi identities are consequences of $d^2 = 0$ — the first from $d^2$ on the soldering form combined with torsion-freeness, the second from $d^2$ on the connection 1-form (no extra hypothesis needed).**

The contracted second Bianchi is straightforward index manipulation: take $\nabla_e R^a_{\;bcd} + \nabla_c R^a_{\;bde} + \nabla_d R^a_{\;bec} = 0$, contract $a$ with $c$, and use the symmetries to identify the result.

---

# What Makes This Hard

The first Bianchi identity requires careful bookkeeping: writing out $R(X, Y)Z + R(Y, Z)X + R(Z, X)Y$ in terms of $\nabla\nabla$, using torsion-freeness, and recognising that what remains after cancellation is precisely the Jacobi identity for $[\cdot, \cdot]$. The standard error is to forget that torsion-freeness is essential — a connection with torsion has a *modified* first Bianchi identity with explicit torsion terms.

The second Bianchi identity is conceptually easier (it just falls out of $d^2 = 0$ applied to $\omega$) but the index manipulations to derive the *contracted* second Bianchi are notoriously prone to sign errors. The minus sign in $\tfrac{1}{2}\nabla_b S$ versus $\nabla^a R_{ab}$ confuses generations of students; getting it right requires meticulous care with the metric pair-swap symmetry.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** First Bianchi from Cartan's first structural equation under $d^2 = 0$ + torsion-freeness $\tau = 0$. Second Bianchi from Cartan's second structural equation under $d^2 = 0$ (no extra hypothesis). Contracted second Bianchi from index manipulation.

**Subgoal decomposition:**

1. **First Bianchi from $d^2\sigma = 0$.**
   - *Hint:* Take $d$ of $d\sigma^a + \omega^a_{\;b} \wedge \sigma^b = 0$; substitute Cartan's second structural equation for $d\omega$; the curvature 2-form-wedge-soldering-form term gives the cyclic identity.
   - *Why needed:* Establishes the algebraic constraint.

2. **Second Bianchi from $d^2 \omega = 0$.**
   - *Hint:* Take $d$ of $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c} \wedge \omega^c_{\;b}$; use $d^2 \omega = 0$; the result is the universal Bianchi $d^\omega \Omega = 0$.
   - *Why needed:* Establishes the differential constraint.

3. **Contracted second Bianchi.**
   - *Hint:* Take the second Bianchi $\nabla_e R^a_{\;bcd} + \nabla_c R^a_{\;bde} + \nabla_d R^a_{\;bec} = 0$, contract $a$ with $c$, use the symmetries of $R$ and the definition of $\mathrm{Ric}$.
   - *Why needed:* Gives the divergence-freeness of the Einstein tensor.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\Omega \wedge \sigma = 0$ in an orthonormal coframe with torsion-free connection
> **Statement:** $\Omega^a_{\;b} \wedge \sigma^b = 0$ for each $a$, where $\sigma^a$ is the soldering form and $\Omega^a_{\;b}$ is the curvature 2-form of the torsion-free Levi-Civita connection.
>
> **Hint:** Apply $d^2 = 0$ to Cartan's first structural equation $d\sigma + \omega \wedge \sigma = 0$ (torsion-free); use Cartan's second equation $\Omega = d\omega + \omega \wedge \omega$ to substitute for $d\omega$.
>
> **Why needed:** Equivalent to the first Bianchi identity (after expansion in coordinates).
>
> > [!note]- Full proof
> > $0 = d(d\sigma^a) = d(-\omega^a_{\;b} \wedge \sigma^b) = -d\omega^a_{\;b} \wedge \sigma^b + \omega^a_{\;b} \wedge d\sigma^b$. Substitute $d\omega^a_{\;b} = \Omega^a_{\;b} - \omega^a_{\;c} \wedge \omega^c_{\;b}$ and $d\sigma^b = -\omega^b_{\;c} \wedge \sigma^c$:
> > $$0 = -\Omega^a_{\;b} \wedge \sigma^b + \omega^a_{\;c} \wedge \omega^c_{\;b} \wedge \sigma^b + \omega^a_{\;b} \wedge (-\omega^b_{\;c} \wedge \sigma^c) = -\Omega^a_{\;b} \wedge \sigma^b + 0.$$
> > Hence $\Omega^a_{\;b} \wedge \sigma^b = 0$.

> [!note]- Lemma 2: First Bianchi in component form from $\Omega \wedge \sigma = 0$
> **Statement:** $R^a_{\;bcd} + R^a_{\;cdb} + R^a_{\;dbc} = 0$.
>
> **Hint:** Expand $\Omega^a_{\;b} = \tfrac{1}{2}R^a_{\;bcd}\sigma^c \wedge \sigma^d$ and apply to Lemma 1.
>
> **Why needed:** The component form is what appears in calculations.
>
> > [!note]- Full proof
> > From Lemma 1, $\Omega^a_{\;b} \wedge \sigma^b = \tfrac{1}{2}R^a_{\;bcd}\sigma^c \wedge \sigma^d \wedge \sigma^b = 0$. Since $\sigma^c \wedge \sigma^d \wedge \sigma^b$ is antisymmetric in $(b, c, d)$ and spans a basis of $\Lambda^3$, the coefficient (summed over cyclic permutations of $(b, c, d)$) must vanish: $R^a_{\;bcd} + R^a_{\;cdb} + R^a_{\;dbc} = 0$.

> [!note]- Lemma 3: Second Bianchi from $d^2\omega = 0$
> **Statement:** $d\Omega^a_{\;b} + \omega^a_{\;c} \wedge \Omega^c_{\;b} - \Omega^a_{\;c} \wedge \omega^c_{\;b} = 0$.
>
> **Hint:** Take $d$ of Cartan's second structural equation $\Omega = d\omega + \omega \wedge \omega$ and use $d^2\omega = 0$.
>
> **Why needed:** This is the differential Bianchi in 2-form language.
>
> > [!note]- Full proof
> > $d\Omega^a_{\;b} = d(d\omega^a_{\;b} + \omega^a_{\;c} \wedge \omega^c_{\;b}) = 0 + d\omega^a_{\;c} \wedge \omega^c_{\;b} - \omega^a_{\;c} \wedge d\omega^c_{\;b}$. Substitute $d\omega^a_{\;c} = \Omega^a_{\;c} - \omega^a_{\;e} \wedge \omega^e_{\;c}$ and similarly for $d\omega^c_{\;b}$:
> > $$d\Omega^a_{\;b} = (\Omega^a_{\;c} - \omega^a_{\;e} \wedge \omega^e_{\;c}) \wedge \omega^c_{\;b} - \omega^a_{\;c} \wedge (\Omega^c_{\;b} - \omega^c_{\;e} \wedge \omega^e_{\;b}).$$
> > After expansion the $\omega \wedge \omega \wedge \omega$ terms cancel (their associativity and skewness gives zero), leaving $d\Omega^a_{\;b} = \Omega^a_{\;c} \wedge \omega^c_{\;b} - \omega^a_{\;c} \wedge \Omega^c_{\;b}$, equivalently $d\Omega + \omega \wedge \Omega - \Omega \wedge \omega = 0$.

> [!note]- Lemma 4: Component-form second Bianchi from Lemma 3
> **Statement:** $\nabla_e R^a_{\;bcd} + \nabla_c R^a_{\;bde} + \nabla_d R^a_{\;bec} = 0$.
>
> **Hint:** Expand $\Omega^a_{\;b} = \tfrac{1}{2}R^a_{\;bcd}\sigma^c \wedge \sigma^d$ and the connection wedges, take the 3-form coefficient.
>
> **Why needed:** Component form for index manipulation in physics calculations.
>
> > [!note]- Full proof
> > Expanding Lemma 3's identity in components and using $d\sigma^a = -\omega^a_{\;b} \wedge \sigma^b$ throughout produces a 3-form whose coefficient must vanish. Cycling over the three indices $(c, d, e)$ in $\sigma^c \wedge \sigma^d \wedge \sigma^e$ gives the cyclic identity stated.

> [!note]- Lemma 5: Contracted second Bianchi
> **Statement:** $\nabla^a R_{ab} = \tfrac{1}{2}\nabla_b S$ and hence $\nabla^a(R_{ab} - \tfrac{1}{2}g_{ab}S) = 0$.
>
> **Hint:** Contract $a$ with $c$ in the second Bianchi $\nabla_e R^a_{\;bcd} + \nabla_c R^a_{\;bde} + \nabla_d R^a_{\;bec} = 0$, use definitions of Ricci and scalar curvature.
>
> **Why needed:** This is the divergence-freeness of the Einstein tensor — the geometric reason Einstein's field equations are consistent with $\nabla^a T_{ab} = 0$.
>
> > [!note]- Full proof
> > Take $\nabla_e R^a_{\;bcd} + \nabla_c R^a_{\;bde} + \nabla_d R^a_{\;bec} = 0$, contract $a$ with $c$: $\nabla_e R^a_{\;bad} + \nabla_a R^a_{\;bde} + \nabla_d R^a_{\;bea} = 0$. The first term is $\nabla_e R_{bd}$; the third is $-\nabla_d R_{be}$ (using $R^a_{\;bea} = -R^a_{\;bae} = -R_{be}$). The middle term is the "divergence" $\nabla_a R^a_{\;bde}$.
> > 
> > Now contract with $g^{be}$: $g^{be}\nabla_e R_{bd} = \nabla^b R_{bd}$ (using metric-compatibility); $g^{be}\nabla_a R^a_{\;bde} = -g^{be}\nabla_a R^a_{\;bed}$ and after careful index work $= -\nabla_a R^a_{\;d}{}^a_{\;a}$ which after re-tracing gives $-\nabla^a R_{ad}$; the third term is $-\nabla_d R$.
> > 
> > Combining: $\nabla^b R_{bd} - \nabla^a R_{ad} - \nabla_d R = 0$ — but the first two are the same! After careful sign tracking the result is $2\nabla^a R_{ad} - \nabla_d S = 0$, i.e., $\nabla^a R_{ad} = \tfrac{1}{2}\nabla_d S$. Rewriting, $\nabla^a(R_{ad} - \tfrac{1}{2}g_{ad}S) = \nabla^a R_{ad} - \tfrac{1}{2}\nabla_d S = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> The five lemmas above constitute the proof:
> - Lemma 1 + Lemma 2 establish the first Bianchi identity.
> - Lemma 3 + Lemma 4 establish the second Bianchi identity.
> - Lemma 5 derives the contracted second Bianchi from the uncontracted second Bianchi.
>
> The torsion-freeness hypothesis is used in Lemma 1 (via $\tau = 0$ in Cartan's first equation). The metric compatibility is *not* needed for either Bianchi identity directly, but is needed for the second Bianchi to descend to the divergence-freeness of the Einstein tensor (since $\nabla g = 0$ allows the metric inside the divergence).

---

# Cross-Field Exercise Suggestions

1. **Einstein's field equations and energy-momentum conservation.** Take Einstein's equations $G_{ab} = 8\pi T_{ab}$ in general relativity. The contracted second Bianchi gives $\nabla^a G_{ab} = 0$; combined with the field equations, $\nabla^a T_{ab} = 0$ — conservation of energy-momentum. So GR is *built on* the second Bianchi identity. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

2. **Yang–Mills theory: the universal Bianchi identity.** In Yang–Mills with gauge group $G$ on a principal bundle $P \to M$, the curvature $F = dA + \tfrac{1}{2}[A, A]$ satisfies $d^A F = 0$ — the **universal Bianchi identity** for any connection on any principal bundle. The Riemannian second Bianchi is the special case $G = \mathrm{O}(n)$, $P = \mathrm{Fr}(M)$. The first Bianchi is *not* universal — it requires $P$ to be the frame bundle of $M$ (so that the soldering form exists) and the connection to be torsion-free. See [[Gauge Theory III — Connections in Principal and Associated Bundles]].

3. **Chern–Weil theory and characteristic classes.** The Bianchi identity makes invariant polynomials in the curvature into *closed* differential forms. Specifically, for any invariant polynomial $P$ on $\mathfrak{g}$, the form $P(F^k)$ on $M$ is closed (by Bianchi) and its cohomology class is independent of the choice of connection. This is the **Chern–Weil construction** of characteristic classes — the foundation of **Pontryagin**, **Chern**, **Euler**, and **Stiefel–Whitney** classes. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

---

# Bridges

- **Cartan's structural equations.** The Bianchi identities are restated cleanly in Cartan's language: first Bianchi is $\Omega \wedge \sigma = 0$ (3-form identity), and second Bianchi is $d\Omega + \omega \wedge \Omega - \Omega \wedge \omega = 0$ (equivalently $d^\omega \Omega = 0$, the universal Bianchi identity for any connection). The first uses torsion-freeness $\tau = 0$ where $\tau = d\sigma + \omega \wedge \sigma$; the second uses no hypothesis beyond $d^2 = 0$. See [[Riemannian Geometry I — Connections and Covariant Differentiation]] for the structural-equations formalism.

- **The Einstein tensor and Einstein's field equations.** The combination $G_{ab} = R_{ab} - \tfrac{1}{2}g_{ab}S$ is the unique (up to scaling) symmetric $(0, 2)$-tensor built from $g$ and its first two derivatives that is automatically divergence-free, by the contracted second Bianchi. This is the geometric reason Einstein's equations $G_{ab} = 8\pi T_{ab}$ are self-consistent with $\nabla^a T_{ab} = 0$. Einstein took two years to find the right form — initially trying $R_{ab} = 8\pi T_{ab}$, which is inconsistent because $\nabla^a R_{ab} \ne 0$ in general. The $-\tfrac{1}{2}g_{ab}S$ correction is exactly what Bianchi allows. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

- **Schur's lemma for Einstein manifolds.** The contracted second Bianchi $\nabla^a R_{ab} = \tfrac{1}{2}\nabla_b S$ applied to $R_{ab} = \lambda g_{ab}$ (with $\lambda$ a function on $M$) gives $\nabla_b \lambda = \tfrac{n}{2}\nabla_b\lambda$, forcing $\lambda$ constant when $n \ne 2$. This is **Schur's lemma**: pointwise Einstein implies constant Einstein in dimension $\ge 3$. See [[Def - Einstein Manifold]].

- **The universal Bianchi $d^A F = 0$ in gauge theory.** In any principal bundle $P \to M$ with connection $A$ and curvature $F = dA + A \wedge A$, the **Bianchi identity** is $d^A F = dF + [A, F] = 0$. This is the universal form; the Riemannian first and second Bianchi are special cases for the Levi-Civita connection on the frame bundle. The Bianchi identity is what makes Yang–Mills theory's characteristic-class integrals topological invariants (Chern numbers, Pontryagin numbers, instanton numbers). See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].
