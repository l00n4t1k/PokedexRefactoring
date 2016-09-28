import re


class Formatter(object):

    @staticmethod
    def hash_stripper(the_list):
        res = []
        for datum in the_list:
            datum[0] = datum[0].strip('#')
            res.append(datum)
        return res

    @staticmethod
    def type_formatter(the_list):
        res = []
        for datum in the_list:
            if datum[2].find(' · ') == -1:
                datum.append('')
            else:
                tl = datum[2].split(' · ')
                datum[2] = tl[0]
                datum.append(tl[1])
            res.append(datum)
        return res

    def add_url(self, the_list, the_url):
        for datum in the_list:
            datum[1] = self.accent_remover(datum[1])
            if re.search('♀', datum[1]):
                datum[1] = 'Nidoran-f'
            elif re.search('♂', datum[1]):
                datum[1] = 'Nidoran-m'
            elif re.search('Farfetch\'d', datum[1]):
                datum[1] = 'Farfetchd'
            elif re.search('Mr. Mime', datum[1]):
                datum[1] = 'Mr-Mime'
            elif re.search('Mime Jr.', datum[1]):
                datum[1] = 'Mime-Jr'
            new_url = the_url + datum[1]
            datum.append(new_url)
        return the_list

    # duplicate code / speculative generality
    @staticmethod
    def comma_remover(i):
        p = re.compile(',')
        i = p.sub('/', i)
        return i

    @staticmethod
    def accent_remover(i):
        p = re.compile('é')
        i = p.sub('e', i)
        return i

    # duplicate code
    @staticmethod
    def height_imp_remover(i):
        n = re.search(r'\d*[.]\d*m', i)
        return n.group()

    @staticmethod
    def weight_imp_remover(i):
        n = re.search(r'\d*[.]\d* kg', i)
        return n.group()

    @staticmethod
    def get_gen(the_list, the_min, the_max):
        the_res = []
        for datum in the_list[the_min:the_max]:
            the_res.append(datum)
        return the_res

    @staticmethod
    def readability_formatter(the_list):
        res = []
        head = ['Number', 'Name', 'Type', '', 'Address', 'Species', 'Height',
                'Weight', 'Local Number(s)']
        the_list.insert(0, head)
        for datum in the_list:
            cur_line = str(datum[0]) + ', ' + str(datum[1]) + ', ' + \
                       str(datum[2])
            if datum[3] != '':
                cur_line += '/' + str(datum[3])
            cur_line += ', ' + str(datum[4]) + ', ' + str(datum[5]) + ', ' + \
                        str(datum[6]) + ', ' + str(datum[7])
            if re.search('—', datum[8]):
                cur_line += ', ' + ''
            else:
                cur_line += ', ' + str(datum[8])
            res.append(cur_line)
        return res
