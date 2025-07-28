import os
import re
from datetime import datetime
from pathlib import Path


def parse_task_file(file_path):
    """Lê um arquivo de tarefa e analisa o front matter YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    front_matter = {}
    # Regex para extrair o bloco ---...---
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None

    yaml_content = match.group(1)
    for line in yaml_content.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if value == 'null' or not value:
                front_matter[key] = None
            elif key in ['estimated_hours']:
                front_matter[key] = float(value)
            else:
                front_matter[key] = value

    # Extrai a descrição do corpo do markdown
    body_content = content[match.end():].strip()
    front_matter['description'] = body_content

    return front_matter


def generate_dashboard():
    """Gera o dashboard HTML a partir dos arquivos de tarefa."""
    project_root = Path(__file__).parent.parent
    tasks_dir = project_root / 'docs' / '4_tasks'
    template_path = project_root / 'scripts' / 'dashboard_template.html'
    output_path = project_root / 'progress.html'

    tasks = []
    for filename in os.listdir(tasks_dir):
        if filename.endswith('.md'):
            task_data = parse_task_file(tasks_dir / filename)
            if task_data:
                tasks.append(task_data)

    # Ordena as tarefas pelo ID
    tasks.sort(key=lambda x: x.get('id', ''))

    # --- Geração dos Componentes HTML ---

    # Kanban
    kanban_cols = {'TODO': '', 'IN_PROGRESS': '', 'DONE': ''}
    for task in tasks:
        status = task.get('status', 'TODO')
        card_class = f"kanban-card status-{status}"
        card_html = f"""
        <div class="{card_class}">
            <h4>{task.get('title', 'N/A')}</h4>
            <p><strong>ID:</strong> {task.get('id', 'N/A')}</p>
            <p><strong>Horas:</strong> {task.get('estimated_hours', 0)}h</p>
        </div>
        """
        if status in kanban_cols:
            kanban_cols[status] += card_html

    # Tabela
    table_rows_html = ''
    for task in tasks:
        table_rows_html += f"""
        <tr>
            <td>{task.get('id', 'N/A')}</td>
            <td>{task.get('title', 'N/A')}</td>
            <td>{task.get('status', 'N/A')}</td>
            <td>{task.get('estimated_hours', 0)}h</td>
            <td>{task.get('start_time', 'N/A')}</td>
            <td>{task.get('end_time', 'N/A')}</td>
        </tr>
        """

    # Gráfico de Gantt
    gantt_chart_code = (
        "gantt\n    dateFormat  YYYY-MM-DD\n    "
        "title       Cronograma do Projeto Frank-Daemon\n\n"
    )
    for task in tasks:
        task_id = task.get('id', 'Task').replace('_', ' ')
        status = task.get('status', 'TODO')
        # Para o Gantt, precisamos de datas. Vamos simular por enquanto.
        # A lógica real usaria os campos start_time e end_time.
        start_date = datetime.now().strftime('%Y-%m-%d')
        # Simula 1 dia de duração para cada 8h de estimativa
        duration = int(task.get('estimated_hours', 8) / 8 * 1)
        gantt_chart_code += (
            f"    section {task_id}\n    {task.get('title', 'N/A')} "
            f":{status.lower()}, {start_date}, {duration}d\n"
        )

    # Métricas
    total_tasks = len(tasks)
    done_tasks = sum(1 for t in tasks if t.get('status') == 'DONE')
    total_hours = sum(t.get('estimated_hours', 0) for t in tasks)
    progress = (done_tasks / total_tasks * 100) if total_tasks > 0 else 0

    metrics_html = f"""
    <div class="metric"><h3>Total de Tarefas</h3><p>{total_tasks}</p></div>
    <div class="metric"><h3>Tarefas Concluídas</h3><p>{done_tasks}</p></div>
    <div class="metric"><h3>Progresso</h3><p>{progress:.1f}%</p></div>
    <div class="metric"><h3>Total de Horas</h3><p>{total_hours}h</p></div>
    """

    # --- Montagem Final ---
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    dashboard_content = template_content.replace('{{kanban_todo}}', kanban_cols['TODO'])
    dashboard_content = dashboard_content.replace(
        '{{kanban_inprogress}}', kanban_cols['IN_PROGRESS']
    )
    dashboard_content = dashboard_content.replace('{{kanban_done}}', kanban_cols['DONE'])
    dashboard_content = dashboard_content.replace('{{task_table_rows}}', table_rows_html)
    dashboard_content = dashboard_content.replace(
        '{{gantt_chart}}', gantt_chart_code
    )
    dashboard_content = dashboard_content.replace('{{metrics}}', metrics_html)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(dashboard_content)

    print(f"Dashboard gerado com sucesso em: {output_path}")


if __name__ == "__main__":
    generate_dashboard()
