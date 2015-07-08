 
import argparse 
from fuel.downloaders.base import default_downloader

 
Datasets = [ 'adult',
             'connect4',
             'dna',
             'mushrooms',
             'nips',
             'ocr_letters',
             'rcv1',
             'web']
             
FILENAME = [ 'a5a_{}.libsvm',
             'connect-4_{}.libsvm',
             'dna_scale_{}.libsvm',
             'mushrooms_{}.libsvm',
             'nips-0-12_all_shuffled_bidon_target_{}.amat',
             'ocr_letters_{}.txt',
             'rcv1_all_subset.binary_{}_voc_150.amat',
             'w6a_{}.libsvm']
             
FILEDirect = [ 'adult/',
             'connect-4/',
             'dna/',
             'mushrooms/',
             'nips-0-12/',
             '',
             'rcv1/',
             'web/']
             
             
def uci_downloader(  dataset,   **kwargs):
    print 'in uci_downloader'


    if dataset not in Datasets :
        raise ValueError("data_name must be one of " + Datasets )
    for i, data_name in enumerate(Datasets ):
	if  dataset == Datasets [i]:
	    File_Name = FILENAME[i]
	    File_Directory = FILEDirect[i] + File_Name
	if  dataset == 'ocr_letters':
	        BASE_URL = 'http://ai.stanford.edu/~btaskar/ocr/letter.data.gz/'
	     
	else:
		BASE_URL = 'http://www.cs.toronto.edu/~larocheh/public/datasets/'
		 
  
    sets = ['train', 'valid', 'test']
    urls = [ BASE_URL + File_Directory.format(s)  for s in sets]
    filenames = [ File_Name.format(s) for s in sets] 
    #actual_filename = FILENAME.format(size)
    #actual_url = BASE_URL + dataset + '/' #    + 'a5a_train.libsvm'
    #filenames=['a5a_train.libsvm'.format(size), 'a5a_test.libsvm'.format(size) ,'a5a_valid.libsvm'.format(size)]
    for i, url in enumerate(urls):
      #print actual_url
      print url
      #print i
      filename = filenames[i]
      if not filename:
	  filename = filename_from_url(url) 

      default_downloader(urls = urls, filenames = filenames , **kwargs) 


def fill_subparser(subparser):
    """Sets up a subparser to download the UCI dataset files.
    The following UCI dataset files can be downloaded
    from http://www.cs.toronto.edu/~larocheh/public/datasets/
 
    Parameters
    ----------
    subparser : :class:`argparse.ArgumentParser`
        Subparser handling the `uci` command.
    """
    subparser.add_argument(
        "dataset", type = str, choices = Datasets,
        help="Name of dataset")
  
    subparser.set_defaults( func=uci_downloader  )

 
 