# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The algorithm used for this model is the RandomForestClassifier. The model has been built to predict a salary threshold for each individual. This threshold is $50,000. The main libraries involved were pickle, sklearn, ml, and pandas.

## Intended Use
This model uses categories to determine which individuals are most likely to fall above or below the threshold of a $50,000 annual income. This data can be useful to groups such as policymakers and advocacy groups, as the data can help them determine if certain groups are being unfairly discriminated against regarding their pay. It can also be used by employers to help determine the type of salary certain individuals typically receive, but this is not recommended as historical bias can mislead employers.

## Training Data
The data used to build this pipeline came from the census.csv dataset, and the target feature was the salary. In order to predict the salary, we used several key categorical features, including: workclass, education, marital status, occupation, relationship, race, sex, and native country.

## Evaluation Data
To best evaluate the data, I split the data into training and testing data using the train_test_split function. The test data was kept separate from the training data so that we could evaluate performance on unseen data. For the split, I went with 80% of the data into training data and the remaining 20% as the testing data. I also included a random state of 42 to ensure that the results came back consistently.

## Metrics
The metrics used on this pipeline include precision, recall, and F1 score. The precision score determined how often predictions were correct, the recall score measured how many actual positive cases the model found, and the F1 score took these two scores and balanced them for one final determinative score. In my latest test, the numbers came back as follows: Precision: 0.7449, Recall: 0.6302, F1: 0.6828. This suggests that my model has moderate performance, with more weight placed on precision than recall.

## Ethical Considerations
Because this model uses features like sex, race, and native country in its analysis, we must be wary that there may be a built-in historical bias in the dataset that could transition into our model. With this in mind, caution should be applied when looking at the outright results, as the historical bias could potentially point people in the wrong direction.

## Caveats and Recommendations
We must keep in mind that this dataset may not have the most up-to-date information, and certainly will become more outdated as time goes on. Because our model was built from this dataset, we must stay aware of the timeframe of the data. Also, while the model performance is moderate, the recall score showed that our model has room for improvement and currently may miss some positive cases. Finally, as stated earlier, concerns with historical bias in this data must be accounted for. 