from sklearn.cluster import KMeans

def run_KMeans(max_k, data, param_dict = 'default'):
    """ It will run the K-Means algo max_k times,
    with the same data and the param_dict hyperparameters.
    Args:
        max_k (int)
        data (pandas.DataFrame)
        param_dict (dict) : contains the following params from the sklearn KMeans ['init', 'n_init', 'tol', \
            'algorithm'].
    Returns:
        dict: Contains each KMeans fit with k \in [2, max_k].
    """
    
    if param_dict == 'default':
        param_dict = {
            'n_init': 10,
            'tol': 1e-4,
            'algorithm': 'full'
        }
    
    kmeans_results = dict()
    for k in range(2 , max_k + 1):
        kmeans = KMeans(n_clusters = k
                        , init = 'k-means++'
                        , n_init = param_dict['n_init']
                        , tol = param_dict['tol']
                        , n_jobs = -1 # use all processors
                        , random_state = 1
                        , algorithm = param_dict['algorithm'])

        kmeans_results.update( {k : kmeans.fit(data)} )