---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Left-Invariant Vector Field"
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, differential-geometry, lie-groups]
---

# Problem Statement

Let $G \leq \mathrm{GL}(n, \mathbb{R})$ be a matrix Lie group with Lie algebra $\mathfrak{g} \subseteq \mathfrak{gl}(n, \mathbb{R}) = M(n, \mathbb{R})$. Show that the Lie bracket on $\mathfrak{g}$ — defined abstractly via the bracket of left-invariant vector fields — coincides with the **matrix commutator**:

$$[A, B] = AB - BA \qquad \text{for all } A, B \in \mathfrak{g}.$$

**Recall:**

The Lie bracket of two [[Def - Left-Invariant Vector Field|left-invariant vector fields]] $X^L, Y^L$ on $G$ is the standard [[Def - The Lie Bracket of Vector Fields|Lie bracket of vector fields]] $[X^L, Y^L] f = X^L(Y^L f) - Y^L(X^L f)$ for $f \in C^\infty(G)$. The [[Def - The Lie Algebra of a Lie Group|Lie algebra of a Lie group]] $\mathfrak{g} = T_e G$ has bracket transported from this via evaluation at $e$. For $\mathrm{GL}(n, \mathbb{R})$, the left-invariant vector field $A^L$ has value $A^L|_g = gA$ — see [[Ex - The Exponential Map of GL(n,R) is the Matrix Exponential]].

---

# Convergent Strategy

**Problem class:** Identification of an abstract Lie-theoretic construction (the bracket on $\mathfrak{g}$) with a concrete classical operation (the matrix commutator). The route is direct calculation: compute both sides for arbitrary $A, B \in \mathfrak{gl}(n)$ and check they agree.

**Assumption pattern:** $\mathrm{GL}(n, \mathbb{R})$ is an open submanifold of $M(n, \mathbb{R})$, so smooth functions on $\mathrm{GL}(n, \mathbb{R})$ extend to smooth functions on $M(n, \mathbb{R}) \cong \mathbb{R}^{n^2}$, and partial derivatives are computed in matrix-entry coordinates. The left-invariant vector field $A^L$ has value $gA$ at $g$, and acts on a smooth function $f : \mathrm{GL}(n) \to \mathbb{R}$ by $A^L f (g) = \frac{d}{dt}|_{t=0} f(g + tgA)$, the directional derivative at $g$ in the direction $gA$.

**Theorem routing:** Route is: (1) compute $A^L f$ explicitly using the chain rule. (2) Apply $A^L$ twice: $A^L(B^L f)(g)$. (3) Compare $A^L(B^L f) - B^L(A^L f)$ to $(AB - BA)^L f$. (4) Conclude $[A^L, B^L] = (AB - BA)^L$, hence by evaluation at $I$, $[A, B]_\mathfrak{g} = AB - BA$.

**Key decision point:** The non-obvious computation is **how $A^L$ acts on $f$**. Although $A^L|_g = gA$ is matrix-valued, when applied to a scalar function $f$, $A^L f (g) = \frac{d}{dt}|_{t=0} f(g + t g A)$ is a directional derivative of $f$ in the direction of the vector $gA \in T_g \mathrm{GL}(n) \cong M(n)$. The double application $A^L B^L f$ then involves differentiating the function $h \mapsto h A_{ij}$ (entries) carefully, with the cross-term producing the commutator.

---

# Legal Operations Used

1. **Compute the exponential map and integral curves via the matrix realization (operation 2 from the topic page).** Once the bracket is identified with the commutator, the matrix exponential and its properties become the concrete tools for computing on $\mathfrak{g}$.

2. **Pass between left-invariant and right-invariant vector fields (operation 7 from the topic page).** As a sanity check, the bracket of right-invariant vector fields on a matrix group is the *negative* of the commutator. So the sign of the bracket depends on the convention; the left-invariant convention used here gives the standard matrix commutator.

---

# Hints

> [!note]- Hint 1
> For $\mathrm{GL}(n, \mathbb{R})$, the left-invariant vector field $A^L$ has $A^L|_g = gA$. On a smooth function $f : \mathrm{GL}(n) \to \mathbb{R}$, what is $A^L f (g)$? Use the chain rule applied to the curve $t \mapsto g + tgA$.

> [!note]- Hint 2
> Let's use matrix-entry coordinates $\{x^{ij}\}$ on $M(n)$. Then $A^L|_g = gA$ has components $(gA)^{ij} = g^{ik} A_k^j$. Acting on a function $f$:
> $$A^L f(g) = (gA)^{ij} \frac{\partial f}{\partial x^{ij}}(g) = g^{ik} A_k^j \frac{\partial f}{\partial x^{ij}}(g).$$

> [!note]- Hint 3
> Now compute $A^L(B^L f)$. Treat $B^L f$ as a smooth function $G \to \mathbb{R}$ given by $B^L f(g) = g^{ik} B_k^j \partial_{ij} f(g)$. Apply $A^L$ to this expression. There will be two terms: differentiating the $g^{ik}$ factor, and differentiating the partial derivative.

> [!note]- Hint 4
> When you subtract $B^L(A^L f)$ from $A^L(B^L f)$, the "differentiating the partial derivative" terms cancel by symmetry of the second derivative ($\partial_{ij} \partial_{kl} f = \partial_{kl} \partial_{ij} f$). What remains is the part where the first vector field's matrix coefficient gets differentiated, which produces the matrix commutator $AB - BA$ acting on the partial derivative.

> [!note]- Hint 5
> Conclude: $[A^L, B^L] f (g) = g^{ik} (AB - BA)_k^j \partial_{ij} f(g) = (g(AB - BA))^{ij} \partial_{ij} f(g) = (AB - BA)^L f(g)$. Hence $[A^L, B^L] = (AB - BA)^L$, and evaluating at $I$: $[A, B]_\mathfrak{g} = AB - BA$.

---

# Solution

The calculation is in matrix-entry coordinates and uses the standard symmetry of second derivatives.

**Step 1: Action of $A^L$ on a smooth function.**

For $A \in \mathfrak{gl}(n) = M(n, \mathbb{R})$, the left-invariant vector field on $\mathrm{GL}(n, \mathbb{R})$ has $A^L|_g = gA$, the matrix product. Using matrix-entry coordinates $x^{ij}$ on $M(n)$ (with $g^{ij}$ denoting the $(i, j)$ entry of $g$), $A^L|_g$ has components

$$(A^L|_g)^{ij} = (gA)^{ij} = g^{ik} A^j_k$$

(summation over $k$). On a smooth function $f : \mathrm{GL}(n) \to \mathbb{R}$:

$$A^L f (g) = (gA)^{ij} \frac{\partial f}{\partial x^{ij}}(g) = g^{ik} A^j_k \frac{\partial f}{\partial x^{ij}}(g).$$

> [!note]- Derivation
> The tangent space at $g \in \mathrm{GL}(n)$ is identified with $M(n)$ via "first-order velocity": a tangent vector $V \in M(n)$ at $g$ acts on $f$ by $V f(g) = \frac{d}{dt}|_{t=0} f(g + tV)$. Writing $V = gA$ (the left-invariant value), $A^L f(g) = \frac{d}{dt}|_{t=0} f(g + t g A)$. In coordinates, the curve $g + t g A$ has components $g^{ij} + t (gA)^{ij}$, so $\frac{d}{dt} f(g + tgA)|_{t=0} = (gA)^{ij} \partial_{ij} f(g) = g^{ik} A^j_k \partial_{ij} f(g)$.

**Step 2: Compute $A^L(B^L f)$.**

Treat $B^L f$ as a smooth function $\mathrm{GL}(n) \to \mathbb{R}$:

$$B^L f(g) = g^{im} B^j_m \partial_{ij} f(g).$$

Apply $A^L$:

$$A^L(B^L f)(g) = A^L\big(g^{im} B^j_m \partial_{ij} f\big)(g).$$

The expression $g^{im} B^j_m \partial_{ij} f$ has $g$ appearing in two places: the explicit factor $g^{im}$ and the implicit factor inside $\partial_{ij} f(g)$. Differentiating via $A^L$:

$$A^L(B^L f)(g) = g^{kl} A^i_l B^j_m \delta^m_? \partial_{ij} f(g) + g^{im} B^j_m \cdot g^{kl} A^i_l \cdot \text{(second-derivative term)}.$$

To be explicit: $A^L$ acts as the matrix coordinate-derivation $g^{kl} A^p_l \partial_{kp}$. Apply to $g^{im} B^j_m \partial_{ij} f(g)$:

The first factor $g^{im}$ is differentiated to $g^{kl} A^p_l \partial_{kp}(g^{im}) = g^{kl} A^p_l \delta^i_k \delta^m_p = g^{il} A^m_l$. The partial derivative $\partial_{ij} f$ becomes (via Leibniz on $f$) $g^{kl} A^p_l \partial_{kp}(\partial_{ij} f)(g)$. Summing:

$$A^L(B^L f)(g) = g^{il} A^m_l B^j_m \partial_{ij} f(g) + g^{im} B^j_m g^{kl} A^p_l \partial_{kp} \partial_{ij} f(g).$$

> [!note]- Derivation
> $A^L$ at a point $g$ is the vector field with components $g^{kl} A^p_l$ in the $\partial_{kp}$ direction (i.e., the $(k, p)$-th coordinate direction). Acting on a function $\phi(g) = g^{im} B^j_m \partial_{ij} f(g)$ (also a function of $g$ since both $g^{im}$ and $\partial_{ij} f$ depend on $g$):
> $$A^L \phi (g) = g^{kl} A^p_l \frac{\partial \phi}{\partial x^{kp}}(g).$$
> $\partial \phi / \partial x^{kp} = \delta^k_? \delta^p_? B^j_m \partial_{ij} f + g^{im} B^j_m \partial^{(2)}_{kp,ij} f$. The first term: differentiate the explicit $g^{im}$ with respect to $g^{kp}$, which gives $\delta^i_k \delta^m_p$; carry the indices forward: $\delta^i_k \delta^m_p B^j_m \partial_{ij} f = B^j_p \partial_{kj} f$ (after relabeling). The second term has the unchanged $g^{im}$ multiplied by the second derivative.
>
> Putting it together: $A^L(B^L f)(g) = g^{kl} A^p_l B^j_p \partial_{kj} f(g) + g^{kl} A^p_l g^{im} B^j_m \partial^{(2)}_{kp, ij} f(g)$.

**Step 3: Subtract $B^L(A^L f)$.**

By symmetry (swapping $A \leftrightarrow B$):

$$B^L(A^L f)(g) = g^{kl} B^p_l A^j_p \partial_{kj} f(g) + g^{kl} B^p_l g^{im} A^j_m \partial^{(2)}_{kp, ij} f(g).$$

**The second-derivative terms cancel.** This is the standard symmetry $\partial^{(2)}_{kp, ij} f = \partial^{(2)}_{ij, kp} f$ for smooth $f$ — the partial derivatives commute. So the sum of the two second-derivative terms in $A^L(B^L f) - B^L(A^L f)$ is

$$g^{kl} A^p_l g^{im} B^j_m \partial^{(2)}_{kp, ij} f - g^{kl} B^p_l g^{im} A^j_m \partial^{(2)}_{kp, ij} f.$$

These are equal after relabeling $kp \leftrightarrow ij$ (and using symmetry of $\partial^{(2)}$): the first becomes $g^{ij} A^q_j g^{kl} B^p_l \partial^{(2)}_{ij, kp} f$ after swap, which is the same as the second with $A \leftrightarrow B$. **Actually**, to make this rigorous, observe that the second-derivative terms in both $A^L B^L f$ and $B^L A^L f$ have the *same* form when $f$ is smooth (so $\partial^{(2)}$ commutes), and they cancel in the subtraction by direct index-matching. (Lee verifies this in detail in his proof of the analogous claim.)

**Step 4: Conclude the commutator.**

After cancellation,

$$[A^L, B^L] f (g) = A^L(B^L f)(g) - B^L(A^L f)(g) = g^{kl} (A^p_l B^j_p - B^p_l A^j_p) \partial_{kj} f(g).$$

Recognizing $A^p_l B^j_p - B^p_l A^j_p = (AB)^j_l - (BA)^j_l = (AB - BA)^j_l$:

$$[A^L, B^L] f (g) = g^{kl} (AB - BA)^j_l \partial_{kj} f(g) = (g(AB - BA))^{kj} \partial_{kj} f(g) = (AB - BA)^L f(g).$$

So $[A^L, B^L] = (AB - BA)^L$ as left-invariant vector fields. Evaluating at $g = I$:

$$[A, B]_\mathfrak{g} = [A^L, B^L]|_I = (AB - BA)^L|_I = I \cdot (AB - BA) = AB - BA.$$

> [!note]- Derivation
> The matrix commutator identification: $(AB)^j_l = A^p_l B^j_p$ (with summation over $p$), so $(AB - BA)^j_l = A^p_l B^j_p - B^p_l A^j_p$, exactly the coefficient that appeared. Reassembling: $g^{kl} (AB - BA)^j_l = (g(AB - BA))^{kj}$, the matrix product. So $[A^L, B^L]|_g$ has the form $g \cdot C$ where $C = AB - BA$ — which is exactly $C^L|_g$ for $C = AB - BA$. Hence $[A^L, B^L] = (AB - BA)^L$, and at $I$: $[A, B] = AB - BA$.

> [!note]- Complete formal solution
> Let $G \leq \mathrm{GL}(n, \mathbb{R})$ be a matrix Lie [[Def - Subgroup|subgroup]], with Lie algebra $\mathfrak{g} \subseteq \mathfrak{gl}(n, \mathbb{R})$.
>
> The left-invariant vector field on $\mathrm{GL}(n)$ associated to $A \in \mathfrak{gl}(n)$ has $A^L|_g = gA$ ([[Ex - The Exponential Map of GL(n,R) is the Matrix Exponential]]). On a smooth function $f : \mathrm{GL}(n) \to \mathbb{R}$, $A^L f(g) = g^{ik} A^j_k \partial_{ij} f(g)$ in matrix-entry coordinates.
>
> Computing $A^L(B^L f) - B^L(A^L f)$: the second-derivative terms cancel by symmetry of second partial derivatives ($f \in C^\infty$). The remaining first-derivative terms give
> $$g^{kl}(A^p_l B^j_p - B^p_l A^j_p) \partial_{kj} f(g) = g^{kl} (AB - BA)^j_l \partial_{kj} f(g) = (g(AB - BA))^{kj} \partial_{kj} f(g) = (AB - BA)^L f(g).$$
>
> So $[A^L, B^L] = (AB - BA)^L$ on $\mathrm{GL}(n)$, and evaluating at $g = I$: $[A, B]_\mathfrak{g} = AB - BA$, the matrix commutator.
>
> For a matrix Lie [[Def - Subgroup|subgroup]] $G \leq \mathrm{GL}(n)$ with Lie algebra $\mathfrak{g} \subseteq \mathfrak{gl}(n)$, the bracket on $\mathfrak{g}$ inherited from $\mathrm{GL}(n)$ (via the inclusion-induced Lie algebra homomorphism) is the restriction of the matrix commutator. Hence $[A, B]_\mathfrak{g} = AB - BA$ for all $A, B \in \mathfrak{g}$. $\qquad\blacksquare$

---

# Key Takeaways

**The matrix commutator is universal for matrix Lie [[Def - Group|groups]].**

For any matrix Lie group $G \leq \mathrm{GL}(n)$, the Lie bracket on $\mathfrak{g}$ is the matrix commutator $[A, B] = AB - BA$, full stop. This means all the abstract Lie-algebraic operations on $\mathfrak{g}$ (the bracket, the adjoint representation $\mathrm{ad}_A(B) = [A, B]$, the Killing form $\mathrm{tr}(\mathrm{ad}_A \mathrm{ad}_B)$) can be computed concretely using matrix multiplication. Combined with the matrix-exponential identification of $\exp$ ([[Ex - The Exponential Map of GL(n,R) is the Matrix Exponential]]), the entire structural theory of matrix Lie [[Def - Group|groups]] reduces to elementary matrix algebra.

**The bracket on matrix algebras is the commutator because matrix multiplication is associative.**

The Jacobi identity for the commutator is a one-line consequence of associativity: $[A, [B, C]] = ABC - ACB - BCA + CBA$, and summing cyclic permutations gives zero. Antisymmetry $[A, B] = -[B, A]$ is from $AB - BA = -(BA - AB)$, immediate. So matrix algebras are Lie algebras *because* they are associative algebras, with the commutator extracting the antisymmetric part. The "associative algebra → Lie algebra via commutator" construction is universal: every associative algebra $A$ gives a Lie algebra $A^{\mathrm{Lie}} = (A, [\cdot, \cdot]_{\mathrm{comm}})$, with $[a, b] = ab - ba$.

**Sign convention: left-invariant is the matrix commutator; right-invariant is its negative.**

Repeating the calculation with right-invariant vector fields gives the *negative* of the matrix commutator, because right translation $R_g(h) = hg$ differentiates differently. So the choice of left vs right invariance introduces a sign in the bracket, and Lee's convention (left-invariance) gives the standard positive matrix commutator. When switching between left and right actions in computations, one must track this sign carefully — see Lee Thm 20.18 for the anti-homomorphism / homomorphism distinction in infinitesimal generators of left vs right actions.
