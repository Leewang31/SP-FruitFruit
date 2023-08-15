import tensorflowjs as tfjs
import tensorflow as tf

tfjs_target_dir = '../model/jsModel'

loadModel = tf.keras.models.load_model('../model/model1')
loadModel.summary()

tfjs.converters.save_keras_model(loadModel, tfjs_target_dir)