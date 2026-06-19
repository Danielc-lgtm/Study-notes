---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Limits in Set and in Functor Categories"
  - "Def - Presheaf"
  - "Def - Preservation, Reflection, and Creation of Limits"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\mathcal{A}$ be a small category and $[\mathcal{A}^{op}, \mathbf{Set}]$ the [[Def - Presheaf|presheaf]] category. Show that limits and colimits in $[\mathcal{A}^{op}, \mathbf{Set}]$ are computed **pointwise** (objectwise): for a diagram $D : J \to [\mathcal{A}^{op}, \mathbf{Set}]$ of presheaves and each $a \in \mathcal{A}$,
$$(\lim_J D)(a) \cong \lim_J\big(D(-)(a)\big), \qquad (\operatorname{colim}_J D)(a) \cong \operatorname{colim}_J\big(D(-)(a)\big).$$
Conclude that every presheaf category is [[Def - Complete and Cocomplete Category|complete and cocomplete]], and verify with an example: the limit of two presheaves over a third is the presheaf of pointwise pullbacks.

**Recall:**

![[Thm - Limits in Set and in Functor Categories#Statement]]

A **presheaf** on $\mathcal{A}$ is a functor $F : \mathcal{A}^{op} \to \mathbf{Set}$; a morphism of presheaves is a natural transformation. The **evaluation functor** $\mathrm{ev}_a : [\mathcal{A}^{op}, \mathbf{Set}] \to \mathbf{Set}$ sends $F \mapsto F(a)$.

---

# Convergent Strategy

**Problem class:** This is a "compute (co)limits in a functor category" problem — applying the pointwise principle to presheaves. The routine: build the candidate (co)limit objectwise using $\mathbf{Set}$'s (co)limits, make it a functor, and verify its universal property reduces to the pointwise ones.

**Assumption pattern:** The structural facts are that $\mathbf{Set}$ is [[Def - Complete and Cocomplete Category|complete and cocomplete]] and that $[\mathcal{A}^{op}, \mathbf{Set}]$ is a functor category. The unlocking principle is [[Thm - Limits in Set and in Functor Categories|"limits in functor categories are pointwise"]]: since the target $\mathbf{Set}$ has all (co)limits, so does the presheaf category, computed objectwise.

**Theorem routing:** The route: each evaluation $\mathrm{ev}_a$ [[Def - Preservation, Reflection, and Creation of Limits|creates]] (co)limits, the family $(\mathrm{ev}_a)_a$ jointly creating them; so a (co)limit of presheaves exists iff all the pointwise (co)limits in $\mathbf{Set}$ exist (they do, $\mathbf{Set}$ being bicomplete), and is their assembly into a functor. The functoriality and naturality are forced by uniqueness of induced maps in $\mathbf{Set}$.

**Key decision point:** The subtle step is checking that the objectwise assignment $a \mapsto \lim_J D(-)(a)$ actually *is a functor* on $\mathcal{A}^{op}$ — that it acts coherently on morphisms of $\mathcal{A}$ — and that the limit cone is *natural*. This is where uniqueness of the induced maps between pointwise limits does the work; skipping it leaves the candidate as a mere object-assignment, not a presheaf.

---

# Legal Operations Used

1. **Apply the pointwise-limit theorem (from the topic page: [[Thm - Limits in Set and in Functor Categories]]).** Since $\mathbf{Set}$ is bicomplete, build the presheaf (co)limit objectwise.

2. **Assemble objectwise data into a functor (operation: induced maps between pointwise limits).** Define the (co)limit presheaf on morphisms of $\mathcal{A}$ via the universal property, using uniqueness for functoriality.

3. **Use evaluation functors create (co)limits (operation: $\mathrm{ev}_a$ creates).** Conclude existence and the universal property pointwise, hence completeness and cocompleteness of $[\mathcal{A}^{op}, \mathbf{Set}]$.

---

# Hints

> [!note]- Hint 1
> A presheaf is a functor, and limits in a functor category $[\mathcal{A}^{op}, \mathcal{D}]$ are computed pointwise whenever $\mathcal{D}$ has them. Here $\mathcal{D} = \mathbf{Set}$, which has all small (co)limits.

> [!note]- Hint 2
> Define the candidate limit presheaf $L$ by $L(a) = \lim_J D(-)(a)$ in $\mathbf{Set}$. The work is making $L$ a functor on $\mathcal{A}^{op}$: for $\alpha : a' \to a$ in $\mathcal{A}$, the maps $D_j(\alpha)$ induce a unique $L(\alpha)$ between pointwise limits.

> [!note]- Hint 3
> A natural transformation into $L$ is a family of components, each natural; each component factors through the pointwise limit, and the factorisations are automatically natural by uniqueness. That gives the universal property.

> [!note]- Hint 4
> For the example: the pullback of two presheaves $F \to H \leftarrow G$ is the presheaf $a \mapsto F(a) \times_{H(a)} G(a)$, the pointwise pullback of sets.

---

# Solution

The plan: define the candidate (co)limit presheaf objectwise via $\mathbf{Set}$'s (co)limits, promote it to a functor using uniqueness of induced maps, verify the universal property reduces pointwise, and conclude bicompleteness with the pullback example.

**Step 1: Define the candidate limit presheaf objectwise.**

> [!note]- Derivation
> Let $D : J \to [\mathcal{A}^{op}, \mathbf{Set}]$, so each $D_j$ is a presheaf and $D_j(a) \in \mathbf{Set}$. Since $\mathbf{Set}$ is complete, define $L(a) = \lim_J D(-)(a)$ for each $a \in \mathcal{A}$, the limit of the diagram $j \mapsto D_j(a)$ in $\mathbf{Set}$ — the set of compatible families $(x_j) \in \prod_j D_j(a)$ with $D(f)_a(x_j) = x_k$. The pointwise projections are $\pi^a_j : L(a) \to D_j(a)$.

**Step 2: Promote $L$ to a presheaf (functoriality).**

> [!note]- Derivation
> For $\alpha : a' \to a$ in $\mathcal{A}$ (a morphism of $\mathcal{A}^{op}$ from $a$ to $a'$), each presheaf gives $D_j(\alpha) : D_j(a) \to D_j(a')$, and these form a morphism of $J$-diagrams $D(-)(a) \to D(-)(a')$ in $\mathbf{Set}$. By the universal property of $L(a') = \lim_J D(-)(a')$, there is a unique $L(\alpha) : L(a) \to L(a')$ commuting with the projections. Uniqueness gives $L(\alpha\beta) = L(\beta)L(\alpha)$ and $L(1_a) = 1_{L(a)}$, so $L : \mathcal{A}^{op} \to \mathbf{Set}$ is a presheaf, and the projections $\pi_j = (\pi^a_j)_a$ are natural transformations $L \Rightarrow D_j$.

**Step 3: Verify the universal property reduces pointwise.**

> [!note]- Derivation
> Let $(\mu_j : G \Rightarrow D_j)$ be a [[Def - Cone and Cocone|cone]] over $D$ in $[\mathcal{A}^{op}, \mathbf{Set}]$. At each $a$, $(\mu_{j,a} : G(a) \to D_j(a))$ is a cone over $D(-)(a)$ in $\mathbf{Set}$, inducing a unique $u_a : G(a) \to L(a)$ with $\pi^a_j u_a = \mu_{j,a}$. Naturality of $u = (u_a)$ follows from uniqueness of the pointwise induced maps (both $u_{a'} \circ G(\alpha)$ and $L(\alpha) \circ u_a$ are induced maps with the same projections). So $u : G \Rightarrow L$ is the unique cone morphism, and $L = \lim_J D$ — computed pointwise. By the dual argument with $\mathbf{Set}$'s colimits, $(\operatorname{colim}_J D)(a) = \operatorname{colim}_J D(-)(a)$.

**Step 4: Bicompleteness and the pullback example.**

> [!note]- Derivation
> Because $\mathbf{Set}$ is [[Def - Complete and Cocomplete Category|complete and cocomplete]], every pointwise (co)limit exists, so every (co)limit of presheaves exists: $[\mathcal{A}^{op}, \mathbf{Set}]$ is bicomplete, with each [[Def - Preservation, Reflection, and Creation of Limits|$\mathrm{ev}_a$ creating]] (co)limits. Example: for presheaf morphisms $F \to H \leftarrow G$, the [[Def - Pullback and Pushout|pullback]] is the presheaf $(F \times_H G)(a) = F(a) \times_{H(a)} G(a)$, the pointwise pullback of sets, with the evident restriction maps; a morphism into it is a pair of presheaf morphisms agreeing in $H$, checked objectwise.

> [!note]- Complete formal solution
> Let $D : J \to [\mathcal{A}^{op}, \mathbf{Set}]$. Define $L(a) = \lim_J D(-)(a)$ in $\mathbf{Set}$ (the compatible families), with projections $\pi^a_j$. For $\alpha : a' \to a$ in $\mathcal{A}$, the maps $D_j(\alpha)$ form a morphism of $J$-diagrams, inducing a unique $L(\alpha) : L(a) \to L(a')$; uniqueness makes $L$ a presheaf and the $\pi_j$ natural. Given a cone $(\mu_j : G \Rightarrow D_j)$, each $a$ yields a unique $u_a : G(a) \to L(a)$ with $\pi^a_j u_a = \mu_{j,a}$, and $u = (u_a)$ is natural by uniqueness, so $L = \lim_J D$ pointwise. Dually colimits are pointwise. Since $\mathbf{Set}$ is bicomplete, all pointwise (co)limits exist, so $[\mathcal{A}^{op}, \mathbf{Set}]$ is [[Def - Complete and Cocomplete Category|complete and cocomplete]], each [[Def - Preservation, Reflection, and Creation of Limits|$\mathrm{ev}_a$ creating]] them. Example: $(F \times_H G)(a) = F(a) \times_{H(a)} G(a)$. $\blacksquare$

---

# Key Takeaways

**Limits in a functor category are computed one object at a time — the pointwise principle makes presheaf categories trivially bicomplete.** The reusable method is that to take a (co)limit of presheaves you compute it separately at each object $a$ in $\mathbf{Set}$, then assemble; because $\mathbf{Set}$ is [[Def - Complete and Cocomplete Category|bicomplete]], the presheaf category inherits all (co)limits with no extra work. This is why presheaf categories — graphs, simplicial sets, $G$-sets, quivers, sheaves-before-sheafification — are uniformly complete and cocomplete, and why their (co)limits are "obvious": just do it objectwise. The trigger: any time you face a category of functors into a bicomplete target, compute (co)limits pointwise and stop worrying about existence.

**Functoriality and naturality of the pointwise limit are forced by uniqueness, not assumed.** The non-obvious labour in the proof is promoting the object-assignment $a \mapsto \lim D(-)(a)$ to an honest functor and checking the limit cone is natural — and this is where uniqueness of induced maps between pointwise limits is indispensable. The transferable insight is that whenever you assemble objectwise data into a functor, the universal property supplies the action on morphisms uniquely, and uniqueness then *forces* functoriality (composition, identities) and naturality for free. This "uniqueness ⇒ coherence" pattern is the same mechanism that makes $\lim$ itself a functor and that proves [[Thm - Limits are Unique up to Unique Isomorphism|limits unique up to unique isomorphism]].

**Limits of sheaves are pointwise, but colimits are not — the asymmetry to remember.** Although this exercise establishes that both limits and colimits of *presheaves* are pointwise, the important downstream caveat is that for *sheaves* (presheaves satisfying a gluing condition), limits remain pointwise but colimits require **sheafification** — the pointwise colimit of sheaves need not be a sheaf. The diagnostic to carry forward is that the inclusion of sheaves into presheaves is a [[Def - Preservation, Reflection, and Creation of Limits|right adjoint]] (it preserves limits, so sheaf limits agree with presheaf limits computed pointwise) but the left adjoint sheafification is what repairs colimits. This is the categorical reason cohomology — the derived functor of the pointwise-computed global-sections limit — is subtle, and it is the entry point to **topos theory** and the functor-of-points construction of [[Ex - Fibre products of schemes are pullbacks|schemes]], where the pointwise computation of fibre products is exactly this principle applied to functors $\mathbf{CRing} \to \mathbf{Set}$.
