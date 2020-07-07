from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = '.'

def main():
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
      extensions=['jinja2.ext.with_'])
    env.filters['skolem'] = lambda x: x.lower().replace(' ', '_').replace('"','')

    for page in ['index', 'resources', 'projects', 'approach', 'about']:
        template = env.get_template('%s.html' % page)
        html = template.render()
        with open('_site/%s.html' % page, 'w') as f:
          f.write(html)
        f.close()

if __name__ == '__main__':
  main()

