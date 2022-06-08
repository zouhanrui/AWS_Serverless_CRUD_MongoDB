# Recap of this project

* It is a great project to get me familiarized with the different python libraries, such as
marshmallow, pymongo, argon2, ujson, JWT.

>1. marshmallow: built the class inherited by Schema, used to construct the fields of user's information and validated them if the input field is in a valid format.
>2. pymongo: built MongoDB connection class, using __enter__ and __exit__ methods to initialize and release the resource: DB connection
>3. argon2: Instantiated PasswordHasher class and @post_load password info then immediately called hash method to encry the plain text password  
>4. ujson: dumps and loads functions come in handy converting between python dictionary, string, and json
>5. JWT: Once logged in, the subsequent requests includes JWT token in the header as authorization to securely transmit info between parties. application like SSO


* Better understanding python Context Manager and with statement to initialize and release the resource, such as open and close file, connect and disconnect a database, in case the throttling of hitting one resource.


* Learnt and deployed the local project to AWS cloud services. 
> * Built the template yaml file to construct the resources needed for cloudformation which further deploys related services like Lambda and API gateway
> 
> * Studied the template yaml file to understand the AWS Serverless type functions and api, and their properties such as the Code path CodeUri, Handler function, the endpoint path of rest api, the method of rest api
> 
> * Tested via Postman, built a collection and created a variable for my invoke url and tested to invoke the api calls for different endpoints constructed in api gateway and achieved different functionalities. 
> 
> * Debugged lambda functions from Cloudwatch log 
