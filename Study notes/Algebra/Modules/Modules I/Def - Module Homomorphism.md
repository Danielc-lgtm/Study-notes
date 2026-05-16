---
type: definition
subject: module-theory
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Quotient Module"
  - "Def - Ring"
  - "Def - Ring Homomorphism"
  - "Def - Abelian Group"
  - "Def - Unit and Field"
tags: [algebra, module-theory]
---

# Notation

$R$ is a commutative ring with $1_R$, and $M, N$ are [[Def - Module|$R$-modules]]. A module homomorphism is written $f : M \to N$. Its **kernel** is $\ker f = \{m \in M : f(m) = 0_N\} \subseteq M$ and its **image** is $\operatorname{im} f = f(M) = \{f(m) : m \in M\} \subseteq N$. An isomorphism is denoted $f : M \xrightarrow{\sim} N$, and $M \cong N$ means there exists an isomorphism between them. On the left of the defining identity $f(rm) = rf(m)$ the action is that of $M$; on the right it is that of $N$. See [[Modules I — §3.1–3.2]] for the full notation registry.

This is a **compound page**: it defines four interlocking notions — module homomorphism, isomorphism, kernel, and image — because they are introduced together and none is fully usable without the others.

---

# Axiom Motivation

Once you have a class of objects — [[Def - Module|modules]] — you immediately need the right notion of *map between them*. The guiding principle, the same one that produces group homomorphisms and ring homomorphisms, is: **a structure-preserving map is a function that commutes with every operation the structure carries.** Get the list of operations right and the definition writes itself.

A module $M$ carries exactly two pieces of operational data: the abelian group structure $(M, +, 0_M)$ and the action $\cdot : R \times M \to M$. So a map $f : M \to N$ deserving the name "module homomorphism" must preserve both. Preserving the group structure means $f(m_1 + m_2) = f(m_1) + f(m_2)$ — that is, $f$ is a [[Def - Abelian Group|homomorphism of abelian groups]] (from which $f(0_M) = 0_N$ and $f(-m) = -f(m)$ follow automatically). Preserving the action means $f(r \cdot m) = r \cdot f(m)$ for every scalar $r$ and every $m$ — applying $f$ after scaling agrees with scaling after applying $f$. That is the whole definition: a module homomorphism is an additive map that also commutes with scalar multiplication.

Watch why neither half can be dropped. If $f$ commutes with the action but not with addition, it could send $m_1 + m_2$ anywhere, and the [[Thm - Isomorphism Theorems for Modules|isomorphism theorems]] — which all rest on $\ker f$ being a subgroup — collapse. If $f$ is additive but ignores the action, then $f$ is blind to the ring structure: it would treat $M$ as a mere abelian group, and a map between $F$-modules that is additive but not $F$-linear (for instance complex conjugation viewed on $\mathbb{C}$ as an $\mathbb{R}$-vector space *is* $\mathbb{R}$-linear, but as a $\mathbb{C}$-vector space it is *not* $\mathbb{C}$-linear, since $\overline{i \cdot 1} = -i \neq i = i\cdot\overline 1$) would wrongly count as a homomorphism. The condition $f(rm) = rf(m)$ is exactly what makes a homomorphism see the scalars.

Why also single out the **kernel** and the **image**, and why insist they are [[Def - Submodule|submodules]]? Because the entire payoff of having homomorphisms is the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]], $M/\ker f \cong \operatorname{im} f$, and that statement does not even *parse* unless $\ker f$ is a submodule of $M$ (so the [[Def - Quotient Module|quotient]] $M/\ker f$ exists) and $\operatorname{im} f$ is a submodule of $N$ (so it is a module to be isomorphic *to*). And they *are* submodules, forced by the two preservation properties: $\ker f$ is a subgroup because $f$ is additive, and it is action-closed because $f(rm) = rf(m) = r \cdot 0_N = 0_N$ whenever $f(m) = 0_N$; symmetrically $\operatorname{im} f$ is a subgroup because $f$ is additive, and action-closed because $r \cdot f(m) = f(rm) \in \operatorname{im} f$. So the definition of "module homomorphism" is precisely strong enough that kernel and image are automatically submodules — no extra hypothesis needed. This is the design target: the maps are defined so that the isomorphism theorems hold.

An **isomorphism** is then the natural notion of "the two modules are the same": a homomorphism that is a bijection. One should check — and it is true — that the set-theoretic inverse $f^{-1}$ of a bijective homomorphism is *automatically* a module homomorphism (if $f(m) = n$ and $f(m') = n'$ then $f^{-1}(n + n') = f^{-1}(f(m) + f(m')) = f^{-1}(f(m+m')) = m + m' = f^{-1}(n) + f^{-1}(n')$, and similarly for the action). This is why "bijective homomorphism" is the right definition of isomorphism and one need not separately demand that the inverse be structure-preserving — a pleasant feature shared with groups and rings, and *not* shared by, say, topological spaces.

---

# The Definition

Let $M$ and $N$ be [[Def - Module|$R$-modules]].

**Module homomorphism.** A function $f : M \to N$ is an **$R$-module homomorphism** (or **$R$-linear map**) if:

1. **Additivity.** $f$ is a homomorphism of abelian groups: $f(m_1 + m_2) = f(m_1) + f(m_2)$ for all $m_1, m_2 \in M$. (Consequently $f(0_M) = 0_N$ and $f(-m) = -f(m)$.)

2. **$R$-linearity.** $f(r \cdot m) = r \cdot f(m)$ for all $r \in R$ and all $m \in M$ — the action on the left is that of $M$, on the right that of $N$.

Equivalently, conditions (1) and (2) combine into the single requirement $f(r m_1 + m_2) = r f(m_1) + f(m_2)$ for all $r \in R$, $m_1, m_2 \in M$.

**Isomorphism.** An $R$-module homomorphism $f : M \to N$ is an **isomorphism** if it is bijective. The set-theoretic inverse $f^{-1} : N \to M$ is then automatically an $R$-module homomorphism. Two modules are **isomorphic**, written $M \cong N$, if there is an isomorphism between them; this is an equivalence relation. An isomorphism $M \to M$ is an **automorphism**.

**Kernel.** The **kernel** of $f$ is $\ker f = \{m \in M : f(m) = 0_N\}$. It is a [[Def - Submodule|submodule]] of $M$.

**Image.** The **image** of $f$ is $\operatorname{im} f = \{f(m) : m \in M\}$. It is a [[Def - Submodule|submodule]] of $N$.

The map $f$ is **injective if and only if $\ker f = \{0_M\}$**, and **surjective if and only if $\operatorname{im} f = N$**.

---

# Categorical Definition

These four notions assemble into the statement that **$R$-modules form a category**, written $R\text{-}\mathbf{Mod}$: the objects are $R$-modules, the morphisms are $R$-module homomorphisms, composition is composition of functions (a composite of module homomorphisms is again one, since each preservation property passes through a composite), and the identity map $\operatorname{id}_M$ is the identity morphism. An **isomorphism** in this category — a morphism with a two-sided inverse morphism — coincides exactly with the bijective-homomorphism notion above, precisely because the inverse of a bijective module homomorphism is automatically a module homomorphism.

The category $R\text{-}\mathbf{Mod}$ has more structure than the category of sets: the set $\operatorname{Hom}_R(M, N)$ of all homomorphisms $M \to N$ is itself an $R$-module under pointwise operations $(f + g)(m) = f(m) + g(m)$ and $(rf)(m) = r \cdot f(m)$ (here using commutativity of $R$ to keep $rf$ linear). A category enriched this way — with abelian-group-valued, indeed module-valued, hom-sets, with kernels, images, and quotients — is called an **abelian category**, and $R\text{-}\mathbf{Mod}$ is the motivating example. The kernel and image defined above are the categorical kernel and image: $\ker f$ is the universal submodule killed by $f$, and the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]] $M/\ker f \cong \operatorname{im} f$ is the statement that every morphism factors as a surjection followed by an injection.

---

# Relate to Other Fields / Compression

A module homomorphism is **a linear map with the field of scalars relaxed to a ring** — precisely the way a [[Def - Module|module]] is a vector space with that same relaxation. When $R = F$ is a [[Def - Unit and Field|field]], an $R$-module homomorphism between $F$-modules is *exactly* an $F$-linear map between vector spaces: conditions (1) and (2) are the two clauses of linearity. Kernel and image become the null space and range; injectivity-iff-trivial-kernel is the rank–nullity setup; and the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]] specialises to the rank–nullity theorem.

It is also the [[Def - Module|module]]-level instance of the universal pattern "homomorphism = operation-preserving map". A [[Def - Ring Homomorphism|ring homomorphism]] preserves $+$, $\cdot$, and $1$; a group homomorphism preserves the group operation; a module homomorphism preserves $+$ and the action. Each comes with a kernel that is the appropriate substructure (an [[Def - Ideal|ideal]] for rings, a normal subgroup for groups, a [[Def - Submodule|submodule]] for modules) and an isomorphism theorem of the form "domain modulo kernel is isomorphic to image". Module homomorphisms are the case where the kernel substructure is *unconditionally* quotientable, which is why their isomorphism theorems carry no side conditions.

When $R = \mathbb{Z}$, an $R$-module homomorphism is exactly a homomorphism of abelian groups: the $\mathbb{Z}$-linearity condition $f(nm) = nf(m)$ is *automatic* from additivity, since the $\mathbb{Z}$-action is repeated addition. So no information is added by the action in the $\mathbb{Z}$ case — consistent with "a $\mathbb{Z}$-module is just an abelian group".

---

# Examples / Corollaries

**Is an instance: the zero map and the identity.** For any modules $M, N$ the constant map $0 : M \to N$, $m \mapsto 0_N$, is a homomorphism (both conditions read $0_N = 0_N$), with $\ker 0 = M$ and $\operatorname{im} 0 = \{0_N\}$. The identity $\operatorname{id}_M : M \to M$ is an isomorphism with $\ker = \{0_M\}$, $\operatorname{im} = M$. These are the trivial calibration cases.

**Is an instance: the quotient map.** For a [[Def - Submodule|submodule]] $N \leq M$, the canonical projection $q : M \to M/N$, $q(m) = m + N$, is a surjective module homomorphism with $\ker q = N$ and $\operatorname{im} q = M/N$. Every submodule of $M$ is the kernel of *some* homomorphism out of $M$ — its own quotient map — so "submodule" and "kernel of a homomorphism" describe the same subsets, exactly as "ideal" coincides with "kernel of a ring homomorphism".

**Is an instance: scaling by a fixed ring element.** Fix $a \in R$. The map $\mu_a : M \to M$, $\mu_a(m) = a m$, is a module homomorphism: additivity is axiom (b) of the module, and $R$-linearity is $\mu_a(rm) = a(rm) = (ar)m = (ra)m = r(am) = r\,\mu_a(m)$, using *commutativity of $R$* in the step $ar = ra$. (This is one place commutativity of the scalar ring is genuinely used.) Its kernel is the $a$-torsion submodule $\{m : am = 0\}$, and $\mu_a$ is an isomorphism precisely when $a$ acts invertibly on $M$.

**Is an instance: an $F[X]$-module homomorphism is an operator-intertwining linear map.** Let $V, W$ be $F[X]$-modules — vector spaces with chosen operators $\alpha$ on $V$ and $\beta$ on $W$. An $F[X]$-module homomorphism $f : V \to W$ is an $F$-linear map that additionally satisfies $f(X \cdot v) = X \cdot f(v)$, i.e. $f(\alpha(v)) = \beta(f(v))$, i.e. $f \circ \alpha = \beta \circ f$. So $F[X]$-module homomorphisms are exactly the linear maps **intertwining** the two operators. An *isomorphism* of $F[X]$-modules is therefore an invertible linear map conjugating $\alpha$ to $\beta$ — which is why classifying $F[X]$-modules classifies operators up to similarity.

**Is NOT an instance: an additive map that is not $R$-linear.** Regard $\mathbb{C}$ as a module over $R = \mathbb{C}$ (a $1$-dimensional $\mathbb{C}$-vector space). Complex conjugation $c : \mathbb{C} \to \mathbb{C}$, $c(z) = \bar z$, is additive: $c(z + w) = c(z) + c(w)$. But it is **not** a $\mathbb{C}$-module homomorphism, because $\mathbb{C}$-linearity fails: $c(i \cdot 1) = \overline{i} = -i$, whereas $i \cdot c(1) = i \cdot 1 = i$, and $-i \neq i$. This non-example isolates condition (2): satisfying additivity alone is not enough; the map must also commute with the *scalar* action. (Viewed instead over $R = \mathbb{R}$, conjugation *is* an $\mathbb{R}$-module homomorphism — which scalar ring you use changes the answer.)

**Is NOT an instance: a non-additive map respecting the action.** On the $\mathbb{R}$-module $M = \mathbb{R}$, consider $f(x) = x + 1$. It does not respect addition — $f(x + y) = x + y + 1 \neq (x+1)+(y+1)$ — so it is not a module homomorphism, despite being a perfectly nice function. Indeed $f(0_M) = 1 \neq 0$, and a homomorphism must send $0_M$ to $0_N$. This isolates condition (1): affine maps that are not linear are excluded.

**Corollary (kernel and image are submodules).** For any module homomorphism $f : M \to N$, $\ker f \leq M$ and $\operatorname{im} f \leq N$. *Calibration check:* $\ker f$ is a subgroup since $f$ is additive, and is action-closed because $m \in \ker f \implies f(rm) = rf(m) = r\cdot 0_N = 0_N$. Likewise $\operatorname{im} f$ is a subgroup, and $r \cdot f(m) = f(rm) \in \operatorname{im} f$. If you can reproduce both you have understood that the two defining conditions exist exactly to make the [[Thm - Isomorphism Theorems for Modules|isomorphism theorems]] well-posed.

**Corollary (injectivity is detected by the kernel).** $f$ is injective if and only if $\ker f = \{0_M\}$. *Calibration check:* if $\ker f = \{0_M\}$ and $f(m) = f(m')$, then $f(m - m') = 0_N$ by additivity, so $m - m' \in \ker f = \{0_M\}$, giving $m = m'$; the converse is immediate since $f(0_M) = 0_N$. This is the module version of "a linear map is injective iff its null space is zero".

**Corollary (the inverse of an isomorphism is a homomorphism).** If $f : M \to N$ is a bijective module homomorphism, then $f^{-1} : N \to M$ is a module homomorphism, hence an isomorphism. *Calibration check:* additivity and $R$-linearity of $f^{-1}$ follow by applying $f^{-1}$ to the corresponding identities for $f$. This is why "isomorphism" can be defined simply as "bijective homomorphism", with no separate clause about the inverse.

**Corollary (first isomorphism theorem).** Every module homomorphism $f : M \to N$ induces an isomorphism $M/\ker f \xrightarrow{\sim} \operatorname{im} f$, $\;m + \ker f \mapsto f(m)$. *Calibration check:* the map is well-defined and injective because its "kernel" is exactly $\ker f$ collapsed to zero, and surjective onto $\operatorname{im} f$ by definition. This is the central reason the four notions on this page are bundled together — see [[Thm - Isomorphism Theorems for Modules]].

---

# Unlocked by This

> [!tip] Isomorphism theorems for modules *(from this chapter)*
> Homomorphisms, kernels, images and quotients are exactly the ingredients of the [[Thm - Isomorphism Theorems for Modules|three isomorphism theorems]]: $M/\ker f \cong \operatorname{im} f$, the diamond isomorphism $(A+B)/A \cong B/(A\cap B)$, and the tower isomorphism $(M/N)/(L/N) \cong M/L$.

> [!tip] Annihilators and cyclic modules *(from this chapter)*
> For $m \in M$, the homomorphism $R \to M$, $r \mapsto rm$, has kernel the [[Def - Annihilator|annihilator]] $\operatorname{Ann}(m)$ and image the cyclic submodule $Rm$, so the first isomorphism theorem gives $Rm \cong R/\operatorname{Ann}(m)$.

> [!tip] Free modules and presentations *(from Commutative Algebra)*
> Surjective homomorphisms from a [[Def - Free Module|free module]] $R^k$ onto $M$ are the device that expresses $M$ as a quotient $R^k/\ker$; this presentation, and the [[Thm - Finitely Generated Modules and Surjections from a Free Module|equivalence with finite generation]], is the gateway to the structure theorem for finitely generated modules over a principal ideal domain.
