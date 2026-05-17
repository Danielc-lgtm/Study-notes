---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Riemann Integral in Several Variables"
  - "Def - Jordan Measure"
  - "Thm - Fubini's Theorem"
  - "Thm - The Lebesgue Criterion for Riemann Integrability"
tags: [analysis, multivariate-analysis]
---

# Notation

$O, \Omega \subseteq \mathbb{R}^n$ are open sets. A **$C^1$ diffeomorphism** $G : O \to \Omega$ is a continuously differentiable bijection whose inverse $G^{-1} : \Omega \to O$ is also continuously differentiable. $DG(x)$ is the **Jacobian matrix** of $G$ at $x$ — the matrix of first partial derivatives — and $\det DG(x)$ its **Jacobian determinant**. $\mathrm{GL}(n,\mathbb{R})$ is the group of invertible real $n \times n$ matrices. $f$ is a function on $\Omega$; $f \circ G$ its composition with $G$. The full symbol registry is on [[Multivariate Analysis III — Integration in Several Variables]].

---

# Statement

> **The Change of Variables Formula.** Let $O$ and $\Omega$ be open subsets of $\mathbb{R}^n$ and $G : O \to \Omega$ a $C^1$ diffeomorphism. If $f$ is [[Def - The Riemann Integral in Several Variables|Riemann integrable]] on $\Omega$ (with compact support in $\Omega$), then $f \circ G \cdot |\det DG|$ is Riemann integrable on $O$, and
> $$\int_\Omega f(y)\,dV(y) = \int_O f\big(G(x)\big)\,\big|\det DG(x)\big|\,dV(x).$$
> The **linear case**: for $A \in \mathrm{GL}(n,\mathbb{R})$ and any compactly supported integrable $f$, $\int_{\mathbb{R}^n} f(y)\,dV = |\det A|\int_{\mathbb{R}^n} f(Ax)\,dV$; equivalently, for a [[Def - Jordan Measure|Jordan measurable]] set $S$, $V(A(S)) = |\det A|\cdot V(S)$.

---

# Motivation

In one variable, substitution is the rule $\int_{G(a)}^{G(b)} f(y)\,dy = \int_a^b f(G(x))\,G'(x)\,dx$ — when you change the variable by $y = G(x)$, the differential picks up a factor $G'(x)$. The factor is there because $G$ stretches the $x$-axis nonuniformly: a tiny interval $dx$ at $x$ becomes a tiny interval of length $|G'(x)|\,dx$ at $y = G(x)$, and the integral has to account for that stretching.

The question this theorem answers is: *what is the analogue in $\mathbb{R}^n$?* When you change variables by a map $G : O \to \Omega$, what replaces the factor $G'(x)$? The answer is forced by the same reasoning. The derivative of $G$ at $x$ is now a *matrix*, the Jacobian $DG(x)$, the best linear approximation to $G$ near $x$. A tiny box at $x$ is mapped, to first order, by this linear map, and a linear map $A$ multiplies volumes by exactly $|\det A|$ — that is what the determinant *is*. So an infinitesimal box of volume $dV$ at $x$ becomes a region of volume $|\det DG(x)|\,dV$ at $G(x)$, and the change of variables formula is the statement that integration must weight by this local volume-distortion factor $|\det DG(x)|$.

This is not a technicality bolted onto integration — it is the entire mechanism by which hard integrals get done. A region with the wrong shape for Fubini becomes the right shape after a change of variables: a disk becomes a rectangle under polar coordinates, a ball becomes a box under spherical coordinates, an ellipsoid becomes a ball under a linear map. And an integrand with an inconvenient form becomes simple in matched coordinates: $e^{-x^2-y^2}$ becomes $e^{-r^2}$ in polar coordinates, which then yields to elementary one-variable integration. The two great computational theorems of the topic are this one and [[Thm - Fubini's Theorem|Fubini]], and they are used in tandem: change variables to fix the geometry, then iterate.

The hypothesis that $G$ be a **diffeomorphism** — in particular a *bijection* — is the load-bearing assumption, and it is exactly the condition that $G$ neither folds the domain (which would make it overcount) nor tears it. The Jacobian being a determinant of a continuously varying invertible matrix is what guarantees the local picture (a linear stretch) glues into a global one.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$G$ is a $C^1$ diffeomorphism between open sets". The skill is recognizing when a candidate change of coordinates qualifies, or can be made to qualify.

The first disguised source is **a classical coordinate system — polar, cylindrical, spherical**. The property $B$ is "the integral has radial or rotational symmetry, so polar/spherical coordinates are natural". The bridge: polar $G(r,\theta) = (r\cos\theta, r\sin\theta)$ and its higher-dimensional cousins are $C^1$ with computable Jacobians ($\det = r$ for polar, $\rho^2\sin\varphi$ for spherical), and although they fail to be diffeomorphisms on the *closed* parameter rectangle (the axis $r = 0$ collapses, the seam $\theta = 0 \equiv 2\pi$ is glued), they *are* diffeomorphisms on the *open* rectangle, and the omitted boundary is a nil set. The non-obvious step is the boundary repair: the formula holds on the open region, and a content-zero set is added back at no cost. *Example problem:* the Gaussian integral — see [[Ex - The Gaussian integral via polar coordinates]].

The second disguised source is **an invertible linear map or affine map**. The property $B$ is "$G(x) = Ax + c$ with $A \in \mathrm{GL}(n,\mathbb{R})$". The bridge: an invertible linear map is automatically a $C^1$ diffeomorphism of $\mathbb{R}^n$ onto itself, with constant Jacobian $DG \equiv A$, so the formula reads $V(A(S)) = |\det A|\,V(S)$. The non-obvious part is that this turns *every* volume of a linearly-deformed shape — ellipsoid, parallelepiped — into a determinant computation. *Example problem:* the volume of an ellipsoid, or the integral over a parallelogram — see [[Ex - A nonlinear change of variables]].

The third disguised source is **a map with nonvanishing Jacobian that is locally invertible and globally injective**. The property $B$ is "$G$ is $C^1$, injective on $O$, and $\det DG(x) \neq 0$ everywhere". The bridge: by the [[Thm - The Inverse Function Theorem|inverse function theorem]], a $C^1$ map with nonvanishing Jacobian is *locally* a diffeomorphism, and adding global injectivity upgrades this to a genuine diffeomorphism onto its (open) image. The non-obvious step is that one need not exhibit $G^{-1}$ explicitly — nonvanishing Jacobian plus injectivity is enough. *Example problem:* substitutions like $u = x + y,\ v = x - y$, or $u = xy,\ v = y/x$ on a suitable region.

**Targets (Output Amplification)**

The conclusion is "$\int_\Omega f(y)\,dy = \int_O f(G(x))|\det DG(x)|\,dx$".

Combine the conclusion with **[[Thm - Fubini's Theorem|Fubini's theorem]]**. After the change of variables the new domain $O$ is typically a box or a region between graphs, on which Fubini iterates the integral. The further result $E$: a fully computed closed-form value. This is the standard pipeline and is non-obvious only in that the change of variables is chosen *precisely so that* the transformed domain is Fubini-friendly — the geometry, not the integrand, dictates the substitution.

Combine the conclusion with **a recursion across dimension**. Choosing $G$ to peel one dimension, or applying the formula in $\mathbb{R}^n$ and relating it to $\mathbb{R}^{n-1}$, sets up a recursion. The further result $E$: dimensional formulas — the volume of the unit $n$-ball $V_n = \pi^{n/2}/\Gamma(n/2+1)$, obtained by recursion. This is non-obvious because the formula, applied once, gives a single identity; applied recursively, an infinite family. See [[Ex - The volume of the n-dimensional ball]].

Combine the linear case with **an integrand that is itself a density**. If $p$ is a probability density and $Y = G(X)$, the formula gives the density of $Y$ as $p(G^{-1}(y))|\det DG^{-1}(y)|$. The further result $E$: the transformation rule for probability densities, and in particular the fact that a linear map with $|\det A| = 1$ preserves densities. This is non-obvious because the abstract change of variables formula, read in probability, *is* the change-of-density rule.

Combine the linear case with **a determinant equal to $\pm 1$**. When $|\det A| = 1$ — rotations, shears, Lorentz transformations — the formula gives $V(A(S)) = V(S)$: the transformation is *volume-preserving*. The further result $E$: invariance of integrals under such maps, e.g. rotation-invariance of $\int e^{-|x|^2}$, or Lorentz-invariance of the spacetime volume element. This is non-obvious because volume-preservation is read directly off a single number, the determinant.

---

# Why Is It True

The formula is believable the moment you accept one fact about determinants: **a linear map $A$ multiplies every volume by $|\det A|$.** This is not an extra theorem to be imported; for many readers it is the *definition* of the determinant — the signed volume of the image of the unit cube. Granting it, the linear case of the change of variables formula, $V(A(S)) = |\det A|\,V(S)$, is immediate, and by approximating an integrable function by indicators of sets, $\int f(y)\,dy = |\det A|\int f(Ax)\,dx$ follows.

The nonlinear case is this linear fact applied *infinitesimally and assembled by integration*. Here is the picture. Partition the domain $O$ into tiny boxes $R_\alpha$. On each box, $G$ is, to first order, its linearization at the box's center $\xi_\alpha$: $G(\xi_\alpha + y) \approx G(\xi_\alpha) + DG(\xi_\alpha)\,y$. So $G$ maps the tiny box $R_\alpha$ approximately onto a tiny *parallelepiped*, the image of $R_\alpha$ under the linear map $DG(\xi_\alpha)$. By the linear case, that parallelepiped has volume $|\det DG(\xi_\alpha)|\cdot V(R_\alpha)$. Now sum: the integral $\int_\Omega f\,dy$ is the sum of the contributions from each image piece $G(R_\alpha)$,
$$\int_\Omega f\,dy = \sum_\alpha \int_{G(R_\alpha)} f\,dy \approx \sum_\alpha f(G(\xi_\alpha))\cdot V(G(R_\alpha)) \approx \sum_\alpha f(G(\xi_\alpha))\,|\det DG(\xi_\alpha)|\,V(R_\alpha),$$
and the last sum is a Riemann sum for $\int_O f(G(x))|\det DG(x)|\,dx$. As the boxes shrink, the first-order approximation becomes exact, and the formula emerges.

So the formula is true because **integration sees only local volume-distortion, and local volume-distortion is the Jacobian determinant**. Everything $G$ does — bending, twisting — is, at the infinitesimal scale, a linear map, and a linear map's effect on volume is a single number. The factor $|\det DG(x)|$ is that number, varying from point to point. The whole content is: replace the global nonlinear $G$ by its pointwise linearizations, apply the linear case to each, and let the boxes shrink.

Why must $G$ be a *diffeomorphism*? Two reasons, both visible in the picture. *Injectivity* is what makes the sum $\sum_\alpha \int_{G(R_\alpha)}$ count each part of $\Omega$ exactly once — if $G$ folded $O$, some region of $\Omega$ would be the image of two boxes and would be counted twice; the integral would overcount by the multiplicity. *Nonvanishing Jacobian* (built into "diffeomorphism" since $G^{-1}$ is differentiable) is what keeps the linearization $DG(\xi_\alpha)$ invertible, so the image of a box is a genuine $n$-dimensional parallelepiped and not a degenerate flattened one. The diffeomorphism hypothesis is precisely the condition that the local picture — each box stretched by an invertible linear map onto a non-degenerate parallelepiped, with no overlaps — is faithful.

---

# What Makes This Hard

The conceptual core — the Jacobian is local volume-distortion — is clean; the genuine difficulties are two. First, the **role of the diffeomorphism hypothesis**: the formula is *false* if $G$ is merely $C^1$ and surjective but not injective, because it then overcounts the image by the local multiplicity, and the standard mistake is to apply polar coordinates on the *closed* rectangle $[0,\rho]\times[0,2\pi]$, where $G$ is not injective (the seam $\theta = 0 \equiv 2\pi$ and the collapsed axis $r = 0$) — the correct argument restricts to the open rectangle and adds back the omitted boundary as a nil set. Second, the **proof's reliance on controlling the approximation error**: showing that $G(R_\alpha)$ is genuinely close to the parallelepiped $DG(\xi_\alpha)(R_\alpha)$, uniformly, requires the continuity of $DG$ and a careful $(1+\varepsilon)$-inflation argument, and this is the technical heart that the intuitive picture glosses over.

---

# Rederivation Scaffold

**High-level strategy:**
Establish the linear case from "a linear map scales volume by $|\det A|$", reducing a general $A$ to a product of elementary matrices. For the nonlinear case, partition $O$ into small boxes; on each, $G$ is approximately its linearization, so $G(R_\alpha)$ is approximately a parallelepiped of volume $|\det DG(\xi_\alpha)|V(R_\alpha)$; sum and pass to the limit. Extend from continuous $f$ to integrable $f$ by squeezing.

**Subgoal decomposition:**

1. **Linear case.** Prove $\int f(y)\,dy = |\det A|\int f(Ax)\,dx$ for $A \in \mathrm{GL}(n,\mathbb{R})$.
   - *Hint:* The set of $A$ for which the identity holds is a subgroup of $\mathrm{GL}(n,\mathbb{R})$; every invertible matrix is a product of elementary matrices (row operations), so it suffices to verify the three elementary types — a permutation, a coordinate scaling, a shear. The shear case uses [[Thm - Fubini's Theorem|Fubini]] to reduce to one variable.
   - *Why needed:* It is the formula for the infinitesimal pieces.

2. **Image of a small box is close to a parallelepiped.** For a $C^1$ diffeomorphism $G$ and a small box $R_\alpha$ centered at $\xi_\alpha$, show $G(R_\alpha) \subseteq \eta_\alpha + (1+\varepsilon)H_\alpha$ where $H_\alpha = DG(\xi_\alpha)(R_\alpha - \xi_\alpha)$ is the linearized parallelepiped.
   - *Hint:* Write $G(\xi_\alpha + y) = \eta_\alpha + DG(\xi_\alpha)y + \Phi y$ with the error $\Phi = \int_0^1[DG(\xi_\alpha + ty) - DG(\xi_\alpha)]\,dt$ small by continuity of $DG$.
   - *Why needed:* It bounds $V(G(R_\alpha))$ by $(1+\varepsilon)^n|\det DG(\xi_\alpha)|V(R_\alpha)$, the per-box estimate.

3. **Sum the per-box estimates.** For $f \geq 0$ continuous, deduce $\int_\Omega f\,dV \leq \int_O f(G(x))|\det DG(x)|\,dV$.
   - *Hint:* $\int_\Omega f = \sum_\alpha \int_{G(R_\alpha)} f \leq \sum_\alpha \sup_{R_\alpha}(f\circ G)\cdot V(G(R_\alpha))$, then apply step 2 and let the partition refine.
   - *Why needed:* It gives one inequality of the formula.

4. **Reverse and combine.** Apply step 3 with $G$ replaced by $G^{-1}$ to get the opposite inequality; the two give equality. Extend from continuous to integrable $f$ by trapping $f$ between continuous functions.
   - *Hint:* Running step 3 for $G^{-1}$ and the function $h = (f\circ G)|\det DG|$ yields $\int_O h \leq \int_\Omega f$.
   - *Why needed:* It upgrades the inequality to the identity and to the full class of integrable $f$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The linear case via elementary matrices
> **Statement:** For every $A \in \mathrm{GL}(n,\mathbb{R})$ and every compactly supported continuous $f$, $\int_{\mathbb{R}^n} f(y)\,dV = |\det A|\int_{\mathbb{R}^n} f(Ax)\,dV$.
>
> **Hint:** Show the set $\mathcal{G}$ of valid $A$ is a subgroup of $\mathrm{GL}(n,\mathbb{R})$; reduce to elementary matrices (permutation, scaling, shear) since every invertible matrix is their product.
>
> **Why needed:** It is the linear building block — the formula for the infinitesimal parallelepipeds — on which the nonlinear case is assembled.
>
> > [!note]- Full proof
> > Write $I_A(f) = \int f(Ax)\,dV$. Then $A \in \mathcal{G}$ iff $I_A(f) = |\det A|^{-1}I(f)$ for all $f$. Since $I_{AB}(f) = I_B(f_A)$ where $f_A(x) = f(Ax)$, and $\det AB = \det A\det B$, the set $\mathcal{G}$ is closed under products and inverses — a subgroup. Every $A \in \mathrm{GL}(n,\mathbb{R})$ is a product of elementary matrices (Gaussian elimination by row operations), so it suffices to check the three elementary types. *Permutation* $A_1 e_j = e_{\sigma(j)}$: $|\det A_1| = 1$, and substituting permutes the coordinate names in the integral, leaving it unchanged — direct from the definition of the integral. *Scaling* $A_2 e_j = c_j e_j$: $|\det A_2| = \prod|c_j|$, and rescaling each coordinate axis by $c_j$ rescales the volume element by $\prod|c_j|$ — again direct from the definition. *Shear* $A_3 e_2 = e_2 + ce_1$, $A_3 e_j = e_j$ otherwise: $|\det A_3| = 1$; by [[Thm - Fubini's Theorem|Fubini]], $\int f(x_1 + cx_2, x') \,dV = \int(\int f(x_1+cx_2,x')\,dx_1)\,dV'$, and the inner one-variable integral is translation-invariant ($\int f(x_1 + b)\,dx_1 = \int f(x_1)\,dx_1$), so the shear leaves the integral unchanged. All three elementary types lie in $\mathcal{G}$; since they generate $\mathrm{GL}(n,\mathbb{R})$ and $\mathcal{G}$ is a subgroup, $\mathcal{G} = \mathrm{GL}(n,\mathbb{R})$.
>
> [!note]- Lemma 2: The image of a small cell is nearly its linearized parallelepiped
> **Statement:** Let $G : O \to \Omega$ be a $C^1$ diffeomorphism, $R_\alpha \subseteq O$ a cell with center $\xi_\alpha$, and $H_\alpha = DG(\xi_\alpha)(R_\alpha - \xi_\alpha)$ the parallelepiped obtained by linearizing $G$ at $\xi_\alpha$. For every $\varepsilon > 0$ there is $\delta > 0$ such that if $\operatorname{maxsize}(R_\alpha) \leq \delta$, then $G(R_\alpha) \subseteq G(\xi_\alpha) + (1+\varepsilon)H_\alpha$, and consequently $V(G(R_\alpha)) \leq (1+\varepsilon)^n|\det DG(\xi_\alpha)|\,V(R_\alpha)$.
>
> **Hint:** Taylor-expand $G$ at $\xi_\alpha$ with integral remainder; the remainder is controlled by the modulus of continuity of $DG$.
>
> **Why needed:** It is the per-cell volume estimate — the quantitative form of "$G$ stretches a tiny box like its Jacobian does".
>
> > [!note]- Full proof
> > For $y$ with $\xi_\alpha + y \in R_\alpha$, the fundamental theorem of calculus along the segment gives
> > $$G(\xi_\alpha + y) = G(\xi_\alpha) + DG(\xi_\alpha)y + \Phi(\xi_\alpha, y)y, \qquad \Phi(\xi_\alpha,y) = \int_0^1[DG(\xi_\alpha + ty) - DG(\xi_\alpha)]\,dt.$$
> > Since $DG$ is continuous, hence uniformly continuous on a compact neighbourhood, for any $\varepsilon' > 0$ there is $\delta$ such that $|y| \leq \delta$ forces the matrix norm $\|\Phi(\xi_\alpha,y)\| \leq \varepsilon'$. Writing $\Phi y = DG(\xi_\alpha)\big(DG(\xi_\alpha)^{-1}\Phi y\big)$, the perturbation $DG(\xi_\alpha)^{-1}\Phi\,y$ has norm $\leq \|DG(\xi_\alpha)^{-1}\|\varepsilon'|y|$, which can be made $\leq \varepsilon|y|$. Hence $G(\xi_\alpha + y) - G(\xi_\alpha) = DG(\xi_\alpha)(y + e)$ with $|e| \leq \varepsilon|y|$, so the image point lies in $G(\xi_\alpha) + DG(\xi_\alpha)((1+\varepsilon)(R_\alpha - \xi_\alpha)) = G(\xi_\alpha) + (1+\varepsilon)H_\alpha$. Taking volumes and using the linear case (Lemma 1), $V(H_\alpha) = |\det DG(\xi_\alpha)|V(R_\alpha)$ and $V((1+\varepsilon)H_\alpha) = (1+\varepsilon)^n V(H_\alpha)$, giving the stated bound.
>
> [!note]- Lemma 3: Reduction from integrable to continuous integrands
> **Statement:** If the change of variables formula holds for all compactly supported continuous $f$, it holds for all compactly supported Riemann integrable $f$.
>
> **Hint:** Trap $f$ between continuous functions $h_\nu \leq f \leq g_\nu$ with $\int(g_\nu - h_\nu) \to 0$, apply the formula to $h_\nu$ and $g_\nu$, and squeeze.
>
> **Why needed:** It extends the theorem from the easy class (continuous) to the class actually used (integrable, including indicators of regions).
>
> > [!note]- Full proof
> > By the approximation property of the Riemann integral (Taylor's Proposition 3.1.11), for each $\nu$ there are compactly supported continuous $h_\nu \leq f \leq g_\nu$ with $\int_\Omega h_\nu \,dV$ and $\int_\Omega g_\nu\,dV$ both within $1/\nu$ of $B = \int_\Omega f\,dV$. The formula applies to the continuous $h_\nu$ and $g_\nu$:
> > $$\int_\Omega h_\nu\,dV = \int_O h_\nu(G(x))|\det DG(x)|\,dV, \qquad \text{likewise for } g_\nu.$$
> > Since $h_\nu \circ G \leq f \circ G \leq g_\nu \circ G$ and $|\det DG| \geq 0$, the function $(f\circ G)|\det DG|$ is trapped between $(h_\nu\circ G)|\det DG|$ and $(g_\nu\circ G)|\det DG|$, whose integrals both converge to $B$. Hence $(f\circ G)|\det DG|$ is integrable on $O$ with integral $B$, which is the formula for $f$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 1 — Linear case.** By Lemma 1, for $A \in \mathrm{GL}(n,\mathbb{R})$ and compactly supported continuous $f$, $\int f(y)\,dV = |\det A|\int f(Ax)\,dV$. By Lemma 3 this extends to all compactly supported integrable $f$; taking $f = \chi_{A(S)}$ gives $V(A(S)) = |\det A|\,V(S)$ for Jordan measurable $S$.
>
> **Step 2 — Nonlinear case, one inequality.** Let $G : O \to \Omega$ be a $C^1$ diffeomorphism and $f$ continuous, compactly supported in $\Omega$, with $f \geq 0$ (the general continuous case splits into positive and negative parts). Using a partition of unity we may assume $f$ is supported in a cell $\widetilde R \subseteq \Omega$ and $f \circ G$ in a cell $R \subseteq O$. Partition $R$ into subcells $\{R_\alpha\}$ with centers $\xi_\alpha$. Each $G(R_\alpha)$ is Jordan measurable (its boundary is $G(\partial R_\alpha)$, the image of a nil set under a $C^1$ — hence locally Lipschitz — map, which is nil), and $\sum_\alpha \chi_{G(R_\alpha)} = 1$ on $\Omega$ except on a nil set. Therefore, by additivity of the integral,
> $$\int_\Omega f\,dV = \sum_\alpha \int_{G(R_\alpha)} f\,dV \leq \sum_\alpha \Big(\sup_{R_\alpha}(f\circ G)\Big)\,V(G(R_\alpha)).$$
> By Lemma 2, for any $\varepsilon > 0$ and fine enough partition, $V(G(R_\alpha)) \leq (1+\varepsilon)^n|\det DG(\xi_\alpha)|\,V(R_\alpha)$. Hence
> $$\int_\Omega f\,dV \leq (1+\varepsilon)^n\sum_\alpha \Big(\sup_{R_\alpha}(f\circ G)\Big)|\det DG(\xi_\alpha)|\,V(R_\alpha).$$
> The sum is, up to the modulus of continuity of $|\det DG|$, a Riemann sum for $\int_O (f\circ G)|\det DG|\,dV$. Letting the partition refine and $\varepsilon \to 0$,
> $$\int_\Omega f\,dV \leq \int_O f(G(x))\,|\det DG(x)|\,dV(x). \tag{$\ast$}$$
>
> **Step 3 — The reverse inequality.** Apply inequality $(\ast)$ with the diffeomorphism $G$ replaced by $G^{-1} : \Omega \to O$, and with $f$ replaced by the continuous compactly supported function $h(x) = f(G(x))|\det DG(x)|$. This gives
> $$\int_O h\,dV \leq \int_\Omega h(G^{-1}(y))\,|\det DG^{-1}(y)|\,dV(y).$$
> Now $h(G^{-1}(y)) = f(G(G^{-1}(y)))|\det DG(G^{-1}(y))| = f(y)\,|\det DG(G^{-1}(y))|$, and by the chain rule $DG^{-1}(y) = [DG(G^{-1}(y))]^{-1}$, so $|\det DG(G^{-1}(y))|\cdot|\det DG^{-1}(y)| = 1$. The integrand on the right collapses to $f(y)$, giving
> $$\int_O f(G(x))|\det DG(x)|\,dV(x) = \int_O h\,dV \leq \int_\Omega f(y)\,dV(y). \tag{$\ast\ast$}$$
>
> **Step 4 — Conclusion.** Inequalities $(\ast)$ and $(\ast\ast)$ together give
> $$\int_\Omega f(y)\,dV(y) = \int_O f(G(x))\,|\det DG(x)|\,dV(x)$$
> for every non-negative continuous compactly supported $f$, hence (splitting into positive and negative parts) for every continuous compactly supported $f$. By Lemma 3, the identity extends to every compactly supported Riemann integrable $f$ on $\Omega$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Gaussian integral and the normal distribution.** Evaluating $\int_{\mathbb{R}^2} e^{-x^2-y^2}\,dA$ by switching to polar coordinates — where the integrand becomes $e^{-r^2}$ and the Jacobian $r$ supplies exactly the factor a substitution $s = r^2$ needs — gives $\pi$, hence $\int_{\mathbb{R}} e^{-x^2}\,dx = \sqrt\pi$. This is the normalization constant of the Gaussian probability density. The application is nonobvious because a *radial symmetry* of the integrand is the cue to change coordinates, and the polar map fails injectivity on a nil seam that must be argued away. See [[Ex - The Gaussian integral via polar coordinates]].

**Lorentz invariance of the spacetime volume element.** A Lorentz transformation $\Lambda$ of Minkowski space is a linear map with $|\det\Lambda| = 1$. By the linear case, $V(\Lambda(S)) = |\det\Lambda|\,V(S) = V(S)$ — four-dimensional spacetime volume is invariant under change of inertial frame. The application is out-of-distribution because a *physical* invariance principle is read off a single algebraic fact, $\det\Lambda = \pm 1$; see [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

**Density of a transformed random variable.** If $X$ has density $p$ on $\mathbb{R}^n$ and $Y = G(X)$ for a diffeomorphism $G$, the density of $Y$ is $p(G^{-1}(y))|\det DG^{-1}(y)|$. This is the change of variables formula read as a statement about densities — the Jacobian factor is what keeps the transformed density integrating to $1$. The application is nonobvious because the "change of variables" of probability and the "change of variables" of integration are literally the same theorem.

**Volume of an ellipsoid as a determinant.** The ellipsoid $\{x : x^\top A^{-1} x \leq 1\}$ is the image of the unit ball under a linear map with determinant $\sqrt{\det A}$, so its volume is $\sqrt{\det A}\cdot V_n$ where $V_n$ is the unit-ball volume. The application is out-of-distribution because a geometric quantity (the volume of a curved region) is computed without any integration — purely from the linear case and a determinant.

---

# Bridges

- **[[Thm - Fubini's Theorem|Fubini's Theorem]]** — the partner computational tool. The change of variables deforms the domain into a box or product; Fubini then iterates. They are mutually entangled: Fubini is *used inside the proof* of the change of variables formula (the shear case of Lemma 1), and the change of variables is used to put domains into Fubini-friendly form.

- **[[Thm - The Inverse Function Theorem|The Inverse Function Theorem]]** — the existence theorem behind the hypothesis. A $C^1$ map with nonvanishing Jacobian determinant is locally a diffeomorphism; the inverse function theorem is what certifies that a candidate change of coordinates *is* a local diffeomorphism, so that the change of variables formula applies. The two together are why "compute $\det DG \neq 0$ and check injectivity" suffices.

- **[[Thm - The General Stokes Theorem|Stokes' Theorem]] and differential forms** — the change of variables formula is the $0$-boundary, top-degree shadow of the theory of [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|differential forms]]. An $n$-form's [[Def - Pullback of a Differential Form|pullback]] under $G$ produces $\det DG$ automatically from the [[Def - The Wedge Product|wedge product]], so $\int_\Omega \omega = \int_O G^*\omega$ *is* the change of variables formula, with the absolute value replaced by an [[Def - Orientation and the Integral of a Form|orientation]].

- **The Lebesgue change of variables formula** — in [[Measure Theory III — §3–4 Product Measures and Differentiation|measure theory]] the same formula holds with the diffeomorphism hypothesis relaxed (Lipschitz suffices, by Rademacher's theorem) and the integral the Lebesgue integral. The Riemann version here is the bounded, Jordan-measurable case of that theory.

---

# Unlocked by This

> [!tip] Integration of Differential Forms *(from Multivariate Analysis IV)*
> The change of variables formula is exactly the statement $\int_\Omega \omega = \int_O G^*\omega$ for a top-degree [[Multivariate Analysis IV — Differential Forms and Stokes' Theorem|differential form]] $\omega$: the Jacobian determinant emerges from the antisymmetric algebra of the [[Def - The Wedge Product|wedge product]], so the formula needs no separate justification once forms are available.

> [!tip] Riemannian Volume and Integration on Manifolds *(from Differential Geometry)*
> On a Riemannian manifold the volume element is $\sqrt{\det g}\,dx$, and the change of variables formula is what makes this *coordinate-independent*: passing between charts multiplies $dx$ by the Jacobian and $\sqrt{\det g}$ by its reciprocal, so the volume form is well-defined.
