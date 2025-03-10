# Cobble Video Downloader

O **Cobble Video Downloader** é uma aplicação desenvolvida em Python com a biblioteca Tkinter para baixar vídeos e áudios do YouTube. A ferramenta permite ao usuário buscar informações sobre o vídeo, como título, duração, tamanho do arquivo e tempo estimado de download, além de selecionar a qualidade desejada e o local de salvamento.

## 🚀 Funcionalidades

- **Busca de vídeos**: insira a URL do vídeo do YouTube e visualize informações como:
  - Thumbnail
  - Título (limitado a 50 caracteres)
  - Duração
  - Tamanho do arquivo
  - Tempo estimado de download
- **Seleção de qualidade**: escolha entre 1080p, 720p ou MP3.
- **Download personalizado**: defina o diretório de salvamento dos arquivos baixados.

## 🧩 Tecnologias utilizadas

- **Python 3**
- **Tkinter**: interface gráfica
- **yt-dlp**: extração de informações e download de vídeos
- **Pillow**: manipulação de imagens (thumbnails)
- **Requests**: requisições HTTP para carregar thumbnails
- **Speedtest-cli**: medição da velocidade de download

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/LRaposoRocha/Cobble-Video-Downloader.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd CobbleVideoDownloader
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate   # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 📜 Uso

Para iniciar o aplicativo, basta rodar o arquivo principal:
```bash
python cobble_video_downloader.py
```

Depois, é só inserir a URL do vídeo, buscar as informações, selecionar a qualidade desejada, escolher o local para salvar e clicar em **Download**.

## 🔧 Estrutura do código

- **Back-End**: Funções que lidam com a extração de dados do vídeo, cálculo do tempo de download e manipulação de arquivos.
- **Front-End**: Interface gráfica construída com Tkinter, organizada em frames para uma experiência visual clara e responsiva.

## ✅ Melhorias futuras

- Adicionar uma barra de progresso durante o download.
- Implementar a funcionalidade de pausar e retomar downloads.
- Suporte a playlists.

## 📃 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e contribuir!

---

Feito por Leonardo Raposo Rocha.

