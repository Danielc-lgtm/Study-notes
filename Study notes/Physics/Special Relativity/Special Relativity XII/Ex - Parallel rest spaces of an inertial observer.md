---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Inertial Observer"
  - "Thm - Globality of the Local Rest Space for Inertial Observers"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\mathcal{O}$ be an [[Def - Inertial Observer|inertial observer]] with constant four-velocity $U$ ($U\cdot U = 1$), worldline $O(t) = O(0) + ct\,U$, and local rest spaces $\mathscr{E}_u(t)$. Working with $c = 1$:

1. Write the rest space $\mathscr{E}_u(t)$ as a level set of a single affine function $\phi(M) = U\cdot\overrightarrow{O(0)M}$, and show $\mathscr{E}_u(t) = \{M : \phi(M) = t\}$.
2. Prove that $\mathscr{E}_u(t_1)$ and $\mathscr{E}_u(t_2)$ are parallel hyperplanes, and disjoint for $t_1 \neq t_2$.
3. Take a concrete inertial observer in $1+1$ dimensions moving at velocity $v$, with $U = \gamma(1, v)$, and draw (describe) the rest-space lines on a spacetime diagram; give their equation $t - vx = \text{const}$ and slope.
4. Contrast with a *uniformly accelerated* observer, whose rest spaces all pass through a common point (the apex of the Rindler wedge) and therefore intersect; explain in one sentence why the inertial case avoids this.

**Recall:**

![[Thm - Globality of the Local Rest Space for Inertial Observers#Statement]]

The **local rest space** $\mathscr{E}_u(t)$ of an observer at proper time $t$ is the hyperplane through $O(t)$ orthogonal to the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U$: the set of events $M$ with $\overrightarrow{O(t)M}\cdot U = 0$; see [[Def - Observer and Local Rest Space]]. For an [[Def - Inertial Observer|inertial observer]] $U$ is constant. Two affine hyperplanes are **parallel** when they have the same normal direction.

---

# Convergent Strategy

**Problem class.** A *characterise-a-foliation* problem: show a family of hyperplanes is parallel and space-filling. The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] for observer problems says everything flows from the constancy of $U$; here it gives the common normal that forces parallelism.

**Assumption pattern.** The decisive assumption is that $U$ is constant. The rest space is by definition $U^\perp$ through $O(t)$, so a constant $U$ means a constant normal direction, hence parallel hyperplanes. The signpost is "inertial observer" $\Rightarrow$ "constant four-velocity" $\Rightarrow$ "common normal".

**Theorem routing.** This is a worked instance of [[Thm - Globality of the Local Rest Space for Inertial Observers]]. The route: write the rest spaces as level sets of the affine function $\phi(M) = U\cdot\overrightarrow{O(0)M}$ (using $O(t) = O(0) + ct\,U$ and $U\cdot U = 1$ to get $\phi(O(t)) = t$); level sets of a non-constant affine function are parallel disjoint hyperplanes foliating the space.

**Key decision point.** The clean move is to package the whole family of hyperplanes as the level sets of *one* function $\phi$, rather than treating each $\mathscr{E}_u(t)$ separately. Once they are level sets of a single non-constant affine function, parallelism, disjointness, and space-filling are automatic from linear algebra. The contrast with the accelerated observer — whose normal $U(t)$ *rotates*, so the hyperplanes pivot about a common edge and cross — pinpoints exactly which hypothesis (constancy of $U$) is doing the work.

---

# Legal Operations Used

1. **Use the constancy of $U$ to make the rest spaces parallel and the coordinates global** (operation 3 from the topic page). The constant four-velocity supplies the common normal direction, from which parallelism and the global foliation follow.

2. **Classify a separation by the orthogonality condition** (a specialisation of operation 9 from the topic page, applied to "simultaneous for $\mathcal{O}$"): an event lies in $\mathscr{E}_u(t)$ exactly when its displacement from $O(t)$ is orthogonal to $U$, i.e. $\phi(M) = t$.

---

# Hints

> [!note]- Hint 1
> The rest space at time $t$ is $\{M : \overrightarrow{O(t)M}\cdot U = 0\}$. Use $\overrightarrow{O(0)M} = \overrightarrow{O(0)O(t)} + \overrightarrow{O(t)M}$ and $\overrightarrow{O(0)O(t)} = t\,U$ (with $c=1$) to rewrite the condition as $U\cdot\overrightarrow{O(0)M} = t$, i.e. $\phi(M) = t$.

> [!note]- Hint 2
> All the hyperplanes $\{\phi = t\}$ have the same normal vector $U$ (the gradient of the affine function $\phi$), so they are parallel. A point $M$ has exactly one value $\phi(M)$, so it lies in exactly one hyperplane — hence distinct hyperplanes are disjoint.

> [!note]- Hint 3
> In $1+1$ with $U = \gamma(1, v)$ and metric $\mathrm{diag}(1, -1)$, the orthogonality $\overrightarrow{O(t)M}\cdot U = 0$ reads $\gamma(\Delta t - v\,\Delta x)\cdot(\text{sign})$... compute $U\cdot X = \gamma(X^0 - v X^1)\cdot$ — carefully, $U\cdot X = \eta_{\mu\nu}U^\mu X^\nu = \gamma(X^0 - v X^1)$. Setting this to $t$ gives the line $t' - v x' = \text{const}$, of slope $v$ in the $(x, t)$ diagram.

---

# Solution

The whole family of rest spaces is captured as the level sets of one affine function. Step 1 writes $\mathscr{E}_u(t) = \{\phi = t\}$ with $\phi(M) = U\cdot\overrightarrow{O(0)M}$. Step 2 reads off parallelism (common normal $U$) and disjointness (single-valuedness of $\phi$). Step 3 specialises to a moving observer in $1+1$, giving the tilted simultaneity lines $t - vx = \text{const}$. Step 4 contrasts the accelerated case, where the normal rotates and the hyperplanes cross.

**Step 1: The rest spaces are level sets of $\phi$.**

> [!note]- Derivation
> The rest space at proper time $t$ is $\mathscr{E}_u(t) = \{M : \overrightarrow{O(t)M}\cdot U = 0\}$. Decompose $\overrightarrow{O(0)M} = \overrightarrow{O(0)O(t)} + \overrightarrow{O(t)M}$. For the inertial worldline $O(t) = O(0) + ct\,U$ (with $c = 1$, $O(t) = O(0) + t\,U$), so $\overrightarrow{O(0)O(t)} = t\,U$. Then
> $$\overrightarrow{O(t)M}\cdot U = \big(\overrightarrow{O(0)M} - t\,U\big)\cdot U = U\cdot\overrightarrow{O(0)M} - t\,(U\cdot U) = \phi(M) - t,$$
> using $U\cdot U = 1$ and defining $\phi(M) = U\cdot\overrightarrow{O(0)M}$. Hence $\overrightarrow{O(t)M}\cdot U = 0 \iff \phi(M) = t$, so
> $$\mathscr{E}_u(t) = \{M : \phi(M) = t\}.$$
> The function $\phi$ is affine (linear in $\overrightarrow{O(0)M}$) and non-constant (since $U \neq 0$), and $\phi(O(t)) = U\cdot(t\,U) = t$, confirming the worldline event $O(t)$ lies in its own rest space at parameter $t$.

**Step 2: Parallel and disjoint.**

> [!note]- Derivation
> Each $\mathscr{E}_u(t) = \{\phi = t\}$ is a level set of the affine function $\phi$, whose linear part has gradient $U$ (the normal vector). All these hyperplanes share the *same* normal $U$, so they are mutually **parallel**. For disjointness: any event $M$ has a single value $\phi(M)$, so it lies in the unique hyperplane $\{\phi = \phi(M)\}$; if $t_1 \neq t_2$ then $\{\phi = t_1\}$ and $\{\phi = t_2\}$ share no point, i.e.
> $$\mathscr{E}_u(t_1)\cap\mathscr{E}_u(t_2) = \varnothing.$$
> The level sets of $\phi$ partition spacetime: every event has exactly one $\phi$-value, so the family $\{\mathscr{E}_u(t)\}_{t\in\mathbb{R}}$ foliates $\mathscr{E}$ by parallel disjoint hyperplanes — the global rest-space foliation.

**Step 3: A moving observer's tilted simultaneity lines.**

> [!note]- Derivation
> Work in $1+1$ dimensions with coordinates $(t, x)$, metric $\eta = \mathrm{diag}(1, -1)$, and an inertial observer of velocity $v$, so $U = \gamma(1, v)$ with $\gamma = (1-v^2)^{-1/2}$ (check $U\cdot U = \gamma^2(1 - v^2) = 1$). For a displacement $X = (X^0, X^1)$ from $O(0)$,
> $$U\cdot X = \eta_{\mu\nu}U^\mu X^\nu = \gamma\,X^0 - \gamma v\,X^1 = \gamma(X^0 - v X^1).$$
> The rest space $\mathscr{E}_u(t) = \{\phi = t\}$ is therefore $\{(X^0, X^1) : \gamma(X^0 - v X^1) = t\}$, i.e. the line
> $$X^0 - v X^1 = \frac{t}{\gamma} = \text{const}, \qquad\text{i.e.}\qquad t_{\text{coord}} = v\,x + \text{const}.$$
> On the spacetime diagram (time $X^0$ vertical, space $X^1$ horizontal) these are lines of **slope $v$** — tilted up from the horizontal by the velocity. As the observer ages (increasing $t$), the line sweeps upward, parallel to itself. The observer's worldline (the $t$-axis of its frame) has slope $1/v$, and the rest-space lines (its $x$-axis, lines of simultaneity) have slope $v$ — the two scissor symmetrically toward the light cone $X^0 = X^1$, the standard picture of the relativity of simultaneity. For the observer at rest ($v = 0$) the rest spaces are horizontal lines $X^0 = \text{const}$, the familiar absolute "nows".

**Step 4: Contrast with the accelerated observer.**

> [!note]- Derivation
> A *uniformly accelerated* observer in $1+1$ has the hyperbolic worldline $X^1 = \sqrt{a^{-2} + (X^0)^2}$, and its four-velocity $U(t) = (\cosh(a t), \sinh(a t))$ *rotates* (hyperbolically) as proper time $t$ advances. The rest space at time $t$ is still the line orthogonal to $U(t)$ through the worldline, but now the normal direction $U(t)$ changes with $t$, so the lines **pivot** rather than translate. Concretely, every one of these rest-space lines passes through the single point $X^0 = X^1 = 0$ (the apex of the Rindler wedge): they are the lines $X^0 = \tanh(at)\,X^1$ through the origin, fanning out as $t$ varies. Distinct rest spaces therefore *intersect* (all at the apex), the foliation breaks down, and the accelerated coordinate system covers only the wedge $X^1 > |X^0|$ — bounded by the Rindler horizon.
>
> The inertial case avoids this in one sentence: because the four-velocity is *constant*, the rest-space hyperplanes have a fixed normal and merely *translate* along it, so they stay parallel and never meet — whereas the accelerated observer's rotating four-velocity makes its rest spaces *pivot* about a common edge and cross.

> [!note]- Complete formal solution
> For an inertial observer with constant $U$ and worldline $O(t) = O(0) + tU$ (with $c = 1$), the rest space $\mathscr{E}_u(t) = \{M : \overrightarrow{O(t)M}\cdot U = 0\}$ equals $\{M : \phi(M) = t\}$ where $\phi(M) = U\cdot\overrightarrow{O(0)M}$, since $\overrightarrow{O(t)M}\cdot U = \phi(M) - t$ using $U\cdot U = 1$. These are level sets of a non-constant affine function with common normal $U$, hence parallel; each event has a unique $\phi$-value, so distinct level sets are disjoint and the family foliates spacetime. In $1+1$ with $U = \gamma(1, v)$, $U\cdot X = \gamma(X^0 - vX^1)$, so the rest spaces are the lines $X^0 - vX^1 = \text{const}$ of slope $v$, translating parallel to themselves as $t$ increases (for $v = 0$, horizontal). A uniformly accelerated observer instead has $U(t) = (\cosh at, \sinh at)$ rotating, so its rest spaces $X^0 = \tanh(at)X^1$ all pass through the apex $X^0 = X^1 = 0$ and intersect there — the foliation fails and the Rindler horizon appears. The inertial foliation survives because constant $U$ makes the hyperplanes translate, not pivot. $\blacksquare$

---

# Key Takeaways

**A family of parallel hyperplanes is the level sets of a single affine function — package them as one, not many.** The technical move that makes Step 2 trivial is recognising the whole one-parameter family $\{\mathscr{E}_u(t)\}$ as the level sets of the single function $\phi(M) = U\cdot\overrightarrow{O(0)M}$. Once they are level sets of a non-constant affine function, parallelism (common normal = the gradient $U$), disjointness (single-valuedness), and space-filling (every point has a value) are immediate linear algebra, with no per-hyperplane work. This packaging trick — replace a family of level surfaces by the function whose level surfaces they are — recurs throughout geometry and physics: a global time function, a foliation by a submersion, a potential whose equipotentials are the family. Whenever you face a family of parallel surfaces, look for the function they level-set.

**Constant normal means translate; rotating normal means pivot — and pivoting hyperplanes cross.** The entire difference between the inertial and accelerated cases is whether the four-velocity (the normal to the rest space) is constant or rotating. A constant normal makes the hyperplanes parallel translates that tile space and never meet; a rotating normal makes them pivot about a common edge and intersect, producing a caustic and a coordinate horizon. This is the geometric heart of why inertial frames are global and accelerated frames are not, and it is worth carrying as a visual: parallel pages of a book (inertial) versus a fan of lines through a point (accelerated, Rindler). The diagnostic transfers directly to general relativity, where a freely-falling congruence with zero shear/expansion/vorticity foliates cleanly while a generic one does not.

**The tilted simultaneity lines of slope $v$ are the relativity of simultaneity, seen geometrically.** Step 3's result — that a moving inertial observer's rest spaces are lines of slope $v$, not horizontal — *is* the relativity of simultaneity. Two inertial observers in relative motion have rest-space foliations with *different* normals ($U$ and $U'$), hence different tilts, so they slice spacetime into different families of "nows" and disagree about which events are simultaneous. The picture of the rest-space lines (the $x'$-axis) and the worldline (the $t'$-axis) scissoring symmetrically toward the light cone is the master diagram for every simultaneity puzzle. Recognise that "simultaneous for an inertial observer" means "lying in a common hyperplane orthogonal to $U$", a purely geometric condition $\phi = \text{const}$, and the frame-dependence of simultaneity becomes the frame-dependence of the normal direction $U$.
