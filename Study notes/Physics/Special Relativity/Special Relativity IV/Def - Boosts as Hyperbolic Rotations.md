---
type: definition
subject: special-relativity
prereqs:
  - "Def - Rapidity"
  - "Def - The Lorentz Group"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. A boost along $x$ acts on the $(t, x)$-plane and fixes $(y, z)$; we usually display only the $2\times 2$ $(t, x)$ block. The boost is parametrised by [[Def - Rapidity|rapidity]] $\varphi$ with $v = \tanh\varphi$, $\gamma = \cosh\varphi$, $\gamma v = \sinh\varphi$. An ordinary rotation of the $(x, y)$-plane by angle $\theta$ is $R[\theta]$. The metric is $\eta = \mathrm{diag}(1,-1,-1,-1)$, the Euclidean metric is $I = \mathrm{diag}(1,1)$ on a plane. The rotation generator is $J$ and the boost generator is $K$. Full registry on [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group]].

---

# Axiom Motivation

A reader meeting the boost matrix for the first time sees an unmotivated array of $\gamma$'s and $v$'s and is told to memorise it. The motivation here is to replace memorisation with a single structural fact: **the boost is the hyperbolic version of a rotation**, and once you accept that, the entire boost matrix is forced and never needs to be memorised again. This is not an analogy bolted on after the fact; it is the definition of what a boost *is*.

Start from what makes a rotation a rotation. An ordinary rotation of the $(x, y)$-plane is the linear map that preserves the Euclidean form $x^2 + y^2$ and the orientation — equivalently the matrix $R$ with $R^{\mathsf T} I\, R = I$ and $\det R = 1$. Solving these constraints gives the one-parameter family $R[\theta] = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$, where the trigonometric functions appear precisely because $\cos^2\theta + \sin^2\theta = 1$ is the identity that makes $R^{\mathsf T} I R = I$ hold. The angle $\theta$ is not put in by hand; it is the natural parameter on the circle of solutions.

Now make the one change that defines special relativity: replace the Euclidean form $x^2 + y^2$ by the Minkowski form $t^2 - x^2$, i.e. replace $I = \mathrm{diag}(1,1)$ by $\eta = \mathrm{diag}(1,-1)$. A boost (in the $(t,x)$-plane) is, by the [[Def - The Lorentz Group|definition of the Lorentz group]], the linear map preserving $t^2 - x^2$ and the orientation and time direction — the matrix $L$ with $L^{\mathsf T}\eta\, L = \eta$, $\det L = 1$, $L^0{}_0 \ge 1$. Solving *these* constraints gives a one-parameter family, but now the bookkeeping identity that must hold is $\cosh^2\varphi - \sinh^2\varphi = 1$ (the hyperbolic identity, the one with a minus sign, matching the minus sign in $\eta$). So the solutions are built from $\cosh$ and $\sinh$ instead of $\cos$ and $\sin$:
$$
\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}.
$$
The hyperbolic angle $\varphi$ is the [[Def - Rapidity|rapidity]], the natural parameter on the hyperbola of solutions, exactly as $\theta$ was the natural parameter on the circle. The boost matrix is not memorised; it is *derived* as "the rotation matrix with the metric's minus sign threaded through".

Why $\cosh, \sinh$ and not, say, $\cos, \sin$ with imaginary argument? The two descriptions coincide — $\cosh\varphi = \cos(i\varphi)$, $\sinh\varphi = -i\sin(i\varphi)$ — and the substitution $\theta = i\varphi$ literally turns a rotation into a boost. This is the "rotation by an imaginary angle" picture: a boost is a rotation through the imaginary angle $i\varphi$ in the plane spanned by time and a space direction. It is a correct and useful mnemonic, but it is best kept as a mnemonic: the honest statement is that both rotations and boosts are isometries of a quadratic form, circular for the definite form and hyperbolic for the indefinite one, and the real distinction is the *sign* of the form, not a detour through complex numbers.

The one place the analogy genuinely breaks must be stated, because mistaking a boost for a literal rotation causes errors. A rotation is *periodic* and *bounded*: $\cos, \sin$ never exceed $1$, $R[\theta + 2\pi] = R[\theta]$, and the rotation group is the compact circle. A boost is *non-periodic* and *unbounded*: $\cosh\varphi \to \infty$ as $\varphi \to \infty$, there is no wrap-around, and the boost "group" along a line is the non-compact real line. This is why velocity has a ceiling ($v = \tanh\varphi < 1$ always, approached only as $\varphi \to \infty$) whereas an angle simply comes back around. The unboundedness is the geometric fingerprint of the indefinite metric, and it is the single most important way a boost is *not* a rotation.

---

# The Definition

A **Lorentz boost as a hyperbolic rotation**: the boost along the $x$-axis with [[Def - Rapidity|rapidity]] $\varphi$ is the linear map of the $(t, x)$-plane
$$
\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix},
\qquad
\begin{pmatrix} t \\ x \end{pmatrix} = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}\begin{pmatrix} t' \\ x' \end{pmatrix},
$$
extended by the identity on the transverse $(y, z)$-plane. In velocity variables, using $\cosh\varphi = \gamma$ and $\sinh\varphi = \gamma v$,
$$
\Lambda[v] = \gamma\begin{pmatrix} 1 & v \\ v & 1 \end{pmatrix} = \begin{pmatrix} \gamma & \gamma v \\ \gamma v & \gamma \end{pmatrix},
\qquad \gamma = (1 - v^2)^{-1/2}.
$$
It satisfies $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ with $\eta = \mathrm{diag}(1,-1)$, has $\det\Lambda = \cosh^2\varphi - \sinh^2\varphi = 1$, and has $\Lambda^0{}_0 = \cosh\varphi \ge 1$, so it lies in the restricted Lorentz group $SO^+(1,3)$.

This is to be read against the ordinary **Euclidean rotation** of the $(x, y)$-plane,
$$
R[\theta] = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},
\qquad R^{\mathsf T} I\, R = I, \quad \det R = 1,
$$
the isometry of the *definite* form $x^2 + y^2$. The boost is obtained from the rotation by the substitutions $\cos\theta \to \cosh\varphi$, $\sin\theta \to \sinh\varphi$, together with the sign change in the upper-right entry (the rotation has $-\sin\theta$ there, the boost has $+\sinh\varphi$) — which is the substitution $I \to \eta$ carried down to the level of matrix entries.

**Generators (preview of the Lie-algebra split).** Differentiating each family at the identity gives its generator:
$$
J = \left.\frac{dR[\theta]}{d\theta}\right|_{\theta=0} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},
\qquad
K = \left.\frac{d\Lambda[\varphi]}{d\varphi}\right|_{\varphi=0} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
$$
Then $R[\theta] = \exp(\theta J)$ and $\Lambda[\varphi] = \exp(\varphi K)$, with $J^2 = -I$ (so the exponential sums to circular functions) and $K^2 = +I$ (so it sums to hyperbolic functions). In the full $\mathfrak{so}(1,3)$ there are three rotation generators $J_1, J_2, J_3$ (antisymmetric, generating the compact $SO(3)$) and three boost generators $K_1, K_2, K_3$ ($\eta$-symmetric, generating the non-compact boosts); the split of the six-dimensional Lorentz algebra into "rotations and boosts" is exactly this $J$ versus $K$ distinction.

---

# Categorical / Structural Definition

Structurally, a boost is an **isometry of the indefinite plane $(\mathbb{R}^2, \eta)$, $\eta = \mathrm{diag}(1,-1)$, lying in the identity component** — that is, an element of $SO^+(1,1)$. The whole content of "boost = hyperbolic rotation" is the parallel:
$$
\text{rotation} \in SO(2) = \mathrm{Isom}^+(\mathbb{R}^2, I),
\qquad
\text{boost} \in SO^+(1,1) = \mathrm{Isom}^+(\mathbb{R}^2, \eta).
$$
Both are the orientation-preserving isometry groups of a non-degenerate symmetric form on the plane; the first is compact (the circle $S^1$), the second is non-compact (the line $\mathbb{R}$). The exponential map sends the one-dimensional Lie algebra to the group in each case, and the difference $J^2 = -I$ versus $K^2 = +I$ is the difference between a generator that squares to $-1$ (rotating, periodic) and one that squares to $+1$ (boosting, hyperbolic). This is the cleanest possible illustration of how the *signature* of a metric, and nothing else, decides whether its isometries are circular or hyperbolic.

The eigenstructure makes the contrast vivid. A rotation $R[\theta]$ has complex eigenvalues $e^{\pm i\theta}$ on the unit circle and no real eigenvectors (for $\theta \neq 0, \pi$) — it spins every real direction. A boost $\Lambda[\varphi]$ has *real* eigenvalues $e^{\pm\varphi}$ and two real eigenvectors, namely the two null directions $(1, 1)$ and $(1, -1)$:
$$
\Lambda[\varphi]\begin{pmatrix} 1 \\ 1 \end{pmatrix} = e^{\varphi}\begin{pmatrix} 1 \\ 1 \end{pmatrix},
\qquad
\Lambda[\varphi]\begin{pmatrix} 1 \\ -1 \end{pmatrix} = e^{-\varphi}\begin{pmatrix} 1 \\ -1 \end{pmatrix}.
$$
The light cone $t = \pm x$ is the eigenbasis of every boost; a boost stretches one null ray by the factor $e^{\varphi}$ (the [[Def - Rapidity|Doppler]] factor $k = e^\varphi$) and shrinks the other by $e^{-\varphi}$, preserving their product $e^\varphi e^{-\varphi} = 1$ — which is exactly the invariance of $t^2 - x^2 = (t+x)(t-x)$. That a boost is *diagonal in null coordinates* (light-cone coordinates $u = t + x$, $w = t - x$, on which $\Lambda$ acts as $u \mapsto e^\varphi u$, $w \mapsto e^{-\varphi}w$) is the single most useful computational form of the boost, and it is the structural reason rapidities add: composing boosts multiplies the diagonal factors, $e^{\varphi_1}e^{\varphi_2} = e^{\varphi_1 + \varphi_2}$.

---

# Relate to Other Fields / Compression

**True name:** a boost is **"a rotation with $\cos, \sin$ replaced by $\cosh, \sinh$"**, equivalently **"the map that scales the two null directions by reciprocal factors $e^{\pm\varphi}$"**. The first form is the mnemonic for writing the matrix; the second is the form to compute with, because in light-cone coordinates a boost is diagonal and composition is multiplication of exponentials.

The construction is the special-relativistic instance of a general fact in the theory of indefinite-metric isometry groups: $SO^+(p, q)$ contains a compact part $SO(p) \times SO(q)$ (rotations within the timelike and within the spacelike subspaces) and non-compact "boost" directions mixing the two, and the boosts are always hyperbolic rotations in the mixed planes. For $SO^+(1, 3)$ the compact part is $SO(3)$ (spatial rotations) and the three boost directions mix the single time axis with each space axis. The same hyperbolic-rotation structure governs the boosts of higher-signature groups (e.g. $SO(2, 2)$ in twistor theory, $SO(4, 1)$ as the de Sitter group), where the "boosts" are again hyperbolic rotations in the mixed planes.

The "imaginary angle" identification $\theta = i\varphi$ connects to the **Wick rotation** of quantum field theory: rotating the time coordinate $t \to -i\tau$ (imaginary time) turns the Minkowski metric $dt^2 - dx^2$ into the Euclidean metric $-(d\tau^2 + dx^2)$, and turns boosts into ordinary $SO(2)$ rotations of the $(\tau, x)$-plane. The non-compactness of the Lorentz boost becomes the compactness of a Euclidean rotation under this analytic continuation, which is why Euclidean field theory is technically better behaved — the boost integrals that diverge in Minkowski signature become convergent angular integrals in Euclidean signature.

---

# Examples / Corollaries

**Is an instance — the standard boost.** With $\varphi = \tanh^{-1}(0.6) \approx 0.693$ ($v = 0.6$, $\gamma = 1.25$), the boost is $\Lambda = \begin{pmatrix} 1.25 & 0.75 \\ 0.75 & 1.25 \end{pmatrix}$, since $\sinh\varphi = \gamma v = 0.75$. Check: $\det = 1.5625 - 0.5625 = 1$, and $1.25^2 - 0.75^2 = 1$, so $\Lambda^{\mathsf T}\eta\Lambda = \eta$.

**Is an instance — the null eigenvectors.** For the same boost, the Doppler factor is $k = e^\varphi = \cosh\varphi + \sinh\varphi = 1.25 + 0.75 = 2$. The null vector $(1,1)$ is stretched to $(2, 2)$ and $(1,-1)$ is shrunk to $(0.5, -0.5)$. A light pulse moving in $+x$ has its frequency multiplied by $2$ and one moving in $-x$ divided by $2$ — the relativistic Doppler effect, read directly off the eigenvalues.

**Is an instance — the rotation it deforms.** Setting $\varphi = i\theta$ formally turns $\Lambda[\varphi]$ into $\begin{pmatrix} \cos\theta & i\sin\theta \\ i\sin\theta & \cos\theta \end{pmatrix}$, which is the rotation $R[\theta]$ after the change of variable $x \to ix$ (Wick rotation of the space axis). The boost and the rotation are the same matrix family viewed in real versus imaginary angle.

**Is NOT an instance — a Galilean shear.** The Galilean boost $\begin{pmatrix} 1 & 0 \\ -v & 1 \end{pmatrix}$ (sending $x \mapsto x - vt$, $t \mapsto t$) is a *shear*, not a hyperbolic rotation: it has the repeated eigenvalue $1$, fixes the entire $t$-axis pointwise on time, and does *not* preserve $t^2 - x^2$. It is the degenerate $\varphi \to 0$ tangent of a boost taken with $v$ fixed — the wrong limit. The honest non-relativistic limit is rapidity small, $\Lambda[\varphi] \approx I + \varphi K$, which to first order does look like a shear, but the exact boost curves the worldlines of the light cone while a shear leaves a horizontal line horizontal.

**Is NOT an instance — a pure rotation in the $(t,x)$-plane.** The Euclidean rotation $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ acting on $(t, x)$ does *not* satisfy $\Lambda^{\mathsf T}\eta\Lambda = \eta$ (it preserves $t^2 + x^2$, not $t^2 - x^2$), so it is not a Lorentz transformation at all. Mixing time and space with circular functions is exactly what is *forbidden*; only hyperbolic functions preserve the indefinite metric.

**Corollary — a boost has no rest direction in the plane but two invariant null lines.** Unlike a rotation (which fixes only the origin) and unlike a shear (which fixes a whole line pointwise), a boost fixes the two null *lines* setwise (scaling along them) but no nonzero vector pointwise. The fixed null lines are the light cone, which is why the light cone is the one geometric structure every boost respects.

**Calibration check.** You should be able to: (1) write down $\Lambda[\varphi]$ from scratch by starting from $R[\theta]$ and substituting $\cos \to \cosh$, $\sin \to \sinh$ with the sign pattern flipped; (2) verify $(1, \pm 1)$ are eigenvectors with eigenvalues $e^{\pm\varphi}$ and explain why this means the light cone is boost-invariant; (3) state, in one sentence each, the two ways a boost differs from a rotation (real vs complex eigenvalues; unbounded vs periodic).

---

# Unlocked by This

> [!tip] The Rotation–Boost Split of so(1,3) *(from the Lorentz Group as a Lie Group)*
> The generators $J$ (rotation, $J^2 = -I$) and $K$ (boost, $K^2 = +I$) introduced here are the building blocks of the full six-dimensional Lie algebra $\mathfrak{so}(1,3)$: three $J_i$ and three $K_i$. Their commutation relations $[J_i, J_j] = \epsilon_{ijk}J_k$, $[J_i, K_j] = \epsilon_{ijk}K_k$, $[K_i, K_j] = -\epsilon_{ijk}J_k$ split the algebra (over $\mathbb{C}$) into two commuting copies of $\mathfrak{su}(2)$ via $A_i = \tfrac12(J_i + iK_i)$, $B_i = \tfrac12(J_i - iK_i)$ — the $(j_A, j_B)$ labelling of all Lorentz representations. The boost-boost commutator producing a rotation ($[K_i, K_j] = -\epsilon_{ijk}J_k$) is the infinitesimal **Thomas rotation**. See [[Special Relativity X — The Lorentz Group as a Lie Group]].

> [!tip] Wick Rotation and Euclidean Field Theory *(from Quantum Field Theory)*
> The formal substitution $\varphi = i\theta$ that turns a boost into a rotation is, at the level of the time coordinate, the **Wick rotation** $t \to -i\tau$. It maps Minkowski-signature field theory to Euclidean-signature field theory, turning the non-compact Lorentz group into the compact rotation group $SO(4)$ and oscillatory path integrals $e^{iS}$ into convergent ones $e^{-S_E}$. This analytic continuation is the technical foundation of lattice field theory and of rigorous constructive quantum field theory.
