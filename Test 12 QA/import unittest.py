import unittest
from StairsAndSnakes import *

class boardTesting(unittest.TestCase):

    def test1_snakesConstruct(self):
        heads = [22, 24, 19, 14]
        tails = [20, 16, 8, 4]
        t1 = snakesConstruct(heads, tails)
        self.assertEqual(t1[0], heads, 'the constructions of the snakes heads is wrong')
    
    def test2_snakesConstruct(self):
        heads = [22, 24, 19, 14]
        tails = [20, 16, 8, 4]
        t1 = snakesConstruct(heads, tails)
        self.assertEqual(t1[1], tails, 'the constructions of the snakes tails is wrong')
    
    def test1_checkStairs(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        pos = -12
        turn = 9
        t1, t2 = checkStairs(stairs, pos, turn)
        self.assertGreater(t1, 1, 'the position is less than 1')
    
    def test2_checkStairs(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        pos = 5
        turn = -4
        t1, t2 = checkStairs(stairs, pos, turn)
        self.assertGreater(t2, 1, 'the turn is less than 1')

    def test3_checkStairs(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        pos = 10
        turn = 9
        t1, t2 = checkStairs(stairs, pos, turn)
        self.assertEqual(t1, 12, 'the position is wrong')   
    
    def test4_checkStairs(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        pos = 12
        turn = 9
        t1, t2 = checkStairs(stairs, pos, turn)
        self.assertEqual(t1, 12, 'the position is wrong')
    
    def test1_checkSnakes(self):
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = -12
        turn = 9
        t1, t2 = checkSnakes(snakes, pos, turn)
        self.assertGreater(t1, 1, 'the position is less than 1')
    
    def test2_checkSnakes(self):
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = 5
        turn = -4
        t1, t2 = checkSnakes(snakes, pos, turn)
        self.assertGreater(t2, 1, 'the turn is less than 1')

    def test3_checkSnakes(self):
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = 22
        turn = 9
        t1, t2 = checkSnakes(snakes, pos, turn)
        self.assertEqual(t1, 20, 'the position is wrong')   
    
    def test4_checkSnakes(self):
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = 20
        turn = 9
        t1, t2 = checkSnakes(snakes, pos, turn)
        self.assertEqual(t1, 20, 'the position is wrong')
    
    def test1_check(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = 9
        turn = 12
        t1, t2 = check(stairs, snakes, pos, turn)
        self.assertEqual(t1, 12, 'the position is wrong')
    
    def test2_check(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = 9
        turn = 12
        t1, t2 = check(stairs, snakes, pos, turn)
        self.assertEqual(t1, 12, 'the position is wrong')
    
    def test3_check(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = 9
        turn = 12
        t1, t2 = check(stairs, snakes, pos, turn)
        self.assertEqual(t2, 13, 'the turn is wrong')
    
    def test4_check(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = -4
        turn = 12
        t1, t2 = check(stairs, snakes, pos, turn)
        self.assertGreater(t1, 1, 'the position is less than 1')
    
    def test5_check(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        pos = 9
        turn = -5
        t1, t2 = check(stairs, snakes, pos, turn)
        self.assertGreater(t2, 1, 'the turn is less than 1')

    def test1_play(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        t1 = play(stairs, snakes)
        self.assertEqual(t1, 0, 'the execution was not correct')
    
    def test1_game(self):
        stairs = [[10, 9, 6, 3], [12, 18, 17, 11]]
        snakes = [[22, 24, 19, 14], [20, 16, 8, 4]]
        t1 = game()
        self.assertEqual(t1, 0, 'the execution was not correct')

if __name__ == '__main__':
    unittest.main()