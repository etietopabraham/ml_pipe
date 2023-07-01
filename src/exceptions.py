import sys 

def get_error_message(error, error_details:sys)->str:
    _,_,exc_tb = error_details.exc_info()
    error_message = "The error occured in file {0}, on line number {1}, error details: {2}".format(
        exc_tb.tb_frame.f_code.co_filename,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys) -> str:
        super().__init__(error_message)
        self.error_message = get_error_message(error=error_message, error_details=error_details)

    def __str__(self) -> str:
        return self.error_message
    

# Test
# import logger
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logger.logging.info("Divide by zero exception has occured")
#         raise CustomException(e, sys) 