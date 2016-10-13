from scraper import Scraper
from bs4 import BeautifulSoup
import requests


class PokemonScraper(Scraper):

    __my_controller = None
    __max = 0
    __min = 0
    __nat_dex = []
    __local_dex = []
    __generation = 0
    __the_url = 'http://pokemondb.net/pokedex/'

    def __init__(self, the_formatter):
        self.__my_formatter = the_formatter

    def gen_decider(self):
        gen = self.get_generation()
        if gen == 1:
            self.__min = 0
            self.__max = 151
        elif gen == 2:
            self.__min = 151
            self.__max = 251
        elif gen == 3:
            self.__min = 251
            self.__max = 386
        elif gen == 4:
            self.__min = 386
            self.__max = 493
        elif gen == 5:
            self.__min = 493
            self.__max = 649
        elif gen == 6:
            self.__min = 649
            self.__max = 722
        elif gen == 0:
            self.__min = 0
            self.__max = 722

    def set_url(self, new_url):
        self.__the_url = new_url

    def get_url(self):
        return self.__the_url

    def set_nat_dex(self, the_dex):
        self.__nat_dex = the_dex

    def get_nat_dex(self):
        return self.__nat_dex

    def set_local_dex(self, the_dex):
        self.__local_dex = the_dex

    def get_local_dex(self):
        return self.__local_dex

    def set_generation(self, the_gen):
        self.__generation = the_gen
        self.gen_decider()

    def get_generation(self):
        return self.__generation

    def get_min(self):
        return self.__min

    def get_max(self):
        return self.__max

    def get_formatter(self):
        return self.__my_formatter

    # def print(self, the_gen, the_list):
    #     self.__my_printer.printer(the_gen, the_list)

    # long method
    def web_scraper(self):
        print('Scraping Main')
        dex_data = []
        r = requests.get(self.get_url() + 'national').text
        soup = BeautifulSoup(r, 'html.parser')
        table = soup.find('div', attrs={'class': 'infocard-tall-list'})
        cards = table.find_all('span')
        c = 0
        for i in range(0, 1):  # <---
            for card in cards[self.__min:self.__max]:
                stuffs = card.find_all(['a', 'small'])
                if c < 1:
                    dex_data.append([stuff.text for stuff in stuffs[1:4]])
                    c += 1
        dex_data = self.format_dex(dex_data)
        self.set_nat_dex(dex_data)
        # print(self.get_nat_dex())

    def scrape_additional(self, the_list):
        print('Scraping additional')
        for datum in the_list:
            url = datum[4]
            print(datum[1])
            r = requests.get(url).text
            soup = BeautifulSoup(r, 'html.parser')
            vt = soup.find('table', attrs={'class': 'vitals-table'})
            rows = vt.find_all('td')

            indi = [row.text for row in rows]
            # print(indi)

            datum.append(self.__my_formatter.accent_remover(indi[2]))
            datum.append(self.__my_formatter.imp_remover(indi[3], 'm'))
            datum.append(self.__my_formatter.imp_remover(indi[4], ' kg'))
            datum.append(self.__my_formatter.comma_remover(indi[6]))
            # print(datum)
        return the_list

    def format_dex(self, the_dex):
        dex_data = self.__my_formatter.hash_stripper(the_dex)
        dex_data = self.__my_formatter.type_formatter(dex_data)
        dex_data = self.__my_formatter.add_url(self.get_formatter(), dex_data,
                                               self.get_url())
        dex_data = self.__my_formatter.get_gen(
            dex_data, self.__min, self.__max)
        dex_data = self.scrape_additional(dex_data)
        return dex_data

    def find_local_dex(self, the_gen):
        self.set_generation(int(the_gen))
        res = []
        for i in self.get_nat_dex():
            if int(i[0]) <= self.__max:
                if int(i[0]) > self.__min:
                    res.append(i)
            else:
                break
        self.set_local_dex(res)
