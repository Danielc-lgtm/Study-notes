---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Brownian Loop Measure"
  - "Def - Dirichlet Form Loop Measure"
  - "Def - Disintegration and the Bridge Measure"
  - "Def - Heat Kernel and Heat Semigroup"
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
  - "Def - Hyperbolic 3-Space, Kleinian Groups, and Complex Length"
tags: [paper, brownian-loops, hyperbolic-geometry, probability]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §7 opening — why the surface construction lifts unchanged to any complete Riemannian manifold, and in particular to hyperbolic 3-manifolds"
---

# Notation

- $(M, g)$ — a complete oriented Riemannian manifold; in the paper $M = \mathbb{H}^2$ (surface case, §§2–6) or $M = \mathbb{H}^3$ (this section).
- $\Delta_g$ — the Laplace–Beltrami operator; $\operatorname{vol}_g$ the Riemannian volume measure.
- $p_g(t, z, w)$ — the Brownian heat kernel on $(M, g)$ (fundamental solution of $\partial_t f = \frac12 \Delta_g f$).
- $\mathbb{W}^{t,g}_{z\to w}$ — the Brownian bridge measure on $M$: the law of Brownian motion started at $z$ conditioned to be at $w$ at time $t$, of total mass $p_g(t, z, w)$.
- $dt/t$ — the multiplicative Haar measure on $(0, \infty)$; the loop-length weighting.
- $\mu_M$ — the Brownian loop measure on $M$, defined by $\mu_M = \int_0^\infty \frac{dt}{t}\int_M \mathbb{W}^{t,g}_{z\to z}\,d\operatorname{vol}_g(z)$.
- $\Gamma$ — a discrete, torsion-free group of isometries of a symmetric space $\widetilde X$ ($\mathbb{H}^2$ for surfaces, $\mathbb{H}^3$ here); $X = \Gamma\backslash \widetilde X$ the quotient manifold.
- $\phi$ — a Bernstein function; $(S_t)$ its subordinator; $\mu^\phi_X$ the subordinate Brownian loop measure on $X$.

> [!recall]- Complete Riemannian manifold
> **Formally:** a Riemannian manifold $(M, g)$ is *complete* if its distance metric $d_g$ makes $M$ a complete metric space; equivalently (Hopf–Rinow) every maximal geodesic is defined on all of $\mathbb{R}$.
> **In words:** you cannot "walk off the edge" — following any geodesic direction, you can keep going for all time. There is no boundary and no missing point.
> **Concretely:** $\mathbb{R}^n$, the round sphere $S^n$, the flat torus $T^n$, and $\mathbb{H}^n$ (in any model) are complete; $\mathbb{R}^n \setminus \{0\}$ and the open unit disc with the induced Euclidean metric are not (a straight-line geodesic hits the missing point / boundary in finite time). Completeness is what makes the heat kernel exist as a genuine transition density: Brownian motion has no chance of escaping to the boundary in finite time.

> [!recall]- Bridge measures $\mathbb{W}^{t,g}_{z\to w}$
> **Formally:** the disintegration of the Brownian path law $\mathbb{W}^{t,g}_z$ (starting at $z$, running for time $t$) with respect to the endpoint map $\omega \mapsto \omega(t)$; equivalently, the conditional law given $\omega(t) = w$. It is a positive measure of total mass $p_g(t, z, w)$ on the space of continuous paths $[0, t] \to M$ from $z$ to $w$.
> **In words:** "all Brownian motions from $z$ to $w$ over time $t$, weighted by how likely each is under Brownian motion." Not a probability measure — its total mass is the heat kernel, which vanishes as $t \to \infty$ and blows up as $z \to w$ with small $t$.
> **Concretely:** on $\mathbb{R}$, $\mathbb{W}^{t}_{0\to 0}$ is Brownian bridge law scaled by the density $p(t, 0, 0) = (2\pi t)^{-1/2}$; on any complete Riemannian manifold the same disintegration exists because $p_g(t, z, w)$ is jointly continuous and positive. See [[Def - Disintegration and the Bridge Measure]].

> [!recall]- Subordination by a Bernstein function
> **Formally:** for a Bernstein function $\phi : (0, \infty) \to (0, \infty)$ (concave, non-decreasing, with completely monotone derivative), the *subordinator* $(S_t)_{t \ge 0}$ is a non-decreasing càdlàg Lévy process with Laplace transform $\mathbb{E}[e^{-\lambda S_t}] = e^{-t\phi(\lambda)}$. The subordinate process is $Y_t = B_{S_t}$ (time-change of Brownian motion by an independent subordinator).
> **In words:** you replace the time-clock of Brownian motion by a random non-decreasing clock — the process jumps when the clock jumps, so a diffusion becomes a jump-diffusion. Concrete cases: $\phi(\lambda) = \lambda$ (identity — pure Brownian); $\phi(\lambda) = \lambda + \kappa$ (killed at rate $\kappa$); $\phi(\lambda) = \lambda^{\alpha/2}$ ($\alpha$-stable process, $0 < \alpha < 2$).
> **Concretely:** for $\phi(\lambda) = \lambda^{1/2}$ (the $\alpha = 1$ Cauchy case), $S_t$ is a $\frac12$-stable subordinator with heavy-tailed jumps, and $Y_t = B_{S_t}$ is the Cauchy process — its paths are discontinuous and have infinite total variation. See [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- Conformal invariance of the Brownian loop measure (surface-specific)
> **Formally:** on a 2-dimensional Riemannian manifold, if $g' = e^{2\varphi} g$ is a conformal change of metric with $\varphi$ compactly supported, then the Brownian loop measure $\mu_{g'}$ equals $\mu_g$ — the loop measure depends only on the conformal class of $g$, not on $g$ itself.
> **In words:** in 2D, the Brownian loop measure "cannot see" a smooth, positive rescaling of the metric — it is a conformal-geometry object, not a Riemannian-geometry object. This is a genuine 2D miracle; it fails in every other dimension.
> **Concretely:** on the round sphere $S^2$ and the round sphere rescaled by any smooth positive function, the loop measure is the same measure on the same space of loops. On $\mathbb{H}^2$ this underwrites the Polyakov anomaly formula (§5) and the Wang–Xue length-spectrum identity (§3.4). See [[Remark - Conformal Invariance of the Brownian Loop Measure Is Two-Dimensional]].

---

# Claim / Identity

> **Claim (Why the surface construction lifts to 3-manifolds).** The entire loop-measure and homotopy-decomposition machinery of §§2–3 uses the ambient manifold $X$ only through structures that exist on any complete Riemannian manifold (heat kernel, bridge measures, volume, multiplicative Haar $dt/t$) and uses the covering group $\Gamma$ only through discreteness plus a cyclic-centraliser descent step. Neither ingredient is two-dimensional. The sole 2D-specific input in the paper is conformal invariance of the Brownian loop measure, which is invoked only in §5 (Polyakov anomaly) and §3.4 (the Wang–Xue length-spectrum identity, itself citing [WX25]) and disappears whenever a killing rate or a non-identity Bernstein subordination is imposed. So Definitions 2.1–2.10, Theorem 2.12, Theorem 3.2, and Remark 3.1 all transfer *verbatim* to $X = \Gamma\backslash \mathbb{H}^3$ with a torsion-free Kleinian $\Gamma$, and this section derives the 3-manifold analogues by making the substitution $\mathbb{H}^2 \leadsto \mathbb{H}^3$, $\mathrm{PSL}(2, \mathbb{R}) \leadsto \mathrm{PSL}(2, \mathbb{C})$, hyperbolic $\leadsto$ loxodromic, real translation length $\ell_\gamma \leadsto$ complex length $L_\gamma$ throughout.

---

# In One Line

The §§2–3 machinery uses only ingredients any complete Riemannian manifold has (heat kernel, bridges, $dt/t$, volume) and a group-descent step that needs only cyclic centralisers, so it lifts unchanged from $\mathbb{H}^2$ to $\mathbb{H}^3$; conformal invariance was the sole surface-specific hypothesis, and it is not used in the subordinate cases §7 targets.

---

# Why It's True

Read the definitions of §2 with a highlighter over every place the ambient manifold enters: the heat kernel $p_g(t, z, w)$, the bridge measure $\mathbb{W}^{t,g}_{z\to w}$, the loop measure at a base point $\int_0^\infty p_g(t,z,z)\,dt/t$, and the integration over $X$ with respect to $\operatorname{vol}_g$. Nothing else. Every one of these is a legitimate object on any complete Riemannian manifold — the heat kernel because $-\frac12\Delta_g$ is essentially self-adjoint and positive, the bridge measures by disintegration of the heat semigroup, $dt/t$ because $(0, \infty)$ has a multiplicative group structure independent of dimension, and $\operatorname{vol}_g$ because the metric is what defines it. So the loop measure $\mu_X$ is a definition on any complete Riemannian $X$; the paper's use of "surface" in §2 is a convenience, not a constraint.

The §3 descent step is more delicate but still dimension-free. The class-mass computation isolates one conjugacy class in the group-sum kernel and unfolds it over left cosets of the *centraliser* $C_\Gamma(\tau^m)$. That centraliser is $\langle\tau\rangle$ (infinite cyclic) as soon as $\tau$ is a primitive element of a torsion-free discrete group of isometries of a symmetric space of rank one — the axis-preserving subgroup of such a group is cyclic on general grounds, not because the ambient dimension is two. So the "one-conjugate-per-coset" enumeration and the "fold onto the fundamental slab" step both survive verbatim.

The single load-bearing 2D-specific hypothesis in the paper is *conformal invariance* of the Brownian loop measure. That hypothesis powers exactly two things: the Polyakov anomaly formula of §5 (which is genuinely a 2D theorem — Polyakov's formula has no natural analogue in higher dimensions) and the length-spectrum identity of §3.4 (which cites [WX25], whose proof uses 2D conformal geometry). §7 does neither of these things. It only re-derives the class-mass formula, which needs no conformal invariance at all — and, importantly, imposing a killing rate or any nonlinear Bernstein subordination *destroys* conformal invariance, so §5's and §3.4's obstructions are absent from the subordinate cases the paper cares about downstream. **Mechanism: strip §§2–3 down to its non-optional ingredients (heat kernel, bridges, volume, $dt/t$, cyclic centraliser), observe that all of them exist on any complete Riemannian manifold, note that the one 2D-specific hypothesis (conformal invariance) enters only in §5 and §3.4 and is absent in the subordinate setup §7 targets, and conclude the machinery transfers to $\mathbb{H}^3$ unchanged.**

---

# Derivation

> [!note]- Gap-free derivation
>
> **Step 1 (audit the §2 ingredients).** The Brownian loop measure of Definition 2.10 is
> $$\mu_X = \int_0^\infty \frac{dt}{t}\int_X \mathbb{W}^{t,g}_{z\to z}\,d\operatorname{vol}_g(z),$$
> and the subordinate Brownian loop measure of Definition 2.12 is the same expression with $p_g$ replaced by $p^\phi_g(t,z,w) = \int p_g(s,z,w)\,\psi^\phi_t(ds)$. Symbol by symbol:
>
> - $p_g(t, z, w)$ — fundamental solution of $\partial_t f = \frac12 \Delta_g f$ on $L^2(X, \operatorname{vol}_g)$. Exists for any complete $(X, g)$ because $-\frac12\Delta_g$ is essentially self-adjoint on $C_c^\infty(X)$ (Chernoff), hence generates a strongly continuous symmetric contraction semigroup $e^{t\Delta_g/2}$, hence has a jointly-continuous positive integral kernel by Aronson-type bounds.
> - $\mathbb{W}^{t,g}_{z\to w}$ — disintegration of $\mathbb{W}^{t,g}_z$ against the endpoint map. Exists for any complete Riemannian manifold by the regular-disintegration theorem applied to the transition kernel of Brownian motion.
> - $dt/t$ — multiplicative Haar on $(0, \infty)$. Independent of $X$ altogether.
> - $\operatorname{vol}_g$ — the Riemannian volume, defined by the metric alone.
>
> No use of the dimension of $X$ enters any of these definitions. In particular Definition 2.10 (the Brownian loop measure), Definition 2.12 (the subordinate Brownian loop measure), Definition 2.9 (the weighted potential measure $V_\phi$), Lemma 2.11 (time-integral collapse), and the whole subordination apparatus of §2 are defined for any complete Riemannian $X$.
>
> **Step 2 (audit the §3 descent).** [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]'s proof uses four ingredients:
>
> (i) The heat-kernel descent $p^E_X(t, z, w) = \sum_{h \in \Gamma} p^E_{\widetilde X}(t, \tilde z, h \tilde w)$ (a periodisation on the universal cover; convergent whenever the geometrically-finite $\Gamma$'s orbit growth is dominated by the kernel decay, which holds on any negatively-curved symmetric space).
>
> (ii) Isolation of one conjugacy class in the group sum — a purely algebraic step (partition a group sum into conjugacy classes).
>
> (iii) Unfolding over cosets of the centraliser: $[\tau^m]_{\mathrm{conj}} = \bigsqcup_{r \in \Gamma/C_\Gamma(\tau^m)} \{r\tau^m r^{-1}\}$, one conjugate per left coset. This is a general group-theoretic fact (orbit–stabiliser for conjugation).
>
> (iv) Reassembly onto the fundamental region of $C_\Gamma(\tau^m)$ via $\Gamma$-invariance of the kernel and the fact that $C_\Gamma(\tau^m) = \langle\tau\rangle$ is cyclic.
>
> Only (iv) needs comment for $\Gamma$ Kleinian. In a torsion-free discrete group of isometries of a rank-one symmetric space, the centraliser of a primitive loxodromic (equivalently, hyperbolic, in 2D) element is cyclic: any $h$ commuting with $\tau^m$ preserves the axis of $\tau^m$, and the axis-preserving subgroup of $\Gamma$ is a discrete infinite cyclic group generated by the primitive $\tau$. This proof is dimension-free — "axis" is the geodesic $\tau$ acts on by translation, present in both $\mathbb{H}^2$ and $\mathbb{H}^3$ (and in any hyperbolic space).
>
> **Step 3 (locate every 2D-specific input).** Search §§2–6 for a hypothesis that uses two-dimensionality:
>
> - §2.1–2.4 (loop measure, subordination, Dirichlet form, decomposition): no 2D input.
> - §3.1–3.3 (Theorem 3.2, Remark 3.1, [[Lemma - Wang-Xue Strip Integral|Lemma 3.4]]): Theorem 3.2 and Remark 3.1 use no 2D input; Lemma 3.4 evaluates a $\mathbb{H}^2$-specific strip integral and is replaced in §7 by a $\mathbb{H}^3$-specific one — same *role*, different formula.
> - §3.4 (length-spectrum identity of Wang–Xue): uses conformal invariance of the loop measure, cited from [WX25]. 2D-specific.
> - §4 (zeta functions): uses only Theorem 3.2's output, dimension-free once Theorem 3.2 is available.
> - §5 (Polyakov anomaly, determinant of the Laplacian): uses conformal invariance essentially (Polyakov's formula is a 2D identity). 2D-specific.
> - §6 (probability measure, homology characters, Poissonisation): uses only Theorem 3.2's output and finite-abelian-Fourier over $H_1(X, \mathbb{Z})$, dimension-free.
>
> **Step 4 (verify conformal invariance is absent in the subordinate cases).** [[Remark - Conformal Invariance of the Brownian Loop Measure Is Two-Dimensional]] shows conformal invariance holds for pure Brownian motion in 2D and fails as soon as a killing rate $\kappa > 0$ or a non-identity Bernstein $\phi \ne \lambda$ enters — the killing term is a mass in the ambient metric, not a conformal object, and any nonlinear $\phi$ produces a jump measure that depends on the metric beyond its conformal class. So even in 2D, the killed and subordinate loop measures are Riemannian objects, not conformal ones. §7's target objects (Theorem 7.2's subordinate class-mass, Corollary 7.3's Brownian class-mass) do not touch §5 or §3.4 and do not require conformal invariance.
>
> **Step 5 (the substitution recipe).** Everything §§2–3 does for surfaces transfers to 3-manifolds by the substitution
> $$\mathbb{H}^2 \leadsto \mathbb{H}^3,\quad \mathrm{PSL}(2, \mathbb{R}) \leadsto \mathrm{PSL}(2, \mathbb{C}),\quad \text{hyperbolic} \leadsto \text{loxodromic},\quad \ell_\gamma \leadsto L_\gamma = \ell_\gamma + i\theta_\gamma$$
> throughout. Theorem 7.1 is the substituted Theorem 3.2; [[Lemma - Hyperbolic 3-Space Strip Integral|the strip integral of §7.2]] is the substituted Lemma 3.4; Theorem 7.2 is the substituted [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]]; Corollary 7.3 is the substituted [[Thm - Mass of a Free Homotopy Class#Corollary]] surface Brownian mass. No re-proof of the underlying machinery is needed — only re-computation of the strip integral, because the $\mathbb{H}^3$ heat kernel is a different explicit function than the $\mathbb{H}^2$ heat kernel and evaluates the strip integral in closed form (see [[Remark - In-House Derivation of the H3 Strip Integral]]).
>
> $\square$

---

# Where the paper uses this

Opens [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7]] and licenses every subsequent 3-manifold result:

- [[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]] (verbatim transfer of Theorem 3.2);
- [[Thm - Mass of Subordinate Loops on 3-Manifolds|Theorem 7.2]] (verbatim transfer of Theorem 3.5);
- [[Cor - Brownian Mass on 3-Manifolds|Corollary 7.3]] (the 3D specialisation to pure Brownian motion);
- and, by the same logic, the paper's own pointer that §§4 and 6's zeta/probability apparatus lifts to 3D by replacing $\ell_\gamma$ with $L_\gamma$ and $\sinh^2$ with $|e^L - 1|^2$ throughout (flagged as intuition, not developed).

Downstream in the general theory: the same lift argument works on any negatively-curved locally symmetric space of rank one (real hyperbolic $\mathbb{H}^n$, complex hyperbolic $\mathbb{H}^n_{\mathbb{C}}$, quaternionic hyperbolic, Cayley plane), replacing "loxodromic" by the appropriate class of "translation-with-transverse-rotation" isometries — a direction the paper mentions in passing but does not pursue.
