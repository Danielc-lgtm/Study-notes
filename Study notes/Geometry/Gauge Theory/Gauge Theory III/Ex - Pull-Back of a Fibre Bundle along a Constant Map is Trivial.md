---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle"
  - "Def - Fibre Bundle"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $(E, \pi, B)$ be a fibre bundle with typical fibre $F$, let $B'$ be a smooth manifold, and let $\lambda \colon B' \to B$ be a **constant map**: there is a fixed point $b_0 \in B$ with $\lambda(b') = b_0$ for every $b' \in B'$. Form the pull-back bundle $\lambda^* E = (E', \pi', B')$ of $(E, \pi, B)$ along $\lambda$.

Prove:
$$\lambda^* E \;=\; B' \times E_{b_0}, \qquad \pi' = \operatorname{pr}_1,$$
where $E_{b_0} = \pi^{-1}(b_0)$ is the fibre of $E$ over $b_0$, and deduce that $\lambda^* E$ is a **trivial** fibre bundle over $B'$, isomorphic to the product bundle $B' \times F \to B'$.

Concretely: compute the total space $E'$ as a subset of $B' \times E$, identify it with $B' \times E_{b_0}$, exhibit an explicit global trivialisation $\lambda^* E \to B' \times F$, and confirm it commutes with the projections to $B'$.

**Recall:**

The objects in play are a fibre bundle and its fibres, the pull-back of a bundle along a smooth map, and the notion of a trivial bundle.

![[Def - Fibre Bundle#The Definition]]

A [[Def - Fibre Bundle|fibre bundle]] $(E, \pi, B)$ with typical fibre $F$ is a surjective smooth map $\pi \colon E \to B$ such that every point $x \in B$ has an open neighbourhood $U \subseteq B$ carrying a **local trivialisation** — a diffeomorphism $\psi_U \colon \pi^{-1}(U) \to U \times F$ with $\operatorname{pr}_1 \circ \psi_U = \pi$. The **fibre** over $x$ is $E_x := \pi^{-1}(x)$; restricting a local trivialisation over $U \ni x$ gives a diffeomorphism $\psi_U|_{E_x} \colon E_x \to \{x\} \times F \cong F$, so every fibre is diffeomorphic to the typical fibre $F$. The bundle is **trivial** if it is isomorphic to the product bundle $(B \times F, \operatorname{pr}_1, B)$, equivalently if a single local trivialisation can be defined over all of $B$ (a global trivialisation).

![[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle#Statement]]

For a fibre bundle $(E, \pi, B)$ with typical fibre $F$ and a smooth map $\lambda \colon B' \to B$, the [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|pull-back]] is
$$E' := \{\,(b', p) \in B' \times E \;:\; \lambda(b') = \pi(p)\,\}, \qquad \pi' := \operatorname{pr}_1|_{E'} \colon E' \to B',$$
and the theorem asserts that $E'$ is an embedded submanifold of $B' \times E$, that $(E', \pi', B')$ is a fibre bundle with typical fibre $F$, that the second projection $\operatorname{pr}_2 \colon E' \to E$ restricts on each fibre to a diffeomorphism $E'_{b'} \to E_{\lambda(b')}$, and that the square
$$\begin{array}{ccc} \lambda^* E & \xrightarrow{\ \operatorname{pr}_2\ } & E \\[2pt] {\scriptstyle \pi'}\big\downarrow & & \big\downarrow{\scriptstyle \pi} \\[2pt] B' & \xrightarrow{\quad\lambda\quad} & B \end{array}$$
commutes.

> [!warning] Convention: the direction of $\lambda$
> Bär's text (Definitions 2.1.9–2.1.11, pp. 39–40) writes the smooth map as "$\lambda \colon B \to B'$" in the sentence that introduces it, but the very next display forms $E' = \{(b', p) : \lambda(b') = \pi(p)\}$ with $b' \in B'$ and produces a bundle *over* $B'$, which requires $\lambda(b') \in B$ and hence $\lambda \colon B' \to B$. The first arrow is a typographical slip; the pull-back is taken **along** $\lambda \colon B' \to B$, carrying a bundle over $B$ back to a bundle over $B'$, and we use that corrected direction throughout, matching [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle]].

---

# Convergent Strategy

**Problem class.** This is a *compute-the-object* problem: the pull-back is defined by a set-builder formula, and everything we need falls out of substituting the hypothesis into that formula and reading off the result. There is no clever construction to invent — the difficulty, such as it is, lies entirely in recognising that a constant map turns the fibred-product defect $\{\lambda(b') = \pi(p)\}$ into an *unconstrained* product. It is the base case of a family of triviality results whose general form is the homotopy theorem of §3.5, [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles]].

**Assumption pattern.** The single hypothesis that does all the work is $\lambda \equiv b_0$: the defining condition $\lambda(b') = \pi(p)$ becomes $b_0 = \pi(p)$, a condition on $p$ **alone** with no coupling to $b'$. Whenever the constraint that carves a fibred product out of an ordinary product decouples into a condition on one factor only, the fibred product *is* an ordinary product; that is the recognisable trigger here. The remaining hypotheses — that $(E, \pi, B)$ is a fibre bundle, so that $E_{b_0} \cong F$, and that the pull-back theorem endows $E'$ with a smooth-bundle structure — are used only to upgrade the set-level equality $E' = B' \times E_{b_0}$ to a diffeomorphism of bundles.

**Theorem routing.** The route is: substitute $\lambda \equiv b_0$ into the definition of $E'$ to get $E' = \{(b', p) : \pi(p) = b_0\} = B' \times E_{b_0}$ as sets and as smooth manifolds (the pull-back theorem, [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle]], makes $E'$ an embedded submanifold, and $B' \times E_{b_0}$ with $E_{b_0}$ the embedded fibre is the same embedded submanifold); observe that $\pi' = \operatorname{pr}_1$ is exactly the product-bundle projection; then use the fibre-bundle definition, [[Def - Fibre Bundle]], to pick a local trivialisation $\psi_U$ near $b_0$ and build the global trivialisation $\Psi \colon \lambda^* E \to B' \times F$, $\Psi(b', p) = (b', \operatorname{pr}_F \psi_U(p))$; conclude triviality because a global trivialisation exists.

**Key decision point.** The one move worth naming is *where the fibre bundle hypothesis re-enters*. The equality $E' = B' \times E_{b_0}$ is already true set-theoretically for any surjection $\pi$; it makes $\lambda^* E$ a product only over the abstract fibre $E_{b_0}$, which is not yet the typical fibre $F$. The bundle hypothesis is spent precisely once more, to supply the diffeomorphism $E_{b_0} \cong F$ from a local trivialisation over a neighbourhood of $b_0$ — and it is this last step that turns "$\lambda^* E$ is a product over its own $b_0$-fibre" into "$\lambda^* E$ is *the* trivial $F$-bundle". Forgetting it leaves the answer one diffeomorphism short of triviality.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles#Legal Operations|the topic page's Legal Operations]]:

1. **Substitute a defining formula.** Insert the hypothesis $\lambda(b') = b_0$ directly into the set-builder definition $E' = \{(b', p) : \lambda(b') = \pi(p)\}$ of the pull-back total space, and simplify the constraint.

2. **Recognise a decoupled constraint as a product.** When a defining condition on a subset of $B' \times E$ constrains the $E$-coordinate alone, identify the subset as a Cartesian product $B' \times (\text{constrained fibre})$.

3. **Match two embedded submanifolds by their common underlying set.** Both $\lambda^* E$ (from the pull-back theorem) and $B' \times E_{b_0}$ (product of $B'$ with the embedded fibre $E_{b_0}$) are embedded submanifolds of $B' \times E$ with the same points; since the embedded smooth structure on a subset is unique, they are equal as smooth manifolds.

4. **Read the pull-back projection as the product projection.** Observe $\pi' = \operatorname{pr}_1|_{E'} = \operatorname{pr}_1$ on $B' \times E_{b_0}$, i.e. the projection of the product bundle.

5. **Extract a fibre-to-typical-fibre diffeomorphism from a local trivialisation.** Use the fibre-bundle axiom to choose a local trivialisation $\psi_U$ over a neighbourhood $U \ni b_0$; its restriction gives a diffeomorphism $E_{b_0} \to F$.

6. **Build a global trivialisation and invoke the triviality criterion.** Assemble the diffeomorphism $\Psi \colon \lambda^* E \to B' \times F$ over the identity of $B'$, and conclude triviality from the criterion that a bundle is trivial if and only if it admits a global trivialisation.

---

# Hints

> [!note]- Hint 1
> Do not try to be clever. Write down the *definition* of the pull-back total space $E' = \{(b', p) \in B' \times E : \lambda(b') = \pi(p)\}$ and put the hypothesis $\lambda(b') = b_0$ into it. What condition on the pair $(b', p)$ survives, and does it involve $b'$ at all?

> [!note]- Hint 2
> The condition becomes $\pi(p) = b_0$, i.e. $p \in E_{b_0}$, with $b'$ free to range over all of $B'$. So as a set, $E' = B' \times E_{b_0}$, and the projection $\pi' = \operatorname{pr}_1$ is the projection of that product. You now have a product bundle over $B'$ — but its fibre is the specific set $E_{b_0}$, not yet the typical fibre $F$. Which axiom of a fibre bundle relates $E_{b_0}$ to $F$?

> [!note]- Hint 3
> Because $(E, \pi, B)$ is a fibre bundle, there is a local trivialisation $\psi_U \colon \pi^{-1}(U) \to U \times F$ over some open $U \ni b_0$. Restricting it to the fibre gives a diffeomorphism $\chi := \operatorname{pr}_F \circ \psi_U|_{E_{b_0}} \colon E_{b_0} \to F$. Use $\chi$ to turn the product $B' \times E_{b_0}$ into $B' \times F$ by acting on the second factor only.

> [!note]- Hint 4
> Define $\Psi \colon \lambda^* E \to B' \times F$ by $\Psi(b', p) = (b', \chi(p))$. Check three things: $\Psi$ is a diffeomorphism (its inverse is $(b', f) \mapsto (b', \chi^{-1}(f))$, both smooth); $\operatorname{pr}_1 \circ \Psi = \pi'$, so $\Psi$ respects the projections; therefore $\Psi$ is a global trivialisation. By the triviality criterion in [[Def - Fibre Bundle]], the existence of a global trivialisation is exactly triviality of the bundle.

---

# Solution

The whole proof is the observation that a constant map imposes no coupling between base and fibre: the defining constraint $\lambda(b') = \pi(p)$ of the pull-back collapses to $\pi(p) = b_0$, which frees the base coordinate entirely and leaves a Cartesian product. We first read off $\lambda^* E = B' \times E_{b_0}$ with its product projection from the definition and the pull-back theorem, and then spend the fibre-bundle hypothesis once more — to replace the abstract fibre $E_{b_0}$ by the typical fibre $F$ — which promotes the product to the trivial $F$-bundle.

**Step 1: Substitute the constant map into the pull-back and identify the total space.**

The total space of $\lambda^* E$ is the set $B' \times E_{b_0}$, and the pull-back projection is the first projection of that product.

> [!note]- Derivation
> By the definition of the pull-back along $\lambda \colon B' \to B$ (the corrected direction; see the Convention callout), the total space is
> $$E' = \{\,(b', p) \in B' \times E \;:\; \lambda(b') = \pi(p)\,\}.$$
> The hypothesis is that $\lambda$ is constant with value $b_0$: $\lambda(b') = b_0$ for every $b' \in B'$. Substituting this into the defining condition,
> $$\lambda(b') = \pi(p) \quad\Longleftrightarrow\quad b_0 = \pi(p) \quad\Longleftrightarrow\quad p \in \pi^{-1}(b_0) = E_{b_0} \qquad (\text{since } \lambda(b') = b_0 \text{ identically}).$$
> The resulting condition constrains $p$ to lie in the fixed fibre $E_{b_0}$ and places **no** restriction on $b' \in B'$. Therefore
> $$E' = \{\,(b', p) \in B' \times E \;:\; p \in E_{b_0}\,\} = B' \times E_{b_0} \qquad (\text{the constraint decoupled onto the } E\text{-factor}).$$
> The pull-back projection is the restriction of the first projection, $\pi' = \operatorname{pr}_1|_{E'}$, which on $B' \times E_{b_0}$ is simply $(b', p) \mapsto b'$ — the projection of the product $B' \times E_{b_0}$ onto $B'$.

**Step 2: The set equality is an equality of smooth manifolds.**

The two descriptions $\lambda^* E$ and $B' \times E_{b_0}$ carry the same smooth structure, because each is an embedded submanifold of $B' \times E$ on the same underlying set.

> [!note]- Derivation
> By [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|the pull-back theorem]] — restated: for a fibre bundle $(E, \pi, B)$ and smooth $\lambda \colon B' \to B$, the set $E' = \{(b', p) : \lambda(b') = \pi(p)\}$ is an embedded submanifold of $B' \times E$ and $(E', \operatorname{pr}_1, B')$ is a fibre bundle with typical fibre $F$ — the total space $\lambda^* E$ is an **embedded submanifold** of $B' \times E$.
>
> On the other hand, the fibre $E_{b_0} = \pi^{-1}(b_0)$ is an embedded submanifold of $E$: choosing a local trivialisation $\psi_U \colon \pi^{-1}(U) \to U \times F$ over an open $U \ni b_0$ (which exists by the [[Def - Fibre Bundle|fibre-bundle axiom]]), $E_{b_0} = \psi_U^{-1}(\{b_0\} \times F)$ is the preimage of the embedded submanifold $\{b_0\} \times F \subseteq U \times F$ under the diffeomorphism $\psi_U$, hence embedded. Consequently the product $B' \times E_{b_0}$ is an embedded submanifold of $B' \times E$ (a product of an embedded submanifold with the whole manifold $B'$ is embedded, its slice charts being products of a chart of $B'$ with the slice charts of $E_{b_0}$).
>
> By Step 1 the two embedded submanifolds $\lambda^* E$ and $B' \times E_{b_0}$ of $B' \times E$ have exactly the same underlying set. The smooth structure that an embedded submanifold inherits from its ambient manifold is uniquely determined by the underlying set (the subspace topology together with the requirement that the inclusion be a smooth embedding fixes the atlas up to no choice). Therefore the two coincide as smooth manifolds:
> $$\lambda^* E = B' \times E_{b_0} \qquad (\text{equality of embedded submanifolds of } B' \times E),$$
> and this equality carries the projections along, $\pi' = \operatorname{pr}_1$.

**Step 3: Replace the abstract fibre $E_{b_0}$ by the typical fibre $F$ and build a global trivialisation.**

A local trivialisation over a neighbourhood of $b_0$ furnishes a diffeomorphism $E_{b_0} \to F$, and multiplying it into the second factor turns $B' \times E_{b_0}$ into a global trivialisation of $\lambda^* E$ over $B' \times F$.

> [!note]- Derivation
> By the [[Def - Fibre Bundle|fibre-bundle axiom]] applied to $(E, \pi, B)$ at the point $b_0 \in B$, there is an open neighbourhood $U \ni b_0$ and a local trivialisation
> $$\psi_U \colon \pi^{-1}(U) \to U \times F, \qquad \operatorname{pr}_1 \circ \psi_U = \pi.$$
> Since $\operatorname{pr}_1 \circ \psi_U = \pi$, the map $\psi_U$ sends the fibre $E_{b_0} \subseteq \pi^{-1}(U)$ into $\{b_0\} \times F$, and restricting it there gives a diffeomorphism $\psi_U|_{E_{b_0}} \colon E_{b_0} \to \{b_0\} \times F$. Composing with the (diffeomorphic) projection $\{b_0\} \times F \to F$ defines
> $$\chi := \operatorname{pr}_F \circ \psi_U|_{E_{b_0}} \colon E_{b_0} \to F, \qquad \chi^{-1} = \psi_U^{-1}(b_0, \,\cdot\,) \colon F \to E_{b_0},$$
> a diffeomorphism (this is exactly Remark 2.1.2 of Bär: a local trivialisation restricts on each fibre to a diffeomorphism with $F$).
>
> Now define
> $$\Psi \colon \lambda^* E = B' \times E_{b_0} \longrightarrow B' \times F, \qquad \Psi(b', p) := (b', \chi(p)).$$
> We verify $\Psi$ is a global trivialisation.
>
> - **$\Psi$ is smooth.** It is $\Psi = (\operatorname{pr}_1, \chi \circ \operatorname{pr}_2)$ on the product $B' \times E_{b_0}$. The projections $\operatorname{pr}_1 \colon B' \times E_{b_0} \to B'$ and $\operatorname{pr}_2 \colon B' \times E_{b_0} \to E_{b_0}$ are smooth (projections of a product manifold), and $\chi$ is smooth; a map into the product $B' \times F$ is smooth if and only if both components are, so $\Psi$ is smooth.
> - **$\Psi$ is a diffeomorphism.** Its two-sided inverse is $\Psi^{-1}(b', f) = (b', \chi^{-1}(f))$, smooth by the same product argument since $\chi^{-1}$ is smooth. One checks $\Psi^{-1}(\Psi(b', p)) = \Psi^{-1}(b', \chi(p)) = (b', \chi^{-1}\chi(p)) = (b', p)$ and $\Psi(\Psi^{-1}(b', f)) = (b', \chi\chi^{-1}(f)) = (b', f)$.
> - **$\Psi$ commutes with the projections.** $\operatorname{pr}_1 \circ \Psi (b', p) = b' = \pi'(b', p)$, so $\operatorname{pr}_1 \circ \Psi = \pi'$.
>
> Thus $\Psi$ is a diffeomorphism $\lambda^* E \to B' \times F$ satisfying $\operatorname{pr}_1 \circ \Psi = \pi'$: a **global trivialisation** of $\lambda^* E$.

**Step 4: Conclude triviality.**

The existence of a global trivialisation is, by definition, triviality of the bundle.

> [!note]- Derivation
> By the triviality criterion recorded in [[Def - Fibre Bundle]] — a fibre bundle is trivial if and only if it admits a global trivialisation, equivalently a bundle isomorphism to the product bundle over the identity of the base — the global trivialisation $\Psi$ of Step 3 shows that
> $$\lambda^* E \;\cong\; B' \times F \quad\text{over } B',$$
> so $\lambda^* E$ is a trivial fibre bundle. Combining with Steps 1–2, we have proved both the exact identity $\lambda^* E = B' \times E_{b_0}$ with $\pi' = \operatorname{pr}_1$ and its consequence, triviality. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** Let $(E, \pi, B)$ be a fibre bundle with typical fibre $F$ and let $\lambda \colon B' \to B$ be the constant map $\lambda \equiv b_0$. Then $\lambda^* E = B' \times E_{b_0}$ with $\pi' = \operatorname{pr}_1$, and $\lambda^* E$ is trivial, isomorphic to $B' \times F \to B'$.
>
> *Proof.* By definition the pull-back total space is $E' = \{(b', p) \in B' \times E : \lambda(b') = \pi(p)\}$. Substituting $\lambda(b') = b_0$, the condition $\lambda(b') = \pi(p)$ becomes $\pi(p) = b_0$, i.e. $p \in E_{b_0}$, with no constraint on $b'$; hence $E' = B' \times E_{b_0}$ and $\pi' = \operatorname{pr}_1|_{E'} = \operatorname{pr}_1$.
>
> This is an equality of smooth manifolds. By [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|the pull-back theorem]], $\lambda^* E$ is an embedded submanifold of $B' \times E$. The fibre $E_{b_0} = \psi_U^{-1}(\{b_0\} \times F)$ is an embedded submanifold of $E$ for any local trivialisation $\psi_U$ over $U \ni b_0$, so $B' \times E_{b_0}$ is an embedded submanifold of $B' \times E$. Two embedded submanifolds with the same underlying set are equal, so $\lambda^* E = B' \times E_{b_0}$ as smooth bundles over $B'$.
>
> Choose a local trivialisation $\psi_U \colon \pi^{-1}(U) \to U \times F$ over an open $U \ni b_0$ (fibre-bundle axiom). Its fibre restriction gives a diffeomorphism $\chi := \operatorname{pr}_F \circ \psi_U|_{E_{b_0}} \colon E_{b_0} \to F$. Define $\Psi(b', p) = (b', \chi(p))$; then $\Psi \colon \lambda^* E \to B' \times F$ is smooth with smooth inverse $(b', f) \mapsto (b', \chi^{-1}(f))$, and $\operatorname{pr}_1 \circ \Psi = \pi'$. Thus $\Psi$ is a global trivialisation, and by the triviality criterion of [[Def - Fibre Bundle]], $\lambda^* E \cong B' \times F$ is trivial. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "$B'$ is not contractible, so how can the pull-back be trivial?"
> One might expect a nontrivial base $B'$ to force a nontrivial bundle, and hesitate to conclude triviality when $B'$ is, say, a torus or a sphere. This intuition is misplaced: triviality of a pull-back is governed by the *map* $\lambda$, not by the shape of $B'$. A constant map factors through a point, and a bundle pulled back through a point can only be a product — no amount of topology in $B'$ can obstruct it, because the map never "sees" that topology. The condition that would make the reasoning legal in the general case is exactly that $\lambda$ be **null-homotopic** (homotopic to a constant); then [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles]] transports the triviality proved here to $\lambda^* E$ for the actual $\lambda$. The present exercise is the base of that argument, not a counterexample to it.

---

# Key Takeaways

**A constant map decouples the fibred product into an ordinary product, and this is the cleanest instance of "the pull-back depends only on the homotopy class of the map".** The pull-back $\lambda^* E$ is defined as the fibred product $\{(b', p) : \lambda(b') = \pi(p)\}$, a subset of $B' \times E$ cut out by matching the base coordinate through $\lambda$ against the projection through $\pi$. Everything nontrivial about a pull-back lives in how that matching condition entangles the two factors. When $\lambda$ is constant, the condition degenerates to $\pi(p) = b_0$, a constraint on $p$ alone; the entanglement vanishes and the fibred product is a Cartesian product $B' \times E_{b_0}$. The reusable principle is that *the pull-back is trivial as soon as the map collapses the constraint onto one factor* — and the map that collapses it most brutally is a constant. This is why a constant map is the archetype: it realises the extreme case in which the pull-back "forgets" the bundle structure over $B$ entirely and remembers only a single fibre. The trigger to reach for this fact is any pull-back along a map that is constant, or that factors through a point, or (via §3.5) that is merely null-homotopic.

**The fibre-bundle hypothesis is spent in two distinct places, and confusing them loses the conclusion.** The first use is silent and cheap: it never appears until Step 2, where the pull-back theorem — which holds *because* $(E, \pi, B)$ is a fibre bundle — supplies the embedded-submanifold structure that upgrades the set equality $E' = B' \times E_{b_0}$ to an equality of manifolds. The second use is the decisive one in Step 3: the axiom that local trivialisations exist gives the diffeomorphism $E_{b_0} \cong F$ that replaces the *abstract* fibre $E_{b_0}$ — which is all the set computation delivers — by the *typical* fibre $F$, which is what "trivial bundle" refers to. A reader who stops after Step 2 has correctly shown $\lambda^* E$ is a product over its own $b_0$-fibre but has not yet shown it is *the* trivial $F$-bundle; the gap is precisely one application of the local-trivialisation axiom. The transferable diagnostic: whenever a computation produces "a product over some particular fibre", ask whether that fibre has been identified with the typical fibre, and locate the trivialisation that does the identifying.

**This exercise is the base case of the homotopy invariance of bundles, and reading it that way explains why triviality is a statement about maps rather than spaces.** The theorem of §3.5, [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles]], asserts that homotopic maps pull back isomorphic bundles; its most-used corollary is that a bundle pulled back along a null-homotopic map is trivial, and every bundle over a contractible base is trivial. The present computation is the seed of that corollary: it establishes triviality for an *actual* constant map by bare hands, and the homotopy theorem then propagates it to every map homotopic to a constant. Seen from this height, the lesson is that the isomorphism class of $\lambda^* E$ is a homotopy invariant of $\lambda$ — so a nontrivial base $B'$ never by itself forces a nontrivial pull-back, since one can always ask instead about the homotopy class of the classifying data. The companion exercises to hold beside this one are [[Ex - The Möbius Strip as a Mapping Torus is a Nontrivial Bundle]] and [[Ex - The Klein Bottle as a Mapping Torus]], which exhibit the opposite phenomenon — bundles whose nontriviality is a genuine obstruction — and thereby calibrate how special the constant-map situation is.
