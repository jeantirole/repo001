
library(keras)

train_datagen <- image_data_generator(rescale = 1./255)
train_generator <- flow_images_from_directory(
  'handwriting_shape/train', generator = train_datagen,
   target_size = c(24,24),
   batch_size =3,
  class_mode = 'categorical'
)

test_datagen <- image_data_generator(rescale = 1./255)
test_generator <- flow_images_from_directory(
  'handwriting_shape/test', generator = test_datagen,
  target_size = c(24,24),
  batch_size =3,
  class_mode = 'categorical'
)

### 모형 정의 
model <- keras_model_sequential() %>%
  layer_conv_2d(filters = 32, kernel_size = c(3,3),
                activation = 'relu', input_shape = c(24,24,3)) %>%
  layer_conv_2d(filters = 64, kernel_size = c(3,3),
                activation = 'relu') %>%
  layer_max_pooling_2d(pool_size = c(2,2)) %>%
  layer_flatten() %>%
  layer_dense(units = 128, activation = 'relu')%>%
  layer_dense(units = 3, activation = 'softmax')
model %>% compile(loss = "categorical_crossentropy",
                  optimizer = 'adam', metrics = c('accuracy'))
history <-model %>% fit_generator(
  train_generator,
  steps_per_epoch = 15,
  epochs = 50,
  validation_data = test_generator,
  validation_steps = 5)
# loss: 3.9882e-06 - accuracy: 1.0000 - val_loss: 0.0054 - val_accuracy: 1.0000
output <- model %>% predict_generator(test_generator, steps = 5)
test_generator$class_indices
round(output,3)
