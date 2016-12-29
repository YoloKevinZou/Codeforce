n, m = map(int, raw_input().split())
word_map = {}

for i in xrange(m):
	first,second = map(str, raw_input().split())
	word_map[first] = second

sentence = raw_input().split()

for word in sentence:
	translated_word = word_map[word]

	if len(word) <= len(translated_word):
		print word,
	elif len(word) > len(translated_word):
		print translated_word,