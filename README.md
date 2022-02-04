# Doc-Gen

This tool is used to create sample documents based upon a reference JSON document passed as a string on the command line or within a JSON file.  For example, if we want to create 100 fictucious documents based upon this document schema:

{
    'Name' : 'some random string',
    'Age' : some random integer
    'Salary' : some random float
}

`python3  doc-gen.py -s '{"Name":"string","Age":123,"Salary":0.0}'`

This will output 100 documents with the schema above to the console.

You can write the sample data to MongoDB by using the -c parameter to define the connection string, the -db parameter for database name and -col for collection as follows:

`python3 doc-gen.py -s '{"Name":"string","Age":123,"Salary":0.0}' -c "mongodb+srv://YOUR CONNECTION STRING GOES HERE" -db "Sample" -col "SampleCollection"`

You can omit the -s flag to write the default json sample schema.

## Command Line Arguments:
|Flag | Description |
|---|---|
|-h| show help|
|-t| Total number of samples to create, default=100|
|-c| MongoDB Connection string, omit to write samples to console |
|-db| Database to write samples |
|-col| Collection to write samples |
|-f| JSON file to load the example schema|
|-s| JSON sample provided as a string |

