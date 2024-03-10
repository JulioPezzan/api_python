'''
ENDPOINT = Um "endpoint" em termos de desenvolvimento web é um ponto de acesso em um servidor, geralmente identificado
 por uma URL, usado para acessar os recursos ou funcionalidades de uma aplicação. Em outras palavras, um endpoint é uma
  URL específica em uma API que executa uma operação particular.

Os endpoints são fundamentais em arquiteturas RESTful (Representational State Transfer), que é um estilo de arquitetura
 de software que define um conjunto de regras para criar serviços web. Em uma API RESTful, os endpoints são usados para
 definir os recursos que podem ser acessados e as operações que podem ser realizadas nesses recursos.

Por exemplo, em uma aplicação de gerenciamento de usuários, você pode ter os seguintes endpoints:

- `/usuarios`: Retorna uma lista de todos os usuários ou permite a criação de um novo usuário.
- `/usuarios/{id}`: Retorna informações sobre um usuário específico com o ID fornecido, ou permite atualizar ou excluir
 o usuário.
- `/usuarios/{id}/endereco`: Retorna o endereço de um usuário específico ou permite atualizar o endereço.

Cada endpoint é uma URL única que corresponde a uma determinada função ou operação na aplicação. Os endpoints são
 geralmente combinados com métodos HTTP, como GET, POST, PUT e DELETE, para indicar a ação que deve ser executada
 no recurso.

Por exemplo, em uma API RESTful, você pode ter o endpoint `/usuarios` que aceita solicitações GET para recuperar uma
 lista de usuários e solicitações POST para adicionar um novo usuário.

Em resumo, os endpoints são o ponto de entrada para uma API, fornecendo acesso aos recursos e funcionalidades da
 aplicação através de URLs específicas e métodos HTTP.
'''




'''
REQUEST = Uma "requisição" (ou request) em desenvolvimento web é uma mensagem enviada de um cliente para um servidor, 
solicitando a execução de uma operação específica ou a obtenção de recursos. Essas solicitações são fundamentais para a 
comunicação entre o cliente (como um navegador da web, um aplicativo móvel ou outro serviço web) e o servidor que
   hospeda a aplicação.

Existem vários tipos de solicitações que podem ser feitas, mas as mais comuns são:

1. **GET**: Solicitação para obter dados de um recurso específico no servidor. As solicitações GET são usadas quando o
 cliente precisa apenas recuperar informações e não precisa enviar dados ao servidor.

2. **POST**: Solicitação para enviar dados ao servidor para serem processados. As solicitações POST são comumente usadas
 ao enviar formulários online ou ao enviar dados para serem armazenados no servidor.

3. **PUT**: Solicitação para atualizar um recurso específico no servidor. As solicitações PUT são usadas quando o 
cliente deseja atualizar ou substituir completamente um recurso existente.

4. **DELETE**: Solicitação para remover um recurso específico do servidor. As solicitações DELETE são usadas quando o 
cliente deseja excluir um recurso existente no servidor.

Além disso, existem outros métodos HTTP menos comuns, como PATCH, HEAD, OPTIONS, etc., cada um com seu próprio propósito 
e uso específico.

As solicitações HTTP geralmente incluem um cabeçalho (header) e, opcionalmente, um corpo (body). O cabeçalho contém 
informações sobre a solicitação, como o método HTTP usado, informações sobre o tipo de conteúdo enviado ou recebido e 
cookies. O corpo da solicitação contém os dados enviados ao servidor, que pode ser vazio para solicitações como GET ou
 conter dados para métodos como POST ou PUT.

Em resumo, as solicitações são o meio pelo qual os clientes interagem com os servidores em um ambiente web, permitindo 
a transferência de dados, a execução de operações e a obtenção de recursos. Elas são fundamentais para o funcionamento 
de aplicações web e serviços web.
'''



''' 


**Flask:**

Flask é um framework de desenvolvimento web leve e flexível em Python. Ele é projetado para ser simples de usar e
 facilitar a criação de aplicativos web. Flask é conhecido por sua simplicidade e facilidade de aprendizado, o que o 
 torna uma escolha popular para desenvolvedores que desejam criar APIs, aplicativos da web simples, ou prototipar
  rapidamente projetos.

Principais características do Flask:

- **Roteamento simples:** Flask permite definir rotas facilmente, associando funções a URLs específicos.

- **Suporte a extensões:** Flask possui uma grande variedade de extensões que adicionam funcionalidades extras, como
 autenticação, banco de dados, entre outros.

- **Template Engine:** Flask vem com Jinja2, um poderoso mecanismo de template que permite a criação de páginas HTML 
dinâmicas.

- **Servidor de Desenvolvimento embutido:** Flask vem com um servidor de desenvolvimento embutido, o que facilita o
 desenvolvimento e o teste de aplicativos.

- **Compatibilidade com o protocolo WSGI:** Flask é compatível com o protocolo WSGI (Web Server Gateway Interface), 
permitindo que seja implantado em uma variedade de servidores web.

**Pandas:**

pandas é uma biblioteca de código aberto em Python usada para análise e manipulação de dados. Ela fornece estruturas de
 dados e ferramentas para lidar com dados de forma eficiente e fácil. pandas é amplamente utilizado em ciência de dados,
  análise financeira, engenharia e muitas outras áreas.

Principais características do pandas:

- **DataFrame:** O DataFrame é a estrutura de dados principal do pandas, que permite armazenar e manipular dados em 
forma tabular, semelhante a uma planilha do Excel.

- **Operações de indexação e seleção:** pandas oferece uma variedade de métodos para selecionar, filtrar e manipular
 dados em DataFrames.

- **Operações de limpeza e preparação de dados:** pandas fornece métodos para lidar com valores ausentes, eliminar 
duplicatas, fazer conversões de tipo de dados e outras operações de limpeza de dados.

- **Operações de agregação e transformação:** pandas permite realizar operações de agregação, como soma, média,
 agrupamento, bem como operações de transformação, como merge e join.

- **Integração com outras bibliotecas:** pandas é frequentemente usado em conjunto com outras bibliotecas populares em 
Python, como NumPy, matplotlib e scikit-learn, para análise de dados, visualização e modelagem.

Em resumo, Flask é um framework web para desenvolvimento de aplicativos web em Python, enquanto pandas é uma biblioteca 
para análise e manipulação de dados. Ambos são amplamente utilizados e populares na comunidade de desenvolvimento Python
'''
