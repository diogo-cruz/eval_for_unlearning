set -e 

apt-get update && apt-get install -y vim unzip

curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH=$PATH:$HOME/.local/bin/env

uv init
uv venv --python=3.10
source .venv/bin/activate

uv pip install -r requirements.txt


# git clone https://github.com/felipemaiapolo/tinyBenchmarks.git
# uv pip install -e tinyBenchmarks