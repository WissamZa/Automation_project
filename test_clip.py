import unittest
import multi_clipboard as mc

class Testclip(unittest.TestCase):
    def test_add(self):
        op=mc.multi_clip()
        self.assertEqual(op.clipsave(), 'assertEqual')

if __name__=='__main__':
    unittest.main()