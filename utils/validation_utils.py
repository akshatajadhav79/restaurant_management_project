from email.utils import parseaddr
import logging 

logger = logging.getLogger(__name__)

def validate_email_address(email):
    try:
        name,addr = parseaddr(email)
        if "@" in addr '.' in addr.split('@')[-1]:
            return True
        return False

    except Exception as e:
        logger.error(f"Email validation error:{e}")
        return False