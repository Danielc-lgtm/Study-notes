---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Subgroup"
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Def - Coset"
  - "Thm - First Isomorphism Theorem"
  - "Thm - Second Isomorphism Theorem"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a group, let $H \leq G$ be a subgroup, and let $N \trianglelefteq G$ be a normal subgroup. Define the **product set**
$$HN := \{\, hn : h \in H,\ n \in N \,\}.$$
Prove the following four statements.

1. $HN$ is a subgroup of $G$.
2. $H \cap N$ is a normal subgroup of $H$.
3. There is an isomorphism $HN/N \;\cong\; H/(H \cap N)$.
4. If $G$ is finite, then $\displaystyle |HN| = \frac{|H|\,|N|}{|H \cap N|}$.

Parts 1–3 are the **second isomorphism theorem**; part 4 is its numerical corollary.

**Recall:**

The objects are a subgroup, a normal subgroup, their product set and intersection, quotients, and the restriction of a homomorphism.

A [[Def - Subgroup|subgroup]] $H \leq G$ contains the identity and is closed under products and inverses.

![[Def - Normal Subgroup#The Definition]]

The face of normality used throughout is the rewriting rule it provides: $N \trianglelefteq G$ means $gN = Ng$ for every $g \in G$, so a factor of $N$ may be slid past any element of $G$ at the cost of replacing it with another element of $N$.

![[Def - Quotient Group#The Definition]]

The **quotient map** (or canonical projection) $\pi : G \to G/N$ sends $g \mapsto gN$. It is a surjective [[Def - Homomorphism|homomorphism]], and its [[Def - Kernel and Image|kernel]] is exactly $N$, since $gN = N$ (the identity coset) precisely when $g \in N$.

The **restriction** of a homomorphism $\varphi : G \to Q$ to a subgroup $H \leq G$ is the homomorphism $\varphi|_H : H \to Q$ obtained by only feeding it elements of $H$. It is again a homomorphism.

![[Thm - First Isomorphism Theorem#Statement]]

![[Thm - Second Isomorphism Theorem#Statement]]

For part 4, [[Thm - Lagrange's Theorem|Lagrange's theorem]]: for a finite group, $|G| = |K|\cdot|G:K|$, so the order of a quotient $G/K$ equals the index $|G:K| = |G|/|K|$.

---

# Convergent Strategy

**Problem class.** This is simultaneously a *prove a subgroup is well-formed* problem, an *identify a quotient* problem, and a *counting* problem — the three are bundled because they all fall out of a single construction. The headline result is the [[Thm - Second Isomorphism Theorem|second isomorphism theorem]], and the lesson the exercise teaches is that this theorem is not a separate piece of machinery to be memorised but a one-line consequence of the [[Thm - First Isomorphism Theorem|first]].

**Assumption pattern.** The recognisable configuration is *two [[Def - Subgroup|subgroups]], exactly one of them normal* — a subgroup $H$ with no special property and a normal subgroup $N$. As [[Group Theory I — §1.1–1.2#Legal Operations|legal operation 9]] of the topic page records, the appearance of two [[Def - Subgroup|subgroups]] at once, one normal, is the precise trigger for the second isomorphism theorem. Normality of $N$ is what makes the product set $HN$ closed and what makes $N$ available to quotient by.

**Theorem routing.** The route is a single elegant idea: *restrict the quotient map to $H$*. Form the canonical projection $\pi : G \to G/N$, then restrict it to a homomorphism $\varphi := \pi|_H : H \to G/N$. Compute its image — it turns out to be $HN/N$ — and its kernel — it turns out to be $H \cap N$. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied to $\varphi$ then yields $H/(H \cap N) \cong HN/N$ in one stroke. Normality of $H \cap N$ in $H$ comes free, because it is a kernel and kernels are normal. The counting in part 4 is then [[Thm - Lagrange's Theorem|Lagrange]] applied to the isomorphism: isomorphic finite [[Def - Group|groups]] have equal order, and $|HN/N|$, $|H/(H\cap N)|$ are indices.

**Key decision point.** The non-obvious move — the entire trick — is to *not* attack $HN$, $H \cap N$, and the isomorphism as three separate problems, but to realise one homomorphism organises all of them. A direct assault would prove $HN$ is a subgroup by hand, prove $H \cap N \trianglelefteq H$ by conjugation, and construct the isomorphism explicitly with a well-definedness check. The decision to instead write $\varphi = \pi|_H$ and read off its image and kernel collapses three proofs into one. Recognising that "the image of a restricted quotient map" is the object $HN/N$ in disguise is where the insight lives.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory I — §1.1–1.2#Legal Operations|the topic page's Legal Operations]]:

1. **Intersect or multiply subgroups** (operation 9). The exercise is built on the two compound objects $HN$ and $H \cap N$; this operation is the recognition that such objects are worth forming and that the second isomorphism theorem is the tool that relates them.

2. **Build a homomorphism to expose structure** (operation 3). The decisive construction is the restricted quotient map $\varphi = \pi|_H : H \to G/N$. The quotient map $G \to G/N$ is one of the standard stock [[Def - Homomorphism|homomorphisms]]; restricting it to $H$ is the creative twist.

3. **Apply the first isomorphism theorem to identify a quotient** (operation 4). Applied to $\varphi$, it produces $H/(H\cap N) \cong HN/N$ — and thereby proves the second isomorphism theorem rather than invoking it.

4. **Conjugate to test or exploit normality** (operation 6), used twice in packaged form: once as the rewriting rule $nh = h n'$ that makes $HN$ closed, and once as the standing fact that the kernel $H \cap N$ of $\varphi$ is automatically normal.

5. **Pass to a quotient to simplify** (operation 5). Moving from $G$ to $G/N$ and viewing $H$ through the projection is exactly the act of working in a quotient; the structure of $H$ modulo $N$ becomes visible there.

---

# Hints

> [!note]- Hint 1
> You are asked to prove three structural facts and one count, all involving the product $HN$ and the intersection $H \cap N$. Resist proving them separately. There is a single homomorphism whose image and kernel are two of these objects — find it.

> [!note]- Hint 2
> There is a canonical homomorphism out of $G$ attached to the normal subgroup $N$: the quotient map $\pi : G \to G/N$, $g \mapsto gN$. You only care about how it sees the subgroup $H$. Restrict it.

> [!note]- Hint 3
> Let $\varphi = \pi|_H : H \to G/N$. Work out $\operatorname{im}\varphi$ — which [[Def - Coset|cosets]] of $N$ are hit by elements of $H$? — and $\ker\varphi$ — which elements of $H$ map to the identity coset $N$? Then apply the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] to $\varphi$.

> [!note]- Hint 4
> For part 4: the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives an isomorphism of *finite* [[Def - Group|groups]], so they have equal order. Use $|HN/N| = |HN|/|N|$ and $|H/(H\cap N)| = |H|/|H\cap N|$, both instances of [[Thm - Lagrange's Theorem|Lagrange]], and solve for $|HN|$.

---

# Solution

The plan is to construct one homomorphism — the quotient map restricted to $H$ — and let it deliver all four parts: closure of $HN$ as its image, normality of $H \cap N$ as its kernel, the isomorphism from the first isomorphism theorem, and the count from Lagrange.

**Step 1: $HN$ is a subgroup of $G$.**

$HN$ contains the identity, and it is closed under products and inverses — the proof uses normality of $N$ as a rewriting rule, $Nh = hN$, to push $N$-factors past $H$-factors.

> [!note]- Derivation
> $HN$ is non-empty: $e = e\cdot e \in HN$ with $e \in H$, $e \in N$.
>
> *Closed under products.* Take $h_1 n_1,\ h_2 n_2 \in HN$. The obstacle is the middle pair $n_1 h_2$, which is in the wrong order. Here normality rescues us: because $N \trianglelefteq G$, we have $Nh_2 = h_2 N$, so $n_1 h_2 = h_2 n_1'$ for some $n_1' \in N$. (Concretely $n_1' = h_2^{-1} n_1 h_2 \in N$ by the conjugation definition of normality.) Then
> $$(h_1 n_1)(h_2 n_2) = h_1 (n_1 h_2) n_2 = h_1 (h_2 n_1') n_2 = (h_1 h_2)(n_1' n_2),$$
> which has the form (element of $H$)(element of $N$) since $h_1 h_2 \in H$ and $n_1' n_2 \in N$. So the product lies in $HN$.
>
> *Closed under inverses.* For $hn \in HN$, $(hn)^{-1} = n^{-1} h^{-1}$, again in the wrong order. Push $n^{-1}$ across $h^{-1}$ using $N h^{-1} = h^{-1} N$: $n^{-1} h^{-1} = h^{-1} n''$ for some $n'' \in N$. So $(hn)^{-1} = h^{-1} n'' \in HN$.
>
> Hence $HN \leq G$. (One can also get this for free as the *image* of the homomorphism in Step 2 — see the remark there — but the direct argument shows exactly where normality is spent.)

**Step 2: Construct $\varphi = \pi|_H$, the quotient map restricted to $H$.**

Let $\pi : G \to G/N$ be the canonical projection $g \mapsto gN$, and let $\varphi$ be its restriction to $H$. Then $\varphi : H \to G/N$ is a homomorphism.

> [!note]- Derivation
> Since $N \trianglelefteq G$, the [[Def - Quotient Group|quotient group]] $G/N$ exists, and the canonical projection
> $$\pi : G \longrightarrow G/N, \qquad \pi(g) = gN$$
> is a homomorphism: $\pi(g_1 g_2) = g_1 g_2 N = (g_1 N)(g_2 N) = \pi(g_1)\pi(g_2)$, where the middle equality is the definition of multiplication in $G/N$.
>
> The restriction $\varphi := \pi|_H : H \to G/N$, defined by $\varphi(h) = hN$ for $h \in H$, is still a homomorphism — restricting a homomorphism to a subgroup of its domain never breaks the homomorphism property, since the identity $\varphi(h_1 h_2) = \varphi(h_1)\varphi(h_2)$ is just $\pi$'s identity tested on elements that happen to lie in $H$. This single map is the engine for everything that follows.

**Step 3: The image of $\varphi$ is $HN/N$.**

The [[Def - Coset|cosets]] of $N$ that are hit by elements of $H$ are exactly the cosets $hN$ for $h \in H$, and these are precisely the cosets making up $HN/N$. So $\operatorname{im}\varphi = HN/N$.

> [!note]- Derivation
> By definition $\operatorname{im}\varphi = \{\varphi(h) : h \in H\} = \{hN : h \in H\}$, the set of $N$-cosets that have a representative in $H$.
>
> I claim this set equals $HN/N$, the set of $N$-cosets of the subgroup $HN$ (which is a subgroup by Step 1, and contains $N$ since $N = eN \subseteq HN$). Indeed, a coset in $HN/N$ has the form $(hn)N$ for some $h \in H$, $n \in N$; but $(hn)N = h(nN) = hN$ because $n \in N$. So every coset in $HN/N$ is $hN$ for some $h \in H$, and conversely every such $hN$ is a coset of an element $h = he \in HN$. Therefore
> $$\operatorname{im}\varphi = \{hN : h \in H\} = HN/N.$$
> As the image of a homomorphism, $\operatorname{im}\varphi$ is a subgroup of $G/N$ — so $HN/N$ is a genuine subgroup of $G/N$, which by the [[Thm - Correspondence Theorem|correspondence]] reflects that $HN$ is a subgroup of $G$, an independent confirmation of Step 1.

**Step 4: The kernel of $\varphi$ is $H \cap N$; hence $H \cap N \trianglelefteq H$.**

An element of $H$ maps to the identity coset $N$ exactly when it lies in $N$ — so $\ker\varphi = H \cap N$. Since kernels are normal, $H \cap N \trianglelefteq H$.

> [!note]- Derivation
> The identity element of $G/N$ is the coset $N$ itself. So
> $$\ker\varphi = \{h \in H : \varphi(h) = N\} = \{h \in H : hN = N\}.$$
> Now $hN = N$ holds if and only if $h \in N$ — the kernel of the *full* projection $\pi$ is exactly $N$. Therefore
> $$\ker\varphi = \{h \in H : h \in N\} = H \cap N.$$
> By the standing lemma in [[Def - Kernel and Image]], the kernel of any homomorphism is a [[Def - Normal Subgroup|normal subgroup]] of its domain. The domain of $\varphi$ is $H$, so
> $$H \cap N = \ker\varphi \trianglelefteq H.$$
> This proves part 2 with no conjugation calculation: normality of $H \cap N$ in $H$ is inherited from its being a kernel. (Note the result is normality in $H$, not in $G$; $H \cap N$ need not be normal in $G$.)

**Step 5: Apply the first isomorphism theorem to get $HN/N \cong H/(H \cap N)$.**

Feeding $\varphi$ to the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives $H/\ker\varphi \cong \operatorname{im}\varphi$, which is exactly $H/(H \cap N) \cong HN/N$.

> [!note]- Derivation
> The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] states that for any homomorphism $\psi : A \to B$, the kernel is normal and
> $$A/\ker\psi \;\cong\; \operatorname{im}\psi.$$
> Apply it to $\psi = \varphi : H \to G/N$. By Step 4, $\ker\varphi = H \cap N$. By Step 3, $\operatorname{im}\varphi = HN/N$. Substituting,
> $$H/(H \cap N) \;\cong\; HN/N.$$
> This is part 3, and together with parts 1 and 2 it is the full [[Thm - Second Isomorphism Theorem|second isomorphism theorem]]. The isomorphism is explicit: it sends the coset $h(H \cap N) \mapsto hN$.

**Step 6: Count — $|HN| = |H|\,|N|/|H \cap N|$.**

Isomorphic finite groups have equal order; writing each side's order as an index via [[Thm - Lagrange's Theorem|Lagrange]] and rearranging gives the formula.

> [!note]- Derivation
> Assume $G$ finite, so $H$, $N$, $HN$, $H \cap N$ are all finite. The isomorphism of Step 5 relates two finite groups, and isomorphic groups have the same number of elements:
> $$|HN/N| = |H/(H \cap N)|.$$
> Now express each order as an index. [[Thm - Lagrange's Theorem|Lagrange's theorem]] gives, for any finite group $A$ and subgroup $K \leq A$, that $|A/K| = |A : K| = |A|/|K|$ (the order of a quotient is the index). Applying this on both sides:
> $$\frac{|HN|}{|N|} = |HN/N| = |H/(H \cap N)| = \frac{|H|}{|H \cap N|}.$$
> Multiplying both sides by $|N|$ and rearranging,
> $$|HN| = \frac{|H|\,|N|}{|H \cap N|}.$$
> This is part 4. Note $HN$ need not be the *internal direct product* of $H$ and $N$ — the formula corrects the naive count $|H|\,|N|$ by exactly the overlap factor $|H \cap N|$, because each element of $HN$ is written as $hn$ in precisely $|H \cap N|$ ways. $\blacksquare$

> [!note]- Complete formal solution
> Let $H \leq G$ and $N \trianglelefteq G$.
>
> *Part 1.* $HN \ni e$. For products, given $h_1 n_1, h_2 n_2 \in HN$, normality of $N$ gives $n_1 h_2 = h_2 (h_2^{-1} n_1 h_2)$ with $h_2^{-1} n_1 h_2 \in N$, so $(h_1 n_1)(h_2 n_2) = (h_1 h_2)\big((h_2^{-1}n_1 h_2) n_2\big) \in HN$. For inverses, $(hn)^{-1} = n^{-1}h^{-1} = h^{-1}(h n^{-1} h^{-1}) \in HN$. Hence $HN \leq G$.
>
> *Construction.* Since $N \trianglelefteq G$, the quotient $G/N$ exists and $\pi : G \to G/N$, $g \mapsto gN$, is a homomorphism. Let $\varphi = \pi|_H : H \to G/N$, $\varphi(h) = hN$; it is a homomorphism.
>
> *Image.* $\operatorname{im}\varphi = \{hN : h \in H\}$. Every coset in $HN/N$ is $(hn)N = hN$ with $h \in H$, and every $hN$ is the coset of $h \in HN$; so $\operatorname{im}\varphi = HN/N$.
>
> *Kernel and Part 2.* $\ker\varphi = \{h \in H : hN = N\} = \{h \in H : h \in N\} = H \cap N$. Kernels are normal in the domain, so $H \cap N \trianglelefteq H$.
>
> *Part 3.* The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied to $\varphi$ gives $H/\ker\varphi \cong \operatorname{im}\varphi$, i.e.
> $$H/(H \cap N) \;\cong\; HN/N.$$
>
> *Part 4.* If $G$ is finite, isomorphic groups have equal order, so $|HN|/|N| = |HN/N| = |H/(H\cap N)| = |H|/|H \cap N|$ by [[Thm - Lagrange's Theorem|Lagrange]]. Rearranging,
> $$|HN| = \frac{|H|\,|N|}{|H \cap N|}. \qquad \blacksquare$$

---

# Key Takeaways

**Restricting a known homomorphism to a subgroup is a general way to manufacture the map you need.** The crux of this proof was not inventing a homomorphism from scratch but *taking one you already have and shrinking its domain*. The quotient map $\pi : G \to G/N$ exists the moment $N$ is normal; the creative act was restricting it to $H$ to get $\varphi = \pi|_H$. Restriction is a cheap, reliable source of [[Def - Homomorphism|homomorphisms]], and its image and kernel are exactly the objects you want: the image is "what $H$ looks like inside the quotient", the kernel is "the part of $H$ that the quotient cannot see", namely $H \cap N$. Whenever a problem involves a subgroup $H$ together with some structure on the ambient group $G$ — a quotient map, a sign map, a determinant, an action — consider restricting that structure to $H$ and applying the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] to the restriction. This is precisely how the [[Thm - Second Isomorphism Theorem|second isomorphism theorem]] is proved, and the same template, restrict-then-first-isomorphism, recurs throughout the subject.

**The first isomorphism theorem is the only isomorphism theorem; the others are corollaries.** This exercise reveals that the second isomorphism theorem need not be memorised as an independent fact. It *is* the first isomorphism theorem applied to one specific, natural homomorphism — the restricted quotient map. The same is true of the [[Thm - Third Isomorphism Theorem|third isomorphism theorem]], which is the first theorem applied to $G/K \to G/L$, $gK \mapsto gL$. The reusable meta-lesson is that when you meet a named theorem asserting an isomorphism between two quotients, you should ask "what homomorphism, fed to the first isomorphism theorem, produces this?" — and the proof, the well-definedness, and the normality of the relevant subgroup all then come for free in one stroke. Internalising the first isomorphism theorem deeply therefore pays compound interest: it is not one tool among several but the single engine behind the whole family. When you remember the first theorem and the trick of picking the right map, you never need to separately remember the second or third.

**Counting falls out of an isomorphism: equal groups have equal order, and Lagrange converts order into index.** Part 4 illustrates a routine but powerful move — once you have an *isomorphism* of finite groups, you instantly have an *equation of integers*, because isomorphic groups are equinumerous. The job is then to express each side's cardinality in terms of the quantities you care about, and [[Thm - Lagrange's Theorem|Lagrange's theorem]] is the universal translator: it rewrites the order of any quotient $A/K$ as the index $|A|/|K|$. So an isomorphism $A/K \cong B/L$ becomes the numerical identity $|A|/|K| = |B|/|L|$, which you solve for whatever is unknown. Here it produced $|HN| = |H||N|/|H\cap N|$, the inclusion–exclusion-flavoured count for a product of subgroups. The general pattern — prove an isomorphism, then read it as a counting identity through Lagrange — is one of the most common ways order formulas are derived in finite group theory, and it is why structural theorems so often have immediate enumerative corollaries. Whenever you want to count something, look for an isomorphism that has the count on one side.
