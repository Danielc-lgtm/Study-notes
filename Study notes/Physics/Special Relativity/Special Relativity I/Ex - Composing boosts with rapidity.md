---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Rapidity"
  - "Def - The Lorentz Group"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c = 1$, in $1+1$ dimensions.

1. Write the boost $\Lambda[v]$ acting on $(t,x)$ as a $2\times 2$ matrix in velocity variables, then re-express it in [[Def - Rapidity|rapidity]] variables and verify it has the hyperbolic-rotation form $\begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$.
2. By multiplying matrices, show directly that $\Lambda[\varphi_1]\,\Lambda[\varphi_2] = \Lambda[\varphi_1+\varphi_2]$ — collinear boosts compose by adding rapidities.
3. Deduce the relativistic velocity-addition formula $u = (u'+v)/(1+u'v)$ from rapidity addition.
4. **The relativistic rocket.** A rocket fires its engine in $n$ identical bursts; each burst increases its speed by $w$ as measured in the rocket's instantaneous rest frame just before that burst. Find the rocket's final speed in the launch frame, and show that as $n \to \infty$ the speed approaches but never reaches $c$.

**Recall:**

The exercise rests on rapidity and the group structure of boosts.

![[Def - Rapidity#The Definition]]

A [[Def - The Lorentz Group|boost]] is an element of the Lorentz group; collinear boosts form a one-parameter subgroup. The [[Thm - Relativistic Velocity Addition|velocity-addition law]] is what rapidity addition becomes in velocity variables.

---

# Convergent Strategy

**Problem class.** A *structural* problem — verifying the group law of boosts — followed by a *compute-an-effect* problem (the rocket). The [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|topic strategy]] says: when boosts must be composed, switch to rapidity, where the group law is addition.

**Assumption pattern.** Several boosts are to be composed. The signpost "compose boosts" points straight at rapidity — the coordinate in which composition is a sum.

**Theorem routing.** Part 1: rewrite $\gamma, \gamma v$ as $\cosh\varphi, \sinh\varphi$. Part 2: multiply the two hyperbolic-rotation matrices and apply the $\cosh, \sinh$ addition formulas. Part 3: $u = \tanh\varphi_u = \tanh(\varphi_1+\varphi_2)$, expanded. Part 4: each burst adds a fixed rapidity, so $n$ bursts give rapidity $n\varphi_w$ and speed $\tanh(n\varphi_w)$.

**Key decision point.** The non-obvious move is part 4's reframing: a burst that adds a fixed *velocity* $w$ in the current rest frame adds a fixed *rapidity* $\varphi_w = \tanh^{-1}w$ in every frame, because rapidity differences are what compose additively. Velocity increments do not add; rapidity increments do.

---

# Legal Operations Used

1. **Switch to rapidity to make boosts additive.** The whole exercise is this operation: rapidity turns the boost subgroup into $(\mathbb{R},+)$.

2. **Apply the Lorentz transformation in matrix form** and multiply matrices to compose boosts.

3. **Add velocities relativistically** — derived in part 3 as $\tanh$ of a rapidity sum.

4. **Compute an invariant / use the group law** — part 4 uses that each burst contributes the same rapidity regardless of the frame it is described in.

---

# Hints

> [!note]- Hint 1
> The boost is $\Lambda[v] = \gamma\begin{pmatrix}1 & v\\v & 1\end{pmatrix} = \begin{pmatrix}\gamma & \gamma v\\\gamma v & \gamma\end{pmatrix}$ (taking the $S' \to S$ sign convention). Now use $\gamma = \cosh\varphi$ and $\gamma v = \sinh\varphi$ — these are consistent because $\gamma^2 - (\gamma v)^2 = 1 = \cosh^2\varphi - \sinh^2\varphi$.

> [!note]- Hint 2
> Multiply $\begin{pmatrix}\cosh\varphi_1 & \sinh\varphi_1\\\sinh\varphi_1 & \cosh\varphi_1\end{pmatrix}\begin{pmatrix}\cosh\varphi_2 & \sinh\varphi_2\\\sinh\varphi_2 & \cosh\varphi_2\end{pmatrix}$. Each entry of the product is a sum of two terms; recognise them as the right-hand sides of $\cosh(\varphi_1+\varphi_2)$ and $\sinh(\varphi_1+\varphi_2)$.

> [!note]- Hint 3
> The combined boost has rapidity $\varphi_1+\varphi_2$, so the combined velocity is $u = \tanh(\varphi_1+\varphi_2)$. Apply $\tanh(a+b) = (\tanh a + \tanh b)/(1+\tanh a\tanh b)$ and substitute $\tanh\varphi_i = v_i$.

> [!note]- Hint 4
> Each burst adds speed $w$ in the rocket's current rest frame. "Add speed $w$ in the current rest frame" means "compose with a boost of rapidity $\varphi_w = \tanh^{-1}w$". Since rapidities add, $n$ bursts give total rapidity $n\varphi_w$. The final speed is $\tanh(n\varphi_w)$. As $n\to\infty$, $n\varphi_w \to \infty$ and $\tanh(n\varphi_w) \to 1$.

---

# Solution

In rapidity, the boost subgroup is just $(\mathbb{R},+)$: a boost is a hyperbolic rotation, composition is addition, and every awkward velocity formula is the image of a simple statement about rapidities under $v = \tanh\varphi$.

**Step 1: The boost is a hyperbolic rotation.**

> [!note]- Derivation
> In velocity variables, the boost (with the $S'\to S$ sign convention) acting on $(t,x)^{\mathsf T}$ is
> $$\Lambda[v] = \begin{pmatrix}\gamma & \gamma v\\\gamma v & \gamma\end{pmatrix}, \qquad \gamma = \frac{1}{\sqrt{1-v^2}}.$$
> The [[Def - The Lorentz Group|boost condition]] $\Lambda^{\mathsf T}\eta\Lambda = \eta$ forces $\gamma^2 - (\gamma v)^2 = 1$. This is identical in form to the hyperbolic identity $\cosh^2\varphi - \sinh^2\varphi = 1$, so there is a unique [[Def - Rapidity|rapidity]] $\varphi$ with
> $$\gamma = \cosh\varphi, \qquad \gamma v = \sinh\varphi, \qquad\text{hence}\qquad v = \frac{\gamma v}{\gamma} = \tanh\varphi.$$
> Substituting,
> $$\Lambda[\varphi] = \begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}.$$
> This is the rotation matrix $\begin{pmatrix}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{pmatrix}$ with circular functions replaced by hyperbolic ones and the sign pattern adjusted: a **hyperbolic rotation** of the $(t,x)$-plane. A boost is a rotation between time and space.

**Step 2: Boosts compose by adding rapidities.**

> [!note]- Derivation
> Multiply two boosts:
> $$\Lambda[\varphi_1]\Lambda[\varphi_2] = \begin{pmatrix}\cosh\varphi_1 & \sinh\varphi_1\\\sinh\varphi_1 & \cosh\varphi_1\end{pmatrix}\begin{pmatrix}\cosh\varphi_2 & \sinh\varphi_2\\\sinh\varphi_2 & \cosh\varphi_2\end{pmatrix}.$$
> The top-left entry is $\cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2 = \cosh(\varphi_1+\varphi_2)$. The top-right is $\cosh\varphi_1\sinh\varphi_2 + \sinh\varphi_1\cosh\varphi_2 = \sinh(\varphi_1+\varphi_2)$. By symmetry the bottom row gives $\sinh(\varphi_1+\varphi_2)$ and $\cosh(\varphi_1+\varphi_2)$. Hence
> $$\Lambda[\varphi_1]\Lambda[\varphi_2] = \begin{pmatrix}\cosh(\varphi_1+\varphi_2) & \sinh(\varphi_1+\varphi_2)\\\sinh(\varphi_1+\varphi_2) & \cosh(\varphi_1+\varphi_2)\end{pmatrix} = \Lambda[\varphi_1+\varphi_2].$$
> Composition of collinear boosts is addition of rapidities. The map $\varphi \mapsto \Lambda[\varphi]$ is a group isomorphism from $(\mathbb{R},+)$ onto the proper orthochronous boost subgroup $SO^+(1,1)$.

**Step 3: The velocity-addition formula.**

> [!note]- Derivation
> A particle moving at $u'$ in $S'$ ($S'$ moving at $v$ relative to $S$) corresponds, in $S$, to the composite boost $\Lambda[\varphi_{u'}]\Lambda[\varphi_v] = \Lambda[\varphi_{u'}+\varphi_v]$ from Step 2. So the particle's velocity in $S$ is
> $$u = \tanh(\varphi_{u'} + \varphi_v).$$
> Apply the hyperbolic tangent addition formula $\tanh(a+b) = \dfrac{\tanh a + \tanh b}{1+\tanh a\tanh b}$ with $\tanh\varphi_{u'} = u'$, $\tanh\varphi_v = v$:
> $$u = \frac{u' + v}{1 + u'v}.$$
> This is [[Thm - Relativistic Velocity Addition|relativistic velocity addition]] — the messy formula is just $\tanh$ of a sum.

**Step 4: The relativistic rocket.**

> [!note]- Derivation
> Each engine burst increases the rocket's speed by $w$ *as measured in the rocket's instantaneous rest frame*. In rapidity, "compose with a boost that has velocity $w$ in the current frame" means "add the rapidity $\varphi_w = \tanh^{-1}w$" — and this added rapidity is the *same number* whichever frame describes the burst, because rapidity *differences* compose additively (Step 2). So:
>
> - After $1$ burst: total rapidity $\varphi_w$.
> - After $2$ bursts: $2\varphi_w$.
> - After $n$ bursts: total rapidity $n\varphi_w$.
>
> The rocket's final speed in the launch frame is
> $$v_n = \tanh(n\varphi_w) = \tanh\big(n\tanh^{-1}w\big).$$
> As $n \to \infty$, the argument $n\varphi_w \to \infty$, and since $\tanh \to 1$ at infinity,
> $$v_n \longrightarrow 1 = c, \qquad\text{but } v_n < 1 \text{ for every finite } n.$$
> The speed climbs towards $c$ and never reaches it. Contrast the Newtonian prediction $nw$, which grows without bound and passes $c$ at $n = \lceil c/w\rceil$. The rapidity, the genuinely additive quantity, *does* grow without bound — it is the velocity, its $\tanh$, that is trapped below $c$. Each successive burst buys less and less speed even though it always buys the same rapidity.

> [!note]- Complete formal solution
> The boost $\Lambda[v] = \begin{pmatrix}\gamma & \gamma v\\\gamma v & \gamma\end{pmatrix}$ satisfies $\gamma^2-(\gamma v)^2 = 1$, so setting $\gamma = \cosh\varphi$, $\gamma v = \sinh\varphi$ (consistent, and giving $v = \tanh\varphi$) yields $\Lambda[\varphi] = \begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$. Multiplying two such matrices and using the $\cosh,\sinh$ addition formulas gives $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1+\varphi_2]$. Hence a particle at $u'$ in $S'$ (itself at $v$ in $S$) has $S$-velocity $u = \tanh(\varphi_{u'}+\varphi_v) = (u'+v)/(1+u'v)$. For the rocket, each burst adds rapidity $\varphi_w = \tanh^{-1}w$, so $n$ bursts give rapidity $n\varphi_w$ and speed $v_n = \tanh(n\tanh^{-1}w) \to 1$ as $n\to\infty$, with $v_n < 1$ always. $\blacksquare$

---

# Key Takeaways

**Rapidity is the right coordinate on the boost subgroup, and "switch to rapidity" is the move whenever boosts must be composed.** Velocity is a bad coordinate: the group law, written in velocity, is the nonlinear $(u'+v)/(1+u'v)$. Rapidity is the good coordinate: the group law is plain addition. This is the same lesson as parametrising rotations by angle rather than by, say, the matrix entry $\cos\theta$ — there is always a canonical coordinate on a one-parameter group in which composition is a sum, and finding it converts hard composition problems into arithmetic. The trigger is unmistakable: any time a problem stacks two or more boosts, or asks for the result of an iterated boost, change variables to rapidity, add, and change back at the end. The famous velocity-addition formula is then not something to memorise but something to *derive* in one line from $\tanh$ of a sum.

**A boost is a hyperbolic rotation, and that single identification organises the whole of §1.2.** Writing the boost matrix as $\begin{pmatrix}\cosh\varphi & \sinh\varphi\\\sinh\varphi & \cosh\varphi\end{pmatrix}$ makes the analogy with rotations exact: same matrix shape, circular functions traded for hyperbolic ones. Every structural fact about boosts is then the corresponding fact about rotations, read through that trade. Composition adds the parameter (angles for rotations, rapidities for boosts). The inverse negates it. The group is one-dimensional. The only structural difference is compactness — rotations close up into a circle, boosts run off to infinity along a line — and that difference is exactly why a rotation angle is periodic while a rapidity is unbounded, hence why velocity saturates at $c$ rather than oscillating. Carry the rotation analogy everywhere; it fails only at the signature, and the signature is the one thing to keep track of.

**Velocity increments do not add, but rapidity increments do — and that is why $c$ is unreachable.** The rocket makes the point sharply. Each burst is engineered to add the same *velocity* $w$ in the current rest frame, and a Newtonian would conclude the speed grows by $w$ each time, without limit. But "the same velocity in the current frame" is "the same rapidity", and it is rapidity that accumulates: $n$ bursts give rapidity $n\varphi_w$, which grows without bound, while the velocity $\tanh(n\varphi_w)$ creeps towards $c$ and stops. The speed of light is unattainable not because some force fails but because the additive quantity is rapidity, and $c$ is rapidity infinity — a finite number of finite rapidity increments is always finite. This is the kinematic seed of the dynamical fact, developed in **Special Relativity II**, that a constant force produces hyperbolic motion: it pumps rapidity in at a constant rate, and the velocity asymptotes. Whenever something "should" reach $c$ by repeated boosting and does not, the resolution is that you have been adding the wrong quantity.
