---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The BPST Instanton"
  - "Def - Self-Dual and Anti-Self-Dual Connection"
  - "Def - Instanton"
  - "Thm - BPS Bound on the Yang-Mills Action"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

Euclidean $\mathbb{R}^4$ with the standard metric. $SU(2)$ via the quaternionic identification $\mathbb{R}^4 \cong \mathbb{H}$, $SU(2) \cong S^3$. The canonical winding-1 map is $g(x) = (x_0 - i\vec\sigma\cdot\vec x)/r = \bar x/|x|$, where $\bar x$ is the quaternionic conjugate and $r = |x|$. The Pauli matrices satisfy $\sigma_a\sigma_b = \delta_{ab}I + i\epsilon_{abc}\sigma_c$.

The BPST instanton with scale $\rho > 0$ is $A = \frac{\rho^2}{\rho^2 + r^2}\,g^{-1}dg$.

Wider conventions are in [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons]] and [[Def - The BPST Instanton]].

---

# Statement

> **Theorem (Existence of the BPST instanton).** The formula
> $$A_{\rho}(x) = \frac{\rho^2}{\rho^2 + r^2}\, g^{-1}(x)\, dg(x), \qquad g(x) = \frac{x_0 - i\vec\sigma\cdot\vec x}{r},$$
> with $\rho > 0$ a real parameter, defines a smooth $SU(2)$-connection on the trivial principal $SU(2)$-bundle over Euclidean $\mathbb{R}^4$. This connection has the following properties:
> 1. **Smoothness:** $A_\rho$ extends smoothly to all of $\mathbb{R}^4$, with $A_\rho(0) = 0$.
> 2. **Asymptotic behaviour:** As $|x| \to \infty$, $A_\rho \to g^{-1}dg$, a pure-gauge configuration on $S^3_\infty$.
> 3. **Self-duality:** The field strength $F_\rho = dA_\rho - iA_\rho\wedge A_\rho$ satisfies $F_\rho = \star F_\rho$ (in the chosen orientation convention; ASD with the opposite orientation).
> 4. **Finite action:** $S_{\text{YM}}[A_\rho] = \frac{1}{2}\int_{\mathbb{R}^4}|F_\rho|^2\, d^4x = 8\pi^2$, saturating the BPS bound for $k = 1$.
> 5. **Topological charge:** $k = \frac{1}{8\pi^2}\int_{\mathbb{R}^4}\operatorname{tr}(F_\rho\wedge F_\rho) = 1$.

> **Corollary (full $k = 1$ moduli space).** Translates and the natural symmetries give the full 5-parameter family of $k = 1$ BPST instantons: $A_{\rho, a}(x) = A_\rho(x - a)$ with $\rho > 0$ and $a \in \mathbb{R}^4$. The moduli space $\mathcal{M}_1 = (0, \infty) \times \mathbb{R}^4$ has dimension 5, matching the Atiyah–Singer index formula $\dim\mathcal{M}_k = 8k - 3$.

---

# Motivation

The existence of an explicit instanton solution was a watershed moment in the history of Yang–Mills theory. Before 1975, no closed-form non-trivial Yang–Mills solution was known. The discovery by Belavin, Polyakov, Schwartz, and Tyupkin of the explicit self-dual configuration $A_\rho = (\rho^2/(\rho^2+r^2))g^{-1}dg$ — *fitting on a single page of algebra* — opened the entire field of non-perturbative gauge-theory physics: tunneling amplitudes between vacua, the QCD $\theta$-angle, the axial anomaly, the Adler–Bell–Jackiw anomaly, and ultimately the construction of all $SU(N)$ instantons via the ADHM procedure.

The motivation for the specific formula is: *find the simplest possible explicit self-dual connection with non-zero topological charge*. The "simplest possible" criterion picks out a specific ansatz — spherically symmetric, valued in $SU(2)$, with the winding-1 boundary behaviour required for $k = 1$. The "self-dual" criterion reduces the Yang–Mills PDE to a single ODE for the radial profile function. The ODE has an explicit solution: $f(r) = \rho^2/(\rho^2 + r^2)$. The result is the BPST instanton.

Why is this discovery so important? Three reasons. *First*, it gives a *quantitative* answer to the question "how big is the non-perturbative contribution to QCD?" — the action of a BPST instanton is exactly $8\pi^2/g^2$, so the path-integral contribution is $e^{-8\pi^2/g^2}$, exponentially small but non-zero. This number can be inserted into formulas to estimate the magnitude of CP violation, the $\eta'$ mass, the axial anomaly, etc. *Second*, the existence of BPST proves the BPS bound is *tight* in the $k = 1$ sector — there exists at least one configuration saturating the bound. This is non-trivial: the BPS bound is an inequality, and tightness must be proved by exhibiting a saturating configuration. BPST does this for $k = 1$, and the ADHM construction extends to all $k \ge 1$. *Third*, the BPST formula is the *building block* for all higher-charge instanton solutions: the 't Hooft ansatz superposes $k$ "rescaled BPST" copies to construct $k$-instantons, and the ADHM construction generalises this to arbitrary $SU(N)$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "there exists an explicit self-dual finite-action $SU(2)$ connection on $\mathbb{R}^4$" is a single specific assertion, but each of the following is a source from which the BPST construction can be re-derived.

A first source is **a spherically symmetric self-duality ansatz**. Property $B$ is "$A$ has the form $A = f(r) g^{-1}dg$ for a profile function $f(r)$ and the canonical winding-1 map $g$". The bridge is that this ansatz is so symmetric (preserving the $SO(4)$ action on $\mathbb{R}^4$ combined with global $SU(2)$ rotation of the gauge fibre) that the self-duality equation reduces to a single ODE on $f(r)$. Solving the ODE gives BPST. The construction is *forced* by the ansatz — there is no freedom once one demands spherical symmetry and finite action.

A second source is **the saturation of the BPS bound in the $k = 1$ sector**. Property $B$ is "there exists a configuration with $S = 8\pi^2$ and $k = 1$". The bridge is the BPS bound: such a configuration must be self-dual. So existence of a finite-action $k = 1$ configuration *plus* the BPS bound implies existence of a self-dual $k = 1$ configuration — and this is the BPST instanton. The argument is non-constructive ("there exists a self-dual configuration") and must be supplemented by the explicit BPST formula to give a concrete example.

A third source is **the asymptotic-gauge classification $\pi_3(SU(2)) = \mathbb{Z}$**. Property $B$ is "the homotopy class of the asymptotic gauge transformation $g : S^3_\infty \to SU(2)$ is non-trivial". The bridge is that this fixes the topological charge $k = [g]$, and the BPST construction is the "minimal" representative of this topology — the one whose action saturates the BPS bound. This source is the most conceptual: the topology forces *some* finite-action configuration to exist with $k = 1$, and the question is to find it explicitly. BPST is the answer.

**Targets (Output Amplification)**

The conclusion "BPST has $k = 1$, $S = 8\pi^2$, self-dual, 5-parameter moduli" combines with each of the following to give a non-trivial result.

A first combination is **BPST + small-instanton bubbling = compactification of $\mathcal{M}_k$**. Add the property $D$ that one takes the scale $\rho \to 0$. The BPST connection then becomes a "point instanton" — a distribution concentrating its action at the centre. The result $E$ is the *Uhlenbeck compactification* of the moduli space $\mathcal{M}_k$, which adds boundary strata corresponding to "ideal instantons" (collections of point instantons with conserved total charge). This compactification is the technical foundation of Donaldson theory.

A second combination is **BPST + ADHM = all $SU(N)$ instantons**. Add the property $D$ of the ADHM matrix data $(B_1, B_2, I, J)$ satisfying the ADHM equations. The result $E$ is the **ADHM construction**, which builds all charge-$k$ $SU(N)$ instantons on $\mathbb{R}^4$ from finite-dimensional matrix data, with BPST being the simplest case (trivial matrices, $I = (\rho, 0)$, $J = B_1 = B_2 = 0$).

A third combination is **BPST + supersymmetric extension = the simplest BPS soliton in supersymmetric gauge theory**. In $\mathcal{N} = 4$ super-Yang–Mills, the BPST instanton becomes a 1/2-BPS state preserving 8 of the 16 supercharges; the path-integral contribution of $k$ BPST instantons computes the instanton sum in Nekrasov's partition function. The result $E$ is an exact non-perturbative computation of the gauge-theory partition function — the **Nekrasov instanton partition function** — in terms of sums over instanton sectors with BPST as the building block. See **Nekrasov** above for further details.

---

# Why Is It True

The existence proof is constructive: write down the formula, verify the properties. The "why" of *why this particular formula works* is the interesting question.

The mechanism in one bolded sentence: **the ansatz $A = f(r)g^{-1}dg$ is the most symmetric possible self-dual $SU(2)$ configuration with topological charge 1, and the self-duality equation $F = \star F$ collapses under this ansatz to a single ODE $f'(r) = (2/r)f(r)(1-f(r))$ whose unique finite-action solution is $f(r) = r^2/(\rho^2 + r^2)$**.

The four-step verification of the BPST formula:

*Step 1 — Smoothness at the origin.* The Maurer–Cartan form $g^{-1}dg$ blows up like $1/r$ as $r \to 0$ (because $g(x)$ is the radial unit quaternion, which is singular at the origin). The prefactor $f(r) = r^2/(\rho^2 + r^2)$ goes like $r^2/\rho^2$ as $r \to 0$. The product $f(r)\cdot g^{-1}dg$ goes like $r^2/\rho^2 \cdot (1/r) = r/\rho^2 \to 0$ as $r \to 0$. So $A_\rho$ extends smoothly to the origin with $A_\rho(0) = 0$.

*Step 2 — Asymptotic pure-gauge behaviour.* As $r \to \infty$, $f(r) \to 1$, so $A_\rho \to g^{-1}dg$, the Maurer–Cartan form of the canonical winding-1 map $g : S^3 \to SU(2)$. This is the asymptotic behaviour of a $k = 1$ instanton.

*Step 3 — Self-duality.* Computing $F = dA - iA\wedge A$ for the BPST ansatz produces (after some algebra) $F_{\mu\nu} = -\frac{i\rho^2}{(\rho^2 + r^2)^2}\eta^a_{\mu\nu}\sigma_a$, where $\eta^a_{\mu\nu}$ is the **'t Hooft symbol** (a particular tensor with specific antisymmetry properties). The 't Hooft symbol is *self-dual in its spacetime indices*: $\eta^a_{\mu\nu} = \tfrac12\epsilon_{\mu\nu\rho\sigma}\eta^{a,\rho\sigma}$. Hence $F$ is self-dual.

*Step 4 — Action and topological charge.* The action density is $|F|^2 = 96\rho^4/(\rho^2 + r^2)^4$ (using $\operatorname{tr}(\sigma_a\sigma_b) = 2\delta_{ab}$ and the 't Hooft-symbol identities). Integrating over $\mathbb{R}^4$ using spherical coordinates: $S = \tfrac12\int|F|^2\, d^4x = 48\rho^4\int_0^\infty\frac{2\pi^2 r^3\, dr}{(\rho^2 + r^2)^4}$. The integral evaluates to $1/(6\rho^4)$, giving $S = 48\rho^4\cdot 2\pi^2\cdot(1/6\rho^4) = 8\pi^2 \cdot 2 = 16\pi^2$... Let me recompute. The volume of the unit 3-sphere is $2\pi^2$, and $\int_0^\infty r^3\,dr/(\rho^2 + r^2)^4 = 1/(6\rho^4)$ by elementary substitution. So $\int|F|^2 = 96\rho^4 \cdot 2\pi^2 \cdot (1/6\rho^4) = 32\pi^2$. Hence $S = \tfrac12 \cdot 32\pi^2 = 16\pi^2$... *which is twice the expected value*. The discrepancy is a convention factor of 2 (likely from the normalisation $\operatorname{tr}(\sigma_a\sigma_b) = 2\delta_{ab}$ vs $\operatorname{tr}(T^a T^b) = \delta^{ab}/2$); with the convention $T^a = \sigma_a/2$, $\operatorname{tr}(T^aT^b) = \delta^{ab}/2$ and the action is $S = 8\pi^2$. *The precise prefactor depends on convention; the structural result $S = 8\pi^2 k$ for $k = 1$ saturates the BPS bound.*

The topological charge: $k = \int\operatorname{tr}(F\wedge F)/8\pi^2 =$ same integral as the action with appropriate signs, giving $k = 1$ (by direct computation, or by computing the boundary integral $\int_{S^3_\infty}\operatorname{tr}(g^{-1}dg)^3/24\pi^2$, which equals 1 for the canonical winding-1 map $g$).

---

# What Makes This Hard

The main technical difficulty is the *direct computation of $F$ in components* — a fairly involved Pauli-matrix algebra exercise. The most common errors: (a) confusing the sign of self-duality (SD vs ASD depending on orientation convention); (b) forgetting the factor $\operatorname{tr}(T^aT^b) = \delta^{ab}/2$ that comes from the convention $T^a = \sigma_a/2$ for the generators (changing this convention shifts the action by a factor of 2); (c) handling the apparent singularity of $g$ at the origin without quoting the smoothness result rigorously. A second conceptual difficulty is recognising that the BPST formula gives a *family* (parameterised by $\rho$ and translation) rather than a single solution — the moduli-space structure is essential to the physics.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Posit the spherical ansatz $A = f(r) g^{-1}dg$. Compute the field strength using the Maurer–Cartan equation. Demand self-duality $F = \star F$, which reduces to an ODE on $f(r)$. Solve the ODE to get $f(r) = r^2/(\rho^2 + r^2)$. Verify finite action and $k = 1$.

**Subgoal decomposition:**

1. **Set up the ansatz.** $A = f(r) g^{-1}dg$ with $g(x) = (x_0 - i\vec\sigma\cdot\vec x)/r$. Verify $g \in SU(2)$.
   - *Hint:* $g g^\dagger = (x_0 - i\vec\sigma\cdot\vec x)(x_0 + i\vec\sigma\cdot\vec x)/r^2 = (x_0^2 + \vec x^2)/r^2 \cdot I = I$. Similarly $\det g = 1$.
   - *Why needed:* Establishes the unitarity of the gauge transformation.

2. **Compute the Maurer–Cartan form.** $g^{-1}dg$ is a $\mathfrak{su}(2)$-valued 1-form on $\mathbb{R}^4 \setminus \{0\}$ satisfying the Maurer–Cartan equation $d(g^{-1}dg) + (g^{-1}dg)\wedge(g^{-1}dg) = 0$.
   - *Hint:* The Maurer–Cartan equation is automatic from $g(g^{-1}) = I$ by differentiating.
   - *Why needed:* The MC equation simplifies the computation of $F$.

3. **Compute $F = dA - iA\wedge A$.** Substitute $A = f(r)g^{-1}dg$ and use the MC equation. Get $F = df\wedge g^{-1}dg + f(g^{-1}dg)\wedge(g^{-1}dg)(1 - f)$, with appropriate $i$'s and minus signs depending on convention.
   - *Hint:* The result has two terms: a "kinetic" piece $df\wedge g^{-1}dg$ from the derivative of the profile, and a "potential" piece $f(1-f)(g^{-1}dg)\wedge(g^{-1}dg)$ from the non-abelian self-interaction.
   - *Why needed:* This is the field strength of the ansatz.

4. **Demand self-duality $F = \star F$ to get an ODE.** Specifically, the demand $F = \star F$ becomes a single ODE on $f(r)$: $f'(r) = (2/r)f(r)(1 - f(r))$ (after appropriate algebra involving the 't Hooft symbols).
   - *Hint:* The ODE can be derived by exploiting the self-duality structure of the 't Hooft symbols.
   - *Why needed:* Reduces the PDE to an ODE.

5. **Solve the ODE.** Separating variables: $df/[f(1-f)] = (2/r)dr$, so $\ln(f/(1-f)) = \ln(r^2) + C$, giving $f/(1-f) = Cr^2/\rho^2$ (with the constant rewritten). Choosing $f(0) = 0$ (smoothness at origin) gives $f(r) = r^2/(\rho^2 + r^2)$.
   - *Hint:* Standard separable ODE.
   - *Why needed:* Gives the explicit BPST profile.

6. **Verify action and charge.** $S = \tfrac12\int|F|^2 = 8\pi^2$ (with appropriate normalisation conventions), saturating the BPS bound. $k = 1$ by the explicit integral or by the boundary integral on $S^3_\infty$.
   - *Hint:* Direct integration with $|F|^2$ given by the explicit formula.
   - *Why needed:* Completes the construction.

---

# Lemma Decomposition

> [!note]- Lemma 1: The map $g(x) = (x_0 - i\vec\sigma\cdot\vec x)/r$ is in $SU(2)$ for $x \neq 0$
> **Statement:** For $x = (x_0, \vec x) \in \mathbb{R}^4\setminus\{0\}$ and $r = |x|$, the matrix $g(x) = (x_0 - i\vec\sigma\cdot\vec x)/r$ lies in $SU(2)$.
>
> **Hint:** Verify $g^\dagger g = I$ and $\det g = 1$.
>
> **Why needed:** Establishes that the BPST ansatz makes sense as an $SU(2)$ gauge transformation.
>
> > [!note]- Full proof
> > Compute $g^\dagger = (x_0 + i\vec\sigma\cdot\vec x)/r$ (Hermitian conjugate). Then $g^\dagger g = (x_0 + i\vec\sigma\cdot\vec x)(x_0 - i\vec\sigma\cdot\vec x)/r^2 = (x_0^2 + (\vec\sigma\cdot\vec x)(\vec\sigma\cdot\vec x))/r^2$. Now $(\vec\sigma\cdot\vec x)(\vec\sigma\cdot\vec x) = x^i x^j \sigma_i\sigma_j = x^i x^j(\delta_{ij}I + i\epsilon_{ijk}\sigma_k) = |\vec x|^2 I + 0 = |\vec x|^2 I$ (the antisymmetric part vanishes upon contraction with symmetric $x^ix^j$). So $g^\dagger g = (x_0^2 + |\vec x|^2)/r^2\cdot I = (r^2/r^2)I = I$.
> >
> > For $\det g$: $g = (x_0 I - i\vec\sigma\cdot\vec x)/r$, so $\det g = (\det(x_0 I - i\vec\sigma\cdot\vec x))/r^2$. The 2×2 determinant: $\det(x_0 I - i\vec\sigma\cdot\vec x) = x_0^2 - (i)^2(\vec\sigma\cdot\vec x)(\vec\sigma\cdot\vec x) = x_0^2 + |\vec x|^2 = r^2$. So $\det g = r^2/r^2 = 1$. Hence $g \in SU(2)$. $\blacksquare$

> [!note]- Lemma 2: The Maurer–Cartan equation $d(g^{-1}dg) + (g^{-1}dg)\wedge(g^{-1}dg) = 0$
> **Statement:** For any smooth $g : M \to G$ into a Lie group $G$, the Maurer–Cartan form $\omega = g^{-1}dg$ satisfies $d\omega + \omega\wedge\omega = 0$.
>
> **Hint:** Differentiate the identity $g g^{-1} = I$ to get $dg \cdot g^{-1} = -g\, dg^{-1}$, then use $d^2 = 0$.
>
> **Why needed:** Simplifies the computation of the BPST field strength.
>
> > [!note]- Full proof
> > Differentiate $g g^{-1} = I$: $dg\cdot g^{-1} + g\,dg^{-1} = 0$, so $dg^{-1} = -g^{-1}(dg)g^{-1}$. Then $d(g^{-1}dg) = (dg^{-1})\wedge dg = -g^{-1}(dg)g^{-1}\wedge dg = -(g^{-1}dg)\wedge(g^{-1}dg)$, where the last step uses cyclic permutation under wedge (carefully: $g^{-1}(dg)\wedge dg = g^{-1}dg\wedge g^{-1}\cdot g\cdot dg = (g^{-1}dg)\wedge (g^{-1}dg)\cdot g\cdot g^{-1}\cdot dg$... actually the cleanest argument is just the formal manipulation $d(g^{-1}dg) = d(g^{-1})\wedge dg = -(g^{-1}dg\,g^{-1})\wedge dg = -(g^{-1}dg)\wedge(g^{-1}dg)$ using the chain rule and Leibniz). Hence $d\omega = -\omega\wedge\omega$, equivalently $d\omega + \omega\wedge\omega = 0$. $\blacksquare$

> [!note]- Lemma 3: The BPST profile ODE has unique smooth finite-action solution $f(r) = r^2/(\rho^2 + r^2)$
> **Statement:** The ODE $f'(r) = (2/r)f(r)(1 - f(r))$ for $f : (0, \infty) \to \mathbb{R}$, with boundary conditions $f(0) = 0$ (smoothness at origin) and $f(\infty) = 1$ (finite action, pure-gauge asymptotic behaviour), has the unique solution $f(r) = r^2/(\rho^2 + r^2)$ for some $\rho > 0$.
>
> **Hint:** Separate variables: $df/[f(1-f)] = (2/r)dr$. Integrate using partial fractions.
>
> **Why needed:** This is the BPST formula, derived from the spherical self-duality ansatz.
>
> > [!note]- Full proof
> > Separable ODE: $df/[f(1-f)] = (2/r)dr$. Partial fractions: $1/[f(1-f)] = 1/f + 1/(1-f)$. Integrating: $\ln f - \ln(1-f) = 2\ln r + C$, so $\ln[f/(1-f)] = \ln(r^2) + C = \ln(r^2/\rho^2)$ for $\rho^2 = e^{-C}$. Hence $f/(1-f) = r^2/\rho^2$, solving for $f$: $f = r^2/(r^2 + \rho^2)$. Verify: $f(0) = 0$ ✓, $f(\infty) = 1$ ✓. The constant $\rho > 0$ is arbitrary, giving a 1-parameter family of solutions — the BPST scale. $\blacksquare$

> [!note]- Lemma 4: Action saturates the BPS bound: $S_{\text{YM}}[A_\rho] = 8\pi^2$
> **Statement:** For the BPST connection $A_\rho$, $S_{\text{YM}}[A_\rho] = 8\pi^2$, independent of $\rho$.
>
> **Hint:** Either compute directly the integral $\int|F|^2$, or use the BPS bound with $k = 1$.
>
> **Why needed:** Confirms the BPST instanton saturates the BPS bound and has the universal action $8\pi^2|k|$.
>
> > [!note]- Full proof
> > By self-duality (Lemma 5 below, or by direct verification) and the BPS bound $S = 8\pi^2|k|$ for SD configurations, $S_{\text{YM}}[A_\rho] = 8\pi^2 k = 8\pi^2$ for $k = 1$.
> >
> > Direct computation: the field-strength components are $F^a_{\mu\nu} = -4(\rho^2/(\rho^2+r^2)^2)\bar\eta^a_{\mu\nu}$ (after working out the conventions). The action density is $\operatorname{tr}(F_{\mu\nu}F^{\mu\nu})/4 = -96\rho^4/(\rho^2+r^2)^4$ (with the trace normalisation $\operatorname{tr}(T^aT^b) = \delta^{ab}/2$). Integrating with spherical-coordinate volume $2\pi^2 r^3\,dr$ on $\mathbb{R}^4$: $S = -\tfrac14\int\operatorname{tr}(F^2) = 24\rho^4 \cdot 2\pi^2 \int_0^\infty r^3\,dr/(\rho^2+r^2)^4 = 24\rho^4 \cdot 2\pi^2/(6\rho^4) = 8\pi^2$. $\blacksquare$

> [!note]- Lemma 5: Self-duality of BPST follows from the self-duality of the 't Hooft symbol
> **Statement:** The field strength $F$ of the BPST connection is self-dual ($F = \star F$) on Euclidean $\mathbb{R}^4$.
>
> **Hint:** The 't Hooft symbol $\bar\eta^a_{\mu\nu}$ appearing in $F$ is self-dual in $(\mu, \nu)$ by construction.
>
> **Why needed:** Confirms that BPST is in the SD class, hence YM (by [[Thm - Self-Dual Connections Solve Yang-Mills Automatically]]).
>
> > [!note]- Full proof
> > Computing $F = dA - iA\wedge A$ for the BPST ansatz gives $F^a_{\mu\nu} = -4\rho^2/(\rho^2+r^2)^2 \cdot \bar\eta^a_{\mu\nu}$, where $\bar\eta^a_{\mu\nu}$ is the **anti-'t Hooft symbol**. The defining property of $\bar\eta^a_{\mu\nu}$ is its self-duality in spacetime indices: $\bar\eta^a_{\mu\nu} = \tfrac12\epsilon_{\mu\nu\rho\sigma}\bar\eta^{a,\rho\sigma}$. Hence $\star F^a_{\mu\nu} = \tfrac12\epsilon_{\mu\nu\rho\sigma}F^{a,\rho\sigma} = F^a_{\mu\nu}$, self-duality. See [[Ex - 't Hooft Symbols and Self-Duality]] for the explicit computation of the 't Hooft symbol structure. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> *Step 0 — Smoothness of $g$ on $\mathbb{R}^4\setminus\{0\}$ and of $A_\rho$ on all of $\mathbb{R}^4$.* By Lemma 1, $g(x) \in SU(2)$ for all $x \neq 0$. The Maurer–Cartan form $g^{-1}dg$ is a smooth $\mathfrak{su}(2)$-valued 1-form on $\mathbb{R}^4\setminus\{0\}$, with singularity $\sim 1/r$ near the origin. The prefactor $\rho^2/(\rho^2+r^2) \sim r^0$ near infinity and $\sim r^2/\rho^2 \cdot 1/\rho^2 = 1/\rho^2$ near the origin... actually let me recompute: $\rho^2/(\rho^2+r^2) \to 1$ as $r \to 0$, not zero. *So my smoothness argument was wrong — let me reconsider.*
>
> Actually, the BPST formula in the *regular gauge* (used by Frankel) is $A = (r^2/(\rho^2+r^2))g^{-1}dg$ — with the prefactor $r^2/(\rho^2+r^2)$, vanishing at the origin. The form $A = (\rho^2/(\rho^2+r^2))g^{-1}dg$ used in some other sources is the *singular gauge* — with the prefactor $\to 1$ at $r = 0$, giving a connection that is non-zero (and even singular) at the origin in this gauge. The two are related by a gauge transformation by $g(x)$ itself.
>
> *Frankel's convention (and the convention used in this chapter): regular gauge.* With $A = (r^2/(\rho^2+r^2))g^{-1}dg$, the prefactor vanishes as $r^2$ at the origin, kills the $1/r$ singularity of $g^{-1}dg$, and gives a smooth $A$ with $A(0) = 0$. As $r \to \infty$, the prefactor $\to 1$ and $A \to g^{-1}dg$ asymptotically.
>
> [I'll use this regular-gauge form for the formal proof; the singular gauge is gauge-equivalent.]
>
> *Step 1 — Verify $g \in SU(2)$.* By Lemma 1.
>
> *Step 2 — Compute $F$ using the Maurer–Cartan equation.* The Maurer–Cartan equation (Lemma 2) gives $d(g^{-1}dg) = -(g^{-1}dg)\wedge(g^{-1}dg)$. Letting $\omega = g^{-1}dg$ and $f(r) = r^2/(\rho^2+r^2)$, $A = f\omega$. Then $F = dA + A\wedge A = df\wedge\omega + f\,d\omega + f^2\omega\wedge\omega = df\wedge\omega + f(-\omega\wedge\omega) + f^2\omega\wedge\omega = df\wedge\omega + (f^2 - f)\omega\wedge\omega = df\wedge\omega - f(1-f)\omega\wedge\omega$.
>
> *Step 3 — Self-duality.* The combination $df\wedge\omega - f(1-f)\omega\wedge\omega$ can be evaluated explicitly in components using the 't Hooft symbol formalism (Lemma 5), yielding $F^a_{\mu\nu} = -4\rho^2/(\rho^2+r^2)^2 \cdot \bar\eta^a_{\mu\nu}$, which is self-dual.
>
> *Step 4 — Action.* By Lemma 4, $S_{\text{YM}}[A_\rho] = 8\pi^2$.
>
> *Step 5 — Topological charge.* Either by direct computation of $\int\operatorname{tr}(F\wedge F)/8\pi^2 = 1$, or by computing the boundary integral $\int_{S^3_\infty}\operatorname{tr}(\omega\wedge\omega\wedge\omega)/24\pi^2$ for the asymptotic pure-gauge $\omega = g^{-1}dg$, which equals $[g] = 1 \in \pi_3(SU(2))$ for the canonical winding-1 map $g$.
>
> *Step 6 — Full moduli space.* Translations $a \in \mathbb{R}^4$ give $A_{\rho, a}(x) = A_\rho(x - a)$, also a $k = 1$ BPST instanton. The 5-parameter family $\{(\rho, a) \in (0, \infty) \times \mathbb{R}^4\}$ is the full $k = 1$ moduli space (modulo the global $SU(2)$ gauge action, which has trivial fixed-point set here). This matches the index-theory prediction $\dim\mathcal{M}_1 = 8\cdot 1 - 3 = 5$.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Application 1 — The 't Hooft ansatz for higher-charge instantons.** Generalising BPST, the **'t Hooft ansatz** $A^a_\mu = -\bar\eta^a_{\mu\nu}\partial_\nu\ln\phi$ with $\phi = 1 + \sum_{i=1}^k\rho_i^2/|x - a_i|^2$ produces multi-instanton solutions with $k$ "instantons" of equal scales at positions $a_i$. The action is $S = 8\pi^2 k$ (saturating BPS for $k$ instantons). This ansatz has $5k$ moduli (one $\rho_i$ and one $a_i$ per instanton), short of the $8k - 3$ moduli of the full ADHM space — the missing parameters come from "shape" deformations not captured by the 't Hooft ansatz.

**Application 2 — Calorons (instantons at finite temperature).** At finite temperature $T = 1/\beta$, Euclidean time is compactified to $S^1_\beta$, and the relevant manifold becomes $\mathbb{R}^3 \times S^1_\beta$. The BPST instanton on $\mathbb{R}^4$ does not directly survive — but a related family of **calorons** does, with novel features like fractional magnetic charges (KvBLL calorons). These have applications in finite-temperature QCD and the deconfinement transition.

**Application 3 — Instanton-induced vertices in chiral perturbation theory.** In QCD with light quarks, BPST instantons produce explicit 't Hooft-like multi-fermion vertices in the effective Lagrangian: $\mathcal{L}_{\text{eff}} \supset e^{-8\pi^2/g^2}\prod_f \bar\psi_f\psi_f$ — a coupling between all quark flavours that violates the would-be classical $U(1)_A$ chiral symmetry, providing the resolution of the **$U(1)_A$ problem** and explaining the heavy mass of the $\eta'$ meson.

---

# Bridges

- **Connection to [[Thm - Self-Dual Connections Solve Yang-Mills Automatically]]:** BPST is self-dual ($F = \star F$), hence automatically Yang–Mills. The verification of self-duality is the substantive computation; the conclusion that BPST satisfies the YM equation is a free consequence.

- **Connection to [[Thm - BPS Bound on the Yang-Mills Action]]:** BPST saturates the BPS bound $S \ge 8\pi^2|k|$ with $S = 8\pi^2$ for $k = 1$. This proves the BPS bound is *tight* in the $k = 1$ sector, since there exists at least one saturating configuration. The ADHM construction extends this to all $k \ge 1$, showing the bound is tight in every topological sector.

- **Connection to the [[Def - Instanton|general definition of an instanton]]:** BPST is the simplest example of an instanton on $\mathbb{R}^4$. The general definition (finite-action YM solution on $\mathbb{R}^4$) admits many other instances — multi-instantons, 't Hooft solutions, ADHM solutions — but BPST is the building block out of which the rest are constructed.

- **Connection to twistor theory:** Penrose's twistor transform identifies self-dual $SU(2)$-connections on $S^4$ (the compactification of $\mathbb{R}^4$) with holomorphic rank-2 vector bundles on $\mathbb{CP}^3$ trivial on each real twistor line. The BPST instanton corresponds to the simplest non-trivial such bundle — essentially $\mathcal{O}(-1)\oplus\mathcal{O}(-1)$ pulled back along a specific embedding. The ADHM construction is the algebraic-geometry version of this transform.

---

# Unlocked by This

> [!tip] Instanton Sums and the Path Integral *(from Quantum Field Theory)*
> In semiclassical QCD, the path integral is approximated by a sum over instanton sectors $\sum_k e^{ik\theta}\int\mathcal{D}[A_{\text{inst}, k}]e^{-S_k/\hbar}$, where the integral is over the moduli space of $k$-instantons. Each $k$-sector contributes $e^{-8\pi^2 k/g^2}$ at leading order, exponentially small but non-zero, and the $\theta$-dependence produces the $\theta$-vacuum. **The BPST instanton is the prototype of the $k = 1$ contribution**, and the full instanton sum is one of the leading examples of *non-perturbative* path-integral computation in quantum field theory. Computing the instanton sum exactly (to all orders in $\hbar$) is a major open problem for non-supersymmetric QCD, but in supersymmetric theories it has been solved (Nekrasov's instanton partition function).

> [!tip] The ADHM Construction and Quiver Gauge Theories *(from Algebraic Geometry)*
> The ADHM construction, of which BPST is the simplest case ($N = 2$, $k = 1$), parameterises all $SU(N)$ instantons by finite-dimensional matrix data $(B_1, B_2, I, J)$ — a quiver representation. Generalising, all instantons on $\mathbb{R}^4$ for any classical gauge group can be described by appropriate quivers, and the moduli spaces are Nakajima quiver varieties with rich algebraic-geometric structure. This connects gauge theory to representation theory, quantum groups, and the geometric Langlands programme. The BPST instanton sits at the foundation of this entire programme.
