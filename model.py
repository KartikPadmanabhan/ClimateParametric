import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import scipy.stats as scs
import plotly.plotly as py
import numpy as np
from scipy.stats import kstest
import cufflinks as cf
import matplotlib.pyplot as plt
import plotly.tools as tls

class MethodOfMoments(object):

    def __init__(self, df):
        self.df=df

    def plot_moments(self):
        fig = plt.figure()
        months=[col for col in df.columns if col != 'Year']
        nplot=1
        for month in months:
            '''For month of January find sample mean, variance and use Gamma distribution'''
            data = df[month]
            sample_mean = data.mean()
            '''Numpy has no built-in function for sample variance, only population var'''
            sample_var = np.sum(np.square(data - sample_mean)) /  (data.count() - 1)
            alpha = sample_mean**2 / sample_var
            beta = sample_mean / sample_var
            norm_mean = sample_mean
            norm_var = sample_var
            gamma_rv = scs.gamma(a=alpha, scale=1/beta)
            norm_rv = scs.norm(norm_mean, norm_var)
            x_vals = np.linspace(data.min(), data.max())
            gamma_p = gamma_rv.pdf(x_vals)
            norm_p = norm_rv.pdf(x_vals)
            x=x_vals
            y1=gamma_p
            y2=norm_p 
            ax = fig.add_subplot(6,2,nplot)
            ax.hist(data,bins=30, normed=1, edgecolor='none')
            ax.plot(x, y1, '.-')
            ax.plot(x, y2, 'r.-')
            ax.set_xlabel('Rainfall')
            ax.set_ylabel('Probability Density')
            s=month + " RainFall"
            ax.set_title(s)
            nplot+=1
        plotly_fig = tls.mpl_to_plotly( fig )
        '''py.iplot_mpl(fig, filename='rainfall')'''
        plotly_url = py.plot(plotly_fig, filename='moments',sharing='public')

class MaximumLikelihood(object):

    def __init__(self, df):
        self.df=df

    def plot_likelihood(self):
        fig = plt.figure()
        months=[col for col in df.columns if col != 'Year']
        nplot=1
        for month in months:
        # For month of January find sample mean, variance and use Gamma distribution
            data = df[month]
            sample_mean = data.mean()
            # Numpy has no built-in function for sample variance, only population var
            sample_var = np.sum(np.square(data - sample_mean)) /  (data.count() - 1)
            alpha = sample_mean**2 / sample_var
            beta = sample_mean / sample_var
            # Use MLE to fit a gamma distribution
            '''If we do not use np.float64 we get AttributEerror'''
            ahat, loc, bhat = scs.gamma.fit(np.float64(df[month]), floc=0)
            alpha_mle, beta_mle = ahat, 1./bhat
            
            gamma_rv = scs.gamma(a=alpha_mle, scale=1/beta_mle)
            x_vals = np.linspace(data.min(), data.max())
            gamma_p = gamma_rv.pdf(x_vals)
            x=x_vals
            y1=gamma_p
            ax = fig.add_subplot(6,2,nplot)
            ax.hist(data,bins=30, normed=1, edgecolor='none')
            ax.plot(x, y1, '.-')
            ax.set_xlabel('Rainfall')
            ax.set_ylabel('Probability Density')
            s=month + " RainFall"
            ax.set_title(s)
            nplot+=1
        plotly_fig = tls.mpl_to_plotly( fig )
        '''py.iplot_mpl(fig, filename='mle_gamma')'''
        plotly_url = py.plot(plotly_fig, filename='likelihood',sharing='public')


def main():

    '''We assume the dataset is in this below location, please change it as per application'''
    rainrdd = sc.textFile('hdfs:///user/root/spark/parametric_estimation/rainfall.csv')

    '''Preprocessing to convert RDD into spark dataframe'''
    sparkDF=rainrdd.map(lambda x: str(x)).map(lambda w: w.split(',')).toDF()

    '''Convert Spark DFF into Pandas DataFrame'''
    df = sparkDF.toPandas()

    '''Converting first row as column name'''
    df.columns = df.iloc[0]
    df=df.reindex(df.index.drop(0))

    '''Changing all the rainfall numbers to floating point values'''
    df.iloc[:,1:]=df.iloc[:,1:].applymap(lambda x: float(x))

    data = [go.Histogram(y=df['Jan'])]

    '''Histograms'''
    df.iloc[:,1:].iplot(kind='histogram', subplots=True, shape=(3, 4), filename='histogram-subplots')

    '''Koglomorov Smirnoff Tests'''
    print kstest(df.Jan.astype(float),'gamma',args=(1,))
    print kstest(df.Jan.astype(float),'uniform',args=(1,))
    print kstest(df.Jan.astype(float),'norm',args=(1,))
    print kstest(df.Jan.astype(float),'poisson',args=(1,))

    '''Plot Method Of Moments Based Estimation Graph'''
    m=MethodOfMoments(df)
    m.plot_moments()



if __name__ == "__main__":
    main()

