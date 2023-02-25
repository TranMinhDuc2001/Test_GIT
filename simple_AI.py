import tensorflow as tf

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

model.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

xs = [1, 2, 3, 4]
ys = [2, 4, 6, 8]

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
