---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Exponential Map Generates the Restricted Lorentz Group"
  - "Def - Lie Algebra of the Lorentz Group"
  - "Def - Boosts as Hyperbolic Rotations"
tags: [physics, special-relativity, lie-groups]
---

# Problem Statement

Compute the exponential of the boost generator $K_1$ and show it is the Lorentz boost of rapidity $\psi$.

1. Compute $K_1^2$ and $K_1^3$, and identify the pattern of powers.
2. Resum the exponential series $\exp(\psi K_1) = \sum_n (\psi K_1)^n/n!$ into closed form, exhibiting the hyperbolic functions $\cosh\psi$ and $\sinh\psi$.
3. Confirm the result is the standard boost matrix and that $v = \tanh\psi$ is the velocity.
4. Contrast with the rotation case: explain why $\exp(\psi K_1)$ uses $\cosh, \sinh$ (hyperbolic) while $\exp(\varphi J_3)$ uses $\cos, \sin$ (circular), tracing the difference to the sign of the generator's square.

**Recall:**

![[Thm - The Exponential Map Generates the Restricted Lorentz Group#Statement]]

The matrix exponential is $\exp(M) = \sum_{n\ge0} M^n/n!$. The boost generator $K_1$ has $1$ in the $(0,1)$ and $(1,0)$ entries. The hyperbolic functions are $\cosh\psi = \sum_{m\ge0}\psi^{2m}/(2m)!$ and $\sinh\psi = \sum_{m\ge0}\psi^{2m+1}/(2m+1)!$. A [[Def - Boosts as Hyperbolic Rotations|boost]] of rapidity $\psi$ along $x$ has matrix $\begin{pmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{pmatrix}$ in the $t$–$x$ block.

---

# Convergent Strategy

**Problem class.** An *exponentiate-a-generator* problem: recover a finite Lorentz transformation from its infinitesimal generator. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] says the mechanical step is to find $G^2$ and recognise its sign — a positive projector gives $\cosh, \sinh$, a negative one gives $\cos, \sin$.

**Assumption pattern.** The generator $K_1$ is sparse and its square is a simple projector. The signpost is that $K_1^2 = \mathrm{diag}(1,1,0,0)$ is a *positive* projector onto the $t$–$x$ plane, with $K_1^3 = K_1$, so the powers cycle and the series splits into even (giving $\cosh$) and odd (giving $\sinh$) parts.

**Theorem routing.** Part 1: compute $K_1^2 = \mathrm{diag}(1,1,0,0)$ and $K_1^3 = K_1$. Part 2: split the series $\sum \psi^n K_1^n/n!$ into even powers ($K_1^{2m} = K_1^2$ for $m\ge1$, summing to $\cosh\psi - 1$) and odd powers ($K_1^{2m+1} = K_1$, summing to $\sinh\psi$), giving $\exp(\psi K_1) = \mathrm{Id} + \sinh\psi\,K_1 + (\cosh\psi-1)K_1^2$ ([[Thm - The Exponential Map Generates the Restricted Lorentz Group]]). Part 3: write out the matrix and identify it as the boost. Part 4: contrast with $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ (negative).

**Key decision point.** The crux is the sign of $K_1^2$: because it is a *positive* projector ($+1$ on the diagonal of the $t$–$x$ block), the even-power series sums to $\cosh$ rather than $\cos$, and the boost is hyperbolic. Had the square been negative (as for the rotation $J_3$), the same resummation would give circular functions. The temptation is to compute the exponential term by term without exploiting $K_1^2$; recognising the projector structure is what makes the resummation immediate.

---

# Legal Operations Used

1. **Exponentiate a generator to a finite transformation (operation 4 from the topic page).** The entire exercise: find $K_1^2$, recognise it as a positive projector, resum to $\cosh, \sinh$.

2. **Compute a commutator / use the structure (operation 3 from the topic page).** Implicitly, $K_1^2 = \mathrm{diag}(1,1,0,0)$ is the projector onto the boost plane, the key structural fact driving the resummation.

---

# Hints

> [!note]- Hint 1
> $K_1$ has $1$ at $(0,1)$ and $(1,0)$. Square it: $(K_1^2)_{00} = (K_1)_{01}(K_1)_{10} = 1$, $(K_1^2)_{11} = (K_1)_{10}(K_1)_{01} = 1$, rest zero. So $K_1^2 = \mathrm{diag}(1,1,0,0)$.

> [!note]- Hint 2
> Then $K_1^3 = K_1 \cdot K_1^2 = K_1$ (since $K_1$ lives in the $t$–$x$ block where $K_1^2$ is the identity). So $K_1^{2m+1} = K_1$ and $K_1^{2m} = K_1^2$ for $m \ge 1$. The powers cycle between $K_1$ and $K_1^2$.

> [!note]- Hint 3
> Split the series: $\exp(\psi K_1) = \mathrm{Id} + \sum_{m\ge0}\frac{\psi^{2m+1}}{(2m+1)!}K_1 + \sum_{m\ge1}\frac{\psi^{2m}}{(2m)!}K_1^2$. Recognise the odd sum as $\sinh\psi$ and the even sum (from $m=1$) as $\cosh\psi - 1$.

> [!note]- Hint 4
> For the contrast: $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ — a *negative* projector. The same resummation with the minus sign gives $\cos\varphi$ and $\sin\varphi$ instead of $\cosh, \sinh$. The sign of $G^2$ is the whole difference.

---

# Solution

Because $K_1^2 = \mathrm{diag}(1,1,0,0)$ is a positive projector with $K_1^3 = K_1$, the exponential series splits into even powers (summing to $\cosh\psi$) and odd powers (summing to $\sinh\psi$), giving the hyperbolic boost matrix. The rotation case differs only in the sign of $J_3^2$, which turns the hyperbolic functions circular.

**Step 1: Powers of $K_1$.**

> [!note]- Derivation
> $K_1$ has $1$ at $(0,1)$ and $(1,0)$. Squaring,
> $$K_1^2 = \begin{pmatrix} 0&1&0&0\\ 1&0&0&0\\ 0&0&0&0\\ 0&0&0&0 \end{pmatrix}^2 = \begin{pmatrix} 1&0&0&0\\ 0&1&0&0\\ 0&0&0&0\\ 0&0&0&0 \end{pmatrix} = \mathrm{diag}(1,1,0,0),$$
> the projector onto the $t$–$x$ plane. Then $K_1^3 = K_1\cdot K_1^2 = K_1$ (multiplying $K_1$ by the projector onto its own support leaves it unchanged). So the powers cycle:
> $$K_1^{2m} = K_1^2 \ (m\ge1),\qquad K_1^{2m+1} = K_1 \ (m\ge0),$$
> with $K_1^0 = \mathrm{Id}$.

**Step 2: Resum the series.**

> [!note]- Derivation
> Insert the power pattern into the exponential series:
> $$\exp(\psi K_1) = \sum_{n\ge0}\frac{\psi^n}{n!}K_1^n = \mathrm{Id} + \sum_{m\ge0}\frac{\psi^{2m+1}}{(2m+1)!}K_1 + \sum_{m\ge1}\frac{\psi^{2m}}{(2m)!}K_1^2.$$
> The odd sum is $\sum_{m\ge0}\psi^{2m+1}/(2m+1)! = \sinh\psi$. The even sum (starting at $m=1$, since the $m=0$ term is the $\mathrm{Id}$ already pulled out) is $\sum_{m\ge1}\psi^{2m}/(2m)! = \cosh\psi - 1$. Therefore
> $$\boxed{\exp(\psi K_1) = \mathrm{Id} + \sinh\psi\,K_1 + (\cosh\psi - 1)K_1^2.}$$

**Step 3: The boost matrix.**

> [!note]- Derivation
> Write out the matrix. $\mathrm{Id} = \mathrm{diag}(1,1,1,1)$; $\sinh\psi\,K_1$ puts $\sinh\psi$ at $(0,1)$ and $(1,0)$; $(\cosh\psi-1)K_1^2$ adds $(\cosh\psi - 1)$ to the $(0,0)$ and $(1,1)$ diagonal entries, turning the $1$'s there into $\cosh\psi$. Collecting,
> $$\exp(\psi K_1) = \begin{pmatrix} \cosh\psi & \sinh\psi & 0 & 0\\ \sinh\psi & \cosh\psi & 0 & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1 \end{pmatrix},$$
> exactly the [[Def - Boosts as Hyperbolic Rotations|boost]] of rapidity $\psi$ in the $t$–$x$ plane. The velocity is $v = \tanh\psi = \sinh\psi/\cosh\psi$, so $\cosh\psi = \gamma = (1-v^2)^{-1/2}$ and $\sinh\psi = \gamma v$ — the boost in standard form. The transverse directions $y, z$ are untouched (the bottom-right block is the identity), as they should be for a boost along $x$.

**Step 4: Hyperbolic versus circular.**

> [!note]- Derivation
> The whole difference between a boost and a rotation is the *sign* of the generator's square. For the boost, $K_1^2 = \mathrm{diag}(1,1,0,0)$ is a *positive* projector, so the even-power series is $\sum \psi^{2m}/(2m)! = \cosh\psi$ — hyperbolic. For the rotation, $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ is a *negative* projector, with $J_3^3 = -J_3$, so the same resummation carries alternating signs:
> $$\exp(\varphi J_3) = \mathrm{Id} + \sin\varphi\,J_3 + (1-\cos\varphi)J_3^2,$$
> the even sum being $\sum (-1)^m\varphi^{2m}/(2m)! = \cos\varphi$ — circular. The signs $(-1)^m$ come precisely from $J_3^2$ being negative. So:
> $$K_1^2 = +(\text{projector}) \Rightarrow \cosh, \sinh \text{ (boost)},\qquad J_3^2 = -(\text{projector}) \Rightarrow \cos, \sin \text{ (rotation)}.$$
> This single sign is the algebraic statement that "a boost is a rotation through an imaginary angle": replacing $\varphi \to i\psi$ in $\cos\varphi, \sin\varphi$ gives $\cosh\psi, i\sinh\psi$, converting a rotation into a boost.

> [!note]- Complete formal solution
> $K_1$ has $1$ at $(0,1)$ and $(1,0)$; squaring gives $K_1^2 = \mathrm{diag}(1,1,0,0)$ (projector onto the $t$–$x$ plane) and $K_1^3 = K_1$, so $K_1^{2m} = K_1^2$, $K_1^{2m+1} = K_1$. The series splits: $\exp(\psi K_1) = \mathrm{Id} + (\sum_{m\ge0}\psi^{2m+1}/(2m+1)!)K_1 + (\sum_{m\ge1}\psi^{2m}/(2m)!)K_1^2 = \mathrm{Id} + \sinh\psi\,K_1 + (\cosh\psi-1)K_1^2$. As a matrix this is the boost $\mathrm{diag\text{-}block}\begin{pmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{pmatrix}$ in the $t$–$x$ block, identity on $y, z$, with $v = \tanh\psi$, $\cosh\psi = \gamma$, $\sinh\psi = \gamma v$. The hyperbolic functions arise because $K_1^2$ is a *positive* projector; the rotation $\exp(\varphi J_3)$ instead gives $\cos, \sin$ because $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ is *negative* — the sign of $G^2$ is the entire difference between boost and rotation. $\blacksquare$

---

# Key Takeaways

**Exponentiating a generator is a one-step computation once you know its square.** The entire method for turning a Lorentz generator into a finite transformation is: compute $G^2$, recognise it as a projector (up to sign), and resum the series into the appropriate functions. For the boost, $K_1^2 = \mathrm{diag}(1,1,0,0)$ is a positive projector, the powers cycle between $K_1$ and $K_1^2$, and the series collapses to $\mathrm{Id} + \sinh\psi\,K_1 + (\cosh\psi-1)K_1^2$. The reusable recipe applies to any generator whose square is a multiple of a projector: $\exp(tG) = \mathrm{Id} + \frac{\sinh(t\sqrt{\lambda})}{\sqrt\lambda}G + \frac{\cosh(t\sqrt\lambda)-1}{\lambda}G^2$ when $G^3 = \lambda G$ with $\lambda > 0$ (hyperbolic), or the circular analogue when $\lambda < 0$. The trigger: a generator with a simple $G^2$ (a projector, or $\pm$ a projector) exponentiates in closed form without summing the full series. This is exactly the structure of all the basic Lorentz and rotation generators, which is why their exponentials are elementary.

**The sign of $G^2$ is the entire difference between hyperbolic and circular — between boost and rotation.** The deepest single takeaway is that "a boost is a rotation through an imaginary angle" is not a metaphor but the precise statement that $K^2$ is positive where $J^2$ is negative. A positive square gives $\cosh, \sinh$ (a boost, unbounded, with no periodicity — you can boost arbitrarily far); a negative square gives $\cos, \sin$ (a rotation, bounded, periodic — angles wrap at $2\pi$). The substitution $\varphi \to i\psi$ converts one into the other, $\cos(i\psi) = \cosh\psi$, $\sin(i\psi) = i\sinh\psi$. This is the algebra-level manifestation of the chapter's refrain that Minkowski geometry is Euclidean geometry with one imaginary axis: the boost generator's positive square is the imaginary-angle rotation, and it is why boosts are non-compact (the rapidity runs to infinity) while rotations are compact (the angle wraps). When you see a generator, the sign of its square tells you immediately whether its one-parameter subgroup is a non-compact line of boosts or a compact circle of rotations.

**The rapidity is the natural exponential parameter, and it is why boosts add.** The exponential $\exp(\psi K_1)$ is parametrised by the rapidity $\psi$, not the velocity $v = \tanh\psi$, and this is the reason rapidities — not velocities — add under composition of collinear boosts. Because $\exp(\psi_1 K_1)\exp(\psi_2 K_1) = \exp((\psi_1+\psi_2)K_1)$ (the generators commute, being the same $K_1$), the rapidity is *additive*, exactly as the angle is additive for coaxial rotations. The velocity-addition formula $v = (v_1 + v_2)/(1 + v_1 v_2)$ is just $\tanh(\psi_1 + \psi_2)$ unpacked. The reusable insight: the canonical coordinate on a one-parameter subgroup is the one that makes the group law additive — the *generator's* parameter — and for boosts that is the rapidity. This is why [[Thm - Boosts Compose by Adding Rapidities|rapidity composition]] is linear while velocity composition is not, and why rapidity, ranging over all of $\mathbb{R}$, exhibits the non-compactness that velocity (trapped in $(-1,1)$) hides.
