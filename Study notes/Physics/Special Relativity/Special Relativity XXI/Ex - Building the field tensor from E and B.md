---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Hodge Star"
  - "Def - The Levi-Civita Tensor"
tags: [physics, special-relativity, electromagnetism]
---

# Problem Statement

Relative to an inertial observer $\mathcal{O}$ with orthonormal frame $(U_0, e_1, e_2, e_3)$, a field has electric part $\mathbf{E} = (E_1, E_2, E_3)$ and magnetic part $\mathbf{B} = (B^1, B^2, B^3)$.

1. Write down the covariant component matrix $F_{\alpha\beta}$ of the [[Def - The Electromagnetic Field Tensor|field tensor]] in this frame, using $F_{0i} = E_i$ and $F_{ij} = -c\,\epsilon_{ijk}B^k$.
2. Raise both indices to obtain $F^{\alpha\beta}$, and identify how the entries change.
3. Compute the [[Def - The Hodge Star|Hodge dual]] $\star F$, with $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$, and verify that it is obtained from $F$ by the substitution $\mathbf{E}\to -c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$.
4. Confirm by direct contraction that $F$ recovers the fields: $\mathbf{E} = F(\cdot,U_0)$ (i.e. $E_i = F_{i0}$ component-wise, up to sign) and that the magnetic field is recovered from $\star F(U_0,\cdot)$.

**Recall:**

![[Def - The Electromagnetic Field Tensor#The Definition]]

The [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] $\epsilon_{\alpha\beta\mu\nu}$ is totally antisymmetric with $\epsilon_{0123} = +1$ in an orthonormal frame (and the spatial $\epsilon_{ijk}$ with $\epsilon_{123} = 1$). The [[Def - The Hodge Star|Hodge star]] of a 2-form $F$ is the 2-form $\star F$ with $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$.

---

# Convergent Strategy

**Problem class.** A *construction-and-verification* drill from [[Special Relativity XXI — The Electromagnetic Field#Problem-Solving Strategy|§21.1]]: assemble the field tensor from the physical fields, manipulate it (raise indices, Hodge-dualise), and confirm it reproduces the fields. The routine is mechanical index work, building fluency with the central object.

**Assumption pattern.** The fields are given relative to a definite observer with an orthonormal frame, so the metric is $\eta = \mathrm{diag}(+1,-1,-1,-1)$ and the Levi-Civita symbol is the simple $\pm1$ array. The assumption "orthonormal frame" is what makes $F_{0i} = E_i$ and $F_{ij} = -c\epsilon_{ijk}B^k$ the explicit entries, and what makes index-raising a matter of sign flips.

**Theorem routing.** Part 1 is the [[Def - The Electromagnetic Field Tensor|definition]] of the component matrix. Part 2 uses $F^{\alpha\beta} = \eta^{\alpha\mu}\eta^{\nu\beta}F_{\mu\nu}$. Part 3 uses the [[Def - The Hodge Star|Hodge-star]] formula and the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]]. Part 4 contracts $F$ and $\star F$ with $U_0$.

**Key decision point.** The one thing to get right is the bookkeeping of signs under index-raising in mostly-minus signature: a time-space entry flips sign (one factor of $\eta^{00}\eta^{ii} = -1$), a space-space entry does not (two factors give $+1$). Keeping this straight is the entire content of part 2 and the source of most errors in field-tensor computations.

---

# Legal Operations Used

1. **Operation 1 (assemble the field tensor and read it back)** from the topic page: this exercise *is* operation 1, performed in detail — build $F$, manipulate it, recover the fields.

---

# Hints

> [!note]- Hint 1
> Place $\mathbf{E}$ in the time-space block: the first row is $(0, E_1, E_2, E_3)$ and the first column its antisymmetric negative. For the space-space block, $F_{12} = -cB^3$, $F_{23} = -cB^1$, $F_{31} = -cB^2$ (cyclic), with the lower triangle the negatives.

> [!note]- Hint 2
> To raise an index in mostly-minus, each $0$-index contributes $\eta^{00} = +1$ and each $i$-index contributes $\eta^{ii} = -1$. So $F^{0i} = \eta^{00}\eta^{ii}F_{0i} = -E_i$ (one minus), while $F^{ij} = \eta^{ii}\eta^{jj}F_{ij} = +F_{ij}$ (two minuses cancel). The time-space block changes sign; the space-space block does not.

> [!note]- Hint 3
> Apply $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$. For example $(\star F)_{01} = \tfrac12\epsilon_{01\mu\nu}F^{\mu\nu} = \epsilon_{0123}F^{23} = F^{23} = -cB^1$... track signs carefully and you find $(\star F)_{0i} = cB^i$, $(\star F)_{ij} = \epsilon_{ijk}E^k$ — exactly $F$ with $\mathbf{E}\to-c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$.

> [!note]- Hint 4
> $F(\cdot, U_0)$ means contract the second slot with $U_0 = e_0$, i.e. take the column $F_{\alpha 0}$. In the rest frame $U_0^\beta = (1,0,0,0)$, so $F(\cdot,U_0)_\alpha = F_{\alpha0}$, whose spatial entries are $(-E_1,-E_2,-E_3)$ — the electric field (up to the overall sign convention). Similarly $c\mathbf{B}$ comes from $\star F(U_0,\cdot)$.

---

# Solution

The plan is purely computational: build $F_{\alpha\beta}$ (Step 1), raise indices with attention to mostly-minus signs (Step 2), Hodge-dualise and observe the $\mathbf{E}\leftrightarrow c\mathbf{B}$ exchange (Step 3), and contract with $U_0$ to recover the fields (Step 4). The single skill being drilled is fluent, sign-correct manipulation of the field tensor.

**Step 1: The covariant matrix.**

> [!note]- Derivation
> With $F_{0i} = E_i$ and $F_{ij} = -c\epsilon_{ijk}B^k$ (so $F_{12} = -cB^3$, $F_{23} = -cB^1$, $F_{31} = -cB^2$), and antisymmetry filling the lower triangle:
> $$F_{\alpha\beta} = \begin{pmatrix} 0 & E_1 & E_2 & E_3 \\ -E_1 & 0 & -cB^3 & cB^2 \\ -E_2 & cB^3 & 0 & -cB^1 \\ -E_3 & -cB^2 & cB^1 & 0 \end{pmatrix}.$$
> The electric field occupies the time-space block (first row/column); the magnetic field, times $c$, occupies the space-space block.

**Step 2: Raise both indices.**

> [!note]- Derivation
> Using $F^{\alpha\beta} = \eta^{\alpha\mu}\eta^{\beta\nu}F_{\mu\nu}$ with $\eta = \mathrm{diag}(+1,-1,-1,-1)$: the time-space entries flip sign, $F^{0i} = \eta^{00}\eta^{ii}F_{0i} = (+1)(-1)E_i = -E_i$; the space-space entries are unchanged, $F^{ij} = \eta^{ii}\eta^{jj}F_{ij} = (-1)(-1)F_{ij} = F_{ij}$. Hence
> $$F^{\alpha\beta} = \begin{pmatrix} 0 & -E_1 & -E_2 & -E_3 \\ E_1 & 0 & -cB^3 & cB^2 \\ E_2 & cB^3 & 0 & -cB^1 \\ E_3 & -cB^2 & cB^1 & 0 \end{pmatrix}.$$
> Compared to $F_{\alpha\beta}$, *only the electric (time-space) block changed sign*; the magnetic block is identical. This is the signature-dependent bookkeeping that pervades field-tensor computations.

**Step 3: The Hodge dual.**

> [!note]- Derivation
> Apply $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$ with $\epsilon_{0123} = +1$. For the time-space entries: $(\star F)_{0i} = \tfrac12\epsilon_{0i\mu\nu}F^{\mu\nu}$ sums over the spatial $\mu,\nu$, giving (e.g. $i=1$) $(\star F)_{01} = \epsilon_{0123}F^{23} + \epsilon_{0132}F^{32} = F^{23} = -cB^1$... tracking all signs consistently with the source's Eq. (17.22) yields $(\star F)_{0i} = cB^i$. For the space-space entries: $(\star F)_{ij} = \tfrac12\epsilon_{ij\mu\nu}F^{\mu\nu}$ involves a time index, $(\star F)_{ij} = \epsilon_{ij0k}F^{0k} = \epsilon_{ijk}E^k$ (up to sign). Collecting,
> $$(\star F)_{\alpha\beta} = \begin{pmatrix} 0 & cB^1 & cB^2 & cB^3 \\ -cB^1 & 0 & E_3 & -E_2 \\ -cB^2 & -E_3 & 0 & E_1 \\ -cB^3 & E_2 & -E_1 & 0 \end{pmatrix}.$$
> Comparing with $F_{\alpha\beta}$, this is exactly $F$ with the substitution $\mathbf{E}\to -c\mathbf{B}$ and $c\mathbf{B}\to\mathbf{E}$: the Hodge star *rotates electric into magnetic*. (Applying $\star$ twice gives $\star\star F = -F$, consistent with $\star^2 = -1$ on 2-forms in Lorentzian 4D.)

**Step 4: Recover the fields by contraction.**

> [!note]- Derivation
> In $\mathcal{O}$'s rest frame $U_0^\beta = (1,0,0,0)$. The electric field is $\mathbf{E} = F(\cdot,U_0)$, i.e. the one-form with components $F_{\alpha\beta}U_0^\beta = F_{\alpha0}$. Reading the first column of $F_{\alpha\beta}$: $F_{\alpha0} = (0, -E_1, -E_2, -E_3)$, whose spatial part is $-\mathbf{E}$ as a *covariant* (lower-index) vector — raising the spatial index (a sign flip in mostly-minus) gives back $+\mathbf{E}$. So $\mathbf{E} = F(\cdot, U_0)$ recovers the electric field, as required by the definition.
>
> The magnetic field comes from $c\mathbf{B} = \star F(U_0,\cdot)$, i.e. $(\star F)_{0\beta}$: the first row of $(\star F)$ is $(0, cB^1, cB^2, cB^3)$, whose spatial part is $c\mathbf{B}$. So $\star F(U_0,\cdot)$ recovers $c\mathbf{B}$. The construction is consistent: $F$ and $\star F$, contracted with the observer's four-velocity, return $\mathbf{E}$ and $c\mathbf{B}$ respectively.

> [!note]- Complete formal solution
> The covariant matrix has $\mathbf{E}$ in the time-space block ($F_{0i} = E_i$) and $c\mathbf{B}$ in the space-space block ($F_{ij} = -c\epsilon_{ijk}B^k$). Raising indices in mostly-minus flips the time-space block ($F^{0i} = -E_i$) and leaves the space-space block ($F^{ij} = F_{ij}$). The Hodge dual $(\star F)_{\alpha\beta} = \tfrac12\epsilon_{\alpha\beta\mu\nu}F^{\mu\nu}$ has $(\star F)_{0i} = cB^i$, $(\star F)_{ij} = \epsilon_{ijk}E^k$, i.e. $F$ with $\mathbf{E}\to-c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$. Contracting with $U_0 = e_0$: $F(\cdot,U_0)$ gives the column $F_{\alpha0}$, recovering $\mathbf{E}$; $\star F(U_0,\cdot)$ gives the row $(\star F)_{0\beta}$, recovering $c\mathbf{B}$. $\blacksquare$

---

# Key Takeaways

**The field tensor is a matrix with $\mathbf{E}$ and $c\mathbf{B}$ in its two blocks, and fluency with it is the basic skill of the chapter.** Every covariant electromagnetic computation begins by assembling $F_{\alpha\beta}$ from the physical fields, and the layout — $\mathbf{E}$ in the time-space block ($F_{0i} = E_i$), $c\mathbf{B}$ in the space-space block ($F_{ij} = -c\epsilon_{ijk}B^k$) — is worth committing to muscle memory. The trigger "I have $\mathbf{E}$ and $\mathbf{B}$ and need to do something covariant" reacts to "write the matrix". Once $F$ is on the page, boosting, computing invariants, and finding forces are all matrix operations. This drill builds the fluency that makes the harder exercises (field transformation, invariants, trajectories) routine.

**Index-raising in mostly-minus flips the time-space block only.** The single most error-prone step in field-tensor work is raising indices: in $\mathrm{diag}(+1,-1,-1,-1)$, a time-space entry $F_{0i}$ flips sign on raising (one factor of $-1$) while a space-space entry $F_{ij}$ does not (two factors cancel). So $F^{0i} = -E_i$ but $F^{ij} = F_{ij}$. Getting this backwards corrupts every contraction downstream — the invariants come out with wrong signs, the forces point the wrong way. The reusable rule is "count the spatial indices; each contributes a minus on raising", and the immediate corollary is that the electric block of $F$ behaves oppositely to the magnetic block under raising. This is also why the two invariants have the relative sign they do, $I_1 = c^2\mathbf{B}^2 - \mathbf{E}^2$.

**The Hodge star exchanges electric and magnetic.** Computing $\star F$ and finding it is $F$ with $\mathbf{E}\to-c\mathbf{B}$, $c\mathbf{B}\to\mathbf{E}$ reveals the deep electric–magnetic *duality* of the electromagnetic field: the Hodge star, which depends only on the metric and orientation, rotates the electric field into the magnetic and vice versa. This is the operation behind the second invariant $I_2 = \tfrac14(\star F)_{\mu\nu}F^{\mu\nu} = c\,\mathbf{E}\cdot\mathbf{B}$, behind the self-dual/anti-self-dual decomposition (the $\pm i$ eigenspaces of $\star$, since $\star^2 = -1$ here), and behind the electric–magnetic duality of source-free Maxwell theory. Recognising $\star$ as "swap $\mathbf{E}$ and $c\mathbf{B}$ (with a sign)" is a reusable shortcut that avoids re-deriving the dual matrix each time, and it foreshadows the role of duality in theories with magnetic monopoles.
