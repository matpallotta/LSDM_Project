# LSDM_PROJECT
## ARCHITECTURE
### Linux Ubuntu v16.04 LTS
## TOOLS
### Big Data Management
1. [MongoDB v3.4](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
  * [mongoimport for csv](https://docs.mongodb.com/manual/reference/program/mongoimport/#csv-import)
  * ``` mongoimport --db motorizzazione --collection parco_circolante --type csv --headerline --file parco_circolante_aggregated.csv --ignoreBlanks ```
2. [CouchBase v4.5.1 Community](https://developer.couchbase.com/documentation/server/4.5/getting-started/installing.html#story-h2-3)
  * [cbtransfer to import from csv](https://developer.couchbase.com/documentation/server/current/cli/cbtransfer-tool.html)
  * ``` ./cbtransfer /home/ubuntumat/Desktop/LargeScaleProject/Dataset/comuniitaliani28062016.csv http://localhost:8091 -B default -u Administrator -p [password] ```
  * Go to /opt/couchbase/bin/ via terminal and run the upper code. We have to specify:
    * filepath of csv file
    * url of Couchbase server (with port number)
    * -B [bucket_name] to specify the bucket
    * Credentials to access the server
  * In the query panel of Couchbase we can create our INDEX
    * CREATE PRIMARY INDEX `default-primary-index` ON `default`

