# 🐍 Exercícios Práticos de Python

> Lista de exercícios organizados por nível para praticar Python do básico ao avançado.

---

## 🗂️ Índice

- [🟢 Nível 1 – Iniciante](#-nível-1--iniciante)
- [🟡 Nível 2 – Intermediário](#-nível-2--intermediário)
- [🔵 Nível 3 – Avançado](#-nível-3--avançado)
- [🏆 Desafio Extra](#-desafio-extra--projeto-para-portfólio)
- [📊 Resumo dos Níveis](#-resumo-dos-níveis)

---

## 🟢 Nível 1 – Iniciante

> **Objetivo:** Dominar entrada de dados, operações básicas e estruturas condicionais.

---

### 1️⃣ Calculadora Simples

Crie um programa que:

- Solicite dois números ao usuário
- Pergunte qual operação deseja realizar: `+`, `-`, `*` ou `/`
- Exiba o resultado da operação

**Conceitos:** `input`, `float`, `if/elif/else`

```python
# Exemplo de uso
Digite o primeiro número: 10
Digite o segundo número: 4
Operação (+, -, *, /): *
Resultado: 40.0
```

---

### 2️⃣ Verificador de Número Par ou Ímpar

- Solicite um número inteiro
- Informe se ele é par ou ímpar

**Dica:** Utilize o operador `%` (módulo)

```python
# Exemplo de uso
Digite um número: 7
O número 7 é ÍMPAR.
```

---

### 3️⃣ Conversor de Temperatura

- Converta uma temperatura de Celsius para Fahrenheit
- **Fórmula:** `F = (C × 9/5) + 32`

```python
# Exemplo de uso
Digite a temperatura em Celsius: 100
100°C equivale a 212.0°F
```

---

## 🟡 Nível 2 – Intermediário

> **Objetivo:** Trabalhar com laços de repetição, listas e dicionários.

---

### 4️⃣ Tabuada com `while`

- Solicite um número ao usuário
- Exiba sua tabuada de 1 a 10 utilizando o `while`

```python
# Exemplo de uso
Digite um número: 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

---

### 5️⃣ Cadastro de Alunos

Crie um sistema que:

- Permita cadastrar vários alunos e suas notas
- Armazene os dados em um dicionário
- Exiba:
  - Lista de alunos
  - Média da turma
  - Alunos aprovados (nota ≥ 7)

**Conceitos:** `dict`, `for`, `sum`, `len`

```python
# Exemplo de uso
Alunos cadastrados: Ana (8.5), Bruno (6.0), Carla (9.0)
Média da turma: 7.83
Aprovados: Ana, Carla
```

---

### 6️⃣ Jogo de Adivinhação

- Gere um número aleatório entre 1 e 100 usando `random`
- O usuário deve tentar adivinhar o número
- Informe se o palpite é maior ou menor
- Mostre o número de tentativas ao final

```python
# Exemplo de uso
Tente adivinhar o número (1–100): 50
Muito alto! Tente novamente: 25
Muito baixo! Tente novamente: 37
Acertou em 3 tentativas!
```

---

## 🔵 Nível 3 – Avançado

> **Objetivo:** Introduzir funções, manipulação de arquivos e menus interativos.

---

### 7️⃣ Sistema de Controle de Estoque

Crie um programa com menu que permita:

```
1. Adicionar produto (nome e quantidade)
2. Remover produto
3. Atualizar quantidade
4. Listar produtos
5. Sair
```

**Conceitos:** `dict`, `while`, funções

---

### 8️⃣ Agenda de Contatos com Arquivo

Desenvolva uma agenda que:

- Permita adicionar, listar e buscar contatos
- Salve os dados em um arquivo `contatos.txt`
- Carregue os dados ao iniciar o programa

**Conceitos:** `open()`, leitura e escrita de arquivos

---

### 9️⃣ Simulação de Caixa Eletrônico

O programa deve:

- Solicitar um PIN para acesso
- Permitir consultar saldo, depositar e sacar
- Validar saldo insuficiente
- Utilizar funções para cada operação

```python
# Exemplo de uso
Digite seu PIN: ****
Bem-vindo!
[1] Consultar saldo  [2] Depositar  [3] Sacar  [4] Sair
```

---

## 🏆 Desafio Extra – Projeto para Portfólio

### 🔟 Sistema de Biblioteca

Funcionalidades:

- Cadastrar livros
- Emprestar e devolver livros
- Listar livros disponíveis e emprestados
- Salvar dados em arquivo

> 💡 Este projeto é ideal para compor seu portfólio no GitHub. Tente implementar sozinho antes de buscar referências!

---

## 📊 Resumo dos Níveis

| Nível | Habilidades Trabalhadas |
|---|---|
| 🟢 Iniciante | `input`, `print`, `if/else`, operações matemáticas |
| 🟡 Intermediário | `while`, `for`, `list`, `dict`, `random` |
| 🔵 Avançado | Funções, arquivos, menus interativos |
| 🏆 Portfólio | Integração de todos os conceitos em projetos completos |

---

## 🚀 Como Praticar

1. Leia o enunciado com atenção
2. Tente resolver **sem ver exemplos** primeiro
3. Teste com diferentes entradas (incluindo casos inválidos)
4. Refatore o código para deixá-lo mais limpo após funcionar

---

<div align="center">
  Bons estudos! 🐍✨
</div>
