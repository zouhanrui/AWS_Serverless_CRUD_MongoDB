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
>Validation Without Deserialization
> 
> https://marshmallow.readthedocs.io/en/stable/quickstart.html#validation-without-deserialization
> 
> Validation Schema.load() vs Schema.loads()
> 
> > https://marshmallow.readthedocs.io/en/stable/quickstart.html#validation
> 
> 
> >load(data: Mapping[str, Any] | Iterable[Mapping[str, Any]], *, many: bool | None = None, partial: bool | types.StrSequenceOrSet | None = None, unknown: str | None = None)
> 
> >loads(json_data: str, *, many: bool | None = None, partial: bool | types.StrSequenceOrSet | None = None, unknown: str | None = None, **kwargs)
> 
>

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
> 
> 
> 

# ujson (ultraJson)
https://pypi.org/project/ujson/
# ujson Encoding and Decoding
> https://mpython.readthedocs.io/en/master/library/pythonStd/ujson.html
>
>ujson.dumps() -> Convert dict type data to str
> 
> ujson.loads() -> Parse the JSON string and return the object.
>>> obj = {1:2, 3:4, "a":6} \
>>> jsDumps = ujson.dumps(obj) \
>>> jsLoads = ujson.loads(jsDumps) \
>>> print(type(obj), obj) \
<class 'dict'> {3: 4, 1: 2, 'a': 6} \
>>> print(type(jsDumps), jsDumps) \
<class 'str'> {3: 4, 1: 2, "a": 6} \
>>> print(type(jsLoads), jsLoads) \
<class 'dict'> {'a': 6, 1: 2, 3: 4} \
> 



# JWT
> JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.
> https://jwt.io/introduction

* ***Authorization***: This is the most common scenario for using JWT. Once the user is logged in, each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token. Single Sign On is a feature that widely uses JWT nowadays, because of its small overhead and its ability to be easily used across different domains.

* ***Information Exchange***: JSON Web Tokens are a good way of securely transmitting information between parties.


> import jwt<br>
> encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")<br>
> print(encoded_jwt)<br>
>> eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U<br>
> 
> jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])<br>
>> {'some': 'payload'}


# Python unit test

> Python’s assert statement
> 
> https://realpython.com/python-assert-statement/#the-syntax-of-the-assert-statement



# json
> json.loads() vs json.dumps()
> 
> https://www.educative.io/edpresso/what-is-the-difference-between-jsonloads-and-jsondumps
> 
> 

# API 
> RESTful API vs. HTTP API 
>> https://hevodata.com/learn/http-api-vs-rest-api/
> 
>  
> API Gateway
>> https://www.redhat.com/en/topics/api/what-does-an-api-gateway-do
>
>> https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html