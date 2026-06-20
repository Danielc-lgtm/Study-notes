---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Opetopic Set"
  - "Def - Limit and Colimit"
  - "Def - Presheaf"
  - "Def - Pullback and Pushout"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Show that the category of [[Def - Opetopic Set|opetopic sets]] $\mathbf{Set}^{\mathbb{O}^{op}}$ is cocomplete, with all [[Def - Limit and Colimit|colimits]] computed **pointwise**: for a diagram $D : \mathcal{J} \to \mathbf{Set}^{\mathbb{O}^{op}}$, the colimit satisfies $(\varinjlim_j D_j)_O = \varinjlim_j (D_j)_O$ for every opetope $O$. As a concrete consequence, describe the [[Def - Pullback and Pushout|pushout]] that glues two opetopic sets along a shared sub-cell — for instance, gluing two arity-$2$ standard cells $\mathbf{y}O$ along a shared boundary arrow — and confirm the gluing is performed cell-by-cell.

**Recall:**

![[Def - Opetopic Set#The Definition]]

A [[Def - Opetopic Set|opetopic set]] is a [[Def - Presheaf|presheaf]] $X : \mathbb{O}^{op} \to \mathbf{Set}$. A [[Def - Limit and Colimit|colimit]] of a diagram is its universal cocone; a [[Def - Pullback and Pushout|pushout]] is the colimit of a span $A \leftarrow C \to B$, the universal object receiving $A$ and $B$ agreeing on $C$. "Pointwise" means the colimit is formed separately in $\mathbf{Set}$ at each object $O$ and these assemble into a presheaf.

---

# Convergent Strategy

**Problem class:** This is an *inherit-a-structural-theorem-from-the-presheaf-setting* problem — a structural-world problem. The goal is to recognise that cocompleteness of opetopic sets is not special to opetopes but is the general fact that presheaf categories are cocomplete with pointwise colimits, and then to instantiate the pushout concretely.

**Assumption pattern:** The assumption is that opetopic sets form a presheaf category $[\mathbb{O}^{op}, \mathbf{Set}]$ and that $\mathbf{Set}$ is cocomplete. These two facts, plus the universal property of colimits, force the pointwise formula — no opetope-specific input is needed. Recognising "this is the general functor-category cocompleteness theorem" is the whole move.

**Theorem routing:** We route through the general fact that a functor category $[\mathcal{C}, \mathcal{E}]$ inherits all (co)limits that $\mathcal{E}$ has, computed pointwise (a corollary of the universal property of colimits and the way [[Def - Natural Transformation|natural transformations]] are evaluated). We instantiate at $\mathcal{C} = \mathbb{O}^{op}$, $\mathcal{E} = \mathbf{Set}$, and then compute one [[Def - Pullback and Pushout|pushout]] explicitly.

**Key decision point:** The non-obvious choice is to verify the *universal property* pointwise rather than to guess the colimit object: define $(\varinjlim D)_O := \varinjlim (D_j)_O$ and check it satisfies the colimit universal property in $\mathbf{Set}^{\mathbb{O}^{op}}$, using that natural transformations out of it are determined pointwise. The tempting error is to build a colimit by some global construction and hope it is pointwise; the clean route is to *define* it pointwise and verify universality.

---

# Legal Operations Used

1. **Operation 3 (take the presheaf on a shape category)** from the topic page. Opetopic sets are presheaves on $\mathbb{O}$, so the general presheaf cocompleteness theorem applies; the entire result is this inheritance.

2. **Operation 4 (invoke Yoneda to turn a cell into a representable)** from the topic page, used to phrase the gluing of standard cells $\mathbf{y}O$ along a shared boundary as a pushout of representables.

---

# Hints

> [!note]- Hint 1
> Recall the general theorem: for any category $\mathcal{C}$ and cocomplete $\mathcal{E}$, the functor category $[\mathcal{C}, \mathcal{E}]$ is cocomplete and colimits are computed pointwise. Opetopic sets are $[\mathbb{O}^{op}, \mathbf{Set}]$, and $\mathbf{Set}$ is cocomplete.

> [!note]- Hint 2
> To prove the pointwise formula, *define* $P_O := \varinjlim_j (D_j)_O$ for each $O$, make $P$ a presheaf using functoriality of colimits in $\mathbf{Set}$, and verify $P$ has the colimit universal property by checking that a map $P \to X$ is the same as a compatible cocone, which is checked at each $O$.

> [!note]- Hint 3
> For the pushout: glue two arity-$2$ standard cells $\mathbf{y}O$ along the shared boundary arrow $\mathbf{y}(\text{arrow})$, i.e. take the pushout of $\mathbf{y}O \leftarrow \mathbf{y}(\text{arrow}) \to \mathbf{y}O$. By pointwise computation, at each opetope $O'$ the result is the pushout of sets, which identifies the two copies of the shared arrow and keeps everything else disjoint.

---

# Solution

The route is to instantiate the general functor-category cocompleteness theorem at $\mathbb{O}^{op}$, prove the pointwise formula by verifying the universal property at each opetope, and then compute one concrete pushout cell-by-cell.

**Step 1: Define the candidate colimit pointwise.**

> [!note]- Derivation
> Let $D : \mathcal{J} \to \mathbf{Set}^{\mathbb{O}^{op}}$ be a diagram of [[Def - Opetopic Set|opetopic sets]]. For each opetope $O$, the evaluation $D_{(-)}(O) : \mathcal{J} \to \mathbf{Set}$, $j \mapsto (D_j)_O$, is a diagram of sets; since $\mathbf{Set}$ is cocomplete, it has a colimit. Define
> $$P_O \;:=\; \varinjlim_{j \in \mathcal{J}} (D_j)_O.$$
> For a face map $\alpha : O' \to O$, the restrictions $(D_j)(\alpha) : (D_j)_O \to (D_j)_{O'}$ are natural in $j$, so by functoriality of the colimit they induce a function $P(\alpha) : P_O \to P_{O'}$, and these make $P$ a presheaf $\mathbb{O}^{op} \to \mathbf{Set}$, i.e. an opetopic set.

**Step 2: Verify the colimit universal property.**

> [!note]- Derivation
> There are coprojection maps $\iota_j : D_j \to P$ (at each $O$, the colimit coprojection $(D_j)_O \to P_O$), forming a cocone. To show $P = \varinjlim D$, take any opetopic set $X$ with a cocone $f_j : D_j \to X$. A map $P \to X$ is, at each $O$, a function $P_O \to X_O$; by the colimit universal property *in $\mathbf{Set}$*, the cocone $\{(f_j)_O : (D_j)_O \to X_O\}$ induces a unique function $P_O \to X_O$. These assemble into a [[Def - Natural Transformation|natural transformation]] $P \to X$ (naturality is checked at each face map using the colimit's functoriality), and it is the unique map compatible with the cocone — because compatibility and uniqueness both reduce, pointwise, to the $\mathbf{Set}$ universal property. Hence $P$ satisfies the universal property of $\varinjlim D$, and colimits in $\mathbf{Set}^{\mathbb{O}^{op}}$ are computed pointwise. Cocompleteness follows since $\mathcal{J}$ was arbitrary.

**Step 3: A concrete pushout, computed cell-by-cell.**

> [!note]- Derivation
> Glue two copies of the arity-$2$ standard cell $\mathbf{y}O$ along a shared boundary arrow. Let $a = \mathbf{y}(\text{arrow})$ be the standard arrow, and consider the span
> $$\mathbf{y}O \;\xleftarrow{\ \sigma\ }\; a \;\xrightarrow{\ \tau\ }\; \mathbf{y}O,$$
> where $\sigma$ includes $a$ as (say) the target arrow of the first cell and $\tau$ as a source arrow of the second. The [[Def - Pullback and Pushout|pushout]] $Q$ is the colimit of this span. By Step 1, it is computed pointwise: at each opetope $O'$,
> $$Q_{O'} \;=\; (\mathbf{y}O)_{O'} \,\amalg_{a_{O'}}\, (\mathbf{y}O)_{O'},$$
> the pushout *of sets* — two copies of the $O'$-cells of the standard cell, glued along the $O'$-cells of the shared arrow. Concretely: the two $2$-cells stay distinct; their shared arrow is identified into one; the remaining arrows and points are kept disjoint except where forced by the identification. The result is the opetopic set with two $2$-cells sharing one boundary arrow — exactly the geometric gluing one would draw, performed automatically by the pointwise pushout. By [[Thm - The Yoneda Lemma|Yoneda]] (Operation 4), the maps $\sigma, \tau$ are the face maps $O' \to O$ packaged as maps of representables, so the whole gluing is a pushout of representables.

> [!note]- Complete formal solution
> Opetopic sets form the functor category $[\mathbb{O}^{op}, \mathbf{Set}]$. Since $\mathbf{Set}$ is cocomplete, so is any such functor category, with colimits computed pointwise: for $D : \mathcal{J} \to \mathbf{Set}^{\mathbb{O}^{op}}$, set $(\varinjlim D)_O := \varinjlim_j (D_j)_O$, made into a presheaf by functoriality of colimits over the face maps. This satisfies the colimit universal property because a map out of it, and the compatibility/uniqueness conditions, are all checked pointwise and reduce to the colimit universal property in $\mathbf{Set}$. For the pushout of $\mathbf{y}O \xleftarrow{\sigma} \mathbf{y}(\text{arrow}) \xrightarrow{\tau} \mathbf{y}O$, the pointwise formula gives, at each $O'$, the set pushout $(\mathbf{y}O)_{O'} \amalg_{(\mathbf{y}(\text{arrow}))_{O'}} (\mathbf{y}O)_{O'}$: the two $2$-cells remain distinct, their shared arrow is identified, and the gluing is cell-by-cell. $\blacksquare$

---

# Key Takeaways

**Presheaf categories inherit all colimits pointwise — this is the workhorse of every cell-complex construction.** The single most useful structural fact about opetopic sets (and simplicial sets, and any presheaf category) is that colimits are computed separately at each shape and then assembled. The trigger is any time you must *build* an opetopic set by gluing, quotienting, or taking a union: do it pointwise as a $\mathbf{Set}$-colimit at each opetope, and the result is automatically a presheaf with the right universal property. This is exactly how CW-complexes are built simplicially (attach cells via pushouts of $\Delta^n$ along their boundaries), and it is how the niches and fillers of the next section are assembled. Pointwise colimits are why "gluing cells" is a precise, automatic operation rather than a delicate hand construction.

**Verify universal properties pointwise rather than guessing the object.** The clean proof did not construct the colimit by a clever global formula; it *defined* it pointwise and verified the universal property, which reduced at each shape to the $\mathbf{Set}$ universal property. The reusable method is: when a (co)limit is claimed to be pointwise, define it pointwise and check the universal property reduces pointwise — this works because maps of presheaves are determined and tested object-by-object. The trigger is any structural claim about (co)limits in a functor category; the pointwise verification is almost always the shortest correct route, and it sidesteps the need to exhibit a concrete global construction.

**Gluing standard cells along shared faces is a pushout of representables.** The concrete pushout shows that the geometric operation "attach two cells along a common boundary" is literally a pushout of the representables $\mathbf{y}O$ along the shared face $\mathbf{y}(\text{arrow})$, computed cell-by-cell. The reusable principle is that *every* finite opetopic set is built from standard cells by such pushouts (the density theorem: every presheaf is a colimit of representables), so understanding pushouts of representables is understanding how opetopic sets are assembled. The trigger is any time you need to construct or decompose an opetopic set: express it as a colimit of standard cells glued along faces. This is the opetopic analogue of building a simplicial set by gluing simplices, and it is the construction underlying the universal-filler conditions that define weak $n$-categories. See [[Ex - The representable opetope as the standard cell via Yoneda]] for the standard cells and [[Ex - An opetopic set is a presheaf, unwound]] for the elementary presheaf data being glued.
