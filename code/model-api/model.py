import numpy as np
import tensorflow as tf

from official.nlp.data import classifier_data_lib as lib 
from tflite_model_maker import model_spec

def predict(text):
  run_id = './model/bert_classifier_on_VTPAN_with_seq-len-512'
  # run_id = './model/bert_classifier_on_PANC_with_seq-len-512'
  run_path = run_id + '/quantized/model.tflite'

  # Load the model
  mb_spec = model_spec.get("bert_classifier")
  mb_spec.seq_len = 512
  example = lib.InputExample(guid='0', text_a=text, label=None) 
  mb_spec.build()
  feature = lib.convert_single_example(
    ex_index=0, example=example, label_list=None,max_seq_length=mb_spec.seq_len, tokenizer=mb_spec.tokenizer)


  # Load the TFLite model and allocate tensors.
  interpreter = tf.lite.Interpreter(model_path=run_path)
  interpreter.allocate_tensors()

  # Get input and output tensors.
  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  # Test the model on random input data.
  input_shape = input_details[0]['shape']
  interpreter.set_tensor(input_details[0]["index"], [np.array(feature.input_ids, dtype=np.int32)])
  interpreter.set_tensor(input_details[1]["index"], [np.array(feature.input_mask, dtype=np.int32)])
  interpreter.set_tensor(input_details[2]["index"], [np.array(feature.segment_ids, dtype=np.int32)])

  interpreter.invoke()

  # The function `get_tensor()` returns a copy of the tensor data.
  # Use `tensor()` in order to get a pointer to the tensor.
  output_data = interpreter.get_tensor(output_details[0]['index'])
  return (output_data[0][1])

