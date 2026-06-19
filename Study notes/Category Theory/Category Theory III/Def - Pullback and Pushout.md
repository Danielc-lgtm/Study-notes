---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Product and Coproduct"
  - "Def - Equalizer and Coequalizer"
  - "Def - Commutative Diagram"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]]. A **cospan** is a pair of morphisms with common codomain, $A \xrightarrow{f} C \xleftarrow{g} B$; a **span** is a pair with common domain, $A \xleftarrow{f} C \xrightarrow{g} B$. The **pullback** (or **fibre product**) of a cospan is written $A \times_C B$, with projections $p_1 : A \times_C B \to A$ and $p_2 : A \times_C B \to B$. The **pushout** (or **amalgamated sum**) of a span is written $A +_C B$ (or $A \sqcup_C B$), with coprojections $i_1 : A \to A +_C B$, $i_2 : B \to A +_C B$. The full registry is on [[Category Theory III — Limits and Colimits]].

This is a compound page: it defines two interlocking notions — the **pullback** and the **pushout** — exact categorical duals, introduced together because each is the natural way to combine two objects over (resp. under) a third, and the pair is the workhorse of geometry (intersections, fibres, base change) and topology (gluing).

---

# Axiom Motivation

A product combines two objects with no relation between them. The pullback asks the more refined question: combine $A$ and $B$, but only the parts that are *compatible over* a shared object $C$. The motivating picture is again $\mathbf{Set}$. Given $f : A \to C$ and $g : B \to C$, the pullback is
$$A \times_C B = \{(a, b) \in A \times B : f(a) = g(b)\},$$
the subset of the product where the two elements have the *same image in $C$*. It is a product cut down by an equation, which already tells you it is a [[Def - Equalizer and Coequalizer|equalizer]] of a product — and indeed $A \times_C B = \mathrm{eq}(f \circ \pi_1,\ g \circ \pi_2)$ inside $A \times B$.

Why is this the right thing to want? Because "having the same image in $C$" is how almost every refined construction is phrased. If $g : B \hookrightarrow C$ is the inclusion of a subset, then $A \times_C B = f^{-1}(B)$ is the **preimage** — the pullback computes inverse images. If both $f$ and $g$ are inclusions of subsets of $C$, then $A \times_C B = A \cap B$ is the **intersection**. If $C = 1$ is terminal, the condition $f(a) = g(b)$ is vacuous and the pullback degenerates to the ordinary product $A \times B$ — so the product is the pullback over the terminal object. If $f : A \to C$ is a map and $c : 1 \to C$ picks a point, then $A \times_C 1$ is the **fibre** $f^{-1}(c)$. Preimage, intersection, fibre, product: these are not four constructions but one, parametrised by the cospan.

The universal property is read off the same way as for products. A map $z : Z \to A \times_C B$ into the pullback is the same as a pair of maps $z_1 : Z \to A$, $z_2 : Z \to B$ that *agree over $C$*, meaning $f \circ z_1 = g \circ z_2$. So we define the pullback abstractly as the universal object completing the cospan to a commuting square: an object $P$ with $p_1 : P \to A$, $p_2 : P \to B$ such that $f p_1 = g p_2$, through which every compatible pair factors uniquely. The commuting-square condition $f p_1 = g p_2$ is the abstract form of "same image in $C$"; uniqueness rules out slack exactly as for products.

Each clause of the universal property earns its place. **Existence** of the factorisation says the pullback is large enough to receive every compatible pair — it does not forget any solutions of $f(a) = g(b)$. **Uniqueness** says it has no redundancy, which (as for equalizers) is what makes the pullback of a [[Def - Isomorphism, Monomorphism, Epimorphism|monomorphism]] again a monomorphism — a fact that underlies the whole theory of subobjects and inverse images as functors. Drop uniqueness and "$f^{-1}(B)$" would no longer be a well-defined subobject; drop the square condition and you are back to the bare product, having thrown away the compatibility that was the entire point.

Now dualise. Reverse the arrows: a span $A \xleftarrow{f} C \xrightarrow{g} B$, and the universal object *under* it. This is the **pushout** $A +_C B$ — glue $A$ and $B$ together along their common part $C$. In $\mathbf{Set}$ it is the disjoint union $A \sqcup B$ with $f(c)$ and $g(c)$ identified for every $c \in C$: two copies of $C$ welded into one. This is *the* gluing construction. In $\mathbf{Top}$ it builds the sphere from two disks glued along their boundary circle, the torus from a square with edges identified, every cell complex. In $\mathbf{Grp}$ it is the amalgamated free product, the algebraic heart of the [[Thm - Seifert-van Kampen Theorem (Statement)|Seifert–van Kampen theorem]]. The pushout is to "gluing" what the pullback is to "intersection".

---

# The Definition

Let $A \xrightarrow{f} C \xleftarrow{g} B$ be a cospan in $\mathcal{C}$.

A **pullback** of $f$ and $g$ is an object $A \times_C B$ together with morphisms $p_1 : A \times_C B \to A$ and $p_2 : A \times_C B \to B$ satisfying $f \circ p_1 = g \circ p_2$, and universal: for every object $Z$ and pair $z_1 : Z \to A$, $z_2 : Z \to B$ with $f \circ z_1 = g \circ z_2$, there is a *unique* morphism $u : Z \to A \times_C B$ with $p_1 \circ u = z_1$ and $p_2 \circ u = z_2$. The resulting commuting square is called a **pullback square** or **cartesian square**:
$$
\begin{array}{ccc}
A \times_C B & \xrightarrow{\;p_2\;} & B \\
{\scriptstyle p_1}\big\downarrow & & \big\downarrow{\scriptstyle g} \\
A & \xrightarrow{\;f\;} & C
\end{array}
$$

Dually, for a span $A \xleftarrow{f} C \xrightarrow{g} B$, a **pushout** is an object $A +_C B$ with morphisms $i_1 : A \to A +_C B$, $i_2 : B \to A +_C B$ satisfying $i_1 \circ f = i_2 \circ g$, universal: for every $z_1 : A \to Z$, $z_2 : B \to Z$ with $z_1 \circ f = z_2 \circ g$, there is a *unique* $u : A +_C B \to Z$ with $u \circ i_1 = z_1$, $u \circ i_2 = z_2$.

The following are immediate and central:

- **The pullback of a monomorphism is a monomorphism.** If $g$ is monic, then $p_1$ is monic. (Dually, the pushout of an epimorphism is an epimorphism.)
- **Pasting lemma (two-pullbacks lemma).** In a diagram of two side-by-side squares
$$
\begin{array}{ccccc}
\bullet & \to & \bullet & \to & \bullet \\
\downarrow & & \downarrow & & \downarrow \\
\bullet & \to & \bullet & \to & \bullet
\end{array}
$$
if the right square is a pullback, then the left square is a pullback if and only if the outer rectangle is. In particular, if both inner squares are pullbacks, so is the outer rectangle: $A \times_C D \cong (A \times_B E) \times_E D$.

---

# Categorical / Structural Definition

The pullback is the [[Def - Limit and Colimit|limit]] of a cospan diagram and the pushout the colimit of a span. Let $J$ be the category $\bullet \to \bullet \leftarrow \bullet$ (three objects, two non-identity arrows into the middle). A functor $D : J \to \mathcal{C}$ is a cospan $A \to C \leftarrow B$, and a [[Def - Cone and Cocone|cone]] over it with apex $Z$ is a triple of maps to $A, B, C$ commuting with the diagram — but the leg to $C$ is forced to be $f \circ (Z \to A) = g \circ (Z \to B)$, so the data is exactly a compatible pair. The limit is the pullback. Dually, the span $\bullet \leftarrow \bullet \to \bullet$ has the pushout as its colimit.

The structural fact that makes pullbacks *constructible* rather than primitive: in a category with binary products and equalizers,
$$A \times_C B \;=\; \mathrm{eq}\big(\,f \circ \pi_1,\ g \circ \pi_2 : A \times B \rightrightarrows C\,\big),$$
the equalizer inside $A \times B$ of the two ways of reaching $C$. Conversely, products are pullbacks over the terminal object ($A \times B = A \times_1 B$) and equalizers are pullbacks of the diagonal. This circle of reductions is why "finite products and equalizers", "pullbacks and a terminal object", and "all finite limits" are three names for the same hypothesis (see [[Thm - Products and Equalizers Give All Limits]]).

There is also a slice-category reading: a pullback of $f : A \to C$ and $g : B \to C$ is exactly the product of the objects $f$ and $g$ in the slice category $\mathcal{C}/C$. Pulling back along a fixed $h : C' \to C$ defines a functor $h^* : \mathcal{C}/C \to \mathcal{C}/C'$, the **base change** functor — the abstract form of restricting a family to a sub-base.

---

# Relate to Other Fields / Compression

The pullback unifies preimage, intersection, fibre, and kernel-pair; the pushout unifies gluing, amalgamated free product, and connected sum. In $\mathbf{Set}$ the **kernel pair** of $f : A \to B$ is the pullback $A \times_B A = \{(a, a') : f(a) = f(a')\}$ — the equivalence relation "have the same image", whose coequalizer reconstructs $\mathrm{im}(f)$; this is the categorical engine of the first isomorphism theorem. In $\mathbf{Grp}$, the pushout of $C \to A$, $C \to B$ is the **amalgamated free product** $A *_C B$, the free product of $A$ and $B$ with the two images of $C$ identified.

**True name:** a pullback is "the object of compatible pairs over $C$"; a pushout is "$A$ and $B$ glued along $C$". When you see "preimage", "intersection", "fibre", "the part where two things agree on a base", reach for a pullback. When you see "glue", "attach", "amalgamate", "form by identifying", reach for a pushout.

---

# Examples / Corollaries

**Is an instance — pullbacks in $\mathbf{Set}$ as preimage and intersection.** With $g : B \hookrightarrow C$ the inclusion of a subset, $A \times_C B = \{(a, b) : f(a) = b\} \cong f^{-1}(B)$, the preimage of $B$ under $f$. With $f : A \hookrightarrow C$ and $g : B \hookrightarrow C$ both inclusions, $A \times_C B \cong A \cap B$. With $C = 1$ terminal, $A \times_1 B \cong A \times B$. These three special cases — preimage, intersection, product — are all the same pullback formula.

**Is an instance — the kernel of a homomorphism as a pullback.** For a group (or module) homomorphism $\varphi : G \to H$, the kernel $\ker\varphi$ is the pullback of $\varphi : G \to H$ along the inclusion of the trivial subgroup $\{e\} \hookrightarrow H$:
$$\ker\varphi = G \times_H \{e\} = \{g : \varphi(g) = e\}.$$
So "kernel" is "pullback along the inclusion of the basepoint", which is why kernels behave functorially and why the kernel is automatically a [[Def - Normal Subgroup|normal subgroup]] (the pullback of a normal subgroup is normal). See [[Ex - The kernel as a pullback]].

**Is an instance — pushouts in $\mathbf{Top}$ build spaces by gluing.** The sphere $S^2$ is the pushout of two disks $D^2 \leftarrow S^1 \rightarrow D^2$ glued along their boundary circle. The torus, Klein bottle, and every CW-complex arise as iterated pushouts attaching cells along their boundary spheres. The pushout carries the [[Def - Quotient Topology and Identification Map|quotient topology]] from $A \sqcup B$, which is exactly the universal property: a map out of the glued space is a pair of maps agreeing on the seam.

**Is an instance — pushouts in $\mathbf{Grp}$ and van Kampen.** If a space $X = U \cup V$ with $U, V, U \cap V$ path-connected, the [[Thm - Seifert-van Kampen Theorem (Statement)|Seifert–van Kampen theorem]] says $\pi_1(X)$ is the pushout (amalgamated free product) $\pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V)$. The topological pushout $U \sqcup_{U\cap V} V \approx X$ is carried by $\pi_1$ to the algebraic pushout — a functor preserving a colimit, which is striking because $\pi_1$ does *not* preserve colimits in general; van Kampen is the statement that it does for this particular gluing.

**Is NOT an instance — the ordinary union is not the pushout unless the maps are injective.** The pushout $A +_C B$ glues along the *images* of $C$, and if the structure maps $C \to A$, $C \to B$ are not injective the gluing identifies more than a naive union would. For $C = \{1, 2\}$, $A = B = \{*\}$ with both maps constant, the pushout is a single point (everything is identified), not a two-point set. The pushout respects the maps, not just the underlying sets.

**Is NOT an instance — a non-cartesian commuting square.** A commuting square $f p_1 = g p_2$ need not be a pullback: in $\mathbf{Set}$ take $C = \{*\}$, $A = B = P = \{*\}$ all singletons except $P = \emptyset$; the square commutes vacuously but $\emptyset$ is not the pullback (which is the singleton $A \times_C B = \{*\}$). Commuting is necessary but far from sufficient; the universal property must be checked.

**Calibration check.** Verify that $A \times_C B \cong B \times_C A$ (symmetry of the cospan); that pulling back along an isomorphism gives back an isomorphic object; and that in $\mathbf{Set}$ the kernel pair $A \times_B A$ of an injective $f$ is just the diagonal $\{(a,a)\}$. If you can also apply the pasting lemma to conclude that a "long rectangle" of two pullback squares is a pullback, you have the working tool.

---

# Unlocked by This

> [!note]- Algebraic geometry background
> A **commutative ring** is a set with $+, \times$ satisfying the usual laws and $xy = yx$. The **functor of points** view encodes a geometric object as a functor $X : \mathbf{CRing} \to \mathbf{Set}$, $R \mapsto X(R)$ = "the $R$-points of $X$". An **affine scheme** is a *representable* such functor, $\mathrm{Spec}\,R = \mathbf{CRing}(R, -)$, and $\mathrm{Spec} : \mathbf{CRing}^{op} \to \mathbf{AffSch}$ is the [[Def - The Yoneda Embedding|Yoneda embedding]], a fully faithful contravariant equivalence.
>
> Pullbacks are *the* construction of scheme theory. Because $\mathrm{Spec}$ is a Yoneda embedding it sends colimits of rings to limits of schemes; the coproduct of rings is the [[Def - Tensor Product of Modules|tensor product]], so
> $$\mathrm{Spec}(R_1 \otimes_S R_2) \;\cong\; \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2.$$
> The left side is the affine scheme of a tensor product of rings; the right side is the **fibre product of schemes** — a pullback. So the fibre product, which classically computes intersections of varieties, fibres of a morphism, and **base change** along $\mathrm{Spec}\,S' \to \mathrm{Spec}\,S$, is literally the categorical pullback you just defined, and it is computed by tensoring rings. Base change is the functor $- \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,S'$, the geometric face of $- \otimes_S S'$. This is the payoff developed on [[Ex - Fibre products of schemes are pullbacks]].

> [!tip] Descent and Stacks *(from Algebraic Geometry)*
> Iterated pullbacks of a cover form the **Čech nerve**, and gluing data satisfying a cocycle condition over its pullbacks is the content of **descent**; promoting "objects glued along a cover" to a functor valued in groupoids gives a **stack**. The pasting lemma and base-change functor $h^*$ are the basic moves of the whole theory.

> [!tip] Homotopy Pullbacks and Pushouts *(from Model Categories)*
> Strict pullbacks and pushouts are not homotopy-invariant; replacing them by **homotopy pullbacks / homotopy pushouts** (computed after fibrant/cofibrant replacement) is the starting point of **model categories** (Chapter VI) and the reason the mapping cone and homotopy fibre are the "right" gluing constructions in **derived** and **stable** settings.
