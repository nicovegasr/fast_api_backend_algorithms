from fastapi import APIRouter, status

class AlgorithmController:
  def __init__(self):
    self.router = APIRouter()
    self.router.get("/get_algorithms", status_code=status.HTTP_200_OK)(self.get_algorithms)

  def get_algorithms(self):
    return ["drivers"]
# class UserController:
#     def __init__(self):
#         self.router = APIRouter()

#         # Definir las rutas y los controladores correspondientes
#         self.router.get("/users", self.get_users)
#         self.router.get("/users/{user_id}", self.get_user)
#         self.router.post("/users", self.create_user)

#     def get_users(self):
#         # Lógica para obtener usuarios
#         return {"message": "List of users"}

#     def get_user(self, user_id: int):
#         # Lógica para obtener un usuario por ID
#         return {"message": f"User {user_id}"}

#     def create_user(self, user_data: dict):
#         # Lógica para crear un nuevo usuario
#         return {"message": "User created successfully"}
