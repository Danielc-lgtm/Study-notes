---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Singular Simplex"
  - "Def - The Boundary Operator"
  - "Def - The Standard p-Simplex"
tags: [geometry, algebraic-topology, boundary]
---

# Notation

$M$ is a topological space, $G$ an abelian coefficient group. $C_p(M; G)$, $\partial$ are the singular chain group and the [[Def - The Boundary Operator|boundary operator]] from [[Def - Singular Chain]]. $f_k : \Delta^{p-1} \to \Delta^p$ are the [[Def - The Standard p-Simplex|face maps]] of the standard simplex.

The composition $\partial \circ \partial$ takes $C_p$ to $C_{p-2}$ via $C_{p-1}$.

---

# Statement

> **Theorem (Boundary of a Boundary).** For every topological space $M$, every abelian group $G$, and every $p \geq 2$, the composition
> $$
> \partial \circ \partial \;:\; C_p(M; G) \;\xrightarrow{\partial}\; C_{p-1}(M; G) \;\xrightarrow{\partial}\; C_{p-2}(M; G)
> $$
> is the zero map. Equivalently, every boundary is a cycle: $B_p \subseteq Z_p$ for all $p$.

The conclusion is the single algebraic fact that makes singular homology a well-defined theory — without $\partial^2 = 0$, the quotient $\ker\partial / \mathrm{im}\,\partial$ in [[Def - Singular Homology|singular homology]] would not even make sense, because $\mathrm{im}\,\partial$ would not be contained in $\ker\partial$.

The proof is purely combinatorial: it reduces by linearity to the case of a single singular simplex, and there to a single identity about the face maps of the standard simplex.

---

# Motivation

The boundary operator $\partial$ formalises the intuitive idea "take the geometric boundary of a $p$-dimensional region." For this to give a coherent theory of cycles and boundaries — a setup where we can ask "which $p$-cycles bound?" and get a non-vacuous answer — we need it to be true that the boundary of a boundary is empty. The boundary of a $p$-dimensional region is a $(p-1)$-dimensional closed surface; the boundary of a closed surface is empty.

Geometrically this is obvious: a square has four edges, and the boundary of the loop of four edges is the eight endpoints, but each endpoint is shared by two edges and appears twice with cancelling signs. Algebraically the same cancellation must happen — and it does, via the alternating-sign convention in $\partial = \sum (-1)^k (\text{face}_k)$.

But the algebraic proof requires more than just "geometrically obvious" — it requires verifying that the specific combinatorial recipe for $\partial$ (alternating signs in a specific order) actually produces the required cancellation. The proof is a small but precise computation: the $j$-th face of the $k$-th face of $\Delta^p$ (for $j < k$) equals the $(k-1)$-th face of the $j$-th face, with a sign relation, and the double sum over $(j, k)$ cancels in pairs.

The role this theorem plays is foundational: every later theorem in the chapter relies on it. The construction of singular homology, the verification of homotopy invariance (which relies on $\partial^2 = 0$ to make chain homotopies well-defined), Mayer–Vietoris (whose long exact sequence depends on the chain-complex structure), the de Rham theorem (whose proof reduces to a Mayer–Vietoris induction) — all rest on this combinatorial identity. The theorem is so fundamental that it gets verified once and then used implicitly everywhere.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *we have the singular chain complex with $\partial = \sum (-1)^k (\sigma \circ f_k)$ defined by the alternating sum of face maps.*

The first disguised source is **any chain complex defined by an alternating-sign face structure on a graded module.** Property $B$: a graded module $(C_p)_{p \geq 0}$ equipped with degree-decreasing operators $d_k^p : C_p \to C_{p-1}$ for $k = 0, \dots, p$, satisfying the simplicial identity $d_j^{p-1} d_k^p = d_{k-1}^{p-1} d_j^p$ for $j < k$. The bridge: define $\partial = \sum_k (-1)^k d_k$; the proof below works verbatim. *Example application:* any simplicial set $X_\bullet$ gives a chain complex with $\partial^2 = 0$ by exactly this proof — including the singular complex of a topological space, the nerve of a category, the Čech complex of a cover, the bar complex of a group.

The second disguised source is **any cosimplicial structure dualised to a cochain complex with $\delta^2 = 0$.** Property $B$: face *maps* (degree-raising, in the opposite direction) and coface relations. The bridge: dualising the alternating-sign sum gives $\delta = \sum (-1)^k (d^k)^*$, and the same proof gives $\delta^2 = 0$. *Example application:* the de Rham complex $\Omega^\bullet$ has $d^2 = 0$ as the cohomology dual of the simplicial $\partial^2 = 0$ — the exterior derivative is structured the same way.

The third disguised source is **the boundary of a manifold with boundary has no boundary.** Property $B$: a compact manifold $W$ with boundary $\partial W$. The bridge: $\partial W$ is a closed manifold, so $\partial(\partial W) = \emptyset$ — the manifold-level boundary operator squares to zero (when applied to the fundamental class). The chain-level statement $\partial^2 = 0$ is the algebraic shadow of this geometric fact, and the proof below is the combinatorial verification that "the alternating face sum captures the geometric boundary."

**Targets (Output Amplification)**

The conclusion $C$: *$\partial^2 = 0$, so boundaries are cycles ($B_p \subseteq Z_p$), and the quotient $H_p = Z_p / B_p$ is well-defined.*

Combine $C$ with **the definition of singular homology as a quotient.** $H_p(M; G) = Z_p / B_p$ requires $B_p$ to be a subgroup of $Z_p$ — which is exactly $\partial^2 = 0$. The further result $E$: singular homology is a well-defined functor $\mathbf{Top} \to \mathbf{Ab}$. Without $\partial^2 = 0$, there is no singular homology at all.

Combine $C$ with **Stokes's theorem $\int_{\partial c} \omega = \int_c d\omega$.** The chain-level $\partial^2 = 0$ pairs with the form-level $d^2 = 0$ via integration: $\int_{\partial^2 c} \omega = \int_{\partial c} d\omega = \int_c d^2 \omega = 0$ — both vanishings come from the same simplicial identity (interpreted geometrically). The further result $E$: the de Rham pairing $\int_c \omega$ is well-defined modulo cohomology and homology classes simultaneously, allowing the de Rham theorem to be stated.

Combine $C$ with **the construction of the long exact sequence in homology.** The snake lemma and the zig-zag lemma both require the input chain complexes to have $\partial^2 = 0$. The further result $E$: every long exact sequence of homology (Mayer–Vietoris, pair, fibration) is available, providing the inductive engine for all computations.

---

# Why Is It True

**The single sentence: the alternating-sign sum $\partial = \sum (-1)^k (\text{face}_k)$ encodes the orientation bookkeeping of a $p$-simplex, and the simplicial identity "face-of-face cancels in pairs" is exactly what the alternating signs are designed to produce.**

The intuition starts with the smallest case. Consider a triangle $\Delta^2 = (P_0, P_1, P_2)$. Its boundary is the loop
$$
\partial(P_0, P_1, P_2) = (P_1, P_2) - (P_0, P_2) + (P_0, P_1) \;=\; e_0 - e_1 + e_2,
$$
where $e_k = (P_0, \dots, \widehat{P_k}, \dots, P_2)$ is the $k$-th edge. Now take the boundary of each edge:
- $\partial e_0 = \partial(P_1, P_2) = P_2 - P_1$
- $\partial e_1 = \partial(P_0, P_2) = P_2 - P_0$
- $\partial e_2 = \partial(P_0, P_1) = P_1 - P_0$

So
$$
\partial^2(P_0, P_1, P_2) = (P_2 - P_1) - (P_2 - P_0) + (P_1 - P_0) = 0.
$$
Each vertex appears twice (since each vertex sits on two of the three edges), and the alternating signs ensure the two appearances cancel.

Now for general $p$: the boundary of a $p$-simplex is a sum of $p+1$ codimension-$1$ faces, and the boundary of each codimension-$1$ face is a sum of $p$ codimension-$2$ faces (which are also codimension-$2$ faces of the original $\Delta^p$). The double sum $\partial^2 \Delta^p$ counts each codimension-$2$ face $(P_0, \dots, \widehat{P_j}, \dots, \widehat{P_k}, \dots, P_p)$ (with $j < k$) *twice*: once as "the $j$-th face of the $k$-th face," and once as "the $(k-1)$-th face of the $j$-th face." (The $(k-1)$ is because after omitting $P_j$, the original index $k$ shifts down to $k-1$.) The signs in these two appearances are $(-1)^k \cdot (-1)^j$ and $(-1)^j \cdot (-1)^{k-1}$ respectively, which are negatives of each other. So the two appearances cancel.

The key combinatorial identity, called the **simplicial identity** or **face-of-face relation**, is
$$
f_j \circ f_k = f_{k} \circ f_{j} \qquad \text{(naively, but with index shift)},
$$
made precise by: for $j < k$, the $j$-th face of the $k$-th face equals the $(k-1)$-th face of the $j$-th face. This is exactly the combinatorial fact "omit vertex $P_k$ first, then omit $P_j$" equals "omit vertex $P_j$ first, then omit $P_{k}$ (which has now become $P_{k-1}$ after the earlier omission)." Both procedures end with the same $(p-2)$-simplex missing vertices $P_j$ and $P_k$.

---

# What Makes This Hard

The proof itself is short and combinatorial, but the index bookkeeping is fiddly: most errors come from confusing whether "the $j$-th face of the $k$-th face" should use the original index $j$ or the shifted index $j-1$. The correct rule is: face omission preserves the indices below the omitted vertex but shifts everything above by one. So if we omit $P_k$ first (with $k > j$), then $P_j$ keeps its original index — but if we omit $P_j$ first, then $P_k$ becomes $P_{k-1}$. Getting this right is the entire proof; getting it wrong gives a sum that doesn't cancel.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce to a single simplex by linearity, then to the standard simplex by naturality, then verify the combinatorial identity by expanding $\partial \partial \Delta^p$ as a double sum and showing each codimension-$2$ face appears with cancelling signs.

**Subgoal decomposition:**

1. **Reduce to a single simplex.** Both $\partial$ and $\partial^2$ are $G$-linear, so $\partial^2(\sum g_i \sigma_i) = \sum g_i \partial^2 \sigma_i$. It suffices to show $\partial^2 \sigma = 0$ for every singular simplex $\sigma$.
   - *Hint:* Use linearity of $\partial$.
   - *Why needed:* Reduces the proof to a calculation on a single simplex.

2. **Reduce to the standard simplex via naturality.** $\partial$ commutes with the chain map $\sigma_\# : C_\bullet(\Delta^p) \to C_\bullet(M)$ induced by $\sigma : \Delta^p \to M$. So $\partial^2 \sigma = \partial^2 \sigma_\# (\Delta^p) = \sigma_\# \partial^2 \Delta^p$. It suffices to show $\partial^2 \Delta^p = 0$, where $\Delta^p$ is the identity map viewed as a singular simplex in itself.
   - *Hint:* Use $\partial \circ \sigma_\# = \sigma_\# \circ \partial$.
   - *Why needed:* Reduces to a fully combinatorial calculation independent of $M$.

3. **Expand the double sum.** $\partial \Delta^p = \sum_{k=0}^p (-1)^k f_k$, so $\partial^2 \Delta^p = \sum_{j=0}^{p-1} \sum_{k=0}^p (-1)^j (-1)^k (f_k \circ f_j) \in C_{p-2}$.
   - *Hint:* Write out the double sum, treating each $f_k \circ f_j$ as a codimension-$2$ face.
   - *Why needed:* This is the algebraic expression to be shown to vanish.

4. **Identify the simplicial identity.** For $j < k$: $f_k \circ f_j = f_{j} \circ f_{k-1}$. (Both equal the codimension-$2$ face omitting $P_j$ and $P_k$.)
   - *Hint:* Verify this from the definition $f_k(P_i) = P_i$ for $i < k$, $f_k(P_i) = P_{i+1}$ for $i \geq k$. Track what happens to indices.
   - *Why needed:* This is the combinatorial identity that creates the cancellation.

5. **Cancel in pairs.** Split the double sum into $j < k$ and $j \geq k$ parts; rewrite the $j \geq k$ part using $j' = k$, $k' = j+1$ (so $j' < k'$), and use the simplicial identity to make terms match. The signs $(-1)^j (-1)^k$ and $(-1)^{k-1}(-1)^j$ are negatives.
   - *Hint:* Pair the term $(j, k)$ with $j < k$ against the term $(k-1, j)$ with $k - 1 \geq j$.
   - *Why needed:* This is the explicit cancellation showing the double sum is zero.

---

# Lemma Decomposition

> [!note]- Lemma 1: Simplicial Identity for Face Maps
> **Statement:** For $0 \leq j < k \leq p$, the face maps of the standard simplex satisfy $f_k \circ f_j = f_j \circ f_{k-1}$, both as maps $\Delta^{p-2} \to \Delta^p$ with image the $(p-2)$-face $(P_0, \dots, \widehat{P_j}, \dots, \widehat{P_k}, \dots, P_p)$.
>
> **Hint:** Recall that $f_m$ is the unique affine map sending $P_i \mapsto P_i$ for $i < m$ and $P_i \mapsto P_{i+1}$ for $i \geq m$. Track what each composition does to each vertex.
>
> **Why needed:** This identity is the combinatorial heart of the proof — without it the double sum in $\partial^2$ would not cancel.
>
> > [!note]- Full proof
> > Both $f_k \circ f_j$ and $f_j \circ f_{k-1}$ are affine maps $\Delta^{p-2} \to \Delta^p$. An affine map is determined by its values on vertices, so it suffices to show they agree on each $P_i$ for $i = 0, 1, \dots, p-2$.
> >
> > Compute $f_k \circ f_j (P_i)$: apply $f_j$ first, then $f_k$. 
> > - If $i < j$: $f_j(P_i) = P_i$, then $f_k(P_i) = P_i$ (since $i < j < k$). Result: $P_i$.
> > - If $j \leq i < k - 1$: $f_j(P_i) = P_{i+1}$, then $f_k(P_{i+1}) = P_{i+1}$ (since $i + 1 < k$). Result: $P_{i+1}$.
> > - If $i \geq k - 1$: $f_j(P_i) = P_{i+1}$, then $f_k(P_{i+1}) = P_{i+2}$ (since $i + 1 \geq k$). Result: $P_{i+2}$.
> >
> > Now $f_j \circ f_{k-1} (P_i)$: apply $f_{k-1}$ first, then $f_j$.
> > - If $i < k - 1$: $f_{k-1}(P_i) = P_i$, then $f_j(P_i) = P_i$ if $i < j$, else $P_{i+1}$.
> > - If $i \geq k - 1$: $f_{k-1}(P_i) = P_{i+1}$, then $f_j(P_{i+1}) = P_{i+2}$ (since $i + 1 > k - 1 > j$).
> >
> > Match cases:
> > - $i < j$: both give $P_i$. ✓
> > - $j \leq i < k - 1$: first gives $P_{i+1}$; second gives $f_j(P_i) = P_{i+1}$ (since $i \geq j$). ✓
> > - $i \geq k - 1$: both give $P_{i+2}$. ✓
> >
> > So $f_k \circ f_j = f_j \circ f_{k-1}$ on every vertex, hence as affine maps. The image is the $(p-2)$-face missing $P_j$ and $P_k$.

> [!note]- Lemma 2: The Double Sum Cancels in Pairs
> **Statement:** $\partial^2 \Delta^p = \sum_{0 \leq j \leq p-1,\ 0 \leq k \leq p} (-1)^{j+k} (f_k \circ f_j) = 0$ in $C_{p-2}$.
>
> **Hint:** Split the double sum into pairs of corresponding terms — one with $j < k$, one with $j \geq k$ — and use Lemma 1 to show that paired terms cancel.
>
> **Why needed:** This is the final algebraic verification that the boundary of a boundary vanishes.
>
> > [!note]- Full proof
> > Write the double sum as $S = \sum_{j, k} (-1)^{j+k} (f_k \circ f_j)$, where the sum runs over $0 \leq j \leq p-1$ and $0 \leq k \leq p$. Split it into two parts based on the relation between $j$ and $k$:
> > $$
> > S = \underbrace{\sum_{j < k} (-1)^{j+k} (f_k \circ f_j)}_{S_1} + \underbrace{\sum_{j \geq k} (-1)^{j+k} (f_k \circ f_j)}_{S_2}.
> > $$
> >
> > For $S_2$, perform the change of variables $j' = k$, $k' = j + 1$. The condition $j \geq k$ becomes $k' - 1 \geq j'$, i.e. $j' < k'$. The original index ranges $j \in \{0, \dots, p-1\}$, $k \in \{0, \dots, p\}$ with $j \geq k$ map to $j' \in \{0, \dots, p-1\}$, $k' \in \{1, \dots, p\}$ with $j' < k'$. So $S_2 = \sum_{j' < k'} (-1)^{(k'-1)+j'} (f_{j'} \circ f_{k'-1})$.
> >
> > Apply Lemma 1: $f_{j'} \circ f_{k'-1} = f_{k'} \circ f_{j'}$ (using the lemma with $(j, k) \to (j', k')$, the identity $f_{k'} \circ f_{j'} = f_{j'} \circ f_{k'-1}$). So $S_2 = \sum_{j' < k'} (-1)^{j'+k'-1} (f_{k'} \circ f_{j'}) = -\sum_{j' < k'} (-1)^{j' + k'} (f_{k'} \circ f_{j'}) = -S_1$.
> >
> > Therefore $S = S_1 + S_2 = S_1 - S_1 = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For every singular chain $c \in C_p(M; G)$ with $p \geq 2$, $\partial \partial c = 0$.
>
> *Proof.*
>
> **Step 0 — reduce to single simplices.** By $G$-linearity of $\partial$, $\partial \partial (\sum_i g_i \sigma_i) = \sum_i g_i \cdot \partial \partial \sigma_i$. It suffices to show $\partial \partial \sigma = 0$ for any single singular simplex $\sigma$.
>
> **Step 1 — reduce to the standard simplex.** Let $\sigma : \Delta^p \to M$ be a singular $p$-simplex. The induced chain map $\sigma_\# : C_\bullet(\Delta^p; G) \to C_\bullet(M; G)$ satisfies $\partial \circ \sigma_\# = \sigma_\# \circ \partial$ on every degree. Hence
> $$
> \partial \partial \sigma = \partial \partial \sigma_\# (\Delta^p) = \sigma_\#(\partial \partial \Delta^p).
> $$
> (Here $\Delta^p$ denotes the identity singular simplex of $\Delta^p$ in itself, an element of $C_p(\Delta^p; G)$.) So it suffices to show $\partial \partial \Delta^p = 0$ in $C_{p-2}(\Delta^p; G)$.
>
> **Step 2 — expand the double sum.** From $\partial \Delta^p = \sum_{k=0}^p (-1)^k f_k$,
> $$
> \partial \partial \Delta^p = \sum_{k=0}^p (-1)^k \partial f_k = \sum_{k=0}^p (-1)^k \sum_{j=0}^{p-1} (-1)^j (f_k \circ f_j) = \sum_{0 \leq j \leq p-1,\ 0 \leq k \leq p} (-1)^{j+k} (f_k \circ f_j).
> $$
>
> **Step 3 — apply the simplicial identity.** Split the double sum into the $j < k$ and $j \geq k$ parts:
> $$
> \partial \partial \Delta^p = \underbrace{\sum_{0 \leq j < k \leq p} (-1)^{j+k} (f_k \circ f_j)}_{S_1} + \underbrace{\sum_{0 \leq k \leq j \leq p-1} (-1)^{j+k} (f_k \circ f_j)}_{S_2}.
> $$
>
> For $S_2$, substitute $j' = k$, $k' = j+1$. The range $0 \leq k \leq j \leq p-1$ maps bijectively to $0 \leq j' < k' \leq p$. The exponent $j + k = (k'-1) + j'$. So $S_2 = \sum_{j' < k'} (-1)^{j'+k'-1} (f_{j'} \circ f_{k'-1})$.
>
> By Lemma 1 (the simplicial identity $f_k \circ f_j = f_j \circ f_{k-1}$ for $j < k$), $f_{j'} \circ f_{k'-1} = f_{k'} \circ f_{j'}$ (applying the lemma with the roles of $(j, k)$ as $(j', k')$). Hence $S_2 = -\sum_{j' < k'} (-1)^{j'+k'} (f_{k'} \circ f_{j'}) = -S_1$.
>
> **Step 4 — conclude.** $\partial \partial \Delta^p = S_1 + S_2 = S_1 - S_1 = 0$.
>
> Combining with Step 1, $\partial \partial \sigma = \sigma_\#(0) = 0$. By Step 0, $\partial \partial c = 0$ for every chain $c$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Cochain version: $d^2 = 0$ for the exterior derivative.** Dualising the singular chain complex via $\mathrm{Hom}(-, G)$ converts $\partial$ to the coboundary $\delta$, and the same proof gives $\delta^2 = 0$. The de Rham analogue is $d^2 = 0$ for the exterior derivative on differential forms — see [[Thm - d-Squared-is-Zero]] from `Differential Geometry VIII`. The two facts are the same identity in dual frames.

**Group cohomology: the bar resolution.** For a group $G$ and a $G$-module $M$, the **bar resolution** defines a chain complex $\cdots \to G^n \otimes M \to G^{n-1} \otimes M \to \cdots$ with $\partial = \sum (-1)^k d_k$ given by face maps $d_k(g_1, \dots, g_n) = (g_1, \dots, \widehat{g_k}, \dots, g_n)$ with appropriate convention adjustments at the boundary. The proof that $\partial^2 = 0$ is structurally identical to ours and gives the well-definedness of group cohomology $H^n(G; M)$.

**Lie algebra cohomology: the Chevalley–Eilenberg complex.** For a Lie algebra $\mathfrak{g}$ and a $\mathfrak{g}$-module $V$, the **Chevalley–Eilenberg complex** has cochains $C^n = \mathrm{Hom}(\bigwedge^n \mathfrak{g}, V)$ with differential $d : C^n \to C^{n+1}$ involving an alternating sum over indices. The proof that $d^2 = 0$ uses the Jacobi identity of $\mathfrak{g}$ — a structurally similar combinatorial cancellation.

**The Koszul complex.** The **Koszul complex** of a regular sequence in a commutative ring has chain group $\bigwedge^k (R^n)$ with differential $d(e_{i_1} \wedge \cdots \wedge e_{i_k}) = \sum (-1)^j x_{i_j} (e_{i_1} \wedge \cdots \wedge \widehat{e_{i_j}} \wedge \cdots \wedge e_{i_k})$. The proof $d^2 = 0$ is the alternating cancellation again, this time on the exterior algebra. The Koszul complex is the foundation of commutative algebra and homological algebra.

**Čech cohomology of a cover.** For an open cover $\mathcal{U} = \{U_i\}$ of $M$, the **Čech complex** $C^n(\mathcal{U}; \mathcal{F})$ for a sheaf $\mathcal{F}$ has cochains assigning to each $(n+1)$-fold intersection $U_{i_0} \cap \cdots \cap U_{i_n}$ a section of $\mathcal{F}$, with $\delta$ the alternating sum over face omissions. The proof $\delta^2 = 0$ is the simplicial cancellation again — Čech cohomology is the cohomology of this simplicial cover-complex.

---

# Bridges

- **[[Thm - d-Squared-is-Zero|$d^2 = 0$ for the exterior derivative]]** — the differential-form version of the same combinatorial identity, dualised. On the singular side, $\partial = \sum (-1)^k (\text{face}_k)$ lowers degree; on the de Rham side, $d$ raises degree but has the same alternating structure (in its coordinate expression). The two facts pair via integration: $\int_{\partial^2 c} \omega = 0 = \int_c d^2 \omega$, and both vanish for the same reason — the simplicial face identity.

- **[[Def - Singular Homology|Singular homology]]** — defined as $H_p = \ker\partial / \mathrm{im}\,\partial$, which requires $\mathrm{im}\,\partial \subseteq \ker\partial$ — equivalently $\partial^2 = 0$. Without this theorem, singular homology does not exist as a well-defined construction. Every subsequent theorem in this topic (homotopy invariance, Mayer–Vietoris, de Rham) tacitly assumes $\partial^2 = 0$.

- **Stokes's theorem $\int_{\partial c} \omega = \int_c d\omega$** — when applied recursively, $\int_{\partial^2 c} \omega = \int_{\partial c} d\omega = \int_c d^2\omega = 0$. The chain-level $\partial^2 = 0$ and the form-level $d^2 = 0$ are equivalent statements via Stokes, both reflecting the same geometric fact "the boundary of a boundary is empty."

- **The simplicial identities** — the face-of-face relation $f_k \circ f_j = f_j \circ f_{k-1}$ (for $j < k$) is one of a small family of identities relating face and degeneracy maps in a **simplicial set**. The full set defines the simplex category $\Delta$, and the requirement that face and degeneracy maps satisfy these identities is the definition of a simplicial object. Singular homology is one instance; group cohomology, the nerve of a category, Eilenberg–MacLane spaces are others.

---

# Unlocked by This

> [!tip] The Singular Homology Functor *(from Algebraic Topology — this same topic)*
> Once $\partial^2 = 0$ is verified, the quotient $H_p = \ker\partial / \mathrm{im}\,\partial$ defines [[Def - Singular Homology|singular homology]], the central object of this chapter. Every later property — functoriality, homotopy invariance, Mayer–Vietoris, the de Rham theorem — depends on having this quotient be well-defined.

> [!tip] Chain Complexes as a Universe *(from Homological Algebra)*
> Any sequence of abelian groups with $\partial^2 = 0$ is a **chain complex**, and the homology is the central invariant. The category $\mathbf{Ch}(\mathbf{Ab})$ of chain complexes is the natural setting for homological algebra; spectral sequences, derived functors, and the derived category all live here. Singular chains form one example of a chain complex; every cohomology theory in mathematics arises by constructing some other chain complex.

> [!tip] **The de Rham Theorem and Mayer–Vietoris** *(from this same topic)*
> The well-definedness of singular cohomology (via $\delta^2 = 0$, the dual of $\partial^2 = 0$) lets us state the de Rham isomorphism $H^p_{dR}(M) \cong H^p(M; \mathbb{R})$ and apply Mayer–Vietoris to both sides of the comparison. The entire proof strategy of [[Thm - The de Rham Theorem (Full Proof)]] relies on having well-defined chain complexes with $\partial^2 = 0$ on both sides.
