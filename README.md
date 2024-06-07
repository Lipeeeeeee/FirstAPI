# FirstAPI

## Projeto

&emsp;&emsp;O projeto proposto, se tratou de construir uma API assíncrona de competição de crossfit, tendo como modelos Atletas, Categorias, e Centros de Treinamento, utilizando o FastAPI, e outras ferramentas que se integram muito bem ao framework para auxiliar, e ao final, adicionar mais algumas funcionalidades para testar o estudo, determinação, aprendizado, e desenvolvimento de código do desafiado.<br>
&emsp;&emsp;A construção foi um grande obstáculo para mim, que nunca havia tido nenhum contato com APIs ou algo do tipo, porém com foco e dedicação consegui passar e concluir o desafio logo em seguida, vou te contar como.<br>
&emsp;&emsp;O primeiro passo que tive foi criar meu ambiente virtual que chamei de "firstAPI", e logo após instalar os pacotes necessários para começar a produção:<br>

### [FastAPI](https://fastapi.tiangolo.com/)

&emsp;&emsp;O FastAPI é um framework para criação de APIs em Python, conhecido por ser veloz, eficiente, intuitivo e robusto por ter uma documentação simples e fácil de se ler, tendo componentes que facilitam na montagem e principalmente no aprendizado, por ser uma ferramenta fácil de se usar.

### [Uvicorn](https://www.uvicorn.org/)

&emsp;&emsp;O Uvicorn é um servidor ASGI, que me possibilitou subir minha aplicação para o servidor local da minha máquina, assim me permitindo enxergar por uma interface gráfica o funcionamento do meu projeto, facilitando a localização de erros e bugs para corrigir. 

### [SqlAlchemy](https://docs.sqlalchemy.org/en/20/)

&emsp;&emsp;O SqlAlchemy é um framework de ORM, que utilizei para facilitar a parte de conexão com o banco de dados e principalmente no mapeamento dos dados para o banco, convertendo dados do banco para os tipos Python e vice-versa. Com a ajuda do [Alembic](https://alembic.sqlalchemy.org/en/latest/), também me foi possível realizar as migrações necessárias dos modelos.

### [Pydantic](https://docs.pydantic.dev/latest/)

&emsp;&emsp;O Pydantic é uma biblioteca Python que utilizei para as validações de dados do meu projeto, que é uma parte importantíssima para que os dados se mantenham seguros e do jeito que precisam ser, além de se integrar com o FastAPI, que ajuda na validação de dados mais específicos.

## Desafio proposto

&emsp;&emsp;Após a construção da firstAPI, agora só foi preciso concluir os desafios propostos no projeto, desafios esses que foram:

1. Adicionar query parameters de "nome" e "CPF" no endpoint GET all de Atleta
2. Customizar o retorno do endpoint GET all de Atleta para que mostre apenas, Nome, Categoria e Centro de Treinamento do Atleta
3. Dinamizar a mensagem de retorno para um erro de integridade de dados, retornando um HTTP 303 (SEE OTHER), e uma mensagem, como exemplo: "Já existe um Atleta cadastrado com o cpf: {x}"
4. Adicionar paginação utilizando a biblioteca fastapi-pagination

&emsp;&emsp;E após a conclusão dos desafios, este foi o resultado final da primeira API que eu construí!

## Considerações finais

&emsp;&emsp;Gostaria de deixar registrado a minha felicidade em terminar este projeto, pois consegui aprender muito com esta oportunidade, e vejo que me sai muito bem, pois nunca tive contato com APIs ou algo do tipo e absorvi grande conhecimento, transformando-o em aprendizado e criando este projeto, passei por dificuldades e estresse durante o desenvolvimento, porém não desisti e consegui mais uma realização para povoar meu portfólio e aprender mais.

## Outras ferramentas utilizadas

1. [docker-compose](https://docs.docker.com/compose/) - Utilizado para estabelecer a conexão com o banco
2. [DBeaver](https://dbeaver.com/docs/dbeaver/) - Utilizado para gerenciar o banco de dados
3. [MakeFile](https://embarcados.com.br/introducao-ao-makefile/) - Utilizado para sobrescrever comandos extensos
4. [Postman](https://www.postman.com/product/what-is-postman/) - Utilizado para adicionar os query parameters e testar a API
5. [fastapi-pagination](https://uriyyo-fastapi-pagination.netlify.app/) - Utilizado para paginação dos dados
