from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Only admins can access this function")
            return None
        else:
            func(user_role)
    return wrapper


@require_admin
def access_tea_inventory(user_role):
    print("Accessing tea inventory")

access_tea_inventory("user")
access_tea_inventory("admin")