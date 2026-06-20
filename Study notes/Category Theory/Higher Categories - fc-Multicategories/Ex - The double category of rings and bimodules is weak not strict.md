---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Weak Double Category"
  - "Def - Ring"
  - "Def - Tensor Product of Modules"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Show that [[Def - Ring|rings]], ring homomorphisms (vertical), bimodules (horizontal), and equivariant bimodule maps ($2$-cells) form a [[Def - Weak Double Category|weak double category]] $\mathbb{R}\mathrm{ing}$ under horizontal composition $M \odot N = M \otimes_S N$, and prove that this double category is *genuinely weak*: exhibit an explicit triple of bimodules for which the associator
$$a : (M \otimes_S N) \otimes_T P \xrightarrow{\ \cong\ } M \otimes_S (N \otimes_T P)$$
is a non-identity isomorphism — so $\mathbb{R}\mathrm{ing}$ cannot be made into a *strict* double category. Identify the horizontal unit and verify it acts as a unit only up to isomorphism.

**Recall:**

![[Def - Weak Double Category#The Definition]]

A **strict double category** is a [[Def - Category|category]] internal to $\mathbf{Cat}$: horizontal composition is strictly associative and unital. A **weak (pseudo) double category** relaxes the horizontal associativity and unitality to coherent invertible $2$-cells (associator $a$, unitors $l, r$, with pentagon and triangle). The **[[Def - Tensor Product of Modules|tensor product over S]]** $M\otimes_S N$ of an $(R,S)$-bimodule $M$ and an $(S,T)$-bimodule $N$ is the $(R,T)$-bimodule with $ms\otimes n = m\otimes sn$.

---

# Convergent Strategy

**Problem class:** A *coherence-vs-strictness* problem: build the structure (template identification) and then *refute* strictness by an explicit counterexample, which is the "weakness is genuine" target on the topic page.

**Assumption pattern:** The horizontal composition is the tensor over the middle ring, and the tensor is built by a universal construction — generators-and-relations, equivalently a coequalizer. Universal constructions are associative *up to canonical iso*, never on the nose, because the underlying sets of $(M\otimes_S N)\otimes_T P$ and $M\otimes_S(N\otimes_T P)$ are built differently even when canonically isomorphic. This is the assumption that forces weakness.

**Theorem routing:** The construction is the representable shadow of the fc-multicategory of [[Ex - The fc-multicategory of rings bimodules and maps]]; that every string has a universal composite (the iterated tensor) makes it a weak double category, by the Categorical/Structural definition of [[Def - Weak Double Category|weak double category]] as a representable [[Def - fc-Multicategory|fc-multicategory]]. The refutation of strictness routes through the explicit non-equality of the two iterated tensors as constructed objects.

**Key decision point:** The non-obvious move is to find a *concrete* triple where strict equality visibly fails, not merely to say "tensor is associative up to iso". The cleanest witness uses elements: pick rings and bimodules where $(m\otimes n)\otimes p$ and $m\otimes(n\otimes p)$ live in different quotient groups whose elements are not literally identical, so the associator genuinely *moves* elements. The temptation to wave at "up to iso" must be replaced by an explicit non-identity map.

---

# Legal Operations Used

1. **Operation 6 (form the tensor as the balancing coequalizer).** Horizontal composition $M\odot N=M\otimes_S N$ is the universal balanced object.

2. **Operation 2 (representability upgrades fc-multicategory to double category).** Every string of bimodules has the universal composite (iterated tensor), so the structure is a weak double category.

3. **Operation 8 (empty string / unit).** The horizontal unit at $R$ is $R$ as an $(R,R)$-bimodule; check $R\otimes_R M\cong M$.

---

# Hints

> [!note]- Hint 1
> First assemble the four layers and check interchange — equivariant maps respect both the vertical (homomorphism) and horizontal (tensor) compositions. Then identify the horizontal unit at $R$: it is $R$ itself as an $(R,R)$-bimodule, with the left unitor $l_M : R\otimes_R M\to M$ given by $r\otimes m\mapsto rm$.

> [!note]- Hint 2
> For weakness, do not argue abstractly. Take $R=S=T=k$ a field and bimodules that are vector spaces. Then $(U\otimes V)\otimes W$ and $U\otimes(V\otimes W)$ are both isomorphic to a space of dimension $\dim U\cdot\dim V\cdot\dim W$, but the *elements* $(u\otimes v)\otimes w$ and $u\otimes(v\otimes w)$ are not literally the same symbol — the associator relabels them.

> [!note]- Hint 3
> The cleanest refutation: a strict double category would require $(M\otimes_S N)\otimes_T P$ and $M\otimes_S(N\otimes_T P)$ to be the *same object*, hence the associator to be the identity. But these are different quotients of different free groups (one balances $N,P$ first, the other $M,N$ first), so they are not equal as sets; the canonical iso is therefore not an identity. Spell this out for a one-dimensional example.

---

# Solution

We build $\mathbb{R}\mathrm{ing}$, verify it is a weak double category, and then exhibit the associator as a non-identity iso.

**Step 1: The four layers and interchange.**

> [!note]- Derivation
> Objects: [[Def - Ring|rings]]. Vertical $1$-cells: ring homomorphisms, composed strictly. Horizontal $1$-cells $R\nrightarrow S$: $(R,S)$-bimodules. $2$-cells: a square with top $M$ ($(R,S)$-bimodule), bottom $M'$ ($(R',S')$-bimodule), left $f : R\to R'$, right $g : S\to S'$ is an additive map $\alpha : M\to M'$ with $\alpha(rms)=f(r)\alpha(m)g(s)$. Vertical composition stacks such squares (compose the $\alpha$'s and the boundary homomorphisms); horizontal composition tensors. Interchange holds because $(\beta\odot\beta')\circ(\alpha\odot\alpha')$ and $(\beta\circ\alpha)\odot(\beta'\circ\alpha')$ are both the map $m\otimes n\mapsto \beta(\alpha(m))\otimes\beta'(\alpha'(n))$ on the tensor.

**Step 2: Horizontal composition is the tensor; it is representable, so $\mathbb{R}\mathrm{ing}$ is a weak double category.**

> [!note]- Derivation
> Set $M\odot N := M\otimes_S N$ for $M$ an $(R,S)$- and $N$ an $(S,T)$-bimodule; this is an $(R,T)$-bimodule. The horizontal unit at $R$ is $\mathrm{U}_R := R$ as an $(R,R)$-bimodule. By the [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]], every string $(M_1,\dots,M_n)$ has the universal composite $M_1\otimes_{R_1}\cdots\otimes_{R_{n-1}}M_n$. By the Categorical/Structural definition of [[Def - Weak Double Category|weak double category]] (a *representable* [[Def - fc-Multicategory|fc-multicategory]]), $\mathbb{R}\mathrm{ing}$ is a weak double category, with associator and unitors supplied by the universal properties. The left unitor $l_M : R\otimes_R M\to M$, $r\otimes m\mapsto rm$, is an iso (inverse $m\mapsto 1\otimes m$), confirming the unit acts up to iso.

**Step 3: The associator is a non-identity isomorphism, so $\mathbb{R}\mathrm{ing}$ is not strict.**

> [!note]- Derivation
> Take $R=S=T=k$ a field and $M=N=P=k$ as one-dimensional $k$-vector spaces (bimodules over $k$). Then:
> - $(M\otimes_k N)\otimes_k P$ is the set of equivalence classes of symbols $(m\otimes n)\otimes p$ in the *iterated* free-then-quotient construction where $M\otimes_k N$ is formed first;
> - $M\otimes_k(N\otimes_k P)$ is formed by tensoring $N,P$ first.
>
> As *constructed* abelian groups these are distinct: their elements are built from different intermediate quotients (one contains symbols of the form $(m\otimes n)\otimes p$, the other $m\otimes(n\otimes p)$), and there is no symbol that literally belongs to both. The associator $a : (m\otimes n)\otimes p\mapsto m\otimes(n\otimes p)$ is the canonical iso; it is *not* the identity map, because the identity is only defined within one object and the two objects are not equal. Concretely, with the basis vector $1\in k$, $a$ sends $(1\otimes 1)\otimes 1\mapsto 1\otimes(1\otimes 1)$ — two genuinely different symbols. A strict double category would require these two objects to be equal and $a=\mathrm{id}$; since they are not equal, no strict structure with these horizontal composites exists. Hence $\mathbb{R}\mathrm{ing}$ is genuinely weak.

> [!note]- Complete formal solution
> $\mathbb{R}\mathrm{ing}$: rings (objects), homomorphisms (vertical, strict), $(R,S)$-bimodules (horizontal), equivariant additive maps (squares). Interchange holds since both pasting orders give $m\otimes n\mapsto\beta\alpha(m)\otimes\beta'\alpha'(n)$. Horizontal composition $M\odot N=M\otimes_S N$, unit $\mathrm{U}_R=R$; by the universal property of $\otimes$ every string has the iterated tensor as universal composite, so $\mathbb{R}\mathrm{ing}$ is a representable [[Def - fc-Multicategory|fc-multicategory]], i.e. a [[Def - Weak Double Category|weak double category]], with $l_M : R\otimes_R M\xrightarrow{\cong}M$. Strictness fails: for $R=S=T=k$ and $M=N=P=k$, the objects $(M\otimes_k N)\otimes_k P$ and $M\otimes_k(N\otimes_k P)$ are distinct constructed groups (different intermediate quotients), so the canonical associator $a:(m\otimes n)\otimes p\mapsto m\otimes(n\otimes p)$ is not an identity. Therefore no strict double category structure with these horizontal composites exists; $\mathbb{R}\mathrm{ing}$ is genuinely weak. $\blacksquare$

---

# Key Takeaways

**Weakness is the signature of universal constructions.** The tensor product is defined by a universal property, and any operation defined by a universal property is associative only up to canonical isomorphism — never strictly — because the universal object is determined only up to iso and the two bracketings construct it by different intermediate steps. This is the deep reason the bimodule double category must be weak, and it is the same reason [[Def - Pullback and Pushout|pullbacks]], coproducts, and free constructions all associate weakly. The transferable trigger: "horizontal composition is a tensor / pullback / colimit" $\Rightarrow$ "expect weakness; do not attempt a strict structure". Strictness is the rare, special case where the operation happens to be literal (e.g. function composition, set product on the nose only after a choice).

**To refute strictness, descend to elements and watch the symbols move.** It is easy to mistake "associative up to iso" for "associative", because the iso is invisible at the level of isomorphism classes. The honest refutation tracks *constructed* objects: $(m\otimes n)\otimes p$ and $m\otimes(n\otimes p)$ are different symbols living in different quotient groups, so the associator genuinely relabels them and is not an identity map. The transferable diagnostic for proving a structure is *not* strict: exhibit two bracketings whose underlying constructed sets are not equal, so that the comparison map cannot be the identity. This is the element-level analogue of legal operation 3 read in reverse — uniqueness of representing objects gives the iso; non-equality of the representatives makes it a non-identity iso.

**The "vertical strict, horizontal weak" convention is forced here, and it tells you how to model any two-arrow situation.** Ring homomorphisms compose strictly (honest functions), bimodules tensor weakly (universal construction); the chapter-wide convention is not a stipulation but a consequence. Whenever you meet objects with two kinds of arrow, the diagnostic is: which arrows are honest functions/maps (make them vertical and strict) and which are processes built by a universal construction (make them horizontal and weak)? Applying this to spans gives [[Ex - The double category of spans]], to categories gives categories/functors/profunctors, and to manifolds gives maps/cobordisms. The asymmetry between the two directions is the structural fingerprint of a genuine double category, and recognising it is half of correctly modelling any such situation.
