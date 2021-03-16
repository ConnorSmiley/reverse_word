def reverse_string(word):
  reversed_word = ""
  for index in range(1, len(word) + 1):
    reversed_word += word[index * -1]
  return reversed_word



def reverse_string(word):
    return word[::-1]



def reverse_string(word):
  reversed_word = ""
  for index in range(1, len(word) + 1):
    reversed_word += word[index * -1]
  return reversed_word