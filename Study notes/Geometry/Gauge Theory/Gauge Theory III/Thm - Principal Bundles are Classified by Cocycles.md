---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Transition Functions and the Cocycle Condition"
  - "Def - Principal G-Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Def - Reduction and Extension of the Structure Group"
  - "Def - Associated Bundle"
  - "Thm - Vector Bundle Construction Lemma"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold (Hausdorff and second countable, as always in this series), $G$ is a Lie group with identity $e$, and $\{U_\alpha\}_{\alpha \in A}$ is an open cover of $M$ indexed by a set $A$. We write $U_{\alpha\beta} := U_\alpha \cap U_\beta$ and $U_{\alpha\beta\gamma} := U_\alpha \cap U_\beta \cap U_\gamma$. Group multiplication in $G$ and its inversion are smooth; for matrix groups they are the usual matrix product and inverse.

We follow the standing series conventions. **Lie groups act on principal bundles on the right**: for a [[Def - Principal G-Bundle|principal G-bundle]] $\pi : P \to M$, the action is written $R_g(p) = p \cdot g$, it is free and transitive on each fibre $P_x := \pi^{-1}(x)$, and the local trivialisations $\psi_U : \pi^{-1}(U) \to U \times G$ are chosen $G$-equivariant, meaning $\psi_U(p \cdot g) = (x, k \cdot g)$ whenever $\psi_U(p) = (x, k)$. A **local section** over an open set $U$ is a smooth map $s : U \to P$ with $\pi \circ s = \operatorname{id}_U$.

Given a family of local sections $s_\alpha : U_\alpha \to P$ (which exist over each trivialising $U_\alpha$ by [[Thm - Sections of a Principal Bundle and Triviality|the correspondence between sections and trivialisations]]), the **transition functions** are the unique smooth maps $g_{\alpha\beta} : U_{\alpha\beta} \to G$ with
$$s_\beta(x) = s_\alpha(x) \cdot g_{\alpha\beta}(x) \qquad (x \in U_{\alpha\beta}),$$
and they satisfy the **cocycle conditions** $g_{\alpha\alpha} = e$, $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$, and $g_{\alpha\beta} g_{\beta\gamma} g_{\gamma\alpha} = e$ on triple overlaps; the existence, uniqueness, smoothness, and these three identities are established on [[Def - Transition Functions and the Cocycle Condition]]. A **cocycle** on $\{U_\alpha\}$ with values in $G$ is any family of smooth maps $\{g_{\alpha\beta} : U_{\alpha\beta} \to G\}$ satisfying those three conditions. Two cocycles $\{g_{\alpha\beta}\}$ and $\{\tilde g_{\alpha\beta}\}$ on the same cover are **cohomologous** if there are smooth maps $h_\alpha : U_\alpha \to G$ with $g_{\alpha\beta} = h_\alpha \tilde g_{\alpha\beta} h_\beta^{-1}$ on every $U_{\alpha\beta}$.

For a Lie group homomorphism $\varphi : G \to H$, the **extension of the structure group** is the principal $H$-bundle $P \times_\varphi H := (P \times H)/G$ built on [[Def - Reduction and Extension of the Structure Group]], where $G$ acts on $P \times H$ by $(p, h) \cdot g = (p \cdot g, \varphi(g)^{-1} h)$, the residual right $H$-action is $[p, h] \cdot h' = [p, h h']$, and $[p, h]$ denotes the $G$-orbit of $(p, h)$. For a representation $\rho : G \to \operatorname{GL}(V)$ on a finite-dimensional vector space $V$ (with $V = \mathbb{R}^n$ or $\mathbb{C}^n$, so $\operatorname{GL}(V) = \operatorname{GL}_n$), the **associated vector bundle** is $P \times_\rho V := (P \times V)/G$ built on [[Def - Associated Bundle]], where $G$ acts by $(p, v) \cdot g = (p \cdot g, \rho(g)^{-1} v)$; we write $[p, v]$ for the orbit of $(p, v)$.

> [!warning] Convention: the transition-function relation and the extension misprint
> Bär writes the transition-function relation as $s_\beta = s_\alpha \cdot g_{\alpha\beta}$ (§2.2), which is the convention used here; Haydys writes the same relation for frames as $e = e' g$ in his equation (6), and after renaming the two agree. In Bär's Conclusion 2.2.9 and the surrounding text the extended bundle is printed once as "$P \times_\varphi G$"; the correct object is $P \times_\varphi H$ (the total space carries the group $H$, not $G$), and we use the corrected form throughout, as recorded on [[Def - Reduction and Extension of the Structure Group]].

The full symbol registry for the chapter is on the parent page **Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles**.

---

# Statement

> **Theorem (classification of principal bundles by cocycles).** Let $M$ be a smooth manifold, $G$ a Lie group, and $\{U_\alpha\}_{\alpha \in A}$ an open cover of $M$.
>
> **(a) Reconstruction.** Let $\{g_{\alpha\beta} : U_{\alpha\beta} \to G\}$ be a cocycle. On the disjoint union $X := \bigsqcup_{\alpha \in A} U_\alpha \times G$ define
> $$(x, g) \sim (x', g') \iff x = x' \ \text{ and } \ g = g_{\alpha\beta}(x) \, g' \qquad \big((x,g) \in U_\alpha \times G,\ (x',g') \in U_\beta \times G\big).$$
> Then $\sim$ is an equivalence relation, the quotient $P := X / \sim$ carries a unique smooth structure making the maps $\theta_\alpha : U_\alpha \times G \to P$, $\theta_\alpha(x,g) = [x,g]_\alpha$, diffeomorphisms onto open subsets, and with the projection $\pi([x,g]_\alpha) = x$ and the right action $[x,g]_\alpha \cdot h = [x, gh]_\alpha$, $(P, \pi, M)$ is a principal $G$-bundle. Its local sections $s_\alpha(x) := [x, e]_\alpha$ have transition functions exactly $g_{\alpha\beta}$.
>
> **(b) Every bundle is reconstructed.** If $Q \to M$ is any principal $G$-bundle admitting local sections over $\{U_\alpha\}$ with transition functions $\{g_{\alpha\beta}\}$, then the map
> $$\Phi : P \to Q, \qquad \Phi([x,g]_\alpha) = s_\alpha^{\,Q}(x) \cdot g$$
> (with $s_\alpha^{\,Q}$ the sections of $Q$) is an isomorphism of principal $G$-bundles covering $\operatorname{id}_M$. Hence every principal $G$-bundle is isomorphic to one reconstructed from its cocycle.
>
> **(c) Cohomologous cocycles classify.** Two cocycles $\{g_{\alpha\beta}\}$ and $\{\tilde g_{\alpha\beta}\}$ on the same cover produce isomorphic principal $G$-bundles (by an isomorphism covering $\operatorname{id}_M$) **if and only if** they are cohomologous, that is $g_{\alpha\beta} = h_\alpha \tilde g_{\alpha\beta} h_\beta^{-1}$ for smooth $h_\alpha : U_\alpha \to G$.
>
> **(d) Functoriality of the cocycle.** If $\{g_{\alpha\beta}\}$ is the cocycle of $P$ for sections $s_\alpha$, then:
> - the extension $P \times_\varphi H$ along a Lie group homomorphism $\varphi : G \to H$ has, with respect to the induced sections $s'_\alpha(x) = [s_\alpha(x), e]$, the transition functions $\varphi \circ g_{\alpha\beta}$;
> - the associated vector bundle $P \times_\rho V$ along a representation $\rho : G \to \operatorname{GL}(V)$ has, with respect to the trivialisations induced by $s_\alpha$, the vector-bundle transition functions $\rho \circ g_{\alpha\beta}$.

---

# Motivation

A principal bundle, as a manifold with a free transitive fibrewise group action, is a global object, and global objects are hard to build and hard to compare. The classification by cocycles is the theorem that trades this global object for a purely local, purely group-theoretic bookkeeping datum that one can actually write down, manipulate, and count. It is the organising theorem of the whole subject: after it, "a principal $G$-bundle over $M$" and "a $G$-valued cocycle on a cover of $M$, up to coboundary" become interchangeable descriptions, and every later construction — connections, characteristic classes, the classification of $U(1)$- and $SU(2)$-bundles — is carried out on whichever side of this dictionary is more convenient.

The problem it solves is concrete. Suppose we want to prove that some manifold carries a nontrivial bundle, or to enumerate all bundles of a given structure group, or to build a bundle with prescribed local behaviour. Working with total spaces directly is unwieldy: to compare two total spaces we would need to produce a diffeomorphism by hand and check equivariance everywhere. The cocycle description reduces all three tasks to linear-algebra-flavoured questions about maps $U_{\alpha\beta} \to G$. To build a bundle, write down a cocycle (part (a)); to recognise a given bundle, read off its cocycle (part (b)); to decide whether two bundles are the same, check whether their cocycles differ by a coboundary (part (c)).

There is a second reading, the physicist's, and it is not a mere analogy. A local section is a **choice of gauge**: it names, smoothly and locally, a preferred point in each fibre, and thereby identifies the fibre $P_x$ with the group $G$. Two overlapping gauges $s_\alpha, s_\beta$ disagree, and the transition function $g_{\alpha\beta}(x)$ is precisely the **gauge transformation** relating them, $s_\beta = s_\alpha g_{\alpha\beta}$. Part (c) then says something a physicist already believes: the physics — the isomorphism class of the bundle — does not depend on the gauge, and changing the gauge $s_\alpha \mapsto s_\alpha h_\alpha$ changes the transition functions by the coboundary $g_{\alpha\beta} \mapsto h_\alpha^{-1} g_{\alpha\beta} h_\beta$. The cohomology class of the cocycle is the gauge-invariant content.

The audience for this page is a reader who has met the [[Def - Principal G-Bundle|definition of a principal bundle]], knows that local sections exist and give rise to transition functions with the [[Def - Transition Functions and the Cocycle Condition|cocycle conditions]], and is comfortable with quotient topologies and smooth atlases. Nothing beyond that is assumed; every use of the sections-triviality correspondence and of the extension and associated-bundle constructions is recalled at its point of use.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of part (a) is mild — *any* $G$-valued cocycle on *any* open cover will do — so the real skill is recognising when a problem secretly hands you a cocycle even though no bundle is named.

The first disguised source is **a manifold given by an atlas together with a rule that transforms fibre data between charts**. Whenever one has overlapping charts $U_\alpha$ and, on each overlap, a smooth $G$-valued matching rule that composes correctly on triple overlaps, one has a cocycle, and part (a) manufactures a bundle from it with no further work. The non-obvious bridge is that the triple-overlap compatibility one always checks when gluing — "the identification $U_\alpha \leftrightarrow U_\gamma$ agrees with $U_\alpha \leftrightarrow U_\beta \leftrightarrow U_\gamma$" — is exactly the third cocycle condition. *Example problem:* build the frame bundle of $TS^2$ directly from the two stereographic charts, whose overlap rule is the Jacobian of the chart change $z \mapsto 1/z$, without ever describing the total space as a set of frames.

The second disguised source is **a family of clutching data on a decomposition of the base into pieces glued along a common boundary or overlap**. When $M$ is covered by two open sets $U_1, U_2$ whose intersection deformation-retracts onto a submanifold, a single map $g_{12} : U_{12} \to G$ automatically satisfies all cocycle conditions (there are no genuine triple overlaps to constrain, and $g_{21} = g_{12}^{-1}$, $g_{11} = g_{22} = e$ by fiat), so the bundle is completely determined by $g_{12}$. The bridge is that a two-set cover collapses the cocycle to one map, so part (c) reduces classification to the homotopy of that single map. *Example problem:* classify principal $G$-bundles over $S^n$ by the homotopy class of a clutching function $S^{n-1} \to G$ on the equatorial overlap of the two hemispheres.

The third disguised source is **a representation or homomorphism applied to a bundle you already understand**. If $P$ has a known cocycle and $\varphi : G \to H$ or $\rho : G \to \operatorname{GL}(V)$ is any Lie group homomorphism, then part (d) hands you the cocycle of the extended or associated bundle for free — it is $\varphi \circ g_{\alpha\beta}$ or $\rho \circ g_{\alpha\beta}$. The bridge is that "form the associated bundle" is, at the level of the classifying datum, just post-composition with a homomorphism, an operation one can compute by hand. *Example problem:* given the frame bundle of a real bundle $E$ with cocycle $g_{\alpha\beta}$ valued in $\operatorname{GL}_k(\mathbb{R})$, read off the cocycle of $E \otimes \mathbb{C}$ as the same $g_{\alpha\beta}$ viewed in $\operatorname{GL}_k(\mathbb{C})$, and of $\operatorname{End}(E)$ as $A \mapsto g_{\alpha\beta} A g_{\alpha\beta}^{-1}$.

**Targets (Output Amplification)**

Combine part (c) with **the connectedness of the structure group and a two-set cover**. If $G$ is connected and $M = U_1 \cup U_2$ with $U_{12}$ connected, the single transition function $g_{12} : U_{12} \to G$ can be deformed to the constant $e$ through maps into $G$, which is a coboundary; the payoff is that *every* such bundle is trivial. This is how one proves that all principal $U(1)$-bundles over $S^1$ are trivial: the extra ingredient is the path-connectedness of $U(1)$.

Combine part (c) with **an invariant of the coboundary class that survives it — a characteristic class or a Čech cohomology class**. Cohomologous cocycles have equal invariants, so any quantity computed from $\{g_{\alpha\beta}\}$ that is unchanged under $g_{\alpha\beta} \mapsto h_\alpha g_{\alpha\beta} h_\beta^{-1}$ is a bundle invariant. The payoff is a complete or partial classification: for abelian $G$ the coboundary relation is exactly the one defining the first Čech cohomology group $\check H^1(M; \underline{G})$ with coefficients in the sheaf of smooth $G$-valued functions, so isomorphism classes of principal $G$-bundles are in bijection with $\check H^1(M; \underline{G})$; the extra ingredient is sheaf/Čech machinery, and the payoff is the identification of the classifying set with a cohomology group.

Combine part (d) with **a known classification of the target's bundles**. If the bundles with structure group $H$ are already classified and $\varphi : G \to H$ is understood, then extension transports information across: a $G$-bundle whose extension is nontrivial is itself nontrivial, and a reduction of an $H$-bundle to $G$ exists exactly when its $H$-cocycle is cohomologous to one landing in $\varphi(G)$. The payoff is the reduction-of-structure-group theory (orientations, metrics, complex structures) expressed entirely in cocycle language; the extra ingredient is a description of the subgroup $\varphi(G) \subseteq H$.

---

# Why Is It True

Strip away the topology and picture what a principal bundle actually is. Over each patch $U_\alpha$ it is nothing but the trivial product $U_\alpha \times G$: the section $s_\alpha$ picks out the "identity" copy $U_\alpha \times \{e\}$, and freeness plus transitivity let the group coordinate the rest of the fibre, so a point of $P$ over $x \in U_\alpha$ is honestly a pair $(x, g)$ once the gauge $s_\alpha$ is fixed. The only real information in the bundle is therefore *how the two product descriptions over $U_\alpha$ and over $U_\beta$ are to be identified on the overlap*. That identification is a map $U_{\alpha\beta} \to G$, and it must be consistent when three patches meet — which is exactly the third cocycle condition. There is nothing else to a principal bundle.

> **The mechanism in one sentence: a principal bundle is a recipe for gluing trivial pieces $U_\alpha \times G$ along their overlaps, the recipe is the cocycle $\{g_{\alpha\beta}\}$, and changing the local gauges $s_\alpha \mapsto s_\alpha h_\alpha$ changes the recipe by a coboundary while leaving the glued object unchanged.**

Part (a) is the statement that any consistent recipe can actually be cooked: form the disjoint union of the trivial pieces and glue, using the cocycle to say which points are identified. The three cocycle conditions are not decoration — they are precisely reflexivity ($g_{\alpha\alpha} = e$), symmetry ($g_{\alpha\beta} = g_{\beta\alpha}^{-1}$), and transitivity ($g_{\alpha\beta} g_{\beta\gamma} = g_{\alpha\gamma}$) of the gluing relation, so they are exactly what is needed for the quotient to make sense. Part (b) is the converse observation that a bundle you were *handed* is recovered by this recipe from its own transition functions: the map $[x,g]_\alpha \mapsto s_\alpha(x) g$ undoes the gluing by re-inserting the gauge. Part (c) is the invariance of the glued object under a change of gauge: two recipes cook the same dish exactly when they differ by relabelling the identity element in each fibre, and relabelling is a coboundary. Part (d) is the observation that pushing the fibre through a homomorphism pushes the recipe through the same homomorphism, because the gluing is done *by* group elements and the homomorphism respects the group law.

The clean way to see part (b) and (c) at once is the torsor principle. Each fibre of a principal $G$-bundle is a $G$-torsor: a set on which $G$ acts freely and transitively, so it looks like $G$ but with no preferred identity. A map between torsors that is fibre-preserving and $G$-equivariant is automatically a bijection (equivariance plus one point determines everything, transitivity gives ontoness, freeness gives injectivity). Both the reconstruction isomorphism of (b) and the isomorphisms of (c) are manufactured to be fibre-preserving and equivariant, so they are automatically isomorphisms — one never has to build an inverse by hand.

---

# What Makes This Hard

The conceptual content is light; the difficulty is entirely in the bookkeeping, and there are three places to slip. First, the equivalence relation of part (a) lives on a *disjoint* union, so a point carries a chart label as well as coordinates $(x,g)$, and the index order in $g = g_{\alpha\beta}(x) g'$ matters: getting the direction of $g_{\alpha\beta}$ versus $g_{\beta\alpha}$ backwards makes $\sim$ fail transitivity, and the fix is to check each of reflexivity, symmetry, transitivity against the corresponding cocycle condition rather than assuming them. Second, the topological hygiene of the quotient — that it is Hausdorff and second countable, and that the charts overlap smoothly — is genuinely part of the proof and is where most textbook treatments simply write "one checks"; the Hausdorff verification in particular splits into the different-fibre and same-fibre cases and uses that the gluing maps are diffeomorphisms. Third, in parts (b), (c), (d) the temptation is to build inverse maps explicitly and verify smoothness twice; the efficient and less error-prone route is the torsor principle, proving each comparison map fibre-preserving and equivariant and then invoking that such a map is automatically an isomorphism — but one must actually verify equivariance, which is the step people skip.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For (a), glue the trivial pieces $U_\alpha \times G$ by the cocycle and check, in order, that the relation is an equivalence relation, that the quotient is a smooth manifold (openness of the quotient map, Hausdorff, second countable, smooth charts), and that the right $G$-action and the sections make it a principal bundle with the prescribed transition functions. For (b) and (c), define the obvious comparison map on representatives, show it is well-defined, fibre-preserving, and $G$-equivariant, and conclude it is an isomorphism by the torsor principle; for the converse of (c) read the coboundary off from an isomorphism by comparing its effect on the canonical sections. For (d) compute both sides of $s'_\beta = s'_\alpha g'_{\alpha\beta}$ using the defining equivalence of the extended or associated bundle and cancel by freeness.

**Subgoal decomposition:**

1. **$\sim$ is an equivalence relation.**
   - *Hint:* Match reflexivity to $g_{\alpha\alpha} = e$, symmetry to $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$, transitivity to $g_{\alpha\beta} g_{\beta\gamma} = g_{\alpha\gamma}$.
   - *Why needed:* Without it there is no quotient set $P$.

2. **The quotient map is open; $P$ is Hausdorff and second countable.**
   - *Hint:* Openness reduces to the gluing maps $(x,g) \mapsto (x, g_{\beta\alpha}(x) g)$ being homeomorphisms; Hausdorff splits into distinct base points (use $M$ Hausdorff) and equal base points (both points lie in one chart image); second countability uses that $M$ is Lindelöf, so the cover has a countable subcover.
   - *Why needed:* These are the standing requirements for $P$ to be a manifold at all.

3. **The charts $\theta_\alpha$ define a smooth atlas and $\pi$ is a submersion.**
   - *Hint:* $\theta_\alpha$ is a continuous open injection, hence a homeomorphism onto an open set; the transition $\theta_\alpha^{-1} \theta_\beta(x,g) = (x, g_{\alpha\beta}(x) g)$ is smooth with smooth inverse.
   - *Why needed:* It puts the smooth structure on $P$ and makes $\pi$ smooth.

4. **The right action is well-defined, smooth, free, transitive on fibres; the $\theta_\alpha$ give equivariant trivialisations.**
   - *Hint:* Well-definedness of $[x,g]\cdot h = [x,gh]$ uses that right multiplication by $h$ commutes with left multiplication by $g_{\alpha\beta}(x)$; freeness and transitivity are the group's own; the sections are $s_\alpha(x) = [x,e]_\alpha$.
   - *Why needed:* This is the content of "principal bundle" and yields the transition functions $g_{\alpha\beta}$.

5. **Reconstruction isomorphism (b).**
   - *Hint:* $\Phi([x,g]_\alpha) = s_\alpha^{Q}(x) g$ is well-defined by $s^Q_\beta = s^Q_\alpha g_{\alpha\beta}$; it is fibre-preserving and equivariant, hence an isomorphism, and in trivialisations it is the identity.
   - *Why needed:* It identifies an arbitrary bundle with its reconstruction.

6. **Cohomologous $\Rightarrow$ isomorphic, and isomorphic $\Rightarrow$ cohomologous (c).**
   - *Hint:* For $\Leftarrow$ use $\Xi([x,g]_\alpha) = [x, h_\alpha(x)^{-1} g]_{\sim'}$; for $\Rightarrow$ compare $\Phi \circ s_\alpha$ with $\tilde s_\alpha$ via a gauge $h_\alpha$ and expand $\Phi(s_\beta)$ two ways.
   - *Why needed:* It is the classification statement itself.

7. **Functoriality (d).**
   - *Hint:* In $P \times_\varphi H$, $[pg, h] = [p, \varphi(g) h]$; in $P \times_\rho V$, $[pg, v] = [p, \rho(g) v]$; substitute $s_\beta = s_\alpha g_{\alpha\beta}$ and read off the transition function.
   - *Why needed:* It computes the cocycles of the derived bundles and connects (a) to the [[Thm - Vector Bundle Construction Lemma|vector-bundle construction lemma]].

---

# Lemma Decomposition

> [!note]- Lemma 1: The gluing relation is an equivalence relation
> **Statement:** With $X = \bigsqcup_\alpha U_\alpha \times G$ and $(x,g) \sim (x',g') \iff x = x'$ and $g = g_{\alpha\beta}(x) g'$ (for $(x,g) \in U_\alpha \times G$, $(x',g') \in U_\beta \times G$), the relation $\sim$ is reflexive, symmetric, and transitive.
>
> **Hint:** Each of the three properties is one of the three cocycle conditions, in order.
>
> **Why needed:** Only an equivalence relation yields a well-defined quotient set $P = X/\sim$.
>
> > [!note]- Full proof
> > We write a point of $X$ as $(\alpha, x, g)$ to keep its chart label $\alpha$ visible; here $\alpha \in A$, $x \in U_\alpha$, $g \in G$. The relation reads $(\alpha, x, g) \sim (\beta, x', g') \iff x = x' \in U_{\alpha\beta}$ and $g = g_{\alpha\beta}(x) g'$.
> >
> > **Reflexivity.** Fix $(\alpha, x, g)$. We must show $g = g_{\alpha\alpha}(x) g$. By the first cocycle condition $g_{\alpha\alpha} = e$ (from [[Def - Transition Functions and the Cocycle Condition]]), so $g_{\alpha\alpha}(x) g = e g = g$. Hence $(\alpha, x, g) \sim (\alpha, x, g)$.
> >
> > **Symmetry.** Suppose $(\alpha, x, g) \sim (\beta, x, g')$, so $x \in U_{\alpha\beta}$ and $g = g_{\alpha\beta}(x) g'$. Multiplying on the left by $g_{\alpha\beta}(x)^{-1}$ gives $g_{\alpha\beta}(x)^{-1} g = g'$. By the second cocycle condition $g_{\alpha\beta}^{-1} = g_{\beta\alpha}$ (from [[Def - Transition Functions and the Cocycle Condition]]), so $g' = g_{\beta\alpha}(x) g$. Since $x \in U_{\beta\alpha} = U_{\alpha\beta}$, this is exactly $(\beta, x, g') \sim (\alpha, x, g)$.
> >
> > **Transitivity.** Suppose $(\alpha, x, g) \sim (\beta, x, g')$ and $(\beta, x, g') \sim (\gamma, x, g'')$. The first gives $x \in U_{\alpha\beta}$ and $g = g_{\alpha\beta}(x) g'$; the second gives $x \in U_{\beta\gamma}$ and $g' = g_{\beta\gamma}(x) g''$. Then $x \in U_\alpha \cap U_\beta \cap U_\gamma = U_{\alpha\beta\gamma}$, and substituting,
> > $$g = g_{\alpha\beta}(x) g' = g_{\alpha\beta}(x) g_{\beta\gamma}(x) g'' \qquad \text{(substituting } g' = g_{\beta\gamma}(x) g''\text{)}.$$
> > The third cocycle condition $g_{\alpha\beta} g_{\beta\gamma} g_{\gamma\alpha} = e$ on $U_{\alpha\beta\gamma}$ (from [[Def - Transition Functions and the Cocycle Condition]]) gives, after right-multiplication by $g_{\gamma\alpha}(x)^{-1} = g_{\alpha\gamma}(x)$ (second condition), the identity $g_{\alpha\beta}(x) g_{\beta\gamma}(x) = g_{\gamma\alpha}(x)^{-1} = g_{\alpha\gamma}(x)$. Therefore
> > $$g = g_{\alpha\gamma}(x) g'' \qquad \text{(by } g_{\alpha\beta}(x) g_{\beta\gamma}(x) = g_{\alpha\gamma}(x)\text{)},$$
> > and since $x \in U_{\alpha\gamma}$ this reads $(\alpha, x, g) \sim (\gamma, x, g'')$. Hence $\sim$ is transitive, and being reflexive, symmetric and transitive, it is an equivalence relation. $\blacksquare$

> [!note]- Lemma 2: The quotient map is open, and $P$ is Hausdorff and second countable
> **Statement:** Let $q : X \to P = X/\sim$ be the quotient map and give $P$ the quotient topology. Then $q$ is an open map, the restriction $\theta_\alpha := q|_{U_\alpha \times G}$ is injective, $P$ is Hausdorff, and $P$ is second countable.
>
> **Hint:** For openness, saturate an open set chart by chart using the diffeomorphisms $(x,g) \mapsto (x, g_{\beta\alpha}(x)g)$; for Hausdorff, treat distinct base points and equal base points separately; for second countability, extract a countable subcover of $\{U_\alpha\}$ by Lindelöf.
>
> **Why needed:** A manifold must be Hausdorff and second countable, and openness of $q$ is what makes the chart images open and $\theta_\alpha$ a homeomorphism.
>
> > [!note]- Full proof
> > Write points of $X$ as $(\alpha, x, g)$ as in Lemma 1, and $[\alpha, x, g] := q(\alpha, x, g)$.
> >
> > **The gluing maps are homeomorphisms.** For $\alpha, \beta \in A$ define $\Psi_{\alpha\beta} : U_{\alpha\beta} \times G \to U_{\alpha\beta} \times G$ by $\Psi_{\alpha\beta}(x, g) = (x, g_{\beta\alpha}(x) g)$. It is continuous ($g_{\beta\alpha}$ is smooth, hence continuous, and group multiplication is continuous), and it has the continuous inverse $(x, g') \mapsto (x, g_{\alpha\beta}(x) g')$ because $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$ (second cocycle condition). So each $\Psi_{\alpha\beta}$ is a homeomorphism.
> >
> > **$q$ is open.** Let $W \subseteq X$ be open. We show $q^{-1}(q(W))$ is open, which by the definition of the quotient topology gives that $q(W)$ is open. Fix $\alpha$. A point $(\alpha, x, g)$ lies in $q^{-1}(q(W))$ iff it is equivalent to some point of $W$, that is, iff there is $\beta$ and a point $(\beta, x, g') \in W$ with $(\alpha, x, g) \sim (\beta, x, g')$, i.e. with $g = g_{\alpha\beta}(x) g'$, equivalently $g' = g_{\beta\alpha}(x) g$. Thus
> > $$q^{-1}(q(W)) \cap (U_\alpha \times G) = \bigcup_{\beta \in A} \Psi_{\alpha\beta}^{-1}\big(W \cap (U_{\alpha\beta} \times G)\big),$$
> > because $(\alpha, x, g)$ with $x \in U_{\alpha\beta}$ satisfies $\Psi_{\alpha\beta}(x,g) = (x, g_{\beta\alpha}(x)g) = (x, g') \in W$ exactly when the displayed condition holds. Each set on the right is open (preimage of an open set under the continuous $\Psi_{\alpha\beta}$), so the union is open, so $q^{-1}(q(W)) \cap (U_\alpha \times G)$ is open for every $\alpha$. Since the $U_\alpha \times G$ are open and cover $X$, their union $q^{-1}(q(W))$ is open. Hence $q$ is open.
> >
> > **$\theta_\alpha$ is injective.** If $\theta_\alpha(x, g) = \theta_\alpha(x', g')$ then $(\alpha, x, g) \sim (\alpha, x', g')$, forcing $x = x'$ and $g = g_{\alpha\alpha}(x) g' = g'$ (first cocycle condition). So $(x,g) = (x',g')$.
> >
> > **$\theta_\alpha$ is a homeomorphism onto an open set.** It is continuous (restriction of $q$), injective (just shown), and open: for $W \subseteq U_\alpha \times G$ open, $W$ is open in $X$, so $\theta_\alpha(W) = q(W)$ is open in $P$ by openness of $q$. A continuous open injection is a homeomorphism onto its image, and $\theta_\alpha(U_\alpha \times G) = q(U_\alpha \times G)$ is open.
> >
> > **$P$ is Hausdorff.** Let $[y_1] \neq [y_2]$ in $P$, with $\pi[y_i] = x_i$ (the well-definedness of $\pi$ is checked in Lemma 3; here we use only that equivalent points share their base point, which is clause (i) of $\sim$).
> > *Case 1: $x_1 \neq x_2$.* Since $M$ is Hausdorff, choose disjoint open $V_1 \ni x_1$, $V_2 \ni x_2$. Then $\pi^{-1}(V_1)$ and $\pi^{-1}(V_2)$ are disjoint; they are open because $\pi \circ \theta_\alpha = \operatorname{pr}_1$ is continuous on each chart and the $\theta_\alpha$ are homeomorphisms onto an open cover of $P$, so $\pi$ is continuous. They separate $[y_1]$ and $[y_2]$.
> > *Case 2: $x_1 = x_2 =: x$.* Pick $\alpha$ with $x \in U_\alpha$. Every point of $P$ over $x$ has a representative in $U_\alpha \times G$: indeed a representative $(\beta, x, g)$ satisfies $(\beta, x, g) \sim (\alpha, x, g_{\alpha\beta}(x) g)$, and the latter lies in $U_\alpha \times G$. Hence $[y_1], [y_2] \in \theta_\alpha(U_\alpha \times G)$, an open subset of $P$ homeomorphic (via $\theta_\alpha$) to the Hausdorff space $U_\alpha \times G$. Two distinct points of a Hausdorff space are separated by disjoint opens of that space, which are open in $P$ because $\theta_\alpha(U_\alpha \times G)$ is open. So $[y_1]$ and $[y_2]$ are separated.
> >
> > **$P$ is second countable.** $M$ is second countable, hence Lindelöf, so the open cover $\{U_\alpha\}$ has a countable subcover $\{U_{\alpha_i}\}_{i \in \mathbb{N}}$. The sets $\theta_{\alpha_i}(U_{\alpha_i} \times G)$ cover $P$: any $[y]$ over $x$ has $x \in U_{\alpha_i}$ for some $i$, and by the argument of Case 2 a representative in $U_{\alpha_i} \times G$. Each $\theta_{\alpha_i}(U_{\alpha_i} \times G)$ is homeomorphic to $U_{\alpha_i} \times G$, which is second countable ($U_{\alpha_i}$ is second countable as a subspace of the second countable $M$, and $G$, being a manifold in this series, is second countable; a product of two second countable spaces is second countable). A topological space that is the union of countably many open second countable subspaces is second countable: taking a countable base for each subspace and forming the countable union yields a countable base for $P$. Hence $P$ is second countable. $\blacksquare$

> [!note]- Lemma 3: The charts form a smooth atlas and $\pi$ is a submersion
> **Statement:** The maps $\theta_\alpha : U_\alpha \times G \to P$ form a smooth atlas on $P$ (their transition maps are diffeomorphisms), giving $P$ a unique smooth structure of dimension $\dim M + \dim G$ in which each $\theta_\alpha$ is a diffeomorphism onto an open set; and $\pi : P \to M$, $\pi[\alpha, x, g] = x$, is a well-defined smooth surjective submersion.
>
> **Hint:** Compute $\theta_\alpha^{-1} \circ \theta_\beta$ on its domain; it is $(x, g) \mapsto (x, g_{\alpha\beta}(x) g)$.
>
> **Why needed:** It equips $P$ with the smooth structure and provides the projection whose fibres carry the group action.
>
> > [!note]- Full proof
> > By Lemma 2, $P$ is Hausdorff and second countable and each $\theta_\alpha$ is a homeomorphism from the smooth manifold $U_\alpha \times G$ onto the open set $\theta_\alpha(U_\alpha \times G) \subseteq P$; these open sets cover $P$. So $\{(\theta_\alpha(U_\alpha \times G), \theta_\alpha^{-1})\}$ is a topological atlas modelling $P$ on the $(\dim M + \dim G)$-dimensional manifolds $U_\alpha \times G$.
> >
> > **Transition maps are smooth.** Fix $\alpha, \beta$. The overlap of the two chart images is $\theta_\alpha(U_\alpha \times G) \cap \theta_\beta(U_\beta \times G)$, which consists of the classes $[y]$ over points $x \in U_{\alpha\beta}$. A point $(x, g') \in U_\beta \times G$ has $\theta_\beta(x, g') = [\beta, x, g']$ in this overlap iff $x \in U_{\alpha\beta}$, and then $[\beta, x, g'] = [\alpha, x, g_{\alpha\beta}(x) g']$ by the definition of $\sim$, so
> > $$(\theta_\alpha^{-1} \circ \theta_\beta)(x, g') = (x, g_{\alpha\beta}(x) g') \qquad \text{on } U_{\alpha\beta} \times G.$$
> > This is smooth: $x \mapsto g_{\alpha\beta}(x)$ is smooth by hypothesis and multiplication $G \times G \to G$ is smooth. Its inverse is $(x, g) \mapsto (x, g_{\beta\alpha}(x) g)$ (using $g_{\alpha\beta}^{-1} = g_{\beta\alpha}$), also smooth. Hence $\theta_\alpha^{-1} \circ \theta_\beta$ is a diffeomorphism between open subsets of $U_\beta \times G$ and $U_\alpha \times G$. So $\{\theta_\alpha\}$ is a smooth atlas, determining a unique smooth structure on $P$ in which every $\theta_\alpha$ is a diffeomorphism onto an open set. Uniqueness is the standard fact that an atlas determines its maximal smooth structure.
> >
> > **$\pi$ is a well-defined smooth submersion.** If $(\alpha, x, g) \sim (\beta, x', g')$ then $x = x'$, so $\pi[\alpha, x, g] := x$ is independent of the representative and $\pi : P \to M$ is well-defined; it is surjective because each $U_\alpha \neq \emptyset$ contributes every $x \in U_\alpha$. In the chart $\theta_\alpha$, $(\pi \circ \theta_\alpha)(x, g) = x = \operatorname{pr}_1(x, g)$, which is smooth and a submersion (its differential is the surjective projection $T_xU_\alpha \oplus T_gG \to T_xU_\alpha$). Since smoothness and the submersion property are local and hold in every chart, $\pi$ is a smooth submersion. Its dimension count is $\dim P = \dim M + \dim G$. $\blacksquare$

> [!note]- Lemma 4: The right action makes $P$ a principal $G$-bundle with cocycle $\{g_{\alpha\beta}\}$
> **Statement:** The formula $[\alpha, x, g] \cdot h := [\alpha, x, gh]$ defines a smooth right $G$-action on $P$ that is free, transitive on each fibre of $\pi$, and for which each $\theta_\alpha^{-1} =: \psi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times G$ is a $G$-equivariant local trivialisation. Consequently $(P, \pi, M)$ is a principal $G$-bundle, its maps $s_\alpha(x) := [\alpha, x, e]$ are smooth local sections, and their transition functions are $s_\beta = s_\alpha g_{\alpha\beta}$, i.e. the cocycle we started from.
>
> **Hint:** Well-definedness of the action uses that left multiplication by $g_{\alpha\beta}(x)$ commutes with right multiplication by $h$; equivariance of $\psi_\alpha$ is immediate in the chart.
>
> **Why needed:** This is the assertion of part (a): the glued object is a principal bundle realising the given cocycle.
>
> > [!note]- Full proof
> > **The action is well-defined.** Suppose $(\alpha, x, g) \sim (\beta, x, g')$, so $g = g_{\alpha\beta}(x) g'$. For $h \in G$, $gh = g_{\alpha\beta}(x) g' h = g_{\alpha\beta}(x)(g' h)$, so $(\alpha, x, gh) \sim (\beta, x, g'h)$. Hence $[\alpha, x, g] \cdot h = [\alpha, x, gh]$ does not depend on the representative. It satisfies $[\alpha,x,g] \cdot e = [\alpha, x, ge] = [\alpha,x,g]$ and $([\alpha,x,g] \cdot h) \cdot h' = [\alpha, x, (gh)h'] = [\alpha, x, g(hh')] = [\alpha,x,g] \cdot (hh')$ by associativity in $G$. So we have a right $G$-action.
> >
> > **The action is smooth.** In the chart $\theta_\alpha$, the action reads $(\theta_\alpha^{-1} \circ R \circ (\theta_\alpha \times \operatorname{id}_G))(x, g, h) = (x, gh)$, where $R(p, h) = p \cdot h$; this is smooth because multiplication in $G$ is smooth. Smoothness being local on $P$, the action map $P \times G \to P$ is smooth.
> >
> > **The action preserves fibres, and is free and transitive on them.** Since $\pi([\alpha, x, g] \cdot h) = \pi[\alpha, x, gh] = x = \pi[\alpha, x, g]$, the action preserves fibres. Freeness: if $[\alpha, x, g] \cdot h = [\alpha, x, g]$ then $[\alpha, x, gh] = [\alpha, x, g]$, and since $\theta_\alpha$ is injective (Lemma 2), $gh = g$, so $h = e$. Transitivity on the fibre over $x$: fix $\alpha$ with $x \in U_\alpha$; every point of $\pi^{-1}(x)$ equals $[\alpha, x, g]$ for some $g \in G$ (by the representative argument of Lemma 2, Case 2), and given two such points $[\alpha, x, g_1], [\alpha, x, g_2]$, we have $[\alpha, x, g_1] \cdot (g_1^{-1} g_2) = [\alpha, x, g_2]$.
> >
> > **$\psi_\alpha = \theta_\alpha^{-1}$ is an equivariant local trivialisation.** First, $\theta_\alpha(U_\alpha \times G) = \pi^{-1}(U_\alpha)$: the inclusion $\subseteq$ is clear from $\pi[\alpha, x, g] = x \in U_\alpha$, and $\supseteq$ is the representative argument again. By Lemma 3, $\theta_\alpha$ is a diffeomorphism $U_\alpha \times G \to \pi^{-1}(U_\alpha)$, so $\psi_\alpha := \theta_\alpha^{-1} : \pi^{-1}(U_\alpha) \to U_\alpha \times G$ is a diffeomorphism; it satisfies $\operatorname{pr}_1 \circ \psi_\alpha = \pi$ (from $\pi \circ \theta_\alpha = \operatorname{pr}_1$), so it is a local trivialisation of the fibre bundle $\pi$. It is equivariant: for $p = [\alpha, x, g]$ with $\psi_\alpha(p) = (x, g)$,
> > $$\psi_\alpha(p \cdot h) = \psi_\alpha([\alpha, x, gh]) = (x, gh) = (x, g) \cdot h,$$
> > where $(x,g) \cdot h := (x, gh)$ is the standard right action on $U_\alpha \times G$. Freeness, transitivity on fibres, and the existence of equivariant local trivialisations are exactly the three clauses of [[Def - Principal G-Bundle|the definition of a principal G-bundle]] (a fibre bundle with a fibrewise-free, fibrewise-transitive right $G$-action admitting equivariant local trivialisations). Hence $(P, \pi, M)$ is a principal $G$-bundle.
> >
> > **The sections and their transition functions.** The map $s_\alpha(x) = [\alpha, x, e] = \theta_\alpha(x, e)$ is smooth (composition of the smooth $x \mapsto (x,e)$ with the diffeomorphism $\theta_\alpha$) and satisfies $\pi \circ s_\alpha = \operatorname{id}_{U_\alpha}$, so it is a local section. For $x \in U_{\alpha\beta}$,
> > $$s_\beta(x) = [\beta, x, e] = [\alpha, x, g_{\alpha\beta}(x) \cdot e] = [\alpha, x, g_{\alpha\beta}(x)] = [\alpha, x, e] \cdot g_{\alpha\beta}(x) = s_\alpha(x) \cdot g_{\alpha\beta}(x),$$
> > using the definition of $\sim$ in the second step and the definition of the right action in the fourth. Hence the transition functions of $P$ with respect to $\{s_\alpha\}$ are the $g_{\alpha\beta}$ we began with. $\blacksquare$

> [!note]- Lemma 5: A fibre-preserving equivariant smooth map of principal $G$-bundles is an isomorphism (torsor principle)
> **Statement:** Let $P, Q$ be principal $G$-bundles over $M$ and let $F : P \to Q$ be smooth, fibre-preserving ($\pi_Q \circ F = \pi_P$), and $G$-equivariant ($F(p \cdot g) = F(p) \cdot g$). Then $F$ is an isomorphism of principal $G$-bundles: it is a diffeomorphism whose inverse is also fibre-preserving and equivariant.
>
> **Hint:** In equivariant trivialisations $F$ becomes $(x, g) \mapsto (x, \lambda(x) g)$ for a smooth $\lambda : U \to G$; such a map is a diffeomorphism.
>
> **Why needed:** It converts the well-definedness-plus-equivariance checks in (b) and (c) into isomorphism statements with no separate inverse construction.
>
> > [!note]- Full proof
> > Fix $x \in M$ and equivariant local trivialisations $\psi^P_\alpha : \pi_P^{-1}(U_\alpha) \to U_\alpha \times G$ and $\psi^Q_\alpha : \pi_Q^{-1}(U_\alpha) \to U_\alpha \times G$ over a neighbourhood $U_\alpha \ni x$ ($P$ and $Q$ are locally trivial, so such trivialisations exist; shrink $U_\alpha$ so that both are defined). In these trivialisations $F$ reads
> > $$(\psi^Q_\alpha \circ F \circ (\psi^P_\alpha)^{-1})(x, g) = (x, \lambda(x) g)$$
> > for some map $\lambda : U_\alpha \to G$. Indeed, $F$ is fibre-preserving so the first coordinate is unchanged; writing the image of $(x, e)$ as $(x, \lambda(x))$ and using equivariance, $F((\psi^P_\alpha)^{-1}(x, g)) = F((\psi^P_\alpha)^{-1}(x, e) \cdot g) = F((\psi^P_\alpha)^{-1}(x,e)) \cdot g$, whose $\psi^Q_\alpha$-image is $(x, \lambda(x)) \cdot g = (x, \lambda(x) g)$. The map $\lambda$ is smooth because it equals $\operatorname{pr}_2 \circ \psi^Q_\alpha \circ F \circ (\psi^P_\alpha)^{-1}(\cdot, e)$, a composition of smooth maps.
> >
> > The local model $(x, g) \mapsto (x, \lambda(x) g)$ is a diffeomorphism of $U_\alpha \times G$ with smooth inverse $(x, g) \mapsto (x, \lambda(x)^{-1} g)$ (inversion in $G$ is smooth). Since $F$ agrees with a diffeomorphism in trivialisations around every point, $F$ is a local diffeomorphism; being also a bijection (injective and surjective on each fibre, because $(x,g) \mapsto (x, \lambda(x) g)$ is a bijection of each fibre and $F$ is fibre-preserving over all of $M$), $F$ is a diffeomorphism. Its inverse is fibre-preserving ($\pi_P \circ F^{-1} = \pi_Q$ follows from $\pi_Q \circ F = \pi_P$) and equivariant ($F^{-1}(q \cdot g) = F^{-1}(q) \cdot g$ follows by applying $F^{-1}$ to $F(F^{-1}(q) \cdot g) = q \cdot g$). Hence $F$ is an isomorphism of principal $G$-bundles. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $M$, $G$, and the open cover $\{U_\alpha\}_{\alpha \in A}$.
>
> **Part (a) — reconstruction.** Let $\{g_{\alpha\beta}\}$ be a cocycle. By **Lemma 1** the relation $\sim$ on $X = \bigsqcup_\alpha U_\alpha \times G$ is an equivalence relation, so $P = X/\sim$ is a set with quotient map $q$. By **Lemma 2** $q$ is open, each $\theta_\alpha = q|_{U_\alpha \times G}$ is injective, and $P$ is Hausdorff and second countable. By **Lemma 3** the $\theta_\alpha$ form a smooth atlas, giving $P$ a unique smooth structure of dimension $\dim M + \dim G$ in which each $\theta_\alpha$ is a diffeomorphism onto an open set, and $\pi[\alpha,x,g] = x$ is a smooth submersion; the local trivialisations $\psi_\alpha = \theta_\alpha^{-1}$ then exhibit $\pi$ as a fibre bundle with fibre $G$. By **Lemma 4** the formula $[\alpha,x,g] \cdot h = [\alpha,x,gh]$ is a smooth, free, fibrewise-transitive right $G$-action for which the $\psi_\alpha$ are equivariant, so $(P, \pi, M)$ is a principal $G$-bundle, and the sections $s_\alpha(x) = [\alpha, x, e]$ have transition functions exactly $g_{\alpha\beta}$. This proves (a), including the uniqueness of the smooth structure asserted in the statement (Lemma 3). $\ \checkmark$
>
> **Part (b) — every bundle is its own reconstruction.** Let $Q \to M$ be a principal $G$-bundle with smooth local sections $s^Q_\alpha : U_\alpha \to Q$ (these exist over each trivialising $U_\alpha$ by [[Thm - Sections of a Principal Bundle and Triviality|the sections-triviality correspondence]]: over a set on which $Q$ is trivial, a trivialisation yields a section $s^Q_\alpha = (\psi^Q_\alpha)^{-1}(\cdot, e)$) and transition functions $g_{\alpha\beta}$ defined by $s^Q_\beta = s^Q_\alpha g_{\alpha\beta}$. Let $P = X/\sim$ be the bundle reconstructed from this cocycle in part (a). Define
> $$\Phi : P \to Q, \qquad \Phi([\alpha, x, g]) := s^Q_\alpha(x) \cdot g.$$
>
> *Step 0 — $\Phi$ is well-defined.* Suppose $(\alpha, x, g) \sim (\beta, x, g')$, so $g = g_{\alpha\beta}(x) g'$. Then
> $$s^Q_\alpha(x) \cdot g = s^Q_\alpha(x) \cdot \big(g_{\alpha\beta}(x) g'\big) = \big(s^Q_\alpha(x) \cdot g_{\alpha\beta}(x)\big) \cdot g' = s^Q_\beta(x) \cdot g' \qquad \text{(by } s^Q_\beta = s^Q_\alpha g_{\alpha\beta}\text{)},$$
> so the value is independent of the representative and $\Phi$ is a well-defined function.
>
> *Step 1 — $\Phi$ is fibre-preserving and equivariant.* Since $s^Q_\alpha(x)$ lies in the fibre over $x$ and the $G$-action preserves fibres, $\pi_Q(\Phi([\alpha,x,g])) = \pi_Q(s^Q_\alpha(x) \cdot g) = x = \pi_P([\alpha,x,g])$, so $\pi_Q \circ \Phi = \pi_P$. For $h \in G$,
> $$\Phi([\alpha,x,g] \cdot h) = \Phi([\alpha, x, gh]) = s^Q_\alpha(x) \cdot (gh) = \big(s^Q_\alpha(x) \cdot g\big) \cdot h = \Phi([\alpha,x,g]) \cdot h,$$
> so $\Phi$ is $G$-equivariant.
>
> *Step 2 — $\Phi$ is smooth.* In the chart $\theta_\alpha$ of $P$, $(\Phi \circ \theta_\alpha)(x, g) = s^Q_\alpha(x) \cdot g$, a composition of the smooth section $s^Q_\alpha$, the smooth inclusion into $Q \times G$, and the smooth action $Q \times G \to Q$; hence $\Phi$ is smooth on each chart image, so smooth.
>
> *Step 3 — conclude.* By **Lemma 5** (torsor principle), a smooth fibre-preserving equivariant map of principal $G$-bundles is an isomorphism; therefore $\Phi : P \to Q$ is an isomorphism of principal $G$-bundles covering $\operatorname{id}_M$. Every principal $G$-bundle admitting sections over $\{U_\alpha\}$ is thus isomorphic to the reconstruction of its cocycle. $\ \checkmark$
>
> **Part (c) — cohomologous cocycles classify.** Let $\{g_{\alpha\beta}\}$ and $\{\tilde g_{\alpha\beta}\}$ be cocycles on the same cover, with reconstructed bundles $P = X/\sim$ and $\tilde P = X/\sim'$ (where $\sim'$ uses $\tilde g_{\alpha\beta}$), canonical sections $s_\alpha(x) = [\alpha,x,e]_\sim$, $\tilde s_\alpha(x) = [\alpha,x,e]_{\sim'}$, and their respective transition functions $g_{\alpha\beta}$, $\tilde g_{\alpha\beta}$ (part (a)).
>
> *Direction ($\Leftarrow$): cohomologous $\Rightarrow$ isomorphic.* Assume $g_{\alpha\beta} = h_\alpha \tilde g_{\alpha\beta} h_\beta^{-1}$ for smooth $h_\alpha : U_\alpha \to G$. Define
> $$\Xi : P \to \tilde P, \qquad \Xi([\alpha, x, g]_\sim) := [\alpha, x, h_\alpha(x)^{-1} g]_{\sim'}.$$
> *Well-defined:* if $(\alpha, x, g) \sim (\beta, x, g')$, then $g = g_{\alpha\beta}(x) g'$, and
> $$h_\alpha(x)^{-1} g = h_\alpha(x)^{-1} g_{\alpha\beta}(x) g' = h_\alpha(x)^{-1}\big(h_\alpha(x) \tilde g_{\alpha\beta}(x) h_\beta(x)^{-1}\big) g' = \tilde g_{\alpha\beta}(x)\, h_\beta(x)^{-1} g' \quad \text{(by } g_{\alpha\beta} = h_\alpha \tilde g_{\alpha\beta} h_\beta^{-1}\text{)},$$
> which says exactly $(\alpha, x, h_\alpha(x)^{-1} g) \sim' (\beta, x, h_\beta(x)^{-1} g')$, so the two $\sim'$-classes agree and $\Xi$ is well-defined. It is fibre-preserving ($\pi_{\tilde P} \circ \Xi = \pi_P$, since the base point $x$ is unchanged) and equivariant ($\Xi([\alpha,x,g] \cdot k) = \Xi([\alpha,x,gk]) = [\alpha, x, h_\alpha(x)^{-1} g k]_{\sim'} = [\alpha,x,h_\alpha(x)^{-1}g]_{\sim'} \cdot k = \Xi([\alpha,x,g]) \cdot k$). It is smooth, since in charts it reads $(x,g) \mapsto (x, h_\alpha(x)^{-1} g)$. By **Lemma 5**, $\Xi$ is an isomorphism of principal $G$-bundles covering $\operatorname{id}_M$, so $P \cong \tilde P$.
>
> *Direction ($\Rightarrow$): isomorphic $\Rightarrow$ cohomologous.* Assume $\Phi : P \to \tilde P$ is an isomorphism of principal $G$-bundles covering $\operatorname{id}_M$. For each $\alpha$, the map $\Phi \circ s_\alpha : U_\alpha \to \tilde P$ is a smooth local section of $\tilde P$ (it covers the identity: $\pi_{\tilde P}(\Phi(s_\alpha(x))) = \pi_P(s_\alpha(x)) = x$). Since $\tilde s_\alpha$ is also a section over $U_\alpha$, and any two smooth local sections of a principal bundle over the same set differ by a unique smooth map into $G$ — this is the existence, uniqueness, and smoothness of the comparison established on [[Def - Transition Functions and the Cocycle Condition]], applied to $\tilde P$ — there is a unique smooth $h_\alpha : U_\alpha \to G$ with
> $$\Phi(s_\alpha(x)) = \tilde s_\alpha(x) \cdot h_\alpha(x) \qquad (x \in U_\alpha).$$
> Now compute $\Phi(s_\beta(x))$ for $x \in U_{\alpha\beta}$ in two ways. First, using $s_\beta = s_\alpha g_{\alpha\beta}$ and equivariance of $\Phi$,
> $$\Phi(s_\beta(x)) = \Phi\big(s_\alpha(x) \cdot g_{\alpha\beta}(x)\big) = \Phi(s_\alpha(x)) \cdot g_{\alpha\beta}(x) = \tilde s_\alpha(x) \cdot h_\alpha(x) g_{\alpha\beta}(x).$$
> Second, using the definition of $h_\beta$ and then $\tilde s_\beta = \tilde s_\alpha \tilde g_{\alpha\beta}$,
> $$\Phi(s_\beta(x)) = \tilde s_\beta(x) \cdot h_\beta(x) = \tilde s_\alpha(x) \cdot \tilde g_{\alpha\beta}(x) h_\beta(x).$$
> Equating the two expressions, $\tilde s_\alpha(x) \cdot \big(h_\alpha(x) g_{\alpha\beta}(x)\big) = \tilde s_\alpha(x) \cdot \big(\tilde g_{\alpha\beta}(x) h_\beta(x)\big)$; since the $G$-action on $\tilde P$ is **free**, we may cancel $\tilde s_\alpha(x)$ to obtain
> $$h_\alpha(x) g_{\alpha\beta}(x) = \tilde g_{\alpha\beta}(x) h_\beta(x), \qquad \text{hence} \qquad g_{\alpha\beta} = h_\alpha^{-1} \tilde g_{\alpha\beta} h_\beta.$$
> Setting $k_\alpha := h_\alpha^{-1}$ (smooth, since inversion in $G$ is smooth) gives $g_{\alpha\beta} = k_\alpha \tilde g_{\alpha\beta} k_\beta^{-1}$, which is the coboundary relation of the statement. Therefore the cocycles are cohomologous. Combining the two directions proves (c). $\ \checkmark$
>
> **Part (d) — functoriality of the cocycle.**
>
> *Extension along $\varphi : G \to H$.* Recall from [[Def - Reduction and Extension of the Structure Group|the extension construction]] that $P' := P \times_\varphi H = (P \times H)/G$ with $G$ acting by $(p, h) \cdot g = (p \cdot g, \varphi(g)^{-1} h)$ and right $H$-action $[p, h] \cdot h' = [p, h h']$; it is proved there to be a principal $H$-bundle. A key identity, obtained by acting with $g$ on $(p, \varphi(g) h)$, is
> $$[p \cdot g, h] = [p, \varphi(g) h], \qquad \text{since } (p, \varphi(g) h) \cdot g = (p \cdot g, \varphi(g)^{-1} \varphi(g) h) = (p \cdot g, h).$$
> Also, for fixed $p$ the map $h \mapsto [p, h]$ is injective: if $[p, h_1] = [p, h_2]$ then $(p, h_2) = (p, h_1) \cdot g = (p \cdot g, \varphi(g)^{-1} h_1)$ for some $g$, whence $p \cdot g = p$, so $g = e$ by **freeness of the $G$-action on $P$**, and then $h_2 = h_1$. The induced sections are $s'_\alpha(x) := [s_\alpha(x), e]$. For $x \in U_{\alpha\beta}$, using $s_\beta = s_\alpha g_{\alpha\beta}$ and the key identity with $p = s_\alpha(x)$, $g = g_{\alpha\beta}(x)$, $h = e$,
> $$s'_\beta(x) = [s_\beta(x), e] = [s_\alpha(x) \cdot g_{\alpha\beta}(x), e] = [s_\alpha(x), \varphi(g_{\alpha\beta}(x))].$$
> On the other hand, writing $g'_{\alpha\beta}$ for the (as yet unknown) transition functions of $P'$ with respect to $\{s'_\alpha\}$, defined by $s'_\beta = s'_\alpha \cdot g'_{\alpha\beta}$,
> $$s'_\beta(x) = s'_\alpha(x) \cdot g'_{\alpha\beta}(x) = [s_\alpha(x), e] \cdot g'_{\alpha\beta}(x) = [s_\alpha(x), g'_{\alpha\beta}(x)].$$
> Equating and using the injectivity of $h \mapsto [s_\alpha(x), h]$ just proved, $\varphi(g_{\alpha\beta}(x)) = g'_{\alpha\beta}(x)$, that is $g'_{\alpha\beta} = \varphi \circ g_{\alpha\beta}$.
>
> *Associated vector bundle along $\rho : G \to \operatorname{GL}(V)$.* Recall from [[Def - Associated Bundle|the associated-bundle construction]] that $E := P \times_\rho V = (P \times V)/G$ with $G$ acting by $(p, v) \cdot g = (p \cdot g, \rho(g)^{-1} v)$, and that acting with $g$ on $(p, \rho(g) v)$ gives the identity
> $$[p \cdot g, v] = [p, \rho(g) v], \qquad \text{since } (p, \rho(g) v) \cdot g = (p \cdot g, \rho(g)^{-1} \rho(g) v) = (p \cdot g, v).$$
> Each section $s_\alpha$ induces a local trivialisation $\Psi_\alpha : E|_{U_\alpha} \to U_\alpha \times V$ of the vector bundle $E$ by $\Psi_\alpha([s_\alpha(x), v]) = (x, v)$; this is well-defined and a fibrewise linear isomorphism, because every class over $x$ has a unique representative of the form $[s_\alpha(x), v]$ (given $[p, v]$ with $\pi(p) = x$, transitivity and freeness give a unique $g$ with $p = s_\alpha(x) \cdot g$, and then $[p, v] = [s_\alpha(x) \cdot g, v] = [s_\alpha(x), \rho(g) v]$). For $x \in U_{\alpha\beta}$ the vector-bundle transition function $\tau_{\alpha\beta} := \Psi_\alpha \circ \Psi_\beta^{-1}$ satisfies, for $v \in V$,
> $$\Psi_\beta^{-1}(x, v) = [s_\beta(x), v] = [s_\alpha(x) \cdot g_{\alpha\beta}(x), v] = [s_\alpha(x), \rho(g_{\alpha\beta}(x)) v] \quad \text{(key identity, } p = s_\alpha(x),\ g = g_{\alpha\beta}(x)\text{)},$$
> so that
> $$\tau_{\alpha\beta}(x) v = (\Psi_\alpha \circ \Psi_\beta^{-1})(x, v) = \Psi_\alpha\big([s_\alpha(x), \rho(g_{\alpha\beta}(x)) v]\big) = (x, \rho(g_{\alpha\beta}(x)) v),$$
> i.e. $\tau_{\alpha\beta}(x) = \rho(g_{\alpha\beta}(x)) = (\rho \circ g_{\alpha\beta})(x) \in \operatorname{GL}(V)$. These maps are smooth (composition of the smooth $g_{\alpha\beta}$ with the smooth homomorphism $\rho$) and satisfy the multiplicative cocycle conditions $\tau_{\alpha\gamma} = \tau_{\alpha\beta} \tau_{\beta\gamma}$ on triple overlaps, since $\rho$ is a homomorphism and $g_{\alpha\beta} g_{\beta\gamma} = g_{\alpha\gamma}$. By the [[Thm - Vector Bundle Construction Lemma|vector bundle construction lemma]] — which states that fibres $E_x$, an open cover, fibrewise-linear bijections $\Psi_\alpha$, and a smooth $\operatorname{GL}$-valued cocycle $\{\tau_{\alpha\beta}\}$ with $(\Psi_\alpha \circ \Psi_\beta^{-1})(x, v) = (x, \tau_{\alpha\beta}(x) v)$ determine a unique smooth vector bundle with the $\Psi_\alpha$ as trivialisations — the bundle $E$ is exactly the vector bundle with transition functions $\rho \circ g_{\alpha\beta}$. This proves (d). $\ \checkmark$
>
> All four parts are established. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Clutching over spheres and homotopy groups (algebraic topology).** Cover $S^n$ by the two open sets $U_1 = S^n \setminus \{\text{south pole}\}$ and $U_2 = S^n \setminus \{\text{north pole}\}$, each contractible, with $U_{12}$ homotopy equivalent to the equator $S^{n-1}$. A cocycle collapses to a single **clutching function** $g_{12} : U_{12} \to G$, and part (c) shows two such give isomorphic bundles exactly when the clutching functions are homotopic. The theorem thus reduces the classification of principal $G$-bundles over $S^n$ to $[S^{n-1}, G] = \pi_{n-1}(G)$ (for connected $G$). This is non-obvious because a purely bundle-theoretic classification is converted into a computation in a homotopy group; the application depends on recognising the two-set cover as the source that kills all triple overlaps.

**Line bundles and the exponential sheaf sequence (complex geometry).** For $G = U(1)$ the coboundary relation $g_{\alpha\beta} = h_\alpha g_{\alpha\beta} h_\beta^{-1} = h_\alpha h_\beta^{-1} g_{\alpha\beta}$ (abelian, so conjugation is trivial and the relation is additive after taking logarithms) identifies isomorphism classes of principal $U(1)$-bundles with $\check H^1(M; \underline{U(1)})$. Feeding this into the exponential sheaf sequence $0 \to \mathbb{Z} \to \underline{\mathbb{R}} \to \underline{U(1)} \to 0$ produces the first Chern class as the connecting homomorphism to $\check H^2(M; \mathbb{Z})$. The application is non-obvious because the theorem's coboundary relation is precisely the equivalence defining Čech $H^1$, a fact one must notice to make the bridge.

**Reduction of structure group and $G$-structures (differential geometry).** A Riemannian metric on a rank-$k$ real bundle $E$ is a reduction of the frame bundle's structure group from $\operatorname{GL}_k(\mathbb{R})$ to $O(k)$; by part (d) and part (c) this is the statement that the $\operatorname{GL}_k$-cocycle of $E$ is cohomologous to one valued in $O(k)$. Deciding when such a reduction exists — always, by a partition of unity — becomes a statement about deforming a cocycle into a subgroup. The application is non-obvious because it recasts the analytic construction of a metric as the cocycle-level operation of conjugating the transition functions into $O(k)$.

---

# Bridges

- **From cocycles to Čech cohomology.** When $G$ is abelian, the set of cocycles on a fixed cover modulo coboundaries is literally the first Čech cohomology group $\check H^1(\{U_\alpha\}; \underline{G})$ of the cover with coefficients in the sheaf $\underline{G}$ of smooth $G$-valued functions; passing to the direct limit over refinements of covers gives $\check H^1(M; \underline{G})$, and part (c) upgrades to the bijection $\{\text{principal } G\text{-bundles}\}/\!\cong \ \leftrightarrow \check H^1(M; \underline{G})$. This is the entry point to the sheaf-theoretic classification of line bundles and, through the exponential sequence, to characteristic classes. For non-abelian $G$ the same coboundary relation defines the pointed set $\check H^1(M; \underline{G})$, which is no longer a group but still classifies bundles.

- **From cocycles to classifying maps.** A principal $G$-bundle is also classified by a homotopy class of maps $M \to BG$ into the classifying space, with the universal bundle $EG \to BG$ pulled back. The cocycle description is the local, hands-on shadow of this: a cocycle is the same data as a map from $M$ to the nerve of the cover, and refining covers corresponds to the limiting process building $BG$. This series proves the concrete low-dimensional classifications ($U(1)$- and $SU(2)$-bundles) directly from the cocycle theorem rather than from $BG$, whose homotopy theory is not developed here.

- **From transition functions to gauge fields (physics).** In gauge theory a local section is a choice of gauge and the transition function $g_{\alpha\beta}$ is the gauge transformation relating overlapping gauges; a connection is described locally by gauge potentials $A_\alpha$ that transform as $A_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}} A_\alpha + g_{\alpha\beta}^* \theta$ under the same $g_{\alpha\beta}$. Part (c) is then the statement that the physics is gauge-independent: the coboundary $g_{\alpha\beta} \mapsto h_\alpha g_{\alpha\beta} h_\beta^{-1}$ is a change of gauge $s_\alpha \mapsto s_\alpha h_\alpha$, and the isomorphism class it leaves fixed is the gauge-invariant content of the field configuration. This bridge is developed on the connection pages of Gauge Theory IV.

---

# Unlocked by This

> [!tip] First Čech Cohomology as a Classifying Set *(from Algebraic Topology / Sheaf Theory)*
> The coboundary relation of part (c) is the defining equivalence of $\check H^1(M; \underline{G})$. For abelian $G$ this makes the isomorphism classes of principal $G$-bundles into a group; the identity is the trivial bundle and the group law is the pointwise product of cocycles. This is the foundation for classifying **Hermitian line bundles** by $\operatorname{Pic}(M)$ and, via the exponential sequence, by the first Chern class, taken up in Gauge Theory VI.

> [!tip] Clutching Construction over Spheres *(from Topology of Fibre Bundles)*
> Over $S^n$, part (a) with the two-hemisphere cover turns a single map $g_{12} : S^{n-1} \to G$ into a bundle, and part (c) turns homotopy of clutching functions into isomorphism of bundles, giving the bijection between principal $G$-bundles over $S^n$ and $\pi_{n-1}(G)$ for connected $G$. This is the engine behind the classifications of **$U(1)$-bundles** (via $\pi_1(U(1)) = \mathbb{Z}$) and **$SU(2)$-bundles over $S^4$** (via $\pi_3(SU(2)) = \mathbb{Z}$) proved later in this chapter.
