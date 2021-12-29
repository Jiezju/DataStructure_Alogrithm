class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = {}
        self.change_word_dict = {}

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            self.word_dict[word] = 1
            for index in range(len(word)):
                tmp = word[:index] + '*' + word[index + 1:]
                # 统计替换字符的字典
                self.change_word_dict[tmp] = self.change_word_dict.get(tmp, 0) + 1
        
    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        
        print(self.change_word_dict)
        print(self.word_dict)
        for index in range(len(searchWord)):
            tmp = searchWord[:index] + '*' + searchWord[index + 1:]
            # 查看 查找字符 替换一个字符 是否存在之前的字典中
            # self.word_dict.get(searchWord, 0) 防止 查找字符串就是 存储字符串
            if self.change_word_dict.get(tmp, 0) - self.word_dict.get(searchWord, 0) > 0:
                print(self.change_word_dict)
                print(self.word_dict)
                return True

        return False

if __name__ == '__main__':
    obj = MagicDictionary()
    obj.buildDict(["hello"])
    param_2 = obj.search('hhllo')