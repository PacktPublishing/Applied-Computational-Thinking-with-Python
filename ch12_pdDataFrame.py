import pandas as pd

myAddressBook = {'names': ['Susan', 'Malena', 'Isabel', 'Juan', 'Mike'],
                 'phoneNumbers':['333-333-3333', '444-444-4444', '555-555-5555',
                                 '777-777-7777', '888-888-8888']}
addressBook = pd.DataFrame(myAddressBook)
print(addressBook)
