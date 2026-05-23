---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Path-Product and the Fundamental Group"
  - "Def - Universal Cover"
  - "Def - Smooth Manifold"
tags: [geometry, algebraic-topology, riemannian-geometry]
---

# Notation

$M^n$ is a complete connected Riemannian manifold of dimension $n$. $\mathrm{Ric}(v, v)$ is the Ricci curvature in unit direction $v$. **Complete** means geodesically complete: every maximal geodesic is defined for all time. $\widetilde M$ is the universal cover. $\pi_1(M)$ is the fundamental group. $\mathrm{diam}(M) := \sup_{p, q \in M} d(p, q)$ is the diameter. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Statement

> **Theorem (S. B. Myers).** Let $M^n$ be a complete connected Riemannian manifold satisfying the Ricci curvature lower bound
> $$\mathrm{Ric}(v, v) \;\geq\; (n - 1)\kappa$$
> for all unit tangent vectors $v$, where $\kappa > 0$ is a positive constant. Then:
>
> 1. **(Diameter bound)** $M$ has finite diameter, $\mathrm{diam}(M) \leq \pi / \sqrt{\kappa}$;
> 2. **(Compactness)** $M$ is compact;
> 3. **(Finite fundamental group)** $\pi_1(M)$ is finite.

The corollary on $\pi_1$ is the headline application from the perspective of this chapter; the diameter bound is the underlying Riemannian-geometry result. The full Riemannian-geometry treatment, including the proof of the diameter bound via the second variation of arc length, is in [[Riemannian Geometry III — Riemann Curvature and Topology]]; here we focus on the $\pi_1$ consequence.

---

# Motivation

Positive curvature is a strong condition on the geometry of a manifold. Intuitively, positive curvature "pulls geodesics together" — neighbouring geodesics converge rather than diverge. The Ricci curvature is an average of sectional curvatures, so $\mathrm{Ric} \geq (n-1)\kappa > 0$ says the average sectional curvature in every direction is positive and bounded below.

Myers' theorem converts this geometric condition into a *topological* conclusion: $\pi_1$ is finite. This is one of the most striking instances of the philosophy "curvature controls topology" — local geometric data (curvature, infinitesimal) constrains global topological invariants ($\pi_1$, fundamental for shape). The mechanism is the universal cover: positive curvature on $M$ pulls back to positive curvature on $\widetilde M$, which forces $\widetilde M$ also to be compact (via the diameter bound), and a compact cover of a compact space must be finite-sheeted, giving finite $\pi_1$.

The theorem has a long history. The two-dimensional case (where $\mathrm{Ric}(T, T)$ is just the Gauss curvature $K$) was proved by Bonnet in 1855: a complete surface with $K \geq c > 0$ has diameter $\leq \pi/\sqrt{c}$ and is compact. The $n$-dimensional generalisation with Ricci curvature was proved by S. B. Myers in 1941, replacing sectional curvature with the weaker Ricci bound. Generalisations relax positivity (Galloway's theorem: $\mathrm{Ric}(T,T) \geq c + df/ds$ along geodesics is enough), and play an essential role in general relativity (singularity theorems of Hawking and Penrose).

The crucial fact is that $\mathrm{Ric}$ is *weaker* than $\sec$: positive sectional curvature implies positive Ricci, but not conversely. So Myers' theorem applies in many cases where $\sec > 0$ would fail. The conclusion is also strictly weaker than Synge's theorem (positive sectional curvature in even dimensions + orientable → *simply* connected), which says $\pi_1 = 0$ rather than $\pi_1$ finite. Myers and Synge together form the standard pair of "positive-curvature theorems."

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "positive Ricci bounded below" applies in various disguises.

The first source is **a complete Riemannian manifold with $\sec \geq \kappa > 0$**. Sectional curvature lower bound trivially implies Ricci lower bound (Ricci is the trace, $\mathrm{Ric}(v, v) = \sum_{j=2}^n K(v \wedge e_j) \geq (n-1)\kappa$ for $K \geq \kappa$). So all of the positive-sectional-curvature spaces are covered: round spheres $S^n$ (with constant sectional $\kappa$), $\mathrm{SU}(2)$ with bi-invariant metric, compact symmetric spaces of positive curvature.

The second source is **a closed Riemannian manifold with positive scalar curvature, in dimension 2**. In two dimensions, $\mathrm{Ric}(T, T) = K(T)$ for any unit $T$ (Ricci = Gauss curvature), so $\mathrm{Ric} \geq c$ iff $K \geq c$. Bonnet's theorem from 1855 applies.

The third source is **Einstein manifolds with positive cosmological constant**. An Einstein manifold satisfies $\mathrm{Ric} = \lambda g$ for some constant $\lambda$. If $\lambda > 0$, then $\mathrm{Ric}(v, v) = \lambda \geq (n-1) \cdot \frac{\lambda}{n-1}$, so Myers applies with $\kappa = \lambda/(n-1) > 0$.

The fourth source is **a Lie group with bi-invariant metric and non-trivial centre algebra**. A compact Lie group $G$ admits a bi-invariant metric (see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]]); the Ricci curvature in such a metric is $\mathrm{Ric}(X, X) = \frac14 \sum |[X, e_j]|^2$, which is positive iff the centre $Z(\mathfrak{g})$ is trivial. So for any compact Lie group with trivial centre — $\mathrm{SU}(n)/Z$, $\mathrm{SO}(n)/Z$, etc. — Myers gives finite $\pi_1$. This is essentially Weyl's theorem (21.24 in Frankel) for the topology of Lie groups.

**Targets (Output Amplification)**

The conclusion is "$M$ compact and $\pi_1(M)$ finite"; combined with other tools, this leads to specific structural results.

The first combination is **with the order of $\pi_1$**: knowing $|\pi_1(M)|$ is finite often lets you compute or bound it. For example, $S^n$ with the round metric has $\mathrm{Ric} = n - 1$, so Myers gives $\pi_1(S^n)$ finite for $n \geq 2$; we know $\pi_1(S^n) = 0$ from other arguments, consistent. For $\mathbb{RP}^n$ with the round metric (positive Ricci inherited from $S^n$), Myers gives finite $\pi_1$; we know $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$.

The second combination is **with the universal cover construction**: positive Ricci on $M$ implies $\widetilde M$ compact (since the metric lifts and the Ricci bound persists). Combined with $\widetilde M = M / \pi_1(M)$, this gives the structure of $\widetilde M$ as a finite-sheeted cover. The combined statement is: positive Ricci → finite-sheeted universal cover.

The third combination is **with Synge's theorem**: in even dimensions and the orientable case, the stronger hypothesis $\sec > 0$ gives $\pi_1 = 0$ rather than just finite. Combining "Myers + orientability + even-dim + sectional bound" sharpens the conclusion. This is the relation explained in Frankel just after Myers' corollary.

The fourth combination is **with Bochner's theorem**: positive Ricci implies $b_1(M) = 0$ (no harmonic 1-forms). Myers' theorem, by giving compactness and finite $\pi_1$, implies a fortiori $b_1 = 0$ (since $b_1 = \mathrm{rk}_\mathbb{Z}(\pi_1(M)^{\mathrm{ab}}) = 0$ when $\pi_1$ is finite). So Myers $\Rightarrow$ Bochner. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

---

# Why Is It True

The intuition is that **positive Ricci shortens distances**: long geodesics cannot exist when curvature is uniformly positive. The reason: the second variation of arc length along a geodesic with $\mathrm{Ric} > 0$ in the orthogonal directions becomes negative for sufficiently long geodesics, meaning the geodesic is not length-minimising. So no two points can be farther than $\pi/\sqrt{\kappa}$ apart, which is the diameter bound.

**The bolded one-liner: positive Ricci forces every geodesic of length $> \pi/\sqrt{\kappa}$ to fail the second-variation test for length-minimisation, so by Hopf-Rinow no two points are farther than that distance, $M$ is bounded and complete, hence compact, hence its universal cover is also compact (positive-Ricci-lifts), and a compact cover of a compact manifold must be finite-sheeted.**

The chain of implications, packaged as a Riemannian-geometry pipeline:

1. **Second variation of arc length.** For a unit-speed geodesic $C : [0, L] \to M$ between $p$ and $q$, the second derivative of length along a variation with vector field $J$ orthogonal to $C$ is
$$L''(0) = \int_0^L \left( |\nabla_T J|^2 - \langle R(J, T) T, J \rangle \right) ds$$
(Synge's formula). Choosing $J = f(s) e_i$ for an orthonormal parallel frame $\{e_2, \dots, e_n\}$ orthogonal to $T$, and summing over $i$ gives
$$\sum_{i=2}^n L_i''(0) = \int_0^L \left( (n-1) |f'(s)|^2 - |f(s)|^2 \, \mathrm{Ric}(T, T) \right) ds.$$

2. **Test function $f(s) = \sin(\pi s / L)$.** With this choice and $\mathrm{Ric}(T, T) \geq (n-1)\kappa$,
$$\sum_{i=2}^n L_i''(0) \leq \frac{L \pi^2 (n-1)}{2 L^2} - \frac{L(n-1)\kappa}{2} = \frac{(n-1)L}{2}\left( \frac{\pi^2}{L^2} - \kappa \right).$$
This is *negative* whenever $L > \pi / \sqrt{\kappa}$.

3. **Length-minimisation forced to fail.** A negative sum of second variations means at least one $L_i''(0) < 0$, so $C$ is not length-minimising for that variation. Hence no geodesic of length $> \pi/\sqrt{\kappa}$ between any two points is length-minimising.

4. **Hopf-Rinow finishes diameter.** $M$ complete, so any pair of points is joined by a minimising geodesic (Hopf-Rinow). That geodesic has length $\leq \pi/\sqrt{\kappa}$. So $\mathrm{diam}(M) \leq \pi/\sqrt{\kappa}$.

5. **Bounded complete → compact.** $M$ has finite diameter; the closed metric ball of radius $\pi/\sqrt{\kappa}$ around any point is all of $M$. By Hopf-Rinow (closed bounded balls in a complete Riemannian manifold are compact), $M$ is compact.

6. **Universal cover inherits positive Ricci.** The universal cover $\widetilde M \to M$ is a local isometry (lift the metric via the covering map), so the Ricci curvature pulls back: $\mathrm{Ric}_{\widetilde M}$ also satisfies the same lower bound. $\widetilde M$ is complete (local-isometric image of geodesically complete $M$). So Myers applies to $\widetilde M$ — it is also compact.

7. **Compact cover of compact → finite-sheeted.** If $\widetilde M \to M$ were infinite-sheeted, any cover of $M$ by an open set $U$ containing $p_0$ (small enough to be evenly covered) would pull back to infinitely many disjoint open sets in $\widetilde M$ — a non-finite cover of compact $\widetilde M$, contradicting compactness. So the cover is finite-sheeted.

8. **Number of sheets = $|\pi_1(M)|$.** For the universal cover, sheet count = $|\pi_1(M)|$. So $\pi_1(M)$ is finite.

The whole pipeline is: Ricci + second variation + Hopf-Rinow = diameter bound = compactness, then transport to the universal cover, then deduce finite sheets.

---

# What Makes This Hard

The proof has two technical pieces. **First**, the second-variation calculation requires care: choosing the right variation vector ($J = f(s) e_i$ with $f$ vanishing at endpoints), the right test function ($\sin(\pi s/L)$, not just any function), and summing over an orthonormal frame are non-obvious. **Second**, the transport of the curvature bound to the universal cover requires that the metric lifts canonically and that the lift is a local isometry — a fact that follows from the covering structure but requires being careful about what "Riemannian metric on a cover" means.

Common errors: (a) Forgetting that the universal cover is automatically Riemannian (lift the metric via the local diffeomorphism of $\pi$), so the same Ricci bound applies; (b) confusing $\sec$ with $\mathrm{Ric}$ — Myers needs the weaker Ricci bound, and a single negative sectional curvature can be compensated by larger positive ones in other directions while keeping the Ricci trace bounded below; (c) failing to invoke completeness — without geodesic completeness, Hopf-Rinow does not give length-minimising geodesics, and the argument breaks. Frankel emphasises completeness explicitly: the paraboloid $z = x^2 + y^2$ has positive Gauss curvature but is *not* complete and hence not compact, escaping the theorem.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** (a) Use the second variation of arc length to show no geodesic of length $> \pi/\sqrt{\kappa}$ is length-minimising, hence the diameter is $\leq \pi/\sqrt{\kappa}$. (b) Bounded complete Riemannian manifold is compact (Hopf-Rinow). (c) The universal cover inherits the Ricci bound (local isometry) and is complete, hence also compact. (d) A compact covering space of a compact space is finite-sheeted; sheet count = $|\pi_1|$.

**Subgoal decomposition:**

1. **Second variation formula.** Set up the second variation of arc length along a unit-speed geodesic $C$ with variation vector $J = f(s) e$ for $e$ parallel orthogonal to $C$. Derive the formula
$$L''(0) = \int_0^L (|f'|^2 - |f|^2 R(e, T, T, e)) \, ds.$$
   - *Hint:* Standard Riemannian calculation; see [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]] for details.
   - *Why needed:* Provides the analytic tool for the Ricci-bound argument.

2. **Sum over orthonormal frame.** Take $\{e_2, \dots, e_n\}$ orthonormal parallel along $C$, orthogonal to $T$. Sum the $(n-1)$ second variations to get
$$\sum_{i=2}^n L_i''(0) = \int_0^L \left((n-1)|f'|^2 - |f|^2 \mathrm{Ric}(T, T)\right) ds.$$
   - *Hint:* $\sum_{i=2}^n R(e_i, T, T, e_i) = \mathrm{Ric}(T, T)$ by definition of Ricci as a trace.
   - *Why needed:* Converts sectional-curvature data to Ricci-curvature data.

3. **Choose $f(s) = \sin(\pi s / L)$.** Compute
$$\int_0^L |f'|^2 \, ds = \frac{\pi^2}{2L}, \quad \int_0^L |f|^2 \, ds = \frac{L}{2}.$$
   - *Hint:* Standard integrals over $[0, L]$ of $\cos^2(\pi s/L)$ and $\sin^2(\pi s/L)$.
   - *Why needed:* Plugs the test function into the formula.

4. **Combine with $\mathrm{Ric} \geq (n-1)\kappa$.** Substituting gives
$$\sum_{i=2}^n L_i''(0) \leq \frac{(n-1) \pi^2}{2L} - \frac{(n-1)L\kappa}{2} = \frac{(n-1)L}{2}\left(\frac{\pi^2}{L^2} - \kappa\right).$$
This is negative iff $L > \pi/\sqrt{\kappa}$.
   - *Hint:* Direct algebra.
   - *Why needed:* Shows the second variation can be made negative for long enough geodesics.

5. **Conclude $C$ is not length-minimising.** If at least one $L_i''(0) < 0$, then $C$ is *not* a local minimum of length; in particular, not length-minimising between its endpoints.
   - *Hint:* Standard variational argument.
   - *Why needed:* Negates the assumption of $C$ being a length-minimising geodesic of length $> \pi/\sqrt{\kappa}$.

6. **Hopf-Rinow gives diameter bound.** $M$ complete + every pair joined by length-minimising geodesic (Hopf-Rinow) + length-minimising geodesics have length $\leq \pi/\sqrt{\kappa}$ implies $\mathrm{diam}(M) \leq \pi/\sqrt{\kappa}$.
   - *Hint:* Hopf-Rinow is non-trivial and is taken as input here; see [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].
   - *Why needed:* Compactness conclusion.

7. **Universal cover is also compact.** Lift the metric to $\widetilde M$ (local isometry); the lifted metric has the same Ricci bound; $\widetilde M$ is complete; apply Myers to $\widetilde M$ — it has finite diameter, hence is compact.
   - *Hint:* Local-isometry property of the universal cover.
   - *Why needed:* Sets up the finite-cover argument.

8. **Compact cover of compact $\Rightarrow$ finite sheets.** $\widetilde M$ compact $\Rightarrow$ any open cover of $\widetilde M$ has a finite subcover. The standard cover of $\widetilde M$ by sheets above evenly covered open sets of $M$ has at most finitely many sheets in any preimage; since $M$ is compact and is covered by finitely many evenly covered open sets, $\widetilde M$ is covered by finitely many sheets total. So the number of sheets is finite, hence $|\pi_1(M)|$ is finite.
   - *Hint:* Lebesgue + finite-subcover argument.
   - *Why needed:* The $\pi_1$-finiteness conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: Second variation under positive Ricci forces length-minimising failure for long geodesics
> **Statement:** Let $M$ have $\mathrm{Ric} \geq (n-1)\kappa > 0$, and let $C$ be a unit-speed geodesic in $M$ from $p$ to $q$ of length $L$. If $L > \pi/\sqrt{\kappa}$, then $C$ is not length-minimising.
>
> **Hint:** Construct $n - 1$ orthogonal variations with test function $\sin(\pi s/L)$; their second variations sum to a negative number, so at least one is negative.
>
> **Why needed:** Provides the diameter bound.
>
> > [!note]- Full proof
> > Let $\{e_2, \dots, e_n\}$ be parallel orthonormal vector fields along $C$ orthogonal to $T = \dot C$. Define $n - 1$ variation vector fields $J_i(s) = \sin(\pi s/L) e_i$ for $i = 2, \dots, n$. Each $J_i$ vanishes at the endpoints $s = 0$ and $s = L$, so each corresponds to a variation of $C$ fixing the endpoints. By the second variation formula (with the boundary term vanishing because $\nabla_J J(0) = \nabla_J J(L) = 0$ for such variations):
> > $$L_i''(0) = \int_0^L \left(|\nabla_T J_i|^2 - \langle R(J_i, T)T, J_i \rangle\right) ds = \int_0^L \left( |\sin'(\pi s/L)|^2 - |\sin(\pi s/L)|^2 R^i_{1i1}(s) \right) ds$$
> > where $R^i_{1i1}$ is the sectional curvature term. Summing $i = 2, \dots, n$:
> > $$\sum_{i=2}^n L_i''(0) = \int_0^L \left( (n-1) \frac{\pi^2}{L^2} \cos^2\left(\frac{\pi s}{L}\right) - \sin^2\left(\frac{\pi s}{L}\right) \mathrm{Ric}(T, T) \right) ds.$$
> > Using $\int_0^L \cos^2(\pi s/L) \, ds = L/2 = \int_0^L \sin^2(\pi s/L) \, ds$ and $\mathrm{Ric}(T, T) \geq (n-1)\kappa$:
> > $$\sum_{i=2}^n L_i''(0) \leq \frac{(n-1)\pi^2}{L^2} \cdot \frac{L}{2} - (n-1)\kappa \cdot \frac{L}{2} = \frac{(n-1)L}{2}\left(\frac{\pi^2}{L^2} - \kappa\right).$$
> > For $L > \pi/\sqrt{\kappa}$, this is negative. So at least one $L_i''(0) < 0$, meaning $C$ is not a local minimum of length for that variation. Hence $C$ is not length-minimising.

> [!note]- Lemma 2: Diameter bound from length-minimising geodesics
> **Statement:** A complete Riemannian manifold $M$ with $\mathrm{Ric} \geq (n-1)\kappa > 0$ has $\mathrm{diam}(M) \leq \pi/\sqrt{\kappa}$.
>
> **Hint:** Hopf-Rinow: complete implies every pair joined by length-minimising geodesic. Lemma 1: length-minimising forces length $\leq \pi/\sqrt{\kappa}$.
>
> **Why needed:** Diameter bound; one half of Myers' main statement.
>
> > [!note]- Full proof
> > For any pair $p, q \in M$, Hopf-Rinow (using completeness) gives a length-minimising geodesic from $p$ to $q$ of length $d(p, q)$. By Lemma 1, this length is $\leq \pi/\sqrt{\kappa}$. Hence $\mathrm{diam}(M) = \sup d(p, q) \leq \pi/\sqrt{\kappa}$.

> [!note]- Lemma 3: Bounded + complete Riemannian manifold is compact
> **Statement:** A complete Riemannian manifold with finite diameter is compact.
>
> **Hint:** Hopf-Rinow: closed bounded balls in a complete Riemannian manifold are compact. The whole manifold is the ball of radius $\mathrm{diam}(M)$ around any point.
>
> **Why needed:** Compactness conclusion.
>
> > [!note]- Full proof
> > Fix $p_0 \in M$. By Hopf-Rinow (one of the equivalent forms of completeness), the closed metric ball $\bar B(p_0, r)$ is compact for every $r$. With $r = \mathrm{diam}(M)$, the closed ball equals all of $M$ (every point is within distance $r$ of $p_0$ by definition of diameter). So $M$ is compact.

> [!note]- Lemma 4: Universal cover inherits Ricci bound
> **Statement:** If $M$ has $\mathrm{Ric} \geq (n-1)\kappa > 0$, then $\widetilde M$ (with the lifted Riemannian metric) has the same Ricci bound and is complete.
>
> **Hint:** $\pi : \widetilde M \to M$ is a local isometry; curvature is a local invariant.
>
> **Why needed:** Allows applying Myers to $\widetilde M$.
>
> > [!note]- Full proof
> > Define a Riemannian metric on $\widetilde M$ by pulling back from $M$ via $\pi$: $\widetilde g_x(v, w) := g_{\pi(x)}(d\pi_x v, d\pi_x w)$, well-defined because $\pi$ is a local diffeomorphism. With this metric, $\pi$ is a local isometry by construction. Sectional curvatures are local-isometry invariants, so $K_{\widetilde M}(\widetilde\sigma)$ at $x$ equals $K_M(d\pi_x \widetilde\sigma)$ at $\pi(x)$. Summing over a frame: $\mathrm{Ric}_{\widetilde M} = \mathrm{Ric}_M$ pulled back, so the same lower bound holds on $\widetilde M$.
> >
> > Completeness: a geodesic in $\widetilde M$ projects to a geodesic in $M$ (local isometry preserves geodesics); the projected geodesic extends for all time (by completeness of $M$); the unique lift of the extension is the extension of the original geodesic in $\widetilde M$. So $\widetilde M$ is geodesically complete.

> [!note]- Lemma 5: Compact cover of compact is finite-sheeted
> **Statement:** If $p : \widetilde M \to M$ is a covering map with both $\widetilde M$ and $M$ compact, then $p$ is finite-sheeted.
>
> **Hint:** Cover $M$ by finitely many evenly covered open sets; preimages are finite disjoint unions; total preimage is finitely many open sets, but if any fibre is infinite then so is the corresponding open subset of $\widetilde M$.
>
> **Why needed:** Yields finite $\pi_1$.
>
> > [!note]- Full proof
> > $M$ compact, so there is a finite open cover $M = U_1 \cup \cdots \cup U_k$ by evenly covered open sets. The preimage $\widetilde M = \bigsqcup_{i, \alpha} \widetilde U_{i, \alpha}$ where $\widetilde U_{i, \alpha}$ are the sheets above $U_i$. If the cover were infinite-sheeted, at least one $U_i$ would have infinitely many sheets above it (since the sheet number is constant on each connected component of $M$, and $M$ is connected). Pick that $U_i$. Pick a point $p \in U_i$. The infinitely many points of $p^{-1}(p) \subseteq \widetilde M$ lie in infinitely many *disjoint* sheets, each a copy of $U_i$. These disjoint copies are infinitely many disjoint open sets in $\widetilde M$, with no finite subcover that includes any one of them — contradiction to compactness of $\widetilde M$. So the cover is finite-sheeted.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $M^n$ be a complete connected Riemannian manifold with $\mathrm{Ric} \geq (n-1)\kappa > 0$. Then $\mathrm{diam}(M) \leq \pi/\sqrt{\kappa}$, $M$ is compact, and $\pi_1(M)$ is finite.
>
> *Proof.*
>
> **Step 0:** $M$ complete, connected; $\mathrm{Ric} \geq (n-1)\kappa > 0$.
>
> **Step 1 (diameter).** Lemma 2 gives $\mathrm{diam}(M) \leq \pi/\sqrt{\kappa}$.
>
> **Step 2 (compactness).** Lemma 3 gives $M$ compact.
>
> **Step 3 (universal cover).** Lemma 4 gives the universal cover $\widetilde M$ a Riemannian metric with the same Ricci bound, and $\widetilde M$ is complete.
>
> **Step 4 ($\widetilde M$ compact).** Apply Steps 1–2 to $\widetilde M$: it has finite diameter and is compact.
>
> **Step 5 (finite sheets).** Lemma 5 gives $\pi : \widetilde M \to M$ finite-sheeted. The number of sheets equals $|\pi_1(M)|$ (universal cover property), so $|\pi_1(M)|$ is finite.
>
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**General relativity: Hawking singularity theorems.** In Lorentzian signature, the analogous theorem replaces "geodesic completeness" with "timelike geodesic completeness" and Ricci with the relevant Lorentzian quantity ($\mathrm{Ric}(T, T) \geq 0$ for timelike $T$ is the **strong energy condition**). The conclusion is: spacetime is timelike geodesically *in*complete — there is a singularity. This is one of the **Hawking singularity theorems** (1965), and it predicts the inevitability of singularities in collapsing matter (black holes) and in cosmological contraction. Frankel discusses this in §21.3.

**Optimal transport: Bakry-Émery Ricci curvature.** Lott-Villani and Sturm extended the notion of "Ricci lower bound" to metric measure spaces, defining the $\mathrm{Ric} \geq K$ condition via convexity of entropy along optimal transport plans. The Myers-type theorem extends: $\mathrm{Ric} \geq K > 0$ on a metric measure space implies compactness and diameter bound. This is the framework for **Ricci-curvature on non-smooth spaces** (Alexandrov spaces, fractals, weighted manifolds).

**Lie group theory: Weyl's theorem on $\pi_1$ of compact semisimple groups.** A compact connected Lie group $G$ with bi-invariant metric and trivial centre algebra has positive Ricci (Frankel 21.24 / Weyl 21.13 strengthened); by Myers, $\pi_1(G)$ is finite. Examples: $\pi_1(\mathrm{SO}(n)) = \mathbb{Z}/2$ for $n \geq 3$ is finite; same for $\pi_1(\mathrm{SU}(n)) = 0$, $\pi_1(\mathrm{Sp}(n)) = 0$, etc. So Myers gives a uniform proof that compact semisimple Lie groups have finite $\pi_1$.

**Bochner technique: positive Ricci implies $b_1 = 0$.** Bochner's theorem (1946) states that on a closed Riemannian manifold with $\mathrm{Ric} \geq 0$, every harmonic 1-form is parallel; if $\mathrm{Ric} > 0$ somewhere, then $b_1 = 0$ (no harmonic 1-forms). Myers is *stronger* than Bochner: it gives finite $\pi_1$, which implies $b_1 = \mathrm{rk}(H_1(M; \mathbb{Q})) = \mathrm{rk}(\pi_1^{\mathrm{ab}} \otimes \mathbb{Q}) = 0$ (finite group has zero rational rank), recovering Bochner. The advantage of Myers: it doesn't require compactness as hypothesis (it derives it), and the conclusion ($\pi_1$ finite) is much stronger than $b_1 = 0$. See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

---

# Bridges

- **[[Riemannian Geometry III — Riemann Curvature and Topology]]** — the natural home of Myers' theorem in the Riemannian-geometry batch. The full proof of the second variation formula and Hopf-Rinow theorem live there; this page focuses on the $\pi_1$ consequence. The companion theorems Synge's (sectional curvature) and Cartan-Hadamard (non-positive curvature) are also in [[Riemannian Geometry III — Riemann Curvature and Topology]].

- **Hopf-Rinow theorem** — the *crucial* input. Hopf-Rinow has multiple equivalent forms (geodesic completeness ↔ closed balls compact ↔ every two points joined by length-minimising geodesic), and Myers uses two of them: geodesic completeness implies points joined by minimising geodesics (gives diameter bound), and closed balls compact upgrades bounded to compact. Without Hopf-Rinow, Myers fails.

- **[[Def - Universal Cover]]** — the universal cover is the bridge from "diameter of $M$" to "$\pi_1(M)$ finite." The metric lifts to $\widetilde M$; the Ricci bound transports; Myers applied to $\widetilde M$ gives $\widetilde M$ compact; then the sheet count is finite. This is the standard pattern: prove a metric property on $M$, lift to $\widetilde M$, deduce a $\pi_1$ statement.

- **Synge's theorem** — the partner result. Synge says: closed Riemannian manifold + even-dimensional + orientable + sectional curvature $> 0$ implies *simply* connected (not just finite $\pi_1$). Synge's hypothesis is stronger (sectional, not Ricci; orientable; even-dim), conclusion is stronger ($\pi_1 = 0$, not just finite). Myers and Synge together are the standard positive-curvature theorems. See [[Riemannian Geometry III — Riemann Curvature and Topology]].

- **Bochner's theorem** — implied by Myers. Bochner: $\mathrm{Ric} \geq 0$ + compact → harmonic 1-forms are parallel; if strict somewhere, $b_1 = 0$. Myers gives much more: $\mathrm{Ric}$ bounded away from 0 → compact + $\pi_1$ finite → $b_1 = 0$ automatically (since $H_1$ is finite-rank torsion). See [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

- **Hawking singularity theorems** — the Lorentzian-signature analogue. Replace "Riemannian Ricci $\geq (n-1)\kappa$" with "timelike Ricci $\geq 0$" (strong energy condition); the second variation argument analogously forces conjugate points along long timelike geodesics. Conclusion: the spacetime is geodesically incomplete (singularity exists). The mathematical structure is Myers-like, but the physical interpretation is reversed: instead of compactness, the theorem predicts the breakdown of geodesic completeness. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
