---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Opetopic Set"
  - "Thm - The Yoneda Lemma"
  - "Def - The Yoneda Embedding"
  - "Def - Presheaf"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

For an opetope $O$, let $\mathbf{y}O = \mathbb{O}(-, O)$ be the representable [[Def - Opetopic Set|opetopic set]]. Prove, using the [[Thm - The Yoneda Lemma|Yoneda lemma]], that for every opetopic set $X$ there is a natural bijection
$$\mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O,\, X) \;\cong\; X_O,$$
so that maps from the standard $O$-cell into $X$ are exactly the $O$-cells of $X$. Deduce that $\mathbf{y}O$ is the "free opetopic set on a single $O$-shaped cell" — the opetopic analogue of the standard simplex $\Delta^n$ — and that the [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathbb{O} \to \mathbf{Set}^{\mathbb{O}^{op}}$ is fully faithful.

**Recall:**

![[Thm - The Yoneda Lemma#Statement]]

The [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathcal{C} \to \mathbf{Set}^{\mathcal{C}^{op}}$ sends an object $c$ to the representable presheaf $\mathbf{y}c = \mathcal{C}(-, c)$. For [[Def - Opetopic Set|opetopic sets]], $\mathcal{C} = \mathbb{O}$ and $\mathbf{y}O = \mathbb{O}(-, O)$ is the **standard $O$-cell**: its set of $O'$-cells is the set of face maps $O' \to O$.

---

# Convergent Strategy

**Problem class:** This is a *specialise-Yoneda-and-read-off-the-consequences* problem — a structural-world problem. The work is to apply the Yoneda lemma at the indexing category $\mathbb{O}$ and extract the standard-cell interpretation, then the full faithfulness of the embedding.

**Assumption pattern:** The assumption is that opetopic sets are a presheaf category, so Yoneda applies verbatim. The moment "opetopic set = presheaf on $\mathbb{O}$" is in hand, the representable-probes-cells statement is *not* an opetope-specific fact but the general Yoneda lemma instantiated, and the whole exercise is recognising that.

**Theorem routing:** We route directly through the [[Thm - The Yoneda Lemma|Yoneda lemma]] ($\mathbf{Set}^{\mathcal{C}^{op}}(\mathbf{y}c, X) \cong X(c)$) with $\mathcal{C} = \mathbb{O}$, $c = O$, and through the corollary that the [[Def - The Yoneda Embedding|Yoneda embedding]] is [[Thm - The Yoneda Embedding is Fully Faithful|fully faithful]].

**Key decision point:** The non-obvious choice is to *not* prove the bijection by hand (constructing maps $\mathbf{y}O \to X$ and inverting) but to recognise it as the Yoneda lemma already proved in general, instantiated at $\mathbb{O}$. The tempting but wasteful alternative is to re-derive Yoneda from scratch for opetopes; the decision is to import the general theorem and only check the instantiation is legitimate (it is, because opetopic sets form a presheaf category).

---

# Legal Operations Used

1. **Operation 4 (invoke Yoneda to turn a cell into a representable)** from the topic page. This is the entire exercise: the bijection $\mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X) \cong X_O$ is the Yoneda lemma at $\mathbb{O}$.

2. **Operation 3 (take the presheaf on a shape category)** from the topic page, used to justify that opetopic sets form a genuine presheaf category, so Yoneda applies without modification.

---

# Hints

> [!note]- Hint 1
> Do not reinvent anything. Opetopic sets are presheaves on $\mathbb{O}$, so the [[Thm - The Yoneda Lemma|Yoneda lemma]] applies with the indexing category set to $\mathbb{O}$. Write down what the lemma says with $\mathcal{C} = \mathbb{O}$, $c = O$.

> [!note]- Hint 2
> The Yoneda bijection sends a natural transformation $\eta : \mathbf{y}O \to X$ to the element $\eta_O(\mathrm{id}_O) \in X_O$ — apply the component at $O$ to the identity face map. Check this is natural in $X$ and in $O$.

> [!note]- Hint 3
> For full faithfulness, specialise the bijection to $X = \mathbf{y}O'$: then $\mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, \mathbf{y}O') \cong (\mathbf{y}O')_O = \mathbb{O}(O, O')$, which says maps of standard cells are exactly face maps of opetopes.

---

# Solution

The route is one instantiation of the Yoneda lemma at $\mathbb{O}$, followed by reading the standard-cell and full-faithfulness consequences off the resulting bijection.

**Step 1: The Yoneda bijection at $\mathbb{O}$.**

> [!note]- Derivation
> The [[Thm - The Yoneda Lemma|Yoneda lemma]] for a category $\mathcal{C}$ states that for every presheaf $X : \mathcal{C}^{op} \to \mathbf{Set}$ and object $c$,
> $$\mathbf{Set}^{\mathcal{C}^{op}}(\mathbf{y}c,\, X) \;\cong\; X(c), \qquad \eta \longmapsto \eta_c(\mathrm{id}_c),$$
> naturally in $c$ and $X$. Opetopic sets are presheaves on $\mathbb{O}$ (Operation 3), so we set $\mathcal{C} = \mathbb{O}$, $c = O$, obtaining
> $$\mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O,\, X) \;\cong\; X_O, \qquad \eta \longmapsto \eta_O(\mathrm{id}_O).$$
> The inverse sends an $O$-cell $x \in X_O$ to the natural transformation whose $O'$-component sends a face map $\alpha : O' \to O$ to the restriction $X(\alpha)(x) \in X_{O'}$. Naturality and bijectivity are the general Yoneda content, requiring no opetope-specific argument. So **a map from the standard $O$-cell into $X$ is exactly an $O$-cell of $X$.**

**Step 2: $\mathbf{y}O$ is the free opetopic set on one $O$-cell.**

> [!note]- Derivation
> Step 1 says picking a map $\mathbf{y}O \to X$ is the same as picking a single $O$-cell of $X$, with no further data and no constraints beyond $x$'s own boundary. This is precisely the universal property of a *free* object: $\mathbf{y}O$ has one "generating" $O$-cell (namely $\mathrm{id}_O$), and any choice of $O$-cell in any $X$ extends uniquely to a map out of $\mathbf{y}O$. Hence $\mathbf{y}O$ is the opetopic set freely generated by a single $O$-shaped cell — the opetopic analogue of the standard simplex $\Delta^n$, whose non-degenerate top simplex is its generating cell. Its lower cells are exactly the faces of $O$ (the face maps into $O$), forced by the boundary of the generating cell.

**Step 3: The Yoneda embedding is fully faithful.**

> [!note]- Derivation
> Specialise the bijection of Step 1 to $X = \mathbf{y}O'$:
> $$\mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O,\, \mathbf{y}O') \;\cong\; (\mathbf{y}O')_O \;=\; \mathbb{O}(O, O').$$
> So natural transformations between standard cells are in bijection with face maps of opetopes, and one checks (the general [[Thm - The Yoneda Embedding is Fully Faithful|Yoneda embedding fully faithful]] statement) that this bijection is precisely the action of $\mathbf{y}$ on morphisms. Therefore $\mathbf{y} : \mathbb{O} \to \mathbf{Set}^{\mathbb{O}^{op}}$ is **fully faithful**: it embeds the category of opetopes into opetopic sets as the standard cells, faithfully recording the face maps. This is the opetopic analogue of $\Delta \hookrightarrow \mathbf{sSet}$ via $[n] \mapsto \Delta^n$.

> [!note]- Complete formal solution
> Opetopic sets are presheaves on $\mathbb{O}$, so the [[Thm - The Yoneda Lemma|Yoneda lemma]] applies: for any $X$ and opetope $O$,
> $$\mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X) \cong X_O, \quad \eta \mapsto \eta_O(\mathrm{id}_O),$$
> with inverse $x \mapsto (\alpha \mapsto X(\alpha)(x))$, naturally in $O$ and $X$. Thus maps from the standard $O$-cell are exactly $O$-cells. This is the universal property of the free opetopic set on one $O$-cell, so $\mathbf{y}O$ is that free object (analogue of $\Delta^n$), with generating cell $\mathrm{id}_O$ and lower cells the faces of $O$. Taking $X = \mathbf{y}O'$ gives $\mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, \mathbf{y}O') \cong \mathbb{O}(O, O')$, so $\mathbf{y}$ is [[Thm - The Yoneda Embedding is Fully Faithful|fully faithful]]. $\blacksquare$

---

# Key Takeaways

**Yoneda is the same theorem at every indexing category — instantiate, do not re-prove.** The deepest efficiency in this whole subject is that "representables probe cells" is *not* a fact about opetopes; it is the Yoneda lemma, true for presheaves on any category, instantiated at $\mathbb{O}$. The trigger is any presheaf-of-cells theory (simplicial, globular, opetopic, cubical): the moment you have identified your structures as presheaves, the standard-cell/probe statement is already proved, and re-deriving it is wasted effort. This is the single biggest payoff of the "separate the shapes from the structure" frame — all the structural theory is general presheaf theory, and only the shape category changes.

**A representable is a free object on one generating cell.** The Yoneda bijection $\mathbf{Set}^{\mathbb{O}^{op}}(\mathbf{y}O, X) \cong X_O$ is, read as a universal property, the statement that $\mathbf{y}O$ is freely generated by a single $O$-cell. The reusable insight is that representables are always "free on one generator" in their presheaf category — $\Delta^n$ in simplicial sets, $\mathbf{y}O$ in opetopic sets, the free module on one element in modules. The trigger is any time you need a "standard cell" or a "test object" of a given shape: take the representable, and use that maps out of it correspond to cells of that shape. This is exactly the role $\Delta^n$ plays in defining horns and fillers, and $\mathbf{y}O$ will play the same role for opetopic niches.

**Full faithfulness means the shape category embeds without distortion.** That $\mathbf{y} : \mathbb{O} \to \mathbf{Set}^{\mathbb{O}^{op}}$ is fully faithful says the opetopes sit inside opetopic sets as the standard cells, with their face maps recorded exactly — no shapes are identified, no maps are added or lost. The reusable principle is that the Yoneda embedding always realises a small category as a full subcategory of its presheaves, which is what lets you treat abstract shapes as concrete objects you can map between. The trigger is any time you want to manipulate the shapes themselves (opetopes, simplices) as objects of the larger, cocomplete presheaf category: embed them via Yoneda and work there, where colimits exist. See [[Ex - An opetopic set is a presheaf, unwound]] for the elementary side of this correspondence and [[Ex - Colimits of opetopic sets are computed pointwise]] for the cocompleteness that makes the embedding useful.
