---
type: theorem
subject: module-theory
prereqs:
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Quotient Module"
  - "Def - Module Homomorphism"
  - "Thm - First Isomorphism Theorem for Rings"
  - "Thm - First Isomorphism Theorem (group version)"
tags: [algebra, module-theory]
---

# Notation

Throughout, $R$ is a commutative ring with identity and all modules are [[Def - Module|$R$-modules]]. A [[Def - Module Homomorphism|module homomorphism]] $f : M \to N$ is a map of abelian groups satisfying $f(r \cdot m) = r \cdot f(m)$ for all $r \in R$, $m \in M$; its **kernel** is $\ker f = \{m \in M : f(m) = 0_N\}$ and its **image** is $\operatorname{im} f = \{f(m) : m \in M\}$. The relation $N \leq M$ means $N$ is a [[Def - Submodule|submodule]] of $M$ — an additive subgroup closed under the $R$-action. For $N \leq M$, the [[Def - Quotient Module|quotient module]] $M/N$ is the set of cosets $m + N$ with addition $(m + N) + (m' + N) = (m + m') + N$ and action $r \cdot (m + N) = (r \cdot m) + N$. For two submodules $A, B \leq M$, their **sum** is $A + B = \{a + b : a \in A,\ b \in B\}$ and their **intersection** $A \cap B$ is the set-theoretic intersection; both are submodules. The symbol $\cong$ denotes module isomorphism — a bijective module homomorphism. The full symbol registry is on the parent page [[Modules I — §3.1–3.2]].

---

# Statement

> **Isomorphism Theorems for Modules.** Let $R$ be a commutative ring and let all modules below be $R$-modules.
>
> **First Isomorphism Theorem.** Let $f : M \to N$ be a module homomorphism. Then $\ker f$ is a submodule of $M$, $\operatorname{im} f$ is a submodule of $N$, and the map
> $$\Phi : M/\ker f \longrightarrow \operatorname{im} f, \qquad m + \ker f \longmapsto f(m)$$
> is a well-defined module isomorphism. Hence $M/\ker f \;\cong\; \operatorname{im} f$.
>
> **Second Isomorphism Theorem.** Let $A, B \leq M$ be submodules. Then $A + B$ and $A \cap B$ are submodules of $M$, and
> $$\frac{A + B}{A} \;\cong\; \frac{B}{A \cap B}.$$
>
> **Third Isomorphism Theorem.** Let $N \leq L \leq M$ be submodules. Then $L/N$ is a submodule of $M/N$, and
> $$\frac{M}{L} \;\cong\; \left.\left(\frac{M}{N}\right)\middle/\left(\frac{L}{N}\right)\right..$$
>
> **Submodule Correspondence.** For a submodule $N \leq M$, the assignment $L \mapsto L/N$ is an inclusion-preserving bijection
> $$\{\text{submodules } L \text{ of } M \text{ with } N \leq L\} \;\longleftrightarrow\; \{\text{submodules of } M/N\}.$$

---

# Motivation

You have just built three new gadgets — the submodule, the quotient module $M/N$, and the module homomorphism — and the immediate question is the same one you asked the first time you met a quotient group and the first time you met a quotient ring: given a quotient $M/N$, *what is it?* Which module that you already understand does it equal up to isomorphism? Reasoning about $M/N$ directly is unpleasant, because its elements are cosets, which are sets, and arithmetic on sets is awkward. The isomorphism theorems are the standard machinery for replacing a quotient by a recognisable module.

Here is the deeper point, and it is the reason this page treats all three theorems together rather than one at a time. You have now proved a "first isomorphism theorem" three times — once for groups, once for rings, now for modules — and each time the statement was the same shape and the proof was the same proof. That is not a coincidence to be tolerated; it is a fact to be understood. The isomorphism theorems are **structure-agnostic**. They are statements about quotients by sub-objects, and they hold in any setting where you have a notion of "sub-object you may quotient by" together with structure-preserving maps. Groups supply normal subgroups; rings supply ideals; modules supply submodules. The arithmetic decoration — a multiplication, an external action — rides along passively. The Cambridge source makes this explicit: it states the module first isomorphism theorem and then writes "we will not prove this again. The proof is exactly the same." This page records that fact and then explains *why* the proof is the same, which is more useful than re-typing it.

There is also something genuinely new in the module setting, and it is a simplification rather than a complication. In groups you could quotient only by *normal* subgroups — a special, restricted class of subgroups. In rings you could quotient only by *ideals* — and an ideal is not a kind of subring at all, it is its own species of sub-object. Modules drop this friction entirely: you can quotient by **any** submodule whatsoever. There is no "normal submodule", no separate "ideal-like" object. Every submodule is quotientable. This is why the second and third isomorphism theorems are cleaner here than for groups: there are no normality side-conditions to track. The single notion of submodule does all the work, and the three isomorphism theorems plus the submodule correspondence describe completely how submodules and quotients interact.

The practical reading is unchanged from the ring case. The first theorem says: to identify $M/N$, do not dissect the quotient — go hunting for a *surjective* homomorphism *out of $M$* whose kernel is $N$, and read off $M/N \cong (\text{its target})$. The second and third theorems are then not new ideas but corollaries of the first applied to two cleverly chosen homomorphisms. And the submodule correspondence is the companion bookkeeping result: where the first theorem identifies the quotient *module*, the correspondence identifies the quotient's *lattice of submodules*.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition of the first theorem is mild — *any* module homomorphism $f : M \to N$ — so the real skill is recognising the disguised input: a problem that secretly hands you a homomorphism, even when none is named.

The first disguised source is **a single element $m$ of a module, used as a "scaling map"**. For any $m \in M$ the assignment $r \mapsto r \cdot m$ is a module homomorphism $R \to M$ (here $R$ is regarded as a module over itself). This is non-obvious because $m$ is an *element*, not a map, yet fixing $m$ and letting the ring scalar vary produces a homomorphism out of $R$. Its image is the [[Def - Finitely Generated Module|cyclic submodule]] $Rm$ and its kernel is the [[Def - Annihilator|annihilator]] $\operatorname{Ann}(m)$, so the first theorem instantly yields $Rm \cong R/\operatorname{Ann}(m)$. *Example problem:* identify the cyclic $\mathbb{Z}$-module generated by an element of order $n$ inside an abelian group — it is $\mathbb{Z}/n\mathbb{Z}$, because the annihilator is $n\mathbb{Z}$.

The second disguised source is **two submodules sitting inside a common ambient module**. Given $A, B \leq M$, the composite $B \hookrightarrow A + B \twoheadrightarrow (A+B)/A$ — inclusion of $B$ followed by the quotient map — is a homomorphism $B \to (A+B)/A$, manufactured rather than given. Its kernel is $A \cap B$ and it is surjective, so the first theorem delivers the second isomorphism theorem. The non-obvious move is that *composing an inclusion with a quotient map builds a brand-new homomorphism* whose kernel and image are computable. *Example problem:* compute $(A+B)/A$ for two subspaces of a vector space — it is $B/(A \cap B)$, the source of the dimension formula $\dim(A+B) = \dim A + \dim B - \dim(A \cap B)$.

The third disguised source is **a nested pair of submodules $N \leq L \leq M$**. The two quotient maps $M \to M/N$ and $M/N \to (M/N)/(L/N)$ compose to a surjection $M \to (M/N)/(L/N)$ whose kernel is exactly $L$; the first theorem then yields the third isomorphism theorem. The non-obviousness is that a *quotient of a quotient* is still a quotient of the original, by a larger submodule. *Example problem:* simplify an iterated quotient $(\mathbb{Z}/12\mathbb{Z})/(2\mathbb{Z}/12\mathbb{Z})$ to $\mathbb{Z}/2\mathbb{Z}$.

A fourth disguised source is **a generating set, used to build a homomorphism out of a [[Def - Free Module|free module]]**. If $M = Rm_1 + \dots + Rm_k$, then $(r_1, \dots, r_k) \mapsto \sum r_i m_i$ is a surjective homomorphism $R^k \twoheadrightarrow M$ (see [[Thm - Finitely Generated Modules and Surjections from a Free Module]]). The first theorem then writes $M \cong R^k/K$ for the [[Def - Finitely Presented Module|relation submodule]] $K = \ker$. This is the engine of finite presentations.

**Targets (Output Amplification)**

The bare conclusion of the first theorem is an isomorphism $M/\ker f \cong \operatorname{im} f$. Combined with other facts it does more.

Combine the conclusion with **surjectivity of $f$**. If $f$ is onto, then $\operatorname{im} f = N$ and the conclusion sharpens to $M/\ker f \cong N$: a clean identification of the *whole* target module as a quotient of $M$. The further result is that any surjection $M \twoheadrightarrow N$ exhibits $N$ as $M$ modulo a single submodule, so structural questions about $N$ become questions about the submodule $\ker f$.

Combine the conclusion with **the field case, where every module is a vector space**. When $R = F$ is a [[Def - Unit and Field|field]], modules are $F$-vector spaces, submodules are subspaces, and "isomorphism" is a vector-space isomorphism. Taking dimensions in $V/\ker T \cong \operatorname{im} T$ yields the **rank–nullity theorem** $\dim V = \dim \ker T + \dim \operatorname{im} T$. The further result is that the abstract first isomorphism theorem *is* rank–nullity once dimension is available — and this very specialisation is what powers [[Thm - Invariance of Rank]].

Combine the second theorem with **a dimension function**. For vector spaces, $(A+B)/A \cong B/(A \cap B)$ becomes, on taking dimensions, the inclusion–exclusion formula $\dim(A+B) + \dim(A \cap B) = \dim A + \dim B$ — a non-obvious counting identity falling straight out of an isomorphism of quotients.

---

# Why Is It True

Forget the formal proof and picture what a module homomorphism $f$ does to $M$. It sends $M$ onto $\operatorname{im} f$, and along the way it identifies some elements — it can send $m$ and $m'$ to the same place. Ask which elements get identified. Because $f$ is in particular an additive homomorphism, $f(m) = f(m')$ if and only if $f(m) - f(m') = 0_N$, which says $f(m - m') = 0_N$, which says $m - m' \in \ker f$. But "$m - m' \in \ker f$" is exactly the condition for $m$ and $m'$ to lie in the same coset of $\ker f$. So:

> Two elements of $M$ have the same image under $f$ **exactly when** they lie in the same coset of $\ker f$.

The cosets of $\ker f$ are *literally* the fibres of $f$ — the sets of elements sharing a common image. The quotient $M/\ker f$ is, by construction, the set of these fibres. Sending each fibre to the common value of $f$ on it is therefore a bijection onto $\operatorname{im} f$: surjective because every value of $f$ is attained on some fibre, injective because distinct fibres carry distinct values. The map $\Phi$ is not a clever construction one must be lucky to find — it is the only thing $f$ could possibly be once you collapse its redundancy.

Now the structure-agnosticism. A module is an abelian group $(M, +)$ with an external $R$-action bolted on. The entire additive content of the first isomorphism theorem — that $\ker f$ is an additive subgroup, that $\Phi$ is well-defined, bijective, and additive — is *already done* by the [[Thm - First Isomorphism Theorem (group version)|first isomorphism theorem for groups]], applied verbatim to $(M, +)$. Nothing in that part knows there is an $R$-action. So the only genuinely module-theoretic content is two one-line checks: that $\ker f$ is closed under the $R$-action ($m \in \ker f \implies r m \in \ker f$, because $f(rm) = r f(m) = r \cdot 0 = 0$), and that $\Phi$ respects the action ($\Phi(r(m + \ker f)) = \Phi(rm + \ker f) = f(rm) = r f(m) = r\Phi(m + \ker f)$). Both are immediate because the action on the quotient is *defined* on representatives. This is exactly the same two-line addition that upgraded the group theorem to the [[Thm - First Isomorphism Theorem for Rings|ring theorem]] — only now the decoration is an action rather than a multiplication. **The slogan: the first isomorphism theorem is a theorem about abelian groups, and the $R$-action comes along for free.** This is why the source can say "the proof is exactly the same" — it genuinely is, and the second and third theorems then follow by feeding the first theorem two specific homomorphisms.

For the **second theorem**, the intuition is a single picture. Inside the big module $A + B$ sits the submodule $A$. The module $B$ also sits inside $A + B$, overlapping $A$ exactly in $A \cap B$. Now collapse $A$ to zero. Every element of $A + B$ becomes a coset $a + b + A = b + A$, so the collapsed module is "$B$ with the overlap squashed" — and the overlap is $A \cap B$. Hence $(A+B)/A$, the result of squashing $A$, is the same as $B$ with $A \cap B$ squashed, which is $B/(A \cap B)$. The formal proof just makes "collapse $A$" into the homomorphism $B \to (A+B)/A$ and checks its kernel is $A \cap B$.

For the **third theorem**, the intuition is that quotienting is *cumulative*. To form $M/L$ you delete everything in $L$. You can do this in two stages: first delete the smaller submodule $N$ (forming $M/N$), then delete what remains of $L$ (which is $L/N$, the image of $L$ inside $M/N$). Deleting in two stages must give the same answer as deleting all at once — that is all the third theorem says. The "cancel the $N$" pattern $\frac{M/N}{L/N} \cong \frac{M}{L}$ is the module analogue of cancelling a common factor.

The **submodule correspondence** is true because the quotient map $q : M \to M/N$ does not lose or scramble the submodule structure *above $N$*. Every submodule of $M/N$ is a collection of cosets; gathering up all the elements in those cosets gives a submodule of $M$ that contains $N$ (it contains $N$ because the zero coset $N$ is in any submodule of $M/N$). Conversely a submodule $L \supseteq N$ maps to the submodule $L/N$. These two operations undo each other because $L \supseteq N$ means $L$ is already a union of $N$-cosets — there is no information below $N$ for the correspondence to mishandle.

---

# What Makes This Hard

The genuine module-theoretic content is tiny — almost everything is inherited from the group theorem applied to $(M, +)$ — so the trap is *over-proving*: re-deriving well-definedness, bijectivity, and additivity of $\Phi$ from scratch when those are free, and missing that the only new obligations are $R$-closure of $\ker f$ and $R$-equivariance of $\Phi$. For the second and third theorems the difficulty is purely *choosing the right homomorphism to feed the first theorem* and then *correctly computing its kernel* — for the second theorem the subtle point is that the map is defined on $B$ (not on $A+B$) so that the kernel comes out as $A \cap B$; the most common error is to set up the map on the wrong domain and obtain a kernel that is not a recognisable submodule.

---

# Rederivation Scaffold

**High-level strategy:**
Prove the first theorem once, by citing the group theorem for the additive part and adding two $R$-action checks. Then derive the second and third theorems as corollaries: each is the first theorem applied to one specific surjective homomorphism, and the only work is identifying that homomorphism and computing its kernel. The submodule correspondence follows by exhibiting the two mutually inverse maps $L \mapsto L/N$ and (submodule of $M/N$) $\mapsto$ (its preimage under the quotient map).

**Subgoal decomposition:**

1. **First theorem — kernel and image are submodules.** Show $\ker f \leq M$ and $\operatorname{im} f \leq N$.
   - *Hint:* Additive-subgroup part is the group case; for $R$-closure compute $f(rm) = r f(m)$.
   - *Why needed:* Without $\ker f \leq M$ there is no quotient $M/\ker f$ to be the source of $\Phi$.

2. **First theorem — import the group theorem.** State that $\Phi(m + \ker f) = f(m)$ is well-defined, bijective onto $\operatorname{im} f$, and additive.
   - *Hint:* Apply the [[Thm - First Isomorphism Theorem (group version)|group first isomorphism theorem]] to the additive homomorphism $f : (M,+) \to (N,+)$; cosets of $\ker f$ are its fibres.
   - *Why needed:* Discharges, for free, every claim about $\Phi$ except $R$-equivariance.

3. **First theorem — $\Phi$ is $R$-equivariant.** Show $\Phi(r(m + \ker f)) = r\Phi(m + \ker f)$.
   - *Hint:* $\Phi(r(m+\ker f)) = \Phi(rm + \ker f) = f(rm) = r f(m)$.
   - *Why needed:* A module isomorphism must respect the action; this is the one module-specific check on the map.

4. **Second theorem.** Define $g : B \to (A+B)/A$ by $g(b) = b + A$; show it is a surjective homomorphism with $\ker g = A \cap B$, then apply the first theorem.
   - *Hint:* Surjective because $a + b + A = b + A$; an element $b$ is in the kernel if and only if $b + A = A$ if and only if $b \in A$, and since $b \in B$ already, if and only if $b \in A \cap B$.
   - *Why needed:* Converts the second theorem into a one-line consequence of the first.

5. **Third theorem.** Define $h : M/N \to M/L$ by $h(m + N) = m + L$; show it is well-defined (because $N \leq L$), surjective, with kernel $L/N$, then apply the first theorem.
   - *Hint:* Well-defined because $m + N = m' + N \implies m - m' \in N \leq L \implies m + L = m' + L$; kernel is $\{m + N : m \in L\} = L/N$.
   - *Why needed:* Converts the third theorem into a one-line consequence of the first.

6. **Submodule correspondence.** Show $L \mapsto L/N$ and $P \mapsto q^{-1}(P)$ (preimage under the quotient map $q : M \to M/N$) are mutually inverse and inclusion-preserving.
   - *Hint:* $q^{-1}(P)$ always contains $\ker q = N$; for $L \supseteq N$, $q^{-1}(L/N) = L$ because $L$ is a union of $N$-cosets.
   - *Why needed:* This is the lattice-level statement accompanying the first theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Kernel and image of a module homomorphism are submodules
> **Statement:** For a module homomorphism $f : M \to N$, the set $\ker f$ is a submodule of $M$ and $\operatorname{im} f$ is a submodule of $N$.
>
> **Hint:** The additive-subgroup parts are the group facts. For $R$-closure compute $f(rm)$ and $r \cdot f(m)$ using $R$-equivariance of $f$.
>
> **Why needed:** It guarantees $M/\ker f$ exists as a module, so the source of $\Phi$ is defined; and that $\operatorname{im} f$ is a module, so the target of $\Phi$ makes sense.
>
> > [!note]- Full proof
> > Since $f$ is in particular a homomorphism of the additive groups $(M,+,0_M) \to (N,+,0_N)$, the set $\ker f$ is an additive subgroup of $M$ and $\operatorname{im} f$ is an additive subgroup of $N$ — these are the group-theory facts, applied verbatim.
> >
> > For $R$-closure of the kernel, let $m \in \ker f$ and $r \in R$. Then
> > $$f(r \cdot m) = r \cdot f(m) = r \cdot 0_N = 0_N,$$
> > using $R$-equivariance of $f$ and that $r \cdot 0_N = 0_N$ in any module (a consequence of the distributive axiom $r \cdot (0 + 0) = r\cdot 0 + r \cdot 0$). So $r \cdot m \in \ker f$, and $\ker f$ is a submodule of $M$.
> >
> > For $R$-closure of the image, let $y \in \operatorname{im} f$ and $r \in R$. Write $y = f(m)$ for some $m \in M$. Then $r \cdot y = r \cdot f(m) = f(r \cdot m) \in \operatorname{im} f$. So $\operatorname{im} f$ is a submodule of $N$.

> [!note]- Lemma 2: The additive part of the first isomorphism is free
> **Statement:** For a module homomorphism $f : M \to N$, the map $\Phi(m + \ker f) = f(m)$ is a well-defined bijection from $M/\ker f$ onto $\operatorname{im} f$ that respects addition.
>
> **Hint:** Apply the first isomorphism theorem for groups to $f : (M,+) \to (N,+)$; nothing here uses the $R$-action.
>
> **Why needed:** It discharges every claim about $\Phi$ except $R$-equivariance, so the module proof reduces to a single extra line.
>
> > [!note]- Full proof
> > Regard $f$ as a homomorphism of additive groups $(M,+,0_M) \to (N,+,0_N)$. The [[Thm - First Isomorphism Theorem (group version)|first isomorphism theorem for groups]] applied to this additive homomorphism states that the assignment $m + \ker f \mapsto f(m)$ is a well-defined group isomorphism from $(M,+)/\ker f$ onto $\operatorname{im} f$. "Well-defined" unpacks as: if $m + \ker f = m' + \ker f$ then $m - m' \in \ker f$, so $f(m) - f(m') = f(m - m') = 0_N$, giving $f(m) = f(m')$. "Group isomorphism" gives bijectivity onto $\operatorname{im} f$ and additivity, $\Phi\big((m + \ker f) + (m' + \ker f)\big) = f(m + m') = f(m) + f(m')$. The additive coset of the quotient module $M/\ker f$ and the additive coset of the quotient group $(M,+)/\ker f$ are literally the same set, so $\Phi$ is exactly that group isomorphism, viewed as a map of the underlying sets of $M/\ker f$ and the submodule $\operatorname{im} f$.

> [!note]- Lemma 3: An additive module-bijection that is $R$-equivariant is a module isomorphism
> **Statement:** Let $\Phi : A \to B$ be a bijection between $R$-modules that respects addition and respects the $R$-action, $\Phi(r \cdot a) = r \cdot \Phi(a)$. Then $\Phi$ is a module isomorphism; in particular $\Phi^{-1}$ is also a module homomorphism.
>
> **Hint:** Transport additivity and equivariance across $\Phi^{-1}$ by writing elements of $B$ as $\Phi$ of elements of $A$.
>
> **Why needed:** It is the final assembly step of the first theorem: once $\Phi$ is shown additive (free, Lemma 2) and $R$-equivariant, this lemma upgrades it to a genuine module isomorphism.
>
> > [!note]- Full proof
> > A module homomorphism that is bijective is by definition a module isomorphism, so it suffices to confirm $\Phi$ is a module homomorphism — which it is, being additive and $R$-equivariant by hypothesis — and that the set-theoretic inverse $\Phi^{-1} : B \to A$ is again a module homomorphism. Take $b_1, b_2 \in B$ and $r \in R$, and write $b_1 = \Phi(a_1)$, $b_2 = \Phi(a_2)$. Since $\Phi$ respects addition, $\Phi(a_1 + a_2) = b_1 + b_2$, so $\Phi^{-1}(b_1 + b_2) = a_1 + a_2 = \Phi^{-1}(b_1) + \Phi^{-1}(b_2)$. Since $\Phi$ respects the action, $\Phi(r \cdot a_1) = r \cdot b_1$, so $\Phi^{-1}(r \cdot b_1) = r \cdot a_1 = r \cdot \Phi^{-1}(b_1)$. So $\Phi^{-1}$ is a module homomorphism and $\Phi$ is a module isomorphism.

> [!note]- Lemma 4: $A + B$ and $A \cap B$ are submodules
> **Statement:** For submodules $A, B \leq M$, both $A + B = \{a + b : a \in A,\ b \in B\}$ and $A \cap B$ are submodules of $M$.
>
> **Hint:** Check the additive-subgroup axioms and $R$-closure for each, using that $A$ and $B$ are themselves submodules.
>
> **Why needed:** The second isomorphism theorem speaks of the modules $(A+B)/A$ and $B/(A \cap B)$; these must be modules for the statement to typecheck.
>
> > [!note]- Full proof
> > **$A + B$.** It is non-empty since $0 = 0 + 0 \in A + B$. If $a + b$ and $a' + b'$ lie in $A + B$ then $(a + b) - (a' + b') = (a - a') + (b - b')$ with $a - a' \in A$ and $b - b' \in B$ (each of $A, B$ is an additive subgroup), so the difference lies in $A + B$ and $A + B$ is an additive subgroup. For $R$-closure, $r \cdot (a + b) = (r \cdot a) + (r \cdot b)$ by the distributive axiom, and $r \cdot a \in A$, $r \cdot b \in B$, so $r \cdot (a + b) \in A + B$.
> >
> > **$A \cap B$.** It contains $0$. If $x, y \in A \cap B$ then $x - y$ lies in $A$ (as $x, y \in A$) and in $B$ (as $x, y \in B$), so $x - y \in A \cap B$. For $R$-closure, if $x \in A \cap B$ then $r \cdot x \in A$ and $r \cdot x \in B$, so $r \cdot x \in A \cap B$.

> [!note]- Lemma 5: The second-theorem map and its kernel
> **Statement:** For submodules $A, B \leq M$, the map $g : B \to (A+B)/A$, $g(b) = b + A$, is a surjective module homomorphism with $\ker g = A \cap B$.
>
> **Hint:** Surjectivity uses $a + b + A = b + A$; the kernel computation uses that $b$ is *already* in $B$.
>
> **Why needed:** Feeding $g$ to the first isomorphism theorem yields the second isomorphism theorem in one line.
>
> > [!note]- Full proof
> > $g$ is the composite of the inclusion $B \hookrightarrow A + B$ and the quotient map $A + B \to (A+B)/A$; both are module homomorphisms, so $g$ is a module homomorphism. (Directly: $g(b + b') = (b + b') + A = (b + A) + (b' + A) = g(b) + g(b')$ and $g(r b) = rb + A = r(b + A) = r\,g(b)$.)
> >
> > **Surjective.** A general element of $(A+B)/A$ is $(a + b) + A$ with $a \in A$, $b \in B$. Since $a \in A$, the coset $(a+b)+A$ equals $b + A = g(b)$. So $g$ hits every element.
> >
> > **Kernel.** $b \in \ker g$ means $g(b) = b + A = A$, the zero coset, which holds if and only if $b \in A$. But $b \in B$ by assumption. Hence $b \in \ker g \iff b \in A \text{ and } b \in B \iff b \in A \cap B$. So $\ker g = A \cap B$.

> [!note]- Lemma 6: The third-theorem map and its kernel
> **Statement:** For submodules $N \leq L \leq M$, the map $h : M/N \to M/L$, $h(m + N) = m + L$, is a well-defined surjective module homomorphism with $\ker h = L/N$.
>
> **Hint:** Well-definedness needs $N \leq L$; the kernel is the set of cosets $m + N$ with $m \in L$.
>
> **Why needed:** Feeding $h$ to the first isomorphism theorem yields the third isomorphism theorem in one line.
>
> > [!note]- Full proof
> > **Well-defined.** Suppose $m + N = m' + N$, i.e. $m - m' \in N$. Since $N \leq L$, also $m - m' \in L$, so $m + L = m' + L$. Thus $h$ does not depend on the choice of representative.
> >
> > **Homomorphism.** $h\big((m+N) + (m'+N)\big) = h\big((m+m') + N\big) = (m + m') + L = (m+L) + (m'+L)$, and $h(r(m+N)) = h(rm + N) = rm + L = r(m + L)$.
> >
> > **Surjective.** Any element of $M/L$ is $m + L = h(m + N)$.
> >
> > **Kernel.** $m + N \in \ker h$ means $m + L = L$, i.e. $m \in L$. So $\ker h = \{m + N : m \in L\}$, which is precisely the image $L/N$ of $L$ under the quotient map $M \to M/N$ — a submodule of $M/N$.

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout, $R$ is a commutative ring and all modules are $R$-modules.
>
> ---
> **First Isomorphism Theorem.** Let $f : M \to N$ be a module homomorphism.
>
> *Step 0 — sub-objects.* By Lemma 1, $\ker f$ is a submodule of $M$ and $\operatorname{im} f$ is a submodule of $N$. In particular the quotient module $M/\ker f$ is defined.
>
> *Step 1 — define the map.* Set
> $$\Phi : M/\ker f \longrightarrow \operatorname{im} f, \qquad \Phi(m + \ker f) = f(m).$$
>
> *Step 2 — well-definedness, bijectivity, additivity are free.* Regard $f$ as a homomorphism of additive groups $(M,+) \to (N,+)$. By the first isomorphism theorem for groups (Lemma 2), $\Phi$ is well-defined, a bijection onto $\operatorname{im} f$, and additive. We do **not** re-prove this — it is exactly the group theorem, and the cosets of $\ker f$ are precisely the fibres of $f$.
>
> *Step 3 — $\Phi$ is $R$-equivariant.* This is the only module-specific check. For $r \in R$ and a coset $m + \ker f$, using the definition of the $R$-action on the quotient module and the $R$-equivariance of $f$,
> $$\Phi\big(r \cdot (m + \ker f)\big) = \Phi(rm + \ker f) = f(rm) = r \cdot f(m) = r \cdot \Phi(m + \ker f).$$
>
> *Step 4 — conclude.* By Steps 2–3, $\Phi$ is a bijection that respects addition and the $R$-action; by Lemma 3 it is a module isomorphism. Hence $M/\ker f \cong \operatorname{im} f$.
>
> ---
> **Second Isomorphism Theorem.** Let $A, B \leq M$. By Lemma 4, $A + B$ and $A \cap B$ are submodules of $M$, so the modules $(A+B)/A$ and $B/(A \cap B)$ are defined. By Lemma 5 the map $g : B \to (A+B)/A$, $g(b) = b + A$, is a surjective module homomorphism with $\ker g = A \cap B$. Applying the First Isomorphism Theorem to $g$:
> $$\frac{B}{\ker g} \;\cong\; \operatorname{im} g \qquad\Longrightarrow\qquad \frac{B}{A \cap B} \;\cong\; \frac{A+B}{A},$$
> using $\ker g = A \cap B$ and $\operatorname{im} g = (A+B)/A$ (surjectivity). $\blacksquare$
>
> ---
> **Third Isomorphism Theorem.** Let $N \leq L \leq M$. By Lemma 6, the map $h : M/N \to M/L$, $h(m + N) = m + L$, is a well-defined surjective module homomorphism with $\ker h = L/N$; in particular $L/N$ is a submodule of $M/N$. Applying the First Isomorphism Theorem to $h$:
> $$\frac{M/N}{\ker h} \;\cong\; \operatorname{im} h \qquad\Longrightarrow\qquad \left.\left(\frac{M}{N}\right)\middle/\left(\frac{L}{N}\right)\right. \;\cong\; \frac{M}{L},$$
> using $\ker h = L/N$ and $\operatorname{im} h = M/L$ (surjectivity). $\blacksquare$
>
> ---
> **Submodule Correspondence.** Let $N \leq M$ and let $q : M \to M/N$ be the quotient map, $q(m) = m + N$, which is a surjective module homomorphism with $\ker q = N$.
>
> Define $\alpha(L) = L/N = q(L)$ for a submodule $L$ with $N \leq L \leq M$, and $\beta(P) = q^{-1}(P) = \{m \in M : m + N \in P\}$ for a submodule $P \leq M/N$.
>
> *$\alpha$ lands in submodules of $M/N$.* If $N \leq L \leq M$ then $q(L)$ is a submodule of $M/N$, being the image of the submodule $L$ under the module homomorphism $q$ (Lemma 1 applied to $q|_L$).
>
> *$\beta$ lands in submodules of $M$ containing $N$.* The preimage $q^{-1}(P)$ of a submodule under a module homomorphism is a submodule (additive-subgroup preimage is a subgroup; and $m \in q^{-1}(P)$, $r \in R \implies q(rm) = r\,q(m) \in P$ so $rm \in q^{-1}(P)$). Moreover $q^{-1}(P)$ contains $\ker q = N$, since $q(N) = \{0\}$ and the zero coset lies in every submodule $P$.
>
> *$\beta \circ \alpha = \operatorname{id}$.* For $N \leq L \leq M$ we must show $q^{-1}(q(L)) = L$. The inclusion $L \subseteq q^{-1}(q(L))$ is automatic. Conversely, if $m \in q^{-1}(q(L))$ then $m + N = \ell + N$ for some $\ell \in L$, so $m - \ell \in N \leq L$, whence $m = \ell + (m - \ell) \in L$. So $q^{-1}(q(L)) = L$.
>
> *$\alpha \circ \beta = \operatorname{id}$.* For $P \leq M/N$ we must show $q(q^{-1}(P)) = P$. Since $q$ is surjective, $q(q^{-1}(P)) = P$ for any subset $P$.
>
> *Inclusion-preserving.* If $L_1 \subseteq L_2$ then $q(L_1) \subseteq q(L_2)$; if $P_1 \subseteq P_2$ then $q^{-1}(P_1) \subseteq q^{-1}(P_2)$. Hence $\alpha$ and $\beta$ are mutually inverse, inclusion-preserving bijections. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Rank–nullity is the first isomorphism theorem.** Take $R = F$ a field, so modules are vector spaces and homomorphisms are linear maps. The first isomorphism theorem gives $V/\ker T \cong \operatorname{im} T$ for a linear map $T : V \to W$. Taking dimensions and using $\dim(V/\ker T) = \dim V - \dim \ker T$ yields $\dim V = \dim \ker T + \dim \operatorname{im} T$ — the rank–nullity theorem. The non-obvious recognition is that a staple of every linear-algebra course is *literally* an isomorphism theorem specialised to vector spaces, with the additive bookkeeping of dimensions standing in for the abstract isomorphism.

**The dimension inclusion–exclusion formula.** For two subspaces $A, B$ of a vector space, the second isomorphism theorem gives $(A+B)/A \cong B/(A \cap B)$. Take dimensions: $\dim(A+B) - \dim A = \dim B - \dim(A \cap B)$, i.e. $\dim(A + B) + \dim(A \cap B) = \dim A + \dim B$. This is non-obvious as an *application of an isomorphism theorem* because the formula is usually proved by extending a basis of $A \cap B$ — yet it falls out instantly from the second theorem plus the fact that dimension is additive on quotients.

**Abelian groups: structure of $\mathbb{Z}$-module quotients.** Since a $\mathbb{Z}$-module is exactly an abelian group, the isomorphism theorems for modules are simultaneously the isomorphism theorems for abelian groups. The third theorem, $(\mathbb{Z}/m\mathbb{Z})/(d\mathbb{Z}/m\mathbb{Z}) \cong \mathbb{Z}/d\mathbb{Z}$ for $d \mid m$, is the engine behind computations in the classification of finite abelian groups. The non-obvious step is recognising that a purely group-theoretic cyclic-quotient computation is an instance of the *module* third isomorphism theorem with $R = \mathbb{Z}$.

**Quotients of function modules.** Let $X$ be a topological space, $A \subseteq X$ a closed subspace, and $M = C(X)$ the module of continuous real-valued functions, regarded as a module over the ring $C(X)$ — or, more simply, over $\mathbb{R}$. Restriction $\rho : C(X) \to C(A)$ is a surjective module homomorphism (when $X$ is, say, normal so restrictions extend) whose kernel is the submodule of functions vanishing on $A$. The first isomorphism theorem identifies $C(X)/\ker\rho \cong C(A)$. This is out-of-distribution because $C(X)$ is infinite-dimensional and analytically defined, yet the purely algebraic isomorphism theorem still pins down the quotient — the disguised source is that restriction respects the $\mathbb{R}$-scaling, so it is a module homomorphism.

---

# Bridges

- **[[Thm - First Isomorphism Theorem (group version)|First Isomorphism Theorem for Groups]]** — the prototype, and literally the engine of the proof here. Applied to the additive group $(M,+)$ it hands over the entire additive content of the module first theorem; the module proof only adds the two $R$-action checks. The module, ring, and group first isomorphism theorems are the *same statement* in three categories — replace "group / normal subgroup / group homomorphism" by "module / submodule / module homomorphism" or by "ring / ideal / ring homomorphism".

- **[[Thm - First Isomorphism Theorem for Rings|First Isomorphism Theorem for Rings]]** — the sibling result. The ring case decorates the group theorem with a *multiplication*; the module case decorates it with an *external action*. Both decorations "come along for free" because the decoration on the quotient is defined on representatives. Comparing the two proofs side by side is the cleanest way to see what "structure-agnostic" means.

- **[[Thm - Finitely Generated Modules and Surjections from a Free Module]]** — the first isomorphism theorem's most-used consequence. Combined with a surjection $R^k \twoheadrightarrow M$ from a [[Def - Free Module|free module]], the first theorem writes any [[Def - Finitely Generated Module|finitely generated]] module as $M \cong R^k/K$ — the basis of [[Def - Finitely Presented Module|finite presentations]] and of the structure theorem for finitely generated modules over a principal ideal domain.

- **[[Thm - Invariance of Rank]]** — a direct application. Invariance of rank is proved by *quotienting* $R^n$ by $IR^n$ for a maximal ideal $I$ and applying the field case of these isomorphism theorems (rank–nullity for vector spaces) to the resulting $(R/I)$-vector space.

- **Submodule Correspondence and the lattice viewpoint** — the correspondence says the quotient map $M \to M/N$ is a lattice isomorphism between the submodules of $M$ above $N$ and *all* submodules of $M/N$. This is the module analogue of the correspondence theorem for groups (normal subgroups above $N$) and for rings (ideals above $I$).

---

# Unlocked by This

> [!tip] Structure Theorem for Finitely Generated Modules over a PID *(from Commutative Algebra)*
> Writing $M \cong R^k/K$ via the first isomorphism theorem, and then using Smith normal form to diagonalise the relation submodule $K$, decomposes any finitely generated module over a principal ideal domain as a direct sum of cyclic modules $R/(d_1) \oplus \dots \oplus R/(d_r) \oplus R^s$. Specialised to $\mathbb{Z}$ this is the classification of finitely generated abelian groups; specialised to $F[X]$ it gives rational and Jordan canonical forms.

> [!tip] Exact Sequences and Homological Algebra *(from Homological Algebra)*
> The first isomorphism theorem is the statement that every module homomorphism $f$ factors as a surjection $M \twoheadrightarrow M/\ker f$ followed by an isomorphism followed by an inclusion $\operatorname{im} f \hookrightarrow N$. Promoting this to the language of short exact sequences $0 \to \ker f \to M \to \operatorname{im} f \to 0$ is the entry point to homological algebra, derived functors, and $\operatorname{Ext}$ and $\operatorname{Tor}$.
