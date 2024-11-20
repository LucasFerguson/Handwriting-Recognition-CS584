import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

print("\nBuild Info:")
sys_details = tf.sysconfig.get_build_info()
print(f"CUDA Version: {sys_details['cuda_version']}")