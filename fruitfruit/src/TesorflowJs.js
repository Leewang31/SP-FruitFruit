import * as tf from '@tensorflow/tfjs';

const loadModel = async () => {
    const tf_dir = '/jsModel/model.json'; // 웹 서버에서 제공하는 경로로 변경

    const model = await tf.loadLayersModel(tf_dir);

    return model
};

export default loadModel;