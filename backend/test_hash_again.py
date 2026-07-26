from app.auth.hashing import hash_password, verify_password

password = "Sarthak123"

hashed = hash_password(password)

print("Generated Hash:", hashed)
print("Verify:", verify_password(password, hashed))