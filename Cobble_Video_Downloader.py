# Importando as bibliotecas necessárias para executar o código.
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import yt_dlp
from io import BytesIO
import speedtest

# ----------------------------------------------------------------------------------------------------
# Back-End

# Define o comprimento máximo do título do vídeo.
def lim_titulo(titulo):
  
  if len(titulo) <= 50:
    return titulo
  else:
    return titulo[:47] + "..." 
    
def video_info():
  
  url_pesq = url_input.get()
  
  for widget in thumb_frame.winfo_children():
    widget.destroy()
    
  if url_pesq.strip():
    try:
      with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url_pesq, download = False)
        thumb = info.get('thumbnail')
        title = lim_titulo(info.get('title'))
        duration = info.get('duration_string', 'Nenhum')  
        file_size = round(info.get('filesize_approx', 0) / (1024 * 1024), 2)        
        estimated_time = calculate_estimated_download_time(url_pesq)

        response = requests.get(thumb)
        img_data = Image.open(BytesIO(response.content))
        img_data.thumbnail((180, 180))
        img_plot = ImageTk.PhotoImage(img_data)
        
        duration_value_label.config(text=duration)
        file_size_value_label.config(text=f'{file_size} MB')
        
        if estimated_time is not None:
          download_time_value_label.config(text = f'Estimativa: {estimated_time}')
        
        img_label = tk.Label(thumb_frame, image = img_plot)
        img_label.image = img_plot
        img_label.pack()
        tk.Label(thumb_frame, text = f'{title}', font = ('Leelawadee UI', 11)).pack(pady = 4)

        root.update_idletasks()
        
    except Exception as e:
      error_label = tk.Label(thumb_frame, text = 'Erro ao carregar informações.', font = ('Leelawadee UI', 11), fg = 'red')
      error_label.pack(pady = 8)
  
  else:
    thumb_frame.pack_forget()
    thumb_frame.pack(**padd_out)
    
def calculate_estimated_download_time(url):
  try:
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    
    
    with yt_dlp.YoutubeDL({'quiet' : True}) as ydl:
      info = ydl.extract_info(url, download = False)
      file_size_bytes = info.get('filesize', 0)
      
      if file_size_bytes == 0:
        return None
        
      file_size_mb = file_size_bytes / 1_000_000
      estimated = file_size_mb / (download_speed / 8)
      return round(estimated)
  
  except:
    return None


    
def caminho_salvar():
  path = filedialog.askdirectory()
  if path:
    saving_path.config(state = 'normal')
    saving_path.delete(0, tk.END)
    saving_path.insert(0, path)
    saving_path.config(state = 'readonly')
    

# ----------------------------------------------------------------------------------------------------
# Front-End

# Define o 'tela' onde os elementos gráficos serão posicionados.
root = tk.Tk()
root.title('Cobble Video Downloader')

# Define variáveis com valores selecionados previamente.
padd_out = {'padx': 16, 'pady': 8}
padd_in =  {'padx': 8, 'pady': 4}

# Cria 'seções' para um melhor posicionamento dos widgets na tela principal.
# Define o posicionamento da seção 'URL'.
url_frame = tk.Frame(root)
url_frame.pack(**padd_out)

thumb_frame = tk.Frame(root)
thumb_frame.pack(**padd_out)

# Define o posicionamento da seção 'Qualidade'.
quality_frame = tk.Frame(root)
quality_frame.pack(**padd_out)

# Define o posicionamento da seção 'Status'.
status_frame = tk.Frame(root)
status_frame.pack(**padd_out)

# Define o posicionamento da seção 'Salvar'.
save_frame = tk.Frame(root)
save_frame.pack(**padd_out)

# Dentro da seção 'url_frame' são criados, uma Label, um TextInput e um Botão.
tk.Label(url_frame, text = 'URL :', font = ('Leelawadee UI', 11, 'bold')).grid(row = 0, column = 0, **padd_in)
url_input = tk.Entry(url_frame, width = 50)
url_input.grid(row = 0, column = 1, **padd_in)
buscar_button = tk.Button(url_frame, text = 'Buscar', font = ('Leelawadee UI', 10, 'bold'), command = video_info, padx = 15).grid(row = 0, column = 2, **padd_in)

# Dentro da seção 'quality_frame' são criados, uma Label e um ComboBox.
tk.Label(quality_frame, text = 'Qualidade :', font = ('Leelawadee UI', 11, 'bold')).grid(row = 0, column = 0, **padd_in)
quality_selection_combobox = ttk.Combobox(quality_frame, values = ['1080p | MP4', '720p | MP4', 'MP3'], state = 'readonly', justify = 'center')
quality_selection_combobox.set('1080p | MP4')
quality_selection_combobox.grid(row = 0, column = 1, **padd_in)
atualizar_button = tk.Button(quality_frame, text = 'Atualizar', font = ('Leelawadee UI', 10, 'bold'), commnad = None, padx = 15).grid(row = 0, column = 2, **padd_in)

# Dentro da seção 'status_frame' são criados 6 Labels.
# Label responsável pelo o texto 'Duração do vídeo:'.
duration_label = tk.Label(status_frame, text = 'Duração do vídeo:', font = ('Leelawadee UI', 11, 'bold'), anchor = 'w')
duration_label.grid(row = 0, column = 0, **padd_in, sticky = 'w')
# Label responsável por variar o valor de 'Duração do vídeo:'.
duration_value_label = tk.Label(status_frame, text = '', font = ('Leelawadee UI', 11), anchor = 'w')
duration_value_label.grid(row = 0, column = 1, **padd_in, sticky = 'w')

# Label responsável pelo o texto 'Tamanho do arquivo:'.
file_size_label = tk.Label(status_frame, text = 'Tamanho do arquivo:', font = ('Leelawadee UI', 11, 'bold'), anchor = 'w')
file_size_label.grid(row = 1, column = 0, **padd_in, sticky = 'w')
# Label responsável por variar o valor de 'Tamanho do arquivo:'.
file_size_value_label = tk.Label(status_frame, text = '', font = ('Leelawadee UI', 11), anchor = 'w')
file_size_value_label.grid(row = 1, column = 1, **padd_in, sticky = 'w')

# Label responsável pelo o texto 'Tempo de download:'.
download_time_label = tk.Label(status_frame, text = 'Tempo de download:', font = ('Leelawadee UI', 11, 'bold'), anchor = 'w')
download_time_label.grid(row = 2, column = 0, **padd_in, sticky = 'w')
# Label responsável por variar o valor de 'Tempo de download:'.
download_time_value_label = tk.Label(status_frame, text = '', font = ('Leelawadee UI', 11), anchor = 'w')
download_time_value_label.grid(row = 2, column = 1, **padd_in, sticky = 'w')

tk.Label(save_frame, text = 'Escolha o local de salvamento :', font = ('Leelawadee UI', 11, 'bold')).pack(pady = 4)
salvar_button = tk.Button(save_frame, text = 'Salvar', font = ('Leelawadee UI', 10, 'bold'), command = caminho_salvar, padx = 20).pack(pady = 4)
saving_path = tk.Entry(save_frame, width = 50, state = 'readonly')
saving_path.pack(pady = 4)

# Faz com que o código seja executado.
root.mainloop()