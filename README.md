# try streamlit

[streamlit](https://streamlit.io/)で MultipageApp を作ってみるテスト

## 環境構築

- clone this repository
- build & run container

```bash
docker-compose up
```

-d などはお好みで。

## 開発環境に入る

docker containerが立ち上がっているので、コンテナに入って作業する（入らなくても良いけど）。

### Visual Studio Code の利用

Extension [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を使うなどして、コンテナにアタッチする。


### コンソールの利用

コンテナIDを確認

```bash
docker ps -a | grep try_streamlit
```

コンテナに入る

```bash
docker exec -it {コンテナ名 | コンテナID} bash 
```


## Streamlit App の起動

```bash
poetry run streamlit run src/home.py
```
