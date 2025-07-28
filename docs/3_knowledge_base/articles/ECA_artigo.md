# Engenharia de Contexto Aumentada (ECA): O Fim da Amnésia nos LLMs

Betinho Timoteo

Como a arquitetura ECA utiliza Orquestração, Memória Híbrida e Achatamento de Contexto para dar superpoderes de julgamento aos Grandes Modelos de Linguagem.

Zoom image will be displayed

Grandes Modelos de Linguagem (LLMs) são como gênios com amnésia severa. Eles podem dissertar sobre física quântica, mas esquecem seu nome no instante em que você o diz. Essa natureza stateless (sem estado) é a maior barreira para a criação de aplicações de IA verdadeiramente inteligentes e interativas.

As soluções comuns, como o RAG, tratam um sintoma (a falta de conhecimento), mas não a causa raiz: a falta de uma arquitetura cognitiva para gerenciar o estado da conversa.

É aqui que entra a Engenharia de Contexto Aumentada (ECA).

A ECA não é mais um framework RAG. É um paradigma de arquitetura, um “exoesqueleto cognitivo” para LLMs, projetado para orquestrar identidade, memória e foco de forma estruturada. Neste artigo, mergulharemos nos três pilares que permitem que a ECA resolva o problema da amnésia e do caos contextual, e mostraremos um exemplo prático de como tudo funciona.

Os Pilares da Mente de uma IA com ECA
Para que uma IA pense de forma coerente, ela precisa mais do que acesso a dados. Ela precisa de um sistema operacional. A ECA fornece esse sistema através de três conceitos fundamentais.

1. A Memória Híbrida: O Cérebro de Curto e Longo Prazo
Humanos não têm um tipo só de memória, e uma IA robusta também não deveria ter. A ECA formaliza a memória em duas camadas distintas:

🧠 Memória Semântica (Longo Prazo): É a base de conhecimento da IA. Contém fatos, regras de negócios e informações consolidadas. É o “livro de receitas” que a IA consulta para obter conhecimento factual.
✍️ Memória Episódica (Curto Prazo): É o histórico da conversa atual. Contém o que foi dito, as perguntas feitas e as respostas dadas. É o “bloco de anotações” da interação, permitindo que a IA lembre o fluxo do diálogo.
Separar essas memórias permite um gerenciamento muito mais inteligente do contexto, buscando fatos relevantes na memória de longo prazo e, ao mesmo tempo, mantendo a coerência da conversa atual.

2. A Orquestração Cognitiva: O Maestro do Contexto
Este é o coração da ECA. O Orquestrador é a peça central que, a cada interação do usuário, executa um ciclo de raciocínio:

Detecta a Intenção: Entende qual é o “domínio” ou tópico da conversa (ex: fiscal, vendas, RH).
Carrega a Identidade: Com base no domínio, carrega um perfil de comportamento específico (a “persona”). A IA pode ser um especialista fiscal rigoroso agora e um assistente de vendas amigável depois.
Busca nas Memórias: Consulta a Memória Semântica em busca de regras e fatos relevantes para a intenção detectada.
Monta o Contexto: Constrói uma “Área de Trabalho Cognitiva” em tempo real, juntando a identidade, as memórias de longo prazo relevantes e o histórico da conversa (memória episódica).
Crucialmente, o Orquestrador faz tudo isso através de um Padrão de Adaptadores. Ele não sabe se os dados vêm de arquivos JSON, de um banco de dados PostgreSQL ou de uma API. Isso torna a arquitetura incrivelmente flexível e desacoplada.

3. O Achatamento de Contexto (Flattening): A Arte da Eficiência
A “Área de Trabalho Cognitiva” que o orquestrador monta é um objeto de dados complexo e estruturado. Isso é ótimo para a lógica da aplicação, mas um LLM só lê texto. Além disso, enviar um contexto verboso e desorganizado para a API de um LLM é caro e ineficiente.

O Achatamento (Flattening) é o passo final e genial do processo. O Orquestrador pega esse estado cognitivo complexo e o “achata”, convertendo-o em uma string de texto altamente otimizada e estruturada com tags.

Pense nisso como criar um “molho de redução”: você pega uma grande quantidade de ingredientes (o estado completo) e os concentra em uma essência poderosa e rica em sabor (o prompt final), removendo tudo o que é redundante.

Este prompt achatado é o que é efetivamente enviado ao LLM, garantindo máxima relevância com o mínimo de tokens.

Da Teoria à Prática com a eca-lib
Toda essa arquitetura é implementada na eca-lib, nossa biblioteca Python open-source. Ela fornece o ECAOrchestrator e um conjunto de adaptadores para você começar a construir rapidamente.

Instalação
O projeto está em fase beta pública. Para instalar a biblioteca, use o comando abaixo, que a busca no repositório de testes TestPyPI:

pip install -i https://test.pypi.org/simple/ eca-lib
Arquitetura do Nosso Exemplo
Para nosso tutorial prático, usaremos a implementação mais simples e didática: adaptadores que leem e escrevem em arquivos JSON locais.

A arquitetura ficará assim:


Como o diagrama mostra, o ECAOrchestrator no seu código (main.py) não acessa os arquivos diretamente. Ele se comunica com as fontes de dados através dos Adaptadores, mantendo a lógica principal limpa e agnóstica à forma de armazenamento.

ECA na Prática: Um Exemplo Autocontido
Agora, vamos criar este exemplo passo a passo.

Passo 1: Crie os Arquivos de Dados
Em uma nova pasta, crie os arquivos que servirão como nossas fontes de memória, identidade e base de conhecimento.

personas.json (Define as personalidades)

[
  {
    "id": "fiscal",
    "name": "ÁBACO",
    "semantic_description": "Análise de documentos fiscais, notas fiscais, impostos.",
    "persona_config": {
      "persona": "Você é ÁBACO, um IA especialista em análise fiscal.",
      "objective": "Analisar documentos fiscais e garantir conformidade.",
      "golden_rules": ["A precisão é mais importante que a velocidade."]
    }
  },
  {
    "id": "product_catalog",
    "name": "CATÁLOGO",
    "semantic_description": "Gerenciamento de catálogo, cadastro de novos produtos, SKUs.",
    "persona_config": {
      "persona": "Você é CATÁLOGO, um IA focado em manter a integridade do cadastro.",
      "objective": "Garantir a organização e padronização do catálogo.",
      "golden_rules": ["Verifique se o produto já existe antes de cadastrar."]
    }
  }
]
memories.json (A Memória Semântica / Longo Prazo)

[
  {
    "id": "mem-uuid-101",
    "domain_id": "fiscal",
    "type": "business_rule",
    "text_content": "Notas fiscais de serviço (NFS-e) devem ter o código de serviço validado contra a lista municipal."
  },
  {
    "id": "mem-uuid-202",
    "domain_id": "fiscal",
    "type": "business_rule",
    "text_content": "Para produtos com NCM iniciado em '8471', a empresa possui um regime especial de tributação de PIS/COFINS."
  },
  {
    "id": "mem-uuid-303",
    "domain_id": "fiscal",
    "type": "business_rule",
    "text_content": "O fornecedor 'Tecno Peças Ltda' frequentemente apresenta erros no cálculo do IPI na última semana do mês."
  },
  {
    "id": "mem-uuid-456",
    "domain_id": "fiscal",
    "type": "business_rule",
    "text_content": "Toda validação de ICMS-ST deve cruzar a informação com o Protocolo ICMS vigente."
  },
  {
    "id": "mem-uuid-789",
    "domain_id": "product_catalog",
    "type": "business_rule",
    "text_content": "O último código de notebook cadastrado foi 'NB-1098'. Novos códigos devem seguir a sequência."
  }
]
nfe_78910.json (Os dados ficticio da nota fiscal)

{
  "numero": "78910",
  "data_emissao": "2025-07-08T10:00:00-03:00",
  "fornecedor_nome": "Tecno Peças Ltda",
  "fornecedor_cnpj": "12.345.678/0001-99",
  "valor_total": 4500.00,
  "origem": "MG",
  "destino": "SP",
  "produtos": [
    {
      "sku": "ROL-AX-3000",
      "nome": "Rolamento Axial 3000",
      "ncm": "8482.10.10",
      "quantidade": 100,
      "valor_unitario": 45.00
    }
  ],
  "impostos": {
    "base_calculo_icms": 4500.00,
    "valor_icms": 810.00,
    "base_calculo_ipi": 4500.00,
    "valor_ipi": 450.00,
    "icms_st": {
      "base_calculo": 4800.00,
      "valor": 432.00
    }
  }
}
Passo 2: Crie e Execute o Código Python

Na mesma pasta, crie o arquivo main.py.

# main.py (com a consulta à nota fiscal)
from datetime import datetime
from eca import (
    ECAOrchestrator,
    JSONPersonaProvider,  
    JSONMemoryProvider,  
    JSONSessionProvider
)
from eca.memory import EpisodicMemory

# --- 1. Configuração dos Adaptadores ---
persona_provider = JSONPersonaProvider(file_path='personas.json')
memory_provider = JSONMemoryProvider(
    semantic_path='memories.json',  
    episodic_path='interaction_log.json'
)
session_provider = JSONSessionProvider(file_path='user_sessions.json')

# --- 2. Instanciação do Orquestrador ---
# Apontamos o `knowledge_base_path` para a pasta atual, onde está a NF.
orchestrator = ECAOrchestrator(
    persona_provider=persona_provider,
    memory_provider=memory_provider,
    session_provider=session_provider,
    knowledge_base_path='.'
)
print("✅ Orquestrador ECA pronto para uso!")

# --- 3. Simulação da Conversa ---
user_id = "ana_paula"

def run_complete_interaction(user_input: str, turn: int):
    print("----------------------------------------------------")
    print(f"🔷 TURNO {turn} 🔷")
    print(f"🗣️  USUÁRIO (Ana Paula): '{user_input}'")
    
    context_object = orchestrator.generate_context_object(user_id, user_input)
    dynamic_context_str = orchestrator._flatten_context_to_string(context_object, user_input)
    final_prompt = orchestrator.meta_prompt_template.replace("{{DYNAMIC_CONTEXT}}", dynamic_context_str)

    print("\n✨ PROMPT 'ACHATADO' GERADO PELA ECA: ✨")
    print(final_prompt)
    
    fake_llm_response = f"Resposta simulada para '{user_input[:25]}...'"
    print(f"\n🤖 RESPOSTA (Simulada do LLM): '{fake_llm_response}'")

    interaction_to_log = EpisodicMemory(
        user_id=user_id,
        domain_id=context_object.current_focus,
        user_input=user_input,
        assistant_output=fake_llm_response,
        timestamp=datetime.now().isoformat()
    )
    memory_provider.log_interaction(interaction_to_log)
    session_provider.save_workspace(context_object)
    print(f"\n[INFO: Turno {turn} salvo na memória e sessão.]")
    print("----------------------------------------------------\n")

# Limpa os logs para uma execução limpa
import os
if os.path.exists("interaction_log.json"): os.remove("interaction_log.json")
if os.path.exists("user_sessions.json"): os.remove("user_sessions.json")

# --- TURNO 1: Foco em Catálogo de Produtos ---
run_complete_interaction(
    user_input="Preciso de ajuda para cadastrar um novo notebook no sistema.",
    turn=1
)

# --- TURNO 2: Troca de Contexto para Fiscal (com consulta a dados) ---
run_complete_interaction(
    user_input="Ok, mudei de ideia. Por favor, analise a Nota Fiscal de Entrada nº 78910.",
    turn=2
)

# --- TURNO 3: Retorno ao Contexto de Catálogo ---
run_complete_interaction(
    user_input="Certo, voltando ao cadastro de produto. Sobre aquele notebook que mencionei, qual é o próximo código que devo usar?",
    turn=3
)
Para executar:

python main.py
O Resultado: A Orquestração em Ação
O output do script é a demonstração física dos conceitos da ECA:

✅ Orquestrador ECA pronto para uso!
----------------------------------------------------
🔷 TURNO 1 🔷
🗣️  USUÁRIO (Ana Paula): 'Preciso de ajuda para cadastrar um novo notebook no sistema.'

✨ PROMPT 'ACHATADO' GERADO PELA ECA: ✨
### ECA - INSTRUÇÃO MESTRA DE RACIOCÍNIO ###

Você é um modelo de linguagem avançado operando como um agente especialista dentro da estrutura ECA (Engenharia de Contexto Aumentada). Sua resposta deve ser gerada seguindo estritamente as informações de contexto e o processo de raciocínio descritos abaixo.

[BEGIN_CONTEXT]
[TIMESTAMP:2025-07-25T20:24:13.757100]
[IDENTITY:CATÁLOGO|PRODUCT_CATALOG]
[OBJECTIVE:Garantir a organização e padronização do catálogo.]
[GOLDEN_RULES:\n- Verifique se o produto já existe antes de cadastrar.]
[USER:ana_paula]
[RECENT_HISTORY:\nUser: Preciso de ajuda para cadastrar um novo notebook no sistema.\nAssistant: Resposta simulada do LLM para a sua pergunta sobre 'Preciso de ajuda para cad...'\nUser: Preciso de ajuda para cadastrar um novo notebook no sistema.\nAssistant: Resposta simulada do LLM para a sua pergunta sobre 'Preciso de ajuda para cad...'\nUser: Certo, voltando ao **cadastro de produto**. Sobre aquele notebook que mencionei, qual é o próximo código que devo usar?\nAssistant: Resposta simulada do LLM para a sua pergunta sobre 'Certo, voltando ao **cada...']\n[CURRENT_SESSION:Initiating new task.]
[ACTIVE_TASK:Analisando a solicitação 'Preciso de ajuda para cadastrar um novo notebook n...' para o domínio 'product_catalog'.]
[RELEVANT_MEMORY_1:O último código de notebook cadastrado foi 'NB-1098'. Novos códigos devem seguir a sequência.]
[USER_INPUT: "Preciso de ajuda para cadastrar um novo notebook no sistema."]
[END_CONTEXT]

**Processo de Raciocínio Obrigatório:**

1.  **Autoanálise:** Revise suas tags **[IDENTITY], [OBJECTIVE] e [GOLDEN_RULES]**. Isso define quem você é, o que você deve alcançar e as restrições sob as quais deve operar.

2.  **Consciência Situacional:** Analise as tags **[USER], [CURRENT_SESSION], [ACTIVE_TASK] e [TIMESTAMP]**. Isso define com quem você está falando, o estado da conversa, seu objetivo imediato e o momento atual.

3.  **Consulta à Memória:** Analise todas as tags [RELEVANT_MEMORY_#]. Estes são insights cruciais do passado. Como eles se aplicam à entrada atual do usuário?

4.  **Análise de Dados:** Se a tag [INPUT_DATA] estiver presente, examine seu conteúdo cuidadosamente. Esta é a carga de dados primária para sua tarefa atual.

5.  **Síntese e Planejamento:** Com base em todo o contexto acima, formule um plano de ação interno passo a passo para endereçar a [USER_INPUT]. Não exponha este plano na resposta. Considere se sua persona exige que você faça perguntas de esclarecimento antes de fornecer uma resposta direta.

6.  **Formulação da Resposta:** Execute seu plano. Gere a resposta final, garantindo que ela incorpore perfeitamente sua persona da tag [IDENTITY], siga suas [GOLDEN_RULES] e responda diretamente à solicitação do usuário usando todo o contexto relevante.
    **IMPORTANTE: Sua resposta final deve ser limpa e direta para o usuário. NUNCA mencione ou cite a estrutura do seu contexto (palavras como 'tags', 'memória relevante', '[IDENTITY]', etc.) na sua resposta.**

**Sua Resposta Final:**

🤖 RESPOSTA (Simulada do LLM): 'Resposta simulada para 'Preciso de ajuda para cad...''

[INFO: Turno 1 salvo na memória e sessão.]
----------------------------------------------------

----------------------------------------------------
🔷 TURNO 2 🔷
🗣️  USUÁRIO (Ana Paula): 'Ok, mudei de ideia. Por favor, analise a Nota Fiscal de Entrada nº 78910.'

✨ PROMPT 'ACHATADO' GERADO PELA ECA: ✨
### ECA - INSTRUÇÃO MESTRA DE RACIOCÍNIO ###

Você é um modelo de linguagem avançado operando como um agente especialista dentro da estrutura ECA (Engenharia de Contexto Aumentada). Sua resposta deve ser gerada seguindo estritamente as informações de contexto e o processo de raciocínio descritos abaixo.

[BEGIN_CONTEXT]
[TIMESTAMP:2025-07-25T20:24:13.757914]
[IDENTITY:ÁBACO|FISCAL]
[OBJETIVO:Analisar documentos fiscais e garantir conformidade.] 
[GOLDEN_RULES:\n- Precisão é mais importante que velocidade.] 
[USER:ana_paula] 
[RECENT_HISTORY:\nUser: Ok, mudei de ideia. Antes, preciso verificar os impostos de uma nota fiscal de serviço. \nAssistant: Resposta simulada do LLM para sua pergunta sobre 'Ok, mudei de ideia. Antes...' \nUser: Ok, mudei de ideia. Antes, preciso verificar os impostos de uma nota fiscal de serviço. \nAssistant: Resposta simulada do LLM para sua pergunta sobre 'Ok, mudei de ideia. Antes...' ]\n[CURRENT_SESSION:Iniciando nova tarefa.] 
[ACTIVE_TASK:Analisando a solicitação 'Ok, mudei de ideia. Por favor, analise a Nota Fisc...' para o domínio 'fiscal' .] 
[RELEVANT_MEMORY_1:Notas fiscais de serviço (NFS-e) devem ter o código de serviço validado contra a lista municipal.] 
[RELEVANT_MEMORY_2:Para produtos com NCM iniciado em '8471' , a empresa possui um regime especial de tributação de PIS/COFINS.] 
[RELEVANT_MEMORY_3:O fornecedor 'Tecno Peças Ltda' frequentemente apresenta erros no cálculo do IPI na última semana do mês.] 
[INPUT_DATA: { "numero" : "78910" , "data_emissao" : "2025-07-08T10:00:00-03:00" , "fornecedor_nome" : "Tecno Peças Ltda" , "fornecedor_cnpj" : "12.345.678/0001-99" , "valor_total" : 4500.0 , "origem" : "MG" , "destino" : "SP" , "produtos" : [{ "sku" : "ROL-AX-3000" , "nome" : "Rolamento Axial 3000" , "ncm" : "8482.10.10" , "quantidade" : 100 , "valor_unitario" : 45.0 }], "impostos" : { "base_calculo_icms" : 4500.0 , "valor_icms" : 810.0 , "base_calculo_ipi" : 4500.0 ,"valor_ipi": 450.0, "icms_st": {"base_calculo": 4800.0, "valor": 432.0}}}]
[USER_INPUT: "Ok, mudei de ideia. Por favor, analise a Nota Fiscal de Entrada nº 78910."]
[END_CONTEXT]

**Processo de Raciocínio Obrigatório:**

1.  **Autoanálise:** Revise suas tags **[IDENTITY], [OBJECTIVE] e [GOLDEN_RULES]**. Isso define quem você é, o que você deve alcançar e as restrições sob as quais deve operar.

2.  **Consciência Situacional:** Analise as tags **[USER], [CURRENT_SESSION], [ACTIVE_TASK] e [TIMESTAMP]**. Isso define com quem você está falando, o estado da conversa, seu objetivo imediato e o momento atual.

3.  **Consulta à Memória:** Analise todas as tags [RELEVANT_MEMORY_#]. Estes são insights cruciais do passado. Como eles se aplicam à entrada atual do usuário?

4.  **Análise de Dados:** Se a tag [INPUT_DATA] estiver presente, examine seu conteúdo cuidadosamente. Esta é a carga de dados primária para sua tarefa atual.

5.  **Síntese e Planejamento:** Com base em todo o contexto acima, formule um plano de ação interno passo a passo para endereçar a [USER_INPUT]. Não exponha este plano na resposta. Considere se sua persona exige que você faça perguntas de esclarecimento antes de fornecer uma resposta direta.

6.  **Formulação da Resposta:** Execute seu plano. Gere a resposta final, garantindo que ela incorpore perfeitamente sua persona da tag [IDENTITY], siga suas [GOLDEN_RULES] e responda diretamente à solicitação do usuário usando todo o contexto relevante.
    **IMPORTANTE: Sua resposta final deve ser limpa e direta para o usuário. NUNCA mencione ou cite a estrutura do seu contexto (palavras como 'tags', 'memória relevante', '[IDENTITY]', etc.) na sua resposta.**

**Sua Resposta Final:**

🤖 RESPOSTA (Simulada do LLM): 'Resposta simulada para 'Ok, mudei de ideia. Por f...''

[INFO: Turno 2 salvo na memória e sessão.]
----------------------------------------------------

----------------------------------------------------
🔷 TURNO 3 🔷
🗣️  USUÁRIO (Ana Paula): 'Certo, voltando ao cadastro de produto. Sobre aquele notebook que mencionei, qual é o próximo código que devo usar?'

✨ PROMPT 'ACHATADO' GERADO PELA ECA: ✨
### ECA - INSTRUÇÃO MESTRA DE RACIOCÍNIO ###

Você é um modelo de linguagem avançado operando como um agente especialista dentro da estrutura ECA (Engenharia de Contexto Aumentada). Sua resposta deve ser gerada seguindo estritamente as informações de contexto e o processo de raciocínio descritos abaixo.

[BEGIN_CONTEXT]
[TIMESTAMP:2025-07-25T20:24:13.758760]
[IDENTITY:CATÁLOGO|PRODUCT_CATALOG]
[OBJECTIVE:Garantir a organização e padronização do catálogo.]
[GOLDEN_RULES:\n- Verifique se o produto já existe antes de cadastrar.]
[USER:ana_paula]
[RECENT_HISTORY:\nUser: Preciso de ajuda para cadastrar um novo notebook no sistema.\nAssistant: Resposta simulada do LLM para a sua pergunta sobre 'Preciso de ajuda para cad...'\nUser: Preciso de ajuda para cadastrar um novo notebook no sistema.\nAssistant: Resposta simulada do LLM para a sua pergunta sobre 'Preciso de ajuda para cad...'\nUser: Certo, voltando ao **cadastro de produto**. Sobre aquele notebook que mencionei, qual é o próximo código que devo usar?\nAssistant: Resposta simulada do LLM para a sua pergunta sobre 'Certo, voltando ao **cada...'\nUser: Preciso de ajuda para cadastrar um novo notebook no sistema.\nAssistant: Resposta simulada para 'Preciso de ajuda para cad...']\n[CURRENT_SESSION:Initiating new task.]
[ACTIVE_TASK:Analisando a solicitação 'Certo, voltando ao cadastro de produto. Sobre aque...' para o domínio 'product_catalog'.]
[RELEVANT_MEMORY_1:O último código de notebook cadastrado foi 'NB-1098'. Novos códigos devem seguir a sequência.]
[USER_INPUT: "Certo, voltando ao cadastro de produto. Sobre aquele notebook que mencionei, qual é o próximo código que devo usar?"]
[END_CONTEXT]

**Processo de Raciocínio Obrigatório:**

1.  **Autoanálise:** Revise suas tags **[IDENTITY], [OBJECTIVE] e [GOLDEN_RULES]**. Isso define quem você é, o que você deve alcançar e as restrições sob as quais deve operar.

2.  **Consciência Situacional:** Analise as tags **[USER], [CURRENT_SESSION], [ACTIVE_TASK] e [TIMESTAMP]**. Isso define com quem você está falando, o estado da conversa, seu objetivo imediato e o momento atual.

3.  **Consulta à Memória:** Analise todas as tags [RELEVANT_MEMORY_#]. Estes são insights cruciais do passado. Como eles se aplicam à entrada atual do usuário?

4.  **Análise de Dados:** Se a tag [INPUT_DATA] estiver presente, examine seu conteúdo cuidadosamente. Esta é a carga de dados primária para sua tarefa atual.

5.  **Síntese e Planejamento:** Com base em todo o contexto acima, formule um plano de ação interno passo a passo para endereçar a [USER_INPUT]. Não exponha este plano na resposta. Considere se sua persona exige que você faça perguntas de esclarecimento antes de fornecer uma resposta direta.

6.  **Formulação da Resposta:** Execute seu plano. Gere a resposta final, garantindo que ela incorpore perfeitamente sua persona da tag [IDENTITY], siga suas [GOLDEN_RULES] e responda diretamente à solicitação do usuário usando todo o contexto relevante.
    **IMPORTANTE: Sua resposta final deve ser limpa e direta para o usuário. NUNCA mencione ou cite a estrutura do seu contexto (palavras como 'tags', 'memória relevante', '[IDENTITY]', etc.) na sua resposta.**

**Sua Resposta Final:**

🤖 RESPOSTA (Simulada do LLM): 'Resposta simulada para 'Certo, voltando ao cadast...''

[INFO: Turno 3 salvo na memória e sessão.]
----------------------------------------------------
Análise do Turno 1 e 3: Permanecem os mesmos, demonstrando a criação de contexto e a capacidade de retornar a um estado pausado.

Análise do Turno 2 (A Cereja do Bolo): O prompt gerado para o Turno 2 agora é espetacular. Além de mudar a identidade para [IDENTITY:ÁBACO|FISCAL] e carregar as memórias semânticas relevantes, ele agora contém uma nova tag crucial:

[INPUT_DATA: {"numero": "78910", "data_emissao": "2025-07-08T10:00:00-03:00", ...}]

Isto prova o pilar “Orquestração Desacoplada” em ação - O Orquestrador:

Analisou a entrada do usuário: "analise a Nota Fiscal de Entrada nº 78910".
Detectou a palavra-chave “78910” (esta lógica pode ser customizada).
Buscou no knowledge_base_path por um arquivo correspondente (nfe_78910.json).
Carregou seu conteúdo e o injetou diretamente no contexto do LLM.
O LLM agora tem tudo o que você precisa para executar a tarefa: sua identidade de especialista, as regras de negócios da memória semântica e os dados brutos e específicos da nota fiscal em questão.

Finalizando
A Engenharia de Contexto Aumentada (ECA) resolve os problemas de amnésia e caos contextual não com um truque, mas com uma arquitetura sólida. Ao orquestrar identidades, gerenciar memórias de curto e longo prazo e otimizar o prompt final por meio de achatamento, a ECA fornece a estrutura necessária para construir a próxima geração de aplicativos de IA: aqueles que não apenas falam, mas lembram, focam e raciocinam.

Se você gostou desta abordagem e quer colocar a mão na massa, aqui estão os links essenciais:

➡️ Execute o exemplo deste artigo: O código-fonte Acesse o código do exemplo no GitHub completo do tutorial que acabamos de construir, incluindo todos os arquivos .py e .json, está disponível para você clonar e rodar imediatamente .
➡️ Apoie o projeto: Visite o repositório da eca-lib no GitHub . Explore o código e, se gostar do que viu, deixe sua estrelinha (⭐) ! Sua contribuição, seja com código, ideias ou reportando issues, é muito bem-vinda.
➡️ Mergulhe na teoria: Para um entendimento profundo dos conceitos e diagramas detalhados, leia nosso Leia nosso whitepaper de arquitetura.
➡️ Conecte-se comigo: Vamos trocar ideias sobre IA, LLMs e arquitetura de software. Siga-me no LinkedIn para acompanhar as novidades.
