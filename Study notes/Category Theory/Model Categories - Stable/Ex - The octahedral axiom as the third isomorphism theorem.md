---
type: exercise
subject: model-categories
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Triangulated Category"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Module"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Work in the [[Def - Chain Map and Chain Homotopy|derived category]] $D(R)$ of a [[Def - Ring|ring]] $R$. Let $X \xrightarrow{f} Y \xrightarrow{g} Z$ be two composable injective [[Def - Chain Map and Chain Homotopy|chain maps]] of complexes of $R$-[[Def - Module|modules]] (concentrate everything in degree $0$ for intuition: $X, Y, Z$ ordinary modules with $f, g$ injective). The octahedral axiom TR4 produces, from the cofiber sequences of $f$, $g$, and $g \circ f$, a distinguished triangle
$$C(f) \to C(gf) \to C(g) \to \Sigma C(f).$$

(a) In the degree-$0$ case with $f, g$ injective, identify the cones $C(f) \simeq Y/X$, $C(g) \simeq Z/Y$, $C(gf) \simeq Z/X$ and show the octahedral triangle becomes the short exact sequence $0 \to Y/X \to Z/X \to Z/Y \to 0$.

(b) Apply $H_0 = [\,R, -\,]$ to the octahedral triangle and recover the **third isomorphism theorem** $(Z/X)\big/(Y/X) \cong Z/Y$ as the statement that the connecting maps vanish, i.e. as the exactness of the resulting long sequence.

**Recall:**

A distinguished triangle in $D(R)$ is a mapping-cone sequence $A \xrightarrow{h} B \to C(h) \to \Sigma A$, where $C(h)$ is the mapping cone, quasi-isomorphic to the cokernel $B/A$ when $h$ is an injection of modules in degree $0$. The octahedral axiom relates the cones of $f$, $g$, $gf$:

![[Def - Triangulated Category#The Definition]]

The third isomorphism theorem for modules: if $X \leq Y \leq Z$ are submodules then $(Z/X)/(Y/X) \cong Z/Y$.

---

# Convergent Strategy

**Problem class:** This is a "decode the abstract axiom in a concrete category" problem — the topic page's strategy of translating a triangulated statement into ordinary algebra, here making the octahedral axiom legible by specializing $D(R)$ to modules in degree $0$.

**Assumption pattern:** The injectivity of $f$ and $g$ is the key resource: it makes the mapping cones quasi-isomorphic to honest cokernels, so the octahedral triangle degenerates to a short exact sequence of quotient modules. Without injectivity the cones would carry genuine homology in two degrees and the picture would be the full derived statement.

**Theorem routing:** Identify the three cones with quotients ([[Def - Chain Map and Chain Homotopy|mapping cone]] $\simeq$ cokernel for an injection); read the octahedral triangle as $0 \to Y/X \to Z/X \to Z/Y \to 0$; then apply $H_0$ and use that this short exact sequence's long exact sequence (operation 2) is exact, which is exactly the third isomorphism theorem.

**Key decision point:** The non-obvious move is recognizing that $C(gf) \simeq Z/X$ is the *middle* term of the octahedral triangle, not an endpoint — the octahedron is built so that the cone of the composite sits between the cones of the factors. Misplacing $Z/X$ gives the wrong short exact sequence; the octahedral combinatorics dictate the order.

---

# Legal Operations Used

1. **Operation 6 from the topic page (use the octahedral axiom on a composite).** This exercise *is* the octahedral axiom, decoded: the composite $g \circ f$ generates the octahedron relating the three cones.

2. **Operation 5 from the topic page (replace by a cofiber sequence).** Used to identify each abstract cone with a concrete cokernel via the mapping-cone construction.

3. **Operation 2 from the topic page (apply a hom-functor for a long exact sequence).** Used in part (b): applying $H_0$ to the octahedral triangle gives the long exact sequence whose exactness is the third isomorphism theorem.

---

# Hints

> [!note]- Hint 1
> For an injection $h \colon A \hookrightarrow B$ of modules in degree $0$, the mapping cone $C(h)$ — the complex $\cdots \to 0 \to A \xrightarrow{h} B \to 0 \to \cdots$ with $A$ in degree $1$, $B$ in degree $0$ — has homology only in degree $0$, equal to $\mathrm{coker}(h) = B/A$. So in $D(R)$, $C(h) \simeq B/A$.

> [!note]- Hint 2
> Apply Hint 1 three times: $C(f) \simeq Y/X$, $C(g) \simeq Z/Y$, $C(gf) \simeq Z/X$ (since $gf \colon X \hookrightarrow Z$). Now write down the octahedral triangle $C(f) \to C(gf) \to C(g) \to \Sigma C(f)$ with these identifications.

> [!note]- Hint 3
> The octahedral triangle $Y/X \to Z/X \to Z/Y \to \Sigma(Y/X)$ with all objects concentrated in degree $0$ *is* a short exact sequence: a distinguished triangle of degree-$0$ objects with connecting map into a shift (degree $1$) is exact iff the connecting map is zero, which it is here because everything lives in degree $0$. Apply $H_0$ and read off the third isomorphism theorem.

---

# Solution

The plan: (a) collapse each cone to a cokernel using injectivity, then read the octahedral triangle as a short exact sequence of quotients; (b) apply $H_0$ and observe the resulting exactness is verbatim the third isomorphism theorem.

**Step 1 (part a): Each cone is a quotient module.**

> [!note]- Derivation
> For an injection $h \colon A \hookrightarrow B$ of modules placed in degree $0$, the mapping cone $C(h)$ is the two-term complex $A \xrightarrow{h} B$ with $A$ in homological degree $1$ and $B$ in degree $0$. Its homology is $H_1 = \ker h = 0$ (injectivity) and $H_0 = \mathrm{coker}\,h = B/A$. A complex with homology only in degree $0$ is quasi-isomorphic to that homology, so $C(h) \simeq B/A$ in $D(R)$. Applying this to $f \colon X \hookrightarrow Y$, $g \colon Y \hookrightarrow Z$, and $gf \colon X \hookrightarrow Z$:
> $$C(f) \simeq Y/X, \qquad C(g) \simeq Z/Y, \qquad C(gf) \simeq Z/X.$$

**Step 2 (part a): The octahedral triangle is the short exact sequence of quotients.**

> [!note]- Derivation
> The octahedral axiom (TR4) furnishes a distinguished triangle $C(f) \to C(gf) \to C(g) \to \Sigma C(f)$. Substituting Step 1's identifications,
> $$Y/X \xrightarrow{\ \bar f\ } Z/X \xrightarrow{\ \bar g\ } Z/Y \xrightarrow{\ \partial\ } \Sigma(Y/X),$$
> where $\bar f$ is induced by the inclusion $Y \hookrightarrow Z$ (sending $y + X \mapsto y + X$) and $\bar g$ by $Z/X \twoheadrightarrow Z/Y$ (sending $z + X \mapsto z + Y$). All four objects except $\Sigma(Y/X)$ live in degree $0$; the connecting map $\partial \colon Z/Y \to \Sigma(Y/X)$ lands in degree $1$, so it is the zero map (there are no nonzero degree-$0$-to-degree-$1$ maps between modules concentrated in their respective single degrees). A distinguished triangle with zero connecting map splits off as the short exact sequence
> $$0 \to Y/X \xrightarrow{\bar f} Z/X \xrightarrow{\bar g} Z/Y \to 0,$$
> exactly the short exact sequence of submodule quotients $X \leq Y \leq Z$.

**Step 3 (part b): Applying $H_0$ recovers the third isomorphism theorem.**

> [!note]- Derivation
> Apply $H_0 = [\,R, -\,]$ to the octahedral triangle; by operation 2 this gives a long exact sequence. Since the objects are concentrated in degree $0$, the long exact sequence collapses to
> $$0 \to Y/X \to Z/X \to Z/Y \to 0,$$
> exact (the higher and lower terms vanish). Exactness at $Z/X$ says $\bar g$ is surjective with kernel $\mathrm{im}\,\bar f = Y/X$ (the image of $Y/X$ in $Z/X$). The first isomorphism theorem applied to $\bar g \colon Z/X \to Z/Y$ then gives
> $$(Z/X)\big/(Y/X) \cong Z/Y,$$
> which is the third isomorphism theorem. So the octahedral axiom, decoded in $D(R)$ on degree-$0$ injections, *is* the third isomorphism theorem; in higher degrees and for non-injective maps it is the homotopy-coherent generalization, relating the cones of a composite to the cones of its factors.

> [!note]- Complete formal solution
> Place $X, Y, Z$ in homological degree $0$ with $f, g$ injective. For any injection $h \colon A \hookrightarrow B$ in degree $0$, the mapping cone $C(h) = [A \xrightarrow{h} B]$ ($A$ in degree $1$) has $H_1 = \ker h = 0$ and $H_0 = B/A$, so $C(h) \simeq B/A$ in $D(R)$. Hence $C(f) \simeq Y/X$, $C(g) \simeq Z/Y$, $C(gf) \simeq Z/X$.
>
> The octahedral triangle $C(f) \to C(gf) \to C(g) \to \Sigma C(f)$ becomes $Y/X \to Z/X \to Z/Y \to \Sigma(Y/X)$. The connecting map targets degree $1$ while its source is in degree $0$, so it vanishes, and the triangle is the short exact sequence $0 \to Y/X \to Z/X \to Z/Y \to 0$. Applying $H_0$ (operation 2) yields the same exact sequence; the first isomorphism theorem applied to the surjection $Z/X \twoheadrightarrow Z/Y$ with kernel $Y/X$ gives $(Z/X)/(Y/X) \cong Z/Y$, the third isomorphism theorem. $\blacksquare$

---

# Key Takeaways

**The octahedral axiom is the homotopy-coherent third isomorphism theorem: the cofiber of a composite is built from the cofibers of the factors.** Stripped of its intimidating eight-faced diagram, TR4 says exactly what $(Z/X)/(Y/X) \cong Z/Y$ says — quotienting in two stages equals quotienting all at once. The trigger to internalize: whenever you see two composable maps and want the cone of the composite, the octahedron tells you it sits between the cones of the factors, $C(f) \to C(gf) \to C(g)$, just as $Z/X$ sits between $Y/X$ and $Z/Y$. This is the single most useful intuition for TR4, which is otherwise the most opaque of the four axioms.

**Mapping cones generalize cokernels, and injectivity is what collapses the cone back to a plain quotient.** The bridge that makes the whole exercise work is "cone of an injection $\simeq$ cokernel." In the derived category the cone is the *homotopy-invariant* replacement for the cokernel — it exists for *every* map, not just injections, and it remembers the kernel as homology in the next degree. The transferable diagnostic: when a map fails to be injective, do not take its cokernel — take its cone, which records both kernel and cokernel and produces the correct long exact sequence. This is the reflex that converts naive abelian-category arguments into correct derived-category ones.

**Decoding an abstract axiom in a familiar category is the fastest route to understanding it, and the right familiar category here is $D(R)$ in degree $0$.** The general lesson for studying triangulated categories — and abstract structures generally — is to specialize until the axiom becomes a theorem you already know. Here, specializing $D(R)$ to ordinary modules turned the octahedron into the third isomorphism theorem, an undergraduate fact. The same move (specialize, recognize the classical shadow, then re-abstract) decodes the long exact sequence as the snake lemma, the rotation sign as $\partial^2 = 0$, and the whole triangulated apparatus as derived-category homological algebra. When an axiom is opaque, find the degree-$0$ corner where it is something you learned years ago.
