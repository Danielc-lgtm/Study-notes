---
type: exercise
subject: model-categories
difficulty: "⭐"
prereqs:
  - "Def - The Quillen Model Structure on Topological Spaces"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Topological Space"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show, directly from the definition of a Serre fibration, that for any [[Def - Topological Space|topological space]] $X$ the unique map $X \to *$ to the one-point space is a Serre fibration. Conclude that **every object of $\mathbf{Top}$ is fibrant** in the [[Def - The Quillen Model Structure on Topological Spaces|Quillen model structure]].

**Recall:**

A **Serre fibration** is a continuous map $p : E \to B$ with the **homotopy lifting property against disks**: for every $n \geq 0$, every homotopy $H : D^n \times I \to B$ and every lift $\tilde{h}_0 : D^n \to E$ of its restriction $H|_{D^n \times \{0\}}$, there exists $\tilde{H} : D^n \times I \to E$ with $\tilde{H}|_{D^n \times \{0\}} = \tilde{h}_0$ and $p \circ \tilde{H} = H$.

![[Def - Cofibrant and Fibrant Objects#The Definition]]

In the Quillen model structure on $\mathbf{Top}$, the fibrations are exactly the Serre fibrations, and $*$ is the one-point space (the terminal object).

---

# Convergent Strategy

**Problem class:** This is the simplest "identify the (co)fibrant objects" problem — establishing that one class of objects is *everything*. The routine is to unwind the definition of "fibrant" (the map to the terminal object is a fibration) and check the lifting condition is vacuous.

**Assumption pattern:** The recognisable assumption is "fibrant", which means $X \to *$ is a fibration = Serre fibration. The structural fact that makes this trivial is that any homotopy *into the point* is the constant homotopy, so the lifting problem has no content beyond its bottom data.

**Theorem routing:** The route is a one-line unwinding of [[Def - The Quillen Model Structure on Topological Spaces|the definition of Serre fibration]]: a homotopy $H : D^n \times I \to *$ is necessarily constant (the only map into a point), so the given lift of its bottom *is already* a lift of the whole homotopy.

**Key decision point:** The only subtlety is realising that the lifted homotopy can be taken constant in the $I$-direction. The natural — and correct — choice is $\tilde{H}(x, t) = \tilde{h}_0(x)$, the homotopy that does nothing; verifying this projects correctly to $H$ is immediate because $H$ itself is constant.

---

# Legal Operations Used

1. **Operation 4 from the topic page (recognise a fibration of spaces by the homotopy lifting property).** The entire solution is checking the homotopy lifting property for the map to a point, where it holds trivially.

---

# Hints

> [!note]- Hint 1
> What does a homotopy $H : D^n \times I \to *$ into the one-point space look like? How many continuous maps are there from any space into a point?

> [!note]- Hint 2
> Since $H$ is forced to be the constant map, the condition $p \circ \tilde{H} = H$ is automatic for *any* $\tilde{H}$ into a point. So you only need $\tilde{H}$ to extend the given $\tilde{h}_0$. What is the easiest such extension?

---

# Solution

The proof is immediate: a homotopy into the point carries no information, so the constant extension of the given bottom lift solves every lifting problem.

**Step 1: $X \to *$ is a Serre fibration.**

> [!note]- Derivation
> Let $p : X \to *$ be the unique map. Take any homotopy lifting problem: a homotopy $H : D^n \times I \to *$ and a lift $\tilde{h}_0 : D^n \to X$ of $H|_{D^n \times \{0\}}$. Since $*$ has exactly one point, $H$ is the unique (constant) map $D^n \times I \to *$, and the condition "$\tilde{h}_0$ lifts $H|_{D^n \times \{0\}}$" is vacuous (it just says $p\tilde{h}_0$ is the constant map, which it is).
>
> Define $\tilde{H} : D^n \times I \to X$ by $\tilde{H}(x, t) = \tilde{h}_0(x)$ — the homotopy constant in $t$. It is continuous (composite of the projection $D^n \times I \to D^n$ with $\tilde{h}_0$), it restricts to $\tilde{h}_0$ at $t = 0$, and $p \circ \tilde{H} = H$ automatically because both are the unique map into $*$. So $\tilde{H}$ is the required lift. As $n$ was arbitrary, $p$ has the homotopy lifting property against all disks, i.e. $p$ is a Serre fibration.

**Step 2: every space is fibrant.**

> [!note]- Derivation
> An object $X$ is [[Def - Cofibrant and Fibrant Objects|fibrant]] precisely when the unique map to the terminal object $X \to *$ is a fibration. In the Quillen model structure the fibrations are the Serre fibrations, and Step 1 shows $X \to *$ is a Serre fibration for every $X$. Therefore every object of $\mathbf{Top}$ is fibrant, and there is no fibrant-replacement step in this model structure.

> [!note]- Complete formal solution
> Let $X$ be any space and $p : X \to *$ the map to the one-point space. For a homotopy lifting problem $H : D^n \times I \to *$, $\tilde{h}_0 : D^n \to X$, note $H$ is the constant map (only one map into $*$). Set $\tilde{H}(x,t) = \tilde{h}_0(x)$; it is continuous, extends $\tilde{h}_0$, and satisfies $p\tilde{H} = H$ trivially. So $p$ is a Serre fibration for every $X$, hence every object is fibrant. $\blacksquare$

---

# Key Takeaways

**Maps into a terminal object are always "the easy direction" — fibrancy over $*$ is usually free or nearly free.** The reason every space is fibrant is structural: the terminal object $*$ absorbs all homotopies trivially, so the lifting problem to it is vacuous. This recurs across model categories: in $\mathbf{Ch}(R)$ every object is fibrant (the map to $0$ is degreewise surjective onto zero), and in the stable module category every object is fibrant too. The trigger is "is $X$ fibrant?" with the terminal object being simple (a point, the zero object); the reaction is "the map to the terminal object usually lifts everything trivially". When fibrancy is *not* automatic — as for simplicial sets, where fibrant means Kan complex — that is the signal that the terminal object is interacting nontrivially and there is real content in fibrant replacement.

**Half of a model structure is often trivial, and knowing which half tells you where the work is.** In the Quillen structure on $\mathbf{Top}$, fibrancy is free and all the difficulty is in cofibrancy (CW approximation). The dual happens in the injective model structure on chain complexes, where cofibrancy is free and fibrancy (injective resolution) is the work. Recognising which side is trivial immediately focuses your effort: if every object is fibrant, then bifibrant means cofibrant, derived functors of *right* Quillen functors are computed by fibrant replacement (= identity, so they are easy) and the action is all in the *left* derived functors. The diagnostic to carry forward: before computing anything in a model category, ask "which objects are automatically (co)fibrant?", because that determines where every replacement step lands.

**A "vacuous lifting problem" is a real proof technique, not a degenerate case.** The argument here — the homotopy is constant, so the constant extension works — is the prototype of a family of arguments where a lifting problem is solved because one of its inputs is forced to be trivial. The same pattern proves that the initial object is cofibrant (the map from $\emptyset$ has empty domain, so every lifting problem against it is vacuously solvable) and underlies many "edge cases" in the small object argument. When you face a lifting problem, always check first whether one of the corner maps is forced (constant, empty, or an isomorphism), because that often collapses the problem entirely.
