---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Higher Homotopy Group"
  - "Thm - Hurewicz Theorem (Statement)"
  - "Def - Singular Homology"
tags: [geometry, algebraic-topology, homotopy]
---

# Problem Statement

Show that $\pi_n(S^n) = \mathbb{Z}$ for every $n \geq 1$, with the integer attached to a continuous based map $f : S^n \to S^n$ being the **Brouwer degree** of $f$. The identity map is the generator.

**Recall:**

The objects in play are higher homotopy groups, singular homology of the sphere, the Hurewicz map, and the degree of a map.

![[Def - Higher Homotopy Group#The Definition]]

The [[Algebraic Topology I — Singular Homology and the de Rham Theorem|singular homology]] of the $n$-sphere is

$$H_k(S^n; \mathbb{Z}) = \begin{cases} \mathbb{Z} & k = 0 \text{ or } k = n \\ 0 & \text{otherwise.} \end{cases}$$

The fundamental class $[S^n] \in H_n(S^n; \mathbb{Z}) = \mathbb{Z}$ is the generator (corresponding to the standard orientation).

For a continuous map $f : S^n \to S^n$, the **Brouwer degree** $\deg(f) \in \mathbb{Z}$ is the integer such that $f_* : H_n(S^n; \mathbb{Z}) \to H_n(S^n; \mathbb{Z})$ is multiplication by $\deg(f)$. Equivalently, for a smooth map $f$ and a regular value $p$, $\deg(f) = \sum_{x \in f^{-1}(p)} \mathrm{sgn}(\det Df_x)$ — the signed count of preimages of any regular value.

![[Thm - Hurewicz Theorem (Statement)#Statement]]

The sphere $S^n$ is **$(n-1)$-connected**: $\pi_k(S^n) = 0$ for $0 \leq k \leq n - 1$.

---

# Convergent Strategy

**Problem class.** This is a **compute a homotopy group of a sphere** problem. As the [[Algebraic Topology III — Higher Homotopy and Chern Forms#Problem-Solving Strategy|topic page's problem-solving strategy]] notes, for spheres the standard tool is either Hurewicz (when the connectivity is right) or the long exact sequence of a fibration. Here the connectivity is exactly right: $S^n$ is $(n-1)$-connected, so Hurewicz applies at degree $n$.

**Assumption pattern.** The single hypothesis is the topological structure of $S^n$. The connectivity $\pi_k(S^n) = 0$ for $k < n$ is needed to *enable* the Hurewicz theorem at degree $n$. This connectivity itself is a fact about spheres: a map $S^k \to S^n$ for $k < n$ misses a point (by Sard), so factors through a contractible space (the sphere minus a point), hence is null-homotopic. The integer-cohomology fact $H_n(S^n; \mathbb{Z}) = \mathbb{Z}$ is the well-known cellular homology computation: $S^n$ has CW structure with one 0-cell and one $n$-cell, giving cellular chain complex $\mathbb{Z} \to 0 \to \cdots \to 0 \to \mathbb{Z}$, hence $H_n = \mathbb{Z}$.

**Theorem routing.** The route is straightforward via the [[Thm - Hurewicz Theorem (Statement)|Hurewicz theorem]]:

$$\pi_n(S^n) \xrightarrow[\sim]{h_n} H_n(S^n; \mathbb{Z}) = \mathbb{Z}.$$

Hurewicz gives the isomorphism; the homology computation gives $\mathbb{Z}$ on the right. The identification of the integer with the Brouwer degree comes from the explicit form of the Hurewicz map: $h_n([f]) = f_*([S^n])$, and the degree is by definition the integer making $f_* = \deg(f) \cdot \mathrm{id}$ on $H_n$.

**Key decision point.** The non-obvious choice is to invoke Hurewicz rather than try to construct the isomorphism by direct homotopy-theoretic means. Direct construction (showing that two maps of the same degree are homotopic) is possible but technical — it requires the **Hopf degree theorem**, which is essentially a special case of Hurewicz. The cleanest path is Hurewicz, which packages the technical content into a general theorem applicable in many other situations.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Algebraic Topology III — Higher Homotopy and Chern Forms#Legal Operations|the topic page's Legal Operations]]:

1. **Compute $\pi_n$ via Hurewicz** (operation 2). The connectivity of $S^n$ enables Hurewicz at the relevant degree, reducing the homotopy computation to the homology one.

2. **Recognise a homotopy class as a degree** (operation 9). The integer in $\pi_n(S^n) = \mathbb{Z}$ is identified with the Brouwer degree via the explicit form of the Hurewicz map.

---

# Hints

> [!note]- Hint 1
> What is the connectivity of $S^n$? Is there a theorem that converts homotopy into homology when the connectivity is high enough?

> [!note]- Hint 2
> $S^n$ is $(n-1)$-connected: $\pi_k(S^n) = 0$ for $k < n$. The first nonzero homotopy group is $\pi_n$. The Hurewicz theorem says that the first nonzero $\pi_n$ equals $H_n(S^n; \mathbb{Z})$ for an $(n-1)$-connected space.

> [!note]- Hint 3
> $H_n(S^n; \mathbb{Z}) = \mathbb{Z}$ by the cellular CW structure (one 0-cell, one $n$-cell). The Hurewicz isomorphism $h_n : \pi_n(S^n) \to H_n(S^n) = \mathbb{Z}$ sends $[f]$ to $f_*([S^n])$, which is by definition $\deg(f) \cdot [S^n]$. So $h_n([f]) = \deg(f)$.

---

# Solution

The proof has two steps. Step 1 establishes the connectivity needed for Hurewicz. Step 2 applies Hurewicz to conclude $\pi_n(S^n) = H_n(S^n) = \mathbb{Z}$ and identifies the integer with the Brouwer degree.

**Step 1: $S^n$ is $(n-1)$-connected.**

Claim: $\pi_k(S^n) = 0$ for $0 \leq k \leq n - 1$.

> [!note]- Derivation
> For $k = 0$: $S^n$ is path-connected for $n \geq 1$, so $\pi_0 = 0$ (one path-component, with the basepoint).
>
> For $1 \leq k < n$: a continuous map $f : S^k \to S^n$ is homotopic to a smooth map (by smoothing approximation). A smooth map $f : S^k \to S^n$ with $k < n$ cannot be surjective: by **Sard's theorem**, the set of critical values of $f$ has measure zero in $S^n$, and the image of $f$ is a $k$-dimensional set, also measure zero. So there is a point $p \in S^n$ not in the image of $f$.
>
> Then $f$ factors through $S^n \setminus \{p\}$, which is homeomorphic to $\mathbb{R}^n$ (via stereographic projection from $p$). Since $\mathbb{R}^n$ is contractible, the inclusion $\mathbb{R}^n \hookrightarrow S^n$ is null-homotopic, so $f$ is null-homotopic. Hence $[f] = 0$ in $\pi_k(S^n)$.
>
> This proves $\pi_k(S^n) = 0$ for $k < n$.

**Step 2: Apply Hurewicz to compute $\pi_n(S^n) = \mathbb{Z}$, with generator the identity map.**

By Step 1, $S^n$ is $(n-1)$-connected. By the [[Thm - Hurewicz Theorem (Statement)|Hurewicz theorem]] at degree $n$, the Hurewicz map

$$h_n : \pi_n(S^n) \to H_n(S^n; \mathbb{Z})$$

is an isomorphism.

> [!note]- Derivation
> The Hurewicz theorem states: for a path-connected space $X$ that is $(n-1)$-connected (with $n \geq 2$), the Hurewicz map $h_n : \pi_n(X) \to H_n(X; \mathbb{Z})$ is an isomorphism. For $n = 1$, the theorem says $h_1 : \pi_1(X)^{\mathrm{ab}} \to H_1(X; \mathbb{Z})$ is an isomorphism; for $S^1$, $\pi_1(S^1) = \mathbb{Z}$ is already abelian, so $\pi_1(S^1) = H_1(S^1; \mathbb{Z}) = \mathbb{Z}$.
>
> For $S^n$ with $n \geq 2$: $S^n$ is $(n-1)$-connected (Step 1), so Hurewicz applies at degree $n$: $\pi_n(S^n) \cong H_n(S^n; \mathbb{Z})$.
>
> Now compute $H_n(S^n; \mathbb{Z})$. The standard CW structure on $S^n$ has one 0-cell and one $n$-cell. The cellular chain complex is $\mathbb{Z}$ in degrees 0 and $n$ with all boundaries zero (the attaching map of the $n$-cell collapses $S^{n-1}$ to a point, contributing zero in cellular boundary). So $H_n(S^n; \mathbb{Z}) = \mathbb{Z}$, generated by the fundamental class $[S^n]$.
>
> Combining: $\pi_n(S^n) \cong \mathbb{Z}$, generated by the class that maps to $[S^n]$ under Hurewicz. The Hurewicz map sends $[\mathrm{id}_{S^n}]$ to $(\mathrm{id}_{S^n})_*([S^n]) = [S^n]$ (the identity map preserves the fundamental class). So $[\mathrm{id}_{S^n}]$ is the generator.

**Step 3: The integer is the Brouwer degree.**

The Hurewicz map sends $[f] \in \pi_n(S^n)$ to $f_*([S^n]) \in H_n(S^n; \mathbb{Z})$. By definition, $f_*$ acts on $H_n(S^n; \mathbb{Z}) = \mathbb{Z}$ as multiplication by $\deg(f)$. So $h_n([f]) = \deg(f) \cdot [S^n]$, and under the identification $H_n(S^n) = \mathbb{Z}$, the integer attached to $[f]$ is exactly $\deg(f)$.

> [!note]- Derivation
> Brouwer degree is defined as the integer $\deg(f)$ such that $f_* : H_n(S^n; \mathbb{Z}) \to H_n(S^n; \mathbb{Z})$ is multiplication by $\deg(f)$ — equivalently, $f_*([S^n]) = \deg(f) \cdot [S^n]$.
>
> Apply this to $h_n([f]) = f_*([S^n]) = \deg(f) \cdot [S^n]$. Under the identification $H_n(S^n; \mathbb{Z}) \to \mathbb{Z}$ (sending $[S^n]$ to $1$), this becomes $h_n([f]) = \deg(f)$.
>
> So the isomorphism $\pi_n(S^n) \to H_n(S^n; \mathbb{Z}) \to \mathbb{Z}$ sends $[f]$ to $\deg(f)$. Every integer arises as the degree of *some* map: for $\deg = k$, take the standard "wrap-$k$-times" map $S^n \to S^n$ given in coordinates by $(z, t) \mapsto (z^k, t)$ in the suspension picture (or directly $z \mapsto z^k$ for $S^1$).

> [!note]- Complete formal solution
> Let $n \geq 1$. We show $\pi_n(S^n) = \mathbb{Z}$ with generator $[\mathrm{id}_{S^n}]$, and the integer attached to $[f]$ is the Brouwer degree $\deg(f)$.
>
> **Connectivity.** For $1 \leq k < n$, every continuous map $f : S^k \to S^n$ is null-homotopic. Indeed, $f$ is homotopic to a smooth map (smoothing approximation); by Sard's theorem, the image of a smooth map of a $k$-manifold into an $n$-manifold ($k < n$) has measure zero, so there is a point $p \in S^n$ outside the image. Then $f$ factors through $S^n \setminus \{p\} \cong \mathbb{R}^n$, which is contractible, so $f$ is null-homotopic. Hence $\pi_k(S^n) = 0$ for $0 \leq k \leq n-1$, i.e., $S^n$ is $(n-1)$-connected.
>
> **Hurewicz.** By the Hurewicz theorem, the map $h_n : \pi_n(S^n) \to H_n(S^n; \mathbb{Z})$ is an isomorphism. The right-hand side is $\mathbb{Z}$, by the cellular homology computation (one 0-cell, one $n$-cell, with attaching boundary zero).
>
> Hence $\pi_n(S^n) \cong \mathbb{Z}$, with the generator being a class mapping to the fundamental class $[S^n]$. Since $h_n([\mathrm{id}_{S^n}]) = (\mathrm{id}_{S^n})_*([S^n]) = [S^n]$, the identity map represents the generator.
>
> **Identification with degree.** The Hurewicz map satisfies $h_n([f]) = f_*([S^n])$. The Brouwer degree is *defined* by $f_*([S^n]) = \deg(f) \cdot [S^n]$. So under the identification $H_n(S^n; \mathbb{Z}) = \mathbb{Z}$, $h_n([f]) = \deg(f)$.
>
> Therefore $\pi_n(S^n) = \mathbb{Z}$, and the isomorphism with $\mathbb{Z}$ is by Brouwer degree. $\blacksquare$

---

# Key Takeaways

**Hurewicz is the gateway from homotopy to homology for spheres and connected spaces.** The conceptual lesson is that whenever you face a question about $\pi_k(X)$ for a space with sufficient connectivity, the first move should be to check whether Hurewicz applies. If $X$ is $(k-1)$-connected, the question reduces to computing $H_k(X; \mathbb{Z})$, which is approachable by standard homological methods (CW chain complex, Mayer–Vietoris, long exact sequence of a pair). For higher $k$ beyond the first nonzero degree, the Hurewicz map is in general neither injective nor surjective, and additional machinery (Serre spectral sequence, Postnikov towers) is needed. The trigger condition for Hurewicz is "the first nonzero $\pi_k$ of a sufficiently connected space" — recognise this and the computation is essentially mechanical.

**Degree is the integer-valued invariant of maps between equal-dimensional spheres.** The Brouwer degree generalises far beyond $\pi_n(S^n)$ — it gives the unifying integer invariant for any orientation-preserving map between closed oriented $n$-manifolds. For Riemann surfaces, degree of holomorphic maps; for Lie groups, winding numbers of group homomorphisms; for vector fields, the index of zeros (Poincaré–Hopf); for instantons, the topological charge. All these are degrees, all integer-valued, all computed by the same fundamental formula "signed count of preimages of a regular value". The lesson: whenever you encounter an integer in topology, ask "what map's degree am I computing?" — almost always, the answer reveals the structural reason for the integrality.

**The connectivity hierarchy of spheres: $\pi_k(S^n) = 0$ for $k < n$, then explodes for $k > n$.** The connectivity result $\pi_k(S^n) = 0$ for $k < n$ is structurally important: it says low-dimensional probes cannot detect high-dimensional spheres, and the Sard-theorem proof is generic — it works for any $(n-1)$-connected manifold, not just spheres. But for $k > n$, the situation is drastically different: $\pi_3(S^2) = \mathbb{Z}$ (Hopf!), $\pi_4(S^3) = \mathbb{Z}/2$, $\pi_5(S^4) = \mathbb{Z}/2$, and the pattern continues with mostly torsion and a few $\mathbb{Z}$s appearing in specific stable degrees (Bott periodicity in the stable range). The lesson: the "easy" range of $\pi_k(S^n)$ is $k \leq n$ (Hurewicz applies, gives $\mathbb{Z}$ at $k = n$); the "hard" range $k > n$ is where stable homotopy theory lives, and computations there are major mathematical accomplishments.
