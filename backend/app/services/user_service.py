from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.auth.hashing import hash_password


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