# LSDM_PROJECT
## ARCHITECTURE
### Linux Ubuntu v16.04 LTS
## TOOLS
### Big Data Management
1. [MongoDB v3.4 Community Edition](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

2. [CouchBase v4.5.1 Community](https://developer.couchbase.com/documentation/server/4.5/getting-started/installing.html#story-h2-3)

  * Preprocess data
    * csv file separeted by comma
    * first field named "id"
  * [cbtransfer to import from csv](https://developer.couchbase.com/documentation/server/current/cli/cbtransfer-tool.html)
    * ``` ./cbtransfer [your_path]/comuniitaliani28062016.csv http://localhost:8091 -B default -u Administrator -p [password] ```
    * Go to /opt/couchbase/bin/ via terminal and run the upper code. We have to specify:
     * filepath of csv file
     * url of Couchbase server (with port number)
     * -B [bucket_name] to specify the bucket
     * Credentials to access the server
  * In the query panel of Couchbase we can create our INDEX
    * CREATE PRIMARY INDEX `default-primary-index` ON `default`

3. [MySQL v5.7](https://dev.mysql.com/doc/refman/5.7/en/)

### Information Integration
* [Talend Open Studio for Data Integration v6.4.1](http://it.talend.com/download/talend-open-studio#t4)

