---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Least Squares Data Fitting"
tags: [algebra, linear-algebra, applied, classification, machine-learning]
---

# Notation

In binary classification, the outcome $y \in \{-1, +1\}$ encodes a categorical label (true/false, spam/not-spam, healthy/diseased). The classifier is a function $\hat{f} : \mathbb{R}^n \to \{-1, +1\}$. In multi-class classification, $y \in \{1, 2, \ldots, K\}$ and the classifier is $\hat{f} : \mathbb{R}^n \to \{1, \ldots, K\}$. The *prediction confidence* (in binary) is the real-valued output $\tilde{f}(x)$ before applying the sign function. The *decision threshold* $\alpha$ shifts the boundary: $\hat{f}(x) = \mathrm{sign}(\tilde{f}(x) - \alpha)$.

A *confusion matrix* tabulates the $K^2$ possible (true label, predicted label) pairs across a dataset; the diagonal entries count correct predictions and the off-diagonal entries count errors. The *true positive rate* (recall) is $N_{tp}/N_p$; the *false positive rate* is $N_{fp}/N_n$.

---

# Axiom Motivation

You have a binary classification problem: predict a label $y \in \{-1, +1\}$ from a feature vector $x \in \mathbb{R}^n$. The honest approach is *logistic regression*: model $P(y = +1 | x) = \sigma(x^T \beta + v)$ where $\sigma$ is the logistic function, and fit $\beta, v$ by maximum likelihood. This is the right thing to do in any production setting and is one of the standard tools of statistics.

But Boyd makes a striking observation: if you simply pretend the discrete labels $\pm 1$ are continuous, run ordinary least squares regression, and threshold the result at zero, you get a perfectly reasonable classifier — and it can be derived from machinery already developed (LS data fitting from §13). The least squares classifier is a *demonstration of generality*: the LS toolkit, originally designed for continuous regression, can be repurposed for classification with no new mathematics needed.

Why does this work? The least squares regression fits the model $\tilde{f}(x) = x^T \beta + v$ to predict the labels $y \in \{-1, +1\}$ as if they were continuous. For a "typical" positive-class point, the LS fit predicts $\tilde{f}(x) \approx +1$; for a typical negative-class point, $\tilde{f}(x) \approx -1$. Then $\mathrm{sign}(\tilde{f}(x))$ recovers the label. The continuous output $\tilde{f}(x)$ can be interpreted as a confidence score: large positive means "very likely positive class," small negative means "barely negative class," etc.

The principled objection is that the LS loss penalizes a *correct* high-confidence prediction. If the true label is $+1$ and the LS regression predicts $\tilde{f}(x) = +1.5$, the squared residual is $(1.5 - 1)^2 = 0.25$ — the model is penalized for being "too confident," even though its classification is correct. Logistic regression does not have this defect; it has a loss function (the cross-entropy) that strictly rewards confident correct predictions. So LS classification is suboptimal at the loss-function level.

But the practical observation is that for many classification problems with relatively well-separated classes, LS classification works *almost as well* as logistic regression and is much faster (closed-form solution, no iterative optimization). The Iris dataset and the MNIST digit classification examples in Boyd show LS classifier error rates of 7-15%, comparable to what logistic regression achieves. The LS classifier is a useful baseline and a perfectly reasonable choice when extreme performance is not required.

The multi-class extension is the *one-versus-rest* construction: for each class $k$, fit a binary LS classifier $\tilde{f}_k$ to distinguish class $k$ from all other classes (encoded as $y^{(i)} = +1$ if class $k$, $-1$ otherwise). Predict $\hat{f}(x) = \arg\max_k \tilde{f}_k(x)$ — the class with the highest "confidence score." This is conceptually simple, fits $K$ binary classifiers, and uses the *same* design matrix $A$ for each (only the right-hand side $y$ changes); a single QR factorization of $A$ serves all $K$ fits.

The *decision threshold* $\alpha$ in $\hat{f}(x) = \mathrm{sign}(\tilde{f}(x) - \alpha)$ allows a deliberate trade-off between false-positive and false-negative rates. Lowering $\alpha$ (towards $-\infty$) predicts $+1$ more often, increasing true positives but also increasing false positives. Raising $\alpha$ does the opposite. Sweeping $\alpha$ traces out the *receiver operating characteristic* (ROC) curve in the (false-positive rate, true-positive rate) plane. The ROC curve characterizes the *capability* of the classifier independent of any particular threshold choice.

The reader has now invented the LS classifier framework. The remaining content is the practical observation that this simple recipe gives competitive performance on many classification problems, and that the same multi-objective LS techniques (regularization, validation, cross-validation) apply unchanged.

---

# The Definition

> **Definition (Least Squares Classifier).** For a binary classification problem with feature vector $x \in \mathbb{R}^n$ and label $y \in \{-1, +1\}$, the *least squares classifier* is constructed as follows:
> 1. Fit a real-valued least squares regression model
> $$\tilde{f}(x) = \theta_1 f_1(x) + \cdots + \theta_p f_p(x)$$
> by minimizing $\sum_i (y^{(i)} - \tilde{f}(x^{(i)}))^2$, treating the binary labels as continuous.
> 2. The classifier is
> $$\hat{f}(x) = \mathrm{sign}(\tilde{f}(x) - \alpha),$$
> where $\alpha$ is a chosen *decision threshold* (default $\alpha = 0$). Here $\mathrm{sign}(a) = +1$ for $a \geq 0$ and $-1$ for $a < 0$.
>
> For *$K$-class classification* (with labels $y \in \{1, \ldots, K\}$), the *one-versus-rest least squares classifier* is constructed by fitting $K$ binary classifiers $\tilde{f}_1, \ldots, \tilde{f}_K$ — the $k$-th distinguishes class $k$ from the rest — and predicting
> $$\hat{f}(x) = \arg\max_{k=1,\ldots,K} \tilde{f}_k(x).$$
> Equivalently, $\hat{f}(x) = \arg\max_k (\tilde{f}_k(x) - \alpha_k)$ for chosen offsets $\alpha_k$ (default $\alpha_k = 0$).

---

# Relate to Other Fields / Compression

**True name:** the LS classifier is *linear regression on encoded class labels, thresholded at zero*. The deep structural fact is that *the discriminant function is linear* (or, with basis functions, linear-in-parameters); the discrete output is just the sign. This is the same class of decision boundaries as logistic regression and linear discriminant analysis (LDA), differing only in the loss function used to fit them.

This is the same construction as:
- **Logistic Regression**: same linear discriminant function $x^T \beta + v$, different loss (cross-entropy instead of squared). Logistic regression is the principled choice; LS is a fast approximation.
- **Linear Discriminant Analysis (LDA)**: in a special probabilistic setting (Gaussian class-conditional distributions with shared covariance), the optimal decision boundary is linear and turns out to coincide (up to a constant) with the LS classifier in a particular limit.
- **Perceptron Algorithm**: an iterative method for fitting a linear discriminant by minimizing a different loss (the perceptron loss). For linearly separable data, the perceptron converges; for non-separable data, it can oscillate. LS classification handles non-separable data gracefully (it's a fixed quadratic problem) but is more sensitive to outliers.
- **Support Vector Machines (SVM)**: another linear-discriminant classifier with a different loss (hinge loss) and an emphasis on maximum-margin separation. SVMs handle the imbalanced/extreme classification problems better than LS.

---

# Examples / Corollaries

*Example 1 (binary classification on Iris).* On Fisher's Iris dataset, fit a binary LS classifier distinguishing Iris Virginica from Iris Setosa + Iris Versicolour, using the four flower measurements as features. The classifier achieves an error rate of about 7.3% on the full dataset, with stability confirmed by 5-fold cross-validation showing test error rates in the 3-17% range across folds. See [[Ex - Binary classifier via least squares]].

*Example 2 (multi-class classification on MNIST digits).* For the 10-class MNIST handwritten digit classification problem, build a one-versus-rest LS classifier with 10 binary classifiers, each using the 494 non-trivial pixel intensities as features. The error rate is 14.5% on training and 13.9% on test — competitive but not state-of-the-art. Adding 5000 random ReLU features (feature engineering!) reduces the error rate to 1.5% on training and 2.6% on test, well below human-level performance.

*Example 3 (ROC curve).* Vary the decision threshold $\alpha$ in $\hat{f}(x) = \mathrm{sign}(\tilde{f}(x) - \alpha)$ from large negative (predicts $+1$ always) to large positive (predicts $-1$ always). Plot the resulting (false-positive rate, true-positive rate) pairs to get the ROC curve. The *area under the curve* (AUC) is a summary measure of classifier quality independent of threshold choice; a perfect classifier has AUC 1, a random classifier has AUC 0.5.

*Example 4 (is NOT logistic regression — same discriminant, different fit).* Both LS classifier and logistic regression learn a linear discriminant of the form $x^T \beta + v$. The difference is only in *how* $\beta, v$ are fit. LS minimizes squared residuals (treating labels as continuous); logistic regression maximizes log-likelihood (treating labels as Bernoulli). On most problems, the resulting decision boundaries are very similar; on hard problems with rare classes or overlap, logistic regression tends to be more accurate, especially when calibrated probabilities are required.

*Example 5 (skewed-threshold trade-off).* In a medical diagnosis classifier where false negatives (missing a disease) are much worse than false positives (alarming a healthy patient), shift the decision threshold $\alpha$ to a negative value. This makes the classifier predict $+1$ ("diseased") more readily, increasing the true positive rate at the cost of more false positives. The ROC curve quantifies exactly this trade-off.

**Calibration check.** Verify: (i) the LS classifier reduces to ordinary LS regression with thresholding when the labels are $\pm 1$; (ii) for a one-versus-rest multi-class classifier with $K = 2$ classes, only one binary classifier needs to be fit (the second is its negation); (iii) the $K$ one-versus-rest classifiers can be computed by a single QR factorization of $A$ (the design matrix), with $K$ separate back-substitutions for the $K$ different right-hand sides.

---

# Unlocked by This

> [!tip] Logistic Regression and the Cross-Entropy Loss *(from Statistics / ML)*
> The principled probabilistic upgrade of the LS classifier is **logistic regression**, which replaces the squared loss with the cross-entropy (Bernoulli log-likelihood). The linear discriminant function remains the same; only the loss function changes. Logistic regression yields *calibrated* probability estimates (its output $\sigma(x^T \beta)$ is a probability) and is the right tool when probability calibration matters. It cannot be solved in closed form — requires Newton-Raphson or stochastic gradient — but is computationally tractable and almost always preferred in practice.

> [!tip] Receiver Operating Characteristic *(from Signal Detection)*
> The ROC curve framework, born in WWII radar research and ubiquitous in ML, applies to *any* score-based classifier — not just LS. A classifier outputs a real-valued score; sweeping the decision threshold traces the ROC. The area under the ROC curve (AUC) is a fundamental classifier metric, equal to the probability that a random positive example has a higher score than a random negative example. Generalizations include the precision-recall curve (more informative for very imbalanced problems) and the lift chart (used in marketing).

> [!tip] Support Vector Machines *(from Machine Learning)*
> Where LS minimizes squared residuals on $\pm 1$ targets, **SVMs** minimize the hinge loss $\max\{0, 1 - y \tilde{f}(x)\}$, which penalizes only misclassified or marginal-correct predictions, ignoring confident correct ones. This focuses the model on *the boundary*, giving "maximum margin" classification. SVMs require quadratic programming (not closed-form LS), but are often more robust, especially with kernel feature maps. The whole SVM theory can be derived as a constrained-LS-like dual problem; the LS classifier is a softer cousin.
