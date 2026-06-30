---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Segal Category and Complete Segal Space"
  - "Def - Simplicial Set"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Construct an explicit **Segal space** $X$ that is *not* a **[[Def - Segal Category and Complete Segal Space|complete Segal space]]**, by arranging two objects that are *equivalent* but lie in *distinct path-components* of the object-space $X_0$. Verify that $X$ satisfies the Segal condition but fails Rezk's completeness condition, and explain why this makes $X$ *not* equivalence-invariant: the [[Def - Homotopy|homotopy]] theory it presents is wrong, because the localisation that should identify equivalent objects genuinely changes $X$. Then describe the *completion* of $X$ and confirm it has a single path-component of objects.

**Recall:**

![[Def - Segal Category and Complete Segal Space#The Definition]]

A **Segal space** $X : \Delta^{op} \to \mathbf{sSet}$ satisfies $X_n \xrightarrow{\simeq} X_1 \times_{X_0} \cdots \times_{X_0} X_1$ for all $n \ge 2$. It is **complete** if the degeneracy $s_0 : X_0 \to X^{\mathrm{heq}}_1$ onto the space of homotopy-equivalences is a weak equivalence — equivalently, *equivalent objects are connected by a path in $X_0$*.

A morphism $f : a \to b$ is a **homotopy equivalence** in $X$ if it is invertible in the homotopy category $\mathrm{ho}(X)$ (there is $g : b \to a$ with $g\circ f \simeq \mathrm{id}_a$, $f\circ g \simeq \mathrm{id}_b$).

---

# Convergent Strategy

**Problem class:** This is a *counterexample-construction* problem — exhibit an object satisfying one axiom but failing another, to demonstrate the second axiom is not redundant. The routine is to build the smallest structure where the two conditions come apart, then trace the consequence (failure of invariance).

**Assumption pattern:** The Segal condition is about *composition* (the spine maps are equivalences); completeness is about *objects* (equivalent objects are path-connected in $X_0$). These are logically independent, so the construction must satisfy the first while violating the second. The recognizable lever is "make two objects equivalent via a morphism but keep $X_0$ discrete with two separate points".

**Theorem routing:** The route is: take the nerve-style Segal space of the *contractible groupoid on two objects* $\mathcal{I} = \{a \xrightarrow{\sim} b\}$ (one isomorphism each way), but record the object-space $X_0$ as the *discrete* two-point set $\{a, b\}$ rather than as the classifying space of $\mathcal{I}$. The Segal condition holds because composition is fine; completeness fails because $a$ and $b$ are equivalent (via the iso) yet $X_0 = \{a, b\}$ has two path-components. The completion replaces $X_0$ by the contractible space $X^{\mathrm{heq}}_1$, which has one path-component.

**Key decision point:** The non-obvious choice is to keep $X_0$ *discrete* (or otherwise under-connected) while making the morphism between the two objects an equivalence. The temptation is to build the "obviously correct" Segal space where $X_0$ already records the equivalence as a path — but that one *is* complete, and would not be a counterexample. The whole point is to record too little in $X_0$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (read the Segal condition as composition).** We verify the Segal condition by checking that composition of the (few) morphisms behaves correctly.

2. **Operation 9 from the topic page (add completeness to rigidify equivalences).** The exercise is precisely a study of what goes wrong *without* this operation, and the completion is operation 9 applied as the repair.

3. **Operation 6 from the topic page (pass to the homotopy category to test invariance).** We compare $\mathrm{ho}(X)$ before and after completion to see that completion does not change the homotopy category but does fix $X_0$.

---

# Hints

> [!note]- Hint 1
> The smallest interesting example uses two objects $a, b$ with a chosen isomorphism between them. As an ordinary category this is the "contractible groupoid" (walking isomorphism) $\mathcal{I}$. The freedom you have is *how much of the equivalence to record in the object-space $X_0$*.

> [!note]- Hint 2
> To violate completeness, make $X_0$ the *discrete* two-point set $\{a, b\}$. Then the isomorphism $a \to b$ is an element of $X^{\mathrm{heq}}_1$, but the degeneracy $s_0 : X_0 \to X^{\mathrm{heq}}_1$ cannot be surjective on path-components: $X_0$ has two components, while $X^{\mathrm{heq}}_1$ (containing the iso connecting $a$ and $b$) is connected.

> [!note]- Hint 3
> "Not equivalence-invariant" means: $X$ should be equivalent (as an $(\infty,1)$-category) to the terminal one-object structure, since $a$ and $b$ are equivalent. But $X$ remembers two objects in $\pi_0 X_0$. The localisation inverting equivalences must therefore *change* $X$ — that change is exactly the completion.

> [!note]- Hint 4
> The completion replaces $X_0$ by (a model of) $X^{\mathrm{heq}}_1$. Compute $X^{\mathrm{heq}}_1$: it contains $\mathrm{id}_a$, $\mathrm{id}_b$, the iso $a\to b$ and its inverse, all connected up, so it is contractible. Hence the completed object-space is contractible — one path-component, one object up to equivalence.

---

# Solution

The construction is the walking isomorphism with an under-recorded object-space. Step 1 builds $X$ and checks the Segal condition. Step 2 shows completeness fails. Step 3 traces the failure of invariance and describes the completion.

**Step 1: build $X$ and verify the Segal condition.**

> [!note]- Derivation
> Let $\mathcal{I}$ be the groupoid with two objects $a, b$ and a unique isomorphism $u : a \to b$ (so morphisms are $\mathrm{id}_a, \mathrm{id}_b, u, u^{-1}$). Build a simplicial space $X$ with:
> - $X_0 = \{a, b\}$, the *discrete* two-point space;
> - $X_1 = \{\mathrm{id}_a, \mathrm{id}_b, u, u^{-1}\}$, discrete, with $d_1, d_0$ giving sources and targets;
> - $X_n$ the set of $n$-chains of composable morphisms of $\mathcal{I}$, discrete.
>
> This is the nerve of $\mathcal{I}$ regarded as a *discrete* simplicial space. The **Segal condition** holds: each spine map $X_n \to X_1 \times_{X_0} \cdots \times_{X_0} X_1$ is a *bijection* (an $n$-chain in a groupoid is exactly an $n$-tuple of composable morphisms, as in the companion nerve exercise), hence a weak equivalence. So $X$ is a Segal space, and its homotopy category $\mathrm{ho}(X) = \mathcal{I}$, in which $a \cong b$.

**Step 2: completeness fails.**

> [!note]- Derivation
> The space of homotopy equivalences $X^{\mathrm{heq}}_1 \subseteq X_1$ consists of those morphisms that are invertible in $\mathrm{ho}(X) = \mathcal{I}$ — i.e. *all* of them: $\mathrm{id}_a, \mathrm{id}_b, u, u^{-1}$ are all [[Def - Isomorphism|isomorphisms]]. As a sub-simplicial-set this is (the nerve of) the maximal subgroupoid of $\mathcal{I}$, which is $\mathcal{I}$ itself, a *contractible* (connected, simply connected) groupoid: every two of its objects are uniquely isomorphic, so $X^{\mathrm{heq}}_1$ is connected. But $X_0 = \{a, b\}$ has *two* path-components. The degeneracy $s_0 : X_0 \to X^{\mathrm{heq}}_1$ sends $a \mapsto \mathrm{id}_a$, $b \mapsto \mathrm{id}_b$, which lie in the *same* path-component of $X^{\mathrm{heq}}_1$ (connected by $u$). So $s_0$ is not surjective on $\pi_0$ inverse-image-wise — precisely, it is not a weak equivalence: $\pi_0(X_0) = \{a, b\}$ has two elements while $\pi_0(X^{\mathrm{heq}}_1)$ has one. **Completeness fails.**

**Step 3: failure of invariance, and the completion.**

> [!note]- Derivation
> Because $a \cong b$ in $\mathrm{ho}(X)$, $X$ *ought* to be equivalent, as an $(\infty,1)$-category, to the terminal structure $\ast$ with one object and no nontrivial morphisms — collapsing the unique-isomorphism groupoid to a point is an equivalence of categories. Yet $X$ records $\pi_0(X_0) = \{a,b\}$, two objects. So $X_0$ is *not* an invariant of the $(\infty,1)$-category $X$ presents; it carries spurious information (which object you are at) that no equivalence-invariant notion should see. The localisation $L$ that inverts equivalences must therefore alter $X$: $L X \not\cong X$ as simplicial spaces, even though they present the same $(\infty,1)$-category.
>
> The **completion** $\widehat{X}$ (Rezk's localisation) replaces $X_0$ by a model of $X^{\mathrm{heq}}_1$ — equivalently, it makes the degeneracy $s_0 : \widehat{X}_0 \to \widehat{X}^{\mathrm{heq}}_1$ a weak equivalence. Since $X^{\mathrm{heq}}_1$ is contractible, $\widehat{X}_0$ is contractible: it has a *single* path-component, so $\widehat{X}$ records *one* object up to equivalence, as it must. The homotopy category is unchanged ($\mathrm{ho}(\widehat{X}) = \mathcal{I} \simeq \ast$), but now $\pi_0(\widehat{X}_0) = \ast$ correctly. This is completeness restored, and the homotopy theory is now the right one.

> [!note]- Complete formal solution
> Let $\mathcal{I} = \{a \xrightarrow{u,\ \cong} b\}$ be the walking isomorphism, and let $X$ be its nerve as a *discrete* simplicial space: $X_0 = \{a,b\}$ discrete, $X_n = N\mathcal{I}_n$ discrete.
>
> **Segal:** each spine map $X_n \to X_1\times_{X_0}\cdots\times_{X_0}X_1$ is a bijection (chains $=$ composable tuples in a groupoid), hence a weak equivalence; $X$ is a Segal space with $\mathrm{ho}(X) = \mathcal{I}$.
>
> **Completeness fails:** $X^{\mathrm{heq}}_1 = N(\text{max subgroupoid of }\mathcal{I}) = N\mathcal{I}$ is connected (any two objects uniquely isomorphic), so $\pi_0(X^{\mathrm{heq}}_1) = \ast$, while $\pi_0(X_0) = \{a,b\}$; thus $s_0 : X_0 \to X^{\mathrm{heq}}_1$ is not a weak equivalence.
>
> **Not invariant:** $a \cong b$ forces $X \simeq \ast$ as $(\infty,1)$-categories, yet $\pi_0 X_0 = \{a,b\}$; so $X_0$ is not an equivalence-invariant, and Rezk localisation $L$ changes $X$.
>
> **Completion:** $\widehat{X}$ has $\widehat{X}_0 \simeq X^{\mathrm{heq}}_1$ contractible, so $\pi_0\widehat{X}_0 = \ast$ (one object up to equivalence); $\mathrm{ho}(\widehat{X}) = \mathcal{I} \simeq \ast$ unchanged. Completeness holds. $\blacksquare$

---

# Key Takeaways

**Completeness is the condition that the object-space is an equivalence-invariant.** The deep content of this exercise is *why* Rezk added completeness at all. A bare Segal space gets composition right but can record the wrong set of objects — it can "see" objects that are equivalent as distinct, which no invariant of an $(\infty,1)$-category should do. Completeness is exactly the demand that $\pi_0$ of the object-space equals the set of objects *up to equivalence*, so that the model carries no information an equivalence cannot see. The trigger is "two equivalent objects in different components of $X_0$", and the reaction is "this Segal space is not complete; its homotopy theory is wrong; complete it". This is the same defect, in a different model, as a non-skeletal category carrying redundant isomorphic objects.

**The diagnostic for "wrong homotopy theory" is non-invariance under the relevant localisation.** A model presents the correct homotopy theory only if it is a fixed point of the localisation that inverts the maps it should invert. Here, inverting equivalences must collapse $\{a,b\}$ to a point, and the bare Segal space is *not* such a fixed point — so it is presenting something finer than the intended $(\infty,1)$-category. This is a general and transferable test: whenever you suspect a model carries spurious data, apply the localisation and check whether it changes the object; if it does, the original model was not invariant. The same logic explains why one works with *fibrant-cofibrant* objects in a [[Def - Model Category|model category]] and with *complete* Segal spaces rather than arbitrary ones.

**The completion is "replace the objects by the space of equivalences".** The repair is mechanical and worth remembering: to complete a Segal space, replace $X_0$ by (a model of) $X^{\mathrm{heq}}_1$, the space of self-equivalences, which forces equivalent objects to be path-connected. The effect is to contract away exactly the redundancy — in the example, the two-point object set becomes contractible because the two objects were equivalent. This is the bisimplicial avatar of *skeletonising* or *univalent-completion*: in homotopy type theory the same move is the univalence axiom (equivalent types are equal), and recognising the three as one operation — complete the Segal space, skeletonise the category, impose univalence — is a high-leverage cross-model insight.
