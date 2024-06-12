class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = [0]*len(deck)
        deck.sort()
        skipped = 1
        index = 0
        
        while deck:
            if skipped == 1 and result[index] == 0:
                result[index] = deck.pop(0)
                skipped = 0
            elif result[index] == 0:
                skipped = 1

            if index == len(result)-1:
                index = 0
            else:
                index += 1

        return result