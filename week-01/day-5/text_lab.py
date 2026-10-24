sentence = input("Sentence: ")

chars_with_spaces=len(sentence)

chars_no_spaces = len(sentence.replace(" ", ""))


words_list=sentence.split()
word_count=len(words_list)

upper_sentence=sentence.upper()
reversed_sentence=sentence[::-1]

count_a=sentence.lower().count('a')

slug = sentence.strip().lower().replace(" ", "_")

if word_count > 0:
     first_word=words_list[0]
     last_word=words_list[-1]

else:
    first_word = ""
    last_word = ""

mentions_python="python" in sentence.lower()

print(f"chars (with spaces) : {chars_with_spaces}")
print(f"chars (no spaces)    : {chars_no_spaces}")
print(f"words                : {word_count}")
print(f"upper                : {upper_sentence}")
print(f"reversed             : {reversed_sentence}")
print(f"count of 'a'         : {count_a}")
print(f"slug                 : {slug}")
print(f"first / last word    : {first_word} / {last_word}")
print(f"mentions python      : {mentions_python}")
