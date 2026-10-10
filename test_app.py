import unittest
from app import *

class RecommendationTests(unittest.TestCase):
    def setUp(self):self.r=Recommender([('a','x'),('b','x'),('b','y')])
    def test_seen_excluded(self):self.assertNotIn('x',[r['item'] for r in self.r.recommend('a')])
    def test_cold_start(self):self.assertEqual(self.r.recommend('new')[0]['item'],'x')
    def test_duplicate_interactions(self):self.assertEqual(Recommender([('a','x')]*3).popularity['x'],1)
    def test_no_items(self):self.assertEqual(Recommender([]).recommend('x'),[])
    def test_leakage_rejected(self):
        with self.assertRaises(ValueError):evaluate([('a','x')],{'a':['x']})

if __name__ == '__main__': unittest.main()
