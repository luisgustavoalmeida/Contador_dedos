# Contador de Dedos - Detecção de Mãos com MediaPipe e OpenCV

Este projeto tem como objetivo detectar mãos e contar o número de dedos levantados em tempo real utilizando as bibliotecas **MediaPipe** e **OpenCV**.

Este repositório contém um aplicativo desenvolvido em Python que aplica conceitos de **visão computacional** para capturar e processar vídeos em tempo real por meio de uma **webcam**, detectando mãos e exibindo quantos dedos estão levantados para cada mão identificada.

O software é uma demonstração prática da tecnologia **MediaPipe Hands**, uma solução de aprendizado de máquina para localização e rastreamento de landmarks das mãos.

---

## Descrição Geral

O script principal (main.py) utiliza técnicas de **visão computacional** para capturar imagens da webcam, identificar mãos no quadro e contar de forma precisa o número de dedos levantados para cada mão detectada. A aplicação é construída utilizando o **MediaPipe Hands**, que fornece landmarks (pontos de referência) detalhados das mãos.

---

## Funcionalidades

- **Detecção de Múltiplas Mãos**: O sistema suporta a detecção de até **duas mãos simultâneas**.
- **Contagem de Dedos**: Baseia-se na posição dos dedos e orientações das landmarks para identificar dedos levantados.
- **Classificação da Mão (Esquerda/Direita)**: Determina se a mão detectada é a esquerda ou a direita.
- **Renderização em Vídeo**:
    - Desenha landmarks (pontos) e conexões (linhas) das mãos.
    - Mostra o lado da mão e o número de dedos levantados diretamente no vídeo.
- **Configurações Personalizáveis**:
    - Resolução da captura.
    - Tamanho da janela de vídeo.
    - Aparência visual com cores e estilos customizáveis.

---

## Referências Técnicas

Este projeto faz uso da biblioteca **MediaPipe**, desenvolvida pela **Google**, para a detecção de mãos. Para mais detalhes sobre como funciona o MediaPipe, suas funcionalidades e documentações oficiais, visite:

[MediaPipe Solutions Guide (Google AI)](https://ai.google.dev/edge/mediapipe/solutions/guide?hl=pt-br)

---

## Requisitos de Instalação

Certifique-se de instalar as dependências necessárias no seu ambiente Python:

### Dependências principais:

- **Python**: 3.12 (testado e desenvolvido)
- **Bibliotecas**:
    - OpenCV
    - MediaPipe

### Instalando as dependências:

Você pode instalá-las com o comando:

```bash
pip install opencv-python mediapipe
```

---

## Como Executar o Projeto

1. Clone este repositório para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/contador-dedos.git
   cd contador-dedos
   ```

2. Verifique se sua webcam está conectada ao dispositivo.

3. Execute o script principal:
   ```bash
   python main.py
   ```

4. A interface de vídeo será exibida mostrando suas mãos detectadas. O número de dedos levantados aparecerá sob um retângulo.

5. Para **fechar o programa**, pressione a tecla `ESC`.

---

## Configurações Suportadas

Dentro do arquivo `main.py`, os seguintes parâmetros podem ser configurados:

```python
# Configuração da resolução da captura
RESOLUCAO_LARGURA_FINAL = 1920  # Largura desejada em pixels
RESOLUCAO_ALTURA_FINAL = 1080  # Altura desejada em pixels

# Nome da janela de exibição
NOME_JANELA = "Deteccao de Maos, ESC para fechar"

# Tamanho inicial da janela em pixels (largura, altura)
TAMANHO_JANELA = (1600, 900)

# Estilos visuais das landmarks e conexões
cor_linhas = desenho.DrawingSpec(color=(0, 0, 255), thickness=2)  # Cor das conexões: Azul
cor_pontos = desenho.DrawingSpec(color=(0, 255, 0), thickness=2)  # Cor dos pontos: Verde
```

Essas configurações podem ser ajustadas para personalizar o comportamento do programa, como alterar a resolução de saída da câmera ou o estilo visual da renderização das mãos.

---

## Principais Funções

O código é desenvolvido de forma modular, e algumas de suas funções principais incluem:

### Determina o lado da mão
```python
def determina_lado_mao(handedness, idx):
    """
    Determina se uma mão detectada é a esquerda ou direita.
    Retorna:
        - "Esquerda" ou "Direita" dependendo do classificador.
        - "Desconhecido" caso não seja possível classificar.
    """
```

### Conta dedos levantados
```python
def conta_dedos(pontos, lado_mao):
    """
    Verifica o número de dedos levantados baseando-se na posição
    dos pontos fornecidos pelo MediaPipe.
    """
```

### Desenha informações na tela
```python
def desenha_mao(imagem, lado_mao, contador_dedos, largura):
    """
    Exibe o lado da mão detectada e o número de dedos levantados
    em um display sobre o vídeo em tempo real.
    """
```

### Configuração da captura e janela
```python
def configurar_video_e_janela():
    """
    Configurações para inicializar a captura de vídeo
    e criação da janela ajustável para saída.
    """
```

---

## Fluxo do Programa

1. Captura os quadros da webcam utilizando a biblioteca OpenCV.
2. Converte os quadros para o formato RGB para processar com o MediaPipe.
3. Identifica landmarks (pontos de referencia)das mãos no quadro.
4. Classifica o lado da mão e conta os dedos levantados.
5. Adiciona desenhos visuais e informações no quadro processado.
6. Exibe o resultado em tempo real.

---

## Exemplo de Saída Visual

### Exibição do Vídeo:
- Pontos (landmarks) são marcados em **verde**.
- Conexões entre os pontos (mapeamento da mão) aparecem em **azul**.
- **Retângulos na lateral** exibem:
    - O lado da mão detectada (Esquerda/Direita).
    - O número de dedos levantados.

---

## Pontos de Melhorias

Embora o funcionamento do programa seja estável, existem algumas melhorias planejadas:

### Problemas Atuais/Condições Específicas
- **Reconhecimento da palma da mão vs costas da mão**:
  - O funcionamento é perfeito quando as **palmas das mãos** estão voltadas para a câmera. No entanto, quando as **costas das mãos** são mostradas, há um problema especificamente relacionado ao **reconhecimento do dedão**.
  - O algoritmo atual presume a orientação da mão sem considerar a posição da palma versus costas da mão. Isso faz com que o dedão seja interpretado de forma incorreta em algumas situações.

### Solução sugerida:
- Desenvolver uma lógica adicional para identificar se a mão exibida está com a **palma aberta** ou as **costas voltadas para a câmera**. Isso pode ser feito avaliando as posições relativas dos landmarks.

---

## Extensibilidade

Este projeto pode ser expandido para várias funcionalidades adicionais, como:

- Reconhecimento de gestos específicos com base em posições das mãos.
- Controle por gestos para interação com sistemas.
- Integração com robótica ou aplicações IoT.

---

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos:

```text
├── main.py             # Código principal que executa a aplicação
├── README.md           # Documentação completa do projeto
└── requirements.txt    # Arquivo (opcional) para instalar dependências
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

---

## Possíveis Problemas e Soluções

### Problema: Erro ao abrir a câmera
```bash
Erro ao capturar o vídeo. 
```
- Solução: Certifique-se de que sua webcam está conectada corretamente e que a câmera não está sendo usada por outro software.

### Problema: Janela de vídeo não aparece
- Solução: Verifique se você possui OpenCV instalado corretamente executando:
  ```bash
  python -c "import cv2; print(cv2.__version__)"
  ```
  Caso a versão não seja exibida, instale o OpenCV novamente.

---

## Autor

Este projeto foi desenvolvido como um exemplo de aplicação em visão computacional utilizando **MediaPipe** e **OpenCV**.

Para dúvidas ou sugestões, sinta-se à vontade para contribuir ou entrar em contato.

Mais detalhes sobre **MediaPipe** podem ser encontrados na [documentação oficial](https://ai.google.dev/edge/mediapipe/solutions/guide?hl=pt-br).

---