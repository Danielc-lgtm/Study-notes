---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Group Action"
  - "Def - Subgroup"
  - "Def - Orbit and Stabiliser"
  - "Def - Normaliser"
  - "Thm - Orbit-Stabiliser Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a [[Def - Group|group]] and let $\mathcal{S}$ be the set of all [[Def - Subgroup|subgroups]] of $G$. For $g \in G$ and $H \in \mathcal{S}$, write $g \cdot H = gHg^{-1} = \{ghg^{-1} : h \in H\}$. Prove the following.

1. The rule $(g, H) \mapsto gHg^{-1}$ is a [[Def - Group Action|group action]] of $G$ on $\mathcal{S}$ — in particular, $gHg^{-1}$ is again a subgroup of $G$.
2. The stabiliser of a subgroup $H$ under this action is the **normaliser** $N_G(H)$.
3. If $G$ is finite, the number of [[Def - Subgroup|subgroups]] of $G$ conjugate to $H$ equals the index $|G : N_G(H)|$.

**Recall:**

The objects in play are a [[Def - Group|group]] action, the stabiliser of a point, the normaliser of a subgroup, and the orbit-stabiliser theorem.

![[Def - Group Action#The Definition]]

A [[Def - Group Action|group action]] of $G$ on a set $X$ is a map $G \times X \to X$, $(g, x) \mapsto g \cdot x$, satisfying $e \cdot x = x$ and $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$. Here the set acted on is unusual: it is not a set of points but $\mathcal{S}$, the set whose *elements are themselves subgroups* of $G$.

![[Def - Orbit and Stabiliser#The Definition]]

For an action of $G$ on $X$ and a point $x$, the [[Def - Orbit and Stabiliser|orbit]] $G \cdot x = \{g \cdot x : g \in G\}$ collects everywhere $x$ can be sent, and the **stabiliser** $G_x = \{g : g \cdot x = x\}$ collects the group elements fixing $x$; the stabiliser is always a subgroup.

![[Def - Normaliser#The Definition]]

The [[Def - Normaliser|normaliser]] of a subgroup $H \leq G$ is $N_G(H) = \{g \in G : gHg^{-1} = H\}$ — the elements that conjugate $H$ onto itself. It always satisfies $H \trianglelefteq N_G(H) \leq G$, and $H$ is normal in $G$ exactly when $N_G(H) = G$.

![[Thm - Orbit-Stabiliser Theorem#Statement]]

The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] states that for a finite group $G$ acting on $X$ and any $x \in X$, the map $gG_x \mapsto g \cdot x$ is a bijection from the [[Def - Coset|cosets]] of the stabiliser to the orbit, so $|G \cdot x| = |G : G_x|$ and $|G| = |G_x|\,|G \cdot x|$.

---

# Convergent Strategy

**Problem class.** This exercise is partly *verification* — checking that a proposed rule satisfies the action axioms — and partly *counting*, namely counting the conjugates of a subgroup. It is the exercise that *justifies a definition*: it is where the [[Def - Normaliser|normaliser]] earns its name as "the stabiliser of $H$ under conjugation", and it supplies the conjugate-counting formula listed in the [[Group Theory II — §1.3–1.4#Legal Operations|topic page's Legal Operations]].

**Assumption pattern.** The hypotheses are minimal: just a group $G$ and the demand to act on its set of subgroups. The recognisable feature is the *type of set* being acted on. The conjugation action $g \cdot x = gxg^{-1}$ is usually met with $x$ ranging over elements of $G$, where its orbits are conjugacy classes; here the very same formula is applied with $x$ ranging over *subgroups* of $G$. Spotting that "conjugation acts on subgroups, not only on elements" is what makes the problem an instance of familiar machinery rather than something new.

**Theorem routing.** Parts 1 and 2 require no theorem — they are direct unwindings of definitions. Part 1 checks that $gHg^{-1}$ is a subgroup and that the two [[Def - Group Action|action axioms]] hold. Part 2 observes that the stabiliser condition "$g \cdot H = H$", written out, is literally $gHg^{-1} = H$, which is verbatim the defining condition of the [[Def - Normaliser|normaliser]] $N_G(H)$ — so the stabiliser *is* the normaliser, by definition and nothing more. Part 3 is then a one-line application of the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]: the conjugates of $H$ form the orbit of $H$, the stabiliser is $N_G(H)$, and the theorem equates the orbit size with the index $|G : N_G(H)|$.

**Key decision point.** The interesting move is conceptual rather than computational: it is the willingness to let a group act on a set of *subsets* — indeed of subgroups — of itself. Once the set $\mathcal{S}$ is accepted as a legitimate set to act on, every subsequent step is forced. The decision point is recognising that the normaliser was *defined* to be a stabiliser, so Part 2 has no content beyond reading the definitions side by side, and that Part 3 is then nothing but orbit-stabiliser with the stabiliser already named. The difficulty, such as it is, lies entirely in the change of perspective on what counts as a point.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory II — §1.3–1.4#Legal Operations|the topic page's Legal Operations]]:

1. **Let the group act on a cleverly chosen set** (operation 1). The chosen set is $\mathcal{S}$, the collection of all subgroups of $G$. The cleverness is only in the choice of set: subgroups, not elements, are the points.

2. **Act on the group itself by conjugation** (operation 5), in its extended form. The conjugation rule $g \cdot x = gxg^{-1}$ is applied not to elements but to subgroups. Its orbits are sets of conjugate subgroups and its stabilisers are normalisers — the structural analogues of conjugacy classes and centralisers.

3. **Count conjugates by the index of a normaliser** (operation 7). This exercise *is* the derivation of that operation: orbit-stabiliser applied to the conjugation action on subgroups, with the [[Def - Normaliser|normaliser]] $N_G(H)$ in the role of stabiliser, yields the count $|G : N_G(H)|$ for the number of conjugates of $H$.

4. **Apply the orbit-stabiliser theorem** (operation 2). With the action set up and its stabiliser identified, $|G \cdot H| = |G : N_G(H)|$ is immediate from the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]].

---

# Hints

> [!note]- Hint 1
> For Part 1, the only mild surprise is the *set* being acted on: its elements are subgroups. So first check that $gHg^{-1}$ is genuinely a subgroup (use that conjugation by a fixed $g$ is a structure-preserving map). Then verify the two action axioms $e \cdot H = H$ and $g_1 \cdot (g_2 \cdot H) = (g_1 g_2) \cdot H$ by direct computation.

> [!note]- Hint 2
> For Part 2, write out what "$g$ stabilises $H$" means for this action: it means $g \cdot H = H$, i.e. $gHg^{-1} = H$. Now look at the definition of the [[Def - Normaliser|normaliser]] $N_G(H)$. Are you looking at the same set?

> [!note]- Hint 3
> For Part 3, the subgroups conjugate to $H$ are exactly the elements of the orbit $G \cdot H$ under this action. The stabiliser of $H$ is $N_G(H)$ by Part 2. Apply the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]: the orbit size equals the index of the stabiliser.

---

# Solution

The plan is: in Part 1 verify that conjugation sends subgroups to subgroups and obeys the action axioms; in Part 2 observe that the stabiliser condition is verbatim the definition of the normaliser; in Part 3 read off the conjugate count from the orbit-stabiliser theorem.

**Step 1 (Part 1): Conjugation by $g$ sends each subgroup to a subgroup, and the rule $(g, H) \mapsto gHg^{-1}$ satisfies the action axioms.**

For a fixed $g$, the map $c_g : x \mapsto gxg^{-1}$ is an [[Def - Isomorphism|isomorphism]] $G \to G$, so it carries any subgroup $H$ to a subgroup $gHg^{-1}$; hence $g \cdot H = gHg^{-1}$ lands in $\mathcal{S}$. The identity axiom $e \cdot H = eHe^{-1} = H$ and the compatibility axiom $g_1 \cdot (g_2 \cdot H) = (g_1 g_2) \cdot H$ both hold by direct computation.

> [!note]- Derivation
> *Conjugation maps subgroups to subgroups.* Fix $g \in G$ and let $c_g : G \to G$ be the map $c_g(x) = gxg^{-1}$. It is a homomorphism, since $c_g(xy) = gxyg^{-1} = (gxg^{-1})(gyg^{-1}) = c_g(x)c_g(y)$, and it is a bijection with inverse $c_{g^{-1}}$, because $c_g(c_{g^{-1}}(x)) = g(g^{-1}xg)g^{-1} = x$. So $c_g$ is an automorphism of $G$. The image of a [[Def - Subgroup|subgroup]] under a homomorphism is a subgroup; therefore $c_g(H) = gHg^{-1}$ is a subgroup of $G$ whenever $H$ is. (Directly: $gHg^{-1}$ contains $geg^{-1} = e$; it is closed under products, $(gh_1g^{-1})(gh_2g^{-1}) = g(h_1h_2)g^{-1}$; and under inverses, $(ghg^{-1})^{-1} = gh^{-1}g^{-1}$.) Hence $g \cdot H := gHg^{-1}$ is a well-defined element of $\mathcal{S}$, so the rule is a map $G \times \mathcal{S} \to \mathcal{S}$.
>
> *Identity axiom.* $e \cdot H = eHe^{-1} = \{ehe^{-1} : h \in H\} = \{h : h \in H\} = H$.
>
> *Compatibility axiom.* For $g_1, g_2 \in G$,
> $$g_1 \cdot (g_2 \cdot H) = g_1 (g_2 H g_2^{-1}) g_1^{-1} = (g_1 g_2)\, H\, (g_2^{-1} g_1^{-1}) = (g_1 g_2)\, H\, (g_1 g_2)^{-1} = (g_1 g_2) \cdot H,$$
> using $(g_1 g_2)^{-1} = g_2^{-1} g_1^{-1}$. Both axioms hold, so $(g, H) \mapsto gHg^{-1}$ is an [[Def - Group Action|action]] of $G$ on the set $\mathcal{S}$ of subgroups.

**Step 2 (Part 2): The stabiliser of $H$ is the normaliser $N_G(H)$.**

By definition the stabiliser is $G_H = \{g \in G : g \cdot H = H\}$. Since $g \cdot H = gHg^{-1}$, the defining condition is $gHg^{-1} = H$ — and this is exactly the defining condition of the [[Def - Normaliser|normaliser]]. Hence $G_H = N_G(H)$.

> [!note]- Derivation
> For the conjugation action on $\mathcal{S}$, the [[Def - Orbit and Stabiliser|stabiliser]] of the point $H$ is
> $$G_H = \{g \in G : g \cdot H = H\} = \{g \in G : gHg^{-1} = H\},$$
> substituting the definition $g \cdot H = gHg^{-1}$. The [[Def - Normaliser|normaliser]] of $H$ is, by definition,
> $$N_G(H) = \{g \in G : gHg^{-1} = H\}.$$
> The two sets are described by the identical condition, so
> $$G_H = N_G(H).$$
> This is not a theorem requiring proof; it is the recognition that the normaliser *was defined* to be the stabiliser of $H$ under conjugation. As a free consequence, $N_G(H)$ is a [[Def - Subgroup|subgroup]] of $G$ — every stabiliser is — which is the cleanest reason the normaliser is a subgroup at all.

**Step 3 (Part 3): The number of conjugates of $H$ is $|G : N_G(H)|$.**

The subgroups conjugate to $H$ are precisely the elements of the orbit $G \cdot H$. By the orbit-stabiliser theorem the orbit size equals the index of the stabiliser, and the stabiliser is $N_G(H)$ by Step 2. Hence the number of conjugates of $H$ is $|G : N_G(H)|$.

> [!note]- Derivation
> A subgroup $H'$ is, by definition, **conjugate** to $H$ when $H' = gHg^{-1}$ for some $g \in G$ — that is, when $H' = g \cdot H$ for some $g$. The set of all such $H'$ is exactly the [[Def - Orbit and Stabiliser|orbit]]
> $$G \cdot H = \{g \cdot H : g \in G\} = \{gHg^{-1} : g \in G\}.$$
> So "the number of subgroups conjugate to $H$" is $|G \cdot H|$.
>
> The [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], applied to the finite group $G$ acting on $\mathcal{S}$, gives a bijection $gG_H \mapsto g \cdot H$ between the left [[Def - Coset|cosets]] of the stabiliser $G_H$ and the orbit $G \cdot H$; counting,
> $$|G \cdot H| = |G : G_H|.$$
> By Step 2, $G_H = N_G(H)$. Substituting,
> $$\#\{\text{subgroups conjugate to } H\} = |G \cdot H| = |G : N_G(H)|. \qquad \blacksquare$$
> In particular this number divides $|G|$, and it equals $1$ exactly when $N_G(H) = G$, i.e. exactly when $H$ is [[Def - Normal Subgroup|normal]] — a normal subgroup is its own only conjugate.

> [!note]- Complete formal solution
> Let $G$ be a group and $\mathcal{S}$ its set of subgroups.
>
> *Part 1.* Fix $g \in G$. The map $c_g(x) = gxg^{-1}$ is an automorphism of $G$: it is a homomorphism, since $c_g(xy) = (gxg^{-1})(gyg^{-1})$, and a bijection with inverse $c_{g^{-1}}$. The image of a subgroup under a homomorphism is a subgroup, so $gHg^{-1} \in \mathcal{S}$ for every $H \in \mathcal{S}$; thus $(g, H) \mapsto gHg^{-1}$ is a map $G \times \mathcal{S} \to \mathcal{S}$. It satisfies $e \cdot H = eHe^{-1} = H$ and
> $$g_1 \cdot (g_2 \cdot H) = g_1(g_2Hg_2^{-1})g_1^{-1} = (g_1g_2)H(g_1g_2)^{-1} = (g_1g_2) \cdot H,$$
> so it is an action of $G$ on $\mathcal{S}$.
>
> *Part 2.* The stabiliser of $H$ is $G_H = \{g : g \cdot H = H\} = \{g : gHg^{-1} = H\}$, which is verbatim the definition of the normaliser $N_G(H)$. Hence $G_H = N_G(H)$.
>
> *Part 3.* The subgroups conjugate to $H$ are the elements of the orbit $G \cdot H = \{gHg^{-1} : g \in G\}$. For finite $G$, the orbit-stabiliser theorem gives $|G \cdot H| = |G : G_H|$. By Part 2, $G_H = N_G(H)$, so the number of conjugates of $H$ is $|G : N_G(H)|$. $\blacksquare$

> [!example] Worked instance — Sylow subgroups
> The conjugate count $|G : N_G(H)|$ is the formula behind the third Sylow theorem. If $P$ is a Sylow $p$-subgroup of a finite group $G$, then all Sylow $p$-subgroups are conjugate, so their number is $n_p = |G : N_G(P)|$. Since $P \leq N_G(P) \leq G$, this index divides $|G : P|$, which is the part of $|G|$ coprime to $p$. That single divisibility fact — extracted from this exercise's formula — is one of the two pillars of Sylow counting, the other being the congruence $n_p \equiv 1 \pmod p$.

---

# Key Takeaways

**A group can act on far more than a set of points — it can act on its own subsets, subgroups, cosets, or partitions, and the same orbit-stabiliser machinery applies verbatim.** The conceptual leap of this exercise is recognising that the "set $X$" in a group action need not be a structureless collection of points. Here $X$ is $\mathcal{S}$, whose elements are *subgroups* of $G$. The conjugation formula $g \cdot x = gxg^{-1}$, familiar from its action on elements, transplants without change. Once one is comfortable with this, a large repertoire of actions opens up: $G$ acts on the cosets of a subgroup (the [[Thm - Coset Action and the Normal Core|coset action]]), on the $k$-element subsets of $G$ (the key to one proof of Sylow's first theorem), on the set of its Sylow subgroups, on the conjugacy classes themselves. The trigger for this technique is a counting question about objects associated with $G$ — subgroups, cosets, configurations — and the move is to recognise the relevant collection as a set $G$ acts on, after which orbit-stabiliser converts the count into an index. The orbit-stabiliser theorem does not care what the points *are*.

**The normaliser is the stabiliser of conjugation-acting-on-subgroups, exactly as the centraliser is the stabiliser of conjugation-acting-on-elements — this parallel is the right way to remember both.** This exercise reveals that $N_G(H)$ is not an ad hoc construction but the precise structural analogue, one level up, of the [[Def - Centraliser and Centre|centraliser]]. Conjugation acting on *elements* has orbits the conjugacy classes and stabilisers the centralisers $C_G(g)$; conjugation acting on *subgroups* has orbits the sets of conjugate subgroups and stabilisers the normalisers $N_G(H)$. The dictionary is exact: "conjugacy class of an element" $\leftrightarrow$ "set of conjugates of a subgroup", "$|G:C_G(g)|$ counts conjugate elements" $\leftrightarrow$ "$|G:N_G(H)|$ counts conjugate subgroups". Remembering the normaliser as "the centraliser's analogue for subgroups" makes its definition, its subgroup property, and the conjugate-counting formula all inevitable rather than memorised. Whenever a new construction is defined as $\{g : g \cdot x = x\}$ for some action, it is a stabiliser, and it is automatically a subgroup with an associated orbit-counting formula.

**When a definition is phrased as a stabiliser, the orbit-stabiliser theorem is already half-applied — counting conjugates is then a single step.** Part 3 of this exercise is one line of work, because Part 2 already identified the relevant stabiliser. This is a general efficiency: many objects in group theory are *defined* to be stabilisers — the normaliser, the centraliser, the centre as $\bigcap_g C_G(g)$, the stabiliser of a point of any geometric action — and for each, the orbit-stabiliser theorem instantly delivers a counting formula of the form "(number of conjugates / images / equivalent objects) $= |G : (\text{the stabiliser})|$". The reusable habit is: upon meeting a subgroup defined as "the elements fixing $x$", immediately write down the companion orbit and the index formula, because they come for free. This is how one obtains, in a single stroke, that the number of conjugates of an element is $|G:C_G(g)|$, that the number of conjugate subgroups is $|G:N_G(H)|$, and that the size of any orbit of any action divides $|G|$. The formula is not a separate result to recall; it is the orbit-stabiliser theorem read off the moment a stabiliser is named.

**A normal subgroup is precisely a subgroup with exactly one conjugate — normality is the degenerate case of the conjugate count.** The formula $|G : N_G(H)|$ for the number of conjugates of $H$ specialises to a clean characterisation of normality: $H$ has a single conjugate (namely itself) if and only if $|G : N_G(H)| = 1$, i.e. $N_G(H) = G$, which is the definition of $H \trianglelefteq G$. So normality is exactly the statement "conjugation cannot move $H$", the orbit of $H$ being a singleton. This reframes a qualitative property — being normal — as the extreme value of a quantitative count, and it makes the normaliser the exact measure of how *far from normal* a subgroup is: the index $|G : N_G(H)|$ is the number of distinct "shadows" $H$ casts under conjugation, equalling $1$ for normal subgroups and growing as $H$ becomes more thoroughly non-normal. This perspective — normality as a degenerate orbit, the normaliser as the obstruction to it — is what powers conjugate-counting proofs of non-simplicity in [[Group Theory III — §1.5–1.7]], where one shows a Sylow subgroup has only one conjugate and is therefore a proper non-trivial normal subgroup.
