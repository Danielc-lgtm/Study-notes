---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - The Quillen Model Structure on Topological Spaces"
  - "Def - Higher Homotopy Group"
  - "Def - Homotopy Equivalence and Contractible Space"
  - "Def - Cofibrant and Fibrant Objects"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Exhibit a **weak homotopy equivalence** that is **not** a [[Def - Homotopy Equivalence and Contractible Space|homotopy equivalence]], and locate exactly where the CW hypothesis of Whitehead's theorem is used. Use the Warsaw circle $W$: the inclusion of a point $* \to W$ is a weak homotopy equivalence but not a homotopy equivalence. Explain why this is *consistent* with the [[Def - The Quillen Model Structure on Topological Spaces|Quillen model structure]] — namely, that the discrepancy disappears after [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]] (CW approximation), which is precisely why $\mathrm{Ho}(\mathbf{Top})$ is built from cofibrant objects.

**Recall:**

A **weak homotopy equivalence** induces a bijection on $\pi_0$ and isomorphisms on all [[Def - Higher Homotopy Group|homotopy groups]] $\pi_n$. A **homotopy equivalence** is a map $f$ with a homotopy inverse $g$ ($gf \simeq \mathrm{id}$, $fg \simeq \mathrm{id}$). **Whitehead's theorem:** a weak homotopy equivalence between CW complexes is a homotopy equivalence. The **Warsaw circle** $W$ is the compact subset of $\mathbb{R}^2$ formed by the closure of the topologist's sine curve $\{(x, \sin(1/x)) : 0 < x \leq 1\}$ together with the vertical segment $\{0\} \times [-1,1]$ and an arc joining the endpoint $(1, \sin 1)$ back to a point of the segment. It is path-connected-after-closure-fails: $W$ has trivial homotopy groups ($\pi_n(W) = 0$ for all $n$) but is **not** contractible.

---

# Convergent Strategy

**Problem class:** This is a "counterexample / boundary-of-a-theorem" problem. The routine is to produce a space where two notions that usually agree (weak and genuine homotopy equivalence) come apart, then diagnose precisely which hypothesis fails and how the model structure repairs it.

**Assumption pattern:** The recognisable structure is a space that is *weakly contractible but not contractible* — the signature of a non-CW pathology. The Warsaw circle's two key properties (all $\pi_n = 0$; not contractible) are exactly what is needed: trivial homotopy groups make $* \to W$ a weak equivalence, while non-contractibility blocks a homotopy inverse.

**Theorem routing:** The route is: (1) $\pi_n(W) = 0$ for all $n$ $\Rightarrow$ $* \to W$ is a weak homotopy equivalence; (2) $W$ not contractible $\Rightarrow$ no homotopy inverse to $* \to W$ exists, so it is not a homotopy equivalence; (3) Whitehead's theorem does not apply because $W$ is not a CW complex; (4) in the [[Def - The Quillen Model Structure on Topological Spaces|model structure]], $W$ is not cofibrant, and its [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]] (CW approximation) *is* a point, so $W$ becomes isomorphic to $*$ in $\mathrm{Ho}(\mathbf{Top})$.

**Key decision point:** The non-obvious choice is proving $W$ is not contractible despite having all homotopy groups trivial — these usually go together. The argument cannot use homotopy groups (they are all zero); it must use a finer property, namely that $W$ fails to be locally connected / locally path-connected near the limit segment, which obstructs the global homotopy that contractibility would require. Recognising that homotopy groups are *insufficient* to detect the obstruction is the entire point of the exercise.

---

# Legal Operations Used

1. **Operation 4 from the topic page (recognise (co)fibrant structure / homotopy intuition).** Used to identify $W$ as fibrant but not cofibrant and to invoke cofibrant replacement.

2. **Operation 5 from the topic page (cellular structure / CW approximation).** The repair is CW approximation, the cofibrant replacement built by attaching cells.

---

# Hints

> [!note]- Hint 1
> First convince yourself $* \to W$ is a weak equivalence: it suffices that $\pi_n(W) = 0$ for all $n$ (and $W$ path-connected for $\pi_0$). Take these properties of $W$ as given.

> [!note]- Hint 2
> Why is $* \to W$ not a homotopy equivalence? A homotopy inverse $W \to *$ composed back would give a homotopy $\mathrm{id}_W \simeq \text{const}$, i.e. a contraction of $W$. So you need: $W$ is not contractible.

> [!note]- Hint 3
> $W$ is not contractible because it is not locally path-connected near the vertical segment $\{0\}\times[-1,1]$: a contracting homotopy would have to move points across the gap where the sine curve oscillates infinitely, which no continuous homotopy can do uniformly. Whitehead's theorem fails here precisely because $W$ is not a CW complex — CW complexes are locally contractible, which $W$ is not.

---

# Solution

The Warsaw circle is weakly contractible (all homotopy groups vanish) but not contractible (no continuous global contraction, due to its bad local structure). So $* \to W$ is a weak equivalence without a homotopy inverse. Whitehead's theorem does not save us because $W$ is not CW; the model structure resolves the tension because $W$ is not cofibrant and its cofibrant replacement is a point.

**Step 1: $* \to W$ is a weak homotopy equivalence.**

> [!note]- Derivation
> The Warsaw circle $W$ has $\pi_n(W) = 0$ for all $n \geq 1$ and is path-connected (so $\pi_0(W) = *$). The inclusion $\iota : * \to W$ of any point induces $\pi_n(*) = 0 \to \pi_n(W) = 0$ for all $n$ — isomorphisms (both trivial) — and a bijection on $\pi_0$. By definition $\iota$ is a [[Def - Higher Homotopy Group|weak homotopy equivalence]].

**Step 2: $* \to W$ is not a homotopy equivalence.**

> [!note]- Derivation
> Suppose $\iota : * \to W$ had a homotopy inverse $r : W \to *$ (the only map to a point). Then $\iota \circ r \simeq \mathrm{id}_W$, i.e. the constant map at $\iota(*)$ is homotopic to $\mathrm{id}_W$. A homotopy $\mathrm{id}_W \simeq \text{const}$ is exactly a contraction of $W$; so $W$ would be [[Def - Homotopy Equivalence and Contractible Space|contractible]].
>
> But $W$ is *not* contractible. The obstruction is its local structure near the limit segment $\{0\}\times[-1,1]$: $W$ is not locally path-connected there (every neighbourhood of a point on the segment contains infinitely many disjoint pieces of the oscillating sine curve). A contracting homotopy $H : W \times I \to W$ would, restricted to the segment, have to continuously pull those infinitely-oscillating arcs together, which is impossible for a continuous map — concretely, one shows any nullhomotopy would force a discontinuity at the segment. Hence $W$ is not contractible, so $\iota$ has no homotopy inverse and is *not* a homotopy equivalence.

**Step 3: Whitehead's theorem and the model-structure repair.**

> [!note]- Derivation
> **Whitehead's theorem** says a weak homotopy equivalence *between CW complexes* is a homotopy equivalence. It does not apply to $\iota : * \to W$ because $W$ is **not a CW complex** — CW complexes are locally contractible, and $W$ fails local contractibility at the segment. This is exactly where the CW hypothesis is load-bearing: Whitehead's proof builds the homotopy inverse cell by cell using the cell structure, and $W$ has no cell structure compatible with its pathological local topology.
>
> In the [[Def - The Quillen Model Structure on Topological Spaces|Quillen model structure]], this is not a defect but the expected behaviour. The point $*$ is cofibrant (CW), but $W$ is **not cofibrant** (not a retract of a CW complex). The [[Thm - The Homotopy Category of a Model Category|fundamental theorem]] computes morphisms via [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]]: a CW approximation of $W$ is a weak equivalence $\Gamma W \xrightarrow{\sim} W$ from a CW complex $\Gamma W$. Since $W$ is weakly contractible, $\Gamma W$ is a weakly contractible CW complex, hence (by Whitehead, now applicable) contractible — it is homotopy equivalent to a point. Therefore in $\mathrm{Ho}(\mathbf{Top})$, $W \cong \Gamma W \cong *$: the Warsaw circle *is* a point in the homotopy category. The weak equivalence $\iota$ becomes an isomorphism in $\mathrm{Ho}$, exactly as a weak equivalence must. The lesson: $\mathrm{Ho}(\mathbf{Top})$ is built from cofibrant objects precisely so that weak equivalences become isomorphisms and Whitehead-type pathologies are washed out.

> [!note]- Complete formal solution
> $W$ has $\pi_n(W) = 0$ for all $n$ and is path-connected, so $\iota : * \to W$ induces isomorphisms on all $\pi_n$ and a bijection on $\pi_0$: it is a weak homotopy equivalence. If $\iota$ were a homotopy equivalence, $\iota \circ r \simeq \mathrm{id}_W$ for $r : W \to *$ would contract $W$; but $W$ is not contractible (it is not locally path-connected at the segment $\{0\}\times[-1,1]$, obstructing any continuous global nullhomotopy). So $\iota$ is not a homotopy equivalence. Whitehead's theorem does not apply because $W$ is not a CW complex (CW complexes are locally contractible, $W$ is not) — this is where the CW hypothesis is essential. In the Quillen model structure $W$ is not cofibrant; its CW approximation $\Gamma W$ is a weakly contractible CW complex, hence contractible by Whitehead, so $W \cong \Gamma W \cong *$ in $\mathrm{Ho}(\mathbf{Top})$, and $\iota$ becomes an isomorphism there. $\blacksquare$

---

# Key Takeaways

**Homotopy groups can all vanish without the space being contractible — weak contractibility is strictly weaker than contractibility.** The central phenomenon is that the homotopy groups $\pi_n$ are *insufficient* invariants for badly-behaved spaces: the Warsaw circle has every $\pi_n = 0$ yet is not contractible. The reason is local: contractibility is a global homotopy condition that interacts with local structure, and a space that is not locally nice (not locally path-connected, not locally contractible) can carry an obstruction invisible to homotopy groups. The diagnostic to carry forward: when asked whether a weakly contractible space is contractible, *do not* try to use homotopy groups (they are all zero); instead probe the local structure, because the obstruction lives there. This is the signature of every non-CW pathology.

**The CW hypothesis in Whitehead's theorem is exactly the hypothesis that the space is cofibrant.** Whitehead's theorem is not a quirk of CW complexes; it is the fundamental theorem of model categories specialised to cofibrant objects. A weak equivalence becomes invertible up to homotopy *between cofibrant objects*, and CW complexes are the cofibrant objects of $\mathbf{Top}$. So "needs CW" everywhere in classical algebraic topology is, model-categorically, "needs cofibrant". The transferable principle: whenever a classical theorem carries a CW (or "nice space") hypothesis, suspect it is really a cofibrancy hypothesis, and the model-categorical version holds for cofibrant objects in any model category. This unifies a scattered collection of "regularity hypotheses" across topology under a single concept.

**Cofibrant replacement is what makes the homotopy category well-behaved, and it washes out pathologies.** The resolution of the apparent paradox — a weak equivalence that is not a homotopy equivalence, in a framework where weak equivalences are supposed to become isomorphisms — is that the homotopy category is built from cofibrant objects via replacement. After CW approximation, the Warsaw circle becomes a point, and the weak equivalence becomes an honest isomorphism in $\mathrm{Ho}(\mathbf{Top})$. The trigger is "a weak equivalence that fails to be invertible on the nose"; the reaction is "replace the offending object by a cofibrant model, where the inversion exists". This is the same mechanism by which a non-projective module is resolved before computing a derived functor: cofibrant replacement is the universal repair that makes homotopy-theoretic constructions well-defined, and the entire point of the (co)fibrant-objects machinery is to perform it systematically.
