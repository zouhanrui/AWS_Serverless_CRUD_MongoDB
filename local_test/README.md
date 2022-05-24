# Context Manager
This interface of __enter__() and __exit__() methods
 which provides the support of with statement in user defined objects
 is called Context Manager.
> *with* statement in Python: https://www.geeksforgeeks.org/with-statement-in-python/
>> The *with* statement itself ensures proper acquisition and release of resources. 

> To use with statement in user defined objects you only need to add the methods __enter__() and __exit__() in the object methods.

__enter__() method, initialize the resource you wish to use in the object.

__enter__() method should always return a descriptor of the acquired resource.

 All the acquired resources are released in the __exit__() method.

https://www.geeksforgeeks.org/context-manager-in-python/

the usage of resources like file operations or database connections is very common


# ODM vs ORM
> ORM (object Relation Mapping) and ODM (Object Document Mapping)
> 


https://medium.com/@julianam.tyler/what-is-the-difference-between-odm-and-orm-267bbb7778b0


# marshmallow: simplified object serialization
* marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

https://marshmallow.readthedocs.io/en/stable/

In short, marshmallow schemas can be used to:

* Validate input data.

* Deserialize input data to app-level objects.

* Serialize app-level objects to primitive Python types. The serialized objects can then be rendered to standard formats such as JSON for use in an HTTP API.

> Data pre-processing and post-processing methods can be registered using 
> the pre_load, post_load, pre_dump, and post_dump decorators.
> 
> https://marshmallow.readthedocs.io/en/stable/extending.html
> 
> https://blogs.sap.com/2014/03/28/how-to-use-pre-load-and-post-load-command-in-data-services/


# pymongo >> MongoClient
https://www.w3schools.com/python/python_mongodb_getstarted.asp

# MongoDB - Atlas:
https://cloud.mongodb.com/v2/628a855c9f07f73a23ff6386#clusters

> Cheat sheet:
https://gist.github.com/bradtraversy/f407d642bdc3b31681bc7e56d95485b6


