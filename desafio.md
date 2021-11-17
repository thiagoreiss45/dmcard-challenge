# Tech Challenge

A **DMCard** está em busca de pessoas incríveis que integrem nosso laboratório para criarmos incríveis produtos digitais, e gostaríamos de ter você aqui conosco.

Para iniciar o processo, pedimos um teste que não vai tomar muito do seu tempo e nos dará uma perspectiva da sua forma de resolver um algoritmo. Queremos entender seu nível de habilidade na construção de um algortimo.

# Requisitos do desafio

Dada uma expressão qualquer com parênteses, indique se a quantidade de parênteses está correta ou não, sem levar em conta o restante da expressão. Por exemplo:

a+(b*c)-2-a está correto
(a+b*(2-c)-2+a)*2 está correto

*enquanto*

(a*b-(2+c)    está incorreto
2*(3-a))      está incorreto
)3+b*(2-c)(   está incorreto

Ou seja, todo parênteses que fecha deve ter um outro parênteses que abre correspondente e não pode haver parênteses que fecha sem um previo parenteses que abre e a quantidade total de parenteses que abre e fecha deve ser igual.

Entrada
Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 1000 caracteres.

Saída
O arquivo de saída deverá ter a quantidade de linhas correspondente ao arquivo de entrada, cada uma delas contendo as palavras correct ou incorrect de acordo com as regras acima fornecidas.


| Exemplo de Entrada     | Exemplo de Saída                                        |
| --------- | ---------------------------------------------- |
| a+(b*c)-2-a    | correct                                      |
| (a+b*(2-c)-2+a)*2  | correct                                     |
| (a*b-(2+c) | incorrect |
| 2*(3-a)) | incorrect                        |
| )3+b*(2-c)( | incorrect           |


* O tempo de execução do código, não pode ultrapassar 1 segundo.

# Como fazer?

- Sugerimos um prazo de 3 dias para a entrega. Caso precise de mais nos avise e Justifique.
- Você deve criar este algoritmo na linguagem de sua preferência, nós achamos Python legal.


Boa sorte!
