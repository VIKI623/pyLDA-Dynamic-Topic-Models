# coding: utf-8
import csv, time
from gensim.models import ldaseqmodel
from gensim import corpora
import pyLDAvis


if __name__ == "__main__":

    start_time = time.time()

    raw_corpus = []
    time_dic = {}
    time_slice = []

    # Read stop list data
    with open("stop_word_list.txt", "r") as stop_list_file:
        stop_list_lines = stop_list_file.readlines()
        new_stop_list = []
        for stop_word in stop_list_lines:
            new_stop_list.append(stop_word.strip())
        stoplist = set(new_stop_list)

    # Read doc data
    # TODO: replace the file name in following line with your data source
    with open("data_1554124264.csv", "r") as csvfile_in:
        csv_reader = csv.reader(csvfile_in)
        csv_header = next(csv_reader)
        for row in csv_reader:
            month_time = row[1][0:4]
            raw_corpus.append(row[2])
            if month_time in time_dic:
                time_dic[month_time] += 1
            else:
                time_dic[month_time] = 1
    
    # Count doc every year
    for month_key in sorted(time_dic.keys()):
        time_slice.append(time_dic[month_key])
    
    # Lowercase each document, split it by white space and filter out stopwords
    texts = [[word for word in document.lower().split() if word not in stoplist]
            for document in raw_corpus]

    # Count word frequencies
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    # Only keep words that appear more than once
    processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
    dictionary = corpora.Dictionary(processed_corpus)
    bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

    # Model
    num_topics = 5
    ldaseq = ldaseqmodel.LdaSeqModel(corpus=bow_corpus, id2word=dictionary, time_slice=time_slice, num_topics=num_topics)

    # Output topic every year
    word_num = 12
    out_path = "topic"
    with open(out_path + ".csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        header = []
        for i in range(0, num_topics):
            header.append(("topic_" + str(i + 1)))
        writer.writerow(header)
        for j in range(0, len(time_slice)):
            writer.writerow(ldaseq.print_topics(j, word_num))

    # Visualising Dynamic Topic Models
    doc_topic, topic_term, doc_lengths, term_frequency, vocab = ldaseq.dtm_vis(time=0, corpus=bow_corpus)
    vis_dtm = pyLDAvis.prepare(topic_term_dists=topic_term, doc_topic_dists=doc_topic, doc_lengths=doc_lengths, vocab=vocab, term_frequency=term_frequency)

    print("\ndone @{}(s)\n".format(time.time() - start_time))

    pyLDAvis.save_html(vis_dtm, "result.html")