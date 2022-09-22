Recipe Recommender created via recipe review data from Food.com using the Sci-Kit Surprise package

Dataset: https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions 
Background: https://aclanthology.org/D19-1613/

Project summary: https://www.youtube.com/watch?v=gAa4Jx_Zu7I

## I. Project Goals and Tasks

In the space of online food recipes, there are seemingly endless possibilities of new recipes to try. This project seeks to provide accurate recipe rating predictions and recipe recommendations using various methods.

I was responsible for trying collaborative filtering using item- and user-based neighborhood models and matrix factorization models such as KNN, NMF, SVD, and SVDpp algorithms, and evaluated accuracy by using the target variable of recipe rating. 

## II. EDA Summary

The median number of ratings per user is 6, and 73% of users only rated one recipe. 2.3% of users rated more than 25 recipes.

- Most recipes took 20-65 minutes to prepare, had 6-12 ingredients, and 6-11 steps.
- The rating data is a bit skewed towards positive ratings - 72% of ratings were 5 and 17% of ratings were 4. Only 8% of the ratings were low (0-2).
- There were 11,659 ingredients simplified to 8,023 generalized ingredients. For example “romaine lettuce leaf” and “mixed baby lettuces and spring greens” both became “lettuce”. 75% of ingredients were used in 50 or fewer recipes (0.03% of recipes).
- A “meal types” category was created using the “tags” column from the raw recipe data. The most common meal types were Main Dish, Desserts, Side Dish, Lunch, Appetizer.

## III. Description of Approach

### Data Cleaning: 

Reviews with a rating of “0” were found to be inconsistent compared to the actual written reviews - it wasn’t clear if these were very low ratings or the absence of a rating value, so these ratings were removed.

Additionally, the ratings dataset (Interactions) was reduced to avoid memory issues, by filtering to users and recipes with at least 25 ratings each. This brought the dataset down from 1,132,367 ratings to 141,512.

### Collaborative Filtering: 

Neighborhood-based and matrix factorization models were compared, specifically: KNNWithMeans, KNNBasic, KNNWithZScore, KNNBaseline, SVD, SVDpp, NMF from the Surprise package, which were compared with default settings. KNN models were all evaluated for both user-based and item-based similarities, and SVD and NMF models were evaluated with biased of True and False. All models were compared across RMSE, MSE, and MAE values using 5-fold cross-validation. The best performing model was optimized to find the best combination of parameters, and that tuned model was used to generate recommendations using the Surprise package.

## IV. Results - Collaborative Filtering

Because the ratings data did not have outliers, MAE was used to evaluated the collaborative filtering models. Using default settings, the best performing neighborhood model was KNN Basic, item-based. The best performing matrix factorization model was SVDpp, however that model had a significantly longer runtime.

The KNN Basic item-based model was tuned using Grid Search to determine the best combination of similarity measures - Pearson, Cosine, or MSD (Mean Squared Difference) - with the number of neighbors ranging from 5-30. The best performing KNN Basic item-based model used MSD similarity measure and 13 neighbors and had an MAE of 0.3548.

Because the SVD model had a very similar MAE to the SVDpp model but a significantly quicker runtime, it was also tuned using Grid Search to check the following combinations of parameters: number of factors: 50 and 100, number of epochs: 10 and 20, biased: True and False, learning rate - all: 0.0005, 0.005, and 0.05, and regularization rate - all 0.002, 0.02, and 0.2. The best performing SVD model used n_factors=50, n_epochs=20, biased=True, lr_all=0.005, reg_all=0.02 and had a MAE of 0.3491.

The tuned SVD model was used to generate recommendations for a given user. The “Top recipes rated by user” represent the recipes that had a rating above the mean rating for that user.

## V. Conclusion

For basic collaborative filtering, the preliminary results were good - given that the MAE is around 0.35, and the ratings are integers, rounding the predicted ratings to whole numbers should result in relatively accurate ratings. The combination of similar accuracy and runtimes at only a fraction of a second, cluster-based recommenders would be scalable for Food.com’s large user base.

However, when generating actual recipe recommendations using the tuned SVD model from the Surprise package, the recommender seems to generate very similar predicted recipes and ratings for every user. Additionally, when comparing meal types for top rated recipes and the top predicted recipes, there were some instances of recommending types of meals the user never rated above average. So relying on the Surprise package alone is not enough, a more useful recommender might also take meal types into account when recommending recipes or include other methods to make more personalized recommendations. Additionally, a dataset with a more balanced distribution of ratings might generate more accurate predictions
