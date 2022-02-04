# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

from pydoc import doc
import random
from random import seed
from random import randint
import argparse
import time
import pymongo
import json
import string

def getValue(sample_type):
    if isinstance(sample_type,int) == True:
        return random.randint(-1000, 1000);
    if isinstance(sample_type,str) == True:
        letters = string.ascii_lowercase
        return ( ''.join(random.choice(letters) for i in range(20)) )
    if isinstance(sample_type,float) == True:
        return random.uniform(-1000.0, 1000.0)

    return 0

def checkmongodbconnection():
    try:
        c = pymongo.MongoClient(MONGO_URI)
        c.admin.command('ismaster')
        time.sleep(2)
        c.close()
        return True
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print('Could not connect to server: %s',e)
        return False

def main():

    global MONGO_URI
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--total", type=int, default=100,help="number of documents to create")
    parser.add_argument("-c","--connection", default='none', help="MongoDB connection string, omit to write to console")
    parser.add_argument("-db","--database", default='SampleDB', help="MongoDB database")
    parser.add_argument("-col","--collection", default='SampleCollection', help="MongoDB collection")
    parser.add_argument("-f","--file", default='none',help="load sample document from file")
    parser.add_argument("-s","--sample", default='none',help="sample document from JSON string")

    args = parser.parse_args()

    print('\nDoc-gen [Document Generation Tool] V1.0\n\n')

    SAMPLE_DOCUMENT=""
    if args.connection != 'none' :
        MONGO_URI=args.connection
        while True:
            print('Checking MongoDB Connection')
            if checkmongodbconnection()==False:
                print('Problem connecting to MongoDB, sleeping 10 seconds')
                time.sleep(10)
            else:
                break
        cxn = pymongo.MongoClient(MONGO_URI)
        cxdb = cxn.get_database(name=args.database)
        print('Successfully connected to MongoDB\nWriting to ' + args.database + '.' + args.collection + '\n')

    if args.file == 'none' and args.sample == 'none':
        print('Default sample schema to be used.')
        SAMPLE_DOCUMENT={"Name":"Name","Favorite Number":123, "Extra Field":"test"}
    if args.file != 'none':
        f = open(args.file)
        SAMPLE_DOCUMENT=json.load(f)
    if args.file == 'none' and args.sample != 'none': SAMPLE_DOCUMENT=json.loads(args.sample)
    
    print('Generating {0} documents based upon schema:'.format(args.total))

    for key in SAMPLE_DOCUMENT:
        print(key, '->', type(SAMPLE_DOCUMENT[key]))

    start = time.time()
    
    for x in range(0, args.total):
        document={}
        for key in SAMPLE_DOCUMENT:
            document[key]=getValue(SAMPLE_DOCUMENT[key])
        if args.connection=='none': print(document)
        else:
            result=cxdb[args.collection].insert_one(document)
            if x % 100 == 0:
                print('\n{0} documents written.'.format(x+100))
    elapsed = time.time()-start
    print("\nTime to complete: " + time.strftime("%H:%M:%S.{}".format(str(elapsed % 1)[2:])[:11], time.gmtime(elapsed)))


main()