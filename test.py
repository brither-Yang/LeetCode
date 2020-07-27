def closed_1(word1, word2):
    assert len(word1) == len(word2)
    one_word_length = len(word1)
    two_words_length = len(set(word2) | set(word1))
    return two_words_length - one_word_length

def haha():
    lists = ["hot", "dot", "dog", "lot", "log", "cog"]
    target = 'cog'

    if target in lists:
        lists.remove(target)
    else:
        return 0
    res = []
    queue = [('hit', 0)]
    visited = {'hit', }
    while queue:
        ss = queue.pop(0)
        print(ss)
        word = ss[0]
        step = ss[1]

        for i in lists:
            if closed_1(i, target) == 1:
                return step + 1
            if closed_1(i, word) == 1 and i not in visited:
                queue.append((i, step + 1))
                visited.add(i)
    return 0


print(haha())