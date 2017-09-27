import tflearn
import	speech_data

learning_rate = 0.0001
training_iterations = 30000

batch = word_batch = speech_data.mfcc_batch_generator(64)

X,Y  = next(batch)

trainX, trainY = X,Y
testX, testY = X,Y

net = tflearn.input_data([None, 80, 20])
net = tflearn.lstm(net, 128, dropout = 0.8)
net = tflearn.fully_connected(net, 10, activation = 'softmax')
net = tflearn.regression(net, optimizer = 'adam', learning_rate = learning_rate, loss = 'categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_verbose = 0)

while 1:
	model.fit(trainX, trainY, n_epoch = 10, validation_set = (testX, testY), show_metric= True, batch_size = 64)
	Y_ = model.predict(X)

model.save('tflearn.lstm.model')
