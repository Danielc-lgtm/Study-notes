---
type: definition
subject: model-categories
prereqs:
  - "Def - Commutative Diagram"
  - "Def - Functor"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a category and $i : A \to B$, $p : X \to Y$ are morphisms. We write $\mathrm{id}_A$ for the identity of $A$ and $g \circ f$ for composition. A **commutative square** with $i$ on the left and $p$ on the right is a choice of maps $f : A \to X$ (top) and $g : B \to Y$ (bottom) with $p \circ f = g \circ i$. The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

This is a compound page: it defines three interlocking notions — the **left/right lifting property**, the **retract** of a morphism, and the **retract argument** that links them — because they are the combinatorial engine of model-category theory and none is fully usable without the others.

---

# Axiom Motivation

The whole subject runs on the ability to *construct maps that do not obviously exist*, and the lifting property is the precise condition guaranteeing such a map. Picture the situation: you have an object $B$, you know what a map out of a subobject $A \subseteq B$ should be (call it $f : A \to X$), and you know what the composite map $B \to Y$ should be after projecting along some $p : X \to Y$ (call it $g$). You want to fill in a map $h : B \to X$ that restricts to $f$ and projects to $g$. There is no reason in general for $h$ to exist — the constraints might be incompatible — and the lifting property is exactly the declaration "for *this* pair $(i, p)$, the fill always exists." Homotopies, comparison maps between resolutions, and retractions are all built this way, so the entire constructive content of the axioms is concentrated in lifting.

Why phrase it as a *square* rather than, say, an extension problem? Because the two boundary conditions are genuinely independent: $f$ pins down what $h$ does on $A$, and $g$ pins down where $h$ goes after $p$. An extension problem (extend $f : A \to X$ over $B$) is the special case where $Y = *$ and $p$ is the map to the terminal object; a lifting problem (lift $g : B \to Y$ through $p$) is the special case where $A = \varnothing$. The square unifies extension and lifting into one diagram, which is why a single axiom (MC4) can govern both the construction of homotopies (extension-like) and the construction of sections (lifting-like).

Now for the retract. A retract of $g$ is a map $f$ that "sits inside $g$ and can be projected back out." The desideratum is to have a notion of "$f$ inherits every good property of $g$" that is weak enough to be common but strong enough to transfer membership in the three classes. If you demanded $f = g$ you would inherit everything but almost never apply it; if you demanded only that $f$ map to $g$ you would inherit nothing. The retract — a map *into* $g$ followed by a map *out* whose composite is the identity — is the Goldilocks notion: a class defined by a lifting property is automatically closed under retracts (this is a short diagram chase), so retract-closure is exactly the compatibility a lifting-defined class must have. That is why MC3 demands it.

The retract argument is the bridge that makes the axioms overdetermined. Its desideratum is to upgrade a *lifting* fact into a *membership* fact: if $f$ has a lifting property, you want to conclude $f$ belongs to a class. Without such a bridge, the lifting axiom MC4 and the factorization axiom MC5 would be unrelated, and the closure theorem would be false. The argument supplies the missing link by a single diagram: factor $f$, use the lifting property to produce a section, and read off the retract. If you tried to weaken the hypothesis — say, drop the factorization and keep only the lifting property — the argument has nothing to retract $f$ *onto*, and the conclusion fails. The factorization provides the target of the retraction; the lifting property provides the retraction map. Both are needed, which is precisely why MC4 and MC5 appear together.

---

# The Definition

**Lifting property.** Let $i : A \to B$ and $p : X \to Y$ be morphisms of a category $\mathcal{C}$. We say $i$ has the **left lifting property** with respect to $p$ — equivalently, $p$ has the **right lifting property** with respect to $i$ — if for every commuting square

$$\begin{array}{ccc} A & \xrightarrow{\ f\ } & X \\ \scriptstyle i \downarrow & & \downarrow \scriptstyle p \\ B & \xrightarrow{\ g\ } & Y \end{array} \qquad (p \circ f = g \circ i)$$

there exists a morphism $h : B \to X$ (a **lift**, or **diagonal filler**) with

$$h \circ i = f \qquad \text{and} \qquad p \circ h = g.$$

We abbreviate "left lifting property" as **LLP** and "right lifting property" as **RLP**. The lift $h$ need not be unique.

**Retract of a morphism.** A morphism $f : A \to B$ is a **retract** of a morphism $g : C \to D$ if there is a commutative diagram

$$\begin{array}{ccccc} A & \longrightarrow & C & \longrightarrow & A \\ \scriptstyle f \downarrow & & \downarrow \scriptstyle g & & \downarrow \scriptstyle f \\ B & \longrightarrow & D & \longrightarrow & B \end{array}$$

in which **both horizontal composites are identities** — the top row composes to $\mathrm{id}_A$ and the bottom row to $\mathrm{id}_B$. Equivalently, $f$ is a retract of $g$ as objects of the arrow category $\mathcal{C}^{\to}$ (whose objects are morphisms of $\mathcal{C}$ and whose morphisms are commutative squares): there are arrow-maps $f \to g$ and $g \to f$ composing to $\mathrm{id}_f$.

**The retract argument.** This is a lemma rather than a definition; its statement and proof are on [[Thm - The Retract Argument]]. In words: if $f = p \circ i$ and $f$ has the LLP with respect to $p$, then $f$ is a retract of $i$; dually, if $f = p \circ i$ and $f$ has the RLP with respect to $i$, then $f$ is a retract of $p$.

---

# Categorical / Structural Definition

The lifting relation organizes into an **orthogonality** between classes of maps, written $\mathcal{L} \boxslash \mathcal{R}$ when every $i \in \mathcal{L}$ has the LLP against every $p \in \mathcal{R}$. Given any class $\mathcal{S}$ of maps, one forms two derived classes: $\mathcal{S}^{\boxslash}$, the maps with RLP against every member of $\mathcal{S}$, and ${}^{\boxslash}\mathcal{S}$, the maps with LLP against every member of $\mathcal{S}$. These operations are a **Galois connection** — they reverse inclusions and $\mathcal{S} \subseteq {}^{\boxslash}(\mathcal{S}^{\boxslash})$ — exactly analogous to the annihilator in linear algebra or the closure operators of Galois theory. A **weak factorization system** is a pair $(\mathcal{L}, \mathcal{R})$ with $\mathcal{L} = {}^{\boxslash}\mathcal{R}$, $\mathcal{R} = \mathcal{L}^{\boxslash}$, and every map factoring as $\mathcal{L}$-then-$\mathcal{R}$. In this language a model structure is two weak factorization systems sharing the class $\mathcal{W}$, and [[Thm - Closure Properties of the Model Structure|the closure theorem]] is the statement that the four classes are the fixed points of this Galois connection.

The retract structure has its own categorical home: $f$ is a retract of $g$ precisely when $f$ is a retract of $g$ in the [[Def - Functor|arrow category]] $\mathcal{C}^{\to}$ — that is, $f$ is an idempotent-split summand of $g$ as an object of $\mathcal{C}^{\to}$. The key structural fact, proved by a one-line diagram chase, is that **any class closed under retracts and defined by a one-sided lifting property is automatically saturated** — closed under retracts, pushouts (for the left class), pullbacks (for the right class), and transfinite composition. This saturation is what the small object argument exploits.

---

# Relate to Other Fields / Compression

The lifting property is the homotopy-theoretic descendant of two classical conditions you have already met. In topology, a **fibration** in the Hurewicz sense is a map with the homotopy lifting property against *all* spaces, and a Serre fibration is one with the lifting property against the disks $D^n$ — both are RLP conditions, and the model-category fibrations of $\mathbf{Top}$ are exactly the Serre fibrations. Dually, a **cofibration** in topology has the homotopy *extension* property, which is an LLP condition. So the abstract LLP/RLP language is a distillation of "can lift homotopies" and "can extend homotopies," stripped of the topology.

In homological algebra the same pattern appears as **projectivity and injectivity**: a [[Def - Module|module]] $P$ is projective exactly when $P \to 0$ has the RLP against every surjection (lift maps out of $P$ through epimorphisms), and injective exactly when $0 \to I$ has the LLP against every injection. The cofibrant objects of $\mathbf{Ch}(R)$ being complexes of projectives is this observation upgraded to chain complexes.

**True name:** the LLP is "**every constraint that can be satisfied separately can be satisfied simultaneously**" — given a partial map ($f$ on $A$) and a downstream target ($g$ after $p$), the lift reconciles them. And the retract argument's true name is "**a map that lifts against its own fibration-factor is its own cofibration-factor (up to retract)**" — it is the statement that the lifting property already determines the class.

---

# Examples / Corollaries

**Is an instance — surjections lift against the empty map.** In $\mathbf{Set}$, a map $p : X \to Y$ has the RLP against $\varnothing \to *$ (the map from the empty set to a point) if and only if $p$ is surjective: a square with $\varnothing$ on top is just a point $y \in Y$, and a lift is a preimage. This is the baby case showing RLP encodes "solvability of equations."

**Is an instance — isomorphisms lift against everything.** If $p$ is an isomorphism, it has the RLP against every map $i$: in any square, set $h = p^{-1} \circ g$, and check $h \circ i = p^{-1} \circ g \circ i = p^{-1} \circ p \circ f = f$ and $p \circ h = g$. Dually every isomorphism has the LLP against everything. This is why, in a model category, isomorphisms are simultaneously trivial cofibrations and trivial fibrations.

**Is an instance — the retract argument in $\mathbf{Set}$.** Factor any map $f : A \to B$ of sets as $A \xrightarrow{i} A \sqcup (B \setminus \mathrm{im}\, f) \xrightarrow{p} B$ where $p$ is surjective. If $f$ happens to have the LLP against $p$ (which holds when $f$ is injective), the retract argument exhibits $f$ as a retract of the injection $i$, recovering the fact that injections form the left class of a factorization system on $\mathbf{Set}$.

**Is NOT an instance — a square with no lift.** In $\mathbf{Top}$, take $i : \{0\} \hookrightarrow [0,1]$ and $p : \{0, 1\} \to \{*\}$. The square sending $0 \mapsto 0$ on top and $[0,1] \to *$ on the bottom has *no* lift $[0,1] \to \{0,1\}$ that is continuous and hits $0$ at the basepoint while being defined everywhere, because $[0,1]$ is connected and $\{0,1\}$ is discrete — any continuous map is constant, but the constraint forces it to be $0$, which is fine here; the genuine failure is the square testing path-lifting against a non-fibration, e.g. the inclusion of an endpoint of a non-fibration. The point of a "NOT" example is that lifting is a real restriction: most pairs $(i, p)$ do not have it, which is exactly why declaring which pairs do is informative structure.

**Is NOT an instance — "$f$ maps to $g$" is not "$f$ is a retract of $g$."** Having an arrow-map $f \to g$ in $\mathcal{C}^{\to}$ does not make $f$ a retract of $g$; you need the *return* arrow-map $g \to f$ with composite the identity. For example, the inclusion $\{0\} \hookrightarrow [0,1]$ maps to the identity of $[0,1]$, but it is not a retract of it (their domains differ as objects with no splitting). Retract is strictly stronger than "receives a map."

**Calibration check.** Verify that the class of maps with the RLP against a fixed map $i$ is closed under composition and under pullback. Verify that "$f$ is a retract of $g$" is transitive (compose retract diagrams). If you can also show that an identity map $\mathrm{id}_A$ has the LLP and RLP against every map, you have understood why identities lie in all three model-category classes.

---

# Unlocked by This

> [!tip] The Lifting Characterization of the Model Structure *(from this chapter)*
> Lifting and retracts together yield [[Thm - Closure Properties of the Model Structure]]: each of the four classes is exactly the maps with a prescribed lifting property, so the three classes of a model structure are mutually determined. The proof is the retract argument applied to the factorizations.

> [!tip] Cofibrant Generation and the Small Object Argument *(from Homotopical Algebra)*
> When a model structure is generated by a *set* $I$ of cofibrations, every fibration is detected as the maps with RLP against $I$, and Quillen's **small object argument** builds the factorizations by transfinitely attaching cells from $I$. The Galois-connection structure of orthogonality is exactly what makes this construction produce a weak factorization system.
