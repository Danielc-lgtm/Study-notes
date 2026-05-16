---
type: definition
subject: module-theory
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Quotient Ring"
  - "Def - Abelian Group"
tags: [algebra, module-theory]
---

# Notation

$R$ is a commutative ring with $1_R$, $M$ is an [[Def - Module|$R$-module]], and $N \leq M$ is a [[Def - Submodule|submodule]]. The quotient module is written $M/N$. Its elements are **cosets** $m + N := \{m + n : n \in N\}$; the coset $m + N$ is also written $\bar m$ when the submodule is fixed and clear. Two cosets satisfy $m + N = m' + N$ if and only if $m - m' \in N$. The zero element of $M/N$ is the coset $0_M + N = N$. See [[Modules I — §3.1–3.2]] for the full notation registry.

---

# Axiom Motivation

The construction to invent is **quotienting**: given a [[Def - Module|module]] $M$ and a [[Def - Submodule|submodule]] $N$, build a new module in which "everything in $N$ has been collapsed to zero". This is the universal move you have already seen for groups (quotient group $G/H$) and for rings (quotient ring $R/I$), and the strategy is always the same: declare two elements *equivalent* when they differ by something in the substructure, and check that the operations descend to the equivalence classes.

The set is forced. We want $m$ and $m'$ identified exactly when $m - m' \in N$. The relation "$m \sim m' \iff m - m' \in N$" is an equivalence relation because $N$ is a subgroup ($N$ contains $0_M$ for reflexivity, is closed under negation for symmetry, closed under addition for transitivity). Its equivalence classes are the **cosets** $m + N$, and the underlying set of the quotient is $M/N$, the set of all such cosets. Nothing here is a choice; it is the only sensible set.

The work — and the place where modules behave *better* than groups and rings — is checking that the two operations descend. Module addition descends because $N$ is a subgroup of the abelian group $(M, +)$: define $(m_1 + N) + (m_2 + N) := (m_1 + m_2) + N$, and if $m_1' \sim m_1$ and $m_2' \sim m_2$ then $m_1' + m_2' - (m_1 + m_2) = (m_1' - m_1) + (m_2' - m_2) \in N$, so the answer is independent of representatives. This is exactly the quotient *group* construction, and it always works for an abelian group quotiented by any subgroup. The new ingredient is the **action**. We want to define $r \cdot (m + N) := (rm) + N$. For this to be well-defined we must check: if $m' \sim m$, is $rm' \sim rm$? That is, if $m' - m \in N$, is $rm' - rm \in N$? Now $rm' - rm = r(m' - m)$, and $m' - m \in N$, so we need $r \cdot (\text{element of } N)$ to lie in $N$. But that is *precisely* the closure-under-the-action axiom of a [[Def - Submodule|submodule]] — condition (2) in the definition of a submodule. So the action descends **for free, for any submodule**, because the submodule axiom was designed to absorb scalar multiplication.

Here is the punchline, and it is worth stating loudly because it is a genuine point of contrast. For **groups**, you cannot quotient by an arbitrary subgroup: $gH$-multiplication descends only when $H$ is *normal*, $gHg^{-1} = H$. For **rings**, you cannot quotient by an arbitrary subring: multiplication descends only when the subobject is an *ideal*, absorbing ring multiplication. In both cases the quotient demands a *special* class of substructure. For **modules**, there is no special class: every submodule already absorbs the action, so $M/N$ is a module for **every** submodule $N$. The reason is structural — a submodule is *defined* by an absorption condition (closure under the $R$-action), which is the very condition the quotient construction needs, whereas a subgroup is defined without any conjugation condition and a subring without any absorption condition. Modules are, in this precise sense, "always quotientable". If you want one sentence to explain why the modules course can move faster than the groups or rings course at this step: the submodule axiom and the well-definedness condition for the quotient are the *same condition*.

A complementary way to see why $M/N$ should exist: it is the universal recipient of a map out of $M$ that kills $N$. There is a natural surjection $q : M \to M/N$, $q(m) = m + N$, the **quotient map**; it is a [[Def - Module Homomorphism|module homomorphism]] with kernel exactly $N$. So $M/N$ is the answer to "what is the largest quotient of $M$ on which $N$ becomes zero", and this is the content the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]] exploits.

---

# The Definition

Let $M$ be an [[Def - Module|$R$-module]] and $N \leq M$ a [[Def - Submodule|submodule]]. The **quotient module** $M/N$ is the [[Def - Module|$R$-module]] whose:

- **Underlying set** is the set of cosets $\{m + N : m \in M\}$, where $m + N = \{m + n : n \in N\}$ and two cosets are equal, $m + N = m' + N$, exactly when $m - m' \in N$;
- **Addition** is $(m_1 + N) + (m_2 + N) = (m_1 + m_2) + N$, with zero element $0_{M/N} = 0_M + N = N$ and additive inverse $-(m + N) = (-m) + N$ — this is the quotient of the abelian group $(M, +, 0_M)$ by the subgroup $N$;
- **Action** is $r \cdot (m + N) = (r \cdot m) + N$, for $r \in R$.

Both operations are **well-defined** — independent of the choice of coset representatives — and satisfy the module axioms. Well-definedness of addition uses only that $N$ is a subgroup; well-definedness of the action uses exactly that $N$ is closed under the $R$-action. **No further hypothesis on $N$ is required**: $M/N$ is a module for *every* submodule $N$, in contrast with quotient groups (which need a normal subgroup) and quotient rings (which need an ideal).

The surjection $q : M \to M/N$, $q(m) = m + N$, is the **quotient map** (or **canonical projection**); it is a [[Def - Module Homomorphism|module homomorphism]] with $\ker q = N$ and $\operatorname{im} q = M/N$.

---

# Relate to Other Fields / Compression

The quotient module is **the quotient-group construction with one extra line of bookkeeping for the action**. Forget the action and $M/N$ is literally the [[Def - Abelian Group|abelian group]] quotient $(M,+)/(N,+)$; everything new is the single formula $r(m+N) = rm + N$, and the single check that it is well-defined.

Against its siblings, the quotient module is the construction with the **fewest preconditions**. A quotient *group* $G/H$ exists only for a *normal* subgroup; a [[Def - Quotient Ring|quotient ring]] $R/I$ exists only for an *ideal*. The quotient *module* $M/N$ exists for *any* submodule. The reason is uniform: each quotient needs the substructure to absorb the relevant operation under the equivalence relation, and the submodule is the only one of the three substructure notions that is *defined by* an absorption condition. So "modules are always quotientable" is not a coincidence but a corollary of how the substructure was axiomatised.

When $R$ is a field, $M/N$ is exactly the **quotient vector space** $V/W$ of linear algebra, with $\dim(V/W) = \dim V - \dim W$. When $M = R$ and $N = I$ is an ideal, the quotient module $R/I$ is the additive-and-action shadow of the [[Def - Quotient Ring|quotient ring]] $R/I$ — same set, same addition, and the $R$-action $r \cdot (a + I) = ra + I$ is the quotient ring's multiplication restricted to scalars from $R$.

---

# Examples / Corollaries

**Is an instance: $\mathbb{Z}/n\mathbb{Z}$.** Take the $\mathbb{Z}$-module $M = \mathbb{Z}$ and the submodule $N = n\mathbb{Z}$. The quotient module $\mathbb{Z}/n\mathbb{Z}$ has $n$ elements, the cosets $\bar 0, \bar 1, \ldots, \overline{n-1}$, with the $\mathbb{Z}$-action $k \cdot \bar a = \overline{ka}$. As a $\mathbb{Z}$-module this is a finite abelian group — the cyclic group of order $n$ — and it visibly exhibits torsion: $n \cdot \bar a = \bar 0$ for every element. This is the prototype quotient module.

**Is an instance: quotient vector space $V/W$.** If $F$ is a field, $V$ a vector space and $W$ a subspace, the quotient module $V/W$ is the quotient vector space. For instance with $V = \mathbb{R}^2$ and $W$ the $x$-axis, $V/W$ is a $1$-dimensional space whose elements are the horizontal lines $\{(x, y_0) : x \in \mathbb{R}\}$; addition of lines and scaling of lines are induced from $\mathbb{R}^2$, and $\dim(V/W) = 2 - 1 = 1$.

**Is an instance: $R/I$ as an $R$-module.** For an [[Def - Ideal|ideal]] $I \trianglelefteq R$, regarding $R$ as a module over itself and quotienting by the submodule $I$ gives the $R$-module $R/I$, with action $r \cdot (a + I) = ra + I$. This is the same underlying set and addition as the [[Def - Quotient Ring|quotient ring]] $R/I$; the module structure remembers how $R$ scales the quotient but forgets the internal multiplication of $R/I$ by its *own* elements.

**Is an instance: $M/M$ and $M/\{0_M\}$.** The two extreme quotients. Quotienting by the whole module, $M/M$, collapses everything to a single coset and is the **zero module**. Quotienting by the zero submodule, $M/\{0_M\}$, identifies $m$ with $m'$ only when $m - m' = 0_M$, so it is canonically isomorphic to $M$ itself via $m + \{0_M\} \mapsto m$. These bracket every quotient: $M/N$ interpolates between $M$ (at $N = 0$) and $0$ (at $N = M$).

**Is NOT an instance — the contrast: you would NOT need a "normal submodule".** It is tempting, by analogy with groups, to expect that only some privileged submodules admit a quotient. They do not. Consider $M = \mathbb{Z}^2$ as a $\mathbb{Z}$-module and the submodule $N = \mathbb{Z} \cdot (1, 0)$. There is *no* normality condition to verify: $\mathbb{Z}^2 / N \cong \mathbb{Z}$ is a perfectly good module, formed exactly as for any submodule. The "non-example" here is the **non-phenomenon**: whereas a non-normal subgroup of a group genuinely fails to yield a quotient group, *no* submodule fails to yield a quotient module. Any time you find yourself checking a normality- or ideal-type condition before forming $M/N$, you have imported a hypothesis that module theory does not require.

**Is NOT an instance: quotient by a mere subgroup that is not a submodule.** If $N$ is a subgroup of $(M, +)$ but *not* closed under the $R$-action, the additive quotient group $(M,+)/N$ still exists, but it is **not** an $R$-module under $r(m + N) := rm + N$, because that formula is not well-defined: representatives differing by $n \in N$ can have $rn \notin N$. For example, in $M = \mathbb{Z}[X]$ over $R = \mathbb{Z}[X]$, the subgroup $N = \mathbb{Z}$ of constants is not a submodule; $\mathbb{Z}[X]/\mathbb{Z}$ is an abelian group but carries no compatible $\mathbb{Z}[X]$-action — $X \cdot (1 + \mathbb{Z})$ would have to be both $X + \mathbb{Z}$ and (using $1 \sim 0$) $0 + \mathbb{Z}$. This is the precise sense in which submodule-hood, not mere subgroup-hood, is the right and necessary input.

**Corollary (the quotient map is a surjective homomorphism with kernel $N$).** The map $q : M \to M/N$, $q(m) = m + N$, is an $R$-[[Def - Module Homomorphism|module homomorphism]]: it respects addition and $q(rm) = rm + N = r(m + N) = r\, q(m)$. It is surjective by construction, and $\ker q = \{m : m + N = N\} = N$. *Calibration check:* every submodule of $M$ arises as the kernel of some module homomorphism out of $M$ — namely its own quotient map — exactly mirroring "every ideal is a kernel" and "every normal subgroup is a kernel".

**Corollary (universal property / first isomorphism theorem).** If $f : M \to P$ is any [[Def - Module Homomorphism|module homomorphism]] with $N \subseteq \ker f$, then $f$ factors uniquely through $q$: there is a unique homomorphism $\bar f : M/N \to P$ with $\bar f \circ q = f$, given by $\bar f(m + N) = f(m)$. Taking $N = \ker f$ and noting $\bar f$ is then injective with image $\operatorname{im} f$ yields the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]] $M/\ker f \cong \operatorname{im} f$. *Calibration check:* this is the same factorisation that holds for groups and rings; modules differ only in that the input $N$ ranges over *all* submodules.

**Corollary (quotients of finitely generated modules are finitely generated).** If $M$ is [[Def - Finitely Generated Module|finitely generated]] and $N \leq M$, then $M/N$ is finitely generated. *Calibration check:* if $m_1, \ldots, m_k$ generate $M$, then their images $m_1 + N, \ldots, m_k + N$ generate $M/N$, since the quotient map $q$ is a surjective homomorphism and $q(r_1 m_1 + \cdots + r_k m_k) = r_1(m_1 + N) + \cdots + r_k(m_k + N)$. (The submodule $N$ itself, by contrast, need *not* be finitely generated.)

---

# Unlocked by This

> [!tip] Isomorphism theorems for modules *(from this chapter)*
> The quotient module is the engine of the [[Thm - Isomorphism Theorems for Modules|three isomorphism theorems]]: the first identifies $M/\ker f \cong \operatorname{im} f$ for a [[Def - Module Homomorphism|module homomorphism]] $f$, and the second and third are statements about how quotients interact with sums and chains of submodules. The proofs are identical to the group and ring versions.

> [!tip] Cyclic modules and the structure theorem *(from Commutative Algebra)*
> Every cyclic module $Rm$ is a quotient $R/\operatorname{Ann}(m)$ of the ring by an [[Def - Ideal|ideal]], via the [[Thm - Isomorphism Theorems for Modules|first isomorphism theorem]]. Iterating this — writing a [[Def - Finitely Generated Module|finitely generated module]] as a quotient of a [[Def - Free Module|free module]] $R^k$ — is the first step toward the structure theorem for finitely generated modules over a principal ideal domain.
