

from datetime import datetime, timezone
from app.db.engine import insert_metadata
from app.schemas.schemas import Metadata


def process_metadata(request_date: str,
                     client_info: dict, 
                     metadata: Metadata):
    request_date = datetime.now(tz=timezone.utc).isoformat()
    insert_response = insert_metadata(
        user_id=metadata.user_id, 
        contract_name=metadata.contract_name, 
        date_created=request_date,
        contract_url=metadata.contract_url, 
        metadata=metadata.metadata,
        client_ip=client_info.get("host"),
        client_port=client_info.get("port"),
        client_user_agent=client_info.get("user_agent")
    )
    
    return insert_response