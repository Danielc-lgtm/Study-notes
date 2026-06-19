---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Limit and Colimit"
  - "Def - Pullback and Pushout"
  - "Def - Quillen Adjunction and Quillen Equivalence"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a model category, $J$ is a small **indexing category**, and $\mathcal{M}^J$ is the category of $J$-shaped diagrams in $\mathcal{M}$ ([[Def - Functor|functors]] $J \to \mathcal{M}$). The ordinary colimit and limit are the left and right adjoints $\mathrm{colim}, \lim : \mathcal{M}^J \to \mathcal{M}$ of the constant-diagram functor $\Delta : \mathcal{M} \to \mathcal{M}^J$. We write $\mathrm{hocolim}$ and $\mathrm{holim}$ for the homotopy colimit and limit. For a span $B \leftarrow A \to C$, the **homotopy pushout** is denoted $B \cup^{h}_A C$; $\Sigma X$ denotes the (unreduced) suspension. The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

This is a motivational page: its purpose is to explain *why* ordinary limits and colimits must be corrected for homotopy theory, and to define the correction self-containedly. The general theory is the derived-functor machinery of [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]].

---

# Axiom Motivation

The motivating defect is sharp and worth stating before anything else: **ordinary colimits are not homotopy-invariant.** A construction is homotopy-invariant if replacing its input by a weakly equivalent input gives a weakly equivalent output. The colimit fails this badly. Here is the canonical example. Consider the pushout (colimit of a span) $* \leftarrow X \to *$ in $\mathbf{Top}$, collapsing $X$ to a point on each side. The strict pushout is a single point. Now replace one of the maps $X \to *$ by a weakly equivalent map — say, replace the target $*$ by a contractible space $C$ that $X$ maps into by an inclusion. The two diagrams $* \leftarrow X \to *$ and $C \leftarrow X \to *$ are objectwise weakly equivalent, but their strict pushouts are a point and the cone on $X$ respectively, which are not weakly equivalent in general. The strict colimit *sees* the difference between weakly equivalent diagrams, which is exactly what a homotopy-invariant construction must not do.

The reason is structural and you have already met it: the colimit functor $\mathrm{colim} : \mathcal{M}^J \to \mathcal{M}$ is a *left adjoint* (to the constant-diagram functor), and left adjoints respect weak equivalences only on cofibrant objects. A diagram is "cofibrant" in the diagram model structure on $\mathcal{M}^J$ when its maps are sufficiently like cofibrations — a span $B \leftarrow A \to C$ is cofibrant when both legs are cofibrations and the objects are cofibrant. The pushout of such a *cofibrant* span *is* homotopy-invariant. So the fix is the universal one from [[Def - Cofibrant and Fibrant Objects]]: replace the diagram by a cofibrant one, then take the strict colimit. This is the homotopy colimit, and it is just $\mathrm{colim}$ with a cofibrant-replacement step bolted on the front — the total left derived functor $\mathbf{L}\,\mathrm{colim}$.

The concrete recipe for the homotopy pushout makes this vivid. To compute the homotopy pushout of $B \xleftarrow{f} A \xrightarrow{g} C$, you do not take the strict pushout (which glues $B$ and $C$ along $A$ rigidly); instead you replace one leg by a cofibration first. Topologically, factor $g : A \to C$ through the **mapping cylinder** $A \times [0,1] \cup_g C$ — glue a cylinder on $A$ to $C$ along the end $A \times \{1\}$ — which makes the leg an honest inclusion, and *then* glue to $B$. The result is the **double mapping cylinder**, the "thickened" pushout where $B$ and $C$ are joined by a tube of length one rather than identified. When both maps are $A \to *$, this double mapping cylinder is exactly the (unreduced) **suspension** $\Sigma A$ — two cones on $A$ glued along $A$. So the homotopy pushout of $* \leftarrow X \to *$ is $\Sigma X$, not a point: the homotopically correct answer remembers $X$, whereas the strict colimit forgets it.

Everything dualizes. The limit functor is a *right adjoint*, respects weak equivalences only on fibrant diagrams, and the homotopy limit is $\lim$ after fibrant replacement — the total right derived functor $\mathbf{R}\lim$. The homotopy pullback of $* \to Y \leftarrow *$ is the **loop space** $\Omega Y$, the fibrant correction of the strict pullback (a point). The pattern is one you should now expect: a (co)limit fails to be homotopy-invariant precisely because it is a (left/right) adjoint, and the fix is precisely (cofibrant/fibrant) replacement.

---

# The Definition

Let $\mathcal{M}$ be a model category and $J$ a small category. The category $\mathcal{M}^J$ of $J$-diagrams carries a model structure (the **projective** or **injective** model structure) with objectwise weak equivalences. The **homotopy colimit** and **homotopy limit** are the total derived functors of the strict colimit and limit:
$$\mathrm{hocolim}_J = \mathbf{L}\,\mathrm{colim}_J : \mathrm{Ho}(\mathcal{M}^J) \to \mathrm{Ho}(\mathcal{M}), \qquad \mathrm{holim}_J = \mathbf{R}\lim_J : \mathrm{Ho}(\mathcal{M}^J) \to \mathrm{Ho}(\mathcal{M}).$$
Concretely, to compute $\mathrm{hocolim}_J D$ for a diagram $D : J \to \mathcal{M}$, replace $D$ by a (projectively) cofibrant diagram $QD$ — one whose latching maps are cofibrations and whose objects are cofibrant — and take the strict colimit:
$$\mathrm{hocolim}_J D \;\simeq\; \mathrm{colim}_J (QD).$$
Dually, $\mathrm{holim}_J D \simeq \lim_J (RD)$ for a fibrant replacement $RD$.

**Homotopy pushout.** For a span $B \xleftarrow{f} A \xrightarrow{g} C$, the **homotopy pushout** $B \cup^h_A C$ is the homotopy colimit over the span category $\bullet \leftarrow \bullet \to \bullet$. It is computed by factoring one leg as a cofibration — say replace $g$ by a cofibration $A \rightarrowtail C'$ with $C' \xrightarrow{\sim} C$ — and forming the strict pushout
$$B \cup^h_A C \;=\; B \sqcup_A C' \;=\; \mathrm{colim}\big( B \xleftarrow{f} A \rightarrowtail C' \big),$$
provided $A, B, C$ are cofibrant. In $\mathbf{Top}$ this is the **double mapping cylinder** $B \sqcup_A (A \times [0,1]) \sqcup_A C$. The **homotopy pullback** is dual.

---

# Relate to Other Fields / Compression

The homotopy (co)limit is the universal example of the slogan "**every derived construction is an ordinary construction with a replacement step.**" Ordinary colimit, plus cofibrant replacement of the diagram, equals homotopy colimit; ordinary limit, plus fibrant replacement, equals homotopy limit. This is literally the same mechanism as the derived tensor product ($\otimes$ after projective resolution gives $\mathbf{Tor}$) and the total derived functors of [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] — because $\mathrm{colim}$ and $\lim$ *are* the left and right adjoints to the constant-diagram functor, so their derived functors are instances of the general theory.

In homological algebra the homotopy colimit of a filtered diagram is the *derived* colimit, and its failure to agree with the strict colimit is measured by the $\varprojlim^1$ and higher **derived limit** terms — the $\lim^1$ exact sequence you may have met is the first sign that limits need deriving. The homotopy pushout's correction term, in the abelian setting, becomes the connecting maps of a long exact sequence: the Mayer–Vietoris sequence is the long exact sequence of a homotopy pushout, and it is exact precisely because the *homotopy* pushout, not the strict one, is used.

**True name:** a homotopy colimit is **"the colimit that does not change when you wiggle the diagram up to weak equivalence,"** computed as $\mathrm{colim}$ after making the diagram cofibrant; the suspension and the cone are its simplest non-trivial values.

---

# Examples / Corollaries

**Is an instance — the suspension as a homotopy pushout.** The homotopy pushout of $* \leftarrow X \to *$ is the unreduced suspension $\Sigma X$. Replacing each leg $X \to *$ by the cofibration $X \hookrightarrow CX$ into the cone $CX = X \times [0,1] / (X \times \{1\})$, the strict pushout $CX \cup_X CX$ glues two cones along $X$, which is $\Sigma X$. For $X = S^n$ this gives $\Sigma S^n = S^{n+1}$, recovering the spheres.

**Is an instance — the loop space as a homotopy pullback.** The homotopy pullback of $* \to Y \leftarrow *$ (both maps picking the basepoint) is the based loop space $\Omega Y$. Replacing one map by the path-fibration $\mathrm{Path}_*(Y) \twoheadrightarrow Y$ of paths starting at the basepoint, the strict pullback is the space of paths starting and ending at the basepoint — loops.

**Is an instance — the mapping cone.** The homotopy pushout of $* \leftarrow X \xrightarrow{f} Y$ is the mapping cone $C_f = Y \cup_f CX$, the construction that fits into the cofibre sequence $X \to Y \to C_f$. In $\mathbf{Ch}(R)$ this is the algebraic mapping cone, the source of the distinguished triangles of the derived category.

**Is NOT an instance — the strict pushout of $* \leftarrow X \to *$.** The strict pushout is a single point, which is *not* the homotopy pushout (that is $\Sigma X$). This is the defining counterexample: the strict colimit collapses all of $X$, the homotopy colimit remembers it as a suspension. Whenever you see a span with a leg that is not a cofibration, the strict and homotopy colimits will generally differ.

**Is NOT an instance — homotopy limit is not the strict limit of a non-fibrant diagram.** The strict pullback of a cospan $B \to D \leftarrow C$ in which neither map is a fibration can fail to be homotopy-invariant: replacing $D$ by a weakly equivalent object can change it. The homotopy pullback replaces a map by a fibration first; only then does the answer respect weak equivalences.

**Calibration check.** Verify that if one leg of a span $B \leftarrow A \to C$ is *already* a cofibration (and the objects are cofibrant), then the strict pushout equals the homotopy pushout — no correction is needed because the diagram is already cofibrant. Verify that the homotopy pushout of $A \xleftarrow{\mathrm{id}} A \to C$ is just $C$ (one leg is an identity, hence a cofibration up to weak equivalence). If you can explain why $\Sigma X$, not a point, is the right answer for $* \leftarrow X \to *$ — because the homotopy colimit must not depend on the strict equality the maps to $*$ impose — you have understood the definition.

---

# Unlocked by This

> [!tip] Spectral Sequences from Homotopy Colimits *(from Algebraic Topology)*
> The homotopy colimit of a complicated diagram is computed by a **spectral sequence** (the Bousfield–Kan spectral sequence), whose $E_2$-page is the derived functors of the strict colimit. This is how homotopy (co)limits are calculated in practice, and it generalizes the $\lim^1$ exact sequence.

> [!tip] Distinguished Triangles and Triangulated Categories *(from Homological Algebra)*
> Homotopy pushouts of the form $* \leftarrow X \to Y$ (mapping cones) generate the **distinguished triangles** that make $\mathrm{Ho}$ of a stable model category a **triangulated category**. The cofibre and fibre sequences are the homotopy-pushout and homotopy-pullback squares with one corner the zero object.

> [!tip] Homotopy Colimits as Geometric Constructions *(from Higher Category Theory)*
> In the ∞-categorical world, the homotopy colimit *is* the colimit — there is no "strict versus derived" distinction, because ∞-categories only know homotopy-invariant constructions. Model-categorical homotopy (co)limits are the point-set presentations of the genuine **∞-categorical (co)limits** of the [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories|Higher Categories]] chapter.
