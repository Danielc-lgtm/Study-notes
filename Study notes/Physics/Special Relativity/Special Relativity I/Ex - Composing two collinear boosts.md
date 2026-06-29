---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Rapidity"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Problem Statement

Two Lorentz boosts along the same ($x$) axis, of velocities $v_1$ and $v_2$, are applied in succession. (Work with $c = 1$.)

1. Write each boost as a $2\times 2$ matrix acting on $(t, x)^{\mathsf T}$, and multiply the matrices to obtain the composite transformation.
2. Show that the composite is *again a boost* — a matrix of the same form — and read off its velocity
$$
v_{12} = \frac{v_1 + v_2}{1 + v_1 v_2}.
$$
This is the [[Thm - Relativistic Velocity Addition|relativistic velocity-addition law]], derived as the composition of boosts.
3. Redo the computation in [[Def - Rapidity|rapidity]] variables ($v_i = \tanh\varphi_i$): show the composite boost has rapidity $\varphi_1 + \varphi_2$, so that **boosts compose by adding rapidities**, and recover the velocity law from $\tanh(\varphi_1 + \varphi_2)$.
4. Conclude that the boosts along a fixed axis form a one-parameter group isomorphic to $(\mathbb{R}, +)$, and explain why this forces $|v_{12}| < 1$ whenever $|v_1|, |v_2| < 1$ — you cannot reach the speed of light by composing sub-light boosts.

**Recall:**

![[Def - The Lorentz Transformation#The Definition]]

A boost along $x$ with $c = 1$ has matrix $\begin{pmatrix} \gamma & -\gamma v \\ -\gamma v & \gamma \end{pmatrix}$ acting on $(t, x)^{\mathsf T}$, with $\gamma = (1 - v^2)^{-1/2}$. The [[Def - Rapidity|rapidity]] $\varphi$ is defined by $v = \tanh\varphi$, so $\gamma = \cosh\varphi$, $\gamma v = \sinh\varphi$, and the boost matrix becomes $\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}$ (with the sign convention that the boost carrying $S \to S'$ has $-\sinh\varphi$ off-diagonal; here we compose active boosts and use the $+\sinh$ form).

---

# Convergent Strategy

**Problem class.** This is a *structural / group-law* problem: establish that a family of transformations is closed under composition and identify the composition rule. The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] notes that verifying "boosts compose to boosts" and finding the composition law is a recurring structural target.

**Assumption pattern.** The only inputs are the two boost matrices; everything follows from matrix multiplication and the hyperbolic addition identities. The recognition is that the velocity-addition law is *not* an independent postulate but a forced consequence of the boost form — composing two boosts and demanding the result be a boost *is* the addition law.

**Theorem routing.** Two equivalent routes: direct matrix multiplication in velocity variables (giving the algebraic addition law) and multiplication in rapidity variables (giving the trivial additive law). The rapidity route is shorter and exposes the group structure; it connects directly to [[Thm - Relativistic Velocity Addition|relativistic velocity addition]] via $v_{12} = \tanh(\varphi_1 + \varphi_2)$.

**Key decision point.** The illuminating choice is to switch to [[Def - Rapidity|rapidity]] *before* computing. In velocity variables the composite matrix entries are messy and one must factor out the right normalisation to recognise a boost; in rapidity variables the product of two hyperbolic-rotation matrices is *immediately* a hyperbolic rotation through the sum angle (by the addition formulas for $\cosh, \sinh$), and the boost structure is manifest. Recognising that rapidity linearises the group law — turning a nonlinear velocity composition into ordinary addition — is the decisive move and the entire reason rapidity is the "true name" of a boost.

---

# Legal Operations Used

1. **Operation 1 from the topic page (apply Lorentz transformations as matrices).** Each boost is written as a matrix and the composite is their product.

2. **Operation 6 from the topic page (switch to rapidity to make boosts additive).** Step 3 is exactly this operation: rapidity converts the composite into a single hyperbolic rotation through the summed angle.

3. **Operation 5 from the topic page (add velocities relativistically).** The output $v_{12} = (v_1 + v_2)/(1 + v_1 v_2)$ is the relativistic velocity-addition law, here *derived* rather than quoted.

---

# Hints

> [!note]- Hint 1
> Multiply $\begin{pmatrix} \gamma_2 & -\gamma_2 v_2 \\ -\gamma_2 v_2 & \gamma_2 \end{pmatrix}\begin{pmatrix} \gamma_1 & -\gamma_1 v_1 \\ -\gamma_1 v_1 & \gamma_1 \end{pmatrix}$. The off-diagonal-to-diagonal ratio of the product is what gives the composite velocity.

> [!note]- Hint 2
> The composite's top-left entry is $\gamma_1\gamma_2(1 + v_1 v_2)$. Factor this out as the new $\gamma_{12}$; then the new $\gamma_{12} v_{12}$ is $\gamma_1\gamma_2(v_1 + v_2)$, so $v_{12} = (v_1 + v_2)/(1 + v_1 v_2)$.

> [!note]- Hint 3
> In rapidity, multiply $\begin{pmatrix} \cosh\varphi_2 & \sinh\varphi_2 \\ \sinh\varphi_2 & \cosh\varphi_2 \end{pmatrix}\begin{pmatrix} \cosh\varphi_1 & \sinh\varphi_1 \\ \sinh\varphi_1 & \cosh\varphi_1 \end{pmatrix}$ and use $\cosh(a+b) = \cosh a\cosh b + \sinh a \sinh b$, $\sinh(a+b) = \sinh a \cosh b + \cosh a \sinh b$.

> [!note]- Hint 4
> Since $\tanh$ maps all of $\mathbb{R}$ into $(-1, 1)$, the sum $\varphi_1 + \varphi_2$ (any real number) gives $v_{12} = \tanh(\varphi_1 + \varphi_2) \in (-1, 1)$. No finite sum of rapidities reaches $\varphi = \infty$, where $v = 1$.

---

# Solution

Composing two collinear boosts is a matrix product. In velocity variables it yields the relativistic addition law after factoring (Steps 1–2); in rapidity variables it is transparently a single boost through the summed rapidity (Step 3), exhibiting the boosts as a one-parameter group and making the speed-of-light ceiling automatic (Step 4).

**Step 1: The composite matrix.**

> [!note]- Derivation
> Apply boost 1 ($v_1$) then boost 2 ($v_2$); the composite acts as $\Lambda(v_2)\Lambda(v_1)$:
> $$
> \Lambda(v_2)\Lambda(v_1) =
> \begin{pmatrix} \gamma_2 & -\gamma_2 v_2 \\ -\gamma_2 v_2 & \gamma_2 \end{pmatrix}
> \begin{pmatrix} \gamma_1 & -\gamma_1 v_1 \\ -\gamma_1 v_1 & \gamma_1 \end{pmatrix}.
> $$
> Multiply:
> $$
> = \gamma_1\gamma_2
> \begin{pmatrix} 1 + v_1 v_2 & -(v_1 + v_2) \\ -(v_1 + v_2) & 1 + v_1 v_2 \end{pmatrix},
> $$
> where the top-left entry is $\gamma_1\gamma_2(1 \cdot 1 + (-v_2)(-v_1)) = \gamma_1\gamma_2(1 + v_1 v_2)$, the top-right is $\gamma_1\gamma_2(1\cdot(-v_1) + (-v_2)\cdot 1) = -\gamma_1\gamma_2(v_1 + v_2)$, and symmetrically for the bottom row.

**Step 2: It is a boost, with $v_{12} = (v_1 + v_2)/(1 + v_1 v_2)$.**

> [!note]- Derivation
> The composite has the form $\begin{pmatrix} A & -B \\ -B & A \end{pmatrix}$ with $A = \gamma_1\gamma_2(1 + v_1 v_2)$, $B = \gamma_1\gamma_2(v_1 + v_2)$. This is a boost provided $A = \gamma_{12}$ and $B = \gamma_{12} v_{12}$ for some $v_{12}$ with $\gamma_{12} = (1 - v_{12}^2)^{-1/2}$. The velocity is the ratio:
> $$v_{12} = \frac{B}{A} = \frac{\gamma_1\gamma_2(v_1 + v_2)}{\gamma_1\gamma_2(1 + v_1 v_2)} = \frac{v_1 + v_2}{1 + v_1 v_2}.$$
> To confirm $A$ really is the corresponding $\gamma_{12}$, check $A^2 - B^2 = 1$ (the defining relation $\gamma^2 - \gamma^2 v^2 = 1$):
> $$A^2 - B^2 = \gamma_1^2\gamma_2^2\big[(1 + v_1 v_2)^2 - (v_1 + v_2)^2\big] = \gamma_1^2\gamma_2^2(1 - v_1^2)(1 - v_2^2) = \gamma_1^2\gamma_2^2 \cdot \frac{1}{\gamma_1^2}\cdot\frac{1}{\gamma_2^2} = 1,$$
> using the algebraic identity $(1 + ab)^2 - (a + b)^2 = (1 - a^2)(1 - b^2)$. So $A = \gamma_{12}$, the composite is a genuine boost, and its velocity is the [[Thm - Relativistic Velocity Addition|relativistic sum]] $v_{12} = (v_1 + v_2)/(1 + v_1 v_2)$ — *not* $v_1 + v_2$.

**Step 3: In rapidity, $\varphi_{12} = \varphi_1 + \varphi_2$.**

> [!note]- Derivation
> Write $v_i = \tanh\varphi_i$, so the boost matrices are hyperbolic rotations:
> $$
> \begin{pmatrix} \cosh\varphi_2 & \sinh\varphi_2 \\ \sinh\varphi_2 & \cosh\varphi_2 \end{pmatrix}
> \begin{pmatrix} \cosh\varphi_1 & \sinh\varphi_1 \\ \sinh\varphi_1 & \cosh\varphi_1 \end{pmatrix}.
> $$
> The top-left entry is $\cosh\varphi_2\cosh\varphi_1 + \sinh\varphi_2\sinh\varphi_1 = \cosh(\varphi_1 + \varphi_2)$, and the top-right is $\cosh\varphi_2\sinh\varphi_1 + \sinh\varphi_2\cosh\varphi_1 = \sinh(\varphi_1 + \varphi_2)$, by the hyperbolic addition formulas. So the product is
> $$
> \begin{pmatrix} \cosh(\varphi_1 + \varphi_2) & \sinh(\varphi_1 + \varphi_2) \\ \sinh(\varphi_1 + \varphi_2) & \cosh(\varphi_1 + \varphi_2) \end{pmatrix},
> $$
> a boost of rapidity $\varphi_{12} = \varphi_1 + \varphi_2$. Rapidities simply *add*. The velocity law follows instantly:
> $$v_{12} = \tanh(\varphi_1 + \varphi_2) = \frac{\tanh\varphi_1 + \tanh\varphi_2}{1 + \tanh\varphi_1\tanh\varphi_2} = \frac{v_1 + v_2}{1 + v_1 v_2},$$
> reproducing Step 2 in one line. The hyperbolic-tangent addition formula *is* the relativistic velocity-addition law.

**Step 4: The boosts form a one-parameter group; $|v_{12}| < 1$ is automatic.**

> [!note]- Derivation
> The map $\varphi \mapsto \Lambda[\varphi]$ (boost of rapidity $\varphi$) satisfies $\Lambda[\varphi_2]\Lambda[\varphi_1] = \Lambda[\varphi_1 + \varphi_2]$, $\Lambda[0] = I$ (the identity), and $\Lambda[\varphi]^{-1} = \Lambda[-\varphi]$. These are exactly the axioms of a group homomorphism from $(\mathbb{R}, +)$, so the boosts along the $x$-axis form a **one-parameter group isomorphic to $(\mathbb{R}, +)$** — a one-dimensional subgroup of the [[Def - The Lorentz Group|Lorentz group]], with rapidity as the canonical additive coordinate.
>
> The speed limit is now automatic. Rapidity ranges over *all* of $\mathbb{R}$, but $v = \tanh\varphi$ maps $\mathbb{R}$ into the open interval $(-1, 1)$: $\tanh$ is bounded, approaching $\pm 1$ only as $\varphi \to \pm\infty$. So for *any* finite rapidities $\varphi_1, \varphi_2$ — equivalently any sub-light $v_1, v_2$ — the sum $\varphi_1 + \varphi_2$ is finite, hence $v_{12} = \tanh(\varphi_1 + \varphi_2) \in (-1, 1)$ strictly. You can add rapidities without bound, but the corresponding velocity never reaches $1$; the speed of light is rapidity *infinity*, unreachable by any finite composition. This is the structural explanation of why no chain of sub-light boosts ever attains $c$.

> [!note]- Complete formal solution
> Compose the boosts as matrices: $\Lambda(v_2)\Lambda(v_1) = \gamma_1\gamma_2\begin{pmatrix} 1 + v_1 v_2 & -(v_1+v_2) \\ -(v_1+v_2) & 1 + v_1 v_2 \end{pmatrix}$. This has boost form $\begin{pmatrix} \gamma_{12} & -\gamma_{12}v_{12} \\ -\gamma_{12}v_{12} & \gamma_{12} \end{pmatrix}$ with $v_{12} = (v_1+v_2)/(1+v_1v_2)$; the check $A^2 - B^2 = \gamma_1^2\gamma_2^2(1-v_1^2)(1-v_2^2) = 1$ confirms it is a genuine boost. In rapidity ($v_i = \tanh\varphi_i$), the product of the two hyperbolic-rotation matrices is the hyperbolic rotation through $\varphi_1 + \varphi_2$ (by the $\cosh/\sinh$ addition formulas), so boosts add rapidities and $v_{12} = \tanh(\varphi_1 + \varphi_2)$. The map $\varphi \mapsto \Lambda[\varphi]$ is a homomorphism from $(\mathbb{R},+)$, so collinear boosts form a one-parameter group; since $\tanh: \mathbb{R} \to (-1,1)$, any finite rapidity sum gives $|v_{12}| < 1$, so sub-light boosts never compose to $c$. $\blacksquare$

> [!warning] Illegal but tempting: adding velocities directly
> The Galilean reflex is to write $v_{12} = v_1 + v_2$. This is wrong except to first order: composing two boosts of $v_1 = v_2 = 0.8$ would give $1.6 > 1$, a superluminal nonsense, whereas the correct law gives $v_{12} = 1.6/1.64 \approx 0.976 < 1$. The error is to treat the boost matrices as commuting *translations* (which would add their parameters) rather than as hyperbolic *rotations* (whose parameters, the rapidities, add — but whose velocities do not). The repair is to compose in rapidity, where addition *is* legal, and convert back with $\tanh$ at the end.

---

# Key Takeaways

**The velocity-addition law is the boost composition law, not an extra postulate — composing transformations *is* combining velocities.** The conceptual upgrade from this exercise is to stop thinking of relativistic velocity addition as a strange standalone formula and start thinking of it as the inevitable consequence of composing two boosts. When you apply one boost then another, the result must again be a valid transformation between inertial frames (the [[Def - The Lorentz Group|Lorentz group]] is closed), and *demanding* the composite have boost form *forces* $v_{12} = (v_1 + v_2)/(1 + v_1 v_2)$. The reusable principle: whenever a "law of combination" appears in physics (adding velocities, composing rotations, stacking phase shifts), suspect it is really the group law of an underlying symmetry, and derive it by composing the corresponding transformations. This reframing turns a memorised formula into a structural necessity and tells you immediately how to handle non-collinear cases (compose the full matrices) where the naive formula fails.

**Rapidity is the additive coordinate that linearises the boost group, and switching to it is the standard move whenever boosts are composed, iterated, or inverted.** The single most valuable habit here is to convert velocities to [[Def - Rapidity|rapidities]] before doing anything involving composition. In velocity variables the group law is the nonlinear $\oplus$; in rapidity variables it is ordinary $+$, because the boost is literally a hyperbolic rotation and rotation angles add. This is exactly analogous to how, for ordinary rotations, *angles* add while the rotation matrices multiply — rapidity is the hyperbolic angle. The trigger to switch: any problem with multiple boosts, any iterated boost ($N$ boosts of rapidity $\varphi$ give rapidity $N\varphi$), any boost inverse ($\varphi \to -\varphi$), or any appearance of the velocity-addition formula's nonlinearity getting in the way. Rapidity also makes the relativistic Doppler factor multiplicative ($k = e^\varphi$, see [[Ex - The k-calculus (Bondi) derivation|the k-calculus]]) and the speed limit obvious ($c$ is $\varphi = \infty$).

**A one-parameter subgroup connected to the identity has a canonical additive coordinate, and the boundedness of the physical parameter ($|v| < c$) is the image of an unbounded additive one under a bounded map.** The boosts along an axis are a one-parameter group isomorphic to $(\mathbb{R}, +)$, with rapidity the coordinate; this is the simplest nontrivial fragment of the [[Def - The Lorentz Group|Lorentz group]]'s Lie structure, and recognising it explains the speed limit without any dynamics. Rapidity is unbounded ($\mathbb{R}$), velocity is bounded ($(-1,1)$), and the bounded one is the image of the unbounded one under $\tanh$ — so "you cannot reach $c$" is the geometric statement "you cannot reach $\varphi = \infty$ by finite addition". The transferable insight: when a physical quantity has a hard ceiling it can approach but never attain (terminal velocity, maximum entropy, a saturating response), look for an underlying *additive* variable that is unbounded, related to the physical one by a bounded function — the ceiling is then a soft consequence of the function's asymptote, not a hard external constraint, and the additive variable is usually the one in which the dynamics is simple.
