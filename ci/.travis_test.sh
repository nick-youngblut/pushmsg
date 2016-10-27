#!/usr/bin/env bash

set -e

python -c "import IPython; print('IPython %s' % IPython.__version__)";
python -c "import pushnote; print('pushnote %s' % pushnote.__version__)";
ipython -c "%load_ext pushnote";
