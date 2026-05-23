---
type: exercise
subject: spinors
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Lichnerowicz Formula"
  - "Def - Spin Connection and the Dirac Operator"
  - "Def - Spin Structure on a Manifold"
tags: [geometry, spinors, riemannian-geometry, index-theory]
---

# Problem Statement

Let $(M, g)$ be a closed Riemannian spin manifold with strictly positive scalar curvature, $R > 0$ everywhere. Prove the **Lichnerowicz vanishing theorem**: the kernel of the Dirac operator $\not D$ is zero, i.e., there are no nontrivial harmonic spinors on $M$.

Then, assuming the Atiyah–Singer index theorem $\mathrm{ind}\,\not D^+ = \int_M \hat A(M)$ for the chiral Dirac operator on a closed Riemannian spin manifold of even dimension, deduce the **$\hat A$-genus obstruction**: a closed spin manifold $M^{2k}$ admits a metric of positive scalar curvature only if $\hat A(M) = 0$.

Apply this to show that the **K3 surface** (a closed spin 4-manifold with $\hat A(K3) = 2$) does *not* admit any Riemannian metric of strictly positive scalar curvature.

**Recall:**

The Lichnerowicz formula:

![[Thm - Lichnerowicz Formula#Statement]]

The Atiyah–Singer index theorem in its spinor version (which we assume): for a closed Riemannian spin manifold $M^{2k}$, the analytical index of the chiral Dirac operator equals the integral of the $\hat A$-genus characteristic class:
$$\mathrm{ind}\,\not D^+ = \dim\ker\not D^+ - \dim\ker\not D^- = \int_M \hat A(M).$$
The $\hat A$-genus is a polynomial in the Pontryagin classes, computable from the curvature tensor. For the K3 surface, $\hat A(K3) = 2$.

---

# Convergent Strategy

**Problem class:** *Vanishing theorem for the kernel of an elliptic operator via the curvature term in a Bochner-Weitzenböck formula.* This is the prototypical example of a vanishing theorem: an operator whose square is a sum of (positive self-adjoint operator) + (curvature-coupled scalar) is forced to have trivial kernel when the curvature is positive.

**Assumption pattern:** Given (i) the Lichnerowicz formula $\not D^2 = \nabla^{S*}\nabla^S + R/4$, (ii) the assumption $R > 0$ everywhere on $M$, and (iii) the closedness of $M$ (so integration by parts is valid without boundary terms). Combining these via integration gives the vanishing.

**Theorem routing:** Apply the *integral form* of the Lichnerowicz formula: $\|\not D\psi\|^2 = \|\nabla^S\psi\|^2 + \int R|\psi|^2/4$. Both terms on the right are non-negative when $R \geq 0$; if $R > 0$, the second is strictly positive unless $\psi = 0$. So $\not D\psi = 0$ forces $\psi = 0$. Combined with the index theorem, the index $\mathrm{ind}\,\not D^+ = \dim\ker\not D^+ - \dim\ker\not D^- = 0$ when $R > 0$, hence $\int_M \hat A(M) = 0$.

**Key decision point:** The trickiest part is the *application*: the index theorem provides a topological invariant ($\hat A(M)$), and the Lichnerowicz vanishing gives a *geometric* condition (positive scalar curvature) under which this invariant must vanish. The contrapositive — if $\hat A(M) \neq 0$, then $M$ does not admit a positive-scalar-curvature metric — is a topological *obstruction*, and applying it to K3 (where $\hat A = 2 \neq 0$) gives a non-trivial result that is not accessible by elementary methods.

---

# Legal Operations Used

1. **Operation 7 from the topic page (lift the Levi-Civita connection to the spinor bundle):** The spin connection $\nabla^S$ is what makes the Lichnerowicz formula make sense — without it, "$\nabla^{S*}\nabla^S$" would be undefined.

2. **Operation 5 from the topic page (square the Dirac operator using the Clifford relation):** The Lichnerowicz formula is the curved-spacetime analog of $\not\partial^2 = \Box$ on flat space, with the additional $R/4$ curvature correction.

3. **Self-adjointness of $\not D$:** On a closed Riemannian manifold, $\not D$ is formally self-adjoint, so $\int\langle\not D\psi, \not D\psi\rangle = \int\langle\psi, \not D^2\psi\rangle$. This is what lets us "integrate the Lichnerowicz formula against $\psi$" to get the integral form.

---

# Hints

> [!note]- Hint 1
> Apply $\not D^2$ to $\psi$ using the Lichnerowicz formula: $\not D^2\psi = \nabla^{S*}\nabla^S\psi + (R/4)\psi$. Pair with $\psi$ and integrate: $\int\langle\psi, \not D^2\psi\rangle = \int\langle\psi, \nabla^{S*}\nabla^S\psi\rangle + \int (R/4)|\psi|^2$.

> [!note]- Hint 2
> Integration by parts on the first term (using closedness — no boundary): $\int\langle\psi, \nabla^{S*}\nabla^S\psi\rangle = \int\langle\nabla^S\psi, \nabla^S\psi\rangle = \|\nabla^S\psi\|^2 \geq 0$.
>
> Self-adjointness of $\not D$ on the left: $\int\langle\psi, \not D^2\psi\rangle = \int\langle\not D\psi, \not D\psi\rangle = \|\not D\psi\|^2$.

> [!note]- Hint 3
> So $\|\not D\psi\|^2 = \|\nabla^S\psi\|^2 + \int (R/4)|\psi|^2$. If $\not D\psi = 0$, the LHS is zero; both terms on the RHS are non-negative, so each must vanish. The second term $\int R|\psi|^2/4 = 0$, combined with $R > 0$ everywhere, forces $|\psi|^2 = 0$ everywhere, i.e., $\psi = 0$.

> [!note]- Hint 4
> For the index-theorem corollary: in even dimension, the Dirac operator splits as $\not D = \not D^+ + \not D^-$ via the chirality decomposition $SM = S^+ \oplus S^-$. The index $\mathrm{ind}\,\not D^+ = \dim\ker\not D^+ - \dim\ker\not D^-$. Since $\ker\not D = \ker\not D^+ \oplus \ker\not D^-$ (the chirality components are independent), and $\ker\not D = 0$ from positive scalar curvature, both kernels vanish: $\dim\ker\not D^\pm = 0$. So $\mathrm{ind}\,\not D^+ = 0$, hence $\hat A(M) = 0$.

> [!note]- Hint 5
> For the K3 application: K3 is a closed simply-connected complex surface (real dimension 4) with $c_1(K3) = 0$ and Euler characteristic $24$. The $\hat A$-genus is computed as $\hat A(M) = -p_1/24$ in real dimension 4; for K3, $p_1 = -48$, so $\hat A(K3) = 2$. Since $\hat A \neq 0$, K3 cannot admit a positive-scalar-curvature metric.

---

# Solution

The plan: integrate the Lichnerowicz formula against any harmonic spinor; conclude both the gradient norm and the curvature integral vanish; positive scalar curvature forces the spinor itself to vanish. The chiral decomposition then gives the index-theoretic obstruction, applied to K3.

**Step 1: The integral identity.**

For any spinor $\psi \in \Gamma(SM)$ on a closed Riemannian spin manifold:
$$\|\not D\psi\|^2_{L^2} = \|\nabla^S\psi\|^2_{L^2} + \tfrac{1}{4}\int_M R|\psi|^2 \, d\mathrm{vol}.$$

> [!note]- Derivation
> Apply the [[Thm - Lichnerowicz Formula|Lichnerowicz formula]] $\not D^2 = \nabla^{S*}\nabla^S + R/4$ to $\psi$:
> $$\not D^2\psi = \nabla^{S*}\nabla^S\psi + \tfrac{R}{4}\psi.$$
>
> Take the $L^2$ inner product with $\psi$:
> $$\langle\psi, \not D^2\psi\rangle_{L^2} = \langle\psi, \nabla^{S*}\nabla^S\psi\rangle_{L^2} + \tfrac{1}{4}\int_M R|\psi|^2.$$
>
> The LHS: by self-adjointness of $\not D$ on a closed manifold, $\langle\psi, \not D^2\psi\rangle = \langle\not D\psi, \not D\psi\rangle = \|\not D\psi\|^2$.
>
> The RHS first term: $\nabla^{S*}\nabla^S$ is by definition the adjoint of $\nabla^S$ followed by $\nabla^S$; on a closed manifold, $\langle\psi, \nabla^{S*}\nabla^S\psi\rangle = \langle\nabla^S\psi, \nabla^S\psi\rangle = \|\nabla^S\psi\|^2$ (integration by parts with no boundary).
>
> So $\|\not D\psi\|^2 = \|\nabla^S\psi\|^2 + \tfrac{1}{4}\int R|\psi|^2$.

**Step 2: Lichnerowicz vanishing.**

If $R > 0$ everywhere and $\psi$ is a harmonic spinor ($\not D\psi = 0$), then $\psi = 0$.

> [!note]- Derivation
> Suppose $\not D\psi = 0$. Then the LHS of the integral identity vanishes: $0 = \|\nabla^S\psi\|^2 + \tfrac{1}{4}\int R|\psi|^2$.
>
> Both terms on the RHS are non-negative: $\|\nabla^S\psi\|^2 \geq 0$ (norm squared); $\int R|\psi|^2 \geq 0$ if $R \geq 0$, and $> 0$ unless $|\psi|^2 = 0$ pointwise (when $R > 0$ everywhere).
>
> For the sum to be zero, both must be zero: $\nabla^S\psi = 0$ (parallel) and $\int R|\psi|^2 = 0$.
>
> When $R > 0$ everywhere (strict inequality), $\int R|\psi|^2 = 0$ forces $|\psi|^2 = 0$ pointwise, hence $\psi = 0$.

**Step 3: Index obstruction.**

On a closed Riemannian spin manifold $M^{2k}$ with $R > 0$, $\mathrm{ind}\,\not D^+ = 0$. By the Atiyah-Singer index theorem, $\int_M \hat A(M) = 0$.

> [!note]- Derivation
> The Dirac operator on an even-dimensional spin manifold splits as $\not D = \not D^+ + \not D^-$ via the chirality decomposition $SM = S^+ \oplus S^-$: $\not D^\pm: \Gamma(S^\pm) \to \Gamma(S^\mp)$. The kernel decomposes as $\ker\not D = \ker\not D^+ \oplus \ker\not D^-$.
>
> By Step 2, $\ker\not D = 0$ when $R > 0$. So $\ker\not D^+ = 0$ and $\ker\not D^- = 0$, hence $\mathrm{ind}\,\not D^+ = \dim\ker\not D^+ - \dim\ker\not D^- = 0$.
>
> By the Atiyah-Singer index theorem (assumed), $\mathrm{ind}\,\not D^+ = \int_M \hat A(M)$. Therefore $\int_M \hat A(M) = 0$.
>
> *Contrapositive:* if $\int_M \hat A(M) \neq 0$, then $M$ does *not* admit a metric of positive scalar curvature.

**Step 4: K3 surface application.**

The K3 surface has $\hat A(K3) = 2 \neq 0$. So K3 does not admit a metric of strictly positive scalar curvature.

> [!note]- Derivation
> *K3 is a closed Riemannian spin 4-manifold:* K3 is a closed, simply-connected complex surface with trivial canonical bundle ($c_1 = 0$). It is spin: $w_2 \equiv c_1 \pmod 2 = 0$. Riemannian metrics exist on any closed manifold (e.g., from any Riemannian metric on $\mathbb{R}^N$ via embedding).
>
> *$\hat A(K3) = 2$:* In real dimension 4, $\hat A(M) = -\tfrac{1}{24}p_1$, where $p_1 = p_1(TM)$ is the first Pontryagin class evaluated on the fundamental class. For K3, $p_1[K3] = -48$, so $\hat A[K3] = -(-48)/24 = 2$. (This computation uses $p_1 = c_1^2 - 2c_2$ for almost-complex surfaces, $c_1(K3) = 0$, $c_2(K3) = \chi(K3) = 24$, giving $p_1 = -48$.)
>
> *Conclusion:* Since $\hat A(K3) = 2 \neq 0$, by Step 3, K3 does not admit a Riemannian metric of strictly positive scalar curvature.
>
> **Historical note:** This result was proven by **Hitchin (1974)**, who used Lichnerowicz vanishing combined with the index theorem to derive the first topological obstructions to positive scalar curvature on spin manifolds. It was the first major application of Dirac-operator methods to differential topology.

> [!note]- Complete formal solution
> Let $(M, g)$ be a closed Riemannian spin manifold with $R > 0$ everywhere.
>
> *Lichnerowicz vanishing.* Apply the Lichnerowicz formula to $\not D^2\psi = \nabla^{S*}\nabla^S\psi + (R/4)\psi$, pair with $\psi$ and integrate:
> $$\|\not D\psi\|^2 = \|\nabla^S\psi\|^2 + \tfrac{1}{4}\int_M R|\psi|^2.$$
> If $\not D\psi = 0$, the LHS is zero. Both RHS terms are non-negative, so both vanish; $\int R|\psi|^2 = 0$ with $R > 0$ forces $\psi = 0$. So $\ker\not D = 0$.
>
> *Index obstruction.* On a closed even-dimensional spin manifold, $\not D$ splits as $\not D^\pm: \Gamma(S^\pm) \to \Gamma(S^\mp)$, with $\ker\not D = \ker\not D^+ \oplus \ker\not D^-$. From the vanishing, both kernels are zero, so $\mathrm{ind}\,\not D^+ = 0$. By Atiyah-Singer, $\mathrm{ind}\,\not D^+ = \int_M \hat A(M) = 0$.
>
> *K3 application.* K3 is a closed simply-connected complex surface (4-real-dimensional) with $c_1 = 0$, $c_2 = 24$, and $\hat A(K3) = -p_1/24 = -(c_1^2 - 2c_2)/24 = 2$. Since $\hat A(K3) = 2 \neq 0$, the contrapositive of the index obstruction gives: K3 does not admit a Riemannian metric of strictly positive scalar curvature.

---

# Key Takeaways

**The Bochner technique: positive curvature kills harmonic objects.** The Lichnerowicz formula $\not D^2 = \nabla^{S*}\nabla^S + R/4$ has the same structure as Bochner's formula for the Hodge Laplacian on $1$-forms: $\Delta = \nabla^*\nabla + \mathrm{Ric}$. Both fit the pattern "(connection Laplacian, positive) + (curvature term)", and both yield vanishing theorems when the curvature is positive: positive Ricci curvature kills harmonic $1$-forms (i.e., $H^1(M; \mathbb{R}) = 0$); positive scalar curvature kills harmonic spinors. The general framework is called the **Bochner technique**, and it is one of the most powerful methods in Riemannian geometry for connecting curvature to topology.

**Topological obstructions to positive scalar curvature come from the index theorem.** The chain of reasoning — Lichnerowicz vanishing implies index vanishing, index equals $\hat A$-genus by Atiyah-Singer, contrapositive gives $\hat A \neq 0 \implies$ no positive-scalar-curvature metric — provides a *topological* obstruction to a *geometric* property. This is the prototype for index-theoretic obstructions: every non-vanishing index of a natural elliptic operator obstructs some natural curvature positivity. The Hitchin result on K3 was the first major application; later work by Schoen-Yau, Gromov-Lawson, and many others extended the framework significantly. The **Gromov-Lawson-Rosenberg conjecture** asks for a complete topological characterisation of positive-scalar-curvature spin manifolds.

**The K3 example shows that simply-connected, low-dimensional manifolds can be deeply constrained by spin geometry.** K3 is one of the simplest closed simply-connected manifolds (along with $S^4$, $\mathbb{CP}^2$, etc.), but it harbors deep geometric structure: it admits a Calabi-Yau (Ricci-flat Kähler) metric, has $\hat A = 2$, and is the unique simply-connected closed 4-manifold admitting both a spin structure and a complex structure of zero first Chern class. The Hitchin result shows that despite K3 being "topologically simple", it cannot accommodate the most basic positive-curvature condition (positive scalar curvature) — the topological obstruction $\hat A = 2$ is rigid. This was one of the first hints that 4-dimensional spin geometry is profoundly different from 3-dimensional and higher-dimensional cases.
