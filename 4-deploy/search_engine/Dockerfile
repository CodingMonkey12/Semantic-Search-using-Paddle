# Build Python 3.9 environment
FROM python:3.9

# MainTainer
LABEL MainTainer="Chen Zehao"

# Add files into workdir
ADD . /search_engine

# Set workdir
WORKDIR /search_engine

# pip Update
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

# pip Configuration
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# Install the requirements
RUN pip install -r requirements.txt
