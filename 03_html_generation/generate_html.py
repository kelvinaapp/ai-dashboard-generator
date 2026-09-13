import pandas as pd
from jinja2 import Environment, FileSystemLoader
import json

def generate_dashboard(data_path, template_path, output_path):
    # Membaca data siap pakai
    df = pd.read_excel(data_path)
    # Mengubah dataframe menjadi list of dictionary agar mudah dibaca Javascript
    data_dict = df.to_dict(orient='records')
    
    # Setup Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    
    # Proses render dan simpan ke file
    html_out = template.render(dashboard_data=data_dict)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_out)

if __name__ == "__main__":
    generate_dashboard('../02_schema_to_dashboard_data/output/data_ready.xlsx', 'template.html', 'output/dashboard_final.html')