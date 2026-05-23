---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Singular Homology"
  - "Def - Singular Chain"
tags: [geometry, algebraic-topology, homology]
---

# Notation

$M$ is a topological space, $G$ an abelian coefficient group. $C_p(M; G)$, $\partial$, $H_p(M; G)$ as in [[Def - Singular Homology]]. We adjoin a "degree $-1$" copy of $G$ to the chain complex, denoted $C_{-1}(M; G) = G$, with a map called the **augmentation**.

This is a compound page: it defines two interlocking notions — the augmentation map $\varepsilon$ and the reduced homology $\tilde H_0$ — because they are introduced together and reduced homology is defined precisely as the kernel of $\varepsilon$.

---

# Axiom Motivation

Plain singular homology has the inconvenience that $H_0(M; G) = G$ for *every* non-empty path-connected space $M$ — including a single point. So the homology of a point is non-trivial in degree zero, and many "natural" exact sequences and isomorphisms get awkwardly off-by-one. The augmentation and reduced homology are bookkeeping devices that shift this trivial constant out of the way, leaving a homology theory that vanishes in *all* degrees on a point.

**Why have an augmentation at all?** The chain complex
$$
\cdots \to C_1(M; G) \xrightarrow{\partial} C_0(M; G) \to 0
$$
terminates at $C_0$. The boundary map $\partial : C_0 \to C_{-1} = 0$ is trivially zero, so every $0$-chain is a $0$-cycle. The boundary $\partial : C_1 \to C_0$ has image $B_0$, consisting of chains of the form $\partial \gamma = q - p$ for a path $\gamma$ from $p$ to $q$ — that is, $B_0$ consists of $0$-chains $\sum g_i p_i$ that, on each path component, have coefficients summing to zero. The quotient $H_0 = C_0 / B_0$ is then "one copy of $G$ per path component" — the coefficient sum on each component is the surviving invariant.

To make a connected space have $H_0 = 0$, we want to quotient out the diagonal copy of $G$ inside $C_0 = G \cdot \{\text{points of }M\}$. The cleanest way is to *extend* the chain complex with one more group $C_{-1} = G$ and a map $\varepsilon : C_0 \to G$ that detects exactly the "coefficient sum" we want to quotient out. This map is the augmentation.

**Why $\varepsilon(\sum g_i p_i) = \sum g_i$?** Because the coefficient sum is precisely the invariant that survives in $H_0(M; G)$ — equivalently, it is the image of a $0$-chain under the natural map "forget the points, remember the total coefficient." The augmentation is the universal such forgetting map. For a path component of $M$, all points contribute equally to $H_0$ (any two are connected by a path, hence homologous as $0$-chains), and the augmentation reads off the coefficient sum that distinguishes different points-with-coefficients.

**Why $\varepsilon \circ \partial = 0$?** Because $\partial \gamma = q - p$ for a $1$-simplex (path) $\gamma$ from $p$ to $q$, and $\varepsilon(q - p) = 1 - 1 = 0$. More generally, $\partial$ of any $1$-chain has all coefficient sums equal to zero, by direct computation. So $\varepsilon$ vanishes on the image of $\partial : C_1 \to C_0$, which means $\varepsilon$ descends to a map $\varepsilon : H_0(M; G) \to G$ on homology.

**Why define reduced homology as $\tilde H_0 = \ker \varepsilon$?** Because this is the quotient $H_0 / (\text{the trivial constant})$ that vanishes on connected spaces. Specifically: for a path-connected $M$, $H_0(M; G) = G$ with generator any point $p$, and $\varepsilon$ sends $g \cdot p \mapsto g$, so $\varepsilon$ is an isomorphism and $\tilde H_0 = \ker \varepsilon = 0$. For a disconnected $M$ with $k$ components, $H_0 = G^k$ with one generator per component, and $\varepsilon : G^k \to G$ sums the coefficients, so $\tilde H_0 = \ker \varepsilon \cong G^{k-1}$ — one less than the unreduced version, the "off-diagonal" components.

**Why is this useful?** Two reasons. First, reduced homology gives a cleaner Mayer–Vietoris sequence and cleaner long exact sequences of pairs — the "augmentation gap" between $H_0$ of a space and $H_0$ of a point disappears. Second, reduced homology makes the homology of a wedge sum (one-point union) of spaces compute as a direct sum of the reduced homologies: $\tilde H_p(X \vee Y) = \tilde H_p(X) \oplus \tilde H_p(Y)$, with no off-by-one correction. Without reducing, the corresponding formula has an awkward correction term.

For higher degrees the augmentation is invisible: $\tilde H_p(M; G) = H_p(M; G)$ for all $p \geq 1$, because the augmentation only modifies degree zero. Reduced homology is a one-step shift in the bookkeeping, agreeing with ordinary homology everywhere except in degree $0$.

---

# The Definition

Let $M$ be a topological space, $G$ an abelian coefficient group. The **augmentation map** is the homomorphism
$$
\varepsilon : C_0(M; G) \to G, \qquad \varepsilon\!\left( \sum_i g_i p_i \right) \;=\; \sum_i g_i,
$$
where $p_i \in M$ are points and $g_i \in G$ are coefficients. Equivalently, $\varepsilon$ is the unique $G$-linear extension of the constant map "every point $\mapsto 1 \in \mathbb{Z}$" combined with the $G$-action.

The augmentation satisfies $\varepsilon \circ \partial = 0$: for any $1$-chain $c = \sum a_i \gamma_i$ (with $\gamma_i$ singular $1$-simplices, i.e. paths), $\partial \gamma_i = q_i - p_i$ where $p_i, q_i$ are the endpoints, so $\varepsilon(\partial c) = \sum a_i (1 - 1) = 0$.

Consequently $\varepsilon$ descends to a map
$$
\varepsilon : H_0(M; G) \to G.
$$
This map is surjective whenever $M$ is non-empty (choose any point $p \in M$; then $\varepsilon([1 \cdot p]) = 1$), and its kernel is the **reduced $0$-th singular homology**:
$$
\tilde H_0(M; G) \;=\; \ker\bigl(\varepsilon : H_0(M; G) \to G\bigr).
$$

There is a short exact sequence
$$
0 \to \tilde H_0(M; G) \to H_0(M; G) \xrightarrow{\varepsilon} G \to 0,
$$
which splits (the augmentation has the section $g \mapsto g \cdot [p]$ for any chosen point $p$), so $H_0(M; G) \cong \tilde H_0(M; G) \oplus G$.

For $p \geq 1$, the **reduced singular homology** is defined to equal the ordinary singular homology:
$$
\tilde H_p(M; G) \;=\; H_p(M; G), \qquad p \geq 1.
$$

The full reduced homology theory $\tilde H_*$ is a covariant functor $\mathbf{Top} \to \mathbf{Ab}$, satisfying $\tilde H_*(\text{point}; G) = 0$ in all degrees — including $\tilde H_0(\text{point}) = 0$.

Equivalently, reduced singular homology is the homology of the **augmented chain complex**
$$
\cdots \to C_2(M; G) \xrightarrow{\partial} C_1(M; G) \xrightarrow{\partial} C_0(M; G) \xrightarrow{\varepsilon} G \to 0,
$$
which has a degree $-1$ slot equal to $G$ and the augmentation as the boundary map at the bottom.

---

# Relate to Other Fields / Compression

Reduced homology is **ordinary homology shifted to make a point the trivial object**. It is the natural normalisation that comes from working with **pointed spaces** $(X, x_0)$ rather than unpointed spaces. In pointed topology, the basepoint should contribute nothing to invariants, and reduced homology achieves this.

In homological algebra, the augmentation is an instance of the more general **augmentation of a chain complex**: given a chain complex $C_\bullet$ and a surjective chain map $C_0 \to A$ to a module $A$, augmenting the complex with $A$ in degree $-1$ shifts the bottom of the chain complex by one. This is the central technique in defining group cohomology, where the standard chain complex is augmented to recognise that $\mathbb{Z}$ (with trivial $G$-action) is the "trivial module."

In topology more broadly, the augmentation appears in the construction of the **reduced suspension** $\Sigma X = (X \times [0,1])/(X \times \{0,1\} \cup \{x_0\} \times [0,1])$, where the basepoint identification is what makes the suspension functor land in pointed spaces. The relation $\tilde H_p(\Sigma X) = \tilde H_{p-1}(X)$ — the **suspension isomorphism** — is a key invariant of pointed homology theories.

**True name:** the augmentation is the **coefficient-sum projection** $C_0 \to G$, and reduced homology is the **homology of the augmented complex**, equivalently "ordinary homology minus the trivial copy of $G$ contributed by any single point." It is one-step bookkeeping, not a different theory.

---

# Examples / Corollaries

**$\tilde H_*(\text{point}; G) = 0$ in all degrees.** For a single point $M = \{p\}$, $C_0(\{p\}; G) = G$ (one generator, the constant $0$-simplex at $p$), and $\varepsilon : G \to G$ is the identity. So $H_0 = G$, $\varepsilon$ is an isomorphism, $\tilde H_0 = \ker \varepsilon = 0$. All higher homologies are zero (singular and reduced agree there).

**$\tilde H_*(S^n; G)$.** For a sphere, $\tilde H_p(S^n; G) = G$ if $p = n$ and zero otherwise. (Unreduced: $H_0 = G$ in degree zero as well.) The "shifted" pattern $\tilde H_p(S^n) = G[\delta_{pn}]$ makes the suspension isomorphism $\tilde H_p(S^{n+1}) = \tilde H_{p-1}(S^n)$ visible — reduced homology of spheres is concentrated in exactly one degree.

**$\tilde H_0$ of a disconnected space.** For $M$ with $k$ path components, $H_0(M; G) = G^k$ and $\varepsilon : G^k \to G$ is the sum map $(g_1, \dots, g_k) \mapsto g_1 + \cdots + g_k$. So $\tilde H_0(M; G) = \ker(\text{sum}) = \{(g_1, \dots, g_k) : \sum g_i = 0\} \cong G^{k-1}$. Reduced $H_0$ counts "off-diagonal" components — for a space of $k$ components, reduced $H_0$ has rank $k - 1$.

**Wedge sum.** For pointed spaces $(X, x_0)$ and $(Y, y_0)$, the wedge $X \vee Y = (X \sqcup Y)/(x_0 \sim y_0)$ has
$$
\tilde H_p(X \vee Y; G) \;=\; \tilde H_p(X; G) \oplus \tilde H_p(Y; G).
$$
The reduced version has no off-by-one correction; the unreduced version would have to subtract one copy of $G$ from $H_0$ to avoid double-counting the merged basepoint.

**Suspension isomorphism.** For any pointed space $(X, x_0)$, the (reduced) suspension $\Sigma X$ satisfies
$$
\tilde H_p(\Sigma X; G) \;=\; \tilde H_{p-1}(X; G).
$$
This is one of the foundational identities of pointed homotopy theory and makes reduced homology a "stable" invariant — well-suited to the suspension-spectrum framework of stable homotopy theory.

**Is NOT an instance: the augmentation as a homology operation in higher degrees.** The augmentation only modifies degree zero; it does not change $H_p$ for $p \geq 1$. So "augmenting" $H_2$ or $H_3$ is meaningless — those groups are already what they should be.

**Corollary (when reduced and unreduced agree).** For a path-connected non-empty space $M$, $H_0(M; G) = G$ and $\varepsilon$ is an isomorphism, so $\tilde H_0(M; G) = 0$. In this case the only difference between $H_*$ and $\tilde H_*$ is the trivial $\tilde H_0 = 0$ versus $H_0 = G$ in degree zero. For path-disconnected spaces, reduced homology of degree zero is non-trivial, and reduced versus unreduced really do differ.

**Corollary (long exact sequence).** The long exact sequence of a pair $(X, A)$ in singular homology has the form $\cdots \to H_p(A) \to H_p(X) \to H_p(X, A) \to H_{p-1}(A) \to \cdots$ ending in $H_0(A) \to H_0(X) \to H_0(X, A) \to 0$. The reduced version $\tilde H_p$ gives the cleaner long exact sequence with the sequence ending one slot lower: $\cdots \to \tilde H_0(A) \to \tilde H_0(X) \to H_0(X, A) \to 0$, with the $H_0$-to-$H_0$ comparison being a homomorphism of reduced groups rather than augmented ones.

**Calibration check.** If you have understood the definition you should be able to: (1) compute $\tilde H_0$ and $\tilde H_*$ of a discrete space of three points; (2) verify the suspension isomorphism for $X = S^0$ (two points): $\Sigma S^0 = S^1$, so $\tilde H_1(S^1) = \tilde H_0(S^0) = \mathbb{Z}$; (3) explain why $\tilde H_p$ is the right normalisation for the wedge-sum formula.

---

# Unlocked by This

> [!tip] Pointed Homology Theories *(from Algebraic Topology)*
> Reduced homology is the natural homology theory on the category of **pointed spaces** $\mathbf{Top}_*$, where morphisms preserve basepoints. In pointed topology, the basepoint should be invisible to invariants, and reduced homology achieves this. Every "stable" invariant — stable homotopy groups, K-theory, cobordism — is naturally a pointed-space invariant and is most cleanly stated in reduced form.

> [!tip] Suspension Isomorphism and the Stable Range *(from Algebraic Topology)*
> The relation $\tilde H_p(\Sigma X) = \tilde H_{p-1}(X)$ is the **suspension isomorphism**, the foundational property that makes reduced homology a stable invariant. Iterating, $\tilde H_p(\Sigma^k X) = \tilde H_{p-k}(X)$. This is the simplest instance of the **Freudenthal suspension theorem**: the suspension of $X$ becomes increasingly "stable" as one applies $\Sigma$ repeatedly, and the stable invariants (such as stable homotopy groups) are exactly the limits of these increasingly-stable behaviors.

> [!tip] **Cellular Homology and the Reduced Chain Complex** *(from Algebraic Topology)*
> For a CW complex $X$ with basepoint $x_0$ in the $0$-skeleton, the cellular chain complex computes singular homology, and the **reduced cellular chain complex** (with the basepoint $0$-cell removed) computes reduced singular homology. This is why reduced homology is computationally natural for pointed CW complexes — it just means "ignore the basepoint cell."
