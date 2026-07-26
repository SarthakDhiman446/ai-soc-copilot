from app.auth.hashing import hash_password

password = "Sarthak123"

hashed = hash_password(password)

print("Original Password:", password)
print("Hashed Password:", hashed)