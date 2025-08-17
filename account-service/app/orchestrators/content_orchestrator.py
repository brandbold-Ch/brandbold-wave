from sqlmodel import Session
from app.decorators.handlers import exception_handler
from app.models import Content
from app.services import ContentService
from app.services import ContentFranchiseService
from app.services import ContentGenreService
from app.dtos import CreateContentDto


class ContentOrchestrator:

    def __init__(self):
        self.content_service = ContentService()
        self.genre_service = ContentGenreService()
        self.franchise_service = ContentFranchiseService()

    @exception_handler
    def register_content(
            self,
            data: CreateContentDto,
            session: Session
    ) -> Content:
        content = self.content_service.create_content(data.flat_info(), session, False)
        session.flush()

        for genre_id in data.genres:
            self.genre_service.create_genre(genre_id, content.id, session, False)
            
        for franchise_id in data.franchises:
            self.franchise_service.create_franchise(franchise_id, content.id, session, False)
        
        session.commit()
        return self.content_service.get_content(content.id, session)
