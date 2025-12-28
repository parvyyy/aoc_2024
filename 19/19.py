
from typing import List


def Part1(blocks: List[str], words: List[str]):
    dp: dict[str, bool] = dict()
    blocks: set[str] = set(blocks)

    for block in blocks:
        dp[block] = True

    def search(dp: dict[str, bool], word: str):
        if word in dp:
            return True
        
        # From the end of the word, break it into
        # a partial word and a block. Then, recursively
        # search for the partial word.
        #
        # Recursion Relation
        # search(<word>) = search(<partial>) + <block>
        n = len(word)
        block_candidate = ''
        for i in range(n):
            block_candidate = word[n - 1 - i] + block_candidate

            if block_candidate in blocks:
                partial = word[:n - 1 - i]
                res = search(dp, partial)

                # Cache the result
                dp[partial] = res

                # Explore the next [partial] + [block]
                # if the search was `False`
                if res:
                    return True

        return False

    total = 0
    for word in words:
        total += search(dp, word)
    
    return total

def Part2(blocks: List[str], words: List[str]):
    dp: dict[str, int] = dict()
    blocks: set[str] = set(blocks)

    def search(dp: dict[str, bool], word: str) -> int:
        if word in dp:
            return dp[word]
        
        n = len(word)
        block_candidate = ''
        
        summ = 0
        for i in range(n):
            block_candidate = word[n - 1 - i] + block_candidate

            if block_candidate in blocks:
                partial = word[:n - 1 - i]
                res = search(dp, partial)

                # Cache the result
                dp[partial] = res

                # Explore the next [partial] + [block]
                # if the search was `False`

                summ += res

        return summ

    # Cannot naively set each `block` to 1.
    # This is as blocks like `bg` maybe able to be made
    # from smaller blocks (i.e. `b` + `g`) and hence
    # should account for multiple solutions.
    for block in sorted(blocks, key = lambda x: len(x)):
        num = 1 + search(dp, block)
        dp[block] = num

    total = 0
    for word in words:
        num_found = search(dp, word)

        total += num_found
    
    return total


with open("input.txt", 'r') as fp:#
    data = fp.read()
    blocks, words = data.split('\n\n')

    blocks = blocks.split(',')
    blocks = [b.strip() for b in blocks]

    words = words.split('\n')

    #290
    ans1 = Part1(blocks, words)
    print(ans1)

    # 712058625427487
    ans2 = Part2(blocks, words)
    print(ans2)