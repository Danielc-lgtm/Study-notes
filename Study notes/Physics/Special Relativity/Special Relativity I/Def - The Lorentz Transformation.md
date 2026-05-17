---
type: definition
subject: special-relativity
prereqs:
  - "Def - Inertial Frame and the Postulates of Special Relativity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Two inertial frames $S$ (coordinates $t, x, y, z$) and $S'$ (coordinates $t', x', y', z'$) are in relative motion: $S'$ moves at velocity $v$ along the common $x$-axis of $S$, and the origins coincide, so the event $(0,0,0,0)$ of $S$ is the event $(0,0,0,0)$ of $S'$. The **Lorentz factor** is $\gamma = \gamma_v = (1 - v^2)^{-1/2}$ (with $c$ restored, $\gamma = (1-v^2/c^2)^{-1/2}$). The full registry is on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Axiom Motivation

We need the formula relating $(t,x)$ to $(t',x')$, and the [[Def - Inertial Frame and the Postulates of Special Relativity|two postulates]] determine it almost completely. The strategy is to write down the most general transformation, then impose each physical fact in turn and watch the freedom shrink to nothing.

Start with the most general relation, $x' = f(x,t)$, $t' = g(x,t)$. The **first constraint is the law of inertia**: in both $S$ and $S'$ a free particle moves in a straight line at constant velocity, so its worldline is a straight line in the $(t,x)$-plane and must remain a straight line in the $(t',x')$-plane. A map that sends every straight line to a straight line and fixes the origin is, by definition, **linear**. So $f$ and $g$ are linear:
$$x' = \alpha_1 x + \alpha_2 t, \qquad t' = \alpha_3 x + \alpha_4 t,$$
with four coefficients, each possibly depending on $v$.

The **second constraint is the motion of the origin of $S'$**. The point $x' = 0$ is, by definition, where $S'$'s spatial origin sits, and that origin moves at velocity $v$ in $S$, tracing the worldline $x = vt$. So $x = vt$ must map to $x' = 0$, which forces $\alpha_1 x + \alpha_2 t = 0$ whenever $x = vt$, i.e. $\alpha_2 = -v\alpha_1$. Writing $\gamma$ for $\alpha_1$,
$$x' = \gamma(x - vt).$$
The coefficient $\gamma$ may still depend on $v$.

The **third constraint is the principle of relativity applied symmetrically**. Viewed from $S'$, the frame $S$ moves at velocity $-v$, and the identical argument gives $x = \gamma'(x' + vt')$ for some $\gamma'$. Now a short symmetry argument shows $\gamma' = \gamma$: the coefficient cannot depend on the *direction* of $v$, only on its magnitude, because nothing in the setup distinguishes left from right — flip the orientation of the $x$-axis and the roles of $\pm v$ swap while the physics is unchanged. Hence $\gamma_v = \gamma_{-v}$, so $\gamma' = \gamma_{-v} = \gamma_v = \gamma$.

The **fourth and decisive constraint is the constancy of light**. A light ray has $x = t$ in $S$ and must have $x' = t'$ in $S'$. Substitute $x = t$ into $x' = \gamma(x-vt)$ to get $x' = \gamma(1-v)t$; substitute $x' = t'$ into $x = \gamma(x'+vt')$ to get $x = \gamma(1+v)t'$. These two must be consistent with $x = t$ and $x' = t'$, and a line of algebra gives
$$\gamma = \frac{1}{\sqrt{1 - v^2}}.$$
This is the only value compatible with both postulates. Notice three things. For $v \ll 1$, $\gamma \approx 1$ and the transformation reduces to the Galilean one. As $v \to 1$, $\gamma \to \infty$. And for $v > 1$, $\gamma$ is imaginary — there is no inertial frame moving faster than light. The temporal law is then forced: substituting $x' = \gamma(x-vt)$ into $x = \gamma(x'+vt')$ and solving for $t'$ gives $t' = \gamma(t - vx)$.

What would break if we kept the Galilean clause $t' = t$? Then $\gamma = 1$ would be forced, and light could not travel at $c$ in both frames. Absolute time and the constancy of $c$ are incompatible; the Lorentz transformation is what you get when you sacrifice the former to keep the latter.

---

# The Definition

Let $S$ and $S'$ be inertial frames with coincident origins, $S'$ moving at velocity $v$ along the $x$-axis of $S$. The **Lorentz transformation** (a **boost** along $x$) relating their coordinates is, with $c = 1$,
$$
\boxed{\quad
x' = \gamma(x - vt), \qquad
t' = \gamma(t - vx), \qquad
y' = y, \qquad
z' = z,
\quad}
$$
where $\gamma = (1 - v^2)^{-1/2}$. Restoring $c$:
$$x' = \gamma(x - vt), \quad t' = \gamma\!\left(t - \tfrac{v}{c^2}x\right), \quad y' = y, \quad z' = z, \qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}.$$
In matrix form, writing the boost as acting on the column $(t, x)^{\mathsf T}$ (suppressing the untouched $y, z$),
$$
\begin{pmatrix} t' \\ x' \end{pmatrix}
= \Lambda[v] \begin{pmatrix} t \\ x \end{pmatrix},
\qquad
\Lambda[v] = \gamma\begin{pmatrix} 1 & -v \\ -v & 1 \end{pmatrix}
= \begin{pmatrix} \gamma & -\gamma v \\ -\gamma v & \gamma \end{pmatrix}.
$$
The **inverse transformation**, expressing $S$ coordinates in terms of $S'$, is obtained by replacing $v$ with $-v$ (since $S$ moves at $-v$ relative to $S'$):
$$x = \gamma(x' + vt'), \qquad t = \gamma(t' + vx').$$
A **general Lorentz transformation** is any composition of such boosts (along arbitrary directions) with spatial rotations; the boost above is the *standard* Lorentz transformation, and the [[Def - The Lorentz Group|Lorentz group]] is the set of all of them.

---

# Relate to Other Fields / Compression

A Lorentz transformation is a **linear change of coordinates** on $\mathbb{R}^4$ — the simplest object studied in [[Multivariate Analysis I — Differentiation in Several Variables]]. Because it is linear, its [[Def - Partial Derivatives and the Jacobian Matrix|Jacobian matrix]] is the constant matrix $\Lambda$ itself, the same at every event: there is no position dependence, no curvature. This is the precise sense in which special relativity is "flat" and needs no differential geometry — the coordinate changes are global linear maps, and the [[Thm - The Chain Rule|chain rule]] for composing them is just matrix multiplication. Compare the polar-coordinate change of [[Ex - The Jacobian of polar coordinates]], whose Jacobian varies from point to point; the Lorentz transformation is the rigid, constant-Jacobian extreme.

The transformation is also a **hyperbolic rotation**. Written in [[Def - Rapidity|rapidity]] variables, $\Lambda[\varphi] = \begin{pmatrix}\cosh\varphi & -\sinh\varphi\\-\sinh\varphi & \cosh\varphi\end{pmatrix}$, which is the rotation matrix $\begin{pmatrix}\cos\theta & -\sin\theta\\-\sin\theta & \cos\theta\end{pmatrix}$ with circular functions replaced by hyperbolic ones. The boost is the analogue, for the indefinite Minkowski form $t^2 - x^2$, of an ordinary rotation for the Euclidean form $x^2 + y^2$. This is the cleanest way to see what a boost "is": not a strange new operation but a rotation, performed in a plane containing the time axis, with respect to a metric that has a minus sign.

---

# Examples / Corollaries

**Is an instance — the Galilean transformation, as a limit.** Setting $c \to \infty$ (equivalently $v/c \to 0$) gives $\gamma \to 1$ and the Lorentz transformation degenerates to $x' = x - vt$, $t' = t$. The Galilean transformation is the low-speed approximation, not a separate theory; relativity contains Newtonian mechanics as the regime $\gamma \approx 1$.

**Is an instance — a light ray maps to a light ray.** Take the light ray $x = t$ in $S$. Then $x' = \gamma(t - vt) = \gamma t(1-v)$ and $t' = \gamma(t - vt) = \gamma t(1-v)$, so $x' = t'$: the ray travels at speed $1$ in $S'$ too. The transformation was *built* to do this, and checking it is the calibration that confirms the formula.

**Is an instance — the boost is its own inverse-up-to-sign.** Composing $\Lambda[v]$ with $\Lambda[-v]$ gives the identity: $\Lambda[-v]\Lambda[v] = I$. The check is a $2\times2$ matrix product using $\gamma^2(1 - v^2) = 1$. This is the first postulate made concrete — $S$ relates to $S'$ exactly as $S'$ relates to $S$, with $v \to -v$.

**Is NOT an instance — $x' = x - vt$, $t' = t$ for $v$ not small.** The Galilean transformation is not a Lorentz transformation: it fails the light-ray check (a $45^\circ$ ray maps to a non-$45^\circ$ line) and it does not preserve the [[Def - The Spacetime Interval|interval]]. It is the correct transformation only in the unphysical limit $c = \infty$.

**Is NOT an instance — a transformation with $v > 1$.** For $|v| > 1$ the factor $\gamma = (1-v^2)^{-1/2}$ is imaginary; there is no real Lorentz transformation, and hence no inertial frame, moving faster than light. The light speed barrier is built into the formula.

**Corollary — transverse directions are untouched.** The boost leaves $y$ and $z$ unchanged: contraction and the mixing of coordinates happen only along the direction of motion. A symmetry argument (transverse lengths cannot change, or both observers would disagree about whether a moving ring fits through a hoop) forces $y' = y$, $z' = z$.

**Corollary — the determinant of a boost is $1$.** $\det\Lambda[v] = \gamma^2 - \gamma^2 v^2 = \gamma^2(1-v^2) = 1$. So a boost is a *proper* Lorentz transformation, an element of $SO(1,3)$; it neither reflects space nor reverses time.

---

# Unlocked by This

> [!tip] The Lorentz Group *(from §1.2)*
> The boosts, together with spatial rotations, generate the **Lorentz group** $O(1,3)$ ([[Def - The Lorentz Group]]) — the group of all linear maps preserving the spacetime interval. The single boost defined here is one element; the group is the whole symmetry structure of Minkowski space.

> [!tip] Length Contraction and Time Dilation *(from §1.1)*
> Applying the Lorentz transformation to the endpoints of a rod gives [[Ex - Length contraction|length contraction]]; applying it to the ticks of a clock gives [[Ex - Time dilation|time dilation]]. Both famous effects are immediate corollaries of this one formula.
