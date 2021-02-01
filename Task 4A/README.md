## Popularity Modeling

Popularity modeling can be done based on the metrices - 
  * requests per unit area
  * requests per unit time
  * number of users (with a logarithm factor)
  * area covered by the POI (with a logarithm factor)
  * proximity from US based POIs (if available)
  * gemographic information of the users like (age, first language etc) making the requests
  * population density in that area
  
We can perform [Principal Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) from the batch of features to generate custom meaningful features.

All the features should be **scaled** in the range `[-1, +1` with their corresponding means and they should be normalized. Using the features on some linear function we can easily determine the popularity score. 

Also, we can come up with an arbitrary linear function and set arbitrary weights on the features. Then we can use ML based optimizing algorithms like `Gradient Descent`, [`Stochastic Gradient Descent`](https://en.wikipedia.org/wiki/Stochastic_gradient_descent), [`Nonlinear conjugate gradient method`](https://en.wikipedia.org/wiki/Nonlinear_conjugate_gradient_method), [`Limited-memory BFGS`](https://en.wikipedia.org/wiki/Limited-memory_BFGS) to come to the converging point and determine the necessary weights and biases.


## Bonus Task

If we visualize the given dataset:

![alt text](https://github.com/safayet08/eqWorks-internship-assignment/blob/main/Results/Analysis/POIDistribution.png)

It is clear to notice that **POIs are based on large cities where population density is high**. They are situated in capitals like: `Edmonton`, `Montreal` & `Halifax`.We can end up with hypotheses as-
  * It's clearly visible that POIs aren't located efficiently(Efficiency metric used here is - Average distance from POI to requestOrigin). We can use unsupervised  [K-Means-Clustering](https://en.wikipedia.org/wiki/K-means_clustering) algorithm with `clusterNumber = numberOfPOIs` to locate the clusters efficienty as this algorithm converges the clusters towards the centroids where the `eucleadean distance` from each point to cluster is minimum.
  * We can compare `K-Means-Clustering` and `Random-Forrest` unsupervised ML algorithms and see which one performs better
  * The POIs are covering most of the densely populated areas of Canada.
  * The POI in Edmonton covers a huge area. We can divide this load into two POIs.
  * If it's the dataset of a marketing campeign, the company should invest more into marketing whre `requests per unit area` is larger.
  * **The west-cost of Canada** doesn't generate as much requests (Assuming this is the dataset of the entire country
  
