---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Adjoint Representation"
  - "Def - The Lie Algebra of a Lie Group"
  - "Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices"
tags: [geometry, differential-geometry, lie-groups]
---

# Problem Statement

Compute the [[Def - Adjoint Representation|adjoint representation]] $\mathrm{Ad} : \mathrm{SO}(3) \to \mathrm{GL}(\mathfrak{so}(3))$ of the rotation group on its Lie algebra explicitly. Show that under the identification $\mathfrak{so}(3) \cong \mathbb{R}^3$ via the [[Ex - The Lie Algebra of SO(3) is Antisymmetric Matrices|hat map]] $v \mapsto \widehat v$, the adjoint representation is **the defining representation**:

$$\mathrm{Ad}_g(\widehat v) = \widehat{gv} \qquad \text{for } g \in \mathrm{SO}(3), v \in \mathbb{R}^3.$$

Conclude that $\mathrm{Ad} : \mathrm{SO}(3) \to \mathrm{GL}(\mathfrak{so}(3))$ factors as the inclusion $\mathrm{SO}(3) \cong \mathrm{Ad}(\mathrm{SO}(3)) \hookrightarrow \mathrm{GL}(\mathfrak{so}(3))$, with $\mathrm{Ad}$ injective.

**Recall:**

The adjoint representation $\mathrm{Ad}_g = d(C_g)_e$ where $C_g(h) = ghg^{-1}$. For matrix Lie [[Def - Group|groups]], $\mathrm{Ad}_g(X) = gXg^{-1}$. The Lie algebra $\mathfrak{so}(3)$ is the antisymmetric $3 \times 3$ matrices, and the hat map sends $v \in \mathbb{R}^3$ to $\widehat v = \begin{pmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0 \end{pmatrix}$.

---

# Convergent Strategy

**Problem class:** Identification of an abstract Lie-theoretic construction (the adjoint representation on $\mathfrak{so}(3)$) with a concrete classical structure (the defining $3$-dimensional representation of $\mathrm{SO}(3)$). The route is direct calculation: compute $\mathrm{Ad}_g(\widehat v)$ for $g \in \mathrm{SO}(3)$ and $v \in \mathbb{R}^3$, and verify it equals $\widehat{gv}$.

**Assumption pattern:** $\mathfrak{so}(3)$ is identified with $\mathbb{R}^3$ via the hat map, which is a linear isomorphism. The adjoint action of $\mathrm{SO}(3)$ on $\mathfrak{so}(3)$ (matrix conjugation) should correspond to a linear action of $\mathrm{SO}(3)$ on $\mathbb{R}^3$ via the hat-map identification. The natural guess — the defining representation — is the one we verify.

**Theorem routing:** Route is: (1) for matrix [[Def - Group|groups]], $\mathrm{Ad}_g(X) = gXg^{-1}$. (2) Compute $g \widehat v g^{-1} = g \widehat v g^T$ (since $g \in \mathrm{SO}(3)$, $g^{-1} = g^T$). (3) Verify the resulting matrix is the hat of $gv$, i.e., that $(g \widehat v g^T)_{ij} = (\widehat{gv})_{ij}$ — this is a direct computation using the formula for the hat map and the orthogonality of $g$. (4) Conclude $\mathrm{Ad}_g(\widehat v) = \widehat{gv}$, so under the hat-map identification, $\mathrm{Ad}$ on $\mathrm{SO}(3)$ is the defining representation.

**Key decision point:** The non-obvious computation is **verifying that $g \widehat v g^T = \widehat{gv}$ for $g \in \mathrm{SO}(3)$**. This uses the orthogonality of $g$ in an essential way: for a general invertible $g$, $g \widehat v g^{-1}$ is *not* of the form $\widehat w$ for some $w$ — only for $g \in \mathrm{SO}(3)$ does the conjugation preserve the antisymmetric/skew structure. The result is also a beautiful identity that justifies the term "$\widehat v$ is the angular velocity associated to $v$" — rotating the system by $g$ rotates the angular velocity vector by $g$.

---

# Legal Operations Used

1. **Use the adjoint representation to convert group conjugation to a linear action (operation 6 from the topic page).** Applied directly: $\mathrm{Ad}_g =$ conjugation-by-$g$ on $\mathfrak{g}$, here $\mathfrak{so}(3)$.

2. **Use matrix exponential identities (operation 12 from the topic page).** As a sanity check, the relation $\mathrm{Ad}_{\exp X} = \exp(\mathrm{ad}_X)$ in matrix form $g \widehat v g^{-1} = e^{\mathrm{ad}_{\log g}} \widehat v$ provides an alternative verification path via the Lie algebra adjoint $\mathrm{ad}_{\widehat u}(\widehat v) = [\widehat u, \widehat v] = \widehat{u \times v}$.

---

# Hints

> [!note]- Hint 1
> For matrix groups, $\mathrm{Ad}_g(X) = gXg^{-1}$. For $g \in \mathrm{SO}(3)$, $g^{-1} = g^T$, so $\mathrm{Ad}_g(X) = gXg^T$. Apply this with $X = \widehat v$.

> [!note]- Hint 2
> The hat map can be characterized by the identity $\widehat v \cdot w = v \times w$ for all $w \in \mathbb{R}^3$ — i.e., $\widehat v$ is the matrix whose action on $w$ is the cross product $v \times w$. This is the most useful characterization for verifications.

> [!note]- Hint 3
> Use the identity to compute $(g \widehat v g^T) w$ for arbitrary $w$. Apply $g^T$ to $w$, then $\widehat v$, then $g$. Use the cross-product characterization at the middle step.

> [!note]- Hint 4
> Key cross-product identity under orthogonal transformations: $g(u \times v) = (gu) \times (gv)$ for $g \in \mathrm{SO}(3)$. (Proof: both sides are bilinear and antisymmetric in $u, v$; check on basis vectors using $g$ orthogonal and $\det g = 1$.) Combining: $(g \widehat v g^T) w = g(v \times g^T w) = (gv) \times w$ (using cross-product compatibility with $\mathrm{SO}(3)$). So $g \widehat v g^T$ acts on $w$ as $(gv) \times$, which is exactly $\widehat{gv} \cdot$. Hence $g \widehat v g^T = \widehat{gv}$.

> [!note]- Hint 5
> Conclusion: $\mathrm{Ad}_g(\widehat v) = \widehat{gv}$. Under the hat-map identification $\mathfrak{so}(3) \cong \mathbb{R}^3$, the adjoint representation of $g \in \mathrm{SO}(3)$ is just multiplication by $g$ — the defining representation. Hence $\mathrm{Ad} : \mathrm{SO}(3) \to \mathrm{GL}(\mathfrak{so}(3)) \cong \mathrm{GL}(\mathbb{R}^3)$ factors through the inclusion $\mathrm{SO}(3) \hookrightarrow \mathrm{GL}(\mathbb{R}^3)$, with image $\mathrm{Ad}(\mathrm{SO}(3)) = \mathrm{SO}(3)$.

---

# Solution

The proof identifies $\mathrm{Ad}_g(\widehat v)$ with $\widehat{gv}$ via the cross-product characterization of the hat map and the orthogonal-invariance of the cross product.

**Step 1: $\mathrm{Ad}_g(\widehat v) = g \widehat v g^T$ for $g \in \mathrm{SO}(3)$.**

For matrix Lie groups, $\mathrm{Ad}_g(X) = g X g^{-1}$. Since $g \in \mathrm{SO}(3) \subseteq \mathrm{O}(3)$, $g^{-1} = g^T$. Applying with $X = \widehat v$: $\mathrm{Ad}_g(\widehat v) = g \widehat v g^T$.

> [!note]- Derivation
> $\mathrm{Ad}_g(\widehat v) = g \widehat v g^{-1}$ by [[Def - Adjoint Representation|the matrix formula for the adjoint representation]]. For $g \in \mathrm{O}(3)$, $g g^T = I$, so $g^{-1} = g^T$. Substituting: $\mathrm{Ad}_g(\widehat v) = g \widehat v g^T$. Note that this matrix is again antisymmetric: $(g \widehat v g^T)^T = (g^T)^T \widehat v^T g^T = g \cdot (-\widehat v) \cdot g^T = -g \widehat v g^T$, so $g \widehat v g^T \in \mathfrak{so}(3)$, confirming $\mathrm{Ad}_g$ takes $\mathfrak{so}(3) \to \mathfrak{so}(3)$.

**Step 2: The hat-map characterization $\widehat v \cdot w = v \times w$.**

For $v, w \in \mathbb{R}^3$, the matrix $\widehat v$ acts on $w$ as the cross product:

$$\widehat v \cdot w = \begin{pmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0 \end{pmatrix} \begin{pmatrix} w_1 \\ w_2 \\ w_3 \end{pmatrix} = \begin{pmatrix} -v_3 w_2 + v_2 w_3 \\ v_3 w_1 - v_1 w_3 \\ -v_2 w_1 + v_1 w_2 \end{pmatrix} = \begin{pmatrix} v_2 w_3 - v_3 w_2 \\ v_3 w_1 - v_1 w_3 \\ v_1 w_2 - v_2 w_1 \end{pmatrix} = v \times w.$$

This is the operational characterization of the hat map.

> [!note]- Derivation
> Direct computation of $\widehat v \cdot w$ using the explicit form of $\widehat v$ and the standard formula $v \times w = (v_2 w_3 - v_3 w_2, v_3 w_1 - v_1 w_3, v_1 w_2 - v_2 w_1)$ from $3D$ vector calculus.

**Step 3: The cross product is $\mathrm{SO}(3)$-equivariant.**

For $g \in \mathrm{SO}(3)$ and $u, v \in \mathbb{R}^3$, $g(u \times v) = (gu) \times (gv)$. *Proof:* both sides are bilinear and antisymmetric in $u, v$. Check on a positively-oriented orthonormal basis $\{e_1, e_2, e_3\}$: $e_1 \times e_2 = e_3$, so $g(e_1 \times e_2) = g e_3$. Also, $(g e_1) \times (g e_2) = ?$ — using the formula $a \times b = (\det[e_1, e_2, e_3]) \cdot (a \times b)$... more directly, the columns of $g$ form a positively-oriented orthonormal basis $\{g e_1, g e_2, g e_3\}$ (since $g \in \mathrm{SO}(3)$), so $(g e_1) \times (g e_2) = g e_3$ by the orthonormal-basis property of the cross product. So $g(e_1 \times e_2) = (g e_1) \times (g e_2)$ on the basis. By bilinearity, it extends to all of $\mathbb{R}^3$.

> [!note]- Derivation
> The cross product on $\mathbb{R}^3$ is uniquely characterized by: (1) bilinearity, (2) antisymmetry, (3) $|u \times v|^2 = |u|^2 |v|^2 - (u \cdot v)^2$ (norm), (4) $u \times v$ is orthogonal to both $u$ and $v$, (5) $\{u, v, u \times v\}$ is positively oriented when $\{u, v\}$ is linearly independent. Orthogonal $g \in \mathrm{SO}(3)$ preserves all of these: bilinearity is trivial; antisymmetry is trivial; the norm is preserved by orthogonality; orthogonality is preserved by orthogonality of $g$; positive orientation is preserved because $\det g = 1$. So $g(u \times v)$ satisfies all the characterizing properties of $(gu) \times (gv)$, hence they are equal.

**Step 4: Combine to get $\mathrm{Ad}_g(\widehat v) = \widehat{gv}$.**

For arbitrary $w \in \mathbb{R}^3$, compute $(g \widehat v g^T) w$:

$$\begin{aligned}
(g \widehat v g^T) w &= g (\widehat v (g^T w)) \\
&= g (v \times g^T w) \qquad \text{(Step 2)} \\
&= g(v \times g^T w) \\
&\stackrel{?}{=} (gv) \times (g \cdot g^T w) \qquad \text{(if Step 3 applies)} \\
&= (gv) \times w \qquad \text{(}gg^T = I\text{)} \\
&= \widehat{gv} \cdot w \qquad \text{(Step 2)}.
\end{aligned}$$

The starred step uses Step 3 applied to $(v, g^T w)$: $g(v \times g^T w) = (gv) \times (g g^T w) = (gv) \times w$.

Since $(g \widehat v g^T) w = \widehat{gv} \cdot w$ for every $w \in \mathbb{R}^3$, the matrices are equal: $g \widehat v g^T = \widehat{gv}$. Hence

$$\mathrm{Ad}_g(\widehat v) = \widehat{gv}.$$

> [!note]- Derivation
> The chain $g \widehat v g^T \cdot w = g(\widehat v (g^T w)) = g(v \times g^T w) = (gv) \times (g g^T w) = (gv) \times w = \widehat{gv} \cdot w$ uses: (a) matrix multiplication associativity (first step); (b) hat-map characterization $\widehat v u = v \times u$ (second step, with $u = g^T w$); (c) $\mathrm{SO}(3)$-equivariance of the cross product (third step); (d) $g g^T = I$ since $g \in \mathrm{O}(3)$ (fourth step); (e) hat-map characterization again (fifth step). The equality holds for all $w$, so the matrices are equal.

**Step 5: Conclude $\mathrm{Ad}$ factors as the defining representation of $\mathrm{SO}(3)$.**

Under the hat-map identification $\widehat{} : \mathbb{R}^3 \to \mathfrak{so}(3)$ (a linear isomorphism), the adjoint action $\mathrm{Ad}_g : \mathfrak{so}(3) \to \mathfrak{so}(3)$ corresponds to the action $v \mapsto gv$ on $\mathbb{R}^3$ — the **defining representation** of $\mathrm{SO}(3)$ on $\mathbb{R}^3$. So $\mathrm{Ad} : \mathrm{SO}(3) \to \mathrm{GL}(\mathfrak{so}(3)) \cong \mathrm{GL}(\mathbb{R}^3)$ is the inclusion

$$\mathrm{Ad} : \mathrm{SO}(3) \hookrightarrow \mathrm{GL}(3, \mathbb{R}), \qquad g \mapsto g,$$

with image $\mathrm{Ad}(\mathrm{SO}(3)) = \mathrm{SO}(3) \subseteq \mathrm{GL}(\mathbb{R}^3)$. **$\mathrm{Ad}$ is injective on $\mathrm{SO}(3)$**: $\ker \mathrm{Ad} = Z(\mathrm{SO}(3)) = \{I\}$ (the center of $\mathrm{SO}(3)$ is trivial — Lee Problem 20-20).

> [!note]- Complete formal solution
> *Computation of $\mathrm{Ad}_g(\widehat v)$.* For $g \in \mathrm{SO}(3)$, $\mathrm{Ad}_g(X) = gXg^{-1} = gXg^T$ (using $g^{-1} = g^T$). The hat map satisfies $\widehat v \cdot w = v \times w$ for all $v, w$. The cross product is $\mathrm{SO}(3)$-equivariant: $g(u \times v) = (gu) \times (gv)$. Combining:
> $$(g \widehat v g^T) w = g(v \times (g^T w)) = (gv) \times (g g^T w) = (gv) \times w = \widehat{gv} \cdot w \quad \forall w \in \mathbb{R}^3,$$
> so $g \widehat v g^T = \widehat{gv}$. Hence $\mathrm{Ad}_g(\widehat v) = \widehat{gv}$.
>
> *Factorization.* Under the hat-map identification $\mathfrak{so}(3) \cong \mathbb{R}^3$, $\mathrm{Ad}_g$ acts as $g$ on $\mathbb{R}^3$ — the defining representation. So $\mathrm{Ad} : \mathrm{SO}(3) \to \mathrm{GL}(\mathfrak{so}(3)) \cong \mathrm{GL}(3, \mathbb{R})$ is the inclusion of $\mathrm{SO}(3)$ as a [[Def - Subgroup|subgroup]] of $\mathrm{GL}(3)$, with image $\mathrm{SO}(3)$. Since $Z(\mathrm{SO}(3)) = \{I\}$, $\mathrm{Ad}$ has trivial kernel — it is **injective**. $\qquad\blacksquare$

> [!warning] Illegal but tempting: assuming $\mathrm{Ad}_g$ acts arbitrarily on $\mathfrak{so}(3)$
> One might think the adjoint representation gives some new, possibly higher-dimensional or irreducible-decomposed action of $\mathrm{SO}(3)$ on $\mathfrak{so}(3)$. The result of this exercise is much cleaner: $\mathrm{Ad}$ on $\mathrm{SO}(3)$ is **just the defining representation**, with no new structure. The reason is that $\mathfrak{so}(3)$ is $3$-dimensional and $\mathrm{SO}(3)$ already has a natural $3$-dimensional irreducible representation (the defining one); by representation-theoretic [[Def - Dimension|dimension]] considerations, the adjoint representation is forced to be the defining one (up to isomorphism, which the hat map provides explicitly).

---

# Key Takeaways

**The adjoint representation of $\mathrm{SO}(n)$ is the antisymmetric-tensor representation on $\Lambda^2 \mathbb{R}^n$.**

For general $n$, $\mathfrak{so}(n) \cong \Lambda^2 \mathbb{R}^n$ (antisymmetric bilinear forms on $\mathbb{R}^n$), and the adjoint representation of $\mathrm{SO}(n)$ on $\mathfrak{so}(n)$ is the natural representation on $\Lambda^2 \mathbb{R}^n$. For $n = 3$, $\Lambda^2 \mathbb{R}^3 \cong \mathbb{R}^3$ via the Hodge star (or the hat map), so the adjoint representation becomes the defining representation. For $n = 4$, $\Lambda^2 \mathbb{R}^4$ is $6$-dimensional, and the adjoint representation on $\mathfrak{so}(4) = \Lambda^2 \mathbb{R}^4$ has a richer structure — in fact it splits as $\mathfrak{so}(4) = \mathfrak{so}(3) \oplus \mathfrak{so}(3)$ (self-dual + anti-self-dual), the source of "[[Def - Instanton|instanton]] chirality" in $4$D gauge theory.

**Adjoint orbits of $\mathrm{SO}(3)$ on $\mathfrak{so}(3) \cong \mathbb{R}^3$ are spheres centered at the origin.**

Since $\mathrm{Ad}_g(\widehat v) = \widehat{gv}$ acts as the defining representation, the orbits of $\mathrm{Ad}$ on $\mathfrak{so}(3) \cong \mathbb{R}^3$ are the orbits of $\mathrm{SO}(3)$ on $\mathbb{R}^3$ — concentric spheres around the origin. Each sphere is a coadjoint orbit (with the canonical symplectic structure), corresponding to a fixed "angular momentum magnitude". This is the geometric origin of the **quantization of angular momentum** in quantum mechanics: representations of $\mathrm{SU}(2)$ (the double cover) on $\mathbb{C}^{2j+1}$ correspond to spin-$j$ particles, with the integer or half-integer label $j$ classifying the irreducible representations and matching the radii of allowed angular-momentum spheres.

**The injectivity of $\mathrm{Ad}$ characterizes "centerless" Lie groups.**

For a general Lie group $G$, $\ker \mathrm{Ad} = Z(G)$ (the center). When $Z(G) = \{e\}$, $\mathrm{Ad}$ is injective, and $G \hookrightarrow \mathrm{GL}(\mathfrak{g})$ via $\mathrm{Ad}$ — so $G$ is realizable as a matrix group. This is the case for $\mathrm{SO}(3)$ (centerless, hence faithfully embedded by $\mathrm{Ad}$). Contrast with $\mathrm{SU}(2)$: its center is $\{\pm I\}$, so $\mathrm{Ad} : \mathrm{SU}(2) \to \mathrm{GL}(\mathfrak{su}(2)) = \mathrm{GL}(3)$ has kernel $\{\pm I\}$, and the image is $\mathrm{SO}(3) \subseteq \mathrm{GL}(3)$ — the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3)$ is exactly the adjoint representation of $\mathrm{SU}(2)$. So **$\mathrm{Ad}$ is the canonical way to relate $\mathrm{SU}(2)$ to $\mathrm{SO}(3)$ via Lie algebra theory**.
