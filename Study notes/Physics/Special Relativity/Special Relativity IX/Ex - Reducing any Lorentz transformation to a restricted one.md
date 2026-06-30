---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Subgroups and Components of the Lorentz Group"
  - "Thm - The Restricted Lorentz Group is a Normal Subgroup"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\Lambda \in O(1,3)$ be an arbitrary Lorentz transformation. Using the discrete reflections
$$
I = -\mathrm{Id}, \qquad P = \mathrm{diag}(1,-1,-1,-1), \qquad T = \mathrm{diag}(-1,1,1,1),
$$
show that exactly one of $\Lambda$, $I\Lambda$, $P\Lambda$, $T\Lambda$ lies in the restricted group $SO^+(1,3)$, and give the recipe (in terms of $\mathrm{sgn}(\det\Lambda)$ and $\mathrm{sgn}(\Lambda^0{}_0)$) for which one. Then apply the recipe to the explicit transformation
$$
\Lambda = \begin{pmatrix} -\cosh\psi & -\sinh\psi & 0 & 0 \\ -\sinh\psi & -\cosh\psi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix},
$$
classifying its component and writing it as a reflection times a restricted transformation.

**Recall:**

![[Def - Subgroups and Components of the Lorentz Group#The Definition]]

The reflections have components $I \in SO_{\text{anti}}$ ($\det = +1$, $I^0{}_0 = -1$), $P \in O^-_{\text{orth}}$ ($\det = -1$, $P^0{}_0 = +1$), $T \in O^-_{\text{anti}}$ ($\det = -1$, $T^0{}_0 = -1$). They are involutions: $I^2 = P^2 = T^2 = \mathrm{Id}$, and $I = PT = TP$.

---

# Convergent Strategy

**Problem class.** A *reduction-to-normal-form* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: given an element of a group with several components, reduce it to the identity component by multiplying by a coset representative. The component is read from two locally-constant invariants, and the correct reflection is the one that flips both invariants to $(+,+)$.

**Assumption pattern.** The two sign invariants $\det\Lambda \in \{\pm 1\}$ and $\mathrm{sgn}\,\Lambda^0{}_0 \in \{\pm 1\}$ classify $\Lambda$ into one of four components. Multiplying by a reflection adds (in $\mathbb{Z}/2\times\mathbb{Z}/2$) the reflection's signs to $\Lambda$'s, so the reflection that lands $\Lambda$ in $SO^+(1,3)$ is the one whose signs are the *inverse* of $\Lambda$'s — and since each reflection is its own inverse, it is the one with the same nonidentity sign pair.

**Theorem routing.** The reduction routes through the [[Thm - The Restricted Lorentz Group is a Normal Subgroup|normal-subgroup theorem]]: $O(1,3) = SO^+(1,3) \sqcup I\cdot SO^+ \sqcup P\cdot SO^+ \sqcup T\cdot SO^+$, so $\Lambda$ lies in exactly one coset, and the coset representative $\in \{\mathrm{Id}, I, P, T\}$ is determined by $\Lambda$'s signs. Left-multiplying by that representative (an involution) yields the restricted part.

**Key decision point.** The non-obvious step is realising the reflection is chosen by *matching* $\Lambda$'s sign pair, not by some computation on the matrix entries. The recipe: if $\det\Lambda = +1, \Lambda^0{}_0 \ge 1$, take $\mathrm{Id}$; if $\det = +1, \Lambda^0{}_0 \le -1$, take $I$; if $\det = -1, \Lambda^0{}_0 \ge 1$, take $P$; if $\det = -1, \Lambda^0{}_0 \le -1$, take $T$. The natural-but-wrong alternative is to guess the reflection from the matrix's appearance (e.g. "it has a minus sign, so use $P$"), which fails because the same matrix can carry several minus signs that conspire.

---

# Legal Operations Used

1. **Read the component of $\Lambda$ from its two signs** (operation 1 from the topic page): compute $\det\Lambda$ and $\mathrm{sgn}\,\Lambda^0{}_0$ to place $\Lambda$ in one of the four components.

2. **Reduce to a restricted transformation by a reflection** (operation 2 from the topic page): left-multiply by the reflection matching $\Lambda$'s nonidentity sign pair, using that each reflection is an involution so the reduction is its own inverse.

---

# Hints

> [!note]- Hint 1
> Compute the two invariants of the given $\Lambda$: its determinant and the sign of its time–time entry $\Lambda^0{}_0$.

> [!note]- Hint 2
> Match the sign pair to a reflection. The reflection $R \in \{\mathrm{Id}, I, P, T\}$ that works has the *same* nonidentity sign pair as $\Lambda$, so that $R\Lambda$ has signs $(+,+)$.

> [!note]- Hint 3
> For the explicit matrix: $\det\Lambda = (-\cosh\psi)(-\cosh\psi) - (-\sinh\psi)(-\sinh\psi)$ on the upper block, times $1\cdot(-1)$ on the lower block. And $\Lambda^0{}_0 = -\cosh\psi \le -1$. Find the matching reflection and multiply.

---

# Solution

The solution is the recipe followed by its application. We first establish that exactly one reflection lands $\Lambda$ in $SO^+(1,3)$, determined by $\Lambda$'s sign pair; then we compute the two invariants of the given matrix and apply the matching reflection.

**Step 1: Exactly one reflection works, matched to the sign pair.**

> [!note]- Derivation
> The sign map $\sigma : O(1,3) \to \mathbb{Z}/2\times\mathbb{Z}/2$, $\sigma(\Lambda) = (\tfrac{1-\det\Lambda}{2}, \tfrac{1-\mathrm{sgn}\Lambda^0{}_0}{2})$, is a homomorphism with $\sigma(\mathrm{Id}) = (0,0)$, $\sigma(I) = (0,1)$, $\sigma(P) = (1,0)$, $\sigma(T) = (1,1)$ — the four reflections realising the four classes. For $R\Lambda$ to be restricted we need $\sigma(R\Lambda) = (0,0)$, i.e. $\sigma(R) + \sigma(\Lambda) = (0,0)$ in $\mathbb{Z}/2\times\mathbb{Z}/2$, i.e. $\sigma(R) = -\sigma(\Lambda) = \sigma(\Lambda)$ (every element is its own inverse). So $R$ is the unique reflection with $\sigma(R) = \sigma(\Lambda)$:
> $$\sigma(\Lambda) = (0,0) \Rightarrow R = \mathrm{Id}; \quad (0,1) \Rightarrow R = I; \quad (1,0) \Rightarrow R = P; \quad (1,1) \Rightarrow R = T.$$
> Since each reflection is an involution, $R^{-1} = R$, and $\Lambda = R(R\Lambda) = R\Lambda_0$ with $\Lambda_0 = R\Lambda \in SO^+(1,3)$. Exactly one $R$ works because $\sigma(\Lambda)$ is a single element of the quotient.

**Step 2: The invariants of the given matrix.**

> [!note]- Derivation
> *Determinant.* The matrix is block-diagonal: the upper $2\times 2$ block $\begin{pmatrix} -\cosh\psi & -\sinh\psi \\ -\sinh\psi & -\cosh\psi \end{pmatrix}$ has determinant $\cosh^2\psi - \sinh^2\psi = 1$; the lower block $\mathrm{diag}(1, -1)$ has determinant $-1$. So $\det\Lambda = 1\cdot(-1) = -1$ (improper).
>
> *Time-component.* $\Lambda^0{}_0 = -\cosh\psi \le -1$ (antichronous).
>
> So $\sigma(\Lambda) = (\tfrac{1-(-1)}{2}, \tfrac{1-(-1)}{2}) = (1, 1)$: the component is improper-antichronous, $O^-_{\text{anti}}(1,3)$.

**Step 3: Apply the matching reflection.**

> [!note]- Derivation
> By Step 1, $\sigma(\Lambda) = (1,1)$ requires $R = T = \mathrm{diag}(-1,1,1,1)$. Compute $\Lambda_0 = T\Lambda$:
> $$T\Lambda = \mathrm{diag}(-1,1,1,1)\begin{pmatrix} -\cosh\psi & -\sinh\psi & 0 & 0 \\ -\sinh\psi & -\cosh\psi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix} = \begin{pmatrix} \cosh\psi & \sinh\psi & 0 & 0 \\ -\sinh\psi & -\cosh\psi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}.$$
> Check: $\det(T\Lambda) = \det T\det\Lambda = (-1)(-1) = +1$ (proper), and $(T\Lambda)^0{}_0 = \cosh\psi \ge 1$ (orthochronous). So $\Lambda_0 = T\Lambda \in SO^+(1,3)$, and $\Lambda = T\Lambda_0$ since $T^2 = \mathrm{Id}$.
>
> The restricted part $\Lambda_0$ is a boost of rapidity $-\psi$ in the $(e_0, e_1)$-plane (note the $-\sinh\psi, -\cosh\psi$ in the second row) composed with a rotation by $\pi$ in the $(e_1, e_3)$... more precisely $\Lambda_0 = \mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ -\sinh\psi & -\cosh\psi\end{smallmatrix}, 1, -1\big)$; reading it, the lower block $\mathrm{diag}(1,-1)$ on $(e_2, e_3)$ is a rotation by $\pi$ about $e_2$... so $\Lambda_0$ is a four-screw (boost in $(e_0,e_1)$ times a $\pi$-rotation), confirming it is restricted. The decomposition $\Lambda = T\Lambda_0$ exhibits $\Lambda$ as time-reversal times a restricted transformation.

> [!note]- Complete formal solution
> The sign map $\sigma : O(1,3) \to \mathbb{Z}/2\times\mathbb{Z}/2$ is a homomorphism, and $R\Lambda \in SO^+(1,3)$ iff $\sigma(R) = \sigma(\Lambda)$ (since $\sigma$ is its own inverse on each element). As $\sigma$ takes the reflections $\{\mathrm{Id}, I, P, T\}$ bijectively to the four classes, exactly one reflection $R$ matches $\sigma(\Lambda)$, and $\Lambda = R(R\Lambda)$ with $R\Lambda$ restricted.
>
> For the given $\Lambda$: $\det\Lambda = (1)(-1) = -1$ (upper block determinant $\cosh^2-\sinh^2 = 1$, lower block $-1$) and $\Lambda^0{}_0 = -\cosh\psi \le -1$, so $\sigma(\Lambda) = (1,1)$, matching $T$. Then $\Lambda_0 = T\Lambda = \mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ -\sinh\psi & -\cosh\psi\end{smallmatrix}, 1, -1\big)$ has $\det = +1$, $\Lambda_0^0{}_0 = \cosh\psi \ge 1$, so $\Lambda_0 \in SO^+(1,3)$, and $\Lambda = T\Lambda_0$. $\blacksquare$

---

# Key Takeaways

**Reducing to the identity component is matching, not computing.** The reflection that lands an arbitrary $\Lambda$ in the restricted group is determined entirely by $\Lambda$'s two signs — its determinant and the sign of its time-component — and is the reflection carrying the *same* nonidentity sign pair. There is no need to inspect the matrix entries beyond computing these two signs. The general principle for any group with a finite component group $\pi_0$: reduce to the identity component by multiplying by the coset representative matching the element's image in $\pi_0$. The trigger is "an element of a disconnected group"; the move is "compute the component invariants, multiply by the matching representative." Here the component invariants are $\det$ and $\mathrm{sgn}\,\Lambda^0{}_0$, and the representatives are the reflections $I, P, T$.

**The four reflections are a complete set of coset representatives because they realise the Klein four-group.** Any one nonidentity reflection (say $P$) generates only a $\mathbb{Z}/2$ and reaches only two of the four components; reducing an *arbitrary* $\Lambda$ requires all three nonidentity reflections, because the component group is $\mathbb{Z}/2\times\mathbb{Z}/2$, not $\mathbb{Z}/2$. This is the practical consequence of the Lorentz group having two independent reflections (in time and in space) rather than the single orientation reflection of the Euclidean group. When you find yourself needing more than one reflection to reduce a transformation, that is the component group $\pi_0$ being non-cyclic, and it is a signal that the geometry has two independent reflection symmetries.

**The same matrix can carry several minus signs that combine, so always compute the invariants rather than eyeballing.** The given matrix has minus signs scattered through it — in the upper block, in the lower block — yet its determinant is $-1$ and its time-component is negative, a combination one cannot read off by counting minus signs. The determinant aggregates all the sign information multiplicatively, and the time-component is a single entry; only these two aggregated invariants determine the component. The lesson, transferable to any classification by locally-constant invariants, is to compute the invariants honestly (here a $2\times 2$ block determinant and one matrix entry) rather than guessing from surface features, because the surface features can conspire to mislead.
