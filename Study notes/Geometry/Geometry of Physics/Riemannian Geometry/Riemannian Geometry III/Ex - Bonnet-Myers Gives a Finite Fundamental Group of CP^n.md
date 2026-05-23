---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Thm - Bonnet-Myers Theorem"
  - "Def - Ricci Tensor"
  - "Def - Sectional Curvature"
tags: [geometry, riemannian-geometry, comparison-theorem, complex-projective-space]
---

# Problem Statement

The complex projective space $\mathbb{CP}^n$ with the **Fubini–Study metric** has sectional curvatures pinched in the interval $[1/4, 1]$ (with maximum $K = 1$ on holomorphic $2$-planes and minimum $K = 1/4$ on totally real $2$-planes).

(a) Compute a lower bound on the Ricci curvature of $\mathbb{CP}^n$ and apply [[Thm - Bonnet-Myers Theorem|Bonnet–Myers]] to deduce that $\pi_1(\mathbb{CP}^n)$ is finite.

(b) Strengthen the conclusion: using either the explicit covering-space structure of $\mathbb{CP}^n = S^{2n+1}/S^1$ (Hopf fibration), or by applying [[Thm - Synge's Theorem|Synge's theorem]] to the even-real-dimensional orientable $\mathbb{CP}^n$, show that in fact $\pi_1(\mathbb{CP}^n) = 0$ — the complex projective spaces are *simply connected*.

(c) Compute the diameter of $\mathbb{CP}^n$ from the Bonnet–Myers diameter bound and compare to the actual diameter $\pi/2$ (in our metric normalisation).

**Recall:**

$\mathbb{CP}^n = (\mathbb{C}^{n+1}\setminus\{0\})/\mathbb{C}^*$ is the space of complex lines through the origin in $\mathbb{C}^{n+1}$. The Fubini–Study metric is the unique (up to scaling) Hermitian metric on $\mathbb{CP}^n$ invariant under the action of $\mathrm{PU}(n+1) = \mathrm{U}(n+1)/\mathrm{U}(1)$. As a real Riemannian manifold, $\mathbb{CP}^n$ has real dimension $2n$.

The **Hopf fibration** $S^{2n+1} \to \mathbb{CP}^n$ is a principal $S^1$-bundle, with the $S^1$-fibres being the orbits of the diagonal $U(1)$-action on $\mathbb{C}^{n+1}\setminus\{0\}$.

[[Thm - Bonnet-Myers Theorem|Bonnet–Myers]]: complete + $\mathrm{Ric} \ge (n-1)\kappa g$ with $\kappa > 0$ $\implies$ $M$ compact, $\mathrm{diam} \le \pi/\sqrt{\kappa}$, $\pi_1(M)$ finite.

[[Thm - Synge's Theorem|Synge]]: compact + orientable + even-dim + $K > 0$ $\implies$ $\pi_1 = 0$.

---

# Convergent Strategy

**Problem class:** Apply a comparison theorem to a specific manifold to extract topological information. Three parts: (a) the Bonnet–Myers application via Ricci, (b) the strengthening via Synge or via the explicit cover, (c) a quantitative diameter comparison.

**Assumption pattern:** $\mathbb{CP}^n$ is a compact even-real-dimensional Kähler manifold with sectional curvatures pinched in $[1/4, 1]$. The lower bound on $K$ gives a lower bound on Ricci, triggering Bonnet–Myers. The even-real-dimensionality + orientability + positive sectional triggers Synge for the stronger conclusion. The Hopf-fibration structure $S^{2n+1} \to \mathbb{CP}^n$ gives a direct route to compute $\pi_1$.

**Theorem routing:** (a) Sectional bound $K \ge 1/4$ $\implies$ Ricci bound $\mathrm{Ric}(v, v) \ge (2n-1)\cdot(1/4)|v|^2$ (since Ricci is the sum of $2n - 1$ sectional curvatures transverse to $v$, each at least $1/4$). Apply Bonnet–Myers with $\kappa = 1/4$ and dimension $2n$. (b) Apply Synge with even-real-dim $2n$, orientability (Kähler implies orientable via the holomorphic volume form), and $K > 0$ (the lower bound $K \ge 1/4 > 0$). (c) Bonnet–Myers gives $\mathrm{diam}(\mathbb{CP}^n) \le \pi/\sqrt{1/4} = 2\pi$, much weaker than the actual $\pi/2$. The slack reflects that Ricci is much less than sectional curvature in this geometry.

**Key decision point:** Recognising that the *Ricci lower bound* needed for Bonnet–Myers is $(\dim_\mathbb{R} M - 1)\kappa$, with $\dim_\mathbb{R}\mathbb{CP}^n = 2n$, not $n$. The most common error in this exercise is confusing complex and real dimension. The relevant formula is: in an orthonormal frame of *real* dim $2n$, $\mathrm{Ric}(v, v) = \sum_{j \ne i}K(v \wedge e_j)$, summing over $2n - 1$ transverse directions.

---

# Legal Operations Used

1. **Operation 4 from the topic page (descend from $K$ to Ricci).** Use the lower bound $K \ge 1/4$ to bound $\mathrm{Ric}$ from below.

2. **Operation 6 from the topic page (lift to universal cover).** Use the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ to identify the universal cover explicitly and compute $\pi_1$.

3. **Apply Bonnet–Myers and Synge as black-box theorems.** These provide the topological conclusions from the curvature hypotheses.

---

# Hints

> [!note]- Hint 1
> Part (a): Use the Ricci lower bound from the sectional bound. The real dimension of $\mathbb{CP}^n$ is $2n$. For any unit vector $v \in T_p\mathbb{CP}^n$, $\mathrm{Ric}(v, v) = \sum_{j \ne i}K(v \wedge e_j)$ (sum over $2n - 1$ orthonormal vectors orthogonal to $v$); each summand is $\ge 1/4$. So $\mathrm{Ric}(v, v) \ge (2n - 1)/4$.

> [!note]- Hint 2
> Part (a) continued: Apply Bonnet–Myers with $\kappa = 1/4$ (so $(n - 1)\kappa = (2n - 1)/4$... wait, but the dim in Bonnet–Myers is the real dim $2n$, so the lower bound condition is $\mathrm{Ric} \ge (2n - 1)\kappa g$ for some $\kappa > 0$. With our bound $\mathrm{Ric} \ge (2n - 1)/4 \cdot g$, we have $\kappa = 1/4$). Conclude: $\mathbb{CP}^n$ is compact (already known), $\mathrm{diam} \le \pi/\sqrt{1/4} = 2\pi$, and $\pi_1(\mathbb{CP}^n)$ is finite.

> [!note]- Hint 3
> Part (b): To strengthen to $\pi_1 = 0$, two routes. **Route 1 (Synge):** $\mathbb{CP}^n$ is compact, orientable (Kähler with $\dim_\mathbb{C} = n$, real $2n$, orientable via the canonical line bundle), even-real-dimensional (real $2n$), and has $K > 0$ (since $K \ge 1/4 > 0$). Synge directly gives $\pi_1 = 0$. **Route 2 (covering space):** Use the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$. The total space $S^{2n+1}$ is simply connected for $n \ge 1$ (since $\pi_1(S^k) = 0$ for $k \ge 2$). The long exact sequence of the fibration $\pi_1(S^1) \to \pi_1(S^{2n+1}) \to \pi_1(\mathbb{CP}^n) \to \pi_0(S^1)$ becomes $\mathbb{Z} \to 0 \to \pi_1(\mathbb{CP}^n) \to 0$, so $\pi_1(\mathbb{CP}^n) = 0$ for $n \ge 1$.

> [!note]- Hint 4
> Part (c): Bonnet–Myers bound: $\mathrm{diam}(\mathbb{CP}^n) \le \pi/\sqrt{1/4} = 2\pi$. Actual diameter: with the Fubini–Study metric normalised so $K_{\max} = 1$, $\mathrm{diam} = \pi/2$. So the Bonnet–Myers bound $2\pi$ is much larger than the actual $\pi/2$ — a factor of $4$ larger. The reason: the Ricci-lower-bound used is from the minimum sectional curvature $1/4$, not the average or maximum. A tighter Ricci bound would give a sharper diameter bound. In fact, the **actual** Ricci of Fubini–Study $\mathbb{CP}^n$ is $\mathrm{Ric} = (2n+2)g$ (so Einstein with $\lambda = 2n + 2$); using this, $(2n - 1)\kappa = 2n + 2$ gives $\kappa = (2n+2)/(2n-1) > 1$, and the diameter bound is $\pi/\sqrt{(2n+2)/(2n-1)} < \pi$ — closer to but still not sharp.

---

# Solution

**Plan:** Three short calculations. (a) Use $K \ge 1/4$ to bound $\mathrm{Ric} \ge (2n - 1)/4 \cdot g$, apply Bonnet–Myers to get $\pi_1$ finite. (b) Apply Synge or use the Hopf fibration to upgrade finite $\pi_1$ to $\pi_1 = 0$. (c) Compare the Bonnet–Myers diameter bound to the actual diameter.

**Step 1: Lower bound on Ricci from the sectional bound.**

> [!note]- Derivation
> The real dimension of $\mathbb{CP}^n$ is $2n$. For a unit vector $v \in T_p\mathbb{CP}^n$, pick an orthonormal basis $\{v, e_1, \ldots, e_{2n-1}\}$ of $T_p\mathbb{CP}^n$. The Ricci curvature in the direction $v$ is
> $$\mathrm{Ric}(v, v) = \sum_{j=1}^{2n - 1}K(v \wedge e_j) \ge \sum_{j=1}^{2n-1}\tfrac{1}{4} = \tfrac{2n - 1}{4},$$
> using the hypothesis $K(\sigma) \ge 1/4$ on every $2$-plane.
>
> Therefore $\mathrm{Ric}(v, v) \ge \tfrac{2n-1}{4}|v|^2$ for all $v$, i.e., $\mathrm{Ric} \ge \tfrac{2n - 1}{4}g$.

**Step 2: Apply Bonnet–Myers.**

> [!note]- Derivation
> Bonnet–Myers in dim $2n$ requires $\mathrm{Ric} \ge (2n - 1)\kappa\, g$. With our bound, $\kappa = 1/4$. So $\mathbb{CP}^n$ is compact (known directly), $\mathrm{diam}(\mathbb{CP}^n) \le \pi/\sqrt{1/4} = 2\pi$, and $\pi_1(\mathbb{CP}^n)$ is **finite**.

**Step 3: Strengthen via Synge to $\pi_1 = 0$.**

> [!note]- Derivation
> $\mathbb{CP}^n$ is compact (✓), of even real dimension $2n$ (✓), orientable (since it is Kähler, hence has a canonical complex structure, and Kähler manifolds are oriented by their volume form $\omega^n/n!$; alternatively, $\mathbb{CP}^n$ is simply connected for $n \ge 1$ which is what we are trying to prove, so we cannot use that here — but Kähler-implies-orientable is a different argument), and has positive sectional curvature ($K \ge 1/4 > 0$, hence $K > 0$ everywhere).
>
> By [[Thm - Synge's Theorem|Synge's theorem]], $\pi_1(\mathbb{CP}^n) = 0$. ∎

**Step 4: Confirm via the Hopf fibration.**

> [!note]- Derivation
> The **Hopf fibration** $\pi : S^{2n+1} \to \mathbb{CP}^n$ identifies $\mathbb{CP}^n$ as the quotient of the unit $(2n+1)$-sphere in $\mathbb{C}^{n+1}$ by the diagonal $S^1$-action $z \mapsto e^{i\alpha}z$. This is a principal $S^1$-bundle.
>
> Long exact sequence of homotopy groups for the fibration $S^1 \hookrightarrow S^{2n+1} \to \mathbb{CP}^n$ (assuming $n \ge 1$, so $\dim S^{2n+1} \ge 3$):
> $$\cdots \to \pi_1(S^1) \to \pi_1(S^{2n+1}) \to \pi_1(\mathbb{CP}^n) \to \pi_0(S^1) \to \pi_0(S^{2n+1}) \to \cdots$$
> $$\cdots \to \mathbb{Z} \to 0 \to \pi_1(\mathbb{CP}^n) \to 0 \to 0 \to \cdots$$
> Exactness at $\pi_1(\mathbb{CP}^n)$: the kernel of $\pi_1(\mathbb{CP}^n) \to \pi_0(S^1) = 0$ is all of $\pi_1(\mathbb{CP}^n)$, and the image of $\pi_1(S^{2n+1}) = 0 \to \pi_1(\mathbb{CP}^n)$ is $0$. Exactness gives $\pi_1(\mathbb{CP}^n) = 0$.
>
> This independent verification confirms Synge's conclusion.

**Step 5: Diameter comparison.**

> [!note]- Derivation
> Bonnet–Myers bound: $\mathrm{diam}(\mathbb{CP}^n) \le \pi/\sqrt{1/4} = 2\pi$.
> Actual diameter (from the explicit Fubini–Study geometry): $\mathrm{diam}(\mathbb{CP}^n) = \pi/2$ (in our normalisation where $K_{\max} = 1$). The diameter is realised between two points $[1 : 0 : \cdots : 0]$ and $[0 : 1 : 0 : \cdots : 0]$ — two orthogonal complex lines through the origin.
>
> The Bonnet–Myers bound $2\pi$ is *much* larger than the actual $\pi/2$: a factor of $4$. The reason: the Ricci bound $(2n-1)/4$ used in Bonnet–Myers is much weaker than the actual Ricci $\mathrm{Ric} = (2n+2)g$ of the Fubini–Study metric (since $\mathbb{CP}^n$ is Einstein with $\lambda = 2n + 2$, far larger than the lower bound $(2n-1)/4$). Substituting $\kappa = (2n + 2)/(2n - 1)$ instead gives a tighter Bonnet–Myers bound $\pi/\sqrt{(2n+2)/(2n-1)}$, which approaches $\pi/\sqrt{1}$ for large $n$ — still not as tight as the actual $\pi/2$, but closer.
>
> The slack between Bonnet–Myers's bound and the actual diameter is the price of using only a *lower* bound on Ricci; sharper conclusions need more refined comparison-geometry tools (e.g., **Cheng's diameter rigidity theorem**: equality in Bonnet–Myers's bound forces $M$ to be isometric to a sphere).

> [!note]- Complete formal solution
> **Part (a).** $K \ge 1/4$ gives $\mathrm{Ric}(v, v) = \sum_{j=1}^{2n-1}K(v \wedge e_j) \ge (2n-1)/4$ in any orthonormal frame, so $\mathrm{Ric} \ge \tfrac{2n-1}{4}g$. By [[Thm - Bonnet-Myers Theorem|Bonnet–Myers]] applied with $\kappa = 1/4$ (dimension $2n$), $\mathbb{CP}^n$ has $\pi_1$ finite and $\mathrm{diam} \le 2\pi$.
>
> **Part (b).** $\mathbb{CP}^n$ satisfies Synge's hypotheses: compact, orientable (Kähler), even real dimension $2n$, $K > 0$. So $\pi_1(\mathbb{CP}^n) = 0$. Confirmation: the Hopf fibration $S^{2n+1} \to \mathbb{CP}^n$ with $\pi_1(S^{2n+1}) = 0$ for $n \ge 1$ gives $\pi_1(\mathbb{CP}^n) = 0$ via the long exact sequence.
>
> **Part (c).** Bonnet–Myers diameter bound is $2\pi$; actual diameter is $\pi/2$. The slack reflects that the Ricci bound $(2n-1)/4$ used (from the minimum sectional curvature $1/4$) is far weaker than the actual Ricci $(2n+2)g$ of the Fubini–Study metric.

---

# Key Takeaways

**Real dimension matters for Bonnet–Myers and Synge on complex manifolds.** A common error in this exercise is to use the *complex* dimension $n$ in the curvature bound instead of the *real* dimension $2n$. Bonnet–Myers and Synge are theorems about real Riemannian manifolds, with the dim in $(n - 1)\kappa$ being the *real* dim. For $\mathbb{CP}^n$, this is $2n$, not $n$. Whenever you apply Riemannian comparison theorems to a complex manifold, double-check that you have the real-dim factor right.

**The two-step bootstrap: Ricci to finite $\pi_1$, then more structure to $\pi_1 = 0$.** Bonnet–Myers gives the weaker conclusion (finite $\pi_1$) from the weaker hypothesis (Ricci lower bound). For the stronger conclusion ($\pi_1 = 0$), more structure is needed: either positive sectional curvature + orientability + even-dim (Synge), or an explicit topological structure like a covering. This is the standard pattern in curvature-topology arguments: get the qualitative finite-$\pi_1$ result first, then refine using extra structure.

**The slack between Bonnet–Myers's diameter bound and the actual diameter is the price of using a Ricci lower bound.** If you knew the Ricci tensor exactly (not just a lower bound), you could often compute the diameter more precisely. For Einstein manifolds with $\mathrm{Ric} = \lambda g$, the Bonnet–Myers bound is $\pi\sqrt{(n-1)/\lambda}$, exactly sharp on the sphere. For $\mathbb{CP}^n$ Einstein with $\lambda = 2n+2$ (real dim $2n$, so $n - 1 = 2n - 1$), the sharper bound is $\pi\sqrt{(2n-1)/(2n+2)}$, which approaches $\pi$ as $n \to \infty$ — still larger than the actual $\pi/2$, but much closer than the $2\pi$ from the cruder calculation. **Cheng's diameter rigidity theorem** ($1975$) shows that equality in Bonnet–Myers (when achieved with Ricci $= (n-1)\kappa g$) forces $M$ to be isometric to the sphere $S^n_\kappa$; the strict inequality on $\mathbb{CP}^n$ thus reflects that $\mathbb{CP}^n$ is *not* a sphere despite having positive curvature.

**Companion exercise: the same Bonnet–Myers argument applies to other positively-curved homogeneous spaces.** Generalised flag manifolds $G/H$ for compact Lie groups, Wallach manifolds, and many examples in **positively-curved Riemannian geometry** satisfy similar curvature bounds, and Bonnet–Myers gives the corresponding diameter bounds and $\pi_1$ finiteness. The technique is canonical.
