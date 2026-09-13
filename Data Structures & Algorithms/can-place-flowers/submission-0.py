class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0]

        for i in range(1, len(flowers) - 1):
            if flowers[i -  1] == 0 and flowers[i] == 0 and flowers[i + 1] == 0:
                flowers[i] = 1
                n -= 1

        return n <= 0