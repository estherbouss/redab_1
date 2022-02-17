from random import randint
#added
import matplotlib.pyplot as plt



def compute_histogram_bins(data=[], bins=[]):
    sticks=[]
    for i in range(len(bins)-1):
        sticks.append(str(bins[i]) +'-'+ str(bins[i+1]))
    return data, bins, sticks
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """


def plot_histogram(bins_count):
    plt.hist(bins_count[0], bins_count[1], align='left', rwidth=0.9, color='purple', edgecolor='black')
    plt.xlabel('Connection duration (s)')
    plt.ylabel('Connection count')
    plt.title('Histogram')
    bins_count[1].pop()
    plt.xticks(bins_count[1], labels= bins_count[2])
    plt.show()
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """

if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]
    
    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
