---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Local Frame and Four-Rotation"
  - "Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Problem Statement

A [[Def - Local Frame and Four-Rotation|local frame]] $(e_\alpha)$ is carried along an observer's worldline, with $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$ and $e_0 = U_0$; its evolution defines the four-rotation $de_\alpha/d\tau = \Omega^\beta{}_\alpha e_\beta$ and the bilinear form $\underline\Omega(X, Y) = X\cdot\Omega(Y)$. Work with $c = 1$, $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. By differentiating the orthonormality $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$, prove that $\underline\Omega$ is **antisymmetric**: $\underline\Omega(e_\beta, e_\alpha) = -\underline\Omega(e_\alpha, e_\beta)$.
2. Show that antisymmetry of $\underline\Omega$ (lowered indices) is **not** the same as $\Omega^\beta{}_\alpha = -\Omega^\alpha{}_\beta$ (mixed indices); derive the correct component relations $\Omega^0{}_0 = 0$, $\Omega^i{}_0 = \Omega^0{}_i$, $\Omega^i{}_j = -\Omega^j{}_i$ in mostly-minus signature.
3. Using the [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|decomposition]] of $\underline\Omega$ into four-acceleration and spatial rotation, write $de_\alpha/d\tau$ and read off that $de_0/d\tau = A_0$ and $de_i/d\tau = -(A_0\cdot e_i)U_0 + \vec\omega\times_{U_0}e_i$.
4. Conclude that the frame is **constant** ($de_\alpha/d\tau = 0$ for all $\alpha$) **iff** $A_0 = 0$ and $\vec\omega = 0$ — the characterisation of an **inertial observer**.

**Recall:**

![[Def - Local Frame and Four-Rotation#The four-rotation and its decomposition]]

The four-acceleration is $A_0 = dU_0/d\tau$ with $A_0\cdot U_0 = 0$ ([[Def - Four-Velocity and Four-Acceleration|four-acceleration]]). Indices are raised and lowered with $\eta$ ([[Def - Metric Duality and Index Manipulation|metric duality]]): $\Omega_{\alpha\beta} = \eta_{\alpha\mu}\Omega^\mu{}_\beta$, with $\eta_{00} = +1$, $\eta_{ii} = -1$. The bilinear form is $\underline\Omega(e_\alpha, e_\beta) = e_\alpha\cdot\Omega(e_\beta) = \Omega_{\alpha\beta}$.

---

# Convergent Strategy

**Problem class.** A *derive-a-constraint-and-classify* problem: prove the four-rotation is antisymmetric, translate to components, and use the decomposition to characterise inertial observers. The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] is to differentiate the constant orthonormality and then split the four-rotation into its acceleration and rotation parts.

**Assumption pattern.** The constant orthonormality $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$ is the key input; differentiating it forces antisymmetry. The subtlety is the index placement — antisymmetry holds with *both indices down*, not in mixed position, because the metric is indefinite. The signpost is "frame carried orthonormally" — its derivative is governed by an antisymmetric form.

**Theorem routing.** Part 1: $\frac{d}{d\tau}(e_\alpha\cdot e_\beta) = 0$ gives $\underline\Omega(e_\alpha, e_\beta) + \underline\Omega(e_\beta, e_\alpha) = 0$. Part 2: lower the index with $\eta$ and track the signs, $\Omega_{\alpha\beta} = \eta_{\alpha\mu}\Omega^\mu{}_\beta$, to get the mixed-index relations. Part 3: apply the [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|decomposition theorem]] with the electric part pinned to $A_0$. Part 4: read off that all $de_\alpha/d\tau$ vanish iff both $A_0$ and $\vec\omega$ vanish.

**Key decision point.** The crux of Part 2 is that "antisymmetric bilinear form" ($\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$) is a statement about *lowered* indices, and in mostly-minus signature lowering the first index of $\Omega^\beta{}_\alpha$ introduces a sign that differs between time and space components — so the mixed-index $\Omega^\beta{}_\alpha$ is *not* antisymmetric, and the relations split into the $\Omega^i{}_0 = +\Omega^0{}_i$ (boost) and $\Omega^i{}_j = -\Omega^j{}_i$ (rotation) blocks. Missing this is the most common error.

---

# Legal Operations Used

1. **Differentiate an orthonormality identity to get an antisymmetry** (operation 7 from the topic page). Differentiating $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$ is the entire content of Part 1.

2. **Decompose an antisymmetric form into electric and magnetic parts** (operation 6 from the topic page). Part 3 applies the decomposition to $\underline\Omega$, with the electric part fixed to $A_0$.

3. **Read the four-acceleration and four-rotation off the frame evolution** (operation 9 from the topic page). Part 4 classifies the observer from the two pieces of $de_\alpha/d\tau$.

---

# Hints

> [!note]- Hint 1
> $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$ is constant in $\tau$. Differentiate: $0 = \frac{d}{d\tau}(e_\alpha\cdot e_\beta) = \frac{de_\alpha}{d\tau}\cdot e_\beta + e_\alpha\cdot\frac{de_\beta}{d\tau} = \Omega(e_\alpha)\cdot e_\beta + e_\alpha\cdot\Omega(e_\beta) = \underline\Omega(e_\beta, e_\alpha) + \underline\Omega(e_\alpha, e_\beta)$.

> [!note]- Hint 2
> Antisymmetry is $\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$ (both down). Now $\Omega_{\alpha\beta} = \eta_{\alpha\mu}\Omega^\mu{}_\beta$. For $\alpha = 0$: $\Omega_{0\beta} = +\Omega^0{}_\beta$; for $\alpha = i$: $\Omega_{i\beta} = -\Omega^i{}_\beta$. Apply $\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$ to the $00$, $0i$, $ij$ blocks and undo the lowering.

> [!note]- Hint 3
> The decomposition gives $\Omega(V) = (U_0\cdot V)A_0 - (A_0\cdot V)U_0 + \vec\omega\times_{U_0}V$. Plug $V = e_0 = U_0$ (using $U_0\cdot U_0 = 1$, $A_0\cdot U_0 = 0$, $\vec\omega\times_{U_0}U_0 = 0$) and $V = e_i$ (using $U_0\cdot e_i = 0$).

> [!note]- Hint 4
> $de_0/d\tau = A_0$ and $de_i/d\tau = -(A_0\cdot e_i)U_0 + \vec\omega\times_{U_0}e_i$. All four vanish iff $A_0 = 0$ (kills $de_0/d\tau$ and the first term of $de_i/d\tau$) and $\vec\omega = 0$ (kills the rotation term). That is the inertial observer.

---

# Solution

The exercise is a careful index computation with a classification payoff. Step 1 differentiates the orthonormality to get antisymmetry of the lowered form. Step 2 tracks the metric signs to find the mixed-index relations, which split into boost and rotation blocks. Step 3 applies the decomposition to write the frame evolution explicitly. Step 4 reads off the inertial-observer condition. The recurring move is differentiating a constant inner product.

**Step 1: The four-rotation form is antisymmetric.**

> [!note]- Derivation
> The orthonormality $g(e_\alpha, e_\beta) = e_\alpha\cdot e_\beta = \eta_{\alpha\beta}$ is **constant** along the worldline. Differentiate:
> $$0 = \frac{d}{d\tau}(e_\alpha\cdot e_\beta) = \frac{de_\alpha}{d\tau}\cdot e_\beta + e_\alpha\cdot\frac{de_\beta}{d\tau}.$$
> Using $de_\gamma/d\tau = \Omega(e_\gamma)$ and the definition $\underline\Omega(X, Y) = X\cdot\Omega(Y)$ together with the symmetry of $g$,
> $$0 = \Omega(e_\alpha)\cdot e_\beta + e_\alpha\cdot\Omega(e_\beta) = \underline\Omega(e_\beta, e_\alpha) + \underline\Omega(e_\alpha, e_\beta).$$
> Hence $\underline\Omega(e_\beta, e_\alpha) = -\underline\Omega(e_\alpha, e_\beta)$: the four-rotation bilinear form $\underline\Omega$ is **antisymmetric**, equivalently $\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$. This is the statement that the frame stays orthonormal — the dragging is by an infinitesimal Lorentz transformation.

**Step 2: Mixed-index relations in mostly-minus signature.**

> [!note]- Derivation
> Antisymmetry is $\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$ with *both indices lowered*. The mixed-index components are $\Omega^\mu{}_\beta$, related by $\Omega_{\alpha\beta} = \eta_{\alpha\mu}\Omega^\mu{}_\beta$ ([[Def - Metric Duality and Index Manipulation|metric duality]]). With $\eta_{00} = +1$, $\eta_{ii} = -1$ (no sum):
> $$\Omega_{0\beta} = +\Omega^0{}_\beta, \qquad \Omega_{i\beta} = -\Omega^i{}_\beta.$$
> Now apply $\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$ block by block:
> - **$(0,0)$:** $\Omega_{00} = -\Omega_{00}\Rightarrow\Omega_{00} = 0$, so $\Omega^0{}_0 = 0$.
> - **$(0,i)$:** $\Omega_{0i} = -\Omega_{i0}$, i.e. $\Omega^0{}_i = -(-\Omega^i{}_0) = \Omega^i{}_0$. So $\boxed{\Omega^i{}_0 = \Omega^0{}_i}$ — the boost block is **symmetric** in mixed indices.
> - **$(i,j)$:** $\Omega_{ij} = -\Omega_{ji}$, i.e. $-\Omega^i{}_j = -(-\Omega^j{}_i) = \Omega^j{}_i$, so $\boxed{\Omega^i{}_j = -\Omega^j{}_i}$ — the rotation block is antisymmetric.
> Thus the mixed-index $\Omega^\beta{}_\alpha$ is **not** antisymmetric: the time-space (boost) block is symmetric, $\Omega^i{}_0 = \Omega^0{}_i$, and only the space-space (rotation) block is antisymmetric, $\Omega^i{}_j = -\Omega^j{}_i$. This is the sign subtlety the indefinite metric forces — and it is exactly the split into a boost part (the four-acceleration) and a rotation part (the spatial rotation).

**Step 3: The frame evolution from the decomposition.**

> [!note]- Derivation
> By the [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|orthogonal decomposition]], with the electric part pinned to the four-acceleration ($\Omega(U_0) = A_0$, since $de_0/d\tau = A_0$) and the magnetic part the spatial rotation $\vec\omega$,
> $$\Omega(V) = (U_0\cdot V)A_0 - (A_0\cdot V)U_0 + \vec\omega\times_{U_0}V.$$
> For $V = e_0 = U_0$: $U_0\cdot U_0 = 1$, $A_0\cdot U_0 = 0$, $\vec\omega\times_{U_0}U_0 = 0$ (repeated $U_0$ in $\epsilon$), so
> $$\frac{de_0}{d\tau} = \Omega(U_0) = (1)A_0 - 0 + 0 = A_0,$$
> consistent with $A_0 = dU_0/d\tau$. For $V = e_i$ (so $U_0\cdot e_i = 0$):
> $$\frac{de_i}{d\tau} = \Omega(e_i) = 0\cdot A_0 - (A_0\cdot e_i)U_0 + \vec\omega\times_{U_0}e_i = -(A_0\cdot e_i)U_0 + \vec\omega\times_{U_0}e_i.$$
> The first term is the Fermi–Walker tilt (the spatial axis acquires a $U_0$-component proportional to the acceleration), the second is the spatial rotation at rate $\vec\omega$.

**Step 4: Inertial means non-accelerating and non-rotating.**

> [!note]- Derivation
> The frame is **constant** ($de_\alpha/d\tau = 0$ for all $\alpha$) iff both equations vanish:
> - $de_0/d\tau = A_0 = 0$ requires $A_0 = 0$;
> - $de_i/d\tau = -(A_0\cdot e_i)U_0 + \vec\omega\times_{U_0}e_i = 0$. If $A_0 = 0$ already, this reduces to $\vec\omega\times_{U_0}e_i = 0$ for all $i = 1,2,3$. Since the $e_i$ span the rest space and the cross product $\vec\omega\times_{U_0}(\cdot)$ vanishes on all of $U_0^\perp$ only when $\vec\omega = 0$ (the cross product with a nonzero $\vec\omega$ has a nonzero kernel of dimension one, not three), this forces $\vec\omega = 0$.
>
> Conversely, if $A_0 = 0$ and $\vec\omega = 0$, then $\Omega(V) = 0$ for all $V$, so $de_\alpha/d\tau = 0$. Therefore
> $$\frac{de_\alpha}{d\tau} = 0\ \forall\alpha \quad\Longleftrightarrow\quad A_0 = 0 \text{ and } \vec\omega = 0,$$
> which is exactly the definition of an **inertial observer**: zero four-acceleration *and* zero four-rotation. Note that "non-rotating" alone ($\vec\omega = 0$, $A_0\neq 0$) is *weaker*: the spatial axes do not spin, but the time axis still tilts ($de_0/d\tau = A_0\neq 0$), so the frame is not constant — that residual is pure Fermi–Walker transport, and integrating it gives Thomas precession.

> [!note]- Complete formal solution
> Differentiating $e_\alpha\cdot e_\beta = \eta_{\alpha\beta}$ gives $\underline\Omega(e_\alpha, e_\beta) + \underline\Omega(e_\beta, e_\alpha) = 0$, so $\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$ (antisymmetric, lowered). Lowering with $\eta$ ($\eta_{00} = +1$, $\eta_{ii} = -1$) gives $\Omega^0{}_0 = 0$, $\Omega^i{}_0 = \Omega^0{}_i$ (symmetric boost block), $\Omega^i{}_j = -\Omega^j{}_i$ (antisymmetric rotation block) — so the mixed-index form is not antisymmetric. The decomposition $\Omega(V) = (U_0\cdot V)A_0 - (A_0\cdot V)U_0 + \vec\omega\times_{U_0}V$ gives $de_0/d\tau = A_0$ and $de_i/d\tau = -(A_0\cdot e_i)U_0 + \vec\omega\times_{U_0}e_i$. All four vanish iff $A_0 = 0$ (kills $de_0/d\tau$ and the tilt) and $\vec\omega = 0$ (kills the rotation, since $\vec\omega\times_{U_0}$ annihilates all of $U_0^\perp$ only if $\vec\omega = 0$): the inertial observer. $\blacksquare$

---

# Key Takeaways

**Differentiating a constant inner product yields an antisymmetry for free — this is the single most productive move in frame kinematics.** The antisymmetry of the four-rotation is not assumed; it falls out of differentiating the orthonormality $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$, which is constant because the frame stays orthonormal. The same trick gives $A_0\cdot U_0 = 0$ (from $U_0\cdot U_0 = 1$) and keeps $\vec\omega$ in the rest space (from $\vec\omega\cdot U_0 = 0$). The transferable principle: whenever a frame or vector is constrained to a fixed inner-product value (orthonormality, unit norm, mutual orthogonality), the derivative of that constraint is a free linear relation — and these relations are the structural facts (antisymmetry of the generator, orthogonality of the acceleration) you most want. In Lie-theoretic terms, "orthonormal frame transported metrically" forces the generator into the Lie algebra $\mathfrak{so}(1,3)$, and antisymmetry *is* that membership.

**Antisymmetry lives in the lowered indices; the mixed-index form splits into a symmetric boost block and an antisymmetric rotation block.** A subtle but essential point: "$\underline\Omega$ is antisymmetric" means $\Omega_{\alpha\beta} = -\Omega_{\beta\alpha}$ with *both indices down*, and in the indefinite mostly-minus metric this does *not* translate to $\Omega^\beta{}_\alpha = -\Omega^\alpha{}_\beta$. Lowering the first index introduces $\eta_{\alpha\mu}$, which is $+1$ for time and $-1$ for space, so the time-space (boost) block comes out *symmetric* ($\Omega^i{}_0 = \Omega^0{}_i$) while only the space-space (rotation) block is antisymmetric ($\Omega^i{}_j = -\Omega^j{}_i$). This index bookkeeping is exactly the split into a boost part (the four-acceleration) and a rotation part (the spatial rotation), seen at the level of components. The diagnostic to carry forward: in an indefinite metric, never assume a "mixed-index" tensor inherits the symmetry of its fully-lowered form — track each index's metric sign, and the resulting block structure usually *is* the physically meaningful decomposition.

**Inertial is strictly stronger than non-rotating: it needs both the acceleration and the rotation to vanish.** The classification payoff is that the frame is constant iff $A_0 = 0$ *and* $\vec\omega = 0$ — two independent conditions, killing the boost block and the rotation block respectively. A merely *non-rotating* observer ($\vec\omega = 0$ but $A_0\neq 0$) still has an evolving frame, because the time axis tilts by the four-acceleration ($de_0/d\tau = A_0$); this residual is pure Fermi–Walker transport, and it produces Thomas precession on a closed orbit. The reusable distinction: "inertial" (geodesic, $A_0 = 0$, $\vec\omega = 0$) and "non-rotating" (Fermi–Walker, $\vec\omega = 0$ only) are different, and conflating them is a classic error. A freely-falling, non-spinning gyroscope in special relativity is both; an accelerated, non-spinning gyroscope is non-rotating but not inertial, and the difference is exactly the measurable Thomas precession. The two measurable quantities — acceleration (accelerometer) and rotation (gyroscope) — are precisely the two blocks of the four-rotation, and an observer is inertial only when both instruments read zero.
