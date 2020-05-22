from Company import *


class Listing:
    """
    Create a Listing class containing compiled data from multiple Company classes.
    """

    def __init__(self, countryFile, companyFile):
        """
        create Listing using input files.
        creates dictionary object mapping company name to country from input countryFile.
        creates list object containing Company types from input companyFile.

        :param countryFile: name of *.txt file containing a company and country on each line (str)
            Example format: '3 Round Stones, Inc.|United States'
        :param companyFile: name of *.txt file containing company and its details on each line (str)
            Example format: '3 Round Stones, Inc.|Data/Technology|United States|17|2010'
        """
        # define countries object as dictionary mapping company name to country according to countryFile input.
        self.countries = {}
        try:
            file1 = open(countryFile, 'r', encoding='utf8')
            country_list = file1.readlines()
            file1.close()

            # take each line from countryFile, split by '|' character, and add to dict.
            for entry in country_list:
                entry = entry.strip()
                company, country = entry.split('|')
                self.countries[company] = country

        except IOError:
            print("Country file not found.")

        # define companies object as list containing all Companies in companyFile input.
        self.companies = []
        try:
            file2 = open(companyFile, 'r', encoding='utf8')
            company_details_list = file2.readlines()
            file2.close()

            # take each line from companyFile split by '|' character, create new Company and append to list.
            for entry in company_details_list:
                name, category, country, num_employees, year_founded = entry.split('|')
                new_entry = Company(name, category, country, num_employees, year_founded)
                self.companies.append(new_entry)

        except IOError:
            print("Company file not found.")

    # PART 1
    def __iter__(self):
        """
        establish starting Listing iterator as 0 index and maximum number of steps possible.

        :return: self (Listing)
        """
        self.max = len(self.companies) - 1
        self.index = 0

        return self

    def __next__(self):
        """
        stops iterator when last item reached, otherwise moves onto next item index in Listing.

        :return: next company iteration in Listing (Company)
        """
        if self.index <= self.max:
            next_iter = self.companies[self.index]
            self.index += 1
            return next_iter
        else:
            raise StopIteration

    def __str__(self):
        """
        create a string format for Listing class.

        :return: listed string values separated by '\n' (str)
            Example format: 'Wolfram Research in Data/Technology sector based in United States\n' \
                            'CitySourced in Governance sector based in United States\n'
        """
        strings = []
        for company in self.companies:
            strings.append(str(company))

        return "\n".join(strings) + "\n"

    # PART 2
    def addCountry(self, company_name, country):
        """
        adds new entry to countries dictionary mapping company name to corresponding country.

        :param company_name: name of company to be added (str)
        :param country: country of origin of company to be added (str)
        :return: None
        """
        self.countries[company_name] = country

    def addCompany(self, company_name, category, num_employees, year_founded):
        """
        adds new Company entry to companies list.
        fails if company name already exists in Listing or if country not found in countries dictionary.

        :param company_name: name of company to be added (str)
        :param category: category of company to be added (str)
        :param num_employees: number of people employed at company to be added (int)
        :param year_founded: year company to be added was founded (int)
        :return: None
        """
        does_exist = False
        for entry in self.companies:
            if entry.name == company_name:
                does_exist = True

        has_country = False
        if company_name in self.countries.keys():
            has_country = True

        if does_exist:
            raise ValueError("This company is already in the listing.")
        elif not has_country:
            raise ValueError("Country information unavailable for this company.\n"
                             "Try first adding this company and country to the country list of this listing.")
        else:
            new_entry = Company(
                company_name,
                category,
                self.countries[company_name],
                num_employees,
                year_founded)
            self.companies.append(new_entry)

    # PART 3
    def removeCompany(self, company_name):
        """
        removes Company entry from Listing according to name of company from input parameter.
        fails if Company does not exist in Listing.

        :param company_name: name of desired company to be removed. (str)
        :return: None
        """

        removed_company = None
        for company in self.companies:
            if company.name == company_name:
                removed_company = company

        if removed_company is None:
            raise ValueError("Company not in list. Nothing was removed.")
        else:
            self.companies.remove(removed_company)

    # PART 4
    def companyDetails(self, company_name):
        """
        returns details of Company within Listing according to company name input parameter.
        fails if Company does not exist in Listing.

        :param company_name: name of company for details to be generated. (str)
        :return: details of company. (str)
            Example format: '3 Round Stones, Inc. in Data/Technology sector based in United States'
        """
        company_details = None
        for company in self.companies:
            if company.name == company_name:
                company_details = company

        if company_details is None:
            return str(company_name) + " is not in the listing."
        else:
            return company_details

    # PART 5
    def filterByCountry(self, country):
        """
        prints all companies and their corresponding details situated in the country specified.

        :param country: country in which all company details will be printed. (str)
        :return: None
        """
        filter_result = []
        for company in self.companies:
            if company.country == country:
                filter_result.append(str(company))

        print("\n".join(filter_result))

    # PART 6
    def saveListing(self, fname):
        """
        saves Listing to file, overwriting any existing file with the same name.

        :param fname: desired name of output file *.txt (str)
        :return: None
        """
        # creates fresh copy of file first, replacing any existing one.
        file = open(fname, 'w')
        file.close()

        for company in self.companies:
            company.save(fname)

    # PART 7
    def largestCompany(self, country):
        """
        computes the largest company in a given country according to number of employees.

        :param country: the country in which the largest company should be searched. (str)
        :return: description of largest company in given country including size and age. (str)
            Example format: 'Moody's Analytics is the largest company in Mexico.\n' \
                            'It has grown to a size of 2294 employees in 115 years.'
        """
        largest_company = Company('Placeholder', None, None, 0, 0)
        for company in self.companies:
            if company.country == country and company.num_employees > largest_company.num_employees:
                largest_company = company

        return "{0} is the largest company in {1}.\n" \
               "It has grown to a size of {2} employees in {3} years.\n".format(
                    largest_company.name,
                    largest_company.country,
                    largest_company.num_employees,
                    largest_company.getAge())
