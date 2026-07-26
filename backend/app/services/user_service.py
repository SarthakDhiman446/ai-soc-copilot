from sqlalchemy.orm import Session

from app.auth.hashing import hash_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    def create_user(db: Session, user: UserCreate):

        existing_user = db.query(User).filter(
            User.email == user.email
        ).first()

        if existing_user:
            raise ValueError("Email already registered")

        db_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):

        print("\n" + "=" * 60)
        print("🔍 LOGIN ATTEMPT")
        print("=" * 60)

        print("Entered Email:", email)
        print("Entered Password:", password)
        print("Password Length:", len(password))

        user = db.query(User).filter(
            User.email == email
        ).first()

        if not user:
            print("❌ User NOT found in database")
            print("=" * 60)
            return None

        print("✅ User found")
        print("Database Email:", user.email)
        print("Stored Hash:", user.password)
        print("Hash Length:", len(user.password))

        result = verify_password(password, user.password)

        print("Password Verified:", result)
        print("=" * 60)

        if not result:
            return None

        return user