---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Orthonormal Frame Bundle"
  - "Def - Associated Bundle"
  - "Def - Homogeneous Bundle"
tags: [geometry, gauge-theory, frame-bundles]
---

# Problem Statement

The 2-sphere $S^2$ is the homogeneous space $\mathrm{SO}(3)/\mathrm{SO}(2)$, where $\mathrm{SO}(3)$ acts on $S^2$ by rotations and $\mathrm{SO}(2)$ is the stabilizer of any chosen point (the rotations about the axis through that point). This gives a principal $\mathrm{SO}(2) = U(1)$-bundle $\mathrm{SO}(2) \to \mathrm{SO}(3) \to S^2$.

**Show:**

(a) The orthonormal frame bundle $\mathrm{Fr}^{\mathrm{SO}}(S^2)$ of the round 2-sphere is diffeomorphic to $\mathrm{SO}(3)$ as a principal $\mathrm{SO}(2)$-bundle.

(b) The tangent bundle $TS^2$ is recovered from the principal bundle $\mathrm{SO}(3) \to S^2$ via the associated-bundle construction with the standard $\mathrm{SO}(2)$ action on $\mathbb{R}^2$:
$$TS^2 \cong \mathrm{SO}(3) \times_{\mathrm{SO}(2)} \mathbb{R}^2.$$

(c) The bundle $TS^2$ is **not trivial**: no global section of $\mathrm{SO}(3) \to S^2$ exists, equivalent to the hairy-ball theorem.

**Recall:**

![[Def - Frame Bundle of a Vector Bundle#The Definition]]

![[Def - Orthonormal Frame Bundle#The Definition]]

![[Def - Associated Bundle#The Definition]]

![[Def - Homogeneous Bundle#The Definition]]

---

# Convergent Strategy

**Problem class:** This is a problem of *identifying a principal bundle structure on a familiar manifold* and using it to construct an associated vector bundle. The topic-page strategy "build bundles from homogeneous-space data" applies: $S^2 = G/H$ with $G = \mathrm{SO}(3)$, $H = \mathrm{SO}(2)$, so the principal $H$-bundle $G \to G/H$ is automatic, and the associated bundle gives $TS^2$.

**Assumption pattern:** The key assumptions are: (i) $\mathrm{SO}(3)$ acts transitively on $S^2$, (ii) the stabilizer of a point is $\mathrm{SO}(2)$, (iii) the tangent space at each point is a 2-dimensional vector space on which $\mathrm{SO}(2)$ acts by rotation. Together these give the homogeneous-bundle structure and the associated-bundle recovery of $TS^2$.

**Theorem routing:** Frankel Theorem 17.11 (closed subgroup theorem / homogeneous-bundle construction) gives $\mathrm{SO}(2) \to \mathrm{SO}(3) \to S^2$ as a principal bundle. The associated-bundle construction $TS^2 = \mathrm{SO}(3) \times_{\mathrm{SO}(2)} \mathbb{R}^2$ uses [[Thm - Associated-Bundle Construction Yields a Bundle]]. The nontriviality follows from the hairy-ball theorem (no nonzero continuous tangent vector field on $S^2$), or equivalently from $\chi(S^2) = 2 \neq 0$ in [[Thm - Gauss-Bonnet for Closed Surfaces (Chern's Proof)]].

**Key decision point:** The non-obvious step is identifying $\mathrm{Fr}^{\mathrm{SO}}(S^2) = \mathrm{SO}(3)$ — i.e., recognizing that an oriented orthonormal frame at $p \in S^2$ is the same data as a rotation matrix $R \in \mathrm{SO}(3)$ such that $R \cdot e_3 = p$ (sending the north pole to $p$) together with a choice of in-plane orientation. The "first basis vector points to $p$" identification is the key insight.

---

# Legal Operations Used

1. **Operation 5 from the topic page (Construct a homogeneous space from a transitive action).** Apply: $\mathrm{SO}(3)$ acts transitively on $S^2$; stabilizer is $\mathrm{SO}(2)$; hence $S^2 \cong \mathrm{SO}(3)/\mathrm{SO}(2)$ as a manifold, and $\mathrm{SO}(3) \to S^2$ is a principal $\mathrm{SO}(2)$-bundle.

2. **Operation 1 from the topic page (Pass between a vector bundle and its frame bundle).** Apply: the principal $\mathrm{SO}(2)$-bundle $\mathrm{SO}(3) \to S^2$ together with the standard $\mathrm{SO}(2)$-action on $\mathbb{R}^2$ gives the associated vector bundle, which is $TS^2$.

3. **Operation 6 from the topic page (Construct a global section to detect triviality).** Apply: showing no global section of $\mathrm{SO}(3) \to S^2$ exists, equivalent to the nonexistence of a nowhere-vanishing vector field on $S^2$.

---

# Hints

> [!note]- Hint 1
> Think of a positively oriented orthonormal frame on $S^2$ as a "rotation that puts the standard $z$-axis basis at the point $p$, with the choice of in-plane rotation tracking the frame orientation". This identifies the frame bundle with $\mathrm{SO}(3)$.

> [!note]- Hint 2
> For part (b), the fibre of $\mathrm{SO}(3) \times_{\mathrm{SO}(2)} \mathbb{R}^2$ over $p \in S^2$ is the set of equivalence classes $[g, v]$ with $g \cdot e_3 = p$ and $v \in \mathbb{R}^2$. Map $[g, v] \in $ fibre over $p$ to the tangent vector at $p$ obtained by transporting $v$ via the frame $g$.

> [!note]- Hint 3
> For part (c), use Gauss-Bonnet: $\chi(S^2) = 2 \neq 0$, so by Poincaré-Hopf no nowhere-vanishing vector field exists, hence no global frame, hence no global section of the principal bundle.

---

# Solution

The proof has three steps. Step 1 establishes the diffeomorphism $\mathrm{Fr}^{\mathrm{SO}}(S^2) \cong \mathrm{SO}(3)$ via the frame-to-rotation identification. Step 2 uses the associated-bundle construction with the principal $\mathrm{SO}(2)$-action on $\mathbb{R}^2$ to recover $TS^2$. Step 3 uses the Euler-characteristic non-vanishing to conclude nontriviality. The non-obvious move is in Step 1, where the identification of frames with rotation matrices is what makes the homogeneous structure visible.

**Step 1: $\mathrm{Fr}^{\mathrm{SO}}(S^2) \cong \mathrm{SO}(3)$ as principal $\mathrm{SO}(2)$-bundles.**

A positively oriented orthonormal frame at $p \in S^2$ is a pair $(p, (e_1, e_2))$ where $(e_1, e_2)$ is an orthonormal basis of $T_pS^2$ with positive orientation.

> [!note]- Derivation
> Identify $T_pS^2 = p^\perp \subset \mathbb{R}^3$. A frame $(p, e_1, e_2)$ extends to an orthonormal basis $(e_1, e_2, p)$ of $\mathbb{R}^3$. Define $R \in \mathrm{SO}(3)$ by $R = (e_1 | e_2 | p)$, the matrix whose columns are $e_1, e_2, p$. The condition "positively oriented in $T_pS^2$" with the convention that $(e_1, e_2, p)$ is right-handed gives $\det R = +1$, i.e., $R \in \mathrm{SO}(3)$. Conversely, every $R \in \mathrm{SO}(3)$ produces a frame at $p = R \cdot e_3 = (R_{13}, R_{23}, R_{33})$ by reading off the first two columns. This is a bijection $\mathrm{SO}(3) \leftrightarrow \mathrm{Fr}^{\mathrm{SO}}(S^2)$, smooth in both directions (since taking columns of a matrix is smooth and constructing a matrix from columns is smooth).
>
> Under this bijection, the projection $\pi : \mathrm{SO}(3) \to S^2$, $R \mapsto R\cdot e_3$, matches the frame-bundle projection $\mathrm{Fr}^{\mathrm{SO}}(S^2) \to S^2$.
>
> The right $\mathrm{SO}(2)$-action on $\mathrm{Fr}^{\mathrm{SO}}(S^2)$ — rotation of the frame within $T_pS^2$ — corresponds to multiplication on the right by $\mathrm{SO}(2) \hookrightarrow \mathrm{SO}(3)$ via $\mathrm{SO}(2) = \begin{pmatrix}\cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1\end{pmatrix}$. Verification: $R \cdot R_\theta$ has columns rotated by $\theta$ in the $(e_1, e_2)$ plane, third column unchanged ($p$ unchanged). So the bijection is $\mathrm{SO}(2)$-equivariant, i.e., an isomorphism of principal $\mathrm{SO}(2)$-bundles.

**Step 2: $TS^2 \cong \mathrm{SO}(3) \times_{\mathrm{SO}(2)} \mathbb{R}^2$.**

The associated-bundle construction yields a rank-2 vector bundle over $S^2$.

> [!note]- Derivation
> By Step 1, $\mathrm{SO}(3) \to S^2$ is the orthonormal frame bundle of $S^2$. By [[Thm - Associated-Bundle Construction Yields a Bundle]], the associated bundle $\mathrm{SO}(3) \times_{\mathrm{SO}(2)} \mathbb{R}^2$ — with $\mathrm{SO}(2)$ acting on $\mathbb{R}^2$ by the standard rotation action — is a rank-2 vector bundle over $S^2$ with structure group $\mathrm{SO}(2)$.
>
> The explicit isomorphism with $TS^2$: a point $[R, v] \in \mathrm{SO}(3) \times_{\mathrm{SO}(2)} \mathbb{R}^2$ corresponds to the tangent vector $v^1 e_1 + v^2 e_2 \in T_{R\cdot e_3}S^2$, where $(e_1, e_2)$ is the frame at $R\cdot e_3$ given by Step 1 (the first two columns of $R$). Well-definedness under the equivalence $(R, v) \sim (R \cdot R_\theta, R_{-\theta}\cdot v)$: the frame at $R \cdot e_3$ rotated by $\theta$ has new basis $(\cos\theta e_1 + \sin\theta e_2, -\sin\theta e_1 + \cos\theta e_2)$, and the inverse rotation of $v$ undoes this, so the resulting tangent vector is invariant.
>
> So $TS^2 \cong \mathrm{SO}(3) \times_{\mathrm{SO}(2)} \mathbb{R}^2$ as rank-2 vector bundles over $S^2$.

**Step 3: $TS^2$ is nontrivial.**

> [!note]- Derivation
> Triviality of $TS^2$ would give a nowhere-vanishing tangent vector field on $S^2$. By the **hairy-ball theorem** (equivalently, Poincaré-Hopf with $\chi(S^2) = 2$), no such vector field exists. So $TS^2$ is not trivial, and equivalently $\mathrm{SO}(3) \to S^2$ has no global section.
>
> Alternatively, by [[Thm - Gauss-Bonnet for Closed Surfaces (Chern's Proof)]], $\frac{1}{2\pi}\int_{S^2} K\,dA = \chi(S^2) = 2$, and a trivial bundle would have zero Euler class.

> [!note]- Complete formal solution
> Identify $\mathrm{SO}(3)$ with $\mathrm{Fr}^{\mathrm{SO}}(S^2)$ via $R \mapsto (R\cdot e_3, R\cdot e_1, R\cdot e_2)$, with right $\mathrm{SO}(2)$-action by matrix multiplication preserving the third column (Step 1). The associated bundle of this principal $\mathrm{SO}(2)$-bundle with the standard $\mathrm{SO}(2)$-action on $\mathbb{R}^2$ is the tangent bundle $TS^2$ by the explicit map $[R, v] \mapsto v^1(R\cdot e_1) + v^2(R\cdot e_2) \in T_{R\cdot e_3}S^2$ (Step 2). The triviality of either $TS^2$ or the principal bundle would give a global section of $\mathrm{SO}(3) \to S^2$, hence a nowhere-vanishing vector field on $S^2$, contradicting $\chi(S^2) = 2 \neq 0$ (Step 3). ∎

> [!warning] Sanity-check via independent route
> The diffeomorphism $\mathrm{SO}(3) \cong \mathbb{RP}^3$ (the double cover $\mathrm{Spin}(3) = S^3 \to \mathrm{SO}(3)$ gives $\mathrm{SO}(3) = S^3/\{\pm 1\} = \mathbb{RP}^3$) is consistent: $\mathbb{RP}^3$ has dimension 3, and $\mathrm{SO}(2) \to \mathbb{RP}^3 \to S^2$ has $\dim \mathrm{SO}(2) + \dim S^2 = 1 + 2 = 3$. ✓

---

# Key Takeaways

**Frame bundles as principal $\mathrm{SO}(n)$-bundles via Lie-theoretic identification.** The orthonormal frame bundle of a symmetric space $G/H$ is often the group $G$ itself, identified via "the first basis vector is where the rotation sent the standard one". This identification turns abstract bundle-theoretic computations into concrete Lie-group computations: bundles become groups, sections become group elements, characteristic classes become Lie-algebraic invariants. The pattern $\mathrm{Fr}^{\mathrm{SO}}(S^n) \cong \mathrm{SO}(n+1)$ generalizes the present example to all spheres; the orthonormal frame bundle of $\mathbb{CP}^n$ is $U(n+1)$ (with extra structure tracking the complex structure); the frame bundle of a Grassmannian is a Stiefel manifold. The "trigger" is "the manifold is a homogeneous space of a compact Lie group" — then the frame bundle is computable explicitly.

**Associated-bundle construction recovers the tangent bundle from the principal bundle.** Once the principal $\mathrm{SO}(n)$-bundle of orthonormal frames is in hand, the tangent bundle is automatically $\mathrm{Fr}^{\mathrm{SO}}(M) \times_{\mathrm{SO}(n)} \mathbb{R}^n$ — and *every* tensor / spinor / form bundle on $M$ is similarly recovered as an associated bundle with the appropriate $\mathrm{SO}(n)$-representation. This is the universal-object characterization of the principal bundle and is why gauge theorists work primarily with principal bundles: one principal bundle generates all the matter-field bundles automatically.

**Nontriviality of $TS^2$ from $\chi(S^2) \neq 0$ via Gauss-Bonnet.** The simplest possible bundle-nontriviality argument: compute the Euler characteristic; if it is nonzero, the tangent bundle is nontrivial. The Gauss-Bonnet theorem makes this rigorous by exhibiting $\chi$ as a curvature integral, hence forcing it to be nonzero for the round sphere (positive Gauss curvature integrates positively). The same argument works for any surface of genus $0, 2, 3, \ldots$ (which all have $\chi \neq 0$) and any even-dimensional manifold with $\chi \neq 0$. For genus-$1$ surfaces ($\chi = 0$) the tangent bundle is trivial (e.g., the flat torus admits a global frame). The trigger-reaction pattern: "is the tangent bundle of this manifold trivial?" → "compute $\chi$; if nonzero, no."

This exercise parallels [[Ex - SU(2) is Diffeomorphic to S^3]] (an instance of the same homogeneous-space framework) and prefigures the spin-structure problem of [[Spinors and the Dirac Equation]] (where the principal $\mathrm{Spin}(n) \to \mathrm{SO}(n)$ lift is asked for instead of the orthonormal frame bundle itself).
