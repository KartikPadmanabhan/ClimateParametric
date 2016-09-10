class MethodOfMoments:

    def __init__(self, df, col, ax):
        self.df=df
        self.col=col
        self.ax=ax

# Define a function that plots distribution fitted to one month's of data
def plot_mom(self):
    data = self.df[self.col]

    sample_mean = data.mean()
    sample_var = np.sum(np.square(data - sample_mean)) /  (data.count() - 1)

    alpha = sample_mean**2 / sample_var
    beta = sample_mean / sample_var

    gamma_rv = scs.gamma(a=alpha, scale=1/beta)

    x_vals = np.linspace(data.min(), data.max())
    gamma_p = gamma_rv.pdf(x_vals)

    ax.plot(x_vals, gamma_p, color='r', alpha=0.4)

    ax.set_xlabel('Rainfall')
    ax.set_ylabel('Probability Density')
    ax.set_title(col)

    ax.set_xlim(0, 12)
    ax.set_ylim(0., .35)
    ax.legend()

    label = 'alpha = %.2f\nbeta = %.2f' % (alpha, beta)
    ax.annotate(label, xy=(8, 0.3))

months = df.columns - ['Year']
months_df = df[months]

# Use pandas to get the histogram, the axes as tuples are returned
axes = months_df.hist(bins=20, normed=1,
                    grid=0, edgecolor='none',
                    figsize=(15, 10)
                    layout=(3,4))

# Iterate through the axes and plot the line on each of the histogram
for month, ax in zip(months, axes.flatten()):
    plot_mom(months_df, month, ax)

plt.tight_layout()