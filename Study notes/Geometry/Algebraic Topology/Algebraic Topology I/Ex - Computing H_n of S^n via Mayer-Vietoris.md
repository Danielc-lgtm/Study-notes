---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Thm - Mayer-Vietoris for Singular Homology"
  - "Thm - Singular Homology of the Sphere"
  - "Thm - Homotopy Invariance of Singular Homology"
tags: [geometry, algebraic-topology, sphere, mayer-vietoris]
---

# Problem Statement

Compute $H_p(S^n; \mathbb{Z})$ for all $p$ and all $n \geq 1$, using [[Thm - Mayer-Vietoris for Singular Homology|Mayer–Vietoris]] applied to the cover of $S^n$ by two open hemispheres.

**Recall:**

The sphere $S^n = \{x \in \mathbb{R}^{n+1} : \|x\| = 1\}$. The open upper hemisphere is $U_+ = S^n \setminus \{-e_{n+1}\}$ (the sphere minus the south pole, slightly thickened to be open); the open lower hemisphere is $U_- = S^n \setminus \{e_{n+1}\}$. Both are open in $S^n$, both cover $S^n$ together, and each is contractible (homeomorphic to $\mathbb{R}^n$ via stereographic projection from the missing pole). Their intersection $U_+ \cap U_- = S^n \setminus \{\pm e_{n+1}\}$ deformation-retracts onto the equator $\{x \in S^n : x_{n+1} = 0\} \cong S^{n-1}$.

![[Thm - Mayer-Vietoris for Singular Homology#Statement]]

By [[Thm - Homotopy Invariance of Singular Homology|homotopy invariance]], $H_*(U_\pm; \mathbb{Z}) = H_*(\text{point}; \mathbb{Z})$ (contractible) and $H_*(U_+ \cap U_-; \mathbb{Z}) = H_*(S^{n-1}; \mathbb{Z})$.

---

# Convergent Strategy

**Problem class:** This is a Mayer–Vietoris-inductive computation: given a space with a natural two-piece cover, compute its homology by setting up the long exact sequence, identifying which terms vanish by contractibility (or known homology of intersections), and reading off the remaining isomorphisms. The class is "homology of a space via Mayer–Vietoris induction on a known cover" — the standard technique for computing $H_*(S^n)$, $H_*(T^n)$, and other spaces with two-piece decompositions.

**Assumption pattern:** $S^n$ has the standard cover by two open hemispheres, each diffeomorphic to $\mathbb{R}^n$ (hence contractible, with $H_*(U_\pm) = H_*(\text{point})$). Their intersection is homotopy-equivalent to $S^{n-1}$, one dimension lower than $S^n$ — providing the inductive base. So Mayer–Vietoris gives us a sequence connecting $H_*(S^n)$ to $H_*(\text{point}) \oplus H_*(\text{point})$ and $H_*(S^{n-1})$, and the latter is known by induction.

**Theorem routing:** Apply [[Thm - Mayer-Vietoris for Singular Homology|Mayer–Vietoris]] with the cover $\{U_+, U_-\}$. Use [[Thm - Homotopy Invariance of Singular Homology|homotopy invariance]] to identify $H_*(U_\pm) = H_*(\text{point}) = \mathbb{Z}[\delta_{p0}]$ and $H_*(U_+ \cap U_-) = H_*(S^{n-1})$ (the equator after deformation retraction). The long exact sequence then determines $H_*(S^n)$ from $H_*(S^{n-1})$. The base case is $S^0$ (two points), whose homology is $\mathbb{Z}^2$ in degree zero.

**Key decision point:** The non-obvious step is handling the special case $p = 1, n = 1$ separately from the inductive case $p \geq 2$. For $p \geq 2$ the flanking terms in Mayer–Vietoris are zero (positive-degree homology of contractibles), giving the clean recursion $H_p(S^n) = H_{p-1}(S^{n-1})$. But for $p = 1$, the $H_0$ flanking terms are non-zero, and one must track them through the exact sequence: $H_1(S^n) = \ker(\text{diagonal} : H_0(S^{n-1}) \to H_0(U_+) \oplus H_0(U_-)) = \ker((g, g) \mapsto (g + g', g + g'))$, which simplifies appropriately. Handling this base case correctly is what gets the $H_1(S^1) = \mathbb{Z}$ right.

---

# Legal Operations Used

1. **Apply Mayer–Vietoris with a two-piece cover** (operation 5 from the topic page). Set up the long exact sequence using the open hemisphere cover.

2. **Use homotopy invariance to replace cover elements with simpler spaces** (operation 6). $U_+$ and $U_-$ are contractible; $U_+ \cap U_-$ is homotopy equivalent to $S^{n-1}$.

3. **Read $H_0$ as a path-component count** (operation 7). $H_0(S^n) = \mathbb{Z}$ for $n \geq 1$ (connected), $H_0(S^0) = \mathbb{Z}^2$ (two points).

4. **Inductive application** (analogous to operation 5, iterated). The same Mayer–Vietoris cover applied to $S^{n-1}$ gives $H_*(S^{n-1})$ from $H_*(S^{n-2})$, all the way down to the base case $S^0$.

---

# Hints

> [!note]- Hint 1
> Set up the Mayer–Vietoris sequence for the cover $\{U_+, U_-\}$ of $S^n$. What do you know about the homology of $U_\pm$ and $U_+ \cap U_-$ from contractibility and homotopy invariance?

> [!note]- Hint 2
> In degrees $p \geq 2$, the terms $H_p(U_+) \oplus H_p(U_-)$ and $H_{p-1}(U_+) \oplus H_{p-1}(U_-)$ are both zero (positive-degree homology of contractibles). What does the Mayer–Vietoris sequence simplify to in these degrees? You should get a clean isomorphism between $H_p(S^n)$ and something one dimension lower.

> [!note]- Hint 3
> The recursion $H_p(S^n) = H_{p-1}(S^{n-1})$ for $p \geq 2$ gives the inductive structure. For the base case, you need to compute $H_*(S^0)$ separately, and then handle $H_1(S^1)$ as a special case where the $H_0$ flanking terms are non-zero. The key is identifying the diagonal map $H_0(S^0) = \mathbb{Z}^2 \to H_0(U_+) \oplus H_0(U_-) = \mathbb{Z}^2$ — it sends $(g_N, g_S)$ to $(g_N + g_S, g_N + g_S)$, an image-of-rank-$1$ map.

---

# Solution

The proof breaks into four steps. Step 1 sets up the Mayer–Vietoris sequence. Step 2 handles the base case $S^0$ (and the special case $H_1(S^1)$). Step 3 derives the recursion $H_p(S^n) = H_{p-1}(S^{n-1})$ for $p \geq 2$. Step 4 iterates the recursion to get the final answer.

**Step 1: Set up the Mayer–Vietoris sequence.**

The cover $\{U_+, U_-\}$ of $S^n$ has $U_+ \cup U_- = S^n$, $U_+ \cap U_- = S^n \setminus \{\pm e_{n+1}\} \simeq S^{n-1}$. By [[Thm - Mayer-Vietoris for Singular Homology|Mayer–Vietoris]] the long exact sequence is
$$
\cdots \to H_p(S^{n-1}) \xrightarrow{(i_*, i_*)} H_p(\text{pt}) \oplus H_p(\text{pt}) \xrightarrow{j_* - j_*} H_p(S^n) \xrightarrow{\delta} H_{p-1}(S^{n-1}) \to \cdots
$$
where we have already substituted $H_p(U_\pm) = H_p(\text{pt})$ (contractibility) and $H_p(U_+ \cap U_-) = H_p(S^{n-1})$ (homotopy equivalence to the equator).

> [!note]- Derivation
> The cover is $\{U_+, U_-\}$. Each $U_\pm$ deformation-retracts onto its central point (the missing pole, *almost* — actually, $U_\pm = S^n \setminus \{\text{one pole}\}$ deformation-retracts onto the other pole or onto any single point in $U_\pm$). So $U_\pm$ is contractible, and by homotopy invariance $H_*(U_\pm) = H_*(\text{pt})$, namely $H_0 = \mathbb{Z}$ and $H_p = 0$ for $p \geq 1$.
>
> The intersection $U_+ \cap U_- = S^n \setminus \{\pm e_{n+1}\}$ is the sphere minus two antipodal points. The deformation $H((x_1, \dots, x_n, z), t) = ((x_1, \dots, x_n, (1-t)z))/\|\text{numerator}\|$ continuously slides $(x_1, \dots, x_n, z)$ toward the equator $\{z = 0\}$, giving a strong deformation retract of $U_+ \cap U_-$ onto the equator $\cong S^{n-1}$. So $H_*(U_+ \cap U_-) = H_*(S^{n-1})$.
>
> The Mayer–Vietoris sequence is the general one with these substitutions.

**Step 2: Base case $S^0$ and the special case $H_1(S^1)$.**

$S^0 = \{N, S\}$ is two points. $H_0(S^0; \mathbb{Z}) = \mathbb{Z}^2$ (two components), $H_p(S^0; \mathbb{Z}) = 0$ for $p \geq 1$.

For $H_1(S^1)$, apply Mayer–Vietoris to the cover $\{U_+, U_-\}$ of $S^1$ with $U_+ \cap U_- \simeq S^0$. The relevant portion of the sequence:
$$
0 \to H_1(S^1) \xrightarrow{\delta} H_0(S^0) \xrightarrow{(i_*, i_*)} H_0(U_+) \oplus H_0(U_-) \xrightarrow{j_* - j_*} H_0(S^1) \to 0,
$$
which substitutes to
$$
0 \to H_1(S^1) \to \mathbb{Z}^2 \xrightarrow{\alpha} \mathbb{Z}^2 \xrightarrow{\beta} \mathbb{Z} \to 0.
$$
The map $\alpha : \mathbb{Z}^2 \to \mathbb{Z}^2$ sends $(g_N, g_S)$ to $(g_N + g_S, g_N + g_S)$ (both poles go to the unique component of each hemisphere). So $\mathrm{im}(\alpha) = \{(g, g) : g \in \mathbb{Z}\} \cong \mathbb{Z}$, the diagonal. The map $\beta : \mathbb{Z}^2 \to \mathbb{Z}$ sends $(a, b) \mapsto a - b$, with kernel the diagonal and image $\mathbb{Z}$. Exactness at $\mathbb{Z}^2$ (the first one) requires $\mathrm{im}(H_1(S^1) \to \mathbb{Z}^2) = \ker \alpha = \{(g_N, g_S) : g_N + g_S = 0\} \cong \mathbb{Z}$. So $H_1(S^1) \cong \mathbb{Z}$.

> [!note]- Derivation
> *Base case $S^0$:* $S^0$ is a discrete space with two points. The chain complex has $C_0(S^0; \mathbb{Z}) = \mathbb{Z} \cdot N \oplus \mathbb{Z} \cdot S = \mathbb{Z}^2$, and in higher degrees $C_p(S^0; \mathbb{Z})$ is generated by constant simplices (one per point), with boundary maps computing the chain complex of two disjoint copies of a point. By [[Ex - Singular Homology of a Point|the homology of a point]], $H_*(\{N\}) = \mathbb{Z}$ in degree zero, zero elsewhere; same for $\{S\}$. Their disjoint union gives $H_0(S^0) = \mathbb{Z}^2$ and $H_p(S^0) = 0$ for $p \geq 1$.
>
> *Special case $H_1(S^1)$:* The Mayer–Vietoris sequence for $S^1$ with the hemisphere cover has $H_1(U_\pm) = 0$ and $H_1(U_+ \cap U_-) = H_1(S^0) = 0$. So the sequence simplifies as stated.
>
> Computing $\alpha : H_0(S^0) \to H_0(U_+) \oplus H_0(U_-)$: the generators of $H_0(S^0) = \mathbb{Z}^2$ are $[N]$ and $[S]$ — the classes of the two points. The inclusion $S^0 \hookrightarrow U_\pm$ sends both points into the connected space $U_\pm$. Both go to the unique connected component of $U_\pm$, so both have the same homology class in $H_0(U_\pm) = \mathbb{Z}$. Specifically, $i_{U_*}(N) = i_{U_*}(S) = [\text{any point in } U_\pm]$ = the generator of $H_0(U_\pm) = \mathbb{Z}$. So $\alpha(g_N, g_S) = (g_N + g_S, g_N + g_S)$.
>
> The image of $\alpha$ is the diagonal $\{(g, g) : g \in \mathbb{Z}\} \cong \mathbb{Z}$. The kernel of $\alpha$ is $\{(g_N, g_S) : g_N + g_S = 0\} = \{(g_N, -g_N) : g_N \in \mathbb{Z}\} \cong \mathbb{Z}$.
>
> By exactness at $H_0(S^0) = \mathbb{Z}^2$, $\mathrm{im}(\delta : H_1(S^1) \to H_0(S^0)) = \ker(\alpha)$. Since $\delta$ is also injective (preceded by $0 \to H_1(S^1)$, and $H_1(U_\pm) = 0$), $H_1(S^1) \cong \ker(\alpha) \cong \mathbb{Z}$.

**Step 3: The recursion $H_p(S^n) = H_{p-1}(S^{n-1})$ for $p \geq 2$.**

In degree $p \geq 2$, the Mayer–Vietoris sequence reads
$$
\underbrace{H_p(U_+) \oplus H_p(U_-)}_{=0,\ p \geq 1} \to H_p(S^n) \xrightarrow{\delta} H_{p-1}(U_+ \cap U_-) \to \underbrace{H_{p-1}(U_+) \oplus H_{p-1}(U_-)}_{= 0,\ p \geq 2},
$$
giving
$$
0 \to H_p(S^n) \xrightarrow{\delta} H_{p-1}(S^{n-1}) \to 0.
$$
Exactness forces $\delta$ to be an isomorphism: $H_p(S^n) \cong H_{p-1}(S^{n-1})$ for $p \geq 2$ and $n \geq 1$.

> [!note]- Derivation
> For $p \geq 2$: the term $H_p(U_+) \oplus H_p(U_-) = 0$ since $U_\pm$ are contractible and $p \geq 1$. The term $H_{p-1}(U_+) \oplus H_{p-1}(U_-) = 0$ since $p - 1 \geq 1$ and $U_\pm$ are contractible.
>
> The Mayer–Vietoris sequence becomes a short exact sequence $0 \to H_p(S^n) \xrightarrow{\delta} H_{p-1}(S^{n-1}) \to 0$, forcing $\delta$ to be both injective (kernel from the left, $= 0$) and surjective (image to the right, $= 0$). So $\delta$ is an isomorphism.

**Step 4: Iterate the recursion.**

Starting from $H_*(S^0)$ (Step 2), apply the recursion $H_p(S^n) = H_{p-1}(S^{n-1})$ for $p \geq 2$ and the special-case computation $H_1(S^n)$ for the $p = 1$ slot. We get:
- $H_*(S^0)$: $\mathbb{Z}^2, 0, 0, 0, \dots$.
- $H_*(S^1)$: $\mathbb{Z}, \mathbb{Z}, 0, 0, \dots$. ($H_0 = \mathbb{Z}$ from connectedness, $H_1 = \mathbb{Z}$ from Step 2, $H_p = 0$ for $p \geq 2$ from the recursion applied to $H_0(S^0) = \mathbb{Z}^2$... wait, this gives $H_2(S^1) = H_1(S^0) = 0$, $H_3(S^1) = H_2(S^0) = 0$, $\dots$, all zero. ✓)
- $H_*(S^2)$: $\mathbb{Z}, 0, \mathbb{Z}, 0, 0, \dots$. ($H_0 = \mathbb{Z}$ from connectedness, $H_1 = 0$ by a parallel argument to Step 2 with $H_1(S^1) = \mathbb{Z}$ now giving the right answer, $H_2 = H_1(S^1) = \mathbb{Z}$, $H_p = 0$ for $p \geq 3$ from the recursion.)
- In general, $H_*(S^n)$: $\mathbb{Z}$ in degrees $0$ and $n$, zero elsewhere, for $n \geq 1$.

> [!note]- Derivation
> Inductive step: assume $H_*(S^{n-1})$ has $\mathbb{Z}$ in degrees $0$ and $n-1$, zero elsewhere.
>
> For $H_*(S^n)$:
> - $H_0(S^n) = \mathbb{Z}$ (connected).
> - $H_p(S^n) = H_{p-1}(S^{n-1})$ for $p \geq 2$. By induction, $H_{p-1}(S^{n-1}) = \mathbb{Z}$ if $p - 1 = n - 1$ (i.e. $p = n$) and zero otherwise (for $p - 1 \in \{0, n-1\}$, but $p \geq 2$ rules out $p = 1$). So $H_n(S^n) = \mathbb{Z}$ and $H_p(S^n) = 0$ for $2 \leq p \neq n$.
> - $H_1(S^n)$: by a parallel argument to Step 2 (Mayer–Vietoris with $H_0(U_\pm) = \mathbb{Z}$ and $H_0(S^{n-1}) = \mathbb{Z}$ now, instead of $\mathbb{Z}^2$). The sequence becomes $0 \to H_1(S^n) \to H_0(S^{n-1}) \to H_0(U_+) \oplus H_0(U_-) \to H_0(S^n) \to 0$, i.e. $0 \to H_1(S^n) \to \mathbb{Z} \to \mathbb{Z}^2 \to \mathbb{Z} \to 0$. The map $\mathbb{Z} \to \mathbb{Z}^2$ sends $1 \mapsto (1, 1)$ (the generator of $H_0(S^{n-1})$ goes to the same generator of both $H_0(U_\pm)$). This is injective, so $H_1(S^n) = \ker = 0$. ✓

> [!note]- Complete formal solution
> **Theorem.** $H_p(S^n; \mathbb{Z}) = \mathbb{Z}$ for $p = 0, n$ and zero otherwise, for $n \geq 1$.
>
> *Proof.* By induction on $n$.
>
> **Base case ($n = 1$).** Apply Mayer–Vietoris to the cover $\{U_+, U_-\}$ of $S^1$. $U_\pm$ are contractible, $U_+ \cap U_- \simeq S^0$ (two points). The relevant slice of the sequence:
> $$
> 0 \to H_1(S^1) \to H_0(S^0) = \mathbb{Z}^2 \xrightarrow{\alpha} H_0(U_+) \oplus H_0(U_-) = \mathbb{Z}^2 \xrightarrow{\beta} H_0(S^1) = \mathbb{Z} \to 0.
> $$
> The map $\alpha(g_N, g_S) = (g_N + g_S, g_N + g_S)$ has image the diagonal $\{(g, g)\} \cong \mathbb{Z}$ and kernel $\{(g, -g)\} \cong \mathbb{Z}$. By exactness, $H_1(S^1) = \ker \alpha = \mathbb{Z}$.
>
> Also $H_0(S^1) = \mathbb{Z}$ (connected) and $H_p(S^1) = H_{p-1}(S^0) = 0$ for $p \geq 2$ (using the recursion below with $n = 1$).
>
> **Inductive step.** Assume the theorem for $S^{n-1}$. By the Mayer–Vietoris cover of $S^n$ and the contractibility of $U_\pm$:
>
> *For $p \geq 2$:* the sequence gives $0 \to H_p(S^n) \xrightarrow{\delta} H_{p-1}(S^{n-1}) \to 0$, an isomorphism. By induction $H_{p-1}(S^{n-1}) = \mathbb{Z}$ if $p - 1 = n - 1$ (i.e. $p = n$) and zero otherwise. So $H_n(S^n) = \mathbb{Z}$ and $H_p(S^n) = 0$ for $2 \leq p \neq n$.
>
> *For $p = 1$:* the sequence
> $$
> 0 \to H_1(S^n) \to H_0(S^{n-1}) = \mathbb{Z} \to H_0(U_+) \oplus H_0(U_-) = \mathbb{Z}^2 \to H_0(S^n) = \mathbb{Z} \to 0
> $$
> has the middle map $\mathbb{Z} \to \mathbb{Z}^2$ sending $1 \mapsto (1, 1)$ (injective). So $H_1(S^n) = \ker = 0$.
>
> *For $p = 0$:* $H_0(S^n) = \mathbb{Z}$ (connected).
>
> Combining, $H_p(S^n) = \mathbb{Z}$ for $p = 0, n$ and zero otherwise. $\qquad\blacksquare$

---

# Key Takeaways

**Mayer–Vietoris reduces the global homology of a space to local pieces plus overlap data.** The strategy "cover by two simpler pieces, compute their homology, take the long exact sequence" is the universal computational technique in singular homology. When the pieces are contractible (so their homology is just $\mathbb{Z}$ in degree zero), the sequence simplifies dramatically and the homology of the union is determined by the homology of the overlap, possibly shifted in dimension. The recursion $H_p(S^n) = H_{p-1}(S^{n-1})$ for $p \geq 2$ is the cleanest example — sphere homology shifts up by one dimension as you go up the dimension ladder. This pattern recurs in *every* iterated Mayer–Vietoris computation: each Mayer–Vietoris application gives a long exact sequence; the "interesting" connecting map is a degree-shifting isomorphism when the cover elements are contractible.

**The base case $n = 0$ is structurally different from $n \geq 1$.** $S^0$ is two points (disconnected), so $H_0(S^0) = \mathbb{Z}^2$, not $\mathbb{Z}$. This is the source of the special-case handling for $H_1(S^1)$: the Mayer–Vietoris sequence in degree $1$ involves $H_0$ of the intersection (which is $\mathbb{Z}^2$ for $n = 1$, $\mathbb{Z}$ for $n \geq 2$), and the diagonal map's image is what carves out $H_1(S^n)$. For $n = 1$ specifically, the diagonal map $\mathbb{Z}^2 \to \mathbb{Z}^2$ has $1$-dimensional image, so $H_1(S^1) = \mathbb{Z}$. For $n \geq 2$, the map $\mathbb{Z} \to \mathbb{Z}^2$ is injective (the diagonal $1 \mapsto (1, 1)$), so $H_1(S^n) = 0$. The transition from "$\mathbb{Z}^2$ source" to "$\mathbb{Z}$ source" at the inductive step is what makes higher-dimensional spheres have $H_1 = 0$ while $H_1(S^1) = \mathbb{Z}$.

**The recursion mirrors the suspension isomorphism.** $S^n$ is (homeomorphic to) the suspension $\Sigma S^{n-1}$ — two cones over $S^{n-1}$ glued along $S^{n-1}$. The reduced suspension isomorphism $\tilde H_p(\Sigma X) = \tilde H_{p-1}(X)$ gives $\tilde H_p(S^n) = \tilde H_{p-1}(S^{n-1})$, the same recursion as Mayer–Vietoris. The two approaches give the same answer via different routes: Mayer–Vietoris is the cover-based view; suspension is the gluing-based view. Both are special cases of the more general "shift dimension by one via a homotopy operation" principle, which appears in many other contexts (the Freudenthal suspension theorem, the stable homotopy category, the loop space).

**The fundamental class $[S^n]$ generates $H_n(S^n; \mathbb{Z}) = \mathbb{Z}$.** Once we know $H_n(S^n) = \mathbb{Z}$, we have a natural choice of generator: the **fundamental class**, the orientation cycle obtained from a triangulation of $S^n$ with consistent orientation signs. This generator is unique up to sign (the two orientations of the sphere). It is the central object connecting smooth and topological invariants of the sphere — it pairs against the volume form via $\int_{S^n} \omega_S$ = volume, and it appears in Poincaré duality as the cap-product partner. The construction of the fundamental class from a Mayer–Vietoris computation is implicit: at each inductive step, the generator of $H_p(S^n)$ comes from the generator of $H_{p-1}(S^{n-1})$ via the connecting map $\delta$, which has a concrete realisation as "the boundary of a contractible filling."
