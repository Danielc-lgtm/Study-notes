---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Thm - The Exponential Map Generates the Restricted Lorentz Group"
  - "Def - Lie Algebra of the Lorentz Group"
tags: [physics, special-relativity, lie-groups]
---

# Problem Statement

Compute the exponential of the rotation generator $J_3$ and show it is the rotation by angle $\varphi$ about the $z$-axis.

1. Compute $J_3^2$ and $J_3^3$, and identify the pattern of powers.
2. Resum the exponential series $\exp(\varphi J_3) = \sum_n (\varphi J_3)^n/n!$ into closed form, exhibiting $\cos\varphi$ and $\sin\varphi$.
3. Write out the resulting $4\times4$ matrix and confirm it is the spatial rotation by $\varphi$ in the $x$–$y$ plane (Rodrigues formula).
4. Verify that $\exp(\varphi J_3)$ is periodic with period $2\pi$, and contrast this with the boost, which is *not* periodic — relating the contrast to compactness.

**Recall:**

![[Thm - The Exponential Map Generates the Restricted Lorentz Group#Statement]]

The matrix exponential is $\exp(M) = \sum_{n\ge0}M^n/n!$. The rotation generator $J_3$ has $-1$ at $(1,2)$ and $+1$ at $(2,1)$, acting as $\mathbf{e}_3\times$ on the spatial block. The circular functions are $\cos\varphi = \sum_{m\ge0}(-1)^m\varphi^{2m}/(2m)!$ and $\sin\varphi = \sum_{m\ge0}(-1)^m\varphi^{2m+1}/(2m+1)!$.

---

# Convergent Strategy

**Problem class.** An *exponentiate-a-generator* problem, the rotation counterpart of the boost. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] recipe is to find $G^2$ and resum: a *negative* projector gives circular functions.

**Assumption pattern.** $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ is a *negative* projector onto the $x$–$y$ plane, with $J_3^3 = -J_3$. The signpost is the minus sign, which inserts $(-1)^m$ into the resummed series and produces $\cos, \sin$.

**Theorem routing.** Part 1: compute $J_3^2 = \mathrm{diag}(0,-1,-1,0)$, $J_3^3 = -J_3$. Part 2: the powers cycle $J_3^{2m+1} = (-1)^m J_3$, $J_3^{2m} = (-1)^{m-1}(-J_3^2)$... resum to $\exp(\varphi J_3) = \mathrm{Id} + \sin\varphi\,J_3 + (1-\cos\varphi)J_3^2$ ([[Thm - The Exponential Map Generates the Restricted Lorentz Group]]). Part 3: write the rotation matrix. Part 4: periodicity from $\cos, \sin$.

**Key decision point.** The crux is the *negative* sign of $J_3^2$, which is what makes the rotation periodic (the $\cos, \sin$ wrap at $2\pi$) and compact — in direct contrast to the boost, whose positive $K_1^2$ gives non-periodic, unbounded $\cosh, \sinh$. Recognising that the sign of the generator's square dictates compactness is the conceptual payoff.

---

# Legal Operations Used

1. **Exponentiate a generator to a finite transformation (operation 4 from the topic page).** Find $J_3^2$, recognise the negative projector, resum to $\cos, \sin$.

2. **Add parameters when generators commute (operation 5 from the topic page).** Implicit in part 4: coaxial rotations add angles, $\exp(\varphi_1 J_3)\exp(\varphi_2 J_3) = \exp((\varphi_1+\varphi_2)J_3)$, with the periodicity $\varphi \to \varphi + 2\pi$ giving the same rotation.

---

# Hints

> [!note]- Hint 1
> $J_3$ has $-1$ at $(1,2)$ and $+1$ at $(2,1)$. Square it: the spatial $2\times2$ block $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ squares to $-I_2$, so $J_3^2 = \mathrm{diag}(0,-1,-1,0)$.

> [!note]- Hint 2
> Then $J_3^3 = J_3\cdot J_3^2 = -J_3$. So $J_3^{2m+1} = (-1)^m J_3$ and $J_3^{2m} = (-1)^{m+1}J_3^2 = -(-1)^m J_3^2$ for $m \ge 1$. The alternating signs are the seeds of $\cos, \sin$.

> [!note]- Hint 3
> Split the series: $\exp(\varphi J_3) = \mathrm{Id} + (\sum_{m\ge0}(-1)^m\varphi^{2m+1}/(2m+1)!)J_3 + (\sum_{m\ge1}(-1)^{m-1}\varphi^{2m}/(2m)!)J_3^2$. The odd sum is $\sin\varphi$; the even sum is $1 - \cos\varphi$.

> [!note]- Hint 4
> $\cos$ and $\sin$ have period $2\pi$, so $\exp((\varphi+2\pi)J_3) = \exp(\varphi J_3)$ — the rotation repeats. The boost $\exp(\psi K_1)$ uses $\cosh, \sinh$, which are *not* periodic and grow without bound; this is the difference between the compact rotation circle and the non-compact boost line.

---

# Solution

Because $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ is a negative projector with $J_3^3 = -J_3$, the alternating-sign series resums into $\cos\varphi$ and $\sin\varphi$, giving the spatial rotation matrix. The negative square makes the rotation periodic and compact — the opposite of the boost.

**Step 1: Powers of $J_3$.**

> [!note]- Derivation
> $J_3$ has $-1$ at $(1,2)$ and $+1$ at $(2,1)$. The spatial $x$–$y$ block is $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, which squares to $\begin{pmatrix}-1&0\\0&-1\end{pmatrix} = -I_2$. So
> $$J_3^2 = \mathrm{diag}(0,-1,-1,0),$$
> a *negative* projector onto the $x$–$y$ plane. Then $J_3^3 = J_3\cdot J_3^2 = -J_3$, and the powers cycle with alternating signs:
> $$J_3^{2m+1} = (-1)^m J_3,\qquad J_3^{2m} = (-1)^{m+1}J_3^2\ (m\ge1),\qquad J_3^0 = \mathrm{Id}.$$

**Step 2: Resum the series.**

> [!note]- Derivation
> Insert into the exponential:
> $$\exp(\varphi J_3) = \mathrm{Id} + \sum_{m\ge0}\frac{(-1)^m\varphi^{2m+1}}{(2m+1)!}J_3 + \sum_{m\ge1}\frac{(-1)^{m-1}\varphi^{2m}}{(2m)!}J_3^2.$$
> The odd sum is $\sum_{m\ge0}(-1)^m\varphi^{2m+1}/(2m+1)! = \sin\varphi$. The even sum is $\sum_{m\ge1}(-1)^{m-1}\varphi^{2m}/(2m)! = -\sum_{m\ge1}(-1)^m\varphi^{2m}/(2m)! = -(\cos\varphi - 1) = 1 - \cos\varphi$. Therefore
> $$\boxed{\exp(\varphi J_3) = \mathrm{Id} + \sin\varphi\,J_3 + (1-\cos\varphi)J_3^2.}$$

**Step 3: The rotation matrix.**

> [!note]- Derivation
> Write it out. $\mathrm{Id} = \mathrm{diag}(1,1,1,1)$; $\sin\varphi\,J_3$ puts $-\sin\varphi$ at $(1,2)$ and $+\sin\varphi$ at $(2,1)$; $(1-\cos\varphi)J_3^2$ subtracts $(1-\cos\varphi)$ from the $(1,1)$ and $(2,2)$ diagonal entries, turning those $1$'s into $\cos\varphi$. Collecting,
> $$\exp(\varphi J_3) = \begin{pmatrix} 1 & 0 & 0 & 0\\ 0 & \cos\varphi & -\sin\varphi & 0\\ 0 & \sin\varphi & \cos\varphi & 0\\ 0 & 0 & 0 & 1 \end{pmatrix},$$
> the rotation by $\varphi$ in the $x$–$y$ plane (this is the Rodrigues formula for rotation about $\mathbf{e}_3$). The time component and the $z$-axis are untouched, as expected for a rotation about $z$. It is a genuine restricted Lorentz transformation: $\det = \cos^2\varphi + \sin^2\varphi = 1$ and $\Lambda^0{}_0 = 1$.

**Step 4: Periodicity and compactness.**

> [!note]- Derivation
> Because $\cos$ and $\sin$ have period $2\pi$, the exponential is periodic:
> $$\exp((\varphi + 2\pi)J_3) = \exp(\varphi J_3).$$
> A rotation by $\varphi$ and by $\varphi + 2\pi$ are the same transformation — the rotation "wraps around". The one-parameter subgroup $\{\exp(\varphi J_3) : \varphi \in \mathbb{R}\}$ is therefore a *circle* (image $\cong SO(2)$), which is **compact**.
>
> Contrast the boost $\exp(\psi K_1)$, built from $\cosh, \sinh$. These are *not* periodic — they grow without bound, $\cosh\psi \to \infty$ — so distinct rapidities $\psi$ give distinct boosts with no wrapping, and the one-parameter subgroup is a *line* ($\cong \mathbb{R}$), which is **non-compact**. The sign of the generator's square is again decisive: $J_3^2 < 0$ gives periodic, bounded, compact (a circle); $K_1^2 > 0$ gives non-periodic, unbounded, non-compact (a line). This is the one-parameter-subgroup root of the global fact that the rotation subgroup $SO(3)$ is compact while the boosts make $SO^+(1,3)$ non-compact.

> [!note]- Complete formal solution
> $J_3$ has $-1$ at $(1,2)$, $+1$ at $(2,1)$; the spatial block squares to $-I_2$, so $J_3^2 = \mathrm{diag}(0,-1,-1,0)$ and $J_3^3 = -J_3$, giving $J_3^{2m+1} = (-1)^m J_3$, $J_3^{2m} = (-1)^{m+1}J_3^2$. The series resums to $\exp(\varphi J_3) = \mathrm{Id} + (\sum(-1)^m\varphi^{2m+1}/(2m+1)!)J_3 + (\sum(-1)^{m-1}\varphi^{2m}/(2m)!)J_3^2 = \mathrm{Id} + \sin\varphi\,J_3 + (1-\cos\varphi)J_3^2$, which as a matrix is the rotation $\begin{pmatrix}\cos\varphi & -\sin\varphi\\ \sin\varphi & \cos\varphi\end{pmatrix}$ in the $x$–$y$ block, identity on $t$ and $z$. It is periodic with period $2\pi$ (so the subgroup is a compact circle), in contrast to the boost's non-periodic $\cosh, \sinh$ (a non-compact line) — the sign of $G^2$ deciding compactness. $\blacksquare$

---

# Key Takeaways

**The rotation exponential is the Rodrigues formula, and the negative square is what makes it a rotation.** The exponential of a rotation generator resums, via $J_3^2 = -(\text{projector})$, into $\mathrm{Id} + \sin\varphi\,J_3 + (1-\cos\varphi)J_3^2$ — the Rodrigues rotation formula, here for rotation about $\mathbf{e}_3$. The reusable recipe mirrors the boost case but with the sign flipped: a generator with a *negative* projector square gives circular functions, hence a rotation, while a positive square gives hyperbolic functions, hence a boost. The trigger is the sign of $G^2$: negative for compact (rotation) generators, positive for non-compact (boost) generators. This is the same computation as the boost exercise with $\varphi \to i\psi$, the formal substitution that turns a rotation into a boost, and it is why "boost = imaginary rotation" is exact at the level of the exponential.

**Periodicity is compactness, and it is decided by one sign.** A rotation repeats every $2\pi$ — $\exp((\varphi+2\pi)J_3) = \exp(\varphi J_3)$ — so its one-parameter subgroup is a circle, compact. A boost never repeats — $\cosh\psi$ grows without bound — so its subgroup is a line, non-compact. The reusable diagnostic: the one-parameter subgroup generated by $G$ is compact (a circle) iff $G^2$ is a *negative* multiple of a projector (giving periodic $\cos, \sin$) and non-compact (a line) iff $G^2$ is *positive* (giving unbounded $\cosh, \sinh$). This local fact assembles into the global one: the rotation subgroup $SO(3)$ is compact because all its generators have negative square, while the boosts make $SO^+(1,3)$ non-compact because their generators have positive square. The periodicity you see in a single rotation is the seed of the compactness of the whole rotation group, and the unboundedness of a single boost is the seed of the non-compactness of the Lorentz group — and both are read off the sign of one generator's square.

**Coaxial rotations add angles, exactly as collinear boosts add rapidities.** Because all the $\exp(\varphi J_3)$ for varying $\varphi$ are generated by the same $J_3$, they commute, and the parameters add: $\exp(\varphi_1 J_3)\exp(\varphi_2 J_3) = \exp((\varphi_1+\varphi_2)J_3)$. The angle is the additive coordinate on the rotation circle, just as the rapidity is on the boost line. The difference is only that the angle is *periodic* (it wraps at $2\pi$, so the circle closes) while the rapidity is *not* (it runs to infinity, so the line is open). The reusable principle is the same in both cases: the canonical coordinate on a one-parameter subgroup is the generator's parameter, and it is always additive — what differs between rotations and boosts is whether that additive coordinate lives on a circle or a line, which is the compact-versus-non-compact distinction once more.
