---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Covering Space"
  - "Def - Universal Cover"
  - "Def - Simply Connected Space"
  - "Thm - Galois Correspondence for Covering Spaces"
tags: [geometry, algebraic-topology, topology]
---

# Problem Statement

Compute $\pi_1(\mathbb{RP}^n)$ for $n \geq 2$ using the antipodal double cover $S^n \to \mathbb{RP}^n$. Show $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$.

Verify also: (a) $\pi_1(\mathbb{RP}^1) = \mathbb{Z}$ (not $\mathbb{Z}/2$), since $\mathbb{RP}^1 \cong S^1$ and the antipodal map on $S^1$ is just rotation by $\pi$; (b) the non-trivial element of $\pi_1(\mathbb{RP}^n)$ for $n \geq 2$ is represented by a "great half-circle" path in $\mathbb{RP}^n$ joining a point to itself (via its antipode in $S^n$); (c) the universal cover of $\mathbb{RP}^n$ (for $n \geq 2$) is $S^n$.

**Recall:**

The universal cover construction:

![[Def - Universal Cover#The Definition]]

Simply connected spaces and why $S^n$ is simply connected for $n \geq 2$:

![[Def - Simply Connected Space#The Definition]]

The Galois correspondence:

![[Thm - Galois Correspondence for Covering Spaces#Statement]]

---

# Convergent Strategy

**Problem class:** Computation of $\pi_1$ for a *quotient by a free group action on a simply-connected space*. The pattern is the cleanest in the chapter: $X = \tilde X / \Gamma$ with $\tilde X$ simply connected and $\Gamma$ acting freely properly discontinuously gives $\pi_1(X) = \Gamma$ immediately. For $\mathbb{RP}^n$, $\Gamma = \mathbb{Z}/2 = \{\pm 1\}$ acting antipodally on $S^n$.

**Assumption pattern:** $\mathbb{RP}^n$ is given as the quotient of $S^n$ by the antipodal map $x \mapsto -x$ (a $\mathbb{Z}/2$-action). The action is free for all $n$ (no fixed points; $x = -x$ would require $2x = 0$, but $|x| = 1$). The total space $S^n$ is simply connected for $n \geq 2$ (an instance of "spheres of high dimension are simply connected" — see [[Def - Simply Connected Space]]). The freeness + simple-connectedness + properness combination is the setup for the universal cover argument.

**Theorem routing:** Apply the [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]] in the special case "universal cover by simply-connected quotient." The deck group of the universal cover equals $\pi_1$. The deck group of $S^n \to \mathbb{RP}^n$ is $\mathbb{Z}/2$ (only the identity and antipodal map commute with $p$). So $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ for $n \geq 2$. For $n = 1$ this argument fails because $S^1$ is *not* simply connected; the universal cover of $\mathbb{RP}^1 = S^1$ is instead $\mathbb{R}$, with deck group $\mathbb{Z}$.

**Key decision point:** Why $n \geq 2$ is the right threshold. The universal-cover argument relies on $S^n$ being simply connected, which holds iff $n \geq 2$. For $n = 1$, the antipodal cover $S^1 \to \mathbb{RP}^1 = S^1$ is still a covering (it is the 2-fold cover $z \mapsto z^2$), but it is not the *universal* cover, so the deck group ($\mathbb{Z}/2$) does not equal $\pi_1$. The correct universal cover of $S^1$ is $\mathbb{R}$, giving $\pi_1(S^1) = \mathbb{Z}$. The dimension threshold is the entire content of the dichotomy.

---

# Legal Operations Used

1. **Operation 4 from the topic page (identify $\pi_1$ via a free properly discontinuous action on a simply-connected space).** The antipodal action $\mathbb{Z}/2 \curvearrowright S^n$ is free and properly discontinuous, and $S^n$ is simply connected for $n \geq 2$. So $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ for $n \geq 2$.

2. **Operation 6 from the topic page (pass to the universal cover).** For $n \geq 2$, the universal cover of $\mathbb{RP}^n$ is $S^n$ (since $S^n$ is simply connected and the antipodal cover is 2-sheeted). Reading off the deck group gives $\pi_1$.

3. **Operation 1 from the topic page (lift a loop through the cover).** A loop in $\mathbb{RP}^n$ lifts to a path in $S^n$ from a chosen starting point to either the same point (trivial class) or its antipode (non-trivial class). This concretely identifies the two elements of $\pi_1(\mathbb{RP}^n)$ and shows the non-trivial loop is geometrically a "great half-circle."

---

# Hints

> [!note]- Hint 1
> $\mathbb{RP}^n$ is defined as $S^n / \{\pm 1\}$ (the antipodal quotient). The quotient map $S^n \to \mathbb{RP}^n$ is a covering map. Use this together with the topology of $S^n$.

> [!note]- Hint 2
> Is $S^n$ simply connected? For $n \geq 2$: yes (any loop on $S^n$ can be perturbed off any point and contracted in the complement, which is contractible). For $n = 1$: no, $S^1$ has $\pi_1 = \mathbb{Z}$. This is the dimension threshold.

> [!note]- Hint 3
> For $n \geq 2$, the antipodal map $S^n \to S^n$ is the *deck transformation* of the covering $S^n \to \mathbb{RP}^n$. The deck group is $\mathbb{Z}/2$ (just identity and antipodal). Apply [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]].

> [!note]- Hint 4
> The non-trivial element of $\pi_1(\mathbb{RP}^n)$ for $n \geq 2$ is represented by: take any great half-circle in $S^n$ joining a point $x$ to its antipode $-x$; project to $\mathbb{RP}^n$ to get a loop at $[x] = [-x]$. This loop's lift to $S^n$ does *not* return to $x$, so it is non-trivial. But traversing it *twice* lifts to a loop in $S^n$ (going there and back), hence is trivial in $\pi_1(\mathbb{RP}^n)$.

---

# Solution

**Plan:** The proof has three steps. First, verify that $S^n \to \mathbb{RP}^n$ is a covering map. Second, observe that $S^n$ is simply connected for $n \geq 2$, so the cover is *universal*. Third, identify the deck group as $\mathbb{Z}/2$, giving $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ by the Galois correspondence. The geometric picture of the non-trivial loop and the dimension-1 contrast are highlighted.

**Step 1: The antipodal map gives a covering $S^n \to \mathbb{RP}^n$.**

> [!note]- Derivation
> $\mathbb{RP}^n = S^n / \sim$ where $x \sim -x$. The quotient map $p : S^n \to \mathbb{RP}^n$ sends $x$ to $\{x, -x\}$. For any point $[x] \in \mathbb{RP}^n$, take a small open spherical cap $U$ around $x$ in $S^n$ that does not meet $-U$ (the antipodal cap). For example, $U = \{y \in S^n : d(y, x) < \epsilon\}$ for small $\epsilon$ has $-U = \{y : d(y, -x) < \epsilon\}$ disjoint from $U$ as long as $\epsilon < \pi/2$ (since $d(x, -x) = \pi$).
>
> The projection $p$ identifies $U$ and $-U$ bijectively, so $p^{-1}(p(U)) = U \cup (-U)$, a disjoint union of two open sets, each mapped homeomorphically to $p(U)$. So $p(U)$ is evenly covered.
>
> The action of $\mathbb{Z}/2 = \{\pm 1\}$ on $S^n$ is free (no fixed points: $x \neq -x$ for $|x| = 1$) and properly discontinuous (the disjoint $U \cup (-U)$ verifies the property for each point). So $S^n \to \mathbb{RP}^n$ is a 2-sheeted covering map. The deck group is $\mathbb{Z}/2$ generated by the antipodal map $x \mapsto -x$.

**Step 2: For $n \geq 2$, $S^n$ is simply connected, so $S^n \to \mathbb{RP}^n$ is the universal cover.**

> [!note]- Derivation
> For $n \geq 2$, $S^n$ is simply connected. The standard argument: pick a loop $\gamma : I \to S^n$ at a base point $x_0$. Pick any other point $p \neq x_0$ on $S^n$ not lying on $\gamma$ — possible because the image $\gamma(I)$ is a compact subset of the smooth $n$-manifold $S^n$, so has measure zero in $S^n$, so $S^n \setminus \gamma(I)$ is non-empty for $n \geq 2$. The complement $S^n \setminus \{p\}$ is homeomorphic to $\mathbb{R}^n$ (via stereographic projection from $p$ — see [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]]), which is contractible. So $\gamma$, which lies in $S^n \setminus \{p\} \cong \mathbb{R}^n$, can be contracted within $\mathbb{R}^n$ to the constant loop at $x_0$. Hence $[\gamma] = 0$ in $\pi_1(S^n)$.
>
> (For $n = 1$: the loop $\gamma$ might *fill* $S^1$, so the complement of any point might be empty along $\gamma$. The argument fails, and indeed $\pi_1(S^1) = \mathbb{Z} \neq 0$.)
>
> So $S^n$ is simply connected for $n \geq 2$, and since the cover $S^n \to \mathbb{RP}^n$ has simply-connected total space, *it is the universal cover* by definition.

**Step 3: By the Galois correspondence, $\pi_1(\mathbb{RP}^n) \cong \mathrm{Deck}(S^n / \mathbb{RP}^n) = \mathbb{Z}/2$.**

> [!note]- Derivation
> By [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]], for the universal cover $\widetilde X \to X$, $\pi_1(X) \cong \mathrm{Deck}(\widetilde X / X)$. The deck group of $S^n \to \mathbb{RP}^n$ consists of self-homeomorphisms $\varphi : S^n \to S^n$ with $p \circ \varphi = p$, i.e., $\varphi(x) \in \{x, -x\}$ for every $x$.
>
> By continuity, either $\varphi(x) = x$ for all $x$ (identity) or $\varphi(x) = -x$ for all $x$ (antipodal map). (The set $\{x : \varphi(x) = x\}$ is open and closed in $S^n$, hence either empty or all of $S^n$ by connectedness.) So $\mathrm{Deck}(S^n / \mathbb{RP}^n) = \{\mathrm{id}, -\mathrm{id}\} \cong \mathbb{Z}/2$.
>
> Hence $\pi_1(\mathbb{RP}^n) \cong \mathbb{Z}/2$ for $n \geq 2$.

**Step 4: Geometric description of the non-trivial element.**

> [!note]- Derivation
> The non-trivial element of $\pi_1(\mathbb{RP}^n)$ for $n \geq 2$ is represented by: take a great half-circle $\alpha$ in $S^n$ from a point $x_0$ to its antipode $-x_0$ — for instance, $\alpha(t) = (\cos\pi t \cdot x_0 + \sin\pi t \cdot y_0)$ for any unit vector $y_0$ orthogonal to $x_0$. The projection $p \circ \alpha : I \to \mathbb{RP}^n$ is a loop at $[x_0] = [-x_0] \in \mathbb{RP}^n$.
>
> The lift of $p \circ \alpha$ starting at $x_0$ is $\alpha$ itself, ending at $-x_0 \neq x_0$. So by the universal-cover identification $\pi_1(\mathbb{RP}^n) = \mathrm{fibre} \,p^{-1}([x_0]) = \{x_0, -x_0\}$, the loop $p \circ \alpha$ corresponds to the non-trivial fibre point $-x_0$, hence the non-trivial element of $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$.
>
> Traversing the loop *twice* lifts to a closed path in $S^n$ (go from $x_0$ to $-x_0$, then $-x_0$ back to $x_0$ via the second traversal of $-\alpha$). This is a loop in $S^n$, hence null-homotopic (since $S^n$ simply connected), so $2 \cdot [p \circ \alpha] = 0$ in $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$. This confirms the group structure: it is $\mathbb{Z}/2$, not $\mathbb{Z}$.

**Step 5: Contrast with $n = 1$.**

> [!note]- Derivation
> For $n = 1$, $S^1$ is *not* simply connected. The covering $S^1 \to \mathbb{RP}^1$ (antipodal quotient) is still 2-sheeted, but it is not the universal cover. The universal cover of $\mathbb{RP}^1$ is $\mathbb{R}$ (since $\mathbb{RP}^1 \cong S^1$ via the homeomorphism $[z] \mapsto z^2$, and the universal cover of $S^1$ is $\mathbb{R}$). The Galois correspondence applied to the universal cover $\mathbb{R} \to \mathbb{RP}^1$ gives $\pi_1(\mathbb{RP}^1) = \mathbb{Z}$, not $\mathbb{Z}/2$.
>
> The discrepancy: for $n = 1$, the antipodal cover $S^1 \to \mathbb{RP}^1$ corresponds to the subgroup $2\mathbb{Z} \leq \mathbb{Z} = \pi_1(\mathbb{RP}^1)$, which is *not* the trivial subgroup. So the cover is regular (since $\mathbb{Z}$ is abelian), but it is not universal.

> [!note]- Complete formal solution
> **Theorem.** $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ for $n \geq 2$, generated by the homotopy class of a great half-circle loop. For $n = 1$, $\pi_1(\mathbb{RP}^1) = \mathbb{Z}$ (since $\mathbb{RP}^1 \cong S^1$).
>
> *Proof.* Consider the antipodal map $\sigma : S^n \to S^n$, $\sigma(x) = -x$. It is a homeomorphism, free of fixed points (since $|x| = 1 \neq 0$), and generates a group $\langle \sigma \rangle \cong \mathbb{Z}/2$ acting on $S^n$. The action is properly discontinuous: any point $x$ has a neighbourhood $U_x \subset S^n$ disjoint from $-U_x$ (e.g., the open hemisphere centred at $x$).
>
> The quotient $S^n / \langle \sigma \rangle = \mathbb{RP}^n$. The projection $p : S^n \to \mathbb{RP}^n$ is a 2-sheeted covering map (verified above).
>
> For $n \geq 2$: $S^n$ is simply connected (Step 2). So $S^n \to \mathbb{RP}^n$ is the *universal* cover of $\mathbb{RP}^n$. By the [[Thm - Galois Correspondence for Covering Spaces|Galois correspondence]], $\pi_1(\mathbb{RP}^n) \cong \mathrm{Deck}(S^n / \mathbb{RP}^n) = \langle \sigma \rangle \cong \mathbb{Z}/2$.
>
> The non-trivial element corresponds to the loop $p \circ \alpha$ in $\mathbb{RP}^n$, where $\alpha$ is a great half-circle in $S^n$ from $x_0$ to $-x_0$. The lift of $p \circ \alpha$ starting at $x_0$ ends at $-x_0$ — the other fibre point — confirming non-triviality.
>
> For $n = 1$: $\mathbb{RP}^1 \cong S^1$ via $[\cos\theta, \sin\theta] \mapsto e^{2i\theta}$. So $\pi_1(\mathbb{RP}^1) = \pi_1(S^1) = \mathbb{Z}$.
>
> $\qquad\blacksquare$

> [!warning] Illegal but tempting alternative route: "$\mathbb{Z}/2 \subseteq \pi_1$ since cover is 2-sheeted"
> One might try to argue "$\pi_1(\mathbb{RP}^n)$ contains $\mathbb{Z}/2$ because the antipodal cover is 2-sheeted." This is *almost* correct for $n \geq 2$ but wrong in general — a 2-sheeted cover corresponds to a subgroup of index 2, not a subgroup of order 2. For $n = 1$, the cover $S^1 \to S^1$ is 2-sheeted but $\pi_1(S^1) = \mathbb{Z}$ has no element of order 2 — the index-2 subgroup is $2\mathbb{Z} \cong \mathbb{Z}$, not $\mathbb{Z}/2$. The reason "2-sheeted → $\mathbb{Z}/2$ in $\pi_1$" *does* work for $n \geq 2$ is that the cover is *universal*, in which case sheet count = $|\pi_1|$. The slogan is: "sheet count = $|\pi_1|$" is true only for the universal cover.

---

# Key Takeaways

**The "free properly discontinuous action on simply-connected space" is the universal computation engine.** Whenever you have a space presented as $X = \tilde X / \Gamma$ with $\Gamma$ a discrete group acting freely properly discontinuously on a simply-connected $\tilde X$, $\pi_1(X) = \Gamma$ without further computation. The trigger condition is: a discrete-group action on a recognisable simply-connected space, with the freeness/properness conditions. The transferable diagnostic: this pattern computes $\pi_1$ of *every* space arising as such a quotient — $T^n = \mathbb{R}^n/\mathbb{Z}^n$ giving $\pi_1 = \mathbb{Z}^n$, $\mathbb{RP}^n = S^n/(\mathbb{Z}/2)$ giving $\pi_1 = \mathbb{Z}/2$, the Klein bottle as $\mathbb{R}^2/\Gamma$ for a non-abelian semi-direct product $\Gamma$, hyperbolic surfaces as $\mathbb{H}^2/\Gamma$ for surface groups. The pattern is the cleanest in the chapter and should be the first thing to try when computing $\pi_1$.

**The dimension threshold $n \geq 2$ matters because of when $S^n$ is simply connected.** The slogan "$\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$" is *false* for $n = 1$ — the antipodal cover of $S^1$ is not the universal cover, because $S^1$ is not simply connected. This is a worked instance of the trigger-reaction pattern: "compute $\pi_1$ via universal cover" requires verifying that the candidate cover *is* universal — and for spheres, this means checking $n \geq 2$. The diagnostic: whenever using the universal-cover argument, the verification step "is the total space simply connected?" is non-negotiable. Failing to check leads to wrong answers in low dimensions.

**The "great half-circle" picture explains why $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ has *order* 2.** The non-trivial loop in $\mathbb{RP}^n$ is a great half-circle in $S^n$ projected down; its lift to $S^n$ does not close, but its *double* does — the doubled loop's lift goes from a point to its antipode and back, forming a full great circle, which is null-homotopic in $S^n$. So in $\mathbb{RP}^n$, the loop's *square* is trivial — hence $\pi_1$ has an element of order $2$, and only that. The trigger condition is: a covering where the deck group has order $k$ and the total space is simply connected, so $\pi_1 = \mathbb{Z}/k$; the doubling-trivialises picture is the geometric content of "deck group is cyclic of order $k$." This pattern explains $\pi_1(\mathrm{SO}(3)) = \mathbb{Z}/2$ via $\mathrm{SU}(2) \cong S^3$ in the same way — see [[Ex - SU(2) is the Universal Cover of SO(3)]].

**The relationship between $\pi_1(\mathbb{RP}^n)$, orientability, and double covers.** $\mathbb{RP}^n$ is orientable iff $n$ is odd; for $n$ even, the orientation double cover is $S^n$. For $n \geq 2$, the orientation double cover and the universal cover *coincide* when $n$ is even (both are $S^n$ with the antipodal $\mathbb{Z}/2$-action), and *differ* when $n$ is odd (orientation cover is trivial, but the universal cover is still $S^n$). This is a coincidence of $\pi_1$ and $w_1$ in even dimensions, and is the prototype example of "characteristic classes and $\pi_1$" interactions. See [[Def - Orientable Double Cover]] and [[Algebraic Topology III — Higher Homotopy and Chern Forms]].
