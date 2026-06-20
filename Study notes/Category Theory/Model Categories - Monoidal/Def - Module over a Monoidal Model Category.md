---
type: definition
subject: model-categories
prereqs:
  - "Def - Monoidal Model Category"
  - "Def - Monoid in a Monoidal Category"
  - "Def - Module"
  - "Def - Closed Monoidal Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $(\mathcal{C}, \otimes, I)$ is a [[Def - Monoidal Model Category|monoidal model category]] (closed symmetric monoidal, with the pushout-product and unit axioms). A **monoid** in $\mathcal{C}$ is an object $R$ with multiplication $\mu : R \otimes R \to R$ and unit $\eta : I \to R$; we use $R, S$ for monoids and $M, N$ for modules. The category of left $R$-modules is $\mathbf{Mod}_R$ (or $R\text{-}\mathbf{Mod}$); for commutative $R$ the left, right, and two-sided notions coincide. The forgetful functor $U : \mathbf{Mod}_R \to \mathcal{C}$ has a left adjoint, the **free module** functor $F = R \otimes - : \mathcal{C} \to \mathbf{Mod}_R$. The full symbol registry is on [[Model Categories — Monoidal Model Categories]].

This is a compound page: it defines three interlocking notions — a **monoid** in $\mathcal{C}$, a **module** over such a monoid, and the **model structure** that $\mathbf{Mod}_R$ inherits — because the homotopy theory of modules is the point, and it is not statable without the algebraic notions of monoid and module that it sits on top of.

---

# Axiom Motivation

The motivation is to do algebra *inside* a homotopy theory. Once you have a tensor product that respects weak equivalences — a [[Def - Monoidal Model Category|monoidal model category]] — you can write down rings and modules using $\otimes$ in place of the set-theoretic multiplication, and then ask for their *homotopy theory*. The reward is enormous: in symmetric spectra, monoids are **ring spectra** and this construction is the entire foundation of "brave new algebra"; in $\mathbf{Ch}(R)$, monoids are **differential graded algebras** and modules over them are the objects of derived representation theory. The question this page answers is: when does the category of modules over a homotopical ring carry a homotopy theory of its own?

Start with the algebra. A [[Def - Monoid in a Monoidal Category|monoid]] in $\mathcal{C}$ is the exact transcription of "ring" with $\otimes$ replacing $\times$: an object $R$, a multiplication $\mu : R \otimes R \to R$ that is associative ($\mu \circ (\mu \otimes 1) = \mu \circ (1 \otimes \mu)$, using the associator), and a unit $\eta : I \to R$ satisfying the unit laws (via the unitors). When $\mathcal{C} = \mathbf{Ab}$ with $\otimes_{\mathbb{Z}}$ this is precisely a [[Def - Ring|ring]]; when $\mathcal{C} = \mathbf{Ch}(R)$ it is a DGA; when $\mathcal{C}$ is spectra it is a ring spectrum. A **module** $M$ is an object with an action $a : R \otimes M \to M$ compatible with $\mu$ and $\eta$ — the transcription of "$R$-module". So far this is pure algebra in a monoidal category and needs no model structure.

Now the homotopy theory, and the difficulty. We want $\mathbf{Mod}_R$ to be a model category, and the natural attempt is **transfer**: declare a map of modules to be a weak equivalence or fibration exactly when the underlying map in $\mathcal{C}$ is, and *generate* the cofibrations via the free-forgetful adjunction $F \dashv U$. For this transfer to produce a genuine model structure, we must factor every map of modules as (trivial cofibration)∘(cofibration into trivial fibration), and the only tool is the small object argument applied to the *free* images $F(I)$, $F(J)$ of the generating (trivial) cofibrations of $\mathcal{C}$. The obstruction is subtle: building a cofibration of modules by attaching free cells involves pushouts along maps of the form $R \otimes (\text{trivial cofibration})$, and *transfinitely composing* such pushouts. We need these transfinite composites of pushouts of $\{R \otimes j : j \in J\}$ to remain weak equivalences. The pushout-product axiom controls $\mathcal{C}$ itself, but it does **not** by itself control what happens after you tensor the trivial cofibrations of $\mathcal{C}$ with an *arbitrary* object and then take transfinite cellular composites.

This is exactly the gap the **monoid axiom** (Schwede–Shipley) fills. It demands: the class generated under transfinite composition and pushout by maps of the form $(\text{trivial cofibration}) \otimes X$, for *arbitrary* $X \in \mathcal{C}$, consists of weak equivalences. The pushout-product axiom gives this only when $X$ is cofibrant; the monoid axiom upgrades it to all $X$, which is what you need because the free module $R \otimes M$ tensors against the possibly-non-cofibrant $R$. With the monoid axiom in hand, the transfer goes through and $\mathbf{Mod}_R$ — and indeed the category of $R$-algebras — becomes a cofibrantly generated model category. What breaks without it? The transferred "trivial cofibrations" might not be weak equivalences, so the factorization axiom fails and $\mathbf{Mod}_R$ is not a model category; one would be doing homotopy theory with broken machinery. The monoid axiom is the precise, minimal extra hypothesis that the homotopy theory of modules requires beyond the homotopy theory of $\mathcal{C}$.

Why is the model structure *created* by the forgetful functor (weak equivalences and fibrations detected underneath) rather than chosen freshly? Because the entire point of $\mathbf{Mod}_R$ is that a map of modules should be a homotopy equivalence exactly when it is one of the underlying objects — the module structure should not change *what counts as the same*, only restrict *which maps are allowed*. Detecting $\mathcal{W}$ and fibrations through $U$ enforces this; the cofibrations are then forced as the maps with the left lifting property, and the free functor $F$ generates them. This is the standard "right-transferred" or "projective" model structure, and it is the only one for which $F \dashv U$ is automatically a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]].

---

# The Definition

Let $(\mathcal{C}, \otimes, I)$ be a [[Def - Monoidal Model Category|monoidal model category]].

**Monoid.** A **monoid** in $\mathcal{C}$ is an object $R$ together with morphisms $\mu : R \otimes R \to R$ (multiplication) and $\eta : I \to R$ (unit) such that the associativity and unit diagrams commute (using the associator $\alpha$ and unitors $\lambda, \rho$ of $\mathcal{C}$). A monoid is **commutative** if $\mu \circ \beta_{R,R} = \mu$, where $\beta$ is the symmetry. (See [[Def - Monoid in a Monoidal Category]].)

**Module.** A **left module** over a monoid $R$ is an object $M$ with an action $a : R \otimes M \to M$ such that
$$a \circ (\mu \otimes 1_M) = a \circ (1_R \otimes a) \circ \alpha_{R,R,M}, \qquad a \circ (\eta \otimes 1_M) = \lambda_M,$$
i.e. the action is associative with $\mu$ and unital with $\eta$. A **morphism of $R$-modules** $f : M \to N$ is a map in $\mathcal{C}$ commuting with the actions: $f \circ a_M = a_N \circ (1_R \otimes f)$. These form the category $\mathbf{Mod}_R$.

**The model structure.** Suppose $\mathcal{C}$ is cofibrantly generated and satisfies the **monoid axiom**:

> **(Monoid Axiom).** Every map in the class
> $$\big(\{(\text{trivial cofibration}) \otimes X : X \in \mathcal{C}\}\big)\text{-cell}$$
> — that is, every transfinite composite of pushouts of maps $j \otimes X$ with $j$ a trivial cofibration and $X$ arbitrary — is a weak equivalence.

Then $\mathbf{Mod}_R$ is a cofibrantly generated model category in which a morphism is a **weak equivalence** or a **fibration** if and only if its underlying map in $\mathcal{C}$ is, and the **cofibrations** are determined by the left lifting property. The generating (trivial) cofibrations are $\{R \otimes i : i \in I\}$ and $\{R \otimes j : j \in J\}$, the free modules on the generators of $\mathcal{C}$. The free-forgetful adjunction $F = R \otimes - \dashv U$ is then a [[Def - Quillen Adjunction and Quillen Equivalence|Quillen adjunction]]. (This is the Schwede–Shipley theorem; for commutative $R$ and a further "commutative monoid axiom", the category of $R$-algebras and of commutative $R$-algebras inherits a model structure too.)

---

# Categorical / Structural Definition

Structurally, $\mathbf{Mod}_R$ is the category of **algebras for the monad** $R \otimes -$ on $\mathcal{C}$. A [[Def - Monoid in a Monoidal Category|monoid]] $R$ makes the endofunctor $T = R \otimes -$ into a [[Def - Monad and Comonad|monad]]: the multiplication $\mu_T : TT = R \otimes R \otimes - \to R \otimes - = T$ is $\mu \otimes 1$, and the unit $\eta_T : 1 \to T$ is $\eta \otimes 1$. An $R$-module is precisely a $T$-algebra, and $\mathbf{Mod}_R$ is the Eilenberg–Moore category of $T$. From this angle the model structure on $\mathbf{Mod}_R$ is a *transferred* (right-induced) model structure along the monadic forgetful functor $U : \mathbf{Mod}_R = \mathcal{C}^T \to \mathcal{C}$, and the monoid axiom is exactly the condition that makes the transfer along this monad valid.

The internal-hom side is equally structural: when $\mathcal{C}$ is closed and $R$ is commutative, $\mathbf{Mod}_R$ is *itself* a closed symmetric monoidal category, with tensor $- \otimes_R -$ (the coequalizer of the two actions $M \otimes R \otimes N \rightrightarrows M \otimes N$, exactly as for ordinary modules) and internal hom $\underline{\mathrm{Hom}}_R(M, N)$ (the equalizer carving out the $R$-linear maps inside $[M, N]$). Under the monoid axiom this descends to a monoidal model structure on $\mathbf{Mod}_R$, so the entire apparatus of this chapter *re-runs one level up*: there is a derived tensor $\otimes^{\mathbf{L}}_R$ on $\mathrm{Ho}(\mathbf{Mod}_R)$, computing the relative Tor over the homotopical ring $R$.

From the (∞,1)-perspective, $\mathbf{Mod}_R$ presents the ∞-category of modules over the **$E_1$- (or $E_\infty$-) algebra** that $R$ presents — the homotopical refinement of "modules over a ring", and the setting of Lurie's *Higher Algebra*.

---

# Relate to Other Fields / Compression

Modules over a monoidal model category are the homotopical version of [[Def - Module|modules over a ring]], with $\otimes$ replacing the underlying multiplication and weak equivalences replacing equalities. The compression is exact: take $\mathcal{C} = \mathbf{Ab}$ with the trivial model structure and $\otimes_{\mathbb{Z}}$; a monoid is a [[Def - Ring|ring]] $R$, a module is an ordinary $R$-module, and the "model structure" is trivial. Now keep the algebra but enrich the homotopy theory — pass to $\mathbf{Ch}(R)$ or to spectra — and the *same* definitions produce DGAs and ring spectra and their derived module categories. The single template "monoid in $\mathcal{C}$, module = object with action, transfer the model structure" specializes to ordinary ring theory, to differential graded algebra, and to the homotopy theory of ring spectra.

**True name:** a module over a monoidal model category is **"an algebra for the monad $R \otimes -$, with its homotopy theory created underneath by the forgetful functor."** The operational reflex: to put homotopy theory on modules, do not invent weak equivalences — *inherit* them from $\mathcal{C}$ and generate cofibrations freely, and check the monoid axiom to license the transfer. When you see "$R$-modules in a monoidal model category", picture "$\mathbf{Ch}(R)$ or module spectra, with quasi-isomorphisms (resp. stable equivalences) detected on underlying objects".

---

# Examples / Corollaries

**Is an instance — ordinary modules over a ring.** Take $\mathcal{C} = (\mathbf{Ab}, \otimes_{\mathbb{Z}})$ with the trivial model structure (isomorphisms only). A monoid is a [[Def - Ring|ring]] $R$, a module is an ordinary [[Def - Module|R-module]], and $\mathbf{Mod}_R$ is the ordinary module category with its trivial model structure. This degenerate case confirms the definitions reduce to classical algebra when the homotopy theory is switched off.

**Is an instance — differential graded modules over a DGA.** Take $\mathcal{C} = \mathbf{Ch}(k)$ over a field $k$, with quasi-isomorphisms. A monoid is a differential graded algebra $A$, a module is a DG $A$-module, and $\mathbf{Mod}_A$ has the projective model structure (quasi-isomorphisms, degreewise epis as fibrations). Its homotopy category is the derived category $D(A)$, and the derived tensor $- \otimes^{\mathbf{L}}_A -$ computes the relative $\mathrm{Tor}^A_*$. This is the home of derived Morita theory.

**Is an instance — module spectra over a ring spectrum.** Take $\mathcal{C}$ = symmetric spectra with the smash product. A monoid is a **ring spectrum** $R$, a module is a module spectrum, and $\mathbf{Mod}_R$ inherits a model structure by Schwede–Shipley (symmetric spectra satisfy the monoid axiom). The Eilenberg–Mac Lane spectrum $HR$ of an ordinary ring recovers $\mathbf{Ch}(R)$ up to equivalence; the sphere spectrum $\mathbb{S}$ gives spectra themselves, since $\mathbf{Mod}_{\mathbb{S}} \simeq$ spectra. This is the central example: the entire subject of structured ring spectra lives here.

**Is NOT an instance — modules when the monoid axiom fails.** If $\mathcal{C}$ is a monoidal model category that does *not* satisfy the monoid axiom, the transferred classes on $\mathbf{Mod}_R$ need not satisfy the factorization axiom: the would-be trivial cofibrations, built by attaching free cells $R \otimes j$, can fail to be weak equivalences. Then $\mathbf{Mod}_R$ is *not* a model category. This is the precise role of the monoid axiom — it is what separates "modules form a category" (always true) from "modules form a model category" (needs the axiom).

**Is NOT an instance — the underlying object of a module is not a module structure.** A common confusion: an object $M \in \mathcal{C}$ is not the same as an $R$-module, even when one exists on it. The *action* $a : R \otimes M \to M$ is extra data, and different actions give different modules with the same underlying object. (For $R = k[x]$ and $M = k^n$, an action is a choice of $n \times n$ matrix — the same vector space carries many module structures.) The forgetful functor $U$ remembers the object and forgets the action; it is faithful but very far from injective on objects.

**Calibration check.** Verify that $R$ itself is a module over $R$ (action $= \mu$), the **free module of rank one**, and that it is the unit for $\otimes_R$ when $R$ is commutative. Verify that the free functor $F = R \otimes -$ is left adjoint to $U$ (a map $R \otimes X \to M$ of modules is the same as a map $X \to M$ in $\mathcal{C}$, by the action). If you can explain *why* the monoid axiom is needed in addition to the pushout-product axiom — because building cofibrations of modules tensors trivial cofibrations against the possibly-non-cofibrant $R$, where the pushout-product axiom's guarantee (cofibrant factor only) runs out — you have understood the role of the axiom.

---

# Unlocked by This

> [!tip] Brave New Algebra and Structured Ring Spectra *(from Stable Homotopy Theory)*
> Modules over ring spectra are the setting for **topological Hochschild and cyclic homology (THH, TC)**, **Galois extensions of ring spectra**, and the chromatic approach to stable homotopy via $E_n$- and Morava-$K$-theory module categories. The whole program of "commutative algebra over the sphere spectrum" is the homotopy theory of $\mathbf{Mod}_R$ for **$E_\infty$-ring spectra** $R$.

> [!tip] Derived Morita Theory and Tilting *(from Derived / Homological Algebra)*
> For DGAs $A, B$, a derived equivalence $D(A) \simeq D(B)$ is detected by a tilting module/complex, and the homotopy theory of $\mathbf{Mod}_A$ is what makes derived Morita theory precise. Two rings are derived-equivalent exactly when their module model categories are Quillen-equivalent — a direct application of comparing $\mathbf{Mod}_R$ across monoids.

> [!tip] Algebras over Operads and $E_\infty$/$A_\infty$-Structures *(from Higher Algebra)*
> The pattern "monoid in $\mathcal{C}$, then modules" generalizes to **algebras over an operad** in $\mathcal{C}$: an $A_\infty$-algebra is a monoid up to coherent homotopy, an $E_\infty$-algebra a commutative one. Under the monoid axiom (and its operadic refinements), algebras over a cofibrant operad inherit model structures, and the homotopy theory of $\mathbf{Mod}_R$ is the associative special case.
