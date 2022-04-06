import itertools
import string
import collections
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--text", help = "Message or Ciphertext..")
parser.add_argument("-k", "--key", help = "Key..")
parser.add_argument("-t", "--task", help = "should be 1 for decrypting and 0 for encrypting...")
args = parser.parse_args()
#parser.parse_args()

text = args.text
key = args.key
task = args.task


def encrypt(text,key,multiplier = -1):
	compressed_text = text.lower()
	## removing punctautions
	for punctuation in str(string.punctuation+' '):
		compressed_text = compressed_text.replace(punctuation,'')
	## preparing key of length same as cipher, just by repating it again and again
	cycler = itertools.cycle(key.lower())
	long_key = ''.join([ next(cycler) for _ in range(len(compressed_text))])
	#print(long_key)

	## encryption part
	#print(compressed_text)
	coded = []
	for number in range(len(long_key)):
		cipher_letter = compressed_text[number]
		key_letter = long_key[number]
		key_index = string.ascii_lowercase.index(key_letter)
		cipher_index = string.ascii_lowercase.index(cipher_letter)
		lowercase = collections.deque(string.ascii_lowercase)
		lowercase.rotate(multiplier * key_index)
		new_alphabet = ''.join(list(lowercase))
		new_character = new_alphabet[cipher_index]
		coded.append(new_character)
	return ''.join(coded)
def decrypt(text,key):
	return encrypt(text,key,1)

#encrypt(cipher,key,-1)


if task == "1":
   print(decrypt(text,key))
elif task == "0":
	print(encrypt(text,key,-1))
else:
	print("Wrong Argument is provided , check vignere-en-de -h")
	exit()
