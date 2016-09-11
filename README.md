# CLIMATE MODELLING USING ORACLE BIG DATA APPLIANCE

### Introduction

A parameteric approach makes assumptions about the distribution of the underlying population and its parameters from which the sample was taken. A main drawback for this modelling approach is that if the data deviates strongly from the assumptions, using a parameteric approach using results in improper conclusions.

In order to avert this problem, techniques like kstest (Koglomorov-Smirnoff Goodness of fit test) is used to ensure that the sample under consideration comes from a population with a specific distribution.

The demo exploits two of the most popular parametric methods on top of Oracle Big Data Appliance to model historic Rainfall Data for Nashville, TN.

* Maximum Likelihood Estimation
* Method Of Moments

### Architecture

### Prerequisites

* Oracle Big Data Appliance
* Anaconda Parcels for Cloudera Manager installed
* Plotly needs to be installed accross all cell nodes
* Cufflinks to work with Plotly and Pandas

### Interesting Results

[plotly link](https://plot.ly/~kpadmana/838/jan-feb-mar-apr-may-jun-jul-aug-sep-oct-nov-dec)
[![ScreenShot](https://rawgit.com/KartikPadmanabhan/Parametric-Estimation/master/html/climate-histogram.png)](https://rawgit.com/KartikPadmanabhan/Parametric-Estimation/master/html/climate-histogram.htm)

[plotly link](https://plot.ly/~kpadmana/856/-line0-line1-line0-line1-line0-line1-line0-line1-line0-line1-line0-line1-line0-l)
[![ScreenShot](https://rawgit.com/KartikPadmanabhan/Parametric-Estimation/master/html/climate-mom.png)](https://rawgit.com/KartikPadmanabhan/Parametric-Estimation/master/html/climate-mom.htm)

[plotly link](https://plot.ly/~kpadmana/858/-line0-line0-line0-line0-line0-line0-line0-line0-line0-line0-line0-line0)
[![ScreenShot](https://rawgit.com/KartikPadmanabhan/Parametric-Estimation/master/html/climate-mle.png)](https://rawgit.com/KartikPadmanabhan/Parametric-Estimation/master/html/climate-mle.htm)

