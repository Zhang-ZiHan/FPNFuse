
class args():
	# training args
	epochs = 4
	batch_size = 1
	dataset = "/data/Disk_B/MSCOCO2014/train2014/"
	HEIGHT = 256
	WIDTH = 256

	save_model_dir_autoencoder = "models/nestfuse_autoencoder"
	save_loss_dir = './models/loss_autoencoder/'

	cuda = 1
	ssim_weight = [1,10,100,1000,10000]
	ssim_path = ['1e0', '1e1', '1e2', '1e3', '1e4']

	lr = 1e-4
	lr_light = 1e-4
	log_interval = 10
	resume = None

	model_default ='models/nestfuse_autoencoder/1e2/Final_epoch_2_Sat_Sep_19_16_52_25_2020_1e2.model'
	model_deepsuper = './models/nestfuse_1e2_deep_super.model'


