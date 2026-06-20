---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Globular Operad"
  - "Def - The Free Strict ω-Category Monad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $P, Q$ be [[Def - Globular Operad|globular operads]] over the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] $T$, and let $X$ be a globular set with **endomorphism operad** $\mathrm{End}(X)$.

(a) Spell out what a **map of globular operads** $f : P \to Q$ is, and show it is determined by its underlying map of collections (its values on operations) together with the requirement that it commute with operadic composition and units.

(b) Define the endomorphism operad $\mathrm{End}(X)$ and prove that a $P$-**algebra** structure on $X$ is the same thing as a globular-operad map $P \to \mathrm{End}(X)$.

**Recall:**

A [[Def - Globular Operad|globular operad]] is a collection $P \xrightarrow{d} T1$ (with $d$ cartesian) with associative, unital operadic composition $\theta \circ (\phi_x)$ and units $1_\pi$; fibre $P(\pi)$ is the operations of shape $\pi$. A **map of globular operads** $f : P \to Q$ is a map of underlying collections (a map of globular sets over $T1$) preserving composition and units. A $P$-**algebra** is a globular set $X$ with an action assigning, to each shape $\pi$, operation $\theta \in P(\pi)$, and labelling $\lambda$ of $\pi$ by cells of $X$, a composite cell $\theta_X(\lambda) \in X$, compatibly with operadic composition and units. The **endomorphism operad** $\mathrm{End}(X)$ has, as its operations of shape $\pi$, *all* functions sending a labelling of $\pi$ by cells of $X$ to a single cell of $X$ over the correct boundary; its operadic composition is composition of such functions, and its units are the "read off the cell" operations.

---

# Convergent Strategy

**Problem class:** This is a *definitional-unwinding* exercise feeding the *algebra-identification* class of the topic page's problem-solving strategy. Part (a) makes "map of globular operads" concrete; part (b) establishes the workhorse identity "$P$-algebra $=$ map $P \to \mathrm{End}(X)$" that the topic page lists among the most reusable properties.

**Assumption pattern:** The assumption that does the work is that an operad map is a map of *collections* (over $T1$) plus *equations* (preserve composition and units) — so it is determined by where it sends operations, with the equations as constraints, not extra data. For (b), the assumption is that an algebra action is "a composite for each operation+labelling", which is exactly a function into $\mathrm{End}(X)$ at each shape. Recognizing "action $=$ assignment of an actual operation to each abstract operation" is the unlock.

**Theorem routing:** No external theorem; route through the definitions of [[Def - Globular Operad|globular operad]] map and algebra, and through the definition of $\mathrm{End}(X)$. The crux is matching the *compatibility* axioms on both sides: an algebra's compatibility with operadic composition is exactly the map-into-$\mathrm{End}(X)$ preserving composition.

**Key decision point:** The non-obvious choice in (b) is to see the algebra action *not* as a family of separate composite-assignments but as a single assignment $\theta \mapsto (\text{the operation } \theta \text{ performs on } X)$, i.e. a map of collections $P \to \mathrm{End}(X)$; the algebra axioms then *become* the operad-map axioms. The tempting alternative — checking the algebra axioms in isolation — obscures that they are literally the statement "$P \to \mathrm{End}(X)$ is an operad map".

---

# Legal Operations Used

1. **Operation 6 from the topic page (identify an operad's algebras by unwinding the action).** Part (b) is the canonical instance: the action is unwound as a map into the endomorphism operad.

2. **Operation 1 from the topic page (encode structure as operations over $T1$).** Both an operad map and an algebra are seen as maps of collections over $T1$ plus equations, the uniform encoding the chapter relies on.

---

# Hints

> [!note]- Hint 1
> For (a): a map of globular operads is first of all a map of the underlying globular sets that commutes with the maps to $T1$ (a map of collections). The operad-map conditions are then *equations* — preserve composition, preserve units — not additional data.

> [!note]- Hint 2
> For (b): an algebra action assigns to each operation $\theta \in P(\pi)$ and each labelling $\lambda$ a composite $\theta_X(\lambda)$. Fix $\theta$ and let $\lambda$ vary: you get a function "labelling $\mapsto$ composite", which is by definition an element of $\mathrm{End}(X)(\pi)$.

> [!note]- Hint 3
> So the action gives, for each $\theta \in P(\pi)$, an element $\widehat{\theta} \in \mathrm{End}(X)(\pi)$ — i.e. a map of collections $P \to \mathrm{End}(X)$. Now check the algebra axioms are exactly the conditions making this map preserve operadic composition and units.

> [!note]- Hint 4
> Compatibility of the algebra action with operadic composition says: performing a composite operation equals composing the performances. That is precisely "the map $P \to \mathrm{End}(X)$ sends operadic composites to operadic composites" — preservation of composition. Match units similarly.

---

# Solution

The solution unwinds operad maps (Step 1), defines $\mathrm{End}(X)$ and constructs the bijection between algebra structures and operad maps into it (Step 2), and verifies the axioms correspond (Step 3). The pivot is currying the action: fix the operation, vary the labelling, land in $\mathrm{End}(X)$.

**Step 1: an operad map is a collection map preserving composition and units.**

> [!note]- Derivation
> A map of globular operads $f : P \to Q$ is a map of underlying globular sets that commutes with the structure maps $d_P, d_Q$ to $T1$ — i.e. it sends an operation of shape $\pi$ to an operation of shape $\pi$ (a map of *collections*) — and that preserves the operad structure:
> $$
> f(\theta \circ (\phi_x)_x) = f(\theta) \circ (f(\phi_x))_x \quad (\text{preserve composition}), \qquad f(1_\pi) = 1_\pi \quad (\text{preserve units}).
> $$
> Crucially, these are *equations* the collection map must satisfy, not extra structure. So $f$ is fully determined by its underlying collection map (its values $f(\theta)$ on operations); the two equations constrain which collection maps qualify. This is the operadic analogue of "a monoid homomorphism is a function preserving the multiplication and unit".

**Step 2: a $P$-algebra is a map $P \to \mathrm{End}(X)$.**

> [!note]- Derivation
> First, $\mathrm{End}(X)$ is a globular operad: its fibre $\mathrm{End}(X)(\pi)$ is the set of all functions
> $$
> \{\text{labellings of } \pi \text{ by cells of } X\} \longrightarrow X(\dim\pi)
> $$
> sending a labelling to a single cell over the correct boundary; operadic composition is honest composition of such functions (substitute the outputs of inner operations as inputs to an outer one), and the unit $1_\pi$ reads off the appropriate cell. The cartesian structure is inherited from $X$. (This is the largest globular operad acting on $X$ — every actual way of composing $X$-labelled diagrams.)
>
> Now let $X$ be a $P$-algebra, with action $\theta_X(\lambda)$ for $\theta \in P(\pi)$ and labelling $\lambda$. Currying — fixing $\theta$ and letting $\lambda$ vary — gives, for each $\theta \in P(\pi)$, a function
> $$
> \widehat{\theta} : \{\text{labellings of } \pi\} \to X(\dim\pi), \qquad \widehat{\theta}(\lambda) = \theta_X(\lambda),
> $$
> i.e. an element $\widehat{\theta} \in \mathrm{End}(X)(\pi)$. The assignment $\theta \mapsto \widehat{\theta}$ is a map of collections $\widehat{(-)} : P \to \mathrm{End}(X)$ over $T1$ (it preserves shapes). Conversely, any collection map $g : P \to \mathrm{End}(X)$ gives an action $\theta_X(\lambda) := g(\theta)(\lambda)$. These are mutually inverse.

**Step 3: the algebra axioms are the operad-map axioms.**

> [!note]- Derivation
> It remains to check that $\widehat{(-)}$ is a map of *operads* (not just collections) exactly when the action satisfies the algebra axioms. The algebra's **compatibility with operadic composition** states
> $$
> (\theta \circ (\phi_x))_X(\lambda) = \theta_X\big((\phi_x)_X(\lambda|_x)\big),
> $$
> "performing a composite operation equals performing the inner operations then the outer". Curried, the left side is $\widehat{\theta \circ (\phi_x)}(\lambda)$ and the right side is $\big(\widehat\theta \circ (\widehat{\phi_x})\big)(\lambda)$ using composition in $\mathrm{End}(X)$. So compatibility says exactly $\widehat{\theta \circ (\phi_x)} = \widehat\theta \circ (\widehat{\phi_x})$ — preservation of composition. The algebra's **unit axiom** $(1_\pi)_X(\lambda) =$ (the cell read off $\lambda$) says $\widehat{1_\pi} = 1_\pi^{\mathrm{End}(X)}$ — preservation of units. Hence $\widehat{(-)} : P \to \mathrm{End}(X)$ is an operad map iff $X$ is a $P$-algebra, and the correspondence is a bijection
> $$
> \{P\text{-algebra structures on } X\} \;\cong\; \{\text{globular-operad maps } P \to \mathrm{End}(X)\}. \qquad \blacksquare
> $$

> [!note]- Complete formal solution
> *(a)* A map of globular operads $f : P \to Q$ is a map of underlying collections (a globular-set map over $T1$, hence shape-preserving) satisfying $f(\theta\circ(\phi_x)) = f(\theta)\circ(f(\phi_x))$ and $f(1_\pi)=1_\pi$. These are equational constraints, so $f$ is determined by its values on operations.
>
> *(b)* The endomorphism operad $\mathrm{End}(X)$ has $\mathrm{End}(X)(\pi) = \{\text{functions } \{\text{labellings of }\pi\}\to X(\dim\pi) \text{ over the right boundary}\}$, with composition $=$ function composition and units $=$ read-off operations. Given a $P$-algebra $X$, currying the action $\theta_X(\lambda)$ gives $\widehat\theta\in\mathrm{End}(X)(\pi)$ and a collection map $\widehat{(-)}:P\to\mathrm{End}(X)$; conversely a collection map $g$ gives an action $g(\theta)(\lambda)$. The algebra's compatibility with operadic composition is exactly $\widehat{\theta\circ(\phi_x)}=\widehat\theta\circ(\widehat{\phi_x})$ and its unit axiom is exactly $\widehat{1_\pi}=1_\pi$, so $\widehat{(-)}$ is an operad map iff $X$ is a $P$-algebra. Hence $P$-algebra structures on $X$ correspond bijectively to globular-operad maps $P\to\mathrm{End}(X)$. $\blacksquare$

---

# Key Takeaways

**An action is a homomorphism into the endomorphisms — the universal pattern.** The identity "$P$-algebra $=$ map $P \to \mathrm{End}(X)$" is the higher-categorical instance of a pattern that recurs everywhere: a group action is a homomorphism into the symmetric group $\mathrm{Sym}(X)$; a module is a ring homomorphism into the endomorphism ring $\mathrm{End}(X)$; an operad algebra is an operad map into the endomorphism operad. In every case the endomorphism object packages *all possible* actions, and a specific action is a structure-preserving selection from them. The trigger for using this: whenever you must show a structure acts on an object, or compare two actions, route through the endomorphism object — abstract action questions become concrete homomorphism questions. This is precisely the lever in [[Ex - Any contractible globular set is a weak omega-category]], where one builds a contraction into $\mathrm{End}(X)$ and then maps $L$ in.

**Operad maps are collection maps plus equations, so they are cheap to specify and constrain.** Part (a)'s lesson is that to give an operad map you only give its values on operations, and the composition/unit equations then *constrain* (rather than extend) the data. This makes operad maps verifiable: check the two equations. It also makes uniqueness arguments easy — if two operad maps agree on enough generating operations and both preserve composition/units, they agree everywhere. This is exactly the structure exploited in proving initiality of $L$ (see [[Thm - The Initial Contractible Globular Operad Exists]]): the unique map out of $L$ is forced on generators by "preserve contraction" and on composites by "preserve composition", with no freedom left.

**Currying turns a two-variable action into a one-variable map of operads.** The technical move that makes part (b) work is currying: the action $\theta_X(\lambda)$, a function of *two* arguments (operation and labelling), is reorganized into a function of *one* argument (operation) valued in functions-of-labellings, i.e. in $\mathrm{End}(X)$. This currying is what converts the algebra axioms into the operad-map axioms verbatim. The transferable diagnostic: when an action's axioms look like a tangle of compatibility conditions, curry to isolate one argument, and the conditions often collapse into "this is a homomorphism". The same reorganization underlies the adjunction between actions and representations throughout algebra. See [[Ex - Algebras for the terminal globular operad are strict omega-categories]] for the case where this machinery identifies $1$-algebras as strict $\omega$-categories.
