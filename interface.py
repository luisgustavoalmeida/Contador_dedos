import tkinter as tk
from tkinter import ttk
import threading
import cv2
from processar_video import configurar_video_e_janela, processa_maos, maos  # Importe suas funções do código principal


class AppInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Detecção de Mãos")
        self.root.geometry("400x350")
        self.running = False
        self.video_thread = None

        # Variável para controlar o log
        self.generate_log = tk.BooleanVar(value=False)  # Inicialmente desativado (False)

        # Botões
        self.start_button = ttk.Button(root, text="Iniciar Detecção", command=self.start_video)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(root, text="Parar Detecção", command=self.stop_video)
        self.stop_button.pack(pady=10)

        # Exibição de status
        self.status_label = ttk.Label(root, text="Status: Parado")
        self.status_label.pack(pady=10)

        # Ajustes de Resolução
        frame_resolucao = ttk.Frame(root)  # Cria um frame para centralizar os widgets
        frame_resolucao.pack(pady=10)  # Adiciona espaçamento em relação ao restante da interface
        ttk.Label(frame_resolucao, text="Resolução", justify="center").pack()  # Rótulo centralizado
        self.resolutions = [("1920x1080", (1920, 1080)), ("1280x720", (1280, 720)), ("640x480", (640, 480))]
        self.selected_res = tk.StringVar(value="1920x1080")

        # Adiciona os botões de rádio ao frame centralizado
        for text, _ in self.resolutions:
            ttk.Radiobutton(frame_resolucao, text=text, variable=self.selected_res, value=text).pack(anchor="w")

        # Controle de Janela
        ttk.Label(root, text="Tamanho da Janela (px)").pack(pady=10)
        self.slider_window = ttk.Scale(root, from_=640, to=1920, orient="horizontal", command=self.update_window_size, length=350)
        self.slider_window.set(1600)
        self.slider_window.pack()

        # Opção de Gerar Log
        ttk.Checkbutton(
            root,
            text="Gerar Log",
            variable=self.generate_log,  # Variável vinculada ao estado do checkbox
            onvalue=True,  # Valor se a checkbox for ativada
            offvalue=False  # Valor se a checkbox for desativada
        ).pack(pady=10)

    def start_video(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Em Execução")
            self.video_thread = threading.Thread(target=self.run_video)
            self.video_thread.start()

    def stop_video(self):
        self.running = False
        self.status_label.config(text="Status: Parado")

    def update_window_size(self, event):
        new_size = int(self.slider_window.get())
        self.status_label.config(text=f"Tamanho da janela ajustado para {new_size}px")

    def run_video(self):
        # Verifica se o log está ativado
        gerar_log = self.generate_log.get()

        # Extraindo valores da interface gráfica
        resolucao_str = self.selected_res.get()  # Exemplo: "1920x1080"
        resolucao_largura, resolucao_altura = map(int, resolucao_str.split("x"))

        # Ajusta o tamanho da janela como uma tupla
        largura_janela = int(self.slider_window.get())
        altura_janela = int(largura_janela * resolucao_altura / resolucao_largura)
        # Tamanho final da janela
        tamanho_janela = (largura_janela, altura_janela)

        # Passando os valores corretos para a função
        captura = configurar_video_e_janela(resolucao_largura, resolucao_altura, tamanho_janela)
        while self.running:
            sucesso, frame = captura.read()
            if not sucesso or frame is None:
                continue

            # Processar a imagem
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            resultado = maos.process(frame_rgb)
            altura, largura, _ = frame.shape
            processa_maos(frame, resultado, largura, altura, log_habilitado=gerar_log)
            cv2.imshow("Stream de Mãos", frame)

            # Parar ao pressionar Esc
            if cv2.waitKey(1) & 0xFF == 27:
                break

        captura.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppInterface(root)
    root.mainloop()
