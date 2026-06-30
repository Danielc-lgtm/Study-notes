---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Thomas Rotation Angle"
  - "Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation"
  - "Thm - Polar Decomposition of the Lorentz Group"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, in an orthonormal frame $(e_0, e_1, e_2, e_3)$. Let $\Lambda_1$ be a boost of speed $V_1$ (Lorentz factor $\Gamma_1$, rapidity $\psi_1$) along $e_1$, and $\Lambda_2$ a boost of speed $V_2$ (Lorentz factor $\Gamma_2$, rapidity $\psi_2$) along $e_2$, so the two velocities are *perpendicular*, $\chi = \pi/2$.

1. Write the two boost matrices and compute the product $\Lambda = \Lambda_2\circ\Lambda_1$ acting on $e_0$; obtain the composite Lorentz factor $\Gamma = e_0\cdot\Lambda(e_0)$ and confirm $\Gamma = \Gamma_1\Gamma_2$ at $\chi = \pi/2$.
2. Show the product matrix $\Lambda$ is *not* symmetric, hence not a boost, and extract the Thomas rotation $R$ as the rotation factor of the polar decomposition $\Lambda = S\circ R$ relative to $e_0$. Verify its plane is $\mathrm{Span}(e_1, e_2)$.
3. Derive the perpendicular-boost Thomas angle
$$
\cos\varphi_T = \frac{\Gamma_1 + \Gamma_2}{1 + \Gamma_1\Gamma_2},
$$
and confirm $\varphi_T \le 0$ (clockwise in the $(e_1, e_2)$-plane oriented by $e_1\times e_2$).
4. **Non-relativistic limit.** Expand for small speeds and show $\varphi_T \approx -\tfrac12 V_1 V_2$ to leading order, the classic "half" of the Thomas precession. Take equal speeds $V_1 = V_2 = V$ and find both the exact angle and the small-$V$ form.

**Recall:**

The exercise specialises the general Thomas-angle formula to perpendicular boosts and checks the non-relativistic limit.

![[Thm - The Thomas Rotation Angle#Statement]]

The composition of two non-collinear boosts is a boost times the [[Def - Thomas Rotation|Thomas rotation]] ([[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|composition theorem]]). The polar boost factor has Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi)$, which at $\chi = \pi/2$ is $\Gamma = \Gamma_1\Gamma_2$. A boost along $e_i$ has $\Lambda^0{}_0 = \Gamma_i$, $\Lambda^0{}_i = \Lambda^i{}_0 = \Gamma_i V_i$, fixing the orthogonal spatial directions.

---

# Convergent Strategy

**Problem class.** An *extract-the-Thomas-rotation* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: compose two boosts, recognise the product is not a boost (asymmetric matrix), and read the residual rotation off the polar decomposition.

**Assumption pattern.** The signpost is "two boosts in perpendicular directions." Perpendicularity ($\chi = \pi/2$, $\cos\chi = 0$) collapses the general formula to the clean $\cos\varphi_T = (\Gamma_1+\Gamma_2)/(1+\Gamma_1\Gamma_2)$ and makes the composite Lorentz factor simply $\Gamma = \Gamma_1\Gamma_2$. The Thomas rotation lives in the plane of the two velocities, here $(e_1, e_2)$, about the $e_3$-axis.

**Theorem routing.** Part 1 uses [[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|the composition theorem]] for $\Gamma$. Parts 2–3 instantiate [[Thm - The Thomas Rotation Angle|the Thomas-angle theorem]] at $\chi = \pi/2$, extracting $R$ via [[Thm - Polar Decomposition of the Lorentz Group|the polar decomposition]] ($\cos\varphi_T = R(e_1)\cdot e_1$, $\sin\varphi_T = R(e_1)\cdot e_2$). Part 4 is the small-velocity expansion $\Gamma_i \approx 1 + \tfrac12 V_i^2$.

**Key decision point.** The crux is to extract the rotation as $R = S^{-1}\Lambda$ rather than trying to read it off the $3\times 3$ spatial block of $\Lambda$ (which is not orthogonal). The boost $S$ is determined by $\Lambda(e_0)$; once divided out, the remainder rotates $(e_1, e_2)$ by $\varphi_T$. The non-relativistic check $\varphi_T \approx -\tfrac12 V_1 V_2$ is the calibration that the algebra is right.

---

# Legal Operations Used

1. **Compose boosts by velocity addition plus a Thomas rotation** (operation 8 from the topic page): the product is a boost ($\Gamma = \Gamma_1\Gamma_2$) times the Thomas rotation.

2. **Polar-decompose relative to a chosen 4-velocity** (operation 7): build $S$ from $\Lambda(e_0)$, set $R = S^{-1}\Lambda$, read $\varphi_T$.

3. **The boost is symmetric, the rotation is orthogonal** (most-reusable property): the product $\Lambda$ is asymmetric, flagging the Thomas rotation.

---

# Hints

> [!note]- Hint 1
> $\Lambda_1(e_0) = \Gamma_1 e_0 + \Gamma_1 V_1 e_1$. Apply $\Lambda_2$ (boost along $e_2$): it acts on the $e_0$ part, sending $\Gamma_1 e_0 \mapsto \Gamma_1(\Gamma_2 e_0 + \Gamma_2 V_2 e_2)$, and leaves the $e_1$ part alone (the $e_2$-boost fixes $e_1$). So $\Lambda(e_0) = \Gamma_1\Gamma_2 e_0 + \Gamma_1 V_1 e_1 + \Gamma_1\Gamma_2 V_2 e_2$. The time-component is $\Gamma = \Gamma_1\Gamma_2$.

> [!note]- Hint 2
> The boost factor $S$ carries $e_0$ to $\Lambda(e_0)$, so $\Gamma = \Gamma_1\Gamma_2$ and the boost velocity points along the spatial part of $\Lambda(e_0)$, namely $(\Gamma_1 V_1, \Gamma_1\Gamma_2 V_2, 0)/\Gamma$. To get $R = S^{-1}\Lambda$, the most economical route is to compute $R(e_1) = S^{-1}\Lambda(e_1)$ and project onto $e_1, e_2$: $\cos\varphi_T = R(e_1)\cdot e_1$, $\sin\varphi_T = R(e_1)\cdot e_2$. Asymmetry of $\Lambda$: compare the $(0,2)$ entry $\Gamma_1\Gamma_2 V_2$ with the $(2,0)$ entry $\Gamma_2 V_2$ — unequal because of the extra $\Gamma_1$.

> [!note]- Hint 3
> Specialise the general formula at $\chi = \pi/2$: $\cos\varphi_T = 1 - \frac{(\Gamma_1-1)(\Gamma_2-1)}{1+\Gamma_1\Gamma_2}$. Now simplify the numerator: $1 + \Gamma_1\Gamma_2 - (\Gamma_1-1)(\Gamma_2-1) = 1 + \Gamma_1\Gamma_2 - \Gamma_1\Gamma_2 + \Gamma_1 + \Gamma_2 - 1 = \Gamma_1 + \Gamma_2$. Hence $\cos\varphi_T = (\Gamma_1+\Gamma_2)/(1+\Gamma_1\Gamma_2)$.

> [!note]- Hint 4
> Small speeds: $\Gamma_i = 1 + \tfrac12 V_i^2 + O(V^4)$. Then $\cos\varphi_T = \frac{2 + \tfrac12(V_1^2 + V_2^2)}{2 + \tfrac12(V_1^2 + V_2^2) + V_1^2 V_2^2/4 + \cdots}$. To leading order $\cos\varphi_T \approx 1 - \tfrac18 V_1^2 V_2^2$, so $\varphi_T^2/2 \approx \tfrac18 V_1^2 V_2^2$, giving $|\varphi_T| \approx \tfrac12 V_1 V_2$. With the clockwise sign, $\varphi_T \approx -\tfrac12 V_1 V_2$.

---

# Solution

We compute the composite Lorentz factor (Step 1), extract the Thomas rotation via the polar decomposition (Step 2), derive the perpendicular-boost angle (Step 3), and take the non-relativistic limit (Step 4).

**Step 1: The composite Lorentz factor.**

> [!note]- Derivation
> Write $\Lambda_1$ (boost along $e_1$) and $\Lambda_2$ (boost along $e_2$):
> $$\Lambda_1 = \begin{pmatrix} \Gamma_1 & \Gamma_1 V_1 & 0 & 0\\ \Gamma_1 V_1 & \Gamma_1 & 0 & 0\\ 0&0&1&0\\ 0&0&0&1\end{pmatrix}, \qquad \Lambda_2 = \begin{pmatrix} \Gamma_2 & 0 & \Gamma_2 V_2 & 0\\ 0&1&0&0\\ \Gamma_2 V_2 & 0 & \Gamma_2 & 0\\ 0&0&0&1\end{pmatrix}.$$
> Apply $\Lambda = \Lambda_2\Lambda_1$ to $e_0$. First $\Lambda_1(e_0) = \Gamma_1 e_0 + \Gamma_1 V_1 e_1$. Then $\Lambda_2$ acts: it sends $e_0 \mapsto \Gamma_2 e_0 + \Gamma_2 V_2 e_2$ and fixes $e_1$, so
> $$\Lambda(e_0) = \Gamma_1(\Gamma_2 e_0 + \Gamma_2 V_2 e_2) + \Gamma_1 V_1 e_1 = \Gamma_1\Gamma_2\,e_0 + \Gamma_1 V_1\,e_1 + \Gamma_1\Gamma_2 V_2\,e_2.$$
> The composite Lorentz factor is the time-component,
> $$\Gamma = e_0\cdot\Lambda(e_0) = \Gamma_1\Gamma_2,$$
> confirming $\Gamma = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi)$ at $\chi = \pi/2$ ($\cos\chi = 0$). Note the asymmetry already: the final velocity has $e_1$-component $\Gamma_1 V_1/\Gamma = V_1/\Gamma_2$ but $e_2$-component $\Gamma_1\Gamma_2 V_2/\Gamma = V_2$ — the first boost's direction is "diminished" by the second's $\Gamma_2$, the hallmark of non-commutative velocity addition.

**Step 2: Extract the Thomas rotation.**

> [!note]- Derivation
> The product matrix has $(0,2)$ entry $\Lambda^0{}_2 = \Gamma_1\Gamma_2 V_2$ (from $\Lambda_2$'s $e_2$-boost acting after) but $(2,0)$ entry $\Lambda^2{}_0 = \Gamma_2 V_2$ (from $\Lambda_2$ alone, since $\Lambda_1$ fixes the $e_2$-row's coupling to $e_0$ only through $\Gamma_1$). Lowering indices, these give an asymmetric matrix: $\Lambda$ is **not** symmetric, hence **not** a boost.
>
> By [[Thm - Polar Decomposition of the Lorentz Group|the polar decomposition]] relative to $e_0$, $\Lambda = S\circ R$ with $S$ the boost carrying $e_0 \mapsto \Lambda(e_0)$ (Lorentz factor $\Gamma = \Gamma_1\Gamma_2$, velocity direction the spatial part of $\Lambda(e_0)$) and $R = S^{-1}\Lambda$ a rotation fixing $e_0$. Computing $R(e_3) = e_3$ (both boosts fix $e_3$, so does $S$), the rotation acts only in $\mathrm{Span}(e_1, e_2)$ — its axis is $e_3 = e_1\times e_2$, the normal to the plane of the two velocities. The angle is read from
> $$\cos\varphi_T = R(e_1)\cdot e_1, \qquad \sin\varphi_T = R(e_1)\cdot e_2,$$
> which Step 3 evaluates. The Thomas rotation plane is confirmed to be $\mathrm{Span}(\mathbf{V}_1, \mathbf{V}_2) = \mathrm{Span}(e_1, e_2)$.

**Step 3: The perpendicular-boost angle.**

> [!note]- Derivation
> Specialise [[Thm - The Thomas Rotation Angle|the Thomas-angle theorem]] to $\chi = \pi/2$, so $\sin^2\chi = 1$ and $\Gamma = \Gamma_1\Gamma_2$:
> $$\cos\varphi_T = 1 - \frac{(\Gamma_1 - 1)(\Gamma_2 - 1)}{1 + \Gamma_1\Gamma_2}.$$
> Combine over the common denominator and expand the numerator:
> $$1 + \Gamma_1\Gamma_2 - (\Gamma_1 - 1)(\Gamma_2 - 1) = 1 + \Gamma_1\Gamma_2 - \big(\Gamma_1\Gamma_2 - \Gamma_1 - \Gamma_2 + 1\big) = \Gamma_1 + \Gamma_2.$$
> Hence
> $$\boxed{\;\cos\varphi_T = \frac{\Gamma_1 + \Gamma_2}{1 + \Gamma_1\Gamma_2}\;}$$
> Since $\Gamma_1, \Gamma_2 \ge 1$, the right side is at most $1$ (it equals $1$ only when $\Gamma_1 = 1$ or $\Gamma_2 = 1$, i.e. one boost is trivial), confirming $\cos\varphi_T \le 1$ and a genuine rotation for nontrivial boosts. The sign of $\sin\varphi_T$ from Lemma 3 of the angle theorem is negative ($\sin\chi = 1 > 0$, bracket positive), so $\varphi_T \in [-\pi, 0]$: the rotation is **clockwise** in the $(e_1, e_2)$-plane oriented by $e_1\times e_2 = e_3$.

**Step 4: The non-relativistic limit.**

> [!note]- Derivation
> Expand $\Gamma_i = (1 - V_i^2)^{-1/2} = 1 + \tfrac12 V_i^2 + \tfrac38 V_i^4 + \cdots$. Then
> $$\Gamma_1 + \Gamma_2 = 2 + \tfrac12(V_1^2 + V_2^2) + O(V^4), \qquad 1 + \Gamma_1\Gamma_2 = 2 + \tfrac12(V_1^2 + V_2^2) + \tfrac14 V_1^2 V_2^2 + O(V^6).$$
> So
> $$\cos\varphi_T = \frac{2 + \tfrac12(V_1^2+V_2^2)}{2 + \tfrac12(V_1^2+V_2^2) + \tfrac14 V_1^2 V_2^2} = 1 - \frac{\tfrac14 V_1^2 V_2^2}{2 + \cdots} = 1 - \tfrac18 V_1^2 V_2^2 + O(V^6).$$
> Using $\cos\varphi_T \approx 1 - \tfrac12\varphi_T^2$ for small $\varphi_T$, we read off $\tfrac12\varphi_T^2 \approx \tfrac18 V_1^2 V_2^2$, so $|\varphi_T| \approx \tfrac12 V_1 V_2$. With the clockwise sign,
> $$\varphi_T \approx -\tfrac12 V_1 V_2.$$
> This is the famous factor of one-half: the Thomas rotation per pair of perpendicular boosts is half the product of the speeds, and it is the seed of the $-\tfrac12$ in the spin–orbit coupling. For **equal speeds** $V_1 = V_2 = V$ (so $\Gamma_1 = \Gamma_2 = \Gamma_0 = (1-V^2)^{-1/2}$), the exact angle is
> $$\cos\varphi_T = \frac{2\Gamma_0}{1 + \Gamma_0^2} = \frac{2\Gamma_0}{1 + \Gamma_0^2},$$
> and since $1 + \Gamma_0^2 = 1 + 1/(1-V^2) = (2 - V^2)/(1-V^2)$ while $2\Gamma_0 = 2/\sqrt{1-V^2}$, this is $\cos\varphi_T = 2\sqrt{1-V^2}/(2 - V^2)$, with small-$V$ form $\varphi_T \approx -\tfrac12 V^2$.

> [!note]- Complete formal solution
> For boosts of speeds $V_1$ along $e_1$ and $V_2$ along $e_2$, $\Lambda_2\Lambda_1(e_0) = \Gamma_1\Gamma_2 e_0 + \Gamma_1 V_1 e_1 + \Gamma_1\Gamma_2 V_2 e_2$, so the composite Lorentz factor is $\Gamma = \Gamma_1\Gamma_2$ (the $\chi=\pi/2$ case of $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$). The product matrix is asymmetric ($\Lambda^0{}_2 = \Gamma_1\Gamma_2 V_2 \ne \Gamma_2 V_2 = \Lambda^2{}_0$), hence not a boost; polar-decomposing $\Lambda = S\circ R$ relative to $e_0$ leaves a rotation $R$ with axis $e_3$ acting in $\mathrm{Span}(e_1,e_2)$. Specialising the Thomas-angle theorem at $\chi=\pi/2$, $\cos\varphi_T = 1 - (\Gamma_1-1)(\Gamma_2-1)/(1+\Gamma_1\Gamma_2) = (\Gamma_1+\Gamma_2)/(1+\Gamma_1\Gamma_2)$, with $\varphi_T \le 0$ (clockwise). Small speeds: $\Gamma_i \approx 1 + \tfrac12 V_i^2$ gives $\cos\varphi_T \approx 1 - \tfrac18 V_1^2 V_2^2$, so $\varphi_T \approx -\tfrac12 V_1 V_2$. For equal speeds $V_1=V_2=V$: $\cos\varphi_T = 2\Gamma_0/(1+\Gamma_0^2) = 2\sqrt{1-V^2}/(2-V^2)$, with $\varphi_T \approx -\tfrac12 V^2$. $\blacksquare$

---

# Key Takeaways

**Perpendicularity collapses the Thomas angle to the symmetric formula $\cos\varphi_T = (\Gamma_1+\Gamma_2)/(1+\Gamma_1\Gamma_2)$.** At $\chi = \pi/2$ the composite Lorentz factor is simply the product $\Gamma = \Gamma_1\Gamma_2$ and the general angle formula simplifies dramatically, because $\sin^2\chi = 1$ and the algebraic identity $1 + \Gamma_1\Gamma_2 - (\Gamma_1-1)(\Gamma_2-1) = \Gamma_1 + \Gamma_2$ does the work. This is the single most quotable instance of the Thomas rotation, and it is worth memorising: it depends only on the two Lorentz factors, is symmetric under swapping them, and reaches its maximum (for fixed speeds) here at perpendicular incidence. The reusable recognition is that the cleanest Thomas-rotation problems are the perpendicular ones, and that the composite $\Gamma = \Gamma_1\Gamma_2$ for perpendicular boosts is the same multiplicativity as for collinear boosts only because the cross-term $V_1 V_2\cos\chi$ vanishes — a coincidence of the right angle, not a general fact.

**The product of perpendicular boosts is asymmetric, and the asymmetry is the Thomas rotation.** Computing $\Lambda_2\Lambda_1$ shows the $(0,2)$ and $(2,0)$ matrix entries differ by a factor of $\Gamma_1$ — the first boost "contaminates" the second boost's coupling to time. This asymmetry is precisely why the product is not a boost (boosts are symmetric) and precisely what the polar decomposition extracts as the rotation $R$. The same diagnostic — compute the product, check whether the matrix is symmetric — answers "do these two boosts compose to a boost?" in one line: symmetric means yes (collinear), asymmetric means no (a Thomas rotation appears). The degree of asymmetry, made precise by $R = S^{-1}\Lambda$, is the rotation angle. This is the concrete computational face of "boosts do not form a subgroup."

**The factor of one-half in $\varphi_T \approx -\tfrac12 V_1 V_2$ is the kinematic origin of the spin–orbit one-half.** The non-relativistic limit of the perpendicular Thomas angle is exactly half the product of the speeds, and the clockwise sign is what makes the induced precession *oppose* the magnetic precession. This is the seed of the celebrated factor of $\tfrac12$ that Thomas supplied in 1926 to reconcile the naive spin–orbit coupling (which overpredicts fine-structure splitting by two) with experiment: integrating these infinitesimal $-\tfrac12 V\,dV$-type rotations around an electron's orbit yields the Thomas precession rate $\boldsymbol{\Omega}_T = \frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}$, whose low-velocity limit carries the same one-half. The reusable lesson is that the "one-half" is not put in by hand anywhere in atomic physics — it falls out of the second-order expansion of the Lorentz group's composition law, a purely kinematic fact about how perpendicular boosts compose. The calibration check $\varphi_T \approx -\tfrac12 V_1 V_2$ is therefore both a verification of the algebra and a direct line to a measured spectral correction.
