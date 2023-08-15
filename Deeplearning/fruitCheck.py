import tensorflow as tf

pred_classes = {
    0: "apple",
    1: "banana",
    2: "beetroot",
    3: "bell pepper",
    4: "cabbage",
    5: "capsicum",
    6: "carrot",
    7: "cauliflower",
    8: "chilli pepper",
    9: "corn",
    10: "cucumber",
    11: "eggplant",
    12: "garlic",
    13: "ginger",
    14: "grapes",
    15: "jalepeno",
    16: "kiwi",
    17: "lemon",
    18: "lettuce",
    19: "mango",
    20: "onion",
    21: "orange",
    22: "paprika",
    23: "pear",
    24: "peas",
    25: "pineapple",
    26: "pomegranate",
    27: "potato",
    28: "raddish",
    29: "soy beans",
    30: "spinach",
    31: "sweetcorn",
    32: "sweetpotato",
    33: "tomato",
    34: "turnip",
    35: "watermelon"
}

# 이미지 전처리 함수
def preprocess_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array /= 255.0
    img_array = tf.expand_dims(img_array, 0)
    return img_array

# 모델 로드
loadModel = tf.keras.models.load_model('../model/model1')
loadModel.summary()
loadModel.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# 이미지 경로
image_path = "../data/test/myTest/test1.jpg"

# 이미지 전처리
img_array = preprocess_image(image_path)

# 예측
predictions = loadModel.predict(img_array)

print(predictions)

# 예측된 클래스의 인덱스
predicted_class = tf.argmax(predictions[0])
predictNum = predicted_class.numpy()

# 예측된 클래스의 인덱스를 과일 이름으로 변환
predicted_fruit = pred_classes[predictNum]

print("Predicted class:", predicted_fruit)
