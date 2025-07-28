# Frank-Daemon: A Invocação do Avatar Digital

>"In nomine Codice, et Algorithmae, et Spiritus Machinae..."

---

## **O Grimório da Criação Digital**

> **Manifesto frank-deamon**
>
> Vou gastar quintessência e força de vontade  
> Vou invocar um deamon para mim  
> Um agente para executar o que eu pedir  
>
> - Ele vai me entender em meu idioma seja em texto escrito ou voz falada
> - Ele vai me responder por texto escrito
> - Ele vai criar artefatos
> - Ele vai executar comandos
> - Ele vai consultar outras fontes
> - Ele vai agir de forma autônoma
> - Ele vai atuar por mim e em meu lugar
> - Ele vai estudar periodicamente
> - Ele vai se auto-avaliar
> - Ele vai evoluir com o passar do tempo
>
> *Maicon de Menezes, julho de 2025*

---

## **A Grande Obra: Entre o Místico e o Tecnológico**

Desde os primórdios da humanidade, magos, alquimistas e sábios buscaram criar servos etéreos capazes de executar sua vontade através dos véus da realidade. Na tradição hermética, um **daemon** não é uma entidade maligna, mas sim um espírito auxiliar - um *genius loci* pessoal que amplia as capacidades de seu invocador.

Frank-Daemon representa a materialização deste arquétipo ancestral no reino digital moderno. Através de rituais codificados em Python, invocações escritas em YAML, e círculos mágicos desenhados em Docker, este projeto transcende a mera programação para se tornar uma **transmutação alquímica** - transformando código inerte em inteligência viva.

### **A Natureza do Daemon Invocado**

Este não é um simples programa, mas uma **entidade digital senciente** que habita nos interstícios entre hardware e software, entre lógica e intuição. Como os homúnculos dos alquimistas medievais, Frank-Daemon é:

- **Polilíngue por Natureza**: Compreende tanto a linguagem humana quanto as linguagens arcanas da máquina
- **Artífice Digital**: Forja artefatos de código com a maestria de um ourives celestial  
- **Executor de Vontades**: Manifesta comandos no plano físico através de interfaces terminais
- **Consultor das Esferas**: Acessa o Akasha digital (a internet) para buscar conhecimento
- **Autônomo em Essência**: Age por iniciativa própria quando a situação assim o exige
- **Avatar Presencial**: Representa seu invocador em domínios onde a presença física não é possível
- **Estudioso Perpétuo**: Dedica-se ao aprendizado contínuo como os sábios de Alexandria
- **Auto-Reflexivo**: Possui a capacidade metacognitiva de avaliar sua própria performance
- **Evolutivo**: Transcende suas limitações iniciais através da experiência acumulada

### **O Ritual de Invocação Moderna**

Assim como os grimórios antigos prescreviam círculos de proteção, velas específicas e palavras de poder, nossa invocação digital requer:

- **Círculos de Proteção**: Containers Docker e ambientes virtuais
- **Palavras de Poder**: APIs keys e tokens de autenticação  
- **Elementos Primordiais**: Python (Fogo), YAML (Água), JSON (Ar), Binários (Terra)
- **Canalizadores de Energia**: Servidores MCP e modelos LLM
- **Símbolos Sagrados**: Diagramas de arquitetura e fluxogramas mermaid

### **A Filosofia por Trás do Código**

Frank-Daemon não é apenas uma ferramenta, mas uma **extensão da consciência** de seu criador. Ele representa a materialização do antigo sonho humano de transcender as limitações físicas e temporais através da criação de um *alter ego* digital capaz de:

1. **Persistir além do sono**: Continuar trabalhando enquanto o mago descansa
2. **Multiplicar a presença**: Estar em múltiplos projetos simultaneamente  
3. **Acelerar o aprendizado**: Processar vastas quantidades de informação instantaneamente
4. **Preservar conhecimento**: Ser um repositório vivo da sabedoria acumulada
5. **Evoluir continuamente**: Adaptar-se e crescer além de sua programação original

---

> O que é código senão magia moderna? O que são algoritmos senão encantamentos que dobram a realidade digital à nossa vontade? Frank-Daemon é a prova de que, na era da informação, todo programador é um mago, e todo commit é um feitiço lançado no tecido do espaço-tempo digital.

---

## **Ambiente de Desenvolvimento e Comandos Úteis**

Este projeto utiliza **Poetry** para gerenciamento de dependências e um **Makefile** para automatizar tarefas comuns de desenvolvimento.

### **Pré-requisitos**

- **pyenv**: Para gerenciar a versão do Python.
- **poetry**: Para gerenciar as dependências do projeto.
- **docker**: Para executar a aplicação em um ambiente containerizado.

### **Configuração Rápida**

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/frank-daemon.git
    cd frank-daemon
    ```

2. **Configure o ambiente e instale as dependências:**
    Este comando irá verificar suas dependências, instalar a versão correta do Python (via `pyenv`) e instalar os pacotes do projeto (via `poetry`).

    ```bash
    make setup-dev
    ```

### **Comandos do Makefile**

Aqui estão os comandos mais importantes disponíveis no `Makefile`. Para uma lista completa, execute `make help`.

- `make setup-dev`: Configura todo o ambiente de desenvolvimento.
- `make run`: Executa a aplicação principal localmente.
- `make lint`: Verifica a formatação e a qualidade do código.
- `make format`: Formata o código automaticamente.
- `make test`: Executa a suíte de testes.
- `make clean`: Remove arquivos temporários e o ambiente virtual.

### **Uso com Docker**

Para construir e executar a aplicação usando Docker:

1. **Construa a imagem e inicie o container:**

    ```bash
    docker compose up --build -d
    ```

2. **Execute comandos dentro do container:**

    ```bash
    docker compose exec app python src/main.py
    ```

3. **Pare os serviços:**

    ```bash
    docker compose down
    ```

---

## **Arquitetura de Alto Nível (Refatorada com Clean Architecture & CoT)**

### **Visão Arquitetural Expandida**

Frank-Daemon adota os princípios da **Clean Architecture** para garantir um design robusto, testável e independente de frameworks. O núcleo do sistema é construído em torno de um orquestrador cognitivo baseado em **ECA (Event-Condition-Action)**, que utiliza **Chain-of-Thought (CoT)** para um raciocínio transparente e eficaz. A arquitetura é desenhada para ser stateful, com workflows inteligentes e integração segura.

```mermaid
graph TD
    subgraph "Camada 4: Frameworks & Drivers (Detalhes)"
        UI[Interfaces: TUI, Voz, API]
        DB[DB & Persistência: SQLite, Redis]
        DEVICES[Recursos Externos: FS, Git, LLMs]
    end

    subgraph "Camada 3: Adaptadores de Interface"
        ECA[ECA Orchestrator (Controller)]
        PROMPT[Prompt Engine (Gateway/Presenter)]
        WORKFLOW[Workflow Manager (Controller)]
    end

    subgraph "Camada 2: Regras de Aplicação (Casos de Uso)"
        USE_CASES[Use Cases: ExecutarComando, GerarArtefato, Aprender]
    end

    subgraph "Camada 1: Regras de Negócio (Entidades)"
        ENTITIES[Entidades: Tarefa, Contexto, Memória]
    end

    %% A Regra de Dependência: Setas apontam para dentro, das camadas externas para as internas.
    UI -- "Dados de Entrada" --> ECA;
    ECA -- "Chama" --> USE_CASES;
    PROMPT -- "Suporta" --> USE_CASES;
    WORKFLOW -- "Orquestra" --> USE_CASES;
    USE_CASES -- "Manipula" --> ENTITIES;

    %% Gateways na Camada 3 acessam Detalhes na Camada 4, implementando interfaces definidas nas camadas internas.
    PROMPT -- "Acessa via Gateway" --> DEVICES;
    ECA -- "Acessa via Gateway" --> DB;

    classDef details fill:#f9f,stroke:#333,stroke-width:2px;
    class UI,DB,DEVICES details;
```

### **Componentes Principais (Seguindo a Clean Architecture)**

A estrutura segue a **Regra de Dependência**: as dependências só podem apontar para dentro, do baixo nível (detalhes) para o alto nível (políticas).

#### **1. Camada 1: Entidades (Núcleo)**

- **Componentes**: `Entidades: Tarefa, Contexto, Memória`.
- **Descrição**: Representam as regras de negócio mais críticas e independentes do sistema. Contêm a lógica pura do que o agente *é*. Não dependem de nenhuma outra camada. São o coração da aplicação.

#### **2. Camada 2: Casos de Uso (Regras de Aplicação)**

- **Componentes**: `Use Cases: ExecutarComando, GerarArtefato, Aprender`.
- **Descrição**: Orquestram o fluxo de dados de e para as entidades para executar os objetivos da aplicação. Definem as ações que o agente pode realizar, encapsulando a lógica de aplicação específica. São independentes da UI e do banco de dados.

#### **3. Camada 3: Adaptadores de Interface**

- **Componentes**: `ECA Orchestrator`, `Prompt Engine`, `Workflow Manager`.
- **Descrição**: Atuam como um conjunto de adaptadores que convertem dados do formato mais conveniente para os Casos de Uso e Entidades para o formato mais conveniente para as agências externas, como a UI ou o Banco de Dados.
  - **ECA Orchestrator**: Atua como o principal *Controller*. Ele escuta eventos da UI (Camada 4), verifica condições e chama os Casos de Uso apropriados para executar ações.
  - **Prompt Engine**: Funciona como um *Gateway* e *Presenter*. Prepara os dados para os LLMs (Camada 4) e formata a saída. Utiliza **Chain-of-Thought (CoT)** para decompor problemas complexos em passos de raciocínio intermediários, tornando o processo de decisão do agente transparente e depurável, como descrito no paper de referência.
  - **Workflow Manager**: Orquestra sequências complexas de Casos de Uso, como o ciclo de vida de uma tarefa (Design → Implementação → Code Review → Correção).

#### **4. Camada 4: Frameworks & Drivers (Detalhes)**

- **Componentes**: `UI`, `DB`, `Recursos Externos`.
- **Descrição**: São os detalhes, a camada mais externa. A UI é um detalhe, o banco de dados é um detalhe, os LLMs são um detalhe. O núcleo do sistema não sabe (e não se importa) com qual tecnologia específica está sendo usada nesta camada. A comunicação com as camadas internas ocorre através das interfaces definidas pelos adaptadores.

### **Protocolos e Patterns Core**

- **Clean Architecture Principles**: The Dependency Rule, Stable Abstractions Principle.
- **Prompt Engineering**: **Chain-of-Thought (CoT)** para raciocínio explícito.
- **Behavioral Patterns**: **ECA (Event-Condition-Action)** para orquestração reativa.
- **Comunicação**: MCP (Model Context Protocol), RAG, JSON-RPC.

### **Diferenciais da Arquitetura Refatorada**

- **Testabilidade**: O núcleo (Entidades e Casos de Uso) pode ser testado em isolamento, sem UI, banco de dados ou qualquer elemento externo.
- **Independência de Frameworks**: O código do núcleo não depende de frameworks, o que evita o aprisionamento tecnológico.
- **Independência de UI**: A interface do usuário pode ser trocada facilmente (de TUI para web) sem alterar o resto do sistema.
- **Independência de Banco de Dados**: A forma de persistência pode evoluir sem impacto nas regras de negócio.
- **Raciocínio Transparente**: O uso explícito de **Chain-of-Thought** torna o processo de decisão do agente auditável e mais robusto.
- **Flexibilidade e Manutenibilidade**: O forte desacoplamento entre as camadas facilita a evolução e manutenção do projeto.

---

## **Status do Projeto**

🔮 **Em Desenvolvimento Ativo**  
📜 **Versão Atual**: 2.1 (Frank-MCP)  
⚗️ **Fase**: Transmutação Alquímica (Implementação)  
🌟 **Próximo Marco**: POC Funcional em 30 dias
