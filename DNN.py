import tensorflow as tf
import numpy as np

#Creating vocabularies for dictionaries
vocab_hate = tf.feature_column.categorical_column_with_vocabulary_file(key = "hate_words", vocabulary_file = "hatewords.txt")
vocab_negative = tf.feature_column.categorical_column_with_vocabulary_file(key = "negative_words", vocabulary_file = "negative.txt")
vocab_modern_acronyms = tf.feature_column.categorical_column_with_vocabulary_file(key = "acronyms", vocabulary_file = "acronyms.txt")

#Creation of feature columns
vocab_hate_emb = tf.feature_column.embedding_column(categorical_column=vocab_hate, dimension = 9)
vocab_negative_emb = tf.feature_column.embedding_column(categorical_column=vocab_negative, dimension = 9)
vocab_modern_acronyms_emb = tf.feature_column.embedding_column(categorical_column=vocab_modern_acronyms, dimension = 9)

feature_columns = [vocab_hate_emb, vocab_negative_emb, vocab_modern_acronyms_emb]

#Creation of Deep Neural Net Classifier using above dictionaries
estimator = tf.estimator.DNNClassifier(feature_columns = feature_columns, hidden_units = [500, 300])

#Features used when searching
feat = {'hate_words': ['retard', 'dyke'],
            'negative_words': ['hate', 'unhappy'],
            'acronyms': ['jfc', 'smh'],
            }

# Input Builders
def input_fn_train(features, labels, batch_size):
    dataset = tf.data.TextLineDataset(filenames = 'training_data.txt')
    dataset = dataset.from_tensor_slices((dict(features), labels))
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)
    return dataset

#wrapper to allow the passing of variables into training algorithm
def input_fn_train_wrapper():
    return input_fn_train(feat, np.array([0,1]), batch_size = 1000)


def input_fn_eval(features, labels, batch_size):
    features = dict(features)
    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)
    dataset = tf.data.TextLineDataset(filenames = 'testing_data.txt')
    dataset = dataset.from_tensor_slices(inputs)
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)
    return dataset

#wrapper to allow the passing of variables into testing algorithm
def input_fn_eval_wrapper():
    return input_fn_eval(feat, np.array([0,1]), batch_size = 1000)

#train DNN
estimator = estimator.train(input_fn = input_fn_train_wrapper, steps = 100)

#test DNN
metrics = estimator.evaluate(input_fn=input_fn_eval_wrapper, steps = 100)

#print results
print(metrics)
