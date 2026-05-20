---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Deformation Retract"
  - "Def - Homotopy Equivalence and Contractible Space"
  - "Def - Homotopy"
tags: [analysis, topology, homotopy, deformation-retract]
---

# Problem Statement

Show that $S^{n-1} = \{x \in \mathbb{R}^n : \|x\| = 1\}$ is a strong deformation retract of $\mathbb{R}^n \setminus \{0\}$. Consequently, $\mathbb{R}^n \setminus \{0\} \simeq S^{n-1}$ (homotopy equivalence).

**Recall:**

A subset $A \subseteq X$ is a [[Def - Deformation Retract|strong deformation retract]] of $X$ if there is a homotopy $F : X \times I \to X$ with: $F(x, 0) = x$; $F(x, 1) \in A$; and $F(a, t) = a$ for all $a \in A$ and $t \in I$. So $A$ is fixed throughout the homotopy.

A strong deformation retract gives a homotopy equivalence: $A \simeq X$.

---

# Convergent Strategy

**Problem class:** Construct a strong deformation retract from punctured Euclidean space to the unit sphere.

**Assumption pattern:** $\mathbb{R}^n \setminus \{0\}$ has the property that every point has a well-defined "radial projection" to the sphere, namely $x \mapsto x/\|x\|$. The homotopy "slides" each point along its ray toward the unit-norm point.

**Theorem routing:** Construct the explicit homotopy $F(x, t) = (1-t)x + t \cdot x/\|x\|$. Verify: continuity, endpoint values, and that $F$ fixes $S^{n-1}$ throughout.

**Key decision point:** The "radial scaling" homotopy. At $t = 0$, $F$ is the identity; at $t = 1$, $F$ sends every $x$ to $x/\|x\| \in S^{n-1}$. For $x \in S^{n-1}$, both endpoints equal $x$, and so does every intermediate value (since $x = x/\|x\|$ when $\|x\| = 1$).

---

# Legal Operations Used

1. **Construct a homotopy by radial interpolation.** The homotopy interpolates linearly between the identity and the radial projection — both are continuous, and the interpolation stays in $\mathbb{R}^n \setminus \{0\}$.

2. **Verify the strong deformation retract conditions.** Three conditions: $F(\cdot, 0) = 1_X$, $F(\cdot, 1) \in A$, $F(a, t) = a$ for $a \in A$, $t \in I$.

---

# Hints

> [!note]- Hint 1
> Combine the identity $x$ and the radial projection $x/\|x\|$ via linear interpolation: $F(x, t) = (1-t)x + t(x/\|x\|)$. Both endpoints are well-defined on $\mathbb{R}^n \setminus \{0\}$.

> [!note]- Hint 2
> Verify that $F(x, t)$ never reaches $0$. $F(x, t) = x \cdot ((1-t) + t/\|x\|) = x \cdot \lambda(t, \|x\|)$ where $\lambda$ is a scalar. The scalar is $(1-t) + t/\|x\| > 0$ for all $t \in I$ and $\|x\| > 0$ (both terms nonneg, both can be 0 only if $t = 0, \|x\| = \infty$ — impossible, or $t = 1, \|x\| = \infty$, also impossible).

> [!note]- Hint 3
> For $x \in S^{n-1}$: $\|x\| = 1$, so $F(x, t) = (1-t)x + tx = x$. So $S^{n-1}$ is fixed throughout — strong deformation retract.

---

# Solution

The proof breaks into six steps that build and verify the radial-projection homotopy. Step 1 defines $F(x, t) = (1-t)x + t(x/\|x\|)$; Step 2 verifies the image stays in $\mathbb{R}^n \setminus \{0\}$ by writing $F(x, t) = \lambda x$ with $\lambda > 0$; Step 3 checks continuity (continuity of the norm on $\mathbb{R}^n \setminus \{0\}$); Step 4 confirms the endpoint conditions $F(x, 0) = x$ and $F(x, 1) = x/\|x\| \in S^{n-1}$; Step 5 verifies $S^{n-1}$ is fixed throughout (since $x/\|x\| = x$ when $\|x\| = 1$); Step 6 concludes. The non-obvious move is in Step 2 — checking that the interpolation never hits the origin, because if either endpoint were lost the deformation would fail.

**Step 1: Define the deformation homotopy.**

For $x \in \mathbb{R}^n \setminus \{0\}$ and $t \in I$, set
$$F(x, t) := (1 - t) x + t \cdot \frac{x}{\|x\|}.$$

**Step 2: Verify $F$ takes values in $\mathbb{R}^n \setminus \{0\}$.**

> [!note]- Derivation
> $F(x, t) = x \cdot \left((1-t) + \frac{t}{\|x\|}\right)$. The scalar factor is $\lambda := (1-t) + t/\|x\|$. We have $1 - t \geq 0$ (since $t \in [0, 1]$) and $t/\|x\| \geq 0$ (since $t \geq 0$ and $\|x\| > 0$). Both are zero only if simultaneously $t = 1$ and $t = 0$ — impossible. So $\lambda > 0$. Hence $F(x, t) = \lambda \cdot x \neq 0$.

**Step 3: Verify continuity.**

> [!note]- Derivation
> Each component of $F$ is $(1-t)x_i + tx_i/\|x\|$. The norm $\|x\| = \sqrt{x_1^2 + \dots + x_n^2}$ is continuous on $\mathbb{R}^n \setminus \{0\}$ (composition of polynomial with square root, neither vanishing). So $x_i/\|x\|$ is continuous on $\mathbb{R}^n \setminus \{0\}$, and the whole expression is a polynomial in continuous functions and $t$. Continuous.

**Step 4: Verify endpoint conditions.**

> [!note]- Derivation
> $F(x, 0) = 1 \cdot x + 0 = x$. So $F(\cdot, 0) = 1_{\mathbb{R}^n \setminus \{0\}}$.
>
> $F(x, 1) = 0 \cdot x + 1 \cdot (x/\|x\|) = x/\|x\| \in S^{n-1}$. So $F(\cdot, 1) : \mathbb{R}^n \setminus \{0\} \to S^{n-1}$, the radial projection.

**Step 5: Verify $S^{n-1}$ is fixed throughout.**

> [!note]- Derivation
> For $x \in S^{n-1}$: $\|x\| = 1$, so $x/\|x\| = x$. Then $F(x, t) = (1-t)x + tx = x$ for all $t$.

**Step 6: Conclude $S^{n-1}$ is a strong deformation retract of $\mathbb{R}^n \setminus \{0\}$.**

By Steps 2–5, $F$ satisfies all conditions for a strong deformation retract:

- $F : (\mathbb{R}^n \setminus \{0\}) \times I \to \mathbb{R}^n \setminus \{0\}$ continuous;
- $F(x, 0) = x$;
- $F(x, 1) \in S^{n-1}$;
- $F(a, t) = a$ for $a \in S^{n-1}$, $t \in I$.

By [[Def - Deformation Retract]], $S^{n-1}$ is a strong deformation retract of $\mathbb{R}^n \setminus \{0\}$. Hence $\mathbb{R}^n \setminus \{0\} \simeq S^{n-1}$.

> [!note]- Complete formal solution
> Define $F(x, t) := (1-t)x + t \cdot (x/\|x\|)$. The codomain is in $\mathbb{R}^n \setminus \{0\}$ because $F(x, t) = \lambda x$ with $\lambda = (1-t) + t/\|x\| > 0$. Continuity follows from continuity of polynomials and of the norm on $\mathbb{R}^n \setminus \{0\}$. $F(x, 0) = x$ and $F(x, 1) = x/\|x\|$. For $x \in S^{n-1}$: $\|x\| = 1$ gives $F(x, t) = x$ for all $t$. Hence $S^{n-1}$ is a strong deformation retract of $\mathbb{R}^n \setminus \{0\}$. $\blacksquare$

---

# Key Takeaways

**Radial projection is the natural deformation in punctured Euclidean space.** Whenever you have a space "with a hole at the origin" — or more generally, a space with a clear "center" — the radial projection toward the unit-norm boundary is the natural deformation. The trigger-reaction pattern: "see a punctured Euclidean space, or an annulus, or a punctured disk $\Rightarrow$ deformation retract onto the boundary or central circle via radial projection".

**The continuity of $x \mapsto x/\|x\|$ depends on excluding $0$.** The map $x \mapsto x/\|x\|$ is *only* continuous on $\mathbb{R}^n \setminus \{0\}$; at the origin, it has no continuous extension (different directions of approach give different limits). This is why we must exclude $\{0\}$ from the source — including it would make the radial projection discontinuous.

**Homotopy invariance of fundamental groups.** Once $S^{n-1} \simeq \mathbb{R}^n \setminus \{0\}$, all homotopy invariants agree: $\pi_k(S^{n-1}) = \pi_k(\mathbb{R}^n \setminus \{0\})$ for every $k$. For $n = 2$: $\pi_1(\mathbb{R}^2 \setminus \{0\}) = \pi_1(S^1) = \mathbb{Z}$, the winding number. This is the topological foundation of the residue theorem in complex analysis.

**Generalization to a punctured convex body.** The same argument works for any convex body $C$ with a point $p$ in its interior removed: $C \setminus \{p\}$ deformation retracts to $\partial C$ via radial projection from $p$. The convexity ensures the segments from $p$ to $\partial C$ stay in $C$, and the deformation $F(x, t) = (1-t)x + t \cdot r_C(x)$ (where $r_C$ is the radial projection) works.
