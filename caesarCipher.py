""" Ceaser Cypher """

# Declare Variables
lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
			'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
			's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
			'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
			'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
newWord = ''

# Request input
word = input("Enter word: ")
shiftLength = input("Shift by how much: ")

# Loop through each letter in word
for i in range(0, len(word)):
	# If the character is a special character...
	if (word[i] == ',' or word[i] == '.' or word[i] == " " or word[i] == "!"):
		# Add the letter to the new word without making any changes
		newWord = newWord + word[i]
	# If the character is a letter...
	else:
		# If the letter is lower case...
		if word[i] in lower_alphabet:
			# Shift character by inputed shiftLength and add to the new word
			oldIndex = lower_alphabet.index(word[i])
			newIndex = (oldIndex + int(shiftLength)) % 26
			newWord = newWord + lower_alphabet[newIndex]
		# If the letter is upper case...
		elif word[i] in upper_alphabet:
			# Shift character by inputed shiftLength and add to the new word
			oldIndex = upper_alphabet.index(word[i])
			newIndex = (oldIndex + int(shiftLength)) % 26
			newWord = newWord + upper_alphabet[newIndex]

# Print output
print(newWord)