---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
tags: [category-theory, foundations]
---

# Notation

A diagram lives in a [[Def - Category|category]] $\mathcal{C}$, with objects $A, B, C, D$ and morphisms $f, g, h, k$. A directed path is a composable string of arrows; its composite is the morphism obtained by composing them in order with $\circ$ (right-to-left). We say a diagram **commutes** when stated below. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

Almost every statement in category theory is an equation between composites of morphisms — $g \circ f = k \circ h$, and so on. Written as a list of such equations, even a modest argument becomes unreadable. The fix is to draw the morphisms as labelled arrows between their objects and assert that **any two directed paths with the same start and end compose to the same morphism**. The picture is the bookkeeping device; "commutes" is the assertion that the bookkeeping is consistent.

The motivation, then, is purely linguistic — but the language is load-bearing, and it depends silently on a single axiom of the ambient [[Def - Category|category]]: associativity. When we write a path $A \xrightarrow{f} B \xrightarrow{g} C \xrightarrow{h} D$ and call its composite "the composite along that path", we are assuming $(h \circ g) \circ f = h \circ (g \circ f)$, so that the path names *one* morphism regardless of how we bracket. **Drop associativity and a diagram has no well-defined notion of "the composite along a path"**, so the entire diagrammatic language collapses. This is why associativity is the axiom that makes diagram chasing legal, and why a commutative diagram is, at bottom, the visual form of associativity-plus-equations.

There is a second, deeper way to see what a diagram *is*, and it pays off because it makes "commutes" precise without hand-waving about "all paths". A diagram of a given shape is a [[Def - Functor|functor]] out of a small **index category** built from the shape. Commutativity is then the single clean condition that the functor is well-defined on the equations imposed by the shape. This reframing is the reason the notion generalizes effortlessly to cones, limits, and natural transformations, all of which are diagrams of prescribed shape.

---

# The Definition

A **diagram** in a [[Def - Category|category]] $\mathcal{C}$ is a directed graph whose vertices are labelled by objects of $\mathcal{C}$ and whose edges are labelled by morphisms of $\mathcal{C}$, with each edge $A \to B$ labelled by a morphism in $\mathcal{C}(A, B)$.

The diagram **commutes** if, for every pair of vertices $X$ and $Y$ and every pair of directed paths from $X$ to $Y$ in the graph, the two composites (formed by composing the edge-labels along each path) are equal as morphisms in $\mathcal{C}$. A path of length zero at a vertex $A$ composes to $1_A$.

The two most common commuting shapes:

- **Commutative triangle.** Vertices $A, B, C$ with $f : A \to B$, $g : B \to C$, $h : A \to C$. The triangle commutes when $h = g \circ f$.
- **Commutative square.** Vertices $A, B, C, D$ with $f : A \to B$, $g : C \to D$, $h : A \to C$, $k : B \to D$. The square commutes when $k \circ f = g \circ h$ — the two routes $A \to B \to D$ and $A \to C \to D$ agree.

A square is displayed as
$$\begin{array}{ccc} A & \xrightarrow{\;f\;} & B \\ \downarrow{\scriptstyle h} & & \downarrow{\scriptstyle k} \\ C & \xrightarrow{\;g\;} & D \end{array} \qquad k \circ f = g \circ h.$$

---

# Categorical / Structural Definition

The precise formulation: a diagram **of shape $\mathcal{J}$** in $\mathcal{C}$ is a [[Def - Functor|functor]] $D : \mathcal{J} \to \mathcal{C}$, where $\mathcal{J}$ is a small **index category** (often the [[Def - Category|free category]] on a directed graph, possibly with some composites forced equal). The functoriality of $D$ — that it preserves composition and identities — is *exactly* the statement that the diagram commutes on the relations holding in $\mathcal{J}$.

Concretely: take the shape graph, form the free category on it (objects $=$ vertices, morphisms $=$ all directed paths, composition $=$ concatenation), and then impose any equations you want to hold (for a commutative square, impose that the two length-two paths are equal). A functor out of the resulting category $\mathcal{J}$ assigns objects and morphisms of $\mathcal{C}$ to the vertices and edges *and automatically respects the imposed equations*, because a functor sends equal morphisms to equal morphisms. So "$D$ is a functor" packages "the diagram commutes" into a single word. This is why a commutative square is the same thing as a functor out of the "walking commutative square" category, and why limits and cones — which are diagrams of prescribed shape — inherit the language wholesale.

---

# Relate to Other Fields / Compression

A commutative diagram is the categorical analogue of a **conservative vector field** or a **path-independent integral**: the value of a path depends only on its endpoints, not on the route taken. In a commutative diagram, the *composite* of a path depends only on its source and target. This is not a loose analogy — in the [[Def - Groupoid|fundamental groupoid]] of a space, where morphisms are homotopy classes of paths, two paths give the same morphism precisely when they are homotopic, and a square commutes exactly when the boundary loop is null-homotopic. Path-independence is the unifying frame.

**True name:** *route-independence of composites* — the assertion that any two directed routes between two fixed objects yield equal morphisms. The operational reflex is **diagram chasing**: to prove a fresh equation $u = v$, embed both as paths in a diagram all of whose smaller cells are already known to commute, then read off $u = v$ by transporting along commuting cells. Each small commuting cell is a licensed rewrite; the chase is a sequence of rewrites.

---

# Examples / Corollaries

**Composition itself.** The defining property of a composite, $h = g \circ f$, *is* a commutative triangle. Every equation between morphisms can be drawn as a commuting diagram, so the language loses no expressive power.

**Naturality.** A [[Def - Natural Transformation|natural transformation]] $\alpha : F \Rightarrow G$ is precisely the assertion that, for every morphism $f : A \to B$, a certain square commutes:
$$\begin{array}{ccc} FA & \xrightarrow{\;\alpha_A\;} & GA \\ \downarrow{\scriptstyle Ff} & & \downarrow{\scriptstyle Gf} \\ FB & \xrightarrow{\;\alpha_B\;} & GB \end{array} \qquad Gf \circ \alpha_A = \alpha_B \circ Ff.$$
The single most-used commutative square in the subject is this **naturality square**.

**A universal property as a triangle.** The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] for [[Def - Group|groups]] is the statement that any homomorphism $\varphi : G \to H$ factors as $G \twoheadrightarrow G/\ker\varphi \xrightarrow{\bar\varphi} H$, a commuting triangle in which the diagonal is $\varphi$, the projection is the quotient map, and $\bar\varphi$ is the induced injection. The triangle commuting is the content "$\varphi = \bar\varphi \circ \pi$".

**Is NOT commutative.** Take $\mathbf{Set}$ with $A = B = \mathbb{Z}$, the maps $f(n) = n + 1$ and $g(n) = 2n$ both $\mathbb{Z} \to \mathbb{Z}$, and form the square with $f$ on top, $g$ on both verticals, $f$ on the bottom. The two routes give $g \circ f(n) = 2(n+1) = 2n + 2$ and $f \circ g(n) = 2n + 1$. They disagree, so the square does **not** commute. The lesson: commutativity is a genuine condition, not a formality — most diagrams one can draw do not commute, and asserting commutativity is asserting an equation that must be proved or imposed.

**Calibration check.** Verify that a triangle $A \xrightarrow{f} B \xrightarrow{g} C$ with hypotenuse $h$ commutes if and only if $h = g \circ f$, and that pasting two commuting squares along a shared edge yields a commuting rectangle (the outer rectangle commutes whenever both inner squares do — the basic move of every diagram chase). Confirm you can explain why associativity of $\mathcal{C}$ is what makes "the composite along a path" unambiguous.

---

# Unlocked by This

> [!tip] Exact Sequences and Diagram Lemmas *(from Homological Algebra)*
> In an **abelian category** the standard diagram lemmas — the five lemma, the snake lemma, the nine lemma — are commutative-diagram statements whose proofs are pure diagram chases. The whole technology of homological algebra is the disciplined manipulation of commuting diagrams of exact sequences.

> [!tip] Cones, Limits, and Universal Properties *(from this subject)*
> A cone over a diagram is a commuting family of arrows from one object to every vertex; a **limit** is the universal such cone. Reframing diagrams as functors out of an index category is exactly what lets [[Def - Limit and Colimit|limits and colimits]] be defined for arbitrary shapes.
