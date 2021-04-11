import numpy as np

#function to normalize the prices data used by wavelet_prices_smooth
def Normalize_Data_Data_Raw(resize_data):
	normal_data = []
	local_min_val = 99999999999
	local_max_val = -99999999999
	for i in range (0, len(resize_data)-1):
		if resize_data[i] > local_max_val:
			local_max_val = resize_data[i]
		if resize_data[i] < local_min_val:
			local_min_val = resize_data[i]
	for i in range (0, len(resize_data)-1):
		normal_data.append( (resize_data[i] - local_min_val)/(local_max_val - local_min_val) )
	np.array(normal_data)
	return(normal_data)
	
#function to normalize data used by MLP and GRU model
def Normalize_Data_DataSet(resize_data):
	normal_data = []
	local_min_val = 99999999999
	local_max_val = -99999999999
	for i in range(len(resize_data)):
		for j in range(len(resize_data[i])):
			if resize_data[i][j] > local_max_val:
				local_max_val = resize_data[i][j]
			if resize_data[i][j] < local_min_val:
				local_min_val = resize_data[i][j]
	for i in range(len(resize_data)):
		temp = []
		for j in range(len(resize_data[i])):
			temp.append((resize_data[i][j] - local_min_val)/(local_max_val - local_min_val))
		temp = np.array(temp)
		normal_data.append(temp)
	new_normal_data = np.array(normal_data)
	return(local_min_val, local_max_val, new_normal_data)

#function to denormalize data used by MLP and GRU model
def DeNormalize(data, min, max):
    denorm_data = []
    for i in range (len(data)):
        denorm_data.append((data[i]*(max - min))+min)
    return(np.array(denorm_data))
	
#function used to split dataset into training, validation and test set
def Divide_Data(normal_data):
    proportion = int((len(normal_data) / 7))
    test_dim = int((len(normal_data) - (2*proportion)))
    train = []
    test = []
    valid = []
    for i in range(test_dim):
        train.append(normal_data[i])
    for i in range(test_dim + 1, test_dim+proportion):
        valid.append(normal_data[i])
    for i in range(test_dim + proportion + 1, len(normal_data)):
        test.append(normal_data[i])
    train = np.array(train)
    test = np.array(test)
    valid = np.array(valid)
    return(train, test, valid)

#function used to create the final dataset	
def CreateDataset(resize_data, campioni):
	images = []
	labels = []
	new_images = []
	new_labels = []
	size_campioni = int(campioni)
	for i in range(0, len(resize_data)-size_campioni):
		img = []
		for j in range(0, size_campioni):
			img.append(resize_data[i+j])
		labels.append(resize_data[i+size_campioni])
		images.append(np.array(img))
	new_images = np.array(images)
	new_labels = np.array(labels)
	return(new_images, new_labels)