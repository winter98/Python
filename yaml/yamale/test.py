import yamale

data = yamale.make_data(content="""
name: Bill
age: 26
height: 6.2
awesome: True
""")

try:
    yamale.validate(schema, data)
    print('Validation success! 👍')
except ValueError as e:
    print('Validation failed!\n%s' % str(e))
    exit(1)

