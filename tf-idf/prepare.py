import os
# read the index.txt and preapre documents,vocab,idf
with open('index.txt','r') as f:
    lines=f.readlines()
    # print(lines)

def preprocess(document_text):
    terms=[term.strip() for term in document_text.lower().split()[1:]]
    # terms=[term.lower() for term in document_text.strip().split()[1:]]
    # print(terms)
    return terms

def read_files_in_folders(parent_folder):
    paragraphs=[]
    for folder_name in sorted(os.listdir(parent_folder)):
        folder_path = os.path.join(parent_folder, folder_name)
        if os.path.isdir(folder_path):
            file_name = folder_name + '.txt'
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r',encoding='utf-8') as file:
                    paragraphs.append(file.read())
                    # print(paragraphs)
    return paragraphs                
                    
parent_folder = 'Qdata'
paragraphs=read_files_in_folders(parent_folder)

def process(para):
    words=para.strip().split()
    word="Example"
    index=words.index(word) if word in words else len(words)
    append_sentence=' '.join(words[:index])
    return append_sentence

for index,para in enumerate(paragraphs):
    lines[index]=lines[index] +" "+process(para)
print(lines)

vocab={}
documents=[]
for index,line in enumerate(lines):
    # print(index)
    # read that problem statement and add it to the document string


    tokens=preprocess(line)
    documents.append(tokens)
    
    # print(documents[:5])
    tokens=set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token]=1
        else:
            vocab[token]+=1
# gives the frequency of "term" across all documents 
# that is if the is present twice in same documents we count it only once not twice
# if the is present in doc-2 then we do frequency+=1


# reverse sort the vocab by the values
vocab=dict(sorted(vocab.items(),key=lambda item: item[1], reverse=True))

# print("Number of documnets: ",len(documents))
# print("Size of vocab: ",len(vocab))
# print("Sample document: ",documents[0])
# print(vocab)

# save the vocab in a text file

with open('tf-idf/vocab.txt','w') as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

with open('tf-idf/idf-values.txt','w') as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])


# saving documents in text file
with open('tf-idf/documents.txt','w') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))



# inverted index construction
inverted_index={}
for index,document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token]=[index]
        else:
            inverted_index[token].append(index)

# save the inverted index in a text file
with open('tf-idf/inverted-index.txt','w') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join(str(doc_id) for doc_id in  inverted_index[key]))
