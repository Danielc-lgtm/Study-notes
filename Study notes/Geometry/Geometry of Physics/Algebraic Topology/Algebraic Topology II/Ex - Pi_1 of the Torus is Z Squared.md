---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Thm - Pi_1 of S^1 is Z"
  - "Def - Covering Space"
  - "Def - Path-Product and the Fundamental Group"
tags: [geometry, algebraic-topology, topology]
---

# Problem Statement

Compute $\pi_1(T^2, *)$ where $T^2 = S^1 \times S^1$ is the 2-torus and $* = (1, 1)$ is the base point. Show that $\pi_1(T^2) \cong \mathbb{Z}^2$, with generators the two coordinate loops $a(\theta) = (e^{2\pi i\theta}, 1)$ and $b(\theta) = (1, e^{2\pi i\theta})$, and that the two generators *commute* — i.e., $\pi_1(T^2)$ is abelian.

Then generalise: $\pi_1(T^n) = \mathbb{Z}^n$ for the $n$-torus $T^n = (S^1)^n$.

**Recall:**

The fundamental group is defined in:

![[Def - Path-Product and the Fundamental Group#The Definition]]

The covering map structure of $T^2$ comes from:

![[Def - Covering Space#The Definition]]

The flagship computation we will lean on:

![[Thm - Pi_1 of S^1 is Z#Statement]]

---

# Convergent Strategy

**Problem class:** Computation of $\pi_1$ for a *product space*. The general principle is the **product formula** $\pi_1(X \times Y) = \pi_1(X) \times \pi_1(Y)$, a foundational result that we will derive concretely for $T^2$ (and the product structure makes the result automatically abelian). Two routes are available: (a) directly via the product formula plus $\pi_1(S^1) = \mathbb{Z}$; (b) via the universal cover $\mathbb{R}^2 \to T^2$ with deck group $\mathbb{Z}^2$ acting by translations. We will combine both: route (a) for the computation, route (b) to justify the commutativity geometrically.

**Assumption pattern:** $T^2$ is a product $S^1 \times S^1$, so its $\pi_1$ should decompose as a product of $\pi_1$'s. We have $\pi_1(S^1) = \mathbb{Z}$ from the previous flagship theorem. The base point is on both factors. The product structure of the space is the key assumption that unlocks the product structure of the group.

**Theorem routing:** [[Thm - Pi_1 of S^1 is Z|\pi₁(S^1) = ℤ]] gives the factor. The product formula $\pi_1(X \times Y) = \pi_1(X) \times \pi_1(Y)$ (proved via the projection homomorphisms $\pi_1(X \times Y) \to \pi_1(X) \times \pi_1(Y)$ and its inverse) gives $\pi_1(T^2) = \mathbb{Z} \times \mathbb{Z} = \mathbb{Z}^2$. The universal cover argument from [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]] gives the same answer geometrically: $\widetilde{T^2} = \mathbb{R}^2$ with deck group $\mathbb{Z}^2$.

**Key decision point:** Whether to prove the product formula in generality or to compute $\pi_1(T^2)$ directly using lifts to $\mathbb{R}^2$. The product-formula route is the cleanest for the algebra; the universal-cover route is more memorable. We do both: product formula as the proof, universal cover as the conceptual picture. The non-obvious aspect of either route is the commutativity — geometrically clear from $\mathbb{Z}^2$ being abelian, algebraically forced by the product structure.

---

# Legal Operations Used

1. **Operation 6 from the topic page (pass to the universal cover).** We pass to the universal cover $\mathbb{R}^2 \to T^2$, which exists and is simply connected. The deck group is $\mathbb{Z}^2$ acting by integer translations, and this gives $\pi_1(T^2) = \mathbb{Z}^2$ directly. This is the geometric route to the answer.

2. **Operation 4 from the topic page (identify the fundamental group of a quotient via covering).** $T^2 = \mathbb{R}^2 / \mathbb{Z}^2$ (with $\mathbb{Z}^2$ acting freely properly discontinuously by translations), and $\mathbb{R}^2$ is simply connected. So by the "free, proper, discontinuous, simply-connected total space" pattern, $\pi_1(T^2) = \mathbb{Z}^2$.

3. **Operation 7 from the topic page (use functoriality).** The two projections $p_1, p_2 : T^2 \to S^1$ induce $\pi_1(T^2) \to \pi_1(S^1) = \mathbb{Z}$ each. Together they give a homomorphism $\pi_1(T^2) \to \mathbb{Z} \times \mathbb{Z}$ that is bijective. This is the algebraic route.

---

# Hints

> [!note]- Hint 1
> The torus is a product space, so try to use the product formula $\pi_1(X \times Y) = \pi_1(X) \times \pi_1(Y)$. The two projections $T^2 \to S^1$ are continuous and induce homomorphisms on $\pi_1$.

> [!note]- Hint 2
> To prove the product formula, define the map $\pi_1(T^2) \to \pi_1(S^1) \times \pi_1(S^1)$ by $[\gamma] \mapsto ([p_1 \circ \gamma], [p_2 \circ \gamma])$. Show it is a bijective homomorphism. The inverse is $(a, b) \mapsto (a, b)$ (concatenate loop $a$ in the first factor with loop $b$ in the second, using the product space structure).

> [!note]- Hint 3
> Alternatively: lift loops on $T^2$ to paths in $\mathbb{R}^2$ via the covering map $\pi(x, y) = (e^{2\pi i x}, e^{2\pi i y})$. The endpoint of the lift is in $\mathbb{Z}^2$ (the fibre over $(1, 1)$). The two integer coordinates are the two winding numbers, giving the isomorphism with $\mathbb{Z}^2$.

> [!note]- Hint 4
> For the commutativity: the generators $[a]$ and $[b]$ both lift to translations of $\mathbb{R}^2$ in orthogonal directions, and translations commute. Alternatively, observe that $T^2$ is a topological group (componentwise multiplication), so $\pi_1(T^2)$ is automatically abelian by the Eckmann-Hilton argument — see [[Ex - Pi_1 of a Topological Group is Abelian]].

---

# Solution

**Plan:** The proof has two parallel components. First, we establish the **product formula** $\pi_1(X \times Y) = \pi_1(X) \times \pi_1(Y)$ via the projection homomorphisms and their inverse. Second, we *separately* verify the commutativity of the generators using the universal cover $\mathbb{R}^2 \to T^2$, which makes geometric sense of the algebraic fact. The non-obvious move is identifying the two-sided inverse for the projection homomorphism using the product space structure.

**Step 1: The projection homomorphism is a bijection.**

The projections $p_1, p_2 : T^2 \to S^1$ induce $(p_1)_*, (p_2)_* : \pi_1(T^2) \to \pi_1(S^1)$. Combined,
$$\Phi : \pi_1(T^2, *) \to \pi_1(S^1) \times \pi_1(S^1), \quad [\gamma] \mapsto ((p_1)_*[\gamma], (p_2)_*[\gamma]).$$

> [!note]- Derivation
> $\Phi$ is a homomorphism: $\Phi([\gamma \cdot \delta]) = ((p_1)_*[\gamma \cdot \delta], (p_2)_*[\gamma \cdot \delta]) = ((p_1)_*[\gamma] \cdot (p_1)_*[\delta], (p_2)_*[\gamma] \cdot (p_2)_*[\delta])$. The latter equals $\Phi([\gamma]) \cdot \Phi([\delta])$ in the product group, by component-wise multiplication.
>
> $\Phi$ is injective: suppose $\Phi([\gamma]) = (0, 0)$, i.e., $p_1 \circ \gamma$ and $p_2 \circ \gamma$ are both null-homotopic in $S^1$. Let $H_1, H_2 : I \times I \to S^1$ be the null-homotopies, fixing the base point $1$. Then $H := (H_1, H_2) : I \times I \to T^2$ is a continuous map (component-wise continuous), satisfying $H(s, 0) = (p_1\gamma(s), p_2\gamma(s)) = \gamma(s)$, $H(s, 1) = (1, 1) = *$, and $H(0, t) = H(1, t) = (1, 1) = *$. So $H$ is a path-homotopy rel endpoints from $\gamma$ to the constant loop. Hence $[\gamma] = 0$.
>
> $\Phi$ is surjective: given $(\alpha, \beta) \in \pi_1(S^1) \times \pi_1(S^1)$, choose loop representatives $\alpha, \beta : I \to S^1$ at $1$. The loop $\gamma : I \to T^2$ defined by $\gamma(s) = (\alpha(s), \beta(s))$ has $p_1 \circ \gamma = \alpha$ and $p_2 \circ \gamma = \beta$, so $\Phi([\gamma]) = ([\alpha], [\beta])$.
>
> So $\Phi$ is a bijective homomorphism, hence an isomorphism.

**Step 2: Apply $\pi_1(S^1) = \mathbb{Z}$ to get $\pi_1(T^2) = \mathbb{Z} \times \mathbb{Z} = \mathbb{Z}^2$.**

> [!note]- Derivation
> [[Thm - Pi_1 of S^1 is Z|\pi₁(S^1) = ℤ]] applied to each factor gives $\pi_1(S^1) \times \pi_1(S^1) = \mathbb{Z} \times \mathbb{Z} = \mathbb{Z}^2$. Combined with Step 1: $\pi_1(T^2) \cong \mathbb{Z}^2$.
>
> Under this isomorphism, the generator $[a]$ of $\pi_1(T^2)$ corresponds to $(1, 0) \in \mathbb{Z}^2$ (winding number $1$ in the first factor, $0$ in the second), and the generator $[b]$ corresponds to $(0, 1)$.

**Step 3: Verify commutativity geometrically via the universal cover.**

> [!note]- Derivation
> The covering map $\pi : \mathbb{R}^2 \to T^2$, $\pi(x, y) = (e^{2\pi i x}, e^{2\pi i y})$, is the universal cover of $T^2$ since $\mathbb{R}^2$ is simply connected. The deck group is $\mathbb{Z}^2 = \{(m, n) : m, n \in \mathbb{Z}\}$ acting by translation $(x, y) \mapsto (x + m, y + n)$. By the [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]], $\pi_1(T^2) \cong \mathrm{Deck}(\mathbb{R}^2 / T^2) = \mathbb{Z}^2$.
>
> Under this identification, the generator $[a]$ corresponds to the translation $(x, y) \mapsto (x + 1, y)$ and $[b]$ to $(x, y) \mapsto (x, y + 1)$. These translations commute: $(x + 1, y + 1) = (x + 1, y + 1)$ regardless of order. So $\pi_1(T^2)$ is abelian.

**Step 4: Generalisation to $T^n$.**

> [!note]- Derivation
> The same argument extends inductively. The $n$-torus $T^n = (S^1)^n$ has universal cover $\mathbb{R}^n \to T^n$ via $(x_1, \dots, x_n) \mapsto (e^{2\pi i x_1}, \dots, e^{2\pi i x_n})$, with deck group $\mathbb{Z}^n$ acting by integer translations.
>
> Alternatively, by induction on $n$: $T^n = T^{n-1} \times S^1$, so $\pi_1(T^n) = \pi_1(T^{n-1}) \times \pi_1(S^1) = \mathbb{Z}^{n-1} \times \mathbb{Z} = \mathbb{Z}^n$ by the product formula and the inductive hypothesis.
>
> Generators: $e_i \in \mathbb{Z}^n$ corresponds to the loop $\omega_i(\theta) = (1, \dots, 1, e^{2\pi i \theta}, 1, \dots, 1)$ with non-trivial entry in position $i$.

> [!note]- Complete formal solution
> **Theorem.** $\pi_1(T^n) \cong \mathbb{Z}^n$ for every $n \geq 1$, with generators $[\omega_1], \dots, [\omega_n]$ where $\omega_i$ is the standard loop in the $i$-th coordinate.
>
> *Proof.* The covering map $\pi : \mathbb{R}^n \to T^n$ defined by $\pi(x_1, \dots, x_n) = (e^{2\pi i x_1}, \dots, e^{2\pi i x_n})$ is a continuous surjection. Each small open product $U_1 \times \cdots \times U_n$ in $T^n$ (with each $U_j$ an evenly covered open arc in $S^1$) is evenly covered: its preimage is the disjoint union $\bigsqcup_{(k_1, \dots, k_n) \in \mathbb{Z}^n} \widetilde U_{k_1} \times \cdots \times \widetilde U_{k_n}$ where $\widetilde U_{k_j} = (\text{angle interval}) + k_j$. So $\pi$ is a covering map.
>
> $\mathbb{R}^n$ is simply connected (convex, hence contractible, hence $\pi_1 = 0$ — see [[Def - Simply Connected Space]]). So $\pi : \mathbb{R}^n \to T^n$ is the **universal cover**. By the Galois correspondence ([[Thm - Galois Correspondence for Covering Spaces]]), $\pi_1(T^n) \cong \mathrm{Deck}(\mathbb{R}^n / T^n)$.
>
> The deck group consists of self-homeomorphisms $\varphi : \mathbb{R}^n \to \mathbb{R}^n$ with $\pi \circ \varphi = \pi$, i.e., $e^{2\pi i \varphi_j(x)} = e^{2\pi i x_j}$ for each $j$, hence $\varphi_j(x) \in x_j + \mathbb{Z}$. By continuity and connectedness of $\mathbb{R}^n$, each $\varphi_j(x) - x_j$ is a constant integer. So $\varphi(x) = x + k$ for some $k = (k_1, \dots, k_n) \in \mathbb{Z}^n$. Composition of such translations is addition of integer vectors, so $\mathrm{Deck}(\mathbb{R}^n / T^n) \cong \mathbb{Z}^n$ (under addition).
>
> Hence $\pi_1(T^n) \cong \mathbb{Z}^n$, and is abelian. The generators $e_1, \dots, e_n$ of $\mathbb{Z}^n$ correspond to the unit translations of $\mathbb{R}^n$, which (under the deck group ↔ $\pi_1$ identification) correspond to the standard loops $\omega_1, \dots, \omega_n$.
>
> $\qquad\blacksquare$

---

# Key Takeaways

**Product formula for $\pi_1$ as a recurring tool.** The identity $\pi_1(X \times Y) = \pi_1(X) \times \pi_1(Y)$ is the cleanest computational tool of the chapter — and it works without any hypothesis beyond products being well-formed. The trigger condition is: the space is given as a product (or deformation-retracts to one). The transferable diagnostic: whenever a problem presents a space as $X \times Y$ or as a fibration with trivial monodromy (a product up to fibres), the product formula computes $\pi_1$ as a direct product. This trivialises $\pi_1$ of all tori, spheres-times-tori, products of Lie groups, products of surfaces — every product setting in differential geometry, complex geometry, and topology where one wants $\pi_1$ in a single line.

**Universal covers via free properly discontinuous group actions.** When a space is presented as a quotient $X = \tilde X / \Gamma$ by a free properly discontinuous action of a discrete group on a simply-connected $\tilde X$, the answer for $\pi_1$ is automatic: $\pi_1(X) = \Gamma$. The trigger condition is: a discrete group action on a contractible (or simply connected) space, with the right freeness/properness. The transferable diagnostic: this pattern computes $\pi_1$ of *every* space that comes as a quotient — $T^n = \mathbb{R}^n / \mathbb{Z}^n$, $\mathbb{RP}^n = S^n / \{\pm 1\}$, $\mathbb{H}^2 / \Gamma$ for hyperbolic surface groups, $\mathbb{R}^n / \Gamma$ for crystallographic groups, $\mathrm{SU}(n)/Z(\mathrm{SU}(n))$ for adjoint Lie groups. Whenever the discrete-group-on-simply-connected pattern appears, $\pi_1$ is read off without any computation beyond identifying the group.

**Commutativity of $\pi_1$ from the universal cover's algebraic structure.** $\pi_1(T^n)$ being abelian is *not* an accident — it follows from the universal cover $\mathbb{R}^n$ being an *abelian Lie group* and the deck group being a *subgroup* of that Lie group's translation group. More generally: $\pi_1$ of a topological group is always abelian (Eckmann-Hilton; [[Ex - Pi_1 of a Topological Group is Abelian]]), which gives a *second* reason $\pi_1(T^n)$ is abelian. The double justification (geometric: translations commute; algebraic: topological group → abelian) is a useful pattern: when two independent arguments give the same conclusion, the conclusion is robust and the underlying principle is structural rather than coincidental.

**The relationship between $\pi_1$ and $H_1$ for $T^n$.** Since $\pi_1(T^n) = \mathbb{Z}^n$ is abelian, its abelianisation is itself, so by Hurewicz $H_1(T^n; \mathbb{Z}) = \pi_1(T^n)^{\mathrm{ab}} = \mathbb{Z}^n$. So the first Betti number is $b_1(T^n) = n$. This is consistent with the cohomology calculation $H^1(T^n; \mathbb{R}) = \mathbb{R}^n$ (one harmonic 1-form per coordinate). More importantly, this is the *prototypical* case where $\pi_1$ and $H_1$ agree exactly — for non-abelian $\pi_1$ (like surfaces of genus $\geq 2$), the abelianisation throws information away. See [[Algebraic Topology I — Singular Homology and the de Rham Theorem]] and [[Ex - Pi_1 of a Topological Group is Abelian]].
