def make_one_versus_all_labels(self, y, m):
    """
    y : numpy array of shape (n,)
    m : int (num_classes)
    returns : numpy array of shape (n, m)
    """
    numpy_array = np.full(len(y),len(m),-1)
    for i in range(len(y)):
        numpy_array[i][y[i]] = 1
    return numpy_array