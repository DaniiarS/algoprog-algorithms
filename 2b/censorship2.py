def split_words(sentense: str):
    DELIMETERS = '.!?:-,;() '

    words = []
    word = ''

    start_read = False
    word_added = False # if the line consists of one word

    for char in sentense:
        if (char not in DELIMETERS) and (not start_read): # First encountered char - started reading
            word_added = False
            start_read = True
            word += char
        elif (char not in DELIMETERS) and start_read: # Started reading word - continue to read the word
            word += char
        elif (char in DELIMETERS) and start_read: # Encountered delimeter - stop reading and saving word
            start_read = False
            words.append(word)
            word_added = True
            word = ''

        
    if not word_added:
        words.append(word)

    return words




input_file = open('input.txt', 'r', encoding='cp866')
file_content = input_file.read()

# print(input_file.readlines())

# print(file_content)

sentences = file_content.split('\n')
modified_sentences = []

# print(sentences)

# Delete delimeters and split words
for sentence in sentences:
    modified_sentence = split_words(sentence)
    modified_sentences.append(modified_sentence)
# print(modified_sentences)

line_flags = [0 for i in range(len(modified_sentences))]
line_index = 0

# Count suspecious words
for modified_sentence in modified_sentences:
    count_suspecious = 0
    sentence_size = len(modified_sentence)

    for word in modified_sentence:
        char_dict = {}

        for char in word:
            if char not in char_dict.keys():
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        
        if len(char_dict.keys()) < 4:
            count_suspecious += 1
    
    if count_suspecious >= sentence_size/2:
        line_flags[line_index] = 1
    
    line_index += 1

input_file.close()
output_file = open('output.txt', 'w', encoding='cp866')

input_file = open('input.txt', 'r', encoding='cp866')
sentences = input_file.readlines()
# print(sentences)
# print(line_flags)

line_flags_size = len(line_flags)
for i in range(line_flags_size):
    if line_flags[i] == 0:
        # print(sentences[i])
        output_file.write(sentences[i])

input_file.close()
output_file.close()




