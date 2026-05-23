---
type: theorem
subject: group-theory
prereqs:
  - "Def - Subgroup"
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group and $K \trianglelefteq G$ is a [[Def - Normal Subgroup|normal subgroup]], so the [[Def - Quotient Group|quotient]] $G/K$ is defined. The quotient homomorphism is $\pi : G \to G/K$, $g \mapsto gK$. For a subgroup $X \leq G/K$, its **preimage** is $\pi^{-1}(X) = \{g \in G : gK \in X\}$. For a subgroup $L$ of $G$ with $K \leq L$, its **image** is $\pi(L) = L/K = \{\ell K : \ell \in L\} \leq G/K$. The index of $H$ in $G$ is written $|G : H|$. The full registry is on the parent page [[Group Theory I — §1.1–1.2]].

---

# Statement

> **Correspondence Theorem (Lattice Isomorphism Theorem).** Let $K \trianglelefteq G$, with quotient map $\pi : G \to G/K$. The assignments
> $$L \;\longmapsto\; L/K = \pi(L), \qquad\qquad X \;\longmapsto\; \pi^{-1}(X) = \{g \in G : gK \in X\}$$
> are mutually inverse bijections between
> $$\{\text{subgroups } L \text{ of } G \text{ with } K \leq L\} \quad\longleftrightarrow\quad \{\text{subgroups } X \text{ of } G/K\}.$$
> This bijection
> 1. **preserves inclusion**: $L_1 \leq L_2 \iff L_1/K \leq L_2/K$;
> 2. **preserves normality**: $L \trianglelefteq G \iff L/K \trianglelefteq G/K$;
> 3. **preserves index**: $|G : L| = |G/K : L/K|$, and for $K \leq L_1 \leq L_2$, $|L_2 : L_1| = |L_2/K : L_1/K|$.

---

# Motivation

Quotienting by a normal subgroup $K$ replaces $G$ with the smaller, hopefully simpler group $G/K$. But "simpler" is only useful if you can still *say something* about $G/K$ — and the most basic things one wants to know about any group are its [[Def - Subgroup|subgroups]], which of them are normal, and how big they are. The correspondence theorem answers all three questions about $G/K$ in a single stroke: it says you do not need to study $G/K$ from scratch, because its entire subgroup structure is *already visible* inside $G$.

Precisely: the [[Def - Subgroup|subgroups]] of $G/K$ are in perfect bijection with the subgroups of $G$ that contain $K$. Not just in bijection as bare sets — the bijection respects everything you care about. If one subgroup contains another upstairs in $G$, the same containment holds for their images downstairs in $G/K$, and vice versa: the bijection is an isomorphism of the *lattices* of subgroups (which is why it is also called the lattice isomorphism theorem). Normal subgroups correspond to normal subgroups. Indices are preserved on the nose. So passing to $G/K$ does not scramble or destroy the subgroup lattice — it simply *truncates* it, deleting every subgroup that fails to contain $K$ and keeping the rest, structure intact.

This is the precise sense in which "quotient to simplify" is a *safe* operation. When you replace $G$ by $G/K$, you genuinely lose information — you can no longer see anything below $K$ — but the surviving structure is faithfully preserved. That guarantee is what licenses **induction on the order of a group**, the single most important proof strategy in finite group theory. You find a proper non-trivial normal subgroup $K$, pass to the strictly smaller $G/K$, solve the problem there, and then pull the conclusion back up — and the correspondence theorem is exactly the tool that makes the pull-back rigorous, because it tells you what each subgroup of $G/K$ *is* as a subgroup of $G$. It is the engine behind the existence of [[Thm - Composition Series|composition series]] and behind essentially every structural theorem about $p$-[[Def - Group|groups]] and solvable [[Def - Group|groups]].

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is simply "$K \trianglelefteq G$". The disguised-source question is: when does a problem hand you a normal subgroup whose quotient you should analyse via the correspondence?

The first source is **$K = \ker\varphi$ for a homomorphism $\varphi : G \to A$**. Every kernel is normal, so any homomorphism out of $G$ supplies a $K$, and the correspondence theorem then describes the subgroups of $G/\ker\varphi \cong \operatorname{im}\varphi$. The non-obvious step is recognising that to understand the subgroups of the *image* of a homomorphism, you study the subgroups of $G$ containing the kernel. *Example problem:* classify the subgroups of $\operatorname{im}\varphi$ by classifying the subgroups of $G$ above $\ker\varphi$.

The second source is **a maximal normal subgroup $K$**. In a finite non-simple group, a proper normal subgroup of maximal order exists. By the correspondence theorem, $G/K$ then has *no* proper non-trivial normal subgroup — because any such would correspond to a normal subgroup of $G$ strictly between $K$ and $G$, contradicting maximality — so $G/K$ is [[Def - Simple Group|simple]]. The non-obviousness is that "maximal among proper normal subgroups" translates, through the correspondence, into "the quotient is simple". *Example problem:* this is the inductive step of [[Thm - Composition Series]].

The third source is **the centre $Z(G)$ or any characteristic subgroup**. These are always normal, so they are always legal choices of $K$, and the correspondence theorem describes the subgroup lattice of $G/Z(G)$. The non-obvious payoff is that facts about subgroups of $G/Z(G)$ — for instance that $G/Z(G)$ cyclic forces $G$ abelian — are proved by transporting subgroups across the correspondence. *Example problem:* analyse $G/Z(G)$ to constrain $G$.

**Targets (Output Amplification)**

The conclusion is an inclusion-, normality-, and index-preserving bijection between two subgroup lattices.

Combine the conclusion with **a normal subgroup found inside the quotient**. If, working in $G/K$, you locate a normal subgroup $X \trianglelefteq G/K$, the correspondence theorem hands you back a normal subgroup $L = \pi^{-1}(X) \trianglelefteq G$ with $K \leq L$. The further result $E$ is a normal subgroup of the *original* group $G$, manufactured by working in the smaller quotient — this is the descent–ascent step that makes induction on $|G|$ work, and it is non-obvious because the subgroup of $G$ is produced indirectly, via a computation in $G/K$.

Combine the conclusion with **the correspondence applied iteratively**. Once you have $L$ with $K \leq L \leq G$, the correspondence also matches the subgroups of $G$ *between* $K$ and $L$ with the subgroups of $L/K$. Combined with the [[Thm - Third Isomorphism Theorem|third isomorphism theorem]] (which computes $\dfrac{G/K}{L/K} \cong G/L$), the further result is a complete dictionary between chains of subgroups in $G$ above $K$ and chains in $G/K$. This is non-obvious and is exactly what is needed to refine, compare, and build normal series.

Combine the conclusion with **a counting argument**. Because index is preserved, $|G : L| = |G/K : L/K|$: a subgroup of small index in $G$ corresponds to a subgroup of the same small index in $G/K$, and conversely. The further result is that index data transfers freely between a group and its quotient, so an index obstruction proved downstairs (e.g. "no subgroup of index $2$") immediately constrains $G$ upstairs.

---

# Why Is It True

The theorem feels like it should be true, and the reason is geometric. Picture the quotient map $\pi : G \to G/K$. It bundles $G$ into the [[Def - Coset|cosets]] of $K$ — disjoint blocks, each a translate of $K$ — and $G/K$ is the set of these blocks. A subgroup $X$ of $G/K$ is a collection of blocks closed under the group operation.

Now here is the key point. Take a subgroup $X \leq G/K$ and form its preimage $\pi^{-1}(X)$ — the union in $G$ of all the blocks belonging to $X$. Because the identity block $K$ always belongs to $X$, this preimage *contains $K$*. And because $X$ is a subgroup, the preimage is a subgroup of $G$. So preimages of subgroups of $G/K$ are exactly subgroups of $G$ containing $K$ — they are *unions of whole blocks*, never a partial block.

Conversely, take a subgroup $L$ of $G$ that contains $K$. Since $L$ contains $K$, and $K$ is a single block, $L$ must be a union of *whole blocks*: if $L$ contains one element of a coset $gK$, then it contains $gk$ for that element and, multiplying by all of $K \subseteq L$, the entire coset $gK$. A subgroup containing $K$ cannot slice a block in half. So $L$ is a clean union of blocks, and the set of blocks it comprises is exactly $L/K$, a subgroup of $G/K$.

That is the whole theorem. Subgroups of $G$ containing $K$ are precisely the **block-unions**, and block-unions are precisely the things that have a well-defined image in $G/K$ and a well-defined preimage from $G/K$. The two operations "take image" and "take preimage" are inverse because forming the union of a set of blocks and then asking which blocks you used returns the same set of blocks. The condition "$L$ contains $K$" is not a technicality — it is *exactly* the condition that $L$ respects the block structure, and only block-respecting subgroups can correspond to anything downstairs. A subgroup not containing $K$ would cut across [[Def - Coset|cosets]], and its image in $G/K$ would forget that, so the correspondence would not be injective without the containment restriction.

Once you see subgroups-above-$K$ as block-unions, the three preservation properties are obvious too. *Inclusion*: one union of blocks sits inside another if and only if its block-set does — set containment is set containment. *Index*: the cosets of $L$ in $G$ are themselves unions of blocks, and they biject with the cosets of $L/K$ in $G/K$, so the counts agree. *Normality*: conjugation in $G$ permutes the blocks the same way conjugation in $G/K$ does (because $\pi$ is a surjective homomorphism), so $L$ is conjugation-invariant in $G$ exactly when $L/K$ is conjugation-invariant in $G/K$.

---

# What Makes This Hard

The conceptual crux is *why the containment $K \leq L$ is exactly the right restriction* — that a subgroup contains $K$ if and only if it is a union of whole $K$-cosets, so that only such subgroups have a faithful image in $G/K$; people often state the theorem without internalising that subgroups *not* containing $K$ are precisely the ones the correspondence must exclude. The most common error is to believe the bijection works for *all* subgroups of $G$: it does not — many subgroups of $G$ have the same image in $G/K$, and injectivity is recovered only after restricting to those above $K$. A second subtlety is the index claim: it is tempting to think quotienting changes indices (it changes group orders), but the index $|G:L|$ is preserved because the cosets themselves correspond, and forgetting this leads to mis-stated counting arguments.

---

# Rederivation Scaffold

**High-level strategy:**
Work with the quotient map $\pi : G \to G/K$. Show "image" and "preimage" land in the right places, show they are mutually inverse (so the correspondence is a bijection), then verify the three preservation properties by unwinding definitions. The recurring lemma is that a subgroup of $G$ contains $K$ if and only if it is a union of $K$-cosets.

**Subgoal decomposition:**

1. **Preimage gives a subgroup containing $K$.** For $X \leq G/K$, show $\pi^{-1}(X) \leq G$ and $K \subseteq \pi^{-1}(X)$.
   - *Hint:* Preimages of subgroups under any homomorphism are subgroups; $K = \pi^{-1}(\{e_{G/K}\}) \subseteq \pi^{-1}(X)$ since $X$ contains the identity coset.
   - *Why needed:* Shows the map $X \mapsto \pi^{-1}(X)$ has the claimed codomain.

2. **Image gives a subgroup of $G/K$.** For $K \leq L \leq G$, show $L/K = \pi(L) \leq G/K$.
   - *Hint:* Images of subgroups under any homomorphism are subgroups.
   - *Why needed:* Shows the map $L \mapsto L/K$ has the claimed codomain.

3. **The maps are mutually inverse.** Show $\pi^{-1}(\pi(L)) = L$ for $K \leq L$, and $\pi(\pi^{-1}(X)) = X$.
   - *Hint:* The first uses the key lemma — $L$ being a union of $K$-cosets means no extra elements are picked up; the containment $K \subseteq L$ is essential here. The second uses surjectivity of $\pi$.
   - *Why needed:* This is the bijection itself — the heart of the theorem.

4. **Inclusion is preserved.** Show $L_1 \leq L_2 \iff L_1/K \leq L_2/K$.
   - *Hint:* Forward by applying $\pi$; backward by applying $\pi^{-1}$ and using step 3.
   - *Why needed:* Upgrades the bijection of sets to an isomorphism of lattices.

5. **Normality is preserved.** Show $L \trianglelefteq G \iff L/K \trianglelefteq G/K$.
   - *Hint:* $\pi$ is a surjective homomorphism, so it carries conjugation in $G$ onto conjugation in $G/K$; check $gLg^{-1} \subseteq L$ transports to $\pi(g)(L/K)\pi(g)^{-1} \subseteq L/K$ and back.
   - *Why needed:* Restricts the correspondence to normal subgroups, as used in induction.

6. **Index is preserved.** Show $|G : L| = |G/K : L/K|$.
   - *Hint:* Exhibit a bijection between cosets of $L$ in $G$ and cosets of $L/K$ in $G/K$ via $gL \mapsto (gK)(L/K)$; check well-defined and bijective.
   - *Why needed:* Makes the correspondence quantitative, enabling counting arguments.

---

# Lemma Decomposition

> [!note]- Lemma 1: A subgroup of $G$ contains $K$ if and only if it is a union of $K$-cosets
> **Statement:** Let $K \trianglelefteq G$ and $L \leq G$. Then $K \subseteq L$ if and only if $L$ is a union of left cosets of $K$, equivalently $L = \pi^{-1}(\pi(L))$.
>
> **Hint:** If $K \subseteq L$ and $\ell \in L$, then the whole coset $\ell K \subseteq L$ by closure; conversely any union of cosets that is a subgroup contains the identity coset $K$.
>
> **Why needed:** This is the structural fact that makes "image" and "preimage" mutually inverse — the core of the correspondence. The hypothesis $K \subseteq L$ enters here.
>
> > [!note]- Full proof
> > ($\Rightarrow$) Suppose $K \subseteq L$. Take any $\ell \in L$. For every $k \in K$ we have $k \in L$, so $\ell k \in L$ by closure of $L$. Hence $\ell K \subseteq L$. Therefore $L = \bigcup_{\ell \in L} \ell K$ is a union of $K$-cosets. Consequently $\pi^{-1}(\pi(L)) = \{g : gK \in \pi(L)\} = \bigcup_{\ell \in L}\ell K = L$.
> >
> > ($\Leftarrow$) Suppose $L$ is a union of $K$-cosets and $L \leq G$. Since $e \in L$, the coset $eK = K$ is one of the cosets comprising $L$, so $K \subseteq L$.

> [!note]- Lemma 2: Images and preimages of subgroups under a homomorphism are subgroups
> **Statement:** Let $\pi : G \to G'$ be a homomorphism. If $L \leq G$ then $\pi(L) \leq G'$; if $X \leq G'$ then $\pi^{-1}(X) \leq G$, and $\pi^{-1}(X) \supseteq \ker\pi$.
>
> **Hint:** Apply the subgroup criterion, pushing it through $\pi$ in each direction.
>
> **Why needed:** It guarantees that "image" and "preimage" actually produce subgroups, so the two sides of the correspondence are sets of subgroups.
>
> > [!note]- Full proof
> > *Image.* $\pi(L)$ contains $\pi(e_G) = e_{G'}$. For $\pi(a), \pi(b) \in \pi(L)$ with $a, b \in L$, $\pi(a)\pi(b)^{-1} = \pi(ab^{-1})$ and $ab^{-1} \in L$, so $\pi(a)\pi(b)^{-1} \in \pi(L)$. By the subgroup criterion $\pi(L) \leq G'$.
> >
> > *Preimage.* $\pi^{-1}(X)$ contains $e_G$ since $\pi(e_G) = e_{G'} \in X$. For $a, b \in \pi^{-1}(X)$, $\pi(ab^{-1}) = \pi(a)\pi(b)^{-1} \in X$ (as $X$ is a subgroup), so $ab^{-1} \in \pi^{-1}(X)$. By the subgroup criterion $\pi^{-1}(X) \leq G$. Finally, if $g \in \ker\pi$ then $\pi(g) = e_{G'} \in X$, so $g \in \pi^{-1}(X)$; hence $\ker\pi \subseteq \pi^{-1}(X)$.

> [!note]- Lemma 3: The correspondence preserves normality
> **Statement:** With $K \trianglelefteq G$ and $K \leq L \leq G$: $L \trianglelefteq G$ if and only if $L/K \trianglelefteq G/K$.
>
> **Hint:** Use that $\pi$ is surjective, so every element of $G/K$ is $\pi(g)$, and $\pi(gLg^{-1}) = \pi(g)\,\pi(L)\,\pi(g)^{-1}$.
>
> **Why needed:** It is the property that lets the correspondence be restricted to normal subgroups — the version used in inductive proofs and in [[Thm - Composition Series|composition series]].
>
> > [!note]- Full proof
> > ($\Rightarrow$) Suppose $L \trianglelefteq G$. Let $x \in G/K$ and write $x = \pi(g)$ (possible since $\pi$ is surjective). Then
> > $$x\,(L/K)\,x^{-1} = \pi(g)\,\pi(L)\,\pi(g)^{-1} = \pi(gLg^{-1}) = \pi(L) = L/K,$$
> > using that $\pi$ is a homomorphism and $gLg^{-1} = L$. So $L/K \trianglelefteq G/K$.
> >
> > ($\Leftarrow$) Suppose $L/K \trianglelefteq G/K$. Let $g \in G$. Then $\pi(gLg^{-1}) = \pi(g)\,(L/K)\,\pi(g)^{-1} = L/K = \pi(L)$. Applying $\pi^{-1}$ and using Lemma 1 (both $gLg^{-1}$ and $L$ contain $K$ — note $gKg^{-1} = K$ since $K \trianglelefteq G$, so $K \subseteq gLg^{-1}$): $gLg^{-1} = \pi^{-1}(\pi(gLg^{-1})) = \pi^{-1}(\pi(L)) = L$. So $L \trianglelefteq G$.

> [!note]- Lemma 4: The correspondence preserves index
> **Statement:** With $K \trianglelefteq G$ and $K \leq L \leq G$: $|G : L| = |G/K : L/K|$.
>
> **Hint:** Map a coset $gL$ to the coset $(gK)(L/K)$ of $L/K$ in $G/K$, and show this is a well-defined bijection.
>
> **Why needed:** It makes the correspondence quantitative, so index obstructions transfer between $G$ and $G/K$.
>
> > [!note]- Full proof
> > Define $\Phi$ from the set of left cosets of $L$ in $G$ to the set of left cosets of $L/K$ in $G/K$ by $\Phi(gL) = (gK)(L/K)$.
> >
> > *Well-defined.* If $gL = g'L$ then $g^{-1}g' \in L$, so $\pi(g^{-1}g') = (g^{-1}g')K \in L/K$, hence $(gK)(L/K) = (g'K)(L/K)$.
> >
> > *Injective.* If $(gK)(L/K) = (g'K)(L/K)$ then $(gK)^{-1}(g'K) = (g^{-1}g')K \in L/K$, so $g^{-1}g' \in \pi^{-1}(L/K) = L$ (Lemma 1), giving $gL = g'L$.
> >
> > *Surjective.* A coset of $L/K$ in $G/K$ has the form $x(L/K)$ with $x = gK$ for some $g$ (surjectivity of $\pi$), and then $x(L/K) = \Phi(gL)$.
> >
> > So $\Phi$ is a bijection, and $|G : L| = |G/K : L/K|$. The relative version for $K \leq L_1 \leq L_2$ follows by the same argument applied within $L_2$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $K \trianglelefteq G$ with quotient map $\pi : G \to G/K$, $g \mapsto gK$. Write
> $$\mathcal{S}_G = \{L : K \leq L \leq G\}, \qquad \mathcal{S}_{G/K} = \{X : X \leq G/K\}.$$
>
> **The two maps land correctly.** For $L \in \mathcal{S}_G$, $\pi(L) = L/K$ is a subgroup of $G/K$ by Lemma 2, so $L \mapsto L/K$ maps $\mathcal{S}_G \to \mathcal{S}_{G/K}$. For $X \in \mathcal{S}_{G/K}$, $\pi^{-1}(X)$ is a subgroup of $G$ containing $\ker\pi = K$ by Lemma 2, so $X \mapsto \pi^{-1}(X)$ maps $\mathcal{S}_{G/K} \to \mathcal{S}_G$.
>
> **The maps are mutually inverse.** Let $L \in \mathcal{S}_G$. Since $K \leq L$, Lemma 1 gives $\pi^{-1}(\pi(L)) = L$. Let $X \in \mathcal{S}_{G/K}$. Since $\pi$ is surjective, for any $x \in X$ we have $x = \pi(g)$ for some $g$, and then $g \in \pi^{-1}(X)$, so $x = \pi(g) \in \pi(\pi^{-1}(X))$; conversely $\pi(\pi^{-1}(X)) \subseteq X$ always. Hence $\pi(\pi^{-1}(X)) = X$. So the two maps are mutually inverse bijections $\mathcal{S}_G \leftrightarrow \mathcal{S}_{G/K}$.
>
> **Inclusion is preserved.** Let $L_1, L_2 \in \mathcal{S}_G$. If $L_1 \leq L_2$ then applying $\pi$ gives $L_1/K = \pi(L_1) \subseteq \pi(L_2) = L_2/K$. Conversely if $L_1/K \leq L_2/K$, applying $\pi^{-1}$ and using $\pi^{-1}(\pi(L_i)) = L_i$ gives $L_1 \leq L_2$. So $L_1 \leq L_2 \iff L_1/K \leq L_2/K$, and the bijection is an isomorphism of subgroup lattices.
>
> **Normality is preserved.** This is Lemma 3: $L \trianglelefteq G \iff L/K \trianglelefteq G/K$. Consequently the bijection restricts to a bijection between $\{L : K \leq L \trianglelefteq G\}$ and $\{X : X \trianglelefteq G/K\}$.
>
> **Index is preserved.** This is Lemma 4: $|G : L| = |G/K : L/K|$, and more generally $|L_2 : L_1| = |L_2/K : L_1/K|$ for $K \leq L_1 \leq L_2 \leq G$.
>
> This establishes all claims. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The subgroup lattice of a cyclic group.** The cyclic group $\mathbb{Z}/n\mathbb{Z}$ is $\mathbb{Z}/K$ with $K = n\mathbb{Z}$. The correspondence theorem says its subgroups correspond to subgroups of $\mathbb{Z}$ containing $n\mathbb{Z}$ — that is, to $d\mathbb{Z}$ with $d \mid n$. So the subgroups of $\mathbb{Z}/n\mathbb{Z}$ are indexed by divisors of $n$, with inclusion reversed relative to divisibility, and index $|G/K : L/K| = d$. The application is non-obvious because the divisor lattice of $n$ is usually derived by hand; the correspondence theorem exhibits it as the truncated lattice of $\mathbb{Z}$.

**Reduction in the proof that $A_5$ is simple, used contrapositively.** To prove a finite group $G$ is *not* simple, one often produces a homomorphism $\varphi$ with non-trivial proper kernel. Conversely, to *use* simplicity of a quotient: if $G$ has a maximal proper normal subgroup $K$, the correspondence theorem shows $G/K$ has no proper non-trivial normal subgroup, hence is simple. This translation — "maximal normal subgroup upstairs $\leftrightarrow$ simple quotient downstairs" — is the non-obvious recognition powering the existence half of [[Thm - Composition Series]].

**Intermediate fields in Galois theory.** The Galois correspondence matches intermediate fields of a Galois extension $L/F$ with subgroups of $\operatorname{Gal}(L/F)$. When $E/F$ is itself Galois, $\operatorname{Gal}(L/E) \trianglelefteq \operatorname{Gal}(L/F)$, and the intermediate fields *between $F$ and $E$* correspond to subgroups of the quotient $\operatorname{Gal}(L/F)/\operatorname{Gal}(L/E) \cong \operatorname{Gal}(E/F)$. This last correspondence is the group-theoretic correspondence theorem in disguise; recognising it lets the Galois correspondence for a subextension be deduced from the full one.

**[[Def - Ideal|Ideals]] of a quotient [[Def - Ring|ring]].** The [[Def - Ring|ring]]-theoretic correspondence theorem says the [[Def - Ideal|ideals]] of $R/I$ correspond to ideals of $R$ containing $I$, preserving inclusion and primality. So to find all ideals of $\mathbb{Z}/12\mathbb{Z}$, find the ideals of $\mathbb{Z}$ containing $12\mathbb{Z}$, namely $d\mathbb{Z}$ for $d \mid 12$. The non-obvious step is realising the group correspondence theorem and the ring version are the same statement — a normal subgroup / ideal is precisely a kernel, and the correspondence is about kernels.

---

# Bridges

- **[[Thm - Third Isomorphism Theorem|Third Isomorphism Theorem]]** — its computational partner. The correspondence theorem identifies the subgroups of $G/K$ (and which are normal); the third isomorphism theorem then computes the quotient by each normal one, $(G/K)/(L/K) \cong G/L$. Together they fully describe the quotient lattice of $G/K$ and all its further quotients.

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]]** — applies the correspondence to images. Since $G/\ker\varphi \cong \operatorname{im}\varphi$, the correspondence theorem for $K = \ker\varphi$ describes the subgroups of $\operatorname{im}\varphi$ in terms of subgroups of $G$ above the kernel.

- **[[Thm - Composition Series|Composition Series]]** — the correspondence theorem is the engine of its existence proof: passing to a quotient by a maximal normal subgroup yields a simple quotient *because* the correspondence forbids any intermediate normal subgroup.

- **The lattice isomorphism theorem** — "correspondence theorem" and "lattice isomorphism theorem" are two names for this result; the latter emphasises that the bijection is an isomorphism of the partially ordered sets (lattices) of subgroups, not merely a bijection of underlying sets.

- **Correspondence theorems for rings and modules** — the identical statement holds with "normal subgroup" replaced by "ideal" (for rings) or "submodule" (for modules): the ideals of $R/I$ are the ideals of $R$ containing $I$. The group case is the prototype, and the proof transfers verbatim.
