---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Riemannian Metric"
  - "Def - Metric-Compatible Connection"
  - "Def - Torsion Tensor"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, riemannian-geometry, connections, levi-civita]
---

# Notation

$(M, g)$ — a Riemannian (or semi-Riemannian) manifold. $\nabla$ — a torsion-free metric-compatible connection on $TM$. $X, Y, Z$ — smooth vector fields on $M$. $[X, Y]$ — the Lie bracket. $Xg(Y, Z)$ — the action of $X$ on the smooth function $g(Y, Z)$, the directional derivative. Full notation registry on [[Riemannian Geometry I — Connections and Covariant Differentiation]].

---

# Statement

> **Theorem (Koszul Formula).** Let $(M, g)$ be a Riemannian or semi-Riemannian manifold and let $\nabla$ be a torsion-free metric-compatible connection on $TM$. Then for all vector fields $X, Y, Z \in \mathfrak{X}(M)$,
> $$
> 2g(\nabla_X Y, Z) = X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X).
> $$

This formula expresses $\nabla_X Y$ entirely in terms of $g$ and the Lie brackets of $X, Y, Z$. Together with the non-degeneracy of $g$, it shows that **a torsion-free metric-compatible connection is unique** (and, run in reverse, that it exists), which is the content of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]].

---

# Motivation

The Levi-Civita connection on a Riemannian manifold is characterised by two conditions — torsion-freeness ($\nabla_X Y - \nabla_Y X = [X, Y]$) and metric-compatibility ($Xg(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$). Together these are *just enough* data to determine $\nabla$ uniquely from $g$ — but it is not transparent from the conditions themselves how one would *compute* $\nabla_X Y$ in practice.

The Koszul formula resolves this completely. It is a closed-form expression for the inner product $g(\nabla_X Y, Z)$ in terms of $g$ and Lie brackets alone — no $\nabla$ appears on the right side. Since $g$ is non-degenerate, knowing $g(\nabla_X Y, Z)$ for every $Z$ determines $\nabla_X Y$ uniquely. So the Koszul formula is the *explicit construction* of the Levi-Civita connection from the metric.

The formula has two main roles in Riemannian geometry. **First**, as the engine of the proof of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem]]: it shows both existence and uniqueness of the Levi-Civita connection. Uniqueness because any two torsion-free metric-compatible connections satisfy the same formula and so agree. Existence because *defining* $\nabla_X Y$ via the formula (using the sharp map of $g$ to convert from "inner product with $Z$" to a vector) gives an operation that one can verify is a torsion-free metric-compatible connection.

**Second**, as the master formula for computing the connection on manifolds where coordinates are awkward. On a Lie group $G$ with bi-invariant metric, Lie brackets of left-invariant fields are known explicitly (they are the Lie bracket of the Lie algebra), and the Koszul formula collapses dramatically: for left-invariant $X, Y, Z$ on a bi-invariantly metric Lie group, $X g(Y, Z) = Y g(Z, X) = Z g(X, Y) = 0$ (inner products of left-invariant fields are constant), and the bi-invariance gives $g([X, Y], Z) = -g(Y, [X, Z])$, simplifying the formula to $2g(\nabla_X Y, Z) = g([X, Y], Z)$, hence $\nabla_X Y = \tfrac{1}{2}[X, Y]$.

---

# Sources and Targets

**Sources (Input Broadening)**

The Koszul formula requires: a torsion-free metric-compatible connection $\nabla$ and the data $(g, X, Y, Z)$. Recognizing when this configuration is in play is mostly recognising when the Levi-Civita connection is the connection of interest.

*Source 1: any Riemannian or semi-Riemannian manifold.* By the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem]], every Riemannian and semi-Riemannian manifold has a unique torsion-free metric-compatible connection — the Levi-Civita. So the Koszul formula applies on *every* Riemannian or semi-Riemannian manifold without further input. The implication is non-obvious only in that not every connection on a Riemannian manifold satisfies Koszul — only the Levi-Civita does. The bridge: "we have a metric" → "Koszul determines the (unique) torsion-free compatible connection".

*Source 2: a Lie group with bi-invariant metric.* On a Lie group $G$ with bi-invariant Riemannian metric, the Koszul formula on left-invariant fields simplifies via three structural facts: (a) inner products of left-invariant fields are constant ($X g(Y, Z) = 0$ for left-invariant $X, Y, Z$); (b) $\mathrm{Ad}$-invariance of $g$ implies $g([X, Y], Z) + g(Y, [X, Z]) = 0$; (c) Jacobi identity for the Lie bracket. The result is $\nabla_X Y = \tfrac{1}{2}[X, Y]$ — see Source 3 of [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)]]. The implication is non-obvious because the original formula has six terms that all collapse to one; the route is via the algebraic identities of the bi-invariant structure.

*Source 3: a submanifold with induced metric in $\mathbb{R}^N$.* For $S \hookrightarrow \mathbb{R}^N$ with induced metric, the Levi-Civita connection on $S$ is the tangential projection $\nabla^S_X Y = (\nabla^{\mathbb{R}^N}_X Y)^\top$. To verify this is the Levi-Civita connection (rather than some other connection), one can use the Koszul formula: substitute the projection definition into the formula and check that the equation holds. The non-obvious step is converting between "tangential projection of ambient $\nabla$" and "explicit Koszul-formula computation"; both characterise the same connection.

*Source 4: any symmetric, non-degenerate $(0, 2)$-tensor field.* The Koszul formula uses only the metric (assumed symmetric and non-degenerate) and Lie brackets; positive-definiteness is *not* used in the derivation. So the formula works equally for Riemannian and Lorentzian metrics, and indeed for any non-degenerate symmetric bilinear form. The Lorentzian application is exactly what makes general relativity possible: the Levi-Civita connection of the Lorentzian spacetime metric is computed by the same Koszul formula.

**Targets (Output Amplification)**

The conclusion is "$g(\nabla_X Y, Z)$ is determined by $g$ and Lie brackets". Combined with further structural inputs, this yields:

*Target combination 1: Koszul + non-degeneracy of $g$ ⟹ uniqueness of Levi-Civita.* The Koszul formula expresses $g(\nabla_X Y, Z)$ for every $Z$. Adding the additional property $D$ that $g$ is non-degenerate (i.e., $g(v, w) = 0$ for all $w$ implies $v = 0$), we conclude $\nabla_X Y$ is determined uniquely: any vector $V$ with $g(V, Z)$ equal to half the RHS of Koszul is unique. The result $E$: the Levi-Civita connection is unique. This combination is the proof of the uniqueness half of the fundamental theorem.

*Target combination 2: Koszul + sharp map ⟹ existence of Levi-Civita.* The Koszul formula RHS is $C^\infty(M)$-linear in $Z$ (a fact requiring direct verification, using the Lie-bracket Leibniz rules). So for fixed $X, Y$, the right side defines a smooth 1-form $\eta \in \Omega^1(M)$ via $\eta(Z) = \tfrac{1}{2}(\text{RHS})$. Adding the additional property $D$ that $g$ has a sharp map ($\sharp : T^*M \to TM$, $\eta \mapsto \eta^\sharp$ with $g(\eta^\sharp, Z) = \eta(Z)$), we can *define* $\nabla_X Y := \eta^\sharp$. The result $E$: existence of a connection satisfying Koszul, which one then verifies is torsion-free and metric-compatible. This combination is the proof of the existence half of the fundamental theorem.

*Target combination 3: Koszul on coordinate frames ⟹ Christoffel formula.* Apply Koszul with $X = \partial_i$, $Y = \partial_j$, $Z = \partial_l$. Since $[\partial_i, \partial_j] = 0$ in any coordinate frame, the Lie-bracket terms vanish. The metric-derivative terms become $\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}$, and $g(\nabla_{\partial_i}\partial_j, \partial_l) = \Gamma^k_{ij}g_{kl}$. Raising the index gives $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$ — the **Christoffel formula** of [[Def - Christoffel Symbols]]. This is the most-used target combination in practice: it converts the abstract Koszul formula into the concrete coordinate formula one uses for actual computations.

*Target combination 4: Koszul on bi-invariant Lie groups ⟹ $\nabla_X Y = \tfrac{1}{2}[X, Y]$.* On a Lie group $G$ with bi-invariant metric, apply Koszul to left-invariant fields $X, Y, Z$. The function-derivative terms $X g(Y, Z), Y g(X, Z), Z g(X, Y)$ all vanish (inner products of left-invariant fields are constants). The bracket terms reduce to $g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X)$. Using $\mathrm{Ad}$-invariance $g([A, B], C) = -g(B, [A, C])$, the last two terms become $-g([X, Z], Y) - g([Y, Z], X) = g(Z, [X, Y]) + g(Z, [Y, X]) = 0$ ... wait, more carefully: $g([X, Z], Y) = -g(Z, [X, Y])$ by $\mathrm{Ad}$-invariance with $A = X$. So $-g([X, Z], Y) = g(Z, [X, Y]) = g([X, Y], Z)$. Similarly $-g([Y, Z], X) = g(Z, [Y, X]) = -g([X, Y], Z)$. The two cancel, leaving just $g([X, Y], Z)$, so $2g(\nabla_X Y, Z) = g([X, Y], Z)$ and $\nabla_X Y = \tfrac{1}{2}[X, Y]$ — the elegant Lie-group formula for the Levi-Civita connection. The result $E$: geodesics through the identity of a bi-invariant Lie group are one-parameter subgroups.

---

# Why Is It True

**Mechanism summary:** **the Koszul formula is what you get by symmetrising metric-compatibility over the three permutations of $(X, Y, Z)$, adding with alternating signs, and using torsion-freeness to eliminate the resulting $\nabla_Y X$ and $\nabla_Z X$, $\nabla_Z Y$ terms in favour of Lie brackets.**

The intuition: metric-compatibility gives one identity relating six $\nabla$-terms, $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$. There are three such identities — one for each cyclic permutation of $(X, Y, Z)$. Adding the three with appropriate signs ($+, +, -$) gives a sum involving the six $\nabla$-terms with patterns: $g(\nabla_X Y, Z), g(\nabla_X Z, Y), g(\nabla_Y Z, X), g(\nabla_Y X, Z), g(\nabla_Z X, Y), g(\nabla_Z Y, X)$. Of these, only the three with "the right ordering" — say $\nabla_X Y, \nabla_Y X, \nabla_Z Y$, where the first argument is "less than" the second in some ordering — are independent of torsion-freeness; the others can be converted by torsion-freeness $\nabla_Y X = \nabla_X Y - [X, Y]$ etc. The conversion leaves only $g(\nabla_X Y, Z)$ doubled (hence the factor of $2$) plus Lie-bracket terms. This is the entire trick.

A different mnemonic: the Koszul formula is the **antisymmetrisation of metric-compatibility under the symmetric group $S_3$ acting on $(X, Y, Z)$**, with the antisymmetric piece being the Lie brackets and the symmetric piece being the inner product $g(\nabla_X Y, Z)$. The symmetrisation collapses the three independent metric-compatibility identities into one explicit formula.

---

# What Makes This Hard

The conceptual difficulty is **the cyclic symmetrisation move itself** — it is not at all obvious that you should add the three permuted metric-compatibility equations with signs $(+, +, -)$, and the choice of signs is what makes the desired $g(\nabla_X Y, Z)$ term emerge while the cross-terms cancel. Students often try the same calculation with different sign choices and get nonsense. The lesson: the sign pattern $(+X g(Y, Z), +Y g(X, Z), -Z g(X, Y))$ is forced by the desire that the $\nabla$-terms with $X$ and $Y$ as the second argument survive while those with $Z$ as the second argument cancel — and this matches the conventional Koszul formula.

The second hard part is **verifying $C^\infty$-linearity of the right side in $Z$**. The Lie-bracket terms $g([X, Y], Z)$ are trivially $C^\infty$-linear in $Z$ (the inner product is $C^\infty$-linear in its second argument). But the function-derivative terms $X g(Y, Z), Y g(X, Z), Z g(X, Y)$ involve $Z$ either as the argument of the inner product (linear) or as the differentiator ($Z g(X, Y)$ — and this is the tricky one). The Leibniz rule applied to $Z g(X, Y) = (fZ)g(X, Y) = ...$, combined with the Leibniz of $[Y, fZ] = f[Y, Z] - Y(f)Z$ in the bracket terms, gives the necessary cancellations. This is a non-trivial direct check.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Start from metric-compatibility in three cyclic permutations. Add with signs $(+, +, -)$. Use torsion-freeness to convert the unwanted $\nabla$ terms into Lie brackets. Collect to get the Koszul formula.

**Subgoal decomposition:**

1. **Write down three metric-compatibility identities.** $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$, with cyclic permutations $(X, Y, Z) \to (Y, Z, X)$ and $(X, Y, Z) \to (Z, X, Y)$.
   - *Hint:* Three identities with $X g(Y, Z), Y g(Z, X), Z g(X, Y)$ on the LHS.
   - *Why needed:* Three relations with different orderings give a system from which to extract $\nabla_X Y$.

2. **Add with signs $(+, +, -)$.** Form $Xg(Y, Z) + Yg(Z, X) - Zg(X, Y)$.
   - *Hint:* The sign on the third is chosen so that the $g(\nabla_Z Y, X)$ and $g(\nabla_Z X, Y)$ contributions cancel rather than reinforce.
   - *Why needed:* Isolates the desired quantity $g(\nabla_X Y, Z)$ on the right.

3. **Apply torsion-freeness to convert misordered $\nabla$ terms to Lie brackets.** $\nabla_Y X = \nabla_X Y - [X, Y]$, $\nabla_Z X = \nabla_X Z - [X, Z]$, $\nabla_Z Y = \nabla_Y Z - [Y, Z]$.
   - *Hint:* This is where torsion-freeness enters. The three substitutions convert all six $\nabla$ terms to expressions involving $\nabla_X Y, \nabla_X Z, \nabla_Y Z$ (with each variable appearing as the second argument once) plus Lie brackets.
   - *Why needed:* Reduces to a single "canonical ordering" of $\nabla$ terms.

4. **Collect terms and extract $g(\nabla_X Y, Z)$.** After substitution, $g(\nabla_X Y, Z)$ appears with coefficient $2$, while the $g(\nabla_X Z, Y)$ and $g(\nabla_Y Z, X)$ terms cancel; the remaining bracket terms form the right side of Koszul.
   - *Hint:* Track the sign on each bracket term carefully — three brackets $[X, Y], [X, Z], [Y, Z]$ with signs $(+, -, -)$.
   - *Why needed:* Yields the formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: $C^\infty$-linearity of the Koszul right-hand side in $Z$
> **Statement:** For fixed $X, Y$, the expression
> $$
> K(Z) := X g(Y, Z) + Y g(X, Z) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X)
> $$
> is $C^\infty(M)$-linear in $Z$: $K(fZ) = f K(Z)$ for $f \in C^\infty(M)$.
>
> **Hint:** Apply Leibniz to each of the three function-derivative terms and to each of the three Lie-bracket terms. The Leibniz corrections all cancel pairwise.
>
> **Why needed:** This is what ensures $K(Z)$ defines a 1-form on $M$ — hence by the [[Def - Musical Isomorphism (Flat and Sharp)|sharp map]] a vector field — which is what allows the *definition* $\nabla_X Y := K(\cdot)^\sharp$ to make sense. Without this linearity, the formula would not produce a vector field, only an $\mathbb{R}$-linear functional on each tangent space.
>
> > [!note]- Full proof
> > Compute $K(fZ)$ term by term:
> > 
> > $X g(Y, fZ) = X(f g(Y, Z)) = X(f)g(Y, Z) + fXg(Y, Z)$.
> > 
> > $Y g(X, fZ) = Y(f)g(X, Z) + fYg(X, Z)$.
> > 
> > $-fZ g(X, Y) = -f Zg(X, Y)$.
> > 
> > $g([X, Y], fZ) = fg([X, Y], Z)$.
> > 
> > $-g([X, fZ], Y) = -g(f[X, Z] + X(f)Z, Y) = -fg([X, Z], Y) - X(f)g(Z, Y)$.
> > 
> > $-g([Y, fZ], X) = -fg([Y, Z], X) - Y(f)g(Z, X)$.
> > 
> > Summing: the $fK(Z)$ pieces give $fK(Z)$. The non-cancelled terms are $X(f)g(Y, Z) + Y(f)g(X, Z) - X(f)g(Z, Y) - Y(f)g(Z, X) = 0$ (each pair cancels). So $K(fZ) = fK(Z)$ as claimed.

> [!note]- Lemma 2: The Koszul formula determines $\nabla$ uniquely (uniqueness of Levi-Civita)
> **Statement:** If $\nabla, \tilde\nabla$ are both torsion-free metric-compatible connections on $(M, g)$, then $\nabla = \tilde\nabla$.
>
> **Hint:** Both connections satisfy the Koszul formula (proved in the main argument), so $g(\nabla_X Y, Z) = g(\tilde\nabla_X Y, Z)$ for every $Z$; non-degeneracy of $g$ gives $\nabla_X Y = \tilde\nabla_X Y$.
>
> **Why needed:** This is the uniqueness half of the fundamental theorem; together with the existence half (Lemma 3), it gives the full statement.
>
> > [!note]- Full proof
> > Apply the Koszul formula to $\nabla$: $2g(\nabla_X Y, Z) = $ RHS of Koszul, expressed in $g$ and Lie brackets. Apply it to $\tilde\nabla$: $2g(\tilde\nabla_X Y, Z) = $ the *same* RHS. So $g(\nabla_X Y, Z) = g(\tilde\nabla_X Y, Z)$ for every $Z$, i.e., $g(\nabla_X Y - \tilde\nabla_X Y, Z) = 0$ for every $Z$. By non-degeneracy of $g$ (every vector that pairs to zero with every $Z$ must be zero), $\nabla_X Y = \tilde\nabla_X Y$. This holds for arbitrary $X, Y$, so $\nabla = \tilde\nabla$. $\blacksquare$

> [!note]- Lemma 3: The Koszul formula defines a torsion-free metric-compatible connection (existence of Levi-Civita)
> **Statement:** Define $\nabla_X Y$ to be the unique vector field with $g(\nabla_X Y, Z) = \tfrac{1}{2}K(Z)$ for all $Z$, where $K(Z)$ is the right side of the Koszul formula. Then $\nabla$ is an affine connection on $TM$ that is torsion-free and metric-compatible.
>
> **Hint:** The well-definedness follows from Lemma 1 (RHS is a 1-form in $Z$) and non-degeneracy of $g$ (1-form yields a unique vector field via the sharp map). Each of the four properties (Leibniz in $Y$, $C^\infty$-linearity in $X$, torsion-freeness, metric-compatibility) is verified by direct computation using the structure of the Koszul formula.
>
> **Why needed:** This is the existence half of the fundamental theorem.
>
> > [!note]- Full proof (sketch)
> > **Well-defined:** Lemma 1 shows $K(\cdot)$ is $C^\infty$-linear in $Z$, hence a 1-form. By non-degeneracy of $g$, there is a unique vector field $V$ with $g(V, Z) = \tfrac{1}{2}K(Z)$ for all $Z$; define $\nabla_X Y := V$.
> >
> > **Tensorial in $X$:** Replace $X$ by $fX$ in the Koszul formula and verify $K^{fX}(Z) = fK^X(Z)$ — a direct calculation similar to Lemma 1, with $f$-corrections cancelling.
> >
> > **Leibniz in $Y$:** Replace $Y$ by $fY$ in the Koszul formula and verify $K^{X, fY}(Z) = X(f)g(Y, Z) + fK^{X, Y}(Z)$, which gives $\nabla_X(fY) = X(f)Y + f\nabla_X Y$ after applying the sharp map.
> >
> > **Torsion-free:** Compute $g(\nabla_X Y - \nabla_Y X, Z) = \tfrac{1}{2}(K^{X, Y}(Z) - K^{Y, X}(Z))$. The function-derivative terms $X g(Y, Z) + Y g(X, Z) - Z g(X, Y)$ are symmetric in $X, Y$ except for the middle one — actually $Xg(Y, Z) + Yg(X, Z)$ is symmetric in $X, Y$ and $-Zg(X, Y) = -Zg(Y, X)$ is symmetric in $X, Y$; so the function-derivative part *is* symmetric. The bracket terms: $g([X, Y], Z) \to g([Y, X], Z) = -g([X, Y], Z)$; $-g([X, Z], Y) \to -g([Y, Z], X)$; $-g([Y, Z], X) \to -g([X, Z], Y)$. Subtracting: $2g([X, Y], Z)$, so $\nabla_X Y - \nabla_Y X = [X, Y]$, i.e., torsion-free.
> >
> > **Metric-compatible:** Compute $g(\nabla_X Y, Z) + g(Y, \nabla_X Z) = \tfrac{1}{2}(K^{X, Y}(Z) + K^{X, Z}(Y))$. Expand both terms and verify the result is $Xg(Y, Z)$ — a careful term-by-term computation where the bracket terms cancel via the antisymmetry of the Lie bracket.

---

# Formal Proof

> [!note]- Complete formal proof
> **Proof of the Koszul Formula.** Let $\nabla$ be a torsion-free metric-compatible connection on $(M, g)$. Metric-compatibility gives, for any $X, Y, Z$:
> $$
> X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z). \tag{$\ast_1$}
> $$
> Cyclically permuting $(X, Y, Z) \to (Y, Z, X) \to (Z, X, Y)$:
> $$
> Y g(Z, X) = g(\nabla_Y Z, X) + g(Z, \nabla_Y X), \tag{$\ast_2$}
> $$
> $$
> Z g(X, Y) = g(\nabla_Z X, Y) + g(X, \nabla_Z Y). \tag{$\ast_3$}
> $$
> Form the combination $(\ast_1) + (\ast_2) - (\ast_3)$:
> $$
> X g(Y, Z) + Y g(Z, X) - Z g(X, Y) = \bigl[g(\nabla_X Y, Z) + g(Y, \nabla_X Z)\bigr] + \bigl[g(\nabla_Y Z, X) + g(Z, \nabla_Y X)\bigr] - \bigl[g(\nabla_Z X, Y) + g(X, \nabla_Z Y)\bigr].
> $$
> Now apply torsion-freeness to each $\nabla$-term in which the differentiator is "swapped" relative to $\nabla_X Y$:
> $$
> \nabla_Y X = \nabla_X Y - [X, Y], \qquad \nabla_Z X = \nabla_X Z - [X, Z], \qquad \nabla_Z Y = \nabla_Y Z - [Y, Z].
> $$
> Substituting:
> $$
> g(Z, \nabla_Y X) = g(Z, \nabla_X Y) - g(Z, [X, Y]) = g(\nabla_X Y, Z) - g([X, Y], Z),
> $$
> $$
> g(Y, \nabla_X Z) \text{ stays as is},
> $$
> $$
> g(\nabla_Y Z, X) \text{ stays as is},
> $$
> $$
> g(\nabla_Z X, Y) = g(\nabla_X Z - [X, Z], Y) = g(\nabla_X Z, Y) - g([X, Z], Y),
> $$
> $$
> g(X, \nabla_Z Y) = g(X, \nabla_Y Z - [Y, Z]) = g(\nabla_Y Z, X) - g([Y, Z], X).
> $$
> Plugging back into the sum:
> $$
> X g(Y, Z) + Y g(Z, X) - Z g(X, Y) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z) + g(\nabla_Y Z, X) + g(\nabla_X Y, Z) - g([X, Y], Z) - \bigl[g(\nabla_X Z, Y) - g([X, Z], Y)\bigr] - \bigl[g(\nabla_Y Z, X) - g([Y, Z], X)\bigr].
> $$
> The terms $g(Y, \nabla_X Z) = g(\nabla_X Z, Y)$ and $g(\nabla_Y Z, X) = g(X, \nabla_Y Z)$ cancel against the corresponding $-g(\nabla_X Z, Y)$ and $-g(\nabla_Y Z, X)$ terms. The two surviving $g(\nabla_X Y, Z)$ combine to $2g(\nabla_X Y, Z)$. The bracket terms collect to $-g([X, Y], Z) + g([X, Z], Y) + g([Y, Z], X)$. Rearranging:
> $$
> 2g(\nabla_X Y, Z) = X g(Y, Z) + Y g(Z, X) - Z g(X, Y) + g([X, Y], Z) - g([X, Z], Y) - g([Y, Z], X). \qquad\blacksquare
> $$

---

# Cross-Field Exercise Suggestions

**1. Bi-invariant Lie groups.** Use the Koszul formula to show that on a Lie group $G$ with bi-invariant Riemannian metric, the Levi-Civita connection on left-invariant fields is $\nabla_X Y = \tfrac{1}{2}[X, Y]$. Use this to conclude geodesics through the identity are one-parameter subgroups. (Standard problem in Lie-group geometry.)

**2. Killing fields and conserved quantities.** A vector field $K$ is **Killing** if $\mathcal{L}_K g = 0$, equivalently $\nabla_i K_j + \nabla_j K_i = 0$. Use the Koszul formula to show that $g(\dot\gamma, K)$ is constant along any geodesic $\gamma$ of the Levi-Civita connection. This is the **Noether-type conservation law for spacetime symmetries** in general relativity; in Schwarzschild it gives the conserved energy and angular momentum used in computing perihelion precession.

**3. The connection on a warped product.** For a warped product metric $g = g_B + f(b)^2 g_F$ on a product manifold $B \times F$, the Koszul formula on horizontal and vertical vector fields gives explicit formulas for the Levi-Civita connection that decompose the curvature into base, fibre, and mixing pieces. This is the standard technique for computing curvature of cosmological FRW spacetimes (where $B = \mathbb{R}_t$ and $F$ is a constant-curvature 3-space) and of Schwarzschild (which is *not* a warped product but has a similar decomposable structure).

**4. The Koszul formula on a complex manifold with Kähler metric.** For a Kähler manifold $(M, g, J)$ with complex structure $J$, the metric and complex structure are compatible ($g(JX, JY) = g(X, Y)$) and the Kähler 2-form $\omega(X, Y) = g(JX, Y)$ is closed. The Koszul formula, combined with the Kähler condition, gives that the Levi-Civita connection is also complex-linear ($\nabla J = 0$), and in holomorphic coordinates the Christoffel symbols have only the "pure" components $\Gamma^k_{ij}$ (with all indices either holomorphic or antiholomorphic). This is the input to **Hodge theory on Kähler manifolds** and to the **Calabi conjecture / Yau's theorem**.

---

# Bridges

- **[[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)]]** — The Koszul formula is the proof engine: it gives uniqueness (any torsion-free metric-compatible connection satisfies it) and existence (defining $\nabla_X Y$ by the formula and the sharp map yields a connection that one verifies is torsion-free and metric-compatible). The relationship is: Koszul = "explicit formula for the unique Levi-Civita connection".

- **[[Def - Christoffel Symbols|Christoffel formula]]** — Specialising Koszul to a coordinate frame and using $[\partial_i, \partial_j] = 0$ gives the explicit coordinate formula $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. So the Christoffel formula is a special case of Koszul, applied to coordinate vector fields. Most practical computations use the Christoffel formula; the Koszul formula is for invariant or Lie-group-theoretic settings.

- **[[Thm - Cartan's First Structural Equation]]** — On an orthonormal frame, the same uniqueness-from-two-conditions argument plays out via Cartan's first equation $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ (torsion-free) combined with antisymmetry $\omega^a{}_b + \omega^b{}_a = 0$ (metric-compatible). The two conditions together determine $\omega^a{}_b$ uniquely from the coframe $\sigma^a$ — exactly as Koszul determines $\nabla_X Y$ uniquely from $g$ and Lie brackets. Cartan's structural equations are the moving-frame version of the Koszul argument.

- **The first variation formula for arc length** — The Koszul formula is the structural identity that delivers the first variation formula for the length functional, $\delta L = -\int g(\ddot\gamma + \Gamma\text{-correction}, V)\,dt$, whose vanishing characterises geodesics. This is the bridge between the connection-theoretic and variational pictures of "shortest path" and is the input to the second variation formula and the Jacobi equation in [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

- **The bi-invariant Lie-group simplification** — On a bi-invariantly-metric Lie group, the Koszul formula collapses to $\nabla_X Y = \tfrac{1}{2}[X, Y]$ on left-invariant fields. This is the most striking "consequence of Koszul" and underlies the entire harmonic-analysis structure on compact Lie groups: the Peter-Weyl theorem, the heat kernel, the spectral decomposition of the Laplacian, the gauge theory of compact groups. The bridge to gauge theory: a bi-invariant Lie group is the simplest example of a "homogeneous space with a canonical connection", and the Koszul formula gives the connection explicitly.

---

# Unlocked by This

> [!tip] The Fundamental Theorem of Riemannian Geometry *(from Riemannian Geometry)*
> The Koszul formula is the technical heart of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]]: every Riemannian (or semi-Riemannian) manifold has a unique torsion-free metric-compatible connection — the Levi-Civita connection. Uniqueness is immediate from Koszul plus non-degeneracy of $g$; existence is by defining $\nabla$ via Koszul and the sharp map, then verifying the connection axioms. This makes the entire subsequent development of Riemannian geometry canonical.

> [!tip] The Christoffel Formula in Coordinates *(from Riemannian Geometry)*
> Specialising Koszul to a coordinate frame and using $[\partial_i, \partial_j] = 0$ gives the [[Def - Christoffel Symbols|Christoffel formula]] $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. This is the most-used computational form of the Levi-Civita connection — every concrete calculation in Riemannian geometry or general relativity begins by computing these symbols from the metric.
