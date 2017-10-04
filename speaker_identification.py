import os
import tensorflow as tf
import tflearn
import speech_data

print (tf.__version__)

speakers = speech_data.get_speakers()

number_classes = len(speakers)

batch = speech_data.wave_batch_generator(batch_size = 1000, source=speech_data.Source.DIGIT_WAVES, target = speech_data.Target.speaker)

X,Y = next(batch)

tflearn.init_graph(num_cores = 8, gpu_memory_fraction = 0.5)

#Neural Net
net = tflearn.input_data(shape=[None, 8192])
net = tflearn.fully_connected(net, 64)
net = tflearn.dropout(net,0.5)
net = tflearn.fully_connected(net, number_classes, activation = 'softmax')

net = tflearn.regression(net, optimizer = 'adam', loss = 'categorical_crossentropy')

#Model
model = tflearn.DNN(net)
model.fit(X,Y, n_epoch=100, show_metric=True, snapshot_step = 100)

demofile = '8_Bruce_260.wav'
demo = data.load_wav_file(data.path + demofile)
result = model.predict([demo])
result = data.one_hot_to_item(results, speakers)

print(demofile, result)
