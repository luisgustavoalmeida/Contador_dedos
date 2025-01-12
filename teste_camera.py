import cv2

# Constantes
RESOLUCAO_LARGURA = 1920  # Resolução desejada (Full HD)
RESOLUCAO_ALTURA = 1080
TECLA_SAIR = 27  # Código ASCII para 'ESC'


def configurar_captura(indice_camera=0, largura=RESOLUCAO_LARGURA, altura=RESOLUCAO_ALTURA):
    """Configura a captura de vídeo com resolução especificada."""
    captura = cv2.VideoCapture(indice_camera)
    captura.set(cv2.CAP_PROP_FRAME_WIDTH, largura)
    captura.set(cv2.CAP_PROP_FRAME_HEIGHT, altura)
    resolucao_largura = int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
    resolucao_altura = int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Resolução configurada: {resolucao_largura}x{resolucao_altura}")
    return captura


# Configura a captura de vídeo
video_capture = configurar_captura()

# Loop principal de captura e exibição
while True:
    captura_sucedida, quadro = video_capture.read()
    if not captura_sucedida:
        print("Erro ao capturar o vídeo.")
        break

    cv2.imshow("Melhor Resolucao da Camera - ESC para sair", quadro)
    if cv2.waitKey(1) & 0xFF == TECLA_SAIR:
        break

# Liberar captura e fechar janelas
video_capture.release()
cv2.destroyAllWindows()