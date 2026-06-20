---
type: definition
subject: model-categories
prereqs:
  - "Def - Cosimplicial and Simplicial Frame"
  - "Def - Simplicial Set"
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Def - Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a [[Def - Model Category|model category]] with homotopy category $\mathrm{Ho}(\mathcal{M}) = \mathcal{M}[\mathcal{W}^{-1}]$, and $X, Y$ are objects. We write $QX$ for a cofibrant replacement and $RY$ for a fibrant replacement (see [[Def - Cofibrant and Fibrant Objects]]). A [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] on $X$ is written $X^{\bullet} : \Delta \to \mathcal{M}$ (with $X^0 \simeq X$), and a [[Def - Cosimplicial and Simplicial Frame|simplicial frame]] on $Y$ is written $Y_{\bullet} : \Delta^{op} \to \mathcal{M}$. The category of [[Def - Simplicial Set|simplicial sets]] is $\mathbf{sSet}$ with homotopy category $\mathrm{Ho}(\mathbf{sSet})$; $\pi_0$ and $\pi_n$ denote (simplicial) homotopy groups. The bracket $[X, Y]$ denotes the set of morphisms $\mathrm{Ho}(\mathcal{M})(X, Y)$. We write $\mathrm{map}(X, Y) \in \mathrm{Ho}(\mathbf{sSet})$ for the homotopy function complex. The full symbol registry is on [[Model Categories — Framings and Function Complexes]].

---

# Axiom Motivation

The homotopy category $\mathrm{Ho}(\mathcal{M})$ throws away too much. Its hom-*set* $[X, Y]$ records the homotopy classes of maps from $X$ to $Y$ — but a *class* is a $\pi_0$, and by collapsing to classes we have discarded all the higher structure: the homotopies between homotopic maps, the homotopies between *those*, and so on. Two maps can be homotopic in essentially-unique ways or in wildly many ways, and $[X, Y]$ cannot tell the difference. The homotopy function complex is the object that remembers all of it: a **space** (a simplicial set) $\mathrm{map}(X, Y)$ whose set of path components is exactly $[X, Y]$, and whose higher homotopy groups record the higher homotopies. The motivating demand is: *upgrade the hom-set $[X,Y]$ to a hom-space.*

Why should one expect such a space to exist, and what should its simplices be? Think about what a $1$-simplex in $\mathrm{map}(X, Y)$ ought to be: a path between two maps, i.e. a **homotopy** $f \simeq g$. We already know how to encode a homotopy — as a map out of a [[Def - Cylinder Object, Path Object, and Homotopy|cylinder object]] $\mathrm{Cyl}(X) \to Y$, or equivalently a map $X^1 \to Y$ where $X^1$ is the degree-$1$ part of a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]]. A $2$-simplex should be a homotopy between homotopies, encoded by a map $X^2 \to Y$. The pattern is forced: the $n$-simplices of the mapping space should be the maps $X^n \to Y$ out of the degree-$n$ part of a frame. In other words,
$$\mathrm{map}(X, Y)_n \;=\; \mathcal{M}(X^n, Y).$$
This is a simplicial set automatically: a cosimplicial object $X^{\bullet}$ contravariantly applied to the corepresentable $\mathcal{M}(-, Y)$ is a simplicial set, with faces and degeneracies coming from the cofaces and codegeneracies of the frame. The frame is exactly the device that produces the higher simplices we needed.

Now the two requirements that make this *correct* rather than merely defined. First, $Y$ must be **fibrant**, and the frame on $X$ must be a genuine frame (Reedy cofibrant, homotopically constant). This is the same combination of cofibrancy-on-the-source and fibrancy-on-the-target that made the homotopy relation an equivalence relation in [[Def - Cylinder Object, Path Object, and Homotopy]]: with $X^{\bullet}$ Reedy cofibrant and $Y$ fibrant, every horn in $\mathrm{map}(X,Y)$ can be filled, so $\mathrm{map}(X,Y)$ is a **Kan complex** — a fibrant simplicial set, hence a legitimate homotopy type. Drop fibrancy of $Y$ and the higher simplices fail to compose; drop Reedy cofibrancy of the frame and the level-$1$ "homotopies" are not genuine homotopies. The two conditions are not decoration; they are what make the simplicial set a space.

Second — and this is the subtle point that the whole subject turns on — the construction must not depend on the *choice* of frame. There are many cosimplicial frames on a given $X$ (frames are cofibrant replacements, which are unique only up to weak equivalence). If $\mathrm{map}(X,Y)$ depended on which frame we picked, it would be a useless invariant. The demand that the answer be well-defined in $\mathrm{Ho}(\mathbf{sSet})$ — the same simplicial homotopy type regardless of frame — is the real content, and it is exactly what [[Thm - Framings Compute Homotopy Function Complexes]] establishes. Once it holds, $\mathrm{map}(X,Y)$ becomes a *bifunctor* into $\mathrm{Ho}(\mathbf{sSet})$, the derived hom of the homotopy theory.

Could a reader invent this? Yes: ask for a hom-*space* refining the hom-*set*; realize $1$-simplices must be homotopies and $n$-simplices iterated homotopies; recognize that a cosimplicial frame is precisely a coherent supply of those iterated homotopies; apply the corepresentable $\mathcal{M}(-,Y)$ to it; and impose fibrancy/cofibrancy to make the result a Kan complex. The definition is the unique sensible one.

---

# The Definition

Let $\mathcal{M}$ be a model category and $X, Y$ objects.

**Via a cosimplicial frame.** Choose a [[Def - Cosimplicial and Simplicial Frame|cosimplicial frame]] $X^{\bullet}$ on a cofibrant model of $X$ and a fibrant model $RY$ of $Y$. The **homotopy function complex** (or **derived mapping space**, or **homotopy mapping space**) is the simplicial set
$$\mathrm{map}^{\ell}(X, Y) \;:=\; \mathcal{M}(X^{\bullet}, RY), \qquad \mathrm{map}^{\ell}(X, Y)_n = \mathcal{M}(X^n, RY),$$
with faces and degeneracies induced by the codegeneracies and cofaces of the frame.

**Via a simplicial frame.** Dually, choose a [[Def - Cosimplicial and Simplicial Frame|simplicial frame]] $Y_{\bullet}$ on a fibrant model of $Y$ and a cofibrant model $QX$ of $X$. The simplicial set
$$\mathrm{map}^{r}(X, Y) \;:=\; \mathcal{M}(QX, Y_{\bullet}), \qquad \mathrm{map}^{r}(X, Y)_n = \mathcal{M}(QX, Y_n)$$
is the homotopy function complex computed on the target side.

**Well-definedness.** When $X$ is cofibrant and $Y$ is fibrant, both simplicial sets are **Kan complexes**, and there is a natural zig-zag of weak equivalences
$$\mathrm{map}^{\ell}(X, Y) \;\xleftarrow{\sim}\; \mathrm{diag}\,\mathcal{M}(X^{\bullet}, Y_{\bullet}) \;\xrightarrow{\sim}\; \mathrm{map}^{r}(X, Y),$$
so both define the **same** object $\mathrm{map}(X, Y) \in \mathrm{Ho}(\mathbf{sSet})$, independent of the chosen frames. The two-variable object $[n] \mapsto \mathcal{M}(X^n, Y_n)$ here is the **bisimplicial set** of the framing, and its diagonal mediates the two one-sided constructions. This is the content of [[Thm - Framings Compute Homotopy Function Complexes]].

**Defining properties.** The homotopy function complex satisfies:
$$\pi_0\,\mathrm{map}(X, Y) \;\cong\; [X, Y] = \mathrm{Ho}(\mathcal{M})(X, Y),$$
its path components recover the homotopy classes; and for $n \ge 1$, $\pi_n(\mathrm{map}(X,Y), f)$ records the **higher homotopies** at a fixed $f$. It is functorial: $\mathrm{map}(-, -) : \mathrm{Ho}(\mathcal{M})^{op} \times \mathrm{Ho}(\mathcal{M}) \to \mathrm{Ho}(\mathbf{sSet})$.

---

# Categorical / Structural Definition

The structural meaning is that $\mathrm{map}(X, Y)$ is the **derived hom-functor** of the homotopy theory $\mathcal{M}$ — the homotopical refinement of $\mathrm{Hom}$. Just as a derived functor $\mathbf{L}F$ resolves the source before applying $F$, the homotopy function complex resolves $X$ by a frame (a homotopical resolution) before applying $\mathcal{M}(-, Y)$, and the simplicial direction of the frame is what makes the output a *space* rather than a set. In the totally formal picture: $\mathcal{M}$ presents an **(∞,1)-category** $\mathcal{M}[\mathcal{W}^{-1}]$ (its underlying ∞-category obtained by inverting the weak equivalences), and
$$\mathrm{map}(X, Y) \;\simeq\; \mathrm{Map}_{\mathcal{M}[\mathcal{W}^{-1}]}(X, Y)$$
is its **mapping space** — the hom-object of the ∞-category. The homotopy function complex is the point-set-computable model of this intrinsic mapping space; framings are the computation.

Three constructions of $\mathrm{map}(X,Y)$ coincide up to weak equivalence, and it is worth knowing they all agree, because each is convenient in a different context:

- **Framings** (this page): resolve $X$ cosimplicially or $Y$ simplicially. Best when $\mathcal{M}$ is a general model category with no extra structure.
- **The Dwyer–Kan simplicial localization** $L^H \mathcal{M}$: form the hammock localization and take its hom-simplicial-set $L^H\mathcal{M}(X,Y)$. Best for the conceptual statement that $\mathrm{map}$ is the ∞-categorical hom.
- **The simplicial mapping object** $\underline{\mathrm{Map}}(QX, RY)$ when $\mathcal{M}$ is a **simplicial model category**. Best when the strict enrichment is present; framings reduce to this case.

That these agree is the theorem that the homotopy function complex is an *invariant of the homotopy theory*, not of any presentation of it.

---

# Relate to Other Fields / Compression

The homotopy function complex is **"$\mathrm{Hom}$ with all its higher homotopies kept,"** the homotopical analogue of the derived hom $\mathbf{R}\mathrm{Hom}$ in homological algebra. In $\mathbf{Ch}(R)$ the homotopy function complex of two complexes is (under Dold–Kan) the truncation of $\mathbf{R}\mathrm{Hom}(M, N)$, whose homotopy groups are the $\mathrm{Ext}$ groups: $\pi_n \mathrm{map}(M, N) = \mathrm{Ext}^{-n}_R(M, N)$ in the appropriate range. So "homotopy function complex" is to "$\mathrm{Hom}$ of objects" as "$\mathbf{R}\mathrm{Hom}$" is to "$\mathrm{Hom}$ of modules" — it is the total derived functor of the hom, organized as a space.

**True name:** the homotopy function complex is "**the derived mapping space**" — a Kan complex with $\pi_0 = [X,Y]$ and higher $\pi_n$ = higher homotopies — and operationally, "**$\mathcal{M}(X^{\bullet}, Y)$ for a cosimplicial frame $X^{\bullet}$ and fibrant $Y$.**" The single fact to internalize: *$\pi_0$ is the homotopy classes; the rest is what the homotopy category forgot.*

The compression against ordinary topology: for $\mathcal{M} = \mathbf{Top}$ (or $\mathbf{sSet}$) with $X$ a CW complex and $Y$ any space, the homotopy function complex is weakly equivalent to the **mapping space** $\mathrm{Map}(X, Y)$ with the compact-open topology (resp. the simplicial mapping object). So framings reconstruct, in any model category, the thing that in topology was free — the space of maps, not just its set of components. This is the entire payoff: every homotopy theory has mapping spaces, computed by resolving with frames.

---

# Examples / Corollaries

**Is an instance — mapping spaces in $\mathbf{Top}$.** For CW $X$ and any $Y$, $\mathrm{map}(X, Y) \simeq \mathrm{Sing}\,\mathrm{Map}(X, Y)$, the singular complex of the topological mapping space. Its $\pi_0$ is $[X, Y]$ (free homotopy classes), and $\pi_n(\mathrm{map}(X,Y), f) = \pi_n(\mathrm{Map}(X,Y), f)$ records homotopies of homotopies. The frame here is the genuine $X \otimes \Delta^{\bullet} = X \times |\Delta^{\bullet}|$.

**Is an instance — function complexes in $\mathbf{sSet}$.** For Kan complexes $X, Y$, the homotopy function complex is the internal hom $Y^X$, $\;(Y^X)_n = \mathbf{sSet}(X \times \Delta^n, Y)$, using the frame $X \times \Delta^{\bullet}$. This is the model in which "mapping space" is most transparent: $n$-simplices are maps from $X$ times the $n$-simplex.

**Is an instance — derived hom in $\mathbf{Ch}(R)$.** For complexes $M, N$ with $M$ cofibrant (degreewise projective) and $N$ fibrant, $\pi_n \mathrm{map}(M, N) \cong H_n \mathbf{R}\mathrm{Hom}(M, N)$, recovering $\mathrm{Ext}$ groups. The homotopy function complex *is* the space-level packaging of $\mathbf{R}\mathrm{Hom}$.

**Is NOT the right object — $\mathcal{M}(X, Y)$ for non-bifibrant $X, Y$.** The naive hom-set $\mathcal{M}(X, Y)$ (before resolving) is not the homotopy function complex and not even a homotopy invariant: replacing $X$ by a weakly equivalent object changes $\mathcal{M}(X, Y)$ arbitrarily. One *must* resolve — cofibrantly replace $X$ (or frame it) and fibrantly replace $Y$ — before the hom carries homotopical meaning. This is the same lesson as: derived functors require resolutions.

**Is NOT the right object — the discrete simplicial set on $[X, Y]$.** It is tempting to "promote" the hom-set $[X, Y]$ to a simplicial set by taking it discrete (only $0$-simplices). This has the correct $\pi_0$ but trivial higher homotopy, so it discards exactly the higher-homotopy information the function complex exists to record. The homotopy function complex is discrete *only* when $\mathcal{M}$ is a $1$-category up to homotopy (e.g. an ordinary category with the trivial model structure), which is precisely the degenerate case.

**Corollary — $\pi_0$ recovers the homotopy category.** Applying $\pi_0$ to $\mathrm{map}(-, -)$ recovers the hom-functor of $\mathrm{Ho}(\mathcal{M})$: $\pi_0 \mathrm{map}(X, Y) = [X, Y]$. So the homotopy function complex is a strict enrichment of $\mathrm{Ho}(\mathcal{M})$ over $\mathrm{Ho}(\mathbf{sSet})$, refining the ordinary homotopy category into a "homotopy theory enriched in spaces."

**Calibration check.** Verify that $\pi_0 \mathrm{map}(X, Y) = [X, Y]$ directly from the definition: a $0$-simplex of $\mathcal{M}(X^{\bullet}, RY)$ is a map $X^0 \to RY$ (a map $X \to Y$ up to the chosen models), and a $1$-simplex $X^1 \to RY$ is exactly a homotopy between two such, since $X^1$ is a cylinder object. Confirm that $\mathrm{map}(X, Y)$ is a Kan complex requires $Y$ fibrant by recalling that horn-filling against $Y$ is the lifting property that fibrancy supplies. If you can also explain why the bisimplicial diagonal mediates the cosimplicial and simplicial computations, you have understood frame-independence.

---

# Unlocked by This

> [!tip] Mapping Spaces of ∞-Categories *(from Higher Category Theory)*
> The homotopy function complex is the **mapping space** $\mathrm{Map}_{\mathcal{C}}(X, Y)$ of the **∞-category** $\mathcal{C} = \mathcal{M}[\mathcal{W}^{-1}]$ presented by $\mathcal{M}$. In the quasi-category model this is the hom-Kan-complex; in the **complete Segal space** model it is the appropriate fibre. Framings are how one computes ∞-categorical hom-spaces from a strict model.

> [!tip] Homotopy Groups of Spaces of Maps *(from Algebraic Topology)*
> Taking $\mathcal{M} = \mathbf{Top}$, the homotopy function complex is the mapping space, and its homotopy groups are the homotopy groups of spaces of maps — the objects studied in obstruction theory, the **Federer spectral sequence**, and the computation of $\pi_*(\mathrm{Map}(X,Y))$. The function complex is the home of all "space of sections / space of maps" computations.

> [!tip] Derived Hom and Ext *(from Homological Algebra)*
> For chain complexes the homotopy function complex packages **$\mathbf{R}\mathrm{Hom}$** as a space, with $\pi_n \mathrm{map}(M,N) = \mathrm{Ext}^{-n}(M,N)$. This is the bridge to **derived categories** and **derived functors**: the homotopy function complex is the universal derived hom, and the **derived category** is its homotopy-category shadow.
