# Doc-Gen

This tool is used to create sample documents based upon a reference JSON document.  For example, if we want to create 1000 fictucious documents based upon this document schema:

{
    'Name' : 'some random string',
    'Age' : some random integer
    'Salary' : some random float
}

`python3  doc-gen.py -s '{"Name":"string","Age":123,"Salary":0.0}'`

This will output the results to the console.

You can write the sample data to MongoDB by using the -c parameter to define the connection string, the -db parameter for database name and -col for collection as follows:

`python3 doc-gen.py -s '{"Name":"string","Age":123,"Salary":0.0}' -c "mongodb+srv://YOUR CONNECTION STRING GOES HERE" -db "Sample" -col "SampleCollection"`

You can omit the -s flag to write the default json sample schema.


