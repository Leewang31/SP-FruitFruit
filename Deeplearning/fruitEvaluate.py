import tensorflow as tf

test_dir = "../data/test"
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255
)
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical",
    shuffle=False
)

#모델 로드
loadModel = tf.keras.models.load_model('../model/model1')
loadModel.summary()
loadModel.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# score 확인
score = loadModel.evaluate(test_generator)
print("정확도 : ",round(score[1]*100,2))