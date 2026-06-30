---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Opposite Category and Duality"
  - "Def - Group"
  - "Def - Category"
tags: [category-theory, foundations]
---

# Problem Statement

Compute the [[Def - Opposite Category and Duality|opposite category]] in two basic cases.

1. **Poset.** Let $(P, \leq)$ be a partially ordered set, viewed as a [[Def - Category|category]] $P$ with a unique arrow $a \to b$ exactly when $a \leq b$. Show that $P^{\mathrm{op}}$ is the poset $(P, \geq)$ — the same set with the order reversed. Identify what meets and joins become under this reversal.

2. **Group.** Let $G$ be a [[Def - Group|group]], viewed as the one-object category $\mathbf{B}G$. Show that $(\mathbf{B}G)^{\mathrm{op}} = \mathbf{B}(G^{\mathrm{op}})$, where $G^{\mathrm{op}}$ is the **opposite group** (same set, product $g \ast h := h g$), and prove $G^{\mathrm{op}} \cong G$ via $g \mapsto g^{-1}$.

**Recall:**

![[Def - Opposite Category and Duality#The Definition]]

A poset becomes a category with at most one arrow per ordered pair; a [[Def - Group|group]] $G$ becomes a one-object category $\mathbf{B}G$ with morphisms the group elements and composition the product.

---

# Convergent Strategy

**Problem class:** This is a "compute a construction on small examples" exercise — instantiating $(-)^{\mathrm{op}}$ on the two degenerate kinds of category (preorders and one-object categories) to see what arrow-reversal means concretely.

**Assumption pattern:** In a poset there is at most one arrow per pair, so reversing arrows just reverses the order relation. In a group every arrow is invertible, so the opposite group is isomorphic to the original via inversion — the extra structure (invertibility) is exactly what makes $G^{\mathrm{op}} \cong G$.

**Theorem routing:** Direct from the definition of $\mathcal{C}^{\mathrm{op}}$. For the group case, the isomorphism $g \mapsto g^{-1}$ is verified by checking it is a group homomorphism $G \to G^{\mathrm{op}}$, using $(gh)^{-1} = h^{-1}g^{-1}$.

**Key decision point:** The instructive contrast is that posets are generally *not* self-opposite (reversing the order genuinely changes the poset, unless it is symmetric), while groups *are* always self-opposite. The reason is invertibility: a group has the anti-automorphism $g \mapsto g^{-1}$, a poset has no analogous order-reversing self-map in general.

---

# Legal Operations Used

1. **Operation: instantiate $(-)^{\mathrm{op}}$ on a concrete category** (topic page, Legal Operation 8). We apply the opposite construction to a poset and to $\mathbf{B}G$.

2. **Operation: exhibit an isomorphism by a formula and check it is a homomorphism** (topic page, Legal Operation 4). For groups, $g \mapsto g^{-1}$ is checked to be a homomorphism $G \to G^{\mathrm{op}}$.

---

# Hints

> [!note]- Hint 1
> In a poset category, reversing the arrow $a \to b$ (which encodes $a \leq b$) gives an arrow $b \to a$. What order relation does an arrow $b \to a$ encode in $P^{\mathrm{op}}$?

> [!note]- Hint 2
> For the group, composition in $(\mathbf{B}G)^{\mathrm{op}}$ is reversed: the composite of $g$ then $h$ becomes $h$ then $g$ in $\mathcal{C}$, i.e. the product $hg$. That is the opposite group law.

> [!note]- Hint 3
> Check $\phi(g) = g^{-1}$ is a homomorphism $G \to G^{\mathrm{op}}$: compute $\phi(gh)$ and compare with $\phi(g) \ast \phi(h)$ where $\ast$ is the opposite product.

---

# Solution

The plan: read off $P^{\mathrm{op}}$ from the definition (reversing the unique arrows reverses the order), then compute $(\mathbf{B}G)^{\mathrm{op}}$ (reversing composition gives the opposite product) and exhibit the inversion isomorphism.

**Step 1: The opposite of a poset is the reversed poset.**

> [!note]- Derivation
> In $P$, there is an arrow $a \to b$ iff $a \leq b$. By definition $P^{\mathrm{op}}(a, b) = P(b, a)$, so there is an arrow $a \to b$ in $P^{\mathrm{op}}$ iff there is an arrow $b \to a$ in $P$, iff $b \leq a$, iff $a \geq b$. So $P^{\mathrm{op}}$ is exactly the poset $(P, \geq)$: the same underlying set with the order reversed. Composition is automatically associative (at most one arrow per pair), and identities correspond to $a \geq a$, so $P^{\mathrm{op}}$ is a legitimate poset category.
>
> Under this reversal, a **meet** (greatest lower bound, the categorical [[Def - Product and Coproduct|product]]) in $P$ becomes a **join** (least upper bound, the coproduct) in $P^{\mathrm{op}}$, and vice versa. The infimum/supremum duality is opposite-category duality: $\inf$ in $P$ is $\sup$ in $P^{\mathrm{op}}$.

**Step 2: The opposite of $\mathbf{B}G$ is $\mathbf{B}(G^{\mathrm{op}})$.**

> [!note]- Derivation
> $\mathbf{B}G$ has one object $\ast$, morphisms $G$, composition $g \circ f = gf$ (group product), identity $e$. Its opposite $(\mathbf{B}G)^{\mathrm{op}}$ has the same one object, the same morphism set $G$, but reversed composition: $g \circ^{\mathrm{op}} f = f \circ g = fg$. Writing $g \ast f := fg$ for this reversed product, $(\mathbf{B}G)^{\mathrm{op}}$ is the one-object category of the set $G$ under $\ast$. The operation $\ast$ is associative (inherited) with identity $e$ and inverses (the inverse of $g$ under $\ast$ is still $g^{-1}$, since $g^{-1} \ast g = g g^{-1} = e$), so $(G, \ast)$ is a group — the **opposite group** $G^{\mathrm{op}}$ — and $(\mathbf{B}G)^{\mathrm{op}} = \mathbf{B}(G^{\mathrm{op}})$.

**Step 3: $G^{\mathrm{op}} \cong G$ via inversion.**

> [!note]- Derivation
> Define $\phi : G \to G^{\mathrm{op}}$ by $\phi(g) = g^{-1}$. It is a bijection (inversion is its own inverse map). It is a homomorphism:
> $$\phi(gh) = (gh)^{-1} = h^{-1}g^{-1} = g^{-1} \ast h^{-1} = \phi(g) \ast \phi(h),$$
> where the middle equality uses $(gh)^{-1} = h^{-1}g^{-1}$ and the next uses the opposite product $x \ast y = yx$. So $\phi$ is a [[Def - Group|group]] [[Def - Homomorphism|isomorphism]] $G \xrightarrow{\sim} G^{\mathrm{op}}$. Hence every group is isomorphic to its opposite, and $\mathbf{B}G \cong (\mathbf{B}G)^{\mathrm{op}}$ — a one-object category is self-opposite. This is special to groups: the witnessing anti-automorphism $g \mapsto g^{-1}$ exists precisely because every element is invertible.

> [!note]- Complete formal solution
> *Poset:* $P^{\mathrm{op}}(a,b) = P(b,a)$, so an arrow $a \to b$ in $P^{\mathrm{op}}$ means $b \leq a$, i.e. $P^{\mathrm{op}} = (P, \geq)$; meets and joins swap.
>
> *Group:* $(\mathbf{B}G)^{\mathrm{op}}$ has reversed composition $g \ast f = fg$, the opposite group $G^{\mathrm{op}}$. The map $\phi(g) = g^{-1}$ satisfies $\phi(gh) = h^{-1}g^{-1} = \phi(g)\ast\phi(h)$ and is bijective, so $G \cong G^{\mathrm{op}}$. $\blacksquare$

---

# Key Takeaways

**On posets, "opposite" means "turn the order upside down", and this is the source of inf/sup duality.** The reusable observation is that for a poset category, $(-)^{\mathrm{op}}$ literally reverses $\leq$, so any order-theoretic statement has an upside-down dual: greatest becomes least, meet becomes join, infimum becomes supremum, top becomes bottom. This is why lattice theory comes in dual pairs and why a theorem about suprema in one poset is a theorem about infima in its opposite. When you meet a poset duality, picture flipping the Hasse diagram; that flip *is* passing to the opposite category.

**[[Def - Group|Groups]] are self-opposite because inversion is an order-reversing automorphism.** The fact that $G \cong G^{\mathrm{op}}$ for every group is worth holding onto: it says a group "looks the same in the mirror", with $g \mapsto g^{-1}$ providing the looking glass. This is the categorical content of the identity $(gh)^{-1} = h^{-1}g^{-1}$, which is itself the one-object instance of the opposite-category composition law. The trigger: whenever a construction depends on left-versus-right multiplication in a group, you can flip handedness for free using the inversion isomorphism — left [[Def - Module|modules]] over $G$ become right modules, left actions become right actions.

**Self-opposite is rare and informative; most categories are not.** Contrasting the two cases trains the right intuition: groups are self-opposite, generic posets are not, and large categories like $\mathbf{Set}$ are emphatically not. When a category *is* self-opposite (finite-dimensional vector spaces, finite abelian groups under Pontryagin duality, compact and discrete via Gelfand duality), every theorem yields a second theorem *about the same category*, which is a powerful and special situation. Recognizing whether your category admits a self-duality tells you whether duality gives you new facts internally or only relates your category to a different one.
