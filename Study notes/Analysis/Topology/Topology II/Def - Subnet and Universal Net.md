---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Directed Set and Net"
  - "Def - Net Convergence"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a topological space, $D$ and $D'$ are directed sets, $\Phi : D \to X$ is a net (the "parent"), and $h : D' \to D$ is a function. The composition $\Phi \circ h : D' \to X$ is the candidate subnet. The notation $\beta \geq \alpha$ in a directed set means $\beta$ is later than (or equal to) $\alpha$. We use $\delta, \delta'$ generically for "thresholds" in directed sets — points beyond which we want the net to behave in some way. The full registry of symbols is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Axiom Motivation

We have a net $\Phi : D \to X$. We want a notion of "subnet" that generalizes "subsequence" — a way to extract a sub-collection of the values of $\Phi$ that retains the structural properties of being a net and respects the directed-set ordering. The naive guess, modelled on subsequences, would be: a subnet is obtained by composing $\Phi$ with a *strictly increasing* function $h : \mathbb{N} \to D$ (so we still index by $\mathbb{N}$). But this fails immediately: if $D$ is uncountable (say, neighbourhoods of a point in a non-first-countable space), there is no strictly increasing function $\mathbb{N} \to D$ that captures cofinal data.

The slightly less naive guess: a subnet is the composition $\Phi \circ h$ where $h : D' \to D$ is a strictly increasing function from another directed set $D'$. This is closer, but still wrong, because *strict monotonicity* is too rigid. Reflect on what we actually want from a subnet: we want it to "preserve eventually" — if the parent net $\Phi$ is eventually in $A$, the subnet should also be eventually in $A$. We do *not* need the subnet to skip every other element or maintain order strictly. What we need from $h : D' \to D$ is that it eventually escapes any fixed threshold in $D$: for every $\delta \in D$ there exists $\delta' \in D'$ such that $h(\alpha') \geq \delta$ whenever $\alpha' \geq \delta'$. This is the **final** condition. It says: "$h$ goes to infinity in $D$ along the directed set $D'$". The final function gets you cofinally far in $D$ without committing to any ordering structure on the way.

With this, the definition of subnet is: $\Phi \circ h$ where $h : D' \to D$ is final. The condition is general enough to subsume "subsequence" (where $h(k) = n_k$ with $n_k$ strictly increasing — clearly final, since you eventually exceed any fixed $N$) and to allow much more (the subnet may be indexed by a "richer" directed set, may revisit values of $\Phi$, may not be monotonic in any sense). The crucial property: the subnet of a convergent net converges to the same limit (and more, the subnet of a net is "frequently in $A$" iff the parent is), but the subnet of a *cluster-point-having* net can be chosen to *converge* to that cluster point — which is the content of the **net-cluster-point–subnet correspondence**. Without the looseness of subnets, the compactness equivalence "every net has a convergent subnet" would fail in non-first-countable spaces.

Now the second concept: the **universal net**. A net is universal if for every subset $A$ of $X$, the net is eventually in $A$ or eventually in $X \setminus A$. This is a very strong condition — strong enough that one might suspect universal nets do not exist outside trivial cases. But every net has a universal *subnet*, by a Zorn's lemma argument (see [[Thm - Every Net Has a Universal Subnet]]). The argument: take a maximal collection $\mathcal{C}$ of subsets of $X$ each of which the net is frequently in (closed under finite intersection); use this to build a "richer" directed set indexing a universal subnet.

What is so special about universal nets? Two crucial properties. First, the image of a universal net under any function is universal (see the proposition in §6.12 of the source): if $\Phi$ is universal in $X$ and $f : X \to Y$ is any function (not necessarily continuous), then $f \circ \Phi$ is universal in $Y$. This means universal nets are *transported* by all maps, not just continuous ones — a remarkable robustness. Second, combining universality with compactness gives convergence directly. In a compact space, every universal net converges (we'll see this in the proof of the compactness equivalence): given a universal $\Phi$, suppose for contradiction it doesn't converge. Then for each $x \in X$ there is an open $U_x$ such that $\Phi$ is *not* eventually in $U_x$, hence (by universality) is eventually in $X \setminus U_x$. The opens $\{U_x\}$ cover $X$; by compactness, finitely many $U_{x_1}, \ldots, U_{x_n}$ cover $X$. The net is eventually in each $X \setminus U_{x_i}$, hence eventually in $\bigcap_i (X \setminus U_{x_i}) = \emptyset$, contradiction.

So the chain of equivalences for compactness uses universal nets as the bridge: (open cover) ↔ (FIP for closed) ↔ (every universal net converges) ↔ (every net has a convergent subnet). The third condition is the "true name" of compactness — the form that is operative for extracting limits. The fourth condition is what you actually deploy in analysis. The middle condition (universal-via-universal-subnet) is the technical glue, and it requires the Axiom of Choice.

One last note: it is **not** true that the right definition of subnet is "$h : D' \to D$ is monotonic and final". One can drop monotonicity entirely — the final condition alone is sufficient for all the properties we want. In fact, requiring monotonicity is too restrictive: there are useful constructions of subnets where $h$ wiggles back and forth in $D$ but still cofinally exhausts it. So the official definition is "$h$ final", with no monotonicity hypothesis.

---

# The Definition

Let $X$ be a topological space, $D$ and $D'$ directed sets, $\Phi : D \to X$ a net.

**Final function.** A function $h : D' \to D$ between directed sets is **final** (or **cofinal**) if for every $\delta \in D$ there exists $\delta' \in D'$ such that $\alpha' \geq \delta'$ in $D'$ implies $h(\alpha') \geq \delta$ in $D$. (Note: monotonicity of $h$ is *not* required.)

**Subnet.** A **subnet** of the net $\Phi : D \to X$ is a composition $\Phi \circ h$ where $h : D' \to D$ is a final function from some directed set $D'$. The subnet is itself a net (indexed by $D'$, valued in $X$).

**Universal net.** A net $\Phi : D \to X$ is **universal** (also called an **ultranet**) if for every subset $A \subseteq X$, $\Phi$ is either eventually in $A$ or eventually in $X \setminus A$.

**Equivalent characterisations of universal:**

1. For every $A \subseteq X$, $\Phi$ is eventually in $A$ or eventually in $X \setminus A$.
2. The collection $\{A \subseteq X : \Phi \text{ is eventually in } A\}$ is an *ultrafilter* on $X$.

**Existence of universal subnets.** Every net in any topological space has a universal subnet. The proof uses Zorn's lemma; see [[Thm - Every Net Has a Universal Subnet]].

**Subsequence as a special case.** A subsequence $\{x_{n_k}\}$ of a sequence $\{x_n\}$ is a subnet with $D' = \mathbb{N}$, $h(k) = n_k$ where $n_1 < n_2 < \ldots$. The strict monotonicity of $h$ ensures finality. So every subsequence is a subnet, but not every subnet of a sequence is a subsequence.

---

# Relate to Other Fields / Compression

The notion of **universal net** is the net-theoretic mirror of **ultrafilter**. A net $\Phi : D \to X$ defines a filter $\mathcal{F}_\Phi = \{A \subseteq X : \Phi \text{ is eventually in } A\}$ on $X$; $\Phi$ is universal iff $\mathcal{F}_\Phi$ is an ultrafilter (a maximal proper filter — equivalently, a filter such that for every $A$, either $A \in \mathcal{F}$ or $X \setminus A \in \mathcal{F}$). The existence of ultrafilters extending every filter (the Boolean prime ideal theorem) is the filter-theoretic statement of the existence of universal subnets, and both are equivalent to a fragment of the Axiom of Choice (the "ultrafilter lemma").

In **model theory**, ultrafilters are the engine of the **ultraproduct construction**: given structures $\{M_i\}_{i \in I}$ and an ultrafilter $\mathcal{U}$ on $I$, the ultraproduct $\prod M_i / \mathcal{U}$ is a structure where "almost-everywhere-true" (in the sense of $\mathcal{U}$) statements are true. **Łoś's theorem** says first-order statements lift from each $M_i$ to the ultraproduct. This is how nonstandard analysis is built: take an ultraproduct of $\mathbb{R}$ with itself indexed by $\mathbb{N}$, modulo a non-principal ultrafilter, to get the hyperreal numbers.

In **set theory**, ultrafilters on $\omega$ (i.e., on $\mathbb{N}$) are studied for their own sake: principal ultrafilters (every set containing a fixed point), and non-principal ultrafilters (existing iff the ultrafilter lemma holds). The cardinality of the set of non-principal ultrafilters on $\omega$ is $2^{2^{\aleph_0}}$, a famous computation.

In **functional analysis**, the **Stone–Čech compactification** $\beta X$ of a discrete space $X$ is the space of ultrafilters on $X$ with a natural topology, and it is the "universal" compact Hausdorff space receiving a continuous map from $X$. So ultrafilters / universal nets are literally the points of $\beta X$.

---

# Examples / Corollaries

**Is an instance of a subnet — every subsequence.** As above, a subsequence $\{x_{n_k}\}$ with $n_1 < n_2 < \ldots$ is a subnet with $h(k) = n_k$. The final condition is straightforward: for any $N \in \mathbb{N}$, choose $K$ such that $n_K \geq N$; then for $k \geq K$, $h(k) = n_k \geq n_K \geq N$.

**Is an instance of a subnet that is NOT a subsequence — a sequence indexed by pairs.** Take the sequence $x_n = 1/n$ in $\mathbb{R}$. Define a subnet indexed by $\mathbb{N} \times \mathbb{N}$ (with componentwise ordering) via $h(k, j) = k + j$. Then $h$ is final (given $N$, take $K = N, J = 0$). The resulting subnet is a "thicker" net than any subsequence, indexed by an uncountable directed set (well, countable here, but the principle is clear). For more striking examples, take sequences and form subnets indexed by uncountable directed sets — these exist via Zorn's lemma constructions and have no subsequence analogue.

**Is an instance of a universal net — a constant sequence.** $x_n = c$ for all $n$, with any constant $c$. For any $A \subseteq X$, either $c \in A$ (and the sequence is eventually — in fact always — in $A$) or $c \notin A$ (and the sequence is eventually in $X \setminus A$). So constant sequences are universal. More generally, eventually-constant sequences are universal.

**Is NOT an instance of a universal net — most sequences.** A sequence is universal iff eventually constant (see [[Ex - A sequence is universal iff eventually constant]]). So the sequence $x_n = (-1)^n$ is *not* universal: it is frequently in $\{1\}$ and frequently in $\{-1\}$, but not eventually in either. To get a universal net out of $\{(-1)^n\}$, we need a universal *subnet* — which by [[Thm - Every Net Has a Universal Subnet]] exists, but is genuinely non-constructive (uses Zorn).

**Is an instance of a universal net — an ultrafilter-induced net.** Let $\mathcal{U}$ be a non-principal ultrafilter on $\mathbb{N}$ (exists by Zorn) and define the directed set $\mathcal{U}$ (the elements of $\mathcal{U}$ ordered by reverse inclusion: $A \leq B$ iff $A \supseteq B$). For each $A \in \mathcal{U}$, pick $\Phi(A) \in A$. The resulting net $\Phi : \mathcal{U} \to \mathbb{N}$ (or into $\mathbb{R}$) is universal: for any set $B \subseteq \mathbb{N}$, either $B \in \mathcal{U}$ (so $\Phi$ is eventually in $B$ — for $A \leq B$ in $\mathcal{U}$, $\Phi(A) \in A \subseteq B$) or $\mathbb{N} \setminus B \in \mathcal{U}$ by maximality.

**Counter-example — a non-final function is NOT a subnet map.** Take $D = D' = \mathbb{N}$ and $h(k) = 0$ for all $k$ (constant). Then $\Phi \circ h$ is the constant net at $\Phi(0)$, which has nothing to do with the parent net. Is $h$ final? No: for $\delta = 1 \in D$, there is no $\delta'$ such that $\alpha' \geq \delta' \Rightarrow h(\alpha') \geq 1$ (since $h$ always returns $0$). So constant maps are not final, and constant nets are not subnets in this sense.

**Corollary — every subnet of a universal net is universal.** Given a universal $\Phi : D \to X$ and a subnet $\Phi \circ h : D' \to X$ via final $h$: for any $A \subseteq X$, $\Phi$ is eventually in $A$ (say) — then there is $\delta \in D$ such that $\Phi(\beta) \in A$ for $\beta \geq \delta$. By finality of $h$, there is $\delta' \in D'$ such that $h(\alpha') \geq \delta$ for $\alpha' \geq \delta'$. So $(\Phi \circ h)(\alpha') = \Phi(h(\alpha')) \in A$ for $\alpha' \geq \delta'$. Hence the subnet is eventually in $A$. (See §6.14 in source.)

**Corollary — the image of a universal net under any function is universal.** If $\Phi : D \to X$ is universal and $f : X \to Y$ is any function (not necessarily continuous), then $f \circ \Phi$ is universal in $Y$. Reason: for $B \subseteq Y$, $\Phi$ is eventually in $f^{-1}(B)$ or eventually in $X \setminus f^{-1}(B) = f^{-1}(Y \setminus B)$. Either way, $f \circ \Phi$ is eventually in $B$ or in $Y \setminus B$.

**Corollary — universal + compactness ⇒ convergence.** In a compact space $X$, every universal net converges. The reason — sketched above and part of the **compactness equivalence** in [[Def - Compact Space]] — is that for each $x \in X$ there is a neighbourhood $U_x$ where the net either eventually lives or eventually doesn't. Cover $X$ by finitely many $U_{x_i}$; the net cannot eventually live in the complement of all of them (that would be in $\emptyset$), so it eventually lives in some $U_{x_i}$, and a similar local argument gives convergence to $x_i$.

**Calibration check.** Identify why each of the following matters: (i) the final condition is *weaker* than monotonicity, so more functions count as subnet maps; (ii) every net has a universal subnet by Zorn, but not constructively — you cannot "exhibit" one in concrete cases; (iii) the image of a universal net under *any* (not necessarily continuous) map is universal, which contrasts sharply with ordinary net convergence where continuity is required.

---

# Unlocked by This

> [!tip] **Compactness Equivalence** *(this topic)*
> The existence of universal subnets is the technical content behind the equivalence "$X$ compact ⟺ every net has a convergent subnet ⟺ every universal net converges". See [[Def - Compact Space]] and [[Thm - Every Net Has a Universal Subnet]]. The proof goes: net → universal subnet (Zorn) → convergent (compactness).

> [!tip] **Ultrafilters and the Boolean Prime Ideal Theorem** *(from Logic / Set Theory)*
> The existence of non-principal ultrafilters on every set is the **Boolean prime ideal theorem**, equivalent under ZF to the ultrafilter lemma. It is strictly weaker than the Axiom of Choice but already strong enough to prove most "Zorn-style" theorems in functional analysis (Hahn–Banach, Banach–Alaoglu).

> [!tip] **Ultraproducts and Łoś's Theorem** *(from Model Theory)*
> Given structures $\{M_i\}_{i \in I}$ and an ultrafilter $\mathcal{U}$ on $I$, the **ultraproduct** $\prod_i M_i / \mathcal{U}$ is a structure where a first-order property holds iff the set of $i$ for which it holds in $M_i$ is in $\mathcal{U}$ (Łoś's theorem). Ultraproducts of $\mathbb{R}$ with non-principal ultrafilters give the **hyperreals** of nonstandard analysis.
