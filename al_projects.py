import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def load_data(path):
	try:
		data = pd.read_csv(path)
	except:
		print("Invalid file error.")
		sys.exit()
	#print("data shape:", data.shape)
	columns = data.columns.tolist()

	return (data.values, columns)

def normalization(data):
	data_min = np.min(data, axis=0)
	data_max = np.max(data, axis=0)
	normalized_data = (data - data_min) / (data_max - data_min)
	return normalized_data, data_min, data_max

def denormalization(normalized_data, data_min, data_max):
	x = normalized_data * (data_max - data_min)
	denormalized_data = normalized_data * (data_max - data_min) + data_min
	return denormalized_data

def plot_scatter(data, feature, target):
	plt.scatter(data[:, 0], data[:, 1])
	plt.title(f'Scatter Plot: {feature} vs {target}')
	plt.xlabel(feature)
	plt.ylabel(target)
	plt.show()

if __name__ == "__main__":
	# Load the data
	data, columns = load_data("al_projects.csv")
	print(data[:,2:])
	print(columns)

	# Normalization
	normalized_data, data_min, data_max = normalization(data[:,2:])
	print(normalized_data)
	plot_scatter(normalized_data, columns[2], columns[3])
