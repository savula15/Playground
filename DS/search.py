import time


def ls(myit, myli):
    for (index, value) in enumerate(myli):
        if value == myit:
            return index
    return -1


def bs(myit, myli):
    lb = 0
    ub = len(myli)

    while True:
        if lb == ub:
            return -1

        mid_index = (lb + ub) // 2

        item_at_middle = myli[mid_index]

        if item_at_middle == myit:
            return mid_index
        if item_at_middle < myit:
            lb = mid_index + 1
        else:
            ub = mid_index


def binary_stride(alist, aitem):
    n = len(alist)
    stride = n // 2
    pos = 0

    while stride >= 1:
        while pos+stride < n and alist[pos+stride] <= aitem:
            pos += stride
        stride //= 2
    if alist[pos] == aitem:
            return pos
    return -1


def find_unknown_words(vocab_words, book_words):
    result = []
    for word in book_words:
        if bs(word, vocab_words) < 0:
            result.append(word)

    return result


def find_unknown_merge_pattern(vocab_words, book_words):
    result = []
    xi = 0
    yi = 0

    while True:
        if vocab_words[xi] == book_words[yi]:
            yi += 1
        elif vocab_words[xi] < book_words[yi]:
            xi += 1
        else:
            result.append(book_words[yi])
            yi += 1

    if xi >= len(vocab_words):
        result.extend(book_words[yi:])
    if yi >= len(book_words):
        result.extend(vocab_words[xi:])

    return result


def remove_adjacent_dups(myli):
    result = []
    most_recent_element = None

    for element in myli:
        if element != most_recent_element:
            result.append(element)
            most_recent_element = element

    return result


def text_to_words(text):
      word_list = []
      character_list = []
      for ch in text:
            if ch.isalnum():
                  character_list.append(ch)
            elif len(character_list) > 0:
                  word = "".join(character_list)
                  word = word.lower()
                  word_list.append(word)
                  character_list = []
      if len(character_list) > 0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)

      return word_list

def get_words_from_book(file1):
      with open(file1) as f:
            lines = f.readlines()
            word_list = []
            for line in lines:
                  words_in_line = text_to_words(line)
                  word_list = word_list + words_in_line
            return word_list


if __name__ == '__main__':

      vocab_words = get_words_from_book('vocab.txt')
      all_words_in_book = get_words_from_book('book.txt')
      t0 = time.clock()
      all_words_in_book.sort()
      book_words = remove_adjacent_dups(all_words_in_book)
      missing_words = find_unknown_merge_pattern(vocab_words, book_words)
##      missing_words = find_unknown_words(vocab_words, book_words)
      t1 = time.clock()

      print('There are {0} missing words'.format(len(missing_words)))
      print('It took {0:.15f} seconds to find out missing words'.format(t1-t0))

      print('There are total {0} words in the book and only {1} are unique in book'.format(len(all_words_in_book), len(book_words)))
##      print('First 100 words are {0}'.format(book_words[0:100]))
      print


