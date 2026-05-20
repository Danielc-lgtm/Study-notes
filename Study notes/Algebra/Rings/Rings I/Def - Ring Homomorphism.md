---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Subring"
  - "Def - Ideal"
  - "Def - Polynomial Ring"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ and $S$ are [[Def - Ring|rings]]; $R$ has additive identity $0_R$ and multiplicative identity $1_R$, and likewise $0_S, 1_S$ for $S$. A ring homomorphism is written $\varphi : R \to S$. Its **kernel** is $\ker\varphi = \{r \in R : \varphi(r) = 0_S\}$, a subset of the domain; its **image** is $\operatorname{im}\varphi = \{\varphi(r) : r \in R\}$, a subset of the codomain. We write $R \cong S$ when there is a ring isomorphism between them. The full symbol registry is on [[Rings I — §2.1–2.2]].

---

# Axiom Motivation

A ring carries *two* operations woven together by distributivity: an addition making it an [[Def - Abelian Group|abelian group]], and a multiplication making it a monoid. A homomorphism is a map that respects structure — so the only question is which structure, and the answer must be: *all of it*. A ring homomorphism is forced to be simultaneously a homomorphism of the additive group and a homomorphism of the multiplicative monoid. There is no freedom here; if a map ignored either operation it would not deserve the name, because the whole purpose of a homomorphism is to let us transport ring-theoretic facts from $R$ to $S$, and a ring-theoretic fact can involve either operation.

Spell this out. To respect addition the map must satisfy $\varphi(r_1 + r_2) = \varphi(r_1) + \varphi(r_2)$ — this is the abelian-group [[Def - Homomorphism|homomorphism]] condition — and a standard consequence of *that* one axiom is $\varphi(0_R) = 0_S$ (apply $\varphi$ to $0 + 0 = 0$ and cancel). To respect multiplication the map must satisfy $\varphi(r_1 r_2) = \varphi(r_1)\varphi(r_2)$. So far this is just "homomorphism of the additive group and of the multiplicative semigroup".

Now the subtle axiom: we *also* demand $\varphi(1_R) = 1_S$, and — unlike $\varphi(0_R) = 0_S$ — this does **not** follow from the others. This is the one place a reader could invent the wrong definition, so it is worth seeing why the extra axiom is needed. The multiplicative structure of a ring is a *monoid*, not a group: there is an identity $1$ but no inverses, so we cannot cancel. From $\varphi(1_R)\varphi(1_R) = \varphi(1_R \cdot 1_R) = \varphi(1_R)$ we learn that $\varphi(1_R)$ is *idempotent* in $S$, but an idempotent need not be the identity. Concretely: the map $\varphi : \mathbb{Z} \to \mathbb{Z} \times \mathbb{Z}$, $n \mapsto (n, 0)$ preserves addition and multiplication perfectly, yet $\varphi(1) = (1, 0) \neq (1,1) = 1_{\mathbb{Z}\times\mathbb{Z}}$. Such a map sends the whole of $\mathbb{Z}$ into the subset $\mathbb{Z} \times \{0\}$, which is a ring in its own right but with a *different* identity — it is not a [[Def - Subring|subring]] of $\mathbb{Z} \times \mathbb{Z}$. If we allowed maps like this to count as ring homomorphisms, the image would not be a subring, the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]] would fail, and $1$ — the most important element of any ring — would not be transported. So the axiom $\varphi(1_R) = 1_S$ is exactly the condition that pins the identity, and it is what separates ring homomorphisms from "merely additive-and-multiplicative" maps.

What about the kernel and the image — why define *those*? Because they are the two diagnostic invariants of a homomorphism, measuring its failure to be injective and its failure to be surjective respectively. The kernel collects everything crushed to $0_S$; the image collects everything actually reached. The reason these specific sets matter is that each turns out to be a structured object — the kernel an [[Def - Ideal|ideal]] of the source, the image a [[Def - Subring|subring]] of the target — and together they reconstruct the homomorphism via $R/\ker\varphi \cong \operatorname{im}\varphi$. Note the asymmetry, and that it is forced by the axioms: the image is a subring (it contains $\varphi(1_R) = 1_S$ and is closed under both operations) but the kernel is *not* a subring (if $1_R$ were in the kernel then $\varphi(1_R) = 0_S$, collapsing $S$ to the zero ring) — the kernel is an ideal instead. This is the ring-theoretic echo of the group fact that the kernel of a [[Def - Homomorphism|group homomorphism]] is a [[Def - Normal Subgroup|normal subgroup]], not just any subgroup.

---

# The Definition

Let $R$ and $S$ be [[Def - Ring|rings]].

**Ring homomorphism.** A function $\varphi : R \to S$ is a **ring homomorphism** if it preserves both operations and both identities:

1. $\varphi(r_1 + r_2) = \varphi(r_1) + \varphi(r_2)$ for all $r_1, r_2 \in R$;
2. $\varphi(0_R) = 0_S$;
3. $\varphi(r_1 \cdot r_2) = \varphi(r_1) \cdot \varphi(r_2)$ for all $r_1, r_2 \in R$;
4. $\varphi(1_R) = 1_S$.

(Axiom 2 is in fact a consequence of axiom 1, since $\varphi$ is then a homomorphism of additive groups; it is listed for emphasis. Axiom 4 is genuinely independent and must be imposed separately.)

**Ring isomorphism.** A ring homomorphism $\varphi : R \to S$ that is also a bijection is a **ring isomorphism**. In that case the set-theoretic inverse $\varphi^{-1} : S \to R$ is *automatically* a ring homomorphism — one need not check it. (Proof sketch: for $s_1, s_2 \in S$ write $s_i = \varphi(r_i)$; then $\varphi(r_1 + r_2) = s_1 + s_2$, so applying $\varphi^{-1}$ gives $\varphi^{-1}(s_1 + s_2) = r_1 + r_2 = \varphi^{-1}(s_1) + \varphi^{-1}(s_2)$, and identically for multiplication; and $\varphi^{-1}(1_S) = 1_R$ since $\varphi(1_R) = 1_S$.) When such a map exists we write $R \cong S$ and say $R$ and $S$ are **isomorphic** — indistinguishable as rings.

**Kernel.** The **kernel** of a ring homomorphism $\varphi : R \to S$ is
$$\ker\varphi := \{r \in R : \varphi(r) = 0_S\} \subseteq R.$$

**Image.** The **image** of $\varphi$ is
$$\operatorname{im}\varphi := \{s \in S : s = \varphi(r) \text{ for some } r \in R\} \subseteq S.$$

Two basic facts tie these together:

- $\ker\varphi$ is an [[Def - Ideal|ideal]] of $R$, and $\operatorname{im}\varphi$ is a [[Def - Subring|subring]] of $S$.
- $\varphi$ is **injective if and only if** $\ker\varphi = \{0_R\}$.

---

# Categorical Definition

A ring homomorphism is precisely an **arrow in the category $\mathbf{Ring}$**. The vocabulary needed is minimal. A *category* $\mathcal{C}$ consists of a class of objects and, for any two objects $A$ and $B$, a set $\operatorname{Hom}_{\mathcal{C}}(A, B)$ of *arrows* from $A$ to $B$, together with an associative composition $\circ$ and identity arrows $\mathrm{id}_A$ acting as units for composition. The category $\mathbf{Ring}$ takes (commutative unital) [[Def - Ring|rings]] as objects and ring homomorphisms as arrows; composition is ordinary function composition (the composite of two ring homomorphisms is a ring homomorphism, since each axiom is checked pointwise), and $\mathrm{id}_R$ is the identity function on $R$. The four-axiom definition above is exactly the data required for a function $R \to S$ to qualify as an arrow.

The categorical viewpoint reveals two structural facts that are otherwise scattered. First, $\mathbb{Z}$ is the **initial object** of $\mathbf{Ring}$: from $\mathbb{Z}$ to any ring $R$ there is exactly one arrow, forced because $\varphi(1_{\mathbb{Z}}) = 1_R$ by axiom 4 and the rest of $\varphi$ is then determined by additivity ($n \mapsto n \cdot 1_R$). "Initial object" is the categorical name for "an object admitting exactly one arrow into every other object", and it is the precise statement of the slogan "$\mathbb{Z}$ is the universal ring". The kernel of this unique arrow is the [[Def - Characteristic of a Ring|characteristic ideal]] of $R$, encoding how $\mathbb{Z}$ sits inside $R$. Second, $\mathbf{Ring}$ has **products** — given two rings $R$ and $S$, the componentwise product ring $R \times S$ together with the projection homomorphisms $\pi_R : R \times S \to R$ and $\pi_S : R \times S \to S$ satisfies the universal property that any pair of homomorphisms into $R$ and into $S$ factors uniquely through $R \times S$. It also has certain **colimits**: the coproduct of two commutative rings $R$ and $S$ is the tensor product $R \otimes_{\mathbb{Z}} S$, and quotients $R \to R/I$ are coequalizers. The [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem]] — that every ring homomorphism factors as a surjection followed by an injection — is the statement that $\mathbf{Ring}$ has the *epi-mono factorisation* characteristic of abelian-flavoured algebraic categories.

A subtle point worth highlighting: the fact that a *bijective* ring homomorphism is automatically a ring **isomorphism** in the categorical sense (i.e. has a two-sided inverse arrow) is special to algebraic categories like $\mathbf{Ring}$, $\mathbf{Grp}$, and $\mathbf{Mod}_R$. It fails in $\mathbf{Top}$, where a continuous bijection need not have a continuous inverse — the categorical distinction between "bijection" and "isomorphism" only collapses when the structure being preserved is purely algebraic.

---

# Relate to Other Fields / Compression

A ring homomorphism is precisely a [[Def - Homomorphism|group homomorphism]] of the underlying additive groups that *additionally* respects the multiplicative monoid structure — identity included. So the definition is the group notion with one extra layer bolted on, and the bolt-on is the pair of axioms (3) and (4). This layered structure is why every theorem about ring homomorphisms is proved by "first invoke the group result for the additive part, then check multiplication separately": the kernel is an [[Def - Ideal|ideal]] because it is *already* an additive subgroup by the group theory, plus strong closure from axiom 3; the [[Thm - First Isomorphism Theorem for Rings|first isomorphism theorem for rings]] is proved by taking the group isomorphism for free and checking only that the map respects multiplication. The ring theory is genuinely a refinement of the group theory, not a parallel reinvention of it.

The asymmetry between kernel and image — kernel is an ideal, image is a subring — is itself the shadow of a general principle. In any algebraic category, the kernel of a morphism is the substructure you may quotient by (a [[Def - Normal Subgroup|normal subgroup]] for groups, an ideal for rings, a submodule for modules), while the image is a genuine subobject of the same kind as the target. The reason "image is a subring but kernel is not" has no analogue in group theory is purely that rings have a distinguished element $1$ that a subobject must contain but a quotientable-substructure must avoid.

There is a category-theoretic compression worth stating. Rings with ring homomorphisms form a category, and the [[Def - Characteristic of a Ring|characteristic]] story shows $\mathbb{Z}$ is its *initial object*: from $\mathbb{Z}$ to any ring $R$ there is exactly one homomorphism (it must send $1 \mapsto 1_R$, and that determines it everywhere by additivity). An isomorphism is then exactly an isomorphism in this category — a morphism with a two-sided inverse — and the fact that the inverse of a bijective ring homomorphism is automatically a homomorphism is the statement that "bijective morphism" and "isomorphism" coincide for rings, which is special and not true in every category (it fails, for instance, for continuous maps of topological spaces).

---

# Examples / Corollaries

**Is an instance — the quotient map $R \to R/I$.** For any [[Def - Ideal|ideal]] $I \trianglelefteq R$, the map $\pi : R \to R/I$ sending $r \mapsto r + I$ is a ring homomorphism: it respects addition and multiplication because the operations on the [[Def - Quotient Ring|quotient ring]] are *defined* by acting on representatives, and $\pi(1_R) = 1_R + I = 1_{R/I}$. Its kernel is exactly $I$ (since $r + I = 0 + I$ means $r \in I$) and it is surjective, so $\operatorname{im}\pi = R/I$. This is the universal example: every ideal arises as a kernel, namely the kernel of its own quotient map.

**Is an instance — evaluation $R[X] \to R$.** Fix $c \in R$. The evaluation map $\operatorname{ev}_c : R[X] \to R$, sending a polynomial $f$ to its value $f(c)$, is a ring homomorphism — substituting a fixed element respects sums and products of polynomials, and the constant polynomial $1$ evaluates to $1_R$. Taking $c = 0$, the kernel of $\operatorname{ev}_0 : R[X] \to R$ is the set of polynomials with zero constant term, which is the [[Def - Ideal|ideal]] $(X)$; the map is surjective onto $R$ (constants hit everything), so this exhibits $(X)$ concretely as a kernel.

**Is an instance — the reduction map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$.** The map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $m \mapsto m + n\mathbb{Z}$, is a ring homomorphism — it is the quotient map for the ideal $n\mathbb{Z}$. Its kernel is $n\mathbb{Z}$, its image is all of $\mathbb{Z}/n\mathbb{Z}$. This map is the engine behind modular arithmetic, and (as the next page records) it is the unique homomorphism from $\mathbb{Z}$ to $\mathbb{Z}/n\mathbb{Z}$.

**Is NOT an instance — $n \mapsto (n, 0)$ from $\mathbb{Z}$ to $\mathbb{Z} \times \mathbb{Z}$.** The map $\varphi : \mathbb{Z} \to \mathbb{Z} \times \mathbb{Z}$, $n \mapsto (n, 0)$, satisfies axioms 1, 2 and 3 — it preserves addition and multiplication — but fails axiom 4, since $\varphi(1) = (1,0)$ while $1_{\mathbb{Z}\times\mathbb{Z}} = (1,1)$. It is therefore *not* a ring homomorphism. This non-example probes the independence of axiom 4: respecting $+$, $\cdot$ and $0$ is not enough; the identity must be imposed by hand.

**Is NOT an instance — complex conjugation composed with forgetting, or any non-multiplicative additive map.** The map $\mathbb{Z} \to \mathbb{Z}$, $n \mapsto 2n$, preserves addition (it is a group homomorphism of $(\mathbb{Z},+)$) but is not a ring homomorphism: $\varphi(1 \cdot 1) = 2$ whereas $\varphi(1)\varphi(1) = 4$, so axiom 3 fails, and indeed $\varphi(1) = 2 \neq 1$ so axiom 4 fails too. This probes the independence of the multiplicative axioms from the additive one — a group homomorphism of the additive structure is a genuinely weaker thing.

**Corollary — $\ker\varphi$ is an ideal of $R$.** The kernel is an additive subgroup (group theory: it is the kernel of $\varphi$ as a [[Def - Homomorphism|map of additive groups]]). For strong closure, take $a \in \ker\varphi$ and $b \in R$; then $\varphi(ab) = \varphi(a)\varphi(b) = 0_S \cdot \varphi(b) = 0_S$, so $ab \in \ker\varphi$. Both [[Def - Ideal|ideal]] axioms hold. Note the kernel cannot be a subring unless $S$ is the zero ring, since $1_R \in \ker\varphi$ would give $1_S = \varphi(1_R) = 0_S$.

**Corollary — $\operatorname{im}\varphi$ is a subring of $S$.** The image contains $\varphi(1_R) = 1_S$, and it is closed under addition and multiplication because $\varphi(r_1) + \varphi(r_2) = \varphi(r_1 + r_2)$ and $\varphi(r_1)\varphi(r_2) = \varphi(r_1 r_2)$ are again values of $\varphi$. So $\operatorname{im}\varphi$ satisfies the [[Def - Subring|subring]] axioms. Contrast with the kernel: the image *does* contain the identity, which is exactly why image and kernel are objects of different types.

**Calibration check.** Verify that $\varphi$ is injective if and only if $\ker\varphi = \{0_R\}$ — the forward direction is immediate, and the reverse is the group-theoretic fact applied to the additive groups, since $\varphi(r_1) = \varphi(r_2)$ rearranges to $\varphi(r_1 - r_2) = 0_S$. Check also that the composite of two ring homomorphisms is a ring homomorphism, and that a ring isomorphism transports every ring-theoretic property — being a [[Def - Unit and Field|field]], being commutative, the [[Def - Characteristic of a Ring|characteristic]] — from one ring to the other. If you can explain why $\varphi(0_R) = 0_S$ is free but $\varphi(1_R) = 1_S$ is not, you have understood the definition.

---

# Unlocked by This

> [!tip] The First Isomorphism Theorem for Rings *(from this topic)*
> Because $\ker\varphi$ is an ideal and $\operatorname{im}\varphi$ a subring, every ring homomorphism factors as $R/\ker\varphi \cong \operatorname{im}\varphi$. See [[Thm - First Isomorphism Theorem for Rings]] — this is the workhorse for identifying quotient rings without tedious coset bookkeeping.

> [!tip] Characteristic of a Ring *(from this topic)*
> There is exactly one ring homomorphism $\iota : \mathbb{Z} \to R$ for any ring $R$, forced by $\iota(1) = 1_R$. Its kernel measures how $\mathbb{Z}$ sits inside $R$ and defines the [[Def - Characteristic of a Ring|characteristic]].

> [!tip] Quotient Ring *(from this topic)*
> The quotient map $R \to R/I$ is the canonical surjective ring homomorphism, and exhibits every [[Def - Ideal|ideal]] as a kernel. See [[Def - Quotient Ring]].
