---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Multicategory"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Show that the notion of an ordinary [[Def - Category|category]] is exactly the notion of a [[Def - Multicategory|multicategory]] in which the only non-empty multimap sets are the unary ones. Precisely: prove that giving a multicategory $\mathcal{M}$ with $\mathcal{M}(a_1, \dots, a_n; b) = \varnothing$ whenever $n \neq 1$ is the same as giving a category, and that under this correspondence multicategory functors restrict to ordinary functors. Then identify, for a general multicategory, the *unary part* $\mathcal{M}_1$ (objects of $\mathcal{M}$, with $\mathcal{M}_1(a,b) = \mathcal{M}(a; b)$) and prove it is always an ordinary category.

**Recall:**

![[Def - Multicategory#The Definition]]

A [[Def - Category|category]] $\mathcal{C}$ consists of objects, a hom-set $\mathrm{Hom}_{\mathcal{C}}(a,b)$ for each ordered pair, an identity $1_a \in \mathrm{Hom}_{\mathcal{C}}(a,a)$, and an associative unital composition $\mathrm{Hom}_{\mathcal{C}}(b,c) \times \mathrm{Hom}_{\mathcal{C}}(a,b) \to \mathrm{Hom}_{\mathcal{C}}(a,c)$.

---

# Convergent Strategy

**Problem class:** This is a *definitional comparison* — show two definitions present the same objects by exhibiting a bijection of data that carries axioms to axioms. The general method, used throughout this chapter, is to write out both definitions as "data plus axioms" and match them piece by piece, checking that the matching is reversible.

**Assumption pattern:** The assumption "$\mathcal{M}(a_1, \dots, a_n; b) = \varnothing$ for $n \neq 1$" collapses the entire multimap structure to its arity-$1$ layer. This is the recognisable signal that all the multi-input machinery (substitution of several inputs, the $S_n$-action for $n \neq 1$) becomes trivial or vacuous, leaving exactly the unary composition — which is ordinary composition.

**Theorem routing:** No external theorem is needed; the route is internal to the [[Def - Multicategory|multicategory]] axioms. Specialise the substitution composition to the case $k = 1$ (one outer multimap) with a single unary inner multimap, and to the case where the outer is unary; the multicategory associativity and unit axioms become precisely the category associativity and unit axioms. The $S_1 = \{1\}$ action is trivial, so symmetry contributes nothing.

**Key decision point:** The non-obvious choice is realising that the *general* multicategory still contains a category inside it — the unary part $\mathcal{M}_1$ — even when higher multimaps are present. One must check that substitution restricted to unary multimaps is closed (a unary into a unary gives a unary, since $1 + \dots + 1$ with one summand is $1$) and inherits associativity and unitality. The temptation is to think the unary part interacts with the higher parts in a way that breaks the category axioms; it does not, because substituting unary into unary never leaves arity $1$.

---

# Legal Operations Used

1. **Specialise the substitution composition to fixed arities (operation 3 from the topic page).** We restrict the general composition $\theta \circ (\varphi_1, \dots, \varphi_k)$ to the cases that produce unary outputs, reading off ordinary composition.

2. **Read an operad/multicategory axiom at a chosen arity (operation 5 from the topic page).** We instantiate the associativity and unit axioms at $k = 1$, $n_1 = 1$ to extract the category axioms.

---

# Hints

> [!note]- Hint 1
> What is the arity of a substitution $\theta \circ (\varphi)$ when $\theta$ has arity $1$ and $\varphi$ has arity $1$? Compute $n_1 + \dots + n_k$ in this case and see that the result is again unary.

> [!note]- Hint 2
> The category composition $g \circ f$ should be the multicategory substitution of the unary $g$ into the (single, unary) input of... no — be careful about order. Identify $\mathrm{Hom}(b,c) \times \mathrm{Hom}(a,b) \to \mathrm{Hom}(a,c)$ with $\mathcal{M}(b;c) \times \mathcal{M}(a;b) \to \mathcal{M}(a;c)$ via $(\theta, \varphi) \mapsto \theta \circ (\varphi)$.

> [!note]- Hint 3
> For the converse (a category gives such a multicategory), define $\mathcal{M}(a;b) = \mathrm{Hom}(a,b)$ and *declare* $\mathcal{M}(a_1, \dots, a_n; b) = \varnothing$ for $n \neq 1$. All higher substitutions are vacuous (their input sets are empty), so the higher axioms hold trivially.

---

# Solution

The proof has two directions plus the unary-part construction. We build the multicategory-from-category map, the category-from-multicategory map, check they are mutually inverse on data and that axioms transport, and finally observe the unary part of any multicategory is a category.

**Step 1: A category yields a "unary-only" multicategory.**

> [!note]- Derivation
> Let $\mathcal{C}$ be a [[Def - Category|category]]. Define a multicategory $\mathcal{M}$ with the same objects, $\mathcal{M}(a;b) = \mathrm{Hom}_{\mathcal{C}}(a,b)$, and $\mathcal{M}(a_1, \dots, a_n; b) = \varnothing$ for $n \neq 1$. The identity multimap $1_a \in \mathcal{M}(a;a)$ is the categorical identity. Substitution: the only non-vacuous composites have all multimaps unary, and substituting a unary $\varphi \in \mathcal{M}(a;b)$ into the single input of a unary $\theta \in \mathcal{M}(b;c)$ gives $\theta \circ (\varphi) \in \mathcal{M}(a;c)$ — define this to be the categorical composite $\theta \circ \varphi$. Every other substitution has at least one empty factor, so its domain is empty and there is nothing to define. The $S_n$-actions are on empty sets for $n \neq 1$ and trivial for $n = 1$. The multicategory associativity and unit axioms, restricted to the only non-vacuous case (all unary), are exactly the category associativity and unit axioms, which hold in $\mathcal{C}$. So $\mathcal{M}$ is a multicategory.

**Step 2: A unary-only multicategory yields a category.**

> [!note]- Derivation
> Conversely let $\mathcal{M}$ be a multicategory with $\mathcal{M}(a_1, \dots, a_n; b) = \varnothing$ for $n \neq 1$. Define a category $\mathcal{C}$ with the same objects, $\mathrm{Hom}_{\mathcal{C}}(a,b) = \mathcal{M}(a;b)$, identity $1_a$, and composition $\theta \circ \varphi := \theta \circ (\varphi)$ (substitution of the unary $\varphi$ into the unary $\theta$). This composite has arity $n_1 = 1$, so it lands in a unary set, as required. Associativity: the multicategory associativity axiom, applied to three unary multimaps $\theta \circ (\varphi \circ (\psi))$, reads $\theta \circ (\varphi) \circ (\psi) = \theta \circ (\varphi \circ (\psi))$, which is $(\theta \circ \varphi) \circ \psi = \theta \circ (\varphi \circ \psi)$. Unitality: $1_b \circ (\theta) = \theta$ and $\theta \circ (1_a) = \theta$ are the multicategory unit axioms. So $\mathcal{C}$ is a category.

**Step 3: The two constructions are mutually inverse, and functors correspond.**

> [!note]- Derivation
> Starting from $\mathcal{C}$, building $\mathcal{M}$, then building a category back, returns $\mathrm{Hom}_{\mathcal{C}}(a,b) = \mathcal{M}(a;b)$ with the same composition — the original $\mathcal{C}$. Starting from a unary-only $\mathcal{M}$, the round trip returns the same multimap sets (unary ones unchanged, higher ones empty) and the same substitution. So the constructions are mutually inverse bijections on objects of the two definitions. A [[Def - Multicategory|functor of multicategories]] $F : \mathcal{M} \to \mathcal{N}$ between unary-only multicategories assigns objects to objects and unary multimaps to unary multimaps preserving identities and substitution — exactly an ordinary functor between the corresponding categories. Hence categories and unary-only multicategories are *the same notion*, functors included.

**Step 4: The unary part of any multicategory is a category.**

> [!note]- Derivation
> For an arbitrary multicategory $\mathcal{M}$, define $\mathcal{M}_1$ with the same objects and $\mathcal{M}_1(a,b) = \mathcal{M}(a;b)$. Substitution of a unary into a unary stays unary ($n_1 = 1$), so composition is closed in $\mathcal{M}_1$. The associativity and unit axioms of $\mathcal{M}$, read on unary multimaps only, give associativity and unitality in $\mathcal{M}_1$ — the presence of higher multimaps is irrelevant, because composing unary with unary never produces or consumes a higher multimap. Therefore $\mathcal{M}_1$ is a category, the *underlying category* of the multicategory.

> [!note]- Complete formal solution
> **Claim.** Categories are exactly unary-only multicategories, and every multicategory has an underlying category $\mathcal{M}_1$.
>
> *Category $\to$ unary-only multicategory.* Given $\mathcal{C}$, set $\mathcal{M}(a;b) = \mathrm{Hom}_{\mathcal{C}}(a,b)$, $\mathcal{M}(a_1,\dots,a_n;b) = \varnothing$ for $n \neq 1$, identities and unary substitution from $\mathcal{C}$'s composition, all higher substitutions vacuous, trivial symmetric actions. The multicategory axioms reduce to the only non-vacuous instances — three composable unary multimaps — which are $\mathcal{C}$'s associativity and unit laws.
>
> *Unary-only multicategory $\to$ category.* Given such $\mathcal{M}$, set $\mathrm{Hom}_{\mathcal{C}}(a,b) = \mathcal{M}(a;b)$ with $\theta \circ \varphi = \theta \circ (\varphi)$; the substitution lands in a unary set since $n_1 = 1$. Associativity and unitality come from the multicategory associativity and unit axioms restricted to unary multimaps.
>
> *Inverse and functoriality.* The two constructions are mutually inverse on data, and a multicategory functor between unary-only multicategories is precisely an ordinary functor. Hence the notions coincide.
>
> *Underlying category.* For any multicategory $\mathcal{M}$, the unary multimaps $\mathcal{M}_1(a,b) = \mathcal{M}(a;b)$ with substitution form a category, since unary-into-unary substitution is closed and inherits the associativity and unit laws. $\blacksquare$

---

# Key Takeaways

**Linear is the arity-one slice of multilinear.** The deep content of this exercise is that ordinary category theory sits inside multicategory theory exactly as functions sit inside multilinear maps: it is the layer where every operation eats one input. Whenever you meet a structure that "remembers operations of several inputs", you should expect an underlying ordinary category hiding in its unary part, and you should expect that ordinary category theory is recovered by forcibly emptying all the higher layers. This is the trigger pattern: when a richer structure has an "arity" or "number of inputs" grading, look for the arity-one slice — it is almost always a category, and it is the bridge back to familiar ground.

**Vacuous axioms do real work.** A surprising amount of the proof is the observation that higher substitutions are *vacuous* (their domains are empty) and therefore satisfy every axiom for free. This is a recurring and underrated move: to verify a structure satisfies an axiom scheme, identify which instances have empty domain and discharge them immediately, concentrating effort on the non-vacuous instances. The same logic shows that any "concentrated in one degree" object trivially satisfies coherence conditions involving the absent degrees — a technique that reappears when checking that the unit symmetric sequence $I$ (concentrated in arity $1$) satisfies the unit laws for the composition product.

**Closure under composition is a degree-counting fact.** The reason the unary part of any multicategory is closed under composition is purely arithmetic: substituting a single arity-$1$ multimap into the one slot of an arity-$1$ multimap gives total arity $1 + \dots + 1 = 1$ (one summand). This degree-counting check — "does composing these arities stay in the subclass I care about?" — is the first thing to verify whenever you carve out a sub-multicategory or sub-operad by an arity condition, and it is exactly the check that fails for, say, "the arity-$2$ part", which is not closed because $2 \cdot 2 = 4 \neq 2$. The lesson generalises to the operad setting: the unary operations $P(1)$ of any [[Def - Operad|operad]] always form a monoid, for the same one-summand reason.
