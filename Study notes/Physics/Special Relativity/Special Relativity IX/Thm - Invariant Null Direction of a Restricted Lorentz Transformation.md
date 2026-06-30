---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Subgroups and Components of the Lorentz Group"
  - "Def - Classification of Four-Vectors"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, timelike $\Leftrightarrow X\cdot X > 0$, null $\Leftrightarrow X\cdot X = 0$. $SO^+(1,3)$ is the [[Def - Subgroups and Components of the Lorentz Group|restricted Lorentz group]]. A **null direction** is a one-dimensional subspace $\Delta = \mathrm{Span}(\ell)$ with $\ell\cdot\ell = 0$, $\ell \ne 0$; the lines through the origin lying on the light cone. The light cone (set of null vectors) is denoted $\mathscr{C}$. Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Statement

> **Theorem (Existence of an invariant null direction).** Every restricted Lorentz transformation $\Lambda \in SO^+(1,3)$ admits at least one invariant null direction: there exists a nonzero null vector $\ell$ and a real $\lambda > 0$ with
> $$\Lambda(\ell) = \lambda\,\ell.$$
> Equivalently, $\Lambda$ leaves invariant the null line $\Delta = \mathrm{Span}(\ell)$, so $\Lambda(\Delta) = \Delta$. The vector $\ell$ is a **null eigenvector** of $\Lambda$, and $\lambda = e^{\psi}$ for some real $\psi$.

---

# Motivation

The classification of restricted Lorentz transformations needs a starting point — a distinguished direction from which to build an adapted frame — and this theorem provides it. Without a guaranteed invariant direction one would have to treat each transformation case by case; with one, the entire taxonomy unfolds from a single algebraic seed.

The choice of a *null* direction rather than a timelike or spacelike one is deliberate and deep. The light cone is the one geometric structure that *every* Lorentz transformation preserves — that is the content of the constancy of the speed of light, lifted to the group level — so the natural invariant object to look for is a fixed generator of the cone. A timelike direction need not be fixed: a boost moves every timelike direction except none, in general. A spacelike direction need not be fixed either. But a null direction always is, and that is because the cone is the invariant skeleton of the geometry.

There is also a question of *why one expects a fixed point at all*. A restricted Lorentz transformation shuffles the null directions among themselves — it maps the cone to the cone — and the null directions form a two-sphere, the celestial sphere of an observer. A continuous self-map of a two-sphere that preserves orientation cannot move every point; some point must stay put, by the same topological pressure that forces a vector field on a sphere to vanish somewhere ("you cannot comb a hairy ball"). That fixed point is the invariant null direction. The theorem is, at heart, a fixed-point theorem on the sphere of light rays.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\Lambda$ is restricted." The disguised sources are the ways this hypothesis arrives.

The first disguised source is **"$\Lambda$ relates the frames of two observers."** Any change between the local frames of two physical observers — both right-handed, both future-pointing — is automatically a restricted transformation, so the theorem applies even when no matrix is written down. The bridge is that a frame change preserving orientation and time-direction is by definition proper and orthochronous. *Example problem:* show that the transformation relating two inertial observers always fixes some light ray's direction.

The second disguised source is **"$\Lambda = \exp(\omega)$ for $\omega \in \mathfrak{so}(1,3)$."** Anything in the image of the exponential map of the Lie algebra is restricted (it lies on a path from the identity), so it has an invariant null direction. The bridge is that the exponential lands in the identity component, which is $SO^+(1,3)$. *Example problem:* given a generator $\omega$, find the null direction fixed by $\exp(t\omega)$ for all $t$, which is a common eigenvector of $\omega$.

The third disguised source is **"$\Lambda$ lifts to $A \in SL(2,\mathbb{C})$."** Through the spinor map, a restricted transformation corresponds to a complex $2\times 2$ matrix of determinant one, and the theorem becomes the statement that the induced Möbius map on the Riemann sphere has a fixed point. The bridge is the [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|double cover]] and the correspondence between null directions and points of $\mathbb{C}P^1$. *Example problem:* show every $A \in SL(2,\mathbb{C})$ fixes a point of the Riemann sphere, equivalently has an eigenvector.

**Targets (Output Amplification)**

The conclusion is "$\Lambda$ fixes a null direction $\mathrm{Span}(\ell)$ with $\Lambda(\ell) = e^\psi\ell$."

Combine the conclusion with **the partner construction**. Given one null eigenvector $\ell$, pick a second future null vector $k$ with $\ell\cdot k = 2$ and form $e_0 = \tfrac12(\ell+k)$, $e_1 = \tfrac12(\ell-k)$, completing an adapted orthonormal frame. The further result is the three-parameter normal form of $\Lambda$ ([[Def - Classification of Restricted Lorentz Transformations]]), from which the entire classification reads off. The combination is the workhorse of §9.2: it converts "there exists a fixed null direction" into "here is the matrix in an adapted frame."

Combine the conclusion with **counting the fixed null directions**. The number of invariant null directions — one, two, or infinitely many — determines the type: exactly one means a null rotation, exactly two means a four-screw, and the degenerate cases fill in the boosts, rotations, and the identity ([[Def - Null Rotations and Four-Screws]]). The further result is the dichotomy theorem. The combination is nonobvious because a single existence statement, iterated and counted, becomes a complete classification.

Combine the conclusion with **the eigenvalue $\lambda = e^\psi > 0$**. Since $\Lambda$ is orthochronous, the eigenvalue on a future null eigenvector is positive, so it equals $e^\psi$ for a real $\psi$ — the rapidity. The further result is that the rapidity of the transformation is encoded in the null eigenvalue, recoverable without diagonalising the whole matrix. The combination links the abstract fixed direction to the measurable boost parameter.

---

# Why Is It True

There are two proofs, a topological one and an algebraic one, and they are the same fact seen from two sides.

**The topological proof: you cannot comb the sphere of light rays.** Consider the null directions of Minkowski space. Intersect the past light cone of an event with a spacelike hyperplane: the result is a two-sphere, the *celestial sphere* of an observer whose rest space is that hyperplane, and each point of the sphere corresponds to one null direction (one incoming light ray). A restricted Lorentz transformation $\Lambda$ preserves the light cone (it preserves the metric, hence the null condition $X\cdot X = 0$), so it maps null directions to null directions, inducing a map $f : S^2 \to S^2$. This $f$ is continuous (any linear map is continuous) and orientation-preserving (because $\Lambda$ is proper and orthochronous). Now the key topological fact: an orientation-preserving continuous self-map of $S^2$ has a fixed point. The cleanest statement is via the Lefschetz fixed-point theorem — a continuous self-map of $S^2$ of degree $d \ne -1$ has a fixed point, and an orientation-preserving map has degree $+1$ — or more elementarily, the Brouwer-type fact that a map homotopic to the identity on $S^2$ cannot be fixed-point-free, since a fixed-point-free self-map of $S^2$ must be homotopic to the antipodal map (degree $-1$). A fixed point of $f$ is an invariant null direction of $\Lambda$. **The mechanism is that the sphere of light rays has no nonvanishing tangent vector field, so the displacement of light rays under $\Lambda$ must vanish somewhere.**

**The algebraic proof: a complex matrix always has an eigenvector.** Through the [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|spinor map]], $\Lambda$ lifts to $A \in SL(2,\mathbb{C})$, and null directions correspond to points of the Riemann sphere $\mathbb{C}P^1 = \mathbb{C}\cup\{\infty\}$, with $\Lambda$ acting as the Möbius transformation $z \mapsto (az+b)/(cz+d)$ for $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. A fixed point of this Möbius map is a solution of $cz^2 + (d-a)z - b = 0$, a quadratic with complex coefficients, which always has a root by the fundamental theorem of algebra. Equivalently, $A$ being a $2\times 2$ complex matrix always has an eigenvector (its characteristic polynomial has a complex root), and the eigenvector corresponds to a fixed null direction. **The mechanism is that the fundamental theorem of algebra guarantees a root, hence a fixed point of the Möbius map, hence an invariant null direction.**

The two proofs agree because the celestial sphere and the Riemann sphere are the same sphere, identified by stereographic projection, and the orientation-preserving self-map of the topological proof is exactly the Möbius transformation of the algebraic one. The topological proof reveals *why* there is always a fixed point (a deep fact about $S^2$); the algebraic proof reveals *how to find it* (solve a quadratic).

---

# What Makes This Hard

The conceptual hurdle is recognising that the right object to fix is a *null* direction, not a timelike or spacelike one — the instinct to look for a fixed timelike axis fails, since a boost fixes no timelike direction. The technical subtlety in the topological proof is the orientation-preserving hypothesis: a fixed-point-free self-map of $S^2$ exists (the antipodal map), so one genuinely needs degree $+1$, and forgetting this is the common error. In the algebraic proof, the subtlety is that the fixed point may be a *single* point (when $A$ is parabolic, a repeated eigenvalue with one eigenvector) rather than two, which is exactly the null-rotation case.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Realise the null directions as a two-sphere (the celestial sphere), observe that a restricted $\Lambda$ induces an orientation-preserving continuous self-map of it, and invoke the fixed-point theorem for $S^2$. The fixed point is the invariant null direction. (Alternatively: lift to $SL(2,\mathbb{C})$ and use that a $2\times 2$ complex matrix has an eigenvector.)

**Subgoal decomposition:**

1. **Realise null directions as $S^2$.** Show the null directions are in bijection with the celestial sphere $\mathscr{S} = \mathscr{C}^-(O)\cap\Sigma$, the intersection of a past light cone with a spacelike hyperplane.
   - *Hint:* Each null direction meets a given spacelike hyperplane in one point; the locus is a round sphere.
   - *Why needed:* It turns "invariant null direction" into "fixed point of a sphere map."

2. **Induce a self-map of $S^2$.** Show $\Lambda$ maps null directions to null directions, inducing a continuous $f : S^2 \to S^2$.
   - *Hint:* $\Lambda$ preserves the metric, hence the null cone; linear maps are continuous.
   - *Why needed:* It is the map to which the fixed-point theorem applies.

3. **Check orientation preservation.** Show $f$ is orientation-preserving, hence of degree $+1$.
   - *Hint:* $\Lambda$ is proper ($\det = +1$) and orthochronous, so it preserves the orientation of the celestial sphere.
   - *Why needed:* The fixed-point theorem needs degree $\ne -1$; orientation-preserving gives degree $+1$.

4. **Apply the fixed-point theorem.** Conclude $f$ has a fixed point, which is an invariant null direction; orthochronicity makes the eigenvalue positive.
   - *Hint:* Lefschetz (or the Euler characteristic $\chi(S^2) = 2 \ne 0$): a degree-$1$ self-map of $S^2$ has a fixed point.
   - *Why needed:* It delivers the existence; positivity of $\lambda$ gives $\lambda = e^\psi$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The null directions form a two-sphere
> **Statement:** Fix an event $O$ and a spacelike hyperplane $\Sigma$ through $O$. The set $\mathscr{S} = \mathscr{C}^-(O)\cap\Sigma$ (past light cone meets hyperplane) is a topological two-sphere, and each of its points determines a unique null direction.
>
> **Hint:** In the rest frame of $\Sigma$, the past light cone is $\{(-r, \mathbf{x}) : |\mathbf{x}| = r\}$ and $\Sigma$ is $\{t = -1\}$ say.
>
> **Why needed:** It realises the abstract null directions as a concrete sphere on which fixed-point theory applies.
>
> > [!note]- Full proof
> > Choose an observer with 4-velocity $e_0$ orthogonal to $\Sigma$, and work in its frame, coordinates $(t,\mathbf{x})$. A future null direction is spanned by $\ell = (1, \mathbf{n})$ with $|\mathbf{n}| = 1$ (so $\ell\cdot\ell = 1 - |\mathbf{n}|^2 = 0$), and the unit vector $\mathbf{n} \in S^2$ labels it bijectively — the direction of the incoming light ray on the observer's sky. The past light cone of $O$ meets the spacelike hyperplane $\Sigma = \{t = -1\}$ in the sphere $\{(-1,\mathbf{n}) : |\mathbf{n}| = 1\} \cong S^2$, and the line from $O$ through each such point is the null direction $\mathrm{Span}(1, \mathbf{n})$. Hence null directions $\leftrightarrow$ points of $S^2$. $\blacksquare$

> [!note]- Lemma 2: A restricted transformation induces an orientation-preserving self-map of the sphere
> **Statement:** $\Lambda \in SO^+(1,3)$ maps null directions to null directions, inducing a continuous orientation-preserving map $f : S^2 \to S^2$.
>
> **Hint:** $\Lambda$ preserves the light cone; properness and orthochronicity give orientation preservation.
>
> **Why needed:** It is the map to which the $S^2$ fixed-point theorem is applied.
>
> > [!note]- Full proof
> > $\Lambda$ preserves the scalar product, hence the null condition $\ell\cdot\ell = 0$, so it maps the light cone $\mathscr{C}$ to itself and thus permutes null directions: $f(\mathrm{Span}(\ell)) = \mathrm{Span}(\Lambda\ell)$. This $f : S^2 \to S^2$ is continuous because $\Lambda$ is linear (continuous) and the passage to directions is continuous. Orientation: $\Lambda$ is orthochronous, so it preserves the future light cone (maps the future sphere to itself rather than to the past sphere), and proper, so it preserves the orientation of that sphere; hence $f$ is orientation-preserving, of degree $+1$. $\blacksquare$

> [!note]- Lemma 3: An orientation-preserving self-map of $S^2$ has a fixed point
> **Statement:** A continuous map $f : S^2 \to S^2$ of degree $+1$ has a fixed point.
>
> **Hint:** Lefschetz fixed-point theorem, or: a fixed-point-free map of $S^2$ is homotopic to the antipodal map (degree $-1$).
>
> **Why needed:** It produces the invariant null direction.
>
> > [!note]- Full proof
> > Suppose $f$ has no fixed point, so $f(x) \ne x$ for all $x$. Then for each $x$ the points $x$ and $f(x)$ are distinct, and the geodesic from $f(x)$ *through* $x$ to the antipode defines a homotopy from $f$ to the antipodal map $a(x) = -x$ (slide $f(x)$ along the great circle to $-x$, never crossing $x$). Hence $f \simeq a$, so $\deg f = \deg a = (-1)^{2+1} = -1$ (the antipodal map of $S^n$ has degree $(-1)^{n+1}$, here $n = 2$). This contradicts $\deg f = +1$. Therefore $f$ has a fixed point. (Equivalently, the Lefschetz number of $f$ is $1 + \deg f = 2 \ne 0$, forcing a fixed point.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Lambda \in SO^+(1,3)$.
>
> By Lemma 1, the null directions of Minkowski space are in bijection with a two-sphere $\mathscr{S} \cong S^2$ (the celestial sphere), each point a null direction $\mathrm{Span}(1,\mathbf{n})$, $|\mathbf{n}| = 1$.
>
> By Lemma 2, $\Lambda$ preserves the light cone and so induces a continuous, orientation-preserving self-map $f : S^2 \to S^2$ of degree $+1$, with $f(\mathrm{Span}(\ell)) = \mathrm{Span}(\Lambda\ell)$.
>
> By Lemma 3, $f$ has a fixed point $\mathrm{Span}(\ell)$, i.e. $\Lambda(\ell) \in \mathrm{Span}(\ell)$, so $\Lambda(\ell) = \lambda\ell$ for some real $\lambda \ne 0$ (nonzero since $\Lambda$ is invertible).
>
> Finally, $\Lambda$ is orthochronous, so it maps the future null vector $\ell$ to a future null vector $\Lambda\ell = \lambda\ell$, forcing $\lambda > 0$. Writing $\lambda = e^{\psi}$ with $\psi = \ln\lambda \in \mathbb{R}$ completes the proof: $\Lambda(\ell) = e^{\psi}\ell$, an invariant null direction. $\blacksquare$
>
> *(Algebraic alternative.)* Lift $\Lambda$ to $A \in SL(2,\mathbb{C})$ via the spinor map. The characteristic polynomial $\det(A - \mu I) = \mu^2 - (\mathrm{tr}\,A)\mu + 1$ has a complex root, so $A$ has an eigenvector $v$, $Av = \mu v$. Under the spinor correspondence the line $\mathbb{C}v \subset \mathbb{C}^2$ maps to a null direction fixed by $\Lambda$, giving the invariant null direction directly.

---

# Cross-Field Exercise Suggestions

**Möbius transformations of the Riemann sphere.** Every Möbius transformation $z \mapsto (az+b)/(cz+d)$ has one or two fixed points (a parabolic map has one, a non-parabolic map two), found by solving the quadratic $cz^2 + (d-a)z - b = 0$. The application is to recognise the invariant-null-direction theorem as this elementary fact in disguise, with the celestial sphere identified with $\mathbb{C}P^1$. It is out-of-distribution because the relativistic content (light rays) and the complex-analytic content (Möbius maps) look unrelated until the spinor map links them.

**Perron–Frobenius theory.** A positive matrix has a positive eigenvector (Perron–Frobenius), found by a fixed-point argument on the simplex. The structural parallel is that a transformation preserving a cone (the light cone here, the positive orthant there) has an eigenvector inside or on the cone. The application battle-tests the "preserves a cone $\Rightarrow$ has an eigen-ray on the cone" pattern, which underlies both the relativistic theorem and the theory of stochastic matrices and population dynamics.

**The hairy ball theorem and flows on spheres.** The topological core — an orientation-preserving self-map of $S^2$ has a fixed point — is a cousin of the hairy ball theorem (no nonvanishing tangent vector field on $S^2$) and governs the existence of equilibria for flows on the sphere. The application is to dynamical systems on $S^2$: any flow's time-one map is orientation-preserving and homotopic to the identity, hence has a fixed point, which is an equilibrium. It is surprising that the existence of an invariant light ray and the existence of an equilibrium of a spherical flow are the same theorem.

---

# Bridges

- **[[Def - Classification of Restricted Lorentz Transformations]]** — this theorem is the seed of the classification: the invariant null direction it guarantees is the first vector $\ell$ of the adapted frame, from which the three-parameter normal form and the entire taxonomy are built. The classification could not begin without the existence statement proved here.

- **[[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group|The double cover SL(2,ℂ)]]** — the algebraic proof *is* the statement that the Möbius transformation induced by the spinor lift $A \in SL(2,\mathbb{C})$ has a fixed point on the Riemann sphere. The four-screw/null-rotation dichotomy of the classification corresponds exactly to the loxodromic/parabolic dichotomy of Möbius transformations: two fixed points versus one. This theorem is the bridge from the geometry of the light cone to the complex analysis of the sphere.

- **The Lefschetz fixed-point theorem** — the topological proof is an instance of the general principle that a self-map $f$ of a compact space with nonzero Lefschetz number $L(f) = \sum (-1)^i \mathrm{tr}(f_* : H_i \to H_i)$ has a fixed point. For an orientation-preserving self-map of $S^2$, $L(f) = 1 + \deg f = 2 \ne 0$, forcing a fixed point. The same machinery underlies the existence of fixed points for maps of higher-dimensional spheres and projective spaces, and it is the topological reason the Lorentz group's action on the celestial sphere can never be fixed-point-free.

---

# Unlocked by This

> [!tip] Little Groups and the Wigner Classification *(from Special Relativity XII)*
> The invariant directions fixed by subgroups of the Lorentz group are the foundation of Wigner's classification of relativistic particles. A massive particle has a timelike 4-momentum, and the subgroup fixing it — its **little group** — is $SO(3)$, the rotations of the rest frame, whose representations are labelled by spin. A massless particle has a *null* 4-momentum, and the subgroup fixing that null direction is the group generated by null rotations and rotations about the direction, isomorphic to $ISO(2)$, the Euclidean group of the plane, whose representations are labelled by helicity. The invariant null direction of this theorem is precisely the fixed null momentum of a massless particle, and the null rotations that fix it (the genuinely non-Euclidean elements of the classification) are the generators of the massless little group. The existence of a fixed null direction for every restricted transformation is thus the geometric fact behind the very notion of a massless particle's helicity.
