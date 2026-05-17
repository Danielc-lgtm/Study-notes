---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Regular Value Theorem"
  - "Def - Submanifold of Euclidean Space"
  - "Def - The Tangent Space to a Submanifold"
  - "Def - Group"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

The **orthogonal group** is the set of length-preserving linear maps of $\mathbb{R}^n$:
$$O(n) = \{A \in \mathbb{R}^{n\times n} : A^T A = I\},$$
a subset of the space $\mathbb{R}^{n\times n} \cong \mathbb{R}^{n^2}$ of all $n\times n$ real matrices.

1. Prove that $O(n)$ is a smooth submanifold of $\mathbb{R}^{n\times n}$, by exhibiting it as a regular level set. The subtlety: the natural defining map $A \mapsto A^TA - I$ should be regarded as taking values in the space $\operatorname{Sym}(n)$ of **symmetric** matrices, not in all of $\mathbb{R}^{n\times n}$.
2. Compute the dimension of $O(n)$.
3. Show that the tangent space at the identity, $T_I O(n)$, is exactly the space of **skew-symmetric** matrices $\{H : H^T = -H\}$.

**Recall:**

The objects in play are the regular value theorem, the space of symmetric matrices, and the tangent space.

![[Thm - The Regular Value Theorem#Statement]]

By the [[Thm - The Regular Value Theorem|regular value theorem]], if $c$ is a regular value of $f \in C^k(U, \mathbb{R}^{n-d})$ — $Df_p$ surjective at every $p$ of $f^{-1}(c)$ — then $f^{-1}(c)$ is a $d$-dimensional [[Def - Submanifold of Euclidean Space|submanifold]] with [[Def - The Tangent Space to a Submanifold|tangent space]] $\ker Df_p$. The space $\operatorname{Sym}(n)$ of symmetric $n\times n$ matrices has dimension $\tfrac{n(n+1)}{2}$ (free entries on and above the diagonal); the space $\operatorname{Skew}(n)$ of skew-symmetric matrices ($H^T = -H$) has dimension $\tfrac{n(n-1)}{2}$. The orthogonal group is also a [[Def - Group|group]] under matrix multiplication — it is the prototype **Lie group**.

---

# Convergent Strategy

**Problem class.** This is a *manifold-structure* problem, of the hardest kind, because the naive application of the regular value theorem *fails* and must be repaired. The [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Problem-Solving Strategy|topic strategy]] route — write as a level set, check regularity — is correct, but the codomain must be chosen with care.

**Assumption pattern.** The defining equation $A^TA = I$ looks like $n^2$ scalar equations, one per matrix entry. But $A^TA$ is *always symmetric*, so the equation $A^TA - I = 0$ really only imposes $\tfrac{n(n+1)}{2}$ independent conditions — the symmetric ones. If one mistakenly takes the codomain to be all of $\mathbb{R}^{n^2}$, the derivative is *never* surjective and the regular value theorem cannot apply. The fix is to recognize the true codomain.

**Theorem routing.** Define $f : \mathbb{R}^{n\times n} \to \operatorname{Sym}(n)$ by $f(A) = A^TA - I$. Compute the derivative $Df_A(H) = A^TH + H^TA$. Show this is surjective onto $\operatorname{Sym}(n)$ at every $A \in O(n)$. The [[Thm - The Regular Value Theorem|regular value theorem]] then gives the manifold structure, with dimension $n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$ and $T_I O(n) = \ker Df_I$.

**Key decision point.** The entire difficulty — and the reason this is a three-star exercise — is the *choice of codomain*. Taking $f$ into $\operatorname{Sym}(n)$ rather than $\mathbb{R}^{n\times n}$ is the non-obvious move; it reflects that the constraint $A^TA = I$ is "automatically symmetric" and so really imposes fewer conditions than it appears to. Getting this right makes the derivative surjective; getting it wrong makes the problem unsolvable.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Check that a value is regular, then declare the level set a manifold.** Verify $Df_A$ is surjective onto $\operatorname{Sym}(n)$ at every $A \in O(n)$ and apply the regular value theorem.

2. **Identify the true codomain of a defining map.** Recognize that $A^TA - I$ is always symmetric, so $f$ maps into $\operatorname{Sym}(n)$; this corrects the dimension count and rescues surjectivity.

3. **Compute a tangent space as a kernel.** $T_I O(n) = \ker Df_I$, the matrices killed by the linearized constraint.

---

# Hints

> [!note]- Hint 1
> The map is $f(A) = A^TA - I$. First observe: for *any* $A$, the matrix $A^TA$ is symmetric ($(A^TA)^T = A^TA$). So $f(A)$ is always symmetric — the map's image lies in $\operatorname{Sym}(n)$, never escaping it. This is why the codomain *must* be taken to be $\operatorname{Sym}(n)$.

> [!note]- Hint 2
> Compute the derivative. $f(A + H) = (A+H)^T(A+H) - I = A^TA - I + A^TH + H^TA + H^TH$. The linear-in-$H$ part is $Df_A(H) = A^TH + H^TA$. Check this lands in $\operatorname{Sym}(n)$.

> [!note]- Hint 3
> Surjectivity at $A \in O(n)$: given any symmetric $S$, find $H$ with $A^TH + H^TA = S$. Try $H = \tfrac12 AS$. Then $A^TH = \tfrac12 A^TAS = \tfrac12 S$ (using $A^TA = I$), and $H^TA = \tfrac12 S^TA^TA = \tfrac12 S^T = \tfrac12 S$ (using $S$ symmetric and $A^TA = I$). Sum: $S$. ✓

> [!note]- Hint 4
> Dimension: $\dim O(n) = \dim\mathbb{R}^{n\times n} - \dim\operatorname{Sym}(n) = n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$. Tangent space at $I$: $T_I O(n) = \ker Df_I = \{H : Df_I(H) = 0\}$, and $Df_I(H) = I^TH + H^TI = H + H^T$. So $H + H^T = 0$ — skew-symmetric.

---

# Solution

The orthogonal group is a regular level set — but only once you see that its defining map lands in the *symmetric* matrices, not in all matrices. With the codomain corrected, the derivative is surjective by a one-line computation, the regular value theorem applies, and the dimension and tangent space follow.

**Step 1: The defining map lands in the symmetric matrices.**

The map $f(A) = A^TA - I$ takes values in $\operatorname{Sym}(n)$, the space of symmetric matrices, because $A^TA$ is symmetric for every $A$. So $O(n) = f^{-1}(0)$ with $f : \mathbb{R}^{n\times n} \to \operatorname{Sym}(n)$.

> [!note]- Derivation
> For any matrix $A$, $(A^TA)^T = A^T(A^T)^T = A^TA$, so $A^TA$ is symmetric; hence $f(A) = A^TA - I$ is symmetric ($I$ is symmetric). The image of $f$ never leaves the subspace $\operatorname{Sym}(n) \subseteq \mathbb{R}^{n\times n}$.
>
> This is the crux of the problem. If one carelessly regards $f$ as a map into all of $\mathbb{R}^{n\times n}$ (dimension $n^2$), then $f$ can *never* have surjective derivative — its image is trapped in the proper subspace $\operatorname{Sym}(n)$, so $Df_A$ can never surject onto $\mathbb{R}^{n\times n}$, and the [[Thm - The Regular Value Theorem|regular value theorem]] would never apply. The constraint $A^TA = I$ is "$n^2$ equations" only superficially; because $A^TA$ is automatically symmetric, the $(i,j)$ equation and the $(j,i)$ equation are *identical*, so there are really only $\tfrac{n(n+1)}{2}$ independent equations. The honest codomain is $\operatorname{Sym}(n)$, of dimension $\tfrac{n(n+1)}{2}$, and $f : \mathbb{R}^{n\times n} \to \operatorname{Sym}(n)$ is a smooth ($C^\infty$, being polynomial) map with $O(n) = f^{-1}(0)$.

**Step 2: $0$ is a regular value — the derivative is surjective onto $\operatorname{Sym}(n)$.**

The derivative is $Df_A(H) = A^TH + H^TA$, and at every $A \in O(n)$ it surjects onto $\operatorname{Sym}(n)$. Hence $0$ is a regular value, and by the regular value theorem $O(n)$ is a smooth submanifold of $\mathbb{R}^{n\times n}$.

> [!note]- Derivation
> Expand $f(A + H)$:
> $$f(A+H) = (A+H)^T(A+H) - I = A^TA - I + \underbrace{A^TH + H^TA}_{\text{linear in } H} + \underbrace{H^TH}_{O(|H|^2)}.$$
> So the derivative is the linear map $Df_A(H) = A^TH + H^TA$. Its output is symmetric: $(A^TH + H^TA)^T = H^TA + A^TH$, the same matrix — good, it lands in $\operatorname{Sym}(n)$ as it must.
>
> Now fix $A \in O(n)$, so $A^TA = I$. We show $Df_A : \mathbb{R}^{n\times n} \to \operatorname{Sym}(n)$ is *surjective*: given an arbitrary symmetric $S \in \operatorname{Sym}(n)$, we produce $H$ with $Df_A(H) = S$. Take
> $$H = \tfrac12 AS.$$
> Then, using $A^TA = I$ and $S^T = S$:
> $$A^TH = A^T\cdot\tfrac12 AS = \tfrac12(A^TA)S = \tfrac12 S, \qquad H^TA = (\tfrac12 AS)^TA = \tfrac12 S^TA^TA = \tfrac12 S^T = \tfrac12 S.$$
> Therefore $Df_A(H) = A^TH + H^TA = \tfrac12 S + \tfrac12 S = S$. Since $S$ was an arbitrary symmetric matrix, $Df_A$ surjects onto $\operatorname{Sym}(n)$.
>
> This holds at *every* $A \in O(n)$, so $0$ is a **regular value** of $f$. By the [[Thm - The Regular Value Theorem|regular value theorem]], $O(n) = f^{-1}(0)$ is a $C^\infty$ submanifold of $\mathbb{R}^{n\times n}$.

**Step 3: The dimension is $\tfrac{n(n-1)}{2}$.**

$$\dim O(n) = \dim\mathbb{R}^{n\times n} - \dim\operatorname{Sym}(n) = n^2 - \frac{n(n+1)}{2} = \frac{n(n-1)}{2}.$$

> [!note]- Derivation
> The regular value theorem gives $\dim f^{-1}(0) = \dim(\text{domain}) - \dim(\text{codomain})$. The domain $\mathbb{R}^{n\times n}$ has dimension $n^2$. The codomain $\operatorname{Sym}(n)$ has dimension $\tfrac{n(n+1)}{2}$ — a symmetric matrix is freely determined by its entries on and above the diagonal, of which there are $n + (n-1) + \dots + 1 = \tfrac{n(n+1)}{2}$. Hence
> $$\dim O(n) = n^2 - \tfrac{n(n+1)}{2} = \tfrac{2n^2 - n^2 - n}{2} = \tfrac{n^2 - n}{2} = \tfrac{n(n-1)}{2}.$$
> For $n = 2$ this is $1$ (the circle of rotation angles, with reflections); for $n = 3$ it is $3$ (the three-dimensional rotation group); in general $\tfrac{n(n-1)}{2}$ is the number of independent planes of rotation. *(Had one wrongly used codomain $\mathbb{R}^{n^2}$, the formula would give $n^2 - n^2 = 0$ — absurd, since $O(n)$ is not a discrete set. The corrected codomain is what makes the dimension come out right.)*

**Step 4: The tangent space at the identity is the skew-symmetric matrices.**

$$T_I O(n) = \ker Df_I = \{H \in \mathbb{R}^{n\times n} : H^T = -H\} = \operatorname{Skew}(n).$$

> [!note]- Derivation
> By the [[Thm - The Regular Value Theorem|regular value theorem]], the tangent space at any $A \in O(n)$ is $\ker Df_A$. At the identity $A = I$:
> $$Df_I(H) = I^TH + H^TI = H + H^T.$$
> So
> $$T_I O(n) = \ker Df_I = \{H : H + H^T = 0\} = \{H : H^T = -H\},$$
> exactly the **skew-symmetric** matrices. This space has dimension $\tfrac{n(n-1)}{2}$ — a skew-symmetric matrix has zero diagonal and is determined by its entries strictly above the diagonal, of which there are $\tfrac{n(n-1)}{2}$ — consistent with $\dim O(n)$, as it must be.
>
> The picture: a curve $A(t)$ of orthogonal matrices through $A(0) = I$ satisfies $A(t)^TA(t) = I$; differentiating at $t = 0$ gives $A'(0)^T + A'(0) = 0$, so the velocity $A'(0)$ is skew-symmetric. The skew-symmetric matrices are the *infinitesimal rotations*. With the commutator bracket $[H, K] = HK - KH$, this tangent space is the **Lie algebra** $\mathfrak{so}(n)$ of the Lie group $O(n)$.

> [!note]- Complete formal solution
> *Codomain.* For any $A$, $A^TA$ is symmetric, so $f(A) = A^TA - I$ defines a $C^\infty$ map $f : \mathbb{R}^{n\times n} \to \operatorname{Sym}(n)$ with $O(n) = f^{-1}(0)$.
>
> *Regularity.* $Df_A(H) = A^TH + H^TA$. For $A \in O(n)$ and any symmetric $S$, set $H = \tfrac12 AS$; then $A^TH = \tfrac12 S$ and $H^TA = \tfrac12 S^T = \tfrac12 S$, so $Df_A(H) = S$. Thus $Df_A$ surjects onto $\operatorname{Sym}(n)$ at every $A \in O(n)$, so $0$ is a regular value. By the [[Thm - The Regular Value Theorem|regular value theorem]], $O(n)$ is a $C^\infty$ submanifold.
>
> *Dimension.* $\dim O(n) = n^2 - \dim\operatorname{Sym}(n) = n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$.
>
> *Tangent space at $I$.* $Df_I(H) = H + H^T$, so $T_I O(n) = \ker Df_I = \{H : H^T = -H\} = \operatorname{Skew}(n)$, dimension $\tfrac{n(n-1)}{2}$. $\blacksquare$

---

# Key Takeaways

**The choice of codomain is part of applying the regular value theorem, and getting it wrong makes the theorem inapplicable.** The defining equation $A^TA = I$ *appears* to be $n^2$ scalar equations, but $A^TA$ is always symmetric, so the equation only ever imposes the $\tfrac{n(n+1)}{2}$ symmetric conditions — the sub-diagonal equations duplicate the super-diagonal ones. If the codomain is taken to be all of $\mathbb{R}^{n^2}$, the map's image is trapped in a proper subspace and its derivative can never be surjective; the regular value theorem cannot even be stated. The fix — and the heart of the exercise — is to recognize the *true codomain*: the smallest space the map's image actually lives in. The general principle: before checking regularity, ask where the defining map *genuinely* lands, and whether structural identities (symmetry, tracelessness, antisymmetry) confine it to a subspace. The same care makes $\operatorname{SL}_n$ (codomain $\mathbb{R}$, the trace-free constraint) and $\operatorname{SU}(n)$ work.

**The dimension of a regular level set is "ambient dimension minus number of *independent* equations", and independence is the subtle word.** Here the count is $n^2 - \tfrac{n(n+1)}{2} = \tfrac{n(n-1)}{2}$, and it comes out right *only* because the codomain dimension $\tfrac{n(n+1)}{2}$ correctly reflects the number of independent constraints. Counting the equations naively as $n^2$ gives dimension $0$, which is absurd — $O(n)$ visibly contains continuous families of rotations. The lesson generalizes: whenever you count the dimension of a constrained set, the constraints must be counted *with their dependencies removed*, and the regular value theorem automates this by making you identify the genuine codomain.

**The tangent space at the identity of a matrix group is its Lie algebra, computed by linearizing the defining equation.** Differentiating the constraint $A^TA = I$ at the identity gives $H + H^T = 0$ — the skew-symmetric matrices. This is a completely general recipe: the tangent space at the identity of any matrix Lie group is found by linearizing its defining equation, and the result, with the commutator bracket, is the **Lie algebra**. The orthogonal group's algebra is $\mathfrak{so}(n)$, the skew-symmetric matrices, the "infinitesimal rotations". This single computation — $A^TA = I$ linearizes to $H + H^T = 0$ — is the prototype of the entire Lie group / Lie algebra correspondence, and it shows how the geometry of [[Thm - The Regular Value Theorem|the regular value theorem]] meets the algebra of [[Def - Group|groups]].

**A set that is both a group and a submanifold is a Lie group, and such objects pervade physics.** $O(n)$ is simultaneously a [[Def - Group|group]] (closed under matrix multiplication and inversion) and, by this exercise, a smooth submanifold — a *Lie group*. The defining equation $A^TA = I$ is "$A$ preserves the Euclidean inner product", and replacing the Euclidean inner product with the *Minkowski* one gives, by the *identical* regular-value computation, the Lorentz group of **special relativity** — a $6$-dimensional manifold whose tangent space at the identity is spanned by the infinitesimal boosts and rotations. The trigger to recognize: a set defined by a *quadratic matrix equation* of the form "preserves a bilinear form" is, generically, a Lie group, and the regular value theorem with the symmetric-codomain correction is the tool that proves it.
