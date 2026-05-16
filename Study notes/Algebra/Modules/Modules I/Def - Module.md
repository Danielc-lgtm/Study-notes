---
type: definition
subject: module-theory
prereqs:
  - "Def - Ring"
  - "Def - Abelian Group"
  - "Def - Ideal"
  - "Def - Quotient Ring"
  - "Def - Unit and Field"
  - "Def - Polynomial Ring"
tags: [algebra, module-theory]
---

# Notation

Throughout, $R$ is a **commutative ring with $1_R$** — this is the standing convention of the rings course, and module theory inherits it. A module is written $(M, +, 0_M, \cdot)$: the underlying set $M$, the **module addition** $+ : M \times M \to M$, the **zero of the module** $0_M$, and the **action** (or **scalar multiplication**) $\cdot : R \times M \to M$. Elements of $R$ are written $r, s, r_1, r_2$ and called **scalars**; elements of $M$ are written $m, n, m_1, m_2$. There are *two* additions in play — $+_R$ inside the ring and $+_M$ inside the module — and *two* multiplications — $\cdot_R$ inside the ring and the action $\cdot$ of $R$ on $M$. They operate on different things, so context disambiguates them; the subscripts $+_R, +_M$ are written only when a formula genuinely mixes both. The action is usually written by juxtaposition, $rm$ for $r \cdot m$. See [[Modules I — §3.1–3.2]] for the full notation registry.

---

# Axiom Motivation

The cleanest way to invent this definition is to take the axioms of a vector space and **delete one word**. A vector space over a field $F$ is an abelian group $V$ of vectors together with a scalar multiplication $F \times V \to V$ obeying the familiar distributivity and associativity laws. Every one of those laws makes sense if you replace the word "field" by the word "ring": nowhere in the statement "$r(m_1 + m_2) = rm_1 + rm_2$" did we ever need the scalar $r$ to be invertible. A **module is exactly a vector space whose scalars are allowed to come from a ring instead of a field.** That single relaxation is the whole definition, and it is worth dwelling on why it is the relaxation worth making.

Start from the desiderata. We have a [[Def - Ring|ring]] $R$, and we have already learned (from group theory) the idea of a group *acting* on a set: a homomorphism that lets group elements move points around. We now want the analogous notion of a ring acting on something. A ring is richer than a group — it has both an addition and a multiplication — so the thing it acts on should be richer than a bare set: it should itself have an addition, so that the ring's addition has something to interact with. The minimal sensible carrier is therefore an [[Def - Abelian Group|abelian group]] $(M, +, 0_M)$, and "$R$ acts on $M$" should mean: each ring element $r$ gives a way of transforming $M$, and the transformations compose and add in a way that mirrors the ring structure. Writing the action as $\cdot : R \times M \to M$, the four axioms are precisely the demand that this mirroring be faithful.

Take them one at a time and watch each one fail if dropped. Axiom (a), $(r_1 + r_2)m = r_1 m + r_2 m$, says the action respects *addition in the ring*: adding scalars first, then acting, agrees with acting separately and adding the results in $M$. Without it the symbol $r_1 + r_2$ inside $R$ would have no predictable effect on $M$, and the ring's addition would be decoration that the action ignores. Axiom (b), $r(m_1 + m_2) = rm_1 + rm_2$, says the action respects *addition in the module*: equivalently, for each fixed $r$ the map $m \mapsto rm$ is a homomorphism of the abelian group $(M, +)$. Drop it and "scalar multiplication" need not even be additive in the vector slot — $r$ could send $m_1 + m_2$ anywhere — and linear algebra collapses, because linearity *is* this axiom. Axiom (c), $r_1(r_2 m) = (r_1 r_2)m$, says the action respects *multiplication in the ring*: acting by $r_2$ and then by $r_1$ is the same as acting once by the product $r_1 r_2$. This is what makes the action a genuine *representation* of the ring's multiplicative structure rather than two unrelated facts; without it you could not simplify $r_1(r_2 m)$ at all. Axiom (d), $1_R m = m$, says the multiplicative identity of the ring acts as the identity transformation. It looks like a triviality but it is load-bearing: drop it and the *zero map* $r \cdot m := 0_M$ for all $r, m$ would satisfy (a), (b), (c) and count as a module structure on every abelian group, which is useless. Axiom (d) is exactly the non-degeneracy condition that rules out that pathology and pins the action down — it forces, for instance, $2m = (1_R + 1_R)m = m + m$, so the ring's arithmetic genuinely controls $M$.

Now, why a ring and not just a field? Because dropping invertibility of scalars is not a loss of structure to be tolerated — it is the entire source of new phenomena. Over a field, every nonzero scalar can be divided out, and the theory is uniform and tame: every vector space has a basis and is classified by a single number, its dimension. The moment scalars are merely ring elements, "divide by $r$" is no longer available, and genuinely new behaviour appears that has no analogue for vector spaces. An element $m$ can be *killed* by a nonzero scalar — there can be $r \neq 0$ with $rm = 0_M$ (impossible in a vector space) — which is the phenomenon of **torsion**. A module need not have a basis at all. Submodules of a finitely generated module can fail to be finitely generated. None of this is a defect; it is the reason module theory exists as a subject distinct from linear algebra. The payoff is unification: with one definition, an [[Def - Abelian Group|abelian group]] becomes a $\mathbb{Z}$-module, a vector space becomes an $F$-module, an [[Def - Ideal|ideal]] of $R$ becomes an $R$-module, and a vector space carrying a chosen linear operator becomes an $F[X]$-module — and every theorem proved about modules speaks about all of these at once.

In summary: a module is the structure a ring acts on. The carrier must be an abelian group so the ring's *addition* has a partner; axioms (a) and (b) make the action respect both additions; axiom (c) makes it respect the ring's *multiplication*; axiom (d) is the non-degeneracy clause that forbids the trivial zero action. Keep the field and you have rediscovered vector spaces; allow a general ring and you have unlocked torsion, the failure of bases, and the common home of abelian groups, ideals, and operators.

---

# The Definition

Let $R$ be a commutative ring with $1_R$. An **$R$-module** is a quadruple $(M, +, 0_M, \cdot)$ where:

1. **Additive group.** $(M, +, 0_M)$ is an [[Def - Abelian Group|abelian group]].

2. **Action.** $\cdot : R \times M \to M$ is an operation satisfying, for all $r, r_1, r_2 \in R$ and all $m, m_1, m_2 \in M$:
   - **(a) Distributivity over ring addition:** $(r_1 + r_2) \cdot m = (r_1 \cdot m) + (r_2 \cdot m)$;
   - **(b) Distributivity over module addition:** $r \cdot (m_1 + m_2) = (r \cdot m_1) + (r \cdot m_2)$;
   - **(c) Associativity of the action:** $r_1 \cdot (r_2 \cdot m) = (r_1 \cdot r_2) \cdot m$;
   - **(d) Unitality:** $1_R \cdot m = m$.

When $R$ is understood, one says simply "module"; one says "$R$ acts on $M$" to mean that $M$ is an $R$-module. The action is normally written by juxtaposition, $rm := r \cdot m$. Closure of the action is not a separate axiom — it is already part of the statement that $\cdot$ is a function with codomain $M$.

Two immediate consequences, both proved exactly as for vector spaces from the four axioms: $0_R \cdot m = 0_M$ for every $m$ (apply axiom (a) to $0_R + 0_R = 0_R$ and cancel in the abelian group), and $r \cdot 0_M = 0_M$ for every $r$ (apply axiom (b) to $0_M + 0_M = 0_M$ and cancel). Consequently $(-1_R) \cdot m = -m$, the additive inverse of $m$ in $M$.

---

# Categorical Definition

There is a clean categorical packaging. For a fixed abelian group $(M, +, 0_M)$, write $\operatorname{End}(M)$ for the set of all group homomorphisms $M \to M$. This set is itself a ring — a generally **non-commutative** one — under pointwise addition $(f + g)(m) = f(m) + g(m)$ and composition $(f \cdot g)(m) = f(g(m))$ as multiplication, with the identity map as $1$. It is the **endomorphism ring** of the abelian group $M$.

Now an $R$-module structure on $M$ is *exactly the same data* as a **ring homomorphism** $\rho : R \to \operatorname{End}(M)$. Given a module structure, define $\rho(r)$ to be the map $m \mapsto rm$; axiom (b) says each $\rho(r)$ is a group homomorphism (so lands in $\operatorname{End}(M)$), axiom (a) says $\rho(r_1 + r_2) = \rho(r_1) + \rho(r_2)$, axiom (c) says $\rho(r_1 r_2) = \rho(r_1) \circ \rho(r_2)$, and axiom (d) says $\rho(1_R) = \operatorname{id}_M$. Those four statements are precisely the assertion that $\rho$ is a [[Def - Ring Homomorphism|ring homomorphism]]. Conversely any such $\rho$ defines an action by $rm := \rho(r)(m)$. (Because $R$ is commutative the image $\rho(R)$ is a commutative subring of the possibly non-commutative $\operatorname{End}(M)$, which is consistent.)

This is the precise sense in which "a module is a ring acting on an abelian group" parallels "a group action is a homomorphism $G \to \operatorname{Sym}(X)$". A $G$-action on a set $X$ is a homomorphism into the symmetry group of $X$; an $R$-module is a homomorphism into the endomorphism *ring* of an abelian group. The richer acting object (a ring, not a group) is reflected in a richer target (a ring, not a group), and in a richer carrier (an abelian group, not a bare set).

---

# Relate to Other Fields / Compression

A module is **a vector space with the field of scalars relaxed to a ring** — this is the single most compressive statement, and it cuts both ways. Every theorem of linear algebra is a candidate theorem about modules; the ones that survive (the [[Thm - Isomorphism Theorems for Modules|isomorphism theorems]]) used only additivity, and the ones that fail (existence of a basis, classification by dimension) secretly used division by scalars. Reading the failures tells you exactly where invertibility of scalars was being spent.

It is simultaneously **the linear-algebra companion of a group action**. A [[Def - Abelian Group|group]] acting on a set is captured by a homomorphism into a symmetry group; a ring acting on an abelian group is captured by a homomorphism into an endomorphism ring (see the Categorical Definition). The submodule generated by an element plays the role of an orbit, the [[Def - Annihilator|annihilator]] plays the role of a stabiliser, and the isomorphism $Rm \cong R/\operatorname{Ann}(m)$ is the module-theoretic orbit–stabiliser theorem.

It also unifies three structures that look unrelated until you see them as modules. An abelian group *is* a $\mathbb{Z}$-module — there is no extra data, the action is forced. An [[Def - Ideal|ideal]] $I \trianglelefteq R$ *is* an $R$-module, and so is the [[Def - Quotient Ring|quotient ring]] $R/I$. A vector space equipped with one chosen linear operator *is* an $F[X]$-module. So module theory is the common generalisation of "abelian group theory", "ideal theory", and "a single linear operator", and a single result about modules can be cashed out in all three settings at once.

---

# Examples / Corollaries

**Is an instance: a vector space, when $R = F$ is a field.** If the ring of scalars happens to be a [[Def - Unit and Field|field]] $F$, the four module axioms are *verbatim* the four axioms of a vector space over $F$. So "$F$-module" and "vector space over $F$" are not merely analogous — they are the **same definition**. Every vector space you have ever met is a module; module theory is what is left of the concept when you stop assuming you can divide by scalars. This example fixes the reference point: a module is tame and basis-friendly exactly when its ring of scalars is a field.

**Is an instance: $R^n$, the free module of rank $n$.** For any ring $R$ and any $n \geq 0$, the set $R^n = R \times \cdots \times R$ is an $R$-module under componentwise addition and the action $r \cdot (r_1, \ldots, r_n) = (rr_1, \ldots, rr_n)$ using the ring's own multiplication. The four axioms hold componentwise because they hold in $R$. This is the literal copy of the construction of the coordinate vector space $F^n$, now over an arbitrary ring; the special case $n = 1$ says $R$ is a module over itself, and $n = 0$ gives the zero module $\{0_M\}$.

**Is an instance: an ideal $I \trianglelefteq R$.** Any [[Def - Ideal|ideal]] $I$ of $R$ is an $R$-module. Its addition and zero are inherited from $R$, and the action is the ring multiplication restricted to $R \times I \to I$ — this lands back in $I$ precisely because the defining property of an ideal is absorption, $rI \subseteq I$. So the ideal axiom "$I$ absorbs multiplication by ring elements" is exactly the closure condition that makes $I$ a submodule of $R$. The notions of ideal and of $R$-submodule of $R$ coincide.

**Is an instance: the quotient ring $R/I$.** For an ideal $I \trianglelefteq R$, the [[Def - Quotient Ring|quotient ring]] $R/I$ is an $R$-module via $r \cdot (a + I) = (ra) + I$. This is well-defined because $I$ is an ideal: changing the representative $a$ by an element of $I$ changes $ra$ by an element of $rI \subseteq I$, so the coset is unchanged. Notice this $R$-module is *not* in general a copy of $R^k$ for any $k$ — for instance $\mathbb{Z}/n\mathbb{Z}$ as a $\mathbb{Z}$-module is finite, while $\mathbb{Z}^k$ is infinite for $k \geq 1$. It exhibits torsion: every element is killed by the nonzero scalar $n$.

**Is an instance: a $\mathbb{Z}$-module is exactly an abelian group.** Given any [[Def - Abelian Group|abelian group]] $A$, there is one and only one way to make it a $\mathbb{Z}$-module, and the structure is *forced* by the axioms. Axiom (d) demands $1 \cdot a = a$; then axiom (a) forces $2 \cdot a = (1+1) \cdot a = a + a$, and inductively $n \cdot a = a + \cdots + a$ ($n$ summands) for $n > 0$, while $(-n) \cdot a = (-a) + \cdots + (-a)$ and $0 \cdot a = 0_M$. There is no freedom: the action is repeated addition. Hence the categories of abelian groups and of $\mathbb{Z}$-modules are literally the same, and every theorem about modules is a theorem about abelian groups when specialised to $R = \mathbb{Z}$.

**Is an instance: an $F[X]$-module is a vector space with a chosen endomorphism.** Let $F$ be a field, $V$ a vector space over $F$, and $\alpha : V \to V$ an $F$-linear map. Then $V$ becomes a module over the [[Def - Polynomial Ring|polynomial ring]] $F[X]$ via $f \cdot v := f(\alpha)(v)$ — substitute the operator $\alpha$ into the polynomial $f$ and apply the resulting operator to $v$. The four axioms hold because polynomial substitution is a ring homomorphism $F[X] \to \operatorname{End}_F(V)$, with $X$ acting as $\alpha$. Crucially, the module structure remembers $\alpha$: a *different* choice of operator on the same $V$ gives a *different* $F[X]$-module. This is why the classification of finitely generated $F[X]$-modules is the same theorem as the classification of linear operators up to conjugacy — it produces rational canonical and Jordan forms.

**Is NOT an instance: an abelian group with the trivial action.** Take any abelian group $M$ and *attempt* to define an action of a ring $R$ with more than one element by $r \cdot m := 0_M$ for all $r$ and $m$. Axioms (a), (b), (c) all hold (every side is $0_M$). But axiom (d) fails: it would require $1_R \cdot m = m$, whereas the trivial action gives $1_R \cdot m = 0_M \neq m$ for any $m \neq 0_M$. This non-example pinpoints the role of unitality: without axiom (d) the degenerate zero action would qualify, so axiom (d) is exactly the clause that forces the action to be non-trivial and to genuinely encode the ring.

**Is NOT an instance: $\mathbb{Q}$ as an "$\mathbb{R}$-module".** One cannot make the additive group $\mathbb{Q}$ into a module over $\mathbb{R}$ in a way extending the obvious multiplication. If it were an $\mathbb{R}$-module, then for the element $1 \in \mathbb{Q}$ the scalar $\sqrt{2} \in \mathbb{R}$ would have to produce some $\sqrt{2} \cdot 1 \in \mathbb{Q}$; but axiom (c) would then force $\sqrt{2} \cdot (\sqrt{2} \cdot 1) = (\sqrt{2}\cdot\sqrt{2}) \cdot 1 = 2 \cdot 1 = 2$, so the rational number $q := \sqrt{2}\cdot 1$ satisfies $q^2$-type constraints incompatible with rationality once one also uses distributivity to pin down $\sqrt 2 \cdot 1$ against $\mathbb{Q}$-scalar multiples. The mismatch — a *larger* ring of scalars cannot act on a *smaller* additive group compatibly — illustrates that the action is highly constrained data, not a free choice.

**Corollary (scalars annihilate the zero vector and zero annihilates everything).** Directly from the axioms, $0_R \cdot m = 0_M$ and $r \cdot 0_M = 0_M$ for all $r \in R$, $m \in M$. *Calibration check:* the first uses axiom (a) on $0_R + 0_R = 0_R$ and cancellation in $(M,+)$; the second uses axiom (b) on $0_M + 0_M = 0_M$. If you can reproduce both, you have understood that distributivity, not a separate rule, makes zero absorbing — exactly as in a [[Def - Ring|ring]].

**Corollary (the sign rule).** $(-1_R) \cdot m = -m$ for every $m \in M$. Indeed $m + (-1_R)m = 1_R m + (-1_R)m = (1_R + (-1_R))m = 0_R \cdot m = 0_M$, so $(-1_R)m$ is the additive inverse of $m$. *Calibration check:* this used axioms (d) and (a) and the previous corollary — the same proof as the negative-one rule in a ring. More generally $(-r)m = -(rm) = r(-m)$.

**Corollary (torsion is possible).** Unlike a vector space, a module can have a nonzero element killed by a nonzero scalar. In the $\mathbb{Z}$-module $\mathbb{Z}/4\mathbb{Z}$, the nonzero element $\bar 2$ satisfies $2 \cdot \bar 2 = \bar 4 = \bar 0$ with $2 \neq 0$ in $\mathbb{Z}$. *Calibration check:* if this surprises you, recall that the vector-space proof "$rm = 0, r \neq 0 \implies m = 0$" multiplies through by $r^{-1}$ — a move unavailable when scalars need not be invertible. The whole subject of torsion lives in this gap.

---

# Unlocked by This

> [!tip] Submodules and quotient modules *(from this chapter)*
> With the module axioms fixed, the immediate next steps are the substructure and the quotient: a [[Def - Submodule|submodule]] is a subset closed under both the group operation and the action, and the [[Def - Quotient Module|quotient module]] $M/N$ exists for *any* submodule $N$ — no normality or ideal condition is needed, unlike for groups and rings.

> [!tip] Finitely generated modules and free modules *(from Commutative Algebra)*
> A [[Def - Finitely Generated Module|finitely generated module]] is one expressible as $Rm_1 + \cdots + Rm_k$; a [[Def - Free Module|free module]] is one isomorphic to some $R^n$. The structure theorem for finitely generated modules over a principal ideal domain — the engine behind the classification of finitely generated abelian groups and of linear operators (Jordan form) — is the central goal of the modules course, and it begins here.

> [!tip] Representation theory *(from Algebra)*
> Specialising $R$ to a *group ring* $F[G]$ turns an $R$-module into a representation of the group $G$ over the field $F$. The module axioms become the axioms of a linear group action, and the whole machinery of submodules, quotients and decomposition specialises to subrepresentations, quotient representations, and irreducible decompositions.
