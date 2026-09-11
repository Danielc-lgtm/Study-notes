---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Principal G-Bundle"
  - "Thm - Homogeneous Space is a Smooth Manifold"
  - "Thm - Local Submersion Theorem"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a Lie group and $H \leq G$ a closed subgroup, so that $H$ is an embedded Lie subgroup and the coset space $G/H = \{gH : g \in G\}$ carries its homogeneous-space smooth structure. Let $\pi : G \to G/H$, $\pi(g) = gH$, be the natural projection, and let $H$ act on $G$ on the **right** by right translation, $g \cdot h := gh$. Prove:

$$\pi : G \to G/H \text{ is a principal } H\text{-bundle.}$$

Concretely, verify the four defining clauses of a principal bundle for this data:

1. $\pi : G \to G/H$ is a smooth fibre bundle whose typical fibre is $H$;
2. the right $H$-action on $G$ is smooth and free;
3. the action preserves the fibres of $\pi$ and is transitive on each fibre;
4. the local trivialisations can be chosen $H$-**equivariant**: $\psi_U(g \cdot h) = \psi_U(g) \cdot h$.

You may use the differential-geometry theorem that $G/H$ is a smooth manifold and $\pi$ a smooth submersion; the content of the exercise is to package that data into the principal-bundle definition of this series, above all to build the equivariant local trivialisations. As special cases, identify the principal bundles $\mathrm{SO}(3) \to S^2$ and $\mathrm{SU}(2) \to S^2$.

This is the standard example of a principal bundle recorded in Bär §2.2, resting on the statement from Differential Geometry XI.

**Recall:**

The objects in play are the definition of a principal bundle (four clauses), the homogeneous-space theorem (giving the manifold structure and submersion), and the local-section corollary of the submersion theorem (the tool that builds trivialisations).

![[Def - Principal G-Bundle#The Definition]]

A [[Def - Principal G-Bundle|principal $G$-bundle]] is a smooth fibre bundle $\pi : P \to M$ together with a smooth right $G$-action on $P$ that is free, preserves fibres, is transitive on each fibre, and admits $G$-equivariant local trivialisations $\psi_U : \pi^{-1}(U) \to U \times G$ with $\psi_U(p \cdot g) = \psi_U(p) \cdot g$, where $G$ acts on $U \times G$ on the second factor by right translation. The four clauses above are these requirements specialised to $P = G$, $M = G/H$, structure group $H$.

![[Thm - Homogeneous Space is a Smooth Manifold#Statement]]

![[Thm - Local Submersion Theorem#Statement]]

The corollary we lean on is the **Local Section Theorem**: a smooth map $F : M \to N$ is a submersion at $p$ if and only if there is an open neighbourhood $V$ of $F(p)$ and a smooth local section $\sigma : V \to M$ (that is, $F \circ \sigma = \operatorname{id}_V$) with $\sigma(F(p)) = p$.

---

# Convergent Strategy

**Problem class.** This is a *verify-a-rich-object-satisfies-a-definition* problem: a differential-geometry theorem hands us a great deal of structure (a manifold, a submersion, a smooth free proper action), and the task is to recognise that this structure *is* a principal bundle in the gauge-theoretic sense, closing the one gap the source theorem leaves implicit — the construction of *equivariant* local trivialisations. The pattern is: import the heavy analytic input, then do the light bookkeeping of matching clauses.

**Assumption pattern.** Closedness of $H$ is used exactly once, upstream, to invoke [[Thm - Homogeneous Space is a Smooth Manifold|the homogeneous-space theorem]] (which needs it for properness of the right action and hence for the quotient to be a manifold with $\pi$ a submersion). After that, only three cheap facts are used: multiplication on $G$ is smooth (for smoothness of the action), the group cancellation law (for freeness and transitivity on fibres), and the local-section property of submersions (for the trivialisations). The recognisable trigger is "I have a submersion with a free fibrewise-transitive group action and I want equivariant charts" — the response is always "take a local section and read off the group element."

**Theorem routing.** The route is: invoke the homogeneous-space theorem to get that $G/H$ is a smooth manifold, $\pi$ a smooth submersion, and the right $H$-action smooth, free, and proper (clauses 1–2, and the fibre structure of clause 3); check directly that $\pi(gh) = \pi(g)$ and $\pi^{-1}(gH) = gH$ (clause 3); then for each $\bar g_0 \in G/H$ apply [[Thm - Local Submersion Theorem|the local section corollary]] to $\pi$ to get a smooth local section $s : U \to G$, and *define* the trivialisation $\psi_U(g) := (\pi(g),\, s(\pi(g))^{-1} g)$, checking that $s(\pi(g))^{-1} g$ lands in $H$, that $\psi_U$ is a diffeomorphism, and that it is equivariant (clauses 1 and 4). The special cases are then handled by [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit–stabiliser]]: identify $S^2$ as $\mathrm{SO}(3)/\mathrm{SO}(2)$ and as $\mathrm{SU}(2)/U(1)$.

**Key decision point.** The single genuinely creative move is the *definition of the trivialisation from a local section*. Given a local section $s : U \to G$ of $\pi$, every $g$ over $U$ lies in the same fibre as $s(\pi(g))$; because $H$ acts freely and transitively on that fibre there is a *unique* $h \in H$ with $g = s(\pi(g)) \cdot h$, and this $h = s(\pi(g))^{-1} g$ is the trivialising coordinate. Recognising that "unique group element carrying the section's value to the given point" is the correct definition — and that it is automatically equivariant because right-multiplying $g$ by $h'$ right-multiplies that unique element by $h'$ — is the crux. The subtlety one must not skip is verifying $s(\pi(g))^{-1} g \in H$ (not just in $G$): it holds precisely because $g$ and $s(\pi(g))$ have the same image under $\pi$, so their ratio is in the fibre $H$.

---

# Legal Operations Used

The Gauge Theory III topic page's Legal Operations are the reference numbering; until that page is assembled the operations are named descriptively here and the orchestrator will reconcile the numbers.

1. **Import a manifold structure and a submersion from a structural theorem.** Rather than build charts on $G/H$ by hand, invoke the homogeneous-space theorem to obtain the smooth structure, the submersion $\pi$, and the free proper right $H$-action in one stroke.

2. **Verify freeness and fibre-transitivity by group cancellation.** The group axioms alone give: $gh = g \Rightarrow h = e$ (free), and any two points of a coset $gH$ differ by right multiplication by an element of $H$ (transitive on fibres).

3. **Build an equivariant local trivialisation from a local section of the submersion.** Use the local-section corollary of the submersion theorem to get $s : U \to G$, then define $\psi_U(g) = (\pi(g), s(\pi(g))^{-1} g)$; freeness and transitivity make the second coordinate well defined and equivariance automatic.

4. **Recognise a homogeneous space via orbit–stabiliser.** For the special cases, exhibit $S^2$ as an orbit of a transitive group action and compute the stabiliser to identify the structure group $H$.

---

# Hints

> [!note]- Hint 1
> Almost all the analytic difficulty is already done for you. [[Thm - Homogeneous Space is a Smooth Manifold|The homogeneous-space theorem]] says $G/H$ is a smooth manifold, $\pi : G \to G/H$ is a smooth submersion, and the right $H$-action on $G$ is smooth, free, and proper. Which clauses of "principal bundle" does that already deliver, and which one does it *not* directly deliver?

> [!note]- Hint 2
> The clause it does not deliver directly is local triviality with *equivariant* charts. A submersion has local sections (the Local Section Theorem). If $s : U \to G$ is a smooth section of $\pi$ over an open $U \subseteq G/H$, how could you use $s$, together with freeness and transitivity of $H$ on fibres, to assign to each $g \in \pi^{-1}(U)$ a well-defined element of $H$?

> [!note]- Hint 3
> For $g \in \pi^{-1}(U)$, the points $g$ and $s(\pi(g))$ lie in the same fibre $\pi^{-1}(\pi(g)) = \pi(g) = (\text{a coset})$. So $s(\pi(g))^{-1} g$ lies in $H$ (check: apply $\pi$). Define $\psi_U(g) := (\pi(g),\, s(\pi(g))^{-1} g) \in U \times H$. Show it is a diffeomorphism by writing down its inverse, and show equivariance by replacing $g$ with $gh'$.

> [!note]- Hint 4
> Inverse: $(\bar g, h) \mapsto s(\bar g)\, h$. Equivariance: $\psi_U(g h') = (\pi(gh'),\, s(\pi(gh'))^{-1} g h')$; since $\pi(gh') = \pi(g)$, this equals $(\pi(g),\, (s(\pi(g))^{-1} g) h') = \psi_U(g) \cdot h'$. For the special cases: $\mathrm{SO}(3)$ acts transitively on $S^2$ with the stabiliser of a point a copy of $\mathrm{SO}(2)$; $\mathrm{SU}(2)$ acts transitively on $\mathbb{CP}^1 = S^2$ with stabiliser the diagonal $U(1)$.

---

# Solution

The strategy is to let [[Thm - Homogeneous Space is a Smooth Manifold|the homogeneous-space theorem]] carry the analytic weight — it provides the manifold $G/H$, the submersion $\pi$, and the smooth free proper right $H$-action — and then to verify the remaining, purely algebraic clauses of the principal-bundle definition by hand. The one construction that is not handed to us is the family of *equivariant* local trivialisations, and we build each of them from a local section of the submersion $\pi$: freeness and transitivity of $H$ on the fibres turn a section into a coordinate valued in $H$, and equivariance is then automatic.

**Step 0: Fix the imported structure.**

$G/H$ is a smooth manifold, $\pi : G \to G/H$ is a smooth submersion, and the right translation action of $H$ on $G$ is smooth, free, and proper.

> [!note]- Derivation
> Because $H$ is a closed subgroup of the Lie group $G$, [[Thm - Homogeneous Space is a Smooth Manifold|the homogeneous-space theorem]] applies: $G/H$ carries a unique smooth manifold structure of dimension $\dim G - \dim H$ for which the projection $\pi : G \to G/H$, $\pi(g) = gH$, is a smooth submersion, and the right $H$-action on $G$ by $g \cdot h = gh$ is smooth, free, and proper. We take this as given (its own page carries the complete proof); everything below uses only these consequences, invoked by name.

**Step 1: The right $H$-action on $G$ is smooth and free.**

Smoothness is the restriction of group multiplication; freeness is left cancellation.

> [!note]- Derivation
> *Smoothness.* The action map $G \times H \to G$, $(g, h) \mapsto gh$, is the restriction to $G \times H \subseteq G \times G$ of the smooth multiplication map $m : G \times G \to G$; a restriction of a smooth map to an embedded submanifold ($H$ is an embedded submanifold of $G$ by the closed-subgroup theorem, imported through Step 0) is smooth. Hence the action is smooth.
>
> *Freeness.* Suppose $g \cdot h = g$ for some $g \in G$, $h \in H$, that is $gh = g$. Left-multiplying by $g^{-1} \in G$ gives $h = g^{-1}(gh) = g^{-1} g = e$ (associativity and the inverse axiom). Thus the only element of $H$ fixing any $g$ is the identity, so the action is free. (This also follows from Step 0, which asserts freeness; we include the one-line proof for self-containedness.)

**Step 2: The action preserves fibres and is transitive on each fibre.**

Right multiplication by $h \in H$ does not change the coset, and any two points of a coset differ by such a multiplication.

> [!note]- Derivation
> *Preserves fibres.* For $g \in G$ and $h \in H$,
> $$\pi(g \cdot h) = \pi(gh) = (gh)H = g(hH) = gH = \pi(g) \qquad \text{(associativity; and } hH = H \text{ since } h \in H\text{).}$$
> So the $H$-orbit of $g$ stays inside the fibre $\pi^{-1}(\pi(g))$.
>
> *Fibres are exactly the orbits (transitivity on fibres).* The fibre over $\bar g = gH$ is
> $$\pi^{-1}(gH) = \{g' \in G : g'H = gH\} = \{g' \in G : g^{-1} g' \in H\} = \{g h : h \in H\} = g \cdot H,$$
> where the middle equality is the standard characterisation of coset equality ($g'H = gH \iff g^{-1}g' \in H$). Thus the fibre over $gH$ is precisely the orbit $g \cdot H$, so $H$ acts transitively on it. Combined with freeness (Step 1), the orbit map $H \to \pi^{-1}(gH)$, $h \mapsto g \cdot h$, is a bijection; each fibre is a copy of $H$.

**Step 3: Construct an equivariant local trivialisation around each point.**

Every $\bar g_0 \in G/H$ has a neighbourhood $U$ with a smooth section $s : U \to G$ of $\pi$, and $\psi_U(g) := (\pi(g),\, s(\pi(g))^{-1} g)$ is an $H$-equivariant diffeomorphism $\pi^{-1}(U) \to U \times H$.

> [!note]- Derivation
> Fix $\bar g_0 \in G/H$ and any $g_0 \in G$ with $\pi(g_0) = \bar g_0$. Since $\pi$ is a submersion (Step 0), the **Local Section Theorem** ([[Thm - Local Submersion Theorem|corollary of the local submersion theorem]]) provides an open neighbourhood $U$ of $\bar g_0$ in $G/H$ and a smooth section $s : U \to G$ with $\pi \circ s = \operatorname{id}_U$ and $s(\bar g_0) = g_0$.
>
> *The second coordinate lands in $H$.* For $g \in \pi^{-1}(U)$ put $\bar g := \pi(g) \in U$. Then $s(\bar g)$ and $g$ satisfy $\pi(s(\bar g)) = \bar g = \pi(g)$, so they lie in the same fibre; by the coset characterisation of Step 2,
> $$s(\bar g)^{-1} g \in H \qquad \text{(since } \pi(s(\bar g)) = \pi(g) \iff s(\bar g)^{-1} g \in H\text{).}$$
> Define
> $$\psi_U : \pi^{-1}(U) \to U \times H, \qquad \psi_U(g) := \big(\pi(g),\ s(\pi(g))^{-1} g\big).$$
> *Smoothness.* The map $g \mapsto s(\pi(g))^{-1} g$ is a composition of the smooth maps $\pi$, $s$, inversion, and multiplication on $G$, hence smooth as a map into $G$; since it factors through the embedded submanifold $H$, and $H$ is embedded, it is smooth as a map into $H$. Together with the smooth $\pi$, $\psi_U$ is smooth.
> *Bijectivity, with smooth inverse.* Define $\Phi : U \times H \to \pi^{-1}(U)$ by $\Phi(\bar g, h) := s(\bar g) \cdot h$; it is smooth (multiplication and the smooth $s$) and lands in $\pi^{-1}(U)$ because $\pi(s(\bar g) h) = \pi(s(\bar g)) = \bar g \in U$ (Step 2). Now
> $$\psi_U(\Phi(\bar g, h)) = \psi_U(s(\bar g) h) = \big(\pi(s(\bar g) h),\ s(\pi(s(\bar g)h))^{-1} s(\bar g) h\big) = \big(\bar g,\ s(\bar g)^{-1} s(\bar g) h\big) = (\bar g, h),$$
> using $\pi(s(\bar g)h) = \bar g$; and
> $$\Phi(\psi_U(g)) = \Phi\big(\pi(g),\ s(\pi(g))^{-1} g\big) = s(\pi(g)) \cdot \big(s(\pi(g))^{-1} g\big) = g.$$
> Hence $\psi_U$ and $\Phi$ are mutually inverse smooth maps, so $\psi_U$ is a diffeomorphism.
> *Equivariance.* For $g \in \pi^{-1}(U)$ and $h' \in H$, using $\pi(g h') = \pi(g)$ (Step 2),
> $$\psi_U(g \cdot h') = \big(\pi(gh'),\ s(\pi(gh'))^{-1} g h'\big) = \big(\pi(g),\ (s(\pi(g))^{-1} g)\, h'\big) = \psi_U(g) \cdot h',$$
> where $H$ acts on $U \times H$ by right multiplication on the second factor. This is exactly the equivariance clause.

**Step 4: Assemble the four clauses into "principal $H$-bundle".**

The equivariant trivialisations of Step 3, covering $G/H$, make $\pi$ a smooth fibre bundle with fibre $H$; together with Steps 1–2 all four clauses hold.

> [!note]- Derivation
> The neighbourhoods $U$ from Step 3, taken over all $\bar g_0 \in G/H$, form an open cover of $G/H$; over each, $\psi_U : \pi^{-1}(U) \to U \times H$ is a diffeomorphism commuting with the projections to $U$ (the first coordinate of $\psi_U$ is $\pi$). Hence $\pi : G \to G/H$ is a smooth fibre bundle with typical fibre $H$ (clause 1). The right $H$-action is smooth and free (Step 1, clause 2), preserves fibres and is transitive on each (Step 2, clause 3), and the trivialisations $\psi_U$ are $H$-equivariant (Step 3, clause 4). All four defining clauses of a [[Def - Principal G-Bundle|principal $H$-bundle]] hold.

> [!note]- Complete formal solution
> **Claim.** For a Lie group $G$ and a closed subgroup $H \leq G$, the projection $\pi : G \to G/H$ with the right-translation $H$-action is a principal $H$-bundle.
>
> By [[Thm - Homogeneous Space is a Smooth Manifold|the homogeneous-space theorem]] (applicable since $H$ is closed), $G/H$ is a smooth manifold, $\pi$ is a smooth submersion, and the right $H$-action on $G$ is smooth, free, and proper.
>
> *Free and smooth (clause 2).* The action map is the restriction of the smooth multiplication of $G$ to $G \times H$, hence smooth; and $gh = g$ implies $h = e$ by left cancellation, so it is free.
>
> *Preserves fibres, transitive on fibres (clause 3).* $\pi(gh) = (gh)H = gH = \pi(g)$ since $hH = H$; and $\pi^{-1}(gH) = \{g' : g^{-1}g' \in H\} = gH = g \cdot H$, so each fibre is a single free orbit, a copy of $H$.
>
> *Equivariant local triviality (clauses 1 and 4).* Fix $\bar g_0 \in G/H$. As $\pi$ is a submersion, the Local Section Theorem gives an open $U \ni \bar g_0$ and a smooth section $s : U \to G$ with $\pi \circ s = \operatorname{id}_U$. For $g \in \pi^{-1}(U)$, $\pi(s(\pi(g))) = \pi(g)$ forces $s(\pi(g))^{-1} g \in H$, so
> $$\psi_U(g) := \big(\pi(g),\ s(\pi(g))^{-1} g\big) \in U \times H$$
> is defined; it is smooth (composition of smooth maps, factoring through the embedded $H$), with smooth inverse $(\bar g, h) \mapsto s(\bar g) h$, hence a diffeomorphism, and $\psi_U(gh') = (\pi(g), (s(\pi(g))^{-1}g)h') = \psi_U(g) h'$ for $h' \in H$, so it is $H$-equivariant. These $\psi_U$ cover $G/H$, making $\pi$ a smooth fibre bundle with fibre $H$.
>
> All four clauses hold, so $\pi : G \to G/H$ is a principal $H$-bundle. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to assert local triviality "because $\pi$ is a submersion and submersions are locally products." A submersion is *locally* a projection in the sense of the [[Thm - Local Submersion Theorem|submersion normal form]], but that normal form gives a chart in which $\pi$ looks like $(x, y) \mapsto x$ — it does **not** by itself supply an $H$-*equivariant* trivialisation, nor does it identify the fibre coordinate with the group $H$. Skipping to "locally a product" therefore proves clause 1 in a form too weak for clause 4. The equivariance is the whole point of a *principal* bundle, and it is obtained only by using freeness and transitivity to read the fibre coordinate as a genuine element of $H$ — which is what the local-section construction does. The extra ingredient that upgrades a bare submersion chart to an equivariant one is exactly the free transitive $H$-action on fibres.

> [!note]- Special cases: $\mathrm{SO}(3) \to S^2$ and $\mathrm{SU}(2) \to S^2$
> **$\mathrm{SO}(3) \to S^2$ is a principal $\mathrm{SO}(2)$-bundle.** The group $\mathrm{SO}(3)$ acts on $S^2 = \{x \in \mathbb{R}^3 : |x| = 1\}$ by rotations; the action is transitive (any unit vector can be rotated to any other). Fix the north pole $e_3 = (0,0,1)$. Its stabiliser is $\{R \in \mathrm{SO}(3) : R e_3 = e_3\}$, the rotations fixing the $z$-axis, which is a copy of $\mathrm{SO}(2) \cong U(1)$. By [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit–stabiliser]], the orbit map $\mathrm{SO}(3)/\mathrm{SO}(2) \to S^2$, $R\,\mathrm{SO}(2) \mapsto R e_3$, is a diffeomorphism. Applying the main result with $G = \mathrm{SO}(3)$, $H = \mathrm{SO}(2)$ shows $\mathrm{SO}(3) \to \mathrm{SO}(3)/\mathrm{SO}(2) = S^2$ is a principal $\mathrm{SO}(2)$-bundle (this is the oriented orthonormal frame bundle of $S^2$).
>
> **$\mathrm{SU}(2) \to S^2$ is a principal $U(1)$-bundle — the Hopf bundle.** The group $\mathrm{SU}(2)$ acts on $\mathbb{CP}^1 \cong S^2$ (through its standard action on $\mathbb{C}^2$, which descends to lines); the action is transitive. The stabiliser of the line $[1 : 0]$ is the diagonal subgroup $\big\{\operatorname{diag}(e^{i\theta}, e^{-i\theta}) : \theta \in \mathbb{R}\big\} \cong U(1)$. By orbit–stabiliser, $\mathrm{SU}(2)/U(1) \cong \mathbb{CP}^1 = S^2$, so $\mathrm{SU}(2) \to S^2$ is a principal $U(1)$-bundle. Since $\mathrm{SU}(2) \cong S^3$ (see [[Ex - SU(2) is Diffeomorphic to S^3|$\mathrm{SU}(2) \cong S^3$]]), this is exactly the **Hopf bundle** $S^3 \to S^2$; it is treated in full, with its non-triviality and Chern number, on [[Def - The Hopf Bundle|the Hopf bundle page]]. This is the forward reference the section promises.

---

# Key Takeaways

**A submersion equipped with a free, fibrewise-transitive right $G$-action is automatically a principal $G$-bundle, and the equivariant charts come from local sections.** The reusable principle is a promotion rule: whenever one has a smooth surjective submersion $\pi : P \to M$ together with a smooth free right $G$-action whose orbits are exactly the fibres of $\pi$, the bundle is principal, and one never has to guess trivialisations — each local section $s : U \to P$ of the submersion yields the equivariant chart $\psi_U(p) = (\pi(p),\, \text{the unique } g \text{ with } p = s(\pi(p)) \cdot g)$. The trigger to recognise is "free action whose orbits are the fibres of a submersion." The transferable diagnostic is that the *uniqueness* of the group element (freeness) is what makes the fibre coordinate well defined, and *transitivity on fibres* is what makes it cover the whole fibre; drop either and the chart construction breaks. This same promotion rule is what makes the frame bundle of a vector bundle, the quotient of a manifold by a free proper action ([[Thm - Homogeneous Space is a Smooth Manifold|the quotient-manifold theorem]]), and every homogeneous space into principal bundles.

**Closedness of the subgroup is the one hypothesis that is genuinely analytic, and it is quarantined in the imported theorem.** The entire proof after Step 0 uses only the group axioms and the abstract local-section property of submersions; the only place a topological hypothesis enters is closedness of $H$, which the homogeneous-space theorem needs to make the quotient a manifold at all (properness of the right action). The instructive contrast is the dense one-parameter subgroup: the irrational-slope line $\mathbb{R} \hookrightarrow T^2$ is a non-closed subgroup, its right action is not proper, and $T^2/\mathbb{R}$ is not a manifold — so there is no principal bundle. The lesson for spaced practice is to remember *where* each hypothesis is spent: closedness buys the manifold and the submersion (once), and thereafter the bundle structure is pure algebra plus the universal local-section trick. When you reconstruct this proof, the reconstruction hinges on "closedness $\Rightarrow$ homogeneous-space theorem $\Rightarrow$ submersion; then local sections do the rest."

**Homogeneous spaces are the master source of examples of principal bundles, and orbit–stabiliser is the tool that recognises a given space as one.** Every space of the form "manifold with a transitive smooth $G$-action" is a homogeneous space $G/G_p$ for the (closed) stabiliser $G_p$ of any basepoint, by [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit–stabiliser]], and hence sits atop a principal $G_p$-bundle $G \to G/G_p$. This is how the two spheres above are recognised: $S^2 = \mathrm{SO}(3)/\mathrm{SO}(2)$ gives the frame bundle, and $S^2 = \mathrm{SU}(2)/U(1)$ gives the Hopf bundle $S^3 \to S^2$, the smallest non-trivial principal $U(1)$-bundle and the running example of the whole series (its non-triviality obstructs a global section, and its first Chern number is $-1$, computed on [[Def - The Hopf Bundle|the Hopf bundle page]]). The transferable pattern: to see a manifold as the base of a principal bundle, look for a Lie group acting transitively on the *total space above it* with the desired structure group as stabiliser, or on the base with the fibre as the group over it; orbit–stabiliser then hands you the bundle. The companion result [[Thm - Sections of a Principal Bundle and Triviality|sections versus triviality]] shows the payoff: $G \to G/H$ is trivial if and only if it has a global section, which for the Hopf bundle it does not.
