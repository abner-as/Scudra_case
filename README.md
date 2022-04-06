# Scudra_case

Case de teste utilizando os requisitos enviados.

Instruções:
1. Ir para o diretorio onde esta o "dockerfile"
2. Executar "docker build --tag image_name ." obs: trocar o "image_name" para o desejado.
3. Executar "docker run -p 8000:8000 image_name"
4. Após estar disponível o container, já é possivel realizar chamadas para ingestão de eventos("/ingestion").
5. Arquivo de exemplo "sample_teste.py"

Considerações:

Os recursos aplicados foram simplicistas, mas em um ambiente real haveriam uma serie de itens adicionais/padrões a serem aplicados.

Exemplo: um topico de Kafka ou Pub/Sub(GCp) poderia ser utilizado para garantir que nenhuma mensagem se perca ou para controle de erros.

 
