## Hash Map

- Python 的 dictionary 和 set 的基本操作

	- dictionary

		![](./img/pythondict.png)
    
    - set

		![](./img/pythonset.png)
        
- python dictionary 扩展

	- Counter 

		传入字符串进行字符统计，同时支持返回最大词频
        
    - defaultdict

		当key不存在dict中，defaultdict支持默认的value设置
        
  - OrderedDict
   	
     有序字典，默认的python dict
     
     
#### **1. 字频统计**

- 解题思路

	遍历字符串，使用字典统计

- 核心代码

	```python
    # 统计字频
    for c in s:
    	if c != ' ' and c.isalpha():
        	# freq.get(word, 0)  default 0
            freq[c] = freq.setdefault(word, 0) + 1
    ```
    
    ```python
    # 获取字典最大 频率 的 key
    max_word = ''
    max_count = 0
    for (w,c) in freq.items():
        if c > max_count:
            max_word = w
            max_count = c
    ```

#### **2. 词频统计**

- 解题思路

	统计单词的频率

- 核心代码

	```python
    # 以空格分割单词，输出列表
    words = s.split(' ')
    for word in words:
        dic[word] = dic.setdefault(word, 0) + 1
    ```
    
    ```python
    wordcount = Counter(s.split()) # 使用 Counter
    ```

#### **3. 找到第一个独特字符的index**

- 解题思路

	- 1. 首先统计字频
	- 2. 再次遍历字符串，出现字频为 1 的返回 index

	另一种使用 python 字符串的 count，返回统计的字符数量
    
- 核心代码

	```python
    index=[s.index(l) for l in letters if s.count(l) == 1]
    ```

#### **4. 两个数组的交集**

- 题目描述

	```python
    Example:

    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

    Note:

    Each element in the result must be unique.
    ```
   
- 解题思路

	求两个 set 的交集
    
- 核心代码

	```python
    list(set(nums1) & set(nums2))
    ```

#### **5. 两个数组的交集II**

- 解题思路

	允许重复元素的交集，需要统计词频，统计重复元素的数量
    
- 核心代码    

	```python
    dict1 = dict()
    for i in nums1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    ret = []
    for i in nums2:
        if i in dict1 and dict1[i]>0:
            ret.append(i)
            dict1[i] -= 1
    ```

#### **6. 钻石与石头**

- 题目描述

	给定钻石代表的字母，从给定的字符串中统计满足钻石的数量
    
    ```python
    Example 1:

    Input: J = "aA", S = "aAAbbbb"

    Output: 3

    Example 2:

    Input: J = "z", S = "ZZ"

    Output: 0
    ```

- 解题思路

	使用 set
    
- 核心代码

	```python
    setJ = set(J)
    return sum(s in setJ for s in S)
    ```
    
#### **7. 重复元素**

- 核心代码

	```python
    len(nums) > len(set(nums))
    ```
    
#### **8. 重复元素II** 

- 题目思路

	给定一个数组一个整数 k， 找到存在的重复元素，且两个元素的索引之差为 小于 k

- 核心代码

	```python
     for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    ```

#### **9. 子网地址的统计** 

- 题目描述

	```python
    Example 1:

    Input: 

    ["9001 scholar.google.com"]

    Output: 

    ["9001 scholar.google.com", "9001 google.com", "9001 com"]

    Example 2:

    Input: 

    ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

    Output: 

    ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
    ```
    
    网址从左到右组成一个局部网址，需要将网址拆成多个网址以后再进行统计
    
- 核心代码

	```python
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        # 获取所有子网
        for i in range(len(frags)):
            ans[".".join(frags[i:])] += count
    ```
    
#### **10. 一行键盘打印字符**

- 题目描述

	给定一个字符串数组，找出使用一行键盘能够打印的字符串
    
- 核心代码

	```python
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    ret = []
    for word in words:
        w = set(word.lower())
        if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
            ret.append(word)
    ```
    
#### **11. 词模式**

- 题目描述

	匹配模式相同
    
    ```python
    Examples:

    pattern = "abba", str = "dog cat cat dog" should return true.

    pattern = "abba", str = "dog cat cat fish" should return false.

    pattern = "aaaa", str = "dog cat cat dog" should return false.

    pattern = "abba", str = "dog dog dog dog" should return false.
    ```
    
- 解题思路

	使用 zip 进行匹配   
    
    ** zip(*iterables) **

    Make an iterator that aggregates elements from each of the iterables.

    Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. 
    
- 核心代码

	```python
    s = pattern
    t = st.split()
    if len(s) != len(t):
    	return False
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
    ```
    
#### **12. 两个列表交集最小 index 和的元素**

- 题目描述

	给定两个 列表，找到列表中的公共元素，且这两个元素的 index 之和最小
    ```python
    Example 1:

    Input:

    ["Shogun", "Tapioca Express", "Burger King", "KFC"]

    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    Output: ["Shogun"]

    Explanation: The only restaurant they both like is "Shogun".

    Example 2:

    Input:

    ["Shogun", "Tapioca Express", "Burger King", "KFC"]

    ["KFC", "Shogun", "Burger King"]

    Output: ["Shogun"]
    ```
    
- 解题思路

	将其中一个 list 转为字典，遍历另一个 列表，查询到字典中元素的最小 index 值
    
- 核心代码

	```python
    Aindex = {u: i for i, u in enumerate(A)}
    best, ans = 1e9, []

    for j, v in enumerate(B):
        i = Aindex.get(v, 1e9)
        if i + j < best:
            best = i + j
            ans = [v]
        elif i + j == best:
            ans.append(v)
    ```
    
#### **13. 字典中最长的单词**    

- 题目描述

	在字典中找到可以通过一个个单词拼写得到的最长单词
    
    ```python
    Example 1:

    Input:

    words = ["w","wo","wor","worl", "world"]

    Output: "world"

    Explanation:

    The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

    Example 2:

    Input:

    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

    Output: "apple"

    Explanation:

    Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
    ```
    
- 解题思路

	- 首先对所有的单词按长度进行排序，让短的单词出现在长的单词之前
	- 将单个字母加入 set
	- 每次遇到一个单词，就判断去掉最后一个字母的单词是否出现在 set 中
		- 如果出现了，就将这个单词加入 set，并更新最优
		- 否则，跳过

- 核心代码

	```python
    words = sorted(words)

    visited = set()
    res = ''

    for word in words:
        if len(word) == 1 or word[:-1] in visited:
            visited.add(word)
            if len(word) > len(res):
                res = word
    ```
    
#### **14. 快乐数字**

- 题目描述

	19 是一个快乐数字
   
	![](./img/happy.png)
    
    经过上述过程最终结果为 1 的为快乐数字
    
- 解题思路

	使用set 保存中间出现的结果(82....)
    
    如果结果不为1 且 已经出现则为 快乐数字
    
- 核心代码

	```python
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(x) **2 for x in str(n)])
    return n == 1
    ```

#### **15. 有效字谜**

- 题目描述

	如果两个字符串组成字母元素相同，则认为是有效字谜
    
- 解题思路

	使用字典进行统计
    
- 核心代码

	 ```python
     dic1, dic2 = {}, {}
     for item in s:
        dic1[item] = dic1.get(item, 0) + 1
     for item in t:
        dic2[item] = dic2.get(item, 0) + 1
     ```

#### **16. 查找字符串中的所有字谜**

- 题目描述

	给定一个单词模式和一个字符串，找到一个字符串中所有有效字符的起始index
    
    ```python
    Example 1:

    Input: s: "cbaebabacd" p: "abc"

    Output: [0, 6]

    Explanation:

    The substring with start index = 0 is "cba", which is an anagram of "abc".

    The substring with start index = 6 is "bac", which is an anagram of "abc".

    Example 2:

    Input: s: "abab" p: "ab"

    Output: [0, 1, 2]
    ```
    
- 解题思路

	- 建立 有效字谜 字典
	- 更新 len(p) - 1 的窗口的字符串，的有效字谜字典
	- 从 该位置开始 继续遍历 字符串，并更新 有效字谜字典，同时与 pattern 对比，更新结果
    
- 核心代码

	```python
    n, m = len(s), len(p)
    if n < m: return res
    phash, shash = [0]*123, [0]*123
    for x in p:
        phash[ord(x)] += 1
    for x in s[:m-1]:
        shash[ord(x)] += 1
    for i in range(m-1, n):
        shash[ord(s[i])] += 1
        if i-m >= 0:
            shash[ord(s[i-m])] -= 1
        if shash == phash:
            res.append(i - m + 1)
    ```
    
#### **17. 有效字谜分组**

- 题目描述

	将相同有效字谜的进行分组
    
    ```python
     Given: ["eat", "tea", "tan", "ate", "nat", "bat"],
     
     Return:

    [

    ["ate", "eat","tea"],

    ["nat","tan"],

    ["bat"]

    ]
    ```
    
- 解题思路

	字典 key 为 set ， value 为 list
    
- 核心代码

	```python
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    ```
    
#### **18. 按字母频率进行排序**

- 题目描述

	```python
    Example 1:

    Input: "tree"

    Output: "eert"

    Explanation:

    'e' appears twice while 'r' and 't' both appear once.

    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

    Example 2:

    Input: "cccaaa"

    Output: "cccaaa"

    Explanation:

    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.

    Note that "cacaca" is incorrect, as the same characters must be together.

    Example 3:

    Input: "Aabb"

    Output: "bbAa"

    Explanation:

    "bbaA" is also a valid answer, but "Aabb" is incorrect.

    Note that 'A' and 'a' are treated as two different characters.
    ```
    
- 解题思路

	   使用字典统计，然后排序按顺序输出
       
- 核心代码

	```python
    templst = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    result = ''

    for ele in templst:
        result += ele[0] * ele[1]

    return result
    ```
    
#### **19. 森林中的兔子**

- 题目描述

	提供一个 列表，列表中的元素是一种颜色的兔子说，除了自己以外其他与自己形同颜色的兔子的数量，根据所有兔子给出的数据，估计出兔子的最少数量
    
- 解题思路

	将 answers 中值相同的元素分为一组，对于每一组，计算出兔子的最少数量，然后将所有组的计算结果累加，就是最终的答案。
    
    如果某个兔子回答的数字是x，那么说明森林里共有x+1个相同颜色的兔子，我们最多允许x+1个兔子同时回答x个，一旦超过了x+1个兔子，那么就得再增加了x+1个新兔子了。统计相同答案的数量 cnt,分组的数量是从ceil(1.0 x cnt/key)计算出来的所以同一个key下所有这些子组的总数是ceil(1.0 * cnt/key) * key。   
    
- 核心代码

	```python
    C=Counter(answers)
    res=0
    print(C)
    for key,cnt in C.items():
        key+=1
        res+=ceil(1.0*cnt/key)*key
    ```
    
#### **20. 实现魔法字典**

- 题目描述

	实现一个带有buildDict, 以及 search方法的魔法字典。
   
   对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。
   
   对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
   
   ```python
    Example 1:

    Input: buildDict(["hello", "leetcode"]), Output: Null

    Input: search("hello"), Output: False

    Input: search("hhllo"), Output: True

    Input: search("hell"), Output: False

    Input: search("leetcoded"), Output: False
   ```
   
- 解题思路

	 对于每个单词，我们逐个将其中的字符替换成特殊字符，然后将所有替换后的结果加入到dict中。接下来对于要search的单词，我们也是逐个将其中的字符替换为特殊字符，然后在查找替换结果在dict中出现的次数。若这个次数大于这个单词本身在原始词表中出现的次数，那么说明至少有一个其他单词可以进行替换。
     
     其实就是针对 两个 字符串 替换的字符情形进行列举，如果有重合，且两个字符串不等则为有效转换
     
- 核心代码

	```python
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
    ```
     
#### **21. Brick Wall**

- 题目描述

	给定一个列表，表明墙砖的分割位置，画一条线，最少切割砖块，能够分开整个墙壁，计算 最少切割砖块数量
    
    ![](./img/bricks.png)
    
- 解题思路

	其实就是遍历列表，统计每个分割位置index有多少转块这里分割，找到最多的那个就可以了
    
- 核心代码

	```python
    d = collections.defaultdict(int)
    for line in wall:
        i = 0
        for brick in line[:-1]:
            i += brick
            d[i] += 1
    # print len(wall), d
    return len(wall) - max(d.values() + [0])
    ```
    
    
    