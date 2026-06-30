---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Law of Velocity Composition"
  - "Def - The Lorentz Group"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

Compose two pure Lorentz boosts in perpendicular directions and show that the result is *not* a pure boost but a boost composed with a spatial rotation — the **Wigner rotation**. Working with $c = 1$:

1. Let $B_x(\varphi)$ be a pure boost of rapidity $\varphi$ along $x$ and $B_y(\psi)$ a pure boost of rapidity $\psi$ along $y$. Write both as $4\times 4$ matrices (acting on $(t, x, y, z)$) and form the product $\Lambda = B_y(\psi)B_x(\varphi)$.
2. Show that $\Lambda$ is *not* symmetric, hence cannot be a pure boost (pure boosts are represented by symmetric matrices). Conclude that $\Lambda = B(\boldsymbol{\zeta})\,R(\omega)$ for some boost $B$ in a tilted direction and a spatial **rotation** $R$ by angle $\omega$ — the polar decomposition.
3. For *infinitesimal* boosts (small $\varphi, \psi$), compute the rotation angle $\omega$ to leading order and show $\omega \approx \tfrac12\varphi\psi \approx \tfrac12 V_x V_y$ (the lowest-order Wigner rotation).
4. Explain why this rotation is invisible in the collinear case and why it is the kinematic root of the statement "boosts do not form a subgroup of the Lorentz group".

**Recall:**

This exercise drills the non-collinear content of the velocity-composition law at the level of group elements.

![[Thm - Law of Velocity Composition#Statement]]

A pure boost of [[Def - Rapidity|rapidity]] $\varphi$ along $x$ acts in the $(t,x)$ plane as $t' = t\cosh\varphi + x\sinh\varphi$, $x' = t\sinh\varphi + x\cosh\varphi$, fixing $y, z$; it is a *symmetric* matrix. The [[Def - The Lorentz Group|Lorentz group]] is the set of $\Lambda$ with $\Lambda^{\mathsf T}\eta\Lambda = \eta$, $\eta = \mathrm{diag}(1,-1,-1,-1)$. A **pure boost** is a positive-definite symmetric Lorentz matrix; a **rotation** is a Lorentz matrix fixing $t$ and acting orthogonally on space. The **polar decomposition** of any restricted Lorentz transformation is $\Lambda = (\text{symmetric positive boost})\times(\text{orthogonal rotation})$, developed in [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Convergent Strategy

**Problem class.** A *structural* problem about the [[Def - The Lorentz Group|Lorentz group]]: show that a composition of group elements fails to close within a subset (the boosts), and extract the rotation that measures the failure. The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] flags that non-collinear composition carries a hidden rotation.

**Assumption pattern.** Two boosts in *perpendicular* directions — the perpendicularity is what guarantees a nonzero rotation (collinear boosts commute and produce no rotation). The matrices are explicit, so the route is direct computation: multiply, test symmetry, polar-decompose.

**Theorem routing.** The [[Thm - Law of Velocity Composition|velocity-composition law]] at the level of velocities predicts that the transverse part transforms with a $\Gamma_0$ factor; at the level of matrices this manifests as the asymmetry of the product $B_y B_x$. The route is: write the matrices, multiply, observe $\Lambda \ne \Lambda^{\mathsf T}$, and identify the antisymmetric (rotation) part. For the angle, linearise in the rapidities.

**Key decision point.** The crux is recognising that a *pure boost is symmetric*, so the asymmetry of the product is the whole signal — the moment $B_y B_x \ne (B_y B_x)^{\mathsf T}$, a rotation is forced. The natural error is to expect that two boosts compose to a boost (as they do in one dimension); the perpendicular case is precisely where this fails, and the decision is to look at the *matrix structure*, not just the resulting velocity, because the velocity alone hides the rotation.

---

# Legal Operations Used

1. **Apply velocity composition / boost composition** (operation 4 from the topic page), here at the level of the boost matrices rather than the velocities, to form the product $\Lambda = B_y B_x$.

2. **Switch to rapidity** (related to operation from [[Def - Rapidity]]), writing each boost via $\cosh, \sinh$ of its rapidity so that the matrix entries are clean and the small-angle expansion is transparent.

3. **Take a Galilean / small-parameter limit** (operation 9 from the topic page), linearising in $\varphi, \psi$ to extract the leading Wigner angle $\omega \approx \tfrac12\varphi\psi$.

---

# Hints

> [!note]- Hint 1
> Write $B_x(\varphi)$ as the $4\times 4$ matrix that is $\begin{pmatrix}\cosh\varphi & \sinh\varphi\\ \sinh\varphi & \cosh\varphi\end{pmatrix}$ in the $(t,x)$ block and identity in $(y,z)$; similarly $B_y(\psi)$ in the $(t,y)$ block. Multiply $B_y(\psi)B_x(\varphi)$ as $4\times 4$ matrices.

> [!note]- Hint 2
> Look at the $(x,y)$ and $(y,x)$ entries of the product. For a *symmetric* matrix they would be equal. Compute them: one is $0$ and the other is $\sinh\psi\sinh\varphi$ (or similar) — they differ. Since pure boosts are symmetric, $\Lambda$ is not a pure boost; the antisymmetric part of the spatial block is a rotation generator.

> [!note]- Hint 3
> For small $\varphi, \psi$: $\cosh \approx 1 + \cdot^2/2$, $\sinh \approx \cdot$. The spatial $(x,y)$–$(y,x)$ block of $\Lambda$, to leading order, is antisymmetric with off-diagonal $\pm\tfrac12\varphi\psi$ — the generator of a rotation by $\omega \approx \tfrac12\varphi\psi$. (The factor $\tfrac12$ is the Thomas factor; the full finite-rapidity formula is $\tan(\omega/2)$-type, derived in SR IX.)

> [!note]- Hint 4
> In the collinear case both boosts are in the same plane (say $(t,x)$), they commute, and their product is again a symmetric boost matrix — no antisymmetric spatial part, no rotation. The rotation appears only when the two boost planes are *different*, which is why it is a genuinely $\ge 2$-dimensional, non-collinear effect. Its existence means $\{$boosts$\}$ is not closed under composition, hence not a subgroup.

---

# Solution

The Wigner rotation is the rotation hidden in the product of two non-collinear boosts. Step 1 writes the boost matrices and their product; Step 2 detects the rotation through the asymmetry of the product (pure boosts being symmetric); Step 3 extracts the leading angle $\omega \approx \tfrac12\varphi\psi$; Step 4 explains the collinear invisibility and the subgroup failure. The non-obvious move is to read the *matrix asymmetry* as the rotation, rather than tracking only the composed velocity, which conceals it.

**Step 1: The boost matrices and their product.**

> [!note]- Derivation
> Order coordinates $(t, x, y, z)$. The boost of rapidity $\varphi$ along $x$:
> $$B_x(\varphi) = \begin{pmatrix} \cosh\varphi & \sinh\varphi & 0 & 0\\ \sinh\varphi & \cosh\varphi & 0 & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\end{pmatrix},\qquad B_y(\psi) = \begin{pmatrix} \cosh\psi & 0 & \sinh\psi & 0\\ 0 & 1 & 0 & 0\\ \sinh\psi & 0 & \cosh\psi & 0\\ 0 & 0 & 0 & 1\end{pmatrix}.$$
> Their product $\Lambda = B_y(\psi)B_x(\varphi)$ (apply $B_x$ first, then $B_y$), restricted to the $(t,x,y)$ block (the $z$-row/column is trivial), is
> $$\Lambda = \begin{pmatrix} \cosh\psi\cosh\varphi & \cosh\psi\sinh\varphi & \sinh\psi\\ \sinh\varphi & \cosh\varphi & 0\\ \sinh\psi\cosh\varphi & \sinh\psi\sinh\varphi & \cosh\psi\end{pmatrix}.$$
> (Computed by ordinary matrix multiplication: e.g. the $(t,t)$ entry is $\cosh\psi\cdot\cosh\varphi + 0 + \sinh\psi\cdot 0 = \cosh\psi\cosh\varphi$; the $(t,y)$ entry is $\cosh\psi\cdot 0 + 0 + \sinh\psi\cdot 1 = \sinh\psi$; the $(y,x)$ entry is $\sinh\psi\cdot\sinh\varphi + 0 + \cosh\psi\cdot 0 = \sinh\psi\sinh\varphi$; the $(x,y)$ entry is $\sinh\varphi\cdot 0 + \cosh\varphi\cdot 0 + 0\cdot\cosh\psi = 0$.)

**Step 2: The product is not a pure boost.**

> [!note]- Derivation
> A pure boost is represented by a *symmetric* matrix (the boost in any direction is symmetric: it equals its own transpose, as $B_x, B_y$ visibly do). Test $\Lambda$ for symmetry by comparing the $(x,y)$ and $(y,x)$ spatial entries:
> $$\Lambda_{xy} = 0, \qquad \Lambda_{yx} = \sinh\psi\sinh\varphi.$$
> These are unequal (for nonzero rapidities), so $\Lambda \ne \Lambda^{\mathsf T}$: $\Lambda$ is **not symmetric**, hence **not a pure boost**. By the [[Special Relativity IX — The Lorentz Group, Structure and Classification|polar decomposition]], every restricted Lorentz transformation factors uniquely as $\Lambda = B\,R$ with $B$ a symmetric positive boost and $R$ a spatial rotation. Since $\Lambda$ is not symmetric, $R \ne I$: a genuine rotation is present. The antisymmetric part of the spatial $(x,y)$ block, $\tfrac12(\Lambda_{yx} - \Lambda_{xy}) = \tfrac12\sinh\psi\sinh\varphi$, is the seed of the rotation generator.

**Step 3: The leading rotation angle.**

> [!note]- Derivation
> Expand for small rapidities $\varphi, \psi$ (so $\sinh\approx\cdot$, $\cosh\approx 1 + \cdot^2/2$). The spatial $2\times 2$ block (rows/columns $x, y$) of $\Lambda$ is
> $$\begin{pmatrix} \cosh\varphi & 0\\ \sinh\psi\sinh\varphi & \cosh\psi\end{pmatrix} \approx \begin{pmatrix} 1 + \varphi^2/2 & 0\\ \psi\varphi & 1 + \psi^2/2\end{pmatrix}.$$
> Its antisymmetric part is $\begin{pmatrix} 0 & -\tfrac12\psi\varphi\\ \tfrac12\psi\varphi & 0\end{pmatrix}$ to leading order (symmetrising: the off-diagonal $\psi\varphi$ splits into a symmetric $\tfrac12\psi\varphi$ shared with the missing $(x,y)$ entry, leaving antisymmetric part $\pm\tfrac12\psi\varphi$). This is the generator of a rotation in the $(x,y)$ plane by angle
> $$\omega \approx \frac{1}{2}\varphi\psi \approx \frac{1}{2}V_x V_y,$$
> using $\varphi \approx V_x$, $\psi \approx V_y$ for small velocities. The factor $\tfrac12$ is the celebrated **Thomas factor**; the full finite-rapidity result (derived in [[Special Relativity IX — The Lorentz Group, Structure and Classification]]) reduces to this at small angles.

**Step 4: Collinear invisibility and the subgroup failure.**

> [!note]- Derivation
> If the two boosts were *collinear* — both along $x$, say — their product would be $B_x(\varphi)B_x(\varphi') = B_x(\varphi + \varphi')$, a single boost (rapidities add), with a *symmetric* matrix and *no* antisymmetric spatial part: no rotation. The rotation appears only because the two boost planes $(t,x)$ and $(t,y)$ are *different*, so the product mixes the spatial directions $x, y$ asymmetrically. This is a genuinely multi-dimensional effect, absent in $1+1$ dimensions.
>
> The structural consequence: the product of two boosts is, in general, *not* a boost (it is boost $\times$ rotation). So the set of pure boosts is **not closed under composition** — it is not a subgroup of the [[Def - The Lorentz Group|Lorentz group]]. The rotation $R$ is exactly the obstruction to closure. Accumulated continuously around a closed loop in velocity space, these infinitesimal rotations integrate to the **Thomas precession**, the relativistic correction to spin–orbit coupling. The velocity-composition law's transverse $\Gamma_0$ factor was the kinematic shadow of this rotation; here it appears explicitly as the antisymmetric matrix entry.

> [!note]- Complete formal solution
> With $B_x(\varphi), B_y(\psi)$ the perpendicular boost matrices, the product $\Lambda = B_y(\psi)B_x(\varphi)$ has spatial entries $\Lambda_{xy} = 0 \ne \sinh\psi\sinh\varphi = \Lambda_{yx}$, so $\Lambda$ is not symmetric and hence not a pure boost. By the polar decomposition $\Lambda = BR$ with $B$ symmetric positive and $R$ a rotation, $R \ne I$: a Wigner rotation is present, with generator the antisymmetric spatial part $\tfrac12\sinh\psi\sinh\varphi$. Linearising in the rapidities gives the rotation angle $\omega \approx \tfrac12\varphi\psi \approx \tfrac12 V_x V_y$. Collinear boosts commute and produce a symmetric product (no rotation), so the effect is intrinsically non-collinear; its existence shows the boosts are not closed under composition, hence not a subgroup of the Lorentz group, and its accumulation is the Thomas precession. $\blacksquare$

---

# Key Takeaways

**A pure boost is symmetric, so the asymmetry of a product of boosts is the rotation — read the matrix, not just the velocity.** The decisive diagnostic of this problem is that pure boosts are represented by symmetric matrices, so any departure from symmetry in a composition is a rotation, full stop. Tracking only the *resulting velocity* of a double boost hides this entirely — the velocity is just a vector, and a vector cannot show you the rotation of the frame that carries it. The reusable principle: when composing Lorentz transformations and asking whether the result is "just a boost", compute the product matrix and test its symmetry; the antisymmetric spatial part *is* the Wigner rotation generator. This is the cleanest detector of the effect and generalises to any number of boosts. The same lesson — that orientation information lives in the antisymmetric part and is invisible at the level of the transported vector — recurs throughout the [[Special Relativity IX — The Lorentz Group, Structure and Classification|structure theory]] of the Lorentz group.

**The Wigner rotation is a genuinely non-collinear, $\ge 2$-dimensional effect, which is why it is missed in the standard one-dimensional treatments.** Almost every introduction to velocity addition works in one dimension, where boosts commute and compose to boosts, so the rotation never appears and the student internalises "boosts compose to boosts" as a general truth. It is false the moment two boost directions differ. The trigger to watch for: any problem that composes boosts in *different directions*, or tracks an orientation (a gyroscope, a spin, a frame) across a sequence of boosts, must account for the Wigner rotation, or it will silently get the orientation wrong. This is the kinematic source of the factor-of-two "Thomas correction" that famously fixed the spin–orbit coupling in atomic physics — a correction that is invisible in any one-dimensional model and that puzzled physicists until Thomas identified its relativistic-kinematic origin.

**Failure of closure is measured by a group element, and that element is physically real.** The boosts not forming a subgroup is not a dry algebraic curiosity — the obstruction to closure is the rotation $R$, and $R$ has observable consequences (the Thomas precession of a spin, a real shift in atomic energy levels). This illustrates a general and transferable idea: when a set of transformations fails to be closed, the "defect" of the composition (here boost $\times$ rotation, with the rotation as defect) is itself a meaningful object, often carrying physics. In the [[Def - The Lorentz Group|Lorentz group]] the defect lands in the rotation subgroup; the systematic statement is that the boosts are a *symmetric space*, not a subgroup, and the rotation is the holonomy of the associated connection — the same holonomy that, in [[Riemannian Geometry III — Riemann Curvature and Topology|curved-space language]], is curvature. The lesson is to treat closure-failure not as a nuisance but as a source of structure, and to identify *which* element measures it.
