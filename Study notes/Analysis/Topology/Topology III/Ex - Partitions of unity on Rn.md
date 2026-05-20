---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Partition of Unity"
  - "Def - Locally Finite Family and Refinement"
tags: [analysis, topology]
---

# Problem Statement

Construct an explicit smooth ($C^\infty$) **partition of unity** on $\mathbb{R}^n$ subordinate to the open cover
$$\{B(k, 2) : k \in \mathbb{Z}^n\}$$
where $B(k, 2)$ is the open ball of radius $2$ centered at the integer point $k \in \mathbb{Z}^n$.

(a) Construct a smooth bump function $\phi : \mathbb{R}^n \to [0, 1]$ with $\phi \equiv 1$ on the closed unit ball $\overline{B(0, 1)}$ and $\operatorname{supp}(\phi) \subseteq B(0, 2)$.

(b) For each $k \in \mathbb{Z}^n$, set $\widehat\rho_k(x) = \phi(x - k)$ — translates of $\phi$.

(c) Show that the sum $S(x) = \sum_{k \in \mathbb{Z}^n} \widehat\rho_k(x)$ is everywhere $\geq 1$ (because the unit balls $\overline{B(k, 1)}$ cover $\mathbb{R}^n$) and is *locally finite* (every $x$ has a neighborhood meeting only finitely many supports).

(d) Define $\rho_k(x) = \widehat\rho_k(x)/S(x)$ and verify $\{\rho_k\}_{k \in \mathbb{Z}^n}$ is a smooth partition of unity subordinate to $\{B(k, 2)\}$.

**Recall:**

A [[Def - Partition of Unity|**partition of unity**]] subordinate to an open cover $\{U_\alpha\}$ of $X$ is a family of continuous (here: smooth) functions $\{\rho_\alpha : X \to [0, 1]\}$ with $\operatorname{supp}(\rho_\alpha) \subseteq U_\alpha$, supports forming a [[Def - Locally Finite Family and Refinement|locally finite]] cover of $X$, and $\sum_\alpha \rho_\alpha(x) = 1$ for every $x$.

![[Def - Partition of Unity#The Definition]]

A family $\{A_\alpha\}$ in $X$ is [[Def - Locally Finite Family and Refinement|**locally finite**]] if every $x \in X$ has a neighborhood meeting only finitely many $A_\alpha$. The support of a function $f : X \to \mathbb{R}$ is $\operatorname{supp}(f) = \overline{\{x : f(x) \neq 0\}}$.

---

# Convergent Strategy

**Problem class.** *Explicit partition of unity* on a specific cover of $\mathbb{R}^n$, used as the standard model for understanding partitions of unity on more general spaces (manifolds, paracompact spaces).

**Assumption pattern.** The integer lattice $\mathbb{Z}^n \subseteq \mathbb{R}^n$ is countable, discrete, regularly spaced — natural "centers" for a periodic cover. Balls of radius $2$ around integer points overlap heavily (any two adjacent balls intersect), and balls of radius $1$ already cover $\mathbb{R}^n$ (since every point is within distance $\sqrt n/2 < 1$ of an integer point — actually within distance $\sqrt n / 2$ for the cube, but $1$ for the closer integer in each coordinate; in fact any point is within distance $\leq \sqrt n / 2$ of $\mathbb{Z}^n$, and for $n \leq 4$, $\sqrt n / 2 \leq 1$; for larger $n$, the radius-1 balls *still* cover because each coordinate can be approximated within $1/2$ separately... we should sanity-check).

Wait — for $n$ large, the distance from $(1/2, 1/2, \dots, 1/2)$ to the nearest integer point is $\sqrt{n}/2$, which exceeds $1$ for $n > 4$. So radius-1 balls do *not* cover $\mathbb{R}^n$ for $n > 4$. We should use radius $> \sqrt n / 2$. The exercise as stated uses radius-$2$ outer balls, but the inner "$\phi \equiv 1$" region should be the radius needed to cover $\mathbb{R}^n$. We'll adjust: use $\phi \equiv 1$ on $\overline{B(0, \sqrt n / 2 + 1/2)}$ or simpler: on $\overline{B(0, \sqrt n)}$ (well within radius $2$ as long as $\sqrt n < 2$, i.e. $n \leq 3$). For general $n$, use $\phi \equiv 1$ on a closed ball whose translates by $\mathbb{Z}^n$ cover $\mathbb{R}^n$.

Cleanest: replace the cover by $\{B(k, R)\}$ with $R$ sufficiently large to ensure coverage. The exercise's statement implicitly assumes $n \leq 3$ or some bound; the spirit is the same. We will work with general $n$ by writing $\phi \equiv 1$ on $\overline{B(0, \sqrt n)}$ — which works for $n$ such that $\sqrt n < 2$, i.e. $n \in \{1, 2, 3\}$. For general $n$, scale the cover.

For the writeup, we'll take the cover as $\{B(k, R)\}$ for $R$ large enough that radius-$R/2$ balls already cover $\mathbb{R}^n$ — specifically $R = 2\sqrt n$, with $\phi \equiv 1$ on $\overline{B(0, \sqrt n)}$ and $\operatorname{supp}(\phi) \subseteq B(0, 2\sqrt n)$. (The problem statement uses radius $2$ but the geometry requires this adjustment for $n > 3$.) The construction is the same.

**Theorem routing.**
- Build a bump $\phi$ via the standard $\exp(-1/t)$ construction.
- Form translates $\widehat\rho_k$.
- The denominator $S(x) = \sum_k \widehat\rho_k(x)$ is locally finite (only finitely many $\widehat\rho_k$ are nonzero at any $x$) and bounded below by $1$ (because the unit-radius translates of the support-$\{1\}$ region cover $\mathbb{R}^n$).
- Normalize.

**Key decision point.** The smooth bump function — the existence of $C^\infty$ functions with prescribed compact support — is the only nontrivial technical input. Everything else is structural.

---

# Legal Operations Used

1. **Construct a smooth bump function via the $\exp(-1/t)$ trick.** $\eta(t) = \exp(-1/t)$ for $t > 0$, $\eta(t) = 0$ for $t \leq 0$ is smooth (all derivatives at $0$ vanish). $\beta(t) = \eta(t) \cdot \eta(1 - t)$ is smooth, supported in $[0, 1]$, positive on $(0, 1)$. Cumulative integrals give smooth step functions.

2. **Translate a bump function by a lattice element** to get a periodic family.

3. **Normalize by a locally finite sum** to convert "supports cover" + "sum positive" into "partition of unity".

4. **Verify local finiteness via lattice geometry.** Any compact $K \subseteq \mathbb{R}^n$ intersects only finitely many lattice translates of a fixed compact set.

---

# Hints

> [!note]- Hint 1
> *Bump construction.* Define $\eta : \mathbb{R} \to \mathbb{R}$ by $\eta(t) = \exp(-1/t)$ for $t > 0$, $\eta(t) = 0$ for $t \leq 0$. $\eta$ is $C^\infty$ (all derivatives at $0$ are zero). Define $\psi : \mathbb{R} \to [0, 1]$ by $\psi(t) = \eta(t)/(\eta(t) + \eta(1 - t))$: smooth, $\psi(t) = 0$ for $t \leq 0$, $\psi(t) = 1$ for $t \geq 1$, monotonically increasing on $[0, 1]$.

> [!note]- Hint 2
> Define $\phi : \mathbb{R}^n \to [0, 1]$ by $\phi(x) = \psi(2 - \lVert x \rVert)$. Then $\phi(x) = 1$ when $\lVert x \rVert \leq 1$ (so $2 - \lVert x \rVert \geq 1$), $\phi(x) = 0$ when $\lVert x \rVert \geq 2$ (so $2 - \lVert x \rVert \leq 0$). So $\phi \equiv 1$ on $\overline{B(0, 1)}$ and $\operatorname{supp}(\phi) \subseteq \overline{B(0, 2)}$. The function $\phi$ is smooth wherever $\lVert x \rVert > 0$, but smoothness at $0$ requires care — work around this by using $\psi(2 - \lVert x \rVert^2)$ instead (smooth everywhere since $\lVert x \rVert^2$ is smooth).

> [!note]- Hint 3
> *Local finiteness.* For $x \in \mathbb{R}^n$, the support of $\widehat\rho_k = \phi(\cdot - k)$ is $\overline{B(k, 2)}$. The compact $\overline{B(x, 1/2)}$ (a neighborhood of $x$) intersects $\overline{B(k, 2)}$ only for $k$ with $\lVert k - x \rVert \leq 5/2$, which is a finite set (bounded subset of $\mathbb{Z}^n$). So only finitely many $\widehat\rho_k$ are nonzero in this neighborhood.

> [!note]- Hint 4
> *$S(x) \geq 1$.* For every $x \in \mathbb{R}^n$, choose $k_0 \in \mathbb{Z}^n$ nearest to $x$. Then $\lVert x - k_0 \rVert \leq \sqrt n / 2$ (by coordinate-by-coordinate rounding). If $\sqrt n / 2 \leq 1$ (i.e. $n \leq 4$), $\widehat\rho_{k_0}(x) = \phi(x - k_0) = 1$, so $S(x) \geq 1$. For $n > 4$, rescale the lattice or use a larger bump (problem assumes manageable $n$).

> [!note]- Hint 5
> $\rho_k = \widehat\rho_k / S$, with $S \geq 1 > 0$ everywhere. Each $\rho_k$ is smooth (smooth/positive-smooth), $\operatorname{supp}(\rho_k) = \operatorname{supp}(\widehat\rho_k) \subseteq \overline{B(k, 2)}$, $\sum_k \rho_k = S/S = 1$.

---

# Solution

The construction is the standard recipe: build a smooth bump $\phi$ on $\mathbb{R}^n$ supported in $B(0, 2)$ and identically $1$ on a sub-region that, when translated by the lattice $\mathbb{Z}^n$, covers $\mathbb{R}^n$. Translate, sum, normalize.

**Step 1: A smooth one-dimensional cutoff.**

The function
$$\eta(t) = \begin{cases} \exp(-1/t), & t > 0 \\ 0, & t \leq 0 \end{cases}$$
is $C^\infty$ on $\mathbb{R}$.

> [!note]- Derivation
> All derivatives of $\eta$ at $t = 0$ from the right are zero — a standard computation using $\eta^{(k)}(t) = P_k(1/t) \exp(-1/t)$ for $t > 0$, $P_k$ a polynomial, and $\exp(-1/t) \to 0$ faster than any polynomial as $t \to 0^+$. So $\eta^{(k)}(0) = 0$ for all $k$, matching the left-hand $\eta \equiv 0$.
>
> Define
> $$\psi(t) = \frac{\eta(t)}{\eta(t) + \eta(1 - t)}.$$
> Denominator never vanishes: $\eta(t) > 0$ for $t > 0$, $\eta(1 - t) > 0$ for $t < 1$, so at least one is positive whenever $t \in \mathbb{R}$. Hence $\psi$ is $C^\infty$. Properties: $\psi(t) = 0$ for $t \leq 0$, $\psi(t) = 1$ for $t \geq 1$ (in those cases the numerator equals the denominator), $\psi$ smoothly interpolates on $[0, 1]$.

**Step 2: The radial bump function on $\mathbb{R}^n$.**

Define $\phi : \mathbb{R}^n \to [0, 1]$ by
$$\phi(x) = \psi(2 - \lVert x \rVert^2).$$
Then $\phi$ is $C^\infty$ on $\mathbb{R}^n$, identically $1$ on $\overline{B(0, 1)}$, and $\operatorname{supp}(\phi) \subseteq \overline{B(0, \sqrt 2)}$ — which is contained in $B(0, 2)$.

> [!note]- Derivation
> *Smoothness.* $\lVert x \rVert^2 = \sum x_i^2$ is $C^\infty$ on $\mathbb{R}^n$ (polynomial). $\psi$ is $C^\infty$ on $\mathbb{R}$. So $\phi = \psi \circ (2 - \lVert \cdot \rVert^2)$ is $C^\infty$.
>
> *Values.* For $\lVert x \rVert \leq 1$, $\lVert x \rVert^2 \leq 1$, so $2 - \lVert x \rVert^2 \geq 1$, so $\phi(x) = \psi(2 - \lVert x \rVert^2) = 1$ (since $\psi(t) = 1$ for $t \geq 1$). For $\lVert x \rVert \geq \sqrt 2$, $\lVert x \rVert^2 \geq 2$, so $2 - \lVert x \rVert^2 \leq 0$, so $\phi(x) = 0$.
>
> So $\phi \equiv 1$ on $\overline{B(0, 1)}$ and $\operatorname{supp}(\phi) \subseteq \overline{B(0, \sqrt 2)} \subseteq B(0, 2)$.

**Step 3: Translate to form a lattice family $\widehat\rho_k$.**

For each $k \in \mathbb{Z}^n$, set $\widehat\rho_k(x) = \phi(x - k)$. Each $\widehat\rho_k$ is $C^\infty$, $\widehat\rho_k \equiv 1$ on $\overline{B(k, 1)}$, $\operatorname{supp}(\widehat\rho_k) \subseteq B(k, 2)$.

> [!note]- Derivation
> Translation $x \mapsto x - k$ is a $C^\infty$ diffeomorphism, so $\widehat\rho_k$ inherits smoothness from $\phi$. The supports and identically-$1$ regions transform under the translation: $\operatorname{supp}(\widehat\rho_k) = k + \operatorname{supp}(\phi) \subseteq B(k, 2)$, and $\widehat\rho_k \equiv 1$ on $k + \overline{B(0, 1)} = \overline{B(k, 1)}$.

**Step 4: The lattice sum $S = \sum_k \widehat\rho_k$ is locally finite and everywhere $\geq 1$ (for $n \leq 4$).**

> [!note]- Derivation
> *Local finiteness.* For any $x \in \mathbb{R}^n$, consider the open ball $B(x, 1)$. A term $\widehat\rho_k$ contributes nonzero to $S$ on $B(x, 1)$ only if $\operatorname{supp}(\widehat\rho_k) \cap B(x, 1) \neq \emptyset$, i.e. $\lVert k - x \rVert < 2 + 1 = 3$. The number of $k \in \mathbb{Z}^n$ with $\lVert k - x \rVert < 3$ is bounded by the number of integer lattice points in a ball of radius $3$, which is finite ($\leq C \cdot 3^n$ for some constant $C$). So at most finitely many $\widehat\rho_k$ are nonzero on $B(x, 1)$, and the sum $S$ is a finite sum on each $B(x, 1)$, hence well-defined and smooth.
>
> *Lower bound $S \geq 1$.* For $n \leq 4$ (the case the problem implicitly assumes), every $x \in \mathbb{R}^n$ is within distance $\sqrt n / 2 \leq \sqrt 4/2 = 1$ of the nearest lattice point $k_0$. Then $\lVert x - k_0 \rVert \leq 1$, so $\widehat\rho_{k_0}(x) = 1$, so $S(x) \geq 1$.
>
> For $n > 4$, the same construction works with a *larger* bump: replace the inner unit-ball by a ball of radius $\sqrt n / 2$, ensuring coverage, and the outer ball of $\phi$ by a ball of correspondingly larger radius. Or, more simply, scale the lattice: use $\mathbb{Z}^n$ scaled by $1/\sqrt n$ (denser lattice) and the same radius-$2$ outer balls. The construction is structurally identical.

**Step 5: The normalized family $\{\rho_k\}$ is a smooth partition of unity.**

Define $\rho_k = \widehat\rho_k / S$. Then $\{\rho_k\}_{k \in \mathbb{Z}^n}$ is the required partition of unity.

> [!note]- Derivation
> *Smoothness.* $S \geq 1 > 0$ everywhere, so $\rho_k = \widehat\rho_k / S$ is smooth (smooth over smooth-positive).
>
> *Values in $[0, 1]$.* $\rho_k = \widehat\rho_k / S$ with $0 \leq \widehat\rho_k \leq 1 \leq S$, so $0 \leq \rho_k \leq 1$.
>
> *Support.* $\operatorname{supp}(\rho_k) = \operatorname{supp}(\widehat\rho_k) \subseteq \overline{B(k, 2)} \subseteq B(k, R)$ for $R$ slightly larger. (To match the original cover $\{B(k, 2)\}$ exactly, replace $\phi$ by a slightly more aggressive cutoff — the support strictly inside $B(0, 2)$.) Concretely: with our $\phi$ supported in $\overline{B(0, \sqrt 2)} \subsetneq B(0, 2)$, the support $\operatorname{supp}(\widehat\rho_k) \subseteq \overline{B(k, \sqrt 2)} \subsetneq B(k, 2)$.
>
> *Locally finite support family.* From Step 4, only finitely many $\widehat\rho_k$ are nonzero on any $B(x, 1)$. The same is true for $\rho_k$ (same support). So the family of supports $\{\operatorname{supp}(\rho_k)\}$ is locally finite.
>
> *Sum.* $\sum_k \rho_k(x) = \sum_k \widehat\rho_k(x)/S(x) = S(x)/S(x) = 1$ for every $x$. (The sum is well-defined as a finite sum at each $x$ by local finiteness.)
>
> Hence $\{\rho_k\}_{k \in \mathbb{Z}^n}$ is a smooth partition of unity subordinate to the cover $\{B(k, 2)\}_{k \in \mathbb{Z}^n}$.

> [!note]- Complete formal solution
> Build $\eta(t) = e^{-1/t}\mathbf{1}_{t > 0}$ ($C^\infty$), $\psi(t) = \eta(t)/(\eta(t) + \eta(1-t))$ ($C^\infty$, $\psi = 0$ on $(-\infty, 0]$, $\psi = 1$ on $[1, \infty)$). Set $\phi(x) = \psi(2 - \lVert x \rVert^2)$ ($C^\infty$, $\phi = 1$ on $\overline{B(0, 1)}$, $\operatorname{supp}\phi \subseteq \overline{B(0, \sqrt 2)} \subseteq B(0, 2)$).
>
> Translates $\widehat\rho_k = \phi(\cdot - k)$ for $k \in \mathbb{Z}^n$ give a locally finite family (only $k$ with $\lVert k - x \rVert < 3$ contribute on $B(x, 1)$). $S = \sum_k \widehat\rho_k \geq 1$ (nearest lattice point is within $\sqrt n / 2 \leq 1$ for $n \leq 4$). Normalize: $\rho_k = \widehat\rho_k / S$. Then $\rho_k$ smooth, $\rho_k \geq 0$, $\sum_k \rho_k = 1$, $\operatorname{supp}\rho_k \subseteq B(k, 2)$, locally finite. $\blacksquare$

---

# Key Takeaways

**Smooth bump functions are the cornerstone of differential topology and analysis on manifolds.** The function $\exp(-1/t)$ — flat at $0$, positive on $(0, \infty)$, all derivatives at $0$ vanish — is what makes smooth manifolds *function-rich*: every closed-open sandwich admits a smooth interpolation. This is in stark contrast to real-analytic functions, which cannot have compactly supported nontrivial examples (analytic + zero on an interval ⇒ zero everywhere). The whole apparatus of smooth analysis — partitions of unity, smooth approximation, smooth extensions — rests on the availability of bump functions, which in turn rests on the $\exp(-1/t)$ construction.

**Translation-by-lattice is the model "locally finite" pattern.** The integer lattice $\mathbb{Z}^n$ in $\mathbb{R}^n$ is the simplest discrete, regularly-spaced subset, and its translates of a compactly supported function give the simplest locally finite family. Any compact set meets only finitely many lattice translates (because $\mathbb{Z}^n \cap K$ is finite for compact $K$). The generalization: any *proper* discrete subset of any locally compact group gives a locally finite family of translates, used in defining locally summable measures, periodic functions via the Poisson summation formula, and the modular group / fundamental domain constructions.

**The partition of unity construction is "build a single bump, translate, normalize" — a recipe that generalizes to manifolds via charts.** Step 1 (bump construction) is the only piece that is genuinely about $\mathbb{R}^n$ and uses smoothness in an essential way. Steps 2-5 (translate, sum, normalize) are formal and generalize: on a paracompact Hausdorff space (in particular, a smooth manifold), one uses bump functions in coordinate charts, pulled back via the chart maps, then the same locally-finite-cover + normalize recipe applies. The general construction is laid out in [[Ex - Partition of unity for a smooth manifold]].

**Local finiteness is what makes the sum $\sum_k \widehat\rho_k$ converge — even pointwise, even smoothly.** At each point, only finitely many terms contribute, so convergence and smoothness are not at issue. This is the *defining* utility of the local finiteness condition: it converts a potentially infinite sum into a *locally finite* sum, which is just a finite sum *near each point* — fully compatible with continuity, smoothness, integrability, and so on. Without local finiteness, the sum might not even be well-defined; with it, all operations commute with the sum. This is the structural reason paracompactness — which guarantees locally finite refinements of any open cover — is the right hypothesis for partition-of-unity constructions.

**Trigger-reaction: "I have a global construction needing to glue local pieces" ⇒ "build a partition of unity subordinate to a chart cover".** This is *the* standard move in differential geometry. Examples: defining a Riemannian metric (take Euclidean metric in each chart, glue with partition of unity); defining a smooth function with prescribed values on a closed subset (Tietze + smooth approximation); proving every smooth manifold admits a Riemannian metric; integrating a top-form over a manifold (define locally in charts, sum with partition of unity, prove invariance via the change-of-variables formula); proving the de Rham theorem (Čech-de Rham double complex computations rely on a fine partition of unity). Each is a "local on each $U_\alpha$, summed with $\rho_\alpha$" move.

**The smoothness of the bump function determines the smoothness of the partition of unity.** Continuous bump → continuous partition; smooth bump → smooth partition. This is what allows smooth partitions of unity on smooth manifolds. In contrast, real-analytic partitions of unity *do not exist* (real-analytic functions cannot be compactly supported and nonzero), which is why real-analytic geometry must use different tools (sheaves, Stein theory, complex coverings) — and why algebraic geometry is structurally so different from differential geometry.

**The dimension-vs-radius issue is a subtle "geometry of the cube" point.** In dimension $n$, the maximum distance from any point of $\mathbb{R}^n$ to the nearest integer lattice point is $\sqrt n / 2$ (achieved at the center of a unit cube). So the lattice $\mathbb{Z}^n$ does not have unit-radius covering balls for $n > 4$. This is a manifestation of the *curse of dimensionality*: balls become "small" relative to cubes as $n$ grows. The fix is to either use a denser lattice or larger covering balls. The exercise's setup (radius-$2$ outer balls, radius-$1$ inner regions) is implicit about the dimensional cap; the general lesson is that geometric estimates in $\mathbb{R}^n$ degrade rapidly with $n$.
