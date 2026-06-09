---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Ring"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Multiplicative Set and Localization"
  - "Def - Local Property (Localizable and Local-to-Global)"
  - "Thm - The Local-Global Principle"
tags: [algebra, commutative-algebra]
---

# Problem Statement

A ring $R$ is [[Def - Radical of an Ideal and the Nilradical|reduced]] if its only nilpotent element is $0$, i.e. $\operatorname{nil} R = (0)$. Prove that **being reduced is a local property of rings**:
$$R \text{ is reduced} \iff R_{\mathfrak{p}} \text{ is reduced for every } \mathfrak{p}\in\operatorname{Spec} R.$$
(This is Example Sheet 2, Q10(e).) Then explain why the analogous statement with "reduced" replaced by "integral domain" is *false* — being a domain is **not** a local property (ES2 Q10(f)).

**Recall:**

![[Def - Radical of an Ideal and the Nilradical#Reduced rings]]

![[Thm - The Local-Global Principle#Statement]]

A ring is [[Def - Radical of an Ideal and the Nilradical|reduced]] iff $\operatorname{nil} R = (0)$, where $\operatorname{nil} R = \{r : r^n = 0\text{ for some } n\}$. Recall the [[Thm - The Local-Global Principle|base lemma]]: an $R$-module $M$ is zero iff $M_{\mathfrak{m}} = 0$ for every maximal ideal $\mathfrak{m}$ (the annihilator argument). And localization commutes with the nilradical: $(\operatorname{nil} R)_{\mathfrak{p}} = \operatorname{nil}(R_{\mathfrak{p}})$.

---

# Convergent Strategy

**Problem class.** This is a *prove-a-property-is-local* problem, the chapter's signature class. Per the [[Commutative Algebra IV — Localization#Problem-Solving Strategy|topic strategy]], such problems split into the easy localizable direction (descent, free from exactness) and the hard local-to-global direction (gluing, powered by "being zero is local"). The twist is that "reduced" is a *ring* property, so we must convert it into a *module* statement — "$\operatorname{nil} R = 0$" — to feed the local–global machinery.

**Assumption pattern.** The recognisable trigger is "reduced $= \operatorname{nil} R = (0)$", which is a *vanishing* statement about the ideal $\operatorname{nil} R$, viewed as a module. The moment a property is phrased as "some canonical module/ideal is zero", the [[Thm - The Local-Global Principle|local–global principle]] applies, because being zero is local. The second key fact is that the nilradical *localizes correctly*: $(\operatorname{nil} R)_{\mathfrak{p}} = \operatorname{nil}(R_{\mathfrak{p}})$, so "the nilradical is zero" can be checked prime by prime.

**Theorem routing.** The route is: reduced $\iff\operatorname{nil} R = (0)$ $\iff(\operatorname{nil} R)_{\mathfrak{p}} = 0$ for all $\mathfrak{p}$ (by the [[Thm - The Local-Global Principle|base lemma]], "being zero is local") $\iff\operatorname{nil}(R_{\mathfrak{p}}) = 0$ for all $\mathfrak{p}$ (since [[Ex - The radical of an extended ideal|localization commutes with the nilradical]]) $\iff R_{\mathfrak{p}}$ reduced for all $\mathfrak{p}$. Every link is a citation; the art is assembling them in the right order.

**Key decision point.** The non-obvious move is *recognising "reduced" as the vanishing of the module $\operatorname{nil} R$*, which is what licenses the module-level local–global principle for a ring property. The natural wrong instinct is to argue elementwise with nilpotents directly; the clean path goes through "$\operatorname{nil} R = 0$ is a local module condition". For the domain counterexample, the decision is to *exhibit a disconnected spectrum* — a product of fields — where every local ring is a domain but the global ring has zero-divisors, because "domain" cannot be the vanishing of any single canonical module.

---

# Legal Operations Used

This solution deploys the following [[Commutative Algebra IV — Localization#Legal Operations|legal operations from the topic page]]:

1. **Operation 4 (reduce a global statement to local rings).** "Reduced" is recast as "$\operatorname{nil} R = 0$", a local property, and checked at each prime.

2. **Operation 5 (test for zero with annihilators).** The base lemma "being zero is local", proved via annihilators, is the engine of the local-to-global direction.

3. **Operation 9 (localization commutes with finite operations).** Specifically $(\operatorname{nil} R)_{\mathfrak{p}} = \operatorname{nil}(R_{\mathfrak{p}})$, identifying the localized nilradical with the nilradical of the localization.

---

# Hints

> [!note]- Hint 1
> "Reduced" is a property of the *whole ring*, but the local–global principle is about *modules being zero*. So rephrase: "$R$ is reduced" means "$\operatorname{nil} R = (0)$", and $\operatorname{nil} R$ is an ideal, hence a module. Now which theorem says a module is zero iff all its localizations are?

> [!note]- Hint 2
> By the base lemma, $\operatorname{nil} R = 0\iff(\operatorname{nil} R)_{\mathfrak{p}} = 0$ for all $\mathfrak{p}$. To finish you need $(\operatorname{nil} R)_{\mathfrak{p}} = \operatorname{nil}(R_{\mathfrak{p}})$ — that localization commutes with taking the nilradical. This is the $I = (0)$ case of $\sqrt{I}^{\,e} = \sqrt{I^e}$.

> [!note]- Hint 3
> For the domain counterexample, you want a ring that is "locally a domain" but globally not. Try $R = \mathbb{C}\times\mathbb{C}$ (or any product of two fields). What are its localizations $R_{\mathfrak{p}}$? Is each a domain? Does $R$ itself have zero-divisors? Why can't "domain" be the vanishing of a canonical module?

---

# Solution

Recast "reduced" as "$\operatorname{nil} R = 0$", a module-vanishing condition, then run the local–global principle: being zero is local, and the nilradical commutes with localization, so the equivalence drops out. For the domain failure, exhibit $\mathbb{C}\times\mathbb{C}$, locally a field but globally not a domain.

**Step 1: "Reduced" is the vanishing of the module $\operatorname{nil} R$.**

$R$ reduced $\iff\operatorname{nil} R = (0)$, and $\operatorname{nil} R$ is an ideal, hence an $R$-module.

> [!note]- Derivation
> By [[Def - Radical of an Ideal and the Nilradical|definition]], $R$ is reduced iff its only nilpotent is $0$, i.e. $\operatorname{nil} R = \{r : r^n = 0\} = (0)$. The nilradical is an ideal of $R$ (closed under addition by the binomial argument, under multiplication by ring elements trivially), so it is an $R$-module, and "reduced" is exactly the statement that this particular module is zero. This is the recasting that unlocks the local–global principle.

**Step 2: Localization commutes with the nilradical.**

$(\operatorname{nil} R)_{\mathfrak{p}} = \operatorname{nil}(R_{\mathfrak{p}})$ for every prime $\mathfrak{p}$.

> [!note]- Derivation
> This is the $I = (0)$ case of [[Ex - The radical of an extended ideal|the radical-of-an-extended-ideal identity]]: with $S = R\setminus\mathfrak{p}$, $(\operatorname{nil} R)_{\mathfrak{p}} = (\sqrt{(0)})^e = \sqrt{(0)^e} = \sqrt{(0)} = \operatorname{nil}(R_{\mathfrak{p}})$. Concretely: a fraction $\tfrac rs\in R_{\mathfrak{p}}$ is nilpotent iff $(\tfrac rs)^n = \tfrac{r^n}{s^n} = 0$ for some $n$, iff $u r^n = 0$ for some $u\in S$, iff $(ur)^n = u^{n-1}\cdot u r^n = 0$, iff $ur\in\operatorname{nil} R$, iff $\tfrac rs = \tfrac{ur}{us}\in(\operatorname{nil} R)_{\mathfrak{p}}$.

**Step 3: Assemble the equivalence via the local–global principle.**

Chain the three facts: reduced $\iff\operatorname{nil} R = 0\iff$ all $(\operatorname{nil} R)_{\mathfrak{p}} = 0\iff$ all $R_{\mathfrak{p}}$ reduced.

> [!note]- Derivation
> $$R\text{ reduced}\overset{\text{Step 1}}{\iff}\operatorname{nil} R = (0)\overset{\text{base lemma}}{\iff}(\operatorname{nil} R)_{\mathfrak{p}} = 0\ \forall\mathfrak{p}\overset{\text{Step 2}}{\iff}\operatorname{nil}(R_{\mathfrak{p}}) = 0\ \forall\mathfrak{p}\iff R_{\mathfrak{p}}\text{ reduced}\ \forall\mathfrak{p}.$$
> The middle equivalence is the [[Thm - The Local-Global Principle|base lemma]] "being zero is a local property" applied to the module $M = \operatorname{nil} R$: $M = 0\iff M_{\mathfrak{p}} = 0$ for all $\mathfrak{p}$ (indeed for all maximal $\mathfrak{m}$). The proof of $\Leftarrow$ there is the annihilator argument. This completes the proof that reduced is local.
>
> Note the two directions in human terms: *localizable* (reduced $\Rightarrow$ locally reduced) is the easy descent — localization adds no nilpotents; *local-to-global* (locally reduced $\Rightarrow$ reduced) is the content — a global nilpotent would have to be detected by some localization, which the annihilator argument guarantees.

**Step 4: Being a domain is NOT local — the counterexample.**

$R = \mathbb{C}\times\mathbb{C}$ has every $R_{\mathfrak{p}}$ a field (hence a domain), yet $R$ is not a domain.

> [!note]- Derivation
> Let $R = \mathbb{C}\times\mathbb{C}$. Its primes are $\mathfrak{p}_1 = \mathbb{C}\times\{0\}$ and $\mathfrak{p}_2 = \{0\}\times\mathbb{C}$ (the ideals of a finite product are products of ideals, prime iff one factor is prime and the rest are the whole ring). Localizing: $R_{\mathfrak{p}_1} = S^{-1}R$ with $S = \mathbb{C}\times(\mathbb{C}\setminus\{0\})$; the map $(x,y)\mapsto y$ inverts $S$ and has kernel $\mathbb{C}\times\{0\}$ killed in the localization (since $(0,1)\in S$ annihilates $(x,0)$), giving $R_{\mathfrak{p}_1}\cong\mathbb{C}$, a field. Similarly $R_{\mathfrak{p}_2}\cong\mathbb{C}$. So *every* $R_{\mathfrak{p}}$ is a domain (indeed a field). But $R$ itself is **not** a domain: $(1,0)(0,1) = (0,0)$ exhibits zero-divisors. Hence "integral domain" fails the local-to-global direction.
>
> The structural reason: "domain" is "no zero-divisors", which is *not* the vanishing of any single canonical module (unlike "$\operatorname{nil} R = 0$"). A disconnected spectrum (here two points) can be locally a domain at each point while globally factoring — the zero-divisors $(1,0), (0,1)$ are the idempotents witnessing the product decomposition, invisible after localizing to one factor. Reducedness survives because it *is* a module-vanishing condition; being a domain does not, because it sees global connectedness.

> [!note]- Complete formal solution
> **Reduced is local.** $R$ is reduced $\iff\operatorname{nil} R = (0)$. The nilradical is a module, and by the base lemma "$M = 0\iff M_{\mathfrak{p}} = 0$ for all $\mathfrak{p}$", $\operatorname{nil} R = 0\iff(\operatorname{nil} R)_{\mathfrak{p}} = 0$ for all $\mathfrak{p}$. Since localization commutes with the nilradical, $(\operatorname{nil} R)_{\mathfrak{p}} = \operatorname{nil}(R_{\mathfrak{p}})$, so this is $\iff\operatorname{nil}(R_{\mathfrak{p}}) = 0$ for all $\mathfrak{p}$ $\iff R_{\mathfrak{p}}$ reduced for all $\mathfrak{p}$. Hence reduced is a local property.
>
> **Domain is not local.** $R = \mathbb{C}\times\mathbb{C}$ has $\operatorname{Spec} R = \{\mathfrak{p}_1, \mathfrak{p}_2\}$ with $R_{\mathfrak{p}_1}\cong R_{\mathfrak{p}_2}\cong\mathbb{C}$, fields, so every localization is a domain; but $(1,0)(0,1) = 0$ shows $R$ is not a domain. So "integral domain" is not local-to-global. $\blacksquare$

---

# Key Takeaways

**To prove a ring property is local, recast it as the vanishing of a canonical module.** The whole proof hinges on rewriting "reduced" as "$\operatorname{nil} R = (0)$", which converts a ring-level statement into the module-level statement the [[Thm - The Local-Global Principle|local–global principle]] is built to handle. This is the universal recipe: a ring property that can be expressed as "some functorial ideal/module is zero" (the nilradical, the conductor, an annihilator, a torsion submodule) is automatically local, because being zero is local and these modules commute with localization. The trigger to recognise: when asked whether a ring property is local, *find the module whose vanishing encodes it*; if you can, locality follows mechanically, and if you cannot, suspect the property is *not* local — which is exactly the situation for "domain".

**The localizable and local-to-global directions fail for genuinely different reasons, and the counterexample exposes the boundary.** Reducedness passes both directions; "domain" passes only the localizable one (a domain localizes to a domain) and *fails* local-to-global. The diagnostic is connectedness of the spectrum: a product $R_1\times R_2$ has a disconnected spectrum, is locally each factor (a domain if the factors are), yet globally has the idempotent zero-divisors $(1,0)(0,1) = 0$. So "domain" sees a *global* feature — irreducibility/connectedness of $\operatorname{Spec} R$ — that no single local ring can detect. The repair (when does "locally a domain" imply "a domain"?) is precisely "$R$ reduced and $\operatorname{Spec} R$ connected", and recognising that *connectedness is the missing ingredient* is the transferable insight: local data glues into a domain exactly when there is no global splitting to obstruct it.

**This is the algebraic seed of "a scheme is reduced iff its stalks are, but irreducibility is global".** Under the structure-sheaf dictionary $R_{\mathfrak{p}} = $ stalk, the result says a scheme is reduced iff all its stalks are reduced — reducedness is checkable pointwise, a genuinely local condition on the structure sheaf. By contrast, *irreducibility* of a scheme (the geometric form of "domain") is a global topological condition: $\operatorname{Spec}(\mathbb{C}\times\mathbb{C})$ is two disjoint points, locally a single reduced point each, but globally disconnected, hence reducible. The lesson transfers across geometry: properties that are vanishing-of-a-sheaf (reduced, flat, the support being empty) are local; properties that are about the *shape* of the space (irreducible, connected, integral) are global and require gluing or connectedness hypotheses — see the parallel failure in [[Ex - Freeness is not a local property]].
