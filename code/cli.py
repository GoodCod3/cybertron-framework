from code.src.app.routes.first_entry.app_manager import AppManager
from src.core.exception.abort_process_exception import AbortProcessException
from src.core.exception.no_data_to_process_exception import (
    NoDataToProcessException,
)
from src.core.helper.logger import Logger

logger = Logger()
app = AppManager()
try:
    logger.info("Process started.")
    app.run()
    summary = app.get_summary()
    logger.info(
        f"""Process finished successfully:
    Input elapsed time: {summary["elapsed_input"]} seconds,
    Transform elapsed time: {summary["elapsed_transform"]} seconds,
    Output elapsed time: {summary["elapsed_output"]} seconds,
    Total elapsed time: {summary["elapsed_total"]}."""
    )
except NoDataToProcessException as err:
    logger.info(str(err))
except AbortProcessException as err:
    logger.critical(str(err), True)
except RuntimeError as err:
    logger.critical(str(err), True)
except Exception as err:
    logger.error(str(err), True)
