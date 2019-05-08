FROM python:3.7.3-alpine

# ソースを置くディレクトリを変数として格納
ARG project_dir=/root/

# 必要なファイルをローカルからコンテナにコピー
ADD requirements.txt $project_dir

# requirements.txtに記載されたパッケージをインストール
WORKDIR $project_dir
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# （コンテナ内で作業する場合）必要なパッケージをインストール
RUN apk update
RUN apk add zsh vim tmux git tig
