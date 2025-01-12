import cv2
import mediapipe as mp

# Define constantes para configuração
RESOLUCAO_LARGURA_FINAL = 1920
RESOLUCAO_ALTURA_FINAL = 1080
NOME_JANELA = "Deteccao de Maos, ESC para fechar"
TAMANHO_JANELA = (1600, 900)
CAMERA_INDICE = 0

# Constantes
DEDO_INDICES = [8, 12, 16, 20]  # Indicador, Médio, Anelar e Mindinho
POSICAO_RETANGULO = {"Direita": (10, 10), "Esquerda": (-200, 10)}

# Configuração do MediaPipe Hands
mp_maos = mp.solutions.hands
maos = mp_maos.Hands(max_num_hands=2)
desenho = mp.solutions.drawing_utils

# Configurando estilos para pontos e conexões (linhas)
cor_linhas = desenho.DrawingSpec(color=(0, 0, 255), thickness=2)  # Verde para conexões
cor_pontos = desenho.DrawingSpec(color=(0, 255, 0), thickness=2)  # Vermelho para os pontos


def determina_lado_mao(handedness, idx):
    """
    Determina se uma mão detectada é esquerda ou direita.

    Args:
        handedness: Resultado da classificação da mão fornecido pelo MediaPipe.
        idx: Índice da mão a ser processada.

    Returns:
        Uma string representando o lado da mão ('Esquerda' ou 'Direita').
        Retorna 'Desconhecido' se não houver classificação disponível.
    """
    if handedness:
        lado_mao_label = handedness[idx].classification[0].label
        return "Direita" if lado_mao_label == "Left" else "Esquerda"
    return "Desconhecido"


def conta_dedos(pontos, lado_mao):
    """
    Conta o número de dedos levantados com base nos pontos das landmarks.

    Args:
        pontos: Lista de coordenadas dos pontos da mão em pixels.
        lado_mao: String indicando o lado da mão ('Esquerda' ou 'Direita').

    Returns:
        O número de dedos levantados (inteiro).
    """

    polegar_levantado = (
            (lado_mao == "Esquerda" and pontos[4][0] < pontos[3][0]) or
            (lado_mao == "Direita" and pontos[4][0] > pontos[3][0])
    )

    # Inicializa a contagem de dedos levantados
    dedos_levantados = 0

    # Itera pelos índices dos dedos
    for dedo in DEDO_INDICES:
        # Verifica se o dedo está levantado comparando sua posição vertical
        if pontos[dedo][1] < pontos[dedo - 2][1]:
            dedos_levantados += 1

    # Soma o estado do polegar com os dedos levantados
    return dedos_levantados + polegar_levantado


def desenha_mao(imagem, lado_mao, contador_dedos, largura):
    """
    Desenha as informações da mão detectada na imagem processada.

    Args:
        imagem: Imagem em que os desenhos serão exibidos.
        lado_mao: String indicando o lado da mão ('Esquerda' ou 'Direita').
        contador_dedos: Número de dedos levantados.
        largura: Largura da imagem em pixels.

    Returns:
        None. A imagem é modificada diretamente.
    """
    start_x, start_y = POSICAO_RETANGULO[lado_mao] if lado_mao in POSICAO_RETANGULO \
        else (10, 10)
    # Ajusta posição relativa ao lado esquerdo
    start_x += largura if lado_mao == "Esquerda" else 0

    # Desenha o retângulo de fundo
    cv2.rectangle(imagem, (start_x, start_y), (start_x + 170, start_y + 100), (255, 0, 0), -1)
    # Exibe o lado da mão e a contagem de dedos levantados
    cv2.putText(imagem, f"{lado_mao}", (start_x + 10, start_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(imagem, f"Dedos: {contador_dedos}", (start_x + 10, start_y + 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


def processa_maos(imagem, resultado, largura, altura):
    """
    Processa as mãos detectadas na imagem.

    Args:
        imagem: Frame atual capturado pela câmera.
        resultado: Resultado do processamento fornecido pelo MediaPipe Hands.
        largura: Largura da imagem em pixels.
        altura: Altura da imagem em pixels.

    Returns:
        None. A imagem é modificada diretamente.
    """
    if resultado.multi_hand_landmarks:
        for idx, pontos_landmarks in enumerate(resultado.multi_hand_landmarks):
            # Desenha os pontos das mãos detectadas
            desenho.draw_landmarks(imagem, pontos_landmarks, mp.solutions.hands.HAND_CONNECTIONS, cor_linhas, cor_pontos)

            lado_mao = determina_lado_mao(resultado.multi_handedness, idx)
            pontos = []

            # Identifica e processa os pontos das landmarks
            for id, coordenada in enumerate(pontos_landmarks.landmark):
                cx, cy = int(coordenada.x * largura), int(coordenada.y * altura)

                # Adiciona os pontos convertidos
                pontos.append((cx, cy))

                # Desenha o índice do ponto na imagem
                cv2.putText(imagem, str(id), (cx, cy + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            contador_dedos = conta_dedos(pontos, lado_mao)
            desenha_mao(imagem, lado_mao, contador_dedos, largura)


def configurar_video_e_janela_local():
    """
    Configura a captura de vídeo e a exibição da janela.
    """
    captura = cv2.VideoCapture(CAMERA_INDICE)
    captura.set(cv2.CAP_PROP_FRAME_WIDTH, RESOLUCAO_LARGURA_FINAL)
    captura.set(cv2.CAP_PROP_FRAME_HEIGHT, RESOLUCAO_ALTURA_FINAL)
    cv2.namedWindow(NOME_JANELA, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(NOME_JANELA, TAMANHO_JANELA[0], TAMANHO_JANELA[1])
    return captura

def configurar_video_e_janela(resolucao_largura, resolucao_altura, tamanho_janela):
    """
    Configura a captura de vídeo e a janela de exibição para o OpenCV.
    """
    captura = cv2.VideoCapture(CAMERA_INDICE)

    # Configura resolução da captura
    captura.set(cv2.CAP_PROP_FRAME_WIDTH, resolucao_largura)
    captura.set(cv2.CAP_PROP_FRAME_HEIGHT, resolucao_altura)

    # Garante que a janela seja criada corretamente apenas uma vez
    cv2.namedWindow("Stream de Mãos", cv2.WINDOW_NORMAL)

    # Ajusta a dimensão da janela para os valores calculados (ex.: 16:9)
    cv2.resizeWindow("Stream de Mãos", tamanho_janela[0], tamanho_janela[1])

    return captura


def main():
    video_capture = configurar_video_e_janela_local()

    while True:
        sucesso, frame = video_capture.read()
        if not sucesso or frame is None:
            print("Erro ao capturar o vídeo.")
            continue

        # Processa o frame
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultado = maos.process(frame_rgb)
        altura, largura, _ = frame.shape
        processa_maos(frame, resultado, largura, altura)
        cv2.imshow(NOME_JANELA, frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Tecla Esc para fechar
            break

    # Libera recursos
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
