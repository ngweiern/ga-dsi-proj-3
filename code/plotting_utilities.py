import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_auc_score

class Plotter(object):
    def __init__(self):
        pass

    def plot_probability_distribution(self, pred_df):
        # Create figure.
        plt.figure(figsize = (10,7))

        # Create two histograms of observations.
        plt.hist(pred_df[pred_df['true_values'] == 0]['pred_probs'],
                 bins=25,
                 color='b',
                 alpha = 0.6,
                 label='Outcome = 0')
        plt.hist(pred_df[pred_df['true_values'] == 1]['pred_probs'],
                 bins=25,
                 color='orange',
                 alpha = 0.6,
                 label='Outcome = 1')

        # Label axes.
        plt.title('Distribution of P(Outcome = 1)', fontsize=22)
        plt.ylabel('Frequency', fontsize=18)
        plt.xlabel('Predicted Probability that Outcome = 1', fontsize=18)

        # Create legend.
        plt.legend(fontsize=20);

    # Define function to calculate sensitivity. (True positive rate.)
    def TPR(self, df, true_col, pred_prob_col, threshold):
        true_positive = df[(df[true_col] == 1) & (df[pred_prob_col] >= threshold)].shape[0]
        false_negative = df[(df[true_col] == 1) & (df[pred_prob_col] < threshold)].shape[0]
        return true_positive / (true_positive + false_negative)

    # Define function to calculate 1 - specificity. (False positive rate.)
    def FPR(self, df, true_col, pred_prob_col, threshold):
        true_negative = df[(df[true_col] == 0) & (df[pred_prob_col] <= threshold)].shape[0]
        false_positive = df[(df[true_col] == 0) & (df[pred_prob_col] > threshold)].shape[0]
        return 1 - (true_negative / (true_negative + false_positive))

    def plot_roc_curve(self, pred_df):
        # Create figure.
        plt.figure(figsize=(10, 7))

        # Create threshold values. (Dashed red line in image.)
        thresholds = np.linspace(0, 1, 200)

        # Calculate sensitivity & 1-specificity for each threshold between 0 and 1.
        tpr_values = [self.TPR(pred_df, 'true_values', 'pred_probs', prob) for prob in thresholds]
        fpr_values = [self.FPR(pred_df, 'true_values', 'pred_probs', prob) for prob in thresholds]

        # Plot ROC curve.
        plt.plot(fpr_values,  # False Positive Rate on X-axis
                 tpr_values,  # True Positive Rate on Y-axis
                 label='ROC Curve')

        # Plot baseline. (Perfect overlap between the two populations.)
        plt.plot(np.linspace(0, 1, 200),
                 np.linspace(0, 1, 200),
                 label='baseline',
                 linestyle='--')

        # Label axes.
        plt.title(f'ROC Curve with AUC = {round(roc_auc_score(pred_df["true_values"], pred_df["pred_probs"]), 3)}',
                  fontsize=22)
        plt.ylabel('Sensitivity', fontsize=18)
        plt.xlabel('1 - Specificity', fontsize=18)

        # Create legend.
        plt.legend(fontsize=16);
