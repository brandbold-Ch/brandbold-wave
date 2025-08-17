import json
import redis
import logging
import signal
from app.config.sqlmodel_config import create_session
from app.utils.settings import get_settings
from app.orchestrators import ContentOrchestrator
from app.dtos import CreateContentDto

settings = get_settings()
logger = logging.getLogger("worker")


class RedisWorker:
    
    def __init__(self):
        self.redis_client = redis.Redis.from_url(settings.redis_internal_url)
        self.orchestrator = ContentOrchestrator()
        self.running = True
        
    def stop(self):
        logger.info("🛑 Stopping worker gracefully...")
        self.running = False
        
    def process_event(self, key, value):
        session = create_session()
        
        try:
            payload = json.loads(value)            
            model = CreateContentDto.model_validate(payload)

            if key == "spring:content:upload:success":
                self.orchestrator.register_content(model, session)
                logger.info(f"✅ Processed content: {payload}")
            
            elif key == "spring:content:upload:error":
                logger.error(f"❌ Upload error: {payload}")
                
        except Exception:
            logger.exception("❌ Critical error during processing")
            self.redis_client.rpush("flask:metadata:save:rollback", value)
            
        finally:
            session.close()
    
    def run(self):
        logger.info("🎧 Listening to Redis in flask server...")

        while self.running:
            events = self.redis_client.blpop([
                "spring:content:upload:success", 
                "spring:content:upload:error"
            ])
            
            if events:
                key = events[0].decode()
                value = events[1].decode()
                self.process_event(key, value)
                

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    worker = RedisWorker()
    
    signal.signal(signal.SIGINT, worker.stop)
    signal.signal(signal.SIGTERM, worker.stop)
    
    worker.run()
    