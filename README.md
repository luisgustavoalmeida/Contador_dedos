# Contador de Dedos - Detecção de Mãos com MediaPipe e OpenCV

Este projeto tem como objetivo detectar mãos e contar o número de dedos levantados em tempo real utilizando as bibliotecas **MediaPipe** e **OpenCV**.

Este repositório contém um aplicativo desenvolvido em Python que aplica conceitos de **visão computacional** para capturar e processar vídeos em tempo real por meio de uma **webcam**, detectando mãos e exibindo quantos dedos estão levantados para cada mão identificada.

O software é uma demonstração prática da tecnologia **MediaPipe Hands**, uma solução de aprendizado de máquina para localização e rastreamento de landmarks das mãos.

![Interface Gráfica](Imagem%20interface%20grafica.png)

Confira o vídeo de demonstração do projeto clicando no link abaixo:

[Demonstração - Contagem de Dedos](Demonstração%20contagem%20de%20dedos.mp4)

---

## Descrição Geral

O script principal (main.py) utiliza técnicas de **visão computacional** para capturar imagens da webcam, identificar mãos no quadro e contar de forma precisa o número de dedos levantados para cada mão detectada. A aplicação é construída utilizando o **MediaPipe Hands**, que fornece landmarks (pontos de referência) detalhados das mãos.

---

## Funcionalidades e Mudanças Recentes

- **Detecção de Múltiplas Mãos**: O sistema suporta a detecção de até **duas mãos simultâneas**.
- **Contagem de Dedos**: Baseia-se na posição dos dedos e orientações das landmarks para identificar dedos levantados.
- **Classificação da Mão (Esquerda/Direita)**: Determina se a mão detectada é a esquerda ou a direita.

- **Renderização em Vídeo**:
    - Desenha landmarks (pontos) e conexões (linhas) das mãos.
    - Mostra o lado da mão e o número de dedos levantados diretamente no vídeo.

- **Interface Gráfica (interface.py)**:
    - Adicionada uma interface gráfica para controle do sistema, permitindo ajustar configurações em tempo real.

- **Renderização em Vídeo**:
    - Resolução da captura.
    - Tamanho da janela de vídeo.

- **Configurações Personalizáveis**:
    - Resolução da captura.
    - Tamanho da janela de vídeo.
    - Escolha de gerar log.


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
   git clone https://github.com/luisgustavoalmeida/Contador_dedos.git
   cd contador-dedos
   ```

2. Verifique se sua webcam está conectada ao dispositivo.

3. Para iniciar a interface, execute:
   ```bash
   python interface.py
   ```

4. Caso prefira executar sem a interface, execute:
   ```bash
   python processar_video.py
   ```

5. A interface de vídeo será exibida mostrando as mãos detectadas. O número de dedos levantados aparecerá sob um retângulo.

6. Para **fechar o programa**, pressione a tecla `ESC`.

---

## Configurações Suportadas

Na interface gráfica implementada no arquivo `interface.py`, é possível configurar e executar as seguintes ações:

- **Tamanho da tela**.
- **Resolução**.
- **Iniciar a execução**.
- **Interromper a execução**.
- **Escolha de gerar log**


Essas configurações podem ser ajustadas para personalizar o comportamento do programa, como alterar a resolução de saída da câmera ou o estilo visual da renderização da janela.

---

## Principais Funções e Melhorias

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
  - O funcionamento é perfeito quando as **palmas das mãos** estão voltadas para a câmera. Melhorias no algoritmo agora permitem a detecção correta das **costas das mãos**, solucionando problemas no **reconhecimento do dedão**.
  - O algoritmo atual presume a orientação da mão sem considerar a posição da palma versus costas da mão. Isso faz com que o dedão seja interpretado de forma incorreta em algumas situações.

### Resolução:
- Implementado um algoritmo que identifica se a mão exibida está com a **palma aberta** ou as **costas voltadas para a câmera**, analisando as posições relativas dos landmarks. Essa lógica agora está ativa por padrão.

---

## Extensibilidade e Futuras Melhorias

Este projeto pode ser expandido para várias funcionalidades adicionais, como:

- Reconhecimento de gestos específicos com base em posições das mãos.
- Controle por gestos para interação com sistemas.
- Integração com robótica ou aplicações IoT.

---

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos e módulos:

```text
├── processar_video.py  # Código principal que executa a aplicação
├── README.md           # Documentação completa do projeto
├── interface.py        # Módulo que gerencia a interface gráfica e ajustes em tempo real
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

Contribuições para o módulo `interface.py` e o reconhecimento das costas das mãos foram adicionadas na versão atual.

---