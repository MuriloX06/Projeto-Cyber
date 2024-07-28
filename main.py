import os
import time
import sys
import numpy as np
import pyautogui
import cv2
from PIL import Image
import pystray
from pystray import MenuItem as item
from tkinter import Tk
from tkinter.filedialog import askdirectory

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Função para carregar o ícone personalizado
def load_icon():
    icon_name = 'icon.ico'
    possible_paths = [
        resource_path(icon_name),
        resource_path(f'_internal/{icon_name}'),  # Adiciona a verificação na pasta _internal
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return Image.open(path)
    raise FileNotFoundError(f"Ícone {icon_name} não encontrado nos caminhos: {possible_paths}")

# Função para mostrar uma janela de diálogo para escolher a pasta
def get_directory():
    # Inicializa a janela do tkinter
    root = Tk()
    root.withdraw()  # Oculta a janela principal do tkinter

    # Abre a janela de diálogo para escolher a pasta
    directory = askdirectory(title="Escolha a pasta para salvar o vídeo")
    return directory

# Função para criar um nome de arquivo com base na data e hora atuais
def get_filename(directory):
    timestamp = time.strftime('%d-%m-%Y - %Hh%Mm%Ss')
    return os.path.join(directory, f'Gravação {timestamp}.avi')

# Função para gravar a tela
def record_screen(filename, duration=60):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 7.0
    out = cv2.VideoWriter(filename, fourcc, fps, screen_size)

    start_time = time.time()
    while int(time.time() - start_time) < duration:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    
    out.release()
    cv2.destroyAllWindows()

# Função chamada ao clicar no menu de contexto
def on_click(icon, item):
    directory = get_directory()
    if directory:  # Verifica se o usuário selecionou uma pasta
        filename = get_filename(directory)
        icon.notify('Gravação iniciada! Aguarde 1 minuto para terminar.')
        time.sleep(3)  # Pequeno delay para garantir que a notificação seja vista
        record_screen(filename)
        icon.notify(f'Gravação concluída! Salvo em: {filename}')
    else:
        icon.notify('Gravação cancelada.')

# Função para criar o menu de contexto
def setup_menu():
    return (item('Gravar Tela', on_click), item('Sair', exit_program))

# Função para sair do programa
def exit_program(icon, item):
    icon.stop()

# Função principal
def main():
    icon = pystray.Icon(name, load_icon(), name, menu=setup_menu())
    icon.run()

if __name__ == "__main__":
    name = 'Gravador de Tela'
    main()
