---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Natural Transformation"
  - "Def - Functor Category"
  - "Def - Functor"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\mathbf{2}$ be the [[Def - Category|walking arrow]] (objects $0, 1$, one non-identity morphism $u : 0 \to 1$). Let $\mathcal{D}$ be any [[Def - Category|category]].

1. Describe explicitly what a [[Def - Functor|functor]] $F : \mathbf{2} \to \mathcal{D}$ is, and what a [[Def - Natural Transformation|natural transformation]] $\alpha : F \Rightarrow G$ between two such functors is. How many components does $\alpha$ have, and how many naturality squares must be checked?

2. More generally, for $\mathcal{C}$ a [[Def - Category|category]] and $\alpha : F \Rightarrow G$ a natural transformation between functors $\mathcal{C} \to \mathcal{D}$, show that **vertical composition** $(\beta \circ \alpha)_A = \beta_A \circ \alpha_A$ is associative and unital, so that $[\mathcal{C}, \mathcal{D}]$ is a category. Show that $\alpha$ is an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]] in $[\mathcal{C}, \mathcal{D}]$ if and only if every component $\alpha_A$ is an isomorphism in $\mathcal{D}$ (i.e. $\alpha$ is a natural isomorphism).

**Recall:**

![[Def - Natural Transformation#The Definition]]

The [[Def - Functor Category|functor category]] $[\mathcal{C}, \mathcal{D}]$ has functors as objects and natural transformations as morphisms, composed componentwise.

---

# Convergent Strategy

**Problem class:** This is a "unwind the definitions on a minimal shape, then prove a structural fact" exercise. The route is to make the abstract notions concrete on $\mathbf{2}$, then verify the functor-category axioms and the componentwise characterization of isomorphisms.

**Assumption pattern:** On $\mathbf{2}$, a functor is just an arrow and a natural transformation is just a commuting square — the smallest nontrivial instance. For the structural part, everything is *componentwise*: composition, identities, and isomorphisms in $[\mathcal{C}, \mathcal{D}]$ are checked one object at a time in $\mathcal{D}$.

**Theorem routing:** No external theorem. Part 1 is unwinding definitions. Part 2's associativity/unit laws are inherited componentwise from $\mathcal{D}$; the isomorphism characterization requires showing that the componentwise inverses *assemble into a natural transformation* (the inverse naturality square).

**Key decision point:** The one genuinely non-obvious step is the forward direction of the isomorphism claim: if $\alpha$ is invertible in $[\mathcal{C}, \mathcal{D}]$ then each $\alpha_A$ is invertible (read off components of the inverse), but the *converse* — componentwise inverses give a natural transformation — needs the inverse naturality square, obtained by inverting the original square.

---

# Legal Operations Used

1. **Operation: unwind a functor/natural transformation on a small shape** (topic page, Legal Operation 7). On $\mathbf{2}$, functor = arrow, natural transformation = commuting square.

2. **Operation: inherit category axioms componentwise** (topic page, Legal Operation 7). Associativity and unit laws of $[\mathcal{C}, \mathcal{D}]$ come from $\mathcal{D}$ object by object.

3. **Operation: invert a naturality square to get the inverse transformation** (topic page, Legal Operation 10). Componentwise inverses are natural because the inverted square commutes.

---

# Hints

> [!note]- Hint 1
> A functor $F : \mathbf{2} \to \mathcal{D}$ assigns objects to $0, 1$ and a morphism to $u : 0 \to 1$ — so $F$ is just the data of a single arrow $Fu : F0 \to F1$ in $\mathcal{D}$.

> [!note]- Hint 2
> A natural transformation $\alpha : F \Rightarrow G$ on $\mathbf{2}$ has components $\alpha_0, \alpha_1$ and one naturality square (for $u$; the two identity morphisms give trivial squares). Two components, one nontrivial square.

> [!note]- Hint 3
> For associativity of vertical composition, evaluate $((\gamma \circ \beta) \circ \alpha)_A$ and $(\gamma \circ (\beta \circ \alpha))_A$ — both equal $\gamma_A \circ \beta_A \circ \alpha_A$ by associativity in $\mathcal{D}$.

> [!note]- Hint 4
> If each $\alpha_A$ is iso, define $\beta_A = (\alpha_A)^{-1}$. To show $\beta$ is natural, take the original naturality square $Gf \circ \alpha_A = \alpha_B \circ Ff$ and pre/post-compose by the inverses to get $Ff \circ \beta_A = \beta_B \circ Gf$.

---

# Solution

The plan: unwind functors and natural transformations on $\mathbf{2}$ (arrow; commuting square with two components), then verify $[\mathcal{C}, \mathcal{D}]$ is a category by componentwise inheritance, and characterize its isomorphisms as the natural isomorphisms by inverting the naturality square.

**Step 1: Functors and natural transformations on $\mathbf{2}$.**

> [!note]- Derivation
> A [[Def - Functor|functor]] $F : \mathbf{2} \to \mathcal{D}$ assigns objects $F0, F1 \in \mathcal{D}$ and a morphism $Fu : F0 \to F1$ to the unique arrow $u : 0 \to 1$ (the identities $1_0, 1_1$ go to $1_{F0}, 1_{F1}$, forced). So $F$ *is* the single arrow $Fu : F0 \to F1$ — functors $\mathbf{2} \to \mathcal{D}$ are exactly arrows of $\mathcal{D}$.
>
> A [[Def - Natural Transformation|natural transformation]] $\alpha : F \Rightarrow G$ has a component for each object of $\mathbf{2}$ — so **two components** $\alpha_0 : F0 \to G0$ and $\alpha_1 : F1 \to G1$ — and a naturality square for each morphism. The two identity morphisms give squares that commute automatically (they reduce to $\alpha_0 = \alpha_0$, $\alpha_1 = \alpha_1$), so there is **one nontrivial naturality square**, for $u$:
> $$Gu \circ \alpha_0 = \alpha_1 \circ Fu.$$
> Thus a natural transformation on $\mathbf{2}$ is exactly a commuting square — which is why $[\mathbf{2}, \mathcal{D}]$ is the arrow category.

**Step 2: $[\mathcal{C}, \mathcal{D}]$ is a category.**

> [!note]- Derivation
> Vertical composition is $(\beta \circ \alpha)_A = \beta_A \circ \alpha_A$. *Well-defined:* the composite $\beta \circ \alpha$ is natural because, for $f : A \to B$, $G$ and $H$ being the source/target, $H f \circ (\beta_A \circ \alpha_A) = (Hf \circ \beta_A)\circ \alpha_A = (\beta_B \circ Gf)\circ\alpha_A = \beta_B \circ(Gf \circ \alpha_A) = \beta_B \circ \alpha_B \circ Ff = (\beta\circ\alpha)_B \circ Ff$, using both naturality squares (this is vertical pasting of two squares). *Associativity:* $((\gamma\circ\beta)\circ\alpha)_A = (\gamma_A \beta_A)\alpha_A = \gamma_A(\beta_A\alpha_A) = (\gamma\circ(\beta\circ\alpha))_A$ by associativity in $\mathcal{D}$. *Identity:* $(1_F)_A := 1_{FA}$ is natural (square reduces to $Ff = Ff$) and is a two-sided unit componentwise. So $[\mathcal{C}, \mathcal{D}]$ is a [[Def - Category|category]].

**Step 3: Isomorphisms in $[\mathcal{C}, \mathcal{D}]$ are natural isomorphisms.**

> [!note]- Derivation
> ($\Rightarrow$) If $\alpha$ has a two-sided inverse $\beta$ in $[\mathcal{C}, \mathcal{D}]$, then $\beta \circ \alpha = 1_F$ and $\alpha \circ \beta = 1_G$ mean, componentwise, $\beta_A \circ \alpha_A = 1_{FA}$ and $\alpha_A \circ \beta_A = 1_{GA}$ — so each $\alpha_A$ is an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]] in $\mathcal{D}$ with inverse $\beta_A$.
>
> ($\Leftarrow$) Suppose each $\alpha_A$ is an iso; set $\beta_A := (\alpha_A)^{-1}$. We must show $\beta = (\beta_A)$ is a natural transformation $G \Rightarrow F$. Start from the naturality square of $\alpha$ for $f : A \to B$: $Gf \circ \alpha_A = \alpha_B \circ Ff$. Pre-compose by $\beta_A = \alpha_A^{-1}$ on the right and post-compose by $\beta_B = \alpha_B^{-1}$ on the left:
> $$\beta_B \circ Gf = \beta_B \circ Gf \circ \alpha_A \circ \beta_A = \beta_B \circ \alpha_B \circ Ff \circ \beta_A = Ff \circ \beta_A,$$
> which is exactly the naturality square for $\beta$. So $\beta$ is natural, and it is the two-sided inverse of $\alpha$ in $[\mathcal{C}, \mathcal{D}]$. Hence $\alpha$ is an isomorphism in the functor category iff every component is an iso — that is, iff $\alpha$ is a [[Def - Natural Transformation|natural isomorphism]].

> [!note]- Complete formal solution
> *On $\mathbf{2}$:* a functor is an arrow $Fu : F0 \to F1$; a natural transformation has two components $\alpha_0, \alpha_1$ and one nontrivial naturality square $Gu \circ \alpha_0 = \alpha_1 \circ Fu$.
>
> *Category:* vertical composition $(\beta\circ\alpha)_A = \beta_A\circ\alpha_A$ is natural (vertical pasting), associative and unital componentwise from $\mathcal{D}$.
>
> *Isomorphisms:* if $\alpha$ is invertible in $[\mathcal{C},\mathcal{D}]$ each $\alpha_A$ is invertible (read components); conversely if each $\alpha_A$ is invertible, $\beta_A = \alpha_A^{-1}$ is natural (invert the square: $\beta_B Gf = Ff \beta_A$), giving the inverse. $\blacksquare$

---

# Key Takeaways

**Everything in a functor category is componentwise — except naturality, which binds the components.** The structural lesson is that composition, identities, and isomorphism-testing in $[\mathcal{C}, \mathcal{D}]$ all happen one object at a time in $\mathcal{D}$, so the functor-category axioms are inherited for free. The single piece of "glue" is the naturality square, which couples the components across the morphisms of $\mathcal{C}$. This split — componentwise data plus naturality glue — is the right mental model for every functor category: representations (componentwise linear maps, glued by equivariance), presheaves (componentwise set maps, glued by compatibility with restriction), chain complexes (componentwise group maps, glued by commuting with differentials).

**A natural isomorphism is exactly a transformation whose components are all invertible.** The practical payoff of Step 3 is a checkable criterion: to prove $\alpha$ is a natural isomorphism, you do *not* construct a global inverse — you simply verify each component $\alpha_A$ is invertible in $\mathcal{D}$, and naturality of the inverse comes free by inverting the square. This is the standard route to natural isomorphisms throughout the subject (the double dual, the unit/counit of an equivalence, the comparison maps of adjunctions): check invertibility pointwise. The trigger "I want a natural iso" should immediately become "check each component is an iso", with the inverse-square argument as the guaranteed follow-through.

**The walking arrow $\mathbf{2}$ is the minimal laboratory for naturality.** Working out functors and natural transformations on $\mathbf{2}$ — arrow and commuting square — is the cleanest way to internalize what the abstract definitions mean, and it pays off because larger diagram shapes are assembled from arrows. Once "functor out of $\mathbf{2}$ = arrow" and "natural transformation on $\mathbf{2}$ = commuting square" are reflexes, the general naturality square reads as "a commuting square for every morphism of the source", and the bookkeeping of components and squares becomes routine. Whenever a naturality computation feels abstract, restrict mentally to a single arrow $u : A \to B$ and draw its square.
