---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Instanton"
  - "Def - Self-Dual and Anti-Self-Dual Connection"
  - "Def - The Yang-Mills Field Strength"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

Euclidean $\mathbb{R}^4$ with the standard metric $\delta_{\mu\nu}$ and orientation $dx^0\wedge dx^1\wedge dx^2\wedge dx^3$. Coordinates $x = (x_0, x_1, x_2, x_3) = (x_0, \vec x)$. Radial coordinate $r = |x| = \sqrt{x_0^2 + x_1^2 + x_2^2 + x_3^2}$.

**Quaternionic identification.** $\mathbb{R}^4 \cong \mathbb{H}$, the quaternions, via $x \leftrightarrow x_0 + i x_1 + j x_2 + k x_3$, where $i, j, k$ are the unit quaternions with $i^2 = j^2 = k^2 = -1$ and $ij = k$ cyclic. The unit quaternions $S^3 = \{q \in \mathbb{H} : |q| = 1\}$ form a Lie group isomorphic to $SU(2)$.

**Pauli matrices.** $\sigma_1 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $\sigma_2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $\sigma_3 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$, satisfying $\sigma_a\sigma_b = \delta_{ab}I + i\epsilon_{abc}\sigma_c$. The map $\mathbb{H} \to SU(2)$, $q = q_0 + i q_1 + j q_2 + k q_3 \mapsto q_0 I - i(q_1\sigma_1 + q_2\sigma_2 + q_3\sigma_3) = q_0 I - i\vec q\cdot\vec\sigma$ is the Lie group isomorphism $S^3 \cong SU(2)$.

**Instanton parameter:** $\rho > 0$, the scale; centre is at the origin (translations add a 4-parameter family).

Wider conventions are in [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

---

# Axiom Motivation

The BPST instanton (Belavin, Polyakov, Schwartz, Tyupkin, 1975) is the simplest non-trivial Yang–Mills solution, and the discovery of its explicit closed form was the moment Yang–Mills theory acquired a non-perturbative example to study. The construction is a textbook case of **soliton ansatz**: posit a solution with the maximum symmetry compatible with the topological charge, reduce the PDE to an ODE, and solve.

*The natural ansatz: pure-gauge-times-radial-cutoff.* Since the asymptotic behaviour of an instanton must be pure gauge ($A \to g^{-1}dg$ at infinity), the simplest possible structure is to extend this asymptotic form throughout $\mathbb{R}^4$ with a radial cutoff: $A = f(r)\, g^{-1}dg$, where $f(r)$ is a profile function with $f(r) \to 1$ as $r \to \infty$ and $f(r) \to 0$ at the origin (the second condition to keep the connection smooth at $r = 0$ where the pure-gauge $g^{-1}dg$ may be singular). The map $g : \mathbb{R}^4 \to SU(2)$ should have winding number $1$ on $S^3_\infty$ to produce $k = 1$.

*The canonical winding-1 map.* The map $g(x) = (x_0 - i\vec\sigma\cdot\vec x)/r$ sends $x \in \mathbb{R}^4 \setminus \{0\}$ to an element of $SU(2)$ via the quaternionic identification: $g(x) = \bar x/|x|$ (where $\bar x$ is the quaternionic conjugate). The restriction of $g$ to any sphere $S^3_R \subset \mathbb{R}^4$ centred at the origin is the identity map $S^3_R \to S^3 \cong SU(2)$ (after rescaling), so it has winding number 1. This is the simplest non-trivial $g : S^3 \to SU(2) = S^3$, and the instanton ansatz built on it will have $k = 1$.

*Reducing self-duality to an ODE for $f(r)$.* Computing $F = dA - iA\wedge A$ from the ansatz $A = f(r) g^{-1}dg$ produces an explicit expression involving $f(r)$, $f'(r)$, and the Maurer–Cartan form $g^{-1}dg$ (which satisfies the Maurer–Cartan equation $d(g^{-1}dg) + (g^{-1}dg)\wedge(g^{-1}dg) = 0$). Demanding $F = \star F$ then becomes a single first-order ODE for $f(r)$: $f'(r) = (2/r) f(r)(1 - f(r))$, the **BPS reduction** of self-duality under the spherical ansatz. This ODE has the explicit solution $f(r) = r^2/(\rho^2 + r^2) = 1 - \rho^2/(\rho^2 + r^2)$, where $\rho > 0$ is an integration constant — the scale of the instanton.

*Why the formula $A = \frac{\rho^2}{\rho^2 + r^2}g^{-1}dg$ is correct.* This is the form one obtains after multiplying out: $A = (1 - \rho^2/(\rho^2+r^2))g^{-1}dg = g^{-1}dg - \frac{\rho^2}{\rho^2+r^2}g^{-1}dg$, but since $g^{-1}dg$ is itself a pure gauge that contributes $F = 0$, the physically meaningful "instanton part" is the second term. *The standard convention is to absorb the pure-gauge piece and write $A = \frac{\rho^2}{\rho^2 + r^2}g^{-1}dg$ as the "regular gauge" representative of the BPST instanton.* This convention keeps $A \to 0$ at infinity rather than $A \to g^{-1}dg$ (which is gauge-equivalent but visually less clean). The two forms are related by a gauge transformation by $g(x)$ itself.

*The scale $\rho$ as a moduli space parameter.* The integration constant $\rho > 0$ in the ODE solution parameterises a one-dimensional family of $k = 1$ instantons. Adding translations of the centre, the full $k = 1$ moduli space is $\mathcal{M}_1 = (0, \infty) \times \mathbb{R}^4$, 5-dimensional, matching the index-theory prediction $\dim\mathcal{M}_1 = 8\cdot 1 - 3 = 5$. The instanton "shrinks" as $\rho \to 0$ (becoming a point-singular configuration on the moduli space boundary) and "spreads" as $\rho \to \infty$ (becoming the trivial connection, again a boundary point). The behaviour at $\rho \to 0$ — **instanton bubbling** — is the central technical phenomenon in the analytical theory of YM moduli spaces, and is what allows the construction of compactifications $\bar{\mathcal M}_k$ via the **Uhlenbeck compactification**.

*The role of self-duality.* The BPST ansatz $A = f(r)g^{-1}dg$ with $g = \bar x/|x|$ is so symmetric that it forces *either* $f$ to be one of two specific functions (the SD and ASD profiles), *or* the field strength to vanish (the trivial connection). The SD solution gives the BPST instanton; the ASD solution gives the BPST anti-instanton, related to it by orientation reversal of $\mathbb{R}^4$ or equivalently by $\rho \to -\rho$ in the formula (which is an odd transformation under the sign of $\rho$ — physically a different solution).

---

# The Definition

The **BPST instanton** (Belavin–Polyakov–Schwartz–Tyupkin, 1975) is the explicit family of self-dual $SU(2)$-connections on Euclidean $\mathbb{R}^4$ given by

$$A = \frac{\rho^2}{\rho^2 + r^2}\, g^{-1}dg, \qquad g(x) = \frac{x_0 - i\vec\sigma\cdot\vec x}{r},$$

where $\rho > 0$ is the **scale** (or **size**) of the instanton, $r = |x| = \sqrt{x_0^2 + \vec x^2}$ is the Euclidean radial coordinate, $\vec\sigma = (\sigma_1, \sigma_2, \sigma_3)$ are the Pauli matrices, and $g : \mathbb{R}^4 \setminus \{0\} \to SU(2)$ is the canonical winding-1 map (equivalently, $g(x) = \bar x / |x|$ under the quaternionic identification $\mathbb{R}^4 \cong \mathbb{H}$, $SU(2) \cong S^3 = \{q \in \mathbb{H}: |q| = 1\}$).

**Properties:**
1. **Smoothness:** Although $g(x)$ is singular at the origin, the connection $A$ is smooth on all of $\mathbb{R}^4$ because the prefactor $\rho^2/(\rho^2 + r^2) \to 0$ as $r \to 0$ kills the singularity. Explicitly, $A$ extends smoothly to $A(0) = 0$.
2. **Asymptotics:** As $r \to \infty$, $A \to g^{-1}dg$, a pure-gauge configuration of winding number 1 on $S^3_\infty$.
3. **Self-duality:** $F_A = \star F_A$.
4. **Action:** $S_{\text{YM}}[A] = 8\pi^2$, saturating the BPS bound $S \ge 8\pi^2|k|$ for $k = 1$.
5. **Topological charge:** $k = \frac{1}{8\pi^2}\int_{\mathbb{R}^4}\operatorname{tr}(F\wedge F) = 1$.

**Variations of the BPST family:**
- **Translations:** $A_a = A(x - a)$ for any $a \in \mathbb{R}^4$ is also a $k = 1$ BPST instanton, centred at $a$.
- **Anti-instanton:** $A^{\text{ASD}} = \frac{\rho^2}{\rho^2 + r^2}g\, dg^{-1}$ with the *opposite* sign convention (or, equivalently, replacing $g$ by $g^{-1}$) is anti-self-dual with $k = -1$.
- **Singular gauge:** the gauge-equivalent form $A^{\text{sing}} = \frac{r^2}{\rho^2 + r^2}g^{-1}dg$ has the *prefactor inverted* and shifts the singularity from the origin to infinity; it is convenient for some computations.

The full **$k = 1$ moduli space** $\mathcal{M}_1$ of $SU(2)$ instantons on $\mathbb{R}^4$ is parameterised by:
- the scale $\rho \in (0, \infty)$;
- the position $a \in \mathbb{R}^4$;
giving $\dim\mathcal{M}_1 = 1 + 4 = 5$, in agreement with the index-theoretic formula $\dim\mathcal{M}_k = 8k - 3$ for $k = 1$. The boundary of $\mathcal{M}_1$ (under Uhlenbeck compactification) consists of "point instantons" — singular configurations at $\rho = 0$ and a fixed centre — which compactify $\mathcal{M}_1$ to the closure $\bar{\mathcal M}_1 = \overline{\mathbb{R}^4 \times (0, \infty]}$.

---

# Relate to Other Fields / Compression

**BPST is the simplest example of an *exact non-perturbative classical solution of a 4-dimensional non-linear gauge theory*.** Before its discovery in 1975, no closed-form non-trivial Yang–Mills solution was known; afterwards, the entire programme of instanton physics (computing tunneling amplitudes, deriving the $\theta$-vacuum, computing the axial anomaly) became tractable. The **'t Hooft instantons** (multi-instanton generalisations) and the full **ADHM construction** (all $SU(N)$ instantons of all charges) followed within a few years of BPST.

**The BPST connection corresponds to the simplest non-trivial holomorphic vector bundle on $\mathbb{CP}^3$.** Under Penrose's twistor transform, self-dual $SU(2)$-connections on $S^4$ (the conformal compactification of $\mathbb{R}^4$) correspond to holomorphic rank-2 vector bundles on $\mathbb{CP}^3$ trivial on each real twistor line. The $k = 1$ BPST instanton corresponds to the bundle $\mathcal{O}(-1)^{\oplus 2}|_{\mathbb{CP}^2}$ via the **Ward correspondence** — the simplest non-trivial holomorphic rank-2 bundle whose ADHM matrices are essentially trivial.

**True name:** the BPST instanton is *the unique smooth $k = 1$ self-dual $SU(2)$ connection on $\mathbb{R}^4$, modulo gauge and translations and scaling*. The operational form is: when you need a concrete instanton example to test general theorems, calibrate moduli-space dimensions, or compute path-integral contributions, *use BPST*. The formula $A = \rho^2/(\rho^2 + r^2)\cdot g^{-1}dg$ is the *expression* of this canonical solution; the true name is the uniqueness-up-to-symmetries statement that makes BPST the right example.

---

# Examples / Corollaries

**Example 1 — BPST in components.** Writing $A = A^a_\mu(\sigma_a/2)\,dx^\mu$ in the Pauli-matrix basis, the components are $A^a_\mu = \frac{2}{q}\frac{\rho^2}{\rho^2+r^2}\bar\eta^a_{\mu\nu}x^\nu/r^2$, where $\bar\eta^a_{\mu\nu}$ is the **anti-'t Hooft symbol** (the conjugate of the 't Hooft symbol — different sources use different sign conventions). The explicit dependence on the antisymmetric 't Hooft tensor encodes the self-duality structure.

**Example 2 — Field strength of BPST.** Computing $F = dA - iA\wedge A$ produces $F^a_{\mu\nu} = -\frac{4\rho^2}{(r^2 + \rho^2)^2}\bar\eta^a_{\mu\nu}$, which is *manifestly self-dual* because $\bar\eta^a_{\mu\nu}$ is self-dual in its $\mu\nu$ indices: $\bar\eta^a_{\mu\nu} = \tfrac12\epsilon_{\mu\nu\rho\sigma}\bar\eta^{a,\rho\sigma}$. The action density is $|F|^2 = 96\rho^4/(r^2+\rho^2)^4$ — concentrated near the origin (radius $\sim\rho$) and decaying as $1/r^8$ at large $r$. Total action $\int|F|^2/2 = 8\pi^2$.

**Example 3 — Higher-charge generalisation: 't Hooft ansatz.** For $k \ge 1$ instantons of equal scale at distinct positions $a_1, \dots, a_k$, the **'t Hooft ansatz** is $A = \tfrac12 \bar\sigma_{\mu\nu}\partial_\nu\ln\phi\, dx^\mu$ where $\phi(x) = 1 + \sum_{i=1}^k \rho_i^2/|x - a_i|^2$ and $\bar\sigma_{\mu\nu}$ are certain spinor structures. This is the *multi-instanton generalisation* of BPST and was the precursor to ADHM. It does not give *all* $k$-instantons (the 't Hooft ansatz has $5k$ moduli, but the full moduli space has $8k - 3$), but it gives an important family.

**Non-example — A "BPST-like" ansatz with the wrong $g$.** Trying $A = \frac{\rho^2}{\rho^2+r^2}h^{-1}dh$ with $h(x) = e^{ix_0}$ (a winding-0 map) gives $F = 0$ (the connection is pure gauge times a radial cutoff — but since $h$ has trivial winding, this is just a gauge transformation of the flat connection). The topology of the map $g$ is essential; without winding number 1, you do not get a non-trivial instanton.

**Calibration check.** A reader who has internalised the definition should be able to: (a) verify that $g(x) = (x_0 - i\vec\sigma\cdot\vec x)/r$ does satisfy $g\,g^\dagger = I$ and $\det g = 1$ (i.e., $g \in SU(2)$), using the Pauli-matrix identities; (b) check that the prefactor $\rho^2/(\rho^2 + r^2)$ goes to 0 as $r \to 0$ and to 1 as $r \to \infty$, ensuring smoothness at the origin and pure-gauge asymptotics; (c) explain why the BPS bound $S \ge 8\pi^2|k|$ is saturated by BPST: the connection is self-dual, so by [[Thm - BPS Bound on the Yang-Mills Action]] $S = 8\pi^2 k = 8\pi^2$.

---

# Unlocked by This

> [!tip] ADHM Construction — All $SU(N)$ Instantons *(from Algebraic Geometry)*
> The BPST instanton is the simplest case ($N = 2$, $k = 1$) of the **Atiyah–Drinfeld–Hitchin–Manin (ADHM) construction**, which gives *all* $SU(N)$ instantons of arbitrary charge $k$ on $\mathbb{R}^4$ in terms of finite-dimensional matrix data: an ADHM datum is a quadruple $(B_1, B_2, I, J)$ with $B_1, B_2 : \mathbb{C}^k \to \mathbb{C}^k$, $I : \mathbb{C}^N \to \mathbb{C}^k$, $J : \mathbb{C}^k \to \mathbb{C}^N$ satisfying the algebraic ADHM equations $[B_1, B_2] + IJ = 0$ and $[B_1, B_1^\dagger] + [B_2, B_2^\dagger] + II^\dagger - J^\dagger J = 0$, modulo a $U(k)$ action. The moduli space of solutions is exactly $\mathcal{M}_k(SU(N))$, the moduli space of charge-$k$ $SU(N)$ instantons, and the BPST instanton corresponds to the trivial ADHM data with $B_1 = B_2 = J = 0$ and $I = (\rho, 0)$. The ADHM construction transforms an infinite-dimensional non-linear PDE problem into a finite-dimensional algebraic moment-map quotient — one of the most striking simplifications in 20th-century geometry.

> [!tip] Yang–Mills Heat Flow and Instanton Bubbling *(from Geometric Analysis)*
> The Yang–Mills heat flow $\partial_t A = -d_A^* F_A$ on a 4-manifold $X^4$ relaxes any initial connection towards a Yang–Mills critical point. **Uhlenbeck's compactness theorem** (1982) controls the behaviour of bounded-energy sequences of connections, allowing the construction of weak limits — but with the possible loss of energy concentrating at isolated points, a phenomenon called **instanton bubbling**. As $\rho \to 0$ in the BPST family, the energy $S_{\text{YM}} = 8\pi^2$ concentrates at the centre of the instanton, in the limit producing a "bubble" — a point-mass of energy $8\pi^2$ plus a smooth limit elsewhere. The **Uhlenbeck compactification** of moduli spaces of YM connections adds these bubble configurations as boundary strata, producing a compact moduli space $\bar{\mathcal M}_k$ on which the **Donaldson invariants** can be defined as cohomology classes integrated over the moduli-space fundamental class.
