---
type: definition
subject: category-theory
prereqs:
  - "Def - Adjunction"
  - "Def - Unit and Counit of an Adjunction"
  - "Def - Subcategory"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{D} \hookrightarrow \mathcal{C}$ is a **full** [[Def - Subcategory|subcategory]]: $\mathcal{D}$ contains some of the objects of $\mathcal{C}$ and *all* morphisms between them, so $\mathcal{D}(X, Y) = \mathcal{C}(X, Y)$ for objects $X, Y \in \mathcal{D}$. We write $\iota : \mathcal{D} \hookrightarrow \mathcal{C}$ for the inclusion functor. A **reflector** is a left adjoint $L : \mathcal{C} \to \mathcal{D}$ to $\iota$, so $L \dashv \iota$ (see [[Def - Adjunction]]); we often drop $\iota$ and write $L : \mathcal{C} \to \mathcal{C}$ landing in $\mathcal{D}$. The unit $\eta_A : A \to \iota L A$ is the **reflection** of $A$, written informally $A \to LA$. The full symbol registry is on [[Category Theory IV — Adjunctions]].

---

# Axiom Motivation

The motivating phenomenon is *best approximation*. You have a big category $\mathcal{C}$ and a nicer sub-collection $\mathcal{D}$ of objects — abelian groups inside all groups, complete metric spaces inside all metric spaces, sheaves inside presheaves — and you want, for each object $A \in \mathcal{C}$, the **best $\mathcal{D}$-approximation of $A$**. "Best" should mean: the closest object of $\mathcal{D}$ to $A$, in the sense that maps from $A$ to anything in $\mathcal{D}$ are *the same as* maps from the approximation. The definition of a reflective subcategory is the distillation of "best approximation by an object of $\mathcal{D}$".

Make "best approximation" precise. We want, for each $A$, an object $LA \in \mathcal{D}$ and a map $\eta_A : A \to LA$ with the universal property:

> every map $f : A \to X$ to an object $X \in \mathcal{D}$ factors *uniquely* through $\eta_A$, as $f = \overline{f}\circ\eta_A$ for a unique $\overline{f} : LA \to X$ in $\mathcal{D}$.

This says $LA$ is the universal $\mathcal{D}$-object receiving a map from $A$ — nothing in $\mathcal{D}$ is "between" $A$ and $LA$. Now compress: "$\mathcal{D}(LA, X) \cong \mathcal{C}(A, X)$ naturally for $X \in \mathcal{D}$" is exactly the statement that $L$ is **left adjoint** to the inclusion $\iota$. So a best-approximation operation is precisely a left adjoint to a full inclusion, and the universal map $\eta_A$ is the adjunction unit. **A reflective subcategory is a subcategory in which every object of the ambient category has a best approximation, functorially.**

Why must the subcategory be **full**? Because we want the approximation to be measured by *all* the maps between $\mathcal{D}$-objects, not an arbitrary chosen subset. If $\mathcal{D}$ were a non-full subcategory, the hom-sets $\mathcal{D}(LA, X)$ would be smaller than $\mathcal{C}(LA, X)$, and the universal property would compare $A$ against an impoverished notion of "maps in $\mathcal{D}$" — the reflection would no longer be the genuine best approximation. Fullness guarantees that "a map in $\mathcal{D}$" and "a map in $\mathcal{C}$ between $\mathcal{D}$-objects" coincide, which is what makes the reflector's universal property the right one. Concretely, drop fullness and the abelianisation would no longer satisfy "every homomorphism to an abelian group factors through it", because some homomorphisms to abelian groups would have been excluded from $\mathcal{D}$.

What is special about the **counit** here? For a reflective subcategory the counit $\varepsilon_X : L\iota X \to X$ (for $X \in \mathcal{D}$) is an **isomorphism**. This is forced by fullness: an object already in $\mathcal{D}$ is its own best approximation, so $L\iota X \cong X$. Indeed, "the counit is an isomorphism" is an equivalent characterisation of reflectivity (given that $\iota$ is fully faithful, $L \dashv \iota$ has invertible counit iff $\iota$ is full). What breaks if the counit fails to be an isomorphism? Then applying the reflector to an object that was *already* nice would change it — abelianising an abelian group would not give it back — and the operation would not deserve to be called "force into $\mathcal{D}$". The isomorphic counit is the precise statement that $\mathcal{D}$ is closed under the reflection and that the reflection is idempotent: $L(LA) \cong LA$.

The dual notion, where the inclusion has a *right* adjoint (a **coreflector**), is a **coreflective subcategory**; it gives best approximation *from the other side* (e.g. the torsion subgroup, the largest subobject lying in $\mathcal{D}$). The two are related by duality and one rarely needs both at once.

---

# The Definition

A full [[Def - Subcategory|subcategory]] $\iota : \mathcal{D} \hookrightarrow \mathcal{C}$ is **reflective** if the inclusion $\iota$ has a left adjoint $L : \mathcal{C} \to \mathcal{D}$, called the **reflector**:
$$\mathcal{D}(LA, X) \;\cong\; \mathcal{C}(A, \iota X) \qquad \text{naturally in } A \in \mathcal{C},\ X \in \mathcal{D}.$$
The unit component $\eta_A : A \to \iota L A$ is the **reflection** of $A$ into $\mathcal{D}$; it is the [[Def - Universal Property and Universal Arrow|universal arrow]] from $A$ to $\iota$. Equivalently, $\mathcal{D}$ is reflective when, for every $A \in \mathcal{C}$, there is an object $LA \in \mathcal{D}$ and a map $\eta_A : A \to LA$ such that every map $A \to X$ with $X \in \mathcal{D}$ factors uniquely through $\eta_A$.

Because $\iota$ is fully faithful, $L \dashv \iota$ has **counit an isomorphism**: $\varepsilon_X : L\iota X \xrightarrow{\cong} X$ for all $X \in \mathcal{D}$. The composite $\iota L : \mathcal{C} \to \mathcal{C}$ is an **idempotent monad** ($\iota L \iota L \cong \iota L$), and reflective subcategories correspond exactly to idempotent monads on $\mathcal{C}$; this is why a reflector is also called a **localization**.

Dually, $\mathcal{D}$ is **coreflective** if $\iota$ has a *right* adjoint (a coreflector).

---

# Categorical / Structural Definition

A reflective subcategory is the categorical packaging of a **localization**: the reflector inverts a class of morphisms. Precisely, $\iota L$ is an idempotent monad, and the objects of $\mathcal{D}$ are exactly the **local objects** — those $X$ for which the unit $\eta_X$ is already an isomorphism. The reflection $\eta_A : A \to LA$ is the universal map inverting the class of morphisms that $L$ sends to isomorphisms. This is the same idea as inverting a multiplicative set in a ring (see [[Thm - Universal Property of Localization|the universal property of localization]]): $S^{-1}R$ is the reflection of $R$ into the subcategory of rings where the elements of $S$ are units, and "$R \to S^{-1}R$ is universal among ring maps sending $S$ to units" is exactly the reflector's universal property.

Two structural facts follow purely formally and are the reason reflectivity is worth recognising:

- **$\mathcal{D}$ is closed under limits taken in $\mathcal{C}$.** A reflective subcategory inherits all limits from the ambient category: if a diagram in $\mathcal{D}$ has a limit in $\mathcal{C}$, that limit lies in $\mathcal{D}$. (The inclusion is a right adjoint, hence preserves limits by [[Thm - Right Adjoints Preserve Limits|RAPL]], and reflectivity lets one show the limit is computed in $\mathcal{D}$.)
- **Colimits in $\mathcal{D}$ are computed by reflecting the ambient colimit.** The colimit of a diagram in $\mathcal{D}$ is $L$ applied to the colimit computed in $\mathcal{C}$, because the reflector $L$, being a left adjoint, preserves colimits ([[Thm - Right Adjoints Preserve Limits|LAPC]]).

---

# Relate to Other Fields / Compression

Reflective subcategories are the home of every "**-ification**" in mathematics: abelian*ization*, complet*ion*, sheaf*ification*, group completion, sober*ification* of a space, the Stone–Čech compactification (compact Hausdorff spaces are reflective). Each takes an object and produces the universal nicer object receiving a map from it. The recurring shape — "left adjoint to a full inclusion, with isomorphic counit" — is what unifies them; once you see it, the universal property and the (co)limit behaviour are automatic.

In order theory, a reflective subcategory of a poset is a **closure operator**: a monotone, inflationary, idempotent map $c$ with $c(c(a)) = c(a)$ and $a \leq c(a)$, whose image (the closed elements) is the reflective sub-poset. Topological closure, the closure of a set under an operation, and the convex hull are all closure operators, hence reflectors.

**True name:** *a reflective subcategory is a best-approximation operation — a left adjoint to a full inclusion whose unit is the universal map into the subcategory and whose counit is an isomorphism.* When you meet an "-ification", the questions to ask are: what is the unit (the universal map), and is the counit an isomorphism (is the operation idempotent on already-nice objects)? If yes to both, you have a reflective subcategory and all its free theorems.

---

# Examples / Corollaries

**Is an instance — abelian groups in groups.** $\mathbf{Ab} \hookrightarrow \mathbf{Grp}$ is reflective; the reflector is the [[Def - Abelian Group|abelianisation]] $G \mapsto G^{ab} = G/[G,G]$, the quotient by the commutator subgroup. The unit $\eta_G : G \to G/[G,G]$ is the quotient map, universal among homomorphisms from $G$ to abelian groups. The counit is an isomorphism: an abelian group is already its own abelianisation. (See [[Ex - Abelianization is left adjoint to inclusion]].) The analogous reflector $\mathbf{CRing} \hookrightarrow \mathbf{Ring}$ quotients a ring by the ideal generated by commutators $xy - yx$.

**Is an instance — complete metric spaces in metric spaces.** The full subcategory of complete metric spaces (with uniformly continuous maps) is reflective; the reflector is **completion** $X \mapsto \widehat{X}$, with unit the dense isometric embedding $X \to \widehat{X}$. Every uniformly continuous map from $X$ to a complete space extends uniquely to $\widehat{X}$ — the universal property of completion is the reflector's universal property.

**Is an instance — sheaves in presheaves (sheafification).** The category of sheaves on a space is a reflective subcategory of presheaves, with reflector **sheafification** $\mathcal{F} \mapsto \mathcal{F}^+$; the unit $\mathcal{F} \to \mathcal{F}^+$ is universal among maps to sheaves. Sheafification is "the universal way to force the gluing axiom". (See [[Ex - Sheafification as a reflective localization]] and the algebraic-geometry callout on [[Category Theory IV — Adjunctions]].)

**Is an instance — torsion-free abelian groups in abelian groups.** $\mathbf{Ab}_{tf} \hookrightarrow \mathbf{Ab}$ is reflective; the reflector quotients an abelian group by its torsion subgroup, $A \mapsto A/A_{\mathrm{tors}}$, universal among maps to torsion-free groups.

**Is NOT an instance — finite groups in groups.** The full subcategory of finite groups is *not* reflective in $\mathbf{Grp}$. There is no "best finite approximation" of an infinite group $G$ that is universal: maps from $\mathbb{Z}$ to finite groups (its finite quotients) do not factor through a single universal finite quotient, since $\mathbb{Z}$ surjects onto every cyclic group $\mathbb{Z}/n$ and there is no terminal one. The would-be reflector does not exist because the relevant colimit/limit of finite quotients leaves the subcategory.

**Is NOT an instance — a non-full subcategory.** Take $\mathcal{C} = \mathbf{Set}$ and let $\mathcal{D}$ be the subcategory with all sets but only the *injective* functions. This is a (non-full) subcategory, and the inclusion has no left adjoint of the reflective kind — fullness fails, so the universal property that defines a reflector cannot even be stated correctly. Reflectivity *requires* fullness.

**Corollary — reflective subcategories are closed under limits.** Any limit of $\mathcal{D}$-objects computed in $\mathcal{C}$ lands in $\mathcal{D}$. So a product of sheaves is a sheaf, a product of complete spaces is complete, a product of abelian groups is abelian.

**Corollary — the reflector is idempotent.** $L(LA) \cong LA$, because $LA \in \mathcal{D}$ and the counit is an isomorphism. Abelianising twice is abelianising once; completing a complete space changes nothing.

**Calibration check.** Verify the abelianisation unit $G \to G/[G,G]$ is universal by checking that any homomorphism $G \to A$ to an abelian group kills $[G,G]$. Confirm the counit of the completion reflector is an isomorphism on complete spaces. Explain in one sentence why "$\mathcal{D}$ closed under limits" follows from the inclusion being a right adjoint.

---

# Unlocked by This

> [!tip] Sheafification, Schemes, and Topoi *(from Algebraic Geometry / Topos Theory)*
> Sheaves-in-presheaves is the prototype of a reflective localization. The **structure sheaf** of a **scheme** is built this way, and the abstract pattern — a left-exact reflective localization of a presheaf category — *is* the definition of a **Grothendieck topos**. The reflector (sheafification) being left-exact is the extra condition that distinguishes topoi from arbitrary reflective subcategories.

> [!tip] Localization of Categories and Model Categories *(from Homotopy Theory — Cluster 8)*
> Inverting a class of morphisms — the reflector viewpoint — is the operation behind the **localization of a category** and behind the **homotopy category** of a model category, where one inverts the weak equivalences. **Bousfield localization** is a reflective localization at the level of model/$\infty$-categories. See Chapter VI.

> [!tip] Idempotent Monads and Modalities *(from Type Theory / Modal Homotopy Type Theory)*
> A reflective subcategory is the same data as an **idempotent monad** (a "modality"). In **homotopy type theory** these are the *modal* type formers (truncation, localization at a map), and they are how one builds the cohesive and differential refinements of the theory.
