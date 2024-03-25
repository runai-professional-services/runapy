class RunaiError(Exception):
    pass

class RuaniHTTPError(RunaiError):
    #TODO: Handle http errors
    pass

class RunaiNotImplementedError(RunaiError):
    pass

class RunaiProjectNotFoundError(RunaiError):
    pass

class RunaiDepartmentNotFoundError(RunaiError):
    pass

class RunaiClusterNotFoundError(RunaiError):
    pass

class RunaiNotFoundError(RunaiError):
    pass