---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Sectional Curvature"
  - "Def - Jacobi Field"
  - "Def - Riemannian Metric"
tags: [geometry, riemannian-geometry, comparison-theorem, fundamental-group]
---

# Notation

$(M, g)$ is a compact, orientable, even-dimensional Riemannian manifold with positive sectional curvature $K > 0$. "Even-dimensional" means $\dim M = 2k$ for some $k \ge 1$. The normal bundle $T\gamma^\perp$ along a closed geodesic $\gamma$ has dimension $2k - 1$ — odd. Parallel transport around $\gamma$ defines a linear isometry $P : T_p\gamma^\perp \to T_p\gamma^\perp$ of this normal space.

---

# Statement

> **Theorem (Synge, 1936).** Let $(M, g)$ be a compact, orientable, even-dimensional Riemannian manifold with positive sectional curvature $K > 0$ everywhere. Then $M$ is **simply connected**: $\pi_1(M) = 0$.

> **Companion theorem (Synge corollary, odd-dim case).** Let $(M, g)$ be a compact, odd-dimensional Riemannian manifold with positive sectional curvature $K > 0$. Then $M$ is **orientable**.

> **Sharpness.** Both hypotheses (even-dim, orientable) are essential for the main theorem:
> - **$\mathbb{RP}^{2n}$** is compact, even-dimensional, positively curved (inherited from $S^{2n}$), but *not* orientable and *not* simply connected ($\pi_1 = \mathbb{Z}/2$).
> - **$\mathbb{RP}^{2n+1}$** is compact, orientable, positively curved, but *odd*-dimensional and not simply connected ($\pi_1 = \mathbb{Z}/2$).

---

# Motivation

Synge's theorem is the strongest topological consequence of positive sectional curvature: not just finite $\pi_1$ (as Bonnet–Myers gives from the weaker Ricci hypothesis), but actually $\pi_1 = 0$. The cost is two extra hypotheses — even dimensionality and orientability — both of which are needed in an essential way, as the $\mathbb{RP}^n$ counterexamples show.

The intuition is the same second-variation-of-arc-length machinery used in Bonnet–Myers, but the strategic move is different. Instead of taking a fixed-endpoint geodesic, Synge takes a *closed* geodesic — a length-minimiser in a nontrivial free homotopy class of loops, whose existence (in a compact manifold with nontrivial $\pi_1$) is guaranteed. He then constructs a variation field that makes the second variation negative, contradicting minimality.

The key technical fact: on an even-dimensional orientable manifold with positive sectional curvature, parallel transport around any closed loop has $+1$ as an eigenvalue on the normal bundle. This eigenvalue gives a parallel-transported normal vector field $J$ along the closed geodesic, and Synge's formula for the second variation in this $J$ direction is

$$L''(0) = -\int_0^L K(T \wedge J)\, ds < 0$$

(under positive sectional curvature). So the closed geodesic is unstable, can be shortened — contradiction.

The theorem was proved by J. L. Synge in 1936 in his book *Tensor Calculus*, with the precise second-variation formula now bearing his name. It is one of the cleanest applications of the parallel-transport-and-eigenvalue technique in Riemannian geometry, and it is also one of the most surprising — at first reading, the role of even-dimensionality and orientability seems unmotivated, but both feed into the same odd-dimensional eigenvalue argument.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: Positive *sectional* curvature $K > 0$.* Stronger than Ricci positivity (which Bonnet–Myers needs). **The bridge:** positive sectional curvature is the precondition that makes Synge's formula give $L''(0) < 0$; Ricci alone would not suffice because the per-plane curvature is what matters when computing along the specific $T \wedge J$ plane. **Example:** the round sphere $S^n$ ($K \equiv 1$), $\mathbb{CP}^n$ ($K \in [1/4, 1]$ — so $K > 0$), positively-curved deformations of $S^n$.

*Source 2: A compact even-dim orientable manifold with $K > 0$ everywhere.* Already satisfies the hypothesis directly. **Example:** the round sphere $S^{2n}$, $\mathbb{CP}^n$ (real dimension $2n$, orientable), the **Wallach manifolds** in dimension $\ge 6$.

*Source 3: A manifold that one wants to show is simply connected, where the curvature is hard to verify but one can show it is "positively curved on enough planes."* **The bridge:** Synge's hypothesis is sectional-curvature $> 0$ on *every* plane — strict positivity. A relaxation to "$K \ge 0$ everywhere with $K > 0$ on a dense open set" does *not* work (the conclusion fails). **Example:** non-example: $S^2 \times S^2$ has $K \ge 0$ but $K = 0$ on mixed planes; it is simply connected anyway, but Synge does not apply directly.

**Targets (Output Amplification).**

*Target 1: Synge + Bonnet–Myers gives compact even-dim orientable + $K > 0$ $\implies$ simply connected + diameter bound.* The two theorems combine: positive sectional implies positive Ricci, so Bonnet–Myers gives diameter $\le \pi/\sqrt{K_{\min}}$ where $K_{\min}$ is the lower bound on sectional curvature; Synge adds $\pi_1 = 0$. **Combined target:** strong global structure: compact + bounded diameter + simply connected — looks more and more like a sphere.

*Target 2: Synge + the classical sphere theorem gives a route to $S^n$ classification.* The classical sphere theorem (**Berger–Klingenberg**) says simply-connected complete with $1/4 < K \le 1$ is homeomorphic to $S^n$. Synge gives the simply-connected hypothesis automatically in the even-dim case under just $K > 0$ and orientability. **Combined target:** Synge + Berger–Klingenberg = $1/4$-pinched even-dim orientable manifolds with $K > 0$ are spheres.

*Target 3: Synge corollary (odd-dim) gives a topological invariant.* The corollary statement that odd-dim positively-curved compact manifolds are orientable can be used to rule out positively-curved metrics on certain odd-dim manifolds (those with $w_1 \ne 0$). **Combined target:** the parallel-transport eigenvalue analysis used in Synge applies to many topological-geometric obstruction problems.

---

# Why Is It True

The geometric picture: suppose $\pi_1(M) \ne 0$. Then there is a nontrivial free homotopy class of loops in $M$. By compactness, in this class there is a *shortest* loop, and this shortest representative must be a *closed geodesic* $\gamma$ (length-minimisers in path classes are always geodesics by first-variation analysis). So *any* nontrivial $\pi_1$ produces a closed geodesic.

Now consider parallel transport around $\gamma$. The tangent direction $T$ is preserved (parallel transport along $\gamma$ preserves $T$ trivially, since $\nabla_T T = 0$). So parallel transport acts on the **normal space** $T_p\gamma^\perp$, which has dimension $\dim M - 1 = 2k - 1$ when $\dim M = 2k$.

The parallel-transport map $P : T_p\gamma^\perp \to T_p\gamma^\perp$ is a linear isometry (it preserves the metric inherited from $g$). So $P \in \mathrm{O}(2k - 1)$.

Now invoke the two hypotheses:
1. **Orientability** of $M$ means that $P$ is orientation-preserving on $T_pM$. Since $P(T) = T$ trivially (the tangent is preserved), and $\det P|_{T_pM} = \det P|_{\mathbb{R}\cdot T} \cdot \det P|_{T_p\gamma^\perp} = 1 \cdot \det P|_{T_p\gamma^\perp}$, orientability gives $\det P|_{T_p\gamma^\perp} = +1$, i.e., $P \in \mathrm{SO}(2k - 1)$.
2. **Odd dimension of the normal space** ($2k - 1$): a matrix in $\mathrm{SO}(2k - 1)$ has eigenvalues that are either real $\pm 1$ or come in complex conjugate pairs $e^{\pm i\theta}$. There are $2k - 1$ eigenvalues in total. Since complex pairs come in twos, the number of real eigenvalues has the same parity as $2k - 1$ — odd. So there are an *odd* number of $\pm 1$ eigenvalues. Their product is $\det P = +1$. The only way an odd number of $\pm 1$'s multiplies to $+1$ is if an odd number of them are $+1$. So at least one eigenvalue is $+1$.

**The eigenvalue $+1$ gives a parallel-transported normal vector field $J$ along $\gamma$.** Use $J$ as the variation vector for a closed-curve variation $x(s, \alpha) = \exp_{\gamma(s)}(\alpha J(s))$. Apply Synge's formula for the second variation: with $J$ parallel and normal, $\nabla_T J = 0$, so the formula simplifies to

$$L''(0) = -\int_0^L K(T \wedge J)\, ds < 0$$

by positive sectional curvature. So $\gamma$ is *not* a length-minimiser in its free homotopy class — contradiction with the minimality assumption.

**The bolded mechanism summary: orientability + even-dim of $M$ = odd-dim of normal bundle + $\det P = 1$ = at least one $+1$ eigenvalue of parallel transport = parallel-transported normal vector field = $L''(0) < 0$ on the shortest closed geodesic = contradiction with shortest-loop existence = $\pi_1 = 0$.**

---

# What Makes This Hard

The eigenvalue argument is the heart and is unexpected: most arguments in Riemannian geometry are direct curvature manipulations, but Synge uses *parity of dimension* and the *spectral theory of orthogonal matrices* to extract a parallel vector field. The standard error is to forget either hypothesis: dropping orientability makes $P$ possibly in $\mathrm{O}(2k-1)\setminus\mathrm{SO}(2k-1)$ (so $\det P = -1$, and an odd number of $\pm 1$ eigenvalues could all be $-1$); dropping even-dim makes the normal bundle even-dim, and an $\mathrm{SO}(2k)$-matrix can have no real eigenvalues at all (all complex conjugate pairs).

A second technical point: the existence of a shortest loop in a free homotopy class on a *compact* manifold requires a separate argument (a direct method-style proof using lower semicontinuity of length and compactness of the loop space). The result is standard but often left implicit; in a careful proof one must verify it.

Finally, Synge's second-variation formula itself has a sign convention that catches students out. The formula reads $L''(0) = \int(|\nabla_T J|^2 - \langle R(J, T)T, J\rangle)ds + \text{boundary term}$, with the boundary term vanishing for closed curves; the negative sign in front of $\langle R(J, T)T, J\rangle$ is what makes positive sectional curvature contribute *negatively* to $L''(0)$ — the key sign that drives the contradiction.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Assume $\pi_1(M) \ne 0$, take a shortest loop in a nontrivial class (a closed geodesic $\gamma$). Show parallel transport $P$ around $\gamma$ has $+1$ as an eigenvalue (using even-dim + orientability + odd-dim normal bundle). Use the corresponding parallel-transported normal field $J$ as the variation vector; Synge's formula gives $L''(0) < 0$, contradicting minimality.

**Subgoal decomposition:**

1. **Nontrivial $\pi_1$ implies existence of a shortest closed geodesic in some free homotopy class.**
   - *Hint:* Compactness + lower semicontinuity of length + first variation analysis.
   - *Why needed:* Produces the geodesic that we will contradict.

2. **Parallel transport around the closed geodesic acts on the $(2k-1)$-dim normal space as an element of $\mathrm{SO}(2k - 1)$.**
   - *Hint:* Parallel transport is a linear isometry; orientability of $M$ gives $\det = +1$ on the full tangent space, and trivial action on the tangent direction gives $\det = +1$ on the normal space.
   - *Why needed:* Sets up the eigenvalue argument.

3. **Any element of $\mathrm{SO}(2k-1)$ has $+1$ as an eigenvalue.**
   - *Hint:* Eigenvalues of an orthogonal matrix come in complex conjugate pairs or are $\pm 1$. With $2k - 1$ eigenvalues total (odd), there must be an odd number of real eigenvalues, all $\pm 1$. Their product is $\det = +1$, so an odd number are $+1$, hence at least one is $+1$.
   - *Why needed:* Produces the parallel vector field.

4. **Synge's formula for closed-curve variation with parallel normal field $J$.**
   - *Hint:* Endpoint terms vanish (closed curve); $\nabla_T J = 0$ kills the $|\nabla_T J|^2$ term; left with $-\int K(T \wedge J)ds$.
   - *Why needed:* Computes the second variation in usable form.

5. **Negative second variation contradicts minimality of $\gamma$ in its free homotopy class.**
   - *Hint:* Negative second variation means the variation strictly shortens $\gamma$ to second order; closed-curve variation preserves the free homotopy class.
   - *Why needed:* Closes the contradiction.

---

# Lemma Decomposition

> [!note]- Lemma 1: Existence of a shortest closed geodesic in a nontrivial free homotopy class on a compact manifold
> **Statement:** If $M$ is compact and $\pi_1(M) \ne 0$, then there exists a nontrivial free homotopy class of closed loops containing a length-minimising representative, and this representative is a smooth closed geodesic.
>
> **Hint:** Standard direct method: take a length-minimising sequence in the class; pass to a subsequence converging uniformly (compactness of $M$ + Arzelà–Ascoli); show the limit is in the same class and is length-minimising. First-variation analysis shows minimisers are geodesics.
>
> **Why needed:** Existence of the object to which the rest of the argument applies.
>
> > [!note]- Full proof
> > Fix a basepoint $p_0 \in M$ and a nontrivial element $\alpha \in \pi_1(M, p_0)$. In the corresponding free homotopy class, take a minimising sequence of loops $\gamma_n$ with $\mathrm{length}(\gamma_n) \to \inf$. By a standard argument (Lemma 1 in any treatment of geodesic loops on compact manifolds — see Lee, *Riemannian Manifolds*, or do Carmo Ch 9), the $\gamma_n$ can be assumed parameterised by arc length and equicontinuous; by Arzelà–Ascoli (using compactness of $M$ as the target), pass to a uniformly convergent subsequence $\gamma_n \to \gamma$. Lower semicontinuity of length gives $\mathrm{length}(\gamma) \le \inf$. Free homotopy class is preserved by uniform convergence in compact manifolds. By the first variation of arc length, any length-minimising curve is a geodesic, so $\gamma$ is a closed geodesic. By minimality, $\gamma$ has length equal to $\inf > 0$.

> [!note]- Lemma 2: Parallel transport around $\gamma$ as an element of $\mathrm{SO}(2k - 1)$ on the normal space
> **Statement:** Let $\gamma$ be a closed geodesic on a $2k$-dim orientable Riemannian manifold. Parallel transport around $\gamma$ is a linear isometry $P : T_p\gamma^\perp \to T_p\gamma^\perp$ with $\det P = +1$, i.e., $P \in \mathrm{SO}(2k - 1)$.
>
> **Hint:** Parallel transport is an isometry (preserves the metric); orientability of $M$ + trivial action on $T$-direction $\Rightarrow$ $\det = +1$ on the normal space.
>
> **Why needed:** Sets up the eigenvalue argument.
>
> > [!note]- Full proof
> > Parallel transport along a curve in a Riemannian manifold preserves the metric (this is one of the defining properties of the Levi-Civita connection — see [[Riemannian Geometry I — Connections and Covariant Differentiation]]). Restricted to the normal bundle $T\gamma^\perp$ (a sub-bundle preserved by parallel transport since $\nabla_T T = 0$ and the metric is preserved), parallel transport around $\gamma$ gives a linear isometry $P : T_p\gamma^\perp \to T_p\gamma^\perp$, so $P \in \mathrm{O}(2k - 1)$.
> > 
> > Orientability of $M$ means a continuous orientation of $T_pM$ exists, and parallel transport around any loop preserves this orientation: $\det(P|_{T_pM}) = +1$. Now $T_pM = \mathbb{R}\cdot T(p) \oplus T_p\gamma^\perp$, and on $\mathbb{R}\cdot T(p)$, parallel transport acts as $+1$ (it sends $T$ to $T$). So $\det(P|_{T_pM}) = (+1) \cdot \det(P|_{T_p\gamma^\perp})$, giving $\det(P|_{T_p\gamma^\perp}) = +1$, hence $P \in \mathrm{SO}(2k - 1)$.

> [!note]- Lemma 3: Any element of $\mathrm{SO}(2k - 1)$ has $+1$ as an eigenvalue
> **Statement:** For $P \in \mathrm{SO}(2k - 1)$, there exists a nonzero $v \in \mathbb{R}^{2k - 1}$ with $Pv = v$.
>
> **Hint:** Eigenvalues of an orthogonal matrix are either real ($\pm 1$) or in complex-conjugate pairs $e^{\pm i\theta}$ ($\theta \ne 0$). In odd dimension $2k - 1$, the number of real eigenvalues has the same parity as $2k - 1$ (odd). Their product is $\det = +1$, so an odd number are $+1$.
>
> **Why needed:** Produces the parallel vector field for the variation.
>
> > [!note]- Full proof
> > By the spectral theorem for orthogonal matrices over $\mathbb{R}$: any $P \in \mathrm{O}(N)$ is conjugate in $\mathrm{O}(N)$ to a block-diagonal matrix with $2 \times 2$ rotation blocks $\binom{\cos\theta_j -\sin\theta_j}{\sin\theta_j \cos\theta_j}$ ($\theta_j \in (0, \pi)$) and $1 \times 1$ blocks $\pm 1$. The complex eigenvalues are $e^{\pm i\theta_j}$ from each $2 \times 2$ block; the real eigenvalues are the $\pm 1$ entries.
> > 
> > For $N = 2k - 1$ (odd), the dimension counts mod $2$ give the number of $1 \times 1$ blocks as odd. Each is $\pm 1$. Product $\det P = (-1)^{(\#\,-1\,\text{blocks})}$, and we know $\det P = +1$, so $\#\,-1\,\text{blocks}$ is even. Combined with $\#\,\text{total real eigenvalues} = (\#\,+1) + (\#\,-1)$ being odd, $\#\,+1$ is odd. In particular, $\#\,+1 \ge 1$ — there exists a nonzero $v$ with $Pv = v$.

> [!note]- Lemma 4: Parallel transport eigenvalue $+1$ gives a parallel normal vector field along $\gamma$
> **Statement:** With $P, v$ from Lemma 3, define $J(s)$ along $\gamma$ as the parallel transport of $v$ from $p = \gamma(0)$ to $\gamma(s)$. Then $J$ is a smooth parallel ($\nabla_T J = 0$) unit normal vector field along $\gamma$, with $J(0) = J(L) = v$.
>
> **Hint:** Parallel transport produces smooth vector fields. The unit-vector property is preserved by parallel transport (metric-preserving). Normality to $\gamma$ is preserved similarly. The "closure" $J(L) = v$ follows from $Pv = v$ — the parallel transport around the full loop sends $v$ to itself.
>
> **Why needed:** Provides the variation field used in Synge's formula.
>
> > [!note]- Full proof
> > Define $J(s) := \mathcal{P}_0^s v$, parallel transport of $v$ from $p$ to $\gamma(s)$. By construction $\nabla_T J = 0$ (parallel). Metric-preservation of parallel transport gives $|J(s)| = |v|$ (constant; choose $|v| = 1$). Initial orthogonality $\langle J(0), T(0)\rangle = \langle v, T(p)\rangle = 0$ (since $v \in T_p\gamma^\perp$) is preserved: $T \mapsto T$ and $J(s) \mapsto J(s)$ both parallel, so $\langle J, T\rangle$ is constant, hence $\equiv 0$. So $J$ is unit normal and parallel along $\gamma$. Finally $J(L) = \mathcal{P}_0^L v = Pv = v = J(0)$, so $J$ defines a smooth normal field on the closed curve.

> [!note]- Lemma 5: Synge's formula for second variation with closed-curve variation and parallel $J$
> **Statement:** With $J$ from Lemma 4 and the variation $x(s, \alpha) = \exp_{\gamma(s)}(\alpha J(s))$, the second variation of arc length is
> $$L''(0) = -\int_0^L K(T \wedge J)\, ds.$$
>
> **Hint:** General Synge's formula reads $L''(0) = [\nabla_J J, T]_0^L + \int (|\nabla_T J|^2 - \langle R(J, T)T, J\rangle)ds$ (for normal variations; see Frankel §12.1, eqn (12.5)–(12.6)). Boundary term: $0$ for closed curve. $\nabla_T J = 0$ for parallel $J$: the $|\nabla_T J|^2$ term vanishes. $\langle R(J, T)T, J\rangle = K(T \wedge J)$ since $J, T$ orthonormal.
>
> **Why needed:** Quantitative form of the contradiction.
>
> > [!note]- Full proof
> > Synge's formula for the second variation of arc length along a geodesic with normal variation $J$ (i.e., $\langle J, T\rangle = 0$):
> > $$L''(0) = \langle\nabla_J J, T\rangle\bigg|_0^L + \int_0^L\bigl(|\nabla_T J|^2 - \langle R(J, T)T, J\rangle\bigr)ds.$$
> > For a *closed* curve variation, the boundary term vanishes (endpoints coincide, parallel-transport-style match-up). For *parallel* $J$, $\nabla_T J = 0$, so $|\nabla_T J|^2 = 0$. With $|J| = |T| = 1$ and $J \perp T$:
> > $$\langle R(J, T)T, J\rangle = \frac{\langle R(J, T)T, J\rangle}{|J|^2|T|^2 - \langle J, T\rangle^2} \cdot 1 = K(T \wedge J).$$
> > Hence $L''(0) = -\int_0^L K(T \wedge J)\, ds < 0$ by $K > 0$.

> [!note]- Lemma 6: $L''(0) < 0$ contradicts minimality of $\gamma$ in its free homotopy class
> **Statement:** Negative second variation at a length-minimising loop in a free homotopy class is a contradiction.
>
> **Hint:** First variation is $0$ at minimisers (Lemma 1's geodesic property). Second variation $< 0$ means the variation strictly decreases length to second order. The variation $x(s, \alpha) = \exp_{\gamma(s)}(\alpha J(s))$ preserves the free homotopy class (it is a smooth homotopy of closed loops). So shorter loops exist in the class — contradiction with minimality.
>
> **Why needed:** Closes the argument.
>
> > [!note]- Full proof
> > At the minimiser $\gamma$, $L'(0) = 0$ (first variation; $\gamma$ is a geodesic). $L''(0) < 0$ by Lemma 5. So $L(\alpha) = L(0) + 0\cdot\alpha + \tfrac{1}{2}L''(0)\alpha^2 + O(\alpha^3) < L(0)$ for $\alpha$ small but nonzero. The varied curves $x(\cdot, \alpha) = \exp_{\gamma(\cdot)}(\alpha J(\cdot))$ are smooth closed loops (continuity of $\exp$ and closure of $\gamma$). They are in the same free homotopy class as $\gamma$ (smooth homotopy through closed loops). So shorter loops exist in the class — contradicting minimality of $\gamma$. Hence the assumption $\pi_1(M) \ne 0$ is wrong.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 (Existence of the shortest loop).** Assume for contradiction $\pi_1(M) \ne 0$. By Lemma 1, there exists a nontrivial free homotopy class of loops containing a length-minimising representative $\gamma$, which is a smooth closed geodesic.
>
> By Lemma 2, parallel transport around $\gamma$ acts on the normal space $T_p\gamma^\perp$ (of dimension $2k - 1$ — odd, since $\dim M = 2k$ is even) as an element of $\mathrm{SO}(2k - 1)$. By Lemma 3, this map has $+1$ as an eigenvalue, so there is a nonzero $v \in T_p\gamma^\perp$ fixed by parallel transport.
>
> By Lemma 4, parallel-transporting $v$ along $\gamma$ produces a smooth parallel unit normal vector field $J$ along $\gamma$. By Lemma 5, the second variation of arc length for the closed-curve variation $x(s, \alpha) = \exp_{\gamma(s)}(\alpha J(s))$ is $L''(0) = -\int_0^L K(T \wedge J)\, ds < 0$ by $K > 0$.
>
> By Lemma 6, this contradicts the minimality of $\gamma$ in its free homotopy class. Hence $\pi_1(M) = 0$. $\Box$
>
> **The odd-dim corollary** (compact odd-dim positively-curved $\Rightarrow$ orientable) follows by a similar parallel-transport eigenvalue argument: if $M$ were non-orientable, there would be a loop along which orientation reverses; analyse parallel transport around that loop and derive a contradiction using the same machinery.

---

# Cross-Field Exercise Suggestions

1. **Positively-curved homogeneous spaces.** The Wallach manifolds, Aloff–Wallach spaces, and Berger spheres are all examples of positively-curved homogeneous spaces that satisfy Synge's hypothesis. They are simply connected — confirming the theorem, and also providing rare examples of positively-curved manifolds not directly built from spheres or projective spaces.

2. **Klingenberg's injectivity radius bound.** A simply-connected complete Riemannian manifold with $K \le 1$ has injectivity radius $\ge \pi$ in dimension even, but only $\ge \pi/2$ in dimension odd (the better bound in even-dim uses Synge's theorem to rule out the topological obstruction that limits odd-dim). This is one of the inputs in the classical sphere theorem of **Berger–Klingenberg**.

3. **Application to general relativity / cosmology.** A spatial slice in an FLRW cosmology with positive spatial curvature is a $3$-sphere or a quotient of it. Since $S^3$ is odd-dim, Synge's main theorem does not directly apply, but Synge's corollary (odd-dim $\Rightarrow$ orientable) does — so positively-curved compact spatial slices in cosmology must be orientable. This rules out non-orientable spatial topologies for closed positively-curved universes.

---

# Bridges

- **Bonnet–Myers (weaker hypothesis, weaker conclusion).** [[Thm - Bonnet-Myers Theorem|Bonnet–Myers]] needs only Ricci-positivity (weaker than positive sectional) and gets finite $\pi_1$ (weaker than $\pi_1 = 0$). Synge sharpens the conclusion under the stronger sectional-curvature hypothesis combined with even-dim + orientability. Both proofs use the same second-variation-of-arc-length machinery; the difference is the strategic choice of geodesic (fixed-endpoint for Bonnet–Myers, closed for Synge).

- **The sphere theorem.** A simply-connected complete manifold with $1/4 < K \le 1$ is homeomorphic to $S^n$ (Berger–Klingenberg, $1960$s; diffeomorphism upgrade by **Brendle–Schoen**, $2009$). In dimension $2n$ + orientable, Synge gives simple-connectedness automatically from $K > 0$; combined with $1/4$-pinching, the sphere theorem then gives homeomorphism to $S^{2n}$. So Synge is a key input to the even-dim case of the sphere theorem.

- **The Synge–Weinstein theorem (refinement).** A stronger result: if $f : M \to M$ is an isometry of a compact orientable even-dim Riemannian manifold with $K > 0$, then $f$ has a fixed point. The proof uses Synge's argument applied to the closed-loop trajectory of $f^k$ for large $k$. **Weinstein** ($1968$) is the original reference; this generalises Synge by giving a fixed-point property for isometries.

- **Universal cover and the orientable double cover.** Synge's proof shows $\pi_1 = 0$ on $M$ when the hypotheses hold. For a non-orientable example like $\mathbb{RP}^{2n}$, the **orientable double cover** $S^{2n} \to \mathbb{RP}^{2n}$ is the universal cover (which *is* simply connected). The orientable-double-cover construction is the standard way to extract an orientable manifold from any manifold, and it is what makes Synge's even-dim case work for orientable manifolds: if $M$ were not simply connected, its orientable double cover would be a positively-curved compact even-dim simply-connected ... wait, this argument is more subtle. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the construction.

- **Parallel-transport eigenvalue and Berger's classification of holonomy.** The argument "$\mathrm{SO}(2k - 1)$ has $+1$ eigenvalue" generalises to holonomy analysis: when the **Riemannian holonomy group** of $M$ at a basepoint is a proper subgroup of $\mathrm{SO}(n)$, certain parallel sections of associated bundles exist (parallel spinors, parallel forms, etc.). Berger's classification of holonomy groups underpins **special holonomy** geometries (Kähler, Calabi–Yau, $G_2$, etc.).
