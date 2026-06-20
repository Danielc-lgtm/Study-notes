---
type: definition
subject: model-categories
prereqs:
  - "Def - Reedy Category and the Reedy Model Structure"
  - "Def - Simplicial Set"
  - "Def - Cylinder Object, Path Object, and Homotopy"
  - "Def - Model Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a [[Def - Model Category|model category]] and $X$ an object of $\mathcal{M}$. The simplex category $\Delta$ has objects $[n] = \{0 < 1 < \cdots < n\}$; a **cosimplicial object** in $\mathcal{M}$ is a [[Def - Functor|functor]] $X^{\bullet} : \Delta \to \mathcal{M}$, written $[n] \mapsto X^n$, and a **simplicial object** is a functor $X_{\bullet} : \Delta^{op} \to \mathcal{M}$, written $[n] \mapsto X_n$. The constant cosimplicial object at $X$ is $c X$ (every $X^n = X$, every structure map the identity). We write $L_n$ and $M_n$ for the [[Def - Reedy Category and the Reedy Model Structure|latching and matching]] objects in the Reedy structure on $\mathcal{M}^{\Delta}$ or $\mathcal{M}^{\Delta^{op}}$, and $\Delta^n = \Delta(-,[n])$ for the standard $n$-simplex in [[Def - Simplicial Set|sSet]]. The symbol $\otimes$ denotes a tensoring of $\mathcal{M}$ over $\mathbf{sSet}$ (when one exists) and $(-)^{(-)}$ the cotensoring. The full symbol registry is on [[Model Categories — Framings and Function Complexes]].

This is a compound page: it defines two dual notions — the **cosimplicial frame** (a cosimplicial resolution of $X$) and the **simplicial frame** (a simplicial resolution) — because they are dual halves of one structure (a frame for $X$ uses the cosimplicial frame on the source side and the simplicial frame on the target side), and neither is fully usable without the other when computing [[Def - Homotopy Function Complex|homotopy function complexes]].

---

# Axiom Motivation

Here is the entire idea in one sentence: a cosimplicial frame on $X$ is a homotopically correct version of the formula "$X \otimes \Delta^{\bullet}$," manufactured even when $\mathcal{M}$ has no actual tensoring over simplicial sets. To see why anyone would want such a thing, recall what goes right in a **simplicial model category** — one that is genuinely enriched, tensored, and cotensored over [[Def - Simplicial Set|sSet]]. There, the mapping object $\underline{\mathrm{Map}}(X, Y) \in \mathbf{sSet}$ is built in, the tensor $X \otimes K$ for a simplicial set $K$ exists, and the homotopy theory of mapping spaces is immediate. Most model categories one meets — chain complexes, arbitrary localizations, exotic algebraic ones — are *not* simplicial in this strict sense. The question is: can every model category be made to behave, *up to homotopy*, as if it were tensored and cotensored over $\mathbf{sSet}$? Framings are the affirmative answer.

Start from the pieces of a tensoring we cannot do without. If $\mathcal{M}$ were tensored over $\mathbf{sSet}$, then for each object $X$ we would have a cosimplicial object $[n] \mapsto X \otimes \Delta^n$. Its degree-$0$ piece is $X \otimes \Delta^0 = X$. Its degree-$1$ piece is $X \otimes \Delta^1$, which is a **cylinder object** on $X$ — because $\Delta^1$ is the interval and tensoring with the interval is exactly what a cylinder is (see [[Def - Cylinder Object, Path Object, and Homotopy]]). Higher pieces $X \otimes \Delta^n$ are higher cylinders encoding higher homotopies. So a cosimplicial object that *looks like* $X \otimes \Delta^{\bullet}$ should: sit over the constant object $cX$ (i.e. its degree-$0$ term is $X$ and the augmentation $X^{\bullet} \to cX$ collapses everything to $X$); have its degree-$1$ term be a cylinder on $X$; and more generally interpolate $X$ with all its iterated cylinders coherently. A **cosimplicial frame** is precisely a cosimplicial object with these properties, packaged correctly.

The "packaged correctly" is the crux, and it is where the Reedy machinery from [[Def - Reedy Category and the Reedy Model Structure]] enters. We must say what "coherently interpolates" means without circular reference to a tensoring we do not have. The answer: demand the cosimplicial object be **Reedy cofibrant**, and demand its augmentation to $cX$ be a weak equivalence in the appropriate sense. Reedy cofibrancy says each latching map $L_n X^{\bullet} \to X^n$ is a cofibration — concretely, that each new level genuinely *attaches a free homotopy cell* over what the lower levels forced, rather than collapsing information. This is exactly the condition that makes $X^1$ a *bona fide* cylinder object (the latching map $L_1 X^{\bullet} = X \sqcup X \to X^1$ being a cofibration is the cylinder's cofibration condition $A \sqcup A \rightarrowtail \mathrm{Cyl}(A)$). Without Reedy cofibrancy you can still write down *a* cosimplicial object over $cX$, but its levels need not be cylinders and it computes garbage; with it, every level is the homotopically right object.

Why a *whole cosimplicial object* and not just a single cylinder? Because a single cylinder computes only $\pi(X,Y)$, the set of homotopy classes — the $\pi_0$ of the mapping space. To recover the entire homotopy type of the derived mapping space $\mathrm{map}(X,Y)$ — all its higher homotopy groups, the higher homotopies between homotopies — you need cylinders on cylinders on cylinders, organized simplicially. The simplicial direction is exactly the direction in which "homotopies between homotopies" are recorded; that is what $\Delta$ is *for*. A frame is the minimal coherent system of all iterated cylinders, and the simplicial identities are what make the system coherent.

Now the dual. Everything above used cylinders (maps *out of* fattened sources), which compute homotopy when the source is cofibrant. To compute when the *target* is fibrant you need path objects (maps *into* fattened targets), and the dual gadget is a **simplicial frame** on $Y$: a simplicial object $[n] \mapsto Y_n$ with $Y_0 = Y$, each $Y_1$ a path object, Reedy *fibrant* (matching maps are fibrations), augmented from the constant simplicial object $cY$ by a weak equivalence. A simplicial frame is "$Y^{\Delta^{\bullet}}$" — the cotensoring — built up to homotopy. The reason both are needed is the same reason left and right homotopy both appear in [[Def - Cylinder Object, Path Object, and Homotopy]]: a cosimplicial frame on $X$ handles the variance of $\mathrm{map}(-,Y)$ in $X$, and a simplicial frame on $Y$ handles the variance of $\mathrm{map}(X,-)$ in $Y$, and they must agree in the middle — which they do, up to homotopy, by [[Thm - Framings Compute Homotopy Function Complexes]].

Could a reader invent this? Yes: want a homotopy mapping space; notice a single cylinder only gives $\pi_0$; realize you need all iterated cylinders organized simplicially; demand Reedy cofibrancy so each level is a genuine cylinder; dualize to path objects for the fibrant side. The definition writes itself once you ask for "$X \otimes \Delta^{\bullet}$ done homotopically."

---

# The Definition

Let $\mathcal{M}$ be a model category and $X, Y$ objects.

**Cosimplicial frame.** A **cosimplicial frame** on $X$ is a cosimplicial object $X^{\bullet} : \Delta \to \mathcal{M}$ together with an augmentation (a map of cosimplicial objects to the constant object) $X^{\bullet} \to cX$, such that:

1. $X^{\bullet}$ is **[[Def - Reedy Category and the Reedy Model Structure|Reedy cofibrant]]** in $\mathcal{M}^{\Delta}$ — each latching map $L_n X^{\bullet} \to X^n$ is a cofibration in $\mathcal{M}$;
2. the augmentation induces a weak equivalence $X^0 \xrightarrow{\sim} X$ (so the degree-$0$ term is a model of $X$), and more strongly every structure map $X^m \to X^n$ along a map $[m] \to [n]$ in $\Delta$ is a weak equivalence — equivalently, $X^{\bullet} \to cX$ is a Reedy weak equivalence onto the constant frame's underlying homotopy type.

Equivalently and more memorably: a cosimplicial frame is a Reedy-cofibrant cosimplicial object all of whose coface and codegeneracy maps are weak equivalences, with $X^0 \simeq X$. Such an object is also called a **cosimplicial resolution** of $X$.

**Simplicial frame.** Dually, a **simplicial frame** on $Y$ is a simplicial object $Y_{\bullet} : \Delta^{op} \to \mathcal{M}$ with a coaugmentation $cY \to Y_{\bullet}$ such that:

1. $Y_{\bullet}$ is **[[Def - Reedy Category and the Reedy Model Structure|Reedy fibrant]]** in $\mathcal{M}^{\Delta^{op}}$ — each matching map $Y_n \to M_n Y_{\bullet}$ is a fibration in $\mathcal{M}$;
2. the coaugmentation induces a weak equivalence $Y \xrightarrow{\sim} Y_0$, and every structure map is a weak equivalence.

Such a $Y_{\bullet}$ is a **simplicial resolution** of $Y$.

**Framing of a model category.** A **framing** on $\mathcal{M}$ is a functorial choice, for every object, of a cosimplicial frame and a simplicial frame, compatible in the sense that the degree-zero data agree and the two resolutions of any object are related by the framing's structure maps. (Hovey constructs a framing on any model category; one may also work with non-functorial frames object by object, since the homotopy invariants do not depend on the choice — see below.)

The key low-degree readings: $X^0 \simeq X$ and $X^1$ is a **cylinder object** for $X$ (in the sense of [[Def - Cylinder Object, Path Object, and Homotopy]]); dually $Y_0 \simeq Y$ and $Y_1$ is a **path object** for $Y$.

---

# Categorical / Structural Definition

Structurally, a frame is a *cofibrant (resp. fibrant) replacement of the constant diagram*, taken in the Reedy model structure. Consider the constant-diagram functor $c : \mathcal{M} \to \mathcal{M}^{\Delta}$, $X \mapsto cX$. A cosimplicial frame on $X$ is a Reedy-cofibrant object $X^{\bullet}$ with a Reedy weak equivalence $X^{\bullet} \xrightarrow{\sim} cX$ — that is, a **cofibrant replacement of $cX$ in $\mathcal{M}^{\Delta}$** whose underlying object in degree $0$ is identified with (a model of) $X$. Dually a simplicial frame is a fibrant replacement of $cY$ in $\mathcal{M}^{\Delta^{op}}$. So "frame" $=$ "Reedy (co)fibrant replacement of the constant diagram," and the existence of frames is just the existence of (co)fibrant replacements in the Reedy structure, which is [[Thm - Diagrams over a Reedy Category Form a Model Category]].

This makes precise the slogan that *framings make $\mathcal{M}$ tensored and cotensored over $\mathbf{sSet}$ up to homotopy*. Given a frame $X^{\bullet}$ and a finite simplicial set $K$, one defines $X \otimes K$ by the coend $\int^{[n] \in \Delta} K_n \cdot X^n$ (a colimit weighted by $K$), and dually $Y^K = \int_{[n]} (Y_n)^{K_n}$. With a frame in place these coend/end formulas land in the right homotopy type, recovering the structure of a simplicial model category at the level of the homotopy category even when $\mathcal{M}$ carries no strict $\mathbf{sSet}$-tensoring. The adjunction $\mathrm{map}(X, Y) \cong$ "$Y^{(-)}$ evaluated against $X^{\bullet}$" is what produces the homotopy function complex of the next page.

---

# Relate to Other Fields / Compression

A frame is a **simplicial resolution in the sense of homological algebra, run in the homotopical setting.** In homological algebra one resolves a module by a complex of projectives so that derived functors compute correctly; here one resolves an object $X$ by a cosimplicial object of "free homotopy cells" so that *derived mapping spaces* compute correctly. The Dold–Kan correspondence makes this exact in the additive case: for $\mathcal{M} = \mathbf{Ch}_{\ge 0}(R)$, a simplicial resolution corresponds under Dold–Kan to a projective resolution, and the homotopy function complex computes $\mathrm{Ext}$.

**True name:** a cosimplicial frame is "**all the iterated cylinders of $X$, organized simplicially and made Reedy cofibrant**," equivalently "**the homotopically meaningful version of $X \otimes \Delta^{\bullet}$**." A simplicial frame is the path-object dual, "**$Y^{\Delta^{\bullet}}$**." The single fact to remember: *level $1$ is a cylinder (resp. path object); the rest of the levels exist to record higher homotopies coherently.*

The relationship to enrichment is the cleanest compression. A **simplicial model category** has a strict tensoring $X \otimes K$ and cotensoring $Y^K$ over $\mathbf{sSet}$ satisfying Quillen's axiom SM7. A framing manufactures these *up to homotopy* for any $\mathcal{M}$: it is the device that says "you do not need to be a simplicial model category to have homotopy mapping spaces — every model category already has them, you just have to resolve." This is why framings are foundational: they free homotopy theory from the requirement of strict simplicial enrichment.

---

# Examples / Corollaries

**Is an instance — the canonical frame in a simplicial model category.** If $\mathcal{M}$ is already tensored/cotensored over $\mathbf{sSet}$ and $X$ is cofibrant, then $X^{\bullet} = X \otimes \Delta^{\bullet}$ (the genuine tensoring with the standard simplices) is a cosimplicial frame: it is Reedy cofibrant because $\Delta^{\bullet}$ is Reedy cofibrant in $\mathbf{sSet}$ and SM7 turns this into Reedy cofibrancy of $X \otimes \Delta^{\bullet}$, and each structure map is a weak equivalence because each $\Delta^n$ is contractible. Dually $Y_{\bullet} = Y^{\Delta^{\bullet}}$ is a simplicial frame on a fibrant $Y$. So framings *recover* the strict structure when it is present — they extend, not replace, simplicial enrichment.

**Is an instance — chain complexes.** In $\mathbf{Ch}_{\ge 0}(R)$ a cosimplicial frame on a cofibrant complex $C$ produces, via Dold–Kan, the data computing $\mathrm{map}(C, D)$ whose homotopy groups are $\mathrm{Ext}^{-n}_R(H_*C, H_*D)$-style invariants; the level-$1$ cylinder is the mapping cylinder of $C$, and the chain homotopies of [[Def - Chain Map and Chain Homotopy|chain homotopy]] are exactly the level-$1$ homotopy data. This is the precise sense in which framings generalize "resolve to compute derived functors."

**Is an instance — the constant frame is usually NOT a frame.** The constant cosimplicial object $cX$ (all $X^n = X$) satisfies condition (2) trivially (all structure maps are identities, hence weak equivalences) but **fails Reedy cofibrancy** unless $X$ is very special: the latching map $L_1(cX) = X \sqcup X \to X$ is the fold map $\nabla$, which is a cofibration only when $X$ has a strict cylinder of itself — generically it is not. So the naive "just take the constant object" does not frame; one must genuinely resolve. This is the single most instructive non-example, because it shows Reedy cofibrancy is doing real work.

**Is NOT a frame — a Reedy cofibrant cosimplicial object whose structure maps are not equivalences.** Take any Reedy cofibrant $X^{\bullet}$ in which a coface $X^0 \to X^1$ fails to be a weak equivalence (for example a genuinely $1$-dimensional cosimplicial object that does not collapse). It satisfies condition (1) but violates (2): it does not *resolve* a single object, it is a non-trivial cosimplicial homotopy type. A frame must be "homotopically constant" — every structure map a weak equivalence — so that it really is a fattened-up copy of one object $X$, not a genuine diagram.

**Corollary — level $1$ is a cylinder/path object.** For any cosimplicial frame $X^{\bullet}$, the two cofaces $d^0, d^1 : X^0 \to X^1$ together with the codegeneracy $s^0 : X^1 \to X^0$ exhibit $X^1$ as a cylinder object on $X^0 \simeq X$: the map $(d^0, d^1) : X^0 \sqcup X^0 \to X^1$ is the latching map at degree $1$ (a cofibration by Reedy cofibrancy) and $s^0$ is a weak equivalence by condition (2). This is the corollary that ties frames back to [[Def - Cylinder Object, Path Object, and Homotopy]].

**Calibration check.** Verify that for a frame $X^{\bullet}$, the augmentation forces $X^0 \simeq X$ and that $L_0 X^{\bullet} = \varnothing$, so Reedy cofibrancy at degree $0$ says exactly that $X^0$ is cofibrant. Check that the constant object $cX$ fails to be a frame by computing its degree-$1$ latching map and observing it is the fold map $X \sqcup X \to X$, not generally a cofibration. If you can also explain why a simplicial frame on $Y$ is a cosimplicial frame on $Y$ in $\mathcal{M}^{op}$, you have understood the duality.

---

# Unlocked by This

> [!tip] Homotopy Function Complexes *(from this chapter)*
> Given a cosimplicial frame $X^{\bullet}$ on $X$ and a fibrant $Y$, the simplicial set $[n] \mapsto \mathcal{M}(X^n, Y)$ is the [[Def - Homotopy Function Complex|homotopy function complex]] $\mathrm{map}(X, Y)$ — the derived mapping space. Frames are the device that produces it; [[Thm - Framings Compute Homotopy Function Complexes]] proves it is well-defined and frame-independent.

> [!tip] Every Model Category is a Homotopical sSet-Module *(from Model Categories)*
> Framings upgrade any model category $\mathcal{M}$ to one tensored and cotensored over $\mathbf{sSet}$ **up to homotopy**, with $X \otimes K$ and $Y^K$ given by coend/end formulas over the frame. This is the structural reason mapping *spaces* (not just mapping *sets*) exist in every homotopy theory.

> [!tip] Derived Mapping Spaces and ∞-Categories *(from Higher Category Theory)*
> The homotopy function complex a frame computes is the **mapping space** $\mathrm{Map}_{\mathcal{M}[\mathcal{W}^{-1}]}(X, Y)$ of the underlying **∞-category** presented by $\mathcal{M}$. Framings are the point-set device that extracts the $\infty$-categorical hom-space from a model category, the same role the **Dwyer–Kan simplicial localization** plays from the other direction.
