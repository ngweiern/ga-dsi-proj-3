# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & Classification

## Table of Contents
- [Executive Summary](#Executive-Summary)
- [Introduction](#Introduction)
- [Problem Statement](#Problem-Statement)
- [Overview](#Overview)
- [Datasets](#Datasets)
- [Conclusion and Recommendations](#Conclusion-and-Recommendations)

--- 

### Executive Summary

This project involves the use of Reddit's web API for the purpose of collecting data of posts belonging to two separate subreddit threads, "Developing Android Apps" and "iOS Programming". 

These posts are then pre-processed, vectorized, and then transformed into tf-idf scores before being used to train two machine learning models, Logistic Regression and Naive Bayes classifier. 

The accuracy of these two models are then compared against each other to identify the better model of the two. 

In the first instance where the subtext of the posts are used, the Logistic Regression outperformed the Naive Bayes classifier in terms of accuracy.

In the second instance where both the subtext and the title of the posts were factored into each model, the Naive Bayes classifier outperformed the Logistic Regression in terms of accuracy and each of them individually had a better classification accuracy than in the first instance.

The results of this project showed that the features, subtext and title, ought to be considered when training the Logistic Regression and Naive Bayes classifier, and that the Naive Bayes would be a better model for classifying the posts accurately after these features were used to train the model.

---

### Introduction

Reddit posts were fetched from the endpoints of two subreddit threads, "iOS Programming" and "Developing Android Apps". These reddit posts were then pre-processed before being separately trained on the Logistic Regression and the Multinomial Naive Bayes classifier to identify the model with the better classification accuracy. Thereafter, feature engineering was performed before both models were compared against one another to once again identify the model with the better classification accuracy.

---

### Problem Statement

To identify the better model between Logistic Regression and Naive Bayes, based on their accuracies in classifying reddit posts into two categories, namely "iOS Programming" subreddit and "Developing Android Apps" subreddit.

---

### Overview

The pipeline:
- Import libraries
- Import data
- Exploratory Data Analysis
- Modeling
- Further Modeling
- Conclusions and Recommendations

---

### Datasets

#### Provided Data

For this project, there are two datasets provided:

- ["Developing Android App" Subreddit Posts](./data/android_dev.csv)
- ["iOS Programming" Subreddit Posts](./data/ios_programming.csv)

These subreddit posts were fetched from the web APIs of reddit, ["Developing Android App" subreddit](https://www.reddit.com/r/androiddev.json) and ["iOS Programming" subreddit](https://www.reddit.com/r/iOSProgramming.json).

---

### Conclusion and Recommendations

The classification metrics of the models used are as follows:

<table>
    <thead>
        <tr>
            <th></th>
            <th colspan=2>Before Feature Engineering</th>
            <th colspan=2>After Feature Engineering</th>
        </tr>
        <tr>
            <th>Metrics</th>
            <th>Naive Bayes</th>
            <th>Logistic Regression</th>
            <th>Naive Bayes</th>
            <th>Logistic Regression</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Accuracy</td>
            <td>0.837</td>
            <td>0.848</td>
            <td>0.885</td>
            <td>0.877</td>
        </tr>
        <tr>
            <td>Misclassification</td>
            <td>0.163</td>
            <td>0.152</td>
            <td>0.115</td>
            <td>0.123</td>
        </tr>
        <tr>
            <td>Sensitivity</td>
            <td>0.856</td>
            <td>0.829</td>
            <td>0.845</td>
            <td>0.841</td>
        </tr>
        <tr>
            <td>Specificity</td>
            <td>0.818</td>
            <td>0.867</td>
            <td>0.924</td>
            <td>0.912</td>
        </tr>
        <tr>
            <td>Precision</td>
            <td>0.824</td>
            <td>0.862</td>
            <td>0.916</td>
            <td>0.904</td>
        </tr>
    </tbody>
</table>

It can be observed that the accuracy of the Logistic Regression classifier was higher than the accuracy of the Naive Bayes classifier before feature engineering was performed.

After feature engineering was performed, where the title and selftext was added together, the Naive Bayes classifier outperformed the Logistic Regression classifier in terms of accuracy.

Based on these findings, it is recommended that the title and selftext are both factored into the Naive Bayes classifier for the highest classification accuracy when classifying reddit posts as either of the two subreddit threads, "Developing Android Apps" and "iOS Programming".