class KillRequestedException(BaseException):
    """Exception raised when a kill request is received during scraping."""
    def __init__(self, runner):
        self.runner = runner
        super().__init__(f"KILL_REQUEST received for session {runner.session_id}")