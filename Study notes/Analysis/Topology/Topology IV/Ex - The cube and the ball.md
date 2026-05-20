---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Convex Body"
  - "Thm - Compact Convex Body is Homeomorphic to a Disk"
tags: [analysis, topology, convexity, homeomorphism]
---

# Problem Statement

Show that the closed cube $[-1, 1]^n \subseteq \mathbb{R}^n$ is homeomorphic to the closed unit ball $D^n = \{x \in \mathbb{R}^n : \|x\| \leq 1\}$, and exhibit an explicit homeomorphism.

**Recall:**

$D^n$ is the closed unit ball in the Euclidean norm. $[-1, 1]^n$ is the closed cube of side length $2$. Both are [[Def - Convex Body|compact convex bodies]] with nonempty interior. By [[Thm - Compact Convex Body is Homeomorphic to a Disk]], both are homeomorphic to $D^n$. The exercise asks for an explicit homeomorphism via radial scaling.

---

# Convergent Strategy

**Problem class:** Construct an explicit homeomorphism between two compact convex bodies, both containing the origin in the interior.

**Assumption pattern:** Both the cube and the ball are convex, compact, and have $0$ in the interior. They are radially parametrized from $0$ by their "support functions": each ray from $0$ exits the body at a unique point, parametrized by the direction.

**Theorem routing:** Use the radial homeomorphism: send the boundary of one body to the boundary of the other via radial projection, then extend radially. Specifically: for $x \neq 0$, scale $x$ so that the resulting point is on the boundary of the cube, and vice versa.

**Key decision point:** The scaling factor. For a point $x \in D^n$ with $\|x\| > 0$, the ray from $0$ through $x$ exits $D^n$ at $x/\|x\|$ (length 1) and exits the cube at $x / \|x\|_\infty$ (where the sup-norm $\|x\|_\infty = \max_i |x_i|$). The homeomorphism $D^n \to [-1, 1]^n$ scales the ball's radial structure to the cube's.

---

# Legal Operations Used

1. **Radial parametrization of a convex body.** Every ray from an interior point exits the boundary at exactly one point.

2. **Continuous extension at the origin.** The radial map is defined for $x \neq 0$; we extend by sending $0 \mapsto 0$, and verify continuity at the origin via a bound.

3. **Bijection from radial structure.** The radial scaling is a bijection between the two bodies because each maps a ray to a ray.

---

# Hints

> [!note]- Hint 1
> Both the unit ball and the cube are radially parametrized from the origin. The ball's boundary is $\{x : \|x\| = 1\}$; the cube's boundary is $\{x : \|x\|_\infty = 1\}$, where $\|x\|_\infty = \max_i |x_i|$.

> [!note]- Hint 2
> Define $f : D^n \to [-1, 1]^n$ as follows: for $x \neq 0$, $f(x) := \|x\| \cdot (x/\|x\|_\infty)$. (For $x = 0$, $f(0) = 0$.) This rescales the ball's "radial coordinate $\|x\|$" to the cube's "radial coordinate $\|x\|_\infty$".

> [!note]- Hint 3
> Equivalently: $f(x) = x \cdot \frac{\|x\|}{\|x\|_\infty}$. Then $\|f(x)\|_\infty = \|x\| \cdot \|x/\|x\|_\infty\|_\infty = \|x\|$ — so $f(x) \in [-1, 1]^n$ iff $\|x\| \leq 1$, i.e., iff $x \in D^n$.

> [!note]- Hint 4
> The inverse: $g : [-1, 1]^n \to D^n$, $g(y) = y \cdot \frac{\|y\|_\infty}{\|y\|}$ for $y \neq 0$, $g(0) = 0$.

---

# Solution

**Step 1: Define the explicit map.**

For $x \in D^n$, define
$$f(x) := \begin{cases} x \cdot \dfrac{\|x\|}{\|x\|_\infty} & x \neq 0 \\ 0 & x = 0. \end{cases}$$

**Step 2: Verify $f(x) \in [-1, 1]^n$.**

> [!note]- Derivation
> For $x \neq 0$: $\|f(x)\|_\infty = \left\| x \cdot \frac{\|x\|}{\|x\|_\infty} \right\|_\infty = \frac{\|x\|}{\|x\|_\infty} \cdot \|x\|_\infty = \|x\|$.
>
> Since $x \in D^n$, $\|x\| \leq 1$. So $\|f(x)\|_\infty \leq 1$, meaning $f(x) \in [-1, 1]^n$.
>
> For $x = 0$: $f(0) = 0 \in [-1, 1]^n$.

**Step 3: Verify $f$ is continuous.**

> [!note]- Derivation
> *Away from $0$:* $f(x)$ is a continuous expression in $x$. $\|x\|$ and $\|x\|_\infty$ are continuous functions on $\mathbb{R}^n$; their ratio is continuous on $\mathbb{R}^n \setminus \{0\}$ (where neither vanishes); scalar multiplication by this ratio is continuous.
>
> *At $0$:* $\|f(x)\|_\infty = \|x\|$, so $\|f(x)\|_\infty \to 0$ as $x \to 0$. Hence $f(x) \to 0 = f(0)$. Continuous.

**Step 4: Define the inverse and verify.**

> [!note]- Derivation
> For $y \in [-1, 1]^n$, define
> $$g(y) := \begin{cases} y \cdot \dfrac{\|y\|_\infty}{\|y\|} & y \neq 0 \\ 0 & y = 0. \end{cases}$$
>
> Check $g(y) \in D^n$: $\|g(y)\| = \|y \cdot \frac{\|y\|_\infty}{\|y\|}\| = \frac{\|y\|_\infty}{\|y\|} \cdot \|y\| = \|y\|_\infty$. Since $y \in [-1, 1]^n$, $\|y\|_\infty \leq 1$. So $\|g(y)\| \leq 1$, $g(y) \in D^n$.
>
> Verify $g \circ f = 1$ on $D^n \setminus \{0\}$:
> $$g(f(x)) = f(x) \cdot \frac{\|f(x)\|_\infty}{\|f(x)\|} = \left(x \cdot \frac{\|x\|}{\|x\|_\infty}\right) \cdot \frac{\|x\|}{\|f(x)\|}.$$
> Now $\|f(x)\| = \|x \cdot \|x\|/\|x\|_\infty\| = (\|x\|/\|x\|_\infty) \cdot \|x\|$. So $\|x\|/\|f(x)\| = \|x\|/((\|x\|/\|x\|_\infty)\|x\|) = \|x\|_\infty/\|x\|$. Substituting:
> $$g(f(x)) = x \cdot \frac{\|x\|}{\|x\|_\infty} \cdot \frac{\|x\|_\infty}{\|x\|} = x.$$
>
> So $g \circ f = 1$ on $D^n \setminus \{0\}$, and also at $0$ (both map to $0$). So $g = f^{-1}$.
>
> Continuity of $g$: same argument as $f$. So $g$ is continuous.

**Step 5: Conclude $f$ is a homeomorphism.**

$f$ is continuous, bijective ($g$ is its inverse), and $f^{-1} = g$ is continuous. So $f$ is a homeomorphism $D^n \to [-1, 1]^n$.

> [!note]- Complete formal solution
> Define $f : D^n \to [-1, 1]^n$ by $f(x) = x \cdot \|x\| / \|x\|_\infty$ for $x \neq 0$, $f(0) = 0$. Then $\|f(x)\|_\infty = \|x\|$, so $f$ maps $D^n$ into $[-1, 1]^n$. Inverse $g(y) = y \cdot \|y\|_\infty / \|y\|$ for $y \neq 0$, $g(0) = 0$. Direct computation shows $g \circ f = 1$, $f \circ g = 1$. Both continuous (continuous on the punctured domain by composition of continuous functions; continuous at $0$ by the norm bound $\|f(x)\|_\infty = \|x\|$ and analogously $\|g(y)\| = \|y\|_\infty$). Hence $f$ is a homeomorphism. $\blacksquare$
>
> Alternative high-level: by [[Thm - Compact Convex Body is Homeomorphic to a Disk]], both $D^n$ and $[-1, 1]^n$ are homeomorphic to the standard $D^n$, hence to each other. The explicit construction above is one realization.

---

# Key Takeaways

**Radial homeomorphism via norm-swapping.** The key trick is to *swap norms*: the homeomorphism $f$ replaces the Euclidean norm $\|x\|$ with the sup-norm $\|x\|_\infty$ (or vice versa) on each ray from the origin. The structure: each ray exits the convex body at a unique boundary point, and the homeomorphism is the unique radial map preserving the rays but changing the boundary parametrization.

**Norms on $\mathbb{R}^n$ all give homeomorphic unit balls.** The unit balls of any two norms on $\mathbb{R}^n$ are homeomorphic (by the same radial-swapping trick). In fact, more is true: the norms themselves are *equivalent* (each is a constant multiple of the other up to a bounded factor) in finite dimensions, by an explicit compactness argument. So the choice of norm doesn't matter for finite-dimensional topology.

**The cube doesn't have rotational symmetry — but it's still topologically a ball.** $D^n$ has the symmetry group $\operatorname{O}(n)$ (all rotations and reflections); the cube has only the finite symmetry group $S_n \wr \mathbb{Z}/2\mathbb{Z}$ (signed permutations of coordinates). Topologically, this symmetry difference doesn't matter — both are $D^n$. The "shape" (corners, edges) is a geometric/differential property, not a topological one.

**The corner singularities are topologically trivial.** A cube has $2^n$ "corner" points (the vertices) where the boundary is non-smooth. These are not topological obstructions: the homeomorphism $f$ "smooths out" the corners — each ray from $0$ to a corner passes through a smooth interior, and the homeomorphism is continuous through these corners. The cube's boundary is a topological $(n-1)$-sphere even though it's not a smooth one. This is the topological analogue of: a polytope's vertices are topologically smooth (despite being geometrically singular).
