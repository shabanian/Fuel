 
import numpy
from numpy.testing import assert_raises
import os
from fuel.datasets import uci
from fuel.datasets.hdf5 import H5PYDataset 
Datasets = [ 'adult',
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
FILESIZE = [(5000, 1414 ,26147,123), #train, valid,test, dim
	    (16000, 4000, 47557, 126), 
	    (1400, 600 ,1186,180),
	    (2000, 500, 5624, 112), 
	    (400,  100, 1240,500), 
	    (32152,10000, 10000,128), 
	    (40000, 10000, 150000, 150), 
	    (14000, 3188 ,32561, 300)]

def test_uci():
    for i, data_name in enumerate(Datasets):
	
	File_Name =   data_name + '.hdf5'
	directory  =os.path.split(os.getcwd())[0]
	print directory, '-----------------------------'
	File_Dir = os.path.join(directory,  File_Name )
	#dataset = uci(File_Dir, load_in_memory=False)
	Data_train =  H5PYDataset(File_Dir, which_set='train')#dataset.open()dataset = uci(data_name, load_in_memory=False)
	Data_valid =  H5PYDataset(File_Dir, which_set='valid')
	Data_test =  H5PYDataset(File_Dir, which_set='test')
	handle = Data_train.open()
	D_train = Data_train.get_data(handle)
	print D_train .shape
	for j, D in enumerate([Data_train,Data_valid, Data_test ]):
	      assert D.dtype == 'uint8'
	      assert D.num_examples==   FILESIZE[i][j] 
      
	 
    assert_allclose(data[0][0][6], known)
    assert labels[0][0] == 5
    assert dataset.num_examples == 60000
    dataset.close(handle)

    stream = DataStream.default_stream(
        dataset, iteration_scheme=SequentialScheme(10, 10))
    data = next(stream.get_epoch_iterator())[0]
    assert data.min() >= 0.0 and data.max() <= 1.0
    assert data.dtype == config.floatX
test_uci()

"""def test_caltech101_silhouettes28():
    skip_if_not_available(datasets=['caltech101_silhouettes28.hdf5'])
    for which_set, size, num_examples in (
            ('train', 28, 4100), ('valid', 28, 2264), ('test', 28, 2307)):
        ds = CalTech101Silhouettes(which_set=which_set, size=size,
                                   load_in_memory=False)

        assert ds.num_examples == num_examples

        handle = ds.open()
        features, targets = ds.get_data(handle, slice(0, 10))

        assert features.shape == (10, 1, size, size)
        assert targets.shape == (10, 1)

        assert features.dtype == numpy.uint8
        assert targets.dtype == numpy.uint8

    assert_raises(ValueError, CalTech101Silhouettes,
                  which_set='test', size=10)"""