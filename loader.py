"""
    Load / normalize / shortens model data (google's model requires gensim)
    Does NOT load the model into memory, just pre-processes the data, line by line
    Author: Wolf Paulus, https://wolfpaulus.com
    Forked by Wonjoon Jun
"""
from wv import Model, Word

def pre_process_data(in_file: str, out_file: str,
                     features: int = 300,
                     normalize: bool = True,
                     skip_1st: bool = False,
                     lines: int = 0) -> None:
    """
    Pre-process word vectors
    :param in_file: input file
    :param out_file: output file
    :param features: number of features defaults to 300
    :param normalize: normalize vectors defaults to True
    :param skip_1st: skip first line defaults to False
    :param lines: number of lines to process 0 for all
    :return: None
    """
    with open(out_file, 'w') as f:
        f.write("") #clear out the data within the outfile
    with open(in_file, 'r') as in_file:
        for _ in range(lines):
            line = in_file.readline() 
            if not line:  
                break 
            listFromLine = line.split(" ")
            word = Word(listFromLine[0], [float(x) for x in listFromLine[1:]])
            word.normalize()
            word.writeToFile(out_file)

    





pre_process_data("short_glove.txt", "short_glove_normalized.txt", lines=100000)
    
