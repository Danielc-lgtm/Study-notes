---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Product and Coproduct"
  - "Def - Homotopy"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a model category; $A, B, X$ are objects and $f, g : A \to B$ are parallel maps. We write $A \sqcup A$ for the coproduct of $A$ with itself, with coproduct inclusions $\mathrm{in}_0, \mathrm{in}_1 : A \to A \sqcup A$, and $\nabla : A \sqcup A \to A$ for the **fold map** (the identity on each summand, induced by $\mathrm{id}_A$ on both). Dually $B \times B$ is the product with projections $\mathrm{pr}_0, \mathrm{pr}_1$ and $\Delta : B \to B \times B$ the **diagonal**. Trivial fibrations are written $\xrightarrow{\sim}\twoheadrightarrow$, trivial cofibrations $\xrightarrow{\sim}\rightarrowtail$. The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

This is a compound page: it defines four interlocking notions — the **cylinder object**, the **path object**, **left homotopy**, and **right homotopy** — because the cylinder and path object are the abstract scaffolding on which the two homotopy relations are built, and the two relations only become a single equivalence relation when both pieces are present and the objects are bifibrant.

---

# Axiom Motivation

The goal is to define "two maps $f, g : A \to B$ are homotopic" in a category that has no notion of "continuous path of maps" to fall back on. In $\mathbf{Top}$ a homotopy is a continuous map $H : A \times [0,1] \to B$ with $H|_{A \times \{0\}} = f$ and $H|_{A \times \{1\}} = g$. The data is: an object that "interpolates between two copies of $A$," and a map out of it restricting to $f$ and $g$ at the ends. The cylinder object is the abstraction of $A \times [0,1]$, and a left homotopy is the abstraction of $H$.

So the first question is: what *is* the cylinder $A \times [0,1]$, categorically? It comes with two inclusions of $A$ (the two ends $A \times \{0\}$ and $A \times \{1\}$), which assemble into a map $A \sqcup A \to A \times [0,1]$; and it comes with a projection $A \times [0,1] \to A$ collapsing the interval, which is a homotopy equivalence. So $A \times [0,1]$ factors the fold map $A \sqcup A \xrightarrow{\nabla} A$ (the map that is the identity on each end) as "include the two ends, then collapse." The cylinder object is the abstraction of exactly this factorization. Why demand the first factor be a *cofibration* and the second a *weak equivalence*? The weak equivalence is because the cylinder must have the same homotopy type as $A$ — collapsing the interval must not change anything up to homotopy. The cofibration is the subtler requirement: it ensures the two ends are "well-embedded," which is what makes homotopy *extendable* and ultimately what makes the homotopy relation transitive. Drop the cofibration condition and you can still define a relation, but it fails to be transitive on general objects — gluing two cylinders need not produce a cylinder.

Now the dual question. There is a second, *a priori different* way to say $f$ and $g$ are homotopic: instead of a map *out of* a fattened $A$, use a map *into* a fattened $B$. A path object $\mathrm{Path}(B)$ abstracts the space $B^{[0,1]}$ of paths in $B$: it factors the diagonal $B \xrightarrow{\Delta} B \times B$ (the map recording a point as a constant path) as a weak equivalence followed by a fibration. A right homotopy is a map $A \to \mathrm{Path}(B)$ whose two projections are $f$ and $g$. The reason to define both is that left homotopy is well-behaved when the *domain* $A$ is cofibrant, and right homotopy when the *codomain* $B$ is fibrant — the cofibration in the cylinder lives over $A$, the fibration in the path object lives over $B$. Neither relation alone is symmetric and transitive on general objects.

The resolution — and the reason both definitions are needed — is the coincidence theorem: **when $A$ is cofibrant and $B$ is fibrant, left homotopy and right homotopy coincide, and the common relation is an equivalence relation.** This is exactly why the homotopy category is built from bifibrant objects: bifibrancy is the precise hypothesis under which "homotopic" is unambiguous and well-behaved. If you tried to define homotopy classes on all objects, the relation would not be an equivalence relation and $\pi(A,B)$ would not exist. The bifibrancy hypothesis is forced by the demand that homotopy be an equivalence relation.

---

# The Definition

Let $\mathcal{M}$ be a model category, $A, B$ objects, and $f, g : A \to B$ parallel maps.

**Cylinder object.** A **cylinder object** for $A$ is a factorization of the fold map $\nabla : A \sqcup A \to A$ as
$$A \sqcup A \;\xrightarrow{\ (\mathrm{i}_0,\, \mathrm{i}_1)\ }\; \mathrm{Cyl}(A) \;\xrightarrow{\ \sigma\ }\; A,$$
where $(\mathrm{i}_0, \mathrm{i}_1)$ is a cofibration and $\sigma$ is a weak equivalence, with $\sigma \circ (\mathrm{i}_0, \mathrm{i}_1) = \nabla$. The maps $\mathrm{i}_0 = (\mathrm{i}_0, \mathrm{i}_1) \circ \mathrm{in}_0$ and $\mathrm{i}_1 = (\mathrm{i}_0, \mathrm{i}_1) \circ \mathrm{in}_1$ are the two **end inclusions** $A \to \mathrm{Cyl}(A)$.

**Left homotopy.** A **left homotopy** from $f$ to $g$ is a map $H : \mathrm{Cyl}(A) \to B$, for some cylinder object $\mathrm{Cyl}(A)$, with
$$H \circ \mathrm{i}_0 = f \qquad \text{and} \qquad H \circ \mathrm{i}_1 = g.$$
We say $f$ and $g$ are **left homotopic**, written $f \simeq_\ell g$, if such an $H$ exists.

**Path object.** A **path object** for $B$ is a factorization of the diagonal $\Delta : B \to B \times B$ as
$$B \;\xrightarrow{\ \rho\ }\; \mathrm{Path}(B) \;\xrightarrow{\ (\mathrm{p}_0,\, \mathrm{p}_1)\ }\; B \times B,$$
where $\rho$ is a weak equivalence and $(\mathrm{p}_0, \mathrm{p}_1)$ is a fibration, with $(\mathrm{p}_0, \mathrm{p}_1) \circ \rho = \Delta$. The maps $\mathrm{p}_0, \mathrm{p}_1 : \mathrm{Path}(B) \to B$ are the two **endpoint evaluations**.

**Right homotopy.** A **right homotopy** from $f$ to $g$ is a map $K : A \to \mathrm{Path}(B)$, for some path object, with
$$\mathrm{p}_0 \circ K = f \qquad \text{and} \qquad \mathrm{p}_1 \circ K = g.$$
We say $f$ and $g$ are **right homotopic**, written $f \simeq_r g$, if such a $K$ exists.

**Homotopy and homotopy classes.** We say $f$ and $g$ are **homotopic**, written $f \simeq g$, if they are both left and right homotopic. The fundamental fact (proved on [[Ex - Left homotopy is an equivalence relation on cofibrant objects]] and its dual) is:

> If $A$ is **cofibrant**, then $\simeq_\ell$ is an equivalence relation on $\mathcal{M}(A, B)$, and a left homotopy can be taken to use the functorial cylinder. Dually, if $B$ is **fibrant**, $\simeq_r$ is an equivalence relation. If $A$ is cofibrant and $B$ is fibrant, then $f \simeq_\ell g \iff f \simeq_r g$, and this common relation $\simeq$ is an equivalence relation.

For bifibrant $A, B$ we write $\pi(A, B) = \mathcal{M}(A, B)/\!\simeq$ for the set of **homotopy classes** of maps.

---

# Relate to Other Fields / Compression

The cylinder/path duality is a perfect instance of the dualization principle: a path object for $B$ in $\mathcal{M}$ is *exactly* a cylinder object for $B$ in the opposite model category $\mathcal{M}^{op}$, and a right homotopy in $\mathcal{M}$ is a left homotopy in $\mathcal{M}^{op}$. So one only ever proves theorems about cylinders and left homotopy; the path-object and right-homotopy versions come free by passing to $\mathcal{M}^{op}$ (see [[Ex - The opposite of a model category]]). This halving of labour is the structural payoff of the dual definitions.

In topology the abstraction is faithful: $\mathrm{Cyl}(A) = A \times [0,1]$ is a cylinder object (the end inclusions $A \to A \times [0,1]$ form a cofibration when $A$ is a CW complex, and the projection is a homotopy equivalence), and $\mathrm{Path}(B) = B^{[0,1]}$, the space of paths with the compact-open topology, is a path object (the constant-path inclusion is a homotopy equivalence and the endpoint-evaluation $(p_0, p_1)$ is a Serre fibration). A left homotopy is then literally a [[Def - Homotopy|homotopy]] $A \times [0,1] \to B$, and a right homotopy is its exponential transpose $A \to B^{[0,1]}$ — the same homotopy, viewed as a path of maps. The coincidence $\simeq_\ell = \simeq_r$ is the topological tautology that a homotopy and its transpose carry the same information.

In $\mathbf{Ch}(R)$, a cylinder object for a complex $C$ produces, for a map of complexes, precisely the data of a [[Def - Chain Map and Chain Homotopy|chain homotopy]]: $f \simeq g$ in the model-categorical sense recovers "$f - g$ is a boundary," i.e. $f - g = d \circ s + s \circ d$ for a degree-$+1$ map $s$. The abstract homotopy relation specializes to chain homotopy, which is why $\mathrm{Ho}(\mathbf{Ch}(R))$ is the derived category.

**True name:** a left homotopy is **"a map out of a fattened source,"** a right homotopy is **"a map into a fattened target,"** and they agree exactly when the source is cofibrant (so the fattening embeds well) and the target is fibrant (so the fattening lifts well).

---

# Examples / Corollaries

**Is an instance — the topological cylinder.** For a CW complex $A$, the space $A \times [0,1]$ with end inclusions and interval-collapse is a cylinder object, and a left homotopy $A \times [0,1] \to B$ is an ordinary homotopy. See [[Ex - Homotopy in spaces recovers the usual notion]].

**Is an instance — the path space.** For any space $B$, the path space $B^{[0,1]}$ is a path object; a right homotopy $A \to B^{[0,1]}$ assigns to each point of $A$ a path in $B$ from $f$ to $g$, the transpose of an ordinary homotopy.

**Is an instance — chain homotopy.** In $\mathbf{Ch}(R)$, model-categorical homotopy of chain maps $f, g : C \to D$ is exactly the existence of a [[Def - Chain Map and Chain Homotopy|chain homotopy]] $s$ with $f - g = ds + sd$.

**Is NOT an instance — left homotopy without cofibrancy can fail symmetry.** On a non-cofibrant object the relation $\simeq_\ell$ need not be symmetric: a left homotopy from $f$ to $g$ uses $\mathrm{i}_0 \mapsto f$, $\mathrm{i}_1 \mapsto g$, and reversing requires a cylinder symmetry $\mathrm{Cyl}(A) \to \mathrm{Cyl}(A)$ swapping the ends, whose existence and weak-equivalence property rely on $\mathrm{i}_0, \mathrm{i}_1$ being trivial cofibrations — which holds when $A$ is cofibrant (then $\mathrm{i}_0$ is a trivial cofibration by 2-out-of-3) but can fail otherwise. This is the concrete reason the equivalence-relation theorem requires cofibrancy.

**Is NOT an instance — distinct maps can be homotopic.** Homotopy is coarser than equality: in $\mathbf{Top}$, any two maps into a contractible space $B$ are homotopic, so $\pi(A, B)$ is a single point even when $\mathcal{M}(A,B)$ is large. Homotopy classes deliberately forget more than isomorphism, which is the whole point of passing to $\mathrm{Ho}(\mathcal{M})$.

**Calibration check.** Verify that the cylinder object is *not* unique — the functorial one $A \times I$ and any other are related by a weak equivalence compatible with the structure maps. Verify that if $A$ is cofibrant then the end inclusion $\mathrm{i}_0 : A \to \mathrm{Cyl}(A)$ is a trivial cofibration (use that $A \to A \sqcup A \to \mathrm{Cyl}(A)$, that $\sigma \mathrm{i}_0 = \mathrm{id}_A$, and 2-out-of-3). If you can also explain why $f \simeq_\ell g$ for cofibrant $A$ forces $f$ and $g$ to become equal in $\mathrm{Ho}(\mathcal{M})$ — because $\sigma$ is inverted there and $\mathrm{i}_0, \mathrm{i}_1$ become equal once $\sigma$ is invertible — you have understood the link to the homotopy category.

---

# Unlocked by This

> [!tip] The Homotopy Category of a Model Category *(from this chapter)*
> The homotopy classes $\pi(A,B)$ defined here are the morphisms of $\mathrm{Ho}(\mathcal{M})$ on bifibrant objects: [[Thm - The Homotopy Category of a Model Category]] proves $\mathrm{Ho}(\mathcal{M})(X,Y) \cong \pi(QRX, QRY)$. The cylinder/path machinery is what gives the localization its concrete description.

> [!tip] Homotopy Groups via Spheres and Loops *(from Algebraic Topology)*
> Iterating cylinders builds suspensions and iterating path objects builds loop spaces; the homotopy classes $[\Sigma^n A, B] \cong [A, \Omega^n B]$ are the abstract form of the suspension–loop adjunction, and $\pi_n(B) = \pi(S^n, B)$ recovers **homotopy groups** as homotopy classes of maps out of spheres.
