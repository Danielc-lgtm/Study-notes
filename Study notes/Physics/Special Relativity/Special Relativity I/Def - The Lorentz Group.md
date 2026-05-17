---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - The Spacetime Interval"
  - "Thm - Invariance of the Spacetime Interval"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. A spacetime coordinate column is $X = (t, x, y, z)^{\mathsf T}$, or $X^\mu$ with $\mu = 0,1,2,3$. The **Minkowski metric** is $\eta = \mathrm{diag}(1,-1,-1,-1)$, with components $\eta_{\mu\nu}$. A Lorentz transformation is a $4\times 4$ matrix $\Lambda$, with components $\Lambda^\mu{}_\nu$; $\Lambda^{\mathsf T}$ is its transpose. The interval is $X^{\mathsf T}\eta X = t^2 - x^2 - y^2 - z^2$. In $1+1$ dimensions, $\eta = \mathrm{diag}(1,-1)$ and $\Lambda$ is $2\times 2$. Full registry on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Axiom Motivation

§1.1 derived the [[Def - The Lorentz Transformation|Lorentz transformation]] from the postulates, frame by frame, boost by boost. That is the right way to *discover* the formula but the wrong way to *organise* the theory. The boost along $x$ is one transformation; there are boosts along $y$ and $z$, rotations of space, and arbitrary compositions of all of these. We want a single concept that contains them all, and we want it characterised by an intrinsic property rather than by an explicit matrix.

[[Thm - Invariance of the Spacetime Interval|The invariance theorem]] supplies the property. It says the boost preserves the interval $X^{\mathsf T}\eta X$, and — crucially — its converse says that *preserving the interval characterises* the boost: the interval-preserving linear maps are exactly the Lorentz transformations. So the natural definition is to turn this converse into the definition. A Lorentz transformation *is* a linear map of spacetime that preserves the interval. This is the move §1.2 is built on, and it is worth pausing on why it is the right move.

First, it is intrinsic. The interval is the one observer-independent quantity in the theory; defining the transformations as its symmetries ties the definition to physics, not to a coordinate choice. Second, it makes the group structure automatic. If $\Lambda_1$ and $\Lambda_2$ each preserve the interval, so does $\Lambda_2\Lambda_1$ (apply one, then the other); the identity preserves it; and an interval-preserving map is invertible with interval-preserving inverse. So the interval-preserving maps form a [[Def - Group|group]] *for free* — closure, identity, inverses all follow from the single defining property, with no checking. Third, it exposes the analogy that runs through the whole topic. The rotations of Euclidean space are *defined* as the linear maps preserving the Euclidean form $X^{\mathsf T}X$ — that is the group $O(3)$. The Lorentz transformations are the linear maps preserving the Minkowski form $X^{\mathsf T}\eta X$. The two definitions are identical except that the identity matrix is replaced by $\eta$. The Lorentz group is to $\eta$ what the orthogonal group is to the Euclidean form: a **pseudo-orthogonal group**.

The desideratum, then, is a condition on the matrix $\Lambda$ equivalent to "preserves the interval". Demanding $X^{\mathsf T}\eta X = (\Lambda X)^{\mathsf T}\eta(\Lambda X) = X^{\mathsf T}(\Lambda^{\mathsf T}\eta\Lambda)X$ for all $X$, and using that a symmetric form is determined by its quadratic form, gives the matrix equation $\Lambda^{\mathsf T}\eta\Lambda = \eta$. This is the definition. Why not a weaker condition — say, preserving only the *light cone* $X^{\mathsf T}\eta X = 0$? Because that admits also the dilations $X \mapsto \kappa X$, which rescale the interval; demanding the full interval be fixed, not just its zero set, is what removes them. Why not a stronger condition — preserving each coordinate separately? Because that admits only the identity; the whole point is that boosts genuinely mix $t$ with $x$.

---

# The Definition

The **Lorentz group** $O(1,3)$ is the set of real $4\times 4$ matrices $\Lambda$ satisfying
$$
\boxed{\quad \Lambda^{\mathsf T}\,\eta\,\Lambda = \eta, \qquad \eta = \mathrm{diag}(1,-1,-1,-1), \quad}
$$
equivalently the linear maps of spacetime that preserve the interval $X^{\mathsf T}\eta X$ for every $X$. In index notation the condition reads $\Lambda^\mu{}_\rho\,\eta_{\mu\nu}\,\Lambda^\nu{}_\sigma = \eta_{\rho\sigma}$. The set $O(1,3)$ is a group under matrix multiplication: it contains the identity, is closed under products, and contains the inverse of each element.

**Subgroups by determinant and time-orientation.** Taking the determinant of the defining equation gives $(\det\Lambda)^2\det\eta = \det\eta$, hence $(\det\Lambda)^2 = 1$ and
$$\det\Lambda = \pm 1.$$
The condition also forces $(\Lambda^0{}_0)^2 \ge 1$, so $\Lambda^0{}_0 \ge 1$ or $\Lambda^0{}_0 \le -1$. These two binary choices split $O(1,3)$ into four disjoint pieces:

- The **proper** Lorentz transformations have $\det\Lambda = +1$; they form the subgroup $SO(1,3)$.
- The **orthochronous** Lorentz transformations have $\Lambda^0{}_0 \ge 1$; they preserve the direction of time.
- The **proper orthochronous** Lorentz group $SO^+(1,3)$ — both conditions — is the piece containing the identity; it is a subgroup, and it is the connected component of the identity.

The remaining three pieces are obtained from $SO^+(1,3)$ by composing with the discrete transformations **parity** $P = \mathrm{diag}(1,-1,-1,-1)$ (spatial reflection, $\det = -1$) and **time reversal** $T = \mathrm{diag}(-1,1,1,1)$ ($\Lambda^0{}_0 < 0$).

**The dimension.** A $4\times 4$ matrix has $16$ entries; the equation $\Lambda^{\mathsf T}\eta\Lambda = \eta$ is an equality of symmetric matrices, hence $10$ independent constraints. So $O(1,3)$ is a $16 - 10 = 6$-parameter group: **three rotations** of space and **three boosts**.

In $1+1$ dimensions, $\eta = \mathrm{diag}(1,-1)$ and $O(1,1)$ is the group of $2\times 2$ matrices with $\Lambda^{\mathsf T}\eta\Lambda = \eta$; it is one-dimensional (one boost, no rotations), and $SO^+(1,1)$ consists exactly of the boost matrices $\begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$.

---

# Categorical / Structural Definition

The Lorentz group is the **isometry group of the Minkowski bilinear form** — equivalently, the **automorphism group of Minkowski space as a metric vector space**. Given a real vector space $V$ with a non-degenerate symmetric bilinear form $\eta$, the structure-preserving linear maps — those $\Lambda$ with $\eta(\Lambda X, \Lambda Y) = \eta(X,Y)$ for all $X, Y$ — form a group, the **isometry group** of $(V,\eta)$, and it depends only on the signature of $\eta$ (Sylvester's law of inertia). When $\eta$ has signature $(p,q)$ this group is the **pseudo-orthogonal group** $O(p,q)$. The Lorentz group is the case $(p,q) = (1,3)$.

This is the same categorical pattern as a [[Def - Group Action|group action]] preserving structure: $O(1,3)$ acts on Minkowski space by linear isometries, exactly as $O(3)$ acts on Euclidean space and as the automorphism group of any structured object acts on that object. The proper orthochronous subgroup $SO^+(1,3)$ is moreover a six-dimensional **Lie group** — a group that is also a smooth manifold, with smooth multiplication — and it is connected, which is why every proper orthochronous transformation can be reached from the identity by a continuous path of boosts and rotations.

---

# Examples / Corollaries

**Is an instance — the boost along $x$.** $\Lambda[v] = \begin{pmatrix}\gamma & -\gamma v & 0 & 0\\-\gamma v & \gamma & 0 & 0\\0&0&1&0\\0&0&0&1\end{pmatrix}$ satisfies $\Lambda^{\mathsf T}\eta\Lambda = \eta$ (a direct $2\times 2$ check using $\gamma^2(1-v^2)=1$, the $y,z$ block being trivial). It has $\det = +1$ and $\Lambda^0{}_0 = \gamma \ge 1$, so it lies in $SO^+(1,3)$.

**Is an instance — a spatial rotation.** $\Lambda = \begin{pmatrix}1 & 0\\0 & R\end{pmatrix}$ with $R \in SO(3)$ (a $3\times 3$ rotation, $R^{\mathsf T}R = I$) satisfies $\Lambda^{\mathsf T}\eta\Lambda = \eta$: it leaves $t$ alone and preserves $x^2+y^2+z^2$. The rotations are the Lorentz transformations that touch only space — they form an $SO(3)$ subgroup, and they account for three of the six parameters.

**Is an instance — parity and time reversal.** $P = \mathrm{diag}(1,-1,-1,-1)$ has $\det P = -1$ (improper, orthochronous); $T = \mathrm{diag}(-1,1,1,1)$ has $\Lambda^0{}_0 = -1$ (proper in $1+3$ since $\det = -1\cdot 1 = -1$... in fact $\det T = -1$, improper and non-orthochronous). These discrete elements lie in $O(1,3)$ but outside $SO^+(1,3)$; they are the reason the Lorentz group has four components.

**Is NOT an instance — a Galilean boost.** The Galilean transformation $\begin{pmatrix}1 & 0\\-v & 1\end{pmatrix}$ does *not* satisfy $\Lambda^{\mathsf T}\eta\Lambda = \eta$: it preserves $t$ but not the interval $t^2 - x^2$. The Galilean group is the isometry group of a *degenerate* structure (absolute time), a genuinely different group, and this is the formal statement that Galilean relativity is not special relativity.

**Is NOT an instance — a dilation.** $\Lambda = \kappa I$ with $\kappa \ne \pm 1$ preserves the *light cone* ($X^{\mathsf T}\eta X = 0 \Rightarrow$ same for $\kappa X$) but rescales the interval by $\kappa^2$, so $\Lambda^{\mathsf T}\eta\Lambda = \kappa^2\eta \ne \eta$. Dilations are excluded precisely because the definition demands the *full* interval be fixed, not just its zero set — the conformal group, which does allow them, is strictly larger.

**Corollary — the Lorentz group is a genuine group, with no checking.** Closure: if $\Lambda_1^{\mathsf T}\eta\Lambda_1 = \eta$ and $\Lambda_2^{\mathsf T}\eta\Lambda_2 = \eta$, then $(\Lambda_2\Lambda_1)^{\mathsf T}\eta(\Lambda_2\Lambda_1) = \Lambda_1^{\mathsf T}(\Lambda_2^{\mathsf T}\eta\Lambda_2)\Lambda_1 = \Lambda_1^{\mathsf T}\eta\Lambda_1 = \eta$. Identity: $I^{\mathsf T}\eta I = \eta$. Inverse: $\det\Lambda = \pm 1 \ne 0$ so $\Lambda^{-1}$ exists, and conjugating the defining equation gives $(\Lambda^{-1})^{\mathsf T}\eta\Lambda^{-1} = \eta$. All three group axioms (see [[Group Theory I — §1.1–1.2]]) hold automatically — this is the payoff of defining the group by an invariance.

**Corollary — every element of $SO^+(1,3)$ is a boost followed by a rotation.** Counting parameters: three boosts, three rotations, six total, matching the dimension. Concretely, any proper orthochronous $\Lambda$ factors as (rotation)(standard boost)(rotation). The boosts alone do not form a subgroup — composing two non-collinear boosts produces a rotation, the **Wigner rotation** — but boosts and rotations together generate $SO^+(1,3)$.

---

# Unlocked by This

> [!tip] Rapidity and the Boost Subgroup *(from §1.2)*
> Along a fixed direction the boosts form a one-parameter subgroup isomorphic to $(\mathbb{R}, +)$; the isomorphism is the **rapidity** ([[Def - Rapidity]]). This is the cleanest piece of the Lorentz group, and it makes [[Thm - Relativistic Velocity Addition|velocity addition]] a triviality.

> [!tip] The Lie Algebra and the Spin of Fields *(from QFT and Gauge Theory)*
> As a Lie group, $SO^+(1,3)$ has a six-dimensional **Lie algebra** $\mathfrak{so}(1,3)$ with generators of rotations and boosts. Its finite-dimensional representations are labelled by two half-integers and classify the **spin** of relativistic fields — scalar, spinor, vector — making the Lorentz group the organising principle of **quantum field theory**.

> [!tip] The Poincaré Group *(from Relativistic Dynamics)*
> Adjoining the spacetime translations to the Lorentz group gives the **Poincaré group** $ISO^+(1,3) = SO^+(1,3) \ltimes \mathbb{R}^{1,3}$, the full symmetry group of Minkowski space. Its irreducible representations are labelled by **mass** and **spin** — Wigner's classification of elementary particles.
