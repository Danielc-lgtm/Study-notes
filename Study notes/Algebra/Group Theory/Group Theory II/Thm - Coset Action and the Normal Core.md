---
type: theorem
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Coset"
  - "Def - Normal Subgroup"
  - "Def - Group Action"
  - "Def - Symmetric Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Def - Simple Group"
  - "Thm - Actions Correspond to Homomorphisms"
  - "Thm - First Isomorphism Theorem"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---

# Notation

$G$ is a group with identity $e$; $H \leq G$ a [[Def - Subgroup|subgroup]]. The set of left [[Def - Coset|cosets]] is $G/H = \{xH : x \in G\}$, and the **index** $|G : H| = |G/H|$ is the number of cosets. A [[Def - Normal Subgroup|normal subgroup]] $N \trianglelefteq G$ satisfies $gNg^{-1} = N$ for all $g$. For $x \in G$, the **conjugate subgroup** is $xHx^{-1} = \{xhx^{-1} : h \in H\}$. The [[Def - Symmetric Group|symmetric group]] of a set $Y$ is $\operatorname{Sym}(Y)$, with $S_n = \operatorname{Sym}(\{1,\dots,n\})$ of order $n!$. The **coset action** is the action of $G$ on $G/H$ by left multiplication, $g\cdot(xH) = gxH$. The **normal core** of $H$ is $\operatorname{Core}_G(H) = \bigcap_{x\in G} xHx^{-1}$. A non-trivial group is [[Def - Simple Group|simple]] if its only normal subgroups are $\{e\}$ and itself. The full notation registry lives on the parent page [[Group Theory II — §1.3–1.4]].

---

# Statement

> **Theorem (Coset action and the normal core).** Let $H \leq G$ be a [[Def - Subgroup|subgroup]]. Then $G$ acts on the set of left [[Def - Coset|cosets]] $G/H$ by left multiplication, $g\cdot(xH) = gxH$. The [[Def - Kernel and Image|kernel]] of the associated [[Def - Homomorphism|homomorphism]] $\rho : G \to \operatorname{Sym}(G/H)$ is
> $$\ker\rho \;=\; \bigcap_{x \in G} xHx^{-1} \;=:\; \operatorname{Core}_G(H),$$
> the **normal core** of $H$ — the largest [[Def - Normal Subgroup|normal subgroup]] of $G$ contained in $H$.

> **Index theorem.** Let $G$ be finite and $H \leq G$ a subgroup of index $n$. Then there is a [[Def - Normal Subgroup|normal subgroup]] $K \trianglelefteq G$ with $K \leq H$ such that $G/K$ is isomorphic to a subgroup of $S_n$. Hence
> $$|G/K| \;\big|\; n! \qquad\text{and}\qquad |G/K| \;\geq\; n.$$

> **Corollary (no small subgroups in a simple group).** Let $G$ be a non-abelian [[Def - Simple Group|simple]] group and $H \leq G$ a proper subgroup of index $n > 1$. Then $G$ is isomorphic to a subgroup of $A_n$; consequently $n \geq 5$ — a non-abelian simple group has no proper subgroup of index less than $5$.

The construction manufactures a normal subgroup from an arbitrary subgroup — the most reliable source of normal subgroups in the topic — and the corollary turns it into a remarkably rigid constraint on simple groups.

---

# Motivation

[[Group Theory I — §1.1–1.2]] established that [[Def - Normal Subgroup|normal subgroups]] are the good subgroups: they are exactly the ones you can quotient by, the kernels of homomorphisms, the building blocks of the structure theory. But normality is a *fragile* property. A generic [[Def - Subgroup|subgroup]] $H \leq G$ is not normal — the condition $gHg^{-1} = H$ for all $g$ is a strong demand, and most subgroups fail it. This leaves a gap: subgroups are easy to come by (every element generates one, every intersection is one), but the *useful* subgroups, the normal ones, are scarce. Where do normal subgroups come from when none is handed to you?

This theorem answers that. It gives a universal recipe — input *any* subgroup $H$, output a normal subgroup — and the recipe is pure [[Thm - Actions Correspond to Homomorphisms|action machinery]]. The idea is that a subgroup, even a badly non-normal one, still has a coset space $G/H$, and $G$ permutes that coset space by left multiplication. An action is a homomorphism; a homomorphism has a kernel; a kernel is normal. So the coset action *converts a subgroup into a normal subgroup automatically*, by routing it through the kernel. The normal subgroup produced — the normal core — is the largest one that fits inside $H$, so the recipe extracts the maximal normal "essence" of any subgroup.

Why is this worth a theorem rather than a remark? Because the size of the coset space is *controlled*: $|G/H| = n$, the index. So the homomorphism lands in $S_n$, a group of order $n!$, and that turns the construction into an *arithmetic weapon*. The quotient $G/K$ embeds in $S_n$, so $|G/K|$ must divide $n!$. When $n$ is small, $n!$ is small, and this divisibility is severe — it can force $K$ to be all of $G$ (the action is trivial) or force a contradiction. This is the standard route by which "a subgroup of small index exists" is converted into a hard structural conclusion: either a normal subgroup appears, or the group cannot exist.

The corollary is the cleanest demonstration. A non-abelian [[Def - Simple Group|simple]] group has, by definition, *no* normal subgroups except the trivial ones. Feed it a proper subgroup of index $n$ and the coset action produces a normal subgroup inside $H$ — which simplicity forces to be trivial — so $G$ itself embeds in $S_n$. Pushing the argument slightly further (the image avoids odd permutations) lands $G$ inside $A_n$. But $A_1, A_2, A_3, A_4$ contain no non-abelian simple group at all, so $n$ must be at least $5$. A single counting action has proved that the smallest "room" a non-abelian simple group can sit in is index $5$ — a constraint extracted from nothing but the existence of a subgroup.

---

# Sources and Targets

This section is not an input/output summary. Sources record the non-obvious circumstances under which you hold the hypothesis — *a subgroup of a group*. Targets record what becomes provable once the conclusion (a normal subgroup $K \leq H$ with $G/K \hookrightarrow S_n$) is combined with one further fact.

**Sources (Input Broadening)**

The hypothesis is "$H \leq G$ is a subgroup of index $n$". The skill is recognizing a subgroup of *controlled index* where the problem advertises something else.

The first source is **a group element of known order in a finite group**. Property $B$ is "$G$ has an element $g$, hence the cyclic subgroup $\langle g\rangle$". The bridge is that $\langle g\rangle$ has index $|G|/\operatorname{ord}(g)$, so any element gives a subgroup of computable index, and the coset action applies to it. The implication is non-obvious because an element does not look like an indexed subgroup. Example: in a group of order $2m$ with $m$ odd, an element of order $2$ generates an index-$m$ subgroup, and the coset action of $G$ on its $m$ cosets is the start of the proof (via the sign map) that $G$ has a normal subgroup of index $2$.

The second source is **a maximal subgroup**. Property $B$ is "$M < G$ is a maximal subgroup" — a proper subgroup contained in no larger proper subgroup. The bridge is that maximal subgroups are exactly the subgroups whose coset action is *primitive*, and they have no normal subgroup strictly between $\operatorname{Core}_G(M)$ and $M$. The implication is non-obvious because maximality is a lattice condition, not an index condition, yet it sharply controls the normal core. Example: if a maximal subgroup $M$ has trivial core then $G$ embeds in $S_{|G:M|}$ — the route to bounding $|G|$ by the index of a maximal subgroup.

The third source is **a subgroup arising as a stabiliser of a transitive action**. Property $B$ is "$G$ acts transitively on a set $X$". The bridge — orbit-stabiliser — is that a point stabiliser $G_x$ has index $|X|$, and the given action is *equivalent* to the coset action on $G/G_x$. The implication is non-obvious because a transitive action on an abstract set $X$ does not visibly carry a subgroup, yet every transitive action *is* a coset action in disguise. Example: a transitive action on $n$ points gives an index-$n$ subgroup, and the kernel of the action is the normal core of that stabiliser.

The fourth source is **a subgroup of index equal to the smallest prime dividing $|G|$**. Property $B$ is "$H \leq G$ has index $p$, where $p$ is the least prime factor of $|G|$". The bridge is the coset action: $G/K \hookrightarrow S_p$, so $|G/K| \mid p!$, and since $|G/K|$ also divides $|G|$ whose prime factors are all $\geq p$, the only common possibility forces $|G/K| = p$, whence $K = H$ and $H$ is normal. The implication is non-obvious because "index is the smallest prime" sounds like a numerical accident, but it is exactly the hypothesis that makes the $S_p$ embedding collapse. Example: this is the standard proof that an index-$2$ subgroup — and more generally an index-smallest-prime subgroup — is automatically normal.

**Targets (Output Amplification)**

The conclusion gives a normal subgroup $K \leq H$ with $G/K \hookrightarrow S_n$, so $|G/K| \mid n!$.

The first combination is **conclusion plus $|G| \nmid n!$ forces non-triviality of $K$, hence non-simplicity**. The conclusion gives $G/K \hookrightarrow S_n$, so $|G/K| \mid n!$. Add property $D$: $|G|$ does not divide $n!$. Then $K \neq \{e\}$ (else $|G/K| = |G|$ would divide $n!$); and if the action moves a coset, $K \neq G$. The further result $E$ is a proper non-trivial normal subgroup, so $G$ is **not** [[Def - Simple Group|simple]]. The combination is non-obvious because the only inputs are a subgroup and the failure of a divisibility — yet they produce a deep structural verdict. This is the workhorse non-simplicity argument.

The second combination is **conclusion plus $H$ core-free pins down an embedding $G \hookrightarrow S_n$**. The conclusion gives $K = \operatorname{Core}_G(H)$. Add property $D$: $H$ is *core-free*, $\operatorname{Core}_G(H) = \{e\}$ — automatic, in particular, when $G$ is simple and $H$ proper. Then $K = \{e\}$ and $G \cong G/K \hookrightarrow S_n$ outright. The result $E$ is a faithful permutation representation of $G$ on $n$ points, bounding $|G| \leq n!$. The combination is non-obvious because "core-free" is a condition on intersections of conjugates, and it is not visible that it upgrades the quotient embedding to an embedding of $G$ itself.

The third combination is **conclusion plus simplicity and parity lands $G$ inside $A_n$**. The conclusion (with $H$ core-free) gives $G \hookrightarrow S_n$. Add property $D$: $G$ is non-abelian simple. Intersecting the image with $A_n$ gives a normal subgroup of $\operatorname{im}\rho \cong G$, which simplicity forces to be everything (it cannot be trivial, else $G$ embeds in $S_n/A_n \cong C_2$ and is abelian). The result $E$ is $G \hookrightarrow A_n$, and since $A_1,\dots,A_4$ have no non-abelian simple subgroup, $n \geq 5$. The combination is non-obvious because the upgrade from $S_n$ to $A_n$ uses the [[Thm - First Isomorphism Theorem|second isomorphism theorem]] and the simplicity of $G$ in a way that has nothing to do with the original coset action.

The fourth combination is **conclusion plus a prime-power order forces normality of small-index subgroups**. The conclusion gives $|G/K| \mid n!$ and $|G/K|$ divides $|G|$. Add property $D$: $n$ is the smallest prime $p$ dividing $|G|$. The only divisor of both $p!$ and $|G|$ that is at least $n$ is $p$ itself, so $|G/K| = p$, forcing $K = H$. The result $E$: every subgroup of index the smallest prime factor of $|G|$ is normal. The combination is non-obvious because it is a pure number-theoretic squeeze — two divisibility constraints with a unique common solution.

---

# Why Is It True

The theorem has two claims — that the coset action exists, and that its kernel is the normal core — and both become transparent once you picture left multiplication shuffling the cosets.

**Why $G$ acts on $G/H$.** Take the set of left cosets $G/H$; its elements are the "clumps" $xH$ that tile $G$. An element $g \in G$ sends the clump $xH$ to the clump $gxH$. Is this a well-defined rule on *clumps* (not on representatives)? Yes — if $xH = x'H$ then $x' = xh$ for some $h \in H$, so $gx'H = gxhH = gxH$, the clump is sent to the same place regardless of which representative names it. And the action axioms are immediate: $e\cdot xH = xH$, and $g_1\cdot(g_2\cdot xH) = g_1 g_2 xH = (g_1 g_2)\cdot xH$ by associativity. So left multiplication genuinely permutes the coset space, exactly as it permutes $G$ itself in [[Thm - Cayley's Theorem|Cayley's theorem]] — the coset action is Cayley's regular action with the points "blurred" into clumps of size $|H|$.

**Why the kernel is the normal core.** Ask which $g$ act *invisibly* — fix every coset. The element $g$ fixes the coset $xH$ when $gxH = xH$. Rearrange: $gxH = xH$ means $x^{-1}gxH = H$, which means $x^{-1}gx \in H$, which means $g \in xHx^{-1}$. So *$g$ fixes the particular coset $xH$ exactly when $g$ lies in the conjugate $xHx^{-1}$.* This is the key local computation, and the argument is completely reversible — each step is an "iff". Now $g$ is in the kernel when it fixes *every* coset, i.e. when $g \in xHx^{-1}$ for *every* $x$. That is precisely the intersection:
$$\ker\rho = \bigcap_{x \in G} xHx^{-1}.$$
So the kernel is forced to be this intersection of all conjugates of $H$ — there is no choice in the matter, it is just the bookkeeping of "fixes coset $xH$ $\iff$ lies in $xHx^{-1}$" run over all $x$.

**Why the intersection is the largest normal subgroup inside $H$.** Two facts. First, it *is* a normal subgroup: it is the kernel of the homomorphism $\rho$, and kernels are always normal. (You can also see normality directly — conjugating the intersection $\bigcap_x xHx^{-1}$ by any $g$ just permutes the conjugates $xHx^{-1}$ among themselves, so the intersection is unchanged.) Second, it is *inside $H$*: taking $x = e$ in the intersection gives the term $eHe^{-1} = H$, and the intersection is contained in each of its terms. Third, it is the *largest* such: if $N \trianglelefteq G$ and $N \leq H$, then for every $x$, normality gives $N = xNx^{-1} \leq xHx^{-1}$, so $N$ is contained in every conjugate of $H$, hence in their intersection. Any normal subgroup hiding inside $H$ is automatically swallowed by the core — which is why the core is the *maximal* normal subgroup contained in $H$, the largest normal "essence" of $H$.

**Why this gives the index theorem.** Now $|G/H| = n$, so $\operatorname{Sym}(G/H) \cong S_n$. The action is a homomorphism $\rho : G \to S_n$ with kernel $K = \operatorname{Core}_G(H) \leq H$. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] identifies $G/K \cong \operatorname{im}\rho \leq S_n$. So $G/K$ is a subgroup of $S_n$ — and by [[Thm - Lagrange's Theorem|Lagrange]], its order divides $|S_n| = n!$. The lower bound $|G/K| \geq n$ holds because the action is transitive on the $n$ cosets, so $\operatorname{im}\rho$ already moves $n$ points and cannot be smaller than $n$; concretely $|G/K| \geq |G/H| = n$ since $K \leq H$. The whole index theorem is just: coset action $\to$ homomorphism into $S_n$ $\to$ first isomorphism theorem.

**Why the corollary holds.** If $G$ is non-abelian [[Def - Simple Group|simple]] and $H$ is proper of index $n$, the normal subgroup $K$ produced is either $\{e\}$ or $G$. It cannot be $G$: some $g$ lies outside $H$ (as $H$ is proper), and that $g$ sends the coset $H$ to $gH \neq H$, so $g$ acts non-trivially and is not in the kernel. So $K = \{e\}$, and $G \cong G/K \hookrightarrow S_n$. To land in $A_n$: the image $\operatorname{im}\rho \cong G$ meets $A_n$ in a subgroup that is normal in $\operatorname{im}\rho$ (since $A_n \trianglelefteq S_n$), hence — by simplicity of $G$ — is either trivial or all of $\operatorname{im}\rho$. If it were trivial, then $\operatorname{im}\rho$ would inject into the quotient $S_n/A_n \cong C_2$ (this is the second isomorphism theorem: $\operatorname{im}\rho / (\operatorname{im}\rho\cap A_n) \cong \operatorname{im}\rho\,A_n / A_n \leq C_2$), making $G$ abelian — contradiction. So $\operatorname{im}\rho \cap A_n = \operatorname{im}\rho$, i.e. $G \hookrightarrow A_n$. Finally $n \geq 5$, because $A_1, A_2, A_3$ are trivial or of order $3$ and $A_4$ has no non-abelian simple subgroup — so $G$, being non-abelian simple, cannot fit into $A_n$ for $n \leq 4$.

---

# What Makes This Hard

The crux is the kernel computation, and the one move people get wrong is the direction of conjugation: from $gxH = xH$ one must derive $x^{-1}gx \in H$ (so $g \in xHx^{-1}$) — *not* $g \in x^{-1}Hx$. Getting this backwards inverts the intersection and breaks the "largest normal subgroup *inside* $H$" conclusion. In the corollary, the genuinely non-obvious step is the upgrade from $S_n$ to $A_n$: it requires the [[Thm - First Isomorphism Theorem|second isomorphism theorem]] to show that if $\operatorname{im}\rho$ missed $A_n$ it would be abelian, and skipping this lands $G$ only in $S_n$, which is too weak to force $n \geq 5$. The common error overall is forgetting to *separately* check $K \neq G$ (the action is non-trivial) and $K \neq \{e\}$ (or, in the simple case, that $K = \{e\}$ by simplicity) — both halves are needed.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Let $G$ act on $G/H$ by $g\cdot xH = gxH$; this is a homomorphism $\rho : G \to \operatorname{Sym}(G/H)$ by [[Thm - Actions Correspond to Homomorphisms]]. Compute the kernel by the reversible chain $gxH = xH \iff x^{-1}gx \in H \iff g \in xHx^{-1}$, intersected over all $x$, giving $\ker\rho = \bigcap_x xHx^{-1}$. This is normal (a kernel) and inside $H$ (take $x = e$); it is the largest such. For the index theorem, $|G/H| = n$ makes $\operatorname{Sym}(G/H) \cong S_n$, and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives $G/K \hookrightarrow S_n$. For the corollary, simplicity collapses $K$ to $\{e\}$, then a second-isomorphism-theorem argument lands $G$ in $A_n$, and small-$n$ inspection forces $n \geq 5$.

**Subgoal decomposition:**

1. **Left multiplication is a well-defined action on $G/H$.** Verify $g\cdot xH := gxH$ does not depend on the representative $x$, and satisfies the action axioms.
   - *Hint:* If $xH = x'H$ then $x' = xh$, so $gx'H = gxhH = gxH$; axioms are $e\cdot xH = xH$ and associativity.
   - *Why needed:* It produces, via [[Thm - Actions Correspond to Homomorphisms]], the homomorphism $\rho : G \to \operatorname{Sym}(G/H)$.

2. **Compute the kernel.** Show $g \in \ker\rho \iff g \in xHx^{-1}$ for all $x$, hence $\ker\rho = \bigcap_x xHx^{-1}$.
   - *Hint:* $g$ fixes $xH$ iff $gxH = xH$ iff $x^{-1}gx \in H$ iff $g \in xHx^{-1}$; every step is reversible; "fixes all cosets" gives the intersection.
   - *Why needed:* This is the identification of the kernel with the normal core.

3. **The core is the largest normal subgroup inside $H$.** Show $\operatorname{Core}_G(H) \trianglelefteq G$, that $\operatorname{Core}_G(H) \leq H$, and that any $N \trianglelefteq G$ with $N \leq H$ satisfies $N \leq \operatorname{Core}_G(H)$.
   - *Hint:* Normal because it is a kernel; inside $H$ because the $x = e$ term is $H$; largest because $N \trianglelefteq G$, $N \leq H$ force $N = xNx^{-1} \leq xHx^{-1}$ for all $x$.
   - *Why needed:* It characterises *which* normal subgroup the construction produces.

4. **Index theorem.** With $|G:H| = n$, conclude $G/K \hookrightarrow S_n$, so $|G/K| \mid n!$ and $|G/K| \geq n$.
   - *Hint:* $\operatorname{Sym}(G/H) \cong S_n$; apply the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] to $\rho$; [[Thm - Lagrange's Theorem|Lagrange]] gives $|G/K| \mid n!$; transitivity (or $K \leq H$) gives $|G/K| \geq n$.
   - *Why needed:* It is the arithmetic form of the theorem.

5. **Corollary: $K$ is trivial for $G$ simple.** Show that for $G$ non-abelian simple and $H$ proper, $K = \{e\}$, so $G \hookrightarrow S_n$.
   - *Hint:* $K \trianglelefteq G$, so $K \in \{\{e\}, G\}$; it is not $G$ because some $g \notin H$ moves the coset $H$; hence $K = \{e\}$.
   - *Why needed:* It converts the quotient embedding into an embedding of $G$ itself.

6. **Corollary: land $G$ inside $A_n$, force $n \geq 5$.** Show $\operatorname{im}\rho \leq A_n$ and that $n \leq 4$ is impossible.
   - *Hint:* $\operatorname{im}\rho\cap A_n \trianglelefteq \operatorname{im}\rho \cong G$; if trivial, the second isomorphism theorem embeds $G$ in $S_n/A_n \cong C_2$, making $G$ abelian — contradiction; so $\operatorname{im}\rho \leq A_n$. And $A_1,\dots,A_4$ contain no non-abelian simple group.
   - *Why needed:* It is the corollary's full statement — the index bound $n \geq 5$.

---

# Lemma Decomposition

Each lemma below is independently practiceable in roughly five minutes.

<details>
<summary><strong>Lemma 1: Left multiplication on cosets is a well-defined action</strong></summary>

**Statement:** For $H \leq G$, the rule $g\cdot(xH) = gxH$ is a well-defined [[Def - Group Action|action]] of $G$ on the set $G/H$ of left cosets.

**Hint:** Check independence of the representative first, then the two action axioms.

**Why needed:** It produces the homomorphism $\rho : G \to \operatorname{Sym}(G/H)$ that is the subject of the theorem.

<details>
<summary>Full proof</summary>

*Well-defined.* Suppose $xH = x'H$, so $x' = xh$ for some $h \in H$. Then $gx'H = g(xh)H = gx(hH) = gxH$, since $hH = H$. So $g\cdot(xH)$ does not depend on the chosen representative.

*Identity axiom:* $e\cdot(xH) = exH = xH$.

*Associativity axiom:* $g_1\cdot(g_2\cdot(xH)) = g_1\cdot(g_2 xH) = g_1 g_2 xH = (g_1 g_2)\cdot(xH)$, by associativity in $G$.

Hence $g\cdot(xH) = gxH$ is an action of $G$ on $G/H$.

</details>
</details>

<details>
<summary><strong>Lemma 2: An element fixes the coset $xH$ iff it lies in $xHx^{-1}$</strong></summary>

**Statement:** For the coset action, $g$ fixes the coset $xH$ (that is, $gxH = xH$) if and only if $g \in xHx^{-1}$.

**Hint:** Rearrange $gxH = xH$ by left-multiplying with $x^{-1}$; every step is an equivalence.

**Why needed:** Intersecting this condition over all $x$ gives the kernel of the action.

<details>
<summary>Full proof</summary>

The element $g$ fixes $xH$ iff $gxH = xH$. Left-multiplying both sides by $x^{-1}$, this holds iff $x^{-1}gxH = H$. A coset $yH$ equals $H$ iff $y \in H$, so this holds iff $x^{-1}gx \in H$. Finally $x^{-1}gx \in H \iff g \in xHx^{-1}$. Every implication is reversible, so $g$ fixes $xH \iff g \in xHx^{-1}$.

</details>
</details>

<details>
<summary><strong>Lemma 3: The kernel of the coset action is the intersection of all conjugates of $H$</strong></summary>

**Statement:** The kernel of $\rho : G \to \operatorname{Sym}(G/H)$ is $\ker\rho = \bigcap_{x\in G} xHx^{-1}$.

**Hint:** An element is in the kernel iff it fixes *every* coset; apply Lemma 2 to each.

**Why needed:** It is the explicit description of the normal subgroup the construction produces.

<details>
<summary>Full proof</summary>

By definition $g \in \ker\rho$ iff $\rho(g)$ is the identity permutation of $G/H$, i.e. iff $g$ fixes every coset $xH$. By Lemma 2, $g$ fixes $xH$ iff $g \in xHx^{-1}$. Therefore $g \in \ker\rho$ iff $g \in xHx^{-1}$ for *all* $x \in G$, which is exactly $g \in \bigcap_{x\in G} xHx^{-1}$. Hence $\ker\rho = \bigcap_{x\in G} xHx^{-1}$.

</details>
</details>

<details>
<summary><strong>Lemma 4: The normal core is the largest normal subgroup of $G$ contained in $H$</strong></summary>

**Statement:** $\operatorname{Core}_G(H) = \bigcap_{x\in G} xHx^{-1}$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$, is contained in $H$, and contains every normal subgroup of $G$ that is contained in $H$.

**Hint:** Normality and containment in $H$ are quick; for "largest", use normality of $N$ to put $N$ inside every conjugate of $H$.

**Why needed:** It justifies calling the kernel the *normal core* and explains exactly which normal subgroup is produced.

<details>
<summary>Full proof</summary>

*Normal.* As the kernel of the homomorphism $\rho$ (Lemma 3), $\operatorname{Core}_G(H) \trianglelefteq G$. (Directly: conjugating $\bigcap_x xHx^{-1}$ by $g$ sends it to $\bigcap_x (gx)H(gx)^{-1}$, the same intersection reindexed.)

*Contained in $H$.* The term for $x = e$ is $eHe^{-1} = H$, and an intersection is contained in each of its terms, so $\operatorname{Core}_G(H) \leq H$.

*Largest.* Let $N \trianglelefteq G$ with $N \leq H$. For any $x \in G$, normality of $N$ gives $N = xNx^{-1}$, and $N \leq H$ gives $xNx^{-1} \leq xHx^{-1}$; hence $N \leq xHx^{-1}$ for every $x$. Therefore $N \leq \bigcap_x xHx^{-1} = \operatorname{Core}_G(H)$.

</details>
</details>

<details>
<summary><strong>Lemma 5: Intersecting a simple image with $A_n$</strong></summary>

**Statement:** Let $G$ be a non-abelian [[Def - Simple Group|simple]] group and $\rho : G \to S_n$ an injective homomorphism. Then $\operatorname{im}\rho \leq A_n$.

**Hint:** $\operatorname{im}\rho\cap A_n$ is normal in $\operatorname{im}\rho \cong G$; rule out the trivial case using the second isomorphism theorem.

**Why needed:** It is the step that upgrades the corollary's embedding from $S_n$ to $A_n$, which is what forces $n \geq 5$.

<details>
<summary>Full proof</summary>

Since $A_n \trianglelefteq S_n$, the intersection $\operatorname{im}\rho \cap A_n$ is normal in $\operatorname{im}\rho$. As $\rho$ is injective, $\operatorname{im}\rho \cong G$ is simple, so $\operatorname{im}\rho\cap A_n$ is either $\{e\}$ or $\operatorname{im}\rho$.

Suppose it is $\{e\}$. By the second isomorphism theorem,
$$\operatorname{im}\rho \;\cong\; \frac{\operatorname{im}\rho}{\operatorname{im}\rho\cap A_n} \;\cong\; \frac{\operatorname{im}\rho\,A_n}{A_n} \;\leq\; \frac{S_n}{A_n} \;\cong\; C_2.$$
Then $\operatorname{im}\rho$, hence $G$, is a subgroup of $C_2$ — abelian, contradicting that $G$ is non-abelian. So $\operatorname{im}\rho\cap A_n = \operatorname{im}\rho$, i.e. $\operatorname{im}\rho \leq A_n$.

</details>
</details>

---

# Formal Proof

<details>
<summary><strong>Complete formal proof</strong></summary>

**Theorem.** For $H \leq G$, the group $G$ acts on $G/H$ by $g\cdot xH = gxH$, and the kernel of the associated homomorphism $\rho : G \to \operatorname{Sym}(G/H)$ is $\bigcap_{x\in G} xHx^{-1}$, the largest normal subgroup of $G$ contained in $H$.

*Proof.* The rule $g\cdot xH = gxH$ is well-defined: if $xH = x'H$ then $x' = xh$ with $h \in H$, so $gx'H = gxhH = gxH$. It satisfies $e\cdot xH = xH$ and $g_1\cdot(g_2\cdot xH) = g_1 g_2 xH = (g_1 g_2)\cdot xH$, so it is an action. By [[Thm - Actions Correspond to Homomorphisms]] it is a homomorphism $\rho : G \to \operatorname{Sym}(G/H)$.

Now $g \in \ker\rho$ iff $g$ fixes every coset, i.e. $gxH = xH$ for all $x \in G$. For a fixed $x$: $gxH = xH \iff x^{-1}gxH = H \iff x^{-1}gx \in H \iff g \in xHx^{-1}$, each step reversible. Hence
$$\ker\rho = \bigcap_{x\in G} xHx^{-1}.$$
This is a normal subgroup, being a kernel. Taking $x = e$ shows it lies in $H$. If $N \trianglelefteq G$ and $N \leq H$, then $N = xNx^{-1} \leq xHx^{-1}$ for all $x$, so $N \leq \bigcap_x xHx^{-1}$; thus $\ker\rho$ is the largest normal subgroup of $G$ inside $H$. $\qquad\blacksquare$

**Index theorem.** Let $G$ be finite, $H \leq G$ of index $n$, and $K = \ker\rho$. Then $K \trianglelefteq G$, $K \leq H$, and $\operatorname{Sym}(G/H) \cong S_n$. By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]],
$$G/K \;\cong\; \operatorname{im}\rho \;\leq\; \operatorname{Sym}(G/H) \;\cong\; S_n.$$
By [[Thm - Lagrange's Theorem|Lagrange's theorem]], $|G/K|$ divides $|S_n| = n!$. And $|G/K| \geq |G/H| = n$, since $K \leq H$ gives $|G:K| \geq |G:H|$. $\qquad\blacksquare$

**Corollary.** Let $G$ be a non-abelian simple group and $H \leq G$ a proper subgroup of index $n > 1$. The coset action gives $\rho : G \to \operatorname{Sym}(G/H) \cong S_n$ with $\ker\rho \trianglelefteq G$. By simplicity, $\ker\rho$ is $\{e\}$ or $G$. It is not $G$: since $H$ is proper there is $g \in G\setminus H$, and then $g\cdot H = gH \neq H$, so $g \notin \ker\rho$. Hence $\ker\rho = \{e\}$, and by the first isomorphism theorem $G \cong \operatorname{im}\rho \leq S_n$.

We strengthen this to $G \hookrightarrow A_n$. Since $A_n \trianglelefteq S_n$, the subgroup $\operatorname{im}\rho\cap A_n$ is normal in $\operatorname{im}\rho \cong G$, hence $\{e\}$ or $\operatorname{im}\rho$. If it were $\{e\}$, the second isomorphism theorem would give
$$\operatorname{im}\rho \cong \frac{\operatorname{im}\rho}{\operatorname{im}\rho\cap A_n} \cong \frac{\operatorname{im}\rho\,A_n}{A_n} \leq \frac{S_n}{A_n} \cong C_2,$$
making $G$ abelian — a contradiction. So $\operatorname{im}\rho\cap A_n = \operatorname{im}\rho$, i.e. $G \cong \operatorname{im}\rho \leq A_n$.

Finally, $n \geq 5$. The groups $S_1, S_2, S_3, S_4$ — equivalently $A_1, A_2, A_3, A_4$ — contain no non-abelian simple subgroup, as one verifies by listing all their subgroups: $A_1, A_2$ are trivial, $A_3 \cong C_3$ is abelian, and every subgroup of $S_4$ (hence of $A_4$) is solvable. So a non-abelian simple $G$ cannot embed in $A_n$ for $n \leq 4$; therefore $n \geq 5$. $\qquad\blacksquare$

This is the theorem and corollary of §1.3 of the source lecture notes, with the coset-action kernel computation as the central reversible argument.

</details>

---

# Cross-Field Exercise Suggestions

The aim is to find settings where the coset action is the productive move, even when no coset space is mentioned.

**Galois theory: bounding the Galois group of a polynomial.** A degree-$n$ irreducible polynomial has a root whose stabiliser in the Galois group $G$ is a subgroup $H$ of index $n$ (the roots form a single orbit of size $n$). The coset action of $G$ on $G/H$ recovers the action of $G$ on the $n$ roots and embeds $G$ in $S_n$ — this is *why* a Galois group of a degree-$n$ polynomial is a subgroup of $S_n$. The application is non-obvious because the field-theoretic setup mentions roots and automorphisms, not coset spaces; recognizing "stabiliser of a root" as an index-$n$ subgroup is the bridge, and the normal core is the kernel of the action on the roots, i.e. the Galois group of the largest normal subextension.

**Classification of small groups: ruling out simple groups of a given order.** To show no simple group of order $N$ exists for a specific composite $N$, one finds (often via Sylow theory) a subgroup $H$ of small index $n$ with $N \nmid n!$; the coset action then forces a proper non-trivial normal subgroup. For instance, a group of order $36$ has a subgroup of index $4$ (a Sylow $3$-subgroup), and $36 \nmid 4! = 24$, so the coset action's kernel is a proper non-trivial normal subgroup — the group is not simple. The application is non-obvious because the problem gives only an integer $N$; the index-$n$ subgroup must be produced, and the divisibility failure $N \nmid n!$ is the trigger.

**Combinatorics and geometry: primitive permutation groups.** A transitive action is *primitive* when the point stabiliser is a maximal subgroup; primitive groups are the "atoms" of permutation group theory and govern the symmetry of highly regular combinatorial objects (block designs, strongly regular graphs). The coset action is the universal model: every transitive action is the coset action on $G/H$, and primitivity is maximality of $H$. The application is non-obvious because primitivity is usually defined via the absence of non-trivial block systems; translating it into "the stabiliser $H$ is a maximal subgroup, so the coset action has no intermediate structure" is the coset-action viewpoint, and the normal core is the kernel that decides whether the primitive action is faithful.

**Computer science: the orbit of a configuration under a transformation group.** In algorithms that explore a state space under a group of symmetries — puzzle solving, isomorphism rejection, symmetry-reduced search — the set of states equivalent to a fixed one is the orbit, and fixing one state gives a subgroup (its stabiliser) of index equal to the orbit size. The coset action models the search as $G$ permuting $G/H$, and the index theorem bounds how the symmetry-reduced state space can sit inside $S_n$. The application is non-obvious because the search problem is phrased operationally, with no group quotient in sight; the stabiliser-of-a-state-as-subgroup identification is what makes the coset action and its core relevant.

---

# Bridges

- **[[Thm - Cayley's Theorem|Cayley's Theorem]]** — Cayley is the coset action at $H = \{e\}$. There the coset space $G/\{e\}$ is all of $G$, the action is the left-regular action, and the normal core $\bigcap_x x\{e\}x^{-1} = \{e\}$ is trivial — so the embedding is faithful but into the enormous $S_{|G|}$. The coset action generalises Cayley by allowing a *non-trivial* $H$: this shrinks the coset space to $|G:H|$ points and the target to $S_{|G:H|}$, at the cost of a possibly non-trivial kernel. Cayley is the extreme, least efficient instance.

- **[[Thm - Actions Correspond to Homomorphisms|Actions Correspond to Homomorphisms]]** — the coset action's entire force comes from this correspondence: the action on $G/H$ is a *homomorphism*, so it *has a kernel*, and that kernel is automatically a normal subgroup. Without the action-homomorphism dictionary there would be no kernel to take and no normal subgroup to produce. The coset action is the headline application of "an action has a kernel".

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]]** — the index theorem is the coset action followed immediately by the first isomorphism theorem: $G/K \cong \operatorname{im}\rho \leq S_n$. The corollary additionally uses the *second* isomorphism theorem to upgrade $S_n$ to $A_n$. The isomorphism theorems are the structural machinery that converts "there is a homomorphism into $S_n$" into the precise embedding statements.

- **[[Thm - Lagrange's Theorem|Lagrange's Theorem]]** — Lagrange supplies the divisibility punch: once $G/K \hookrightarrow S_n$, it is Lagrange that concludes $|G/K| \mid n!$. The coset action manufactures the embedding; Lagrange extracts the arithmetic consequence. Together they are the route from "small index" to a numerical contradiction.

- **[[Thm - Simplicity of the Alternating Group|Simplicity of the Alternating Group]]** — the corollary that a non-abelian simple group has no proper subgroup of index $< 5$ is the converse-facing companion to the simplicity of $A_n$: the simplicity theorem *produces* the simple groups $A_n$ ($n \geq 5$), while this corollary *constrains* how any non-abelian simple group can sit inside a symmetric group. The number $5$ in the corollary and the threshold $n \geq 5$ for simplicity of $A_n$ are the same exceptional boundary, seen from the two sides.

- **Sylow Theory** *(from [[Group Theory III — §1.5–1.7]])* — the coset action is one of the recurring engines of the Sylow-theoretic classification of finite groups: many non-simplicity proofs locate a subgroup of small index (frequently the normaliser of a Sylow subgroup) and apply the index theorem to extract a normal subgroup or a contradiction from $|G| \nmid n!$. The technique of this page is, in the next topic, deployed group order by group order.
