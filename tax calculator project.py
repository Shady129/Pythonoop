class Taxes:
    #Class constructor that set taxes percentage.
    def __init__ (self, PersonalPersentages, SMPersentage,LargePercentage ):
        self.PersonalPersentages = PersonalPersentages
        self.SMPersentage = SMPersentage
        self.LargePercentage = LargePercentage

    #Class method that calculate taxes for persons.
    def individuals(self, value):
        resutlt = value * self.PersonalPersentages
        return f"Amount: {self.PersonalPersentages} DHS, \n"\
               f"Tax = {self.PersonalPersentages * 100} % {resutlt} DHS,\nTotal amount after tax: {value - resutlt} DHS"
    

    #Class method that calculate taxes for small and medium sized companies
    def small_and_medium_sized_companies(self, value):
        result = value * self.SMPersentage
        return f"Amount: {self.SMPersentage} DHS \n"\
        f"Tax = {self.SMPersentage*100} % {result} DHS\nTotal amount after tax: {value - result} DHS"


    
    #Class method that calculate taxes for large sized companies
    def large_companies(self, value):
        result = value * self.LargePercentage
        return f"Amount: {self.LargePercentage} DHS \n"\
        f"Tax = {self.LargePercentage*100} % {result} DHS\nTotal amount after tax: {value - result} DHS"
    



#Create instance
tax = Taxes(0.05, 0.10, 0.15)
#Calculate personal tax
person = tax.individuals(3000)
#Calculate small and medium tax
smcompanies = tax.small_and_medium_sized_companies(5000)
#Calculate large tax
lcompaines = tax.large_companies(10000)


#print taxes
print(person)
print(smcompanies)
print(lcompaines)



