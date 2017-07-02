'''
12-6. Extended Import. Create a new function called importAs(). This function will import a
module into your namespace, but with a name you specify, not its original name. For
example, calling newname=importAs ('mymodule') will import the module mymodule, but
the module and all its elements are accessible only as newname or newname.attr. This is
the exact functionality provided by the new extended import syntax introduced in
Python 2.0.
'''

def importAs(module_name):
    return __import__(module_name)


syst = importAs('os')
print('cpu count', syst.cpu_count())