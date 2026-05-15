---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Def - Normal Subgroup"
  - "Def - Simple Group"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a [[Def - Simple Group|simple group]] and let $\varphi : G \to H$ be a homomorphism to any group $H$. Prove that $\varphi$ is either **trivial** — meaning $\varphi(g) = e_H$ for every $g \in G$, so $\operatorname{im}\varphi = \{e_H\}$ — or **injective**.

In other words: a homomorphism out of a simple group is either constant or an embedding; there is no middle ground.

**Recall:**

The problem is about homomorphisms out of a simple group, so the objects in play are homomorphisms, kernels, normality, and simplicity.

![[Def - Homomorphism#The Definition]]

![[Def - Kernel and Image#The Definition]]

Two facts about the kernel are used. First, $\ker\varphi$ is always a [[Def - Normal Subgroup|normal subgroup]] of the domain $G$. Second, the kernel detects injectivity: $\varphi$ is injective if and only if $\ker\varphi = \{e\}$.

![[Def - Normal Subgroup#The Definition]]

![[Def - Simple Group#The Definition]]

The content of simplicity is that the *only* normal subgroups of a simple group $G$ are the two extreme ones — the trivial subgroup $\{e\}$ and the whole group $G$. There are no normal subgroups strictly in between.

---

# Convergent Strategy

**Problem class.** This is a *structural dichotomy* problem: you must show one of two clean outcomes always holds, with nothing intermediate. Such "either trivial or injective" statements are the characteristic way simplicity makes itself felt, because simplicity is itself a dichotomy — every normal subgroup is one of two things — and any object controlled by a normal subgroup inherits that two-way split.

**Assumption pattern.** Two hypotheses, and each is recognisable. First, *$G$ is simple*: this is a statement that severely restricts the normal subgroups of $G$ — there are exactly two of them. Second, *a homomorphism $\varphi$ is given*: as the [[Group Theory I — §1.1–1.2#Sources and Targets|sources of the topic]] note, the instant you have a homomorphism you have a normal subgroup for free, namely $\ker\varphi \trianglelefteq G$. The two hypotheses interlock: one produces a normal subgroup, the other says that subgroup has only two possible values.

**Theorem routing.** The route does not even need a named theorem in its lightest form — it runs straight through the definitions. The kernel $\ker\varphi$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$ (a fact from [[Def - Kernel and Image]]). Simplicity ([[Def - Simple Group]]) forces $\ker\varphi \in \{\{e\},\ G\}$. Then the kernel's two meanings finish the job: $\ker\varphi = G$ means $\varphi$ kills everything (trivial map), and $\ker\varphi = \{e\}$ means $\varphi$ is injective. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] supplies an optional second viewpoint — it identifies $\operatorname{im}\varphi$ with $G/\ker\varphi$, which is either the trivial group or a copy of $G$ — and is worth recording because it shows the dichotomy is really about what quotients $G$ admits.

**Key decision point.** The one move that makes the proof is *naming the kernel and recognising it as the only normal subgroup in sight*. A beginner stares at $\varphi$ and tries to reason about its values directly; the expert immediately writes "consider $\ker\varphi$", because that single subgroup is where the hypothesis of simplicity can bite. Everything after that is forced. The subtlety is purely in knowing to look at the kernel rather than the image or the map itself.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory I — §1.1–1.2#Legal Operations|the topic page's Legal Operations]]:

1. **Build a homomorphism to expose structure** (operation 3), used in reverse. Here the homomorphism $\varphi$ is *given* rather than built, but we exploit exactly the property the operation advertises: a homomorphism comes packaged with a normal subgroup, its kernel $\ker\varphi$.

2. **Conjugate to test or exploit normality** (operation 6), in packaged form. We do not conjugate elements by hand; we use the standing fact from [[Def - Kernel and Image]] that every kernel is normal — the conjugation argument carried out once and for all.

3. **Apply the first isomorphism theorem to identify a quotient** (operation 4), in the optional second viewpoint of Step 3. It recasts the image as the quotient $G/\ker\varphi$, exposing the dichotomy as a statement about which quotients a simple group has.

---

# Hints

> [!note]- Hint 1
> You are given a homomorphism and told the domain is simple. Simplicity is a statement about *normal subgroups*. Which normal subgroup does a homomorphism always hand you for free?

> [!note]- Hint 2
> Consider $\ker\varphi$. It is a normal subgroup of $G$. Since $G$ is simple, how many possibilities are there for what $\ker\varphi$ can be? List them.

> [!note]- Hint 3
> Two cases. If $\ker\varphi = G$, every element is sent to $e_H$ — the map is trivial. If $\ker\varphi = \{e\}$, recall that a homomorphism is injective precisely when its kernel is trivial. There is no third case, because $G$ is simple.

---

# Solution

The plan is to look at the one normal subgroup the homomorphism supplies — its kernel — let simplicity collapse it to one of two values, and translate each value into a statement about $\varphi$.

**Step 1: The kernel $\ker\varphi$ is a normal subgroup of $G$.**

For any homomorphism, the kernel is a normal subgroup of the domain. So $\ker\varphi \trianglelefteq G$.

> [!note]- Derivation
> By [[Def - Kernel and Image]], the kernel $\ker\varphi = \{g \in G : \varphi(g) = e_H\}$ is the set of elements sent to the identity of $H$. It is a [[Def - Normal Subgroup|normal subgroup]] of $G$ — a standard lemma. Briefly: it is a subgroup because if $\varphi(g) = \varphi(h) = e_H$ then $\varphi(gh^{-1}) = \varphi(g)\varphi(h)^{-1} = e_H$, and it contains $e_G$; it is normal because for any $g \in \ker\varphi$ and any $x \in G$,
> $$\varphi(x g x^{-1}) = \varphi(x)\,\varphi(g)\,\varphi(x)^{-1} = \varphi(x)\,e_H\,\varphi(x)^{-1} = e_H,$$
> so $x g x^{-1} \in \ker\varphi$, which is the conjugation criterion for normality. Hence $\ker\varphi \trianglelefteq G$. This is the foothold: the hypothesis "$G$ is simple" is a statement about normal subgroups, and we have just produced one.

**Step 2: Simplicity forces $\ker\varphi = \{e\}$ or $\ker\varphi = G$.**

A simple group has only two normal subgroups, $\{e\}$ and $G$. Since $\ker\varphi$ is one of them, $\ker\varphi \in \{\{e\},\ G\}$.

> [!note]- Derivation
> By [[Def - Simple Group]], a non-trivial group $G$ is **simple** when its only normal subgroups are the trivial subgroup $\{e\}$ and $G$ itself — there is no proper non-trivial normal subgroup. Step 1 established that $\ker\varphi$ is a normal subgroup of $G$. A normal subgroup of a simple group therefore has nowhere to be except one of the two extremes:
> $$\ker\varphi = \{e\} \qquad \text{or} \qquad \ker\varphi = G.$$
> These two cases are exhaustive and mutually exclusive (they would coincide only for the trivial group, which is excluded since simple groups are non-trivial). This is the entire force of the simplicity hypothesis: it converts the a priori unknown subgroup $\ker\varphi$ into a two-valued object.

**Step 3: Translate each case into a statement about $\varphi$.**

If $\ker\varphi = G$, then $\varphi$ is the trivial homomorphism. If $\ker\varphi = \{e\}$, then $\varphi$ is injective. These are the two claimed outcomes.

> [!note]- Derivation
> *Case $\ker\varphi = G$.* The kernel being all of $G$ means *every* element of $G$ is sent to $e_H$:
> $$\varphi(g) = e_H \quad \text{for all } g \in G.$$
> So $\varphi$ is the **trivial homomorphism**, and its image is $\operatorname{im}\varphi = \{e_H\}$.
>
> *Case $\ker\varphi = \{e\}$.* Here we use the kernel's role as the detector of injectivity, the second fact from [[Def - Kernel and Image]]: a homomorphism $\varphi$ is **injective if and only if $\ker\varphi = \{e\}$**. The reason is that $\varphi(a) = \varphi(b)$ rearranges, via the homomorphism property, to $\varphi(a b^{-1}) = e_H$, i.e. $a b^{-1} \in \ker\varphi$; if the kernel is trivial this forces $a b^{-1} = e$, that is $a = b$. So $\ker\varphi = \{e\}$ gives that $\varphi$ is **injective**.
>
> By Step 2 one of these two cases must hold, so $\varphi$ is either trivial or injective, with no third possibility. $\blacksquare$
>
> *Optional second viewpoint via the first isomorphism theorem.* The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] states $G/\ker\varphi \cong \operatorname{im}\varphi$. In the case $\ker\varphi = G$ this reads $G/G \cong \operatorname{im}\varphi$, and $G/G$ is the trivial group, so $\operatorname{im}\varphi = \{e_H\}$. In the case $\ker\varphi = \{e\}$ it reads $G/\{e\} \cong \operatorname{im}\varphi$, and $G/\{e\} \cong G$, so $\operatorname{im}\varphi$ is an isomorphic copy of $G$ sitting inside $H$ — which is exactly what it means for $\varphi$ to be injective. This viewpoint shows the dichotomy is really the statement that a simple group has only two quotients, the trivial one and itself.

> [!note]- Complete formal solution
> Let $G$ be a simple group and $\varphi : G \to H$ a homomorphism.
>
> The kernel $\ker\varphi = \{g \in G : \varphi(g) = e_H\}$ is a normal subgroup of $G$: it is a subgroup, and for $g \in \ker\varphi$, $x \in G$ one computes $\varphi(xgx^{-1}) = \varphi(x)\varphi(g)\varphi(x)^{-1} = \varphi(x)e_H\varphi(x)^{-1} = e_H$, so $xgx^{-1} \in \ker\varphi$ and $\ker\varphi \trianglelefteq G$.
>
> Since $G$ is simple, its only normal subgroups are $\{e\}$ and $G$. Hence $\ker\varphi = \{e\}$ or $\ker\varphi = G$.
>
> - If $\ker\varphi = G$, then $\varphi(g) = e_H$ for all $g \in G$, so $\varphi$ is the trivial homomorphism with $\operatorname{im}\varphi = \{e_H\}$.
> - If $\ker\varphi = \{e\}$, then $\varphi$ is injective: $\varphi(a) = \varphi(b) \implies \varphi(ab^{-1}) = e_H \implies ab^{-1} \in \ker\varphi = \{e\} \implies a = b$.
>
> These two cases are exhaustive, so $\varphi$ is either trivial or injective. $\blacksquare$

---

# Key Takeaways

**The kernel is the bridge that lets a hypothesis on normal subgroups govern a homomorphism.** The whole proof pivots on one reflex: when a homomorphism is in play and the hypothesis concerns normal subgroups, look at $\ker\varphi$. A homomorphism by itself is an unwieldy object — a function with infinitely many values — but it carries with it a single normal subgroup, its kernel, and that subgroup is the handle by which any normal-subgroup hypothesis grips the map. Here the hypothesis was "$G$ is simple"; the kernel converted it into "$\varphi$ has trivial or total kernel". The same reflex works whenever a constraint on a group's normal subgroups must be made to say something about maps out of the group: a hypothesis about normal subgroups becomes a hypothesis about kernels becomes a conclusion about homomorphisms. The trigger is the co-occurrence of a homomorphism and any statement restricting normal subgroups — centre, derived subgroup, "no normal subgroup of index $n$", and so on.

**Simplicity is a dichotomy, and it stamps that dichotomy onto everything it touches.** A simple group has exactly two normal subgroups, the two extremes. This is the defining feature, and its consequences are always two-way splits. Any object that a simple group controls through one of its normal subgroups inherits a binary outcome. For homomorphisms out of $G$ the split is trivial-versus-injective, as proved here. For the action of a simple group on a set, the associated permutation representation is similarly either trivial or faithful. For a simple group sitting as a normal subgroup of a larger group, it is either central or its own conjugacy is fully active. The recognition pattern is: the moment "simple" appears in the hypotheses, expect the conclusion to be an "either ... or ..." with the two branches corresponding to the two extreme normal subgroups, and structure the proof as "produce the relevant normal subgroup, then let simplicity bisect it". You are not really proving a dichotomy; you are transporting the dichotomy that simplicity already is.

**An injective homomorphism is an embedding — so this result is a tool for placing simple groups inside other groups.** Reading the dichotomy from the side of its useful conclusion: if you have a homomorphism out of a simple group and can rule out the trivial case — usually by exhibiting a single element $g$ with $\varphi(g) \neq e_H$ — then $\varphi$ is automatically injective, and an injective homomorphism realises $G$ as a subgroup of $H$ (its image $\operatorname{im}\varphi \cong G$). This is the standard route for proving non-existence and embedding facts about simple groups: to show no non-trivial homomorphism $G \to H$ exists when $H$ is "too small", it suffices to show $G$ cannot embed in $H$ — for instance by a [[Thm - Lagrange's Theorem|Lagrange]] divisibility obstruction, $|G| \nmid |H|$. Conversely, any non-trivial action of a simple group on a small set embeds $G$ into a symmetric group $S_n$, which combined with order constraints is exactly how one proves results like "a simple group of order $60$ embeds in $A_5$". The first isomorphism theorem makes this precise: ruling out the trivial case forces $G/\ker\varphi = G/\{e\} \cong \operatorname{im}\varphi$, an honest copy of $G$ inside $H$.
