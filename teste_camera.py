import cv2

# Constantes
RESOLUCAO_LARGURA = 1920  # Resolução desejada (Full HD)
RESOLUCAO_ALTURA = 1080
TECLA_SAIR = 27  # Código ASCII para 'ESC'
CAMERA_INDICE = 0


def listar_cameras_disponiveis():
    """Lista as câmeras disponíveis no sistema."""
    cameras_disponiveis = []
    for indice in range(10):  # Verifica os primeiros 10 índices de dispositivo
        captura = cv2.VideoCapture(indice)
        if captura.isOpened():
            cameras_disponiveis.append(indice)
            captura.release()
    return cameras_disponiveis


def configurar_captura(indice_camera=0, largura=RESOLUCAO_LARGURA, altura=RESOLUCAO_ALTURA):
    """Configura a captura de vídeo com resolução especificada."""
    captura = cv2.VideoCapture(indice_camera)
    captura.set(cv2.CAP_PROP_FRAME_WIDTH, largura)
    captura.set(cv2.CAP_PROP_FRAME_HEIGHT, altura)
    resolucao_largura = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
    resolucao_altura = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Resolução configurada: {resolucao_largura}x{resolucao_altura}")
    return captura


# Listar e exibir as câmeras
cameras = listar_cameras_disponiveis()
if cameras:
    print(f"Câmeras disponíveis: {cameras}")
else:
    print("Nenhuma câmera disponível.")

# Configura a captura de vídeo
video_capture = configurar_captura(CAMERA_INDICE)

# Loop principal de captura e exibição
while True:
    captura_sucedida, quadro = video_capture.read(CAMERA_INDICE)
    if not captura_sucedida:
        print("Erro ao capturar o vídeo.")
        break

    cv2.imshow("Melhor Resolucao da Camera - ESC para sair", quadro)
    if cv2.waitKey(1) & 0xFF == TECLA_SAIR:
        break

# Liberar captura e fechar janelas
video_capture.release()
cv2.destroyAllWindows()
