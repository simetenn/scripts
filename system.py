import subprocess
import sys

from logger import create_logger

logger = create_logger("error")

def system(cmds):
    """Run system command cmd using subprocess module."""
    output = None

    if isinstance(cmds, str):
        cmds = [cmds]

    if isinstance(cmds, (tuple, list)):
        for cmd in cmds:
            logger.debug(cmd)

            try:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                if output:
                    output = output.decode("utf-8")
                    logger.debug(output)

            except subprocess.CalledProcessError as e:
                msg = "Command failed with return code: {returncode}: \n {cmd} \n  \n\nSee output above for details.".format(cmd=cmd, returncode=e.returncode)
                logger.error(e.output.decode("utf-8"))
                logger.error(msg)
                sys.exit(1)

    else:
        raise TypeError

    return output
