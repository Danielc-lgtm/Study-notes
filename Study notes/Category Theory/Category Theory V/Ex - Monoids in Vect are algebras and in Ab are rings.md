---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Monoid in a Monoidal Category"
  - "Def - Monoidal Category"
  - "Def - Ring"
  - "Def - Tensor Product of Vector Spaces"
tags: [category-theory, foundations]
---

# Problem Statement

**(a)** Show that a [[Def - Monoid in a Monoidal Category|monoid object]] in the monoidal category $(\mathbf{Ab}, \otimes_{\mathbb{Z}}, \mathbb{Z})$ is exactly a [[Def - Ring|ring]], and a *commutative* monoid object is exactly a commutative ring.

**(b)** Show that a monoid object in $(\mathbf{Vect}_k, \otimes_k, k)$ is exactly a unital associative $k$-algebra.

**(c)** Confirm that a monoid object in $([\mathcal{C},\mathcal{C}], \circ, 1_{\mathcal{C}})$ is exactly a [[Def - Monad and Comonad|monad]], closing the loop of the chapter.

**Recall:**

![[Def - Monoid in a Monoidal Category#The Definition]]

The [[Def - Tensor Product of Vector Spaces|tensor product]] $V\otimes_k W$ has the universal property that $k$-linear maps $V\otimes_k W\to U$ correspond to $k$-bilinear maps $V\times W\to U$. The same holds for $\otimes_{\mathbb{Z}}$ on [[Def - Abelian Group|abelian groups]] (bilinear = biadditive).

---

# Convergent Strategy

**Problem class:** An "unwind a monoid object" problem — translating the abstract [[Def - Monoid in a Monoidal Category|monoid-object]] axioms into a concrete category to recover a familiar structure (legal operation 7).

**Assumption pattern:** The key is the universal property of $\otimes$: a multiplication $m : M\otimes M\to M$ is the *same data* as a bilinear map $M\times M\to M$. The assumption to leverage is "linear map out of a tensor = bilinear map," which converts the abstract $m$ into a concrete bilinear multiplication.

**Theorem routing:** Route through [[Def - Monoid in a Monoidal Category]] and the universal property of the [[Def - Tensor Product of Vector Spaces|tensor product]]: rewrite $m, e$ as a bilinear multiplication and a chosen unit, then translate the associativity and unitality diagrams into the ring/algebra axioms. For (c), $\otimes = \circ$, so $m$ is a natural transformation and the axioms are the monad axioms.

**Key decision point:** The crux is recognizing that the monoidal unit object differs across the three cases — $\mathbb{Z}$ for $\mathbf{Ab}$, $k$ for $\mathbf{Vect}_k$, $1_{\mathcal{C}}$ for endofunctors — and that the unit map $e : I\to M$ correspondingly picks out $1_R \in R$, $1 \in A$, or $\eta : 1\Rightarrow T$. The "linear out of tensor = bilinear" reduction is what makes (a),(b) immediate.

---

# Legal Operations Used

1. **Operation 7 from the topic page (unwind a monoid object in a monoidal category).** Each part translates the monoid-object diagrams into a concrete category.

2. **Operation 8 from the topic page (invoke coherence to drop parentheses).** By [[Thm - Mac Lane Coherence Theorem|coherence]] we suppress $\alpha, \lambda, \rho$, so the associativity axiom reads $m\circ(m\otimes 1) = m\circ(1\otimes m)$ without associator clutter.

---

# Hints

> [!note]- Hint 1
> By the universal property of $\otimes$, a morphism $m : M\otimes M\to M$ is the same as a bilinear map $M\times M\to M$, i.e. a multiplication satisfying $m(a+a',b) = m(a,b)+m(a',b)$ and similarly in the second slot. Write $a\cdot b := m(a\otimes b)$.

> [!note]- Hint 2
> The unit $e : I\to M$ is a morphism out of the unit object. For $\mathbf{Ab}$, $I = \mathbb{Z}$, and $e$ is determined by $e(1) =: 1_M$; for $\mathbf{Vect}_k$, $I = k$, similarly. The unitality diagram says $1_M\cdot x = x = x\cdot 1_M$.

> [!note]- Hint 3
> The associativity diagram $m\circ(m\otimes 1) = m\circ(1\otimes m)$ (associators suppressed by coherence) says $(a\cdot b)\cdot c = a\cdot(b\cdot c)$. Bilinearity + associativity + unit = ring (in $\mathbf{Ab}$) or $k$-algebra (in $\mathbf{Vect}_k$).

> [!note]- Hint 4
> For (c), $\otimes = \circ$ in $([\mathcal{C},\mathcal{C}],\circ,1)$, so $m : T\circ T\Rightarrow T$ is a natural transformation $\mu$, $e : 1\Rightarrow T$ is $\eta$, and the (strict) monoid axioms are *verbatim* the monad axioms — no associators because the endofunctor category is strict.

---

# Solution

The plan: use the universal property of $\otimes$ to turn the abstract multiplication into a bilinear one (Step 1), translate the unit and associativity diagrams into ring/algebra axioms (Step 2), and specialize to endofunctors where $\otimes = \circ$ gives a monad (Step 3). The crux is "linear out of a tensor = bilinear."

**Step 1 (a),(b): Multiplication = bilinear map.**

> [!note]- Derivation
> In $(\mathbf{Ab}, \otimes_{\mathbb{Z}})$, the universal property of the tensor product says a group homomorphism $m : M\otimes_{\mathbb{Z}} M \to M$ corresponds bijectively to a $\mathbb{Z}$-bilinear (= biadditive) map $M\times M\to M$. Write $a\cdot b := m(a\otimes b)$. Biadditivity gives the distributive laws $a(b+c) = ab+ac$ and $(a+b)c = ac+bc$. The same holds verbatim in $(\mathbf{Vect}_k, \otimes_k)$ with "$k$-bilinear" in place of "biadditive," giving $k$-bilinearity (so $\cdot$ is also compatible with scalar multiplication).

**Step 2 (a),(b): Unit and associativity → ring / algebra axioms.**

> [!note]- Derivation
> *Unit.* The morphism $e : I\to M$ out of the unit object ($I = \mathbb{Z}$ or $k$) is determined by $1_M := e(1)$. The unitality diagram (with unitors suppressed by [[Thm - Mac Lane Coherence Theorem|coherence]]) reads $m\circ(e\otimes 1) = 1_M$ and $m\circ(1\otimes e) = 1_M$, i.e. $1_M\cdot x = x = x\cdot 1_M$. So $1_M$ is a two-sided multiplicative unit.
>
> *Associativity.* The associativity diagram $m\circ(m\otimes 1_M) = m\circ(1_M\otimes m)$ reads, on elements, $(a\cdot b)\cdot c = a\cdot(b\cdot c)$.
>
> Assembling: $(M, +, \cdot, 1_M)$ is an [[Def - Abelian Group|abelian group]] under $+$, with an associative, biadditive (= distributive), unital multiplication — exactly a [[Def - Ring|ring]] (in $\mathbf{Ab}$) or a unital associative $k$-algebra (in $\mathbf{Vect}_k$, where additionally the multiplication is $k$-bilinear, the defining feature of a $k$-algebra). A *commutative* monoid object (using the symmetry $\beta$, $m\circ\beta = m$) gives $a\cdot b = b\cdot a$: a commutative ring (resp. commutative $k$-algebra).

**Step 3 (c): Monoid in endofunctors = monad.**

> [!note]- Derivation
> In $([\mathcal{C},\mathcal{C}], \circ, 1_{\mathcal{C}})$ the tensor is composition and the unit object is $1_{\mathcal{C}}$. A monoid object is $(T, m, e)$ with $m : T\otimes T = T\circ T\Rightarrow T$ and $e : 1_{\mathcal{C}}\Rightarrow T$. Set $\mu := m$ and $\eta := e$. The endofunctor category is **strict** monoidal ($\alpha, \lambda, \rho$ are identities), so the associativity axiom $m\circ(m\otimes 1) = m\circ(1\otimes m)$ reads $\mu\circ(\mu T) = \mu\circ(T\mu)$ with no associator, and the unitality axioms read $\mu\circ(\eta T) = 1_T = \mu\circ(T\eta)$. These are *exactly* the [[Def - Monad and Comonad|monad]] axioms. So a monoid in endofunctors is a monad, closing the loop with §5.1.

> [!note]- Complete formal solution
> **(a)** A morphism $m : M\otimes_{\mathbb{Z}}M\to M$ is a biadditive map $M\times M\to M$ (universal property of $\otimes$); writing $a\cdot b = m(a\otimes b)$, biadditivity is distributivity. The unit $e : \mathbb{Z}\to M$ gives $1_M = e(1)$ with $1_M\cdot x = x = x\cdot 1_M$ (unitality), and associativity of $m$ gives $(ab)c = a(bc)$. So $(M,+,\cdot,1_M)$ is a [[Def - Ring|ring]]; commutativity (via $\beta$) gives a commutative ring.
>
> **(b)** Identical over $k$: $m : V\otimes_k V\to V$ is $k$-bilinear, giving a $k$-algebra.
>
> **(c)** In $([\mathcal{C},\mathcal{C}],\circ,1)$ (strict), a monoid $(T,\mu,\eta)$ has $\mu : T\circ T\Rightarrow T$, $\eta : 1\Rightarrow T$, and the monoid axioms are the monad axioms verbatim. $\blacksquare$

> [!tip] Why the unit object changes the answer
> The *same* monoid-object definition gives a ring, a $k$-algebra, or a monad depending only on the ambient monoidal category — specifically on its tensor and unit object. The unit map $e : I\to M$ is what picks out $1_R$, $1_A$, or $\eta$, and the tensor is what makes the multiplication biadditive, bilinear, or a natural transformation. Varying $(\mathcal{V},\otimes,I)$ is the single lever generating the whole zoo.

---

# Key Takeaways

**"Linear map out of a tensor product = bilinear map" is the workhorse identity.** The entire content of parts (a) and (b) is the universal property of $\otimes$: a morphism $M\otimes M\to M$ is the same data as a bilinear multiplication $M\times M\to M$. This single translation converts the abstract monoid-object multiplication into the concrete ring/algebra multiplication, after which the associativity and unitality diagrams become the familiar axioms. The transferable lesson is that whenever a monoidal category's tensor classifies bilinear (or multilinear) maps, "monoid object" unwinds to "object with an associative unital bilinear multiplication" — which is a ring-like structure. The trigger is a tensor with a universal multilinear property; the reaction is to rewrite every $\otimes$-morphism as a multilinear map.

**The ambient monoidal category is a dial that selects the algebraic structure.** The deepest takeaway is that one definition — monoid object — produces ordinary monoids, rings, $k$-algebras, $R$-algebras, and monads, purely by changing $(\mathcal{V},\otimes,I)$. The tensor product determines the *kind* of multiplication (set-function, biadditive, bilinear, or natural transformation), and the unit object determines what "the unit element" is (a point, $1_R$, $1_A$, or $\eta$). This is the unifying frame of §5.4: rings and monads are not analogous structures that happen to look alike — they are *the same structure* in different worlds. Recognizing a familiar algebraic object as a monoid object immediately tells you what its modules, bimodules, and tensor products should be, by importing the general monoid-object theory.

**Strictness of the endofunctor category is why monads have no associators.** Part (c) closes the chapter's loop, and the subtle point is that $([\mathcal{C},\mathcal{C}],\circ,1)$ is *strict* monoidal — composition is associative and unital on the nose — so the monoid-object axioms have no associator or unitor clutter and read off as the monad axioms verbatim. In a general (weak) monoidal category like $(\mathbf{Vect}_k,\otimes)$ the associativity axiom carries an associator, but [[Thm - Mac Lane Coherence Theorem|coherence]] lets you suppress it. The lesson is that the slogan "a monad is a monoid in endofunctors" is *literally* true precisely because the endofunctor category is strict, and coherence is what guarantees the weak cases behave the same way. See [[Ex - Braidings and symmetry]] for the further structure (commutativity) that the braiding adds, which distinguishes commutative from non-commutative rings.
