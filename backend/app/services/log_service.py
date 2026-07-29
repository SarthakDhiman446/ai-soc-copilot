from sqlalchemy.orm import Session

from app.models.log import Log


class LogService:

    @staticmethod
    def create_log(
        db: Session,
        filename: str,
        filepath: str,
        file_size: int
    ):

        log = Log(
            filename=filename,
            filepath=filepath,
            file_size=file_size,
            status="uploaded"
        )

        db.add(log)
        db.commit()
        db.refresh(log)

        return log