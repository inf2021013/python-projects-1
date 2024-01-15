# Trying to find module in the parent package
import config
    print(config.debug)
    del config
except ImportError:
    print('Relative import failed')

























