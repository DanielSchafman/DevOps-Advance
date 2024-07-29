from datetime import datetime

class CurrentTime:
    def _get_current_time():
        now = datetime.now()
        formatted_time = now.strftime('%d-%m-%y %H:%M:%S')
        return formatted_time