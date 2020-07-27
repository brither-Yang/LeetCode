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

        def closed_1(word1, word2):
            assert len(word1) == len(word2)
            one_word_length = len(word1)
            two_words_length = len(set(word2) | set(word1))
            return two_words_length - one_word_length

        if endWord not in wordList:
            return 0

        wordList.remove(endWord)

        queue = [(beginWord, 1)]
        visited = {beginWord, }

        while queue:
            node = queue.pop(0)
            word = node[0]
            step = node[1]

            res = [x for x in wordList if closed_1(x, word) == 1]

            for i in res:
                if closed_1(i, endWord) == 1:
                    return step + 2
                if i not in visited:
                    visited.add(i)
                    queue.append((i, step+1))

        return 0


if __name__ == '__main__':
    ss = Solution()
    print(ss.ladderLength("hit", "cog", ["hot","dot","log","cog"]))

#         words_dict = {}
#         for i in wordList:
#             words_dict[i] = words_dict.get(i, 0) + 1
#
#         if len(wordList) == 0 or endWord not in words_dict:
#             return 0
#
#         queue = [beginWord, 0]
#         visited = {beginWord, }
#
#         while queue:
#             n = len(queue)
#             for i in range(n):
#                 word = queue.pop(0)
#
#
# ss = Solution()
# print(ss.ladderLength(beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]))
#
#
# 智能模式
# 12
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
# 控制台
# 贡献
# 2 / 229
#
# 广度优先遍历、双向广度优先遍历（Java、Python）
# liweiwei1419
# 发布于 2020-06-05
# 4.6k
# 一句话题解
# 无向图中两个顶点之间的最短路径的长度，可以通过广度优先遍历得到；
# 为什么 BFS 得到的路径最短？可以把起点和终点所在的路径拉直来看，两点之间线段最短；
# 已知目标顶点的情况下，可以分别从起点和目标顶点（终点）执行广度优先遍历，直到遍历的部分有交集，这是双向广度优先遍历的思想。
# 视频解题
# 视频时间线：建议倍速观看
#
# 读题、讲解注意事项：00:00 开始
# 分析示例 1 并讲解如何建图、BFS、双向 BFS 思路：02:58 开始
# 讲解 BFS 代码：11:41 开始
# 讲解双向 BFS 代码：18:54 开始
#
# 分析题意：
#
# 「转换」意即：两个单词对应位置只有一个字符不同，例如 "hit" 与 "hot"，这种转换是可以逆向的，
# 因此，根据题目给出的单词列表，可以构建出一个无向（无权）图；
# image.png
#
# 如果一开始就构建图，每一个单词都需要和除它以外的另外的单词进行比较，复杂度是 O(N \rm{wordLen})O(NwordLen)，这里 NN 是单词列表的长度；
# 为此，我们在遍历一开始，把所有的单词列表放进一个哈希表中，然后在遍历的时候构建图，每一次得到在单词列表里可以转换的单词，
# 复杂度是 O(26 \times \rm{wordLen})O(26×wordLen)，借助哈希表，找到邻居与 NN 无关；
# 使用 BFS 进行遍历，需要的辅助数据结构是：
# 队列；
# visited 集合。说明：可以直接在 wordSet (由 wordList 放进集合中得到)里做删除。
# 但更好的做法是新开一个哈希表，遍历过的字符串放进哈希表里。这种做法具有普遍意义。绝大多数在线测评系统和应用场景都不会在意空间开销。
# 方法一：广度优先遍历
# 参考代码 1：
#
#
# from typing import List
# from collections import deque
#
#
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         word_set = set(wordList)
#         if len(word_set) == 0 or endWord not in word_set:
#             return 0
#
#         if beginWord in word_set:
#             word_set.remove(beginWord)
#
#         queue = deque()
#         queue.append(beginWord)
#
#         visited = set(beginWord)
#         visited.add(beginWord)
#
#         word_len = len(beginWord)
#         step = 1
#         while queue:
#             current_size = len(queue)
#             for i in range(current_size):
#                 word = queue.popleft()
#
#                 word_list = list(word)
#                 for j in range(word_len):
#                     origin_char = word_list[j]
#
#                     for k in range(26):
#                         word_list[j] = chr(ord('a') + k)
#                         next_word = ''.join(word_list)
#                         if next_word in word_set:
#                             if next_word == endWord:
#                                 return step + 1
#                             if next_word not in visited:
#                                 queue.append(next_word)
#                                 visited.add(next_word)
#                     word_list[j] = origin_char
#             step += 1
#         return 0
#
#
# if __name__ == '__main__':
#     beginWord = "hit"
#     endWord = "cog"
#     wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
#     solution = Solution()
#     res = solution.ladderLength(beginWord, endWord, wordList)
#     print(res)