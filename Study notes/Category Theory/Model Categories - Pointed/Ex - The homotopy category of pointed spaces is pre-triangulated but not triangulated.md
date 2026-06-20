---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Pre-Triangulated Category"
  - "Def - Pointed Model Category Suspension and Loop"
  - "Thm - The Puppe Cofiber and Fiber Sequences Agree"
  - "Def - Higher Homotopy Group"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{T} = \mathrm{Ho}(\mathbf{Top}_*)$ be the homotopy category of pointed spaces.

1. Verify that $\mathcal{T}$ is a [[Def - Pre-Triangulated Category|pre-triangulated category]]: it is pointed, carries the adjunction $\Sigma \dashv \Omega$, has cofiber and fiber sequences, and the long-exact-sequence axioms hold.
2. Show that $\Sigma : \mathcal{T} \to \mathcal{T}$ is **not** an equivalence, so $\mathcal{T}$ is **not** triangulated. Give two distinct witnesses: (a) the unit $\eta : X \to \Omega\Sigma X$ is not an isomorphism for $X = S^0$; (b) not every object is a suspension.
3. State precisely which axiom separates pre-triangulated from triangulated and why $\mathbf{Top}_*$ fails it.

**Recall:**

![[Def - Pre-Triangulated Category#The Definition]]

A [[Def - Pre-Triangulated Category|pre-triangulated category]] becomes **triangulated** exactly when $\Sigma$ is an equivalence (so $\Omega = \Sigma^{-1}$ and the unit/counit are isomorphisms). By [[Thm - The Puppe Cofiber and Fiber Sequences Agree]], $\mathrm{Ho}(\mathcal{C})$ is always pre-triangulated. The [[Def - Higher Homotopy Group|homotopy group]] $\pi_n(Y) = [S^n, Y]$; $\Omega S^1 \simeq \mathbb{Z}$ (discrete), since $\pi_n(\Omega S^1) = \pi_{n+1}(S^1) = 0$ for $n \ge 1$ and $\pi_0(\Omega S^1) = \pi_1(S^1) = \mathbb{Z}$.

---

# Convergent Strategy

**Problem class:** This is a "verify the structural axioms, then locate the discriminating hypothesis" exercise. The route is to confirm the pre-triangulated ingredients (mostly already established in the chapter) and then refute invertibility of $\Sigma$ with explicit witnesses.

**Assumption pattern:** The pre-triangulated structure on $\mathrm{Ho}(\mathbf{Top}_*)$ is *given* by the chapter's main theorem; the work is the refutation of triangulation. The key assumption to exploit is that $\Omega\Sigma X \simeq X$ is the precise condition for $\Sigma$ to be invertible, so a single object where it fails settles the matter.

**Theorem routing:** Part (1) routes through [[Thm - The Puppe Cofiber and Fiber Sequences Agree]] (which proves $\mathrm{Ho}(\mathcal{C})$ is pre-triangulated) and the chapter's constructions. Part (2a) routes through computing $\Omega\Sigma S^0 = \Omega S^1$ and comparing homotopy types with $S^0$. Part (2b) routes through a connectivity/dimension obstruction to being a suspension. Part (3) routes through the definition's "$\Sigma$ an equivalence" clause.

**Key decision point:** The interesting choice is *which object* to test for $\Omega\Sigma X \simeq X$. Choosing $X = S^0$ is decisive because $\Sigma S^0 = S^1$ and $\Omega S^1$ is computable (homotopy equivalent to the discrete space $\mathbb{Z}$), which is manifestly not $S^0$. A poor choice (an object where $\eta$ happens to be close to an iso) would obscure the failure; $S^0$ makes it stark.

---

# Legal Operations Used

1. **Operation 3 from the topic page (recognize a homotopy pushout/pullback square with a corner at $*$).** Part (1) uses the cofiber and fiber squares to confirm the distinguished classes exist.

2. **Operation 6 from the topic page (use the suspension–loop adjunction).** Part (2a) computes $\Omega\Sigma S^0$ and uses $\pi_n(\Omega Y) = \pi_{n+1}(Y)$.

3. **Operation 1 from the topic page (homotopy versions of (co)limits) and the diagnostic "is $\Omega\Sigma X \simeq X$?".** Part (2)–(3) hinge on this diagnostic separating pre-triangulated from triangulated.

---

# Hints

> [!note]- Hint 1
> Part (1) is mostly citation: the chapter proves $\mathrm{Ho}(\mathcal{C})$ is pre-triangulated for any pointed model category. List the four ingredients and point to where each was established.

> [!note]- Hint 2
> For (2a), compute $\Sigma S^0 = S^1$, then $\Omega S^1$. Use $\pi_n(\Omega S^1) = \pi_{n+1}(S^1)$. What are the homotopy groups of $S^1$?

> [!note]- Hint 3
> $\pi_{n+1}(S^1) = 0$ for $n \ge 1$ and $\pi_1(S^1) = \mathbb{Z}$, so $\Omega S^1$ has $\pi_0 = \mathbb{Z}$ and all higher groups zero — it is homotopy equivalent to the discrete space $\mathbb{Z}$. That is not $S^0$ (which has $\pi_0$ a two-element set). So $\eta : S^0 \to \Omega\Sigma S^0$ is not an isomorphism.

---

# Solution

The solution confirms the pre-triangulated axioms by citing the chapter's constructions, then refutes triangulation by showing $\Omega\Sigma S^0 \ne S^0$ and that not every object is a suspension.

**Step 1: $\mathrm{Ho}(\mathbf{Top}_*)$ is pre-triangulated.**

> [!note]- Derivation
> Check the four ingredients of a [[Def - Pre-Triangulated Category|pre-triangulated category]]. (i) *Pointed:* the one-point space $*$ is the zero object of $\mathbf{Top}_*$, so $\mathcal{T}$ is pointed with zero maps. (ii) *Adjunction $\Sigma \dashv \Omega$:* established in [[Thm - The Suspension-Loop Adjunction]] for any pointed model category. (iii) *Cofiber and fiber sequences:* the [[Def - Cofiber and Fiber Sequence|Puppe sequences]] of cofibrations and fibrations, established in §6.2. (iv) *Long-exact-sequence and compatibility axioms:* exactly the content of [[Thm - The Puppe Cofiber and Fiber Sequences Agree]], which proves $\mathrm{Ho}(\mathcal{C})$ is pre-triangulated for any pointed model category $\mathcal{C}$; specialize $\mathcal{C} = \mathbf{Top}_*$. Hence $\mathcal{T}$ is pre-triangulated.

**Step 2: $\Sigma$ is not an equivalence.**

> [!note]- Derivation
> **Witness (a): the unit is not an isomorphism.** Take $X = S^0$. Then $\Sigma S^0 = S^1$, and $\Omega\Sigma S^0 = \Omega S^1$. Compute the homotopy of $\Omega S^1$ via [[Thm - The Suspension-Loop Adjunction|the adjunction]] $\pi_n(\Omega S^1) = \pi_{n+1}(S^1)$:
> $$\pi_0(\Omega S^1) = \pi_1(S^1) = \mathbb{Z}, \qquad \pi_n(\Omega S^1) = \pi_{n+1}(S^1) = 0 \ (n \ge 1),$$
> since $S^1$ has contractible universal cover $\mathbb{R}$, so $\pi_{\ge 2}(S^1) = 0$. Thus $\Omega S^1$ is weakly equivalent to the **discrete countable space** $\mathbb{Z}$. The unit $\eta : S^0 \to \Omega\Sigma S^0 = \Omega S^1$ sends the two points of $S^0$ to two of the countably many points of $\mathbb{Z}$; it is not an isomorphism (its target has $\pi_0 = \mathbb{Z}$, a countable set, while $S^0$ has $\pi_0 = \{*, p\}$, a two-element set). So $\Sigma$ is not an equivalence.
>
> **Witness (b): not every object is a suspension.** If $\Sigma$ were an equivalence, every object $Y$ would be $\Sigma(\Sigma^{-1} Y)$, hence a suspension. But a suspension $\Sigma A$ is always **simply connected after one suspension** in the sense that $\Sigma A$ is a co-$H$-space, so its fundamental group is *free* and, more sharply, $\widetilde{H}_*(\Sigma A)$ has trivial cup products (the reduced cohomology of a suspension is a square-zero ring). Take $Y = \mathbb{C}P^2$ (pointed): its cohomology ring $\widetilde{H}^*(\mathbb{C}P^2) = \mathbb{Z}\{x, x^2\}$ with $x \in H^2$, $x^2 \ne 0$ has a nontrivial cup product, so $\mathbb{C}P^2$ is **not** a suspension. Hence $\Sigma$ is not essentially surjective, so not an equivalence.

**Step 3: The discriminating axiom.**

> [!note]- Derivation
> The single clause separating [[Def - Pre-Triangulated Category|pre-triangulated]] from **triangulated** is "$\Sigma$ is an equivalence" (equivalently, the unit $\eta$ and counit $\varepsilon$ of $\Sigma \dashv \Omega$ are natural isomorphisms, so $\Omega = \Sigma^{-1}$). Pre-triangulated requires only the adjunction $\Sigma \dashv \Omega$; triangulated additionally requires invertibility, which then merges the cofiber and fiber sequence classes into one class of distinguished triangles and supports the octahedral axiom. $\mathbf{Top}_*$ fails invertibility, as Step 2 shows: $\Omega\Sigma S^0 \not\simeq S^0$ (unit not iso) and $\mathbb{C}P^2$ is not a suspension (not essentially surjective). The depth of this failure is measured by the **Freudenthal suspension theorem**, which says $\eta : X \to \Omega\Sigma X$ is an isomorphism only in a range of degrees below twice the connectivity of $X$ — invertibility holds *stably*, not unstably, and forcing it is exactly the passage to spectra.

> [!note]- Complete formal solution
> **(1)** $\mathrm{Ho}(\mathbf{Top}_*)$ is pointed ($*$ is the zero object), has $\Sigma \dashv \Omega$ ([[Thm - The Suspension-Loop Adjunction]]), has cofiber/fiber sequences (§6.2), and satisfies the long-exact-sequence and compatibility axioms ([[Thm - The Puppe Cofiber and Fiber Sequences Agree]]). So it is pre-triangulated.
>
> **(2)** $\Sigma$ is not an equivalence: (a) $\Omega\Sigma S^0 = \Omega S^1 \simeq \mathbb{Z}$ (discrete), since $\pi_n(\Omega S^1) = \pi_{n+1}(S^1)$ gives $\pi_0 = \mathbb{Z}$ and higher groups $0$, so $\eta : S^0 \to \Omega S^1$ is not an iso; (b) $\mathbb{C}P^2$ has nontrivial cup product $x^2 \ne 0$, but suspensions have square-zero reduced cohomology, so $\mathbb{C}P^2$ is not a suspension and $\Sigma$ is not essentially surjective.
>
> **(3)** The separating axiom is invertibility of $\Sigma$; $\mathbf{Top}_*$ fails it, as Step 2 shows, and the Freudenthal theorem quantifies the failure. $\blacksquare$

---

# Key Takeaways

**The pre-triangulated/triangulated divide is a single axiom — invertibility of $\Sigma$ — and it is the unstable/stable divide.** Everything else in the two structures is shared; the only difference is whether $\Sigma$ is an equivalence. This is not a technicality but the most important dichotomy in homotopy theory: spaces are eternally unstable because $\Sigma$ is far from invertible, while spectra and derived categories are stable because $\Sigma$ is inverted (by construction or automatically). The diagnostic to carry into any such question is the single test "is $\Omega\Sigma X \simeq X$?" — answering it decides triangulation, and the productive object to test is usually a low-dimensional sphere where both sides are computable.

**Suspensions are special objects, and cup products detect that they are special.** The witness $\mathbb{C}P^2$ is worth remembering as the canonical "not a suspension," and the reason — suspensions have square-zero reduced cohomology rings (they are co-$H$-spaces, so the diagonal is coreduced) — is a reusable obstruction. The transferable trigger is: to show an object is not a suspension, exhibit a nontrivial cup product, since the reduced cohomology of any $\Sigma A$ has trivial products. This is one of the cleanest "is NOT" tests in the subject and generalizes: co-$H$-structure forces vanishing products, so any nonvanishing product obstructs being a (co-)suspension.

**The Freudenthal theorem is the precise measure of how non-invertible suspension is.** That $\eta : X \to \Omega\Sigma X$ is an isomorphism only in a stable range — degrees below roughly twice the connectivity — is the quantitative heart of the unstable/stable story. It explains why $\mathbf{Top}_*$ is merely pre-triangulated (invertibility fails outside the range) and why stabilizing (forcing $\eta$ to be an iso in all degrees by passing to spectra) yields a triangulated category. The takeaway for working with these structures is that "pre-triangulated" is the honest level for unstable homotopy theory, and any time you find yourself wanting $\Omega\Sigma X = X$, you are implicitly working stably and should pass to spectra to make it true.
