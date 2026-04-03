'''import logging
import time
import flet as ft

# Generate a dynamic filename with timestamp
log_filename = f"SentinelOne_API_{time.strftime('%Y-%m-%d-%H-%M-%S')}.log"

# Set up logging configuration
logging.basicConfig(filename=log_filename, 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(message, terminal_output, level='info'):
    if level == 'info':
        logging.info(message)
        terminal_output.value += f"INFO: {message}\n"
        terminal_output.page.update()
        logging.shutdown()
    elif level == 'warning':
        logging.warning(message)
        terminal_output.value += f"Warning: {message}\n"
        terminal_output.page.update()
        logging.shutdown()
    elif level == 'error':
        logging.error(message)
        terminal_output.value += f"Error: {message}\n"
        terminal_output.page.update()
        logging.shutdown()
    elif level == 'critical':
        logging.critical(message)
        terminal_output.value += f"Critical: {message}\n"
        terminal_output.page.update()
        logging.shutdown()
    else:
        logging.debug(message)
        terminal_output.value += f"Debug: {message}\n"
        terminal_output.page.update()
        logging.shutdown()
    return
'''

import logging
import time
import flet as ft

# Generate a dynamic filename with timestamp
log_filename = f"SentinelOne_API_{time.strftime('%Y-%m-%d-%H-%M-%S')}.log"

# Set up logging configuration
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_event(message, terminal_output, level='info'):
    # Determine log prefix based on level
    prefix = {
        'info': "INFO",
        'warning': "WARNING",
        'error': "ERROR",
        'critical': "CRITICAL",
        'debug': "DEBUG",
    }.get(level, "INFO")

    # Log to file
    if level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'critical':
        logging.critical(message)
    else:
        logging.debug(message)

    # Log to terminal_output (Flet ListView)
    terminal_output.controls.append(ft.Text(f"{prefix}: {message}"))
    terminal_output.update()
