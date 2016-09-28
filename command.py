from cmd import Cmd


class Command(Cmd):
    """
    command line interface
    """
    intro = 'Enter a command or type "help" for a list of commands'
    prompt = '(> >_< <)'
    my_controller = None
    my_scraper = None
    my_formatter = None
    my_IO = None
    __gen = 0
    __filepath = None

    def set__gen(self, the_gen):
        self.__gen = the_gen

    def get__gen(self):
        return self.__gen

    def do_set_filepath(self, is_load):
        if is_load:
            self.__filepath = input("Enter the path to the folder your file is"
                                    " stored: ")
        else:
            self.__filepath = input("Enter the path to the folder you wish to "
                                    "store the file in: ")
        print("Saving scrape to " + self.__filepath)

    def __init__(self, the_controller):
        super(Command, self).__init__()
        self.my_controller = the_controller
        self.my_scraper = self.my_controller.get_scraper()
        self.my_IO = self.my_controller.get_io()
        self.my_formatter = self.my_controller.my_scraper.get_formatter()

    def do_new_scrape(self, line):
        """
        Perform a fresh web scrape of the entire pokedex
        """
        if self.__filepath is None:
            self.do_set_filepath(False)

        file_name = input("Enter the name to save the file as: ")
        self.my_scraper.set_generation(0)
        dex = self.my_scraper.web_scraper()
        self.my_controller.set_full_dex(dex)
        self.my_IO.pickler(self.my_controller.get_full_dex(),
                           self.__filepath, file_name)

    def do_load(self, line):
        """
        Loads a pickled instance of a full national pokedex (all 721 Pokemon
        from the 6 generations)
        """
        file_name = input("Enter the name of the pickled file to load: ")
        if self.__filepath is None:
            self.do_set_filepath(True)
        try:
            self.my_scraper.set_nat_dex(self.my_IO.load(self.__filepath,
                                                        file_name))
        except FileNotFoundError:
            res = input('File not found. Would you like to perform a fresh '
                        'scrape "Y or N" ? ')
            if res.upper() == 'Y':
                self.do_new_scrape()
        # print(self.my_scraper.get_nat_dex())

    def do_get_local_dex(self, line):
        """
        Creates a list of all the Pokemon from the entered generation
        """
        self.__gen = input("Enter the generation number you want to search "
                           "for: ")
        self.my_scraper.find_local_dex(self.__gen)

    def do_print_nat(self, line):
        """
        Prints the full national Pokedex of 721 Pokemon
        """
        self.my_IO.printer(0, self.my_formatter.readability_formatter(
            self.my_scraper.get_nat_dex()))

    def do_print_local(self, line):
        """
        Prints the selected local Pokedex
        """
        self.my_IO.printer(self.__gen, self.my_formatter.readability_formatter(
            self.my_scraper.get_local_dex()))

    @staticmethod
    def do_quit(line):
        """
        Exit the Program
        """
        print("Exiting.")
        return True

    do_q = do_quit
    do_printLocal = do_print_local
    do_printNat = do_print_nat
    do_getLocal = do_get_local_dex
    do_new = do_new_scrape
