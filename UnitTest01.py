import unittest
from program_main import Main
from pokemon_scraper import PokemonScraper
from command import Command
from controller import Controller
from formatter import Formatter
from IO import IO


class TestScraper(unittest.TestCase):

    def setUp(self):
        self.m = Main()
        self.m.go_test()
        self.my_scraper = self.m.my_scraper
        self.my_formatter = self.my_scraper.get_formatter()
        self.c = self.m.my_cmd

    def test_hash_stripper_pokemon(self):
        the_list = [["#Pokemon"]]
        output = Formatter.hash_stripper(the_list)
        self.assertEqual(output, [["Pokemon"]])

    def test_type_formatter_bulbasaur(self):
        the_list = [['001', 'Bulbasaur', 'Grass · Poison',
                     'http://pokemondb.net/pokedex/Bulbasaur', 'Seed Pokemon',
                     '0.71m', '6.9 kg', '001 (Red/Blue/Yellow/FireRed/LeafGr'
                     'een)226 (Gold/Silver/Crystal)231'
                                        '(HeartGold/SoulSilver)080 (X/Y)']]
        output = Formatter.type_formatter(the_list)
        self.assertEqual(output[0][2], "Grass")

    def test_add_url_bulbasaur(self):
        the_list = [['#001', 'Bulbasaur', 'Grass · Poison']]
        the_url = 'http://pokemondb.net/pokedex/'
        output = self.my_formatter.add_url(self.my_formatter,
                                           the_list, the_url)
        self.assertEqual(output[0][3], 'http://pokemondb.net/pokedex/'
                                       'Bulbasaur')

    def test_comma_remover(self):
        the_string = 'hello, world!'
        output = self.my_formatter.comma_remover(the_string)
        self.assertEqual(output, 'hello/ world!')

    def test_accent_remover_pokemon(self):
        output = Formatter.accent_remover("Pokémon")
        self.assertEqual(output, "Pokemon")

    def test_weight_form_bulbasaur(self):
        output = self.my_formatter.height_imp_remover('2′4″ (0.71m)')
        self.assertEqual(output, '0.71m')

    def test_height_form_bulbasaur(self):
        output = self.my_formatter.weight_imp_remover('15.2 lbs (6.9 kg)')
        self.assertEqual(output, '6.9 kg')

    def test_readability_form_bulbasaur(self):
        test_data = ['001', 'Bulbasaur', 'Grass', 'Poison',
                     'http://pokemondb.net/pokedex/Bulbasaur', 'Seed Pokemon',
                     '0.71m', '6.9 kg', '001 (Red/Blue/Yellow/FireRed/'
                                        'LeafGreen)226 '
                                        '(Gold/Silver/Crystal)231 '
                                        '(HeartGold/SoulSilver)080 (X/Y)']
        output = self.my_formatter.readability_formatter([test_data])
        test_out = '001, Bulbasaur, Grass/Poison, ' \
                   'http://pokemondb.net/pokedex/Bulbasaur, Seed Pokemon, ' \
                   '0.71m, 6.9 kg, 001 (Red/Blue/Yellow/FireRed/LeafGreen)' \
                   '226 (Gold/Silver/Crystal)231' \
                   ' (HeartGold/SoulSilver)080 (X/Y)'
        self.assertEqual(output[1], test_out)

    def test_newScrape_comma_remover(self):
        expected = [['001', 'Bulbasaur', 'Grass', 'Poison',
                    'http://pokemondb.net/pokedex/Bulbasaur', 'Seed Pokemon',
                    '0.71m', '6.9 kg', '001 (Red/Blue/Yellow/FireRed/'
                                       'LeafGreen)226 (Gold/Silver/Crystal)231'
                                       ' (HeartGold/SoulSilver)080 (X/Y)']]
        self.my_scraper.set_generation(0)
        self.my_scraper.web_scraper()
        actual = self.my_scraper.get_nat_dex()
        self.assertEqual(expected, actual)

    # def test_newScrape_wo_comma_remover(self):
    #     expected = [['001', 'Bulbasaur', 'Grass', 'Poison',
    #                 'http://pokemondb.net/pokedex/Bulbasaur', 'Seed Pokemon',
    #                 '0.71m', '6.9 kg', '001 (Red,Blue,Yellow,FireRed,'
    #                                    'LeafGreen)226 (Gold,'
    #                                                    Silver,Crystal)231'
    #                                    ' (HeartGold,SoulSilver)080 (X,Y)']]
    #     self.my_scraper.set_generation(0)
    #     self.my_scraper.web_scraper()
    #     actual = self.my_scraper.get_nat_dex()
    #     self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
