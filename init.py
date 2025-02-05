from hood import handler

if __name__ == "__main__":
    
    #
    
    dataset_path_train = "/content/dataset/train/"
    dataset_path_validation = "/content/dataset/validation/"
    #dataset_path_validation = False
    
    #
    
    buffer_size = 100
    
    #
    
    transforming_shape = (450, 450)
    transforming_convs = 3
    
    #
    
    metric_target = 0.05
    
    #
    
    save_path = "/content/"
    
    #
    
    handler = handler.Handler(dataset_path_train, dataset_path_validation, buffer_size, input_image, output_labels, metric_target, save_path)
    handler.start()
    
    #
#