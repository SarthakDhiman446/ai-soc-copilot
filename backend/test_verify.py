from app.auth.hashing import verify_password

hashed = "$2b$12$a6y0X78Gug.CooYA/VmHtOcw0II1lPAS5b12SP5UkY349V317fQXa"

print(verify_password("Sarthak123", hashed))