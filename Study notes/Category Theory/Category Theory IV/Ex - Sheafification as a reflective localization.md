---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Reflective Subcategory"
  - "Def - Adjunction"
  - "Def - Presheaf"
tags: [category-theory, foundations]
---

# Problem Statement

> [!note]- Algebraic geometry background
> A **presheaf of sets** on a topological space $X$ assigns to each open set $U\subseteq X$ a set $\mathcal{F}(U)$ (its **sections** over $U$ — picture "functions recordable on $U$") and to each inclusion $V\subseteq U$ a **restriction map** $\mathrm{res}^U_V : \mathcal{F}(U)\to\mathcal{F}(V)$, with $\mathrm{res}^U_U = \mathrm{id}$ and $\mathrm{res}^V_W\circ\mathrm{res}^U_V = \mathrm{res}^U_W$. Equivalently it is a [[Def - Functor|contravariant functor]] $\mathcal{F} : \mathrm{Open}(X)^{op}\to\mathbf{Set}$ on the poset of opens. A presheaf is a **sheaf** if it satisfies the **gluing axiom**: for every open cover $U = \bigcup_i U_i$ and every family of sections $s_i\in\mathcal{F}(U_i)$ that **agree on overlaps** ($s_i|_{U_i\cap U_j} = s_j|_{U_i\cap U_j}$), there is a *unique* $s\in\mathcal{F}(U)$ with $s|_{U_i} = s_i$ for all $i$. (Continuous functions form a sheaf; bounded functions do not, since boundedness does not glue.) Write $\mathbf{PSh}(X)$ for presheaves and $\mathbf{Sh}(X)\hookrightarrow\mathbf{PSh}(X)$ for the full subcategory of sheaves.

Assume (as is standard) that the inclusion $\iota : \mathbf{Sh}(X)\hookrightarrow\mathbf{PSh}(X)$ admits a left adjoint $(-)^+ : \mathbf{PSh}(X)\to\mathbf{Sh}(X)$, **sheafification**, with unit $\theta_{\mathcal{F}} : \mathcal{F}\to\mathcal{F}^+$.

**(a)** State precisely what it means for $\mathbf{Sh}(X)$ to be a reflective subcategory of $\mathbf{PSh}(X)$, and write the adjunction bijection.

**(b)** Explain why sheafification is "the universal way to force the gluing axiom", and why the counit is an isomorphism.

**(c)** Use the reflectivity to deduce: limits of sheaves are computed as in presheaves (objectwise), but colimits of sheaves are the sheafification of the objectwise presheaf colimit.

**Recall:**

A [[Def - Reflective Subcategory|reflective subcategory]] is a full subcategory whose inclusion has a left adjoint (the reflector); the unit is the universal map into the subcategory, and the counit is an isomorphism. A [[Def - Presheaf|presheaf]] (general sense) is a functor $\mathcal{C}^{op}\to\mathbf{Set}$.

---

# Convergent Strategy

**Problem class:** This is a "recognise an -ification as a reflective localization, then harvest the (co)limit consequences" problem (⭐⭐⭐). The AG content is self-contained in the callout; the categorical content is the reflective-subcategory pattern of [[Ex - Abelianization is left adjoint to inclusion|abelianisation]], now with the forced property being the gluing axiom.

**Assumption pattern:** The decisive structural facts: sheaves form a *full* subcategory of presheaves (a map of sheaves is just a map of presheaves), and sheafification is *left adjoint* to the inclusion with unit $\theta_{\mathcal{F}} : \mathcal{F}\to\mathcal{F}^+$. The unit being universal among maps to sheaves is "force the gluing axiom universally"; the counit being an isomorphism is "a sheaf is already its own sheafification".

**Theorem routing:** State the reflector bijection (part a). Interpret the unit's universal property as "best sheaf approximation" and use fullness $+$ the universal property to get the counit isomorphism (part b). Apply [[Thm - Right Adjoints Preserve Limits|RAPL]] to the inclusion (a right adjoint preserves limits, so sheaf limits $=$ presheaf limits) and LAPC to the reflector (a left adjoint preserves colimits, so sheaf colimits $=$ sheafified presheaf colimits) (part c).

**Key decision point:** The non-obvious step is part (c)'s asymmetry: *limits* of sheaves are objectwise (computed in presheaves) but *colimits* are not — you must sheafify. The reason is handedness: the inclusion is a right adjoint (preserves limits), the reflector is a left adjoint (preserves colimits), so the colimit must be transported by the reflector $(-)^+$. Forgetting to sheafify a colimit of sheaves is the standard error.

---

# Legal Operations Used

1. **Operation 8 from the topic page (identify a reflector to import localization theorems).** Sheafification is recognised as the reflector of $\mathbf{Sh}(X)\hookrightarrow\mathbf{PSh}(X)$.

2. **Operation 4 from the topic page (apply RAPL/LAPC to transport (co)limits).** Part (c) uses preservation of limits by the inclusion and of colimits by the reflector.

3. **Operation 1 from the topic page (transpose across the adjunction).** The universal factorization of a presheaf map through $\theta_{\mathcal{F}}$ is the adjunction transpose.

---

# Hints

> [!note]- Hint 1
> Reflective means: $\iota$ is a full inclusion with a left adjoint $(-)^+$. The bijection is $\mathbf{Sh}(X)(\mathcal{F}^+, \mathcal{G})\cong\mathbf{PSh}(X)(\mathcal{F}, \iota\mathcal{G})$ for a sheaf $\mathcal{G}$.

> [!note]- Hint 2
> The unit $\theta_{\mathcal{F}} : \mathcal{F}\to\mathcal{F}^+$ being universal means: any map from $\mathcal{F}$ to a sheaf factors uniquely through $\mathcal{F}^+$. So $\mathcal{F}^+$ is the closest sheaf to $\mathcal{F}$ — the universal target forcing the gluing axiom. For the counit: a sheaf $\mathcal{G}$ already satisfies gluing, so $\mathcal{G}^+\cong\mathcal{G}$.

> [!note]- Hint 3
> For (c): the inclusion $\iota$ is a *right* adjoint, so by RAPL it preserves limits — a limit of sheaves, computed in presheaves (objectwise), is already a sheaf. The reflector $(-)^+$ is a *left* adjoint, so by LAPC it preserves colimits — the colimit of sheaves is $(-)^+$ applied to the presheaf (objectwise) colimit.

---

# Solution

Sheafification is the reflector of the full inclusion of sheaves into presheaves. Its unit is the universal map forcing gluing; its counit is an isomorphism because sheaves already glue. Limits of sheaves are objectwise (the inclusion preserves them); colimits are sheafified objectwise colimits (the reflector preserves them).

**Step 1: Reflectivity and the bijection (part a).**

$\mathbf{Sh}(X)$ is reflective in $\mathbf{PSh}(X)$: $\iota$ is full and has the left adjoint $(-)^+$, with
$$\mathbf{Sh}(X)(\mathcal{F}^+, \mathcal{G})\;\cong\;\mathbf{PSh}(X)(\mathcal{F}, \iota\mathcal{G}), \qquad \mathcal{G}\in\mathbf{Sh}(X).$$

> [!note]- Derivation
> "Reflective" means the inclusion of a full subcategory has a left adjoint. The subcategory $\mathbf{Sh}(X)\hookrightarrow\mathbf{PSh}(X)$ is full: a morphism of sheaves is precisely a morphism of the underlying presheaves (a natural transformation of the functors). The left adjoint is sheafification $(-)^+$, so the adjunction bijection is as displayed, natural in $\mathcal{F}$ and $\mathcal{G}$. The unit is $\theta_{\mathcal{F}} : \mathcal{F}\to\mathcal{F}^+ = \iota(\mathcal{F}^+)$.

**Step 2: Universal forcing of gluing; counit iso (part b).**

> [!note]- Derivation
> The unit's universal property reads: for every sheaf $\mathcal{G}$ and every presheaf morphism $\phi : \mathcal{F}\to\iota\mathcal{G}$, there is a *unique* sheaf morphism $\overline{\phi} : \mathcal{F}^+\to\mathcal{G}$ with $\overline{\phi}\circ\theta_{\mathcal{F}} = \phi$. In words: *any* attempt to map the presheaf $\mathcal{F}$ into something satisfying the gluing axiom factors through $\mathcal{F}^+$. So $\mathcal{F}^+$ is the universal — closest, minimal-change — sheaf receiving a map from $\mathcal{F}$: it is "the best sheaf approximation", obtained by forcing exactly the gluing axiom and nothing more. Sections of $\mathcal{F}^+$ over $U$ are families of *compatible germs* — the universal repair that makes local-compatible data glue.
>
> **Counit isomorphism.** For a sheaf $\mathcal{G}$, the counit $\varepsilon_{\mathcal{G}} : (\iota\mathcal{G})^+\to\mathcal{G}$ is an isomorphism: since $\mathcal{G}$ already satisfies the gluing axiom, forcing the axiom changes nothing, so $\mathcal{G}^+\cong\mathcal{G}$. Formally, for a full inclusion the counit of $L\dashv\iota$ is invertible iff $\iota$ is full and faithful — which it is. This is the defining feature of a reflective subcategory and makes $(-)^+$ idempotent: $(\mathcal{F}^+)^+\cong\mathcal{F}^+$ (sheafifying twice is sheafifying once).

**Step 3: Limits objectwise, colimits sheafified (part c).**

> [!note]- Derivation
> **Limits.** The inclusion $\iota : \mathbf{Sh}(X)\hookrightarrow\mathbf{PSh}(X)$ is a *right* adjoint (to $(-)^+$). By [[Thm - Right Adjoints Preserve Limits|RAPL]] it preserves limits. Limits in the presheaf category $\mathbf{PSh}(X) = [\mathrm{Open}(X)^{op},\mathbf{Set}]$ are computed objectwise (a limit of presheaves is the presheaf $U\mapsto\lim_i\mathcal{F}_i(U)$). Since $\iota$ preserves limits, the limit of a diagram of sheaves, computed objectwise as presheaves, is *already a sheaf* and is the limit in $\mathbf{Sh}(X)$. So **limits of sheaves are objectwise** — a product of sheaves, an equalizer of sheaf maps, a kernel, are computed section-by-section.
>
> **Colimits.** The reflector $(-)^+$ is a *left* adjoint. By LAPC it preserves colimits. The colimit of a diagram of sheaves $\{\mathcal{F}_i\}$ in $\mathbf{Sh}(X)$ is computed as: take the colimit $P = \mathrm{colim}_i\,\iota\mathcal{F}_i$ in presheaves (objectwise, $U\mapsto\mathrm{colim}_i\mathcal{F}_i(U)$), which need *not* be a sheaf, then sheafify: $\mathrm{colim}^{\mathbf{Sh}}_i\mathcal{F}_i\cong P^+$. Concretely, $\mathrm{colim}^{\mathbf{Sh}}_i\mathcal{F}_i = \big(\mathrm{colim}_i^{\mathbf{PSh}}\mathcal{F}_i\big)^+$. The objectwise colimit fails the gluing axiom in general (a colimit of sheaves is "locally" a colimit but the gluing must be reimposed), and sheafification is exactly the reapplication of gluing.

> [!note]- Complete formal solution
> **(a)** $\mathbf{Sh}(X)$ is a full subcategory of $\mathbf{PSh}(X)$, and the inclusion $\iota$ has a left adjoint $(-)^+$ (sheafification), so $\mathbf{Sh}(X)$ is reflective with bijection $\mathbf{Sh}(X)(\mathcal{F}^+,\mathcal{G})\cong\mathbf{PSh}(X)(\mathcal{F},\iota\mathcal{G})$ and unit $\theta_{\mathcal{F}} : \mathcal{F}\to\mathcal{F}^+$.
>
> **(b)** The unit is universal among maps from $\mathcal{F}$ to sheaves, so $\mathcal{F}^+$ is the universal way to force the gluing axiom (the best sheaf approximation). The counit $\varepsilon_{\mathcal{G}} : \mathcal{G}^+\to\mathcal{G}$ is an isomorphism for sheaves $\mathcal{G}$ (a sheaf already glues), making $(-)^+$ idempotent — the defining property of reflectivity.
>
> **(c)** By RAPL, $\iota$ preserves limits, so limits of sheaves are the objectwise presheaf limits (already sheaves). By LAPC, $(-)^+$ preserves colimits, so colimits of sheaves are the sheafification of the objectwise presheaf colimit: $\mathrm{colim}^{\mathbf{Sh}}\mathcal{F}_i = (\mathrm{colim}^{\mathbf{PSh}}\mathcal{F}_i)^+$. $\blacksquare$

---

# Key Takeaways

**Sheafification is a reflector, so "the universal way to force the gluing axiom" is a one-line universal property, not a construction.** The intricate hands-on construction of $\mathcal{F}^+$ (sheaf of compatible germs, plus-construction applied twice) is replaced, categorically, by a single statement: $(-)^+$ is left adjoint to the inclusion of sheaves into presheaves, and the unit $\theta_{\mathcal{F}} : \mathcal{F}\to\mathcal{F}^+$ is universal among maps from $\mathcal{F}$ to sheaves. This is the same reflective-subcategory pattern as [[Ex - Abelianization is left adjoint to inclusion|abelianisation]] and completion: an "-ification" is a reflector, its unit is the universal map forcing the property, and its counit is an isomorphism. The trigger to recognise this is any "force a local-to-global / closure / completeness condition universally" — the operation is a reflector and inherits all the abstract theorems.

**Handedness dictates that sheaf limits are objectwise but sheaf colimits must be sheafified.** Because the inclusion is a *right* adjoint it preserves limits, so a product or equalizer or pullback of sheaves is computed section-by-section and is automatically a sheaf. Because the reflector is a *left* adjoint it preserves colimits, so a coproduct, coequalizer, or pushout of sheaves is the *sheafification* of the objectwise presheaf colimit — the objectwise version generally fails gluing. This asymmetry is the single most important computational fact about sheaf categories and the source of countless errors: "the colimit of sheaves is objectwise" is false. The general principle — reflective subcategories are closed under limits but have colimits computed by reflecting the ambient colimit — follows purely from [[Thm - Right Adjoints Preserve Limits|RAPL/LAPC]] and applies to every reflective localization.

**This is the gateway from adjunctions to algebraic geometry and topos theory.** The recognition "sheaves are a reflective subcategory of presheaves, with sheafification the reflector" is the entry point to the entire sheaf-theoretic machinery of modern geometry. A **Grothendieck topos** is *defined* as a left-exact reflective localization of a presheaf category — exactly this structure, with the extra demand that the reflector $(-)^+$ preserve finite limits (left-exactness), which is what makes sheaf cohomology and the internal logic behave. The **structure sheaf** of a **scheme** is built by sheafifying a presheaf of rings; the **functor of points** sees a scheme as a sheaf for the Zariski (or étale) topology. So this single ⭐⭐⭐ exercise is the categorical seed of schemes, topoi, and sheaf cohomology — the running algebraic-geometry thread of the whole Category Theory subject. The companion exercise [[Ex - Abelianization is left adjoint to inclusion|Abelianization is left adjoint to inclusion]] is the same reflector pattern in pure algebra, useful as a warm-up before the sheaf case.
