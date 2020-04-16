import marqueurs
import distance
import unittest

class TestMarqueurs(unittest.TestCase):
    boulangerie=Commerce('Boulangerie','Nice',(8,4),'ouvert','velo')
    jean=Individu('Jean','Nice',(1,1),22,'velo')

    def test_boolouverture(self):
        result=boulangerie.boolOuverture()
        self.assertTrue(result)
    def test_getDistance(self):
        result=boulangerie.getDistance(jean.position)
        self.assertEqual(10,result)
    def test_distance(self):
        result=distance(jean,boulangerie)
        self.assertTrue(result)
    def test_getId(self):
        result=jean.getId
        self.assertEqual(result,jean.idt)
      
if __name__ == "__main__":
    unittest.main()
