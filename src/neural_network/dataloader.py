import torch.utils.data



class MySampler(torch.utils.data.Sampler):
    def __init__(self, dataset, batch_size):
        """
        :param dataset: The dataset for which to create indices.
        :param batch_size: Number of indices in each batch.
        """
        super().__init__(dataset)
        self.dataset = dataset
        self.batch_size = batch_size

    def __iter__(self):
        # TODO:
        #  Return an iterator of indices, i.e. numbers in range(len(dataset)).
        #  dataset and represents  one  batch.
        #  The indices must be generated in a way that ensures
        #  that when a batch of indices is takes, samples in the same index of
        #  adjacent batches are also adjacent in the dataset.
        #  In the case when the last batch can't have batch_size samples,
        #  you can drop it.
        idx = None  # idx should be a 1-d list of indices.
        # ====== YOUR CODE: ======
        idx = []
        batches = int(len(self.dataset) / self.batch_size)
        for i in range(0, batches):
            for j in range(0, self.batch_size):
                index = i + j * batches
                idx.append(index)
        # ========================
        return iter(idx)

    def __len__(self):
        return len(self.dataset)



