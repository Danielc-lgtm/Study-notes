---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Symmetric Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
tags: [algebra, group-theory]
---

# Notation

An **action** of a group $(G, \cdot, e)$ on a set $X$ is written as a map $G \times X \to X$, $(g, x) \mapsto g \cdot x$ (or $g * x$ when the group operation also uses $\cdot$ and confusion threatens). The associated [[Def - Homomorphism|homomorphism]] $G \to \operatorname{Sym}(X)$ — sending each $g$ to the permutation $x \mapsto g \cdot x$ — is the **permutation representation** of the action, written $\rho$ or $\varphi$. Following the source lecture notes, for an action with permutation representation $\varphi$ we write

$$G^X = \operatorname{im}(\varphi) \quad\text{and}\quad G_X = \ker(\varphi),$$

so $G^X$ is the permutation group through which $G$ actually acts, and $G_X$ is the set of elements acting invisibly. The set $X$ equipped with an action of $G$ is called a **$G$-set**. See [[Group Theory II — §1.3–1.4]] for the full notation registry.

---

# Axiom Motivation

The slogan to be turned into mathematics is "**$G$ is a [[Def - Group|group]] of symmetries of $X$**". Concretely: the integers translate the number line, the rotation [[Def - Group|group]] spins a sphere, $S_n$ rearranges $n$ objects, the symmetries of a cube move its faces around. In each case every group element does *something* to the set $X$, and the doing is compatible with the group's multiplication. We want a definition that records exactly this and nothing more — exactly "$G$ does things to $X$, in a way that respects how $G$ multiplies".

Here is the most direct route to inventing the definition. A symmetry of $X$ — a reversible rearrangement of it — is, as established in [[Def - Symmetric Group]], a bijection $X \to X$, an element of $\operatorname{Sym}(X)$. To say "$G$ is a group of symmetries of $X$" is to say each $g \in G$ *is* such a bijection, or at least *names* one, in a manner compatible with multiplication: the bijection named by a product $g_1 g_2$ should be the composite of the bijections named by $g_1$ and $g_2$, and the bijection named by $e$ should be the identity. But a structure-respecting map from $G$ to the group $\operatorname{Sym}(X)$ is exactly a [[Def - Homomorphism|homomorphism]] $\rho : G \to \operatorname{Sym}(X)$. So the slogan, taken at face value, *is* the data of a homomorphism into a symmetric group, and that is the cleanest possible definition. (This is the content of [[Thm - Actions Correspond to Homomorphisms]], and it is the "true name" of the concept.)

Why, then, not simply *define* an action to be such a homomorphism, and why instead write the definition as a map $G \times X \to X$ with two axioms? Because the map-with-axioms form is what you actually *verify* in examples, and it is the form in which actions naturally arise. When you say "$G$ acts on $X$" you usually have in hand a rule that takes a group element $g$ and a point $x$ and returns a point — translate $x$ by $g$, rotate $x$ by $g$, conjugate $x$ by $g$. That rule is a function $G \times X \to X$. The two definitions are equivalent (this is the whole point of [[Thm - Actions Correspond to Homomorphisms]]), and the map-with-axioms version is the *operational* one: it is how you check that something is an action, and it is the version the [[#The Definition]] below adopts.

Now derive the two axioms from the desideratum, and watch each one be forced. We want the rule $(g,x) \mapsto g \cdot x$ to mean "$g$ does its thing to $x$" compatibly with multiplication.

First, **the identity must do nothing**: $e \cdot x = x$. The element $e$ is the "no-move" of the group, so the symmetry it names must be the no-move of $X$, the identity bijection. What goes wrong without this axiom? Drop it and the map $g \mapsto (x \mapsto g \cdot x)$ need no longer land in $\operatorname{Sym}(X)$ at all. Here is the failure concretely: suppose $G = \{e, g\}$ is the two-element group and define $h \cdot x = x_0$ for *every* $h$ and every $x$, where $x_0$ is one fixed point. This satisfies the compatibility axiom below — both sides collapse to $x_0$ — but $e$ acts as the constant map $x \mapsto x_0$, which is not a bijection (for $|X| > 1$) and has no inverse. The identity axiom is exactly what guarantees each $g$ acts *invertibly*: with $e \cdot x = x$, the maps $x \mapsto g \cdot x$ and $x \mapsto g^{-1} \cdot x$ become mutually inverse, so each is a genuine permutation. Without it, "$G$ acts by symmetries" fails because the elements need not act by symmetries.

Second, **composition must be respected**: $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$. Doing $g_2$ and then $g_1$ should be the same as doing the single move $g_1 g_2$. This is the heart of the word "compatible": it is what makes the assignment $g \mapsto (\text{symmetry of } X)$ a [[Def - Homomorphism|homomorphism]] rather than an unstructured labelling. Drop this axiom and you have merely "every element of $G$ is some permutation of $X$", with no relation between the permutation of $g_1 g_2$ and those of $g_1, g_2$ — the group structure of $G$ has been thrown away and only the underlying set of $G$ survives. Concretely, with this axiom gone you could let $g$ act as a $90^\circ$ rotation and $g^2$ act as a reflection, even though $g^2$ is forced by the group; the action would not know that $g^2$ *is* $g$ done twice. The compatibility axiom is what makes an action transport the *algebra* of $G$, not just its elements.

Note carefully which direction the compatibility axiom is written. We demand $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$ — apply $g_2$ *first*, then $g_1$ — matching the reading of function composition. This is a *left* action. If instead one wants $g_1$ applied first, one writes a *right* action $(x \cdot g_1) \cdot g_2 = x \cdot (g_1 g_2)$; the two are interchangeable by replacing $g$ with $g^{-1}$, and we fix the left convention throughout. Choosing neither convention, or mixing them, breaks the homomorphism property — a "mixed" rule would give an *anti*-homomorphism, $g_1 g_2 \mapsto \rho(g_2)\rho(g_1)$.

Could one *strengthen* the definition? One might demand the action be **faithful** (only $e$ acts invisibly) or **transitive** (a single orbit). Both are genuine and useful extra hypotheses — defined below — but folding them into the definition of "action" would be a mistake, because the most important actions fail them. The conjugation action of a group on itself (the engine of [[Group Theory II — §1.3–1.4|§1.4]]) is rarely faithful — its kernel is the [[Def - Centraliser and Centre|centre]] — and the action on a set with several orbit types is not transitive. The bare definition is deliberately permissive so that *every* natural construction counts as an action; faithfulness and transitivity are then layered on as named special cases when needed.

---

# The Definition

An **action** of a group $(G, \cdot, e)$ on a set $X$ is a function

$$- \cdot - \ : \ G \times X \longrightarrow X, \qquad (g, x) \longmapsto g \cdot x,$$

satisfying the two axioms:

1. **Identity.** For all $x \in X$, $\quad e \cdot x = x$.
2. **Compatibility.** For all $g_1, g_2 \in G$ and all $x \in X$, $\quad g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$.

A set $X$ equipped with such an action is a **$G$-set**, and one says **$G$ acts on $X$**.

**Permutation representation.** Given an action, define for each $g \in G$ the function $\rho(g) : X \to X$ by $\rho(g)(x) = g \cdot x$. The two axioms make each $\rho(g)$ a bijection — its inverse is $\rho(g^{-1})$, since $\rho(g^{-1})(\rho(g)(x)) = g^{-1}\cdot(g\cdot x) = (g^{-1}g)\cdot x = e\cdot x = x$ — and make the assignment

$$\rho : G \longrightarrow \operatorname{Sym}(X)$$

a [[Def - Homomorphism|homomorphism]], because $\rho(g_1)\circ\rho(g_2)$ and $\rho(g_1 g_2)$ agree on every point by axiom (2). This homomorphism $\rho$ is the **permutation representation** of the action. Conversely every homomorphism $G \to \operatorname{Sym}(X)$ arises this way from a unique action, by setting $g \cdot x := \rho(g)(x)$; see [[Thm - Actions Correspond to Homomorphisms]].

**Image and kernel.** Following the source notes, write

$$G^X = \operatorname{im}(\rho) \ \leq\ \operatorname{Sym}(X), \qquad G_X = \ker(\rho) \ \trianglelefteq\ G.$$

The image $G^X$ is the [[Def - Permutation Group|permutation group]] through which $G$ genuinely acts; the kernel $G_X$ is the [[Def - Normal Subgroup|normal subgroup]] of elements that act invisibly (acting as $\operatorname{id}_X$). The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives $G/G_X \cong G^X$.

**Faithful and transitive actions.** The action is:
- **faithful** if $G_X = \{e\}$, i.e. only the identity acts as the identity permutation — equivalently $\rho$ is injective, so $G$ embeds in $\operatorname{Sym}(X)$ as the permutation group $G^X \cong G$;
- **transitive** if for every $x, y \in X$ there is some $g \in G$ with $g \cdot x = y$ — equivalently the action has a single [[Def - Orbit and Stabiliser|orbit]].

---

# Categorical Definition

A group action has a categorical description so clean that it is arguably the *right* definition, and it requires only a little vocabulary to state self-containedly.

**The vocabulary.** A *category* $\mathcal{C}$ consists of objects, arrows (or morphisms) between objects, an associative composition of arrows, and an identity arrow on each object. The category $\mathbf{Set}$ has sets as objects and functions as arrows. A *functor* $F : \mathcal{C} \to \mathcal{D}$ is a structure-preserving map between categories: it sends each object of $\mathcal{C}$ to an object of $\mathcal{D}$ and each arrow to an arrow, preserving composition ($F(f \circ g) = F(f) \circ F(g)$) and identities. Finally — the key fact — **a group $G$ is the same thing as a category with exactly one object in which every arrow is invertible**, a *one-object groupoid*: take a single object $\star$, let the arrows $\star \to \star$ be the elements of $G$, let arrow composition be group multiplication, the identity arrow be $e$, and invertibility of arrows be the existence of inverses. (This is the categorical definition of a group; see [[Def - Group#Categorical Definition]].) Write $\mathbf{B}G$ for this one-object groupoid.

**The definition.** A **left action of $G$ on a set** is precisely **a functor $\mathbf{B}G \to \mathbf{Set}$**.

Unwind it and the concrete definition reappears exactly. A functor $F : \mathbf{B}G \to \mathbf{Set}$ must send the single object $\star$ somewhere — to a set, call it $X$. It must send each arrow, i.e. each group element $g$, to an arrow of $\mathbf{Set}$ from $F(\star)$ to $F(\star)$, i.e. to a function $X \to X$ — call it $\rho(g)$. Functoriality demands $F$ preserve identities, so $\rho(e) = \operatorname{id}_X$ — this is the **identity axiom**. Functoriality demands $F$ preserve composition, so $\rho(g_1 g_2) = \rho(g_1) \circ \rho(g_2)$ — this is the **compatibility axiom**. And because every arrow of $\mathbf{B}G$ is invertible and functors preserve inverses, each $\rho(g)$ is a bijection automatically. A functor $\mathbf{B}G \to \mathbf{Set}$ is therefore exactly a set $X$ together with a homomorphism $G \to \operatorname{Sym}(X)$ — exactly an action. The two axioms of the concrete definition are not two separate stipulations at all; they are the *single* word "functor".

This viewpoint pays off immediately. A *$G$-equivariant map* between two $G$-sets — a function commuting with the action — is, in this language, just a *natural transformation* between the two functors, so the category of $G$-sets is the functor category $[\mathbf{B}G, \mathbf{Set}]$. Replacing the target $\mathbf{Set}$ by another category yields other species of action by the same template: a functor $\mathbf{B}G \to \mathbf{Vect}$ is a [[Def - Homomorphism|linear representation]] of $G$, a functor $\mathbf{B}G \to \mathbf{Top}$ is an action on a topological space. The concrete map-with-axioms definition is one instance — the $\mathbf{Set}$ instance — of a uniform notion.

---

# Relate to Other Fields / Compression

A group action is **a [[Def - Homomorphism|homomorphism]] $G \to \operatorname{Sym}(X)$**, and that is the most compressing thing one can say about it: see [[Thm - Actions Correspond to Homomorphisms]]. Every concept attached to actions is then a concept about homomorphisms in disguise. A *faithful* action is an *injective* homomorphism. The *kernel* $G_X$ of the action is the kernel of the homomorphism. The orbit-counting and stabiliser machinery is the homomorphism's image-and-kernel structure made geometric. This is why the entire apparatus of [[Group Theory I — §1.1–1.2]] — kernels, images, the [[Thm - First Isomorphism Theorem|isomorphism theorems]] — descends onto actions without any new work.

A group action is the algebraic special case of a **dynamical system**. A dynamical system is a set (a "state space") together with a prescribed way for "time" to move the states; when time is the group $(\mathbb{R}, +)$ one has a flow, when time is $(\mathbb{Z}, +)$ one has the iterates of a single invertible map. A group action is exactly this with the time-group allowed to be *any* group: $X$ is the state space and $G$ is a generalised, possibly non-commutative, "time" that evolves it. The compatibility axiom $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$ is the law that "evolving by $g_2$ then by $g_1$ equals evolving by $g_1 g_2$", which for $G = \mathbb{R}$ is precisely the flow property $\Phi_s \circ \Phi_t = \Phi_{s+t}$. [[Def - Orbit and Stabiliser|Orbits]] of a group action are then literally the orbits of a dynamical system, and the symmetry groups of differential equations are group actions in exactly this sense.

In one more compression: a group action is the precise, mathematical content of the informal word **"symmetry"**. Whenever a structure has symmetry — a crystal, an equation, a geometric figure, a physical law — that symmetry *is* a group acting on the structure, and Noether's theorem, crystallographic classification, and Galois theory are all the study of specific such actions.

---

# Examples / Corollaries

**Is an instance: the left-regular action of $G$ on itself.** Any group $G$ acts on the set $X = G$ by $g \cdot x = gx$, left multiplication. The identity axiom is $e \cdot x = ex = x$; compatibility is $g_1 \cdot (g_2 \cdot x) = g_1(g_2 x) = (g_1 g_2)x = (g_1 g_2)\cdot x$, which is just associativity in $G$. This action is faithful — if $gx = x$ for all $x$ then $g = e$ — and transitive, and its permutation representation is the embedding of [[Thm - Cayley's Theorem|Cayley's theorem]].

**Is an instance: $S_n$ acting on $\{1, \dots, n\}$.** The [[Def - Symmetric Group|symmetric group]] acts on the set it permutes by $\sigma \cdot i = \sigma(i)$. Compatibility is the definition of composition. This action is faithful (a permutation fixing every point is the identity) and transitive. It is the prototype: the permutation representation $\rho : S_n \to \operatorname{Sym}(\{1,\dots,n\})$ is the identity map.

**Is an instance: conjugation, $G$ acting on $G$.** A group acts on its own underlying set by $g \cdot x = gxg^{-1}$. The identity axiom holds since $exe^{-1} = x$, and compatibility holds since $g_1(g_2 x g_2^{-1})g_1^{-1} = (g_1 g_2)x(g_1 g_2)^{-1}$. This action is the entire subject of [[Group Theory II — §1.3–1.4|§1.4]]: its [[Def - Orbit and Stabiliser|orbits]] are the [[Def - Conjugacy Class|conjugacy classes]] and its kernel $G_X$ is the [[Def - Centraliser and Centre|centre]] $Z(G)$. It is generally **not faithful** — precisely the example showing why faithfulness is not folded into the definition.

**Is an instance: $G$ acting on the [[Def - Coset|cosets]] $G/H$.** For $H \leq G$, the group acts on the set of left [[Def - Coset|cosets]] by $g \cdot (xH) = gxH$. This is the [[Thm - Coset Action and the Normal Core|coset action]]; it is transitive, and its kernel is the normal core of $H$. It shows actions need not be on $G$ itself or on a geometric object — any naturally occurring set will serve.

**Is an instance: the trivial action.** For any group $G$ and any set $X$, the rule $g \cdot x = x$ for all $g, x$ is an action — both axioms hold trivially. Its permutation representation is the constant homomorphism $g \mapsto \operatorname{id}_X$, so $G_X = G$ and $G^X = \{\operatorname{id}_X\}$. It is maximally *un*faithful. It is a legitimate action and the degenerate baseline against which non-triviality is measured.

**Is NOT an instance: the rule $g \cdot x = g^{-1} \cdot_{\text{reg}} x = g^{-1}x$ as a "left" action.** Define a candidate action of $G$ on itself by $g \cdot x = g^{-1}x$. The identity axiom holds: $e \cdot x = e^{-1}x = x$. But compatibility **fails**: $g_1 \cdot (g_2 \cdot x) = g_1^{-1}(g_2^{-1}x) = (g_2 g_1)^{-1}x$, whereas $(g_1 g_2)\cdot x = (g_1 g_2)^{-1}x$, and $(g_2 g_1)^{-1} \neq (g_1 g_2)^{-1}$ in a non-abelian group. The rule $g \mapsto (x \mapsto g^{-1}x)$ is an *anti*-homomorphism — it reverses the order of multiplication — so it defines a *right* action, not a left one. This non-example pins down that the *direction* in axiom (2) is load-bearing.

**Is NOT an instance: $\mathbb{Z}$ "acting" on $\mathbb{R}$ by $n \cdot x = x + 1$.** Define a candidate action of $(\mathbb{Z}, +)$ on $\mathbb{R}$ by $n \cdot x = x + 1$ for every $n$ — every group element shifts by exactly one. Compatibility fails immediately: $1 \cdot (1 \cdot x) = (x+1)+1 = x+2$, but $(1 + 1)\cdot x = 2 \cdot x = x + 1$. And the identity axiom fails too: $0 \cdot x = x + 1 \neq x$. The correct action, $n \cdot x = x + n$, *does* satisfy both. This non-example shows that "every element does something" is not enough — the something must track the group's arithmetic.

**Corollary (each group element acts invertibly).** In any action, the map $x \mapsto g \cdot x$ is a bijection of $X$ for every $g$, with inverse $x \mapsto g^{-1}\cdot x$. *Calibration check:* the proof uses *both* axioms — compatibility to compute $g^{-1}\cdot(g\cdot x) = (g^{-1}g)\cdot x = e \cdot x$, then the identity axiom to finish. If you see why both are needed, you have understood why a constant "action" is excluded.

**Corollary (kernel is normal; first isomorphism theorem).** The kernel $G_X = \ker\rho$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$, being the kernel of the homomorphism $\rho$, and $G/G_X \cong G^X \leq \operatorname{Sym}(X)$ by the [[Thm - First Isomorphism Theorem|first isomorphism theorem]]. In particular, *every kernel of an action is a normal [[Def - Subgroup|subgroup]]* — which is the manufacturing process for normal [[Def - Subgroup|subgroups]] in this topic.

**Corollary (faithful $\iff$ embedding).** An action is faithful exactly when its permutation representation $\rho$ is injective, exactly when $G \cong G^X$ is a [[Def - Permutation Group|permutation group]] inside $\operatorname{Sym}(X)$. *Calibration check:* a faithful action is the data that realises an abstract group concretely as permutations.

**Corollary (trivial action $\iff$ kernel is everything).** An action is trivial precisely when $G_X = G$, i.e. the permutation representation is the constant homomorphism. This is the opposite extreme to faithful, and the [[Def - Kernel and Image|kernel]] $G_X$ interpolates between the two: it measures *how far the action is from faithful*.

---

# Unlocked by This

> [!tip] Orbit-Stabiliser Theorem *(from Group Theory II, §1.3)*
> Once a group acts on a set, the [[Def - Orbit and Stabiliser|orbit]] of a point and its [[Def - Orbit and Stabiliser|stabiliser]] are defined, and the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] ties their sizes to $|G|$ — the master counting tool of finite group theory.

> [!tip] Linear Representation and Character *(from Representation Theory)*
> Replacing the set $X$ by a vector space $V$ — equivalently, replacing the functor target $\mathbf{Set}$ by $\mathbf{Vect}$ — turns an action into a [[Def - Homomorphism|homomorphism]] $G \to \mathrm{GL}(V)$, a linear representation. Characters, the functions constant on [[Def - Conjugacy Class|conjugacy classes]], become the central invariants.

> [!tip] Principal Bundles and Deck Transformations *(from Differential Geometry and Algebraic Topology)*
> A free action of a group on a space is the structure of a principal bundle, and the action of the fundamental group on the universal cover by deck transformations is a group action whose orbit space recovers the base — the geometric incarnation of the orbit-stabiliser correspondence.
