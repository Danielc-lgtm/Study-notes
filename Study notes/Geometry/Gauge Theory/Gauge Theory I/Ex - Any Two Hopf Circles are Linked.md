---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Complex Projective Space as a Quotient"
  - "Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map"
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
difficulty: "⭐⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Throughout, $S^3 = \{w = (w_1, w_2) \in \mathbb{C}^2 : |w_1|^2 + |w_2|^2 = 1\}$ is the unit sphere of $\mathbb{C}^2$, and the circle group $U(1) = \{z \in \mathbb{C} : |z| = 1\}$ acts on $S^3$ by complex scalar multiplication, $z \cdot (w_1, w_2) = (z w_1, z w_2)$. We identify $\mathbb{C}^2$ with $\mathbb{R}^4$ through $(w_1, w_2) = (x_1 + i x_2,\ x_3 + i x_4)$, so that $S^3 = \{x \in \mathbb{R}^4 : x_1^2 + x_2^2 + x_3^2 + x_4^2 = 1\}$. A **Hopf circle** is an orbit $U(1) \cdot w = \{z w : |z| = 1\}$ of this action; by [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map]] the Hopf circles are exactly the fibres of the Hopf map $\mathrm{Hopf} : S^3 \to S^2$, and we use the two names interchangeably. Let $N := (1, 0) \in S^3$, that is $N = (1, 0, 0, 0) \in \mathbb{R}^4$, and let
$$\sigma : S^3 \setminus \{N\} \to \mathbb{R}^3, \qquad \sigma(x_1, x_2, x_3, x_4) = \frac{1}{1 - x_1}\,(x_3, x_4, x_2)$$
be stereographic projection from $N$, with the coordinates of $\mathbb{R}^3$ written $y = (y_1, y_2, y_3)$ and the plane $\{y_3 = 0\}$ called the $xy$-plane. Write
$$C_0 := U(1) \cdot (0, 1) = \{(0, e^{i\theta}) : \theta \in \mathbb{R}\}, \qquad D_0 := \{(y_1, y_2, 0) \in \mathbb{R}^3 : y_1^2 + y_2^2 < 1\}$$
for the Hopf circle through $(0, 1)$ and for the open flat disc in the $xy$-plane bounded by the unit circle.

**Definition used on this page (linking with $C_0$).** A subset $C \subset \mathbb{R}^3$ that is a round circle or a straight line, disjoint from the unit circle $\sigma(C_0)$, is said to be **linked with $\sigma(C_0)$** if $C$ meets the open disc $D_0$ in exactly one point, and at that point $C$ crosses the plane $\{y_3 = 0\}$ transversally, meaning that the tangent line of $C$ there is not contained in $\{y_3 = 0\}$. This is the intersection-number criterion of knot theory (one transverse crossing of a spanning disc means linking number $\pm 1$); since the series does not yet have homology at its disposal (chapter XII), the criterion is adopted here as the definition.

Prove the following.

**(a) The picture of the fibration in $\mathbb{R}^3$.** The map $\sigma$ is a bijection onto $\mathbb{R}^3$ with inverse $\tau(y) = \frac{1}{1 + |y|^2}\,(|y|^2 - 1,\ 2 y_3,\ 2 y_1,\ 2 y_2)$. The Hopf circle $U(1) \cdot N = \{(e^{i\theta}, 0)\}$ is the fibre of the Hopf map over the south pole $(0, 0, -1) \in S^2$, it is the only Hopf circle through $N$, and $\sigma$ maps it (minus $N$) onto the $z$-axis $\{(0, 0, y_3) : y_3 \in \mathbb{R}\}$. Every other Hopf circle is mapped by $\sigma$ onto a round circle in $\mathbb{R}^3$. Consequently $\mathbb{R}^3$ is the disjoint union of round circles and one straight line.

**(b) Every Hopf circle is linked with $\sigma(C_0)$.** The circle $C_0$ is the fibre of the Hopf map over the north pole $(0, 0, 1) \in S^2$, and $\sigma(C_0)$ is the unit circle $\{(\cos\theta, \sin\theta, 0)\}$ in the $xy$-plane. For every Hopf circle $C \neq C_0$, the set $\sigma(C \setminus \{N\})$ — a round circle, or the $z$-axis when $C = U(1) \cdot N$ — meets $D_0$ in exactly one point, transversally. Hence every Hopf circle other than $C_0$ is linked with $\sigma(C_0)$ in the sense defined above.

**(c) Any two Hopf circles.** For any two distinct Hopf circles $C_1, C_2 \subset S^3$ there is a unitary matrix $A \in U(2)$, hence an isometry of $\mathbb{R}^4$ that permutes the Hopf circles, with $A C_1 = C_0$; so after the stereographic projection $\sigma \circ A$ (which is stereographic projection of $S^3$ from the point $A^{-1} N$, a point of the Hopf circle $A^{-1}(U(1) \cdot N)$, followed by the orthogonal change of coordinates $A$), $C_1$ becomes the unit circle of the $xy$-plane and $C_2$ becomes a round circle or the $z$-axis, linked with it by (b). In this sense any two Hopf circles are linked: they form a Hopf link.

The route intended by the source is the explicit parametrisation of a general fibre, $\theta \mapsto (e^{i\theta} \cos\alpha,\ e^{i\theta} \sin\alpha)$ with $\alpha \in (0, \pi/2)$, projected by $\sigma$; on this page we keep one more phase $\phi$ in the second coordinate so that the parametrisation reaches every fibre without a separate symmetry argument.

**Recall:**

The orbit space $S^3 / U(1)$ of the scalar action is the complex projective line, and the fibres of the Hopf map are the orbits.

![[Def - Complex Projective Space as a Quotient#The Definition]]

![[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map#Statement]]

The vocabulary of orbits and of free actions (the scalar action of $U(1)$ on $S^3$ is free, so every Hopf circle is an embedded copy of the circle $U(1)$; this is verified on [[Ex - The Scalar Action of U(1) on Odd Spheres is Free]]):

![[Def - Free, Transitive, Effective, and Proper Group Actions#The Definition]]

Stereographic projection of $S^n$ from a pole, with its explicit inverse, is constructed on [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]]; the map $\sigma$ above is that projection from the point $N = (1, 0, 0, 0)$ after the permutation of coordinates $(x_1, x_2, x_3, x_4) \mapsto (x_3, x_4, x_2, x_1)$, chosen so that the exceptional fibre lands on the $z$-axis rather than on the $x$-axis. The Hopf map in Bär's normalisation, which this series uses (see the Notation section of [[Def - Complex Projective Space as a Quotient]]), is
$$\mathrm{Hopf}(w_1, w_2) = \frac{1}{4|w_2|^2 + |w_1|^2}\,\big(4 w_1 \bar w_2,\ 4|w_2|^2 - |w_1|^2\big) \in \mathbb{C} \times \mathbb{R} = \mathbb{R}^3,$$
and its fibres are the $U(1)$-orbits. Only the fibres over the two poles are needed here, and we compute them directly from the formula in Step 2 below, so the page does not depend on which normalisation of the Hopf map is used.

> [!warning] Convention: which pole is which
> Under Bär's Hopf map the fibre over the north pole $(0, 0, 1)$ is $\{w_1 = 0\}$ and the fibre over the south pole $(0, 0, -1)$ is $\{w_2 = 0\}$ (Step 2). The page [[Def - The Hopf Map]] in Algebraic Topology III uses the real formula $\eta(a, b, c, d) = (2(ac + bd),\ 2(bc - ad),\ a^2 + b^2 - c^2 - d^2)$, whose third component is $|w_1|^2 - |w_2|^2$; there the poles are exchanged (north pole fibre $\{w_2 = 0\}$). The one-line conversion is the swap $(w_1, w_2) \mapsto (w_2, w_1)$ of the two complex coordinates, which interchanges the two fibres and reflects the $S^2$ picture in its equatorial plane. Nothing in this exercise depends on the choice: the statement "the fibre through $N$ becomes a line and every other fibre a circle" is about the orbits, not about their labels.

---

# Convergent Strategy

**Problem class:** This is a *make-the-quotient-visible* problem: an orbit decomposition of $S^3$ is transported to $\mathbb{R}^3$ by a chart, and a topological property of the decomposition (pairwise linking of the orbits) is then read off by an explicit intersection count. It sits in the family of exercises in which a free action is understood not through the orbit space alone but through the way the orbits sit inside the total space — the first appearance in the series of the fact, used constantly from chapter III onward, that the Hopf fibration $S^1 \hookrightarrow S^3 \to S^2$ is a non-trivial bundle: a trivial bundle $S^2 \times S^1$ would have unlinked fibres.

**Assumption pattern:** The data are an orbit of a linear action of a compact group on a sphere and a stereographic chart. Two features of the action drive everything. First, the action is *complex-linear*: the orbit of $w$ is the unit circle of the complex line $\mathbb{C} w$, hence the intersection of $S^3$ with a real 2-plane through the origin — a great circle. Second, the action *commutes with $U(2)$*, which acts transitively on $S^3$; so no orbit is distinguished, and any pair of orbits can be moved by a unitary matrix to a pair in which one orbit is $C_0$. The recognisable trigger is "orbits of a linear action on a sphere, projected stereographically": great circles go to round circles (or a line), so the picture is made of round circles and can be analysed with plane geometry.

**Theorem routing:** The route is: (1) write $\sigma$ and its inverse $\tau$ and verify both compositions, so that $\sigma$ is a bijection and the image of a set can be computed by asking which $y$ have $\tau(y)$ in the set; (2) show every orbit is $S^3 \cap \Pi_w$ for the real 2-plane $\Pi_w = \operatorname{span}_{\mathbb{R}}(w, iw)$, and that $N \in \Pi_w$ if and only if $\Pi_w = \Pi_N$; (3) prove a lemma — the image under $\sigma$ of $S^3 \cap \Pi$ for a 2-plane $\Pi \not\ni N$ is the intersection of a sphere with a plane in $\mathbb{R}^3$, hence a round circle — by substituting $\tau(y)$ into the two linear equations that cut out $\Pi$; (4) parametrise a general fibre as $\gamma(\theta) = (e^{i\theta}\cos\alpha,\ e^{i(\theta + \phi)}\sin\alpha)$, compute $p(\theta) = \sigma(\gamma(\theta))$, solve $p_3(\theta) = 0$, and find that of the two solutions exactly one lies inside the unit circle, with $p_3'(\theta) \neq 0$ there; (5) reduce an arbitrary pair of orbits to the pair $(C_0, C)$ by a unitary matrix. The pages invoked are [[Def - Complex Projective Space as a Quotient]] (the action, the Hopf map, the orbit space), [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map]] (fibres of the Hopf map are the orbits), and [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]] (the shape of $\sigma$ and $\tau$); everything else is computed on the page.

**Key decision point:** Two choices decide whether the computation is short or hopeless. The first is *which point to project from*: projecting from a point of the fibre over the south pole makes that fibre the $z$-axis and makes $C_0$ the unit circle of the $xy$-plane, so that the spanning disc $D_0$ is flat and the intersection count is the solution set of the single equation $p_3(\theta) = 0$. Projecting from a point not on a fibre through a pole gives the same topology but a tilted picture in which every disc must be tilted too. The second is *how to prove that the images are round circles*: rather than verifying "constant distance from a centre" on the explicit parametrisation (a trigonometric identity of no independent interest), one substitutes $\tau(y)$ into the *linear* equations of the plane $\Pi_w$; linear equations in $x$ become one sphere equation and one plane equation in $y$, and a plane section of a sphere is a round circle by Pythagoras. The genuine insight of part (b) is that the two points where a fibre meets the $xy$-plane are at distances $\cot(\alpha/2)$ and $\tan(\alpha/2)$ from the origin — one outside and one inside the unit circle for every $\alpha \in (0, \pi/2)$ — so every fibre threads the disc exactly once.

---

# Legal Operations Used

The topic page of this chapter is written after its subpages; the operations below are named descriptively, and the orchestrator reconciles the numbering with the topic page's Legal Operations list.

1. **Verify a bijection by exhibiting its inverse and checking both compositions.** Applied to $\sigma$ and $\tau$ in Step 1: rather than arguing geometrically that the line through $N$ and $x$ meets the hyperplane $\{x_1 = 0\}$ once, we write $\tau$ down and compute $\sigma \circ \tau = \mathrm{id}$ and $\tau \circ \sigma = \mathrm{id}$, which also gives the formula used in Step 4.

2. **Describe an orbit of a linear action as the intersection of the sphere with a linear subspace.** Applied in Step 2: $U(1) \cdot w = \{(\cos\theta) w + (\sin\theta)(iw)\} = S^3 \cap \operatorname{span}_{\mathbb{R}}(w, iw)$, because $w$ and $iw$ are orthonormal in $\mathbb{R}^4$. This turns a question about orbits into a question about 2-planes.

3. **Compute the image of a set under a bijection by pulling back its defining equations along the inverse.** Applied in Step 4: $y \in \sigma(S^3 \cap \Pi)$ if and only if $\tau(y) \in \Pi$, and $\Pi$ is cut out by two linear equations, which after substitution of $\tau(y)$ become a sphere equation and a plane equation.

4. **Reduce to a normal form using a symmetry that commutes with the action.** Applied twice: in Step 5, a phase $e^{-i\phi_1}$ in $U(1)$ itself puts a base point of the fibre in the form $(\cos\alpha, e^{i\phi}\sin\alpha)$; in Step 7, a unitary matrix $A \in U(2)$, which commutes with scalar multiplication and preserves $S^3$, moves an arbitrary Hopf circle onto $C_0$.

5. **Count intersection points by solving one scalar equation along a parametrisation, and decide transversality by differentiating it.** Applied in Step 6: the intersection of $\sigma(C)$ with the plane $\{y_3 = 0\}$ is the zero set of $p_3(\theta)$ on one period, and the crossing is transverse exactly when $p_3'(\theta) \neq 0$ at the zero.

6. **Use half-angle identities to compare a computed radius with $1$.** Applied in Step 6: $\frac{\sin\alpha}{1 - \cos\alpha} = \cot(\alpha/2)$ and $\frac{\sin\alpha}{1 + \cos\alpha} = \tan(\alpha/2)$, and for $\alpha \in (0, \pi/2)$ these are respectively greater than and less than $1$.

---

# Hints

> [!note]- Hint 1
> Before computing anything, decide what a Hopf circle *is* as a subset of $\mathbb{R}^4$. The orbit of $w$ is $\{e^{i\theta} w\} = \{(\cos\theta) w + (\sin\theta)(iw)\}$. Check that $w$ and $iw$ are orthonormal vectors of $\mathbb{R}^4$. So every Hopf circle is a great circle: the intersection of $S^3$ with a real 2-plane through the origin. Which of these 2-planes contains $N = (1, 0)$?

> [!note]- Hint 2
> Stereographic projection sends a great circle not through the projection point to a round circle. To prove this without trigonometry, write the inverse $\tau(y)$ of $\sigma$ and substitute it into the two linear equations $\langle a, x \rangle = 0$, $\langle b, x \rangle = 0$ that define the 2-plane. Each becomes $a_1(|y|^2 - 1) + 2\langle \tilde a, y \rangle = 0$ for a suitable $\tilde a \in \mathbb{R}^3$ — a sphere if $a_1 \neq 0$, a plane if $a_1 = 0$. Arrange the basis $a, b$ of the normal space so that $a_1 = 1$ and $b_1 = 0$.

> [!note]- Hint 3
> Every point of $S^3$ can be written $(e^{i\phi_1}\cos\alpha,\ e^{i\phi_2}\sin\alpha)$ with $\alpha \in [0, \pi/2]$. Multiply by $e^{-i\phi_1}$ — a point of $U(1)$, so this stays inside the orbit — to see that every orbit contains a point $(\cos\alpha,\ e^{i\phi}\sin\alpha)$ and is parametrised by $\gamma(\theta) = (e^{i\theta}\cos\alpha,\ e^{i(\theta + \phi)}\sin\alpha)$. Write $\gamma$ in real coordinates and apply $\sigma$; the third component of $\sigma(\gamma(\theta))$ is $\frac{\cos\alpha \sin\theta}{1 - \cos\alpha\cos\theta}$.

> [!note]- Hint 4
> The third component vanishes exactly at $\theta = 0$ and $\theta = \pi$. Compute the distance from the origin of $p(0)$ and $p(\pi)$: they are $\frac{\sin\alpha}{1 - \cos\alpha}$ and $\frac{\sin\alpha}{1 + \cos\alpha}$. Use $\sin\alpha = 2\sin(\alpha/2)\cos(\alpha/2)$, $1 - \cos\alpha = 2\sin^2(\alpha/2)$, $1 + \cos\alpha = 2\cos^2(\alpha/2)$ to rewrite these as $\cot(\alpha/2)$ and $\tan(\alpha/2)$. For $\alpha \in (0, \pi/2)$ the first exceeds $1$ and the second lies strictly between $0$ and $1$. For transversality differentiate the third component at $\theta = \pi$.

> [!note]- Hint 5
> For part (c), given $w \in S^3$, the vector $v = (-\bar w_2, \bar w_1)$ completes $w$ to an orthonormal basis of $\mathbb{C}^2$. The unitary matrix $B$ with columns $v, w$ sends $e_2 = (0, 1)$ to $w$; its inverse $A = B^*$ sends $w$ to $(0, 1)$, and $A(zw') = zAw'$ for every $z \in U(1)$, so $A$ maps Hopf circles to Hopf circles and $A(U(1) \cdot w) = C_0$.

---

# Solution

The solution transports the orbit decomposition of $S^3$ to $\mathbb{R}^3$ by an explicit stereographic projection and then reads off linking by counting intersection points with a flat disc. Steps 1 to 4 establish the picture of part (a): $\sigma$ is a bijection with an explicit inverse, every Hopf circle is a great circle, the one great circle through $N$ becomes the $z$-axis, and every other one becomes a round circle because its two linear defining equations become a sphere and a plane in $\mathbb{R}^3$. Steps 5 and 6 prove part (b) by parametrising a general fibre and solving a single trigonometric equation, and Step 7 proves part (c) by moving an arbitrary pair of fibres into the position of Step 6 with a unitary matrix.

**Step 1: $\sigma$ is a bijection $S^3 \setminus \{N\} \to \mathbb{R}^3$ with inverse $\tau$ — this makes images computable.**

The map $\sigma$ is well defined on $S^3 \setminus \{N\}$, the map $\tau$ takes values in $S^3 \setminus \{N\}$, and $\sigma \circ \tau = \mathrm{id}_{\mathbb{R}^3}$, $\tau \circ \sigma = \mathrm{id}_{S^3 \setminus \{N\}}$.

> [!note]- Derivation
> **Well-definedness of $\sigma$.** For $x \in S^3$ we have $x_1^2 \le x_1^2 + x_2^2 + x_3^2 + x_4^2 = 1$, so $x_1 \le 1$, with $x_1 = 1$ if and only if $x_2 = x_3 = x_4 = 0$, that is $x = N$. Hence $1 - x_1 > 0$ on $S^3 \setminus \{N\}$ and $\sigma$ is well defined there (and smooth, as a quotient of smooth functions with non-vanishing denominator).
>
> **$\tau$ takes values in $S^3 \setminus \{N\}$.** For $y \in \mathbb{R}^3$,
> $$|\tau(y)|^2 = \frac{(|y|^2 - 1)^2 + 4y_3^2 + 4y_1^2 + 4y_2^2}{(1 + |y|^2)^2} = \frac{(|y|^2 - 1)^2 + 4|y|^2}{(1 + |y|^2)^2} = \frac{(|y|^2 + 1)^2}{(1 + |y|^2)^2} = 1 \qquad \text{(expanding } (|y|^2 - 1)^2 + 4|y|^2 = |y|^4 + 2|y|^2 + 1\text{)},$$
> so $\tau(y) \in S^3$; and its first coordinate is $\frac{|y|^2 - 1}{|y|^2 + 1} < 1$ (since $|y|^2 - 1 < |y|^2 + 1$), so $\tau(y) \neq N$.
>
> **$\sigma \circ \tau = \mathrm{id}$.** Let $x = \tau(y)$. Then
> $$1 - x_1 = 1 - \frac{|y|^2 - 1}{|y|^2 + 1} = \frac{2}{|y|^2 + 1} \qquad \text{(common denominator)},$$
> and therefore
> $$\sigma(\tau(y)) = \frac{|y|^2 + 1}{2}\,(x_3, x_4, x_2) = \frac{|y|^2 + 1}{2} \cdot \frac{2}{|y|^2 + 1}\,(y_1, y_2, y_3) = y \qquad \text{(definition of } \sigma \text{; } x_3 = \tfrac{2y_1}{1 + |y|^2},\ x_4 = \tfrac{2y_2}{1 + |y|^2},\ x_2 = \tfrac{2y_3}{1 + |y|^2}\text{)}.$$
>
> **$\tau \circ \sigma = \mathrm{id}$.** Let $x \in S^3 \setminus \{N\}$ and $y = \sigma(x)$. Then
> $$|y|^2 = \frac{x_3^2 + x_4^2 + x_2^2}{(1 - x_1)^2} = \frac{1 - x_1^2}{(1 - x_1)^2} = \frac{1 + x_1}{1 - x_1} \qquad \text{(since } x_2^2 + x_3^2 + x_4^2 = 1 - x_1^2 \text{ on } S^3 \text{, and } 1 - x_1^2 = (1 - x_1)(1 + x_1)\text{)},$$
> so that
> $$|y|^2 + 1 = \frac{2}{1 - x_1}, \qquad |y|^2 - 1 = \frac{2x_1}{1 - x_1} \qquad \text{(adding and subtracting } 1 = \tfrac{1 - x_1}{1 - x_1}\text{)}.$$
> Hence the first coordinate of $\tau(y)$ is $\frac{|y|^2 - 1}{|y|^2 + 1} = \frac{2x_1}{1 - x_1} \cdot \frac{1 - x_1}{2} = x_1$, and the remaining coordinates are
> $$\frac{2 y_3}{|y|^2 + 1} = \frac{2x_2}{1 - x_1} \cdot \frac{1 - x_1}{2} = x_2, \qquad \frac{2 y_1}{|y|^2 + 1} = x_3, \qquad \frac{2 y_2}{|y|^2 + 1} = x_4 \qquad \text{(} y_3 = \tfrac{x_2}{1 - x_1},\ y_1 = \tfrac{x_3}{1 - x_1},\ y_2 = \tfrac{x_4}{1 - x_1} \text{ by definition of } \sigma\text{)}.$$
> So $\tau(\sigma(x)) = x$.
>
> Therefore $\sigma$ is a bijection with inverse $\tau$. In particular, for any subset $E \subset S^3 \setminus \{N\}$ we have $\sigma(E) = \{y \in \mathbb{R}^3 : \tau(y) \in E\}$, which is how images are computed in Steps 3 and 4.

**Step 2: Every Hopf circle is a great circle $S^3 \cap \Pi_w$; the fibres over the poles; the only Hopf circle through $N$.**

For $w \in S^3$ the orbit is $U(1) \cdot w = S^3 \cap \Pi_w$ with $\Pi_w := \operatorname{span}_{\mathbb{R}}(w, iw)$ a real 2-plane through the origin. The fibre of the Hopf map over the north pole is $C_0 = U(1) \cdot (0, 1)$, the fibre over the south pole is $U(1) \cdot N = \{(e^{i\theta}, 0)\}$, and $N \in U(1) \cdot w$ if and only if $U(1) \cdot w = U(1) \cdot N$.

> [!note]- Derivation
> **The orbit is the unit circle of the complex line.** The real inner product on $\mathbb{R}^4 = \mathbb{C}^2$ is $\langle u, v \rangle = \operatorname{Re}(u_1 \bar v_1 + u_2 \bar v_2)$ (this is $x_1 x_1' + x_2 x_2' + x_3 x_3' + x_4 x_4'$ when $u = (x_1 + i x_2, x_3 + i x_4)$ and $v = (x_1' + i x_2', x_3' + i x_4')$, because $\operatorname{Re}\big((x_1 + i x_2)(x_1' - i x_2')\big) = x_1 x_1' + x_2 x_2'$). For $w \in S^3$,
> $$\langle w, iw \rangle = \operatorname{Re}\big(w_1 \overline{i w_1} + w_2 \overline{i w_2}\big) = \operatorname{Re}\big(-i(|w_1|^2 + |w_2|^2)\big) = \operatorname{Re}(-i) = 0, \qquad |iw|^2 = |i|^2 |w|^2 = 1 \qquad \text{(} \overline{i} = -i \text{; } |w| = 1\text{)},$$
> so $(w, iw)$ is an orthonormal pair and $\Pi_w = \{s w + t\, iw : s, t \in \mathbb{R}\}$ is a 2-dimensional subspace of $\mathbb{R}^4$ in which $|sw + t\,iw|^2 = s^2 + t^2$ (Pythagoras for an orthonormal pair). Hence
> $$S^3 \cap \Pi_w = \{sw + t\,iw : s^2 + t^2 = 1\} = \{(\cos\theta) w + (\sin\theta)(iw) : \theta \in \mathbb{R}\} = \{(\cos\theta + i \sin\theta) w : \theta \in \mathbb{R}\} = \{e^{i\theta} w : \theta \in \mathbb{R}\} = U(1) \cdot w$$
> (the second equality parametrises the unit circle of $\mathbb{R}^2$; the third uses that scalar multiplication by $\cos\theta + i\sin\theta$ on $\mathbb{C}^2$ is $(\cos\theta) w + (\sin\theta)(iw)$; the last uses $U(1) = \{e^{i\theta}\}$). So every Hopf circle is a great circle of $S^3$.
>
> **Fibres over the poles.** With Bär's formula $\mathrm{Hopf}(w) = \frac{1}{4|w_2|^2 + |w_1|^2}(4 w_1 \bar w_2,\ 4|w_2|^2 - |w_1|^2)$, the equation $\mathrm{Hopf}(w) = (0, 0, 1)$ reads $4 w_1 \bar w_2 = 0$ and $4|w_2|^2 - |w_1|^2 = 4|w_2|^2 + |w_1|^2$; the second says $2|w_1|^2 = 0$, so $w_1 = 0$, and then the first holds automatically. Conversely $w_1 = 0$ gives $\mathrm{Hopf}(0, w_2) = \frac{1}{4|w_2|^2}(0, 4|w_2|^2) = (0, 0, 1)$. So the fibre over the north pole is $\{(0, w_2) : |w_2| = 1\} = \{(0, e^{i\theta})\} = U(1) \cdot (0, 1) = C_0$. The equation $\mathrm{Hopf}(w) = (0, 0, -1)$ reads $4 w_1 \bar w_2 = 0$ and $4|w_2|^2 - |w_1|^2 = -4|w_2|^2 - |w_1|^2$, whose second part says $8|w_2|^2 = 0$, so $w_2 = 0$; conversely $\mathrm{Hopf}(w_1, 0) = \frac{1}{|w_1|^2}(0, -|w_1|^2) = (0, 0, -1)$. So the fibre over the south pole is $\{(w_1, 0) : |w_1| = 1\} = \{(e^{i\theta}, 0)\} = U(1) \cdot N$. (That these fibres are single orbits, rather than unions of orbits, is visible in the formulas; that *every* fibre of the Hopf map is a single orbit is the content of [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map]], which we do not need here.)
>
> **The only Hopf circle through $N$.** Distinct orbits of a group action are disjoint (if $u \in U(1) \cdot w \cap U(1) \cdot w'$ then $u = zw = z'w'$, so $w = z^{-1} z' w'$ and every $z''w = z'' z^{-1} z' w' \in U(1) \cdot w'$; the reverse inclusion is the same argument with the roles exchanged). Since $N \in U(1) \cdot N$, an orbit containing $N$ meets $U(1) \cdot N$ and is therefore equal to it. Thus $N \in U(1) \cdot w$ if and only if $U(1) \cdot w = U(1) \cdot N$; equivalently, $N \in \Pi_w$ if and only if $\Pi_w = \Pi_N$ (because $N \in \Pi_w$ and $|N| = 1$ force $N \in S^3 \cap \Pi_w = U(1) \cdot w$).

**Step 3: The exceptional fibre becomes the $z$-axis.**

$\sigma\big(U(1) \cdot N \setminus \{N\}\big) = \{(0, 0, y_3) : y_3 \in \mathbb{R}\}$.

> [!note]- Derivation
> In real coordinates $U(1) \cdot N = \{(\cos\theta, \sin\theta, 0, 0) : \theta \in \mathbb{R}\}$ (since $e^{i\theta} = \cos\theta + i\sin\theta$ and $w_2 = 0$ means $x_3 = x_4 = 0$). The point $N$ corresponds to $\theta \in 2\pi\mathbb{Z}$; the rest of the orbit is parametrised injectively by $\theta \in (0, 2\pi)$. For such $\theta$,
> $$\sigma(\cos\theta, \sin\theta, 0, 0) = \frac{1}{1 - \cos\theta}\,(0, 0, \sin\theta) = \Big(0, 0, \frac{2\sin(\theta/2)\cos(\theta/2)}{2\sin^2(\theta/2)}\Big) = \big(0, 0, \cot(\theta/2)\big) \qquad \text{(definition of } \sigma\text{; half-angle identities } \sin\theta = 2\sin\tfrac{\theta}{2}\cos\tfrac{\theta}{2},\ 1 - \cos\theta = 2\sin^2\tfrac{\theta}{2}\text{)}.$$
> As $\theta$ runs over $(0, 2\pi)$, $\theta/2$ runs over $(0, \pi)$, on which $\cot$ is a continuous strictly decreasing bijection onto $\mathbb{R}$ (its derivative is $-\csc^2 < 0$, and $\cot(\theta/2) \to +\infty$ as $\theta \to 0^+$, $\cot(\theta/2) \to -\infty$ as $\theta \to 2\pi^-$). Hence the image is exactly the $z$-axis $\{(0, 0, y_3) : y_3 \in \mathbb{R}\}$. The point $(-1, 0) \in S^3$, at $\theta = \pi$, goes to the origin.

**Step 4: A great circle not through $N$ becomes a round circle — the image of $S^3 \cap \Pi$ is a plane section of a sphere.**

Let $\Pi \subset \mathbb{R}^4$ be a 2-dimensional linear subspace with $N \notin \Pi$. Then there are a plane $H \subset \mathbb{R}^3$ through the origin, a point $m \in H$ and a radius $r > 0$ with $\sigma(S^3 \cap \Pi) = \{y \in H : |y - m| = r\}$, a round circle. Applied to $\Pi = \Pi_w$ for $w \notin U(1) \cdot N$, this proves that every Hopf circle other than the exceptional one is mapped onto a round circle, and completes part (a).

> [!note]- Derivation
> **Choose a normalised basis of $\Pi^\perp$.** The orthogonal complement $\Pi^\perp = \{a \in \mathbb{R}^4 : \langle a, x \rangle = 0 \text{ for all } x \in \Pi\}$ is 2-dimensional and $\Pi = (\Pi^\perp)^\perp$ (finite-dimensional linear algebra). Since $N \notin \Pi = (\Pi^\perp)^\perp$, there is $a' \in \Pi^\perp$ with $\langle a', N \rangle = a'_1 \neq 0$; put $a := a' / a'_1$, so $a \in \Pi^\perp$ and $a_1 = 1$. Choose $b' \in \Pi^\perp$ linearly independent of $a$ and set $b := b' - b'_1 a$; then $b \in \Pi^\perp$, $b_1 = b'_1 - b'_1 \cdot 1 = 0$, and $b \neq 0$ (otherwise $b' = b'_1 a$ would be a multiple of $a$). The pair $(a, b)$ is linearly independent (a relation $s a + t b = 0$ has first coordinate $s = 0$, and then $t b = 0$ forces $t = 0$), hence a basis of $\Pi^\perp$, and
> $$\Pi = \{x \in \mathbb{R}^4 : \langle a, x \rangle = 0 \text{ and } \langle b, x \rangle = 0\} \qquad \text{(since } \Pi = (\Pi^\perp)^\perp \text{ and } a, b \text{ span } \Pi^\perp\text{)}.$$
>
> **Substitute the inverse.** By Step 1, $y \in \sigma(S^3 \cap \Pi)$ if and only if $\tau(y) \in \Pi$ (recall $\tau(y) \in S^3 \setminus \{N\}$ for every $y$, and $\sigma$ is a bijection with inverse $\tau$). For any $a \in \mathbb{R}^4$ write $\tilde a := (a_3, a_4, a_2) \in \mathbb{R}^3$, the components of $a$ read in the order in which $\sigma$ uses them. Then
> $$\langle a, \tau(y) \rangle = \frac{a_1 (|y|^2 - 1) + 2 a_2 y_3 + 2 a_3 y_1 + 2 a_4 y_2}{1 + |y|^2} = \frac{a_1 (|y|^2 - 1) + 2 \langle \tilde a, y \rangle}{1 + |y|^2} \qquad \text{(definition of } \tau \text{; } \langle \tilde a, y \rangle = a_3 y_1 + a_4 y_2 + a_2 y_3\text{)},$$
> and since $1 + |y|^2 > 0$,
> $$\langle a, \tau(y) \rangle = 0 \iff a_1 (|y|^2 - 1) + 2\langle \tilde a, y \rangle = 0.$$
>
> **The equation for $a$ is a sphere.** With $a_1 = 1$,
> $$|y|^2 - 1 + 2\langle \tilde a, y \rangle = 0 \iff |y|^2 + 2\langle \tilde a, y \rangle + |\tilde a|^2 = 1 + |\tilde a|^2 \iff |y + \tilde a|^2 = 1 + |\tilde a|^2 \qquad \text{(adding } |\tilde a|^2 \text{ to both sides; expanding } |y + \tilde a|^2\text{)}.$$
> So $\{y : \langle a, \tau(y) \rangle = 0\} = S := \{y : |y - c| = \rho\}$, the sphere with centre $c := -\tilde a$ and radius $\rho := \sqrt{1 + |\tilde a|^2} > |\tilde a| = |c|$.
>
> **The equation for $b$ is a plane.** With $b_1 = 0$, the condition reads $2\langle \tilde b, y \rangle = 0$, that is $y \in H := \{y \in \mathbb{R}^3 : \langle \tilde b, y \rangle = 0\}$. Here $\tilde b = (b_3, b_4, b_2) \neq 0$, because $b \neq 0$ and $b_1 = 0$ mean that some $b_j$ with $j \in \{2, 3, 4\}$ is non-zero; so $H$ is a plane through the origin with unit normal $n := \tilde b / |\tilde b|$.
>
> **Combine.** By the two preceding paragraphs and the definition of $\Pi$ by the equations of $a$ and $b$,
> $$\sigma(S^3 \cap \Pi) = \{y : \tau(y) \in \Pi\} = \{y : \langle a, \tau(y) \rangle = 0 \text{ and } \langle b, \tau(y) \rangle = 0\} = S \cap H.$$
>
> **A plane section of a sphere is a round circle.** Let $m := c - \langle c, n \rangle n$ be the orthogonal projection of the centre onto $H$ (so $m \in H$, since $\langle m, n \rangle = \langle c, n \rangle - \langle c, n \rangle |n|^2 = 0$), and $d := |\langle c, n \rangle|$ the distance from $c$ to $H$. For $y \in H$, the vector $y - m$ lies in $H$ (as $H$ is a linear subspace containing $y$ and $m$) and $m - c = -\langle c, n \rangle n$ is orthogonal to $H$, so
> $$|y - c|^2 = |(y - m) + (m - c)|^2 = |y - m|^2 + |m - c|^2 = |y - m|^2 + d^2 \qquad \text{(Pythagoras: } \langle y - m, m - c \rangle = 0\text{)}.$$
> Hence for $y \in H$: $y \in S \iff |y - m|^2 = \rho^2 - d^2$. Now $d^2 = \langle c, n \rangle^2 \le |c|^2 |n|^2 = |\tilde a|^2 < 1 + |\tilde a|^2 = \rho^2$ (Cauchy–Schwarz, then the definition of $\rho$), so $r := \sqrt{\rho^2 - d^2} > 0$ and
> $$\sigma(S^3 \cap \Pi) = S \cap H = \{y \in H : |y - m| = r\},$$
> a round circle of radius $r > 0$ with centre $m$ in the plane $H$. This is the claim.
>
> **Conclusion of part (a).** By Step 2 every Hopf circle is $S^3 \cap \Pi_w$, and $N \in \Pi_w$ exactly for the exceptional fibre $U(1) \cdot N$. For every other fibre the present step applies and its image is a round circle; for the exceptional fibre Step 3 gives the $z$-axis. Since $S^3$ is the disjoint union of its $U(1)$-orbits (Step 2: distinct orbits are disjoint, and every point lies in its own orbit) and $\sigma$ is a bijection of $S^3 \setminus \{N\}$ onto $\mathbb{R}^3$ (Step 1), $\mathbb{R}^3$ is the disjoint union of the images: round circles, and one straight line. This is the description in Bär's Example 1.5.10.

**Step 5: $\sigma(C_0)$ is the unit circle of the $xy$-plane; parametrisation of a general fibre and its projection.**

$\sigma(C_0) = \{(\cos\theta, \sin\theta, 0) : \theta \in \mathbb{R}\}$. Every Hopf circle other than $C_0$ and $U(1) \cdot N$ has the form
$$C_{\alpha, \phi} := \{\gamma(\theta) : \theta \in \mathbb{R}\}, \qquad \gamma(\theta) := \big(e^{i\theta}\cos\alpha,\ e^{i(\theta + \phi)}\sin\alpha\big), \qquad \alpha \in (0, \pi/2),\ \phi \in \mathbb{R},$$
and its image under $\sigma$ is the curve
$$p(\theta) := \sigma(\gamma(\theta)) = \frac{1}{1 - \cos\alpha\cos\theta}\,\big(\sin\alpha\cos(\theta + \phi),\ \sin\alpha\sin(\theta + \phi),\ \cos\alpha\sin\theta\big),$$
which is injective on $[0, 2\pi)$.

> [!note]- Derivation
> **The image of $C_0$.** In real coordinates $C_0 = \{(0, 0, \cos\theta, \sin\theta)\}$ (as $w_1 = 0$ and $w_2 = e^{i\theta}$). None of these points is $N$ (their first coordinate is $0$). By the definition of $\sigma$,
> $$\sigma(0, 0, \cos\theta, \sin\theta) = \frac{1}{1 - 0}\,(\cos\theta, \sin\theta, 0) = (\cos\theta, \sin\theta, 0),$$
> so $\sigma(C_0)$ is the unit circle of the $xy$-plane, which bounds $D_0$.
>
> **Normal form of a base point.** Let $w = (w_1, w_2) \in S^3$. Since $|w_1|^2 + |w_2|^2 = 1$ with $|w_1|, |w_2| \in [0, 1]$, there is a unique $\alpha \in [0, \pi/2]$ with $|w_1| = \cos\alpha$ and $|w_2| = \sin\alpha$ (namely $\alpha = \arccos|w_1|$; then $\sin\alpha = \sqrt{1 - \cos^2\alpha} = \sqrt{1 - |w_1|^2} = |w_2|$, the square root being non-negative because $\alpha \in [0, \pi/2]$). If $\alpha = \pi/2$ then $w_1 = 0$ and $U(1) \cdot w = C_0$; if $\alpha = 0$ then $w_2 = 0$ and $U(1) \cdot w = U(1) \cdot N$. Otherwise $\alpha \in (0, \pi/2)$, both $w_1$ and $w_2$ are non-zero, and we may write $w_1 = e^{i\phi_1}\cos\alpha$, $w_2 = e^{i\phi_2}\sin\alpha$ with $\phi_1, \phi_2 \in \mathbb{R}$ (polar form of non-zero complex numbers). Put $\phi := \phi_2 - \phi_1$. Then
> $$U(1) \cdot w = \{e^{i\theta'} w : \theta' \in \mathbb{R}\} = \{e^{i(\theta - \phi_1)} w : \theta \in \mathbb{R}\} = \{(e^{i\theta}\cos\alpha,\ e^{i(\theta + \phi_2 - \phi_1)}\sin\alpha) : \theta \in \mathbb{R}\} = C_{\alpha, \phi}$$
> (substituting $\theta' = \theta - \phi_1$, which runs over $\mathbb{R}$ as $\theta$ does; then $e^{i(\theta - \phi_1)} e^{i\phi_1} = e^{i\theta}$ and $e^{i(\theta - \phi_1)} e^{i\phi_2} = e^{i(\theta + \phi)}$). Conversely each $C_{\alpha, \phi}$ is the orbit of $\gamma(0) = (\cos\alpha, e^{i\phi}\sin\alpha) \in S^3$.
>
> **Real coordinates and the projection.** With $e^{i\theta}\cos\alpha = \cos\alpha\cos\theta + i\cos\alpha\sin\theta$ and $e^{i(\theta + \phi)}\sin\alpha = \sin\alpha\cos(\theta + \phi) + i\sin\alpha\sin(\theta + \phi)$,
> $$\gamma(\theta) = \big(\cos\alpha\cos\theta,\ \cos\alpha\sin\theta,\ \sin\alpha\cos(\theta + \phi),\ \sin\alpha\sin(\theta + \phi)\big) \in \mathbb{R}^4.$$
> Its first coordinate satisfies $\cos\alpha\cos\theta \le \cos\alpha < 1$ (as $\cos\theta \le 1$, $\cos\alpha > 0$, and $\alpha > 0$), so $\gamma(\theta) \neq N$ for every $\theta$, in agreement with Step 2, and $1 - \cos\alpha\cos\theta \ge 1 - \cos\alpha > 0$. Applying the definition of $\sigma$ (third, fourth, second coordinate, divided by $1 - x_1$) gives the stated formula for $p(\theta)$.
>
> **Injectivity on a period.** The map $\theta \mapsto e^{i\theta}$ is injective on $[0, 2\pi)$; the map $z \mapsto z w$ is injective on $U(1)$ because $w \neq 0$ (if $zw = z'w$ then $(z - z')w = 0$, so $z = z'$); and $\sigma$ is injective (Step 1). Hence $p = \sigma \circ \gamma$ is injective on $[0, 2\pi)$, and $\sigma(C_{\alpha, \phi}) = \{p(\theta) : \theta \in [0, 2\pi)\}$ with each point of the image attained exactly once.

**Step 6: Each $C_{\alpha, \phi}$ and the $z$-axis meet $D_0$ in exactly one point, transversally — part (b).**

The circle $\sigma(C_{\alpha, \phi})$ meets the plane $\{y_3 = 0\}$ in exactly two points, $p(0)$ at distance $\cot(\alpha/2) > 1$ from the origin and $p(\pi)$ at distance $\tan(\alpha/2) \in (0, 1)$; so it meets $D_0$ exactly in $p(\pi)$, and there $p_3'(\pi) = -\frac{\cos\alpha}{1 + \cos\alpha} \neq 0$, so the crossing is transverse. The $z$-axis meets $D_0$ exactly at the origin, transversally.

> [!note]- Derivation
> **Intersection with the plane.** By Step 5, $p(\theta) \in \{y_3 = 0\}$ if and only if $\frac{\cos\alpha\sin\theta}{1 - \cos\alpha\cos\theta} = 0$, if and only if $\sin\theta = 0$ (the denominator is positive and $\cos\alpha > 0$ for $\alpha \in (0, \pi/2)$), if and only if $\theta \in \{0, \pi\}$ for $\theta \in [0, 2\pi)$. By the injectivity of Step 5, $\sigma(C_{\alpha, \phi}) \cap \{y_3 = 0\}$ consists of exactly the two points $p(0)$ and $p(\pi)$.
>
> **The two points.** At $\theta = 0$: $\cos\theta = 1$, $\sin\theta = 0$, so
> $$p(0) = \frac{\sin\alpha}{1 - \cos\alpha}\,(\cos\phi, \sin\phi, 0), \qquad |p(0)| = \frac{\sin\alpha}{1 - \cos\alpha} = \frac{2\sin(\alpha/2)\cos(\alpha/2)}{2\sin^2(\alpha/2)} = \cot(\alpha/2) \qquad \text{(} |(\cos\phi, \sin\phi, 0)| = 1\text{; half-angle identities)}.$$
> At $\theta = \pi$: $\cos\theta = -1$, $\sin\theta = 0$, $\cos(\pi + \phi) = -\cos\phi$, $\sin(\pi + \phi) = -\sin\phi$, so
> $$p(\pi) = -\frac{\sin\alpha}{1 + \cos\alpha}\,(\cos\phi, \sin\phi, 0), \qquad |p(\pi)| = \frac{\sin\alpha}{1 + \cos\alpha} = \frac{2\sin(\alpha/2)\cos(\alpha/2)}{2\cos^2(\alpha/2)} = \tan(\alpha/2) \qquad \text{(half-angle identity } 1 + \cos\alpha = 2\cos^2(\alpha/2)\text{)}.$$
> Since $\alpha \in (0, \pi/2)$ we have $\alpha/2 \in (0, \pi/4)$; on this interval $\tan$ is strictly increasing with $\tan 0 = 0$ and $\tan(\pi/4) = 1$, so $0 < \tan(\alpha/2) < 1$, and $\cot(\alpha/2) = 1/\tan(\alpha/2) > 1$. Therefore $p(\pi) \in D_0$ (it lies in the plane $y_3 = 0$ at distance less than $1$ from the origin) while $p(0) \notin \overline{D_0}$ (distance greater than $1$). So $\sigma(C_{\alpha, \phi}) \cap D_0 = \{p(\pi)\}$: exactly one point. (In particular $p(\pi)$ is not on the unit circle, and indeed $\sigma(C_{\alpha, \phi}) \cap \sigma(C_0) = \emptyset$, as it must be: distinct orbits are disjoint and $\sigma$ is injective.)
>
> **Transversality at $p(\pi)$.** Write $p_3(\theta) = \frac{\cos\alpha\sin\theta}{1 - \cos\alpha\cos\theta}$. By the quotient rule,
> $$p_3'(\theta) = \cos\alpha \cdot \frac{\cos\theta\,(1 - \cos\alpha\cos\theta) - \sin\theta\,(\cos\alpha\sin\theta)}{(1 - \cos\alpha\cos\theta)^2} = \cos\alpha \cdot \frac{\cos\theta - \cos\alpha(\cos^2\theta + \sin^2\theta)}{(1 - \cos\alpha\cos\theta)^2} = \frac{\cos\alpha\,(\cos\theta - \cos\alpha)}{(1 - \cos\alpha\cos\theta)^2} \qquad \text{(} \cos^2\theta + \sin^2\theta = 1\text{)}.$$
> At $\theta = \pi$:
> $$p_3'(\pi) = \frac{\cos\alpha\,(-1 - \cos\alpha)}{(1 + \cos\alpha)^2} = -\frac{\cos\alpha}{1 + \cos\alpha} \neq 0 \qquad \text{(cancelling one factor } 1 + \cos\alpha > 0 \text{; } \cos\alpha > 0\text{)}.$$
> The image $\sigma(C_{\alpha, \phi})$ is a round circle (Step 4), a smooth embedded curve, and $p$ is a smooth parametrisation of it with $p'(\pi) \neq 0$ (its third component is non-zero), so the tangent line of the circle at $p(\pi)$ is $\mathbb{R}\, p'(\pi)$. The tangent plane of $\{y_3 = 0\}$ is $\{v \in \mathbb{R}^3 : v_3 = 0\}$, and $p'(\pi)$ does not lie in it. Hence the circle crosses the plane $\{y_3 = 0\}$ transversally at $p(\pi)$. Together with the one-point intersection, this says exactly that $\sigma(C_{\alpha, \phi})$ is linked with $\sigma(C_0)$ in the sense of the definition on this page.
>
> **The $z$-axis.** By Step 3 the exceptional fibre becomes $\{(0, 0, \cot(\theta/2)) : \theta \in (0, 2\pi)\}$. It meets $\{y_3 = 0\}$ exactly where $\cot(\theta/2) = 0$, that is at $\theta = \pi$, at the origin, which lies in $D_0$; so it meets $D_0$ in exactly one point. The tangent vector there is $\frac{d}{d\theta}(0, 0, \cot(\theta/2))|_{\theta = \pi} = (0, 0, -\tfrac{1}{2}\csc^2(\pi/2)) = (0, 0, -\tfrac12) \neq 0$, with non-zero third component, so the crossing is transverse. Hence the $z$-axis is linked with $\sigma(C_0)$ as well.
>
> **Conclusion of part (b).** By Step 5 every Hopf circle other than $C_0$ is either $U(1) \cdot N$ or some $C_{\alpha, \phi}$ with $\alpha \in (0, \pi/2)$; in both cases its image under $\sigma$ meets $D_0$ in exactly one point, transversally. Therefore every Hopf circle other than $C_0$ is linked with $\sigma(C_0)$.
>
> **A remark on the direction of crossing.** In every case the third component of the tangent vector at the crossing is negative ($p_3'(\pi) < 0$ for the circles, $-\tfrac12$ for the axis) while the parameter $\theta$ increases along the direction of the $U(1)$-action: all Hopf circles pierce the disc $D_0$ in the same direction. This is the coordinate shadow of the statement that all the linking numbers are equal (to $+1$ or to $-1$, depending on the orientations chosen), which is what one expects from a fibration whose fibres are all moved onto one another by the symmetry group $U(2)$ of Step 7.

**Step 7: Any two Hopf circles — reduction to part (b) by a unitary matrix.**

Let $C_1 \neq C_2$ be Hopf circles and $w \in C_1$. There is $A \in U(2)$ with $Aw = (0, 1)$; $A$ preserves $S^3$, commutes with the $U(1)$-action, maps Hopf circles bijectively onto Hopf circles, and satisfies $A C_1 = C_0$. Hence $A C_2$ is a Hopf circle different from $C_0$, and by part (b) $\sigma(A C_2 \setminus \{N\})$ is linked with $\sigma(A C_1) = \sigma(C_0)$, the unit circle of the $xy$-plane.

> [!note]- Derivation
> **Construction of $A$.** Let $w = (w_1, w_2) \in S^3$ and $v := (-\bar w_2, \bar w_1)$. With the Hermitian inner product $\langle u, u' \rangle_{\mathbb{C}} = u_1 \bar u'_1 + u_2 \bar u'_2$,
> $$\langle v, w \rangle_{\mathbb{C}} = -\bar w_2 \bar w_1 + \bar w_1 \bar w_2 = 0, \qquad |v|^2 = |w_2|^2 + |w_1|^2 = 1,$$
> so $(v, w)$ is an orthonormal basis of $\mathbb{C}^2$. Let $B$ be the $2 \times 2$ complex matrix with columns $v$ and $w$; then $B^* B$ is the Gram matrix of $(v, w)$, which is the identity, so $B \in U(2)$, and $B e_2 = w$ where $e_2 = (0, 1)$. Put $A := B^{-1} = B^* \in U(2)$; then $A w = e_2 = (0, 1)$.
>
> **$A$ preserves $S^3$ and commutes with the action.** For $u \in \mathbb{C}^2$, $|Au|^2 = \langle Au, Au \rangle_{\mathbb{C}} = \langle u, A^*A u \rangle_{\mathbb{C}} = |u|^2$ (since $A^*A = 1$), so $A(S^3) \subset S^3$, and likewise $A^{-1}(S^3) \subset S^3$; hence $A$ restricts to a bijection of $S^3$. Since $A$ is $\mathbb{C}$-linear, $A(zu) = zAu$ for $z \in U(1)$, so
> $$A(U(1) \cdot u) = \{A(zu) : z \in U(1)\} = \{z\,Au : z \in U(1)\} = U(1) \cdot Au,$$
> that is, $A$ maps the orbit of $u$ onto the orbit of $Au$; applying the same to $A^{-1}$ shows that $A$ induces a bijection of the set of Hopf circles. Because $A$ preserves the Hermitian norm it preserves the real inner product $\operatorname{Re}\langle \cdot, \cdot \rangle_{\mathbb{C}}$ of $\mathbb{R}^4$ (polarisation), so $A$ is an isometry of $\mathbb{R}^4$; consequently $\sigma \circ A$, defined on $S^3 \setminus \{A^{-1}N\}$, is stereographic projection of $S^3$ from the point $A^{-1}N$ followed by the orthogonal change of coordinates $A$ — a legitimate "stereographic projection from a point of a fibre", the fibre in question being $A^{-1}(U(1) \cdot N)$.
>
> **Reduction.** With $w \in C_1$, $A C_1 = A(U(1) \cdot w) = U(1) \cdot (0, 1) = C_0$. Since $A$ is injective on the set of Hopf circles and $C_2 \neq C_1$, we have $A C_2 \neq C_0$. By Step 5, $A C_2$ is either $U(1) \cdot N$ or some $C_{\alpha, \phi}$, and by Step 6 its image under $\sigma$ (minus $N$ in the first case) meets $D_0$ in exactly one point, transversally. In the coordinates $y = \sigma(Ax)$ on $S^3 \setminus \{A^{-1}N\}$, therefore, $C_1$ is the unit circle of the $xy$-plane and $C_2$ is a round circle or the $z$-axis linked with it. This is part (c): any two Hopf circles are linked. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** With the notation of the Problem Statement: (a) $\sigma$ is a bijection with inverse $\tau$, $\sigma(U(1) \cdot N \setminus \{N\})$ is the $z$-axis, every other Hopf circle is mapped by $\sigma$ onto a round circle, and $\mathbb{R}^3$ is the disjoint union of these circles and that line; (b) $\sigma(C_0)$ is the unit circle of the $xy$-plane and every other Hopf circle is linked with it; (c) for any two distinct Hopf circles $C_1, C_2$ there is $A \in U(2)$ with $AC_1 = C_0$ and $AC_2$ linked with $C_0$ after projection.
>
> **Part (a).**
>
> *Step 0 (the bijection).* For $x \in S^3$, $x_1 \le 1$ with equality only at $N$, so $\sigma$ is defined on $S^3 \setminus \{N\}$. For $y \in \mathbb{R}^3$, $|\tau(y)|^2 = \frac{(|y|^2 - 1)^2 + 4|y|^2}{(1 + |y|^2)^2} = 1$ and the first coordinate of $\tau(y)$ is $\frac{|y|^2 - 1}{|y|^2 + 1} < 1$, so $\tau(y) \in S^3 \setminus \{N\}$. If $x = \tau(y)$ then $1 - x_1 = \frac{2}{1 + |y|^2}$ and $(x_3, x_4, x_2) = \frac{2}{1 + |y|^2} y$, so $\sigma(\tau(y)) = y$. If $y = \sigma(x)$ with $x \in S^3 \setminus \{N\}$, then $|y|^2 = \frac{1 - x_1^2}{(1 - x_1)^2} = \frac{1 + x_1}{1 - x_1}$, so $|y|^2 + 1 = \frac{2}{1 - x_1}$ and $|y|^2 - 1 = \frac{2x_1}{1 - x_1}$, whence $\tau(y) = (x_1, x_2, x_3, x_4)$. Thus $\sigma$ is a bijection with inverse $\tau$, and for $E \subset S^3 \setminus \{N\}$, $\sigma(E) = \{y : \tau(y) \in E\}$.
>
> *Step 1 (orbits are great circles).* For $w \in S^3$, $\langle w, iw \rangle = \operatorname{Re}(-i|w|^2) = 0$ and $|iw| = 1$, so $\Pi_w := \operatorname{span}_{\mathbb{R}}(w, iw)$ is a 2-plane with orthonormal basis $(w, iw)$, and $S^3 \cap \Pi_w = \{(\cos\theta)w + (\sin\theta)iw\} = \{e^{i\theta}w\} = U(1) \cdot w$. Distinct orbits are disjoint, so $N \in U(1) \cdot w$ if and only if $U(1) \cdot w = U(1) \cdot N$, if and only if $N \in \Pi_w$. From Bär's formula, $\mathrm{Hopf}(w) = (0, 0, 1)$ if and only if $w_1 = 0$, and $\mathrm{Hopf}(w) = (0, 0, -1)$ if and only if $w_2 = 0$; so $C_0 = U(1) \cdot (0, 1)$ is the fibre over the north pole and $U(1) \cdot N = \{(e^{i\theta}, 0)\}$ the fibre over the south pole.
>
> *Step 2 (the exceptional fibre).* For $\theta \in (0, 2\pi)$, $\sigma(\cos\theta, \sin\theta, 0, 0) = (0, 0, \frac{\sin\theta}{1 - \cos\theta}) = (0, 0, \cot(\theta/2))$ (half-angle identities), and $\cot : (0, \pi) \to \mathbb{R}$ is a bijection; so $\sigma(U(1) \cdot N \setminus \{N\})$ is the $z$-axis.
>
> *Step 3 (other fibres are round circles).* Let $\Pi$ be a 2-plane with $N \notin \Pi$. Choose a basis $(a, b)$ of $\Pi^\perp$ with $a_1 = 1$, $b_1 = 0$ (possible since $N \notin (\Pi^\perp)^\perp$ gives some $a' \in \Pi^\perp$ with $a'_1 \neq 0$; normalise it, and subtract its multiple from an independent $b'$). For $a \in \mathbb{R}^4$ put $\tilde a = (a_3, a_4, a_2)$; then $\langle a, \tau(y) \rangle = 0$ if and only if $a_1(|y|^2 - 1) + 2\langle \tilde a, y \rangle = 0$ (multiply through by $1 + |y|^2 > 0$). For $a$ this is $|y + \tilde a|^2 = 1 + |\tilde a|^2$, the sphere $S$ with centre $c = -\tilde a$ and radius $\rho = \sqrt{1 + |\tilde a|^2}$; for $b$ it is $\langle \tilde b, y \rangle = 0$ with $\tilde b \neq 0$, a plane $H$ through the origin with unit normal $n$. Hence $\sigma(S^3 \cap \Pi) = \{y : \tau(y) \in \Pi\} = S \cap H$. With $m = c - \langle c, n \rangle n \in H$ and $d = |\langle c, n \rangle|$, Pythagoras gives $|y - c|^2 = |y - m|^2 + d^2$ for $y \in H$, and $d^2 \le |c|^2 = |\tilde a|^2 < \rho^2$ (Cauchy–Schwarz), so $S \cap H = \{y \in H : |y - m| = r\}$ with $r = \sqrt{\rho^2 - d^2} > 0$: a round circle. Applied to $\Pi_w$ for $U(1) \cdot w \neq U(1) \cdot N$, this shows every non-exceptional Hopf circle becomes a round circle. As $S^3$ is the disjoint union of its orbits and $\sigma$ is a bijection, $\mathbb{R}^3$ is the disjoint union of these round circles and the $z$-axis. This proves (a).
>
> **Part (b).**
>
> *Step 4 (normal form).* $\sigma(0, 0, \cos\theta, \sin\theta) = (\cos\theta, \sin\theta, 0)$, so $\sigma(C_0)$ is the unit circle of the $xy$-plane. For $w \in S^3$ write $|w_1| = \cos\alpha$, $|w_2| = \sin\alpha$ with $\alpha \in [0, \pi/2]$; $\alpha = \pi/2$ gives $C_0$, $\alpha = 0$ gives $U(1) \cdot N$, and otherwise $w = (e^{i\phi_1}\cos\alpha, e^{i\phi_2}\sin\alpha)$ and, with $\phi = \phi_2 - \phi_1$, $U(1) \cdot w = \{e^{i(\theta - \phi_1)} w\} = \{\gamma(\theta)\} = C_{\alpha, \phi}$ where $\gamma(\theta) = (e^{i\theta}\cos\alpha, e^{i(\theta + \phi)}\sin\alpha)$. In real coordinates $\gamma(\theta) = (\cos\alpha\cos\theta, \cos\alpha\sin\theta, \sin\alpha\cos(\theta + \phi), \sin\alpha\sin(\theta + \phi))$, whose first coordinate is at most $\cos\alpha < 1$, so
> $$p(\theta) := \sigma(\gamma(\theta)) = \frac{\big(\sin\alpha\cos(\theta + \phi),\ \sin\alpha\sin(\theta + \phi),\ \cos\alpha\sin\theta\big)}{1 - \cos\alpha\cos\theta},$$
> and $p$ is injective on $[0, 2\pi)$ (injectivity of $\theta \mapsto e^{i\theta}$ on $[0, 2\pi)$, of $z \mapsto zw$, and of $\sigma$).
>
> *Step 5 (one point in the disc).* $p_3(\theta) = 0$ if and only if $\sin\theta = 0$ (as $\cos\alpha > 0$ and the denominator is positive), if and only if $\theta \in \{0, \pi\}$. Now $|p(0)| = \frac{\sin\alpha}{1 - \cos\alpha} = \cot(\alpha/2) > 1$ and $|p(\pi)| = \frac{\sin\alpha}{1 + \cos\alpha} = \tan(\alpha/2) \in (0, 1)$, because $\alpha/2 \in (0, \pi/4)$ (half-angle identities; monotonicity of $\tan$ on $(0, \pi/4)$). So $\sigma(C_{\alpha, \phi}) \cap D_0 = \{p(\pi)\}$.
>
> *Step 6 (transversality).* By the quotient rule $p_3'(\theta) = \frac{\cos\alpha(\cos\theta - \cos\alpha)}{(1 - \cos\alpha\cos\theta)^2}$, so $p_3'(\pi) = -\frac{\cos\alpha}{1 + \cos\alpha} \neq 0$. Since $\sigma(C_{\alpha, \phi})$ is a round circle with smooth parametrisation $p$ and $p'(\pi) \neq 0$, its tangent line at $p(\pi)$ is $\mathbb{R} p'(\pi)$, which is not contained in $\{v_3 = 0\}$. Hence the crossing is transverse. For the $z$-axis, $\{(0, 0, \cot(\theta/2))\}$ meets $\{y_3 = 0\}$ only at $\theta = \pi$, at the origin $\in D_0$, with tangent $(0, 0, -\tfrac12)$, transversally. Therefore every Hopf circle other than $C_0$ is linked with $\sigma(C_0)$. This proves (b).
>
> **Part (c).**
>
> *Step 7 (moving a pair into position).* Let $C_1 \neq C_2$ be Hopf circles and $w \in C_1$. With $v = (-\bar w_2, \bar w_1)$, the pair $(v, w)$ is orthonormal for the Hermitian product, so the matrix $B$ with columns $v, w$ is unitary with $Be_2 = w$; $A := B^*$ is unitary with $Aw = (0, 1)$. As $A^*A = 1$, $A$ preserves the Hermitian norm, hence restricts to a bijection of $S^3$ and is an isometry of $\mathbb{R}^4$; as $A$ is $\mathbb{C}$-linear, $A(U(1) \cdot u) = U(1) \cdot Au$, so $A$ permutes the Hopf circles. Then $AC_1 = U(1) \cdot (0, 1) = C_0$ and $AC_2 \neq C_0$, so by (b) the image of $AC_2$ under $\sigma$ meets $D_0$ in exactly one point, transversally, while $AC_1$ becomes the unit circle of the $xy$-plane. In the stereographic coordinates $\sigma \circ A$ on $S^3 \setminus \{A^{-1}N\}$, therefore, $C_1$ and $C_2$ are linked. This proves (c).
>
> Therefore, under the stereographic projection $\sigma$ from a point of the fibre over the south pole, that fibre becomes the $z$-axis and every other fibre a round circle; the fibre over the north pole becomes the unit circle of the $xy$-plane and is threaded exactly once, transversally, by every other fibre; and any two fibres can be brought into this position by a unitary change of coordinates. Any two Hopf circles are linked. $\blacksquare$

> [!note]- Sanity check: the explicit circle for phi = 0, and rotation equivariance
> For $\phi = 0$ the plane $\Pi_w$ of the fibre $C_{\alpha, 0}$ is spanned by $\gamma(0) = (\cos\alpha, 0, \sin\alpha, 0)$ and $\gamma(\pi/2) = (0, \cos\alpha, 0, \sin\alpha)$, so $\Pi_w^\perp$ is spanned by $(\sin\alpha, 0, -\cos\alpha, 0)$ and $(0, \sin\alpha, 0, -\cos\alpha)$ (each is orthogonal to both spanning vectors, by direct substitution). Normalising as in Step 4: $a = (1, 0, -\cot\alpha, 0)$ and $b = (0, \sin\alpha, 0, -\cos\alpha)$ with $b_1 = 0$. Then $\tilde a = (a_3, a_4, a_2) = (-\cot\alpha, 0, 0)$, so the sphere $S$ has centre $c = (\cot\alpha, 0, 0)$ and radius $\rho = \sqrt{1 + \cot^2\alpha} = 1/\sin\alpha$; and $\tilde b = (b_3, b_4, b_2) = (0, -\cos\alpha, \sin\alpha)$, so $H = \{y : -\cos\alpha\, y_2 + \sin\alpha\, y_3 = 0\} = \{y_3 = \cot\alpha\, y_2\}$, a plane containing the $x$-axis. The centre $c$ lies in $H$ (its $y_2$ and $y_3$ components vanish), so $d = 0$ and $\sigma(C_{\alpha, 0})$ is the circle of radius $1/\sin\alpha$ centred at $(\cot\alpha, 0, 0)$ in the tilted plane $y_3 = \cot\alpha\, y_2$. Check against Step 6: the two points of the circle on the $x$-axis are $c \pm (1/\sin\alpha)(1, 0, 0)$, at $y_1 = \cot\alpha + \frac{1}{\sin\alpha} = \frac{\cos\alpha + 1}{\sin\alpha} = \cot(\alpha/2)$ and $y_1 = \cot\alpha - \frac{1}{\sin\alpha} = \frac{\cos\alpha - 1}{\sin\alpha} = -\tan(\alpha/2)$, which are exactly $p(0)$ and $p(\pi)$. As $\alpha \to \pi/2$ the centre tends to the origin, the radius to $1$, and the plane to $\{y_3 = 0\}$: the circles $C_{\alpha, 0}$ converge to $\sigma(C_0)$. As $\alpha \to 0$ the centre and the radius both go to infinity: the circles converge to the $z$-axis.
>
> For general $\phi$, let $R_\phi(w_1, w_2) := (w_1, e^{i\phi} w_2)$, a unitary map fixing $N$, and let $\rho_\phi$ be the rotation of $\mathbb{R}^3$ by the angle $\phi$ about the $z$-axis. In real coordinates $R_\phi$ fixes $(x_1, x_2)$ and rotates the pair $(x_3, x_4)$ by $\phi$; since $\sigma(x) = \frac{1}{1 - x_1}(x_3, x_4, x_2)$ uses $(x_3, x_4)$ as its first two components and $x_1$ only in the denominator, $\sigma \circ R_\phi = \rho_\phi \circ \sigma$ on $S^3 \setminus \{N\}$. Also $R_\phi \gamma_{\alpha, 0}(\theta) = \gamma_{\alpha, \phi}(\theta)$, so $\sigma(C_{\alpha, \phi}) = \rho_\phi(\sigma(C_{\alpha, 0}))$: the general fibre is the $\phi = 0$ fibre rotated about the $z$-axis, and since $\rho_\phi$ preserves $D_0$, $\sigma(C_0)$, and the plane $\{y_3 = 0\}$, the linking statement for $C_{\alpha, \phi}$ follows from that for $C_{\alpha, 0}$ — in agreement with the direct computation of Step 6, where $\phi$ entered only through the direction $(\cos\phi, \sin\phi, 0)$ of the two intersection points.

> [!warning] Illegal but tempting: "the fibres are disjoint circles, so they are unlinked"
> Disjointness says nothing about linking; two disjoint round circles in $\mathbb{R}^3$ may be unlinked (two concentric circles in a plane) or linked (a circle and a second circle through its centre in a perpendicular plane). The extra condition that makes an intersection count meaningful is a *spanning surface*: one must choose a disc bounded by one circle and count the transverse crossings of the other circle with it, which is what Step 6 does with the flat disc $D_0$. The count is $\pm 1$ here and $0$ for unlinked circles. (That the count does not depend on the choice of spanning disc is a homological statement; it is not needed here because the page takes the criterion with the specific disc $D_0$ as its definition.)

---

# Key Takeaways

**Orbits of a linear action on a sphere are the sphere's intersections with linear subspaces, and stereographic projection turns those into round spheres and circles: the picture of a quotient can be computed exactly.** The single observation that powers part (a) is that $U(1) \cdot w = S^3 \cap \operatorname{span}_{\mathbb{R}}(w, iw)$, because $w$ and $iw$ are orthonormal. Every orbit is therefore cut out by two *linear* equations $\langle a, x \rangle = 0$, $\langle b, x \rangle = 0$, and the substitution $x = \tau(y)$ converts a linear equation in $x$ into an equation $a_1(|y|^2 - 1) + 2\langle \tilde a, y \rangle = 0$ in $y$ — a sphere if $a_1 \neq 0$, a plane if $a_1 = 0$. This is the entire content of the classical fact that stereographic projection maps circles to circles or lines, and it is proved in two lines once one pulls back the equations rather than pushing forward a parametrisation. The trigger for this technique is any question of the form "what does an orbit of a linear action on $S^n$ look like in a stereographic chart"; the transferable diagnostic is to ask whether the orbit is a *linear section* of the sphere (true for orbits of one-parameter subgroups of $O(n+1)$ through points of a 2-plane, for orbits of $U(1) \subset U(n)$ acting by scalars, and for great spheres cut by fixed-point sets of linear involutions) and, if so, to write its defining linear equations and substitute the inverse projection.

**Linking is detected by counting transverse intersections with a spanning disc, and the count is a scalar equation once the disc is flat.** The whole of part (b) reduces to solving $p_3(\theta) = 0$ on one period, because the disc $D_0$ was chosen flat in the coordinate plane $\{y_3 = 0\}$. That choice was made available by the choice of projection point: projecting from a point of the fibre over the south pole makes the fibre over the north pole the unit circle of the $xy$-plane. The reusable principle is that a linking or intersection question about curves in $\mathbb{R}^3$ should be set up so that one of the two objects is as flat as possible, since then "meets the disc" becomes "one coordinate vanishes and the other two are small". The decisive computation, that a general fibre meets the plane at distances $\cot(\alpha/2)$ and $\tan(\alpha/2)$ from the origin — one outside and one inside the unit circle for every $\alpha \in (0, \pi/2)$ — is what shows every fibre threads the disc exactly once; and the derivative $p_3'(\pi) = -\cos\alpha/(1 + \cos\alpha)$ shows that the threading is transverse and, since it is negative for every $\alpha$, that all fibres thread in the same direction. When the series reaches homology (chapter XII), this same count becomes the linking number of the two fibres, and its non-vanishing is the elementary reason that the Hopf fibration is non-trivial; the same non-triviality is expressed by the first Chern class of the Hopf line bundle in [[Ex - The Chern Number of the Hopf Line Bundle over CP^1]] and, in chapter III, on [[Def - The Hopf Bundle]].

**Use the largest symmetry group that commutes with the action to reduce "any two" to "one specific pair".** Part (c) is not a new computation: it is the observation that $U(2)$ acts on $S^3$ by isometries, commutes with scalar multiplication by $U(1)$, and acts transitively on $S^3$, so that any Hopf circle can be moved onto $C_0$ by a unitary matrix, and the second circle of the pair then falls under part (b). The same pattern — find the group of symmetries of the whole configuration, check that it acts transitively on the objects being compared, and compute for one normalised representative — is how one shows that all fibres of a homogeneous bundle are congruent, that all great circles of $S^3$ are equivalent under $O(4)$, and, later in the series, that the holonomy groups at different points of a connected manifold are conjugate. The diagnostic question to ask is "what acts on the total space, preserving the structure, and how many orbits does it have on the set of objects I am comparing?"; if the answer is "one orbit", a single explicit computation settles the general statement. The companion exercises for this page are [[Ex - The Scalar Action of U(1) on Odd Spheres is Free]] (why each fibre is an embedded circle), [[Ex - The Hopf Map is a Submersion]] (why the fibres vary smoothly), and [[Ex - SU(2) is Diffeomorphic to S^3]] (the identification of $S^3$ with $SU(2)$ under which the Hopf circles become the cosets of a circle subgroup).
