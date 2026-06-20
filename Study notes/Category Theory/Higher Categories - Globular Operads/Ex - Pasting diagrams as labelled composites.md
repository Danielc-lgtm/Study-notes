---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - The Free Strict ω-Category Monad"
  - "Def - Pullback and Pushout"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $T$ be the [[Def - The Free Strict ω-Category Monad|free strict ω-category monad]] on **globular sets** and let $X$ be a globular set.

(a) Show that an element of $(TX)(m)$ is the data of a pasting diagram $\pi \in \mathrm{pd}(m) = (T1)(m)$ together with a *labelling* of the constituent cells of $\pi$ by cells of $X$ of matching dimension.

(b) Identify the map $TX \to T1$ (induced by the unique map $X \to 1$) as the "forget the labels, keep the shape" projection.

(c) Use cartesianness of $T$ to show that the fibre of $TX \to T1$ over a fixed pasting diagram $\pi$ is exactly the set of labellings of $\pi$ by $X$, and explain why this is the structural fact that the definition of a [[Def - Globular Operad|globular operad]] exploits.

**Recall:**

The **free strict $\omega$-category monad** $T$ sends a globular set $X$ to the strict $\omega$-category $TX$ of all formal composites of the cells of $X$. On the terminal globular set $1$ it yields the **pasting diagrams** $T1 = \mathrm{pd}$, recursively $\mathrm{pd}(0) = 1$, $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$. The monad is **cartesian**: $T$ preserves [[Def - Pullback and Pushout|pullbacks]] and the naturality squares of $\eta, \mu$ are pullbacks. For a globular set $X$ there is a unique map $! : X \to 1$, inducing $T! : TX \to T1$. The **fibre** of a map $f : A \to B$ over $b \in B$ is $f^{-1}(b)$; categorically it is the pullback of $f$ along $\{b\} \to B$.

---

# Convergent Strategy

**Problem class:** This bridges the *computation* class (making $T$ concrete, as in [[Ex - Computing the low-dimensional pasting diagrams]]) and the *cartesianness* class from the topic page's problem-solving strategy. The goal is to extract, from the abstract monad, the concrete picture "an element of $TX$ is a labelled pasting diagram" and to see that cartesianness is exactly what makes "labelling of a fixed shape" a well-defined fibre.

**Assumption pattern:** Two assumptions drive the solution. First, the meaning of $T$ as "free strict $\omega$-category" — $TX$ is formal composites of $X$'s cells, and a formal composite is a *shape* (which cells, in what arrangement) plus a *filling* (which cells of $X$). Second, **cartesianness**: the naturality square of the unit, or equivalently $T$ preserving the pullback that defines a fibre, is what guarantees the fibre is literally the labellings. Recognizing "fibre $=$ pullback along a point, and $T$ preserves it" is the unlock.

**Theorem routing:** Route (a) and (b) through the definition of $T$ and the recursion of [[Def - The Free Strict ω-Category Monad|the free strict ω-category monad]]. Route (c) through cartesianness: the fibre of $TX \to T1$ over $\pi$ is the pullback of $T(X \to 1)$ along $\{\pi\} \hookrightarrow T1$, and since $T$ preserves pullbacks this fibre is computed by $T$ applied to the corresponding pullback downstairs — yielding exactly the labellings.

**Key decision point:** The non-obvious choice is to read "fibre over $\pi$" as a *pullback* and then invoke cartesianness, rather than arguing set-theoretically that the labels are independent of the shape. The tempting alternative — just asserting "obviously a labelled diagram restricts to a shape" — misses *why* the fibres are well-behaved enough to define operad composition; only the pullback/cartesian reading shows the fibres glue correctly under substitution.

---

# Legal Operations Used

1. **Operation 2 from the topic page (use cartesianness to form the fibres).** This is the exercise where that operation is justified in its primary form: the fibres $P(\pi)$ that all later operad theory uses are, for $P = TX$, exactly the labellings, and cartesianness is what makes this hold.

2. **Operation 1 from the topic page (encode structure as operations over $T1$).** We see the prototype: $TX$ is a collection over $T1$ whose fibres are labellings, the template every globular operad refines.

---

# Hints

> [!note]- Hint 1
> Think about what a "formal composite" of cells of $X$ is. It must record *which* cells were composed and *how* they were arranged. The "how" is a pasting diagram; the "which" is an assignment of an $X$-cell to each slot of the diagram.

> [!note]- Hint 2
> Compare with the labelled version of the recursion: an element of $(TX)(m+1)$ should be a finite sequence of elements of $(TX)(m)$ whose endpoints match, mirroring $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$ but now carrying $X$-labels. The projection to $T1$ drops the labels at every level.

> [!note]- Hint 3
> For (c), the fibre of $TX \to T1$ over $\pi$ is the pullback of $TX \to T1$ along the inclusion $\{\pi\} \hookrightarrow T1$. Write $\{\pi\}$ as the image of a map from the terminal globular set picking out $\pi$, and use that $T$ *preserves* this pullback.

> [!note]- Hint 4
> The naturality square of the unit (or the pullback defining the fibre) being a pullback says: the labellings of $\pi$ are computed by pulling back $X \to 1$ along the shape $\pi$ — i.e., a labelling is exactly a compatible assignment of $X$-cells to the cells of $\pi$, with no extra constraints and no missing data. That "no extra, no missing" is the pullback condition, hence cartesianness.

---

# Solution

The solution unwinds $TX$ as labelled pasting diagrams (Step 1), identifies the projection (Step 2), and computes the fibre via cartesianness (Step 3), closing with why this powers the operad definition. The pivot is reading the fibre as a pullback and invoking that $T$ preserves it.

**Step 1: an element of $(TX)(m)$ is a labelled pasting diagram.**

> [!note]- Derivation
> $TX$ is the free strict $\omega$-category on $X$: its $m$-cells are the formal $m$-fold composites built from cells of $X$. Such a composite is determined by two pieces of data. The *shape* records the combinatorial arrangement — how many cells, pasted along which boundaries — and is exactly an element $\pi \in \mathrm{pd}(m) = (T1)(m)$, since applying $T$ to the one-cell-per-dimension globular set $1$ keeps only the shape. The *labelling* records which cell of $X$ occupies each slot of $\pi$: for every constituent cell of $\pi$ of dimension $k$, a cell of $X$ of dimension $k$, with the source/target of the chosen $X$-cells matching the way the slots of $\pi$ are glued. Mirroring the recursion, an element of $(TX)(m+1)$ is a finite endpoint-matching sequence of elements of $(TX)(m)$ — the labelled analogue of $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$. So $(TX)(m) = \{(\pi, \text{labelling of } \pi \text{ by } X)\}$.

**Step 2: the projection forgets the labels.**

> [!note]- Derivation
> The unique map $! : X \to 1$ induces $T! : TX \to T1 = \mathrm{pd}$. On an element $(\pi, \lambda)$ of $(TX)(m)$ — a shape $\pi$ with labelling $\lambda$ — the map $T!$ replaces every $X$-label by the unique cell of $1$ of the same dimension, which discards the labelling entirely and returns the bare shape:
> $$
> (T!)(\pi, \lambda) = \pi.
> $$
> So $T! : TX \to T1$ is precisely "forget the labels, keep the shape". This realises $TX$ as a **collection** over $T1$ in the sense of the topic page.

**Step 3: cartesianness makes the fibre the labellings.**

> [!note]- Derivation
> Fix $\pi \in \mathrm{pd}(m)$ and consider the fibre $(T!)^{-1}(\pi) \subseteq (TX)(m)$. Categorically the fibre is the pullback of $T! : TX \to T1$ along the inclusion $\{\pi\} \hookrightarrow T1$ (the map from the terminal globular set selecting $\pi$):
> $$
> \begin{array}{ccc}
> (T!)^{-1}(\pi) & \longrightarrow & TX\\
> \downarrow & & \big\downarrow{\scriptstyle T!}\\
> \{\pi\} & \hookrightarrow & T1.
> \end{array}
> $$
> Now use that $T$ is **cartesian**. The inclusion $\{\pi\} \hookrightarrow T1$ exhibits $\pi$ as (the image of) a chosen element, and the relevant naturality/pullback square for $T$ applied to $X \to 1$ is a pullback. Tracing it through, the fibre is computed as the set of *all* compatible assignments of cells of $X$ to the slots of $\pi$ — no constraint beyond matching the gluing of $\pi$, and none missing. That is exactly the set of labellings of $\pi$ by $X$:
> $$
> (T!)^{-1}(\pi) \;\cong\; \{\text{labellings of } \pi \text{ by cells of } X\}.
> $$
> Without cartesianness, this pullback could fail to be preserved by $T$, and the "fibre" might not coincide with the labellings — there could be spurious or missing elements, and "operations of shape $\pi$" would be ill-defined.
>
> *Why this powers the globular-operad definition.* A [[Def - Globular Operad|globular operad]] is a collection $P \xrightarrow{d} T1$ with $d$ cartesian; its fibre $P(\pi)$ is "the operations of shape $\pi$", and operadic composition substitutes operations into the slots of $\pi$. The whole notion of "substitute an operation into a slot" relies on the slots of $\pi$ being well-defined and the fibres composing correctly — which is exactly what cartesianness guarantees, as this computation for $P = TX$ shows in the prototype case. The labellings-as-fibre picture is the template: a general globular operad replaces "labellings" by an abstract set of operations, but the cartesian fibre structure is identical.

> [!note]- Complete formal solution
> *(a)* $TX$ is the free strict $\omega$-category on $X$; an $m$-cell is a formal $m$-fold composite, determined by a shape $\pi \in \mathrm{pd}(m) = (T1)(m)$ and a labelling assigning to each constituent $k$-cell slot of $\pi$ a $k$-cell of $X$, with source/target matching the gluing of $\pi$. (Equivalently, by the labelled recursion $(TX)(m+1) =$ endpoint-matching sequences of elements of $(TX)(m)$.)
>
> *(b)* The unique $! : X \to 1$ induces $T! : TX \to T1$; on $(\pi, \lambda)$ it sends every $X$-label to the unique same-dimension cell of $1$, giving $(T!)(\pi, \lambda) = \pi$ — the forget-labels projection, exhibiting $TX$ as a collection over $T1$.
>
> *(c)* The fibre $(T!)^{-1}(\pi)$ is the pullback of $T!$ along $\{\pi\} \hookrightarrow T1$. Since $T$ is cartesian (preserves pullbacks; cartesian unit/multiplication), $T$ preserves this pullback, computing the fibre as the set of all compatible $X$-labellings of $\pi$ — exactly the labellings, with nothing extra or missing. This is the structural fact a globular operad $P \xrightarrow{d} T1$ generalizes: $d$ cartesian makes the fibres $P(\pi)$ ("operations of shape $\pi$") well-defined and composable by substitution into the slots of $\pi$. $\blacksquare$

---

# Key Takeaways

**Every element of a free higher structure splits into shape plus filling.** The reusable principle is the clean separation $(TX)(m) = \{(\text{shape } \pi,\ \text{labelling by } X)\}$: a formal composite is a combinatorial arrangement together with an assignment of generators to its slots. This shape-versus-filling decomposition is what makes the projection $TX \to T1$ exist and what makes "operations of a fixed shape" meaningful. The trigger for using it: whenever you meet a free-algebra construction over a presheaf category, look for the projection to the free structure on the terminal object — it stratifies your structure by shape, and each fibre is the fillings of that shape. This is the same decomposition that, for simplicial sets, splits a simplex into its degeneracy-shape and its labelling, and for trees splits a tree into its planar shape and its decorations.

**A fibre is a pullback, and cartesianness is the guarantee the fibre is what you think.** The technical heart is reading $(T!)^{-1}(\pi)$ as a pullback of $T!$ along a point and invoking that $T$ preserves it. This converts a set-theoretic "obviously the labels don't depend on the shape" into a structural fact that *also* tells you the fibres compose correctly under substitution — which the naive argument never delivers. The diagnostic: whenever you want "operations of shape $\pi$" to be well-defined *and* to support composition, check that the shape map is cartesian; cartesianness is precisely the condition that the fibres behave like genuine fibres of a bundle, pulling back and gluing as expected. This is why the topic page's first illegal-but-tempting operation (defining an operad from a non-cartesian map) fails — the fibres would not compose.

**The labellings-as-fibre picture is the prototype every globular operad imitates.** Having seen that $TX$'s fibre over $\pi$ is the labellings of $\pi$ by $X$, the leap to a general globular operad is small: replace "labellings of $\pi$ by $X$" with "an abstract set $P(\pi)$ of operations of shape $\pi$", keeping the cartesian fibre structure. The terminal operad shrinks each fibre to one point (the strict case); a contractible operad enlarges them to house coherence cells (the weak case). Holding this prototype in mind makes the abstract operad definition concrete: $P(\pi)$ is "the menu of ways to compose a diagram of shape $\pi$", and an algebra performs the menu, exactly as $TX$'s labellings are "the diagrams of shape $\pi$" that a strict $\omega$-category composes. See [[Ex - Algebras for the terminal globular operad are strict omega-categories]] for the algebra side and [[Ex - The substitution product and why cartesianness is needed]] for the composition side.
