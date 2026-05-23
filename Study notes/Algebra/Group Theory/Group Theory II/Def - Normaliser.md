---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Group Action"
  - "Def - Orbit and Stabiliser"
  - "Def - Conjugacy Class"
  - "Def - Centraliser and Centre"
  - "Def - Normal Subgroup"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group with identity $e$, and $H \leq G$ denotes a [[Def - Subgroup|subgroup]]. The **conjugate subgroup** of $H$ by $g \in G$ is $gHg^{-1} = \{ghg^{-1} : h \in H\}$, itself always a subgroup of $G$ of the same order as $H$. The **normaliser** of $H$ in $G$ is written $N_G(H)$. We write $H \trianglelefteq G$ for "$H$ is [[Def - Normal Subgroup|normal]] in $G$" and $|G : H|$ for the index. Note the contrast with the [[Def - Centraliser and Centre|centraliser]] $C_G(g)$, which is attached to an *element*: the normaliser is attached to a *subgroup*. The full symbol registry for this topic is on [[Group Theory II — §1.3–1.4]].

---

# Axiom Motivation

The normaliser solves a problem you run into the moment you care about [[Def - Normal Subgroup|normal subgroups]]: a given subgroup $H \leq G$ is usually *not* normal in $G$, and you would like to know how badly it fails — and whether the failure can be repaired.

Recall what normality asks. $H$ is normal in $G$ when $gHg^{-1} = H$ for *every* $g \in G$. For most [[Def - Subgroup|subgroups]] this fails: there is some $g$ for which $gHg^{-1}$ is a *different* subgroup. But the failure is rarely total. Some elements $g$ *do* satisfy $gHg^{-1} = H$ — at the very least every $g \in H$ does, since $H$ is closed under conjugation by its own elements. So the elements of $G$ split into two kinds: those that conjugate $H$ to itself, and those that conjugate $H$ to something else. The desideratum is a name and a structure for the *good* set — the elements under which $H$ is invariant.

Define, then, $N_G(H) = \{g \in G : gHg^{-1} = H\}$. Two things must be true for this to be the right object, and both are forced.

*First, it must be a [[Def - Subgroup|subgroup]] of $G$.* It is — and the cleanest way to see this is not to check closure by hand but to recognise $N_G(H)$ as a **stabiliser**. The [[Def - Group|group]] $G$ acts on the *set of all its [[Def - Subgroup|subgroups]]* by conjugation: $g$ sends a subgroup $K$ to $gKg^{-1}$, which is again a subgroup. This is a genuine [[Def - Group Action|action]] (the identity fixes every subgroup, and $g_1(g_2 K g_2^{-1})g_1^{-1} = (g_1g_2)K(g_1g_2)^{-1}$). The normaliser of $H$ is precisely the [[Def - Orbit and Stabiliser|stabiliser]] of the point $H$ in this action — and stabilisers of actions are always subgroups. So defining $N_G(H)$ as the conjugation-stabiliser of $H$ hands us the subgroup property for free, and immediately tells us, via the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], that the *number of conjugate subgroups* $gHg^{-1}$ equals the index $|G : N_G(H)|$.

*Second, $H$ must be normal inside $N_G(H)$.* Check it: for $g \in N_G(H)$ we have $gHg^{-1} = H$ by definition, and that is exactly the statement $H \trianglelefteq N_G(H)$. So we have $H \trianglelefteq N_G(H) \leq G$ — the normaliser is a subgroup *containing $H$, in which $H$ becomes normal*. This is the repair we wanted: even when $H$ is not normal in all of $G$, it is normal in the normaliser, so we can form the quotient $N_G(H)/H$ locally.

Now the question that pins down *this* definition rather than a near variant: how big should $N_G(H)$ be? It must be the **largest** subgroup of $G$ in which $H$ is normal. Suppose $K$ is any subgroup with $H \trianglelefteq K \leq G$. Normality of $H$ in $K$ says $kHk^{-1} = H$ for all $k \in K$, which is exactly the condition for $k \in N_G(H)$ — so $K \leq N_G(H)$. The normaliser swallows every subgroup in which $H$ is normal. That is the characterising property, and it is why the condition is "$gHg^{-1} = H$" and not something weaker or stronger.

What if we *weakened* the defining condition to $gHg^{-1} \subseteq H$ — containment instead of equality? For a *finite* $H$ this is harmless: a subgroup contained in $H$ with the same finite order $|gHg^{-1}| = |H|$ must equal $H$, so containment upgrades to equality automatically. But for *infinite* $H$ the weakened version is genuinely larger and is no longer a subgroup (it need not be closed under inverses), and it is not the stabiliser of anything. So equality is the correct condition; containment is a finite-only coincidence.

What if we *strengthened* it — demanded not $gHg^{-1} = H$ but $ghg^{-1} = h$ for every individual $h \in H$? That is a strictly stronger condition: it says $g$ commutes with each element of $H$ one at a time, not merely that it permutes $H$ among itself. The strengthened object is the **centraliser** $C_G(H) = \bigcap_{h \in H} C_G(h)$, and it is a *subgroup of* the normaliser, $C_G(H) \leq N_G(H)$, usually proper. The distinction is the whole point: the normaliser asks $g$ to *preserve $H$ setwise*, the centraliser asks $g$ to *fix $H$ pointwise*. Preserving setwise is what makes a quotient possible; fixing pointwise is a much rarer and stronger demand. The normaliser is the Goldilocks notion — weak enough to be large and useful, strong enough that $H$ is normal inside it.

A final motivating remark by jumping ahead. The normaliser is the engine of the **counting of conjugate subgroups**, and that is what makes the Sylow theorems work. Sylow's theorems are about the conjugacy class of a Sylow $p$-subgroup $P$; the number of Sylow $p$-subgroups is the size of that conjugacy class, which by orbit-stabiliser is $|G : N_G(P)|$. Without the normaliser there is no formula for "how many subgroups are conjugate to this one", and the entire numerical theory of Sylow collapses. The normaliser exists because we need a denominator for counting conjugate subgroups, exactly as the [[Def - Centraliser and Centre|centraliser]] exists to be the denominator for counting conjugate *elements*.

---

# The Definition

Let $G$ be a [[Def - Group|group]] and $H \leq G$ a [[Def - Subgroup|subgroup]]. The **normaliser** of $H$ in $G$ is
$$N_G(H) \;=\; \{\, g \in G : gHg^{-1} = H \,\},$$
the set of elements of $G$ that conjugate $H$ to itself (as a set). Equivalently, $N_G(H)$ is the [[Def - Orbit and Stabiliser|stabiliser]] of $H$ under the [[Def - Group Action|action]] of $G$ by conjugation on the set of all subgroups of $G$; it is therefore a subgroup of $G$.

The normaliser has three defining structural properties.

1. **It contains $H$ and makes $H$ normal:** $H \trianglelefteq N_G(H) \leq G$. Every $h \in H$ satisfies $hHh^{-1} = H$, so $H \leq N_G(H)$; and $gHg^{-1} = H$ for all $g \in N_G(H)$ is exactly the statement that $H$ is normal in $N_G(H)$.

2. **It is the largest such subgroup.** If $K \leq G$ satisfies $H \trianglelefteq K$, then $K \leq N_G(H)$. So $N_G(H)$ is the unique largest subgroup of $G$ in which $H$ is a normal subgroup.

3. **It detects normality in $G$:** $H \trianglelefteq G$ if and only if $N_G(H) = G$. At the other extreme, $N_G(H) = H$ means $H$ is "self-normalising" — as normal as it can be without being normal at all.

By the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], the **number of distinct conjugate subgroups** of $H$ — the subgroups of the form $gHg^{-1}$ — equals the index
$$\#\{\, gHg^{-1} : g \in G \,\} \;=\; |G : N_G(H)|.$$

For a *singleton* subgroup, the normaliser specialises to the [[Def - Centraliser and Centre|centraliser]]: $N_G(\{g\}) = C_G(g)$, since requiring $g\{x\}g^{-1} = \{x\}$ is requiring $gxg^{-1} = x$.

---

# Relate to Other Fields / Compression

The normaliser is one instance of a pattern that occurs throughout mathematics: **the symmetries of an ambient object that preserve a chosen sub-object** — the *stabiliser of a subobject*, as opposed to the stabiliser of a point.

The cleanest comparison is with the [[Def - Centraliser and Centre|centraliser]], its companion on this topic. The centraliser $C_G(g)$ stabilises an *element* under conjugation; the normaliser $N_G(H)$ stabilises a *subgroup*. They are the same construction — conjugation-stabiliser — applied to two different sets the group acts on: the set $G$ of elements, and the set of subgroups of $G$. Indeed $N_G(\{g\}) = C_G(g)$ exactly. Their indices count two different conjugacy questions: $|G : C_G(g)|$ counts elements conjugate to $g$, and $|G : N_G(H)|$ counts subgroups conjugate to $H$.

In **linear algebra and Lie theory** the analogue of the normaliser is the *stabiliser of a subspace* — the matrices $g$ with $gW = W$ for a fixed subspace $W$ — which is a *parabolic-type* subgroup of $\mathrm{GL}_n$. The genuine Lie-theoretic normaliser, $N_G(H)$ for $H$ a subgroup of a Lie group $G$, controls the structure of homogeneous spaces: the *Weyl group* of a compact Lie group is the quotient $N_G(T)/T$ of the normaliser of a maximal torus $T$ by the torus itself — literally the construction $N_G(H)/H$ from this page, and one of the central objects of the theory. A reader with a geometry background has met $N_G(T)/T$ as the Weyl group without perhaps recognising it as a normaliser quotient.

In **Galois theory** the normaliser governs which subfields are themselves Galois. Under the Galois correspondence, a subgroup $H$ of the Galois group corresponds to an intermediate field, and that field is a *normal* (Galois) extension of the base exactly when $H$ is normal in the full Galois group. The normaliser $N_G(H)$ corresponds to the largest intermediate field over which the extension is Galois — the field-theoretic shadow of "the largest subgroup in which $H$ is normal".

So the compression is: the normaliser is "the part of the group that preserves a subgroup as a set", the largest place where you can quotient by that subgroup; specialise to a singleton and it is the centraliser, specialise to a maximal torus and its quotient is the Weyl group, pass through the Galois correspondence and it is the largest intermediate field with a normal extension.

---

# Examples / Corollaries

**Is an instance — the normaliser of a non-normal subgroup of $S_3$.** Take $H = \langle (1\,2)\rangle = \{e, (1\,2)\}$ in $S_3$. Which $g$ satisfy $gHg^{-1} = H$? Certainly the two elements of $H$ do. The element $(1\,3)$ does not: $(1\,3)(1\,2)(1\,3) = (2\,3)$, so $(1\,3)H(1\,3)^{-1} = \{e,(2\,3)\} \neq H$. Checking the rest, no element outside $H$ normalises $H$, so $N_{S_3}(H) = H$ — the subgroup is *self-normalising*. The orbit-stabiliser count then gives $|S_3 : N_{S_3}(H)| = 6/2 = 3$ conjugate subgroups, namely $\{e,(1\,2)\}, \{e,(1\,3)\}, \{e,(2\,3)\}$ — and indeed there are three order-$2$ subgroups, all conjugate.

**Is an instance — the normaliser of $A_3$ in $S_3$.** Take $H = A_3 = \{e, (1\,2\,3), (1\,3\,2)\}$, the alternating subgroup. It has index $2$ in $S_3$, and any index-$2$ subgroup is [[Def - Normal Subgroup|normal]], so $A_3 \trianglelefteq S_3$. By property (3) of the definition, $N_{S_3}(A_3) = S_3$ — the normaliser is the whole group exactly when the subgroup is normal. The conjugate-subgroup count is $|S_3 : S_3| = 1$: $A_3$ has only itself as a conjugate.

**Is an instance — the normaliser of a Sylow subgroup.** In any finite group $G$, if $P$ is a Sylow $p$-subgroup, the number of Sylow $p$-subgroups is $|G : N_G(P)|$. For example in $S_4$ (order $24$) a Sylow $2$-subgroup $P$ has order $8$; the number of Sylow $2$-subgroups is $3$, so $|N_{S_4}(P)| = 24/3 = 8$, meaning $P$ is self-normalising. This is the prototype of every Sylow-counting argument.

**Is NOT an instance — the normaliser is not the centraliser.** It is tempting to conflate $N_G(H)$ with the [[Def - Centraliser and Centre|centraliser]] $C_G(H) = \{g : gh = hg \ \forall h \in H\}$. They differ. Take $G = S_3$ and $H = A_3$. The normaliser is all of $S_3$ (shown above). The centraliser $C_{S_3}(A_3)$ is only $A_3$ itself: a transposition does *not* commute with the $3$-cycles — $(1\,2)(1\,2\,3) = (1\,3) \neq (2\,3) = (1\,2\,3)(1\,2)$ — even though it normalises $A_3$. So $C_{S_3}(A_3) = A_3 \subsetneq S_3 = N_{S_3}(A_3)$. The normaliser asks $g$ to permute $H$ among itself; the centraliser asks $g$ to fix every element of $H$.

**Is NOT an instance — the conjugate $gHg^{-1}$ is not "$H$ shifted".** A common slip is to picture $gHg^{-1}$ as a [[Def - Coset|coset]] or a translate of $H$. It is neither: $gHg^{-1}$ is a *subgroup* (it contains $e$ and is closed), generally a different subgroup of the same order, whereas a coset $gH$ is *not* a subgroup unless $g \in H$. The normaliser is the set of $g$ for which the *subgroup* $gHg^{-1}$ coincides with $H$ — a statement about subgroups, not about [[Def - Coset|cosets]].

**Corollary — the normaliser tower $C_G(H) \leq N_G(H) \leq G$, with $C_G(H) \trianglelefteq N_G(H)$.** The [[Def - Centraliser and Centre|centraliser]] of $H$ is contained in the normaliser, and is in fact normal in it. Moreover the quotient $N_G(H)/C_G(H)$ embeds in the [[Def - Automorphism Group|automorphism group]] $\operatorname{Aut}(H)$: an element of the normaliser conjugates $H$ to itself and so induces an automorphism of $H$, the kernel of this assignment being exactly the centraliser. This $N/C$ theorem is how one bounds the structure of $N_G(H)$ when $\operatorname{Aut}(H)$ is understood.

**Corollary — $H \trianglelefteq G$ if and only if $N_G(H) = G$ if and only if $H$ has exactly one conjugate.** Three equivalent statements of normality, each a calibration check. $H$ is normal precisely when every $g$ normalises it, precisely when the normaliser is everything, precisely when the conjugacy class of subgroups $\{gHg^{-1}\}$ is the singleton $\{H\}$ — i.e. $|G : N_G(H)| = 1$.

**Corollary — index of the smallest prime forces normality, via the normaliser.** If $H \leq G$ has index equal to the smallest prime $p$ dividing $|G|$, then $H \trianglelefteq G$. One route is the [[Thm - Coset Action and the Normal Core|coset action]]; another uses the normaliser directly together with the conjugate-counting formula. The number of conjugates of $H$ is $|G : N_G(H)|$, which divides $|G : H| = p$, so it is $1$ or $p$; a short counting argument on the elements covered rules out $p$, forcing one conjugate, hence $N_G(H) = G$, hence normality. This is the standard application: the normaliser converts "few conjugates" into "normal".

---

# Unlocked by This

> [!tip] The Sylow Theorems *(from Group Theory III)*
> The number of Sylow $p$-subgroups of a finite group is the index $|G : N_G(P)|$ of the normaliser of any one of them; Sylow's theorems are statements about this conjugacy class of subgroups. The normaliser is the indispensable denominator for the entire numerical theory in [[Group Theory III — §1.5–1.7]].

> [!tip] The Frattini Argument *(from Group Theory III)*
> A recurring technique — the *Frattini argument* — factors a group as $G = N \cdot N_G(P)$ when $P$ is a Sylow subgroup of a normal subgroup $N$. It is one of the most productive uses of the normaliser in structural group theory, and it depends entirely on the conjugacy properties recorded on this page.

> [!tip] The Weyl Group *(from Lie Theory)*
> For a compact Lie group $G$ with maximal torus $T$, the *Weyl group* is the quotient $N_G(T)/T$ of the normaliser of the torus by the torus itself — literally the construction $N_G(H)/H$ from this page. The Weyl group is a finite reflection group and is the combinatorial heart of the representation theory of $G$.
