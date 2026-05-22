---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Least Squares Classifier"
  - "Def - Least Squares Data Fitting"
tags: [algebra, linear-algebra, applied, classification, machine-learning]
---

# Problem Statement

You are given $N$ data points $\{(x^{(i)}, y^{(i)})\}_{i=1}^N$ with $x^{(i)} \in \mathbb{R}^n$ (feature vector) and $y^{(i)} \in \{-1, +1\}$ (binary class label). Build a binary classifier $\hat{f} : \mathbb{R}^n \to \{-1, +1\}$ as follows.

1. *Train.* Fit a real-valued linear-in-features regression model $\tilde{f}(x) = x^T \beta + v$ to the labels $y^{(i)}$ (treating them as continuous) by ordinary least squares.
2. *Classify.* Define $\hat{f}(x) = \mathrm{sign}(\tilde{f}(x))$.

Apply this to Fisher's Iris dataset (150 samples, 4 features, 3 classes), distinguishing Iris Virginica ($y = +1$) from the other two species ($y = -1$). Compute the confusion matrix and error rate. Use 5-fold cross-validation to estimate the test error rate.

Then construct the *receiver operating characteristic* (ROC) curve by varying the decision threshold $\alpha$: $\hat{f}(x) = \mathrm{sign}(\tilde{f}(x) - \alpha)$.

**Recall:**

A [[Def - Least Squares Classifier|least squares classifier]] is built by fitting a real-valued LS regression to binary labels and thresholding. The classifier's *confusion matrix* tabulates predicted vs. actual labels. The *true positive rate* is $N_{tp}/N_p$, the *false positive rate* is $N_{fp}/N_n$. The *ROC curve* plots TPR vs. FPR as $\alpha$ varies.

[[Def - Validation (Training and Test Error)|Cross-validation]] partitions the data into folds and rotates the held-out fold to estimate test error.

---

# Convergent Strategy

**Problem class:** This is a *binary classification via continuous-regression-thresholded* problem. The class is "use LS regression on $\pm 1$ labels as a classifier, evaluated by confusion matrix and ROC analysis." The class transfers any LS regression problem to classification by changing the labels and adding a sign-thresholding step.

**Assumption pattern:** Binary labels are encoded as $\pm 1$ (rather than $\{0, 1\}$); the labels are treated as continuous targets for the regression. The features are real-valued $n$-vectors; the design matrix $A$ has rows $(x^{(i)})^T$ with an additional column for the intercept. The assumption "columns of $A$ are linearly independent" almost always holds for real datasets (one would have to have features that are linear combinations of others, which is rare in practice).

**Theorem routing:** Apply [[Thm - Existence and Uniqueness of Least Squares Solution]] to get the unique LS regression $\tilde{f}(x) = x^T \beta + v$. The classifier is $\hat{f}(x) = \mathrm{sign}(\tilde{f}(x))$; analyze its confusion matrix on the training data. Apply [[Def - Validation (Training and Test Error)|cross-validation]] to estimate test error. Sweep $\alpha$ to construct the ROC curve, noting how it traces the achievable (FPR, TPR) points.

**Key decision point:** The non-obvious choice is *how to encode the labels*. Some sources use $y \in \{0, 1\}$, others $y \in \{-1, +1\}$. The two encodings give the same classifier (up to a shift in the intercept), but the $\pm 1$ encoding has the cleaner symmetry: the LS fit $\tilde{f}(x)$ has the interpretation of "how confidently positive" the prediction is, with magnitude proportional to confidence and sign giving the class. Decision-theoretic interpretation is sharpest with $\pm 1$.

---

# Legal Operations Used

1. **Compute the LS fit via QR factorization.** (Operation 2 from the topic page.) Fit the regression $\tilde{f}(x) = x^T \beta + v$ to the labels via QR. The fit is closed-form and fast — a single LS solve.

2. **Apply the sign function for classification.** (Operation 11 of the topic page in the multi-class case; here, just a thresholding step.) After computing $\tilde{f}(x^{(i)})$ on each training point, predict the class as $\mathrm{sign}(\tilde{f}(x^{(i)}))$. Errors are when the sign disagrees with the actual label.

3. **Sweep the decision threshold $\alpha$ to construct the ROC curve.** This generates a family of classifiers parametrized by $\alpha$; each $\alpha$ gives a (FPR, TPR) point on the ROC curve. The shape of the ROC tells you the classifier's *capability* independent of threshold choice.

---

# Hints

> [!note]- Hint 1
> The LS classifier treats the binary labels $\pm 1$ as if they were continuous and fits an LS regression. The classifier is $\mathrm{sign}(\tilde{f}(x))$ where $\tilde{f}(x) = x^T \beta + v$.

> [!note]- Hint 2
> The design matrix $A$ has rows $((x^{(i)})^T, 1)$ — the feature vector plus an intercept column. For the Iris dataset with 4 features, $A$ is $150 \times 5$. The LS solution $\hat{\theta} = (\beta_1, \beta_2, \beta_3, \beta_4, v)$ has 5 components, fit by solving $A^T A \hat{\theta} = A^T y$.

> [!note]- Hint 3
> For the Iris Virginica vs. others problem, Boyd reports coefficients $\beta = (-0.0918, 0.406, 0.00798, 1.10)$ and $v = -2.39$, with overall error rate $\approx 7.3\%$. The largest-magnitude coefficient is $\beta_4 = 1.10$, on the petal width feature — petal width is the most discriminative attribute.

> [!note]- Hint 4
> For 5-fold cross-validation: partition the 150 samples into 5 folds of 30 each (10 Virginica + 20 other in each, if stratified). Fit on 4 folds, evaluate on the 5th, rotate. The cross-validated test error rates vary from $\approx 3.3\%$ to $\approx 17\%$ across folds (the variation is large because of the small fold size — only 30 test points), with a mean cross-validation error $\approx 7-10\%$ — consistent with the training error.

> [!note]- Hint 5 (for ROC)
> The ROC curve is constructed by varying $\alpha \in (-\infty, +\infty)$ and plotting (FPR($\alpha$), TPR($\alpha$)) for each. As $\alpha$ increases, both FPR and TPR decrease; as $\alpha$ decreases, both increase. The ROC has the canonical concave shape, with the area under the curve (AUC) being a summary measure of classifier quality.

---

# Solution

The proof has three parts. Step 1 fits the LS regression and computes the confusion matrix; this is the basic classification step. Step 2 runs 5-fold cross-validation to estimate test error and check parameter stability. Step 3 constructs the ROC curve by varying the decision threshold and interprets the resulting trade-off between false positives and false negatives.

**Step 1: Fit the LS regression and compute the confusion matrix.**

Encode $y^{(i)} = +1$ for Iris Virginica and $y^{(i)} = -1$ for Iris Setosa and Versicolour. Form the $150 \times 5$ design matrix $A$ (4 feature columns + 1 intercept column). Apply [[Thm - Least Squares via QR Factorization]] to compute $\hat{\theta} = (\hat{\beta}, \hat{v}) = (A^T A)^{-1} A^T y$.

> [!note]- Derivation
> Boyd computes (using all 150 samples):
> $$\hat{\theta} = (-0.0918, 0.406, 0.00798, 1.10, -2.39).$$
> The classifier is $\hat{f}(x) = \mathrm{sign}(x^T \hat{\beta} + \hat{v}) = \mathrm{sign}(-0.092 x_1 + 0.406 x_2 + 0.008 x_3 + 1.10 x_4 - 2.39)$.
>
> Applying this to each of the 150 training samples and tabulating predicted vs. actual labels gives the confusion matrix:
> $$\begin{array}{c|cc|c} & \hat{y} = +1 & \hat{y} = -1 & \text{Total} \\ \hline y = +1 & 46 & 4 & 50 \\ y = -1 & 7 & 93 & 100 \\ \hline \text{Total} & 53 & 97 & 150 \end{array}.$$
> The total errors are $4 + 7 = 11$ out of 150 samples, giving error rate $\approx 7.3\%$. The true positive rate is $46/50 = 92\%$, the false positive rate is $7/100 = 7\%$.

**Step 2: 5-fold cross-validation.**

Randomly partition the 150 samples into 5 folds of 30 each. For each fold $k = 1, \ldots, 5$:
- Fit the LS classifier on the other 4 folds (120 samples).
- Evaluate the classifier on the held-out fold (30 samples).
- Record the test error rate.

> [!note]- Derivation
> Boyd reports for one particular random partition:
> | Fold | Train error | Test error |
> | --- | --- | --- |
> | 1 | 6.7% | 3.3% |
> | 2 | 5.8% | 10.0% |
> | 3 | 7.5% | 3.3% |
> | 4 | 6.7% | 16.7% |
> | 5 | 8.3% | 3.3% |
>
> The mean test error is $\approx 7.3\%$, consistent with the training-set error. The large fold-to-fold variation in test error ($3.3\%$ to $16.7\%$) is due to the small test set size (only 30 samples — a single misclassified sample flips the test error by $3.3\%$). The mean is the more reliable estimate of true test error.
>
> Looking at the model parameters fit on each fold, they vary from $\beta_4 = 0.94$ to $\beta_4 = 1.25$ — modest variation suggesting reasonable parameter stability. The classifier as a whole is consistent in its behavior across folds, even though individual coefficients vary somewhat.

**Step 3: Construct the ROC curve.**

The modified classifier is $\hat{f}_\alpha(x) = \mathrm{sign}(\tilde{f}(x) - \alpha)$. As $\alpha$ varies from $-\infty$ to $+\infty$, the classifier transitions from "predict $+1$ always" (TPR = 1, FPR = 1) to "predict $-1$ always" (TPR = 0, FPR = 0).

> [!note]- Derivation
> For each candidate $\alpha$ value (say, on a grid of 100 values from $-2.5$ to $+2.5$):
> - Apply $\hat{f}_\alpha$ to all 150 samples.
> - Tabulate confusion matrix.
> - Compute TPR($\alpha$) = (number of $y = +1$ with $\hat{f}_\alpha = +1$) / (number of $y = +1$) and FPR($\alpha$) = (number of $y = -1$ with $\hat{f}_\alpha = +1$) / (number of $y = -1$).
> - Plot (FPR($\alpha$), TPR($\alpha$)) as a point.
>
> The resulting curve starts at (1, 1) for very negative $\alpha$, goes to (0, 0) for very positive $\alpha$, and follows a concave shape in between. The "knee" of the curve (corresponding to $\alpha \approx 0$) achieves the standard error rate of $\approx 7\%$; shifting $\alpha$ moves along the curve, trading FPR against TPR. The *area under the curve* (AUC) for this classifier is approximately $0.96$ — close to the perfect-classifier value of 1.

> [!note]- Complete formal solution
> *Step 1 (Training fit):* Form the design matrix $A \in \mathbb{R}^{150 \times 5}$ with rows $((x_1^{(i)}, x_2^{(i)}, x_3^{(i)}, x_4^{(i)}, 1))$. Solve $\hat{\theta} = (A^T A)^{-1} A^T y$ via QR factorization (per [[Thm - Least Squares via QR Factorization]]). The resulting $\hat{\theta} = (-0.092, 0.406, 0.008, 1.10, -2.39)$ gives $\tilde{f}(x) = -0.092 x_1 + 0.406 x_2 + 0.008 x_3 + 1.10 x_4 - 2.39$.
>
> *Step 1 (Classification):* For each training sample $x^{(i)}$, compute $\tilde{f}(x^{(i)})$ and predict $\hat{y}^{(i)} = \mathrm{sign}(\tilde{f}(x^{(i)}))$. Comparing with actual $y^{(i)}$ gives the confusion matrix (above), with overall error rate $11/150 = 7.3\%$.
>
> *Step 2 (Cross-validation):* Randomly partition into 5 folds of 30 each. For each held-out fold, fit on the remaining 120 and evaluate on the held-out 30. Mean test error across folds $\approx 7.3\%$, consistent with training error and confirming the model is not overfit.
>
> *Step 3 (ROC):* For each candidate $\alpha$, compute the classifier $\hat{f}_\alpha = \mathrm{sign}(\tilde{f} - \alpha)$ and tabulate confusion matrix. Plot TPR vs. FPR. The resulting curve has AUC $\approx 0.96$. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to fit a *logistic regression* model instead, which would be statistically more principled. Logistic regression uses the cross-entropy loss $-\sum [y^{(i)} \log \sigma(\tilde{f}(x^{(i)})) + (1 - y^{(i)}) \log(1 - \sigma(\tilde{f}(x^{(i)})))]$ rather than the squared loss. This *is* a better approach in principle — the cross-entropy is the correct log-likelihood for binary outcomes. But it requires iterative optimization (Newton-Raphson or gradient descent), losing the closed-form benefit of LS. For most problems, LS classification and logistic regression give very similar decision boundaries; LS is preferred for speed and simplicity, logistic for accuracy and calibration. Logistic regression is the topic of Boyd Ch 18 ([[Linear Algebra XII — Applied III — Nonlinear Least Squares]]).

---

# Key Takeaways

**LS classification is a fast, closed-form baseline; logistic regression is the principled choice.**

The LS classifier achieves the same linear decision boundary as logistic regression, but fits via closed-form LS rather than iterative optimization. For most classification problems with well-separated classes, the two give nearly identical decision boundaries and comparable accuracy. The LS classifier is appropriate when (a) you want a quick baseline, (b) the closed-form fit is computationally important, or (c) you don't need calibrated probability estimates. Logistic regression is appropriate when (a) you need calibrated probabilities, (b) the classes are imbalanced or hard, or (c) you can afford iterative training. The trigger for using LS classification: "I want a classifier *right now*, with no iterative training and no probability calibration."

**ROC analysis decouples classifier capability from threshold choice.**

The ROC curve summarizes the classifier's discrimination ability *regardless of any specific threshold*. The AUC (area under the curve) is a single number characterizing this ability: AUC = 1 means perfect classification at some threshold; AUC = 0.5 means random guessing. For a fixed dataset, *the same classifier* (same $\tilde{f}$) gives the same ROC, while choosing different $\alpha$ moves along the curve. This is the principled way to compare classifiers: ROC-AUC is threshold-independent, so it captures the inherent discrimination quality. For unbalanced classification problems, the precision-recall curve is preferred over ROC.

**Cross-validation gives a more reliable error estimate than a single train/test split.**

A single 80/20 train/test split gives one estimate of test error; cross-validation gives 5 (for 5-fold), and their mean is more stable. The fold-to-fold variation in test error also provides a check for *parameter stability* — if the model's coefficients vary wildly across folds, the model is unstable (possibly overfit or near-collinear features); if coefficients are similar, the model is stable and the cross-validated error is a reliable generalization estimate. For the Iris problem, the small fold size (30 test samples) makes individual fold errors noisy, but the mean is consistent at $\approx 7.3\%$. The lesson: prefer cross-validation over a single split when sample size is limited.

This exercise is the foundation for understanding more sophisticated classification methods. The next step is the multi-class extension (one-versus-rest), the regularized form (ridge classifier, with $\lambda \|\beta\|^2$ added to the LS objective), and the nonlinear extension (logistic regression in [[Linear Algebra XII — Applied III — Nonlinear Least Squares]], support vector machines, neural networks).
