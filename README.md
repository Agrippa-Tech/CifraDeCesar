# Cifra de César - Implementação Didática em Python

Implementação educacional da Cifra de César sem uso de funções modulares, desenvolvida para compreensão profunda do modelo criptográfico clássico e dos fundamentos da linguagem Python.

## Sobre

Este projeto apresenta uma implementação completa da Cifra de César, um dos algoritmos de criptografia por substituição mais antigos e conhecidos. A abordagem pedagógica adotada deliberadamente evita o uso de funções modulares, permitindo visualizar explicitamente cada etapa do processo criptográfico e dos mecanismos fundamentais do Python.

## Fundamentação Teórica

A Cifra de César é um método de criptografia por substituição onde cada letra do texto original é deslocada um número fixo de posições no alfabeto. Matematicamente:

- **Encriptação**: `E(x) = (x + k) mod 26`
- **Decriptação**: `D(x) = (x - k) mod 26`

Onde:
- `x` = posição da letra no alfabeto
- `k` = chave de deslocamento (0-25)
- `mod 26` = operação modular para manter o resultado dentro do alfabeto

## Abordagem Didática

### Por que sem funções modulares?

A implementação linear e sequencial foi escolhida intencionalmente para:

1. **Visualização do Fluxo**: Permite acompanhar cada operação passo a passo
2. **Compreensão de Conceitos**: Facilita o entendimento de conversões ASCII, operações modulares e manipulação de strings
3. **Aprendizado de Python**: Demonstra estruturas de controle, loops, tratamento de exceções e manipulação de entrada/saída
4. **Transparência Algorítmica**: Torna explícito cada estágio do processo criptográfico

> **Nota Importante**: Esta abordagem é exclusivamente didática. Em ambientes de produção, recomenda-se fortemente a modularização do código através de funções e classes.

## Funcionalidades

O programa oferece cinco operações principais:

### 1. Encriptar Mensagem
Converte texto claro em texto cifrado utilizando uma chave especificada pelo usuário.

**Processo**:
- Recebe mensagem em texto claro (X1)
- Aplica chave de deslocamento K (0-25)
- Gera texto cifrado (Y)

### 2. Decriptar Mensagem
Reverte o processo de encriptação, convertendo texto cifrado de volta ao texto original.

**Processo**:
- Recebe texto cifrado (Y)
- Aplica chave de deslocamento K no sentido inverso
- Recupera texto original (X2)

### 3. Quebrar Cifra Manualmente
Modo de desafio educacional que gera frases aleatórias cifradas.

**Dinâmica**:
- Sistema gera frase aleatória e cifra com chave desconhecida
- Usuário tenta decifrar manualmente
- Feedback imediato sobre acerto/erro

### 4. Testar Todas as Chaves
Implementação de ataque por força bruta, testando sistematicamente todas as 26 chaves possíveis.

**Aplicação**:
- Demonstra vulnerabilidade da Cifra de César
- Ilustra conceito de espaço de chaves reduzido
- Permite identificação visual da mensagem original

### 5. Sair
Encerra o programa de forma controlada.

## Estrutura do Código

### Componentes Principais

**Dicionário de Componentes de Frases**:
```python
componentes_frases_cifradas = {
    'sujeito': [...],
    'verbo': [...],
    'complemento': [...]
}
```
Utilizado para geração de frases aleatórias no modo de quebra manual.

### Mecanismo de Conversão

O código utiliza manipulação ASCII para operações criptográficas:

1. **Determinação da base**: `ord('A')` ou `ord('a')` dependendo do caso
2. **Conversão letra → número**: `ord(letra) - conversao_alpha_ascii`
3. **Aplicação da chave**: `+ chave_K` ou `- chave_K`
4. **Operação modular**: `% 26`
5. **Conversão número → letra**: `chr(...)`

### Sistema de Segurança

**Limitador de Tentativas**:
- 4 tentativas iniciais para entrada válida
- Penalidade temporal de 30 segundos antes da última tentativa
- Encerramento automático após esgotamento

## Conceitos de Python Demonstrados

- ✓ Estruturas de repetição (`while`, `for`)
- ✓ Estruturas condicionais (`if`, `elif`, `else`)
- ✓ Tratamento de exceções (`try`, `except`)
- ✓ Manipulação de strings
- ✓ Operações com caracteres ASCII (`ord`, `chr`)
- ✓ Dicionários e listas
- ✓ Entrada/saída de dados (`input`, `print`)
- ✓ Formatação de strings (f-strings)
- ✓ Módulos da biblioteca padrão (`random`, `time`, `os`)
- ✓ Operações modulares
- ✓ Validação de entrada

## Requisitos

- Python 3.6 ou superior
- Ambiente de terminal/console
- Nenhuma dependência externa

## Como Executar

```bash
python cifra_cesar.py
```

## Limitações Educacionais Reconhecidas

Como implementação didática, o código apresenta características que seriam inadequadas em produção:

1. **Repetição de código**: Lógica de cifragem duplicada em múltiplos blocos
2. **Acoplamento**: Toda lógica concentrada em um único arquivo
3. **Nomenclatura**: Variáveis em português para facilitar compreensão inicial
4. **Ausência de testes**: Não inclui suite de testes automatizados
5. **Modularização**: Ausência intencional de funções reutilizáveis

## Conceitos Criptográficos Ilustrados

- **Criptografia Simétrica**: Mesma chave para cifrar e decifrar
- **Substituição Monoalfabética**: Cada letra sempre substituída pela mesma letra cifrada
- **Vulnerabilidade a Força Bruta**: Espaço de chaves limitado (26 possibilidades)
- **Preservação de Estrutura**: Espaços e pontuação mantidos
- **Case-sensitivity**: Tratamento diferenciado para maiúsculas e minúsculas

## Possíveis Extensões Educacionais

Para estudantes que dominarem este código:

1. Refatorar usando funções modulares
2. Implementar análise de frequência de letras
3. Adicionar suporte a outros alfabetos
4. Criar interface gráfica (GUI)
5. Implementar cifras relacionadas (ROT13, Cifra de Vigenère)
6. Adicionar testes unitários
7. Desenvolver versão orientada a objetos

## Objetivo Pedagógico

Proporcionar compreensão sólida de:
- Fundamentos de criptografia clássica
- Manipulação de caracteres em Python
- Estruturas de controle e fluxo de programa
- Tratamento de erros e validação de entrada
- Operações matemáticas modulares aplicadas

## Licença

Este código é dedicado a fins educacionais. Sinta-se livre para estudar, modificar e utilizar como base para aprendizado de Python e criptografia básica.

---

**Nota Final**: Este projeto representa uma etapa fundamental no aprendizado de programação e criptografia. A compreensão profunda destes conceitos básicos é essencial antes de avançar para implementações mais sofisticadas e modularizadas.