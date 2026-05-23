---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Singular Homology"
  - "Thm - Homotopy Invariance of Singular Homology"
  - "Def - Chain Map and Chain Homotopy"
tags: [geometry, algebraic-topology, mayer-vietoris]
---

# Notation

$M$ is a topological space, $U, V \subseteq M$ open with $M = U \cup V$. $G$ is an abelian coefficient group.

$i_U : U \cap V \hookrightarrow U$, $i_V : U \cap V \hookrightarrow V$, $j_U : U \hookrightarrow M$, $j_V : V \hookrightarrow M$ are the inclusions.

$\delta : H_p(M; G) \to H_{p-1}(U \cap V; G)$ is the **Mayer–Vietoris connecting homomorphism**, constructed below.

---

# Statement

> **Theorem (Mayer–Vietoris for Singular Homology).** Let $M$ be a topological space with an open cover $M = U \cup V$. For every $p \geq 0$ and every abelian group $G$, there is a long exact sequence
> $$
> \cdots \to H_p(U \cap V; G) \xrightarrow{(i_{U*}, i_{V*})} H_p(U; G) \oplus H_p(V; G) \xrightarrow{j_{U*} - j_{V*}} H_p(M; G) \xrightarrow{\delta} H_{p-1}(U \cap V; G) \to \cdots
> $$
> ending at $\cdots \to H_0(M; G) \to 0$ (or, in reduced form, ending one slot lower).
>
> The maps $(i_{U*}, i_{V*})$ and $j_{U*} - j_{V*}$ are induced by inclusion (with the natural sign convention to make exactness work); $\delta$ is the **connecting homomorphism**.

The sequence is the inductive engine for every explicit computation of singular homology. The proof relies on a subtle technical fact: the chain complex of "small" singular simplices (each contained in $U$ or in $V$) is chain-homotopy equivalent to the full chain complex, allowing us to control how cycles "split" across the cover.

---

# Motivation

To compute $H_*(M)$ for a complicated space $M$, the best strategy is to decompose $M$ into simpler pieces whose homology is known, and then assemble the local data into global information. The Mayer–Vietoris sequence is the precise accounting of this assembly.

Imagine you want to compute $H_*(S^2)$. Cover $S^2$ by the open upper hemisphere $U$ (slightly thickened to include the equator) and the open lower hemisphere $V$. Both $U$ and $V$ are contractible (each deformation-retracts onto its central point), so $H_*(U) = H_*(V) = H_*(\text{point})$. Their intersection $U \cap V$ is a thickened equator, homotopy equivalent to $S^1$. The Mayer–Vietoris sequence then connects $H_*(S^2)$ to $H_*(\text{point}) \oplus H_*(\text{point})$ and $H_*(S^1)$, and exactness determines $H_*(S^2)$ uniquely.

More generally, the Mayer–Vietoris sequence enables an inductive computation: $H_*(S^n)$ from $H_*(S^{n-1})$, $H_*(T^n)$ from $H_*(T^{n-1})$, $H_*(\mathbb{CP}^n)$ from $H_*(\mathbb{CP}^{n-1})$. The base case is usually a contractible space or a discrete space; each inductive step uses Mayer–Vietoris to add one dimension.

The exactness of the sequence is the algebraic incarnation of "global homology equals local homology plus gluing data." The maps $H_*(U) \oplus H_*(V) \to H_*(M)$ assemble local cycles into global cycles by inclusion; the connecting map $\delta : H_p(M) \to H_{p-1}(U \cap V)$ records "the mismatch between $U$ and $V$ on the overlap," which is itself a $(p-1)$-dimensional homology class. Exactness ensures that the global cycles that don't come from local data are exactly the ones that the connecting map sends to non-trivial overlap classes.

There is a parallel **Mayer–Vietoris for de Rham cohomology** (Frankel §13.3a, our [[Thm - The Mayer-Vietoris Sequence]] from `Differential Geometry X`) and the two are isomorphic via the de Rham theorem. The singular version proven here is the topological analogue; the de Rham version on smooth manifolds is the smooth analogue. Both work, and they compute the same answer over $\mathbb{R}$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *an open cover $M = U \cup V$ by two open sets.*

The first disguised source is **a finite "good cover" of $M$.** Property $B$: a finite open cover $\{U_1, \dots, U_n\}$ of $M$ such that every finite intersection $U_{i_1} \cap \cdots \cap U_{i_k}$ is contractible (or has known homology). The bridge: iterate Mayer–Vietoris starting with $U = U_1 \cup \cdots \cup U_{n-1}$ and $V = U_n$, using known homologies of $U \cap V$ (which is a smaller cover problem). *Example application:* the sphere $S^n$ admits a cover by $n + 1$ contractible open sets (slight thickenings of the faces of an inscribed simplex), allowing iterative computation of $H_*(S^n)$.

The second disguised source is **a CW complex decomposition.** Property $B$: $M$ is built by attaching cells of increasing dimension. The bridge: each cell attachment is a "wedge along a sphere" operation, which Mayer–Vietoris turns into an exact sequence relating the homology before and after attachment. *Example application:* every CW homology computation (computing $H_*$ of $\mathbb{RP}^n$, $\mathbb{CP}^n$, $\text{Grassmannian}$) is an iterated Mayer–Vietoris.

The third disguised source is **a manifold with a hypersurface separating it into two pieces.** Property $B$: a closed embedded $(n-1)$-submanifold $\Sigma \subset M$ that separates $M$ into two pieces $M_+, M_-$ with $\partial M_\pm = \Sigma$. The bridge: take $U, V$ to be small open neighborhoods of $M_\pm$, with $U \cap V$ a tubular neighborhood of $\Sigma$ (homotopy equivalent to $\Sigma$). The Mayer–Vietoris sequence then connects $H_*(M)$ to $H_*(M_+) \oplus H_*(M_-)$ and $H_*(\Sigma)$. *Example application:* this is how one computes the homology of a connected sum $M_1 \# M_2$ from $H_*(M_1)$ and $H_*(M_2)$.

**Targets (Output Amplification)**

The conclusion $C$: *the long exact sequence connecting $H_*(U \cap V)$, $H_*(U) \oplus H_*(V)$, $H_*(M)$ by inclusion maps and the connecting homomorphism $\delta$.*

Combine $C$ with **vanishing of $H_*(U)$ and $H_*(V)$ in positive degrees.** Property $D$: $U, V$ are both contractible. Then $H_p(U) = H_p(V) = 0$ for $p \geq 1$, and the Mayer–Vietoris sequence simplifies to
$$
0 \to H_p(M) \xrightarrow{\delta} H_{p-1}(U \cap V) \to 0 \qquad \text{for } p \geq 2.
$$
The further result $E$: $H_p(M) \cong H_{p-1}(U \cap V)$ for $p \geq 2$. This is the **suspension isomorphism** in disguise — and it's how the inductive computation $H_*(S^n)$ in terms of $H_*(S^{n-1})$ works.

Combine $C$ with **a Lie group acting on $M$.** Property $D$: a continuous action of a Lie group $K$ on $M$ that preserves the cover $\{U, V\}$. The Mayer–Vietoris sequence becomes a sequence of $K$-modules, and equivariant cohomology refinements (with $K$-coefficients) compute richer invariants of the action.

Combine $C$ with **the five lemma.** $D$: a continuous map $f : M \to N$ inducing a comparison of Mayer–Vietoris sequences (one for the cover $\{U, V\}$ of $M$, one for the image cover $\{f(U), f(V)\}$ of $N$). If $f$ induces isomorphisms on $H_*(U)$, $H_*(V)$, and $H_*(U \cap V)$, then by the **five lemma** of homological algebra, $f$ induces an isomorphism on $H_*(M)$. The further result $E$: comparisons of homology via Mayer–Vietoris reduce to comparisons of local pieces. This is the central technique in the proof of the de Rham theorem.

---

# Why Is It True

**The single sentence: barycentric subdivision is a chain-homotopy equivalence from the full singular chain complex of $M$ to the subcomplex of "small" chains contained in either $U$ or $V$, and the long exact sequence then follows from the short exact sequence of chain complexes $0 \to C_*^{U \cap V} \to C_*^U \oplus C_*^V \to C_*^{U + V} \to 0$ plus a snake-lemma argument.**

The intuition has two layers.

**Layer 1: at the chain level, every cycle splits.** The chain group $C_p^{U + V}(M; G)$ of "small" chains — those each of whose simplices lies entirely in $U$ or entirely in $V$ — sits inside $C_p(M; G)$. By **barycentric subdivision**, every singular simplex can be subdivided into smaller simplices until each one is small enough to fit inside $U$ or $V$ (by a Lebesgue-number argument applied to the open cover). The subdivision is a chain homotopy equivalence, so $C_*^{U + V}$ computes the same homology as $C_*(M)$. This is the technical heart of Mayer–Vietoris and is non-trivial.

**Layer 2: the small chain complex sits in a short exact sequence.** With $C_*^{U + V}$ as the target, we have a short exact sequence
$$
0 \to C_*(U \cap V; G) \xrightarrow{(i_U, i_V)} C_*(U; G) \oplus C_*(V; G) \xrightarrow{j_U - j_V} C_*^{U+V}(M; G) \to 0.
$$
Exactness on the left: a chain in $U \cap V$ injects diagonally into both $C_*(U)$ and $C_*(V)$. Exactness in the middle: a chain $(\alpha, \beta) \in C_*(U) \oplus C_*(V)$ maps to $j_U(\alpha) - j_V(\beta) = 0$ in $C^{U+V}$ exactly when $\alpha = \beta$ (using the same chain in $U \cap V$). Exactness on the right: every small chain in $M$ splits as a sum of a $U$-supported piece and a $V$-supported piece.

**Layer 3: the snake lemma (or zigzag) produces the long exact sequence in homology.** A short exact sequence of chain complexes induces a long exact sequence in homology, via the standard snake-lemma argument: the connecting homomorphism $\delta : H_p \to H_{p-1}$ comes from "lifting a cycle to a preimage, taking its boundary, and observing the boundary lives in the kernel of the left map." This is exactly the Mayer–Vietoris connecting map: given a homology class $[c] \in H_p(M)$, lift to a small chain (using barycentric subdivision), write it as $c = c_U + c_V$ with $c_U \in C_p(U)$ and $c_V \in C_p(V)$, take $\partial c_U \in C_{p-1}(U)$. Since $\partial c = 0$, we have $\partial c_U = -\partial c_V$, and so $\partial c_U \in C_{p-1}(U \cap V)$. Its homology class is $\delta[c]$.

The proof is therefore split into (a) the technical lemma that barycentric subdivision is chain-homotopy equivalent to the identity (the "subdivision operator" $S$ and its chain homotopy back to $\mathrm{id}$ are constructed explicitly), and (b) the snake-lemma argument from the short exact sequence of chain complexes. Together these give the long exact sequence.

---

# What Makes This Hard

The conceptual difficulty is recognising that **subdivision is the key**: the obvious short exact sequence $0 \to C_*(U \cap V) \to C_*(U) \oplus C_*(V) \to C_*(M) \to 0$ at the level of full chain complexes is *not* exact — the rightmost map fails surjectivity because a general singular simplex $\sigma : \Delta^p \to M$ might not be contained in $U$ or in $V$ alone (its image could span both). The fix is to restrict to the small chain complex $C_*^{U+V}$, but proving that this restriction does not change the homology requires the subdivision argument.

The most common error is to skip this step and assume the obvious sequence is exact. Hatcher's proof (§2.2) carefully addresses this with the **small-chain theorem** (Proposition 2.21 in Hatcher) before deducing Mayer–Vietoris.

The other non-obvious step is the explicit construction of the connecting homomorphism $\delta$. It is "lift, take boundary, observe it lives in the intersection" — but verifying this gives a well-defined map (independent of the lift chosen) requires a small commutative-diagram check.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** (1) Show that the inclusion of the "small chain complex" $C_*^{U+V}$ into the full chain complex $C_*(M)$ is a chain-homotopy equivalence, using barycentric subdivision. (2) Write down the short exact sequence of chain complexes $0 \to C_*(U \cap V) \to C_*(U) \oplus C_*(V) \to C_*^{U+V}(M) \to 0$ and verify exactness. (3) Apply the snake lemma (or the zigzag lemma) to get the long exact sequence in homology.

**Subgoal decomposition:**

1. **Construct the barycentric subdivision operator $S : C_*(M) \to C_*(M)$.** For each singular simplex $\sigma : \Delta^p \to M$, $S(\sigma)$ is the alternating sum of the simplices in the barycentric subdivision of $\Delta^p$ (pre-composed with $\sigma$).
   - *Hint:* The barycentric subdivision of $\Delta^p$ partitions it into $(p+1)!$ smaller simplices, each having the barycenter $b$ and a chain of vertices.
   - *Why needed:* This is the subdivision operator that shrinks chains until they fit inside cover elements.

2. **Verify $S$ is a chain homotopy equivalence.** Construct an explicit chain homotopy $T : C_*(M) \to C_{*+1}(M)$ with $\mathrm{id} - S = \partial T + T \partial$. Hence $S_* = \mathrm{id}$ on homology.
   - *Hint:* $T$ is constructed inductively, with $T(\sigma)$ being a "cone" of $\sigma$ from the barycenter — a $(p+1)$-chain whose boundary involves $\sigma$ and its subdivision.
   - *Why needed:* This shows that subdivision does not change homology.

3. **Iterate to make chains "small."** For any singular chain $c$ on $M$, after applying $S$ sufficiently many times, every simplex in $S^n c$ has diameter less than the Lebesgue number of the cover $\{U, V\}$, hence lies entirely in $U$ or in $V$. So $S^n c \in C_*^{U+V}(M)$.
   - *Hint:* The Lebesgue number lemma applied to a compact triangulated standard simplex.
   - *Why needed:* This shows every homology class on $M$ has a representative in the small chain complex.

4. **State the small-chain theorem.** The inclusion $C_*^{U+V}(M) \hookrightarrow C_*(M)$ is a chain-homotopy equivalence; hence $H_*^{U+V}(M) = H_*(M)$.
   - *Hint:* Steps 2 and 3 together give this — the subdivision provides an inverse chain map up to chain homotopy.
   - *Why needed:* This is the technical foundation enabling the rest of the proof.

5. **Write down the short exact sequence of small chain complexes.**
   $$
   0 \to C_*(U \cap V; G) \xrightarrow{(i_U, i_V)} C_*(U; G) \oplus C_*(V; G) \xrightarrow{j_U - j_V} C_*^{U+V}(M; G) \to 0
   $$
   Verify each spot is exact.
   - *Hint:* Left exact: a chain in $U \cap V$ injects via $\sigma \mapsto (\sigma, \sigma)$. Middle exact: $(\alpha, \beta) \mapsto j_U(\alpha) - j_V(\beta)$ vanishes iff $\alpha = \beta$ in the overlap. Right exact: every small chain is a sum of a $U$-piece and a $V$-piece (after possibly subdividing or splitting overlapping simplices).
   - *Why needed:* This is the algebraic input to the snake lemma.

6. **Apply the snake lemma to get the long exact sequence in homology.**
   - *Hint:* Standard snake lemma / zigzag argument from homological algebra. The connecting map $\delta$ is constructed as: lift $[c] \in H_p(M)$ to a small chain $c = c_U + c_V$, compute $\partial c_U \in C_{p-1}(U)$, observe $\partial c_U = -\partial c_V \in C_{p-1}(V)$ also, so $\partial c_U \in C_{p-1}(U \cap V)$. Its class in $H_{p-1}(U \cap V)$ is $\delta[c]$.
   - *Why needed:* This is the desired Mayer–Vietoris sequence.

---

# Lemma Decomposition

> [!note]- Lemma 1: Barycentric Subdivision and the Small-Chain Theorem
> **Statement:** Let $\{U_\alpha\}$ be an open cover of $M$. Let $C_*^\mathcal{U}(M; G)$ denote the subcomplex of $C_*(M; G)$ generated by singular simplices whose image lies in some $U_\alpha$. Then the inclusion $C_*^\mathcal{U}(M; G) \hookrightarrow C_*(M; G)$ is a chain-homotopy equivalence; consequently $H_*(C_*^\mathcal{U}(M; G)) = H_*(M; G)$.
>
> **Hint:** Construct the barycentric subdivision operator $S : C_*(M; G) \to C_*(M; G)$ and a chain homotopy $T$ between $S$ and the identity, then iterate $S$ enough times to make any given chain "small" by a Lebesgue-number argument.
>
> **Why needed:** This is the technical heart of Mayer–Vietoris and allows us to work with the smaller, more tractable chain complex of "cover-fitting" simplices.
>
> > [!note]- Sketch
> > See Hatcher, Proposition 2.21. The construction of $S$: barycentric subdivision of $\Delta^p$ gives $(p+1)!$ smaller simplices, each having the barycenter $b$ of $\Delta^p$ and a chain of barycenters of faces. The chain homotopy $T$ is built inductively, with $T(\sigma)$ being a "$T$-coning" from the barycenter. Iteration $S^n$ shrinks the diameter of each simplex by a factor depending on $n$, and by Lebesgue, after enough iterations every simplex of $S^n c$ has diameter less than the cover Lebesgue number, hence fits inside some $U_\alpha$.

> [!note]- Lemma 2: The Short Exact Sequence of Chain Complexes
> **Statement:** For $M = U \cup V$ open cover and the small chain complex $C_*^{U+V}(M; G)$, there is a short exact sequence
> $$
> 0 \to C_*(U \cap V; G) \xrightarrow{(i_U, i_V)} C_*(U; G) \oplus C_*(V; G) \xrightarrow{j_U - j_V} C_*^{U+V}(M; G) \to 0.
> $$
> Here $(i_U, i_V)(\sigma) = (\sigma, \sigma)$ and $(j_U - j_V)(\alpha, \beta) = j_U(\alpha) - j_V(\beta)$.
>
> **Hint:** Check the three exactness conditions: injectivity on the left, image-equals-kernel in the middle, surjectivity on the right. The surjectivity uses the definition of $C_*^{U+V}$: every chain therein is by definition a sum of chains in $U$ and chains in $V$.
>
> **Why needed:** Snake lemma input: every short exact sequence of chain complexes induces a long exact sequence in homology.
>
> > [!note]- Full proof
> > *Injectivity of $(i_U, i_V)$:* if $(\sigma, \sigma) = 0$ then $\sigma = 0$.
> >
> > *Middle exactness:* $(j_U - j_V)(\sigma, \sigma) = \sigma - \sigma = 0$, so $\mathrm{im}(i_U, i_V) \subseteq \ker(j_U - j_V)$. Conversely, if $(j_U - j_V)(\alpha, \beta) = j_U(\alpha) - j_V(\beta) = 0$ in $C_*^{U+V}(M)$, then $\alpha$ and $\beta$ define the same chain in $M$. Since $\alpha \in C_*(U)$ and $\beta \in C_*(V)$, this common chain has support in both $U$ and $V$, hence in $U \cap V$. So $\alpha = \beta \in C_*(U \cap V)$, and $(\alpha, \beta) = (i_U, i_V)(\alpha)$.
> >
> > *Surjectivity of $j_U - j_V$:* by definition, every chain in $C_*^{U+V}(M)$ is a sum $\sum a_i \sigma_i$ where each $\sigma_i$ has image in $U$ or in $V$. Group: let $\alpha = \sum_{\sigma_i \subseteq U} a_i \sigma_i \in C_*(U)$ and $\beta = -\sum_{\sigma_i \subseteq V} a_i \sigma_i \in C_*(V)$. Then $j_U(\alpha) - j_V(\beta) = \sum_i a_i \sigma_i$ as desired. (For simplices that lie in both $U$ and $V$, assign them to either; the choice does not matter modulo the image of $(i_U, i_V)$.)

> [!note]- Lemma 3: The Snake Lemma Produces the Long Exact Sequence
> **Statement:** A short exact sequence of chain complexes $0 \to A_\bullet \to B_\bullet \to C_\bullet \to 0$ induces a long exact sequence in homology
> $$
> \cdots \to H_p(A) \to H_p(B) \to H_p(C) \xrightarrow{\delta} H_{p-1}(A) \to H_{p-1}(B) \to \cdots
> $$
> The **connecting homomorphism** $\delta : H_p(C) \to H_{p-1}(A)$ is constructed by lifting a cycle in $C$ to a chain in $B$, taking its boundary in $B$, and observing the boundary lives in $A$.
>
> **Hint:** Standard zigzag argument from homological algebra.
>
> **Why needed:** Converts the short exact sequence of chain complexes (Lemma 2) into the long exact sequence in homology.
>
> > [!note]- Sketch
> > See Hatcher §2.1 or any homological algebra textbook. Given a cycle $c \in Z_p(C)$, lift to a chain $b \in B_p$ via surjectivity of $B \to C$. Then $\partial b$ in $B$ maps to $\partial c = 0$ in $C$, so $\partial b$ lies in the kernel of $B \to C$, hence in the image of $A \to B$. Lift to $a \in A_{p-1}$. Verify $a$ is a cycle (i.e. $\partial a = 0$ in $A$) by injectivity. Define $\delta[c] = [a]$. Verify well-definedness modulo boundaries.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For an open cover $M = U \cup V$, there is a natural long exact sequence in singular homology connecting $H_*(U \cap V)$, $H_*(U) \oplus H_*(V)$, and $H_*(M)$.
>
> *Proof.*
>
> **Step 1 — small chain theorem.** By Lemma 1, the inclusion $C_*^{U+V}(M; G) \hookrightarrow C_*(M; G)$ is a chain-homotopy equivalence, so it induces an isomorphism on homology: $H_*(C_*^{U+V}(M; G)) = H_*(M; G)$.
>
> **Step 2 — short exact sequence of chain complexes.** By Lemma 2,
> $$
> 0 \to C_*(U \cap V; G) \xrightarrow{(i_U, i_V)} C_*(U; G) \oplus C_*(V; G) \xrightarrow{j_U - j_V} C_*^{U+V}(M; G) \to 0
> $$
> is a short exact sequence of chain complexes.
>
> **Step 3 — long exact sequence in homology.** By Lemma 3 (snake lemma), this induces the long exact sequence
> $$
> \cdots \to H_p(U \cap V; G) \xrightarrow{(i_{U*}, i_{V*})} H_p(U; G) \oplus H_p(V; G) \xrightarrow{j_{U*} - j_{V*}} H_p^{U+V}(M; G) \xrightarrow{\delta} H_{p-1}(U \cap V; G) \to \cdots
> $$
>
> **Step 4 — replace $H^{U+V}$ by $H_*(M)$.** By Step 1, $H_*^{U+V}(M; G) = H_*(M; G)$. Substituting,
> $$
> \cdots \to H_p(U \cap V; G) \xrightarrow{(i_{U*}, i_{V*})} H_p(U; G) \oplus H_p(V; G) \xrightarrow{j_{U*} - j_{V*}} H_p(M; G) \xrightarrow{\delta} H_{p-1}(U \cap V; G) \to \cdots
> $$
> This is the Mayer–Vietoris long exact sequence. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Mayer–Vietoris for de Rham cohomology.** The de Rham version (Frankel's §13.3a and our [[Thm - The Mayer-Vietoris Sequence]] from `Differential Geometry X`) uses partition of unity instead of subdivision to split forms across the cover. The two Mayer–Vietoris sequences — singular and de Rham — agree on real coefficients by the [[Thm - The de Rham Theorem (Full Proof)|de Rham theorem]].

**Mayer–Vietoris for a CW complex attached cell.** Attaching an $n$-cell $D^n$ to a space $X$ along a map $\varphi : S^{n-1} \to X$ gives a space $Y = X \cup_\varphi D^n$. A Mayer–Vietoris argument with $U$ = neighborhood of $X$ in $Y$ and $V$ = open disk in the cell gives an exact sequence relating $H_*(X)$ and $H_*(Y)$, recovering the cellular boundary formula.

**Mayer–Vietoris for a connected sum.** For closed $n$-manifolds $M_1, M_2$, the connected sum $M_1 \# M_2$ has a Mayer–Vietoris decomposition with $U \simeq M_1 \setminus \{pt\}$, $V \simeq M_2 \setminus \{pt\}$, and $U \cap V \simeq S^{n-1}$. This recovers a formula for $H_*(M_1 \# M_2)$ in terms of $H_*(M_1)$ and $H_*(M_2)$.

**Čech-de Rham double complex.** For a cover with more than two pieces, iterating Mayer–Vietoris becomes unwieldy, and the right replacement is the **Čech-de Rham double complex** (Bott–Tu, Ch 8). The associated spectral sequence converges to $H^*_{dR}(M)$, with $E_2$-page involving the Čech cohomology of the cover with values in de Rham cohomology of the intersections. This is the "infinitely-iterated Mayer–Vietoris" — see [[Thm - The de Rham Theorem (Full Proof)]] for how this is exploited in the proof.

---

# Bridges

- **[[Thm - The Mayer-Vietoris Sequence|Mayer–Vietoris for de Rham cohomology]]** — the de Rham version of this theorem, proved with partition of unity instead of subdivision. By the [[Thm - The de Rham Theorem (Full Proof)|de Rham theorem]], the two sequences agree on real coefficients, and both reduce computation of $H^*(M)$ to local pieces.

- **[[Thm - The de Rham Theorem (Full Proof)|The de Rham theorem]]** — the proof reduces by Mayer–Vietoris on a good cover to the case of Euclidean balls, where both sides are trivially $\mathbb{R}$ in degree zero. The five-lemma argument that propagates the isomorphism from contractibles to arbitrary manifolds uses the Mayer–Vietoris sequence on both the singular and the de Rham side, plus naturality of the de Rham homomorphism.

- **The long exact sequence of a pair $(M, A)$** — for an inclusion $A \hookrightarrow M$, there is a long exact sequence $\cdots \to H_p(A) \to H_p(M) \to H_p(M, A) \to H_{p-1}(A) \to \cdots$ where $H_p(M, A)$ is **relative homology**. This is constructed similarly to Mayer–Vietoris, via the short exact sequence of chain complexes $0 \to C_*(A) \to C_*(M) \to C_*(M)/C_*(A) \to 0$ — both are instances of the snake lemma applied to topologically meaningful chain complexes.

- **The Eilenberg–Steenrod excision axiom** — Mayer–Vietoris is equivalent to **excision** for the cover $(U, V)$: excision says $H_*(M, A) \cong H_*(M \setminus B, A \setminus B)$ when $\overline{B} \subseteq \mathrm{int}(A)$. The two are equivalent characterisations of "local-to-global propagation" in singular homology.

- **Spectral sequences** — the Mayer–Vietoris sequence is the simplest case of a spectral sequence: it converges in one step (the $E_2$-page is the answer). For covers with more than two pieces, the spectral sequence has more pages, but the principle is the same: compute global cohomology from local pieces plus overlap data.

---

# Unlocked by This

> [!tip] Singular Homology of the Sphere *(from Algebraic Topology — this same topic)*
> The inductive computation $H_*(S^n)$ uses Mayer–Vietoris on the cover by two open hemispheres, each contractible, with intersection homotopy-equivalent to $S^{n-1}$. The connecting map shifts dimension by one, giving the recursion $H_p(S^n) = H_{p-1}(S^{n-1})$ for $p \geq 2$. See [[Thm - Singular Homology of the Sphere]].

> [!tip] The de Rham Theorem *(from Algebraic Topology — this same topic)*
> The proof reduces by Mayer–Vietoris (and the five lemma) to the case of a contractible chart, where both sides are computed by the Poincaré lemma and the contractibility of the chart. See [[Thm - The de Rham Theorem (Full Proof)]].

> [!tip] **Excision Theorem** *(from Algebraic Topology)*
> An equivalent reformulation of "local-to-global propagation" for singular homology: $H_*(M, A) \cong H_*(M \setminus B, A \setminus B)$ when $\overline{B} \subseteq \mathrm{int}(A)$. Excision and Mayer–Vietoris are equivalent characterisations and both are derived from the small-chain theorem.

> [!tip] **Čech-to-Derived-Functor Spectral Sequence** *(from Algebraic Topology and Sheaf Theory)*
> For an open cover with more than two pieces, the right generalisation of Mayer–Vietoris is the **Čech-to-derived-functor spectral sequence** (or the Mayer–Vietoris spectral sequence). The $E_2$ page involves Čech cohomology of the cover with values in derived functors; the abutment is the cohomology of the global space. This is the systematic tool for computing global invariants from a cover.

> [!tip] **Long Exact Sequence of a Fibration** *(from Algebraic Topology)*
> For a fibration $F \to E \to B$ with fiber $F$, there is a **long exact sequence in homotopy** $\cdots \to \pi_p(F) \to \pi_p(E) \to \pi_p(B) \to \pi_{p-1}(F) \to \cdots$ — the higher-dimensional analogue of Mayer–Vietoris. The proof uses the long exact sequence of a pair applied to the fiber inclusion, plus the homotopy lifting property of the fibration. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].
