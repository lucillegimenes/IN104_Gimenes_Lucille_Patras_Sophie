import marqueurs
import distance
import unittest


class TestMarqueurs(unittest.TestCase):

    def test_boolouverture(self):
        boulangerie=marqueurs.Commerce('Boulangerie','Nice',(8,4),'ouvert','velo')
        self.assertTrue(boulangerie.boolOuverture())
    def test_getDistance(self):
        boulangerie=marqueurs.Commerce('Boulangerie','Nice',(8,4),'ouvert','velo')
        jean=marqueurs.Individu('Jean','Nice',(1,1),22,'velo')
        result=boulangerie.getDistance(jean.position)
        self.assertEqual(10,result)
    def test_distance(self):
        boulangerie=marqueurs.Commerce('Boulangerie','Nice',(8,4),'ouvert','velo')
        jean=marqueurs.Individu('Jean','Nice',(1,1),82,'velo')
        self.assertFalse(distance(jean,boulangerie))
    def test_getId(self):
        jean=marqueurs.Individu('Jean','Nice',(1,1),22,'velo')
        result=jean.getId
        self.assertEqual(result,'Jean')
      
if __name__ == "__main__":
    unittest.main()
