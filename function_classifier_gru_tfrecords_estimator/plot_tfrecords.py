import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import config

tfrecords_filename = config.data_tmp_folder + config.test_tfrecord_filename
record_iterator = tf.python_io.tf_record_iterator(path=tfrecords_filename)

for string_record in record_iterator:
    # Parse the next example
    example = tf.train.Example()
    example.ParseFromString(string_record)

    # Get the features you stored (change to match your tfrecord writing code)
    sequence_length = int(example.features.feature['seqlen']
                                 .int64_list
                                 .value[0])

    input_dimension = int(example.features.feature['dim']
                                .int64_list
                                .value[0])

    sequence_string = (example.features.feature['seq_raw']
                                  .bytes_list
                                  .value[0])

    label_string = (example.features.feature['label_raw']
                                  .bytes_list
                                  .value[0])

    # Convert to a numpy array (change dtype to the datatype you stored)
    sequence = np.fromstring(sequence_string, dtype=np.float32)
    label = np.fromstring(label_string, dtype=np.uint8)
    # Print the shape; does it match your expectations?
    print('Sequence: ')
    print(sequence_length)
    print(input_dimension)
    print(sequence.shape)
    print(label)
    plt.plot(sequence.tolist())
    plt.show(block=True)
