'''
127. 单词接龙
给定两个单词（beginWord 和 endWord）和一个字典，
找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。
'''


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        word_set = set(wordList)

        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        stack = [(beginWord, 1)]
        visited = {beginWord, }

        while stack:
            tem = []
            for token in stack:
                word = token[0]
                step = token[1]

                word_len = len(word)

                for i in range(word_len):
                    word_list = list(word)

                    for j in range(26):
                        word_list[i] = chr(ord('a') + j)
                        new_word = ''.join(word_list)

                        if new_word in word_set:
                            if new_word == endWord:
                                return step + 1
                            if new_word not in visited:
                                tem.append((new_word, step + 1))
                                visited.add(new_word)
            stack = tem
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "cog"]
    ss = Solution()
    res = ss.ladderLength(beginWord, endWord, wordList)
    print(res)