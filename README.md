## The repository pattern
The changing pace of software development needs us to develop faster ways of deploying software. We need tests that grant us some safety-net from real world bugs.
To enable testing, we need to decouple the various parts of our application from each other. This needs some knowledge of domain-driven design(Modelling objects) with the business model(domain) in mind. 

Since, most of the job we do as software developers is to create some sort of CRUD(Create-Read-Update-Delete), we'll be interacting with databases to store our data. 

The repository pattern is an abstraction over storage. This allows us to not know about the implementation details of whichever repository we'll use. 
We create an abstract repository(interface) which defines the methods and the return types that the repositories implementing the interface will need to have. 

https://lyz-code.github.io/blue-book/architecture/repository_pattern/

## Advantages of Repository Pattern
- Enables testability of database storage.
- Makes the switch/migration from one database system to another easy. (From PostgreSQL to MongoDB)
- Easier to mock the repository when doing end-to-end tests.
- Frees the API layer of the data storage implementation details, so the API Layer doesn't know which database the system is using. 


