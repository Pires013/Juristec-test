/* 
  Objetivo: Listar processos abertos em 2023 para clientes de SP.
*/
SELECT c.nome, p.assunto, p.data_abertura
FROM clientes c
INNER JOIN processos p ON c.id_cliente = p.id_cliente
WHERE c.estado = 'SP'
AND p.data_abertura BETWEEN '2023-01-01' AND '2023-12-31'