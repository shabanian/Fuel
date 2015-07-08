 
# -*- coding: utf-8 -*-
import os

from fuel import config
from fuel.datasets import H5PYDataset
Datasets = [ 'adult',
             'binarized_mnist',
             'connect4',
             'dna',
             'mushrooms',
             'nips',
             'ocr_letters',
             'rcv1',
             'web']
FILENAME = [ 'adult/a5a_{}.libsvm',
             'connect-4/connect-4_{}.libsvm',
             'dna/dna_scale_{}.libsvm',
             'mushrooms/mushrooms_{}.libsvm',
             'nips-0-12/nips-0-12_all_shuffled_bidon_target_{}.amat',
             'ocr_letters_{}.txt',
             'rcv1/rcv1_all_subset.binary_{}_voc_150.amat',
             'web/w6a_train.libsvm']
 
class uci(H5PYDataset):
    u"""CalTech 101 Silhouettes dataset.
    This dataset provides the `split1` train/validation/test split of the
    CalTech101 Silhouette dataset prepared by Benjamin M. Marlin [MARLIN].
    This class provides both the 16x16 and the 28x28 pixel sized version.
    The 16x16 version contains 4082 examples in the training set, 2257
    examples in the validation set and 2302 examples in the test set. The
    28x28 version contains 4100, 2264 and 2307 examples in the train, valid
    and test set.
    .. [MARLIN] https://people.cs.umass.edu/~marlin/data.shtml
    Parameters
    ----------
    which_set : {'train', 'valid', 'test'}
        Access the training, validation or test set.
    size : {16, 28}
        Either 16 or 28 to select the 16x16 or 28x28 pixels version
        of the dataset (default: 28).
    """
    def __init__(self,  dataset, **kwargs):
      
        kwargs.setdefault('load_in_memory', True)
        if dataset not in Datasets:
            raise ValueError('dataset  must be in ', Datasets)
	 
	self.filename = dataset +'.hdf5'
        super(uci, self).__init__(self.data_path, dataset, **kwargs)
        
        
  

    @property
    def data_path(self):
        return os.path.join(config.data_path, self.filename)