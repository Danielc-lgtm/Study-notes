---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Rapidity"
  - "Def - Boosts as Hyperbolic Rotations"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. A boost along $x$ of [[Def - Rapidity|rapidity]] $\varphi$ is the [[Def - Boosts as Hyperbolic Rotations|hyperbolic rotation]] $\Lambda[\varphi] = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}$ on $(t, x)$, with $v = \tanh\varphi$, $\gamma = \cosh\varphi$. Velocities of successive boosts are $v_1, v_2$ with rapidities $\varphi_1 = \tanh^{-1}v_1$, $\varphi_2 = \tanh^{-1}v_2$. Full registry on [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group]].

---

# Statement

> **Composition of collinear boosts (rapidity additivity).** For two boosts along the same axis, with rapidities $\varphi_1$ and $\varphi_2$,
> $$\Lambda[\varphi_1]\,\Lambda[\varphi_2] \;=\; \Lambda[\varphi_1 + \varphi_2].$$
> Consequently the boosts along a fixed direction form a one-parameter subgroup of $SO^+(1,3)$ isomorphic to the additive group $(\mathbb{R}, +)$, and the composed velocity is
> $$v = \tanh(\varphi_1 + \varphi_2) = \frac{v_1 + v_2}{1 + v_1 v_2}\qquad\Big(\text{with } c:\ v = \frac{v_1 + v_2}{1 + v_1 v_2/c^2}\Big),$$
> which is the [[Thm - Relativistic Velocity Addition|relativistic velocity-addition law]].

> **Remark (non-collinear boosts do not simply add).** If the two boosts are along *different* directions, their product is *not* a pure boost: it is a boost composed with a spatial rotation, the **Thomas–Wigner rotation**. Rapidity additivity is special to the collinear case.

---

# Motivation

The relativistic velocity-addition law $v = (v_1 + v_2)/(1 + v_1 v_2)$ is one of the first genuinely strange formulas of special relativity, and on its own it looks like an arbitrary correction to the obvious Galilean rule $v_1 + v_2$. Where does the denominator come from? Why does the formula conspire to keep $c$ as a ceiling? Stated in velocities, these questions have no transparent answer.

This theorem supplies the answer by changing coordinates. In [[Def - Rapidity|rapidity]] the composition law is the simplest law there is — addition — and the bizarre velocity formula is exposed as nothing more than the addition formula for the hyperbolic tangent. The motivation for proving the theorem is to make the velocity-addition law *unsurprising*: once you know boosts are [[Def - Boosts as Hyperbolic Rotations|hyperbolic rotations]] and that the natural parameter of a one-parameter rotation family adds (as angles do for circular rotations), the velocity law is forced, and its every peculiarity — the denominator, the $c$-ceiling, the $c$-fixed-point — becomes a property of $\tanh$.

The theorem also installs the group-theoretic fact that the collinear boosts form a one-parameter subgroup $\cong (\mathbb{R}, +)$. This is the relativistic analogue of "rotations about a fixed axis form the circle group $SO(2)$", with the crucial difference that the boost group is the *line*, not the circle — non-compact, non-periodic, unbounded. That difference is exactly why velocity has a ceiling: the additive parameter runs to infinity, but its image under $\tanh$ only approaches $1$.

The remark about non-collinear boosts is not a footnote; it is a warning that the additive simplicity is fragile. Two boosts along different axes compose to a boost *times a rotation*, and that extra rotation — the Thomas rotation — is responsible for the spin–orbit coupling in atomic physics and the precession of gyroscopes in orbit. Rapidity additivity holds *only* when the boosts are parallel, and conflating the collinear case with the general case is a classic error.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "two boosts along the same axis". Recognising this hypothesis in disguise is the skill.

The first disguised source is **"a velocity is measured relative to a moving frame, both motions along one line"**. Whenever a problem says "$A$ moves at $v_1$ relative to $B$, and $B$ moves at $v_2$ relative to $C$, all collinear", that *is* a composition of two collinear boosts, and the theorem applies: convert to rapidities, add, convert back. The bridge is that "change of frame" is "apply a boost", so two successive frame changes are two successive boosts. *Example problem:* a rocket fires a probe at $0.8c$ relative to itself while moving at $0.8c$ relative to Earth; find the probe's Earth-frame speed by adding rapidities $\tanh^{-1}(0.8) + \tanh^{-1}(0.8)$.

The second disguised source is **"a chain of many collinear boosts"**. An $N$-fold composition $\Lambda[\varphi_1]\cdots\Lambda[\varphi_N]$ collapses to $\Lambda[\varphi_1 + \cdots + \varphi_N]$ by induction. The bridge is associativity of the group together with the two-boost rule. The nonobviousness is that iterating the velocity formula $N$ times is a nightmare, while summing $N$ rapidities is trivial. *Example problem:* a particle is accelerated by $N$ successive identical kicks each adding rapidity $\Delta\varphi$ in its instantaneous rest frame; its final velocity is $\tanh(N\Delta\varphi)$, which $\to 1$ but never reaches it — the relativistic rocket problem.

The third disguised source is **"the Doppler factors multiply"**. If you know the [[Def - Rapidity|Doppler]] factors $k_i = e^{\varphi_i}$ of two collinear boosts, their composition has Doppler factor $k_1 k_2$, because $e^{\varphi_1}e^{\varphi_2} = e^{\varphi_1 + \varphi_2}$. The bridge is $k = e^\varphi$ and rapidity additivity. *Example problem:* light relayed through a chain of receding mirrors, each redshifting by a factor $k$, arrives redshifted by $k^N$ — the rapidities add, the Doppler factors multiply.

**Targets (Output Amplification)**

The conclusion is "$\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1 + \varphi_2]$".

Combine the conclusion with **the unboundedness of $\varphi$ and boundedness of $\tanh$**. Since rapidities add without limit but $v = \tanh\varphi < 1$ always, no finite chain of sub-light boosts reaches $c$. The further result is the *unattainability of the speed of light* by acceleration — a structural fact, not a numerical accident. The combination is useful because it converts the awkward "can you reach $c$?" question into the transparent "$\tanh$ has horizontal asymptotes". *Example:* the relativistic rocket never reaches $c$ no matter how long it burns.

Combine the conclusion with **the inverse being $\Lambda[-\varphi]$**. Additivity gives $\Lambda[\varphi]\Lambda[-\varphi] = \Lambda[0] = I$, so undoing a boost is subtracting its rapidity. The further result is a clean formula for *relative velocity*: the velocity of frame $2$ as seen by frame $1$ has rapidity $\varphi_2 - \varphi_1$, hence $v_{\text{rel}} = \tanh(\varphi_2 - \varphi_1) = (v_2 - v_1)/(1 - v_1 v_2)$. The combination is nonobvious because the *difference* of rapidities gives the relative velocity directly, bypassing any frame-by-frame transformation. *Example:* two particles in a collider with rapidities $\varphi_1, \varphi_2$ approach each other at $\tanh(\varphi_1 + \varphi_2)$ (head-on) — the closing speed.

Combine the conclusion with **a non-collinear second boost**. The clean additivity *fails*, and the failure is itself a result: the product acquires a rotation. The further result is the **Thomas–Wigner rotation** and, taking the rotation rate, the **Thomas precession** $\boldsymbol{\omega}_T = \tfrac{\gamma^2}{\gamma+1}\,\mathbf{a}\times\mathbf{v}$ of an accelerated spin. The combination is useful because it tells you exactly when the simple picture breaks and what replaces it. *Example:* the spin–orbit coupling correction in the hydrogen atom is a Thomas-precession effect.

---

# Why Is It True

The theorem is true for the same reason that rotation angles add: **the natural parameter of a one-parameter group of "rotations" is additive, and rapidity is that parameter for boosts**. The cleanest way to see it is to put the boost in the coordinates where it is diagonal.

A boost is diagonal in light-cone (null) coordinates. Set $u = t + x$ and $w = t - x$; then the boost $\Lambda[\varphi]$ acts as $u \mapsto e^{\varphi}u$ and $w \mapsto e^{-\varphi}w$ (because $(1, 1)$ and $(1, -1)$ are the eigenvectors, with eigenvalues $e^{\pm\varphi}$ — see [[Def - Boosts as Hyperbolic Rotations]]). Composition is now obvious: applying $\Lambda[\varphi_2]$ then $\Lambda[\varphi_1]$ multiplies the $u$-coordinate by $e^{\varphi_1}e^{\varphi_2} = e^{\varphi_1 + \varphi_2}$ and the $w$-coordinate by $e^{-\varphi_1}e^{-\varphi_2} = e^{-(\varphi_1 + \varphi_2)}$. That is precisely $\Lambda[\varphi_1 + \varphi_2]$. **In light-cone coordinates a boost is a multiplication by $e^{\pm\varphi}$, so composing boosts multiplies exponentials, and multiplying exponentials adds exponents — which is rapidity additivity.**

This is the same mechanism that makes rotation angles add, viewed through the right coordinates. A rotation is diagonal in the *complex* null coordinates $z = x + iy$, $\bar z = x - iy$, acting as $z \mapsto e^{i\theta}z$; composing rotations multiplies $e^{i\theta_1}e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$, so angles add. The boost is the same story with the imaginary angle $i\theta$ replaced by the real rapidity $\varphi$ — circular eigenvalues $e^{\pm i\theta}$ on the unit circle become hyperbolic eigenvalues $e^{\pm\varphi}$ on the real axis. The additive structure is identical; only the reality of the exponent differs.

The velocity-addition law then *follows* rather than being assumed. The velocity is $v = \tanh\varphi = (e^\varphi - e^{-\varphi})/(e^\varphi + e^{-\varphi})$, the ratio that measures how lopsided the two null-stretch factors are. When you add rapidities, $\tanh$'s addition formula $\tanh(\varphi_1 + \varphi_2) = (\tanh\varphi_1 + \tanh\varphi_2)/(1 + \tanh\varphi_1\tanh\varphi_2)$ delivers the velocity law with its characteristic denominator. The denominator is just the cross term in the product of two exponentials; it is not put in by hand.

---

# What Makes This Hard

The computation itself is short, and the only genuine subtlety is conceptual: it is tempting to think the theorem says velocities add, when it says *rapidities* add and velocities therefore combine by $\tanh$ of a sum. The most common error is to apply rapidity additivity to *non-collinear* boosts, where it is false — two boosts along different axes give a boost *times a Thomas rotation*, and forgetting that rotation is the standard pitfall (it is the historical reason the hydrogen fine-structure factor was initially off by a factor of two). The matrix multiplication, if done in velocity variables, is also error-prone because the $\gamma$ factors hide the structure; doing it in rapidity (or in null coordinates) is where the proof becomes transparent.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Multiply the two hyperbolic-rotation matrices and use the hyperbolic addition formulas $\cosh(\varphi_1 + \varphi_2) = \cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2$ and $\sinh(\varphi_1 + \varphi_2) = \sinh\varphi_1\cosh\varphi_2 + \cosh\varphi_1\sinh\varphi_2$. Then read off the velocity via $\tanh$. (Alternative: diagonalise both boosts in null coordinates, where each is $\mathrm{diag}(e^{\varphi}, e^{-\varphi})$, and multiply diagonals.)

**Subgoal decomposition:**

1. **Write both boosts as $2\times 2$ hyperbolic-rotation matrices.** $\Lambda[\varphi_i] = \begin{pmatrix} \cosh\varphi_i & \sinh\varphi_i \\ \sinh\varphi_i & \cosh\varphi_i \end{pmatrix}$.
   - *Hint:* This is the rapidity form of the boost; the $y, z$ block is the identity and contributes nothing.
   - *Why needed:* It exposes the entries that the hyperbolic addition formulas will combine.

2. **Multiply and apply the hyperbolic addition formulas.** Compute the four entries of the product and recognise each as $\cosh$ or $\sinh$ of $\varphi_1 + \varphi_2$.
   - *Hint:* The $(1,1)$ entry is $\cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2 = \cosh(\varphi_1 + \varphi_2)$.
   - *Why needed:* It is the entire content of the matrix identity.

3. **Read off the velocity with $\tanh$.** The composed boost is $\Lambda[\varphi_1 + \varphi_2]$, so $v = \tanh(\varphi_1 + \varphi_2)$; expand to recover $(v_1 + v_2)/(1 + v_1 v_2)$.
   - *Hint:* Use $\tanh(a+b) = (\tanh a + \tanh b)/(1 + \tanh a\tanh b)$.
   - *Why needed:* It connects the abstract additivity to the concrete velocity-addition law.

---

# Lemma Decomposition

> [!note]- Lemma 1: Hyperbolic addition formulas
> **Statement:** $\cosh(\varphi_1 + \varphi_2) = \cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2$ and $\sinh(\varphi_1 + \varphi_2) = \sinh\varphi_1\cosh\varphi_2 + \cosh\varphi_1\sinh\varphi_2$.
>
> **Hint:** Expand using $\cosh\varphi = \tfrac12(e^\varphi + e^{-\varphi})$, $\sinh\varphi = \tfrac12(e^\varphi - e^{-\varphi})$, or differentiate the circular identities under $\varphi = i\theta$.
>
> **Why needed:** These are the identities that turn the matrix product into a single boost; without them the product is an opaque array.
>
> > [!note]- Full proof
> > Write $\cosh\varphi_i = \tfrac12(e^{\varphi_i} + e^{-\varphi_i})$ and $\sinh\varphi_i = \tfrac12(e^{\varphi_i} - e^{-\varphi_i})$. Then
> > $$\cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2 = \tfrac14\Big[(e^{\varphi_1}+e^{-\varphi_1})(e^{\varphi_2}+e^{-\varphi_2}) + (e^{\varphi_1}-e^{-\varphi_1})(e^{\varphi_2}-e^{-\varphi_2})\Big].$$
> > Expanding, the cross terms $e^{\varphi_1}e^{-\varphi_2}$ and $e^{-\varphi_1}e^{\varphi_2}$ cancel between the two products and the like terms double, giving $\tfrac12(e^{\varphi_1 + \varphi_2} + e^{-(\varphi_1+\varphi_2)}) = \cosh(\varphi_1 + \varphi_2)$. The $\sinh$ identity is identical with one sign changed. $\blacksquare$

> [!note]- Lemma 2: The matrix product is a single boost
> **Statement:** $\begin{pmatrix} \cosh\varphi_1 & \sinh\varphi_1 \\ \sinh\varphi_1 & \cosh\varphi_1 \end{pmatrix}\begin{pmatrix} \cosh\varphi_2 & \sinh\varphi_2 \\ \sinh\varphi_2 & \cosh\varphi_2 \end{pmatrix} = \begin{pmatrix} \cosh(\varphi_1+\varphi_2) & \sinh(\varphi_1+\varphi_2) \\ \sinh(\varphi_1+\varphi_2) & \cosh(\varphi_1+\varphi_2) \end{pmatrix}$.
>
> **Hint:** Multiply the matrices entry by entry and apply Lemma 1 to each entry.
>
> **Why needed:** This *is* the theorem $\Lambda[\varphi_1]\Lambda[\varphi_2] = \Lambda[\varphi_1 + \varphi_2]$ in the $(t,x)$ block.
>
> > [!note]- Full proof
> > The $(1,1)$ entry is $\cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2 = \cosh(\varphi_1 + \varphi_2)$ by Lemma 1. The $(1,2)$ entry is $\cosh\varphi_1\sinh\varphi_2 + \sinh\varphi_1\cosh\varphi_2 = \sinh(\varphi_1 + \varphi_2)$. By the symmetry of the matrices the $(2,1)$ entry equals the $(1,2)$ entry and the $(2,2)$ entry equals the $(1,1)$ entry. So the product is the hyperbolic rotation of rapidity $\varphi_1 + \varphi_2$. The transverse $(y,z)$ block is $I \cdot I = I$, unchanged. $\blacksquare$

> [!note]- Lemma 3: The velocity-addition law from tanh
> **Statement:** $\tanh(\varphi_1 + \varphi_2) = (v_1 + v_2)/(1 + v_1 v_2)$ where $v_i = \tanh\varphi_i$.
>
> **Hint:** Divide $\sinh(\varphi_1+\varphi_2)$ by $\cosh(\varphi_1+\varphi_2)$ from Lemma 1, then divide numerator and denominator by $\cosh\varphi_1\cosh\varphi_2$.
>
> **Why needed:** It identifies the composed velocity with the familiar relativistic velocity-addition formula, closing the loop with [[Thm - Relativistic Velocity Addition]].
>
> > [!note]- Full proof
> > By Lemma 1,
> > $$\tanh(\varphi_1+\varphi_2) = \frac{\sinh(\varphi_1+\varphi_2)}{\cosh(\varphi_1+\varphi_2)} = \frac{\sinh\varphi_1\cosh\varphi_2 + \cosh\varphi_1\sinh\varphi_2}{\cosh\varphi_1\cosh\varphi_2 + \sinh\varphi_1\sinh\varphi_2}.$$
> > Divide numerator and denominator by $\cosh\varphi_1\cosh\varphi_2$:
> > $$\tanh(\varphi_1+\varphi_2) = \frac{\tanh\varphi_1 + \tanh\varphi_2}{1 + \tanh\varphi_1\tanh\varphi_2} = \frac{v_1 + v_2}{1 + v_1 v_2}.$$
> > Restoring $c$ replaces $v_i v_2$ by $v_1 v_2/c^2$ by dimensional analysis. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Work in the $(t, x)$-plane; the transverse directions are fixed by both boosts and contribute the identity. By [[Def - Boosts as Hyperbolic Rotations|the hyperbolic-rotation form of the boost]], $\Lambda[\varphi_i] = \begin{pmatrix} \cosh\varphi_i & \sinh\varphi_i \\ \sinh\varphi_i & \cosh\varphi_i \end{pmatrix}$.
>
> By Lemma 2, the product is
> $$\Lambda[\varphi_1]\Lambda[\varphi_2] = \begin{pmatrix} \cosh(\varphi_1+\varphi_2) & \sinh(\varphi_1+\varphi_2) \\ \sinh(\varphi_1+\varphi_2) & \cosh(\varphi_1+\varphi_2) \end{pmatrix} = \Lambda[\varphi_1 + \varphi_2],$$
> using the hyperbolic addition formulas (Lemma 1). This is the additivity statement.
>
> Since $\varphi \mapsto \Lambda[\varphi]$ is a bijection from $\mathbb{R}$ onto the collinear boosts, carries $+$ to matrix multiplication, sends $0$ to $I$, and sends $\varphi$ to the inverse of $\Lambda[-\varphi]$, the collinear boosts form a subgroup of $SO^+(1,3)$ isomorphic to $(\mathbb{R}, +)$.
>
> Finally, the composed velocity is $v = \tanh(\varphi_1 + \varphi_2)$, and by Lemma 3 this equals $(v_1 + v_2)/(1 + v_1 v_2)$, the [[Thm - Relativistic Velocity Addition|relativistic velocity-addition law]]. $\blacksquare$
>
> **On the non-collinear case.** If the boosts are along different axes, the generators $K_i$ and $K_j$ do not commute — indeed $[K_i, K_j] = -\epsilon_{ijk}J_k$ is a rotation generator — so $\exp(\varphi_1 K_i)\exp(\varphi_2 K_j) \neq \exp(\varphi_1 K_i + \varphi_2 K_j)$, and by the Baker–Campbell–Hausdorff formula the product picks up a rotation factor. The product of two non-collinear boosts is a boost composed with the **Thomas–Wigner rotation**; rapidity additivity is recovered only in the collinear limit where $K_i$ and $K_j$ coincide and commute.

---

# Cross-Field Exercise Suggestions

**The relativistic rocket and the unreachable speed of light.** A rocket that accelerates so as to add a fixed rapidity increment $\Delta\varphi$ per unit proper time has rapidity $\varphi(\tau) = (a/c)\tau$ growing linearly, so its velocity $v = c\tanh(a\tau/c)$ approaches but never reaches $c$. Rapidity additivity is what makes "constant proper acceleration" mean "constant rate of rapidity gain", which is the right relativistic notion of steady acceleration. The application is nonobvious because the natural Newtonian quantity (velocity) is the wrong one; rapidity is the quantity that grows steadily.

**Particle-physics rapidity and boost-invariant observables.** In a hadron collider the longitudinal rapidity of a produced particle shifts by a constant under a boost along the beam, so rapidity *differences* and the *shapes* of rapidity distributions are boost-invariant — which is why experimenters plot cross-sections against (pseudo)rapidity rather than velocity or angle. This is rapidity additivity applied to every particle simultaneously. The application is surprising in that an abstract group-theoretic fact dictates the choice of experimental coordinate.

**Thomas precession in atomic physics.** The electron in a hydrogen atom is continuously boosted as it orbits, and because successive boosts are non-collinear, the accumulated transformation includes a net rotation — the Thomas precession — which halves the naive spin–orbit coupling and corrects the fine-structure splitting. This is the *failure* of rapidity additivity (the remark above) turned into a measurable effect. The application is the deepest test of the theorem's collinearity hypothesis.

---

# Bridges

- **[[Thm - Relativistic Velocity Addition]]** — this theorem is the structural explanation of that one: the velocity-addition law $(v_1 + v_2)/(1 + v_1 v_2)$ is the $\tanh$ addition formula, and the denominator that looks mysterious in velocity variables is the cross term in $\cosh(\varphi_1 + \varphi_2)$. Where the velocity-addition page derives the law by dividing transformed coordinates, this page derives it as a one-line corollary of "rapidities add", and explains *why* $c$ is a fixed point ($\tanh$ maps $+\infty$ to $1$) and a ceiling (the asymptote is never reached).

- **[[Def - Rapidity]]** — additivity is the defining property of rapidity; this theorem is the proof that the parameter introduced there really does add. The one-parameter subgroup structure $\cong (\mathbb{R}, +)$ established here is what makes rapidity the *canonical coordinate* on the boost group, the exact analogue of the angle on the rotation group.

- **[[Def - Boosts as Hyperbolic Rotations]]** — the proof runs entirely on the hyperbolic-rotation form of the boost; in null (light-cone) coordinates each boost is $\mathrm{diag}(e^{\varphi}, e^{-\varphi})$ and additivity is the statement that diagonal matrices multiply by multiplying entries, i.e. exponents add. This is the same calculation as "rotations diagonalise to $e^{\pm i\theta}$ and angles add", with the imaginary angle replaced by a real rapidity.

- **Thomas–Wigner rotation** — the non-collinear failure of this theorem is a theorem in its own right, proved from the boost-boost commutator $[K_i, K_j] = -\epsilon_{ijk}J_k$ in [[Special Relativity IX — The Lorentz Group, Structure and Classification]]. The product of two non-parallel boosts is a third boost times a spatial rotation, and the rotation angle is the area of the corresponding triangle in the hyperbolic velocity space — the curvature of velocity space made into a physical precession.

---

# Unlocked by This

> [!tip] The Thomas–Wigner Rotation and Thomas Precession *(from the Structure of the Lorentz Group)*
> The remark that non-collinear boosts fail to add is the entry point to one of the subtlest effects in special relativity. Two boosts along different directions compose to a boost *times* a rotation; the rotation angle is the holonomy of the hyperbolic velocity space, and its time-derivative for an accelerating particle is the **Thomas precession** $\boldsymbol{\omega}_T = \frac{\gamma^2}{\gamma+1}\,\mathbf{a}\times\mathbf{v}$. This is the relativistic correction to spin precession; see [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

> [!tip] One-Parameter Subgroups and the Exponential Map *(from the Lorentz Group as a Lie Group)*
> "Collinear boosts form a one-parameter subgroup $\cong (\mathbb{R}, +)$" is the first instance of the general Lie-theoretic fact that every one-parameter subgroup of a Lie group is the image of a straight line in the Lie algebra under the **exponential map** $\varphi \mapsto \exp(\varphi K)$. Additivity is the homomorphism property $\exp(\varphi_1 K)\exp(\varphi_2 K) = \exp((\varphi_1 + \varphi_2)K)$, valid because the matrices commute. See [[Special Relativity X — The Lorentz Group as a Lie Group]].
