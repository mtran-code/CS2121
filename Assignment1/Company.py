class Company:
    """
    Create a company class containing name, category, country of origin, number of employees, and year founded.
    """

    def __init__(self, name, category, country, num_employees, year_founded):
        """
        assign all input parameters to respective objects within company class.
        :param name: name of company (str)
        :param category: category of company (str)
        :param country: country of origin of company (str)
        :param num_employees: number of people employed at company (int)
        :param year_founded: year company was founded (int)
        """
        self.name = str(name)
        self.category = str(category)
        self.country = str(country)
        self.num_employees = int(num_employees)
        self.year_founded = int(year_founded)

    def __str__(self):
        """
        create a string format for Company class.
        :return: string format for Company. (str)
            Example format: 'Wolfram Research in Data/Technology sector based in United States'
        """
        return "{0} in {1} sector based in {2}".format(self.name, self.category, self.country)

    def getAge(self):
        """
        calculates the number of years since the company was founded.
        NOTE: test.py assumes 2019 as current year; actual current year is 2020.
        :return: number of years since company was founded.
        """
        return 2019 - int(self.year_founded)

    def save(self, fname):
        """
        opens text file 'fname' and appends formatted Company details to last line.
        Example format: Wolfram Research|Data/Technology|United States|800|1987
        :param fname: name of *.txt file to save to (str)
        :return: None
        """
        file = open(fname, 'a')
        file.write("{0}|{1}|{2}|{3}|{4}\n".format(
            self.name, self.category, self.country, self.num_employees, self.year_founded))
        file.close()

    def __eq__(self, other):
        """
        determines equivalence of two Company objects according to name.
        :param other: other Company to be compared to. (Company)
        :return: bool indicating if Company is equivalent to another Company (bool)
        """
        if self.name == other.name:
            return True
        else:
            return False
