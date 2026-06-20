---
type: exercise
subject: higher-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Operad"
  - "Def - Algebra for an Operad"
  - "Def - Monad and Comonad"
  - "Def - Algebra for a Monad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $P$ be an [[Def - Operad|operad]] in $\mathbf{Set}$. Define the endofunctor $T_P$ on $\mathbf{Set}$ by
$$T_P(X) = \coprod_{n \geq 0} P(n) \times_{S_n} X^n,$$
where $P(n) \times_{S_n} X^n$ is the quotient of $P(n) \times X^n$ by the relation $(\theta\cdot\sigma, x_1, \dots, x_n) \sim (\theta, x_{\sigma(1)}, \dots, x_{\sigma(n)})$.

(a) Equip $T_P$ with a unit $\eta : \mathrm{Id} \to T_P$ and multiplication $\mu : T_P T_P \to T_P$ making it a [[Def - Monad and Comonad|monad]]; verify the monad axioms (using the operad unit and composition).

(b) Prove that the category of [[Def - Algebra for an Operad|$P$-algebras]] is isomorphic to the category of [[Def - Algebra for a Monad|Eilenberg–Moore algebras]] for $T_P$.

(c) Identify $T_P$ for $P = \mathrm{Assoc}$ and for $P = \mathrm{Comm}$, and recognise these as the free-monoid and free-commutative-monoid monads.

**Recall:**

![[Def - Monad and Comonad#The Definition]]

A [[Def - Algebra for a Monad|monad algebra]] (Eilenberg–Moore algebra) for $(T, \eta, \mu)$ is an object $X$ with $h : TX \to X$ satisfying $h \circ \eta_X = \mathrm{id}_X$ and $h \circ \mu_X = h \circ Th$. A $P$-algebra has structure maps $\rho_n : P(n) \times_{S_n} X^n \to X$ compatible with operad composition, unit, and the action.

---

# Convergent Strategy

**Problem class:** This is a *bridge-between-two-formalisms* problem: realise an operad as a monad and match their algebras. It applies the corollary of [[Thm - Operads as Monoids in Symmetric Sequences|the monoid theorem]] concretely, and the method is to build the monad structure from the operad data and chase the algebra definitions until they coincide.

**Assumption pattern:** The signal is "a sum of symmetric-power pieces". The endofunctor $T_P(X) = \coprod_n P(n) \times_{S_n} X^n$ is *analytic* (polynomial with symmetric coefficients), and any such endofunctor is a monad exactly when the coefficients form an operad. Recognising $T_P$ as "free $P$-algebra on $X$" tells you immediately that its monad structure is the free–forgetful one and its algebras are $P$-algebras.

**Theorem routing:** Part (a) builds $\eta$ from the unit $\mathrm{id} \in P(1)$ (an element $x \in X = P(1)\times_{S_1} X^1 \subseteq T_P X$) and $\mu$ from the operad composition $\gamma$ (substituting operations into operations). The monad axioms route through operad associativity and unitality. Part (b) routes through unwinding both algebra definitions to the same data $\coprod_n P(n)\times_{S_n} X^n \to X$. Part (c) routes through computing the coinvariants: for $\mathrm{Assoc}$, $S_n \times_{S_n} X^n = X^n$ gives $\coprod_n X^n$ (lists, the free monoid monad); for $\mathrm{Comm}$, $\{*\}\times_{S_n} X^n = X^n/S_n$ gives unordered tuples (the free commutative monoid monad).

**Key decision point:** The crux of (a) is defining $\mu$ correctly: an element of $T_P T_P(X)$ is "an operation $\theta \in P(k)$ applied to $k$ elements of $T_P X$, each itself an operation applied to elements of $X$" — i.e. a two-layer structure — and $\mu$ must *graft* using $\gamma$. The temptation is to mishandle the symmetric coinvariants; one must check $\mu$ is well-defined on the $\times_{S_n}$ quotients, which is exactly where operad equivariance is used. In (c) the decision is to *compute the coinvariants* concretely rather than reason abstractly: $S_n \times_{S_n} X^n \cong X^n$ versus $\{*\} \times_{S_n} X^n \cong X^n/S_n$ is the whole difference between lists and multisets.

---

# Legal Operations Used

1. **Build the operadic monad from the operad (operation 6 from the topic page).** We assemble $T_P$, $\eta$, $\mu$ from the operad data.

2. **Verify monad axioms via operad axioms (operation 2 from the topic page).** Operad associativity and unit become the monad axioms.

3. **Match two algebra definitions (operation 4 from the topic page).** We identify $P$-algebras with $T_P$-algebras.

4. **Compute symmetric coinvariants explicitly (operation 3 from the topic page).** We evaluate $P(n)\times_{S_n} X^n$ for $\mathrm{Assoc}$ and $\mathrm{Comm}$.

---

# Hints

> [!note]- Hint 1
> The unit $\eta_X : X \to T_P X$ sends $x$ to the class of $(\mathrm{id}, x) \in P(1) \times_{S_1} X^1$. This is "the trivial unary operation applied to $x$".

> [!note]- Hint 2
> An element of $T_P T_P(X)$ is a class of $(\theta; t_1, \dots, t_k)$ with $\theta \in P(k)$ and each $t_i = [\varphi_i; x_{i,\bullet}] \in T_P X$. Define $\mu$ to graft: $\mu[\theta; t_\bullet] = [\gamma(\theta; \varphi_1, \dots, \varphi_k);\ x_{1,1}, \dots, x_{k,n_k}]$. Check this respects the $\times_{S_n}$ relations using operad equivariance.

> [!note]- Hint 3
> Monad associativity $\mu \circ T_P\mu = \mu \circ \mu_{T_P}$ is operad associativity of $\gamma$ (the two ways of grafting a three-layer structure). The unit axioms are the operad unit laws.

> [!note]- Hint 4
> For (c): $\mathrm{Assoc}(n) = S_n$, and $S_n \times_{S_n} X^n \cong X^n$ (the free $S_n$-set quotients to a single copy). So $T_{\mathrm{Assoc}}(X) = \coprod_n X^n$ = lists = free monoid. $\mathrm{Comm}(n) = \{*\}$, and $\{*\} \times_{S_n} X^n = X^n/S_n$ = unordered $n$-tuples = multisets = free commutative monoid.

---

# Solution

The plan: define $\eta, \mu$ from the operad unit and $\gamma$ and verify the monad axioms (Step 1); match $P$-algebras with $T_P$-algebras by unwinding both (Step 2); compute $T_{\mathrm{Assoc}}$ and $T_{\mathrm{Comm}}$ via coinvariants (Step 3).

**Step 1: $T_P$ is a monad.**

> [!note]- Derivation
> *Unit.* $\eta_X(x) = [\mathrm{id}; x] \in P(1)\times_{S_1} X$. Natural in $X$.
>
> *Multiplication.* An element of $T_P T_P X$ is $[\theta; t_1, \dots, t_k]$ with $\theta \in P(k)$, $t_i = [\varphi_i; x_{i,1}, \dots, x_{i,n_i}]$. Define
> $$\mu_X[\theta; t_\bullet] = \big[\gamma(\theta; \varphi_1, \dots, \varphi_k);\ x_{1,1}, \dots, x_{k,n_k}\big] \in P\big({\textstyle\sum} n_i\big)\times_{S_{\sum n_i}} X^{\sum n_i}.$$
> *Well-defined:* if we replace $\theta$ by $\theta\cdot\sigma$ and permute the $t_i$ accordingly, operad equivariance ensures $\gamma(\theta\cdot\sigma; \dots) = \gamma(\theta; \dots)\cdot\sigma\langle n_\bullet\rangle$, matching the corresponding permutation of the $x$'s; similarly for permutations inside each $t_i$. So $\mu$ descends to the coinvariants.
>
> *Monad axioms.* Left/right unit: $\mu \circ \eta_{T_P} = \mathrm{id} = \mu \circ T_P\eta$ are the operad unit laws $\gamma(\mathrm{id}; \varphi) = \varphi = \gamma(\theta; \mathrm{id}, \dots)$. Associativity: $\mu \circ \mu_{T_P}$ grafts the bottom two layers first, $\mu \circ T_P\mu$ grafts the top two first; both equal the single grafting of the three-layer structure by operad associativity of $\gamma$. So $(T_P, \eta, \mu)$ is a monad.

**Step 2: $P$-algebras = $T_P$-algebras.**

> [!note]- Derivation
> A $T_P$-algebra is $h : T_P X \to X$ with $h\eta = \mathrm{id}$, $h\mu = h \circ T_P h$. Now $h : \coprod_n P(n)\times_{S_n} X^n \to X$ is the same data as a family $\rho_n : P(n)\times_{S_n} X^n \to X$, i.e. $S_n$-equivariant maps $P(n)\times X^n \to X$ — exactly the structure maps of a [[Def - Algebra for an Operad|$P$-algebra]]. The condition $h\eta = \mathrm{id}$ is $\rho_1(\mathrm{id}; x) = x$, the algebra unit law. The condition $h\mu = h\circ T_P h$ unwinds: $h\mu[\theta; \varphi_\bullet; x_\bullet] = \rho(\gamma(\theta; \varphi_\bullet); x_\bullet)$, while $h \circ T_P h$ first applies $\rho$ to each inner layer then $\rho(\theta; -)$, giving $\rho(\theta; \rho(\varphi_1; x_{1,\bullet}), \dots)$. Their equality is the algebra associativity. So $T_P$-algebra structures = $P$-algebra structures, and a morphism of $T_P$-algebras is a morphism of $P$-algebras. Hence $\mathbf{Set}^{T_P} \cong \mathrm{Alg}_P$.

**Step 3: $T_{\mathrm{Assoc}}$ and $T_{\mathrm{Comm}}$.**

> [!note]- Derivation
> *$\mathrm{Assoc}$.* $\mathrm{Assoc}(n) = S_n$ with the regular (free) action, so $S_n \times_{S_n} X^n \cong X^n$ canonically (each orbit of the diagonal action has a unique representative with $\theta = e$). Thus $T_{\mathrm{Assoc}}(X) = \coprod_n X^n$, the set of finite **lists** in $X$; $\eta$ is the singleton list and $\mu$ is concatenation/flattening. This is the **free-monoid monad** (see [[Ex - The free monoid monad|the free-monoid monad]]), whose algebras are monoids — consistent with $\mathrm{Assoc}$-algebras being monoids.
>
> *$\mathrm{Comm}$.* $\mathrm{Comm}(n) = \{*\}$ with trivial action, so $\{*\} \times_{S_n} X^n = X^n/S_n$, the **unordered** $n$-tuples (multisets of size $n$). Thus $T_{\mathrm{Comm}}(X) = \coprod_n X^n/S_n$, the set of finite **multisets** in $X$; $\eta$ is the singleton multiset, $\mu$ is multiset union. This is the **free-commutative-monoid monad**, whose algebras are commutative monoids — consistent with $\mathrm{Comm}$-algebras. The contrast lists-versus-multisets is precisely the free-versus-trivial $S_n$-action, the same dial as $\mathrm{Assoc}$-versus-$\mathrm{Comm}$.

> [!note]- Complete formal solution
> *(a)* $\eta_X(x) = [\mathrm{id}; x]$; $\mu_X[\theta; [\varphi_i; x_{i,\bullet}]_i] = [\gamma(\theta; \varphi_\bullet); x_{\bullet,\bullet}]$, well-defined on coinvariants by operad equivariance. Monad unit and associativity axioms are the operad unit and associativity of $\gamma$. So $T_P$ is a monad.
>
> *(b)* A $T_P$-algebra $h : T_P X \to X$ is a family $\rho_n : P(n)\times_{S_n} X^n \to X$; the EM axioms are exactly the operad-algebra unit and associativity. Hence $\mathbf{Set}^{T_P} \cong \mathrm{Alg}_P$.
>
> *(c)* $T_{\mathrm{Assoc}}(X) = \coprod_n X^n$ (lists, free-monoid monad); $T_{\mathrm{Comm}}(X) = \coprod_n X^n/S_n$ (multisets, free-commutative-monoid monad). $\blacksquare$

---

# Key Takeaways

**Every operad is a monad, and operads are exactly the "analytic" monads.** The central lesson is the bridge $P \mapsto T_P$: an operad always induces a monad whose algebras it controls, so operad theory is a *refinement* of monad theory. The endofunctor $T_P(X) = \coprod_n P(n)\times_{S_n} X^n$ is a sum of symmetric-power pieces — a "power series in $X$ with coefficients the $S_n$-sets $P(n)$" — and the operad is precisely the data needed to make this power series a monad (the operad composition is the monad multiplication). The recognition heuristic: when a monad's underlying functor is such a sum-of-symmetric-powers, it comes from an operad, and you gain the entire operadic toolkit (free algebras, presentations, resolutions) on its algebras. This is why operads dominate where monads are too coarse — they carry the extra "presentation by graded operations" that opaque monads lack.

**The symmetric coinvariants are where lists become multisets.** The computation in (c) crystallises the role of the $\times_{S_n}$ quotient: with a free $S_n$-action ($\mathrm{Assoc}$) the quotient does nothing and you get ordered lists; with a trivial action ($\mathrm{Comm}$) the quotient identifies all orderings and you get unordered multisets. The general slogan — *coinvariants by a free action are invisible; coinvariants by a trivial action are total symmetrisation* — lets you predict the shape of any operadic monad from the $S_n$-set structure of the operad. This is the same associative-to-commutative dial seen throughout the chapter, now visible at the level of the free-algebra functor: free monoid (lists) versus free commutative monoid (multisets).

**Well-definedness on coinvariants is exactly where equivariance earns its keep.** The one genuinely technical point — that $\mu$ descends to the $\times_{S_n}$ quotients — is precisely the operad equivariance axiom doing its job. This is a recurring pattern: whenever you define a map out of a quotient by a group action, the well-definedness check *is* an equivariance condition, and structures are axiomatised with equivariance built in exactly so that such maps exist. Recognising this tells you where to look when a construction on operadic or equivariant objects threatens to be ill-defined: the fix is always to verify compatibility with the symmetric action, and the axiom guaranteeing it is equivariance. It is the same role equivariance played in the endomorphism operad and in the composition product, unified here as "the action axiom that makes coinvariant constructions work".
