class parameters():

    prog_name = "retriever"

    # set up your own path here
    root_path = "/workspace/ML-Capstone/"
    output_path = "/workspace/ML-Capstone/outputs/retriever/"
    cache_dir = "/workspace/ML-Capstone/cache/retriever/"

    # the name of your result folder.
    model_save_name = "retriever-bert-base-uncased"

    train_file = root_path + "dataset/train.json"
    valid_file = root_path + "dataset/dev.json"

    test_file = root_path + "dataset/test.json"

    op_list_file = "operation_list.txt"
    const_list_file = "constant_list.txt"

    # model choice: bert, roberta
    pretrained_model = "bert"
    model_size = "bert-base-uncased"

    # pretrained_model = "roberta"
    # model_size = "roberta-base"

    # train, test, or private
    # private: for testing private test data
    device = "cuda"
    mode = "train"
    resume_model_path = ""

    ### to load the trained model in test time
    saved_model_path = output_path + \
        "bert-base-6k_20210427232814/saved_model/loads/3/model.pt"
    build_summary = False

    option = "rand"
    neg_rate = 3
    topn = 5

    sep_attention = True
    layer_norm = True
    num_decoder_layers = 1

    max_seq_length = 512
    max_program_length = 100
    n_best_size = 20
    dropout_rate = 0.1

    batch_size = 16
    batch_size_test = 16
    epoch = 10
    learning_rate = 2e-5

    report = 1000
    report_loss = 100
