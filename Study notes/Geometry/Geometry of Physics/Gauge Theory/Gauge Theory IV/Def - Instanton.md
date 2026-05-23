---
type: definition
subject: gauge-theory
prereqs:
  - "Def - The Yang-Mills Equation"
  - "Def - Self-Dual and Anti-Self-Dual Connection"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

**Standing convention — Euclidean signature.** Instantons are inherently Euclidean objects, defined on $\mathbb{R}^4$ with the flat Euclidean metric $\delta_{\mu\nu}$. The reason is that the finite-action condition makes sense only for positive-definite metrics — in Lorentzian signature the action density $\tfrac12(\vec E^2 - \vec B^2)$ can be arbitrarily negative, so $|S| < \infty$ is no constraint. The term "instanton" reflects this: in the Wick-rotated picture, what is a tunneling event in Lorentzian time becomes a localised "instant" in Euclidean time.

$\mathbb{R}^4$ with Euclidean metric. $G$: compact Lie group, often $SU(2)$. $A$: connection on a principal $G$-bundle. $F$: field strength. $r = \sqrt{x_0^2 + x_1^2 + x_2^2 + x_3^2}$: Euclidean radial coordinate. $S^3_R = \{x : |x| = R\}$: the 3-sphere of radius $R$, with $S^3_\infty = \lim_{R\to\infty} S^3_R$ as the asymptotic 3-sphere.

The instanton number $k$ is the integer $k = \frac{1}{8\pi^2}\int_{\mathbb{R}^4}\operatorname{tr}(F\wedge F)$.

Wider conventions are in [[Gauge Theory IV — Yang–Mills Fields and Instantons]].

---

# Axiom Motivation

An instanton is, by definition, a finite-action Yang–Mills solution on Euclidean $\mathbb{R}^4$. The four words "finite-action Yang–Mills solution Euclidean" each play a non-trivial role; together they pick out a class of configurations with extraordinary mathematical structure and crucial physical significance.

*Why finite action?* Without this condition, every connection on $\mathbb{R}^4$ that satisfies the Yang–Mills equation pointwise is a "Yang–Mills solution", including configurations with infinite total action $S = \int|F|^2 = \infty$. These would include, for instance, plane-wave solutions (which carry infinite energy when extended over all of $\mathbb{R}^4$). The finite-action condition restricts attention to *localised* configurations — ones whose curvature decays sufficiently fast at infinity for the integral to converge. This is the natural condition for "particle-like" classical solutions, in analogy with finite-energy solutions of soliton equations.

*Why does finite action force topology?* The pointwise Cauchy–Schwarz inequality $|F(x)| \le |F(x)|$ gives the trivial bound, but the integral condition $\int |F|^2 < \infty$ requires $|F(x)| \to 0$ as $|x| \to \infty$ faster than $|x|^{-2}$. Hence $F$ decays at infinity, and the connection $A$ must approach a *pure-gauge* configuration $A \to g^{-1}dg$ for some $g : S^3_\infty \to G$. The homotopy class $[g] \in \pi_3(G)$ of this asymptotic gauge transformation is *gauge-invariant* and *topological* — it is the **instanton number** $k$. The formula $k = \frac{1}{8\pi^2}\int_{\mathbb{R}^4}\operatorname{tr}(F\wedge F)$ produces this integer, and the integrality $k \in \mathbb{Z}$ is the content of the classification $\pi_3(SU(2)) = \mathbb{Z}$ (or $\pi_3(SU(N)) = \mathbb{Z}$ for $N \ge 2$, or $\pi_3(\text{any compact simply connected simple Lie group}) = \mathbb{Z}$).

*Why Yang–Mills?* If one dropped the YM equation and asked only for finite-action configurations with topological charge $k$, one would get the entire homotopy class $\mathcal{B}_k = \{A : \int\operatorname{tr}(F\wedge F)/8\pi^2 = k, \int|F|^2 < \infty\}/\mathcal{G}$ — an infinite-dimensional space. The YM equation cuts this down to the *critical points of $S_{\text{YM}}$ on each $\mathcal{B}_k$*, a much smaller finite-dimensional moduli space. The BPS bound $S \ge 8\pi^2|k|$ further singles out the *minimum-action* critical points, which by BPS-saturation are precisely the (anti-)self-dual ones. So in practice, "instanton" usually means "self-dual (or anti-self-dual) finite-action Yang–Mills solution", with self-duality being the analytically tractable form.

*Why Euclidean $\mathbb{R}^4$?* On Lorentzian Minkowski $\mathbb{R}^{1,3}$, the YM action $\tfrac12\int|F|^2$ is *not* positive-definite — the $-\vec E^2$ part can be arbitrarily negative — so finite action is no constraint, and there is no analogue of the topological-charge / action bound. The physical role of instantons (tunneling amplitudes in the quantum theory) requires Wick rotation $t \to it$ to Euclidean signature, where the path integral $\int\mathcal{D}A\, e^{iS}\to\int\mathcal{D}A\,e^{-S_E}$ becomes a positive-definite Gaussian dominated by configurations of low Euclidean action — that is, by instantons.

*Physical interpretation.* In the quantum theory, the Yang–Mills vacuum on $\mathbb{R}^3$ admits an infinite family of topologically distinct classical vacua, labelled by their winding number $n \in \mathbb{Z}$ (the homotopy class of the asymptotic gauge transformation on the spatial $\mathbb{R}^3$, identified at infinity to become $S^3$). An instanton with topological charge $k$ is, in the Wick-rotated picture, a Euclidean configuration interpolating from the vacuum with winding $n$ at $t_E = -\infty$ to the vacuum with winding $n+k$ at $t_E = +\infty$. Quantum mechanically, this represents *tunneling* between distinct vacua: the amplitude to go from $|n\rangle$ to $|n+k\rangle$ is dominated by $e^{-S_E[A_{\text{inst}}]} = e^{-8\pi^2 k/g^2}$ in the semiclassical limit. The instanton's contribution to physical observables is one of the cleanest examples of *non-perturbative* quantum field theory.

If one removed the boundary condition at infinity and worked on a closed 4-manifold like $S^4$, one would obtain essentially the same theory — the (compactified) instanton becomes a Yang–Mills connection on the compact $S^4$, with $\pi_3(G)$ classification of the underlying principal bundle. The choice $\mathbb{R}^4$ with finite-action condition and $S^4$ with non-trivial bundle are *equivalent* (related by stereographic projection), and analysts typically work on one or the other based on convenience.

---

# The Definition

An **instanton** on Euclidean $\mathbb{R}^4$ is a smooth connection $A$ on a principal $G$-bundle (for a compact Lie group $G$) over $\mathbb{R}^4$ that:
1. satisfies the **Yang–Mills equation** $d_A\star F = 0$;
2. has **finite Yang–Mills action** $S_{\text{YM}}[A] = \tfrac12\int_{\mathbb{R}^4}|F|^2\,d^4x < \infty$.

Equivalently, an instanton is a finite-action critical point of $S_{\text{YM}}$ on $\mathbb{R}^4$.

The integer

$$k = \frac{1}{8\pi^2}\int_{\mathbb{R}^4}\operatorname{tr}(F\wedge F)$$

is the **instanton number**, also called the **topological charge** or **second Chern number**. It takes values in $\pi_3(G) \cong \mathbb{Z}$ (for $G = SU(2)$ and any compact simply-connected simple Lie group).

The asymptotic behaviour of an instanton is controlled by finiteness of the action: as $|x| \to \infty$, the field strength $F$ decays to zero, and the connection approaches a pure-gauge configuration $A \to g^{-1}dg$ for some smooth $g : S^3_\infty \to G$. The homotopy class $[g] \in \pi_3(G)$ equals the instanton number $k$, giving the topological-vs-integral identity

$$k = \frac{1}{8\pi^2}\int_{\mathbb{R}^4}\operatorname{tr}(F\wedge F) = \frac{1}{24\pi^2}\int_{S^3_\infty}\operatorname{tr}(g^{-1}dg)^3 = [g] \in \pi_3(G).$$

(The middle equality uses Stokes' theorem applied to the Chern–Simons 3-form $\operatorname{CS}(A) = \operatorname{tr}(A\wedge dA + \tfrac{2}{3}A\wedge A\wedge A)$, whose exterior derivative is $\operatorname{tr}(F\wedge F)$.)

**(Anti-)self-dual instantons** are instantons whose field strength satisfies $F = \pm\star F$. By the BPS bound, these are the *minimum-action representatives* in each topological sector, with $S_{\text{YM}}[A] = 8\pi^2|k|$. Most known explicit instanton solutions (BPST, 't Hooft, ADHM) are self-dual or anti-self-dual.

---

# Relate to Other Fields / Compression

**Instantons are a paradigm of *soliton* — a localised, finite-action classical solution of a non-linear field equation, classified by a topological charge.** The same general structure appears throughout mathematical physics:
- Magnetic monopoles in 3 dimensions: localised solutions of Yang–Mills–Higgs on $\mathbb{R}^3$, classified by $\pi_2(G/H) = \mathbb{Z}$ for spontaneous symmetry breaking $G \to H$.
- Vortices in 2 dimensions: localised solutions of abelian Higgs on $\mathbb{R}^2$, classified by $\pi_1(U(1)) = \mathbb{Z}$.
- Kinks in 1 dimension: localised solutions of $\phi^4$ on $\mathbb{R}$, classified by $\pi_0(\{\pm v\}) = \mathbb{Z}/2$.
- Skyrmions in 3D: localised maps $\mathbb{R}^3 \to SU(2)$, classified by $\pi_3(SU(2)) = \mathbb{Z}$.

In each case, the same structure repeats: a finite-action condition forces asymptotic decay to a vacuum, the asymptotic configuration is a map $S^{n-1} \to \text{vacuum manifold}$, and the homotopy class is a topological invariant — the soliton number.

**Instantons are also the *Euclidean path-integral saddle points* of Yang–Mills quantum field theory.** The path-integral computation $\langle\Omega| O|\Omega\rangle = \int\mathcal{D}A\, O[A]\,e^{-S_E[A]}/\int\mathcal{D}A\,e^{-S_E[A]}$ is, in the semiclassical limit $g \to 0$, dominated by configurations of low Euclidean action. The trivial vacuum $A = 0$ gives $S_E = 0$, but the $k = 1$ BPST instanton gives $S_E = 8\pi^2/g^2 = 8\pi^2/(g^2)$ — non-zero, but exponentially small in $1/g^2$ rather than perturbative. Instantons contribute *non-perturbative* effects to QCD (the $\theta$-vacuum, the axial anomaly, the $U(1)_A$ problem), to electroweak theory (B+L violation via sphalerons), and to supersymmetric gauge theory (Nekrasov's exact partition function, Seiberg–Witten theory).

**True name:** an instanton is *a Euclidean Yang–Mills bounce — a finite-action saddle point of the Euclidean action interpolating between distinct vacua*. The operational form is "look for finite-action solutions of YM on $\mathbb{R}^4$, classified by $\pi_3(G)$, with the SD/ASD ones being the action minima in each sector". The official definition is the technical version; the true name is the path-integral interpretation that explains *why* one cares.

---

# Examples / Corollaries

**Example 1 — The BPST $k=1$ instanton.** $A = \frac{\rho^2}{\rho^2 + r^2}\, g^{-1}dg$ with $g(x) = (x_0 - i\vec\sigma\cdot\vec x)/r$ for $SU(2)$ on $\mathbb{R}^4$. The action is $S = 8\pi^2$, the instanton number is $k = 1$, and the connection is self-dual. The parameter $\rho > 0$ is the **scale** of the instanton; translating the origin adds four more parameters (the **position** $a \in \mathbb{R}^4$). The full moduli space of $k = 1$ BPST instantons is therefore $(0, \infty) \times \mathbb{R}^4$, 5-dimensional, matching the index-theory prediction $\dim\mathcal{M}_1 = 8\cdot 1 - 3 = 5$. As $\rho \to 0$ the instanton "shrinks to a point" and develops a singularity on the boundary of moduli space — a feature called **bubbling**.

**Example 2 — The trivial connection is the $k = 0$ instanton.** $A = 0$ has $F = 0$, $S = 0$, and $k = 0$. The "moduli space" $\mathcal{M}_0$ is a single point (the trivial connection) — there are no non-trivial $k = 0$ instantons. This is consistent with the index formula $\dim\mathcal{M}_0 = 8\cdot 0 - 3 = -3$, indicating that for $k = 0$ the moduli space is "negative-dimensional", i.e., generically empty.

**Example 3 — Higher-charge ADHM instantons.** For $k \ge 2$, the moduli space $\mathcal{M}_k$ has dimension $8k - 3$ — 13 for $k = 2$, 21 for $k = 3$, etc. The **ADHM construction** (Atiyah–Drinfeld–Hitchin–Manin, 1978) parameterises all $SU(N)$ instantons of charge $k$ by sets of matrices $(B_1, B_2, I, J)$ satisfying algebraic ADHM equations modulo a $U(k)$ gauge action. The construction is an explicit bijection between the solutions of the non-linear self-duality PDE and the finite-dimensional algebraic variety of ADHM data. It is one of the most striking explicit constructions in modern geometry.

**Non-example — Lorentzian "instantons" do not exist.** On Minkowski space, the would-be instanton equation $F = \star F$ has $\star^2 = -1$ on 2-forms, so the only real solutions are $F = 0$ (trivial). One can study *complex* instantons with $F = i\star F$, but these do not have a direct physical interpretation as Lorentzian field configurations. The role of instantons in physics is *always* via Wick rotation to Euclidean signature — there is no Lorentzian counterpart.

**Calibration check.** A reader who has internalised the definition should be able to: (a) state that the BPST instanton has $k = 1$ and $S = 8\pi^2$, and verify these are consistent with the BPS bound $S \ge 8\pi^2|k|$ (it is saturated); (b) explain why the instanton number is necessarily an integer — the asymptotic gauge transformation $g : S^3 \to SU(2) \cong S^3$ has a Brouwer degree, which is the topological obstruction to extending $g$ to a map $D^4 \to SU(2)$; (c) name three physical applications of instantons (QCD $\theta$-vacuum, axial anomaly, electroweak sphalerons) and the corresponding role each plays.

---

# Unlocked by This

> [!tip] The QCD $\theta$-Vacuum and the Strong CP Problem *(from Quantum Chromodynamics)*
> Because Yang–Mills theory on $\mathbb{R}^4$ has an infinite family of classically degenerate vacua labelled by integer winding $n \in \mathbb{Z}$, and instantons mediate tunneling between them, the true quantum vacuum is the **$\theta$-vacuum** $|\theta\rangle = \sum_n e^{in\theta}|n\rangle$, parameterised by an angle $\theta \in [0, 2\pi)$. The $\theta$-angle is a fundamental parameter of QCD that adds a CP-violating term $\theta\cdot\operatorname{tr}(F\wedge F)/8\pi^2$ to the Lagrangian. Experimentally, $\theta \approx 0$ to a part in $10^{10}$ (from limits on the neutron electric dipole moment), a fact known as the **strong CP problem** — there is no a priori reason for $\theta$ to be small, since gravity-mediated effects should naturally give $\theta \sim O(1)$. The leading proposal to explain this — **Peccei–Quinn symmetry** — promotes $\theta$ to a dynamical field, the **axion**, which is among the leading dark-matter candidates and is the target of major experimental programmes (ADMX, CASPEr).

> [!tip] Nekrasov's Instanton Partition Function *(from Supersymmetric Gauge Theory)*
> The partition function of $\mathcal{N} = 2$ supersymmetric Yang–Mills theory on $\mathbb{R}^4$ can be computed *exactly* — non-perturbatively — by summing over all topological sectors, with the contribution of each instanton sector given by a localisation formula on the ADHM moduli space. **Nekrasov's instanton partition function** $Z_{\text{inst}}(a, \epsilon_1, \epsilon_2)$ (2002) expresses this sum as a product of explicit rational functions of the Coulomb-branch parameter $a$ and the equivariant parameters $\epsilon_1, \epsilon_2$. In the limit $\epsilon \to 0$, $\log Z_{\text{inst}}$ recovers the Seiberg–Witten prepotential — the holomorphic function determining the low-energy effective theory of $\mathcal{N} = 2$ gauge theory. Nekrasov's formula was a milestone in the mathematical understanding of non-perturbative supersymmetric gauge theory and the seed of the **AGT correspondence** relating 4D gauge theories to 2D conformal field theories.
