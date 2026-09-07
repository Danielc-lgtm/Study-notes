---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Path-Product and the Fundamental Group"
  - "Def - Covering Space"
  - "Def - Lift of a Map"
  - "Thm - Path Lifting and Homotopy Lifting"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$S^1 = \{z \in \mathbb{C} : |z| = 1\}$, the unit circle. The base point is $1 = e^{i \cdot 0}$. The exponential map $p : \mathbb{R} \to S^1$ is $p(t) = e^{2\pi i t}$; it is a [[Def - Covering Space|covering map]] with fibre $p^{-1}(1) = \mathbb{Z}$. For a loop $\gamma : I \to S^1$ at $1$, the **winding number** is the integer $\tilde\gamma(1) - \tilde\gamma(0)$, where $\tilde\gamma$ is any lift of $\gamma$ to $\mathbb{R}$. We write $\omega_n(\theta) := e^{2\pi i n \theta}$ for the standard loop with winding number $n$. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

---

# Statement

> **Theorem ($\pi_1(S^1) = \mathbb{Z}$).** The fundamental group of the circle is the integers:
> $$\pi_1(S^1, 1) \cong \mathbb{Z},$$
> with the isomorphism given by the **winding number** $W : \pi_1(S^1, 1) \to \mathbb{Z}$, $W([\gamma]) := \tilde\gamma(1) - \tilde\gamma(0)$, where $\tilde\gamma : I \to \mathbb{R}$ is the lift of $\gamma$ through $p(t) = e^{2\pi i t}$ starting at $0$. The integer $n$ corresponds to the homotopy class $[\omega_n]$ of the standard loop $\omega_n(\theta) = e^{2\pi i n\theta}$.

This is the flagship computation of the chapter. Almost every concrete $\pi_1$ calculation in the rest of the topic reduces to this one, either directly (via product formulas, $\pi_1(T^n) = \mathbb{Z}^n$) or indirectly (via the Seifert-van Kampen theorem decomposing into pieces involving circles).

---

# Motivation

The circle is the simplest space with a non-trivial fundamental group, and it is the testbed for the entire covering-space machinery. The computation answers: how many "essentially different" ways can a loop on the circle be drawn, up to continuous deformation? The answer is, intuitively, "one for each integer winding number" — a loop that goes around once is genuinely different from a loop that stays put (different image), but also genuinely different from a loop that goes around twice (different winding count), and continuously different from going around once-in-the-other-direction (different sign). Every integer is a different homotopy class; no two distinct integers give homotopic loops.

The genuine content of the theorem is that the winding number is (a) well-defined as a homotopy invariant, and (b) all there is — every integer is realised, and the group operation on loops matches integer addition. The proof uses the universal cover $\mathbb{R} \to S^1$: every loop on the circle has a unique lift to $\mathbb{R}$ (once a starting point is chosen), and the endpoint of the lift records the winding. Homotopies lift, so homotopic loops have lifts with the same endpoint, hence the same winding. And the path-product of loops corresponds to adding the lifts' endpoints, so winding is a homomorphism.

The theorem is the model for *every* later $\pi_1$ computation. The universal-cover-plus-lifting strategy used here generalises to $\pi_1(T^n) = \mathbb{Z}^n$ (lift to $\mathbb{R}^n$), $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ (lift to $S^n$), $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$ (lift to $\mathrm{SU}(2) = S^3$), and most importantly $\pi_1(M) = \mathrm{Deck}(\widetilde M / M)$ for any space with a universal cover. Knowing $\pi_1(S^1) = \mathbb{Z}$ also unlocks the no-retraction theorem ($\pi_1(D^2) = 0 \neq \mathbb{Z} = \pi_1(S^1)$, so no continuous retraction $D^2 \to S^1$), the Brouwer fixed-point theorem in dimension 2, the fundamental theorem of algebra (every non-constant complex polynomial has a root), and the dimension invariance $\mathbb{R}^2 \not\cong \mathbb{R}^n$ for $n \neq 2$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is just "$X = S^1$." But many spaces are *secretly* circles up to homotopy, and recognising this is what lets you deploy the theorem in non-circle contexts.

The first source is **any space homotopy equivalent to $S^1$**. The annulus $\{1 < |z| < 2\}$, the punctured plane $\mathbb{R}^2 \setminus \{0\}$, the Möbius strip, $\mathbb{R}^2 \setminus K$ for a contractible compact $K$, the cylinder $S^1 \times \mathbb{R}$ — all have $\pi_1 = \mathbb{Z}$ because they all deformation-retract to $S^1$. The bridge: a deformation retraction $X \to S^1$ induces an isomorphism on $\pi_1$. Once you see "this space has the homotopy type of a circle," $\pi_1 = \mathbb{Z}$ is immediate.

The second source is **the punctured plane $\mathbb{R}^2 \setminus \{p\}$**, which deformation-retracts to $S^1$ around $p$. Loops in the punctured plane are classified by their winding number around $p$, an integer. This is the source behind the **Cauchy integral formula** in complex analysis: $\oint \frac{dz}{z - p}$ is $2\pi i$ times the winding number around $p$, which is a $\pi_1$-invariant of the loop.

The third source is **any $\mathrm{U}(1)$-bundle or $S^1$-fibre bundle**. The fibre being $S^1$ means each fibre has $\pi_1 = \mathbb{Z}$, and via the long exact sequence of a fibration, this $\mathbb{Z}$ contributes to the $\pi_1$ of the total space. The classification of $\mathrm{U}(1)$-bundles by their first Chern class in $H^2(M; \mathbb{Z})$ is downstream of $\pi_1(S^1) = \mathbb{Z}$.

The fourth source is **any 1-dimensional CW complex** with a non-trivial cycle. By taking a maximal tree, any such complex deformation-retracts to a wedge of circles. Each circle contributes a factor of $\mathbb{Z}$ to $\pi_1$, and the result is a free group $F_n$. The single-circle case (a graph with one independent cycle) gives $\pi_1 = \mathbb{Z}$.

**Targets (Output Amplification)**

The conclusion is "$\pi_1(S^1) = \mathbb{Z}$" — a single computed group. Combined with other tools, this conclusion unlocks a vast collection of consequences.

The first combination is **with functoriality**: a continuous map $f : X \to S^1$ induces a homomorphism $f_* : \pi_1(X) \to \mathbb{Z}$. The non-obvious upshot is that *every* homotopy class $[X, S^1]$ corresponds to a cohomology class in $H^1(X; \mathbb{Z})$. This is the first instance of $[X, K(G, n)] = H^n(X; G)$ — Eilenberg-MacLane spaces classifying cohomology — and it begins with $S^1 = K(\mathbb{Z}, 1)$.

The second combination is **with the no-retraction theorem**. If $r : D^2 \to S^1$ were a continuous retraction (i.e., $r|_{S^1} = \mathrm{id}$), then composing with the inclusion $i : S^1 \hookrightarrow D^2$ gives $r \circ i = \mathrm{id}_{S^1}$, which on $\pi_1$ becomes $r_* \circ i_* = \mathrm{id}_\mathbb{Z}$. But $i_* : \mathbb{Z} \to \pi_1(D^2) = 0$ is zero, so $r_* \circ i_* = 0 \neq \mathrm{id}_\mathbb{Z}$, contradiction. Combined: $\pi_1(S^1) = \mathbb{Z} \neq 0 = \pi_1(D^2)$ + functoriality $\implies$ no retraction.

The third combination is **with the Brouwer fixed-point theorem in dimension 2**. Suppose $f : D^2 \to D^2$ has no fixed point. Then for each $x \in D^2$, draw the ray from $f(x)$ through $x$ and let $r(x)$ be where it hits $S^1$. Then $r$ is a continuous retraction $D^2 \to S^1$, contradicting the no-retraction theorem. Combined: $\pi_1(S^1) = \mathbb{Z}$ + no-retraction + a ray construction $\implies$ Brouwer fixed-point. See [[Ex - The Brouwer Fixed Point Theorem in Dimension 2 via Pi_1]].

The fourth combination is **with the fundamental theorem of algebra**. For a complex polynomial $p(z) = a_n z^n + \cdots + a_0$ with $n \geq 1$, consider the map $z \mapsto p(z)/|p(z)| : S^1_R \to S^1$ where $S^1_R$ is the circle of radius $R$. For $R$ large, this map has winding number $n$ (it is homotopic to $z^n / |z^n| = z^n$, which winds $n$ times). For $R = 0$, the map is the constant $a_0/|a_0|$, with winding number $0$. So as $R$ shrinks from $\infty$ to $0$, the winding number jumps from $n$ to $0$ — impossible without $p$ vanishing somewhere. Combined: $\pi_1(S^1) = \mathbb{Z}$ + degree continuity $\implies$ FTA.

---

# Why Is It True

The intuition is the **winding-number-counting picture**: a loop on $S^1$ is fully determined, up to homotopy, by how many times and in which direction it goes around. The lift to $\mathbb{R}$ makes this manifest — by "unrolling" the circle into the real line, each integer "wrap-around" of the loop on $S^1$ becomes a $\pm 1$ displacement on $\mathbb{R}$.

**The bolded one-liner: the universal cover $\mathbb{R} \to S^1$ converts the topological question "is this loop homotopic to that one?" into the arithmetic question "do these lifts have the same endpoint?", which has a discrete (integer-valued) answer.**

In more detail:

1. **Why every loop has a well-defined winding number.** Given a loop $\gamma : I \to S^1$ at $1$, lift it to $\tilde\gamma : I \to \mathbb{R}$ starting at $0$. The endpoint $\tilde\gamma(1)$ lies in the fibre $p^{-1}(1) = \mathbb{Z}$ — it is an integer. The lift exists and is unique by path lifting.

2. **Why the winding number is homotopy-invariant.** Homotopies lift too. If $\gamma \simeq \gamma'$ via a homotopy $H : I \times I \to S^1$ rel endpoints, then $H$ lifts to $\tilde H : I \times I \to \mathbb{R}$ with $\tilde H(\cdot, 0) = \tilde\gamma$. The endpoints of the lifts $\tilde H(1, t)$ vary continuously with $t$, but they always lie in the discrete set $\mathbb{Z}$, so they are constant. So $\tilde\gamma'(1) = \tilde\gamma(1)$, and the winding number is the same.

3. **Why the winding number is a homomorphism.** Given two loops $\gamma_1, \gamma_2$ with lifts $\tilde\gamma_1, \tilde\gamma_2$ starting at $0$, the lift of $\gamma_1 \cdot \gamma_2$ starting at $0$ is: lift $\gamma_1$ first (ends at $\tilde\gamma_1(1) =: n_1 \in \mathbb{Z}$), then lift $\gamma_2$ starting at $n_1$ (which is $n_1 + \tilde\gamma_2$ — translation by $n_1$). The endpoint is $n_1 + n_2$. So $W([\gamma_1 \cdot \gamma_2]) = W([\gamma_1]) + W([\gamma_2])$.

4. **Why every integer is realised.** The standard loop $\omega_n(\theta) = e^{2\pi i n \theta}$ has lift $\tilde\omega_n(\theta) = n\theta$ (verify: $p(n\theta) = e^{2\pi i n\theta}$), endpoint $n$. So $W([\omega_n]) = n$, hence $W$ is surjective.

5. **Why $W$ is injective.** If $W([\gamma]) = 0$, then $\tilde\gamma(1) = 0 = \tilde\gamma(0)$, so $\tilde\gamma$ is a loop in $\mathbb{R}$. But $\mathbb{R}$ is contractible (simply connected), so $\tilde\gamma$ is null-homotopic in $\mathbb{R}$ via a homotopy rel endpoints. Projecting that homotopy back down to $S^1$ gives a null-homotopy of $\gamma$. So $[\gamma] = [c_1]$.

The whole proof is the universal cover doing its work: a hard topological question becomes a simple arithmetic question once you lift.

---

# What Makes This Hard

The proof has three subtleties. First, **constructing the lift** of a loop requires the path-lifting lemma, which itself needs the even-covering structure of the cover $\mathbb{R} \to S^1$. People sometimes try to construct the lift directly via the inverse function $\log : S^1 \to \mathbb{R}$, forgetting that no continuous branch of $\log$ exists on all of $S^1$. Second, **homotopy invariance of the winding number** requires *homotopy lifting*, which is a strictly stronger lemma than path lifting (the homotopy parameter has to lift continuously too); the standard error is to assume "homotopic loops have the same lift," which is wrong — they have *different* lifts that happen to share endpoints. Third, **injectivity of $W$** requires the universal cover to be simply connected, which is the only place the simple connectedness of $\mathbb{R}$ enters the proof; without this, the argument would not close.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Lift loops on $S^1$ to paths on $\mathbb{R}$ using the universal cover $p : \mathbb{R} \to S^1$, $p(t) = e^{2\pi i t}$. The endpoint of the lift (starting at $0$) is an integer — the winding number. Show it is a well-defined homomorphism $\pi_1(S^1) \to \mathbb{Z}$ (using homotopy lifting), surjective (via $\omega_n$), and injective (using simple connectedness of $\mathbb{R}$).

**Subgoal decomposition:**

1. **Path lifting.** For any path $\gamma : I \to S^1$ and any starting lift $\tilde x_0 \in p^{-1}(\gamma(0)) \subset \mathbb{R}$, there exists a unique continuous lift $\tilde\gamma : I \to \mathbb{R}$ with $p \circ \tilde\gamma = \gamma$ and $\tilde\gamma(0) = \tilde x_0$.
   - *Hint:* Subdivide $I$ finely enough that each subinterval maps into an evenly covered arc; lift each subinterval using the local inverse on the chosen sheet.
   - *Why needed:* The definition of winding number requires the lift to exist and be unique.

2. **Homotopy lifting.** For any homotopy $H : I \times I \to S^1$ and any starting lift $\tilde H_0 : I \to \mathbb{R}$ of the bottom edge, there exists a unique continuous lift $\tilde H : I \times I \to \mathbb{R}$ with $p \circ \tilde H = H$ and $\tilde H|_{I \times \{0\}} = \tilde H_0$.
   - *Hint:* Same as path lifting, but in two parameters — chop $I \times I$ into small squares lying in evenly covered preimages.
   - *Why needed:* Without homotopy lifting, the winding number is not homotopy-invariant.

3. **Well-definedness of winding number.** For a loop $\gamma$ at $1$, the endpoint of its lift starting at $0$ is an integer (since $p(\tilde\gamma(1)) = \gamma(1) = 1$ means $\tilde\gamma(1) \in p^{-1}(1) = \mathbb{Z}$). If $\gamma \simeq \gamma'$ rel endpoints, then $W([\gamma]) = W([\gamma'])$.
   - *Hint:* Lift the homotopy; the endpoints $\tilde H(1, t)$ form a continuous path in $\mathbb{Z}$, hence constant.
   - *Why needed:* The map $W : \pi_1(S^1) \to \mathbb{Z}$ is well-defined.

4. **$W$ is a homomorphism.** $W([\gamma_1] \cdot [\gamma_2]) = W([\gamma_1]) + W([\gamma_2])$.
   - *Hint:* The lift of $\gamma_1 \cdot \gamma_2$ starting at $0$ is $\tilde\gamma_1$ on $[0, \tfrac12]$ followed by $\tilde\gamma_2 + n_1$ on $[\tfrac12, 1]$, where $n_1 = \tilde\gamma_1(1)$.
   - *Why needed:* Without homomorphism property, $W$ is just a set map.

5. **$W$ is surjective.** Every integer $n$ is realised by $W([\omega_n])$ where $\omega_n(\theta) = e^{2\pi i n \theta}$.
   - *Hint:* The lift of $\omega_n$ starting at $0$ is $\tilde\omega_n(\theta) = n\theta$, endpoint $n$.
   - *Why needed:* $W$ has image $\mathbb{Z}$.

6. **$W$ is injective.** If $W([\gamma]) = 0$ then $\gamma$ is null-homotopic.
   - *Hint:* $\tilde\gamma(0) = \tilde\gamma(1) = 0$ means $\tilde\gamma$ is a loop in $\mathbb{R}$, which is simply connected; project the null-homotopy in $\mathbb{R}$ down to $S^1$.
   - *Why needed:* $W$ is a bijection.

---

# Lemma Decomposition

> [!note]- Lemma 1: Existence and uniqueness of path lifts to $\mathbb{R}$
> **Statement:** For every continuous $\gamma : I \to S^1$ and every $\tilde x_0 \in p^{-1}(\gamma(0))$, there exists a unique continuous $\tilde\gamma : I \to \mathbb{R}$ with $p \circ \tilde\gamma = \gamma$ and $\tilde\gamma(0) = \tilde x_0$.
>
> **Hint:** Use the Lebesgue number lemma to subdivide $I$ so each subinterval $\gamma$-maps into an evenly covered open arc; use the local sheet to lift one subinterval at a time.
>
> **Why needed:** Defines the winding number; this is the foundational lifting lemma for the whole proof.
>
> > [!note]- Full proof
> > $S^1$ is covered by evenly covered open arcs (e.g., the upper and lower half-circles, each of which has preimage a disjoint union of intervals in $\mathbb{R}$). Cover $\gamma(I)$ by finitely many such arcs $U_1, \dots, U_N$. By the Lebesgue number lemma applied to the cover $\{\gamma^{-1}(U_j)\}$ of the compact $I$, there is a $\delta > 0$ such that any subinterval of $I$ of length $< \delta$ maps entirely into some $U_j$. Subdivide $I$ as $0 = t_0 < t_1 < \cdots < t_k = 1$ with $t_{i+1} - t_i < \delta$. Inductively, having defined $\tilde\gamma$ on $[0, t_i]$ with $\tilde\gamma(t_i) =: \tilde y_i$, the arc $\gamma([t_i, t_{i+1}])$ lies in some evenly covered $U_j$. The component of $p^{-1}(U_j)$ containing $\tilde y_i$ is a sheet $V$ mapped homeomorphically to $U_j$ by $p$. Define $\tilde\gamma|_{[t_i, t_{i+1}]} := (p|_V)^{-1} \circ \gamma|_{[t_i, t_{i+1}]}$. Continuity follows from gluing.
> >
> > Uniqueness: if $\tilde\gamma_1, \tilde\gamma_2$ are two lifts with $\tilde\gamma_1(0) = \tilde\gamma_2(0)$, the set $\{t : \tilde\gamma_1(t) = \tilde\gamma_2(t)\}$ is non-empty, open (lift uniqueness on each sheet), and closed (preimage of the diagonal in $\mathbb{R} \times \mathbb{R}$), hence all of $I$.

> [!note]- Lemma 2: Homotopy lifting
> **Statement:** For every continuous $H : I \times I \to S^1$ and every continuous lift $\tilde H_0 : I \to \mathbb{R}$ of $H|_{I \times \{0\}}$, there is a unique continuous lift $\tilde H : I \times I \to \mathbb{R}$ with $p \circ \tilde H = H$ and $\tilde H|_{I \times \{0\}} = \tilde H_0$.
>
> **Hint:** Subdivide $I \times I$ into small enough subsquares to lie in evenly covered preimages; lift one square at a time, matching the boundary.
>
> **Why needed:** Homotopy invariance of winding number.
>
> > [!note]- Full proof
> > Cover $H(I \times I)$ by evenly covered arcs. By Lebesgue, subdivide $I \times I$ into a grid of small squares each mapping into one such arc. Lift the bottom row of squares using the prescribed bottom lift; on each subsequent row, lift each square using the unique sheet matching the already-lifted left and bottom edges (uniqueness from Lemma 1 ensures consistency). Continuity and uniqueness follow as in Lemma 1.

> [!note]- Lemma 3: Winding number is a well-defined homomorphism
> **Statement:** For a loop $\gamma$ at $1$ in $S^1$, $W([\gamma]) := \tilde\gamma(1) \in \mathbb{Z}$ (lift starting at $0$) is well-defined on the homotopy class $[\gamma]$ and satisfies $W([\gamma_1] \cdot [\gamma_2]) = W([\gamma_1]) + W([\gamma_2])$.
>
> **Hint:** Homotopy invariance is "lift the homotopy and observe endpoints stay in $\mathbb{Z}$." Homomorphism is "lift $\gamma_1$ first, then $\gamma_2$ starting where $\tilde\gamma_1$ ended."
>
> **Why needed:** Establishes the map $W : \pi_1(S^1, 1) \to \mathbb{Z}$ as a homomorphism of groups.
>
> > [!note]- Full proof
> > *Well-defined on classes:* Suppose $\gamma \simeq \gamma'$ via $H$ rel endpoints. Lift $H$ to $\tilde H$ with $\tilde H(\cdot, 0)$ the standard lift of $\gamma$ at $0$. The bottom edge $\tilde H(\cdot, 0) = \tilde\gamma$ has $\tilde H(1, 0) = \tilde\gamma(1) = W([\gamma])$. The right edge $\{1\} \times I$ maps to $\tilde H(1, t)$, with $p(\tilde H(1, t)) = H(1, t) = 1$ (rel endpoints), so $\tilde H(1, t) \in p^{-1}(1) = \mathbb{Z}$. Since $t \mapsto \tilde H(1, t)$ is continuous from $I$ to $\mathbb{Z}$, it is constant. So $\tilde H(1, 1) = \tilde H(1, 0)$. But $\tilde H(\cdot, 1)$ is a lift of $\gamma'$; its initial value $\tilde H(0, 1)$ equals $\tilde H(0, 0) = 0$ (same argument on the left edge), so $\tilde H(\cdot, 1)$ is the standard lift of $\gamma'$ starting at $0$. Hence $W([\gamma']) = \tilde H(1, 1) = \tilde H(1, 0) = W([\gamma])$.
> >
> > *Homomorphism:* Let $\tilde\gamma_1, \tilde\gamma_2$ be standard lifts. The path $\tau : I \to \mathbb{R}$ defined by $\tau(s) = \tilde\gamma_1(2s)$ on $[0, \tfrac12]$ and $\tau(s) = \tilde\gamma_1(1) + \tilde\gamma_2(2s - 1)$ on $[\tfrac12, 1]$ is continuous (the two pieces agree at $s = \tfrac12$ on $\tilde\gamma_1(1)$) and satisfies $p \circ \tau = \gamma_1 \cdot \gamma_2$ on $[0, \tfrac12]$ trivially and on $[\tfrac12, 1]$ via $p(\tilde\gamma_1(1) + \tilde\gamma_2(2s - 1)) = p(\tilde\gamma_1(1)) p(\tilde\gamma_2(2s - 1)) = 1 \cdot \gamma_2(2s - 1) = \gamma_2(2s - 1)$. So $\tau$ is the standard lift of $\gamma_1 \cdot \gamma_2$ at $0$. Its endpoint is $\tau(1) = \tilde\gamma_1(1) + \tilde\gamma_2(1) = W([\gamma_1]) + W([\gamma_2])$.

> [!note]- Lemma 4: $W$ is a bijection
> **Statement:** The winding number map $W : \pi_1(S^1, 1) \to \mathbb{Z}$ is bijective.
>
> **Hint:** Surjective via $\omega_n(\theta) = e^{2\pi i n \theta}$ with lift $n\theta$, endpoint $n$. Injective via: $\tilde\gamma$ a loop in $\mathbb{R}$, which is contractible.
>
> **Why needed:** Together with Lemma 3, gives $\pi_1(S^1) \cong \mathbb{Z}$.
>
> > [!note]- Full proof
> > *Surjective:* For $n \in \mathbb{Z}$, define $\omega_n(\theta) = e^{2\pi i n \theta}$. The lift starting at $0$ is $\tilde\omega_n(\theta) = n\theta$ (check: $p(n\theta) = e^{2\pi i n \theta} = \omega_n(\theta)$, and $\tilde\omega_n(0) = 0$). Hence $W([\omega_n]) = n$.
> >
> > *Injective:* Suppose $W([\gamma]) = 0$, so $\tilde\gamma(1) = 0 = \tilde\gamma(0)$ — $\tilde\gamma$ is a loop in $\mathbb{R}$. Since $\mathbb{R}$ is convex, the straight-line homotopy $\tilde H(s, t) = (1 - t)\tilde\gamma(s)$ contracts $\tilde\gamma$ to the constant at $0$, rel endpoints. Project: $H = p \circ \tilde H$ is a homotopy in $S^1$ from $\gamma$ to the constant loop at $1$, rel endpoints. So $[\gamma] = [c_1]$ in $\pi_1(S^1, 1)$. Hence $\ker W = \{[c_1]\}$ and $W$ is injective.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** $\pi_1(S^1, 1) \cong \mathbb{Z}$ via the winding-number map $W$.
>
> *Proof.* The covering map $p : \mathbb{R} \to S^1$, $p(t) = e^{2\pi i t}$, has fibre $p^{-1}(1) = \mathbb{Z}$ and even-cover neighbourhoods around every point of $S^1$ (e.g., open semi-circles).
>
> By Lemma 1, every path $\gamma : I \to S^1$ lifts uniquely to $\tilde\gamma : I \to \mathbb{R}$ once a starting fibre point is chosen. For a loop at $1$ starting at $0 \in \mathbb{R}$, the endpoint $\tilde\gamma(1)$ lies in $p^{-1}(\gamma(1)) = p^{-1}(1) = \mathbb{Z}$. Define
> $$W : \pi_1(S^1, 1) \to \mathbb{Z}, \qquad W([\gamma]) := \tilde\gamma(1).$$
> By Lemma 3, $W$ is well-defined on homotopy classes (homotopy lifting from Lemma 2) and is a group homomorphism. By Lemma 4, $W$ is bijective.
>
> Hence $W$ is an isomorphism, and $\pi_1(S^1, 1) \cong \mathbb{Z}$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Complex analysis: the fundamental theorem of algebra.** A non-constant complex polynomial $p(z)$ of degree $n$ must have a root. Consider $z \mapsto p(z)/|p(z)|$ on $\{|z| = R\}$; for $R$ large, this is homotopic to $z \mapsto z^n / |z^n| = z^n$ on $S^1$, with winding number $n$ on $S^1 \to S^1$. For $R = 0$, the map is constant. As $R$ varies, the winding number is constant, so if $p$ has no roots in $|z| \leq R$, the winding numbers at $R = 0$ and $R = \infty$ must agree — but they are $0$ and $n$ respectively. Contradiction. So $p$ has a root somewhere.

**Differential geometry: index of a vector field on $S^1$.** A nowhere-zero vector field on $S^1$ gives a map $S^1 \to S^1$ (the unit tangent at each point); its winding number is a $\pi_1$-invariant called the **index**. For $S^1$ this is just an integer; for higher surfaces, the sum of local indices around zeros of a vector field equals the Euler characteristic (Poincaré-Hopf). The 1-dimensional case is downstream of $\pi_1(S^1) = \mathbb{Z}$.

**Number theory: roots of unity and the cyclotomic Galois group.** Each $n$-th root of unity $\zeta_n = e^{2\pi i / n}$ corresponds to a loop $\omega_1$ traversed $n$ times — winding $n$ in $S^1$. The Galois group $\mathrm{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) = (\mathbb{Z}/n)^\times$ acts by permuting the roots, mirroring the action of the deck group $\mathbb{Z}$ on the lifts in $\mathbb{R}$ (mod $n$). The cyclotomic Galois group is essentially the algebraic shadow of $\pi_1(S^1) = \mathbb{Z}$.

**Physics: monopole charge and quantization.** In the magnetic monopole setup ([[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]]), the magnetic charge is constrained to be an integer multiple of a basic unit — the **Dirac quantization condition** — and the integer is precisely a winding number on $S^2 \setminus \{\text{poles}\}$ (where $\pi_1 = \mathbb{Z}$, by deformation retract to $S^1$). The fact that the charge is integer-valued is a direct manifestation of $\pi_1(S^1) = \mathbb{Z}$.

---

# Bridges

- **[[Thm - Path Lifting and Homotopy Lifting]]** — the engine for this theorem. Path lifting gives the existence of the lift; homotopy lifting gives the well-definedness of the winding number on homotopy classes. Without these two foundational lemmas, the theorem's proof has nothing to stand on. Both work for any covering map, not just $\mathbb{R} \to S^1$, which is why the same proof generalises to $\pi_1(T^n) = \mathbb{Z}^n$ and other deck-group computations.

- **[[Thm - Galois Correspondence for Covering Spaces]]** — this theorem is the canonical example. The universal cover of $S^1$ is $\mathbb{R}$ (simply connected); its deck group is $\mathbb{Z}$ (acting by translation); the Galois correspondence identifies $\pi_1(S^1) = \mathrm{Deck}(\mathbb{R}/S^1) = \mathbb{Z}$. The non-universal covers of $S^1$ are the $n$-fold covers $S^1 \to S^1$ via $z \mapsto z^n$, corresponding to subgroups $n\mathbb{Z} \leq \mathbb{Z}$. So the entire lattice of covers of $S^1$ is the lattice of subgroups of $\mathbb{Z}$.

- **Brouwer fixed-point theorem in dimension 2** — proved as a corollary of $\pi_1(S^1) = \mathbb{Z}$ and $\pi_1(D^2) = 0$ via the no-retraction argument. See [[Ex - The Brouwer Fixed Point Theorem in Dimension 2 via Pi_1]]. The two-dimensional Brouwer is the prototype for many higher-dimensional fixed-point and retraction theorems; the higher-dimensional cases use higher homotopy groups.

- **The fundamental theorem of algebra** — proved via winding number: a polynomial of degree $n$ has the property that the map $z \mapsto p(z)/|p(z)|$ on $S^1_R$ has winding number $n$ for large $R$ and $0$ for $R = 0$, so it must pass through a zero somewhere. The same winding-number argument proves topological invariance of degree in any dimension; the $S^1$ case is the original.

- **Hurewicz in degree 1** — $H_1(S^1; \mathbb{Z}) = \mathbb{Z}$ matches $\pi_1(S^1)^{\mathrm{ab}} = \mathbb{Z}^{\mathrm{ab}} = \mathbb{Z}$ trivially (since $\mathbb{Z}$ is already abelian). For $S^1$ the Hurewicz theorem is a tautology, but it sets up the pattern: the lowest-degree homotopy and homology groups agree, with all higher-degree algebraic shadow following.
