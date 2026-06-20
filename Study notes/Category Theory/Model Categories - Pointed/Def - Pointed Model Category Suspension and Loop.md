---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Initial and Terminal Object"
  - "Def - Pullback and Pushout"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Thm - The Homotopy Category of a Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a **pointed model category**: a [[Def - Model Category|model category]] equipped with a [[Def - Initial and Terminal Object|zero object]] $*$, an object that is simultaneously initial and terminal. We write $\mathrm{Ho}(\mathcal{C})$ for its [[Thm - The Homotopy Category of a Model Category|homotopy category]], the localization at the weak equivalences. For objects $X, Y$ we write $[X, Y] = \mathrm{Ho}(\mathcal{C})(X, Y)$ for the set of morphisms in the homotopy category — when $X$ is [[Def - Cofibrant and Fibrant Objects|cofibrant]] and $Y$ is fibrant this is the set $\pi(X, Y)$ of [[Def - Cylinder Object, Path Object, and Homotopy|homotopy classes]] of maps $X \to Y$. The unique map factoring through $*$ from $X$ to $Y$ is the **zero map** $0 : X \to Y$. The functors are $\Sigma$ (**suspension**) and $\Omega$ (**loop**), each $\mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$. We write $\mathrm{Cyl}(X)$ and $\mathrm{Path}(Y)$ for [[Def - Cylinder Object, Path Object, and Homotopy|cylinder and path objects]]. The full symbol registry is on [[Model Categories — Pointed Model Categories and Cofiber Sequences]].

This is a compound page: it defines three interlocking notions — the **pointed model category**, the **suspension functor** $\Sigma$, and the **loop functor** $\Omega$ — because the suspension and loop are constructed from the zero object and only make sense once the category is pointed, and they are introduced together as the adjoint pair that organizes the whole chapter.

---

# Axiom Motivation

The motivating question is the simplest possible one in homotopy theory: given a space, how do you build a new space one dimension higher? On pointed topological spaces the answer is the suspension. You take a pointed space $X$, glue a cone on the top and a cone on the bottom, and you get $\Sigma X$ — for the circle $S^1$ this produces the sphere $S^2$, and in general $\Sigma S^n = S^{n+1}$. The loop space $\Omega X$ runs the other way: it is the space of based loops in $X$, and it is the right adjoint, in the sense that maps out of a suspension are the same as maps into a loop space. The content of this chapter is that *this entire structure is not special to topology* — it exists in any pointed model category, built mechanically from the model structure. The job of the definition is to identify the categorical bones of "cone on top, cone on bottom" so that the construction survives the move to an arbitrary $\mathcal{C}$.

Start with the requirement that $\mathcal{C}$ be **pointed**. Why insist on a zero object rather than just any model category? In an unpointed category the natural notion is the *unbased* suspension, the pushout of $* \leftarrow X \rightarrow *$ where the two $*$ are a single terminal object — but the terminal object and the initial (empty) object are different, so there is no canonical basepoint on the result, and crucially there is no **zero map** between objects. The whole apparatus of cofiber sequences depends on having a distinguished morphism $X \to Y$ for *every* pair, against which "the cofiber" can be measured. A zero object delivers exactly this: the composite $X \to * \to Y$ is the zero map, and it exists and is canonical precisely because $*$ is both initial and terminal. Drop initiality of $*$ and you lose the maps *out of* $*$ that anchor the suspension's basepoint; drop terminality and you lose the maps *into* $*$ that the loop construction needs. Pointedness is not decoration — it is the hypothesis that makes "the space of maps $[X, Y]$ is a pointed set" true, with the zero map as basepoint, and that pointed structure is what every later construction leans on.

Now the suspension itself. We want $\Sigma X$ to be "$X$ with both ends crushed to a point." Categorically, crushing the top means a map $X \to *$ and crushing the bottom means another map $X \to *$; forming the object that universally receives both crushings while remembering nothing else is the **pushout** of the diagram $* \leftarrow X \to *$. In $\mathbf{Top}_*$ this pushout is exactly the unreduced suspension (and, up to homotopy, the reduced suspension that is the standard $\Sigma$). But there is a subtlety that *forces* the word "homotopy" into the definition: the strict pushout of $* \leftarrow X \to *$ in $\mathcal{C}$ is just $*$ again, because $*$ is terminal and the pushout of two copies of the terminal object over anything collapses. The naive categorical suspension is trivial. What we actually want is the **homotopy pushout** — the pushout computed after replacing the maps by cofibrations so that the gluing is homotopy-invariant. Concretely, factor $X \to *$ as a cofibration $X \rightarrowtail C$ followed by a trivial fibration (this $C$ is a cone on $X$, a cylinder with one end at $*$), do this on both sides, and take the honest pushout of the two cofibrations. This is why the construction must be performed on a cofibrant $X$ with a cylinder object: the homotopy pushout of $* \leftarrow X \rightarrow *$ is the pushout $* \cup_X \mathrm{Cyl}(X) \cup_X *$, which collapses both ends of the cylinder. If you forget to make the maps cofibrations — if you take the strict pushout — the answer is wrong (it is $*$), and the functor you define does not descend to the homotopy category. The lesson is the recurring one in model-category theory: **a colimit only computes the right homotopical thing when its inputs are cofibrant and its legs are cofibrations.**

The loop functor is the exact dual, and the duality is not a convenience but a theorem about what $\Omega$ must be if $\Sigma \dashv \Omega$ is to hold. We want $\Omega Y$ to be "the based loops in $Y$," and the based-loop space is the homotopy fiber of $* \to Y$, equivalently the homotopy **pullback** of $* \to Y \leftarrow *$. The same subtlety appears: the strict pullback of $* \to Y \leftarrow *$ is $*$ (because $*$ is initial, dually), so one must use the homotopy pullback — replace $* \to Y$ by a fibration $\mathrm{Path}(Y) \cap (\text{one endpoint at } *) \to Y$ using a path object, and take the honest pullback. The need for fibrant $Y$ and a path object is the precise dual of the need for cofibrant $X$ and a cylinder object. One could ask: why define $\Omega$ separately at all, rather than just declaring it to be whatever right adjoint $\Sigma$ has? Because in a general pointed model category $\Sigma$ on the homotopy category need not have *any* adjoint until you exhibit one, and the homotopy-pullback construction is precisely the adjoint, by an argument that mirrors the cylinder/path duality. Defining $\Omega$ concretely is what *makes* the adjunction a theorem rather than a wish.

A final point that a would-be inventor must confront: why are $\Sigma$ and $\Omega$ functors on $\mathrm{Ho}(\mathcal{C})$ and not on $\mathcal{C}$ itself? Because the homotopy pushout and homotopy pullback are only well-defined up to weak equivalence — the cone $C$, the cylinder $\mathrm{Cyl}(X)$, and the path object $\mathrm{Path}(Y)$ all involve choices, and different choices give weakly equivalent but not isomorphic results. The constructions become genuine functors only after you pass to the homotopy category, where weakly equivalent objects are identified. This is the same reason the [[Thm - The Homotopy Category of a Model Category|homotopy category]] is where derived functors live: $\Sigma$ is the **derived functor of the (degenerate) strict suspension**, and $\Omega$ is the derived functor of the strict loop. Demanding the construction be homotopy-invariant is what pushes it onto $\mathrm{Ho}(\mathcal{C})$.

---

# The Definition

Let $\mathcal{C}$ be a model category.

**Pointed model category.** $\mathcal{C}$ is **pointed** if it has a [[Def - Initial and Terminal Object|zero object]] $*$: an object that is both initial and terminal, so that for every $X$ the hom-sets $\mathcal{C}(*, X)$ and $\mathcal{C}(X, *)$ are singletons. For every pair $X, Y$ the **zero map** $0 = 0_{X,Y} : X \to Y$ is the unique composite $X \to * \to Y$. (Concretely, the category $\mathcal{C}_*$ of *pointed objects* — objects under $*$ — of any model category $\mathcal{C}$ with terminal object is pointed; this is how $\mathbf{Top}_*$ and $\mathbf{sSet}_*$ arise.)

**Suspension.** Let $X$ be a [[Def - Cofibrant and Fibrant Objects|cofibrant]] object. Choose a [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] $\mathrm{Cyl}(X)$, with end inclusions $\mathrm{i}_0, \mathrm{i}_1 : X \to \mathrm{Cyl}(X)$. The **suspension** $\Sigma X$ is the [[Def - Pullback and Pushout|pushout]]
$$\Sigma X \;=\; * \cup_X \mathrm{Cyl}(X) \cup_X *,$$
that is, the colimit of $* \xleftarrow{\,0\,} X \xrightarrow{\mathrm{i}_0} \mathrm{Cyl}(X) \xleftarrow{\mathrm{i}_1} X \xrightarrow{\,0\,} *$ — the cylinder with both ends collapsed to the point. Equivalently, $\Sigma X$ is the **homotopy pushout** of $* \leftarrow X \rightarrow *$. This passes to a functor
$$\Sigma : \mathrm{Ho}(\mathcal{C}) \longrightarrow \mathrm{Ho}(\mathcal{C}),$$
independent of the choice of cylinder up to canonical isomorphism in $\mathrm{Ho}(\mathcal{C})$.

**Loop.** Let $Y$ be a [[Def - Cofibrant and Fibrant Objects|fibrant]] object. Choose a [[Def - Cylinder Object, Path Object, and Homotopy|path object]] $\mathrm{Path}(Y)$, with endpoint evaluations $\mathrm{p}_0, \mathrm{p}_1 : \mathrm{Path}(Y) \to Y$. The **loop object** $\Omega Y$ is the [[Def - Pullback and Pushout|pullback]]
$$\Omega Y \;=\; * \times_Y \mathrm{Path}(Y) \times_Y *,$$
the limit of $* \xrightarrow{\,0\,} Y \xleftarrow{\mathrm{p}_0} \mathrm{Path}(Y) \xrightarrow{\mathrm{p}_1} Y \xleftarrow{\,0\,} *$ — the paths in $Y$ that begin and end at the basepoint. Equivalently, $\Omega Y$ is the **homotopy pullback** of $* \rightarrow Y \leftarrow *$. This passes to a functor
$$\Omega : \mathrm{Ho}(\mathcal{C}) \longrightarrow \mathrm{Ho}(\mathcal{C}),$$
independent of the choice of path object up to canonical isomorphism in $\mathrm{Ho}(\mathcal{C})$.

The central fact, proved on [[Thm - The Suspension-Loop Adjunction]], is that $\Sigma$ is left adjoint to $\Omega$ on $\mathrm{Ho}(\mathcal{C})$:
$$[\Sigma X, Y] \;\cong\; [X, \Omega Y] \qquad \text{naturally in } X, Y.$$

---

# Categorical / Structural Definition

The cleanest categorical packaging is as **derived (co)limits**. The strict suspension is the functor $X \mapsto * \sqcup_X *$, the pushout of the cospan $* \leftarrow X \rightarrow *$; the strict loop is $Y \mapsto * \times_Y *$. Both are degenerate on the nose (they return $*$), so what one actually wants is their **derived functors**. A pushout is a colimit, and the total left derived functor of a colimit is the **homotopy colimit**; a pullback is a limit, and its total right derived functor is the **homotopy limit**. Thus:
$$\Sigma X = \mathrm{hocolim}\big( * \leftarrow X \rightarrow * \big), \qquad \Omega Y = \mathrm{holim}\big( * \rightarrow Y \leftarrow * \big),$$
where $\mathrm{hocolim}$ and $\mathrm{holim}$ are the [[Def - Homotopy Limit and Colimit|homotopy colimit and homotopy limit]]. The reason $\Sigma$ lands on the left and $\Omega$ on the right of an adjunction is now structural: homotopy colimits are left adjoints (they are derived left adjoints to constant-diagram functors), homotopy limits are right adjoints, and the diagrams defining $\Sigma$ and $\Omega$ are mutually dual. The adjunction $\Sigma \dashv \Omega$ is the homotopical shadow of the trivial adjunction "colimit $\dashv$ diagonal $\dashv$ limit," restricted to the pushout/pullback shape and corrected for homotopy.

There is a second structural description that explains the name "suspension" via cofiber sequences. The suspension is the **cofiber of the cofiber**: it is the homotopy cofiber of the map $X \to *$, and the homotopy cofiber is itself a homotopy pushout. Dually $\Omega$ is the homotopy fiber of $* \to Y$. This is the bridge to [[Def - Cofiber and Fiber Sequence|cofiber and fiber sequences]]: $\Sigma X$ is the third term in the cofiber sequence of $X \to *$, and the chapter's main structural theorem assembles these third terms into the Puppe sequence.

---

# Relate to Other Fields / Compression

In algebraic topology the suspension and loop are the engines of [[Def - Higher Homotopy Group|homotopy groups]]. On pointed spaces, $\Sigma S^n \simeq S^{n+1}$, so iterating the suspension manufactures all the spheres from $S^0$; and the adjunction $[\Sigma X, Y] \cong [X, \Omega Y]$ specializes, with $X = S^n$ and using $\pi_n(Y) = [S^n, Y]$, to the loop-space shift $\pi_{n+1}(Y) = \pi_n(\Omega Y)$ — the statement that "looping drops the homotopy degree by one." The classical reduced suspension $\Sigma X = X \wedge S^1$ and loop space $\Omega Y = \mathrm{Map}_*(S^1, Y)$ are *exactly* the homotopy pushout and homotopy pullback above, computed in $\mathbf{Top}_*$ with its [[Def - Model Category|Quillen model structure]]. So the abstract $\Sigma$ and $\Omega$ are not analogues of the topological ones — they *are* the topological ones, read off the model structure.

**True name:** $\Sigma X$ is the **homotopy cofiber of $X \to *$**, and $\Omega Y$ is the **homotopy fiber of $* \to Y$**. The cone-and-collapse picture is how you compute it; "homotopy cofiber of the map to a point" is what you should *think*, because it immediately tells you $\Sigma$ sits at the end of every cofiber sequence and obeys all the long-exact-sequence machinery. The operational form is even shorter: $\Sigma = -\!\wedge S^1$ and $\Omega = \mathrm{Map}_*(S^1, -)$ whenever $\mathcal{C}$ is a pointed simplicial or topological model category, and the abstract definition reduces to these.

There is a homological compression too. In a [[Def - Chain Map and Chain Homotopy|chain-complex]] model — the projective model structure on $\mathrm{Ch}(R)$, made pointed by the zero complex — the suspension is the **degree shift** $X \mapsto X[1]$ (move every term up one degree) and the loop is $X \mapsto X[-1]$. The adjunction becomes the tautology that shifting up and shifting down are inverse, foreshadowing the fact (in the next chapter) that for stable categories $\Sigma$ is an *equivalence*, not just an adjoint. So "suspension" unifies "add a dimension" (topology) and "shift the grading" (homological algebra) under one categorical construction.

---

# Examples / Corollaries

**Is an instance — pointed topological spaces.** Take $\mathcal{C} = \mathbf{Top}_*$, pointed compactly generated spaces with the [[Def - Model Category|Quillen model structure]] (weak equivalences = weak homotopy equivalences, fibrations = Serre fibrations); the zero object is the one-point space $*$. For a cofibrant (CW) pointed space $X$, the cylinder is $X \times [0,1]$ and collapsing both ends gives the reduced suspension $\Sigma X = X \wedge S^1$; for $X = S^n$ this is $S^{n+1}$. The loop object of a fibrant $Y$ is the based path-space pullback, which is the based loop space $\Omega Y = \mathrm{Map}_*(S^1, Y)$. The hom-set $[S^n, Y] = \pi_n(Y)$, and the adjunction is the classical $\pi_{n+1}(Y) \cong \pi_n(\Omega Y)$. This is the example all the others are abstracted from.

**Is an instance — pointed simplicial sets.** Take $\mathcal{C} = \mathbf{sSet}_*$, pointed [[Def - Simplicial Set|simplicial sets]] with the Kan–Quillen model structure; the zero object is $\Delta^0$ with its unique point, written $*$. Every object is cofibrant (cofibrations are monomorphisms), and fibrant objects are pointed Kan complexes. The suspension $\Sigma X$ is the simplicial reduced suspension $X \wedge S^1$ where $S^1 = \Delta^1/\partial\Delta^1$; the loop $\Omega Y$, for $Y$ a Kan complex, is the simplicial based loop object, and its homotopy groups are the simplicial homotopy groups of $Y$. Geometric realization carries this $\Sigma, \Omega$ to the topological ones, which is one reason $\mathbf{sSet}_*$ and $\mathbf{Top}_*$ model the same homotopy theory.

**Is an instance — chain complexes.** In the projective model structure on $\mathrm{Ch}(R)$ made pointed by the zero complex $0$, the suspension of a complex $X_\bullet$ is the shift $X[1]$ with $X[1]_n = X_{n-1}$, and the loop is $X[-1]$. Here $\Sigma$ is already invertible on the homotopy category (the derived category $D(R)$), which previews that $\mathrm{Ch}(R)$ is a *stable* model category and $D(R)$ is triangulated.

**Is NOT an instance — an unpointed model category.** Take $\mathcal{C} = \mathbf{Top}$ (unbased spaces, Quillen structure). It has a terminal object $*$ but its initial object is the empty space $\emptyset \ne *$, so it is **not pointed** and there are no zero maps. One cannot even write down "$\Sigma X$ = homotopy pushout of $* \leftarrow X \rightarrow *$ giving a *pointed* object," because the result has no canonical basepoint and the loop construction has no basepoint to loop around. The remedy is to pass to $\mathbf{Top}_*$, adjoining a disjoint basepoint via $X \mapsto X_+ = X \sqcup *$, which is exactly the free pointed object on $X$. This non-example is the reason the chapter insists on pointedness from the first line.

**Is NOT an instance — the strict pushout.** It is tempting to define $\Sigma X$ as the *strict* (non-homotopy) pushout of $* \leftarrow X \rightarrow *$. But $*$ is terminal, so this pushout is $*$ for every $X$: the strict suspension functor is constant at the zero object. This is a non-example of the *construction*, not of the category, and it is the single most important warning on the page: $\Sigma$ is the **derived** pushout, and computing it strictly destroys all information.

**Calibration check.** Verify three things. First, that in any pointed category the zero map $0_{X,Y}$ is independent of the choice of factorization through $*$ (use that $\mathcal{C}(*, Y)$ is a singleton). Second, that the strict pushout of $* \leftarrow X \rightarrow *$ is $*$, so the homotopy pushout is genuinely needed. Third, that for $\mathcal{C} = \mathbf{Top}_*$ and $X = S^0$ (two points, one the basepoint) the suspension $\Sigma S^0$ is $S^1$ — i.e., collapsing both ends of $S^0 \times [0,1]$, two intervals, glues them into a circle.

---

# Unlocked by This

> [!tip] Cofiber and Fiber Sequences *(from this chapter)*
> With $\Sigma$ in hand, the [[Def - Cofiber and Fiber Sequence|Puppe cofiber sequence]] $X \to Y \to C \to \Sigma X \to \Sigma Y \to \cdots$ exists in any pointed model category: $\Sigma X$ is the term that lets the sequence continue past the cofiber and become infinite, and the [[Thm - The Suspension-Loop Adjunction|adjunction]] converts the cofiber sequence into a long exact sequence of pointed sets $[\,-, Z]$.

> [!tip] Stable Model Categories and Triangulated Categories *(from the next chapter)*
> A pointed model category is called **stable** when $\Sigma : \mathrm{Ho}(\mathcal{C}) \to \mathrm{Ho}(\mathcal{C})$ is an equivalence — when looping and suspending are mutually inverse rather than merely adjoint. The homotopy category of a stable model category is a **triangulated category**, with $\Sigma$ as the shift and the cofiber sequences as the distinguished triangles. The derived category $D(R)$, where $\Sigma$ is the shift $X \mapsto X[1]$, and the **stable homotopy category of spectra**, where one has *formally inverted* $\Sigma$, are the two great examples.

> [!tip] The Spectrum and the Stabilization *(from stable homotopy theory)*
> Forcing $\Sigma$ to be invertible by hand — taking sequences $(X_0, X_1, \dots)$ with maps $\Sigma X_n \to X_{n+1}$ — produces a **spectrum**, and the category of spectra is the universal stable home for the suspension. The suspension and loop defined here are the seed of the whole subject of **stable homotopy theory** and of **stable $\infty$-categories**, the modern refinement where the shift is invertible by construction.
