# CLIMATE MODELLING USING PARAMETER APPROACHES 

## ORACLE BIG DATA APPLIANCE DEMO

### Introduction

A parameteric approach makes assumptions about the distribution of the underlying population and its parameters from which the sample was taken. A main drawback for this modelling approach is that if the data deviates strongly from the assumptions, using a parameteric approach using results in improper conclusions.

In order to avert this problem, techniques like kstest (Koglomorov-Smirnoff Goodness of fit test) is used to ensure that the sample under consideration comes from a population with a specific distribution.

The demo exploits two of the most popular parametric methods on top of Oracle Big Data Appliance to model historic Rainfall Data for Nashville, TN.

* Maximum Likelihood Estimation
* Method Of Moments

### Architecture

### Prerequisites

* Oracle Big Data Appliance
* Anaconda Parcels for Cloudera Manager Installed


### Interesting Results

a. The following is the histogram data plotted accross all months

```html
<div>
    <a href="https://plot.ly/~kpadmana/838/" target="_blank" title="Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec" style="display: block; text-align: center;"><img src="https://plot.ly/~kpadmana/838.png" alt="Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec" style="max-width: 100%;width: 1000px;"  width="1000" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="kpadmana:838"  src="https://plot.ly/embed.js" async></script>
</div>
```
