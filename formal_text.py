import nltk
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag

# Download NLTK data required for tokenization
nltk.download('punkt')

def correct_spelling(text):
    corrected_words=[]
    spell = SpellChecker()
    words = word_tokenize(text)
    tags=pos_tag(words)
    print(tags)
    for i in range(len(words)):
        if not spell.known([words[i]]):
            if tags[i][0] in words[i]:
                if tags[i][1]=="NN" or tags[i][1]=="NNP":
                    words[i]=words[i]
                    corrected_words.append(words[i])
                else:
                    words[i]=spell.correction(words[i])
                    corrected_words.append(words[i])
            else:
                corrected_words.append(words[i])
        else:
            corrected_words.append(words[i])
    #corrected_words = [spell.correction(word) if not spell.known([word]) else word for word in words]
    print(corrected_words)
    corrected_text = ' '.join(corrected_words)
    return corrected_text

def make_text_formal(text):
    informal_to_formal = {
        "gonna": "going to",
        "wanna": "want to",
        "gotta": "got to",
        "ain't": "is not",
        "don't": "do not",
        "can't": "cannot",
        "won't": "will not",
        "isn't": "is not",
        "you're": "you are",
        "doesn't": "does not"
    }
    words = word_tokenize(text)
    formal_words = [informal_to_formal.get(word.lower(), word) for word in words]
    
    # Capitalize the first letter of each sentence
    sentences = sent_tokenize(' '.join(formal_words))
    formal_text = ' '.join(sentence.capitalize() for sentence in sentences)
    return formal_text

def main(input_text):
    formal_list=[]
    sentence_list=[]
    sentences=sent_tokenize(input_text)
    for i in sentences:
        if i==".":
            sentences.remove(i)
    print("sentences",sentences)
    for sentence in sentences:
        if sentence[-1]==".":
            sentence_list.append(sentence)
        if sentence[-1]!=".":
            sentence=sentence+"."
            sentence_list.append(sentence)
    for sentence in sentence_list:
    # Correct spelling in the input text
        corrected_spelling = correct_spelling(sentence)    
    # Make the corrected text more formal
        formal_text = make_text_formal(corrected_spelling)
        formal_list.append(formal_text)
        print("$#".join(formal_list))
    return "$#".join(formal_list)

