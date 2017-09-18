[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's ds

```python

def CohenEffectSize(group1, group2):
   
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()
#(7.201094430437772, 7.325855614973262)
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
#-0.088672927072602006

```
If mean1 is bigger than mean2, the effect size will be positive. If mean2 is larger than mean1, the effect size will be negative
The sign of your Cohen’s d effect tells you the direction of the effect.
