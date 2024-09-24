import nltk
from textblob import TextBlob
from nltk.tokenize import word_tokenize, sent_tokenize


nltk.download('punkt')

def correct_spelling(text):

    try:
        blob = TextBlob(text)
        corrected_text = blob.correct()
        return str(corrected_text)
    except Exception as e:
        print(f"Error in spelling correction: {e}")
        return text

def process_text(text):

    try:
        sentences = sent_tokenize(text)
        processed_sentences = []

        for sentence in sentences:
            words = word_tokenize(sentence)
            processed_sentences.append(" ".join(words))

        return " ".join(processed_sentences)
    except Exception as e:
        print(f"Error in text processing: {e}")
        return text

def main(input_text):
    corrected_spelling = correct_spelling(input_text)
    original_words=word_tokenize(input_text)
    corrected_words=word_tokenize(corrected_spelling)
    wrong_word=[]
    correct_word=[]
    new_input_list=[]
    if len(wrong_word)==len(correct_word):
        for i,j in zip(original_words,corrected_words):
            if i!=j:
                wrong_word.append(i)
                correct_word.append(j)
        if len(correct_word)!=0:
            message=f'Warning: found some mistake in : {input_text} <br> it should be like : {corrected_spelling} <br><br> mistakes : {wrong_word} <br> correction : {correct_word} '
        else:
            message=""
    else:
        new_input=word_tokenize(input_text)
        for words in new_input:
            new_input_list.append("".join(words))
        processing_text=" ".join(new_input_list)
        if len(processing_text)==len(corrected_words):
            for i,j in zip(processing_text,corrected_words):
                wrong_word.append(i)
                correct_word.append(j)
        if len(correct_word)!=0:
            message=f'Warning: found some mistake in : {input_text} <br> it should be like : {corrected_spelling} <br><br> mistakes : {wrong_word} <br> correction : {correct_word} '
        else:
            message=""

    processed_text = process_text(corrected_spelling)
 
    return message
