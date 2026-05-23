---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Higher Homotopy Group"
  - "Def - Singular Homology"
  - "Def - Fundamental Group"
tags: [geometry, algebraic-topology, homotopy, homology]
---

# Notation

$X$ is a topological space, $x_0 \in X$ a base point. $\pi_k(X, x_0)$ is the [[Def - Higher Homotopy Group|$k$-th homotopy group]]. $H_k(X; \mathbb{Z})$ is the [[Algebraic Topology I — Singular Homology and the de Rham Theorem|singular homology]] with integer coefficients. $[S^k] \in H_k(S^k; \mathbb{Z}) = \mathbb{Z}$ is the **fundamental class** of the oriented $k$-sphere — the generator. For $f : S^k \to X$, $f_*([S^k]) \in H_k(X; \mathbb{Z})$ is the pushforward of the fundamental class. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

The motivating question is: *what is the comparison between homotopy (which is hard) and homology (which is computable)?* Both $\pi_k(X)$ and $H_k(X; \mathbb{Z})$ measure "$k$-dimensional features" of $X$. Homotopy uses spheres as probes — a class in $\pi_k$ is a homotopy class of maps $S^k \to X$. Homology uses *cycles* — a class in $H_k$ is a singular cycle (a $\mathbb{Z}$-linear combination of $k$-simplices with vanishing boundary) modulo boundaries.

Both are functorial: a map $f : X \to Y$ induces homomorphisms $f_* : \pi_k(X) \to \pi_k(Y)$ and $f_* : H_k(X) \to H_k(Y)$. Both vanish for contractible spaces. So they share many formal properties, but they are *not* equal in general. The Hurewicz map is the comparison.

The construction is direct: a map $f : S^k \to X$ representing a class in $\pi_k(X)$ pushes the fundamental class $[S^k] \in H_k(S^k)$ forward to a class $f_*([S^k]) \in H_k(X)$. Two homotopic maps push the fundamental class to homologous cycles (because the homotopy provides a $(k+1)$-chain bounding their difference). So the assignment $[f] \mapsto f_*([S^k])$ descends to a well-defined map $h_k : \pi_k(X) \to H_k(X; \mathbb{Z})$ on homotopy classes.

Why is this the right comparison? Because:

1. **It is the only natural homomorphism between $\pi_k$ and $H_k$ in any reasonable sense.** Every alternative ends up agreeing with this one.

2. **For $k = 1$, it identifies $H_1$ with the abelianisation of $\pi_1$**: $\pi_1^{\mathrm{ab}}(X) \cong H_1(X; \mathbb{Z})$. The kernel of $h_1$ is exactly the commutator subgroup. This is the classical theorem of **Poincaré–Hurewicz** at degree 1.

3. **For higher $k$, it is an isomorphism in the first nonzero degree** for sufficiently connected spaces (the [[Thm - Hurewicz Theorem (Statement)|Hurewicz theorem]]). This is the central computational tool of homotopy theory.

The deep content is the **gap** between $\pi_k$ and $H_k$ in higher degrees. For instance, the Hurewicz map $h_3 : \pi_3(S^2) \to H_3(S^2)$ sends the Hopf class to zero (since $H_3(S^2) = 0$), so the Hopf invariant is *not* visible to ordinary homology. It is visible to cup products in cohomology — the **Hopf invariant** is the cup product $\alpha \cup \alpha$ in $H^*(S^2; \mathbb{Z})$ where $\alpha$ is a 2-class representing the Hopf map — but not to homology per se. The discrepancy is the source of much of higher homotopy theory.

The kernel and cokernel of the Hurewicz map record higher-order homotopy information not captured by homology. In the Postnikov-tower picture, these are the **Postnikov $k$-invariants** that glue together Eilenberg–MacLane stages.

---

# The Definition

Let $(X, x_0)$ be a pointed topological space and $k \geq 1$. The **Hurewicz map** is

$$h_k : \pi_k(X, x_0) \to H_k(X; \mathbb{Z})$$

defined by

$$h_k([f]) = f_*([S^k]),$$

where $f : S^k \to X$ is any based representative of the homotopy class, $[S^k] \in H_k(S^k; \mathbb{Z}) = \mathbb{Z}$ is the fundamental class of the oriented $k$-sphere, and $f_*$ is the induced map in singular homology.

**Properties:**

1. $h_k$ is a well-defined group homomorphism (the assignment factors through homotopy classes).
2. $h_k$ is **natural**: for any continuous based map $\varphi : (X, x_0) \to (Y, y_0)$, the diagram
$$
\begin{array}{ccc}
\pi_k(X, x_0) & \xrightarrow{\varphi_*} & \pi_k(Y, y_0) \\
\downarrow h_k & & \downarrow h_k \\
H_k(X; \mathbb{Z}) & \xrightarrow{\varphi_*} & H_k(Y; \mathbb{Z})
\end{array}
$$
commutes.

3. For $k = 1$, $h_1$ factors through the abelianisation:
$$h_1 : \pi_1(X, x_0) \twoheadrightarrow \pi_1(X, x_0)^{\mathrm{ab}} \cong H_1(X; \mathbb{Z}),$$
and this last isomorphism is the **Hurewicz isomorphism at degree 1**, valid for any path-connected $X$ without further hypothesis (the classical Hurewicz–Poincaré theorem).

4. For $k \geq 2$, $h_k$ is automatically a homomorphism into an abelian group (since $\pi_k$ is already abelian by Eckmann–Hilton).

5. **Hurewicz theorem (statement, see [[Thm - Hurewicz Theorem (Statement)]]):** if $X$ is path-connected and $(n-1)$-connected (i.e., $\pi_k(X) = 0$ for $0 \leq k \leq n-1$) with $n \geq 2$, then $h_n : \pi_n(X) \to H_n(X; \mathbb{Z})$ is an isomorphism, and $h_{n+1}$ is surjective.

---

# Categorical / Structural Definition

The Hurewicz map is a **natural transformation** between two functors $\mathrm{hTop}_* \to \mathrm{Ab}$:

- $\pi_k : \mathrm{hTop}_* \to \mathrm{Ab}$ (for $k \geq 2$; for $k = 1$ the target is $\mathrm{Grp}$).
- $H_k(\cdot; \mathbb{Z}) : \mathrm{hTop}_* \to \mathrm{Ab}$.

Naturality is the commutative square above. The natural transformation $h_k$ is the unique one (up to scaling) that sends the identity class of $\pi_k(S^k) = \mathbb{Z}$ to the fundamental class of $H_k(S^k) = \mathbb{Z}$.

In modern homotopy theory, the Hurewicz map is the bottom row of a much richer apparatus: the **Hurewicz spectral sequence** and the **Eilenberg–MacLane spectral sequence**, which compute the difference between homotopy and homology systematically in terms of Postnikov invariants and $k$-invariants.

A more refined picture uses **stable homotopy**: the stable Hurewicz map $h_k^s : \pi_k^s(X) \to H_k(X; \mathbb{Z})$ from stable homotopy to ordinary homology has interpretation via the **Spanier–Whitehead duality** and the natural transformation **stable homotopy** $\to$ **homology**, which is one of the basic comparisons in stable homotopy theory.

In **Eilenberg–MacLane spaces**, the Hurewicz map at the fundamental degree is an isomorphism by definition: $\pi_n(K(\pi, n)) = \pi$ and $H_n(K(\pi, n); \mathbb{Z}) = \pi$ (for abelian $\pi$), and the Hurewicz map is the identity. This is what makes Eilenberg–MacLane spaces the natural building blocks of homotopy theory.

---

# Relate to Other Fields / Compression

**True name:** the Hurewicz map is **the comparison between two notions of "$k$-dimensional features" of a space — those detectable by spheres and those detectable by chains**. The operational picture is: take a sphere mapped into $X$, declare its image to be a cycle by pushing forward the fundamental class, and read off the homology class. The map captures the part of homotopy that is visible to homology; the kernel and cokernel record the discrepancy.

In **homological algebra**, the Hurewicz map plays an analogous role to the **abelianisation** of a group: the natural transformation from a non-abelian to abelian invariant, with isomorphism at the first level. Both forget non-commutative or higher information to extract a computable abelian shadow.

In **rational homotopy theory** (Sullivan, Quillen), the Hurewicz map is rationalised: $h \otimes \mathbb{Q} : \pi_*(X) \otimes \mathbb{Q} \to H_*(X; \mathbb{Q})$. For simply connected $X$, the rational homotopy groups $\pi_k(X) \otimes \mathbb{Q}$ are encoded in a *differential graded algebra* (the **Sullivan model**), and the Hurewicz map becomes the differential in a Koszul-dual sense. This is the basis of formal computations of $\pi_*(X) \otimes \mathbb{Q}$ for simple spaces.

In **stable homotopy theory**, the stable Hurewicz map $\pi_*^s(X) \to H_*(X)$ is part of a *transformation of cohomology theories* — stable homotopy (which is a generalised cohomology) to ordinary homology. The fibre is the **stable homotopy of the basepoint**, $\pi_*^s = \pi_*^s(\mathrm{pt})$ — the stable stems, the central computational object of stable homotopy.

In **algebraic geometry**, the algebraic analogue of the Hurewicz map relates algebraic K-theory $K_*$ to motivic cohomology $H^{*, *}_{\mathrm{mot}}$ via the **motivic Hurewicz map** — the bridge from non-commutative K-theory to commutative motivic cohomology.

---

# Examples / Corollaries

**Example: $\pi_1$ of a wedge of circles.** $\pi_1(S^1 \vee S^1) = F_2$, the free group on two generators (highly non-abelian). $H_1(S^1 \vee S^1; \mathbb{Z}) = \mathbb{Z}^2 = F_2^{\mathrm{ab}}$. The Hurewicz map $h_1$ is the quotient by the commutator subgroup, sending each generator of $F_2$ to a standard basis vector of $\mathbb{Z}^2$. The kernel is the commutator subgroup, which is free of infinite rank.

**Example: $\pi_2(S^2)$ to $H_2(S^2)$.** Both are $\mathbb{Z}$, and $h_2$ is an isomorphism (Hurewicz). The generator of $\pi_2(S^2)$ is the identity map $S^2 \to S^2$; its image under $h_2$ is the fundamental class $[S^2] \in H_2(S^2) = \mathbb{Z}$. This identifies the integer parameter on $\pi_2(S^2)$ with the Brouwer degree of the map.

**Example: $\pi_3(S^2)$ to $H_3(S^2)$.** $\pi_3(S^2) = \mathbb{Z}$ (generated by the Hopf map), but $H_3(S^2) = 0$. So the Hurewicz map $h_3 : \mathbb{Z} \to 0$ is *zero* — the Hopf class is *not detected* by integer homology. This is the classical demonstration that higher Hurewicz is in general neither injective nor surjective.

**Example: $\pi_k(S^n)$ for $k = n$.** $\pi_n(S^n) = \mathbb{Z}$ (Brouwer degree), $H_n(S^n) = \mathbb{Z}$, $h_n$ is an isomorphism. Identifies degree with the integer in $H_n$.

**Example: $\pi_k(\mathbb{RP}^n)$ for $n \geq 2$.** $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$, $H_1(\mathbb{RP}^n; \mathbb{Z}) = \mathbb{Z}/2$, $h_1$ is the (in this case trivial) abelianisation isomorphism.

**Example: $\pi_2(T^2)$.** $\pi_1(T^2) = \mathbb{Z}^2$, $\pi_2(T^2) = 0$ (torus is aspherical, $K(\mathbb{Z}^2, 1)$). The Hurewicz map $h_2 : 0 \to H_2(T^2) = \mathbb{Z}$ is trivially the zero map, but $H_2(T^2)$ is non-zero — the discrepancy reflects that the 2-cycle of the torus (the fundamental class) cannot be represented by a single sphere-image, but only by a torus-image.

**Example: a $K(\pi, n)$ space.** For $K(\pi, n)$ with $\pi$ abelian and $n \geq 1$:

$$\pi_k(K(\pi, n)) = \begin{cases} \pi & k = n \\ 0 & k \neq n \end{cases}, \qquad H_k(K(\pi, n); \mathbb{Z}) = ?$$

By Hurewicz, $H_k = 0$ for $0 < k < n$ and $H_n = \pi$. Higher $H_k$ (for $k > n$) are usually non-zero and computable in principle; e.g., $H^*(K(\mathbb{Z}, 2); \mathbb{Z}) = H^*(\mathbb{CP}^\infty; \mathbb{Z}) = \mathbb{Z}[h]$, polynomial in the generator $h \in H^2$. The Hurewicz map is an isomorphism at degree $n$, in agreement with the general theorem.

**Is NOT an instance: a map from $H_k$ to $\pi_k$.** There is no natural map in the opposite direction (homology to homotopy) — homotopy is *not* the abelianisation of homology, nor any other standard functor. The map is genuinely one-directional. This is why "compute $\pi_k$ via $H_k$" via the Hurewicz theorem is the most we can do.

**Corollary: connectivity implications.** If $h_k = 0$ for some $k \leq n$ on a simply-connected space, then $H_k(X; \mathbb{Z}) = 0$ for that $k$ (by Hurewicz reasoning). This often constrains the homotopy type.

**Corollary: Whitehead's theorem.** A based map $f : X \to Y$ between simply-connected CW complexes is a homotopy equivalence iff it induces isomorphisms $H_n(X; \mathbb{Z}) \to H_n(Y; \mathbb{Z})$ for all $n$. This uses Hurewicz inductively: an isomorphism in homology forces (via Hurewicz) an isomorphism in homotopy in the first nonzero degree, then connectivity bootstraps the inductive step.

**Calibration check.** If you understand the definition you should be able to: (i) verify that $h_k$ is well-defined on homotopy classes; (ii) explain why $h_3 : \pi_3(S^2) \to H_3(S^2)$ is zero; (iii) verify the abelianisation property of $h_1$; (iv) compute $h_n(\mathrm{id}_{S^n}) = [S^n] \in H_n(S^n; \mathbb{Z})$.

---

# Unlocked by This

> [!tip] Postnikov Tower *(from Homotopy Theory)*
> Every connected space has a **Postnikov tower** $\cdots \to X[n+1] \to X[n] \to \cdots \to X[1] \to X[0] = \mathrm{pt}$, where $X[n]$ has homotopy concentrated in degrees $\leq n$. The fibre of $X[n+1] \to X[n]$ is the Eilenberg–MacLane space $K(\pi_{n+1}, n+1)$, and the data gluing the layers is the **Postnikov $k$-invariant** $k_n \in H^{n+2}(X[n]; \pi_{n+1})$. The Hurewicz map at each layer is an isomorphism (because each layer has homotopy concentrated in a single degree), and the Postnikov $k$-invariants measure precisely the failure of Hurewicz at higher degrees.

> [!tip] Sullivan Models and Rational Homotopy *(from Rational Homotopy Theory)*
> For a simply connected space $X$ with finite-type rational cohomology, there is a **Sullivan minimal model** — a differential graded commutative algebra $(A_X, d)$ over $\mathbb{Q}$ whose cohomology is $H^*(X; \mathbb{Q})$ and whose generators correspond to $\pi_*(X) \otimes \mathbb{Q}$. The Hurewicz map is the *inclusion of generators*, and rational homotopy is computable from the algebra structure of $H^*(X; \mathbb{Q})$ and the higher Massey products. This makes rational homotopy a fully algorithmic invariant — unlike integer homotopy, which is hopelessly complicated.

> [!tip] Generalized Hurewicz Map *(from Stable Homotopy Theory)*
> For any generalised cohomology theory $E^*$, there is a natural transformation from stable homotopy $\pi_*^s$ to $E^*$, the **Hurewicz map for $E$**. For $E =$ ordinary cohomology this is the classical Hurewicz; for $E =$ K-theory it is the comparison from stable homotopy to K-theory; for $E =$ cobordism it is the Thom-spectrum map. These maps and their kernels/cokernels (the **first differentials of the Adams spectral sequence**) are the computational tools that pin down stable homotopy.
