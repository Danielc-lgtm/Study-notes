---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Def - Homotopy"
  - "Def - Model Category"
  - "Def - Topological Space"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Work in $\mathbf{Top}$ with the Quillen (Serre) model structure: weak equivalences are weak homotopy equivalences, fibrations are Serre fibrations, cofibrations are retracts of relative cell complexes.

(a) Show that for a CW complex $A$, the product $A \times [0,1]$ — with the two end-inclusions $a \mapsto (a,0)$, $a \mapsto (a,1)$ and the projection $A \times [0,1] \to A$ — is a [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] for $A$ in the model-categorical sense.

(b) Conclude that for a CW complex $A$ and any space $B$, two continuous maps $f, g : A \to B$ are **left homotopic** in the model-categorical sense if and only if they are [[Def - Homotopy|homotopic]] in the classical sense (there is a continuous $H : A \times [0,1] \to B$ with $H(-, 0) = f$, $H(-, 1) = g$).

(c) Identify the dual: describe a path object for a space $B$, and explain why right homotopy also recovers classical homotopy.

**Recall:**

![[Def - Cylinder Object, Path Object, and Homotopy#The Definition]]

A classical [[Def - Homotopy|homotopy]] between $f, g : A \to B$ is a continuous map $H : A \times [0,1] \to B$ with $H(a, 0) = f(a)$ and $H(a, 1) = g(a)$.

In the Quillen model structure on $\mathbf{Top}$, the inclusion of a subcomplex into a CW complex is a cofibration, and the projection $A \times [0,1] \to A$ is a homotopy equivalence (hence a weak equivalence).

---

# Convergent Strategy

**Problem class:** This is an identification problem — showing that the abstract model-categorical homotopy relation specializes to the concrete classical one. It is an instance of the "identify the homotopy category" family on the [[Model Categories — Quillen's Axiomatization of Homotopy Theory#Sources and Targets|topic page]], at the level of the homotopy *relation* rather than the whole category.

**Assumption pattern:** The recognizable feature is that the abstract cylinder $\mathrm{Cyl}(A)$ is being matched to the concrete $A \times [0,1]$. The unlock is checking that $A \times [0,1]$ has the two defining properties of a cylinder object — the end-inclusions assemble into a cofibration, and the projection is a weak equivalence — both of which are standard facts about CW complexes.

**Theorem routing:** Part (a) routes through "subcomplex inclusion is a cofibration" (so $A \sqcup A = A \times \{0,1\} \hookrightarrow A \times [0,1]$ is a cofibration) and "projection is a homotopy equivalence hence a weak equivalence." Part (b) is then immediate from the definition of left homotopy: a map $A \times [0,1] \to B$ restricting to $f, g$ on the ends *is* a classical homotopy. Part (c) dualizes to the path space $B^{[0,1]}$.

**Key decision point:** The one thing to verify carefully is that $A \times \{0, 1\} \hookrightarrow A \times [0,1]$ is a cofibration — this is where CW structure (or, more precisely, $A$ being cofibrant) is used. The decision is to recognize $A \times \{0,1\}$ as a subcomplex of the CW complex $A \times [0,1]$, so its inclusion is a relative cell complex inclusion, hence a cofibration.

---

# Legal Operations Used

1. **Operation 6 from the topic page (build a homotopy as a map out of a cylinder).** The whole exercise is the identification of "map out of $\mathrm{Cyl}(A)$" with "classical homotopy $A \times [0,1] \to B$."

2. **Operation 8 from the topic page (recognize a class by its lifting property), applied to cofibrations.** Verifying $A \times \{0,1\} \hookrightarrow A \times [0,1]$ is a cofibration uses the characterization of cofibrations as subcomplex inclusions (which have the homotopy extension property, the LLP form).

3. **Operation 5 from the topic page (use two-out-of-three / weak equivalence).** The projection $A \times [0,1] \to A$ is a homotopy equivalence, hence a weak homotopy equivalence (homotopy equivalences induce isomorphisms on all $\pi_n$).

---

# Hints

> [!note]- Hint 1
> A cylinder object factors the fold map $A \sqcup A \to A$. Note $A \sqcup A = A \times \{0\} \sqcup A \times \{1\} = A \times \{0,1\}$, and the fold map is $A \times \{0,1\} \to A$, $(a, \epsilon) \mapsto a$. The candidate factorization is $A \times \{0,1\} \hookrightarrow A \times [0,1] \xrightarrow{\mathrm{pr}} A$.

> [!note]- Hint 2
> Why is $A \times \{0,1\} \hookrightarrow A \times [0,1]$ a cofibration? Because $A \times \{0,1\}$ is a subcomplex of the CW complex $A \times [0,1]$, and subcomplex inclusions are cofibrations (they have the homotopy extension property).

> [!note]- Hint 3
> Why is $\mathrm{pr} : A \times [0,1] \to A$ a weak equivalence? Because $[0,1]$ is contractible, $A \times [0,1] \to A$ is a homotopy equivalence (the zero-section is a homotopy inverse), and homotopy equivalences are weak homotopy equivalences.

> [!note]- Hint 4
> For (b): a left homotopy is a map $H : A \times [0,1] \to B$ with $H \circ \mathrm{i}_0 = f$, $H \circ \mathrm{i}_1 = g$. Unwinding, $H(a, 0) = f(a)$ and $H(a, 1) = g(a)$ — this is exactly a classical homotopy.

---

# Solution

The solution verifies $A \times [0,1]$ is a cylinder object (end-inclusion a cofibration, projection a weak equivalence), reads off that left homotopy is classical homotopy, and dualizes to the path space.

**Step 1: $A \times [0,1]$ is a cylinder object for a CW complex $A$.**

> [!note]- Derivation
> The fold map $\nabla : A \sqcup A \to A$ is, identifying $A \sqcup A = A \times \{0,1\}$, the projection $(a, \epsilon) \mapsto a$. Factor it as
> $$A \times \{0,1\} \;\xrightarrow{\;\iota\;}\; A \times [0,1] \;\xrightarrow{\;\mathrm{pr}\;}\; A.$$
> *The inclusion $\iota$ is a cofibration:* $A \times \{0,1\}$ is a subcomplex of the CW complex $A \times [0,1]$ (the product CW structure has $A \times \{0\}$ and $A \times \{1\}$ as subcomplexes), so $\iota$ is a relative cell complex inclusion, hence a cofibration in the Quillen model structure. *The projection $\mathrm{pr}$ is a weak equivalence:* the zero-section $A \to A \times [0,1]$, $a \mapsto (a, 0)$, is a homotopy inverse to $\mathrm{pr}$ (their composites are homotopic to identities via the linear contraction of $[0,1]$ to $0$), so $\mathrm{pr}$ is a homotopy equivalence, hence induces isomorphisms on all $\pi_n$, hence is a weak homotopy equivalence. So the factorization exhibits $A \times [0,1]$ as a cylinder object, with end-inclusions $\mathrm{i}_0(a) = (a,0)$, $\mathrm{i}_1(a) = (a,1)$ and structure map $\mathrm{pr}$.

**Step 2: Left homotopy = classical homotopy.**

> [!note]- Derivation
> By definition, $f \simeq_\ell g$ means there is a map $H : \mathrm{Cyl}(A) \to B$ with $H \mathrm{i}_0 = f$, $H \mathrm{i}_1 = g$. Taking $\mathrm{Cyl}(A) = A \times [0,1]$ (Step 1), this is a continuous map $H : A \times [0,1] \to B$ with $H(a, 0) = (H \mathrm{i}_0)(a) = f(a)$ and $H(a, 1) = (H \mathrm{i}_1)(a) = g(a)$ — precisely a classical homotopy from $f$ to $g$. Conversely any classical homotopy is such an $H$. So the two notions coincide. (That left homotopy does not depend on the choice of cylinder, when $A$ is cofibrant, is the content of [[Ex - Left homotopy is an equivalence relation on cofibrant objects]]; here we have exhibited one cylinder for which it is literally classical homotopy.)

**Step 3: The dual — path objects and right homotopy.**

> [!note]- Derivation
> A path object for $B$ factors the diagonal $\Delta : B \to B \times B$. Take the path space $B^{[0,1]}$ (continuous maps $[0,1] \to B$, compact-open topology). The constant-path inclusion $c : B \to B^{[0,1]}$, $b \mapsto (\text{constant path at } b)$, is a homotopy equivalence (with homotopy inverse the evaluation at $0$), hence a weak equivalence; the endpoint-evaluation $(\mathrm{ev}_0, \mathrm{ev}_1) : B^{[0,1]} \to B \times B$ is a Serre fibration (path-lifting). Since $(\mathrm{ev}_0, \mathrm{ev}_1) \circ c = \Delta$, this is a path object. A right homotopy $K : A \to B^{[0,1]}$ with $\mathrm{ev}_0 K = f$, $\mathrm{ev}_1 K = g$ assigns to each $a \in A$ a path from $f(a)$ to $g(a)$; its exponential transpose $A \times [0,1] \to B$ is exactly a classical homotopy. So right homotopy also recovers classical homotopy, and the two agree (as they must, since CW complexes are cofibrant and every space is fibrant, so $A, B$ is a cofibrant/fibrant pair).

> [!note]- Complete formal solution
> **(a)** Identify $A \sqcup A = A \times \{0,1\}$ and the fold map with the projection. The factorization $A \times \{0,1\} \xrightarrow{\iota} A \times [0,1] \xrightarrow{\mathrm{pr}} A$ has $\iota$ a cofibration (subcomplex inclusion into the CW complex $A \times [0,1]$) and $\mathrm{pr}$ a weak equivalence (homotopy equivalence via the zero-section, since $[0,1]$ is contractible). So $A \times [0,1]$ is a cylinder object.
>
> **(b)** A left homotopy is a map $H : A \times [0,1] \to B$ with $H(a,0) = f(a)$, $H(a,1) = g(a)$ — exactly a classical homotopy. Hence $f \simeq_\ell g$ iff $f \simeq g$ classically.
>
> **(c)** The path space $B^{[0,1]}$, with constant-path inclusion (a weak equivalence) and endpoint evaluation (a Serre fibration), is a path object; a right homotopy $A \to B^{[0,1]}$ transposes to a classical homotopy $A \times [0,1] \to B$. Since $A$ is cofibrant and $B$ fibrant, left and right homotopy coincide, both equal to classical homotopy. $\blacksquare$

---

# Key Takeaways

**The abstract cylinder object is faithful to the topological cylinder, which is the sanity check that the axiomatization captured the right notion.** The whole point of defining homotopy through cylinder objects was to abstract the topological cylinder $A \times [0,1]$ to settings with no interval; this exercise confirms that in $\mathbf{Top}$ the abstraction recovers exactly the classical relation. The two defining properties of a cylinder object — the end-inclusion is a cofibration, the projection is a weak equivalence — translate to "the ends embed nicely (subcomplex inclusion)" and "the interval is contractible," which are precisely the geometric facts that make classical homotopy work. Recognizing that an abstract definition reduces to the familiar one in the prototype example is how you build trust that the abstract machinery is doing what you want.

**Left versus right homotopy is the cylinder-versus-path-space dichotomy, and in $\mathbf{Top}$ they are exponential transposes.** A left homotopy is a map *out of* $A \times [0,1]$; a right homotopy is a map *into* $B^{[0,1]}$; and the two carry the same information because $A \times [0,1] \to B$ and $A \to B^{[0,1]}$ are related by the product–hom adjunction (currying). This is the topological reason the coincidence theorem ($\simeq_\ell = \simeq_r$) holds, and it explains the abstract slogan from [[Def - Cylinder Object, Path Object, and Homotopy]] that a path object is a cylinder object in the opposite category. The transferable insight is that "homotopy as a path of maps" can always be packaged two ways — fattening the source or fattening the target — and which is convenient depends on whether the source is cofibrant or the target is fibrant.

**Cofibrancy of the domain corresponds to the CW hypothesis, and it is what guarantees the cylinder behaves.** Throughout, $A$ is taken to be a CW complex — which is exactly the cofibrancy condition in $\mathbf{Top}$ — and that hypothesis is used precisely where the subcomplex inclusion $A \times \{0,1\} \hookrightarrow A \times [0,1]$ must be a cofibration. For a general (non-CW) space the product with $[0,1]$ might fail to give a cofibration on the ends, and the abstract and classical homotopy relations could diverge in their formal behaviour. This concretizes the abstract requirement that left homotopy is well-behaved only on cofibrant domains: in $\mathbf{Top}$, "cofibrant" means "CW," and the CW hypothesis is doing exactly the work the abstract cofibrancy hypothesis does in [[Ex - Left homotopy is an equivalence relation on cofibrant objects]].
