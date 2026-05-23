---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Fibration"
  - "Def - Higher Homotopy Group"
  - "Def - Exact Sequence of Groups"
tags: [geometry, algebraic-topology, homotopy, fibre-bundles]
---

# Notation

$F \hookrightarrow E \xrightarrow{\pi} B$ is a [[Def - Fibration|fibration]] with total space $E$, base $B$, and fibre $F = \pi^{-1}(b_0)$ over a base point $b_0 \in B$. All spaces are pointed, and we take $b_0 \in B$, $e_0 \in F \subseteq E$ as base points with $\pi(e_0) = b_0$. The inclusion $i : F \hookrightarrow E$ and projection $\pi : E \to B$ induce maps in homotopy: $i_* : \pi_k(F, e_0) \to \pi_k(E, e_0)$ and $\pi_* : \pi_k(E, e_0) \to \pi_k(B, b_0)$. The **connecting homomorphism** is $\partial : \pi_k(B, b_0) \to \pi_{k-1}(F, e_0)$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Statement

> **Theorem (Long Exact Sequence of a Fibration).** Let $F \hookrightarrow E \xrightarrow{\pi} B$ be a Hurewicz fibration with $F$ path-connected. Then there is a long exact sequence of homotopy groups
>
> $$\cdots \to \pi_k(F, e_0) \xrightarrow{i_*} \pi_k(E, e_0) \xrightarrow{\pi_*} \pi_k(B, b_0) \xrightarrow{\partial} \pi_{k-1}(F, e_0) \to \cdots$$
>
> $$\cdots \to \pi_2(F) \to \pi_2(E) \to \pi_2(B) \xrightarrow{\partial} \pi_1(F) \to \pi_1(E) \to \pi_1(B) \to 1.$$
>
> The maps $i_*$ and $\pi_*$ are induced by the inclusion of the fibre and the bundle projection. The connecting homomorphism $\partial : \pi_k(B) \to \pi_{k-1}(F)$ is constructed via the homotopy lifting property: a sphere in $B$ is lifted to a disc in $E$ whose boundary $(k-1)$-sphere lies in $F$.

> **Remark (degree 0).** If $F$ is *not* path-connected, the sequence continues one more term to $\pi_0(F) \to \pi_0(E) \to \pi_0(B)$ (with $\pi_0$ as a pointed set), but exactness at $\pi_1(B)$ may fail. For us, $F$ is always taken path-connected and the sequence terminates with $\pi_1(B) \to 1$.

---

# Motivation

The long exact sequence of a fibration is the single most important computational tool in higher homotopy theory. Almost every explicit computation of $\pi_k(X)$ for a non-trivial space $X$ at low to moderate $k$ goes through it: $\pi_k$ of spheres via Hopf fibrations, $\pi_k$ of Lie groups via $G \to G/H$, $\pi_k$ of homogeneous spaces, $\pi_k$ of bundle total spaces. The sequence is the analogue of the long exact sequence of a pair in homology, with the boundary map $\partial$ playing the central role.

The motivating question is: *given the homotopy of any two of $F, E, B$ in a fibration, can we recover the homotopy of the third?* The answer is yes, modulo the boundary map: the long exact sequence locks three groups together in each degree, and knowing two of the three (plus exactness) determines the third up to extension.

The structural insight is that **a fibration is the homotopy-theoretic analogue of a quotient**, with $F$ the "kernel" and $B$ the "quotient". The long exact sequence then plays the role of the snake lemma applied to a "short exact sequence of homotopy types" $F \to E \to B$. The fact that it works at all — that homotopy groups, despite being highly non-trivial invariants, fit into a long exact sequence — is a deep and useful fact.

The boundary map $\partial$ is the geometric heart of the theorem. It encodes the *twist* in the bundle: how the fibres are glued together as you move around the base. For a *trivial* bundle $E = B \times F$, $\partial$ is the zero map and the sequence splits into short exact pieces $0 \to \pi_k(F) \to \pi_k(E) \to \pi_k(B) \to 0$, recovering $\pi_k(B \times F) = \pi_k(B) \oplus \pi_k(F)$. For a *non-trivial* bundle, $\partial$ is non-zero, and the kernel/cokernel structure encodes the topological twist.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem requires a **Hurewicz fibration** $F \to E \to B$. The skill is recognising when a given map is a fibration.

**Source 1: any smooth fibre bundle.** Every smooth fibre bundle in the differential-geometric sense is a Hurewicz fibration. The HLP follows from local triviality and partition-of-unity arguments. So every principal bundle, vector bundle, frame bundle, and associated bundle gives a long exact sequence. *Example:* the Hopf fibration $S^1 \to S^3 \to S^2$ gives $\pi_3(S^2) = \mathbb{Z}$.

**Source 2: a homogeneous space.** For a Lie group $G$ and closed subgroup $H$, the quotient map $G \to G/H$ is a principal $H$-bundle, hence a fibration. The long exact sequence gives a recursive way to compute $\pi_k(G/H)$ or $\pi_k(G)$ in terms of each other. *Example:* $SU(n-1) \to SU(n) \to S^{2n-1}$ gives $\pi_k(SU(n)) = \pi_k(SU(n-1))$ for $k < 2n-2$, eventually computing $\pi_k(SU(n))$ via Bott periodicity.

**Source 3: a covering space.** A covering $\tilde X \to X$ with fibre $F$ a discrete set is a fibration. The long exact sequence collapses (since $\pi_k(F) = 0$ for $k \geq 1$ when $F$ is discrete) to give $\pi_k(\tilde X) \cong \pi_k(X)$ for $k \geq 2$ (the **lifting isomorphism**) and the short exact $1 \to \pi_1(\tilde X) \to \pi_1(X) \to F \to 1$ (when the cover is regular). This is how [[Algebraic Topology II — Fundamental Group and Covering Spaces|covering-space theory]] becomes a special case of fibration theory.

**Source 4: a path-loop fibration.** For any pointed space $X$, $\Omega X \to PX \to X$ is a Hurewicz fibration with $PX$ contractible. The long exact sequence gives $\pi_k(X) \cong \pi_{k-1}(\Omega X)$ for all $k \geq 1$ — the **loop-space adjunction**. Iterating: $\pi_k(X) = \pi_0(\Omega^k X)$. This is one of the most-used identifications in homotopy theory.

**Source 5: a Serre fibration.** Strictly weaker than Hurewicz (HLP for CW complexes only), but every Serre fibration also has a long exact sequence — the proof goes through the same way. Most fibrations arising in practice are Serre fibrations even when full Hurewicz is not obvious.

**Targets (Output Amplification)**

The conclusion is a long exact sequence. The combinations with other facts unlock specific homotopy computations.

**Target 1: pin down $\pi_k(B)$ when $E$ is "nice".** When the total space $E$ has trivial higher homotopy (e.g., $E$ contractible, as in the path-loop fibration), the long exact sequence shifts: $\pi_k(B) \cong \pi_{k-1}(F)$ for all $k$. *Useful when:* $E$ is the path space (or any contractible cover/extension of $B$).

**Target 2: pin down $\pi_k(F)$ when $E$ and $B$ are known.** The exact sequence $\pi_k(E) \to \pi_k(B) \to \pi_{k-1}(F) \to \pi_{k-1}(E) \to \pi_{k-1}(B)$ allows $\pi_{k-1}(F)$ to be computed from the four other groups. *Useful for:* computing the homotopy of fibres of known bundles.

**Target 3: identify $\pi_k(\mathrm{Lie group})$ recursively.** Bott's computation of $\pi_k(U)$, $\pi_k(O)$, $\pi_k(\mathrm{Sp})$ uses the long exact sequence applied iteratively to $G/H \to G \to G/H$ structures. The result is **Bott periodicity**: $\pi_k(U) = \pi_{k+2}(U)$ and $\pi_k(O) = \pi_{k+8}(O)$ — periodicities that drive K-theory.

**Target 4: detect the boundary map $\partial$ via geometric witnesses.** The map $\partial : \pi_k(B) \to \pi_{k-1}(F)$ is determined by lifting spheres. For the Hopf fibration, $\partial : \pi_2(S^2) \to \pi_1(S^1)$ sends $[\mathrm{id}_{S^2}]$ to a generator of $\pi_1(S^1) = \mathbb{Z}$ — explicitly verifiable by drawing the lift.

---

# Why Is It True

**The one-line mechanism:** *the homotopy lifting property turns a sphere in $B$ into a disc in $E$ whose boundary lies in $F$; the boundary map records this boundary as an element of $\pi_{k-1}(F)$, and exactness at each group is the statement that lifts can always be adjusted to be honest spheres when the obstructions vanish.*

The intuition begins with the boundary map $\partial$. Given a class $[f] \in \pi_k(B)$ represented by $f : S^k \to B$, think of $f$ as a homotopy: $S^k = I^k / \dot I^k$, and the "initial position" $I^{k-1} \times \{0\}$ has $f|_{\text{initial}}$ the constant map at $b_0$. The HLP says: lift this homotopy to $E$, starting from the constant lift at $e_0$. The result is a map $\tilde F : I^k \to E$ lifting $f$, with $\tilde F$ constant on the initial position. The boundary $\tilde F|_{\partial I^k \setminus \text{initial}}$ lies in the fibre $\pi^{-1}(b_0) = F$ (because $f$ collapses $\dot I^k$ to $b_0$, and $\tilde F$ is a lift). This boundary is an $(k-1)$-disc that maps its boundary $(k-2)$-sphere to a single point — i.e., it represents an element of $\pi_{k-1}(F)$. That element is $\partial [f]$.

For example, take the Hopf fibration $S^1 \to S^3 \to S^2$ and the identity class $[\mathrm{id}_{S^2}] \in \pi_2(S^2) = \mathbb{Z}$. We lift the identity map $S^2 \to S^2$ to $S^3$, but the lift cannot be a sphere because $\pi_2(S^3) = 0$ — instead it is a disc with boundary in the fibre $S^1$. The boundary is a circle in $S^1$, mapping non-trivially: it is the generator of $\pi_1(S^1) = \mathbb{Z}$. So $\partial[\mathrm{id}_{S^2}]$ is a generator, recovering $\partial$ as an isomorphism $\pi_2(S^2) \xrightarrow{\sim} \pi_1(S^1)$. This is the geometric content of the long exact sequence applied to the Hopf bundle.

Now exactness. Consider the three-term piece $\pi_k(F) \xrightarrow{i_*} \pi_k(E) \xrightarrow{\pi_*} \pi_k(B)$.

- **$\pi_* \circ i_* = 0$:** if $f : S^k \to F \subseteq E$, then $\pi \circ f : S^k \to B$ is constant (because $F = \pi^{-1}(b_0)$ collapses to $b_0$ under $\pi$). So the image of $i_*$ lies in $\ker \pi_*$.

- **$\ker \pi_* \subseteq \mathrm{im}\, i_*$:** if $f : S^k \to E$ has $\pi \circ f \simeq $ constant, then the homotopy can be lifted (by HLP) to a homotopy in $E$ that deforms $f$ to a map landing in $F$. So $f$ is homotopic to a map factoring through $F$, hence $[f] \in \mathrm{im}\, i_*$.

The other exactness statements follow similar patterns: at each group, the "obstruction to triviality" of one map is precisely what is detected by the next map in the sequence, via HLP.

---

# What Makes This Hard

The bookkeeping in constructing $\partial$ rigorously is the hardest part. The lift exists by HLP, but showing that the boundary class in $\pi_{k-1}(F)$ is well-defined (independent of representative $f$ and of lift $\tilde F$) requires careful homotopies and verification that the boundary is also a sphere (not just a disc). The dimensional juggling — a $k$-sphere in $B$, lifted to a $k$-disc in $E$ with boundary $(k-1)$-sphere in $F$ — is the source of most computational errors when first learning this.

The second difficulty is recognising fibrations *in the wild*. Many maps "look like" they should be fibrations but actually fail HLP (e.g., maps with non-homotopy-equivalent fibres). Verifying HLP for a given map can require partition-of-unity arguments or appeal to general theorems (e.g., "every smooth bundle is a fibration") rather than direct verification.

The third difficulty is that the boundary map $\partial$ is *not* induced by any continuous map of spaces — it is an algebraic construction. There is no canonical "boundary map" $B \to F$ in the topological category; only at the level of homotopy groups does it appear. This is the analogue of the snake lemma's boundary map in homological algebra: a structural artefact of exactness, not a geometric map.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Construct the boundary map $\partial : \pi_k(B) \to \pi_{k-1}(F)$ via the homotopy lifting property: a sphere in $B$ becomes a disc in $E$ whose boundary is a sphere in $F$. Verify exactness at each of the three groups in each segment $\pi_k(F) \to \pi_k(E) \to \pi_k(B) \to \pi_{k-1}(F)$ by direct lifting arguments.

**Subgoal decomposition:**

1. **Construct $\partial$.** For $[f] \in \pi_k(B)$, represent $f$ as a map $I^k \to B$ with $f(\dot I^k) = b_0$. View this as a homotopy on $I^{k-1}$. Lift via HLP to a map $\tilde F : I^k \to E$ with $\tilde F$ constant at $e_0$ on the initial face. The restriction $\tilde F|_{\text{terminal face}} : I^{k-1} \to F$ defines a class in $\pi_{k-1}(F)$ (after verifying the boundary is constant).
   - *Hint:* The lift exists by HLP. Check well-definedness via a second lift and a homotopy.
   - *Why needed:* This is the connecting map. Without it, no long sequence — only two short ones.

2. **Exactness at $\pi_k(E)$.** Show $\ker \pi_* = \mathrm{im}\, i_*$. Use HLP to lift homotopies in $B$ to homotopies in $E$.

3. **Exactness at $\pi_k(B)$.** Show $\ker \partial = \mathrm{im}\, \pi_*$. If $\partial[f] = 0$, the boundary of the lifted disc is null-homotopic in $F$, allowing the lift to be modified to an honest sphere.

4. **Exactness at $\pi_{k-1}(F)$.** Show $\ker i_* = \mathrm{im}\, \partial$. If a sphere in $F$ becomes null-homotopic in $E$, the null-homotopy can be projected to give a sphere in $B$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Construction of the connecting map $\partial$
> **Statement:** For $k \geq 1$ and $[f] \in \pi_k(B, b_0)$, there is a well-defined element $\partial[f] \in \pi_{k-1}(F, e_0)$, constructed by lifting $f$ to a disc in $E$ with boundary in $F$.
>
> **Hint:** Represent $f$ as $I^k \to B$ with $f(\dot I^k) = b_0$. Restrict to $I^{k-1} \times \{0\} \subseteq I^k$ and view the rest as a homotopy. Lift via HLP starting from the constant map at $e_0$. The terminal value of the lift is a map $I^{k-1} \to E$ with boundary in $F = \pi^{-1}(b_0)$, providing a class in $\pi_{k-1}(F)$.
>
> **Why needed:** Without the boundary map, the long exact sequence does not exist as a long sequence — only as disconnected short pieces.
>
> > [!note]- Full proof
> > Let $f : I^k \to B$ represent $[f] \in \pi_k(B)$, with $f(\dot I^k) = b_0$. Define the **initial face** $\Sigma_0 = I^{k-1} \times \{0\} \subseteq I^k$ and the **terminal face** $\Sigma_1 = I^{k-1} \times \{1\}$. The boundary of $I^k$ decomposes as $\dot I^k = \Sigma_0 \cup \Sigma_1 \cup (\dot I^{k-1} \times I)$.
> >
> > By assumption $f|_{\Sigma_0} = b_0$ (constant), so we can view $f : \Sigma_0 \times I \to B$ as a homotopy of the constant map at $b_0$ in $B$. Define the constant lift $\tilde f_0 : \Sigma_0 \to E$ at $e_0$. By the HLP of the fibration $\pi : E \to B$, this lifts to a map $\tilde F : \Sigma_0 \times I = I^k \to E$ with $\tilde F|_{\Sigma_0} = e_0$ and $\pi \circ \tilde F = f$.
> >
> > The terminal face value $\tilde F|_{\Sigma_1} : \Sigma_1 \to E$ satisfies: (i) its image lies in $F = \pi^{-1}(b_0)$ (because $\pi \circ \tilde F|_{\Sigma_1} = f|_{\Sigma_1} = b_0$ since $\Sigma_1 \subseteq \dot I^k$); (ii) its boundary $\dot \Sigma_1 \subseteq \dot I^k$ maps to $\tilde F(\dot \Sigma_1)$; we need this to be constant at $e_0$ for the result to be a sphere class.
> >
> > For the boundary, observe $\dot \Sigma_1 \subseteq \dot I^{k-1} \times I \cup \Sigma_1$, and on this region $f = b_0$. The lift on $\dot I^{k-1} \times I$ can be required to be constant at $e_0$ (the constant lift of the constant homotopy at $b_0$, well-defined and unique starting from $\tilde F|_{\dot I^{k-1} \times \{0\}} = e_0$). So $\tilde F|_{\dot \Sigma_1} = e_0$.
> >
> > Therefore $\tilde F|_{\Sigma_1} : I^{k-1}/\dot I^{k-1} \to F$ with constant value $e_0$ on the boundary — a class in $\pi_{k-1}(F, e_0)$. Define $\partial[f] = [\tilde F|_{\Sigma_1}]$.
> >
> > Well-definedness modulo homotopy of $f$ and choice of lift: a second representative $f'$ homotopic to $f$ gives a homotopy of homotopies which lifts to a homotopy of lifts $\tilde F \simeq \tilde F'$, and the terminal-face restrictions are homotopic. Similarly two lifts of the same $f$ are homotopic by HLP applied to the homotopy of constant maps. So $\partial$ is well-defined.

> [!note]- Lemma 2: Exactness at $\pi_k(E)$
> **Statement:** $\mathrm{im}(i_* : \pi_k(F) \to \pi_k(E)) = \ker(\pi_* : \pi_k(E) \to \pi_k(B))$.
>
> **Hint:** "$\subseteq$": clear, since $\pi \circ i$ is constant. "$\supseteq$": if $[\pi \circ g] = 0$ in $\pi_k(B)$, lift the null-homotopy of $\pi \circ g$ to a homotopy of $g$, ending in a map factoring through $F$.
>
> **Why needed:** One of the three exactness statements at $\pi_k(E)$; together with Lemmas 3 and 4 these establish full exactness of the sequence.
>
> > [!note]- Full proof
> > **$\subseteq$:** If $g : S^k \to F$, then $\pi \circ i \circ g$ takes every point to $b_0$ (since $F = \pi^{-1}(b_0)$), so $\pi_* \circ i_* [g] = 0$.
> >
> > **$\supseteq$:** Let $g : S^k \to E$ with $\pi \circ g \simeq \mathrm{const}_{b_0}$ via a homotopy $H : S^k \times I \to B$ with $H(\cdot, 0) = \pi \circ g$ and $H(\cdot, 1) = b_0$. Lift $H$ via HLP starting from the given lift $g : S^k \to E$ at $t = 0$: get $\tilde H : S^k \times I \to E$ with $\tilde H(\cdot, 0) = g$ and $\pi \circ \tilde H = H$. Then $\tilde H(\cdot, 1) : S^k \to E$ has $\pi \circ \tilde H(\cdot, 1) = b_0$, so it factors through $F$. Thus $g \simeq \tilde H(\cdot, 1) = i \circ g'$ for some $g' : S^k \to F$, and $[g] = i_*[g']$.

> [!note]- Lemma 3: Exactness at $\pi_k(B)$
> **Statement:** $\mathrm{im}(\pi_* : \pi_k(E) \to \pi_k(B)) = \ker(\partial : \pi_k(B) \to \pi_{k-1}(F))$.
>
> **Hint:** "$\subseteq$": if $f = \pi \circ g$ for $g : S^k \to E$, the natural lift is $g$ itself, with boundary on the constant fibre map. "$\supseteq$": if $\partial[f] = 0$, the boundary disc in $F$ extends to a contraction, allowing the lift of $f$ to be modified to a sphere in $E$.
>
> **Why needed:** Exactness at $\pi_k(B)$, the middle group in each triple.
>
> > [!note]- Full proof
> > **$\subseteq$:** If $[f] = \pi_*[g]$, then $f = \pi \circ g$ can be lifted to $g$ directly, with terminal-face value constant (homotopic to the basepoint $e_0$). So $\partial[f] = 0$.
> >
> > **$\supseteq$:** If $\partial[f] = 0$, the terminal-face restriction $\tilde F|_{\Sigma_1}$ is null-homotopic in $F$. Use this null-homotopy to modify the lift $\tilde F$: replace $\tilde F$ on $\Sigma_1 \times [\epsilon, 1]$ with the null-homotopy contracted to the basepoint. The result is a new lift $\tilde F' : I^k \to E$ with $\tilde F'$ constant at $e_0$ on *both* $\Sigma_0$ and $\Sigma_1$, hence $\tilde F'$ collapses all of $\dot I^k$ to $e_0$, defining a sphere class $[\tilde F'] \in \pi_k(E)$. Then $\pi_*[\tilde F'] = [\pi \circ \tilde F'] = [f]$.

> [!note]- Lemma 4: Exactness at $\pi_{k-1}(F)$
> **Statement:** $\mathrm{im}(\partial : \pi_k(B) \to \pi_{k-1}(F)) = \ker(i_* : \pi_{k-1}(F) \to \pi_{k-1}(E))$.
>
> **Hint:** "$\subseteq$": the boundary class $\partial[f]$ is the boundary of a disc in $E$, hence null in $\pi_{k-1}(E)$. "$\supseteq$": if a sphere in $F$ bounds a disc in $E$, project the disc to get a sphere in $B$ whose $\partial$ recovers the original class.
>
> **Why needed:** Exactness at $\pi_{k-1}(F)$, completing the cyclic argument.
>
> > [!note]- Full proof
> > **$\subseteq$:** Given $\partial[f]$ represented by $\tilde F|_{\Sigma_1}$, the lift $\tilde F : I^k \to E$ extends this map to a disc $I^k$. So $\tilde F|_{\Sigma_1}$ bounds an $E$-disc, making $i_* \partial[f] = 0$.
> >
> > **$\supseteq$:** Let $\sigma : I^{k-1} \to F$ represent a class with $i_*[\sigma] = 0$, so there is a null-homotopy $G : I^{k-1} \times I \to E$ with $G|_{I^{k-1} \times \{0\}} = i \circ \sigma$ and $G|_{I^{k-1} \times \{1\}} = e_0$, with $G|_{\dot I^{k-1} \times I} = e_0$. Project: $\pi \circ G : I^k \to B$ has boundary (everything except $\Sigma_0 = I^{k-1} \times \{0\}$) mapping to $b_0$, so it represents a class in $\pi_k(B)$. By construction, $\partial$ of this class is $[\sigma]$.

---

# Formal Proof

> [!note]- Complete formal proof
> Combine Lemmas 1, 2, 3, 4.
>
> Step 0 — well-posedness: $F$ is path-connected (assumed), so $\pi_0(F) = 0$, ensuring the sequence terminates cleanly at $\pi_1(B) \to 1$. All base points are chosen consistently with $\pi(e_0) = b_0$, so the induced maps $i_*, \pi_*$ are well-defined.
>
> By Lemma 1, the connecting homomorphism $\partial : \pi_k(B, b_0) \to \pi_{k-1}(F, e_0)$ is well-defined for every $k \geq 1$ via the HLP construction.
>
> By Lemmas 2, 3, 4, the sequence is exact at $\pi_k(E)$, $\pi_k(B)$, and $\pi_{k-1}(F)$ respectively. Applied for every $k \geq 1$, this establishes exactness of the entire sequence
> $$\cdots \to \pi_k(F) \to \pi_k(E) \to \pi_k(B) \to \pi_{k-1}(F) \to \cdots$$
> terminating at $\pi_1(B) \to 1$ (since $\pi_*$ is surjective onto $\pi_1(B)$ when $F$ is path-connected — a fibre-connectedness fact: any loop in $B$ lifts to a path in $E$ whose endpoints can be joined within the connected fibre to give a closed loop).
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Compute $\pi_k(SU(n))$ recursively.** Apply the long exact sequence to $SU(n-1) \to SU(n) \to S^{2n-1}$ iteratively. Use $\pi_k(S^{2n-1}) = 0$ for $k < 2n - 1$ to deduce $\pi_k(SU(n)) = \pi_k(SU(n-1))$ in low degrees. Iterate down to $SU(2) = S^3$.

**Loop spaces.** Apply to the path-loop fibration $\Omega X \to PX \to X$ with $PX$ contractible. The long exact sequence collapses to $\pi_k(X) \cong \pi_{k-1}(\Omega X)$, recovering the loop-space identification.

**Covering spaces.** Apply to a covering $\tilde X \to X$ with discrete fibre $F$. Since $\pi_k(F) = 0$ for $k \geq 1$, get $\pi_k(\tilde X) \cong \pi_k(X)$ for $k \geq 2$ and short exact sequence $1 \to \pi_1(\tilde X) \to \pi_1(X) \to F \to 1$ (where $F$ becomes the deck group action).

**Stiefel manifold $V_k(\mathbb{R}^n) = SO(n)/SO(n-k)$.** Apply to the principal $SO(n-k)$-bundle $SO(n) \to V_k(\mathbb{R}^n)$, computing $\pi_*(V_k(\mathbb{R}^n))$ in terms of $\pi_*(SO(n))$ and $\pi_*(SO(n-k))$.

**Berry phase / Aharonov–Bohm.** The long exact sequence of the $U(1)$ bundle over the configuration space (or moduli space of quantum states) gives the topological obstruction to a global phase choice — exactly the Berry phase / Aharonov–Bohm phase.

---

# Bridges

- **[[Algebraic Topology II — Fundamental Group and Covering Spaces|Covering-space theory]]** — The covering-space fundamental sequence $1 \to \pi_1(\tilde X) \to \pi_1(X) \to G \to 1$ for a regular cover (with $G$ the deck group) is the *short* exact sequence one gets from the long exact sequence of the fibration $G \to \tilde X \to X$ when $G$ is a discrete (zero-dimensional) group. The higher $\pi_k$ all coincide ($\pi_k(\tilde X) = \pi_k(X)$ for $k \geq 2$), because the discrete fibre contributes nothing to higher homotopy. So covering-space theory is the discrete-fibre special case of fibration theory, and the Galois correspondence becomes a special case of the long exact sequence machinery applied to fibrations with discrete fibre.

- **Snake lemma in homological algebra.** The long exact sequence of a fibration is the homotopy-theoretic analogue of the **snake lemma** in homological algebra: a short exact sequence (here, the "exact sequence of spaces" $F \to E \to B$) produces a long exact sequence in derived invariants (here, homotopy groups). The boundary map $\partial$ plays the same algebraic role as the snake-lemma boundary. The conceptual parallel is exact: both are constructed by "lifting and observing boundaries", and both produce alternating cycles of group maps.

- **Serre spectral sequence.** The long exact sequence of a fibration in *homotopy* is the bottom row of the **Serre spectral sequence** in *homology*: the $E^2$-page $E^2_{p, q} = H_p(B; H_q(F))$ converges to $H_{p+q}(E)$. The five-term exact sequence at the bottom of the spectral sequence recovers the homological long exact sequence; the homotopy long exact sequence is a separate (but related) structure on $\pi_*$. The Serre spectral sequence is the *generalisation* of the long exact sequence to higher homological information.

- **[[Def - The Hopf Map|The Hopf map]]** — The single most important application: the long exact sequence applied to $S^1 \to S^3 \to S^2$ gives $\pi_3(S^2) = \pi_3(S^3) = \mathbb{Z}$, with the Hopf map as generator. This is the spectacular fact that motivated the whole theory of higher homotopy groups. See [[Ex - Pi_3 of S^2 is Z via the Hopf Map]].

- **[[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|Lie groups]] and Bott periodicity.** Iterating the long exact sequence over chains of inclusions $H \hookrightarrow G$ produces the homotopy groups of all classical Lie groups. Bott showed: $\pi_k(U) = \mathbb{Z}$ for $k$ odd, $0$ for $k$ even (Bott period 2); $\pi_k(O)$ has period 8 with values $\mathbb{Z}/2, \mathbb{Z}/2, 0, \mathbb{Z}, 0, 0, 0, \mathbb{Z}$. These periodicities are the foundation of **K-theory**: $K^0(\mathbb{Z}/2k\mathbb{Z}) = \pi_{-1}(BU) = \pi_0(U)$ etc., periodic of period 2 (complex K-theory) or 8 (real K-theory).

---

# Unlocked by This

> [!tip] Bott Periodicity *(from K-theory)*
> Applying the long exact sequence iteratively to the inclusions $U(n) \hookrightarrow U(n+1)$ and similar for $O(n)$, one obtains **Bott periodicity**: the homotopy groups of the stable classical groups are periodic.
> $$\pi_k(U) = \begin{cases} \mathbb{Z} & k \text{ odd} \\ 0 & k \text{ even} \end{cases}, \qquad \pi_k(O) = \begin{cases} \mathbb{Z}/2 & k \equiv 0, 1 \pmod 8 \\ \mathbb{Z} & k \equiv 3, 7 \pmod 8 \\ 0 & \text{otherwise.} \end{cases}$$
> Bott periodicity is the foundation of K-theory: $K^0(X) \cong K^{-2}(X)$ (complex) and $K^0_{\mathbb{R}}(X) \cong K^{-8}_{\mathbb{R}}(X)$ (real). The deeper interpretation is via the spaces $BU$ and $BO$: $\Omega^2 BU \simeq BU$, $\Omega^8 BO \simeq BO$.

> [!tip] Serre Spectral Sequence *(from Homological Algebra)*
> The Serre spectral sequence of a fibration $F \to E \to B$ has $E^2$-page $E^2_{p, q} = H_p(B; H_q(F))$ and converges to $H_{p+q}(E)$. It is the homological generalisation of the homotopy long exact sequence, allowing computation of $H_*(E)$ from $H_*(F)$ and $H_*(B)$. Convergence is in the Cartan–Eilenberg sense, with extensions accounting for the failure of simple multiplicativity. For a principal fibration with simply connected base, the spectral sequence often collapses, giving a Künneth-type formula $H_*(E) = H_*(B) \otimes H_*(F)$.
