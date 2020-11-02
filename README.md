# A statistic for the test (finally)

The previous exercise introduced the basic idea that we are going to use to test if the expectations of our distributions are all the same in qualitative terms.  Qualitatively, if our N samples are all from the same distribution the treatment and error sum of squares will both take similar values.  If, by contrast, the distributions have different expectations then the treatment sum of squares will be larger than the error sum of squares.  To make this idea more quantitative recall that we can estimate the common variance for the distributions from the error sum of squares as shown below:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{SS_E}{\sum_{j=1}^t(n_j-1)}=\frac{\sum_{j=1}^t(n_j-1)s_j^2}{\sum_{j=1}^t(n_j-1)})

with:

![](https://render.githubusercontent.com/render/math?math=S_j^2=\frac{n_j}{n_j-1}\left[\frac{1}{n_j}\sum_{i=1}^{n_j}X_i^2-\left(\frac{1}{n_j}\sum_{i=1}^{n_j}X_i\right)^2\right])

Furthermore, ![](https://render.githubusercontent.com/render/math?math=S^2) here is an estimate for the true variance of the distribution of the random variable, ![](https://render.githubusercontent.com/render/math?math=\textrm{var}(X_i)).  Now consider the treatment sum of squares:

![](https://render.githubusercontent.com/render/math?math=SS_T=\sum_{j=1}^t\sum_{i=1}^{n_j}(\overline{X_j}-\overline{X})^2=\sum_{j=1}^tn_j(\overline{X_j)-\overline{X})^2

If we assume that all the ![](https://render.githubusercontent.com/render/math?math=\overline{X_j}) are identical random variables and if we ignore the ![](https://render.githubusercontent.com/render/math?math=n_j) in this expression above for a moment this looks like the numerator in the following expression for estimating the sample variance of ![](https://render.githubusercontent.com/render/math?math=\overline{X}_j):

![](https://render.githubusercontent.com/render/math?math=S_{\overline{X_j}}=\frac{1}{t-1}\sum_{j=1}^t(\overline{X_j}-\overline{X})^2)^2)

Now recall that ![](https://render.githubusercontent.com/render/math?math=\overline{X}_j) is simply a sample mean computed from ![](https://render.githubusercontent.com/render/math?math=n_j) identically distributed random variables ![](https://render.githubusercontent.com/render/math?math=X_i) as we can then write the following statement about the exact variance that we are estimating above:

![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(\overline{X_j})=\mathbb{E}(X_i)\qquad\textrm{and}\qquad\textrm{var}(\overline{X_j})=\frac{\textrm{var}(X_i)}{n_j})

If all the distributions have the same expectation the treatment sum of squares is thus related to an estimator for the common variance by the following relation:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{SS_T}{T-1})

We will thus define the following statistic, F, for these hypothesis tests:

![](https://render.githubusercontent.com/render/math?math=F=\frac{SS_T/(T-1)}{SS_E/\left[\sum_{j=1}^t(N_j-1)\right]})

The arguments above illustrate that if the sampled distributions are all the same and if the estimates for the variance in the numerator and the denominator in this expression are replaced by their exact values F will be equal to one.  The test we are doing when we sample F is thus the comparison of variances that we have learned above in the earlier tasks of this exercise.

__To complete this exercise I thus want you to complete the function called  `gen_f_estimate`.   This function should generate random variables from the distribution that is sampled by the test statistic, F__.  You will need to use everything that you have learned in the previous tasks in order to complete this exercise.  Two integers called `T` and `N` are input into the function.  Within the function, you should generate `T` samples of `N` standard normal random variables.   You will then use what you learned in the previous exercises to calculate ![](https://render.githubusercontent.com/render/math?math=SS_T), ![](https://render.githubusercontent.com/render/math?math=SS_E) and ultimately F from these samples.  The value of F should then be returned.

When the function is complete a graph showing 100 values from the distribution generated from the distribution sampled by F is produced. 
 


 
