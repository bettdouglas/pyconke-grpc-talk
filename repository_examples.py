from domain_models import User
from data_repositories import UserRepository
from arango_db_user_repository import ArangoUserRepository


# neater cruds

user_repository = ArangoUserRepository()
# user_repository = PostgresqlUserRepository()
# user_repository = MongoDBUserRepository()

user = User(id="1", name="John", phone="+1-123-456-7890")

# create user
saved_user = user_repository.add(user)

# get user
got_user = user_repository.get_user_by_id(saved_user.id)

# update 
user.phone = "+1-234-567-8901"
updated_user = user_repository.update(user)

# delete 
deleted_user = user_repository.delete(user)

deleted_user = user_repository.delete_by_id(user.id)