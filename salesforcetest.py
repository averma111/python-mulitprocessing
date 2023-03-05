from simple_salesforce import Salesforce
from Auth  import *
import argparse
import pandas
import math
from collections import OrderedDict


sf = Salesforce(
    username=username, 
    password=password, 
    security_token=security_token,
    instance_url = instance_url
    )

#Insert new record
#sf.Contact.create({'FirstName':'Ashish','LastName': 'Verma', 'Email': 'example@example.com'}) 

#Get the record details
contact = sf.Contact.get('003Dm000003rcGPIAY')
contact_dict = dict(contact)
id = contact_dict['Id']
print(id)

#Update the record 
sf.Contact.update(id,{'LastName': 'Sharma', 'FirstName': 'Ashu'})

#Delete the record
sf.Contact.delete(id)

