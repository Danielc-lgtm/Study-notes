---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - de Rham Cohomology"
  - "Thm - The Mayer-Vietoris Sequence"
  - "Thm - The Poincaré Lemma on a Star-Shaped Region"
tags: [geometry, differential-geometry, cohomology, mayer-vietoris]
---

# Problem Statement

Use the Mayer–Vietoris sequence to compute $H^k_{dR}(S^1)$ for all $k \geq 0$. Identify an explicit generator of $H^1_{dR}(S^1)$.

**Recall:**

![[Thm - The Mayer-Vietoris Sequence#Statement]]

![[Thm - The Poincaré Lemma on a Star-Shaped Region#Statement]]

The angular $1$-form on $\mathbb{R}^2 \setminus \{0\}$: $d\theta = (-y\,dx + x\,dy)/(x^2 + y^2)$, the differential of the multivalued angle function. It is closed everywhere on $\mathbb{R}^2 \setminus \{0\}$ but not exact (its integral around any loop encircling the origin is $2\pi$, not zero).

---

# Convergent Strategy

**Problem class:** A direct Mayer–Vietoris computation on a small manifold — the simplest non-trivial application of the cover-and-glue strategy. Pattern: cover $S^1$ by two pieces each [[Def - Homotopy|homotopy]]-equivalent to a contractible space, write down the long exact sequence, and read off the unknown cohomology from exactness.

**Assumption pattern:** $S^1$ is a compact connected $1$-manifold. The natural cover is by two open arcs, each contractible ([[Def - Homotopy|homotopy]] equivalent to a point). The intersection is two disjoint contractible arcs (homotopy equivalent to two points). The cohomology of contractible pieces is trivial in positive degrees; the long exact sequence reduces to a single non-trivial step.

**Theorem routing:** [[Thm - The Poincaré Lemma on a Star-Shaped Region]] (or homotopy invariance from a more general statement) gives $H^*$ of each contractible piece. [[Thm - The Mayer-Vietoris Sequence]] then connects everything. The resulting exact sequence has only one "interesting" term, and exactness determines $H^1(S^1)$.

**Key decision point:** The choice to cover $S^1$ by two *open* arcs (rather than one arc plus a "cap" or some other decomposition) is critical — Mayer–Vietoris requires *open* sets. The standard choice is $U = S^1 \setminus \{N\}$ and $V = S^1 \setminus \{S\}$, where $N$ and $S$ are antipodal points; both are diffeomorphic to $\mathbb{R}$ via stereographic projection from the omitted point.

---

# Legal Operations Used

1. **Cut into pieces and assemble via Mayer–Vietoris** (operation 8 from the topic page). The cover of $S^1$ by two open arcs gives the input to Mayer–Vietoris.

2. **Use homotopy invariance to replace $M$ with a homotopy-equivalent simpler space** (operation 7 from the topic page). $U$ and $V$ are contractible (homotopy equivalent to a point), so $H^*(U) = H^*(V) = (\mathbb{R}, 0, 0, \dots)$. The intersection $U \cap V$ is homotopy equivalent to two disjoint points, so $H^0(U \cap V) = \mathbb{R}^2$ and higher cohomology zero.

3. **Detect a non-trivial cohomology class by integration over a cycle** (operation 3 from the topic page). The closed form $d\theta$ on $S^1$ has $\int_{S^1} d\theta = 2\pi \neq 0$, so $[d\theta] \neq 0$ in $H^1(S^1)$.

---

# Hints

> [!note]- Hint 1
> Cover $S^1$ by two open arcs that overlap in a small region. What is the topology of each arc? Of their intersection?

> [!note]- Hint 2
> Each arc is contractible (homotopy equivalent to a point), so its $H^*$ is concentrated in degree 0. The intersection has two connected components, so $H^0$ is $\mathbb{R}^2$.

> [!note]- Hint 3
> Write down the Mayer–Vietoris sequence. In low degrees: $0 \to H^0(S^1) \to H^0(U) \oplus H^0(V) \to H^0(U \cap V) \to H^1(S^1) \to 0$.

> [!note]- Hint 4
> The map $H^0(U) \oplus H^0(V) \to H^0(U \cap V)$ sends $(a, b)$ (constants on $U$ and $V$) to the restrictions on each of the two intersection components, then takes the difference: $(a, b) \mapsto (a - b, a - b)$. What is its image and kernel?

> [!note]- Hint 5
> By exactness, $\dim H^1(S^1) = \dim H^0(U \cap V) - \dim(\text{image of restriction map})$. Compute and conclude.

---

# Solution

The plan: cover $S^1$ by two open arcs, identify each as contractible, identify their two-component intersection, and run Mayer–Vietoris. The long exact sequence has only one non-trivial degree, and rank-counting gives $\dim H^1 = 1$. Then we identify $[d\theta]$ as an explicit generator.

**Step 1: Set up the cover.**

> [!note]- Derivation
> Let $N, S \in S^1$ be antipodal points. Define $U = S^1 \setminus \{N\}$ and $V = S^1 \setminus \{S\}$. Each is open in $S^1$ and the union is $U \cup V = S^1 \setminus (\{N\} \cap \{S\}) = S^1$ (since $N \neq S$). The intersection $U \cap V = S^1 \setminus \{N, S\}$ is the disjoint union of two open arcs.
>
> Stereographic projection from $N$ gives a [[Def - Diffeomorphism|diffeomorphism]] $U \cong \mathbb{R}$, similarly from $S$ for $V$. Each $U$, $V$ is diffeomorphic to $\mathbb{R}$, hence contractible. $U \cap V$ is the disjoint union of two arcs (each homeomorphic to $\mathbb{R}$, hence contractible), so it is homotopy equivalent to two disjoint points.

**Step 2: Compute cohomologies of the pieces.**

> [!note]- Derivation
> By [[Thm - The Poincaré Lemma on a Star-Shaped Region]] (or homotopy invariance from $U \simeq$ point, $V \simeq$ point):
> $$H^0(U) = H^0(V) = \mathbb{R}, \qquad H^k(U) = H^k(V) = 0 \text{ for } k \geq 1.$$
>
> For $U \cap V$ (two contractible components):
> $$H^0(U \cap V) = \mathbb{R}^2, \qquad H^k(U \cap V) = 0 \text{ for } k \geq 1.$$

**Step 3: Apply Mayer–Vietoris.**

> [!note]- Derivation
> The Mayer–Vietoris sequence:
> $$0 \to H^0(S^1) \xrightarrow{(k^*, l^*)} H^0(U) \oplus H^0(V) \xrightarrow{i^* - j^*} H^0(U \cap V) \xrightarrow{\delta} H^1(S^1) \to H^1(U) \oplus H^1(V) \to \cdots$$
>
> Substituting:
> $$0 \to H^0(S^1) \xrightarrow{(k^*, l^*)} \mathbb{R} \oplus \mathbb{R} \xrightarrow{i^* - j^*} \mathbb{R}^2 \xrightarrow{\delta} H^1(S^1) \to 0 \to 0.$$
>
> The map $i^* - j^* : \mathbb{R} \oplus \mathbb{R} \to \mathbb{R}^2$ sends $(f_U, f_V)$ (constants on $U$, $V$) to the differences on the two components of $U \cap V$. Call the two arcs $A_1$ and $A_2$. On $A_1$: $f_U - f_V = a - b$. On $A_2$: $f_U - f_V = a - b$ (the same value, since both $f_U$ and $f_V$ are constants on their respective contractible domains). So $(a, b) \mapsto (a - b, a - b) \in \mathbb{R}^2$, image is the diagonal.
>
> So $\dim \mathrm{image}(i^* - j^*) = 1$, $\dim \ker(i^* - j^*) = 2 - 1 = 1$.
>
> By exactness at $\mathbb{R}^2 = H^0(U \cap V)$: $\dim H^1(S^1) = \dim H^0(U \cap V) - \dim \mathrm{image}(i^* - j^*) = 2 - 1 = 1$.
>
> By exactness at $H^0(S^1)$ (injection into $\mathbb{R}^2$): $H^0(S^1) \hookrightarrow \mathbb{R}^2$ as the diagonal kernel of $i^* - j^*$ — so $H^0(S^1) = \mathbb{R}$. (Consistent with $S^1$ being connected.)
>
> For $k \geq 2$: $H^k(U \cap V) = 0$ (vanishing) and $H^k(U) \oplus H^k(V) = 0$ as well, so $H^k(S^1)$ is sandwiched between two zeros — must be zero.

**Step 4: Explicit generator $[d\theta]$.**

> [!note]- Derivation
> The closed $1$-form $d\theta$ on $S^1$ — locally $d\theta$ in the standard angular coordinate, globally the restriction of $(-y\,dx + x\,dy)/(x^2 + y^2)$ from $\mathbb{R}^2 \setminus \{0\}$ to $S^1$ — is closed: $d(d\theta) = 0$ trivially (in dimension 1, every $1$-form is closed since there are no $2$-forms).
>
> To see $[d\theta] \neq 0$: compute $\int_{S^1} d\theta = 2\pi$. If $d\theta$ were exact, say $d\theta = df$ for some smooth $f$ on $S^1$, Stokes's theorem would give $\int_{S^1} df = \int_{\partial S^1} f = 0$ (since $\partial S^1 = \emptyset$). But $2\pi \neq 0$, contradiction. So $[d\theta]$ is non-trivial.
>
> Since $\dim H^1(S^1) = 1$, $[d\theta]$ is a basis.

> [!note]- Complete formal solution
> Cover $S^1$ by two open arcs $U = S^1 \setminus \{N\}$ and $V = S^1 \setminus \{S\}$, where $N$ and $S$ are antipodal. Each arc is contractible (diffeomorphic to $\mathbb{R}$ via stereographic projection from the omitted point), so $H^*(U) = H^*(V) = (\mathbb{R}, 0, 0, \dots)$. The intersection $U \cap V = S^1 \setminus \{N, S\}$ is two disjoint contractible arcs, so $H^*(U \cap V) = (\mathbb{R}^2, 0, 0, \dots)$.
>
> The Mayer–Vietoris sequence reduces to
> $$0 \to H^0(S^1) \to \mathbb{R}^2 \xrightarrow{i^* - j^*} \mathbb{R}^2 \to H^1(S^1) \to 0$$
> with $H^k(S^1) = 0$ for $k \geq 2$ (sandwiched between zeros). The map $i^* - j^* : (a, b) \mapsto (a - b, a - b)$ has $1$-dimensional image (the diagonal) and $1$-dimensional kernel. By exactness:
> - $H^0(S^1) = \ker(i^* - j^*) \cong \mathbb{R}$, consistent with $S^1$ connected.
> - $H^1(S^1) = \mathbb{R}^2 / \mathrm{image} \cong \mathbb{R}$, $1$-dimensional.
>
> The class $[d\theta]$ generates $H^1(S^1)$: $d\theta$ is closed (every $1$-form on a $1$-manifold is closed), and $\int_{S^1} d\theta = 2\pi \neq 0$ certifies non-exactness (an exact form would integrate to zero by Stokes). So $[d\theta]$ is a non-zero class in a $1$-dimensional space, hence a basis.
>
> Summary:
> $$H^k_{dR}(S^1) = \begin{cases} \mathbb{R} & k = 0, 1 \\ 0 & k \geq 2 \end{cases}$$
> with basis $\{1\}$ in degree 0 and $\{[d\theta]\}$ in degree 1. $\blacksquare$

> [!warning] Illegal but tempting alternative route — using only the angular form $d\theta$
> One might be tempted to "compute" $H^1(S^1)$ by simply exhibiting $[d\theta]$ as a non-trivial element and claiming it generates. But this only shows $\dim H^1(S^1) \geq 1$; it does not by itself show $\dim H^1(S^1) = 1$. To get the upper bound, you need an actual cohomology computation — and Mayer–Vietoris is the standard tool. The "only one generator" requires a structural argument, not just an example. This is a common pitfall in first-time cohomology computations: confusing "I have a non-trivial element" with "I have the whole answer."

---

# Key Takeaways

**Mayer–Vietoris with a two-arc cover is the universal computation for $S^1$, and similar covers extend to higher spheres.** The strategy "cover by two contractible pieces with computable intersection" works for $S^n$ via the two-hemisphere cover, with intersection homotopy equivalent to $S^{n-1}$. This leads to an inductive computation $H^*(S^n) \cong H^{*-1}(S^{n-1})$ in positive degrees (shifted by the connecting map $\delta$), giving $H^k(S^n) = \mathbb{R}$ for $k = 0, n$ and zero otherwise. The trigger to recognize: any compact connected manifold with a known "two-piece" decomposition should be tackled by Mayer–Vietoris first.

**The angular form $d\theta$ is the prototype non-exact closed form, and its non-triviality is detected by integration.** It is the simplest example of a cohomology class that is forced into existence by topology — the loop $S^1$ has a non-trivial $H^1$ because it has a non-trivial $\pi_1 = \mathbb{Z}$, and integration of $d\theta$ around $S^1$ recovers the winding number. This is the de Rham–singular-cohomology pairing in action, with $[\gamma] \in H_1(S^1) = \mathbb{Z}$ pairing with $[d\theta] \in H^1(S^1) = \mathbb{R}$ via $\gamma \mapsto \int_\gamma d\theta = 2\pi \cdot \mathrm{wn}(\gamma)$. The trigger: any time you suspect a closed form is non-exact, integrate it over the suspected non-trivial cycle and observe a non-zero result.

**The connecting map $\delta$ in Mayer–Vietoris shifts degree and tracks "how much the local primitives fail to glue."** In this exercise, the non-trivial $H^1(S^1)$ arises because $H^0(U \cap V)$ has $2$ [[Def - Dimension|dimensions]] while the restrictions from $H^0(U) \oplus H^0(V)$ span only a $1$-dimensional [[Def - Subspace|subspace]] — the "missing" $1$-dimensional cokernel becomes $H^1(S^1)$ via the connecting map. This is the geometric meaning of $\delta$: it measures the topological obstruction to extending local primitives globally. The trigger: in every Mayer–Vietoris computation, the connecting map $\delta$ is where the new cohomology comes from; learn to identify its [[Def - Dimension|dimensions]] by exactness rather than computing it explicitly.

**The dimension count $\dim H^1(S^1) = \dim H^0(U \cap V) - \dim \mathrm{image}(i^* - j^*)$ is a special case of a general principle.** When two of three of $\dim H^p(U)$, $\dim H^p(V)$, $\dim H^p(U \cap V)$, $\dim H^p(M)$ are known at a particular degree, the long exact sequence determines the fourth by rank-counting. This is the *computational engine* of Mayer–Vietoris, and learning to do these rank counts efficiently is the practical skill. *Companion exercise:* [[Ex - The de Rham Cohomology of the Torus]] uses this in a more complex setting via Künneth.
