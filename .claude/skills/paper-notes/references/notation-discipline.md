# Notation Discipline — Typing, Terminology, Prose

This document holds Rules 3, 4, and 7 of the paper-notes skill in full. The SKILL.md body summarises them and points here. Read this before writing any statement, definition, or proof. The governing prose voice is the reference thesis (`paper_source/Chiang Sung En-Thesis.pdf`); this document is about *precision*, and the SKILL's Prose Standard is about *voice* — they work together.

---

## Rule 3 — Full typing

**Every object carries its type the first time it appears, and the type is on the page.** A type is not a name. Naming a symbol $p$ "the density" is not typing it; typing it is saying *density of which measure, with respect to which reference measure, on which space*. The reader who bottoms out at the undergraduate floor cannot supply a missing type from context — they have not seen the field's conventions — so every type must be stated.

### What "the type" means, object by object

- **A map / function.** Domain and codomain: `$f : X \to Y$`. Say what $X$ and $Y$ are (which sets, which spaces). If $f$ is only defined on a subset, say so. If $f$ is linear / continuous / measurable / smooth, that adjective is part of the working type — state it when it is used.
- **An element.** The space it lives in: "$x \in X$", "$v \in V$ a real vector space", "$\omega \in \Omega$ a sample point", "$\gamma \in \pi_1(M)$ a homotopy class". Never let a symbol appear without the reader knowing the set it ranges over.
- **A measure.** *What it is a measure over* — the measurable space $(X, \mathcal{F})$ — **and** whether it is finite, $\sigma$-finite, or a probability measure. "$\mu$ a measure" is not a type; "$\mu$ a $\sigma$-finite measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$" is. For a density, name the reference measure: "$f = \frac{d\mu}{d\nu}$, the density of $\mu$ with respect to $\nu$".
- **A random variable.** The probability space it is defined on and the space it takes values in: "$X : (\Omega, \mathcal{F}, \mathbb{P}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$". Distinguish the random variable $X$ from a value $x$ it takes and from its distribution $P_X$ — three different types that sloppy notation conflates.
- **An operator.** What it acts on and what it produces: "$T : H \to H$ a bounded linear operator on a Hilbert space $H$", "$\mathcal{L}$ acting on $C^2$ functions". If it has a domain smaller than the whole space, state the domain.
- **A distribution / probability object.** Whether $P$ is a distribution, a density, a measure, or a mass function — these are different types and the paper may slide between them. Pin down which.
- **A physical quantity.** Its units, and the convention if one is in force ("$c = 1$", "$\hbar = 1$"). A quantity and its units share a type; an equation whose two sides carry different units is a bug.

### Free, bound, and quantified status

State, for every symbol in a displayed statement, whether it is **free** (a fixed but arbitrary object the statement is about), **bound** (an integration or summation variable, local to the expression), or **quantified** (and over what set). The thesis is scrupulous about this — "for any subset $K_1, K_2 \subseteq V \setminus \{X_i, X_j\}$", "$\forall h \in \Gamma \setminus \{1\}$". The classic bug is a symbol that is bound inside a sum but reused free outside it, or a "for all $\varepsilon$" whose $\varepsilon$ silently becomes a specific value. When you write a statement, name the quantifier of every variable in it before or as it appears.

### The signature table

The companion page's **Notation and Standing Conventions** section carries a signature table: every symbol used anywhere in the paper, with its type, in one place, so a reader dropping into any section can resolve a symbol without hunting. Format:

```markdown
| Symbol | Type | Meaning |
|---|---|---|
| $\Omega$ | set | sample space |
| $\mathbb{P}$ | probability measure on $(\Omega, \mathcal{F})$ | the underlying probability |
| $X_i$ | random variable $(\Omega,\mathcal{F},\mathbb{P}) \to (\mathcal{X}_i, \mathcal{B})$ | the $i$-th observed variable |
| $\mu$ | $\sigma$-finite measure on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ | reference measure for densities |
| $\Delta_L P$ | signed measure on the product space | Lancaster interaction measure |
```

Repeat the type inline at first use in each section too — the table is the index, not a substitute for typing at point of use. A returning reader should never have to scroll to the table mid-proof.

### Type-check before you write

Before committing any expression to the page, check that it type-checks: both sides of an equation are the same kind of object (a measure equals a measure, a number equals a number, not a random variable equated to its distribution); a function is applied only to arguments in its domain; a sum ranges over a stated index set; a conditional expectation is of an integrable random variable given a $\sigma$-algebra. The thesis's independence computations are worth emulating precisely because every intermediate line is a well-typed equation between distributions. If an expression does not type-check, either the paper has an abuse of notation you must expand and explain, or you have made an error — resolve it before writing, and if it is the paper's abuse, say so and give the precise form.

### One symbol, one meaning

A symbol means exactly one thing throughout the note-set. When the paper reuses a letter for two objects (a spectral parameter $s$ and a proper-time variable $s$), rename one with a distinct glyph and record the choice in the signature table and a standing-conventions note. Do not write "$s$ means two things depending on context" — that is exactly the load the floor-level reader cannot carry.

**Collisions between the paper's notation and a shared atomic note's.** The atomic prerequisite notes and their recalls are reusable vault assets, so they **stay in the standard notation** of their own field (a measure is $\mu$, a spectral variable is $\lambda$) — a paper-local rename must never be pushed into them. When the paper's local use of a letter clashes with the standard symbol a linked recall or atomic note uses for a prerequisite, do the reconciliation **on the companion side, not in the shared note**, one of two ways: (a) keep the standard symbol for the prerequisite and rename the paper's clashing use, noting the substitution wherever the paper's original notation is displayed ("the paper writes $\mu$ for its mean; here $\mu$ is reserved for the measure, so its mean is written $m$"); or (b) when a recall imports a symbol that clashes with the companion's local meaning, state the translation inline in that recall ("the source note writes this density as $\mu$; on this page $\mu$ is the measure, so read it as $\rho$"). State the reconciliation in the companion's Standing Conventions so the reader meets it once, up front.

---

## Rule 4 — Standard terminology only

**Name every concept with the name the literature uses, and attribute the field.** The reader must be able to take any term from the notes, search it, and land on the same concept in a textbook or paper. Coined names break that guarantee.

### What to do

- **Use the established name and say whose it is.** "This quantity is the **Radon–Nikodym derivative** $\frac{d\mu}{d\nu}$." "This is the **Fenchel–Legendre transform** (called the Legendre transform in the smooth, convex case and the convex conjugate in optimisation)." "The condition is **faithfulness** of the distribution to the graph, in the causal-inference sense." Attribution is not decoration — it tells the floor-level reader which body of results the object connects to.
- **Give both names when subfields differ.** Many objects carry different names in different communities: *relative entropy* = *Kullback–Leibler divergence*; *characteristic function* (probability) vs. *Fourier transform of the measure*; *precision matrix* = *inverse covariance*; *potential* vs. *log-density*. State both, so a reader coming from either side recognises it.
- **When a concept has no standard name, say so and describe it.** If the paper introduces a genuinely new object, use the paper's own name for it, in quotes on first use, attributed to the paper ("what the authors call the *interaction hypergraph*"), and then describe it by its type and role. Do not silently promote a paper's ad-hoc notation to a general term, and do not invent a tidier name of your own.

### What not to do

- **No coined compound-noun jargon.** Do not manufacture a term like "the surprise-excess functional" for the KL divergence because it reads nicely. Use the real name.
- **No Capitalised pseudo-terms.** Do not invent Capitalised Names for note-local concepts ("the Standing Setup", "the Discharge Table") and use them as if they were mathematics. Describe the thing in plain words.
- **No repurposing of standard symbols.** Do not use $\otimes$ for something that is not a tensor product, $\ll$ for anything but absolute continuity, $\perp$ for anything but independence/orthogonality in a context where that is expected, $\nabla$ for a non-gradient/connection object, without a loud, explicit redefinition — and prefer a different glyph instead. A standard symbol carries a standard type-expectation the floor reader relies on.
- **No abbreviation in prose.** Following the vault convention: write "with respect to", "if and only if", "almost everywhere" in prose, not "w.r.t.", "iff", "a.e." (the symbol $\iff$ in a formal statement is fine; the abbreviation in a sentence is not).

The test: could the reader take any noun phrase in the notes, type it into a search engine, and find the same concept the notes mean? If not, the term is coined and must be replaced with the standard one.

---

## Rule 7 — Prose over compression

**Comprehensive standard prose is preferred to compact formalism, even when it runs several times longer.** The reference thesis is expansive on purpose: it re-explains the KL divergence three ways, it unpacks the bivariate case right after stating the general one, it computes a worked Möbius inversion in full right after giving the general formula. That length is the feature, not a flaw to be trimmed. The floor-level reader does not save time from a compressed page; they lose the ability to follow it.

### The rule in practice

- **Default to a sentence, not a symbol.** When a step can be said in words the reader already commands, say it in words. Reach for notation only when prose is *genuinely worse* — that is, for a computation, a precise quantified statement, a signature, or a manipulation whose whole content is symbolic. "The average surprise under $P$ when you assume $Q$ exceeds the minimum by exactly the divergence" is prose worth having *alongside* $D_{KL}(P\|Q) = H(P,Q) - H(P)$, not replaced by it.
- **Never write a formula that only restates a sentence.** If a displayed equation says nothing the preceding sentence did not already say, delete the equation (or delete the sentence and keep the equation with a word of unpacking — but do not keep both when they are the same content twice). The test for whether a formula earns its place: *does a reader who has the surrounding prose learn something from the formula that the prose did not give them?* If not, it is compression for its own sake.
- **Unpack, don't gesture.** "By a standard argument" and "it is easily seen" are compressions that fail the floor reader. Replace them with the argument. This is Rule 5 (gap-free proofs) meeting Rule 7: the expansion *is* the deliverable.
- **Unpack the general statement in its smallest concrete case, immediately after stating it.** Motivate a definition with plain-language prose, then state the general definition crisply, then immediately unpack it in the smallest concrete case in prose and numbers — as the thesis does with the bivariate Lancaster measure right after Definition 2.1.1 and the worked $\mathbb{Z}_3$ Möbius inversion right after Definition 2.1.3. The general statement is the opening move of the definition and the concrete case is the unpacking that follows; the numeric worked instance never substitutes for stating the general form first. (A *motivating scenario* in prose may precede the definition; the worked numbers come after it.)
- **Length is not the enemy; density-without-explanation is.** Expansive prose that re-explains and re-grounds is what this skill wants. What it does not want is a wall of symbols with no connective tissue, or — the opposite failure — padding that repeats without adding. Every paragraph should advance the reader's understanding; within that constraint, longer and more explained beats shorter and terser every time.

### Interaction with the other rules

Rule 7 is why the notes can be several times the length of the paper: the paper compresses (its readers are specialists); the notes decompress (its reader is not). Typing (Rule 3) and gap-free proofs (Rule 5) are both instances of decompression — they write out what the paper left implicit. Rule 4 keeps the decompressed prose anchored to standard names so the length buys comprehension rather than a private language. The thesis voice (Prose Standard) is the register in which all of this decompression is written.
