#!/usr/bin/env bash

set -e

python -c "import IPython; print('IPython %s' % IPython.__version__)";
python -c "import pushmsg; print('pushmsg %s' % pushmsg.__version__)";
ipython -c "%load_ext pushmsg";
