from jinja2 import Environment, FileSystemLoader
import glob
import json

TEMPLATES_DIR = '.'

def main():
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
      extensions=['jinja2.ext.with_'])

    # We load the data.
    CONTEXT = {}
    for json_file in glob.glob('_data/*.json'):
      data = json.load(open(json_file))
      context_name = json_file.split('/')[-1].split('.')[0].lower()
      CONTEXT[context_name] = data
    
    # To follow references in Jinja2 templates, e.g.
    # {{member.affiliations[0] | deref('orgs', 'website') }}
    def deref(id, table, attribute):
      for item in CONTEXT[table]:
        if item['__id__'] == id:
          if attribute in item:
            return item[attribute]
          else:
            None
      return None 

    env.filters['deref'] = lambda x, y, z: deref(x,y,z)


    NAVIGATION = [ ('About', 'about.html'),
                   ('Approach', 'approach.html'),
                   ('Projects', 'projects.html') ]

    for page in ['index', 'resources', 'projects', 'approach', 'about']:
        template = env.get_template('%s.html' % page)
        html = template.render(site=CONTEXT, nav=NAVIGATION)
        with open('_site/%s.html' % page, 'w') as f:
          f.write(html)
        f.close()

if __name__ == '__main__':
  main()

