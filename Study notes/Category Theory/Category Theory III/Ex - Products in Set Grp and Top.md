---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Product and Coproduct"
  - "Def - Direct Product"
  - "Def - Product Topology"
tags: [category-theory, foundations]
---

# Problem Statement

Show that the categorical [[Def - Product and Coproduct|product]] exists in each of $\mathbf{Set}$, $\mathbf{Grp}$, and $\mathbf{Top}$, and identify it concretely: the cartesian product of sets, the [[Def - Direct Product|direct product]] of groups, and the topological product carrying the [[Def - Product Topology|product topology]]. In each case, exhibit the projections and verify the universal property — that a map into the product is exactly a pair of maps into the factors.

**Recall:**

A **product** of $A$ and $B$ in a category $\mathcal{C}$ is an object $A \times B$ with projections $\pi_1 : A \times B \to A$, $\pi_2 : A \times B \to B$ such that for every $X$ and every pair $f : X \to A$, $g : X \to B$ there is a *unique* $\langle f, g \rangle : X \to A \times B$ with $\pi_1 \langle f, g\rangle = f$ and $\pi_2 \langle f, g\rangle = g$.

![[Def - Direct Product#The Definition]]

The [[Def - Product Topology|product topology]] on $X \times Y$ is the coarsest topology making both projections continuous; a basis is $\{U \times V : U \subseteq X, V \subseteq Y \text{ open}\}$.

---

# Convergent Strategy

**Problem class:** This is an "identify the universal object in a concrete category" problem — the most basic recurring task of the chapter, in which a familiar set-level construction is shown to satisfy a universal property and thereby revealed as a categorical limit. The routine is always: write down the candidate object and projections, then check existence and uniqueness of the induced map.

**Assumption pattern:** The only assumption is the ambient category. What changes between $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Top}$ is the *extra structure the induced map must respect*: in $\mathbf{Set}$ none, in $\mathbf{Grp}$ a group homomorphism, in $\mathbf{Top}$ continuity. Recognising that the underlying-set construction is the same and only the structure-check differs is what unlocks all three at once.

**Theorem routing:** The induced map $\langle f, g\rangle(x) = (f(x), g(x))$ is the unique candidate in every case (forced by the projection equations). The verification routes through: in $\mathbf{Grp}$, that componentwise operations make $\langle f, g\rangle$ a homomorphism; in $\mathbf{Top}$, that the [[Def - Product Topology|product topology]]'s defining property *is* the universal property, so continuity of $\langle f, g\rangle$ is equivalent to continuity of its components. The general principle is [[Thm - Representable Functors Preserve Limits|representability]]: $\mathcal{C}(X, A\times B) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B)$.

**Key decision point:** The non-obvious move is in $\mathbf{Top}$: one must recognise that the product topology is *not* an arbitrary choice but is forced by demanding the universal property, so the verification is not "check this topology works" but "the universal property defines this topology". Choosing the wrong topology (e.g. the box topology on an infinite product) breaks universality, which is the lesson.

---

# Legal Operations Used

1. **Verify a universal property (operation: "verify the universal property of a candidate", from the topic page).** In each category, take an arbitrary test object $X$ with maps to the factors and produce the unique induced map; this is the universal-property verification that identifies a limit.

2. **Read maps into a product as pairs of maps (operation: representability of the product).** Use $\mathcal{C}(X, A \times B) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B)$ to reduce each verification to "a structured map to the product is a pair of structured maps".

3. **Inherit structure from the underlying set (operation: forgetful functor creates the product).** Build the product on underlying sets, then equip it with the unique compatible structure (group operation, topology) making the projections morphisms.

---

# Hints

> [!note]- Hint 1
> In all three categories the underlying set of the product is the cartesian product, and the projections are the coordinate maps. Start by writing down the only possible induced map $\langle f, g\rangle$.

> [!note]- Hint 2
> Uniqueness is forced everywhere by the equations $\pi_1 u = f$, $\pi_2 u = g$: they pin down $u(x) = (f(x), g(x))$. The work is showing this $u$ is a morphism (homomorphism / continuous).

> [!note]- Hint 3
> For $\mathbf{Top}$, do not try to prove continuity of $\langle f, g\rangle$ from a chosen topology directly. Instead use that the product topology is *defined* so that $\langle f, g\rangle$ is continuous iff $f$ and $g$ are — that equivalence is the universal property.

---

# Solution

The proof is one template applied three times. In each category the product object is the cartesian product of underlying sets with coordinate projections; the induced map is $\langle f,g\rangle(x) = (f(x),g(x))$, unique by the projection equations; the only category-specific work is checking $\langle f,g\rangle$ is a morphism, which uses componentwise structure ($\mathbf{Grp}$) or the defining property of the product topology ($\mathbf{Top}$).

**Step 1: The product in $\mathbf{Set}$ is the cartesian product.**

> [!note]- Derivation
> Let $A \times B = \{(a,b) : a \in A, b \in B\}$ with $\pi_1(a,b) = a$, $\pi_2(a,b) = b$. Given $f : X \to A$, $g : X \to B$, define $\langle f,g\rangle(x) = (f(x), g(x))$. Then $\pi_1\langle f,g\rangle = f$ and $\pi_2\langle f,g\rangle = g$. For uniqueness, if $u : X \to A \times B$ satisfies $\pi_1 u = f$, $\pi_2 u = g$, then $u(x) = (\pi_1 u(x), \pi_2 u(x)) = (f(x), g(x)) = \langle f,g\rangle(x)$. So $\langle f,g\rangle$ is the unique induced map, and $A\times B$ is the product.

**Step 2: The product in $\mathbf{Grp}$ is the direct product.**

> [!note]- Derivation
> Let $G \times H$ have underlying set the cartesian product, with componentwise operation $(g,h)(g',h') = (gg', hh')$, identity $(e_G, e_H)$, inverse $(g,h)^{-1} = (g^{-1}, h^{-1})$; this is the [[Def - Direct Product|direct product]], a group. The projections $\pi_1, \pi_2$ are homomorphisms since the operation is componentwise. Given homomorphisms $f : X \to G$, $g : X \to H$, the set-level induced map $\langle f,g\rangle(x) = (f(x), g(x))$ is a homomorphism:
> $$\langle f,g\rangle(xy) = (f(xy), g(xy)) = (f(x)f(y), g(x)g(y)) = (f(x),g(x))(f(y),g(y)) = \langle f,g\rangle(x)\langle f,g\rangle(y).$$
> Uniqueness is as in Step 1 (a homomorphism with the right projections is determined coordinatewise). So $G \times H$ is the product in $\mathbf{Grp}$.

**Step 3: The product in $\mathbf{Top}$ is the product topology.**

> [!note]- Derivation
> Let $X \times Y$ carry the [[Def - Product Topology|product topology]], the coarsest topology for which $\pi_1, \pi_2$ are continuous. Given continuous $f : Z \to X$, $g : Z \to Y$, the induced map $\langle f,g\rangle(z) = (f(z), g(z))$ is the unique set-level map with the right projections (Step 1). It is continuous: a subbasic open set of $X \times Y$ is $\pi_1^{-1}(U)$ or $\pi_2^{-1}(V)$, and $\langle f,g\rangle^{-1}(\pi_1^{-1}(U)) = f^{-1}(U)$, $\langle f,g\rangle^{-1}(\pi_2^{-1}(V)) = g^{-1}(V)$, both open since $f, g$ are continuous; preimages of subbasic opens being open suffices for continuity. Conversely, if $\langle f,g\rangle$ is continuous then $f = \pi_1\langle f,g\rangle$ and $g = \pi_2\langle f,g\rangle$ are continuous. So continuity of the induced map is *equivalent* to continuity of the components — which is exactly the universal property — and $X \times Y$ with the product topology is the product in $\mathbf{Top}$.

> [!note]- Complete formal solution
> In each of $\mathbf{Set}, \mathbf{Grp}, \mathbf{Top}$, take the product object to be the cartesian product of underlying sets with coordinate projections $\pi_1, \pi_2$. Given a test object $X$ (resp. $Z$) and morphisms $f, g$ to the two factors, the assignment $\langle f,g\rangle(x) = (f(x), g(x))$ is the unique function satisfying $\pi_1\langle f,g\rangle = f$, $\pi_2\langle f,g\rangle = g$ (any such $u$ has $u(x) = (\pi_1 u(x), \pi_2 u(x)) = (f(x),g(x))$). It remains to check $\langle f,g\rangle$ is a morphism. In $\mathbf{Set}$ there is nothing to check. In $\mathbf{Grp}$, with the componentwise group structure on $G \times H$ (the [[Def - Direct Product|direct product]]), $\langle f,g\rangle(xy) = (f(xy),g(xy)) = (f(x)f(y),g(x)g(y)) = \langle f,g\rangle(x)\langle f,g\rangle(y)$, so it is a homomorphism. In $\mathbf{Top}$, with the [[Def - Product Topology|product topology]] on $X \times Y$, preimages of the subbasic opens $\pi_1^{-1}(U), \pi_2^{-1}(V)$ under $\langle f,g\rangle$ are $f^{-1}(U), g^{-1}(V)$, open by continuity of $f, g$; so $\langle f,g\rangle$ is continuous, and the converse shows the equivalence is the universal property. Hence the product exists and is as claimed in all three categories. By [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness of limits]], each is *the* product up to unique isomorphism. $\blacksquare$

---

# Key Takeaways

**The product is one construction wearing three coats, and only the structure-check differs.** The decisive realisation is that the underlying set, the projections, and the formula for the induced map $\langle f, g\rangle(x) = (f(x), g(x))$ are *identical* across $\mathbf{Set}$, $\mathbf{Grp}$, and $\mathbf{Top}$; the only category-specific labour is verifying that the induced map respects the ambient structure. This is the general shape of "identify the limit in category $\mathcal{C}$" problems: build it on underlying sets, then check the structure comes along for free. Recognising this lets you dispatch products in $\mathbf{Ab}$, $\mathbf{Ring}$, $\mathbf{Mod}_R$, $\mathbf{Vect}_k$ by the same template without rethinking the universal property each time, because the forgetful functor to $\mathbf{Set}$ creates the product in each.

**The product topology is forced, not chosen — this is the reusable lesson.** The trigger to remember is: when a topology (or any structure) is defined to make certain maps continuous, that defining property *is* a universal property, and you should verify constructions through it rather than by manipulating open sets. The product topology is exactly the topology for which "a map into the product is continuous iff its components are", and trying to prove this for a different topology (the box topology on an infinite product) fails — the box topology is too fine, and the diagonal-style induced maps stop being continuous. Whenever you see "the coarsest/finest topology making ... continuous", read "the limit/colimit in $\mathbf{Top}$".

**Uniqueness of the induced map is what makes the product an operation rather than a choice.** In every case the projection equations $\pi_1 u = f$, $\pi_2 u = g$ determine $u$ outright, leaving no freedom. This forced uniqueness is the categorical content that distinguishes the product from a mere object that happens to map to both factors, and it is what [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness of limits]] then promotes to "the product is well-defined up to a unique isomorphism". The transferable diagnostic: whenever you suspect an object is a universal construction, the first thing to confirm is that the comparison map is *unique*, because existence alone (a map into a candidate exists) is satisfied by far too many objects, as the disjoint union shows for the would-be set product. See the companion [[Ex - Coproducts are disjoint unions free products and direct sums]] for how dramatically the dual construction differs between these same categories.
