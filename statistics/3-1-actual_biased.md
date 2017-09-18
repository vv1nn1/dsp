[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
#read data
resp = nsfg.ReadFemResp()
#create pmf
pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')
#create biased pmf
biased = BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

pmf.Mean()
#1.0242051550438309
biased.Mean()
#2.4036791006642821
```
