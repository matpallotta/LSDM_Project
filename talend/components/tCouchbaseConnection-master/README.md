tCouchbaseConnection
====================

tCouchbaseConnection is a Talend component which enables you to interact with a [Couchbase Server](http://www.talend.com/products/open-studio-di.php) cluster from [Talend Open Studio](http://www.talend.com/products/open-studio-di.php).
This component is compatible with both Couchbase Server 1.8 and 2.0.

How To Use it
==============

Basic Settings
---------------
Fill out required information to connect to a Couchbase Server cluster :

- URIs: A list of URIs to bootstrap a Couchbase client, you have to specify at least one URI to get Couchbase Server cluster information and connect. If you specify different servers' URI within the same cluster, you'll get higher availability and be able to interact with the database even one of servers goes down.
- Bucket Name: Specify the bucket to connect.
- Username: Specify the SASL authentication username if needed.
- Password: Specify the SASL authentication password if needed. 

Interact with a couchbase cluster
------------------------------------------------------
This component does nothing more than holding a connection to the database. 
To extract/input data, please refer to tCouchbaseBulk, tCouchbaseInput and tCouchbaseOutput.
This component has to be set up before any tCouchbaseBulk, tCouchbaseInput and tCouchbaseOutput components. Use the "OnSubjobOK" trigger to ensure the execution order.
